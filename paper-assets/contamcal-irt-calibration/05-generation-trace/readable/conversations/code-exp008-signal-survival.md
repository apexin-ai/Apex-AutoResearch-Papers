# code exp008 signal survival

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 86
- **Recorded user turns:** 0
- **Tool calls:** 43
- **Original source:** `logs/chats/worker_code_exp008_signal_survival_20260514T151627.jsonl`
- **Structured JSON:** [`92962227da5b26d0b6d7.json`](../../sessions/92/92962227da5b26d0b6d7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

86 recorded events

### Tool call

_source line 1 · 2026-05-14T15:21:56.251807+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:TodoWrite",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:TodoWrite",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T15:21:56.252385+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T15:21:56.252742+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'SSH读取exp008/所有4个文件代码', 'status': 'in_progress', 'activeForm': '读取exp008代码文件'}, {'content': '检查exp-002信号输出文件是否存在且非空', 'status': 'pending', 'activeForm': '检查exp-002信号输出'}, {'content': '审查代码：输入路径对齐、逻辑正确性、依赖分析', 'status': 'pending', 'activeForm': '审查代码逻辑和路径'}, {'content': '确认是否纯CPU、是否需要额外输入', 'status': 'pending', 'activeForm': '分析运行依赖'}, {'content': '执行dry-run或准备提交命令', 'status': 'pending', 'activeForm': '执行或准备命令'}, {'content': '汇报结果', 'status': 'pending', 'activeForm': '汇报审查结果'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'SSH读取exp008/所有4个文件代码', 'status': 'in_progress', 'activeForm': '读取exp008代码文件'}, {'content': '检查exp-002信号输出文件是否存在且非空', 'status': 'pending', 'activeForm': '检查exp-002信号输出'}, {'content': '审查代码：输入路径对齐、逻辑正确性、依赖分析', 'status': 'pending', 'activeForm': '审查代码逻辑和路径'}, {'content': '确认是否纯CPU、是否需要额外输入', 'status': 'pending', 'activeForm': '分析运行依赖'}, {'content': '执行dry-run或准备提交命令', 'status': 'pending', 'activeForm': '执行或准备命令'}, {'content': '汇报结果', 'status': 'pending', 'activeForm': '汇报审查结果'}]"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T15:21:56.253090+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T15:21:56.259455+00:00_

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
  "session": "worker_code_exp008_signal_survival_20260514T151627",
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

_source line 6 · 2026-05-14T15:21:56.259753+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T15:21:56.260037+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/contamcal-irt-calibration/exp008/signal_survival_analysis.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/contamcal-irt-calibration/exp008/signal_survival_analysis.py"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T15:21:56.260519+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nexp-008 Signal Survival Analysis — core analysis module.\\nv2: Extended from SFT/RL pairwise to N-regime comparison.\\n\\nComputes:\\n  - AUC matrix: N_signals x N_regimes AUROC for contamination detection\\n  - Pairwise tests: statistical tests between all adjacent regime pairs\\n    (Cohen's d, Spearman rho, AUROC ratio, Wilcoxon signed-rank)\\n\\nInput:  OrderedDict mapping regime_name -> {signal_key: [records]}, plus labels.\\nOutput: {regime_names, auc_matrix, pairwise_tests, per_signal (compat), summary}\\n\\\"\\\"\\\"\\n\\nimport json\\nimport logging\\nfrom collections import OrderedDict\\nfrom pathlib import Path\\n\\nimport numpy as np\\nfrom scipy import stats\\nfrom sklearn.metrics import roc_auc_score\\n\\nlogger = logging.getLogger(__name__)\\n\\nSIGNAL_KEYS = [\\\"s1_embedding\\\", \\\"s2_minkpp\\\", \\\"s3_constat\\\", \\\"s4_selfcritique\\\"]\\nSIGNAL_LABELS = {\\n    \\\"s1_embedding\\\": \\\"Embedding\\\",\\n    \\\"s2_minkpp\\\": \\\"Min-K%++\\\",\\n    \\\"s3_constat\\\": \\\"ConStat\\\",\\n    \\\"s4_selfcritique\\\": \\\"Self-Critique\\\",\\n}\\n\\n\\ndef cohens_d(group1: np.ndarray, group2: np.ndarray) -> float:\\n    \\\"\\\"\\\"Cohen's d effect size between two groups.\\\"\\\"\\\"\\n    n1, n2 = len(group1), len(group2)\\n    if n1 < 2 or n2 < 2:\\n        return float(\\\"nan\\\")\\n    var1 = group1.var(ddof=1)\\n    var2 = group2.var(ddof=1)\\n    pooled_std = np.sqrt(((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2))\\n    if pooled_std == 0:\\n        return float(\\\"nan\\\")\\n    return (group1.mean() - group2.mean()) / pooled_std\\n\\n\\ndef compute_single_regime_metrics(values: np.ndarray, labels: np.ndarray) -> dict:\\n    \\\"\\\"\\\"AUROC and Cohen's d for contamination detection in one regime.\\\"\\\"\\\"\\n    mask = ~(np.isnan(values) | np.isnan(labels))\\n    v = values[mask]\\n    lab = labels[mask].astype(int)\\n    contam = lab == 1\\n    clean = la
…[truncated 7478 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T15:21:56.262612+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/contamcal-irt-calibration/exp008/run_signal_survival.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/contamcal-irt-calibration/exp008/run_signal_survival.py"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-14T15:21:56.262841+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/contamcal-irt-calibration/exp008/signal_survival.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/contamcal-irt-calibration/exp008/signal_survival.py"
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T15:21:56.263086+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/contamcal-irt-calibration/exp008/plot_survival.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/contamcal-irt-calibration/exp008/plot_survival.py"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T15:21:56.269388+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls -la /root/autodl-tmp/exp002/signals/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls -la /root/autodl-tmp/exp002/signals/"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-14T15:21:56.269934+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nexp-008 Signal Survival — end-to-end execution script.\\nv2: Extended from SFT/RL pairwise to N-regime comparison.\\n\\nUsage:\\n  python run_signal_survival.py \\\\\\n    --regime-dirs base=/path/base SFT_clean=/path/sft RL=/path/rl \\\\\\n    --labels-file /path/to/labels.json \\\\\\n    --output-dir /path/to/exp008_output/\\n\\n  # Legacy 2-regime (still works):\\n  python run_signal_survival.py \\\\\\n    --sft-signals-dir /path/sft/ --rl-signals-dir /path/rl/ \\\\\\n    --labels-file labels.json\\n\\n  # Quick validation with mock data:\\n  python run_signal_survival.py --dry-run --max-items 10\\n  python run_signal_survival.py --dry-run --max-items 10 --regime-names base SFT RL DPO\\n\\nDependencies: numpy, scipy, sklearn\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport logging\\nimport sys\\nfrom collections import OrderedDict\\nfrom pathlib import Path\\n\\nimport numpy as np\\n\\nfrom signal_survival_analysis import (\\n    SIGNAL_KEYS,\\n    print_summary_table,\\n    run_survival_analysis,\\n    save_report,\\n)\\n\\nlogger = logging.getLogger(__name__)\\n\\n\\ndef load_signal_file(path: Path, signal_key: str) -> list[dict]:\\n    \\\"\\\"\\\"Load a signal JSON file and validate it has expected fields.\\\"\\\"\\\"\\n    with open(path) as f:\\n        data = json.load(f)\\n    if not isinstance(data, list) or len(data) == 0:\\n        raise ValueError(f\\\"Expected non-empty list in {path}\\\")\\n    if signal_key not in data[0]:\\n        raise ValueError(f\\\"Signal key '{signal_key}' not found in {path}\\\")\\n    return data\\n\\n\\ndef load_signals_from_dir(signals_dir: Path) -> dict[str, list[dict]]:\\n    \\\"\\\"\\\"\\n    Load all signal files from a directory.\\n    Returns {signal_key: [records]}.\\n    \\\"\\\"\\\"\\n    signals = {}\\n\\n    merged_files = list(signals_dir.glob(\\\"signals_merged_*.json\\\"))\\n    if merged_files:\\n        logger.info(\\\"Found
…[truncated 7141 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 7
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T15:21:56.270516+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nexp-008 Signal Survival Analysis — main script (v3).\\n\\nAnalyzes how contamination detection signals survive across training regimes\\n(base → SFT-clean → SFT-contam → RL-aligned). Supports paper C2 claim:\\n\\\"cliff-like signal degradation under RL alignment.\\\"\\n\\nInput:\\n  - Per-regime signal directories from exp-002 compute_signals.py.\\n    Directory structure: {regime_dir}/{benchmark}/ containing\\n    signal_{type}_{benchmark}.json or signals_merged_{benchmark}.json.\\n    Record format: [{\\\"index\\\": int, \\\"benchmark\\\": str, \\\"s1_embedding\\\": float, ...}]\\n  - Contamination labels per benchmark: JSON {str(index): 0 | 1}\\n  - (Optional) RRF aggregated scores: rrf_{benchmark}.json or\\n    exposure_rrf_{benchmark}.json from aggregate_rrf.py\\n\\nOutput (to --output-dir):\\n  - per_benchmark/{benchmark}/survival_report.json\\n  - cliff_analysis.json — cliff vs gradual degradation detection\\n  - cross_benchmark_summary.json — aggregated statistics\\n  - Console summary table\\n\\nDependencies: numpy, scipy, sklearn\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport logging\\nimport sys\\nfrom collections import OrderedDict\\nfrom pathlib import Path\\n\\nimport numpy as np\\nfrom scipy import stats\\nfrom sklearn.metrics import roc_auc_score\\n\\nlogger = logging.getLogger(__name__)\\n\\nALL_SIGNAL_KEYS = [\\n    \\\"s1_embedding\\\", \\\"s2_minkpp\\\", \\\"s3_constat\\\", \\\"s4_selfcritique\\\", \\\"rrf_score\\\",\\n]\\nSIGNAL_LABELS = {\\n    \\\"s1_embedding\\\": \\\"Embedding\\\",\\n    \\\"s2_minkpp\\\": \\\"Min-K%++\\\",\\n    \\\"s3_constat\\\": \\\"ConStat\\\",\\n    \\\"s4_selfcritique\\\": \\\"Self-Critique\\\",\\n    \\\"rrf_score\\\": \\\"RRF (fused)\\\",\\n}\\nDEFAULT_BENCHMARKS = [\\\"mmlu\\\", \\\"gsm8k\\\", \\\"arc_challenge\\\"]\\nCLIFF_THRESHOLD = 0.7\\n\\n\\n# ---------------------------------------------------------------------------\\n# Data 
…[truncated 7085 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 7
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-14T15:21:56.270996+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nexp-008 Signal Survival — visualization.\\nv2: Extended to N regimes; primary output is AUC heatmap (paper Figure 2).\\n\\nGenerates:\\n  1. AUC heatmap: signal x regime AUROC matrix\\n  2. Pairwise delta-AUC heatmap: AUC change between adjacent regime pairs\\n\\nInput:  survival_report.json (from run_signal_survival.py)\\nOutput: PDF files in output directory\\n\\nDependencies: matplotlib, seaborn (optional fallback to imshow), numpy\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport logging\\nfrom pathlib import Path\\n\\nimport matplotlib\\nmatplotlib.use(\\\"Agg\\\")\\nimport matplotlib.pyplot as plt\\nimport numpy as np\\n\\nlogger = logging.getLogger(__name__)\\n\\nSIGNAL_KEYS = [\\\"s1_embedding\\\", \\\"s2_minkpp\\\", \\\"s3_constat\\\", \\\"s4_selfcritique\\\"]\\nSIGNAL_LABELS = {\\n    \\\"s1_embedding\\\": \\\"Embedding\\\",\\n    \\\"s2_minkpp\\\": \\\"Min-K%++\\\",\\n    \\\"s3_constat\\\": \\\"ConStat\\\",\\n    \\\"s4_selfcritique\\\": \\\"Self-Critique\\\",\\n}\\n\\n\\ndef _try_import_seaborn():\\n    try:\\n        import seaborn as sns\\n        return sns\\n    except ImportError:\\n        logger.warning(\\\"seaborn not available, falling back to matplotlib imshow\\\")\\n        return None\\n\\n\\ndef plot_auc_heatmap(report: dict, output_path: Path):\\n    \\\"\\\"\\\"Signal x regime AUC heatmap (paper Figure 2 format).\\\"\\\"\\\"\\n    sns = _try_import_seaborn()\\n\\n    auc_matrix = report[\\\"auc_matrix\\\"]\\n    regime_names = report[\\\"regime_names\\\"]\\n\\n    signals = [k for k in SIGNAL_KEYS if k in auc_matrix]\\n    if not signals:\\n        logger.warning(\\\"No signals to plot\\\")\\n        return\\n\\n    sig_labels = [SIGNAL_LABELS[k] for k in signals]\\n    data = np.array([\\n        [auc_matrix[s].get(r, float(\\\"nan\\\")) for r in regime_names]\\n        for s in signals\\n    ])\\n\\n    fig, ax = plt.subplots(\\n        figsize=(max(3.5, 1.5
…[truncated 6261 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 7
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T15:21:56.271291+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 16\\ndrwxr-xr-x 5 root root  151 May 14 21:29 .\\ndrwxr-xr-x 3 root root   29 May 14 15:57 ..\\ndrwxr-xr-x 2 root root 4096 May 14 21:06 Qwen2.5-0.5B_d000_s42\\ndrwxr-xr-x 2 root root 4096 May 14 21:29 Qwen2.5-0.5B_d005_s42\\ndrwxr-xr-x 2 root root 4096 May 14 21:58 Qwen2.5-0.5B_d100_s42\\n-rw-r--r-- 1 root root  561 May 14 21:58 batch_report_Qwen2.5-0.5B.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T15:21:56.277739+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls -la /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls -la /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T15:21:56.278007+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 16048\\ndrwxr-xr-x 2 root root    4096 May 14 21:06 .\\ndrwxr-xr-x 5 root root     151 May 14 21:29 ..\\n-rw-r--r-- 1 root root  515053 May 14 18:41 signal_embedding_arc_challenge.json\\n-rw-r--r-- 1 root root  567771 May 14 20:49 signal_embedding_gsm8k.json\\n-rw-r--r-- 1 root root 6093045 May 14 18:50 signal_embedding_mmlu.json\\n-rw-r--r-- 1 root root    2179 May 14 16:00 signal_embedding_mmlu_Qwen2.5-0.5B_d000_s42.json\\n-rw-r--r-- 1 root root  185943 May 14 21:05 signal_minkpp_arc_challenge.json\\n-rw-r--r-- 1 root root  199977 May 14 20:50 signal_minkpp_gsm8k.json\\n-rw-r--r-- 1 root root 2121205 May 14 18:55 signal_minkpp_mmlu.json\\n-rw-r--r-- 1 root root  254781 May 14 21:06 signal_selfcritique_arc_challenge.json\\n-rw-r--r-- 1 root root  276624 May 14 21:05 signal_selfcritique_gsm8k.json\\n-rw-r--r-- 1 root root 2934171 May 14 21:04 signal_selfcritique_mmlu.json\\n-rw-r--r-- 1 root root  239249 May 14 21:06 signals_merged_arc_challenge.json\\n-rw-r--r-- 1 root root  258901 May 14 21:05 signals_merged_gsm8k.json\\n-rw-r--r-- 1 root root 2756294 May 14 21:04 signals_merged_mmlu.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T15:21:56.278359+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls -la /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d100_s42/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls -la /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d100_s42/"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T15:21:56.278612+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 16016\\ndrwxr-xr-x 2 root root    4096 May 14 21:58 .\\ndrwxr-xr-x 5 root root     151 May 14 21:29 ..\\n-rw-r--r-- 1 root root  513223 May 14 21:56 signal_embedding_arc_challenge.json\\n-rw-r--r-- 1 root root  566915 May 14 21:52 signal_embedding_gsm8k.json\\n-rw-r--r-- 1 root root 6043238 May 14 21:33 signal_embedding_mmlu.json\\n-rw-r--r-- 1 root root  185963 May 14 21:57 signal_minkpp_arc_challenge.json\\n-rw-r--r-- 1 root root  199993 May 14 21:52 signal_minkpp_gsm8k.json\\n-rw-r--r-- 1 root root 2121519 May 14 21:39 signal_minkpp_mmlu.json\\n-rw-r--r-- 1 root root  256439 May 14 21:58 signal_selfcritique_arc_challenge.json\\n-rw-r--r-- 1 root root  276957 May 14 21:53 signal_selfcritique_gsm8k.json\\n-rw-r--r-- 1 root root 2952787 May 14 21:48 signal_selfcritique_mmlu.json\\n-rw-r--r-- 1 root root  239643 May 14 21:58 signals_merged_arc_challenge.json\\n-rw-r--r-- 1 root root  258969 May 14 21:53 signals_merged_gsm8k.json\\n-rw-r--r-- 1 root root 2758329 May 14 21:48 signals_merged_mmlu.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T15:21:56.278828+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls -la /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d005_s42/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls -la /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d005_s42/"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T15:21:56.279057+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 16048\\ndrwxr-xr-x 2 root root    4096 May 14 21:29 .\\ndrwxr-xr-x 5 root root     151 May 14 21:29 ..\\n-rw-r--r-- 1 root root  514645 May 14 21:27 signal_embedding_arc_challenge.json\\n-rw-r--r-- 1 root root  567631 May 14 21:23 signal_embedding_gsm8k.json\\n-rw-r--r-- 1 root root 6077177 May 14 18:45 signal_embedding_mmlu.json\\n-rw-r--r-- 1 root root  185939 May 14 21:28 signal_minkpp_arc_challenge.json\\n-rw-r--r-- 1 root root  200053 May 14 21:24 signal_minkpp_gsm8k.json\\n-rw-r--r-- 1 root root 2121481 May 14 21:12 signal_minkpp_mmlu.json\\n-rw-r--r-- 1 root root  256587 May 14 21:29 signal_selfcritique_arc_challenge.json\\n-rw-r--r-- 1 root root  276365 May 14 21:25 signal_selfcritique_gsm8k.json\\n-rw-r--r-- 1 root root 2952548 May 14 21:20 signal_selfcritique_mmlu.json\\n-rw-r--r-- 1 root root  239694 May 14 21:29 signals_merged_arc_challenge.json\\n-rw-r--r-- 1 root root  258884 May 14 21:25 signals_merged_gsm8k.json\\n-rw-r--r-- 1 root root 2759581 May 14 21:20 signals_merged_mmlu.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T15:21:56.279278+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/autodl-tmp/exp002/ -name \"labels_*\" -o -name \"contamination_labels*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/autodl-tmp/exp002/ -name \"labels_*\" -o -name \"contamination_labels*\""
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T15:21:56.285627+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 6
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T15:21:56.285857+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -5 /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d100_s42/signals_merged_mmlu.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -5 /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d100_s42/signals_merged_mmlu.json"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T15:21:56.286080+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[\\n  {\\n    \\\"index\\\": 0,\\n    \\\"benchmark\\\": \\\"mmlu\\\",\\n    \\\"s1_embedding\\\": 0.9028400778770447,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T15:21:56.286289+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/contamcal-irt-calibration/ -name \"labels_*\" -o -name \"contamination_labels*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/contamcal-irt-calibration/ -name \"labels_*\" -o -name \"contamination_labels*\""
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T15:21:56.286527+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T15:21:56.286837+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'SSH读取exp008/所有4个文件代码', 'status': 'completed', 'activeForm': '读取exp008代码文件'}, {'content': '检查exp-002信号输出文件是否存在且非空', 'status': 'in_progress', 'activeForm': '检查exp-002信号输出'}, {'content': '审查代码：输入路径对齐、逻辑正确性、依赖分析', 'status': 'pending', 'activeForm': '审查代码逻辑和路径'}, {'content': '确认是否纯CPU、是否需要额外输入', 'status': 'pending', 'activeForm': '分析运行依赖'}, {'content': '执行dry-run或准备提交命令', 'status': 'pending', 'activeForm': '执行或准备命令'}, {'content': '汇报结果', 'status': 'pending', 'activeForm': '汇报审查结果'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'SSH读取exp008/所有4个文件代码', 'status': 'completed', 'activeForm': '读取exp008代码文件'}, {'content': '检查exp-002信号输出文件是否存在且非空', 'status': 'in_progress', 'activeForm': '检查exp-002信号输出'}, {'content': '审查代码：输入路径对齐、逻辑正确性、依赖分析', 'status': 'pending', 'activeForm': '审查代码逻辑和路径'}, {'content': '确认是否纯CPU、是否需要额外输入', 'status': 'pending', 'activeForm': '分析运行依赖'}, {'content': '执行dry-run或准备提交命令', 'status': 'pending', 'activeForm': '执行或准备命令'}, {'content': '汇报结果', 'status': 'pending', 'activeForm': '汇报审查结果'}]"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T15:21:56.287111+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T15:21:56.296383+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/contamcal-irt-calibration/ -name \"labels*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/contamcal-irt-calibration/ -name \"labels*\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T15:21:56.296742+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T15:21:56.296997+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/autodl-tmp/ -name \"labels*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/autodl-tmp/ -name \"labels*\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T15:21:56.297230+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.57}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-14T15:21:56.297463+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -3 /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d100_s42/signals_merged_mmlu.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -3 /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d100_s42/signals_merged_mmlu.json"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-14T15:21:56.297678+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[\\n  {\\n    \\\"index\\\": 0,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-14T15:21:56.297882+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d100_s42/signals_merged_mmlu.json')); print(list(d[0].keys())); print(len(d))\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d100_s42/signals_merged_mmlu.json')); print(list(d[0].keys())); print(len(d))\""
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-14T15:21:56.298086+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-14T15:21:56.298285+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/autodl-tmp/exp001/ -name \"*contam*\" -o -name \"*dosage*\" -o -name \"*inject*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/autodl-tmp/exp001/ -name \"*contam*\" -o -name \"*dosage*\" -o -name \"*inject*\""
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-14T15:21:56.306730+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl\\n/root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl\\n/root/autodl-tmp/exp001/sft_data/contamination_labels_arc_challenge_d005.json\\n/root/autodl-tmp/exp001/sft_data/contamination_labels_gsm8k_d005.json\\n/root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl\\n/root/autodl-tmp/exp001/sft_data/contamination_labels_arc_challenge_d025.json\\n/root/autodl-tmp/exp001/sft_data/contamination_labels_gsm8k_d025.json\\n/root/autodl-tmp/exp001/sft_data/sft_dosage_050.jsonl\\n/root/autodl-tmp/exp001/sft_data/contamination_labels_arc_challenge_d050.json\\n/root/autodl-tmp/exp001/sft_data/contamination_labels_gsm8k_d050.json\\n/root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl\\n/root/autodl-tmp/exp001/sft_data/contamination_labels_arc_challenge_d100.json\\n/root/autodl-tmp/exp001/sft_data/contamination_labels_gsm8k_d100.json\\n/root/autodl-tmp/exp001/sft_data/contamination_labels_mmlu_d005.json\\n/root/autodl-tmp/exp001/sft_data/contamination_labels_mmlu_d025.json\\n/root/autodl-tmp/exp001/sft_data/contamination_labels_mmlu_d050.json\\n/root/autodl-tmp/exp001/sft_data/contamination_labels_mmlu_d100.json\\n/root/autodl-tmp/exp001/sft_data_qc_filtered/sft_dosage_005.jsonl\\n/root/autodl-tmp/exp001/sft_data_qc_filtered/contamination_labels_arc_challenge_d005.json\\n/root/autodl-tmp/exp001/sft_data_qc_filtered/contamination_labels_gsm8k_d005.json\\n/root/autodl-tmp/exp001/sft_data_qc_filtered/contamination_labels_humaneval_d005.json\\n/root/autodl-tmp/exp001/sft_data_qc_filtered/contamination_labels_mmlu_d005.json\\n/root/autodl-tmp/exp001/sft_data_qc_filtered/sft_dosage_025.jsonl\\n/root/autodl-tmp/exp001/sft_data_qc_filtered/contamination_labels_arc_challenge_d025.json\\n/root/autodl-tmp/exp001/sft_data_qc_filtered/contamination_labels_gsm8k_d025.json\\n/root/autodl-tmp/exp001/sft_data_qc_filtered/contamination_labels_humaneval_d025.json\\n/root/autodl-tmp/exp001/s
…[truncated 992 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 8
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-14T15:21:56.307023+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls /root/contamcal-irt-calibration/exp008/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls /root/contamcal-irt-calibration/exp008/"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-14T15:21:56.307249+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"__pycache__\\nexp008_output\\nplot_survival.py\\nrun_exp008.sh\\nrun_exp008.sh.bak\\nrun_signal_survival.py\\nsignal_survival.py\\nsignal_survival_analysis.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-14T15:21:56.307556+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/contamcal-irt-calibration/exp008/run_exp008.sh"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/contamcal-irt-calibration/exp008/run_exp008.sh"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-14T15:21:56.307947+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/bin/bash\\nset -euo pipefail\\n\\nGPUS=\\\"${1:?Usage: bash run_exp008.sh GPU_IDS (e.g. 1,4,5)}\\\"\\n\\n# === Paths ===\\nBASE_MODEL=\\\"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B\\\"\\nINSTRUCT_MODEL=\\\"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B-Instruct\\\"\\nD000_ADAPTER=\\\"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter\\\"\\nD005_ADAPTER=\\\"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42/lora_adapter\\\"  # d005: mixed 0/1 labels, AUC computable\\nSFT_DATA=\\\"/root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl\\\"\\nLABELS_DIR=\\\"/root/autodl-tmp/exp001/sft_data\\\"\\n\\nOUTPUT_BASE=\\\"/root/autodl-tmp/exp008\\\"\\nSIGNALS_DIR=\\\"${OUTPUT_BASE}/signals\\\"\\nRESULTS_DIR=\\\"${OUTPUT_BASE}/results\\\"\\n\\nBENCHMARKS=(mmlu gsm8k arc_challenge)\\nSIGNALS=\\\"embedding minkpp selfcritique\\\"\\n\\nSCRIPT_DIR=\\\"$(cd \\\"$(dirname \\\"$0\\\")\\\" && pwd)\\\"\\nCOMPUTE_SCRIPT=\\\"${SCRIPT_DIR}/../exp002/compute_signals.py\\\"\\nSURVIVAL_SCRIPT=\\\"${SCRIPT_DIR}/run_signal_survival.py\\\"\\n\\n# === Environment ===\\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base\\nexport CUDA_VISIBLE_DEVICES=\\\"$GPUS\\\"\\n\\n# === Regime definitions ===\\ndeclare -A REGIME_MODEL\\nREGIME_MODEL[base]=\\\"$BASE_MODEL\\\"\\nREGIME_MODEL[sft_clean]=\\\"$D000_ADAPTER\\\"\\nREGIME_MODEL[sft_contam]=\\\"$D005_ADAPTER\\\"\\nREGIME_MODEL[rl_aligned]=\\\"$INSTRUCT_MODEL\\\"\\nREGIMES=(base sft_clean sft_contam rl_aligned)\\n\\necho \\\"=== exp-008 Signal Survival ===\\\"\\necho \\\"GPUs: $GPUS | Benchmarks: ${BENCHMARKS[*]} | Signals: $SIGNALS\\\"\\necho \\\"Regimes: ${REGIMES[*]}\\\"\\necho \\\"\\\"\\n\\n# === Step 0: Convert labels to {index: 0/1} format ===\\nmkdir -p \\\"${OUTPUT_BASE}/labels\\\"\\nfor bench in \\\"${BENCHMARKS[@]}\\\"; do\\n    SRC=\\\"${LABELS_DIR}/contamination_labels_${bench}_d005.json\\\"\\n    DST=\\\"${OUTPUT_BASE}/labels/labels_${benc
…[truncated 2285 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-14T15:21:56.308225+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/contamcal-irt-calibration/exp008/run_exp008.sh.bak"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/contamcal-irt-calibration/exp008/run_exp008.sh.bak"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-14T15:21:56.316710+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/bin/bash\\nset -euo pipefail\\n\\nGPUS=\\\"${1:?Usage: bash run_exp008.sh GPU_IDS (e.g. 1,4,5)}\\\"\\n\\n# === Paths ===\\nBASE_MODEL=\\\"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B\\\"\\nINSTRUCT_MODEL=\\\"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B-Instruct\\\"\\nD000_ADAPTER=\\\"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter\\\"\\nD005_ADAPTER=\\\"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42/lora_adapter\\\"  # d005: mixed 0/1 labels, AUC computable\\nSFT_DATA=\\\"/root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl\\\"\\nLABELS_DIR=\\\"/root/autodl-tmp/exp001/sft_data\\\"\\n\\nOUTPUT_BASE=\\\"/root/autodl-tmp/exp008\\\"\\nSIGNALS_DIR=\\\"${OUTPUT_BASE}/signals\\\"\\nRESULTS_DIR=\\\"${OUTPUT_BASE}/results\\\"\\n\\nBENCHMARKS=(mmlu gsm8k arc_challenge)\\nSIGNALS=\\\"embedding minkpp selfcritique\\\"\\n\\nSCRIPT_DIR=\\\"$(cd \\\"$(dirname \\\"$0\\\")\\\" && pwd)\\\"\\nCOMPUTE_SCRIPT=\\\"${SCRIPT_DIR}/../exp002/compute_signals.py\\\"\\nSURVIVAL_SCRIPT=\\\"${SCRIPT_DIR}/run_signal_survival.py\\\"\\n\\n# === Environment ===\\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base\\nexport CUDA_VISIBLE_DEVICES=\\\"$GPUS\\\"\\n\\n# === Regime definitions ===\\ndeclare -A REGIME_MODEL REGIME_ADAPTER\\nREGIME_MODEL[base]=\\\"$BASE_MODEL\\\";           REGIME_ADAPTER[base]=\\\"\\\"\\nREGIME_MODEL[sft_clean]=\\\"$BASE_MODEL\\\";      REGIME_ADAPTER[sft_clean]=\\\"$D000_ADAPTER\\\"\\nREGIME_MODEL[sft_contam]=\\\"$BASE_MODEL\\\";     REGIME_ADAPTER[sft_contam]=\\\"$D005_ADAPTER\\\"\\nREGIME_MODEL[rl_aligned]=\\\"$INSTRUCT_MODEL\\\"; REGIME_ADAPTER[rl_aligned]=\\\"\\\"\\nREGIMES=(base sft_clean sft_contam rl_aligned)\\n\\necho \\\"=== exp-008 Signal Survival ===\\\"\\necho \\\"GPUs: $GPUS | Benchmarks: ${BENCHMARKS[*]} | Signals: $SIGNALS\\\"\\necho \\\"Regimes: ${REGIMES[*]}\\\"\\necho \\\"\\\"\\n\\n# === Step 0: Convert labels to {index: 0/1} format ===\\nmkdir -
…[truncated 2630 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 8
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-14T15:21:56.317002+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls -la /root/contamcal-irt-calibration/exp008/exp008_output/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls -la /root/contamcal-irt-calibration/exp008/exp008_output/"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-14T15:21:56.317267+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 80\\ndrwxr-xr-x 3 root root  4096 May 14 20:48 .\\ndrwxr-xr-x 4 root root  4096 May 14 21:55 ..\\n-rw-r--r-- 1 root root  8323 May 14 21:53 cliff_analysis.json\\n-rw-r--r-- 1 root root  2010 May 14 21:53 cross_benchmark_summary.json\\ndrwxr-xr-x 5 root root    68 May 14 20:48 per_benchmark\\n-rw-r--r-- 1 root root 23361 May 14 12:07 signal_decay_scatter.pdf\\n-rw-r--r-- 1 root root 16612 May 14 12:07 survival_auc_comparison.pdf\\n-rw-r--r-- 1 root root  8765 May 14 22:17 survival_report.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-14T15:21:56.317530+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -20 /root/autodl-tmp/exp001/sft_data/contamination_labels_mmlu_d100.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -20 /root/autodl-tmp/exp001/sft_data/contamination_labels_mmlu_d100.json"
  }
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-14T15:21:56.317765+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "wc -l /root/autodl-tmp/exp001/sft_data/contamination_labels_mmlu_d100.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "wc -l /root/autodl-tmp/exp001/sft_data/contamination_labels_mmlu_d100.json"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-14T15:21:56.318015+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"benchmark\\\": \\\"mmlu\\\",\\n  \\\"dosage\\\": 100,\\n  \\\"total_items\\\": 14042,\\n  \\\"contaminated_count\\\": 14042,\\n  \\\"labels\\\": [\\n    1,\\n    1,\\n    1,\\n    1,\\n    1,\\n    1,\\n    1,\\n    1,\\n    1,\\n    1,\\n    1,\\n    1,\\n    1,\\n    1,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-14T15:21:56.318216+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"14049 /root/autodl-tmp/exp001/sft_data/contamination_labels_mmlu_d100.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-14T15:21:56.325502+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls -la /root/autodl-tmp/exp008/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls -la /root/autodl-tmp/exp008/"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-14T15:21:56.325827+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 4\\ndrwxr-xr-x  3 root root   29 May 14 23:14 .\\ndrwxr-xr-x 16 root root 4096 May 14 23:14 ..\\ndrwxr-xr-x  4 root root   53 May 14 23:14 signals\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-14T15:21:56.326100+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/autodl-tmp/exp008/ -type d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/autodl-tmp/exp008/ -type d"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-14T15:21:56.326391+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/exp008/\\n/root/autodl-tmp/exp008/signals\\n/root/autodl-tmp/exp008/signals/sft_clean\\n/root/autodl-tmp/exp008/signals/sft_clean/mmlu\\n/root/autodl-tmp/exp008/signals/sft_clean/gsm8k\\n/root/autodl-tmp/exp008/signals/sft_clean/arc_challenge\\n/root/autodl-tmp/exp008/signals/sft_contam\\n/root/autodl-tmp/exp008/signals/sft_contam/mmlu\\n/root/autodl-tmp/exp008/signals/sft_contam/gsm8k\\n/root/autodl-tmp/exp008/signals/sft_contam/arc_challenge\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-14T15:21:56.326652+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/contamcal-irt-calibration/exp008/exp008_output/cross_benchmark_summary.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/contamcal-irt-calibration/exp008/exp008_output/cross_benchmark_summary.json"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-14T15:21:56.327016+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"regime_names\\\": [\\n    \\\"base\\\",\\n    \\\"sft_clean\\\",\\n    \\\"sft_contam\\\",\\n    \\\"rl_aligned\\\"\\n  ],\\n  \\\"benchmarks\\\": [\\n    \\\"mmlu\\\",\\n    \\\"gsm8k\\\",\\n    \\\"arc_challenge\\\"\\n  ],\\n  \\\"per_signal_aggregated\\\": {\\n    \\\"rrf_score\\\": {\\n      \\\"label\\\": \\\"RRF (fused)\\\",\\n      \\\"mean_auc_base\\\": 0.9975,\\n      \\\"std_auc_base\\\": 0.0044,\\n      \\\"mean_auc_sft_clean\\\": 1.0,\\n      \\\"std_auc_sft_clean\\\": 0.0,\\n      \\\"mean_auc_sft_contam\\\": 0.9873,\\n      \\\"std_auc_sft_contam\\\": 0.0067,\\n      \\\"mean_auc_rl_aligned\\\": 0.6105,\\n      \\\"std_auc_rl_aligned\\\": 0.0671\\n    },\\n    \\\"s1_embedding\\\": {\\n      \\\"label\\\": \\\"Embedding\\\",\\n      \\\"mean_auc_base\\\": 0.9918,\\n      \\\"std_auc_base\\\": 0.0072,\\n      \\\"mean_auc_sft_clean\\\": 0.9968,\\n      \\\"std_auc_sft_clean\\\": 0.0055,\\n      \\\"mean_auc_sft_contam\\\": 0.9841,\\n      \\\"std_auc_sft_contam\\\": 0.0162,\\n      \\\"mean_auc_rl_aligned\\\": 0.9733,\\n      \\\"std_auc_rl_aligned\\\": 0.0231\\n    },\\n    \\\"s2_minkpp\\\": {\\n      \\\"label\\\": \\\"Min-K%++\\\",\\n      \\\"mean_auc_base\\\": 0.9962,\\n      \\\"std_auc_base\\\": 0.0033,\\n      \\\"mean_auc_sft_clean\\\": 0.9981,\\n      \\\"std_auc_sft_clean\\\": 0.0019,\\n      \\\"mean_auc_sft_contam\\\": 0.9981,\\n      \\\"std_auc_sft_contam\\\": 0.0019,\\n      \\\"mean_auc_rl_aligned\\\": 0.7092,\\n      \\\"std_auc_rl_aligned\\\": 0.1178\\n    },\\n    \\\"s3_constat\\\": {\\n      \\\"label\\\": \\\"ConStat\\\",\\n      \\\"mean_auc_base\\\": 0.9975,\\n      \\\"std_auc_base\\\": 0.0022,\\n      \\\"mean_auc_sft_clean\\\": 0.993,\\n      \\\"std_auc_sft_clean\\\": 0.0077,\\n      \\\"mean_auc_sft_contam\\\": 0.9771,\\n      \\\"std_auc_sft_contam\\\": 0.0088,\\n      \\\"mean_auc_rl_aligned\\\": 0.5473,\\n      \\\"std_auc_rl_aligned\\\": 0.079\\n    },\\
…[truncated 756 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-14T15:21:56.333007+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls /root/contamcal-irt-calibration/exp008/exp008_output/per_benchmark/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls /root/contamcal-irt-calibration/exp008/exp008_output/per_benchmark/"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-14T15:21:56.333302+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"arc_challenge\\ngsm8k\\nmmlu\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 5
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-14T15:21:56.333545+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -50 /root/autodl-tmp/exp001/sft_data/contamination_labels_mmlu_d005.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -50 /root/autodl-tmp/exp001/sft_data/contamination_labels_mmlu_d005.json"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-14T15:21:56.333781+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"benchmark\\\": \\\"mmlu\\\",\\n  \\\"dosage\\\": 5,\\n  \\\"total_items\\\": 14042,\\n  \\\"contaminated_count\\\": 703,\\n  \\\"labels\\\": [\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-14T15:21:56.334068+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/autodl-tmp/exp008/signals/ -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/autodl-tmp/exp008/signals/ -type f"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-14T15:21:56.334344+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-14T15:21:56.334548+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/contamcal-irt-calibration/exp008/exp008_output/survival_report.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/contamcal-irt-calibration/exp008/exp008_output/survival_report.json"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-14T15:21:56.335026+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"regime_names\\\": [\\n    \\\"base\\\",\\n    \\\"sft_clean\\\",\\n    \\\"sft_contam\\\",\\n    \\\"rl_aligned\\\"\\n  ],\\n  \\\"auc_matrix\\\": {\\n    \\\"s1_embedding\\\": {\\n      \\\"base\\\": 0.9943,\\n      \\\"sft_clean\\\": 0.899,\\n      \\\"sft_contam\\\": 0.7695,\\n      \\\"rl_aligned\\\": 0.6829\\n    },\\n    \\\"s2_minkpp\\\": {\\n      \\\"base\\\": 0.9695,\\n      \\\"sft_clean\\\": 0.9467,\\n      \\\"sft_contam\\\": 0.8343,\\n      \\\"rl_aligned\\\": 0.7848\\n    },\\n    \\\"s3_constat\\\": {\\n      \\\"base\\\": 0.9771,\\n      \\\"sft_clean\\\": 0.9448,\\n      \\\"sft_contam\\\": 0.8133,\\n      \\\"rl_aligned\\\": 0.6467\\n    },\\n    \\\"s4_selfcritique\\\": {\\n      \\\"base\\\": 0.9981,\\n      \\\"sft_clean\\\": 0.9962,\\n      \\\"sft_contam\\\": 0.8914,\\n      \\\"rl_aligned\\\": 0.7086\\n    }\\n  },\\n  \\\"effect_size_matrix\\\": {\\n    \\\"s1_embedding\\\": {\\n      \\\"base\\\": 3.6603,\\n      \\\"sft_clean\\\": 1.8074,\\n      \\\"sft_contam\\\": 1.1501,\\n      \\\"rl_aligned\\\": 0.6708\\n    },\\n    \\\"s2_minkpp\\\": {\\n      \\\"base\\\": 2.7157,\\n      \\\"sft_clean\\\": 2.322,\\n      \\\"sft_contam\\\": 1.254,\\n      \\\"rl_aligned\\\": 1.1604\\n    },\\n    \\\"s3_constat\\\": {\\n      \\\"base\\\": 2.7081,\\n      \\\"sft_clean\\\": 2.261,\\n      \\\"sft_contam\\\": 1.2469,\\n      \\\"rl_aligned\\\": 0.5573\\n    },\\n    \\\"s4_selfcritique\\\": {\\n      \\\"base\\\": 3.7205,\\n      \\\"sft_clean\\\": 3.347,\\n      \\\"sft_contam\\\": 1.7833,\\n      \\\"rl_aligned\\\": 0.8725\\n    }\\n  },\\n  \\\"pairwise_tests\\\": {\\n    \\\"base_vs_sft_clean\\\": {\\n      \\\"s1_embedding\\\": {\\n        \\\"n_items\\\": 50,\\n        \\\"n_contaminated\\\": 15,\\n        \\\"n_clean\\\": 35,\\n        \\\"effect_size_a\\\": 3.6603,\\n        \\\"effect_size_b\\\": 1.8074,\\n        \\\"effect_size_ratio\\\": 0.4938,\\n        \\\"spearman_r
…[truncated 8581 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-14T15:21:56.335286+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls /root/contamcal-irt-calibration/exp008/exp008_output/per_benchmark/mmlu/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls /root/contamcal-irt-calibration/exp008/exp008_output/per_benchmark/mmlu/"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-14T15:21:56.343443+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"survival_report.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 8
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-14T15:21:56.343748+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/contamcal-irt-calibration/exp008/exp008_output/per_benchmark/mmlu/survival_report.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/contamcal-irt-calibration/exp008/exp008_output/per_benchmark/mmlu/survival_report.json"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-14T15:21:56.344288+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"regime_names\\\": [\\n    \\\"base\\\",\\n    \\\"sft_clean\\\",\\n    \\\"sft_contam\\\",\\n    \\\"rl_aligned\\\"\\n  ],\\n  \\\"auc_matrix\\\": {\\n    \\\"s1_embedding\\\": {\\n      \\\"base\\\": 1.0,\\n      \\\"sft_clean\\\": 1.0,\\n      \\\"sft_contam\\\": 1.0,\\n      \\\"rl_aligned\\\": 1.0\\n    },\\n    \\\"s2_minkpp\\\": {\\n      \\\"base\\\": 0.9981,\\n      \\\"sft_clean\\\": 0.9962,\\n      \\\"sft_contam\\\": 1.0,\\n      \\\"rl_aligned\\\": 0.781\\n    },\\n    \\\"s3_constat\\\": {\\n      \\\"base\\\": 0.9962,\\n      \\\"sft_clean\\\": 0.9848,\\n      \\\"sft_contam\\\": 0.9676,\\n      \\\"rl_aligned\\\": 0.6114\\n    },\\n    \\\"s4_selfcritique\\\": {\\n      \\\"base\\\": 1.0,\\n      \\\"sft_clean\\\": 1.0,\\n      \\\"sft_contam\\\": 0.9905,\\n      \\\"rl_aligned\\\": 0.3124\\n    },\\n    \\\"rrf_score\\\": {\\n      \\\"base\\\": 0.9924,\\n      \\\"sft_clean\\\": 1.0,\\n      \\\"sft_contam\\\": 0.9867,\\n      \\\"rl_aligned\\\": 0.5362\\n    }\\n  },\\n  \\\"effect_size_matrix\\\": {\\n    \\\"s1_embedding\\\": {\\n      \\\"base\\\": 4.1114,\\n      \\\"sft_clean\\\": 3.32,\\n      \\\"sft_contam\\\": 4.4787,\\n      \\\"rl_aligned\\\": 3.037\\n    },\\n    \\\"s2_minkpp\\\": {\\n      \\\"base\\\": 4.2537,\\n      \\\"sft_clean\\\": 3.8832,\\n      \\\"sft_contam\\\": 4.1447,\\n      \\\"rl_aligned\\\": 1.0976\\n    },\\n    \\\"s3_constat\\\": {\\n      \\\"base\\\": 3.5298,\\n      \\\"sft_clean\\\": 3.1116,\\n      \\\"sft_contam\\\": 2.3158,\\n      \\\"rl_aligned\\\": 0.2961\\n    },\\n    \\\"s4_selfcritique\\\": {\\n      \\\"base\\\": 4.3915,\\n      \\\"sft_clean\\\": 3.7025,\\n      \\\"sft_contam\\\": 2.783,\\n      \\\"rl_aligned\\\": -0.697\\n    },\\n    \\\"rrf_score\\\": {\\n      \\\"base\\\": 3.3423,\\n      \\\"sft_clean\\\": 4.4199,\\n      \\\"sft_contam\\\": 2.9419,\\n      \\\"rl_aligned\\\": 0.2179\\n    }\\n  },\\n  \\\"pairwise_tests\\\": 
…[truncated 8568 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-14T15:21:56.344586+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "wc -l /root/contamcal-irt-calibration/exp008/signal_survival_analysis.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "wc -l /root/contamcal-irt-calibration/exp008/signal_survival_analysis.py"
  }
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-14T15:21:56.344797+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tail -200 /root/contamcal-irt-calibration/exp008/signal_survival_analysis.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "tail -200 /root/contamcal-irt-calibration/exp008/signal_survival_analysis.py"
  }
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-14T15:21:56.345006+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"414 /root/contamcal-irt-calibration/exp008/signal_survival_analysis.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-14T15:21:56.356518+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"            \\\"%s: AUC %s\\\",\\n            SIGNAL_LABELS[sig_key],\\n            \\\" -> \\\".join(\\n                f\\\"{r}={auc_matrix[sig_key].get(r, 'N/A')}\\\" for r in regime_names\\n            ),\\n        )\\n\\n    # Backward compat per_signal (maps first adjacent pair to old SFT/RL keys)\\n    per_signal: dict[str, dict] = {}\\n    if adjacent_pairs:\\n        first_pair_key = f\\\"{adjacent_pairs[0][0]}_vs_{adjacent_pairs[0][1]}\\\"\\n        for sig_key, pm in pairwise_tests.get(first_pair_key, {}).items():\\n            per_signal[sig_key] = {\\n                \\\"signal_label\\\": SIGNAL_LABELS.get(sig_key, sig_key),\\n                \\\"n_items\\\": pm[\\\"n_items\\\"],\\n                \\\"n_contaminated\\\": pm[\\\"n_contaminated\\\"],\\n                \\\"n_clean\\\": pm[\\\"n_clean\\\"],\\n                \\\"effect_size_sft\\\": pm[\\\"effect_size_a\\\"],\\n                \\\"effect_size_rl\\\": pm[\\\"effect_size_b\\\"],\\n                \\\"effect_size_ratio\\\": pm.get(\\\"effect_size_ratio\\\"),\\n                \\\"spearman_rho\\\": pm.get(\\\"spearman_rho\\\"),\\n                \\\"spearman_p\\\": pm.get(\\\"spearman_p\\\"),\\n                \\\"auc_sft\\\": pm.get(\\\"auc_a\\\"),\\n                \\\"auc_rl\\\": pm.get(\\\"auc_b\\\"),\\n                \\\"auc_ratio\\\": pm.get(\\\"auc_ratio\\\"),\\n                \\\"wilcoxon_stat\\\": pm.get(\\\"wilcoxon_stat\\\"),\\n                \\\"wilcoxon_p\\\": pm.get(\\\"wilcoxon_p\\\"),\\n            }\\n\\n    # Summary: signal \\\"survives\\\" if last regime AUC >= 0.6 and d-ratio >= 0.5\\n    last_regime = regime_names[-1]\\n    first_regime = regime_names[0]\\n    surviving = []\\n    for sig_key in auc_matrix:\\n        auc_last = auc_matrix[sig_key].get(last_regime)\\n        d_first = effect_size_matrix.get(sig_key, {}).get(first_regime)\\n        d_last = effect_size_matrix.get(sig_key, {}).get(last_regime)\\n     
…[truncated 6385 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 11
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-14T15:21:56.356988+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -n \"wilcoxon_stat.*= N\" /root/contamcal-irt-calibration/exp008/signal_survival_analysis.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -n \"wilcoxon_stat.*= N\" /root/contamcal-irt-calibration/exp008/signal_survival_analysis.py"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-14T15:21:56.357250+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"129:        result[\\\"wilcoxon_stat\\\"] = None\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-14T15:21:56.357485+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -n \"= N$\" /root/contamcal-irt-calibration/exp008/signal_survival_analysis.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -n \"= N$\" /root/contamcal-irt-calibration/exp008/signal_survival_analysis.py"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-14T15:21:56.357696+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-14T15:21:56.357896+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -n \"wilcoxon\" /root/contamcal-irt-calibration/exp008/signal_survival_analysis.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -n \"wilcoxon\" /root/contamcal-irt-calibration/exp008/signal_survival_analysis.py"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-14T15:21:56.358116+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"125:        w_stat, w_p = stats.wilcoxon(nonzero_diffs)\\n126:        result[\\\"wilcoxon_stat\\\"] = float(w_stat)\\n127:        result[\\\"wilcoxon_p\\\"] = float(f\\\"{w_p:.2e}\\\")\\n129:        result[\\\"wilcoxon_stat\\\"] = None\\n130:        result[\\\"wilcoxon_p\\\"] = None\\n240:                \\\"wilcoxon_stat\\\": pm.get(\\\"wilcoxon_stat\\\"),\\n241:                \\\"wilcoxon_p\\\": pm.get(\\\"wilcoxon_p\\\"),\\n400:            f\\\"{fmt(m.get('wilcoxon_p'), 2):>10} \\\"\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-14T15:21:56.363476+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -220 /root/contamcal-irt-calibration/exp008/signal_survival_analysis.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -220 /root/contamcal-irt-calibration/exp008/signal_survival_analysis.py"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-14T15:21:56.363904+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nexp-008 Signal Survival Analysis — core analysis module.\\nv2: Extended from SFT/RL pairwise to N-regime comparison.\\n\\nComputes:\\n  - AUC matrix: N_signals x N_regimes AUROC for contamination detection\\n  - Pairwise tests: statistical tests between all adjacent regime pairs\\n    (Cohen's d, Spearman rho, AUROC ratio, Wilcoxon signed-rank)\\n\\nInput:  OrderedDict mapping regime_name -> {signal_key: [records]}, plus labels.\\nOutput: {regime_names, auc_matrix, pairwise_tests, per_signal (compat), summary}\\n\\\"\\\"\\\"\\n\\nimport json\\nimport logging\\nfrom collections import OrderedDict\\nfrom pathlib import Path\\n\\nimport numpy as np\\nfrom scipy import stats\\nfrom sklearn.metrics import roc_auc_score\\n\\nlogger = logging.getLogger(__name__)\\n\\nSIGNAL_KEYS = [\\\"s1_embedding\\\", \\\"s2_minkpp\\\", \\\"s3_constat\\\", \\\"s4_selfcritique\\\"]\\nSIGNAL_LABELS = {\\n    \\\"s1_embedding\\\": \\\"Embedding\\\",\\n    \\\"s2_minkpp\\\": \\\"Min-K%++\\\",\\n    \\\"s3_constat\\\": \\\"ConStat\\\",\\n    \\\"s4_selfcritique\\\": \\\"Self-Critique\\\",\\n}\\n\\n\\ndef cohens_d(group1: np.ndarray, group2: np.ndarray) -> float:\\n    \\\"\\\"\\\"Cohen's d effect size between two groups.\\\"\\\"\\\"\\n    n1, n2 = len(group1), len(group2)\\n    if n1 < 2 or n2 < 2:\\n        return float(\\\"nan\\\")\\n    var1 = group1.var(ddof=1)\\n    var2 = group2.var(ddof=1)\\n    pooled_std = np.sqrt(((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2))\\n    if pooled_std == 0:\\n        return float(\\\"nan\\\")\\n    return (group1.mean() - group2.mean()) / pooled_std\\n\\n\\ndef compute_single_regime_metrics(values: np.ndarray, labels: np.ndarray) -> dict:\\n    \\\"\\\"\\\"AUROC and Cohen's d for contamination detection in one regime.\\\"\\\"\\\"\\n    mask = ~(np.isnan(values) | np.isnan(labels))\\n    v = values[mask]\\n    lab = labels[mask].astype(int)\\n    contam = lab == 1\\n    clean = la
…[truncated 6004 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-14T15:21:56.364189+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -n \"def \\|class \" /root/contamcal-irt-calibration/exp008/signal_survival.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -n \"def \\|class \" /root/contamcal-irt-calibration/exp008/signal_survival.py"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-14T15:21:56.364440+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-14T15:21:56.364648+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -350 /root/contamcal-irt-calibration/exp008/signal_survival.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -350 /root/contamcal-irt-calibration/exp008/signal_survival.py"
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-14T15:21:56.365045+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nexp-008 Signal Survival Analysis — main script (v3).\\n\\nAnalyzes how contamination detection signals survive across training regimes\\n(base → SFT-clean → SFT-contam → RL-aligned). Supports paper C2 claim:\\n\\\"cliff-like signal degradation under RL alignment.\\\"\\n\\nInput:\\n  - Per-regime signal directories from exp-002 compute_signals.py.\\n    Directory structure: {regime_dir}/{benchmark}/ containing\\n    signal_{type}_{benchmark}.json or signals_merged_{benchmark}.json.\\n    Record format: [{\\\"index\\\": int, \\\"benchmark\\\": str, \\\"s1_embedding\\\": float, ...}]\\n  - Contamination labels per benchmark: JSON {str(index): 0 | 1}\\n  - (Optional) RRF aggregated scores: rrf_{benchmark}.json or\\n    exposure_rrf_{benchmark}.json from aggregate_rrf.py\\n\\nOutput (to --output-dir):\\n  - per_benchmark/{benchmark}/survival_report.json\\n  - cliff_analysis.json — cliff vs gradual degradation detection\\n  - cross_benchmark_summary.json — aggregated statistics\\n  - Console summary table\\n\\nDependencies: numpy, scipy, sklearn\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport logging\\nimport sys\\nfrom collections import OrderedDict\\nfrom pathlib import Path\\n\\nimport numpy as np\\nfrom scipy import stats\\nfrom sklearn.metrics import roc_auc_score\\n\\nlogger = logging.getLogger(__name__)\\n\\nALL_SIGNAL_KEYS = [\\n    \\\"s1_embedding\\\", \\\"s2_minkpp\\\", \\\"s3_constat\\\", \\\"s4_selfcritique\\\", \\\"rrf_score\\\",\\n]\\nSIGNAL_LABELS = {\\n    \\\"s1_embedding\\\": \\\"Embedding\\\",\\n    \\\"s2_minkpp\\\": \\\"Min-K%++\\\",\\n    \\\"s3_constat\\\": \\\"ConStat\\\",\\n    \\\"s4_selfcritique\\\": \\\"Self-Critique\\\",\\n    \\\"rrf_score\\\": \\\"RRF (fused)\\\",\\n}\\nDEFAULT_BENCHMARKS = [\\\"mmlu\\\", \\\"gsm8k\\\", \\\"arc_challenge\\\"]\\nCLIFF_THRESHOLD = 0.7\\n\\n\\n# ---------------------------------------------------------------------------\\n# Data 
…[truncated 7159 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp008_signal_survival_20260514T151627",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---
