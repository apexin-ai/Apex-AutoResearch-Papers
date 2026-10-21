# analysis docred bcs r2

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 0
- **Tool calls:** 15
- **Original source:** `logs/chats/worker_analysis_docred_bcs_r2_20260519T140257.jsonl`
- **Structured JSON:** [`9111b72f6d5622d99f03.json`](../../sessions/91/9111b72f6d5622d99f03.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

31 recorded events

### Tool call

_source line 1 · 2026-05-19T14:06:25.864614+00:00_

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
  "session": "worker_analysis_docred_bcs_r2_20260519T140257",
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

_source line 2 · 2026-05-19T14:06:25.864972+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_docred_bcs_r2_20260519T140257",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T14:06:25.865161+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "ls -la /root/schema-dag-extraction/artifacts/exp_docred_bcs_expanded/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_docred_bcs_r2_20260519T140257",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "ls -la /root/schema-dag-extraction/artifacts/exp_docred_bcs_expanded/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T14:06:25.865313+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 732\\ndrwxr-xr-x  3 root root   4096 May 19 20:53 .\\ndrwxr-xr-x 61 root root   4096 May 19 19:51 ..\\ndrwxr-xr-x  2 root root     42 May 19 20:52 all_predictions\\n-rw-r--r--  1 root root   7892 May 19 20:52 bcs_controlled_results.json\\n-rw-r--r--  1 root root   2620 May 19 20:53 bootstrap_analysis.json\\n-rw-r--r--  1 root root  29977 May 19 20:52 eval_results.json\\n-rw-r--r--  1 root root   1755 May 19 20:53 factorial_analysis.json\\n-rw-r--r--  1 root root 686236 May 19 22:02 preprocess_config.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.23}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_docred_bcs_r2_20260519T140257",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T14:06:25.865446+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "head -200 /root/schema-dag-extraction/artifacts/exp_docred_bcs_expanded/bcs_controlled_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_docred_bcs_r2_20260519T140257",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "head -200 /root/schema-dag-extraction/artifacts/exp_docred_bcs_expanded/bcs_controlled_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T14:06:25.865642+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"bcs_count_16_high_bcs\\\": {\\n    \\\"batches\\\": [\\n      0.5064935064935064,\\n      0.4025974025974026,\\n      0.37662337662337664,\\n      0.4675324675324675,\\n      0.4805194805194805,\\n      0.4675324675324675,\\n      0.36363636363636365,\\n      0.2987012987012987,\\n      0.4805194805194805,\\n      0.4805194805194805,\\n      0.4155844155844156,\\n      0.4805194805194805,\\n      0.38961038961038963,\\n      0.33766233766233766,\\n      0.37662337662337664\\n    ],\\n    \\\"mean_acc\\\": 0.42164502164502166,\\n    \\\"std_acc\\\": 0.061258088143060524,\\n    \\\"bcs_values\\\": [\\n      0.6771903283894062,\\n      0.7205597172180812,\\n      0.7506259034077326,\\n      0.7453926106293997,\\n      0.7570966427524884,\\n      0.6901882817347844,\\n      0.6510756264130274,\\n      0.7203258109589418,\\n      0.7570966427524884,\\n      0.7570966427524884,\\n      0.7312004278103511,\\n      0.7570966427524884,\\n      0.751556758582592,\\n      0.7202082688609759,\\n      0.6510756264130274\\n    ],\\n    \\\"mean_bcs\\\": 0.7225190620952181,\\n    \\\"n_samples\\\": [\\n      77,\\n      77,\\n      77,\\n      77,\\n      77,\\n      77,\\n      77,\\n      77,\\n      77,\\n      77,\\n      77,\\n      77,\\n      77,\\n      77,\\n      77\\n    ]\\n  },\\n  \\\"bcs_count_16_low_bcs\\\": {\\n    \\\"batches\\\": [\\n      0.7105263157894737,\\n      0.6447368421052632,\\n      0.6710526315789473,\\n      0.7123287671232876,\\n      0.6578947368421053,\\n      0.6842105263157895,\\n      0.6842105263157895,\\n      0.6710526315789473,\\n      0.6973684210526315,\\n      0.6578947368421053,\\n      0.6710526315789473,\\n      0.6578947368421053,\\n      0.6447368421052632,\\n      0.6578947368421053,\\n      0.6578947368421053\\n    ],\\n    \\\"mean_acc\\\": 0.6720499879836581,\\n    \\\"std_acc\\\": 0.02087493552543715,\\n    \\\"bcs_values\\\": [\\n      0.380259021371603,\\n   
…[truncated 2616 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_docred_bcs_r2_20260519T140257",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T14:06:25.865812+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "head -200 /root/schema-dag-extraction/artifacts/exp_docred_bcs_expanded/eval_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_docred_bcs_r2_20260519T140257",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "head -200 /root/schema-dag-extraction/artifacts/exp_docred_bcs_expanded/eval_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T14:06:25.866264+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"bcs_count_16_high_bcs_0\\\": {\\n    \\\"accuracy\\\": 0.5064935064935064,\\n    \\\"correct\\\": 39,\\n    \\\"total\\\": 77,\\n    \\\"bcs\\\": 0.6771903283894062,\\n    \\\"bcs_max\\\": 0.9001671075820923,\\n    \\\"config_key\\\": \\\"bcs_count_16\\\",\\n    \\\"strategy\\\": \\\"high_bcs\\\",\\n    \\\"batch_idx\\\": 0,\\n    \\\"num_types\\\": 16\\n  },\\n  \\\"bcs_count_16_high_bcs_1\\\": {\\n    \\\"accuracy\\\": 0.4025974025974026,\\n    \\\"correct\\\": 31,\\n    \\\"total\\\": 77,\\n    \\\"bcs\\\": 0.7205597172180812,\\n    \\\"bcs_max\\\": 0.9001671075820923,\\n    \\\"config_key\\\": \\\"bcs_count_16\\\",\\n    \\\"strategy\\\": \\\"high_bcs\\\",\\n    \\\"batch_idx\\\": 1,\\n    \\\"num_types\\\": 16\\n  },\\n  \\\"bcs_count_16_high_bcs_2\\\": {\\n    \\\"accuracy\\\": 0.37662337662337664,\\n    \\\"correct\\\": 29,\\n    \\\"total\\\": 77,\\n    \\\"bcs\\\": 0.7506259034077326,\\n    \\\"bcs_max\\\": 0.9001671075820923,\\n    \\\"config_key\\\": \\\"bcs_count_16\\\",\\n    \\\"strategy\\\": \\\"high_bcs\\\",\\n    \\\"batch_idx\\\": 2,\\n    \\\"num_types\\\": 16\\n  },\\n  \\\"bcs_count_16_high_bcs_3\\\": {\\n    \\\"accuracy\\\": 0.4675324675324675,\\n    \\\"correct\\\": 36,\\n    \\\"total\\\": 77,\\n    \\\"bcs\\\": 0.7453926106293997,\\n    \\\"bcs_max\\\": 0.9001671075820923,\\n    \\\"config_key\\\": \\\"bcs_count_16\\\",\\n    \\\"strategy\\\": \\\"high_bcs\\\",\\n    \\\"batch_idx\\\": 3,\\n    \\\"num_types\\\": 16\\n  },\\n  \\\"bcs_count_16_high_bcs_4\\\": {\\n    \\\"accuracy\\\": 0.4805194805194805,\\n    \\\"correct\\\": 37,\\n    \\\"total\\\": 77,\\n    \\\"bcs\\\": 0.7570966427524884,\\n    \\\"bcs_max\\\": 0.9001671075820923,\\n    \\\"config_key\\\": \\\"bcs_count_16\\\",\\n    \\\"strategy\\\": \\\"high_bcs\\\",\\n    \\\"batch_idx\\\": 4,\\n    \\\"num_types\\\": 16\\n  },\\n  \\\"bcs_count_16_low_bcs_0\\\": {\\n    \\\"accuracy\\\": 0.7105263157894737,\\n    \\\
…[truncated 4743 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_docred_bcs_r2_20260519T140257",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T14:06:25.866453+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "head -100 /root/schema-dag-extraction/artifacts/exp_docred_bcs_expanded/bootstrap_analysis.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_docred_bcs_r2_20260519T140257",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "head -100 /root/schema-dag-extraction/artifacts/exp_docred_bcs_expanded/bootstrap_analysis.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T14:06:25.866657+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"count_16\\\": {\\n    \\\"n_batches\\\": 55,\\n    \\\"bcs_range\\\": [\\n      0.37963757539788884,\\n      0.7570966427524884\\n    ],\\n    \\\"acc_range\\\": [\\n      0.2987012987012987,\\n      0.75\\n    ],\\n    \\\"spearman_r\\\": -0.762254771270759,\\n    \\\"spearman_p\\\": 1.3737636015552895e-11,\\n    \\\"regression\\\": {\\n      \\\"slope\\\": -0.7316661051875889,\\n      \\\"intercept\\\": 0.977487374598605,\\n      \\\"r_squared\\\": 0.6528292306186455,\\n      \\\"p_value\\\": 8.925682180933223e-14,\\n      \\\"slope_95ci\\\": [\\n        -0.8606367461041239,\\n        -0.6193657152412085\\n      ]\\n    },\\n    \\\"quartile_analysis\\\": {\\n      \\\"q25_threshold\\\": 0.38950070415933924,\\n      \\\"q75_threshold\\\": 0.6510756264130274,\\n      \\\"low_bcs_quartile_mean_acc\\\": 0.6721212277268513,\\n      \\\"high_bcs_quartile_mean_acc\\\": 0.42164502164502166,\\n      \\\"gap\\\": 0.2504762060818297,\\n      \\\"gap_95ci\\\": [\\n        0.1751301488879079,\\n        0.2818345233260276\\n      ],\\n      \\\"n_low\\\": 14,\\n      \\\"n_high\\\": 15\\n    },\\n    \\\"strategy_breakdown\\\": {\\n      \\\"high_bcs\\\": {\\n        \\\"mean\\\": 0.42164502164502166,\\n        \\\"std\\\": 0.061258088143060524,\\n        \\\"n\\\": 15\\n      },\\n      \\\"low_bcs\\\": {\\n        \\\"mean\\\": 0.6720499879836581,\\n        \\\"std\\\": 0.02087493552543715,\\n        \\\"n\\\": 15\\n      },\\n      \\\"random\\\": {\\n        \\\"mean\\\": 0.6103171929689594,\\n        \\\"std\\\": 0.07686467783092508,\\n        \\\"n\\\": 25\\n      }\\n    }\\n  },\\n  \\\"count_32\\\": {\\n    \\\"n_batches\\\": 55,\\n    \\\"bcs_range\\\": [\\n      0.4324798233086063,\\n      0.694971195512241\\n    ],\\n    \\\"acc_range\\\": [\\n      0.37579617834394907,\\n      0.6470588235294118\\n    ],\\n    \\\"spearman_r\\\": -0.6929482388738422,\\n    \\\"spearman_p\\\": 4.56079014158981e-09,\\
…[truncated 1239 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_docred_bcs_r2_20260519T140257",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T14:06:25.866867+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "cat /root/schema-dag-extraction/artifacts/exp_docred_bcs_expanded/bootstrap_analysis.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_docred_bcs_r2_20260519T140257",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "cat /root/schema-dag-extraction/artifacts/exp_docred_bcs_expanded/bootstrap_analysis.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T14:06:25.867066+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"count_16\\\": {\\n    \\\"n_batches\\\": 55,\\n    \\\"bcs_range\\\": [\\n      0.37963757539788884,\\n      0.7570966427524884\\n    ],\\n    \\\"acc_range\\\": [\\n      0.2987012987012987,\\n      0.75\\n    ],\\n    \\\"spearman_r\\\": -0.762254771270759,\\n    \\\"spearman_p\\\": 1.3737636015552895e-11,\\n    \\\"regression\\\": {\\n      \\\"slope\\\": -0.7316661051875889,\\n      \\\"intercept\\\": 0.977487374598605,\\n      \\\"r_squared\\\": 0.6528292306186455,\\n      \\\"p_value\\\": 8.925682180933223e-14,\\n      \\\"slope_95ci\\\": [\\n        -0.8606367461041239,\\n        -0.6193657152412085\\n      ]\\n    },\\n    \\\"quartile_analysis\\\": {\\n      \\\"q25_threshold\\\": 0.38950070415933924,\\n      \\\"q75_threshold\\\": 0.6510756264130274,\\n      \\\"low_bcs_quartile_mean_acc\\\": 0.6721212277268513,\\n      \\\"high_bcs_quartile_mean_acc\\\": 0.42164502164502166,\\n      \\\"gap\\\": 0.2504762060818297,\\n      \\\"gap_95ci\\\": [\\n        0.1751301488879079,\\n        0.2818345233260276\\n      ],\\n      \\\"n_low\\\": 14,\\n      \\\"n_high\\\": 15\\n    },\\n    \\\"strategy_breakdown\\\": {\\n      \\\"high_bcs\\\": {\\n        \\\"mean\\\": 0.42164502164502166,\\n        \\\"std\\\": 0.061258088143060524,\\n        \\\"n\\\": 15\\n      },\\n      \\\"low_bcs\\\": {\\n        \\\"mean\\\": 0.6720499879836581,\\n        \\\"std\\\": 0.02087493552543715,\\n        \\\"n\\\": 15\\n      },\\n      \\\"random\\\": {\\n        \\\"mean\\\": 0.6103171929689594,\\n        \\\"std\\\": 0.07686467783092508,\\n        \\\"n\\\": 25\\n      }\\n    }\\n  },\\n  \\\"count_32\\\": {\\n    \\\"n_batches\\\": 55,\\n    \\\"bcs_range\\\": [\\n      0.4324798233086063,\\n      0.694971195512241\\n    ],\\n    \\\"acc_range\\\": [\\n      0.37579617834394907,\\n      0.6470588235294118\\n    ],\\n    \\\"spearman_r\\\": -0.6929482388738422,\\n    \\\"spearman_p\\\": 4.56079014158981e-09,\\
…[truncated 1402 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_docred_bcs_r2_20260519T140257",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T14:06:25.867295+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-38874",
  "command": "cat > /tmp/r2_analysis.py << 'PYEOF'\nimport json\nimport numpy as np\nfrom scipy import stats\nfrom sklearn.linear_model import LinearRegression\n\nnp.random.seed(42)\n\nwith open('/root/schema-dag-extraction/artifacts/exp_docred_bcs_expanded/bcs_controlled_results.json') as f:\n    data = json.load(f)\n\nresults = {}\n\nfor count_level in ['count_16', 'count_32']:\n    bcs_all = []\n    acc_all = []\n    for strategy in ['high_bcs', 'low_bcs', 'random']:\n        key = f'bcs_{count_level}_{strategy}'\n        bcs_all.extend(data[key]['bcs_values'])\n        acc_all.extend(data[key]['batches'])\n    \n    bcs_arr = np.array(bcs_all)\n    acc_arr = np.array(acc_all)\n    n = len(bcs_arr)\n    \n    X = bcs_arr.reshape(-1, 1)\n    y = acc_arr\n    model = LinearRegression().fit(X, y)\n    r2 = model.score(X, y)\n    slope = model.coef_[0]\n    intercept = model.intercept_\n    \n    pearson_r, pearson_p = stats.pearsonr(bcs_arr, acc_arr)\n    spearman_rho, spearman_p = stats.spearmanr(bcs_arr, acc_arr)\n    \n    # Bootstrap 95% CI for R²\n    n_boot = 10000\n    r2_boots = []\n    for _ in range(n_boot):\n        idx = np.random.choice(n, n, replace=True)\n        try:\n            r2_boot = LinearRegression().fit(X[idx], y[idx]).score(X[idx], y[idx])\n            r2_boots.append(r2_boot)\n        except:\n            pass\n    ci_lower, ci_upper = np.percentile(r2_boots, [2.5, 97.5])\n    \n    results[count_level] = {\n        'r2': round(r2, 4),\n        'r2_ci': [round(ci_lower, 4), round(ci_upper, 4)],\n        'pearson_r': round(pearson_r, 4),\n        'pearson_p': float(f'{pearson_p:.2e}'),\n        'spearman_rho': round(spearman_rho, 4),\n        'spearman_p': float(f'{spearman_p:.2e}'),\n        'n': n,\n        'slope': round(slope, 4),\n        'intercept': round(intercept, 4)\n    }\n\n# Pooled (count_16 + count_32)\nbcs_pooled = []\nacc_pooled = []\ncount_labels = []\nfor count_level in ['count_16', 'count_32']:\n    for strategy in ['high_bcs', 'low_bcs', 'random']:\n        key = f'bcs_{count_level}_{strategy}'\n        bcs_pooled.extend(data[key]['bcs_values'])\n        acc_pooled.extend(data[key]['batches'])\n        count_labels.extend([count_level] * len(data[key]['bcs_values']))\n\nbcs_pooled = np.array(bcs_pooled)\nacc_pooled = np.array(acc_pooled)\nn_pooled = len(bcs_pooled)\n\nX_pooled = bcs_pooled.reshape(-1, 1)\nmodel_pooled = LinearRegression().fit(X_pooled, acc_pooled)\nr2_pooled = model_pooled.score(X_pooled, acc_pooled)\n\n# Pooled bootstrap\nr2_boots_pooled = []\nfor _ in range(n_boot):\n    idx = np.random.choice(n_pooled, n_pooled, replace=True)\n    try:\n        r2_b = LinearRegression().fit(X_pooled[idx], acc_pooled[idx]).score(X_pooled[idx], acc_pooled[idx])\n        r2_boots_pooled.append(r2_b)\n    except:\n        pass\nci_pooled = np.percentile(r2_boots_pooled, [2.5, 97.5])\n\n# Also compute pooled with count_level as covariate (partial R² of BCS)\ncount_dummy = np.array([1 if c == 'count_32' else 0 for c in count_labels]).reshape(-1, 1)\nX_with_count = np.hstack([bcs_pooled.reshape(-1, 1), count_dummy])\nmodel_full = LinearRegression().fit(X_with_count, acc_pooled)\nr2_full = model_full.score(X_with_count, acc_pooled)\n\nmodel_count_only = LinearRegression().fit(count_dummy, acc_pooled)\nr2_count_only = model_count_only.score(count_dummy, acc_pooled)\n\n# Semi-partial R² of BCS controlling for count\nsemi_partial_r2_bcs = r2_full - r2_count_only\n\nresults['pooled'] = {\n    'r2': round(r2_pooled, 4),\n    'r2_ci': [round(ci_pooled[0], 4), round(ci_pooled[1], 4)],\n    'n': n_pooled,\n    'slope': round(model_pooled.coef_[0], 4),\n    'intercept': round(model_pooled.intercept_, 4),\n    'pearson_r': round(float(stats.pearsonr(bcs_pooled, acc_pooled)[0]), 4),\n    'spearman_rho': round(float(stats.spearmanr(bcs_pooled, acc_pooled)[0]), 4),\n    'r2_controlling_count': round(semi_partial_r2_bcs, 4),\n    'r2_full_model': round(r2_full, 4),\n}\n\nresults['comparison'] = {\n    'original_r2': 0.525,\n    'original_n': 35,\n    'original_ci': [0.27, 0.73],\n    'note': 'Original was count_16 only with 35 batches (10 low + 10 high + 15 random). Expanded has 55 batches (15+15+25).'\n}\n\n# Save\nout_path = '/root/schema-dag-extraction/artifacts/exp_docred_bcs_expanded/r2_analysis.json'\nwith open(out_path, 'w') as f:\n    json.dump(results, f, indent=2)\n\n# Print summary\nprint(\"=\" * 70)\nprint(\"R² ANALYSIS: BCS → Accuracy (OLS Regression)\")\nprint(\"=\" * 70)\n\nfor cl in ['count_16', 'count_32']:\n    r = results[cl]\n    print(f\"\\n--- {cl} (n={r['n']}) ---\")\n    print(f\"  R²           = {r['r2']:.4f}  95% CI [{r['r2_ci'][0]:.4f}, {r['r2_ci'][1]:.4f}]\")\n    print(f\"  Pearson r    = {r['pearson_r']:.4f}  (p={r['pearson_p']:.2e})\")\n    print(f\"  Spearman ρ   = {r['spearman_rho']:.4f}  (p={r['spearman_p']:.2e})\")\n    print(f\"  Slope        = {r['slope']:.4f}\")\n    print(f\"  Intercept    = {r['intercept']:.4f}\")\n\np = results['pooled']\nprint(f\"\\n--- Pooled (n={p['n']}) ---\")\nprint(f\"  R² (BCS only)            = {p['r2']:.4f}  95% CI [{p['r2_ci'][0]:.4f}, {p['r2_ci'][1]:.4f}]\")\nprint(f\"  R² (BCS + count control) = {p['r2_full_model']:.4f}\")\nprint(f\"  Semi-partial R² of BCS   = {p['r2_controlling_count']:.4f}\")\nprint(f\"  Pearson r                = {p['pearson_r']:.4f}\")\nprint(f\"  Spearman ρ               = {p['spearman_rho']:.4f}\")\n\nprint(f\"\\n--- Comparison with original ---\")\nprint(f\"  Original count_16: R² = 0.525, n=35, 95% CI [0.27, 0.73]\")\nprint(f\"  Expanded count_16: R² = {results['count_16']['r2']:.4f}, n=55, 95% CI [{results['count_16']['r2_ci'][0]:.4f}, {results['count_16']['r2_ci'][1]:.4f}]\")\nprint(f\"  Expanded count_32: R² = {results['count_32']['r2']:.4f}, n=55, 95% CI [{results['count_32']['r2_ci'][0]:.4f}, {results['count_32']['r2_ci'][1]:.4f}]\")\n\n# Range for paper\nr2_min = min(results['count_16']['r2'], results['count_32']['r2'])\nr2_max = max(results['count_16']['r2'], results['count_32']['r2'])\nprint(f\"\\n>>> Paper citation: R² = {r2_min:.2f}–{r2_max:.2f} (n=55 per count level)\")\nprint(f\">>> As percentage: {r2_min*100:.0f}–{r2_max*100:.0f}%\")\n\nprint(f\"\\nSaved to: {out_path}\")\nPYEOF\n/root/miniconda3/bin/python3 /tmp/r2_analysis.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_docred_bcs_r2_20260519T140257",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "cat > /tmp/r2_analysis.py << 'PYEOF'\nimport json\nimport numpy as np\nfrom scipy import stats\nfrom sklearn.linear_model import LinearRegression\n\nnp.random.seed(42)\n\nwith open('/root/schema-dag-extraction/artifacts/exp_docred_bcs_expanded/bcs_controlled_results.json') as f:\n    data = json.load(f)\n\nresults = {}\n\nfor count_level in ['count_16', 'count_32']:\n    bcs_all = []\n    acc_all = []\n    for strategy in ['high_bcs', 'low_bcs', 'random']:\n        key = f'bcs_{count_level}_{strategy}'\n        bcs_all.extend(data[key]['bcs_values'])\n        acc_all.extend(data[key]['batches'])\n    \n    bcs_arr = np.array(bcs_all)\n    acc_arr = np.array(acc_all)\n    n = len(bcs_arr)\n    \n    X = bcs_arr.reshape(-1, 1)\n    y = acc_arr\n    model = LinearRegression().fit(X, y)\n    r2 = model.score(X, y)\n    slope = model.coef_[0]\n    intercept = model.intercept_\n    \n    pearson_r, pearson_p = stats.pearsonr(bcs_arr, acc_arr)\n    spearman_rho, spearman_p = stats.spearmanr(bcs_arr, acc_arr)\n    \n    # Bootstrap 95% CI for R²\n    n_boot = 10000\n    r2_boots = []\n    for _ in range(n_boot):\n        idx = np.random.choice(n, n, replace=True)\n        try:\n            r2_boot = LinearRegression().fit(X[idx], y[idx]).score(X[idx], y[idx])\n            r2_boots.append(r2_boot)\n        except:\n            pass\n    ci_lower, ci_upper = np.percentile(r2_boots, [2.5, 97.5])\n    \n    results[count_level] = {\n        'r2': round(r2, 4),\n        'r2_ci': [round(ci_lower, 4), round(ci_upper, 4)],\n        'pearson_r': round(pearson_r, 4),\n        'pearson_p': float(f'{pearson_p:.2e}'),\n        'spearman_rho': round(spearman_rho, 4),\n        'spearman_p': float(f'{spearman_p:.2e}'),\n        'n': n,\n        'slope': round(slope, 4),\n        'intercept': round(intercept, 4)\n    }\n\n# Pooled (count_16 + count_32)\nbcs_pooled = []\nacc_pooled = []\ncount_labels = []\nfor count_level in ['count_16', 'count_32']:\n    for strategy in ['high_bcs', 'low_bcs', 'random']:\n        key = f'bcs_{count_level}_{strategy}'\n        bcs_pooled.extend(data[key]['bcs_values'])\n        acc_pooled.extend(data[key]['batches'])\n        count_labels.extend([count_level] * len(data[key]['bcs_values']))\n\nbcs_pooled = np.array(bcs_pooled)\nacc_pooled = np.array(acc_pooled)\nn_pooled = len(bcs_pooled)\n\nX_pooled = bcs_pooled.reshape(-1, 1)\nmodel_pooled = LinearRegression().fit(X_pooled, acc_pooled)\nr2_pooled = model_pooled.score(X_pooled, acc_pooled)\n\n# Pooled bootstrap\nr2_boots_pooled = []\nfor _ in range(n_boot):\n    idx = np.random.choice(n_pooled, n_pooled, replace=True)\n    try:\n        r2_b = LinearRegression().fit(X_pooled[idx], acc_pooled[idx]).score(X_pooled[idx], acc_pooled[idx])\n        r2_boots_pooled.append(r2_b)\n    except:\n        pass\nci_pooled = np.percentile(r2_boots_pooled, [2.5, 97.5])\n\n# Also compute pooled with count_level as covariate (partial R² of BCS)\ncount_dummy = np.array([1 if c == 'count_32' else 0 for c in count_labels]).reshape(-1, 1)\nX_with_count = np.hstack([bcs_pooled.reshape(-1, 1), count_dummy])\nmodel_full = LinearRegression().fit(X_with_count, acc_pooled)\nr2_full = model_full.score(X_with_count, acc_pooled)\n\nmodel_count_only = LinearRegression().fit(count_dummy, acc_pooled)\nr2_count_only = model_count_only.score(count_dummy, acc_pooled)\n\n# Semi-partial R² of BCS controlling for count\nsemi_partial_r2_bcs = r2_full - r2_count_only\n\nresults['pooled'] = {\n    'r2': round(r2_pooled, 4),\n    'r2_ci': [round(ci_pooled[0], 4), round(ci_pooled[1], 4)],\n    'n': n_pooled,\n    'slope': round(model_pooled.coef_[0], 4),\n    'intercept': round(model_pooled.intercept_, 4),\n    'pearson_r': round(float(stats.pearsonr(bcs_pooled, acc_pooled)[0]), 4),\n    'spearman_rho': round(float(stats.spearmanr(bcs_pooled, acc_pooled)[0]), 4),\n    'r2_controlling_count': round(semi_partial_r2_bcs, 4),\n    'r2_full_model': round(r2_full, 4),\n}\n\nresults['comparison'] = {\n    'original_r2': 0.525,\n    'original_n': 35,\n    'original_ci': [0.27, 0.73],\n    'note': 'Original was count_16 only with 35 batches (10 low + 10 high + 15 random). Expanded has 55 batches (15+15+25).'\n}\n\n# Save\nout_path = '/root/schema-dag-extraction/artifacts/exp_docred_bcs_expanded/r2_analysis.json'\nwith open(out_path, 'w') as f:\n    json.dump(results, f, indent=2)\n\n# Print summary\nprint(\"=\" * 70)\nprint(\"R² ANALYSIS: BCS → Accuracy (OLS Regression)\")\nprint(\"=\" * 70)\n\nfor cl in ['count_16', 'count_32']:\n    r = results[cl]\n    print(f\"\\n--- {cl} (n={r['n']}) ---\")\n    print(f\"  R²           = {r['r2']:.4f}  95% CI [{r['r2_ci'][0]:.4f}, {r['r2_ci'][1]:.4f}]\")\n    print(f\"  Pearson r    = {r['pearson_r']:.4f}  (p={r['pearson_p']:.2e})\")\n    print(f\"  Spearman ρ   = {r['spearman_rho']:.4f}  (p={r['spearman_p']:.2e})\")\n    print(f\"  Slope        = {r['slope']:.4f}\")\n    print(f\"  Intercept    = {r['intercept']:.4f}\")\n\np = results['pooled']\nprint(f\"\\n--- Pooled (n={p['n']}) ---\")\nprint(f\"  R² (BCS only)            = {p['r2']:.4f}  95% CI [{p['r2_ci'][0]:.4f}, {p['r2_ci'][1]:.4f}]\")\nprint(f\"  R² (BCS + count control) = {p['r2_full_model']:.4f}\")\nprint(f\"  Semi-partial R² of BCS   = {p['r2_controlling_count']:.4f}\")\nprint(f\"  Pearson r                = {p['pearson_r']:.4f}\")\nprint(f\"  Spearman ρ               = {p['spearman_rho']:.4f}\")\n\nprint(f\"\\n--- Comparison with original ---\")\nprint(f\"  Original count_16: R² = 0.525, n=35, 95% CI [0.27, 0.73]\")\nprint(f\"  Expanded count_16: R² = {results['count_16']['r2']:.4f}, n=55, 95% CI [{results['count_16']['r2_ci'][0]:.4f}, {results['count_16']['r2_ci'][1]:.4f}]\")\nprint(f\"  Expanded count_32: R² = {results['count_32']['r2']:.4f}, n=55, 95% CI [{results['count_32']['r2_ci'][0]:.4f}, {results['count_32']['r2_ci'][1]:.4f}]\")\n\n# Range for paper\nr2_min = min(results['count_16']['r2'], results['count_32']['r2'])\nr2_max = max(results['count_16']['r2'], results['count_32']['r2'])\nprint(f\"\\n>>> Paper citation: R² = {r2_min:.2f}–{r2_max:.2f} (n=55 per count level)\")\nprint(f\">>> As percentage: {r2_min*100:.0f}–{r2_max*100:.0f}%\")\n\nprint(f\"\\nSaved to: {out_path}\")\nPYEOF\n/root/miniconda3/bin/python3 /tmp/r2_analysis.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T14:06:25.867651+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'cat > /tmp/r2_analysis.py << \\\\'PYEOF\\\\'\\\\nimport json\\\\nimport numpy as np\\\\nfrom scipy import stats\\\\nfrom sklearn.linear_model import LinearRegression\\\\n\\\\nnp.random.seed(42)\\\\n\\\\nwith open(\\\\'/root/schema-dag-extraction/artifacts/exp_docred_bcs_expanded/bcs_controlled_results.json\\\\') as f:\\\\n    data = json.load(f)\\\\n\\\\nresults = {}\\\\n\\\\nfor count_level in [\\\\'count_16\\\\', \\\\'count_32\\\\']:\\\\n    bcs_all = []\\\\n    acc_all = []\\\\n    for strategy in [\\\\'high_bcs\\\\', \\\\'low_bcs\\\\', \\\\'random\\\\']:\\\\n        key = f\\\\'bcs_{count_level}_{strategy}\\\\'\\\\n        bcs_all.extend(data[key][\\\\'bcs_values\\\\'])\\\\n        acc_all.extend(data[key][\\\\'batches\\\\'])\\\\n    \\\\n    bcs_arr = np.array(bcs_all)\\\\n    acc_arr = np.array(acc_all)\\\\n    n = len(bcs_arr)\\\\n    \\\\n    X = bcs_arr.reshape(-1, 1)\\\\n    y = acc_arr\\\\n    model = LinearRegression().fit(X, y)\\\\n    r2 = model.score(X, y)\\\\n    slope = model.coef_[0]\\\\n    intercept = model.intercept_\\\\n    \\\\n    pearson_r, pearson_p = stats.pearsonr(bcs_arr, acc_arr)\\\\n    spearman_rho, spearman_p = stats.spearmanr(bcs_arr, acc_arr)\\\\n    \\\\n    # Bootstrap 95% CI for R²\\\\n    n_boot = 10000\\\\n    r2_boots = []\\\\n    for _ in range(n_boot):\\\\n        idx = np.random.choice(n, n, replace=True)\\\\n        try:\\\\n            r2_boot = LinearRegression().fit(X[idx], y[idx]).score(X[idx], y[idx])\\\\n            r2_boots.append(r2_boot)\\\\n        except:\\\\n            pass\\\\n    ci_lower, ci_upper = np.percentile(r2_boots, [2.5, 97.5])\\\\n    \\\\n    results[count_level] = {\\\\n        \\\\'r2\\\\': round(r2, 4),\\\\n        \\\\'r2_ci\\\\': [round(ci_lower, 4), round(ci_upper, 4)],\\\\n        \\\\'pearson_r\\\\': round(pearson_r, 4),\\\\n        \\\\'pearson_p\\\\': float(f\\\\'{pearso
…[truncated 5795 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_docred_bcs_r2_20260519T140257",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T14:06:25.867900+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-38874",
  "command": "cat > /tmp/r2_analysis.py << 'PYEOF'\nimport json, numpy as np\nfrom scipy import stats\nfrom sklearn.linear_model import LinearRegression\n\nnp.random.seed(42)\n\nwith open('/root/schema-dag-extraction/artifacts/exp_docred_bcs_expanded/bcs_controlled_results.json') as f:\n    data = json.load(f)\n\nresults = {}\nn_boot = 10000\n\nfor count_level in ['count_16', 'count_32']:\n    bcs_all, acc_all = [], []\n    for strategy in ['high_bcs', 'low_bcs', 'random']:\n        key = f'bcs_{count_level}_{strategy}'\n        bcs_all.extend(data[key]['bcs_values'])\n        acc_all.extend(data[key]['batches'])\n    bcs_arr = np.array(bcs_all)\n    acc_arr = np.array(acc_all)\n    n = len(bcs_arr)\n    X = bcs_arr.reshape(-1, 1)\n    y = acc_arr\n    model = LinearRegression().fit(X, y)\n    r2 = model.score(X, y)\n    pearson_r, pearson_p = stats.pearsonr(bcs_arr, acc_arr)\n    spearman_rho, spearman_p = stats.spearmanr(bcs_arr, acc_arr)\n    r2_boots = []\n    for _ in range(n_boot):\n        idx = np.random.choice(n, n, replace=True)\n        r2_boots.append(LinearRegression().fit(X[idx], y[idx]).score(X[idx], y[idx]))\n    ci_lo, ci_hi = np.percentile(r2_boots, [2.5, 97.5])\n    results[count_level] = {\n        'r2': round(r2, 4), 'r2_ci': [round(ci_lo, 4), round(ci_hi, 4)],\n        'pearson_r': round(pearson_r, 4), 'pearson_p': float(f'{pearson_p:.2e}'),\n        'spearman_rho': round(spearman_rho, 4), 'spearman_p': float(f'{spearman_p:.2e}'),\n        'n': n, 'slope': round(model.coef_[0], 4), 'intercept': round(model.intercept_, 4)\n    }\n\n# Pooled\nbcs_p, acc_p, labels = [], [], []\nfor cl in ['count_16', 'count_32']:\n    for s in ['high_bcs', 'low_bcs', 'random']:\n        key = f'bcs_{cl}_{s}'\n        bcs_p.extend(data[key]['bcs_values'])\n        acc_p.extend(data[key]['batches'])\n        labels.extend([cl] * len(data[key]['bcs_values']))\nbcs_p, acc_p = np.array(bcs_p), np.array(acc_p)\nXp = bcs_p.reshape(-1, 1)\nmp = LinearRegression().fit(Xp, acc_p)\nr2_p = mp.score(Xp, acc_p)\nr2_bp = [LinearRegression().fit(Xp[i:=np.random.choice(len(Xp), len(Xp), replace=True)], acc_p[i]).score(Xp[i], acc_p[i]) for _ in range(n_boot)]\nci_p = np.percentile(r2_bp, [2.5, 97.5])\n# Semi-partial R2\ndummy = np.array([1 if l == 'count_32' else 0 for l in labels]).reshape(-1, 1)\nr2_full = LinearRegression().fit(np.hstack([Xp, dummy]), acc_p).score(np.hstack([Xp, dummy]), acc_p)\nr2_co = LinearRegression().fit(dummy, acc_p).score(dummy, acc_p)\nresults['pooled'] = {\n    'r2': round(r2_p, 4), 'r2_ci': [round(ci_p[0], 4), round(ci_p[1], 4)],\n    'n': len(bcs_p), 'slope': round(mp.coef_[0], 4), 'intercept': round(mp.intercept_, 4),\n    'pearson_r': round(float(stats.pearsonr(bcs_p, acc_p)[0]), 4),\n    'spearman_rho': round(float(stats.spearmanr(bcs_p, acc_p)[0]), 4),\n    'r2_controlling_count': round(r2_full - r2_co, 4), 'r2_full_model': round(r2_full, 4)\n}\nresults['comparison'] = {'original_r2': 0.525, 'original_n': 35, 'original_ci': [0.27, 0.73]}\n\nwith open('/root/schema-dag-extraction/artifacts/exp_docred_bcs_expanded/r2_analysis.json', 'w') as f:\n    json.dump(results, f, indent=2)\n\nfor cl in ['count_16', 'count_32']:\n    r = results[cl]\n    print(f\"{cl} (n={r['n']}): R2={r['r2']:.4f} CI[{r['r2_ci'][0]:.4f},{r['r2_ci'][1]:.4f}] pearson={r['pearson_r']:.4f}(p={r['pearson_p']:.1e}) spearman={r['spearman_rho']:.4f}(p={r['spearman_p']:.1e}) slope={r['slope']:.4f} int={r['intercept']:.4f}\")\np = results['pooled']\nprint(f\"pooled (n={p['n']}): R2={p['r2']:.4f} CI[{p['r2_ci'][0]:.4f},{p['r2_ci'][1]:.4f}] semi-partial={p['r2_controlling_count']:.4f} full={p['r2_full_model']:.4f}\")\nr2s = [results['count_16']['r2'], results['count_32']['r2']]\nprint(f\"Paper: R2={min(r2s):.2f}-{max(r2s):.2f} ({min(r2s)*100:.0f}-{max(r2s)*100:.0f}%)\")\nprint(f\"vs original: R2=0.525 CI[0.27,0.73] n=35\")\nPYEOF\necho \"SCRIPT_WRITTEN\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_docred_bcs_r2_20260519T140257",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "cat > /tmp/r2_analysis.py << 'PYEOF'\nimport json, numpy as np\nfrom scipy import stats\nfrom sklearn.linear_model import LinearRegression\n\nnp.random.seed(42)\n\nwith open('/root/schema-dag-extraction/artifacts/exp_docred_bcs_expanded/bcs_controlled_results.json') as f:\n    data = json.load(f)\n\nresults = {}\nn_boot = 10000\n\nfor count_level in ['count_16', 'count_32']:\n    bcs_all, acc_all = [], []\n    for strategy in ['high_bcs', 'low_bcs', 'random']:\n        key = f'bcs_{count_level}_{strategy}'\n        bcs_all.extend(data[key]['bcs_values'])\n        acc_all.extend(data[key]['batches'])\n    bcs_arr = np.array(bcs_all)\n    acc_arr = np.array(acc_all)\n    n = len(bcs_arr)\n    X = bcs_arr.reshape(-1, 1)\n    y = acc_arr\n    model = LinearRegression().fit(X, y)\n    r2 = model.score(X, y)\n    pearson_r, pearson_p = stats.pearsonr(bcs_arr, acc_arr)\n    spearman_rho, spearman_p = stats.spearmanr(bcs_arr, acc_arr)\n    r2_boots = []\n    for _ in range(n_boot):\n        idx = np.random.choice(n, n, replace=True)\n        r2_boots.append(LinearRegression().fit(X[idx], y[idx]).score(X[idx], y[idx]))\n    ci_lo, ci_hi = np.percentile(r2_boots, [2.5, 97.5])\n    results[count_level] = {\n        'r2': round(r2, 4), 'r2_ci': [round(ci_lo, 4), round(ci_hi, 4)],\n        'pearson_r': round(pearson_r, 4), 'pearson_p': float(f'{pearson_p:.2e}'),\n        'spearman_rho': round(spearman_rho, 4), 'spearman_p': float(f'{spearman_p:.2e}'),\n        'n': n, 'slope': round(model.coef_[0], 4), 'intercept': round(model.intercept_, 4)\n    }\n\n# Pooled\nbcs_p, acc_p, labels = [], [], []\nfor cl in ['count_16', 'count_32']:\n    for s in ['high_bcs', 'low_bcs', 'random']:\n        key = f'bcs_{cl}_{s}'\n        bcs_p.extend(data[key]['bcs_values'])\n        acc_p.extend(data[key]['batches'])\n        labels.extend([cl] * len(data[key]['bcs_values']))\nbcs_p, acc_p = np.array(bcs_p), np.array(acc_p)\nXp = bcs_p.reshape(-1, 1)\nmp = LinearRegression().fit(Xp, acc_p)\nr2_p = mp.score(Xp, acc_p)\nr2_bp = [LinearRegression().fit(Xp[i:=np.random.choice(len(Xp), len(Xp), replace=True)], acc_p[i]).score(Xp[i], acc_p[i]) for _ in range(n_boot)]\nci_p = np.percentile(r2_bp, [2.5, 97.5])\n# Semi-partial R2\ndummy = np.array([1 if l == 'count_32' else 0 for l in labels]).reshape(-1, 1)\nr2_full = LinearRegression().fit(np.hstack([Xp, dummy]), acc_p).score(np.hstack([Xp, dummy]), acc_p)\nr2_co = LinearRegression().fit(dummy, acc_p).score(dummy, acc_p)\nresults['pooled'] = {\n    'r2': round(r2_p, 4), 'r2_ci': [round(ci_p[0], 4), round(ci_p[1], 4)],\n    'n': len(bcs_p), 'slope': round(mp.coef_[0], 4), 'intercept': round(mp.intercept_, 4),\n    'pearson_r': round(float(stats.pearsonr(bcs_p, acc_p)[0]), 4),\n    'spearman_rho': round(float(stats.spearmanr(bcs_p, acc_p)[0]), 4),\n    'r2_controlling_count': round(r2_full - r2_co, 4), 'r2_full_model': round(r2_full, 4)\n}\nresults['comparison'] = {'original_r2': 0.525, 'original_n': 35, 'original_ci': [0.27, 0.73]}\n\nwith open('/root/schema-dag-extraction/artifacts/exp_docred_bcs_expanded/r2_analysis.json', 'w') as f:\n    json.dump(results, f, indent=2)\n\nfor cl in ['count_16', 'count_32']:\n    r = results[cl]\n    print(f\"{cl} (n={r['n']}): R2={r['r2']:.4f} CI[{r['r2_ci'][0]:.4f},{r['r2_ci'][1]:.4f}] pearson={r['pearson_r']:.4f}(p={r['pearson_p']:.1e}) spearman={r['spearman_rho']:.4f}(p={r['spearman_p']:.1e}) slope={r['slope']:.4f} int={r['intercept']:.4f}\")\np = results['pooled']\nprint(f\"pooled (n={p['n']}): R2={p['r2']:.4f} CI[{p['r2_ci'][0]:.4f},{p['r2_ci'][1]:.4f}] semi-partial={p['r2_controlling_count']:.4f} full={p['r2_full_model']:.4f}\")\nr2s = [results['count_16']['r2'], results['count_32']['r2']]\nprint(f\"Paper: R2={min(r2s):.2f}-{max(r2s):.2f} ({min(r2s)*100:.0f}-{max(r2s)*100:.0f}%)\")\nprint(f\"vs original: R2=0.525 CI[0.27,0.73] n=35\")\nPYEOF\necho \"SCRIPT_WRITTEN\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T14:06:25.868095+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"SCRIPT_WRITTEN\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.97}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_docred_bcs_r2_20260519T140257",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T14:06:25.868223+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-38874",
  "command": "cd /root/schema-dag-extraction && /root/miniconda3/bin/python3 /tmp/r2_analysis.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_docred_bcs_r2_20260519T140257",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "cd /root/schema-dag-extraction && /root/miniconda3/bin/python3 /tmp/r2_analysis.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T14:06:25.868349+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'cd /root/schema-dag-extraction && /root/miniconda3/bin/python3 /tmp/r2_analysis.py'\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_docred_bcs_r2_20260519T140257",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T14:06:25.868514+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-38874",
  "command": "cat > /tmp/r2_fast.py << 'PYEOF'\nimport json, numpy as np\nfrom scipy import stats\n\nnp.random.seed(42)\n\ndef ols_r2(x, y):\n    n = len(x)\n    mx, my = x.mean(), y.mean()\n    ss_xy = np.sum((x - mx) * (y - my))\n    ss_xx = np.sum((x - mx) ** 2)\n    ss_yy = np.sum((y - my) ** 2)\n    if ss_xx == 0 or ss_yy == 0:\n        return 0, 0, 0\n    slope = ss_xy / ss_xx\n    intercept = my - slope * mx\n    r2 = (ss_xy ** 2) / (ss_xx * ss_yy)\n    return r2, slope, intercept\n\ndef bootstrap_r2(x, y, n_boot=10000):\n    n = len(x)\n    idx_all = np.random.randint(0, n, size=(n_boot, n))\n    r2s = np.empty(n_boot)\n    for i in range(n_boot):\n        idx = idx_all[i]\n        xi, yi = x[idx], y[idx]\n        mx, my = xi.mean(), yi.mean()\n        ss_xy = np.sum((xi - mx) * (yi - my))\n        ss_xx = np.sum((xi - mx) ** 2)\n        ss_yy = np.sum((yi - my) ** 2)\n        r2s[i] = (ss_xy ** 2) / (ss_xx * ss_yy) if ss_xx > 0 and ss_yy > 0 else 0\n    return np.percentile(r2s, [2.5, 97.5])\n\nwith open('/root/schema-dag-extraction/artifacts/exp_docred_bcs_expanded/bcs_controlled_results.json') as f:\n    data = json.load(f)\n\nresults = {}\nfor cl in ['count_16', 'count_32']:\n    bcs, acc = [], []\n    for s in ['high_bcs', 'low_bcs', 'random']:\n        k = f'bcs_{cl}_{s}'\n        bcs.extend(data[k]['bcs_values'])\n        acc.extend(data[k]['batches'])\n    bcs, acc = np.array(bcs), np.array(acc)\n    r2, slope, intercept = ols_r2(bcs, acc)\n    ci = bootstrap_r2(bcs, acc)\n    pr, pp = stats.pearsonr(bcs, acc)\n    sr, sp = stats.spearmanr(bcs, acc)\n    results[cl] = {\n        'r2': round(r2, 4), 'r2_ci': [round(ci[0], 4), round(ci[1], 4)],\n        'pearson_r': round(pr, 4), 'pearson_p': float(f'{pp:.2e}'),\n        'spearman_rho': round(sr, 4), 'spearman_p': float(f'{sp:.2e}'),\n        'n': len(bcs), 'slope': round(slope, 4), 'intercept': round(intercept, 4)\n    }\n\n# Pooled\nbcs_p, acc_p, labs = [], [], []\nfor cl in ['count_16', 'count_32']:\n    for s in ['high_bcs', 'low_bcs', 'random']:\n        k = f'bcs_{cl}_{s}'\n        bcs_p.extend(data[k]['bcs_values'])\n        acc_p.extend(data[k]['batches'])\n        labs.extend([cl] * len(data[k]['bcs_values']))\nbcs_p, acc_p = np.array(bcs_p), np.array(acc_p)\nr2_p, sl_p, int_p = ols_r2(bcs_p, acc_p)\nci_p = bootstrap_r2(bcs_p, acc_p)\n# Semi-partial: R2(BCS+count) - R2(count)\ndummy = np.array([1.0 if l == 'count_32' else 0.0 for l in labs])\nX_full = np.column_stack([bcs_p, dummy])\n# Full model R2 via multiple regression\nX_f = np.column_stack([np.ones(len(acc_p)), bcs_p, dummy])\nbeta_f = np.linalg.lstsq(X_f, acc_p, rcond=None)[0]\npred_f = X_f @ beta_f\nss_res_f = np.sum((acc_p - pred_f)**2)\nss_tot = np.sum((acc_p - acc_p.mean())**2)\nr2_full = 1 - ss_res_f / ss_tot\n# Count-only model\nX_c = np.column_stack([np.ones(len(acc_p)), dummy])\nbeta_c = np.linalg.lstsq(X_c, acc_p, rcond=None)[0]\npred_c = X_c @ beta_c\nr2_co = 1 - np.sum((acc_p - pred_c)**2) / ss_tot\nresults['pooled'] = {\n    'r2': round(r2_p, 4), 'r2_ci': [round(ci_p[0], 4), round(ci_p[1], 4)],\n    'n': len(bcs_p), 'slope': round(sl_p, 4), 'intercept': round(int_p, 4),\n    'pearson_r': round(float(stats.pearsonr(bcs_p, acc_p)[0]), 4),\n    'spearman_rho': round(float(stats.spearmanr(bcs_p, acc_p)[0]), 4),\n    'r2_controlling_count': round(r2_full - r2_co, 4), 'r2_full_model': round(r2_full, 4)\n}\nresults['comparison'] = {'original_r2': 0.525, 'original_n': 35, 'original_ci': [0.27, 0.73]}\n\nwith open('/root/schema-dag-extraction/artifacts/exp_docred_bcs_expanded/r2_analysis.json', 'w') as f:\n    json.dump(results, f, indent=2)\n\nfor cl in ['count_16', 'count_32']:\n    r = results[cl]\n    print(f\"{cl} (n={r['n']}): R2={r['r2']:.4f} CI[{r['r2_ci'][0]:.4f},{r['r2_ci'][1]:.4f}] pearson={r['pearson_r']:.4f}(p={r['pearson_p']:.1e}) spearman={r['spearman_rho']:.4f}(p={r['spearman_p']:.1e}) slope={r['slope']:.4f} int={r['intercept']:.4f}\")\np = results['pooled']\nprint(f\"pooled (n={p['n']}): R2={p['r2']:.4f} CI[{p['r2_ci'][0]:.4f},{p['r2_ci'][1]:.4f}] semi-partial={p['r2_controlling_count']:.4f} full={p['r2_full_model']:.4f}\")\nr2s = [results['count_16']['r2'], results['count_32']['r2']]\nprint(f\"Paper: R2={min(r2s):.2f}-{max(r2s):.2f} ({min(r2s)*100:.0f}-{max(r2s)*100:.0f}%)\")\nPYEOF\necho \"DONE_WRITING\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_docred_bcs_r2_20260519T140257",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "cat > /tmp/r2_fast.py << 'PYEOF'\nimport json, numpy as np\nfrom scipy import stats\n\nnp.random.seed(42)\n\ndef ols_r2(x, y):\n    n = len(x)\n    mx, my = x.mean(), y.mean()\n    ss_xy = np.sum((x - mx) * (y - my))\n    ss_xx = np.sum((x - mx) ** 2)\n    ss_yy = np.sum((y - my) ** 2)\n    if ss_xx == 0 or ss_yy == 0:\n        return 0, 0, 0\n    slope = ss_xy / ss_xx\n    intercept = my - slope * mx\n    r2 = (ss_xy ** 2) / (ss_xx * ss_yy)\n    return r2, slope, intercept\n\ndef bootstrap_r2(x, y, n_boot=10000):\n    n = len(x)\n    idx_all = np.random.randint(0, n, size=(n_boot, n))\n    r2s = np.empty(n_boot)\n    for i in range(n_boot):\n        idx = idx_all[i]\n        xi, yi = x[idx], y[idx]\n        mx, my = xi.mean(), yi.mean()\n        ss_xy = np.sum((xi - mx) * (yi - my))\n        ss_xx = np.sum((xi - mx) ** 2)\n        ss_yy = np.sum((yi - my) ** 2)\n        r2s[i] = (ss_xy ** 2) / (ss_xx * ss_yy) if ss_xx > 0 and ss_yy > 0 else 0\n    return np.percentile(r2s, [2.5, 97.5])\n\nwith open('/root/schema-dag-extraction/artifacts/exp_docred_bcs_expanded/bcs_controlled_results.json') as f:\n    data = json.load(f)\n\nresults = {}\nfor cl in ['count_16', 'count_32']:\n    bcs, acc = [], []\n    for s in ['high_bcs', 'low_bcs', 'random']:\n        k = f'bcs_{cl}_{s}'\n        bcs.extend(data[k]['bcs_values'])\n        acc.extend(data[k]['batches'])\n    bcs, acc = np.array(bcs), np.array(acc)\n    r2, slope, intercept = ols_r2(bcs, acc)\n    ci = bootstrap_r2(bcs, acc)\n    pr, pp = stats.pearsonr(bcs, acc)\n    sr, sp = stats.spearmanr(bcs, acc)\n    results[cl] = {\n        'r2': round(r2, 4), 'r2_ci': [round(ci[0], 4), round(ci[1], 4)],\n        'pearson_r': round(pr, 4), 'pearson_p': float(f'{pp:.2e}'),\n        'spearman_rho': round(sr, 4), 'spearman_p': float(f'{sp:.2e}'),\n        'n': len(bcs), 'slope': round(slope, 4), 'intercept': round(intercept, 4)\n    }\n\n# Pooled\nbcs_p, acc_p, labs = [], [], []\nfor cl in ['count_16', 'count_32']:\n    for s in ['high_bcs', 'low_bcs', 'random']:\n        k = f'bcs_{cl}_{s}'\n        bcs_p.extend(data[k]['bcs_values'])\n        acc_p.extend(data[k]['batches'])\n        labs.extend([cl] * len(data[k]['bcs_values']))\nbcs_p, acc_p = np.array(bcs_p), np.array(acc_p)\nr2_p, sl_p, int_p = ols_r2(bcs_p, acc_p)\nci_p = bootstrap_r2(bcs_p, acc_p)\n# Semi-partial: R2(BCS+count) - R2(count)\ndummy = np.array([1.0 if l == 'count_32' else 0.0 for l in labs])\nX_full = np.column_stack([bcs_p, dummy])\n# Full model R2 via multiple regression\nX_f = np.column_stack([np.ones(len(acc_p)), bcs_p, dummy])\nbeta_f = np.linalg.lstsq(X_f, acc_p, rcond=None)[0]\npred_f = X_f @ beta_f\nss_res_f = np.sum((acc_p - pred_f)**2)\nss_tot = np.sum((acc_p - acc_p.mean())**2)\nr2_full = 1 - ss_res_f / ss_tot\n# Count-only model\nX_c = np.column_stack([np.ones(len(acc_p)), dummy])\nbeta_c = np.linalg.lstsq(X_c, acc_p, rcond=None)[0]\npred_c = X_c @ beta_c\nr2_co = 1 - np.sum((acc_p - pred_c)**2) / ss_tot\nresults['pooled'] = {\n    'r2': round(r2_p, 4), 'r2_ci': [round(ci_p[0], 4), round(ci_p[1], 4)],\n    'n': len(bcs_p), 'slope': round(sl_p, 4), 'intercept': round(int_p, 4),\n    'pearson_r': round(float(stats.pearsonr(bcs_p, acc_p)[0]), 4),\n    'spearman_rho': round(float(stats.spearmanr(bcs_p, acc_p)[0]), 4),\n    'r2_controlling_count': round(r2_full - r2_co, 4), 'r2_full_model': round(r2_full, 4)\n}\nresults['comparison'] = {'original_r2': 0.525, 'original_n': 35, 'original_ci': [0.27, 0.73]}\n\nwith open('/root/schema-dag-extraction/artifacts/exp_docred_bcs_expanded/r2_analysis.json', 'w') as f:\n    json.dump(results, f, indent=2)\n\nfor cl in ['count_16', 'count_32']:\n    r = results[cl]\n    print(f\"{cl} (n={r['n']}): R2={r['r2']:.4f} CI[{r['r2_ci'][0]:.4f},{r['r2_ci'][1]:.4f}] pearson={r['pearson_r']:.4f}(p={r['pearson_p']:.1e}) spearman={r['spearman_rho']:.4f}(p={r['spearman_p']:.1e}) slope={r['slope']:.4f} int={r['intercept']:.4f}\")\np = results['pooled']\nprint(f\"pooled (n={p['n']}): R2={p['r2']:.4f} CI[{p['r2_ci'][0]:.4f},{p['r2_ci'][1]:.4f}] semi-partial={p['r2_controlling_count']:.4f} full={p['r2_full_model']:.4f}\")\nr2s = [results['count_16']['r2'], results['count_32']['r2']]\nprint(f\"Paper: R2={min(r2s):.2f}-{max(r2s):.2f} ({min(r2s)*100:.0f}-{max(r2s)*100:.0f}%)\")\nPYEOF\necho \"DONE_WRITING\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T14:06:25.868753+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"DONE_WRITING\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.01}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_docred_bcs_r2_20260519T140257",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T14:06:25.868970+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-38874",
  "command": "nohup /root/miniconda3/bin/python3 /tmp/r2_fast.py > /tmp/r2_output.log 2>&1 & echo \"PID=$!\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_docred_bcs_r2_20260519T140257",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "nohup /root/miniconda3/bin/python3 /tmp/r2_fast.py > /tmp/r2_output.log 2>&1 & echo \"PID=$!\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-19T14:06:25.869109+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"PID=614245\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_docred_bcs_r2_20260519T140257",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-19T14:06:25.869226+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "tail -20 /tmp/r2_output.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_docred_bcs_r2_20260519T140257",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "tail -20 /tmp/r2_output.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T14:06:25.869344+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_docred_bcs_r2_20260519T140257",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-19T14:06:25.869472+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "ps -p 614245 -o pid=",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_docred_bcs_r2_20260519T140257",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "ps -p 614245 -o pid=",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-19T14:06:25.869589+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_docred_bcs_r2_20260519T140257",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-19T14:06:25.869720+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "cat /tmp/r2_output.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_docred_bcs_r2_20260519T140257",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "cat /tmp/r2_output.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-19T14:06:25.869864+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"count_16 (n=55): R2=0.6528 CI[0.5272,0.7661] pearson=-0.8080(p=8.9e-14) spearman=-0.7623(p=1.4e-11) slope=-0.7317 int=0.9775\\ncount_32 (n=55): R2=0.6135 CI[0.4662,0.7482] pearson=-0.7833(p=1.6e-12) spearman=-0.6929(p=4.6e-09) slope=-0.6296 int=0.8558\\npooled (n=110): R2=0.5779 CI[0.4629,0.6838] semi-partial=0.5676 full=0.6784\\nPaper: R2=0.61-0.65 (61-65%)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_docred_bcs_r2_20260519T140257",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-19T14:06:25.870009+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "cat /root/schema-dag-extraction/artifacts/exp_docred_bcs_expanded/r2_analysis.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_docred_bcs_r2_20260519T140257",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "cat /root/schema-dag-extraction/artifacts/exp_docred_bcs_expanded/r2_analysis.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-19T14:06:25.870160+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"count_16\\\": {\\n    \\\"r2\\\": 0.6528,\\n    \\\"r2_ci\\\": [\\n      0.5272,\\n      0.7661\\n    ],\\n    \\\"pearson_r\\\": -0.808,\\n    \\\"pearson_p\\\": 8.93e-14,\\n    \\\"spearman_rho\\\": -0.7623,\\n    \\\"spearman_p\\\": 1.37e-11,\\n    \\\"n\\\": 55,\\n    \\\"slope\\\": -0.7317,\\n    \\\"intercept\\\": 0.9775\\n  },\\n  \\\"count_32\\\": {\\n    \\\"r2\\\": 0.6135,\\n    \\\"r2_ci\\\": [\\n      0.4662,\\n      0.7482\\n    ],\\n    \\\"pearson_r\\\": -0.7833,\\n    \\\"pearson_p\\\": 1.58e-12,\\n    \\\"spearman_rho\\\": -0.6929,\\n    \\\"spearman_p\\\": 4.56e-09,\\n    \\\"n\\\": 55,\\n    \\\"slope\\\": -0.6296,\\n    \\\"intercept\\\": 0.8558\\n  },\\n  \\\"pooled\\\": {\\n    \\\"r2\\\": 0.5779,\\n    \\\"r2_ci\\\": [\\n      0.4629,\\n      0.6838\\n    ],\\n    \\\"n\\\": 110,\\n    \\\"slope\\\": -0.7028,\\n    \\\"intercept\\\": 0.929,\\n    \\\"pearson_r\\\": -0.7602,\\n    \\\"spearman_rho\\\": -0.7407,\\n    \\\"r2_controlling_count\\\": 0.5676,\\n    \\\"r2_full_model\\\": 0.6784\\n  },\\n  \\\"comparison\\\": {\\n    \\\"original_r2\\\": 0.525,\\n    \\\"original_n\\\": 35,\\n    \\\"original_ci\\\": [\\n      0.27,\\n      0.73\\n    ]\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_docred_bcs_r2_20260519T140257",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-19T14:06:25.870332+00:00_

结果已保存到 `r2_analysis.json`。汇总：

### Per count level (n=55 each)

| Metric | count_16 | count_32 |
|--------|----------|----------|
| **R²** | **0.6528** | **0.6135** |
| R² 95% CI | [0.5272, 0.7661] | [0.4662, 0.7482] |
| Pearson r | −0.808 (p=8.9e-14) | −0.783 (p=1.6e-12) |
| Spearman ρ | −0.762 (p=1.4e-11) | −0.693 (p=4.6e-09) |
| Slope | −0.7317 | −0.6296 |
| Intercept | 0.9775 | 0.8558 |

### Pooled (n=110)
- R² (BCS only) = 0.5779, CI [0.4629, 0.6838]
- R² (BCS + count covariate) = 0.6784
- Semi-partial R² of BCS = 0.5676

### vs. original
- Original count_16: R² = 0.525, n=35, CI [0.27, 0.73]
- Expanded count_16: R² = **0.6528**, n=55, CI [0.53, 0.77] — 更高且 CI 更窄

### 论文引用
**R² = 0.61–0.65 (61–65%)**，替代原来的 "22–53%"。原来那个范围对应的是旧实验（n=35, R²=0.525 是 count_16 的，其他 count levels 的 R² 更低），expanded 实验两个 count level 都稳定在 61–65%。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_docred_bcs_r2_20260519T140257"
}
```

</details>

---
