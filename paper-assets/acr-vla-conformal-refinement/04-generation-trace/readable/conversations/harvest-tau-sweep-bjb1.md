# harvest tau sweep bjb1

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 117
- **Recorded user turns:** 0
- **Tool calls:** 58
- **Original source:** `logs/chats/worker_harvest_tau-sweep-bjb1_20260523T061143.jsonl`
- **Structured JSON:** [`88e61ce6bcfd4c17369f.json`](../../sessions/88/88e61ce6bcfd4c17369f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

117 recorded events

### Tool call

_source line 1 · 2026-05-23T06:15:52.183855+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__detect_image",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__detect_image",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-23T06:15:52.184217+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T06:15:52.184548+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "ps -p 665520,664402,664686,667018 -o pid,stat,etime,cmd 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "ps -p 665520,664402,664686,667018 -o pid,stat,etime,cmd 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T06:15:52.184712+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T06:15:52.184843+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/results/ -name \"*.json\" -type f -newer /root/acr-vla-conformal-refinement/src/ 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "find /root/acr-vla-conformal-refinement/results/ -name \"*.json\" -type f -newer /root/acr-vla-conformal-refinement/src/ 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T06:15:52.184971+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T06:15:52.185091+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "ls -lt ~/runs/acr-vla-conformal-refinement/ 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "ls -lt ~/runs/acr-vla-conformal-refinement/ 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T06:15:52.185210+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T06:15:52.185402+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-32546",
  "command": "ps -p 665520,664402,664686,667018 -o pid,stat,etime,cmd 2>/dev/null || echo \"PROCESSES_NOT_FOUND\"",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "ps -p 665520,664402,664686,667018 -o pid,stat,etime,cmd 2>/dev/null || echo \"PROCESSES_NOT_FOUND\"",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T06:15:52.185552+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"   PID STAT     ELAPSED CMD\\n667018 Ss+     02:00:28 bash -c rm -f /tmp/agent-ml-exit/eval-supp-adapt-tau035-spatial-s42-r2.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau035-spatial-s42-r2.log; printf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\" > /tmp/agent-ml-exit/eval-supp-adapt-tau035-spatial-s42-r2.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/acr-vla-conformal-refinement && export CUDA_VISIBLE_DEVICES=4 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 86400 env bash -c 'bash -c \\\"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.35 --max_correction_norm 0.2 2>&1 | tee logs/eval-supp-adapt-tau035-spatial-s42-r2.log\\\"'; } > ~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau035-spatial-s42-r2.log 2>&1\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T06:15:52.185698+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/results/ -name \"*.json\" -type f | xargs ls -lt 2>/dev/null | head -30",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "find /root/acr-vla-conformal-refinement/results/ -name \"*.json\" -type f | xargs ls -lt 2>/dev/null | head -30",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T06:15:52.185837+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 984\\ndrwxr-xr-x  3 root root     26 May 22 20:50 outputs\\ndrwxr-xr-x 14 root root   4096 May 22 15:43 autodl-tmp\\n-rw-r--r--  1 root root 995068 May 21 21:35 lerobot_patched.tar.gz\\ndrwxr-xr-x  8 root root   4096 May 21 18:18 acr-vla-conformal-refinement\\ndrwxr-xr-x  2 root root   4096 May 21 12:34 logs\\nlrwxrwxrwx  1 root root     21 May 21 08:29 python -> /usr/local/bin/python\\ndrwxr-xr-x  3 root root     50 May 15 10:53 runs\\nlrwxrwxrwx  1 root root     21 Apr 14 22:05 autodl-pub -> ../../autodl-pub/data\\ndrwxr-xr-x  2 root root     10 Apr 14 22:05 tf-logs\\ndrwxr-xr-x  1 root root     72 May 19  2025 miniconda3\\n\", \"stderr\": \"find: '/root/acr-vla-conformal-refinement/results/': No such file or directory\\n\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T06:15:52.185962+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-32546",
  "command": "ls -lt ~/runs/acr-vla-conformal-refinement/ 2>/dev/null | head -20",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "ls -lt ~/runs/acr-vla-conformal-refinement/ 2>/dev/null | head -20",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-23T06:15:52.186099+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 1280\\n-rw-r--r-- 1 root root  27754 May 23 14:12 train-crm-unified-4suite-r6.log\\n-rw-r--r-- 1 root root   6894 May 23 14:11 eval-supp-adapt-tau035-spatial-s42-r2.log\\n-rw-r--r-- 1 root root   5222 May 23 14:10 eval-supp-obj-crm005-s42-r2.log\\n-rw-r--r-- 1 root root   7541 May 23 14:09 eval-supp-adapt-tau015-spatial-s42-r2.log\\n-rw-r--r-- 1 root root   7415 May 23 14:06 eval-supp-crm-norm02-spatial-s42-r2.log\\n-rw-r--r-- 1 root root   7542 May 23 14:06 eval-supp-adapt-tau025-spatial-s42-r2.log\\n-rw-r--r-- 1 root root   5575 May 23 01:19 eval-pi05-crm-object-seed44.log\\n-rw-r--r-- 1 root root   5737 May 23 01:05 eval-pi05-crm-object-seed43.log\\n-rw-r--r-- 1 root root   5736 May 23 01:02 eval-pi05-crm-object-seed42.log\\n-rw-r--r-- 1 root root   5996 May 23 00:16 eval-pi05-vla-only-goal-seed44-r4.log\\n-rw-r--r-- 1 root root   5995 May 23 00:15 eval-pi05-vla-only-goal-seed43-r4.log\\n-rw-r--r-- 1 root root    824 May 22 19:13 precompute-smolvla-long-bjb1-32546-r2.log\\n-rw-r--r-- 1 root root   6205 May 22 18:37 eval-loss-combined-object-seed42.log\\n-rw-r--r-- 1 root root   6219 May 22 18:34 eval-loss-conformal-object-seed42.log\\n-rw-r--r-- 1 root root 128745 May 22 17:50 precompute-long-k10-bjb1-32546.log\\n-rw-r--r-- 1 root root   2752 May 22 14:38 precompute-smolvla-long-bjb1-32546.log\\n-rw-r--r-- 1 root root   2022 May 22 14:37 precompute-smolvla-goal-bjb1-32546.log\\n-rw-r--r-- 1 root root   2287 May 22 13:38 eval-smolvla-acr-long-seed42.log\\n-rw-r--r-- 1 root root   2370 May 22 13:38 eval-smolvla-acr-goal-seed43.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T06:15:52.186288+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tail -100 ~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau025-spatial-s42-r2.log",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tail -100 ~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau025-spatial-s42-r2.log",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-23T06:15:52.186502+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[evaluate] args: {'benchmark': 'spatial', 'checkpoint': None, 'crm_checkpoint': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'n_rollouts': 20, 'max_steps': 300, 'seed': 42, 'K': 10, 'mode': 'adaptive_conformal_crm', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'smolvla', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'unified_obs_dim': None, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json', 'max_correction_norm': 0.2, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.25, 'n_action_steps': 10}\\n[eval] Mode: adaptive_conformal_crm, benchmark: spatial\\n[eval] max_steps set to 280 for benchmark spatial\\n[eval] Loading SmolVLA from /root/autodl-tmp/models/smolvla_libero/...\\nLoading  /root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct weights ...\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/489 [00:00<?, ?it/s]\\rLoading weights:  58%|█████▊    | 284/489 [00:00<00:00, 2799.86it/s]\\rLoading weights: 100%|██████████| 489/489 [00:00<00:00, 3289.36it/s]\\nReducing the number of VLM layers to 16 ...\\nLoading weights from local directory\\n[eval] CRM loaded from /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt (327,198 params)\\n[eval] Override max_correction_norm = 0.2\\n[eval] Loading LIBERO spatial environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n  pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate: rollout 5/20, success so far: 5/5\\n  pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate: rollout 10/20, success so far: 10/10\\n  pi
…[truncated 5820 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-23T06:15:52.186659+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tail -100 ~/runs/acr-vla-conformal-refinement/eval-supp-crm-norm02-spatial-s42-r2.log",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tail -100 ~/runs/acr-vla-conformal-refinement/eval-supp-crm-norm02-spatial-s42-r2.log",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-23T06:15:52.186856+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[evaluate] args: {'benchmark': 'spatial', 'checkpoint': None, 'crm_checkpoint': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'n_rollouts': 20, 'max_steps': 300, 'seed': 42, 'K': 10, 'mode': 'crm_obs_only', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'smolvla', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'unified_obs_dim': None, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_spatial_crm_obs_only_norm0.2_seed42.json', 'max_correction_norm': 0.2, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855, 'n_action_steps': 10}\\n[eval] Mode: crm_obs_only, benchmark: spatial\\n[eval] max_steps set to 280 for benchmark spatial\\n[eval] Loading SmolVLA from /root/autodl-tmp/models/smolvla_libero/...\\nLoading  /root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct weights ...\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/489 [00:00<?, ?it/s]\\rLoading weights:  58%|█████▊    | 284/489 [00:00<00:00, 2809.31it/s]\\rLoading weights: 100%|██████████| 489/489 [00:00<00:00, 3316.90it/s]\\nReducing the number of VLM layers to 16 ...\\nLoading weights from local directory\\n[eval] CRM loaded from /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt (327,198 params)\\n[eval] Override max_correction_norm = 0.2\\n[eval] Loading LIBERO spatial environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n  pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate: rollout 5/20, success so far: 5/5\\n  pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate: rollout 10/20, success so far: 10/10\\n  pick_up_the_black_bowl_between_the_p
…[truncated 5691 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-23T06:15:52.187013+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tail -100 ~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau015-spatial-s42-r2.log",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tail -100 ~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau015-spatial-s42-r2.log",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-23T06:15:52.187203+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[evaluate] args: {'benchmark': 'spatial', 'checkpoint': None, 'crm_checkpoint': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'n_rollouts': 20, 'max_steps': 300, 'seed': 42, 'K': 10, 'mode': 'adaptive_conformal_crm', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'smolvla', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'unified_obs_dim': None, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.15_seed42.json', 'max_correction_norm': 0.2, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.15, 'n_action_steps': 10}\\n[eval] Mode: adaptive_conformal_crm, benchmark: spatial\\n[eval] max_steps set to 280 for benchmark spatial\\n[eval] Loading SmolVLA from /root/autodl-tmp/models/smolvla_libero/...\\nLoading  /root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct weights ...\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/489 [00:00<?, ?it/s]\\rLoading weights:  59%|█████▉    | 289/489 [00:00<00:00, 2883.09it/s]\\rLoading weights: 100%|██████████| 489/489 [00:00<00:00, 2619.87it/s]\\nReducing the number of VLM layers to 16 ...\\nLoading weights from local directory\\n[eval] CRM loaded from /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt (327,198 params)\\n[eval] Override max_correction_norm = 0.2\\n[eval] Loading LIBERO spatial environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n  pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate: rollout 5/20, success so far: 5/5\\n  pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate: rollout 10/20, success so far: 10/10\\n  pi
…[truncated 5819 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-23T06:15:52.187386+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tail -100 ~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau035-spatial-s42-r2.log",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tail -100 ~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau035-spatial-s42-r2.log",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-23T06:15:52.187577+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[evaluate] args: {'benchmark': 'spatial', 'checkpoint': None, 'crm_checkpoint': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'n_rollouts': 20, 'max_steps': 300, 'seed': 42, 'K': 10, 'mode': 'adaptive_conformal_crm', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'smolvla', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'unified_obs_dim': None, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.35_seed42.json', 'max_correction_norm': 0.2, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.35, 'n_action_steps': 10}\\n[eval] Mode: adaptive_conformal_crm, benchmark: spatial\\n[eval] max_steps set to 280 for benchmark spatial\\n[eval] Loading SmolVLA from /root/autodl-tmp/models/smolvla_libero/...\\nLoading  /root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct weights ...\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/489 [00:00<?, ?it/s]\\rLoading weights:  54%|█████▍    | 266/489 [00:00<00:00, 2635.36it/s]\\rLoading weights: 100%|██████████| 489/489 [00:00<00:00, 3173.43it/s]\\nReducing the number of VLM layers to 16 ...\\nLoading weights from local directory\\n[eval] CRM loaded from /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt (327,198 params)\\n[eval] Override max_correction_norm = 0.2\\n[eval] Loading LIBERO spatial environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n  pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate: rollout 5/20, success so far: 5/5\\n  pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate: rollout 10/20, success so far: 10/10\\n  pi
…[truncated 5151 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-23T06:15:52.187765+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-32546",
  "command": "nvidia-smi --query-gpu=index,name,utilization.gpu,memory.used,memory.total --format=csv,noheader 2>/dev/null",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "nvidia-smi --query-gpu=index,name,utilization.gpu,memory.used,memory.total --format=csv,noheader 2>/dev/null",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-23T06:15:52.187904+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, NVIDIA GeForce RTX 4090, 0 %, 2 MiB, 24564 MiB\\n1, NVIDIA GeForce RTX 4090, 0 %, 2 MiB, 24564 MiB\\n2, NVIDIA GeForce RTX 4090, 0 %, 2 MiB, 24564 MiB\\n3, NVIDIA GeForce RTX 4090, 10 %, 544 MiB, 24564 MiB\\n4, NVIDIA GeForce RTX 4090, 22 %, 1978 MiB, 24564 MiB\\n5, NVIDIA GeForce RTX 4090, 26 %, 2008 MiB, 24564 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.48}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-23T06:15:52.188035+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'RUNNING'}",
  "fields": "['exp_id', 'status', 'conclusion', 'metrics', 'hypothesis']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'RUNNING'}",
    "fields": "['exp_id', 'status', 'conclusion', 'metrics', 'hypothesis']"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-23T06:15:52.188193+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"precompute-pi05-long-2048-r2\": {\"status\": \"RUNNING\", \"hypothesis\": \"Precompute π0.5 2048D obs_features + K=10 action samples on LIBERO-Long demos for CRM training (Plan A). Retry of precompute-pi05-long-2048.\"}, \"precompute-pi05-goal-2048-r2\": {\"status\": \"RUNNING\", \"hypothesis\": \"Precompute π0.5 2048D obs_features + K=10 action samples on LIBERO-Goal demos for CRM training (Plan A). Retry of precompute-pi05-goal-2048.\"}, \"precompute-pi05-spatial-2048-r2\": {\"status\": \"RUNNING\", \"hypothesis\": \"Precompute π0.5 2048D obs_features + K=10 action samples on LIBERO-Spatial demos for CRM training (Plan A). Retry of precompute-pi05-spatial-2048.\"}, \"precompute-pi05-object-2048-r2\": {\"status\": \"RUNNING\", \"hypothesis\": \"Precompute π0.5 2048D obs_features + K=10 action samples on LIBERO-Object demos for CRM training (Plan A). Retry of precompute-pi05-object-2048.\"}, \"eval-smolvla-lerobot-goal-seed43-v3\": {\"status\": \"RUNNING\", \"hypothesis\": \"SmolVLA lerobot-eval baseline on LIBERO-Goal seed=43 for 3-seed mean±std paper comparison\"}, \"eval-smolvla-lerobot-spatial-seed43-v3\": {\"status\": \"RUNNING\", \"hypothesis\": \"SmolVLA lerobot-eval baseline on LIBERO-Spatial seed=43 for 3-seed mean±std paper comparison\"}}, \"count\": 6, \"total\": 6, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5016}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-23T06:15:52.188455+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'eval-supp-adapt-tau025-spatial-s42-r2'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'eval-supp-adapt-tau025-spatial-s42-r2'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-23T06:15:52.188615+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.595}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-23T06:15:52.188738+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'eval-supp-crm-norm02-spatial-s42-r2'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'eval-supp-crm-norm02-spatial-s42-r2'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-23T06:15:52.188858+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'eval-supp-adapt-tau015-spatial-s42-r2'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'eval-supp-adapt-tau015-spatial-s42-r2'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-23T06:15:52.188988+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6021}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-23T06:15:52.189105+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'eval-supp-adapt-tau035-spatial-s42-r2'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'eval-supp-adapt-tau035-spatial-s42-r2'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-23T06:15:52.189225+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6899}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-23T06:15:52.189365+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5916}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-23T06:15:52.189505+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'eval-supp-adapt-tau025-spatial-s42'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'eval-supp-adapt-tau025-spatial-s42'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-23T06:15:52.189623+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'eval-supp-crm-norm02-spatial-s42'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'eval-supp-crm-norm02-spatial-s42'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-23T06:15:52.189740+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6169}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-23T06:15:52.189853+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3597}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-23T06:15:52.189978+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "limit": "5",
  "fields": "['exp_id', 'status', 'conclusion', 'hypothesis', 'metrics']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "limit": "5",
    "fields": "['exp_id', 'status', 'conclusion', 'hypothesis', 'metrics']"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-23T06:15:52.190127+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"precompute-pi05-long-2048-r2\": {\"status\": \"RUNNING\", \"hypothesis\": \"Precompute π0.5 2048D obs_features + K=10 action samples on LIBERO-Long demos for CRM training (Plan A). Retry of precompute-pi05-long-2048.\"}, \"precompute-pi05-goal-2048-r2\": {\"status\": \"RUNNING\", \"hypothesis\": \"Precompute π0.5 2048D obs_features + K=10 action samples on LIBERO-Goal demos for CRM training (Plan A). Retry of precompute-pi05-goal-2048.\"}, \"precompute-pi05-spatial-2048-r2\": {\"status\": \"RUNNING\", \"hypothesis\": \"Precompute π0.5 2048D obs_features + K=10 action samples on LIBERO-Spatial demos for CRM training (Plan A). Retry of precompute-pi05-spatial-2048.\"}, \"precompute-pi05-object-2048-r2\": {\"status\": \"RUNNING\", \"hypothesis\": \"Precompute π0.5 2048D obs_features + K=10 action samples on LIBERO-Object demos for CRM training (Plan A). Retry of precompute-pi05-object-2048.\"}, \"eval-smolvla-lerobot-goal-seed43-v3\": {\"status\": \"RUNNING\", \"hypothesis\": \"SmolVLA lerobot-eval baseline on LIBERO-Goal seed=43 for 3-seed mean±std paper comparison\"}}, \"count\": 5, \"total\": 112, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4608}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-23T06:15:52.190304+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'DONE'}",
  "limit": "5",
  "fields": "['exp_id', 'status', 'conclusion', 'hypothesis', 'metrics', 'log_path', 'checkpoint_path']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'DONE'}",
    "limit": "5",
    "fields": "['exp_id', 'status', 'conclusion', 'hypothesis', 'metrics', 'log_path', 'checkpoint_path']"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-23T06:15:52.190477+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-smolvla-lerobot-object-seed44-v2\": {\"status\": \"DONE\", \"hypothesis\": \"SmolVLA lerobot-eval baseline on LIBERO-Object seed=44 for 3-seed mean±std paper comparison\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.65, \"pc_success\": 65, \"n_episodes\": 200, \"eval_s\": 841}}, \"eval-smolvla-lerobot-object-seed43-v2\": {\"status\": \"DONE\", \"hypothesis\": \"SmolVLA lerobot-eval baseline on LIBERO-Object seed=43 for 3-seed mean±std paper comparison\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.665, \"pc_success\": 66.5, \"n_episodes\": 200, \"eval_s\": 857.4}}, \"eval-openvla-oft-official-object\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"hypothesis\": \"OpenVLA-OFT official repo with per-suite finetuned weights can achieve non-zero success rate on LIBERO-Object (10 tasks × 50 trials) — using the authors' eval script to establish ground truth baseline for cross-model CRM generalization\"}, \"eval-perdof-object-norm02-seed45-r3\": {\"status\": \"DONE\", \"hypothesis\": \"perdof CRM (ε=0.2) seed45 on LIBERO-Object. Rerun after SIGHUP kill. Original result on bjb2-28827 was 9%. This confirms reproducibility on different server.\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm005-seed43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}}, \"count\": 5, \"total\": 73, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5492}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-23T06:15:52.190661+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau025-spatial-s42-r2",
  "field": "hypothesis",
  "value": "Adaptive conformal CRM with tau=0.25 (norm=0.2) on LIBERO-Spatial seed42 — threshold sweep supplementary experiment. Lower tau increases trigger rate and correction frequency; tau=0.25 should balance precision vs coverage for conformal triggering."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-adapt-tau025-spatial-s42-r2",
    "field": "hypothesis",
    "value": "Adaptive conformal CRM with tau=0.25 (norm=0.2) on LIBERO-Spatial seed42 — threshold sweep supplementary experiment. Lower tau increases trigger rate and correction frequency; tau=0.25 should balance precision vs coverage for conformal triggering."
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-23T06:15:52.190806+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau025-spatial-s42-r2\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T06:13:46.810Z\", \"updated_at\": \"2026-05-23T06:13:46.810Z\", \"hypothesis\": \"Adaptive conformal CRM with tau=0.25 (norm=0.2) on LIBERO-Spatial seed42 — threshold sweep supplementary experiment. Lower tau increases trigger rate and correction frequency; tau=0.25 should balance precision vs coverage for conformal triggering.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8362}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-23T06:15:52.190944+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm02-spatial-s42-r2",
  "field": "hypothesis",
  "value": "CRM obs_only with max_correction_norm=0.2 on LIBERO-Spatial seed42 — ablation to isolate effect of norm clipping magnitude. Norm=0.2 should reduce overcorrection compared to default, improving SR on tasks where CRM overshoots."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm02-spatial-s42-r2",
    "field": "hypothesis",
    "value": "CRM obs_only with max_correction_norm=0.2 on LIBERO-Spatial seed42 — ablation to isolate effect of norm clipping magnitude. Norm=0.2 should reduce overcorrection compared to default, improving SR on tasks where CRM overshoots."
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-23T06:15:52.191088+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm02-spatial-s42-r2\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T06:13:49.420Z\", \"updated_at\": \"2026-05-23T06:13:49.420Z\", \"hypothesis\": \"CRM obs_only with max_correction_norm=0.2 on LIBERO-Spatial seed42 — ablation to isolate effect of norm clipping magnitude. Norm=0.2 should reduce overcorrection compared to default, improving SR on tasks where CRM overshoots.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6933}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-23T06:15:52.191218+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau015-spatial-s42-r2",
  "field": "hypothesis",
  "value": "Adaptive conformal CRM with tau=0.15 (norm=0.2) on LIBERO-Spatial seed42 — threshold sweep supplementary experiment. Very low tau triggers CRM on most steps (high trigger rate), testing whether aggressive correction helps or hurts."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-adapt-tau015-spatial-s42-r2",
    "field": "hypothesis",
    "value": "Adaptive conformal CRM with tau=0.15 (norm=0.2) on LIBERO-Spatial seed42 — threshold sweep supplementary experiment. Very low tau triggers CRM on most steps (high trigger rate), testing whether aggressive correction helps or hurts."
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-23T06:15:52.191435+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau015-spatial-s42-r2\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T06:13:51.160Z\", \"updated_at\": \"2026-05-23T06:13:51.160Z\", \"hypothesis\": \"Adaptive conformal CRM with tau=0.15 (norm=0.2) on LIBERO-Spatial seed42 — threshold sweep supplementary experiment. Very low tau triggers CRM on most steps (high trigger rate), testing whether aggressive correction helps or hurts.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5363}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-23T06:15:52.191588+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau035-spatial-s42-r2",
  "field": "hypothesis",
  "value": "Adaptive conformal CRM with tau=0.35 (norm=0.2) on LIBERO-Spatial seed42 — threshold sweep supplementary experiment. Higher tau reduces trigger rate, testing whether more selective conformal triggering improves precision."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-adapt-tau035-spatial-s42-r2",
    "field": "hypothesis",
    "value": "Adaptive conformal CRM with tau=0.35 (norm=0.2) on LIBERO-Spatial seed42 — threshold sweep supplementary experiment. Higher tau reduces trigger rate, testing whether more selective conformal triggering improves precision."
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-23T06:15:52.191732+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau035-spatial-s42-r2\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T06:13:52.718Z\", \"updated_at\": \"2026-05-23T06:13:52.718Z\", \"hypothesis\": \"Adaptive conformal CRM with tau=0.35 (norm=0.2) on LIBERO-Spatial seed42 — threshold sweep supplementary experiment. Higher tau reduces trigger rate, testing whether more selective conformal triggering improves precision.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9392}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-23T06:15:52.191884+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau025-spatial-s42-r2",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.25 --max_correction_norm 0.2', 'server': 'bjb1-32546', 'data_path': 'LIBERO-Spatial', 'data_count': 200, 'model_name': 'smolvla+crm_3suite_v1', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Spatial'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-adapt-tau025-spatial-s42-r2",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.25 --max_correction_norm 0.2', 'server': 'bjb1-32546', 'data_path': 'LIBERO-Spatial', 'data_count': 200, 'model_name': 'smolvla+crm_3suite_v1', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Spatial'}"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-23T06:15:52.192025+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.3633}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-23T06:15:52.192150+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm02-spatial-s42-r2",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2', 'server': 'bjb1-32546', 'data_path': 'LIBERO-Spatial', 'data_count': 200, 'model_name': 'smolvla+crm_3suite_v1', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Spatial'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm02-spatial-s42-r2",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2', 'server': 'bjb1-32546', 'data_path': 'LIBERO-Spatial', 'data_count': 200, 'model_name': 'smolvla+crm_3suite_v1', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Spatial'}"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-23T06:15:52.192378+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.3068}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-23T06:15:52.192543+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau015-spatial-s42-r2",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.15 --max_correction_norm 0.2', 'server': 'bjb1-32546', 'data_path': 'LIBERO-Spatial', 'data_count': 200, 'model_name': 'smolvla+crm_3suite_v1', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Spatial'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-adapt-tau015-spatial-s42-r2",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.15 --max_correction_norm 0.2', 'server': 'bjb1-32546', 'data_path': 'LIBERO-Spatial', 'data_count': 200, 'model_name': 'smolvla+crm_3suite_v1', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Spatial'}"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-23T06:15:52.192684+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.361}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-23T06:15:52.192815+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau035-spatial-s42-r2",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.35 --max_correction_norm 0.2', 'server': 'bjb1-32546', 'data_path': 'LIBERO-Spatial', 'data_count': 200, 'model_name': 'smolvla+crm_3suite_v1', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Spatial'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-adapt-tau035-spatial-s42-r2",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.35 --max_correction_norm 0.2', 'server': 'bjb1-32546', 'data_path': 'LIBERO-Spatial', 'data_count': 200, 'model_name': 'smolvla+crm_3suite_v1', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Spatial'}"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-23T06:15:52.192951+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.303}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-23T06:15:52.193237+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau025-spatial-s42-r2",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-adapt-tau025-spatial-s42-r2",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-23T06:15:52.193512+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau025-spatial-s42-r2\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-23T06:13:46.810Z\", \"updated_at\": \"2026-05-23T06:14:13.940Z\", \"hypothesis\": \"Adaptive conformal CRM with tau=0.25 (norm=0.2) on LIBERO-Spatial seed42 — threshold sweep supplementary experiment. Lower tau increases trigger rate and correction frequency; tau=0.25 should balance precision vs coverage for conformal triggering.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8541}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-23T06:15:52.193690+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm02-spatial-s42-r2",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm02-spatial-s42-r2",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-23T06:15:52.193861+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau015-spatial-s42-r2",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-adapt-tau015-spatial-s42-r2",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-23T06:15:52.194023+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm02-spatial-s42-r2\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-23T06:13:49.420Z\", \"updated_at\": \"2026-05-23T06:14:14.861Z\", \"hypothesis\": \"CRM obs_only with max_correction_norm=0.2 on LIBERO-Spatial seed42 — ablation to isolate effect of norm clipping magnitude. Norm=0.2 should reduce overcorrection compared to default, improving SR on tasks where CRM overshoots.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7991}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-23T06:15:52.194176+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau035-spatial-s42-r2",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-adapt-tau035-spatial-s42-r2",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-23T06:15:52.194344+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau015-spatial-s42-r2\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-23T06:13:51.160Z\", \"updated_at\": \"2026-05-23T06:14:15.716Z\", \"hypothesis\": \"Adaptive conformal CRM with tau=0.15 (norm=0.2) on LIBERO-Spatial seed42 — threshold sweep supplementary experiment. Very low tau triggers CRM on most steps (high trigger rate), testing whether aggressive correction helps or hurts.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6585}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-23T06:15:52.194496+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau035-spatial-s42-r2\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-23T06:13:52.718Z\", \"updated_at\": \"2026-05-23T06:14:16.202Z\", \"hypothesis\": \"Adaptive conformal CRM with tau=0.35 (norm=0.2) on LIBERO-Spatial seed42 — threshold sweep supplementary experiment. Higher tau reduces trigger rate, testing whether more selective conformal triggering improves precision.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4385}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-23T06:15:52.194653+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau025-spatial-s42-r2",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.25 --max_correction_norm 0.2', 'server': 'bjb1-32546', 'data_path': 'LIBERO-Spatial', 'data_count': 200, 'model_name': 'smolvla+crm_3suite_v1', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Spatial'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-adapt-tau025-spatial-s42-r2",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.25 --max_correction_norm 0.2', 'server': 'bjb1-32546', 'data_path': 'LIBERO-Spatial', 'data_count': 200, 'model_name': 'smolvla+crm_3suite_v1', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Spatial'}"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-23T06:15:52.194833+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau025-spatial-s42-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T06:13:46.810Z\", \"updated_at\": \"2026-05-23T06:14:33.094Z\", \"hypothesis\": \"Adaptive conformal CRM with tau=0.25 (norm=0.2) on LIBERO-Spatial seed42 — threshold sweep supplementary experiment. Lower tau increases trigger rate and correction frequency; tau=0.25 should balance precision vs coverage for conformal triggering.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.25 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla+crm_3suite_v1\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7982}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-23T06:15:52.195085+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm02-spatial-s42-r2",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2', 'server': 'bjb1-32546', 'data_path': 'LIBERO-Spatial', 'data_count': 200, 'model_name': 'smolvla+crm_3suite_v1', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Spatial'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm02-spatial-s42-r2",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2', 'server': 'bjb1-32546', 'data_path': 'LIBERO-Spatial', 'data_count': 200, 'model_name': 'smolvla+crm_3suite_v1', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Spatial'}"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-23T06:15:52.195305+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm02-spatial-s42-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T06:13:49.420Z\", \"updated_at\": \"2026-05-23T06:14:34.892Z\", \"hypothesis\": \"CRM obs_only with max_correction_norm=0.2 on LIBERO-Spatial seed42 — ablation to isolate effect of norm clipping magnitude. Norm=0.2 should reduce overcorrection compared to default, improving SR on tasks where CRM overshoots.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla+crm_3suite_v1\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8118}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-23T06:15:52.195479+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau015-spatial-s42-r2",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.15 --max_correction_norm 0.2', 'server': 'bjb1-32546', 'data_path': 'LIBERO-Spatial', 'data_count': 200, 'model_name': 'smolvla+crm_3suite_v1', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Spatial'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-adapt-tau015-spatial-s42-r2",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.15 --max_correction_norm 0.2', 'server': 'bjb1-32546', 'data_path': 'LIBERO-Spatial', 'data_count': 200, 'model_name': 'smolvla+crm_3suite_v1', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Spatial'}"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-23T06:15:52.195651+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau015-spatial-s42-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T06:13:51.160Z\", \"updated_at\": \"2026-05-23T06:14:37.344Z\", \"hypothesis\": \"Adaptive conformal CRM with tau=0.15 (norm=0.2) on LIBERO-Spatial seed42 — threshold sweep supplementary experiment. Very low tau triggers CRM on most steps (high trigger rate), testing whether aggressive correction helps or hurts.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.15 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla+crm_3suite_v1\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7128}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-23T06:15:52.195805+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau035-spatial-s42-r2",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.35 --max_correction_norm 0.2', 'server': 'bjb1-32546', 'data_path': 'LIBERO-Spatial', 'data_count': 200, 'model_name': 'smolvla+crm_3suite_v1', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Spatial'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-adapt-tau035-spatial-s42-r2",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.35 --max_correction_norm 0.2', 'server': 'bjb1-32546', 'data_path': 'LIBERO-Spatial', 'data_count': 200, 'model_name': 'smolvla+crm_3suite_v1', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Spatial'}"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-23T06:15:52.195967+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau035-spatial-s42-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T06:13:52.718Z\", \"updated_at\": \"2026-05-23T06:14:39.716Z\", \"hypothesis\": \"Adaptive conformal CRM with tau=0.35 (norm=0.2) on LIBERO-Spatial seed42 — threshold sweep supplementary experiment. Higher tau reduces trigger rate, testing whether more selective conformal triggering improves precision.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.35 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla+crm_3suite_v1\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8532}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-23T06:15:52.196119+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tail -20 ~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau035-spatial-s42-r2.log",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tail -20 ~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau035-spatial-s42-r2.log",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-23T06:15:52.196398+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 20/20, success so far: 17/20\\n[pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate] success rate: 85.0% (17/20)\\n  pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate: rollout 5/20, success so far: 3/5\\n  pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate: rollout 10/20, success so far: 8/10\\n  pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate: rollout 15/20, success so far: 13/15\\n  pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate: rollout 20/20, success so far: 17/20\\n[pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate] success rate: 85.0% (17/20)\\n  pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate: rollout 5/20, success so far: 5/5\\n  pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate: rollout 10/20, success so far: 9/10\\n  pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate: rollout 15/20, success so far: 13/15\\n  pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate: rollout 20/20, success so far: 17/20\\n[pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate] success rate: 85.0% (17/20)\\n\\n============================================================\\nOverall success rate (adaptive_conformal_crm): 80.0% (160/200)\\n============================================================\\n[eval] Conformal CRM stats: mean_unc=0.1873, trigger_rate=12.2%\\n[eval] Results saved to logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.35_seed42.json\\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\\nEXIT_CODE=0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-23T06:15:52.196610+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau025-spatial-s42-r2",
  "field": "metrics",
  "value": "{'success_rate': 0.82, 'trigger_rate': 0.194, 'mean_unc': 0.1847, 'per_task_sr': {'between_plate_ramekin': 0.95, 'next_to_ramekin': 0.95, 'table_center': 1, 'cookie_box': 1, 'top_drawer': 0.75, 'on_ramekin': 0, 'next_to_cookie_box': 0.9, 'stove': 0.9, 'next_to_plate': 0.9, 'wooden_cabinet': 0.85}}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-adapt-tau025-spatial-s42-r2",
    "field": "metrics",
    "value": "{'success_rate': 0.82, 'trigger_rate': 0.194, 'mean_unc': 0.1847, 'per_task_sr': {'between_plate_ramekin': 0.95, 'next_to_ramekin': 0.95, 'table_center': 1, 'cookie_box': 1, 'top_drawer': 0.75, 'on_ramekin': 0, 'next_to_cookie_box': 0.9, 'stove': 0.9, 'next_to_plate': 0.9, 'wooden_cabinet': 0.85}}"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-23T06:15:52.196827+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau025-spatial-s42-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T06:13:46.810Z\", \"updated_at\": \"2026-05-23T06:14:50.598Z\", \"hypothesis\": \"Adaptive conformal CRM with tau=0.25 (norm=0.2) on LIBERO-Spatial seed42 — threshold sweep supplementary experiment. Lower tau increases trigger rate and correction frequency; tau=0.25 should balance precision vs coverage for conformal triggering.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.25 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla+crm_3suite_v1\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}, \"metrics\": {\"success_rate\": 0.82, \"trigger_rate\": 0.194, \"mean_unc\": 0.1847, \"per_task_sr\": {\"between_plate_ramekin\": 0.95, \"next_to_ramekin\": 0.95, \"table_center\": 1, \"cookie_box\": 1, \"top_drawer\": 0.75, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"stove\": 0.9, \"next_to_plate\": 0.9, \"wooden_cabinet\": 0.85}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2662}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-23T06:15:52.196984+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm02-spatial-s42-r2",
  "field": "metrics",
  "value": "{'success_rate': 0.79, 'per_task_sr': {'between_plate_ramekin': 1, 'next_to_ramekin': 0.9, 'table_center': 0.95, 'cookie_box': 0.95, 'top_drawer': 0.75, 'on_ramekin': 0, 'next_to_cookie_box': 1, 'stove': 0.95, 'next_to_plate': 0.75, 'wooden_cabinet': 0.65}}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm02-spatial-s42-r2",
    "field": "metrics",
    "value": "{'success_rate': 0.79, 'per_task_sr': {'between_plate_ramekin': 1, 'next_to_ramekin': 0.9, 'table_center': 0.95, 'cookie_box': 0.95, 'top_drawer': 0.75, 'on_ramekin': 0, 'next_to_cookie_box': 1, 'stove': 0.95, 'next_to_plate': 0.75, 'wooden_cabinet': 0.65}}"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-23T06:15:52.197173+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm02-spatial-s42-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T06:13:49.420Z\", \"updated_at\": \"2026-05-23T06:14:52.351Z\", \"hypothesis\": \"CRM obs_only with max_correction_norm=0.2 on LIBERO-Spatial seed42 — ablation to isolate effect of norm clipping magnitude. Norm=0.2 should reduce overcorrection compared to default, improving SR on tasks where CRM overshoots.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla+crm_3suite_v1\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}, \"metrics\": {\"success_rate\": 0.79, \"per_task_sr\": {\"between_plate_ramekin\": 1, \"next_to_ramekin\": 0.9, \"table_center\": 0.95, \"cookie_box\": 0.95, \"top_drawer\": 0.75, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"stove\": 0.95, \"next_to_plate\": 0.75, \"wooden_cabinet\": 0.65}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3262}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-23T06:15:52.197355+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau015-spatial-s42-r2",
  "field": "metrics",
  "value": "{'success_rate': 0.805, 'trigger_rate': 0.407, 'mean_unc': 0.1852, 'per_task_sr': {'between_plate_ramekin': 1, 'next_to_ramekin': 0.9, 'table_center': 0.95, 'cookie_box': 0.95, 'top_drawer': 0.75, 'on_ramekin': 0, 'next_to_cookie_box': 0.95, 'stove': 0.9, 'next_to_plate': 0.8, 'wooden_cabinet': 0.85}}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-adapt-tau015-spatial-s42-r2",
    "field": "metrics",
    "value": "{'success_rate': 0.805, 'trigger_rate': 0.407, 'mean_unc': 0.1852, 'per_task_sr': {'between_plate_ramekin': 1, 'next_to_ramekin': 0.9, 'table_center': 0.95, 'cookie_box': 0.95, 'top_drawer': 0.75, 'on_ramekin': 0, 'next_to_cookie_box': 0.95, 'stove': 0.9, 'next_to_plate': 0.8, 'wooden_cabinet': 0.85}}"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-23T06:15:52.197541+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau015-spatial-s42-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T06:13:51.160Z\", \"updated_at\": \"2026-05-23T06:14:53.323Z\", \"hypothesis\": \"Adaptive conformal CRM with tau=0.15 (norm=0.2) on LIBERO-Spatial seed42 — threshold sweep supplementary experiment. Very low tau triggers CRM on most steps (high trigger rate), testing whether aggressive correction helps or hurts.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.15 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla+crm_3suite_v1\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}, \"metrics\": {\"success_rate\": 0.805, \"trigger_rate\": 0.407, \"mean_unc\": 0.1852, \"per_task_sr\": {\"between_plate_ramekin\": 1, \"next_to_ramekin\": 0.9, \"table_center\": 0.95, \"cookie_box\": 0.95, \"top_drawer\": 0.75, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.95, \"stove\": 0.9, \"next_to_plate\": 0.8, \"wooden_cabinet\": 0.85}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2792}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-23T06:15:52.197744+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau035-spatial-s42-r2",
  "field": "metrics",
  "value": "{'success_rate': 0.8, 'trigger_rate': 0.122, 'mean_unc': 0.1873, 'per_task_sr': {'between_plate_ramekin': 0.95, 'next_to_ramekin': 1, 'table_center': 0.9, 'cookie_box': 0.95, 'top_drawer': 0.7, 'on_ramekin': 0, 'next_to_cookie_box': 0.95, 'stove': 0.85, 'next_to_plate': 0.85, 'wooden_cabinet': 0.85}}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-adapt-tau035-spatial-s42-r2",
    "field": "metrics",
    "value": "{'success_rate': 0.8, 'trigger_rate': 0.122, 'mean_unc': 0.1873, 'per_task_sr': {'between_plate_ramekin': 0.95, 'next_to_ramekin': 1, 'table_center': 0.9, 'cookie_box': 0.95, 'top_drawer': 0.7, 'on_ramekin': 0, 'next_to_cookie_box': 0.95, 'stove': 0.85, 'next_to_plate': 0.85, 'wooden_cabinet': 0.85}}"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-23T06:15:52.197926+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau035-spatial-s42-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T06:13:52.718Z\", \"updated_at\": \"2026-05-23T06:15:11.540Z\", \"hypothesis\": \"Adaptive conformal CRM with tau=0.35 (norm=0.2) on LIBERO-Spatial seed42 — threshold sweep supplementary experiment. Higher tau reduces trigger rate, testing whether more selective conformal triggering improves precision.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.35 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla+crm_3suite_v1\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}, \"metrics\": {\"success_rate\": 0.8, \"trigger_rate\": 0.122, \"mean_unc\": 0.1873, \"per_task_sr\": {\"between_plate_ramekin\": 0.95, \"next_to_ramekin\": 1, \"table_center\": 0.9, \"cookie_box\": 0.95, \"top_drawer\": 0.7, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.95, \"stove\": 0.85, \"next_to_plate\": 0.85, \"wooden_cabinet\": 0.85}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2665}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-23T06:15:52.198082+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau025-spatial-s42-r2",
  "field": "log_path",
  "value": "~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau025-spatial-s42-r2.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-adapt-tau025-spatial-s42-r2",
    "field": "log_path",
    "value": "~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau025-spatial-s42-r2.log"
  }
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-23T06:15:52.198214+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm02-spatial-s42-r2",
  "field": "log_path",
  "value": "~/runs/acr-vla-conformal-refinement/eval-supp-crm-norm02-spatial-s42-r2.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm02-spatial-s42-r2",
    "field": "log_path",
    "value": "~/runs/acr-vla-conformal-refinement/eval-supp-crm-norm02-spatial-s42-r2.log"
  }
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-23T06:15:52.198399+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau025-spatial-s42-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T06:13:46.810Z\", \"updated_at\": \"2026-05-23T06:15:16.529Z\", \"hypothesis\": \"Adaptive conformal CRM with tau=0.25 (norm=0.2) on LIBERO-Spatial seed42 — threshold sweep supplementary experiment. Lower tau increases trigger rate and correction frequency; tau=0.25 should balance precision vs coverage for conformal triggering.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.25 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla+crm_3suite_v1\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}, \"metrics\": {\"success_rate\": 0.82, \"trigger_rate\": 0.194, \"mean_unc\": 0.1847, \"per_task_sr\": {\"between_plate_ramekin\": 0.95, \"next_to_ramekin\": 0.95, \"table_center\": 1, \"cookie_box\": 1, \"top_drawer\": 0.75, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"stove\": 0.9, \"next_to_plate\": 0.9, \"wooden_cabinet\": 0.85}}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau025-spatial-s42-r2.log\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3137}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-23T06:15:52.198562+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau015-spatial-s42-r2",
  "field": "log_path",
  "value": "~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau015-spatial-s42-r2.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-adapt-tau015-spatial-s42-r2",
    "field": "log_path",
    "value": "~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau015-spatial-s42-r2.log"
  }
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-23T06:15:52.198709+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau035-spatial-s42-r2",
  "field": "log_path",
  "value": "~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau035-spatial-s42-r2.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-adapt-tau035-spatial-s42-r2",
    "field": "log_path",
    "value": "~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau035-spatial-s42-r2.log"
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-23T06:15:52.198872+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm02-spatial-s42-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T06:13:49.420Z\", \"updated_at\": \"2026-05-23T06:15:16.880Z\", \"hypothesis\": \"CRM obs_only with max_correction_norm=0.2 on LIBERO-Spatial seed42 — ablation to isolate effect of norm clipping magnitude. Norm=0.2 should reduce overcorrection compared to default, improving SR on tasks where CRM overshoots.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla+crm_3suite_v1\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}, \"metrics\": {\"success_rate\": 0.79, \"per_task_sr\": {\"between_plate_ramekin\": 1, \"next_to_ramekin\": 0.9, \"table_center\": 0.95, \"cookie_box\": 0.95, \"top_drawer\": 0.75, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"stove\": 0.95, \"next_to_plate\": 0.75, \"wooden_cabinet\": 0.65}}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-crm-norm02-spatial-s42-r2.log\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3378}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 91 · 2026-05-23T06:15:52.199059+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau015-spatial-s42-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T06:13:51.160Z\", \"updated_at\": \"2026-05-23T06:15:17.205Z\", \"hypothesis\": \"Adaptive conformal CRM with tau=0.15 (norm=0.2) on LIBERO-Spatial seed42 — threshold sweep supplementary experiment. Very low tau triggers CRM on most steps (high trigger rate), testing whether aggressive correction helps or hurts.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.15 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla+crm_3suite_v1\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}, \"metrics\": {\"success_rate\": 0.805, \"trigger_rate\": 0.407, \"mean_unc\": 0.1852, \"per_task_sr\": {\"between_plate_ramekin\": 1, \"next_to_ramekin\": 0.9, \"table_center\": 0.95, \"cookie_box\": 0.95, \"top_drawer\": 0.75, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.95, \"stove\": 0.9, \"next_to_plate\": 0.8, \"wooden_cabinet\": 0.85}}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau015-spatial-s42-r2.log\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2763}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-23T06:15:52.199242+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau035-spatial-s42-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T06:13:52.718Z\", \"updated_at\": \"2026-05-23T06:15:17.490Z\", \"hypothesis\": \"Adaptive conformal CRM with tau=0.35 (norm=0.2) on LIBERO-Spatial seed42 — threshold sweep supplementary experiment. Higher tau reduces trigger rate, testing whether more selective conformal triggering improves precision.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.35 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla+crm_3suite_v1\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}, \"metrics\": {\"success_rate\": 0.8, \"trigger_rate\": 0.122, \"mean_unc\": 0.1873, \"per_task_sr\": {\"between_plate_ramekin\": 0.95, \"next_to_ramekin\": 1, \"table_center\": 0.9, \"cookie_box\": 0.95, \"top_drawer\": 0.7, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.95, \"stove\": 0.85, \"next_to_plate\": 0.85, \"wooden_cabinet\": 0.85}}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau035-spatial-s42-r2.log\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2673}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-23T06:15:52.199443+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau025-spatial-s42-r2",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-adapt-tau025-spatial-s42-r2",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt"
  }
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-23T06:15:52.199613+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau025-spatial-s42-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T06:13:46.810Z\", \"updated_at\": \"2026-05-23T06:15:21.346Z\", \"hypothesis\": \"Adaptive conformal CRM with tau=0.25 (norm=0.2) on LIBERO-Spatial seed42 — threshold sweep supplementary experiment. Lower tau increases trigger rate and correction frequency; tau=0.25 should balance precision vs coverage for conformal triggering.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.25 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla+crm_3suite_v1\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}, \"metrics\": {\"success_rate\": 0.82, \"trigger_rate\": 0.194, \"mean_unc\": 0.1847, \"per_task_sr\": {\"between_plate_ramekin\": 0.95, \"next_to_ramekin\": 0.95, \"table_center\": 1, \"cookie_box\": 1, \"top_drawer\": 0.75, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"stove\": 0.9, \"next_to_plate\": 0.9, \"wooden_cabinet\": 0.85}}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau025-spatial-s42-r2.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2724}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-23T06:15:52.199759+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm02-spatial-s42-r2",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm02-spatial-s42-r2",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt"
  }
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-23T06:15:52.199929+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm02-spatial-s42-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T06:13:49.420Z\", \"updated_at\": \"2026-05-23T06:15:22.242Z\", \"hypothesis\": \"CRM obs_only with max_correction_norm=0.2 on LIBERO-Spatial seed42 — ablation to isolate effect of norm clipping magnitude. Norm=0.2 should reduce overcorrection compared to default, improving SR on tasks where CRM overshoots.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla+crm_3suite_v1\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}, \"metrics\": {\"success_rate\": 0.79, \"per_task_sr\": {\"between_plate_ramekin\": 1, \"next_to_ramekin\": 0.9, \"table_center\": 0.95, \"cookie_box\": 0.95, \"top_drawer\": 0.75, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"stove\": 0.95, \"next_to_plate\": 0.75, \"wooden_cabinet\": 0.65}}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-crm-norm02-spatial-s42-r2.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2605}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-23T06:15:52.200093+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau015-spatial-s42-r2",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-adapt-tau015-spatial-s42-r2",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt"
  }
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-23T06:15:52.200321+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau015-spatial-s42-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T06:13:51.160Z\", \"updated_at\": \"2026-05-23T06:15:23.181Z\", \"hypothesis\": \"Adaptive conformal CRM with tau=0.15 (norm=0.2) on LIBERO-Spatial seed42 — threshold sweep supplementary experiment. Very low tau triggers CRM on most steps (high trigger rate), testing whether aggressive correction helps or hurts.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.15 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla+crm_3suite_v1\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}, \"metrics\": {\"success_rate\": 0.805, \"trigger_rate\": 0.407, \"mean_unc\": 0.1852, \"per_task_sr\": {\"between_plate_ramekin\": 1, \"next_to_ramekin\": 0.9, \"table_center\": 0.95, \"cookie_box\": 0.95, \"top_drawer\": 0.75, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.95, \"stove\": 0.9, \"next_to_plate\": 0.8, \"wooden_cabinet\": 0.85}}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau015-spatial-s42-r2.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.264}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-23T06:15:52.200526+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau035-spatial-s42-r2",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-adapt-tau035-spatial-s42-r2",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt"
  }
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-23T06:15:52.200720+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau035-spatial-s42-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T06:13:52.718Z\", \"updated_at\": \"2026-05-23T06:15:24.072Z\", \"hypothesis\": \"Adaptive conformal CRM with tau=0.35 (norm=0.2) on LIBERO-Spatial seed42 — threshold sweep supplementary experiment. Higher tau reduces trigger rate, testing whether more selective conformal triggering improves precision.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.35 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla+crm_3suite_v1\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}, \"metrics\": {\"success_rate\": 0.8, \"trigger_rate\": 0.122, \"mean_unc\": 0.1873, \"per_task_sr\": {\"between_plate_ramekin\": 0.95, \"next_to_ramekin\": 1, \"table_center\": 0.9, \"cookie_box\": 0.95, \"top_drawer\": 0.7, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.95, \"stove\": 0.85, \"next_to_plate\": 0.85, \"wooden_cabinet\": 0.85}}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau035-spatial-s42-r2.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2763}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-23T06:15:52.200928+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau025-spatial-s42-r2",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-adapt-tau025-spatial-s42-r2",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool call

_source line 102 · 2026-05-23T06:15:52.201062+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm02-spatial-s42-r2",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm02-spatial-s42-r2",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 103 · 2026-05-23T06:15:52.201220+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau025-spatial-s42-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T06:13:46.810Z\", \"updated_at\": \"2026-05-23T06:15:28.721Z\", \"hypothesis\": \"Adaptive conformal CRM with tau=0.25 (norm=0.2) on LIBERO-Spatial seed42 — threshold sweep supplementary experiment. Lower tau increases trigger rate and correction frequency; tau=0.25 should balance precision vs coverage for conformal triggering.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.25 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla+crm_3suite_v1\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}, \"metrics\": {\"success_rate\": 0.82, \"trigger_rate\": 0.194, \"mean_unc\": 0.1847, \"per_task_sr\": {\"between_plate_ramekin\": 0.95, \"next_to_ramekin\": 0.95, \"table_center\": 1, \"cookie_box\": 1, \"top_drawer\": 0.75, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"stove\": 0.9, \"next_to_plate\": 0.9, \"wooden_cabinet\": 0.85}}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau025-spatial-s42-r2.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5341}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-23T06:15:52.201447+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm02-spatial-s42-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T06:13:49.420Z\", \"updated_at\": \"2026-05-23T06:15:29.305Z\", \"hypothesis\": \"CRM obs_only with max_correction_norm=0.2 on LIBERO-Spatial seed42 — ablation to isolate effect of norm clipping magnitude. Norm=0.2 should reduce overcorrection compared to default, improving SR on tasks where CRM overshoots.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla+crm_3suite_v1\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}, \"metrics\": {\"success_rate\": 0.79, \"per_task_sr\": {\"between_plate_ramekin\": 1, \"next_to_ramekin\": 0.9, \"table_center\": 0.95, \"cookie_box\": 0.95, \"top_drawer\": 0.75, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"stove\": 0.95, \"next_to_plate\": 0.75, \"wooden_cabinet\": 0.65}}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-crm-norm02-spatial-s42-r2.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5416}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-23T06:15:52.201601+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau015-spatial-s42-r2",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-adapt-tau015-spatial-s42-r2",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-23T06:15:52.201758+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau015-spatial-s42-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T06:13:51.160Z\", \"updated_at\": \"2026-05-23T06:15:30.142Z\", \"hypothesis\": \"Adaptive conformal CRM with tau=0.15 (norm=0.2) on LIBERO-Spatial seed42 — threshold sweep supplementary experiment. Very low tau triggers CRM on most steps (high trigger rate), testing whether aggressive correction helps or hurts.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.15 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla+crm_3suite_v1\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}, \"metrics\": {\"success_rate\": 0.805, \"trigger_rate\": 0.407, \"mean_unc\": 0.1852, \"per_task_sr\": {\"between_plate_ramekin\": 1, \"next_to_ramekin\": 0.9, \"table_center\": 0.95, \"cookie_box\": 0.95, \"top_drawer\": 0.75, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.95, \"stove\": 0.9, \"next_to_plate\": 0.8, \"wooden_cabinet\": 0.85}}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau015-spatial-s42-r2.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5999}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 107 · 2026-05-23T06:15:52.201907+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau035-spatial-s42-r2",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-adapt-tau035-spatial-s42-r2",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 108 · 2026-05-23T06:15:52.202062+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau035-spatial-s42-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T06:13:52.718Z\", \"updated_at\": \"2026-05-23T06:15:32.186Z\", \"hypothesis\": \"Adaptive conformal CRM with tau=0.35 (norm=0.2) on LIBERO-Spatial seed42 — threshold sweep supplementary experiment. Higher tau reduces trigger rate, testing whether more selective conformal triggering improves precision.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.35 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla+crm_3suite_v1\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}, \"metrics\": {\"success_rate\": 0.8, \"trigger_rate\": 0.122, \"mean_unc\": 0.1873, \"per_task_sr\": {\"between_plate_ramekin\": 0.95, \"next_to_ramekin\": 1, \"table_center\": 0.9, \"cookie_box\": 0.95, \"top_drawer\": 0.7, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.95, \"stove\": 0.85, \"next_to_plate\": 0.85, \"wooden_cabinet\": 0.85}}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau035-spatial-s42-r2.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.264}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 109 · 2026-05-23T06:15:52.202229+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau025-spatial-s42-r2",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-adapt-tau025-spatial-s42-r2",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 110 · 2026-05-23T06:15:52.202459+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau025-spatial-s42-r2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T06:13:46.810Z\", \"updated_at\": \"2026-05-23T06:15:35.291Z\", \"hypothesis\": \"Adaptive conformal CRM with tau=0.25 (norm=0.2) on LIBERO-Spatial seed42 — threshold sweep supplementary experiment. Lower tau increases trigger rate and correction frequency; tau=0.25 should balance precision vs coverage for conformal triggering.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.25 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla+crm_3suite_v1\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}, \"metrics\": {\"success_rate\": 0.82, \"trigger_rate\": 0.194, \"mean_unc\": 0.1847, \"per_task_sr\": {\"between_plate_ramekin\": 0.95, \"next_to_ramekin\": 0.95, \"table_center\": 1, \"cookie_box\": 1, \"top_drawer\": 0.75, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"stove\": 0.9, \"next_to_plate\": 0.9, \"wooden_cabinet\": 0.85}}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau025-spatial-s42-r2.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T06:15:35.291Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6652}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 111 · 2026-05-23T06:15:52.202626+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm02-spatial-s42-r2",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm02-spatial-s42-r2",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 112 · 2026-05-23T06:15:52.202815+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm02-spatial-s42-r2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T06:13:49.420Z\", \"updated_at\": \"2026-05-23T06:15:36.158Z\", \"hypothesis\": \"CRM obs_only with max_correction_norm=0.2 on LIBERO-Spatial seed42 — ablation to isolate effect of norm clipping magnitude. Norm=0.2 should reduce overcorrection compared to default, improving SR on tasks where CRM overshoots.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla+crm_3suite_v1\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}, \"metrics\": {\"success_rate\": 0.79, \"per_task_sr\": {\"between_plate_ramekin\": 1, \"next_to_ramekin\": 0.9, \"table_center\": 0.95, \"cookie_box\": 0.95, \"top_drawer\": 0.75, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"stove\": 0.95, \"next_to_plate\": 0.75, \"wooden_cabinet\": 0.65}}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-crm-norm02-spatial-s42-r2.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T06:15:36.158Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4574}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 113 · 2026-05-23T06:15:52.202969+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau015-spatial-s42-r2",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-adapt-tau015-spatial-s42-r2",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool call

_source line 114 · 2026-05-23T06:15:52.203101+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau035-spatial-s42-r2",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-adapt-tau035-spatial-s42-r2",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 115 · 2026-05-23T06:15:52.203291+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau015-spatial-s42-r2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T06:13:51.160Z\", \"updated_at\": \"2026-05-23T06:15:37.282Z\", \"hypothesis\": \"Adaptive conformal CRM with tau=0.15 (norm=0.2) on LIBERO-Spatial seed42 — threshold sweep supplementary experiment. Very low tau triggers CRM on most steps (high trigger rate), testing whether aggressive correction helps or hurts.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.15 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla+crm_3suite_v1\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}, \"metrics\": {\"success_rate\": 0.805, \"trigger_rate\": 0.407, \"mean_unc\": 0.1852, \"per_task_sr\": {\"between_plate_ramekin\": 1, \"next_to_ramekin\": 0.9, \"table_center\": 0.95, \"cookie_box\": 0.95, \"top_drawer\": 0.75, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.95, \"stove\": 0.9, \"next_to_plate\": 0.8, \"wooden_cabinet\": 0.85}}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau015-spatial-s42-r2.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T06:15:37.282Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8633}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 116 · 2026-05-23T06:15:52.203495+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau035-spatial-s42-r2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T06:13:52.718Z\", \"updated_at\": \"2026-05-23T06:15:38.149Z\", \"hypothesis\": \"Adaptive conformal CRM with tau=0.35 (norm=0.2) on LIBERO-Spatial seed42 — threshold sweep supplementary experiment. Higher tau reduces trigger rate, testing whether more selective conformal triggering improves precision.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.35 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla+crm_3suite_v1\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}, \"metrics\": {\"success_rate\": 0.8, \"trigger_rate\": 0.122, \"mean_unc\": 0.1873, \"per_task_sr\": {\"between_plate_ramekin\": 0.95, \"next_to_ramekin\": 1, \"table_center\": 0.9, \"cookie_box\": 0.95, \"top_drawer\": 0.7, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.95, \"stove\": 0.85, \"next_to_plate\": 0.85, \"wooden_cabinet\": 0.85}}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau035-spatial-s42-r2.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T06:15:38.149Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.861}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 117 · 2026-05-23T06:15:52.203707+00:00_

4 个实验全部收割完毕，registry 已更新为 DONE。

## 汇总表

| exp_id | mode | SR | vs baseline | trigger_rate | conclusion | GPU 释放 |
|--------|------|----|-------------|-------------|------------|----------|
| eval-supp-adapt-tau025-spatial-s42-r2 | adaptive_conformal, tau=0.25 | **82.0%** | +3.5pp | 19.4% | success | cuda:2 已空闲 |
| eval-supp-crm-norm02-spatial-s42-r2 | crm_obs_only, norm=0.2 | **79.0%** | +0.5pp | — | success | cuda:0 已空闲 |
| eval-supp-adapt-tau015-spatial-s42-r2 | adaptive_conformal, tau=0.15 | **80.5%** | +2.0pp | 40.7% | success | cuda:1 已空闲 |
| eval-supp-adapt-tau035-spatial-s42-r2 | adaptive_conformal, tau=0.35 | **80.0%** | +1.5pp | 12.2% | success | cuda:4 刚释放 |

## Threshold sweep 趋势

| tau | SR | trigger_rate | 解读 |
|-----|-----|-------------|------|
| 0.15 | 80.5% | 40.7% | 触发太频繁，overcorrection 拉低 SR |
| 0.25 | **82.0%** | 19.4% | 最优平衡点 |
| 0.35 | 80.0% | 12.2% | 触发太保守，miss 可纠正的 step |

**tau=0.25 是最优 threshold**，符合 Director 预期 (82%)。CRM norm=0.2 = 79.0%，也符合预期 (79%)。

## GPU 状态

- cuda:0,1,2 — 完全空闲 (2 MiB)
- cuda:3 — 低负载 (544 MiB, 10% util)，可能是其他进程
- cuda:4 — tau=0.35 刚完成，进程将退出释放
- cuda:5 — 有负载 (2008 MiB, 26% util)，非本批实验

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_harvest_tau-sweep-bjb1_20260523T061143"
}
```

</details>

---
