# analysis exp003 p2 data check

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 0
- **Tool calls:** 21
- **Original source:** `logs/chats/worker_analysis_exp003-p2-data-check_20260520T022655.jsonl`
- **Structured JSON:** [`8c75c5e5b8679abc7e88.json`](../../sessions/8c/8c75c5e5b8679abc7e88.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

43 recorded events

### Tool call

_source line 1 · 2026-05-20T02:29:09.278568+00:00_

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
  "session": "worker_analysis_exp003-p2-data-check_20260520T022655",
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

_source line 2 · 2026-05-20T02:29:09.278930+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp003-p2-data-check_20260520T022655",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T02:29:09.279099+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "ls -la /root/entrainment_gated_ft/lm_eval_clean/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp003-p2-data-check_20260520T022655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "ls -la /root/entrainment_gated_ft/lm_eval_clean/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-20T02:29:09.279231+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "ls -la /root/entrainment_gated_ft/analysis/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp003-p2-data-check_20260520T022655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "ls -la /root/entrainment_gated_ft/analysis/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-20T02:29:09.279429+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 1689444\\ndrwxr-xr-x 10 root root      4096 May 20 01:51 .\\ndrwxr-xr-x 11 root root      4096 May 20 09:23 ..\\n-rw-r--r--  1 root root 132179538 May 18 21:55 1.3B-100B-GatedDeltaNet-hybrid-12-1.json\\n-rw-r--r--  1 root root    271099 May 18 21:55 1.3B-100B-GatedDeltaNet-hybrid-12-1_final.log\\n-rw-r--r--  1 root root     14282 May 18 22:13 1.3B-100B-GatedDeltaNet-hybrid-24-1_results.json\\n-rw-r--r--  1 root root     14289 May 18 22:00 1.3B-100B-GatedDeltaNet-hybrid-3-1_results.json\\n-rw-r--r--  1 root root     14300 May 18 22:07 1.3B-100B-GatedDeltaNet-hybrid-6-1_results.json\\n-rw-r--r--  1 root root 132160102 May 18 21:45 1.3B-100B-GatedDeltaNet-pure.json\\n-rw-r--r--  1 root root      5444 May 18 21:38 1.3B-100B-GatedDeltaNet-pure.log\\n-rw-r--r--  1 root root    246441 May 18 21:45 1.3B-100B-GatedDeltaNet-pure_final.log\\n-rw-r--r--  1 root root   7929496 May 18 21:17 1.3B-100B-GatedDeltaNet-pure_lambada_only.json\\n-rw-r--r--  1 root root       286 May 18 21:22 1.3B-100B-GatedDeltaNet-pure_results.json\\n-rw-r--r--  1 root root 132153710 May 19 00:15 1.3B-100B-HGRN2-hybrid-12-1.json\\n-rw-r--r--  1 root root 132165547 May 19 00:24 1.3B-100B-HGRN2-hybrid-24-1.json\\n-rw-r--r--  1 root root 132168839 May 19 00:51 1.3B-100B-HGRN2-hybrid-3-1.json\\n-rw-r--r--  1 root root 132176544 May 19 01:04 1.3B-100B-HGRN2-hybrid-6-1.json\\n-rw-r--r--  1 root root 132172054 May 19 02:37 1.3B-100B-HGRN2-pure.json\\n-rw-r--r--  1 root root 132168964 May 18 23:27 1.3B-100B-RetNet-hybrid-12-1.json\\n-rw-r--r--  1 root root 132159737 May 18 23:30 1.3B-100B-RetNet-hybrid-24-1.json\\n-rw-r--r--  1 root root 132165204 May 19 00:41 1.3B-100B-RetNet-hybrid-3-1.json\\n-rw-r--r--  1 root root 132160156 May 19 00:34 1.3B-100B-RetNet-hybrid-6-1.json\\n-rw-r--r--  1 root root 132175098 May 18 23:15 1.3B-100B-RetNet-pure.json\\n-rw-r--r--  1 root root    344046 May 18 22:04 1.3B-100B-RetNet-pure_final.log\\n-rw-r--r--  1 root r
…[truncated 1870 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp003-p2-data-check_20260520T022655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T02:29:09.279675+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 3908\\ndrwxr-xr-x  5 root root   4096 May 20 02:52 .\\ndrwxr-xr-x 11 root root   4096 May 20 09:23 ..\\n-rw-r--r--  1 root root   7227 May 19 22:37 additional_benchmarks_convergence.py\\n-rw-r--r--  1 root root   4587 May 20 01:03 all_benchmark_convergence_summary.json\\ndrwxr-xr-x  2 root root   4096 May 20 01:14 attention_weights\\n-rw-r--r--  1 root root  23299 May 19 14:38 convergence_analysis.pdf\\n-rw-r--r--  1 root root 131061 May 19 14:38 convergence_analysis.png\\n-rw-r--r--  1 root root   4818 May 19 14:38 convergence_analysis.py\\n-rw-r--r--  1 root root  34344 May 19 13:37 cross_scale_convergence.pdf\\n-rw-r--r--  1 root root 305368 May 19 13:37 cross_scale_convergence.png\\n-rw-r--r--  1 root root  12937 May 19 13:37 cross_scale_convergence.py\\n-rw-r--r--  1 root root   9219 May 19 13:37 cross_scale_summary.csv\\n-rw-r--r--  1 root root  12372 May 20 02:52 exp007_analysis.py\\n-rw-r--r--  1 root root   5885 May 20 02:53 exp007_analysis_summary.json\\n-rw-r--r--  1 root root  13822 May 19 23:06 exp010_bridge_analysis.py\\n-rw-r--r--  1 root root   1539 May 19 23:07 exp010_bridge_results.csv\\n-rw-r--r--  1 root root   6557 May 19 23:07 exp010_bridge_summary.json\\n-rw-r--r--  1 root root   9295 May 20 00:18 exp011_convergence_analysis.py\\n-rw-r--r--  1 root root   1450 May 20 00:18 exp011_convergence_results.csv\\n-rw-r--r--  1 root root   2840 May 20 00:18 exp011_convergence_summary.json\\n-rw-r--r--  1 root root  15494 May 20 00:42 extract_attention_weights.py\\ndrwxr-xr-x  2 root root     70 May 20 00:07 figures\\n-rw-r--r--  1 root root  12116 May 19 22:00 fix_hgrn2_and_complete.py\\n-rw-r--r--  1 root root   3160 May 20 00:07 generate_paper_data.py\\n-rw-r--r--  1 root root 218267 May 19 04:59 lambada_attention_analysis.png\\n-rw-r--r--  1 root root 181908 May 19 04:59 lambada_crossmodel_scatter.png\\n-rw-r--r--  1 root root  37465 May 19 14:54 lambada_matched_comparison.pdf\\n-rw-r--r-
…[truncated 3214 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp003-p2-data-check_20260520T022655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T02:29:09.279891+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "find /root/entrainment_gated_ft/lm_eval_clean/ -name \"*pure*\" -o -name \"*h3*\" -o -name \"*hybrid-3-1*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp003-p2-data-check_20260520T022655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "find /root/entrainment_gated_ft/lm_eval_clean/ -name \"*pure*\" -o -name \"*h3*\" -o -name \"*hybrid-3-1*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T02:29:09.280077+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/entrainment_gated_ft/lm_eval_clean/gdn_pure_validation.log\\n/root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-GatedDeltaNet-pure_results.json\\n/root/entrainment_gated_ft/lm_eval_clean/retnet_pure.log\\n/root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-GatedDeltaNet-pure_lambada_only.json\\n/root/entrainment_gated_ft/lm_eval_clean/retnet_pure_v2.log\\n/root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-GatedDeltaNet-pure.log\\n/root/entrainment_gated_ft/lm_eval_clean/retnet_pure_final.log\\n/root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-GatedDeltaNet-pure_final.log\\n/root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-GatedDeltaNet-pure.json\\n/root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-RetNet-pure_results.json\\n/root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-RetNet-pure_final.log\\n/root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-GatedDeltaNet-hybrid-3-1_results.json\\n/root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-RetNet-pure.json\\n/root/entrainment_gated_ft/lm_eval_clean/340m/340M-20B-GatedDeltaNet-pure-baseline.json\\n/root/entrainment_gated_ft/lm_eval_clean/340m/340M-20B-GatedDeltaNet-hybrid-3-1.json\\n/root/entrainment_gated_ft/lm_eval_clean/340m/340M-20B-RetNet-pure\\n/root/entrainment_gated_ft/lm_eval_clean/340m/340M-20B-RetNet-pure/340M-20B-RetNet-pure.json\\n/root/entrainment_gated_ft/lm_eval_clean/340m/340M-20B-RetNet-hybrid-3-1\\n/root/entrainment_gated_ft/lm_eval_clean/340m/340M-20B-RetNet-hybrid-3-1/340M-20B-RetNet-hybrid-3-1.json\\n/root/entrainment_gated_ft/lm_eval_clean/340m/340M-20B-HGRN2-pure-baseline\\n/root/entrainment_gated_ft/lm_eval_clean/340m/340M-20B-HGRN2-pure-baseline/340M-20B-HGRN2-pure-baseline.json\\n/root/entrainment_gated_ft/lm_eval_clean/340m/340M-20B-HGRN2-hybrid-3-1\\n/root/entrainment_gated_ft/lm_eval_clean/340m/340M-20B-HGRN2-hybrid-3-1/340M-20B-HGRN2-hybrid-3-1.json\\n/root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-RetNet-hybrid-3-1.json\\n/
…[truncated 3323 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp003-p2-data-check_20260520T022655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T02:29:09.280227+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "head -5 /root/entrainment_gated_ft/analysis/sample_perplexity_results.csv",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp003-p2-data-check_20260520T022655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "head -5 /root/entrainment_gated_ft/analysis/sample_perplexity_results.csv",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T02:29:09.280359+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"doc_id,GDN_pure_loss,GDN_helped,GDN_hurt,RetNet_pure_loss,RetNet_helped,RetNet_hurt,HGRN2_pure_loss,HGRN2_helped,HGRN2_hurt\\r\\n0,3.423137,0,0,3.505070,0,0,3.428979,0,0\\r\\n1,3.347848,0,0,3.456544,0,1,3.342849,0,0\\r\\n2,3.456130,1,0,3.479137,0,0,3.446791,0,0\\r\\n3,2.973024,0,0,3.004976,0,0,2.914154,0,1\\r\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.82}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp003-p2-data-check_20260520T022655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T02:29:09.280480+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "wc -l /root/entrainment_gated_ft/analysis/sample_perplexity_results.csv",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp003-p2-data-check_20260520T022655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "wc -l /root/entrainment_gated_ft/analysis/sample_perplexity_results.csv",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-20T02:29:09.280599+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "ls -la /root/entrainment_gated_ft/lm_eval_clean/1.3b/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp003-p2-data-check_20260520T022655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "ls -la /root/entrainment_gated_ft/lm_eval_clean/1.3b/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-20T02:29:09.280744+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"5154 /root/entrainment_gated_ft/analysis/sample_perplexity_results.csv\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.86}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp003-p2-data-check_20260520T022655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T02:29:09.280867+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 4\\ndrwxr-xr-x  5 root root  104 May 19 11:40 .\\ndrwxr-xr-x 10 root root 4096 May 20 01:51 ..\\ndrwxr-xr-x  3 root root   81 May 19 11:39 GDN-h24-1-logsamples\\ndrwxr-xr-x  3 root root   80 May 19 11:38 GDN-h3-1-logsamples\\ndrwxr-xr-x  3 root root   80 May 19 11:40 GDN-h6-1-logsamples\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.87}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp003-p2-data-check_20260520T022655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T02:29:09.280995+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "cat /root/entrainment_gated_ft/analysis/sample_perplexity_summary.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp003-p2-data-check_20260520T022655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "cat /root/entrainment_gated_ft/analysis/sample_perplexity_summary.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T02:29:09.281159+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"phase2_perplexity\\\": {\\n    \\\"per_arch\\\": {\\n      \\\"GDN\\\": {\\n        \\\"n_helped\\\": 462,\\n        \\\"n_hurt\\\": 615,\\n        \\\"helped_mean\\\": 3.3694951250439598,\\n        \\\"helped_median\\\": 3.381838321685791,\\n        \\\"hurt_mean\\\": 3.3382038151345603,\\n        \\\"hurt_median\\\": 3.329054832458496,\\n        \\\"helped_std\\\": 0.3823682017339572,\\n        \\\"hurt_std\\\": 0.36454578631490975,\\n        \\\"U\\\": 148410.0,\\n        \\\"p\\\": 0.20918889018323172,\\n        \\\"r_rb\\\": -0.04466265441875206\\n      },\\n      \\\"RetNet\\\": {\\n        \\\"n_helped\\\": 426,\\n        \\\"n_hurt\\\": 495,\\n        \\\"helped_mean\\\": 3.4432366946493516,\\n        \\\"helped_median\\\": 3.412011504173279,\\n        \\\"hurt_mean\\\": 3.420704110945114,\\n        \\\"hurt_median\\\": 3.4004030227661133,\\n        \\\"helped_std\\\": 0.3818517346223916,\\n        \\\"hurt_std\\\": 0.37388984830392696,\\n        \\\"U\\\": 107210.0,\\n        \\\"p\\\": 0.659319445715385,\\n        \\\"r_rb\\\": -0.01683501683501687\\n      },\\n      \\\"HGRN2\\\": {\\n        \\\"n_helped\\\": 548,\\n        \\\"n_hurt\\\": 395,\\n        \\\"helped_mean\\\": 3.3775308388863166,\\n        \\\"helped_median\\\": 3.3708789348602295,\\n        \\\"hurt_mean\\\": 3.3538390660587747,\\n        \\\"hurt_median\\\": 3.3314054012298584,\\n        \\\"helped_std\\\": 0.3714853490681262,\\n        \\\"hurt_std\\\": 0.3634934045283436,\\n        \\\"U\\\": 112999.0,\\n        \\\"p\\\": 0.24785563963631896,\\n        \\\"r_rb\\\": -0.044063568326711655\\n      }\\n    },\\n    \\\"cross_arch_helped\\\": {\\n      \\\"kruskal_wallis_H\\\": 7.810488381645882,\\n      \\\"kruskal_wallis_p\\\": 0.020136036855481716,\\n      \\\"pairwise\\\": {\\n        \\\"GDN_vs_RetNet\\\": {\\n          \\\"U\\\": 88819.0,\\n          \\\"p\\\": 0.01205330727905433,\\n          \\\"r\\\": 0.09742292136
…[truncated 639 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp003-p2-data-check_20260520T022655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T02:29:09.281340+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "du -sh /root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-GatedDeltaNet-pure.json /root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-RetNet-pure.json /root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-HGRN2-pure.json /root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-GatedDeltaNet-hybrid-3-1.json /root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-RetNet-hybrid-3-1.json /root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-HGRN2-hybrid-3-1.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp003-p2-data-check_20260520T022655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "du -sh /root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-GatedDeltaNet-pure.json /root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-RetNet-pure.json /root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-HGRN2-pure.json /root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-GatedDeltaNet-hybrid-3-1.json /root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-RetNet-hybrid-3-1.json /root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-HGRN2-hybrid-3-1.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T02:29:09.281514+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"127M\\t/root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-GatedDeltaNet-pure.json\\n127M\\t/root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-RetNet-pure.json\\n127M\\t/root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-HGRN2-pure.json\\n127M\\t/root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-RetNet-hybrid-3-1.json\\n127M\\t/root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-HGRN2-hybrid-3-1.json\\n\", \"stderr\": \"du: cannot access '/root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-GatedDeltaNet-hybrid-3-1.json': No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.76}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp003-p2-data-check_20260520T022655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T02:29:09.281684+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "head -3 /root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-GatedDeltaNet-pure_lambada_only.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp003-p2-data-check_20260520T022655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "head -3 /root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-GatedDeltaNet-pure_lambada_only.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T02:29:09.281852+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"results\\\": {\\n    \\\"lambada_openai\\\": {\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.76}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp003-p2-data-check_20260520T022655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T02:29:09.282006+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "du -sh /root/entrainment_gated_ft/lm_eval_clean/1.3b/GDN-h3-1-logsamples/1.3B-100B-GatedDeltaNet-hybrid-3-1.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp003-p2-data-check_20260520T022655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "du -sh /root/entrainment_gated_ft/lm_eval_clean/1.3b/GDN-h3-1-logsamples/1.3B-100B-GatedDeltaNet-hybrid-3-1.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-20T02:29:09.282131+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"12K\\t/root/entrainment_gated_ft/lm_eval_clean/1.3b/GDN-h3-1-logsamples/1.3B-100B-GatedDeltaNet-hybrid-3-1.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.77}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp003-p2-data-check_20260520T022655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T02:29:09.282248+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "python3 -c \"import json; d=json.load(open('/root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-GatedDeltaNet-pure.json')); tasks=list(d.get('samples',{}).keys()) if 'samples' in d else list(d.keys()); print('keys:', tasks[:10])\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp003-p2-data-check_20260520T022655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "python3 -c \"import json; d=json.load(open('/root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-GatedDeltaNet-pure.json')); tasks=list(d.get('samples',{}).keys()) if 'samples' in d else list(d.keys()); print('keys:', tasks[:10])\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-20T02:29:09.282365+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp003-p2-data-check_20260520T022655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T02:29:09.282478+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "wc -l /root/entrainment_gated_ft/analysis/lambada_per_example.csv /root/entrainment_gated_ft/analysis/lambada_matched_per_example.csv",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp003-p2-data-check_20260520T022655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "wc -l /root/entrainment_gated_ft/analysis/lambada_per_example.csv /root/entrainment_gated_ft/analysis/lambada_matched_per_example.csv",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-20T02:29:09.282616+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  5162 /root/entrainment_gated_ft/analysis/lambada_per_example.csv\\n  5162 /root/entrainment_gated_ft/analysis/lambada_matched_per_example.csv\\n 10324 total\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.76}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp003-p2-data-check_20260520T022655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T02:29:09.282787+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "python3 -c \"import json; d=json.load(open('/root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-GatedDeltaNet-pure.json')); print(list(d.keys())[:10])\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp003-p2-data-check_20260520T022655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "python3 -c \"import json; d=json.load(open('/root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-GatedDeltaNet-pure.json')); print(list(d.keys())[:10])\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-20T02:29:09.282921+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp003-p2-data-check_20260520T022655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-20T02:29:09.283039+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "head -1 /root/entrainment_gated_ft/lm_eval_clean/1.3b/GDN-h3-1-logsamples/1.3B-100B-GatedDeltaNet-hybrid-3-1.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp003-p2-data-check_20260520T022655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "head -1 /root/entrainment_gated_ft/lm_eval_clean/1.3b/GDN-h3-1-logsamples/1.3B-100B-GatedDeltaNet-hybrid-3-1.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-20T02:29:09.283156+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "head -1 /root/entrainment_gated_ft/analysis/lambada_per_example.csv",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp003-p2-data-check_20260520T022655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "head -1 /root/entrainment_gated_ft/analysis/lambada_per_example.csv",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-20T02:29:09.283271+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.76}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp003-p2-data-check_20260520T022655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-20T02:29:09.283410+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"doc_id,context_length,target,gdn_pure_acc,gdn_pure_lp,gdn_h12_acc,gdn_h12_lp,hgrn2_pure_acc,hgrn2_pure_lp,hgrn2_h3_acc,hgrn2_h3_lp\\r\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.86}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp003-p2-data-check_20260520T022655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T02:29:09.283580+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "du -sh /root/entrainment_gated_ft/lm_eval_clean/exp011/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp003-p2-data-check_20260520T022655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "du -sh /root/entrainment_gated_ft/lm_eval_clean/exp011/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-20T02:29:09.283743+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"952K\\t/root/entrainment_gated_ft/lm_eval_clean/exp011/\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.76}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp003-p2-data-check_20260520T022655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-20T02:29:09.283866+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "ls -lh /root/entrainment_gated_ft/lm_eval_clean/exp011/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp003-p2-data-check_20260520T022655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "ls -lh /root/entrainment_gated_ft/lm_eval_clean/exp011/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-20T02:29:09.283981+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "head -5 /root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-GatedDeltaNet-pure_lambada_only.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp003-p2-data-check_20260520T022655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "head -5 /root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-GatedDeltaNet-pure_lambada_only.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-20T02:29:09.284110+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 948K\\n-rw-r--r-- 1 root root  15K May 19 22:49 1.3B-100B-GatedDeltaNet-hybrid-12-1.json\\n-rw-r--r-- 1 root root  15K May 19 22:42 1.3B-100B-GatedDeltaNet-hybrid-24-1.json\\n-rw-r--r-- 1 root root  15K May 19 23:01 1.3B-100B-GatedDeltaNet-hybrid-3-1.json\\n-rw-r--r-- 1 root root  15K May 19 22:56 1.3B-100B-GatedDeltaNet-hybrid-6-1.json\\n-rw-r--r-- 1 root root  15K May 19 22:31 1.3B-100B-GatedDeltaNet-pure.json\\n-rw-r--r-- 1 root root  15K May 19 23:52 1.3B-100B-HGRN2-hybrid-12-1.json\\n-rw-r--r-- 1 root root  15K May 19 23:46 1.3B-100B-HGRN2-hybrid-24-1.json\\n-rw-r--r-- 1 root root  15K May 20 00:05 1.3B-100B-HGRN2-hybrid-3-1.json\\n-rw-r--r-- 1 root root  15K May 19 23:59 1.3B-100B-HGRN2-hybrid-6-1.json\\n-rw-r--r-- 1 root root  15K May 19 23:39 1.3B-100B-HGRN2-pure.json\\n-rw-r--r-- 1 root root  15K May 19 23:20 1.3B-100B-RetNet-hybrid-12-1.json\\n-rw-r--r-- 1 root root  15K May 19 23:13 1.3B-100B-RetNet-hybrid-24-1.json\\n-rw-r--r-- 1 root root  15K May 19 23:33 1.3B-100B-RetNet-hybrid-3-1.json\\n-rw-r--r-- 1 root root  15K May 19 23:27 1.3B-100B-RetNet-hybrid-6-1.json\\n-rw-r--r-- 1 root root  15K May 19 23:07 1.3B-100B-RetNet-pure.json\\n-rw-r--r-- 1 root root 691K May 20 00:11 run_all.log\\n-rw-r--r-- 1 root root  15K May 20 00:11 transformer_1.3B_baseline.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.81}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp003-p2-data-check_20260520T022655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-20T02:29:09.284248+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"results\\\": {\\n    \\\"lambada_openai\\\": {\\n      \\\"name\\\": \\\"lambada_openai\\\",\\n      \\\"alias\\\": \\\"lambada_openai\\\",\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.86}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp003-p2-data-check_20260520T022655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-20T02:29:09.284420+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp003-p2-data-check_20260520T022655",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/",
    "description": "List artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-20T02:29:09.284546+00:00_

__pycache__
_project
d009_assessment.md
dream_reports
eval_composition.py
eval_composition_modified.py
exp-001
exp-003
exp-003-p2
exp-004
exp-007
exp007_data_check.md
exp007_script_ready.md
lm_eval_1.3b_results.md
manifest.yaml
null_jaccard_results.json
paper_agent_inputs.md
paper_data
per_example_data_audit.md
synthetic_task_design.md
wang_7b_search_results.md
wang_et_al_analysis.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp003-p2-data-check_20260520T022655",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-20T02:29:09.284710+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/exp003_p2_data_check.md",
  "content": "# exp-003-p2 数据完整性检查\n\n检查时间: 2026-05-20\n\n## 1. Pure 模型 log_samples (1.3B)\n\n全部存在，均为 lm-eval `--log_samples` 全 benchmark 输出（含 per-example logprob）：\n\n| 模型 | 文件路径 | 大小 |\n|------|----------|------|\n| GatedDeltaNet-pure | `lm_eval_clean/1.3B-100B-GatedDeltaNet-pure.json` | 127M |\n| RetNet-pure | `lm_eval_clean/1.3B-100B-RetNet-pure.json` | 127M |\n| HGRN2-pure | `lm_eval_clean/1.3B-100B-HGRN2-pure.json` | 127M |\n\n另有 GDN-pure LAMBADA-only 结果文件: `1.3B-100B-GatedDeltaNet-pure_lambada_only.json` (7.6M)，格式为 results（非 per-example samples）。\n\n## 2. H3-1 (hybrid-3-1) 模型 log_samples (1.3B)\n\n| 模型 | 文件路径 | 大小 | 状态 |\n|------|----------|------|------|\n| GatedDeltaNet h3-1 | 顶层无 log_samples，仅 `_results.json` (14K) | — | **缺失** |\n| RetNet h3-1 | `lm_eval_clean/1.3B-100B-RetNet-hybrid-3-1.json` | 127M | 存在 |\n| HGRN2 h3-1 | `lm_eval_clean/1.3B-100B-HGRN2-hybrid-3-1.json` | 127M | 存在 |\n\n**注意**: GDN h3-1 的 log_samples 缺失。`1.3b/GDN-h3-1-logsamples/` 下有一个 12K 文件，是 results 格式（非 per-example）。顶层 `1.3B-100B-GatedDeltaNet-hybrid-3-1_results.json` 也仅是聚合 scores。\n\nGDN **h12-1** 的 log_samples 存在: `1.3B-100B-GatedDeltaNet-hybrid-12-1.json` (127M)。\n\n## 3. exp-003-p2 分析脚本和输出\n\n| 文件 | 存在 | 详情 |\n|------|------|------|\n| `analysis/sample_perplexity_analysis.py` | ✓ | 12K, 2026-05-19 22:06 |\n| `analysis/sample_perplexity_results.csv` | ✓ | 226K, 5154 行 (header + 5153 examples = LAMBADA 全集) |\n| `analysis/sample_perplexity_summary.json` | ✓ | 统计检验结果 |\n| `analysis/sample_perplexity_figure.pdf` | ✓ | 可视化 |\n| `analysis/lambada_per_example.csv` | ✓ | 5162 行, 列含 `gdn_h12` (非 h3) |\n| `analysis/lambada_matched_per_example.csv` | ✓ | 5162 行, matched comparison |\n\n### sample_perplexity_results.csv 字段\n```\ndoc_id, GDN_pure_loss, GDN_helped, GDN_hurt, RetNet_pure_loss, RetNet_helped, RetNet_hurt, HGRN2_pure_loss, HGRN2_helped, HGRN2_hurt\n```\n\n### 统计检验结果 (summary.json)\n- GDN: helped=462, hurt=615, Mann-Whitney p=0.209 (不显著)\n- RetNet: helped=426, hurt=495, p=0.659 (不显著)\n- HGRN2: helped=548, hurt=395, p=0.248 (不显著)\n- 结论: within-arch helped vs hurt perplexity 差异不显著\n\n### lambada_per_example.csv 注意\n列名使用 `gdn_h12`（hybrid-12-1）而非 `gdn_h3`（hybrid-3-1），说明 **GDN 的 per-example 分析使用了 h12-1 作为 hybrid baseline**，可能因为 h3-1 log_samples 缺失。\n\n## 4. 结论\n\n| 项 | 状态 |\n|----|------|\n| Pure 模型 log_samples | ✅ 3/3 完整 |\n| H3-1 模型 log_samples | ⚠️ 2/3 (GDN h3-1 缺失，分析用了 h12-1 替代) |\n| 分析脚本和结果 | ✅ 完整，5153 examples 覆盖 LAMBADA 全集 |\n| 是否需要重跑 GPU inference | **视需求而定** — 如果要求 GDN 也用 h3-1 做 per-example 对比（与 RetNet/HGRN2 一致），需补跑 GDN h3-1 的 `--log_samples` eval；如果接受用 h12-1 作为 GDN hybrid baseline，则现有数据已足够 |\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp003-p2-data-check_20260520T022655",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/exp003_p2_data_check.md",
    "content": "# exp-003-p2 数据完整性检查\n\n检查时间: 2026-05-20\n\n## 1. Pure 模型 log_samples (1.3B)\n\n全部存在，均为 lm-eval `--log_samples` 全 benchmark 输出（含 per-example logprob）：\n\n| 模型 | 文件路径 | 大小 |\n|------|----------|------|\n| GatedDeltaNet-pure | `lm_eval_clean/1.3B-100B-GatedDeltaNet-pure.json` | 127M |\n| RetNet-pure | `lm_eval_clean/1.3B-100B-RetNet-pure.json` | 127M |\n| HGRN2-pure | `lm_eval_clean/1.3B-100B-HGRN2-pure.json` | 127M |\n\n另有 GDN-pure LAMBADA-only 结果文件: `1.3B-100B-GatedDeltaNet-pure_lambada_only.json` (7.6M)，格式为 results（非 per-example samples）。\n\n## 2. H3-1 (hybrid-3-1) 模型 log_samples (1.3B)\n\n| 模型 | 文件路径 | 大小 | 状态 |\n|------|----------|------|------|\n| GatedDeltaNet h3-1 | 顶层无 log_samples，仅 `_results.json` (14K) | — | **缺失** |\n| RetNet h3-1 | `lm_eval_clean/1.3B-100B-RetNet-hybrid-3-1.json` | 127M | 存在 |\n| HGRN2 h3-1 | `lm_eval_clean/1.3B-100B-HGRN2-hybrid-3-1.json` | 127M | 存在 |\n\n**注意**: GDN h3-1 的 log_samples 缺失。`1.3b/GDN-h3-1-logsamples/` 下有一个 12K 文件，是 results 格式（非 per-example）。顶层 `1.3B-100B-GatedDeltaNet-hybrid-3-1_results.json` 也仅是聚合 scores。\n\nGDN **h12-1** 的 log_samples 存在: `1.3B-100B-GatedDeltaNet-hybrid-12-1.json` (127M)。\n\n## 3. exp-003-p2 分析脚本和输出\n\n| 文件 | 存在 | 详情 |\n|------|------|------|\n| `analysis/sample_perplexity_analysis.py` | ✓ | 12K, 2026-05-19 22:06 |\n| `analysis/sample_perplexity_results.csv` | ✓ | 226K, 5154 行 (header + 5153 examples = LAMBADA 全集) |\n| `analysis/sample_perplexity_summary.json` | ✓ | 统计检验结果 |\n| `analysis/sample_perplexity_figure.pdf` | ✓ | 可视化 |\n| `analysis/lambada_per_example.csv` | ✓ | 5162 行, 列含 `gdn_h12` (非 h3) |\n| `analysis/lambada_matched_per_example.csv` | ✓ | 5162 行, matched comparison |\n\n### sample_perplexity_results.csv 字段\n```\ndoc_id, GDN_pure_loss, GDN_helped, GDN_hurt, RetNet_pure_loss, RetNet_helped, RetNet_hurt, HGRN2_pure_loss, HGRN2_helped, HGRN2_hurt\n```\n\n### 统计检验结果 (summary.json)\n- GDN: helped=462, hurt=615, Mann-Whitney p=0.209 (不显著)\n- RetNet: helped=426, hurt=495, p=0.659 (不显著)\n- HGRN2: helped=548, hurt=395, p=0.248 (不显著)\n- 结论: within-arch helped vs hurt perplexity 差异不显著\n\n### lambada_per_example.csv 注意\n列名使用 `gdn_h12`（hybrid-12-1）而非 `gdn_h3`（hybrid-3-1），说明 **GDN 的 per-example 分析使用了 h12-1 作为 hybrid baseline**，可能因为 h3-1 log_samples 缺失。\n\n## 4. 结论\n\n| 项 | 状态 |\n|----|------|\n| Pure 模型 log_samples | ✅ 3/3 完整 |\n| H3-1 模型 log_samples | ⚠️ 2/3 (GDN h3-1 缺失，分析用了 h12-1 替代) |\n| 分析脚本和结果 | ✅ 完整，5153 examples 覆盖 LAMBADA 全集 |\n| 是否需要重跑 GPU inference | **视需求而定** — 如果要求 GDN 也用 h3-1 做 per-example 对比（与 RetNet/HGRN2 一致），需补跑 GDN h3-1 的 `--log_samples` eval；如果接受用 h12-1 作为 GDN hybrid baseline，则现有数据已足够 |\n"
  }
}
````

</details>

---

### Tool result

_source line 42 · 2026-05-20T02:29:09.284890+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/exp003_p2_data_check.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp003-p2-data-check_20260520T022655",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-20T02:29:09.285044+00:00_

报告已写入 `artifacts/exp003_p2_data_check.md`。

核心发现：
- **Pure 模型 log_samples**: 3/3 完整（GDN/RetNet/HGRN2，各 127MB）
- **H3-1 模型 log_samples**: 2/3 — RetNet 和 HGRN2 存在，**GDN h3-1 缺失**（只有 14K 的聚合 results，无 per-example 数据）
- **分析结果**: 完整，5153 examples 覆盖 LAMBADA 全集。但 `lambada_per_example.csv` 中 GDN 用的是 **h12-1**（非 h3-1）做 hybrid baseline，可能正是因为 h3-1 log_samples 缺失
- **统计结论不变**: 三个 arch 的 helped vs hurt perplexity 差异均不显著（p=0.21/0.66/0.25）

如果要求三个 arch 统一用 h3-1 对比，需补跑 GDN h3-1 的 `--log_samples` eval。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_exp003-p2-data-check_20260520T022655"
}
```

</details>

---
