# fix mlp correlation extend

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 0
- **Tool calls:** 22
- **Original source:** `logs/chats/worker_fix_mlp-correlation-extend_20260514T052804.jsonl`
- **Structured JSON:** [`89c7094d14121121e2d0.json`](../../sessions/89/89c7094d14121121e2d0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

45 recorded events

### Tool call

_source line 1 · 2026-05-14T05:38:16.867731+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_mlp-correlation-extend_20260514T052804",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T05:38:16.868146+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_mlp-correlation-extend_20260514T052804",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T05:38:16.868367+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "stat -c '%Y %n' /root/recovery_aware_struct_prune/src/cka_overlap.py /root/recovery_aware_struct_prune/src/correlation_analysis.py /root/recovery_aware_struct_prune/src/prune.py /root/recovery_aware_struct_prune/src/importance_score.py 2>&1",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_mlp-correlation-extend_20260514T052804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "stat -c '%Y %n' /root/recovery_aware_struct_prune/src/cka_overlap.py /root/recovery_aware_struct_prune/src/correlation_analysis.py /root/recovery_aware_struct_prune/src/prune.py /root/recovery_aware_struct_prune/src/importance_score.py 2>&1",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T05:38:16.868538+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_mlp-correlation-extend_20260514T052804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T05:38:16.868668+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "stat -c '%Y %n' /root/recovery_aware_struct_prune/src/cka_overlap.py /root/recovery_aware_struct_prune/src/correlation_analysis.py /root/recovery_aware_struct_prune/src/prune.py /root/recovery_aware_struct_prune/src/importance_score.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_mlp-correlation-extend_20260514T052804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "stat -c '%Y %n' /root/recovery_aware_struct_prune/src/cka_overlap.py /root/recovery_aware_struct_prune/src/correlation_analysis.py /root/recovery_aware_struct_prune/src/prune.py /root/recovery_aware_struct_prune/src/importance_score.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T05:38:16.868799+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"1778735926 /root/recovery_aware_struct_prune/src/cka_overlap.py\\n1778731373 /root/recovery_aware_struct_prune/src/correlation_analysis.py\\n1778728609 /root/recovery_aware_struct_prune/src/prune.py\\n1778736119 /root/recovery_aware_struct_prune/src/importance_score.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.77}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_mlp-correlation-extend_20260514T052804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T05:38:16.868939+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "sleep 30 && echo \"done\"",
  "description": "Wait 30 seconds before second mtime check"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_mlp-correlation-extend_20260514T052804",
  "tool": "Bash",
  "tool_args": {
    "command": "sleep 30 && echo \"done\"",
    "description": "Wait 30 seconds before second mtime check"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T05:38:16.869057+00:00_

&lt;tool_use_error>Blocked: sleep 30 followed by: echo "done". To wait for a condition, use Monitor with an until-loop (e.g. `until &lt;check>; do sleep 2; done`). To wait for a command you started, use run_in_background: true. Do not chain shorter sleeps to work around this block.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_mlp-correlation-extend_20260514T052804",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T05:38:16.869174+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "until [ $(($(date +%s) - 1747220000)) -gt 30 ]; do sleep 2; done && echo \"done\"",
  "description": "Wait ~30 seconds for file stability check",
  "timeout": "60000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_mlp-correlation-extend_20260514T052804",
  "tool": "Bash",
  "tool_args": {
    "command": "until [ $(($(date +%s) - 1747220000)) -gt 30 ]; do sleep 2; done && echo \"done\"",
    "description": "Wait ~30 seconds for file stability check",
    "timeout": "60000"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T05:38:16.869379+00:00_

done

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_mlp-correlation-extend_20260514T052804",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T05:38:16.869502+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "stat -c '%Y %n' /root/recovery_aware_struct_prune/src/cka_overlap.py /root/recovery_aware_struct_prune/src/correlation_analysis.py /root/recovery_aware_struct_prune/src/prune.py /root/recovery_aware_struct_prune/src/importance_score.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_mlp-correlation-extend_20260514T052804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "stat -c '%Y %n' /root/recovery_aware_struct_prune/src/cka_overlap.py /root/recovery_aware_struct_prune/src/correlation_analysis.py /root/recovery_aware_struct_prune/src/prune.py /root/recovery_aware_struct_prune/src/importance_score.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T05:38:16.869637+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"1778735926 /root/recovery_aware_struct_prune/src/cka_overlap.py\\n1778731373 /root/recovery_aware_struct_prune/src/correlation_analysis.py\\n1778728609 /root/recovery_aware_struct_prune/src/prune.py\\n1778736119 /root/recovery_aware_struct_prune/src/importance_score.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.71}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_mlp-correlation-extend_20260514T052804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T05:38:16.869798+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "cat /root/recovery_aware_struct_prune/src/cka_overlap.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_mlp-correlation-extend_20260514T052804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "cat /root/recovery_aware_struct_prune/src/cka_overlap.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T05:38:16.870085+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nCKA Overlap Computation for RASP.\\n\\nComputes intra-layer functional overlap F(g) for each GQA group and MLP channel group\\nusing linear CKA (Centered Kernel Alignment via HSIC).\\n\\nGQA group: each group contains heads_per_kv Q heads + 1 KV head.\\nActivations are the concatenation of Q head outputs within the group.\\n\\nInput:  model + calibration data (GSM8K train subset)\\nOutput: per-structure F(g) scores saved as dict in .pt file\\n        Keys: 'attn_overlap' (dict[layer_idx -> tensor[n_kv_heads]]),\\n              'mlp_overlap'  (dict[layer_idx -> tensor[n_groups]])\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport logging\\nimport math\\nimport os\\nimport random\\n\\nimport numpy as np\\nimport torch\\nfrom datasets import load_dataset\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n)\\nlogger = logging.getLogger(__name__)\\n\\n\\ndef set_seed(seed: int):\\n    random.seed(seed)\\n    np.random.seed(seed)\\n    torch.manual_seed(seed)\\n    torch.cuda.manual_seed_all(seed)\\n\\n\\ndef linear_cka(X: torch.Tensor, Y: torch.Tensor) -> float:\\n    \\\"\\\"\\\"Linear CKA between two activation matrices.\\n    X: [n, p], Y: [n, q]. Returns scalar similarity in [0, 1].\\n    \\\"\\\"\\\"\\n    X = X - X.mean(0)\\n    Y = Y - Y.mean(0)\\n    hsic_xy = torch.norm(X.T @ Y, \\\"fro\\\") ** 2\\n    hsic_xx = torch.norm(X.T @ X, \\\"fro\\\") ** 2\\n    hsic_yy = torch.norm(Y.T @ Y, \\\"fro\\\") ** 2\\n    return (hsic_xy / (torch.sqrt(hsic_xx) * torch.sqrt(hsic_yy) + 1e-8)).item()\\n\\n\\ndef load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):\\n    \\\"\\\"\\\"Load GSM8K train questions as calibration prompts.\\\"\\\"\\\"\\n    ds = load_dataset(\\\"openai/gsm8k\\\", \\\"main\\\", split=\\\"train\\\")\\n    ds = ds.shuffle(seed=seed
…[truncated 7021 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_mlp-correlation-extend_20260514T052804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T05:38:16.870315+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "wc -l /root/recovery_aware_struct_prune/src/cka_overlap.py /root/recovery_aware_struct_prune/src/correlation_analysis.py /root/recovery_aware_struct_prune/src/prune.py /root/recovery_aware_struct_prune/src/importance_score.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_mlp-correlation-extend_20260514T052804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "wc -l /root/recovery_aware_struct_prune/src/cka_overlap.py /root/recovery_aware_struct_prune/src/correlation_analysis.py /root/recovery_aware_struct_prune/src/prune.py /root/recovery_aware_struct_prune/src/importance_score.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T05:38:16.870513+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  263 /root/recovery_aware_struct_prune/src/cka_overlap.py\\n  335 /root/recovery_aware_struct_prune/src/correlation_analysis.py\\n  411 /root/recovery_aware_struct_prune/src/prune.py\\n  219 /root/recovery_aware_struct_prune/src/importance_score.py\\n 1228 total\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.71}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_mlp-correlation-extend_20260514T052804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T05:38:16.870646+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "head -160 /root/recovery_aware_struct_prune/src/cka_overlap.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_mlp-correlation-extend_20260514T052804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "head -160 /root/recovery_aware_struct_prune/src/cka_overlap.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T05:38:16.870845+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nCKA Overlap Computation for RASP.\\n\\nComputes intra-layer functional overlap F(g) for each GQA group and MLP channel group\\nusing linear CKA (Centered Kernel Alignment via HSIC).\\n\\nGQA group: each group contains heads_per_kv Q heads + 1 KV head.\\nActivations are the concatenation of Q head outputs within the group.\\n\\nInput:  model + calibration data (GSM8K train subset)\\nOutput: per-structure F(g) scores saved as dict in .pt file\\n        Keys: 'attn_overlap' (dict[layer_idx -> tensor[n_kv_heads]]),\\n              'mlp_overlap'  (dict[layer_idx -> tensor[n_groups]])\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport logging\\nimport math\\nimport os\\nimport random\\n\\nimport numpy as np\\nimport torch\\nfrom datasets import load_dataset\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n)\\nlogger = logging.getLogger(__name__)\\n\\n\\ndef set_seed(seed: int):\\n    random.seed(seed)\\n    np.random.seed(seed)\\n    torch.manual_seed(seed)\\n    torch.cuda.manual_seed_all(seed)\\n\\n\\ndef linear_cka(X: torch.Tensor, Y: torch.Tensor) -> float:\\n    \\\"\\\"\\\"Linear CKA between two activation matrices.\\n    X: [n, p], Y: [n, q]. Returns scalar similarity in [0, 1].\\n    \\\"\\\"\\\"\\n    X = X - X.mean(0)\\n    Y = Y - Y.mean(0)\\n    hsic_xy = torch.norm(X.T @ Y, \\\"fro\\\") ** 2\\n    hsic_xx = torch.norm(X.T @ X, \\\"fro\\\") ** 2\\n    hsic_yy = torch.norm(Y.T @ Y, \\\"fro\\\") ** 2\\n    return (hsic_xy / (torch.sqrt(hsic_xx) * torch.sqrt(hsic_yy) + 1e-8)).item()\\n\\n\\ndef load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):\\n    \\\"\\\"\\\"Load GSM8K train questions as calibration prompts.\\\"\\\"\\\"\\n    ds = load_dataset(\\\"openai/gsm8k\\\", \\\"main\\\", split=\\\"train\\\")\\n    ds = ds.shuffle(seed=seed
…[truncated 4231 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_mlp-correlation-extend_20260514T052804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T05:38:16.871000+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "tail -110 /root/recovery_aware_struct_prune/src/cka_overlap.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_mlp-correlation-extend_20260514T052804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "tail -110 /root/recovery_aware_struct_prune/src/cka_overlap.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T05:38:16.871200+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    for layer_idx in range(n_layers):\\n        tensors = gate_outputs[layer_idx]\\n        per_group_list = []\\n        for t in tensors:\\n            t = t.squeeze(0)  # [seq, intermediate_size]\\n            t = t.mean(dim=0)  # [intermediate_size]\\n            usable = n_groups * group_size\\n            t = t[:usable].view(n_groups, group_size)\\n            per_group_list.append(t)\\n        layer_activations[layer_idx] = torch.stack(per_group_list, dim=0)\\n        gate_outputs[layer_idx] = None\\n\\n    return layer_activations\\n\\n\\ndef compute_overlap(activations_dict: dict, structure_name: str) -> tuple:\\n    \\\"\\\"\\\"Compute F(g) = mean CKA similarity and pairwise CKA matrix per layer.\\n\\n    activations_dict: dict[layer_idx] -> tensor[n_samples, n_structures, dim]\\n    Returns: (overlap_scores, cka_matrices)\\n        overlap_scores: dict[layer_idx] -> tensor[n_structures] of overlap F(g) in [0, 1]\\n        cka_matrices: dict[layer_idx] -> tensor[n_structures, n_structures] pairwise CKA\\n    \\\"\\\"\\\"\\n    overlap_scores = {}\\n    cka_matrices = {}\\n    for layer_idx, acts in activations_dict.items():\\n        n_samples, n_structs, dim = acts.shape\\n        matrix = torch.zeros(n_structs, n_structs)\\n        for i in range(n_structs):\\n            matrix[i, i] = 1.0\\n            for j in range(i + 1, n_structs):\\n                val = linear_cka(acts[:, i, :].float(), acts[:, j, :].float())\\n                matrix[i, j] = val\\n                matrix[j, i] = val\\n        scores = (matrix.sum(dim=1) - 1.0) / max(n_structs - 1, 1)\\n        overlap_scores[layer_idx] = scores\\n        cka_matrices[layer_idx] = matrix\\n        logger.info(\\n            f\\\"  Layer {layer_idx} {structure_name}: F(g) range [{scores.min():.4f}, {scores.max():.4f}], \\\"\\n            f\\\"mean={scores.mean():.4f}\\\"\\n        )\\n    return overlap_scores, cka_matrices\\n\\n\\ndef main():\
…[truncated 3558 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_mlp-correlation-extend_20260514T052804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T05:38:16.871414+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "cat /root/recovery_aware_struct_prune/src/correlation_analysis.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_mlp-correlation-extend_20260514T052804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "cat /root/recovery_aware_struct_prune/src/correlation_analysis.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T05:38:16.871696+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nCorrelation Analysis: rho(CKA overlap, RLVR recoverability).\\n\\nTests the MVP hypothesis: pruned heads with higher CKA overlap F(h) are more\\neffectively compensated by RLVR through their most similar retained head.\\n\\nMetric: for each pruned head h_p, find the most CKA-similar retained head h_r,\\nthen measure h_r's activation shift between pruned model and RLVR-recovered model.\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport random\\n\\nimport numpy as np\\nimport scipy.stats as stats\\nimport torch\\nimport torch.nn.functional as F\\nfrom datasets import load_dataset\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n)\\nlogger = logging.getLogger(__name__)\\n\\n\\ndef set_seed(seed: int):\\n    random.seed(seed)\\n    np.random.seed(seed)\\n    torch.manual_seed(seed)\\n    torch.cuda.manual_seed_all(seed)\\n\\n\\ndef load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):\\n    ds = load_dataset(\\\"openai/gsm8k\\\", \\\"main\\\", split=\\\"train\\\")\\n    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))\\n    encodings = []\\n    for example in ds:\\n        prompt = f\\\"Question: {example['question']}\\\\nAnswer: Let me think step by step.\\\\n\\\"\\n        ids = tokenizer(prompt, return_tensors=\\\"pt\\\", truncation=True, max_length=max_length)\\n        encodings.append(ids)\\n    return encodings\\n\\n\\ndef load_pruned_model(base_model_path, saved_model_path, pruning_meta, torch_dtype, device):\\n    \\\"\\\"\\\"Load a structurally pruned model by reconstructing from base model + saved weights.\\\"\\\"\\\"\\n    logging.getLogger(\\\"prune\\\").setLevel(logging.WARNING)\\n    from prune import prune_attention_heads, prune_mlp_channels\\n\\n    model = AutoModelFo
…[truncated 7131 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_mlp-correlation-extend_20260514T052804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T05:38:16.871893+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "head -230 /root/recovery_aware_struct_prune/src/correlation_analysis.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_mlp-correlation-extend_20260514T052804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "head -230 /root/recovery_aware_struct_prune/src/correlation_analysis.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T05:38:16.872159+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nCorrelation Analysis: rho(CKA overlap, RLVR recoverability).\\n\\nTests the MVP hypothesis: pruned heads with higher CKA overlap F(h) are more\\neffectively compensated by RLVR through their most similar retained head.\\n\\nMetric: for each pruned head h_p, find the most CKA-similar retained head h_r,\\nthen measure h_r's activation shift between pruned model and RLVR-recovered model.\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport random\\n\\nimport numpy as np\\nimport scipy.stats as stats\\nimport torch\\nimport torch.nn.functional as F\\nfrom datasets import load_dataset\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n)\\nlogger = logging.getLogger(__name__)\\n\\n\\ndef set_seed(seed: int):\\n    random.seed(seed)\\n    np.random.seed(seed)\\n    torch.manual_seed(seed)\\n    torch.cuda.manual_seed_all(seed)\\n\\n\\ndef load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):\\n    ds = load_dataset(\\\"openai/gsm8k\\\", \\\"main\\\", split=\\\"train\\\")\\n    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))\\n    encodings = []\\n    for example in ds:\\n        prompt = f\\\"Question: {example['question']}\\\\nAnswer: Let me think step by step.\\\\n\\\"\\n        ids = tokenizer(prompt, return_tensors=\\\"pt\\\", truncation=True, max_length=max_length)\\n        encodings.append(ids)\\n    return encodings\\n\\n\\ndef load_pruned_model(base_model_path, saved_model_path, pruning_meta, torch_dtype, device):\\n    \\\"\\\"\\\"Load a structurally pruned model by reconstructing from base model + saved weights.\\\"\\\"\\\"\\n    logging.getLogger(\\\"prune\\\").setLevel(logging.WARNING)\\n    from prune import prune_attention_heads, prune_mlp_channels\\n\\n    model = AutoModelFo
…[truncated 7029 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_mlp-correlation-extend_20260514T052804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T05:38:16.872343+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "cat /root/recovery_aware_struct_prune/src/prune.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_mlp-correlation-extend_20260514T052804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "cat /root/recovery_aware_struct_prune/src/prune.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T05:38:16.872591+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nStructured Pruning for Qwen2.5 architecture (GQA-group granularity).\\n\\nRemoves GQA groups (7 Q heads + 1 KV head each) and MLP channel groups\\nbased on RASP or standard importance scores.\\n\\nInput:  pretrained model + pruning scores\\nOutput: pruned model saved to disk\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport copy\\nimport logging\\nimport os\\nimport random\\n\\nimport numpy as np\\nimport torch\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n)\\nlogger = logging.getLogger(__name__)\\n\\n\\ndef set_seed(seed: int):\\n    random.seed(seed)\\n    np.random.seed(seed)\\n    torch.manual_seed(seed)\\n    torch.cuda.manual_seed_all(seed)\\n\\n\\ndef prune_attention_heads(model, attn_keep_masks: dict):\\n    \\\"\\\"\\\"Prune GQA groups from the model by slicing weight matrices in-place.\\n\\n    attn_keep_masks: dict[layer_idx -> list of GQA group indices to KEEP]\\n    Each GQA group = heads_per_kv Q heads + 1 KV head.\\n    \\\"\\\"\\\"\\n    config = model.config\\n    n_heads = config.num_attention_heads\\n    n_kv_heads = config.num_key_value_heads\\n    head_dim = config.hidden_size // n_heads\\n    heads_per_kv = n_heads // n_kv_heads\\n\\n    total_pruned_groups = 0\\n\\n    for layer_idx, keep_groups in attn_keep_masks.items():\\n        layer = model.model.layers[layer_idx]\\n        attn = layer.self_attn\\n        n_keep_groups = len(keep_groups)\\n        pruned_groups = n_kv_heads - n_keep_groups\\n\\n        # Expand GQA group indices to Q head weight indices\\n        q_indices = []\\n        for g in keep_groups:\\n            for qh in range(heads_per_kv):\\n                h = g * heads_per_kv + qh\\n                start = h * head_dim\\n                q_indices.extend(range(start, start + head_dim))\\n        q_indices = torch.tensor(q_indi
…[truncated 6907 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_mlp-correlation-extend_20260514T052804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T05:38:16.872770+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "head -115 /root/recovery_aware_struct_prune/src/correlation_analysis.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_mlp-correlation-extend_20260514T052804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "head -115 /root/recovery_aware_struct_prune/src/correlation_analysis.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T05:38:16.872953+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nCorrelation Analysis: rho(CKA overlap, RLVR recoverability).\\n\\nTests the MVP hypothesis: pruned heads with higher CKA overlap F(h) are more\\neffectively compensated by RLVR through their most similar retained head.\\n\\nMetric: for each pruned head h_p, find the most CKA-similar retained head h_r,\\nthen measure h_r's activation shift between pruned model and RLVR-recovered model.\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport random\\n\\nimport numpy as np\\nimport scipy.stats as stats\\nimport torch\\nimport torch.nn.functional as F\\nfrom datasets import load_dataset\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n)\\nlogger = logging.getLogger(__name__)\\n\\n\\ndef set_seed(seed: int):\\n    random.seed(seed)\\n    np.random.seed(seed)\\n    torch.manual_seed(seed)\\n    torch.cuda.manual_seed_all(seed)\\n\\n\\ndef load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):\\n    ds = load_dataset(\\\"openai/gsm8k\\\", \\\"main\\\", split=\\\"train\\\")\\n    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))\\n    encodings = []\\n    for example in ds:\\n        prompt = f\\\"Question: {example['question']}\\\\nAnswer: Let me think step by step.\\\\n\\\"\\n        ids = tokenizer(prompt, return_tensors=\\\"pt\\\", truncation=True, max_length=max_length)\\n        encodings.append(ids)\\n    return encodings\\n\\n\\ndef load_pruned_model(base_model_path, saved_model_path, pruning_meta, torch_dtype, device):\\n    \\\"\\\"\\\"Load a structurally pruned model by reconstructing from base model + saved weights.\\\"\\\"\\\"\\n    logging.getLogger(\\\"prune\\\").setLevel(logging.WARNING)\\n    from prune import prune_attention_heads, prune_mlp_channels\\n\\n    model = AutoModelFo
…[truncated 2468 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_mlp-correlation-extend_20260514T052804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T05:38:16.873111+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "tail -n +112 /root/recovery_aware_struct_prune/src/correlation_analysis.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_mlp-correlation-extend_20260514T052804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "tail -n +112 /root/recovery_aware_struct_prune/src/correlation_analysis.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T05:38:16.873392+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    for layer_idx in range(n_layers):\\n        n_retained = len(keep_masks[layer_idx])\\n        per_head = []\\n        for t in q_outputs[layer_idx]:\\n            t = t.squeeze(0)  # [seq, n_retained * head_dim]\\n            t = t.view(t.shape[0], n_retained, head_dim)  # [seq, n_retained, head_dim]\\n            t = t.mean(dim=0)  # [n_retained, head_dim]\\n            per_head.append(t)\\n        activations[layer_idx] = torch.stack(per_head, dim=0).float()\\n        q_outputs[layer_idx] = None\\n\\n    return activations\\n\\n\\ndef compute_recoverability(pruned_acts, recovered_acts, cka_data, keep_masks,\\n                           n_heads_original=28):\\n    \\\"\\\"\\\"Compute per-pruned-head recoverability as activation shift of best retained head.\\\"\\\"\\\"\\n    attn_overlap = cka_data[\\\"attn_overlap\\\"]\\n    attn_cka_matrix = cka_data[\\\"attn_cka_matrix\\\"]\\n    results = []\\n\\n    for layer_idx in range(len(keep_masks)):\\n        retained = keep_masks[layer_idx]\\n        pruned_heads = sorted(set(range(n_heads_original)) - set(retained))\\n        if not pruned_heads:\\n            continue\\n\\n        cka_matrix = attn_cka_matrix[layer_idx]\\n\\n        for h_p in pruned_heads:\\n            sims = torch.tensor([cka_matrix[h_p, h_r].item() for h_r in retained])\\n            best_idx = sims.argmax().item()\\n            h_r = retained[best_idx]\\n            h_r_local = retained.index(h_r)\\n\\n            act_p = pruned_acts[layer_idx][:, h_r_local, :]\\n            act_r = recovered_acts[layer_idx][:, h_r_local, :]\\n            cos_sim = F.cosine_similarity(act_p, act_r, dim=-1)\\n            activation_shift = 1.0 - cos_sim.mean().item()\\n\\n            results.append({\\n                \\\"layer\\\": layer_idx,\\n                \\\"pruned_head\\\": h_p,\\n                \\\"best_retained_head\\\": h_r,\\n                \\\"cka_overlap\\\": attn_overlap[layer_idx][h_p].i
…[truncated 7144 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_mlp-correlation-extend_20260514T052804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T05:38:16.873580+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "cat /root/recovery_aware_struct_prune/src/importance_score.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_mlp-correlation-extend_20260514T052804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "cat /root/recovery_aware_struct_prune/src/importance_score.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T05:38:16.873829+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nGradient-based Importance Scoring for structured pruning.\\n\\nComputes Taylor-expansion importance I(g) = ||w * grad||_2 for each\\nGQA group and MLP channel group on calibration data.\\n\\nGQA group importance = sum of Q head importances (q_proj + o_proj) + KV head importance (k_proj + v_proj).\\n\\nInput:  model + calibration data (GSM8K train subset)\\nOutput: per-structure I(g) scores saved as dict in .pt file\\n        Keys: 'attn_importance' (dict[layer_idx -> tensor[n_kv_heads]]),\\n              'mlp_importance'  (dict[layer_idx -> tensor[n_mlp_groups]])\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport logging\\nimport os\\nimport random\\n\\nimport numpy as np\\nimport torch\\nfrom datasets import load_dataset\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n)\\nlogger = logging.getLogger(__name__)\\n\\n\\ndef set_seed(seed: int):\\n    random.seed(seed)\\n    np.random.seed(seed)\\n    torch.manual_seed(seed)\\n    torch.cuda.manual_seed_all(seed)\\n\\n\\ndef load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):\\n    \\\"\\\"\\\"Load GSM8K train questions as calibration prompts with labels for loss computation.\\\"\\\"\\\"\\n    ds = load_dataset(\\\"openai/gsm8k\\\", \\\"main\\\", split=\\\"train\\\")\\n    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))\\n\\n    encodings = []\\n    for example in ds:\\n        text = f\\\"Question: {example['question']}\\\\nAnswer: {example['answer']}\\\"\\n        ids = tokenizer(text, return_tensors=\\\"pt\\\", truncation=True, max_length=max_length)\\n        encodings.append(ids)\\n    return encodings\\n\\n\\ndef compute_importance(model, calibration_data, device):\\n    \\\"\\\"\\\"Compute gradient-based importance for GQA groups and MLP groups.\\n\\n    GQA group im
…[truncated 6896 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_mlp-correlation-extend_20260514T052804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T05:38:16.874130+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "head -280 /root/recovery_aware_struct_prune/src/prune.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_mlp-correlation-extend_20260514T052804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "head -280 /root/recovery_aware_struct_prune/src/prune.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T05:38:16.874419+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nStructured Pruning for Qwen2.5 architecture (GQA-group granularity).\\n\\nRemoves GQA groups (7 Q heads + 1 KV head each) and MLP channel groups\\nbased on RASP or standard importance scores.\\n\\nInput:  pretrained model + pruning scores\\nOutput: pruned model saved to disk\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport copy\\nimport logging\\nimport os\\nimport random\\n\\nimport numpy as np\\nimport torch\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n)\\nlogger = logging.getLogger(__name__)\\n\\n\\ndef set_seed(seed: int):\\n    random.seed(seed)\\n    np.random.seed(seed)\\n    torch.manual_seed(seed)\\n    torch.cuda.manual_seed_all(seed)\\n\\n\\ndef prune_attention_heads(model, attn_keep_masks: dict):\\n    \\\"\\\"\\\"Prune GQA groups from the model by slicing weight matrices in-place.\\n\\n    attn_keep_masks: dict[layer_idx -> list of GQA group indices to KEEP]\\n    Each GQA group = heads_per_kv Q heads + 1 KV head.\\n    \\\"\\\"\\\"\\n    config = model.config\\n    n_heads = config.num_attention_heads\\n    n_kv_heads = config.num_key_value_heads\\n    head_dim = config.hidden_size // n_heads\\n    heads_per_kv = n_heads // n_kv_heads\\n\\n    total_pruned_groups = 0\\n\\n    for layer_idx, keep_groups in attn_keep_masks.items():\\n        layer = model.model.layers[layer_idx]\\n        attn = layer.self_attn\\n        n_keep_groups = len(keep_groups)\\n        pruned_groups = n_kv_heads - n_keep_groups\\n\\n        # Expand GQA group indices to Q head weight indices\\n        q_indices = []\\n        for g in keep_groups:\\n            for qh in range(heads_per_kv):\\n                h = g * heads_per_kv + qh\\n                start = h * head_dim\\n                q_indices.extend(range(start, start + head_dim))\\n        q_indices = torch.tensor(q_indi
…[truncated 6807 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_mlp-correlation-extend_20260514T052804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-14T05:38:16.874602+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "tail -n +275 /root/recovery_aware_struct_prune/src/prune.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_mlp-correlation-extend_20260514T052804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "tail -n +275 /root/recovery_aware_struct_prune/src/prune.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-14T05:38:16.874794+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    # Build keep masks\\n    attn_keep_masks = {}\\n    for layer_idx in range(n_layers):\\n        keep = [g for g in range(n_gqa_groups) if (layer_idx, g) not in attn_prune_set]\\n        attn_keep_masks[layer_idx] = keep\\n\\n    mlp_keep_masks = {}\\n    for layer_idx in range(n_layers):\\n        keep = [g for g in range(n_mlp_groups) if (layer_idx, g) not in mlp_prune_set]\\n        mlp_keep_masks[layer_idx] = keep\\n\\n    # Execute pruning\\n    logger.info(\\\"Pruning GQA groups...\\\")\\n    prune_attention_heads(model, attn_keep_masks)\\n\\n    logger.info(\\\"Pruning MLP channels...\\\")\\n    prune_mlp_channels(model, mlp_keep_masks, n_mlp_groups=n_mlp_groups)\\n\\n    pruned_params_actual = count_parameters(model)\\n    actual_sparsity = 1.0 - pruned_params_actual / original_params\\n    logger.info(\\n        f\\\"Pruned model parameters: {pruned_params_actual:,} \\\"\\n        f\\\"(actual sparsity: {actual_sparsity:.2%})\\\"\\n    )\\n\\n    # --- Update model config ---\\n    per_layer_q_heads = []\\n    per_layer_kv_heads = []\\n    for li in range(n_layers):\\n        layer_i = model.model.layers[li]\\n        per_layer_q_heads.append(layer_i.self_attn.num_heads)\\n        per_layer_kv_heads.append(layer_i.self_attn.num_key_value_heads)\\n\\n    unique_q = set(per_layer_q_heads)\\n    unique_kv = set(per_layer_kv_heads)\\n\\n    if len(unique_q) == 1 and len(unique_kv) == 1:\\n        model.config.num_attention_heads = per_layer_q_heads[0]\\n        model.config.num_key_value_heads = per_layer_kv_heads[0]\\n        logger.info(f\\\"Uniform pruning: config num_attention_heads={per_layer_q_heads[0]}, \\\"\\n                    f\\\"num_key_value_heads={per_layer_kv_heads[0]}\\\")\\n    else:\\n        model.config.num_attention_heads = min(per_layer_q_heads)\\n        model.config.num_key_value_heads = min(per_layer_kv_heads)\\n        model.config.per_layer_num_attention_heads = per_layer_q_h
…[truncated 3465 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_mlp-correlation-extend_20260514T052804",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-14T05:38:16.875187+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/correlation_analysis.py",
  "content": "\"\"\"\nCorrelation Analysis: rho(CKA overlap, RLVR recoverability).\n\nTests the hypothesis: pruned structures (GQA groups or MLP channel groups) with\nhigher CKA overlap F(g) are more effectively compensated by RLVR through their\nmost similar retained structure.\n\nMetric: for each pruned structure g_p, find the most CKA-similar retained\nstructure g_r, then measure g_r's activation shift between pruned and\nRLVR-recovered models.\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nimport random\n\nimport numpy as np\nimport scipy.stats as stats\nimport torch\nimport torch.nn.functional as F\nfrom datasets import load_dataset\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n)\nlogger = logging.getLogger(__name__)\n\n\ndef set_seed(seed: int):\n    random.seed(seed)\n    np.random.seed(seed)\n    torch.manual_seed(seed)\n    torch.cuda.manual_seed_all(seed)\n\n\ndef load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):\n    ds = load_dataset(\"openai/gsm8k\", \"main\", split=\"train\")\n    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))\n    encodings = []\n    for example in ds:\n        prompt = f\"Question: {example['question']}\\nAnswer: Let me think step by step.\\n\"\n        ids = tokenizer(prompt, return_tensors=\"pt\", truncation=True, max_length=max_length)\n        encodings.append(ids)\n    return encodings\n\n\ndef load_pruned_model(base_model_path, saved_model_path, pruning_meta, torch_dtype, device):\n    logging.getLogger(\"prune\").setLevel(logging.WARNING)\n    from prune import prune_attention_heads, prune_mlp_channels\n\n    model = AutoModelForCausalLM.from_pretrained(\n        base_model_path, torch_dtype=torch_dtype, device_map=\"cpu\", trust_remote_code=True\n    )\n    prune_attention_heads(model, pruning_meta[\"attn_keep_masks\"])\n    prune_mlp_channels(model, pruning_meta[\"mlp_keep_masks\"])\n\n    safetensor_files = sorted(\n        [f for f in os.listdir(saved_model_path) if f.endswith(\".safetensors\")]\n    )\n    if safetensor_files:\n        from safetensors.torch import load_file\n        state_dict = {}\n        for f in safetensor_files:\n            state_dict.update(load_file(os.path.join(saved_model_path, f)))\n    else:\n        state_dict = torch.load(\n            os.path.join(saved_model_path, \"pytorch_model.bin\"),\n            map_location=\"cpu\", weights_only=True,\n        )\n\n    model.load_state_dict(state_dict)\n    model.to(device)\n    return model\n\n\ndef collect_all_activations(model, calibration_data, attn_keep_masks, mlp_keep_masks, device):\n    \"\"\"Collect both GQA-group and MLP-group activations in a single forward pass.\n\n    Returns:\n        attn_acts: dict[layer_idx] -> tensor[n_samples, n_retained_gqa, heads_per_kv * head_dim]\n        mlp_acts:  dict[layer_idx] -> tensor[n_samples, n_retained_mlp, group_size]\n    \"\"\"\n    config = model.config\n    n_layers = config.num_hidden_layers\n    n_heads = config.num_attention_heads\n    n_kv_heads = config.num_key_value_heads\n    head_dim = config.hidden_size // n_heads\n    heads_per_kv = n_heads // n_kv_heads\n\n    q_outputs = {i: [] for i in range(n_layers)}\n    gate_outputs = {i: [] for i in range(n_layers)}\n    hooks = []\n\n    def make_q_hook(layer_idx):\n        def fn(module, inp, out):\n            q_outputs[layer_idx].append(out.detach().cpu())\n        return fn\n\n    def make_gate_hook(layer_idx):\n        def fn(module, inp, out):\n            gate_outputs[layer_idx].append(out.detach().cpu())\n        return fn\n\n    for i in range(n_layers):\n        h1 = model.model.layers[i].self_attn.q_proj.register_forward_hook(make_q_hook(i))\n        h2 = model.model.layers[i].mlp.gate_proj.register_forward_hook(make_gate_hook(i))\n        hooks.extend([h1, h2])\n\n    model.eval()\n    with torch.no_grad():\n        for idx, enc in enumerate(calibration_data):\n            input_ids = enc[\"input_ids\"].to(device)\n            attention_mask = enc[\"attention_mask\"].to(device)\n            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)\n            if (idx + 1) % 50 == 0:\n                logger.info(f\"  Processed {idx + 1}/{len(calibration_data)} samples\")\n\n    for h in hooks:\n        h.remove()\n\n    attn_activations = {}\n    for layer_idx in range(n_layers):\n        n_retained_gqa = len(attn_keep_masks[layer_idx])\n        per_group = []\n        for t in q_outputs[layer_idx]:\n            t = t.squeeze(0)  # [seq, n_retained_gqa * heads_per_kv * head_dim]\n            t = t.view(t.shape[0], n_retained_gqa, heads_per_kv, head_dim)\n            t = t.view(t.shape[0], n_retained_gqa, heads_per_kv * head_dim)\n            t = t.mean(dim=0)  # [n_retained_gqa, heads_per_kv * head_dim]\n            per_group.append(t)\n        attn_activations[layer_idx] = torch.stack(per_group, dim=0).float()\n        q_outputs[layer_idx] = None\n\n    mlp_activations = {}\n    for layer_idx in range(n_layers):\n        n_retained = len(mlp_keep_masks[layer_idx])\n        per_group = []\n        for t in gate_outputs[layer_idx]:\n            t = t.squeeze(0)  # [seq, n_retained * group_size]\n            total_channels = t.shape[-1]\n            group_size = total_channels // n_retained\n            usable = n_retained * group_size\n            t = t[:, :usable].view(t.shape[0], n_retained, group_size)\n            t = t.mean(dim=0)  # [n_retained, group_size]\n            per_group.append(t)\n        mlp_activations[layer_idx] = torch.stack(per_group, dim=0).float()\n        gate_outputs[layer_idx] = None\n\n    return attn_activations, mlp_activations\n\n\ndef compute_attn_recoverability(pruned_acts, recovered_acts, cka_data, attn_keep_masks,\n                                n_gqa_groups_original):\n    attn_overlap = cka_data[\"attn_overlap\"]\n    attn_cka_matrix = cka_data[\"attn_cka_matrix\"]\n    results = []\n\n    for layer_idx in sorted(attn_keep_masks.keys()):\n        retained = attn_keep_masks[layer_idx]\n        pruned_groups = sorted(set(range(n_gqa_groups_original)) - set(retained))\n        if not pruned_groups:\n            continue\n\n        cka_matrix = attn_cka_matrix[layer_idx]\n\n        for g_p in pruned_groups:\n            sims = torch.tensor([cka_matrix[g_p, g_r].item() for g_r in retained])\n            best_idx = sims.argmax().item()\n            g_r = retained[best_idx]\n            g_r_local = retained.index(g_r)\n\n            act_p = pruned_acts[layer_idx][:, g_r_local, :]\n            act_r = recovered_acts[layer_idx][:, g_r_local, :]\n            cos_sim = F.cosine_similarity(act_p, act_r, dim=-1)\n            activation_shift = 1.0 - cos_sim.mean().item()\n\n            results.append({\n                \"layer\": layer_idx,\n                \"type\": \"attention\",\n                \"pruned_group\": g_p,\n                \"best_retained_group\": g_r,\n                \"cka_overlap\": attn_overlap[layer_idx][g_p].item(),\n                \"recoverability\": activation_shift,\n                \"cka_similarity_to_retained\": sims[best_idx].item(),\n            })\n\n    return results\n\n\ndef compute_mlp_recoverability(pruned_acts, recovered_acts, cka_data, mlp_keep_masks,\n                               n_mlp_groups_original):\n    mlp_overlap = cka_data[\"mlp_overlap\"]\n    mlp_cka_matrix = cka_data[\"mlp_cka_matrix\"]\n    results = []\n\n    for layer_idx in sorted(mlp_keep_masks.keys()):\n        retained = mlp_keep_masks[layer_idx]\n        pruned_groups = sorted(set(range(n_mlp_groups_original)) - set(retained))\n        if not pruned_groups:\n            continue\n\n        cka_matrix = mlp_cka_matrix[layer_idx]\n\n        for m_p in pruned_groups:\n            sims = torch.tensor([cka_matrix[m_p, m_r].item() for m_r in retained])\n            best_idx = sims.argmax().item()\n            m_r = retained[best_idx]\n            m_r_local = retained.index(m_r)\n\n            act_p = pruned_acts[layer_idx][:, m_r_local, :]\n            act_r = recovered_acts[layer_idx][:, m_r_local, :]\n            cos_sim = F.cosine_similarity(act_p, act_r, dim=-1)\n            activation_shift = 1.0 - cos_sim.mean().item()\n\n            results.append({\n                \"layer\": layer_idx,\n                \"type\": \"mlp\",\n                \"pruned_group\": m_p,\n                \"best_retained_group\": m_r,\n                \"cka_overlap\": mlp_overlap[layer_idx][m_p].item(),\n                \"recoverability\": activation_shift,\n                \"cka_similarity_to_retained\": sims[best_idx].item(),\n            })\n\n    return results\n\n\ndef bootstrap_spearman(x, y, n_bootstrap=10000, seed=42):\n    rng = np.random.RandomState(seed)\n    x, y = np.array(x), np.array(y)\n    n = len(x)\n    rhos = []\n    for _ in range(n_bootstrap):\n        idx = rng.choice(n, n, replace=True)\n        r, _ = stats.spearmanr(x[idx], y[idx])\n        if not np.isnan(r):\n            rhos.append(r)\n    return np.percentile(rhos, [2.5, 97.5]).tolist()\n\n\ndef permutation_test(x, y, n_perm=10000, seed=42):\n    rng = np.random.RandomState(seed)\n    x, y = np.array(x), np.array(y)\n    observed, _ = stats.spearmanr(x, y)\n    count = 0\n    for _ in range(n_perm):\n        r, _ = stats.spearmanr(x, rng.permutation(y))\n        if abs(r) >= abs(observed):\n            count += 1\n    return count / n_perm\n\n\ndef compute_correlation_stats(fh, rec, seed=42):\n    if len(fh) < 3:\n        return {\n            \"spearman_rho\": float(\"nan\"), \"p_value\": float(\"nan\"),\n            \"bootstrap_ci_95\": [float(\"nan\"), float(\"nan\")],\n            \"permutation_p_value\": float(\"nan\"),\n            \"n_pruned_groups\": len(fh),\n        }\n    rho, p_value = stats.spearmanr(fh, rec)\n    ci = bootstrap_spearman(fh, rec, seed=seed)\n    perm_p = permutation_test(fh, rec, seed=seed)\n    return {\n        \"spearman_rho\": rho, \"p_value\": p_value,\n        \"bootstrap_ci_95\": ci, \"permutation_p_value\": perm_p,\n        \"n_pruned_groups\": len(fh),\n    }\n\n\ndef make_scatter_plot(results, stat, output_path, title_prefix=\"\", color_by_type=False):\n    try:\n        import matplotlib\n        matplotlib.use(\"Agg\")\n        import matplotlib.pyplot as plt\n    except ImportError:\n        logger.warning(\"matplotlib not available, skipping scatter plot\")\n        return\n\n    fh = [r[\"cka_overlap\"] for r in results]\n    rec = [r[\"recoverability\"] for r in results]\n    rho = stat[\"spearman_rho\"]\n    p_value = stat[\"p_value\"]\n    ci = stat[\"bootstrap_ci_95\"]\n    perm_p = stat.get(\"permutation_p_value\", float(\"nan\"))\n\n    fig, ax = plt.subplots(figsize=(8, 6))\n\n    if color_by_type:\n        type_colors = {\"attention\": \"#1f77b4\", \"mlp\": \"#ff7f0e\"}\n        for stype, color in type_colors.items():\n            mask = [r[\"type\"] == stype for r in results]\n            x = [f for f, m in zip(fh, mask) if m]\n            y = [r for r, m in zip(rec, mask) if m]\n            if x:\n                ax.scatter(x, y, c=color, alpha=0.7, edgecolors=\"k\",\n                           linewidths=0.3, s=30, label=stype)\n        ax.legend()\n    else:\n        layers = [r[\"layer\"] for r in results]\n        sc = ax.scatter(fh, rec, c=layers, cmap=\"viridis\", alpha=0.7,\n                        edgecolors=\"k\", linewidths=0.3, s=30)\n        plt.colorbar(sc, ax=ax, label=\"Layer index\")\n\n    ax.set_xlabel(\"F(g) — CKA overlap of pruned structure\")\n    ax.set_ylabel(\"Recoverability — activation shift of best retained structure\")\n\n    verdict = \"PASS\" if rho >= 0.4 else (\"WARNING\" if rho >= 0.3 else \"FAIL\")\n    ax.set_title(\n        f\"{title_prefix}CKA Overlap vs RLVR Recoverability\\n\"\n        f\"ρ={rho:.3f}, 95% CI=[{ci[0]:.3f}, {ci[1]:.3f}], \"\n        f\"p={p_value:.1e}, perm_p={perm_p:.1e} — {verdict}\"\n    )\n    plt.tight_layout()\n    plt.savefig(output_path, dpi=150, bbox_inches=\"tight\")\n    plt.close()\n    logger.info(f\"Scatter plot saved to {output_path}\")\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Correlation analysis: rho(CKA overlap, RLVR recoverability) \"\n                    \"for attention GQA groups and MLP channel groups\"\n    )\n    parser.add_argument(\"--base_model_path\", required=True,\n                        help=\"Path to original unpruned model\")\n    parser.add_argument(\"--pruned_model_path\", required=True,\n                        help=\"Path to pruned model (before RLVR)\")\n    parser.add_argument(\"--recovered_model_path\", required=True,\n                        help=\"Path to RLVR-recovered model\")\n    parser.add_argument(\"--cka_scores_path\", required=True,\n                        help=\"Path to CKA overlap .pt file\")\n    parser.add_argument(\"--pruning_mask_path\", required=True,\n                        help=\"Path to pruning_metadata.pt\")\n    parser.add_argument(\"--n_samples\", type=int, default=128,\n                        help=\"Number of calibration samples\")\n    parser.add_argument(\"--n_gqa_groups\", type=int, default=4,\n                        help=\"Number of original GQA groups (KV heads) per layer\")\n    parser.add_argument(\"--n_mlp_groups\", type=int, default=28,\n                        help=\"Number of original MLP channel groups per layer\")\n    parser.add_argument(\"--output_dir\", default=\"results/analysis/\",\n                        help=\"Output directory\")\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--dtype\", type=str, default=\"bfloat16\",\n                        choices=[\"float16\", \"bfloat16\", \"float32\"])\n    args = parser.parse_args()\n\n    set_seed(args.seed)\n    device = torch.device(\"cuda\" if torch.cuda.is_available() else \"cpu\")\n    torch_dtype = {\"float16\": torch.float16, \"bfloat16\": torch.bfloat16,\n                   \"float32\": torch.float32}[args.dtype]\n\n    logger.info(\"Loading CKA scores...\")\n    cka_data = torch.load(args.cka_scores_path, map_location=\"cpu\", weights_only=True)\n    for key in (\"attn_cka_matrix\", \"mlp_cka_matrix\"):\n        if key not in cka_data:\n            raise ValueError(f\"CKA scores missing '{key}'. Re-run cka_overlap.py.\")\n\n    logger.info(\"Loading pruning metadata...\")\n    pruning_meta = torch.load(args.pruning_mask_path, map_location=\"cpu\",\n                              weights_only=True)\n    attn_keep_masks = pruning_meta[\"attn_keep_masks\"]\n    mlp_keep_masks = pruning_meta[\"mlp_keep_masks\"]\n\n    tokenizer = AutoTokenizer.from_pretrained(args.base_model_path, trust_remote_code=True)\n    calibration_data = load_calibration_data(tokenizer, args.n_samples, seed=args.seed)\n    logger.info(f\"Loaded {len(calibration_data)} calibration samples\")\n\n    # --- Pruned model ---\n    logger.info(f\"Loading pruned model from {args.pruned_model_path}\")\n    pruned_model = load_pruned_model(\n        args.base_model_path, args.pruned_model_path, pruning_meta, torch_dtype, device\n    )\n    logger.info(\"Collecting activations from pruned model...\")\n    pruned_attn_acts, pruned_mlp_acts = collect_all_activations(\n        pruned_model, calibration_data, attn_keep_masks, mlp_keep_masks, device\n    )\n    del pruned_model\n    torch.cuda.empty_cache()\n\n    # --- Recovered model ---\n    logger.info(f\"Loading recovered model from {args.recovered_model_path}\")\n    recovered_model = load_pruned_model(\n        args.base_model_path, args.recovered_model_path, pruning_meta, torch_dtype, device\n    )\n    logger.info(\"Collecting activations from recovered model...\")\n    recovered_attn_acts, recovered_mlp_acts = collect_all_activations(\n        recovered_model, calibration_data, attn_keep_masks, mlp_keep_masks, device\n    )\n    del recovered_model\n    torch.cuda.empty_cache()\n\n    # --- Attention recoverability ---\n    logger.info(\"Computing attention recoverability...\")\n    attn_results = compute_attn_recoverability(\n        pruned_attn_acts, recovered_attn_acts, cka_data,\n        attn_keep_masks, args.n_gqa_groups,\n    )\n    del pruned_attn_acts, recovered_attn_acts\n    logger.info(f\"Computed recoverability for {len(attn_results)} pruned GQA groups\")\n\n    # --- MLP recoverability ---\n    logger.info(\"Computing MLP recoverability...\")\n    mlp_results = compute_mlp_recoverability(\n        pruned_mlp_acts, recovered_mlp_acts, cka_data,\n        mlp_keep_masks, args.n_mlp_groups,\n    )\n    del pruned_mlp_acts, recovered_mlp_acts\n    logger.info(f\"Computed recoverability for {len(mlp_results)} pruned MLP groups\")\n\n    # --- Statistics ---\n    attn_fh = [r[\"cka_overlap\"] for r in attn_results]\n    attn_rec = [r[\"recoverability\"] for r in attn_results]\n    attn_stats = compute_correlation_stats(attn_fh, attn_rec, seed=args.seed)\n\n    mlp_fh = [r[\"cka_overlap\"] for r in mlp_results]\n    mlp_rec = [r[\"recoverability\"] for r in mlp_results]\n    mlp_stats = compute_correlation_stats(mlp_fh, mlp_rec, seed=args.seed)\n\n    combined_results = attn_results + mlp_results\n    combined_fh = [r[\"cka_overlap\"] for r in combined_results]\n    combined_rec = [r[\"recoverability\"] for r in combined_results]\n    combined_stats = compute_correlation_stats(combined_fh, combined_rec, seed=args.seed)\n    combined_stats[\"n_total_pruned\"] = len(combined_results)\n\n    combined_rho = combined_stats[\"spearman_rho\"]\n    verdict = \"PASS\" if combined_rho >= 0.4 else (\n        \"WARNING\" if combined_rho >= 0.3 else \"FAIL\")\n\n    # --- Save results ---\n    os.makedirs(args.output_dir, exist_ok=True)\n\n    output = {\n        \"attention\": {**attn_stats, \"per_group_data\": attn_results},\n        \"mlp\": {**mlp_stats, \"per_group_data\": mlp_results},\n        \"combined\": combined_stats,\n        \"mvp_verdict\": verdict,\n    }\n    json_path = os.path.join(args.output_dir, \"correlation_results.json\")\n    with open(json_path, \"w\") as f:\n        json.dump(output, f, indent=2)\n    logger.info(f\"Results saved to {json_path}\")\n\n    # --- Scatter plots ---\n    if attn_results:\n        make_scatter_plot(\n            attn_results, attn_stats,\n            os.path.join(args.output_dir, \"fh_vs_recoverability_attention.png\"),\n            title_prefix=\"Attention: \",\n        )\n    if mlp_results:\n        make_scatter_plot(\n            mlp_results, mlp_stats,\n            os.path.join(args.output_dir, \"fh_vs_recoverability_mlp.png\"),\n            title_prefix=\"MLP: \",\n        )\n    if combined_results:\n        make_scatter_plot(\n            combined_results, combined_stats,\n            os.path.join(args.output_dir, \"fh_vs_recoverability_combined.png\"),\n            title_prefix=\"Combined: \",\n            color_by_type=True,\n        )\n\n    # --- Summary ---\n    print(f\"\\n{'='*60}\")\n    print(\"Correlation Analysis Results (Attention + MLP)\")\n    print(f\"{'='*60}\")\n    if attn_results:\n        print(f\"  ATTENTION: rho={attn_stats['spearman_rho']:.4f}, \"\n              f\"p={attn_stats['p_value']:.2e}, N={len(attn_results)}\")\n    else:\n        print(\"  ATTENTION: no pruned groups\")\n    if mlp_results:\n        print(f\"  MLP:       rho={mlp_stats['spearman_rho']:.4f}, \"\n              f\"p={mlp_stats['p_value']:.2e}, N={len(mlp_results)}\")\n    else:\n        print(\"  MLP:       no pruned groups\")\n    print(f\"  COMBINED:  rho={combined_rho:.4f}, \"\n          f\"p={combined_stats['p_value']:.2e}, N={len(combined_results)}\")\n    print(f\"  95% CI:    [{combined_stats['bootstrap_ci_95'][0]:.4f}, \"\n          f\"{combined_stats['bootstrap_ci_95'][1]:.4f}]\")\n    print(f\"  MVP Verdict: {verdict}\")\n    print(f\"{'='*60}\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_mlp-correlation-extend_20260514T052804",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/correlation_analysis.py",
    "content": "\"\"\"\nCorrelation Analysis: rho(CKA overlap, RLVR recoverability).\n\nTests the hypothesis: pruned structures (GQA groups or MLP channel groups) with\nhigher CKA overlap F(g) are more effectively compensated by RLVR through their\nmost similar retained structure.\n\nMetric: for each pruned structure g_p, find the most CKA-similar retained\nstructure g_r, then measure g_r's activation shift between pruned and\nRLVR-recovered models.\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nimport random\n\nimport numpy as np\nimport scipy.stats as stats\nimport torch\nimport torch.nn.functional as F\nfrom datasets import load_dataset\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n)\nlogger = logging.getLogger(__name__)\n\n\ndef set_seed(seed: int):\n    random.seed(seed)\n    np.random.seed(seed)\n    torch.manual_seed(seed)\n    torch.cuda.manual_seed_all(seed)\n\n\ndef load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):\n    ds = load_dataset(\"openai/gsm8k\", \"main\", split=\"train\")\n    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))\n    encodings = []\n    for example in ds:\n        prompt = f\"Question: {example['question']}\\nAnswer: Let me think step by step.\\n\"\n        ids = tokenizer(prompt, return_tensors=\"pt\", truncation=True, max_length=max_length)\n        encodings.append(ids)\n    return encodings\n\n\ndef load_pruned_model(base_model_path, saved_model_path, pruning_meta, torch_dtype, device):\n    logging.getLogger(\"prune\").setLevel(logging.WARNING)\n    from prune import prune_attention_heads, prune_mlp_channels\n\n    model = AutoModelForCausalLM.from_pretrained(\n        base_model_path, torch_dtype=torch_dtype, device_map=\"cpu\", trust_remote_code=True\n    )\n    prune_attention_heads(model, pruning_meta[\"attn_keep_masks\"])\n    prune_mlp_channels(model, pruning_meta[\"mlp_keep_masks\"])\n\n    safetensor_files = sorted(\n        [f for f in os.listdir(saved_model_path) if f.endswith(\".safetensors\")]\n    )\n    if safetensor_files:\n        from safetensors.torch import load_file\n        state_dict = {}\n        for f in safetensor_files:\n            state_dict.update(load_file(os.path.join(saved_model_path, f)))\n    else:\n        state_dict = torch.load(\n            os.path.join(saved_model_path, \"pytorch_model.bin\"),\n            map_location=\"cpu\", weights_only=True,\n        )\n\n    model.load_state_dict(state_dict)\n    model.to(device)\n    return model\n\n\ndef collect_all_activations(model, calibration_data, attn_keep_masks, mlp_keep_masks, device):\n    \"\"\"Collect both GQA-group and MLP-group activations in a single forward pass.\n\n    Returns:\n        attn_acts: dict[layer_idx] -> tensor[n_samples, n_retained_gqa, heads_per_kv * head_dim]\n        mlp_acts:  dict[layer_idx] -> tensor[n_samples, n_retained_mlp, group_size]\n    \"\"\"\n    config = model.config\n    n_layers = config.num_hidden_layers\n    n_heads = config.num_attention_heads\n    n_kv_heads = config.num_key_value_heads\n    head_dim = config.hidden_size // n_heads\n    heads_per_kv = n_heads // n_kv_heads\n\n    q_outputs = {i: [] for i in range(n_layers)}\n    gate_outputs = {i: [] for i in range(n_layers)}\n    hooks = []\n\n    def make_q_hook(layer_idx):\n        def fn(module, inp, out):\n            q_outputs[layer_idx].append(out.detach().cpu())\n        return fn\n\n    def make_gate_hook(layer_idx):\n        def fn(module, inp, out):\n            gate_outputs[layer_idx].append(out.detach().cpu())\n        return fn\n\n    for i in range(n_layers):\n        h1 = model.model.layers[i].self_attn.q_proj.register_forward_hook(make_q_hook(i))\n        h2 = model.model.layers[i].mlp.gate_proj.register_forward_hook(make_gate_hook(i))\n        hooks.extend([h1, h2])\n\n    model.eval()\n    with torch.no_grad():\n        for idx, enc in enumerate(calibration_data):\n            input_ids = enc[\"input_ids\"].to(device)\n            attention_mask = enc[\"attention_mask\"].to(device)\n            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)\n            if (idx + 1) % 50 == 0:\n                logger.info(f\"  Processed {idx + 1}/{len(calibration_data)} samples\")\n\n    for h in hooks:\n        h.remove()\n\n    attn_activations = {}\n    for layer_idx in range(n_layers):\n        n_retained_gqa = len(attn_keep_masks[layer_idx])\n        per_group = []\n        for t in q_outputs[layer_idx]:\n            t = t.squeeze(0)  # [seq, n_retained_gqa * heads_per_kv * head_dim]\n            t = t.view(t.shape[0], n_retained_gqa, heads_per_kv, head_dim)\n            t = t.view(t.shape[0], n_retained_gqa, heads_per_kv * head_dim)\n            t = t.mean(dim=0)  # [n_retained_gqa, heads_per_kv * head_dim]\n            per_group.append(t)\n        attn_activations[layer_idx] = torch.stack(per_group, dim=0).float()\n        q_outputs[layer_idx] = None\n\n    mlp_activations = {}\n    for layer_idx in range(n_layers):\n        n_retained = len(mlp_keep_masks[layer_idx])\n        per_group = []\n        for t in gate_outputs[layer_idx]:\n            t = t.squeeze(0)  # [seq, n_retained * group_size]\n            total_channels = t.shape[-1]\n            group_size = total_channels // n_retained\n            usable = n_retained * group_size\n            t = t[:, :usable].view(t.shape[0], n_retained, group_size)\n            t = t.mean(dim=0)  # [n_retained, group_size]\n            per_group.append(t)\n        mlp_activations[layer_idx] = torch.stack(per_group, dim=0).float()\n        gate_outputs[layer_idx] = None\n\n    return attn_activations, mlp_activations\n\n\ndef compute_attn_recoverability(pruned_acts, recovered_acts, cka_data, attn_keep_masks,\n                                n_gqa_groups_original):\n    attn_overlap = cka_data[\"attn_overlap\"]\n    attn_cka_matrix = cka_data[\"attn_cka_matrix\"]\n    results = []\n\n    for layer_idx in sorted(attn_keep_masks.keys()):\n        retained = attn_keep_masks[layer_idx]\n        pruned_groups = sorted(set(range(n_gqa_groups_original)) - set(retained))\n        if not pruned_groups:\n            continue\n\n        cka_matrix = attn_cka_matrix[layer_idx]\n\n        for g_p in pruned_groups:\n            sims = torch.tensor([cka_matrix[g_p, g_r].item() for g_r in retained])\n            best_idx = sims.argmax().item()\n            g_r = retained[best_idx]\n            g_r_local = retained.index(g_r)\n\n            act_p = pruned_acts[layer_idx][:, g_r_local, :]\n            act_r = recovered_acts[layer_idx][:, g_r_local, :]\n            cos_sim = F.cosine_similarity(act_p, act_r, dim=-1)\n            activation_shift = 1.0 - cos_sim.mean().item()\n\n            results.append({\n                \"layer\": layer_idx,\n                \"type\": \"attention\",\n                \"pruned_group\": g_p,\n                \"best_retained_group\": g_r,\n                \"cka_overlap\": attn_overlap[layer_idx][g_p].item(),\n                \"recoverability\": activation_shift,\n                \"cka_similarity_to_retained\": sims[best_idx].item(),\n            })\n\n    return results\n\n\ndef compute_mlp_recoverability(pruned_acts, recovered_acts, cka_data, mlp_keep_masks,\n                               n_mlp_groups_original):\n    mlp_overlap = cka_data[\"mlp_overlap\"]\n    mlp_cka_matrix = cka_data[\"mlp_cka_matrix\"]\n    results = []\n\n    for layer_idx in sorted(mlp_keep_masks.keys()):\n        retained = mlp_keep_masks[layer_idx]\n        pruned_groups = sorted(set(range(n_mlp_groups_original)) - set(retained))\n        if not pruned_groups:\n            continue\n\n        cka_matrix = mlp_cka_matrix[layer_idx]\n\n        for m_p in pruned_groups:\n            sims = torch.tensor([cka_matrix[m_p, m_r].item() for m_r in retained])\n            best_idx = sims.argmax().item()\n            m_r = retained[best_idx]\n            m_r_local = retained.index(m_r)\n\n            act_p = pruned_acts[layer_idx][:, m_r_local, :]\n            act_r = recovered_acts[layer_idx][:, m_r_local, :]\n            cos_sim = F.cosine_similarity(act_p, act_r, dim=-1)\n            activation_shift = 1.0 - cos_sim.mean().item()\n\n            results.append({\n                \"layer\": layer_idx,\n                \"type\": \"mlp\",\n                \"pruned_group\": m_p,\n                \"best_retained_group\": m_r,\n                \"cka_overlap\": mlp_overlap[layer_idx][m_p].item(),\n                \"recoverability\": activation_shift,\n                \"cka_similarity_to_retained\": sims[best_idx].item(),\n            })\n\n    return results\n\n\ndef bootstrap_spearman(x, y, n_bootstrap=10000, seed=42):\n    rng = np.random.RandomState(seed)\n    x, y = np.array(x), np.array(y)\n    n = len(x)\n    rhos = []\n    for _ in range(n_bootstrap):\n        idx = rng.choice(n, n, replace=True)\n        r, _ = stats.spearmanr(x[idx], y[idx])\n        if not np.isnan(r):\n            rhos.append(r)\n    return np.percentile(rhos, [2.5, 97.5]).tolist()\n\n\ndef permutation_test(x, y, n_perm=10000, seed=42):\n    rng = np.random.RandomState(seed)\n    x, y = np.array(x), np.array(y)\n    observed, _ = stats.spearmanr(x, y)\n    count = 0\n    for _ in range(n_perm):\n        r, _ = stats.spearmanr(x, rng.permutation(y))\n        if abs(r) >= abs(observed):\n            count += 1\n    return count / n_perm\n\n\ndef compute_correlation_stats(fh, rec, seed=42):\n    if len(fh) < 3:\n        return {\n            \"spearman_rho\": float(\"nan\"), \"p_value\": float(\"nan\"),\n            \"bootstrap_ci_95\": [float(\"nan\"), float(\"nan\")],\n            \"permutation_p_value\": float(\"nan\"),\n            \"n_pruned_groups\": len(fh),\n        }\n    rho, p_value = stats.spearmanr(fh, rec)\n    ci = bootstrap_spearman(fh, rec, seed=seed)\n    perm_p = permutation_test(fh, rec, seed=seed)\n    return {\n        \"spearman_rho\": rho, \"p_value\": p_value,\n        \"bootstrap_ci_95\": ci, \"permutation_p_value\": perm_p,\n        \"n_pruned_groups\": len(fh),\n    }\n\n\ndef make_scatter_plot(results, stat, output_path, title_prefix=\"\", color_by_type=False):\n    try:\n        import matplotlib\n        matplotlib.use(\"Agg\")\n        import matplotlib.pyplot as plt\n    except ImportError:\n        logger.warning(\"matplotlib not available, skipping scatter plot\")\n        return\n\n    fh = [r[\"cka_overlap\"] for r in results]\n    rec = [r[\"recoverability\"] for r in results]\n    rho = stat[\"spearman_rho\"]\n    p_value = stat[\"p_value\"]\n    ci = stat[\"bootstrap_ci_95\"]\n    perm_p = stat.get(\"permutation_p_value\", float(\"nan\"))\n\n    fig, ax = plt.subplots(figsize=(8, 6))\n\n    if color_by_type:\n        type_colors = {\"attention\": \"#1f77b4\", \"mlp\": \"#ff7f0e\"}\n        for stype, color in type_colors.items():\n            mask = [r[\"type\"] == stype for r in results]\n            x = [f for f, m in zip(fh, mask) if m]\n            y = [r for r, m in zip(rec, mask) if m]\n            if x:\n                ax.scatter(x, y, c=color, alpha=0.7, edgecolors=\"k\",\n                           linewidths=0.3, s=30, label=stype)\n        ax.legend()\n    else:\n        layers = [r[\"layer\"] for r in results]\n        sc = ax.scatter(fh, rec, c=layers, cmap=\"viridis\", alpha=0.7,\n                        edgecolors=\"k\", linewidths=0.3, s=30)\n        plt.colorbar(sc, ax=ax, label=\"Layer index\")\n\n    ax.set_xlabel(\"F(g) — CKA overlap of pruned structure\")\n    ax.set_ylabel(\"Recoverability — activation shift of best retained structure\")\n\n    verdict = \"PASS\" if rho >= 0.4 else (\"WARNING\" if rho >= 0.3 else \"FAIL\")\n    ax.set_title(\n        f\"{title_prefix}CKA Overlap vs RLVR Recoverability\\n\"\n        f\"ρ={rho:.3f}, 95% CI=[{ci[0]:.3f}, {ci[1]:.3f}], \"\n        f\"p={p_value:.1e}, perm_p={perm_p:.1e} — {verdict}\"\n    )\n    plt.tight_layout()\n    plt.savefig(output_path, dpi=150, bbox_inches=\"tight\")\n    plt.close()\n    logger.info(f\"Scatter plot saved to {output_path}\")\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Correlation analysis: rho(CKA overlap, RLVR recoverability) \"\n                    \"for attention GQA groups and MLP channel groups\"\n    )\n    parser.add_argument(\"--base_model_path\", required=True,\n                        help=\"Path to original unpruned model\")\n    parser.add_argument(\"--pruned_model_path\", required=True,\n                        help=\"Path to pruned model (before RLVR)\")\n    parser.add_argument(\"--recovered_model_path\", required=True,\n                        help=\"Path to RLVR-recovered model\")\n    parser.add_argument(\"--cka_scores_path\", required=True,\n                        help=\"Path to CKA overlap .pt file\")\n    parser.add_argument(\"--pruning_mask_path\", required=True,\n                        help=\"Path to pruning_metadata.pt\")\n    parser.add_argument(\"--n_samples\", type=int, default=128,\n                        help=\"Number of calibration samples\")\n    parser.add_argument(\"--n_gqa_groups\", type=int, default=4,\n                        help=\"Number of original GQA groups (KV heads) per layer\")\n    parser.add_argument(\"--n_mlp_groups\", type=int, default=28,\n                        help=\"Number of original MLP channel groups per layer\")\n    parser.add_argument(\"--output_dir\", default=\"results/analysis/\",\n                        help=\"Output directory\")\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--dtype\", type=str, default=\"bfloat16\",\n                        choices=[\"float16\", \"bfloat16\", \"float32\"])\n    args = parser.parse_args()\n\n    set_seed(args.seed)\n    device = torch.device(\"cuda\" if torch.cuda.is_available() else \"cpu\")\n    torch_dtype = {\"float16\": torch.float16, \"bfloat16\": torch.bfloat16,\n                   \"float32\": torch.float32}[args.dtype]\n\n    logger.info(\"Loading CKA scores...\")\n    cka_data = torch.load(args.cka_scores_path, map_location=\"cpu\", weights_only=True)\n    for key in (\"attn_cka_matrix\", \"mlp_cka_matrix\"):\n        if key not in cka_data:\n            raise ValueError(f\"CKA scores missing '{key}'. Re-run cka_overlap.py.\")\n\n    logger.info(\"Loading pruning metadata...\")\n    pruning_meta = torch.load(args.pruning_mask_path, map_location=\"cpu\",\n                              weights_only=True)\n    attn_keep_masks = pruning_meta[\"attn_keep_masks\"]\n    mlp_keep_masks = pruning_meta[\"mlp_keep_masks\"]\n\n    tokenizer = AutoTokenizer.from_pretrained(args.base_model_path, trust_remote_code=True)\n    calibration_data = load_calibration_data(tokenizer, args.n_samples, seed=args.seed)\n    logger.info(f\"Loaded {len(calibration_data)} calibration samples\")\n\n    # --- Pruned model ---\n    logger.info(f\"Loading pruned model from {args.pruned_model_path}\")\n    pruned_model = load_pruned_model(\n        args.base_model_path, args.pruned_model_path, pruning_meta, torch_dtype, device\n    )\n    logger.info(\"Collecting activations from pruned model...\")\n    pruned_attn_acts, pruned_mlp_acts = collect_all_activations(\n        pruned_model, calibration_data, attn_keep_masks, mlp_keep_masks, device\n    )\n    del pruned_model\n    torch.cuda.empty_cache()\n\n    # --- Recovered model ---\n    logger.info(f\"Loading recovered model from {args.recovered_model_path}\")\n    recovered_model = load_pruned_model(\n        args.base_model_path, args.recovered_model_path, pruning_meta, torch_dtype, device\n    )\n    logger.info(\"Collecting activations from recovered model...\")\n    recovered_attn_acts, recovered_mlp_acts = collect_all_activations(\n        recovered_model, calibration_data, attn_keep_masks, mlp_keep_masks, device\n    )\n    del recovered_model\n    torch.cuda.empty_cache()\n\n    # --- Attention recoverability ---\n    logger.info(\"Computing attention recoverability...\")\n    attn_results = compute_attn_recoverability(\n        pruned_attn_acts, recovered_attn_acts, cka_data,\n        attn_keep_masks, args.n_gqa_groups,\n    )\n    del pruned_attn_acts, recovered_attn_acts\n    logger.info(f\"Computed recoverability for {len(attn_results)} pruned GQA groups\")\n\n    # --- MLP recoverability ---\n    logger.info(\"Computing MLP recoverability...\")\n    mlp_results = compute_mlp_recoverability(\n        pruned_mlp_acts, recovered_mlp_acts, cka_data,\n        mlp_keep_masks, args.n_mlp_groups,\n    )\n    del pruned_mlp_acts, recovered_mlp_acts\n    logger.info(f\"Computed recoverability for {len(mlp_results)} pruned MLP groups\")\n\n    # --- Statistics ---\n    attn_fh = [r[\"cka_overlap\"] for r in attn_results]\n    attn_rec = [r[\"recoverability\"] for r in attn_results]\n    attn_stats = compute_correlation_stats(attn_fh, attn_rec, seed=args.seed)\n\n    mlp_fh = [r[\"cka_overlap\"] for r in mlp_results]\n    mlp_rec = [r[\"recoverability\"] for r in mlp_results]\n    mlp_stats = compute_correlation_stats(mlp_fh, mlp_rec, seed=args.seed)\n\n    combined_results = attn_results + mlp_results\n    combined_fh = [r[\"cka_overlap\"] for r in combined_results]\n    combined_rec = [r[\"recoverability\"] for r in combined_results]\n    combined_stats = compute_correlation_stats(combined_fh, combined_rec, seed=args.seed)\n    combined_stats[\"n_total_pruned\"] = len(combined_results)\n\n    combined_rho = combined_stats[\"spearman_rho\"]\n    verdict = \"PASS\" if combined_rho >= 0.4 else (\n        \"WARNING\" if combined_rho >= 0.3 else \"FAIL\")\n\n    # --- Save results ---\n    os.makedirs(args.output_dir, exist_ok=True)\n\n    output = {\n        \"attention\": {**attn_stats, \"per_group_data\": attn_results},\n        \"mlp\": {**mlp_stats, \"per_group_data\": mlp_results},\n        \"combined\": combined_stats,\n        \"mvp_verdict\": verdict,\n    }\n    json_path = os.path.join(args.output_dir, \"correlation_results.json\")\n    with open(json_path, \"w\") as f:\n        json.dump(output, f, indent=2)\n    logger.info(f\"Results saved to {json_path}\")\n\n    # --- Scatter plots ---\n    if attn_results:\n        make_scatter_plot(\n            attn_results, attn_stats,\n            os.path.join(args.output_dir, \"fh_vs_recoverability_attention.png\"),\n            title_prefix=\"Attention: \",\n        )\n    if mlp_results:\n        make_scatter_plot(\n            mlp_results, mlp_stats,\n            os.path.join(args.output_dir, \"fh_vs_recoverability_mlp.png\"),\n            title_prefix=\"MLP: \",\n        )\n    if combined_results:\n        make_scatter_plot(\n            combined_results, combined_stats,\n            os.path.join(args.output_dir, \"fh_vs_recoverability_combined.png\"),\n            title_prefix=\"Combined: \",\n            color_by_type=True,\n        )\n\n    # --- Summary ---\n    print(f\"\\n{'='*60}\")\n    print(\"Correlation Analysis Results (Attention + MLP)\")\n    print(f\"{'='*60}\")\n    if attn_results:\n        print(f\"  ATTENTION: rho={attn_stats['spearman_rho']:.4f}, \"\n              f\"p={attn_stats['p_value']:.2e}, N={len(attn_results)}\")\n    else:\n        print(\"  ATTENTION: no pruned groups\")\n    if mlp_results:\n        print(f\"  MLP:       rho={mlp_stats['spearman_rho']:.4f}, \"\n              f\"p={mlp_stats['p_value']:.2e}, N={len(mlp_results)}\")\n    else:\n        print(\"  MLP:       no pruned groups\")\n    print(f\"  COMBINED:  rho={combined_rho:.4f}, \"\n          f\"p={combined_stats['p_value']:.2e}, N={len(combined_results)}\")\n    print(f\"  95% CI:    [{combined_stats['bootstrap_ci_95'][0]:.4f}, \"\n          f\"{combined_stats['bootstrap_ci_95'][1]:.4f}]\")\n    print(f\"  MVP Verdict: {verdict}\")\n    print(f\"{'='*60}\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-14T05:38:16.875998+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/correlation_analysis.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_mlp-correlation-extend_20260514T052804",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-14T05:38:16.876205+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/correlation_analysis.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_mlp-correlation-extend_20260514T052804",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/correlation_analysis.py"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-14T05:38:16.876596+00:00_

1	"""
2	Correlation Analysis: rho(CKA overlap, RLVR recoverability).
3	
4	Tests the hypothesis: pruned structures (GQA groups or MLP channel groups) with
5	higher CKA overlap F(g) are more effectively compensated by RLVR through their
6	most similar retained structure.
7	
8	Metric: for each pruned structure g_p, find the most CKA-similar retained
9	structure g_r, then measure g_r's activation shift between pruned and
10	RLVR-recovered models.
11	"""
12	
13	import argparse
14	import json
15	import logging
16	import os
17	import random
18	
19	import numpy as np
20	import scipy.stats as stats
21	import torch
22	import torch.nn.functional as F
23	from datasets import load_dataset
24	from transformers import AutoModelForCausalLM, AutoTokenizer
25	
26	logging.basicConfig(
27	    level=logging.INFO,
28	    format="%(asctime)s [%(levelname)s] %(message)s",
29	)
30	logger = logging.getLogger(__name__)
31	
32	
33	def set_seed(seed: int):
34	    random.seed(seed)
35	    np.random.seed(seed)
36	    torch.manual_seed(seed)
37	    torch.cuda.manual_seed_all(seed)
38	
39	
40	def load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):
41	    ds = load_dataset("openai/gsm8k", "main", split="train")
42	    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))
43	    encodings = []
44	    for example in ds:
45	        prompt = f"Question: {example['question']}\nAnswer: Let me think step by step.\n"
46	        ids = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=max_length)
47	        encodings.append(ids)
48	    return encodings
49	
50	
51	def load_pruned_model(base_model_path, saved_model_path, pruning_meta, torch_dtype, device):
52	    logging.getLogger("prune").setLevel(logging.WARNING)
53	    from prune import prune_attention_heads, prune_mlp_channels
54	
55	    model = AutoModelForCausalLM.from_pretrained(
56	        base_model_path, torch_dtype=torch_dtype, device_map="cpu", trust_remote_code=True
57	    )
58	    p
…[truncated 19006 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_mlp-correlation-extend_20260514T052804",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-14T05:38:16.876867+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westb-23072",
  "command": "cat > /root/recovery_aware_struct_prune/src/correlation_analysis.py << 'FILEEOF'\n\"\"\"\nCorrelation Analysis: rho(CKA overlap, RLVR recoverability).\n\nTests the hypothesis: pruned structures (GQA groups or MLP channel groups) with\nhigher CKA overlap F(g) are more effectively compensated by RLVR through their\nmost similar retained structure.\n\nMetric: for each pruned structure g_p, find the most CKA-similar retained\nstructure g_r, then measure g_r's activation shift between pruned and\nRLVR-recovered models.\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nimport random\n\nimport numpy as np\nimport scipy.stats as stats\nimport torch\nimport torch.nn.functional as F\nfrom datasets import load_dataset\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n)\nlogger = logging.getLogger(__name__)\n\n\ndef set_seed(seed: int):\n    random.seed(seed)\n    np.random.seed(seed)\n    torch.manual_seed(seed)\n    torch.cuda.manual_seed_all(seed)\n\n\ndef load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):\n    ds = load_dataset(\"openai/gsm8k\", \"main\", split=\"train\")\n    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))\n    encodings = []\n    for example in ds:\n        prompt = f\"Question: {example['question']}\\nAnswer: Let me think step by step.\\n\"\n        ids = tokenizer(prompt, return_tensors=\"pt\", truncation=True, max_length=max_length)\n        encodings.append(ids)\n    return encodings\n\n\ndef load_pruned_model(base_model_path, saved_model_path, pruning_meta, torch_dtype, device):\n    logging.getLogger(\"prune\").setLevel(logging.WARNING)\n    from prune import prune_attention_heads, prune_mlp_channels\n\n    model = AutoModelForCausalLM.from_pretrained(\n        base_model_path, torch_dtype=torch_dtype, device_map=\"cpu\", trust_remote_code=True\n    )\n    prune_attention_heads(model, pruning_meta[\"attn_keep_masks\"])\n    prune_mlp_channels(model, pruning_meta[\"mlp_keep_masks\"])\n\n    safetensor_files = sorted(\n        [f for f in os.listdir(saved_model_path) if f.endswith(\".safetensors\")]\n    )\n    if safetensor_files:\n        from safetensors.torch import load_file\n        state_dict = {}\n        for f in safetensor_files:\n            state_dict.update(load_file(os.path.join(saved_model_path, f)))\n    else:\n        state_dict = torch.load(\n            os.path.join(saved_model_path, \"pytorch_model.bin\"),\n            map_location=\"cpu\", weights_only=True,\n        )\n\n    model.load_state_dict(state_dict)\n    model.to(device)\n    return model\n\n\ndef collect_all_activations(model, calibration_data, attn_keep_masks, mlp_keep_masks, device):\n    \"\"\"Collect both GQA-group and MLP-group activations in a single forward pass.\n\n    Returns:\n        attn_acts: dict[layer_idx] -> tensor[n_samples, n_retained_gqa, heads_per_kv * head_dim]\n        mlp_acts:  dict[layer_idx] -> tensor[n_samples, n_retained_mlp, group_size]\n    \"\"\"\n    config = model.config\n    n_layers = config.num_hidden_layers\n    n_heads = config.num_attention_heads\n    n_kv_heads = config.num_key_value_heads\n    head_dim = config.hidden_size // n_heads\n    heads_per_kv = n_heads // n_kv_heads\n\n    q_outputs = {i: [] for i in range(n_layers)}\n    gate_outputs = {i: [] for i in range(n_layers)}\n    hooks = []\n\n    def make_q_hook(layer_idx):\n        def fn(module, inp, out):\n            q_outputs[layer_idx].append(out.detach().cpu())\n        return fn\n\n    def make_gate_hook(layer_idx):\n        def fn(module, inp, out):\n            gate_outputs[layer_idx].append(out.detach().cpu())\n        return fn\n\n    for i in range(n_layers):\n        h1 = model.model.layers[i].self_attn.q_proj.register_forward_hook(make_q_hook(i))\n        h2 = model.model.layers[i].mlp.gate_proj.register_forward_hook(make_gate_hook(i))\n        hooks.extend([h1, h2])\n\n    model.eval()\n    with torch.no_grad():\n        for idx, enc in enumerate(calibration_data):\n            input_ids = enc[\"input_ids\"].to(device)\n            attention_mask = enc[\"attention_mask\"].to(device)\n            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)\n            if (idx + 1) % 50 == 0:\n                logger.info(f\"  Processed {idx + 1}/{len(calibration_data)} samples\")\n\n    for h in hooks:\n        h.remove()\n\n    attn_activations = {}\n    for layer_idx in range(n_layers):\n        n_retained_gqa = len(attn_keep_masks[layer_idx])\n        per_group = []\n        for t in q_outputs[layer_idx]:\n            t = t.squeeze(0)  # [seq, n_retained_gqa * heads_per_kv * head_dim]\n            t = t.view(t.shape[0], n_retained_gqa, heads_per_kv, head_dim)\n            t = t.view(t.shape[0], n_retained_gqa, heads_per_kv * head_dim)\n            t = t.mean(dim=0)  # [n_retained_gqa, heads_per_kv * head_dim]\n            per_group.append(t)\n        attn_activations[layer_idx] = torch.stack(per_group, dim=0).float()\n        q_outputs[layer_idx] = None\n\n    mlp_activations = {}\n    for layer_idx in range(n_layers):\n        n_retained = len(mlp_keep_masks[layer_idx])\n        per_group = []\n        for t in gate_outputs[layer_idx]:\n            t = t.squeeze(0)  # [seq, n_retained * group_size]\n            total_channels = t.shape[-1]\n            group_size = total_channels // n_retained\n            usable = n_retained * group_size\n            t = t[:, :usable].view(t.shape[0], n_retained, group_size)\n            t = t.mean(dim=0)  # [n_retained, group_size]\n            per_group.append(t)\n        mlp_activations[layer_idx] = torch.stack(per_group, dim=0).float()\n        gate_outputs[layer_idx] = None\n\n    return attn_activations, mlp_activations\n\n\ndef compute_attn_recoverability(pruned_acts, recovered_acts, cka_data, attn_keep_masks,\n                                n_gqa_groups_original):\n    attn_overlap = cka_data[\"attn_overlap\"]\n    attn_cka_matrix = cka_data[\"attn_cka_matrix\"]\n    results = []\n\n    for layer_idx in sorted(attn_keep_masks.keys()):\n        retained = attn_keep_masks[layer_idx]\n        pruned_groups = sorted(set(range(n_gqa_groups_original)) - set(retained))\n        if not pruned_groups:\n            continue\n\n        cka_matrix = attn_cka_matrix[layer_idx]\n\n        for g_p in pruned_groups:\n            sims = torch.tensor([cka_matrix[g_p, g_r].item() for g_r in retained])\n            best_idx = sims.argmax().item()\n            g_r = retained[best_idx]\n            g_r_local = retained.index(g_r)\n\n            act_p = pruned_acts[layer_idx][:, g_r_local, :]\n            act_r = recovered_acts[layer_idx][:, g_r_local, :]\n            cos_sim = F.cosine_similarity(act_p, act_r, dim=-1)\n            activation_shift = 1.0 - cos_sim.mean().item()\n\n            results.append({\n                \"layer\": layer_idx,\n                \"type\": \"attention\",\n                \"pruned_group\": g_p,\n                \"best_retained_group\": g_r,\n                \"cka_overlap\": attn_overlap[layer_idx][g_p].item(),\n                \"recoverability\": activation_shift,\n                \"cka_similarity_to_retained\": sims[best_idx].item(),\n            })\n\n    return results\n\n\ndef compute_mlp_recoverability(pruned_acts, recovered_acts, cka_data, mlp_keep_masks,\n                               n_mlp_groups_original):\n    mlp_overlap = cka_data[\"mlp_overlap\"]\n    mlp_cka_matrix = cka_data[\"mlp_cka_matrix\"]\n    results = []\n\n    for layer_idx in sorted(mlp_keep_masks.keys()):\n        retained = mlp_keep_masks[layer_idx]\n        pruned_groups = sorted(set(range(n_mlp_groups_original)) - set(retained))\n        if not pruned_groups:\n            continue\n\n        cka_matrix = mlp_cka_matrix[layer_idx]\n\n        for m_p in pruned_groups:\n            sims = torch.tensor([cka_matrix[m_p, m_r].item() for m_r in retained])\n            best_idx = sims.argmax().item()\n            m_r = retained[best_idx]\n            m_r_local = retained.index(m_r)\n\n            act_p = pruned_acts[layer_idx][:, m_r_local, :]\n            act_r = recovered_acts[layer_idx][:, m_r_local, :]\n            cos_sim = F.cosine_similarity(act_p, act_r, dim=-1)\n            activation_shift = 1.0 - cos_sim.mean().item()\n\n            results.append({\n                \"layer\": layer_idx,\n                \"type\": \"mlp\",\n                \"pruned_group\": m_p,\n                \"best_retained_group\": m_r,\n                \"cka_overlap\": mlp_overlap[layer_idx][m_p].item(),\n                \"recoverability\": activation_shift,\n                \"cka_similarity_to_retained\": sims[best_idx].item(),\n            })\n\n    return results\n\n\ndef bootstrap_spearman(x, y, n_bootstrap=10000, seed=42):\n    rng = np.random.RandomState(seed)\n    x, y = np.array(x), np.array(y)\n    n = len(x)\n    rhos = []\n    for _ in range(n_bootstrap):\n        idx = rng.choice(n, n, replace=True)\n        r, _ = stats.spearmanr(x[idx], y[idx])\n        if not np.isnan(r):\n            rhos.append(r)\n    return np.percentile(rhos, [2.5, 97.5]).tolist()\n\n\ndef permutation_test(x, y, n_perm=10000, seed=42):\n    rng = np.random.RandomState(seed)\n    x, y = np.array(x), np.array(y)\n    observed, _ = stats.spearmanr(x, y)\n    count = 0\n    for _ in range(n_perm):\n        r, _ = stats.spearmanr(x, rng.permutation(y))\n        if abs(r) >= abs(observed):\n            count += 1\n    return count / n_perm\n\n\ndef compute_correlation_stats(fh, rec, seed=42):\n    if len(fh) < 3:\n        return {\n            \"spearman_rho\": float(\"nan\"), \"p_value\": float(\"nan\"),\n            \"bootstrap_ci_95\": [float(\"nan\"), float(\"nan\")],\n            \"permutation_p_value\": float(\"nan\"),\n            \"n_pruned_groups\": len(fh),\n        }\n    rho, p_value = stats.spearmanr(fh, rec)\n    ci = bootstrap_spearman(fh, rec, seed=seed)\n    perm_p = permutation_test(fh, rec, seed=seed)\n    return {\n        \"spearman_rho\": rho, \"p_value\": p_value,\n        \"bootstrap_ci_95\": ci, \"permutation_p_value\": perm_p,\n        \"n_pruned_groups\": len(fh),\n    }\n\n\ndef make_scatter_plot(results, stat, output_path, title_prefix=\"\", color_by_type=False):\n    try:\n        import matplotlib\n        matplotlib.use(\"Agg\")\n        import matplotlib.pyplot as plt\n    except ImportError:\n        logger.warning(\"matplotlib not available, skipping scatter plot\")\n        return\n\n    fh = [r[\"cka_overlap\"] for r in results]\n    rec = [r[\"recoverability\"] for r in results]\n    rho = stat[\"spearman_rho\"]\n    p_value = stat[\"p_value\"]\n    ci = stat[\"bootstrap_ci_95\"]\n    perm_p = stat.get(\"permutation_p_value\", float(\"nan\"))\n\n    fig, ax = plt.subplots(figsize=(8, 6))\n\n    if color_by_type:\n        type_colors = {\"attention\": \"#1f77b4\", \"mlp\": \"#ff7f0e\"}\n        for stype, color in type_colors.items():\n            mask = [r[\"type\"] == stype for r in results]\n            x = [f for f, m in zip(fh, mask) if m]\n            y = [r for r, m in zip(rec, mask) if m]\n            if x:\n                ax.scatter(x, y, c=color, alpha=0.7, edgecolors=\"k\",\n                           linewidths=0.3, s=30, label=stype)\n        ax.legend()\n    else:\n        layers = [r[\"layer\"] for r in results]\n        sc = ax.scatter(fh, rec, c=layers, cmap=\"viridis\", alpha=0.7,\n                        edgecolors=\"k\", linewidths=0.3, s=30)\n        plt.colorbar(sc, ax=ax, label=\"Layer index\")\n\n    ax.set_xlabel(\"F(g) — CKA overlap of pruned structure\")\n    ax.set_ylabel(\"Recoverability — activation shift of best retained structure\")\n\n    verdict = \"PASS\" if rho >= 0.4 else (\"WARNING\" if rho >= 0.3 else \"FAIL\")\n    ax.set_title(\n        f\"{title_prefix}CKA Overlap vs RLVR Recoverability\\n\"\n        f\"ρ={rho:.3f}, 95% CI=[{ci[0]:.3f}, {ci[1]:.3f}], \"\n        f\"p={p_value:.1e}, perm_p={perm_p:.1e} — {verdict}\"\n    )\n    plt.tight_layout()\n    plt.savefig(output_path, dpi=150, bbox_inches=\"tight\")\n    plt.close()\n    logger.info(f\"Scatter plot saved to {output_path}\")\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Correlation analysis: rho(CKA overlap, RLVR recoverability) \"\n                    \"for attention GQA groups and MLP channel groups\"\n    )\n    parser.add_argument(\"--base_model_path\", required=True,\n                        help=\"Path to original unpruned model\")\n    parser.add_argument(\"--pruned_model_path\", required=True,\n                        help=\"Path to pruned model (before RLVR)\")\n    parser.add_argument(\"--recovered_model_path\", required=True,\n                        help=\"Path to RLVR-recovered model\")\n    parser.add_argument(\"--cka_scores_path\", required=True,\n                        help=\"Path to CKA overlap .pt file\")\n    parser.add_argument(\"--pruning_mask_path\", required=True,\n                        help=\"Path to pruning_metadata.pt\")\n    parser.add_argument(\"--n_samples\", type=int, default=128,\n                        help=\"Number of calibration samples\")\n    parser.add_argument(\"--n_gqa_groups\", type=int, default=4,\n                        help=\"Number of original GQA groups (KV heads) per layer\")\n    parser.add_argument(\"--n_mlp_groups\", type=int, default=28,\n                        help=\"Number of original MLP channel groups per layer\")\n    parser.add_argument(\"--output_dir\", default=\"results/analysis/\",\n                        help=\"Output directory\")\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--dtype\", type=str, default=\"bfloat16\",\n                        choices=[\"float16\", \"bfloat16\", \"float32\"])\n    args = parser.parse_args()\n\n    set_seed(args.seed)\n    device = torch.device(\"cuda\" if torch.cuda.is_available() else \"cpu\")\n    torch_dtype = {\"float16\": torch.float16, \"bfloat16\": torch.bfloat16,\n                   \"float32\": torch.float32}[args.dtype]\n\n    logger.info(\"Loading CKA scores...\")\n    cka_data = torch.load(args.cka_scores_path, map_location=\"cpu\", weights_only=True)\n    for key in (\"attn_cka_matrix\", \"mlp_cka_matrix\"):\n        if key not in cka_data:\n            raise ValueError(f\"CKA scores missing '{key}'. Re-run cka_overlap.py.\")\n\n    logger.info(\"Loading pruning metadata...\")\n    pruning_meta = torch.load(args.pruning_mask_path, map_location=\"cpu\",\n                              weights_only=True)\n    attn_keep_masks = pruning_meta[\"attn_keep_masks\"]\n    mlp_keep_masks = pruning_meta[\"mlp_keep_masks\"]\n\n    tokenizer = AutoTokenizer.from_pretrained(args.base_model_path, trust_remote_code=True)\n    calibration_data = load_calibration_data(tokenizer, args.n_samples, seed=args.seed)\n    logger.info(f\"Loaded {len(calibration_data)} calibration samples\")\n\n    # --- Pruned model ---\n    logger.info(f\"Loading pruned model from {args.pruned_model_path}\")\n    pruned_model = load_pruned_model(\n        args.base_model_path, args.pruned_model_path, pruning_meta, torch_dtype, device\n    )\n    logger.info(\"Collecting activations from pruned model...\")\n    pruned_attn_acts, pruned_mlp_acts = collect_all_activations(\n        pruned_model, calibration_data, attn_keep_masks, mlp_keep_masks, device\n    )\n    del pruned_model\n    torch.cuda.empty_cache()\n\n    # --- Recovered model ---\n    logger.info(f\"Loading recovered model from {args.recovered_model_path}\")\n    recovered_model = load_pruned_model(\n        args.base_model_path, args.recovered_model_path, pruning_meta, torch_dtype, device\n    )\n    logger.info(\"Collecting activations from recovered model...\")\n    recovered_attn_acts, recovered_mlp_acts = collect_all_activations(\n        recovered_model, calibration_data, attn_keep_masks, mlp_keep_masks, device\n    )\n    del recovered_model\n    torch.cuda.empty_cache()\n\n    # --- Attention recoverability ---\n    logger.info(\"Computing attention recoverability...\")\n    attn_results = compute_attn_recoverability(\n        pruned_attn_acts, recovered_attn_acts, cka_data,\n        attn_keep_masks, args.n_gqa_groups,\n    )\n    del pruned_attn_acts, recovered_attn_acts\n    logger.info(f\"Computed recoverability for {len(attn_results)} pruned GQA groups\")\n\n    # --- MLP recoverability ---\n    logger.info(\"Computing MLP recoverability...\")\n    mlp_results = compute_mlp_recoverability(\n        pruned_mlp_acts, recovered_mlp_acts, cka_data,\n        mlp_keep_masks, args.n_mlp_groups,\n    )\n    del pruned_mlp_acts, recovered_mlp_acts\n    logger.info(f\"Computed recoverability for {len(mlp_results)} pruned MLP groups\")\n\n    # --- Statistics ---\n    attn_fh = [r[\"cka_overlap\"] for r in attn_results]\n    attn_rec = [r[\"recoverability\"] for r in attn_results]\n    attn_stats = compute_correlation_stats(attn_fh, attn_rec, seed=args.seed)\n\n    mlp_fh = [r[\"cka_overlap\"] for r in mlp_results]\n    mlp_rec = [r[\"recoverability\"] for r in mlp_results]\n    mlp_stats = compute_correlation_stats(mlp_fh, mlp_rec, seed=args.seed)\n\n    combined_results = attn_results + mlp_results\n    combined_fh = [r[\"cka_overlap\"] for r in combined_results]\n    combined_rec = [r[\"recoverability\"] for r in combined_results]\n    combined_stats = compute_correlation_stats(combined_fh, combined_rec, seed=args.seed)\n    combined_stats[\"n_total_pruned\"] = len(combined_results)\n\n    combined_rho = combined_stats[\"spearman_rho\"]\n    verdict = \"PASS\" if combined_rho >= 0.4 else (\n        \"WARNING\" if combined_rho >= 0.3 else \"FAIL\")\n\n    # --- Save results ---\n    os.makedirs(args.output_dir, exist_ok=True)\n\n    output = {\n        \"attention\": {**attn_stats, \"per_group_data\": attn_results},\n        \"mlp\": {**mlp_stats, \"per_group_data\": mlp_results},\n        \"combined\": combined_stats,\n        \"mvp_verdict\": verdict,\n    }\n    json_path = os.path.join(args.output_dir, \"correlation_results.json\")\n    with open(json_path, \"w\") as f:\n        json.dump(output, f, indent=2)\n    logger.info(f\"Results saved to {json_path}\")\n\n    # --- Scatter plots ---\n    if attn_results:\n        make_scatter_plot(\n            attn_results, attn_stats,\n            os.path.join(args.output_dir, \"fh_vs_recoverability_attention.png\"),\n            title_prefix=\"Attention: \",\n        )\n    if mlp_results:\n        make_scatter_plot(\n            mlp_results, mlp_stats,\n            os.path.join(args.output_dir, \"fh_vs_recoverability_mlp.png\"),\n            title_prefix=\"MLP: \",\n        )\n    if combined_results:\n        make_scatter_plot(\n            combined_results, combined_stats,\n            os.path.join(args.output_dir, \"fh_vs_recoverability_combined.png\"),\n            title_prefix=\"Combined: \",\n            color_by_type=True,\n        )\n\n    # --- Summary ---\n    print(f\"\\n{'='*60}\")\n    print(\"Correlation Analysis Results (Attention + MLP)\")\n    print(f\"{'='*60}\")\n    if attn_results:\n        print(f\"  ATTENTION: rho={attn_stats['spearman_rho']:.4f}, \"\n              f\"p={attn_stats['p_value']:.2e}, N={len(attn_results)}\")\n    else:\n        print(\"  ATTENTION: no pruned groups\")\n    if mlp_results:\n        print(f\"  MLP:       rho={mlp_stats['spearman_rho']:.4f}, \"\n              f\"p={mlp_stats['p_value']:.2e}, N={len(mlp_results)}\")\n    else:\n        print(\"  MLP:       no pruned groups\")\n    print(f\"  COMBINED:  rho={combined_rho:.4f}, \"\n          f\"p={combined_stats['p_value']:.2e}, N={len(combined_results)}\")\n    print(f\"  95% CI:    [{combined_stats['bootstrap_ci_95'][0]:.4f}, \"\n          f\"{combined_stats['bootstrap_ci_95'][1]:.4f}]\")\n    print(f\"  MVP Verdict: {verdict}\")\n    print(f\"{'='*60}\")\n\n\nif __name__ == \"__main__\":\n    main()\nFILEEOF\necho \"WRITE_OK: $?\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_mlp-correlation-extend_20260514T052804",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westb-23072",
    "command": "cat > /root/recovery_aware_struct_prune/src/correlation_analysis.py << 'FILEEOF'\n\"\"\"\nCorrelation Analysis: rho(CKA overlap, RLVR recoverability).\n\nTests the hypothesis: pruned structures (GQA groups or MLP channel groups) with\nhigher CKA overlap F(g) are more effectively compensated by RLVR through their\nmost similar retained structure.\n\nMetric: for each pruned structure g_p, find the most CKA-similar retained\nstructure g_r, then measure g_r's activation shift between pruned and\nRLVR-recovered models.\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nimport random\n\nimport numpy as np\nimport scipy.stats as stats\nimport torch\nimport torch.nn.functional as F\nfrom datasets import load_dataset\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n)\nlogger = logging.getLogger(__name__)\n\n\ndef set_seed(seed: int):\n    random.seed(seed)\n    np.random.seed(seed)\n    torch.manual_seed(seed)\n    torch.cuda.manual_seed_all(seed)\n\n\ndef load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):\n    ds = load_dataset(\"openai/gsm8k\", \"main\", split=\"train\")\n    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))\n    encodings = []\n    for example in ds:\n        prompt = f\"Question: {example['question']}\\nAnswer: Let me think step by step.\\n\"\n        ids = tokenizer(prompt, return_tensors=\"pt\", truncation=True, max_length=max_length)\n        encodings.append(ids)\n    return encodings\n\n\ndef load_pruned_model(base_model_path, saved_model_path, pruning_meta, torch_dtype, device):\n    logging.getLogger(\"prune\").setLevel(logging.WARNING)\n    from prune import prune_attention_heads, prune_mlp_channels\n\n    model = AutoModelForCausalLM.from_pretrained(\n        base_model_path, torch_dtype=torch_dtype, device_map=\"cpu\", trust_remote_code=True\n    )\n    prune_attention_heads(model, pruning_meta[\"attn_keep_masks\"])\n    prune_mlp_channels(model, pruning_meta[\"mlp_keep_masks\"])\n\n    safetensor_files = sorted(\n        [f for f in os.listdir(saved_model_path) if f.endswith(\".safetensors\")]\n    )\n    if safetensor_files:\n        from safetensors.torch import load_file\n        state_dict = {}\n        for f in safetensor_files:\n            state_dict.update(load_file(os.path.join(saved_model_path, f)))\n    else:\n        state_dict = torch.load(\n            os.path.join(saved_model_path, \"pytorch_model.bin\"),\n            map_location=\"cpu\", weights_only=True,\n        )\n\n    model.load_state_dict(state_dict)\n    model.to(device)\n    return model\n\n\ndef collect_all_activations(model, calibration_data, attn_keep_masks, mlp_keep_masks, device):\n    \"\"\"Collect both GQA-group and MLP-group activations in a single forward pass.\n\n    Returns:\n        attn_acts: dict[layer_idx] -> tensor[n_samples, n_retained_gqa, heads_per_kv * head_dim]\n        mlp_acts:  dict[layer_idx] -> tensor[n_samples, n_retained_mlp, group_size]\n    \"\"\"\n    config = model.config\n    n_layers = config.num_hidden_layers\n    n_heads = config.num_attention_heads\n    n_kv_heads = config.num_key_value_heads\n    head_dim = config.hidden_size // n_heads\n    heads_per_kv = n_heads // n_kv_heads\n\n    q_outputs = {i: [] for i in range(n_layers)}\n    gate_outputs = {i: [] for i in range(n_layers)}\n    hooks = []\n\n    def make_q_hook(layer_idx):\n        def fn(module, inp, out):\n            q_outputs[layer_idx].append(out.detach().cpu())\n        return fn\n\n    def make_gate_hook(layer_idx):\n        def fn(module, inp, out):\n            gate_outputs[layer_idx].append(out.detach().cpu())\n        return fn\n\n    for i in range(n_layers):\n        h1 = model.model.layers[i].self_attn.q_proj.register_forward_hook(make_q_hook(i))\n        h2 = model.model.layers[i].mlp.gate_proj.register_forward_hook(make_gate_hook(i))\n        hooks.extend([h1, h2])\n\n    model.eval()\n    with torch.no_grad():\n        for idx, enc in enumerate(calibration_data):\n            input_ids = enc[\"input_ids\"].to(device)\n            attention_mask = enc[\"attention_mask\"].to(device)\n            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)\n            if (idx + 1) % 50 == 0:\n                logger.info(f\"  Processed {idx + 1}/{len(calibration_data)} samples\")\n\n    for h in hooks:\n        h.remove()\n\n    attn_activations = {}\n    for layer_idx in range(n_layers):\n        n_retained_gqa = len(attn_keep_masks[layer_idx])\n        per_group = []\n        for t in q_outputs[layer_idx]:\n            t = t.squeeze(0)  # [seq, n_retained_gqa * heads_per_kv * head_dim]\n            t = t.view(t.shape[0], n_retained_gqa, heads_per_kv, head_dim)\n            t = t.view(t.shape[0], n_retained_gqa, heads_per_kv * head_dim)\n            t = t.mean(dim=0)  # [n_retained_gqa, heads_per_kv * head_dim]\n            per_group.append(t)\n        attn_activations[layer_idx] = torch.stack(per_group, dim=0).float()\n        q_outputs[layer_idx] = None\n\n    mlp_activations = {}\n    for layer_idx in range(n_layers):\n        n_retained = len(mlp_keep_masks[layer_idx])\n        per_group = []\n        for t in gate_outputs[layer_idx]:\n            t = t.squeeze(0)  # [seq, n_retained * group_size]\n            total_channels = t.shape[-1]\n            group_size = total_channels // n_retained\n            usable = n_retained * group_size\n            t = t[:, :usable].view(t.shape[0], n_retained, group_size)\n            t = t.mean(dim=0)  # [n_retained, group_size]\n            per_group.append(t)\n        mlp_activations[layer_idx] = torch.stack(per_group, dim=0).float()\n        gate_outputs[layer_idx] = None\n\n    return attn_activations, mlp_activations\n\n\ndef compute_attn_recoverability(pruned_acts, recovered_acts, cka_data, attn_keep_masks,\n                                n_gqa_groups_original):\n    attn_overlap = cka_data[\"attn_overlap\"]\n    attn_cka_matrix = cka_data[\"attn_cka_matrix\"]\n    results = []\n\n    for layer_idx in sorted(attn_keep_masks.keys()):\n        retained = attn_keep_masks[layer_idx]\n        pruned_groups = sorted(set(range(n_gqa_groups_original)) - set(retained))\n        if not pruned_groups:\n            continue\n\n        cka_matrix = attn_cka_matrix[layer_idx]\n\n        for g_p in pruned_groups:\n            sims = torch.tensor([cka_matrix[g_p, g_r].item() for g_r in retained])\n            best_idx = sims.argmax().item()\n            g_r = retained[best_idx]\n            g_r_local = retained.index(g_r)\n\n            act_p = pruned_acts[layer_idx][:, g_r_local, :]\n            act_r = recovered_acts[layer_idx][:, g_r_local, :]\n            cos_sim = F.cosine_similarity(act_p, act_r, dim=-1)\n            activation_shift = 1.0 - cos_sim.mean().item()\n\n            results.append({\n                \"layer\": layer_idx,\n                \"type\": \"attention\",\n                \"pruned_group\": g_p,\n                \"best_retained_group\": g_r,\n                \"cka_overlap\": attn_overlap[layer_idx][g_p].item(),\n                \"recoverability\": activation_shift,\n                \"cka_similarity_to_retained\": sims[best_idx].item(),\n            })\n\n    return results\n\n\ndef compute_mlp_recoverability(pruned_acts, recovered_acts, cka_data, mlp_keep_masks,\n                               n_mlp_groups_original):\n    mlp_overlap = cka_data[\"mlp_overlap\"]\n    mlp_cka_matrix = cka_data[\"mlp_cka_matrix\"]\n    results = []\n\n    for layer_idx in sorted(mlp_keep_masks.keys()):\n        retained = mlp_keep_masks[layer_idx]\n        pruned_groups = sorted(set(range(n_mlp_groups_original)) - set(retained))\n        if not pruned_groups:\n            continue\n\n        cka_matrix = mlp_cka_matrix[layer_idx]\n\n        for m_p in pruned_groups:\n            sims = torch.tensor([cka_matrix[m_p, m_r].item() for m_r in retained])\n            best_idx = sims.argmax().item()\n            m_r = retained[best_idx]\n            m_r_local = retained.index(m_r)\n\n            act_p = pruned_acts[layer_idx][:, m_r_local, :]\n            act_r = recovered_acts[layer_idx][:, m_r_local, :]\n            cos_sim = F.cosine_similarity(act_p, act_r, dim=-1)\n            activation_shift = 1.0 - cos_sim.mean().item()\n\n            results.append({\n                \"layer\": layer_idx,\n                \"type\": \"mlp\",\n                \"pruned_group\": m_p,\n                \"best_retained_group\": m_r,\n                \"cka_overlap\": mlp_overlap[layer_idx][m_p].item(),\n                \"recoverability\": activation_shift,\n                \"cka_similarity_to_retained\": sims[best_idx].item(),\n            })\n\n    return results\n\n\ndef bootstrap_spearman(x, y, n_bootstrap=10000, seed=42):\n    rng = np.random.RandomState(seed)\n    x, y = np.array(x), np.array(y)\n    n = len(x)\n    rhos = []\n    for _ in range(n_bootstrap):\n        idx = rng.choice(n, n, replace=True)\n        r, _ = stats.spearmanr(x[idx], y[idx])\n        if not np.isnan(r):\n            rhos.append(r)\n    return np.percentile(rhos, [2.5, 97.5]).tolist()\n\n\ndef permutation_test(x, y, n_perm=10000, seed=42):\n    rng = np.random.RandomState(seed)\n    x, y = np.array(x), np.array(y)\n    observed, _ = stats.spearmanr(x, y)\n    count = 0\n    for _ in range(n_perm):\n        r, _ = stats.spearmanr(x, rng.permutation(y))\n        if abs(r) >= abs(observed):\n            count += 1\n    return count / n_perm\n\n\ndef compute_correlation_stats(fh, rec, seed=42):\n    if len(fh) < 3:\n        return {\n            \"spearman_rho\": float(\"nan\"), \"p_value\": float(\"nan\"),\n            \"bootstrap_ci_95\": [float(\"nan\"), float(\"nan\")],\n            \"permutation_p_value\": float(\"nan\"),\n            \"n_pruned_groups\": len(fh),\n        }\n    rho, p_value = stats.spearmanr(fh, rec)\n    ci = bootstrap_spearman(fh, rec, seed=seed)\n    perm_p = permutation_test(fh, rec, seed=seed)\n    return {\n        \"spearman_rho\": rho, \"p_value\": p_value,\n        \"bootstrap_ci_95\": ci, \"permutation_p_value\": perm_p,\n        \"n_pruned_groups\": len(fh),\n    }\n\n\ndef make_scatter_plot(results, stat, output_path, title_prefix=\"\", color_by_type=False):\n    try:\n        import matplotlib\n        matplotlib.use(\"Agg\")\n        import matplotlib.pyplot as plt\n    except ImportError:\n        logger.warning(\"matplotlib not available, skipping scatter plot\")\n        return\n\n    fh = [r[\"cka_overlap\"] for r in results]\n    rec = [r[\"recoverability\"] for r in results]\n    rho = stat[\"spearman_rho\"]\n    p_value = stat[\"p_value\"]\n    ci = stat[\"bootstrap_ci_95\"]\n    perm_p = stat.get(\"permutation_p_value\", float(\"nan\"))\n\n    fig, ax = plt.subplots(figsize=(8, 6))\n\n    if color_by_type:\n        type_colors = {\"attention\": \"#1f77b4\", \"mlp\": \"#ff7f0e\"}\n        for stype, color in type_colors.items():\n            mask = [r[\"type\"] == stype for r in results]\n            x = [f for f, m in zip(fh, mask) if m]\n            y = [r for r, m in zip(rec, mask) if m]\n            if x:\n                ax.scatter(x, y, c=color, alpha=0.7, edgecolors=\"k\",\n                           linewidths=0.3, s=30, label=stype)\n        ax.legend()\n    else:\n        layers = [r[\"layer\"] for r in results]\n        sc = ax.scatter(fh, rec, c=layers, cmap=\"viridis\", alpha=0.7,\n                        edgecolors=\"k\", linewidths=0.3, s=30)\n        plt.colorbar(sc, ax=ax, label=\"Layer index\")\n\n    ax.set_xlabel(\"F(g) — CKA overlap of pruned structure\")\n    ax.set_ylabel(\"Recoverability — activation shift of best retained structure\")\n\n    verdict = \"PASS\" if rho >= 0.4 else (\"WARNING\" if rho >= 0.3 else \"FAIL\")\n    ax.set_title(\n        f\"{title_prefix}CKA Overlap vs RLVR Recoverability\\n\"\n        f\"ρ={rho:.3f}, 95% CI=[{ci[0]:.3f}, {ci[1]:.3f}], \"\n        f\"p={p_value:.1e}, perm_p={perm_p:.1e} — {verdict}\"\n    )\n    plt.tight_layout()\n    plt.savefig(output_path, dpi=150, bbox_inches=\"tight\")\n    plt.close()\n    logger.info(f\"Scatter plot saved to {output_path}\")\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Correlation analysis: rho(CKA overlap, RLVR recoverability) \"\n                    \"for attention GQA groups and MLP channel groups\"\n    )\n    parser.add_argument(\"--base_model_path\", required=True,\n                        help=\"Path to original unpruned model\")\n    parser.add_argument(\"--pruned_model_path\", required=True,\n                        help=\"Path to pruned model (before RLVR)\")\n    parser.add_argument(\"--recovered_model_path\", required=True,\n                        help=\"Path to RLVR-recovered model\")\n    parser.add_argument(\"--cka_scores_path\", required=True,\n                        help=\"Path to CKA overlap .pt file\")\n    parser.add_argument(\"--pruning_mask_path\", required=True,\n                        help=\"Path to pruning_metadata.pt\")\n    parser.add_argument(\"--n_samples\", type=int, default=128,\n                        help=\"Number of calibration samples\")\n    parser.add_argument(\"--n_gqa_groups\", type=int, default=4,\n                        help=\"Number of original GQA groups (KV heads) per layer\")\n    parser.add_argument(\"--n_mlp_groups\", type=int, default=28,\n                        help=\"Number of original MLP channel groups per layer\")\n    parser.add_argument(\"--output_dir\", default=\"results/analysis/\",\n                        help=\"Output directory\")\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--dtype\", type=str, default=\"bfloat16\",\n                        choices=[\"float16\", \"bfloat16\", \"float32\"])\n    args = parser.parse_args()\n\n    set_seed(args.seed)\n    device = torch.device(\"cuda\" if torch.cuda.is_available() else \"cpu\")\n    torch_dtype = {\"float16\": torch.float16, \"bfloat16\": torch.bfloat16,\n                   \"float32\": torch.float32}[args.dtype]\n\n    logger.info(\"Loading CKA scores...\")\n    cka_data = torch.load(args.cka_scores_path, map_location=\"cpu\", weights_only=True)\n    for key in (\"attn_cka_matrix\", \"mlp_cka_matrix\"):\n        if key not in cka_data:\n            raise ValueError(f\"CKA scores missing '{key}'. Re-run cka_overlap.py.\")\n\n    logger.info(\"Loading pruning metadata...\")\n    pruning_meta = torch.load(args.pruning_mask_path, map_location=\"cpu\",\n                              weights_only=True)\n    attn_keep_masks = pruning_meta[\"attn_keep_masks\"]\n    mlp_keep_masks = pruning_meta[\"mlp_keep_masks\"]\n\n    tokenizer = AutoTokenizer.from_pretrained(args.base_model_path, trust_remote_code=True)\n    calibration_data = load_calibration_data(tokenizer, args.n_samples, seed=args.seed)\n    logger.info(f\"Loaded {len(calibration_data)} calibration samples\")\n\n    # --- Pruned model ---\n    logger.info(f\"Loading pruned model from {args.pruned_model_path}\")\n    pruned_model = load_pruned_model(\n        args.base_model_path, args.pruned_model_path, pruning_meta, torch_dtype, device\n    )\n    logger.info(\"Collecting activations from pruned model...\")\n    pruned_attn_acts, pruned_mlp_acts = collect_all_activations(\n        pruned_model, calibration_data, attn_keep_masks, mlp_keep_masks, device\n    )\n    del pruned_model\n    torch.cuda.empty_cache()\n\n    # --- Recovered model ---\n    logger.info(f\"Loading recovered model from {args.recovered_model_path}\")\n    recovered_model = load_pruned_model(\n        args.base_model_path, args.recovered_model_path, pruning_meta, torch_dtype, device\n    )\n    logger.info(\"Collecting activations from recovered model...\")\n    recovered_attn_acts, recovered_mlp_acts = collect_all_activations(\n        recovered_model, calibration_data, attn_keep_masks, mlp_keep_masks, device\n    )\n    del recovered_model\n    torch.cuda.empty_cache()\n\n    # --- Attention recoverability ---\n    logger.info(\"Computing attention recoverability...\")\n    attn_results = compute_attn_recoverability(\n        pruned_attn_acts, recovered_attn_acts, cka_data,\n        attn_keep_masks, args.n_gqa_groups,\n    )\n    del pruned_attn_acts, recovered_attn_acts\n    logger.info(f\"Computed recoverability for {len(attn_results)} pruned GQA groups\")\n\n    # --- MLP recoverability ---\n    logger.info(\"Computing MLP recoverability...\")\n    mlp_results = compute_mlp_recoverability(\n        pruned_mlp_acts, recovered_mlp_acts, cka_data,\n        mlp_keep_masks, args.n_mlp_groups,\n    )\n    del pruned_mlp_acts, recovered_mlp_acts\n    logger.info(f\"Computed recoverability for {len(mlp_results)} pruned MLP groups\")\n\n    # --- Statistics ---\n    attn_fh = [r[\"cka_overlap\"] for r in attn_results]\n    attn_rec = [r[\"recoverability\"] for r in attn_results]\n    attn_stats = compute_correlation_stats(attn_fh, attn_rec, seed=args.seed)\n\n    mlp_fh = [r[\"cka_overlap\"] for r in mlp_results]\n    mlp_rec = [r[\"recoverability\"] for r in mlp_results]\n    mlp_stats = compute_correlation_stats(mlp_fh, mlp_rec, seed=args.seed)\n\n    combined_results = attn_results + mlp_results\n    combined_fh = [r[\"cka_overlap\"] for r in combined_results]\n    combined_rec = [r[\"recoverability\"] for r in combined_results]\n    combined_stats = compute_correlation_stats(combined_fh, combined_rec, seed=args.seed)\n    combined_stats[\"n_total_pruned\"] = len(combined_results)\n\n    combined_rho = combined_stats[\"spearman_rho\"]\n    verdict = \"PASS\" if combined_rho >= 0.4 else (\n        \"WARNING\" if combined_rho >= 0.3 else \"FAIL\")\n\n    # --- Save results ---\n    os.makedirs(args.output_dir, exist_ok=True)\n\n    output = {\n        \"attention\": {**attn_stats, \"per_group_data\": attn_results},\n        \"mlp\": {**mlp_stats, \"per_group_data\": mlp_results},\n        \"combined\": combined_stats,\n        \"mvp_verdict\": verdict,\n    }\n    json_path = os.path.join(args.output_dir, \"correlation_results.json\")\n    with open(json_path, \"w\") as f:\n        json.dump(output, f, indent=2)\n    logger.info(f\"Results saved to {json_path}\")\n\n    # --- Scatter plots ---\n    if attn_results:\n        make_scatter_plot(\n            attn_results, attn_stats,\n            os.path.join(args.output_dir, \"fh_vs_recoverability_attention.png\"),\n            title_prefix=\"Attention: \",\n        )\n    if mlp_results:\n        make_scatter_plot(\n            mlp_results, mlp_stats,\n            os.path.join(args.output_dir, \"fh_vs_recoverability_mlp.png\"),\n            title_prefix=\"MLP: \",\n        )\n    if combined_results:\n        make_scatter_plot(\n            combined_results, combined_stats,\n            os.path.join(args.output_dir, \"fh_vs_recoverability_combined.png\"),\n            title_prefix=\"Combined: \",\n            color_by_type=True,\n        )\n\n    # --- Summary ---\n    print(f\"\\n{'='*60}\")\n    print(\"Correlation Analysis Results (Attention + MLP)\")\n    print(f\"{'='*60}\")\n    if attn_results:\n        print(f\"  ATTENTION: rho={attn_stats['spearman_rho']:.4f}, \"\n              f\"p={attn_stats['p_value']:.2e}, N={len(attn_results)}\")\n    else:\n        print(\"  ATTENTION: no pruned groups\")\n    if mlp_results:\n        print(f\"  MLP:       rho={mlp_stats['spearman_rho']:.4f}, \"\n              f\"p={mlp_stats['p_value']:.2e}, N={len(mlp_results)}\")\n    else:\n        print(\"  MLP:       no pruned groups\")\n    print(f\"  COMBINED:  rho={combined_rho:.4f}, \"\n          f\"p={combined_stats['p_value']:.2e}, N={len(combined_results)}\")\n    print(f\"  95% CI:    [{combined_stats['bootstrap_ci_95'][0]:.4f}, \"\n          f\"{combined_stats['bootstrap_ci_95'][1]:.4f}]\")\n    print(f\"  MVP Verdict: {verdict}\")\n    print(f\"{'='*60}\")\n\n\nif __name__ == \"__main__\":\n    main()\nFILEEOF\necho \"WRITE_OK: $?\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-14T05:38:16.877208+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"WRITE_OK: 0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.84}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_mlp-correlation-extend_20260514T052804",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-14T05:38:16.877391+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westb-23072",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune/src && python3 correlation_analysis.py --help",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_mlp-correlation-extend_20260514T052804",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westb-23072",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune/src && python3 correlation_analysis.py --help",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-14T05:38:16.877548+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"usage: correlation_analysis.py [-h] --base_model_path BASE_MODEL_PATH\\n                               --pruned_model_path PRUNED_MODEL_PATH\\n                               --recovered_model_path RECOVERED_MODEL_PATH\\n                               --cka_scores_path CKA_SCORES_PATH\\n                               --pruning_mask_path PRUNING_MASK_PATH\\n                               [--n_samples N_SAMPLES]\\n                               [--n_gqa_groups N_GQA_GROUPS]\\n                               [--n_mlp_groups N_MLP_GROUPS]\\n                               [--output_dir OUTPUT_DIR] [--seed SEED]\\n                               [--dtype {float16,bfloat16,float32}]\\n\\nCorrelation analysis: rho(CKA overlap, RLVR recoverability) for attention GQA\\ngroups and MLP channel groups\\n\\noptions:\\n  -h, --help            show this help message and exit\\n  --base_model_path BASE_MODEL_PATH\\n                        Path to original unpruned model\\n  --pruned_model_path PRUNED_MODEL_PATH\\n                        Path to pruned model (before RLVR)\\n  --recovered_model_path RECOVERED_MODEL_PATH\\n                        Path to RLVR-recovered model\\n  --cka_scores_path CKA_SCORES_PATH\\n                        Path to CKA overlap .pt file\\n  --pruning_mask_path PRUNING_MASK_PATH\\n                        Path to pruning_metadata.pt\\n  --n_samples N_SAMPLES\\n                        Number of calibration samples\\n  --n_gqa_groups N_GQA_GROUPS\\n                        Number of original GQA groups (KV heads) per layer\\n  --n_mlp_groups N_MLP_GROUPS\\n                        Number of original MLP channel groups per layer\\n  --output_dir OUTPUT_DIR\\n                        Output directory\\n  --seed SEED\\n  --dtype {float16,bfloat16,float32}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.77}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_mlp-correlation-extend_20260514T052804",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-14T05:38:16.877736+00:00_

--help 验证通过。汇报：

### 1. cka_overlap.py — 无需修改
`mlp_cka_matrix` 已存在。输出包含 `attn_overlap`, `mlp_overlap`, `attn_cka_matrix`, `mlp_cka_matrix` 四个 key。

### 2. prune.py — 无需修改
`pruning_metadata.pt` 已包含 `attn_keep_masks` 和 `mlp_keep_masks`。

### 3. correlation_analysis.py — 重写完成

**修复的问题**：
- 旧代码用 `n_heads=28`（Q head 数）做 recoverability 计算，但 CKA matrix 是 `[4, 4]`（GQA group 粒度），会 index out of bounds。改为用 `--n_gqa_groups=4`，与 CKA matrix 和 pruning_metadata 的 GQA group 粒度对齐。

**新增内容**：
- `collect_all_activations()` — 单次 forward pass 同时 hook q_proj + gate_proj，收集 attention GQA group 和 MLP group 两种激活，避免重复推理
- `compute_attn_recoverability()` — GQA group 粒度的 attention recoverability
- `compute_mlp_recoverability()` — MLP group 粒度的 recoverability（hook gate_proj，按 group_size 切分 intermediate channels）
- `compute_correlation_stats()` — 统一的统计计算（Spearman rho + bootstrap CI + permutation test），处理 N<3 的退化情况
- 新增 `--n_gqa_groups`（default=4）和 `--n_mlp_groups`（default=28）参数

### 4. 输出格式
```json
{
  "attention": { "spearman_rho", "p_value", "bootstrap_ci_95", "permutation_p_value", "n_pruned_groups", "per_group_data" },
  "mlp":       { ... 同上 ... },
  "combined":  { ... + "n_total_pruned" },
  "mvp_verdict": "PASS/WARNING/FAIL"  // 基于 combined rho
}
```

Scatter plots：
- `fh_vs_recoverability_attention.png`（按 layer 着色）
- `fh_vs_recoverability_mlp.png`（按 layer 着色）
- `fh_vs_recoverability_combined.png`（按 attention/MLP 类型着色，蓝/橙区分）

### 5. --help 验证通过
新增参数 `--n_gqa_groups`, `--n_mlp_groups` 正确显示。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_fix_mlp-correlation-extend_20260514T052804"
}
```

</details>

---
