# code zeromask ablation prep

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 54
- **Recorded user turns:** 0
- **Tool calls:** 26
- **Original source:** `logs/chats/worker_code_zeromask_ablation_prep_20260525T154421.jsonl`
- **Structured JSON:** [`48078a624a64a941709e.json`](../../sessions/48/48078a624a64a941709e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

54 recorded events

### Assistant

_source line 1 · 2026-05-25T15:44:30.268406+00:00_

You've hit your limit · resets May 26, 6pm (UTC)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-25T15:49:47.013233+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__detect_image,TodoWrite",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__detect_image,TodoWrite",
    "max_results": "10"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-25T15:49:47.013706+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-25T15:49:47.014047+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Read eval_openvla_l2norm_libero.py on westd-38929', 'activeForm': 'Reading eval_openvla_l2norm_libero.py', 'status': 'in_progress'}, {'content': 'Read existing π0.5 zeromask reference for design pattern', 'activeForm': 'Reading π0.5 zeromask reference', 'status': 'pending'}, {'content': 'Write eval_openvla_zeromask_libero.py with --ablation_mode', 'activeForm': 'Writing eval_openvla_zeromask_libero.py', 'status': 'pending'}, {'content': 'Dry-run validate (syntax + argparse)', 'activeForm': 'Dry-running validation', 'status': 'pending'}, {'content': 'Register as artifact', 'activeForm': 'Registering artifact', 'status': 'pending'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Read eval_openvla_l2norm_libero.py on westd-38929', 'activeForm': 'Reading eval_openvla_l2norm_libero.py', 'status': 'in_progress'}, {'content': 'Read existing π0.5 zeromask reference for design pattern', 'activeForm': 'Reading π0.5 zeromask reference', 'status': 'pending'}, {'content': 'Write eval_openvla_zeromask_libero.py with --ablation_mode', 'activeForm': 'Writing eval_openvla_zeromask_libero.py', 'status': 'pending'}, {'content': 'Dry-run validate (syntax + argparse)', 'activeForm': 'Dry-running validation', 'status': 'pending'}, {'content': 'Register as artifact', 'activeForm': 'Registering artifact', 'status': 'pending'}]"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-25T15:49:47.014383+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-25T15:49:47.014614+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-38929",
  "command": "ls /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py /root/autodl-tmp/importance_margin_vla_compress/artifacts/eval_pi05_zeromask_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-38929",
    "command": "ls /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py /root/autodl-tmp/importance_margin_vla_compress/artifacts/eval_pi05_zeromask_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-25T15:49:47.014829+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-38929",
  "command": "wc -l /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-38929",
    "command": "wc -l /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-25T15:49:47.015049+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py\\n\", \"stderr\": \"ls: cannot access '/root/autodl-tmp/importance_margin_vla_compress/artifacts/eval_pi05_zeromask_ablation.py': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 1.3}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-25T15:49:47.015313+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"402 /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-25T15:49:47.015526+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-38929",
  "command": "find /root/autodl-tmp/importance_margin_vla_compress -maxdepth 3 -name \"*zeromask*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-38929",
    "command": "find /root/autodl-tmp/importance_margin_vla_compress -maxdepth 3 -name \"*zeromask*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-25T15:49:47.015758+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-25T15:49:47.015971+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-38929",
  "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-38929",
    "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-25T15:49:47.016459+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nOpenVLA LIBERO Evaluation: Baseline + Random/L2-Norm Token Pruning.\\nUsage:\\n    python eval_openvla_l2norm_libero.py --mode baseline --suite libero_object\\n    python eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.5 --suite libero_object\\n\\\"\\\"\\\"\\nimport argparse, io, json, math, os, sys, time\\nos.environ[\\\"MUJOCO_GL\\\"] = \\\"egl\\\"\\nos.environ.setdefault(\\\"CUDA_VISIBLE_DEVICES\\\", \\\"0\\\")\\nos.environ[\\\"TRANSFORMERS_OFFLINE\\\"] = \\\"1\\\"\\nos.environ[\\\"HF_HUB_OFFLINE\\\"] = \\\"1\\\"\\n\\n# Use transformers 4.40.1 for OpenVLA compat\\nsys.path.insert(0, \\\"/root/autodl-tmp/openvla_deps\\\")\\n\\nimport numpy as np\\nimport torch\\nfrom PIL import Image\\n\\n# Import OpenVLA model code\\nhf_dir = \\\"/root/autodl-tmp/openvla-repo/prismatic/extern/hf\\\"\\ninit_path = os.path.join(hf_dir, \\\"__init__.py\\\")\\nif not os.path.exists(init_path):\\n    open(init_path, \\\"w\\\").close()\\nsys.path.insert(0, \\\"/root/autodl-tmp/openvla-repo/prismatic/extern\\\")\\nfrom hf.configuration_prismatic import OpenVLAConfig\\nfrom hf.modeling_prismatic import OpenVLAForActionPrediction\\nfrom hf.processing_prismatic import PrismaticImageProcessor, PrismaticProcessor\\n\\nDEVICE = torch.device(\\\"cuda:0\\\")\\nCHECKPOINT_PATH = \\\"/root/autodl-tmp/openvla-libero-object\\\"\\nUNNORM_KEY = \\\"libero_object\\\"\\n\\nSUITE_MAX_STEPS = {\\n    \\\"libero_spatial\\\": 280,\\n    \\\"libero_object\\\": 280,\\n    \\\"libero_goal\\\": 300,\\n    \\\"libero_10\\\": 520,\\n}\\n\\n\\ndef parse_args():\\n    p = argparse.ArgumentParser()\\n    p.add_argument(\\\"--mode\\\", choices=[\\\"baseline\\\", \\\"random_prune\\\", \\\"l2norm_prune\\\", \\\"attention_prune\\\"], default=\\\"baseline\\\")\\n    p.add_argument(\\\"--k_ratio\\\", type=float, default=0.5)\\n    p.add_argument(\\\"--suite\\\", type=str, default=\\\"libero_object\\\")\\n    p.add_argument(\\\"--num_epis
…[truncated 7155 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-25T15:49:47.016849+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-38929",
  "command": "sed -n '110,280p' /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-38929",
    "command": "sed -n '110,280p' /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-25T15:49:47.017281+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'sed' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-25T15:49:47.017592+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-38929",
  "command": "tail -n +110 /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-38929",
    "command": "tail -n +110 /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-25T15:49:47.018018+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"def get_action(vla, processor, image: Image.Image, task_label: str):\\n    prompt = f\\\"In: What action should the robot take to {task_label.lower()}?\\\\nOut:\\\"\\n    inputs = processor(prompt, image).to(DEVICE, dtype=torch.bfloat16)\\n    action = vla.predict_action(**inputs, unnorm_key=UNNORM_KEY, do_sample=False)\\n    return action\\n\\n\\ndef normalize_gripper_action(action, binarize=True):\\n    action[..., -1] = 2 * action[..., -1] - 1\\n    if binarize:\\n        action[..., -1] = np.sign(action[..., -1])\\n    return action\\n\\n\\ndef invert_gripper_action(action):\\n    action[..., -1] *= -1.0\\n    return action\\n\\n\\nclass RandomPruningHook:\\n    def __init__(self, k_ratio=0.5):\\n        self.k_ratio = k_ratio\\n        self.logged = False\\n\\n    def __call__(self, module, input, output):\\n        B, N, D = output.shape\\n        keep = int(N * self.k_ratio)\\n        indices = torch.randperm(N)[:keep].sort().values.to(output.device)\\n        pruned = output[:, indices, :]\\n        if not self.logged:\\n            print(f\\\"[Pruning] {N} -> {keep} vision tokens (k={self.k_ratio})\\\", flush=True)\\n            self.logged = True\\n        return pruned\\n\\n\\n\\nclass L2NormPruningHook:\\n    \\\"\\\"\\\"Keep top-k vision tokens ranked by L2 norm (largest norm = most important).\\\"\\\"\\\"\\n    def __init__(self, k_ratio=0.5):\\n        self.k_ratio = k_ratio\\n        self.logged = False\\n\\n    def __call__(self, module, input, output):\\n        B, N, D = output.shape\\n        keep = int(N * self.k_ratio)\\n        norms = torch.norm(output.float(), dim=-1)  # (B, N)\\n        _, indices = torch.topk(norms, keep, dim=-1)  # (B, keep)\\n        indices = indices.sort(dim=-1).values  # preserve spatial order\\n        pruned = torch.gather(output, 1, indices.unsqueeze(-1).expand(-1, -1, D))\\n        if not self.logged:\\n            print(f\\\"[L2 Pruning] {N} -> {keep} vision
…[truncated 6912 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-25T15:49:47.018381+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-38929",
  "command": "tail -n +210 /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-38929",
    "command": "tail -n +210 /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-25T15:49:47.018775+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"                from transformers.models.llama.modeling_llama import rotate_half\\n                q_embed = (q * cos) + (rotate_half(q) * sin)\\n                k_embed = (k * cos) + (rotate_half(k) * sin)\\n\\n                if n_kv_heads != n_q_heads:\\n                    n_rep = n_q_heads // n_kv_heads\\n                    k_embed = k_embed.repeat_interleave(n_rep, dim=1)\\n                    v = v.repeat_interleave(n_rep, dim=1)\\n\\n                attn_weights = torch.matmul(q_embed, k_embed.transpose(-2, -1)) / math.sqrt(head_dim)\\n                attn_weights = F.softmax(attn_weights, dim=-1, dtype=torch.float32)\\n                all_attn.append(attn_weights)\\n\\n                attn_out = torch.matmul(attn_weights.to(v.dtype), v)\\n                attn_out = attn_out.transpose(1, 2).reshape(B, N, n_q_heads * head_dim)\\n                attn_out = layer.self_attn.o_proj(attn_out)\\n                hidden = hidden + attn_out\\n\\n                normed2 = layer.post_attention_layernorm(hidden)\\n                mlp_out = layer.mlp(normed2)\\n                hidden = hidden + mlp_out\\n\\n        avg_attn = torch.stack(all_attn).mean(dim=0).mean(dim=1)  # [B, N, N]\\n        importance = avg_attn.sum(dim=1)  # [B, N]\\n\\n        _, indices = torch.topk(importance, keep, dim=-1)\\n        indices = indices.sort(dim=-1).values\\n        pruned = torch.gather(output, 1, indices.unsqueeze(-1).expand(-1, -1, D))\\n\\n        if not self.logged:\\n            print(f\\\"[Attn Pruning] {N} -> {keep} vision tokens (k={self.k_ratio}), \\\"\\n                  f\\\"importance range=[{importance.min():.4f}, {importance.max():.4f}]\\\",\\n                  flush=True)\\n            self.logged = True\\n\\n        return pruned\\n\\n\\ndef count_vision_tokens(vla, processor):\\n    dummy = Image.new(\\\"RGB\\\", (224, 224), (128, 128, 128))\\n    prompt = \\\"In: What action should the robot take to pick up t
…[truncated 6602 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-25T15:49:47.019079+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-38929",
  "command": "find /root/autodl-tmp/importance_margin_vla_compress -name \"*zeromask*\" -o -name \"*zero_mask*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-38929",
    "command": "find /root/autodl-tmp/importance_margin_vla_compress -name \"*zeromask*\" -o -name \"*zero_mask*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-25T15:49:47.019330+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-25T15:49:47.019529+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-38929",
  "command": "ls /root/autodl-tmp/importance_margin_vla_compress/artifacts/ 2>/dev/null | head -50",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-38929",
    "command": "ls /root/autodl-tmp/importance_margin_vla_compress/artifacts/ 2>/dev/null | head -50",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-25T15:49:47.019726+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-25T15:49:47.019965+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Read eval_openvla_l2norm_libero.py on westd-38929', 'activeForm': 'Reading eval_openvla_l2norm_libero.py', 'status': 'completed'}, {'content': 'Write eval_openvla_zeromask_libero.py with --ablation_mode', 'activeForm': 'Writing eval_openvla_zeromask_libero.py', 'status': 'in_progress'}, {'content': 'Dry-run validate (syntax + argparse)', 'activeForm': 'Dry-running validation', 'status': 'pending'}, {'content': 'Register as artifact', 'activeForm': 'Registering artifact', 'status': 'pending'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Read eval_openvla_l2norm_libero.py on westd-38929', 'activeForm': 'Reading eval_openvla_l2norm_libero.py', 'status': 'completed'}, {'content': 'Write eval_openvla_zeromask_libero.py with --ablation_mode', 'activeForm': 'Writing eval_openvla_zeromask_libero.py', 'status': 'in_progress'}, {'content': 'Dry-run validate (syntax + argparse)', 'activeForm': 'Dry-running validation', 'status': 'pending'}, {'content': 'Register as artifact', 'activeForm': 'Registering artifact', 'status': 'pending'}]"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-25T15:49:47.020226+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-25T15:49:47.020630+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-38929",
  "command": "cat > /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_zeromask_libero.py << 'PYEOF'\n\"\"\"\nOpenVLA LIBERO Evaluation: Zero-mask vs Hard-prune Ablation.\n\nDistinguishes two failure mechanisms of token pruning:\n  (a) information loss (pruned token content gone)\n  (b) position disruption (remaining tokens shift in position embedding)\n\n--ablation_mode hard_prune : physically removes pruned tokens (sequence length shrinks)\n--ablation_mode zero_mask  : sets value of pruned tokens to 0, keeps sequence length / positions\n\nUsage:\n    python eval_openvla_zeromask_libero.py --mode l2norm_prune --ablation_mode zero_mask \\\\\n        --k_ratio 0.5 --suite libero_object\n\"\"\"\nimport argparse, io, json, math, os, sys, time\nos.environ[\"MUJOCO_GL\"] = \"egl\"\nos.environ.setdefault(\"CUDA_VISIBLE_DEVICES\", \"0\")\nos.environ[\"TRANSFORMERS_OFFLINE\"] = \"1\"\nos.environ[\"HF_HUB_OFFLINE\"] = \"1\"\n\n# Use transformers 4.40.1 for OpenVLA compat\nsys.path.insert(0, \"/root/autodl-tmp/openvla_deps\")\n\nimport numpy as np\nimport torch\nfrom PIL import Image\n\n# Import OpenVLA model code\nhf_dir = \"/root/autodl-tmp/openvla-repo/prismatic/extern/hf\"\ninit_path = os.path.join(hf_dir, \"__init__.py\")\nif not os.path.exists(init_path):\n    open(init_path, \"w\").close()\nsys.path.insert(0, \"/root/autodl-tmp/openvla-repo/prismatic/extern\")\nfrom hf.configuration_prismatic import OpenVLAConfig\nfrom hf.modeling_prismatic import OpenVLAForActionPrediction\nfrom hf.processing_prismatic import PrismaticImageProcessor, PrismaticProcessor\n\nDEVICE = torch.device(\"cuda:0\")\nCHECKPOINT_PATH = \"/root/autodl-tmp/openvla-libero-object\"\nUNNORM_KEY = \"libero_object\"\n\nSUITE_MAX_STEPS = {\n    \"libero_spatial\": 280,\n    \"libero_object\": 280,\n    \"libero_goal\": 300,\n    \"libero_10\": 520,\n}\n\n\ndef parse_args():\n    p = argparse.ArgumentParser()\n    p.add_argument(\"--mode\", choices=[\"baseline\", \"random_prune\", \"l2norm_prune\", \"attention_prune\"], default=\"baseline\")\n    p.add_argument(\"--ablation_mode\", choices=[\"hard_prune\", \"zero_mask\"], default=\"hard_prune\",\n                   help=\"hard_prune: physically remove pruned tokens. \"\n                        \"zero_mask: zero out pruned tokens, keep positions.\")\n    p.add_argument(\"--k_ratio\", type=float, default=0.5)\n    p.add_argument(\"--suite\", type=str, default=\"libero_object\")\n    p.add_argument(\"--num_episodes\", type=int, default=50)\n    p.add_argument(\"--seed\", type=int, default=7)\n    p.add_argument(\"--output\", type=str, default=None)\n    p.add_argument(\"--center_crop\", action=\"store_true\", default=True)\n    p.add_argument(\"--num_steps_wait\", type=int, default=10)\n    p.add_argument(\"--model_path\", type=str, default=\"/root/autodl-tmp/openvla-libero-object\")\n    p.add_argument(\"--unnorm_key\", type=str, default=\"libero_object\")\n    return p.parse_args()\n\n\ndef set_seed(seed):\n    torch.manual_seed(seed)\n    torch.cuda.manual_seed_all(seed)\n    np.random.seed(seed)\n    import random\n    random.seed(seed)\n\n\ndef load_model():\n    print(\"[*] Loading OpenVLA from:\", CHECKPOINT_PATH, flush=True)\n    config = OpenVLAConfig.from_pretrained(CHECKPOINT_PATH)\n    vla = OpenVLAForActionPrediction.from_pretrained(\n        CHECKPOINT_PATH,\n        config=config,\n        torch_dtype=torch.bfloat16,\n        low_cpu_mem_usage=True,\n    ).to(DEVICE)\n    with open(os.path.join(CHECKPOINT_PATH, \"dataset_statistics.json\")) as f:\n        vla.norm_stats = json.load(f)\n    vla.eval()\n\n    from transformers import AutoTokenizer\n    tokenizer = AutoTokenizer.from_pretrained(CHECKPOINT_PATH)\n    image_processor = PrismaticImageProcessor.from_pretrained(CHECKPOINT_PATH)\n    processor = PrismaticProcessor(image_processor=image_processor, tokenizer=tokenizer)\n    print(f\"[*] Model loaded, GPU: {torch.cuda.max_memory_allocated()/1e9:.1f} GB\", flush=True)\n    return vla, processor\n\n\ndef center_crop_image(image: Image.Image, crop_scale=0.9) -> Image.Image:\n    w, h = image.size\n    new_w = int(w * math.sqrt(crop_scale))\n    new_h = int(h * math.sqrt(crop_scale))\n    left = (w - new_w) // 2\n    top = (h - new_h) // 2\n    cropped = image.crop((left, top, left + new_w, top + new_h))\n    return cropped.resize((w, h), Image.LANCZOS)\n\n\ndef preprocess_image(obs, center_crop=True):\n    img = obs[\"agentview_image\"]\n    img = img[::-1, ::-1]\n    pil_img = Image.fromarray(img)\n    buf = io.BytesIO()\n    pil_img.save(buf, format=\"JPEG\")\n    buf.seek(0)\n    pil_img = Image.open(buf).convert(\"RGB\")\n    pil_img = pil_img.resize((224, 224), Image.LANCZOS)\n    if center_crop:\n        pil_img = center_crop_image(pil_img, crop_scale=0.9)\n    return pil_img\n\n\ndef get_action(vla, processor, image: Image.Image, task_label: str):\n    prompt = f\"In: What action should the robot take to {task_label.lower()}?\\nOut:\"\n    inputs = processor(prompt, image).to(DEVICE, dtype=torch.bfloat16)\n    action = vla.predict_action(**inputs, unnorm_key=UNNORM_KEY, do_sample=False)\n    return action\n\n\ndef normalize_gripper_action(action, binarize=True):\n    action[..., -1] = 2 * action[..., -1] - 1\n    if binarize:\n        action[..., -1] = np.sign(action[..., -1])\n    return action\n\n\ndef invert_gripper_action(action):\n    action[..., -1] *= -1.0\n    return action\n\n\ndef _apply_selection(output, keep_indices, ablation_mode):\n    \"\"\"Apply pruning given indices to keep.\n\n    output: (B, N, D)\n    keep_indices: (B, keep) — indices into N dimension, already sorted ascending.\n    ablation_mode: 'hard_prune' (gather, len=keep) or 'zero_mask' (mask out\n        non-selected positions, len=N preserved).\n    \"\"\"\n    B, N, D = output.shape\n    if ablation_mode == \"hard_prune\":\n        return torch.gather(output, 1, keep_indices.unsqueeze(-1).expand(-1, -1, D))\n    # zero_mask: build (B, N) keep-mask, zero the rest, preserve shape & positions\n    mask = torch.zeros(B, N, dtype=torch.bool, device=output.device)\n    mask.scatter_(1, keep_indices, True)\n    return output * mask.unsqueeze(-1).to(output.dtype)\n\n\nclass RandomPruningHook:\n    def __init__(self, k_ratio=0.5, ablation_mode=\"hard_prune\"):\n        self.k_ratio = k_ratio\n        self.ablation_mode = ablation_mode\n        self.logged = False\n\n    def __call__(self, module, input, output):\n        B, N, D = output.shape\n        keep = int(N * self.k_ratio)\n        if keep >= N:\n            return output\n        perm = torch.randperm(N, device=output.device)[:keep].sort().values\n        keep_indices = perm.unsqueeze(0).expand(B, -1)\n        out = _apply_selection(output, keep_indices, self.ablation_mode)\n        if not self.logged:\n            print(f\"[Random {self.ablation_mode}] {N} -> keep {keep} (k={self.k_ratio})\", flush=True)\n            self.logged = True\n        return out\n\n\nclass L2NormPruningHook:\n    \"\"\"Keep top-k vision tokens ranked by L2 norm (largest norm = most important).\"\"\"\n    def __init__(self, k_ratio=0.5, ablation_mode=\"hard_prune\"):\n        self.k_ratio = k_ratio\n        self.ablation_mode = ablation_mode\n        self.logged = False\n\n    def __call__(self, module, input, output):\n        B, N, D = output.shape\n        keep = int(N * self.k_ratio)\n        if keep >= N:\n            return output\n        norms = torch.norm(output.float(), dim=-1)  # (B, N)\n        _, indices = torch.topk(norms, keep, dim=-1)\n        keep_indices = indices.sort(dim=-1).values\n        out = _apply_selection(output, keep_indices, self.ablation_mode)\n        if not self.logged:\n            print(f\"[L2 {self.ablation_mode}] {N} -> keep {keep} (k={self.k_ratio})\", flush=True)\n            self.logged = True\n        return out\n\n\nclass AttentionPruningHook:\n    \"\"\"Keep top-k vision tokens ranked by attention importance (2-layer probe).\"\"\"\n    def __init__(self, k_ratio, vla, ablation_mode=\"hard_prune\"):\n        self.k_ratio = k_ratio\n        self.vla = vla\n        self.ablation_mode = ablation_mode\n        self.logged = False\n\n    def __call__(self, module, input, output):\n        import torch.nn.functional as F\n\n        B, N, D = output.shape\n        keep = max(1, int(N * self.k_ratio))\n        if keep >= N:\n            return output\n\n        lm = self.vla.language_model.model\n        position_ids = torch.arange(N, device=output.device).unsqueeze(0).expand(B, -1)\n\n        hidden = output\n        all_attn = []\n\n        with torch.no_grad():\n            for layer_idx in range(min(2, len(lm.layers))):\n                layer = lm.layers[layer_idx]\n                normed = layer.input_layernorm(hidden)\n\n                head_dim = layer.self_attn.head_dim\n                n_q_heads = layer.self_attn.num_heads\n                n_kv_heads = layer.self_attn.num_key_value_heads\n\n                q = layer.self_attn.q_proj(normed)\n                k = layer.self_attn.k_proj(normed)\n                v = layer.self_attn.v_proj(normed)\n\n                q = q.view(B, N, n_q_heads, head_dim).transpose(1, 2)\n                k = k.view(B, N, n_kv_heads, head_dim).transpose(1, 2)\n                v = v.view(B, N, n_kv_heads, head_dim).transpose(1, 2)\n\n                cos, sin = layer.self_attn.rotary_emb(v, position_ids)\n                from transformers.models.llama.modeling_llama import rotate_half\n                q_embed = (q * cos) + (rotate_half(q) * sin)\n                k_embed = (k * cos) + (rotate_half(k) * sin)\n\n                if n_kv_heads != n_q_heads:\n                    n_rep = n_q_heads // n_kv_heads\n                    k_embed = k_embed.repeat_interleave(n_rep, dim=1)\n                    v = v.repeat_interleave(n_rep, dim=1)\n\n                attn_weights = torch.matmul(q_embed, k_embed.transpose(-2, -1)) / math.sqrt(head_dim)\n                attn_weights = F.softmax(attn_weights, dim=-1, dtype=torch.float32)\n                all_attn.append(attn_weights)\n\n                attn_out = torch.matmul(attn_weights.to(v.dtype), v)\n                attn_out = attn_out.transpose(1, 2).reshape(B, N, n_q_heads * head_dim)\n                attn_out = layer.self_attn.o_proj(attn_out)\n                hidden = hidden + attn_out\n\n                normed2 = layer.post_attention_layernorm(hidden)\n                mlp_out = layer.mlp(normed2)\n                hidden = hidden + mlp_out\n\n        avg_attn = torch.stack(all_attn).mean(dim=0).mean(dim=1)  # [B, N, N]\n        importance = avg_attn.sum(dim=1)  # [B, N]\n\n        _, indices = torch.topk(importance, keep, dim=-1)\n        keep_indices = indices.sort(dim=-1).values\n        out = _apply_selection(output, keep_indices, self.ablation_mode)\n\n        if not self.logged:\n            print(f\"[Attn {self.ablation_mode}] {N} -> keep {keep} (k={self.k_ratio}), \"\n                  f\"importance range=[{importance.min():.4f}, {importance.max():.4f}]\", flush=True)\n            self.logged = True\n\n        return out\n\n\ndef count_vision_tokens(vla, processor):\n    dummy = Image.new(\"RGB\", (224, 224), (128, 128, 128))\n    prompt = \"In: What action should the robot take to pick up the object?\\nOut:\"\n    inputs = processor(prompt, dummy).to(DEVICE, dtype=torch.bfloat16)\n    count = {}\n    def hook(m, i, o):\n        count[\"n_tokens\"] = o.shape[1]\n        count[\"hidden_dim\"] = o.shape[2]\n        return o\n    h = vla.projector.register_forward_hook(hook)\n    with torch.no_grad():\n        vla.predict_action(**inputs, unnorm_key=UNNORM_KEY, do_sample=False)\n    h.remove()\n    return count\n\n\ndef main():\n    args = parse_args()\n    global CHECKPOINT_PATH, UNNORM_KEY\n    CHECKPOINT_PATH = args.model_path\n    UNNORM_KEY = args.unnorm_key\n    set_seed(args.seed)\n    max_steps = SUITE_MAX_STEPS.get(args.suite, 300)\n\n    if args.mode == \"baseline\" and args.ablation_mode != \"hard_prune\":\n        print(f\"[!] ablation_mode={args.ablation_mode} ignored for baseline mode\", flush=True)\n\n    vla, processor = load_model()\n\n    token_info = count_vision_tokens(vla, processor)\n    print(f\"[*] Vision tokens: {token_info['n_tokens']}, dim: {token_info['hidden_dim']}\", flush=True)\n\n    hook_handle = None\n    if args.mode == \"random_prune\":\n        hook_handle = vla.projector.register_forward_hook(\n            RandomPruningHook(args.k_ratio, ablation_mode=args.ablation_mode))\n        print(f\"[*] Random pruning: k={args.k_ratio} ablation={args.ablation_mode}\", flush=True)\n    elif args.mode == \"l2norm_prune\":\n        hook_handle = vla.projector.register_forward_hook(\n            L2NormPruningHook(args.k_ratio, ablation_mode=args.ablation_mode))\n        print(f\"[*] L2 norm pruning: k={args.k_ratio} ablation={args.ablation_mode}\", flush=True)\n    elif args.mode == \"attention_prune\":\n        hook_handle = vla.projector.register_forward_hook(\n            AttentionPruningHook(args.k_ratio, vla, ablation_mode=args.ablation_mode))\n        print(f\"[*] Attention pruning: k={args.k_ratio} ablation={args.ablation_mode}\", flush=True)\n\n    from libero.libero import benchmark, get_libero_path\n    from libero.libero.envs import OffScreenRenderEnv\n\n    benchmark_dict = benchmark.get_benchmark_dict()\n    task_suite = benchmark_dict[args.suite]()\n    n_tasks = task_suite.n_tasks\n    print(f\"[*] {args.suite}: {n_tasks} tasks x {args.num_episodes} episodes = {n_tasks * args.num_episodes} total\", flush=True)\n\n    per_task_results = {}\n    total_successes = 0\n    total_episodes = 0\n    t_start = time.time()\n\n    for task_id in range(n_tasks):\n        task = task_suite.get_task(task_id)\n        task_description = task.language\n        task_bddl_file = os.path.join(\n            get_libero_path(\"bddl_files\"), task.problem_folder, task.bddl_file\n        )\n        env = OffScreenRenderEnv(\n            bddl_file_name=task_bddl_file, camera_heights=256, camera_widths=256\n        )\n        env.seed(args.seed)\n\n        task_successes = 0\n        print(f\"\\n[Task {task_id+1}/{n_tasks}] {task_description}\", flush=True)\n\n        for ep in range(args.num_episodes):\n            env.reset()\n            init_states = task_suite.get_task_init_states(task_id)\n            obs = env.set_init_state(init_states[ep])\n            done = False\n            t = 0\n\n            while t < max_steps + args.num_steps_wait:\n                try:\n                    if t < args.num_steps_wait:\n                        obs, reward, done, info = env.step([0, 0, 0, 0, 0, 0, -1])\n                        t += 1\n                        continue\n\n                    img = preprocess_image(obs, center_crop=args.center_crop)\n                    action = get_action(vla, processor, img, task_description)\n                    action = normalize_gripper_action(action, binarize=True)\n                    action = invert_gripper_action(action)\n                    obs, reward, done, info = env.step(action.tolist())\n                    if done:\n                        task_successes += 1\n                        total_successes += 1\n                        break\n                    t += 1\n                except Exception as e:\n                    print(f\"  Exception t={t}: {e}\", flush=True)\n                    break\n\n            total_episodes += 1\n            if (ep + 1) % 10 == 0:\n                elapsed = time.time() - t_start\n                eps_per_min = total_episodes / (elapsed / 60)\n                print(f\"  Ep {ep+1}/{args.num_episodes} task_sr={task_successes}/{ep+1} \"\n                      f\"({eps_per_min:.1f} eps/min)\", flush=True)\n\n        task_sr = task_successes / args.num_episodes\n        per_task_results[task_description] = {\n            \"success_rate\": task_sr,\n            \"successes\": task_successes,\n            \"episodes\": args.num_episodes,\n        }\n        print(f\"  => Task SR: {task_sr:.3f} ({task_successes}/{args.num_episodes})\", flush=True)\n        env.close()\n\n    overall_sr = total_successes / total_episodes\n    elapsed = time.time() - t_start\n    print(f\"\\n{'='*60}\", flush=True)\n    print(f\"Overall SR: {overall_sr:.4f} ({total_successes}/{total_episodes})\", flush=True)\n    print(f\"Time: {elapsed/60:.1f} min\", flush=True)\n    print(f\"{'='*60}\", flush=True)\n\n    results = {\n        \"model\": os.path.basename(CHECKPOINT_PATH),\n        \"mode\": args.mode,\n        \"ablation_mode\": args.ablation_mode,\n        \"suite\": args.suite,\n        \"k_ratio\": args.k_ratio if args.mode != \"baseline\" else None,\n        \"overall_success_rate\": overall_sr,\n        \"total_successes\": total_successes,\n        \"total_episodes\": total_episodes,\n        \"per_task\": per_task_results,\n        \"vision_tokens\": token_info,\n        \"max_steps\": max_steps,\n        \"seed\": args.seed,\n        \"elapsed_minutes\": elapsed / 60,\n        \"timestamp\": time.strftime(\"%Y-%m-%d %H:%M:%S\"),\n    }\n\n    if args.output:\n        out_path = args.output\n    else:\n        out_dir = \"/root/autodl-tmp/importance_margin_vla_compress/eval_results\"\n        os.makedirs(out_dir, exist_ok=True)\n        suite_short = args.suite.replace('libero_', '')\n        if args.mode == \"baseline\":\n            out_path = f\"{out_dir}/openvla_baseline_{suite_short}_seed{args.seed}.json\"\n        else:\n            k_str = str(args.k_ratio).replace(\".\", \"\")\n            abl_tag = \"zm\" if args.ablation_mode == \"zero_mask\" else \"hp\"\n            out_path = f\"{out_dir}/openvla_{args.mode}_{abl_tag}_k{k_str}_{suite_short}_seed{args.seed}.json\"\n\n    with open(out_path, \"w\") as f:\n        json.dump(results, f, indent=2)\n    print(f\"[*] Saved: {out_path}\", flush=True)\n\n    if hook_handle:\n        hook_handle.remove()\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"WRITE_OK\"\nwc -l /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_zeromask_libero.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-38929",
    "command": "cat > /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_zeromask_libero.py << 'PYEOF'\n\"\"\"\nOpenVLA LIBERO Evaluation: Zero-mask vs Hard-prune Ablation.\n\nDistinguishes two failure mechanisms of token pruning:\n  (a) information loss (pruned token content gone)\n  (b) position disruption (remaining tokens shift in position embedding)\n\n--ablation_mode hard_prune : physically removes pruned tokens (sequence length shrinks)\n--ablation_mode zero_mask  : sets value of pruned tokens to 0, keeps sequence length / positions\n\nUsage:\n    python eval_openvla_zeromask_libero.py --mode l2norm_prune --ablation_mode zero_mask \\\\\n        --k_ratio 0.5 --suite libero_object\n\"\"\"\nimport argparse, io, json, math, os, sys, time\nos.environ[\"MUJOCO_GL\"] = \"egl\"\nos.environ.setdefault(\"CUDA_VISIBLE_DEVICES\", \"0\")\nos.environ[\"TRANSFORMERS_OFFLINE\"] = \"1\"\nos.environ[\"HF_HUB_OFFLINE\"] = \"1\"\n\n# Use transformers 4.40.1 for OpenVLA compat\nsys.path.insert(0, \"/root/autodl-tmp/openvla_deps\")\n\nimport numpy as np\nimport torch\nfrom PIL import Image\n\n# Import OpenVLA model code\nhf_dir = \"/root/autodl-tmp/openvla-repo/prismatic/extern/hf\"\ninit_path = os.path.join(hf_dir, \"__init__.py\")\nif not os.path.exists(init_path):\n    open(init_path, \"w\").close()\nsys.path.insert(0, \"/root/autodl-tmp/openvla-repo/prismatic/extern\")\nfrom hf.configuration_prismatic import OpenVLAConfig\nfrom hf.modeling_prismatic import OpenVLAForActionPrediction\nfrom hf.processing_prismatic import PrismaticImageProcessor, PrismaticProcessor\n\nDEVICE = torch.device(\"cuda:0\")\nCHECKPOINT_PATH = \"/root/autodl-tmp/openvla-libero-object\"\nUNNORM_KEY = \"libero_object\"\n\nSUITE_MAX_STEPS = {\n    \"libero_spatial\": 280,\n    \"libero_object\": 280,\n    \"libero_goal\": 300,\n    \"libero_10\": 520,\n}\n\n\ndef parse_args():\n    p = argparse.ArgumentParser()\n    p.add_argument(\"--mode\", choices=[\"baseline\", \"random_prune\", \"l2norm_prune\", \"attention_prune\"], default=\"baseline\")\n    p.add_argument(\"--ablation_mode\", choices=[\"hard_prune\", \"zero_mask\"], default=\"hard_prune\",\n                   help=\"hard_prune: physically remove pruned tokens. \"\n                        \"zero_mask: zero out pruned tokens, keep positions.\")\n    p.add_argument(\"--k_ratio\", type=float, default=0.5)\n    p.add_argument(\"--suite\", type=str, default=\"libero_object\")\n    p.add_argument(\"--num_episodes\", type=int, default=50)\n    p.add_argument(\"--seed\", type=int, default=7)\n    p.add_argument(\"--output\", type=str, default=None)\n    p.add_argument(\"--center_crop\", action=\"store_true\", default=True)\n    p.add_argument(\"--num_steps_wait\", type=int, default=10)\n    p.add_argument(\"--model_path\", type=str, default=\"/root/autodl-tmp/openvla-libero-object\")\n    p.add_argument(\"--unnorm_key\", type=str, default=\"libero_object\")\n    return p.parse_args()\n\n\ndef set_seed(seed):\n    torch.manual_seed(seed)\n    torch.cuda.manual_seed_all(seed)\n    np.random.seed(seed)\n    import random\n    random.seed(seed)\n\n\ndef load_model():\n    print(\"[*] Loading OpenVLA from:\", CHECKPOINT_PATH, flush=True)\n    config = OpenVLAConfig.from_pretrained(CHECKPOINT_PATH)\n    vla = OpenVLAForActionPrediction.from_pretrained(\n        CHECKPOINT_PATH,\n        config=config,\n        torch_dtype=torch.bfloat16,\n        low_cpu_mem_usage=True,\n    ).to(DEVICE)\n    with open(os.path.join(CHECKPOINT_PATH, \"dataset_statistics.json\")) as f:\n        vla.norm_stats = json.load(f)\n    vla.eval()\n\n    from transformers import AutoTokenizer\n    tokenizer = AutoTokenizer.from_pretrained(CHECKPOINT_PATH)\n    image_processor = PrismaticImageProcessor.from_pretrained(CHECKPOINT_PATH)\n    processor = PrismaticProcessor(image_processor=image_processor, tokenizer=tokenizer)\n    print(f\"[*] Model loaded, GPU: {torch.cuda.max_memory_allocated()/1e9:.1f} GB\", flush=True)\n    return vla, processor\n\n\ndef center_crop_image(image: Image.Image, crop_scale=0.9) -> Image.Image:\n    w, h = image.size\n    new_w = int(w * math.sqrt(crop_scale))\n    new_h = int(h * math.sqrt(crop_scale))\n    left = (w - new_w) // 2\n    top = (h - new_h) // 2\n    cropped = image.crop((left, top, left + new_w, top + new_h))\n    return cropped.resize((w, h), Image.LANCZOS)\n\n\ndef preprocess_image(obs, center_crop=True):\n    img = obs[\"agentview_image\"]\n    img = img[::-1, ::-1]\n    pil_img = Image.fromarray(img)\n    buf = io.BytesIO()\n    pil_img.save(buf, format=\"JPEG\")\n    buf.seek(0)\n    pil_img = Image.open(buf).convert(\"RGB\")\n    pil_img = pil_img.resize((224, 224), Image.LANCZOS)\n    if center_crop:\n        pil_img = center_crop_image(pil_img, crop_scale=0.9)\n    return pil_img\n\n\ndef get_action(vla, processor, image: Image.Image, task_label: str):\n    prompt = f\"In: What action should the robot take to {task_label.lower()}?\\nOut:\"\n    inputs = processor(prompt, image).to(DEVICE, dtype=torch.bfloat16)\n    action = vla.predict_action(**inputs, unnorm_key=UNNORM_KEY, do_sample=False)\n    return action\n\n\ndef normalize_gripper_action(action, binarize=True):\n    action[..., -1] = 2 * action[..., -1] - 1\n    if binarize:\n        action[..., -1] = np.sign(action[..., -1])\n    return action\n\n\ndef invert_gripper_action(action):\n    action[..., -1] *= -1.0\n    return action\n\n\ndef _apply_selection(output, keep_indices, ablation_mode):\n    \"\"\"Apply pruning given indices to keep.\n\n    output: (B, N, D)\n    keep_indices: (B, keep) — indices into N dimension, already sorted ascending.\n    ablation_mode: 'hard_prune' (gather, len=keep) or 'zero_mask' (mask out\n        non-selected positions, len=N preserved).\n    \"\"\"\n    B, N, D = output.shape\n    if ablation_mode == \"hard_prune\":\n        return torch.gather(output, 1, keep_indices.unsqueeze(-1).expand(-1, -1, D))\n    # zero_mask: build (B, N) keep-mask, zero the rest, preserve shape & positions\n    mask = torch.zeros(B, N, dtype=torch.bool, device=output.device)\n    mask.scatter_(1, keep_indices, True)\n    return output * mask.unsqueeze(-1).to(output.dtype)\n\n\nclass RandomPruningHook:\n    def __init__(self, k_ratio=0.5, ablation_mode=\"hard_prune\"):\n        self.k_ratio = k_ratio\n        self.ablation_mode = ablation_mode\n        self.logged = False\n\n    def __call__(self, module, input, output):\n        B, N, D = output.shape\n        keep = int(N * self.k_ratio)\n        if keep >= N:\n            return output\n        perm = torch.randperm(N, device=output.device)[:keep].sort().values\n        keep_indices = perm.unsqueeze(0).expand(B, -1)\n        out = _apply_selection(output, keep_indices, self.ablation_mode)\n        if not self.logged:\n            print(f\"[Random {self.ablation_mode}] {N} -> keep {keep} (k={self.k_ratio})\", flush=True)\n            self.logged = True\n        return out\n\n\nclass L2NormPruningHook:\n    \"\"\"Keep top-k vision tokens ranked by L2 norm (largest norm = most important).\"\"\"\n    def __init__(self, k_ratio=0.5, ablation_mode=\"hard_prune\"):\n        self.k_ratio = k_ratio\n        self.ablation_mode = ablation_mode\n        self.logged = False\n\n    def __call__(self, module, input, output):\n        B, N, D = output.shape\n        keep = int(N * self.k_ratio)\n        if keep >= N:\n            return output\n        norms = torch.norm(output.float(), dim=-1)  # (B, N)\n        _, indices = torch.topk(norms, keep, dim=-1)\n        keep_indices = indices.sort(dim=-1).values\n        out = _apply_selection(output, keep_indices, self.ablation_mode)\n        if not self.logged:\n            print(f\"[L2 {self.ablation_mode}] {N} -> keep {keep} (k={self.k_ratio})\", flush=True)\n            self.logged = True\n        return out\n\n\nclass AttentionPruningHook:\n    \"\"\"Keep top-k vision tokens ranked by attention importance (2-layer probe).\"\"\"\n    def __init__(self, k_ratio, vla, ablation_mode=\"hard_prune\"):\n        self.k_ratio = k_ratio\n        self.vla = vla\n        self.ablation_mode = ablation_mode\n        self.logged = False\n\n    def __call__(self, module, input, output):\n        import torch.nn.functional as F\n\n        B, N, D = output.shape\n        keep = max(1, int(N * self.k_ratio))\n        if keep >= N:\n            return output\n\n        lm = self.vla.language_model.model\n        position_ids = torch.arange(N, device=output.device).unsqueeze(0).expand(B, -1)\n\n        hidden = output\n        all_attn = []\n\n        with torch.no_grad():\n            for layer_idx in range(min(2, len(lm.layers))):\n                layer = lm.layers[layer_idx]\n                normed = layer.input_layernorm(hidden)\n\n                head_dim = layer.self_attn.head_dim\n                n_q_heads = layer.self_attn.num_heads\n                n_kv_heads = layer.self_attn.num_key_value_heads\n\n                q = layer.self_attn.q_proj(normed)\n                k = layer.self_attn.k_proj(normed)\n                v = layer.self_attn.v_proj(normed)\n\n                q = q.view(B, N, n_q_heads, head_dim).transpose(1, 2)\n                k = k.view(B, N, n_kv_heads, head_dim).transpose(1, 2)\n                v = v.view(B, N, n_kv_heads, head_dim).transpose(1, 2)\n\n                cos, sin = layer.self_attn.rotary_emb(v, position_ids)\n                from transformers.models.llama.modeling_llama import rotate_half\n                q_embed = (q * cos) + (rotate_half(q) * sin)\n                k_embed = (k * cos) + (rotate_half(k) * sin)\n\n                if n_kv_heads != n_q_heads:\n                    n_rep = n_q_heads // n_kv_heads\n                    k_embed = k_embed.repeat_interleave(n_rep, dim=1)\n                    v = v.repeat_interleave(n_rep, dim=1)\n\n                attn_weights = torch.matmul(q_embed, k_embed.transpose(-2, -1)) / math.sqrt(head_dim)\n                attn_weights = F.softmax(attn_weights, dim=-1, dtype=torch.float32)\n                all_attn.append(attn_weights)\n\n                attn_out = torch.matmul(attn_weights.to(v.dtype), v)\n                attn_out = attn_out.transpose(1, 2).reshape(B, N, n_q_heads * head_dim)\n                attn_out = layer.self_attn.o_proj(attn_out)\n                hidden = hidden + attn_out\n\n                normed2 = layer.post_attention_layernorm(hidden)\n                mlp_out = layer.mlp(normed2)\n                hidden = hidden + mlp_out\n\n        avg_attn = torch.stack(all_attn).mean(dim=0).mean(dim=1)  # [B, N, N]\n        importance = avg_attn.sum(dim=1)  # [B, N]\n\n        _, indices = torch.topk(importance, keep, dim=-1)\n        keep_indices = indices.sort(dim=-1).values\n        out = _apply_selection(output, keep_indices, self.ablation_mode)\n\n        if not self.logged:\n            print(f\"[Attn {self.ablation_mode}] {N} -> keep {keep} (k={self.k_ratio}), \"\n                  f\"importance range=[{importance.min():.4f}, {importance.max():.4f}]\", flush=True)\n            self.logged = True\n\n        return out\n\n\ndef count_vision_tokens(vla, processor):\n    dummy = Image.new(\"RGB\", (224, 224), (128, 128, 128))\n    prompt = \"In: What action should the robot take to pick up the object?\\nOut:\"\n    inputs = processor(prompt, dummy).to(DEVICE, dtype=torch.bfloat16)\n    count = {}\n    def hook(m, i, o):\n        count[\"n_tokens\"] = o.shape[1]\n        count[\"hidden_dim\"] = o.shape[2]\n        return o\n    h = vla.projector.register_forward_hook(hook)\n    with torch.no_grad():\n        vla.predict_action(**inputs, unnorm_key=UNNORM_KEY, do_sample=False)\n    h.remove()\n    return count\n\n\ndef main():\n    args = parse_args()\n    global CHECKPOINT_PATH, UNNORM_KEY\n    CHECKPOINT_PATH = args.model_path\n    UNNORM_KEY = args.unnorm_key\n    set_seed(args.seed)\n    max_steps = SUITE_MAX_STEPS.get(args.suite, 300)\n\n    if args.mode == \"baseline\" and args.ablation_mode != \"hard_prune\":\n        print(f\"[!] ablation_mode={args.ablation_mode} ignored for baseline mode\", flush=True)\n\n    vla, processor = load_model()\n\n    token_info = count_vision_tokens(vla, processor)\n    print(f\"[*] Vision tokens: {token_info['n_tokens']}, dim: {token_info['hidden_dim']}\", flush=True)\n\n    hook_handle = None\n    if args.mode == \"random_prune\":\n        hook_handle = vla.projector.register_forward_hook(\n            RandomPruningHook(args.k_ratio, ablation_mode=args.ablation_mode))\n        print(f\"[*] Random pruning: k={args.k_ratio} ablation={args.ablation_mode}\", flush=True)\n    elif args.mode == \"l2norm_prune\":\n        hook_handle = vla.projector.register_forward_hook(\n            L2NormPruningHook(args.k_ratio, ablation_mode=args.ablation_mode))\n        print(f\"[*] L2 norm pruning: k={args.k_ratio} ablation={args.ablation_mode}\", flush=True)\n    elif args.mode == \"attention_prune\":\n        hook_handle = vla.projector.register_forward_hook(\n            AttentionPruningHook(args.k_ratio, vla, ablation_mode=args.ablation_mode))\n        print(f\"[*] Attention pruning: k={args.k_ratio} ablation={args.ablation_mode}\", flush=True)\n\n    from libero.libero import benchmark, get_libero_path\n    from libero.libero.envs import OffScreenRenderEnv\n\n    benchmark_dict = benchmark.get_benchmark_dict()\n    task_suite = benchmark_dict[args.suite]()\n    n_tasks = task_suite.n_tasks\n    print(f\"[*] {args.suite}: {n_tasks} tasks x {args.num_episodes} episodes = {n_tasks * args.num_episodes} total\", flush=True)\n\n    per_task_results = {}\n    total_successes = 0\n    total_episodes = 0\n    t_start = time.time()\n\n    for task_id in range(n_tasks):\n        task = task_suite.get_task(task_id)\n        task_description = task.language\n        task_bddl_file = os.path.join(\n            get_libero_path(\"bddl_files\"), task.problem_folder, task.bddl_file\n        )\n        env = OffScreenRenderEnv(\n            bddl_file_name=task_bddl_file, camera_heights=256, camera_widths=256\n        )\n        env.seed(args.seed)\n\n        task_successes = 0\n        print(f\"\\n[Task {task_id+1}/{n_tasks}] {task_description}\", flush=True)\n\n        for ep in range(args.num_episodes):\n            env.reset()\n            init_states = task_suite.get_task_init_states(task_id)\n            obs = env.set_init_state(init_states[ep])\n            done = False\n            t = 0\n\n            while t < max_steps + args.num_steps_wait:\n                try:\n                    if t < args.num_steps_wait:\n                        obs, reward, done, info = env.step([0, 0, 0, 0, 0, 0, -1])\n                        t += 1\n                        continue\n\n                    img = preprocess_image(obs, center_crop=args.center_crop)\n                    action = get_action(vla, processor, img, task_description)\n                    action = normalize_gripper_action(action, binarize=True)\n                    action = invert_gripper_action(action)\n                    obs, reward, done, info = env.step(action.tolist())\n                    if done:\n                        task_successes += 1\n                        total_successes += 1\n                        break\n                    t += 1\n                except Exception as e:\n                    print(f\"  Exception t={t}: {e}\", flush=True)\n                    break\n\n            total_episodes += 1\n            if (ep + 1) % 10 == 0:\n                elapsed = time.time() - t_start\n                eps_per_min = total_episodes / (elapsed / 60)\n                print(f\"  Ep {ep+1}/{args.num_episodes} task_sr={task_successes}/{ep+1} \"\n                      f\"({eps_per_min:.1f} eps/min)\", flush=True)\n\n        task_sr = task_successes / args.num_episodes\n        per_task_results[task_description] = {\n            \"success_rate\": task_sr,\n            \"successes\": task_successes,\n            \"episodes\": args.num_episodes,\n        }\n        print(f\"  => Task SR: {task_sr:.3f} ({task_successes}/{args.num_episodes})\", flush=True)\n        env.close()\n\n    overall_sr = total_successes / total_episodes\n    elapsed = time.time() - t_start\n    print(f\"\\n{'='*60}\", flush=True)\n    print(f\"Overall SR: {overall_sr:.4f} ({total_successes}/{total_episodes})\", flush=True)\n    print(f\"Time: {elapsed/60:.1f} min\", flush=True)\n    print(f\"{'='*60}\", flush=True)\n\n    results = {\n        \"model\": os.path.basename(CHECKPOINT_PATH),\n        \"mode\": args.mode,\n        \"ablation_mode\": args.ablation_mode,\n        \"suite\": args.suite,\n        \"k_ratio\": args.k_ratio if args.mode != \"baseline\" else None,\n        \"overall_success_rate\": overall_sr,\n        \"total_successes\": total_successes,\n        \"total_episodes\": total_episodes,\n        \"per_task\": per_task_results,\n        \"vision_tokens\": token_info,\n        \"max_steps\": max_steps,\n        \"seed\": args.seed,\n        \"elapsed_minutes\": elapsed / 60,\n        \"timestamp\": time.strftime(\"%Y-%m-%d %H:%M:%S\"),\n    }\n\n    if args.output:\n        out_path = args.output\n    else:\n        out_dir = \"/root/autodl-tmp/importance_margin_vla_compress/eval_results\"\n        os.makedirs(out_dir, exist_ok=True)\n        suite_short = args.suite.replace('libero_', '')\n        if args.mode == \"baseline\":\n            out_path = f\"{out_dir}/openvla_baseline_{suite_short}_seed{args.seed}.json\"\n        else:\n            k_str = str(args.k_ratio).replace(\".\", \"\")\n            abl_tag = \"zm\" if args.ablation_mode == \"zero_mask\" else \"hp\"\n            out_path = f\"{out_dir}/openvla_{args.mode}_{abl_tag}_k{k_str}_{suite_short}_seed{args.seed}.json\"\n\n    with open(out_path, \"w\") as f:\n        json.dump(results, f, indent=2)\n    print(f\"[*] Saved: {out_path}\", flush=True)\n\n    if hook_handle:\n        hook_handle.remove()\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"WRITE_OK\"\nwc -l /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_zeromask_libero.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-25T15:49:47.021181+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"WRITE_OK\\n439 /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_zeromask_libero.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-25T15:49:47.021414+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Read eval_openvla_l2norm_libero.py on westd-38929', 'activeForm': 'Reading eval_openvla_l2norm_libero.py', 'status': 'completed'}, {'content': 'Write eval_openvla_zeromask_libero.py with --ablation_mode', 'activeForm': 'Writing eval_openvla_zeromask_libero.py', 'status': 'completed'}, {'content': 'Dry-run validate (syntax + argparse)', 'activeForm': 'Dry-running validation', 'status': 'in_progress'}, {'content': 'Register as artifact', 'activeForm': 'Registering artifact', 'status': 'pending'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Read eval_openvla_l2norm_libero.py on westd-38929', 'activeForm': 'Reading eval_openvla_l2norm_libero.py', 'status': 'completed'}, {'content': 'Write eval_openvla_zeromask_libero.py with --ablation_mode', 'activeForm': 'Writing eval_openvla_zeromask_libero.py', 'status': 'completed'}, {'content': 'Dry-run validate (syntax + argparse)', 'activeForm': 'Dry-running validation', 'status': 'in_progress'}, {'content': 'Register as artifact', 'activeForm': 'Registering artifact', 'status': 'pending'}]"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-25T15:49:47.021635+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-25T15:49:47.021859+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-38929",
  "command": "cd /root/autodl-tmp/importance_margin_vla_compress && python3 -m py_compile eval_openvla_zeromask_libero.py && echo \"PYCOMPILE_OK\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-38929",
    "command": "cd /root/autodl-tmp/importance_margin_vla_compress && python3 -m py_compile eval_openvla_zeromask_libero.py && echo \"PYCOMPILE_OK\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-25T15:49:47.022061+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"PYCOMPILE_OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.48}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-25T15:49:47.022295+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-38929",
  "command": "cd /tmp && cat > _ablation_logic_test.py << 'EOF'\n\"\"\"Verify the zero_mask vs hard_prune branch in _apply_selection works correctly.\nPure-tensor unit test, no model load.\"\"\"\nimport sys\nsys.path.insert(0, \"/root/autodl-tmp/importance_margin_vla_compress\")\n# import the helper without touching the model-loading top-level code\nimport ast, types\nsrc = open(\"/root/autodl-tmp/importance_margin_vla_compress/eval_openvla_zeromask_libero.py\").read()\ntree = ast.parse(src)\n# pull out only the _apply_selection function definition\nfn_src = None\nfor node in tree.body:\n    if isinstance(node, ast.FunctionDef) and node.name == \"_apply_selection\":\n        fn_src = ast.unparse(node)\n        break\nassert fn_src is not None, \"no _apply_selection found\"\nimport torch\nns = {\"torch\": torch}\nexec(fn_src, ns)\n_apply_selection = ns[\"_apply_selection\"]\n\nB, N, D = 2, 8, 4\ntorch.manual_seed(0)\noutput = torch.randn(B, N, D)\nkeep_idx = torch.tensor([[0, 2, 5, 7], [1, 3, 4, 6]])  # B=2, keep=4\n\nhp = _apply_selection(output, keep_idx, \"hard_prune\")\nzm = _apply_selection(output, keep_idx, \"zero_mask\")\n\n# hard_prune: shape (B, 4, D), equal to gathered rows\nassert hp.shape == (B, 4, D), f\"hard_prune wrong shape: {hp.shape}\"\nfor b in range(B):\n    for j, idx in enumerate(keep_idx[b].tolist()):\n        assert torch.allclose(hp[b, j], output[b, idx]), f\"hp mismatch b={b} j={j}\"\n\n# zero_mask: shape (B, N, D); kept rows identical, others zero\nassert zm.shape == (B, N, D), f\"zero_mask wrong shape: {zm.shape}\"\nfor b in range(B):\n    keep_set = set(keep_idx[b].tolist())\n    for n in range(N):\n        if n in keep_set:\n            assert torch.allclose(zm[b, n], output[b, n]), f\"zm: kept row changed b={b} n={n}\"\n        else:\n            assert torch.allclose(zm[b, n], torch.zeros(D)), f\"zm: pruned row not zero b={b} n={n}\"\n\nprint(\"APPLY_SELECTION_OK\")\nEOF\npython3 _ablation_logic_test.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-38929",
    "command": "cd /tmp && cat > _ablation_logic_test.py << 'EOF'\n\"\"\"Verify the zero_mask vs hard_prune branch in _apply_selection works correctly.\nPure-tensor unit test, no model load.\"\"\"\nimport sys\nsys.path.insert(0, \"/root/autodl-tmp/importance_margin_vla_compress\")\n# import the helper without touching the model-loading top-level code\nimport ast, types\nsrc = open(\"/root/autodl-tmp/importance_margin_vla_compress/eval_openvla_zeromask_libero.py\").read()\ntree = ast.parse(src)\n# pull out only the _apply_selection function definition\nfn_src = None\nfor node in tree.body:\n    if isinstance(node, ast.FunctionDef) and node.name == \"_apply_selection\":\n        fn_src = ast.unparse(node)\n        break\nassert fn_src is not None, \"no _apply_selection found\"\nimport torch\nns = {\"torch\": torch}\nexec(fn_src, ns)\n_apply_selection = ns[\"_apply_selection\"]\n\nB, N, D = 2, 8, 4\ntorch.manual_seed(0)\noutput = torch.randn(B, N, D)\nkeep_idx = torch.tensor([[0, 2, 5, 7], [1, 3, 4, 6]])  # B=2, keep=4\n\nhp = _apply_selection(output, keep_idx, \"hard_prune\")\nzm = _apply_selection(output, keep_idx, \"zero_mask\")\n\n# hard_prune: shape (B, 4, D), equal to gathered rows\nassert hp.shape == (B, 4, D), f\"hard_prune wrong shape: {hp.shape}\"\nfor b in range(B):\n    for j, idx in enumerate(keep_idx[b].tolist()):\n        assert torch.allclose(hp[b, j], output[b, idx]), f\"hp mismatch b={b} j={j}\"\n\n# zero_mask: shape (B, N, D); kept rows identical, others zero\nassert zm.shape == (B, N, D), f\"zero_mask wrong shape: {zm.shape}\"\nfor b in range(B):\n    keep_set = set(keep_idx[b].tolist())\n    for n in range(N):\n        if n in keep_set:\n            assert torch.allclose(zm[b, n], output[b, n]), f\"zm: kept row changed b={b} n={n}\"\n        else:\n            assert torch.allclose(zm[b, n], torch.zeros(D)), f\"zm: pruned row not zero b={b} n={n}\"\n\nprint(\"APPLY_SELECTION_OK\")\nEOF\npython3 _ablation_logic_test.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-25T15:49:47.022580+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cd /tmp && cat > _ablation_logic_test.py << \\\\'EOF\\\\'\\\\n\\\"\\\"\\\"Verify the zero_mask vs hard_prune branch in _apply_selection works correctly.\\\\nPure-tensor unit test, no model load.\\\"\\\"\\\"\\\\nimport sys\\\\nsys.path.insert(0, \\\"/root/autodl-tmp/importance_margin_vla_compress\\\")\\\\n# import the helper without touching the model-loading top-level code\\\\nimport ast, types\\\\nsrc = open(\\\"/root/autodl-tmp/importance_margin_vla_compress/eval_openvla_zeromask_libero.py\\\").read()\\\\ntree = ast.parse(src)\\\\n# pull out only the _apply_selection function definition\\\\nfn_src = None\\\\nfor node in tree.body:\\\\n    if isinstance(node, ast.FunctionDef) and node.name == \\\"_apply_selection\\\":\\\\n        fn_src = ast.unparse(node)\\\\n        break\\\\nassert fn_src is not None, \\\"no _apply_selection found\\\"\\\\nimport torch\\\\nns = {\\\"torch\\\": torch}\\\\nexec(fn_src, ns)\\\\n_apply_selection = ns[\\\"_apply_selection\\\"]\\\\n\\\\nB, N, D = 2, 8, 4\\\\ntorch.manual_seed(0)\\\\noutput = torch.randn(B, N, D)\\\\nkeep_idx = torch.tensor([[0, 2, 5, 7], [1, 3, 4, 6]])  # B=2, keep=4\\\\n\\\\nhp = _apply_selection(output, keep_idx, \\\"hard_prune\\\")\\\\nzm = _apply_selection(output, keep_idx, \\\"zero_mask\\\")\\\\n\\\\n# hard_prune: shape (B, 4, D), equal to gathered rows\\\\nassert hp.shape == (B, 4, D), f\\\"hard_prune wrong shape: {hp.shape}\\\"\\\\nfor b in range(B):\\\\n    for j, idx in enumerate(keep_idx[b].tolist()):\\\\n        assert torch.allclose(hp[b, j], output[b, idx]), f\\\"hp mismatch b={b} j={j}\\\"\\\\n\\\\n# zero_mask: shape (B, N, D); kept rows identical, others zero\\\\nassert zm.shape == (B, N, D), f\\\"zero_mask wrong shape: {zm.shape}\\\"\\\\nfor b in range(B):\\\\n    keep_set = set(keep_idx[b].tolist())\\\\n    for n in range(N):\\\\n        if n in keep_set:\\\\n            assert torch.allclose(
…[truncated 560 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-25T15:49:47.022838+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-38929",
  "command": "cd /tmp && cat > _argparse_test.py << 'EOF'\n\"\"\"Verify --help and --ablation_mode argparse without loading the model.\"\"\"\nimport ast, sys\nsrc = open(\"/root/autodl-tmp/importance_margin_vla_compress/eval_openvla_zeromask_libero.py\").read()\ntree = ast.parse(src)\n# extract parse_args function only\nfor node in tree.body:\n    if isinstance(node, ast.FunctionDef) and node.name == \"parse_args\":\n        fn_src = ast.unparse(node)\n        break\nimport argparse\nns = {\"argparse\": argparse}\nexec(fn_src, ns)\nparse_args = ns[\"parse_args\"]\n\n# valid combos\nfor argv in [\n    [\"--mode\", \"baseline\"],\n    [\"--mode\", \"l2norm_prune\", \"--ablation_mode\", \"zero_mask\", \"--k_ratio\", \"0.5\"],\n    [\"--mode\", \"random_prune\", \"--ablation_mode\", \"hard_prune\"],\n    [\"--mode\", \"attention_prune\", \"--ablation_mode\", \"zero_mask\", \"--k_ratio\", \"0.25\"],\n]:\n    sys.argv = [\"prog\"] + argv\n    args = parse_args()\n    assert args.ablation_mode in (\"hard_prune\", \"zero_mask\")\n    print(f\"OK: {argv} -> mode={args.mode} ablation={args.ablation_mode} k={args.k_ratio}\")\n\n# invalid ablation_mode rejected\nsys.argv = [\"prog\", \"--ablation_mode\", \"bogus\"]\ntry:\n    parse_args()\n    print(\"FAIL: should have rejected bogus ablation_mode\")\n    sys.exit(1)\nexcept SystemExit:\n    print(\"OK: rejected bogus ablation_mode\")\n\nprint(\"ARGPARSE_OK\")\nEOF\npython3 _argparse_test.py 2>&1 | tail -20",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-38929",
    "command": "cd /tmp && cat > _argparse_test.py << 'EOF'\n\"\"\"Verify --help and --ablation_mode argparse without loading the model.\"\"\"\nimport ast, sys\nsrc = open(\"/root/autodl-tmp/importance_margin_vla_compress/eval_openvla_zeromask_libero.py\").read()\ntree = ast.parse(src)\n# extract parse_args function only\nfor node in tree.body:\n    if isinstance(node, ast.FunctionDef) and node.name == \"parse_args\":\n        fn_src = ast.unparse(node)\n        break\nimport argparse\nns = {\"argparse\": argparse}\nexec(fn_src, ns)\nparse_args = ns[\"parse_args\"]\n\n# valid combos\nfor argv in [\n    [\"--mode\", \"baseline\"],\n    [\"--mode\", \"l2norm_prune\", \"--ablation_mode\", \"zero_mask\", \"--k_ratio\", \"0.5\"],\n    [\"--mode\", \"random_prune\", \"--ablation_mode\", \"hard_prune\"],\n    [\"--mode\", \"attention_prune\", \"--ablation_mode\", \"zero_mask\", \"--k_ratio\", \"0.25\"],\n]:\n    sys.argv = [\"prog\"] + argv\n    args = parse_args()\n    assert args.ablation_mode in (\"hard_prune\", \"zero_mask\")\n    print(f\"OK: {argv} -> mode={args.mode} ablation={args.ablation_mode} k={args.k_ratio}\")\n\n# invalid ablation_mode rejected\nsys.argv = [\"prog\", \"--ablation_mode\", \"bogus\"]\ntry:\n    parse_args()\n    print(\"FAIL: should have rejected bogus ablation_mode\")\n    sys.exit(1)\nexcept SystemExit:\n    print(\"OK: rejected bogus ablation_mode\")\n\nprint(\"ARGPARSE_OK\")\nEOF\npython3 _argparse_test.py 2>&1 | tail -20",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-25T15:49:47.023084+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"usage: prog [-h] [--mode {baseline,random_prune,l2norm_prune,attention_prune}]\\n            [--ablation_mode {hard_prune,zero_mask}] [--k_ratio K_RATIO]\\n            [--suite SUITE] [--num_episodes NUM_EPISODES] [--seed SEED]\\n            [--output OUTPUT] [--center_crop]\\n            [--num_steps_wait NUM_STEPS_WAIT] [--model_path MODEL_PATH]\\n            [--unnorm_key UNNORM_KEY]\\nprog: error: argument --ablation_mode: invalid choice: 'bogus' (choose from 'hard_prune', 'zero_mask')\\nOK: ['--mode', 'baseline'] -> mode=baseline ablation=hard_prune k=0.5\\nOK: ['--mode', 'l2norm_prune', '--ablation_mode', 'zero_mask', '--k_ratio', '0.5'] -> mode=l2norm_prune ablation=zero_mask k=0.5\\nOK: ['--mode', 'random_prune', '--ablation_mode', 'hard_prune'] -> mode=random_prune ablation=hard_prune k=0.5\\nOK: ['--mode', 'attention_prune', '--ablation_mode', 'zero_mask', '--k_ratio', '0.25'] -> mode=attention_prune ablation=zero_mask k=0.25\\nOK: rejected bogus ablation_mode\\nARGPARSE_OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.18}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-25T15:49:47.023372+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-38929",
  "command": "ls /root/autodl-tmp/importance_margin_vla_compress/.venv/bin/python /root/miniconda3/bin/python /opt/conda/bin/python /root/autodl-tmp/openvla_deps/bin/python",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-38929",
    "command": "ls /root/autodl-tmp/importance_margin_vla_compress/.venv/bin/python /root/miniconda3/bin/python /opt/conda/bin/python /root/autodl-tmp/openvla_deps/bin/python",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-25T15:49:47.023586+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"/root/miniconda3/bin/python\\n\", \"stderr\": \"ls: cannot access '/root/autodl-tmp/importance_margin_vla_compress/.venv/bin/python': No such file or directory\\nls: cannot access '/opt/conda/bin/python': No such file or directory\\nls: cannot access '/root/autodl-tmp/openvla_deps/bin/python': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-25T15:49:47.023783+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-38929",
  "command": "/root/miniconda3/bin/python /tmp/_ablation_logic_test.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-38929",
    "command": "/root/miniconda3/bin/python /tmp/_ablation_logic_test.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-25T15:49:47.023980+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"APPLY_SELECTION_OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.73}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-25T15:49:47.024231+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-38929",
  "command": "rm -f /tmp/_ablation_logic_test.py /tmp/_argparse_test.py && echo \"CLEANED\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-38929",
    "command": "rm -f /tmp/_ablation_logic_test.py /tmp/_argparse_test.py && echo \"CLEANED\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-25T15:49:47.024443+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"CLEANED\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-25T15:49:47.024647+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-38929",
  "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_zeromask_libero.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-38929",
    "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_zeromask_libero.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-25T15:49:47.025090+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nOpenVLA LIBERO Evaluation: Zero-mask vs Hard-prune Ablation.\\n\\nDistinguishes two failure mechanisms of token pruning:\\n  (a) information loss (pruned token content gone)\\n  (b) position disruption (remaining tokens shift in position embedding)\\n\\n--ablation_mode hard_prune : physically removes pruned tokens (sequence length shrinks)\\n--ablation_mode zero_mask  : sets value of pruned tokens to 0, keeps sequence length / positions\\n\\nUsage:\\n    python eval_openvla_zeromask_libero.py --mode l2norm_prune --ablation_mode zero_mask \\\\\\\\\\n        --k_ratio 0.5 --suite libero_object\\n\\\"\\\"\\\"\\nimport argparse, io, json, math, os, sys, time\\nos.environ[\\\"MUJOCO_GL\\\"] = \\\"egl\\\"\\nos.environ.setdefault(\\\"CUDA_VISIBLE_DEVICES\\\", \\\"0\\\")\\nos.environ[\\\"TRANSFORMERS_OFFLINE\\\"] = \\\"1\\\"\\nos.environ[\\\"HF_HUB_OFFLINE\\\"] = \\\"1\\\"\\n\\n# Use transformers 4.40.1 for OpenVLA compat\\nsys.path.insert(0, \\\"/root/autodl-tmp/openvla_deps\\\")\\n\\nimport numpy as np\\nimport torch\\nfrom PIL import Image\\n\\n# Import OpenVLA model code\\nhf_dir = \\\"/root/autodl-tmp/openvla-repo/prismatic/extern/hf\\\"\\ninit_path = os.path.join(hf_dir, \\\"__init__.py\\\")\\nif not os.path.exists(init_path):\\n    open(init_path, \\\"w\\\").close()\\nsys.path.insert(0, \\\"/root/autodl-tmp/openvla-repo/prismatic/extern\\\")\\nfrom hf.configuration_prismatic import OpenVLAConfig\\nfrom hf.modeling_prismatic import OpenVLAForActionPrediction\\nfrom hf.processing_prismatic import PrismaticImageProcessor, PrismaticProcessor\\n\\nDEVICE = torch.device(\\\"cuda:0\\\")\\nCHECKPOINT_PATH = \\\"/root/autodl-tmp/openvla-libero-object\\\"\\nUNNORM_KEY = \\\"libero_object\\\"\\n\\nSUITE_MAX_STEPS = {\\n    \\\"libero_spatial\\\": 280,\\n    \\\"libero_object\\\": 280,\\n    \\\"libero_goal\\\": 300,\\n    \\\"libero_10\\\": 520,\\n}\\n\\n\\ndef parse_args():\\n    p = argparse.ArgumentParser
…[truncated 7177 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-25T15:49:47.025373+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Read eval_openvla_l2norm_libero.py on westd-38929', 'activeForm': 'Reading eval_openvla_l2norm_libero.py', 'status': 'completed'}, {'content': 'Write eval_openvla_zeromask_libero.py with --ablation_mode', 'activeForm': 'Writing eval_openvla_zeromask_libero.py', 'status': 'completed'}, {'content': 'Dry-run validate (syntax + argparse)', 'activeForm': 'Dry-running validation', 'status': 'completed'}, {'content': 'Register as artifact', 'activeForm': 'Registering artifact', 'status': 'in_progress'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Read eval_openvla_l2norm_libero.py on westd-38929', 'activeForm': 'Reading eval_openvla_l2norm_libero.py', 'status': 'completed'}, {'content': 'Write eval_openvla_zeromask_libero.py with --ablation_mode', 'activeForm': 'Writing eval_openvla_zeromask_libero.py', 'status': 'completed'}, {'content': 'Dry-run validate (syntax + argparse)', 'activeForm': 'Dry-running validation', 'status': 'completed'}, {'content': 'Register as artifact', 'activeForm': 'Registering artifact', 'status': 'in_progress'}]"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-25T15:49:47.025583+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-25T15:49:47.025772+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts && ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/ | head",
  "description": "Verify artifacts directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "Bash",
  "tool_args": {
    "command": "mkdir -p /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts && ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/ | head",
    "description": "Verify artifacts directory exists"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-25T15:49:47.025944+00:00_

__pycache__
_lerobot_compat.py
_project
acis_overhead.json
action_divergence_closedloop.json
action_divergence_curve.pdf
action_divergence_curve.png
action_divergence_data.json
action_divergence_summary.pdf
analysis_eval_pi05_random_k09_spatial_seed42_postfix_v2.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-25T15:49:47.026118+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "scp connect.westd.seetacloud.com:/root/autodl-tmp/importance_margin_vla_compress/eval_openvla_zeromask_libero.py /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/eval_openvla_zeromask_libero.py 2>&1 | tail -3 && wc -l /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/eval_openvla_zeromask_libero.py",
  "description": "Copy script from server for artifact registration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "Bash",
  "tool_args": {
    "command": "scp connect.westd.seetacloud.com:/root/autodl-tmp/importance_margin_vla_compress/eval_openvla_zeromask_libero.py /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/eval_openvla_zeromask_libero.py 2>&1 | tail -3 && wc -l /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/eval_openvla_zeromask_libero.py",
    "description": "Copy script from server for artifact registration"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-25T15:49:47.026319+00:00_

Exit code 1
ssh_askpass: exec(/usr/bin/ssh-askpass): No such file or directory
ubuntu@connect.westd.seetacloud.com: Permission denied ().
scp: Connection closed
wc: /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/eval_openvla_zeromask_libero.py: No such file or directory

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-25T15:49:47.026685+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "eval_openvla_zeromask_libero",
  "type": "intermediate",
  "description": "OpenVLA LIBERO eval script with --ablation_mode {hard_prune, zero_mask}. Zero-mask preserves sequence length and position embeddings (only sets pruned-token values to 0), enabling clean attribution of pruning degradation to information loss vs position disruption. Validated: py_compile passes, _apply_selection unit test passes (hard_prune gathers correctly; zero_mask: kept rows unchanged, pruned rows = 0), argparse accepts all 4 mode × 2 ablation combos. Server path: /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_zeromask_libero.py on westd-38929. Not yet run on GPU (waiting for cliff-zone experiments to free GPUs).",
  "project": "importance_margin_vla_compress",
  "content_filename": "eval_openvla_zeromask_libero.py",
  "tags": "['openvla', 'libero', 'zeromask', 'ablation', 'pruning', 'position-embedding']",
  "content": "\"\"\"\nOpenVLA LIBERO Evaluation: Zero-mask vs Hard-prune Ablation.\n\nDistinguishes two failure mechanisms of token pruning:\n  (a) information loss (pruned token content gone)\n  (b) position disruption (remaining tokens shift in position embedding)\n\n--ablation_mode hard_prune : physically removes pruned tokens (sequence length shrinks)\n--ablation_mode zero_mask  : sets value of pruned tokens to 0, keeps sequence length / positions\n\nUsage:\n    python eval_openvla_zeromask_libero.py --mode l2norm_prune --ablation_mode zero_mask \\\\\n        --k_ratio 0.5 --suite libero_object\n\"\"\"\nimport argparse, io, json, math, os, sys, time\nos.environ[\"MUJOCO_GL\"] = \"egl\"\nos.environ.setdefault(\"CUDA_VISIBLE_DEVICES\", \"0\")\nos.environ[\"TRANSFORMERS_OFFLINE\"] = \"1\"\nos.environ[\"HF_HUB_OFFLINE\"] = \"1\"\n\n# Use transformers 4.40.1 for OpenVLA compat\nsys.path.insert(0, \"/root/autodl-tmp/openvla_deps\")\n\nimport numpy as np\nimport torch\nfrom PIL import Image\n\n# Import OpenVLA model code\nhf_dir = \"/root/autodl-tmp/openvla-repo/prismatic/extern/hf\"\ninit_path = os.path.join(hf_dir, \"__init__.py\")\nif not os.path.exists(init_path):\n    open(init_path, \"w\").close()\nsys.path.insert(0, \"/root/autodl-tmp/openvla-repo/prismatic/extern\")\nfrom hf.configuration_prismatic import OpenVLAConfig\nfrom hf.modeling_prismatic import OpenVLAForActionPrediction\nfrom hf.processing_prismatic import PrismaticImageProcessor, PrismaticProcessor\n\nDEVICE = torch.device(\"cuda:0\")\nCHECKPOINT_PATH = \"/root/autodl-tmp/openvla-libero-object\"\nUNNORM_KEY = \"libero_object\"\n\nSUITE_MAX_STEPS = {\n    \"libero_spatial\": 280,\n    \"libero_object\": 280,\n    \"libero_goal\": 300,\n    \"libero_10\": 520,\n}\n\n\ndef parse_args():\n    p = argparse.ArgumentParser()\n    p.add_argument(\"--mode\", choices=[\"baseline\", \"random_prune\", \"l2norm_prune\", \"attention_prune\"], default=\"baseline\")\n    p.add_argument(\"--ablation_mode\", choices=[\"hard_prune\", \"zero_mask\"], default=\"hard_prune\",\n                   help=\"hard_prune: physically remove pruned tokens. \"\n                        \"zero_mask: zero out pruned tokens, keep positions.\")\n    p.add_argument(\"--k_ratio\", type=float, default=0.5)\n    p.add_argument(\"--suite\", type=str, default=\"libero_object\")\n    p.add_argument(\"--num_episodes\", type=int, default=50)\n    p.add_argument(\"--seed\", type=int, default=7)\n    p.add_argument(\"--output\", type=str, default=None)\n    p.add_argument(\"--center_crop\", action=\"store_true\", default=True)\n    p.add_argument(\"--num_steps_wait\", type=int, default=10)\n    p.add_argument(\"--model_path\", type=str, default=\"/root/autodl-tmp/openvla-libero-object\")\n    p.add_argument(\"--unnorm_key\", type=str, default=\"libero_object\")\n    return p.parse_args()\n\n\ndef set_seed(seed):\n    torch.manual_seed(seed)\n    torch.cuda.manual_seed_all(seed)\n    np.random.seed(seed)\n    import random\n    random.seed(seed)\n\n\ndef load_model():\n    print(\"[*] Loading OpenVLA from:\", CHECKPOINT_PATH, flush=True)\n    config = OpenVLAConfig.from_pretrained(CHECKPOINT_PATH)\n    vla = OpenVLAForActionPrediction.from_pretrained(\n        CHECKPOINT_PATH,\n        config=config,\n        torch_dtype=torch.bfloat16,\n        low_cpu_mem_usage=True,\n    ).to(DEVICE)\n    with open(os.path.join(CHECKPOINT_PATH, \"dataset_statistics.json\")) as f:\n        vla.norm_stats = json.load(f)\n    vla.eval()\n\n    from transformers import AutoTokenizer\n    tokenizer = AutoTokenizer.from_pretrained(CHECKPOINT_PATH)\n    image_processor = PrismaticImageProcessor.from_pretrained(CHECKPOINT_PATH)\n    processor = PrismaticProcessor(image_processor=image_processor, tokenizer=tokenizer)\n    print(f\"[*] Model loaded, GPU: {torch.cuda.max_memory_allocated()/1e9:.1f} GB\", flush=True)\n    return vla, processor\n\n\ndef center_crop_image(image: Image.Image, crop_scale=0.9) -> Image.Image:\n    w, h = image.size\n    new_w = int(w * math.sqrt(crop_scale))\n    new_h = int(h * math.sqrt(crop_scale))\n    left = (w - new_w) // 2\n    top = (h - new_h) // 2\n    cropped = image.crop((left, top, left + new_w, top + new_h))\n    return cropped.resize((w, h), Image.LANCZOS)\n\n\ndef preprocess_image(obs, center_crop=True):\n    img = obs[\"agentview_image\"]\n    img = img[::-1, ::-1]\n    pil_img = Image.fromarray(img)\n    buf = io.BytesIO()\n    pil_img.save(buf, format=\"JPEG\")\n    buf.seek(0)\n    pil_img = Image.open(buf).convert(\"RGB\")\n    pil_img = pil_img.resize((224, 224), Image.LANCZOS)\n    if center_crop:\n        pil_img = center_crop_image(pil_img, crop_scale=0.9)\n    return pil_img\n\n\ndef get_action(vla, processor, image: Image.Image, task_label: str):\n    prompt = f\"In: What action should the robot take to {task_label.lower()}?\\nOut:\"\n    inputs = processor(prompt, image).to(DEVICE, dtype=torch.bfloat16)\n    action = vla.predict_action(**inputs, unnorm_key=UNNORM_KEY, do_sample=False)\n    return action\n\n\ndef normalize_gripper_action(action, binarize=True):\n    action[..., -1] = 2 * action[..., -1] - 1\n    if binarize:\n        action[..., -1] = np.sign(action[..., -1])\n    return action\n\n\ndef invert_gripper_action(action):\n    action[..., -1] *= -1.0\n    return action\n\n\ndef _apply_selection(output, keep_indices, ablation_mode):\n    \"\"\"Apply pruning given indices to keep.\n\n    output: (B, N, D)\n    keep_indices: (B, keep) -- indices into N dimension, already sorted ascending.\n    ablation_mode: 'hard_prune' (gather, len=keep) or 'zero_mask' (mask out\n        non-selected positions, len=N preserved).\n    \"\"\"\n    B, N, D = output.shape\n    if ablation_mode == \"hard_prune\":\n        return torch.gather(output, 1, keep_indices.unsqueeze(-1).expand(-1, -1, D))\n    # zero_mask: build (B, N) keep-mask, zero the rest, preserve shape & positions\n    mask = torch.zeros(B, N, dtype=torch.bool, device=output.device)\n    mask.scatter_(1, keep_indices, True)\n    return output * mask.unsqueeze(-1).to(output.dtype)\n\n\nclass RandomPruningHook:\n    def __init__(self, k_ratio=0.5, ablation_mode=\"hard_prune\"):\n        self.k_ratio = k_ratio\n        self.ablation_mode = ablation_mode\n        self.logged = False\n\n    def __call__(self, module, input, output):\n        B, N, D = output.shape\n        keep = int(N * self.k_ratio)\n        if keep >= N:\n            return output\n        perm = torch.randperm(N, device=output.device)[:keep].sort().values\n        keep_indices = perm.unsqueeze(0).expand(B, -1)\n        out = _apply_selection(output, keep_indices, self.ablation_mode)\n        if not self.logged:\n            print(f\"[Random {self.ablation_mode}] {N} -> keep {keep} (k={self.k_ratio})\", flush=True)\n            self.logged = True\n        return out\n\n\nclass L2NormPruningHook:\n    \"\"\"Keep top-k vision tokens ranked by L2 norm (largest norm = most important).\"\"\"\n    def __init__(self, k_ratio=0.5, ablation_mode=\"hard_prune\"):\n        self.k_ratio = k_ratio\n        self.ablation_mode = ablation_mode\n        self.logged = False\n\n    def __call__(self, module, input, output):\n        B, N, D = output.shape\n        keep = int(N * self.k_ratio)\n        if keep >= N:\n            return output\n        norms = torch.norm(output.float(), dim=-1)  # (B, N)\n        _, indices = torch.topk(norms, keep, dim=-1)\n        keep_indices = indices.sort(dim=-1).values\n        out = _apply_selection(output, keep_indices, self.ablation_mode)\n        if not self.logged:\n            print(f\"[L2 {self.ablation_mode}] {N} -> keep {keep} (k={self.k_ratio})\", flush=True)\n            self.logged = True\n        return out\n\n\nclass AttentionPruningHook:\n    \"\"\"Keep top-k vision tokens ranked by attention importance (2-layer probe).\"\"\"\n    def __init__(self, k_ratio, vla, ablation_mode=\"hard_prune\"):\n        self.k_ratio = k_ratio\n        self.vla = vla\n        self.ablation_mode = ablation_mode\n        self.logged = False\n\n    def __call__(self, module, input, output):\n        import torch.nn.functional as F\n\n        B, N, D = output.shape\n        keep = max(1, int(N * self.k_ratio))\n        if keep >= N:\n            return output\n\n        lm = self.vla.language_model.model\n        position_ids = torch.arange(N, device=output.device).unsqueeze(0).expand(B, -1)\n\n        hidden = output\n        all_attn = []\n\n        with torch.no_grad():\n            for layer_idx in range(min(2, len(lm.layers))):\n                layer = lm.layers[layer_idx]\n                normed = layer.input_layernorm(hidden)\n\n                head_dim = layer.self_attn.head_dim\n                n_q_heads = layer.self_attn.num_heads\n                n_kv_heads = layer.self_attn.num_key_value_heads\n\n                q = layer.self_attn.q_proj(normed)\n                k = layer.self_attn.k_proj(normed)\n                v = layer.self_attn.v_proj(normed)\n\n                q = q.view(B, N, n_q_heads, head_dim).transpose(1, 2)\n                k = k.view(B, N, n_kv_heads, head_dim).transpose(1, 2)\n                v = v.view(B, N, n_kv_heads, head_dim).transpose(1, 2)\n\n                cos, sin = layer.self_attn.rotary_emb(v, position_ids)\n                from transformers.models.llama.modeling_llama import rotate_half\n                q_embed = (q * cos) + (rotate_half(q) * sin)\n                k_embed = (k * cos) + (rotate_half(k) * sin)\n\n                if n_kv_heads != n_q_heads:\n                    n_rep = n_q_heads // n_kv_heads\n                    k_embed = k_embed.repeat_interleave(n_rep, dim=1)\n                    v = v.repeat_interleave(n_rep, dim=1)\n\n                attn_weights = torch.matmul(q_embed, k_embed.transpose(-2, -1)) / math.sqrt(head_dim)\n                attn_weights = F.softmax(attn_weights, dim=-1, dtype=torch.float32)\n                all_attn.append(attn_weights)\n\n                attn_out = torch.matmul(attn_weights.to(v.dtype), v)\n                attn_out = attn_out.transpose(1, 2).reshape(B, N, n_q_heads * head_dim)\n                attn_out = layer.self_attn.o_proj(attn_out)\n                hidden = hidden + attn_out\n\n                normed2 = layer.post_attention_layernorm(hidden)\n                mlp_out = layer.mlp(normed2)\n                hidden = hidden + mlp_out\n\n        avg_attn = torch.stack(all_attn).mean(dim=0).mean(dim=1)  # [B, N, N]\n        importance = avg_attn.sum(dim=1)  # [B, N]\n\n        _, indices = torch.topk(importance, keep, dim=-1)\n        keep_indices = indices.sort(dim=-1).values\n        out = _apply_selection(output, keep_indices, self.ablation_mode)\n\n        if not self.logged:\n            print(f\"[Attn {self.ablation_mode}] {N} -> keep {keep} (k={self.k_ratio}), \"\n                  f\"importance range=[{importance.min():.4f}, {importance.max():.4f}]\", flush=True)\n            self.logged = True\n\n        return out\n\n\ndef count_vision_tokens(vla, processor):\n    dummy = Image.new(\"RGB\", (224, 224), (128, 128, 128))\n    prompt = \"In: What action should the robot take to pick up the object?\\nOut:\"\n    inputs = processor(prompt, dummy).to(DEVICE, dtype=torch.bfloat16)\n    count = {}\n    def hook(m, i, o):\n        count[\"n_tokens\"] = o.shape[1]\n        count[\"hidden_dim\"] = o.shape[2]\n        return o\n    h = vla.projector.register_forward_hook(hook)\n    with torch.no_grad():\n        vla.predict_action(**inputs, unnorm_key=UNNORM_KEY, do_sample=False)\n    h.remove()\n    return count\n\n\ndef main():\n    args = parse_args()\n    global CHECKPOINT_PATH, UNNORM_KEY\n    CHECKPOINT_PATH = args.model_path\n    UNNORM_KEY = args.unnorm_key\n    set_seed(args.seed)\n    max_steps = SUITE_MAX_STEPS.get(args.suite, 300)\n\n    if args.mode == \"baseline\" and args.ablation_mode != \"hard_prune\":\n        print(f\"[!] ablation_mode={args.ablation_mode} ignored for baseline mode\", flush=True)\n\n    vla, processor = load_model()\n\n    token_info = count_vision_tokens(vla, processor)\n    print(f\"[*] Vision tokens: {token_info['n_tokens']}, dim: {token_info['hidden_dim']}\", flush=True)\n\n    hook_handle = None\n    if args.mode == \"random_prune\":\n        hook_handle = vla.projector.register_forward_hook(\n            RandomPruningHook(args.k_ratio, ablation_mode=args.ablation_mode))\n        print(f\"[*] Random pruning: k={args.k_ratio} ablation={args.ablation_mode}\", flush=True)\n    elif args.mode == \"l2norm_prune\":\n        hook_handle = vla.projector.register_forward_hook(\n            L2NormPruningHook(args.k_ratio, ablation_mode=args.ablation_mode))\n        print(f\"[*] L2 norm pruning: k={args.k_ratio} ablation={args.ablation_mode}\", flush=True)\n    elif args.mode == \"attention_prune\":\n        hook_handle = vla.projector.register_forward_hook(\n            AttentionPruningHook(args.k_ratio, vla, ablation_mode=args.ablation_mode))\n        print(f\"[*] Attention pruning: k={args.k_ratio} ablation={args.ablation_mode}\", flush=True)\n\n    from libero.libero import benchmark, get_libero_path\n    from libero.libero.envs import OffScreenRenderEnv\n\n    benchmark_dict = benchmark.get_benchmark_dict()\n    task_suite = benchmark_dict[args.suite]()\n    n_tasks = task_suite.n_tasks\n    print(f\"[*] {args.suite}: {n_tasks} tasks x {args.num_episodes} episodes = {n_tasks * args.num_episodes} total\", flush=True)\n\n    per_task_results = {}\n    total_successes = 0\n    total_episodes = 0\n    t_start = time.time()\n\n    for task_id in range(n_tasks):\n        task = task_suite.get_task(task_id)\n        task_description = task.language\n        task_bddl_file = os.path.join(\n            get_libero_path(\"bddl_files\"), task.problem_folder, task.bddl_file\n        )\n        env = OffScreenRenderEnv(\n            bddl_file_name=task_bddl_file, camera_heights=256, camera_widths=256\n        )\n        env.seed(args.seed)\n\n        task_successes = 0\n        print(f\"\\n[Task {task_id+1}/{n_tasks}] {task_description}\", flush=True)\n\n        for ep in range(args.num_episodes):\n            env.reset()\n            init_states = task_suite.get_task_init_states(task_id)\n            obs = env.set_init_state(init_states[ep])\n            done = False\n            t = 0\n\n            while t < max_steps + args.num_steps_wait:\n                try:\n                    if t < args.num_steps_wait:\n                        obs, reward, done, info = env.step([0, 0, 0, 0, 0, 0, -1])\n                        t += 1\n                        continue\n\n                    img = preprocess_image(obs, center_crop=args.center_crop)\n                    action = get_action(vla, processor, img, task_description)\n                    action = normalize_gripper_action(action, binarize=True)\n                    action = invert_gripper_action(action)\n                    obs, reward, done, info = env.step(action.tolist())\n                    if done:\n                        task_successes += 1\n                        total_successes += 1\n                        break\n                    t += 1\n                except Exception as e:\n                    print(f\"  Exception t={t}: {e}\", flush=True)\n                    break\n\n            total_episodes += 1\n            if (ep + 1) % 10 == 0:\n                elapsed = time.time() - t_start\n                eps_per_min = total_episodes / (elapsed / 60)\n                print(f\"  Ep {ep+1}/{args.num_episodes} task_sr={task_successes}/{ep+1} \"\n                      f\"({eps_per_min:.1f} eps/min)\", flush=True)\n\n        task_sr = task_successes / args.num_episodes\n        per_task_results[task_description] = {\n            \"success_rate\": task_sr,\n            \"successes\": task_successes,\n            \"episodes\": args.num_episodes,\n        }\n        print(f\"  => Task SR: {task_sr:.3f} ({task_successes}/{args.num_episodes})\", flush=True)\n        env.close()\n\n    overall_sr = total_successes / total_episodes\n    elapsed = time.time() - t_start\n    print(f\"\\n{'='*60}\", flush=True)\n    print(f\"Overall SR: {overall_sr:.4f} ({total_successes}/{total_episodes})\", flush=True)\n    print(f\"Time: {elapsed/60:.1f} min\", flush=True)\n    print(f\"{'='*60}\", flush=True)\n\n    results = {\n        \"model\": os.path.basename(CHECKPOINT_PATH),\n        \"mode\": args.mode,\n        \"ablation_mode\": args.ablation_mode,\n        \"suite\": args.suite,\n        \"k_ratio\": args.k_ratio if args.mode != \"baseline\" else None,\n        \"overall_success_rate\": overall_sr,\n        \"total_successes\": total_successes,\n        \"total_episodes\": total_episodes,\n        \"per_task\": per_task_results,\n        \"vision_tokens\": token_info,\n        \"max_steps\": max_steps,\n        \"seed\": args.seed,\n        \"elapsed_minutes\": elapsed / 60,\n        \"timestamp\": time.strftime(\"%Y-%m-%d %H:%M:%S\"),\n    }\n\n    if args.output:\n        out_path = args.output\n    else:\n        out_dir = \"/root/autodl-tmp/importance_margin_vla_compress/eval_results\"\n        os.makedirs(out_dir, exist_ok=True)\n        suite_short = args.suite.replace('libero_', '')\n        if args.mode == \"baseline\":\n            out_path = f\"{out_dir}/openvla_baseline_{suite_short}_seed{args.seed}.json\"\n        else:\n            k_str = str(args.k_ratio).replace(\".\", \"\")\n            abl_tag = \"zm\" if args.ablation_mode == \"zero_mask\" else \"hp\"\n            out_path = f\"{out_dir}/openvla_{args.mode}_{abl_tag}_k{k_str}_{suite_short}_seed{args.seed}.json\"\n\n    with open(out_path, \"w\") as f:\n        json.dump(results, f, indent=2)\n    print(f\"[*] Saved: {out_path}\", flush=True)\n\n    if hook_handle:\n        hook_handle.remove()\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "eval_openvla_zeromask_libero",
    "type": "intermediate",
    "description": "OpenVLA LIBERO eval script with --ablation_mode {hard_prune, zero_mask}. Zero-mask preserves sequence length and position embeddings (only sets pruned-token values to 0), enabling clean attribution of pruning degradation to information loss vs position disruption. Validated: py_compile passes, _apply_selection unit test passes (hard_prune gathers correctly; zero_mask: kept rows unchanged, pruned rows = 0), argparse accepts all 4 mode × 2 ablation combos. Server path: /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_zeromask_libero.py on westd-38929. Not yet run on GPU (waiting for cliff-zone experiments to free GPUs).",
    "project": "importance_margin_vla_compress",
    "content_filename": "eval_openvla_zeromask_libero.py",
    "tags": "['openvla', 'libero', 'zeromask', 'ablation', 'pruning', 'position-embedding']",
    "content": "\"\"\"\nOpenVLA LIBERO Evaluation: Zero-mask vs Hard-prune Ablation.\n\nDistinguishes two failure mechanisms of token pruning:\n  (a) information loss (pruned token content gone)\n  (b) position disruption (remaining tokens shift in position embedding)\n\n--ablation_mode hard_prune : physically removes pruned tokens (sequence length shrinks)\n--ablation_mode zero_mask  : sets value of pruned tokens to 0, keeps sequence length / positions\n\nUsage:\n    python eval_openvla_zeromask_libero.py --mode l2norm_prune --ablation_mode zero_mask \\\\\n        --k_ratio 0.5 --suite libero_object\n\"\"\"\nimport argparse, io, json, math, os, sys, time\nos.environ[\"MUJOCO_GL\"] = \"egl\"\nos.environ.setdefault(\"CUDA_VISIBLE_DEVICES\", \"0\")\nos.environ[\"TRANSFORMERS_OFFLINE\"] = \"1\"\nos.environ[\"HF_HUB_OFFLINE\"] = \"1\"\n\n# Use transformers 4.40.1 for OpenVLA compat\nsys.path.insert(0, \"/root/autodl-tmp/openvla_deps\")\n\nimport numpy as np\nimport torch\nfrom PIL import Image\n\n# Import OpenVLA model code\nhf_dir = \"/root/autodl-tmp/openvla-repo/prismatic/extern/hf\"\ninit_path = os.path.join(hf_dir, \"__init__.py\")\nif not os.path.exists(init_path):\n    open(init_path, \"w\").close()\nsys.path.insert(0, \"/root/autodl-tmp/openvla-repo/prismatic/extern\")\nfrom hf.configuration_prismatic import OpenVLAConfig\nfrom hf.modeling_prismatic import OpenVLAForActionPrediction\nfrom hf.processing_prismatic import PrismaticImageProcessor, PrismaticProcessor\n\nDEVICE = torch.device(\"cuda:0\")\nCHECKPOINT_PATH = \"/root/autodl-tmp/openvla-libero-object\"\nUNNORM_KEY = \"libero_object\"\n\nSUITE_MAX_STEPS = {\n    \"libero_spatial\": 280,\n    \"libero_object\": 280,\n    \"libero_goal\": 300,\n    \"libero_10\": 520,\n}\n\n\ndef parse_args():\n    p = argparse.ArgumentParser()\n    p.add_argument(\"--mode\", choices=[\"baseline\", \"random_prune\", \"l2norm_prune\", \"attention_prune\"], default=\"baseline\")\n    p.add_argument(\"--ablation_mode\", choices=[\"hard_prune\", \"zero_mask\"], default=\"hard_prune\",\n                   help=\"hard_prune: physically remove pruned tokens. \"\n                        \"zero_mask: zero out pruned tokens, keep positions.\")\n    p.add_argument(\"--k_ratio\", type=float, default=0.5)\n    p.add_argument(\"--suite\", type=str, default=\"libero_object\")\n    p.add_argument(\"--num_episodes\", type=int, default=50)\n    p.add_argument(\"--seed\", type=int, default=7)\n    p.add_argument(\"--output\", type=str, default=None)\n    p.add_argument(\"--center_crop\", action=\"store_true\", default=True)\n    p.add_argument(\"--num_steps_wait\", type=int, default=10)\n    p.add_argument(\"--model_path\", type=str, default=\"/root/autodl-tmp/openvla-libero-object\")\n    p.add_argument(\"--unnorm_key\", type=str, default=\"libero_object\")\n    return p.parse_args()\n\n\ndef set_seed(seed):\n    torch.manual_seed(seed)\n    torch.cuda.manual_seed_all(seed)\n    np.random.seed(seed)\n    import random\n    random.seed(seed)\n\n\ndef load_model():\n    print(\"[*] Loading OpenVLA from:\", CHECKPOINT_PATH, flush=True)\n    config = OpenVLAConfig.from_pretrained(CHECKPOINT_PATH)\n    vla = OpenVLAForActionPrediction.from_pretrained(\n        CHECKPOINT_PATH,\n        config=config,\n        torch_dtype=torch.bfloat16,\n        low_cpu_mem_usage=True,\n    ).to(DEVICE)\n    with open(os.path.join(CHECKPOINT_PATH, \"dataset_statistics.json\")) as f:\n        vla.norm_stats = json.load(f)\n    vla.eval()\n\n    from transformers import AutoTokenizer\n    tokenizer = AutoTokenizer.from_pretrained(CHECKPOINT_PATH)\n    image_processor = PrismaticImageProcessor.from_pretrained(CHECKPOINT_PATH)\n    processor = PrismaticProcessor(image_processor=image_processor, tokenizer=tokenizer)\n    print(f\"[*] Model loaded, GPU: {torch.cuda.max_memory_allocated()/1e9:.1f} GB\", flush=True)\n    return vla, processor\n\n\ndef center_crop_image(image: Image.Image, crop_scale=0.9) -> Image.Image:\n    w, h = image.size\n    new_w = int(w * math.sqrt(crop_scale))\n    new_h = int(h * math.sqrt(crop_scale))\n    left = (w - new_w) // 2\n    top = (h - new_h) // 2\n    cropped = image.crop((left, top, left + new_w, top + new_h))\n    return cropped.resize((w, h), Image.LANCZOS)\n\n\ndef preprocess_image(obs, center_crop=True):\n    img = obs[\"agentview_image\"]\n    img = img[::-1, ::-1]\n    pil_img = Image.fromarray(img)\n    buf = io.BytesIO()\n    pil_img.save(buf, format=\"JPEG\")\n    buf.seek(0)\n    pil_img = Image.open(buf).convert(\"RGB\")\n    pil_img = pil_img.resize((224, 224), Image.LANCZOS)\n    if center_crop:\n        pil_img = center_crop_image(pil_img, crop_scale=0.9)\n    return pil_img\n\n\ndef get_action(vla, processor, image: Image.Image, task_label: str):\n    prompt = f\"In: What action should the robot take to {task_label.lower()}?\\nOut:\"\n    inputs = processor(prompt, image).to(DEVICE, dtype=torch.bfloat16)\n    action = vla.predict_action(**inputs, unnorm_key=UNNORM_KEY, do_sample=False)\n    return action\n\n\ndef normalize_gripper_action(action, binarize=True):\n    action[..., -1] = 2 * action[..., -1] - 1\n    if binarize:\n        action[..., -1] = np.sign(action[..., -1])\n    return action\n\n\ndef invert_gripper_action(action):\n    action[..., -1] *= -1.0\n    return action\n\n\ndef _apply_selection(output, keep_indices, ablation_mode):\n    \"\"\"Apply pruning given indices to keep.\n\n    output: (B, N, D)\n    keep_indices: (B, keep) -- indices into N dimension, already sorted ascending.\n    ablation_mode: 'hard_prune' (gather, len=keep) or 'zero_mask' (mask out\n        non-selected positions, len=N preserved).\n    \"\"\"\n    B, N, D = output.shape\n    if ablation_mode == \"hard_prune\":\n        return torch.gather(output, 1, keep_indices.unsqueeze(-1).expand(-1, -1, D))\n    # zero_mask: build (B, N) keep-mask, zero the rest, preserve shape & positions\n    mask = torch.zeros(B, N, dtype=torch.bool, device=output.device)\n    mask.scatter_(1, keep_indices, True)\n    return output * mask.unsqueeze(-1).to(output.dtype)\n\n\nclass RandomPruningHook:\n    def __init__(self, k_ratio=0.5, ablation_mode=\"hard_prune\"):\n        self.k_ratio = k_ratio\n        self.ablation_mode = ablation_mode\n        self.logged = False\n\n    def __call__(self, module, input, output):\n        B, N, D = output.shape\n        keep = int(N * self.k_ratio)\n        if keep >= N:\n            return output\n        perm = torch.randperm(N, device=output.device)[:keep].sort().values\n        keep_indices = perm.unsqueeze(0).expand(B, -1)\n        out = _apply_selection(output, keep_indices, self.ablation_mode)\n        if not self.logged:\n            print(f\"[Random {self.ablation_mode}] {N} -> keep {keep} (k={self.k_ratio})\", flush=True)\n            self.logged = True\n        return out\n\n\nclass L2NormPruningHook:\n    \"\"\"Keep top-k vision tokens ranked by L2 norm (largest norm = most important).\"\"\"\n    def __init__(self, k_ratio=0.5, ablation_mode=\"hard_prune\"):\n        self.k_ratio = k_ratio\n        self.ablation_mode = ablation_mode\n        self.logged = False\n\n    def __call__(self, module, input, output):\n        B, N, D = output.shape\n        keep = int(N * self.k_ratio)\n        if keep >= N:\n            return output\n        norms = torch.norm(output.float(), dim=-1)  # (B, N)\n        _, indices = torch.topk(norms, keep, dim=-1)\n        keep_indices = indices.sort(dim=-1).values\n        out = _apply_selection(output, keep_indices, self.ablation_mode)\n        if not self.logged:\n            print(f\"[L2 {self.ablation_mode}] {N} -> keep {keep} (k={self.k_ratio})\", flush=True)\n            self.logged = True\n        return out\n\n\nclass AttentionPruningHook:\n    \"\"\"Keep top-k vision tokens ranked by attention importance (2-layer probe).\"\"\"\n    def __init__(self, k_ratio, vla, ablation_mode=\"hard_prune\"):\n        self.k_ratio = k_ratio\n        self.vla = vla\n        self.ablation_mode = ablation_mode\n        self.logged = False\n\n    def __call__(self, module, input, output):\n        import torch.nn.functional as F\n\n        B, N, D = output.shape\n        keep = max(1, int(N * self.k_ratio))\n        if keep >= N:\n            return output\n\n        lm = self.vla.language_model.model\n        position_ids = torch.arange(N, device=output.device).unsqueeze(0).expand(B, -1)\n\n        hidden = output\n        all_attn = []\n\n        with torch.no_grad():\n            for layer_idx in range(min(2, len(lm.layers))):\n                layer = lm.layers[layer_idx]\n                normed = layer.input_layernorm(hidden)\n\n                head_dim = layer.self_attn.head_dim\n                n_q_heads = layer.self_attn.num_heads\n                n_kv_heads = layer.self_attn.num_key_value_heads\n\n                q = layer.self_attn.q_proj(normed)\n                k = layer.self_attn.k_proj(normed)\n                v = layer.self_attn.v_proj(normed)\n\n                q = q.view(B, N, n_q_heads, head_dim).transpose(1, 2)\n                k = k.view(B, N, n_kv_heads, head_dim).transpose(1, 2)\n                v = v.view(B, N, n_kv_heads, head_dim).transpose(1, 2)\n\n                cos, sin = layer.self_attn.rotary_emb(v, position_ids)\n                from transformers.models.llama.modeling_llama import rotate_half\n                q_embed = (q * cos) + (rotate_half(q) * sin)\n                k_embed = (k * cos) + (rotate_half(k) * sin)\n\n                if n_kv_heads != n_q_heads:\n                    n_rep = n_q_heads // n_kv_heads\n                    k_embed = k_embed.repeat_interleave(n_rep, dim=1)\n                    v = v.repeat_interleave(n_rep, dim=1)\n\n                attn_weights = torch.matmul(q_embed, k_embed.transpose(-2, -1)) / math.sqrt(head_dim)\n                attn_weights = F.softmax(attn_weights, dim=-1, dtype=torch.float32)\n                all_attn.append(attn_weights)\n\n                attn_out = torch.matmul(attn_weights.to(v.dtype), v)\n                attn_out = attn_out.transpose(1, 2).reshape(B, N, n_q_heads * head_dim)\n                attn_out = layer.self_attn.o_proj(attn_out)\n                hidden = hidden + attn_out\n\n                normed2 = layer.post_attention_layernorm(hidden)\n                mlp_out = layer.mlp(normed2)\n                hidden = hidden + mlp_out\n\n        avg_attn = torch.stack(all_attn).mean(dim=0).mean(dim=1)  # [B, N, N]\n        importance = avg_attn.sum(dim=1)  # [B, N]\n\n        _, indices = torch.topk(importance, keep, dim=-1)\n        keep_indices = indices.sort(dim=-1).values\n        out = _apply_selection(output, keep_indices, self.ablation_mode)\n\n        if not self.logged:\n            print(f\"[Attn {self.ablation_mode}] {N} -> keep {keep} (k={self.k_ratio}), \"\n                  f\"importance range=[{importance.min():.4f}, {importance.max():.4f}]\", flush=True)\n            self.logged = True\n\n        return out\n\n\ndef count_vision_tokens(vla, processor):\n    dummy = Image.new(\"RGB\", (224, 224), (128, 128, 128))\n    prompt = \"In: What action should the robot take to pick up the object?\\nOut:\"\n    inputs = processor(prompt, dummy).to(DEVICE, dtype=torch.bfloat16)\n    count = {}\n    def hook(m, i, o):\n        count[\"n_tokens\"] = o.shape[1]\n        count[\"hidden_dim\"] = o.shape[2]\n        return o\n    h = vla.projector.register_forward_hook(hook)\n    with torch.no_grad():\n        vla.predict_action(**inputs, unnorm_key=UNNORM_KEY, do_sample=False)\n    h.remove()\n    return count\n\n\ndef main():\n    args = parse_args()\n    global CHECKPOINT_PATH, UNNORM_KEY\n    CHECKPOINT_PATH = args.model_path\n    UNNORM_KEY = args.unnorm_key\n    set_seed(args.seed)\n    max_steps = SUITE_MAX_STEPS.get(args.suite, 300)\n\n    if args.mode == \"baseline\" and args.ablation_mode != \"hard_prune\":\n        print(f\"[!] ablation_mode={args.ablation_mode} ignored for baseline mode\", flush=True)\n\n    vla, processor = load_model()\n\n    token_info = count_vision_tokens(vla, processor)\n    print(f\"[*] Vision tokens: {token_info['n_tokens']}, dim: {token_info['hidden_dim']}\", flush=True)\n\n    hook_handle = None\n    if args.mode == \"random_prune\":\n        hook_handle = vla.projector.register_forward_hook(\n            RandomPruningHook(args.k_ratio, ablation_mode=args.ablation_mode))\n        print(f\"[*] Random pruning: k={args.k_ratio} ablation={args.ablation_mode}\", flush=True)\n    elif args.mode == \"l2norm_prune\":\n        hook_handle = vla.projector.register_forward_hook(\n            L2NormPruningHook(args.k_ratio, ablation_mode=args.ablation_mode))\n        print(f\"[*] L2 norm pruning: k={args.k_ratio} ablation={args.ablation_mode}\", flush=True)\n    elif args.mode == \"attention_prune\":\n        hook_handle = vla.projector.register_forward_hook(\n            AttentionPruningHook(args.k_ratio, vla, ablation_mode=args.ablation_mode))\n        print(f\"[*] Attention pruning: k={args.k_ratio} ablation={args.ablation_mode}\", flush=True)\n\n    from libero.libero import benchmark, get_libero_path\n    from libero.libero.envs import OffScreenRenderEnv\n\n    benchmark_dict = benchmark.get_benchmark_dict()\n    task_suite = benchmark_dict[args.suite]()\n    n_tasks = task_suite.n_tasks\n    print(f\"[*] {args.suite}: {n_tasks} tasks x {args.num_episodes} episodes = {n_tasks * args.num_episodes} total\", flush=True)\n\n    per_task_results = {}\n    total_successes = 0\n    total_episodes = 0\n    t_start = time.time()\n\n    for task_id in range(n_tasks):\n        task = task_suite.get_task(task_id)\n        task_description = task.language\n        task_bddl_file = os.path.join(\n            get_libero_path(\"bddl_files\"), task.problem_folder, task.bddl_file\n        )\n        env = OffScreenRenderEnv(\n            bddl_file_name=task_bddl_file, camera_heights=256, camera_widths=256\n        )\n        env.seed(args.seed)\n\n        task_successes = 0\n        print(f\"\\n[Task {task_id+1}/{n_tasks}] {task_description}\", flush=True)\n\n        for ep in range(args.num_episodes):\n            env.reset()\n            init_states = task_suite.get_task_init_states(task_id)\n            obs = env.set_init_state(init_states[ep])\n            done = False\n            t = 0\n\n            while t < max_steps + args.num_steps_wait:\n                try:\n                    if t < args.num_steps_wait:\n                        obs, reward, done, info = env.step([0, 0, 0, 0, 0, 0, -1])\n                        t += 1\n                        continue\n\n                    img = preprocess_image(obs, center_crop=args.center_crop)\n                    action = get_action(vla, processor, img, task_description)\n                    action = normalize_gripper_action(action, binarize=True)\n                    action = invert_gripper_action(action)\n                    obs, reward, done, info = env.step(action.tolist())\n                    if done:\n                        task_successes += 1\n                        total_successes += 1\n                        break\n                    t += 1\n                except Exception as e:\n                    print(f\"  Exception t={t}: {e}\", flush=True)\n                    break\n\n            total_episodes += 1\n            if (ep + 1) % 10 == 0:\n                elapsed = time.time() - t_start\n                eps_per_min = total_episodes / (elapsed / 60)\n                print(f\"  Ep {ep+1}/{args.num_episodes} task_sr={task_successes}/{ep+1} \"\n                      f\"({eps_per_min:.1f} eps/min)\", flush=True)\n\n        task_sr = task_successes / args.num_episodes\n        per_task_results[task_description] = {\n            \"success_rate\": task_sr,\n            \"successes\": task_successes,\n            \"episodes\": args.num_episodes,\n        }\n        print(f\"  => Task SR: {task_sr:.3f} ({task_successes}/{args.num_episodes})\", flush=True)\n        env.close()\n\n    overall_sr = total_successes / total_episodes\n    elapsed = time.time() - t_start\n    print(f\"\\n{'='*60}\", flush=True)\n    print(f\"Overall SR: {overall_sr:.4f} ({total_successes}/{total_episodes})\", flush=True)\n    print(f\"Time: {elapsed/60:.1f} min\", flush=True)\n    print(f\"{'='*60}\", flush=True)\n\n    results = {\n        \"model\": os.path.basename(CHECKPOINT_PATH),\n        \"mode\": args.mode,\n        \"ablation_mode\": args.ablation_mode,\n        \"suite\": args.suite,\n        \"k_ratio\": args.k_ratio if args.mode != \"baseline\" else None,\n        \"overall_success_rate\": overall_sr,\n        \"total_successes\": total_successes,\n        \"total_episodes\": total_episodes,\n        \"per_task\": per_task_results,\n        \"vision_tokens\": token_info,\n        \"max_steps\": max_steps,\n        \"seed\": args.seed,\n        \"elapsed_minutes\": elapsed / 60,\n        \"timestamp\": time.strftime(\"%Y-%m-%d %H:%M:%S\"),\n    }\n\n    if args.output:\n        out_path = args.output\n    else:\n        out_dir = \"/root/autodl-tmp/importance_margin_vla_compress/eval_results\"\n        os.makedirs(out_dir, exist_ok=True)\n        suite_short = args.suite.replace('libero_', '')\n        if args.mode == \"baseline\":\n            out_path = f\"{out_dir}/openvla_baseline_{suite_short}_seed{args.seed}.json\"\n        else:\n            k_str = str(args.k_ratio).replace(\".\", \"\")\n            abl_tag = \"zm\" if args.ablation_mode == \"zero_mask\" else \"hp\"\n            out_path = f\"{out_dir}/openvla_{args.mode}_{abl_tag}_k{k_str}_{suite_short}_seed{args.seed}.json\"\n\n    with open(out_path, \"w\") as f:\n        json.dump(results, f, indent=2)\n    print(f\"[*] Saved: {out_path}\", flush=True)\n\n    if hook_handle:\n        hook_handle.remove()\n\n\nif __name__ == \"__main__\":\n    main()\n"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-25T15:49:47.027200+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260525_4ac92d\", \"name\": \"eval_openvla_zeromask_libero\", \"type\": \"intermediate\", \"description\": \"OpenVLA LIBERO eval script with --ablation_mode {hard_prune, zero_mask}. Zero-mask preserves sequence length and position embeddings (only sets pruned-token values to 0), enabling clean attribution of pruning degradation to information loss vs position disruption. Validated: py_compile passes, _apply_selection unit test passes (hard_prune gathers correctly; zero_mask: kept rows unchanged, pruned rows = 0), argparse accepts all 4 mode × 2 ablation combos. Server path: /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_zeromask_libero.py on westd-38929. Not yet run on GPU (waiting for cliff-zone experiments to free GPUs).\", \"path\": \"projects/importance_margin_vla_compress/artifacts/_project/intermediate/eval_openvla_zeromask_libero.py\", \"url\": null, \"project\": \"importance_margin_vla_compress\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-25T15:49:30.139221+00:00\", \"tags\": [\"openvla\", \"libero\", \"zeromask\", \"ablation\", \"pruning\", \"position-embedding\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-25T15:49:47.027441+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Read eval_openvla_l2norm_libero.py on westd-38929', 'activeForm': 'Reading eval_openvla_l2norm_libero.py', 'status': 'completed'}, {'content': 'Write eval_openvla_zeromask_libero.py with --ablation_mode', 'activeForm': 'Writing eval_openvla_zeromask_libero.py', 'status': 'completed'}, {'content': 'Dry-run validate (syntax + argparse)', 'activeForm': 'Dry-running validation', 'status': 'completed'}, {'content': 'Register as artifact', 'activeForm': 'Registering artifact', 'status': 'completed'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Read eval_openvla_l2norm_libero.py on westd-38929', 'activeForm': 'Reading eval_openvla_l2norm_libero.py', 'status': 'completed'}, {'content': 'Write eval_openvla_zeromask_libero.py with --ablation_mode', 'activeForm': 'Writing eval_openvla_zeromask_libero.py', 'status': 'completed'}, {'content': 'Dry-run validate (syntax + argparse)', 'activeForm': 'Dry-running validation', 'status': 'completed'}, {'content': 'Register as artifact', 'activeForm': 'Registering artifact', 'status': 'completed'}]"
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-25T15:49:47.027645+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 54 · 2026-05-25T15:49:47.027879+00:00_

完成。

**脚本**: `/root/autodl-tmp/importance_margin_vla_compress/eval_openvla_zeromask_libero.py` (westd-38929, 439 行)

**核心改动**:
- 新增 `--ablation_mode {hard_prune, zero_mask}`，默认 `hard_prune`（保持原行为）
- 抽出 `_apply_selection(output, keep_indices, ablation_mode)` 共享逻辑：`hard_prune` 走 `torch.gather`（shape 缩减），`zero_mask` 走 `scatter_`+乘 mask（shape 保留，未选中位置置 0，position embedding 不变）
- `RandomPruningHook` / `L2NormPruningHook` / `AttentionPruningHook` 均接受 `ablation_mode` 参数，三种 importance 信号 × 两种 ablation 共 6 种组合可用
- 结果 JSON 增加 `ablation_mode` 字段；输出文件名加 `_zm`/`_hp` tag 避免覆盖

**验证**（不占 GPU）:
- `python3 -m py_compile` → 通过
- `_apply_selection` 单元测试（torch CPU tensor）→ `hard_prune` gather 正确，`zero_mask` 选中行原值保留 + 未选中行为 0
- argparse 4 个有效组合通过、`--ablation_mode bogus` 被正确拒绝

**artifact id**: `art_20260525_4ac92d`

未跑 GPU eval（westd-38929 4 卡满载 cliff zone 实验，按指令等 GPU 空出再跑）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_zeromask_ablation_prep_20260525T154421"
}
```

</details>

---
