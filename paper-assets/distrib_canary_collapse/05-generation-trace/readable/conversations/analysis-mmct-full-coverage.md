# analysis mmct full coverage

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 89
- **Recorded user turns:** 0
- **Tool calls:** 44
- **Original source:** `logs/chats/worker_analysis_mmct_full_coverage_20260519T031507.jsonl`
- **Structured JSON:** [`06e46b272d41f97933b7.json`](../../sessions/06/06e46b272d41f97933b7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

89 recorded events

### Tool call

_source line 1 · 2026-05-19T03:20:49.545909+00:00_

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
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
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

_source line 2 · 2026-05-19T03:20:49.546189+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T03:20:49.546376+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "grep -rn \"mmct\\|MMCT\\|weighted_pair\\|weighted_global\\|uniform_forward\\|uniform_bidirectional\" /root/autodl-tmp/distrib_canary_collapse/*.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "grep -rn \"mmct\\|MMCT\\|weighted_pair\\|weighted_global\\|uniform_forward\\|uniform_bidirectional\" /root/autodl-tmp/distrib_canary_collapse/*.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T03:20:49.546523+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T03:20:49.546647+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-19T03:20:49.546767+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "find /root/autodl-tmp/distrib_canary_collapse/ -name \"*.py\" -path \"*mmct*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "find /root/autodl-tmp/distrib_canary_collapse/ -name \"*.py\" -path \"*mmct*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-19T03:20:49.546893+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"alpha_sweep\\nalpha_sweep_analysis\\nanalysis\\nbootstrap_ty_dryrun.json\\nbootstrap_ty_results.json\\ndetrending\\ndose_response_drift.csv\\ngen_wiki_gpt2m_a100_s43\\ngeneralize\\nintervention\\nmethod_ablation_phase2_panel.json\\nmethod_ablation_phase2_report.md\\nmethod_ablation_phase3_panel.json\\nmethod_ablation_phase3_report.md\\nperm_granger_power_bootstrap.json\\nrebuttal\\nscale_check\\nshapley_values.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.1}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T03:20:49.547021+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/mmct/__init__.py\\n/root/autodl-tmp/distrib_canary_collapse/mmct/methods.py\\n/root/autodl-tmp/distrib_canary_collapse/mmct/null_distribution.py\\n/root/autodl-tmp/distrib_canary_collapse/mmct/consensus_test.py\\n/root/autodl-tmp/distrib_canary_collapse/mmct/run_mmct.py\\n/root/autodl-tmp/distrib_canary_collapse/mmct/unified_analysis.py\\n/root/autodl-tmp/distrib_canary_collapse/run_mmct_s43.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T03:20:49.547152+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/mmct/run_mmct.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/mmct/run_mmct.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T03:20:49.547485+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Run MMCT across all available conditions.\\n\\nUses unified 5-method analysis data (from unified_analysis.py) with\\nTable 7 consistent parameters (2-sigma threshold, n_perm=5000).\\nRuns MMCT in 6 modes and generates all output files.\\n\\\"\\\"\\\"\\n\\nimport json\\nimport os\\nimport sys\\nfrom datetime import datetime\\n\\nsys.path.insert(0, \\\"/root/autodl-tmp/distrib_canary_collapse\\\")\\n\\nfrom mmct.methods import METRIC_PAIRS, METHOD_NAMES, set_unified_data_dir\\nfrom mmct.null_distribution import NullDistribution\\nfrom mmct.consensus_test import MMCT\\n\\nBASE_DIR = \\\"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep\\\"\\nGENERALIZE_DIR = \\\"/root/autodl-tmp/distrib_canary_collapse/results/generalize\\\"\\nOUTPUT_DIR = \\\"/root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results\\\"\\nUNIFIED_DATA_DIR = os.path.join(OUTPUT_DIR, \\\"unified_data\\\")\\n\\nNULL_DIRS = [\\n    os.path.join(BASE_DIR, \\\"a000_s42\\\"),\\n    os.path.join(BASE_DIR, \\\"a000_s43\\\"),\\n    os.path.join(BASE_DIR, \\\"a000_s44\\\"),\\n]\\n\\nMODES = [\\n    {\\\"weighted\\\": False, \\\"bidirectional\\\": False, \\\"weighted_mode\\\": \\\"pair\\\",\\n     \\\"name\\\": \\\"uniform_forward\\\"},\\n    {\\\"weighted\\\": False, \\\"bidirectional\\\": True, \\\"weighted_mode\\\": \\\"pair\\\",\\n     \\\"name\\\": \\\"uniform_bidirectional\\\"},\\n    {\\\"weighted\\\": True, \\\"bidirectional\\\": False, \\\"weighted_mode\\\": \\\"pair\\\",\\n     \\\"name\\\": \\\"weighted_pair_forward\\\"},\\n    {\\\"weighted\\\": True, \\\"bidirectional\\\": True, \\\"weighted_mode\\\": \\\"pair\\\",\\n     \\\"name\\\": \\\"weighted_pair_bidirectional\\\"},\\n    {\\\"weighted\\\": True, \\\"bidirectional\\\": False, \\\"weighted_mode\\\": \\\"global\\\",\\n     \\\"name\\\": \\\"weighted_global_forward\\\"},\\n    {\\\"weighted\\\": True, \\\"bidirectional\\\": True, \\\"weighted_mode\\\": \\\"global
…[truncated 7861 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T03:20:49.547650+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/run_mmct_s43.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/run_mmct_s43.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T03:20:49.547851+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"MMCT analysis for GPT-2m s43 bf16 using null from alpha=0.00.\\\"\\\"\\\"\\nimport sys\\nsys.path.insert(0, \\\"/root/autodl-tmp/distrib_canary_collapse\\\")\\n\\nfrom mmct.methods import METRIC_PAIRS, METHOD_NAMES\\nfrom mmct.null_distribution import NullDistribution\\nfrom mmct.consensus_test import MMCT\\n\\nNULL_DIRS = [\\n    \\\"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42\\\",\\n    \\\"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s43\\\",\\n    \\\"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s44\\\",\\n]\\n\\n# s43 bf16 forward significance (from 5method analysis)\\nS43_FWD = {\\n    (\\\"token_entropy\\\", \\\"distinct_1\\\"): {\\\"naive_xcorr\\\": True, \\\"diff_xcorr\\\": True, \\\"threshold_onset\\\": True, \\\"perm_granger\\\": False, \\\"ty_granger\\\": False},\\n    (\\\"token_entropy\\\", \\\"distinct_2\\\"): {\\\"naive_xcorr\\\": True, \\\"diff_xcorr\\\": True, \\\"threshold_onset\\\": True, \\\"perm_granger\\\": False, \\\"ty_granger\\\": False},\\n    (\\\"token_entropy\\\", \\\"distinct_3\\\"): {\\\"naive_xcorr\\\": True, \\\"diff_xcorr\\\": True, \\\"threshold_onset\\\": True, \\\"perm_granger\\\": False, \\\"ty_granger\\\": False},\\n    (\\\"token_entropy\\\", \\\"perplexity\\\"):  {\\\"naive_xcorr\\\": True, \\\"diff_xcorr\\\": True, \\\"threshold_onset\\\": True, \\\"perm_granger\\\": False, \\\"ty_granger\\\": False},\\n    (\\\"ece\\\", \\\"distinct_1\\\"):            {\\\"naive_xcorr\\\": True, \\\"diff_xcorr\\\": True, \\\"threshold_onset\\\": True, \\\"perm_granger\\\": False, \\\"ty_granger\\\": False},\\n    (\\\"ece\\\", \\\"distinct_2\\\"):            {\\\"naive_xcorr\\\": True, \\\"diff_xcorr\\\": True, \\\"threshold_onset\\\": True, \\\"perm_granger\\\": False, \\\"ty_granger\\\": False},\\n    (\\\"ece\\\", \\\"distinct_3\\\"):            {\\\"naive_xcorr\\\": True, \\\"diff_xcorr\\\": False, \\\
…[truncated 3219 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T03:20:49.548022+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/mmct/consensus_test.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/mmct/consensus_test.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T03:20:49.548204+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Multi-Method Consensus Test (MMCT) core implementation.\\n\\nModes:\\n  - uniform: consensus = count of significant methods\\n  - weighted_pair: consensus = inverse per-pair-FPR weighted sum\\n  - weighted_global: consensus = inverse global-FPR weighted sum\\n  - forward-only: test canary -> downstream direction only\\n  - bidirectional: require forward significant AND reverse non-significant\\n\\\"\\\"\\\"\\n\\nfrom dataclasses import dataclass, field, asdict\\nfrom typing import Optional\\n\\nfrom .methods import METHOD_NAMES, extract_method_significance, load_5method_results\\nfrom .null_distribution import NullDistribution\\n\\n\\n@dataclass\\nclass MMCTResult:\\n    canary: str\\n    downstream: str\\n    consensus_score: float\\n    p_value: float\\n    ci_lower: float\\n    ci_upper: float\\n    method_results: dict\\n    significant: bool\\n    alpha: float = 0.05\\n    mode: str = \\\"uniform_forward\\\"\\n    weights: Optional[dict] = None\\n    reverse_p_value: Optional[float] = None\\n    reverse_consensus_score: Optional[float] = None\\n    reverse_method_results: Optional[dict] = None\\n\\n    def to_dict(self):\\n        d = asdict(self)\\n        if d[\\\"weights\\\"]:\\n            d[\\\"weights\\\"] = {k: round(v, 4) for k, v in d[\\\"weights\\\"].items()}\\n        return d\\n\\n\\nclass MMCT:\\n    \\\"\\\"\\\"Multi-Method Consensus Test.\\\"\\\"\\\"\\n\\n    def __init__(self, null_distribution, weighted=False,\\n                 bidirectional=False, alpha=0.05, weighted_mode=\\\"pair\\\"):\\n        self.null = null_distribution\\n        self.weighted = weighted\\n        self.bidirectional = bidirectional\\n        self.alpha = alpha\\n        self.weighted_mode = weighted_mode\\n\\n    @property\\n    def mode_name(self):\\n        if self.weighted:\\n            w = f\\\"weighted_{self.weighted_mode}\\\"\\n        else:\\n            w = \\\"uniform\\\"\\n        d = \\\"bi
…[truncated 2625 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T03:20:49.548375+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/mmct/unified_analysis.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/mmct/unified_analysis.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T03:20:49.548647+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Unified 5-method analysis with Table 7 consistent parameters.\\n\\nKey change from 5method_leadlag.json:\\n- Threshold onset: 2-sigma (Table 7) instead of 3-sigma\\n- All params: n_perm=5000, xcorr_lag=5, granger_lag=1, alpha=0.05\\n\\\"\\\"\\\"\\nimport json, os, sys, time\\nimport numpy as np\\nfrom scipy import stats\\nfrom statsmodels.tsa.stattools import adfuller\\n\\nsys.path.insert(0, \\\"/root/autodl-tmp/distrib_canary_collapse\\\")\\nfrom permutation_granger import permutation_granger_test\\n\\nN_PERM = 5000\\nALPHA = 0.05\\nXCORR_LAG = 5\\nGRANGER_LAG = 1\\nTHRESHOLD_SIGMA = 2.0\\n\\nCANARIES = [\\\"token_entropy\\\", \\\"ece\\\"]\\nDOWNSTREAMS = [\\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\", \\\"perplexity\\\"]\\nPAIRS = [(c, d) for c in CANARIES for d in DOWNSTREAMS]\\nHIGHER_IS_WORSE = {\\\"ece\\\", \\\"perplexity\\\"}\\nLOWER_IS_WORSE = {\\\"token_entropy\\\", \\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\"}\\n\\nBASE = \\\"/root/autodl-tmp/distrib_canary_collapse\\\"\\nOUTPUT_DIR = os.path.join(BASE, \\\"artifacts\\\", \\\"mmct_results\\\", \\\"unified_data\\\")\\n\\nCONDITIONS = {\\n    \\\"a000_s42\\\": os.path.join(BASE, \\\"results/alpha_sweep/a000_s42\\\"),\\n    \\\"a000_s43\\\": os.path.join(BASE, \\\"results/alpha_sweep/a000_s43\\\"),\\n    \\\"a000_s44\\\": os.path.join(BASE, \\\"results/alpha_sweep/a000_s44\\\"),\\n    \\\"a025_s43\\\": os.path.join(BASE, \\\"results/alpha_sweep/a025_s43\\\"),\\n    \\\"a025_s44\\\": os.path.join(BASE, \\\"results/alpha_sweep/a025_s44\\\"),\\n    \\\"a050_s42\\\": os.path.join(BASE, \\\"results/alpha_sweep/a050_s42\\\"),\\n    \\\"a050_s43\\\": os.path.join(BASE, \\\"results/alpha_sweep/a050_s43\\\"),\\n    \\\"a050_s44\\\": os.path.join(BASE, \\\"results/alpha_sweep/a050_s44\\\"),\\n    \\\"a075_s42\\\": os.path.join(BASE, \\\"results/alpha_sweep/a075_s42\\\"),\\n    \\\"a075_s43\\\": os.path.join(BASE, \\\"results/
…[truncated 7402 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T03:20:49.548825+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results/unified_data/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results/unified_data/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T03:20:49.548960+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"a000_s42.json\\na000_s43.json\\na000_s44.json\\na025_s43.json\\na025_s44.json\\na050_s42.json\\na050_s43.json\\na050_s44.json\\na060_s42_bf16.json\\na075_s42.json\\na075_s43.json\\na075_s44.json\\ngpt2m_wiki_a100_s42.json\\nopt1b_wiki_a100_s42.json\\npythia14b_wiki_a100_s42.json\\npythia14b_wiki_a100_s43.json\\npythia1b_c4_a100_s42.json\\npythia1b_c4_a100_s43.json\\npythia410m_wiki_a100_s42.json\\nsummary.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T03:20:49.549087+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T03:20:49.549213+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"a000_s42\\na000_s43\\na000_s44\\na010_s42\\na025_3seed_unified_summary.txt\\na025_s43\\na025_s44\\na050_s42\\na050_s43\\na050_s44\\na060_s42_bf16\\na075_s42\\na075_s43\\na075_s44\\nalpha_monotonicity.png\\nanalysis\\nanalysis_s44\\nanalysis_summary.json\\npooled_panel_results.json\\npooled_panel_summary.txt\\nty_3seed_a025_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T03:20:49.549355+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/generalize/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/generalize/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-19T03:20:49.549478+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"analysis\\ngpt2m_wiki_a100_s42\\nopt1b_wiki_a100_s42\\npythia14b_wiki_a100_s42\\npythia14b_wiki_a100_s43\\npythia1b_c4_a100_s42\\npythia1b_c4_a100_s43\\npythia410m_wiki_a100_s42\\nsmollm3_3b_wiki_a100_s42\\nsmollm3_3b_wiki_a100_s42_fp32_v3\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-19T03:20:49.549593+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/gen_wiki_gpt2m_a100_s42_v4/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/gen_wiki_gpt2m_a100_s42_v4/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T03:20:49.549711+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/autodl-tmp/distrib_canary_collapse/results/gen_wiki_gpt2m_a100_s42_v4/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-19T03:20:49.549824+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "find /root/autodl-tmp/distrib_canary_collapse/results/ -name \"all_metrics.json\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "find /root/autodl-tmp/distrib_canary_collapse/results/ -name \"all_metrics.json\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-19T03:20:49.549962+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/all_metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42/all_metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a075_s42/all_metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s43/all_metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s43/all_metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s44/all_metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a075_s43/all_metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a075_s44/all_metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s43/all_metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s44/all_metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s44/all_metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a010_s42/all_metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a060_s42_bf16/all_metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia410m_wiki_a100_s42/all_metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/generalize/opt1b_wiki_a100_s42/all_metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia1b_c4_a100_s42/all_metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia14b_wiki_a100_s42/all_metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia1b_c4_a100_s43/all_metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/generalize/gpt2m_wiki_a100_s42/all_metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia14b_wiki_a100_s43/all_metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/intervention/reactive_d1_
…[truncated 324 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-19T03:20:49.550131+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-19T03:20:49.550272+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"data_consistency_check.md\\nfpr_fnr_comparison.md\\nfpr_fnr_comparison_v2.md\\nmmct_report.md\\nmmct_report_v2.md\\nmmct_results.json\\nmmct_results_v2.json\\nmmct_table7.md\\nnull_distribution.json\\nnull_distribution_v2.json\\nunified_data\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-19T03:20:49.550400+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "find /root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results/ -name \"*.json\" -not -path \"*/unified_data/*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "find /root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results/ -name \"*.json\" -not -path \"*/unified_data/*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-19T03:20:49.550519+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/mmct/methods.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/mmct/methods.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-19T03:20:49.550643+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results/mmct_results.json\\n/root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results/null_distribution.json\\n/root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results/mmct_results_v2.json\\n/root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results/null_distribution_v2.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-19T03:20:49.550801+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Unified wrapper for 5 lead-lag detection methods.\\n\\nReads pre-computed results from JSON files. Supports:\\n  - Original 5method_leadlag.json (two formats A and B)\\n  - Unified unified_5method.json (from unified_analysis.py)\\n\\nSet _UNIFIED_DATA_DIR to redirect loading to unified data.\\n\\\"\\\"\\\"\\n\\nimport json\\nfrom pathlib import Path\\n\\nMETHOD_NAMES = [\\\"naive_xcorr\\\", \\\"diff_xcorr\\\", \\\"threshold_onset\\\",\\n                \\\"perm_granger\\\", \\\"ty_granger\\\"]\\n\\nCANARY_METRICS = [\\\"token_entropy\\\", \\\"ece\\\"]\\nDOWNSTREAM_METRICS = [\\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\", \\\"perplexity\\\"]\\n\\nMETRIC_PAIRS = [(c, d) for c in CANARY_METRICS for d in DOWNSTREAM_METRICS]\\n\\n_UNIFIED_DATA_DIR = None\\n\\n\\ndef set_unified_data_dir(path):\\n    global _UNIFIED_DATA_DIR\\n    _UNIFIED_DATA_DIR = path\\n\\n\\ndef load_5method_results(data_dir):\\n    \\\"\\\"\\\"Load pre-computed 5-method lead-lag results for one condition.\\n    \\n    If _UNIFIED_DATA_DIR is set, loads from unified data instead.\\n    \\\"\\\"\\\"\\n    if _UNIFIED_DATA_DIR:\\n        name = Path(data_dir).name\\n        unified_path = Path(_UNIFIED_DATA_DIR) / f\\\"{name}.json\\\"\\n        if unified_path.exists():\\n            with open(unified_path) as f:\\n                return json.load(f)\\n    path = Path(data_dir) / \\\"analysis\\\" / \\\"5method_leadlag.json\\\"\\n    with open(path) as f:\\n        return json.load(f)\\n\\n\\ndef _find_pair(results, canary, downstream):\\n    \\\"\\\"\\\"Find the pair dict, handling both JSON formats.\\\"\\\"\\\"\\n    for pair in results[\\\"pairs\\\"]:\\n        if pair.get(\\\"canary\\\") == canary and pair.get(\\\"downstream\\\") == downstream:\\n            return pair\\n        fwd = pair.get(\\\"forward\\\", {})\\n        if fwd.get(\\\"canary\\\") == canary and fwd.get(\\\"downstream\\\") == downstream:\\n          
…[truncated 1178 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-19T03:20:49.550965+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "head -100 /root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results/mmct_results_v2.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "head -100 /root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results/mmct_results_v2.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-19T03:20:49.551144+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"meta\\\": {\\n    \\\"timestamp\\\": \\\"2026-05-19T00:43:44.035297\\\",\\n    \\\"null_dirs\\\": [\\n      \\\"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42\\\",\\n      \\\"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s43\\\",\\n      \\\"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s44\\\"\\n    ],\\n    \\\"n_null\\\": 24,\\n    \\\"methods\\\": [\\n      \\\"naive_xcorr\\\",\\n      \\\"diff_xcorr\\\",\\n      \\\"threshold_onset\\\",\\n      \\\"perm_granger\\\",\\n      \\\"ty_granger\\\"\\n    ],\\n    \\\"modes\\\": [\\n      \\\"uniform_forward\\\",\\n      \\\"uniform_bidirectional\\\",\\n      \\\"weighted_pair_forward\\\",\\n      \\\"weighted_pair_bidirectional\\\",\\n      \\\"weighted_global_forward\\\",\\n      \\\"weighted_global_bidirectional\\\"\\n    ],\\n    \\\"data_source\\\": \\\"unified_5method (2-sigma threshold, Table 7 params)\\\",\\n    \\\"unified_data_dir\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results/unified_data\\\",\\n    \\\"alpha_conditions\\\": {\\n      \\\"0.0\\\": [\\n        \\\"a000_s42\\\",\\n        \\\"a000_s43\\\",\\n        \\\"a000_s44\\\"\\n      ],\\n      \\\"0.25\\\": [\\n        \\\"a025_s43\\\",\\n        \\\"a025_s44\\\"\\n      ],\\n      \\\"0.5\\\": [\\n        \\\"a050_s42\\\",\\n        \\\"a050_s43\\\",\\n        \\\"a050_s44\\\"\\n      ],\\n      \\\"0.75\\\": [\\n        \\\"a075_s42\\\",\\n        \\\"a075_s43\\\",\\n        \\\"a075_s44\\\"\\n      ]\\n    },\\n    \\\"table7_conditions\\\": [\\n      \\\"Baseline\\\",\\n      \\\"Arch: GPT-2m\\\",\\n      \\\"Arch: OPT\\\",\\n      \\\"Scale: 1.4B s42\\\",\\n      \\\"Scale: 1.4B s43\\\",\\n      \\\"Domain: C4 s42\\\",\\n      \\\"Domain: C4 s43\\\"\\n    ]\\n  },\\n  \\\"results\\\": {\\n    \\\"uniform_forward\\\": {\\n      \\\"a000\\\": [\\n        {\\n          \\\"canary\\\": \\\"token_e
…[truncated 1576 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-19T03:20:49.551308+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results/mmct_report_v2.md",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results/mmct_report_v2.md",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-19T03:20:49.551503+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"# MMCT Results Report (v2 — Unified Data)\\n\\nGenerated: 2026-05-19T00:43:44.035297\\nData source: unified_5method (2-sigma threshold, Table 7 params)\\n\\nNull dirs: 3\\nMethods: naive_xcorr, diff_xcorr, threshold_onset, perm_granger, ty_granger\\nModes: uniform_forward, uniform_bidirectional, weighted_pair_forward, weighted_pair_bidirectional, weighted_global_forward, weighted_global_bidirectional\\n\\n## Alpha Sweep Results\\n\\n### uniform_forward\\n\\n#### Alpha = a000\\n\\n| Canary | Downstream | Seed | Score | p-value | CI | Sig |\\n|--------|------------|------|-------|---------|----|-----|\\n| token_entropy | distinct_1 | 42 | 3.0000 | 0.4400 | [0.2400, 0.6400] | no |\\n| token_entropy | distinct_2 | 42 | 3.0000 | 0.4400 | [0.2400, 0.6400] | no |\\n| token_entropy | distinct_3 | 42 | 3.0000 | 0.4400 | [0.2400, 0.6400] | no |\\n| token_entropy | perplexity | 42 | 2.0000 | 0.6400 | [0.4400, 0.8400] | no |\\n| ece | distinct_1 | 42 | 2.0000 | 0.6400 | [0.4400, 0.8400] | no |\\n| ece | distinct_2 | 42 | 1.0000 | 0.9600 | [0.8800, 1.0000] | no |\\n| ece | distinct_3 | 42 | 3.0000 | 0.4400 | [0.2400, 0.6400] | no |\\n| ece | perplexity | 42 | 1.0000 | 0.9600 | [0.8800, 1.0000] | no |\\n| token_entropy | distinct_1 | 43 | 3.0000 | 0.4400 | [0.2400, 0.6400] | no |\\n| token_entropy | distinct_2 | 43 | 3.0000 | 0.4400 | [0.2400, 0.6400] | no |\\n| token_entropy | distinct_3 | 43 | 4.0000 | 0.1600 | [0.0400, 0.2800] | no |\\n| token_entropy | perplexity | 43 | 2.0000 | 0.6400 | [0.4400, 0.8400] | no |\\n| ece | distinct_1 | 43 | 1.0000 | 0.9600 | [0.8800, 1.0000] | no |\\n| ece | distinct_2 | 43 | 1.0000 | 0.9600 | [0.8800, 1.0000] | no |\\n| ece | distinct_3 | 43 | 1.0000 | 0.9600 | [0.8800, 1.0000] | no |\\n| ece | perplexity | 43 | 0.0000 | 1.0000 | [1.0000, 1.0000] | no |\\n| token_entropy | distinct_1 | 44 | 3.0000 | 0.4400 | [0.2400, 0.6400] | no |\\n| token_entropy | distinct_2 | 44 | 4.0000 | 0.1600 | [
…[truncated 6454 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-19T03:20:49.551680+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results/mmct_table7.md",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results/mmct_table7.md",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-19T03:20:49.551846+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"# MMCT Table 7: Generalization Results (alpha=1.0, Unified Data)\\n\\nEach cell = significant pairs / 8 total pairs (MMCT p<0.05)\\n\\n| Condition | Model | Data | unif_fwd | unif_bidir | w_pair_fwd | w_pair_bidir | w_global_fwd | w_global_bidir |\\n|-----------|-------|------|------|------|------|------|------|------|\\n| Baseline | Pythia-410M | Wiki | 1/8 | 1/8 | 6/8 | 5/8 | 2/8 | 2/8 |\\n| Arch: GPT-2m | GPT-2m | Wiki | 2/8 | 2/8 | 8/8 | 7/8 | 2/8 | 2/8 |\\n| Arch: OPT | OPT-1.3B | Wiki | 0/8 | 0/8 | 6/8 | 5/8 | 0/8 | 0/8 |\\n| Scale: 1.4B s42 | Pythia-1.4B | Wiki | 0/8 | 0/8 | 6/8 | 6/8 | 0/8 | 0/8 |\\n| Scale: 1.4B s43 | Pythia-1.4B | Wiki | 2/8 | 2/8 | 6/8 | 5/8 | 2/8 | 1/8 |\\n| Domain: C4 s42 | Pythia-1B | C4 | 1/8 | 1/8 | 7/8 | 6/8 | 1/8 | 1/8 |\\n| Domain: C4 s43 | Pythia-1B | C4 | 2/8 | 2/8 | 6/8 | 6/8 | 2/8 | 1/8 |\\n\\n## Per-Pair Detail (weighted_global_forward)\\n\\n### Baseline\\n\\n| Canary | Downstream | Score | p-value | Sig |\\n|--------|------------|-------|---------|-----|\\n| token_entropy | distinct_1 | 0.5243 | 0.2400 | no |\\n| token_entropy | distinct_2 | 0.5243 | 0.2400 | no |\\n| token_entropy | distinct_3 | 0.5243 | 0.2400 | no |\\n| token_entropy | perplexity | 0.2071 | 0.4400 | no |\\n| ece | distinct_1 | 0.5243 | 0.2400 | no |\\n| ece | distinct_2 | 1.0000 | 0.0400 | YES |\\n| ece | distinct_3 | 0.5243 | 0.2400 | no |\\n| ece | perplexity | 0.6829 | 0.0400 | YES |\\n\\n### Arch: GPT-2m\\n\\n| Canary | Downstream | Score | p-value | Sig |\\n|--------|------------|-------|---------|-----|\\n| token_entropy | distinct_1 | 0.5243 | 0.2400 | no |\\n| token_entropy | distinct_2 | 1.0000 | 0.0400 | YES |\\n| token_entropy | distinct_3 | 1.0000 | 0.0400 | YES |\\n| token_entropy | perplexity | 0.2071 | 0.4400 | no |\\n| ece | distinct_1 | 0.5243 | 0.2400 | no |\\n| ece | distinct_2 | 0.5243 | 0.2400 | no |\\n| ece | distinct_3 | 0.5243 | 0.2400 | no |\\n| ece | perplexity | 0.2071 | 0.
…[truncated 2798 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-19T03:20:49.552001+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "grep -n \"a060\\|a010\\|bf16\\|gen_wiki_gpt2m\" /root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results/mmct_results_v2.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "grep -n \"a060\\|a010\\|bf16\\|gen_wiki_gpt2m\" /root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results/mmct_results_v2.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-19T03:20:49.552130+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-19T03:20:49.552248+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a010_s42/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a010_s42/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-19T03:20:49.552390+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"EXIT_CODE\\nall_metrics.json\\nconfig.json\\ngen_0\\ngen_1\\ngen_10\\ngen_2\\ngen_3\\ngen_4\\ngen_5\\ngen_6\\ngen_7\\ngen_8\\ngen_9\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-19T03:20:49.552506+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "find /root/autodl-tmp/distrib_canary_collapse/results/ -maxdepth 2 -name \"gen_wiki_gpt2m*\" -type d",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "find /root/autodl-tmp/distrib_canary_collapse/results/ -maxdepth 2 -name \"gen_wiki_gpt2m*\" -type d",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-19T03:20:49.552624+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/results/gen_wiki_gpt2m_a100_s43\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-19T03:20:49.552772+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "grep \"a060\" /root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results/mmct_results_v2.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "grep \"a060\" /root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results/mmct_results_v2.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-19T03:20:49.552893+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-19T03:20:49.553007+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "grep \"a010\" /root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results/mmct_results_v2.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "grep \"a010\" /root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results/mmct_results_v2.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-19T03:20:49.553124+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-19T03:20:49.553240+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "grep \"gen_wiki_gpt2m\" /root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results/mmct_results_v2.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "grep \"gen_wiki_gpt2m\" /root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results/mmct_results_v2.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-19T03:20:49.553378+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-19T03:20:49.553491+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/mmct/null_distribution.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/mmct/null_distribution.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-19T03:20:49.553683+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Null distribution construction from alpha=0.00 data.\\n\\nUses alpha=0.00 runs (no synthetic contamination) to build the empirical\\ndistribution of consensus scores under H0. Supports uniform, per-pair weighted,\\nand global weighted consensus modes.\\n\\\"\\\"\\\"\\n\\nimport numpy as np\\nfrom pathlib import Path\\n\\nfrom .methods import (METHOD_NAMES, METRIC_PAIRS, load_5method_results,\\n                      extract_method_significance)\\n\\n\\nclass NullDistribution:\\n    \\\"\\\"\\\"Empirical null distribution for MMCT consensus scores.\\\"\\\"\\\"\\n\\n    def __init__(self, null_dirs, n_bootstrap=10000, seed=42):\\n        self.null_dirs = null_dirs\\n        self.n_bootstrap = n_bootstrap\\n        self.seed = seed\\n\\n        self._per_pair_sigs = {}\\n        self._load_null_data()\\n        self._compute_fpr_profile()\\n        self._build_distributions()\\n        self._precompute_bootstrap()\\n\\n    def _load_null_data(self):\\n        for d in self.null_dirs:\\n            results = load_5method_results(d)\\n            for canary, downstream in METRIC_PAIRS:\\n                key = (canary, downstream)\\n                if key not in self._per_pair_sigs:\\n                    self._per_pair_sigs[key] = {\\\"forward\\\": [], \\\"reverse\\\": []}\\n\\n                fwd = extract_method_significance(\\n                    results, canary, downstream, \\\"forward\\\")\\n                rev = extract_method_significance(\\n                    results, canary, downstream, \\\"reverse\\\")\\n                self._per_pair_sigs[key][\\\"forward\\\"].append(fwd)\\n                self._per_pair_sigs[key][\\\"reverse\\\"].append(rev)\\n\\n    def _compute_fpr_profile(self):\\n        self.fpr_profile = {}\\n        self.global_fpr = {}\\n\\n        method_sig_counts = {m: 0 for m in METHOD_NAMES}\\n        total_obs = 0\\n\\n        for key in METRIC_PAIRS:\\n            key = tuple(ke
…[truncated 6698 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-19T03:20:49.553886+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/gen_wiki_gpt2m_a100_s43/all_metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/gen_wiki_gpt2m_a100_s43/all_metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-19T03:20:49.554022+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"cat: /root/autodl-tmp/distrib_canary_collapse/results/gen_wiki_gpt2m_a100_s43/all_metrics.json: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-19T03:20:49.554142+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "head -5 /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a010_s42/all_metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "head -5 /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a010_s42/all_metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-19T03:20:49.554278+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[\\n  {\\n    \\\"token_entropy\\\": 3.2341948700181407,\\n    \\\"self_bleu\\\": 0.010194395218435404,\\n    \\\"distinct_1\\\": 0.0982156685333268,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-19T03:20:49.554399+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "wc -l /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a010_s42/all_metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "wc -l /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a010_s42/all_metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-19T03:20:49.554516+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"166 /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a010_s42/all_metrics.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.48}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-19T03:20:49.554654+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/gen_wiki_gpt2m_a100_s43/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/gen_wiki_gpt2m_a100_s43/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-19T03:20:49.554771+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"config.json\\ngen_0\\ngen_1\\ngen_2\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-19T03:20:49.554880+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "wc -l /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a060_s42_bf16/all_metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "wc -l /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a060_s42_bf16/all_metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-19T03:20:49.554996+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"13 /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a060_s42_bf16/all_metrics.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-19T03:20:49.555144+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "cat > /root/autodl-tmp/distrib_canary_collapse/run_mmct_all.py << 'PYEOF'\n\"\"\"Run MMCT on ALL available conditions, including a010 and a060.\n\nSteps:\n1. Generate unified 5-method data for a010_s42 (missing)\n2. Re-run full MMCT with all discovered conditions\n3. Output comprehensive JSON results\n\"\"\"\nimport json, os, sys, time\n\nsys.path.insert(0, \"/root/autodl-tmp/distrib_canary_collapse\")\n\n# Step 1: Generate unified data for a010_s42\nfrom mmct.unified_analysis import analyze_condition, OUTPUT_DIR\n\nos.makedirs(OUTPUT_DIR, exist_ok=True)\n\nmissing = {\n    \"a010_s42\": \"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a010_s42\",\n}\n\nfor name, data_dir in missing.items():\n    out_path = os.path.join(OUTPUT_DIR, f\"{name}.json\")\n    if os.path.exists(out_path):\n        print(f\"SKIP unified analysis for {name} (already exists)\")\n        continue\n    metrics_path = os.path.join(data_dir, \"all_metrics.json\")\n    if not os.path.exists(metrics_path):\n        print(f\"SKIP {name}: no all_metrics.json\")\n        continue\n    seed = 42 if \"_s42\" in name else (43 if \"_s43\" in name else 44)\n    print(f\"Running unified analysis for {name} (seed={seed})...\", end=\" \", flush=True)\n    t0 = time.time()\n    result = analyze_condition(name, data_dir, seed)\n    with open(out_path, 'w') as f:\n        json.dump(result, f, indent=2)\n    print(f\"done ({time.time()-t0:.1f}s)\")\n\n# Step 2: Re-run full MMCT\nprint(\"\\n=== Running full MMCT ===\\n\")\n\nfrom mmct.methods import set_unified_data_dir\nfrom mmct.run_mmct import run_all\n\nrun_all()\n\nprint(\"\\nDone.\")\nPYEOF\necho \"Script written.\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat > /root/autodl-tmp/distrib_canary_collapse/run_mmct_all.py << 'PYEOF'\n\"\"\"Run MMCT on ALL available conditions, including a010 and a060.\n\nSteps:\n1. Generate unified 5-method data for a010_s42 (missing)\n2. Re-run full MMCT with all discovered conditions\n3. Output comprehensive JSON results\n\"\"\"\nimport json, os, sys, time\n\nsys.path.insert(0, \"/root/autodl-tmp/distrib_canary_collapse\")\n\n# Step 1: Generate unified data for a010_s42\nfrom mmct.unified_analysis import analyze_condition, OUTPUT_DIR\n\nos.makedirs(OUTPUT_DIR, exist_ok=True)\n\nmissing = {\n    \"a010_s42\": \"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a010_s42\",\n}\n\nfor name, data_dir in missing.items():\n    out_path = os.path.join(OUTPUT_DIR, f\"{name}.json\")\n    if os.path.exists(out_path):\n        print(f\"SKIP unified analysis for {name} (already exists)\")\n        continue\n    metrics_path = os.path.join(data_dir, \"all_metrics.json\")\n    if not os.path.exists(metrics_path):\n        print(f\"SKIP {name}: no all_metrics.json\")\n        continue\n    seed = 42 if \"_s42\" in name else (43 if \"_s43\" in name else 44)\n    print(f\"Running unified analysis for {name} (seed={seed})...\", end=\" \", flush=True)\n    t0 = time.time()\n    result = analyze_condition(name, data_dir, seed)\n    with open(out_path, 'w') as f:\n        json.dump(result, f, indent=2)\n    print(f\"done ({time.time()-t0:.1f}s)\")\n\n# Step 2: Re-run full MMCT\nprint(\"\\n=== Running full MMCT ===\\n\")\n\nfrom mmct.methods import set_unified_data_dir\nfrom mmct.run_mmct import run_all\n\nrun_all()\n\nprint(\"\\nDone.\")\nPYEOF\necho \"Script written.\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-19T03:20:49.555293+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script written.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-19T03:20:49.555412+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "cd /root/autodl-tmp/distrib_canary_collapse && python run_mmct_all.py 2>&1",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "cd /root/autodl-tmp/distrib_canary_collapse && python run_mmct_all.py 2>&1",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-19T03:20:49.555530+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"bash: line 1: python: command not found\\n\", \"stderr\": \"\", \"return_code\": 127}, \"error\": \"exit code 127\", \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-19T03:20:49.555641+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "which python3",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "which python3",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-19T03:20:49.555753+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/usr/bin/python3\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-19T03:20:49.555868+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "cd /root/autodl-tmp/distrib_canary_collapse && python3 run_mmct_all.py 2>&1",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "cd /root/autodl-tmp/distrib_canary_collapse && python3 run_mmct_all.py 2>&1",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-19T03:20:49.556003+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"Traceback (most recent call last):\\n  File \\\"/root/autodl-tmp/distrib_canary_collapse/run_mmct_all.py\\\", line 13, in &lt;module>\\n    from mmct.unified_analysis import analyze_condition, OUTPUT_DIR\\n  File \\\"/root/autodl-tmp/distrib_canary_collapse/mmct/__init__.py\\\", line 8, in &lt;module>\\n    from .consensus_test import MMCT, MMCTResult\\n  File \\\"/root/autodl-tmp/distrib_canary_collapse/mmct/consensus_test.py\\\", line 15, in &lt;module>\\n    from .null_distribution import NullDistribution\\n  File \\\"/root/autodl-tmp/distrib_canary_collapse/mmct/null_distribution.py\\\", line 8, in &lt;module>\\n    import numpy as np\\nModuleNotFoundError: No module named 'numpy'\\n\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-19T03:20:49.556122+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/miniconda3/bin/python 2>/dev/null; ls /root/anaconda3/bin/python 2>/dev/null; find /root -maxdepth 3 -name \"python*\" -type f 2>/dev/null | head -10",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/miniconda3/bin/python 2>/dev/null; ls /root/anaconda3/bin/python 2>/dev/null; find /root -maxdepth 3 -name \"python*\" -type f 2>/dev/null | head -10",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-19T03:20:49.556238+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/miniconda3/bin/python\\n/root/miniconda3/bin/python3.12\\n/root/miniconda3/bin/python3.12-config\\n/root/miniconda3/conda-meta/python-3.12.3-h996f2a0_1.json\\n/root/miniconda3/pkgs/python-3.12.3-h996f2a0_1.conda\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-19T03:20:49.556371+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "cd /root/autodl-tmp/distrib_canary_collapse && /root/miniconda3/bin/python run_mmct_all.py 2>&1",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "cd /root/autodl-tmp/distrib_canary_collapse && /root/miniconda3/bin/python run_mmct_all.py 2>&1",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-19T03:20:49.556521+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Running unified analysis for a010_s42 (seed=42)... done (2.5s)\\n\\n=== Running full MMCT ===\\n\\nAlpha sweep: {0.0: 3, 0.1: 1, 0.25: 2, 0.5: 3, 0.6: 1, 0.75: 3}\\nTable 7: 7 conditions available\\nBuilding null distribution from alpha=0.00 unified data...\\n  24 null observations (3 seeds x 8 pairs)\\n  Global FPR: {'naive_xcorr': 0.9583333333333334, 'diff_xcorr': 0.5, 'threshold_onset': 0.4583333333333333, 'perm_granger': 0.125, 'ty_granger': 0.08333333333333333}\\n  Global weights: {'naive_xcorr': 1.04, 'diff_xcorr': 2.0, 'threshold_onset': 2.18, 'perm_granger': 8.0, 'ty_granger': 12.0}\\n\\n--- Mode: uniform_forward ---\\n  alpha=0.00: 0/24 significant\\n  alpha=0.10: 0/8 significant\\n  alpha=0.25: 0/16 significant\\n  alpha=0.50: 0/24 significant\\n  alpha=0.60: 0/8 significant\\n  alpha=0.75: 2/24 significant\\n\\n--- Mode: uniform_bidirectional ---\\n  alpha=0.00: 0/24 significant\\n  alpha=0.10: 0/8 significant\\n  alpha=0.25: 0/16 significant\\n  alpha=0.50: 0/24 significant\\n  alpha=0.60: 0/8 significant\\n  alpha=0.75: 2/24 significant\\n\\n--- Mode: weighted_pair_forward ---\\n  alpha=0.00: 0/24 significant\\n  alpha=0.10: 1/8 significant\\n  alpha=0.25: 7/16 significant\\n  alpha=0.50: 14/24 significant\\n  alpha=0.60: 6/8 significant\\n  alpha=0.75: 19/24 significant\\n\\n--- Mode: weighted_pair_bidirectional ---\\n  alpha=0.00: 0/24 significant\\n  alpha=0.10: 1/8 significant\\n  alpha=0.25: 7/16 significant\\n  alpha=0.50: 14/24 significant\\n  alpha=0.60: 6/8 significant\\n  alpha=0.75: 19/24 significant\\n\\n--- Mode: weighted_global_forward ---\\n  alpha=0.00: 0/24 significant\\n  alpha=0.10: 0/8 significant\\n  alpha=0.25: 0/16 significant\\n  alpha=0.50: 0/24 significant\\n  alpha=0.60: 0/8 significant\\n  alpha=0.75: 2/24 significant\\n\\n--- Mode: weighted_global_bidirectional ---\\n  alpha=0.00: 0/24 significant\\n  alpha=0.10: 0/8 significant\\n  alpha=0.25: 0/16 significant\\n  alph
…[truncated 2110 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-19T03:20:49.556692+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results/fpr_fnr_comparison_v2.md",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results/fpr_fnr_comparison_v2.md",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-19T03:20:49.556853+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"# FPR-FNR 6-Way Comparison (v2 — Unified Data)\\n\\nuniform vs weighted_pair vs weighted_global x forward vs bidirectional\\n\\n## Detection Rate by Alpha Condition\\n\\n| Mode | FPR (a=0.00) | a010 | a025 | a050 | a060 | a075 |\\n|------|-------------|------|------|------|------|------|\\n| uniform_forward | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0833 |\\n| uniform_bidirectional | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0833 |\\n| weighted_pair_forward | 0.0000 | 0.1250 | 0.4375 | 0.5833 | 0.7500 | 0.7917 |\\n| weighted_pair_bidirectional | 0.0000 | 0.1250 | 0.4375 | 0.5833 | 0.7500 | 0.7917 |\\n| weighted_global_forward | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0833 |\\n| weighted_global_bidirectional | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0417 |\\n\\n## Tradeoff Analysis\\n\\n- **FPR**: fraction of alpha=0.00 tests incorrectly flagged\\n- **Detection rate**: fraction flagged significant at each alpha\\n- Weighted_pair: per-pair inverse-FPR weights (can be unstable with few null seeds)\\n- Weighted_global: pooled-across-pairs inverse-FPR weights (more stable)\\n- Bidirectional: requires forward sig. AND reverse non-sig.\\n- Ideal: FPR=0 at alpha=0.00 with high detection at alpha>0\\n\\n## Effect of Each Enhancement\\n\\n| Comparison | FPR Change | a075 Det. Change |\\n|------------|-----------|--------------------| \\n| +weighted_pair (fwd) | 0.0000 -> 0.0000 | 0.0833 -> 0.7917 |\\n| +weighted_global (fwd) | 0.0000 -> 0.0000 | 0.0833 -> 0.0833 |\\n| +bidirectional (uniform) | 0.0000 -> 0.0000 | 0.0833 -> 0.0833 |\\n| +weighted_pair+bidir | 0.0000 -> 0.0000 | 0.0833 -> 0.7917 |\\n| +weighted_global+bidir | 0.0000 -> 0.0000 | 0.0833 -> 0.0417 |\\n| global vs pair (fwd) | 0.0000 -> 0.0000 | 0.7917 -> 0.0833 |\\n| global vs pair (bidir) | 0.0000 -> 0.0000 | 0.7917 -> 0.0417 |\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-19T03:20:49.557092+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results/mmct_table7.md",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results/mmct_table7.md",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-19T03:20:49.557364+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"# MMCT Table 7: Generalization Results (alpha=1.0, Unified Data)\\n\\nEach cell = significant pairs / 8 total pairs (MMCT p<0.05)\\n\\n| Condition | Model | Data | unif_fwd | unif_bidir | w_pair_fwd | w_pair_bidir | w_global_fwd | w_global_bidir |\\n|-----------|-------|------|------|------|------|------|------|------|\\n| Baseline | Pythia-410M | Wiki | 1/8 | 1/8 | 6/8 | 5/8 | 2/8 | 2/8 |\\n| Arch: GPT-2m | GPT-2m | Wiki | 2/8 | 2/8 | 8/8 | 7/8 | 2/8 | 2/8 |\\n| Arch: OPT | OPT-1.3B | Wiki | 0/8 | 0/8 | 6/8 | 5/8 | 0/8 | 0/8 |\\n| Scale: 1.4B s42 | Pythia-1.4B | Wiki | 0/8 | 0/8 | 6/8 | 6/8 | 0/8 | 0/8 |\\n| Scale: 1.4B s43 | Pythia-1.4B | Wiki | 2/8 | 2/8 | 6/8 | 5/8 | 2/8 | 1/8 |\\n| Domain: C4 s42 | Pythia-1B | C4 | 1/8 | 1/8 | 7/8 | 6/8 | 1/8 | 1/8 |\\n| Domain: C4 s43 | Pythia-1B | C4 | 2/8 | 2/8 | 6/8 | 6/8 | 2/8 | 1/8 |\\n\\n## Per-Pair Detail (weighted_global_forward)\\n\\n### Baseline\\n\\n| Canary | Downstream | Score | p-value | Sig |\\n|--------|------------|-------|---------|-----|\\n| token_entropy | distinct_1 | 0.5243 | 0.2400 | no |\\n| token_entropy | distinct_2 | 0.5243 | 0.2400 | no |\\n| token_entropy | distinct_3 | 0.5243 | 0.2400 | no |\\n| token_entropy | perplexity | 0.2071 | 0.4400 | no |\\n| ece | distinct_1 | 0.5243 | 0.2400 | no |\\n| ece | distinct_2 | 1.0000 | 0.0400 | YES |\\n| ece | distinct_3 | 0.5243 | 0.2400 | no |\\n| ece | perplexity | 0.6829 | 0.0400 | YES |\\n\\n### Arch: GPT-2m\\n\\n| Canary | Downstream | Score | p-value | Sig |\\n|--------|------------|-------|---------|-----|\\n| token_entropy | distinct_1 | 0.5243 | 0.2400 | no |\\n| token_entropy | distinct_2 | 1.0000 | 0.0400 | YES |\\n| token_entropy | distinct_3 | 1.0000 | 0.0400 | YES |\\n| token_entropy | perplexity | 0.2071 | 0.4400 | no |\\n| ece | distinct_1 | 0.5243 | 0.2400 | no |\\n| ece | distinct_2 | 0.5243 | 0.2400 | no |\\n| ece | distinct_3 | 0.5243 | 0.2400 | no |\\n| ece | perplexity | 0.2071 | 0.
…[truncated 2798 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-19T03:20:49.557645+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "cat > /tmp/extract_mmct.py << 'PYEOF'\nimport json\n\nwith open(\"/root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results/mmct_results_v2.json\") as f:\n    data = json.load(f)\n\n# For each mode, count significant per run_id\nmodes_to_check = [\"uniform_forward\", \"weighted_pair_forward\", \"weighted_global_forward\",\n                   \"uniform_bidirectional\", \"weighted_pair_bidirectional\", \"weighted_global_bidirectional\"]\n\n# Alpha sweep\nprint(\"=== ALPHA SWEEP PER-RUN ===\")\nfor mode in modes_to_check:\n    mode_data = data[\"results\"][mode]\n    print(f\"\\n--- {mode} ---\")\n    for alpha_key in sorted(mode_data.keys()):\n        entries = mode_data[alpha_key]\n        # Group by run_id\n        by_run = {}\n        for e in entries:\n            rid = e[\"run_id\"]\n            if rid not in by_run:\n                by_run[rid] = {\"sig\": 0, \"total\": 0}\n            by_run[rid][\"total\"] += 1\n            if e[\"significant\"]:\n                by_run[rid][\"sig\"] += 1\n        for rid in sorted(by_run.keys()):\n            print(f\"  {alpha_key}/{rid}: {by_run[rid]['sig']}/{by_run[rid]['total']}\")\n\n# Table 7\nprint(\"\\n=== TABLE 7 PER-CONDITION ===\")\nt7 = data.get(\"table7_results\", {})\nfor mode in modes_to_check:\n    if mode not in t7:\n        continue\n    print(f\"\\n--- {mode} ---\")\n    for cond, cdata in t7[mode].items():\n        print(f\"  {cond} ({cdata['model']}, {cdata['data']}): {cdata['n_significant']}/{cdata['n_total']}\")\nPYEOF\n/root/miniconda3/bin/python /tmp/extract_mmct.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat > /tmp/extract_mmct.py << 'PYEOF'\nimport json\n\nwith open(\"/root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results/mmct_results_v2.json\") as f:\n    data = json.load(f)\n\n# For each mode, count significant per run_id\nmodes_to_check = [\"uniform_forward\", \"weighted_pair_forward\", \"weighted_global_forward\",\n                   \"uniform_bidirectional\", \"weighted_pair_bidirectional\", \"weighted_global_bidirectional\"]\n\n# Alpha sweep\nprint(\"=== ALPHA SWEEP PER-RUN ===\")\nfor mode in modes_to_check:\n    mode_data = data[\"results\"][mode]\n    print(f\"\\n--- {mode} ---\")\n    for alpha_key in sorted(mode_data.keys()):\n        entries = mode_data[alpha_key]\n        # Group by run_id\n        by_run = {}\n        for e in entries:\n            rid = e[\"run_id\"]\n            if rid not in by_run:\n                by_run[rid] = {\"sig\": 0, \"total\": 0}\n            by_run[rid][\"total\"] += 1\n            if e[\"significant\"]:\n                by_run[rid][\"sig\"] += 1\n        for rid in sorted(by_run.keys()):\n            print(f\"  {alpha_key}/{rid}: {by_run[rid]['sig']}/{by_run[rid]['total']}\")\n\n# Table 7\nprint(\"\\n=== TABLE 7 PER-CONDITION ===\")\nt7 = data.get(\"table7_results\", {})\nfor mode in modes_to_check:\n    if mode not in t7:\n        continue\n    print(f\"\\n--- {mode} ---\")\n    for cond, cdata in t7[mode].items():\n        print(f\"  {cond} ({cdata['model']}, {cdata['data']}): {cdata['n_significant']}/{cdata['n_total']}\")\nPYEOF\n/root/miniconda3/bin/python /tmp/extract_mmct.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-19T03:20:49.557939+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== ALPHA SWEEP PER-RUN ===\\n\\n--- uniform_forward ---\\n  a000/a000_s42: 0/8\\n  a000/a000_s43: 0/8\\n  a000/a000_s44: 0/8\\n  a010/a010_s42: 0/8\\n  a025/a025_s43: 0/8\\n  a025/a025_s44: 0/8\\n  a050/a050_s42: 0/8\\n  a050/a050_s43: 0/8\\n  a050/a050_s44: 0/8\\n  a060/a060_s42_bf16: 0/8\\n  a075/a075_s42: 1/8\\n  a075/a075_s43: 1/8\\n  a075/a075_s44: 0/8\\n\\n--- weighted_pair_forward ---\\n  a000/a000_s42: 0/8\\n  a000/a000_s43: 0/8\\n  a000/a000_s44: 0/8\\n  a010/a010_s42: 1/8\\n  a025/a025_s43: 3/8\\n  a025/a025_s44: 4/8\\n  a050/a050_s42: 5/8\\n  a050/a050_s43: 5/8\\n  a050/a050_s44: 4/8\\n  a060/a060_s42_bf16: 6/8\\n  a075/a075_s42: 7/8\\n  a075/a075_s43: 6/8\\n  a075/a075_s44: 6/8\\n\\n--- weighted_global_forward ---\\n  a000/a000_s42: 0/8\\n  a000/a000_s43: 0/8\\n  a000/a000_s44: 0/8\\n  a010/a010_s42: 0/8\\n  a025/a025_s43: 0/8\\n  a025/a025_s44: 0/8\\n  a050/a050_s42: 0/8\\n  a050/a050_s43: 0/8\\n  a050/a050_s44: 0/8\\n  a060/a060_s42_bf16: 0/8\\n  a075/a075_s42: 1/8\\n  a075/a075_s43: 1/8\\n  a075/a075_s44: 0/8\\n\\n--- uniform_bidirectional ---\\n  a000/a000_s42: 0/8\\n  a000/a000_s43: 0/8\\n  a000/a000_s44: 0/8\\n  a010/a010_s42: 0/8\\n  a025/a025_s43: 0/8\\n  a025/a025_s44: 0/8\\n  a050/a050_s42: 0/8\\n  a050/a050_s43: 0/8\\n  a050/a050_s44: 0/8\\n  a060/a060_s42_bf16: 0/8\\n  a075/a075_s42: 1/8\\n  a075/a075_s43: 1/8\\n  a075/a075_s44: 0/8\\n\\n--- weighted_pair_bidirectional ---\\n  a000/a000_s42: 0/8\\n  a000/a000_s43: 0/8\\n  a000/a000_s44: 0/8\\n  a010/a010_s42: 1/8\\n  a025/a025_s43: 3/8\\n  a025/a025_s44: 4/8\\n  a050/a050_s42: 5/8\\n  a050/a050_s43: 5/8\\n  a050/a050_s44: 4/8\\n  a060/a060_s42_bf16: 6/8\\n  a075/a075_s42: 7/8\\n  a075/a075_s43: 6/8\\n  a075/a075_s44: 6/8\\n\\n--- weighted_global_bidirectional ---\\n  a000/a000_s42: 0/8\\n  a000/a000_s43: 0/8\\n  a000/a000_s44: 0/8\\n  a010/a010_s42: 0/8\\n  a025/a025_s43: 0/8\\n  a025/a025_s44: 0/8\\n  a050/a050_s42: 0/8\\n  a050/a050_s
…[truncated 2175 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-19T03:20:49.558222+00:00_

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
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
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

_source line 82 · 2026-05-19T03:20:49.558438+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-19T03:20:49.558615+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-19T03:20:49.558811+00:00_

D040
_project
a050_s44_draft_versions.tex
a075_analysis_prep.md
alpha_sweep
alpha_sweep_a000_s43
alpha_sweep_a000_s44
alpha_sweep_a005_s42
alpha_sweep_a010_s42_v2
alpha_sweep_a010_s43
alpha_sweep_a050_s42
alpha_sweep_a050_s43
alpha_sweep_a050_s44
alpha_sweep_a060_s42_bf16
alpha_sweep_a075_s42
alpha_sweep_a075_s43
alpha_sweep_a075_s44
alpha_sweep_c4_a050_s42_bf16
analysis
analysis_alpha_sweep_a010_s42_v2.md
analyze_extended.py
analyze_mvp.py
c4_vs_wikitext_a050_collapse.md
ccf_maxlag7_report.md
check_progress.sh
consensus_framework
cross_alpha_aggregation
cross_alpha_analysis_v4.py
cross_alpha_v4_ready.md
d024_literature_notes.md
d026_optimized_commands.md
d059_mvp_reverse_reanalysis.md
d060_pythia69b_prep.md
d061_conditional_granger_analysis.md
detrending_utils.py
diag_gen_gpt2m_a100_s43_bf16.md
dose_response_fp32.csv
dose_response_fp32_detail.csv
dream_reports
drift_discrepancy_audit
effrank_trajectories.csv
figures
framing_alignment_check.md
gen_gpt2m_a100_s43_bf16
gen_wiki_gpt2m_a025_s42
gen_wiki_gpt2m_a100_s42_v3
gen_wiki_gpt2m_a100_s42_v4
generalization_draft.tex
generalization_prep.md
generalize_pythia14b_wiki_a100_s43
generalize_pythia1b_c4_a100_s42
generalize_pythia1b_c4_a100_s43
generalize_pythia410m
generalize_pythia410m_wiki_a100_s42
gpt2m_a025_analysis_plan.md
gpt2m_kappa
intervention_reactive_s42
iterative_train.py
literature_map.yaml
literature_scan_20260514.md
literature_scan_20260515
manifest.yaml
method_ablation
method_ablation_phase2
method_ablation_phase3
metrics.py
mvp_evaluation_criteria.md
panel_analysis_feasibility.md
paper_consistency_audit.md
permutation_granger.py
pipeline_analysis
plan_006_s42
prep_c4_gpt2m_readiness.md
prep_cross_alpha_v5_verify.md
prepare_data.py
report_gen_wiki_gpt2m_failure.md
review_issues.yaml
review_reports
run_mvp.sh
scale_14b_a050_s42
scale_14b_effrank_analysis
scale_s42_failure_analysis.md
shapley_method_contribution.pdf
shapley_method_contribution.png
shapley_values.json
table7_draft.md
tables
test_alpha_sweep.p
…[truncated 57 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-19T03:20:49.559038+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/mmct_full_results.md",
  "content": "# MMCT Full Results Across All Completed Experiments\n\nGenerated: 2026-05-19\nData source: unified_5method (2-sigma threshold, Table 7 params: n_perm=5000, xcorr_lag=5, granger_lag=1, alpha=0.05)\nNull baseline: 3 seeds x 8 pairs = 24 null observations from alpha=0.00\n\n## Summary: FPR and Detection Rate by Alpha (Aggregated)\n\n| Mode | FPR (a=0.00) | a0.10 | a0.25 | a0.50 | a0.60 | a0.75 |\n|------|-------------|-------|-------|-------|-------|-------|\n| uniform_forward | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0833 |\n| uniform_bidirectional | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0833 |\n| weighted_pair_forward | 0.0000 | 0.1250 | 0.4375 | 0.5833 | 0.7500 | 0.7917 |\n| weighted_pair_bidirectional | 0.0000 | 0.1250 | 0.4375 | 0.5833 | 0.7500 | 0.7917 |\n| weighted_global_forward | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0833 |\n| weighted_global_bidirectional | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0417 |\n\n## Alpha Sweep: Per-Run Results (sig_pairs / 8 total)\n\n| Condition | alpha | Model | Seed | unif_fwd | wpair_fwd | wglobal_fwd | unif_bidir | wpair_bidir | wglobal_bidir | Notes |\n|-----------|-------|-------|------|----------|-----------|-------------|------------|-------------|---------------|-------|\n| a000_s42 | 0.00 | Pythia-410M | 42 | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 | Null baseline |\n| a000_s43 | 0.00 | Pythia-410M | 43 | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 | Null baseline |\n| a000_s44 | 0.00 | Pythia-410M | 44 | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 | Null baseline |\n| a010_s42 | 0.10 | Pythia-410M | 42 | 0/8 | 1/8 | 0/8 | 0/8 | 1/8 | 0/8 | NEW; single seed only (s43/s44 not available) |\n| a025_s43 | 0.25 | Pythia-410M | 43 | 0/8 | 3/8 | 0/8 | 0/8 | 3/8 | 0/8 | |\n| a025_s44 | 0.25 | Pythia-410M | 44 | 0/8 | 4/8 | 0/8 | 0/8 | 4/8 | 0/8 | |\n| a050_s42 | 0.50 | Pythia-410M | 42 | 0/8 | 5/8 | 0/8 | 0/8 | 5/8 | 0/8 | |\n| a050_s43 | 0.50 | Pythia-410M | 43 | 0/8 | 5/8 | 0/8 | 0/8 | 5/8 | 0/8 | |\n| a050_s44 | 0.50 | Pythia-410M | 44 | 0/8 | 4/8 | 0/8 | 0/8 | 4/8 | 0/8 | |\n| a060_s42_bf16 | 0.60 | Pythia-410M | 42 | 0/8 | 6/8 | 0/8 | 0/8 | 6/8 | 0/8 | bf16 precision; single seed |\n| a075_s42 | 0.75 | Pythia-410M | 42 | 1/8 | 7/8 | 1/8 | 1/8 | 7/8 | 1/8 | |\n| a075_s43 | 0.75 | Pythia-410M | 43 | 1/8 | 6/8 | 1/8 | 1/8 | 6/8 | 0/8 | |\n| a075_s44 | 0.75 | Pythia-410M | 44 | 0/8 | 6/8 | 0/8 | 0/8 | 6/8 | 0/8 | |\n\n## Table 7: Generalization Results (alpha=1.00, sig_pairs / 8 total)\n\n| Condition | alpha | Model | Data | unif_fwd | wpair_fwd | wglobal_fwd | unif_bidir | wpair_bidir | wglobal_bidir | Notes |\n|-----------|-------|-------|------|----------|-----------|-------------|------------|-------------|---------------|-------|\n| Baseline | 1.00 | Pythia-410M | Wiki | 1/8 | 6/8 | 2/8 | 1/8 | 5/8 | 2/8 | |\n| Arch: GPT-2m | 1.00 | GPT-2m | Wiki | 2/8 | 8/8 | 2/8 | 2/8 | 7/8 | 2/8 | Best wpair detection |\n| Arch: OPT | 1.00 | OPT-1.3B | Wiki | 0/8 | 6/8 | 0/8 | 0/8 | 5/8 | 0/8 | |\n| Scale: 1.4B s42 | 1.00 | Pythia-1.4B | Wiki | 0/8 | 6/8 | 0/8 | 0/8 | 6/8 | 0/8 | |\n| Scale: 1.4B s43 | 1.00 | Pythia-1.4B | Wiki | 2/8 | 6/8 | 2/8 | 2/8 | 5/8 | 1/8 | |\n| Domain: C4 s42 | 1.00 | Pythia-1B | C4 | 1/8 | 7/8 | 1/8 | 1/8 | 6/8 | 1/8 | |\n| Domain: C4 s43 | 1.00 | Pythia-1B | C4 | 2/8 | 6/8 | 2/8 | 2/8 | 6/8 | 1/8 | |\n\n## Missing Experiments (Not Available for MMCT)\n\n| Condition | Reason |\n|-----------|--------|\n| a010_s43 | Experiment directory does not exist |\n| a010_s44 | Experiment directory does not exist |\n| a025_s42 | Experiment directory does not exist |\n| gen_wiki_gpt2m_a100_s42_v4 | Directory does not exist; GPT-2m alpha=1.00 s42 covered via generalize/gpt2m_wiki_a100_s42 |\n| gen_wiki_gpt2m_a100_s43 | Incomplete: only 3/11 generations, no all_metrics.json |\n\n## Key Observations\n\n1. **FPR = 0 across all modes**: No false positives at alpha=0.00 (0/24 in every mode).\n\n2. **weighted_pair is the most sensitive mode**: Detection rates monotonically increase with alpha (0.125 at a0.10, 0.4375 at a0.25, 0.5833 at a0.50, 0.75 at a0.60, 0.7917 at a0.75). FPR remains zero.\n\n3. **uniform and weighted_global are conservative**: Only detect at alpha>=0.75, and even then only 1-2/24 pairs.\n\n4. **Bidirectional adds minimal filtering**: weighted_pair_bidirectional matches weighted_pair_forward exactly in the alpha sweep (the directional asymmetry filter rarely changes the call).\n\n5. **Table 7 generalization**: weighted_pair_forward detects 6-8/8 pairs across all 7 conditions at alpha=1.00, confirming generalization across architectures (GPT-2m, OPT-1.3B), scales (410M to 1.4B), and domains (Wiki, C4).\n\n6. **Dose-response monotonicity** (weighted_pair_forward pooled rates):\n   - a0.00: 0.000\n   - a0.10: 0.125\n   - a0.25: 0.438\n   - a0.50: 0.583\n   - a0.60: 0.750\n   - a0.75: 0.792\n   - a1.00 (Table 7 avg): 0.813\n\n## Source Files\n\n- Full MMCT results JSON: `westd-19828:/root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results/mmct_results_v2.json`\n- Null distribution: `westd-19828:/root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results/null_distribution_v2.json`\n- FPR/FNR comparison: `westd-19828:/root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results/fpr_fnr_comparison_v2.md`\n- Table 7 detail: `westd-19828:/root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results/mmct_table7.md`\n- Per-condition unified data: `westd-19828:/root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results/unified_data/*.json`\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/mmct_full_results.md",
    "content": "# MMCT Full Results Across All Completed Experiments\n\nGenerated: 2026-05-19\nData source: unified_5method (2-sigma threshold, Table 7 params: n_perm=5000, xcorr_lag=5, granger_lag=1, alpha=0.05)\nNull baseline: 3 seeds x 8 pairs = 24 null observations from alpha=0.00\n\n## Summary: FPR and Detection Rate by Alpha (Aggregated)\n\n| Mode | FPR (a=0.00) | a0.10 | a0.25 | a0.50 | a0.60 | a0.75 |\n|------|-------------|-------|-------|-------|-------|-------|\n| uniform_forward | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0833 |\n| uniform_bidirectional | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0833 |\n| weighted_pair_forward | 0.0000 | 0.1250 | 0.4375 | 0.5833 | 0.7500 | 0.7917 |\n| weighted_pair_bidirectional | 0.0000 | 0.1250 | 0.4375 | 0.5833 | 0.7500 | 0.7917 |\n| weighted_global_forward | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0833 |\n| weighted_global_bidirectional | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0417 |\n\n## Alpha Sweep: Per-Run Results (sig_pairs / 8 total)\n\n| Condition | alpha | Model | Seed | unif_fwd | wpair_fwd | wglobal_fwd | unif_bidir | wpair_bidir | wglobal_bidir | Notes |\n|-----------|-------|-------|------|----------|-----------|-------------|------------|-------------|---------------|-------|\n| a000_s42 | 0.00 | Pythia-410M | 42 | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 | Null baseline |\n| a000_s43 | 0.00 | Pythia-410M | 43 | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 | Null baseline |\n| a000_s44 | 0.00 | Pythia-410M | 44 | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 | Null baseline |\n| a010_s42 | 0.10 | Pythia-410M | 42 | 0/8 | 1/8 | 0/8 | 0/8 | 1/8 | 0/8 | NEW; single seed only (s43/s44 not available) |\n| a025_s43 | 0.25 | Pythia-410M | 43 | 0/8 | 3/8 | 0/8 | 0/8 | 3/8 | 0/8 | |\n| a025_s44 | 0.25 | Pythia-410M | 44 | 0/8 | 4/8 | 0/8 | 0/8 | 4/8 | 0/8 | |\n| a050_s42 | 0.50 | Pythia-410M | 42 | 0/8 | 5/8 | 0/8 | 0/8 | 5/8 | 0/8 | |\n| a050_s43 | 0.50 | Pythia-410M | 43 | 0/8 | 5/8 | 0/8 | 0/8 | 5/8 | 0/8 | |\n| a050_s44 | 0.50 | Pythia-410M | 44 | 0/8 | 4/8 | 0/8 | 0/8 | 4/8 | 0/8 | |\n| a060_s42_bf16 | 0.60 | Pythia-410M | 42 | 0/8 | 6/8 | 0/8 | 0/8 | 6/8 | 0/8 | bf16 precision; single seed |\n| a075_s42 | 0.75 | Pythia-410M | 42 | 1/8 | 7/8 | 1/8 | 1/8 | 7/8 | 1/8 | |\n| a075_s43 | 0.75 | Pythia-410M | 43 | 1/8 | 6/8 | 1/8 | 1/8 | 6/8 | 0/8 | |\n| a075_s44 | 0.75 | Pythia-410M | 44 | 0/8 | 6/8 | 0/8 | 0/8 | 6/8 | 0/8 | |\n\n## Table 7: Generalization Results (alpha=1.00, sig_pairs / 8 total)\n\n| Condition | alpha | Model | Data | unif_fwd | wpair_fwd | wglobal_fwd | unif_bidir | wpair_bidir | wglobal_bidir | Notes |\n|-----------|-------|-------|------|----------|-----------|-------------|------------|-------------|---------------|-------|\n| Baseline | 1.00 | Pythia-410M | Wiki | 1/8 | 6/8 | 2/8 | 1/8 | 5/8 | 2/8 | |\n| Arch: GPT-2m | 1.00 | GPT-2m | Wiki | 2/8 | 8/8 | 2/8 | 2/8 | 7/8 | 2/8 | Best wpair detection |\n| Arch: OPT | 1.00 | OPT-1.3B | Wiki | 0/8 | 6/8 | 0/8 | 0/8 | 5/8 | 0/8 | |\n| Scale: 1.4B s42 | 1.00 | Pythia-1.4B | Wiki | 0/8 | 6/8 | 0/8 | 0/8 | 6/8 | 0/8 | |\n| Scale: 1.4B s43 | 1.00 | Pythia-1.4B | Wiki | 2/8 | 6/8 | 2/8 | 2/8 | 5/8 | 1/8 | |\n| Domain: C4 s42 | 1.00 | Pythia-1B | C4 | 1/8 | 7/8 | 1/8 | 1/8 | 6/8 | 1/8 | |\n| Domain: C4 s43 | 1.00 | Pythia-1B | C4 | 2/8 | 6/8 | 2/8 | 2/8 | 6/8 | 1/8 | |\n\n## Missing Experiments (Not Available for MMCT)\n\n| Condition | Reason |\n|-----------|--------|\n| a010_s43 | Experiment directory does not exist |\n| a010_s44 | Experiment directory does not exist |\n| a025_s42 | Experiment directory does not exist |\n| gen_wiki_gpt2m_a100_s42_v4 | Directory does not exist; GPT-2m alpha=1.00 s42 covered via generalize/gpt2m_wiki_a100_s42 |\n| gen_wiki_gpt2m_a100_s43 | Incomplete: only 3/11 generations, no all_metrics.json |\n\n## Key Observations\n\n1. **FPR = 0 across all modes**: No false positives at alpha=0.00 (0/24 in every mode).\n\n2. **weighted_pair is the most sensitive mode**: Detection rates monotonically increase with alpha (0.125 at a0.10, 0.4375 at a0.25, 0.5833 at a0.50, 0.75 at a0.60, 0.7917 at a0.75). FPR remains zero.\n\n3. **uniform and weighted_global are conservative**: Only detect at alpha>=0.75, and even then only 1-2/24 pairs.\n\n4. **Bidirectional adds minimal filtering**: weighted_pair_bidirectional matches weighted_pair_forward exactly in the alpha sweep (the directional asymmetry filter rarely changes the call).\n\n5. **Table 7 generalization**: weighted_pair_forward detects 6-8/8 pairs across all 7 conditions at alpha=1.00, confirming generalization across architectures (GPT-2m, OPT-1.3B), scales (410M to 1.4B), and domains (Wiki, C4).\n\n6. **Dose-response monotonicity** (weighted_pair_forward pooled rates):\n   - a0.00: 0.000\n   - a0.10: 0.125\n   - a0.25: 0.438\n   - a0.50: 0.583\n   - a0.60: 0.750\n   - a0.75: 0.792\n   - a1.00 (Table 7 avg): 0.813\n\n## Source Files\n\n- Full MMCT results JSON: `westd-19828:/root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results/mmct_results_v2.json`\n- Null distribution: `westd-19828:/root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results/null_distribution_v2.json`\n- FPR/FNR comparison: `westd-19828:/root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results/fpr_fnr_comparison_v2.md`\n- Table 7 detail: `westd-19828:/root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results/mmct_table7.md`\n- Per-condition unified data: `westd-19828:/root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results/unified_data/*.json`\n"
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-19T03:20:49.559318+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/mmct_full_results.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-19T03:20:49.559528+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "MMCT Full Results (All Experiments)",
  "type": "report",
  "description": "Comprehensive MMCT results across all 20 completed experiments: 13 alpha-sweep runs (a0.00-a0.75) + 7 Table 7 generalization conditions (a1.00). Includes per-run sig counts for all 6 MMCT modes, FPR/detection rate summary, and dose-response analysis.",
  "project": "distrib_canary_collapse",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/mmct_full_results.md",
  "tags": "['mmct', 'analysis', 'reviewer-response']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "MMCT Full Results (All Experiments)",
    "type": "report",
    "description": "Comprehensive MMCT results across all 20 completed experiments: 13 alpha-sweep runs (a0.00-a0.75) + 7 Table 7 generalization conditions (a1.00). Includes per-run sig counts for all 6 MMCT modes, FPR/detection rate summary, and dose-response analysis.",
    "project": "distrib_canary_collapse",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/mmct_full_results.md",
    "tags": "['mmct', 'analysis', 'reviewer-response']"
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-19T03:20:49.559738+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260519_73c8d3\", \"name\": \"MMCT Full Results (All Experiments)\", \"type\": \"report\", \"description\": \"Comprehensive MMCT results across all 20 completed experiments: 13 alpha-sweep runs (a0.00-a0.75) + 7 Table 7 generalization conditions (a1.00). Includes per-run sig counts for all 6 MMCT modes, FPR/detection rate summary, and dose-response analysis.\", \"path\": \"projects/distrib_canary_collapse/artifacts/_project/report/mmct_full_results.md\", \"url\": null, \"project\": \"distrib_canary_collapse\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-19T03:20:38.241698+00:00\", \"tags\": [\"mmct\", \"analysis\", \"reviewer-response\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 89 · 2026-05-19T03:20:49.559959+00:00_

完成。汇总：

**执行内容：**
1. 为 `a010_s42` 生成了缺失的 unified 5-method 分析数据
2. 重新运行 MMCT，覆盖 20 个实验：13 个 alpha-sweep (含新增的 a010、a060) + 7 个 Table 7 generalize 条件

**关键结果：**
- FPR = 0（所有 6 种 MMCT 模式在 alpha=0.00 均无假阳性）
- `weighted_pair_forward` 检测率随 alpha 单调递增：0.00 → 0.125 → 0.438 → 0.583 → 0.750 → 0.792 → 0.813 (Table 7 均值)
- Table 7 全部 7 个泛化条件在 `weighted_pair_forward` 下检测率 6/8 到 8/8
- `uniform` 和 `weighted_global` 模式较保守，仅在 alpha>=0.75 有少量检测

**无法运行的实验：**
- `a010_s43`, `a010_s44`, `a025_s42`: 实验目录不存在
- `gen_wiki_gpt2m_a100_s43`: 未完成（3/11 generations）

产出文件：`artifacts/mmct_full_results.md`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_mmct_full_coverage_20260519T031507"
}
```

</details>

---
