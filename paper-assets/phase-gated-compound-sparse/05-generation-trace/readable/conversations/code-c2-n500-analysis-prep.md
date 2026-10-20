# code c2 n500 analysis prep

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 0
- **Tool calls:** 21
- **Original source:** `logs/chats/worker_code_c2_n500_analysis_prep_20260514T184028.jsonl`
- **Structured JSON:** [`0dba6489e9b7330ee801.json`](../../sessions/0d/0dba6489e9b7330ee801.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

43 recorded events

### Tool call

_source line 1 · 2026-05-14T18:44:15.081728+00:00_

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
  "session": "worker_code_c2_n500_analysis_prep_20260514T184028",
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

_source line 2 · 2026-05-14T18:44:15.082093+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_c2_n500_analysis_prep_20260514T184028",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T18:44:15.082260+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "ls /root/autodl-tmp/pacs/analysis_output/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_c2_n500_analysis_prep_20260514T184028",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "ls /root/autodl-tmp/pacs/analysis_output/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-14T18:44:15.082391+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "find /root/autodl-tmp/pacs/scripts/ -name \"*.py\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_c2_n500_analysis_prep_20260514T184028",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "find /root/autodl-tmp/pacs/scripts/ -name \"*.py\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-14T18:44:15.082564+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"analyze_n500_deepseek_dryrun.json\\nanalyze_n500_qwen_dryrun.json\\nbf16_qw_rand_s015\\nbf16_qw_rand_s020\\nbf16_qw_rand_s025\\nbf16_qw_rand_s030\\nc2_n500_report_dryrun.md\\nc2_n500_results_dryrun.json\\nc3_llama_cohens_d.json\\nc3_llama_report.md\\nc3_llama_results.json\\ncohens_d_bf16.json\\ncohens_d_bf16_qwen.json\\ncohens_d_n500_dryrun.json\\ncohens_d_paired_b10000.json\\ncohens_d_paired_b10000_6point.json\\ncohens_d_paired_dz_6point.json\\ncross_model_analysis.json\\nexperiment_summary_table.json\\npermutation_test_results.json\\nrebootstrap_b10000_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.3}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_c2_n500_analysis_prep_20260514T184028",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T18:44:15.082694+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "find /root/autodl-tmp/pacs -path \"*/c2_*n500*\" -name \"profiling_results.json\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_c2_n500_analysis_prep_20260514T184028",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "find /root/autodl-tmp/pacs -path \"*/c2_*n500*\" -name \"profiling_results.json\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-14T18:44:15.082819+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"find: '/root/autodl-tmp/pacs/scripts/': No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_c2_n500_analysis_prep_20260514T184028",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T18:44:15.082937+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_c2_n500_analysis_prep_20260514T184028",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T18:44:15.083067+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "find /root/autodl-tmp/pacs -name \"analyze*.py\" -o -name \"analysis*.py\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_c2_n500_analysis_prep_20260514T184028",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "find /root/autodl-tmp/pacs -name \"analyze*.py\" -o -name \"analysis*.py\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T18:44:15.083196+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/pacs/profiling/analyze_results.py\\n/root/autodl-tmp/pacs/profiling/analyze_n500.py\\n/root/autodl-tmp/pacs/pacs/profiling/analyze_results.py\\n/root/autodl-tmp/pacs/pacs/profiling/analyze_n500.py\\n/root/autodl-tmp/pacs/analyze_v4_comparison.py\\n/root/autodl-tmp/pacs/analysis/analyze_strategy_phase_crossover.py\\n/root/autodl-tmp/pacs/analysis/analyze_v6_complete.py\\n/root/autodl-tmp/pacs/analyze_c2_n500.py\\n/root/autodl-tmp/pacs/analyze_c3_llama.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_c2_n500_analysis_prep_20260514T184028",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T18:44:15.083323+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "head -100 /root/autodl-tmp/pacs/analysis_output/c3_llama_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_c2_n500_analysis_prep_20260514T184028",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "head -100 /root/autodl-tmp/pacs/analysis_output/c3_llama_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T18:44:15.083527+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"conditions\\\": {\\n    \\\"s015\\\": {\\n      \\\"sparsity_label\\\": \\\"s015\\\",\\n      \\\"sparsity_key\\\": \\\"0.15\\\",\\n      \\\"imp_vs_rand\\\": {\\n        \\\"d_z\\\": 0.19225138846763962,\\n        \\\"d_z_ci\\\": [\\n          -0.08617740273835006,\\n          0.49603215305542003\\n        ],\\n        \\\"d_z_interpretation\\\": \\\"negligible\\\",\\n        \\\"median_diff\\\": 0.020257102834024265,\\n        \\\"median_diff_ci\\\": [\\n          0.0016488482019793027,\\n          0.04347908904179021\\n        ],\\n        \\\"ci_crosses_zero\\\": false,\\n        \\\"mean_diff\\\": 0.021268112473844396,\\n        \\\"std_diff\\\": 0.11062657410884871,\\n        \\\"wilcoxon_stat\\\": 774.0,\\n        \\\"wilcoxon_p\\\": 0.05487489561739345,\\n        \\\"wilcoxon_p_bonferroni\\\": 0.2194995824695738,\\n        \\\"significant_bonferroni\\\": false,\\n        \\\"n_valid\\\": 49,\\n        \\\"n_skipped\\\": 1\\n      },\\n      \\\"phase_gradient_importance\\\": {\\n        \\\"d_z\\\": 1.0079201236023063,\\n        \\\"d_z_ci\\\": [\\n          0.5930227488814525,\\n          1.7024933729406215\\n        ],\\n        \\\"d_z_interpretation\\\": \\\"large\\\",\\n        \\\"mean_diff\\\": 0.05441382480766818,\\n        \\\"std_diff\\\": 0.05398624705814305,\\n        \\\"n\\\": 49,\\n        \\\"n_skipped\\\": 1\\n      },\\n      \\\"phase_gradient_random\\\": {\\n        \\\"d_z\\\": 0.3497305202096621,\\n        \\\"d_z_ci\\\": [\\n          0.06654450841272631,\\n          0.6916419318996692\\n        ],\\n        \\\"d_z_interpretation\\\": \\\"small\\\",\\n        \\\"mean_diff\\\": 0.03314571233382378,\\n        \\\"std_diff\\\": 0.09477500652203032,\\n        \\\"n\\\": 49,\\n        \\\"n_skipped\\\": 1\\n      }\\n    },\\n    \\\"s020\\\": {\\n      \\\"sparsity_label\\\": \\\"s020\\\",\\n      \\\"sparsity_key\\\": \\\"0.2\\\",\\n      \\\"imp_vs_rand\\\": {\\n        
…[truncated 1687 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_c2_n500_analysis_prep_20260514T184028",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T18:44:15.083684+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "find /root/autodl-tmp/pacs -path \"*/c2_*\" -type d",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_c2_n500_analysis_prep_20260514T184028",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "find /root/autodl-tmp/pacs -path \"*/c2_*\" -type d",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T18:44:15.083835+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_c2_n500_analysis_prep_20260514T184028",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T18:44:15.083996+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "cat /root/autodl-tmp/pacs/analyze_c2_n500.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_c2_n500_analysis_prep_20260514T184028",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "cat /root/autodl-tmp/pacs/analyze_c2_n500.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T18:44:15.084275+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nC2 n=500 Analysis: Phase-gated compound sparsity interaction.\\n\\nInput:  profiling_output_n500_bf16_{ds,qw}_{imp,rand}_s{015,020,025,030}/profiling_results.json\\n        profiling_output_bf16_{ds,qw}_{imp,rand}_s{015,020,025,030}/profiling_results.json  (n=50 reference)\\nOutput: analysis_output/c2_n500_results.json       — full analysis results\\n        analysis_output/cohens_d_n500.json          — paired d_z for paper figures\\n        analysis_output/c2_n500_report.md           — markdown report\\n        stdout                                      — formatted report\\n\\nUsage:  python analyze_c2_n500.py [--n50-only]    # --n50-only: dry-run with n=50 data\\n\\\"\\\"\\\"\\n\\nimport json\\nimport argparse\\nimport sys\\nimport os\\nfrom pathlib import Path\\nimport numpy as np\\nfrom scipy import stats\\n\\nBASE = Path(\\\"/root/autodl-tmp/pacs\\\")\\n\\nMODELS = {\\\"deepseek\\\": \\\"ds\\\", \\\"qwen\\\": \\\"qw\\\"}\\nMASKING_TYPES = [\\\"imp\\\", \\\"rand\\\"]\\nSPARSITY_LABELS = [\\\"s015\\\", \\\"s020\\\", \\\"s025\\\", \\\"s030\\\"]\\nSPARSITY_KEY_MAP = {\\\"s015\\\": \\\"0.15\\\", \\\"s020\\\": \\\"0.2\\\", \\\"s025\\\": \\\"0.25\\\", \\\"s030\\\": \\\"0.3\\\"}\\nPHASES = [\\\"high\\\", \\\"mid\\\", \\\"low\\\"]\\n\\nB_BOOTSTRAP = 10000\\nSEED = 42\\n\\n\\ndef output_dir_name(model_short, masking, slabel, prefix=\\\"n500\\\"):\\n    if prefix == \\\"n500\\\":\\n        return f\\\"profiling_output_n500_bf16_{model_short}_{masking}_{slabel}\\\"\\n    else:\\n        return f\\\"profiling_output_bf16_{model_short}_{masking}_{slabel}\\\"\\n\\n\\ndef load_profiling(dirpath):\\n    fpath = Path(dirpath) / \\\"profiling_results.json\\\"\\n    if not fpath.exists():\\n        return None\\n    with open(fpath) as f:\\n        return json.load(f)\\n\\n\\ndef extract_per_problem_ii(data):\\n    ppi = data.get(\\\"per_problem_ii\\\", {})\\n    keys = list(ppi.keys())\\n    if not keys:\\n  
…[truncated 7469 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_c2_n500_analysis_prep_20260514T184028",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T18:44:15.084452+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "cat /root/autodl-tmp/pacs/profiling/analyze_n500.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_c2_n500_analysis_prep_20260514T184028",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "cat /root/autodl-tmp/pacs/profiling/analyze_n500.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T18:44:15.084735+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nC2 n=500 analysis: integrity checks, paired statistics, dose-response, discrimination.\\n\\nUsage:\\n  python -m pacs.profiling.analyze_n500 --model deepseek\\n  python -m pacs.profiling.analyze_n500 --model qwen\\n  python -m pacs.profiling.analyze_n500 --model deepseek --n50-only   # dry-run with n=50 data\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport sys\\nfrom collections import Counter\\nfrom pathlib import Path\\nfrom typing import Any, Dict, List, Optional, Tuple\\n\\nimport numpy as np\\nfrom scipy import stats\\n\\nBASE = Path(\\\"/root/autodl-tmp/pacs\\\")\\nOUT_DIR = BASE / \\\"analysis_output\\\"\\n\\nMODELS = {\\\"deepseek\\\": \\\"ds\\\", \\\"qwen\\\": \\\"qw\\\"}\\nMETHODS = [\\\"imp\\\", \\\"rand\\\"]\\nSPARSITY_LABELS = [\\\"s015\\\", \\\"s020\\\", \\\"s025\\\", \\\"s030\\\"]\\nSPARSITY_VALUES = {\\\"s015\\\": 0.15, \\\"s020\\\": 0.20, \\\"s025\\\": 0.25, \\\"s030\\\": 0.30}\\nSPARSITY_KEYS = {\\\"s015\\\": \\\"0.15\\\", \\\"s020\\\": \\\"0.2\\\", \\\"s025\\\": \\\"0.25\\\", \\\"s030\\\": \\\"0.3\\\"}\\nPHASES = [\\\"high\\\", \\\"mid\\\", \\\"low\\\"]\\n\\nB_BOOTSTRAP = 10000\\nSEED = 42\\n\\n\\n# ── Path helpers ─────────────────────��───────────────────────────────\\n\\ndef result_dir(model_short: str, method: str, slabel: str, n500: bool) -> Path:\\n    prefix = \\\"n500_bf16\\\" if n500 else \\\"bf16\\\"\\n    return BASE / f\\\"profiling_output_{prefix}_{model_short}_{method}_{slabel}\\\"\\n\\n\\ndef load_json(dirpath: Path) -> Optional[dict]:\\n    fpath = dirpath / \\\"profiling_results.json\\\"\\n    if not fpath.exists():\\n        return None\\n    with open(fpath) as f:\\n        return json.load(f)\\n\\n\\n# ── Data integrity ───────────────────────────────────────────────────\\n\\ndef check_integrity(data: dict, expected_n: int, label: str) -> dict:\\n    \\\"\\\"\\\"Validate data integrity for one condition.\\\"\\\"\\\"\\n    report = {\\n        \\\"l
…[truncated 7427 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_c2_n500_analysis_prep_20260514T184028",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T18:44:15.084944+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "find /root/autodl-tmp/pacs -name \"profiling_results.json\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_c2_n500_analysis_prep_20260514T184028",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "find /root/autodl-tmp/pacs -name \"profiling_results.json\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T18:44:15.085115+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/pacs/profiling_output_v2/profiling_results.json\\n/root/autodl-tmp/pacs/profiling_output_v3/profiling_results.json\\n/root/autodl-tmp/pacs/profiling_output_v4a/profiling_results.json\\n/root/autodl-tmp/pacs/profiling_output_v4b/profiling_results.json\\n/root/autodl-tmp/pacs/profiling_output_v4c/profiling_results.json\\n/root/autodl-tmp/pacs/profiling_output_v4d/profiling_results.json\\n/root/autodl-tmp/pacs/profiling_output_v4_random_r2/profiling_results.json\\n/root/autodl-tmp/pacs/profiling_output_qwen_dryrun/profiling_results.json\\n/root/autodl-tmp/pacs/profiling_output_v4_s025/profiling_results.json\\n/root/autodl-tmp/pacs/profiling_output_v4_s035/profiling_results.json\\n/root/autodl-tmp/pacs/profiling_output_v5_s020/profiling_results.json\\n/root/autodl-tmp/pacs/profiling_output_v5_s030/profiling_results.json\\n/root/autodl-tmp/pacs/profiling_output_sanity_check/profiling_results.json\\n/root/autodl-tmp/pacs/profiling_output_v5_s015/profiling_results.json\\n/root/autodl-tmp/pacs/profiling_output_v5_s025/profiling_results.json\\n/root/autodl-tmp/pacs/profiling_output_v5_s020_r2/profiling_results.json\\n/root/autodl-tmp/pacs/profiling_output_v5_s030_r2/profiling_results.json\\n/root/autodl-tmp/pacs/profiling_output_v5_random_s015/profiling_results.json\\n/root/autodl-tmp/pacs/profiling_output_v5_random_s025/profiling_results.json\\n/root/autodl-tmp/pacs/profiling_output_v5_random_s020/profiling_results.json\\n/root/autodl-tmp/pacs/profiling_output_v5_random_s030/profiling_results.json\\n/root/autodl-tmp/pacs/profiling_output_dryrun/profiling_results.json\\n/root/autodl-tmp/pacs/profiling_output_v6_importance_s015/profiling_results.json\\n/root/autodl-tmp/pacs/profiling_output_v6_importance_s020/profiling_results.json\\n/root/autodl-tmp/pacs/profiling_output_v6_importance_s025/profiling_results.json\\n/root/autodl-tmp/pacs/profiling_output_v6_importance_s030/profiling_results.json\\n/root/a
…[truncated 3240 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_c2_n500_analysis_prep_20260514T184028",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T18:44:15.085289+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "head -80 /root/autodl-tmp/pacs/profiling_output_n500_bf16_ds_imp_s015/profiling_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_c2_n500_analysis_prep_20260514T184028",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "head -80 /root/autodl-tmp/pacs/profiling_output_n500_bf16_ds_imp_s015/profiling_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T18:44:15.085487+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": {\\n    \\\"model\\\": \\\"/root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B\\\",\\n    \\\"sparsity_levels\\\": [\\n      0.15\\n    ],\\n    \\\"masking_method\\\": \\\"importance\\\",\\n    \\\"head_importance_metric\\\": \\\"attention_frobenius_norm\\\",\\n    \\\"kv_importance_metric\\\": \\\"cumulative_attention_received\\\",\\n    \\\"segmentation_method\\\": \\\"quantile\\\",\\n    \\\"n_bootstrap\\\": 1000,\\n    \\\"n_problems\\\": 500,\\n    \\\"seed\\\": 42\\n  },\\n  \\\"phase_stats\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"n_tokens\\\": 230984,\\n      \\\"n_segments\\\": 4527\\n    },\\n    \\\"low_sparsity\\\": {\\n      \\\"n_tokens\\\": 290009,\\n      \\\"n_segments\\\": 4123\\n    },\\n    \\\"mid_sparsity\\\": {\\n      \\\"n_tokens\\\": 177399,\\n      \\\"n_segments\\\": 2420\\n    }\\n  },\\n  \\\"perplexity\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"0.15\\\": {\\n        \\\"dense\\\": 1.1827,\\n        \\\"attn\\\": 1.4964,\\n        \\\"kv\\\": 1.4501,\\n        \\\"both\\\": 1.5975\\n      }\\n    },\\n    \\\"low_sparsity\\\": {\\n      \\\"0.15\\\": {\\n        \\\"dense\\\": 1.2215,\\n        \\\"attn\\\": 1.5661,\\n        \\\"kv\\\": 7.9546,\\n        \\\"both\\\": 10.004\\n      }\\n    },\\n    \\\"mid_sparsity\\\": {\\n      \\\"0.15\\\": {\\n        \\\"dense\\\": 1.2304,\\n        \\\"attn\\\": 1.5219,\\n        \\\"kv\\\": 3.2278,\\n        \\\"both\\\": 3.839\\n      }\\n    }\\n  },\\n  \\\"interaction_index\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"0.15\\\": {\\n        \\\"mean\\\": -0.137396,\\n        \\\"ci_low\\\": -0.185634,\\n        \\\"ci_high\\\": -0.103346,\\n        \\\"median\\\": 0.006531,\\n        \\\"median_ci_low\\\": 0.005469,\\n        \\\"median_ci_high\\\": 0.007701,\\n        \\\"winsorized_mean\\\": -0.071004,\\n        \\\"skewness\\\": -42.927,\\n        \\\"outlier_count\\\": 20\\n      
…[truncated 527 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_c2_n500_analysis_prep_20260514T184028",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T18:44:15.085652+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/pacs/profiling_output_n500_bf16_ds_imp_s015/profiling_results.json')); print(list(d.keys())); ppi=d.get('per_problem_ii',{}); k=list(ppi.keys()); print('levels:', k); print('n_problems:', len(ppi[k[0]]) if k else 0); print('sample:', json.dumps(ppi[k[0]][0], indent=2) if k else 'none')\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_c2_n500_analysis_prep_20260514T184028",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/pacs/profiling_output_n500_bf16_ds_imp_s015/profiling_results.json')); print(list(d.keys())); ppi=d.get('per_problem_ii',{}); k=list(ppi.keys()); print('levels:', k); print('n_problems:', len(ppi[k[0]]) if k else 0); print('sample:', json.dumps(ppi[k[0]][0], indent=2) if k else 'none')\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T18:44:15.085780+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_c2_n500_analysis_prep_20260514T184028",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T18:44:15.085899+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/pacs/profiling_output_n500_bf16_ds_imp_s015/profiling_results.json')); print(list(d.keys()))\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_c2_n500_analysis_prep_20260514T184028",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/pacs/profiling_output_n500_bf16_ds_imp_s015/profiling_results.json')); print(list(d.keys()))\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T18:44:15.086015+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_c2_n500_analysis_prep_20260514T184028",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T18:44:15.086130+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/pacs/profiling_output_n500_bf16_ds_imp_s015/profiling_results.json')); ppi=d.get('per_problem_ii',{}); print('levels:', list(ppi.keys())); k=list(ppi.keys())[0]; print('n:', len(ppi[k])); print(json.dumps(ppi[k][0], indent=2))\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_c2_n500_analysis_prep_20260514T184028",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/pacs/profiling_output_n500_bf16_ds_imp_s015/profiling_results.json')); ppi=d.get('per_problem_ii',{}); print('levels:', list(ppi.keys())); k=list(ppi.keys())[0]; print('n:', len(ppi[k])); print(json.dumps(ppi[k][0], indent=2))\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T18:44:15.086245+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_c2_n500_analysis_prep_20260514T184028",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T18:44:15.086356+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "grep -c \"problem_idx\" /root/autodl-tmp/pacs/profiling_output_n500_bf16_ds_imp_s015/profiling_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_c2_n500_analysis_prep_20260514T184028",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "grep -c \"problem_idx\" /root/autodl-tmp/pacs/profiling_output_n500_bf16_ds_imp_s015/profiling_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T18:44:15.086497+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"500\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_c2_n500_analysis_prep_20260514T184028",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T18:44:15.086618+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "grep -m 1 \"per_problem_ii\" /root/autodl-tmp/pacs/profiling_output_n500_bf16_ds_imp_s015/profiling_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_c2_n500_analysis_prep_20260514T184028",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "grep -m 1 \"per_problem_ii\" /root/autodl-tmp/pacs/profiling_output_n500_bf16_ds_imp_s015/profiling_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T18:44:15.086733+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  \\\"per_problem_ii\\\": {\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_c2_n500_analysis_prep_20260514T184028",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T18:44:15.086847+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-22162",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\nd = json.load(open('/root/autodl-tmp/pacs/profiling_output_n500_bf16_ds_imp_s015/profiling_results.json'))\nprint('top keys:', list(d.keys()))\nppi = d.get('per_problem_ii', {})\nlevels = list(ppi.keys())\nprint('levels:', levels)\nif levels:\n    k = levels[0]\n    probs = ppi[k]\n    print('n_problems:', len(probs))\n    print('sample problem keys:', list(probs[0].keys()))\n    print('sample:', json.dumps(probs[0], indent=2))\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_c2_n500_analysis_prep_20260514T184028",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-22162",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\nd = json.load(open('/root/autodl-tmp/pacs/profiling_output_n500_bf16_ds_imp_s015/profiling_results.json'))\nprint('top keys:', list(d.keys()))\nppi = d.get('per_problem_ii', {})\nlevels = list(ppi.keys())\nprint('levels:', levels)\nif levels:\n    k = levels[0]\n    probs = ppi[k]\n    print('n_problems:', len(probs))\n    print('sample problem keys:', list(probs[0].keys()))\n    print('sample:', json.dumps(probs[0], indent=2))\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T18:44:15.086974+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"top keys: ['config', 'phase_stats', 'perplexity', 'interaction_index', 'pass_fail', 'warnings', 'diagnostics', 'per_problem_ii']\\nlevels: ['0.15']\\nn_problems: 500\\nsample problem keys: ['problem_idx', 'problem_id', 'ii_high', 'n_segments_high', 'ii_mid', 'n_segments_mid', 'ii_low', 'n_segments_low']\\nsample: {\\n  \\\"problem_idx\\\": 0,\\n  \\\"problem_id\\\": \\\"test/precalculus/807.json\\\",\\n  \\\"ii_high\\\": -0.01966178644683314,\\n  \\\"n_segments_high\\\": 5,\\n  \\\"ii_mid\\\": null,\\n  \\\"n_segments_mid\\\": 0,\\n  \\\"ii_low\\\": 0.05441385994922232,\\n  \\\"n_segments_low\\\": 2\\n}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_c2_n500_analysis_prep_20260514T184028",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-14T18:44:15.087130+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-22162",
  "command": "mkdir -p /root/autodl-tmp/pacs/scripts",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_c2_n500_analysis_prep_20260514T184028",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-22162",
    "command": "mkdir -p /root/autodl-tmp/pacs/scripts",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-14T18:44:15.087248+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_c2_n500_analysis_prep_20260514T184028",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-14T18:44:15.087481+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-22162",
  "command": "cat > /root/autodl-tmp/pacs/scripts/analyze_c2_n500.py << 'SCRIPT_EOF'\n\"\"\"\nC2 n=500 Median Bootstrap Analysis (D054-compliant).\n\nPrimary metric: median II + median bootstrap 95% CI (not mean).\nReason: DeepSeek II skewness ~9.5, mean unreliable.\n\nInput:  {base}/profiling_output_n500_bf16_{ds,qw}_{imp,rand}_s{015,020,025,030}/profiling_results.json\nOutput: {out}/c2_n500_results.json, {out}/c2_n500_report.md\n\nUsage:\n  python scripts/analyze_c2_n500.py\n  python scripts/analyze_c2_n500.py --base-dir /root/autodl-tmp/pacs --output-dir ./analysis_output\n  python scripts/analyze_c2_n500.py --model deepseek\n  python scripts/analyze_c2_n500.py --n50-only          # dry-run with n=50 reference data\n\"\"\"\n\nimport argparse\nimport json\nimport sys\nfrom collections import Counter\nfrom datetime import datetime\nfrom pathlib import Path\nfrom typing import Any, Dict, List, Optional, Tuple\n\nimport numpy as np\nfrom scipy import stats\n\n# ── Constants ────────────────────────────────────────────────────────\n\nMODELS = {\"deepseek\": \"ds\", \"qwen\": \"qw\"}\nMETHODS = [\"imp\", \"rand\"]\nSPARSITY_LABELS = [\"s015\", \"s020\", \"s025\", \"s030\"]\nSPARSITY_VALUES = {\"s015\": 0.15, \"s020\": 0.20, \"s025\": 0.25, \"s030\": 0.30}\nSPARSITY_KEYS = {\"s015\": \"0.15\", \"s020\": \"0.2\", \"s025\": \"0.25\", \"s030\": \"0.3\"}\nPHASES = [\"high\", \"mid\", \"low\"]\n\nB_BOOTSTRAP = 10000\nSEED = 42\nALPHA = 0.05\nN_BONFERRONI = 4  # 4 sparsity levels per model\n\n\n# ── Path helpers ─────────────────────────────────────────────────────\n\ndef result_dir(base: Path, model_short: str, method: str, slabel: str, n500: bool) -> Path:\n    prefix = \"n500_bf16\" if n500 else \"bf16\"\n    return base / f\"profiling_output_{prefix}_{model_short}_{method}_{slabel}\"\n\n\ndef load_json(dirpath: Path) -> Optional[dict]:\n    fpath = dirpath / \"profiling_results.json\"\n    if not fpath.exists():\n        return None\n    with open(fpath) as f:\n        return json.load(f)\n\n\ndef get_problems(data: dict) -> Optional[List[dict]]:\n    ppi = data.get(\"per_problem_ii\", {})\n    levels = list(ppi.keys())\n    if not levels:\n        return None\n    return ppi[levels[0]]\n\n\n# ── Data integrity ───────────────────────────────────────────────────\n\ndef check_integrity(data: dict, expected_n: int, label: str) -> dict:\n    report = {\"label\": label, \"status\": \"OK\", \"warnings\": [], \"errors\": []}\n\n    config_n = data.get(\"config\", {}).get(\"n_problems\", None)\n    problems = get_problems(data)\n    if not problems:\n        report[\"status\"] = \"ERROR\"\n        report[\"errors\"].append(\"No per_problem_ii data found\")\n        return report\n\n    actual_n = len(problems)\n\n    if actual_n != expected_n:\n        report[\"errors\"].append(f\"Expected {expected_n} problems, got {actual_n}\")\n        report[\"status\"] = \"ERROR\"\n\n    if config_n is not None and config_n != expected_n:\n        report[\"warnings\"].append(f\"Config n_problems={config_n}, expected {expected_n}\")\n\n    # problem_idx monotonicity\n    indices = [p[\"problem_idx\"] for p in problems]\n    non_monotonic = []\n    for i in range(1, len(indices)):\n        if indices[i] <= indices[i - 1]:\n            non_monotonic.append((i, indices[i - 1], indices[i]))\n    if non_monotonic:\n        if report[\"status\"] == \"OK\":\n            report[\"status\"] = \"WARNING\"\n        report[\"warnings\"].append(\n            f\"Non-monotonic problem_idx at {len(non_monotonic)} positions \"\n            f\"(first: pos {non_monotonic[0][0]}, \"\n            f\"{non_monotonic[0][1]} -> {non_monotonic[0][2]}). \"\n            f\"Possible duplicate-process contamination.\"\n        )\n\n    # duplicate problem_id\n    pids = [p[\"problem_id\"] for p in problems]\n    pid_counts = Counter(pids)\n    duplicates = {k: v for k, v in pid_counts.items() if v > 1}\n    if duplicates:\n        report[\"status\"] = \"ERROR\"\n        report[\"errors\"].append(\n            f\"Duplicate problem_ids: {len(duplicates)} IDs appear >1 time. \"\n            f\"First: {list(duplicates.items())[:3]}\"\n        )\n\n    # NaN/None in II values\n    nan_count = sum(1 for p in problems if p.get(\"ii_low\") is None or p.get(\"ii_high\") is None)\n    if nan_count > 0:\n        report[\"warnings\"].append(f\"{nan_count}/{actual_n} problems have null ii_high or ii_low\")\n        if nan_count > actual_n * 0.1:\n            report[\"status\"] = \"WARNING\"\n\n    # Check for null ii_mid (informational)\n    mid_null = sum(1 for p in problems if p.get(\"ii_mid\") is None)\n    if mid_null > 0:\n        report[\"warnings\"].append(f\"{mid_null}/{actual_n} problems have null ii_mid\")\n\n    return report\n\n\n# ── Statistical functions ────────────────────────────────────────────\n\ndef bootstrap_median_ci(values: np.ndarray, B: int = B_BOOTSTRAP, alpha: float = ALPHA, seed: int = SEED) -> Tuple[float, float]:\n    rng = np.random.RandomState(seed)\n    n = len(values)\n    boot = np.array([np.median(values[rng.randint(0, n, size=n)]) for _ in range(B)])\n    return float(np.percentile(boot, 100 * alpha / 2)), float(np.percentile(boot, 100 * (1 - alpha / 2)))\n\n\ndef bootstrap_mean_ci(values: np.ndarray, B: int = B_BOOTSTRAP, alpha: float = ALPHA, seed: int = SEED) -> Tuple[float, float]:\n    rng = np.random.RandomState(seed)\n    n = len(values)\n    boot = np.array([np.mean(values[rng.randint(0, n, size=n)]) for _ in range(B)])\n    return float(np.percentile(boot, 100 * alpha / 2)), float(np.percentile(boot, 100 * (1 - alpha / 2)))\n\n\ndef bootstrap_dz_ci(diffs: np.ndarray, B: int = B_BOOTSTRAP, alpha: float = ALPHA, seed: int = SEED) -> Tuple[float, float]:\n    rng = np.random.RandomState(seed)\n    n = len(diffs)\n    boot = np.empty(B)\n    for i in range(B):\n        sample = diffs[rng.randint(0, n, size=n)]\n        s = sample.std(ddof=1)\n        boot[i] = sample.mean() / s if s > 0 else np.nan\n    boot = boot[~np.isnan(boot)]\n    if len(boot) == 0:\n        return float(\"nan\"), float(\"nan\")\n    return float(np.percentile(boot, 100 * alpha / 2)), float(np.percentile(boot, 100 * (1 - alpha / 2)))\n\n\ndef paired_cohens_dz(diffs: np.ndarray) -> float:\n    if len(diffs) < 2:\n        return float(\"nan\")\n    s = np.std(diffs, ddof=1)\n    if s == 0:\n        return float(\"nan\")\n    return float(np.mean(diffs) / s)\n\n\ndef wilcoxon_test(diffs: np.ndarray, alternative: str = \"two-sided\") -> Tuple[float, float]:\n    nonzero = diffs[diffs != 0]\n    if len(nonzero) < 10:\n        return float(\"nan\"), float(\"nan\")\n    stat, p = stats.wilcoxon(nonzero, alternative=alternative)\n    return float(stat), float(p)\n\n\ndef interpret_d(d: float) -> str:\n    ad = abs(d)\n    if ad < 0.2:\n        return \"negligible\"\n    elif ad < 0.5:\n        return \"small\"\n    elif ad < 0.8:\n        return \"medium\"\n    return \"large\"\n\n\n# ── Per-condition analysis ───────────────────────────────────────────\n\ndef analyze_condition(problems: List[dict]) -> dict:\n    \"\"\"Full analysis for one condition. Phase gradient: D = ii_low - ii_high.\"\"\"\n    ii_low = []\n    ii_high = []\n    ii_mid = []\n    valid_idx = []\n\n    for i, p in enumerate(problems):\n        vl = p.get(\"ii_low\")\n        vh = p.get(\"ii_high\")\n        if vl is not None and vh is not None:\n            ii_low.append(vl)\n            ii_high.append(vh)\n            valid_idx.append(i)\n        vm = p.get(\"ii_mid\")\n        if vm is not None:\n            ii_mid.append(vm)\n\n    ii_low = np.array(ii_low)\n    ii_high = np.array(ii_high)\n    ii_mid = np.array(ii_mid) if ii_mid else np.array([])\n\n    diffs = ii_low - ii_high  # phase gradient: D per problem\n    n_valid = len(diffs)\n    n_total = len(problems)\n    n_skipped = n_total - n_valid\n\n    if n_valid < 10:\n        return {\"error\": f\"Too few valid problems ({n_valid})\", \"n_valid\": n_valid, \"n_total\": n_total}\n\n    # Primary metric: median + median bootstrap CI (D054)\n    median_diff = float(np.median(diffs))\n    median_ci = bootstrap_median_ci(diffs)\n    ci_crosses_zero = (median_ci[0] <= 0 <= median_ci[1])\n\n    # Reference: mean + mean bootstrap CI\n    mean_diff = float(np.mean(diffs))\n    std_diff = float(np.std(diffs, ddof=1))\n    mean_ci = bootstrap_mean_ci(diffs)\n\n    # Cohen's d_z (paired)\n    d_z = paired_cohens_dz(diffs)\n    d_z_ci = bootstrap_dz_ci(diffs)\n\n    # Wilcoxon signed-rank\n    w_stat, w_p = wilcoxon_test(diffs, alternative=\"two-sided\")\n    w_p_bonf = min(w_p * N_BONFERRONI, 1.0) if not np.isnan(w_p) else float(\"nan\")\n\n    # Skewness\n    skew = float(stats.skew(diffs))\n\n    # Per-phase medians (for reporting)\n    phase_medians = {}\n    for name, arr in [(\"low\", ii_low), (\"high\", ii_high), (\"mid\", ii_mid)]:\n        if len(arr) > 0:\n            med = float(np.median(arr))\n            ci = bootstrap_median_ci(arr)\n            phase_medians[name] = {\"median\": med, \"ci\": list(ci), \"n\": len(arr)}\n\n    return {\n        \"n_valid\": n_valid,\n        \"n_total\": n_total,\n        \"n_skipped\": n_skipped,\n        \"median_diff\": {\n            \"value\": median_diff,\n            \"ci\": list(median_ci),\n            \"ci_crosses_zero\": ci_crosses_zero,\n        },\n        \"mean_diff\": {\n            \"value\": mean_diff,\n            \"std\": std_diff,\n            \"ci\": list(mean_ci),\n        },\n        \"phase_gradient\": {\n            \"d_z\": d_z,\n            \"d_z_ci\": list(d_z_ci),\n            \"d_z_interpretation\": interpret_d(d_z),\n        },\n        \"wilcoxon\": {\n            \"stat\": w_stat,\n            \"p_value\": w_p,\n            \"p_bonferroni\": w_p_bonf,\n            \"significant_bonf_005\": bool(w_p_bonf < 0.05) if not np.isnan(w_p_bonf) else None,\n        },\n        \"skewness\": skew,\n        \"phase_medians\": phase_medians,\n    }\n\n\n# ── Paired imp vs rand ──────────────────────────────────────────────\n\ndef paired_imp_vs_rand(imp_problems: List[dict], rand_problems: List[dict]) -> dict:\n    \"\"\"Compare imp vs rand for the same questions (paired by problem_id).\"\"\"\n    imp_by_id = {}\n    for p in imp_problems:\n        vl, vh = p.get(\"ii_low\"), p.get(\"ii_high\")\n        if vl is not None and vh is not None:\n            imp_by_id[p[\"problem_id\"]] = vl - vh\n\n    rand_by_id = {}\n    for p in rand_problems:\n        vl, vh = p.get(\"ii_low\"), p.get(\"ii_high\")\n        if vl is not None and vh is not None:\n            rand_by_id[p[\"problem_id\"]] = vl - vh\n\n    common = sorted(set(imp_by_id.keys()) & set(rand_by_id.keys()))\n    if len(common) < 10:\n        return {\"error\": f\"Too few common problems ({len(common)})\"}\n\n    imp_vals = np.array([imp_by_id[pid] for pid in common])\n    rand_vals = np.array([rand_by_id[pid] for pid in common])\n    diffs = imp_vals - rand_vals  # D = gradient_imp - gradient_rand\n\n    median_diff = float(np.median(diffs))\n    median_ci = bootstrap_median_ci(diffs)\n    mean_diff = float(np.mean(diffs))\n    d_z = paired_cohens_dz(diffs)\n    d_z_ci = bootstrap_dz_ci(diffs)\n    w_stat, w_p = wilcoxon_test(diffs)\n\n    return {\n        \"n_paired\": len(common),\n        \"median_diff\": {\n            \"value\": median_diff,\n            \"ci\": list(median_ci),\n            \"ci_crosses_zero\": (median_ci[0] <= 0 <= median_ci[1]),\n        },\n        \"mean_diff\": mean_diff,\n        \"d_z\": d_z,\n        \"d_z_ci\": list(d_z_ci),\n        \"d_z_interpretation\": interpret_d(d_z),\n        \"wilcoxon_p\": w_p,\n    }\n\n\n# ── Markdown report ──────────────────────────────────────────────────\n\ndef format_report(all_results: dict, paired: dict, integrity: list,\n                  preregistration: dict, metadata: dict) -> str:\n    lines = []\n    lines.append(\"# C2 n=500 Median Bootstrap Analysis (D054)\")\n    lines.append(\"\")\n    lines.append(f\"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\")\n    lines.append(f\"Data source: {metadata.get('data_source', 'n=500')}\")\n    lines.append(f\"Bootstrap resamples: {B_BOOTSTRAP}, seed: {SEED}\")\n    lines.append(f\"**Primary metric: MEDIAN** (mean provided as reference only)\")\n    lines.append(\"\")\n\n    # Integrity\n    lines.append(\"## Data Integrity\")\n    lines.append(\"\")\n    for r in integrity:\n        status = r[\"status\"]\n        icon = \"OK\" if status == \"OK\" else (\"WARN\" if status == \"WARNING\" else \"ERR\")\n        lines.append(f\"- `{r['label']}`: [{icon}] n={r.get('actual_n', '?')}\")\n        for w in r.get(\"warnings\", []):\n            lines.append(f\"  - Warning: {w}\")\n        for e in r.get(\"errors\", []):\n            lines.append(f\"  - **Error: {e}**\")\n    lines.append(\"\")\n\n    # Per-condition table\n    lines.append(\"## Phase Gradient by Condition (D = ii_low - ii_high)\")\n    lines.append(\"\")\n    lines.append(\"| Condition | n | Median D | Median 95% CI | CI crosses 0? | Mean D | d_z | Wilcoxon p | Skew |\")\n    lines.append(\"|-----------|---|----------|---------------|---------------|--------|-----|------------|------|\")\n    for key in sorted(all_results.keys()):\n        r = all_results[key]\n        if \"error\" in r:\n            lines.append(f\"| {key} | - | ERROR: {r['error']} | | | | | | |\")\n            continue\n        md = r[\"median_diff\"]\n        mn = r[\"mean_diff\"]\n        pg = r[\"phase_gradient\"]\n        w = r[\"wilcoxon\"]\n        cross = \"YES\" if md[\"ci_crosses_zero\"] else \"no\"\n        sig = \"\"\n        if w.get(\"significant_bonf_005\"):\n            sig = \" *\"\n        lines.append(\n            f\"| {key} | {r['n_valid']} | {md['value']:.4f} | \"\n            f\"[{md['ci'][0]:.4f}, {md['ci'][1]:.4f}] | {cross} | \"\n            f\"{mn['value']:.4f} | {pg['d_z']:.3f} ({pg['d_z_interpretation']}) | \"\n            f\"{w['p_value']:.4f}{sig} | {r['skewness']:.1f} |\"\n        )\n    lines.append(\"\")\n\n    # Paired imp vs rand\n    lines.append(\"## Importance vs Random (paired by problem_id)\")\n    lines.append(\"\")\n    lines.append(\"| Sparsity | n_paired | Median(imp-rand) | Median 95% CI | d_z | Wilcoxon p |\")\n    lines.append(\"|----------|----------|------------------|---------------|-----|------------|\")\n    for key in sorted(paired.keys()):\n        p = paired[key]\n        if \"error\" in p:\n            lines.append(f\"| {key} | - | {p['error']} | | | |\")\n            continue\n        md = p[\"median_diff\"]\n        lines.append(\n            f\"| {key} | {p['n_paired']} | {md['value']:.4f} | \"\n            f\"[{md['ci'][0]:.4f}, {md['ci'][1]:.4f}] | \"\n            f\"{p['d_z']:.3f} ({p['d_z_interpretation']}) | {p['wilcoxon_p']:.4f} |\"\n        )\n    lines.append(\"\")\n\n    # Pre-registration verdict\n    if preregistration:\n        lines.append(\"## Pre-registration Verdict\")\n        lines.append(\"\")\n        for key, v in preregistration.items():\n            lines.append(f\"### {key}\")\n            lines.append(f\"- Median diff = {v['median_diff']:.6f}\")\n            lines.append(f\"- Median 95% CI = [{v['median_ci_lo']:.4f}, {v['median_ci_hi']:.4f}]\")\n            lines.append(f\"- CI crosses zero: **{v['crosses_zero']}**\")\n            lines.append(f\"- Wilcoxon p = {v['wilcoxon_p']:.4f}\")\n            lines.append(f\"- **Verdict: {v['verdict']}**\")\n            lines.append(\"\")\n\n    return \"\\n\".join(lines)\n\n\n# ── Main ─────────────────────────────────────────────────────────────\n\ndef parse_args():\n    p = argparse.ArgumentParser(\n        description=\"C2 n=500 Median Bootstrap Analysis (D054-compliant)\"\n    )\n    p.add_argument(\n        \"--base-dir\", type=str, default=\"/root/autodl-tmp/pacs\",\n        help=\"Base directory containing profiling_output_* dirs\"\n    )\n    p.add_argument(\n        \"--output-dir\", type=str, default=None,\n        help=\"Output directory (default: {base-dir}/analysis_output)\"\n    )\n    p.add_argument(\n        \"--model\", type=str, default=None, choices=[\"deepseek\", \"qwen\"],\n        help=\"Analyze one model only (default: both)\"\n    )\n    p.add_argument(\n        \"--n50-only\", action=\"store_true\",\n        help=\"Dry-run using n=50 reference data\"\n    )\n    p.add_argument(\n        \"--bootstrap\", type=int, default=B_BOOTSTRAP,\n        help=f\"Number of bootstrap resamples (default: {B_BOOTSTRAP})\"\n    )\n    return p.parse_args()\n\n\ndef main():\n    args = parse_args()\n    base = Path(args.base_dir)\n    out_dir = Path(args.output_dir) if args.output_dir else base / \"analysis_output\"\n    out_dir.mkdir(parents=True, exist_ok=True)\n\n    global B_BOOTSTRAP\n    B_BOOTSTRAP = args.bootstrap\n\n    n500 = not args.n50_only\n    expected_n = 500 if n500 else 50\n    data_tag = \"n=500\" if n500 else \"n=50 (dry-run)\"\n\n    models_to_run = {k: v for k, v in MODELS.items() if args.model is None or k == args.model}\n\n    print(f\"C2 n=500 Analysis (D054: median primary)\")\n    print(f\"  Base: {base}\")\n    print(f\"  Data: {data_tag}\")\n    print(f\"  Models: {list(models_to_run.keys())}\")\n    print(f\"  Bootstrap: {B_BOOTSTRAP} resamples\")\n    print()\n\n    # 1. Load data\n    all_data = {}\n    missing = []\n    for model_name, ms in models_to_run.items():\n        for method in METHODS:\n            for sl in SPARSITY_LABELS:\n                key = f\"{ms}_{method}_{sl}\"\n                dpath = result_dir(base, ms, method, sl, n500)\n                data = load_json(dpath)\n                if data:\n                    all_data[key] = data\n                    print(f\"  Loaded: {key} ({dpath.name})\")\n                else:\n                    missing.append(key)\n                    print(f\"  MISSING: {key} ({dpath.name})\")\n\n    print(f\"\\n  Loaded {len(all_data)}/{len(all_data) + len(missing)} conditions\")\n    if missing:\n        print(f\"  Missing: {missing}\")\n    print()\n\n    if not all_data:\n        print(\"ERROR: No data loaded. Exiting.\")\n        sys.exit(1)\n\n    # 2. Integrity checks\n    print(\"=\" * 70)\n    print(\"DATA INTEGRITY\")\n    print(\"=\" * 70)\n    integrity_reports = []\n    for key, data in sorted(all_data.items()):\n        r = check_integrity(data, expected_n, key)\n        problems = get_problems(data)\n        r[\"actual_n\"] = len(problems) if problems else 0\n        integrity_reports.append(r)\n        status_str = f\"[{r['status']}]\"\n        print(f\"  {key}: {status_str:10s} n={r['actual_n']}\")\n        for w in r[\"warnings\"]:\n            print(f\"    WARN: {w}\")\n        for e in r[\"errors\"]:\n            print(f\"    ERROR: {e}\")\n    print()\n\n    has_errors = any(r[\"status\"] == \"ERROR\" for r in integrity_reports)\n    if has_errors:\n        print(\"WARNING: Integrity errors found. Proceeding with available data.\\n\")\n\n    # 3. Per-condition statistics\n    print(\"=\" * 70)\n    print(\"PER-CONDITION STATISTICS (D = ii_low - ii_high)\")\n    print(\"=\" * 70)\n    all_results = {}\n    for key, data in sorted(all_data.items()):\n        problems = get_problems(data)\n        if problems:\n            result = analyze_condition(problems)\n            all_results[key] = result\n            if \"error\" not in result:\n                md = result[\"median_diff\"]\n                pg = result[\"phase_gradient\"]\n                w = result[\"wilcoxon\"]\n                cross = \" [CI CROSSES 0]\" if md[\"ci_crosses_zero\"] else \"\"\n                print(f\"  {key}: median={md['value']:+.4f} CI=[{md['ci'][0]:.4f},{md['ci'][1]:.4f}]{cross}\"\n                      f\"  d_z={pg['d_z']:.3f}({pg['d_z_interpretation']})  p={w['p_value']:.4f}\"\n                      f\"  skew={result['skewness']:.1f}\")\n            else:\n                print(f\"  {key}: {result['error']}\")\n        else:\n            all_results[key] = {\"error\": \"no per_problem_ii data\"}\n            print(f\"  {key}: no data\")\n    print()\n\n    # 4. Paired imp vs rand\n    print(\"=\" * 70)\n    print(\"PAIRED: IMPORTANCE vs RANDOM (same questions)\")\n    print(\"=\" * 70)\n    paired = {}\n    for model_name, ms in models_to_run.items():\n        for sl in SPARSITY_LABELS:\n            imp_key = f\"{ms}_imp_{sl}\"\n            rand_key = f\"{ms}_rand_{sl}\"\n            pair_key = f\"{ms}_{sl}\"\n            if imp_key in all_data and rand_key in all_data:\n                imp_probs = get_problems(all_data[imp_key])\n                rand_probs = get_problems(all_data[rand_key])\n                if imp_probs and rand_probs:\n                    p = paired_imp_vs_rand(imp_probs, rand_probs)\n                    paired[pair_key] = p\n                    if \"error\" not in p:\n                        md = p[\"median_diff\"]\n                        print(f\"  {pair_key}: n={p['n_paired']} median(imp-rand)={md['value']:+.4f}\"\n                              f\"  CI=[{md['ci'][0]:.4f},{md['ci'][1]:.4f}]\"\n                              f\"  d_z={p['d_z']:.3f}  p={p['wilcoxon_p']:.4f}\")\n                    else:\n                        print(f\"  {pair_key}: {p['error']}\")\n            else:\n                avail = []\n                if imp_key not in all_data:\n                    avail.append(f\"missing {imp_key}\")\n                if rand_key not in all_data:\n                    avail.append(f\"missing {rand_key}\")\n                paired[pair_key] = {\"error\": \", \".join(avail)}\n                print(f\"  {pair_key}: {paired[pair_key]['error']}\")\n    print()\n\n    # 5. Pre-registration: Qwen s015 CI crosses zero?\n    preregistration = {}\n    qw_s015_key = \"qw_imp_s015\"\n    if qw_s015_key in all_results and \"error\" not in all_results[qw_s015_key]:\n        r = all_results[qw_s015_key]\n        md = r[\"median_diff\"]\n        w = r[\"wilcoxon\"]\n        pg = r[\"phase_gradient\"]\n        verdict = \"threshold_s020\" if md[\"ci_crosses_zero\"] else \"effect_at_s015\"\n        preregistration[\"qwen_s015\"] = {\n            \"median_diff\": md[\"value\"],\n            \"median_ci_lo\": md[\"ci\"][0],\n            \"median_ci_hi\": md[\"ci\"][1],\n            \"crosses_zero\": md[\"ci_crosses_zero\"],\n            \"d_z\": pg[\"d_z\"],\n            \"d_z_ci\": pg[\"d_z_ci\"],\n            \"wilcoxon_p\": w[\"p_value\"],\n            \"verdict\": verdict,\n        }\n        print(\"=\" * 70)\n        print(\"PRE-REGISTRATION VERDICT: Qwen s015\")\n        print(\"=\" * 70)\n        print(f\"  Median diff = {md['value']:.6f}\")\n        print(f\"  Median 95% CI = [{md['ci'][0]:.4f}, {md['ci'][1]:.4f}]\")\n        print(f\"  CI crosses zero: {md['ci_crosses_zero']}\")\n        if md[\"ci_crosses_zero\"]:\n            print(\"  -> VERDICT: Change narrative to threshold ~s020\")\n        else:\n            print(\"  -> VERDICT: Compound effect confirmed at s015\")\n        print()\n\n    # 6. Generate markdown report\n    metadata = {\n        \"data_source\": data_tag,\n        \"n_bootstrap\": B_BOOTSTRAP,\n        \"seed\": SEED,\n        \"missing_conditions\": missing,\n        \"timestamp\": datetime.now().isoformat(),\n    }\n    report = format_report(all_results, paired, integrity_reports, preregistration, metadata)\n\n    # 7. Save outputs\n    suffix = \"_dryrun\" if args.n50_only else \"\"\n\n    results_path = out_dir / f\"c2_n500_results{suffix}.json\"\n    with open(results_path, \"w\") as f:\n        json.dump({\n            \"conditions\": {k: _sanitize(v) for k, v in all_results.items()},\n            \"paired_imp_vs_rand\": {k: _sanitize(v) for k, v in paired.items()},\n            \"preregistration\": preregistration,\n            \"integrity\": [_sanitize(r) for r in integrity_reports],\n            \"metadata\": metadata,\n        }, f, indent=2)\n    print(f\"Saved results: {results_path}\")\n\n    report_path = out_dir / f\"c2_n500_report{suffix}.md\"\n    with open(report_path, \"w\") as f:\n        f.write(report)\n    print(f\"Saved report: {report_path}\")\n\n    print(f\"\\nDone. {len(all_results)} conditions analyzed.\")\n\n\ndef _sanitize(obj):\n    if isinstance(obj, dict):\n        return {k: _sanitize(v) for k, v in obj.items()}\n    if isinstance(obj, list):\n        return [_sanitize(v) for v in obj]\n    if isinstance(obj, (np.integer,)):\n        return int(obj)\n    if isinstance(obj, (np.floating,)):\n        return float(obj)\n    if isinstance(obj, np.ndarray):\n        return obj.tolist()\n    if isinstance(obj, (np.bool_,)):\n        return bool(obj)\n    return obj\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT_EOF",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_c2_n500_analysis_prep_20260514T184028",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-22162",
    "command": "cat > /root/autodl-tmp/pacs/scripts/analyze_c2_n500.py << 'SCRIPT_EOF'\n\"\"\"\nC2 n=500 Median Bootstrap Analysis (D054-compliant).\n\nPrimary metric: median II + median bootstrap 95% CI (not mean).\nReason: DeepSeek II skewness ~9.5, mean unreliable.\n\nInput:  {base}/profiling_output_n500_bf16_{ds,qw}_{imp,rand}_s{015,020,025,030}/profiling_results.json\nOutput: {out}/c2_n500_results.json, {out}/c2_n500_report.md\n\nUsage:\n  python scripts/analyze_c2_n500.py\n  python scripts/analyze_c2_n500.py --base-dir /root/autodl-tmp/pacs --output-dir ./analysis_output\n  python scripts/analyze_c2_n500.py --model deepseek\n  python scripts/analyze_c2_n500.py --n50-only          # dry-run with n=50 reference data\n\"\"\"\n\nimport argparse\nimport json\nimport sys\nfrom collections import Counter\nfrom datetime import datetime\nfrom pathlib import Path\nfrom typing import Any, Dict, List, Optional, Tuple\n\nimport numpy as np\nfrom scipy import stats\n\n# ── Constants ────────────────────────────────────────────────────────\n\nMODELS = {\"deepseek\": \"ds\", \"qwen\": \"qw\"}\nMETHODS = [\"imp\", \"rand\"]\nSPARSITY_LABELS = [\"s015\", \"s020\", \"s025\", \"s030\"]\nSPARSITY_VALUES = {\"s015\": 0.15, \"s020\": 0.20, \"s025\": 0.25, \"s030\": 0.30}\nSPARSITY_KEYS = {\"s015\": \"0.15\", \"s020\": \"0.2\", \"s025\": \"0.25\", \"s030\": \"0.3\"}\nPHASES = [\"high\", \"mid\", \"low\"]\n\nB_BOOTSTRAP = 10000\nSEED = 42\nALPHA = 0.05\nN_BONFERRONI = 4  # 4 sparsity levels per model\n\n\n# ── Path helpers ─────────────────────────────────────────────────────\n\ndef result_dir(base: Path, model_short: str, method: str, slabel: str, n500: bool) -> Path:\n    prefix = \"n500_bf16\" if n500 else \"bf16\"\n    return base / f\"profiling_output_{prefix}_{model_short}_{method}_{slabel}\"\n\n\ndef load_json(dirpath: Path) -> Optional[dict]:\n    fpath = dirpath / \"profiling_results.json\"\n    if not fpath.exists():\n        return None\n    with open(fpath) as f:\n        return json.load(f)\n\n\ndef get_problems(data: dict) -> Optional[List[dict]]:\n    ppi = data.get(\"per_problem_ii\", {})\n    levels = list(ppi.keys())\n    if not levels:\n        return None\n    return ppi[levels[0]]\n\n\n# ── Data integrity ───────────────────────────────────────────────────\n\ndef check_integrity(data: dict, expected_n: int, label: str) -> dict:\n    report = {\"label\": label, \"status\": \"OK\", \"warnings\": [], \"errors\": []}\n\n    config_n = data.get(\"config\", {}).get(\"n_problems\", None)\n    problems = get_problems(data)\n    if not problems:\n        report[\"status\"] = \"ERROR\"\n        report[\"errors\"].append(\"No per_problem_ii data found\")\n        return report\n\n    actual_n = len(problems)\n\n    if actual_n != expected_n:\n        report[\"errors\"].append(f\"Expected {expected_n} problems, got {actual_n}\")\n        report[\"status\"] = \"ERROR\"\n\n    if config_n is not None and config_n != expected_n:\n        report[\"warnings\"].append(f\"Config n_problems={config_n}, expected {expected_n}\")\n\n    # problem_idx monotonicity\n    indices = [p[\"problem_idx\"] for p in problems]\n    non_monotonic = []\n    for i in range(1, len(indices)):\n        if indices[i] <= indices[i - 1]:\n            non_monotonic.append((i, indices[i - 1], indices[i]))\n    if non_monotonic:\n        if report[\"status\"] == \"OK\":\n            report[\"status\"] = \"WARNING\"\n        report[\"warnings\"].append(\n            f\"Non-monotonic problem_idx at {len(non_monotonic)} positions \"\n            f\"(first: pos {non_monotonic[0][0]}, \"\n            f\"{non_monotonic[0][1]} -> {non_monotonic[0][2]}). \"\n            f\"Possible duplicate-process contamination.\"\n        )\n\n    # duplicate problem_id\n    pids = [p[\"problem_id\"] for p in problems]\n    pid_counts = Counter(pids)\n    duplicates = {k: v for k, v in pid_counts.items() if v > 1}\n    if duplicates:\n        report[\"status\"] = \"ERROR\"\n        report[\"errors\"].append(\n            f\"Duplicate problem_ids: {len(duplicates)} IDs appear >1 time. \"\n            f\"First: {list(duplicates.items())[:3]}\"\n        )\n\n    # NaN/None in II values\n    nan_count = sum(1 for p in problems if p.get(\"ii_low\") is None or p.get(\"ii_high\") is None)\n    if nan_count > 0:\n        report[\"warnings\"].append(f\"{nan_count}/{actual_n} problems have null ii_high or ii_low\")\n        if nan_count > actual_n * 0.1:\n            report[\"status\"] = \"WARNING\"\n\n    # Check for null ii_mid (informational)\n    mid_null = sum(1 for p in problems if p.get(\"ii_mid\") is None)\n    if mid_null > 0:\n        report[\"warnings\"].append(f\"{mid_null}/{actual_n} problems have null ii_mid\")\n\n    return report\n\n\n# ── Statistical functions ────────────────────────────────────────────\n\ndef bootstrap_median_ci(values: np.ndarray, B: int = B_BOOTSTRAP, alpha: float = ALPHA, seed: int = SEED) -> Tuple[float, float]:\n    rng = np.random.RandomState(seed)\n    n = len(values)\n    boot = np.array([np.median(values[rng.randint(0, n, size=n)]) for _ in range(B)])\n    return float(np.percentile(boot, 100 * alpha / 2)), float(np.percentile(boot, 100 * (1 - alpha / 2)))\n\n\ndef bootstrap_mean_ci(values: np.ndarray, B: int = B_BOOTSTRAP, alpha: float = ALPHA, seed: int = SEED) -> Tuple[float, float]:\n    rng = np.random.RandomState(seed)\n    n = len(values)\n    boot = np.array([np.mean(values[rng.randint(0, n, size=n)]) for _ in range(B)])\n    return float(np.percentile(boot, 100 * alpha / 2)), float(np.percentile(boot, 100 * (1 - alpha / 2)))\n\n\ndef bootstrap_dz_ci(diffs: np.ndarray, B: int = B_BOOTSTRAP, alpha: float = ALPHA, seed: int = SEED) -> Tuple[float, float]:\n    rng = np.random.RandomState(seed)\n    n = len(diffs)\n    boot = np.empty(B)\n    for i in range(B):\n        sample = diffs[rng.randint(0, n, size=n)]\n        s = sample.std(ddof=1)\n        boot[i] = sample.mean() / s if s > 0 else np.nan\n    boot = boot[~np.isnan(boot)]\n    if len(boot) == 0:\n        return float(\"nan\"), float(\"nan\")\n    return float(np.percentile(boot, 100 * alpha / 2)), float(np.percentile(boot, 100 * (1 - alpha / 2)))\n\n\ndef paired_cohens_dz(diffs: np.ndarray) -> float:\n    if len(diffs) < 2:\n        return float(\"nan\")\n    s = np.std(diffs, ddof=1)\n    if s == 0:\n        return float(\"nan\")\n    return float(np.mean(diffs) / s)\n\n\ndef wilcoxon_test(diffs: np.ndarray, alternative: str = \"two-sided\") -> Tuple[float, float]:\n    nonzero = diffs[diffs != 0]\n    if len(nonzero) < 10:\n        return float(\"nan\"), float(\"nan\")\n    stat, p = stats.wilcoxon(nonzero, alternative=alternative)\n    return float(stat), float(p)\n\n\ndef interpret_d(d: float) -> str:\n    ad = abs(d)\n    if ad < 0.2:\n        return \"negligible\"\n    elif ad < 0.5:\n        return \"small\"\n    elif ad < 0.8:\n        return \"medium\"\n    return \"large\"\n\n\n# ── Per-condition analysis ───────────────────────────────────────────\n\ndef analyze_condition(problems: List[dict]) -> dict:\n    \"\"\"Full analysis for one condition. Phase gradient: D = ii_low - ii_high.\"\"\"\n    ii_low = []\n    ii_high = []\n    ii_mid = []\n    valid_idx = []\n\n    for i, p in enumerate(problems):\n        vl = p.get(\"ii_low\")\n        vh = p.get(\"ii_high\")\n        if vl is not None and vh is not None:\n            ii_low.append(vl)\n            ii_high.append(vh)\n            valid_idx.append(i)\n        vm = p.get(\"ii_mid\")\n        if vm is not None:\n            ii_mid.append(vm)\n\n    ii_low = np.array(ii_low)\n    ii_high = np.array(ii_high)\n    ii_mid = np.array(ii_mid) if ii_mid else np.array([])\n\n    diffs = ii_low - ii_high  # phase gradient: D per problem\n    n_valid = len(diffs)\n    n_total = len(problems)\n    n_skipped = n_total - n_valid\n\n    if n_valid < 10:\n        return {\"error\": f\"Too few valid problems ({n_valid})\", \"n_valid\": n_valid, \"n_total\": n_total}\n\n    # Primary metric: median + median bootstrap CI (D054)\n    median_diff = float(np.median(diffs))\n    median_ci = bootstrap_median_ci(diffs)\n    ci_crosses_zero = (median_ci[0] <= 0 <= median_ci[1])\n\n    # Reference: mean + mean bootstrap CI\n    mean_diff = float(np.mean(diffs))\n    std_diff = float(np.std(diffs, ddof=1))\n    mean_ci = bootstrap_mean_ci(diffs)\n\n    # Cohen's d_z (paired)\n    d_z = paired_cohens_dz(diffs)\n    d_z_ci = bootstrap_dz_ci(diffs)\n\n    # Wilcoxon signed-rank\n    w_stat, w_p = wilcoxon_test(diffs, alternative=\"two-sided\")\n    w_p_bonf = min(w_p * N_BONFERRONI, 1.0) if not np.isnan(w_p) else float(\"nan\")\n\n    # Skewness\n    skew = float(stats.skew(diffs))\n\n    # Per-phase medians (for reporting)\n    phase_medians = {}\n    for name, arr in [(\"low\", ii_low), (\"high\", ii_high), (\"mid\", ii_mid)]:\n        if len(arr) > 0:\n            med = float(np.median(arr))\n            ci = bootstrap_median_ci(arr)\n            phase_medians[name] = {\"median\": med, \"ci\": list(ci), \"n\": len(arr)}\n\n    return {\n        \"n_valid\": n_valid,\n        \"n_total\": n_total,\n        \"n_skipped\": n_skipped,\n        \"median_diff\": {\n            \"value\": median_diff,\n            \"ci\": list(median_ci),\n            \"ci_crosses_zero\": ci_crosses_zero,\n        },\n        \"mean_diff\": {\n            \"value\": mean_diff,\n            \"std\": std_diff,\n            \"ci\": list(mean_ci),\n        },\n        \"phase_gradient\": {\n            \"d_z\": d_z,\n            \"d_z_ci\": list(d_z_ci),\n            \"d_z_interpretation\": interpret_d(d_z),\n        },\n        \"wilcoxon\": {\n            \"stat\": w_stat,\n            \"p_value\": w_p,\n            \"p_bonferroni\": w_p_bonf,\n            \"significant_bonf_005\": bool(w_p_bonf < 0.05) if not np.isnan(w_p_bonf) else None,\n        },\n        \"skewness\": skew,\n        \"phase_medians\": phase_medians,\n    }\n\n\n# ── Paired imp vs rand ──────────────────────────────────────────────\n\ndef paired_imp_vs_rand(imp_problems: List[dict], rand_problems: List[dict]) -> dict:\n    \"\"\"Compare imp vs rand for the same questions (paired by problem_id).\"\"\"\n    imp_by_id = {}\n    for p in imp_problems:\n        vl, vh = p.get(\"ii_low\"), p.get(\"ii_high\")\n        if vl is not None and vh is not None:\n            imp_by_id[p[\"problem_id\"]] = vl - vh\n\n    rand_by_id = {}\n    for p in rand_problems:\n        vl, vh = p.get(\"ii_low\"), p.get(\"ii_high\")\n        if vl is not None and vh is not None:\n            rand_by_id[p[\"problem_id\"]] = vl - vh\n\n    common = sorted(set(imp_by_id.keys()) & set(rand_by_id.keys()))\n    if len(common) < 10:\n        return {\"error\": f\"Too few common problems ({len(common)})\"}\n\n    imp_vals = np.array([imp_by_id[pid] for pid in common])\n    rand_vals = np.array([rand_by_id[pid] for pid in common])\n    diffs = imp_vals - rand_vals  # D = gradient_imp - gradient_rand\n\n    median_diff = float(np.median(diffs))\n    median_ci = bootstrap_median_ci(diffs)\n    mean_diff = float(np.mean(diffs))\n    d_z = paired_cohens_dz(diffs)\n    d_z_ci = bootstrap_dz_ci(diffs)\n    w_stat, w_p = wilcoxon_test(diffs)\n\n    return {\n        \"n_paired\": len(common),\n        \"median_diff\": {\n            \"value\": median_diff,\n            \"ci\": list(median_ci),\n            \"ci_crosses_zero\": (median_ci[0] <= 0 <= median_ci[1]),\n        },\n        \"mean_diff\": mean_diff,\n        \"d_z\": d_z,\n        \"d_z_ci\": list(d_z_ci),\n        \"d_z_interpretation\": interpret_d(d_z),\n        \"wilcoxon_p\": w_p,\n    }\n\n\n# ── Markdown report ──────────────────────────────────────────────────\n\ndef format_report(all_results: dict, paired: dict, integrity: list,\n                  preregistration: dict, metadata: dict) -> str:\n    lines = []\n    lines.append(\"# C2 n=500 Median Bootstrap Analysis (D054)\")\n    lines.append(\"\")\n    lines.append(f\"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\")\n    lines.append(f\"Data source: {metadata.get('data_source', 'n=500')}\")\n    lines.append(f\"Bootstrap resamples: {B_BOOTSTRAP}, seed: {SEED}\")\n    lines.append(f\"**Primary metric: MEDIAN** (mean provided as reference only)\")\n    lines.append(\"\")\n\n    # Integrity\n    lines.append(\"## Data Integrity\")\n    lines.append(\"\")\n    for r in integrity:\n        status = r[\"status\"]\n        icon = \"OK\" if status == \"OK\" else (\"WARN\" if status == \"WARNING\" else \"ERR\")\n        lines.append(f\"- `{r['label']}`: [{icon}] n={r.get('actual_n', '?')}\")\n        for w in r.get(\"warnings\", []):\n            lines.append(f\"  - Warning: {w}\")\n        for e in r.get(\"errors\", []):\n            lines.append(f\"  - **Error: {e}**\")\n    lines.append(\"\")\n\n    # Per-condition table\n    lines.append(\"## Phase Gradient by Condition (D = ii_low - ii_high)\")\n    lines.append(\"\")\n    lines.append(\"| Condition | n | Median D | Median 95% CI | CI crosses 0? | Mean D | d_z | Wilcoxon p | Skew |\")\n    lines.append(\"|-----------|---|----------|---------------|---------------|--------|-----|------------|------|\")\n    for key in sorted(all_results.keys()):\n        r = all_results[key]\n        if \"error\" in r:\n            lines.append(f\"| {key} | - | ERROR: {r['error']} | | | | | | |\")\n            continue\n        md = r[\"median_diff\"]\n        mn = r[\"mean_diff\"]\n        pg = r[\"phase_gradient\"]\n        w = r[\"wilcoxon\"]\n        cross = \"YES\" if md[\"ci_crosses_zero\"] else \"no\"\n        sig = \"\"\n        if w.get(\"significant_bonf_005\"):\n            sig = \" *\"\n        lines.append(\n            f\"| {key} | {r['n_valid']} | {md['value']:.4f} | \"\n            f\"[{md['ci'][0]:.4f}, {md['ci'][1]:.4f}] | {cross} | \"\n            f\"{mn['value']:.4f} | {pg['d_z']:.3f} ({pg['d_z_interpretation']}) | \"\n            f\"{w['p_value']:.4f}{sig} | {r['skewness']:.1f} |\"\n        )\n    lines.append(\"\")\n\n    # Paired imp vs rand\n    lines.append(\"## Importance vs Random (paired by problem_id)\")\n    lines.append(\"\")\n    lines.append(\"| Sparsity | n_paired | Median(imp-rand) | Median 95% CI | d_z | Wilcoxon p |\")\n    lines.append(\"|----------|----------|------------------|---------------|-----|------------|\")\n    for key in sorted(paired.keys()):\n        p = paired[key]\n        if \"error\" in p:\n            lines.append(f\"| {key} | - | {p['error']} | | | |\")\n            continue\n        md = p[\"median_diff\"]\n        lines.append(\n            f\"| {key} | {p['n_paired']} | {md['value']:.4f} | \"\n            f\"[{md['ci'][0]:.4f}, {md['ci'][1]:.4f}] | \"\n            f\"{p['d_z']:.3f} ({p['d_z_interpretation']}) | {p['wilcoxon_p']:.4f} |\"\n        )\n    lines.append(\"\")\n\n    # Pre-registration verdict\n    if preregistration:\n        lines.append(\"## Pre-registration Verdict\")\n        lines.append(\"\")\n        for key, v in preregistration.items():\n            lines.append(f\"### {key}\")\n            lines.append(f\"- Median diff = {v['median_diff']:.6f}\")\n            lines.append(f\"- Median 95% CI = [{v['median_ci_lo']:.4f}, {v['median_ci_hi']:.4f}]\")\n            lines.append(f\"- CI crosses zero: **{v['crosses_zero']}**\")\n            lines.append(f\"- Wilcoxon p = {v['wilcoxon_p']:.4f}\")\n            lines.append(f\"- **Verdict: {v['verdict']}**\")\n            lines.append(\"\")\n\n    return \"\\n\".join(lines)\n\n\n# ── Main ─────────────────────────────────────────────────────────────\n\ndef parse_args():\n    p = argparse.ArgumentParser(\n        description=\"C2 n=500 Median Bootstrap Analysis (D054-compliant)\"\n    )\n    p.add_argument(\n        \"--base-dir\", type=str, default=\"/root/autodl-tmp/pacs\",\n        help=\"Base directory containing profiling_output_* dirs\"\n    )\n    p.add_argument(\n        \"--output-dir\", type=str, default=None,\n        help=\"Output directory (default: {base-dir}/analysis_output)\"\n    )\n    p.add_argument(\n        \"--model\", type=str, default=None, choices=[\"deepseek\", \"qwen\"],\n        help=\"Analyze one model only (default: both)\"\n    )\n    p.add_argument(\n        \"--n50-only\", action=\"store_true\",\n        help=\"Dry-run using n=50 reference data\"\n    )\n    p.add_argument(\n        \"--bootstrap\", type=int, default=B_BOOTSTRAP,\n        help=f\"Number of bootstrap resamples (default: {B_BOOTSTRAP})\"\n    )\n    return p.parse_args()\n\n\ndef main():\n    args = parse_args()\n    base = Path(args.base_dir)\n    out_dir = Path(args.output_dir) if args.output_dir else base / \"analysis_output\"\n    out_dir.mkdir(parents=True, exist_ok=True)\n\n    global B_BOOTSTRAP\n    B_BOOTSTRAP = args.bootstrap\n\n    n500 = not args.n50_only\n    expected_n = 500 if n500 else 50\n    data_tag = \"n=500\" if n500 else \"n=50 (dry-run)\"\n\n    models_to_run = {k: v for k, v in MODELS.items() if args.model is None or k == args.model}\n\n    print(f\"C2 n=500 Analysis (D054: median primary)\")\n    print(f\"  Base: {base}\")\n    print(f\"  Data: {data_tag}\")\n    print(f\"  Models: {list(models_to_run.keys())}\")\n    print(f\"  Bootstrap: {B_BOOTSTRAP} resamples\")\n    print()\n\n    # 1. Load data\n    all_data = {}\n    missing = []\n    for model_name, ms in models_to_run.items():\n        for method in METHODS:\n            for sl in SPARSITY_LABELS:\n                key = f\"{ms}_{method}_{sl}\"\n                dpath = result_dir(base, ms, method, sl, n500)\n                data = load_json(dpath)\n                if data:\n                    all_data[key] = data\n                    print(f\"  Loaded: {key} ({dpath.name})\")\n                else:\n                    missing.append(key)\n                    print(f\"  MISSING: {key} ({dpath.name})\")\n\n    print(f\"\\n  Loaded {len(all_data)}/{len(all_data) + len(missing)} conditions\")\n    if missing:\n        print(f\"  Missing: {missing}\")\n    print()\n\n    if not all_data:\n        print(\"ERROR: No data loaded. Exiting.\")\n        sys.exit(1)\n\n    # 2. Integrity checks\n    print(\"=\" * 70)\n    print(\"DATA INTEGRITY\")\n    print(\"=\" * 70)\n    integrity_reports = []\n    for key, data in sorted(all_data.items()):\n        r = check_integrity(data, expected_n, key)\n        problems = get_problems(data)\n        r[\"actual_n\"] = len(problems) if problems else 0\n        integrity_reports.append(r)\n        status_str = f\"[{r['status']}]\"\n        print(f\"  {key}: {status_str:10s} n={r['actual_n']}\")\n        for w in r[\"warnings\"]:\n            print(f\"    WARN: {w}\")\n        for e in r[\"errors\"]:\n            print(f\"    ERROR: {e}\")\n    print()\n\n    has_errors = any(r[\"status\"] == \"ERROR\" for r in integrity_reports)\n    if has_errors:\n        print(\"WARNING: Integrity errors found. Proceeding with available data.\\n\")\n\n    # 3. Per-condition statistics\n    print(\"=\" * 70)\n    print(\"PER-CONDITION STATISTICS (D = ii_low - ii_high)\")\n    print(\"=\" * 70)\n    all_results = {}\n    for key, data in sorted(all_data.items()):\n        problems = get_problems(data)\n        if problems:\n            result = analyze_condition(problems)\n            all_results[key] = result\n            if \"error\" not in result:\n                md = result[\"median_diff\"]\n                pg = result[\"phase_gradient\"]\n                w = result[\"wilcoxon\"]\n                cross = \" [CI CROSSES 0]\" if md[\"ci_crosses_zero\"] else \"\"\n                print(f\"  {key}: median={md['value']:+.4f} CI=[{md['ci'][0]:.4f},{md['ci'][1]:.4f}]{cross}\"\n                      f\"  d_z={pg['d_z']:.3f}({pg['d_z_interpretation']})  p={w['p_value']:.4f}\"\n                      f\"  skew={result['skewness']:.1f}\")\n            else:\n                print(f\"  {key}: {result['error']}\")\n        else:\n            all_results[key] = {\"error\": \"no per_problem_ii data\"}\n            print(f\"  {key}: no data\")\n    print()\n\n    # 4. Paired imp vs rand\n    print(\"=\" * 70)\n    print(\"PAIRED: IMPORTANCE vs RANDOM (same questions)\")\n    print(\"=\" * 70)\n    paired = {}\n    for model_name, ms in models_to_run.items():\n        for sl in SPARSITY_LABELS:\n            imp_key = f\"{ms}_imp_{sl}\"\n            rand_key = f\"{ms}_rand_{sl}\"\n            pair_key = f\"{ms}_{sl}\"\n            if imp_key in all_data and rand_key in all_data:\n                imp_probs = get_problems(all_data[imp_key])\n                rand_probs = get_problems(all_data[rand_key])\n                if imp_probs and rand_probs:\n                    p = paired_imp_vs_rand(imp_probs, rand_probs)\n                    paired[pair_key] = p\n                    if \"error\" not in p:\n                        md = p[\"median_diff\"]\n                        print(f\"  {pair_key}: n={p['n_paired']} median(imp-rand)={md['value']:+.4f}\"\n                              f\"  CI=[{md['ci'][0]:.4f},{md['ci'][1]:.4f}]\"\n                              f\"  d_z={p['d_z']:.3f}  p={p['wilcoxon_p']:.4f}\")\n                    else:\n                        print(f\"  {pair_key}: {p['error']}\")\n            else:\n                avail = []\n                if imp_key not in all_data:\n                    avail.append(f\"missing {imp_key}\")\n                if rand_key not in all_data:\n                    avail.append(f\"missing {rand_key}\")\n                paired[pair_key] = {\"error\": \", \".join(avail)}\n                print(f\"  {pair_key}: {paired[pair_key]['error']}\")\n    print()\n\n    # 5. Pre-registration: Qwen s015 CI crosses zero?\n    preregistration = {}\n    qw_s015_key = \"qw_imp_s015\"\n    if qw_s015_key in all_results and \"error\" not in all_results[qw_s015_key]:\n        r = all_results[qw_s015_key]\n        md = r[\"median_diff\"]\n        w = r[\"wilcoxon\"]\n        pg = r[\"phase_gradient\"]\n        verdict = \"threshold_s020\" if md[\"ci_crosses_zero\"] else \"effect_at_s015\"\n        preregistration[\"qwen_s015\"] = {\n            \"median_diff\": md[\"value\"],\n            \"median_ci_lo\": md[\"ci\"][0],\n            \"median_ci_hi\": md[\"ci\"][1],\n            \"crosses_zero\": md[\"ci_crosses_zero\"],\n            \"d_z\": pg[\"d_z\"],\n            \"d_z_ci\": pg[\"d_z_ci\"],\n            \"wilcoxon_p\": w[\"p_value\"],\n            \"verdict\": verdict,\n        }\n        print(\"=\" * 70)\n        print(\"PRE-REGISTRATION VERDICT: Qwen s015\")\n        print(\"=\" * 70)\n        print(f\"  Median diff = {md['value']:.6f}\")\n        print(f\"  Median 95% CI = [{md['ci'][0]:.4f}, {md['ci'][1]:.4f}]\")\n        print(f\"  CI crosses zero: {md['ci_crosses_zero']}\")\n        if md[\"ci_crosses_zero\"]:\n            print(\"  -> VERDICT: Change narrative to threshold ~s020\")\n        else:\n            print(\"  -> VERDICT: Compound effect confirmed at s015\")\n        print()\n\n    # 6. Generate markdown report\n    metadata = {\n        \"data_source\": data_tag,\n        \"n_bootstrap\": B_BOOTSTRAP,\n        \"seed\": SEED,\n        \"missing_conditions\": missing,\n        \"timestamp\": datetime.now().isoformat(),\n    }\n    report = format_report(all_results, paired, integrity_reports, preregistration, metadata)\n\n    # 7. Save outputs\n    suffix = \"_dryrun\" if args.n50_only else \"\"\n\n    results_path = out_dir / f\"c2_n500_results{suffix}.json\"\n    with open(results_path, \"w\") as f:\n        json.dump({\n            \"conditions\": {k: _sanitize(v) for k, v in all_results.items()},\n            \"paired_imp_vs_rand\": {k: _sanitize(v) for k, v in paired.items()},\n            \"preregistration\": preregistration,\n            \"integrity\": [_sanitize(r) for r in integrity_reports],\n            \"metadata\": metadata,\n        }, f, indent=2)\n    print(f\"Saved results: {results_path}\")\n\n    report_path = out_dir / f\"c2_n500_report{suffix}.md\"\n    with open(report_path, \"w\") as f:\n        f.write(report)\n    print(f\"Saved report: {report_path}\")\n\n    print(f\"\\nDone. {len(all_results)} conditions analyzed.\")\n\n\ndef _sanitize(obj):\n    if isinstance(obj, dict):\n        return {k: _sanitize(v) for k, v in obj.items()}\n    if isinstance(obj, list):\n        return [_sanitize(v) for v in obj]\n    if isinstance(obj, (np.integer,)):\n        return int(obj)\n    if isinstance(obj, (np.floating,)):\n        return float(obj)\n    if isinstance(obj, np.ndarray):\n        return obj.tolist()\n    if isinstance(obj, (np.bool_,)):\n        return bool(obj)\n    return obj\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT_EOF",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-14T18:44:15.088123+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.54}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_c2_n500_analysis_prep_20260514T184028",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-14T18:44:15.088291+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-22162",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /root/autodl-tmp/pacs/scripts/analyze_c2_n500.py --help",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_c2_n500_analysis_prep_20260514T184028",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-22162",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /root/autodl-tmp/pacs/scripts/analyze_c2_n500.py --help",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-14T18:44:15.088477+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"usage: analyze_c2_n500.py [-h] [--base-dir BASE_DIR] [--output-dir OUTPUT_DIR]\\n                          [--model {deepseek,qwen}] [--n50-only]\\n                          [--bootstrap BOOTSTRAP]\\n\\nC2 n=500 Median Bootstrap Analysis (D054-compliant)\\n\\noptions:\\n  -h, --help            show this help message and exit\\n  --base-dir BASE_DIR   Base directory containing profiling_output_* dirs\\n  --output-dir OUTPUT_DIR\\n                        Output directory (default: {base-dir}/analysis_output)\\n  --model {deepseek,qwen}\\n                        Analyze one model only (default: both)\\n  --n50-only            Dry-run using n=50 reference data\\n  --bootstrap BOOTSTRAP\\n                        Number of bootstrap resamples (default: 10000)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.09}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_c2_n500_analysis_prep_20260514T184028",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-14T18:44:15.088670+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-22162",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /root/autodl-tmp/pacs/scripts/analyze_c2_n500.py --n50-only --bootstrap 1000",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_c2_n500_analysis_prep_20260514T184028",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-22162",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /root/autodl-tmp/pacs/scripts/analyze_c2_n500.py --n50-only --bootstrap 1000",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-14T18:44:15.088861+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"C2 n=500 Analysis (D054: median primary)\\n  Base: /root/autodl-tmp/pacs\\n  Data: n=50 (dry-run)\\n  Models: ['deepseek', 'qwen']\\n  Bootstrap: 1000 resamples\\n\\n  Loaded: ds_imp_s015 (profiling_output_bf16_ds_imp_s015)\\n  Loaded: ds_imp_s020 (profiling_output_bf16_ds_imp_s020)\\n  Loaded: ds_imp_s025 (profiling_output_bf16_ds_imp_s025)\\n  Loaded: ds_imp_s030 (profiling_output_bf16_ds_imp_s030)\\n  Loaded: ds_rand_s015 (profiling_output_bf16_ds_rand_s015)\\n  Loaded: ds_rand_s020 (profiling_output_bf16_ds_rand_s020)\\n  Loaded: ds_rand_s025 (profiling_output_bf16_ds_rand_s025)\\n  Loaded: ds_rand_s030 (profiling_output_bf16_ds_rand_s030)\\n  Loaded: qw_imp_s015 (profiling_output_bf16_qw_imp_s015)\\n  Loaded: qw_imp_s020 (profiling_output_bf16_qw_imp_s020)\\n  Loaded: qw_imp_s025 (profiling_output_bf16_qw_imp_s025)\\n  Loaded: qw_imp_s030 (profiling_output_bf16_qw_imp_s030)\\n  Loaded: qw_rand_s015 (profiling_output_bf16_qw_rand_s015)\\n  Loaded: qw_rand_s020 (profiling_output_bf16_qw_rand_s020)\\n  Loaded: qw_rand_s025 (profiling_output_bf16_qw_rand_s025)\\n  Loaded: qw_rand_s030 (profiling_output_bf16_qw_rand_s030)\\n\\n  Loaded 16/16 conditions\\n\\n======================================================================\\nDATA INTEGRITY\\n======================================================================\\n  ds_imp_s015: [OK]       n=50\\n    WARN: 1/50 problems have null ii_high or ii_low\\n    WARN: 10/50 problems have null ii_mid\\n  ds_imp_s020: [OK]       n=50\\n    WARN: 1/50 problems have null ii_high or ii_low\\n    WARN: 10/50 problems have null ii_mid\\n  ds_imp_s025: [OK]       n=50\\n    WARN: 1/50 problems have null ii_high or ii_low\\n    WARN: 10/50 problems have null ii_mid\\n  ds_imp_s030: [OK]       n=50\\n    WARN: 1/50 problems have null ii_high or ii_low\\n    WARN: 10/50 problems have null ii_mid\\n  ds_rand_s015: [OK]       n=50\\n    WARN: 1/50 problems have null ii_high or ii
…[truncated 4773 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_c2_n500_analysis_prep_20260514T184028",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-14T18:44:15.089053+00:00_

干净通过，16/16 conditions 加载，统计输出正确。

脚本已部署到 `/root/autodl-tmp/pacs/scripts/analyze_c2_n500.py`，dry-run 验证通过。功能：

- **D054 合规**：median + median bootstrap 95% CI 为主指标，mean 仅作参考
- **完整性检查**：n=500 验证、problem_idx 单调性（检测重复进程污染）、duplicate problem_id、null II 统计
- **统计量**：median D, median CI, mean D, Cohen's d_z + CI, Wilcoxon signed-rank (双侧) + Bonferroni 校正
- **paired imp vs rand**：按 problem_id 配对，计算 importance - random 梯度差
- **预注册判断**：自动检查 Qwen s015 CI 是否跨零
- **输出**：`c2_n500_results.json` + `c2_n500_report.md`

实验完成后运行：
```bash
python /root/autodl-tmp/pacs/scripts/analyze_c2_n500.py
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_c2_n500_analysis_prep_20260514T184028"
}
```

</details>

---
