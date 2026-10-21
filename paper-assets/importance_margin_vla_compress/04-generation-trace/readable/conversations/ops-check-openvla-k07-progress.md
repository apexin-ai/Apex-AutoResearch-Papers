# ops check openvla k07 progress

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_ops_check_openvla_k07_progress_20260518T012051.jsonl`
- **Structured JSON:** [`ad09fe9b63eb9e51d14a.json`](../../sessions/ad/ad09fe9b63eb9e51d14a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-18T01:21:40.926083+00:00_

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
  "session": "worker_ops_check_openvla_k07_progress_20260518T012051",
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

_source line 2 · 2026-05-18T01:21:40.926584+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check_openvla_k07_progress_20260518T012051",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T01:21:40.926885+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "ps -p 755666 -o pid,stat,etime,cmd",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check_openvla_k07_progress_20260518T012051",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "ps -p 755666 -o pid,stat,etime,cmd",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-18T01:21:40.929185+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"   PID STAT     ELAPSED CMD\\n755666 S       01:15:38 bash -c cd /root/autodl-tmp/importance_margin_vla_compress && source /root/miniconda3/bin/activate && nohup python -u eval_openvla_libero.py --mode random_prune --k_ratio 0.7 --suite libero_object --num_episodes 50 --seed 7 > eval_results/openvla_random_prune_k07_object.log 2>&1 & echo \\\"PID=$!\\\"\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.27}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check_openvla_k07_progress_20260518T012051",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T01:21:40.929527+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-27271",
  "command": "find /root/autodl-tmp/importance_margin_vla_compress/ -name \"*k07*\" -o -name \"*pruning*k*0.7*\" 2>/dev/null | head -20",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check_openvla_k07_progress_20260518T012051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-27271",
    "command": "find /root/autodl-tmp/importance_margin_vla_compress/ -name \"*k07*\" -o -name \"*pruning*k*0.7*\" 2>/dev/null | head -20",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-18T01:21:40.929756+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-27271",
  "command": "nvidia-smi",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check_openvla_k07_progress_20260518T012051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-27271",
    "command": "nvidia-smi",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-18T01:21:40.929989+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/importance_margin_vla_compress/configs/libero_imm_twostage_fullft_k07.yaml\\n/root/autodl-tmp/importance_margin_vla_compress/configs/libero_acis_stage1only_k07.yaml\\n/root/autodl-tmp/importance_margin_vla_compress/logs/eval_stage1only_k07.log\\n/root/autodl-tmp/importance_margin_vla_compress/checkpoints/libero_imm_twostage_fullft_k07\\n/root/autodl-tmp/importance_margin_vla_compress/checkpoints/libero_acis_stage1only_k07\\n/root/autodl-tmp/importance_margin_vla_compress/eval_results/eval_imm_k07_object_acis_prune.json\\n/root/autodl-tmp/importance_margin_vla_compress/eval_results/eval_imm_k07_bypass_object.log\\n/root/autodl-tmp/importance_margin_vla_compress/eval_results/imm_k07_bypass_object.json\\n/root/autodl-tmp/importance_margin_vla_compress/eval_results/eval_k07_zero_mask.log\\n/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_random_prune_k07_object.json\\n/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_random_prune_k07_object.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check_openvla_k07_progress_20260518T012051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-18T01:21:40.930233+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "cat /root/autodl-tmp/importance_margin_vla_compress/artifacts/openvla_attention_entropy.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check_openvla_k07_progress_20260518T012051",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "cat /root/autodl-tmp/importance_margin_vla_compress/artifacts/openvla_attention_entropy.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-18T01:21:40.930503+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Mon May 18 09:21:08 2026       \\n+-----------------------------------------------------------------------------------------+\\n| NVIDIA-SMI 580.95.05              Driver Version: 580.95.05      CUDA Version: 13.0     |\\n+-----------------------------------------+------------------------+----------------------+\\n| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |\\n| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |\\n|                                         |                        |               MIG M. |\\n|=========================================+========================+======================|\\n|   0  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:A8:00.0 Off |                  Off |\\n| N/A   56C    P0            305W /  600W |   15980MiB /  97887MiB |     71%      Default |\\n|                                         |                        |             Disabled |\\n+-----------------------------------------+------------------------+----------------------+\\n|   1  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:B8:00.0 Off |                  Off |\\n| N/A   50C    P0            279W /  600W |   16108MiB /  97887MiB |     68%      Default |\\n|                                         |                        |             Disabled |\\n+-----------------------------------------+------------------------+----------------------+\\n\\n+-----------------------------------------------------------------------------------------+\\n| Processes:                                                                              |\\n|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |\\n|        ID   ID                                                               Usage      |\\n|=========================================================================================|\\n|    0   N/A  N/A          
…[truncated 359 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check_openvla_k07_progress_20260518T012051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-18T01:21:40.930836+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model\\\": \\\"OpenVLA (Llama-2 7B)\\\",\\n  \\\"n_vision_tokens\\\": 256,\\n  \\\"max_entropy_bits\\\": 8.0,\\n  \\\"n_samples\\\": 20,\\n  \\\"n_layers\\\": 32,\\n  \\\"n_heads\\\": 32,\\n  \\\"overall_mean_entropy\\\": 4.939382752787788,\\n  \\\"overall_std_entropy\\\": 1.7177960934044976,\\n  \\\"overall_entropy_ratio\\\": 0.6174228440984735,\\n  \\\"overall_vision_attn_fraction\\\": 0.09347279490316396,\\n  \\\"smolvla_entropy_ratio\\\": 0.98,\\n  \\\"per_layer_mean_entropy\\\": [\\n    7.889183443784714,\\n    7.705506944656372,\\n    6.781321092694998,\\n    6.588479212671518,\\n    6.6338807918131355,\\n    6.612360173463822,\\n    6.803562635183335,\\n    6.616292607039213,\\n    6.404642391949892,\\n    6.43172005340457,\\n    6.243048326298594,\\n    6.0511128447949885,\\n    5.350716729462147,\\n    5.223223012499512,\\n    5.181629741378129,\\n    5.342604849301279,\\n    4.837295683473348,\\n    4.202291099540889,\\n    3.969349375553429,\\n    3.801894642971456,\\n    3.6596607489511372,\\n    3.57459620218724,\\n    3.612714874744415,\\n    3.4020296612754466,\\n    2.9928100161254405,\\n    3.1141538904979824,\\n    3.047243582829833,\\n    3.186041377298534,\\n    2.9693243163637817,\\n    2.9733963487669826,\\n    3.043236758094281,\\n    3.814924660138786\\n  ],\\n  \\\"per_layer_std_entropy\\\": [\\n    0.043579970535024125,\\n    0.2080733540021285,\\n    0.5414623929823356,\\n    0.4569874093497661,\\n    0.5079827168213592,\\n    0.5952268263111063,\\n    0.35876517435481686,\\n    0.46124879760965803,\\n    0.49361448093315446,\\n    0.44163992661238805,\\n    0.4562331022159579,\\n    0.583081705141786,\\n    0.865760635789802,\\n    0.8741658044918388,\\n    0.9303554851486772,\\n    0.8678665878059033,\\n    0.670472109800004,\\n    0.8252506176870302,\\n    0.9046819503151653,\\n    0.7581969163645232,\\n    0.6773650616200502,\\n    0.8026298918855166,\\n    0.90178554512
…[truncated 2436 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check_openvla_k07_progress_20260518T012051",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T01:21:40.931120+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-27271",
  "command": "tail -80 /root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_random_prune_k07_object.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check_openvla_k07_progress_20260518T012051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-27271",
    "command": "tail -80 /root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_random_prune_k07_object.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-18T01:21:40.933538+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[*] Loading OpenVLA from: /root/autodl-tmp/openvla-libero-object\\n\\rLoading checkpoint shards:   0%|          | 0/4 [00:00<?, ?it/s]\\rLoading checkpoint shards:  50%|█████     | 2/4 [00:00<00:00, 12.49it/s]\\rLoading checkpoint shards: 100%|██████████| 4/4 [00:00<00:00, 14.53it/s]\\rLoading checkpoint shards: 100%|██████████| 4/4 [00:00<00:00, 14.17it/s]\\n[*] Model loaded, GPU: 15.1 GB\\n[*] Vision tokens: 256, dim: 4096\\n[*] Random pruning: k=0.7\\n[robosuite WARNING] No private macro file found! (__init__.py:7)\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[*] libero_object: 10 tasks x 50 episodes = 500 total\\n\\n[Task 1/10] pick up the alphabet soup and place it in the basket\\n[Pruning] 256 -> 179 vision tokens (k=0.7)\\n  Ep 10/50 task_sr=6/10 (1.9 eps/min)\\n  Ep 20/50 task_sr=15/20 (2.0 eps/min)\\n  Ep 30/50 task_sr=22/30 (2.0 eps/min)\\n  Ep 40/50 task_sr=31/40 (2.1 eps/min)\\n  Ep 50/50 task_sr=37/50 (2.0 eps/min)\\n  => Task SR: 0.740 (37/50)\\n\\n[Task 2/10] pick up the cream cheese and place it in the basket\\n  Ep 10/50 task_sr=1/10 (1.9 eps/min)\\n  Ep 20/50 task_sr=4/20 (1.9 eps/min)\\n  Ep 30/50 task_sr=6/30 (1.9 eps/min)\\n  Ep 40/50 task_sr=7/40 (1.9 eps/min)\\n  Ep 50/50 task_sr=9/50 (1.9 eps/min)\\n  => Task SR: 0.180 (9/50)\\n\\n[Task 3/10] pick up the salad dressing and place it in the basket\\n  Ep 10/50 task_sr=9/10 (1.9 eps/min)\\n  Ep 20/50 task_sr=17/20 (2.0 eps/min)\\n  Ep 30/50 task_sr=24/30 (2.0 eps/min)\\n  Ep 40/50 task_sr=29/40 (2.0 eps/min)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check_openvla_k07_progress_20260518T012051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T01:21:40.933823+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_random_prune_k07_object.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check_openvla_k07_progress_20260518T012051",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_random_prune_k07_object.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-18T01:21:40.934116+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model\\\": \\\"openvla-7b-libero-object\\\",\\n  \\\"mode\\\": \\\"random_prune\\\",\\n  \\\"suite\\\": \\\"libero_object\\\",\\n  \\\"k_ratio\\\": 0.7,\\n  \\\"overall_success_rate\\\": 0.3,\\n  \\\"total_successes\\\": 3,\\n  \\\"total_episodes\\\": 10,\\n  \\\"per_task\\\": {\\n    \\\"pick up the alphabet soup and place it in the basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"episodes\\\": 1\\n    },\\n    \\\"pick up the cream cheese and place it in the basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"episodes\\\": 1\\n    },\\n    \\\"pick up the salad dressing and place it in the basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 1,\\n      \\\"episodes\\\": 1\\n    },\\n    \\\"pick up the bbq sauce and place it in the basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 1,\\n      \\\"episodes\\\": 1\\n    },\\n    \\\"pick up the ketchup and place it in the basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"episodes\\\": 1\\n    },\\n    \\\"pick up the tomato sauce and place it in the basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"episodes\\\": 1\\n    },\\n    \\\"pick up the butter and place it in the basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"episodes\\\": 1\\n    },\\n    \\\"pick up the milk and place it in the basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"episodes\\\": 1\\n    },\\n    \\\"pick up the chocolate pudding and place it in the basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"episodes\\\": 1\\n    },\\n    \\\"pick up the orange juice and place it in the basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\"
…[truncated 398 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check_openvla_k07_progress_20260518T012051",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-18T01:21:40.934411+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-27271",
  "command": "ps -p 768729 -o pid,stat,etime,cmd",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check_openvla_k07_progress_20260518T012051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-27271",
    "command": "ps -p 768729 -o pid,stat,etime,cmd",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-18T01:21:40.934633+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"   PID STAT     ELAPSED CMD\\n768729 Rl         16:35 python -u /tmp/eval_openvla_libero_gpu1.py --mode random_prune --k_ratio 0.3 --suite libero_object --num_episodes 50 --seed 7\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check_openvla_k07_progress_20260518T012051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-18T01:21:40.934922+00:00_

JSON 文件是之前 quick test（每 task 1 episode）的结果。当前正式 eval（每 task 50 episodes）正在跑。

**OpenVLA k=0.7 eval**: running | Task 3/10 (Ep 40/50) | 已运行 1h16m
- Task 1 (alphabet soup): SR=74% (37/50)
- Task 2 (cream cheese): SR=18% (9/50)
- Task 3 (salad dressing): 进行中, 当前 29/40
- 速度 ~2.0 eps/min，预计还需 ~3h 完成剩余 ~360 episodes

**cuda:1**: busy, PID 768729, 运行 17min, 跑的是 **k=0.3 random prune** eval (libero_object, 50 eps)

**Attention entropy** (`artifacts/openvla_attention_entropy.json`):

```json
{
  "model": "OpenVLA (Llama-2 7B)",
  "n_vision_tokens": 256,
  "max_entropy_bits": 8.0,
  "n_samples": 20,
  "n_layers": 32,
  "n_heads": 32,
  "overall_mean_entropy": 4.939 (ratio: 0.617),
  "overall_vision_attn_fraction": 0.093,
  "smolvla_entropy_ratio": 0.98,
  "min_entropy_layer": { "layer": 28, "entropy": 2.969, "ratio": 0.371 },
  "max_entropy_layer": { "layer": 0, "entropy": 7.889, "ratio": 0.986 },
  "per_layer_entropy_ratio": [
    0.986, 0.963, 0.848, 0.824, 0.829, 0.827, 0.850, 0.827,
    0.801, 0.804, 0.780, 0.756, 0.669, 0.653, 0.648, 0.668,
    0.605, 0.525, 0.496, 0.475, 0.457, 0.447, 0.452, 0.425,
    0.374, 0.389, 0.381, 0.398, 0.371, 0.372, 0.380, 0.477
  ],
  "per_layer_vision_attn_fraction": [
    0.364, 0.277, 0.064, 0.052, 0.053, 0.057, 0.058, 0.059,
    0.070, 0.076, 0.075, 0.099, 0.084, 0.090, 0.152, 0.171,
    0.085, 0.080, 0.082, 0.069, 0.077, 0.085, 0.075, 0.074,
    0.083, 0.070, 0.074, 0.053, 0.052, 0.065, 0.062, 0.102
  ]
}
```

关键发现：
- 整体 entropy ratio 0.617（远低于 SmolVLA 的 0.98），说明 OpenVLA 注意力分布更集中，更适合 token pruning
- 早期层（0-1）entropy 接近最大值（ratio>0.96），注意力几乎均匀分布
- 深层（24-30）entropy ratio 降到 0.37-0.40，注意力高度集中
- Vision attention fraction 整体仅 9.3%，层 14-15 有个 spike（15-17%），层 0 最高（36%）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ops_check_openvla_k07_progress_20260518T012051"
}
```

</details>

---
