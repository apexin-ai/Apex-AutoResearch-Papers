# deploy bjb2 28827 openvla eval 2gpu

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 0
- **Tool calls:** 20
- **Original source:** `logs/chats/worker_deploy_bjb2-28827-openvla-eval-2gpu_20260520T191957.jsonl`
- **Structured JSON:** [`0013c6214fa3372689a7.json`](../../sessions/00/0013c6214fa3372689a7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

41 recorded events

### Tool call

_source line 1 · 2026-05-20T19:22:08.987038+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__register_cron,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__detect_image",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-openvla-eval-2gpu_20260520T191957",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__register_cron,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__detect_image",
    "max_results": "6"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T19:22:08.988928+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-openvla-eval-2gpu_20260520T191957",
  "tool": "ToolSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T19:22:08.989296+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "grep -n \"openvla\\|vla_type\\|backbone\\|SmolVLA\\|smolvla\\|OpenVLA\" /root/acr-vla-conformal-refinement/src/evaluate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-openvla-eval-2gpu_20260520T191957",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "grep -n \"openvla\\|vla_type\\|backbone\\|SmolVLA\\|smolvla\\|OpenVLA\" /root/acr-vla-conformal-refinement/src/evaluate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T19:22:08.989541+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-openvla-eval-2gpu_20260520T191957",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T19:22:08.989746+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "ls -la /root/autodl-tmp/checkpoints/crm_openvla_obs_only/crm_best.pt",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-openvla-eval-2gpu_20260520T191957",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "ls -la /root/autodl-tmp/checkpoints/crm_openvla_obs_only/crm_best.pt",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-20T19:22:08.989950+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "ps -p 741948 -o pid= 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-openvla-eval-2gpu_20260520T191957",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "ps -p 741948 -o pid= 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-20T19:22:08.990152+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 4507227 May 21 02:53 /root/autodl-tmp/checkpoints/crm_openvla_obs_only/crm_best.pt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.93}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-openvla-eval-2gpu_20260520T191957",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T19:22:08.990490+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-openvla-eval-2gpu_20260520T191957",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T19:22:08.990726+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "ps -p 742213 -o pid= 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-openvla-eval-2gpu_20260520T191957",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "ps -p 742213 -o pid= 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T19:22:08.990942+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-openvla-eval-2gpu_20260520T191957",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T19:22:08.991161+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "ps -p 728278 -o pid= 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-openvla-eval-2gpu_20260520T191957",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "ps -p 728278 -o pid= 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T19:22:08.991391+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-openvla-eval-2gpu_20260520T191957",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T19:22:08.991643+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "grep -n -i \"openvla\\|vla_type\\|backbone\\|SmolVLA\\|smolvla\\|OpenVLA\" /root/acr-vla-conformal-refinement/src/evaluate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-openvla-eval-2gpu_20260520T191957",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "grep -n -i \"openvla\\|vla_type\\|backbone\\|SmolVLA\\|smolvla\\|OpenVLA\" /root/acr-vla-conformal-refinement/src/evaluate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T19:22:08.991851+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-openvla-eval-2gpu_20260520T191957",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T19:22:08.992037+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "ps -p 741948,742213,728278 -o pid,stat,args",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-openvla-eval-2gpu_20260520T191957",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "ps -p 741948,742213,728278 -o pid,stat,args",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T19:22:08.992253+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"   PID STAT COMMAND\\n741948 S    bash -c export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 42 --n_rollouts 10 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed42.json 2>&1 | tee logs/eval-adaptive-unc-head-object-seed42.log\\n742213 S    bash -c export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 43 --n_rollouts 10 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed43.json 2>&1 | tee logs/eval-adaptive-unc-head-object-seed43.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.33}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-openvla-eval-2gpu_20260520T191957",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T19:22:08.992495+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "grep -rn \"norm003.*seed43\\|norm.*0.03.*seed.43\" /proc/*/cmdline",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-openvla-eval-2gpu_20260520T191957",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "grep -rn \"norm003.*seed43\\|norm.*0.03.*seed.43\" /proc/*/cmdline",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T19:22:08.992724+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-openvla-eval-2gpu_20260520T191957",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T19:22:08.992998+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "grep -n -i -e \"openvla\" -e \"vla_type\" -e \"backbone\" -e \"SmolVLA\" -e \"smolvla\" /root/acr-vla-conformal-refinement/src/evaluate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-openvla-eval-2gpu_20260520T191957",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "grep -n -i -e \"openvla\" -e \"vla_type\" -e \"backbone\" -e \"SmolVLA\" -e \"smolvla\" /root/acr-vla-conformal-refinement/src/evaluate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T19:22:08.993235+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"6:  2. Load SmolVLA (frozen) + CRM\\n9:     b. Each step: obs → SmolVLA K=10 samples → CGS on 6D pose → CRM\\n15:  - \\\"vla_only\\\": SmolVLA mean of K=10, no CRM refinement\\n80:    p.add_argument(\\\"--smolvla_path\\\", type=str, default=\\\"/root/autodl-tmp/models/smolvla_libero/\\\")\\n466:    # Load SmolVLA\\n467:    from smolvla_wrapper import SmolVLAWrapper\\n468:    print(f\\\"[eval] Loading SmolVLA from {args.smolvla_path}...\\\")\\n469:    wrapper = SmolVLAWrapper(args.smolvla_path, device=str(device))\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-openvla-eval-2gpu_20260520T191957",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T19:22:08.994991+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_adaptive_unc_head_object_seed44.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-openvla-eval-2gpu_20260520T191957",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_adaptive_unc_head_object_seed44.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-20T19:22:08.995609+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"adaptive_unc_head\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 10,\\n  \\\"overall_success_rate\\\": 0.11,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.2,\\n      \\\"successes\\\": 2,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.2,\\n      \\\"successes\\\": 2,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.2,\\n      \\\"successes\\\": 2,\\n      \\\"total\\\": 10\\n    }\\n  },\\n  \\\"per_step_K\\\": [\\n    1,\\n    
…[truncated 8473 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-openvla-eval-2gpu_20260520T191957",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T19:22:08.995908+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "find /root/acr-vla-conformal-refinement/logs -name \"*adaptive_unc_head*seed44*\" -name \"*.json\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-openvla-eval-2gpu_20260520T191957",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "find /root/acr-vla-conformal-refinement/logs -name \"*adaptive_unc_head*seed44*\" -name \"*.json\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-20T19:22:08.996127+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_adaptive_unc_head_object_seed44.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-openvla-eval-2gpu_20260520T191957",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T19:22:08.997960+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "grep -rn -e \"norm003\" -e \"norm.*0.03\" /root/acr-vla-conformal-refinement/logs/*.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-openvla-eval-2gpu_20260520T191957",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "grep -rn -e \"norm003\" -e \"norm.*0.03\" /root/acr-vla-conformal-refinement/logs/*.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-20T19:22:08.998261+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval-obs-only-object-norm003-seed43.log:1:[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt', 'n_rollouts': 10, 'max_steps': 300, 'seed': 43, 'K': 10, 'mode': 'crm_obs_only', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'obs_dim': 960, 'hidden_dim': 256, 'render': False, 'output_file': 'logs/eval_obs_only_object_norm003_seed43.json', 'max_correction_norm': 0.03, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5}\\n/root/acr-vla-conformal-refinement/logs/eval-obs-only-object-norm003-seed43.log:10:[eval] Override max_correction_norm = 0.03\\n/root/acr-vla-conformal-refinement/logs/eval-obs-only-object-norm003-seed43.log:49:[eval] Results saved to logs/eval_obs_only_object_norm003_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval-obs-only-object-norm003-seed44.log:1:[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt', 'n_rollouts': 10, 'max_steps': 300, 'seed': 44, 'K': 10, 'mode': 'crm_obs_only', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'obs_dim': 960, 'hidden_dim': 256, 'render': False, 'output_file': 'logs/eval_object_obs_only_norm003_seed44.json', 'max_correction_norm': 0.03, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5}\\n/root/acr-vla-conformal-refinement/logs/eval-obs-only-object-norm003-seed44.log:10:[eval] Override max_correction_norm = 0.03\\n/root/acr-vla-conformal-refinement/logs/eval-obs-only-object-norm003-seed44.log:48:[eval] Results saved to logs/eval_object_obs_only_norm003_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed46.log:1:[evaluate] args: {'
…[truncated 1418 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-openvla-eval-2gpu_20260520T191957",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T19:22:08.998546+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "tmux list-sessions",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-openvla-eval-2gpu_20260520T191957",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "tmux list-sessions",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-20T19:22:08.998761+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'tmux' is not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-openvla-eval-2gpu_20260520T191957",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-20T19:22:08.999032+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-28827",
  "command": "tmux list-sessions 2>/dev/null; echo \"---\"; ps aux | grep \"norm003.*seed43\\|seed.43.*norm003\\|norm.*0.03.*seed.43\" | grep -v grep",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-openvla-eval-2gpu_20260520T191957",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "tmux list-sessions 2>/dev/null; echo \"---\"; ps aux | grep \"norm003.*seed43\\|seed.43.*norm003\\|norm.*0.03.*seed.43\" | grep -v grep",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-20T19:22:08.999312+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"eval-random-selection-object-seed44: 1 windows (created Wed May 20 22:30:06 2026)\\neval-seed43-r3: 1 windows (created Thu May 21 01:57:49 2026)\\n---\\nroot     742545  0.0  0.0   4364  3212 ?        S    01:20   0:00 bash -c export CUDA_VISIBLE_DEVICES=4 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 43 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_obs_only_object_norm003_seed43.json 2>&1 | tee logs/eval-obs-only-object-norm003-seed43.log\\nroot     742550  593  0.9 61497968 9822540 ?    Rl   01:20 713:32 python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 43 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_obs_only_object_norm003_seed43.json\\nroot     742551  0.0  0.0   2796  1016 ?        S    01:20   0:00 tee logs/eval-obs-only-object-norm003-seed43.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-openvla-eval-2gpu_20260520T191957",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-20T19:22:08.999561+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "head -5 /root/acr-vla-conformal-refinement/logs/eval_adaptive_unc_head_object_seed44.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-openvla-eval-2gpu_20260520T191957",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "head -5 /root/acr-vla-conformal-refinement/logs/eval_adaptive_unc_head_object_seed44.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-20T19:22:08.999785+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"adaptive_unc_head\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 10,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-openvla-eval-2gpu_20260520T191957",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T19:22:09.000046+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'status': 'RUNNING'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-openvla-eval-2gpu_20260520T191957",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'status': 'RUNNING'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-20T19:22:09.000734+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"D088-eval-adaptive-unc-head-object-seed42\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:00:39.505Z\", \"updated_at\": \"2026-05-20T19:00:06.959Z\", \"hypothesis\": \"D088 方案 B: Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM on LIBERO-Object seed42. n_rollouts=100 for statistical significance. 测试 uncertainty-gated selective CRM 在固定延迟(K=1)下能否保持接近 K=10 CRM 的 SR。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 42 --n_rollouts 100 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed42.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"data_path\": \"LIBERO-Object\", \"data_count\": 1000, \"model_name\": \"UncertaintyHead+CRM_obs_only\", \"checkpoint_source\": \"uncertainty_head_v1/uncertainty_head_best.pt\", \"seed\": 42, \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"logs/eval-adaptive-unc-head-object-seed42.log\"}, \"conclusion\": \"killed\"}, \"D088-eval-adaptive-unc-head-object-seed43\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:00:42.469Z\", \"updated_at\": \"2026-05-20T18:58:53.609Z\", \"hypothesis\": \"D088 方案 B: Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM on LIBERO-Object seed43. n_rollouts=100 for statistical significance. 测试 uncertainty-gated selective CRM 在固定延迟(K=1)下能否保持接近 K=10 CRM 的 SR。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 43 --n_rollouts 100 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncer
…[truncated 18068 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-openvla-eval-2gpu_20260520T191957",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-20T19:22:09.001085+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-adaptive-unc-head-object-seed44",
  "field": "metrics",
  "value": "{'success_rate': 0.11, 'n_tasks': 10, 'n_rollouts': 10, 'total_rollouts': 100, 'avg_K': 1, 'adaptive_trigger_rate': 0, 'crm_trigger_rate': 0.8795, 'unc_threshold': 0.42}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-openvla-eval-2gpu_20260520T191957",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-adaptive-unc-head-object-seed44",
    "field": "metrics",
    "value": "{'success_rate': 0.11, 'n_tasks': 10, 'n_rollouts': 10, 'total_rollouts': 100, 'avg_K': 1, 'adaptive_trigger_rate': 0, 'crm_trigger_rate': 0.8795, 'unc_threshold': 0.42}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-20T19:22:09.001386+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-adaptive-unc-head-object-seed44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T16:52:03.117Z\", \"updated_at\": \"2026-05-20T19:21:36.573Z\", \"hypothesis\": \"D088 方案 B 验证：Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM correction on LIBERO-Object seed44. 测试 uncertainty-gated CRM 是否能在 K=1 延迟下保持接近 K=10 的 SR。\", \"plan_id\": \"d088\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 44 --n_rollouts 10 --K 1 --crm_checkpoint crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:5\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"UncertaintyHead+CRM_obs_only\", \"seed\": 44, \"checkpoint_source\": \"uncertainty_head_v1/uncertainty_head_best.pt\", \"pid\": 728278, \"log_path\": \"logs/eval-adaptive-unc-head-object-seed44.log\"}, \"metrics\": {\"success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"avg_K\": 1, \"adaptive_trigger_rate\": 0, \"crm_trigger_rate\": 0.8795, \"unc_threshold\": 0.42}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.6648}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-openvla-eval-2gpu_20260520T191957",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-20T19:22:09.001635+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-adaptive-unc-head-object-seed44",
  "field": "conclusion",
  "value": "negative",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-openvla-eval-2gpu_20260520T191957",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-adaptive-unc-head-object-seed44",
    "field": "conclusion",
    "value": "negative",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-20T19:22:09.001887+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-adaptive-unc-head-object-seed44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T16:52:03.117Z\", \"updated_at\": \"2026-05-20T19:21:42.757Z\", \"hypothesis\": \"D088 方案 B 验证：Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM correction on LIBERO-Object seed44. 测试 uncertainty-gated CRM 是否能在 K=1 延迟下保持接近 K=10 的 SR。\", \"plan_id\": \"d088\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 44 --n_rollouts 10 --K 1 --crm_checkpoint crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:5\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"UncertaintyHead+CRM_obs_only\", \"seed\": 44, \"checkpoint_source\": \"uncertainty_head_v1/uncertainty_head_best.pt\", \"pid\": 728278, \"log_path\": \"logs/eval-adaptive-unc-head-object-seed44.log\"}, \"metrics\": {\"success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"avg_K\": 1, \"adaptive_trigger_rate\": 0, \"crm_trigger_rate\": 0.8795, \"unc_threshold\": 0.42}, \"conclusion\": \"negative\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.0367}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-openvla-eval-2gpu_20260520T191957",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-20T19:22:09.002133+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-adaptive-unc-head-object-seed44",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 44 --n_rollouts 10 --K 1 --crm_checkpoint crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2', 'server': 'bjb2-28827', 'gpu': 'cuda:5', 'data_path': 'LIBERO-Object', 'data_count': 100, 'model_name': 'UncertaintyHead+CRM_obs_only', 'seed': 44, 'checkpoint_source': 'uncertainty_head_v1/uncertainty_head_best.pt', 'pid': 728278, 'log_path': 'logs/eval-adaptive-unc-head-object-seed44.log', 'checkpoint_path': 'N/A (eval-only)', 'account': 'root'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-openvla-eval-2gpu_20260520T191957",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-adaptive-unc-head-object-seed44",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 44 --n_rollouts 10 --K 1 --crm_checkpoint crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2', 'server': 'bjb2-28827', 'gpu': 'cuda:5', 'data_path': 'LIBERO-Object', 'data_count': 100, 'model_name': 'UncertaintyHead+CRM_obs_only', 'seed': 44, 'checkpoint_source': 'uncertainty_head_v1/uncertainty_head_best.pt', 'pid': 728278, 'log_path': 'logs/eval-adaptive-unc-head-object-seed44.log', 'checkpoint_path': 'N/A (eval-only)', 'account': 'root'}"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-20T19:22:09.002465+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-adaptive-unc-head-object-seed44\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T16:52:03.117Z\", \"updated_at\": \"2026-05-20T19:21:50.874Z\", \"hypothesis\": \"D088 方案 B 验证：Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM correction on LIBERO-Object seed44. 测试 uncertainty-gated CRM 是否能在 K=1 延迟下保持接近 K=10 的 SR。\", \"plan_id\": \"d088\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 44 --n_rollouts 10 --K 1 --crm_checkpoint crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:5\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"UncertaintyHead+CRM_obs_only\", \"seed\": 44, \"checkpoint_source\": \"uncertainty_head_v1/uncertainty_head_best.pt\", \"pid\": 728278, \"log_path\": \"logs/eval-adaptive-unc-head-object-seed44.log\", \"checkpoint_path\": \"N/A (eval-only)\", \"account\": \"root\"}, \"metrics\": {\"success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"avg_K\": 1, \"adaptive_trigger_rate\": 0, \"crm_trigger_rate\": 0.8795, \"unc_threshold\": 0.42}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-20T19:21:50.874Z\"}, \"hint\": \"💡 建议将本次教训写入 memory.md（什么不 work、为什么）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.0352}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-openvla-eval-2gpu_20260520T191957",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-20T19:22:09.002776+00:00_

## 结果汇总

### OpenVLA CRM Eval — 情况 B：需要代码适配，无法部署

`evaluate.py` 硬编码了 SmolVLA，不支持 OpenVLA：

| 位置 | 问题 |
|------|------|
| L80 | `--smolvla_path` 参数，无 `--vla_type` 选项 |
| L466-467 | `from smolvla_wrapper import SmolVLAWrapper` 硬编码导入 |
| L468-469 | `SmolVLAWrapper(args.smolvla_path, device=...)` 直接实例化 |
| 全局 | `obs_dim=960` 是 SmolVLA 特征维度，OpenVLA 不同 |

**需要修改才能跑 OpenVLA eval：**
1. 新增 `--vla_type` 参数 (`smolvla` / `openvla`)
2. 条件导入和实例化 VLA wrapper（需要写 `OpenVLAWrapper` 或复用已有的）
3. 根据 VLA 类型设置 `obs_dim`（OpenVLA feature dim ≠ 960）
4. CRM checkpoint 的输入维度需匹配（`crm_openvla_obs_only` 的 CRM 是用 OpenVLA features 训练的，obs_dim 不同）

### D088 Eval 状态（非 D088-prefixed，n_rollouts=10）

| Seed | PID | 状态 | SR |
|------|-----|------|----|
| 42 | 741948 | **仍在运行** (cuda:0) | — |
| 43 | 742213 | **仍在运行** (cuda:1) | — |
| 44 | 728278 | **完成** → DONE/negative | **11%**（baseline ~14%）|

seed44 详细：`adaptive_trigger_rate=0.0`, `avg_K=1.0`, `crm_trigger_rate=87.95%` — uncertainty head 在 τ=0.42 下从未触发 K>1，全程 K=1 单样本 + selective CRM。

### 清理

- **norm003-seed43**：只有 1 个进程（PID 742550, cuda:4），无重复，无需 kill。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_deploy_bjb2-28827-openvla-eval-2gpu_20260520T191957"
}
```

</details>

---
