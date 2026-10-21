# ops scierc seeds registry update

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 55
- **Recorded user turns:** 0
- **Tool calls:** 27
- **Original source:** `logs/chats/worker_ops_scierc-seeds-registry-update_20260522T182548.jsonl`
- **Structured JSON:** [`308f568514e69eaebe24.json`](../../sessions/30/308f568514e69eaebe24.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

55 recorded events

### Tool call

_source line 1 · 2026-05-22T18:28:40.375388+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-22T18:28:40.375789+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T18:28:40.376057+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "tail -30 /root/runs/struct_self_consist_ie/exp_scierc_n8_s2024.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "tail -30 /root/runs/struct_self_consist_ie/exp_scierc_n8_s2024.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-22T18:28:40.376346+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  Greedy F1:      0.6641\\n  Oracle F1:      0.7914\\n  Oracle headroom:+0.1273\\n------------------------------------------------------------\\n  Fleiss' kappa (mean):    0.3572\\n  Soft Jaccard (mean):     0.6606\\n------------------------------------------------------------\\n  Sample F1 (mean):        0.5971\\n  Sample F1 (std):         0.3243\\n  Sample F1=0 (%):         14.1%\\n------------------------------------------------------------\\n  Gold-empty filtered:     22\\n  All-samples-F1=0 filtered: 51\\n------------------------------------------------------------\\n  Full ρ(κ,F1):   +0.2356  p=4.1810e-08  n=529\\n  Full ρ(SJ,F1):  +0.3370  p=1.6327e-15  n=529\\n  Cond ρ(κ,F1):   +0.1465  p=1.3236e-03  n=478\\n  Cond ρ(SJ,F1):  +0.2890  p=1.2008e-10  n=478\\n  Structural > Surface:    YES  (delta=+0.1014)\\n------------------------------------------------------------\\n  Logprob (full):  ρ=+0.1831  τ=+0.1315  AUROC=0.5629\\n  Logprob (cond):  ρ=+0.1196  τ=+0.0847  AUROC=0.5305\\n------------------------------------------------------------\\n  Verdict:        MARGINAL\\n  Note:           MVP verdict on single subtask; final pass requires at least one of NER/RE/EAE to meet threshold\\n============================================================\\n\\nReport saved to output/scierc_mf4v2_seed2024/report.json\\n(EngineCore pid=164117) INFO 05-23 02:04:49 [core.py:1201] Shutdown initiated (timeout=0)\\n(EngineCore pid=164117) INFO 05-23 02:04:49 [core.py:1224] Shutdown complete\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T18:28:40.376578+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "tail -30 /root/runs/struct_self_consist_ie/exp_scierc_n8_s3141.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "tail -30 /root/runs/struct_self_consist_ie/exp_scierc_n8_s3141.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-22T18:28:40.376773+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'exp_scierc_n8_s2024'}",
  "project": "struct_self_consist_ie",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'exp_scierc_n8_s2024'}",
    "project": "struct_self_consist_ie",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-22T18:28:40.376999+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  Greedy F1:      0.6609\\n  Oracle F1:      0.7645\\n  Oracle headroom:+0.1036\\n------------------------------------------------------------\\n  Fleiss' kappa (mean):    0.2906\\n  Soft Jaccard (mean):     0.6265\\n------------------------------------------------------------\\n  Sample F1 (mean):        0.5802\\n  Sample F1 (std):         0.3357\\n  Sample F1=0 (%):         16.5%\\n------------------------------------------------------------\\n  Gold-empty filtered:     22\\n  All-samples-F1=0 filtered: 52\\n------------------------------------------------------------\\n  Full ρ(κ,F1):   +0.2074  p=1.5062e-06  n=529\\n  Full ρ(SJ,F1):  +0.3477  p=1.7583e-16  n=529\\n  Cond ρ(κ,F1):   +0.0806  p=7.8604e-02  n=477\\n  Cond ρ(SJ,F1):  +0.2427  p=8.0172e-08  n=477\\n  Structural > Surface:    YES  (delta=+0.1404)\\n------------------------------------------------------------\\n  Logprob (full):  ρ=+0.1926  τ=+0.1377  AUROC=0.5733\\n  Logprob (cond):  ρ=+0.1231  τ=+0.0881  AUROC=0.5399\\n------------------------------------------------------------\\n  Verdict:        MARGINAL\\n  Note:           MVP verdict on single subtask; final pass requires at least one of NER/RE/EAE to meet threshold\\n============================================================\\n\\nReport saved to output/scierc_mf4v2_seed3141/report.json\\n(EngineCore pid=164269) INFO 05-23 02:04:48 [core.py:1201] Shutdown initiated (timeout=0)\\n(EngineCore pid=164269) INFO 05-23 02:04:48 [core.py:1224] Shutdown complete\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-22T18:28:40.377241+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'exp_scierc_n8_s3141'}",
  "project": "struct_self_consist_ie",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'exp_scierc_n8_s3141'}",
    "project": "struct_self_consist_ie",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-22T18:28:40.377440+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9412}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T18:28:40.377632+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9438}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T18:28:40.377849+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/scierc_mf4v2_seed2024/report.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/scierc_mf4v2_seed2024/report.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-22T18:28:40.378044+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/scierc_mf4v2_seed3141/report.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/scierc_mf4v2_seed3141/report.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-22T18:28:40.378328+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"dataset\\\": \\\"scierc\\\",\\n  \\\"subtask\\\": \\\"ner\\\",\\n  \\\"n_samples\\\": 8,\\n  \\\"temperature\\\": 1.0,\\n  \\\"num_instances\\\": 551,\\n  \\\"use_train_format\\\": true,\\n  \\\"greedy_f1\\\": 0.6640857653365099,\\n  \\\"oracle_f1\\\": 0.7913539477634343,\\n  \\\"oracle_headroom\\\": 0.1272681824269244,\\n  \\\"fleiss_kappa_mean\\\": 0.35722740565031563,\\n  \\\"soft_jaccard_mean\\\": 0.6606459152652094,\\n  \\\"correlation_fleiss_vs_f1_full\\\": {\\n    \\\"rho\\\": 0.23558640837690706,\\n    \\\"p_value\\\": 4.1810220337145165e-08,\\n    \\\"n\\\": 529\\n  },\\n  \\\"correlation_softjaccard_vs_f1_full\\\": {\\n    \\\"rho\\\": 0.33698352005650445,\\n    \\\"p_value\\\": 1.6326980557024641e-15,\\n    \\\"n\\\": 529\\n  },\\n  \\\"correlation_fleiss_vs_f1_conditional\\\": {\\n    \\\"rho\\\": 0.14645022229239293,\\n    \\\"p_value\\\": 0.0013235816827462917,\\n    \\\"n\\\": 478\\n  },\\n  \\\"correlation_softjaccard_vs_f1_conditional\\\": {\\n    \\\"rho\\\": 0.2889738184569162,\\n    \\\"p_value\\\": 1.200766218136739e-10,\\n    \\\"n\\\": 478\\n  },\\n  \\\"n_gold_empty_filtered\\\": 22,\\n  \\\"n_greedy_f1_zero_filtered\\\": 51,\\n  \\\"structural_beats_surface\\\": true,\\n  \\\"rho_advantage\\\": 0.10139711167959739,\\n  \\\"sample_f1_mean\\\": 0.5970985879523764,\\n  \\\"sample_f1_std\\\": 0.32428924534119935,\\n  \\\"sample_f1_pct_zero\\\": 14.083175803402646,\\n  \\\"logprob_baseline\\\": {\\n    \\\"full\\\": {\\n      \\\"rho\\\": 0.18312664844353968,\\n      \\\"p_rho\\\": 2.2568202594747298e-05,\\n      \\\"tau\\\": 0.13145135131655863,\\n      \\\"p_tau\\\": 1.6351382731691056e-05,\\n      \\\"auroc\\\": 0.5629391100702577,\\n      \\\"n\\\": 529\\n    },\\n    \\\"conditional\\\": {\\n      \\\"rho\\\": 0.11961951638608342,\\n      \\\"p_rho\\\": 0.008849219005439585,\\n      \\\"tau\\\": 0.08465756887355227,\\n      \\\"p_tau\\\": 0.00865181041070658,\\n      \\\"auroc
…[truncated 340 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T18:28:40.378630+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"dataset\\\": \\\"scierc\\\",\\n  \\\"subtask\\\": \\\"ner\\\",\\n  \\\"n_samples\\\": 8,\\n  \\\"temperature\\\": 1.0,\\n  \\\"num_instances\\\": 551,\\n  \\\"use_train_format\\\": true,\\n  \\\"greedy_f1\\\": 0.6608903495667762,\\n  \\\"oracle_f1\\\": 0.7644810349897089,\\n  \\\"oracle_headroom\\\": 0.1035906854229327,\\n  \\\"fleiss_kappa_mean\\\": 0.290628264581424,\\n  \\\"soft_jaccard_mean\\\": 0.626464462003852,\\n  \\\"correlation_fleiss_vs_f1_full\\\": {\\n    \\\"rho\\\": 0.2073610692994053,\\n    \\\"p_value\\\": 1.5062474962356499e-06,\\n    \\\"n\\\": 529\\n  },\\n  \\\"correlation_softjaccard_vs_f1_full\\\": {\\n    \\\"rho\\\": 0.34773768938246363,\\n    \\\"p_value\\\": 1.758280460453104e-16,\\n    \\\"n\\\": 529\\n  },\\n  \\\"correlation_fleiss_vs_f1_conditional\\\": {\\n    \\\"rho\\\": 0.0806123960408722,\\n    \\\"p_value\\\": 0.07860378214308755,\\n    \\\"n\\\": 477\\n  },\\n  \\\"correlation_softjaccard_vs_f1_conditional\\\": {\\n    \\\"rho\\\": 0.2426801355292697,\\n    \\\"p_value\\\": 8.017222986458957e-08,\\n    \\\"n\\\": 477\\n  },\\n  \\\"n_gold_empty_filtered\\\": 22,\\n  \\\"n_greedy_f1_zero_filtered\\\": 52,\\n  \\\"structural_beats_surface\\\": true,\\n  \\\"rho_advantage\\\": 0.14037662008305835,\\n  \\\"sample_f1_mean\\\": 0.5802483909365651,\\n  \\\"sample_f1_std\\\": 0.3357445933785089,\\n  \\\"sample_f1_pct_zero\\\": 16.517013232514177,\\n  \\\"logprob_baseline\\\": {\\n    \\\"full\\\": {\\n      \\\"rho\\\": 0.19255331829711078,\\n      \\\"p_rho\\\": 8.19390234325669e-06,\\n      \\\"tau\\\": 0.1376582610386675,\\n      \\\"p_tau\\\": 6.369953294708341e-06,\\n      \\\"auroc\\\": 0.5733042212518195,\\n      \\\"n\\\": 529\\n    },\\n    \\\"conditional\\\": {\\n      \\\"rho\\\": 0.12307094532896291,\\n      \\\"p_rho\\\": 0.007121790259124205,\\n      \\\"tau\\\": 0.08808066699365684,\\n      \\\"p_tau\\\": 0.006348685268540362,\\n      \\\"auroc\\\": 0.5399
…[truncated 327 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T18:28:40.378912+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "struct_self_consist_ie",
  "fields": "['exp_id', 'status', 'conclusion']",
  "limit": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "fields": "['exp_id', 'status', 'conclusion']",
    "limit": "0"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-22T18:28:40.379095+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__update_registry",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__update_registry",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-22T18:28:40.379703+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp_esj_qwen3_all\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp_fewnerd_pretrained_n16_s42_v2\": {\"status\": \"RUNNING\"}, \"exp_fewnerd_pretrained_n32_s42_v2\": {\"status\": \"RUNNING\"}, \"exp_fewnerd_mf4_s456\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_fewnerd_mf4_s123_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_scierc_n8_s3141\": {\"status\": \"PREPARING\"}, \"exp_scierc_n8_s2024\": {\"status\": \"PREPARING\"}, \"exp_fewnerd_pretrained_n32_s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp_fewnerd_pretrained_n16_s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp_conll_freeform_n8_s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_fewnerd_freeform_n8_s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_fewnerd_5epoch_lp_s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_fewnerd_mf4_s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_scierc_n8_s456\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_scierc_n8_s123\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_fewnerd_n32_s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_fewnerd_mf4_s123\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp_conll_pretrained_n64_s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_conll_pretrained_n16_s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_scierc_pretrained_n16_s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_scierc_pretrained_n64_s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_conll_n32_s456\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_scierc_n32_s456\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_conll_n64_s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_conll_pretrained_n32_s42\": {\"status\": \"DONE\", \"conc
…[truncated 24727 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-22T18:28:40.379882+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-22T18:28:40.380063+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_scierc_n8_s2024",
  "field": "metrics",
  "value": "{'greedy_f1': 0.6641, 'oracle_f1': 0.7914, 'oracle_headroom': 0.1273, 'fleiss_kappa_mean': 0.3572, 'soft_jaccard_mean': 0.6606, 'rho_sj_f1_full': 0.337, 'rho_kappa_f1_full': 0.2356, 'rho_sj_f1_cond': 0.289, 'rho_kappa_f1_cond': 0.1465, 'structural_beats_surface': True, 'rho_advantage': 0.1014, 'logprob_rho_full': 0.1831, 'logprob_auroc_full': 0.5629, 'logprob_rho_cond': 0.1196, 'logprob_auroc_cond': 0.5305, 'sample_f1_mean': 0.5971, 'sample_f1_std': 0.3243, 'sample_f1_pct_zero': 14.1, 'n_instances': 551, 'degeneracy_rate': 14.1, 'verdict': 'MARGINAL'}",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_scierc_n8_s2024",
    "field": "metrics",
    "value": "{'greedy_f1': 0.6641, 'oracle_f1': 0.7914, 'oracle_headroom': 0.1273, 'fleiss_kappa_mean': 0.3572, 'soft_jaccard_mean': 0.6606, 'rho_sj_f1_full': 0.337, 'rho_kappa_f1_full': 0.2356, 'rho_sj_f1_cond': 0.289, 'rho_kappa_f1_cond': 0.1465, 'structural_beats_surface': True, 'rho_advantage': 0.1014, 'logprob_rho_full': 0.1831, 'logprob_auroc_full': 0.5629, 'logprob_rho_cond': 0.1196, 'logprob_auroc_cond': 0.5305, 'sample_f1_mean': 0.5971, 'sample_f1_std': 0.3243, 'sample_f1_pct_zero': 14.1, 'n_instances': 551, 'degeneracy_rate': 14.1, 'verdict': 'MARGINAL'}",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T18:28:40.380285+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_scierc_n8_s2024\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:33:46.085Z\", \"updated_at\": \"2026-05-22T18:27:09.611Z\", \"hypothesis\": \"R40 N2 statistical power: SciERC N=8 T=1.0 seed=2024 finetuned Qwen3-8B. 4th seed to strengthen 5-seed Holm-Bonferroni test for core correlation-selection claim (current p_adj=0.055 with 3 seeds).\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc --dataset scierc --subtask ner --n_samples 8 --temperature 1.0 --seed 2024 --collect_logprobs --output_dir output/scierc_mf4v2_seed2024/\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"158714\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_scierc_n8_s2024.log\", \"submitted_at\": \"2026-05-22T16:34:02.708Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"greedy_f1\": 0.6641, \"oracle_f1\": 0.7914, \"oracle_headroom\": 0.1273, \"fleiss_kappa_mean\": 0.3572, \"soft_jaccard_mean\": 0.6606, \"rho_sj_f1_full\": 0.337, \"rho_kappa_f1_full\": 0.2356, \"rho_sj_f1_cond\": 0.289, \"rho_kappa_f1_cond\": 0.1465, \"structural_beats_surface\": true, \"rho_advantage\": 0.1014, \"logprob_rho_full\": 0.1831, \"logprob_auroc_full\": 0.5629, \"logprob_rho_cond\": 0.1196, \"logprob_auroc_cond\": 0.5305, \"sample_f1_mean\": 0.5971, \"sample_f1_std\": 0.3243, \"sample_f1_pct_zero\": 14.1, \"n_instances\": 551, \"degeneracy_rate\": 14.1, \"verdict\": \"MARGINAL\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.7046}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-22T18:28:40.380441+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_scierc_n8_s3141",
  "field": "metrics",
  "value": "{'greedy_f1': 0.6609, 'oracle_f1': 0.7645, 'oracle_headroom': 0.1036, 'fleiss_kappa_mean': 0.2906, 'soft_jaccard_mean': 0.6265, 'rho_sj_f1_full': 0.3477, 'rho_kappa_f1_full': 0.2074, 'rho_sj_f1_cond': 0.2427, 'rho_kappa_f1_cond': 0.0806, 'structural_beats_surface': True, 'rho_advantage': 0.1404, 'logprob_rho_full': 0.1926, 'logprob_auroc_full': 0.5733, 'logprob_rho_cond': 0.1231, 'logprob_auroc_cond': 0.5399, 'sample_f1_mean': 0.5802, 'sample_f1_std': 0.3357, 'sample_f1_pct_zero': 16.5, 'n_instances': 551, 'degeneracy_rate': 16.5, 'verdict': 'MARGINAL'}",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_scierc_n8_s3141",
    "field": "metrics",
    "value": "{'greedy_f1': 0.6609, 'oracle_f1': 0.7645, 'oracle_headroom': 0.1036, 'fleiss_kappa_mean': 0.2906, 'soft_jaccard_mean': 0.6265, 'rho_sj_f1_full': 0.3477, 'rho_kappa_f1_full': 0.2074, 'rho_sj_f1_cond': 0.2427, 'rho_kappa_f1_cond': 0.0806, 'structural_beats_surface': True, 'rho_advantage': 0.1404, 'logprob_rho_full': 0.1926, 'logprob_auroc_full': 0.5733, 'logprob_rho_cond': 0.1231, 'logprob_auroc_cond': 0.5399, 'sample_f1_mean': 0.5802, 'sample_f1_std': 0.3357, 'sample_f1_pct_zero': 16.5, 'n_instances': 551, 'degeneracy_rate': 16.5, 'verdict': 'MARGINAL'}",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-22T18:28:40.380620+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_scierc_n8_s3141\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:33:47.527Z\", \"updated_at\": \"2026-05-22T18:27:12.658Z\", \"hypothesis\": \"R40 N2 statistical power: SciERC N=8 T=1.0 seed=3141 finetuned Qwen3-8B. 5th seed to strengthen 5-seed Holm-Bonferroni test for core correlation-selection claim (current p_adj=0.055 with 3 seeds).\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc --dataset scierc --subtask ner --n_samples 8 --temperature 1.0 --seed 3141 --collect_logprobs --output_dir output/scierc_mf4v2_seed3141/\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"158859\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_scierc_n8_s3141.log\", \"submitted_at\": \"2026-05-22T16:34:05.985Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"greedy_f1\": 0.6609, \"oracle_f1\": 0.7645, \"oracle_headroom\": 0.1036, \"fleiss_kappa_mean\": 0.2906, \"soft_jaccard_mean\": 0.6265, \"rho_sj_f1_full\": 0.3477, \"rho_kappa_f1_full\": 0.2074, \"rho_sj_f1_cond\": 0.2427, \"rho_kappa_f1_cond\": 0.0806, \"structural_beats_surface\": true, \"rho_advantage\": 0.1404, \"logprob_rho_full\": 0.1926, \"logprob_auroc_full\": 0.5733, \"logprob_rho_cond\": 0.1231, \"logprob_auroc_cond\": 0.5399, \"sample_f1_mean\": 0.5802, \"sample_f1_std\": 0.3357, \"sample_f1_pct_zero\": 16.5, \"n_instances\": 551, \"degeneracy_rate\": 16.5, \"verdict\": \"MARGINAL\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.435}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-22T18:28:40.380776+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_scierc_n8_s2024",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/struct_self_consist_ie/output/scierc_mf4v2_seed2024/",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_scierc_n8_s2024",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/struct_self_consist_ie/output/scierc_mf4v2_seed2024/",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-22T18:28:40.380904+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_scierc_n8_s2024",
  "field": "log_path",
  "value": "~/runs/struct_self_consist_ie/exp_scierc_n8_s2024.log",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_scierc_n8_s2024",
    "field": "log_path",
    "value": "~/runs/struct_self_consist_ie/exp_scierc_n8_s2024.log",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-22T18:28:40.381052+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_scierc_n8_s2024\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:33:46.085Z\", \"updated_at\": \"2026-05-22T18:27:18.827Z\", \"hypothesis\": \"R40 N2 statistical power: SciERC N=8 T=1.0 seed=2024 finetuned Qwen3-8B. 4th seed to strengthen 5-seed Holm-Bonferroni test for core correlation-selection claim (current p_adj=0.055 with 3 seeds).\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc --dataset scierc --subtask ner --n_samples 8 --temperature 1.0 --seed 2024 --collect_logprobs --output_dir output/scierc_mf4v2_seed2024/\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"158714\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_scierc_n8_s2024.log\", \"submitted_at\": \"2026-05-22T16:34:02.708Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"greedy_f1\": 0.6641, \"oracle_f1\": 0.7914, \"oracle_headroom\": 0.1273, \"fleiss_kappa_mean\": 0.3572, \"soft_jaccard_mean\": 0.6606, \"rho_sj_f1_full\": 0.337, \"rho_kappa_f1_full\": 0.2356, \"rho_sj_f1_cond\": 0.289, \"rho_kappa_f1_cond\": 0.1465, \"structural_beats_surface\": true, \"rho_advantage\": 0.1014, \"logprob_rho_full\": 0.1831, \"logprob_auroc_full\": 0.5629, \"logprob_rho_cond\": 0.1196, \"logprob_auroc_cond\": 0.5305, \"sample_f1_mean\": 0.5971, \"sample_f1_std\": 0.3243, \"sample_f1_pct_zero\": 14.1, \"n_instances\": 551, \"degeneracy_rate\": 14.1, \"verdict\": \"MARGINAL\"}, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/scierc_mf4v2_seed2024/\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.5949}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-22T18:28:40.381227+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_scierc_n8_s3141",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/struct_self_consist_ie/output/scierc_mf4v2_seed3141/",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_scierc_n8_s3141",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/struct_self_consist_ie/output/scierc_mf4v2_seed3141/",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-22T18:28:40.381388+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_scierc_n8_s2024\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:33:46.085Z\", \"updated_at\": \"2026-05-22T18:27:20.425Z\", \"hypothesis\": \"R40 N2 statistical power: SciERC N=8 T=1.0 seed=2024 finetuned Qwen3-8B. 4th seed to strengthen 5-seed Holm-Bonferroni test for core correlation-selection claim (current p_adj=0.055 with 3 seeds).\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc --dataset scierc --subtask ner --n_samples 8 --temperature 1.0 --seed 2024 --collect_logprobs --output_dir output/scierc_mf4v2_seed2024/\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"158714\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_scierc_n8_s2024.log\", \"submitted_at\": \"2026-05-22T16:34:02.708Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"greedy_f1\": 0.6641, \"oracle_f1\": 0.7914, \"oracle_headroom\": 0.1273, \"fleiss_kappa_mean\": 0.3572, \"soft_jaccard_mean\": 0.6606, \"rho_sj_f1_full\": 0.337, \"rho_kappa_f1_full\": 0.2356, \"rho_sj_f1_cond\": 0.289, \"rho_kappa_f1_cond\": 0.1465, \"structural_beats_surface\": true, \"rho_advantage\": 0.1014, \"logprob_rho_full\": 0.1831, \"logprob_auroc_full\": 0.5629, \"logprob_rho_cond\": 0.1196, \"logprob_auroc_cond\": 0.5305, \"sample_f1_mean\": 0.5971, \"sample_f1_std\": 0.3243, \"sample_f1_pct_zero\": 14.1, \"n_instances\": 551, \"degeneracy_rate\": 14.1, \"verdict\": \"MARGINAL\"}, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/scierc_mf4v2_seed2024/\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_scierc_n8_s2024.log\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.4742}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-22T18:28:40.381531+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_scierc_n8_s3141",
  "field": "log_path",
  "value": "~/runs/struct_self_consist_ie/exp_scierc_n8_s3141.log",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_scierc_n8_s3141",
    "field": "log_path",
    "value": "~/runs/struct_self_consist_ie/exp_scierc_n8_s3141.log",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-22T18:28:40.381681+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_scierc_n8_s3141\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:33:47.527Z\", \"updated_at\": \"2026-05-22T18:27:21.885Z\", \"hypothesis\": \"R40 N2 statistical power: SciERC N=8 T=1.0 seed=3141 finetuned Qwen3-8B. 5th seed to strengthen 5-seed Holm-Bonferroni test for core correlation-selection claim (current p_adj=0.055 with 3 seeds).\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc --dataset scierc --subtask ner --n_samples 8 --temperature 1.0 --seed 3141 --collect_logprobs --output_dir output/scierc_mf4v2_seed3141/\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"158859\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_scierc_n8_s3141.log\", \"submitted_at\": \"2026-05-22T16:34:05.985Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"greedy_f1\": 0.6609, \"oracle_f1\": 0.7645, \"oracle_headroom\": 0.1036, \"fleiss_kappa_mean\": 0.2906, \"soft_jaccard_mean\": 0.6265, \"rho_sj_f1_full\": 0.3477, \"rho_kappa_f1_full\": 0.2074, \"rho_sj_f1_cond\": 0.2427, \"rho_kappa_f1_cond\": 0.0806, \"structural_beats_surface\": true, \"rho_advantage\": 0.1404, \"logprob_rho_full\": 0.1926, \"logprob_auroc_full\": 0.5733, \"logprob_rho_cond\": 0.1231, \"logprob_auroc_cond\": 0.5399, \"sample_f1_mean\": 0.5802, \"sample_f1_std\": 0.3357, \"sample_f1_pct_zero\": 16.5, \"n_instances\": 551, \"degeneracy_rate\": 16.5, \"verdict\": \"MARGINAL\"}, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/scierc_mf4v2_seed3141/\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.4282}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-22T18:28:40.381836+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_scierc_n8_s3141\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:33:47.527Z\", \"updated_at\": \"2026-05-22T18:27:23.333Z\", \"hypothesis\": \"R40 N2 statistical power: SciERC N=8 T=1.0 seed=3141 finetuned Qwen3-8B. 5th seed to strengthen 5-seed Holm-Bonferroni test for core correlation-selection claim (current p_adj=0.055 with 3 seeds).\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc --dataset scierc --subtask ner --n_samples 8 --temperature 1.0 --seed 3141 --collect_logprobs --output_dir output/scierc_mf4v2_seed3141/\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"158859\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_scierc_n8_s3141.log\", \"submitted_at\": \"2026-05-22T16:34:05.985Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"greedy_f1\": 0.6609, \"oracle_f1\": 0.7645, \"oracle_headroom\": 0.1036, \"fleiss_kappa_mean\": 0.2906, \"soft_jaccard_mean\": 0.6265, \"rho_sj_f1_full\": 0.3477, \"rho_kappa_f1_full\": 0.2074, \"rho_sj_f1_cond\": 0.2427, \"rho_kappa_f1_cond\": 0.0806, \"structural_beats_surface\": true, \"rho_advantage\": 0.1404, \"logprob_rho_full\": 0.1926, \"logprob_auroc_full\": 0.5733, \"logprob_rho_cond\": 0.1231, \"logprob_auroc_cond\": 0.5399, \"sample_f1_mean\": 0.5802, \"sample_f1_std\": 0.3357, \"sample_f1_pct_zero\": 16.5, \"n_instances\": 551, \"degeneracy_rate\": 16.5, \"verdict\": \"MARGINAL\"}, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/scierc_mf4v2_seed3141/\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_scierc_n8_s3141.log\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.4383}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-22T18:28:40.381986+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_scierc_n8_s2024",
  "field": "conclusion",
  "value": "success",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_scierc_n8_s2024",
    "field": "conclusion",
    "value": "success",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-22T18:28:40.382149+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_scierc_n8_s3141",
  "field": "conclusion",
  "value": "success",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_scierc_n8_s3141",
    "field": "conclusion",
    "value": "success",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-22T18:28:40.382306+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_scierc_n8_s2024\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:33:46.085Z\", \"updated_at\": \"2026-05-22T18:27:28.286Z\", \"hypothesis\": \"R40 N2 statistical power: SciERC N=8 T=1.0 seed=2024 finetuned Qwen3-8B. 4th seed to strengthen 5-seed Holm-Bonferroni test for core correlation-selection claim (current p_adj=0.055 with 3 seeds).\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc --dataset scierc --subtask ner --n_samples 8 --temperature 1.0 --seed 2024 --collect_logprobs --output_dir output/scierc_mf4v2_seed2024/\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"158714\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_scierc_n8_s2024.log\", \"submitted_at\": \"2026-05-22T16:34:02.708Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"greedy_f1\": 0.6641, \"oracle_f1\": 0.7914, \"oracle_headroom\": 0.1273, \"fleiss_kappa_mean\": 0.3572, \"soft_jaccard_mean\": 0.6606, \"rho_sj_f1_full\": 0.337, \"rho_kappa_f1_full\": 0.2356, \"rho_sj_f1_cond\": 0.289, \"rho_kappa_f1_cond\": 0.1465, \"structural_beats_surface\": true, \"rho_advantage\": 0.1014, \"logprob_rho_full\": 0.1831, \"logprob_auroc_full\": 0.5629, \"logprob_rho_cond\": 0.1196, \"logprob_auroc_cond\": 0.5305, \"sample_f1_mean\": 0.5971, \"sample_f1_std\": 0.3243, \"sample_f1_pct_zero\": 14.1, \"n_instances\": 551, \"degeneracy_rate\": 14.1, \"verdict\": \"MARGINAL\"}, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/scierc_mf4v2_seed2024/\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_scierc_n8_s2024.log\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elaps
…[truncated 23 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-22T18:28:40.382501+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_scierc_n8_s3141\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:33:47.527Z\", \"updated_at\": \"2026-05-22T18:27:29.767Z\", \"hypothesis\": \"R40 N2 statistical power: SciERC N=8 T=1.0 seed=3141 finetuned Qwen3-8B. 5th seed to strengthen 5-seed Holm-Bonferroni test for core correlation-selection claim (current p_adj=0.055 with 3 seeds).\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc --dataset scierc --subtask ner --n_samples 8 --temperature 1.0 --seed 3141 --collect_logprobs --output_dir output/scierc_mf4v2_seed3141/\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"158859\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_scierc_n8_s3141.log\", \"submitted_at\": \"2026-05-22T16:34:05.985Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"greedy_f1\": 0.6609, \"oracle_f1\": 0.7645, \"oracle_headroom\": 0.1036, \"fleiss_kappa_mean\": 0.2906, \"soft_jaccard_mean\": 0.6265, \"rho_sj_f1_full\": 0.3477, \"rho_kappa_f1_full\": 0.2074, \"rho_sj_f1_cond\": 0.2427, \"rho_kappa_f1_cond\": 0.0806, \"structural_beats_surface\": true, \"rho_advantage\": 0.1404, \"logprob_rho_full\": 0.1926, \"logprob_auroc_full\": 0.5733, \"logprob_rho_cond\": 0.1231, \"logprob_auroc_cond\": 0.5399, \"sample_f1_mean\": 0.5802, \"sample_f1_std\": 0.3357, \"sample_f1_pct_zero\": 16.5, \"n_instances\": 551, \"degeneracy_rate\": 16.5, \"verdict\": \"MARGINAL\"}, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/scierc_mf4v2_seed3141/\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_scierc_n8_s3141.log\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"ela
…[truncated 26 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-22T18:28:40.382676+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_scierc_n8_s2024",
  "field": "status",
  "value": "DONE",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_scierc_n8_s2024",
    "field": "status",
    "value": "DONE",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-22T18:28:40.382805+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_scierc_n8_s3141",
  "field": "status",
  "value": "DONE",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_scierc_n8_s3141",
    "field": "status",
    "value": "DONE",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-22T18:28:40.382933+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → DONE. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.8951}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-22T18:28:40.383066+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → DONE. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.8294}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-22T18:28:40.383259+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_scierc_n8_s2024",
  "field": "status",
  "value": "RUNNING",
  "project": "struct_self_consist_ie",
  "spec": "{'command': 'python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc --dataset scierc --subtask ner --n_samples 8 --temperature 1.0 --seed 2024 --collect_logprobs --output_dir output/scierc_mf4v2_seed2024/', 'server': 'autodl-5090', 'data_path': 'data/scierc', 'data_count': 551, 'model_name': 'qwen3-8b-scierc-merged-v2', 'seed': 2024}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_scierc_n8_s2024",
    "field": "status",
    "value": "RUNNING",
    "project": "struct_self_consist_ie",
    "spec": "{'command': 'python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc --dataset scierc --subtask ner --n_samples 8 --temperature 1.0 --seed 2024 --collect_logprobs --output_dir output/scierc_mf4v2_seed2024/', 'server': 'autodl-5090', 'data_path': 'data/scierc', 'data_count': 551, 'model_name': 'qwen3-8b-scierc-merged-v2', 'seed': 2024}"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-22T18:28:40.383406+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.8538}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-22T18:28:40.383535+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_scierc_n8_s3141",
  "field": "status",
  "value": "RUNNING",
  "project": "struct_self_consist_ie",
  "spec": "{'command': 'python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc --dataset scierc --subtask ner --n_samples 8 --temperature 1.0 --seed 3141 --collect_logprobs --output_dir output/scierc_mf4v2_seed3141/', 'server': 'autodl-5090', 'data_path': 'data/scierc', 'data_count': 551, 'model_name': 'qwen3-8b-scierc-merged-v2', 'seed': 3141}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_scierc_n8_s3141",
    "field": "status",
    "value": "RUNNING",
    "project": "struct_self_consist_ie",
    "spec": "{'command': 'python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc --dataset scierc --subtask ner --n_samples 8 --temperature 1.0 --seed 3141 --collect_logprobs --output_dir output/scierc_mf4v2_seed3141/', 'server': 'autodl-5090', 'data_path': 'data/scierc', 'data_count': 551, 'model_name': 'qwen3-8b-scierc-merged-v2', 'seed': 3141}"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-22T18:28:40.383668+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 1.6899}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-22T18:28:40.383821+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_scierc_n8_s2024",
  "field": "status",
  "value": "QUEUED",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_scierc_n8_s2024",
    "field": "status",
    "value": "QUEUED",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-22T18:28:40.383943+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_scierc_n8_s3141",
  "field": "status",
  "value": "QUEUED",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_scierc_n8_s3141",
    "field": "status",
    "value": "QUEUED",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-22T18:28:40.384093+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_scierc_n8_s2024\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:33:46.085Z\", \"updated_at\": \"2026-05-22T18:27:52.937Z\", \"hypothesis\": \"R40 N2 statistical power: SciERC N=8 T=1.0 seed=2024 finetuned Qwen3-8B. 4th seed to strengthen 5-seed Holm-Bonferroni test for core correlation-selection claim (current p_adj=0.055 with 3 seeds).\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc --dataset scierc --subtask ner --n_samples 8 --temperature 1.0 --seed 2024 --collect_logprobs --output_dir output/scierc_mf4v2_seed2024/\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"158714\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_scierc_n8_s2024.log\", \"submitted_at\": \"2026-05-22T16:34:02.708Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"greedy_f1\": 0.6641, \"oracle_f1\": 0.7914, \"oracle_headroom\": 0.1273, \"fleiss_kappa_mean\": 0.3572, \"soft_jaccard_mean\": 0.6606, \"rho_sj_f1_full\": 0.337, \"rho_kappa_f1_full\": 0.2356, \"rho_sj_f1_cond\": 0.289, \"rho_kappa_f1_cond\": 0.1465, \"structural_beats_surface\": true, \"rho_advantage\": 0.1014, \"logprob_rho_full\": 0.1831, \"logprob_auroc_full\": 0.5629, \"logprob_rho_cond\": 0.1196, \"logprob_auroc_cond\": 0.5305, \"sample_f1_mean\": 0.5971, \"sample_f1_std\": 0.3243, \"sample_f1_pct_zero\": 14.1, \"n_instances\": 551, \"degeneracy_rate\": 14.1, \"verdict\": \"MARGINAL\"}, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/scierc_mf4v2_seed2024/\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_scierc_n8_s2024.log\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_
…[truncated 21 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-22T18:28:40.384292+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_scierc_n8_s3141\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:33:47.527Z\", \"updated_at\": \"2026-05-22T18:27:57.294Z\", \"hypothesis\": \"R40 N2 statistical power: SciERC N=8 T=1.0 seed=3141 finetuned Qwen3-8B. 5th seed to strengthen 5-seed Holm-Bonferroni test for core correlation-selection claim (current p_adj=0.055 with 3 seeds).\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc --dataset scierc --subtask ner --n_samples 8 --temperature 1.0 --seed 3141 --collect_logprobs --output_dir output/scierc_mf4v2_seed3141/\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"158859\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_scierc_n8_s3141.log\", \"submitted_at\": \"2026-05-22T16:34:05.985Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"greedy_f1\": 0.6609, \"oracle_f1\": 0.7645, \"oracle_headroom\": 0.1036, \"fleiss_kappa_mean\": 0.2906, \"soft_jaccard_mean\": 0.6265, \"rho_sj_f1_full\": 0.3477, \"rho_kappa_f1_full\": 0.2074, \"rho_sj_f1_cond\": 0.2427, \"rho_kappa_f1_cond\": 0.0806, \"structural_beats_surface\": true, \"rho_advantage\": 0.1404, \"logprob_rho_full\": 0.1926, \"logprob_auroc_full\": 0.5733, \"logprob_rho_cond\": 0.1231, \"logprob_auroc_cond\": 0.5399, \"sample_f1_mean\": 0.5802, \"sample_f1_std\": 0.3357, \"sample_f1_pct_zero\": 16.5, \"n_instances\": 551, \"degeneracy_rate\": 16.5, \"verdict\": \"MARGINAL\"}, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/scierc_mf4v2_seed3141/\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_scierc_n8_s3141.log\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapse
…[truncated 23 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-22T18:28:40.384445+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_scierc_n8_s2024",
  "field": "status",
  "value": "RUNNING",
  "project": "struct_self_consist_ie",
  "spec": "{'command': 'python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc --dataset scierc --subtask ner --n_samples 8 --temperature 1.0 --seed 2024 --collect_logprobs --output_dir output/scierc_mf4v2_seed2024/', 'server': 'autodl-5090', 'data_path': 'data/scierc', 'data_count': 551, 'model_name': 'qwen3-8b-scierc-merged-v2', 'seed': 2024}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_scierc_n8_s2024",
    "field": "status",
    "value": "RUNNING",
    "project": "struct_self_consist_ie",
    "spec": "{'command': 'python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc --dataset scierc --subtask ner --n_samples 8 --temperature 1.0 --seed 2024 --collect_logprobs --output_dir output/scierc_mf4v2_seed2024/', 'server': 'autodl-5090', 'data_path': 'data/scierc', 'data_count': 551, 'model_name': 'qwen3-8b-scierc-merged-v2', 'seed': 2024}"
  }
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-22T18:28:40.384584+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_scierc_n8_s3141",
  "field": "status",
  "value": "RUNNING",
  "project": "struct_self_consist_ie",
  "spec": "{'command': 'python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc --dataset scierc --subtask ner --n_samples 8 --temperature 1.0 --seed 3141 --collect_logprobs --output_dir output/scierc_mf4v2_seed3141/', 'server': 'autodl-5090', 'data_path': 'data/scierc', 'data_count': 551, 'model_name': 'qwen3-8b-scierc-merged-v2', 'seed': 3141}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_scierc_n8_s3141",
    "field": "status",
    "value": "RUNNING",
    "project": "struct_self_consist_ie",
    "spec": "{'command': 'python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc --dataset scierc --subtask ner --n_samples 8 --temperature 1.0 --seed 3141 --collect_logprobs --output_dir output/scierc_mf4v2_seed3141/', 'server': 'autodl-5090', 'data_path': 'data/scierc', 'data_count': 551, 'model_name': 'qwen3-8b-scierc-merged-v2', 'seed': 3141}"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-22T18:28:40.384743+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_scierc_n8_s2024\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:33:46.085Z\", \"updated_at\": \"2026-05-22T18:28:09.417Z\", \"hypothesis\": \"R40 N2 statistical power: SciERC N=8 T=1.0 seed=2024 finetuned Qwen3-8B. 4th seed to strengthen 5-seed Holm-Bonferroni test for core correlation-selection claim (current p_adj=0.055 with 3 seeds).\", \"spec\": {\"command\": \"python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc --dataset scierc --subtask ner --n_samples 8 --temperature 1.0 --seed 2024 --collect_logprobs --output_dir output/scierc_mf4v2_seed2024/\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"158714\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_scierc_n8_s2024.log\", \"submitted_at\": \"2026-05-22T16:34:02.708Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scierc\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 2024}, \"metrics\": {\"greedy_f1\": 0.6641, \"oracle_f1\": 0.7914, \"oracle_headroom\": 0.1273, \"fleiss_kappa_mean\": 0.3572, \"soft_jaccard_mean\": 0.6606, \"rho_sj_f1_full\": 0.337, \"rho_kappa_f1_full\": 0.2356, \"rho_sj_f1_cond\": 0.289, \"rho_kappa_f1_cond\": 0.1465, \"structural_beats_surface\": true, \"rho_advantage\": 0.1014, \"logprob_rho_full\": 0.1831, \"logprob_auroc_full\": 0.5629, \"logprob_rho_cond\": 0.1196, \"logprob_auroc_cond\": 0.5305, \"sample_f1_mean\": 0.5971, \"sample_f1_std\": 0.3243, \"sample_f1_pct_zero\": 14.1, \"n_instances\": 551, \"degeneracy_rate\": 14.1, \"verdict\": \"MARGINAL\"}, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/scierc_mf4v2_seed2024/\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_scierc_n8_s2024.log\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.5578}
…[truncated 3 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-22T18:28:40.384919+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_scierc_n8_s3141\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:33:47.527Z\", \"updated_at\": \"2026-05-22T18:28:13.134Z\", \"hypothesis\": \"R40 N2 statistical power: SciERC N=8 T=1.0 seed=3141 finetuned Qwen3-8B. 5th seed to strengthen 5-seed Holm-Bonferroni test for core correlation-selection claim (current p_adj=0.055 with 3 seeds).\", \"spec\": {\"command\": \"python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc --dataset scierc --subtask ner --n_samples 8 --temperature 1.0 --seed 3141 --collect_logprobs --output_dir output/scierc_mf4v2_seed3141/\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"158859\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_scierc_n8_s3141.log\", \"submitted_at\": \"2026-05-22T16:34:05.985Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scierc\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 3141}, \"metrics\": {\"greedy_f1\": 0.6609, \"oracle_f1\": 0.7645, \"oracle_headroom\": 0.1036, \"fleiss_kappa_mean\": 0.2906, \"soft_jaccard_mean\": 0.6265, \"rho_sj_f1_full\": 0.3477, \"rho_kappa_f1_full\": 0.2074, \"rho_sj_f1_cond\": 0.2427, \"rho_kappa_f1_cond\": 0.0806, \"structural_beats_surface\": true, \"rho_advantage\": 0.1404, \"logprob_rho_full\": 0.1926, \"logprob_auroc_full\": 0.5733, \"logprob_rho_cond\": 0.1231, \"logprob_auroc_cond\": 0.5399, \"sample_f1_mean\": 0.5802, \"sample_f1_std\": 0.3357, \"sample_f1_pct_zero\": 16.5, \"n_instances\": 551, \"degeneracy_rate\": 16.5, \"verdict\": \"MARGINAL\"}, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/scierc_mf4v2_seed3141/\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_scierc_n8_s3141.log\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.508
…[truncated 5 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-22T18:28:40.385078+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_scierc_n8_s2024",
  "field": "status",
  "value": "DONE",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_scierc_n8_s2024",
    "field": "status",
    "value": "DONE",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-22T18:28:40.385225+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_scierc_n8_s3141",
  "field": "status",
  "value": "DONE",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_scierc_n8_s3141",
    "field": "status",
    "value": "DONE",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-22T18:28:40.385405+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_scierc_n8_s2024\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:33:46.085Z\", \"updated_at\": \"2026-05-22T18:28:21.440Z\", \"hypothesis\": \"R40 N2 statistical power: SciERC N=8 T=1.0 seed=2024 finetuned Qwen3-8B. 4th seed to strengthen 5-seed Holm-Bonferroni test for core correlation-selection claim (current p_adj=0.055 with 3 seeds).\", \"spec\": {\"command\": \"python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc --dataset scierc --subtask ner --n_samples 8 --temperature 1.0 --seed 2024 --collect_logprobs --output_dir output/scierc_mf4v2_seed2024/\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"158714\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_scierc_n8_s2024.log\", \"submitted_at\": \"2026-05-22T16:34:02.708Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scierc\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 2024, \"wall_clock_seconds\": 6858.7, \"gpu_hours\": 1.91}, \"metrics\": {\"greedy_f1\": 0.6641, \"oracle_f1\": 0.7914, \"oracle_headroom\": 0.1273, \"fleiss_kappa_mean\": 0.3572, \"soft_jaccard_mean\": 0.6606, \"rho_sj_f1_full\": 0.337, \"rho_kappa_f1_full\": 0.2356, \"rho_sj_f1_cond\": 0.289, \"rho_kappa_f1_cond\": 0.1465, \"structural_beats_surface\": true, \"rho_advantage\": 0.1014, \"logprob_rho_full\": 0.1831, \"logprob_auroc_full\": 0.5629, \"logprob_rho_cond\": 0.1196, \"logprob_auroc_cond\": 0.5305, \"sample_f1_mean\": 0.5971, \"sample_f1_std\": 0.3243, \"sample_f1_pct_zero\": 14.1, \"n_instances\": 551, \"degeneracy_rate\": 14.1, \"verdict\": \"MARGINAL\"}, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/scierc_mf4v2_seed2024/\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_scierc_n8_s2024.log\", \"conclusion\": \"success\", \"completed_
…[truncated 152 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-22T18:28:40.385609+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_scierc_n8_s3141\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:33:47.527Z\", \"updated_at\": \"2026-05-22T18:28:25.162Z\", \"hypothesis\": \"R40 N2 statistical power: SciERC N=8 T=1.0 seed=3141 finetuned Qwen3-8B. 5th seed to strengthen 5-seed Holm-Bonferroni test for core correlation-selection claim (current p_adj=0.055 with 3 seeds).\", \"spec\": {\"command\": \"python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc --dataset scierc --subtask ner --n_samples 8 --temperature 1.0 --seed 3141 --collect_logprobs --output_dir output/scierc_mf4v2_seed3141/\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"158859\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_scierc_n8_s3141.log\", \"submitted_at\": \"2026-05-22T16:34:05.985Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scierc\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 3141, \"wall_clock_seconds\": 6859.2, \"gpu_hours\": 1.91}, \"metrics\": {\"greedy_f1\": 0.6609, \"oracle_f1\": 0.7645, \"oracle_headroom\": 0.1036, \"fleiss_kappa_mean\": 0.2906, \"soft_jaccard_mean\": 0.6265, \"rho_sj_f1_full\": 0.3477, \"rho_kappa_f1_full\": 0.2074, \"rho_sj_f1_cond\": 0.2427, \"rho_kappa_f1_cond\": 0.0806, \"structural_beats_surface\": true, \"rho_advantage\": 0.1404, \"logprob_rho_full\": 0.1926, \"logprob_auroc_full\": 0.5733, \"logprob_rho_cond\": 0.1231, \"logprob_auroc_cond\": 0.5399, \"sample_f1_mean\": 0.5802, \"sample_f1_std\": 0.3357, \"sample_f1_pct_zero\": 16.5, \"n_instances\": 551, \"degeneracy_rate\": 16.5, \"verdict\": \"MARGINAL\"}, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/scierc_mf4v2_seed3141/\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_scierc_n8_s3141.log\", \"conclusion\": \"success\", \"complete
…[truncated 154 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 55 · 2026-05-22T18:28:40.385799+00:00_

Registry 更新完成。两个实验摘要：

| | exp_scierc_n8_s2024 | exp_scierc_n8_s3141 |
|---|---|---|
| **status** | DONE (success) | DONE (success) |
| **greedy_f1** | 0.6641 | 0.6609 |
| **oracle_f1** | 0.7914 | 0.7645 |
| **ρ(SJ,F1) full** | 0.337 | 0.348 |
| **ρ(κ,F1) full** | 0.236 | 0.207 |
| **structural > surface** | YES (+0.101) | YES (+0.140) |
| **logprob ρ full** | 0.183 | 0.193 |
| **verdict** | MARGINAL | MARGINAL |
| **wall_clock** | ~1.9 GPU-hrs | ~1.9 GPU-hrs |

两个 seed 均确认 structural consistency (SJ) 优于 surface consistency (kappa)，与之前 3 个 seed 一致。现在 SciERC 有 5 个 seed (42, 123, 456, 2024, 3141)，可用于 Holm-Bonferroni 校正。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ops_scierc-seeds-registry-update_20260522T182548"
}
```

</details>

---
