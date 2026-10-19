# check d088 eval status urgent

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 0
- **Tool calls:** 14
- **Original source:** `logs/chats/worker_check_d088-eval-status-urgent_20260520T173003.jsonl`
- **Structured JSON:** [`8f4c984530f021d710d0.json`](../../sessions/8f/8f4c984530f021d710d0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

29 recorded events

### Tool call

_source line 1 · 2026-05-20T17:31:04.222012+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_d088-eval-status-urgent_20260520T173003",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T17:31:04.223448+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_d088-eval-status-urgent_20260520T173003",
  "tool": "ToolSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T17:31:04.223766+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "ps -p 741948,742213,728278 -o pid,etime,cmd 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_d088-eval-status-urgent_20260520T173003",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "ps -p 741948,742213,728278 -o pid,etime,cmd 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T17:31:04.223993+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_d088-eval-status-urgent_20260520T173003",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T17:31:04.224202+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "ls -la /root/acr-vla-conformal-refinement/logs/eval_adaptive_unc_head_object_seed4*.json 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_d088-eval-status-urgent_20260520T173003",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "ls -la /root/acr-vla-conformal-refinement/logs/eval_adaptive_unc_head_object_seed4*.json 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T17:31:04.224580+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_d088-eval-status-urgent_20260520T173003",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T17:31:04.224814+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "ps -p 365151 -o pid,etime,cmd 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_d088-eval-status-urgent_20260520T173003",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "ps -p 365151 -o pid,etime,cmd 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T17:31:04.225019+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_d088-eval-status-urgent_20260520T173003",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T17:31:04.225218+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "ls /root/autodl-tmp/crm_cache_k1_openvla/object/ 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_d088-eval-status-urgent_20260520T173003",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "ls /root/autodl-tmp/crm_cache_k1_openvla/object/ 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T17:31:04.225470+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_d088-eval-status-urgent_20260520T173003",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T17:31:04.225781+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "ps -p 741948,742213,728278 -o pid,etime,cmd",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_d088-eval-status-urgent_20260520T173003",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "ps -p 741948,742213,728278 -o pid,etime,cmd",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T17:31:04.226046+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"   PID     ELAPSED CMD\\n728278       30:53 bash -c cd /root/acr-vla-conformal-refinement && nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=5 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 44 --n_rollouts 10 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed44.json 2>&1 | tee logs/eval-adaptive-unc-head-object-seed44.log' > /tmp/nohup_eval_unc_seed44.log 2>&1 & echo $!\\n741948       09:52 bash -c export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 42 --n_rollouts 10 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed42.json 2>&1 | tee logs/eval-adaptive-unc-head-object-seed42.log\\n742213       09:50 bash -c export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 43 --n_rollouts 10 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_h
…[truncated 360 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_d088-eval-status-urgent_20260520T173003",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T17:31:04.226315+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "ls -la /root/acr-vla-conformal-refinement/logs/eval_adaptive_unc_head_object_seed42.json /root/acr-vla-conformal-refinement/logs/eval_adaptive_unc_head_object_seed43.json /root/acr-vla-conformal-refinement/logs/eval_adaptive_unc_head_object_seed44.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_d088-eval-status-urgent_20260520T173003",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "ls -la /root/acr-vla-conformal-refinement/logs/eval_adaptive_unc_head_object_seed42.json /root/acr-vla-conformal-refinement/logs/eval_adaptive_unc_head_object_seed43.json /root/acr-vla-conformal-refinement/logs/eval_adaptive_unc_head_object_seed44.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T17:31:04.226608+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "ps -p 365151 -o pid,etime,cmd",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_d088-eval-status-urgent_20260520T173003",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "ps -p 365151 -o pid,etime,cmd",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T17:31:04.226816+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "ls /root/autodl-tmp/crm_cache_k1_openvla/object/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_d088-eval-status-urgent_20260520T173003",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "ls /root/autodl-tmp/crm_cache_k1_openvla/object/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T17:31:04.227021+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/acr-vla-conformal-refinement/logs/eval_adaptive_unc_head_object_seed42.json': No such file or directory\\nls: cannot access '/root/acr-vla-conformal-refinement/logs/eval_adaptive_unc_head_object_seed43.json': No such file or directory\\nls: cannot access '/root/acr-vla-conformal-refinement/logs/eval_adaptive_unc_head_object_seed44.json': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_d088-eval-status-urgent_20260520T173003",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-20T17:31:04.227243+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"   PID     ELAPSED CMD\\n365151    03:41:06 python precompute_openvla.py --device cuda:0 --max_demos_per_task 50 --cache_dir /root/autodl-tmp/crm_cache_k1_openvla/\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_d088-eval-status-urgent_20260520T173003",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T17:31:04.227714+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"sample_000000.pt\\nsample_000001.pt\\nsample_000002.pt\\nsample_000003.pt\\nsample_000004.pt\\nsample_000005.pt\\nsample_000006.pt\\nsample_000007.pt\\nsample_000008.pt\\nsample_000009.pt\\nsample_000010.pt\\nsample_000011.pt\\nsample_000012.pt\\nsample_000013.pt\\nsample_000014.pt\\nsample_000015.pt\\nsample_000016.pt\\nsample_000017.pt\\nsample_000018.pt\\nsample_000019.pt\\nsample_000020.pt\\nsample_000021.pt\\nsample_000022.pt\\nsample_000023.pt\\nsample_000024.pt\\nsample_000025.pt\\nsample_000026.pt\\nsample_000027.pt\\nsample_000028.pt\\nsample_000029.pt\\nsample_000030.pt\\nsample_000031.pt\\nsample_000032.pt\\nsample_000033.pt\\nsample_000034.pt\\nsample_000035.pt\\nsample_000036.pt\\nsample_000037.pt\\nsample_000038.pt\\nsample_000039.pt\\nsample_000040.pt\\nsample_000041.pt\\nsample_000042.pt\\nsample_000043.pt\\nsample_000044.pt\\nsample_000045.pt\\nsample_000046.pt\\nsample_000047.pt\\nsample_000048.pt\\nsample_000049.pt\\nsample_000050.pt\\nsample_000051.pt\\nsample_000052.pt\\nsample_000053.pt\\nsample_000054.pt\\nsample_000055.pt\\nsample_000056.pt\\nsample_000057.pt\\nsample_000058.pt\\nsample_000059.pt\\nsample_000060.pt\\nsample_000061.pt\\nsample_000062.pt\\nsample_000063.pt\\nsample_000064.pt\\nsample_000065.pt\\nsample_000066.pt\\nsample_000067.pt\\nsample_000068.pt\\nsample_000069.pt\\nsample_000070.pt\\nsample_000071.pt\\nsample_000072.pt\\nsample_000073.pt\\nsample_000074.pt\\nsample_000075.pt\\nsample_000076.pt\\nsample_000077.pt\\nsample_000078.pt\\nsample_000079.pt\\nsample_000080.pt\\nsample_000081.pt\\nsample_000082.pt\\nsample_000083.pt\\nsample_000084.pt\\nsample_000085.pt\\nsample_000086.pt\\nsample_000087.pt\\nsample_000088.pt\\nsample_000089.pt\\nsample_000090.pt\\nsample_000091.pt\\nsample_000092.pt\\nsample_000093.pt\\nsample_000094.pt\\nsample_000095.pt\\nsample_000096.pt\\nsample_000097.pt\\nsample_000098.pt\\nsample_000099.pt\\nsample_000100.pt\\nsample_000101.pt\\nsample
…[truncated 7146 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_d088-eval-status-urgent_20260520T173003",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T17:31:04.228015+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "tail -20 /root/acr-vla-conformal-refinement/logs/eval-adaptive-unc-head-object-seed42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_d088-eval-status-urgent_20260520T173003",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "tail -20 /root/acr-vla-conformal-refinement/logs/eval-adaptive-unc-head-object-seed42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T17:31:04.228260+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt', 'n_rollouts': 10, 'max_steps': 300, 'seed': 42, 'K': 1, 'mode': 'adaptive_unc_head', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'obs_dim': 960, 'hidden_dim': 256, 'render': False, 'output_file': 'logs/eval_adaptive_unc_head_object_seed42.json', 'max_correction_norm': 0.2, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': '/root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt', 'unc_threshold': 0.42}\\n[eval] Mode: adaptive_unc_head, benchmark: object\\n[eval] Loading SmolVLA from /root/autodl-tmp/models/smolvla_libero/...\\nLoading  /root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct weights ...\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/489 [00:00<?, ?it/s]\\rLoading weights:  34%|███▎      | 164/489 [00:00<00:00, 1555.49it/s]\\rLoading weights: 100%|██████████| 489/489 [00:00<00:00, 2967.04it/s]\\nReducing the number of VLM layers to 16 ...\\nLoading weights from local directory\\n[eval] CRM loaded from /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt (327,198 params)\\n[eval] Override max_correction_norm = 0.2\\n[eval] UncertaintyHead loaded from /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt (15,665 params), threshold=0.42\\n[eval] Loading LIBERO object environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 5/10, success so far: 0/5\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_d088-eval-status-urgent_20260520T173003",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T17:31:04.228537+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "tail -20 /root/acr-vla-conformal-refinement/logs/eval-adaptive-unc-head-object-seed43.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_d088-eval-status-urgent_20260520T173003",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "tail -20 /root/acr-vla-conformal-refinement/logs/eval-adaptive-unc-head-object-seed43.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-20T17:31:04.228873+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt', 'n_rollouts': 10, 'max_steps': 300, 'seed': 43, 'K': 1, 'mode': 'adaptive_unc_head', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'obs_dim': 960, 'hidden_dim': 256, 'render': False, 'output_file': 'logs/eval_adaptive_unc_head_object_seed43.json', 'max_correction_norm': 0.2, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': '/root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt', 'unc_threshold': 0.42}\\n[eval] Mode: adaptive_unc_head, benchmark: object\\n[eval] Loading SmolVLA from /root/autodl-tmp/models/smolvla_libero/...\\nLoading  /root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct weights ...\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/489 [00:00<?, ?it/s]\\rLoading weights:  36%|███▌      | 175/489 [00:00<00:00, 1745.18it/s]\\rLoading weights:  77%|███████▋  | 377/489 [00:00<00:00, 1901.24it/s]\\rLoading weights: 100%|██████████| 489/489 [00:00<00:00, 2034.77it/s]\\nReducing the number of VLM layers to 16 ...\\nLoading weights from local directory\\n[eval] CRM loaded from /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt (327,198 params)\\n[eval] Override max_correction_norm = 0.2\\n[eval] UncertaintyHead loaded from /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt (15,665 params), threshold=0.42\\n[eval] Loading LIBERO object environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 5/10, success so far: 0/5\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_d088-eval-status-urgent_20260520T173003",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T17:31:04.229141+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "tail -20 /root/acr-vla-conformal-refinement/logs/eval-adaptive-unc-head-object-seed44.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_d088-eval-status-urgent_20260520T173003",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "tail -20 /root/acr-vla-conformal-refinement/logs/eval-adaptive-unc-head-object-seed44.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-20T17:31:04.229424+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt', 'n_rollouts': 100, 'max_steps': 300, 'seed': 44, 'K': 1, 'mode': 'adaptive_unc_head', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'obs_dim': 960, 'hidden_dim': 256, 'render': False, 'output_file': 'logs/eval_adaptive_unc_head_object_seed44.json', 'max_correction_norm': 0.2, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': '/root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt', 'unc_threshold': 0.42}\\n[eval] Mode: adaptive_unc_head, benchmark: object\\n[eval] Loading SmolVLA from /root/autodl-tmp/models/smolvla_libero/...\\nLoading  /root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct weights ...\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/489 [00:00<?, ?it/s]\\rLoading weights:  35%|��██▍      | 171/489 [00:00<00:00, 1708.17it/s]\\rLoading weights:  70%|██████▉   | 342/489 [00:00<00:00, 1703.02it/s]\\rLoading weights: 100%|██████████| 489/489 [00:00<00:00, 1978.65it/s]\\nReducing the number of VLM layers to 16 ...\\nLoading weights from local directory\\n[eval] CRM loaded from /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt (327,198 params)\\n[eval] Override max_correction_norm = 0.2\\n[eval] UncertaintyHead loaded from /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt (15,665 params), threshold=0.42\\n[eval] Loading LIBERO object environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 5/100, success so far: 0/5\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 10/100, success so far: 0/10\\npick_up_the_alphabet_soup_and_place_it_in_the
…[truncated 408 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_d088-eval-status-urgent_20260520T173003",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T17:31:04.229667+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "find /root/autodl-tmp/crm_cache_k1_openvla/object/ -name \"*.pt\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_d088-eval-status-urgent_20260520T173003",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "find /root/autodl-tmp/crm_cache_k1_openvla/object/ -name \"*.pt\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-20T17:31:04.229872+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "tail -20 /root/runs/acr-vla-conformal-refinement/openvla-precompute-k1.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_d088-eval-status-urgent_20260520T173003",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "tail -20 /root/runs/acr-vla-conformal-refinement/openvla-precompute-k1.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-20T17:31:04.230227+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/crm_cache_k1_openvla/object/sample_030991.pt\\n/root/autodl-tmp/crm_cache_k1_openvla/object/sample_030992.pt\\n/root/autodl-tmp/crm_cache_k1_openvla/object/sample_030993.pt\\n/root/autodl-tmp/crm_cache_k1_openvla/object/sample_030994.pt\\n/root/autodl-tmp/crm_cache_k1_openvla/object/sample_030995.pt\\n/root/autodl-tmp/crm_cache_k1_openvla/object/sample_030996.pt\\n/root/autodl-tmp/crm_cache_k1_openvla/object/sample_030997.pt\\n/root/autodl-tmp/crm_cache_k1_openvla/object/sample_030998.pt\\n/root/autodl-tmp/crm_cache_k1_openvla/object/sample_030999.pt\\n/root/autodl-tmp/crm_cache_k1_openvla/object/sample_031000.pt\\n/root/autodl-tmp/crm_cache_k1_openvla/object/sample_031001.pt\\n/root/autodl-tmp/crm_cache_k1_openvla/object/sample_031002.pt\\n/root/autodl-tmp/crm_cache_k1_openvla/object/sample_031003.pt\\n/root/autodl-tmp/crm_cache_k1_openvla/object/sample_031004.pt\\n/root/autodl-tmp/crm_cache_k1_openvla/object/sample_031005.pt\\n/root/autodl-tmp/crm_cache_k1_openvla/object/sample_031006.pt\\n/root/autodl-tmp/crm_cache_k1_openvla/object/sample_031007.pt\\n/root/autodl-tmp/crm_cache_k1_openvla/object/sample_031008.pt\\n/root/autodl-tmp/crm_cache_k1_openvla/object/sample_031009.pt\\n/root/autodl-tmp/crm_cache_k1_openvla/object/sample_031010.pt\\n/root/autodl-tmp/crm_cache_k1_openvla/object/sample_031011.pt\\n/root/autodl-tmp/crm_cache_k1_openvla/object/sample_031012.pt\\n/root/autodl-tmp/crm_cache_k1_openvla/object/sample_031013.pt\\n/root/autodl-tmp/crm_cache_k1_openvla/object/sample_031014.pt\\n/root/autodl-tmp/crm_cache_k1_openvla/object/sample_031015.pt\\n/root/autodl-tmp/crm_cache_k1_openvla/object/sample_031016.pt\\n/root/autodl-tmp/crm_cache_k1_openvla/object/sample_031017.pt\\n/root/autodl-tmp/crm_cache_k1_openvla/object/sample_031018.pt\\n/root/autodl-tmp/crm_cache_k1_openvla/object/sample_031019.pt\\n/root/autodl-tmp/crm_cache_k1_openvla/object/sample_031020.pt\\n/root/autodl-tmp/crm_cac
…[truncated 6462 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_d088-eval-status-urgent_20260520T173003",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-20T17:31:04.230533+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  [object] 61400/74507 (5.0 samples/s, ETA: 44min)\\n  [object] 61600/74507 (5.0 samples/s, ETA: 43min)\\n  [object] 61800/74507 (5.0 samples/s, ETA: 43min)\\n  [object] 62000/74507 (5.0 samples/s, ETA: 42min)\\n  [object] 62200/74507 (5.0 samples/s, ETA: 41min)\\n  [object] 62400/74507 (5.0 samples/s, ETA: 41min)\\n  [object] 62600/74507 (5.0 samples/s, ETA: 40min)\\n  [object] 62800/74507 (5.0 samples/s, ETA: 39min)\\n  [object] 63000/74507 (5.0 samples/s, ETA: 39min)\\n  [object] 63200/74507 (4.9 samples/s, ETA: 38min)\\n  [object] 63400/74507 (5.0 samples/s, ETA: 37min)\\n  [object] 63600/74507 (5.0 samples/s, ETA: 37min)\\n  [object] 63800/74507 (5.0 samples/s, ETA: 36min)\\n  [object] 64000/74507 (5.0 samples/s, ETA: 35min)\\n  [object] 64200/74507 (5.0 samples/s, ETA: 35min)\\n  [object] 64400/74507 (5.0 samples/s, ETA: 34min)\\n  [object] 64600/74507 (5.0 samples/s, ETA: 33min)\\n  [object] 64800/74507 (5.0 samples/s, ETA: 33min)\\n  [object] 65000/74507 (5.0 samples/s, ETA: 32min)\\n  [object] 65200/74507 (5.0 samples/s, ETA: 31min)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_d088-eval-status-urgent_20260520T173003",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-20T17:31:04.230956+00:00_

## D088 Eval Results
| seed | PID | uptime | progress | status |
|------|-----|--------|----------|--------|
| seed42 | 741948 | 9m52s | task 1/10, rollout 5/10 | **RUNNING** |
| seed43 | 742213 | 9m50s | task 1/10, rollout 5/10 | **RUNNING** |
| seed44 | 728278 | 30m53s | task 2/10 done (task1=0%, task2=10%) | **RUNNING** |

JSON 均未生成。注意：**seed44 的 n_rollouts=100**（不是10），比其他两个慢 ~10x。

## OpenVLA Precompute
```
Status: RUNNING at 87.5% (65200/74507)
Speed:  5.0 samples/s
ETA:    ~31 min
PID:    365151 (uptime 3h41m)
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_check_d088-eval-status-urgent_20260520T173003"
}
```

</details>

---
