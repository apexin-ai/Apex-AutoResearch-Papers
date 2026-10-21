# analysis opt1b full 8pair

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 0
- **Tool calls:** 19
- **Original source:** `logs/chats/worker_analysis_opt1b_full_8pair_20260517T124735.jsonl`
- **Structured JSON:** [`ef7b55b7f3b7e034ea47.json`](../../sessions/ef/ef7b55b7f3b7e034ea47.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

39 recorded events

### Tool call

_source line 1 · 2026-05-17T12:50:47.847093+00:00_

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
  "session": "worker_analysis_opt1b_full_8pair_20260517T124735",
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

_source line 2 · 2026-05-17T12:50:47.847427+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_opt1b_full_8pair_20260517T124735",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T12:50:47.847612+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/analyze_generalize.py /root/autodl-tmp/distrib_canary_collapse/five_method_analysis.py /root/autodl-tmp/distrib_canary_collapse/reverse_permg_pythia410m.py 2>&1",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_opt1b_full_8pair_20260517T124735",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/analyze_generalize.py /root/autodl-tmp/distrib_canary_collapse/five_method_analysis.py /root/autodl-tmp/distrib_canary_collapse/reverse_permg_pythia410m.py 2>&1",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T12:50:47.847758+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_opt1b_full_8pair_20260517T124735",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T12:50:47.847885+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/generalize/opt1b_wiki_a100_s42/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_opt1b_full_8pair_20260517T124735",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/generalize/opt1b_wiki_a100_s42/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T12:50:47.848013+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"EXIT_CODE\\nall_metrics.json\\nconfig.json\\ngen_0\\ngen_1\\ngen_10\\ngen_2\\ngen_3\\ngen_4\\ngen_5\\ngen_6\\ngen_7\\ngen_8\\ngen_9\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.06}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_opt1b_full_8pair_20260517T124735",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T12:50:47.848132+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/analyze_generalize.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_opt1b_full_8pair_20260517T124735",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/analyze_generalize.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T12:50:47.848268+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/analyze_generalize.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_opt1b_full_8pair_20260517T124735",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T12:50:47.848399+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/five_method_analysis.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_opt1b_full_8pair_20260517T124735",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/five_method_analysis.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T12:50:47.848518+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/autodl-tmp/distrib_canary_collapse/five_method_analysis.py': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_opt1b_full_8pair_20260517T124735",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T12:50:47.848643+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/reverse_permg_pythia410m.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_opt1b_full_8pair_20260517T124735",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/reverse_permg_pythia410m.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T12:50:47.848764+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/reverse_permg_pythia410m.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_opt1b_full_8pair_20260517T124735",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T12:50:47.848878+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/analyze_generalize.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_opt1b_full_8pair_20260517T124735",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/analyze_generalize.py",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-17T12:50:47.848990+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/reverse_permg_pythia410m.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_opt1b_full_8pair_20260517T124735",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/reverse_permg_pythia410m.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-17T12:50:47.849208+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"5-method causal analysis for generalize experiments.\\n\\nReuses the same statistical methods as cross_alpha_analysis_v4.py\\nbut targets results/generalize/{experiment}/all_metrics.json.\\n\\nUsage:\\n    python analyze_generalize.py --exp pythia410m_wiki_a100_s42\\n    python analyze_generalize.py --exp opt1b_wiki_a100_s42\\n    python analyze_generalize.py  # all experiments in results/generalize/\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport os\\nimport sys\\nimport warnings\\nfrom datetime import datetime\\n\\nimport numpy as np\\nfrom statsmodels.stats.multitest import multipletests\\n\\nwarnings.filterwarnings(\\\"ignore\\\")\\n\\nBASE_DIR = os.path.dirname(os.path.abspath(__file__))\\nsys.path.insert(0, BASE_DIR)\\n\\nfrom method_ablation import (\\n    CANARY, DOWNSTREAM,\\n    extract as ma_extract,\\n    naive_pearson, diff_xcorr, threshold_lead, toda_yamamoto, perm_granger,\\n)\\n\\nGENERALIZE_DIR = os.path.join(BASE_DIR, \\\"results\\\", \\\"generalize\\\")\\n\\nMA_METHODS = {\\n    \\\"naive_pearson\\\": naive_pearson,\\n    \\\"differenced_xcorr\\\": diff_xcorr,\\n    \\\"threshold_onset\\\": threshold_lead,\\n    \\\"toda_yamamoto\\\": toda_yamamoto,\\n    \\\"permutation_granger\\\": perm_granger,\\n}\\n\\nMETRICS = [\\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\",\\n           \\\"token_entropy\\\", \\\"ece\\\", \\\"perplexity\\\"]\\n\\nclass NumpyEncoder(json.JSONEncoder):\\n    def default(self, obj):\\n        if isinstance(obj, (np.integer,)):\\n            return int(obj)\\n        if isinstance(obj, (np.floating,)):\\n            return float(obj)\\n        if isinstance(obj, np.ndarray):\\n            return obj.tolist()\\n        return super().default(obj)\\n\\n\\ndef assemble_all_metrics(exp_dir):\\n    \\\"\\\"\\\"Assemble all_metrics.json from per-gen metrics.json if needed.\\\"\\\"\\\"\\n    all_path = os.path.join(exp_dir, \\\"all_metrics.json\
…[truncated 6768 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_opt1b_full_8pair_20260517T124735",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T12:50:47.849488+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Reverse Permutation Granger test for Pythia-410M generalize experiment.\\n\\nForward: H0: canary does NOT Granger-cause downstream\\nReverse: H0: downstream does NOT Granger-cause canary\\n\\nTests 8 canonical pairs: {token_entropy, ece} x {distinct_1, distinct_2, distinct_3, mauve}\\n\\\"\\\"\\\"\\n\\nimport json\\nimport os\\nimport sys\\nimport numpy as np\\nfrom statsmodels.stats.multitest import multipletests\\n\\nBASE_DIR = os.path.dirname(os.path.abspath(__file__))\\nsys.path.insert(0, BASE_DIR)\\nfrom permutation_granger import permutation_granger_test\\n\\nDATA_PATH = os.path.join(BASE_DIR, \\\"results\\\", \\\"generalize\\\",\\n                         \\\"pythia410m_wiki_a100_s42\\\", \\\"all_metrics.json\\\")\\n\\nCANARY_METRICS = [\\\"token_entropy\\\", \\\"ece\\\"]\\nDOWNSTREAM_METRICS = [\\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\", \\\"mauve\\\"]\\n\\nHIGHER_IS_WORSE = {\\\"self_bleu\\\", \\\"ece\\\", \\\"perplexity\\\"}\\nLOWER_IS_WORSE = {\\\"token_entropy\\\", \\\"effective_rank\\\",\\n                  \\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\", \\\"mauve\\\"}\\n\\nMAX_LAG = 1\\nN_PERM = 1000\\nSEED = 42\\nFDR_Q = 0.05\\n\\n\\ndef orient(series, name):\\n    return -series.copy() if name in LOWER_IS_WORSE else series.copy()\\n\\n\\ndef extract(metrics_list, name):\\n    return np.array([m[name] for m in sorted(metrics_list,\\n                                              key=lambda x: x[\\\"generation\\\"])])\\n\\n\\ndef main():\\n    with open(DATA_PATH) as f:\\n        metrics_list = json.load(f)\\n\\n    print(f\\\"Loaded {len(metrics_list)} generations from {DATA_PATH}\\\")\\n    print(f\\\"Parameters: max_lag={MAX_LAG}, n_perm={N_PERM}, seed={SEED}\\\")\\n    print()\\n\\n    # --- Forward sanity check (2 pairs) ---\\n    print(\\\"=\\\" * 70)\\n    print(\\\"FORWARD SANITY CHECK (canary -> downstream)\\\")\\n    print(\\\"-\\\" * 70)\\n    for 
…[truncated 5628 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_opt1b_full_8pair_20260517T124735",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T12:50:47.849662+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "head -80 /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_opt1b_full_8pair_20260517T124735",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "head -80 /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-17T12:50:47.849896+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Method ablation: compare four lead-lag estimation methods.\\n\\nCompares naive vs robust approaches to detect canary->downstream lead-lag,\\nquantifying the spurious regression rate when non-stationary series are\\ncorrelated without proper detrending.\\n\\nInput:  results/mvp/rep_{seed}/all_metrics.json (seeds 42-45)\\nOutput: results/mvp/analysis/method_ablation.json\\n        (with BH FDR correction and effect sizes)\\n\\nMethods:\\n  1. Naive Pearson lag-correlation (raw levels)\\n  2. Differenced cross-correlation (first-differenced series)\\n  3. Threshold-based lead time (2-sigma onset detection)\\n  4. Toda-Yamamoto augmented-lag Granger causality\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport os\\nimport warnings\\nfrom itertools import product\\n\\nimport numpy as np\\nfrom scipy import stats\\nfrom statsmodels.stats.multitest import multipletests\\nfrom statsmodels.tsa.stattools import adfuller\\nfrom permutation_granger import permutation_granger_test\\n\\nwarnings.filterwarnings(\\\"ignore\\\")\\n\\nCANARY = [\\\"token_entropy\\\", \\\"self_bleu\\\", \\\"ece\\\", \\\"effective_rank\\\"]\\nDOWNSTREAM = [\\\"perplexity\\\", \\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\"]\\n\\n# Sign conventions: \\\"higher is worse\\\" kept as-is; \\\"lower is worse\\\" negated\\n# so that degradation = positive direction in all analyses.\\nHIGHER_IS_WORSE = {\\\"self_bleu\\\", \\\"ece\\\", \\\"perplexity\\\"}\\nLOWER_IS_WORSE = {\\\"token_entropy\\\", \\\"effective_rank\\\",\\n                   \\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\"}\\n\\nALPHA = 0.05\\n\\n\\ndef load_metrics(data_dir, seeds):\\n    \\\"\\\"\\\"Load all_metrics.json for each seed.\\\"\\\"\\\"\\n    data = {}\\n    for s in seeds:\\n        path = os.path.join(data_dir, f\\\"rep_{s}\\\", \\\"all_metrics.json\\\")\\n        with open(path) as f:\\n            data[s] = json.load(f)\\n    return 
…[truncated 1260 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_opt1b_full_8pair_20260517T124735",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-17T12:50:47.850065+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "head -30 /root/autodl-tmp/distrib_canary_collapse/results/generalize/opt1b_wiki_a100_s42/all_metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_opt1b_full_8pair_20260517T124735",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "head -30 /root/autodl-tmp/distrib_canary_collapse/results/generalize/opt1b_wiki_a100_s42/all_metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-17T12:50:47.850225+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[\\n  {\\n    \\\"token_entropy\\\": 3.048328940379015,\\n    \\\"self_bleu\\\": 0.009909845233669574,\\n    \\\"distinct_1\\\": 0.10402947839808178,\\n    \\\"distinct_2\\\": 0.5267106260688658,\\n    \\\"distinct_3\\\": 0.816691203046625,\\n    \\\"ece\\\": 0.019933249393078112,\\n    \\\"effective_rank\\\": 65.30501920524436,\\n    \\\"perplexity\\\": 24.876835754631482,\\n    \\\"mauve\\\": 0.031181469084121352,\\n    \\\"generation\\\": 0\\n  },\\n  {\\n    \\\"token_entropy\\\": 1.891728403983633,\\n    \\\"self_bleu\\\": 0.009736369636781457,\\n    \\\"distinct_1\\\": 0.10599251944137987,\\n    \\\"distinct_2\\\": 0.526738303673938,\\n    \\\"distinct_3\\\": 0.8131261940854091,\\n    \\\"ece\\\": 0.1928858748013738,\\n    \\\"effective_rank\\\": 94.87976472875667,\\n    \\\"perplexity\\\": 39.33064744065543,\\n    \\\"mauve\\\": 0.03154995423565758,\\n    \\\"generation\\\": 1\\n  },\\n  {\\n    \\\"token_entropy\\\": 1.440482375630306,\\n    \\\"self_bleu\\\": 0.011732248835009541,\\n    \\\"distinct_1\\\": 0.08458740066760836,\\n    \\\"distinct_2\\\": 0.42675189393939394,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_opt1b_full_8pair_20260517T124735",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-17T12:50:47.850428+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "head -60 /root/autodl-tmp/distrib_canary_collapse/permutation_granger.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_opt1b_full_8pair_20260517T124735",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "head -60 /root/autodl-tmp/distrib_canary_collapse/permutation_granger.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-17T12:50:47.850587+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Permutation-based Granger causality test.\\n\\nUses permutation to build a null distribution of the Granger F-statistic,\\navoiding asymptotic assumptions that fail on short series (T<20).\\nFirst-differences the series to handle non-stationarity, then uses random\\nshuffle (not circular shift) since differencing removes autocorrelation.\\n\\\"\\\"\\\"\\n\\nimport numpy as np\\n\\n\\ndef _build_lag_matrix(y, x, max_lag):\\n    \\\"\\\"\\\"Build design matrices for restricted and unrestricted Granger models.\\\"\\\"\\\"\\n    T = len(y)\\n    n = T - max_lag\\n    Y = y[max_lag:]\\n\\n    cols_r = [np.ones(n)]\\n    for lag in range(1, max_lag + 1):\\n        cols_r.append(y[max_lag - lag: T - lag])\\n\\n    cols_u = list(cols_r)\\n    for lag in range(1, max_lag + 1):\\n        cols_u.append(x[max_lag - lag: T - lag])\\n\\n    X_r = np.column_stack(cols_r)\\n    X_u = np.column_stack(cols_u)\\n    return Y, X_r, X_u\\n\\n\\ndef _granger_f_stat(y, x, max_lag):\\n    \\\"\\\"\\\"Compute Granger F-statistic: does x help predict y beyond y's own lags?\\\"\\\"\\\"\\n    Y, X_r, X_u = _build_lag_matrix(y, x, max_lag)\\n    n = len(Y)\\n    q = max_lag\\n\\n    try:\\n        beta_r = np.linalg.lstsq(X_r, Y, rcond=None)[0]\\n        beta_u = np.linalg.lstsq(X_u, Y, rcond=None)[0]\\n    except np.linalg.LinAlgError:\\n        return np.nan\\n\\n    rss_r = np.sum((Y - X_r @ beta_r) ** 2)\\n    rss_u = np.sum((Y - X_u @ beta_u) ** 2)\\n\\n    k_u = X_u.shape[1]\\n    df_resid = n - k_u\\n\\n    if df_resid <= 0 or rss_u < 1e-15:\\n        return np.nan\\n\\n    F = ((rss_r - rss_u) / q) / (rss_u / df_resid)\\n    return F\\n\\n\\ndef permutation_granger_test(x, y, max_lag=1, n_perm=1000, seed=42,\\n                              difference=True):\\n    \\\"\\\"\\\"Permutation-based Granger causality test.\\n\\n    Tests whether x Granger-causes y using permutation null distribution.\\n\", \"stderr\": \"\", \"
…[truncated 80 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_opt1b_full_8pair_20260517T124735",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-17T12:50:47.850738+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "grep -n \"def \" /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_opt1b_full_8pair_20260517T124735",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "grep -n \"def \" /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-17T12:50:47.850873+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"44:def load_metrics(data_dir, seeds):\\n54:def extract(metrics_list, name):\\n60:def orient(series, name):\\n69:def naive_pearson(c, d, cn, dn, max_lag=3):\\n98:def diff_xcorr(c, d, cn, dn, max_lag=3):\\n129:def _onset_gen(series, name):\\n142:def threshold_lead(c, d, cn, dn):\\n177:def _adf_order(series, max_d=2):\\n193:def toda_yamamoto(c, d, cn, dn):\\n275:def classify_effect_size_r(r_abs):\\n286:def classify_effect_size_f2(f2_val):\\n297:def _apply_fdr_and_effect_size(all_pairs):\\n375:def perm_granger(c, d, cn, dn, max_lag=1, n_perm=1000):\\n401:def main():\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_opt1b_full_8pair_20260517T124735",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-17T12:50:47.850996+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "tail -50 /root/autodl-tmp/distrib_canary_collapse/permutation_granger.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_opt1b_full_8pair_20260517T124735",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "tail -50 /root/autodl-tmp/distrib_canary_collapse/permutation_granger.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-17T12:50:47.851155+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"        hdr = f\\\"{'Canary':<16} {'Downstream':<12}\\\"\\n        for s in seeds:\\n            hdr += f\\\" | s{s} p_raw  p_fdr  sig\\\"\\n        print(hdr)\\n        print(\\\"-\\\" * 70)\\n\\n        for pair in pairs_data:\\n            line = f\\\"{pair['canary']:<16} {pair['downstream']:<12}\\\"\\n            for sr in pair[\\\"per_seed\\\"]:\\n                r = sr[mode]\\n                p_raw = r.get(\\\"p_raw\\\")\\n                p_fdr = r.get(\\\"p_fdr\\\")\\n                sig = r.get(\\\"significant_fdr\\\", False)\\n                p_raw_s = f\\\"{p_raw:.4f}\\\" if p_raw is not None else \\\"  N/A \\\"\\n                p_fdr_s = f\\\"{p_fdr:.4f}\\\" if p_fdr is not None else \\\"  N/A \\\"\\n                sig_s = \\\" *\\\" if sig else \\\"  \\\"\\n                line += f\\\" | {p_raw_s} {p_fdr_s}{sig_s}\\\"\\n            line += f\\\"  [{pair['summary'][mode]['sig_seeds']}/4]\\\"\\n            print(line)\\n\\n    # FDR impact summary\\n    print(\\\"\\\\n\\\" + \\\"=\\\" * 70)\\n    print(\\\"FDR CORRECTION IMPACT\\\")\\n    print(\\\"-\\\" * 70)\\n    for mode in [\\\"differenced\\\", \\\"undifferenced\\\"]:\\n        fs = fdr_summary[mode]\\n        flipped = fs[\\\"raw_significant\\\"] - fs[\\\"fdr_significant\\\"]\\n        print(f\\\"  {mode:<15}: {fs['raw_significant']:>2} raw-sig -> \\\"\\n              f\\\"{fs['fdr_significant']:>2} FDR-sig \\\"\\n              f\\\"(of {fs['total_tests']}, {flipped} flipped)\\\")\\n\\n    # Check for flips\\n    print(\\\"\\\\nFLIPPED PAIRS (raw-sig -> FDR-n.s.)\\\")\\n    print(\\\"-\\\" * 70)\\n    any_flip = False\\n    for pair in pairs_data:\\n        for sr in pair[\\\"per_seed\\\"]:\\n            for mode in [\\\"differenced\\\", \\\"undifferenced\\\"]:\\n                r = sr[mode]\\n                p_raw = r.get(\\\"p_raw\\\")\\n                sig_fdr = r.get(\\\"significant_fdr\\\", False)\\n                if p_raw is not None a
…[truncated 510 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_opt1b_full_8pair_20260517T124735",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-17T12:50:47.851355+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_opt1b_full_8pair_20260517T124735",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-17T12:50:47.851635+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Method ablation: compare four lead-lag estimation methods.\\n\\nCompares naive vs robust approaches to detect canary->downstream lead-lag,\\nquantifying the spurious regression rate when non-stationary series are\\ncorrelated without proper detrending.\\n\\nInput:  results/mvp/rep_{seed}/all_metrics.json (seeds 42-45)\\nOutput: results/mvp/analysis/method_ablation.json\\n        (with BH FDR correction and effect sizes)\\n\\nMethods:\\n  1. Naive Pearson lag-correlation (raw levels)\\n  2. Differenced cross-correlation (first-differenced series)\\n  3. Threshold-based lead time (2-sigma onset detection)\\n  4. Toda-Yamamoto augmented-lag Granger causality\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport os\\nimport warnings\\nfrom itertools import product\\n\\nimport numpy as np\\nfrom scipy import stats\\nfrom statsmodels.stats.multitest import multipletests\\nfrom statsmodels.tsa.stattools import adfuller\\nfrom permutation_granger import permutation_granger_test\\n\\nwarnings.filterwarnings(\\\"ignore\\\")\\n\\nCANARY = [\\\"token_entropy\\\", \\\"self_bleu\\\", \\\"ece\\\", \\\"effective_rank\\\"]\\nDOWNSTREAM = [\\\"perplexity\\\", \\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\"]\\n\\n# Sign conventions: \\\"higher is worse\\\" kept as-is; \\\"lower is worse\\\" negated\\n# so that degradation = positive direction in all analyses.\\nHIGHER_IS_WORSE = {\\\"self_bleu\\\", \\\"ece\\\", \\\"perplexity\\\"}\\nLOWER_IS_WORSE = {\\\"token_entropy\\\", \\\"effective_rank\\\",\\n                   \\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\"}\\n\\nALPHA = 0.05\\n\\n\\ndef load_metrics(data_dir, seeds):\\n    \\\"\\\"\\\"Load all_metrics.json for each seed.\\\"\\\"\\\"\\n    data = {}\\n    for s in seeds:\\n        path = os.path.join(data_dir, f\\\"rep_{s}\\\", \\\"all_metrics.json\\\")\\n        with open(path) as f:\\n            data[s] = json.load(f)\\n    return 
…[truncated 7427 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_opt1b_full_8pair_20260517T124735",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-17T12:50:47.851917+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "cat > /root/autodl-tmp/distrib_canary_collapse/analyze_opt1b_full.py << 'SCRIPT'\n\"\"\"Full 6-method analysis for OPT-1.3B generalize experiment.\n\n8 canonical pairs: {token_entropy, ece} x {distinct_1, distinct_2, distinct_3, mauve}\n6 methods: Naive XCorr, Diff XCorr (FDR), Threshold Onset, PermG forward (FDR),\n           PermG reverse (FDR), TY Granger\n\"\"\"\n\nimport json\nimport os\nimport sys\nimport warnings\nfrom datetime import datetime\n\nimport numpy as np\nfrom scipy import stats\nfrom statsmodels.stats.multitest import multipletests\nfrom statsmodels.tsa.stattools import adfuller\n\nwarnings.filterwarnings(\"ignore\")\n\nBASE_DIR = os.path.dirname(os.path.abspath(__file__))\nsys.path.insert(0, BASE_DIR)\nfrom permutation_granger import permutation_granger_test\n\n# 8 canonical pairs\nCANARY = [\"token_entropy\", \"ece\"]\nDOWNSTREAM = [\"distinct_1\", \"distinct_2\", \"distinct_3\", \"mauve\"]\n\nHIGHER_IS_WORSE = {\"self_bleu\", \"ece\", \"perplexity\"}\nLOWER_IS_WORSE = {\"token_entropy\", \"effective_rank\",\n                  \"distinct_1\", \"distinct_2\", \"distinct_3\", \"mauve\"}\n\nALPHA = 0.05\nMAX_LAG = 1\nN_PERM = 1000\nSEED = 42\n\nDATA_DIR = os.path.join(BASE_DIR, \"results\", \"generalize\", \"opt1b_wiki_a100_s42\")\n\n\ndef extract(metrics_list, name):\n    return np.array([m[name] for m in sorted(metrics_list, key=lambda x: x[\"generation\"])])\n\n\ndef orient(series, name):\n    return -series.copy() if name in LOWER_IS_WORSE else series.copy()\n\n\ndef naive_pearson(c, d, cn, dn):\n    x, y = orient(c, cn), orient(d, dn)\n    n = len(x)\n    best_lag, best_r, best_p = 0, 0.0, 1.0\n    for lag in range(-MAX_LAG, MAX_LAG + 1):\n        if lag >= 0:\n            a, b = x[lag:], y[:n - lag]\n        else:\n            a, b = x[:n + lag], y[-lag:]\n        if len(a) < 4:\n            continue\n        r, p = stats.pearsonr(a, b)\n        if abs(r) > abs(best_r):\n            best_lag, best_r, best_p = lag, r, p\n    return {\"method\": \"naive_pearson\", \"lag\": int(best_lag),\n            \"r\": round(float(best_r), 4), \"p_value\": round(float(best_p), 6),\n            \"significant\": bool(best_p < ALPHA)}\n\n\ndef diff_xcorr(c, d, cn, dn):\n    dx, dy = np.diff(orient(c, cn)), np.diff(orient(d, dn))\n    n = len(dx)\n    best_lag, best_r, best_p = 0, 0.0, 1.0\n    for lag in range(-MAX_LAG, MAX_LAG + 1):\n        if lag >= 0:\n            a, b = dx[lag:], dy[:n - lag]\n        else:\n            a, b = dx[:n + lag], dy[-lag:]\n        if len(a) < 4:\n            continue\n        if np.std(a) < 1e-12 or np.std(b) < 1e-12:\n            continue\n        r, p = stats.pearsonr(a, b)\n        if abs(r) > abs(best_r):\n            best_lag, best_r, best_p = lag, r, p\n    return {\"method\": \"diff_xcorr\", \"lag\": int(best_lag),\n            \"r\": round(float(best_r), 4), \"p_value\": round(float(best_p), 6),\n            \"significant\": bool(best_p < ALPHA)}\n\n\ndef threshold_onset(c, d, cn, dn):\n    xo, yo = orient(c, cn), orient(d, dn)\n    def _onset(s):\n        mu, sigma = s[:3].mean(), s[:3].std()\n        if sigma < 1e-12:\n            sigma = abs(mu) * 0.01 if abs(mu) > 1e-12 else 1e-6\n        threshold = mu + 2.0 * sigma\n        for i, v in enumerate(s):\n            if v > threshold:\n                return i\n        return None\n    c_onset = _onset(xo)\n    d_onset = _onset(yo)\n    if c_onset is None or d_onset is None:\n        return {\"method\": \"threshold_onset\", \"canary_onset\": c_onset,\n                \"downstream_onset\": d_onset, \"lead_time\": None, \"significant\": False}\n    lead = d_onset - c_onset\n    return {\"method\": \"threshold_onset\", \"canary_onset\": int(c_onset),\n            \"downstream_onset\": int(d_onset), \"lead_time\": int(lead),\n            \"significant\": bool(lead > 0)}\n\n\ndef permg_forward(c, d, cn, dn):\n    x, y = orient(c, cn), orient(d, dn)\n    res = permutation_granger_test(x, y, max_lag=MAX_LAG, n_perm=N_PERM,\n                                   seed=SEED, difference=True)\n    return {\"method\": \"permg_forward\", \"f_stat\": round(float(res[\"f_stat\"]), 4) if res[\"f_stat\"] is not None and not np.isnan(res[\"f_stat\"]) else None,\n            \"p_value\": round(float(res[\"p_value\"]), 6) if res[\"p_value\"] is not None else None,\n            \"significant\": bool(res.get(\"significant\", False))}\n\n\ndef permg_reverse(c, d, cn, dn):\n    x, y = orient(c, cn), orient(d, dn)\n    # Reverse: downstream -> canary\n    res = permutation_granger_test(y, x, max_lag=MAX_LAG, n_perm=N_PERM,\n                                   seed=SEED, difference=True)\n    return {\"method\": \"permg_reverse\", \"f_stat\": round(float(res[\"f_stat\"]), 4) if res[\"f_stat\"] is not None and not np.isnan(res[\"f_stat\"]) else None,\n            \"p_value\": round(float(res[\"p_value\"]), 6) if res[\"p_value\"] is not None else None,\n            \"significant\": bool(res.get(\"significant\", False))}\n\n\ndef _adf_order(series, max_d=2):\n    for d in range(max_d + 1):\n        s = series.copy()\n        for _ in range(d):\n            s = np.diff(s)\n        if len(s) < 4:\n            return d\n        try:\n            _, p, *_ = adfuller(s, maxlag=1)\n            if p < 0.05:\n                return d\n        except:\n            pass\n    return max_d\n\n\ndef toda_yamamoto(c, d, cn, dn):\n    x, y = orient(c, cn), orient(d, dn)\n    d_x = _adf_order(x)\n    d_y = _adf_order(y)\n    d_max = max(d_x, d_y)\n    k = 1  # VAR lag order\n    p_aug = k + d_max\n    T = len(x)\n    \n    if T - p_aug - 1 <= 0:\n        return {\"method\": \"toda_yamamoto\", \"d_max\": int(d_max), \"k\": k,\n                \"wald_F\": None, \"p_value\": None, \"significant\": False,\n                \"note\": \"insufficient_df\"}\n    \n    # Build VAR(p_aug) for y equation\n    n = T - p_aug\n    Y = y[p_aug:]\n    cols = [np.ones(n)]\n    for lag in range(1, p_aug + 1):\n        cols.append(y[p_aug - lag: T - lag])\n    for lag in range(1, p_aug + 1):\n        cols.append(x[p_aug - lag: T - lag])\n    X_u = np.column_stack(cols)\n    \n    # Restricted: drop x lags 1..k (keep augmented x lags k+1..p_aug)\n    # In X_u: cols are [const, y_lag1..y_lag_paug, x_lag1..x_lag_paug]\n    # x lags start at index 1 + p_aug\n    # We want to test x_lag1..x_lagk (indices 1+p_aug .. 1+p_aug+k-1)\n    x_start = 1 + p_aug\n    restrict_idx = list(range(x_start, x_start + k))\n    keep_idx = [i for i in range(X_u.shape[1]) if i not in restrict_idx]\n    X_r = X_u[:, keep_idx]\n    \n    try:\n        beta_u = np.linalg.lstsq(X_u, Y, rcond=None)[0]\n        beta_r = np.linalg.lstsq(X_r, Y, rcond=None)[0]\n    except:\n        return {\"method\": \"toda_yamamoto\", \"d_max\": int(d_max), \"k\": k,\n                \"wald_F\": None, \"p_value\": None, \"significant\": False, \"note\": \"lstsq_fail\"}\n    \n    rss_u = np.sum((Y - X_u @ beta_u) ** 2)\n    rss_r = np.sum((Y - X_r @ beta_r) ** 2)\n    \n    q = k\n    df_resid = n - X_u.shape[1]\n    if df_resid <= 0 or rss_u < 1e-15:\n        return {\"method\": \"toda_yamamoto\", \"d_max\": int(d_max), \"k\": k,\n                \"wald_F\": None, \"p_value\": None, \"significant\": False,\n                \"note\": f\"df_resid={df_resid}\"}\n    \n    F = ((rss_r - rss_u) / q) / (rss_u / df_resid)\n    p_val = 1 - stats.f.cdf(F, q, df_resid)\n    \n    return {\"method\": \"toda_yamamoto\", \"d_max\": int(d_max), \"k\": k,\n            \"df_resid\": int(df_resid), \"wald_F\": round(float(F), 4),\n            \"p_value\": round(float(p_val), 6), \"significant\": bool(p_val < ALPHA)}\n\n\ndef main():\n    all_metrics_path = os.path.join(DATA_DIR, \"all_metrics.json\")\n    with open(all_metrics_path) as f:\n        metrics_list = json.load(f)\n    \n    T = len(metrics_list)\n    print(f\"OPT-1.3B WikiText a=1.0 s42 | T={T} generations\")\n    print()\n    \n    # Collapse trajectory\n    print(\"=\" * 70)\n    print(\"COLLAPSE TRAJECTORY\")\n    print(\"-\" * 70)\n    all_metrics_names = [\"token_entropy\", \"ece\", \"perplexity\",\n                         \"distinct_1\", \"distinct_2\", \"distinct_3\", \"mauve\"]\n    gen0 = metrics_list[0]\n    genN = metrics_list[-1]\n    print(f\"  {'metric':<16} {'gen0':>12} {'gen10':>12} {'drift%':>10}\")\n    print(f\"  {'-'*50}\")\n    trajectory = {}\n    for m in all_metrics_names:\n        v0, vN = gen0[m], genN[m]\n        drift = (vN - v0) / abs(v0) * 100 if abs(v0) > 1e-12 else 0.0\n        print(f\"  {m:<16} {v0:>12.6f} {vN:>12.6f} {drift:>+9.1f}%\")\n        trajectory[m] = {\"gen0\": v0, \"gen10\": vN, \"drift_pct\": round(drift, 2)}\n    \n    # Run 6 methods on 8 pairs\n    print()\n    print(\"=\" * 70)\n    print(\"6-METHOD ANALYSIS (8 canonical pairs)\")\n    print(\"-\" * 70)\n    \n    methods = [\n        (\"naive_xcorr\", naive_pearson),\n        (\"diff_xcorr\", diff_xcorr),\n        (\"threshold_onset\", threshold_onset),\n        (\"permg_fwd\", permg_forward),\n        (\"permg_rev\", permg_reverse),\n        (\"ty_granger\", toda_yamamoto),\n    ]\n    \n    pair_results = {}\n    # Collect p-values for FDR correction per method group\n    fdr_groups = {name: [] for name, _ in methods}\n    fdr_keys = {name: [] for name, _ in methods}\n    \n    for cn in CANARY:\n        for dn in DOWNSTREAM:\n            pair_key = f\"{cn}->{dn}\"\n            c = extract(metrics_list, cn)\n            d = extract(metrics_list, dn)\n            \n            pair_results[pair_key] = {}\n            for method_name, method_fn in methods:\n                try:\n                    res = method_fn(c, d, cn, dn)\n                except Exception as e:\n                    res = {\"method\": method_name, \"error\": str(e), \"significant\": False}\n                pair_results[pair_key][method_name] = res\n                \n                p = res.get(\"p_value\")\n                if p is not None:\n                    fdr_groups[method_name].append(p)\n                    fdr_keys[method_name].append(pair_key)\n    \n    # Apply BH FDR correction per method\n    for method_name in fdr_groups:\n        ps = fdr_groups[method_name]\n        keys = fdr_keys[method_name]\n        if not ps:\n            continue\n        _, fdr_ps, _, _ = multipletests(ps, method=\"fdr_bh\")\n        for i, pk in enumerate(keys):\n            pair_results[pk][method_name][\"p_fdr\"] = round(float(fdr_ps[i]), 6)\n            pair_results[pk][method_name][\"sig_fdr\"] = bool(fdr_ps[i] < ALPHA)\n    \n    # For methods with FDR, use sig_fdr as final significance\n    # For threshold_onset (no p-value, uses lead>0), keep original\n    def is_sig(pair_key, method_name):\n        r = pair_results[pair_key][method_name]\n        if \"sig_fdr\" in r:\n            return r[\"sig_fdr\"]\n        return r.get(\"significant\", False)\n    \n    # Summary table\n    print()\n    print(\"TABLE 5 ROW (OPT-1.3B):\")\n    print(f\"{'Method':<22} | {'Sig':>3} | Sig Pairs\")\n    print(\"-\" * 70)\n    method_sig_counts = {}\n    for method_name, _ in methods:\n        sig_pairs = []\n        for cn in CANARY:\n            for dn in DOWNSTREAM:\n                pk = f\"{cn}->{dn}\"\n                if is_sig(pk, method_name):\n                    sig_pairs.append(pk)\n        method_sig_counts[method_name] = sig_pairs\n        print(f\"{method_name:<22} | {len(sig_pairs):>1}/8 | {', '.join(sig_pairs) if sig_pairs else '(none)'}\")\n    \n    # Consensus (exclude TY and reverse PermG from consensus = use first 4 forward methods)\n    # Actually task says \"Consensus >=3/5\" implying 5 methods for consensus\n    # Use: naive, diff, threshold, permg_fwd, ty (the 5 \"forward\" methods)\n    consensus_methods = [\"naive_xcorr\", \"diff_xcorr\", \"threshold_onset\", \"permg_fwd\", \"ty_granger\"]\n    consensus_3 = []\n    consensus_4 = []\n    for cn in CANARY:\n        for dn in DOWNSTREAM:\n            pk = f\"{cn}->{dn}\"\n            votes = sum(1 for m in consensus_methods if is_sig(pk, m))\n            if votes >= 3:\n                consensus_3.append(pk)\n            if votes >= 4:\n                consensus_4.append(pk)\n    \n    print(f\"{'Consensus >=3/5':<22} | {len(consensus_3):>1}/8 | {', '.join(consensus_3) if consensus_3 else '(none)'}\")\n    print(f\"{'Consensus >=4/5':<22} | {len(consensus_4):>1}/8 | {', '.join(consensus_4) if consensus_4 else '(none)'}\")\n    \n    # Per-pair detail table\n    print()\n    print(\"PER-PAIR DETAIL:\")\n    print(f\"{'Pair':<22} | {'Naive':>5} | {'Diff':>5} | {'Thresh':>6} | {'PG_f':>5} | {'PG_r':>5} | {'TY':>5} | votes\")\n    print(\"-\" * 80)\n    for cn in CANARY:\n        for dn in DOWNSTREAM:\n            pk = f\"{cn}->{dn}\"\n            sigs = []\n            for mn in [\"naive_xcorr\", \"diff_xcorr\", \"threshold_onset\", \"permg_fwd\", \"permg_rev\", \"ty_granger\"]:\n                s = is_sig(pk, mn)\n                sigs.append(\"Y\" if s else \"N\")\n            votes_5 = sum(1 for mn in consensus_methods if is_sig(pk, mn))\n            print(f\"{pk:<22} | {sigs[0]:>5} | {sigs[1]:>5} | {sigs[2]:>6} | {sigs[3]:>5} | {sigs[4]:>5} | {sigs[5]:>5} | {votes_5}/5\")\n    \n    # Detailed p-values\n    print()\n    print(\"P-VALUES (raw / FDR):\")\n    print(f\"{'Pair':<22} | {'Naive p':>8} | {'Diff p_fdr':>10} | {'PG_f p_fdr':>10} | {'PG_r p_fdr':>10} | {'TY p_fdr':>8}\")\n    print(\"-\" * 80)\n    for cn in CANARY:\n        for dn in DOWNSTREAM:\n            pk = f\"{cn}->{dn}\"\n            naive_p = pair_results[pk][\"naive_xcorr\"].get(\"p_value\", None)\n            diff_p = pair_results[pk][\"diff_xcorr\"].get(\"p_fdr\", None)\n            pgf_p = pair_results[pk][\"permg_fwd\"].get(\"p_fdr\", None)\n            pgr_p = pair_results[pk][\"permg_rev\"].get(\"p_fdr\", None)\n            ty_p = pair_results[pk][\"ty_granger\"].get(\"p_fdr\", None)\n            \n            def fmt(v):\n                return f\"{v:.4f}\" if v is not None else \"N/A\"\n            \n            print(f\"{pk:<22} | {fmt(naive_p):>8} | {fmt(diff_p):>10} | {fmt(pgf_p):>10} | {fmt(pgr_p):>10} | {fmt(ty_p):>8}\")\n    \n    # Save JSON\n    out_dir = os.path.join(DATA_DIR, \"analysis\")\n    os.makedirs(out_dir, exist_ok=True)\n    \n    output = {\n        \"experiment\": \"opt1b_wiki_a100_s42\",\n        \"model\": \"facebook/opt-1.3b\",\n        \"dataset\": \"wikitext-103\",\n        \"alpha\": 1.0,\n        \"seed\": 42,\n        \"n_generations\": T,\n        \"timestamp\": datetime.now().isoformat(),\n        \"parameters\": {\n            \"max_lag\": MAX_LAG,\n            \"n_perm\": N_PERM,\n            \"seed\": SEED,\n            \"fdr_method\": \"fdr_bh\",\n            \"fdr_q\": ALPHA,\n        },\n        \"trajectory\": trajectory,\n        \"pair_results\": pair_results,\n        \"summary\": {\n            \"method_sig_counts\": {k: len(v) for k, v in method_sig_counts.items()},\n            \"method_sig_pairs\": {k: v for k, v in method_sig_counts.items()},\n            \"consensus_3of5\": consensus_3,\n            \"consensus_4of5\": consensus_4,\n        },\n    }\n    \n    class NumpyEncoder(json.JSONEncoder):\n        def default(self, obj):\n            if isinstance(obj, (np.integer,)):\n                return int(obj)\n            if isinstance(obj, (np.floating,)):\n                return float(obj)\n            if isinstance(obj, np.ndarray):\n                return obj.tolist()\n            if isinstance(obj, (np.bool_,)):\n                return bool(obj)\n            return super().default(obj)\n    \n    out_path = os.path.join(out_dir, \"opt1b_6method_full.json\")\n    with open(out_path, \"w\") as f:\n        json.dump(output, f, indent=2, cls=NumpyEncoder)\n    print(f\"\\nSaved: {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_opt1b_full_8pair_20260517T124735",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat > /root/autodl-tmp/distrib_canary_collapse/analyze_opt1b_full.py << 'SCRIPT'\n\"\"\"Full 6-method analysis for OPT-1.3B generalize experiment.\n\n8 canonical pairs: {token_entropy, ece} x {distinct_1, distinct_2, distinct_3, mauve}\n6 methods: Naive XCorr, Diff XCorr (FDR), Threshold Onset, PermG forward (FDR),\n           PermG reverse (FDR), TY Granger\n\"\"\"\n\nimport json\nimport os\nimport sys\nimport warnings\nfrom datetime import datetime\n\nimport numpy as np\nfrom scipy import stats\nfrom statsmodels.stats.multitest import multipletests\nfrom statsmodels.tsa.stattools import adfuller\n\nwarnings.filterwarnings(\"ignore\")\n\nBASE_DIR = os.path.dirname(os.path.abspath(__file__))\nsys.path.insert(0, BASE_DIR)\nfrom permutation_granger import permutation_granger_test\n\n# 8 canonical pairs\nCANARY = [\"token_entropy\", \"ece\"]\nDOWNSTREAM = [\"distinct_1\", \"distinct_2\", \"distinct_3\", \"mauve\"]\n\nHIGHER_IS_WORSE = {\"self_bleu\", \"ece\", \"perplexity\"}\nLOWER_IS_WORSE = {\"token_entropy\", \"effective_rank\",\n                  \"distinct_1\", \"distinct_2\", \"distinct_3\", \"mauve\"}\n\nALPHA = 0.05\nMAX_LAG = 1\nN_PERM = 1000\nSEED = 42\n\nDATA_DIR = os.path.join(BASE_DIR, \"results\", \"generalize\", \"opt1b_wiki_a100_s42\")\n\n\ndef extract(metrics_list, name):\n    return np.array([m[name] for m in sorted(metrics_list, key=lambda x: x[\"generation\"])])\n\n\ndef orient(series, name):\n    return -series.copy() if name in LOWER_IS_WORSE else series.copy()\n\n\ndef naive_pearson(c, d, cn, dn):\n    x, y = orient(c, cn), orient(d, dn)\n    n = len(x)\n    best_lag, best_r, best_p = 0, 0.0, 1.0\n    for lag in range(-MAX_LAG, MAX_LAG + 1):\n        if lag >= 0:\n            a, b = x[lag:], y[:n - lag]\n        else:\n            a, b = x[:n + lag], y[-lag:]\n        if len(a) < 4:\n            continue\n        r, p = stats.pearsonr(a, b)\n        if abs(r) > abs(best_r):\n            best_lag, best_r, best_p = lag, r, p\n    return {\"method\": \"naive_pearson\", \"lag\": int(best_lag),\n            \"r\": round(float(best_r), 4), \"p_value\": round(float(best_p), 6),\n            \"significant\": bool(best_p < ALPHA)}\n\n\ndef diff_xcorr(c, d, cn, dn):\n    dx, dy = np.diff(orient(c, cn)), np.diff(orient(d, dn))\n    n = len(dx)\n    best_lag, best_r, best_p = 0, 0.0, 1.0\n    for lag in range(-MAX_LAG, MAX_LAG + 1):\n        if lag >= 0:\n            a, b = dx[lag:], dy[:n - lag]\n        else:\n            a, b = dx[:n + lag], dy[-lag:]\n        if len(a) < 4:\n            continue\n        if np.std(a) < 1e-12 or np.std(b) < 1e-12:\n            continue\n        r, p = stats.pearsonr(a, b)\n        if abs(r) > abs(best_r):\n            best_lag, best_r, best_p = lag, r, p\n    return {\"method\": \"diff_xcorr\", \"lag\": int(best_lag),\n            \"r\": round(float(best_r), 4), \"p_value\": round(float(best_p), 6),\n            \"significant\": bool(best_p < ALPHA)}\n\n\ndef threshold_onset(c, d, cn, dn):\n    xo, yo = orient(c, cn), orient(d, dn)\n    def _onset(s):\n        mu, sigma = s[:3].mean(), s[:3].std()\n        if sigma < 1e-12:\n            sigma = abs(mu) * 0.01 if abs(mu) > 1e-12 else 1e-6\n        threshold = mu + 2.0 * sigma\n        for i, v in enumerate(s):\n            if v > threshold:\n                return i\n        return None\n    c_onset = _onset(xo)\n    d_onset = _onset(yo)\n    if c_onset is None or d_onset is None:\n        return {\"method\": \"threshold_onset\", \"canary_onset\": c_onset,\n                \"downstream_onset\": d_onset, \"lead_time\": None, \"significant\": False}\n    lead = d_onset - c_onset\n    return {\"method\": \"threshold_onset\", \"canary_onset\": int(c_onset),\n            \"downstream_onset\": int(d_onset), \"lead_time\": int(lead),\n            \"significant\": bool(lead > 0)}\n\n\ndef permg_forward(c, d, cn, dn):\n    x, y = orient(c, cn), orient(d, dn)\n    res = permutation_granger_test(x, y, max_lag=MAX_LAG, n_perm=N_PERM,\n                                   seed=SEED, difference=True)\n    return {\"method\": \"permg_forward\", \"f_stat\": round(float(res[\"f_stat\"]), 4) if res[\"f_stat\"] is not None and not np.isnan(res[\"f_stat\"]) else None,\n            \"p_value\": round(float(res[\"p_value\"]), 6) if res[\"p_value\"] is not None else None,\n            \"significant\": bool(res.get(\"significant\", False))}\n\n\ndef permg_reverse(c, d, cn, dn):\n    x, y = orient(c, cn), orient(d, dn)\n    # Reverse: downstream -> canary\n    res = permutation_granger_test(y, x, max_lag=MAX_LAG, n_perm=N_PERM,\n                                   seed=SEED, difference=True)\n    return {\"method\": \"permg_reverse\", \"f_stat\": round(float(res[\"f_stat\"]), 4) if res[\"f_stat\"] is not None and not np.isnan(res[\"f_stat\"]) else None,\n            \"p_value\": round(float(res[\"p_value\"]), 6) if res[\"p_value\"] is not None else None,\n            \"significant\": bool(res.get(\"significant\", False))}\n\n\ndef _adf_order(series, max_d=2):\n    for d in range(max_d + 1):\n        s = series.copy()\n        for _ in range(d):\n            s = np.diff(s)\n        if len(s) < 4:\n            return d\n        try:\n            _, p, *_ = adfuller(s, maxlag=1)\n            if p < 0.05:\n                return d\n        except:\n            pass\n    return max_d\n\n\ndef toda_yamamoto(c, d, cn, dn):\n    x, y = orient(c, cn), orient(d, dn)\n    d_x = _adf_order(x)\n    d_y = _adf_order(y)\n    d_max = max(d_x, d_y)\n    k = 1  # VAR lag order\n    p_aug = k + d_max\n    T = len(x)\n    \n    if T - p_aug - 1 <= 0:\n        return {\"method\": \"toda_yamamoto\", \"d_max\": int(d_max), \"k\": k,\n                \"wald_F\": None, \"p_value\": None, \"significant\": False,\n                \"note\": \"insufficient_df\"}\n    \n    # Build VAR(p_aug) for y equation\n    n = T - p_aug\n    Y = y[p_aug:]\n    cols = [np.ones(n)]\n    for lag in range(1, p_aug + 1):\n        cols.append(y[p_aug - lag: T - lag])\n    for lag in range(1, p_aug + 1):\n        cols.append(x[p_aug - lag: T - lag])\n    X_u = np.column_stack(cols)\n    \n    # Restricted: drop x lags 1..k (keep augmented x lags k+1..p_aug)\n    # In X_u: cols are [const, y_lag1..y_lag_paug, x_lag1..x_lag_paug]\n    # x lags start at index 1 + p_aug\n    # We want to test x_lag1..x_lagk (indices 1+p_aug .. 1+p_aug+k-1)\n    x_start = 1 + p_aug\n    restrict_idx = list(range(x_start, x_start + k))\n    keep_idx = [i for i in range(X_u.shape[1]) if i not in restrict_idx]\n    X_r = X_u[:, keep_idx]\n    \n    try:\n        beta_u = np.linalg.lstsq(X_u, Y, rcond=None)[0]\n        beta_r = np.linalg.lstsq(X_r, Y, rcond=None)[0]\n    except:\n        return {\"method\": \"toda_yamamoto\", \"d_max\": int(d_max), \"k\": k,\n                \"wald_F\": None, \"p_value\": None, \"significant\": False, \"note\": \"lstsq_fail\"}\n    \n    rss_u = np.sum((Y - X_u @ beta_u) ** 2)\n    rss_r = np.sum((Y - X_r @ beta_r) ** 2)\n    \n    q = k\n    df_resid = n - X_u.shape[1]\n    if df_resid <= 0 or rss_u < 1e-15:\n        return {\"method\": \"toda_yamamoto\", \"d_max\": int(d_max), \"k\": k,\n                \"wald_F\": None, \"p_value\": None, \"significant\": False,\n                \"note\": f\"df_resid={df_resid}\"}\n    \n    F = ((rss_r - rss_u) / q) / (rss_u / df_resid)\n    p_val = 1 - stats.f.cdf(F, q, df_resid)\n    \n    return {\"method\": \"toda_yamamoto\", \"d_max\": int(d_max), \"k\": k,\n            \"df_resid\": int(df_resid), \"wald_F\": round(float(F), 4),\n            \"p_value\": round(float(p_val), 6), \"significant\": bool(p_val < ALPHA)}\n\n\ndef main():\n    all_metrics_path = os.path.join(DATA_DIR, \"all_metrics.json\")\n    with open(all_metrics_path) as f:\n        metrics_list = json.load(f)\n    \n    T = len(metrics_list)\n    print(f\"OPT-1.3B WikiText a=1.0 s42 | T={T} generations\")\n    print()\n    \n    # Collapse trajectory\n    print(\"=\" * 70)\n    print(\"COLLAPSE TRAJECTORY\")\n    print(\"-\" * 70)\n    all_metrics_names = [\"token_entropy\", \"ece\", \"perplexity\",\n                         \"distinct_1\", \"distinct_2\", \"distinct_3\", \"mauve\"]\n    gen0 = metrics_list[0]\n    genN = metrics_list[-1]\n    print(f\"  {'metric':<16} {'gen0':>12} {'gen10':>12} {'drift%':>10}\")\n    print(f\"  {'-'*50}\")\n    trajectory = {}\n    for m in all_metrics_names:\n        v0, vN = gen0[m], genN[m]\n        drift = (vN - v0) / abs(v0) * 100 if abs(v0) > 1e-12 else 0.0\n        print(f\"  {m:<16} {v0:>12.6f} {vN:>12.6f} {drift:>+9.1f}%\")\n        trajectory[m] = {\"gen0\": v0, \"gen10\": vN, \"drift_pct\": round(drift, 2)}\n    \n    # Run 6 methods on 8 pairs\n    print()\n    print(\"=\" * 70)\n    print(\"6-METHOD ANALYSIS (8 canonical pairs)\")\n    print(\"-\" * 70)\n    \n    methods = [\n        (\"naive_xcorr\", naive_pearson),\n        (\"diff_xcorr\", diff_xcorr),\n        (\"threshold_onset\", threshold_onset),\n        (\"permg_fwd\", permg_forward),\n        (\"permg_rev\", permg_reverse),\n        (\"ty_granger\", toda_yamamoto),\n    ]\n    \n    pair_results = {}\n    # Collect p-values for FDR correction per method group\n    fdr_groups = {name: [] for name, _ in methods}\n    fdr_keys = {name: [] for name, _ in methods}\n    \n    for cn in CANARY:\n        for dn in DOWNSTREAM:\n            pair_key = f\"{cn}->{dn}\"\n            c = extract(metrics_list, cn)\n            d = extract(metrics_list, dn)\n            \n            pair_results[pair_key] = {}\n            for method_name, method_fn in methods:\n                try:\n                    res = method_fn(c, d, cn, dn)\n                except Exception as e:\n                    res = {\"method\": method_name, \"error\": str(e), \"significant\": False}\n                pair_results[pair_key][method_name] = res\n                \n                p = res.get(\"p_value\")\n                if p is not None:\n                    fdr_groups[method_name].append(p)\n                    fdr_keys[method_name].append(pair_key)\n    \n    # Apply BH FDR correction per method\n    for method_name in fdr_groups:\n        ps = fdr_groups[method_name]\n        keys = fdr_keys[method_name]\n        if not ps:\n            continue\n        _, fdr_ps, _, _ = multipletests(ps, method=\"fdr_bh\")\n        for i, pk in enumerate(keys):\n            pair_results[pk][method_name][\"p_fdr\"] = round(float(fdr_ps[i]), 6)\n            pair_results[pk][method_name][\"sig_fdr\"] = bool(fdr_ps[i] < ALPHA)\n    \n    # For methods with FDR, use sig_fdr as final significance\n    # For threshold_onset (no p-value, uses lead>0), keep original\n    def is_sig(pair_key, method_name):\n        r = pair_results[pair_key][method_name]\n        if \"sig_fdr\" in r:\n            return r[\"sig_fdr\"]\n        return r.get(\"significant\", False)\n    \n    # Summary table\n    print()\n    print(\"TABLE 5 ROW (OPT-1.3B):\")\n    print(f\"{'Method':<22} | {'Sig':>3} | Sig Pairs\")\n    print(\"-\" * 70)\n    method_sig_counts = {}\n    for method_name, _ in methods:\n        sig_pairs = []\n        for cn in CANARY:\n            for dn in DOWNSTREAM:\n                pk = f\"{cn}->{dn}\"\n                if is_sig(pk, method_name):\n                    sig_pairs.append(pk)\n        method_sig_counts[method_name] = sig_pairs\n        print(f\"{method_name:<22} | {len(sig_pairs):>1}/8 | {', '.join(sig_pairs) if sig_pairs else '(none)'}\")\n    \n    # Consensus (exclude TY and reverse PermG from consensus = use first 4 forward methods)\n    # Actually task says \"Consensus >=3/5\" implying 5 methods for consensus\n    # Use: naive, diff, threshold, permg_fwd, ty (the 5 \"forward\" methods)\n    consensus_methods = [\"naive_xcorr\", \"diff_xcorr\", \"threshold_onset\", \"permg_fwd\", \"ty_granger\"]\n    consensus_3 = []\n    consensus_4 = []\n    for cn in CANARY:\n        for dn in DOWNSTREAM:\n            pk = f\"{cn}->{dn}\"\n            votes = sum(1 for m in consensus_methods if is_sig(pk, m))\n            if votes >= 3:\n                consensus_3.append(pk)\n            if votes >= 4:\n                consensus_4.append(pk)\n    \n    print(f\"{'Consensus >=3/5':<22} | {len(consensus_3):>1}/8 | {', '.join(consensus_3) if consensus_3 else '(none)'}\")\n    print(f\"{'Consensus >=4/5':<22} | {len(consensus_4):>1}/8 | {', '.join(consensus_4) if consensus_4 else '(none)'}\")\n    \n    # Per-pair detail table\n    print()\n    print(\"PER-PAIR DETAIL:\")\n    print(f\"{'Pair':<22} | {'Naive':>5} | {'Diff':>5} | {'Thresh':>6} | {'PG_f':>5} | {'PG_r':>5} | {'TY':>5} | votes\")\n    print(\"-\" * 80)\n    for cn in CANARY:\n        for dn in DOWNSTREAM:\n            pk = f\"{cn}->{dn}\"\n            sigs = []\n            for mn in [\"naive_xcorr\", \"diff_xcorr\", \"threshold_onset\", \"permg_fwd\", \"permg_rev\", \"ty_granger\"]:\n                s = is_sig(pk, mn)\n                sigs.append(\"Y\" if s else \"N\")\n            votes_5 = sum(1 for mn in consensus_methods if is_sig(pk, mn))\n            print(f\"{pk:<22} | {sigs[0]:>5} | {sigs[1]:>5} | {sigs[2]:>6} | {sigs[3]:>5} | {sigs[4]:>5} | {sigs[5]:>5} | {votes_5}/5\")\n    \n    # Detailed p-values\n    print()\n    print(\"P-VALUES (raw / FDR):\")\n    print(f\"{'Pair':<22} | {'Naive p':>8} | {'Diff p_fdr':>10} | {'PG_f p_fdr':>10} | {'PG_r p_fdr':>10} | {'TY p_fdr':>8}\")\n    print(\"-\" * 80)\n    for cn in CANARY:\n        for dn in DOWNSTREAM:\n            pk = f\"{cn}->{dn}\"\n            naive_p = pair_results[pk][\"naive_xcorr\"].get(\"p_value\", None)\n            diff_p = pair_results[pk][\"diff_xcorr\"].get(\"p_fdr\", None)\n            pgf_p = pair_results[pk][\"permg_fwd\"].get(\"p_fdr\", None)\n            pgr_p = pair_results[pk][\"permg_rev\"].get(\"p_fdr\", None)\n            ty_p = pair_results[pk][\"ty_granger\"].get(\"p_fdr\", None)\n            \n            def fmt(v):\n                return f\"{v:.4f}\" if v is not None else \"N/A\"\n            \n            print(f\"{pk:<22} | {fmt(naive_p):>8} | {fmt(diff_p):>10} | {fmt(pgf_p):>10} | {fmt(pgr_p):>10} | {fmt(ty_p):>8}\")\n    \n    # Save JSON\n    out_dir = os.path.join(DATA_DIR, \"analysis\")\n    os.makedirs(out_dir, exist_ok=True)\n    \n    output = {\n        \"experiment\": \"opt1b_wiki_a100_s42\",\n        \"model\": \"facebook/opt-1.3b\",\n        \"dataset\": \"wikitext-103\",\n        \"alpha\": 1.0,\n        \"seed\": 42,\n        \"n_generations\": T,\n        \"timestamp\": datetime.now().isoformat(),\n        \"parameters\": {\n            \"max_lag\": MAX_LAG,\n            \"n_perm\": N_PERM,\n            \"seed\": SEED,\n            \"fdr_method\": \"fdr_bh\",\n            \"fdr_q\": ALPHA,\n        },\n        \"trajectory\": trajectory,\n        \"pair_results\": pair_results,\n        \"summary\": {\n            \"method_sig_counts\": {k: len(v) for k, v in method_sig_counts.items()},\n            \"method_sig_pairs\": {k: v for k, v in method_sig_counts.items()},\n            \"consensus_3of5\": consensus_3,\n            \"consensus_4of5\": consensus_4,\n        },\n    }\n    \n    class NumpyEncoder(json.JSONEncoder):\n        def default(self, obj):\n            if isinstance(obj, (np.integer,)):\n                return int(obj)\n            if isinstance(obj, (np.floating,)):\n                return float(obj)\n            if isinstance(obj, np.ndarray):\n                return obj.tolist()\n            if isinstance(obj, (np.bool_,)):\n                return bool(obj)\n            return super().default(obj)\n    \n    out_path = os.path.join(out_dir, \"opt1b_6method_full.json\")\n    with open(out_path, \"w\") as f:\n        json.dump(output, f, indent=2, cls=NumpyEncoder)\n    print(f\"\\nSaved: {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-17T12:50:47.852206+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_opt1b_full_8pair_20260517T124735",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-17T12:50:47.852471+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "cd /root/autodl-tmp/distrib_canary_collapse && python analyze_opt1b_full.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_opt1b_full_8pair_20260517T124735",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "cd /root/autodl-tmp/distrib_canary_collapse && python analyze_opt1b_full.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-17T12:50:47.852691+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cd /root/autodl-tmp/distrib_canary_collapse && python analyze_opt1b_full.py'\\n\\nExit code: 127\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 1: python: command not found\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_opt1b_full_8pair_20260517T124735",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-17T12:50:47.852936+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "cd /root/autodl-tmp/distrib_canary_collapse && python3 analyze_opt1b_full.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_opt1b_full_8pair_20260517T124735",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "cd /root/autodl-tmp/distrib_canary_collapse && python3 analyze_opt1b_full.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-17T12:50:47.853141+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cd /root/autodl-tmp/distrib_canary_collapse && python3 analyze_opt1b_full.py'\\n\\nExit code: 1\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nTraceback (most recent call last):\\n  File \\\"/root/autodl-tmp/distrib_canary_collapse/analyze_opt1b_full.py\\\", line 14, in &lt;module>\\n    import numpy as np\\nModuleNotFoundError: No module named 'numpy'\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.93}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_opt1b_full_8pair_20260517T124735",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-17T12:50:47.853390+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "find /root -name \"python*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_opt1b_full_8pair_20260517T124735",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "find /root -name \"python*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-17T12:50:47.853741+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/miniconda3/bin/python3.12\\n/root/miniconda3/bin/python3.12-config\\n/root/miniconda3/conda-meta/python-3.12.3-h996f2a0_1.json\\n/root/miniconda3/include/python3.12/cpython/pythonrun.h\\n/root/miniconda3/include/python3.12/pythonrun.h\\n/root/miniconda3/lib/pkgconfig/python-3.12-embed.pc\\n/root/miniconda3/lib/pkgconfig/python-3.12.pc\\n/root/miniconda3/lib/python3.12/config-3.12-x86_64-linux-gnu/__pycache__/python-config.cpython-312.pyc\\n/root/miniconda3/lib/python3.12/config-3.12-x86_64-linux-gnu/python-config.py\\n/root/miniconda3/lib/python3.12/config-3.12-x86_64-linux-gnu/python.o\\n/root/miniconda3/lib/python3.12/idlelib/Icons/python.gif\\n/root/miniconda3/lib/python3.12/site-packages/conda/cli/__pycache__/python_api.cpython-312.pyc\\n/root/miniconda3/lib/python3.12/site-packages/conda/cli/python_api.py\\n/root/miniconda3/lib/python3.12/site-packages/conda/common/pkg_formats/__pycache__/python.cpython-312.pyc\\n/root/miniconda3/lib/python3.12/site-packages/conda/common/pkg_formats/python.py\\n/root/miniconda3/lib/python3.12/site-packages/pip/_vendor/pygments/lexers/__pycache__/python.cpython-312.pyc\\n/root/miniconda3/lib/python3.12/site-packages/pip/_vendor/pygments/lexers/python.py\\n/root/miniconda3/lib/python3.12/site-packages/pyarrow/include/arrow/python/python_test.h\\n/root/miniconda3/lib/python3.12/site-packages/pyarrow/include/arrow/python/python_to_arrow.h\\n/root/miniconda3/lib/python3.12/site-packages/pyarrow/include/arrow/python/vendored/pythoncapi_compat.h\\n/root/miniconda3/lib/python3.12/site-packages/pyarrow/src/arrow/python/python_test.cc\\n/root/miniconda3/lib/python3.12/site-packages/pyarrow/src/arrow/python/python_test.h\\n/root/miniconda3/lib/python3.12/site-packages/pyarrow/src/arrow/python/python_to_arrow.cc\\n/root/miniconda3/lib/python3.12/site-packages/pyarrow/src/arrow/python/python_to_arrow.h\\n/root/miniconda3/lib/python3.12/site-packages/pyarrow/src/arrow/python/vendo
…[truncated 6379 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_opt1b_full_8pair_20260517T124735",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-17T12:50:47.853958+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "cd /root/autodl-tmp/distrib_canary_collapse && /root/miniconda3/bin/python3.12 analyze_opt1b_full.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_opt1b_full_8pair_20260517T124735",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "cd /root/autodl-tmp/distrib_canary_collapse && /root/miniconda3/bin/python3.12 analyze_opt1b_full.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-17T12:50:47.854133+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"OPT-1.3B WikiText a=1.0 s42 | T=11 generations\\n\\n======================================================================\\nCOLLAPSE TRAJECTORY\\n----------------------------------------------------------------------\\n  metric                   gen0        gen10     drift%\\n  --------------------------------------------------\\n  token_entropy        3.048329     1.158671     -62.0%\\n  ece                  0.019933     0.422201   +2018.1%\\n  perplexity          24.876836   647.419815   +2502.5%\\n  distinct_1           0.104029     0.071164     -31.6%\\n  distinct_2           0.526711     0.324831     -38.3%\\n  distinct_3           0.816691     0.522071     -36.1%\\n  mauve                0.031181     0.029360      -5.8%\\n\\n======================================================================\\n6-METHOD ANALYSIS (8 canonical pairs)\\n----------------------------------------------------------------------\\n\\nTABLE 5 ROW (OPT-1.3B):\\nMethod                 | Sig | Sig Pairs\\n----------------------------------------------------------------------\\nnaive_xcorr            | 6/8 | token_entropy->distinct_1, token_entropy->distinct_2, token_entropy->distinct_3, ece->distinct_1, ece->distinct_2, ece->distinct_3\\ndiff_xcorr             | 6/8 | token_entropy->distinct_1, token_entropy->distinct_2, token_entropy->distinct_3, ece->distinct_1, ece->distinct_2, ece->distinct_3\\nthreshold_onset        | 0/8 | (none)\\npermg_fwd              | 6/8 | token_entropy->distinct_1, token_entropy->distinct_2, token_entropy->distinct_3, ece->distinct_1, ece->distinct_2, ece->distinct_3\\npermg_rev              | 0/8 | (none)\\nty_granger             | 2/8 | token_entropy->distinct_1, ece->distinct_1\\nConsensus >=3/5        | 6/8 | token_entropy->distinct_1, token_entropy->distinct_2, token_entropy->distinct_3, ece->distinct_1, ece->distinct_2, ece->distinct_3\\nConsensus >=4/5        | 2/8 | token_entropy->distinct_1, e
…[truncated 1975 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_opt1b_full_8pair_20260517T124735",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-17T12:50:47.854387+00:00_

分析完成。结果已保存到 `results/generalize/opt1b_wiki_a100_s42/analysis/opt1b_6method_full.json`。

---

## OPT-1.3B WikiText α=1.0 — 8 Canonical Pairs

### Collapse trajectory:
| metric | gen0 | gen10 | drift% |
|--------|------|-------|--------|
| token_entropy | 3.048329 | 1.158671 | -62.0% |
| ece | 0.019933 | 0.422201 | +2018.1% |
| perplexity | 24.876836 | 647.419815 | +2502.5% |
| distinct_1 | 0.104029 | 0.071164 | -31.6% |
| distinct_2 | 0.526711 | 0.324831 | -38.3% |
| distinct_3 | 0.816691 | 0.522071 | -36.1% |
| mauve | 0.031181 | 0.029360 | -5.8% |

### Table 5 Row:
| Method | Sig Count | Sig Pairs |
|--------|-----------|-----------|
| Naive XCorr | 6/8 | entropy→d1, entropy→d2, entropy→d3, ece→d1, ece→d2, ece→d3 |
| Diff XCorr (FDR) | 6/8 | same 6 |
| Threshold Onset | 0/8 | (none) |
| PermG forward (FDR) | 6/8 | same 6 |
| PermG reverse (FDR) | 0/8 | (none) |
| TY Granger | 2/8 | entropy→d1, ece→d1 |
| Consensus ≥3/5 | 6/8 | all 6 distinct pairs |
| Consensus ≥4/5 | 2/8 | entropy→d1, ece→d1 |

### Per-pair detail:
| Pair | Naive | Diff | Thresh | PG_fwd | PG_rev | TY | votes |
|------|-------|------|--------|--------|--------|-----|-------|
| entropy→d1 | Y | Y | N | Y | N | Y | 4/5 |
| entropy→d2 | Y | Y | N | Y | N | N | 3/5 |
| entropy→d3 | Y | Y | N | Y | N | N | 3/5 |
| entropy→mauve | N | N | N | N | N | N | 0/5 |
| ece→d1 | Y | Y | N | Y | N | Y | 4/5 |
| ece→d2 | Y | Y | N | Y | N | N | 3/5 |
| ece→d3 | Y | Y | N | Y | N | N | 3/5 |
| ece→mauve | N | N | N | N | N | N | 0/5 |

### Key observations:
- **Strong directionality**: PermG forward 6/8 sig vs PermG reverse 0/8 — confirms canary→downstream direction, not reverse
- **mauve is non-responsive**: 0/8 across all methods (drift only -5.8%, essentially flat)
- **Threshold Onset = 0/8**: likely because both canary and downstream degrade from gen0→gen1 simultaneously (no detectable lead)
- **TY underpowered** as expected at T=11 (only 2/8 sig, but those 2 are the strongest pairs d1)
- **6/8 consensus ≥3/5**: all distinct_N pairs pass, mauve pairs fail universally

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_opt1b_full_8pair_20260517T124735"
}
```

</details>

---
