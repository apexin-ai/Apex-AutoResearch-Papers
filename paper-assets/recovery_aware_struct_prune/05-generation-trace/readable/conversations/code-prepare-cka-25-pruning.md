# code prepare cka 25 pruning

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 0
- **Tool calls:** 23
- **Original source:** `logs/chats/worker_code_prepare_cka_25_pruning_20260519T033337.jsonl`
- **Structured JSON:** [`baa03f8f3eec20cff7e3.json`](../../sessions/ba/baa03f8f3eec20cff7e3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

47 recorded events

### Tool call

_source line 1 · 2026-05-19T03:35:19.512374+00:00_

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
  "session": "worker_code_prepare_cka_25_pruning_20260519T033337",
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

_source line 2 · 2026-05-19T03:35:19.512718+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_prepare_cka_25_pruning_20260519T033337",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T03:35:19.512899+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29022",
  "command": "ls /root/recovery_aware_struct_prune/src/*prune* /root/recovery_aware_struct_prune/src/*cka* 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_prepare_cka_25_pruning_20260519T033337",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29022",
    "command": "ls /root/recovery_aware_struct_prune/src/*prune* /root/recovery_aware_struct_prune/src/*cka* 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T03:35:19.513055+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_prepare_cka_25_pruning_20260519T033337",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T03:35:19.513191+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29022",
  "command": "grep -r \"cka\\|CKA\" /root/recovery_aware_struct_prune/src/ --include=\"*.py\" -l",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_prepare_cka_25_pruning_20260519T033337",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29022",
    "command": "grep -r \"cka\\|CKA\" /root/recovery_aware_struct_prune/src/ --include=\"*.py\" -l",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T03:35:19.513403+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_prepare_cka_25_pruning_20260519T033337",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T03:35:19.513591+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29022",
  "command": "find /root/recovery_aware_struct_prune/src/ -name \"*prune*\" -o -name \"*cka*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_prepare_cka_25_pruning_20260519T033337",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29022",
    "command": "find /root/recovery_aware_struct_prune/src/ -name \"*prune*\" -o -name \"*cka*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-19T03:35:19.513795+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29022",
  "command": "grep -rl \"cka\" /root/recovery_aware_struct_prune/src/ --include=\"*.py\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_prepare_cka_25_pruning_20260519T033337",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29022",
    "command": "grep -rl \"cka\" /root/recovery_aware_struct_prune/src/ --include=\"*.py\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-19T03:35:19.514015+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/recovery_aware_struct_prune/src/cka_overlap.py\\n/root/recovery_aware_struct_prune/src/cka_overlap.py.bak\\n/root/recovery_aware_struct_prune/src/extract_cka_for_figures.py\\n/root/recovery_aware_struct_prune/src/plot_cka_figures.py\\n/root/recovery_aware_struct_prune/src/prune.py\\n/root/recovery_aware_struct_prune/src/prune.py.bak\\n/root/recovery_aware_struct_prune/src/run_cka_reliability.py\\n/root/recovery_aware_struct_prune/src/run_grasp_prune.sh\\n/root/recovery_aware_struct_prune/src/prune_unstructured.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.04}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_prepare_cka_25_pruning_20260519T033337",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T03:35:19.514225+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/recovery_aware_struct_prune/src/cka_overlap.py\\n/root/recovery_aware_struct_prune/src/correlation_analysis.py\\n/root/recovery_aware_struct_prune/src/extract_cka_for_figures.py\\n/root/recovery_aware_struct_prune/src/plot_cka_figures.py\\n/root/recovery_aware_struct_prune/src/prune.py\\n/root/recovery_aware_struct_prune/src/rasp_scoring.py\\n/root/recovery_aware_struct_prune/src/run_cka_reliability.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_prepare_cka_25_pruning_20260519T033337",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T03:35:19.514487+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29022",
  "command": "head -150 /root/recovery_aware_struct_prune/src/prune.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_prepare_cka_25_pruning_20260519T033337",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29022",
    "command": "head -150 /root/recovery_aware_struct_prune/src/prune.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T03:35:19.514800+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nStructured Pruning for Qwen2.5 architecture (GQA-group granularity).\\n\\nRemoves GQA groups (7 Q heads + 1 KV head each) and MLP channel groups\\nbased on RASP or standard importance scores.\\n\\nInput:  pretrained model + pruning scores\\nOutput: pruned model saved to disk\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport copy\\nimport logging\\nimport os\\nimport random\\n\\nimport numpy as np\\nimport torch\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n)\\nlogger = logging.getLogger(__name__)\\n\\n\\ndef set_seed(seed: int):\\n    random.seed(seed)\\n    np.random.seed(seed)\\n    torch.manual_seed(seed)\\n    torch.cuda.manual_seed_all(seed)\\n\\n\\ndef prune_attention_heads(model, attn_keep_masks: dict):\\n    \\\"\\\"\\\"Prune GQA groups from the model by slicing weight matrices in-place.\\n\\n    attn_keep_masks: dict[layer_idx -> list of GQA group indices to KEEP]\\n    Each GQA group = heads_per_kv Q heads + 1 KV head.\\n    \\\"\\\"\\\"\\n    config = model.config\\n    n_heads = config.num_attention_heads\\n    n_kv_heads = config.num_key_value_heads\\n    head_dim = config.hidden_size // n_heads\\n    heads_per_kv = n_heads // n_kv_heads\\n\\n    total_pruned_groups = 0\\n\\n    for layer_idx, keep_groups in attn_keep_masks.items():\\n        layer = model.model.layers[layer_idx]\\n        attn = layer.self_attn\\n        n_keep_groups = len(keep_groups)\\n        pruned_groups = n_kv_heads - n_keep_groups\\n\\n        # Expand GQA group indices to Q head weight indices\\n        q_indices = []\\n        for g in keep_groups:\\n            for qh in range(heads_per_kv):\\n                h = g * heads_per_kv + qh\\n                start = h * head_dim\\n                q_indices.extend(range(start, start + head_dim))\\n        q_indices = torch.tensor(q_indi
…[truncated 4110 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_prepare_cka_25_pruning_20260519T033337",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T03:35:19.515038+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29022",
  "command": "find /root/recovery_aware_struct_prune/ -name \"*.sh\" -path \"*/src/*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_prepare_cka_25_pruning_20260519T033337",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29022",
    "command": "find /root/recovery_aware_struct_prune/ -name \"*.sh\" -path \"*/src/*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T03:35:19.515247+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/recovery_aware_struct_prune/src/run_alpha_ablation.sh\\n/root/recovery_aware_struct_prune/src/run_alpha_ablation_full.sh\\n/root/recovery_aware_struct_prune/src/run_eval_25.sh\\n/root/recovery_aware_struct_prune/src/run_full_eval.sh\\n/root/recovery_aware_struct_prune/src/run_full_eval_all.sh\\n/root/recovery_aware_struct_prune/src/run_full_eval_d008.sh\\n/root/recovery_aware_struct_prune/src/run_full_eval_d008_parallel.sh\\n/root/recovery_aware_struct_prune/src/run_grasp_prune.sh\\n/root/recovery_aware_struct_prune/src/run_graspune.sh\\n/root/recovery_aware_struct_prune/src/run_grpo_multiseed.sh\\n/root/recovery_aware_struct_prune/src/run_grpo_stage2.sh\\n/root/recovery_aware_struct_prune/src/run_grpo_v4.sh\\n/root/recovery_aware_struct_prune/src/run_multi_seed_rasp.sh\\n/root/recovery_aware_struct_prune/src/run_mvp.sh\\n/root/recovery_aware_struct_prune/src/run_mvp_resume.sh\\n/root/recovery_aware_struct_prune/src/run_mvp_resume_from_3_5.sh\\n/root/recovery_aware_struct_prune/src/run_post_recovery_eval.sh\\n/root/recovery_aware_struct_prune/src/run_sft_eval.sh\\n/root/recovery_aware_struct_prune/src/run_sft_warmup.sh\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_prepare_cka_25_pruning_20260519T033337",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T03:35:19.515480+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29022",
  "command": "wc -l /root/recovery_aware_struct_prune/src/prune.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_prepare_cka_25_pruning_20260519T033337",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29022",
    "command": "wc -l /root/recovery_aware_struct_prune/src/prune.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T03:35:19.515664+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"458 /root/recovery_aware_struct_prune/src/prune.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_prepare_cka_25_pruning_20260519T033337",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T03:35:19.515837+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29022",
  "command": "tail -n +150 /root/recovery_aware_struct_prune/src/prune.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_prepare_cka_25_pruning_20260519T033337",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29022",
    "command": "tail -n +150 /root/recovery_aware_struct_prune/src/prune.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T03:35:19.516230+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"        )\\n\\n    logger.info(f\\\"Total MLP pruning: {total_pruned} groups removed\\\")\\n\\n\\ndef count_parameters(model) -> int:\\n    return sum(p.numel() for p in model.parameters())\\n\\n\\ndef main():\\n    parser = argparse.ArgumentParser(description=\\\"Execute structured pruning on Qwen2.5 model (GQA-group granularity)\\\")\\n    parser.add_argument(\\\"--model_path\\\", type=str, required=True, help=\\\"Path to pretrained model\\\")\\n    parser.add_argument(\\\"--importance_path\\\", type=str, default=None, help=\\\"Path to importance scores .pt\\\")\\n    parser.add_argument(\\\"--cka_path\\\", type=str, default=None, help=\\\"Path to CKA overlap scores .pt\\\")\\n    parser.add_argument(\\\"--mode\\\", type=str, choices=[\\\"standard\\\", \\\"rasp\\\", \\\"rasp-rlvr\\\", \\\"cka_only\\\", \\\"random\\\"], required=True)\\n    parser.add_argument(\\\"--sparsity\\\", type=float, default=0.35, help=\\\"Target sparsity ratio\\\")\\n    parser.add_argument(\\\"--alpha\\\", type=float, default=1.0, help=\\\"RASP alpha parameter\\\")\\n    parser.add_argument(\\\"--output_path\\\", type=str, required=True, help=\\\"Output path for pruned model\\\")\\n    parser.add_argument(\\\"--seed\\\", type=int, default=42)\\n    parser.add_argument(\\\"--dtype\\\", type=str, default=\\\"bfloat16\\\", choices=[\\\"float16\\\", \\\"bfloat16\\\", \\\"float32\\\"])\\n    args = parser.parse_args()\\n\\n    set_seed(args.seed)\\n    device = torch.device(\\\"cuda\\\" if torch.cuda.is_available() else \\\"cpu\\\")\\n    dtype_map = {\\\"float16\\\": torch.float16, \\\"bfloat16\\\": torch.bfloat16, \\\"float32\\\": torch.float32}\\n    torch_dtype = dtype_map[args.dtype]\\n\\n    logger.info(f\\\"Loading model from {args.model_path}\\\")\\n    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)\\n    model = AutoModelForCausalLM.from_pretrained(\\n        args.model_path,\\n        torch_dt
…[truncated 7102 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_prepare_cka_25_pruning_20260519T033337",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T03:35:19.516540+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29022",
  "command": "grep -r \"cka_only\" /root/recovery_aware_struct_prune/src/ --include=\"*.sh\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_prepare_cka_25_pruning_20260519T033337",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29022",
    "command": "grep -r \"cka_only\" /root/recovery_aware_struct_prune/src/ --include=\"*.sh\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T03:35:19.516741+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_prepare_cka_25_pruning_20260519T033337",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T03:35:19.516931+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29022",
  "command": "find /root/autodl-tmp/recovery_aware_struct_prune/ -name \"*cka*\" -type d",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_prepare_cka_25_pruning_20260519T033337",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29022",
    "command": "find /root/autodl-tmp/recovery_aware_struct_prune/ -name \"*cka*\" -type d",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-19T03:35:19.517113+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20\\n/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20\\n/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_extended_300\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_prepare_cka_25_pruning_20260519T033337",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-19T03:35:19.517324+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29022",
  "command": "find /root/autodl-tmp/recovery_aware_struct_prune/ -name \"*cka*overlap*\" -o -name \"*cka*scores*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_prepare_cka_25_pruning_20260519T033337",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29022",
    "command": "find /root/autodl-tmp/recovery_aware_struct_prune/ -name \"*cka*overlap*\" -o -name \"*cka*scores*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T03:35:19.517481+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/cka_scores_qwen_math.pt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_prepare_cka_25_pruning_20260519T033337",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-19T03:35:19.517612+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29022",
  "command": "find /root/autodl-tmp/recovery_aware_struct_prune/ -name \"pruned_cka*\" -type d",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_prepare_cka_25_pruning_20260519T033337",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29022",
    "command": "find /root/autodl-tmp/recovery_aware_struct_prune/ -name \"pruned_cka*\" -type d",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-19T03:35:19.517773+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_prepare_cka_25_pruning_20260519T033337",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-19T03:35:19.517911+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29022",
  "command": "grep -r \"cka_only\" /root/recovery_aware_struct_prune/ --include=\"*.sh\" --include=\"*.py\" -l",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_prepare_cka_25_pruning_20260519T033337",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29022",
    "command": "grep -r \"cka_only\" /root/recovery_aware_struct_prune/ --include=\"*.sh\" --include=\"*.py\" -l",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-19T03:35:19.518037+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/recovery_aware_struct_prune/src/prune.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_prepare_cka_25_pruning_20260519T033337",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-19T03:35:19.518175+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29022",
  "command": "grep \"cka_only\" /root/.bash_history",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_prepare_cka_25_pruning_20260519T033337",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29022",
    "command": "grep \"cka_only\" /root/.bash_history",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-19T03:35:19.518331+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"grep: /root/.bash_history: No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_prepare_cka_25_pruning_20260519T033337",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-19T03:35:19.518468+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29022",
  "command": "find /root/autodl-tmp/recovery_aware_struct_prune/ -name \"pruning_metadata.pt\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_prepare_cka_25_pruning_20260519T033337",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29022",
    "command": "find /root/autodl-tmp/recovery_aware_struct_prune/ -name \"pruning_metadata.pt\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-19T03:35:19.518600+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_qwen_math_rasp_20/pruning_metadata.pt\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_qwen_math_standard_20/pruning_metadata.pt\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_25/pruning_metadata.pt\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_25_qwen_math/pruning_metadata.pt\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_rlvr_20_qwen_math/pruning_metadata.pt\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_25/pruning_metadata.pt\\n/root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_25_qwen_math/pruning_metadata.pt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_prepare_cka_25_pruning_20260519T033337",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-19T03:35:19.518740+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29022",
  "command": "ls /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_prepare_cka_25_pruning_20260519T033337",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29022",
    "command": "ls /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-19T03:35:19.518863+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"chat_template.jinja\\nconfig.json\\ngeneration_config.json\\nmodel.safetensors\\ntokenizer.json\\ntokenizer_config.json\\ntraining_args.bin\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_prepare_cka_25_pruning_20260519T033337",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-19T03:35:19.519017+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29022",
  "command": "find /root/autodl-tmp/recovery_aware_struct_prune/ -maxdepth 1 -name \"*cka*\" -type d",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_prepare_cka_25_pruning_20260519T033337",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29022",
    "command": "find /root/autodl-tmp/recovery_aware_struct_prune/ -maxdepth 1 -name \"*cka*\" -type d",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-19T03:35:19.519161+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20\\n/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20\\n/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_extended_300\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_prepare_cka_25_pruning_20260519T033337",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-19T03:35:19.519330+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29022",
  "command": "ls /root/autodl-tmp/recovery_aware_struct_prune/results/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_prepare_cka_25_pruning_20260519T033337",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29022",
    "command": "ls /root/autodl-tmp/recovery_aware_struct_prune/results/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-19T03:35:19.519502+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"artifacts\\nbootstrap_ci_plot.png\\nbootstrap_ci_results.json\\ncka_scores_qwen_math.pt\\neval_grpo_rasp_20_qwen_math.json\\neval_grpo_rasp_20_qwen_math.log\\neval_grpo_rasp_25.log\\neval_grpo_rasp_25_qwen_math.json\\neval_grpo_rasp_25_qwen_math.log\\neval_grpo_rasp_rlvr_20_qwen_math.json\\neval_grpo_standard_20_qwen_math.json\\neval_grpo_standard_20_qwen_math.log\\neval_grpo_standard_25.json\\neval_grpo_standard_25_n1319.json\\neval_grpo_standard_25_qwen_math.json\\neval_grpo_standard_25_qwen_math.log\\neval_grpo_unpruned_v2_step100.json\\neval_grpo_unpruned_v2_step90.json\\neval_gsm8k_standard_300.log\\neval_humaneval_grpo_rasp_20.json\\neval_humaneval_grpo_rasp_20_2048.json\\neval_humaneval_grpo_standard_20.json\\neval_humaneval_grpo_standard_20_2048.json\\neval_humaneval_sft_rasp_20.json\\neval_humaneval_sft_rasp_20_2048.json\\neval_humaneval_sft_standard_20.json\\neval_humaneval_sft_standard_20_2048.json\\neval_humaneval_unpruned.json\\neval_humaneval_unpruned_2048.json\\neval_math500_sft_rasp_20.json\\neval_math500_sft_standard_20.json\\neval_math500_unpruned.json\\neval_math500_v4.log\\neval_pass_k8_rasp_20_grpo_deepseek.json\\neval_pass_k8_rasp_20_grpo_deepseek.log\\neval_pass_k8_rasp_20_grpo_qwen_math.json\\neval_pass_k8_rasp_20_sft_qwen_math.json\\neval_pass_k8_standard_20_grpo_deepseek.json\\neval_pass_k8_standard_20_grpo_qwen_math_v2.json\\neval_pass_k8_unpruned_qwen_math.json\\neval_postprune_rasp_25.json\\neval_postprune_rasp_30.json\\neval_postprune_standard_25.json\\neval_postprune_standard_30.json\\neval_sft_cka_only_20_n1319.json\\neval_sft_grasp_20_greedy.json\\neval_sft_qwen_math_rasp_25.json\\neval_sft_qwen_math_standard_25.json\\neval_sft_rasp_20_seed123.json\\neval_sft_rasp_25.log\\neval_sft_rasp_25_retry.log\\neval_sft_rasp_qwen_math.json\\neval_sft_rasp_qwen_math.log\\neval_sft_rasp_rlvr_20_qwen_math.json\\neval_sft_standard_20_full_westd.json\\neval_sft_standard_20_seed123.json\\neval_
…[truncated 629 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_prepare_cka_25_pruning_20260519T033337",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-19T03:35:19.519676+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29022",
  "command": "ls /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_prepare_cka_25_pruning_20260519T033337",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29022",
    "command": "ls /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-19T03:35:19.519823+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"LICENSE\\nREADME.md\\nconfig.json\\nfigures\\ngeneration_config.json\\nmodel-00001-of-000002.safetensors\\nmodel-00002-of-000002.safetensors\\nmodel.safetensors.index.json\\ntokenizer.json\\ntokenizer_config.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_prepare_cka_25_pruning_20260519T033337",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-19T03:35:19.519966+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-29022",
  "command": "/root/miniconda3/bin/python -c \"import torch; d=torch.load('/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_25_qwen_math/pruning_metadata.pt', map_location='cpu', weights_only=False); print({k:v for k,v in d.items() if k not in ('attn_keep_masks','mlp_keep_masks')})\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_prepare_cka_25_pruning_20260519T033337",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-29022",
    "command": "/root/miniconda3/bin/python -c \"import torch; d=torch.load('/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_25_qwen_math/pruning_metadata.pt', map_location='cpu', weights_only=False); print({k:v for k,v in d.items() if k not in ('attn_keep_masks','mlp_keep_masks')})\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-19T03:35:19.520117+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{'mode': 'rasp', 'sparsity_target': 0.25, 'sparsity_actual': 0.2405090515145939, 'alpha': 1.0, 'original_params': 7615616512, 'pruned_params': 5783991808, 'n_attn_groups_pruned': 0, 'n_mlp_groups_pruned': 252}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.81}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_prepare_cka_25_pruning_20260519T033337",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-19T03:35:19.520420+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-29022",
  "command": "/root/miniconda3/bin/python -c \"import torch; d=torch.load('/root/autodl-tmp/recovery_aware_struct_prune/results/cka_scores_qwen_math.pt', map_location='cpu', weights_only=True); print(list(d.keys())); print('attn layers:', len(d.get('attn_overlap',{}))); print('mlp layers:', len(d.get('mlp_overlap',{})))\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_prepare_cka_25_pruning_20260519T033337",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-29022",
    "command": "/root/miniconda3/bin/python -c \"import torch; d=torch.load('/root/autodl-tmp/recovery_aware_struct_prune/results/cka_scores_qwen_math.pt', map_location='cpu', weights_only=True); print(list(d.keys())); print('attn layers:', len(d.get('attn_overlap',{}))); print('mlp layers:', len(d.get('mlp_overlap',{})))\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-19T03:35:19.520589+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"['attn_overlap', 'mlp_overlap', 'attn_cka_matrix', 'mlp_cka_matrix']\\nattn layers: 28\\nmlp layers: 28\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.82}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_prepare_cka_25_pruning_20260519T033337",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-19T03:35:19.520735+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-29022",
  "command": "cd /root/recovery_aware_struct_prune && /root/miniconda3/bin/python src/prune.py --help",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_prepare_cka_25_pruning_20260519T033337",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-29022",
    "command": "cd /root/recovery_aware_struct_prune && /root/miniconda3/bin/python src/prune.py --help",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-19T03:35:19.520875+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"usage: prune.py [-h] --model_path MODEL_PATH\\n                [--importance_path IMPORTANCE_PATH] [--cka_path CKA_PATH]\\n                --mode {standard,rasp,rasp-rlvr,cka_only,random}\\n                [--sparsity SPARSITY] [--alpha ALPHA] --output_path\\n                OUTPUT_PATH [--seed SEED] [--dtype {float16,bfloat16,float32}]\\n\\nExecute structured pruning on Qwen2.5 model (GQA-group granularity)\\n\\noptions:\\n  -h, --help            show this help message and exit\\n  --model_path MODEL_PATH\\n                        Path to pretrained model\\n  --importance_path IMPORTANCE_PATH\\n                        Path to importance scores .pt\\n  --cka_path CKA_PATH   Path to CKA overlap scores .pt\\n  --mode {standard,rasp,rasp-rlvr,cka_only,random}\\n  --sparsity SPARSITY   Target sparsity ratio\\n  --alpha ALPHA         RASP alpha parameter\\n  --output_path OUTPUT_PATH\\n                        Output path for pruned model\\n  --seed SEED\\n  --dtype {float16,bfloat16,float32}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.6}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_prepare_cka_25_pruning_20260519T033337",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-19T03:35:19.521060+00:00_

所有信息已确认。以下是准备好的命令：

## CKA-only 25% Sparsity Pruning 命令

```bash
cd /root/recovery_aware_struct_prune && \
CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python src/prune.py \
  --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B \
  --cka_path /root/autodl-tmp/recovery_aware_struct_prune/results/cka_scores_qwen_math.pt \
  --mode cka_only \
  --sparsity 0.25 \
  --output_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_25 \
  --seed 42 \
  --dtype bfloat16
```

## 说明

- **`--importance_path` 不需要**：`cka_only` 模式只用 CKA overlap scores（`score = 1 - overlap`），不需要 importance scores
- **CKA scores 已存在**：`cka_scores_qwen_math.pt` 包含 28 层的 attn_overlap 和 mlp_overlap，无需重新计算
- **输出路径**：写入数据盘 `/root/autodl-tmp/`（遵守 C002 约束）
- **GPU 需求**：模型加载到 CPU 做 pruning（代码中 `device_map="cpu"`），仅 forward pass 验证需要少量 GPU。单卡即可，预计 2-3 分钟完成
- **参考**：RASP 25% pruning 实际达到 24.05% sparsity（从 7.6B 剪到 5.8B params），CKA-only 25% 预计类似量级

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_prepare_cka_25_pruning_20260519T033337"
}
```

</details>

---
