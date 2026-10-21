# code profiling script

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 55
- **Recorded user turns:** 0
- **Tool calls:** 27
- **Original source:** `logs/chats/worker_code_profiling_script_20260525T114510.jsonl`
- **Structured JSON:** [`ff6decafed39b7513f07.json`](../../sessions/ff/ff6decafed39b7513f07.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

55 recorded events

### Tool call

_source line 1 · 2026-05-25T11:49:25.352870+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_project_file",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_project_file",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-25T11:49:25.353358+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-25T11:49:25.353612+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "ls /root/autodl-tmp/importance_margin_vla_compress/eval_*.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "ls /root/autodl-tmp/importance_margin_vla_compress/eval_*.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-25T11:49:25.353861+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_acis_overhead.py\\n/root/autodl-tmp/importance_margin_vla_compress/eval_formal_bound.py\\n/root/autodl-tmp/importance_margin_vla_compress/eval_official_libero.py\\n/root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py\\n/root/autodl-tmp/importance_margin_vla_compress/eval_openvla_libero.py\\n/root/autodl-tmp/importance_margin_vla_compress/eval_openvla_pruning_simplerenv.py\\n/root/autodl-tmp/importance_margin_vla_compress/eval_openvla_simplerenv_ms3.py\\n/root/autodl-tmp/importance_margin_vla_compress/eval_openvla_smart_compress.py\\n/root/autodl-tmp/importance_margin_vla_compress/eval_pi05_pruning_libero.py\\n/root/autodl-tmp/importance_margin_vla_compress/eval_pruning_sweep.py\\n/root/autodl-tmp/importance_margin_vla_compress/eval_sim.py\\n/root/autodl-tmp/importance_margin_vla_compress/eval_smart_compress_libero.py\\n/root/autodl-tmp/importance_margin_vla_compress/eval_smolvla_pruning_metaworld.py\\n/root/autodl-tmp/importance_margin_vla_compress/eval_smolvla_pruning_official.py\\n/root/autodl-tmp/importance_margin_vla_compress/eval_success_rate.py\\n/root/autodl-tmp/importance_margin_vla_compress/eval_success_rate_libero.py\\n/root/autodl-tmp/importance_margin_vla_compress/eval_token_importance.py\\n/root/autodl-tmp/importance_margin_vla_compress/eval_xvla_attention_pruning_libero.py\\n/root/autodl-tmp/importance_margin_vla_compress/eval_xvla_pruning_libero.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.17}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-25T11:49:25.354210+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "head -200 /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "head -200 /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-25T11:49:25.354492+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nOpenVLA LIBERO Evaluation: Baseline + Random/L2-Norm Token Pruning.\\nUsage:\\n    python eval_openvla_l2norm_libero.py --mode baseline --suite libero_object\\n    python eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.5 --suite libero_object\\n\\\"\\\"\\\"\\nimport argparse, io, json, math, os, sys, time\\nos.environ[\\\"MUJOCO_GL\\\"] = \\\"egl\\\"\\nos.environ.setdefault(\\\"CUDA_VISIBLE_DEVICES\\\", \\\"0\\\")\\nos.environ[\\\"TRANSFORMERS_OFFLINE\\\"] = \\\"1\\\"\\nos.environ[\\\"HF_HUB_OFFLINE\\\"] = \\\"1\\\"\\n\\n# Use transformers 4.40.1 for OpenVLA compat\\nsys.path.insert(0, \\\"/root/autodl-tmp/openvla_deps\\\")\\n\\nimport numpy as np\\nimport torch\\nfrom PIL import Image\\n\\n# Import OpenVLA model code\\nhf_dir = \\\"/root/autodl-tmp/openvla-repo/prismatic/extern/hf\\\"\\ninit_path = os.path.join(hf_dir, \\\"__init__.py\\\")\\nif not os.path.exists(init_path):\\n    open(init_path, \\\"w\\\").close()\\nsys.path.insert(0, \\\"/root/autodl-tmp/openvla-repo/prismatic/extern\\\")\\nfrom hf.configuration_prismatic import OpenVLAConfig\\nfrom hf.modeling_prismatic import OpenVLAForActionPrediction\\nfrom hf.processing_prismatic import PrismaticImageProcessor, PrismaticProcessor\\n\\nDEVICE = torch.device(\\\"cuda:0\\\")\\nCHECKPOINT_PATH = \\\"/root/autodl-tmp/openvla-libero-object\\\"\\nUNNORM_KEY = \\\"libero_object\\\"\\n\\nSUITE_MAX_STEPS = {\\n    \\\"libero_spatial\\\": 280,\\n    \\\"libero_object\\\": 280,\\n    \\\"libero_goal\\\": 300,\\n    \\\"libero_10\\\": 520,\\n}\\n\\n\\ndef parse_args():\\n    p = argparse.ArgumentParser()\\n    p.add_argument(\\\"--mode\\\", choices=[\\\"baseline\\\", \\\"random_prune\\\", \\\"l2norm_prune\\\", \\\"attention_prune\\\"], default=\\\"baseline\\\")\\n    p.add_argument(\\\"--k_ratio\\\", type=float, default=0.5)\\n    p.add_argument(\\\"--suite\\\", type=str, default=\\\"libero_object\\\")\\n    p.add_argument(\\\"--num_epis
…[truncated 6078 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-25T11:49:25.354671+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "head -200 /root/autodl-tmp/importance_margin_vla_compress/eval_pi05_pruning_libero.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "head -200 /root/autodl-tmp/importance_margin_vla_compress/eval_pi05_pruning_libero.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-25T11:49:25.354945+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python\\n\\\"\\\"\\\"Pi0.5 LIBERO eval with vision token pruning (random / l2norm / none).\\n\\nUsage:\\n    python eval_pi05_pruning_libero.py --suite libero_object --prune_mode none\\n    python eval_pi05_pruning_libero.py --suite libero_object --prune_mode random --keep_ratio 0.5\\n    python eval_pi05_pruning_libero.py --suite libero_spatial --prune_mode l2norm --keep_ratio 0.7\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport os\\nimport sys\\nimport time as time_mod\\nimport types\\nimport logging\\nfrom pathlib import Path\\nfrom collections import deque\\n\\nos.environ[\\\"MUJOCO_GL\\\"] = \\\"egl\\\"\\nos.environ[\\\"HF_HOME\\\"] = \\\"/root/autodl-tmp/.hf_cache\\\"\\nos.environ[\\\"HF_TOKEN\\\"] = \\\"[REDACTED_HF_TOKEN]\\\"\\n\\nimport numpy as np\\nimport torch\\nimport torch._dynamo; torch._dynamo.config.disable = True\\nfrom safetensors.torch import load_file\\n\\nlogging.basicConfig(level=logging.INFO, force=True, format=\\\"%(asctime)s %(message)s\\\")\\nlog = logging.getLogger(__name__)\\n\\nSUITE_CONFIG = {\\n    \\\"libero_object\\\":  {\\\"name\\\": \\\"libero_object\\\",  \\\"max_steps\\\": 280},\\n    \\\"libero_spatial\\\":  {\\\"name\\\": \\\"libero_spatial\\\",  \\\"max_steps\\\": 400},\\n    \\\"libero_goal\\\":     {\\\"name\\\": \\\"libero_goal\\\",     \\\"max_steps\\\": 400},\\n    \\\"libero_10\\\":       {\\\"name\\\": \\\"libero_10\\\",       \\\"max_steps\\\": 520},\\n}\\n\\n\\ndef parse_args():\\n    p = argparse.ArgumentParser()\\n    p.add_argument(\\\"--model_path\\\", type=str, default=\\\"/root/autodl-tmp/pi05_libero_finetuned\\\")\\n    p.add_argument(\\\"--suite\\\", type=str, default=\\\"libero_object\\\", choices=list(SUITE_CONFIG))\\n    p.add_argument(\\\"--prune_mode\\\", type=str, default=\\\"none\\\", choices=[\\\"none\\\", \\\"random\\\", \\\"l2norm\\\"])\\n    p.add_argument(\\\"--keep_ratio\\\", type=float, default=1.0
…[truncated 6912 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-25T11:49:25.355116+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "head -200 /root/autodl-tmp/importance_margin_vla_compress/eval_xvla_pruning_libero.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "head -200 /root/autodl-tmp/importance_margin_vla_compress/eval_xvla_pruning_libero.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-25T11:49:25.355553+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"X-VLA Vision Token Pruning Evaluation on LIBERO.\\n\\nPrunes vision tokens by L2 norm after Florence2's image encoder + linear projection,\\nbefore they enter the Florence2 language encoder. Evaluates on LIBERO suites.\\n\\nFollows official X-VLA evaluation protocol:\\n  - Absolute EEF control (use_delta=False)\\n  - 20D action space: [arm1: pos(3)+rot6d(6)+grip(1)] + [arm2: zeros(10)]\\n  - 20D proprio: [pos(3)+rot6d(6)+0.0] + zeros(10)\\n  - domain_id=3 for LIBERO\\n  - Closed-loop proprio update from last predicted action\\n\\nUsage:\\n    CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl python eval_xvla_pruning_libero.py \\\\\\n        --model_path /path/to/X-VLA-Libero \\\\\\n        --suite libero_object \\\\\\n        --keep_ratio 0.5 \\\\\\n        --num_episodes 50 \\\\\\n        --gpu 0\\n\\\"\\\"\\\"\\n\\nfrom __future__ import annotations\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport sys\\nimport time as time_mod\\nfrom pathlib import Path\\nfrom functools import wraps\\n\\nos.environ.setdefault(\\\"MUJOCO_GL\\\", \\\"egl\\\")\\n\\nimport numpy as np\\nimport torch\\nfrom PIL import Image\\n\\nsys.path.insert(0, str(Path(__file__).resolve().parent))\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n    datefmt=\\\"%Y-%m-%d %H:%M:%S\\\",\\n)\\nlog = logging.getLogger(__name__)\\n\\nSUITE_MAX_STEPS = {\\n    \\\"libero_spatial\\\": 800,\\n    \\\"libero_object\\\": 800,\\n    \\\"libero_goal\\\": 800,\\n    \\\"libero_10\\\": 900,\\n    \\\"libero_90\\\": 800,\\n}\\n\\nEPS = 1e-6\\n\\n\\ndef parse_args():\\n    p = argparse.ArgumentParser(description=\\\"X-VLA pruning eval on LIBERO\\\")\\n    p.add_argument(\\\"--model_path\\\", type=str, default=\\\"2toINF/X-VLA-Libero\\\",\\n                   help=\\\"HuggingFace model path or local dir\\\")\\n    p.add_argument(\\\"--suite\\\", type=str, default=\\\"liber
…[truncated 5925 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-25T11:49:25.355856+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -n \"for step\\|for ep\\|for t \\|while\\|get_action\\|predict_action\\|step_env\\|env.step\\|infer\\|torch.no_grad\\|action_chunk\\|.infer(\" /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "grep -n \"for step\\|for ep\\|for t \\|while\\|get_action\\|predict_action\\|step_env\\|env.step\\|infer\\|torch.no_grad\\|action_chunk\\|.infer(\" /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-25T11:49:25.356077+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-25T11:49:25.356309+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -n \"for step\\|for ep\\|for t \\|while\\|action_chunk\\|.infer(\\|env.step\\|predict_action\\|torch.no_grad\\|replan\\|policy.select_action\" /root/autodl-tmp/importance_margin_vla_compress/eval_pi05_pruning_libero.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "grep -n \"for step\\|for ep\\|for t \\|while\\|action_chunk\\|.infer(\\|env.step\\|predict_action\\|torch.no_grad\\|replan\\|policy.select_action\" /root/autodl-tmp/importance_margin_vla_compress/eval_pi05_pruning_libero.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-25T11:49:25.356534+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-25T11:49:25.356738+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -n \"for step\\|for ep\\|for t \\|while\\|action_chunk\\|.infer(\\|env.step\\|predict_action\\|torch.no_grad\\|model.predict\\|model(\" /root/autodl-tmp/importance_margin_vla_compress/eval_xvla_pruning_libero.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "grep -n \"for step\\|for ep\\|for t \\|while\\|action_chunk\\|.infer(\\|env.step\\|predict_action\\|torch.no_grad\\|model.predict\\|model(\" /root/autodl-tmp/importance_margin_vla_compress/eval_xvla_pruning_libero.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-25T11:49:25.356940+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-25T11:49:25.357151+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -n \"for step\\|for ep\\|for t \\|while\\|get_action\\|predict_action\\|env.step\\|torch.no_grad\" /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "grep -n \"for step\\|for ep\\|for t \\|while\\|get_action\\|predict_action\\|env.step\\|torch.no_grad\" /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-25T11:49:25.357361+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-25T11:49:25.357555+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -n \"for step\\|for ep\\|for t \\|while\\|select_action\\|env.step\\|torch.no_grad\\|replan\" /root/autodl-tmp/importance_margin_vla_compress/eval_pi05_pruning_libero.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "grep -n \"for step\\|for ep\\|for t \\|while\\|select_action\\|env.step\\|torch.no_grad\\|replan\" /root/autodl-tmp/importance_margin_vla_compress/eval_pi05_pruning_libero.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-25T11:49:25.357762+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-25T11:49:25.357966+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -n \"for step\\|for ep\\|for t \\|while\\|predict\\|env.step\\|torch.no_grad\\|model(\" /root/autodl-tmp/importance_margin_vla_compress/eval_xvla_pruning_libero.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "grep -n \"for step\\|for ep\\|for t \\|while\\|predict\\|env.step\\|torch.no_grad\\|model(\" /root/autodl-tmp/importance_margin_vla_compress/eval_xvla_pruning_libero.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-25T11:49:25.358185+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-25T11:49:25.358441+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -nE \"for step|for ep|for t |while |get_action|predict_action|env.step|torch.no_grad\" /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "grep -nE \"for step|for ep|for t |while |get_action|predict_action|env.step|torch.no_grad\" /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-25T11:49:25.358647+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-25T11:49:25.358838+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -nE \"for step|for ep|for t |while |select_action|env.step|torch.no_grad|replan\" /root/autodl-tmp/importance_margin_vla_compress/eval_pi05_pruning_libero.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "grep -nE \"for step|for ep|for t |while |select_action|env.step|torch.no_grad|replan\" /root/autodl-tmp/importance_margin_vla_compress/eval_pi05_pruning_libero.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-25T11:49:25.359031+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-25T11:49:25.359245+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -nE \"for step|for ep|for t |while |predict|env.step|torch.no_grad|model\\(\" /root/autodl-tmp/importance_margin_vla_compress/eval_xvla_pruning_libero.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "grep -nE \"for step|for ep|for t |while |predict|env.step|torch.no_grad|model\\(\" /root/autodl-tmp/importance_margin_vla_compress/eval_xvla_pruning_libero.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-25T11:49:25.359444+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-25T11:49:25.359679+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "tail -200 /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "tail -200 /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-25T11:49:25.360104+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"                from transformers.models.llama.modeling_llama import rotate_half\\n                q_embed = (q * cos) + (rotate_half(q) * sin)\\n                k_embed = (k * cos) + (rotate_half(k) * sin)\\n\\n                if n_kv_heads != n_q_heads:\\n                    n_rep = n_q_heads // n_kv_heads\\n                    k_embed = k_embed.repeat_interleave(n_rep, dim=1)\\n                    v = v.repeat_interleave(n_rep, dim=1)\\n\\n                attn_weights = torch.matmul(q_embed, k_embed.transpose(-2, -1)) / math.sqrt(head_dim)\\n                attn_weights = F.softmax(attn_weights, dim=-1, dtype=torch.float32)\\n                all_attn.append(attn_weights)\\n\\n                attn_out = torch.matmul(attn_weights.to(v.dtype), v)\\n                attn_out = attn_out.transpose(1, 2).reshape(B, N, n_q_heads * head_dim)\\n                attn_out = layer.self_attn.o_proj(attn_out)\\n                hidden = hidden + attn_out\\n\\n                normed2 = layer.post_attention_layernorm(hidden)\\n                mlp_out = layer.mlp(normed2)\\n                hidden = hidden + mlp_out\\n\\n        avg_attn = torch.stack(all_attn).mean(dim=0).mean(dim=1)  # [B, N, N]\\n        importance = avg_attn.sum(dim=1)  # [B, N]\\n\\n        _, indices = torch.topk(importance, keep, dim=-1)\\n        indices = indices.sort(dim=-1).values\\n        pruned = torch.gather(output, 1, indices.unsqueeze(-1).expand(-1, -1, D))\\n\\n        if not self.logged:\\n            print(f\\\"[Attn Pruning] {N} -> {keep} vision tokens (k={self.k_ratio}), \\\"\\n                  f\\\"importance range=[{importance.min():.4f}, {importance.max():.4f}]\\\",\\n                  flush=True)\\n            self.logged = True\\n\\n        return pruned\\n\\n\\ndef count_vision_tokens(vla, processor):\\n    dummy = Image.new(\\\"RGB\\\", (224, 224), (128, 128, 128))\\n    prompt = \\\"In: What action should the robot take to pick up t
…[truncated 6959 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-25T11:49:25.360380+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "tail -200 /root/autodl-tmp/importance_margin_vla_compress/eval_pi05_pruning_libero.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "tail -200 /root/autodl-tmp/importance_margin_vla_compress/eval_pi05_pruning_libero.py",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-25T11:49:25.360598+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "tail -200 /root/autodl-tmp/importance_margin_vla_compress/eval_xvla_pruning_libero.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "tail -200 /root/autodl-tmp/importance_margin_vla_compress/eval_xvla_pruning_libero.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-25T11:49:25.361102+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"        image_outputs = self.paligemma.model.vision_tower(image)\\n        selected_image_feature = image_outputs.last_hidden_state\\n        features = self.paligemma.model.multi_modal_projector(selected_image_feature)\\n\\n        if features.dtype != out_dtype:\\n            features = features.to(out_dtype)\\n        return features\\n\\n    paligemma_expert.embed_image = types.MethodType(patched_embed_image, paligemma_expert)\\n    log.info(\\\"Patched embed_image\\\")\\n\\n    policy = policy.to(DEVICE)\\n    policy.eval()\\n    log.info(f\\\"Model: {sum(p.numel() for p in policy.parameters())/1e6:.1f}M params\\\")\\n\\n    N_PATCHES = (224 // 14) ** 2\\n    log.info(f\\\"Vision tokens: {N_PATCHES}/image, 3 slots -> {N_PATCHES*3} total\\\")\\n\\n    prune_fn = None\\n    if args.prune_mode == \\\"random\\\":\\n        prune_fn = prune_tokens_random\\n    elif args.prune_mode == \\\"l2norm\\\":\\n        prune_fn = prune_tokens_l2norm\\n\\n    if prune_fn is not None:\\n        original_embed_prefix = policy.model.embed_prefix\\n\\n        def pruned_embed_prefix(self_model, images, img_masks, tokens, masks):\\n            embs = []\\n            pad_masks_list = []\\n            att_masks = []\\n\\n            for img, img_mask in zip(images, img_masks, strict=True):\\n                img_emb = self_model.paligemma_with_expert.embed_image(img)\\n                bsize, num_img_embs, dim = img_emb.shape\\n\\n                img_emb, n_keep = prune_fn(img_emb, args.keep_ratio)\\n\\n                embs.append(img_emb)\\n                pad_masks_list.append(img_mask[:, None].expand(bsize, n_keep))\\n                att_masks += [0] * n_keep\\n\\n            lang_emb = self_model.paligemma_with_expert.embed_language_tokens(tokens)\\n            embs.append(lang_emb)\\n            pad_masks_list.append(masks)\\n            att_masks += [0] * lang_emb.shape[1]\\n\\n            embs = torch.cat(embs, dim=1)\\n  
…[truncated 6949 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-25T11:49:25.361547+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"        image_mask=inputs[\\\"image_mask\\\"],\\n        proprio=proprio_t,\\n        domain_id=domain_t,\\n        steps=denoise_steps,\\n    )\\n\\n    return actions.squeeze(0).float().cpu().numpy()\\n\\n\\ndef wilson_ci(successes, total, z=1.96):\\n    if total == 0:\\n        return 0.0, 0.0, 1.0\\n    p = successes / total\\n    denom = 1 + z ** 2 / total\\n    center = (p + z ** 2 / (2 * total)) / denom\\n    spread = z * np.sqrt((p * (1 - p) + z ** 2 / (4 * total)) / total) / denom\\n    return center, max(0.0, center - spread), min(1.0, center + spread)\\n\\n\\ndef run_evaluation(args):\\n    device = torch.device(f\\\"cuda:{args.gpu}\\\" if torch.cuda.is_available() else \\\"cpu\\\")\\n    max_steps = args.max_steps or SUITE_MAX_STEPS.get(args.suite, 800)\\n    output_path = Path(args.output or\\n                       f\\\"eval_results/xvla_prune_k{args.keep_ratio}_{args.suite}.json\\\")\\n\\n    log.info(\\\"Suite: %s | Device: %s | keep_ratio=%.2f | Episodes/task: %d | Max steps: %d\\\",\\n             args.suite, device, args.keep_ratio, args.num_episodes, max_steps)\\n\\n    np.random.seed(args.seed)\\n    torch.manual_seed(args.seed)\\n\\n    t0 = time_mod.time()\\n    model, processor = load_model(args.model_path, device)\\n    log.info(\\\"Model loaded in %.1fs\\\", time_mod.time() - t0)\\n\\n    dummy_img = torch.randn(1, 3, 224, 224, device=device)\\n    with torch.no_grad():\\n        dummy_feats = model.vlm._encode_image(dummy_img)\\n    n_vis_tokens = dummy_feats.shape[1]\\n    k_tokens = max(1, int(args.keep_ratio * n_vis_tokens))\\n    log.info(\\\"Vision tokens: %d total, keeping %d (%.0f%%)\\\",\\n             n_vis_tokens, k_tokens, args.keep_ratio * 100)\\n\\n    install_vision_pruning(model, args.keep_ratio, args.mode)\\n\\n    num_actions_per_chunk = model.num_actions\\n\\n    from libero.libero import benchmark, get_libero_path\\n    from libero.libero.envs import OffScreenRender
…[truncated 6108 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-25T11:49:25.361835+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -n \"def predict_actions\" /root/autodl-tmp/importance_margin_vla_compress/eval_xvla_pruning_libero.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "grep -n \"def predict_actions\" /root/autodl-tmp/importance_margin_vla_compress/eval_xvla_pruning_libero.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-25T11:49:25.362049+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"245:def predict_actions(model, processor, images, task_desc, proprio_20d, domain_id,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-25T11:49:25.362273+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "cat -n /root/autodl-tmp/importance_margin_vla_compress/eval_xvla_pruning_libero.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "cat -n /root/autodl-tmp/importance_margin_vla_compress/eval_xvla_pruning_libero.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-25T11:49:25.362750+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"     1\\t\\\"\\\"\\\"X-VLA Vision Token Pruning Evaluation on LIBERO.\\n     2\\t\\n     3\\tPrunes vision tokens by L2 norm after Florence2's image encoder + linear projection,\\n     4\\tbefore they enter the Florence2 language encoder. Evaluates on LIBERO suites.\\n     5\\t\\n     6\\tFollows official X-VLA evaluation protocol:\\n     7\\t  - Absolute EEF control (use_delta=False)\\n     8\\t  - 20D action space: [arm1: pos(3)+rot6d(6)+grip(1)] + [arm2: zeros(10)]\\n     9\\t  - 20D proprio: [pos(3)+rot6d(6)+0.0] + zeros(10)\\n    10\\t  - domain_id=3 for LIBERO\\n    11\\t  - Closed-loop proprio update from last predicted action\\n    12\\t\\n    13\\tUsage:\\n    14\\t    CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl python eval_xvla_pruning_libero.py \\\\\\n    15\\t        --model_path /path/to/X-VLA-Libero \\\\\\n    16\\t        --suite libero_object \\\\\\n    17\\t        --keep_ratio 0.5 \\\\\\n    18\\t        --num_episodes 50 \\\\\\n    19\\t        --gpu 0\\n    20\\t\\\"\\\"\\\"\\n    21\\t\\n    22\\tfrom __future__ import annotations\\n    23\\t\\n    24\\timport argparse\\n    25\\timport json\\n    26\\timport logging\\n    27\\timport os\\n    28\\timport sys\\n    29\\timport time as time_mod\\n    30\\tfrom pathlib import Path\\n    31\\tfrom functools import wraps\\n    32\\t\\n    33\\tos.environ.setdefault(\\\"MUJOCO_GL\\\", \\\"egl\\\")\\n    34\\t\\n    35\\timport numpy as np\\n    36\\timport torch\\n    37\\tfrom PIL import Image\\n    38\\t\\n    39\\tsys.path.insert(0, str(Path(__file__).resolve().parent))\\n    40\\t\\n    41\\tlogging.basicConfig(\\n    42\\t    level=logging.INFO,\\n    43\\t    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n    44\\t    datefmt=\\\"%Y-%m-%d %H:%M:%S\\\",\\n    45\\t)\\n    46\\tlog = logging.getLogger(__name__)\\n    47\\t\\n    48\\tSUITE_MAX_STEPS = {\\n    49\\t    \\\"libero_spatial\\\": 800,\\n    50\\t    \\\"libero_object\\\": 800
…[truncated 7453 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-25T11:49:25.363042+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "head -100 /root/autodl-tmp/importance_margin_vla_compress/eval_acis_overhead.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "head -100 /root/autodl-tmp/importance_margin_vla_compress/eval_acis_overhead.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-25T11:49:25.363357+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"ACIS overhead quantification: params, FLOPs, latency vs baseline SmolVLA.\\\"\\\"\\\"\\n\\nfrom __future__ import annotations\\n\\nimport argparse\\nimport json\\nimport logging\\nimport sys\\nimport time\\nfrom pathlib import Path\\n\\nimport numpy as np\\nimport torch\\nimport torch.nn.functional as F\\n\\nsys.path.insert(0, str(Path(__file__).resolve().parent))\\n\\nfrom evaluate import load_config, load_model_and_checkpoint\\nfrom train import load_dataset, make_dataloader, preprocess_batch, get_tokenizer_from_policy\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n    datefmt=\\\"%Y-%m-%d %H:%M:%S\\\",\\n)\\nlog = logging.getLogger(__name__)\\n\\n\\ndef count_params(module):\\n    return sum(p.numel() for p in module.parameters())\\n\\n\\ndef estimate_acis_flops(acis, batch_size=1, n_visual=64, n_query=50):\\n    \\\"\\\"\\\"Analytical FLOPs for ACIS cross-attention.\\\"\\\"\\\"\\n    D = acis.visual_dim\\n    A = 720\\n    H = acis.num_heads\\n    d = acis.head_dim\\n    Q = n_query\\n    N = n_visual\\n    B = batch_size\\n\\n    flops = 0\\n    flops += 2 * Q * A * D          # query_proj\\n    flops += 2 * Q * D * D          # q_proj\\n    flops += 2 * N * D * D          # k_proj\\n    flops += 2 * N * D * D          # v_proj\\n    flops += 2 * Q * N * D          # QK^T\\n    flops += 5 * H * Q * N          # softmax approx\\n    flops += 2 * N * Q * D          # transposed attn x q\\n    flops += 2 * N * D              # score_head\\n    return flops * B\\n\\n\\ndef estimate_baseline_flops(model, batch_size=1, n_visual=64, seq_len=200):\\n    \\\"\\\"\\\"Rough FLOPs for the VLM forward pass.\\\"\\\"\\\"\\n    bm = model.base_model\\n    vlm = bm.vlm_with_expert\\n    hidden_size = vlm.config.text_config.hidden_size\\n    num_layers = vlm.config.text_config.num_hidden_layers\\n    intermediate_size = getattr(vlm.config.text_
…[truncated 1677 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-25T11:49:25.363618+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/",
    "description": "List artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-25T11:49:25.363861+00:00_

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
analysis_xvla_token_importance
analyze_action_divergence.py
analyze_action_divergence_v2.py
architecture_report.md
attention_analysis.json
attention_data.npz
attention_distribution.pdf
attention_distribution.png
attention_heatmap.pdf
attention_heatmap.png
attention_metadata.json
attention_per_task.pdf
attention_per_task.png
audit_westd38929.md
audit_westd41074.md
binomial_cliff_model
c5_roboflamingo_feasibility.md
checkpoint_integrity_report.md
compute_openvla_oft_cv.py
compute_pi05_attn_entropy.py
configs
corl2026_abstract_draft_v1.md
corl2026_abstract_draft_v2.md
corl_template
degradation_curve.pdf
diag_eval_pi05_l2norm_k095_spatial.md
diag_long_postfix_failure_20250524.md
diag_westd38929_openvla_batch_fail.md
diag_xvla_random_k05_goal_seed43_crash.md
diagnose_eval_pi05_random_k085.md
diagnose_xvla_l2norm_k03_goal_v2.md
diagnosis_fullft_batch64_v2_crash.md
dream_reports
eval_formal_bound.py
eval_imm_v7_final.json
eval_oft_libero.py
eval_openvla_acis_prune.py
eval_openvla_pruning_libero.py
eval_openvla_smart_compress.py
eval_pi05_baseline.json
eval_pi05_l2norm_k07_long_seed42_v2
eval_pi05_l2norm_k09_spatial_seed43_postfix
eval_pi05_random_k085_long_seed42_postfix
eval_pi05_random_k085_object_postfix_results.md
eval_pi05_random_k09_spatial_seed42_postfix_v2
eval_random_prune_baseline
eval_results
eval_sim.py
eval_success_rate_libero.py
eval_token_importance.py
eval_xvla_attention_pruning_libero.py
eval_xvla_pruning_libero.py
eval_xvla_random_k085_long_seed42
evaluate.py
experiment_summary.csv
experiment_summary.json
fig_token_heatmap_synthetic.png
figures
gen_token_heatmap.py
geometric_prior_pruning.py
grids_positioning_for_related_work.txt
imm
imm_two_stage_v9
inference_latency_comparison
inference_laten
…[truncated 1356 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-25T11:49:25.364357+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/profile_inference_efficiency.py",
  "content": "\"\"\"Inference efficiency profiling for VLA token pruning.\n\nMeasures latency, GPU memory, and throughput across different keep ratios\nfor OpenVLA, Pi0.5, and X-VLA on LIBERO environments.\n\nUsage:\n    # OpenVLA with L2 norm pruning, sweep k_ratios\n    python profile_inference_efficiency.py --model openvla --method l2norm \\\n        --k_ratios 1.0,0.9,0.7,0.5,0.3 --suite libero_object --num_episodes 50\n\n    # Pi0.5 baseline (no pruning)\n    python profile_inference_efficiency.py --model pi05 --method baseline \\\n        --suite libero_object --num_episodes 50\n\n    # X-VLA random pruning\n    python profile_inference_efficiency.py --model xvla --method random \\\n        --k_ratios 1.0,0.9,0.7,0.5 --suite libero_object --num_episodes 50\n\nInput:\n    --model: openvla / pi05 / xvla\n    --method: baseline / random / l2norm / attention (attention only for openvla)\n    --k_ratios: comma-separated keep ratios (default: 1.0,0.95,0.9,0.85,0.7,0.5,0.3)\n    --suite: LIBERO suite name\n    --num_episodes: episodes to sample (for latency profiling, not full eval)\n    --warmup_steps: steps to skip before recording (default: 10)\n    --seed, --gpu, --output\n\nOutput CSV:\n    model,method,k_ratio,suite,latency_mean_ms,latency_std_ms,memory_peak_mb,throughput_sps,num_steps\n\nDependencies:\n    - OpenVLA: transformers 4.40.1 (from /root/autodl-tmp/openvla_deps),\n               openvla-repo (from /root/autodl-tmp/openvla-repo)\n    - Pi0.5:   lerobot with PI05Policy\n    - X-VLA:   configuration_xvla, modeling_xvla, processing_xvla (in model dir)\n    - All:     libero, torch, numpy, PIL\n\"\"\"\n\nfrom __future__ import annotations\n\nimport argparse\nimport csv\nimport io\nimport json\nimport logging\nimport math\nimport os\nimport sys\nimport time\nimport types\nfrom collections import deque\nfrom pathlib import Path\n\nos.environ[\"MUJOCO_GL\"] = \"egl\"\nos.environ.setdefault(\"TRANSFORMERS_OFFLINE\", \"1\")\nos.environ.setdefault(\"HF_HUB_OFFLINE\", \"1\")\n\nimport numpy as np\nimport torch\nfrom PIL import Image\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    datefmt=\"%Y-%m-%d %H:%M:%S\",\n)\nlog = logging.getLogger(__name__)\n\nSUITE_MAX_STEPS = {\n    \"libero_spatial\": 280,\n    \"libero_object\": 280,\n    \"libero_goal\": 300,\n    \"libero_10\": 520,\n}\n\n# X-VLA uses longer horizons\nXVLA_SUITE_MAX_STEPS = {\n    \"libero_spatial\": 800,\n    \"libero_object\": 800,\n    \"libero_goal\": 800,\n    \"libero_10\": 900,\n}\n\nDEFAULT_K_RATIOS = [1.0, 0.95, 0.9, 0.85, 0.7, 0.5, 0.3]\n\n\ndef parse_args():\n    p = argparse.ArgumentParser(description=\"Profile VLA inference efficiency\")\n    p.add_argument(\"--model\", type=str, required=True,\n                   choices=[\"openvla\", \"pi05\", \"xvla\"])\n    p.add_argument(\"--method\", type=str, default=\"baseline\",\n                   choices=[\"baseline\", \"random\", \"l2norm\", \"attention\"])\n    p.add_argument(\"--k_ratios\", type=str, default=\"1.0,0.95,0.9,0.85,0.7,0.5,0.3\")\n    p.add_argument(\"--suite\", type=str, default=\"libero_object\")\n    p.add_argument(\"--num_episodes\", type=int, default=50)\n    p.add_argument(\"--warmup_steps\", type=int, default=10)\n    p.add_argument(\"--seed\", type=int, default=42)\n    p.add_argument(\"--gpu\", type=int, default=0)\n    p.add_argument(\"--output\", type=str, default=\"profile_results.csv\")\n    # Model-specific paths\n    p.add_argument(\"--model_path\", type=str, default=None,\n                   help=\"Override default model checkpoint path\")\n    p.add_argument(\"--unnorm_key\", type=str, default=\"libero_object\",\n                   help=\"OpenVLA unnormalization key\")\n    p.add_argument(\"--replan_steps\", type=int, default=5,\n                   help=\"Pi0.5 action chunk replan interval\")\n    p.add_argument(\"--denoise_steps\", type=int, default=10,\n                   help=\"X-VLA flow matching denoising steps\")\n    p.add_argument(\"--domain_id\", type=int, default=3,\n                   help=\"X-VLA domain id for LIBERO\")\n    return p.parse_args()\n\n\nclass LatencyTracker:\n    \"\"\"Records per-step latency with CUDA synchronization.\"\"\"\n\n    def __init__(self, device):\n        self.device = device\n        self.latencies = []\n        self._start = 0.0\n\n    def start(self):\n        torch.cuda.synchronize(self.device)\n        self._start = time.perf_counter()\n\n    def end(self):\n        torch.cuda.synchronize(self.device)\n        elapsed = (time.perf_counter() - self._start) * 1000.0\n        self.latencies.append(elapsed)\n\n    def get_stats(self):\n        arr = np.array(self.latencies)\n        return {\n            \"latency_mean_ms\": float(np.mean(arr)),\n            \"latency_std_ms\": float(np.std(arr)),\n            \"throughput_sps\": float(1000.0 / np.mean(arr)) if np.mean(arr) > 0 else 0.0,\n            \"num_steps\": len(arr),\n        }\n\n\n# ---------------------------------------------------------------------------\n# OpenVLA\n# ---------------------------------------------------------------------------\n\ndef _load_openvla(model_path, device):\n    sys.path.insert(0, \"/root/autodl-tmp/openvla_deps\")\n    sys.path.insert(0, \"/root/autodl-tmp/openvla-repo/prismatic/extern\")\n\n    hf_dir = \"/root/autodl-tmp/openvla-repo/prismatic/extern/hf\"\n    init_path = os.path.join(hf_dir, \"__init__.py\")\n    if not os.path.exists(init_path):\n        open(init_path, \"w\").close()\n\n    from hf.configuration_prismatic import OpenVLAConfig\n    from hf.modeling_prismatic import OpenVLAForActionPrediction\n    from hf.processing_prismatic import PrismaticImageProcessor, PrismaticProcessor\n    from transformers import AutoTokenizer\n\n    config = OpenVLAConfig.from_pretrained(model_path)\n    vla = OpenVLAForActionPrediction.from_pretrained(\n        model_path, config=config, torch_dtype=torch.bfloat16, low_cpu_mem_usage=True,\n    ).to(device)\n    with open(os.path.join(model_path, \"dataset_statistics.json\")) as f:\n        vla.norm_stats = json.load(f)\n    vla.eval()\n\n    tokenizer = AutoTokenizer.from_pretrained(model_path)\n    image_processor = PrismaticImageProcessor.from_pretrained(model_path)\n    processor = PrismaticProcessor(image_processor=image_processor, tokenizer=tokenizer)\n    return vla, processor\n\n\ndef _install_openvla_pruning(vla, method, k_ratio):\n    \"\"\"Install pruning hook on OpenVLA projector. Returns hook handle or None.\"\"\"\n    if method == \"baseline\" or k_ratio >= 1.0:\n        return None\n\n    class _RandomHook:\n        def __init__(self, k_ratio):\n            self.k_ratio = k_ratio\n            self.logged = False\n\n        def __call__(self, module, input, output):\n            B, N, D = output.shape\n            keep = int(N * self.k_ratio)\n            indices = torch.randperm(N)[:keep].sort().values.to(output.device)\n            pruned = output[:, indices, :]\n            if not self.logged:\n                log.info(\"[Pruning] %d -> %d vision tokens (random, k=%.2f)\", N, keep, self.k_ratio)\n                self.logged = True\n            return pruned\n\n    class _L2NormHook:\n        def __init__(self, k_ratio):\n            self.k_ratio = k_ratio\n            self.logged = False\n\n        def __call__(self, module, input, output):\n            B, N, D = output.shape\n            keep = int(N * self.k_ratio)\n            norms = torch.norm(output.float(), dim=-1)\n            _, indices = torch.topk(norms, keep, dim=-1)\n            indices = indices.sort(dim=-1).values\n            pruned = torch.gather(output, 1, indices.unsqueeze(-1).expand(-1, -1, D))\n            if not self.logged:\n                log.info(\"[Pruning] %d -> %d vision tokens (l2norm, k=%.2f)\", N, keep, self.k_ratio)\n                self.logged = True\n            return pruned\n\n    class _AttentionHook:\n        def __init__(self, k_ratio, vla):\n            self.k_ratio = k_ratio\n            self.vla = vla\n            self.logged = False\n\n        def __call__(self, module, input, output):\n            import torch.nn.functional as F\n            B, N, D = output.shape\n            keep = max(1, int(N * self.k_ratio))\n            if keep >= N:\n                return output\n\n            lm = self.vla.language_model.model\n            position_ids = torch.arange(N, device=output.device).unsqueeze(0).expand(B, -1)\n            hidden = output\n            all_attn = []\n\n            with torch.no_grad():\n                for layer_idx in range(min(2, len(lm.layers))):\n                    layer = lm.layers[layer_idx]\n                    normed = layer.input_layernorm(hidden)\n                    head_dim = layer.self_attn.head_dim\n                    n_q_heads = layer.self_attn.num_heads\n                    n_kv_heads = layer.self_attn.num_key_value_heads\n\n                    q = layer.self_attn.q_proj(normed).view(B, N, n_q_heads, head_dim).transpose(1, 2)\n                    k = layer.self_attn.k_proj(normed).view(B, N, n_kv_heads, head_dim).transpose(1, 2)\n                    v = layer.self_attn.v_proj(normed).view(B, N, n_kv_heads, head_dim).transpose(1, 2)\n\n                    cos, sin = layer.self_attn.rotary_emb(v, position_ids)\n                    from transformers.models.llama.modeling_llama import rotate_half\n                    q_embed = (q * cos) + (rotate_half(q) * sin)\n                    k_embed = (k * cos) + (rotate_half(k) * sin)\n\n                    if n_kv_heads != n_q_heads:\n                        n_rep = n_q_heads // n_kv_heads\n                        k_embed = k_embed.repeat_interleave(n_rep, dim=1)\n                        v = v.repeat_interleave(n_rep, dim=1)\n\n                    attn_weights = torch.matmul(q_embed, k_embed.transpose(-2, -1)) / math.sqrt(head_dim)\n                    attn_weights = F.softmax(attn_weights, dim=-1, dtype=torch.float32)\n                    all_attn.append(attn_weights)\n\n                    attn_out = torch.matmul(attn_weights.to(v.dtype), v)\n                    attn_out = attn_out.transpose(1, 2).reshape(B, N, n_q_heads * head_dim)\n                    attn_out = layer.self_attn.o_proj(attn_out)\n                    hidden = hidden + attn_out\n                    normed2 = layer.post_attention_layernorm(hidden)\n                    mlp_out = layer.mlp(normed2)\n                    hidden = hidden + mlp_out\n\n            avg_attn = torch.stack(all_attn).mean(dim=0).mean(dim=1)\n            importance = avg_attn.sum(dim=1)\n            _, indices = torch.topk(importance, keep, dim=-1)\n            indices = indices.sort(dim=-1).values\n            pruned = torch.gather(output, 1, indices.unsqueeze(-1).expand(-1, -1, D))\n            if not self.logged:\n                log.info(\"[Pruning] %d -> %d vision tokens (attention, k=%.2f)\", N, keep, self.k_ratio)\n                self.logged = True\n            return pruned\n\n    hook_cls = {\"random\": _RandomHook, \"l2norm\": _L2NormHook, \"attention\": _AttentionHook}[method]\n    if method == \"attention\":\n        hook = hook_cls(k_ratio, vla)\n    else:\n        hook = hook_cls(k_ratio)\n    return vla.projector.register_forward_hook(hook)\n\n\ndef _openvla_preprocess_image(obs, center_crop=True):\n    img = obs[\"agentview_image\"][::-1, ::-1]\n    pil_img = Image.fromarray(img)\n    buf = io.BytesIO()\n    pil_img.save(buf, format=\"JPEG\")\n    buf.seek(0)\n    pil_img = Image.open(buf).convert(\"RGB\").resize((224, 224), Image.LANCZOS)\n    if center_crop:\n        w, h = pil_img.size\n        new_w = int(w * math.sqrt(0.9))\n        new_h = int(h * math.sqrt(0.9))\n        left, top = (w - new_w) // 2, (h - new_h) // 2\n        pil_img = pil_img.crop((left, top, left + new_w, top + new_h)).resize((w, h), Image.LANCZOS)\n    return pil_img\n\n\ndef _openvla_get_action(vla, processor, image, task_label, unnorm_key, device):\n    prompt = f\"In: What action should the robot take to {task_label.lower()}?\\nOut:\"\n    inputs = processor(prompt, image).to(device, dtype=torch.bfloat16)\n    action = vla.predict_action(**inputs, unnorm_key=unnorm_key, do_sample=False)\n    return action\n\n\ndef _normalize_and_invert_gripper(action):\n    action[..., -1] = 2 * action[..., -1] - 1\n    action[..., -1] = np.sign(action[..., -1])\n    action[..., -1] *= -1.0\n    return action\n\n\ndef profile_openvla(args, k_ratios):\n    device = torch.device(f\"cuda:{args.gpu}\")\n    model_path = args.model_path or \"/root/autodl-tmp/openvla-libero-object\"\n    max_steps = SUITE_MAX_STEPS.get(args.suite, 280)\n\n    log.info(\"Loading OpenVLA from %s ...\", model_path)\n    vla, processor = _load_openvla(model_path, device)\n\n    from libero.libero import benchmark, get_libero_path\n    from libero.libero.envs import OffScreenRenderEnv\n\n    np.random.seed(args.seed)\n    torch.manual_seed(args.seed)\n    task_suite = benchmark.get_benchmark_dict()[args.suite]()\n    n_tasks = task_suite.n_tasks\n\n    results = []\n    for k_ratio in k_ratios:\n        method = \"baseline\" if k_ratio >= 1.0 else args.method\n        log.info(\"=== OpenVLA method=%s k_ratio=%.2f ===\", method, k_ratio)\n\n        hook_handle = _install_openvla_pruning(vla, method, k_ratio)\n\n        tracker = LatencyTracker(device)\n        global_step = 0\n\n        torch.cuda.reset_peak_memory_stats(device)\n\n        for task_id in range(n_tasks):\n            task = task_suite.get_task(task_id)\n            task_desc = task.language\n            bddl = os.path.join(\n                get_libero_path(\"bddl_files\"), task.problem_folder, task.bddl_file\n            )\n            env = OffScreenRenderEnv(bddl_file_name=bddl, camera_heights=256, camera_widths=256)\n            env.seed(args.seed)\n            init_states = task_suite.get_task_init_states(task_id)\n\n            eps_this_task = min(args.num_episodes, len(init_states))\n            for ep in range(eps_this_task):\n                env.reset()\n                obs = env.set_init_state(init_states[ep])\n\n                for _ in range(10):\n                    obs, _, _, _ = env.step([0, 0, 0, 0, 0, 0, -1])\n\n                for t in range(max_steps):\n                    img = _openvla_preprocess_image(obs)\n\n                    tracker.start()\n                    action = _openvla_get_action(vla, processor, img, task_desc, args.unnorm_key, device)\n                    tracker.end()\n\n                    global_step += 1\n                    action = _normalize_and_invert_gripper(action)\n                    obs, reward, done, info = env.step(action.tolist())\n                    if done:\n                        break\n\n            env.close()\n\n        memory_peak_mb = torch.cuda.max_memory_allocated(device) / (1024 ** 2)\n\n        # Discard warmup steps\n        if len(tracker.latencies) > args.warmup_steps:\n            tracker.latencies = tracker.latencies[args.warmup_steps:]\n\n        stats = tracker.get_stats()\n        row = {\n            \"model\": \"openvla\",\n            \"method\": method,\n            \"k_ratio\": k_ratio,\n            \"suite\": args.suite,\n            \"latency_mean_ms\": round(stats[\"latency_mean_ms\"], 2),\n            \"latency_std_ms\": round(stats[\"latency_std_ms\"], 2),\n            \"memory_peak_mb\": round(memory_peak_mb, 1),\n            \"throughput_sps\": round(stats[\"throughput_sps\"], 2),\n            \"num_steps\": stats[\"num_steps\"],\n        }\n        results.append(row)\n        log.info(\"Result: %s\", row)\n\n        if hook_handle is not None:\n            hook_handle.remove()\n\n    return results\n\n\n# ---------------------------------------------------------------------------\n# Pi0.5\n# ---------------------------------------------------------------------------\n\ndef _pi05_prune_tokens_random(img_emb, keep_ratio):\n    bsize, n_tokens, dim = img_emb.shape\n    n_keep = max(1, int(n_tokens * keep_ratio))\n    indices = torch.randperm(n_tokens)[:n_keep].sort().values.to(img_emb.device)\n    return img_emb[:, indices, :], n_keep\n\n\ndef _pi05_prune_tokens_l2norm(img_emb, keep_ratio):\n    bsize, n_tokens, dim = img_emb.shape\n    n_keep = max(1, int(n_tokens * keep_ratio))\n    norms = torch.norm(img_emb[0].float(), dim=-1)\n    _, topk_idx = torch.topk(norms, n_keep)\n    topk_idx = topk_idx.sort().values\n    return img_emb[:, topk_idx, :], n_keep\n\n\ndef _load_pi05(model_path, device, method, keep_ratio):\n    os.environ.setdefault(\"HF_HOME\", \"/root/autodl-tmp/.hf_cache\")\n    torch._dynamo.config.disable = True\n\n    from lerobot.policies.pi05.modeling_pi05 import PI05Policy\n    policy = PI05Policy.from_pretrained(model_path)\n\n    paligemma_expert = policy.model.paligemma_with_expert\n\n    def patched_embed_image(self, image):\n        out_dtype = image.dtype\n        if image.dtype != torch.float32:\n            image = image.to(torch.float32)\n        image_outputs = self.paligemma.model.vision_tower(image)\n        selected_image_feature = image_outputs.last_hidden_state\n        features = self.paligemma.model.multi_modal_projector(selected_image_feature)\n        if features.dtype != out_dtype:\n            features = features.to(out_dtype)\n        return features\n\n    paligemma_expert.embed_image = types.MethodType(patched_embed_image, paligemma_expert)\n    policy = policy.to(device)\n    policy.eval()\n\n    N_PATCHES = (224 // 14) ** 2\n\n    prune_fn = None\n    if method == \"random\":\n        prune_fn = _pi05_prune_tokens_random\n    elif method == \"l2norm\":\n        prune_fn = _pi05_prune_tokens_l2norm\n\n    if prune_fn is not None and keep_ratio < 1.0:\n        def pruned_embed_prefix(self_model, images, img_masks, tokens, masks):\n            embs = []\n            pad_masks_list = []\n            att_masks = []\n            for img, img_mask in zip(images, img_masks, strict=True):\n                img_emb = self_model.paligemma_with_expert.embed_image(img)\n                bsize, num_img_embs, dim = img_emb.shape\n                img_emb, n_keep = prune_fn(img_emb, keep_ratio)\n                embs.append(img_emb)\n                pad_masks_list.append(img_mask[:, None].expand(bsize, n_keep))\n                att_masks += [0] * n_keep\n            lang_emb = self_model.paligemma_with_expert.embed_language_tokens(tokens)\n            embs.append(lang_emb)\n            pad_masks_list.append(masks)\n            att_masks += [0] * lang_emb.shape[1]\n            embs = torch.cat(embs, dim=1)\n            pad_masks_cat = torch.cat(pad_masks_list, dim=1)\n            att_masks_t = torch.tensor(att_masks, dtype=torch.bool, device=pad_masks_cat.device)\n            att_masks_t = att_masks_t[None, :].expand(bsize, len(att_masks))\n            return embs, pad_masks_cat, att_masks_t\n\n        policy.model.embed_prefix = types.MethodType(pruned_embed_prefix, policy.model)\n        log.info(\"Pi0.5 pruning installed: method=%s keep_ratio=%.2f\", method, keep_ratio)\n\n    from lerobot.policies.factory import make_pre_post_processors\n    preprocess, postprocess = make_pre_post_processors(\n        policy.config, model_path,\n        preprocessor_overrides={\"device_processor\": {\"device\": str(device)}},\n    )\n    return policy, preprocess, postprocess\n\n\ndef _quat_to_axisangle(quat):\n    q = quat.copy()\n    q[3] = np.clip(q[3], -1.0, 1.0)\n    den = np.sqrt(1.0 - q[3] ** 2)\n    if abs(den) < 1e-8:\n        return np.zeros(3, dtype=np.float32)\n    return (q[:3] * 2.0 * np.arccos(q[3]) / den).astype(np.float32)\n\n\ndef profile_pi05(args, k_ratios):\n    device = torch.device(f\"cuda:{args.gpu}\")\n    model_path = args.model_path or \"/root/autodl-tmp/pi05_libero_finetuned\"\n    max_steps = SUITE_MAX_STEPS.get(args.suite, 280)\n\n    from libero.libero import benchmark, get_libero_path\n    from libero.libero.envs import OffScreenRenderEnv\n\n    np.random.seed(args.seed)\n    torch.manual_seed(args.seed)\n    torch.cuda.manual_seed_all(args.seed)\n    task_suite = benchmark.get_benchmark_dict()[args.suite]()\n    n_tasks = task_suite.n_tasks\n\n    results = []\n    for k_ratio in k_ratios:\n        method = \"baseline\" if k_ratio >= 1.0 else args.method\n        log.info(\"=== Pi0.5 method=%s k_ratio=%.2f ===\", method, k_ratio)\n\n        policy, preprocess, postprocess = _load_pi05(model_path, device, method, k_ratio)\n\n        tracker = LatencyTracker(device)\n        global_step = 0\n\n        torch.cuda.reset_peak_memory_stats(device)\n\n        for task_id in range(n_tasks):\n            task = task_suite.get_task(task_id)\n            task_desc = task.language\n            init_states = task_suite.get_task_init_states(task_id)\n            bddl = str(Path(get_libero_path(\"bddl_files\")) / task.problem_folder / task.bddl_file)\n            env = OffScreenRenderEnv(bddl_file_name=bddl, camera_heights=256, camera_widths=256)\n            env.seed(args.seed)\n\n            eps_this_task = min(args.num_episodes, len(init_states))\n            for ep in range(eps_this_task):\n                env.reset()\n                obs = env.set_init_state(init_states[ep])\n                for _ in range(10):\n                    obs, _, _, _ = env.step([0.0] * 6 + [-1.0])\n\n                action_queue = deque()\n                for t in range(max_steps):\n                    if not action_queue:\n                        base_img = obs[\"agentview_image\"]\n                        wrist_img = obs[\"robot0_eye_in_hand_image\"]\n                        base_t = torch.from_numpy(base_img.copy()).permute(2, 0, 1).float() / 255.0\n                        base_t = torch.flip(base_t, dims=[1, 2])\n                        wrist_t = torch.from_numpy(wrist_img.copy()).permute(2, 0, 1).float() / 255.0\n                        wrist_t = torch.flip(wrist_t, dims=[1, 2])\n\n                        eef_pos = obs[\"robot0_eef_pos\"]\n                        eef_quat = obs[\"robot0_eef_quat\"]\n                        gripper_qpos = obs[\"robot0_gripper_qpos\"]\n                        state = np.concatenate([\n                            eef_pos, _quat_to_axisangle(eef_quat), gripper_qpos\n                        ]).astype(np.float32)\n                        state_t = torch.from_numpy(state)\n\n                        raw_obs = {\n                            \"observation.images.image\": base_t,\n                            \"observation.images.image2\": wrist_t,\n                            \"observation.state\": state_t,\n                            \"task\": task_desc,\n                        }\n                        batch = preprocess(raw_obs)\n\n                        tracker.start()\n                        with torch.no_grad():\n                            actions = policy.predict_action_chunk(batch)\n                        tracker.end()\n\n                        actions_unnorm = postprocess(actions)\n                        action_np = actions_unnorm[0].cpu().numpy()\n                        for a in action_np[:args.replan_steps]:\n                            action_queue.append(a[:7])\n\n                        global_step += 1\n\n                    action = action_queue.popleft()\n                    obs, reward, done, info = env.step(action.tolist())\n                    if done:\n                        break\n\n            env.close()\n\n        memory_peak_mb = torch.cuda.max_memory_allocated(device) / (1024 ** 2)\n\n        if len(tracker.latencies) > args.warmup_steps:\n            tracker.latencies = tracker.latencies[args.warmup_steps:]\n\n        stats = tracker.get_stats()\n        row = {\n            \"model\": \"pi05\",\n            \"method\": method,\n            \"k_ratio\": k_ratio,\n            \"suite\": args.suite,\n            \"latency_mean_ms\": round(stats[\"latency_mean_ms\"], 2),\n            \"latency_std_ms\": round(stats[\"latency_std_ms\"], 2),\n            \"memory_peak_mb\": round(memory_peak_mb, 1),\n            \"throughput_sps\": round(stats[\"throughput_sps\"], 2),\n            \"num_steps\": stats[\"num_steps\"],\n        }\n        results.append(row)\n        log.info(\"Result: %s\", row)\n\n        # Free model for next k_ratio (Pi0.5 patching is not easily reversible)\n        del policy\n        torch.cuda.empty_cache()\n\n    return results\n\n\n# ---------------------------------------------------------------------------\n# X-VLA\n# ---------------------------------------------------------------------------\n\nEPS_XVLA = 1e-6\n\n\ndef _load_xvla(model_path, device):\n    model_dir = str(Path(model_path).resolve())\n    sys.path.insert(0, model_dir)\n\n    from configuration_xvla import XVLAConfig\n    from modeling_xvla import XVLA\n    from processing_xvla import XVLAProcessor\n    from safetensors.torch import load_file\n\n    config = XVLAConfig.from_pretrained(model_dir)\n    model = XVLA(config)\n\n    safetensors_path = Path(model_dir) / \"model.safetensors\"\n    if safetensors_path.exists():\n        state_dict = load_file(str(safetensors_path))\n    else:\n        state_dict = torch.load(Path(model_dir) / \"pytorch_model.bin\", map_location=\"cpu\")\n    model.load_state_dict(state_dict, strict=False)\n    model = model.to(device).eval()\n\n    processor = XVLAProcessor.from_pretrained(model_dir, trust_remote_code=True)\n    if processor.tokenizer.pad_token is None:\n        processor.tokenizer.pad_token = \"&lt;pad>\"\n        processor.tokenizer.pad_token_id = 1\n\n    return model, processor\n\n\ndef _install_xvla_pruning(model, keep_ratio, mode):\n    from functools import wraps\n\n    if keep_ratio >= 1.0:\n        return\n\n    original_encode = model.vlm._encode_image\n\n    @wraps(original_encode)\n    def pruned_encode(pixel_values):\n        features = original_encode(pixel_values)\n        N = features.shape[1]\n        k = max(1, int(keep_ratio * N))\n        if k >= N:\n            return features\n        if mode == \"l2norm\":\n            norms = features.norm(dim=-1)\n            _, indices = norms.topk(k, dim=-1)\n        elif mode == \"random\":\n            indices = torch.stack([\n                torch.randperm(N)[:k] for _ in range(features.shape[0])\n            ], dim=0)\n        else:\n            return features\n        indices_sorted = indices.sort(dim=-1).values.to(features.device)\n        pruned = features.gather(\n            1, indices_sorted.unsqueeze(-1).expand(-1, -1, features.shape[-1])\n        )\n        return pruned\n\n    model.vlm._encode_image = pruned_encode\n    model._original_encode_image = original_encode\n    log.info(\"X-VLA pruning installed: keep_ratio=%.2f mode=%s\", keep_ratio, mode)\n\n\ndef _xvla_restore_encode(model):\n    if hasattr(model, \"_original_encode_image\"):\n        model.vlm._encode_image = model._original_encode_image\n        del model._original_encode_image\n\n\ndef _xvla_mat_to_rot6d(R):\n    return np.concatenate([R[:3, 0], R[:3, 1]], axis=-1).astype(np.float32)\n\n\ndef _xvla_rot6d_to_axis_angle(r6d):\n    import robosuite.utils.transform_utils as T\n    single = r6d.ndim == 1\n    if single:\n        r6d = r6d[None, :]\n    a1 = r6d[:, 0:3]\n    a2 = r6d[:, 3:6]\n    b1 = a1 / (np.linalg.norm(a1, axis=-1, keepdims=True) + EPS_XVLA)\n    dot_prod = np.sum(b1 * a2, axis=-1, keepdims=True)\n    b2_orth = a2 - dot_prod * b1\n    b2 = b2_orth / (np.linalg.norm(b2_orth, axis=-1, keepdims=True) + EPS_XVLA)\n    b3 = np.cross(b1, b2, axis=-1)\n    R = np.stack([b1, b2, b3], axis=-1)\n    results = []\n    for i in range(R.shape[0]):\n        quat = T.mat2quat(R[i])\n        aa = T.quat2axisangle(quat)\n        results.append(aa)\n    result = np.stack(results, axis=0)\n    return result[0] if single else result\n\n\ndef _xvla_extract_proprio_20d(env):\n    robot = env.env.robots[0]\n    ee_pos = robot.controller.ee_pos.copy()\n    ee_ori_mat = robot.controller.ee_ori_mat.copy()\n    rot6d = _xvla_mat_to_rot6d(ee_ori_mat)\n    arm1 = np.concatenate([ee_pos, rot6d, np.array([0.0], dtype=np.float32)])\n    arm2 = np.zeros(10, dtype=np.float32)\n    return np.concatenate([arm1, arm2])\n\n\ndef _xvla_get_images_from_obs(obs):\n    images = []\n    for key in [\"agentview_image\", \"robot0_eye_in_hand_image\"]:\n        if key in obs:\n            img = obs[key]\n            img = img[::-1, ::-1]\n            pil = Image.fromarray(img).convert(\"RGB\")\n            images.append(pil)\n    return images\n\n\ndef _xvla_predict_actions(model, processor, images, task_desc, proprio_20d,\n                          domain_id, device, denoise_steps):\n    inputs = processor(\n        images=images,\n        text=task_desc,\n        return_tensors=\"pt\",\n        padding=True,\n    )\n    inputs = {k: v.to(device) if isinstance(v, torch.Tensor) else v for k, v in inputs.items()}\n\n    proprio_t = torch.tensor(proprio_20d, dtype=torch.float32, device=device).unsqueeze(0)\n    domain_t = torch.tensor([domain_id], dtype=torch.long, device=device)\n\n    with torch.no_grad():\n        actions = model.predict_action(\n            input_ids=inputs[\"input_ids\"],\n            pixel_values=inputs[\"pixel_values\"],\n            image_mask=inputs[\"image_mask\"],\n            proprio=proprio_t,\n            domain_id=domain_t,\n            steps=denoise_steps,\n        )\n    return actions.squeeze(0).float().cpu().numpy()\n\n\ndef _xvla_decode_action_20d_to_7d(raw_actions):\n    results = []\n    for act in raw_actions:\n        pos = act[:3]\n        rot6d = act[3:9]\n        grip = act[9]\n        aa = _xvla_rot6d_to_axis_angle(rot6d)\n        action_7d = np.concatenate([pos, aa, [grip]])\n        results.append(action_7d.astype(np.float32))\n    return np.array(results)\n\n\ndef profile_xvla(args, k_ratios):\n    device = torch.device(f\"cuda:{args.gpu}\")\n    model_path = args.model_path or \"/root/autodl-tmp/X-VLA-Libero\"\n    max_steps = XVLA_SUITE_MAX_STEPS.get(args.suite, 800)\n\n    log.info(\"Loading X-VLA from %s ...\", model_path)\n    model, processor = _load_xvla(model_path, device)\n\n    num_actions_per_chunk = model.num_actions\n\n    from libero.libero import benchmark, get_libero_path\n    from libero.libero.envs import OffScreenRenderEnv\n\n    np.random.seed(args.seed)\n    torch.manual_seed(args.seed)\n    task_suite = benchmark.get_benchmark(args.suite)()\n    n_tasks = task_suite.n_tasks\n\n    results = []\n    for k_ratio in k_ratios:\n        method = \"baseline\" if k_ratio >= 1.0 else args.method\n        log.info(\"=== X-VLA method=%s k_ratio=%.2f ===\", method, k_ratio)\n\n        _xvla_restore_encode(model)\n        _install_xvla_pruning(model, k_ratio, method)\n\n        tracker = LatencyTracker(device)\n        global_step = 0\n\n        torch.cuda.reset_peak_memory_stats(device)\n\n        for task_id in range(n_tasks):\n            task = task_suite.get_task(task_id)\n            task_desc = task.language\n            task_bddl = os.path.join(\n                get_libero_path(\"bddl_files\"), task.problem_folder, task.bddl_file\n            )\n            init_states = task_suite.get_task_init_states(task_id)\n\n            eps_this_task = min(args.num_episodes, len(init_states))\n            for ep in range(eps_this_task):\n                env = OffScreenRenderEnv(\n                    bddl_file_name=task_bddl, camera_heights=256, camera_widths=256,\n                )\n                env.seed(args.seed + ep + 100)\n                obs = env.reset()\n                init_state_id = ep % init_states.shape[0]\n                obs = env.set_init_state(init_states[init_state_id])\n\n                for _ in range(10):\n                    obs, _, _, _ = env.step(np.array([0.0] * 6 + [-1.0], dtype=np.float32))\n\n                for robot in env.env.robots:\n                    robot.controller.use_delta = False\n\n                action_queue = []\n                proprio_state = None\n\n                for step_idx in range(max_steps):\n                    if not action_queue:\n                        proprio_20d = _xvla_extract_proprio_20d(env)\n                        if proprio_state is not None:\n                            proprio_20d[:9] = proprio_state[:9]\n\n                        images = _xvla_get_images_from_obs(obs)\n\n                        tracker.start()\n                        raw_actions = _xvla_predict_actions(\n                            model, processor, images, task_desc, proprio_20d,\n                            args.domain_id, device, args.denoise_steps,\n                        )\n                        tracker.end()\n\n                        proprio_state = proprio_20d.copy()\n                        proprio_state[:9] = raw_actions[-1, :9].copy()\n\n                        actions_7d = _xvla_decode_action_20d_to_7d(raw_actions)\n                        action_queue = list(actions_7d)\n                        global_step += 1\n\n                    action = action_queue.pop(0)\n                    obs, reward, done, info = env.step(action)\n\n                    if done or reward > 0.5:\n                        break\n\n                env.close()\n\n        memory_peak_mb = torch.cuda.max_memory_allocated(device) / (1024 ** 2)\n\n        if len(tracker.latencies) > args.warmup_steps:\n            tracker.latencies = tracker.latencies[args.warmup_steps:]\n\n        stats = tracker.get_stats()\n        row = {\n            \"model\": \"xvla\",\n            \"method\": method,\n            \"k_ratio\": k_ratio,\n            \"suite\": args.suite,\n            \"latency_mean_ms\": round(stats[\"latency_mean_ms\"], 2),\n            \"latency_std_ms\": round(stats[\"latency_std_ms\"], 2),\n            \"memory_peak_mb\": round(memory_peak_mb, 1),\n            \"throughput_sps\": round(stats[\"throughput_sps\"], 2),\n            \"num_steps\": stats[\"num_steps\"],\n        }\n        results.append(row)\n        log.info(\"Result: %s\", row)\n\n    return results\n\n\n# ---------------------------------------------------------------------------\n# Main\n# ---------------------------------------------------------------------------\n\nPROFILE_FN = {\n    \"openvla\": profile_openvla,\n    \"pi05\": profile_pi05,\n    \"xvla\": profile_xvla,\n}\n\n\ndef main():\n    args = parse_args()\n    os.environ[\"CUDA_VISIBLE_DEVICES\"] = str(args.gpu)\n\n    k_ratios = [float(x) for x in args.k_ratios.split(\",\")]\n    log.info(\"Model: %s | Method: %s | k_ratios: %s | Suite: %s | Episodes: %d\",\n             args.model, args.method, k_ratios, args.suite, args.num_episodes)\n\n    profile_fn = PROFILE_FN[args.model]\n    results = profile_fn(args, k_ratios)\n\n    fieldnames = [\n        \"model\", \"method\", \"k_ratio\", \"suite\",\n        \"latency_mean_ms\", \"latency_std_ms\", \"memory_peak_mb\",\n        \"throughput_sps\", \"num_steps\",\n    ]\n    output_path = args.output\n    write_header = not os.path.exists(output_path)\n    with open(output_path, \"a\", newline=\"\") as f:\n        writer = csv.DictWriter(f, fieldnames=fieldnames)\n        if write_header:\n            writer.writeheader()\n        for row in results:\n            writer.writerow(row)\n\n    log.info(\"Results appended to %s (%d rows)\", output_path, len(results))\n\n    for row in results:\n        log.info(\"  %s %s k=%.2f: %.1f±%.1f ms, %.0f MB, %.1f sps (%d steps)\",\n                 row[\"model\"], row[\"method\"], row[\"k_ratio\"],\n                 row[\"latency_mean_ms\"], row[\"latency_std_ms\"],\n                 row[\"memory_peak_mb\"], row[\"throughput_sps\"], row[\"num_steps\"])\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/profile_inference_efficiency.py",
    "content": "\"\"\"Inference efficiency profiling for VLA token pruning.\n\nMeasures latency, GPU memory, and throughput across different keep ratios\nfor OpenVLA, Pi0.5, and X-VLA on LIBERO environments.\n\nUsage:\n    # OpenVLA with L2 norm pruning, sweep k_ratios\n    python profile_inference_efficiency.py --model openvla --method l2norm \\\n        --k_ratios 1.0,0.9,0.7,0.5,0.3 --suite libero_object --num_episodes 50\n\n    # Pi0.5 baseline (no pruning)\n    python profile_inference_efficiency.py --model pi05 --method baseline \\\n        --suite libero_object --num_episodes 50\n\n    # X-VLA random pruning\n    python profile_inference_efficiency.py --model xvla --method random \\\n        --k_ratios 1.0,0.9,0.7,0.5 --suite libero_object --num_episodes 50\n\nInput:\n    --model: openvla / pi05 / xvla\n    --method: baseline / random / l2norm / attention (attention only for openvla)\n    --k_ratios: comma-separated keep ratios (default: 1.0,0.95,0.9,0.85,0.7,0.5,0.3)\n    --suite: LIBERO suite name\n    --num_episodes: episodes to sample (for latency profiling, not full eval)\n    --warmup_steps: steps to skip before recording (default: 10)\n    --seed, --gpu, --output\n\nOutput CSV:\n    model,method,k_ratio,suite,latency_mean_ms,latency_std_ms,memory_peak_mb,throughput_sps,num_steps\n\nDependencies:\n    - OpenVLA: transformers 4.40.1 (from /root/autodl-tmp/openvla_deps),\n               openvla-repo (from /root/autodl-tmp/openvla-repo)\n    - Pi0.5:   lerobot with PI05Policy\n    - X-VLA:   configuration_xvla, modeling_xvla, processing_xvla (in model dir)\n    - All:     libero, torch, numpy, PIL\n\"\"\"\n\nfrom __future__ import annotations\n\nimport argparse\nimport csv\nimport io\nimport json\nimport logging\nimport math\nimport os\nimport sys\nimport time\nimport types\nfrom collections import deque\nfrom pathlib import Path\n\nos.environ[\"MUJOCO_GL\"] = \"egl\"\nos.environ.setdefault(\"TRANSFORMERS_OFFLINE\", \"1\")\nos.environ.setdefault(\"HF_HUB_OFFLINE\", \"1\")\n\nimport numpy as np\nimport torch\nfrom PIL import Image\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    datefmt=\"%Y-%m-%d %H:%M:%S\",\n)\nlog = logging.getLogger(__name__)\n\nSUITE_MAX_STEPS = {\n    \"libero_spatial\": 280,\n    \"libero_object\": 280,\n    \"libero_goal\": 300,\n    \"libero_10\": 520,\n}\n\n# X-VLA uses longer horizons\nXVLA_SUITE_MAX_STEPS = {\n    \"libero_spatial\": 800,\n    \"libero_object\": 800,\n    \"libero_goal\": 800,\n    \"libero_10\": 900,\n}\n\nDEFAULT_K_RATIOS = [1.0, 0.95, 0.9, 0.85, 0.7, 0.5, 0.3]\n\n\ndef parse_args():\n    p = argparse.ArgumentParser(description=\"Profile VLA inference efficiency\")\n    p.add_argument(\"--model\", type=str, required=True,\n                   choices=[\"openvla\", \"pi05\", \"xvla\"])\n    p.add_argument(\"--method\", type=str, default=\"baseline\",\n                   choices=[\"baseline\", \"random\", \"l2norm\", \"attention\"])\n    p.add_argument(\"--k_ratios\", type=str, default=\"1.0,0.95,0.9,0.85,0.7,0.5,0.3\")\n    p.add_argument(\"--suite\", type=str, default=\"libero_object\")\n    p.add_argument(\"--num_episodes\", type=int, default=50)\n    p.add_argument(\"--warmup_steps\", type=int, default=10)\n    p.add_argument(\"--seed\", type=int, default=42)\n    p.add_argument(\"--gpu\", type=int, default=0)\n    p.add_argument(\"--output\", type=str, default=\"profile_results.csv\")\n    # Model-specific paths\n    p.add_argument(\"--model_path\", type=str, default=None,\n                   help=\"Override default model checkpoint path\")\n    p.add_argument(\"--unnorm_key\", type=str, default=\"libero_object\",\n                   help=\"OpenVLA unnormalization key\")\n    p.add_argument(\"--replan_steps\", type=int, default=5,\n                   help=\"Pi0.5 action chunk replan interval\")\n    p.add_argument(\"--denoise_steps\", type=int, default=10,\n                   help=\"X-VLA flow matching denoising steps\")\n    p.add_argument(\"--domain_id\", type=int, default=3,\n                   help=\"X-VLA domain id for LIBERO\")\n    return p.parse_args()\n\n\nclass LatencyTracker:\n    \"\"\"Records per-step latency with CUDA synchronization.\"\"\"\n\n    def __init__(self, device):\n        self.device = device\n        self.latencies = []\n        self._start = 0.0\n\n    def start(self):\n        torch.cuda.synchronize(self.device)\n        self._start = time.perf_counter()\n\n    def end(self):\n        torch.cuda.synchronize(self.device)\n        elapsed = (time.perf_counter() - self._start) * 1000.0\n        self.latencies.append(elapsed)\n\n    def get_stats(self):\n        arr = np.array(self.latencies)\n        return {\n            \"latency_mean_ms\": float(np.mean(arr)),\n            \"latency_std_ms\": float(np.std(arr)),\n            \"throughput_sps\": float(1000.0 / np.mean(arr)) if np.mean(arr) > 0 else 0.0,\n            \"num_steps\": len(arr),\n        }\n\n\n# ---------------------------------------------------------------------------\n# OpenVLA\n# ---------------------------------------------------------------------------\n\ndef _load_openvla(model_path, device):\n    sys.path.insert(0, \"/root/autodl-tmp/openvla_deps\")\n    sys.path.insert(0, \"/root/autodl-tmp/openvla-repo/prismatic/extern\")\n\n    hf_dir = \"/root/autodl-tmp/openvla-repo/prismatic/extern/hf\"\n    init_path = os.path.join(hf_dir, \"__init__.py\")\n    if not os.path.exists(init_path):\n        open(init_path, \"w\").close()\n\n    from hf.configuration_prismatic import OpenVLAConfig\n    from hf.modeling_prismatic import OpenVLAForActionPrediction\n    from hf.processing_prismatic import PrismaticImageProcessor, PrismaticProcessor\n    from transformers import AutoTokenizer\n\n    config = OpenVLAConfig.from_pretrained(model_path)\n    vla = OpenVLAForActionPrediction.from_pretrained(\n        model_path, config=config, torch_dtype=torch.bfloat16, low_cpu_mem_usage=True,\n    ).to(device)\n    with open(os.path.join(model_path, \"dataset_statistics.json\")) as f:\n        vla.norm_stats = json.load(f)\n    vla.eval()\n\n    tokenizer = AutoTokenizer.from_pretrained(model_path)\n    image_processor = PrismaticImageProcessor.from_pretrained(model_path)\n    processor = PrismaticProcessor(image_processor=image_processor, tokenizer=tokenizer)\n    return vla, processor\n\n\ndef _install_openvla_pruning(vla, method, k_ratio):\n    \"\"\"Install pruning hook on OpenVLA projector. Returns hook handle or None.\"\"\"\n    if method == \"baseline\" or k_ratio >= 1.0:\n        return None\n\n    class _RandomHook:\n        def __init__(self, k_ratio):\n            self.k_ratio = k_ratio\n            self.logged = False\n\n        def __call__(self, module, input, output):\n            B, N, D = output.shape\n            keep = int(N * self.k_ratio)\n            indices = torch.randperm(N)[:keep].sort().values.to(output.device)\n            pruned = output[:, indices, :]\n            if not self.logged:\n                log.info(\"[Pruning] %d -> %d vision tokens (random, k=%.2f)\", N, keep, self.k_ratio)\n                self.logged = True\n            return pruned\n\n    class _L2NormHook:\n        def __init__(self, k_ratio):\n            self.k_ratio = k_ratio\n            self.logged = False\n\n        def __call__(self, module, input, output):\n            B, N, D = output.shape\n            keep = int(N * self.k_ratio)\n            norms = torch.norm(output.float(), dim=-1)\n            _, indices = torch.topk(norms, keep, dim=-1)\n            indices = indices.sort(dim=-1).values\n            pruned = torch.gather(output, 1, indices.unsqueeze(-1).expand(-1, -1, D))\n            if not self.logged:\n                log.info(\"[Pruning] %d -> %d vision tokens (l2norm, k=%.2f)\", N, keep, self.k_ratio)\n                self.logged = True\n            return pruned\n\n    class _AttentionHook:\n        def __init__(self, k_ratio, vla):\n            self.k_ratio = k_ratio\n            self.vla = vla\n            self.logged = False\n\n        def __call__(self, module, input, output):\n            import torch.nn.functional as F\n            B, N, D = output.shape\n            keep = max(1, int(N * self.k_ratio))\n            if keep >= N:\n                return output\n\n            lm = self.vla.language_model.model\n            position_ids = torch.arange(N, device=output.device).unsqueeze(0).expand(B, -1)\n            hidden = output\n            all_attn = []\n\n            with torch.no_grad():\n                for layer_idx in range(min(2, len(lm.layers))):\n                    layer = lm.layers[layer_idx]\n                    normed = layer.input_layernorm(hidden)\n                    head_dim = layer.self_attn.head_dim\n                    n_q_heads = layer.self_attn.num_heads\n                    n_kv_heads = layer.self_attn.num_key_value_heads\n\n                    q = layer.self_attn.q_proj(normed).view(B, N, n_q_heads, head_dim).transpose(1, 2)\n                    k = layer.self_attn.k_proj(normed).view(B, N, n_kv_heads, head_dim).transpose(1, 2)\n                    v = layer.self_attn.v_proj(normed).view(B, N, n_kv_heads, head_dim).transpose(1, 2)\n\n                    cos, sin = layer.self_attn.rotary_emb(v, position_ids)\n                    from transformers.models.llama.modeling_llama import rotate_half\n                    q_embed = (q * cos) + (rotate_half(q) * sin)\n                    k_embed = (k * cos) + (rotate_half(k) * sin)\n\n                    if n_kv_heads != n_q_heads:\n                        n_rep = n_q_heads // n_kv_heads\n                        k_embed = k_embed.repeat_interleave(n_rep, dim=1)\n                        v = v.repeat_interleave(n_rep, dim=1)\n\n                    attn_weights = torch.matmul(q_embed, k_embed.transpose(-2, -1)) / math.sqrt(head_dim)\n                    attn_weights = F.softmax(attn_weights, dim=-1, dtype=torch.float32)\n                    all_attn.append(attn_weights)\n\n                    attn_out = torch.matmul(attn_weights.to(v.dtype), v)\n                    attn_out = attn_out.transpose(1, 2).reshape(B, N, n_q_heads * head_dim)\n                    attn_out = layer.self_attn.o_proj(attn_out)\n                    hidden = hidden + attn_out\n                    normed2 = layer.post_attention_layernorm(hidden)\n                    mlp_out = layer.mlp(normed2)\n                    hidden = hidden + mlp_out\n\n            avg_attn = torch.stack(all_attn).mean(dim=0).mean(dim=1)\n            importance = avg_attn.sum(dim=1)\n            _, indices = torch.topk(importance, keep, dim=-1)\n            indices = indices.sort(dim=-1).values\n            pruned = torch.gather(output, 1, indices.unsqueeze(-1).expand(-1, -1, D))\n            if not self.logged:\n                log.info(\"[Pruning] %d -> %d vision tokens (attention, k=%.2f)\", N, keep, self.k_ratio)\n                self.logged = True\n            return pruned\n\n    hook_cls = {\"random\": _RandomHook, \"l2norm\": _L2NormHook, \"attention\": _AttentionHook}[method]\n    if method == \"attention\":\n        hook = hook_cls(k_ratio, vla)\n    else:\n        hook = hook_cls(k_ratio)\n    return vla.projector.register_forward_hook(hook)\n\n\ndef _openvla_preprocess_image(obs, center_crop=True):\n    img = obs[\"agentview_image\"][::-1, ::-1]\n    pil_img = Image.fromarray(img)\n    buf = io.BytesIO()\n    pil_img.save(buf, format=\"JPEG\")\n    buf.seek(0)\n    pil_img = Image.open(buf).convert(\"RGB\").resize((224, 224), Image.LANCZOS)\n    if center_crop:\n        w, h = pil_img.size\n        new_w = int(w * math.sqrt(0.9))\n        new_h = int(h * math.sqrt(0.9))\n        left, top = (w - new_w) // 2, (h - new_h) // 2\n        pil_img = pil_img.crop((left, top, left + new_w, top + new_h)).resize((w, h), Image.LANCZOS)\n    return pil_img\n\n\ndef _openvla_get_action(vla, processor, image, task_label, unnorm_key, device):\n    prompt = f\"In: What action should the robot take to {task_label.lower()}?\\nOut:\"\n    inputs = processor(prompt, image).to(device, dtype=torch.bfloat16)\n    action = vla.predict_action(**inputs, unnorm_key=unnorm_key, do_sample=False)\n    return action\n\n\ndef _normalize_and_invert_gripper(action):\n    action[..., -1] = 2 * action[..., -1] - 1\n    action[..., -1] = np.sign(action[..., -1])\n    action[..., -1] *= -1.0\n    return action\n\n\ndef profile_openvla(args, k_ratios):\n    device = torch.device(f\"cuda:{args.gpu}\")\n    model_path = args.model_path or \"/root/autodl-tmp/openvla-libero-object\"\n    max_steps = SUITE_MAX_STEPS.get(args.suite, 280)\n\n    log.info(\"Loading OpenVLA from %s ...\", model_path)\n    vla, processor = _load_openvla(model_path, device)\n\n    from libero.libero import benchmark, get_libero_path\n    from libero.libero.envs import OffScreenRenderEnv\n\n    np.random.seed(args.seed)\n    torch.manual_seed(args.seed)\n    task_suite = benchmark.get_benchmark_dict()[args.suite]()\n    n_tasks = task_suite.n_tasks\n\n    results = []\n    for k_ratio in k_ratios:\n        method = \"baseline\" if k_ratio >= 1.0 else args.method\n        log.info(\"=== OpenVLA method=%s k_ratio=%.2f ===\", method, k_ratio)\n\n        hook_handle = _install_openvla_pruning(vla, method, k_ratio)\n\n        tracker = LatencyTracker(device)\n        global_step = 0\n\n        torch.cuda.reset_peak_memory_stats(device)\n\n        for task_id in range(n_tasks):\n            task = task_suite.get_task(task_id)\n            task_desc = task.language\n            bddl = os.path.join(\n                get_libero_path(\"bddl_files\"), task.problem_folder, task.bddl_file\n            )\n            env = OffScreenRenderEnv(bddl_file_name=bddl, camera_heights=256, camera_widths=256)\n            env.seed(args.seed)\n            init_states = task_suite.get_task_init_states(task_id)\n\n            eps_this_task = min(args.num_episodes, len(init_states))\n            for ep in range(eps_this_task):\n                env.reset()\n                obs = env.set_init_state(init_states[ep])\n\n                for _ in range(10):\n                    obs, _, _, _ = env.step([0, 0, 0, 0, 0, 0, -1])\n\n                for t in range(max_steps):\n                    img = _openvla_preprocess_image(obs)\n\n                    tracker.start()\n                    action = _openvla_get_action(vla, processor, img, task_desc, args.unnorm_key, device)\n                    tracker.end()\n\n                    global_step += 1\n                    action = _normalize_and_invert_gripper(action)\n                    obs, reward, done, info = env.step(action.tolist())\n                    if done:\n                        break\n\n            env.close()\n\n        memory_peak_mb = torch.cuda.max_memory_allocated(device) / (1024 ** 2)\n\n        # Discard warmup steps\n        if len(tracker.latencies) > args.warmup_steps:\n            tracker.latencies = tracker.latencies[args.warmup_steps:]\n\n        stats = tracker.get_stats()\n        row = {\n            \"model\": \"openvla\",\n            \"method\": method,\n            \"k_ratio\": k_ratio,\n            \"suite\": args.suite,\n            \"latency_mean_ms\": round(stats[\"latency_mean_ms\"], 2),\n            \"latency_std_ms\": round(stats[\"latency_std_ms\"], 2),\n            \"memory_peak_mb\": round(memory_peak_mb, 1),\n            \"throughput_sps\": round(stats[\"throughput_sps\"], 2),\n            \"num_steps\": stats[\"num_steps\"],\n        }\n        results.append(row)\n        log.info(\"Result: %s\", row)\n\n        if hook_handle is not None:\n            hook_handle.remove()\n\n    return results\n\n\n# ---------------------------------------------------------------------------\n# Pi0.5\n# ---------------------------------------------------------------------------\n\ndef _pi05_prune_tokens_random(img_emb, keep_ratio):\n    bsize, n_tokens, dim = img_emb.shape\n    n_keep = max(1, int(n_tokens * keep_ratio))\n    indices = torch.randperm(n_tokens)[:n_keep].sort().values.to(img_emb.device)\n    return img_emb[:, indices, :], n_keep\n\n\ndef _pi05_prune_tokens_l2norm(img_emb, keep_ratio):\n    bsize, n_tokens, dim = img_emb.shape\n    n_keep = max(1, int(n_tokens * keep_ratio))\n    norms = torch.norm(img_emb[0].float(), dim=-1)\n    _, topk_idx = torch.topk(norms, n_keep)\n    topk_idx = topk_idx.sort().values\n    return img_emb[:, topk_idx, :], n_keep\n\n\ndef _load_pi05(model_path, device, method, keep_ratio):\n    os.environ.setdefault(\"HF_HOME\", \"/root/autodl-tmp/.hf_cache\")\n    torch._dynamo.config.disable = True\n\n    from lerobot.policies.pi05.modeling_pi05 import PI05Policy\n    policy = PI05Policy.from_pretrained(model_path)\n\n    paligemma_expert = policy.model.paligemma_with_expert\n\n    def patched_embed_image(self, image):\n        out_dtype = image.dtype\n        if image.dtype != torch.float32:\n            image = image.to(torch.float32)\n        image_outputs = self.paligemma.model.vision_tower(image)\n        selected_image_feature = image_outputs.last_hidden_state\n        features = self.paligemma.model.multi_modal_projector(selected_image_feature)\n        if features.dtype != out_dtype:\n            features = features.to(out_dtype)\n        return features\n\n    paligemma_expert.embed_image = types.MethodType(patched_embed_image, paligemma_expert)\n    policy = policy.to(device)\n    policy.eval()\n\n    N_PATCHES = (224 // 14) ** 2\n\n    prune_fn = None\n    if method == \"random\":\n        prune_fn = _pi05_prune_tokens_random\n    elif method == \"l2norm\":\n        prune_fn = _pi05_prune_tokens_l2norm\n\n    if prune_fn is not None and keep_ratio < 1.0:\n        def pruned_embed_prefix(self_model, images, img_masks, tokens, masks):\n            embs = []\n            pad_masks_list = []\n            att_masks = []\n            for img, img_mask in zip(images, img_masks, strict=True):\n                img_emb = self_model.paligemma_with_expert.embed_image(img)\n                bsize, num_img_embs, dim = img_emb.shape\n                img_emb, n_keep = prune_fn(img_emb, keep_ratio)\n                embs.append(img_emb)\n                pad_masks_list.append(img_mask[:, None].expand(bsize, n_keep))\n                att_masks += [0] * n_keep\n            lang_emb = self_model.paligemma_with_expert.embed_language_tokens(tokens)\n            embs.append(lang_emb)\n            pad_masks_list.append(masks)\n            att_masks += [0] * lang_emb.shape[1]\n            embs = torch.cat(embs, dim=1)\n            pad_masks_cat = torch.cat(pad_masks_list, dim=1)\n            att_masks_t = torch.tensor(att_masks, dtype=torch.bool, device=pad_masks_cat.device)\n            att_masks_t = att_masks_t[None, :].expand(bsize, len(att_masks))\n            return embs, pad_masks_cat, att_masks_t\n\n        policy.model.embed_prefix = types.MethodType(pruned_embed_prefix, policy.model)\n        log.info(\"Pi0.5 pruning installed: method=%s keep_ratio=%.2f\", method, keep_ratio)\n\n    from lerobot.policies.factory import make_pre_post_processors\n    preprocess, postprocess = make_pre_post_processors(\n        policy.config, model_path,\n        preprocessor_overrides={\"device_processor\": {\"device\": str(device)}},\n    )\n    return policy, preprocess, postprocess\n\n\ndef _quat_to_axisangle(quat):\n    q = quat.copy()\n    q[3] = np.clip(q[3], -1.0, 1.0)\n    den = np.sqrt(1.0 - q[3] ** 2)\n    if abs(den) < 1e-8:\n        return np.zeros(3, dtype=np.float32)\n    return (q[:3] * 2.0 * np.arccos(q[3]) / den).astype(np.float32)\n\n\ndef profile_pi05(args, k_ratios):\n    device = torch.device(f\"cuda:{args.gpu}\")\n    model_path = args.model_path or \"/root/autodl-tmp/pi05_libero_finetuned\"\n    max_steps = SUITE_MAX_STEPS.get(args.suite, 280)\n\n    from libero.libero import benchmark, get_libero_path\n    from libero.libero.envs import OffScreenRenderEnv\n\n    np.random.seed(args.seed)\n    torch.manual_seed(args.seed)\n    torch.cuda.manual_seed_all(args.seed)\n    task_suite = benchmark.get_benchmark_dict()[args.suite]()\n    n_tasks = task_suite.n_tasks\n\n    results = []\n    for k_ratio in k_ratios:\n        method = \"baseline\" if k_ratio >= 1.0 else args.method\n        log.info(\"=== Pi0.5 method=%s k_ratio=%.2f ===\", method, k_ratio)\n\n        policy, preprocess, postprocess = _load_pi05(model_path, device, method, k_ratio)\n\n        tracker = LatencyTracker(device)\n        global_step = 0\n\n        torch.cuda.reset_peak_memory_stats(device)\n\n        for task_id in range(n_tasks):\n            task = task_suite.get_task(task_id)\n            task_desc = task.language\n            init_states = task_suite.get_task_init_states(task_id)\n            bddl = str(Path(get_libero_path(\"bddl_files\")) / task.problem_folder / task.bddl_file)\n            env = OffScreenRenderEnv(bddl_file_name=bddl, camera_heights=256, camera_widths=256)\n            env.seed(args.seed)\n\n            eps_this_task = min(args.num_episodes, len(init_states))\n            for ep in range(eps_this_task):\n                env.reset()\n                obs = env.set_init_state(init_states[ep])\n                for _ in range(10):\n                    obs, _, _, _ = env.step([0.0] * 6 + [-1.0])\n\n                action_queue = deque()\n                for t in range(max_steps):\n                    if not action_queue:\n                        base_img = obs[\"agentview_image\"]\n                        wrist_img = obs[\"robot0_eye_in_hand_image\"]\n                        base_t = torch.from_numpy(base_img.copy()).permute(2, 0, 1).float() / 255.0\n                        base_t = torch.flip(base_t, dims=[1, 2])\n                        wrist_t = torch.from_numpy(wrist_img.copy()).permute(2, 0, 1).float() / 255.0\n                        wrist_t = torch.flip(wrist_t, dims=[1, 2])\n\n                        eef_pos = obs[\"robot0_eef_pos\"]\n                        eef_quat = obs[\"robot0_eef_quat\"]\n                        gripper_qpos = obs[\"robot0_gripper_qpos\"]\n                        state = np.concatenate([\n                            eef_pos, _quat_to_axisangle(eef_quat), gripper_qpos\n                        ]).astype(np.float32)\n                        state_t = torch.from_numpy(state)\n\n                        raw_obs = {\n                            \"observation.images.image\": base_t,\n                            \"observation.images.image2\": wrist_t,\n                            \"observation.state\": state_t,\n                            \"task\": task_desc,\n                        }\n                        batch = preprocess(raw_obs)\n\n                        tracker.start()\n                        with torch.no_grad():\n                            actions = policy.predict_action_chunk(batch)\n                        tracker.end()\n\n                        actions_unnorm = postprocess(actions)\n                        action_np = actions_unnorm[0].cpu().numpy()\n                        for a in action_np[:args.replan_steps]:\n                            action_queue.append(a[:7])\n\n                        global_step += 1\n\n                    action = action_queue.popleft()\n                    obs, reward, done, info = env.step(action.tolist())\n                    if done:\n                        break\n\n            env.close()\n\n        memory_peak_mb = torch.cuda.max_memory_allocated(device) / (1024 ** 2)\n\n        if len(tracker.latencies) > args.warmup_steps:\n            tracker.latencies = tracker.latencies[args.warmup_steps:]\n\n        stats = tracker.get_stats()\n        row = {\n            \"model\": \"pi05\",\n            \"method\": method,\n            \"k_ratio\": k_ratio,\n            \"suite\": args.suite,\n            \"latency_mean_ms\": round(stats[\"latency_mean_ms\"], 2),\n            \"latency_std_ms\": round(stats[\"latency_std_ms\"], 2),\n            \"memory_peak_mb\": round(memory_peak_mb, 1),\n            \"throughput_sps\": round(stats[\"throughput_sps\"], 2),\n            \"num_steps\": stats[\"num_steps\"],\n        }\n        results.append(row)\n        log.info(\"Result: %s\", row)\n\n        # Free model for next k_ratio (Pi0.5 patching is not easily reversible)\n        del policy\n        torch.cuda.empty_cache()\n\n    return results\n\n\n# ---------------------------------------------------------------------------\n# X-VLA\n# ---------------------------------------------------------------------------\n\nEPS_XVLA = 1e-6\n\n\ndef _load_xvla(model_path, device):\n    model_dir = str(Path(model_path).resolve())\n    sys.path.insert(0, model_dir)\n\n    from configuration_xvla import XVLAConfig\n    from modeling_xvla import XVLA\n    from processing_xvla import XVLAProcessor\n    from safetensors.torch import load_file\n\n    config = XVLAConfig.from_pretrained(model_dir)\n    model = XVLA(config)\n\n    safetensors_path = Path(model_dir) / \"model.safetensors\"\n    if safetensors_path.exists():\n        state_dict = load_file(str(safetensors_path))\n    else:\n        state_dict = torch.load(Path(model_dir) / \"pytorch_model.bin\", map_location=\"cpu\")\n    model.load_state_dict(state_dict, strict=False)\n    model = model.to(device).eval()\n\n    processor = XVLAProcessor.from_pretrained(model_dir, trust_remote_code=True)\n    if processor.tokenizer.pad_token is None:\n        processor.tokenizer.pad_token = \"&lt;pad>\"\n        processor.tokenizer.pad_token_id = 1\n\n    return model, processor\n\n\ndef _install_xvla_pruning(model, keep_ratio, mode):\n    from functools import wraps\n\n    if keep_ratio >= 1.0:\n        return\n\n    original_encode = model.vlm._encode_image\n\n    @wraps(original_encode)\n    def pruned_encode(pixel_values):\n        features = original_encode(pixel_values)\n        N = features.shape[1]\n        k = max(1, int(keep_ratio * N))\n        if k >= N:\n            return features\n        if mode == \"l2norm\":\n            norms = features.norm(dim=-1)\n            _, indices = norms.topk(k, dim=-1)\n        elif mode == \"random\":\n            indices = torch.stack([\n                torch.randperm(N)[:k] for _ in range(features.shape[0])\n            ], dim=0)\n        else:\n            return features\n        indices_sorted = indices.sort(dim=-1).values.to(features.device)\n        pruned = features.gather(\n            1, indices_sorted.unsqueeze(-1).expand(-1, -1, features.shape[-1])\n        )\n        return pruned\n\n    model.vlm._encode_image = pruned_encode\n    model._original_encode_image = original_encode\n    log.info(\"X-VLA pruning installed: keep_ratio=%.2f mode=%s\", keep_ratio, mode)\n\n\ndef _xvla_restore_encode(model):\n    if hasattr(model, \"_original_encode_image\"):\n        model.vlm._encode_image = model._original_encode_image\n        del model._original_encode_image\n\n\ndef _xvla_mat_to_rot6d(R):\n    return np.concatenate([R[:3, 0], R[:3, 1]], axis=-1).astype(np.float32)\n\n\ndef _xvla_rot6d_to_axis_angle(r6d):\n    import robosuite.utils.transform_utils as T\n    single = r6d.ndim == 1\n    if single:\n        r6d = r6d[None, :]\n    a1 = r6d[:, 0:3]\n    a2 = r6d[:, 3:6]\n    b1 = a1 / (np.linalg.norm(a1, axis=-1, keepdims=True) + EPS_XVLA)\n    dot_prod = np.sum(b1 * a2, axis=-1, keepdims=True)\n    b2_orth = a2 - dot_prod * b1\n    b2 = b2_orth / (np.linalg.norm(b2_orth, axis=-1, keepdims=True) + EPS_XVLA)\n    b3 = np.cross(b1, b2, axis=-1)\n    R = np.stack([b1, b2, b3], axis=-1)\n    results = []\n    for i in range(R.shape[0]):\n        quat = T.mat2quat(R[i])\n        aa = T.quat2axisangle(quat)\n        results.append(aa)\n    result = np.stack(results, axis=0)\n    return result[0] if single else result\n\n\ndef _xvla_extract_proprio_20d(env):\n    robot = env.env.robots[0]\n    ee_pos = robot.controller.ee_pos.copy()\n    ee_ori_mat = robot.controller.ee_ori_mat.copy()\n    rot6d = _xvla_mat_to_rot6d(ee_ori_mat)\n    arm1 = np.concatenate([ee_pos, rot6d, np.array([0.0], dtype=np.float32)])\n    arm2 = np.zeros(10, dtype=np.float32)\n    return np.concatenate([arm1, arm2])\n\n\ndef _xvla_get_images_from_obs(obs):\n    images = []\n    for key in [\"agentview_image\", \"robot0_eye_in_hand_image\"]:\n        if key in obs:\n            img = obs[key]\n            img = img[::-1, ::-1]\n            pil = Image.fromarray(img).convert(\"RGB\")\n            images.append(pil)\n    return images\n\n\ndef _xvla_predict_actions(model, processor, images, task_desc, proprio_20d,\n                          domain_id, device, denoise_steps):\n    inputs = processor(\n        images=images,\n        text=task_desc,\n        return_tensors=\"pt\",\n        padding=True,\n    )\n    inputs = {k: v.to(device) if isinstance(v, torch.Tensor) else v for k, v in inputs.items()}\n\n    proprio_t = torch.tensor(proprio_20d, dtype=torch.float32, device=device).unsqueeze(0)\n    domain_t = torch.tensor([domain_id], dtype=torch.long, device=device)\n\n    with torch.no_grad():\n        actions = model.predict_action(\n            input_ids=inputs[\"input_ids\"],\n            pixel_values=inputs[\"pixel_values\"],\n            image_mask=inputs[\"image_mask\"],\n            proprio=proprio_t,\n            domain_id=domain_t,\n            steps=denoise_steps,\n        )\n    return actions.squeeze(0).float().cpu().numpy()\n\n\ndef _xvla_decode_action_20d_to_7d(raw_actions):\n    results = []\n    for act in raw_actions:\n        pos = act[:3]\n        rot6d = act[3:9]\n        grip = act[9]\n        aa = _xvla_rot6d_to_axis_angle(rot6d)\n        action_7d = np.concatenate([pos, aa, [grip]])\n        results.append(action_7d.astype(np.float32))\n    return np.array(results)\n\n\ndef profile_xvla(args, k_ratios):\n    device = torch.device(f\"cuda:{args.gpu}\")\n    model_path = args.model_path or \"/root/autodl-tmp/X-VLA-Libero\"\n    max_steps = XVLA_SUITE_MAX_STEPS.get(args.suite, 800)\n\n    log.info(\"Loading X-VLA from %s ...\", model_path)\n    model, processor = _load_xvla(model_path, device)\n\n    num_actions_per_chunk = model.num_actions\n\n    from libero.libero import benchmark, get_libero_path\n    from libero.libero.envs import OffScreenRenderEnv\n\n    np.random.seed(args.seed)\n    torch.manual_seed(args.seed)\n    task_suite = benchmark.get_benchmark(args.suite)()\n    n_tasks = task_suite.n_tasks\n\n    results = []\n    for k_ratio in k_ratios:\n        method = \"baseline\" if k_ratio >= 1.0 else args.method\n        log.info(\"=== X-VLA method=%s k_ratio=%.2f ===\", method, k_ratio)\n\n        _xvla_restore_encode(model)\n        _install_xvla_pruning(model, k_ratio, method)\n\n        tracker = LatencyTracker(device)\n        global_step = 0\n\n        torch.cuda.reset_peak_memory_stats(device)\n\n        for task_id in range(n_tasks):\n            task = task_suite.get_task(task_id)\n            task_desc = task.language\n            task_bddl = os.path.join(\n                get_libero_path(\"bddl_files\"), task.problem_folder, task.bddl_file\n            )\n            init_states = task_suite.get_task_init_states(task_id)\n\n            eps_this_task = min(args.num_episodes, len(init_states))\n            for ep in range(eps_this_task):\n                env = OffScreenRenderEnv(\n                    bddl_file_name=task_bddl, camera_heights=256, camera_widths=256,\n                )\n                env.seed(args.seed + ep + 100)\n                obs = env.reset()\n                init_state_id = ep % init_states.shape[0]\n                obs = env.set_init_state(init_states[init_state_id])\n\n                for _ in range(10):\n                    obs, _, _, _ = env.step(np.array([0.0] * 6 + [-1.0], dtype=np.float32))\n\n                for robot in env.env.robots:\n                    robot.controller.use_delta = False\n\n                action_queue = []\n                proprio_state = None\n\n                for step_idx in range(max_steps):\n                    if not action_queue:\n                        proprio_20d = _xvla_extract_proprio_20d(env)\n                        if proprio_state is not None:\n                            proprio_20d[:9] = proprio_state[:9]\n\n                        images = _xvla_get_images_from_obs(obs)\n\n                        tracker.start()\n                        raw_actions = _xvla_predict_actions(\n                            model, processor, images, task_desc, proprio_20d,\n                            args.domain_id, device, args.denoise_steps,\n                        )\n                        tracker.end()\n\n                        proprio_state = proprio_20d.copy()\n                        proprio_state[:9] = raw_actions[-1, :9].copy()\n\n                        actions_7d = _xvla_decode_action_20d_to_7d(raw_actions)\n                        action_queue = list(actions_7d)\n                        global_step += 1\n\n                    action = action_queue.pop(0)\n                    obs, reward, done, info = env.step(action)\n\n                    if done or reward > 0.5:\n                        break\n\n                env.close()\n\n        memory_peak_mb = torch.cuda.max_memory_allocated(device) / (1024 ** 2)\n\n        if len(tracker.latencies) > args.warmup_steps:\n            tracker.latencies = tracker.latencies[args.warmup_steps:]\n\n        stats = tracker.get_stats()\n        row = {\n            \"model\": \"xvla\",\n            \"method\": method,\n            \"k_ratio\": k_ratio,\n            \"suite\": args.suite,\n            \"latency_mean_ms\": round(stats[\"latency_mean_ms\"], 2),\n            \"latency_std_ms\": round(stats[\"latency_std_ms\"], 2),\n            \"memory_peak_mb\": round(memory_peak_mb, 1),\n            \"throughput_sps\": round(stats[\"throughput_sps\"], 2),\n            \"num_steps\": stats[\"num_steps\"],\n        }\n        results.append(row)\n        log.info(\"Result: %s\", row)\n\n    return results\n\n\n# ---------------------------------------------------------------------------\n# Main\n# ---------------------------------------------------------------------------\n\nPROFILE_FN = {\n    \"openvla\": profile_openvla,\n    \"pi05\": profile_pi05,\n    \"xvla\": profile_xvla,\n}\n\n\ndef main():\n    args = parse_args()\n    os.environ[\"CUDA_VISIBLE_DEVICES\"] = str(args.gpu)\n\n    k_ratios = [float(x) for x in args.k_ratios.split(\",\")]\n    log.info(\"Model: %s | Method: %s | k_ratios: %s | Suite: %s | Episodes: %d\",\n             args.model, args.method, k_ratios, args.suite, args.num_episodes)\n\n    profile_fn = PROFILE_FN[args.model]\n    results = profile_fn(args, k_ratios)\n\n    fieldnames = [\n        \"model\", \"method\", \"k_ratio\", \"suite\",\n        \"latency_mean_ms\", \"latency_std_ms\", \"memory_peak_mb\",\n        \"throughput_sps\", \"num_steps\",\n    ]\n    output_path = args.output\n    write_header = not os.path.exists(output_path)\n    with open(output_path, \"a\", newline=\"\") as f:\n        writer = csv.DictWriter(f, fieldnames=fieldnames)\n        if write_header:\n            writer.writeheader()\n        for row in results:\n            writer.writerow(row)\n\n    log.info(\"Results appended to %s (%d rows)\", output_path, len(results))\n\n    for row in results:\n        log.info(\"  %s %s k=%.2f: %.1f±%.1f ms, %.0f MB, %.1f sps (%d steps)\",\n                 row[\"model\"], row[\"method\"], row[\"k_ratio\"],\n                 row[\"latency_mean_ms\"], row[\"latency_std_ms\"],\n                 row[\"memory_peak_mb\"], row[\"throughput_sps\"], row[\"num_steps\"])\n\n\nif __name__ == \"__main__\":\n    main()\n"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-25T11:49:25.365310+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/profile_inference_efficiency.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-25T11:49:25.365558+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__append_idea",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__append_idea",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-25T11:49:25.365853+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-25T11:49:25.366102+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "register_artifact",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "register_artifact",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-25T11:49:25.366326+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-25T11:49:25.366518+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "artifact register save",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "artifact register save",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-25T11:49:25.366706+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-25T11:49:25.366915+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/manifest.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/manifest.yaml"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-25T11:49:25.367817+00:00_

1	- id: art_20260516_a1c1c0
2	  name: v8_reeval_fixed_results
3	  type: data
4	  description: v8 D028 fix re-eval results. G1=50.2x G2=+58.8pp G3=1.344x(FAIL) G4=0.087
5	  path: projects/importance_margin_vla_compress/artifacts/mvp_imm_anchor_v8/data/v8_reeval_fixed_summary.txt
6	  url: null
7	  project: importance_margin_vla_compress
8	  exp_id: mvp_imm_anchor_v8
9	  skill: ''
10	  created_at: '2026-05-16T04:06:05.235772+00:00'
11	  tags:
12	  - eval
13	  - v8
14	  - D028
15	  - fixed
16	- id: art_20260516_233350
17	  name: two_stage_dryrun_log
18	  type: intermediate
19	  description: 'Two-stage ACIS-only training dry-run log (5 steps). Validates: baseline
20	    loading, LoRA freeze, ACIS grad flow, Stage 2 skip.'
21	  path: projects/importance_margin_vla_compress/artifacts/imm_two_stage_v9/intermediate/two_stage_dryrun_results.txt
22	  url: null
23	  project: importance_margin_vla_compress
24	  exp_id: imm_two_stage_v9
25	  skill: ''
26	  created_at: '2026-05-16T04:24:11.887346+00:00'
27	  tags:
28	  - two-stage
29	  - dry-run
30	  - ACIS
31	  - v9
32	- id: art_20260516_d6cf0d
33	  name: sim_success_rate
34	  type: data
35	  description: 'aloha_sim_insertion rollout success rate evaluation (50 episodes x
36	    3 modes: baseline, acis_prune, bypass)'
37	  path: projects/importance_margin_vla_compress/artifacts/mvp_imm_v8b_twostage/data/eval_sim.py
38	  url: null
39	  project: importance_margin_vla_compress
40	  exp_id: mvp_imm_v8b_twostage
41	  skill: ''
42	  created_at: '2026-05-16T07:56:44.282702+00:00'
43	  tags:
44	  - eval
45	  - sim
46	  - rollout
47	  - success_rate
48	- id: art_20260516_a430ee
49	  name: ACIS Overhead Quantification Results
50	  type: data
51	  description: 'ACIS module overhead vs baseline SmolVLA: params (+0.77%), FLOPs (+0.24%),
52	    latency (+0.32ms/0.63%). Confirms deployment cost is negligible.'
53	  path: projects/importance_margin_vla_compress/artifacts/plan_011_acis_overhead/data/acis_overhead.json
54	  url: null
55	  project:
…[truncated 68380 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-25T11:49:25.368122+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/manifest.yaml",
  "old_string": "  - importance\n  - visualization\n  - paper-figure\n  - histogram\n  - cliff-zone",
  "new_string": "  - importance\n  - visualization\n  - paper-figure\n  - histogram\n  - cliff-zone\n- id: art_20260525_profile\n  name: profile_inference_efficiency\n  type: intermediate\n  description: 'Inference efficiency profiling script: measures latency, GPU memory,\n    throughput across keep ratios for OpenVLA/Pi0.5/X-VLA on LIBERO. Wraps existing\n    eval scripts with CUDA-synchronized timing.'\n  path: projects/importance_margin_vla_compress/artifacts/profile_inference_efficiency.py\n  url: null\n  project: importance_margin_vla_compress\n  exp_id: null\n  skill: ''\n  created_at: '2026-05-25T00:00:00.000000+00:00'\n  tags:\n  - profiling\n  - latency\n  - memory\n  - throughput\n  - inference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/manifest.yaml",
    "old_string": "  - importance\n  - visualization\n  - paper-figure\n  - histogram\n  - cliff-zone",
    "new_string": "  - importance\n  - visualization\n  - paper-figure\n  - histogram\n  - cliff-zone\n- id: art_20260525_profile\n  name: profile_inference_efficiency\n  type: intermediate\n  description: 'Inference efficiency profiling script: measures latency, GPU memory,\n    throughput across keep ratios for OpenVLA/Pi0.5/X-VLA on LIBERO. Wraps existing\n    eval scripts with CUDA-synchronized timing.'\n  path: projects/importance_margin_vla_compress/artifacts/profile_inference_efficiency.py\n  url: null\n  project: importance_margin_vla_compress\n  exp_id: null\n  skill: ''\n  created_at: '2026-05-25T00:00:00.000000+00:00'\n  tags:\n  - profiling\n  - latency\n  - memory\n  - throughput\n  - inference"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-25T11:49:25.368690+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/manifest.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_profiling_script_20260525T114510",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 55 · 2026-05-25T11:49:25.368972+00:00_

脚本已写入 `/artifacts/profile_inference_efficiency.py` 并注册到 manifest。

支持的功能：
- **三个模型**: OpenVLA（projector hook pruning）、Pi0.5（embed_prefix monkey-patch）、X-VLA（_encode_image 包装）
- **四种方法**: baseline / random / l2norm / attention（attention 仅 OpenVLA）
- **批量扫描 k_ratio**: 一次加载模型，切换 k_ratio（OpenVLA/X-VLA 不需重载；Pi0.5 因 patch 不可逆每次重载）
- **精确计时**: 每个 inference step 前后 `torch.cuda.synchronize()`，跳过前 N 个 warmup step
- **Memory**: `torch.cuda.reset_peak_memory_stats()` + `max_memory_allocated()`
- **CSV 追加模式**: 多次运行结果可拼接

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_profiling_script_20260525T114510"
}
```

</details>

---
