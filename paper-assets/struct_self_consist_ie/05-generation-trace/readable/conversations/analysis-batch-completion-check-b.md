# analysis batch completion check b

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 0
- **Tool calls:** 18
- **Original source:** `logs/chats/worker_analysis_batch_completion_check_b_20260516T140055.jsonl`
- **Structured JSON:** [`4bc33470fd6957824e36.json`](../../sessions/4b/4bc33470fd6957824e36.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

37 recorded events

### Tool call

_source line 1 · 2026-05-16T14:02:35.025174+00:00_

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
  "session": "worker_analysis_batch_completion_check_b_20260516T140055",
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

_source line 2 · 2026-05-16T14:02:35.025651+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_batch_completion_check_b_20260516T140055",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T14:02:35.025924+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls -la /root/autodl-tmp/struct_self_consist_ie/output/exp_026_t05/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_batch_completion_check_b_20260516T140055",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls -la /root/autodl-tmp/struct_self_consist_ie/output/exp_026_t05/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-16T14:02:35.026186+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls -la /root/autodl-tmp/struct_self_consist_ie/output/exp_026_t08/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_batch_completion_check_b_20260516T140055",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls -la /root/autodl-tmp/struct_self_consist_ie/output/exp_026_t08/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-16T14:02:35.026431+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 20256\\ndrwxr-xr-x   2 root root       58 May 16 20:23 .\\ndrwxr-xr-x 115 root root     8192 May 16 21:37 ..\\n-rw-r--r--   1 root root     1727 May 16 20:23 report.json\\n-rw-r--r--   1 root root 20722852 May 16 20:23 samples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.91}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_batch_completion_check_b_20260516T140055",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T14:02:35.026659+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 19828\\ndrwxr-xr-x   2 root root       58 May 16 21:01 .\\ndrwxr-xr-x 115 root root     8192 May 16 21:37 ..\\n-rw-r--r--   1 root root     1732 May 16 21:01 report.json\\n-rw-r--r--   1 root root 20285117 May 16 21:01 samples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_batch_completion_check_b_20260516T140055",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T14:02:35.026880+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls -la /root/autodl-tmp/struct_self_consist_ie/output/exp_019_trained_verifier/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_batch_completion_check_b_20260516T140055",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls -la /root/autodl-tmp/struct_self_consist_ie/output/exp_019_trained_verifier/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T14:02:35.027114+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 56\\ndrwxr-xr-x   2 root root   119 May 16 19:32 .\\ndrwxr-xr-x 115 root root  8192 May 16 21:37 ..\\n-rw-r--r--   1 root root   702 May 16 19:32 feature_importance.json\\n-rw-r--r--   1 root root  2745 May 16 19:32 report.md\\n-rw-r--r--   1 root root  6842 May 16 19:32 results.json\\n-rw-r--r--   1 root root 25843 May 16 19:31 train_verifier.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_batch_completion_check_b_20260516T140055",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T14:02:35.027369+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls -la /root/autodl-tmp/struct_self_consist_ie/output/exp_027_mlp_verifier/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_batch_completion_check_b_20260516T140055",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls -la /root/autodl-tmp/struct_self_consist_ie/output/exp_027_mlp_verifier/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T14:02:35.027603+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 48\\ndrwxr-xr-x   2 root root    88 May 16 21:44 .\\ndrwxr-xr-x 115 root root  8192 May 16 21:37 ..\\n-rw-r--r--   1 root root  3169 May 16 21:44 report.md\\n-rw-r--r--   1 root root  7631 May 16 21:43 results.json\\n-rw-r--r--   1 root root 20904 May 16 21:44 train_mlp_verifier.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_batch_completion_check_b_20260516T140055",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T14:02:35.027851+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "wc -l /root/autodl-tmp/struct_self_consist_ie/output/exp_026_t05/samples.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_batch_completion_check_b_20260516T140055",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "wc -l /root/autodl-tmp/struct_self_consist_ie/output/exp_026_t05/samples.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T14:02:35.028078+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"551 /root/autodl-tmp/struct_self_consist_ie/output/exp_026_t05/samples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_batch_completion_check_b_20260516T140055",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T14:02:35.028321+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_026_t05/report.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_batch_completion_check_b_20260516T140055",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_026_t05/report.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T14:02:35.028611+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"dataset\\\": \\\"scierc\\\",\\n  \\\"subtask\\\": \\\"ner\\\",\\n  \\\"n_samples\\\": 8,\\n  \\\"temperature\\\": 0.5,\\n  \\\"num_instances\\\": 551,\\n  \\\"use_train_format\\\": true,\\n  \\\"greedy_f1\\\": 0.6646866646866646,\\n  \\\"oracle_f1\\\": 0.7423167848699763,\\n  \\\"oracle_headroom\\\": 0.07763012018331172,\\n  \\\"fleiss_kappa_mean\\\": 0.5768944047623729,\\n  \\\"soft_jaccard_mean\\\": 0.8333504281499606,\\n  \\\"correlation_fleiss_vs_f1_full\\\": {\\n    \\\"rho\\\": 0.2562729944979881,\\n    \\\"p_value\\\": 2.2246018886526807e-09,\\n    \\\"n\\\": 529\\n  },\\n  \\\"correlation_softjaccard_vs_f1_full\\\": {\\n    \\\"rho\\\": 0.2970104220289181,\\n    \\\"p_value\\\": 3.101588697922607e-12,\\n    \\\"n\\\": 529\\n  },\\n  \\\"correlation_fleiss_vs_f1_conditional\\\": {\\n    \\\"rho\\\": 0.23101526459064237,\\n    \\\"p_value\\\": 3.1856837449231265e-07,\\n    \\\"n\\\": 479\\n  },\\n  \\\"correlation_softjaccard_vs_f1_conditional\\\": {\\n    \\\"rho\\\": 0.2781284141706589,\\n    \\\"p_value\\\": 5.870932916256781e-10,\\n    \\\"n\\\": 479\\n  },\\n  \\\"n_gold_empty_filtered\\\": 22,\\n  \\\"n_greedy_f1_zero_filtered\\\": 50,\\n  \\\"structural_beats_surface\\\": true,\\n  \\\"rho_advantage\\\": 0.04073742753092996,\\n  \\\"sample_f1_mean\\\": 0.6358160799616321,\\n  \\\"sample_f1_std\\\": 0.3087691195817718,\\n  \\\"sample_f1_pct_zero\\\": 10.326086956521738,\\n  \\\"logprob_baseline\\\": {\\n    \\\"full\\\": {\\n      \\\"rho\\\": 0.21781651832605584,\\n      \\\"p_rho\\\": 4.2191798011736937e-07,\\n      \\\"tau\\\": 0.15754657878338615,\\n      \\\"p_tau\\\": 2.3394729435169404e-07,\\n      \\\"auroc\\\": 0.5781432748538011,\\n      \\\"n\\\": 529\\n    },\\n    \\\"conditional\\\": {\\n      \\\"rho\\\": 0.15563076800416717,\\n      \\\"p_rho\\\": 0.0006306098990388763,\\n      \\\"tau\\\": 0.11177590784221654,\\n      \\\"p_tau\\\": 0.000512367664145719,\\n      \\\"auroc\
…[truncated 335 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_batch_completion_check_b_20260516T140055",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T14:02:35.028880+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "wc -l /root/autodl-tmp/struct_self_consist_ie/output/exp_026_t08/samples.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_batch_completion_check_b_20260516T140055",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "wc -l /root/autodl-tmp/struct_self_consist_ie/output/exp_026_t08/samples.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T14:02:35.029115+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"551 /root/autodl-tmp/struct_self_consist_ie/output/exp_026_t08/samples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_batch_completion_check_b_20260516T140055",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T14:02:35.029360+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_026_t08/report.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_batch_completion_check_b_20260516T140055",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_026_t08/report.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T14:02:35.029651+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"dataset\\\": \\\"scierc\\\",\\n  \\\"subtask\\\": \\\"ner\\\",\\n  \\\"n_samples\\\": 8,\\n  \\\"temperature\\\": 0.8,\\n  \\\"num_instances\\\": 551,\\n  \\\"use_train_format\\\": true,\\n  \\\"greedy_f1\\\": 0.6632805497460412,\\n  \\\"oracle_f1\\\": 0.768361581920904,\\n  \\\"oracle_headroom\\\": 0.10508103217486275,\\n  \\\"fleiss_kappa_mean\\\": 0.45135470547078205,\\n  \\\"soft_jaccard_mean\\\": 0.7491270870949764,\\n  \\\"correlation_fleiss_vs_f1_full\\\": {\\n    \\\"rho\\\": 0.24975402762887722,\\n    \\\"p_value\\\": 5.770082197489549e-09,\\n    \\\"n\\\": 529\\n  },\\n  \\\"correlation_softjaccard_vs_f1_full\\\": {\\n    \\\"rho\\\": 0.3588756535805622,\\n    \\\"p_value\\\": 1.5945620683809034e-17,\\n    \\\"n\\\": 529\\n  },\\n  \\\"correlation_fleiss_vs_f1_conditional\\\": {\\n    \\\"rho\\\": 0.1870997229290378,\\n    \\\"p_value\\\": 3.923052013088392e-05,\\n    \\\"n\\\": 477\\n  },\\n  \\\"correlation_softjaccard_vs_f1_conditional\\\": {\\n    \\\"rho\\\": 0.31232058637927484,\\n    \\\"p_value\\\": 2.9811217205038742e-12,\\n    \\\"n\\\": 477\\n  },\\n  \\\"n_gold_empty_filtered\\\": 22,\\n  \\\"n_greedy_f1_zero_filtered\\\": 52,\\n  \\\"structural_beats_surface\\\": true,\\n  \\\"rho_advantage\\\": 0.10912162595168501,\\n  \\\"sample_f1_mean\\\": 0.6222022375307056,\\n  \\\"sample_f1_std\\\": 0.31200289440895507,\\n  \\\"sample_f1_pct_zero\\\": 11.1531190926276,\\n  \\\"logprob_baseline\\\": {\\n    \\\"full\\\": {\\n      \\\"rho\\\": 0.25255391809580263,\\n      \\\"p_rho\\\": 3.8442910139044905e-09,\\n      \\\"tau\\\": 0.18233307683445807,\\n      \\\"p_tau\\\": 2.2269564512574965e-09,\\n      \\\"auroc\\\": 0.5890452876376989,\\n      \\\"n\\\": 529\\n    },\\n    \\\"conditional\\\": {\\n      \\\"rho\\\": 0.18079103823336262,\\n      \\\"p_rho\\\": 7.158821030927929e-05,\\n      \\\"tau\\\": 0.13066179440161066,\\n      \\\"p_tau\\\": 5.122473633604472e-05,\\n      \\\"auroc
…[truncated 340 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_batch_completion_check_b_20260516T140055",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T14:02:35.029909+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_019_trained_verifier/report.md",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_batch_completion_check_b_20260516T140055",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_019_trained_verifier/report.md",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T14:02:35.030222+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"# exp-019: Trained Verifier Baseline (Logistic Regression)\\n\\nSeeds: [42, 123, 789], Dataset: SciERC NER, N=8, Qwen2.5-7B-Instruct\\n\\n## 1. Selection F1 Comparison\\n\\n| Method | seed42 | seed123 | seed789 | Mean ± σ |\\n|--------|--------|---------|---------|----------|\\n| Greedy | 0.6439 | 0.6457 | 0.6511 | 0.6469 ± 0.0037 |\\n| SJ (unsup) | 0.6450 | 0.6475 | 0.6378 | 0.6434 ± 0.0050 |\\n| FK (unsup) | 0.6448 | 0.6468 | 0.6410 | 0.6442 ± 0.0029 |\\n| LP (unsup) | 0.6501 | 0.6436 | 0.6478 | 0.6472 ± 0.0033 |\\n| EM (unsup) | 0.6362 | 0.6381 | 0.6406 | 0.6383 ± 0.0022 |\\n| VC (unsup) | 0.6256 | 0.6204 | 0.6195 | 0.6218 ± 0.0033 |\\n| **LR (supervised)** | 0.6484 | 0.6467 | 0.6490 | **0.6480 ± 0.0012** |\\n| Oracle | 0.7758 | 0.7805 | 0.7885 | 0.7816 ± 0.0064 |\\n\\nOracle gap: 0.1347\\nLR gain over greedy: +0.0011\\nLR vs best unsupervised (LP): +0.0009\\nGap closure: 0.8%\\n\\n## 2. Instance-level AUROC\\n\\n| Method | seed42 | seed123 | seed789 | Mean ± σ |\\n|--------|--------|---------|---------|----------|\\n| SJ | 0.6715 | 0.6919 | 0.6893 | 0.6842 ± 0.0111 |\\n| FK | 0.6154 | 0.6300 | 0.6020 | 0.6158 ± 0.0140 |\\n| LP | 0.6116 | 0.6132 | 0.6124 | 0.6124 ± 0.0008 |\\n| EM | 0.6472 | 0.6596 | 0.6468 | 0.6512 ± 0.0073 |\\n| VC | 0.6879 | 0.7089 | 0.7223 | 0.7064 ± 0.0173 |\\n| **LR (5 signals)** | 0.6795 | 0.7016 | 0.7109 | **0.6973 ± 0.0161** |\\n\\nLR vs best single signal (VC): -0.0090\\n\\n## 3. Feature Importance (LR Coefficients)\\n\\n| Signal | seed42 | seed123 | seed789 | Mean ± σ |\\n|--------|--------|---------|---------|----------|\\n| SJ | -0.1739 | -0.0996 | -0.0845 | -0.1193 ± 0.0479 |\\n| FK | 0.0925 | 0.1324 | 0.0432 | 0.0894 ± 0.0447 |\\n| LP | 0.1161 | 0.0914 | 0.1073 | 0.1049 ± 0.0125 |\\n| EM | 0.1913 | 0.1588 | -0.0438 | 0.1021 ± 0.1274 |\\n| VC | 0.6455 | 0.6768 | 0.9198 | 0.7474 ± 0.1501 |\\n\\n## 4. Ablation (Leave-One-Signal-Out AUROC)\\n\\n| Dropped | seed42 AUROC | seed123 A
…[truncated 1014 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_batch_completion_check_b_20260516T140055",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T14:02:35.030495+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_019_trained_verifier/results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_batch_completion_check_b_20260516T140055",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_019_trained_verifier/results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T14:02:35.030965+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"per_seed\\\": {\\n    \\\"42\\\": {\\n      \\\"n_instances\\\": 529,\\n      \\\"n_samples\\\": 8,\\n      \\\"greedy_f1\\\": 0.6439,\\n      \\\"oracle_f1\\\": 0.7758,\\n      \\\"unsup_selection_f1\\\": {\\n        \\\"SJ\\\": 0.645,\\n        \\\"FK\\\": 0.6448,\\n        \\\"LP\\\": 0.6501,\\n        \\\"EM\\\": 0.6362,\\n        \\\"VC\\\": 0.6256\\n      },\\n      \\\"lr_selection_f1_loo\\\": 0.6484,\\n      \\\"lr_selection_f1_5fold\\\": 0.6475,\\n      \\\"lr_auroc_loo\\\": 0.6795,\\n      \\\"lr_auroc_5fold\\\": 0.6794,\\n      \\\"single_signal_aurocs\\\": {\\n        \\\"SJ\\\": 0.6715,\\n        \\\"FK\\\": 0.6154,\\n        \\\"LP\\\": 0.6116,\\n        \\\"EM\\\": 0.6472,\\n        \\\"VC\\\": 0.6879\\n      },\\n      \\\"feature_importance\\\": {\\n        \\\"SJ\\\": -0.1739,\\n        \\\"FK\\\": 0.0925,\\n        \\\"LP\\\": 0.1161,\\n        \\\"EM\\\": 0.1913,\\n        \\\"VC\\\": 0.6455\\n      },\\n      \\\"ablation\\\": {\\n        \\\"SJ\\\": {\\n          \\\"auroc_without\\\": 0.6814,\\n          \\\"delta\\\": -0.0019\\n        },\\n        \\\"FK\\\": {\\n          \\\"auroc_without\\\": 0.6802,\\n          \\\"delta\\\": -0.0007\\n        },\\n        \\\"LP\\\": {\\n          \\\"auroc_without\\\": 0.6788,\\n          \\\"delta\\\": 0.0007\\n        },\\n        \\\"EM\\\": {\\n          \\\"auroc_without\\\": 0.678,\\n          \\\"delta\\\": 0.0015\\n        },\\n        \\\"VC\\\": {\\n          \\\"auroc_without\\\": 0.6577,\\n          \\\"delta\\\": 0.0218\\n        }\\n      },\\n      \\\"learning_curve\\\": {\\n        \\\"0.1\\\": {\\n          \\\"mean_auroc\\\": 0.6201,\\n          \\\"std_auroc\\\": 0.0755,\\n          \\\"n_train\\\": 52\\n        },\\n        \\\"0.25\\\": {\\n          \\\"mean_auroc\\\": 0.6682,\\n          \\\"std_auroc\\\": 0.0384,\\n          \\\"n_train\\\": 132\\n        },\\n        \\\"0.5\\\": {\\n          \\\"mean_auroc\\\"
…[truncated 7138 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_batch_completion_check_b_20260516T140055",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T14:02:35.031285+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_027_mlp_verifier/report.md",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_batch_completion_check_b_20260516T140055",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_027_mlp_verifier/report.md",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T14:02:35.031598+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"# exp-027: MLP + Random Forest Verifiers\\n\\n## Setup\\n- Data: SciERC NER, N=16, seeds=[42, 123, 456]\\n- Instances per seed: 551\\n- Binary label: instance best-sample F1 > median\\n- Instance AUROC: 5-fold stratified CV\\n- Selection F1: 5-fold grouped CV (grouped by instance)\\n- Features: 5 basic (SJ, FK, LP, EM, VC) or +10 pairwise interactions = 15\\n\\n## Main Results (3-seed mean +/- std)\\n\\n| Model | Features | AUROC | Selection F1 |\\n|-------|----------|-------|-------------|\\n| Best single (EM) | 1 | 0.6476 | 0.6470 (LP) |\\n| LR | 5 | 0.6522 +/- 0.0130 | 0.6406 +/- 0.0010 |\\n| MLP | 5 | 0.6393 +/- 0.0209 | 0.6377 +/- 0.0031 |\\n| RF | 5 | 0.5868 +/- 0.0208 | 0.6133 +/- 0.0120 |\\n| MLP | 15 | 0.6322 +/- 0.0165 | 0.6339 +/- 0.0079 |\\n| RF | 15 | 0.6043 +/- 0.0314 | 0.6143 +/- 0.0148 |\\n| Greedy | - | - | 0.6441 |\\n| Oracle | - | - | 0.8231 |\\n\\n## Key Findings\\n\\n1. **MLP ≈ LR on 5 features** (AUROC delta=-0.0129): nonlinear model does NOT improve over LR.\\n   Features are the bottleneck, not model capacity.\\n2. **RF underperforms** both LR and MLP (AUROC=0.5868), likely overfitting to noise with limited features.\\n3. Interaction features (15-feat): MLP delta=-0.0071, RF delta=+0.0175 - marginal or no gain.\\n4. Best supervised AUROC=0.6522 vs best single signal=0.6476 (delta=+0.0046)\\n5. Best supervised selection F1=0.6406 vs best unsup=0.6470 (delta=-0.0064)\\n\\n## Conclusion\\n\\n**Features are the bottleneck, not model capacity.** MLP and RF fail to improve over\\nsimple LR on 5 signals, and even LR barely beats the best single signal (EM).\\nThis confirms that the 5 instance-level aggregates (SJ, FK, LP, EM, VC) have\\nlimited discriminative information that cannot be unlocked by nonlinear models\\nor interaction terms. Future work should focus on richer features (e.g., per-sample\\nstructural patterns, entity-level signals) rather than more complex classifiers.\\n\\n## RF Fea
…[truncated 1505 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_batch_completion_check_b_20260516T140055",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T14:02:35.031881+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_027_mlp_verifier/results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_batch_completion_check_b_20260516T140055",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_027_mlp_verifier/results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T14:02:35.032406+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"per_seed\\\": {\\n    \\\"42\\\": {\\n      \\\"LR_5feat\\\": {\\n        \\\"auroc\\\": 0.6634,\\n        \\\"selection_f1\\\": 0.6396\\n      },\\n      \\\"MLP_5feat\\\": {\\n        \\\"auroc\\\": 0.6629,\\n        \\\"selection_f1\\\": 0.635\\n      },\\n      \\\"RF_5feat\\\": {\\n        \\\"auroc\\\": 0.6042,\\n        \\\"selection_f1\\\": 0.6154\\n      },\\n      \\\"MLP_15feat\\\": {\\n        \\\"auroc\\\": 0.6434,\\n        \\\"selection_f1\\\": 0.6374\\n      },\\n      \\\"RF_15feat\\\": {\\n        \\\"auroc\\\": 0.6267,\\n        \\\"selection_f1\\\": 0.6096\\n      },\\n      \\\"single_signal_aurocs\\\": {\\n        \\\"SJ\\\": 0.5838,\\n        \\\"FK\\\": 0.4915,\\n        \\\"LP\\\": 0.5618,\\n        \\\"EM\\\": 0.6509,\\n        \\\"VC\\\": 0.5676\\n      },\\n      \\\"unsup_selection_f1\\\": {\\n        \\\"SJ\\\": 0.646,\\n        \\\"FK\\\": 0.6469,\\n        \\\"LP\\\": 0.6453,\\n        \\\"EM\\\": 0.6317,\\n        \\\"VC\\\": 0.589\\n      },\\n      \\\"greedy_f1\\\": 0.6442,\\n      \\\"oracle_f1\\\": 0.8247,\\n      \\\"rf_importance_15\\\": {\\n        \\\"SJ\\\": 0.0581,\\n        \\\"FK\\\": 0.0622,\\n        \\\"LP\\\": 0.0802,\\n        \\\"EM\\\": 0.0427,\\n        \\\"VC\\\": 0.0501,\\n        \\\"SJxFK\\\": 0.0641,\\n        \\\"SJxLP\\\": 0.0755,\\n        \\\"SJxEM\\\": 0.0752,\\n        \\\"SJxVC\\\": 0.0542,\\n        \\\"FKxLP\\\": 0.0885,\\n        \\\"FKxEM\\\": 0.0695,\\n        \\\"FKxVC\\\": 0.0568,\\n        \\\"LPxEM\\\": 0.0839,\\n        \\\"LPxVC\\\": 0.0702,\\n        \\\"EMxVC\\\": 0.0688\\n      },\\n      \\\"rf_importance_5\\\": {\\n        \\\"SJ\\\": 0.1894,\\n        \\\"FK\\\": 0.2324,\\n        \\\"LP\\\": 0.2728,\\n        \\\"EM\\\": 0.1338,\\n        \\\"VC\\\": 0.1717\\n      },\\n      \\\"ablation_mlp\\\": {\\n        \\\"SJ\\\": {\\n          \\\"auroc_without\\\": 0.6558,\\n          \\\"delta\\\": 0.0071\\n        },\\n     
…[truncated 8223 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_batch_completion_check_b_20260516T140055",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T14:02:35.032695+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_019_trained_verifier/feature_importance.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_batch_completion_check_b_20260516T140055",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_019_trained_verifier/feature_importance.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T14:02:35.032949+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"SJ\\\": {\\n    \\\"mean\\\": -0.1193,\\n    \\\"std\\\": 0.0479,\\n    \\\"per_seed\\\": {\\n      \\\"42\\\": -0.1739,\\n      \\\"123\\\": -0.0996,\\n      \\\"789\\\": -0.0845\\n    }\\n  },\\n  \\\"FK\\\": {\\n    \\\"mean\\\": 0.0894,\\n    \\\"std\\\": 0.0447,\\n    \\\"per_seed\\\": {\\n      \\\"42\\\": 0.0925,\\n      \\\"123\\\": 0.1324,\\n      \\\"789\\\": 0.0432\\n    }\\n  },\\n  \\\"LP\\\": {\\n    \\\"mean\\\": 0.1049,\\n    \\\"std\\\": 0.0125,\\n    \\\"per_seed\\\": {\\n      \\\"42\\\": 0.1161,\\n      \\\"123\\\": 0.0914,\\n      \\\"789\\\": 0.1073\\n    }\\n  },\\n  \\\"EM\\\": {\\n    \\\"mean\\\": 0.1021,\\n    \\\"std\\\": 0.1274,\\n    \\\"per_seed\\\": {\\n      \\\"42\\\": 0.1913,\\n      \\\"123\\\": 0.1588,\\n      \\\"789\\\": -0.0438\\n    }\\n  },\\n  \\\"VC\\\": {\\n    \\\"mean\\\": 0.7474,\\n    \\\"std\\\": 0.1501,\\n    \\\"per_seed\\\": {\\n      \\\"42\\\": 0.6455,\\n      \\\"123\\\": 0.6768,\\n      \\\"789\\\": 0.9198\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_batch_completion_check_b_20260516T140055",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T14:02:35.033240+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/output/exp_026_t05/ -name \"*.log\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_batch_completion_check_b_20260516T140055",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/struct_self_consist_ie/output/exp_026_t05/ -name \"*.log\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-16T14:02:35.033465+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/output/exp_026_t08/ -name \"*.log\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_batch_completion_check_b_20260516T140055",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/struct_self_consist_ie/output/exp_026_t08/ -name \"*.log\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-16T14:02:35.033677+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_batch_completion_check_b_20260516T140055",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-16T14:02:35.033882+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_batch_completion_check_b_20260516T140055",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-16T14:02:35.034152+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_batch_completion_check_b_20260516T140055",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/",
    "description": "List artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-16T14:02:35.034411+00:00_

3seed_ner_summary.md
3seed_summary
__pycache__
_project
analysis_fk_bootstrap_ci_full.json
analysis_lp_range_cdf.json
analysis_lp_range_cdf_n16_3seed.json
analysis_scierc_n16_3seed_selection_f1.json
analysis_scierc_re_n16_3seed_selection_f1.json
analysis_unified_rho.json
analysis_unified_rho_full.json
analyze_exp004_re_diagnostic.py
analyze_exp004_v2_re_diagnostic.py
analyze_exp005_v2_temperature.py
analyze_exp015_metrics_expansion.py
analyze_exp016_ensemble.py
analyze_ood_signals.py
audit_autodl5090_loop3.md
audit_gpu5090_4x2_loop3.md
auroc_bug_diagnosis.md
autodl_process_check.md
bertoldi_citation_check
bjb1_status_report.md
bootstrap_ci_nscaling
bootstrap_ci_summary.json
bootstrap_ci_tables.tex
consistency.py
d072_paper_patch_inventory.md
d108
d108_lp_vc_combination
d112
d112_claim_audit
d113_table2_fix
d113_table2_narrative_fix
data
data_utils.py
dream_reports
evaluate_verifier.py
evaluation.py
exp-001
exp-015
exp-019
exp-022
exp001_postprocess.py
exp005_temperature
exp009_stratification_analysis.py
exp010_selection_curves
exp_001
exp_001_n16
exp_001_ner_n16_scierc
exp_001_seed456_v2_ner
exp_002
exp_003
exp_004_re_diagnostic
exp_004_v2
exp_005
exp_005_v2
exp_009_capability_stratification
exp_009_v2
exp_009_v2_re_rerun
exp_009_v2_stratification.py
exp_010_selection_curves
exp_011_ood_scierc_to_conll
exp_012_logprob_baseline
exp_012_rerun_1024
exp_015_metrics_expansion
exp_016_rerun_1024
exp_016_rerun_1024_bootstrap
exp_016_signal_ensemble
exp_016_v2
exp_016_v2_ensemble.py
exp_017_llama_conll_n8_t07
exp_018
exp_018_provenance_report.md
exp_019_trained_verifier
exp_023_lora_rank8
exp_025
exp_026_t12
exp_027
exp_entity_token_lp
exp_freeform_ablation
exp_freeform_conll_4seed
exp_llama3b_scierc_ablation
exp_vc_quartile_analysis
exp_verbalized_confidence
fig_selection_gap.png
figures
fk_excess_agreement_all_configs.md
freeform_3seed_summary.json
freeform_ablation_appendix_table.tex
freeform_ablation_deep_analysis.md
freeform_ablation_results.md
ft_001
ft_002
greedy_f1_
…[truncated 1014 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_batch_completion_check_b_20260516T140055",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-16T14:02:35.034692+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/batch_completion_check_b.md",
  "content": "# Batch Completion Check B — 2026-05-16\n\n## 1. exp_026_t05 (T=0.5 SciERC NER inference)\n\n**Status**: COMPLETE  \n**Path**: `output/exp_026_t05/`  \n**Files**: `samples.jsonl` (551 lines, 20.7MB), `report.json` (1.7KB)  \n**Timestamp**: 2026-05-16 20:23\n\n### Key Metrics\n| Metric | Value |\n|--------|-------|\n| Greedy F1 | 0.6647 |\n| Oracle F1 | 0.7423 |\n| Oracle headroom | 0.0776 |\n| Fleiss κ mean | 0.5769 |\n| Soft Jaccard mean | 0.8334 |\n| ρ(SJ, F1) full | 0.2970 |\n| ρ(FK, F1) full | 0.2563 |\n| SJ rho advantage over FK | +0.0407 |\n| Logprob AUROC (full) | 0.5781 |\n| Logprob AUROC (conditional) | 0.5921 |\n| Verdict | **FAIL** |\n\n---\n\n## 2. exp_026_t08 (T=0.8 SciERC NER inference)\n\n**Status**: COMPLETE  \n**Path**: `output/exp_026_t08/`  \n**Files**: `samples.jsonl` (551 lines, 20.3MB), `report.json` (1.7KB)  \n**Timestamp**: 2026-05-16 21:01\n\n### Key Metrics\n| Metric | Value |\n|--------|-------|\n| Greedy F1 | 0.6633 |\n| Oracle F1 | 0.7684 |\n| Oracle headroom | 0.1051 |\n| Fleiss κ mean | 0.4514 |\n| Soft Jaccard mean | 0.7491 |\n| ρ(SJ, F1) full | 0.3589 |\n| ρ(FK, F1) full | 0.2498 |\n| SJ rho advantage over FK | +0.1091 |\n| Logprob AUROC (full) | 0.5890 |\n| Logprob AUROC (conditional) | 0.5509 |\n| Verdict | **MARGINAL** |\n\n### T=0.5 vs T=0.8 Comparison\n| Metric | T=0.5 | T=0.8 | Δ |\n|--------|-------|-------|---|\n| Oracle headroom | 0.0776 | 0.1051 | +0.0275 |\n| SJ ρ (full) | 0.2970 | 0.3589 | +0.0619 |\n| SJ ρ advantage | 0.0407 | 0.1091 | +0.0684 |\n| Logprob AUROC | 0.5781 | 0.5890 | +0.0109 |\n\nT=0.8 has more headroom and SJ correlation advantage is much larger.\n\n---\n\n## 3. exp_019 Trained Verifier (Logistic Regression) — N=8\n\n**Status**: COMPLETE  \n**Path**: `output/exp_019_trained_verifier/`  \n**Seeds**: [42, 123, 789], Dataset: SciERC NER, N=8\n\n### Selection F1\n| Method | Mean ± σ | vs Greedy |\n|--------|----------|-----------|\n| Greedy | 0.6469 ± 0.0037 | — |\n| LR (supervised) | **0.6480 ± 0.0012** | **+0.0011** |\n| LP (best unsup) | 0.6472 ± 0.0033 | +0.0003 |\n| Oracle | 0.7816 ± 0.0064 | +0.1347 |\n\n**Oracle gap closure: 0.8%** (LR closes 0.0011 of 0.1347 gap)\n\n### Instance AUROC\n| Method | Mean ± σ |\n|--------|----------|\n| VC (best single) | 0.7064 ± 0.0173 |\n| LR (5 signals) | 0.6973 ± 0.0161 |\n| SJ | 0.6842 ± 0.0111 |\n| EM | 0.6512 ± 0.0073 |\n\nLR AUROC vs best single (VC): **-0.0090** (does not exceed)\n\n### LR Feature Coefficients (mean)\n| Signal | Coefficient |\n|--------|-------------|\n| VC | **0.7474** |\n| LP | 0.1049 |\n| EM | 0.1021 |\n| FK | 0.0894 |\n| SJ | -0.1193 |\n\nVC dominates; signals largely redundant.\n\n---\n\n## 4. exp_027 MLP + RF Verifiers — N=16\n\n**Status**: COMPLETE  \n**Path**: `output/exp_027_mlp_verifier/`  \n**Seeds**: [42, 123, 456], Dataset: SciERC NER, N=16\n\n### Main Results (3-seed mean)\n| Model | Features | AUROC | Selection F1 | vs Greedy (0.6441) |\n|-------|----------|-------|-------------|-----|\n| LR | 5 | 0.6522 ± 0.0130 | 0.6406 ± 0.0010 | -0.0035 |\n| MLP | 5 | 0.6393 ± 0.0209 | 0.6377 ± 0.0031 | -0.0064 |\n| RF | 5 | 0.5868 ± 0.0208 | 0.6133 ± 0.0120 | -0.0308 |\n| MLP | 15 | 0.6322 ± 0.0165 | 0.6339 ± 0.0079 | -0.0102 |\n| RF | 15 | 0.6043 ± 0.0314 | 0.6143 ± 0.0148 | -0.0298 |\n| Best unsup (LP) | 1 | — | 0.6470 | +0.0029 |\n| Best single AUROC (EM) | 1 | 0.6476 | — | — |\n| Oracle | — | — | 0.8231 | +0.1790 |\n\n### Key Finding\n**Features are the bottleneck, not model capacity.**\n- MLP ≈ LR (AUROC delta = -0.0129): nonlinear model does NOT improve over LR\n- RF underperforms both (AUROC = 0.5868)\n- Interaction features (15-feat) provide marginal or no gain\n- All supervised models FAIL to beat greedy on selection F1\n- Best supervised AUROC (LR=0.6522) only marginally exceeds best single signal (EM=0.6476, delta=+0.0046)\n\n### RF Feature Importance (15-feat, top 5)\n| Feature | Importance |\n|---------|-----------|\n| FKxLP | 0.0888 |\n| LPxEM | 0.0780 |\n| LP | 0.0768 |\n| SJxLP | 0.0761 |\n| SJxEM | 0.0729 |\n\n---\n\n## Summary\n\n| Experiment | Status | Key Result |\n|-----------|--------|------------|\n| exp_026_t05 | ✓ Complete | FAIL verdict; SJ ρ=0.297, headroom=0.078 |\n| exp_026_t08 | ✓ Complete | MARGINAL verdict; SJ ρ=0.359, headroom=0.105 |\n| exp_019 LR verifier | ✓ Complete | Gap closure 0.8%; LR barely beats greedy (+0.0011) |\n| exp_027 MLP/RF verifier | ✓ Complete | Features are bottleneck; MLP/RF cannot beat LR |\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_batch_completion_check_b_20260516T140055",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/batch_completion_check_b.md",
    "content": "# Batch Completion Check B — 2026-05-16\n\n## 1. exp_026_t05 (T=0.5 SciERC NER inference)\n\n**Status**: COMPLETE  \n**Path**: `output/exp_026_t05/`  \n**Files**: `samples.jsonl` (551 lines, 20.7MB), `report.json` (1.7KB)  \n**Timestamp**: 2026-05-16 20:23\n\n### Key Metrics\n| Metric | Value |\n|--------|-------|\n| Greedy F1 | 0.6647 |\n| Oracle F1 | 0.7423 |\n| Oracle headroom | 0.0776 |\n| Fleiss κ mean | 0.5769 |\n| Soft Jaccard mean | 0.8334 |\n| ρ(SJ, F1) full | 0.2970 |\n| ρ(FK, F1) full | 0.2563 |\n| SJ rho advantage over FK | +0.0407 |\n| Logprob AUROC (full) | 0.5781 |\n| Logprob AUROC (conditional) | 0.5921 |\n| Verdict | **FAIL** |\n\n---\n\n## 2. exp_026_t08 (T=0.8 SciERC NER inference)\n\n**Status**: COMPLETE  \n**Path**: `output/exp_026_t08/`  \n**Files**: `samples.jsonl` (551 lines, 20.3MB), `report.json` (1.7KB)  \n**Timestamp**: 2026-05-16 21:01\n\n### Key Metrics\n| Metric | Value |\n|--------|-------|\n| Greedy F1 | 0.6633 |\n| Oracle F1 | 0.7684 |\n| Oracle headroom | 0.1051 |\n| Fleiss κ mean | 0.4514 |\n| Soft Jaccard mean | 0.7491 |\n| ρ(SJ, F1) full | 0.3589 |\n| ρ(FK, F1) full | 0.2498 |\n| SJ rho advantage over FK | +0.1091 |\n| Logprob AUROC (full) | 0.5890 |\n| Logprob AUROC (conditional) | 0.5509 |\n| Verdict | **MARGINAL** |\n\n### T=0.5 vs T=0.8 Comparison\n| Metric | T=0.5 | T=0.8 | Δ |\n|--------|-------|-------|---|\n| Oracle headroom | 0.0776 | 0.1051 | +0.0275 |\n| SJ ρ (full) | 0.2970 | 0.3589 | +0.0619 |\n| SJ ρ advantage | 0.0407 | 0.1091 | +0.0684 |\n| Logprob AUROC | 0.5781 | 0.5890 | +0.0109 |\n\nT=0.8 has more headroom and SJ correlation advantage is much larger.\n\n---\n\n## 3. exp_019 Trained Verifier (Logistic Regression) — N=8\n\n**Status**: COMPLETE  \n**Path**: `output/exp_019_trained_verifier/`  \n**Seeds**: [42, 123, 789], Dataset: SciERC NER, N=8\n\n### Selection F1\n| Method | Mean ± σ | vs Greedy |\n|--------|----------|-----------|\n| Greedy | 0.6469 ± 0.0037 | — |\n| LR (supervised) | **0.6480 ± 0.0012** | **+0.0011** |\n| LP (best unsup) | 0.6472 ± 0.0033 | +0.0003 |\n| Oracle | 0.7816 ± 0.0064 | +0.1347 |\n\n**Oracle gap closure: 0.8%** (LR closes 0.0011 of 0.1347 gap)\n\n### Instance AUROC\n| Method | Mean ± σ |\n|--------|----------|\n| VC (best single) | 0.7064 ± 0.0173 |\n| LR (5 signals) | 0.6973 ± 0.0161 |\n| SJ | 0.6842 ± 0.0111 |\n| EM | 0.6512 ± 0.0073 |\n\nLR AUROC vs best single (VC): **-0.0090** (does not exceed)\n\n### LR Feature Coefficients (mean)\n| Signal | Coefficient |\n|--------|-------------|\n| VC | **0.7474** |\n| LP | 0.1049 |\n| EM | 0.1021 |\n| FK | 0.0894 |\n| SJ | -0.1193 |\n\nVC dominates; signals largely redundant.\n\n---\n\n## 4. exp_027 MLP + RF Verifiers — N=16\n\n**Status**: COMPLETE  \n**Path**: `output/exp_027_mlp_verifier/`  \n**Seeds**: [42, 123, 456], Dataset: SciERC NER, N=16\n\n### Main Results (3-seed mean)\n| Model | Features | AUROC | Selection F1 | vs Greedy (0.6441) |\n|-------|----------|-------|-------------|-----|\n| LR | 5 | 0.6522 ± 0.0130 | 0.6406 ± 0.0010 | -0.0035 |\n| MLP | 5 | 0.6393 ± 0.0209 | 0.6377 ± 0.0031 | -0.0064 |\n| RF | 5 | 0.5868 ± 0.0208 | 0.6133 ± 0.0120 | -0.0308 |\n| MLP | 15 | 0.6322 ± 0.0165 | 0.6339 ± 0.0079 | -0.0102 |\n| RF | 15 | 0.6043 ± 0.0314 | 0.6143 ± 0.0148 | -0.0298 |\n| Best unsup (LP) | 1 | — | 0.6470 | +0.0029 |\n| Best single AUROC (EM) | 1 | 0.6476 | — | — |\n| Oracle | — | — | 0.8231 | +0.1790 |\n\n### Key Finding\n**Features are the bottleneck, not model capacity.**\n- MLP ≈ LR (AUROC delta = -0.0129): nonlinear model does NOT improve over LR\n- RF underperforms both (AUROC = 0.5868)\n- Interaction features (15-feat) provide marginal or no gain\n- All supervised models FAIL to beat greedy on selection F1\n- Best supervised AUROC (LR=0.6522) only marginally exceeds best single signal (EM=0.6476, delta=+0.0046)\n\n### RF Feature Importance (15-feat, top 5)\n| Feature | Importance |\n|---------|-----------|\n| FKxLP | 0.0888 |\n| LPxEM | 0.0780 |\n| LP | 0.0768 |\n| SJxLP | 0.0761 |\n| SJxEM | 0.0729 |\n\n---\n\n## Summary\n\n| Experiment | Status | Key Result |\n|-----------|--------|------------|\n| exp_026_t05 | ✓ Complete | FAIL verdict; SJ ρ=0.297, headroom=0.078 |\n| exp_026_t08 | ✓ Complete | MARGINAL verdict; SJ ρ=0.359, headroom=0.105 |\n| exp_019 LR verifier | ✓ Complete | Gap closure 0.8%; LR barely beats greedy (+0.0011) |\n| exp_027 MLP/RF verifier | ✓ Complete | Features are bottleneck; MLP/RF cannot beat LR |\n"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-16T14:02:35.035019+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/batch_completion_check_b.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_batch_completion_check_b_20260516T140055",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-16T14:02:35.035316+00:00_

所有 3 个实验均已完成，报告已写入 `artifacts/batch_completion_check_b.md`。

核心发现：
- **exp_026_t05** (T=0.5): 完成，verdict=FAIL，SJ ρ=0.297，oracle headroom 仅 0.078
- **exp_026_t08** (T=0.8): 完成，verdict=MARGINAL，SJ ρ=0.359，headroom 更大(0.105)，T=0.8 各项指标优于 T=0.5
- **Trained verifier (exp_019 LR, N=8)**: LR selection F1 仅比 greedy +0.0011，oracle gap closure 0.8%，VC 系数独大(0.75)，信号高度冗余
- **exp_027 MLP/RF (N=16)**: MLP/RF 均无法超越 LR，所有监督方法的 selection F1 甚至不如 greedy。**结论：特征是瓶颈而非模型容量**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_batch_completion_check_b_20260516T140055"
}
```

</details>

---
