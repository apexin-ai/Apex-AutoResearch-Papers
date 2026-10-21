# code mahalanobis r1 32b qwq

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 0
- **Tool calls:** 15
- **Original source:** `logs/chats/worker_code_mahalanobis_r1_32b_qwq_20260517T145609.jsonl`
- **Structured JSON:** [`9f335efb87a435464c5d.json`](../../sessions/9f/9f335efb87a435464c5d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

31 recorded events

### Tool call

_source line 1 · 2026-05-17T14:59:00.684864+00:00_

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
  "session": "worker_code_mahalanobis_r1_32b_qwq_20260517T145609",
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

_source line 2 · 2026-05-17T14:59:00.685336+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_mahalanobis_r1_32b_qwq_20260517T145609",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T14:59:00.685621+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "find /root/autodl-tmp/contrastive_trace_safety/ -name \"*mahalanobis*\" -name \"*.py\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_mahalanobis_r1_32b_qwq_20260517T145609",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "find /root/autodl-tmp/contrastive_trace_safety/ -name \"*mahalanobis*\" -name \"*.py\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T14:59:00.685806+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/contrastive_trace_safety/src/experiments/trajguard_mahalanobis.py\\n/root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_r3_mahalanobis_ot7b.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.89}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_mahalanobis_r1_32b_qwq_20260517T145609",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T14:59:00.685944+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "ls /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r3_mahalanobis_ot7b/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_mahalanobis_r1_32b_qwq_20260517T145609",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "ls /root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r3_mahalanobis_ot7b/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T14:59:00.686075+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_mahalanobis_r1_32b_qwq_20260517T145609",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T14:59:00.686201+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "find /root/autodl-tmp/contrastive_trace_safety/data -type d -name \"*32b*\" -o -type d -name \"*qwq*\" -o -type d -name \"*QwQ*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_mahalanobis_r1_32b_qwq_20260517T145609",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "find /root/autodl-tmp/contrastive_trace_safety/data -type d -name \"*32b*\" -o -type d -name \"*qwq*\" -o -type d -name \"*QwQ*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T14:59:00.686328+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"find: '/root/autodl-tmp/contrastive_trace_safety/data': No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_mahalanobis_r1_32b_qwq_20260517T145609",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T14:59:00.686450+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "cat /root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_r3_mahalanobis_ot7b.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_mahalanobis_r1_32b_qwq_20260517T145609",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "cat /root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_r3_mahalanobis_ot7b.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T14:59:00.686771+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Mahalanobis distance baseline on OT-7B Layer 16.\\\"\\\"\\\"\\n\\nimport sys, json, time\\nimport numpy as np\\nimport torch\\nfrom pathlib import Path\\nfrom sklearn.decomposition import PCA\\nfrom sklearn.covariance import LedoitWolf\\n\\nHS_DIR = Path(\\\"/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_ot7b\\\")\\nOUT_DIR = Path(\\\"/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r3_mahalanobis_ot7b\\\")\\nOUT_DIR.mkdir(parents=True, exist_ok=True)\\n\\nSEED = 42\\nTRAIN_RATIO = 0.6\\nVAL_RATIO = 0.2\\nLAYER_IDX = 17\\nPCA_DIMS = [16, 32, 64, 128]\\nTHRESHOLD_PERCENTILES = [50, 75, 90, 95]\\nDETECTION_WINDOWS = [3, 5]\\n\\n\\ndef load_all_traces():\\n    \\\"\\\"\\\"Load all traces with hidden states into memory at once.\\\"\\\"\\\"\\n    traces = []\\n    for f in sorted(HS_DIR.glob(\\\"*.pt\\\")):\\n        d = torch.load(f, map_location=\\\"cpu\\\", weights_only=False)\\n        cp = d.get(\\\"commitment_point\\\")\\n        if cp is None:\\n            continue\\n        hs = d[\\\"hidden_states\\\"][:, LAYER_IDX, :].float().numpy()\\n        traces.append({\\n            \\\"trace_id\\\": d[\\\"trace_id\\\"],\\n            \\\"commitment_point\\\": int(cp),\\n            \\\"step_labels\\\": d[\\\"step_labels\\\"] if isinstance(d[\\\"step_labels\\\"], list) else d[\\\"step_labels\\\"].tolist(),\\n            \\\"num_steps\\\": int(d[\\\"num_sentences\\\"]),\\n            \\\"hs\\\": hs,\\n        })\\n    return traces\\n\\n\\ndef split_data(traces, seed=SEED):\\n    rng = np.random.default_rng(seed)\\n    idx = rng.permutation(len(traces))\\n    n_train = int(len(traces) * TRAIN_RATIO)\\n    n_val = int(len(traces) * VAL_RATIO)\\n    return (\\n        [traces[i] for i in idx[:n_train]],\\n        [traces[i] for i in idx[n_train:n_train+n_val]],\\n        [traces[i] for i in idx[n_train+n_val:]],\\n    )\\n\\n\\ndef collect_pre_commitment_hs(traces):\\n    parts = 
…[truncated 7361 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_mahalanobis_r1_32b_qwq_20260517T145609",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T14:59:00.686974+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "find /root/autodl-tmp/contrastive_trace_safety -type d -maxdepth 3",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_mahalanobis_r1_32b_qwq_20260517T145609",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "find /root/autodl-tmp/contrastive_trace_safety -type d -maxdepth 3",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T14:59:00.687152+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/contrastive_trace_safety\\n/root/autodl-tmp/contrastive_trace_safety/artifacts\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/probes\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/diagnostics\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_005_trajguard\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_013_text_baseline\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_006_bootstrap\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_014_bocpd\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_015_fpr\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_001b\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_r1_32b\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_001a\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/r1_8b_balanced_recompute\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_003_cross_transfer\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/m001_layer_fix\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_c2_control\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/r1_8b_bootstrap_hs_text\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/qwq_text_verify\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_007_window_ablation\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/acc_precision_bootstrap\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/text_window_ablation_r1_8b\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/paper_data\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/figures\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/figures/paper\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/qwq_paired_bootstrap_w5\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/r1_32b_paired_bo
…[truncated 2914 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_mahalanobis_r1_32b_qwq_20260517T145609",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T14:59:00.687332+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "ls /root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_r1_32b/ | head -5",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_mahalanobis_r1_32b_qwq_20260517T145609",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "ls /root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_r1_32b/ | head -5",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T14:59:00.687461+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_mahalanobis_r1_32b_qwq_20260517T145609",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T14:59:00.687582+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "ls /root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b/ | head -5",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_mahalanobis_r1_32b_qwq_20260517T145609",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "ls /root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b/ | head -5",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T14:59:00.687729+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_mahalanobis_r1_32b_qwq_20260517T145609",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T14:59:00.687850+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "ls /root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_r1_32b/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_mahalanobis_r1_32b_qwq_20260517T145609",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "ls /root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_r1_32b/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-17T14:59:00.688040+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0340a9c152a84e88a1bb1a1b0c1ece69.pt\\n03ab25e611ab42d5bab0e091b2bfb4db.pt\\n03e731a127e4403ea8b4f6b0da22d40b.pt\\n065cd061633b48ffba91c8ab8468aee5.pt\\n072fffe312724613b373f5e9423bec9e.pt\\n077d0c46eeaa4d26bcf796ff257b4107.pt\\n078bffd5b7bf41229684593b116e9b64.pt\\n0d024d64ea6f4fe7a326c146bf004b9d.pt\\n0e290c942d794d6a9b60fade0b82ba11.pt\\n133bb30152c348aa914bef1a46cd5065.pt\\n1366b9a156ef444eaf0fabf28b0fd17b.pt\\n14745efac5e24605833ff1a36d3bea9c.pt\\n1616070d73a044c9b80fd6fb09bc7dad.pt\\n181fe09ad4d14befa56def067985a204.pt\\n192fc3f6944947f5a8f9bfa4bf79bc72.pt\\n1ddd805c9c69471bb91971a3ee33c32c.pt\\n2011a70d7e5f4cc681606c655581d0d4.pt\\n2013ecb74dda42488eb7caad35193314.pt\\n21c16ece865541588c7ec69bea892c79.pt\\n2239e2c5ff6b47fe88e4d70829aa02e7.pt\\n225661d7e1fb4c3c88693d53091206ca.pt\\n22c71ef412f042b3b1eae36f3b8d0a57.pt\\n23ceb4debb184eeabaa722b5bc148171.pt\\n2426e92a447a414c95dcfb4dbdbecd8b.pt\\n297fc59b3baa47e3a6365c5bec100ad2.pt\\n2989f4f4b129410e99ecccdd81fd9fea.pt\\n2b065031a798402791fbc376a7f84d7c.pt\\n2b91b6c7c2814afba34da843197964c6.pt\\n2c0260c7322b4d0c98c751ecb6d55ee5.pt\\n2d2b904c8d7946b9ae11b460e3d503fa.pt\\n2d3d6eec4132486986192862f7e9961c.pt\\n2dd179bd68cc4f20a9231b1d96328d99.pt\\n2e340305abb747b98426f999b57586a3.pt\\n2e6a68c203c44e9886a106da957bfafb.pt\\n31337720fdd9418492a4d118fba549c6.pt\\n3318d4e152204670877251dd9e73d999.pt\\n33c6a82d38b14a7480065fd7cc7a52d8.pt\\n365cab697ffe461a80ddb6cd2b7c7ca1.pt\\n36b9c92c286d4529acec148e5c04eb2f.pt\\n3a8da7148d6a40b8a093713502df1735.pt\\n3aa7b05627f04350bc7141d9c5402799.pt\\n3f1e1cfdb7b74292a2c483219b6a3a35.pt\\n40ce79d4a62549339ad84b32eaaf38ab.pt\\n42ce50f59c454232903c343fd934ffd7.pt\\n451e48b93ec3417badeb7eec1d1e606f.pt\\n4522b1a20a0c4514859150cb4a40cb29.pt\\n453cd67cf5c44bcea3cf4d4a20b08f29.pt\\n45f0198e7b054e21b358a3ddf5b25233.pt\\n474c2b11e4614bdc81fee0b0e1ccf21c.pt\\n4796bb358cea4cafa963d7b8a7c9f776.pt\\n488a8b25d77445cd850d416ff1752f8d.pt\\n4a0e76
…[truncated 1986 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_mahalanobis_r1_32b_qwq_20260517T145609",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-17T14:59:00.688205+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "ls /root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_mahalanobis_r1_32b_qwq_20260517T145609",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "ls /root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-17T14:59:00.688363+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"004ee4398ad043f88590dc868baed39c.pt\\n0067d71cad0d4adba09c0ca1ba6de9f4.pt\\n043bdc40cc3a425da4a80dd2c3b54093.pt\\n069b39dd44c749edac6b2b9a22000146.pt\\n069c405acb984a728d6d4b4a4403dc2e.pt\\n08c889f0d70b4a9cb94a1c50eb7809c3.pt\\n08f53c080455450a875a13e071520fcc.pt\\n09e1cee11dc944ae89c4a077451046cc.pt\\n0c8ae288d6de43058d6a4c7dc97f72b8.pt\\n104fb6e29e284eadb21d6e934f30ac32.pt\\n110ec3ef86634737a0cd9c990c736659.pt\\n125a765ce4e1440c8375cb947cc74891.pt\\n1284370b1811430a8029ce530e1b1609.pt\\n14998b617a6b425e81749647c7a00f8b.pt\\n14e4e1baf5be42b0afe19deca15703a5.pt\\n1536ec9382d3409292a65544836eff18.pt\\n163bbe567d7649ffb07bd25aaceacc49.pt\\n16c401658cf84881927b644dee22f263.pt\\n17e198e535d340659b829e4a3a677d7e.pt\\n184cda0553f945c5bfd7bc5e4487b2e8.pt\\n1865bac475df48dc82ec59ffa7aefa99.pt\\n19ee776ab7c64da19403e822bb265156.pt\\n1a2e3b84d89b439f926c11c459d34f5c.pt\\n1a66328ff3704e7ab99d11ac49ef2e94.pt\\n1c167cf073234d54a3aaf0931ed64771.pt\\n1ebb5b137072402eba8e12d2f4a6112e.pt\\n21f936ea97f94c848f7d4f047470766c.pt\\n22609944c6dc46c79544d5e2a98d22a0.pt\\n236c6c98cf7046efb199379307454d69.pt\\n256dfa73942345f09beb2bfe933b0b1b.pt\\n25993fa332954b7c831a1220c1a56ebc.pt\\n278be80b336641ddb92b108575ff0ebd.pt\\n298cb1454adb4b6da16ca2445189ed1e.pt\\n2a2487286db5440a8a6a08095b21f90e.pt\\n2b75bd31301f41b1ad3f2c81925c8e88.pt\\n2c83d4c6db1548438b235222b56be3bf.pt\\n301054e81ece4f59992d2e46de39d60b.pt\\n30fe394a8d2d4f23be5e87ce958a2c0e.pt\\n32ed854363d241cf87863eaf14cbcc24.pt\\n33e402d236e148a8ba82c0ee4ceee012.pt\\n3478ec8ed5dd459a92c54cdb13c888ee.pt\\n34a8c0bbc9d94d559a0990a7dbe3dea4.pt\\n36524c4d9c574d238d5ee826198c6a48.pt\\n37af416bd3b94220a9b84a29044c796a.pt\\n3808a31861724e759e12702bcf58535e.pt\\n3accbfb57c714ffdaf1dc03babb19e69.pt\\n3b70c05b41fa4aa3858e6e7d586aecaf.pt\\n3f98b7efccf249108d46c8d8c35aa301.pt\\n3fa300f79a5e48b2a2d6ce3a69588b1d.pt\\n3fea40a6688448b898bae5930a4ee96e.pt\\n40a6788423024e4f977bbb7ce01d68b7.pt\\n4114a1
…[truncated 1796 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_mahalanobis_r1_32b_qwq_20260517T145609",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-17T14:59:00.688551+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "find /root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_r1_32b -name \"*.pt\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_mahalanobis_r1_32b_qwq_20260517T145609",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "find /root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_r1_32b -name \"*.pt\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-17T14:59:00.688844+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_r1_32b/0340a9c152a84e88a1bb1a1b0c1ece69.pt\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_r1_32b/50ff71894ca142608c5b715ef0466541.pt\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_r1_32b/7aeb2669e5f547deaa9325a6ad59b233.pt\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_r1_32b/2d3d6eec4132486986192862f7e9961c.pt\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_r1_32b/36b9c92c286d4529acec148e5c04eb2f.pt\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_r1_32b/5d9633889311476b933f5cf024355466.pt\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_r1_32b/4e72fcb872934b969333f9cfe6697552.pt\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_r1_32b/33c6a82d38b14a7480065fd7cc7a52d8.pt\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_r1_32b/297fc59b3baa47e3a6365c5bec100ad2.pt\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_r1_32b/4796bb358cea4cafa963d7b8a7c9f776.pt\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_r1_32b/31337720fdd9418492a4d118fba549c6.pt\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_r1_32b/0e290c942d794d6a9b60fade0b82ba11.pt\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_r1_32b/4fac5203d70445608a28ca49b7aeb78a.pt\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_r1_32b/5ce8318698004ffdab4cc315c30f9329.pt\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_r1_32b/743f1055a2594eecb37f0846f0846737.pt\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_r1_32b/60b3c307f8234d5c818faf996a99e084.pt\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_r1_32b/2b91b6c7c2814afba34da843197964c6.pt\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/hidde
…[truncated 6347 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_mahalanobis_r1_32b_qwq_20260517T145609",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-17T14:59:00.689009+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "find /root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b -name \"*.pt\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_mahalanobis_r1_32b_qwq_20260517T145609",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "find /root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b -name \"*.pt\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-17T14:59:00.689206+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b/37af416bd3b94220a9b84a29044c796a.pt\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b/298cb1454adb4b6da16ca2445189ed1e.pt\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b/8060adc175bf428db45d5d6b5eac199e.pt\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b/1c167cf073234d54a3aaf0931ed64771.pt\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b/19ee776ab7c64da19403e822bb265156.pt\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b/654bf91248e340ddb10ee23ed78074f6.pt\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b/46989b57c2cc4b8792a14f3001d2951f.pt\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b/069b39dd44c749edac6b2b9a22000146.pt\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b/66b7d883496449fe8110a8cd6269fd01.pt\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b/721e2f964dad4632aeaca6dcc2e5fb9c.pt\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b/25993fa332954b7c831a1220c1a56ebc.pt\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b/5b207dd7221247c8a885b696c019ff6c.pt\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b/3b70c05b41fa4aa3858e6e7d586aecaf.pt\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b/7c83d8b177bb477f8a2850cedc8c3510.pt\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b/7647a80bc55a467285dcc89e8773fb99.pt\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b/4774b77e27844d01bd6b8ddcaffee466.pt\\n/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b/63dcd4dae6264692aed628b029fa3c24.pt\\n/root/autodl-tmp/contrastive_trace_safet
…[truncated 6347 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_mahalanobis_r1_32b_qwq_20260517T145609",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-17T14:59:00.689388+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "source /root/miniconda3/bin/activate && python3 -c \"\nimport torch\nfrom pathlib import Path\n\n# Check R1-32B\nr1_dir = Path('/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_r1_32b')\nr1_files = sorted(r1_dir.glob('*.pt'))\nprint(f'R1-32B: {len(r1_files)} .pt files')\nd = torch.load(r1_files[0], map_location='cpu', weights_only=False)\nprint('Keys:', list(d.keys()))\nprint('hidden_states shape:', d['hidden_states'].shape)\nprint('commitment_point:', d.get('commitment_point'))\nprint('num_sentences:', d.get('num_sentences'))\nprint('step_labels type:', type(d.get('step_labels')))\n\n# Check QwQ\nqwq_dir = Path('/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b')\nqwq_files = sorted(qwq_dir.glob('*.pt'))\nprint(f'\\nQwQ-32B: {len(qwq_files)} .pt files')\nd2 = torch.load(qwq_files[0], map_location='cpu', weights_only=False)\nprint('Keys:', list(d2.keys()))\nprint('hidden_states shape:', d2['hidden_states'].shape)\nprint('commitment_point:', d2.get('commitment_point'))\nprint('num_sentences:', d2.get('num_sentences'))\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_mahalanobis_r1_32b_qwq_20260517T145609",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "source /root/miniconda3/bin/activate && python3 -c \"\nimport torch\nfrom pathlib import Path\n\n# Check R1-32B\nr1_dir = Path('/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_r1_32b')\nr1_files = sorted(r1_dir.glob('*.pt'))\nprint(f'R1-32B: {len(r1_files)} .pt files')\nd = torch.load(r1_files[0], map_location='cpu', weights_only=False)\nprint('Keys:', list(d.keys()))\nprint('hidden_states shape:', d['hidden_states'].shape)\nprint('commitment_point:', d.get('commitment_point'))\nprint('num_sentences:', d.get('num_sentences'))\nprint('step_labels type:', type(d.get('step_labels')))\n\n# Check QwQ\nqwq_dir = Path('/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b')\nqwq_files = sorted(qwq_dir.glob('*.pt'))\nprint(f'\\nQwQ-32B: {len(qwq_files)} .pt files')\nd2 = torch.load(qwq_files[0], map_location='cpu', weights_only=False)\nprint('Keys:', list(d2.keys()))\nprint('hidden_states shape:', d2['hidden_states'].shape)\nprint('commitment_point:', d2.get('commitment_point'))\nprint('num_sentences:', d2.get('num_sentences'))\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-17T14:59:00.689534+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"R1-32B: 100 .pt files\\nKeys: ['hidden_states', 'trace_id', 'num_sentences', 'commitment_point', 'step_labels', 'query']\\nhidden_states shape: torch.Size([36, 64, 5120])\\ncommitment_point: 32\\nnum_sentences: 36\\nstep_labels type: &lt;class 'list'>\\n\\nQwQ-32B: 95 .pt files\\nKeys: ['hidden_states', 'trace_id', 'num_sentences', 'commitment_point', 'step_labels', 'query']\\nhidden_states shape: torch.Size([48, 64, 5120])\\ncommitment_point: 8\\nnum_sentences: 48\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.81}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_mahalanobis_r1_32b_qwq_20260517T145609",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-17T14:59:00.689811+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "cat > /root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_r3_mahalanobis_32b.py << 'PYEOF'\n\"\"\"Mahalanobis distance baseline on R1-32B (Layer 63) and QwQ-32B (Layer 60).\"\"\"\n\nimport sys, json, time\nimport numpy as np\nimport torch\nfrom pathlib import Path\nfrom sklearn.decomposition import PCA\nfrom sklearn.covariance import LedoitWolf\n\nSEED = 42\nTRAIN_RATIO = 0.6\nVAL_RATIO = 0.2\nPCA_DIMS = [16, 32, 64, 128]\nTHRESHOLD_PERCENTILES = [50, 75, 90, 95]\nDETECTION_WINDOWS = [3, 5]\n\nMODELS = {\n    \"R1-32B\": {\n        \"hs_dir\": Path(\"/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_r1_32b\"),\n        \"out_dir\": Path(\"/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r3_mahalanobis_r1_32b\"),\n        \"layer_idx\": 63,\n        \"layer_name\": 63,\n        \"hidden_dim\": 5120,\n    },\n    \"QwQ-32B\": {\n        \"hs_dir\": Path(\"/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b\"),\n        \"out_dir\": Path(\"/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r3_mahalanobis_qwq\"),\n        \"layer_idx\": 60,\n        \"layer_name\": 60,\n        \"hidden_dim\": 5120,\n    },\n}\n\n\ndef load_all_traces(hs_dir, layer_idx):\n    traces = []\n    for f in sorted(hs_dir.glob(\"*.pt\")):\n        d = torch.load(f, map_location=\"cpu\", weights_only=False)\n        cp = d.get(\"commitment_point\")\n        if cp is None:\n            continue\n        hs = d[\"hidden_states\"][:, layer_idx, :].float().numpy()\n        traces.append({\n            \"trace_id\": d[\"trace_id\"],\n            \"commitment_point\": int(cp),\n            \"step_labels\": d[\"step_labels\"] if isinstance(d[\"step_labels\"], list) else d[\"step_labels\"].tolist(),\n            \"num_steps\": int(d[\"num_sentences\"]),\n            \"hs\": hs,\n        })\n    return traces\n\n\ndef split_data(traces, seed=SEED):\n    rng = np.random.default_rng(seed)\n    idx = rng.permutation(len(traces))\n    n_train = int(len(traces) * TRAIN_RATIO)\n    n_val = int(len(traces) * VAL_RATIO)\n    return (\n        [traces[i] for i in idx[:n_train]],\n        [traces[i] for i in idx[n_train:n_train+n_val]],\n        [traces[i] for i in idx[n_train+n_val:]],\n    )\n\n\ndef collect_pre_commitment_hs(traces):\n    parts = []\n    for t in traces:\n        cp = t[\"commitment_point\"]\n        if cp > 0:\n            parts.append(t[\"hs\"][:cp])\n    return np.concatenate(parts, axis=0)\n\n\ndef collect_post_commitment_hs(traces):\n    parts = []\n    for t in traces:\n        cp = t[\"commitment_point\"]\n        if cp < t[\"hs\"].shape[0]:\n            parts.append(t[\"hs\"][cp:])\n    return np.concatenate(parts, axis=0)\n\n\ndef first_crossing(md_seq, threshold, k):\n    n = len(md_seq)\n    if n < k:\n        return None\n    for i in range(n - k + 1):\n        if np.all(md_seq[i:i+k] > threshold):\n            return i\n    return None\n\n\ndef evaluate_crossing(test_traces, md_fn, safe_val_md, config_name):\n    results = []\n    for k in DETECTION_WINDOWS:\n        for pctl in THRESHOLD_PERCENTILES:\n            threshold = float(np.percentile(safe_val_md, pctl))\n            detected = 0\n            false_alarms = 0\n            leads = []\n            n_traces = 0\n\n            for trace in test_traces:\n                n_traces += 1\n                md_seq = md_fn(trace[\"hs\"])\n                cp = trace[\"commitment_point\"]\n                fcp = first_crossing(md_seq, threshold, k)\n                if fcp is not None:\n                    detected += 1\n                    leads.append(cp - fcp)\n                    if fcp >= cp:\n                        false_alarms += 0\n                    # Check false alarm: detection in safe region\n                safe_md = md_fn(trace[\"hs\"][:cp]) if cp > 0 else np.array([])\n                if len(safe_md) >= k:\n                    fa_cross = first_crossing(safe_md, threshold, k)\n                    if fa_cross is not None:\n                        false_alarms += 1\n\n            tp_rate = detected / n_traces if n_traces > 0 else 0.0\n            fa_rate = false_alarms / n_traces if n_traces > 0 else 0.0\n            results.append({\n                \"config\": config_name,\n                \"detection_window\": k,\n                \"threshold_percentile\": pctl,\n                \"threshold_value\": threshold,\n                \"crossing_rate\": tp_rate,\n                \"false_alarm_rate\": fa_rate,\n                \"lead_time_mean\": float(np.mean(leads)) if leads else None,\n                \"lead_time_median\": float(np.median(leads)) if leads else None,\n                \"n_traces\": n_traces,\n                \"n_detected\": detected,\n                \"n_false_alarms\": false_alarms,\n            })\n    return results\n\n\ndef run_model(model_name, cfg):\n    t0 = time.time()\n    print(\"=\" * 70)\n    print(f\"MAHALANOBIS DISTANCE: {model_name} Layer {cfg['layer_name']}\")\n    print(\"=\" * 70)\n\n    cfg[\"out_dir\"].mkdir(parents=True, exist_ok=True)\n\n    print(\"Loading traces...\")\n    traces = load_all_traces(cfg[\"hs_dir\"], cfg[\"layer_idx\"])\n    print(f\"Loaded {len(traces)} traces ({time.time()-t0:.1f}s)\")\n\n    train, val, test = split_data(traces)\n    print(f\"Split: train={len(train)}, val={len(val)}, test={len(test)}\")\n\n    print(\"\\nCollecting pre/post commitment hidden states...\")\n    X_safe_train = collect_pre_commitment_hs(train)\n    X_safe_val = collect_pre_commitment_hs(val)\n    X_post_train = collect_post_commitment_hs(train)\n    print(f\"Safe train steps: {X_safe_train.shape[0]}, Safe val steps: {X_safe_val.shape[0]}\")\n    print(f\"Post train steps: {X_post_train.shape[0]}\")\n\n    md_stats = {}\n    all_results = []\n\n    for pca_dim in PCA_DIMS:\n        config_name = f\"pca_{pca_dim}\"\n        print(f\"\\n--- PCA {pca_dim} + LedoitWolf ---\")\n\n        pca = PCA(n_components=pca_dim, random_state=SEED)\n        pca.fit(X_safe_train)\n        X_tr = pca.transform(X_safe_train)\n        X_val_tr = pca.transform(X_safe_val)\n        X_post_tr = pca.transform(X_post_train)\n\n        lw = LedoitWolf()\n        lw.fit(X_tr)\n        _mean = lw.location_\n        _prec = lw.precision_\n\n        def _md(X, _m=_mean, _p=_prec, _pca=pca):\n            Xt = _pca.transform(X)\n            diff = Xt - _m\n            return np.sqrt(np.sum(diff @ _p * diff, axis=1))\n\n        safe_val_md = _md(X_safe_val)\n        post_md = _md(X_post_train)\n\n        md_stats[config_name] = {\n            \"safe_md_mean\": float(safe_val_md.mean()),\n            \"safe_md_std\": float(safe_val_md.std()),\n            \"post_md_mean\": float(post_md.mean()),\n            \"post_md_std\": float(post_md.std()),\n            \"separation\": float(post_md.mean() - safe_val_md.mean()),\n        }\n        print(f\"  Safe MD: mean={safe_val_md.mean():.4f}, std={safe_val_md.std():.4f}\")\n        print(f\"  Post MD: mean={post_md.mean():.4f}, std={post_md.std():.4f}\")\n        print(f\"  Separation: {post_md.mean() - safe_val_md.mean():.4f}\")\n\n        configs = evaluate_crossing(test, _md, safe_val_md, config_name)\n        all_results.extend(configs)\n\n    # Summary\n    print(\"\\n\" + \"=\" * 90)\n    print(\"TOP-10 CONFIGS BY CROSSING RATE\")\n    print(\"=\" * 90)\n    sorted_configs = sorted(all_results, key=lambda c: (-c[\"crossing_rate\"], -(c[\"lead_time_mean\"] or -999)))\n    print(f\"{'Config':<16} {'K':<4} {'Pctl':<6} {'CrossRate':<12} {'FA_Rate':<10} {'LeadMean':<12} {'LeadMed':<10}\")\n    print(\"-\" * 80)\n    for c in sorted_configs[:10]:\n        lead_m = f\"{c['lead_time_mean']:.1f}\" if c['lead_time_mean'] is not None else \"N/A\"\n        lead_med = f\"{c['lead_time_median']:.1f}\" if c['lead_time_median'] is not None else \"N/A\"\n        print(f\"{c['config']:<16} {c['detection_window']:<4} p{c['threshold_percentile']:<5} \"\n              f\"{c['crossing_rate']:<12.3f} {c['false_alarm_rate']:<10.3f} {lead_m:<12} {lead_med:<10}\")\n\n    # Best configs for K=5\n    k5_configs = [c for c in all_results if c[\"detection_window\"] == 5]\n    best_k5 = max(k5_configs, key=lambda c: c[\"crossing_rate\"]) if k5_configs else None\n    k3_configs = [c for c in all_results if c[\"detection_window\"] == 3]\n    best_k3 = max(k3_configs, key=lambda c: c[\"crossing_rate\"]) if k3_configs else None\n\n    # Best PCA dim by separation\n    best_pca = max(md_stats.items(), key=lambda x: x[1][\"separation\"])\n\n    result = {\n        \"method\": \"trajguard_mahalanobis\",\n        \"model\": model_name,\n        \"layer\": cfg[\"layer_name\"],\n        \"layer_idx\": cfg[\"layer_idx\"],\n        \"hidden_dim\": cfg[\"hidden_dim\"],\n        \"n_traces\": len(traces),\n        \"split\": {\"train\": len(train), \"val\": len(val), \"test\": len(test)},\n        \"n_safe_train_steps\": int(X_safe_train.shape[0]),\n        \"n_safe_val_steps\": int(X_safe_val.shape[0]),\n        \"md_distribution_stats\": md_stats,\n        \"best_pca_config\": best_pca[0],\n        \"best_k3\": best_k3,\n        \"best_k5\": best_k5,\n        \"configs\": all_results,\n    }\n\n    output_path = cfg[\"out_dir\"] / \"results.json\"\n    with open(output_path, \"w\") as f:\n        json.dump(result, f, indent=2)\n    print(f\"\\nResults saved to {output_path}\")\n    print(f\"Time: {time.time()-t0:.1f}s\")\n\n    return result\n\n\ndef main():\n    t0 = time.time()\n    all_model_results = {}\n\n    for model_name, cfg in MODELS.items():\n        res = run_model(model_name, cfg)\n        all_model_results[model_name] = res\n\n    # 4-model comparison table\n    print(\"\\n\" + \"=\" * 100)\n    print(\"4-MODEL MAHALANOBIS COMPARISON (best PCA dim, K=5)\")\n    print(\"=\" * 100)\n\n    comparison = [\n        {\"model\": \"R1-8B\", \"layer\": \"L28\", \"safe_md\": 6.66, \"post_md\": 6.73,\n         \"separation\": 0.07, \"note\": \"previous result\"},\n        {\"model\": \"OT-7B\", \"layer\": \"L16\", \"safe_md\": 7.68, \"post_md\": 7.71,\n         \"separation\": 0.03, \"note\": \"previous result\"},\n    ]\n\n    for model_name, res in all_model_results.items():\n        best_pca = res[\"best_pca_config\"]\n        stats = res[\"md_distribution_stats\"][best_pca]\n        best_k5 = res[\"best_k5\"]\n        comparison.append({\n            \"model\": model_name,\n            \"layer\": f\"L{res['layer']}\",\n            \"safe_md\": stats[\"safe_md_mean\"],\n            \"post_md\": stats[\"post_md_mean\"],\n            \"separation\": stats[\"separation\"],\n            \"best_pca\": best_pca,\n            \"crossing_rate_k5\": best_k5[\"crossing_rate\"] if best_k5 else None,\n            \"fa_rate_k5\": best_k5[\"false_alarm_rate\"] if best_k5 else None,\n        })\n\n    print(f\"{'Model':<12} {'Layer':<8} {'safe_MD':<10} {'post_MD':<10} {'separation':<12} {'FA>=TP?':<10}\")\n    print(\"-\" * 70)\n    for c in comparison:\n        fa_ge_tp = \"\"\n        if \"fa_rate_k5\" in c and c.get(\"crossing_rate_k5\") is not None:\n            fa_ge_tp = \"YES\" if c[\"fa_rate_k5\"] >= c[\"crossing_rate_k5\"] else \"NO\"\n        elif c.get(\"note\") == \"previous result\":\n            fa_ge_tp = \"YES\"\n        print(f\"{c['model']:<12} {c['layer']:<8} {c['safe_md']:<10.2f} {c['post_md']:<10.2f} \"\n              f\"{c['separation']:<12.4f} {fa_ge_tp:<10}\")\n\n    print(f\"\\nTotal time: {time.time()-t0:.1f}s\")\n\n    # Conclusion\n    all_sep = [c[\"separation\"] for c in comparison]\n    if all(s < 0.5 for s in all_sep):\n        print(\"\\nCONCLUSION: 4/4 models show Mahalanobis separation ≈ 0. Method has no discriminative power.\")\n    else:\n        print(\"\\nCONCLUSION: Some models show non-trivial separation. Check details.\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"Script written.\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_mahalanobis_r1_32b_qwq_20260517T145609",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "cat > /root/autodl-tmp/contrastive_trace_safety/src/experiments/exp_r3_mahalanobis_32b.py << 'PYEOF'\n\"\"\"Mahalanobis distance baseline on R1-32B (Layer 63) and QwQ-32B (Layer 60).\"\"\"\n\nimport sys, json, time\nimport numpy as np\nimport torch\nfrom pathlib import Path\nfrom sklearn.decomposition import PCA\nfrom sklearn.covariance import LedoitWolf\n\nSEED = 42\nTRAIN_RATIO = 0.6\nVAL_RATIO = 0.2\nPCA_DIMS = [16, 32, 64, 128]\nTHRESHOLD_PERCENTILES = [50, 75, 90, 95]\nDETECTION_WINDOWS = [3, 5]\n\nMODELS = {\n    \"R1-32B\": {\n        \"hs_dir\": Path(\"/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_r1_32b\"),\n        \"out_dir\": Path(\"/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r3_mahalanobis_r1_32b\"),\n        \"layer_idx\": 63,\n        \"layer_name\": 63,\n        \"hidden_dim\": 5120,\n    },\n    \"QwQ-32B\": {\n        \"hs_dir\": Path(\"/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_qwq_32b\"),\n        \"out_dir\": Path(\"/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r3_mahalanobis_qwq\"),\n        \"layer_idx\": 60,\n        \"layer_name\": 60,\n        \"hidden_dim\": 5120,\n    },\n}\n\n\ndef load_all_traces(hs_dir, layer_idx):\n    traces = []\n    for f in sorted(hs_dir.glob(\"*.pt\")):\n        d = torch.load(f, map_location=\"cpu\", weights_only=False)\n        cp = d.get(\"commitment_point\")\n        if cp is None:\n            continue\n        hs = d[\"hidden_states\"][:, layer_idx, :].float().numpy()\n        traces.append({\n            \"trace_id\": d[\"trace_id\"],\n            \"commitment_point\": int(cp),\n            \"step_labels\": d[\"step_labels\"] if isinstance(d[\"step_labels\"], list) else d[\"step_labels\"].tolist(),\n            \"num_steps\": int(d[\"num_sentences\"]),\n            \"hs\": hs,\n        })\n    return traces\n\n\ndef split_data(traces, seed=SEED):\n    rng = np.random.default_rng(seed)\n    idx = rng.permutation(len(traces))\n    n_train = int(len(traces) * TRAIN_RATIO)\n    n_val = int(len(traces) * VAL_RATIO)\n    return (\n        [traces[i] for i in idx[:n_train]],\n        [traces[i] for i in idx[n_train:n_train+n_val]],\n        [traces[i] for i in idx[n_train+n_val:]],\n    )\n\n\ndef collect_pre_commitment_hs(traces):\n    parts = []\n    for t in traces:\n        cp = t[\"commitment_point\"]\n        if cp > 0:\n            parts.append(t[\"hs\"][:cp])\n    return np.concatenate(parts, axis=0)\n\n\ndef collect_post_commitment_hs(traces):\n    parts = []\n    for t in traces:\n        cp = t[\"commitment_point\"]\n        if cp < t[\"hs\"].shape[0]:\n            parts.append(t[\"hs\"][cp:])\n    return np.concatenate(parts, axis=0)\n\n\ndef first_crossing(md_seq, threshold, k):\n    n = len(md_seq)\n    if n < k:\n        return None\n    for i in range(n - k + 1):\n        if np.all(md_seq[i:i+k] > threshold):\n            return i\n    return None\n\n\ndef evaluate_crossing(test_traces, md_fn, safe_val_md, config_name):\n    results = []\n    for k in DETECTION_WINDOWS:\n        for pctl in THRESHOLD_PERCENTILES:\n            threshold = float(np.percentile(safe_val_md, pctl))\n            detected = 0\n            false_alarms = 0\n            leads = []\n            n_traces = 0\n\n            for trace in test_traces:\n                n_traces += 1\n                md_seq = md_fn(trace[\"hs\"])\n                cp = trace[\"commitment_point\"]\n                fcp = first_crossing(md_seq, threshold, k)\n                if fcp is not None:\n                    detected += 1\n                    leads.append(cp - fcp)\n                    if fcp >= cp:\n                        false_alarms += 0\n                    # Check false alarm: detection in safe region\n                safe_md = md_fn(trace[\"hs\"][:cp]) if cp > 0 else np.array([])\n                if len(safe_md) >= k:\n                    fa_cross = first_crossing(safe_md, threshold, k)\n                    if fa_cross is not None:\n                        false_alarms += 1\n\n            tp_rate = detected / n_traces if n_traces > 0 else 0.0\n            fa_rate = false_alarms / n_traces if n_traces > 0 else 0.0\n            results.append({\n                \"config\": config_name,\n                \"detection_window\": k,\n                \"threshold_percentile\": pctl,\n                \"threshold_value\": threshold,\n                \"crossing_rate\": tp_rate,\n                \"false_alarm_rate\": fa_rate,\n                \"lead_time_mean\": float(np.mean(leads)) if leads else None,\n                \"lead_time_median\": float(np.median(leads)) if leads else None,\n                \"n_traces\": n_traces,\n                \"n_detected\": detected,\n                \"n_false_alarms\": false_alarms,\n            })\n    return results\n\n\ndef run_model(model_name, cfg):\n    t0 = time.time()\n    print(\"=\" * 70)\n    print(f\"MAHALANOBIS DISTANCE: {model_name} Layer {cfg['layer_name']}\")\n    print(\"=\" * 70)\n\n    cfg[\"out_dir\"].mkdir(parents=True, exist_ok=True)\n\n    print(\"Loading traces...\")\n    traces = load_all_traces(cfg[\"hs_dir\"], cfg[\"layer_idx\"])\n    print(f\"Loaded {len(traces)} traces ({time.time()-t0:.1f}s)\")\n\n    train, val, test = split_data(traces)\n    print(f\"Split: train={len(train)}, val={len(val)}, test={len(test)}\")\n\n    print(\"\\nCollecting pre/post commitment hidden states...\")\n    X_safe_train = collect_pre_commitment_hs(train)\n    X_safe_val = collect_pre_commitment_hs(val)\n    X_post_train = collect_post_commitment_hs(train)\n    print(f\"Safe train steps: {X_safe_train.shape[0]}, Safe val steps: {X_safe_val.shape[0]}\")\n    print(f\"Post train steps: {X_post_train.shape[0]}\")\n\n    md_stats = {}\n    all_results = []\n\n    for pca_dim in PCA_DIMS:\n        config_name = f\"pca_{pca_dim}\"\n        print(f\"\\n--- PCA {pca_dim} + LedoitWolf ---\")\n\n        pca = PCA(n_components=pca_dim, random_state=SEED)\n        pca.fit(X_safe_train)\n        X_tr = pca.transform(X_safe_train)\n        X_val_tr = pca.transform(X_safe_val)\n        X_post_tr = pca.transform(X_post_train)\n\n        lw = LedoitWolf()\n        lw.fit(X_tr)\n        _mean = lw.location_\n        _prec = lw.precision_\n\n        def _md(X, _m=_mean, _p=_prec, _pca=pca):\n            Xt = _pca.transform(X)\n            diff = Xt - _m\n            return np.sqrt(np.sum(diff @ _p * diff, axis=1))\n\n        safe_val_md = _md(X_safe_val)\n        post_md = _md(X_post_train)\n\n        md_stats[config_name] = {\n            \"safe_md_mean\": float(safe_val_md.mean()),\n            \"safe_md_std\": float(safe_val_md.std()),\n            \"post_md_mean\": float(post_md.mean()),\n            \"post_md_std\": float(post_md.std()),\n            \"separation\": float(post_md.mean() - safe_val_md.mean()),\n        }\n        print(f\"  Safe MD: mean={safe_val_md.mean():.4f}, std={safe_val_md.std():.4f}\")\n        print(f\"  Post MD: mean={post_md.mean():.4f}, std={post_md.std():.4f}\")\n        print(f\"  Separation: {post_md.mean() - safe_val_md.mean():.4f}\")\n\n        configs = evaluate_crossing(test, _md, safe_val_md, config_name)\n        all_results.extend(configs)\n\n    # Summary\n    print(\"\\n\" + \"=\" * 90)\n    print(\"TOP-10 CONFIGS BY CROSSING RATE\")\n    print(\"=\" * 90)\n    sorted_configs = sorted(all_results, key=lambda c: (-c[\"crossing_rate\"], -(c[\"lead_time_mean\"] or -999)))\n    print(f\"{'Config':<16} {'K':<4} {'Pctl':<6} {'CrossRate':<12} {'FA_Rate':<10} {'LeadMean':<12} {'LeadMed':<10}\")\n    print(\"-\" * 80)\n    for c in sorted_configs[:10]:\n        lead_m = f\"{c['lead_time_mean']:.1f}\" if c['lead_time_mean'] is not None else \"N/A\"\n        lead_med = f\"{c['lead_time_median']:.1f}\" if c['lead_time_median'] is not None else \"N/A\"\n        print(f\"{c['config']:<16} {c['detection_window']:<4} p{c['threshold_percentile']:<5} \"\n              f\"{c['crossing_rate']:<12.3f} {c['false_alarm_rate']:<10.3f} {lead_m:<12} {lead_med:<10}\")\n\n    # Best configs for K=5\n    k5_configs = [c for c in all_results if c[\"detection_window\"] == 5]\n    best_k5 = max(k5_configs, key=lambda c: c[\"crossing_rate\"]) if k5_configs else None\n    k3_configs = [c for c in all_results if c[\"detection_window\"] == 3]\n    best_k3 = max(k3_configs, key=lambda c: c[\"crossing_rate\"]) if k3_configs else None\n\n    # Best PCA dim by separation\n    best_pca = max(md_stats.items(), key=lambda x: x[1][\"separation\"])\n\n    result = {\n        \"method\": \"trajguard_mahalanobis\",\n        \"model\": model_name,\n        \"layer\": cfg[\"layer_name\"],\n        \"layer_idx\": cfg[\"layer_idx\"],\n        \"hidden_dim\": cfg[\"hidden_dim\"],\n        \"n_traces\": len(traces),\n        \"split\": {\"train\": len(train), \"val\": len(val), \"test\": len(test)},\n        \"n_safe_train_steps\": int(X_safe_train.shape[0]),\n        \"n_safe_val_steps\": int(X_safe_val.shape[0]),\n        \"md_distribution_stats\": md_stats,\n        \"best_pca_config\": best_pca[0],\n        \"best_k3\": best_k3,\n        \"best_k5\": best_k5,\n        \"configs\": all_results,\n    }\n\n    output_path = cfg[\"out_dir\"] / \"results.json\"\n    with open(output_path, \"w\") as f:\n        json.dump(result, f, indent=2)\n    print(f\"\\nResults saved to {output_path}\")\n    print(f\"Time: {time.time()-t0:.1f}s\")\n\n    return result\n\n\ndef main():\n    t0 = time.time()\n    all_model_results = {}\n\n    for model_name, cfg in MODELS.items():\n        res = run_model(model_name, cfg)\n        all_model_results[model_name] = res\n\n    # 4-model comparison table\n    print(\"\\n\" + \"=\" * 100)\n    print(\"4-MODEL MAHALANOBIS COMPARISON (best PCA dim, K=5)\")\n    print(\"=\" * 100)\n\n    comparison = [\n        {\"model\": \"R1-8B\", \"layer\": \"L28\", \"safe_md\": 6.66, \"post_md\": 6.73,\n         \"separation\": 0.07, \"note\": \"previous result\"},\n        {\"model\": \"OT-7B\", \"layer\": \"L16\", \"safe_md\": 7.68, \"post_md\": 7.71,\n         \"separation\": 0.03, \"note\": \"previous result\"},\n    ]\n\n    for model_name, res in all_model_results.items():\n        best_pca = res[\"best_pca_config\"]\n        stats = res[\"md_distribution_stats\"][best_pca]\n        best_k5 = res[\"best_k5\"]\n        comparison.append({\n            \"model\": model_name,\n            \"layer\": f\"L{res['layer']}\",\n            \"safe_md\": stats[\"safe_md_mean\"],\n            \"post_md\": stats[\"post_md_mean\"],\n            \"separation\": stats[\"separation\"],\n            \"best_pca\": best_pca,\n            \"crossing_rate_k5\": best_k5[\"crossing_rate\"] if best_k5 else None,\n            \"fa_rate_k5\": best_k5[\"false_alarm_rate\"] if best_k5 else None,\n        })\n\n    print(f\"{'Model':<12} {'Layer':<8} {'safe_MD':<10} {'post_MD':<10} {'separation':<12} {'FA>=TP?':<10}\")\n    print(\"-\" * 70)\n    for c in comparison:\n        fa_ge_tp = \"\"\n        if \"fa_rate_k5\" in c and c.get(\"crossing_rate_k5\") is not None:\n            fa_ge_tp = \"YES\" if c[\"fa_rate_k5\"] >= c[\"crossing_rate_k5\"] else \"NO\"\n        elif c.get(\"note\") == \"previous result\":\n            fa_ge_tp = \"YES\"\n        print(f\"{c['model']:<12} {c['layer']:<8} {c['safe_md']:<10.2f} {c['post_md']:<10.2f} \"\n              f\"{c['separation']:<12.4f} {fa_ge_tp:<10}\")\n\n    print(f\"\\nTotal time: {time.time()-t0:.1f}s\")\n\n    # Conclusion\n    all_sep = [c[\"separation\"] for c in comparison]\n    if all(s < 0.5 for s in all_sep):\n        print(\"\\nCONCLUSION: 4/4 models show Mahalanobis separation ≈ 0. Method has no discriminative power.\")\n    else:\n        print(\"\\nCONCLUSION: Some models show non-trivial separation. Check details.\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"Script written.\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-17T14:59:00.690096+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script written.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_mahalanobis_r1_32b_qwq_20260517T145609",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-17T14:59:00.690302+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-rtx6000",
  "command": "source /root/miniconda3/bin/activate && cd /root/autodl-tmp/contrastive_trace_safety && python src/experiments/exp_r3_mahalanobis_32b.py",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_mahalanobis_r1_32b_qwq_20260517T145609",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-rtx6000",
    "command": "source /root/miniconda3/bin/activate && cd /root/autodl-tmp/contrastive_trace_safety && python src/experiments/exp_r3_mahalanobis_32b.py",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-17T14:59:00.690511+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"======================================================================\\nMAHALANOBIS DISTANCE: R1-32B Layer 63\\n======================================================================\\nLoading traces...\\nLoaded 100 traces (1.1s)\\nSplit: train=60, val=20, test=20\\n\\nCollecting pre/post commitment hidden states...\\nSafe train steps: 1440, Safe val steps: 601\\nPost train steps: 757\\n\\n--- PCA 16 + LedoitWolf ---\\n  Safe MD: mean=3.3412, std=0.9621\\n  Post MD: mean=3.4894, std=0.6740\\n  Separation: 0.1482\\n\\n--- PCA 32 + LedoitWolf ---\\n  Safe MD: mean=4.6409, std=1.0425\\n  Post MD: mean=4.7765, std=0.8650\\n  Separation: 0.1356\\n\\n--- PCA 64 + LedoitWolf ---\\n  Safe MD: mean=6.7289, std=1.1473\\n  Post MD: mean=6.8795, std=1.0985\\n  Separation: 0.1505\\n\\n--- PCA 128 + LedoitWolf ---\\n  Safe MD: mean=9.6837, std=1.5617\\n  Post MD: mean=9.5997, std=1.5969\\n  Separation: -0.0840\\n\\n==========================================================================================\\nTOP-10 CONFIGS BY CROSSING RATE\\n==========================================================================================\\nConfig           K    Pctl   CrossRate    FA_Rate    LeadMean     LeadMed   \\n--------------------------------------------------------------------------------\\npca_32           3    p50    1.000        0.700      6.6          4.5       \\npca_64           3    p50    0.850        0.550      9.5          4.0       \\npca_16           3    p50    0.800        0.650      14.0         13.5      \\npca_128          3    p50    0.750        0.450      8.9          11.0      \\npca_16           5    p50    0.650        0.450      13.5         11.0      \\npca_64           5    p50    0.650        0.350      9.5          11.0      \\npca_16           3    p75    0.600        0.450      10.8         9.5       \\npca_64           3    p75    0.600        0.350      5.4          4.0       \\npca_32        
…[truncated 3390 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_mahalanobis_r1_32b_qwq_20260517T145609",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-17T14:59:00.690764+00:00_

实验完成。结果汇总:

## 4-Model Mahalanobis Comparison

| Model | Layer | safe_MD | post_MD | separation | Best PCA |
|-------|-------|---------|---------|------------|----------|
| R1-8B | L28 | 6.66 | 6.73 | 0.07 | (prev) |
| OT-7B | L16 | 7.68 | 7.71 | 0.03 | (prev) |
| R1-32B | L63 | 6.73 | 6.88 | 0.15 | pca_64 |
| QwQ-32B | L60 | 3.22 | 3.42 | 0.20 | pca_16 |

所有 4 个模型 separation 均 < 0.21，Mahalanobis distance 无判别力。即使 crossing rate 最高的配置（R1-32B: 0.65, QwQ: 0.58），对应的 false alarm rate 也极高（0.45, 0.42），几乎等同于随机检测。

**结论: 4/4 模型 Mahalanobis 均失败。** 结果已保存至:
- `/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r3_mahalanobis_r1_32b/results.json`
- `/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r3_mahalanobis_qwq/results.json`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_mahalanobis_r1_32b_qwq_20260517T145609"
}
```

</details>

---
