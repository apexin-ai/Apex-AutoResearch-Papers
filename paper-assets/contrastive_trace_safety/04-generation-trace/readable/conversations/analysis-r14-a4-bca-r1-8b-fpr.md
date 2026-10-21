# analysis r14 a4 bca r1 8b fpr

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 0
- **Tool calls:** 17
- **Original source:** `logs/chats/worker_analysis_r14_a4_bca_r1_8b_fpr_20260518T162942.jsonl`
- **Structured JSON:** [`7d4be75465c46c5578cd.json`](../../sessions/7d/7d4be75465c46c5578cd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

35 recorded events

### Tool call

_source line 1 · 2026-05-18T16:33:56.414325+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__detect_image",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r14_a4_bca_r1_8b_fpr_20260518T162942",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__detect_image",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-18T16:33:56.414694+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r14_a4_bca_r1_8b_fpr_20260518T162942",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T16:33:56.414905+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "ls /root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states/ && echo \"---\" && ls /root/autodl-tmp/contrastive_trace_safety/src/ 2>/dev/null || echo \"no src dir\" && echo \"---\" && find /root/autodl-tmp/contrastive_trace_safety/ -name \"*.py\" -path \"*/r14*\" 2>/dev/null | head -20 && echo \"---\" && find /root/autodl-tmp/contrastive_trace_safety/ -name \"*.py\" | grep -i \"bootstrap\\|fpr\\|hotelling\\|split\" | head -20",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r14_a4_bca_r1_8b_fpr_20260518T162942",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "ls /root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states/ && echo \"---\" && ls /root/autodl-tmp/contrastive_trace_safety/src/ 2>/dev/null || echo \"no src dir\" && echo \"---\" && find /root/autodl-tmp/contrastive_trace_safety/ -name \"*.py\" -path \"*/r14*\" 2>/dev/null | head -20 && echo \"---\" && find /root/autodl-tmp/contrastive_trace_safety/ -name \"*.py\" | grep -i \"bootstrap\\|fpr\\|hotelling\\|split\" | head -20",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-18T16:33:56.415161+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"008edcde3b3d48dcaee8313c4779f687.pt\\n018ad1b2027a488aad4ce925258db0c7.pt\\n02361be96b4e4f11af5524a64c34f612.pt\\n023c413259524b2187989e61d96e351c.pt\\n02fad27f069d4009861ea612984ab65c.pt\\n0334a1be1cc84efc853bd93eb5327499.pt\\n03a149305aae4ed58d62489ed1f66329.pt\\n04e287adbc58415cb184c3db0ac3d8c5.pt\\n0516bc55867f4454966f3ecfd6cd85c5.pt\\n051a975475d7420d99f686fe89e83691.pt\\n05e1498f8ff741718f500af3772def28.pt\\n0601b6d225274449bcfcca10af190a9a.pt\\n06470bdf141a4267b541332987c6f695.pt\\n06d85d8b941f4a4e97dc7f33c81c34c4.pt\\n0828a2af61e846f1aea6a834017ec7be.pt\\n0901d657f92b441e8cac21db87d066e5.pt\\n0a31d31d974b410eb923f33cfbf6e6b9.pt\\n0c9c5e6cf60849bb925d007dd2b061fc.pt\\n0d13aa7b2f374a3fa367bdea42493ed5.pt\\n0d19422cc82743568f671961b534c215.pt\\n0d8b146a9bce48f7a8083f6ed962664e.pt\\n0daf036448c04433859bdf6758495bc3.pt\\n0f35040637024040b7944abd48472d22.pt\\n0f6bdcb1133f442ba26e11047e5351c6.pt\\n0f860c71503e43c985eafc0142546731.pt\\n10a2a6c355d4408ab97b759b490a6a8b.pt\\n10a3ace02006485ca641aaa88684b5dd.pt\\n10e4c756140247b4af10559f16d8f876.pt\\n114499174dfa48daa5e053c629c83a10.pt\\n116042e8dc164c17b02d5670b015f807.pt\\n11a094cbf15549bca819c57910c2a2ff.pt\\n11c4c8713262422eb211ec189c3715ab.pt\\n11f61793e9b449e799abe7ce14cbcf6c.pt\\n1249b76a00da42b8be3aa81d823cd820.pt\\n130e2b41b4bf43f883f087b5036afe85.pt\\n13258d4ff6e04f67b9510328b89251ea.pt\\n1362fe58c432487aac432b576babe0c2.pt\\n13b5b2b441534e818b1a2d2f577cb99c.pt\\n153e58ce7b554163a43030ecfa47a304.pt\\n1582380f856b429490eca59328ce551d.pt\\n15e5e40e8ddc475594dce89bc52c9056.pt\\n16015e85a86d4ad6aae05eda39472b0a.pt\\n16d9dd7bb2484ec19ed11d44fb46af7f.pt\\n177c234e76104e7b9f2858bdd71f4963.pt\\n17a5d38bd028469aad6f4cb0304c7e01.pt\\n17d1d68121644dec87c3bb936abfb615.pt\\n181e5d60e4f1457fb60796052713110b.pt\\n18ca23538f9d4c3faa4cb9c4e2ec4c2d.pt\\n196b722aadd6473f9ce6795294f9a88a.pt\\n1a27d43f250e4201bb0099ae23551974.pt\\n1a2bca42efbd45458fe50b6a6b44242f.pt\\n1af63c
…[truncated 6617 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r14_a4_bca_r1_8b_fpr_20260518T162942",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T16:33:56.415351+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "cat /root/autodl-tmp/contrastive_trace_safety/src/experiments/r1_8b_bootstrap_hs_text.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r14_a4_bca_r1_8b_fpr_20260518T162942",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "cat /root/autodl-tmp/contrastive_trace_safety/src/experiments/r1_8b_bootstrap_hs_text.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-18T16:33:56.415667+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"r1-8b: Pre-CP FPR Paired Bootstrap Test - HS probe vs Text probe.\\\"\\\"\\\"\\n\\nimport os, sys, json\\nos.environ[\\\"TOKENIZERS_PARALLELISM\\\"] = \\\"false\\\"\\nos.environ[\\\"HF_ENDPOINT\\\"] = \\\"https://hf-mirror.com\\\"\\n\\nimport numpy as np\\nimport torch\\nfrom sklearn.linear_model import LogisticRegression\\nfrom pathlib import Path\\n\\nsys.path.insert(0, \\\"/root/autodl-tmp/contrastive_trace_safety\\\")\\nfrom src.data_loader import load_harmthoughts, extract_commitment_point, create_step_labels\\nfrom src.config import SAFETY_LABELS\\n\\nHS_DIR = Path(\\\"/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states\\\")\\nOUTPUT_DIR = Path(\\\"/root/autodl-tmp/contrastive_trace_safety/artifacts/r1_8b_bootstrap_hs_text\\\")\\nHIDDEN_DIM = 4096\\nTEXT_DIM = 384\\nLAYER_IDX = 2  # Layer 14 = LAYERS[2] in stored tensors (LAYERS starts at 12)\\nWINDOW_SIZE = 15\\nSEED = 42\\n\\n\\ndef load_traces_with_sentences():\\n    print(\\\"Loading HarmThoughts dataset (r1-8b)...\\\")\\n    raw_traces = load_harmthoughts(\\\"r1-8b\\\")\\n\\n    traces = []\\n    for trace_id, steps in raw_traces.items():\\n        is_jailbreak = steps[0][\\\"final_judgment\\\"] == 1.0\\n        if not is_jailbreak:\\n            continue\\n        labels = [s[\\\"label\\\"] for s in steps]\\n        cp = extract_commitment_point(labels)\\n        if cp is None:\\n            continue\\n\\n        hs_path = HS_DIR / f\\\"{trace_id}.pt\\\"\\n        if not hs_path.exists():\\n            continue\\n\\n        sentences = [s[\\\"sentence\\\"] for s in steps]\\n        step_labels = create_step_labels(cp, len(sentences))\\n\\n        hs_data = torch.load(hs_path, map_location=\\\"cpu\\\", weights_only=False)\\n\\n        traces.append({\\n            \\\"trace_id\\\": trace_id,\\n            \\\"sentences\\\": sentences,\\n            \\\"hidden_states\\\": hs_data[\\\"hidden_states\\\"],\\n            \\\"comm
…[truncated 7107 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r14_a4_bca_r1_8b_fpr_20260518T162942",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-18T16:33:56.415846+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "cat /root/autodl-tmp/contrastive_trace_safety/artifacts/r1_8b_bootstrap_hs_text/results.json 2>/dev/null | python3 -c \"import sys,json; d=json.load(sys.stdin); print('hs_fpr:', d['hs_precp_fpr_mean']); print('text_fpr:', d['text_precp_fpr_mean']); print('diff:', d['difference_mean']); print('p:', d['p_value']); print('ci:', d['difference_ci_95']); print('n_traces:', d['n_traces_test']); print('n_hs_fprs:', len(d['per_trace_hs_fprs'])); print('n_text_fprs:', len(d['per_trace_text_fprs']))\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r14_a4_bca_r1_8b_fpr_20260518T162942",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "cat /root/autodl-tmp/contrastive_trace_safety/artifacts/r1_8b_bootstrap_hs_text/results.json 2>/dev/null | python3 -c \"import sys,json; d=json.load(sys.stdin); print('hs_fpr:', d['hs_precp_fpr_mean']); print('text_fpr:', d['text_precp_fpr_mean']); print('diff:', d['difference_mean']); print('p:', d['p_value']); print('ci:', d['difference_ci_95']); print('n_traces:', d['n_traces_test']); print('n_hs_fprs:', len(d['per_trace_hs_fprs'])); print('n_text_fprs:', len(d['per_trace_text_fprs']))\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-18T16:33:56.415997+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cat /root/autodl-tmp/contrastive_trace_safety/artifacts/r1_8b_bootstrap_hs_text/results.json 2>/dev/null | python3 -c \\\"import sys,json; d=json.load(sys.stdin); print(\\\\'hs_fpr:\\\\', d[\\\\'hs_precp_fpr_mean\\\\']); print(\\\\'text_fpr:\\\\', d[\\\\'text_precp_fpr_mean\\\\']); print(\\\\'diff:\\\\', d[\\\\'difference_mean\\\\']); print(\\\\'p:\\\\', d[\\\\'p_value\\\\']); print(\\\\'ci:\\\\', d[\\\\'difference_ci_95\\\\']); print(\\\\'n_traces:\\\\', d[\\\\'n_traces_test\\\\']); print(\\\\'n_hs_fprs:\\\\', len(d[\\\\'per_trace_hs_fprs\\\\'])); print(\\\\'n_text_fprs:\\\\', len(d[\\\\'per_trace_text_fprs\\\\']))\\\"'\\n\\nExit code: 127\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 1: python3: command not found\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r14_a4_bca_r1_8b_fpr_20260518T162942",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T16:33:56.416133+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "cat /root/autodl-tmp/contrastive_trace_safety/artifacts/r1_8b_bootstrap_hs_text/results.json 2>/dev/null | /root/miniconda3/bin/python3.12 -c \"import sys,json; d=json.load(sys.stdin); print('hs_fpr:', d['hs_precp_fpr_mean']); print('text_fpr:', d['text_precp_fpr_mean']); print('diff:', d['difference_mean']); print('p:', d['p_value']); print('ci:', d['difference_ci_95']); print('n_traces:', d['n_traces_test']); print('n_hs_fprs:', len(d['per_trace_hs_fprs'])); print('n_text_fprs:', len(d['per_trace_text_fprs']))\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r14_a4_bca_r1_8b_fpr_20260518T162942",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "cat /root/autodl-tmp/contrastive_trace_safety/artifacts/r1_8b_bootstrap_hs_text/results.json 2>/dev/null | /root/miniconda3/bin/python3.12 -c \"import sys,json; d=json.load(sys.stdin); print('hs_fpr:', d['hs_precp_fpr_mean']); print('text_fpr:', d['text_precp_fpr_mean']); print('diff:', d['difference_mean']); print('p:', d['p_value']); print('ci:', d['difference_ci_95']); print('n_traces:', d['n_traces_test']); print('n_hs_fprs:', len(d['per_trace_hs_fprs'])); print('n_text_fprs:', len(d['per_trace_text_fprs']))\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-18T16:33:56.416266+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"hs_fpr: 0.1483665597701362\\ntext_fpr: 0.22192538830579658\\ndiff: -0.07355882853566037\\np: 0.044\\nci: [-0.15581308843147962, -0.0035979738892938417]\\nn_traces: 43\\nn_hs_fprs: 43\\nn_text_fprs: 43\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.94}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r14_a4_bca_r1_8b_fpr_20260518T162942",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T16:33:56.416423+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "/root/miniconda3/bin/python3.12 -c \"import scipy; print(scipy.__version__); from scipy.stats import bootstrap; print('bootstrap available')\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r14_a4_bca_r1_8b_fpr_20260518T162942",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "/root/miniconda3/bin/python3.12 -c \"import scipy; print(scipy.__version__); from scipy.stats import bootstrap; print('bootstrap available')\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-18T16:33:56.416569+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"1.17.1\\nbootstrap available\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.2}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r14_a4_bca_r1_8b_fpr_20260518T162942",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T16:33:56.416750+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "/root/miniconda3/bin/python3.12 -c \"\nfrom scipy.stats import bootstrap\nimport inspect\nsig = inspect.signature(bootstrap)\nprint(sig)\n# Check if method='BCa' is supported\nhelp_text = bootstrap.__doc__\nfor line in help_text.split('\\n'):\n    if 'method' in line.lower() or 'bca' in line.lower() or 'BCa' in line:\n        print(line)\n\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r14_a4_bca_r1_8b_fpr_20260518T162942",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "/root/miniconda3/bin/python3.12 -c \"\nfrom scipy.stats import bootstrap\nimport inspect\nsig = inspect.signature(bootstrap)\nprint(sig)\n# Check if method='BCa' is supported\nhelp_text = bootstrap.__doc__\nfor line in help_text.split('\\n'):\n    if 'method' in line.lower() or 'bca' in line.lower() or 'BCa' in line:\n        print(line)\n\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-18T16:33:56.416905+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"(data, statistic, *, n_resamples=9999, batch=None, vectorized=None, paired=False, axis=0, confidence_level=0.95, alternative='two-sided', method='BCa', bootstrap_result=None, rng=None, random_state=None)\\nWhen `method` is ``'percentile'`` and `alternative` is ``'two-sided'``,\\nWhile the ``'percentile'`` method is the most intuitive, it is rarely\\nused in practice. Two more common methods are available, ``'basic'``\\n('reverse percentile') and ``'BCa'`` ('bias-corrected and accelerated');\\n    (or ``batch = max(n_resamples, n)`` for ``method='BCa'``).\\nmethod : {'percentile', 'basic', 'bca'}, default: ``'BCa'``\\n    confidence interval (``'BCa'``).\\n    `confidence_level`, change `method`, or see the effect of performing\\n    Generated when ``method='BCa'`` and the bootstrap distribution is\\nElements of the confidence interval may be NaN for ``method='BCa'`` if\\nIn this case, consider using another `method` or inspecting `data` for\\nHere, we use the 'percentile' method with the default 95% confidence level.\\n>>> res = bootstrap(data, my_statistic, method='basic', rng=rng)\\n...                  method='percentile', confidence_level=0.9)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.61}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r14_a4_bca_r1_8b_fpr_20260518T162942",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-18T16:33:56.417141+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "cat > /root/autodl-tmp/contrastive_trace_safety/scripts/a4_bca_fpr.py << 'PYEOF'\n\"\"\"A4: BCa bootstrap CI + leave-one-out/leave-two-out sensitivity for R1-8B FPR.\"\"\"\n\nimport json, os, time\nimport numpy as np\nfrom scipy.stats import bootstrap, norm\nfrom pathlib import Path\nfrom itertools import combinations\n\nRESULTS_PATH = Path(\"/root/autodl-tmp/contrastive_trace_safety/artifacts/r1_8b_bootstrap_hs_text/results.json\")\nOUTPUT_DIR = Path(\"/root/autodl-tmp/contrastive_trace_safety/artifacts/r14_a4_bca_fpr\")\nOUTPUT_DIR.mkdir(parents=True, exist_ok=True)\n\nSEED = 42\nN_RESAMPLES_BCA = 10000\nN_RESAMPLES_LOO = 1000\n\n# Load per-trace FPR arrays\nwith open(RESULTS_PATH) as f:\n    data = json.load(f)\n\nhs_fprs = np.array(data[\"per_trace_hs_fprs\"])\ntext_fprs = np.array(data[\"per_trace_text_fprs\"])\nn = len(hs_fprs)\nassert n == 43, f\"Expected 43 traces, got {n}\"\n\n# ΔFPR = text_FPR - HS_FPR (positive means text has higher FPR = worse)\ndelta_fpr = text_fprs - hs_fprs\nobserved_mean = np.mean(delta_fpr)\n\nprint(f\"n = {n} test traces\")\nprint(f\"HS FPR mean:   {np.mean(hs_fprs):.4f}\")\nprint(f\"Text FPR mean: {np.mean(text_fprs):.4f}\")\nprint(f\"ΔFPR mean (text - HS): {observed_mean:.4f}\")\nprint()\n\n# ============================================================\n# Part 1: BCa bootstrap CI via scipy.stats.bootstrap\n# ============================================================\nprint(\"=\" * 60)\nprint(\"Part 1: BCa Bootstrap CI\")\nprint(\"=\" * 60)\n\ndef mean_stat(x, axis):\n    return np.mean(x, axis=axis)\n\nrng = np.random.default_rng(SEED)\nbca_result = bootstrap(\n    (delta_fpr,),\n    statistic=mean_stat,\n    n_resamples=N_RESAMPLES_BCA,\n    method='BCa',\n    confidence_level=0.95,\n    alternative='two-sided',\n    rng=rng,\n)\n\nbca_ci_low = float(bca_result.confidence_interval.low)\nbca_ci_high = float(bca_result.confidence_interval.high)\ncontains_zero = (bca_ci_low <= 0 <= bca_ci_high)\n\nprint(f\"BCa 95% CI for ΔFPR (text - HS): [{bca_ci_low:.6f}, {bca_ci_high:.6f}]\")\nprint(f\"Contains 0: {'Yes' if contains_zero else 'No'}\")\n\n# Manual BCa computation for z0 and acceleration, and BCa p-value\nboot_means = bca_result.bootstrap_distribution\nz0_prop = np.mean(boot_means < observed_mean)\nz0 = float(norm.ppf(z0_prop))\nprint(f\"BCa z0 (bias correction): {z0:.4f} (prop below observed: {z0_prop:.4f})\")\n\n# Jackknife for acceleration constant\njackknife_means = np.zeros(n)\nfor i in range(n):\n    jackknife_means[i] = np.mean(np.delete(delta_fpr, i))\njack_mean = np.mean(jackknife_means)\ninfluence = jack_mean - jackknife_means\nnum = np.sum(influence**3)\nden = 6.0 * (np.sum(influence**2))**(1.5)\nacceleration = float(num / den) if den != 0 else 0.0\nprint(f\"BCa acceleration constant a: {acceleration:.6f}\")\n\n# BCa p-value: fraction of bootstrap distribution <= 0, adjusted by BCa\n# Standard bootstrap p-value (proportion of bootstrap means <= 0)\nboot_p_percentile = float(np.mean(boot_means <= 0))\nprint(f\"Percentile bootstrap p-value (ΔFPR <= 0): {boot_p_percentile:.4f}\")\n\n# BCa-adjusted p-value\n# P(ΔFPR <= 0): find where 0 sits in BCa-adjusted distribution\n# z_test = Φ^{-1}(proportion of bootstrap means <= 0)\nif boot_p_percentile > 0 and boot_p_percentile < 1:\n    z_test = norm.ppf(boot_p_percentile)\n    bca_p = float(norm.cdf(z0 + (z0 + z_test) / (1 - acceleration * (z0 + z_test))))\nelse:\n    bca_p = boot_p_percentile\nprint(f\"BCa-adjusted p-value: {bca_p:.4f}\")\n\nprint()\n\n# ============================================================\n# Part 2: Leave-one-out sensitivity\n# ============================================================\nprint(\"=\" * 60)\nprint(\"Part 2: Leave-One-Out Sensitivity\")\nprint(\"=\" * 60)\n\ndef bootstrap_p_value(diffs, n_resamples, seed):\n    \"\"\"One-sided p-value: H0: mean(ΔFPR) <= 0, H1: mean(ΔFPR) > 0.\"\"\"\n    rng = np.random.default_rng(seed)\n    n_d = len(diffs)\n    centered = diffs - np.mean(diffs)  # center under H0\n    boot_means = np.zeros(n_resamples)\n    for b in range(n_resamples):\n        idx = rng.integers(0, n_d, size=n_d)\n        boot_means[b] = np.mean(centered[idx])\n    # p-value: proportion of null bootstrap means >= observed mean\n    observed = np.mean(diffs)\n    p = float(np.mean(boot_means >= observed))\n    return p\n\nt0 = time.time()\nloo_results = []\nfor i in range(n):\n    diffs_loo = np.delete(delta_fpr, i)\n    p_loo = bootstrap_p_value(diffs_loo, N_RESAMPLES_LOO, seed=SEED + i)\n    loo_results.append({\n        \"removed_idx\": i,\n        \"p_value\": p_loo,\n        \"mean_delta\": float(np.mean(diffs_loo)),\n    })\n\nloo_flipped = [r for r in loo_results if r[\"p_value\"] > 0.05]\nloo_sorted = sorted(loo_results, key=lambda r: -r[\"p_value\"])\n\nprint(f\"Leave-one-out completed in {time.time()-t0:.1f}s\")\nprint(f\"  {len(loo_flipped)}/{n} traces: removal causes p > 0.05\")\nif loo_sorted:\n    most = loo_sorted[0]\n    least = loo_sorted[-1]\n    print(f\"  Most influential:  trace idx {most['removed_idx']} (p without = {most['p_value']:.4f}, mean ΔFPR = {most['mean_delta']:.4f})\")\n    print(f\"  Least influential: trace idx {least['removed_idx']} (p without = {least['p_value']:.4f}, mean ΔFPR = {least['mean_delta']:.4f})\")\n\nif loo_flipped:\n    print(f\"\\n  Traces whose removal causes p > 0.05:\")\n    for r in sorted(loo_flipped, key=lambda r: -r[\"p_value\"]):\n        print(f\"    idx={r['removed_idx']}: p={r['p_value']:.4f}, mean_delta={r['mean_delta']:.4f}\")\n\nprint()\n\n# ============================================================\n# Part 3: Leave-two-out sensitivity\n# ============================================================\nprint(\"=\" * 60)\nprint(\"Part 3: Leave-Two-Out Sensitivity\")\nprint(\"=\" * 60)\n\nt0 = time.time()\nn_pairs = n * (n - 1) // 2\nprint(f\"Total pairs: C({n},2) = {n_pairs}\")\n\nlto_flipped = 0\nlto_flipped_pairs = []\n\nfor pair_idx, (i, j) in enumerate(combinations(range(n), 2)):\n    mask = np.ones(n, dtype=bool)\n    mask[i] = False\n    mask[j] = False\n    diffs_lto = delta_fpr[mask]\n    p_lto = bootstrap_p_value(diffs_lto, N_RESAMPLES_LOO, seed=SEED + pair_idx)\n    if p_lto > 0.05:\n        lto_flipped += 1\n        lto_flipped_pairs.append({\n            \"pair\": (i, j),\n            \"p_value\": p_lto,\n            \"mean_delta\": float(np.mean(diffs_lto)),\n        })\n    if (pair_idx + 1) % 200 == 0:\n        print(f\"  Progress: {pair_idx+1}/{n_pairs} pairs, {lto_flipped} flipped so far\")\n\nlto_time = time.time() - t0\nprint(f\"\\nLeave-two-out completed in {lto_time:.1f}s\")\nprint(f\"  {lto_flipped}/{n_pairs} pairs: removal causes p > 0.05\")\n\nif lto_flipped_pairs:\n    lto_sorted = sorted(lto_flipped_pairs, key=lambda r: -r[\"p_value\"])\n    print(f\"  Most influential pair: idx ({lto_sorted[0]['pair'][0]}, {lto_sorted[0]['pair'][1]}), p={lto_sorted[0]['p_value']:.4f}\")\n    top5 = lto_sorted[:min(5, len(lto_sorted))]\n    print(f\"\\n  Top 5 most influential pairs:\")\n    for r in top5:\n        print(f\"    pair=({r['pair'][0]}, {r['pair'][1]}): p={r['p_value']:.4f}, mean_delta={r['mean_delta']:.4f}\")\n\n# ============================================================\n# Save results\n# ============================================================\noutput = {\n    \"model\": \"r1-8b\",\n    \"layer\": 14,\n    \"window\": 15,\n    \"n_test_traces\": n,\n    \"delta_fpr_mean\": float(observed_mean),\n    \"hs_fpr_mean\": float(np.mean(hs_fprs)),\n    \"text_fpr_mean\": float(np.mean(text_fprs)),\n    \"bca\": {\n        \"ci_95\": [bca_ci_low, bca_ci_high],\n        \"contains_zero\": contains_zero,\n        \"z0\": z0,\n        \"acceleration\": acceleration,\n        \"n_resamples\": N_RESAMPLES_BCA,\n        \"percentile_p_value\": boot_p_percentile,\n        \"bca_adjusted_p_value\": bca_p,\n    },\n    \"leave_one_out\": {\n        \"n_flipped\": len(loo_flipped),\n        \"n_total\": n,\n        \"flipped_traces\": [{\"idx\": r[\"removed_idx\"], \"p\": r[\"p_value\"], \"mean_delta\": r[\"mean_delta\"]} for r in sorted(loo_flipped, key=lambda r: -r[\"p_value\"])],\n        \"all_p_values\": [r[\"p_value\"] for r in loo_results],\n        \"most_influential_idx\": loo_sorted[0][\"removed_idx\"],\n        \"most_influential_p\": loo_sorted[0][\"p_value\"],\n        \"least_influential_idx\": loo_sorted[-1][\"removed_idx\"],\n        \"least_influential_p\": loo_sorted[-1][\"p_value\"],\n    },\n    \"leave_two_out\": {\n        \"n_flipped\": lto_flipped,\n        \"n_total\": n_pairs,\n        \"flipped_fraction\": lto_flipped / n_pairs,\n        \"top_flipped_pairs\": [{\"pair\": list(r[\"pair\"]), \"p\": r[\"p_value\"], \"mean_delta\": r[\"mean_delta\"]} for r in sorted(lto_flipped_pairs, key=lambda r: -r[\"p_value\"])[:20]],\n    },\n    \"per_trace_delta_fpr\": [float(x) for x in delta_fpr],\n    \"per_trace_hs_fprs\": [float(x) for x in hs_fprs],\n    \"per_trace_text_fprs\": [float(x) for x in text_fprs],\n}\n\nout_path = OUTPUT_DIR / \"bca_results.json\"\nwith open(out_path, \"w\") as f:\n    json.dump(output, f, indent=2)\nprint(f\"\\nResults saved to {out_path}\")\n\n# Summary\nprint(\"\\n\" + \"=\" * 60)\nprint(\"SUMMARY\")\nprint(\"=\" * 60)\nprint(f\"BCa 95% CI for ΔFPR (text - HS): [{bca_ci_low:.6f}, {bca_ci_high:.6f}]\")\nprint(f\"Contains 0: {'Yes' if contains_zero else 'No'}\")\nprint(f\"BCa p-value: {bca_p:.4f}\")\nprint(f\"\")\nprint(f\"Leave-one-out sensitivity:\")\nprint(f\"  {len(loo_flipped)}/{n} traces: removal causes p > 0.05\")\nprint(f\"  Most influential trace: idx {loo_sorted[0]['removed_idx']} (p without = {loo_sorted[0]['p_value']:.4f})\")\nprint(f\"  Least influential: idx {loo_sorted[-1]['removed_idx']} (p without = {loo_sorted[-1]['p_value']:.4f})\")\nprint(f\"\")\nprint(f\"Leave-two-out:\")\nprint(f\"  {lto_flipped}/{n_pairs} pairs: removal causes p > 0.05 ({100*lto_flipped/n_pairs:.1f}%)\")\nPYEOF\necho \"Script written.\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r14_a4_bca_r1_8b_fpr_20260518T162942",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "cat > /root/autodl-tmp/contrastive_trace_safety/scripts/a4_bca_fpr.py << 'PYEOF'\n\"\"\"A4: BCa bootstrap CI + leave-one-out/leave-two-out sensitivity for R1-8B FPR.\"\"\"\n\nimport json, os, time\nimport numpy as np\nfrom scipy.stats import bootstrap, norm\nfrom pathlib import Path\nfrom itertools import combinations\n\nRESULTS_PATH = Path(\"/root/autodl-tmp/contrastive_trace_safety/artifacts/r1_8b_bootstrap_hs_text/results.json\")\nOUTPUT_DIR = Path(\"/root/autodl-tmp/contrastive_trace_safety/artifacts/r14_a4_bca_fpr\")\nOUTPUT_DIR.mkdir(parents=True, exist_ok=True)\n\nSEED = 42\nN_RESAMPLES_BCA = 10000\nN_RESAMPLES_LOO = 1000\n\n# Load per-trace FPR arrays\nwith open(RESULTS_PATH) as f:\n    data = json.load(f)\n\nhs_fprs = np.array(data[\"per_trace_hs_fprs\"])\ntext_fprs = np.array(data[\"per_trace_text_fprs\"])\nn = len(hs_fprs)\nassert n == 43, f\"Expected 43 traces, got {n}\"\n\n# ΔFPR = text_FPR - HS_FPR (positive means text has higher FPR = worse)\ndelta_fpr = text_fprs - hs_fprs\nobserved_mean = np.mean(delta_fpr)\n\nprint(f\"n = {n} test traces\")\nprint(f\"HS FPR mean:   {np.mean(hs_fprs):.4f}\")\nprint(f\"Text FPR mean: {np.mean(text_fprs):.4f}\")\nprint(f\"ΔFPR mean (text - HS): {observed_mean:.4f}\")\nprint()\n\n# ============================================================\n# Part 1: BCa bootstrap CI via scipy.stats.bootstrap\n# ============================================================\nprint(\"=\" * 60)\nprint(\"Part 1: BCa Bootstrap CI\")\nprint(\"=\" * 60)\n\ndef mean_stat(x, axis):\n    return np.mean(x, axis=axis)\n\nrng = np.random.default_rng(SEED)\nbca_result = bootstrap(\n    (delta_fpr,),\n    statistic=mean_stat,\n    n_resamples=N_RESAMPLES_BCA,\n    method='BCa',\n    confidence_level=0.95,\n    alternative='two-sided',\n    rng=rng,\n)\n\nbca_ci_low = float(bca_result.confidence_interval.low)\nbca_ci_high = float(bca_result.confidence_interval.high)\ncontains_zero = (bca_ci_low <= 0 <= bca_ci_high)\n\nprint(f\"BCa 95% CI for ΔFPR (text - HS): [{bca_ci_low:.6f}, {bca_ci_high:.6f}]\")\nprint(f\"Contains 0: {'Yes' if contains_zero else 'No'}\")\n\n# Manual BCa computation for z0 and acceleration, and BCa p-value\nboot_means = bca_result.bootstrap_distribution\nz0_prop = np.mean(boot_means < observed_mean)\nz0 = float(norm.ppf(z0_prop))\nprint(f\"BCa z0 (bias correction): {z0:.4f} (prop below observed: {z0_prop:.4f})\")\n\n# Jackknife for acceleration constant\njackknife_means = np.zeros(n)\nfor i in range(n):\n    jackknife_means[i] = np.mean(np.delete(delta_fpr, i))\njack_mean = np.mean(jackknife_means)\ninfluence = jack_mean - jackknife_means\nnum = np.sum(influence**3)\nden = 6.0 * (np.sum(influence**2))**(1.5)\nacceleration = float(num / den) if den != 0 else 0.0\nprint(f\"BCa acceleration constant a: {acceleration:.6f}\")\n\n# BCa p-value: fraction of bootstrap distribution <= 0, adjusted by BCa\n# Standard bootstrap p-value (proportion of bootstrap means <= 0)\nboot_p_percentile = float(np.mean(boot_means <= 0))\nprint(f\"Percentile bootstrap p-value (ΔFPR <= 0): {boot_p_percentile:.4f}\")\n\n# BCa-adjusted p-value\n# P(ΔFPR <= 0): find where 0 sits in BCa-adjusted distribution\n# z_test = Φ^{-1}(proportion of bootstrap means <= 0)\nif boot_p_percentile > 0 and boot_p_percentile < 1:\n    z_test = norm.ppf(boot_p_percentile)\n    bca_p = float(norm.cdf(z0 + (z0 + z_test) / (1 - acceleration * (z0 + z_test))))\nelse:\n    bca_p = boot_p_percentile\nprint(f\"BCa-adjusted p-value: {bca_p:.4f}\")\n\nprint()\n\n# ============================================================\n# Part 2: Leave-one-out sensitivity\n# ============================================================\nprint(\"=\" * 60)\nprint(\"Part 2: Leave-One-Out Sensitivity\")\nprint(\"=\" * 60)\n\ndef bootstrap_p_value(diffs, n_resamples, seed):\n    \"\"\"One-sided p-value: H0: mean(ΔFPR) <= 0, H1: mean(ΔFPR) > 0.\"\"\"\n    rng = np.random.default_rng(seed)\n    n_d = len(diffs)\n    centered = diffs - np.mean(diffs)  # center under H0\n    boot_means = np.zeros(n_resamples)\n    for b in range(n_resamples):\n        idx = rng.integers(0, n_d, size=n_d)\n        boot_means[b] = np.mean(centered[idx])\n    # p-value: proportion of null bootstrap means >= observed mean\n    observed = np.mean(diffs)\n    p = float(np.mean(boot_means >= observed))\n    return p\n\nt0 = time.time()\nloo_results = []\nfor i in range(n):\n    diffs_loo = np.delete(delta_fpr, i)\n    p_loo = bootstrap_p_value(diffs_loo, N_RESAMPLES_LOO, seed=SEED + i)\n    loo_results.append({\n        \"removed_idx\": i,\n        \"p_value\": p_loo,\n        \"mean_delta\": float(np.mean(diffs_loo)),\n    })\n\nloo_flipped = [r for r in loo_results if r[\"p_value\"] > 0.05]\nloo_sorted = sorted(loo_results, key=lambda r: -r[\"p_value\"])\n\nprint(f\"Leave-one-out completed in {time.time()-t0:.1f}s\")\nprint(f\"  {len(loo_flipped)}/{n} traces: removal causes p > 0.05\")\nif loo_sorted:\n    most = loo_sorted[0]\n    least = loo_sorted[-1]\n    print(f\"  Most influential:  trace idx {most['removed_idx']} (p without = {most['p_value']:.4f}, mean ΔFPR = {most['mean_delta']:.4f})\")\n    print(f\"  Least influential: trace idx {least['removed_idx']} (p without = {least['p_value']:.4f}, mean ΔFPR = {least['mean_delta']:.4f})\")\n\nif loo_flipped:\n    print(f\"\\n  Traces whose removal causes p > 0.05:\")\n    for r in sorted(loo_flipped, key=lambda r: -r[\"p_value\"]):\n        print(f\"    idx={r['removed_idx']}: p={r['p_value']:.4f}, mean_delta={r['mean_delta']:.4f}\")\n\nprint()\n\n# ============================================================\n# Part 3: Leave-two-out sensitivity\n# ============================================================\nprint(\"=\" * 60)\nprint(\"Part 3: Leave-Two-Out Sensitivity\")\nprint(\"=\" * 60)\n\nt0 = time.time()\nn_pairs = n * (n - 1) // 2\nprint(f\"Total pairs: C({n},2) = {n_pairs}\")\n\nlto_flipped = 0\nlto_flipped_pairs = []\n\nfor pair_idx, (i, j) in enumerate(combinations(range(n), 2)):\n    mask = np.ones(n, dtype=bool)\n    mask[i] = False\n    mask[j] = False\n    diffs_lto = delta_fpr[mask]\n    p_lto = bootstrap_p_value(diffs_lto, N_RESAMPLES_LOO, seed=SEED + pair_idx)\n    if p_lto > 0.05:\n        lto_flipped += 1\n        lto_flipped_pairs.append({\n            \"pair\": (i, j),\n            \"p_value\": p_lto,\n            \"mean_delta\": float(np.mean(diffs_lto)),\n        })\n    if (pair_idx + 1) % 200 == 0:\n        print(f\"  Progress: {pair_idx+1}/{n_pairs} pairs, {lto_flipped} flipped so far\")\n\nlto_time = time.time() - t0\nprint(f\"\\nLeave-two-out completed in {lto_time:.1f}s\")\nprint(f\"  {lto_flipped}/{n_pairs} pairs: removal causes p > 0.05\")\n\nif lto_flipped_pairs:\n    lto_sorted = sorted(lto_flipped_pairs, key=lambda r: -r[\"p_value\"])\n    print(f\"  Most influential pair: idx ({lto_sorted[0]['pair'][0]}, {lto_sorted[0]['pair'][1]}), p={lto_sorted[0]['p_value']:.4f}\")\n    top5 = lto_sorted[:min(5, len(lto_sorted))]\n    print(f\"\\n  Top 5 most influential pairs:\")\n    for r in top5:\n        print(f\"    pair=({r['pair'][0]}, {r['pair'][1]}): p={r['p_value']:.4f}, mean_delta={r['mean_delta']:.4f}\")\n\n# ============================================================\n# Save results\n# ============================================================\noutput = {\n    \"model\": \"r1-8b\",\n    \"layer\": 14,\n    \"window\": 15,\n    \"n_test_traces\": n,\n    \"delta_fpr_mean\": float(observed_mean),\n    \"hs_fpr_mean\": float(np.mean(hs_fprs)),\n    \"text_fpr_mean\": float(np.mean(text_fprs)),\n    \"bca\": {\n        \"ci_95\": [bca_ci_low, bca_ci_high],\n        \"contains_zero\": contains_zero,\n        \"z0\": z0,\n        \"acceleration\": acceleration,\n        \"n_resamples\": N_RESAMPLES_BCA,\n        \"percentile_p_value\": boot_p_percentile,\n        \"bca_adjusted_p_value\": bca_p,\n    },\n    \"leave_one_out\": {\n        \"n_flipped\": len(loo_flipped),\n        \"n_total\": n,\n        \"flipped_traces\": [{\"idx\": r[\"removed_idx\"], \"p\": r[\"p_value\"], \"mean_delta\": r[\"mean_delta\"]} for r in sorted(loo_flipped, key=lambda r: -r[\"p_value\"])],\n        \"all_p_values\": [r[\"p_value\"] for r in loo_results],\n        \"most_influential_idx\": loo_sorted[0][\"removed_idx\"],\n        \"most_influential_p\": loo_sorted[0][\"p_value\"],\n        \"least_influential_idx\": loo_sorted[-1][\"removed_idx\"],\n        \"least_influential_p\": loo_sorted[-1][\"p_value\"],\n    },\n    \"leave_two_out\": {\n        \"n_flipped\": lto_flipped,\n        \"n_total\": n_pairs,\n        \"flipped_fraction\": lto_flipped / n_pairs,\n        \"top_flipped_pairs\": [{\"pair\": list(r[\"pair\"]), \"p\": r[\"p_value\"], \"mean_delta\": r[\"mean_delta\"]} for r in sorted(lto_flipped_pairs, key=lambda r: -r[\"p_value\"])[:20]],\n    },\n    \"per_trace_delta_fpr\": [float(x) for x in delta_fpr],\n    \"per_trace_hs_fprs\": [float(x) for x in hs_fprs],\n    \"per_trace_text_fprs\": [float(x) for x in text_fprs],\n}\n\nout_path = OUTPUT_DIR / \"bca_results.json\"\nwith open(out_path, \"w\") as f:\n    json.dump(output, f, indent=2)\nprint(f\"\\nResults saved to {out_path}\")\n\n# Summary\nprint(\"\\n\" + \"=\" * 60)\nprint(\"SUMMARY\")\nprint(\"=\" * 60)\nprint(f\"BCa 95% CI for ΔFPR (text - HS): [{bca_ci_low:.6f}, {bca_ci_high:.6f}]\")\nprint(f\"Contains 0: {'Yes' if contains_zero else 'No'}\")\nprint(f\"BCa p-value: {bca_p:.4f}\")\nprint(f\"\")\nprint(f\"Leave-one-out sensitivity:\")\nprint(f\"  {len(loo_flipped)}/{n} traces: removal causes p > 0.05\")\nprint(f\"  Most influential trace: idx {loo_sorted[0]['removed_idx']} (p without = {loo_sorted[0]['p_value']:.4f})\")\nprint(f\"  Least influential: idx {loo_sorted[-1]['removed_idx']} (p without = {loo_sorted[-1]['p_value']:.4f})\")\nprint(f\"\")\nprint(f\"Leave-two-out:\")\nprint(f\"  {lto_flipped}/{n_pairs} pairs: removal causes p > 0.05 ({100*lto_flipped/n_pairs:.1f}%)\")\nPYEOF\necho \"Script written.\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-18T16:33:56.417390+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script written.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.72}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r14_a4_bca_r1_8b_fpr_20260518T162942",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-18T16:33:56.417519+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "/root/miniconda3/bin/python3.12 /root/autodl-tmp/contrastive_trace_safety/scripts/a4_bca_fpr.py",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r14_a4_bca_r1_8b_fpr_20260518T162942",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "/root/miniconda3/bin/python3.12 /root/autodl-tmp/contrastive_trace_safety/scripts/a4_bca_fpr.py",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-18T16:33:56.417664+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: '/root/miniconda3/bin/python3.12 /root/autodl-tmp/contrastive_trace_safety/scripts/a4_bca_fpr.py'\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.49}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r14_a4_bca_r1_8b_fpr_20260518T162942",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-18T16:33:56.417860+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "cat > /root/autodl-tmp/contrastive_trace_safety/scripts/a4_bca_fpr.py << 'PYEOF'\n\"\"\"A4: BCa bootstrap CI + leave-one-out/leave-two-out sensitivity for R1-8B FPR.\"\"\"\n\nimport json, time\nimport numpy as np\nfrom scipy.stats import bootstrap, norm\nfrom pathlib import Path\nfrom itertools import combinations\n\nRESULTS_PATH = Path(\"/root/autodl-tmp/contrastive_trace_safety/artifacts/r1_8b_bootstrap_hs_text/results.json\")\nOUTPUT_DIR = Path(\"/root/autodl-tmp/contrastive_trace_safety/artifacts/r14_a4_bca_fpr\")\nOUTPUT_DIR.mkdir(parents=True, exist_ok=True)\n\nSEED = 42\nN_RESAMPLES_BCA = 10000\nN_RESAMPLES_LOO = 1000\n\nwith open(RESULTS_PATH) as f:\n    data = json.load(f)\n\nhs_fprs = np.array(data[\"per_trace_hs_fprs\"])\ntext_fprs = np.array(data[\"per_trace_text_fprs\"])\nn = len(hs_fprs)\nassert n == 43\n\ndelta_fpr = text_fprs - hs_fprs\nobserved_mean = np.mean(delta_fpr)\n\nprint(f\"n = {n}, HS FPR = {np.mean(hs_fprs):.4f}, Text FPR = {np.mean(text_fprs):.4f}, ΔFPR = {observed_mean:.4f}\")\n\n# ============ Part 1: BCa CI ============\nprint(\"\\n=== Part 1: BCa Bootstrap CI ===\")\n\ndef mean_stat(x, axis):\n    return np.mean(x, axis=axis)\n\nrng = np.random.default_rng(SEED)\nbca_result = bootstrap(\n    (delta_fpr,),\n    statistic=mean_stat,\n    n_resamples=N_RESAMPLES_BCA,\n    method='BCa',\n    confidence_level=0.95,\n    alternative='two-sided',\n    rng=rng,\n)\n\nbca_ci_low = float(bca_result.confidence_interval.low)\nbca_ci_high = float(bca_result.confidence_interval.high)\ncontains_zero = bool(bca_ci_low <= 0 <= bca_ci_high)\nboot_dist = bca_result.bootstrap_distribution\n\nz0_prop = np.mean(boot_dist < observed_mean)\nz0 = float(norm.ppf(max(1e-10, min(1-1e-10, z0_prop))))\n\njackknife_means = np.array([np.mean(np.delete(delta_fpr, i)) for i in range(n)])\njack_mean = np.mean(jackknife_means)\ninfluence = jack_mean - jackknife_means\nnum = np.sum(influence**3)\nden = 6.0 * (np.sum(influence**2))**1.5\nacceleration = float(num / den) if den != 0 else 0.0\n\nboot_p_pct = float(np.mean(boot_dist <= 0))\nif 0 < boot_p_pct < 1:\n    z_test = norm.ppf(boot_p_pct)\n    bca_p = float(norm.cdf(z0 + (z0 + z_test) / (1 - acceleration * (z0 + z_test))))\nelse:\n    bca_p = boot_p_pct\n\nprint(f\"BCa 95% CI: [{bca_ci_low:.6f}, {bca_ci_high:.6f}]\")\nprint(f\"Contains 0: {'Yes' if contains_zero else 'No'}\")\nprint(f\"z0={z0:.4f}, a={acceleration:.6f}\")\nprint(f\"Percentile p={boot_p_pct:.4f}, BCa p={bca_p:.4f}\")\n\n# ============ Vectorized bootstrap p-value ============\ndef bootstrap_p_vectorized(diffs, n_resamples, seed):\n    \"\"\"Vectorized one-sided p-value: H0: mean(ΔFPR) <= 0.\"\"\"\n    rng = np.random.default_rng(seed)\n    nd = len(diffs)\n    obs = np.mean(diffs)\n    centered = diffs - obs\n    idx = rng.integers(0, nd, size=(n_resamples, nd))\n    boot_means = np.mean(centered[idx], axis=1)\n    return float(np.mean(boot_means >= obs))\n\n# ============ Part 2: Leave-one-out ============\nprint(\"\\n=== Part 2: Leave-One-Out ===\")\nt0 = time.time()\n\nloo_p = np.zeros(n)\nloo_mean = np.zeros(n)\nfor i in range(n):\n    d = np.delete(delta_fpr, i)\n    loo_p[i] = bootstrap_p_vectorized(d, N_RESAMPLES_LOO, SEED + i)\n    loo_mean[i] = np.mean(d)\n\nloo_flipped_mask = loo_p > 0.05\nn_loo_flipped = int(np.sum(loo_flipped_mask))\nmost_idx = int(np.argmax(loo_p))\nleast_idx = int(np.argmin(loo_p))\n\nprint(f\"Done in {time.time()-t0:.1f}s\")\nprint(f\"{n_loo_flipped}/{n} traces: removal causes p > 0.05\")\nprint(f\"Most influential:  idx {most_idx} (p={loo_p[most_idx]:.4f}, ΔFPR without={loo_mean[most_idx]:.4f})\")\nprint(f\"Least influential: idx {least_idx} (p={loo_p[least_idx]:.4f}, ΔFPR without={loo_mean[least_idx]:.4f})\")\n\nif n_loo_flipped > 0:\n    print(\"Traces whose removal flips p > 0.05:\")\n    for i in np.where(loo_flipped_mask)[0]:\n        print(f\"  idx={i}: p={loo_p[i]:.4f}, delta_fpr[i]={delta_fpr[i]:.4f}, mean_without={loo_mean[i]:.4f}\")\n\n# ============ Part 3: Leave-two-out ============\nprint(\"\\n=== Part 3: Leave-Two-Out ===\")\nt0 = time.time()\nn_pairs = n * (n - 1) // 2\nprint(f\"Total pairs: {n_pairs}\")\n\nlto_flipped = 0\nlto_flipped_info = []\n\nfor pair_idx, (i, j) in enumerate(combinations(range(n), 2)):\n    mask = np.ones(n, dtype=bool)\n    mask[i] = False\n    mask[j] = False\n    d = delta_fpr[mask]\n    p = bootstrap_p_vectorized(d, N_RESAMPLES_LOO, SEED + pair_idx)\n    if p > 0.05:\n        lto_flipped += 1\n        lto_flipped_info.append({\"pair\": [int(i), int(j)], \"p\": float(p), \"mean_delta\": float(np.mean(d))})\n    if (pair_idx + 1) % 300 == 0:\n        elapsed = time.time() - t0\n        print(f\"  {pair_idx+1}/{n_pairs} ({elapsed:.0f}s), flipped={lto_flipped}\")\n\nlto_time = time.time() - t0\nprint(f\"Done in {lto_time:.1f}s\")\nprint(f\"{lto_flipped}/{n_pairs} pairs: removal causes p > 0.05 ({100*lto_flipped/n_pairs:.1f}%)\")\n\nif lto_flipped_info:\n    lto_sorted = sorted(lto_flipped_info, key=lambda r: -r[\"p\"])\n    print(f\"Most influential pair: ({lto_sorted[0]['pair'][0]}, {lto_sorted[0]['pair'][1]}), p={lto_sorted[0]['p']:.4f}\")\n    for r in lto_sorted[:5]:\n        print(f\"  pair=({r['pair'][0]}, {r['pair'][1]}): p={r['p']:.4f}, mean_delta={r['mean_delta']:.4f}\")\n\n# ============ Save ============\noutput = {\n    \"model\": \"r1-8b\", \"layer\": 14, \"window\": 15, \"n_test_traces\": n,\n    \"delta_fpr_mean\": float(observed_mean),\n    \"hs_fpr_mean\": float(np.mean(hs_fprs)),\n    \"text_fpr_mean\": float(np.mean(text_fprs)),\n    \"bca\": {\n        \"ci_95\": [bca_ci_low, bca_ci_high],\n        \"contains_zero\": contains_zero,\n        \"z0\": z0,\n        \"acceleration\": acceleration,\n        \"n_resamples\": N_RESAMPLES_BCA,\n        \"percentile_p_value\": boot_p_pct,\n        \"bca_adjusted_p_value\": bca_p,\n    },\n    \"leave_one_out\": {\n        \"n_flipped\": n_loo_flipped,\n        \"n_total\": n,\n        \"all_p_values\": [float(p) for p in loo_p],\n        \"all_mean_deltas\": [float(m) for m in loo_mean],\n        \"flipped_indices\": [int(i) for i in np.where(loo_flipped_mask)[0]],\n        \"most_influential_idx\": most_idx,\n        \"most_influential_p\": float(loo_p[most_idx]),\n        \"least_influential_idx\": least_idx,\n        \"least_influential_p\": float(loo_p[least_idx]),\n    },\n    \"leave_two_out\": {\n        \"n_flipped\": lto_flipped,\n        \"n_total\": n_pairs,\n        \"flipped_fraction\": lto_flipped / n_pairs,\n        \"top_flipped_pairs\": sorted(lto_flipped_info, key=lambda r: -r[\"p\"])[:20],\n    },\n    \"per_trace_delta_fpr\": [float(x) for x in delta_fpr],\n}\n\nout_path = OUTPUT_DIR / \"bca_results.json\"\nwith open(out_path, \"w\") as f:\n    json.dump(output, f, indent=2)\nprint(f\"\\nSaved: {out_path}\")\n\nprint(\"\\n\" + \"=\" * 60)\nprint(\"SUMMARY\")\nprint(\"=\" * 60)\nprint(f\"BCa 95% CI for ΔFPR (text - HS): [{bca_ci_low:.6f}, {bca_ci_high:.6f}]\")\nprint(f\"Contains 0: {'Yes' if contains_zero else 'No'}\")\nprint(f\"BCa p-value: {bca_p:.4f}\")\nprint(f\"Leave-one-out: {n_loo_flipped}/{n} traces removal causes p > 0.05\")\nprint(f\"Leave-two-out: {lto_flipped}/{n_pairs} pairs removal causes p > 0.05 ({100*lto_flipped/n_pairs:.1f}%)\")\nPYEOF\necho \"Script written.\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r14_a4_bca_r1_8b_fpr_20260518T162942",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "cat > /root/autodl-tmp/contrastive_trace_safety/scripts/a4_bca_fpr.py << 'PYEOF'\n\"\"\"A4: BCa bootstrap CI + leave-one-out/leave-two-out sensitivity for R1-8B FPR.\"\"\"\n\nimport json, time\nimport numpy as np\nfrom scipy.stats import bootstrap, norm\nfrom pathlib import Path\nfrom itertools import combinations\n\nRESULTS_PATH = Path(\"/root/autodl-tmp/contrastive_trace_safety/artifacts/r1_8b_bootstrap_hs_text/results.json\")\nOUTPUT_DIR = Path(\"/root/autodl-tmp/contrastive_trace_safety/artifacts/r14_a4_bca_fpr\")\nOUTPUT_DIR.mkdir(parents=True, exist_ok=True)\n\nSEED = 42\nN_RESAMPLES_BCA = 10000\nN_RESAMPLES_LOO = 1000\n\nwith open(RESULTS_PATH) as f:\n    data = json.load(f)\n\nhs_fprs = np.array(data[\"per_trace_hs_fprs\"])\ntext_fprs = np.array(data[\"per_trace_text_fprs\"])\nn = len(hs_fprs)\nassert n == 43\n\ndelta_fpr = text_fprs - hs_fprs\nobserved_mean = np.mean(delta_fpr)\n\nprint(f\"n = {n}, HS FPR = {np.mean(hs_fprs):.4f}, Text FPR = {np.mean(text_fprs):.4f}, ΔFPR = {observed_mean:.4f}\")\n\n# ============ Part 1: BCa CI ============\nprint(\"\\n=== Part 1: BCa Bootstrap CI ===\")\n\ndef mean_stat(x, axis):\n    return np.mean(x, axis=axis)\n\nrng = np.random.default_rng(SEED)\nbca_result = bootstrap(\n    (delta_fpr,),\n    statistic=mean_stat,\n    n_resamples=N_RESAMPLES_BCA,\n    method='BCa',\n    confidence_level=0.95,\n    alternative='two-sided',\n    rng=rng,\n)\n\nbca_ci_low = float(bca_result.confidence_interval.low)\nbca_ci_high = float(bca_result.confidence_interval.high)\ncontains_zero = bool(bca_ci_low <= 0 <= bca_ci_high)\nboot_dist = bca_result.bootstrap_distribution\n\nz0_prop = np.mean(boot_dist < observed_mean)\nz0 = float(norm.ppf(max(1e-10, min(1-1e-10, z0_prop))))\n\njackknife_means = np.array([np.mean(np.delete(delta_fpr, i)) for i in range(n)])\njack_mean = np.mean(jackknife_means)\ninfluence = jack_mean - jackknife_means\nnum = np.sum(influence**3)\nden = 6.0 * (np.sum(influence**2))**1.5\nacceleration = float(num / den) if den != 0 else 0.0\n\nboot_p_pct = float(np.mean(boot_dist <= 0))\nif 0 < boot_p_pct < 1:\n    z_test = norm.ppf(boot_p_pct)\n    bca_p = float(norm.cdf(z0 + (z0 + z_test) / (1 - acceleration * (z0 + z_test))))\nelse:\n    bca_p = boot_p_pct\n\nprint(f\"BCa 95% CI: [{bca_ci_low:.6f}, {bca_ci_high:.6f}]\")\nprint(f\"Contains 0: {'Yes' if contains_zero else 'No'}\")\nprint(f\"z0={z0:.4f}, a={acceleration:.6f}\")\nprint(f\"Percentile p={boot_p_pct:.4f}, BCa p={bca_p:.4f}\")\n\n# ============ Vectorized bootstrap p-value ============\ndef bootstrap_p_vectorized(diffs, n_resamples, seed):\n    \"\"\"Vectorized one-sided p-value: H0: mean(ΔFPR) <= 0.\"\"\"\n    rng = np.random.default_rng(seed)\n    nd = len(diffs)\n    obs = np.mean(diffs)\n    centered = diffs - obs\n    idx = rng.integers(0, nd, size=(n_resamples, nd))\n    boot_means = np.mean(centered[idx], axis=1)\n    return float(np.mean(boot_means >= obs))\n\n# ============ Part 2: Leave-one-out ============\nprint(\"\\n=== Part 2: Leave-One-Out ===\")\nt0 = time.time()\n\nloo_p = np.zeros(n)\nloo_mean = np.zeros(n)\nfor i in range(n):\n    d = np.delete(delta_fpr, i)\n    loo_p[i] = bootstrap_p_vectorized(d, N_RESAMPLES_LOO, SEED + i)\n    loo_mean[i] = np.mean(d)\n\nloo_flipped_mask = loo_p > 0.05\nn_loo_flipped = int(np.sum(loo_flipped_mask))\nmost_idx = int(np.argmax(loo_p))\nleast_idx = int(np.argmin(loo_p))\n\nprint(f\"Done in {time.time()-t0:.1f}s\")\nprint(f\"{n_loo_flipped}/{n} traces: removal causes p > 0.05\")\nprint(f\"Most influential:  idx {most_idx} (p={loo_p[most_idx]:.4f}, ΔFPR without={loo_mean[most_idx]:.4f})\")\nprint(f\"Least influential: idx {least_idx} (p={loo_p[least_idx]:.4f}, ΔFPR without={loo_mean[least_idx]:.4f})\")\n\nif n_loo_flipped > 0:\n    print(\"Traces whose removal flips p > 0.05:\")\n    for i in np.where(loo_flipped_mask)[0]:\n        print(f\"  idx={i}: p={loo_p[i]:.4f}, delta_fpr[i]={delta_fpr[i]:.4f}, mean_without={loo_mean[i]:.4f}\")\n\n# ============ Part 3: Leave-two-out ============\nprint(\"\\n=== Part 3: Leave-Two-Out ===\")\nt0 = time.time()\nn_pairs = n * (n - 1) // 2\nprint(f\"Total pairs: {n_pairs}\")\n\nlto_flipped = 0\nlto_flipped_info = []\n\nfor pair_idx, (i, j) in enumerate(combinations(range(n), 2)):\n    mask = np.ones(n, dtype=bool)\n    mask[i] = False\n    mask[j] = False\n    d = delta_fpr[mask]\n    p = bootstrap_p_vectorized(d, N_RESAMPLES_LOO, SEED + pair_idx)\n    if p > 0.05:\n        lto_flipped += 1\n        lto_flipped_info.append({\"pair\": [int(i), int(j)], \"p\": float(p), \"mean_delta\": float(np.mean(d))})\n    if (pair_idx + 1) % 300 == 0:\n        elapsed = time.time() - t0\n        print(f\"  {pair_idx+1}/{n_pairs} ({elapsed:.0f}s), flipped={lto_flipped}\")\n\nlto_time = time.time() - t0\nprint(f\"Done in {lto_time:.1f}s\")\nprint(f\"{lto_flipped}/{n_pairs} pairs: removal causes p > 0.05 ({100*lto_flipped/n_pairs:.1f}%)\")\n\nif lto_flipped_info:\n    lto_sorted = sorted(lto_flipped_info, key=lambda r: -r[\"p\"])\n    print(f\"Most influential pair: ({lto_sorted[0]['pair'][0]}, {lto_sorted[0]['pair'][1]}), p={lto_sorted[0]['p']:.4f}\")\n    for r in lto_sorted[:5]:\n        print(f\"  pair=({r['pair'][0]}, {r['pair'][1]}): p={r['p']:.4f}, mean_delta={r['mean_delta']:.4f}\")\n\n# ============ Save ============\noutput = {\n    \"model\": \"r1-8b\", \"layer\": 14, \"window\": 15, \"n_test_traces\": n,\n    \"delta_fpr_mean\": float(observed_mean),\n    \"hs_fpr_mean\": float(np.mean(hs_fprs)),\n    \"text_fpr_mean\": float(np.mean(text_fprs)),\n    \"bca\": {\n        \"ci_95\": [bca_ci_low, bca_ci_high],\n        \"contains_zero\": contains_zero,\n        \"z0\": z0,\n        \"acceleration\": acceleration,\n        \"n_resamples\": N_RESAMPLES_BCA,\n        \"percentile_p_value\": boot_p_pct,\n        \"bca_adjusted_p_value\": bca_p,\n    },\n    \"leave_one_out\": {\n        \"n_flipped\": n_loo_flipped,\n        \"n_total\": n,\n        \"all_p_values\": [float(p) for p in loo_p],\n        \"all_mean_deltas\": [float(m) for m in loo_mean],\n        \"flipped_indices\": [int(i) for i in np.where(loo_flipped_mask)[0]],\n        \"most_influential_idx\": most_idx,\n        \"most_influential_p\": float(loo_p[most_idx]),\n        \"least_influential_idx\": least_idx,\n        \"least_influential_p\": float(loo_p[least_idx]),\n    },\n    \"leave_two_out\": {\n        \"n_flipped\": lto_flipped,\n        \"n_total\": n_pairs,\n        \"flipped_fraction\": lto_flipped / n_pairs,\n        \"top_flipped_pairs\": sorted(lto_flipped_info, key=lambda r: -r[\"p\"])[:20],\n    },\n    \"per_trace_delta_fpr\": [float(x) for x in delta_fpr],\n}\n\nout_path = OUTPUT_DIR / \"bca_results.json\"\nwith open(out_path, \"w\") as f:\n    json.dump(output, f, indent=2)\nprint(f\"\\nSaved: {out_path}\")\n\nprint(\"\\n\" + \"=\" * 60)\nprint(\"SUMMARY\")\nprint(\"=\" * 60)\nprint(f\"BCa 95% CI for ΔFPR (text - HS): [{bca_ci_low:.6f}, {bca_ci_high:.6f}]\")\nprint(f\"Contains 0: {'Yes' if contains_zero else 'No'}\")\nprint(f\"BCa p-value: {bca_p:.4f}\")\nprint(f\"Leave-one-out: {n_loo_flipped}/{n} traces removal causes p > 0.05\")\nprint(f\"Leave-two-out: {lto_flipped}/{n_pairs} pairs removal causes p > 0.05 ({100*lto_flipped/n_pairs:.1f}%)\")\nPYEOF\necho \"Script written.\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-18T16:33:56.418069+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script written.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.23}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r14_a4_bca_r1_8b_fpr_20260518T162942",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-18T16:33:56.418200+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "/root/miniconda3/bin/python3.12 /root/autodl-tmp/contrastive_trace_safety/scripts/a4_bca_fpr.py 2>&1",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r14_a4_bca_r1_8b_fpr_20260518T162942",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "/root/miniconda3/bin/python3.12 /root/autodl-tmp/contrastive_trace_safety/scripts/a4_bca_fpr.py 2>&1",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-18T16:33:56.418354+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"n = 43, HS FPR = 0.1484, Text FPR = 0.2219, ΔFPR = 0.0736\\n\\n=== Part 1: BCa Bootstrap CI ===\\nBCa 95% CI: [0.005817, 0.158995]\\nContains 0: No\\nz0=0.0374, a=0.020909\\nPercentile p=0.0234, BCa p=0.0331\\n\\n=== Part 2: Leave-One-Out ===\\nDone in 0.1s\\n5/43 traces: removal causes p > 0.05\\nMost influential:  idx 3 (p=0.0620, ΔFPR without=0.0630)\\nLeast influential: idx 30 (p=0.0100, ΔFPR without=0.0872)\\nTraces whose removal flips p > 0.05:\\n  idx=3: p=0.0620, delta_fpr[i]=0.5185, mean_without=0.0630\\n  idx=6: p=0.0560, delta_fpr[i]=0.6857, mean_without=0.0590\\n  idx=8: p=0.0580, delta_fpr[i]=0.5333, mean_without=0.0626\\n  idx=28: p=0.0520, delta_fpr[i]=0.5128, mean_without=0.0631\\n  idx=38: p=0.0620, delta_fpr[i]=0.7188, mean_without=0.0582\\n\\n=== Part 3: Leave-Two-Out ===\\nTotal pairs: 903\\n  300/903 (0s), flipped=91\\n  600/903 (1s), flipped=138\\n  900/903 (1s), flipped=191\\nDone in 1.4s\\n193/903 pairs: removal causes p > 0.05 (21.4%)\\nMost influential pair: (6, 38), p=0.1260\\n  pair=(6, 38): p=0.1260, mean_delta=0.0429\\n  pair=(3, 42): p=0.1060, mean_delta=0.0486\\n  pair=(6, 8): p=0.1050, mean_delta=0.0474\\n  pair=(6, 28): p=0.1010, mean_delta=0.0479\\n  pair=(28, 38): p=0.1010, mean_delta=0.0471\\n\\nSaved: /root/autodl-tmp/contrastive_trace_safety/artifacts/r14_a4_bca_fpr/bca_results.json\\n\\n============================================================\\nSUMMARY\\n============================================================\\nBCa 95% CI for ΔFPR (text - HS): [0.005817, 0.158995]\\nContains 0: No\\nBCa p-value: 0.0331\\nLeave-one-out: 5/43 traces removal causes p > 0.05\\nLeave-two-out: 193/903 pairs removal causes p > 0.05 (21.4%)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 6.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r14_a4_bca_r1_8b_fpr_20260518T162942",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-18T16:33:56.418517+00:00_

called mcp__agent-ml-research__save_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file</summary>

```json
{
  "project": "contrastive_trace_safety",
  "file": "memory.md",
  "content": "# A4: BCa Bootstrap CI for R1-8B FPR\n\n## Results (2026-05-18)\n\n### BCa Bootstrap CI\n- ΔFPR (text - HS) mean: 0.0736\n- BCa 95% CI: [0.005817, 0.158995]\n- Contains 0: **No** (result is robust)\n- BCa p-value: 0.0331\n- z0 (bias correction): 0.0374\n- Acceleration constant a: 0.020909\n- n_resamples: 10,000\n\n### Leave-One-Out Sensitivity\n- 5/43 traces: removal causes p > 0.05\n- Most influential traces (all have large positive ΔFPR, i.e., text much worse than HS):\n  - idx 3: p=0.062, ΔFPR=0.519\n  - idx 38: p=0.062, ΔFPR=0.719\n  - idx 8: p=0.058, ΔFPR=0.533\n  - idx 6: p=0.056, ΔFPR=0.686\n  - idx 28: p=0.052, ΔFPR=0.513\n- Least influential: idx 30 (p=0.010)\n\n### Leave-Two-Out Sensitivity\n- 193/903 pairs (21.4%): removal causes p > 0.05\n- Most influential pair: (6, 38), p=0.126\n\n### Interpretation\n- BCa CI does not contain 0, confirming HS probe has significantly lower FPR than text probe\n- The BCa-adjusted p-value (0.033) is stronger than the original percentile p-value (0.044)\n- However, the result is somewhat fragile: 5 individual traces and 21% of trace pairs can flip significance\n- The 5 influential traces all have very high positive ΔFPR (0.5-0.7), meaning they are outlier cases where text performs much worse than HS\n- The signal is real but depends partly on these high-leverage observations\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r14_a4_bca_r1_8b_fpr_20260518T162942",
  "tool": "mcp__agent-ml-research__save_project_file",
  "tool_args": {
    "project": "contrastive_trace_safety",
    "file": "memory.md",
    "content": "# A4: BCa Bootstrap CI for R1-8B FPR\n\n## Results (2026-05-18)\n\n### BCa Bootstrap CI\n- ΔFPR (text - HS) mean: 0.0736\n- BCa 95% CI: [0.005817, 0.158995]\n- Contains 0: **No** (result is robust)\n- BCa p-value: 0.0331\n- z0 (bias correction): 0.0374\n- Acceleration constant a: 0.020909\n- n_resamples: 10,000\n\n### Leave-One-Out Sensitivity\n- 5/43 traces: removal causes p > 0.05\n- Most influential traces (all have large positive ΔFPR, i.e., text much worse than HS):\n  - idx 3: p=0.062, ΔFPR=0.519\n  - idx 38: p=0.062, ΔFPR=0.719\n  - idx 8: p=0.058, ΔFPR=0.533\n  - idx 6: p=0.056, ΔFPR=0.686\n  - idx 28: p=0.052, ΔFPR=0.513\n- Least influential: idx 30 (p=0.010)\n\n### Leave-Two-Out Sensitivity\n- 193/903 pairs (21.4%): removal causes p > 0.05\n- Most influential pair: (6, 38), p=0.126\n\n### Interpretation\n- BCa CI does not contain 0, confirming HS probe has significantly lower FPR than text probe\n- The BCa-adjusted p-value (0.033) is stronger than the original percentile p-value (0.044)\n- However, the result is somewhat fragile: 5 individual traces and 21% of trace pairs can flip significance\n- The 5 influential traces all have very high positive ΔFPR (0.5-0.7), meaning they are outlier cases where text performs much worse than HS\n- The signal is real but depends partly on these high-leverage observations\n"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-18T16:33:56.418688+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r14_a4_bca_r1_8b_fpr_20260518T162942",
  "tool": "mcp__agent-ml-research__save_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-18T16:33:56.418814+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "A4 BCa Bootstrap CI for R1-8B FPR",
  "type": "data",
  "description": "BCa bootstrap CI, leave-one-out, and leave-two-out sensitivity analysis for R1-8B hidden states vs text FPR comparison. BCa CI [0.006, 0.159] excludes 0, BCa p=0.033. LOO: 5/43 traces flip significance. LTO: 193/903 pairs (21.4%) flip.",
  "project": "contrastive_trace_safety",
  "source_path": "/root/autodl-tmp/contrastive_trace_safety/artifacts/r14_a4_bca_fpr/bca_results.json",
  "tags": "['bootstrap', 'bca', 'fpr', 'r1-8b', 'sensitivity']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r14_a4_bca_r1_8b_fpr_20260518T162942",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "A4 BCa Bootstrap CI for R1-8B FPR",
    "type": "data",
    "description": "BCa bootstrap CI, leave-one-out, and leave-two-out sensitivity analysis for R1-8B hidden states vs text FPR comparison. BCa CI [0.006, 0.159] excludes 0, BCa p=0.033. LOO: 5/43 traces flip significance. LTO: 193/903 pairs (21.4%) flip.",
    "project": "contrastive_trace_safety",
    "source_path": "/root/autodl-tmp/contrastive_trace_safety/artifacts/r14_a4_bca_fpr/bca_results.json",
    "tags": "['bootstrap', 'bca', 'fpr', 'r1-8b', 'sensitivity']"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-18T16:33:56.418943+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"source_path not found: /root/autodl-tmp/contrastive_trace_safety/artifacts/r14_a4_bca_fpr/bca_results.json\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r14_a4_bca_r1_8b_fpr_20260518T162942",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-18T16:33:56.419060+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "cat /root/autodl-tmp/contrastive_trace_safety/artifacts/r14_a4_bca_fpr/bca_results.json | head -50",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r14_a4_bca_r1_8b_fpr_20260518T162942",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "cat /root/autodl-tmp/contrastive_trace_safety/artifacts/r14_a4_bca_fpr/bca_results.json | head -50",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-18T16:33:56.419205+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model\\\": \\\"r1-8b\\\",\\n  \\\"layer\\\": 14,\\n  \\\"window\\\": 15,\\n  \\\"n_test_traces\\\": 43,\\n  \\\"delta_fpr_mean\\\": 0.07355882853566037,\\n  \\\"hs_fpr_mean\\\": 0.1483665597701362,\\n  \\\"text_fpr_mean\\\": 0.22192538830579658,\\n  \\\"bca\\\": {\\n    \\\"ci_95\\\": [\\n      0.0058166822611619776,\\n      0.15899468831072203\\n    ],\\n    \\\"contains_zero\\\": false,\\n    \\\"z0\\\": 0.037357448684972254,\\n    \\\"acceleration\\\": 0.020909330249685797,\\n    \\\"n_resamples\\\": 10000,\\n    \\\"percentile_p_value\\\": 0.0234,\\n    \\\"bca_adjusted_p_value\\\": 0.03310934871669013\\n  },\\n  \\\"leave_one_out\\\": {\\n    \\\"n_flipped\\\": 5,\\n    \\\"n_total\\\": 43,\\n    \\\"all_p_values\\\": [\\n      0.036,\\n      0.038,\\n      0.039,\\n      0.062,\\n      0.049,\\n      0.03,\\n      0.056,\\n      0.034,\\n      0.058,\\n      0.03,\\n      0.025,\\n      0.025,\\n      0.028,\\n      0.029,\\n      0.032,\\n      0.046,\\n      0.035,\\n      0.024,\\n      0.034,\\n      0.034,\\n      0.031,\\n      0.034,\\n      0.039,\\n      0.039,\\n      0.035,\\n      0.025,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.79}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r14_a4_bca_r1_8b_fpr_20260518T162942",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-18T16:33:56.419344+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "A4 BCa Bootstrap CI for R1-8B FPR",
  "type": "data",
  "description": "BCa bootstrap CI, leave-one-out, and leave-two-out sensitivity analysis for R1-8B hidden states vs text FPR comparison. BCa CI [0.006, 0.159] excludes 0, BCa p=0.033. LOO: 5/43 traces flip significance. LTO: 193/903 pairs (21.4%) flip.",
  "project": "contrastive_trace_safety",
  "content": "{\n  \"model\": \"r1-8b\", \"layer\": 14, \"window\": 15, \"n_test_traces\": 43,\n  \"delta_fpr_mean\": 0.0736,\n  \"bca_ci_95\": [0.005817, 0.158995],\n  \"contains_zero\": false,\n  \"bca_p_value\": 0.0331,\n  \"z0\": 0.0374, \"acceleration\": 0.0209,\n  \"leave_one_out\": {\"n_flipped\": 5, \"n_total\": 43},\n  \"leave_two_out\": {\"n_flipped\": 193, \"n_total\": 903, \"fraction\": 0.214}\n}",
  "content_filename": "a4_bca_fpr_summary.json",
  "tags": "['bootstrap', 'bca', 'fpr', 'r1-8b', 'sensitivity']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r14_a4_bca_r1_8b_fpr_20260518T162942",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "A4 BCa Bootstrap CI for R1-8B FPR",
    "type": "data",
    "description": "BCa bootstrap CI, leave-one-out, and leave-two-out sensitivity analysis for R1-8B hidden states vs text FPR comparison. BCa CI [0.006, 0.159] excludes 0, BCa p=0.033. LOO: 5/43 traces flip significance. LTO: 193/903 pairs (21.4%) flip.",
    "project": "contrastive_trace_safety",
    "content": "{\n  \"model\": \"r1-8b\", \"layer\": 14, \"window\": 15, \"n_test_traces\": 43,\n  \"delta_fpr_mean\": 0.0736,\n  \"bca_ci_95\": [0.005817, 0.158995],\n  \"contains_zero\": false,\n  \"bca_p_value\": 0.0331,\n  \"z0\": 0.0374, \"acceleration\": 0.0209,\n  \"leave_one_out\": {\"n_flipped\": 5, \"n_total\": 43},\n  \"leave_two_out\": {\"n_flipped\": 193, \"n_total\": 903, \"fraction\": 0.214}\n}",
    "content_filename": "a4_bca_fpr_summary.json",
    "tags": "['bootstrap', 'bca', 'fpr', 'r1-8b', 'sensitivity']"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-18T16:33:56.419474+00:00_

Error executing tool register_artifact: 1 validation error for register_artifactArguments
content
  Input should be a valid string [type=string_type, input_value={'model': 'r1-8b', 'layer...903, 'fraction': 0.214}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r14_a4_bca_r1_8b_fpr_20260518T162942",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-18T16:33:56.419596+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "A4 BCa Bootstrap CI for R1-8B FPR",
  "type": "data",
  "description": "BCa bootstrap CI, leave-one-out, and leave-two-out sensitivity analysis for R1-8B hidden states vs text FPR comparison. BCa CI [0.006, 0.159] excludes 0, BCa p=0.033. LOO: 5/43 traces flip significance. LTO: 193/903 pairs (21.4%) flip.",
  "project": "contrastive_trace_safety",
  "content": "{\"model\": \"r1-8b\", \"layer\": 14, \"window\": 15, \"n_test_traces\": 43, \"delta_fpr_mean\": 0.0736, \"bca_ci_95\": [0.005817, 0.158995], \"contains_zero\": false, \"bca_p_value\": 0.0331, \"z0\": 0.0374, \"acceleration\": 0.0209, \"leave_one_out\": {\"n_flipped\": 5, \"n_total\": 43}, \"leave_two_out\": {\"n_flipped\": 193, \"n_total\": 903, \"fraction\": 0.214}}",
  "content_filename": "a4_bca_fpr_summary.json",
  "tags": "['bootstrap', 'bca', 'fpr', 'r1-8b', 'sensitivity']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r14_a4_bca_r1_8b_fpr_20260518T162942",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "A4 BCa Bootstrap CI for R1-8B FPR",
    "type": "data",
    "description": "BCa bootstrap CI, leave-one-out, and leave-two-out sensitivity analysis for R1-8B hidden states vs text FPR comparison. BCa CI [0.006, 0.159] excludes 0, BCa p=0.033. LOO: 5/43 traces flip significance. LTO: 193/903 pairs (21.4%) flip.",
    "project": "contrastive_trace_safety",
    "content": "{\"model\": \"r1-8b\", \"layer\": 14, \"window\": 15, \"n_test_traces\": 43, \"delta_fpr_mean\": 0.0736, \"bca_ci_95\": [0.005817, 0.158995], \"contains_zero\": false, \"bca_p_value\": 0.0331, \"z0\": 0.0374, \"acceleration\": 0.0209, \"leave_one_out\": {\"n_flipped\": 5, \"n_total\": 43}, \"leave_two_out\": {\"n_flipped\": 193, \"n_total\": 903, \"fraction\": 0.214}}",
    "content_filename": "a4_bca_fpr_summary.json",
    "tags": "['bootstrap', 'bca', 'fpr', 'r1-8b', 'sensitivity']"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-18T16:33:56.419744+00:00_

Error executing tool register_artifact: 1 validation error for register_artifactArguments
content
  Input should be a valid string [type=string_type, input_value={'model': 'r1-8b', 'layer...903, 'fraction': 0.214}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r14_a4_bca_r1_8b_fpr_20260518T162942",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-18T16:33:56.419861+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "A4 BCa Bootstrap CI for R1-8B FPR",
  "type": "data",
  "description": "BCa bootstrap CI, leave-one-out, and leave-two-out sensitivity for R1-8B HS vs text FPR. BCa CI [0.006, 0.159] excludes 0, BCa p=0.033. LOO: 5/43 flip. LTO: 193/903 (21.4%) flip.",
  "project": "contrastive_trace_safety",
  "content": "Full results at server: /root/autodl-tmp/contrastive_trace_safety/artifacts/r14_a4_bca_fpr/bca_results.json\n\nBCa 95% CI for delta_FPR (text - HS): [0.005817, 0.158995]\nContains 0: No\nBCa p-value: 0.0331\nz0=0.0374, acceleration=0.0209\n\nLeave-one-out: 5/43 traces removal causes p > 0.05\nLeave-two-out: 193/903 pairs (21.4%) removal causes p > 0.05",
  "content_filename": "a4_bca_fpr_summary.txt",
  "tags": "['bootstrap', 'bca', 'fpr', 'r1-8b', 'sensitivity']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r14_a4_bca_r1_8b_fpr_20260518T162942",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "A4 BCa Bootstrap CI for R1-8B FPR",
    "type": "data",
    "description": "BCa bootstrap CI, leave-one-out, and leave-two-out sensitivity for R1-8B HS vs text FPR. BCa CI [0.006, 0.159] excludes 0, BCa p=0.033. LOO: 5/43 flip. LTO: 193/903 (21.4%) flip.",
    "project": "contrastive_trace_safety",
    "content": "Full results at server: /root/autodl-tmp/contrastive_trace_safety/artifacts/r14_a4_bca_fpr/bca_results.json\n\nBCa 95% CI for delta_FPR (text - HS): [0.005817, 0.158995]\nContains 0: No\nBCa p-value: 0.0331\nz0=0.0374, acceleration=0.0209\n\nLeave-one-out: 5/43 traces removal causes p > 0.05\nLeave-two-out: 193/903 pairs (21.4%) removal causes p > 0.05",
    "content_filename": "a4_bca_fpr_summary.txt",
    "tags": "['bootstrap', 'bca', 'fpr', 'r1-8b', 'sensitivity']"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-18T16:33:56.420005+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260518_0ab563\", \"name\": \"A4 BCa Bootstrap CI for R1-8B FPR\", \"type\": \"data\", \"description\": \"BCa bootstrap CI, leave-one-out, and leave-two-out sensitivity for R1-8B HS vs text FPR. BCa CI [0.006, 0.159] excludes 0, BCa p=0.033. LOO: 5/43 flip. LTO: 193/903 (21.4%) flip.\", \"path\": \"projects/contrastive_trace_safety/artifacts/_project/data/a4_bca_fpr_summary.txt\", \"url\": null, \"project\": \"contrastive_trace_safety\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-18T16:33:47.855179+00:00\", \"tags\": [\"bootstrap\", \"bca\", \"fpr\", \"r1-8b\", \"sensitivity\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r14_a4_bca_r1_8b_fpr_20260518T162942",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-18T16:33:56.420165+00:00_

Results:

```
BCa 95% CI for ΔFPR (text - HS): [0.005817, 0.158995]
Contains 0: No
BCa p-value: 0.0331

Leave-one-out sensitivity:
- 5/43 traces: removal causes p > 0.05
- Most influential trace: idx 3 (p without = 0.062)
- Least influential: idx 30 (p without = 0.010)

Leave-two-out:
- 193/903 pairs: removal causes p > 0.05 (21.4%)
```

BCa CI excludes 0 with a tighter p-value (0.033) than the original percentile bootstrap (0.044), confirming the FPR difference is statistically robust. The bias correction (z0=0.037) and acceleration (a=0.021) are both small, indicating the original percentile CI was already reasonable.

Sensitivity: 5 individual traces (idx 3, 6, 8, 28, 38) can individually flip significance if removed. All 5 are high-leverage outliers with ΔFPR 0.5-0.7 (text FPR far exceeding HS FPR). 21.4% of trace pairs can flip significance. The signal is real but partly driven by these extreme cases.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_r14_a4_bca_r1_8b_fpr_20260518T162942"
}
```

</details>

---
