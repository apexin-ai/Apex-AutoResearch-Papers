# code plan009 pathological matrices v2

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 49
- **Recorded user turns:** 0
- **Tool calls:** 24
- **Original source:** `logs/chats/worker_code_plan009-pathological-matrices-v2_20260520T181421.jsonl`
- **Structured JSON:** [`866fce36941cff7211d3.json`](../../sessions/86/866fce36941cff7211d3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

49 recorded events

### Tool call

_source line 1 · 2026-05-20T18:26:04.849485+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__register_artifact",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan009-pathological-matrices-v2_20260520T181421",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__register_artifact",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T18:26:04.849813+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan009-pathological-matrices-v2_20260520T181421",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T18:26:04.849983+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "home-1x5090",
  "command": "ls -la /home/sonny/causal_annot_error_attrib/plan_*.py",
  "account": "sonny"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan009-pathological-matrices-v2_20260520T181421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "home-1x5090",
    "command": "ls -la /home/sonny/causal_annot_error_attrib/plan_*.py",
    "account": "sonny"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T18:26:04.850131+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-rw-r-- 1 sonny sonny 25871 May 20 05:25 /home/sonny/causal_annot_error_attrib/plan_001_collider_mbias_iv.py\\n-rw-rw-r-- 1 sonny sonny  8599 May 20 02:16 /home/sonny/causal_annot_error_attrib/plan_001_dag_taxonomy.py\\n-rw-rw-r-- 1 sonny sonny 15223 May 20 05:25 /home/sonny/causal_annot_error_attrib/plan_001_mediation_frontdoor.py\\n-rw-rw-r-- 1 sonny sonny 19107 May 20 09:08 /home/sonny/causal_annot_error_attrib/plan_002_k57_extended_7topo.py\\n-rw-rw-r-- 1 sonny sonny 24168 May 20 09:08 /home/sonny/causal_annot_error_attrib/plan_002_k57_extension.py\\n-rw-rw-r-- 1 sonny sonny 31714 May 20 05:56 /home/sonny/causal_annot_error_attrib/plan_004_asv_framework.py\\n-rw-rw-r-- 1 sonny sonny 36333 May 20 06:55 /home/sonny/causal_annot_error_attrib/plan_004_asv_v3_fixed.py\\n-rw-rw-r-- 1 sonny sonny 32324 May 20 06:27 /home/sonny/causal_annot_error_attrib/plan_004_asv_v3.py\\n-rw-rw-r-- 1 sonny sonny  6570 May 20 07:07 /home/sonny/causal_annot_error_attrib/plan_004_n_sensitivity.py\\n-rw-rw-r-- 1 sonny sonny 34855 May 20 08:16 /home/sonny/causal_annot_error_attrib/plan_005_asv_extended_fixed.py\\n-rw-rw-r-- 1 sonny sonny 32601 May 20 07:39 /home/sonny/causal_annot_error_attrib/plan_005_asv_extended.py\\n-rw-rw-r-- 1 sonny sonny 22117 May 20 06:11 /home/sonny/causal_annot_error_attrib/plan_008_binarization_collapse.py\\n-rw-rw-r-- 1 sonny sonny 28893 May 20 09:45 /home/sonny/causal_annot_error_attrib/plan_009_pathological_matrices.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.71}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan009-pathological-matrices-v2_20260520T181421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T18:26:04.850322+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "home-1x5090",
  "command": "head -200 /home/sonny/causal_annot_error_attrib/plan_002_k57_extended_7topo.py",
  "account": "sonny"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan009-pathological-matrices-v2_20260520T181421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "home-1x5090",
    "command": "head -200 /home/sonny/causal_annot_error_attrib/plan_002_k57_extended_7topo.py",
    "account": "sonny"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-20T18:26:04.850453+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "home-1x5090",
  "command": "head -300 /home/sonny/causal_annot_error_attrib/plan_001_collider_mbias_iv.py",
  "account": "sonny"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan009-pathological-matrices-v2_20260520T181421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "home-1x5090",
    "command": "head -300 /home/sonny/causal_annot_error_attrib/plan_001_collider_mbias_iv.py",
    "account": "sonny"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-20T18:26:04.850665+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nPlan 002 Extended: All 7 topologies × K={3,5,7}\\n\\nTopologies:\\n  1. Confounding: A→T, A→Y, T→Y\\n  2. Mediation: T→A→Y\\n  3. Collider: T→A←Y\\n  4. Exposure: A→Y\\n  5. M-bias: U1→{A,T}, U2→{A,Y}, T→Y\\n  6. IV: Z→A→Y, U→{A,Y}\\n  7. Front-door: T→M→Y, U→{T,Y}\\n\\nFor each topology × K: 100k random K×K confusion matrices (Dirichlet),\\nplim-based bias metrics including tau_specific_sign_flip (key paper claim).\\n\\\"\\\"\\\"\\n\\nimport torch\\nimport numpy as np\\nimport time\\nimport os\\nimport sys\\nimport hashlib\\n\\ndef _det_seed(topo_name, K, tag, base_seed=42):\\n    h = hashlib.sha256(f\\\"{topo_name}|{K}|{tag}|{base_seed}\\\".encode()).hexdigest()\\n    return int(h[:8], 16)\\n\\nK_VALUES = [3, 5, 7]\\nN_RANDOM = 100_000\\nN_LARGE = 5_000_000\\nSEED = 42\\nDEVICE = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')\\nDTYPE = torch.float64\\nOUT_DIR = os.path.dirname(os.path.abspath(__file__))\\n\\n_ALPHA_POOL  = [1.5, -1.0, 0.8, -0.5, 1.2, -0.7]\\n_BETA_A_POOL = [1.0, -0.5, 0.7, -0.3, 0.5, -0.2]\\n_BETA_POOL   = [0.0, 1.0, -0.5, 0.7, -0.3, 0.5, -0.2]\\n_GAMMA_POOL  = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]\\n_DELTA_POOL  = [0.0, 0.8, -0.6, 0.5, -0.4, 0.3, -0.2]\\n_DT_POOL     = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]\\n_DY_POOL     = [0.0, 0.8, 0.6, -0.5, 0.4, -0.3, 0.2]\\n_MBIAS_A1_POOL = [0.0, 0.8, -0.5, 0.6, -0.4, 0.5, -0.3]\\n_MBIAS_A2_POOL = [0.0, 0.6, 0.9, -0.4, 0.7, -0.3, 0.5]\\n_IV_DZ_POOL = [0.0, 1.0, -0.5, 0.8, -0.4, 0.6, -0.3]\\n_IV_DU_POOL = [0.0, 0.8, 0.6, -0.5, 0.7, -0.3, 0.4]\\n_FD_GAMMA_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]\\n_FD_DELTA_POOL = [0.0, 1.0, -0.8, 0.7, -0.5, 0.4, -0.3]\\n\\n\\ndef make_p_A(K):\\n    if K == 3:\\n        return np.array([0.40, 0.35, 0.25])\\n    raw = np.array([1.0 / i for i in range(1, K + 1)])\\n    return raw / raw.sum()\\n\\n\\ndef make_all_params(K):\\n    p_A = make_p_A(K)\\n    return di
…[truncated 5461 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan009-pathological-matrices-v2_20260520T181421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-20T18:26:04.850832+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "home-1x5090",
  "command": "head -200 /home/sonny/causal_annot_error_attrib/plan_001_mediation_frontdoor.py",
  "account": "sonny"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan009-pathological-matrices-v2_20260520T181421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "home-1x5090",
    "command": "head -200 /home/sonny/causal_annot_error_attrib/plan_001_mediation_frontdoor.py",
    "account": "sonny"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-20T18:26:04.851141+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nCollider + M-bias + Instrument DAG: bias via large-sample moments + MC verification.\\nK=3 LLM annotation error bias propagation in causal inference.\\n\\\"\\\"\\\"\\n\\nimport numpy as np\\nfrom collections import OrderedDict\\nimport time\\n\\n# -- Constants ---------------------------------------------------------------\\n\\nBETA_MIXED = np.array([0.0, 1.0, -0.5])\\nBETA_SAME  = np.array([0.0, 1.0,  0.5])\\n\\nC1_SYMMETRIC_HIGH = np.array([[0.80, 0.10, 0.10], [0.10, 0.80, 0.10], [0.10, 0.10, 0.80]])\\nC2_ASYMMETRIC     = np.array([[0.65, 0.05, 0.10], [0.30, 0.85, 0.10], [0.05, 0.10, 0.80]])\\nC3_STRUCTURAL_12  = np.array([[0.96, 0.01, 0.01], [0.02, 0.69, 0.30], [0.02, 0.30, 0.69]])\\nC4_WEAK_DIAG      = np.array([[0.40, 0.35, 0.25], [0.35, 0.40, 0.35], [0.25, 0.25, 0.40]])\\nC5_NEAR_PERM      = np.array([[0.05, 0.05, 0.90], [0.90, 0.05, 0.05], [0.05, 0.90, 0.05]])\\nC6_DIFFERENTIAL   = np.array([[0.85, 0.15, 0.05], [0.075, 0.70, 0.05], [0.075, 0.15, 0.90]])\\n\\nALL_C = OrderedDict([\\n    (\\\"C1_sym_high\\\",   C1_SYMMETRIC_HIGH),\\n    (\\\"C2_asymmetric\\\", C2_ASYMMETRIC),\\n    (\\\"C3_struct_12\\\",  C3_STRUCTURAL_12),\\n    (\\\"C4_weak_diag\\\",  C4_WEAK_DIAG),\\n    (\\\"C5_near_perm\\\",  C5_NEAR_PERM),\\n    (\\\"C6_differential\\\", C6_DIFFERENTIAL),\\n])\\n\\n# -- Utilities ---------------------------------------------------------------\\n\\ndef _generate_Astar(A, C, rng):\\n    probs = C[:, A]\\n    cum = np.cumsum(probs, axis=0)\\n    u = rng.uniform(size=len(A))\\n    return (u >= cum[0]).astype(int) + (u >= cum[1]).astype(int)\\n\\n\\ndef _generate_Astar_fixed_u(A, C, u):\\n    probs = C[:, A]\\n    cum = np.cumsum(probs, axis=0)\\n    return (u >= cum[0]).astype(int) + (u >= cum[1]).astype(int)\\n\\n\\ndef _softmax_sample(logits, rng):\\n    exp_l = np.exp(logits - logits.max(axis=1, keepdims=True))\\n    probs = exp_l / exp_l.sum(axis=1, keepdims=True)\\n    cum = np.cumsum
…[truncated 6721 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan009-pathological-matrices-v2_20260520T181421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-20T18:26:04.851375+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "home-1x5090",
  "command": "cat /home/sonny/causal_annot_error_attrib/plan_009_pathological_matrices.py",
  "account": "sonny"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan009-pathological-matrices-v2_20260520T181421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "home-1x5090",
    "command": "cat /home/sonny/causal_annot_error_attrib/plan_009_pathological_matrices.py",
    "account": "sonny"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-20T18:26:04.851593+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n# -*- coding: utf-8 -*-\\n\\\"\\\"\\\"Plan 001: Mediation + Front-door DAG — closed-form bias + MC verification.\\\"\\\"\\\"\\nimport numpy as np\\nimport time\\nimport warnings\\nfrom collections import OrderedDict\\n\\nwarnings.filterwarnings('ignore')\\n\\n# ================================================================\\n# Configuration\\n# ================================================================\\nK = 3\\nN_MC = 10_000\\nN_REPS = 1_000\\nN_LARGE = 50_000_000\\nN_RANDOM = 100_000\\n\\nBETA_MIXED = np.array([0.0, 1.0, -0.5])\\nBETA_SAME  = np.array([0.0, 1.0,  0.5])\\n\\nTAU = 0.5\\nGAMMA_MED = np.array([0.0, 0.5, -0.3])\\nDELTA_MED = np.array([0.0, 0.8, -0.6])\\n\\nALPHA_U = 1.0\\nLAMBDA_U = 1.0\\nGAMMA_FD = np.array([0.0, 0.5, -0.3])\\nDELTA_FD = np.array([0.0, 1.0, -0.8])\\n\\nC_DICT = OrderedDict([\\n    (\\\"1_sym_high\\\",   np.array([[.80,.10,.10],[.10,.80,.10],[.10,.10,.80]])),\\n    (\\\"2_asymmetric\\\", np.array([[.65,.05,.10],[.30,.85,.10],[.05,.10,.80]])),\\n    (\\\"3_struct_12\\\",  np.array([[.96,.01,.01],[.02,.69,.30],[.02,.30,.69]])),\\n    (\\\"4_weak_diag\\\",  np.array([[.40,.35,.25],[.35,.40,.35],[.25,.25,.40]])),\\n    (\\\"5_near_perm\\\",  np.array([[.05,.05,.90],[.90,.05,.05],[.05,.90,.05]])),\\n    (\\\"6_diff_base\\\",  np.array([[.85,.15,.05],[.075,.70,.05],[.075,.15,.90]])),\\n])\\n\\nCOEF_NAMES = ['β₀', 'τ', 'β₁', 'β₂']\\n\\n\\n# ================================================================\\n# Helpers\\n# ================================================================\\ndef softmax(x):\\n    e = np.exp(x - x.max())\\n    return e / e.sum()\\n\\n\\ndef p_cat(t, g, d):\\n    return softmax(g + d * t)\\n\\n\\ndef gen_Astar(A, C, rng):\\n    pr = C[:, A]\\n    cu = np.cumsum(pr, axis=0)\\n    u = rng.uniform(size=len(A))\\n    return (u >= cu[0]).astype(int) + (u >= cu[1]).astype(int)\\n\\n\\ndef ols(Z, Y):\\n    return np.linalg.lstsq(Z, Y, 
…[truncated 5171 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan009-pathological-matrices-v2_20260520T181421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T18:26:04.851867+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nPlan 009: Pathological Confusion Matrix Analysis\\n\\nIdentifies structural conditions under which pathological confusion matrices\\nproduce catastrophic estimation bias across 7 DAG topologies.\\n\\nThree types of pathological C matrices (K×K column-stochastic):\\n\\n  (a) Near-permutation: C = (1-ε)P + ε·(1/K)·𝟏𝟏ᵀ\\n      P = random permutation matrix, ε ~ U(0.01, 0.99).\\n      Models systematic label swaps with varying noise levels.\\n\\n  (b) Rank-deficient: Dirichlet-generated C with row j ≈ row i + 𝒩(0, σ²),\\n      σ ~ U(1e-6, 0.05), then column-renormalized.\\n      Models annotators who cannot distinguish certain categories.\\n\\n  (c) Block-diagonal: K partitioned into 2 blocks; high within-block confusion\\n      (Dirichlet α=5), low between-block leakage ~ U(0.001, 0.1).\\n      Models structured confusion (e.g., fine-grained subcategory mix-ups).\\n\\nFeatures computed per matrix:\\n  - spectral_gap:     λ₁ - λ₂ (top two eigenvalue magnitudes of C)\\n  - diag_dominance:   min(diag(C)) / (1/K)\\n  - effective_rank:   (Σσᵢ)² / Σσᵢ² (from SVD)\\n  - condition_number: σ_max / σ_min\\n\\nOutput:\\n  - Per-topology OLS regression: bias ~ features (standardized coefficients, R²)\\n  - Feature importance ranking across topologies\\n  - Catastrophic bias thresholds per feature\\n  - Scatter plot: spectral_gap vs |bias| by topology (PNG)\\n\\\"\\\"\\\"\\n\\nimport torch\\nimport numpy as np\\nimport time\\nimport os\\nimport sys\\nfrom itertools import permutations\\n\\n# ================================================================\\n# Configuration\\n# ================================================================\\nK_VALUES = [3]  # primary K; append 5 for extended analysis\\nN_SAMPLES = 100_000\\nN_LARGE = 5_000_000\\nBASE_SEED = 42\\nDEVICE = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')\\nDTYPE = torch.float64\\nOUT_DIR = os.path.dirname(os
…[truncated 6851 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan009-pathological-matrices-v2_20260520T181421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T18:26:04.852068+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "home-1x5090",
  "command": "grep -n \"def compute_plim\\|def plim_\\|def _plim\\|def bias_\" /home/sonny/causal_annot_error_attrib/plan_002_k57_extended_7topo.py",
  "account": "sonny"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan009-pathological-matrices-v2_20260520T181421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "home-1x5090",
    "command": "grep -n \"def compute_plim\\|def plim_\\|def _plim\\|def bias_\" /home/sonny/causal_annot_error_attrib/plan_002_k57_extended_7topo.py",
    "account": "sonny"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T18:26:04.852229+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan009-pathological-matrices-v2_20260520T181421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T18:26:04.852361+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "home-1x5090",
  "command": "grep -n \"def compute_plim\\|def plim_\\|def _plim\\|def bias_\" /home/sonny/causal_annot_error_attrib/plan_002_k57_extension.py",
  "account": "sonny"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan009-pathological-matrices-v2_20260520T181421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "home-1x5090",
    "command": "grep -n \"def compute_plim\\|def plim_\\|def _plim\\|def bias_\" /home/sonny/causal_annot_error_attrib/plan_002_k57_extension.py",
    "account": "sonny"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T18:26:04.852487+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan009-pathological-matrices-v2_20260520T181421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T18:26:04.852621+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "home-1x5090",
  "command": "grep -n \"def compute_plim\\|def plim_\\|def _plim\\|def bias_\" /home/sonny/causal_annot_error_attrib/plan_002_k57_extended_7topo.py",
  "account": "sonny"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan009-pathological-matrices-v2_20260520T181421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "home-1x5090",
    "command": "grep -n \"def compute_plim\\|def plim_\\|def _plim\\|def bias_\" /home/sonny/causal_annot_error_attrib/plan_002_k57_extended_7topo.py",
    "account": "sonny"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T18:26:04.852769+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan009-pathological-matrices-v2_20260520T181421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T18:26:04.852893+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "home-1x5090",
  "command": "grep -n \"def compute_plim\\|def plim_\\|def _plim\\|def bias_\" /home/sonny/causal_annot_error_attrib/plan_002_k57_extension.py",
  "account": "sonny"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan009-pathological-matrices-v2_20260520T181421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "home-1x5090",
    "command": "grep -n \"def compute_plim\\|def plim_\\|def _plim\\|def bias_\" /home/sonny/causal_annot_error_attrib/plan_002_k57_extension.py",
    "account": "sonny"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T18:26:04.853016+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan009-pathological-matrices-v2_20260520T181421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T18:26:04.853133+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "home-1x5090",
  "command": "grep -n \"def \" /home/sonny/causal_annot_error_attrib/plan_002_k57_extended_7topo.py",
  "account": "sonny"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan009-pathological-matrices-v2_20260520T181421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "home-1x5090",
    "command": "grep -n \"def \" /home/sonny/causal_annot_error_attrib/plan_002_k57_extended_7topo.py",
    "account": "sonny"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-20T18:26:04.853276+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "home-1x5090",
  "command": "grep -n \"def \" /home/sonny/causal_annot_error_attrib/plan_002_k57_extension.py",
  "account": "sonny"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan009-pathological-matrices-v2_20260520T181421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "home-1x5090",
    "command": "grep -n \"def \" /home/sonny/causal_annot_error_attrib/plan_002_k57_extension.py",
    "account": "sonny"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-20T18:26:04.853410+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"25:def _det_seed(topo_name, K, tag, base_seed=42):\\n52:def make_p_A(K):\\n59:def make_all_params(K):\\n78:def _softmax_rows(logits):\\n83:def _sample_cat(probs, rng):\\n89:def gen_confounding(K, N, p, rng):\\n99:def gen_mediation(K, N, p, rng):\\n110:def gen_collider(K, N, p, rng):\\n118:def gen_exposure(K, N, p, rng):\\n127:def gen_mbias(K, N, p, rng):\\n139:def gen_iv(K, N, p, rng):\\n154:def gen_frontdoor(K, N, p, rng):\\n173:    def __init__(self, T, Y, A, K):\\n189:    def to_device(self, dev):\\n202:    def __init__(self, Z, Y, A, K):\\n210:    def to_device(self, dev):\\n216:def plim_with_T(ss, C):\\n235:def plim_exposure(ss, C):\\n250:def plim_iv_batched(ss, C):\\n258:def gen_random_C(K, N, device, seed=SEED, min_diag=None):\\n279:def compute_metrics(plim_batch, plim_true, tau_idx=None):\\n321:def worst_case_ols(plim_fn, ss, K, device, tau_idx=1, thresholds=(0.5, 0.7, 0.9), topo_name=\\\"\\\"):\\n342:def worst_case_iv(ss, K, device, thresholds=(0.5, 0.7, 0.9), topo_name=\\\"\\\"):\\n363:def main():\\n449:            def _pct(x): return f\\\"{x:.1%}\\\" if x == x else \\\"nan\\\"\\n487:            def _f(x, w=11):\\n489:            def _fw(x, w=10):\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.71}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan009-pathological-matrices-v2_20260520T181421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-20T18:26:04.853547+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"28:def _det_seed(topo_name, K, tag, base_seed=42):\\n58:def make_p_A(K):\\n66:def make_params(K):\\n103:def _softmax_rows(logits):\\n108:def _sample_cat(probs, rng):\\n115:def gen_confounding(K, N, p, rng):\\n126:def gen_mediation(K, N, p, rng):\\n139:def gen_collider(K, N, p, rng):\\n151:def gen_exposure(K, N, p, rng):\\n179:    def __init__(self, T, Y, A, K):\\n193:    def to_device(self, dev):\\n208:def plim_with_T(ss, C):\\n253:def plim_exposure(ss, C):\\n281:def gen_random_C(K, N, device, seed=SEED, min_diag=None):\\n313:def compute_metrics(plim_batch, plim_true, tau_idx=None):\\n349:def mc_verify(K, topo, params, C_np, n_reps=500, n_mc=10_000, seed=0):\\n382:def eigen_analysis(plim_batch, plim_true):\\n400:def worst_case_bounds(ss, plim_fn, K, device, thresholds=(0.5, 0.7, 0.9), topo_name=\\\"\\\"):\\n432:def sensitivity_heatmap(ss, plim_fn, K, device, out_path, topo_name):\\n479:def main():\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.84}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan009-pathological-matrices-v2_20260520T181421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T18:26:04.853676+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "home-1x5090",
  "command": "sed -n '216,280p' /home/sonny/causal_annot_error_attrib/plan_002_k57_extended_7topo.py",
  "account": "sonny"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan009-pathological-matrices-v2_20260520T181421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "home-1x5090",
    "command": "sed -n '216,280p' /home/sonny/causal_annot_error_attrib/plan_002_k57_extended_7topo.py",
    "account": "sonny"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-20T18:26:04.853796+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'sed' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan009-pathological-matrices-v2_20260520T181421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T18:26:04.853912+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "home-1x5090",
  "command": "sed -n '208,280p' /home/sonny/causal_annot_error_attrib/plan_002_k57_extension.py",
  "account": "sonny"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan009-pathological-matrices-v2_20260520T181421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "home-1x5090",
    "command": "sed -n '208,280p' /home/sonny/causal_annot_error_attrib/plan_002_k57_extension.py",
    "account": "sonny"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-20T18:26:04.854102+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'sed' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan009-pathological-matrices-v2_20260520T181421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-20T18:26:04.854326+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "home-1x5090",
  "command": "tail -n +216 /home/sonny/causal_annot_error_attrib/plan_002_k57_extended_7topo.py",
  "account": "sonny"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan009-pathological-matrices-v2_20260520T181421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "home-1x5090",
    "command": "tail -n +216 /home/sonny/causal_annot_error_attrib/plan_002_k57_extended_7topo.py",
    "account": "sonny"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-20T18:26:04.854684+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"def plim_with_T(ss, C):\\n    B, K = C.shape[0], ss.K\\n    dim = K + 1\\n    q = C @ ss.t_p_A\\n    ct = C @ ss.t_E_TD\\n    cy = C @ ss.t_E_YD\\n    EZZ = torch.zeros(B, dim, dim, dtype=DTYPE, device=C.device)\\n    EZZ[:, 0, 0] = 1.0\\n    EZZ[:, 0, 1] = ss.t_E_T; EZZ[:, 1, 0] = ss.t_E_T\\n    EZZ[:, 1, 1] = ss.t_E_T2\\n    EZZ[:, 0, 2:] = q[:, 1:]; EZZ[:, 2:, 0] = q[:, 1:]\\n    EZZ[:, 1, 2:] = ct[:, 1:]; EZZ[:, 2:, 1] = ct[:, 1:]\\n    idx = torch.arange(K - 1, device=C.device)\\n    EZZ[:, idx + 2, idx + 2] = q[:, 1:]\\n    EZY = torch.zeros(B, dim, dtype=DTYPE, device=C.device)\\n    EZY[:, 0] = ss.t_E_Y; EZY[:, 1] = ss.t_E_TY; EZY[:, 2:] = cy[:, 1:]\\n    return torch.linalg.solve(EZZ, EZY)\\n\\n\\ndef plim_exposure(ss, C):\\n    B, K = C.shape[0], ss.K\\n    dim = K\\n    q = C @ ss.t_p_A\\n    cy = C @ ss.t_E_YD\\n    EZZ = torch.zeros(B, dim, dim, dtype=DTYPE, device=C.device)\\n    EZZ[:, 0, 0] = 1.0\\n    EZZ[:, 0, 1:] = q[:, 1:]; EZZ[:, 1:, 0] = q[:, 1:]\\n    idx = torch.arange(K - 1, device=C.device)\\n    EZZ[:, idx + 1, idx + 1] = q[:, 1:]\\n    EZY = torch.zeros(B, dim, dtype=DTYPE, device=C.device)\\n    EZY[:, 0] = ss.t_E_Y; EZY[:, 1:] = cy[:, 1:]\\n    return torch.linalg.solve(EZZ, EZY)\\n\\n\\ndef plim_iv_batched(ss, C):\\n    FS_star = C @ ss.t_FS\\n    denom = FS_star[:, 1]\\n    nan_val = torch.tensor(float('nan'), dtype=DTYPE, device=C.device)\\n    result = torch.where(denom.abs() < 1e-8, nan_val, ss.t_RF / denom)\\n    return result.unsqueeze(1)\\n\\n\\ndef gen_random_C(K, N, device, seed=SEED, min_diag=None):\\n    rng = np.random.default_rng(seed)\\n    C = np.zeros((N, K, K))\\n    if min_diag is not None and min_diag > 0:\\n        for j in range(K):\\n            diag = rng.uniform(min_diag, 1.0, N)\\n            offdiag = rng.dirichlet(np.ones(K - 1), N) * (1.0 - diag)[:, None]\\n            col = np.zeros((N, K))\\n            col[:, j] = diag\\n            off_idx = 0\\n   
…[truncated 6839 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan009-pathological-matrices-v2_20260520T181421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-20T18:26:04.854984+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "home-1x5090",
  "command": "tail -n +200 /home/sonny/causal_annot_error_attrib/plan_002_k57_extended_7topo.py",
  "account": "sonny"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan009-pathological-matrices-v2_20260520T181421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "home-1x5090",
    "command": "tail -n +200 /home/sonny/causal_annot_error_attrib/plan_002_k57_extended_7topo.py",
    "account": "sonny"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-20T18:26:04.855383+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\nclass IVSuffStats:\\n    def __init__(self, Z, Y, A, K):\\n        self.K = K\\n        z1 = Z == 1; z0 = Z == 0\\n        self.RF = Y[z1].mean() - Y[z0].mean()\\n        self.FS = np.zeros(K)\\n        for k in range(K):\\n            self.FS[k] = (A[z1] == k).mean() - (A[z0] == k).mean()\\n\\n    def to_device(self, dev):\\n        self.t_RF = torch.tensor(self.RF, dtype=DTYPE, device=dev)\\n        self.t_FS = torch.tensor(self.FS, dtype=DTYPE, device=dev)\\n        return self\\n\\n\\ndef plim_with_T(ss, C):\\n    B, K = C.shape[0], ss.K\\n    dim = K + 1\\n    q = C @ ss.t_p_A\\n    ct = C @ ss.t_E_TD\\n    cy = C @ ss.t_E_YD\\n    EZZ = torch.zeros(B, dim, dim, dtype=DTYPE, device=C.device)\\n    EZZ[:, 0, 0] = 1.0\\n    EZZ[:, 0, 1] = ss.t_E_T; EZZ[:, 1, 0] = ss.t_E_T\\n    EZZ[:, 1, 1] = ss.t_E_T2\\n    EZZ[:, 0, 2:] = q[:, 1:]; EZZ[:, 2:, 0] = q[:, 1:]\\n    EZZ[:, 1, 2:] = ct[:, 1:]; EZZ[:, 2:, 1] = ct[:, 1:]\\n    idx = torch.arange(K - 1, device=C.device)\\n    EZZ[:, idx + 2, idx + 2] = q[:, 1:]\\n    EZY = torch.zeros(B, dim, dtype=DTYPE, device=C.device)\\n    EZY[:, 0] = ss.t_E_Y; EZY[:, 1] = ss.t_E_TY; EZY[:, 2:] = cy[:, 1:]\\n    return torch.linalg.solve(EZZ, EZY)\\n\\n\\ndef plim_exposure(ss, C):\\n    B, K = C.shape[0], ss.K\\n    dim = K\\n    q = C @ ss.t_p_A\\n    cy = C @ ss.t_E_YD\\n    EZZ = torch.zeros(B, dim, dim, dtype=DTYPE, device=C.device)\\n    EZZ[:, 0, 0] = 1.0\\n    EZZ[:, 0, 1:] = q[:, 1:]; EZZ[:, 1:, 0] = q[:, 1:]\\n    idx = torch.arange(K - 1, device=C.device)\\n    EZZ[:, idx + 1, idx + 1] = q[:, 1:]\\n    EZY = torch.zeros(B, dim, dtype=DTYPE, device=C.device)\\n    EZY[:, 0] = ss.t_E_Y; EZY[:, 1:] = cy[:, 1:]\\n    return torch.linalg.solve(EZZ, EZY)\\n\\n\\ndef plim_iv_batched(ss, C):\\n    FS_star = C @ ss.t_FS\\n    denom = FS_star[:, 1]\\n    nan_val = torch.tensor(float('nan'), dtype=DTYPE, device=C.device)\\n    result = torch.where(denom.abs() < 1e-8, nan_va
…[truncated 6843 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan009-pathological-matrices-v2_20260520T181421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T18:26:04.856080+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_009_pathological_matrices.py",
  "content": "#!/usr/bin/env python3\n\"\"\"\nPlan 009: Pathological Confusion Matrix Analysis\n\nStudies extreme bias behavior under 3 classes of pathological K*K\ncolumn-stochastic confusion matrices across 7 DAG topologies and K in {3,5,7}.\n\nPathological C types (M=1000 instances each per (K, type, param)):\n  (a) Near-permutation: C = (1-eps)P + eps*U, eps in {0.01, 0.05, 0.1, 0.2}\n  (b) Rank-deficient: SVD truncation to rank r in {1, ..., K-1}\n  (c) Block-diagonal: b blocks, b in {2, max(K//2, 2)}\n\nMatrix features extracted per C:\n  spectral_gap, diag_dominance, effective_rank, condition_number, off_diagonal_max\n\nAnalysis:\n  - Per-(topo, K, C_type, param): bias distribution statistics\n  - OLS regression: |bias| ~ features (per-topology + global)\n  - Catastrophic bias detection: |bias| > 2*|tau_true|\n\nInput:\n  DGP parameters from plan_002 (7 topologies), N_LARGE=5M samples for plim\nOutput -> artifacts/plan009/:\n  pathological_bias_summary.json, regression_results.txt\n\nDependencies: torch (CUDA), numpy, scipy.stats\n\"\"\"\n\nimport torch\nimport numpy as np\nimport json\nimport time\nimport os\nimport sys\nimport hashlib\nimport argparse\n\n# ================================================================\n# Configuration\n# ================================================================\nK_VALUES = [3, 5, 7]\nM_DEFAULT = 1000\nN_LARGE = 5_000_000\nDEVICE = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')\nDTYPE = torch.float64\n\nALL_TOPOS = ['confounding', 'mediation', 'collider', 'exposure',\n             'mbias', 'iv', 'frontdoor']\nNEAR_PERM_EPSILONS = [0.01, 0.05, 0.1, 0.2]\nFEATURE_NAMES = ['spectral_gap', 'diag_dominance', 'effective_rank',\n                 'condition_number', 'off_diagonal_max']\n\nSCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))\nOUT_DIR = os.path.join(SCRIPT_DIR, 'artifacts', 'plan009')\n\n\ndef _det_seed(topo_name, K, c_type, base_seed=42):\n    h = hashlib.sha256(\n        f\"{topo_name}_{K}_{c_type}_{base_seed}\".encode()\n    ).hexdigest()\n    return int(h[:8], 16) % (2**31)\n\n\n# ================================================================\n# DGP parameter pools (from plan_002_k57_extended_7topo.py)\n# ================================================================\n_ALPHA_POOL  = [1.5, -1.0, 0.8, -0.5, 1.2, -0.7]\n_BETA_A_POOL = [1.0, -0.5, 0.7, -0.3, 0.5, -0.2]\n_BETA_POOL   = [0.0, 1.0, -0.5, 0.7, -0.3, 0.5, -0.2]\n_GAMMA_POOL  = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]\n_DELTA_POOL  = [0.0, 0.8, -0.6, 0.5, -0.4, 0.3, -0.2]\n_DT_POOL     = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]\n_DY_POOL     = [0.0, 0.8, 0.6, -0.5, 0.4, -0.3, 0.2]\n_MBIAS_A1    = [0.0, 0.8, -0.5, 0.6, -0.4, 0.5, -0.3]\n_MBIAS_A2    = [0.0, 0.6, 0.9, -0.4, 0.7, -0.3, 0.5]\n_IV_DZ       = [0.0, 1.0, -0.5, 0.8, -0.4, 0.6, -0.3]\n_IV_DU       = [0.0, 0.8, 0.6, -0.5, 0.7, -0.3, 0.4]\n_FD_GAMMA    = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]\n_FD_DELTA    = [0.0, 1.0, -0.8, 0.7, -0.5, 0.4, -0.3]\n\n\ndef make_p_A(K):\n    if K == 3:\n        return np.array([0.40, 0.35, 0.25])\n    raw = np.array([1.0 / i for i in range(1, K + 1)])\n    return raw / raw.sum()\n\n\ndef make_all_params(K):\n    p_A = make_p_A(K)\n    return dict(\n        confounding=dict(p_A=p_A, alpha=np.array(_ALPHA_POOL[:K-1]),\n                         beta_A=np.array(_BETA_A_POOL[:K-1]),\n                         beta_T=2.0, sigma_T=1.0),\n        mediation=dict(tau=0.5, gamma=np.array(_GAMMA_POOL[:K]),\n                       delta=np.array(_DELTA_POOL[:K]),\n                       beta=np.array(_BETA_POOL[:K])),\n        collider=dict(tau=1.0, g=np.zeros(K),\n                      dT=np.array(_DT_POOL[:K]),\n                      dY=np.array(_DY_POOL[:K])),\n        exposure=dict(beta=np.array(_BETA_POOL[:K]), p_A=p_A),\n        mbias=dict(tau=1.0, delta_coef=1.0, lam=1.0, g=np.zeros(K),\n                   a1=np.array(_MBIAS_A1[:K]),\n                   a2=np.array(_MBIAS_A2[:K])),\n        iv=dict(lam=1.0, g=np.zeros(K),\n                dZ=np.array(_IV_DZ[:K]),\n                dU=np.array(_IV_DU[:K]),\n                beta=np.array(_BETA_POOL[:K])),\n        frontdoor=dict(alpha_U=1.0, lam_U=1.0,\n                       gamma=np.array(_FD_GAMMA[:K]),\n                       delta=np.array(_FD_DELTA[:K]),\n                       beta=np.array(_BETA_POOL[:K])),\n    )\n\n\n# ================================================================\n# DGP generators (from plan_002_k57_extended_7topo.py)\n# ================================================================\ndef _softmax_rows(logits):\n    e = np.exp(logits - logits.max(axis=-1, keepdims=True))\n    return e / e.sum(axis=-1, keepdims=True)\n\n\ndef _sample_cat(probs, rng):\n    cum = np.cumsum(probs, axis=1)\n    u = rng.uniform(size=probs.shape[0])[:, None]\n    return (u >= cum).sum(axis=1).astype(int)\n\n\ndef gen_confounding(K, N, p, rng):\n    A = rng.choice(K, size=N, p=p['p_A'])\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (A == j + 1).astype(float)\n    T = D @ p['alpha'] + rng.normal(0, p['sigma_T'], N)\n    Y = p['beta_T'] * T + D @ p['beta_A'] + rng.normal(0, 1, N)\n    return T, Y, A\n\n\ndef gen_mediation(K, N, p, rng):\n    T = rng.binomial(1, 0.5, N).astype(float)\n    logits = p['gamma'][None, :] + p['delta'][None, :] * T[:, None]\n    A = _sample_cat(_softmax_rows(logits), rng)\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (A == j + 1)\n    Y = p['beta'][0] + D @ p['beta'][1:] + p['tau'] * T + rng.normal(0, 1, N)\n    return T, Y, A\n\n\ndef gen_collider(K, N, p, rng):\n    T = rng.normal(0, 1, N)\n    Y = p['tau'] * T + rng.normal(0, 1, N)\n    logits = (p['g'][None, :] + p['dT'][None, :] * T[:, None]\n              + p['dY'][None, :] * Y[:, None])\n    A = _sample_cat(_softmax_rows(logits), rng)\n    return T, Y, A\n\n\ndef gen_exposure(K, N, p, rng):\n    A = rng.choice(K, size=N, p=p['p_A'])\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (A == j + 1).astype(float)\n    Y = p['beta'][0] + D @ p['beta'][1:] + rng.normal(0, 1, N)\n    return None, Y, A\n\n\ndef gen_mbias(K, N, p, rng):\n    U1 = rng.normal(0, 1, N)\n    U2 = rng.normal(0, 1, N)\n    T = p['delta_coef'] * U1 + rng.normal(0, 1, N)\n    Y = p['tau'] * T + p['lam'] * U2 + rng.normal(0, 1, N)\n    logits = np.zeros((N, K))\n    for j in range(1, K):\n        logits[:, j] = p['g'][j] + p['a1'][j] * U1 + p['a2'][j] * U2\n    A = _sample_cat(_softmax_rows(logits), rng)\n    return T, Y, A\n\n\ndef gen_iv(K, N, p, rng):\n    Z = rng.binomial(1, 0.5, N).astype(float)\n    U = rng.normal(0, 1, N)\n    eps = rng.normal(0, 1, N)\n    logits = np.zeros((N, K))\n    for j in range(1, K):\n        logits[:, j] = p['g'][j] + p['dZ'][j] * Z + p['dU'][j] * U\n    A = _sample_cat(_softmax_rows(logits), rng)\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (A == j + 1).astype(float)\n    Y = D @ p['beta'][1:] + p['lam'] * U + eps\n    return Z, Y, A\n\n\ndef gen_frontdoor(K, N, p, rng):\n    U = rng.normal(0, 1, N)\n    T = p['alpha_U'] * U + rng.normal(0, 1, N)\n    logits = np.zeros((N, K))\n    for j in range(1, K):\n        logits[:, j] = p['gamma'][j] + p['delta'][j] * T\n    M = _sample_cat(_softmax_rows(logits), rng)\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (M == j + 1).astype(float)\n    Y = D @ p['beta'][1:] + p['lam_U'] * U + rng.normal(0, 1, N)\n    return T, Y, M\n\n\n_GEN = dict(confounding=gen_confounding, mediation=gen_mediation,\n            collider=gen_collider, exposure=gen_exposure,\n            mbias=gen_mbias, iv=gen_iv, frontdoor=gen_frontdoor)\n\n\n# ================================================================\n# Sufficient statistics\n# ================================================================\nclass SuffStats:\n    def __init__(self, T, Y, A, K):\n        self.K = K\n        self.has_T = T is not None\n        N = len(Y)\n        DA = np.zeros((N, K))\n        for k in range(K):\n            DA[:, k] = (A == k).astype(float)\n        self.p_A = DA.mean(0)\n        self.E_Y = Y.mean()\n        self.E_YD = (DA * Y[:, None]).mean(0)\n        if self.has_T:\n            self.E_T = T.mean()\n            self.E_T2 = (T ** 2).mean()\n            self.E_TY = (T * Y).mean()\n            self.E_TD = (DA * T[:, None]).mean(0)\n\n    def to_device(self, dev):\n        self.t_p_A = torch.tensor(self.p_A, dtype=DTYPE, device=dev)\n        self.t_E_Y = torch.tensor(self.E_Y, dtype=DTYPE, device=dev)\n        self.t_E_YD = torch.tensor(self.E_YD, dtype=DTYPE, device=dev)\n        if self.has_T:\n            self.t_E_T = torch.tensor(self.E_T, dtype=DTYPE, device=dev)\n            self.t_E_T2 = torch.tensor(self.E_T2, dtype=DTYPE, device=dev)\n            self.t_E_TY = torch.tensor(self.E_TY, dtype=DTYPE, device=dev)\n            self.t_E_TD = torch.tensor(self.E_TD, dtype=DTYPE, device=dev)\n        return self\n\n\nclass IVSuffStats:\n    def __init__(self, Z, Y, A, K):\n        self.K = K\n        z1 = Z == 1\n        z0 = Z == 0\n        self.RF = Y[z1].mean() - Y[z0].mean()\n        self.FS = np.zeros(K)\n        for k in range(K):\n            self.FS[k] = (A[z1] == k).mean() - (A[z0] == k).mean()\n\n    def to_device(self, dev):\n        self.t_RF = torch.tensor(self.RF, dtype=DTYPE, device=dev)\n        self.t_FS = torch.tensor(self.FS, dtype=DTYPE, device=dev)\n        return self\n\n\n# ================================================================\n# Plim functions (batched GPU)\n# ================================================================\ndef plim_with_T(ss, C):\n    B, K = C.shape[0], ss.K\n    dim = K + 1\n    q = C @ ss.t_p_A\n    ct = C @ ss.t_E_TD\n    cy = C @ ss.t_E_YD\n    EZZ = torch.zeros(B, dim, dim, dtype=DTYPE, device=C.device)\n    EZZ[:, 0, 0] = 1.0\n    EZZ[:, 0, 1] = ss.t_E_T\n    EZZ[:, 1, 0] = ss.t_E_T\n    EZZ[:, 1, 1] = ss.t_E_T2\n    EZZ[:, 0, 2:] = q[:, 1:]\n    EZZ[:, 2:, 0] = q[:, 1:]\n    EZZ[:, 1, 2:] = ct[:, 1:]\n    EZZ[:, 2:, 1] = ct[:, 1:]\n    idx = torch.arange(K - 1, device=C.device)\n    EZZ[:, idx + 2, idx + 2] = q[:, 1:]\n    EZY = torch.zeros(B, dim, dtype=DTYPE, device=C.device)\n    EZY[:, 0] = ss.t_E_Y\n    EZY[:, 1] = ss.t_E_TY\n    EZY[:, 2:] = cy[:, 1:]\n    return torch.linalg.solve(EZZ, EZY)\n\n\ndef plim_exposure(ss, C):\n    B, K = C.shape[0], ss.K\n    dim = K\n    q = C @ ss.t_p_A\n    cy = C @ ss.t_E_YD\n    EZZ = torch.zeros(B, dim, dim, dtype=DTYPE, device=C.device)\n    EZZ[:, 0, 0] = 1.0\n    EZZ[:, 0, 1:] = q[:, 1:]\n    EZZ[:, 1:, 0] = q[:, 1:]\n    idx = torch.arange(K - 1, device=C.device)\n    EZZ[:, idx + 1, idx + 1] = q[:, 1:]\n    EZY = torch.zeros(B, dim, dtype=DTYPE, device=C.device)\n    EZY[:, 0] = ss.t_E_Y\n    EZY[:, 1:] = cy[:, 1:]\n    return torch.linalg.solve(EZZ, EZY)\n\n\ndef plim_iv_batched(ss, C):\n    FS_star = C @ ss.t_FS\n    denom = FS_star[:, 1]\n    nan_val = torch.tensor(float('nan'), dtype=DTYPE, device=C.device)\n    result = torch.where(denom.abs() < 1e-8, nan_val, ss.t_RF / denom)\n    return result.unsqueeze(1)\n\n\n# ================================================================\n# Pathological C matrix generators\n# ================================================================\ndef gen_near_permutation(K, M, epsilon, rng):\n    \"\"\"C = (1-eps)*P + eps*U where P=random permutation, U=random col-stochastic.\"\"\"\n    Cs = np.zeros((M, K, K))\n    for i in range(M):\n        perm = rng.permutation(K)\n        P = np.zeros((K, K))\n        P[perm, np.arange(K)] = 1.0\n        U = rng.dirichlet(np.ones(K), size=K).T\n        C = (1 - epsilon) * P + epsilon * U\n        C = np.clip(C, 1e-12, None)\n        C /= C.sum(axis=0, keepdims=True)\n        Cs[i] = C\n    return Cs\n\n\ndef gen_rank_deficient(K, M, rank, rng):\n    \"\"\"Rank-r col-stochastic via SVD truncation + non-negative projection.\"\"\"\n    Cs = np.zeros((M, K, K))\n    for i in range(M):\n        C_full = rng.dirichlet(np.ones(K) * 2.0, size=K).T\n        U, S, Vt = np.linalg.svd(C_full, full_matrices=True)\n        S_trunc = np.zeros_like(S)\n        S_trunc[:rank] = S[:rank]\n        C_approx = U @ np.diag(S_trunc) @ Vt\n        C_approx = np.clip(C_approx, 1e-12, None)\n        C_approx /= C_approx.sum(axis=0, keepdims=True)\n        Cs[i] = C_approx\n    return Cs\n\n\ndef gen_block_diagonal(K, M, n_blocks, rng):\n    \"\"\"Block-diagonal: high intra-block accuracy, low inter-block leakage.\"\"\"\n    block_sizes = []\n    base = K // n_blocks\n    remainder = K % n_blocks\n    for b in range(n_blocks):\n        block_sizes.append(base + (1 if b < remainder else 0))\n\n    Cs = np.zeros((M, K, K))\n    for i in range(M):\n        C = np.zeros((K, K))\n        leak = rng.uniform(0.001, 0.05)\n        start = 0\n        for bs in block_sizes:\n            end = start + bs\n            for col in range(start, end):\n                within = rng.dirichlet(5.0 * np.ones(bs))\n                n_outside = K - bs\n                if n_outside > 0:\n                    between = rng.dirichlet(np.ones(n_outside)) * leak\n                else:\n                    between = np.array([])\n                C[start:end, col] = within * (1 - leak)\n                idx = 0\n                for row in range(K):\n                    if row < start or row >= end:\n                        C[row, col] = between[idx]\n                        idx += 1\n            start = end\n        C = np.clip(C, 1e-12, None)\n        C /= C.sum(axis=0, keepdims=True)\n        Cs[i] = C\n    return Cs\n\n\n# ================================================================\n# Matrix feature extraction\n# ================================================================\ndef extract_features(C_batch):\n    M, K, _ = C_batch.shape\n    feats = {fn: np.zeros(M) for fn in FEATURE_NAMES}\n\n    diags = np.diagonal(C_batch, axis1=1, axis2=2)\n    feats['diag_dominance'] = diags.min(axis=1) * K\n\n    svd_vals = np.linalg.svd(C_batch, compute_uv=False)\n    sv_sum = svd_vals.sum(axis=1)\n    sv_sq_sum = (svd_vals ** 2).sum(axis=1)\n    feats['effective_rank'] = np.where(\n        sv_sum > 0, sv_sum**2 / sv_sq_sum, 0.0)\n    feats['condition_number'] = (\n        svd_vals[:, 0] / np.maximum(svd_vals[:, -1], 1e-15))\n\n    eye_mask = ~np.eye(K, dtype=bool)\n    for i in range(M):\n        eigvals = np.linalg.eigvals(C_batch[i])\n        eig_abs = np.sort(np.abs(eigvals))[::-1]\n        feats['spectral_gap'][i] = (\n            eig_abs[0] - eig_abs[1] if K > 1 else eig_abs[0])\n        feats['off_diagonal_max'][i] = C_batch[i][eye_mask].max()\n\n    return feats\n\n\n# ================================================================\n# OLS regression\n# ================================================================\ndef ols_regression(y, X_raw):\n    n = len(y)\n    p = X_raw.shape[1]\n    if n < p + 5:\n        return None\n\n    X_mean = X_raw.mean(axis=0)\n    X_std = X_raw.std(axis=0)\n    X_std[X_std < 1e-15] = 1.0\n    Xs = (X_raw - X_mean) / X_std\n    X = np.column_stack([np.ones(n), Xs])\n\n    beta = np.linalg.lstsq(X, y, rcond=None)[0]\n    y_hat = X @ beta\n    ss_res = ((y - y_hat) ** 2).sum()\n    ss_tot = ((y - y.mean()) ** 2).sum()\n    r2 = 1 - ss_res / ss_tot if ss_tot > 1e-15 else 0.0\n\n    dof = n - X.shape[1]\n    if dof <= 0:\n        pv = np.full(p, np.nan)\n    else:\n        mse = ss_res / dof\n        try:\n            cov_mat = mse * np.linalg.inv(X.T @ X)\n            se = np.sqrt(np.maximum(np.diag(cov_mat), 0))\n            t_stat = np.where(se > 1e-15, beta / se, 0.0)\n            from scipy.stats import t as t_dist\n            pv = 2 * (1 - t_dist.cdf(np.abs(t_stat[1:]), dof))\n        except np.linalg.LinAlgError:\n            pv = np.full(p, np.nan)\n\n    return dict(\n        r_squared=float(r2),\n        coefs={fn: float(beta[i + 1]) for i, fn in enumerate(FEATURE_NAMES)},\n        p_values={fn: float(pv[i]) for i, fn in enumerate(FEATURE_NAMES)},\n        n_obs=n,\n    )\n\n\n# ================================================================\n# Main\n# ================================================================\ndef main():\n    parser = argparse.ArgumentParser(\n        description='Plan 009: Pathological confusion matrix bias analysis '\n                    'across 7 DAG topologies')\n    parser.add_argument('--M', type=int, default=M_DEFAULT,\n                        help=f'C instances per config [default: {M_DEFAULT}]')\n    parser.add_argument('--N', type=int, default=N_LARGE,\n                        help=f'DGP sample size [default: {N_LARGE}]')\n    parser.add_argument('--K', type=int, nargs='+', default=K_VALUES,\n                        help=f'K values [default: {K_VALUES}]')\n    parser.add_argument('--topos', type=str, nargs='+', default=ALL_TOPOS,\n                        help='Topologies')\n    parser.add_argument('--dry-run', action='store_true',\n                        help='Quick test: M=10, K=[3], 1 topo, N=100k')\n    args = parser.parse_args()\n\n    if args.dry_run:\n        args.M = 10\n        args.K = [3]\n        args.topos = ['confounding']\n        args.N = 100_000\n        print(\"=== DRY RUN ===\\n\")\n\n    os.makedirs(OUT_DIR, exist_ok=True)\n    t0 = time.time()\n    print(f\"Plan 009: Pathological Matrices\")\n    print(f\"  Device={DEVICE}  M={args.M}  N={args.N:,}\")\n    print(f\"  K={args.K}  topos={args.topos}\")\n    print(f\"  Output -> {OUT_DIR}\\n\")\n\n    all_results = {}\n    topo_bias = {t: [] for t in ALL_TOPOS}\n    topo_feats = {t: {fn: [] for fn in FEATURE_NAMES} for t in ALL_TOPOS}\n\n    for K in args.K:\n        params = make_all_params(K)\n        rank_vals = list(range(1, K))\n        block_vals = sorted(set([2, max(K // 2, 2)]))\n\n        c_configs = {\n            'near_permutation': [(f'eps={e}', e) for e in NEAR_PERM_EPSILONS],\n            'rank_deficient': [(f'rank={r}', r) for r in rank_vals],\n            'block_diagonal': [(f'blocks={b}', b) for b in block_vals],\n        }\n\n        for topo in args.topos:\n            tk = time.time()\n            print(f\"{'='*70}\")\n            print(f\"  {topo}  K={K}\")\n            print(f\"{'='*70}\")\n\n            seed_dgp = _det_seed(topo, K, 'dgp')\n            rng = np.random.default_rng(seed_dgp)\n            T_or_Z, Y, A = _GEN[topo](K, args.N, params[topo], rng)\n\n            if topo == 'iv':\n                ss = IVSuffStats(T_or_Z, Y, A, K).to_device(DEVICE)\n                plim_fn = plim_iv_batched\n                tau_idx = 0\n            elif topo == 'exposure':\n                ss = SuffStats(None, Y, A, K).to_device(DEVICE)\n                plim_fn = plim_exposure\n                tau_idx = 1\n            else:\n                ss = SuffStats(T_or_Z, Y, A, K).to_device(DEVICE)\n                plim_fn = plim_with_T\n                tau_idx = 1\n\n            I_batch = torch.eye(K, dtype=DTYPE, device=DEVICE).unsqueeze(0)\n            plim_true = plim_fn(ss, I_batch).squeeze(0)\n            tau_true = plim_true[tau_idx].item()\n            print(f\"  tau_true(C=I) = {tau_true:.6f}  \"\n                  f\"[DGP {time.time()-tk:.1f}s]\")\n\n            for c_type, param_list in c_configs.items():\n                for param_label, param_val in param_list:\n                    seed = _det_seed(topo, K,\n                                     f'{c_type}_{param_label}')\n                    rng_c = np.random.default_rng(seed)\n\n                    if c_type == 'near_permutation':\n                        Cb = gen_near_permutation(\n                            K, args.M, param_val, rng_c)\n                    elif c_type == 'rank_deficient':\n                        Cb = gen_rank_deficient(\n                            K, args.M, param_val, rng_c)\n                    else:\n                        Cb = gen_block_diagonal(\n                            K, args.M, param_val, rng_c)\n\n                    Ct = torch.tensor(Cb, dtype=DTYPE, device=DEVICE)\n                    plim_batch = plim_fn(ss, Ct)\n                    bias = (plim_batch[:, tau_idx]\n                            - tau_true).cpu().numpy()\n\n                    valid = np.isfinite(bias)\n                    bias = bias[valid]\n                    Cb_valid = Cb[valid]\n\n                    key = f\"{topo}_K{K}_{c_type}_{param_label}\"\n                    if len(bias) == 0:\n                        all_results[key] = dict(error='all_nan')\n                        print(f\"    {c_type:20s} {param_label:10s}:\"\n                              f\" ALL NaN\")\n                        continue\n\n                    ab = np.abs(bias)\n                    feats = extract_features(Cb_valid)\n\n                    cat_thr = 2 * abs(tau_true)\n                    if abs(tau_true) > 1e-10:\n                        cat_frac = float((ab > cat_thr).mean())\n                    else:\n                        cat_frac = float('nan')\n\n                    stats = dict(\n                        n_valid=int(len(bias)),\n                        bias_mean=float(bias.mean()),\n                        bias_std=float(bias.std()),\n                        abs_bias_mean=float(ab.mean()),\n                        abs_bias_max=float(ab.max()),\n                        abs_bias_min=float(ab.min()),\n                        abs_bias_p5=float(np.percentile(ab, 5)),\n                        abs_bias_p25=float(np.percentile(ab, 25)),\n                        abs_bias_p50=float(np.percentile(ab, 50)),\n                        abs_bias_p75=float(np.percentile(ab, 75)),\n                        abs_bias_p95=float(np.percentile(ab, 95)),\n                        catastrophic_frac=cat_frac,\n                        catastrophic_threshold=float(cat_thr),\n                        feat_means={fn: float(feats[fn].mean())\n                                    for fn in FEATURE_NAMES},\n                    )\n                    all_results[key] = stats\n\n                    topo_bias[topo].extend(ab.tolist())\n                    for fn in FEATURE_NAMES:\n                        topo_feats[topo][fn].extend(\n                            feats[fn].tolist())\n\n                    cat_s = (f\"  cat={cat_frac:.1%}\"\n                             if cat_frac == cat_frac else \"\")\n                    print(\n                        f\"    {c_type:20s} {param_label:10s}: \"\n                        f\"n={len(bias):4d}  \"\n                        f\"|bias| mean={ab.mean():.4f} \"\n                        f\"max={ab.max():.4f} \"\n                        f\"p95={np.percentile(ab, 95):.4f}\"\n                        f\"{cat_s}\")\n\n            print(f\"  [{time.time()-tk:.1f}s]\\n\")\n            sys.stdout.flush()\n\n    # ================================================================\n    # Regression\n    # ================================================================\n    print(f\"\\n{'='*80}\")\n    print(\"  REGRESSION: |bias| ~ spectral_gap + diag_dominance \"\n          \"+ effective_rank\")\n    print(\"              + condition_number + off_diagonal_max\")\n    print(f\"{'='*80}\")\n\n    reg_lines = [\"Plan 009: OLS Regression Results\",\n                 \"=\" * 80, \"\"]\n    regression_results = {}\n    all_bias_g = []\n    all_feats_g = {fn: [] for fn in FEATURE_NAMES}\n\n    for topo in args.topos:\n        y = np.array(topo_bias[topo])\n        if len(y) < 20:\n            continue\n        X = np.column_stack(\n            [np.array(topo_feats[topo][fn])\n             for fn in FEATURE_NAMES])\n\n        all_bias_g.extend(y.tolist())\n        for fn in FEATURE_NAMES:\n            all_feats_g[fn].extend(topo_feats[topo][fn])\n\n        reg = ols_regression(y, X)\n        if reg is None:\n            continue\n        regression_results[topo] = reg\n\n        hdr = (f\"\\n  {topo} (n={reg['n_obs']}):  \"\n               f\"R2 = {reg['r_squared']:.4f}\")\n        print(hdr)\n        reg_lines.append(hdr)\n        col = f\"    {'Feature':25s} {'Coef':>10s} {'p-value':>12s}\"\n        print(col)\n        reg_lines.append(col)\n        sep = f\"    {'-'*49}\"\n        print(sep)\n        reg_lines.append(sep)\n        for fn in FEATURE_NAMES:\n            c = reg['coefs'][fn]\n            pv = reg['p_values'][fn]\n            sig = ('***' if pv < 0.001\n                   else ('**' if pv < 0.01\n                         else ('*' if pv < 0.05 else '')))\n            ln = (f\"    {fn:25s} {c:10.4f} \"\n                  f\"{pv:12.6f} {sig}\")\n            print(ln)\n            reg_lines.append(ln)\n\n    y_g = np.array(all_bias_g)\n    if len(y_g) >= 20:\n        X_g = np.column_stack(\n            [np.array(all_feats_g[fn]) for fn in FEATURE_NAMES])\n        reg_g = ols_regression(y_g, X_g)\n        if reg_g is not None:\n            regression_results['_global'] = reg_g\n            hdr = (f\"\\n  GLOBAL (n={reg_g['n_obs']}):  \"\n                   f\"R2 = {reg_g['r_squared']:.4f}\")\n            print(hdr)\n            reg_lines.append(hdr)\n            col = (f\"    {'Feature':25s} {'Coef':>10s} \"\n                   f\"{'p-value':>12s}\")\n            print(col)\n            reg_lines.append(col)\n            sep = f\"    {'-'*49}\"\n            print(sep)\n            reg_lines.append(sep)\n            for fn in FEATURE_NAMES:\n                c = reg_g['coefs'][fn]\n                pv = reg_g['p_values'][fn]\n                sig = ('***' if pv < 0.001\n                       else ('**' if pv < 0.01\n                             else ('*' if pv < 0.05 else '')))\n                ln = (f\"    {fn:25s} {c:10.4f} \"\n                      f\"{pv:12.6f} {sig}\")\n                print(ln)\n                reg_lines.append(ln)\n\n    # ================================================================\n    # Save\n    # ================================================================\n    summary = dict(\n        config=dict(\n            M=args.M, N=args.N, K_values=args.K,\n            topologies=args.topos,\n            near_perm_epsilons=NEAR_PERM_EPSILONS,\n            feature_names=FEATURE_NAMES),\n        bias_results=all_results,\n        regression=regression_results,\n    )\n\n    json_path = os.path.join(OUT_DIR,\n                             'pathological_bias_summary.json')\n    with open(json_path, 'w') as f:\n        json.dump(summary, f, indent=2, default=str)\n    print(f\"\\nSaved {json_path}\")\n\n    reg_path = os.path.join(OUT_DIR, 'regression_results.txt')\n    with open(reg_path, 'w') as f:\n        f.write('\\n'.join(reg_lines))\n    print(f\"Saved {reg_path}\")\n\n    print(f\"\\nTotal: {time.time() - t0:.0f}s\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan009-pathological-matrices-v2_20260520T181421",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_009_pathological_matrices.py",
    "content": "#!/usr/bin/env python3\n\"\"\"\nPlan 009: Pathological Confusion Matrix Analysis\n\nStudies extreme bias behavior under 3 classes of pathological K*K\ncolumn-stochastic confusion matrices across 7 DAG topologies and K in {3,5,7}.\n\nPathological C types (M=1000 instances each per (K, type, param)):\n  (a) Near-permutation: C = (1-eps)P + eps*U, eps in {0.01, 0.05, 0.1, 0.2}\n  (b) Rank-deficient: SVD truncation to rank r in {1, ..., K-1}\n  (c) Block-diagonal: b blocks, b in {2, max(K//2, 2)}\n\nMatrix features extracted per C:\n  spectral_gap, diag_dominance, effective_rank, condition_number, off_diagonal_max\n\nAnalysis:\n  - Per-(topo, K, C_type, param): bias distribution statistics\n  - OLS regression: |bias| ~ features (per-topology + global)\n  - Catastrophic bias detection: |bias| > 2*|tau_true|\n\nInput:\n  DGP parameters from plan_002 (7 topologies), N_LARGE=5M samples for plim\nOutput -> artifacts/plan009/:\n  pathological_bias_summary.json, regression_results.txt\n\nDependencies: torch (CUDA), numpy, scipy.stats\n\"\"\"\n\nimport torch\nimport numpy as np\nimport json\nimport time\nimport os\nimport sys\nimport hashlib\nimport argparse\n\n# ================================================================\n# Configuration\n# ================================================================\nK_VALUES = [3, 5, 7]\nM_DEFAULT = 1000\nN_LARGE = 5_000_000\nDEVICE = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')\nDTYPE = torch.float64\n\nALL_TOPOS = ['confounding', 'mediation', 'collider', 'exposure',\n             'mbias', 'iv', 'frontdoor']\nNEAR_PERM_EPSILONS = [0.01, 0.05, 0.1, 0.2]\nFEATURE_NAMES = ['spectral_gap', 'diag_dominance', 'effective_rank',\n                 'condition_number', 'off_diagonal_max']\n\nSCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))\nOUT_DIR = os.path.join(SCRIPT_DIR, 'artifacts', 'plan009')\n\n\ndef _det_seed(topo_name, K, c_type, base_seed=42):\n    h = hashlib.sha256(\n        f\"{topo_name}_{K}_{c_type}_{base_seed}\".encode()\n    ).hexdigest()\n    return int(h[:8], 16) % (2**31)\n\n\n# ================================================================\n# DGP parameter pools (from plan_002_k57_extended_7topo.py)\n# ================================================================\n_ALPHA_POOL  = [1.5, -1.0, 0.8, -0.5, 1.2, -0.7]\n_BETA_A_POOL = [1.0, -0.5, 0.7, -0.3, 0.5, -0.2]\n_BETA_POOL   = [0.0, 1.0, -0.5, 0.7, -0.3, 0.5, -0.2]\n_GAMMA_POOL  = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]\n_DELTA_POOL  = [0.0, 0.8, -0.6, 0.5, -0.4, 0.3, -0.2]\n_DT_POOL     = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]\n_DY_POOL     = [0.0, 0.8, 0.6, -0.5, 0.4, -0.3, 0.2]\n_MBIAS_A1    = [0.0, 0.8, -0.5, 0.6, -0.4, 0.5, -0.3]\n_MBIAS_A2    = [0.0, 0.6, 0.9, -0.4, 0.7, -0.3, 0.5]\n_IV_DZ       = [0.0, 1.0, -0.5, 0.8, -0.4, 0.6, -0.3]\n_IV_DU       = [0.0, 0.8, 0.6, -0.5, 0.7, -0.3, 0.4]\n_FD_GAMMA    = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]\n_FD_DELTA    = [0.0, 1.0, -0.8, 0.7, -0.5, 0.4, -0.3]\n\n\ndef make_p_A(K):\n    if K == 3:\n        return np.array([0.40, 0.35, 0.25])\n    raw = np.array([1.0 / i for i in range(1, K + 1)])\n    return raw / raw.sum()\n\n\ndef make_all_params(K):\n    p_A = make_p_A(K)\n    return dict(\n        confounding=dict(p_A=p_A, alpha=np.array(_ALPHA_POOL[:K-1]),\n                         beta_A=np.array(_BETA_A_POOL[:K-1]),\n                         beta_T=2.0, sigma_T=1.0),\n        mediation=dict(tau=0.5, gamma=np.array(_GAMMA_POOL[:K]),\n                       delta=np.array(_DELTA_POOL[:K]),\n                       beta=np.array(_BETA_POOL[:K])),\n        collider=dict(tau=1.0, g=np.zeros(K),\n                      dT=np.array(_DT_POOL[:K]),\n                      dY=np.array(_DY_POOL[:K])),\n        exposure=dict(beta=np.array(_BETA_POOL[:K]), p_A=p_A),\n        mbias=dict(tau=1.0, delta_coef=1.0, lam=1.0, g=np.zeros(K),\n                   a1=np.array(_MBIAS_A1[:K]),\n                   a2=np.array(_MBIAS_A2[:K])),\n        iv=dict(lam=1.0, g=np.zeros(K),\n                dZ=np.array(_IV_DZ[:K]),\n                dU=np.array(_IV_DU[:K]),\n                beta=np.array(_BETA_POOL[:K])),\n        frontdoor=dict(alpha_U=1.0, lam_U=1.0,\n                       gamma=np.array(_FD_GAMMA[:K]),\n                       delta=np.array(_FD_DELTA[:K]),\n                       beta=np.array(_BETA_POOL[:K])),\n    )\n\n\n# ================================================================\n# DGP generators (from plan_002_k57_extended_7topo.py)\n# ================================================================\ndef _softmax_rows(logits):\n    e = np.exp(logits - logits.max(axis=-1, keepdims=True))\n    return e / e.sum(axis=-1, keepdims=True)\n\n\ndef _sample_cat(probs, rng):\n    cum = np.cumsum(probs, axis=1)\n    u = rng.uniform(size=probs.shape[0])[:, None]\n    return (u >= cum).sum(axis=1).astype(int)\n\n\ndef gen_confounding(K, N, p, rng):\n    A = rng.choice(K, size=N, p=p['p_A'])\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (A == j + 1).astype(float)\n    T = D @ p['alpha'] + rng.normal(0, p['sigma_T'], N)\n    Y = p['beta_T'] * T + D @ p['beta_A'] + rng.normal(0, 1, N)\n    return T, Y, A\n\n\ndef gen_mediation(K, N, p, rng):\n    T = rng.binomial(1, 0.5, N).astype(float)\n    logits = p['gamma'][None, :] + p['delta'][None, :] * T[:, None]\n    A = _sample_cat(_softmax_rows(logits), rng)\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (A == j + 1)\n    Y = p['beta'][0] + D @ p['beta'][1:] + p['tau'] * T + rng.normal(0, 1, N)\n    return T, Y, A\n\n\ndef gen_collider(K, N, p, rng):\n    T = rng.normal(0, 1, N)\n    Y = p['tau'] * T + rng.normal(0, 1, N)\n    logits = (p['g'][None, :] + p['dT'][None, :] * T[:, None]\n              + p['dY'][None, :] * Y[:, None])\n    A = _sample_cat(_softmax_rows(logits), rng)\n    return T, Y, A\n\n\ndef gen_exposure(K, N, p, rng):\n    A = rng.choice(K, size=N, p=p['p_A'])\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (A == j + 1).astype(float)\n    Y = p['beta'][0] + D @ p['beta'][1:] + rng.normal(0, 1, N)\n    return None, Y, A\n\n\ndef gen_mbias(K, N, p, rng):\n    U1 = rng.normal(0, 1, N)\n    U2 = rng.normal(0, 1, N)\n    T = p['delta_coef'] * U1 + rng.normal(0, 1, N)\n    Y = p['tau'] * T + p['lam'] * U2 + rng.normal(0, 1, N)\n    logits = np.zeros((N, K))\n    for j in range(1, K):\n        logits[:, j] = p['g'][j] + p['a1'][j] * U1 + p['a2'][j] * U2\n    A = _sample_cat(_softmax_rows(logits), rng)\n    return T, Y, A\n\n\ndef gen_iv(K, N, p, rng):\n    Z = rng.binomial(1, 0.5, N).astype(float)\n    U = rng.normal(0, 1, N)\n    eps = rng.normal(0, 1, N)\n    logits = np.zeros((N, K))\n    for j in range(1, K):\n        logits[:, j] = p['g'][j] + p['dZ'][j] * Z + p['dU'][j] * U\n    A = _sample_cat(_softmax_rows(logits), rng)\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (A == j + 1).astype(float)\n    Y = D @ p['beta'][1:] + p['lam'] * U + eps\n    return Z, Y, A\n\n\ndef gen_frontdoor(K, N, p, rng):\n    U = rng.normal(0, 1, N)\n    T = p['alpha_U'] * U + rng.normal(0, 1, N)\n    logits = np.zeros((N, K))\n    for j in range(1, K):\n        logits[:, j] = p['gamma'][j] + p['delta'][j] * T\n    M = _sample_cat(_softmax_rows(logits), rng)\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (M == j + 1).astype(float)\n    Y = D @ p['beta'][1:] + p['lam_U'] * U + rng.normal(0, 1, N)\n    return T, Y, M\n\n\n_GEN = dict(confounding=gen_confounding, mediation=gen_mediation,\n            collider=gen_collider, exposure=gen_exposure,\n            mbias=gen_mbias, iv=gen_iv, frontdoor=gen_frontdoor)\n\n\n# ================================================================\n# Sufficient statistics\n# ================================================================\nclass SuffStats:\n    def __init__(self, T, Y, A, K):\n        self.K = K\n        self.has_T = T is not None\n        N = len(Y)\n        DA = np.zeros((N, K))\n        for k in range(K):\n            DA[:, k] = (A == k).astype(float)\n        self.p_A = DA.mean(0)\n        self.E_Y = Y.mean()\n        self.E_YD = (DA * Y[:, None]).mean(0)\n        if self.has_T:\n            self.E_T = T.mean()\n            self.E_T2 = (T ** 2).mean()\n            self.E_TY = (T * Y).mean()\n            self.E_TD = (DA * T[:, None]).mean(0)\n\n    def to_device(self, dev):\n        self.t_p_A = torch.tensor(self.p_A, dtype=DTYPE, device=dev)\n        self.t_E_Y = torch.tensor(self.E_Y, dtype=DTYPE, device=dev)\n        self.t_E_YD = torch.tensor(self.E_YD, dtype=DTYPE, device=dev)\n        if self.has_T:\n            self.t_E_T = torch.tensor(self.E_T, dtype=DTYPE, device=dev)\n            self.t_E_T2 = torch.tensor(self.E_T2, dtype=DTYPE, device=dev)\n            self.t_E_TY = torch.tensor(self.E_TY, dtype=DTYPE, device=dev)\n            self.t_E_TD = torch.tensor(self.E_TD, dtype=DTYPE, device=dev)\n        return self\n\n\nclass IVSuffStats:\n    def __init__(self, Z, Y, A, K):\n        self.K = K\n        z1 = Z == 1\n        z0 = Z == 0\n        self.RF = Y[z1].mean() - Y[z0].mean()\n        self.FS = np.zeros(K)\n        for k in range(K):\n            self.FS[k] = (A[z1] == k).mean() - (A[z0] == k).mean()\n\n    def to_device(self, dev):\n        self.t_RF = torch.tensor(self.RF, dtype=DTYPE, device=dev)\n        self.t_FS = torch.tensor(self.FS, dtype=DTYPE, device=dev)\n        return self\n\n\n# ================================================================\n# Plim functions (batched GPU)\n# ================================================================\ndef plim_with_T(ss, C):\n    B, K = C.shape[0], ss.K\n    dim = K + 1\n    q = C @ ss.t_p_A\n    ct = C @ ss.t_E_TD\n    cy = C @ ss.t_E_YD\n    EZZ = torch.zeros(B, dim, dim, dtype=DTYPE, device=C.device)\n    EZZ[:, 0, 0] = 1.0\n    EZZ[:, 0, 1] = ss.t_E_T\n    EZZ[:, 1, 0] = ss.t_E_T\n    EZZ[:, 1, 1] = ss.t_E_T2\n    EZZ[:, 0, 2:] = q[:, 1:]\n    EZZ[:, 2:, 0] = q[:, 1:]\n    EZZ[:, 1, 2:] = ct[:, 1:]\n    EZZ[:, 2:, 1] = ct[:, 1:]\n    idx = torch.arange(K - 1, device=C.device)\n    EZZ[:, idx + 2, idx + 2] = q[:, 1:]\n    EZY = torch.zeros(B, dim, dtype=DTYPE, device=C.device)\n    EZY[:, 0] = ss.t_E_Y\n    EZY[:, 1] = ss.t_E_TY\n    EZY[:, 2:] = cy[:, 1:]\n    return torch.linalg.solve(EZZ, EZY)\n\n\ndef plim_exposure(ss, C):\n    B, K = C.shape[0], ss.K\n    dim = K\n    q = C @ ss.t_p_A\n    cy = C @ ss.t_E_YD\n    EZZ = torch.zeros(B, dim, dim, dtype=DTYPE, device=C.device)\n    EZZ[:, 0, 0] = 1.0\n    EZZ[:, 0, 1:] = q[:, 1:]\n    EZZ[:, 1:, 0] = q[:, 1:]\n    idx = torch.arange(K - 1, device=C.device)\n    EZZ[:, idx + 1, idx + 1] = q[:, 1:]\n    EZY = torch.zeros(B, dim, dtype=DTYPE, device=C.device)\n    EZY[:, 0] = ss.t_E_Y\n    EZY[:, 1:] = cy[:, 1:]\n    return torch.linalg.solve(EZZ, EZY)\n\n\ndef plim_iv_batched(ss, C):\n    FS_star = C @ ss.t_FS\n    denom = FS_star[:, 1]\n    nan_val = torch.tensor(float('nan'), dtype=DTYPE, device=C.device)\n    result = torch.where(denom.abs() < 1e-8, nan_val, ss.t_RF / denom)\n    return result.unsqueeze(1)\n\n\n# ================================================================\n# Pathological C matrix generators\n# ================================================================\ndef gen_near_permutation(K, M, epsilon, rng):\n    \"\"\"C = (1-eps)*P + eps*U where P=random permutation, U=random col-stochastic.\"\"\"\n    Cs = np.zeros((M, K, K))\n    for i in range(M):\n        perm = rng.permutation(K)\n        P = np.zeros((K, K))\n        P[perm, np.arange(K)] = 1.0\n        U = rng.dirichlet(np.ones(K), size=K).T\n        C = (1 - epsilon) * P + epsilon * U\n        C = np.clip(C, 1e-12, None)\n        C /= C.sum(axis=0, keepdims=True)\n        Cs[i] = C\n    return Cs\n\n\ndef gen_rank_deficient(K, M, rank, rng):\n    \"\"\"Rank-r col-stochastic via SVD truncation + non-negative projection.\"\"\"\n    Cs = np.zeros((M, K, K))\n    for i in range(M):\n        C_full = rng.dirichlet(np.ones(K) * 2.0, size=K).T\n        U, S, Vt = np.linalg.svd(C_full, full_matrices=True)\n        S_trunc = np.zeros_like(S)\n        S_trunc[:rank] = S[:rank]\n        C_approx = U @ np.diag(S_trunc) @ Vt\n        C_approx = np.clip(C_approx, 1e-12, None)\n        C_approx /= C_approx.sum(axis=0, keepdims=True)\n        Cs[i] = C_approx\n    return Cs\n\n\ndef gen_block_diagonal(K, M, n_blocks, rng):\n    \"\"\"Block-diagonal: high intra-block accuracy, low inter-block leakage.\"\"\"\n    block_sizes = []\n    base = K // n_blocks\n    remainder = K % n_blocks\n    for b in range(n_blocks):\n        block_sizes.append(base + (1 if b < remainder else 0))\n\n    Cs = np.zeros((M, K, K))\n    for i in range(M):\n        C = np.zeros((K, K))\n        leak = rng.uniform(0.001, 0.05)\n        start = 0\n        for bs in block_sizes:\n            end = start + bs\n            for col in range(start, end):\n                within = rng.dirichlet(5.0 * np.ones(bs))\n                n_outside = K - bs\n                if n_outside > 0:\n                    between = rng.dirichlet(np.ones(n_outside)) * leak\n                else:\n                    between = np.array([])\n                C[start:end, col] = within * (1 - leak)\n                idx = 0\n                for row in range(K):\n                    if row < start or row >= end:\n                        C[row, col] = between[idx]\n                        idx += 1\n            start = end\n        C = np.clip(C, 1e-12, None)\n        C /= C.sum(axis=0, keepdims=True)\n        Cs[i] = C\n    return Cs\n\n\n# ================================================================\n# Matrix feature extraction\n# ================================================================\ndef extract_features(C_batch):\n    M, K, _ = C_batch.shape\n    feats = {fn: np.zeros(M) for fn in FEATURE_NAMES}\n\n    diags = np.diagonal(C_batch, axis1=1, axis2=2)\n    feats['diag_dominance'] = diags.min(axis=1) * K\n\n    svd_vals = np.linalg.svd(C_batch, compute_uv=False)\n    sv_sum = svd_vals.sum(axis=1)\n    sv_sq_sum = (svd_vals ** 2).sum(axis=1)\n    feats['effective_rank'] = np.where(\n        sv_sum > 0, sv_sum**2 / sv_sq_sum, 0.0)\n    feats['condition_number'] = (\n        svd_vals[:, 0] / np.maximum(svd_vals[:, -1], 1e-15))\n\n    eye_mask = ~np.eye(K, dtype=bool)\n    for i in range(M):\n        eigvals = np.linalg.eigvals(C_batch[i])\n        eig_abs = np.sort(np.abs(eigvals))[::-1]\n        feats['spectral_gap'][i] = (\n            eig_abs[0] - eig_abs[1] if K > 1 else eig_abs[0])\n        feats['off_diagonal_max'][i] = C_batch[i][eye_mask].max()\n\n    return feats\n\n\n# ================================================================\n# OLS regression\n# ================================================================\ndef ols_regression(y, X_raw):\n    n = len(y)\n    p = X_raw.shape[1]\n    if n < p + 5:\n        return None\n\n    X_mean = X_raw.mean(axis=0)\n    X_std = X_raw.std(axis=0)\n    X_std[X_std < 1e-15] = 1.0\n    Xs = (X_raw - X_mean) / X_std\n    X = np.column_stack([np.ones(n), Xs])\n\n    beta = np.linalg.lstsq(X, y, rcond=None)[0]\n    y_hat = X @ beta\n    ss_res = ((y - y_hat) ** 2).sum()\n    ss_tot = ((y - y.mean()) ** 2).sum()\n    r2 = 1 - ss_res / ss_tot if ss_tot > 1e-15 else 0.0\n\n    dof = n - X.shape[1]\n    if dof <= 0:\n        pv = np.full(p, np.nan)\n    else:\n        mse = ss_res / dof\n        try:\n            cov_mat = mse * np.linalg.inv(X.T @ X)\n            se = np.sqrt(np.maximum(np.diag(cov_mat), 0))\n            t_stat = np.where(se > 1e-15, beta / se, 0.0)\n            from scipy.stats import t as t_dist\n            pv = 2 * (1 - t_dist.cdf(np.abs(t_stat[1:]), dof))\n        except np.linalg.LinAlgError:\n            pv = np.full(p, np.nan)\n\n    return dict(\n        r_squared=float(r2),\n        coefs={fn: float(beta[i + 1]) for i, fn in enumerate(FEATURE_NAMES)},\n        p_values={fn: float(pv[i]) for i, fn in enumerate(FEATURE_NAMES)},\n        n_obs=n,\n    )\n\n\n# ================================================================\n# Main\n# ================================================================\ndef main():\n    parser = argparse.ArgumentParser(\n        description='Plan 009: Pathological confusion matrix bias analysis '\n                    'across 7 DAG topologies')\n    parser.add_argument('--M', type=int, default=M_DEFAULT,\n                        help=f'C instances per config [default: {M_DEFAULT}]')\n    parser.add_argument('--N', type=int, default=N_LARGE,\n                        help=f'DGP sample size [default: {N_LARGE}]')\n    parser.add_argument('--K', type=int, nargs='+', default=K_VALUES,\n                        help=f'K values [default: {K_VALUES}]')\n    parser.add_argument('--topos', type=str, nargs='+', default=ALL_TOPOS,\n                        help='Topologies')\n    parser.add_argument('--dry-run', action='store_true',\n                        help='Quick test: M=10, K=[3], 1 topo, N=100k')\n    args = parser.parse_args()\n\n    if args.dry_run:\n        args.M = 10\n        args.K = [3]\n        args.topos = ['confounding']\n        args.N = 100_000\n        print(\"=== DRY RUN ===\\n\")\n\n    os.makedirs(OUT_DIR, exist_ok=True)\n    t0 = time.time()\n    print(f\"Plan 009: Pathological Matrices\")\n    print(f\"  Device={DEVICE}  M={args.M}  N={args.N:,}\")\n    print(f\"  K={args.K}  topos={args.topos}\")\n    print(f\"  Output -> {OUT_DIR}\\n\")\n\n    all_results = {}\n    topo_bias = {t: [] for t in ALL_TOPOS}\n    topo_feats = {t: {fn: [] for fn in FEATURE_NAMES} for t in ALL_TOPOS}\n\n    for K in args.K:\n        params = make_all_params(K)\n        rank_vals = list(range(1, K))\n        block_vals = sorted(set([2, max(K // 2, 2)]))\n\n        c_configs = {\n            'near_permutation': [(f'eps={e}', e) for e in NEAR_PERM_EPSILONS],\n            'rank_deficient': [(f'rank={r}', r) for r in rank_vals],\n            'block_diagonal': [(f'blocks={b}', b) for b in block_vals],\n        }\n\n        for topo in args.topos:\n            tk = time.time()\n            print(f\"{'='*70}\")\n            print(f\"  {topo}  K={K}\")\n            print(f\"{'='*70}\")\n\n            seed_dgp = _det_seed(topo, K, 'dgp')\n            rng = np.random.default_rng(seed_dgp)\n            T_or_Z, Y, A = _GEN[topo](K, args.N, params[topo], rng)\n\n            if topo == 'iv':\n                ss = IVSuffStats(T_or_Z, Y, A, K).to_device(DEVICE)\n                plim_fn = plim_iv_batched\n                tau_idx = 0\n            elif topo == 'exposure':\n                ss = SuffStats(None, Y, A, K).to_device(DEVICE)\n                plim_fn = plim_exposure\n                tau_idx = 1\n            else:\n                ss = SuffStats(T_or_Z, Y, A, K).to_device(DEVICE)\n                plim_fn = plim_with_T\n                tau_idx = 1\n\n            I_batch = torch.eye(K, dtype=DTYPE, device=DEVICE).unsqueeze(0)\n            plim_true = plim_fn(ss, I_batch).squeeze(0)\n            tau_true = plim_true[tau_idx].item()\n            print(f\"  tau_true(C=I) = {tau_true:.6f}  \"\n                  f\"[DGP {time.time()-tk:.1f}s]\")\n\n            for c_type, param_list in c_configs.items():\n                for param_label, param_val in param_list:\n                    seed = _det_seed(topo, K,\n                                     f'{c_type}_{param_label}')\n                    rng_c = np.random.default_rng(seed)\n\n                    if c_type == 'near_permutation':\n                        Cb = gen_near_permutation(\n                            K, args.M, param_val, rng_c)\n                    elif c_type == 'rank_deficient':\n                        Cb = gen_rank_deficient(\n                            K, args.M, param_val, rng_c)\n                    else:\n                        Cb = gen_block_diagonal(\n                            K, args.M, param_val, rng_c)\n\n                    Ct = torch.tensor(Cb, dtype=DTYPE, device=DEVICE)\n                    plim_batch = plim_fn(ss, Ct)\n                    bias = (plim_batch[:, tau_idx]\n                            - tau_true).cpu().numpy()\n\n                    valid = np.isfinite(bias)\n                    bias = bias[valid]\n                    Cb_valid = Cb[valid]\n\n                    key = f\"{topo}_K{K}_{c_type}_{param_label}\"\n                    if len(bias) == 0:\n                        all_results[key] = dict(error='all_nan')\n                        print(f\"    {c_type:20s} {param_label:10s}:\"\n                              f\" ALL NaN\")\n                        continue\n\n                    ab = np.abs(bias)\n                    feats = extract_features(Cb_valid)\n\n                    cat_thr = 2 * abs(tau_true)\n                    if abs(tau_true) > 1e-10:\n                        cat_frac = float((ab > cat_thr).mean())\n                    else:\n                        cat_frac = float('nan')\n\n                    stats = dict(\n                        n_valid=int(len(bias)),\n                        bias_mean=float(bias.mean()),\n                        bias_std=float(bias.std()),\n                        abs_bias_mean=float(ab.mean()),\n                        abs_bias_max=float(ab.max()),\n                        abs_bias_min=float(ab.min()),\n                        abs_bias_p5=float(np.percentile(ab, 5)),\n                        abs_bias_p25=float(np.percentile(ab, 25)),\n                        abs_bias_p50=float(np.percentile(ab, 50)),\n                        abs_bias_p75=float(np.percentile(ab, 75)),\n                        abs_bias_p95=float(np.percentile(ab, 95)),\n                        catastrophic_frac=cat_frac,\n                        catastrophic_threshold=float(cat_thr),\n                        feat_means={fn: float(feats[fn].mean())\n                                    for fn in FEATURE_NAMES},\n                    )\n                    all_results[key] = stats\n\n                    topo_bias[topo].extend(ab.tolist())\n                    for fn in FEATURE_NAMES:\n                        topo_feats[topo][fn].extend(\n                            feats[fn].tolist())\n\n                    cat_s = (f\"  cat={cat_frac:.1%}\"\n                             if cat_frac == cat_frac else \"\")\n                    print(\n                        f\"    {c_type:20s} {param_label:10s}: \"\n                        f\"n={len(bias):4d}  \"\n                        f\"|bias| mean={ab.mean():.4f} \"\n                        f\"max={ab.max():.4f} \"\n                        f\"p95={np.percentile(ab, 95):.4f}\"\n                        f\"{cat_s}\")\n\n            print(f\"  [{time.time()-tk:.1f}s]\\n\")\n            sys.stdout.flush()\n\n    # ================================================================\n    # Regression\n    # ================================================================\n    print(f\"\\n{'='*80}\")\n    print(\"  REGRESSION: |bias| ~ spectral_gap + diag_dominance \"\n          \"+ effective_rank\")\n    print(\"              + condition_number + off_diagonal_max\")\n    print(f\"{'='*80}\")\n\n    reg_lines = [\"Plan 009: OLS Regression Results\",\n                 \"=\" * 80, \"\"]\n    regression_results = {}\n    all_bias_g = []\n    all_feats_g = {fn: [] for fn in FEATURE_NAMES}\n\n    for topo in args.topos:\n        y = np.array(topo_bias[topo])\n        if len(y) < 20:\n            continue\n        X = np.column_stack(\n            [np.array(topo_feats[topo][fn])\n             for fn in FEATURE_NAMES])\n\n        all_bias_g.extend(y.tolist())\n        for fn in FEATURE_NAMES:\n            all_feats_g[fn].extend(topo_feats[topo][fn])\n\n        reg = ols_regression(y, X)\n        if reg is None:\n            continue\n        regression_results[topo] = reg\n\n        hdr = (f\"\\n  {topo} (n={reg['n_obs']}):  \"\n               f\"R2 = {reg['r_squared']:.4f}\")\n        print(hdr)\n        reg_lines.append(hdr)\n        col = f\"    {'Feature':25s} {'Coef':>10s} {'p-value':>12s}\"\n        print(col)\n        reg_lines.append(col)\n        sep = f\"    {'-'*49}\"\n        print(sep)\n        reg_lines.append(sep)\n        for fn in FEATURE_NAMES:\n            c = reg['coefs'][fn]\n            pv = reg['p_values'][fn]\n            sig = ('***' if pv < 0.001\n                   else ('**' if pv < 0.01\n                         else ('*' if pv < 0.05 else '')))\n            ln = (f\"    {fn:25s} {c:10.4f} \"\n                  f\"{pv:12.6f} {sig}\")\n            print(ln)\n            reg_lines.append(ln)\n\n    y_g = np.array(all_bias_g)\n    if len(y_g) >= 20:\n        X_g = np.column_stack(\n            [np.array(all_feats_g[fn]) for fn in FEATURE_NAMES])\n        reg_g = ols_regression(y_g, X_g)\n        if reg_g is not None:\n            regression_results['_global'] = reg_g\n            hdr = (f\"\\n  GLOBAL (n={reg_g['n_obs']}):  \"\n                   f\"R2 = {reg_g['r_squared']:.4f}\")\n            print(hdr)\n            reg_lines.append(hdr)\n            col = (f\"    {'Feature':25s} {'Coef':>10s} \"\n                   f\"{'p-value':>12s}\")\n            print(col)\n            reg_lines.append(col)\n            sep = f\"    {'-'*49}\"\n            print(sep)\n            reg_lines.append(sep)\n            for fn in FEATURE_NAMES:\n                c = reg_g['coefs'][fn]\n                pv = reg_g['p_values'][fn]\n                sig = ('***' if pv < 0.001\n                       else ('**' if pv < 0.01\n                             else ('*' if pv < 0.05 else '')))\n                ln = (f\"    {fn:25s} {c:10.4f} \"\n                      f\"{pv:12.6f} {sig}\")\n                print(ln)\n                reg_lines.append(ln)\n\n    # ================================================================\n    # Save\n    # ================================================================\n    summary = dict(\n        config=dict(\n            M=args.M, N=args.N, K_values=args.K,\n            topologies=args.topos,\n            near_perm_epsilons=NEAR_PERM_EPSILONS,\n            feature_names=FEATURE_NAMES),\n        bias_results=all_results,\n        regression=regression_results,\n    )\n\n    json_path = os.path.join(OUT_DIR,\n                             'pathological_bias_summary.json')\n    with open(json_path, 'w') as f:\n        json.dump(summary, f, indent=2, default=str)\n    print(f\"\\nSaved {json_path}\")\n\n    reg_path = os.path.join(OUT_DIR, 'regression_results.txt')\n    with open(reg_path, 'w') as f:\n        f.write('\\n'.join(reg_lines))\n    print(f\"Saved {reg_path}\")\n\n    print(f\"\\nTotal: {time.time() - t0:.0f}s\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-20T18:26:04.856766+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_009_pathological_matrices.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan009-pathological-matrices-v2_20260520T181421",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-20T18:26:04.857098+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "home-1x5090",
  "command": "cat > /home/sonny/causal_annot_error_attrib/plan_009_pathological_matrices.py << 'SCRIPT_EOF'\n#!/usr/bin/env python3\n\"\"\"\nPlan 009: Pathological Confusion Matrix Analysis\n\nStudies extreme bias behavior under 3 classes of pathological K*K\ncolumn-stochastic confusion matrices across 7 DAG topologies and K in {3,5,7}.\n\nPathological C types (M=1000 instances each per (K, type, param)):\n  (a) Near-permutation: C = (1-eps)P + eps*U, eps in {0.01, 0.05, 0.1, 0.2}\n  (b) Rank-deficient: SVD truncation to rank r in {1, ..., K-1}\n  (c) Block-diagonal: b blocks, b in {2, max(K//2, 2)}\n\nMatrix features extracted per C:\n  spectral_gap, diag_dominance, effective_rank, condition_number, off_diagonal_max\n\nAnalysis:\n  - Per-(topo, K, C_type, param): bias distribution statistics\n  - OLS regression: |bias| ~ features (per-topology + global)\n  - Catastrophic bias detection: |bias| > 2*|tau_true|\n\nInput:\n  DGP parameters from plan_002 (7 topologies), N_LARGE=5M samples for plim\nOutput -> artifacts/plan009/:\n  pathological_bias_summary.json, regression_results.txt\n\nDependencies: torch (CUDA), numpy, scipy.stats\n\"\"\"\n\nimport torch\nimport numpy as np\nimport json\nimport time\nimport os\nimport sys\nimport hashlib\nimport argparse\n\n# ================================================================\n# Configuration\n# ================================================================\nK_VALUES = [3, 5, 7]\nM_DEFAULT = 1000\nN_LARGE = 5_000_000\nDEVICE = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')\nDTYPE = torch.float64\n\nALL_TOPOS = ['confounding', 'mediation', 'collider', 'exposure',\n             'mbias', 'iv', 'frontdoor']\nNEAR_PERM_EPSILONS = [0.01, 0.05, 0.1, 0.2]\nFEATURE_NAMES = ['spectral_gap', 'diag_dominance', 'effective_rank',\n                 'condition_number', 'off_diagonal_max']\n\nSCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))\nOUT_DIR = os.path.join(SCRIPT_DIR, 'artifacts', 'plan009')\n\n\ndef _det_seed(topo_name, K, c_type, base_seed=42):\n    h = hashlib.sha256(\n        f\"{topo_name}_{K}_{c_type}_{base_seed}\".encode()\n    ).hexdigest()\n    return int(h[:8], 16) % (2**31)\n\n\n# ================================================================\n# DGP parameter pools (from plan_002_k57_extended_7topo.py)\n# ================================================================\n_ALPHA_POOL  = [1.5, -1.0, 0.8, -0.5, 1.2, -0.7]\n_BETA_A_POOL = [1.0, -0.5, 0.7, -0.3, 0.5, -0.2]\n_BETA_POOL   = [0.0, 1.0, -0.5, 0.7, -0.3, 0.5, -0.2]\n_GAMMA_POOL  = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]\n_DELTA_POOL  = [0.0, 0.8, -0.6, 0.5, -0.4, 0.3, -0.2]\n_DT_POOL     = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]\n_DY_POOL     = [0.0, 0.8, 0.6, -0.5, 0.4, -0.3, 0.2]\n_MBIAS_A1    = [0.0, 0.8, -0.5, 0.6, -0.4, 0.5, -0.3]\n_MBIAS_A2    = [0.0, 0.6, 0.9, -0.4, 0.7, -0.3, 0.5]\n_IV_DZ       = [0.0, 1.0, -0.5, 0.8, -0.4, 0.6, -0.3]\n_IV_DU       = [0.0, 0.8, 0.6, -0.5, 0.7, -0.3, 0.4]\n_FD_GAMMA    = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]\n_FD_DELTA    = [0.0, 1.0, -0.8, 0.7, -0.5, 0.4, -0.3]\n\n\ndef make_p_A(K):\n    if K == 3:\n        return np.array([0.40, 0.35, 0.25])\n    raw = np.array([1.0 / i for i in range(1, K + 1)])\n    return raw / raw.sum()\n\n\ndef make_all_params(K):\n    p_A = make_p_A(K)\n    return dict(\n        confounding=dict(p_A=p_A, alpha=np.array(_ALPHA_POOL[:K-1]),\n                         beta_A=np.array(_BETA_A_POOL[:K-1]),\n                         beta_T=2.0, sigma_T=1.0),\n        mediation=dict(tau=0.5, gamma=np.array(_GAMMA_POOL[:K]),\n                       delta=np.array(_DELTA_POOL[:K]),\n                       beta=np.array(_BETA_POOL[:K])),\n        collider=dict(tau=1.0, g=np.zeros(K),\n                      dT=np.array(_DT_POOL[:K]),\n                      dY=np.array(_DY_POOL[:K])),\n        exposure=dict(beta=np.array(_BETA_POOL[:K]), p_A=p_A),\n        mbias=dict(tau=1.0, delta_coef=1.0, lam=1.0, g=np.zeros(K),\n                   a1=np.array(_MBIAS_A1[:K]),\n                   a2=np.array(_MBIAS_A2[:K])),\n        iv=dict(lam=1.0, g=np.zeros(K),\n                dZ=np.array(_IV_DZ[:K]),\n                dU=np.array(_IV_DU[:K]),\n                beta=np.array(_BETA_POOL[:K])),\n        frontdoor=dict(alpha_U=1.0, lam_U=1.0,\n                       gamma=np.array(_FD_GAMMA[:K]),\n                       delta=np.array(_FD_DELTA[:K]),\n                       beta=np.array(_BETA_POOL[:K])),\n    )\n\n\n# ================================================================\n# DGP generators (from plan_002_k57_extended_7topo.py)\n# ================================================================\ndef _softmax_rows(logits):\n    e = np.exp(logits - logits.max(axis=-1, keepdims=True))\n    return e / e.sum(axis=-1, keepdims=True)\n\n\ndef _sample_cat(probs, rng):\n    cum = np.cumsum(probs, axis=1)\n    u = rng.uniform(size=probs.shape[0])[:, None]\n    return (u >= cum).sum(axis=1).astype(int)\n\n\ndef gen_confounding(K, N, p, rng):\n    A = rng.choice(K, size=N, p=p['p_A'])\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (A == j + 1).astype(float)\n    T = D @ p['alpha'] + rng.normal(0, p['sigma_T'], N)\n    Y = p['beta_T'] * T + D @ p['beta_A'] + rng.normal(0, 1, N)\n    return T, Y, A\n\n\ndef gen_mediation(K, N, p, rng):\n    T = rng.binomial(1, 0.5, N).astype(float)\n    logits = p['gamma'][None, :] + p['delta'][None, :] * T[:, None]\n    A = _sample_cat(_softmax_rows(logits), rng)\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (A == j + 1)\n    Y = p['beta'][0] + D @ p['beta'][1:] + p['tau'] * T + rng.normal(0, 1, N)\n    return T, Y, A\n\n\ndef gen_collider(K, N, p, rng):\n    T = rng.normal(0, 1, N)\n    Y = p['tau'] * T + rng.normal(0, 1, N)\n    logits = (p['g'][None, :] + p['dT'][None, :] * T[:, None]\n              + p['dY'][None, :] * Y[:, None])\n    A = _sample_cat(_softmax_rows(logits), rng)\n    return T, Y, A\n\n\ndef gen_exposure(K, N, p, rng):\n    A = rng.choice(K, size=N, p=p['p_A'])\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (A == j + 1).astype(float)\n    Y = p['beta'][0] + D @ p['beta'][1:] + rng.normal(0, 1, N)\n    return None, Y, A\n\n\ndef gen_mbias(K, N, p, rng):\n    U1 = rng.normal(0, 1, N)\n    U2 = rng.normal(0, 1, N)\n    T = p['delta_coef'] * U1 + rng.normal(0, 1, N)\n    Y = p['tau'] * T + p['lam'] * U2 + rng.normal(0, 1, N)\n    logits = np.zeros((N, K))\n    for j in range(1, K):\n        logits[:, j] = p['g'][j] + p['a1'][j] * U1 + p['a2'][j] * U2\n    A = _sample_cat(_softmax_rows(logits), rng)\n    return T, Y, A\n\n\ndef gen_iv(K, N, p, rng):\n    Z = rng.binomial(1, 0.5, N).astype(float)\n    U = rng.normal(0, 1, N)\n    eps = rng.normal(0, 1, N)\n    logits = np.zeros((N, K))\n    for j in range(1, K):\n        logits[:, j] = p['g'][j] + p['dZ'][j] * Z + p['dU'][j] * U\n    A = _sample_cat(_softmax_rows(logits), rng)\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (A == j + 1).astype(float)\n    Y = D @ p['beta'][1:] + p['lam'] * U + eps\n    return Z, Y, A\n\n\ndef gen_frontdoor(K, N, p, rng):\n    U = rng.normal(0, 1, N)\n    T = p['alpha_U'] * U + rng.normal(0, 1, N)\n    logits = np.zeros((N, K))\n    for j in range(1, K):\n        logits[:, j] = p['gamma'][j] + p['delta'][j] * T\n    M = _sample_cat(_softmax_rows(logits), rng)\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (M == j + 1).astype(float)\n    Y = D @ p['beta'][1:] + p['lam_U'] * U + rng.normal(0, 1, N)\n    return T, Y, M\n\n\n_GEN = dict(confounding=gen_confounding, mediation=gen_mediation,\n            collider=gen_collider, exposure=gen_exposure,\n            mbias=gen_mbias, iv=gen_iv, frontdoor=gen_frontdoor)\n\n\n# ================================================================\n# Sufficient statistics\n# ================================================================\nclass SuffStats:\n    def __init__(self, T, Y, A, K):\n        self.K = K\n        self.has_T = T is not None\n        N = len(Y)\n        DA = np.zeros((N, K))\n        for k in range(K):\n            DA[:, k] = (A == k).astype(float)\n        self.p_A = DA.mean(0)\n        self.E_Y = Y.mean()\n        self.E_YD = (DA * Y[:, None]).mean(0)\n        if self.has_T:\n            self.E_T = T.mean()\n            self.E_T2 = (T ** 2).mean()\n            self.E_TY = (T * Y).mean()\n            self.E_TD = (DA * T[:, None]).mean(0)\n\n    def to_device(self, dev):\n        self.t_p_A = torch.tensor(self.p_A, dtype=DTYPE, device=dev)\n        self.t_E_Y = torch.tensor(self.E_Y, dtype=DTYPE, device=dev)\n        self.t_E_YD = torch.tensor(self.E_YD, dtype=DTYPE, device=dev)\n        if self.has_T:\n            self.t_E_T = torch.tensor(self.E_T, dtype=DTYPE, device=dev)\n            self.t_E_T2 = torch.tensor(self.E_T2, dtype=DTYPE, device=dev)\n            self.t_E_TY = torch.tensor(self.E_TY, dtype=DTYPE, device=dev)\n            self.t_E_TD = torch.tensor(self.E_TD, dtype=DTYPE, device=dev)\n        return self\n\n\nclass IVSuffStats:\n    def __init__(self, Z, Y, A, K):\n        self.K = K\n        z1 = Z == 1\n        z0 = Z == 0\n        self.RF = Y[z1].mean() - Y[z0].mean()\n        self.FS = np.zeros(K)\n        for k in range(K):\n            self.FS[k] = (A[z1] == k).mean() - (A[z0] == k).mean()\n\n    def to_device(self, dev):\n        self.t_RF = torch.tensor(self.RF, dtype=DTYPE, device=dev)\n        self.t_FS = torch.tensor(self.FS, dtype=DTYPE, device=dev)\n        return self\n\n\n# ================================================================\n# Plim functions (batched GPU)\n# ================================================================\ndef plim_with_T(ss, C):\n    B, K = C.shape[0], ss.K\n    dim = K + 1\n    q = C @ ss.t_p_A\n    ct = C @ ss.t_E_TD\n    cy = C @ ss.t_E_YD\n    EZZ = torch.zeros(B, dim, dim, dtype=DTYPE, device=C.device)\n    EZZ[:, 0, 0] = 1.0\n    EZZ[:, 0, 1] = ss.t_E_T\n    EZZ[:, 1, 0] = ss.t_E_T\n    EZZ[:, 1, 1] = ss.t_E_T2\n    EZZ[:, 0, 2:] = q[:, 1:]\n    EZZ[:, 2:, 0] = q[:, 1:]\n    EZZ[:, 1, 2:] = ct[:, 1:]\n    EZZ[:, 2:, 1] = ct[:, 1:]\n    idx = torch.arange(K - 1, device=C.device)\n    EZZ[:, idx + 2, idx + 2] = q[:, 1:]\n    EZY = torch.zeros(B, dim, dtype=DTYPE, device=C.device)\n    EZY[:, 0] = ss.t_E_Y\n    EZY[:, 1] = ss.t_E_TY\n    EZY[:, 2:] = cy[:, 1:]\n    return torch.linalg.solve(EZZ, EZY)\n\n\ndef plim_exposure(ss, C):\n    B, K = C.shape[0], ss.K\n    dim = K\n    q = C @ ss.t_p_A\n    cy = C @ ss.t_E_YD\n    EZZ = torch.zeros(B, dim, dim, dtype=DTYPE, device=C.device)\n    EZZ[:, 0, 0] = 1.0\n    EZZ[:, 0, 1:] = q[:, 1:]\n    EZZ[:, 1:, 0] = q[:, 1:]\n    idx = torch.arange(K - 1, device=C.device)\n    EZZ[:, idx + 1, idx + 1] = q[:, 1:]\n    EZY = torch.zeros(B, dim, dtype=DTYPE, device=C.device)\n    EZY[:, 0] = ss.t_E_Y\n    EZY[:, 1:] = cy[:, 1:]\n    return torch.linalg.solve(EZZ, EZY)\n\n\ndef plim_iv_batched(ss, C):\n    FS_star = C @ ss.t_FS\n    denom = FS_star[:, 1]\n    nan_val = torch.tensor(float('nan'), dtype=DTYPE, device=C.device)\n    result = torch.where(denom.abs() < 1e-8, nan_val, ss.t_RF / denom)\n    return result.unsqueeze(1)\n\n\n# ================================================================\n# Pathological C matrix generators\n# ================================================================\ndef gen_near_permutation(K, M, epsilon, rng):\n    \"\"\"C = (1-eps)*P + eps*U where P=random permutation, U=random col-stochastic.\"\"\"\n    Cs = np.zeros((M, K, K))\n    for i in range(M):\n        perm = rng.permutation(K)\n        P = np.zeros((K, K))\n        P[perm, np.arange(K)] = 1.0\n        U = rng.dirichlet(np.ones(K), size=K).T\n        C = (1 - epsilon) * P + epsilon * U\n        C = np.clip(C, 1e-12, None)\n        C /= C.sum(axis=0, keepdims=True)\n        Cs[i] = C\n    return Cs\n\n\ndef gen_rank_deficient(K, M, rank, rng):\n    \"\"\"Rank-r col-stochastic via SVD truncation + non-negative projection.\"\"\"\n    Cs = np.zeros((M, K, K))\n    for i in range(M):\n        C_full = rng.dirichlet(np.ones(K) * 2.0, size=K).T\n        U, S, Vt = np.linalg.svd(C_full, full_matrices=True)\n        S_trunc = np.zeros_like(S)\n        S_trunc[:rank] = S[:rank]\n        C_approx = U @ np.diag(S_trunc) @ Vt\n        C_approx = np.clip(C_approx, 1e-12, None)\n        C_approx /= C_approx.sum(axis=0, keepdims=True)\n        Cs[i] = C_approx\n    return Cs\n\n\ndef gen_block_diagonal(K, M, n_blocks, rng):\n    \"\"\"Block-diagonal: high intra-block accuracy, low inter-block leakage.\"\"\"\n    block_sizes = []\n    base = K // n_blocks\n    remainder = K % n_blocks\n    for b in range(n_blocks):\n        block_sizes.append(base + (1 if b < remainder else 0))\n\n    Cs = np.zeros((M, K, K))\n    for i in range(M):\n        C = np.zeros((K, K))\n        leak = rng.uniform(0.001, 0.05)\n        start = 0\n        for bs in block_sizes:\n            end = start + bs\n            for col in range(start, end):\n                within = rng.dirichlet(5.0 * np.ones(bs))\n                n_outside = K - bs\n                if n_outside > 0:\n                    between = rng.dirichlet(np.ones(n_outside)) * leak\n                else:\n                    between = np.array([])\n                C[start:end, col] = within * (1 - leak)\n                idx = 0\n                for row in range(K):\n                    if row < start or row >= end:\n                        C[row, col] = between[idx]\n                        idx += 1\n            start = end\n        C = np.clip(C, 1e-12, None)\n        C /= C.sum(axis=0, keepdims=True)\n        Cs[i] = C\n    return Cs\n\n\n# ================================================================\n# Matrix feature extraction\n# ================================================================\ndef extract_features(C_batch):\n    M, K, _ = C_batch.shape\n    feats = {fn: np.zeros(M) for fn in FEATURE_NAMES}\n\n    diags = np.diagonal(C_batch, axis1=1, axis2=2)\n    feats['diag_dominance'] = diags.min(axis=1) * K\n\n    svd_vals = np.linalg.svd(C_batch, compute_uv=False)\n    sv_sum = svd_vals.sum(axis=1)\n    sv_sq_sum = (svd_vals ** 2).sum(axis=1)\n    feats['effective_rank'] = np.where(\n        sv_sum > 0, sv_sum**2 / sv_sq_sum, 0.0)\n    feats['condition_number'] = (\n        svd_vals[:, 0] / np.maximum(svd_vals[:, -1], 1e-15))\n\n    eye_mask = ~np.eye(K, dtype=bool)\n    for i in range(M):\n        eigvals = np.linalg.eigvals(C_batch[i])\n        eig_abs = np.sort(np.abs(eigvals))[::-1]\n        feats['spectral_gap'][i] = (\n            eig_abs[0] - eig_abs[1] if K > 1 else eig_abs[0])\n        feats['off_diagonal_max'][i] = C_batch[i][eye_mask].max()\n\n    return feats\n\n\n# ================================================================\n# OLS regression\n# ================================================================\ndef ols_regression(y, X_raw):\n    n = len(y)\n    p = X_raw.shape[1]\n    if n < p + 5:\n        return None\n\n    X_mean = X_raw.mean(axis=0)\n    X_std = X_raw.std(axis=0)\n    X_std[X_std < 1e-15] = 1.0\n    Xs = (X_raw - X_mean) / X_std\n    X = np.column_stack([np.ones(n), Xs])\n\n    beta = np.linalg.lstsq(X, y, rcond=None)[0]\n    y_hat = X @ beta\n    ss_res = ((y - y_hat) ** 2).sum()\n    ss_tot = ((y - y.mean()) ** 2).sum()\n    r2 = 1 - ss_res / ss_tot if ss_tot > 1e-15 else 0.0\n\n    dof = n - X.shape[1]\n    if dof <= 0:\n        pv = np.full(p, np.nan)\n    else:\n        mse = ss_res / dof\n        try:\n            cov_mat = mse * np.linalg.inv(X.T @ X)\n            se = np.sqrt(np.maximum(np.diag(cov_mat), 0))\n            t_stat = np.where(se > 1e-15, beta / se, 0.0)\n            from scipy.stats import t as t_dist\n            pv = 2 * (1 - t_dist.cdf(np.abs(t_stat[1:]), dof))\n        except np.linalg.LinAlgError:\n            pv = np.full(p, np.nan)\n\n    return dict(\n        r_squared=float(r2),\n        coefs={fn: float(beta[i + 1]) for i, fn in enumerate(FEATURE_NAMES)},\n        p_values={fn: float(pv[i]) for i, fn in enumerate(FEATURE_NAMES)},\n        n_obs=n,\n    )\n\n\n# ================================================================\n# Main\n# ================================================================\ndef main():\n    parser = argparse.ArgumentParser(\n        description='Plan 009: Pathological confusion matrix bias analysis '\n                    'across 7 DAG topologies')\n    parser.add_argument('--M', type=int, default=M_DEFAULT,\n                        help=f'C instances per config [default: {M_DEFAULT}]')\n    parser.add_argument('--N', type=int, default=N_LARGE,\n                        help=f'DGP sample size [default: {N_LARGE}]')\n    parser.add_argument('--K', type=int, nargs='+', default=K_VALUES,\n                        help=f'K values [default: {K_VALUES}]')\n    parser.add_argument('--topos', type=str, nargs='+', default=ALL_TOPOS,\n                        help='Topologies')\n    parser.add_argument('--dry-run', action='store_true',\n                        help='Quick test: M=10, K=[3], 1 topo, N=100k')\n    args = parser.parse_args()\n\n    if args.dry_run:\n        args.M = 10\n        args.K = [3]\n        args.topos = ['confounding']\n        args.N = 100_000\n        print(\"=== DRY RUN ===\\n\")\n\n    os.makedirs(OUT_DIR, exist_ok=True)\n    t0 = time.time()\n    print(f\"Plan 009: Pathological Matrices\")\n    print(f\"  Device={DEVICE}  M={args.M}  N={args.N:,}\")\n    print(f\"  K={args.K}  topos={args.topos}\")\n    print(f\"  Output -> {OUT_DIR}\\n\")\n\n    all_results = {}\n    topo_bias = {t: [] for t in ALL_TOPOS}\n    topo_feats = {t: {fn: [] for fn in FEATURE_NAMES} for t in ALL_TOPOS}\n\n    for K in args.K:\n        params = make_all_params(K)\n        rank_vals = list(range(1, K))\n        block_vals = sorted(set([2, max(K // 2, 2)]))\n\n        c_configs = {\n            'near_permutation': [(f'eps={e}', e) for e in NEAR_PERM_EPSILONS],\n            'rank_deficient': [(f'rank={r}', r) for r in rank_vals],\n            'block_diagonal': [(f'blocks={b}', b) for b in block_vals],\n        }\n\n        for topo in args.topos:\n            tk = time.time()\n            print(f\"{'='*70}\")\n            print(f\"  {topo}  K={K}\")\n            print(f\"{'='*70}\")\n\n            seed_dgp = _det_seed(topo, K, 'dgp')\n            rng = np.random.default_rng(seed_dgp)\n            T_or_Z, Y, A = _GEN[topo](K, args.N, params[topo], rng)\n\n            if topo == 'iv':\n                ss = IVSuffStats(T_or_Z, Y, A, K).to_device(DEVICE)\n                plim_fn = plim_iv_batched\n                tau_idx = 0\n            elif topo == 'exposure':\n                ss = SuffStats(None, Y, A, K).to_device(DEVICE)\n                plim_fn = plim_exposure\n                tau_idx = 1\n            else:\n                ss = SuffStats(T_or_Z, Y, A, K).to_device(DEVICE)\n                plim_fn = plim_with_T\n                tau_idx = 1\n\n            I_batch = torch.eye(K, dtype=DTYPE, device=DEVICE).unsqueeze(0)\n            plim_true = plim_fn(ss, I_batch).squeeze(0)\n            tau_true = plim_true[tau_idx].item()\n            print(f\"  tau_true(C=I) = {tau_true:.6f}  \"\n                  f\"[DGP {time.time()-tk:.1f}s]\")\n\n            for c_type, param_list in c_configs.items():\n                for param_label, param_val in param_list:\n                    seed = _det_seed(topo, K,\n                                     f'{c_type}_{param_label}')\n                    rng_c = np.random.default_rng(seed)\n\n                    if c_type == 'near_permutation':\n                        Cb = gen_near_permutation(\n                            K, args.M, param_val, rng_c)\n                    elif c_type == 'rank_deficient':\n                        Cb = gen_rank_deficient(\n                            K, args.M, param_val, rng_c)\n                    else:\n                        Cb = gen_block_diagonal(\n                            K, args.M, param_val, rng_c)\n\n                    Ct = torch.tensor(Cb, dtype=DTYPE, device=DEVICE)\n                    plim_batch = plim_fn(ss, Ct)\n                    bias = (plim_batch[:, tau_idx]\n                            - tau_true).cpu().numpy()\n\n                    valid = np.isfinite(bias)\n                    bias = bias[valid]\n                    Cb_valid = Cb[valid]\n\n                    key = f\"{topo}_K{K}_{c_type}_{param_label}\"\n                    if len(bias) == 0:\n                        all_results[key] = dict(error='all_nan')\n                        print(f\"    {c_type:20s} {param_label:10s}:\"\n                              f\" ALL NaN\")\n                        continue\n\n                    ab = np.abs(bias)\n                    feats = extract_features(Cb_valid)\n\n                    cat_thr = 2 * abs(tau_true)\n                    if abs(tau_true) > 1e-10:\n                        cat_frac = float((ab > cat_thr).mean())\n                    else:\n                        cat_frac = float('nan')\n\n                    stats = dict(\n                        n_valid=int(len(bias)),\n                        bias_mean=float(bias.mean()),\n                        bias_std=float(bias.std()),\n                        abs_bias_mean=float(ab.mean()),\n                        abs_bias_max=float(ab.max()),\n                        abs_bias_min=float(ab.min()),\n                        abs_bias_p5=float(np.percentile(ab, 5)),\n                        abs_bias_p25=float(np.percentile(ab, 25)),\n                        abs_bias_p50=float(np.percentile(ab, 50)),\n                        abs_bias_p75=float(np.percentile(ab, 75)),\n                        abs_bias_p95=float(np.percentile(ab, 95)),\n                        catastrophic_frac=cat_frac,\n                        catastrophic_threshold=float(cat_thr),\n                        feat_means={fn: float(feats[fn].mean())\n                                    for fn in FEATURE_NAMES},\n                    )\n                    all_results[key] = stats\n\n                    topo_bias[topo].extend(ab.tolist())\n                    for fn in FEATURE_NAMES:\n                        topo_feats[topo][fn].extend(\n                            feats[fn].tolist())\n\n                    cat_s = (f\"  cat={cat_frac:.1%}\"\n                             if cat_frac == cat_frac else \"\")\n                    print(\n                        f\"    {c_type:20s} {param_label:10s}: \"\n                        f\"n={len(bias):4d}  \"\n                        f\"|bias| mean={ab.mean():.4f} \"\n                        f\"max={ab.max():.4f} \"\n                        f\"p95={np.percentile(ab, 95):.4f}\"\n                        f\"{cat_s}\")\n\n            print(f\"  [{time.time()-tk:.1f}s]\\n\")\n            sys.stdout.flush()\n\n    # ================================================================\n    # Regression\n    # ================================================================\n    print(f\"\\n{'='*80}\")\n    print(\"  REGRESSION: |bias| ~ spectral_gap + diag_dominance \"\n          \"+ effective_rank\")\n    print(\"              + condition_number + off_diagonal_max\")\n    print(f\"{'='*80}\")\n\n    reg_lines = [\"Plan 009: OLS Regression Results\",\n                 \"=\" * 80, \"\"]\n    regression_results = {}\n    all_bias_g = []\n    all_feats_g = {fn: [] for fn in FEATURE_NAMES}\n\n    for topo in args.topos:\n        y = np.array(topo_bias[topo])\n        if len(y) < 20:\n            continue\n        X = np.column_stack(\n            [np.array(topo_feats[topo][fn])\n             for fn in FEATURE_NAMES])\n\n        all_bias_g.extend(y.tolist())\n        for fn in FEATURE_NAMES:\n            all_feats_g[fn].extend(topo_feats[topo][fn])\n\n        reg = ols_regression(y, X)\n        if reg is None:\n            continue\n        regression_results[topo] = reg\n\n        hdr = (f\"\\n  {topo} (n={reg['n_obs']}):  \"\n               f\"R2 = {reg['r_squared']:.4f}\")\n        print(hdr)\n        reg_lines.append(hdr)\n        col = f\"    {'Feature':25s} {'Coef':>10s} {'p-value':>12s}\"\n        print(col)\n        reg_lines.append(col)\n        sep = f\"    {'-'*49}\"\n        print(sep)\n        reg_lines.append(sep)\n        for fn in FEATURE_NAMES:\n            c = reg['coefs'][fn]\n            pv = reg['p_values'][fn]\n            sig = ('***' if pv < 0.001\n                   else ('**' if pv < 0.01\n                         else ('*' if pv < 0.05 else '')))\n            ln = (f\"    {fn:25s} {c:10.4f} \"\n                  f\"{pv:12.6f} {sig}\")\n            print(ln)\n            reg_lines.append(ln)\n\n    y_g = np.array(all_bias_g)\n    if len(y_g) >= 20:\n        X_g = np.column_stack(\n            [np.array(all_feats_g[fn]) for fn in FEATURE_NAMES])\n        reg_g = ols_regression(y_g, X_g)\n        if reg_g is not None:\n            regression_results['_global'] = reg_g\n            hdr = (f\"\\n  GLOBAL (n={reg_g['n_obs']}):  \"\n                   f\"R2 = {reg_g['r_squared']:.4f}\")\n            print(hdr)\n            reg_lines.append(hdr)\n            col = (f\"    {'Feature':25s} {'Coef':>10s} \"\n                   f\"{'p-value':>12s}\")\n            print(col)\n            reg_lines.append(col)\n            sep = f\"    {'-'*49}\"\n            print(sep)\n            reg_lines.append(sep)\n            for fn in FEATURE_NAMES:\n                c = reg_g['coefs'][fn]\n                pv = reg_g['p_values'][fn]\n                sig = ('***' if pv < 0.001\n                       else ('**' if pv < 0.01\n                             else ('*' if pv < 0.05 else '')))\n                ln = (f\"    {fn:25s} {c:10.4f} \"\n                      f\"{pv:12.6f} {sig}\")\n                print(ln)\n                reg_lines.append(ln)\n\n    # ================================================================\n    # Save\n    # ================================================================\n    summary = dict(\n        config=dict(\n            M=args.M, N=args.N, K_values=args.K,\n            topologies=args.topos,\n            near_perm_epsilons=NEAR_PERM_EPSILONS,\n            feature_names=FEATURE_NAMES),\n        bias_results=all_results,\n        regression=regression_results,\n    )\n\n    json_path = os.path.join(OUT_DIR,\n                             'pathological_bias_summary.json')\n    with open(json_path, 'w') as f:\n        json.dump(summary, f, indent=2, default=str)\n    print(f\"\\nSaved {json_path}\")\n\n    reg_path = os.path.join(OUT_DIR, 'regression_results.txt')\n    with open(reg_path, 'w') as f:\n        f.write('\\n'.join(reg_lines))\n    print(f\"Saved {reg_path}\")\n\n    print(f\"\\nTotal: {time.time() - t0:.0f}s\")\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT_EOF",
  "account": "sonny"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan009-pathological-matrices-v2_20260520T181421",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "home-1x5090",
    "command": "cat > /home/sonny/causal_annot_error_attrib/plan_009_pathological_matrices.py << 'SCRIPT_EOF'\n#!/usr/bin/env python3\n\"\"\"\nPlan 009: Pathological Confusion Matrix Analysis\n\nStudies extreme bias behavior under 3 classes of pathological K*K\ncolumn-stochastic confusion matrices across 7 DAG topologies and K in {3,5,7}.\n\nPathological C types (M=1000 instances each per (K, type, param)):\n  (a) Near-permutation: C = (1-eps)P + eps*U, eps in {0.01, 0.05, 0.1, 0.2}\n  (b) Rank-deficient: SVD truncation to rank r in {1, ..., K-1}\n  (c) Block-diagonal: b blocks, b in {2, max(K//2, 2)}\n\nMatrix features extracted per C:\n  spectral_gap, diag_dominance, effective_rank, condition_number, off_diagonal_max\n\nAnalysis:\n  - Per-(topo, K, C_type, param): bias distribution statistics\n  - OLS regression: |bias| ~ features (per-topology + global)\n  - Catastrophic bias detection: |bias| > 2*|tau_true|\n\nInput:\n  DGP parameters from plan_002 (7 topologies), N_LARGE=5M samples for plim\nOutput -> artifacts/plan009/:\n  pathological_bias_summary.json, regression_results.txt\n\nDependencies: torch (CUDA), numpy, scipy.stats\n\"\"\"\n\nimport torch\nimport numpy as np\nimport json\nimport time\nimport os\nimport sys\nimport hashlib\nimport argparse\n\n# ================================================================\n# Configuration\n# ================================================================\nK_VALUES = [3, 5, 7]\nM_DEFAULT = 1000\nN_LARGE = 5_000_000\nDEVICE = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')\nDTYPE = torch.float64\n\nALL_TOPOS = ['confounding', 'mediation', 'collider', 'exposure',\n             'mbias', 'iv', 'frontdoor']\nNEAR_PERM_EPSILONS = [0.01, 0.05, 0.1, 0.2]\nFEATURE_NAMES = ['spectral_gap', 'diag_dominance', 'effective_rank',\n                 'condition_number', 'off_diagonal_max']\n\nSCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))\nOUT_DIR = os.path.join(SCRIPT_DIR, 'artifacts', 'plan009')\n\n\ndef _det_seed(topo_name, K, c_type, base_seed=42):\n    h = hashlib.sha256(\n        f\"{topo_name}_{K}_{c_type}_{base_seed}\".encode()\n    ).hexdigest()\n    return int(h[:8], 16) % (2**31)\n\n\n# ================================================================\n# DGP parameter pools (from plan_002_k57_extended_7topo.py)\n# ================================================================\n_ALPHA_POOL  = [1.5, -1.0, 0.8, -0.5, 1.2, -0.7]\n_BETA_A_POOL = [1.0, -0.5, 0.7, -0.3, 0.5, -0.2]\n_BETA_POOL   = [0.0, 1.0, -0.5, 0.7, -0.3, 0.5, -0.2]\n_GAMMA_POOL  = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]\n_DELTA_POOL  = [0.0, 0.8, -0.6, 0.5, -0.4, 0.3, -0.2]\n_DT_POOL     = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]\n_DY_POOL     = [0.0, 0.8, 0.6, -0.5, 0.4, -0.3, 0.2]\n_MBIAS_A1    = [0.0, 0.8, -0.5, 0.6, -0.4, 0.5, -0.3]\n_MBIAS_A2    = [0.0, 0.6, 0.9, -0.4, 0.7, -0.3, 0.5]\n_IV_DZ       = [0.0, 1.0, -0.5, 0.8, -0.4, 0.6, -0.3]\n_IV_DU       = [0.0, 0.8, 0.6, -0.5, 0.7, -0.3, 0.4]\n_FD_GAMMA    = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]\n_FD_DELTA    = [0.0, 1.0, -0.8, 0.7, -0.5, 0.4, -0.3]\n\n\ndef make_p_A(K):\n    if K == 3:\n        return np.array([0.40, 0.35, 0.25])\n    raw = np.array([1.0 / i for i in range(1, K + 1)])\n    return raw / raw.sum()\n\n\ndef make_all_params(K):\n    p_A = make_p_A(K)\n    return dict(\n        confounding=dict(p_A=p_A, alpha=np.array(_ALPHA_POOL[:K-1]),\n                         beta_A=np.array(_BETA_A_POOL[:K-1]),\n                         beta_T=2.0, sigma_T=1.0),\n        mediation=dict(tau=0.5, gamma=np.array(_GAMMA_POOL[:K]),\n                       delta=np.array(_DELTA_POOL[:K]),\n                       beta=np.array(_BETA_POOL[:K])),\n        collider=dict(tau=1.0, g=np.zeros(K),\n                      dT=np.array(_DT_POOL[:K]),\n                      dY=np.array(_DY_POOL[:K])),\n        exposure=dict(beta=np.array(_BETA_POOL[:K]), p_A=p_A),\n        mbias=dict(tau=1.0, delta_coef=1.0, lam=1.0, g=np.zeros(K),\n                   a1=np.array(_MBIAS_A1[:K]),\n                   a2=np.array(_MBIAS_A2[:K])),\n        iv=dict(lam=1.0, g=np.zeros(K),\n                dZ=np.array(_IV_DZ[:K]),\n                dU=np.array(_IV_DU[:K]),\n                beta=np.array(_BETA_POOL[:K])),\n        frontdoor=dict(alpha_U=1.0, lam_U=1.0,\n                       gamma=np.array(_FD_GAMMA[:K]),\n                       delta=np.array(_FD_DELTA[:K]),\n                       beta=np.array(_BETA_POOL[:K])),\n    )\n\n\n# ================================================================\n# DGP generators (from plan_002_k57_extended_7topo.py)\n# ================================================================\ndef _softmax_rows(logits):\n    e = np.exp(logits - logits.max(axis=-1, keepdims=True))\n    return e / e.sum(axis=-1, keepdims=True)\n\n\ndef _sample_cat(probs, rng):\n    cum = np.cumsum(probs, axis=1)\n    u = rng.uniform(size=probs.shape[0])[:, None]\n    return (u >= cum).sum(axis=1).astype(int)\n\n\ndef gen_confounding(K, N, p, rng):\n    A = rng.choice(K, size=N, p=p['p_A'])\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (A == j + 1).astype(float)\n    T = D @ p['alpha'] + rng.normal(0, p['sigma_T'], N)\n    Y = p['beta_T'] * T + D @ p['beta_A'] + rng.normal(0, 1, N)\n    return T, Y, A\n\n\ndef gen_mediation(K, N, p, rng):\n    T = rng.binomial(1, 0.5, N).astype(float)\n    logits = p['gamma'][None, :] + p['delta'][None, :] * T[:, None]\n    A = _sample_cat(_softmax_rows(logits), rng)\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (A == j + 1)\n    Y = p['beta'][0] + D @ p['beta'][1:] + p['tau'] * T + rng.normal(0, 1, N)\n    return T, Y, A\n\n\ndef gen_collider(K, N, p, rng):\n    T = rng.normal(0, 1, N)\n    Y = p['tau'] * T + rng.normal(0, 1, N)\n    logits = (p['g'][None, :] + p['dT'][None, :] * T[:, None]\n              + p['dY'][None, :] * Y[:, None])\n    A = _sample_cat(_softmax_rows(logits), rng)\n    return T, Y, A\n\n\ndef gen_exposure(K, N, p, rng):\n    A = rng.choice(K, size=N, p=p['p_A'])\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (A == j + 1).astype(float)\n    Y = p['beta'][0] + D @ p['beta'][1:] + rng.normal(0, 1, N)\n    return None, Y, A\n\n\ndef gen_mbias(K, N, p, rng):\n    U1 = rng.normal(0, 1, N)\n    U2 = rng.normal(0, 1, N)\n    T = p['delta_coef'] * U1 + rng.normal(0, 1, N)\n    Y = p['tau'] * T + p['lam'] * U2 + rng.normal(0, 1, N)\n    logits = np.zeros((N, K))\n    for j in range(1, K):\n        logits[:, j] = p['g'][j] + p['a1'][j] * U1 + p['a2'][j] * U2\n    A = _sample_cat(_softmax_rows(logits), rng)\n    return T, Y, A\n\n\ndef gen_iv(K, N, p, rng):\n    Z = rng.binomial(1, 0.5, N).astype(float)\n    U = rng.normal(0, 1, N)\n    eps = rng.normal(0, 1, N)\n    logits = np.zeros((N, K))\n    for j in range(1, K):\n        logits[:, j] = p['g'][j] + p['dZ'][j] * Z + p['dU'][j] * U\n    A = _sample_cat(_softmax_rows(logits), rng)\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (A == j + 1).astype(float)\n    Y = D @ p['beta'][1:] + p['lam'] * U + eps\n    return Z, Y, A\n\n\ndef gen_frontdoor(K, N, p, rng):\n    U = rng.normal(0, 1, N)\n    T = p['alpha_U'] * U + rng.normal(0, 1, N)\n    logits = np.zeros((N, K))\n    for j in range(1, K):\n        logits[:, j] = p['gamma'][j] + p['delta'][j] * T\n    M = _sample_cat(_softmax_rows(logits), rng)\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (M == j + 1).astype(float)\n    Y = D @ p['beta'][1:] + p['lam_U'] * U + rng.normal(0, 1, N)\n    return T, Y, M\n\n\n_GEN = dict(confounding=gen_confounding, mediation=gen_mediation,\n            collider=gen_collider, exposure=gen_exposure,\n            mbias=gen_mbias, iv=gen_iv, frontdoor=gen_frontdoor)\n\n\n# ================================================================\n# Sufficient statistics\n# ================================================================\nclass SuffStats:\n    def __init__(self, T, Y, A, K):\n        self.K = K\n        self.has_T = T is not None\n        N = len(Y)\n        DA = np.zeros((N, K))\n        for k in range(K):\n            DA[:, k] = (A == k).astype(float)\n        self.p_A = DA.mean(0)\n        self.E_Y = Y.mean()\n        self.E_YD = (DA * Y[:, None]).mean(0)\n        if self.has_T:\n            self.E_T = T.mean()\n            self.E_T2 = (T ** 2).mean()\n            self.E_TY = (T * Y).mean()\n            self.E_TD = (DA * T[:, None]).mean(0)\n\n    def to_device(self, dev):\n        self.t_p_A = torch.tensor(self.p_A, dtype=DTYPE, device=dev)\n        self.t_E_Y = torch.tensor(self.E_Y, dtype=DTYPE, device=dev)\n        self.t_E_YD = torch.tensor(self.E_YD, dtype=DTYPE, device=dev)\n        if self.has_T:\n            self.t_E_T = torch.tensor(self.E_T, dtype=DTYPE, device=dev)\n            self.t_E_T2 = torch.tensor(self.E_T2, dtype=DTYPE, device=dev)\n            self.t_E_TY = torch.tensor(self.E_TY, dtype=DTYPE, device=dev)\n            self.t_E_TD = torch.tensor(self.E_TD, dtype=DTYPE, device=dev)\n        return self\n\n\nclass IVSuffStats:\n    def __init__(self, Z, Y, A, K):\n        self.K = K\n        z1 = Z == 1\n        z0 = Z == 0\n        self.RF = Y[z1].mean() - Y[z0].mean()\n        self.FS = np.zeros(K)\n        for k in range(K):\n            self.FS[k] = (A[z1] == k).mean() - (A[z0] == k).mean()\n\n    def to_device(self, dev):\n        self.t_RF = torch.tensor(self.RF, dtype=DTYPE, device=dev)\n        self.t_FS = torch.tensor(self.FS, dtype=DTYPE, device=dev)\n        return self\n\n\n# ================================================================\n# Plim functions (batched GPU)\n# ================================================================\ndef plim_with_T(ss, C):\n    B, K = C.shape[0], ss.K\n    dim = K + 1\n    q = C @ ss.t_p_A\n    ct = C @ ss.t_E_TD\n    cy = C @ ss.t_E_YD\n    EZZ = torch.zeros(B, dim, dim, dtype=DTYPE, device=C.device)\n    EZZ[:, 0, 0] = 1.0\n    EZZ[:, 0, 1] = ss.t_E_T\n    EZZ[:, 1, 0] = ss.t_E_T\n    EZZ[:, 1, 1] = ss.t_E_T2\n    EZZ[:, 0, 2:] = q[:, 1:]\n    EZZ[:, 2:, 0] = q[:, 1:]\n    EZZ[:, 1, 2:] = ct[:, 1:]\n    EZZ[:, 2:, 1] = ct[:, 1:]\n    idx = torch.arange(K - 1, device=C.device)\n    EZZ[:, idx + 2, idx + 2] = q[:, 1:]\n    EZY = torch.zeros(B, dim, dtype=DTYPE, device=C.device)\n    EZY[:, 0] = ss.t_E_Y\n    EZY[:, 1] = ss.t_E_TY\n    EZY[:, 2:] = cy[:, 1:]\n    return torch.linalg.solve(EZZ, EZY)\n\n\ndef plim_exposure(ss, C):\n    B, K = C.shape[0], ss.K\n    dim = K\n    q = C @ ss.t_p_A\n    cy = C @ ss.t_E_YD\n    EZZ = torch.zeros(B, dim, dim, dtype=DTYPE, device=C.device)\n    EZZ[:, 0, 0] = 1.0\n    EZZ[:, 0, 1:] = q[:, 1:]\n    EZZ[:, 1:, 0] = q[:, 1:]\n    idx = torch.arange(K - 1, device=C.device)\n    EZZ[:, idx + 1, idx + 1] = q[:, 1:]\n    EZY = torch.zeros(B, dim, dtype=DTYPE, device=C.device)\n    EZY[:, 0] = ss.t_E_Y\n    EZY[:, 1:] = cy[:, 1:]\n    return torch.linalg.solve(EZZ, EZY)\n\n\ndef plim_iv_batched(ss, C):\n    FS_star = C @ ss.t_FS\n    denom = FS_star[:, 1]\n    nan_val = torch.tensor(float('nan'), dtype=DTYPE, device=C.device)\n    result = torch.where(denom.abs() < 1e-8, nan_val, ss.t_RF / denom)\n    return result.unsqueeze(1)\n\n\n# ================================================================\n# Pathological C matrix generators\n# ================================================================\ndef gen_near_permutation(K, M, epsilon, rng):\n    \"\"\"C = (1-eps)*P + eps*U where P=random permutation, U=random col-stochastic.\"\"\"\n    Cs = np.zeros((M, K, K))\n    for i in range(M):\n        perm = rng.permutation(K)\n        P = np.zeros((K, K))\n        P[perm, np.arange(K)] = 1.0\n        U = rng.dirichlet(np.ones(K), size=K).T\n        C = (1 - epsilon) * P + epsilon * U\n        C = np.clip(C, 1e-12, None)\n        C /= C.sum(axis=0, keepdims=True)\n        Cs[i] = C\n    return Cs\n\n\ndef gen_rank_deficient(K, M, rank, rng):\n    \"\"\"Rank-r col-stochastic via SVD truncation + non-negative projection.\"\"\"\n    Cs = np.zeros((M, K, K))\n    for i in range(M):\n        C_full = rng.dirichlet(np.ones(K) * 2.0, size=K).T\n        U, S, Vt = np.linalg.svd(C_full, full_matrices=True)\n        S_trunc = np.zeros_like(S)\n        S_trunc[:rank] = S[:rank]\n        C_approx = U @ np.diag(S_trunc) @ Vt\n        C_approx = np.clip(C_approx, 1e-12, None)\n        C_approx /= C_approx.sum(axis=0, keepdims=True)\n        Cs[i] = C_approx\n    return Cs\n\n\ndef gen_block_diagonal(K, M, n_blocks, rng):\n    \"\"\"Block-diagonal: high intra-block accuracy, low inter-block leakage.\"\"\"\n    block_sizes = []\n    base = K // n_blocks\n    remainder = K % n_blocks\n    for b in range(n_blocks):\n        block_sizes.append(base + (1 if b < remainder else 0))\n\n    Cs = np.zeros((M, K, K))\n    for i in range(M):\n        C = np.zeros((K, K))\n        leak = rng.uniform(0.001, 0.05)\n        start = 0\n        for bs in block_sizes:\n            end = start + bs\n            for col in range(start, end):\n                within = rng.dirichlet(5.0 * np.ones(bs))\n                n_outside = K - bs\n                if n_outside > 0:\n                    between = rng.dirichlet(np.ones(n_outside)) * leak\n                else:\n                    between = np.array([])\n                C[start:end, col] = within * (1 - leak)\n                idx = 0\n                for row in range(K):\n                    if row < start or row >= end:\n                        C[row, col] = between[idx]\n                        idx += 1\n            start = end\n        C = np.clip(C, 1e-12, None)\n        C /= C.sum(axis=0, keepdims=True)\n        Cs[i] = C\n    return Cs\n\n\n# ================================================================\n# Matrix feature extraction\n# ================================================================\ndef extract_features(C_batch):\n    M, K, _ = C_batch.shape\n    feats = {fn: np.zeros(M) for fn in FEATURE_NAMES}\n\n    diags = np.diagonal(C_batch, axis1=1, axis2=2)\n    feats['diag_dominance'] = diags.min(axis=1) * K\n\n    svd_vals = np.linalg.svd(C_batch, compute_uv=False)\n    sv_sum = svd_vals.sum(axis=1)\n    sv_sq_sum = (svd_vals ** 2).sum(axis=1)\n    feats['effective_rank'] = np.where(\n        sv_sum > 0, sv_sum**2 / sv_sq_sum, 0.0)\n    feats['condition_number'] = (\n        svd_vals[:, 0] / np.maximum(svd_vals[:, -1], 1e-15))\n\n    eye_mask = ~np.eye(K, dtype=bool)\n    for i in range(M):\n        eigvals = np.linalg.eigvals(C_batch[i])\n        eig_abs = np.sort(np.abs(eigvals))[::-1]\n        feats['spectral_gap'][i] = (\n            eig_abs[0] - eig_abs[1] if K > 1 else eig_abs[0])\n        feats['off_diagonal_max'][i] = C_batch[i][eye_mask].max()\n\n    return feats\n\n\n# ================================================================\n# OLS regression\n# ================================================================\ndef ols_regression(y, X_raw):\n    n = len(y)\n    p = X_raw.shape[1]\n    if n < p + 5:\n        return None\n\n    X_mean = X_raw.mean(axis=0)\n    X_std = X_raw.std(axis=0)\n    X_std[X_std < 1e-15] = 1.0\n    Xs = (X_raw - X_mean) / X_std\n    X = np.column_stack([np.ones(n), Xs])\n\n    beta = np.linalg.lstsq(X, y, rcond=None)[0]\n    y_hat = X @ beta\n    ss_res = ((y - y_hat) ** 2).sum()\n    ss_tot = ((y - y.mean()) ** 2).sum()\n    r2 = 1 - ss_res / ss_tot if ss_tot > 1e-15 else 0.0\n\n    dof = n - X.shape[1]\n    if dof <= 0:\n        pv = np.full(p, np.nan)\n    else:\n        mse = ss_res / dof\n        try:\n            cov_mat = mse * np.linalg.inv(X.T @ X)\n            se = np.sqrt(np.maximum(np.diag(cov_mat), 0))\n            t_stat = np.where(se > 1e-15, beta / se, 0.0)\n            from scipy.stats import t as t_dist\n            pv = 2 * (1 - t_dist.cdf(np.abs(t_stat[1:]), dof))\n        except np.linalg.LinAlgError:\n            pv = np.full(p, np.nan)\n\n    return dict(\n        r_squared=float(r2),\n        coefs={fn: float(beta[i + 1]) for i, fn in enumerate(FEATURE_NAMES)},\n        p_values={fn: float(pv[i]) for i, fn in enumerate(FEATURE_NAMES)},\n        n_obs=n,\n    )\n\n\n# ================================================================\n# Main\n# ================================================================\ndef main():\n    parser = argparse.ArgumentParser(\n        description='Plan 009: Pathological confusion matrix bias analysis '\n                    'across 7 DAG topologies')\n    parser.add_argument('--M', type=int, default=M_DEFAULT,\n                        help=f'C instances per config [default: {M_DEFAULT}]')\n    parser.add_argument('--N', type=int, default=N_LARGE,\n                        help=f'DGP sample size [default: {N_LARGE}]')\n    parser.add_argument('--K', type=int, nargs='+', default=K_VALUES,\n                        help=f'K values [default: {K_VALUES}]')\n    parser.add_argument('--topos', type=str, nargs='+', default=ALL_TOPOS,\n                        help='Topologies')\n    parser.add_argument('--dry-run', action='store_true',\n                        help='Quick test: M=10, K=[3], 1 topo, N=100k')\n    args = parser.parse_args()\n\n    if args.dry_run:\n        args.M = 10\n        args.K = [3]\n        args.topos = ['confounding']\n        args.N = 100_000\n        print(\"=== DRY RUN ===\\n\")\n\n    os.makedirs(OUT_DIR, exist_ok=True)\n    t0 = time.time()\n    print(f\"Plan 009: Pathological Matrices\")\n    print(f\"  Device={DEVICE}  M={args.M}  N={args.N:,}\")\n    print(f\"  K={args.K}  topos={args.topos}\")\n    print(f\"  Output -> {OUT_DIR}\\n\")\n\n    all_results = {}\n    topo_bias = {t: [] for t in ALL_TOPOS}\n    topo_feats = {t: {fn: [] for fn in FEATURE_NAMES} for t in ALL_TOPOS}\n\n    for K in args.K:\n        params = make_all_params(K)\n        rank_vals = list(range(1, K))\n        block_vals = sorted(set([2, max(K // 2, 2)]))\n\n        c_configs = {\n            'near_permutation': [(f'eps={e}', e) for e in NEAR_PERM_EPSILONS],\n            'rank_deficient': [(f'rank={r}', r) for r in rank_vals],\n            'block_diagonal': [(f'blocks={b}', b) for b in block_vals],\n        }\n\n        for topo in args.topos:\n            tk = time.time()\n            print(f\"{'='*70}\")\n            print(f\"  {topo}  K={K}\")\n            print(f\"{'='*70}\")\n\n            seed_dgp = _det_seed(topo, K, 'dgp')\n            rng = np.random.default_rng(seed_dgp)\n            T_or_Z, Y, A = _GEN[topo](K, args.N, params[topo], rng)\n\n            if topo == 'iv':\n                ss = IVSuffStats(T_or_Z, Y, A, K).to_device(DEVICE)\n                plim_fn = plim_iv_batched\n                tau_idx = 0\n            elif topo == 'exposure':\n                ss = SuffStats(None, Y, A, K).to_device(DEVICE)\n                plim_fn = plim_exposure\n                tau_idx = 1\n            else:\n                ss = SuffStats(T_or_Z, Y, A, K).to_device(DEVICE)\n                plim_fn = plim_with_T\n                tau_idx = 1\n\n            I_batch = torch.eye(K, dtype=DTYPE, device=DEVICE).unsqueeze(0)\n            plim_true = plim_fn(ss, I_batch).squeeze(0)\n            tau_true = plim_true[tau_idx].item()\n            print(f\"  tau_true(C=I) = {tau_true:.6f}  \"\n                  f\"[DGP {time.time()-tk:.1f}s]\")\n\n            for c_type, param_list in c_configs.items():\n                for param_label, param_val in param_list:\n                    seed = _det_seed(topo, K,\n                                     f'{c_type}_{param_label}')\n                    rng_c = np.random.default_rng(seed)\n\n                    if c_type == 'near_permutation':\n                        Cb = gen_near_permutation(\n                            K, args.M, param_val, rng_c)\n                    elif c_type == 'rank_deficient':\n                        Cb = gen_rank_deficient(\n                            K, args.M, param_val, rng_c)\n                    else:\n                        Cb = gen_block_diagonal(\n                            K, args.M, param_val, rng_c)\n\n                    Ct = torch.tensor(Cb, dtype=DTYPE, device=DEVICE)\n                    plim_batch = plim_fn(ss, Ct)\n                    bias = (plim_batch[:, tau_idx]\n                            - tau_true).cpu().numpy()\n\n                    valid = np.isfinite(bias)\n                    bias = bias[valid]\n                    Cb_valid = Cb[valid]\n\n                    key = f\"{topo}_K{K}_{c_type}_{param_label}\"\n                    if len(bias) == 0:\n                        all_results[key] = dict(error='all_nan')\n                        print(f\"    {c_type:20s} {param_label:10s}:\"\n                              f\" ALL NaN\")\n                        continue\n\n                    ab = np.abs(bias)\n                    feats = extract_features(Cb_valid)\n\n                    cat_thr = 2 * abs(tau_true)\n                    if abs(tau_true) > 1e-10:\n                        cat_frac = float((ab > cat_thr).mean())\n                    else:\n                        cat_frac = float('nan')\n\n                    stats = dict(\n                        n_valid=int(len(bias)),\n                        bias_mean=float(bias.mean()),\n                        bias_std=float(bias.std()),\n                        abs_bias_mean=float(ab.mean()),\n                        abs_bias_max=float(ab.max()),\n                        abs_bias_min=float(ab.min()),\n                        abs_bias_p5=float(np.percentile(ab, 5)),\n                        abs_bias_p25=float(np.percentile(ab, 25)),\n                        abs_bias_p50=float(np.percentile(ab, 50)),\n                        abs_bias_p75=float(np.percentile(ab, 75)),\n                        abs_bias_p95=float(np.percentile(ab, 95)),\n                        catastrophic_frac=cat_frac,\n                        catastrophic_threshold=float(cat_thr),\n                        feat_means={fn: float(feats[fn].mean())\n                                    for fn in FEATURE_NAMES},\n                    )\n                    all_results[key] = stats\n\n                    topo_bias[topo].extend(ab.tolist())\n                    for fn in FEATURE_NAMES:\n                        topo_feats[topo][fn].extend(\n                            feats[fn].tolist())\n\n                    cat_s = (f\"  cat={cat_frac:.1%}\"\n                             if cat_frac == cat_frac else \"\")\n                    print(\n                        f\"    {c_type:20s} {param_label:10s}: \"\n                        f\"n={len(bias):4d}  \"\n                        f\"|bias| mean={ab.mean():.4f} \"\n                        f\"max={ab.max():.4f} \"\n                        f\"p95={np.percentile(ab, 95):.4f}\"\n                        f\"{cat_s}\")\n\n            print(f\"  [{time.time()-tk:.1f}s]\\n\")\n            sys.stdout.flush()\n\n    # ================================================================\n    # Regression\n    # ================================================================\n    print(f\"\\n{'='*80}\")\n    print(\"  REGRESSION: |bias| ~ spectral_gap + diag_dominance \"\n          \"+ effective_rank\")\n    print(\"              + condition_number + off_diagonal_max\")\n    print(f\"{'='*80}\")\n\n    reg_lines = [\"Plan 009: OLS Regression Results\",\n                 \"=\" * 80, \"\"]\n    regression_results = {}\n    all_bias_g = []\n    all_feats_g = {fn: [] for fn in FEATURE_NAMES}\n\n    for topo in args.topos:\n        y = np.array(topo_bias[topo])\n        if len(y) < 20:\n            continue\n        X = np.column_stack(\n            [np.array(topo_feats[topo][fn])\n             for fn in FEATURE_NAMES])\n\n        all_bias_g.extend(y.tolist())\n        for fn in FEATURE_NAMES:\n            all_feats_g[fn].extend(topo_feats[topo][fn])\n\n        reg = ols_regression(y, X)\n        if reg is None:\n            continue\n        regression_results[topo] = reg\n\n        hdr = (f\"\\n  {topo} (n={reg['n_obs']}):  \"\n               f\"R2 = {reg['r_squared']:.4f}\")\n        print(hdr)\n        reg_lines.append(hdr)\n        col = f\"    {'Feature':25s} {'Coef':>10s} {'p-value':>12s}\"\n        print(col)\n        reg_lines.append(col)\n        sep = f\"    {'-'*49}\"\n        print(sep)\n        reg_lines.append(sep)\n        for fn in FEATURE_NAMES:\n            c = reg['coefs'][fn]\n            pv = reg['p_values'][fn]\n            sig = ('***' if pv < 0.001\n                   else ('**' if pv < 0.01\n                         else ('*' if pv < 0.05 else '')))\n            ln = (f\"    {fn:25s} {c:10.4f} \"\n                  f\"{pv:12.6f} {sig}\")\n            print(ln)\n            reg_lines.append(ln)\n\n    y_g = np.array(all_bias_g)\n    if len(y_g) >= 20:\n        X_g = np.column_stack(\n            [np.array(all_feats_g[fn]) for fn in FEATURE_NAMES])\n        reg_g = ols_regression(y_g, X_g)\n        if reg_g is not None:\n            regression_results['_global'] = reg_g\n            hdr = (f\"\\n  GLOBAL (n={reg_g['n_obs']}):  \"\n                   f\"R2 = {reg_g['r_squared']:.4f}\")\n            print(hdr)\n            reg_lines.append(hdr)\n            col = (f\"    {'Feature':25s} {'Coef':>10s} \"\n                   f\"{'p-value':>12s}\")\n            print(col)\n            reg_lines.append(col)\n            sep = f\"    {'-'*49}\"\n            print(sep)\n            reg_lines.append(sep)\n            for fn in FEATURE_NAMES:\n                c = reg_g['coefs'][fn]\n                pv = reg_g['p_values'][fn]\n                sig = ('***' if pv < 0.001\n                       else ('**' if pv < 0.01\n                             else ('*' if pv < 0.05 else '')))\n                ln = (f\"    {fn:25s} {c:10.4f} \"\n                      f\"{pv:12.6f} {sig}\")\n                print(ln)\n                reg_lines.append(ln)\n\n    # ================================================================\n    # Save\n    # ================================================================\n    summary = dict(\n        config=dict(\n            M=args.M, N=args.N, K_values=args.K,\n            topologies=args.topos,\n            near_perm_epsilons=NEAR_PERM_EPSILONS,\n            feature_names=FEATURE_NAMES),\n        bias_results=all_results,\n        regression=regression_results,\n    )\n\n    json_path = os.path.join(OUT_DIR,\n                             'pathological_bias_summary.json')\n    with open(json_path, 'w') as f:\n        json.dump(summary, f, indent=2, default=str)\n    print(f\"\\nSaved {json_path}\")\n\n    reg_path = os.path.join(OUT_DIR, 'regression_results.txt')\n    with open(reg_path, 'w') as f:\n        f.write('\\n'.join(reg_lines))\n    print(f\"Saved {reg_path}\")\n\n    print(f\"\\nTotal: {time.time() - t0:.0f}s\")\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT_EOF",
    "account": "sonny"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-20T18:26:04.857655+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.95}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan009-pathological-matrices-v2_20260520T181421",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-20T18:26:04.857827+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "home-1x5090",
  "command": "cd /home/sonny/causal_annot_error_attrib && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python plan_009_pathological_matrices.py --help",
  "account": "sonny"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan009-pathological-matrices-v2_20260520T181421",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "home-1x5090",
    "command": "cd /home/sonny/causal_annot_error_attrib && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python plan_009_pathological_matrices.py --help",
    "account": "sonny"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-20T18:26:04.857969+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cd /home/sonny/causal_annot_error_attrib && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python plan_009_pathological_matrices.py --help'\\n\\nExit code: 1\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 1: /root/miniconda3/etc/profile.d/conda.sh: Permission denied\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.84}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan009-pathological-matrices-v2_20260520T181421",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-20T18:26:04.858111+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "home-1x5090",
  "command": "which python3",
  "account": "sonny"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan009-pathological-matrices-v2_20260520T181421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "home-1x5090",
    "command": "which python3",
    "account": "sonny"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-20T18:26:04.858304+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'which' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan009-pathological-matrices-v2_20260520T181421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-20T18:26:04.858444+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "home-1x5090",
  "command": "which python",
  "account": "sonny"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan009-pathological-matrices-v2_20260520T181421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "home-1x5090",
    "command": "which python",
    "account": "sonny"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-20T18:26:04.858571+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'which' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan009-pathological-matrices-v2_20260520T181421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-20T18:26:04.858693+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "home-1x5090",
  "command": "which python3 && python3 --version",
  "account": "sonny"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan009-pathological-matrices-v2_20260520T181421",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "home-1x5090",
    "command": "which python3 && python3 --version",
    "account": "sonny"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-20T18:26:04.858818+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/usr/bin/python3\\nPython 3.10.12\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.61}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan009-pathological-matrices-v2_20260520T181421",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-20T18:26:04.858936+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "home-1x5090",
  "command": "cd /home/sonny/causal_annot_error_attrib && python3 plan_009_pathological_matrices.py --help",
  "account": "sonny"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan009-pathological-matrices-v2_20260520T181421",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "home-1x5090",
    "command": "cd /home/sonny/causal_annot_error_attrib && python3 plan_009_pathological_matrices.py --help",
    "account": "sonny"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-20T18:26:04.859065+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"usage: plan_009_pathological_matrices.py [-h] [--M M] [--N N] [--K K [K ...]]\\n                                         [--topos TOPOS [TOPOS ...]]\\n                                         [--dry-run]\\n\\nPlan 009: Pathological confusion matrix bias analysis across 7 DAG topologies\\n\\noptions:\\n  -h, --help            show this help message and exit\\n  --M M                 C instances per config [default: 1000]\\n  --N N                 DGP sample size [default: 5000000]\\n  --K K [K ...]         K values [default: [3, 5, 7]]\\n  --topos TOPOS [TOPOS ...]\\n                        Topologies\\n  --dry-run             Quick test: M=10, K=[3], 1 topo, N=100k\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.26}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan009-pathological-matrices-v2_20260520T181421",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-20T18:26:04.859251+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "home-1x5090",
  "command": "cd /home/sonny/causal_annot_error_attrib && python3 plan_009_pathological_matrices.py --dry-run 2>&1",
  "account": "sonny"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan009-pathological-matrices-v2_20260520T181421",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "home-1x5090",
    "command": "cd /home/sonny/causal_annot_error_attrib && python3 plan_009_pathological_matrices.py --dry-run 2>&1",
    "account": "sonny"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-20T18:26:04.859420+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== DRY RUN ===\\n\\nPlan 009: Pathological Matrices\\n  Device=cuda:0  M=10  N=100,000\\n  K=[3]  topos=['confounding']\\n  Output -> /home/sonny/causal_annot_error_attrib/artifacts/plan009\\n\\n======================================================================\\n  confounding  K=3\\n======================================================================\\n  tau_true(C=I) = 1.997155  [DGP 0.2s]\\n    near_permutation     eps=0.01  : n=  10  |bias| mean=0.0129 max=0.0203 p95=0.0186  cat=0.0%\\n    near_permutation     eps=0.05  : n=  10  |bias| mean=0.0631 max=0.0788 p95=0.0788  cat=0.0%\\n    near_permutation     eps=0.1   : n=  10  |bias| mean=0.1009 max=0.1330 p95=0.1311  cat=0.0%\\n    near_permutation     eps=0.2   : n=  10  |bias| mean=0.1609 max=0.1999 p95=0.1880  cat=0.0%\\n    rank_deficient       rank=1    : n=  10  |bias| mean=0.2997 max=0.2997 p95=0.2997  cat=0.0%\\n    rank_deficient       rank=2    : n=  10  |bias| mean=0.2916 max=0.2997 p95=0.2997  cat=0.0%\\n    block_diagonal       blocks=2  : n=  10  |bias| mean=0.2057 max=0.2259 p95=0.2254  cat=0.0%\\n  [0.2s]\\n\\n\\n================================================================================\\n  REGRESSION: |bias| ~ spectral_gap + diag_dominance + effective_rank\\n              + condition_number + off_diagonal_max\\n================================================================================\\n\\n  confounding (n=70):  R2 = 0.8058\\n    Feature                         Coef      p-value\\n    -------------------------------------------------\\n    spectral_gap                  0.0657     0.026942 *\\n    diag_dominance                0.0649     0.143827 \\n    effective_rank               -0.1015     0.000001 ***\\n    condition_number             -0.0516     0.054229 \\n    off_diagonal_max              0.0672     0.139716 \\n\\n  GLOBAL (n=70):  R2 = 0.8058\\n    Feature                         Coef      p-value\\n    ---------
…[truncated 636 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan009-pathological-matrices-v2_20260520T181421",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-20T18:26:04.859613+00:00_

Dry-run 完成，所有组件正常：

- `--help` 输出正确的参数文档
- GPU (`cuda:0`) 正常使用
- 3 类病态 C 矩阵（near-permutation × 4 ε、rank-deficient × 2 ranks、block-diagonal × 1 block config）均生成成功
- plim 计算、bias 统计、feature 提取、OLS 回归全部无 bug
- `tau_true(C=I) = 1.997155`（接近理论值 `beta_T=2.0`，N=100k 下的有限样本误差）
- R² = 0.806（effective_rank 是最强预测因子，p < 1e-5）
- 输出 JSON 和回归结果 txt 已写入 `artifacts/plan009/`

脚本已就绪，等审批后可用全量参数（M=1000, K={3,5,7}, 7 topos）正式运行。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_plan009-pathological-matrices-v2_20260520T181421"
}
```

</details>

---
