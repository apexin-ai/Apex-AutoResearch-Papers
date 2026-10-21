# ops humaneval relay cuda3 sft standard

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/chats/worker_ops_humaneval_relay_cuda3_sft_standard_20260519T090821.jsonl`
- **Structured JSON:** [`e28a79a1b5fc4a361178.json`](../../sessions/e2/e28a79a1b5fc4a361178.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

19 recorded events

### Tool call

_source line 1 · 2026-05-19T09:09:36.689043+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_relay_cuda3_sft_standard_20260519T090821",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T09:09:36.689400+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_relay_cuda3_sft_standard_20260519T090821",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T09:09:36.689573+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29022",
  "command": "ls -la /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_relay_cuda3_sft_standard_20260519T090821",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29022",
    "command": "ls -la /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-19T09:09:36.689725+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29022",
  "command": "tmux ls",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_relay_cuda3_sft_standard_20260519T090821",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29022",
    "command": "tmux ls",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-19T09:09:36.689888+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 12046280\\ndrwxr-xr-x  2 root root        4096 May 19 07:12 .\\ndrwxr-xr-x 40 root root        4096 May 19 06:43 ..\\n-rw-r--r--  1 root root        2246 May 19 07:12 chat_template.jinja\\n-rw-r--r--  1 root root        1733 May 19 07:11 config.json\\n-rw-r--r--  1 root root         240 May 19 07:11 generation_config.json\\n-rw-r--r--  1 root root 12323931184 May 19 07:12 model.safetensors\\n-rw-r--r--  1 root root    11421907 May 19 07:12 tokenizer.json\\n-rw-r--r--  1 root root         420 May 19 07:12 tokenizer_config.json\\n-rw-r--r--  1 root root        5777 May 19 07:12 training_args.bin\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.07}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_relay_cuda3_sft_standard_20260519T090821",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T09:09:36.690026+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'tmux' is not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_relay_cuda3_sft_standard_20260519T090821",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T09:09:36.690150+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29022",
  "command": "find /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20/ -name \"*.safetensors\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_relay_cuda3_sft_standard_20260519T090821",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29022",
    "command": "find /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20/ -name \"*.safetensors\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T09:09:36.690295+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20/model.safetensors\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_relay_cuda3_sft_standard_20260519T090821",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T09:09:36.690446+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-29022",
  "command": "tmux ls 2>/dev/null; echo \"---\"; nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory,name --format=csv,noheader; echo \"---\"; nvidia-smi --query-gpu=index,memory.used,memory.total,utilization.gpu --format=csv,noheader",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_relay_cuda3_sft_standard_20260519T090821",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-29022",
    "command": "tmux ls 2>/dev/null; echo \"---\"; nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory,name --format=csv,noheader; echo \"---\"; nvidia-smi --query-gpu=index,memory.used,memory.total,utilization.gpu --format=csv,noheader",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T09:09:36.690595+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"eval_gsm8k_std_fair_v2: 1 windows (created Tue May 19 16:58:39 2026)\\neval_humaneval_grpo_standard_20_fair_2048_v3: 1 windows (created Tue May 19 15:03:11 2026)\\neval_humaneval_rasp_fair: 1 windows (created Tue May 19 14:38:33 2026)\\neval_humaneval_sft_cka_only_20_2048_v2: 1 windows (created Tue May 19 15:38:18 2026)\\n---\\n83299, GPU-b0514b26-657b-5010-9c8a-0cfa75ef3680, 27798 MiB, /root/miniconda3/bin/python\\n78740, GPU-ce0f2777-60eb-9e2d-8a71-b291f0fd9862, 17268 MiB, /root/miniconda3/bin/python\\n76392, GPU-fd1974e9-1073-6c9d-ef0e-b4517a1bd1ac, 17268 MiB, /root/miniconda3/bin/python\\n74303, GPU-893d671d-d57f-55be-2df8-686a356756ee, 17802 MiB, /root/miniconda3/bin/python\\n---\\n0, 27807 MiB, 97887 MiB, 99 %\\n1, 17277 MiB, 97887 MiB, 92 %\\n2, 17277 MiB, 97887 MiB, 96 %\\n3, 17811 MiB, 97887 MiB, 95 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.61}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_relay_cuda3_sft_standard_20260519T090821",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T09:09:36.690758+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-29022",
  "command": "tmux capture-pane -t eval_humaneval_rasp_fair -p | tail -5",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_relay_cuda3_sft_standard_20260519T090821",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-29022",
    "command": "tmux capture-pane -t eval_humaneval_rasp_fair -p | tail -5",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T09:09:36.690899+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"HumanEval:  60%|██████    | 99/164 [1:34:21<1:20:36, 74.41s/it]2026-05-19 16:17:\\n28,468 [INFO] Progress: 100/164, Pass@1: 0.1300\\nHumanEval:  73%|███████▎  | 119/164 [1:58:19<39:14, 52.32s/it]2026-05-19 16:41:2\\n6,603 [INFO] Progress: 120/164, Pass@1: 0.1250\\nHumanEval:  84%|████████▍ | 138/164 [2:27:20<43:37, 100.66s/it]\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_relay_cuda3_sft_standard_20260519T090821",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T09:09:36.691064+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_sft_standard_20_2048_v3",
  "field": "status",
  "value": "PREPARING"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_relay_cuda3_sft_standard_20260519T090821",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_sft_standard_20_2048_v3",
    "field": "status",
    "value": "PREPARING"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T09:09:36.691196+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_sft_standard_20_2048_v3\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T09:09:05.797Z\", \"updated_at\": \"2026-05-19T09:09:05.797Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.318}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_relay_cuda3_sft_standard_20260519T090821",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T09:09:36.691341+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_sft_standard_20_2048_v3",
  "field": "hypothesis",
  "value": "SFT Standard 20% HumanEval pass@1 @2048. Uses current sft_standard_20 model on westd-29022 (same as MATH-500 eval at 25.8%). Fills SFT×method HumanEval matrix. Compare with GRPO Standard fair (~11% interim) and SFT CKA-only (~30% interim)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_relay_cuda3_sft_standard_20260519T090821",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_sft_standard_20_2048_v3",
    "field": "hypothesis",
    "value": "SFT Standard 20% HumanEval pass@1 @2048. Uses current sft_standard_20 model on westd-29022 (same as MATH-500 eval at 25.8%). Fills SFT×method HumanEval matrix. Compare with GRPO Standard fair (~11% interim) and SFT CKA-only (~30% interim)."
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T09:09:36.691491+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_sft_standard_20_2048_v3\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T09:09:05.797Z\", \"updated_at\": \"2026-05-19T09:09:11.817Z\", \"hypothesis\": \"SFT Standard 20% HumanEval pass@1 @2048. Uses current sft_standard_20 model on westd-29022 (same as MATH-500 eval at 25.8%). Fills SFT×method HumanEval matrix. Compare with GRPO Standard fair (~11% interim) and SFT CKA-only (~30% interim).\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1685}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_relay_cuda3_sft_standard_20260519T090821",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T09:09:36.691650+00:00_

called ScheduleWakeup

<details open><summary>🔧 Tool call — ScheduleWakeup</summary>

````json
{
  "delaySeconds": "1800",
  "reason": "等待 RASP fair eval 完成（138/164, ~40min 剩余），cuda:3 释放后启动 SFT Standard HumanEval",
  "prompt": "GPU 接力任务：等 cuda:3 空闲后启动 SFT Standard HumanEval @2048。\n\n## 背景\nwestd-29022 cuda:3 正在跑 HumanEval GRPO RASP fair（134/164，~45min 后完成）。完成后立即启动 SFT Standard HumanEval eval。\n\n## 步骤\n\n### 1. 确认 checkpoint 路径\nSSH 到 westd-29022：\n```bash\nls -la /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20/\nls /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20/*.safetensors 2>/dev/null | head -3\n```\n\n### 2. 等待 cuda:3 释放\n监控 RASP fair eval 完成：\n```bash\n# 检查 RASP fair 是否还在跑\nwhile true; do\n    if ! tmux has-session -t eval_humaneval_rasp_fair 2>/dev/null; then\n        echo \"RASP fair 完成，cuda:3 释放\"\n        break\n    fi\n    echo \"$(date): RASP fair 仍在运行...\"\n    sleep 60\ndone\n```\n\n### 3. 收割 RASP fair 结果\n```bash\ncat /root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_grpo_rasp_20_fair_2048.json | python3 -c \"\nimport json, sys\nd = json.load(sys.stdin)\nprint(f'RASP fair HumanEval: pass@1={d.get(\\\"pass_at_1\\\",\\\"?\\\")}, correct={d.get(\\\"n_correct\\\",\\\"?\\\")}/{d.get(\\\"n_total\\\",\\\"?\\\")}')\n\"\n```\n\n### 4. 启动 SFT Standard HumanEval\n用 submit_training_job 提交：\n- exp_id: eval_humaneval_sft_standard_20_2048_v3\n- server: westd-29022\n- gpu_ids: [3]\n- command: `bash -c \"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_sft_standard_20_2048_v3.json\"`\n\n提交前先创建 registry 条目：\n1. update_registry(exp_id=\"eval_humaneval_sft_standard_20_2048_v3\", field=\"status\", value=\"PREPARING\")\n2. update_registry(exp_id=\"eval_humaneval_sft_standard_20_2048_v3\", field=\"hypothesis\", value=\"SFT Standard 20% HumanEval pass@1 @2048. Uses current sft_standard_20 model on westd-29022 (same as MATH-500 eval at 25.8%). Fills SFT×method HumanEval matrix. Compare with GRPO Standard fair (~11% interim) and SFT CKA-only (~30% interim).\")\n\n### 5. 验证启动成功\n```bash\nnvidia-smi | grep -A2 \"cuda:3\"\ntmux ls | grep standard\n```\n\n## 产出\n1. RASP fair HumanEval 最终 pass@1\n2. SFT Standard HumanEval 启动确认（PID、GPU 占用）\n\n## 注意\n- 确保 conda 激活（/root/miniconda3/bin/python）\n- eval_humaneval.py 已修复 sys.executable\n- 如果 sft_standard_20/ 不存在，报告错误不要猜测路径"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_ops_humaneval_relay_cuda3_sft_standard_20260519T090821",
  "tool": "ScheduleWakeup",
  "tool_args": {
    "delaySeconds": "1800",
    "reason": "等待 RASP fair eval 完成（138/164, ~40min 剩余），cuda:3 释放后启动 SFT Standard HumanEval",
    "prompt": "GPU 接力任务：等 cuda:3 空闲后启动 SFT Standard HumanEval @2048。\n\n## 背景\nwestd-29022 cuda:3 正在跑 HumanEval GRPO RASP fair（134/164，~45min 后完成）。完成后立即启动 SFT Standard HumanEval eval。\n\n## 步骤\n\n### 1. 确认 checkpoint 路径\nSSH 到 westd-29022：\n```bash\nls -la /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20/\nls /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20/*.safetensors 2>/dev/null | head -3\n```\n\n### 2. 等待 cuda:3 释放\n监控 RASP fair eval 完成：\n```bash\n# 检查 RASP fair 是否还在跑\nwhile true; do\n    if ! tmux has-session -t eval_humaneval_rasp_fair 2>/dev/null; then\n        echo \"RASP fair 完成，cuda:3 释放\"\n        break\n    fi\n    echo \"$(date): RASP fair 仍在运行...\"\n    sleep 60\ndone\n```\n\n### 3. 收割 RASP fair 结果\n```bash\ncat /root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_grpo_rasp_20_fair_2048.json | python3 -c \"\nimport json, sys\nd = json.load(sys.stdin)\nprint(f'RASP fair HumanEval: pass@1={d.get(\\\"pass_at_1\\\",\\\"?\\\")}, correct={d.get(\\\"n_correct\\\",\\\"?\\\")}/{d.get(\\\"n_total\\\",\\\"?\\\")}')\n\"\n```\n\n### 4. 启动 SFT Standard HumanEval\n用 submit_training_job 提交：\n- exp_id: eval_humaneval_sft_standard_20_2048_v3\n- server: westd-29022\n- gpu_ids: [3]\n- command: `bash -c \"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_sft_standard_20_2048_v3.json\"`\n\n提交前先创建 registry 条目：\n1. update_registry(exp_id=\"eval_humaneval_sft_standard_20_2048_v3\", field=\"status\", value=\"PREPARING\")\n2. update_registry(exp_id=\"eval_humaneval_sft_standard_20_2048_v3\", field=\"hypothesis\", value=\"SFT Standard 20% HumanEval pass@1 @2048. Uses current sft_standard_20 model on westd-29022 (same as MATH-500 eval at 25.8%). Fills SFT×method HumanEval matrix. Compare with GRPO Standard fair (~11% interim) and SFT CKA-only (~30% interim).\")\n\n### 5. 验证启动成功\n```bash\nnvidia-smi | grep -A2 \"cuda:3\"\ntmux ls | grep standard\n```\n\n## 产出\n1. RASP fair HumanEval 最终 pass@1\n2. SFT Standard HumanEval 启动确认（PID、GPU 占用）\n\n## 注意\n- 确保 conda 激活（/root/miniconda3/bin/python）\n- eval_humaneval.py 已修复 sys.executable\n- 如果 sft_standard_20/ 不存在，报告错误不要猜测路径"
  }
}
````

</details>

---

### Tool result

_source line 18 · 2026-05-19T09:09:36.691803+00:00_

Next wakeup scheduled for 09:40:00 (in 1829s).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_humaneval_relay_cuda3_sft_standard_20260519T090821",
  "tool": "ScheduleWakeup",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-19T09:09:36.691961+00:00_

当前状态：
- **Checkpoint**: `/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20/model.safetensors` (12.3GB) ✓
- **RASP fair 进度**: 138/164, pass@1=0.125 interim, ~40min 剩余
- **Registry**: `eval_humaneval_sft_standard_20_2048_v3` 已创建 (PREPARING)
- **下次检查**: ~30 分钟后，RASP fair 应已完成，届时收割结果并启动 SFT Standard HumanEval

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ops_humaneval_relay_cuda3_sft_standard_20260519T090821"
}
```

</details>

---
