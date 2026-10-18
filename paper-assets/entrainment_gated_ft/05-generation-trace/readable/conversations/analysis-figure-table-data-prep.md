# analysis figure table data prep

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 61
- **Recorded user turns:** 0
- **Tool calls:** 30
- **Original source:** `logs/chats/worker_analysis_figure-table-data-prep_20260519T164223.jsonl`
- **Structured JSON:** [`532e26d2fea1a293d1f5.json`](../../sessions/53/532e26d2fea1a293d1f5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

61 recorded events

### Tool call

_source line 1 · 2026-05-19T16:45:32.421705+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__ssh_read_only",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__ssh_read_only",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T16:45:32.422029+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T16:45:32.422211+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "entrainment_gated_ft",
  "filters": "{'experiment_id': 'exp-001'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "entrainment_gated_ft",
    "filters": "{'experiment_id': 'exp-001'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T16:45:32.422358+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0364}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T16:45:32.422485+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "entrainment_gated_ft",
  "filters": "{'experiment_id': 'exp-003'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "entrainment_gated_ft",
    "filters": "{'experiment_id': 'exp-003'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T16:45:32.422613+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0345}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T16:45:32.422780+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "entrainment_gated_ft",
  "filters": "{'experiment_id': 'exp-003-p2'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "entrainment_gated_ft",
    "filters": "{'experiment_id': 'exp-003-p2'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T16:45:32.422907+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0417}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T16:45:32.423022+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "entrainment_gated_ft",
  "filters": "{'experiment_id': 'exp-008'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "entrainment_gated_ft",
    "filters": "{'experiment_id': 'exp-008'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T16:45:32.423139+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0377}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T16:45:32.423251+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "entrainment_gated_ft",
  "filters": "{'experiment_id': 'exp-010'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "entrainment_gated_ft",
    "filters": "{'experiment_id': 'exp-010'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T16:45:32.423383+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0351}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T16:45:32.423524+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "entrainment_gated_ft",
  "filters": "{'experiment_id': 'exp-011'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "entrainment_gated_ft",
    "filters": "{'experiment_id': 'exp-011'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T16:45:32.423658+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0734}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T16:45:32.423778+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "entrainment_gated_ft",
  "filters": "{'experiment_id': 'exp-011-xstorycloze'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "entrainment_gated_ft",
    "filters": "{'experiment_id': 'exp-011-xstorycloze'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T16:45:32.423893+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0428}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T16:45:32.424002+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "cat /root/entrainment_gated_ft/analysis/exp011_convergence_results.csv",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "cat /root/entrainment_gated_ft/analysis/exp011_convergence_results.csv",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-19T16:45:32.424115+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "cat /root/entrainment_gated_ft/analysis/xstorycloze_convergence_results.csv",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "cat /root/entrainment_gated_ft/analysis/xstorycloze_convergence_results.csv",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T16:45:32.424225+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "cat /root/entrainment_gated_ft/analysis/exp010_bridge_results.csv",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "cat /root/entrainment_gated_ft/analysis/exp010_bridge_results.csv",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T16:45:32.424352+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"benchmark,attention_ratio,GDN_acc,RetNet_acc,HGRN2_acc,cross_arch_std,Transformer_acc\\nboolq,0.0,0.5862385321100917,0.6128440366972477,0.5737003058103975,0.016321,0.6198776758409786\\nboolq,0.04,0.4896024464831804,0.6033639143730887,0.608868501529052,0.054971,0.6198776758409786\\nboolq,0.0769,0.6357798165137615,0.6048929663608563,0.608868501529052,0.013719,0.6198776758409786\\nboolq,0.1429,0.5703363914373089,0.6214067278287462,0.6168195718654435,0.02307,0.6198776758409786\\nboolq,0.25,0.6223241590214067,0.5804281345565749,0.6357798165137615,0.023571,0.6198776758409786\\ncopa,0.0,0.79,0.74,0.8,0.026247,0.77\\ncopa,0.04,0.75,0.79,0.77,0.01633,0.77\\ncopa,0.0769,0.8,0.76,0.79,0.016997,0.77\\ncopa,0.1429,0.75,0.76,0.79,0.016997,0.77\\ncopa,0.25,0.78,0.79,0.78,0.004714,0.77\\npiqa,0.0,0.7252448313384113,0.7263329706202394,0.7372143634385201,0.005404,0.736126224156692\\npiqa,0.04,0.7268770402611534,0.721436343852013,0.735582154515778,0.005826,0.736126224156692\\npiqa,0.0769,0.7263329706202394,0.7236126224156693,0.7383025027203483,0.006381,0.736126224156692\\npiqa,0.1429,0.7328618063112078,0.7274211099020674,0.7323177366702938,0.002447,0.736126224156692\\npiqa,0.25,0.7377584330794341,0.7323177366702938,0.7295973884657236,0.003393,0.736126224156692\\nsciq,0.0,0.917,0.903,0.896,0.008731,0.929\\nsciq,0.04,0.912,0.902,0.911,0.004497,0.929\\nsciq,0.0769,0.914,0.909,0.909,0.002357,0.929\\nsciq,0.1429,0.919,0.916,0.897,0.009741,0.929\\nsciq,0.25,0.903,0.913,0.921,0.007364,0.929\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.18}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-19T16:45:32.424492+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"attention_ratio,GDN_acc,RetNet_acc,HGRN2_acc,cross_arch_std,Transformer_acc\\r\\n0.0,0.7068166776968895,0.686962276637988,0.6949040370615487,0.008159383193870278,0.6737260092653872\\r\\n0.04,0.6975512905360688,0.6671078755790867,0.6882859033752482,0.012741697840894458,0.6737260092653872\\r\\n0.07692307692307693,0.685638649900728,0.6730641958967571,0.6968894771674388,0.009731632473025692,0.6737260092653872\\r\\n0.14285714285714285,0.6915949702183984,0.6790205162144275,0.6882859033752482,0.005322011066320267,0.6737260092653872\\r\\n0.25,0.6882859033752482,0.6796823295830576,0.6929185969556585,0.0054841398167465236,0.6737260092653872\\r\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-19T16:45:32.424622+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"variant,attention_ratio,cross_arch_std,mean_jaccard_helped,mean_jaccard_hurt,mean_net_asymmetry,jaccard_helped_GDN_vs_HGRN2,jaccard_hurt_GDN_vs_HGRN2,net_asymmetry_GDN_vs_HGRN2,jaccard_helped_GDN_vs_RetNet,jaccard_hurt_GDN_vs_RetNet,net_asymmetry_GDN_vs_RetNet,jaccard_helped_HGRN2_vs_RetNet,jaccard_hurt_HGRN2_vs_RetNet,net_asymmetry_HGRN2_vs_RetNet\\r\\npure,0.0000,0.024047126977057007,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan\\r\\nh24-1,0.0400,0.016238171620323174,0.09452342313036471,0.08733237965030449,0.012808072967203571,0.1004566210045662,0.07168458781362007,0.019212109450805356,0.08995327102803738,0.09507445589919816,0.0017465554046186688,0.09316037735849056,0.09523809523809523,0.017465554046186688\\r\\nh12-1,0.0769,0.013595712311665278,0.09508958868918442,0.08086978856885539,0.01888867326476486,0.09786276715410573,0.07043879907621248,0.028138948185522997,0.08658536585365853,0.08690869086908691,0.00019406171162429653,0.10082063305978899,0.08526187576126674,0.028333009897147293\\r\\nh6-1,0.1429,0.006055084765553574,0.0922297437493516,0.09879533906172999,0.03868296785044311,0.09953703703703703,0.08505997818974918,0.05802445177566466,0.09126984126984126,0.11597151576805696,0.01397244323694935,0.08588235294117647,0.09535452322738386,0.04405200853871531\\r\\nh3-1,0.2500,0.004942545182713789,0.10018204935668666,0.09281095910886135,0.03958858917135649,0.10021786492374728,0.08836206896551724,0.05938288375703474,0.09225092250922509,0.10337972166998012,0.01630118377644091,0.1080773606370876,0.08669108669108669,0.04308169998059383\\r\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-19T16:45:32.424796+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "entrainment_gated_ft",
  "limit": "20",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "entrainment_gated_ft",
    "limit": "20",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T16:45:32.425252+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp-004\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T16:41:10.744Z\", \"updated_at\": \"2026-05-19T16:41:30.535Z\", \"hypothesis\": \"Attention weight patterns in hybrid h3-1 models differ systematically between helped and hurt samples on LAMBADA, with cross-architecture attention pattern similarity lower than expected given aggregate convergence — providing mechanistic evidence for architecture-specific per-example effects (Claim 3)\", \"parent\": \"exp-003\", \"spec\": {\"command\": \"python extract_attention_weights.py (forward hooks on Q,K, manual softmax(QK^T/√d) with GQA expansion)\", \"server\": \"westb-48145\", \"data_path\": \"/root/entrainment_gated_ft/lm_eval_clean/lambada_openai per-example data\", \"data_count\": 5153, \"model_name\": \"GDN-h3-1, RetNet-h3-1, HGRN2-h3-1 (1.3B)\", \"seed\": 42, \"gpu\": \"cuda:0\", \"checkpoint_source\": \"Wang et al. pretrained weights\", \"eval_data\": \"lambada_openai (5153 examples)\"}}, \"exp-011\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T14:12:29.428Z\", \"updated_at\": \"2026-05-19T16:37:27.600Z\", \"hypothesis\": \"Cross-architecture variance on additional retrieval-dependent benchmarks (StoryCloze, BoolQ, COPA, PIQA, SciQ) decreases monotonically with attention ratio, providing a second statistically significant anchor (exact permutation p<0.05, two-tailed) beyond LAMBADA after Bonferroni correction\", \"parent\": \"exp-001\", \"spec\": {\"command\": \"bash /root/entrainment_gated_ft/run_exp011_batch.sh (nohup PID 474289)\", \"server\": \"westb-48145\", \"data_path\": \"/root/autodl-tmp/models_1.3b/ (16 models)\", \"data_count\": 16, \"model_name\": \"GDN/RetNet/HGRN2 x 5 ratios + Transformer baseline (1.3B)\", \"seed\": 0, \"eval_data\": \"boolq, copa, piqa, sciq (4 benchmarks x 16 models)\", \"gpu\": \"cuda:0 (RTX PRO 6000)\", \"checkpoint_source\": \"/root/autodl-tmp/models_1.3b/ (Wan
…[truncated 18865 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-19T16:45:32.425430+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "ls /root/entrainment_gated_ft/analysis/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "ls /root/entrainment_gated_ft/analysis/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-19T16:45:32.425559+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "find /root/entrainment_gated_ft -name \"registry*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "find /root/entrainment_gated_ft -name \"registry*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-19T16:45:32.425728+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"additional_benchmarks_convergence.py\\nall_benchmark_convergence_summary.json\\nconvergence_analysis.pdf\\nconvergence_analysis.png\\nconvergence_analysis.py\\ncross_scale_convergence.pdf\\ncross_scale_convergence.png\\ncross_scale_convergence.py\\ncross_scale_summary.csv\\nexp010_bridge_analysis.py\\nexp010_bridge_results.csv\\nexp010_bridge_summary.json\\nexp011_convergence_analysis.py\\nexp011_convergence_results.csv\\nexp011_convergence_summary.json\\nextract_attention_weights.py\\nfigures\\nfix_hgrn2_and_complete.py\\ngenerate_paper_data.py\\nlambada_attention_analysis.png\\nlambada_crossmodel_scatter.png\\nlambada_matched_comparison.pdf\\nlambada_matched_comparison.png\\nlambada_matched_comparison.py\\nlambada_matched_comparison.py.bak\\nlambada_matched_per_example.csv\\nlambada_per_example.csv\\nlambada_robustness_h6.pdf\\nlambada_robustness_h6.png\\nlambada_robustness_h6.py\\nlambada_three_arch_comparison.pdf\\nlambada_three_arch_comparison.png\\nlambada_three_arch_comparison.py\\nlogprob_analysis.py\\nlogprob_plots.py\\npaper_data\\nplot_decoupling.py\\nrobustness_results.csv\\nrobustness_results.csv.bak\\nrobustness_summary.md\\nrobustness_summary.md.bak\\nrobustness_supplement_gdn_excluded.csv\\nrobustness_supplement_summary.json\\nsample_characterization.pdf\\nsample_characterization.png\\nsample_characterization.py\\nsample_characterization_results.csv\\nsample_perplexity_analysis.py\\nsample_perplexity_dryrun.py\\nsample_perplexity_figure.pdf\\nsample_perplexity_figure.png\\nsample_perplexity_results.csv\\nsample_perplexity_summary.json\\nstatistical_robustness.py\\nstatistical_robustness.py.bak\\nstatistical_robustness_supplement.py\\ntask_specificity_analysis.py\\ntask_specificity_figure.pdf\\ntask_specificity_figure.png\\ntask_specificity_results.csv\\nwang_et_al_differentiation.md\\nxstorycloze_convergence_analysis.py\\nxstorycloze_convergence_results.csv\\n\", \"stderr\": \"\", \"return_code\
…[truncated 68 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-19T16:45:32.425884+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-19T16:45:32.426051+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "cat /root/entrainment_gated_ft/analysis/robustness_results.csv",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "cat /root/entrainment_gated_ft/analysis/robustness_results.csv",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-19T16:45:32.426175+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "cat /root/entrainment_gated_ft/analysis/task_specificity_results.csv",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "cat /root/entrainment_gated_ft/analysis/task_specificity_results.csv",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-19T16:45:32.426314+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"benchmark,spearman_rho,p_value_exact,monotone_decreasing,bonferroni_adj_p,bh_fdr_adj_p,boot_ci_lower,boot_ci_upper,rho_excl_gdn,p_excl_gdn_exact,mono_excl_gdn,cohen_d,cohen_d_ci_lo,cohen_d_ci_hi,eta_squared,omega_squared,std_attn0,std_attn1,std_attn2,std_attn4,std_attn8,std_nogdn_attn0,std_nogdn_attn1,std_nogdn_attn2,std_nogdn_attn4,std_nogdn_attn8\\nLAMBADA,-0.9999999999999999,0.016666666666666666,True,0.1,0.1,-0.9999999999999999,0.0,-0.7,0.23333333333333334,False,-0.2068944236207555,-1.8115034323354806,1.3977145850939696,0.08071590316015283,-0.2628356703887264,0.02404712697705703,0.016238171620323174,0.013595712311665278,0.006055084765553574,0.004942545182713789,0.016204152920628795,0.007471375897535437,0.0020376479720551344,0.005821851348728924,0.0053366970696681615\\nHellaSwag,0.3,0.6833333333333333,False,1.0,0.82,-0.8999999999999998,0.49999999999999994,0.49999999999999994,0.45,False,-0.06223569337755609,-1.6629563539532428,1.5384849671981307,0.06744149272612315,-0.2795154583257995,0.011684919531365781,0.008615212910147578,0.00946859081425128,0.009201244143823003,0.01183082679011367,0.009211312487552303,0.01020713005377416,0.008564031069508038,0.009808803027285373,0.012447719577773353\\nWinoGrande,0.09999999999999999,0.95,False,1.0,0.9499999999999998,-0.8999999999999998,0.3,0.3,0.6833333333333333,False,0.029443619762019427,-1.5709763872408922,1.629863626764931,0.015329960999343995,-0.3446057580764223,0.0067074710781278545,0.021181496667056418,0.009652163287473934,0.007597752737802509,0.007839865522626334,0.005919494869771114,0.01617995264404104,0.008287292817679592,0.006314127861089203,0.008681925808997626\\nARC-Easy,-0.7,0.23333333333333334,False,1.0,0.4666666666666666,-0.8999999999999998,0.0,-0.8999999999999998,0.08333333333333333,False,-0.561421070977342,-2.1929757438407664,1.0701336018860823,0.12114591993773265,-0.21178307052525108,0.010014909257898295,0.019452560645897617,0.016761201811228865,0.0045761
…[truncated 1108 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-19T16:45:32.426453+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "cat /root/entrainment_gated_ft/analysis/robustness_supplement_gdn_excluded.csv",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "cat /root/entrainment_gated_ft/analysis/robustness_supplement_gdn_excluded.csv",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-19T16:45:32.426593+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"benchmark,taxonomy_category,std_pure_1.3B,std_pure_340M,std_h24-1_1.3B,std_h24-1_340M,std_h12-1_1.3B,std_h12-1_340M,std_h6-1_1.3B,std_h6-1_340M,std_h3-1_1.3B,std_h3-1_340M,spearman_rho_1.3B,p_value_1.3B,significant_1.3B,spearman_rho_340M,p_value_340M,significant_340M\\nLAMBADA,Retrieval-dependent,0.02404712697705703,0.024555261611474578,0.016238171620323174,0.010936543996588673,0.013595712311665278,0.01732555602405885,0.006055084765553574,0.010812254492773449,0.004942545182713789,0.015053096764030554,-0.9999999999999999,0.016666666666666666,True,-0.49999999999999994,0.45,False\\nHellaSwag,Reasoning-dependent,0.011684919531365781,0.008730316189724646,0.008615212910147578,0.02284108266114241,0.00946859081425128,0.00977266404295068,0.009201244143823003,0.01114673344940407,0.01183082679011367,0.01328594637040945,0.3,0.6833333333333333,False,0.39999999999999997,0.5166666666666667,False\\nARC-C,Reasoning-dependent,0.009577621297202906,0.013693291373391028,0.007705470525679222,0.01467973595058468,0.007673912152009124,0.011510868228013702,0.012565825958119756,0.011110366885451991,0.013242829040754071,0.008821423446684193,0.6,0.35,False,-0.8999999999999998,0.08333333333333333,False\\nWinoGrande,Reasoning-dependent,0.0067074710781278545,0.0042908462063404335,0.021181496667056418,0.003549260079776889,0.009652163287473934,0.010549822497113106,0.007597752737802509,0.0054045352760258136,0.007839865522626334,0.013149170217942466,0.09999999999999999,0.95,False,0.7999999999999999,0.13333333333333333,False\\nARC-E,Mixed,0.010014909257898295,0.031533528980082624,0.019452560645897617,0.025552372452290466,0.016761201811228865,0.03793382541847497,0.004576180255415263,0.030653679561850628,0.001301012695776599,0.020911480929206045,-0.7,0.23333333333333334,False,-0.49999999999999994,0.45,False\\nMMLU,Mixed,0.009200975872321134,0.007100334138115536,0.005255878164789419,0.004196648355958801,0.008432748146591302,0.005703422033948428,0.007
…[truncated 245 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-19T16:45:32.426766+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"benchmark,rho_full,p_full,mono_full,rho_gdn_excluded,p_gdn_excluded,mono_gdn_excluded,direction,std_full_attn0,std_full_attn1,std_full_attn2,std_full_attn4,std_full_attn8,std_nogdn_attn0,std_nogdn_attn1,std_nogdn_attn2,std_nogdn_attn4,std_nogdn_attn8\\nLAMBADA,-0.9999999999999999,0.016666666666666666,True,-0.7,0.23333333333333334,False,WEAKER,0.02404712697705703,0.016238171620323174,0.013595712311665278,0.006055084765553574,0.004942545182713789,0.016204152920628795,0.007471375897535437,0.0020376479720551344,0.005821851348728924,0.0053366970696681615\\nHellaSwag,0.3,0.6833333333333333,False,0.49999999999999994,0.45,False,STRONGER,0.011684919531365781,0.008615212910147578,0.00946859081425128,0.009201244143823003,0.01183082679011367,0.009211312487552303,0.01020713005377416,0.008564031069508038,0.009808803027285373,0.012447719577773353\\nWinoGrande,0.09999999999999999,0.95,False,0.3,0.6833333333333333,False,STRONGER,0.0067074710781278545,0.021181496667056418,0.009652163287473934,0.007597752737802509,0.007839865522626334,0.005919494869771114,0.01617995264404104,0.008287292817679592,0.006314127861089203,0.008681925808997626\\nARC-Easy,-0.7,0.23333333333333334,False,-0.8999999999999998,0.08333333333333333,False,STRONGER,0.010014909257898295,0.019452560645897617,0.016761201811228865,0.004576180255415263,0.001301012695776599,0.008838383838383868,0.01704545454545453,0.006944444444444475,0.0050505050505050275,0.00021043771043771642\\nARC-Challenge,0.6,0.35,False,-0.19999999999999998,0.7833333333333333,False,WEAKER,0.009577621297202906,0.007705470525679222,0.007673912152009124,0.012565825958119756,0.013242829040754071,0.011518771331057998,0.00938566552901024,0.004266211604095599,0.015358361774744034,0.007679180887372017\\nMMLU,-0.7,0.23333333333333334,False,0.6,0.35,False,WEAKER,0.009200975872321134,0.005255878164789419,0.008432748146591302,0.007086829501826489,0.004045832460787097,0.0032402791625124466,0.00074775672981056
…[truncated 173 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-19T16:45:32.426989+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/paper_data",
  "description": "Create paper_data output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "Bash",
  "tool_args": {
    "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/paper_data",
    "description": "Create paper_data output directory"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-19T16:45:32.427121+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-19T16:45:32.427242+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/paper_data/convergence_table.csv",
  "content": "benchmark,taxonomy,rho,raw_p,bonferroni_6_adj_p,bonferroni_10_adj_p,std_pure,std_h3_1,convergence_ratio,significant\nLAMBADA,retrieval,-1.0,0.0167,0.100,0.167,0.02405,0.00494,4.87,no\nHellaSwag,reasoning,0.3,0.6833,1.0,1.0,0.01168,0.01183,0.99,no\nARC-Challenge,reasoning,0.6,0.35,1.0,1.0,0.00958,0.01324,0.72,no\nWinoGrande,reasoning,0.1,0.95,1.0,1.0,0.00671,0.00784,0.86,no\nARC-Easy,mixed,-0.7,0.2333,1.0,1.0,0.01001,0.00130,7.70,no\nMMLU,mixed,-0.7,0.2333,1.0,1.0,0.00920,0.00405,2.27,no\nBoolQ,retrieval,0.2,0.7833,,1.0,0.01632,0.02357,0.69,no\nPIQA,reasoning,-0.5,0.45,,1.0,0.00540,0.00339,1.59,no\nSciQ,mixed,0.1,0.95,,1.0,0.00873,0.00736,1.19,no\nxstorycloze_en,retrieval,-0.6,0.35,,1.0,0.00816,0.00548,1.49,no\nCOPA (supplementary),reasoning,-0.67,0.2667,,,0.02625,0.00471,5.57,supplementary\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/paper_data/convergence_table.csv",
    "content": "benchmark,taxonomy,rho,raw_p,bonferroni_6_adj_p,bonferroni_10_adj_p,std_pure,std_h3_1,convergence_ratio,significant\nLAMBADA,retrieval,-1.0,0.0167,0.100,0.167,0.02405,0.00494,4.87,no\nHellaSwag,reasoning,0.3,0.6833,1.0,1.0,0.01168,0.01183,0.99,no\nARC-Challenge,reasoning,0.6,0.35,1.0,1.0,0.00958,0.01324,0.72,no\nWinoGrande,reasoning,0.1,0.95,1.0,1.0,0.00671,0.00784,0.86,no\nARC-Easy,mixed,-0.7,0.2333,1.0,1.0,0.01001,0.00130,7.70,no\nMMLU,mixed,-0.7,0.2333,1.0,1.0,0.00920,0.00405,2.27,no\nBoolQ,retrieval,0.2,0.7833,,1.0,0.01632,0.02357,0.69,no\nPIQA,reasoning,-0.5,0.45,,1.0,0.00540,0.00339,1.59,no\nSciQ,mixed,0.1,0.95,,1.0,0.00873,0.00736,1.19,no\nxstorycloze_en,retrieval,-0.6,0.35,,1.0,0.00816,0.00548,1.49,no\nCOPA (supplementary),reasoning,-0.67,0.2667,,,0.02625,0.00471,5.57,supplementary\n"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-19T16:45:32.427386+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/paper_data/convergence_table.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-19T16:45:32.427518+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/paper_data/per_example_table.csv",
  "content": "arch,helped_count,hurt_count,net_effect,pairwise_jaccard_helped,pairwise_jaccard_hurt\nGDN,462,615,-153,0.096,0.096\nRetNet,426,495,-69,0.100,0.095\nHGRN2,548,395,+153,0.104,0.088\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/paper_data/per_example_table.csv",
    "content": "arch,helped_count,hurt_count,net_effect,pairwise_jaccard_helped,pairwise_jaccard_hurt\nGDN,462,615,-153,0.096,0.096\nRetNet,426,495,-69,0.100,0.095\nHGRN2,548,395,+153,0.104,0.088\n"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-19T16:45:32.427659+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/paper_data/per_example_table.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-19T16:45:32.427783+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/paper_data/gdn_sensitivity_table.csv",
  "content": "benchmark,rho_with_gdn,p_with_gdn,rho_without_gdn,p_without_gdn,direction_change\nLAMBADA,-1.0,0.0167,-0.7,0.2333,WEAKER\nHellaSwag,0.3,0.6833,0.5,0.45,STRONGER\nWinoGrande,0.1,0.95,0.3,0.6833,STRONGER\nARC-Easy,-0.7,0.2333,-0.9,0.0833,STRONGER\nARC-Challenge,0.6,0.35,-0.2,0.7833,WEAKER\nMMLU,-0.7,0.2333,0.6,0.35,WEAKER\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/paper_data/gdn_sensitivity_table.csv",
    "content": "benchmark,rho_with_gdn,p_with_gdn,rho_without_gdn,p_without_gdn,direction_change\nLAMBADA,-1.0,0.0167,-0.7,0.2333,WEAKER\nHellaSwag,0.3,0.6833,0.5,0.45,STRONGER\nWinoGrande,0.1,0.95,0.3,0.6833,STRONGER\nARC-Easy,-0.7,0.2333,-0.9,0.0833,STRONGER\nARC-Challenge,0.6,0.35,-0.2,0.7833,WEAKER\nMMLU,-0.7,0.2333,0.6,0.35,WEAKER\n"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-19T16:45:32.427899+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/paper_data/gdn_sensitivity_table.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-19T16:45:32.428012+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/paper_data/decoupling_data.csv",
  "content": "attention_ratio,cross_arch_std,jaccard_helped,jaccard_hurt,net_asymmetry\n0.0000,0.024047,,,\n0.0400,0.016238,0.09452,0.08733,0.01281\n0.0769,0.013596,0.09509,0.08087,0.01889\n0.1429,0.006055,0.09223,0.09880,0.03868\n0.2500,0.004943,0.10018,0.09281,0.03959\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/paper_data/decoupling_data.csv",
    "content": "attention_ratio,cross_arch_std,jaccard_helped,jaccard_hurt,net_asymmetry\n0.0000,0.024047,,,\n0.0400,0.016238,0.09452,0.08733,0.01281\n0.0769,0.013596,0.09509,0.08087,0.01889\n0.1429,0.006055,0.09223,0.09880,0.03868\n0.2500,0.004943,0.10018,0.09281,0.03959\n"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-19T16:45:32.428125+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/paper_data/decoupling_data.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-19T16:45:32.428240+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/paper_data/bca_ci_data.json",
  "content": "{\n  \"benchmark\": \"LAMBADA\",\n  \"rho\": -1.0,\n  \"method_used\": \"percentile\",\n  \"ci_lower\": -1.0,\n  \"ci_upper\": -0.7,\n  \"confidence_level\": 0.95,\n  \"crosses_zero\": false,\n  \"n_bootstrap\": 10000,\n  \"n_valid\": 8875,\n  \"degenerate_count\": 1125,\n  \"degenerate_pct\": 11.25,\n  \"seed\": 42,\n  \"p_rho_negative\": 1.0,\n  \"p_rho_positive\": 0.0,\n  \"bca_note\": \"BCa degenerate at rho=-1.0 boundary (11.25% of bootstrap samples had zero variance); percentile CI used instead. The CI [-1.0, -0.7] excludes zero, supporting a negative correlation.\",\n  \"percentile_vs_bca\": \"BCa correction requires finite acceleration estimate, which degenerates when the point estimate is at the parameter boundary (rho=-1.0). Percentile CI is valid but slightly less accurate for skewed distributions. With 88.75% valid samples, the percentile interval is reliable.\"\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/paper_data/bca_ci_data.json",
    "content": "{\n  \"benchmark\": \"LAMBADA\",\n  \"rho\": -1.0,\n  \"method_used\": \"percentile\",\n  \"ci_lower\": -1.0,\n  \"ci_upper\": -0.7,\n  \"confidence_level\": 0.95,\n  \"crosses_zero\": false,\n  \"n_bootstrap\": 10000,\n  \"n_valid\": 8875,\n  \"degenerate_count\": 1125,\n  \"degenerate_pct\": 11.25,\n  \"seed\": 42,\n  \"p_rho_negative\": 1.0,\n  \"p_rho_positive\": 0.0,\n  \"bca_note\": \"BCa degenerate at rho=-1.0 boundary (11.25% of bootstrap samples had zero variance); percentile CI used instead. The CI [-1.0, -0.7] excludes zero, supporting a negative correlation.\",\n  \"percentile_vs_bca\": \"BCa correction requires finite acceleration estimate, which degenerates when the point estimate is at the parameter boundary (rho=-1.0). Percentile CI is valid but slightly less accurate for skewed distributions. With 88.75% valid samples, the percentile interval is reliable.\"\n}\n"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-19T16:45:32.428365+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/paper_data/bca_ci_data.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-19T16:45:32.428495+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "for f in /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/paper_data/*; do echo \"=== $(basename $f) ===\" && wc -l \"$f\" && cat \"$f\" && echo; done",
  "description": "Verify all output files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "Bash",
  "tool_args": {
    "command": "for f in /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/paper_data/*; do echo \"=== $(basename $f) ===\" && wc -l \"$f\" && cat \"$f\" && echo; done",
    "description": "Verify all output files"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-19T16:45:32.428657+00:00_

=== bca_ci_data.json ===
18 /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/paper_data/bca_ci_data.json
{
  "benchmark": "LAMBADA",
  "rho": -1.0,
  "method_used": "percentile",
  "ci_lower": -1.0,
  "ci_upper": -0.7,
  "confidence_level": 0.95,
  "crosses_zero": false,
  "n_bootstrap": 10000,
  "n_valid": 8875,
  "degenerate_count": 1125,
  "degenerate_pct": 11.25,
  "seed": 42,
  "p_rho_negative": 1.0,
  "p_rho_positive": 0.0,
  "bca_note": "BCa degenerate at rho=-1.0 boundary (11.25% of bootstrap samples had zero variance); percentile CI used instead. The CI [-1.0, -0.7] excludes zero, supporting a negative correlation.",
  "percentile_vs_bca": "BCa correction requires finite acceleration estimate, which degenerates when the point estimate is at the parameter boundary (rho=-1.0). Percentile CI is valid but slightly less accurate for skewed distributions. With 88.75% valid samples, the percentile interval is reliable."
}

=== convergence_table.csv ===
12 /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/paper_data/convergence_table.csv
benchmark,taxonomy,rho,raw_p,bonferroni_6_adj_p,bonferroni_10_adj_p,std_pure,std_h3_1,convergence_ratio,significant
LAMBADA,retrieval,-1.0,0.0167,0.100,0.167,0.02405,0.00494,4.87,no
HellaSwag,reasoning,0.3,0.6833,1.0,1.0,0.01168,0.01183,0.99,no
ARC-Challenge,reasoning,0.6,0.35,1.0,1.0,0.00958,0.01324,0.72,no
WinoGrande,reasoning,0.1,0.95,1.0,1.0,0.00671,0.00784,0.86,no
ARC-Easy,mixed,-0.7,0.2333,1.0,1.0,0.01001,0.00130,7.70,no
MMLU,mixed,-0.7,0.2333,1.0,1.0,0.00920,0.00405,2.27,no
BoolQ,retrieval,0.2,0.7833,,1.0,0.01632,0.02357,0.69,no
PIQA,reasoning,-0.5,0.45,,1.0,0.00540,0.00339,1.59,no
SciQ,mixed,0.1,0.95,,1.0,0.00873,0.00736,1.19,no
xstorycloze_en,retrieval,-0.6,0.35,,1.0,0.00816,0.00548,1.49,no
COPA (supplementary),reasoning,-0.67,0.2667,,,0.02625,0.00471,5.57,supplementary

=== decoupling_data.csv ===
6 /home/ubuntu/.agent-ml-research-idea_gen_0509_2
…[truncated 1132 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-19T16:45:32.428826+00:00_

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
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
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

_source line 50 · 2026-05-19T16:45:32.428972+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-19T16:45:32.429092+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "paper_data_convergence_table",
  "type": "data",
  "description": "Table 1: Full 11-benchmark convergence statistics (rho, p-values, Bonferroni corrections, std, convergence ratio)",
  "project": "entrainment_gated_ft",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/paper_data/convergence_table.csv",
  "tags": "['paper', 'table1', 'convergence']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "paper_data_convergence_table",
    "type": "data",
    "description": "Table 1: Full 11-benchmark convergence statistics (rho, p-values, Bonferroni corrections, std, convergence ratio)",
    "project": "entrainment_gated_ft",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/paper_data/convergence_table.csv",
    "tags": "['paper', 'table1', 'convergence']"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-19T16:45:32.429229+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260519_1adf01\", \"name\": \"paper_data_convergence_table\", \"type\": \"data\", \"description\": \"Table 1: Full 11-benchmark convergence statistics (rho, p-values, Bonferroni corrections, std, convergence ratio)\", \"path\": \"projects/entrainment_gated_ft/artifacts/_project/data/convergence_table.csv\", \"url\": null, \"project\": \"entrainment_gated_ft\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-19T16:45:15.536674+00:00\", \"tags\": [\"paper\", \"table1\", \"convergence\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-19T16:45:32.429355+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "paper_data_per_example_table",
  "type": "data",
  "description": "Table 2: Per-example helped/hurt counts and pairwise Jaccard by architecture (GDN, RetNet, HGRN2)",
  "project": "entrainment_gated_ft",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/paper_data/per_example_table.csv",
  "tags": "['paper', 'table2', 'per-example']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "paper_data_per_example_table",
    "type": "data",
    "description": "Table 2: Per-example helped/hurt counts and pairwise Jaccard by architecture (GDN, RetNet, HGRN2)",
    "project": "entrainment_gated_ft",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/paper_data/per_example_table.csv",
    "tags": "['paper', 'table2', 'per-example']"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-19T16:45:32.429490+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260519_c85296\", \"name\": \"paper_data_per_example_table\", \"type\": \"data\", \"description\": \"Table 2: Per-example helped/hurt counts and pairwise Jaccard by architecture (GDN, RetNet, HGRN2)\", \"path\": \"projects/entrainment_gated_ft/artifacts/_project/data/per_example_table.csv\", \"url\": null, \"project\": \"entrainment_gated_ft\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-19T16:45:17.176497+00:00\", \"tags\": [\"paper\", \"table2\", \"per-example\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-19T16:45:32.429609+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "paper_data_gdn_sensitivity_table",
  "type": "data",
  "description": "Table 3: GDN sensitivity analysis - rho/p with vs without GDN across 6 benchmarks",
  "project": "entrainment_gated_ft",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/paper_data/gdn_sensitivity_table.csv",
  "tags": "['paper', 'table3', 'gdn-sensitivity']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "paper_data_gdn_sensitivity_table",
    "type": "data",
    "description": "Table 3: GDN sensitivity analysis - rho/p with vs without GDN across 6 benchmarks",
    "project": "entrainment_gated_ft",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/paper_data/gdn_sensitivity_table.csv",
    "tags": "['paper', 'table3', 'gdn-sensitivity']"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-19T16:45:32.429790+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260519_18c708\", \"name\": \"paper_data_gdn_sensitivity_table\", \"type\": \"data\", \"description\": \"Table 3: GDN sensitivity analysis - rho/p with vs without GDN across 6 benchmarks\", \"path\": \"projects/entrainment_gated_ft/artifacts/_project/data/gdn_sensitivity_table.csv\", \"url\": null, \"project\": \"entrainment_gated_ft\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-19T16:45:19.088023+00:00\", \"tags\": [\"paper\", \"table3\", \"gdn-sensitivity\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-19T16:45:32.429922+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "paper_data_decoupling",
  "type": "data",
  "description": "D008 decoupling figure data: cross-arch std + Jaccard helped/hurt + net asymmetry by attention ratio",
  "project": "entrainment_gated_ft",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/paper_data/decoupling_data.csv",
  "tags": "['paper', 'figure', 'decoupling', 'D008']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "paper_data_decoupling",
    "type": "data",
    "description": "D008 decoupling figure data: cross-arch std + Jaccard helped/hurt + net asymmetry by attention ratio",
    "project": "entrainment_gated_ft",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/paper_data/decoupling_data.csv",
    "tags": "['paper', 'figure', 'decoupling', 'D008']"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-19T16:45:32.430059+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260519_318a0c\", \"name\": \"paper_data_decoupling\", \"type\": \"data\", \"description\": \"D008 decoupling figure data: cross-arch std + Jaccard helped/hurt + net asymmetry by attention ratio\", \"path\": \"projects/entrainment_gated_ft/artifacts/_project/data/decoupling_data.csv\", \"url\": null, \"project\": \"entrainment_gated_ft\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-19T16:45:21.420265+00:00\", \"tags\": [\"paper\", \"figure\", \"decoupling\", \"D008\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-19T16:45:32.430180+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "paper_data_bca_ci",
  "type": "data",
  "description": "BCa bootstrap CI data for LAMBADA rho: CI bounds, degeneracy stats, percentile vs BCa explanation",
  "project": "entrainment_gated_ft",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/paper_data/bca_ci_data.json",
  "tags": "['paper', 'bootstrap', 'CI', 'LAMBADA']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "paper_data_bca_ci",
    "type": "data",
    "description": "BCa bootstrap CI data for LAMBADA rho: CI bounds, degeneracy stats, percentile vs BCa explanation",
    "project": "entrainment_gated_ft",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/paper_data/bca_ci_data.json",
    "tags": "['paper', 'bootstrap', 'CI', 'LAMBADA']"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-19T16:45:32.430311+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260519_d07792\", \"name\": \"paper_data_bca_ci\", \"type\": \"data\", \"description\": \"BCa bootstrap CI data for LAMBADA rho: CI bounds, degeneracy stats, percentile vs BCa explanation\", \"path\": \"projects/entrainment_gated_ft/artifacts/_project/data/bca_ci_data.json\", \"url\": null, \"project\": \"entrainment_gated_ft\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-19T16:45:23.544793+00:00\", \"tags\": [\"paper\", \"bootstrap\", \"CI\", \"LAMBADA\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 61 · 2026-05-19T16:45:32.430465+00:00_

5 个数据文件全部生成并注册完成。

| 文件 | 行数 | 路径 |
|------|------|------|
| `convergence_table.csv` | 12 (header+11 benchmarks) | `artifacts/paper_data/convergence_table.csv` |
| `per_example_table.csv` | 4 (header+3 archs) | `artifacts/paper_data/per_example_table.csv` |
| `gdn_sensitivity_table.csv` | 7 (header+6 benchmarks) | `artifacts/paper_data/gdn_sensitivity_table.csv` |
| `decoupling_data.csv` | 6 (header+5 ratios) | `artifacts/paper_data/decoupling_data.csv` |
| `bca_ci_data.json` | 18 | `artifacts/paper_data/bca_ci_data.json` |

数据来源：exp-001/008 registry（6 benchmarks）、exp-011/011-xstorycloze registry（5 benchmarks）、exp-003/003-p2 registry（per-example counts）、exp-010 registry + bridge CSV（decoupling + Jaccard）、exp-008 bootstrap_ci（BCa CI）。COPA 标记为 supplementary (n=100)，不参与 Bonferroni 校正。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_figure-table-data-prep_20260519T164223"
}
```

</details>

---
