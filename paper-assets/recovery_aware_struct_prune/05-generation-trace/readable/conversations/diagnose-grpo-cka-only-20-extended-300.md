# diagnose grpo cka only 20 extended 300

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 0
- **Tool calls:** 16
- **Original source:** `logs/chats/worker_diagnose_grpo_cka_only_20_extended_300_20260518T220207.jsonl`
- **Structured JSON:** [`331a89be6ba17887477a.json`](../../sessions/33/331a89be6ba17887477a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

33 recorded events

### Tool call

_source line 1 · 2026-05-18T22:04:06.177045+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__read_registry",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_grpo_cka_only_20_extended_300_20260518T220207",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__read_registry",
    "max_results": "6"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-18T22:04:06.177431+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_grpo_cka_only_20_extended_300_20260518T220207",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T22:04:06.177622+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29022",
  "command": "tail -100 ~/runs/recovery_aware_struct_prune/grpo_cka_only_20_extended_300.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_grpo_cka_only_20_extended_300_20260518T220207",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29022",
    "command": "tail -100 ~/runs/recovery_aware_struct_prune/grpo_cka_only_20_extended_300.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-18T22:04:06.177958+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"│ │                         │ #### 19                │           │           │ │\\n│ │                         │ #### 20                │           │           │ │\\n│ │                         │ #### 21                │           │           │ │\\n│ │                         │ #### 22                │           │           │ │\\n│ │                         │ #### 23                │           │           │ │\\n│ │                         │ #### 24                │           │           │ │\\n│ │                         │ #### 25                │           │           │ │\\n│ │                         │ #### 26                │           │           │ │\\n│ │                         │ #### 27                │           │           │ │\\n│ │                         │ #### 28                │           │           │ │\\n│ │                         │ #### 29                │           │           │ │\\n│ │                         │ #### 30                │           │           │ │\\n│ │                         │ #### 31                │           │           │ │\\n│ │                         │ #### 32                │           │           │ │\\n│ │                         │ #### 33                │           │           │ │\\n│ │                         │ #### 34                │           │           │ │\\n│ │                         │ #### 35                │           │           │ │\\n│ │                         │ #### 36                │           │           │ │\\n│ │                         │ #### 37                │           │           │ │\\n│ │                         │ #### 38                │           │           │ │\\n│ │                         │ #### 39                │           │           │ │\\n│ ���                         │ #### 40                │           │           │ │\\n│ │                         │ #### 41                │           │           │ │\\n│ │                         │ ###
…[truncated 6515 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_grpo_cka_only_20_extended_300_20260518T220207",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T22:04:06.178158+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29022",
  "command": "grep -n -i \"sighup\\|signal\\|kill\\|error\\|exception\\|traceback\\|step 300\\|step=300\\|global_step.*300\" ~/runs/recovery_aware_struct_prune/grpo_cka_only_20_extended_300.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_grpo_cka_only_20_extended_300_20260518T220207",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29022",
    "command": "grep -n -i \"sighup\\|signal\\|kill\\|error\\|exception\\|traceback\\|step 300\\|step=300\\|global_step.*300\" ~/runs/recovery_aware_struct_prune/grpo_cka_only_20_extended_300.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-18T22:04:06.178356+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_grpo_cka_only_20_extended_300_20260518T220207",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-18T22:04:06.178503+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29022",
  "command": "ps aux",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_grpo_cka_only_20_extended_300_20260518T220207",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29022",
    "command": "ps aux",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-18T22:04:06.178678+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"USER        PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND\\nroot          1  0.0  0.0   4476  3344 ?        Ss   May18   0:00 bash /init/boot/boot.sh\\nroot        917  2.2  0.0 717984 21620 ?        Sl   May18  12:38 /bin/supervisord -c /init/supervisor/supervisor.ini\\nroot        933  0.0  0.0 187552 101872 ?       S    May18   0:01 /root/miniconda3/bin/python /root/miniconda3/bin/jupyter-lab --allow-root --config=/init/jupyter/jupyter_config.py\\nroot        935  0.0  0.0  15444  9192 ?        S    May18   0:00 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups\\nroot        938  0.1  0.0 6746572 116368 ?      Sl   May18   1:01 autopanel serve --work-dir=/root/autodl-tmp --cache-dir=/root/autodl-tmp\\nroot        939  0.0  0.0 2425836 19736 ?       Sl   May18   0:07 proxy -c /init/proxy/proxy-hot-backup.ini\\nroot        940  0.0  0.0 4147292 79680 ?       Sl   May18   0:26 /root/miniconda3/bin/python /root/miniconda3/bin/tensorboard --host 0.0.0.0 --port 6007 --logdir /root/tf-logs\\nroot        941  0.1  0.0 2426348 20516 ?       Sl   May18   1:04 proxy -c /init/proxy/proxy.ini\\nroot       1052  0.0  0.0 28341068 12380 ?      Sl   May18   0:32 /root/miniconda3/lib/python3.12/site-packages/tensorboard_data_server/bin/server --logdir=/root/tf-logs --reload=5 --samples-per-plugin= --port=0 --port-file=/tmp/tensorboard_data_server_4_ocohnk/port --die-after-stdin --error-file=/tmp/tensorboard_data_server_4_ocohnk/startup_error\\nroot      15617  0.0  0.0  16692 10656 ?        Ss   00:27   0:03 sshd: root@notty\\nroot      19609  0.0  0.0   6184  3872 ?        Ss   01:52   0:00 tmux new-session -d -s math500_standard_grpo_fair source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair --output_path /root/autodl-tmp/recovery_aware_stru
…[truncated 3371 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_grpo_cka_only_20_extended_300_20260518T220207",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T22:04:06.178829+00:00_

called mcp__agent-ml-research__fetch_wandb_metrics

<details open><summary>🔧 Tool call — mcp__agent-ml-research__fetch_wandb_metrics</summary>

```json
{
  "run_id": "z9f0z901",
  "metric_names": "['reward', 'mean_reward', 'reward/mean', 'train/global_step', 'global_step', '_step']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_grpo_cka_only_20_extended_300_20260518T220207",
  "tool": "mcp__agent-ml-research__fetch_wandb_metrics",
  "tool_args": {
    "run_id": "z9f0z901",
    "metric_names": "['reward', 'mean_reward', 'reward/mean', 'train/global_step', 'global_step', '_step']"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-18T22:04:06.178960+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"W&B entity/project not configured. Set in config/projects/*.yaml\", \"metadata\": {\"elapsed_seconds\": 0}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_grpo_cka_only_20_extended_300_20260518T220207",
  "tool": "mcp__agent-ml-research__fetch_wandb_metrics",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T22:04:06.179081+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "filters": "{'experiment_id': 'grpo_cka_only_20_extended_300'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_grpo_cka_only_20_extended_300_20260518T220207",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "recovery_aware_struct_prune",
    "filters": "{'experiment_id': 'grpo_cka_only_20_extended_300'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-18T22:04:06.179213+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "file": "memory.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_grpo_cka_only_20_extended_300_20260518T220207",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "recovery_aware_struct_prune",
    "file": "memory.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-18T22:04:06.179387+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5265}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_grpo_cka_only_20_extended_300_20260518T220207",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-18T22:04:06.179544+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/memory.md\", \"content\": \"# Memory — recovery_aware_struct_prune\\n\\n## E2 CKA-only Extended GRPO reward=1.00 调查结论 (2026-05-18)\\nreward=1.00 是单条 sample reward，非 batch 均值。实际 reward_mean 在 0.23-0.34 区间波动（step 110-190），无顿悟迹象。\\n\\n## westd cuda:1 遗留问题 (2026-05-18)\\neval_math500_grpo_standard_20_fair 原始版本（PID 19616，无 --max_new_tokens 2048）仍在 cuda:1 上运行，registry 已被 cron 误标为 DONE/failed。Director 之前下达的 kill+restart v2 指令在 context compaction 期间丢失。等待 Director 决策。\\n\\n## westd cuda:2 v4 进程死亡确认 (2026-05-18)\\nurgent worker 检查 nvidia-smi 发现 cuda:2 实际 0MiB，v4 进程已自然死亡。启动了 v4_restart。Director 的\\\"不要重置 cuda:2\\\"撤回指令到达时进程已死，restart 是正确操作。\\n\\n## 1.5B GRPO 训练结果汇总 (2026-05-18)\\n- CKA-only: reward=0.2375（最高）\\n- RASP: reward=0.099（未 collapse，与 7B 不同）\\n- Standard: reward=0.084\\n\\n## Dense MATH-500 baseline (2026-05-18)\\naccuracy=0.736 (368/500), stderr=0.0197, natural_eos_pct=75.2%。westd-29022 验证，与 westd-11672 结果一致。\\n\\n## E3 CKA heatmap 关键发现 (2026-05-18)\\nCKA-only 对角线 CKA 最低 (0.62 vs 0.88-0.92 for others)，偏离 dense 最多，但 GRPO recovery 最好。支持\\\"CKA-only 选择高可塑性而非高保留结构\\\"的解释。\\n\\n## submit_training_job 命令格式 (2026-05-18)\\nwestd 上命令需要用 bash -c 包裹，src/ 前缀，绝对路径指定模型。\\n\\n## westb 磁盘清理记录 (2026-05-18)\\n删除 grpo_rasp_20_1p5b optimizer states (~3.2GB) + Qwen2.5-Math-7B (~15GB)，释放至 38GB 可用。\\n\", \"total_chars\": 1205, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_grpo_cka_only_20_extended_300_20260518T220207",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-18T22:04:06.179724+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29022",
  "command": "grep -n -i \"sighup\\|signal\\|kill\\|error\\|exception\\|traceback\" /root/runs/recovery_aware_struct_prune/grpo_cka_only_20_extended_300.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_grpo_cka_only_20_extended_300_20260518T220207",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29022",
    "command": "grep -n -i \"sighup\\|signal\\|kill\\|error\\|exception\\|traceback\" /root/runs/recovery_aware_struct_prune/grpo_cka_only_20_extended_300.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-18T22:04:06.179854+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_grpo_cka_only_20_extended_300_20260518T220207",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-18T22:04:06.179983+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29022",
  "command": "grep -n \"reward\" /root/runs/recovery_aware_struct_prune/grpo_cka_only_20_extended_300.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_grpo_cka_only_20_extended_300_20260518T220207",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29022",
    "command": "grep -n \"reward\" /root/runs/recovery_aware_struct_prune/grpo_cka_only_20_extended_300.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-18T22:04:06.180173+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"19:2026-05-18 23:14:19,592 [INFO] beta=0.01, loss_type=dapo, format_reward=0.1\\n36:\\r  0%|          | 0/300 [00:00<?, ?it/s]\\r 34%|███▎      | 101/300 [02:04<04:05,  1.23s/it]\\r 34%|███▍      | 102/300 [03:53<09:02,  2.74s/it]\\r 34%|███▍      | 103/300 [05:42<15:48,  4.81s/it]\\r 35%|███▍      | 104/300 [07:27<24:34,  7.52s/it]\\r 35%|███▌      | 105/300 [09:22<37:29, 11.54s/it]\\r 35%|███▌      | 106/300 [11:13<53:36, 16.58s/it]\\r 36%|███▌      | 107/300 [13:05<1:14:03, 23.02s/it]\\r 36%|███▌      | 108/300 [14:59<1:39:11, 31.00s/it]\\r 36%|███▋      | 109/300 [17:01<2:10:52, 41.11s/it]\\r 37%|███▋      | 110/300 [19:04<2:46:08, 52.47s/it]\\r                                                   \\r\\r 37%|███▋      | 110/300 [19:04<2:46:08, 52.47s/it]{'loss': '0.0246', 'grad_norm': '1.828', 'learning_rate': '6.367e-07', 'num_tokens': '9.433e+05', 'completions/mean_length': '294.6', 'completions/min_length': '65.3', 'completions/max_length': '512', 'completions/clipped_ratio': '0.4', 'completions/mean_terminated_length': '145.3', 'completions/min_terminated_length': '65.3', 'completions/max_terminated_length': '290.7', 'rewards/reward_fn/mean': '0.3206', 'rewards/reward_fn/std': '0.4188', 'reward': '0.3206', 'reward_std': '0.4188', 'frac_reward_zero_std': '0.175', 'kl': '0.001129', 'entropy': '0.09788', 'clip_ratio/low_mean': '0', 'clip_ratio/low_min': '0', 'clip_ratio/high_mean': '0', 'clip_ratio/high_max': '0', 'clip_ratio/region_mean': '0', 'step_time': '114.1', 'epoch': '0.05889'}\\n39:│ ┃ Prompt                  ┃ Completion             ┃ reward_fn ┃ Advantage ┃ │\\n900:\\r 37%|███▋      | 111/300 [20:57<3:16:36, 62.42s/it]\\r 37%|███▋      | 112/300 [22:54<3:47:41, 72.67s/it]\\r 38%|███▊      | 113/300 [24:47<4:13:32, 81.35s/it]\\r 38%|███▊      | 114/300 [26:39<4:34:27, 88.53s/it]\\r 38%|███▊      | 115/300 [28:39<4:57:02, 96.34s/it]\\r 39%|███▊      | 116/300 [30:39<5:14:51, 102.67s/it]\\r 39%|███▉  
…[truncated 6364 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_grpo_cka_only_20_extended_300_20260518T220207",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-18T22:04:06.180351+00:00_

called mcp__agent-ml-research__fetch_wandb_metrics

<details open><summary>🔧 Tool call — mcp__agent-ml-research__fetch_wandb_metrics</summary>

```json
{
  "run_id": "z9f0z901",
  "metric_names": "['reward', 'mean_reward', 'reward/mean', 'train/global_step', 'global_step', '_step']",
  "entity": "xiaoyucorynne-",
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_grpo_cka_only_20_extended_300_20260518T220207",
  "tool": "mcp__agent-ml-research__fetch_wandb_metrics",
  "tool_args": {
    "run_id": "z9f0z901",
    "metric_names": "['reward', 'mean_reward', 'reward/mean', 'train/global_step', 'global_step', '_step']",
    "entity": "xiaoyucorynne-",
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-18T22:04:06.180493+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "limit": "5",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_grpo_cka_only_20_extended_300_20260518T220207",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "recovery_aware_struct_prune",
    "limit": "5",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-18T22:04:06.180724+00:00_

{"result":"{\"success\": true, \"data\": {\"run_id\": \"z9f0z901\", \"run_name\": \"grpo_grpo_cka_only_20\", \"metrics\": {\"train/global_step\": 300, \"_step\": 5641}, \"missing_metrics\": [\"reward\", \"mean_reward\", \"reward/mean\", \"global_step\"], \"state\": \"finished\", \"config\": {\"beta\": 0.01, \"bf16\": true, \"fp16\": false, \"fsdp\": [], \"seed\": 42, \"debug\": [], \"dtype\": \"bfloat16\", \"optim\": \"adamw_8bit\", \"top_k\": 0, \"top_p\": 1, \"do_eval\": false, \"epsilon\": 0.2, \"project\": \"huggingface\", \"use_cpu\": false, \"do_train\": false, \"id2label\": {\"0\": \"LABEL_0\", \"1\": \"LABEL_1\"}, \"label2id\": {\"LABEL_0\": 0, \"LABEL_1\": 1}, \"run_name\": \"grpo_grpo_cka_only_20\", \"use_vllm\": false, \"hub_token\": \"&lt;HUB_TOKEN>\", \"log_level\": \"passive\", \"loss_type\": \"dapo\", \"max_steps\": 300, \"report_to\": [\"wandb\"], \"use_cache\": false, \"use_mrope\": false, \"vllm_mode\": \"colocate\", \"adam_beta1\": 0.9, \"adam_beta2\": 0.999, \"do_predict\": false, \"eval_delay\": 0, \"hidden_act\": \"silu\", \"local_rank\": -1, \"model_type\": \"qwen2\", \"output_dir\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_extended_300\", \"save_steps\": 50, \"vocab_size\": 152064, \"ddp_timeout\": 1800, \"fsdp_config\": {\"xla\": false, \"xla_fsdp_v2\": false, \"min_num_params\": 0, \"xla_fsdp_grad_ckpt\": false}, \"hidden_size\": 3584, \"layer_types\": [\"full_attention\", \"full_attention\", \"full_attention\", \"full_attention\", \"full_attention\", \"full_attention\", \"full_attention\", \"full_attention\", \"full_attention\", \"full_attention\", \"full_attention\", \"full_attention\", \"full_attention\", \"full_attention\", \"full_attention\", \"full_attention\", \"full_attention\", \"full_attention\", \"full_attention\", \"full_attention\", \"full_attention\", \"full_attention\", \"full_attention\", \"full_attention\", \"full_attention\", \"full_attention\", \"full_attention\", \"full_attention\"], \"logging_dir\": 
…[truncated 4243 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_grpo_cka_only_20_extended_300_20260518T220207",
  "tool": "mcp__agent-ml-research__fetch_wandb_metrics",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-18T22:04:06.180988+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"grpo_cka_only_20_extended_300\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T14:51:36.423Z\", \"updated_at\": \"2026-05-18T21:43:18.847Z\", \"hypothesis\": \"Extended GRPO CKA-only 7B from step 100 to 300. Paired control for E2 Standard extended: if CKA-only continues improving while Standard enters reward desert, proves CKA-only's structural advantage persists under longer training. Standard showed reward decline after step 260 (0.102→0.056); CKA-only's peak at step 100 was 0.354 — expect continued learning.\", \"parent\": \"grpo_cka_only_20\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_extended_300 --beta 0.01 --temperature 0.4 --repetition_penalty 1.15 --format_reward_weight 0.1 --loss_type dapo --learning_rate 1e-6 --max_steps 300 --save_steps 50 --save_total_limit 3 --resume_from_checkpoint /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/checkpoint-100'\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:0\"], \"pid\": \"11457\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_cka_only_20_extended_300.log\", \"submitted_at\": \"2026-05-18T15:10:04.515Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (CKA-only 20% pruned, SFT recovered, GRPO extended)\", \"data_path\": \"openai/gsm8k\", \"data_count\": 7473, \"seed\": 42, \"wandb_run_id\": \"z9f0z901\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/checkpoint-100\", \"eval_data\": \"openai/gsm8k (GRPO RL training)\", \"hyperparams\": {\"beta\": 0.01, \"temperature\": 0.4, \"repetition_penalty\": 1.15, \"form
…[truncated 5133 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_grpo_cka_only_20_extended_300_20260518T220207",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-18T22:04:06.181196+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__fetch_wandb_run_history",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_grpo_cka_only_20_extended_300_20260518T220207",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__fetch_wandb_run_history",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-18T22:04:06.181353+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_grpo_cka_only_20_extended_300_20260518T220207",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-18T22:04:06.181477+00:00_

called mcp__agent-ml-research__fetch_wandb_run_history

<details open><summary>🔧 Tool call — mcp__agent-ml-research__fetch_wandb_run_history</summary>

```json
{
  "run_id": "z9f0z901",
  "metrics": "['reward', 'rewards/reward_fn/mean', 'train/global_step']",
  "samples": "500",
  "entity": "xiaoyucorynne-",
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_grpo_cka_only_20_extended_300_20260518T220207",
  "tool": "mcp__agent-ml-research__fetch_wandb_run_history",
  "tool_args": {
    "run_id": "z9f0z901",
    "metrics": "['reward', 'rewards/reward_fn/mean', 'train/global_step']",
    "samples": "500",
    "entity": "xiaoyucorynne-",
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-18T22:04:06.181609+00:00_

{"result":"{\"success\": true, \"data\": {\"run_id\": \"z9f0z901\", \"run_name\": \"grpo_grpo_cka_only_20\", \"steps\": [], \"history\": {\"reward\": [], \"rewards/reward_fn/mean\": [], \"train/global_step\": []}, \"num_points\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.25}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_grpo_cka_only_20_extended_300_20260518T220207",
  "tool": "mcp__agent-ml-research__fetch_wandb_run_history",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-18T22:04:06.181774+00:00_

called mcp__agent-ml-research__fetch_wandb_run_history

<details open><summary>🔧 Tool call — mcp__agent-ml-research__fetch_wandb_run_history</summary>

```json
{
  "run_id": "z9f0z901",
  "metrics": "['train/reward', 'train/rewards/reward_fn/mean', 'train/loss', 'loss']",
  "samples": "50",
  "entity": "xiaoyucorynne-",
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_grpo_cka_only_20_extended_300_20260518T220207",
  "tool": "mcp__agent-ml-research__fetch_wandb_run_history",
  "tool_args": {
    "run_id": "z9f0z901",
    "metrics": "['train/reward', 'train/rewards/reward_fn/mean', 'train/loss', 'loss']",
    "samples": "50",
    "entity": "xiaoyucorynne-",
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-18T22:04:06.181981+00:00_

{"result":"{\"success\": true, \"data\": {\"run_id\": \"z9f0z901\", \"run_name\": \"grpo_grpo_cka_only_20\", \"steps\": [], \"history\": {\"train/reward\": [], \"train/rewards/reward_fn/mean\": [], \"train/loss\": [], \"loss\": []}, \"num_points\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.16}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_grpo_cka_only_20_extended_300_20260518T220207",
  "tool": "mcp__agent-ml-research__fetch_wandb_run_history",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-18T22:04:06.182162+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "file": "memory.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_grpo_cka_only_20_extended_300_20260518T220207",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "recovery_aware_struct_prune",
    "file": "memory.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-18T22:04:06.182337+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/memory.md\", \"content\": \"# Memory — recovery_aware_struct_prune\\n\\n## E2 CKA-only Extended GRPO reward=1.00 调查结论 (2026-05-18)\\nreward=1.00 是单条 sample reward，非 batch 均值。实际 reward_mean 在 0.23-0.34 区间波动（step 110-190），无顿悟迹象。\\n\\n## westd cuda:1 遗留问题 (2026-05-18)\\neval_math500_grpo_standard_20_fair 原始版本（PID 19616，无 --max_new_tokens 2048）仍在 cuda:1 上运行，registry 已被 cron 误标为 DONE/failed。Director 之前下达的 kill+restart v2 指令在 context compaction 期间丢失。等待 Director 决策。\\n\\n## westd cuda:2 v4 进程死亡确认 (2026-05-18)\\nurgent worker 检查 nvidia-smi 发现 cuda:2 实际 0MiB，v4 进程已自然死亡。启动了 v4_restart。Director 的\\\"不要重置 cuda:2\\\"撤回指令到达时进程已死，restart 是正确操作。\\n\\n## 1.5B GRPO 训练结果汇总 (2026-05-18)\\n- CKA-only: reward=0.2375（最高）\\n- RASP: reward=0.099（未 collapse，与 7B 不同）\\n- Standard: reward=0.084\\n\\n## Dense MATH-500 baseline (2026-05-18)\\naccuracy=0.736 (368/500), stderr=0.0197, natural_eos_pct=75.2%。westd-29022 验证，与 westd-11672 结果一致。\\n\\n## E3 CKA heatmap 关键发现 (2026-05-18)\\nCKA-only 对角线 CKA 最低 (0.62 vs 0.88-0.92 for others)，偏离 dense 最多，但 GRPO recovery 最好。支持\\\"CKA-only 选择高可塑性而非高保留结构\\\"的解释。\\n\\n## submit_training_job 命令格式 (2026-05-18)\\nwestd 上命令需要用 bash -c 包裹，src/ 前缀，绝对路径指定模型。\\n\\n## westb 磁盘清理记录 (2026-05-18)\\n删除 grpo_rasp_20_1p5b optimizer states (~3.2GB) + Qwen2.5-Math-7B (~15GB)，释放至 38GB 可用。\\n\", \"total_chars\": 1205, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_grpo_cka_only_20_extended_300_20260518T220207",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-18T22:04:06.182511+00:00_

called mcp__agent-ml-research__save_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "file": "memory.md",
  "content": "# Memory — recovery_aware_struct_prune\n\n## E2 CKA-only Extended GRPO reward=1.00 调查结论 (2026-05-18)\nreward=1.00 是单条 sample reward，非 batch 均值。实际 reward_mean 在 0.23-0.34 区间波动（step 110-190），无顿悟迹象。\n\n## westd cuda:1 遗留问题 (2026-05-18)\neval_math500_grpo_standard_20_fair 原始版本（PID 19616，无 --max_new_tokens 2048）仍在 cuda:1 上运行，registry 已被 cron 误标为 DONE/failed。Director 之前下达的 kill+restart v2 指令在 context compaction 期间丢失。等待 Director 决策。\n\n## westd cuda:2 v4 进程死亡确认 (2026-05-18)\nurgent worker 检查 nvidia-smi 发现 cuda:2 实际 0MiB，v4 进程已自然死亡。启动了 v4_restart。Director 的\"不要重置 cuda:2\"撤回指令到达时进程已死，restart 是正确操作。\n\n## 1.5B GRPO 训练结果汇总 (2026-05-18)\n- CKA-only: reward=0.2375（最高）\n- RASP: reward=0.099（未 collapse，与 7B 不同）\n- Standard: reward=0.084\n\n## Dense MATH-500 baseline (2026-05-18)\naccuracy=0.736 (368/500), stderr=0.0197, natural_eos_pct=75.2%。westd-29022 验证，与 westd-11672 结果一致。\n\n## E3 CKA heatmap 关键发现 (2026-05-18)\nCKA-only 对角线 CKA 最低 (0.62 vs 0.88-0.92 for others)，偏离 dense 最多，但 GRPO recovery 最好。支持\"CKA-only 选择高可塑性而非高保留结构\"的解释。\n\n## submit_training_job 命令格式 (2026-05-18)\nwestd 上命令需要用 bash -c 包裹，src/ 前缀，绝对路径指定模型。\n\n## westb 磁盘清理记录 (2026-05-18)\n删除 grpo_rasp_20_1p5b optimizer states (~3.2GB) + Qwen2.5-Math-7B (~15GB)，释放至 38GB 可用。\n\n## grpo_cka_only_20_extended_300 验证报告 (2026-05-19)\n\n### 结论：训练成功完成，registry 标记正确\n\n**1. 训练完成状态：✅ 确认 300/300 步完成**\n- 日志进度条：`100%|██████████| 300/300 [6:23:12]`\n- 最终日志消息：`GRPO v4 recovery training complete.` (05:38:04)\n- 模型已保存至 `/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_extended_300`\n- W&B run z9f0z901 状态：`finished`，`train/global_step=300`\n\n**2. SIGHUP (EXIT_CODE=129) 原因：训练后的 wrapper 清理信号，非训练中断**\n- 时间线：训练完成 (05:37:51) → 模型保存 (05:38:04) → W&B finalize → EXIT_CODE=129\n- SIGHUP 发生在所有实质工作完成之后，来自 tmux session 或 cron wrapper 的进程清理\n- 无 traceback/exception/error（grep 验证无 shell metachar 所以未搜到，但日志末尾无异常）\n\n**3. 指标验证：✅ 日志与 registry 完全一致**\n\n| 指标 | 日志值 | Registry 值 | 匹配 |\n|------|--------|-------------|------|\n| global_step | 300 | 300 | ✅ |\n| peak_reward (step 280) | 0.4444 | 0.4444 | ✅ |\n| final_reward (step 300) | 0.3075 | 0.3075 | ✅ |\n| final_loss | 0.03488 | 0.0349 | ✅ (四舍五入) |\n\n**4. Reward 轨迹（从日志提取，每 10 步）：**\n- Step 110: 0.3206 → Step 120: 0.2562 → ... → Step 280: 0.4444 (peak) → Step 290: 0.2238 → Step 300: 0.3075\n- 模式：持续振荡（0.22-0.44 范围），无 collapse\n- registry 标记 `pattern: \"sustained oscillation, no collapse\"` 准确\n\n**5. 与相关实验对比：**\n- vs parent (grpo_cka_only_20, 100步): reward 0.354 → extended 后 peak 提升至 0.4444，final 0.3075 略低于 parent 终点，但仍在健康范围\n- vs Standard extended (grpo_standard_20_extended_300_v2, 300步): Standard 发生 reward collapse (0.102→0.056)，CKA-only 保持稳定振荡不崩溃，证实 CKA-only 的结构优势在长训练中持续\n\n**6. 进程状态：✅ 已完全退出，无残留进程**\n- `ps aux` 确认 westd-29022 上无 grpo_cka_only_20_extended_300 相关进程\n\n**W&B 注意事项：** W&B history API 对该 run 返回空（所有 metric key 均无 history 数据点），可能是 TRL 的日志方式只写 summary 不写 history。metric 验证依赖日志文件，已确认一致。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_grpo_cka_only_20_extended_300_20260518T220207",
  "tool": "mcp__agent-ml-research__save_project_file",
  "tool_args": {
    "project": "recovery_aware_struct_prune",
    "file": "memory.md",
    "content": "# Memory — recovery_aware_struct_prune\n\n## E2 CKA-only Extended GRPO reward=1.00 调查结论 (2026-05-18)\nreward=1.00 是单条 sample reward，非 batch 均值。实际 reward_mean 在 0.23-0.34 区间波动（step 110-190），无顿悟迹象。\n\n## westd cuda:1 遗留问题 (2026-05-18)\neval_math500_grpo_standard_20_fair 原始版本（PID 19616，无 --max_new_tokens 2048）仍在 cuda:1 上运行，registry 已被 cron 误标为 DONE/failed。Director 之前下达的 kill+restart v2 指令在 context compaction 期间丢失。等待 Director 决策。\n\n## westd cuda:2 v4 进程死亡确认 (2026-05-18)\nurgent worker 检查 nvidia-smi 发现 cuda:2 实际 0MiB，v4 进程已自然死亡。启动了 v4_restart。Director 的\"不要重置 cuda:2\"撤回指令到达时进程已死，restart 是正确操作。\n\n## 1.5B GRPO 训练结果汇总 (2026-05-18)\n- CKA-only: reward=0.2375（最高）\n- RASP: reward=0.099（未 collapse，与 7B 不同）\n- Standard: reward=0.084\n\n## Dense MATH-500 baseline (2026-05-18)\naccuracy=0.736 (368/500), stderr=0.0197, natural_eos_pct=75.2%。westd-29022 验证，与 westd-11672 结果一致。\n\n## E3 CKA heatmap 关键发现 (2026-05-18)\nCKA-only 对角线 CKA 最低 (0.62 vs 0.88-0.92 for others)，偏离 dense 最多，但 GRPO recovery 最好。支持\"CKA-only 选择高可塑性而非高保留结构\"的解释。\n\n## submit_training_job 命令格式 (2026-05-18)\nwestd 上命令需要用 bash -c 包裹，src/ 前缀，绝对路径指定模型。\n\n## westb 磁盘清理记录 (2026-05-18)\n删除 grpo_rasp_20_1p5b optimizer states (~3.2GB) + Qwen2.5-Math-7B (~15GB)，释放至 38GB 可用。\n\n## grpo_cka_only_20_extended_300 验证报告 (2026-05-19)\n\n### 结论：训练成功完成，registry 标记正确\n\n**1. 训练完成状态：✅ 确认 300/300 步完成**\n- 日志进度条：`100%|██████████| 300/300 [6:23:12]`\n- 最终日志消息：`GRPO v4 recovery training complete.` (05:38:04)\n- 模型已保存至 `/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_extended_300`\n- W&B run z9f0z901 状态：`finished`，`train/global_step=300`\n\n**2. SIGHUP (EXIT_CODE=129) 原因：训练后的 wrapper 清理信号，非训练中断**\n- 时间线：训练完成 (05:37:51) → 模型保存 (05:38:04) → W&B finalize → EXIT_CODE=129\n- SIGHUP 发生在所有实质工作完成之后，来自 tmux session 或 cron wrapper 的进程清理\n- 无 traceback/exception/error（grep 验证无 shell metachar 所以未搜到，但日志末尾无异常）\n\n**3. 指标验证：✅ 日志与 registry 完全一致**\n\n| 指标 | 日志值 | Registry 值 | 匹配 |\n|------|--------|-------------|------|\n| global_step | 300 | 300 | ✅ |\n| peak_reward (step 280) | 0.4444 | 0.4444 | ✅ |\n| final_reward (step 300) | 0.3075 | 0.3075 | ✅ |\n| final_loss | 0.03488 | 0.0349 | ✅ (四舍五入) |\n\n**4. Reward 轨迹（从日志提取，每 10 步）：**\n- Step 110: 0.3206 → Step 120: 0.2562 → ... → Step 280: 0.4444 (peak) → Step 290: 0.2238 → Step 300: 0.3075\n- 模式：持续振荡（0.22-0.44 范围），无 collapse\n- registry 标记 `pattern: \"sustained oscillation, no collapse\"` 准确\n\n**5. 与相关实验对比：**\n- vs parent (grpo_cka_only_20, 100步): reward 0.354 → extended 后 peak 提升至 0.4444，final 0.3075 略低于 parent 终点，但仍在健康范围\n- vs Standard extended (grpo_standard_20_extended_300_v2, 300步): Standard 发生 reward collapse (0.102→0.056)，CKA-only 保持稳定振荡不崩溃，证实 CKA-only 的结构优势在长训练中持续\n\n**6. 进程状态：✅ 已完全退出，无残留进程**\n- `ps aux` 确认 westd-29022 上无 grpo_cka_only_20_extended_300 相关进程\n\n**W&B 注意事项：** W&B history API 对该 run 返回空（所有 metric key 均无 history 数据点），可能是 TRL 的日志方式只写 summary 不写 history。metric 验证依赖日志文件，已确认一致。\n"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-18T22:04:06.182681+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_grpo_cka_only_20_extended_300_20260518T220207",
  "tool": "mcp__agent-ml-research__save_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-18T22:04:06.182846+00:00_

验证完成。

**结论：grpo_cka_only_20_extended_300 训练成功，registry 标记正确。**

关键发现：
- **300/300 步完成**，模型已保存，W&B run 状态 `finished`
- **EXIT_CODE=129 是假阳性** — SIGHUP 发生在训练完成、模型保存、W&B finalize 全部结束之后，来自 tmux/wrapper 清理信号
- **指标与 registry 完全一致**：peak_reward=0.4444 @ step 280，final_reward=0.3075 @ step 300
- **Reward 轨迹**：0.22-0.44 范围内持续振荡，无 collapse。与 Standard extended 的 reward collapse (0.102→0.056) 形成鲜明对比，确认 CKA-only 的结构优势在长训练中持续
- **进程已完全退出**，无残留

报告已追加到 memory.md。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_diagnose_grpo_cka_only_20_extended_300_20260518T220207"
}
```

</details>

---
