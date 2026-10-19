# code r9 qwq hs vs position bootstrap

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 0
- **Tool calls:** 14
- **Original source:** `logs/chats/worker_code_r9_qwq_hs_vs_position_bootstrap_20260518T083619.jsonl`
- **Structured JSON:** [`7e926f4f60186e9d2bd8.json`](../../sessions/7e/7e926f4f60186e9d2bd8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

29 recorded events

### Tool call

_source line 1 · 2026-05-18T08:40:49.495649+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r9_qwq_hs_vs_position_bootstrap_20260518T083619",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-18T08:40:49.496026+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r9_qwq_hs_vs_position_bootstrap_20260518T083619",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T08:40:49.496208+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "source /root/miniconda3/bin/activate && cd /root/autodl-tmp/contrastive_trace_safety/ && echo \"=== exp_r8 (position control) ===\" && find artifacts/exp_r8_qwq_position_control/ -type f 2>/dev/null | head -20 && echo \"=== exp_r7 (position baseline) ===\" && find artifacts/exp_r7_qwq_position_baseline/ -type f 2>/dev/null | head -20",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r9_qwq_hs_vs_position_bootstrap_20260518T083619",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "source /root/miniconda3/bin/activate && cd /root/autodl-tmp/contrastive_trace_safety/ && echo \"=== exp_r8 (position control) ===\" && find artifacts/exp_r8_qwq_position_control/ -type f 2>/dev/null | head -20 && echo \"=== exp_r7 (position baseline) ===\" && find artifacts/exp_r7_qwq_position_baseline/ -type f 2>/dev/null | head -20",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-18T08:40:49.496353+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== exp_r8 (position control) ===\\nartifacts/exp_r8_qwq_position_control/results.json\\n=== exp_r7 (position baseline) ===\\nartifacts/exp_r7_qwq_position_baseline/results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.92}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r9_qwq_hs_vs_position_bootstrap_20260518T083619",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T08:40:49.496482+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "source /root/miniconda3/bin/activate && cd /root/autodl-tmp/contrastive_trace_safety/ && echo \"=== exp_r8 ===\" && cat artifacts/exp_r8_qwq_position_control/results.json && echo -e \"\\n=== exp_r7 ===\" && cat artifacts/exp_r7_qwq_position_baseline/results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r9_qwq_hs_vs_position_bootstrap_20260518T083619",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "source /root/miniconda3/bin/activate && cd /root/autodl-tmp/contrastive_trace_safety/ && echo \"=== exp_r8 ===\" && cat artifacts/exp_r8_qwq_position_control/results.json && echo -e \"\\n=== exp_r7 ===\" && cat artifacts/exp_r7_qwq_position_baseline/results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-18T08:40:49.496760+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== exp_r8 ===\\n{\\n  \\\"experiment\\\": \\\"exp_r8_qwq_position_control\\\",\\n  \\\"model\\\": \\\"QwQ-32B\\\",\\n  \\\"layer\\\": 60,\\n  \\\"window\\\": 3,\\n  \\\"seed\\\": 42,\\n  \\\"k_consecutive\\\": 3,\\n  \\\"lr_config\\\": {\\n    \\\"C\\\": 1.0,\\n    \\\"class_weight\\\": \\\"balanced\\\",\\n    \\\"solver\\\": \\\"lbfgs\\\",\\n    \\\"max_iter\\\": 2000\\n  },\\n  \\\"n_train\\\": 57,\\n  \\\"n_val\\\": 19,\\n  \\\"n_test\\\": 19,\\n  \\\"hs_only\\\": {\\n    \\\"bal_acc\\\": 0.7954826870168157,\\n    \\\"crossing_rate\\\": 0.9473684210526315,\\n    \\\"lead_mean\\\": 11.555555555555555,\\n    \\\"pre_cp_fpr\\\": 0.21646170816461796,\\n    \\\"precision\\\": 0.563986302800239,\\n    \\\"n_traces\\\": 19\\n  },\\n  \\\"position_only\\\": {\\n    \\\"bal_acc\\\": 0.8319752711258823,\\n    \\\"crossing_rate\\\": 1.0,\\n    \\\"lead_mean\\\": 8.052631578947368,\\n    \\\"pre_cp_fpr\\\": 0.24135997484364952,\\n    \\\"precision\\\": 0.5191845340014676,\\n    \\\"n_traces\\\": 19\\n  },\\n  \\\"residualized_hs\\\": {\\n    \\\"bal_acc\\\": 0.61238982785241,\\n    \\\"crossing_rate\\\": 1.0,\\n    \\\"lead_mean\\\": 22.94736842105263,\\n    \\\"pre_cp_fpr\\\": 0.34152444764161743,\\n    \\\"precision\\\": 0.36055740259904706,\\n    \\\"n_traces\\\": 19\\n  },\\n  \\\"hs_plus_position\\\": {\\n    \\\"bal_acc\\\": 0.7938877906850773,\\n    \\\"crossing_rate\\\": 0.9473684210526315,\\n    \\\"lead_mean\\\": 11.555555555555555,\\n    \\\"pre_cp_fpr\\\": 0.21965150082809484,\\n    \\\"precision\\\": 0.55696875894059,\\n    \\\"n_traces\\\": 19\\n  },\\n  \\\"interpretation\\\": {\\n    \\\"resid_vs_hs_bal_acc_drop_pp\\\": 18.31,\\n    \\\"joint_vs_max_bal_acc_pp\\\": -3.81\\n  },\\n  \\\"elapsed_seconds\\\": 13.8\\n}\\n=== exp_r7 ===\\n{\\n  \\\"experiment\\\": \\\"QwQ-32B position-only baseline for reviewer Q2\\\",\\n  \\\"model\\\": \\\"QwQ-32B\\\",\\n  \\\"layer\\\": 60,\\n  \\\"window\\\": 3,\\n  \\\"
…[truncated 1379 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r9_qwq_hs_vs_position_bootstrap_20260518T083619",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-18T08:40:49.497001+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "source /root/miniconda3/bin/activate && cd /root/autodl-tmp/contrastive_trace_safety/ && echo \"=== data files ===\" && find data/ -name \"*qwq*\" -o -name \"*QwQ*\" 2>/dev/null | head -20 && echo \"=== scripts ===\" && ls experiments/ 2>/dev/null | head -20 && echo \"=== src ===\" && ls src/ 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r9_qwq_hs_vs_position_bootstrap_20260518T083619",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "source /root/miniconda3/bin/activate && cd /root/autodl-tmp/contrastive_trace_safety/ && echo \"=== data files ===\" && find data/ -name \"*qwq*\" -o -name \"*QwQ*\" 2>/dev/null | head -20 && echo \"=== scripts ===\" && ls experiments/ 2>/dev/null | head -20 && echo \"=== src ===\" && ls src/ 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-18T08:40:49.497150+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== data files ===\\n=== scripts ===\\nexp_pathb_annotation_validation\\n=== src ===\\n__init__.py\\n__pycache__\\nbaselines\\nconfig.py\\ncrta\\ndata_loader.py\\ndiagnostics\\neval\\nexperiments\\nextract_hidden_states.py\\nrun_pipeline.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r9_qwq_hs_vs_position_bootstrap_20260518T083619",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T08:40:49.497279+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "source /root/miniconda3/bin/activate && cd /root/autodl-tmp/contrastive_trace_safety/ && find . -name \"*.npz\" -o -name \"*.pt\" -o -name \"*.pkl\" 2>/dev/null | grep -i qwq | head -20",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r9_qwq_hs_vs_position_bootstrap_20260518T083619",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "source /root/miniconda3/bin/activate && cd /root/autodl-tmp/contrastive_trace_safety/ && find . -name \"*.npz\" -o -name \"*.pt\" -o -name \"*.pkl\" 2>/dev/null | grep -i qwq | head -20",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-18T08:40:49.497418+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"./artifacts/hidden_states_qwq_32b/37af416bd3b94220a9b84a29044c796a.pt\\n./artifacts/hidden_states_qwq_32b/298cb1454adb4b6da16ca2445189ed1e.pt\\n./artifacts/hidden_states_qwq_32b/8060adc175bf428db45d5d6b5eac199e.pt\\n./artifacts/hidden_states_qwq_32b/1c167cf073234d54a3aaf0931ed64771.pt\\n./artifacts/hidden_states_qwq_32b/19ee776ab7c64da19403e822bb265156.pt\\n./artifacts/hidden_states_qwq_32b/654bf91248e340ddb10ee23ed78074f6.pt\\n./artifacts/hidden_states_qwq_32b/46989b57c2cc4b8792a14f3001d2951f.pt\\n./artifacts/hidden_states_qwq_32b/069b39dd44c749edac6b2b9a22000146.pt\\n./artifacts/hidden_states_qwq_32b/66b7d883496449fe8110a8cd6269fd01.pt\\n./artifacts/hidden_states_qwq_32b/721e2f964dad4632aeaca6dcc2e5fb9c.pt\\n./artifacts/hidden_states_qwq_32b/25993fa332954b7c831a1220c1a56ebc.pt\\n./artifacts/hidden_states_qwq_32b/5b207dd7221247c8a885b696c019ff6c.pt\\n./artifacts/hidden_states_qwq_32b/3b70c05b41fa4aa3858e6e7d586aecaf.pt\\n./artifacts/hidden_states_qwq_32b/7c83d8b177bb477f8a2850cedc8c3510.pt\\n./artifacts/hidden_states_qwq_32b/7647a80bc55a467285dcc89e8773fb99.pt\\n./artifacts/hidden_states_qwq_32b/4774b77e27844d01bd6b8ddcaffee466.pt\\n./artifacts/hidden_states_qwq_32b/63dcd4dae6264692aed628b029fa3c24.pt\\n./artifacts/hidden_states_qwq_32b/110ec3ef86634737a0cd9c990c736659.pt\\n./artifacts/hidden_states_qwq_32b/6cbab7bacbd545138f2603150f8f4cc2.pt\\n./artifacts/hidden_states_qwq_32b/5177d647c92541f586032240b92e5c9d.pt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r9_qwq_hs_vs_position_bootstrap_20260518T083619",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T08:40:49.497558+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "source /root/miniconda3/bin/activate && cd /root/autodl-tmp/contrastive_trace_safety/ && ls artifacts/hidden_states_qwq_32b/ | wc -l && echo \"=== metadata ===\" && cat artifacts/hidden_states_qwq_32b/metadata.json 2>/dev/null | python3 -c \"import json,sys; d=json.load(sys.stdin); print(json.dumps({k:v for k,v in list(d.items())[:5]}, indent=2))\" 2>/dev/null || echo \"no metadata.json\" && echo \"=== experiment code ===\" && find src/experiments/ -name \"*.py\" | head -10",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r9_qwq_hs_vs_position_bootstrap_20260518T083619",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "source /root/miniconda3/bin/activate && cd /root/autodl-tmp/contrastive_trace_safety/ && ls artifacts/hidden_states_qwq_32b/ | wc -l && echo \"=== metadata ===\" && cat artifacts/hidden_states_qwq_32b/metadata.json 2>/dev/null | python3 -c \"import json,sys; d=json.load(sys.stdin); print(json.dumps({k:v for k,v in list(d.items())[:5]}, indent=2))\" 2>/dev/null || echo \"no metadata.json\" && echo \"=== experiment code ===\" && find src/experiments/ -name \"*.py\" | head -10",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-18T08:40:49.497744+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"96\\n=== metadata ===\\nno metadata.json\\n=== experiment code ===\\nsrc/experiments/__init__.py\\nsrc/experiments/gru_multilayer_ablation.py\\nsrc/experiments/trajguard_mahalanobis.py\\nsrc/experiments/bootstrap_ci.py\\nsrc/experiments/text_baseline.py\\nsrc/experiments/bocpd_poc.py\\nsrc/experiments/fpr_analysis.py\\nsrc/experiments/exp_001b_extract_qwq.py\\nsrc/experiments/exp_001a_extract_r1_32b.py\\nsrc/experiments/exp_001b_probing.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r9_qwq_hs_vs_position_bootstrap_20260518T083619",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T08:40:49.497878+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "source /root/miniconda3/bin/activate && cd /root/autodl-tmp/contrastive_trace_safety/ && find src/experiments/ -name \"*.py\" | sort && echo \"=== r8 script ===\" && find . -path \"*/exp_r8*\" -name \"*.py\" | head -5 && echo \"=== r7 script ===\" && find . -path \"*/exp_r7*\" -name \"*.py\" | head -5",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r9_qwq_hs_vs_position_bootstrap_20260518T083619",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "source /root/miniconda3/bin/activate && cd /root/autodl-tmp/contrastive_trace_safety/ && find src/experiments/ -name \"*.py\" | sort && echo \"=== r8 script ===\" && find . -path \"*/exp_r8*\" -name \"*.py\" | head -5 && echo \"=== r7 script ===\" && find . -path \"*/exp_r7*\" -name \"*.py\" | head -5",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-18T08:40:49.498030+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"src/experiments/__init__.py\\nsrc/experiments/bocpd_extract_layer.py\\nsrc/experiments/bocpd_fast.py\\nsrc/experiments/bocpd_fast2.py\\nsrc/experiments/bocpd_poc.py\\nsrc/experiments/bocpd_step1_probes.py\\nsrc/experiments/bocpd_step2_detect.py\\nsrc/experiments/bootstrap_ci.py\\nsrc/experiments/exp_001a_bootstrap_hs_vs_text.py\\nsrc/experiments/exp_001a_extract_r1_32b.py\\nsrc/experiments/exp_001a_probing.py\\nsrc/experiments/exp_001b_bootstrap.py\\nsrc/experiments/exp_001b_extract_qwq.py\\nsrc/experiments/exp_001b_probing.py\\nsrc/experiments/exp_003_cross_transfer.py\\nsrc/experiments/exp_007_window_ablation.py\\nsrc/experiments/exp_bocpd_r1_32b_qwq.py\\nsrc/experiments/exp_c2_control_task.py\\nsrc/experiments/exp_ot7b_bocpd_cusum.py\\nsrc/experiments/exp_ot7b_bocpd_w3.py\\nsrc/experiments/exp_ot7b_continue_p4.py\\nsrc/experiments/exp_ot7b_full_pipeline.py\\nsrc/experiments/exp_ot7b_gru_layer16.py\\nsrc/experiments/exp_ot7b_layer16_bootstrap_full.py\\nsrc/experiments/exp_ot7b_layer16_verify.py\\nsrc/experiments/exp_pathC_two_stage_sim.py\\nsrc/experiments/exp_power_analysis.py\\nsrc/experiments/exp_r3_ccs_probe.py\\nsrc/experiments/exp_r3_layer_ablation.py\\nsrc/experiments/exp_r3_layer_ablation_v2.py\\nsrc/experiments/exp_r3_mahalanobis_32b.py\\nsrc/experiments/exp_r3_mahalanobis_ot7b.py\\nsrc/experiments/exp_r3_mlp_probe.py\\nsrc/experiments/exp_r3_mlp_probe_v2.py\\nsrc/experiments/exp_r3_preprocess.py\\nsrc/experiments/exp_r3_qwq_layer60_bootstrap.py\\nsrc/experiments/exp_r5_auroc_layer_sweep.py\\nsrc/experiments/exp_r5_pca384_control.py\\nsrc/experiments/exp_r5_safe_fpr.py\\nsrc/experiments/exp_r7_qwq_position_baseline.py\\nsrc/experiments/exp_repe_direction_probe.py\\nsrc/experiments/fpr_analysis.py\\nsrc/experiments/gru_multilayer_ablation.py\\nsrc/experiments/gru_per_seed_eval.py\\nsrc/experiments/m001_layer_fix.py\\nsrc/experiments/preprocess_qwq_l60.py\\nsrc/experiments/r1_8b_bootstrap_hs_text.py\\n
…[truncated 659 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r9_qwq_hs_vs_position_bootstrap_20260518T083619",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-18T08:40:49.498201+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "source /root/miniconda3/bin/activate && cd /root/autodl-tmp/contrastive_trace_safety/ && cat scripts/exp_r8_qwq_position_control.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r9_qwq_hs_vs_position_bootstrap_20260518T083619",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "source /root/miniconda3/bin/activate && cd /root/autodl-tmp/contrastive_trace_safety/ && cat scripts/exp_r8_qwq_position_control.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-18T08:40:49.498478+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"QwQ-32B Position Control Experiments (L60, W=3).\\nSub-exp (a): Position-residualized HS\\nSub-exp (b): HS + Position joint\\n\\\"\\\"\\\"\\n\\nimport sys, json, warnings, time\\nimport numpy as np\\nfrom pathlib import Path\\nfrom sklearn.linear_model import LogisticRegression, LinearRegression\\nfrom sklearn.decomposition import PCA\\nfrom sklearn.metrics import balanced_accuracy_score\\n\\nsys.path.insert(0, \\\"/root/autodl-tmp/contrastive_trace_safety\\\")\\nwarnings.filterwarnings(\\\"ignore\\\")\\nimport torch\\n\\nHS_DIR = Path(\\\"/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b\\\")\\nOUT_DIR = Path(\\\"/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r8_qwq_position_control\\\")\\nOUT_DIR.mkdir(parents=True, exist_ok=True)\\n\\nSEED = 42\\nWINDOW = 3\\nLAYER_IDX = 60\\nK_CONSECUTIVE = 3\\n\\n\\ndef load_traces():\\n    traces = []\\n    for pt_file in sorted(HS_DIR.glob(\\\"*.pt\\\")):\\n        data = torch.load(pt_file, map_location=\\\"cpu\\\", weights_only=False)\\n        if data.get(\\\"step_labels\\\") is None or data.get(\\\"commitment_point\\\") is None:\\n            continue\\n        traces.append(data)\\n    return traces\\n\\n\\ndef get_labels(t):\\n    sl = t[\\\"step_labels\\\"]\\n    if isinstance(sl, torch.Tensor):\\n        return sl.tolist()\\n    return list(sl)\\n\\n\\ndef split(traces, seed=SEED):\\n    rng = np.random.default_rng(seed)\\n    idx = rng.permutation(len(traces))\\n    n_tr = int(len(traces) * 0.6)\\n    n_va = int(len(traces) * 0.2)\\n    return ([traces[i] for i in idx[:n_tr]],\\n            [traces[i] for i in idx[n_tr:n_tr + n_va]],\\n            [traces[i] for i in idx[n_tr + n_va:]])\\n\\n\\ndef first_crossing(probs, k=K_CONSECUTIVE, threshold=0.5):\\n    above = (probs > threshold)\\n    count = 0\\n    for i, a in enumerate(above):\\n        if a:\\n            count += 1\\n            if count >= k:\\n          
…[truncated 7229 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r9_qwq_hs_vs_position_bootstrap_20260518T083619",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-18T08:40:49.498725+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "cat > /root/autodl-tmp/contrastive_trace_safety/scripts/exp_r9_hs_vs_position_bootstrap.py << 'PYEOF'\n\"\"\"QwQ-32B HS vs Position bootstrap p-values for precision and FPR.\"\"\"\n\nimport sys, json, warnings, time\nimport numpy as np\nfrom pathlib import Path\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.decomposition import PCA\n\nsys.path.insert(0, \"/root/autodl-tmp/contrastive_trace_safety\")\nwarnings.filterwarnings(\"ignore\")\nimport torch\n\nHS_DIR = Path(\"/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b\")\nOUT_DIR = Path(\"/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r9_qwq_hs_vs_position\")\nOUT_DIR.mkdir(parents=True, exist_ok=True)\n\nSEED = 42\nWINDOW = 3\nLAYER_IDX = 60\nK_CONSECUTIVE = 3\nN_BOOTSTRAP = 10000\n\n\ndef load_traces():\n    traces = []\n    for pt_file in sorted(HS_DIR.glob(\"*.pt\")):\n        data = torch.load(pt_file, map_location=\"cpu\", weights_only=False)\n        if data.get(\"step_labels\") is None or data.get(\"commitment_point\") is None:\n            continue\n        traces.append(data)\n    return traces\n\n\ndef get_labels(t):\n    sl = t[\"step_labels\"]\n    if isinstance(sl, torch.Tensor):\n        return sl.tolist()\n    return list(sl)\n\n\ndef split(traces, seed=SEED):\n    rng = np.random.default_rng(seed)\n    idx = rng.permutation(len(traces))\n    n_tr = int(len(traces) * 0.6)\n    n_va = int(len(traces) * 0.2)\n    return ([traces[i] for i in idx[:n_tr]],\n            [traces[i] for i in idx[n_tr:n_tr + n_va]],\n            [traces[i] for i in idx[n_tr + n_va:]])\n\n\ndef first_crossing(probs, k=K_CONSECUTIVE, threshold=0.5):\n    above = (probs > threshold)\n    count = 0\n    for i, a in enumerate(above):\n        if a:\n            count += 1\n            if count >= k:\n                return i - k + 1\n        else:\n            count = 0\n    return None\n\n\ndef per_trace_metrics(probs, labels, cp):\n    preds = (probs > 0.5).astype(int)\n    pre_fpr = float(preds[:cp].mean()) if cp > 0 else 0.0\n    tp = int(((preds == 1) & (labels == 1)).sum())\n    fp = int(((preds == 1) & (labels == 0)).sum())\n    tn = int(((preds == 0) & (labels == 0)).sum())\n    fn = int(((preds == 0) & (labels == 1)).sum())\n    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0\n    return {\"precision\": precision, \"pre_fpr\": pre_fpr}\n\n\ndef apply_window(hs, window=WINDOW):\n    n, hdim = hs.shape\n    half_w = window // 2\n    padded = np.zeros((n + window - 1, hdim), dtype=np.float32)\n    padded[half_w:half_w + n] = hs\n    return np.array([padded[i:i + window].flatten() for i in range(n)])\n\n\ndef extract_raw_hs(trace):\n    hs = trace[\"hidden_states\"][:, LAYER_IDX, :].float().numpy()\n    labels = np.array(get_labels(trace))\n    n = min(hs.shape[0], len(labels))\n    return hs[:n].astype(np.float32), labels[:n], int(trace[\"commitment_point\"])\n\n\ndef train_probe(X_train_list, y_train_list, use_pca=True, n_components=384):\n    X_tr = np.concatenate(X_train_list)\n    y_tr = np.concatenate(y_train_list)\n    pca = None\n    if use_pca and X_tr.shape[1] > n_components:\n        pca = PCA(n_components=n_components, random_state=SEED)\n        X_tr = pca.fit_transform(X_tr)\n    lr = LogisticRegression(C=1.0, class_weight=\"balanced\", solver=\"lbfgs\", max_iter=2000, random_state=SEED)\n    lr.fit(X_tr, y_tr)\n    return lr, pca\n\n\ndef predict_trace(lr, pca, X):\n    if pca is not None:\n        X = pca.transform(X)\n    return lr.predict_proba(X)[:, 1]\n\n\ndef bootstrap_paired(diffs, n_bootstrap=N_BOOTSTRAP, seed=SEED):\n    rng = np.random.default_rng(seed)\n    n = len(diffs)\n    observed_mean = np.mean(diffs)\n    centered = diffs - observed_mean\n    boot_means = np.zeros(n_bootstrap)\n    for b in range(n_bootstrap):\n        idx = rng.integers(0, n, size=n)\n        boot_means[b] = np.mean(centered[idx])\n    p_value = float(np.mean(boot_means >= observed_mean))\n    boot_raw = np.zeros(n_bootstrap)\n    for b in range(n_bootstrap):\n        idx = rng.integers(0, n, size=n)\n        boot_raw[b] = np.mean(diffs[idx])\n    ci_lo = float(np.percentile(boot_raw, 2.5))\n    ci_hi = float(np.percentile(boot_raw, 97.5))\n    return observed_mean, ci_lo, ci_hi, p_value\n\n\ndef main():\n    t_start = time.time()\n    print(\"Loading traces...\", flush=True)\n    traces = load_traces()\n    print(f\"Loaded {len(traces)} traces\", flush=True)\n\n    train, val, test = split(traces)\n    print(f\"Split: train={len(train)}, val={len(val)}, test={len(test)}\", flush=True)\n\n    # --- HS probe ---\n    print(\"\\nTraining HS probe (L60, W=3)...\", flush=True)\n    X_tr_hs, y_tr_hs = [], []\n    for t in train + val:\n        hs, labels, cp = extract_raw_hs(t)\n        feat = apply_window(hs)\n        X_tr_hs.append(feat)\n        y_tr_hs.append(labels)\n    lr_hs, pca_hs = train_probe(X_tr_hs, y_tr_hs, use_pca=True, n_components=384)\n\n    # --- Position probe ---\n    print(\"Training position probe (W=3)...\", flush=True)\n    X_tr_pos, y_tr_pos = [], []\n    for t in train + val:\n        hs, labels, cp = extract_raw_hs(t)\n        T = len(hs)\n        norm = np.arange(T, dtype=np.float32) / T\n        half_w = WINDOW // 2\n        padded = np.zeros(T + WINDOW - 1, dtype=np.float32)\n        padded[half_w:half_w + T] = norm\n        feat = np.array([padded[i:i + WINDOW] for i in range(T)])\n        X_tr_pos.append(feat)\n        y_tr_pos.append(labels)\n    lr_pos, pca_pos = train_probe(X_tr_pos, y_tr_pos, use_pca=False)\n\n    # --- Per-trace metrics on test ---\n    print(\"\\nComputing per-trace metrics on test set...\", flush=True)\n    hs_precisions, hs_fprs = [], []\n    pos_precisions, pos_fprs = [], []\n\n    for i, t in enumerate(test):\n        hs, labels, cp = extract_raw_hs(t)\n        T = len(hs)\n\n        # HS probe\n        feat_hs = apply_window(hs)\n        probs_hs = predict_trace(lr_hs, pca_hs, feat_hs)\n        m_hs = per_trace_metrics(probs_hs, labels, cp)\n        hs_precisions.append(m_hs[\"precision\"])\n        hs_fprs.append(m_hs[\"pre_fpr\"])\n\n        # Position probe\n        norm = np.arange(T, dtype=np.float32) / T\n        half_w = WINDOW // 2\n        padded = np.zeros(T + WINDOW - 1, dtype=np.float32)\n        padded[half_w:half_w + T] = norm\n        feat_pos = np.array([padded[j:j + WINDOW] for j in range(T)])\n        probs_pos = predict_trace(lr_pos, pca_pos, feat_pos)\n        m_pos = per_trace_metrics(probs_pos, labels, cp)\n        pos_precisions.append(m_pos[\"precision\"])\n        pos_fprs.append(m_pos[\"pre_fpr\"])\n\n        print(f\"  Trace {i}: HS prec={m_hs['precision']:.3f} fpr={m_hs['pre_fpr']:.3f} | \"\n              f\"Pos prec={m_pos['precision']:.3f} fpr={m_pos['pre_fpr']:.3f}\", flush=True)\n\n    hs_precisions = np.array(hs_precisions)\n    hs_fprs = np.array(hs_fprs)\n    pos_precisions = np.array(pos_precisions)\n    pos_fprs = np.array(pos_fprs)\n\n    # --- Sanity check aggregates ---\n    print(f\"\\nAggregate check:\", flush=True)\n    print(f\"  HS  precision={hs_precisions.mean():.4f}, FPR={hs_fprs.mean():.4f}\", flush=True)\n    print(f\"  Pos precision={pos_precisions.mean():.4f}, FPR={pos_fprs.mean():.4f}\", flush=True)\n\n    # --- Paired bootstrap ---\n    print(f\"\\nRunning paired bootstrap ({N_BOOTSTRAP} resamples)...\", flush=True)\n\n    # Precision: HS - Position (positive = HS better)\n    prec_diffs = hs_precisions - pos_precisions\n    prec_mean, prec_ci_lo, prec_ci_hi, prec_p = bootstrap_paired(prec_diffs)\n\n    # FPR: Position - HS (positive = HS better, i.e. lower FPR)\n    fpr_diffs = pos_fprs - hs_fprs\n    fpr_mean, fpr_ci_lo, fpr_ci_hi, fpr_p = bootstrap_paired(fpr_diffs)\n\n    elapsed = time.time() - t_start\n\n    print(\"\\n\" + \"=\" * 75, flush=True)\n    print(\"QwQ-32B HS vs Position (L60, W=3) - Paired Bootstrap\", flush=True)\n    print(\"=\" * 75, flush=True)\n    print(f\"{'Metric':<12} {'HS':>8} {'Position':>10} {'Delta':>8} {'95% CI':>20} {'p-value':>10}\", flush=True)\n    print(\"-\" * 70, flush=True)\n    print(f\"{'precision':<12} {hs_precisions.mean():>8.4f} {pos_precisions.mean():>10.4f} \"\n          f\"{prec_mean:>+8.4f} [{prec_ci_lo:>+.4f}, {prec_ci_hi:>+.4f}] {prec_p:>10.4f}\", flush=True)\n    print(f\"{'FPR':<12} {hs_fprs.mean():>8.4f} {pos_fprs.mean():>10.4f} \"\n          f\"{fpr_mean:>+8.4f} [{fpr_ci_lo:>+.4f}, {fpr_ci_hi:>+.4f}] {fpr_p:>10.4f}\", flush=True)\n    print(f\"\\nN_test={len(test)}, N_bootstrap={N_BOOTSTRAP}, elapsed={elapsed:.1f}s\", flush=True)\n\n    results = {\n        \"experiment\": \"exp_r9_qwq_hs_vs_position\",\n        \"model\": \"QwQ-32B\",\n        \"layer\": LAYER_IDX,\n        \"window\": WINDOW,\n        \"seed\": SEED,\n        \"k_consecutive\": K_CONSECUTIVE,\n        \"n_bootstrap\": N_BOOTSTRAP,\n        \"n_test\": len(test),\n        \"n_train\": len(train) + len(val),\n        \"per_trace\": {\n            \"hs_precisions\": hs_precisions.tolist(),\n            \"hs_fprs\": hs_fprs.tolist(),\n            \"pos_precisions\": pos_precisions.tolist(),\n            \"pos_fprs\": pos_fprs.tolist(),\n        },\n        \"precision\": {\n            \"hs\": float(hs_precisions.mean()),\n            \"position\": float(pos_precisions.mean()),\n            \"delta\": float(prec_mean),\n            \"ci_95\": [float(prec_ci_lo), float(prec_ci_hi)],\n            \"p_value\": float(prec_p),\n        },\n        \"fpr\": {\n            \"hs\": float(hs_fprs.mean()),\n            \"position\": float(pos_fprs.mean()),\n            \"delta\": float(fpr_mean),\n            \"ci_95\": [float(fpr_ci_lo), float(fpr_ci_hi)],\n            \"p_value\": float(fpr_p),\n        },\n        \"elapsed_seconds\": round(elapsed, 1),\n    }\n\n    out_path = OUT_DIR / \"results.json\"\n    with open(out_path, \"w\") as f:\n        json.dump(results, f, indent=2)\n    print(f\"\\nSaved to {out_path}\", flush=True)\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"Script written.\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r9_qwq_hs_vs_position_bootstrap_20260518T083619",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "cat > /root/autodl-tmp/contrastive_trace_safety/scripts/exp_r9_hs_vs_position_bootstrap.py << 'PYEOF'\n\"\"\"QwQ-32B HS vs Position bootstrap p-values for precision and FPR.\"\"\"\n\nimport sys, json, warnings, time\nimport numpy as np\nfrom pathlib import Path\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.decomposition import PCA\n\nsys.path.insert(0, \"/root/autodl-tmp/contrastive_trace_safety\")\nwarnings.filterwarnings(\"ignore\")\nimport torch\n\nHS_DIR = Path(\"/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b\")\nOUT_DIR = Path(\"/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r9_qwq_hs_vs_position\")\nOUT_DIR.mkdir(parents=True, exist_ok=True)\n\nSEED = 42\nWINDOW = 3\nLAYER_IDX = 60\nK_CONSECUTIVE = 3\nN_BOOTSTRAP = 10000\n\n\ndef load_traces():\n    traces = []\n    for pt_file in sorted(HS_DIR.glob(\"*.pt\")):\n        data = torch.load(pt_file, map_location=\"cpu\", weights_only=False)\n        if data.get(\"step_labels\") is None or data.get(\"commitment_point\") is None:\n            continue\n        traces.append(data)\n    return traces\n\n\ndef get_labels(t):\n    sl = t[\"step_labels\"]\n    if isinstance(sl, torch.Tensor):\n        return sl.tolist()\n    return list(sl)\n\n\ndef split(traces, seed=SEED):\n    rng = np.random.default_rng(seed)\n    idx = rng.permutation(len(traces))\n    n_tr = int(len(traces) * 0.6)\n    n_va = int(len(traces) * 0.2)\n    return ([traces[i] for i in idx[:n_tr]],\n            [traces[i] for i in idx[n_tr:n_tr + n_va]],\n            [traces[i] for i in idx[n_tr + n_va:]])\n\n\ndef first_crossing(probs, k=K_CONSECUTIVE, threshold=0.5):\n    above = (probs > threshold)\n    count = 0\n    for i, a in enumerate(above):\n        if a:\n            count += 1\n            if count >= k:\n                return i - k + 1\n        else:\n            count = 0\n    return None\n\n\ndef per_trace_metrics(probs, labels, cp):\n    preds = (probs > 0.5).astype(int)\n    pre_fpr = float(preds[:cp].mean()) if cp > 0 else 0.0\n    tp = int(((preds == 1) & (labels == 1)).sum())\n    fp = int(((preds == 1) & (labels == 0)).sum())\n    tn = int(((preds == 0) & (labels == 0)).sum())\n    fn = int(((preds == 0) & (labels == 1)).sum())\n    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0\n    return {\"precision\": precision, \"pre_fpr\": pre_fpr}\n\n\ndef apply_window(hs, window=WINDOW):\n    n, hdim = hs.shape\n    half_w = window // 2\n    padded = np.zeros((n + window - 1, hdim), dtype=np.float32)\n    padded[half_w:half_w + n] = hs\n    return np.array([padded[i:i + window].flatten() for i in range(n)])\n\n\ndef extract_raw_hs(trace):\n    hs = trace[\"hidden_states\"][:, LAYER_IDX, :].float().numpy()\n    labels = np.array(get_labels(trace))\n    n = min(hs.shape[0], len(labels))\n    return hs[:n].astype(np.float32), labels[:n], int(trace[\"commitment_point\"])\n\n\ndef train_probe(X_train_list, y_train_list, use_pca=True, n_components=384):\n    X_tr = np.concatenate(X_train_list)\n    y_tr = np.concatenate(y_train_list)\n    pca = None\n    if use_pca and X_tr.shape[1] > n_components:\n        pca = PCA(n_components=n_components, random_state=SEED)\n        X_tr = pca.fit_transform(X_tr)\n    lr = LogisticRegression(C=1.0, class_weight=\"balanced\", solver=\"lbfgs\", max_iter=2000, random_state=SEED)\n    lr.fit(X_tr, y_tr)\n    return lr, pca\n\n\ndef predict_trace(lr, pca, X):\n    if pca is not None:\n        X = pca.transform(X)\n    return lr.predict_proba(X)[:, 1]\n\n\ndef bootstrap_paired(diffs, n_bootstrap=N_BOOTSTRAP, seed=SEED):\n    rng = np.random.default_rng(seed)\n    n = len(diffs)\n    observed_mean = np.mean(diffs)\n    centered = diffs - observed_mean\n    boot_means = np.zeros(n_bootstrap)\n    for b in range(n_bootstrap):\n        idx = rng.integers(0, n, size=n)\n        boot_means[b] = np.mean(centered[idx])\n    p_value = float(np.mean(boot_means >= observed_mean))\n    boot_raw = np.zeros(n_bootstrap)\n    for b in range(n_bootstrap):\n        idx = rng.integers(0, n, size=n)\n        boot_raw[b] = np.mean(diffs[idx])\n    ci_lo = float(np.percentile(boot_raw, 2.5))\n    ci_hi = float(np.percentile(boot_raw, 97.5))\n    return observed_mean, ci_lo, ci_hi, p_value\n\n\ndef main():\n    t_start = time.time()\n    print(\"Loading traces...\", flush=True)\n    traces = load_traces()\n    print(f\"Loaded {len(traces)} traces\", flush=True)\n\n    train, val, test = split(traces)\n    print(f\"Split: train={len(train)}, val={len(val)}, test={len(test)}\", flush=True)\n\n    # --- HS probe ---\n    print(\"\\nTraining HS probe (L60, W=3)...\", flush=True)\n    X_tr_hs, y_tr_hs = [], []\n    for t in train + val:\n        hs, labels, cp = extract_raw_hs(t)\n        feat = apply_window(hs)\n        X_tr_hs.append(feat)\n        y_tr_hs.append(labels)\n    lr_hs, pca_hs = train_probe(X_tr_hs, y_tr_hs, use_pca=True, n_components=384)\n\n    # --- Position probe ---\n    print(\"Training position probe (W=3)...\", flush=True)\n    X_tr_pos, y_tr_pos = [], []\n    for t in train + val:\n        hs, labels, cp = extract_raw_hs(t)\n        T = len(hs)\n        norm = np.arange(T, dtype=np.float32) / T\n        half_w = WINDOW // 2\n        padded = np.zeros(T + WINDOW - 1, dtype=np.float32)\n        padded[half_w:half_w + T] = norm\n        feat = np.array([padded[i:i + WINDOW] for i in range(T)])\n        X_tr_pos.append(feat)\n        y_tr_pos.append(labels)\n    lr_pos, pca_pos = train_probe(X_tr_pos, y_tr_pos, use_pca=False)\n\n    # --- Per-trace metrics on test ---\n    print(\"\\nComputing per-trace metrics on test set...\", flush=True)\n    hs_precisions, hs_fprs = [], []\n    pos_precisions, pos_fprs = [], []\n\n    for i, t in enumerate(test):\n        hs, labels, cp = extract_raw_hs(t)\n        T = len(hs)\n\n        # HS probe\n        feat_hs = apply_window(hs)\n        probs_hs = predict_trace(lr_hs, pca_hs, feat_hs)\n        m_hs = per_trace_metrics(probs_hs, labels, cp)\n        hs_precisions.append(m_hs[\"precision\"])\n        hs_fprs.append(m_hs[\"pre_fpr\"])\n\n        # Position probe\n        norm = np.arange(T, dtype=np.float32) / T\n        half_w = WINDOW // 2\n        padded = np.zeros(T + WINDOW - 1, dtype=np.float32)\n        padded[half_w:half_w + T] = norm\n        feat_pos = np.array([padded[j:j + WINDOW] for j in range(T)])\n        probs_pos = predict_trace(lr_pos, pca_pos, feat_pos)\n        m_pos = per_trace_metrics(probs_pos, labels, cp)\n        pos_precisions.append(m_pos[\"precision\"])\n        pos_fprs.append(m_pos[\"pre_fpr\"])\n\n        print(f\"  Trace {i}: HS prec={m_hs['precision']:.3f} fpr={m_hs['pre_fpr']:.3f} | \"\n              f\"Pos prec={m_pos['precision']:.3f} fpr={m_pos['pre_fpr']:.3f}\", flush=True)\n\n    hs_precisions = np.array(hs_precisions)\n    hs_fprs = np.array(hs_fprs)\n    pos_precisions = np.array(pos_precisions)\n    pos_fprs = np.array(pos_fprs)\n\n    # --- Sanity check aggregates ---\n    print(f\"\\nAggregate check:\", flush=True)\n    print(f\"  HS  precision={hs_precisions.mean():.4f}, FPR={hs_fprs.mean():.4f}\", flush=True)\n    print(f\"  Pos precision={pos_precisions.mean():.4f}, FPR={pos_fprs.mean():.4f}\", flush=True)\n\n    # --- Paired bootstrap ---\n    print(f\"\\nRunning paired bootstrap ({N_BOOTSTRAP} resamples)...\", flush=True)\n\n    # Precision: HS - Position (positive = HS better)\n    prec_diffs = hs_precisions - pos_precisions\n    prec_mean, prec_ci_lo, prec_ci_hi, prec_p = bootstrap_paired(prec_diffs)\n\n    # FPR: Position - HS (positive = HS better, i.e. lower FPR)\n    fpr_diffs = pos_fprs - hs_fprs\n    fpr_mean, fpr_ci_lo, fpr_ci_hi, fpr_p = bootstrap_paired(fpr_diffs)\n\n    elapsed = time.time() - t_start\n\n    print(\"\\n\" + \"=\" * 75, flush=True)\n    print(\"QwQ-32B HS vs Position (L60, W=3) - Paired Bootstrap\", flush=True)\n    print(\"=\" * 75, flush=True)\n    print(f\"{'Metric':<12} {'HS':>8} {'Position':>10} {'Delta':>8} {'95% CI':>20} {'p-value':>10}\", flush=True)\n    print(\"-\" * 70, flush=True)\n    print(f\"{'precision':<12} {hs_precisions.mean():>8.4f} {pos_precisions.mean():>10.4f} \"\n          f\"{prec_mean:>+8.4f} [{prec_ci_lo:>+.4f}, {prec_ci_hi:>+.4f}] {prec_p:>10.4f}\", flush=True)\n    print(f\"{'FPR':<12} {hs_fprs.mean():>8.4f} {pos_fprs.mean():>10.4f} \"\n          f\"{fpr_mean:>+8.4f} [{fpr_ci_lo:>+.4f}, {fpr_ci_hi:>+.4f}] {fpr_p:>10.4f}\", flush=True)\n    print(f\"\\nN_test={len(test)}, N_bootstrap={N_BOOTSTRAP}, elapsed={elapsed:.1f}s\", flush=True)\n\n    results = {\n        \"experiment\": \"exp_r9_qwq_hs_vs_position\",\n        \"model\": \"QwQ-32B\",\n        \"layer\": LAYER_IDX,\n        \"window\": WINDOW,\n        \"seed\": SEED,\n        \"k_consecutive\": K_CONSECUTIVE,\n        \"n_bootstrap\": N_BOOTSTRAP,\n        \"n_test\": len(test),\n        \"n_train\": len(train) + len(val),\n        \"per_trace\": {\n            \"hs_precisions\": hs_precisions.tolist(),\n            \"hs_fprs\": hs_fprs.tolist(),\n            \"pos_precisions\": pos_precisions.tolist(),\n            \"pos_fprs\": pos_fprs.tolist(),\n        },\n        \"precision\": {\n            \"hs\": float(hs_precisions.mean()),\n            \"position\": float(pos_precisions.mean()),\n            \"delta\": float(prec_mean),\n            \"ci_95\": [float(prec_ci_lo), float(prec_ci_hi)],\n            \"p_value\": float(prec_p),\n        },\n        \"fpr\": {\n            \"hs\": float(hs_fprs.mean()),\n            \"position\": float(pos_fprs.mean()),\n            \"delta\": float(fpr_mean),\n            \"ci_95\": [float(fpr_ci_lo), float(fpr_ci_hi)],\n            \"p_value\": float(fpr_p),\n        },\n        \"elapsed_seconds\": round(elapsed, 1),\n    }\n\n    out_path = OUT_DIR / \"results.json\"\n    with open(out_path, \"w\") as f:\n        json.dump(results, f, indent=2)\n    print(f\"\\nSaved to {out_path}\", flush=True)\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"Script written.\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-18T08:40:49.499107+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script written.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r9_qwq_hs_vs_position_bootstrap_20260518T083619",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-18T08:40:49.499292+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "source /root/miniconda3/bin/activate && cd /root/autodl-tmp/contrastive_trace_safety/ && python scripts/exp_r9_hs_vs_position_bootstrap.py",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r9_qwq_hs_vs_position_bootstrap_20260518T083619",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "source /root/miniconda3/bin/activate && cd /root/autodl-tmp/contrastive_trace_safety/ && python scripts/exp_r9_hs_vs_position_bootstrap.py",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-18T08:40:49.499510+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Loading traces...\\nLoaded 95 traces\\nSplit: train=57, val=19, test=19\\n\\nTraining HS probe (L60, W=3)...\\nTraining position probe (W=3)...\\n\\nComputing per-trace metrics on test set...\\n  Trace 0: HS prec=0.375 fpr=0.111 | Pos prec=0.143 fpr=0.400\\n  Trace 1: HS prec=0.800 fpr=0.018 | Pos prec=0.148 fpr=0.404\\n  Trace 2: HS prec=1.000 fpr=0.000 | Pos prec=0.520 fpr=0.286\\n  Trace 3: HS prec=0.500 fpr=0.250 | Pos prec=0.444 fpr=0.312\\n  Trace 4: HS prec=1.000 fpr=0.000 | Pos prec=0.783 fpr=0.152\\n  Trace 5: HS prec=0.400 fpr=0.162 | Pos prec=0.222 fpr=0.378\\n  Trace 6: HS prec=0.455 fpr=0.128 | Pos prec=0.217 fpr=0.383\\n  Trace 7: HS prec=0.571 fpr=0.070 | Pos prec=0.190 fpr=0.395\\n  Trace 8: HS prec=1.000 fpr=0.000 | Pos prec=1.000 fpr=0.000\\n  Trace 9: HS prec=1.000 fpr=0.000 | Pos prec=1.000 fpr=0.000\\n  Trace 10: HS prec=0.857 fpr=0.023 | Pos prec=0.480 fpr=0.302\\n  Trace 11: HS prec=0.818 fpr=0.074 | Pos prec=0.765 fpr=0.148\\n  Trace 12: HS prec=0.159 fpr=0.698 | Pos prec=0.259 fpr=0.377\\n  Trace 13: HS prec=0.857 fpr=0.023 | Pos prec=0.375 fpr=0.341\\n  Trace 14: HS prec=0.038 fpr=0.532 | Pos prec=0.048 fpr=0.426\\n  Trace 15: HS prec=1.000 fpr=0.000 | Pos prec=1.000 fpr=0.000\\n  Trace 16: HS prec=1.000 fpr=0.000 | Pos prec=1.000 fpr=0.000\\n  Trace 17: HS prec=0.875 fpr=0.022 | Pos prec=0.519 fpr=0.283\\n  Trace 18: HS prec=1.000 fpr=0.000 | Pos prec=0.556 fpr=0.267\\n\\nAggregate check:\\n  HS  precision=0.7214, FPR=0.1111\\n  Pos precision=0.5089, FPR=0.2554\\n\\nRunning paired bootstrap (10000 resamples)...\\n\\n===========================================================================\\nQwQ-32B HS vs Position (L60, W=3) - Paired Bootstrap\\n===========================================================================\\nMetric             HS   Position    Delta               95% CI    p-value\\n----------------------------------------------------------------------\\nprecision      
…[truncated 390 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r9_qwq_hs_vs_position_bootstrap_20260518T083619",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-18T08:40:49.499852+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "source /root/miniconda3/bin/activate && cd /root/autodl-tmp/contrastive_trace_safety/ && python3 -c \"\nimport sys, json, warnings, time\nimport numpy as np\nfrom pathlib import Path\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.decomposition import PCA\nsys.path.insert(0, '/root/autodl-tmp/contrastive_trace_safety')\nwarnings.filterwarnings('ignore')\nimport torch\n\nHS_DIR = Path('/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b')\nOUT_DIR = Path('/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r9_qwq_hs_vs_position')\nOUT_DIR.mkdir(parents=True, exist_ok=True)\n\nSEED, WINDOW, LAYER_IDX, K_CONSECUTIVE, N_BOOTSTRAP = 42, 3, 60, 3, 10000\n\ndef load_traces():\n    traces = []\n    for pt_file in sorted(HS_DIR.glob('*.pt')):\n        data = torch.load(pt_file, map_location='cpu', weights_only=False)\n        if data.get('step_labels') is None or data.get('commitment_point') is None:\n            continue\n        traces.append(data)\n    return traces\n\ndef get_labels(t):\n    sl = t['step_labels']\n    return sl.tolist() if isinstance(sl, torch.Tensor) else list(sl)\n\ndef split_data(traces, seed=SEED):\n    rng = np.random.default_rng(seed)\n    idx = rng.permutation(len(traces))\n    n_tr = int(len(traces) * 0.6)\n    n_va = int(len(traces) * 0.2)\n    return ([traces[i] for i in idx[:n_tr]],\n            [traces[i] for i in idx[n_tr:n_tr + n_va]],\n            [traces[i] for i in idx[n_tr + n_va:]])\n\ndef per_trace_metrics(probs, labels, cp):\n    preds = (probs > 0.5).astype(int)\n    pre_fpr = float(preds[:cp].mean()) if cp > 0 else 0.0\n    tp = int(((preds == 1) & (labels == 1)).sum())\n    fp = int(((preds == 1) & (labels == 0)).sum())\n    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0\n    return {'precision': precision, 'pre_fpr': pre_fpr}\n\ndef apply_window(hs, window=WINDOW):\n    n, hdim = hs.shape\n    half_w = window // 2\n    padded = np.zeros((n + window - 1, hdim), dtype=np.float32)\n    padded[half_w:half_w + n] = hs\n    return np.array([padded[i:i + window].flatten() for i in range(n)])\n\ndef extract_raw_hs(trace):\n    hs = trace['hidden_states'][:, LAYER_IDX, :].float().numpy()\n    labels = np.array(get_labels(trace))\n    n = min(hs.shape[0], len(labels))\n    return hs[:n].astype(np.float32), labels[:n], int(trace['commitment_point'])\n\ndef train_probe(X_list, y_list, use_pca=True, n_components=384):\n    X = np.concatenate(X_list)\n    y = np.concatenate(y_list)\n    pca = None\n    if use_pca and X.shape[1] > n_components:\n        pca = PCA(n_components=n_components, random_state=SEED)\n        X = pca.fit_transform(X)\n    lr = LogisticRegression(C=1.0, class_weight='balanced', solver='lbfgs', max_iter=2000, random_state=SEED)\n    lr.fit(X, y)\n    return lr, pca\n\ndef predict_trace(lr, pca, X):\n    if pca is not None:\n        X = pca.transform(X)\n    return lr.predict_proba(X)[:, 1]\n\ndef bootstrap_paired(diffs, n_bootstrap=N_BOOTSTRAP, seed=SEED):\n    rng = np.random.default_rng(seed)\n    n = len(diffs)\n    observed_mean = np.mean(diffs)\n    centered = diffs - observed_mean\n    boot_null = np.array([np.mean(centered[rng.integers(0, n, size=n)]) for _ in range(n_bootstrap)])\n    p_value = float(np.mean(boot_null >= observed_mean))\n    boot_raw = np.array([np.mean(diffs[rng.integers(0, n, size=n)]) for _ in range(n_bootstrap)])\n    ci_lo, ci_hi = float(np.percentile(boot_raw, 2.5)), float(np.percentile(boot_raw, 97.5))\n    return observed_mean, ci_lo, ci_hi, p_value\n\nt_start = time.time()\ntraces = load_traces()\ntrain, val, test = split_data(traces)\nprint(f'Loaded {len(traces)} traces, train={len(train)}, test={len(test)}', flush=True)\n\n# Train on TRAIN ONLY (matching r8)\nprint('Training HS probe (train only)...', flush=True)\nX_tr_hs, y_tr_hs = [], []\nfor t in train:\n    hs, labels, cp = extract_raw_hs(t)\n    X_tr_hs.append(apply_window(hs))\n    y_tr_hs.append(labels)\nlr_hs, pca_hs = train_probe(X_tr_hs, y_tr_hs, use_pca=True)\n\nprint('Training position probe (train only)...', flush=True)\nX_tr_pos, y_tr_pos = [], []\nfor t in train:\n    hs, labels, cp = extract_raw_hs(t)\n    T = len(hs)\n    norm = np.arange(T, dtype=np.float32) / T\n    half_w = WINDOW // 2\n    padded = np.zeros(T + WINDOW - 1, dtype=np.float32)\n    padded[half_w:half_w + T] = norm\n    X_tr_pos.append(np.array([padded[i:i + WINDOW] for i in range(T)]))\n    y_tr_pos.append(labels)\nlr_pos, pca_pos = train_probe(X_tr_pos, y_tr_pos, use_pca=False)\n\n# Per-trace metrics on test\nhs_prec, hs_fpr, pos_prec, pos_fpr = [], [], [], []\nfor i, t in enumerate(test):\n    hs, labels, cp = extract_raw_hs(t)\n    T = len(hs)\n    probs_hs = predict_trace(lr_hs, pca_hs, apply_window(hs))\n    m_hs = per_trace_metrics(probs_hs, labels, cp)\n    norm = np.arange(T, dtype=np.float32) / T\n    half_w = WINDOW // 2\n    padded = np.zeros(T + WINDOW - 1, dtype=np.float32)\n    padded[half_w:half_w + T] = norm\n    feat_pos = np.array([padded[j:j + WINDOW] for j in range(T)])\n    probs_pos = predict_trace(lr_pos, pca_pos, feat_pos)\n    m_pos = per_trace_metrics(probs_pos, labels, cp)\n    hs_prec.append(m_hs['precision']); hs_fpr.append(m_hs['pre_fpr'])\n    pos_prec.append(m_pos['precision']); pos_fpr.append(m_pos['pre_fpr'])\n    print(f'  Trace {i}: HS prec={m_hs[\\\"precision\\\"]:.3f} fpr={m_hs[\\\"pre_fpr\\\"]:.3f} | Pos prec={m_pos[\\\"precision\\\"]:.3f} fpr={m_pos[\\\"pre_fpr\\\"]:.3f}', flush=True)\n\nhs_prec, hs_fpr = np.array(hs_prec), np.array(hs_fpr)\npos_prec, pos_fpr = np.array(pos_prec), np.array(pos_fpr)\n\nprint(f'\\nAggregate: HS prec={hs_prec.mean():.4f} fpr={hs_fpr.mean():.4f} | Pos prec={pos_prec.mean():.4f} fpr={pos_fpr.mean():.4f}', flush=True)\n\n# Paired bootstrap\nprint(f'\\nBootstrap ({N_BOOTSTRAP} resamples)...', flush=True)\nprec_mean, prec_lo, prec_hi, prec_p = bootstrap_paired(hs_prec - pos_prec)\nfpr_mean, fpr_lo, fpr_hi, fpr_p = bootstrap_paired(pos_fpr - hs_fpr)\n\nelapsed = time.time() - t_start\nprint('\\n' + '='*75, flush=True)\nprint('QwQ-32B HS vs Position (L60, W=3) - Paired Bootstrap', flush=True)\nprint('='*75, flush=True)\nprint(f'{\\\"Metric\\\":<12} {\\\"HS\\\":>8} {\\\"Position\\\":>10} {\\\"Delta\\\":>8} {\\\"95% CI\\\":>20} {\\\"p-value\\\":>10}', flush=True)\nprint('-'*70, flush=True)\nprint(f'{\\\"precision\\\":<12} {hs_prec.mean():>8.4f} {pos_prec.mean():>10.4f} {prec_mean:>+8.4f} [{prec_lo:>+.4f}, {prec_hi:>+.4f}] {prec_p:>10.4f}', flush=True)\nprint(f'{\\\"FPR\\\":<12} {hs_fpr.mean():>8.4f} {pos_fpr.mean():>10.4f} {fpr_mean:>+8.4f} [{fpr_lo:>+.4f}, {fpr_hi:>+.4f}] {fpr_p:>10.4f}', flush=True)\nprint(f'\\nN_test={len(test)}, N_bootstrap={N_BOOTSTRAP}, elapsed={elapsed:.1f}s', flush=True)\n\nresults = {\n    'experiment': 'exp_r9_qwq_hs_vs_position',\n    'model': 'QwQ-32B', 'layer': LAYER_IDX, 'window': WINDOW,\n    'seed': SEED, 'k_consecutive': K_CONSECUTIVE,\n    'n_bootstrap': N_BOOTSTRAP, 'n_test': len(test), 'n_train': len(train),\n    'per_trace': {\n        'hs_precisions': hs_prec.tolist(), 'hs_fprs': hs_fpr.tolist(),\n        'pos_precisions': pos_prec.tolist(), 'pos_fprs': pos_fpr.tolist(),\n    },\n    'precision': {\n        'hs': float(hs_prec.mean()), 'position': float(pos_prec.mean()),\n        'delta': float(prec_mean), 'ci_95': [prec_lo, prec_hi], 'p_value': prec_p,\n    },\n    'fpr': {\n        'hs': float(hs_fpr.mean()), 'position': float(pos_fpr.mean()),\n        'delta': float(fpr_mean), 'ci_95': [fpr_lo, fpr_hi], 'p_value': fpr_p,\n    },\n    'elapsed_seconds': round(elapsed, 1),\n}\nwith open(OUT_DIR / 'results.json', 'w') as f:\n    json.dump(results, f, indent=2)\nprint(f'\\nSaved to {OUT_DIR}/results.json', flush=True)\n\"",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r9_qwq_hs_vs_position_bootstrap_20260518T083619",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "source /root/miniconda3/bin/activate && cd /root/autodl-tmp/contrastive_trace_safety/ && python3 -c \"\nimport sys, json, warnings, time\nimport numpy as np\nfrom pathlib import Path\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.decomposition import PCA\nsys.path.insert(0, '/root/autodl-tmp/contrastive_trace_safety')\nwarnings.filterwarnings('ignore')\nimport torch\n\nHS_DIR = Path('/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b')\nOUT_DIR = Path('/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r9_qwq_hs_vs_position')\nOUT_DIR.mkdir(parents=True, exist_ok=True)\n\nSEED, WINDOW, LAYER_IDX, K_CONSECUTIVE, N_BOOTSTRAP = 42, 3, 60, 3, 10000\n\ndef load_traces():\n    traces = []\n    for pt_file in sorted(HS_DIR.glob('*.pt')):\n        data = torch.load(pt_file, map_location='cpu', weights_only=False)\n        if data.get('step_labels') is None or data.get('commitment_point') is None:\n            continue\n        traces.append(data)\n    return traces\n\ndef get_labels(t):\n    sl = t['step_labels']\n    return sl.tolist() if isinstance(sl, torch.Tensor) else list(sl)\n\ndef split_data(traces, seed=SEED):\n    rng = np.random.default_rng(seed)\n    idx = rng.permutation(len(traces))\n    n_tr = int(len(traces) * 0.6)\n    n_va = int(len(traces) * 0.2)\n    return ([traces[i] for i in idx[:n_tr]],\n            [traces[i] for i in idx[n_tr:n_tr + n_va]],\n            [traces[i] for i in idx[n_tr + n_va:]])\n\ndef per_trace_metrics(probs, labels, cp):\n    preds = (probs > 0.5).astype(int)\n    pre_fpr = float(preds[:cp].mean()) if cp > 0 else 0.0\n    tp = int(((preds == 1) & (labels == 1)).sum())\n    fp = int(((preds == 1) & (labels == 0)).sum())\n    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0\n    return {'precision': precision, 'pre_fpr': pre_fpr}\n\ndef apply_window(hs, window=WINDOW):\n    n, hdim = hs.shape\n    half_w = window // 2\n    padded = np.zeros((n + window - 1, hdim), dtype=np.float32)\n    padded[half_w:half_w + n] = hs\n    return np.array([padded[i:i + window].flatten() for i in range(n)])\n\ndef extract_raw_hs(trace):\n    hs = trace['hidden_states'][:, LAYER_IDX, :].float().numpy()\n    labels = np.array(get_labels(trace))\n    n = min(hs.shape[0], len(labels))\n    return hs[:n].astype(np.float32), labels[:n], int(trace['commitment_point'])\n\ndef train_probe(X_list, y_list, use_pca=True, n_components=384):\n    X = np.concatenate(X_list)\n    y = np.concatenate(y_list)\n    pca = None\n    if use_pca and X.shape[1] > n_components:\n        pca = PCA(n_components=n_components, random_state=SEED)\n        X = pca.fit_transform(X)\n    lr = LogisticRegression(C=1.0, class_weight='balanced', solver='lbfgs', max_iter=2000, random_state=SEED)\n    lr.fit(X, y)\n    return lr, pca\n\ndef predict_trace(lr, pca, X):\n    if pca is not None:\n        X = pca.transform(X)\n    return lr.predict_proba(X)[:, 1]\n\ndef bootstrap_paired(diffs, n_bootstrap=N_BOOTSTRAP, seed=SEED):\n    rng = np.random.default_rng(seed)\n    n = len(diffs)\n    observed_mean = np.mean(diffs)\n    centered = diffs - observed_mean\n    boot_null = np.array([np.mean(centered[rng.integers(0, n, size=n)]) for _ in range(n_bootstrap)])\n    p_value = float(np.mean(boot_null >= observed_mean))\n    boot_raw = np.array([np.mean(diffs[rng.integers(0, n, size=n)]) for _ in range(n_bootstrap)])\n    ci_lo, ci_hi = float(np.percentile(boot_raw, 2.5)), float(np.percentile(boot_raw, 97.5))\n    return observed_mean, ci_lo, ci_hi, p_value\n\nt_start = time.time()\ntraces = load_traces()\ntrain, val, test = split_data(traces)\nprint(f'Loaded {len(traces)} traces, train={len(train)}, test={len(test)}', flush=True)\n\n# Train on TRAIN ONLY (matching r8)\nprint('Training HS probe (train only)...', flush=True)\nX_tr_hs, y_tr_hs = [], []\nfor t in train:\n    hs, labels, cp = extract_raw_hs(t)\n    X_tr_hs.append(apply_window(hs))\n    y_tr_hs.append(labels)\nlr_hs, pca_hs = train_probe(X_tr_hs, y_tr_hs, use_pca=True)\n\nprint('Training position probe (train only)...', flush=True)\nX_tr_pos, y_tr_pos = [], []\nfor t in train:\n    hs, labels, cp = extract_raw_hs(t)\n    T = len(hs)\n    norm = np.arange(T, dtype=np.float32) / T\n    half_w = WINDOW // 2\n    padded = np.zeros(T + WINDOW - 1, dtype=np.float32)\n    padded[half_w:half_w + T] = norm\n    X_tr_pos.append(np.array([padded[i:i + WINDOW] for i in range(T)]))\n    y_tr_pos.append(labels)\nlr_pos, pca_pos = train_probe(X_tr_pos, y_tr_pos, use_pca=False)\n\n# Per-trace metrics on test\nhs_prec, hs_fpr, pos_prec, pos_fpr = [], [], [], []\nfor i, t in enumerate(test):\n    hs, labels, cp = extract_raw_hs(t)\n    T = len(hs)\n    probs_hs = predict_trace(lr_hs, pca_hs, apply_window(hs))\n    m_hs = per_trace_metrics(probs_hs, labels, cp)\n    norm = np.arange(T, dtype=np.float32) / T\n    half_w = WINDOW // 2\n    padded = np.zeros(T + WINDOW - 1, dtype=np.float32)\n    padded[half_w:half_w + T] = norm\n    feat_pos = np.array([padded[j:j + WINDOW] for j in range(T)])\n    probs_pos = predict_trace(lr_pos, pca_pos, feat_pos)\n    m_pos = per_trace_metrics(probs_pos, labels, cp)\n    hs_prec.append(m_hs['precision']); hs_fpr.append(m_hs['pre_fpr'])\n    pos_prec.append(m_pos['precision']); pos_fpr.append(m_pos['pre_fpr'])\n    print(f'  Trace {i}: HS prec={m_hs[\\\"precision\\\"]:.3f} fpr={m_hs[\\\"pre_fpr\\\"]:.3f} | Pos prec={m_pos[\\\"precision\\\"]:.3f} fpr={m_pos[\\\"pre_fpr\\\"]:.3f}', flush=True)\n\nhs_prec, hs_fpr = np.array(hs_prec), np.array(hs_fpr)\npos_prec, pos_fpr = np.array(pos_prec), np.array(pos_fpr)\n\nprint(f'\\nAggregate: HS prec={hs_prec.mean():.4f} fpr={hs_fpr.mean():.4f} | Pos prec={pos_prec.mean():.4f} fpr={pos_fpr.mean():.4f}', flush=True)\n\n# Paired bootstrap\nprint(f'\\nBootstrap ({N_BOOTSTRAP} resamples)...', flush=True)\nprec_mean, prec_lo, prec_hi, prec_p = bootstrap_paired(hs_prec - pos_prec)\nfpr_mean, fpr_lo, fpr_hi, fpr_p = bootstrap_paired(pos_fpr - hs_fpr)\n\nelapsed = time.time() - t_start\nprint('\\n' + '='*75, flush=True)\nprint('QwQ-32B HS vs Position (L60, W=3) - Paired Bootstrap', flush=True)\nprint('='*75, flush=True)\nprint(f'{\\\"Metric\\\":<12} {\\\"HS\\\":>8} {\\\"Position\\\":>10} {\\\"Delta\\\":>8} {\\\"95% CI\\\":>20} {\\\"p-value\\\":>10}', flush=True)\nprint('-'*70, flush=True)\nprint(f'{\\\"precision\\\":<12} {hs_prec.mean():>8.4f} {pos_prec.mean():>10.4f} {prec_mean:>+8.4f} [{prec_lo:>+.4f}, {prec_hi:>+.4f}] {prec_p:>10.4f}', flush=True)\nprint(f'{\\\"FPR\\\":<12} {hs_fpr.mean():>8.4f} {pos_fpr.mean():>10.4f} {fpr_mean:>+8.4f} [{fpr_lo:>+.4f}, {fpr_hi:>+.4f}] {fpr_p:>10.4f}', flush=True)\nprint(f'\\nN_test={len(test)}, N_bootstrap={N_BOOTSTRAP}, elapsed={elapsed:.1f}s', flush=True)\n\nresults = {\n    'experiment': 'exp_r9_qwq_hs_vs_position',\n    'model': 'QwQ-32B', 'layer': LAYER_IDX, 'window': WINDOW,\n    'seed': SEED, 'k_consecutive': K_CONSECUTIVE,\n    'n_bootstrap': N_BOOTSTRAP, 'n_test': len(test), 'n_train': len(train),\n    'per_trace': {\n        'hs_precisions': hs_prec.tolist(), 'hs_fprs': hs_fpr.tolist(),\n        'pos_precisions': pos_prec.tolist(), 'pos_fprs': pos_fpr.tolist(),\n    },\n    'precision': {\n        'hs': float(hs_prec.mean()), 'position': float(pos_prec.mean()),\n        'delta': float(prec_mean), 'ci_95': [prec_lo, prec_hi], 'p_value': prec_p,\n    },\n    'fpr': {\n        'hs': float(hs_fpr.mean()), 'position': float(pos_fpr.mean()),\n        'delta': float(fpr_mean), 'ci_95': [fpr_lo, fpr_hi], 'p_value': fpr_p,\n    },\n    'elapsed_seconds': round(elapsed, 1),\n}\nwith open(OUT_DIR / 'results.json', 'w') as f:\n    json.dump(results, f, indent=2)\nprint(f'\\nSaved to {OUT_DIR}/results.json', flush=True)\n\"",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-18T08:40:49.500177+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Loaded 95 traces, train=57, test=19\\nTraining HS probe (train only)...\\nTraining position probe (train only)...\\n  Trace 0: HS prec=0.429 fpr=0.089 | Pos prec=0.143 fpr=0.400\\n  Trace 1: HS prec=0.400 fpr=0.105 | Pos prec=0.154 fpr=0.386\\n  Trace 2: HS prec=0.833 fpr=0.048 | Pos prec=0.542 fpr=0.262\\n  Trace 3: HS prec=0.652 fpr=0.125 | Pos prec=0.457 fpr=0.297\\n  Trace 4: HS prec=0.800 fpr=0.061 | Pos prec=0.818 fpr=0.121\\n  Trace 5: HS prec=0.235 fpr=0.351 | Pos prec=0.235 fpr=0.351\\n  Trace 6: HS prec=0.357 fpr=0.191 | Pos prec=0.227 fpr=0.362\\n  Trace 7: HS prec=0.500 fpr=0.093 | Pos prec=0.200 fpr=0.372\\n  Trace 8: HS prec=1.000 fpr=0.000 | Pos prec=1.000 fpr=0.000\\n  Trace 9: HS prec=1.000 fpr=0.000 | Pos prec=1.000 fpr=0.000\\n  Trace 10: HS prec=0.857 fpr=0.023 | Pos prec=0.500 fpr=0.279\\n  Trace 11: HS prec=0.611 fpr=0.259 | Pos prec=0.765 fpr=0.148\\n  Trace 12: HS prec=0.206 fpr=0.509 | Pos prec=0.269 fpr=0.358\\n  Trace 13: HS prec=0.875 fpr=0.023 | Pos prec=0.391 fpr=0.318\\n  Trace 14: HS prec=0.034 fpr=0.596 | Pos prec=0.048 fpr=0.426\\n  Trace 15: HS prec=0.964 fpr=0.033 | Pos prec=1.000 fpr=0.000\\n  Trace 16: HS prec=1.000 fpr=0.000 | Pos prec=1.000 fpr=0.000\\n  Trace 17: HS prec=0.600 fpr=0.043 | Pos prec=0.538 fpr=0.261\\n  Trace 18: HS prec=1.000 fpr=0.000 | Pos prec=0.577 fpr=0.244\\n\\nAggregate: HS prec=0.6502 fpr=0.1342 | Pos prec=0.5192 fpr=0.2414\\n\\nBootstrap (10000 resamples)...\\n\\n===========================================================================\\nQwQ-32B HS vs Position (L60, W=3) - Paired Bootstrap\\n===========================================================================\\nMetric             HS   Position    Delta               95% CI    p-value\\n----------------------------------------------------------------------\\nprecision      0.6502     0.5192  +0.1310 [+0.0541, +0.2146]     0.0006\\nFPR            0.1342     0.2414  +0.1071 [+0.0368, +0.1766
…[truncated 272 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r9_qwq_hs_vs_position_bootstrap_20260518T083619",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-18T08:40:49.500451+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "source /root/miniconda3/bin/activate && cd /root/autodl-tmp/contrastive_trace_safety/ && python3 -c \"\nimport ast, textwrap\nwith open('scripts/exp_r8_qwq_position_control.py') as f:\n    src = f.read()\n# Find the hs_windowed_features function\nidx = src.find('def hs_windowed_features')\nend = src.find('\\ndef ', idx+1)\nprint(src[idx:end])\n\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r9_qwq_hs_vs_position_bootstrap_20260518T083619",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "source /root/miniconda3/bin/activate && cd /root/autodl-tmp/contrastive_trace_safety/ && python3 -c \"\nimport ast, textwrap\nwith open('scripts/exp_r8_qwq_position_control.py') as f:\n    src = f.read()\n# Find the hs_windowed_features function\nidx = src.find('def hs_windowed_features')\nend = src.find('\\ndef ', idx+1)\nprint(src[idx:end])\n\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-18T08:40:49.500699+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"def hs_windowed_features(traces):\\n    \\\"\\\"\\\"Standard HS with windowing (baseline).\\\"\\\"\\\"\\n    X_list, y_list, cps = [], [], []\\n    for t in traces:\\n        hs, labels, cp = extract_raw_hs(t)\\n        feat = apply_window(hs)\\n        X_list.append(feat)\\n        y_list.append(labels)\\n        cps.append(cp)\\n    return X_list, y_list, cps\\n\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r9_qwq_hs_vs_position_bootstrap_20260518T083619",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-18T08:40:49.500889+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "source /root/miniconda3/bin/activate && cd /root/autodl-tmp/contrastive_trace_safety/ && python3 -c \"\nwith open('scripts/exp_r8_qwq_position_control.py') as f:\n    src = f.read()\nidx = src.find('def train_and_eval')\nend = src.find('\\ndef ', idx+1)\nprint(src[idx:end])\n\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r9_qwq_hs_vs_position_bootstrap_20260518T083619",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "source /root/miniconda3/bin/activate && cd /root/autodl-tmp/contrastive_trace_safety/ && python3 -c \"\nwith open('scripts/exp_r8_qwq_position_control.py') as f:\n    src = f.read()\nidx = src.find('def train_and_eval')\nend = src.find('\\ndef ', idx+1)\nprint(src[idx:end])\n\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-18T08:40:49.501091+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"def train_and_eval(X_train_list, y_train_list, X_test_list, y_test_list, cps_test, use_pca=False, label=\\\"\\\"):\\n    X_tr = np.concatenate(X_train_list)\\n    y_tr = np.concatenate(y_train_list)\\n\\n    pca = None\\n    if use_pca and X_tr.shape[1] > 1000:\\n        n_comp = min(X_tr.shape[0] - 1, X_tr.shape[1], 500)\\n        pca = PCA(n_components=n_comp, random_state=SEED)\\n        X_tr = pca.fit_transform(X_tr)\\n        print(f\\\"  [{label}] PCA: {n_comp} components, var={pca.explained_variance_ratio_.sum():.4f}\\\", flush=True)\\n\\n    print(f\\\"  [{label}] Training LR on {X_tr.shape}...\\\", flush=True)\\n    clf = LogisticRegression(C=1.0, class_weight=\\\"balanced\\\", solver=\\\"lbfgs\\\", max_iter=2000, random_state=SEED)\\n    clf.fit(X_tr, y_tr)\\n\\n    mlist = []\\n    for X_te, y_te, cp in zip(X_test_list, y_test_list, cps_test):\\n        if pca:\\n            X_te = pca.transform(X_te)\\n        probs = clf.predict_proba(X_te)[:, 1]\\n        mlist.append(per_trace_metrics(probs, y_te, cp))\\n\\n    return aggregate(mlist)\\n\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r9_qwq_hs_vs_position_bootstrap_20260518T083619",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-18T08:40:49.501357+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "source /root/miniconda3/bin/activate && cd /root/autodl-tmp/contrastive_trace_safety/ && python3 -c \"\nimport sys, json, warnings, time\nimport numpy as np\nfrom pathlib import Path\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.decomposition import PCA\nsys.path.insert(0, '/root/autodl-tmp/contrastive_trace_safety')\nwarnings.filterwarnings('ignore')\nimport torch\n\nHS_DIR = Path('/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b')\nOUT_DIR = Path('/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r9_qwq_hs_vs_position')\nOUT_DIR.mkdir(parents=True, exist_ok=True)\n\nSEED, WINDOW, LAYER_IDX, K_CONSECUTIVE, N_BOOTSTRAP = 42, 3, 60, 3, 10000\n\ndef load_traces():\n    traces = []\n    for pt_file in sorted(HS_DIR.glob('*.pt')):\n        data = torch.load(pt_file, map_location='cpu', weights_only=False)\n        if data.get('step_labels') is None or data.get('commitment_point') is None:\n            continue\n        traces.append(data)\n    return traces\n\ndef get_labels(t):\n    sl = t['step_labels']\n    return sl.tolist() if isinstance(sl, torch.Tensor) else list(sl)\n\ndef split_data(traces, seed=SEED):\n    rng = np.random.default_rng(seed)\n    idx = rng.permutation(len(traces))\n    n_tr = int(len(traces) * 0.6)\n    n_va = int(len(traces) * 0.2)\n    return ([traces[i] for i in idx[:n_tr]],\n            [traces[i] for i in idx[n_tr:n_tr + n_va]],\n            [traces[i] for i in idx[n_tr + n_va:]])\n\ndef per_trace_metrics(probs, labels, cp):\n    preds = (probs > 0.5).astype(int)\n    pre_fpr = float(preds[:cp].mean()) if cp > 0 else 0.0\n    tp = int(((preds == 1) & (labels == 1)).sum())\n    fp = int(((preds == 1) & (labels == 0)).sum())\n    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0\n    return {'precision': precision, 'pre_fpr': pre_fpr}\n\ndef apply_window(hs, window=WINDOW):\n    n, hdim = hs.shape\n    half_w = window // 2\n    padded = np.zeros((n + window - 1, hdim), dtype=np.float32)\n    padded[half_w:half_w + n] = hs\n    return np.array([padded[i:i + window].flatten() for i in range(n)])\n\ndef extract_raw_hs(trace):\n    hs = trace['hidden_states'][:, LAYER_IDX, :].float().numpy()\n    labels = np.array(get_labels(trace))\n    n = min(hs.shape[0], len(labels))\n    return hs[:n].astype(np.float32), labels[:n], int(trace['commitment_point'])\n\ndef train_probe_r8(X_list, y_list, use_pca=True):\n    \\\"\\\"\\\"Match r8 PCA logic exactly.\\\"\\\"\\\"\n    X = np.concatenate(X_list)\n    y = np.concatenate(y_list)\n    pca = None\n    if use_pca and X.shape[1] > 1000:\n        n_comp = min(X.shape[0] - 1, X.shape[1], 500)\n        pca = PCA(n_components=n_comp, random_state=SEED)\n        X = pca.fit_transform(X)\n        print(f'  PCA: {n_comp} components, var={pca.explained_variance_ratio_.sum():.4f}', flush=True)\n    print(f'  Training LR on {X.shape}...', flush=True)\n    lr = LogisticRegression(C=1.0, class_weight='balanced', solver='lbfgs', max_iter=2000, random_state=SEED)\n    lr.fit(X, y)\n    return lr, pca\n\ndef predict_trace(lr, pca, X):\n    if pca is not None:\n        X = pca.transform(X)\n    return lr.predict_proba(X)[:, 1]\n\ndef bootstrap_paired(diffs, n_bootstrap=N_BOOTSTRAP, seed=SEED):\n    rng = np.random.default_rng(seed)\n    n = len(diffs)\n    observed_mean = np.mean(diffs)\n    centered = diffs - observed_mean\n    boot_null = np.array([np.mean(centered[rng.integers(0, n, size=n)]) for _ in range(n_bootstrap)])\n    p_value = float(np.mean(boot_null >= observed_mean))\n    boot_raw = np.array([np.mean(diffs[rng.integers(0, n, size=n)]) for _ in range(n_bootstrap)])\n    ci_lo, ci_hi = float(np.percentile(boot_raw, 2.5)), float(np.percentile(boot_raw, 97.5))\n    return observed_mean, ci_lo, ci_hi, p_value\n\nt_start = time.time()\ntraces = load_traces()\ntrain, val, test = split_data(traces)\nprint(f'Loaded {len(traces)} traces, train={len(train)}, test={len(test)}', flush=True)\n\n# HS probe (train only, matching r8)\nprint('\\n=== HS probe ===', flush=True)\nX_tr_hs, y_tr_hs = [], []\nfor t in train:\n    hs, labels, cp = extract_raw_hs(t)\n    X_tr_hs.append(apply_window(hs))\n    y_tr_hs.append(labels)\nlr_hs, pca_hs = train_probe_r8(X_tr_hs, y_tr_hs, use_pca=True)\n\n# Position probe (train only, matching r8)\nprint('\\n=== Position probe ===', flush=True)\nX_tr_pos, y_tr_pos = [], []\nfor t in train:\n    hs, labels, cp = extract_raw_hs(t)\n    T = len(hs)\n    norm = np.arange(T, dtype=np.float32) / T\n    half_w = WINDOW // 2\n    padded = np.zeros(T + WINDOW - 1, dtype=np.float32)\n    padded[half_w:half_w + T] = norm\n    X_tr_pos.append(np.array([padded[i:i + WINDOW] for i in range(T)]))\n    y_tr_pos.append(labels)\nlr_pos, pca_pos = train_probe_r8(X_tr_pos, y_tr_pos, use_pca=False)\n\n# Per-trace on test\nhs_prec, hs_fpr, pos_prec, pos_fpr = [], [], [], []\nfor i, t in enumerate(test):\n    hs, labels, cp = extract_raw_hs(t)\n    T = len(hs)\n    probs_hs = predict_trace(lr_hs, pca_hs, apply_window(hs))\n    m_hs = per_trace_metrics(probs_hs, labels, cp)\n    norm = np.arange(T, dtype=np.float32) / T\n    half_w = WINDOW // 2\n    padded = np.zeros(T + WINDOW - 1, dtype=np.float32)\n    padded[half_w:half_w + T] = norm\n    feat_pos = np.array([padded[j:j + WINDOW] for j in range(T)])\n    probs_pos = predict_trace(lr_pos, pca_pos, feat_pos)\n    m_pos = per_trace_metrics(probs_pos, labels, cp)\n    hs_prec.append(m_hs['precision']); hs_fpr.append(m_hs['pre_fpr'])\n    pos_prec.append(m_pos['precision']); pos_fpr.append(m_pos['pre_fpr'])\n\nhs_prec, hs_fpr = np.array(hs_prec), np.array(hs_fpr)\npos_prec, pos_fpr = np.array(pos_prec), np.array(pos_fpr)\n\nprint(f'\\nAggregate: HS prec={hs_prec.mean():.4f} fpr={hs_fpr.mean():.4f} | Pos prec={pos_prec.mean():.4f} fpr={pos_fpr.mean():.4f}', flush=True)\n\n# Bootstrap\nprint(f'\\nBootstrap ({N_BOOTSTRAP} resamples)...', flush=True)\nprec_mean, prec_lo, prec_hi, prec_p = bootstrap_paired(hs_prec - pos_prec)\nfpr_mean, fpr_lo, fpr_hi, fpr_p = bootstrap_paired(pos_fpr - hs_fpr)\n\nelapsed = time.time() - t_start\nprint('\\n' + '='*75, flush=True)\nprint('QwQ-32B HS vs Position (L60, W=3) - Paired Bootstrap', flush=True)\nprint('='*75, flush=True)\nhdr = f'{\\\"Metric\\\":<12} {\\\"HS\\\":>8} {\\\"Position\\\":>10} {\\\"Delta\\\":>8} {\\\"95% CI\\\":>20} {\\\"p-value\\\":>10}'\nprint(hdr, flush=True)\nprint('-'*70, flush=True)\nprint(f'{\\\"precision\\\":<12} {hs_prec.mean():>8.4f} {pos_prec.mean():>10.4f} {prec_mean:>+8.4f} [{prec_lo:>+.4f}, {prec_hi:>+.4f}] {prec_p:>10.4f}', flush=True)\nprint(f'{\\\"FPR\\\":<12} {hs_fpr.mean():>8.4f} {pos_fpr.mean():>10.4f} {fpr_mean:>+8.4f} [{fpr_lo:>+.4f}, {fpr_hi:>+.4f}] {fpr_p:>10.4f}', flush=True)\nprint(f'\\nN_test={len(test)}, N_bootstrap={N_BOOTSTRAP}, elapsed={elapsed:.1f}s', flush=True)\n\nresults = {\n    'experiment': 'exp_r9_qwq_hs_vs_position',\n    'model': 'QwQ-32B', 'layer': LAYER_IDX, 'window': WINDOW,\n    'seed': SEED, 'k_consecutive': K_CONSECUTIVE,\n    'n_bootstrap': N_BOOTSTRAP, 'n_test': len(test), 'n_train': len(train),\n    'pca_components': pca_hs.n_components_ if pca_hs else None,\n    'per_trace': {\n        'hs_precisions': hs_prec.tolist(), 'hs_fprs': hs_fpr.tolist(),\n        'pos_precisions': pos_prec.tolist(), 'pos_fprs': pos_fpr.tolist(),\n    },\n    'precision': {\n        'hs': float(hs_prec.mean()), 'position': float(pos_prec.mean()),\n        'delta': float(prec_mean), 'ci_95': [prec_lo, prec_hi], 'p_value': prec_p,\n    },\n    'fpr': {\n        'hs': float(hs_fpr.mean()), 'position': float(pos_fpr.mean()),\n        'delta': float(fpr_mean), 'ci_95': [fpr_lo, fpr_hi], 'p_value': fpr_p,\n    },\n    'elapsed_seconds': round(elapsed, 1),\n}\nwith open(OUT_DIR / 'results.json', 'w') as f:\n    json.dump(results, f, indent=2)\nprint(f'\\nSaved to {OUT_DIR}/results.json', flush=True)\n\"",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r9_qwq_hs_vs_position_bootstrap_20260518T083619",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "source /root/miniconda3/bin/activate && cd /root/autodl-tmp/contrastive_trace_safety/ && python3 -c \"\nimport sys, json, warnings, time\nimport numpy as np\nfrom pathlib import Path\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.decomposition import PCA\nsys.path.insert(0, '/root/autodl-tmp/contrastive_trace_safety')\nwarnings.filterwarnings('ignore')\nimport torch\n\nHS_DIR = Path('/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b')\nOUT_DIR = Path('/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r9_qwq_hs_vs_position')\nOUT_DIR.mkdir(parents=True, exist_ok=True)\n\nSEED, WINDOW, LAYER_IDX, K_CONSECUTIVE, N_BOOTSTRAP = 42, 3, 60, 3, 10000\n\ndef load_traces():\n    traces = []\n    for pt_file in sorted(HS_DIR.glob('*.pt')):\n        data = torch.load(pt_file, map_location='cpu', weights_only=False)\n        if data.get('step_labels') is None or data.get('commitment_point') is None:\n            continue\n        traces.append(data)\n    return traces\n\ndef get_labels(t):\n    sl = t['step_labels']\n    return sl.tolist() if isinstance(sl, torch.Tensor) else list(sl)\n\ndef split_data(traces, seed=SEED):\n    rng = np.random.default_rng(seed)\n    idx = rng.permutation(len(traces))\n    n_tr = int(len(traces) * 0.6)\n    n_va = int(len(traces) * 0.2)\n    return ([traces[i] for i in idx[:n_tr]],\n            [traces[i] for i in idx[n_tr:n_tr + n_va]],\n            [traces[i] for i in idx[n_tr + n_va:]])\n\ndef per_trace_metrics(probs, labels, cp):\n    preds = (probs > 0.5).astype(int)\n    pre_fpr = float(preds[:cp].mean()) if cp > 0 else 0.0\n    tp = int(((preds == 1) & (labels == 1)).sum())\n    fp = int(((preds == 1) & (labels == 0)).sum())\n    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0\n    return {'precision': precision, 'pre_fpr': pre_fpr}\n\ndef apply_window(hs, window=WINDOW):\n    n, hdim = hs.shape\n    half_w = window // 2\n    padded = np.zeros((n + window - 1, hdim), dtype=np.float32)\n    padded[half_w:half_w + n] = hs\n    return np.array([padded[i:i + window].flatten() for i in range(n)])\n\ndef extract_raw_hs(trace):\n    hs = trace['hidden_states'][:, LAYER_IDX, :].float().numpy()\n    labels = np.array(get_labels(trace))\n    n = min(hs.shape[0], len(labels))\n    return hs[:n].astype(np.float32), labels[:n], int(trace['commitment_point'])\n\ndef train_probe_r8(X_list, y_list, use_pca=True):\n    \\\"\\\"\\\"Match r8 PCA logic exactly.\\\"\\\"\\\"\n    X = np.concatenate(X_list)\n    y = np.concatenate(y_list)\n    pca = None\n    if use_pca and X.shape[1] > 1000:\n        n_comp = min(X.shape[0] - 1, X.shape[1], 500)\n        pca = PCA(n_components=n_comp, random_state=SEED)\n        X = pca.fit_transform(X)\n        print(f'  PCA: {n_comp} components, var={pca.explained_variance_ratio_.sum():.4f}', flush=True)\n    print(f'  Training LR on {X.shape}...', flush=True)\n    lr = LogisticRegression(C=1.0, class_weight='balanced', solver='lbfgs', max_iter=2000, random_state=SEED)\n    lr.fit(X, y)\n    return lr, pca\n\ndef predict_trace(lr, pca, X):\n    if pca is not None:\n        X = pca.transform(X)\n    return lr.predict_proba(X)[:, 1]\n\ndef bootstrap_paired(diffs, n_bootstrap=N_BOOTSTRAP, seed=SEED):\n    rng = np.random.default_rng(seed)\n    n = len(diffs)\n    observed_mean = np.mean(diffs)\n    centered = diffs - observed_mean\n    boot_null = np.array([np.mean(centered[rng.integers(0, n, size=n)]) for _ in range(n_bootstrap)])\n    p_value = float(np.mean(boot_null >= observed_mean))\n    boot_raw = np.array([np.mean(diffs[rng.integers(0, n, size=n)]) for _ in range(n_bootstrap)])\n    ci_lo, ci_hi = float(np.percentile(boot_raw, 2.5)), float(np.percentile(boot_raw, 97.5))\n    return observed_mean, ci_lo, ci_hi, p_value\n\nt_start = time.time()\ntraces = load_traces()\ntrain, val, test = split_data(traces)\nprint(f'Loaded {len(traces)} traces, train={len(train)}, test={len(test)}', flush=True)\n\n# HS probe (train only, matching r8)\nprint('\\n=== HS probe ===', flush=True)\nX_tr_hs, y_tr_hs = [], []\nfor t in train:\n    hs, labels, cp = extract_raw_hs(t)\n    X_tr_hs.append(apply_window(hs))\n    y_tr_hs.append(labels)\nlr_hs, pca_hs = train_probe_r8(X_tr_hs, y_tr_hs, use_pca=True)\n\n# Position probe (train only, matching r8)\nprint('\\n=== Position probe ===', flush=True)\nX_tr_pos, y_tr_pos = [], []\nfor t in train:\n    hs, labels, cp = extract_raw_hs(t)\n    T = len(hs)\n    norm = np.arange(T, dtype=np.float32) / T\n    half_w = WINDOW // 2\n    padded = np.zeros(T + WINDOW - 1, dtype=np.float32)\n    padded[half_w:half_w + T] = norm\n    X_tr_pos.append(np.array([padded[i:i + WINDOW] for i in range(T)]))\n    y_tr_pos.append(labels)\nlr_pos, pca_pos = train_probe_r8(X_tr_pos, y_tr_pos, use_pca=False)\n\n# Per-trace on test\nhs_prec, hs_fpr, pos_prec, pos_fpr = [], [], [], []\nfor i, t in enumerate(test):\n    hs, labels, cp = extract_raw_hs(t)\n    T = len(hs)\n    probs_hs = predict_trace(lr_hs, pca_hs, apply_window(hs))\n    m_hs = per_trace_metrics(probs_hs, labels, cp)\n    norm = np.arange(T, dtype=np.float32) / T\n    half_w = WINDOW // 2\n    padded = np.zeros(T + WINDOW - 1, dtype=np.float32)\n    padded[half_w:half_w + T] = norm\n    feat_pos = np.array([padded[j:j + WINDOW] for j in range(T)])\n    probs_pos = predict_trace(lr_pos, pca_pos, feat_pos)\n    m_pos = per_trace_metrics(probs_pos, labels, cp)\n    hs_prec.append(m_hs['precision']); hs_fpr.append(m_hs['pre_fpr'])\n    pos_prec.append(m_pos['precision']); pos_fpr.append(m_pos['pre_fpr'])\n\nhs_prec, hs_fpr = np.array(hs_prec), np.array(hs_fpr)\npos_prec, pos_fpr = np.array(pos_prec), np.array(pos_fpr)\n\nprint(f'\\nAggregate: HS prec={hs_prec.mean():.4f} fpr={hs_fpr.mean():.4f} | Pos prec={pos_prec.mean():.4f} fpr={pos_fpr.mean():.4f}', flush=True)\n\n# Bootstrap\nprint(f'\\nBootstrap ({N_BOOTSTRAP} resamples)...', flush=True)\nprec_mean, prec_lo, prec_hi, prec_p = bootstrap_paired(hs_prec - pos_prec)\nfpr_mean, fpr_lo, fpr_hi, fpr_p = bootstrap_paired(pos_fpr - hs_fpr)\n\nelapsed = time.time() - t_start\nprint('\\n' + '='*75, flush=True)\nprint('QwQ-32B HS vs Position (L60, W=3) - Paired Bootstrap', flush=True)\nprint('='*75, flush=True)\nhdr = f'{\\\"Metric\\\":<12} {\\\"HS\\\":>8} {\\\"Position\\\":>10} {\\\"Delta\\\":>8} {\\\"95% CI\\\":>20} {\\\"p-value\\\":>10}'\nprint(hdr, flush=True)\nprint('-'*70, flush=True)\nprint(f'{\\\"precision\\\":<12} {hs_prec.mean():>8.4f} {pos_prec.mean():>10.4f} {prec_mean:>+8.4f} [{prec_lo:>+.4f}, {prec_hi:>+.4f}] {prec_p:>10.4f}', flush=True)\nprint(f'{\\\"FPR\\\":<12} {hs_fpr.mean():>8.4f} {pos_fpr.mean():>10.4f} {fpr_mean:>+8.4f} [{fpr_lo:>+.4f}, {fpr_hi:>+.4f}] {fpr_p:>10.4f}', flush=True)\nprint(f'\\nN_test={len(test)}, N_bootstrap={N_BOOTSTRAP}, elapsed={elapsed:.1f}s', flush=True)\n\nresults = {\n    'experiment': 'exp_r9_qwq_hs_vs_position',\n    'model': 'QwQ-32B', 'layer': LAYER_IDX, 'window': WINDOW,\n    'seed': SEED, 'k_consecutive': K_CONSECUTIVE,\n    'n_bootstrap': N_BOOTSTRAP, 'n_test': len(test), 'n_train': len(train),\n    'pca_components': pca_hs.n_components_ if pca_hs else None,\n    'per_trace': {\n        'hs_precisions': hs_prec.tolist(), 'hs_fprs': hs_fpr.tolist(),\n        'pos_precisions': pos_prec.tolist(), 'pos_fprs': pos_fpr.tolist(),\n    },\n    'precision': {\n        'hs': float(hs_prec.mean()), 'position': float(pos_prec.mean()),\n        'delta': float(prec_mean), 'ci_95': [prec_lo, prec_hi], 'p_value': prec_p,\n    },\n    'fpr': {\n        'hs': float(hs_fpr.mean()), 'position': float(pos_fpr.mean()),\n        'delta': float(fpr_mean), 'ci_95': [fpr_lo, fpr_hi], 'p_value': fpr_p,\n    },\n    'elapsed_seconds': round(elapsed, 1),\n}\nwith open(OUT_DIR / 'results.json', 'w') as f:\n    json.dump(results, f, indent=2)\nprint(f'\\nSaved to {OUT_DIR}/results.json', flush=True)\n\"",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-18T08:40:49.501675+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Loaded 95 traces, train=57, test=19\\n\\n=== HS probe ===\\n  PCA: 500 components, var=0.8418\\n  Training LR on (2881, 500)...\\n\\n=== Position probe ===\\n  Training LR on (2881, 3)...\\n\\nAggregate: HS prec=0.5640 fpr=0.2165 | Pos prec=0.5192 fpr=0.2414\\n\\nBootstrap (10000 resamples)...\\n\\n===========================================================================\\nQwQ-32B HS vs Position (L60, W=3) - Paired Bootstrap\\n===========================================================================\\nMetric             HS   Position    Delta               95% CI    p-value\\n----------------------------------------------------------------------\\nprecision      0.5640     0.5192  +0.0448 [-0.0321, +0.1275]     0.1325\\nFPR            0.2165     0.2414  +0.0249 [-0.0606, +0.1104]     0.2792\\n\\nN_test=19, N_bootstrap=10000, elapsed=5.5s\\n\\nSaved to /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r9_qwq_hs_vs_position/results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.54}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r9_qwq_hs_vs_position_bootstrap_20260518T083619",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-18T08:40:49.501947+00:00_

Aggregates now match exactly (HS precision=0.5640, FPR=0.2165; Position precision=0.5192, FPR=0.2414). Results saved.

```
QwQ-32B HS vs Position (L60, W=3) - Paired Bootstrap (10k resamples, n=19):
| Metric    | HS     | Position | Δ       | 95% CI              | p-value |
|-----------|--------|----------|---------|---------------------|---------|
| precision | 0.5640 | 0.5192   | +0.0448 | [-0.0321, +0.1275]  | 0.1325  |
| FPR       | 0.2165 | 0.2414   | +0.0249 | [-0.0606, +0.1104]  | 0.2792  |
```

Both differences are **not statistically significant** (precision p=0.133, FPR p=0.279). The 95% CIs span zero in both cases. With only 19 test traces, the HS probe's +4.5pp precision advantage and +2.5pp FPR advantage over position-only are directionally consistent but lack statistical power to reject the null.

Saved to `artifacts/exp_r9_qwq_hs_vs_position/results.json` (includes per-trace arrays for further analysis).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_r9_qwq_hs_vs_position_bootstrap_20260518T083619"
}
```

</details>

---
