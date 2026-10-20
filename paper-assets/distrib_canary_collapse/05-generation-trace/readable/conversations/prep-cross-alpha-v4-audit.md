# prep cross alpha v4 audit

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 59
- **Recorded user turns:** 0
- **Tool calls:** 29
- **Original source:** `logs/chats/worker_prep_cross_alpha_v4_audit_20260515T113914.jsonl`
- **Structured JSON:** [`a4405fc47fbca9db7172.json`](../../sessions/a4/a4405fc47fbca9db7172.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

59 recorded events

### Tool call

_source line 1 · 2026-05-15T11:43:27.401363+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T11:43:27.401644+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T11:43:27.401799+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "find /root/autodl-tmp/distrib_canary_collapse/ -name \"*cross_alpha*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "find /root/autodl-tmp/distrib_canary_collapse/ -name \"*cross_alpha*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T11:43:27.401945+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/__pycache__/cross_alpha_analysis_v4.cpython-312.pyc\\n/root/autodl-tmp/distrib_canary_collapse/results/analysis/cross_alpha_analysis.json\\n/root/autodl-tmp/distrib_canary_collapse/results/analysis/cross_alpha_analysis.md\\n/root/autodl-tmp/distrib_canary_collapse/results/analysis/cross_alpha_v3_full.json\\n/root/autodl-tmp/distrib_canary_collapse/results/analysis/cross_alpha_v4.json\\n/root/autodl-tmp/distrib_canary_collapse/results/analysis/cross_alpha_v4_report.md\\n/root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis.py\\n/root/autodl-tmp/distrib_canary_collapse/cross_alpha_v3_analysis.py\\n/root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis_v4.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.2}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T11:43:27.402092+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "wc -l /root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis_v4.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "wc -l /root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis_v4.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T11:43:27.402219+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"873 /root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis_v4.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T11:43:27.402445+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "head -300 /root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis_v4.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "head -300 /root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis_v4.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T11:43:27.402771+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Cross-alpha analysis v4 with per-alpha consensus classification.\\n\\nExtends v3 with:\\n  5. Per-alpha multi-method consensus classification (regime-dependent validity)\\n  6. Markdown report output\\n\\nHandles mixed data paths:\\n  - alpha-sweep: results/alpha_sweep/a{NNN}_s42/all_metrics.json (single seed)\\n  - alpha=1.0:   results/mvp/rep_{42..45}/all_metrics.json (4 seeds)\\n  - alpha=1.0 consensus loads existing method_ablation.json\\n  - Single-seed alpha points: seed_threshold=1, method agreement only\\n\\nDependencies: numpy, scipy, statsmodels\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport glob\\nimport json\\nimport os\\nimport re\\nimport sys\\nimport warnings\\nfrom datetime import datetime\\n\\nimport numpy as np\\nfrom statsmodels.stats.multitest import multipletests\\n\\nwarnings.filterwarnings(\\\"ignore\\\")\\n\\nBASE_DIR = os.path.dirname(os.path.abspath(__file__))\\nsys.path.insert(0, BASE_DIR)\\n\\nfrom method_ablation import (\\n    CANARY, DOWNSTREAM,\\n    extract as ma_extract,\\n    naive_pearson, diff_xcorr, threshold_lead, toda_yamamoto, perm_granger,\\n)\\nfrom consensus_framework import classify_robust, load_sig_matrix, NumpyEncoder\\n\\nSWEEP_DIR = os.path.join(BASE_DIR, \\\"results\\\", \\\"alpha_sweep\\\")\\nMVP_DIR = os.path.join(BASE_DIR, \\\"results\\\", \\\"mvp\\\")\\nANALYSIS_DIR = os.path.join(BASE_DIR, \\\"results\\\", \\\"analysis\\\")\\n\\nMETRICS = [\\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\", \\\"token_entropy\\\", \\\"ece\\\", \\\"perplexity\\\"]\\n\\nGRANGER_PAIRS = [\\n    (\\\"token_entropy\\\", \\\"distinct_1\\\", \\\"entropy->d1\\\"),\\n    (\\\"ece\\\",           \\\"distinct_1\\\", \\\"ECE->d1\\\"),\\n    (\\\"token_entropy\\\", \\\"distinct_2\\\", \\\"entropy->d2\\\"),\\n    (\\\"ece\\\",           \\\"distinct_2\\\", \\\"ECE->d2\\\"),\\n    (\\\"distinct_1\\\", \\\"token_entropy\\\", \\\"d1->entropy\\\"),\\n    (\\\"distinct_1\\\",
…[truncated 7272 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T11:43:27.402962+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "tail -n +301 /root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis_v4.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "tail -n +301 /root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis_v4.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T11:43:27.403226+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"                std_a, std_b = np.std(a, ddof=1), np.std(b, ddof=1)\\n                if std_a < 1e-15 or std_b < 1e-15:\\n                    r = 0.0\\n                else:\\n                    r = float(np.corrcoef(a, b)[0, 1])\\n                lags[str(lag)] = round(r, 4)\\n                if abs(r) > abs(best_r):\\n                    best_lag, best_r = lag, r\\n            entry[pair_label] = {\\n                \\\"peak_lag\\\": best_lag,\\n                \\\"peak_r\\\": round(best_r, 4),\\n                \\\"lags\\\": lags,\\n            }\\n        result[alpha_key] = entry\\n    return result\\n\\n\\n# ---------------------------------------------------------------------------\\n# 4. Per-gen velocity\\n# ---------------------------------------------------------------------------\\n\\ndef per_gen_velocity(all_data):\\n    result = {}\\n    for alpha_key, alpha_val, metrics_list in all_data:\\n        vals = extract_series(metrics_list, \\\"distinct_1\\\")\\n        deltas = np.diff(vals)\\n        n = len(deltas)\\n        mid = n // 2\\n        early_mean = float(np.mean(deltas[:mid])) if mid > 0 else None\\n        late_mean = float(np.mean(deltas[mid:])) if mid < n else None\\n        max_drop_idx = int(np.argmin(deltas))\\n        result[alpha_key] = {\\n            \\\"alpha\\\": alpha_val,\\n            \\\"d1_values\\\": [round(float(v), 6) for v in vals],\\n            \\\"d1_deltas\\\": [round(float(d), 6) for d in deltas],\\n            \\\"cumulative_drift_pct\\\": round((vals[-1] - vals[0]) / abs(vals[0]) * 100, 2),\\n            \\\"mean_velocity\\\": round(float(np.mean(deltas)), 6),\\n            \\\"max_drop_gen\\\": max_drop_idx,\\n            \\\"max_drop_value\\\": round(float(deltas[max_drop_idx]), 6),\\n            \\\"early_mean_velocity\\\": round(early_mean, 6) if early_mean is not None else None,\\n            \\\"late_mean_velocity\\\": round(late_mean, 6) if late_mean is 
…[truncated 7137 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T11:43:27.403521+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "head -200 /root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis_v4.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "head -200 /root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis_v4.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T11:43:27.403870+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Cross-alpha analysis v4 with per-alpha consensus classification.\\n\\nExtends v3 with:\\n  5. Per-alpha multi-method consensus classification (regime-dependent validity)\\n  6. Markdown report output\\n\\nHandles mixed data paths:\\n  - alpha-sweep: results/alpha_sweep/a{NNN}_s42/all_metrics.json (single seed)\\n  - alpha=1.0:   results/mvp/rep_{42..45}/all_metrics.json (4 seeds)\\n  - alpha=1.0 consensus loads existing method_ablation.json\\n  - Single-seed alpha points: seed_threshold=1, method agreement only\\n\\nDependencies: numpy, scipy, statsmodels\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport glob\\nimport json\\nimport os\\nimport re\\nimport sys\\nimport warnings\\nfrom datetime import datetime\\n\\nimport numpy as np\\nfrom statsmodels.stats.multitest import multipletests\\n\\nwarnings.filterwarnings(\\\"ignore\\\")\\n\\nBASE_DIR = os.path.dirname(os.path.abspath(__file__))\\nsys.path.insert(0, BASE_DIR)\\n\\nfrom method_ablation import (\\n    CANARY, DOWNSTREAM,\\n    extract as ma_extract,\\n    naive_pearson, diff_xcorr, threshold_lead, toda_yamamoto, perm_granger,\\n)\\nfrom consensus_framework import classify_robust, load_sig_matrix, NumpyEncoder\\n\\nSWEEP_DIR = os.path.join(BASE_DIR, \\\"results\\\", \\\"alpha_sweep\\\")\\nMVP_DIR = os.path.join(BASE_DIR, \\\"results\\\", \\\"mvp\\\")\\nANALYSIS_DIR = os.path.join(BASE_DIR, \\\"results\\\", \\\"analysis\\\")\\n\\nMETRICS = [\\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\", \\\"token_entropy\\\", \\\"ece\\\", \\\"perplexity\\\"]\\n\\nGRANGER_PAIRS = [\\n    (\\\"token_entropy\\\", \\\"distinct_1\\\", \\\"entropy->d1\\\"),\\n    (\\\"ece\\\",           \\\"distinct_1\\\", \\\"ECE->d1\\\"),\\n    (\\\"token_entropy\\\", \\\"distinct_2\\\", \\\"entropy->d2\\\"),\\n    (\\\"ece\\\",           \\\"distinct_2\\\", \\\"ECE->d2\\\"),\\n    (\\\"distinct_1\\\", \\\"token_entropy\\\", \\\"d1->entropy\\\"),\\n    (\\\"distinct_1\\\",
…[truncated 5837 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T11:43:27.404133+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "grep -n \"def \" /root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis_v4.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "grep -n \"def \" /root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis_v4.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T11:43:27.404364+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"77:def _find_mvp_seeds():\\n88:def discover_alpha_dirs(explicit=None, include_mvp=True):\\n127:def load_metrics(alpha_dir):\\n134:def load_all_seeds_metrics(alpha_val, primary_dir, seeds):\\n148:def extract_series(metrics_list, key):\\n156:def compute_dose_response(all_data):\\n177:def _build_lag_matrix(y, x, max_lag):\\n190:def _granger_f_stat(y, x, max_lag):\\n208:def permutation_granger_test(x, y, max_lag=1, n_perm=5000, seed=42, difference=True):\\n243:def run_granger_all(all_data, max_lag=1, n_perms=5000):\\n261:def apply_fdr(granger_results):\\n283:def cross_correlation(all_data, max_lag=3):\\n322:def per_gen_velocity(all_data):\\n351:def run_consensus_per_alpha(alpha_dirs, mvp_ablation_path=None, consensus_n_perm=1000):\\n463:def consensus_regime_comparison(consensus_results):\\n508:def generate_markdown_report(output, out_path):\\n639:def auto_version():\\n650:def print_summary(output):\\n763:def main():\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T11:43:27.404567+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "head -462 /root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis_v4.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "head -462 /root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis_v4.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T11:43:27.404950+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Cross-alpha analysis v4 with per-alpha consensus classification.\\n\\nExtends v3 with:\\n  5. Per-alpha multi-method consensus classification (regime-dependent validity)\\n  6. Markdown report output\\n\\nHandles mixed data paths:\\n  - alpha-sweep: results/alpha_sweep/a{NNN}_s42/all_metrics.json (single seed)\\n  - alpha=1.0:   results/mvp/rep_{42..45}/all_metrics.json (4 seeds)\\n  - alpha=1.0 consensus loads existing method_ablation.json\\n  - Single-seed alpha points: seed_threshold=1, method agreement only\\n\\nDependencies: numpy, scipy, statsmodels\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport glob\\nimport json\\nimport os\\nimport re\\nimport sys\\nimport warnings\\nfrom datetime import datetime\\n\\nimport numpy as np\\nfrom statsmodels.stats.multitest import multipletests\\n\\nwarnings.filterwarnings(\\\"ignore\\\")\\n\\nBASE_DIR = os.path.dirname(os.path.abspath(__file__))\\nsys.path.insert(0, BASE_DIR)\\n\\nfrom method_ablation import (\\n    CANARY, DOWNSTREAM,\\n    extract as ma_extract,\\n    naive_pearson, diff_xcorr, threshold_lead, toda_yamamoto, perm_granger,\\n)\\nfrom consensus_framework import classify_robust, load_sig_matrix, NumpyEncoder\\n\\nSWEEP_DIR = os.path.join(BASE_DIR, \\\"results\\\", \\\"alpha_sweep\\\")\\nMVP_DIR = os.path.join(BASE_DIR, \\\"results\\\", \\\"mvp\\\")\\nANALYSIS_DIR = os.path.join(BASE_DIR, \\\"results\\\", \\\"analysis\\\")\\n\\nMETRICS = [\\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\", \\\"token_entropy\\\", \\\"ece\\\", \\\"perplexity\\\"]\\n\\nGRANGER_PAIRS = [\\n    (\\\"token_entropy\\\", \\\"distinct_1\\\", \\\"entropy->d1\\\"),\\n    (\\\"ece\\\",           \\\"distinct_1\\\", \\\"ECE->d1\\\"),\\n    (\\\"token_entropy\\\", \\\"distinct_2\\\", \\\"entropy->d2\\\"),\\n    (\\\"ece\\\",           \\\"distinct_2\\\", \\\"ECE->d2\\\"),\\n    (\\\"distinct_1\\\", \\\"token_entropy\\\", \\\"d1->entropy\\\"),\\n    (\\\"distinct_1\\\",
…[truncated 7349 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T11:43:27.405240+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "grep -n \"def threshold_lead\" /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "grep -n \"def threshold_lead\" /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T11:43:27.405439+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"142:def threshold_lead(c, d, cn, dn):\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T11:43:27.405568+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "grep -n \"def load_sig_matrix\\|def classify_robust\\|significant_fdr\\|significant\" /root/autodl-tmp/distrib_canary_collapse/consensus_framework.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "grep -n \"def load_sig_matrix\\|def classify_robust\\|significant_fdr\\|significant\" /root/autodl-tmp/distrib_canary_collapse/consensus_framework.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T11:43:27.405686+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T11:43:27.405801+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "grep -n \"def threshold_lead\\|return\\|significant\\|p_value\\|p_raw\" /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "grep -n \"def threshold_lead\\|return\\|significant\\|p_value\\|p_raw\" /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T11:43:27.405919+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T11:43:27.406031+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "grep -n \"def load_sig_matrix\" /root/autodl-tmp/distrib_canary_collapse/consensus_framework.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "grep -n \"def load_sig_matrix\" /root/autodl-tmp/distrib_canary_collapse/consensus_framework.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T11:43:27.406144+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"53:def load_sig_matrix(ablation_path, apply_fdr=True):\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T11:43:27.406266+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "grep -n \"significant_fdr\" /root/autodl-tmp/distrib_canary_collapse/consensus_framework.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "grep -n \"significant_fdr\" /root/autodl-tmp/distrib_canary_collapse/consensus_framework.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T11:43:27.406409+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"89:                            sig[mi, pi, si] = seed_rec[method].get(\\\"significant_fdr\\\", False)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T11:43:27.406547+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "head -120 /root/autodl-tmp/distrib_canary_collapse/consensus_framework.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "head -120 /root/autodl-tmp/distrib_canary_collapse/consensus_framework.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T11:43:27.406732+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nMulti-method consensus framework for canary→downstream association robustness.\\n\\nFormalizes \\\"robust association\\\": a pair is robust only when ≥method_threshold\\nindependent statistical methods agree (each requiring ≥seed_threshold seeds\\nsignificant). Two-stage aggregation: seed→method verdict, then method→consensus.\\n\\nInput:  results/mvp/analysis/method_ablation.json\\nOutput: consensus classification, sensitivity heatmap, FPR/FNR table (JSON)\\n\\nDependencies: numpy, json (stdlib)\\n\\\"\\\"\\\"\\n\\nimport json\\nimport os\\n\\nimport numpy as np\\n\\nMETHOD_NAMES = [\\n    \\\"naive_pearson\\\",\\n    \\\"differenced_xcorr\\\",\\n    \\\"threshold_onset\\\",\\n    \\\"toda_yamamoto\\\",\\n    \\\"permutation_granger\\\",\\n]\\n\\n# Primary FPR ground truth: alpha=0.0 null control; differenced_xcorr retained for legacy\\nDIFF_INDEX = 1\\n\\n\\ndef _to_native(obj):\\n    \\\"\\\"\\\"Convert numpy types to Python native for JSON serialization.\\\"\\\"\\\"\\n    if isinstance(obj, (np.integer,)):\\n        return int(obj)\\n    if isinstance(obj, (np.floating,)):\\n        return float(obj)\\n    if isinstance(obj, (np.bool_,)):\\n        return bool(obj)\\n    if isinstance(obj, np.ndarray):\\n        return obj.tolist()\\n    return obj\\n\\n\\nclass NumpyEncoder(json.JSONEncoder):\\n    \\\"\\\"\\\"JSON encoder that handles numpy types.\\\"\\\"\\\"\\n    def default(self, obj):\\n        native = _to_native(obj)\\n        if native is not obj:\\n            return native\\n        return super().default(obj)\\n\\n\\ndef load_sig_matrix(ablation_path, apply_fdr=True):\\n    \\\"\\\"\\\"\\n    Load method_ablation.json into a boolean significance tensor.\\n\\n    Args:\\n        ablation_path: path to method_ablation.json\\n\\n    Returns:\\n        sig_matrix: np.ndarray, shape (5, 16, 4), dtype bool\\n                    axes = (method, pair, seed)\\n        pair_names: list of (
…[truncated 2539 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T11:43:27.406882+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "tail -n +142 /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "tail -n +142 /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T11:43:27.407130+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"def threshold_lead(c, d, cn, dn):\\n    \\\"\\\"\\\"Lead time based on 2σ signal-onset detection.\\\"\\\"\\\"\\n    co = _onset_gen(c, cn)\\n    do = _onset_gen(d, dn)\\n    if co is None or do is None:\\n        missing = []\\n        if co is None:\\n            missing.append(\\\"canary\\\")\\n        if do is None:\\n            missing.append(\\\"downstream\\\")\\n        return {\\n            \\\"method\\\": \\\"threshold_onset\\\",\\n            \\\"canary_onset\\\": None if co is None else int(co),\\n            \\\"downstream_onset\\\": None if do is None else int(do),\\n            \\\"lead_time\\\": None,\\n            \\\"significant\\\": False,\\n            \\\"note\\\": f\\\"onset not detected for: {', '.join(missing)}\\\",\\n        }\\n    lt = do - co\\n    return {\\n        \\\"method\\\": \\\"threshold_onset\\\",\\n        \\\"canary_onset\\\": int(co),\\n        \\\"downstream_onset\\\": int(do),\\n        \\\"lead_time\\\": int(lt),\\n        \\\"significant\\\": bool(lt > 0),\\n    }\\n\\n\\n# ─── Method 4: Toda-Yamamoto augmented-lag Granger causality ─────────────────\\n# Fits VAR(p + d_max) where d_max = max integration order of the two\\n# series, but the Wald test is restricted to the first p lag coefficients.\\n# This bypasses unit-root pre-testing bias (Toda & Yamamoto 1995).\\n# With T=10, only p=1 is feasible; the F-test has very few residual df,\\n# so power is low — significant results here are highly credible.\\n\\ndef _adf_order(series, max_d=2):\\n    \\\"\\\"\\\"Integration order via iterated ADF (maxlag=1 for short series).\\\"\\\"\\\"\\n    for d in range(max_d + 1):\\n        s = series.copy()\\n        for _ in range(d):\\n            s = np.diff(s)\\n        if len(s) < 5:\\n            return d\\n        try:\\n            if adfuller(s, maxlag=1, autolag=None)[1] < 0.05:\\n                return d\\n        except Exception:\\n            pass\\n    return max_d\\n
…[truncated 7417 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T11:43:27.407373+00:00_

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
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
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

### Tool call

_source line 32 · 2026-05-15T11:43:27.407521+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "grep -n \"def perm_granger\" /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "grep -n \"def perm_granger\" /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-15T11:43:27.407649+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"a000_s42\\na025_s42\\na050_s42\\na075_s42\\nalpha_monotonicity.png\\nanalysis\\nanalysis_summary.json\\npooled_panel_results.json\\npooled_panel_summary.txt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.48}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T11:43:27.407766+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"375:def perm_granger(c, d, cn, dn, max_lag=1, n_perm=1000):\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T11:43:27.407878+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "grep -n \"consensus_regime_comparison\\|print_summary\\|generate_markdown\" /root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis_v4.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "grep -n \"consensus_regime_comparison\\|print_summary\\|generate_markdown\" /root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis_v4.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-15T11:43:27.408030+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-15T11:43:27.408164+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "head -420 /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "head -420 /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-15T11:43:27.408486+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Method ablation: compare four lead-lag estimation methods.\\n\\nCompares naive vs robust approaches to detect canary->downstream lead-lag,\\nquantifying the spurious regression rate when non-stationary series are\\ncorrelated without proper detrending.\\n\\nInput:  results/mvp/rep_{seed}/all_metrics.json (seeds 42-45)\\nOutput: results/mvp/analysis/method_ablation.json\\n        (with BH FDR correction and effect sizes)\\n\\nMethods:\\n  1. Naive Pearson lag-correlation (raw levels)\\n  2. Differenced cross-correlation (first-differenced series)\\n  3. Threshold-based lead time (2-sigma onset detection)\\n  4. Toda-Yamamoto augmented-lag Granger causality\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport os\\nimport warnings\\nfrom itertools import product\\n\\nimport numpy as np\\nfrom scipy import stats\\nfrom statsmodels.stats.multitest import multipletests\\nfrom statsmodels.tsa.stattools import adfuller\\nfrom permutation_granger import permutation_granger_test\\n\\nwarnings.filterwarnings(\\\"ignore\\\")\\n\\nCANARY = [\\\"token_entropy\\\", \\\"self_bleu\\\", \\\"ece\\\", \\\"effective_rank\\\"]\\nDOWNSTREAM = [\\\"perplexity\\\", \\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\"]\\n\\n# Sign conventions: \\\"higher is worse\\\" kept as-is; \\\"lower is worse\\\" negated\\n# so that degradation = positive direction in all analyses.\\nHIGHER_IS_WORSE = {\\\"self_bleu\\\", \\\"ece\\\", \\\"perplexity\\\"}\\nLOWER_IS_WORSE = {\\\"token_entropy\\\", \\\"effective_rank\\\",\\n                   \\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\"}\\n\\nALPHA = 0.05\\n\\n\\ndef load_metrics(data_dir, seeds):\\n    \\\"\\\"\\\"Load all_metrics.json for each seed.\\\"\\\"\\\"\\n    data = {}\\n    for s in seeds:\\n        path = os.path.join(data_dir, f\\\"rep_{s}\\\", \\\"all_metrics.json\\\")\\n        with open(path) as f:\\n            data[s] = json.load(f)\\n    return 
…[truncated 7372 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-15T11:43:27.408660+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "head -510 /root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis_v4.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "head -510 /root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis_v4.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-15T11:43:27.408936+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Cross-alpha analysis v4 with per-alpha consensus classification.\\n\\nExtends v3 with:\\n  5. Per-alpha multi-method consensus classification (regime-dependent validity)\\n  6. Markdown report output\\n\\nHandles mixed data paths:\\n  - alpha-sweep: results/alpha_sweep/a{NNN}_s42/all_metrics.json (single seed)\\n  - alpha=1.0:   results/mvp/rep_{42..45}/all_metrics.json (4 seeds)\\n  - alpha=1.0 consensus loads existing method_ablation.json\\n  - Single-seed alpha points: seed_threshold=1, method agreement only\\n\\nDependencies: numpy, scipy, statsmodels\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport glob\\nimport json\\nimport os\\nimport re\\nimport sys\\nimport warnings\\nfrom datetime import datetime\\n\\nimport numpy as np\\nfrom statsmodels.stats.multitest import multipletests\\n\\nwarnings.filterwarnings(\\\"ignore\\\")\\n\\nBASE_DIR = os.path.dirname(os.path.abspath(__file__))\\nsys.path.insert(0, BASE_DIR)\\n\\nfrom method_ablation import (\\n    CANARY, DOWNSTREAM,\\n    extract as ma_extract,\\n    naive_pearson, diff_xcorr, threshold_lead, toda_yamamoto, perm_granger,\\n)\\nfrom consensus_framework import classify_robust, load_sig_matrix, NumpyEncoder\\n\\nSWEEP_DIR = os.path.join(BASE_DIR, \\\"results\\\", \\\"alpha_sweep\\\")\\nMVP_DIR = os.path.join(BASE_DIR, \\\"results\\\", \\\"mvp\\\")\\nANALYSIS_DIR = os.path.join(BASE_DIR, \\\"results\\\", \\\"analysis\\\")\\n\\nMETRICS = [\\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\", \\\"token_entropy\\\", \\\"ece\\\", \\\"perplexity\\\"]\\n\\nGRANGER_PAIRS = [\\n    (\\\"token_entropy\\\", \\\"distinct_1\\\", \\\"entropy->d1\\\"),\\n    (\\\"ece\\\",           \\\"distinct_1\\\", \\\"ECE->d1\\\"),\\n    (\\\"token_entropy\\\", \\\"distinct_2\\\", \\\"entropy->d2\\\"),\\n    (\\\"ece\\\",           \\\"distinct_2\\\", \\\"ECE->d2\\\"),\\n    (\\\"distinct_1\\\", \\\"token_entropy\\\", \\\"d1->entropy\\\"),\\n    (\\\"distinct_1\\\",
…[truncated 7442 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-15T11:43:27.409136+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "tail -n +639 /root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis_v4.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "tail -n +639 /root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis_v4.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-15T11:43:27.409444+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"def auto_version():\\n    os.makedirs(ANALYSIS_DIR, exist_ok=True)\\n    existing = glob.glob(os.path.join(ANALYSIS_DIR, \\\"cross_alpha_v*.json\\\"))\\n    max_v = 0\\n    for f in existing:\\n        m = re.search(r\\\"cross_alpha_v(\\\\d+)\\\", f)\\n        if m:\\n            max_v = max(max_v, int(m.group(1)))\\n    return max_v + 1\\n\\n\\ndef print_summary(output):\\n    print(\\\"\\\\n\\\" + \\\"=\\\" * 80)\\n    print(\\\"CROSS-ALPHA ANALYSIS SUMMARY (v4)\\\")\\n    print(\\\"=\\\" * 80)\\n\\n    dr = output[\\\"dose_response\\\"]\\n    alphas = sorted(dr.keys())\\n    print(f\\\"\\\\nDOSE-RESPONSE (drift %)\\\")\\n    print(\\\"-\\\" * 80)\\n    header = f\\\"{'Metric':<16}\\\"\\n    for ak in alphas:\\n        header += f\\\" | a={dr[ak]['alpha']:<5}\\\"\\n    print(header)\\n    print(\\\"-\\\" * 80)\\n    for metric in METRICS:\\n        line = f\\\"{metric:<16}\\\"\\n        for ak in alphas:\\n            d = dr[ak][metric][\\\"drift_pct\\\"]\\n            line += f\\\" | {d:>+7.1f}%\\\"\\n        print(line)\\n\\n    gc = output[\\\"granger_causality\\\"]\\n    print(f\\\"\\\\nGRANGER CAUSALITY (bidirectional, differenced, permutation)\\\")\\n    print(\\\"-\\\" * 80)\\n    header = f\\\"{'Direction':<20}\\\"\\n    alpha_keys = sorted(set(r[\\\"alpha_key\\\"] for r in gc))\\n    for ak in alpha_keys:\\n        header += f\\\" | a={[r for r in gc if r['alpha_key']==ak][0]['alpha']:<4} p_raw   p_fdr\\\"\\n    print(header)\\n    print(\\\"-\\\" * 80)\\n\\n    directions = list(dict.fromkeys(r[\\\"direction\\\"] for r in gc))\\n    for d in directions:\\n        line = f\\\"{d:<20}\\\"\\n        for ak in alpha_keys:\\n            match = [r for r in gc if r[\\\"alpha_key\\\"] == ak and r[\\\"direction\\\"] == d]\\n            if match:\\n                r = match[0]\\n                p_raw = f\\\"{r['p_raw']:.4f}\\\" if r.get(\\\"p_raw\\\") is not None else \\\"  N/A \\\"\\n                p_fdr =
…[truncated 7404 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-15T11:43:27.409663+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "tail -n +763 /root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis_v4.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "tail -n +763 /root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis_v4.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-15T11:43:27.409860+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"def main():\\n    parser = argparse.ArgumentParser(\\n        description=\\\"Cross-alpha analysis v4 with per-alpha consensus classification.\\\"\\n    )\\n    parser.add_argument(\\\"--alpha-dirs\\\", nargs=\\\"*\\\", default=None,\\n                        help=\\\"Specific alpha dirs (e.g. a000_s42 a025_s42 mvp). Default: auto-discover all.\\\")\\n    parser.add_argument(\\\"--n-perms\\\", type=int, default=5000,\\n                        help=\\\"Permutations for Granger test (default: 5000)\\\")\\n    parser.add_argument(\\\"--consensus-n-perms\\\", type=int, default=1000,\\n                        help=\\\"Permutations for consensus perm_granger method (default: 1000)\\\")\\n    parser.add_argument(\\\"--max-lag\\\", type=int, default=1,\\n                        help=\\\"Max lag for Granger test (default: 1)\\\")\\n    parser.add_argument(\\\"--no-mvp\\\", action=\\\"store_true\\\",\\n                        help=\\\"Exclude MVP (alpha=1.0) from auto-discovery\\\")\\n    parser.add_argument(\\\"--no-consensus\\\", action=\\\"store_true\\\",\\n                        help=\\\"Skip consensus classification (faster)\\\")\\n    parser.add_argument(\\\"--version\\\", type=int, default=None,\\n                        help=\\\"Output version number (default: auto-increment)\\\")\\n    parser.add_argument(\\\"--update-registry\\\", action=\\\"store_true\\\",\\n                        help=\\\"Print registry update commands after analysis\\\")\\n    args = parser.parse_args()\\n\\n    alpha_dirs = discover_alpha_dirs(args.alpha_dirs, include_mvp=not args.no_mvp)\\n    if not alpha_dirs:\\n        print(\\\"ERROR: No alpha directories found.\\\", file=sys.stderr)\\n        sys.exit(1)\\n\\n    print(f\\\"Found {len(alpha_dirs)} alpha points: \\\"\\n          f\\\"{[(a[0], f'seeds={a[3]}') for a in alpha_dirs]}\\\")\\n\\n    all_data = []\\n    for alpha_key, alpha_val, path, seeds in alpha_dirs:\\n        metrics
…[truncated 3637 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-15T11:43:27.410013+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "tail -n +508 /root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis_v4.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "tail -n +508 /root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis_v4.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-15T11:43:27.410286+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"def generate_markdown_report(output, out_path):\\n    lines = []\\n    lines.append(f\\\"# Cross-Alpha Analysis Report ({output['version']})\\\")\\n    lines.append(\\\"\\\")\\n    lines.append(f\\\"**Date:** {output['date']}\\\")\\n    lines.append(f\\\"**Alpha points:** {output['alpha_points']}\\\")\\n    lines.append(f\\\"**Generations:** {output['gen_range']}\\\")\\n    lines.append(\\\"\\\")\\n\\n    # 1. Dose-response\\n    lines.append(\\\"## 1. Dose-Response (gen0 to genN drift %)\\\")\\n    lines.append(\\\"\\\")\\n    dr = output[\\\"dose_response\\\"]\\n    alphas = sorted(dr.keys())\\n    header = \\\"| Metric |\\\"\\n    sep = \\\"|--------|\\\"\\n    for ak in alphas:\\n        header += f\\\" α={dr[ak]['alpha']:.2f} |\\\"\\n        sep += \\\"--------:|\\\"\\n    lines.append(header)\\n    lines.append(sep)\\n    for metric in METRICS:\\n        row = f\\\"| {metric} |\\\"\\n        for ak in alphas:\\n            d = dr[ak][metric][\\\"drift_pct\\\"]\\n            row += f\\\" {d:+.1f}% |\\\"\\n        lines.append(row)\\n    lines.append(\\\"\\\")\\n\\n    # 2. Granger\\n    lines.append(\\\"## 2. Granger Causality (bidirectional, permutation, FDR-corrected)\\\")\\n    lines.append(\\\"\\\")\\n    gc = output[\\\"granger_causality\\\"]\\n    ak_list = sorted(set(r[\\\"alpha_key\\\"] for r in gc))\\n    header = \\\"| Direction |\\\"\\n    sep = \\\"|-----------|\\\"\\n    for ak in ak_list:\\n        a = [r for r in gc if r[\\\"alpha_key\\\"] == ak][0][\\\"alpha\\\"]\\n        header += f\\\" α={a:.2f} p_raw | p_fdr |\\\"\\n        sep += \\\"--------:|--------:|\\\"\\n    lines.append(header)\\n    lines.append(sep)\\n    directions = list(dict.fromkeys(r[\\\"direction\\\"] for r in gc))\\n    for d in directions:\\n        row = f\\\"| {d} |\\\"\\n        for ak in ak_list:\\n            match = [r for r in gc if r[\\\"alpha_key\\\"] == ak and r[\\\"direction\\\"] == d]\\n            if match
…[truncated 7412 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-15T11:43:27.410482+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a075_s42/all_metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a075_s42/all_metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-15T11:43:27.410607+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/method_ablation.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/method_ablation.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-15T11:43:27.410737+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a075_s42/all_metrics.json': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-15T11:43:27.410864+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/method_ablation.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-15T11:43:27.410978+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a075_s42/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a075_s42/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-15T11:43:27.411092+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"config.json\\ngen_0\\ngen_1\\ngen_2\\ngen_3\\ngen_4\\ngen_5\\ngen_6\\ngen_7\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.54}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-15T11:43:27.411221+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/all_metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/all_metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-15T11:43:27.411355+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a075_s42/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a075_s42/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-15T11:43:27.411469+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/all_metrics.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-15T11:43:27.411579+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"config.json\\ngen_0\\ngen_1\\ngen_2\\ngen_3\\ngen_4\\ngen_5\\ngen_6\\ngen_7\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.59}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-15T11:43:27.411698+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-15T11:43:27.411812+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"EXIT_CODE\\nall_metrics.json\\nconfig.json\\ngen_0\\ngen_1\\ngen_10\\ngen_2\\ngen_3\\ngen_4\\ngen_5\\ngen_6\\ngen_7\\ngen_8\\ngen_9\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 59 · 2026-05-15T11:43:27.412000+00:00_

审计完成。以下是完整报告。

---

## 审计结果：✅ Ready（代码无 bug，等数据就绪即可运行）

### 1. FDR 混合策略 — ✅ 正确

**alpha=1.0 路径**（加载已有 method_ablation.json）：
- `consensus_framework.py:86-89`：`threshold_onset` 读 `significant`，其余 4 方法读 `significant_fdr`
- 完全符合 D029 要求

**非 alpha=1.0 路径**（从头跑 5 个方法）：
- `threshold_lead()` 只返回 `significant`（无 p_value）→ 直接写入 sig_matrix
- 其余 4 方法返回 `p_value` → 存入 `p_raw_matrix` → 经 BH FDR 校正后覆盖 sig_matrix
- FDR 循环只处理 `p_raw_matrix` 中有效值的位置 → threshold_onset 天然免于 FDR
- BH FDR q=0.05：`multipletests(pvals[valid], alpha=0.05, method="fdr_bh")` ✅

**permG / TY 列互换**：`MA_METHODS` 列表和 `MA_METHOD_FN` 字典映射一致，`enumerate` 遍历保证 method index 对应正确函数。✅ 无互换。

### 2. 5-α-point 兼容性 — ✅

- **α 列表不是硬编码**：`discover_alpha_dirs()` 用 `glob(a*_s42)` 动态发现 + 自动纳入 MVP(α=1.0)
- 数据目录现状：`a000_s42` ✅ / `a025_s42` ✅ / `a050_s42` ✅ / `a075_s42` ⚠️ / MVP ✅
- **`--n-perms 5000`**：已支持，default=5000 ✅
- **`--consensus-n-perms 1000`**：已支持，default=1000 ✅
- **`--update-registry`**：存在，打印每个 α 的 drift 统计 ✅
- **输出路径**：`results/analysis/cross_alpha_v{N}.json` + `cross_alpha_v{N}_report.md`

### 3. α=0.25 单 seed 处理 — ✅

Line ~450：`st = 1 if n_seeds == 1 else 3`
- 所有 sweep α 点（0.0, 0.25, 0.50, 0.75）均为 seed=[42]，n_seeds=1 → seed_threshold=1
- method_threshold = 4（≥4/5 方法一致）
- mode = `"method_agreement_only"` for single-seed

### 4. 输出格式 — ✅

- `print_summary`：Granger 表显示每个方向×每个 α 的 p_raw / p_fdr，汇总行 `N/M raw-sig -> K/M FDR-sig`
- Consensus 区：每个 α 的 robust/non-robust counts + regime comparison（stable vs regime-dependent）
- Markdown report 包含同样的信息以格式化表格呈现

### 5. ⚠️ 唯一阻塞：α=0.75 数据未完成

`a075_s42` 目录存在但只有 gen_0 到 gen_7（8/11 代），**无 `all_metrics.json`**。完整实验需 gen_0–gen_10。脚本会在 `load_metrics(a075_s42)` 时报 FileNotFoundError。

等实验完成 + 生成 `all_metrics.json` 后即可运行。

### 建议运行命令

```bash
cd /root/autodl-tmp/distrib_canary_collapse
python cross_alpha_analysis_v4.py --n-perms 5000 --consensus-n-perms 1000 --update-registry
```

无需指定 `--alpha-dirs`，auto-discovery 会自动找到全部 5 个 α 点。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_prep_cross_alpha_v4_audit_20260515T113914"
}
```

</details>

---
