# check bjb1 40020 progress

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/chats/worker_check_bjb1_40020_progress_20260520T051545.jsonl`
- **Structured JSON:** [`b37ccffc2c4e995953b0.json`](../../sessions/b3/b37ccffc2c4e995953b0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

21 recorded events

### Tool call

_source line 1 · 2026-05-20T05:16:28.857389+00:00_

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
  "session": "worker_check_bjb1_40020_progress_20260520T051545",
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

_source line 2 · 2026-05-20T05:16:28.857835+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_bjb1_40020_progress_20260520T051545",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T05:16:28.858052+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-40020",
  "command": "ps aux | grep -i dreamer",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_bjb1_40020_progress_20260520T051545",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-40020",
    "command": "ps aux | grep -i dreamer",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T05:16:28.858200+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_bjb1_40020_progress_20260520T051545",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T05:16:28.858329+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-40020",
  "command": "nvidia-smi",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_bjb1_40020_progress_20260520T051545",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-40020",
    "command": "nvidia-smi",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-20T05:16:28.858455+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-40020",
  "command": "find /root/autodl-tmp/event-gated-adaptive-horizon/logdir -name \"metrics.jsonl\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_bjb1_40020_progress_20260520T051545",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-40020",
    "command": "find /root/autodl-tmp/event-gated-adaptive-horizon/logdir -name \"metrics.jsonl\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T05:16:28.858577+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-40020",
  "command": "find /root/runs -name \"metrics.jsonl\" -type f 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_bjb1_40020_progress_20260520T051545",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-40020",
    "command": "find /root/runs -name \"metrics.jsonl\" -type f 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T05:16:28.858730+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Wed May 20 13:16:03 2026       \\n+-----------------------------------------------------------------------------------------+\\n| NVIDIA-SMI 580.105.08             Driver Version: 580.105.08     CUDA Version: 13.0     |\\n+-----------------------------------------+------------------------+----------------------+\\n| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |\\n| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |\\n|                                         |                        |               MIG M. |\\n|=========================================+========================+======================|\\n|   0  NVIDIA GeForce RTX 4090        On  |   00000000:1B:00.0 Off |                  Off |\\n| 30%   35C    P2             84W /  450W |    3564MiB /  24564MiB |     13%      Default |\\n|                                         |                        |                  N/A |\\n+-----------------------------------------+------------------------+----------------------+\\n|   1  NVIDIA GeForce RTX 4090        On  |   00000000:3D:00.0 Off |                  Off |\\n| 30%   34C    P2             68W /  450W |    2535MiB /  24564MiB |      1%      Default |\\n|                                         |                        |                  N/A |\\n+-----------------------------------------+------------------------+----------------------+\\n\\n+-----------------------------------------------------------------------------------------+\\n| Processes:                                                                              |\\n|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |\\n|        ID   ID                                                               Usage      |\\n|=========================================================================================|\\n|    0   N/A  N/A          
…[truncated 453 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_bjb1_40020_progress_20260520T051545",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-20T05:16:28.858920+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_025_obs_sgs_walker_s1/metrics.jsonl\\n/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_025_obs_sgs_walker_s2/metrics.jsonl\\n/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_026_obs_sgs_cheetah_s0/metrics.jsonl\\n/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_026_obs_sgs_cheetah_s1/metrics.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.48}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_bjb1_40020_progress_20260520T051545",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T05:16:28.859051+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_bjb1_40020_progress_20260520T051545",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T05:16:28.859202+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-40020",
  "command": "find /root -maxdepth 4 -type d -name \"exp_027*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_bjb1_40020_progress_20260520T051545",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-40020",
    "command": "find /root -maxdepth 4 -type d -name \"exp_027*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T05:16:28.859329+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0_sigma02\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_bjb1_40020_progress_20260520T051545",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T05:16:28.859450+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-40020",
  "command": "find /root -maxdepth 4 -type d -name \"exp_028*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_bjb1_40020_progress_20260520T051545",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-40020",
    "command": "find /root -maxdepth 4 -type d -name \"exp_028*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T05:16:28.859568+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-40020",
  "command": "ps aux",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_bjb1_40020_progress_20260520T051545",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-40020",
    "command": "ps aux",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-20T05:16:28.859686+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0_ceil15\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_bjb1_40020_progress_20260520T051545",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T05:16:28.859910+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"USER        PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND\\nroot          1  0.0  0.0   4476  3344 ?        Ss   00:23   0:00 bash /init/boot/boot.sh\\nroot       1193  1.7  0.0 724384 22320 ?        Sl   00:23  13:19 /bin/supervisord -c /init/supervisor/supervisor.ini\\nroot       1212  0.1  0.0 4901480 95600 ?       Sl   00:23   1:13 autopanel serve --work-dir=/root/autodl-tmp --cache-dir=/root/autodl-tmp\\nroot       1213  0.0  0.0  15444  9280 ?        S    00:23   0:00 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups\\nroot       1214  0.0  0.0 182308 97772 ?        S    00:23   0:02 /root/miniconda3/bin/python /root/miniconda3/bin/jupyter-lab --allow-root --config=/init/jupyter/jupyter_config.py\\nroot       1215  0.0  0.0 2835808 79188 ?       Sl   00:23   0:26 /root/miniconda3/bin/python /root/miniconda3/bin/tensorboard --host 0.0.0.0 --port 6007 --logdir /root/tf-logs\\nroot       1217  0.0  0.0 3016972 18648 ?       Sl   00:23   0:20 proxy -c /init/proxy/proxy.ini\\nroot       1218  0.0  0.0 3089424 18164 ?       Sl   00:23   0:10 proxy -c /init/proxy/proxy-hot-backup.ini\\nroot       1301  0.0  0.0 17524960 10760 ?      Sl   00:23   0:17 /root/miniconda3/lib/python3.12/site-packages/tensorboard_data_server/bin/server --logdir=/root/tf-logs --reload=5 --samples-per-plugin= --port=0 --port-file=/tmp/tensorboard_data_server_f5j8mxat/port --die-after-stdin --error-file=/tmp/tensorboard_data_server_f5j8mxat/startup_error\\nroot      36514  0.0  0.0  16692 10636 ?        Ss   11:27   0:01 sshd: root@notty\\nroot      37862  0.0  0.0   6112  3744 ?        Ss   11:48   0:00 tmux new-session -d -s exp_027_tcn_walker_s0_sigma02 rm -f /tmp/agent-ml-exit/exp_027_tcn_walker_s0_sigma02.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0_sigma02.log; printf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \\\"$(date -u +%Y-%
…[truncated 6350 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_bjb1_40020_progress_20260520T051545",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T05:16:28.860104+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-40020",
  "command": "tail -20 /root/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0_sigma02.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_bjb1_40020_progress_20260520T051545",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-40020",
    "command": "tail -20 /root/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0_sigma02.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T05:16:28.860267+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[35000] eval_return 278.2 / eval_length 500.0 / eval_episodes 10.0\\nStart training.\\n[35000] civo/ve_ratio 0.2 / civo/delta_ve 0.1 / civo/alert 0.0 / model_loss 4.7 / model_grad_norm 8.2 / height_loss 0.0 / orientations_loss 0.1 / velocity_loss 0.7 / reward_loss 0.6 / cont_loss 0.0 / kl_free 1.0 / dyn_scale 0.5 / rep_scale 0.1 / dyn_loss 5.6 / rep_loss 5.6 / kl 5.5 / prior_ent 38.0 / post_ent 32.4 / normed_target_mean 0.7 / normed_target_std 0.3 / normed_target_min -0.1 / normed_target_max 1.6 / EMA_005 39.4 / EMA_095 58.5 / value_mean 52.2 / value_std 5.5 / value_min 31.3 / value_max 57.0 / target_mean 53.9 / target_std 6.1 / target_min 37.4 / target_max 68.5 / imag_reward_mean 0.5 / imag_reward_std 0.5 / imag_reward_min 0.0 / imag_reward_max 3.3 / imag_action_mean 0.2 / imag_action_std 0.8 / imag_action_min -1.0 / imag_action_max 1.0 / actor_entropy -2.6 / gate_dt_mean 2.0 / gate_dt_std 0.0 / gate_dt_min 2.0 / gate_dt_max 2.0 / gate_dt_1_frac 0.0 / gate_dt_2_frac 1.0 / gate_dt_3_frac 0.0 / gate_dt_4_frac 0.0 / gate_dt_5_frac 0.0 / gate_dt_6_frac 0.0 / gate_dt_7_frac 0.0 / gate_dt_8_frac 0.0 / gate_empirical_entropy 0.0 / gate_entropy_ratio 0.0 / gate_dt_autocorr 0.0 / actor_loss -0.1 / actor_grad_norm 0.1 / value_loss 1.2 / value_grad_norm 0.5 / update_count 7599.0 / fps 7.9\\n[36000] dataset_size 18000.0 / train_return 242.8 / train_length 500.0 / train_episodes 36.0\\n[36000] dataset_size 18000.0 / train_return 273.1 / train_length 500.0 / train_episodes 36.0\\n[36000] dataset_size 18000.0 / train_return 279.9 / train_length 500.0 / train_episodes 36.0\\n[36000] dataset_size 18000.0 / train_return 251.8 / train_length 500.0 / train_episodes 36.0\\n[40000] dataset_size 20000.0 / train_return 317.3 / train_length 500.0 / train_episodes 40.0\\n[40000] dataset_size 20000.0 / train_return 288.2 / train_length 500.0 / train_episodes 40.0\\n[40000] dataset_size 20000.0 / train_return 193.8 / train_length 500.0 /
…[truncated 1939 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_bjb1_40020_progress_20260520T051545",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T05:16:28.860420+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-40020",
  "command": "tail -20 /root/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0_ceil15.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_bjb1_40020_progress_20260520T051545",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-40020",
    "command": "tail -20 /root/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0_ceil15.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T05:16:28.860573+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[35000] eval_return 180.1 / eval_length 500.0 / eval_episodes 10.0\\nStart training.\\n[35000] civo/ve_ratio 0.2 / civo/delta_ve 0.1 / civo/alert 0.0 / model_loss 4.6 / model_grad_norm 8.2 / height_loss 0.0 / orientations_loss 0.1 / velocity_loss 0.6 / reward_loss 0.6 / cont_loss 0.0 / kl_free 1.0 / dyn_scale 0.5 / rep_scale 0.1 / dyn_loss 5.5 / rep_loss 5.5 / kl 5.4 / prior_ent 36.7 / post_ent 31.5 / normed_target_mean 0.8 / normed_target_std 0.3 / normed_target_min -0.5 / normed_target_max 1.7 / EMA_005 40.2 / EMA_095 47.6 / value_mean 44.4 / value_std 2.5 / value_min 16.3 / value_max 46.7 / target_mean 45.8 / target_std 2.5 / target_min 37.1 / target_max 52.9 / imag_reward_mean 0.4 / imag_reward_std 0.4 / imag_reward_min 0.0 / imag_reward_max 2.3 / imag_action_mean 0.3 / imag_action_std 0.8 / imag_action_min -1.0 / imag_action_max 1.0 / actor_entropy -3.2 / gate_dt_mean 2.0 / gate_dt_std 0.0 / gate_dt_min 2.0 / gate_dt_max 2.0 / gate_dt_1_frac 0.0 / gate_dt_2_frac 1.0 / gate_dt_3_frac 0.0 / gate_dt_4_frac 0.0 / gate_dt_5_frac 0.0 / gate_dt_6_frac 0.0 / gate_dt_7_frac 0.0 / gate_dt_8_frac 0.0 / gate_empirical_entropy 0.0 / gate_entropy_ratio 0.0 / gate_dt_autocorr 0.0 / actor_loss -0.2 / actor_grad_norm 0.2 / value_loss 1.1 / value_grad_norm 0.3 / update_count 7599.0 / fps 7.8\\n[36000] dataset_size 18000.0 / train_return 178.3 / train_length 500.0 / train_episodes 36.0\\n[36000] dataset_size 18000.0 / train_return 174.6 / train_length 500.0 / train_episodes 36.0\\n[36000] dataset_size 18000.0 / train_return 176.3 / train_length 500.0 / train_episodes 36.0\\n[36000] dataset_size 18000.0 / train_return 139.5 / train_length 500.0 / train_episodes 36.0\\n[40000] dataset_size 20000.0 / train_return 77.8 / train_length 500.0 / train_episodes 40.0\\n[40000] dataset_size 20000.0 / train_return 96.1 / train_length 500.0 / train_episodes 40.0\\n[40000] dataset_size 20000.0 / train_return 163.8 / train_length 500.0 / t
…[truncated 1933 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_bjb1_40020_progress_20260520T051545",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-20T05:16:28.860757+00:00_

两个实验都正常推进，已脱离 8K 区间。

| 实验 | 当前 step | eval_return | GPU | GPU Util | FPS | 状态 |
|------|-----------|-------------|-----|----------|-----|------|
| **exp_027** (TCN, σ=0.2) | **45000** / 210K | 315.6 | GPU 0 (4090) | 13% | 7.7 | 正常 |
| **exp_028** (RAVE, ceil=1.5) | **45000** / 210K | 166.9 | GPU 1 (4090) | 1% | 7.8 | 正常 |

两个实验约 1.5 小时前启动（11:48/11:49），已完成约 21% 进度。exp_027 的 return 明显高于 exp_028（315 vs 167）。GPU util 偏低是正常的（dreamer 有大量 CPU 端 env step）。无报错。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_check_bjb1_40020_progress_20260520T051545"
}
```

</details>

---
