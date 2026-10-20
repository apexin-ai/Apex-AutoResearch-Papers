# fix n500 pipeline d063 d064

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 51
- **Recorded user turns:** 0
- **Tool calls:** 25
- **Original source:** `logs/chats/worker_fix_n500_pipeline_d063_d064_20260515T045046.jsonl`
- **Structured JSON:** [`76c3c66bd2f5ea2b9c18.json`](../../sessions/76/76c3c66bd2f5ea2b9c18.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

51 recorded events

### Tool call

_source line 1 · 2026-05-15T04:54:38.052266+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T04:54:38.052653+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T04:54:38.052828+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "cat /root/autodl-tmp/pacs/analyze_n500_unified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "cat /root/autodl-tmp/pacs/analyze_n500_unified.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T04:54:38.053136+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nUnified n=500 analysis for phase-gated compound sparsity (PACS).\\n\\nAnalyses performed:\\n  1. Median II (low-high) + bootstrap 95% CI (B=10000, percentile method)\\n  2. Mid-phase null rate per condition\\n  3. Within-importance paired Cohen's d_z across sparsity levels (D059)\\n     - imp-vs-rand: Wilcoxon p + median_diff only, NO d_z\\n  4. Permutation monotonicity test across sparsity gradient\\n  5. Bonferroni correction on all reported p-values\\n\\nInput:  profiling_output_{n500_,}bf16_{ds,qw}_{imp,rand}_s{015..030}/profiling_results.json\\nOutput: analysis_output/n500_unified{_dryrun}.json\\n        analysis_output/n500_unified{_dryrun}.csv  (--csv)\\n        LaTeX table rows to stdout (--latex)\\n\\nConstraints:\\n  D054: median only, no mean\\n  D059: d_z within-importance only; imp-vs-rand gets Wilcoxon + median_diff\\n\\\"\\\"\\\"\\n\\nimport json\\nimport argparse\\nimport sys\\nfrom pathlib import Path\\nfrom typing import Optional, List, Dict, Tuple, Any\\n\\nimport numpy as np\\nfrom scipy import stats\\n\\nBASE = Path(\\\"/root/autodl-tmp/pacs\\\")\\n\\nMODEL_MAP = {\\\"deepseek\\\": \\\"ds\\\", \\\"qwen\\\": \\\"qw\\\"}\\nMASKING_TYPES = [\\\"imp\\\", \\\"rand\\\"]\\nSPARSITY_LABELS = [\\\"s015\\\", \\\"s020\\\", \\\"s025\\\", \\\"s030\\\"]\\nSPARSITY_VALUES = {\\\"s015\\\": 0.15, \\\"s020\\\": 0.20, \\\"s025\\\": 0.25, \\\"s030\\\": 0.30}\\nSPARSITY_KEY_MAP = {\\\"s015\\\": \\\"0.15\\\", \\\"s020\\\": \\\"0.2\\\", \\\"s025\\\": \\\"0.25\\\", \\\"s030\\\": \\\"0.3\\\"}\\n\\nWITHIN_IMP_PAIRS = [\\n    (\\\"s015\\\", \\\"s020\\\"),\\n    (\\\"s020\\\", \\\"s025\\\"),\\n    (\\\"s025\\\", \\\"s030\\\"),\\n    (\\\"s015\\\", \\\"s030\\\"),\\n]\\n\\nB_BOOT = 10000\\nSEED = 42\\nALPHA = 0.05\\nN_PERM = 5000\\n\\n\\n# ── Path / IO ────────────────────────────────────────────────────────\\n\\ndef dir_name(model_short: str, masking: str, slabel: str, n500: bool = True) -> str:\\n    pr
…[truncated 7402 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T04:54:38.053344+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "wc -l /root/autodl-tmp/pacs/analyze_n500_unified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "wc -l /root/autodl-tmp/pacs/analyze_n500_unified.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T04:54:38.053511+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"676 /root/autodl-tmp/pacs/analyze_n500_unified.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T04:54:38.053651+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "head -200 /root/autodl-tmp/pacs/analyze_n500_unified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "head -200 /root/autodl-tmp/pacs/analyze_n500_unified.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T04:54:38.053907+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nUnified n=500 analysis for phase-gated compound sparsity (PACS).\\n\\nAnalyses performed:\\n  1. Median II (low-high) + bootstrap 95% CI (B=10000, percentile method)\\n  2. Mid-phase null rate per condition\\n  3. Within-importance paired Cohen's d_z across sparsity levels (D059)\\n     - imp-vs-rand: Wilcoxon p + median_diff only, NO d_z\\n  4. Permutation monotonicity test across sparsity gradient\\n  5. Bonferroni correction on all reported p-values\\n\\nInput:  profiling_output_{n500_,}bf16_{ds,qw}_{imp,rand}_s{015..030}/profiling_results.json\\nOutput: analysis_output/n500_unified{_dryrun}.json\\n        analysis_output/n500_unified{_dryrun}.csv  (--csv)\\n        LaTeX table rows to stdout (--latex)\\n\\nConstraints:\\n  D054: median only, no mean\\n  D059: d_z within-importance only; imp-vs-rand gets Wilcoxon + median_diff\\n\\\"\\\"\\\"\\n\\nimport json\\nimport argparse\\nimport sys\\nfrom pathlib import Path\\nfrom typing import Optional, List, Dict, Tuple, Any\\n\\nimport numpy as np\\nfrom scipy import stats\\n\\nBASE = Path(\\\"/root/autodl-tmp/pacs\\\")\\n\\nMODEL_MAP = {\\\"deepseek\\\": \\\"ds\\\", \\\"qwen\\\": \\\"qw\\\"}\\nMASKING_TYPES = [\\\"imp\\\", \\\"rand\\\"]\\nSPARSITY_LABELS = [\\\"s015\\\", \\\"s020\\\", \\\"s025\\\", \\\"s030\\\"]\\nSPARSITY_VALUES = {\\\"s015\\\": 0.15, \\\"s020\\\": 0.20, \\\"s025\\\": 0.25, \\\"s030\\\": 0.30}\\nSPARSITY_KEY_MAP = {\\\"s015\\\": \\\"0.15\\\", \\\"s020\\\": \\\"0.2\\\", \\\"s025\\\": \\\"0.25\\\", \\\"s030\\\": \\\"0.3\\\"}\\n\\nWITHIN_IMP_PAIRS = [\\n    (\\\"s015\\\", \\\"s020\\\"),\\n    (\\\"s020\\\", \\\"s025\\\"),\\n    (\\\"s025\\\", \\\"s030\\\"),\\n    (\\\"s015\\\", \\\"s030\\\"),\\n]\\n\\nB_BOOT = 10000\\nSEED = 42\\nALPHA = 0.05\\nN_PERM = 5000\\n\\n\\n# ── Path / IO ────────────────────────────────────────────────────────\\n\\ndef dir_name(model_short: str, masking: str, slabel: str, n500: bool = True) -> str:\\n    pr
…[truncated 5585 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T04:54:38.054068+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "head -400 /root/autodl-tmp/pacs/analyze_n500_unified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "head -400 /root/autodl-tmp/pacs/analyze_n500_unified.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T04:54:38.054341+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nUnified n=500 analysis for phase-gated compound sparsity (PACS).\\n\\nAnalyses performed:\\n  1. Median II (low-high) + bootstrap 95% CI (B=10000, percentile method)\\n  2. Mid-phase null rate per condition\\n  3. Within-importance paired Cohen's d_z across sparsity levels (D059)\\n     - imp-vs-rand: Wilcoxon p + median_diff only, NO d_z\\n  4. Permutation monotonicity test across sparsity gradient\\n  5. Bonferroni correction on all reported p-values\\n\\nInput:  profiling_output_{n500_,}bf16_{ds,qw}_{imp,rand}_s{015..030}/profiling_results.json\\nOutput: analysis_output/n500_unified{_dryrun}.json\\n        analysis_output/n500_unified{_dryrun}.csv  (--csv)\\n        LaTeX table rows to stdout (--latex)\\n\\nConstraints:\\n  D054: median only, no mean\\n  D059: d_z within-importance only; imp-vs-rand gets Wilcoxon + median_diff\\n\\\"\\\"\\\"\\n\\nimport json\\nimport argparse\\nimport sys\\nfrom pathlib import Path\\nfrom typing import Optional, List, Dict, Tuple, Any\\n\\nimport numpy as np\\nfrom scipy import stats\\n\\nBASE = Path(\\\"/root/autodl-tmp/pacs\\\")\\n\\nMODEL_MAP = {\\\"deepseek\\\": \\\"ds\\\", \\\"qwen\\\": \\\"qw\\\"}\\nMASKING_TYPES = [\\\"imp\\\", \\\"rand\\\"]\\nSPARSITY_LABELS = [\\\"s015\\\", \\\"s020\\\", \\\"s025\\\", \\\"s030\\\"]\\nSPARSITY_VALUES = {\\\"s015\\\": 0.15, \\\"s020\\\": 0.20, \\\"s025\\\": 0.25, \\\"s030\\\": 0.30}\\nSPARSITY_KEY_MAP = {\\\"s015\\\": \\\"0.15\\\", \\\"s020\\\": \\\"0.2\\\", \\\"s025\\\": \\\"0.25\\\", \\\"s030\\\": \\\"0.3\\\"}\\n\\nWITHIN_IMP_PAIRS = [\\n    (\\\"s015\\\", \\\"s020\\\"),\\n    (\\\"s020\\\", \\\"s025\\\"),\\n    (\\\"s025\\\", \\\"s030\\\"),\\n    (\\\"s015\\\", \\\"s030\\\"),\\n]\\n\\nB_BOOT = 10000\\nSEED = 42\\nALPHA = 0.05\\nN_PERM = 5000\\n\\n\\n# ── Path / IO ────────────────────────────────────────────────────────\\n\\ndef dir_name(model_short: str, masking: str, slabel: str, n500: bool = True) -> str:\\n    pr
…[truncated 7361 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T04:54:38.054532+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "tail -n +380 /root/autodl-tmp/pacs/analyze_n500_unified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "tail -n +380 /root/autodl-tmp/pacs/analyze_n500_unified.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T04:54:38.054824+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"        if \\\"wilcoxon_p\\\" in v:\\n            p_registry.append((\\\"imp_vs_rand\\\", sl, \\\"wilcoxon_p\\\"))\\n            all_p_values.append(v[\\\"wilcoxon_p\\\"])\\n\\n    n_tests = len(all_p_values)\\n\\n    for i, (category, key, field) in enumerate(p_registry):\\n        raw_p = all_p_values[i]\\n        corrected = bonferroni(raw_p, n_tests)\\n        if category == \\\"condition\\\":\\n            cond_out[key][\\\"bonferroni_p\\\"] = corrected\\n            cond_out[key][\\\"n_tests_bonferroni\\\"] = n_tests\\n        elif category == \\\"dz_imp\\\":\\n            dz_importance[key][\\\"bonferroni_p\\\"] = corrected\\n        elif category == \\\"rand_within\\\":\\n            rand_comparisons[key][\\\"bonferroni_p\\\"] = corrected\\n        elif category == \\\"imp_vs_rand\\\":\\n            imp_vs_rand[key][\\\"bonferroni_p\\\"] = corrected\\n\\n    return {\\n        \\\"conditions\\\": cond_out,\\n        \\\"within_dz_importance\\\": dz_importance,\\n        \\\"within_rand_comparisons\\\": rand_comparisons,\\n        \\\"imp_vs_rand\\\": imp_vs_rand,\\n        \\\"dose_response\\\": {\\n            \\\"importance\\\": dose_imp,\\n            \\\"random\\\": dose_rand,\\n        },\\n        \\\"bonferroni_n_tests\\\": n_tests,\\n        \\\"available_conditions\\\": available,\\n    }\\n\\n\\n# ── LaTeX output ──────────────────────────────────────────────────────\\n\\ndef fmt(v: float, decimals: int = 4) -> str:\\n    return f\\\"{v:.{decimals}f}\\\"\\n\\n\\ndef fmt_p(p: float) -> str:\\n    if p < 0.001:\\n        return \\\"$<$0.001\\\"\\n    return f\\\"{p:.3f}\\\"\\n\\n\\ndef latex_output(full_output: dict):\\n    print(\\\"\\\\n\\\" + \\\"=\\\" * 70)\\n    print(\\\"LATEX TABLE ROWS\\\")\\n    print(\\\"=\\\" * 70)\\n\\n    # Table 1: Per-condition median II diff + CI\\n    print(\\\"\\\\n% Table: Median II (low-high) by condition\\\")\\n    print(\\\"% Model & Masking & Sparsity & n 
…[truncated 7519 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T04:54:38.055024+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "head -550 /root/autodl-tmp/pacs/analyze_n500_unified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "head -550 /root/autodl-tmp/pacs/analyze_n500_unified.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T04:54:38.055305+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nUnified n=500 analysis for phase-gated compound sparsity (PACS).\\n\\nAnalyses performed:\\n  1. Median II (low-high) + bootstrap 95% CI (B=10000, percentile method)\\n  2. Mid-phase null rate per condition\\n  3. Within-importance paired Cohen's d_z across sparsity levels (D059)\\n     - imp-vs-rand: Wilcoxon p + median_diff only, NO d_z\\n  4. Permutation monotonicity test across sparsity gradient\\n  5. Bonferroni correction on all reported p-values\\n\\nInput:  profiling_output_{n500_,}bf16_{ds,qw}_{imp,rand}_s{015..030}/profiling_results.json\\nOutput: analysis_output/n500_unified{_dryrun}.json\\n        analysis_output/n500_unified{_dryrun}.csv  (--csv)\\n        LaTeX table rows to stdout (--latex)\\n\\nConstraints:\\n  D054: median only, no mean\\n  D059: d_z within-importance only; imp-vs-rand gets Wilcoxon + median_diff\\n\\\"\\\"\\\"\\n\\nimport json\\nimport argparse\\nimport sys\\nfrom pathlib import Path\\nfrom typing import Optional, List, Dict, Tuple, Any\\n\\nimport numpy as np\\nfrom scipy import stats\\n\\nBASE = Path(\\\"/root/autodl-tmp/pacs\\\")\\n\\nMODEL_MAP = {\\\"deepseek\\\": \\\"ds\\\", \\\"qwen\\\": \\\"qw\\\"}\\nMASKING_TYPES = [\\\"imp\\\", \\\"rand\\\"]\\nSPARSITY_LABELS = [\\\"s015\\\", \\\"s020\\\", \\\"s025\\\", \\\"s030\\\"]\\nSPARSITY_VALUES = {\\\"s015\\\": 0.15, \\\"s020\\\": 0.20, \\\"s025\\\": 0.25, \\\"s030\\\": 0.30}\\nSPARSITY_KEY_MAP = {\\\"s015\\\": \\\"0.15\\\", \\\"s020\\\": \\\"0.2\\\", \\\"s025\\\": \\\"0.25\\\", \\\"s030\\\": \\\"0.3\\\"}\\n\\nWITHIN_IMP_PAIRS = [\\n    (\\\"s015\\\", \\\"s020\\\"),\\n    (\\\"s020\\\", \\\"s025\\\"),\\n    (\\\"s025\\\", \\\"s030\\\"),\\n    (\\\"s015\\\", \\\"s030\\\"),\\n]\\n\\nB_BOOT = 10000\\nSEED = 42\\nALPHA = 0.05\\nN_PERM = 5000\\n\\n\\n# ── Path / IO ────────────────────────────────────────────────────────\\n\\ndef dir_name(model_short: str, masking: str, slabel: str, n500: bool = True) -> str:\\n    pr
…[truncated 7429 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T04:54:38.055509+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "head -380 /root/autodl-tmp/pacs/analyze_n500_unified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "head -380 /root/autodl-tmp/pacs/analyze_n500_unified.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T04:54:38.055807+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nUnified n=500 analysis for phase-gated compound sparsity (PACS).\\n\\nAnalyses performed:\\n  1. Median II (low-high) + bootstrap 95% CI (B=10000, percentile method)\\n  2. Mid-phase null rate per condition\\n  3. Within-importance paired Cohen's d_z across sparsity levels (D059)\\n     - imp-vs-rand: Wilcoxon p + median_diff only, NO d_z\\n  4. Permutation monotonicity test across sparsity gradient\\n  5. Bonferroni correction on all reported p-values\\n\\nInput:  profiling_output_{n500_,}bf16_{ds,qw}_{imp,rand}_s{015..030}/profiling_results.json\\nOutput: analysis_output/n500_unified{_dryrun}.json\\n        analysis_output/n500_unified{_dryrun}.csv  (--csv)\\n        LaTeX table rows to stdout (--latex)\\n\\nConstraints:\\n  D054: median only, no mean\\n  D059: d_z within-importance only; imp-vs-rand gets Wilcoxon + median_diff\\n\\\"\\\"\\\"\\n\\nimport json\\nimport argparse\\nimport sys\\nfrom pathlib import Path\\nfrom typing import Optional, List, Dict, Tuple, Any\\n\\nimport numpy as np\\nfrom scipy import stats\\n\\nBASE = Path(\\\"/root/autodl-tmp/pacs\\\")\\n\\nMODEL_MAP = {\\\"deepseek\\\": \\\"ds\\\", \\\"qwen\\\": \\\"qw\\\"}\\nMASKING_TYPES = [\\\"imp\\\", \\\"rand\\\"]\\nSPARSITY_LABELS = [\\\"s015\\\", \\\"s020\\\", \\\"s025\\\", \\\"s030\\\"]\\nSPARSITY_VALUES = {\\\"s015\\\": 0.15, \\\"s020\\\": 0.20, \\\"s025\\\": 0.25, \\\"s030\\\": 0.30}\\nSPARSITY_KEY_MAP = {\\\"s015\\\": \\\"0.15\\\", \\\"s020\\\": \\\"0.2\\\", \\\"s025\\\": \\\"0.25\\\", \\\"s030\\\": \\\"0.3\\\"}\\n\\nWITHIN_IMP_PAIRS = [\\n    (\\\"s015\\\", \\\"s020\\\"),\\n    (\\\"s020\\\", \\\"s025\\\"),\\n    (\\\"s025\\\", \\\"s030\\\"),\\n    (\\\"s015\\\", \\\"s030\\\"),\\n]\\n\\nB_BOOT = 10000\\nSEED = 42\\nALPHA = 0.05\\nN_PERM = 5000\\n\\n\\n# ── Path / IO ────────────────────────────────────────────────────────\\n\\ndef dir_name(model_short: str, masking: str, slabel: str, n500: bool = True) -> str:\\n    pr
…[truncated 7343 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T04:54:38.056009+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "head -300 /root/autodl-tmp/pacs/analyze_n500_unified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "head -300 /root/autodl-tmp/pacs/analyze_n500_unified.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T04:54:38.056285+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nUnified n=500 analysis for phase-gated compound sparsity (PACS).\\n\\nAnalyses performed:\\n  1. Median II (low-high) + bootstrap 95% CI (B=10000, percentile method)\\n  2. Mid-phase null rate per condition\\n  3. Within-importance paired Cohen's d_z across sparsity levels (D059)\\n     - imp-vs-rand: Wilcoxon p + median_diff only, NO d_z\\n  4. Permutation monotonicity test across sparsity gradient\\n  5. Bonferroni correction on all reported p-values\\n\\nInput:  profiling_output_{n500_,}bf16_{ds,qw}_{imp,rand}_s{015..030}/profiling_results.json\\nOutput: analysis_output/n500_unified{_dryrun}.json\\n        analysis_output/n500_unified{_dryrun}.csv  (--csv)\\n        LaTeX table rows to stdout (--latex)\\n\\nConstraints:\\n  D054: median only, no mean\\n  D059: d_z within-importance only; imp-vs-rand gets Wilcoxon + median_diff\\n\\\"\\\"\\\"\\n\\nimport json\\nimport argparse\\nimport sys\\nfrom pathlib import Path\\nfrom typing import Optional, List, Dict, Tuple, Any\\n\\nimport numpy as np\\nfrom scipy import stats\\n\\nBASE = Path(\\\"/root/autodl-tmp/pacs\\\")\\n\\nMODEL_MAP = {\\\"deepseek\\\": \\\"ds\\\", \\\"qwen\\\": \\\"qw\\\"}\\nMASKING_TYPES = [\\\"imp\\\", \\\"rand\\\"]\\nSPARSITY_LABELS = [\\\"s015\\\", \\\"s020\\\", \\\"s025\\\", \\\"s030\\\"]\\nSPARSITY_VALUES = {\\\"s015\\\": 0.15, \\\"s020\\\": 0.20, \\\"s025\\\": 0.25, \\\"s030\\\": 0.30}\\nSPARSITY_KEY_MAP = {\\\"s015\\\": \\\"0.15\\\", \\\"s020\\\": \\\"0.2\\\", \\\"s025\\\": \\\"0.25\\\", \\\"s030\\\": \\\"0.3\\\"}\\n\\nWITHIN_IMP_PAIRS = [\\n    (\\\"s015\\\", \\\"s020\\\"),\\n    (\\\"s020\\\", \\\"s025\\\"),\\n    (\\\"s025\\\", \\\"s030\\\"),\\n    (\\\"s015\\\", \\\"s030\\\"),\\n]\\n\\nB_BOOT = 10000\\nSEED = 42\\nALPHA = 0.05\\nN_PERM = 5000\\n\\n\\n# ── Path / IO ────────────────────────────────────────────────────────\\n\\ndef dir_name(model_short: str, masking: str, slabel: str, n500: bool = True) -> str:\\n    pr
…[truncated 7319 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T04:54:38.056502+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "grep -n -i \"FAIL\\|PASS\\|fail\\|pass\" /root/autodl-tmp/pacs/analyze_n500_unified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "grep -n -i \"FAIL\\|PASS\\|fail\\|pass\" /root/autodl-tmp/pacs/analyze_n500_unified.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T04:54:38.056640+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T04:54:38.056766+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "grep -n -iE \"FAIL|PASS\" /root/autodl-tmp/pacs/analyze_n500_unified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "grep -n -iE \"FAIL|PASS\" /root/autodl-tmp/pacs/analyze_n500_unified.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T04:54:38.056888+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T04:54:38.057014+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "grep -n \"FAIL\" /root/autodl-tmp/pacs/analyze_n500_unified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "grep -n \"FAIL\" /root/autodl-tmp/pacs/analyze_n500_unified.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T04:54:38.057136+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T04:54:38.057251+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "grep -n \"PASS\" /root/autodl-tmp/pacs/analyze_n500_unified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "grep -n \"PASS\" /root/autodl-tmp/pacs/analyze_n500_unified.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T04:54:38.057369+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T04:54:38.057506+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "grep -n \"ci_excludes_zero\" /root/autodl-tmp/pacs/analyze_n500_unified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "grep -n \"ci_excludes_zero\" /root/autodl-tmp/pacs/analyze_n500_unified.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T04:54:38.057634+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"228:        \\\"ci_excludes_zero\\\": not crosses_zero,\\n632:                    \\\"ci_excludes_zero,wilcoxon_p,bonferroni_p,mid_null_rate\\\\n\\\")\\n643:                            f\\\"{c['ci_excludes_zero']},{c['wilcoxon_p']},\\\"\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T04:54:38.057794+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "head -170 /root/autodl-tmp/pacs/analyze_n500_unified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "head -170 /root/autodl-tmp/pacs/analyze_n500_unified.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T04:54:38.058030+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nUnified n=500 analysis for phase-gated compound sparsity (PACS).\\n\\nAnalyses performed:\\n  1. Median II (low-high) + bootstrap 95% CI (B=10000, percentile method)\\n  2. Mid-phase null rate per condition\\n  3. Within-importance paired Cohen's d_z across sparsity levels (D059)\\n     - imp-vs-rand: Wilcoxon p + median_diff only, NO d_z\\n  4. Permutation monotonicity test across sparsity gradient\\n  5. Bonferroni correction on all reported p-values\\n\\nInput:  profiling_output_{n500_,}bf16_{ds,qw}_{imp,rand}_s{015..030}/profiling_results.json\\nOutput: analysis_output/n500_unified{_dryrun}.json\\n        analysis_output/n500_unified{_dryrun}.csv  (--csv)\\n        LaTeX table rows to stdout (--latex)\\n\\nConstraints:\\n  D054: median only, no mean\\n  D059: d_z within-importance only; imp-vs-rand gets Wilcoxon + median_diff\\n\\\"\\\"\\\"\\n\\nimport json\\nimport argparse\\nimport sys\\nfrom pathlib import Path\\nfrom typing import Optional, List, Dict, Tuple, Any\\n\\nimport numpy as np\\nfrom scipy import stats\\n\\nBASE = Path(\\\"/root/autodl-tmp/pacs\\\")\\n\\nMODEL_MAP = {\\\"deepseek\\\": \\\"ds\\\", \\\"qwen\\\": \\\"qw\\\"}\\nMASKING_TYPES = [\\\"imp\\\", \\\"rand\\\"]\\nSPARSITY_LABELS = [\\\"s015\\\", \\\"s020\\\", \\\"s025\\\", \\\"s030\\\"]\\nSPARSITY_VALUES = {\\\"s015\\\": 0.15, \\\"s020\\\": 0.20, \\\"s025\\\": 0.25, \\\"s030\\\": 0.30}\\nSPARSITY_KEY_MAP = {\\\"s015\\\": \\\"0.15\\\", \\\"s020\\\": \\\"0.2\\\", \\\"s025\\\": \\\"0.25\\\", \\\"s030\\\": \\\"0.3\\\"}\\n\\nWITHIN_IMP_PAIRS = [\\n    (\\\"s015\\\", \\\"s020\\\"),\\n    (\\\"s020\\\", \\\"s025\\\"),\\n    (\\\"s025\\\", \\\"s030\\\"),\\n    (\\\"s015\\\", \\\"s030\\\"),\\n]\\n\\nB_BOOT = 10000\\nSEED = 42\\nALPHA = 0.05\\nN_PERM = 5000\\n\\n\\n# ── Path / IO ────────────────────────────────────────────────────────\\n\\ndef dir_name(model_short: str, masking: str, slabel: str, n500: bool = True) -> str:\\n    pr
…[truncated 4526 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T04:54:38.058217+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "grep -n \"verdict\\|result\\|status\\|label\\|sig\" /root/autodl-tmp/pacs/analyze_n500_unified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "grep -n \"verdict\\|result\\|status\\|label\\|sig\" /root/autodl-tmp/pacs/analyze_n500_unified.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T04:54:38.058589+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T04:54:38.058744+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-22162",
  "command": "cd /root/autodl-tmp/pacs && cp analyze_n500_unified.py analyze_n500_unified.py.bak",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-22162",
    "command": "cd /root/autodl-tmp/pacs && cp analyze_n500_unified.py analyze_n500_unified.py.bak",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T04:54:38.058874+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T04:54:38.059080+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-22162",
  "command": "cat > /root/autodl-tmp/pacs/_patch_d063_d064.py << 'PYEOF'\nimport re\n\nfilepath = \"/root/autodl-tmp/pacs/analyze_n500_unified.py\"\nwith open(filepath, \"r\") as f:\n    code = f.read()\n\n# ============================================================\n# 1. Update docstring: add D063/D064 constraints\n# ============================================================\nold_constraints = \"\"\"Constraints:\n  D054: median only, no mean\n  D059: d_z within-importance only; imp-vs-rand gets Wilcoxon + median_diff\"\"\"\n\nnew_constraints = \"\"\"Constraints:\n  D054: median only, no mean\n  D059: d_z within-importance only; imp-vs-rand gets Wilcoxon + median_diff\n  D063: random conditions report values + significance, no FAIL/PASS\n  D064: d_z auxiliary with reliability flag; rank-biserial correlation added\"\"\"\n\ncode = code.replace(old_constraints, new_constraints)\n\n# ============================================================\n# 2. Add new helper functions after interpret_d()\n# ============================================================\nafter_interpret_d = '''def interpret_d(d: float) -> str:\n    ad = abs(d)\n    if ad < 0.2:\n        return \"negligible\"\n    elif ad < 0.5:\n        return \"small\"\n    elif ad < 0.8:\n        return \"medium\"\n    return \"large\"'''\n\nnew_helpers = after_interpret_d + '''\n\n\ndef sig_stars(p: float) -> str:\n    if p < 0.001:\n        return \"***\"\n    if p < 0.01:\n        return \"**\"\n    if p < 0.05:\n        return \"*\"\n    return \"ns\"\n\n\ndef matched_pairs_rank_biserial(diffs: np.ndarray) -> float:\n    nonzero = diffs[diffs != 0]\n    n = len(nonzero)\n    if n < 2:\n        return float(\"nan\")\n    ranks = stats.rankdata(np.abs(nonzero))\n    w_plus = float(np.sum(ranks[nonzero > 0]))\n    w_minus = float(np.sum(ranks[nonzero < 0]))\n    denom = n * (n + 1) / 2.0\n    return float((w_plus - w_minus) / denom)\n\n\ndef dz_is_reliable(dz_ci: list, slabel_a: str, slabel_b: str) -> bool:\n    ci_lo, ci_hi = dz_ci\n    if any(np.isnan(x) for x in [ci_lo, ci_hi]):\n        return False\n    ci_width = ci_hi - ci_lo\n    if ci_width > 0.5:\n        return False\n    high_sparsity = slabel_a in (\"s025\", \"s030\") or slabel_b in (\"s025\", \"s030\")\n    if high_sparsity:\n        mid = (ci_lo + ci_hi) / 2.0\n        upper = ci_hi - mid\n        lower = mid - ci_lo\n        if lower > 0 and upper / lower > 3.0:\n            return False\n        if upper > 0 and lower / upper > 3.0:\n            return False\n    return True'''\n\ncode = code.replace(after_interpret_d, new_helpers)\n\n# ============================================================\n# 3. Add sig_stars to analyze_condition output\n# ============================================================\nold_condition_return = \"\"\"    return {\n        \"n_valid\": n_valid,\n        \"median_ii_diff\": med,\n        \"median_ii_diff_ci\": [ci_lo, ci_hi],\n        \"ci_excludes_zero\": not crosses_zero,\n        \"wilcoxon_stat\": float(wilcoxon_stat),\n        \"wilcoxon_p\": float(wilcoxon_p),\n        \"per_phase_median\": per_phase,\n        \"midphase_null\": null_info,\n    }\"\"\"\n\nnew_condition_return = \"\"\"    p_val = float(wilcoxon_p)\n    return {\n        \"n_valid\": n_valid,\n        \"median_ii_diff\": med,\n        \"median_ii_diff_ci\": [ci_lo, ci_hi],\n        \"ci_excludes_zero\": not crosses_zero,\n        \"significance\": sig_stars(p_val),\n        \"wilcoxon_stat\": float(wilcoxon_stat),\n        \"wilcoxon_p\": p_val,\n        \"per_phase_median\": per_phase,\n        \"midphase_null\": null_info,\n    }\"\"\"\n\ncode = code.replace(old_condition_return, new_condition_return)\n\n# ============================================================\n# 4. Add dz_reliable + rank_biserial to within-importance d_z\n# ============================================================\nold_dz_block = \"\"\"        dz_importance[pair_key] = {\n            \"d_z\": dz,\n            \"d_z_ci\": list(dz_ci),\n            \"interpretation\": interpret_d(dz),\n            \"n_paired\": n_paired,\n            \"median_diff\": float(np.median(paired_diffs)),\n            \"wilcoxon_stat\": float(w_stat),\n            \"wilcoxon_p\": float(w_p),\n        }\"\"\"\n\nnew_dz_block = \"\"\"        dz_ci_list = list(dz_ci)\n        r_rb = matched_pairs_rank_biserial(paired_diffs)\n        dz_importance[pair_key] = {\n            \"d_z\": dz,\n            \"d_z_ci\": dz_ci_list,\n            \"dz_reliable\": dz_is_reliable(dz_ci_list, sl_a, sl_b),\n            \"interpretation\": interpret_d(dz),\n            \"rank_biserial_r\": r_rb,\n            \"n_paired\": n_paired,\n            \"median_diff\": float(np.median(paired_diffs)),\n            \"wilcoxon_stat\": float(w_stat),\n            \"wilcoxon_p\": float(w_p),\n        }\"\"\"\n\ncode = code.replace(old_dz_block, new_dz_block)\n\n# ============================================================\n# 5. Add rank_biserial to imp_vs_rand\n# ============================================================\nold_ivr = \"\"\"        imp_vs_rand[sl] = {\n            \"median_diff\": float(np.median(paired_diffs)),\n            \"wilcoxon_stat\": float(w_stat),\n            \"wilcoxon_p\": float(w_p),\n            \"n_paired\": n_paired,\n        }\n\n    # 5. Permutation monotonicity test\"\"\"\n\nnew_ivr = \"\"\"        r_rb_ivr = matched_pairs_rank_biserial(paired_diffs)\n        imp_vs_rand[sl] = {\n            \"median_diff\": float(np.median(paired_diffs)),\n            \"rank_biserial_r\": r_rb_ivr,\n            \"wilcoxon_stat\": float(w_stat),\n            \"wilcoxon_p\": float(w_p),\n            \"n_paired\": n_paired,\n        }\n\n    # 5. Permutation monotonicity test\"\"\"\n\ncode = code.replace(old_ivr, new_ivr)\n\n# ============================================================\n# 6. Update LaTeX Table 1: add significance column, no FAIL/PASS\n# ============================================================\nold_latex_t1_header = \"\"\"    print(\"\\\\n% Table: Median II (low-high) by condition\")\n    print(\"% Model & Masking & Sparsity & n & Median & CI_low & CI_high & p & p_bonf \\\\\\\\\\\\\\\\\")\"\"\"\n\nnew_latex_t1_header = \"\"\"    print(\"\\\\n% Table: Median II (low-high) by condition\")\n    print(\"% Model & Masking & Sparsity & n & Median & CI_low & CI_high & p & p_bonf & sig \\\\\\\\\\\\\\\\\")\"\"\"\n\ncode = code.replace(old_latex_t1_header, new_latex_t1_header)\n\nold_latex_t1_row = '''                print(f\"{m_name.capitalize()} & {mask_label} & {s_val:.0%} & \"\n                      f\"{c['n_valid']} & {fmt(c['median_ii_diff'])} & \"\n                      f\"{fmt(ci[0])} & {fmt(ci[1])} & \"\n                      f\"{fmt_p(p_raw)} & {fmt_p(p_bonf)} \\\\\\\\\\\\\\\\\")'''\n\nnew_latex_t1_row = '''                sig = c.get(\"significance\", \"\")\n                print(f\"{m_name.capitalize()} & {mask_label} & {s_val:.0%} & \"\n                      f\"{c['n_valid']} & {fmt(c['median_ii_diff'])} & \"\n                      f\"{fmt(ci[0])} & {fmt(ci[1])} & \"\n                      f\"{fmt_p(p_raw)} & {fmt_p(p_bonf)} & {sig} \\\\\\\\\\\\\\\\\")'''\n\ncode = code.replace(old_latex_t1_row, new_latex_t1_row)\n\n# ============================================================\n# 7. Update LaTeX Table 3 (within-importance d_z): add † for unreliable\n# ============================================================\nold_latex_t3_header = \"\"\"    print(\"\\\\n% Table: Within-importance paired d_z (D059)\")\n    print(\"% Model & Pair & d_z & CI_low & CI_high & Interp & p & p_bonf \\\\\\\\\\\\\\\\\")\"\"\"\n\nnew_latex_t3_header = \"\"\"    print(\"\\\\n% Table: Within-importance paired d_z (D059, D064)\")\n    print(\"% Model & Pair & d_z & CI_low & CI_high & Interp & r_rb & p & p_bonf \\\\\\\\\\\\\\\\\")\"\"\"\n\ncode = code.replace(old_latex_t3_header, new_latex_t3_header)\n\nold_latex_t3_row = '''            p_bonf = v.get(\"bonferroni_p\", v[\"wilcoxon_p\"])\n            print(f\"{m_name.capitalize()} & {pair_key} & \"\n                  f\"{fmt(v['d_z'])} & {fmt(v['d_z_ci'][0])} & {fmt(v['d_z_ci'][1])} & \"\n                  f\"{v['interpretation']} & {fmt_p(v['wilcoxon_p'])} & {fmt_p(p_bonf)} \\\\\\\\\\\\\\\\\")'''\n\nnew_latex_t3_row = '''            p_bonf = v.get(\"bonferroni_p\", v[\"wilcoxon_p\"])\n            dz_str = fmt(v['d_z'])\n            if not v.get('dz_reliable', True):\n                dz_str += \"$\\\\\\\\dagger$\"\n            r_rb_str = fmt(v.get('rank_biserial_r', float('nan')))\n            print(f\"{m_name.capitalize()} & {pair_key} & \"\n                  f\"{dz_str} & {fmt(v['d_z_ci'][0])} & {fmt(v['d_z_ci'][1])} & \"\n                  f\"{v['interpretation']} & {r_rb_str} & {fmt_p(v['wilcoxon_p'])} & {fmt_p(p_bonf)} \\\\\\\\\\\\\\\\\")'''\n\ncode = code.replace(old_latex_t3_row, new_latex_t3_row)\n\n# ============================================================\n# 8. Update CSV header for conditions: add significance column\n# ============================================================\nold_csv_header = '''            f.write(\"model,masking,sparsity,n,median_ii_diff,ci_lo,ci_hi,\"\n                    \"ci_excludes_zero,wilcoxon_p,bonferroni_p,mid_null_rate\\\\n\")'''\n\nnew_csv_header = '''            f.write(\"model,masking,sparsity,n,median_ii_diff,ci_lo,ci_hi,\"\n                    \"ci_excludes_zero,significance,wilcoxon_p,bonferroni_p,mid_null_rate\\\\n\")'''\n\ncode = code.replace(old_csv_header, new_csv_header)\n\nold_csv_row = '''                    f.write(f\"{m_name},{masking},{sl},{c['n_valid']},\"\n                            f\"{c['median_ii_diff']},{ci[0]},{ci[1]},\"\n                            f\"{c['ci_excludes_zero']},{c['wilcoxon_p']},\"\n                            f\"{c.get('bonferroni_p', '')},{null_rate}\\\\n\")'''\n\nnew_csv_row = '''                    sig = c.get(\"significance\", \"\")\n                    f.write(f\"{m_name},{masking},{sl},{c['n_valid']},\"\n                            f\"{c['median_ii_diff']},{ci[0]},{ci[1]},\"\n                            f\"{c['ci_excludes_zero']},{sig},{c['wilcoxon_p']},\"\n                            f\"{c.get('bonferroni_p', '')},{null_rate}\\\\n\")'''\n\ncode = code.replace(old_csv_row, new_csv_row)\n\n# ============================================================\n# 9. Update CSV d_z section: add dz_reliable + rank_biserial\n# ============================================================\nold_csv_dz_header = '''            f.write(\"\\\\n# Within-importance d_z\\\\n\")\n            f.write(\"model,pair,d_z,dz_ci_lo,dz_ci_hi,interpretation,wilcoxon_p,bonferroni_p,n_paired\\\\n\")'''\n\nnew_csv_dz_header = '''            f.write(\"\\\\n# Within-importance d_z (D064: dz_reliable flag)\\\\n\")\n            f.write(\"model,pair,d_z,dz_ci_lo,dz_ci_hi,dz_reliable,interpretation,rank_biserial_r,wilcoxon_p,bonferroni_p,n_paired\\\\n\")'''\n\ncode = code.replace(old_csv_dz_header, new_csv_dz_header)\n\nold_csv_dz_row = '''                    f.write(f\"{m_name},{pk},{v['d_z']},\"\n                            f\"{v['d_z_ci'][0]},{v['d_z_ci'][1]},\"\n                            f\"{v['interpretation']},{v['wilcoxon_p']},\"\n                            f\"{v.get('bonferroni_p', '')},{v['n_paired']}\\\\n\")'''\n\nnew_csv_dz_row = '''                    f.write(f\"{m_name},{pk},{v['d_z']},\"\n                            f\"{v['d_z_ci'][0]},{v['d_z_ci'][1]},\"\n                            f\"{v.get('dz_reliable', '')},\"\n                            f\"{v['interpretation']},{v.get('rank_biserial_r', '')},\"\n                            f\"{v['wilcoxon_p']},\"\n                            f\"{v.get('bonferroni_p', '')},{v['n_paired']}\\\\n\")'''\n\ncode = code.replace(old_csv_dz_row, new_csv_dz_row)\n\n# ============================================================\n# 10. Update CSV imp-vs-rand section: add rank_biserial\n# ============================================================\nold_csv_ivr_header = '''            f.write(\"\\\\n# Imp vs Rand (Wilcoxon only)\\\\n\")\n            f.write(\"model,sparsity,median_diff,wilcoxon_p,bonferroni_p,n_paired\\\\n\")'''\n\nnew_csv_ivr_header = '''            f.write(\"\\\\n# Imp vs Rand (Wilcoxon + rank-biserial)\\\\n\")\n            f.write(\"model,sparsity,median_diff,rank_biserial_r,wilcoxon_p,bonferroni_p,n_paired\\\\n\")'''\n\ncode = code.replace(old_csv_ivr_header, new_csv_ivr_header)\n\nold_csv_ivr_row = '''                    f.write(f\"{m_name},{sl},{v['median_diff']},\"\n                            f\"{v['wilcoxon_p']},{v.get('bonferroni_p', '')},\"\n                            f\"{v['n_paired']}\\\\n\")'''\n\nnew_csv_ivr_row = '''                    f.write(f\"{m_name},{sl},{v['median_diff']},\"\n                            f\"{v.get('rank_biserial_r', '')},\"\n                            f\"{v['wilcoxon_p']},{v.get('bonferroni_p', '')},\"\n                            f\"{v['n_paired']}\\\\n\")'''\n\ncode = code.replace(old_csv_ivr_row, new_csv_ivr_row)\n\n# ============================================================\n# 11. Update console output in main() for conditions: add sig\n# ============================================================\nold_console_cond = '''                print(f\"    {key}: median={c['median_ii_diff']:+.4f} \"\n                      f\"CI=[{ci[0]:.4f},{ci[1]:.4f}] \"\n                      f\"p_bonf={p_bonf:.4f} \"\n                      f\"mid_null={null_rate}\")'''\n\nnew_console_cond = '''                sig = c.get(\"significance\", \"\")\n                print(f\"    {key}: median={c['median_ii_diff']:+.4f} \"\n                      f\"CI=[{ci[0]:.4f},{ci[1]:.4f}] \"\n                      f\"p_bonf={p_bonf:.4f} [{sig}] \"\n                      f\"mid_null={null_rate}\")'''\n\ncode = code.replace(old_console_cond, new_console_cond)\n\n# ============================================================\n# 12. Update console output for d_z: add reliability + r_rb\n# ============================================================\nold_console_dz = '''                print(f\"    {pk}: d_z={v['d_z']:+.3f} [{v['d_z_ci'][0]:.3f},{v['d_z_ci'][1]:.3f}] \"\n                      f\"({v['interpretation']})\")'''\n\nnew_console_dz = '''                rel = \"reliable\" if v.get('dz_reliable', True) else \"UNRELIABLE†\"\n                r_rb_val = v.get('rank_biserial_r', float('nan'))\n                print(f\"    {pk}: d_z={v['d_z']:+.3f} [{v['d_z_ci'][0]:.3f},{v['d_z_ci'][1]:.3f}] \"\n                      f\"({v['interpretation']}) r_rb={r_rb_val:+.3f} [{rel}]\")'''\n\ncode = code.replace(old_console_dz, new_console_dz)\n\n# ============================================================\n# 13. Update console output for imp-vs-rand: add r_rb\n# ============================================================\nold_console_ivr = '''                print(f\"    {sl}: median_diff={v['median_diff']:+.4f} \"\n                      f\"p_bonf={v.get('bonferroni_p', v['wilcoxon_p']):.4f}\")'''\n\nnew_console_ivr = '''                r_rb_val = v.get('rank_biserial_r', float('nan'))\n                print(f\"    {sl}: median_diff={v['median_diff']:+.4f} \"\n                      f\"r_rb={r_rb_val:+.3f} \"\n                      f\"p_bonf={v.get('bonferroni_p', v['wilcoxon_p']):.4f}\")'''\n\ncode = code.replace(old_console_ivr, new_console_ivr)\n\nwith open(filepath, \"w\") as f:\n    f.write(code)\n\nprint(\"Patch applied successfully.\")\nprint(f\"File size: {len(code)} chars\")\nPYEOF\npython3 /root/autodl-tmp/pacs/_patch_d063_d064.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-22162",
    "command": "cat > /root/autodl-tmp/pacs/_patch_d063_d064.py << 'PYEOF'\nimport re\n\nfilepath = \"/root/autodl-tmp/pacs/analyze_n500_unified.py\"\nwith open(filepath, \"r\") as f:\n    code = f.read()\n\n# ============================================================\n# 1. Update docstring: add D063/D064 constraints\n# ============================================================\nold_constraints = \"\"\"Constraints:\n  D054: median only, no mean\n  D059: d_z within-importance only; imp-vs-rand gets Wilcoxon + median_diff\"\"\"\n\nnew_constraints = \"\"\"Constraints:\n  D054: median only, no mean\n  D059: d_z within-importance only; imp-vs-rand gets Wilcoxon + median_diff\n  D063: random conditions report values + significance, no FAIL/PASS\n  D064: d_z auxiliary with reliability flag; rank-biserial correlation added\"\"\"\n\ncode = code.replace(old_constraints, new_constraints)\n\n# ============================================================\n# 2. Add new helper functions after interpret_d()\n# ============================================================\nafter_interpret_d = '''def interpret_d(d: float) -> str:\n    ad = abs(d)\n    if ad < 0.2:\n        return \"negligible\"\n    elif ad < 0.5:\n        return \"small\"\n    elif ad < 0.8:\n        return \"medium\"\n    return \"large\"'''\n\nnew_helpers = after_interpret_d + '''\n\n\ndef sig_stars(p: float) -> str:\n    if p < 0.001:\n        return \"***\"\n    if p < 0.01:\n        return \"**\"\n    if p < 0.05:\n        return \"*\"\n    return \"ns\"\n\n\ndef matched_pairs_rank_biserial(diffs: np.ndarray) -> float:\n    nonzero = diffs[diffs != 0]\n    n = len(nonzero)\n    if n < 2:\n        return float(\"nan\")\n    ranks = stats.rankdata(np.abs(nonzero))\n    w_plus = float(np.sum(ranks[nonzero > 0]))\n    w_minus = float(np.sum(ranks[nonzero < 0]))\n    denom = n * (n + 1) / 2.0\n    return float((w_plus - w_minus) / denom)\n\n\ndef dz_is_reliable(dz_ci: list, slabel_a: str, slabel_b: str) -> bool:\n    ci_lo, ci_hi = dz_ci\n    if any(np.isnan(x) for x in [ci_lo, ci_hi]):\n        return False\n    ci_width = ci_hi - ci_lo\n    if ci_width > 0.5:\n        return False\n    high_sparsity = slabel_a in (\"s025\", \"s030\") or slabel_b in (\"s025\", \"s030\")\n    if high_sparsity:\n        mid = (ci_lo + ci_hi) / 2.0\n        upper = ci_hi - mid\n        lower = mid - ci_lo\n        if lower > 0 and upper / lower > 3.0:\n            return False\n        if upper > 0 and lower / upper > 3.0:\n            return False\n    return True'''\n\ncode = code.replace(after_interpret_d, new_helpers)\n\n# ============================================================\n# 3. Add sig_stars to analyze_condition output\n# ============================================================\nold_condition_return = \"\"\"    return {\n        \"n_valid\": n_valid,\n        \"median_ii_diff\": med,\n        \"median_ii_diff_ci\": [ci_lo, ci_hi],\n        \"ci_excludes_zero\": not crosses_zero,\n        \"wilcoxon_stat\": float(wilcoxon_stat),\n        \"wilcoxon_p\": float(wilcoxon_p),\n        \"per_phase_median\": per_phase,\n        \"midphase_null\": null_info,\n    }\"\"\"\n\nnew_condition_return = \"\"\"    p_val = float(wilcoxon_p)\n    return {\n        \"n_valid\": n_valid,\n        \"median_ii_diff\": med,\n        \"median_ii_diff_ci\": [ci_lo, ci_hi],\n        \"ci_excludes_zero\": not crosses_zero,\n        \"significance\": sig_stars(p_val),\n        \"wilcoxon_stat\": float(wilcoxon_stat),\n        \"wilcoxon_p\": p_val,\n        \"per_phase_median\": per_phase,\n        \"midphase_null\": null_info,\n    }\"\"\"\n\ncode = code.replace(old_condition_return, new_condition_return)\n\n# ============================================================\n# 4. Add dz_reliable + rank_biserial to within-importance d_z\n# ============================================================\nold_dz_block = \"\"\"        dz_importance[pair_key] = {\n            \"d_z\": dz,\n            \"d_z_ci\": list(dz_ci),\n            \"interpretation\": interpret_d(dz),\n            \"n_paired\": n_paired,\n            \"median_diff\": float(np.median(paired_diffs)),\n            \"wilcoxon_stat\": float(w_stat),\n            \"wilcoxon_p\": float(w_p),\n        }\"\"\"\n\nnew_dz_block = \"\"\"        dz_ci_list = list(dz_ci)\n        r_rb = matched_pairs_rank_biserial(paired_diffs)\n        dz_importance[pair_key] = {\n            \"d_z\": dz,\n            \"d_z_ci\": dz_ci_list,\n            \"dz_reliable\": dz_is_reliable(dz_ci_list, sl_a, sl_b),\n            \"interpretation\": interpret_d(dz),\n            \"rank_biserial_r\": r_rb,\n            \"n_paired\": n_paired,\n            \"median_diff\": float(np.median(paired_diffs)),\n            \"wilcoxon_stat\": float(w_stat),\n            \"wilcoxon_p\": float(w_p),\n        }\"\"\"\n\ncode = code.replace(old_dz_block, new_dz_block)\n\n# ============================================================\n# 5. Add rank_biserial to imp_vs_rand\n# ============================================================\nold_ivr = \"\"\"        imp_vs_rand[sl] = {\n            \"median_diff\": float(np.median(paired_diffs)),\n            \"wilcoxon_stat\": float(w_stat),\n            \"wilcoxon_p\": float(w_p),\n            \"n_paired\": n_paired,\n        }\n\n    # 5. Permutation monotonicity test\"\"\"\n\nnew_ivr = \"\"\"        r_rb_ivr = matched_pairs_rank_biserial(paired_diffs)\n        imp_vs_rand[sl] = {\n            \"median_diff\": float(np.median(paired_diffs)),\n            \"rank_biserial_r\": r_rb_ivr,\n            \"wilcoxon_stat\": float(w_stat),\n            \"wilcoxon_p\": float(w_p),\n            \"n_paired\": n_paired,\n        }\n\n    # 5. Permutation monotonicity test\"\"\"\n\ncode = code.replace(old_ivr, new_ivr)\n\n# ============================================================\n# 6. Update LaTeX Table 1: add significance column, no FAIL/PASS\n# ============================================================\nold_latex_t1_header = \"\"\"    print(\"\\\\n% Table: Median II (low-high) by condition\")\n    print(\"% Model & Masking & Sparsity & n & Median & CI_low & CI_high & p & p_bonf \\\\\\\\\\\\\\\\\")\"\"\"\n\nnew_latex_t1_header = \"\"\"    print(\"\\\\n% Table: Median II (low-high) by condition\")\n    print(\"% Model & Masking & Sparsity & n & Median & CI_low & CI_high & p & p_bonf & sig \\\\\\\\\\\\\\\\\")\"\"\"\n\ncode = code.replace(old_latex_t1_header, new_latex_t1_header)\n\nold_latex_t1_row = '''                print(f\"{m_name.capitalize()} & {mask_label} & {s_val:.0%} & \"\n                      f\"{c['n_valid']} & {fmt(c['median_ii_diff'])} & \"\n                      f\"{fmt(ci[0])} & {fmt(ci[1])} & \"\n                      f\"{fmt_p(p_raw)} & {fmt_p(p_bonf)} \\\\\\\\\\\\\\\\\")'''\n\nnew_latex_t1_row = '''                sig = c.get(\"significance\", \"\")\n                print(f\"{m_name.capitalize()} & {mask_label} & {s_val:.0%} & \"\n                      f\"{c['n_valid']} & {fmt(c['median_ii_diff'])} & \"\n                      f\"{fmt(ci[0])} & {fmt(ci[1])} & \"\n                      f\"{fmt_p(p_raw)} & {fmt_p(p_bonf)} & {sig} \\\\\\\\\\\\\\\\\")'''\n\ncode = code.replace(old_latex_t1_row, new_latex_t1_row)\n\n# ============================================================\n# 7. Update LaTeX Table 3 (within-importance d_z): add † for unreliable\n# ============================================================\nold_latex_t3_header = \"\"\"    print(\"\\\\n% Table: Within-importance paired d_z (D059)\")\n    print(\"% Model & Pair & d_z & CI_low & CI_high & Interp & p & p_bonf \\\\\\\\\\\\\\\\\")\"\"\"\n\nnew_latex_t3_header = \"\"\"    print(\"\\\\n% Table: Within-importance paired d_z (D059, D064)\")\n    print(\"% Model & Pair & d_z & CI_low & CI_high & Interp & r_rb & p & p_bonf \\\\\\\\\\\\\\\\\")\"\"\"\n\ncode = code.replace(old_latex_t3_header, new_latex_t3_header)\n\nold_latex_t3_row = '''            p_bonf = v.get(\"bonferroni_p\", v[\"wilcoxon_p\"])\n            print(f\"{m_name.capitalize()} & {pair_key} & \"\n                  f\"{fmt(v['d_z'])} & {fmt(v['d_z_ci'][0])} & {fmt(v['d_z_ci'][1])} & \"\n                  f\"{v['interpretation']} & {fmt_p(v['wilcoxon_p'])} & {fmt_p(p_bonf)} \\\\\\\\\\\\\\\\\")'''\n\nnew_latex_t3_row = '''            p_bonf = v.get(\"bonferroni_p\", v[\"wilcoxon_p\"])\n            dz_str = fmt(v['d_z'])\n            if not v.get('dz_reliable', True):\n                dz_str += \"$\\\\\\\\dagger$\"\n            r_rb_str = fmt(v.get('rank_biserial_r', float('nan')))\n            print(f\"{m_name.capitalize()} & {pair_key} & \"\n                  f\"{dz_str} & {fmt(v['d_z_ci'][0])} & {fmt(v['d_z_ci'][1])} & \"\n                  f\"{v['interpretation']} & {r_rb_str} & {fmt_p(v['wilcoxon_p'])} & {fmt_p(p_bonf)} \\\\\\\\\\\\\\\\\")'''\n\ncode = code.replace(old_latex_t3_row, new_latex_t3_row)\n\n# ============================================================\n# 8. Update CSV header for conditions: add significance column\n# ============================================================\nold_csv_header = '''            f.write(\"model,masking,sparsity,n,median_ii_diff,ci_lo,ci_hi,\"\n                    \"ci_excludes_zero,wilcoxon_p,bonferroni_p,mid_null_rate\\\\n\")'''\n\nnew_csv_header = '''            f.write(\"model,masking,sparsity,n,median_ii_diff,ci_lo,ci_hi,\"\n                    \"ci_excludes_zero,significance,wilcoxon_p,bonferroni_p,mid_null_rate\\\\n\")'''\n\ncode = code.replace(old_csv_header, new_csv_header)\n\nold_csv_row = '''                    f.write(f\"{m_name},{masking},{sl},{c['n_valid']},\"\n                            f\"{c['median_ii_diff']},{ci[0]},{ci[1]},\"\n                            f\"{c['ci_excludes_zero']},{c['wilcoxon_p']},\"\n                            f\"{c.get('bonferroni_p', '')},{null_rate}\\\\n\")'''\n\nnew_csv_row = '''                    sig = c.get(\"significance\", \"\")\n                    f.write(f\"{m_name},{masking},{sl},{c['n_valid']},\"\n                            f\"{c['median_ii_diff']},{ci[0]},{ci[1]},\"\n                            f\"{c['ci_excludes_zero']},{sig},{c['wilcoxon_p']},\"\n                            f\"{c.get('bonferroni_p', '')},{null_rate}\\\\n\")'''\n\ncode = code.replace(old_csv_row, new_csv_row)\n\n# ============================================================\n# 9. Update CSV d_z section: add dz_reliable + rank_biserial\n# ============================================================\nold_csv_dz_header = '''            f.write(\"\\\\n# Within-importance d_z\\\\n\")\n            f.write(\"model,pair,d_z,dz_ci_lo,dz_ci_hi,interpretation,wilcoxon_p,bonferroni_p,n_paired\\\\n\")'''\n\nnew_csv_dz_header = '''            f.write(\"\\\\n# Within-importance d_z (D064: dz_reliable flag)\\\\n\")\n            f.write(\"model,pair,d_z,dz_ci_lo,dz_ci_hi,dz_reliable,interpretation,rank_biserial_r,wilcoxon_p,bonferroni_p,n_paired\\\\n\")'''\n\ncode = code.replace(old_csv_dz_header, new_csv_dz_header)\n\nold_csv_dz_row = '''                    f.write(f\"{m_name},{pk},{v['d_z']},\"\n                            f\"{v['d_z_ci'][0]},{v['d_z_ci'][1]},\"\n                            f\"{v['interpretation']},{v['wilcoxon_p']},\"\n                            f\"{v.get('bonferroni_p', '')},{v['n_paired']}\\\\n\")'''\n\nnew_csv_dz_row = '''                    f.write(f\"{m_name},{pk},{v['d_z']},\"\n                            f\"{v['d_z_ci'][0]},{v['d_z_ci'][1]},\"\n                            f\"{v.get('dz_reliable', '')},\"\n                            f\"{v['interpretation']},{v.get('rank_biserial_r', '')},\"\n                            f\"{v['wilcoxon_p']},\"\n                            f\"{v.get('bonferroni_p', '')},{v['n_paired']}\\\\n\")'''\n\ncode = code.replace(old_csv_dz_row, new_csv_dz_row)\n\n# ============================================================\n# 10. Update CSV imp-vs-rand section: add rank_biserial\n# ============================================================\nold_csv_ivr_header = '''            f.write(\"\\\\n# Imp vs Rand (Wilcoxon only)\\\\n\")\n            f.write(\"model,sparsity,median_diff,wilcoxon_p,bonferroni_p,n_paired\\\\n\")'''\n\nnew_csv_ivr_header = '''            f.write(\"\\\\n# Imp vs Rand (Wilcoxon + rank-biserial)\\\\n\")\n            f.write(\"model,sparsity,median_diff,rank_biserial_r,wilcoxon_p,bonferroni_p,n_paired\\\\n\")'''\n\ncode = code.replace(old_csv_ivr_header, new_csv_ivr_header)\n\nold_csv_ivr_row = '''                    f.write(f\"{m_name},{sl},{v['median_diff']},\"\n                            f\"{v['wilcoxon_p']},{v.get('bonferroni_p', '')},\"\n                            f\"{v['n_paired']}\\\\n\")'''\n\nnew_csv_ivr_row = '''                    f.write(f\"{m_name},{sl},{v['median_diff']},\"\n                            f\"{v.get('rank_biserial_r', '')},\"\n                            f\"{v['wilcoxon_p']},{v.get('bonferroni_p', '')},\"\n                            f\"{v['n_paired']}\\\\n\")'''\n\ncode = code.replace(old_csv_ivr_row, new_csv_ivr_row)\n\n# ============================================================\n# 11. Update console output in main() for conditions: add sig\n# ============================================================\nold_console_cond = '''                print(f\"    {key}: median={c['median_ii_diff']:+.4f} \"\n                      f\"CI=[{ci[0]:.4f},{ci[1]:.4f}] \"\n                      f\"p_bonf={p_bonf:.4f} \"\n                      f\"mid_null={null_rate}\")'''\n\nnew_console_cond = '''                sig = c.get(\"significance\", \"\")\n                print(f\"    {key}: median={c['median_ii_diff']:+.4f} \"\n                      f\"CI=[{ci[0]:.4f},{ci[1]:.4f}] \"\n                      f\"p_bonf={p_bonf:.4f} [{sig}] \"\n                      f\"mid_null={null_rate}\")'''\n\ncode = code.replace(old_console_cond, new_console_cond)\n\n# ============================================================\n# 12. Update console output for d_z: add reliability + r_rb\n# ============================================================\nold_console_dz = '''                print(f\"    {pk}: d_z={v['d_z']:+.3f} [{v['d_z_ci'][0]:.3f},{v['d_z_ci'][1]:.3f}] \"\n                      f\"({v['interpretation']})\")'''\n\nnew_console_dz = '''                rel = \"reliable\" if v.get('dz_reliable', True) else \"UNRELIABLE†\"\n                r_rb_val = v.get('rank_biserial_r', float('nan'))\n                print(f\"    {pk}: d_z={v['d_z']:+.3f} [{v['d_z_ci'][0]:.3f},{v['d_z_ci'][1]:.3f}] \"\n                      f\"({v['interpretation']}) r_rb={r_rb_val:+.3f} [{rel}]\")'''\n\ncode = code.replace(old_console_dz, new_console_dz)\n\n# ============================================================\n# 13. Update console output for imp-vs-rand: add r_rb\n# ============================================================\nold_console_ivr = '''                print(f\"    {sl}: median_diff={v['median_diff']:+.4f} \"\n                      f\"p_bonf={v.get('bonferroni_p', v['wilcoxon_p']):.4f}\")'''\n\nnew_console_ivr = '''                r_rb_val = v.get('rank_biserial_r', float('nan'))\n                print(f\"    {sl}: median_diff={v['median_diff']:+.4f} \"\n                      f\"r_rb={r_rb_val:+.3f} \"\n                      f\"p_bonf={v.get('bonferroni_p', v['wilcoxon_p']):.4f}\")'''\n\ncode = code.replace(old_console_ivr, new_console_ivr)\n\nwith open(filepath, \"w\") as f:\n    f.write(code)\n\nprint(\"Patch applied successfully.\")\nprint(f\"File size: {len(code)} chars\")\nPYEOF\npython3 /root/autodl-tmp/pacs/_patch_d063_d064.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-15T04:54:38.059388+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Patch applied successfully.\\nFile size: 28332 chars\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-15T04:54:38.059570+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-22162",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python3 -c \"import py_compile; py_compile.compile('analyze_n500_unified.py', doraise=True); print('syntax OK')\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-22162",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python3 -c \"import py_compile; py_compile.compile('analyze_n500_unified.py', doraise=True); print('syntax OK')\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-15T04:54:38.059706+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"syntax OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-15T04:54:38.059916+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-22162",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python3 analyze_n500_unified.py --csv --latex 2>&1",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-22162",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python3 analyze_n500_unified.py --csv --latex 2>&1",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-15T04:54:38.060156+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n======================================================================\\n  DEEPSEEK\\n======================================================================\\n  imp_s015: median=+0.3907 CI=[0.3496,0.4431] p_bonf=0.0000 mid_null=0.102\\n  imp_s020: median=+1.2149 CI=[1.1072,1.3365] p_bonf=0.0000 mid_null=0.102\\n  imp_s025: median=+3.9857 CI=[3.5272,4.3588] p_bonf=0.0000 mid_null=0.102\\n  rand_s015: median=+0.0139 CI=[-0.0167,0.0389] p_bonf=1.0000 mid_null=0.102\\n  rand_s020: median=+0.0315 CI=[-0.0112,0.0767] p_bonf=1.0000 mid_null=0.102\\n  rand_s025: median=+0.2574 CI=[0.1265,0.3498] p_bonf=0.0190 mid_null=0.102\\n\\n  Within-imp d_z:\\n    s015_vs_s020: d_z=-0.468 [-0.528,-0.415] (small) r_rb=-0.876 [reliable]\\n    s020_vs_s025: d_z=-0.156 [-0.643,-0.135] (negligible) r_rb=-0.923 [UNRELIABLE†]\\n    s025_vs_s030: missing data\\n    s015_vs_s030: missing data\\n\\n  Imp-vs-rand:\\n    s015: median_diff=+0.4227 r_rb=+0.696 p_bonf=0.0000\\n    s020: median_diff=+1.2908 r_rb=+0.735 p_bonf=0.0000\\n    s025: median_diff=+4.1973 r_rb=+0.744 p_bonf=0.0000\\n    s030: missing data\\n\\n  Dose-response:\\n    importance: monotonic=True rho=1.000 (p=0.0000) gradient_sum=3.5950 perm_p=0.1650\\n    random: monotonic=True rho=1.000 (p=0.0000) gradient_sum=0.2435 perm_p=0.1650\\n\\n======================================================================\\n  QWEN\\n======================================================================\\n  imp_s015: median=+0.0659 CI=[0.0492,0.0925] p_bonf=0.0000 mid_null=0.452\\n  imp_s020: median=+0.3073 CI=[0.2612,0.3564] p_bonf=0.0000 mid_null=0.452\\n  imp_s025: median=+1.0745 CI=[0.9766,1.1787] p_bonf=0.0000 mid_null=0.452\\n  rand_s015: median=-0.0111 CI=[-0.0390,0.0124] p_bonf=1.0000 mid_null=0.452\\n  rand_s020: median=+0.0153 CI=[-0.0145,0.0684] p_bonf=1.0000 mid_null=0.452\\n  rand_s025: median=+0.3931 CI=[0.2360,0.5529] p_bonf=0.0000 mid_null=0.452\\n\\n  Within-imp d_z:\\n 
…[truncated 4790 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-15T04:54:38.060368+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "grep -n \"dz_reliable\\|rank_biserial\\|significance\" /root/autodl-tmp/pacs/analysis_output/n500_unified.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "grep -n \"dz_reliable\\|rank_biserial\\|significance\" /root/autodl-tmp/pacs/analysis_output/n500_unified.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-15T04:54:38.060531+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-15T04:54:38.060657+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "grep -n \"dz_reliable\" /root/autodl-tmp/pacs/analysis_output/n500_unified.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "grep -n \"dz_reliable\" /root/autodl-tmp/pacs/analysis_output/n500_unified.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-15T04:54:38.060792+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"282:          \\\"dz_reliable\\\": true,\\n297:          \\\"dz_reliable\\\": false,\\n692:          \\\"dz_reliable\\\": true,\\n707:          \\\"dz_reliable\\\": true,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-15T04:54:38.060914+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "grep -n \"rank_biserial\" /root/autodl-tmp/pacs/analysis_output/n500_unified.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "grep -n \"rank_biserial\" /root/autodl-tmp/pacs/analysis_output/n500_unified.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-15T04:54:38.061047+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"284:          \\\"rank_biserial_r\\\": -0.876143960537418,\\n299:          \\\"rank_biserial_r\\\": -0.9225027584864023,\\n338:          \\\"rank_biserial_r\\\": 0.695949892905822,\\n346:          \\\"rank_biserial_r\\\": 0.7346498344908159,\\n354:          \\\"rank_biserial_r\\\": 0.7443532160706172,\\n694:          \\\"rank_biserial_r\\\": -0.6320035382574082,\\n709:          \\\"rank_biserial_r\\\": -0.8395577178239717,\\n748:          \\\"rank_biserial_r\\\": 0.30130030959752324,\\n756:          \\\"rank_biserial_r\\\": 0.3725077399380805,\\n764:          \\\"rank_biserial_r\\\": 0.30943830163644404,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-15T04:54:38.061171+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "grep -n \"significance\" /root/autodl-tmp/pacs/analysis_output/n500_unified.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "grep -n \"significance\" /root/autodl-tmp/pacs/analysis_output/n500_unified.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-15T04:54:38.061308+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"24:          \\\"significance\\\": \\\"***\\\",\\n67:          \\\"significance\\\": \\\"***\\\",\\n110:          \\\"significance\\\": \\\"***\\\",\\n153:          \\\"significance\\\": \\\"ns\\\",\\n196:          \\\"significance\\\": \\\"ns\\\",\\n239:          \\\"significance\\\": \\\"**\\\",\\n434:          \\\"significance\\\": \\\"***\\\",\\n477:          \\\"significance\\\": \\\"***\\\",\\n520:          \\\"significance\\\": \\\"***\\\",\\n563:          \\\"significance\\\": \\\"ns\\\",\\n606:          \\\"significance\\\": \\\"ns\\\",\\n649:          \\\"significance\\\": \\\"***\\\",\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-15T04:54:38.061463+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-22162",
  "command": "rm /root/autodl-tmp/pacs/_patch_d063_d064.py /root/autodl-tmp/pacs/analyze_n500_unified.py.bak",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-22162",
    "command": "rm /root/autodl-tmp/pacs/_patch_d063_d064.py /root/autodl-tmp/pacs/analyze_n500_unified.py.bak",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-15T04:54:38.061599+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-15T04:54:38.061759+00:00_

修改完成，三项变更已全部生效：

**D063** — random 条件不再有二元判断，改为 `significance` 字段（`***`/`**`/`*`/`ns`），LaTeX 和 CSV 均包含新列

**D064** — `dz_reliable` 布尔字段已加入（CI 宽度 > 0.5 或高 sparsity 下 CI 不对称比 > 3:1 → `false`）。Deepseek `s020_vs_s025` 被标记为不可靠（CI 宽度 0.507），LaTeX 中显示 `†`

**Rank-biserial** — `rank_biserial_r` 已加入 within-importance d_z 和 imp-vs-rand 两个分析块的 JSON/CSV/LaTeX/console 输出

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_fix_n500_pipeline_d063_d064_20260515T045046"
}
```

</details>

---
