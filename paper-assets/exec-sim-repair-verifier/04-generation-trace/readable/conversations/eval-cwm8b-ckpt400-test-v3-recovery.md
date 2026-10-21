# eval cwm8b ckpt400 test v3 recovery

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/chats/worker_eval_cwm8b-ckpt400-test-v3-recovery_20260516T011402.jsonl`
- **Structured JSON:** [`0d7c1d38bf76a777bda1.json`](../../sessions/0d/0d7c1d38bf76a777bda1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

23 recorded events

### Tool call

_source line 1 · 2026-05-16T01:15:32.578776+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__register_cron,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__submit_training_job,mcp__agent-ml-research__read_registry",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_cwm8b-ckpt400-test-v3-recovery_20260516T011402",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__register_cron,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__submit_training_job,mcp__agent-ml-research__read_registry",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T01:15:32.579174+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_cwm8b-ckpt400-test-v3-recovery_20260516T011402",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T01:15:32.579359+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-westd-4x5090",
  "command": "ps -p 443216 -o pid,etime,cmd=",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_cwm8b-ckpt400-test-v3-recovery_20260516T011402",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-westd-4x5090",
    "command": "ps -p 443216 -o pid,etime,cmd=",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-16T01:15:32.579497+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-westd-4x5090",
  "command": "tmux ls",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_cwm8b-ckpt400-test-v3-recovery_20260516T011402",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-westd-4x5090",
    "command": "tmux ls",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-16T01:15:32.579643+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"   PID     ELAPSED \\n443216       27:32 bash -c rm -f /tmp/agent-ml-exit/cwm8b-ckpt400-test-eval-v3.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/exec-sim-repair-verifier/cwm8b-ckpt400-test-eval-v3.log; printf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\" > /tmp/agent-ml-exit/cwm8b-ckpt400-test-eval-v3.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /home/sonny/exec-sim-repair-verifier && export CUDA_VISIBLE_DEVICES=3 && timeout 86400 env bash -c 'bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && HF_HUB_OFFLINE=1 python3 eval_repo_cwm.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cwm_8b_conda/checkpoint-400 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ --split test --device cuda:0 --batch_size 8 --max_new_tokens 1024 --output_dir /root/autodl-tmp/eval_results/cwm_8b_ckpt400_test/\\\"'; } > ~/runs/exec-sim-repair-verifier/cwm8b-ckpt400-test-eval-v3.log 2>&1\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.48}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_cwm8b-ckpt400-test-v3-recovery_20260516T011402",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T01:15:32.579780+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'tmux' is not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_cwm8b-ckpt400-test-v3-recovery_20260516T011402",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T01:15:32.579936+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-westd-4x5090",
  "command": "nvidia-smi --query-gpu=index,utilization.gpu,memory.used,memory.total --format=csv,noheader",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_cwm8b-ckpt400-test-v3-recovery_20260516T011402",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-westd-4x5090",
    "command": "nvidia-smi --query-gpu=index,utilization.gpu,memory.used,memory.total --format=csv,noheader",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T01:15:32.580070+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 78 %, 17609 MiB, 32607 MiB\\n1, 80 %, 17609 MiB, 32607 MiB\\n2, 100 %, 0 MiB, 32607 MiB\\n3, 88 %, 21133 MiB, 32607 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.54}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_cwm8b-ckpt400-test-v3-recovery_20260516T011402",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T01:15:32.580206+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-westd-4x5090",
  "command": "ls /root/autodl-tmp/eval_results/cwm_8b_ckpt400_test/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_cwm8b-ckpt400-test-v3-recovery_20260516T011402",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-westd-4x5090",
    "command": "ls /root/autodl-tmp/eval_results/cwm_8b_ckpt400_test/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-16T01:15:32.580333+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'cwm8b-ckpt400-test-eval-v3'}",
  "project": "exec-sim-repair-verifier",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_cwm8b-ckpt400-test-v3-recovery_20260516T011402",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'cwm8b-ckpt400-test-eval-v3'}",
    "project": "exec-sim-repair-verifier",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-16T01:15:32.580462+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"eval_v2.log\\nresults_incremental.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_cwm8b-ckpt400-test-v3-recovery_20260516T011402",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T01:15:32.580587+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5401}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_cwm8b-ckpt400-test-v3-recovery_20260516T011402",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T01:15:32.580744+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-westd-4x5090",
  "command": "wc -l /root/autodl-tmp/eval_results/cwm_8b_ckpt400_test/results_incremental.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_cwm8b-ckpt400-test-v3-recovery_20260516T011402",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-westd-4x5090",
    "command": "wc -l /root/autodl-tmp/eval_results/cwm_8b_ckpt400_test/results_incremental.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T01:15:32.580901+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"5512 /root/autodl-tmp/eval_results/cwm_8b_ckpt400_test/results_incremental.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_cwm8b-ckpt400-test-v3-recovery_20260516T011402",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T01:15:32.581038+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-westd-4x5090",
  "command": "tail -20 /root/runs/exec-sim-repair-verifier/cwm8b-ckpt400-test-eval-v3.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_cwm8b-ckpt400-test-v3-recovery_20260516T011402",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-westd-4x5090",
    "command": "tail -20 /root/runs/exec-sim-repair-verifier/cwm8b-ckpt400-test-eval-v3.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T01:15:32.581255+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-16 08:56:29,783 INFO [CWM] 5360/9784  running_acc=67.1%  (new=73 resumed=5287)\\n2026-05-16 08:57:26,562 INFO [CWM] 5368/9784  running_acc=67.9%  (new=81 resumed=5287)\\n2026-05-16 08:58:23,110 INFO [CWM] 5376/9784  running_acc=67.4%  (new=89 resumed=5287)\\n2026-05-16 08:59:19,589 INFO [CWM] 5384/9784  running_acc=67.0%  (new=97 resumed=5287)\\n2026-05-16 09:00:16,325 INFO [CWM] 5392/9784  running_acc=66.7%  (new=105 resumed=5287)\\n2026-05-16 09:01:12,779 INFO [CWM] 5400/9784  running_acc=64.6%  (new=113 resumed=5287)\\n2026-05-16 09:02:09,391 INFO [CWM] 5408/9784  running_acc=64.5%  (new=121 resumed=5287)\\n2026-05-16 09:02:56,498 INFO [CWM] 5416/9784  running_acc=62.8%  (new=129 resumed=5287)\\n2026-05-16 09:03:53,035 INFO [CWM] 5424/9784  running_acc=61.3%  (new=137 resumed=5287)\\n2026-05-16 09:04:49,749 INFO [CWM] 5432/9784  running_acc=59.3%  (new=145 resumed=5287)\\n2026-05-16 09:05:46,232 INFO [CWM] 5440/9784  running_acc=59.5%  (new=153 resumed=5287)\\n2026-05-16 09:06:42,810 INFO [CWM] 5448/9784  running_acc=60.2%  (new=161 resumed=5287)\\n2026-05-16 09:07:39,198 INFO [CWM] 5456/9784  running_acc=59.8%  (new=169 resumed=5287)\\n2026-05-16 09:08:35,726 INFO [CWM] 5464/9784  running_acc=60.5%  (new=177 resumed=5287)\\n2026-05-16 09:09:23,021 INFO [CWM] 5472/9784  running_acc=61.1%  (new=185 resumed=5287)\\n2026-05-16 09:10:19,558 INFO [CWM] 5480/9784  running_acc=60.1%  (new=193 resumed=5287)\\n2026-05-16 09:11:16,257 INFO [CWM] 5488/9784  running_acc=59.2%  (new=201 resumed=5287)\\n2026-05-16 09:12:12,815 INFO [CWM] 5496/9784  running_acc=60.3%  (new=209 resumed=5287)\\n2026-05-16 09:13:09,266 INFO [CWM] 5504/9784  running_acc=59.9%  (new=217 resumed=5287)\\n2026-05-16 09:14:06,171 INFO [CWM] 5512/9784  running_acc=60.4%  (new=225 resumed=5287)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_cwm8b-ckpt400-test-v3-recovery_20260516T011402",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T01:15:32.581418+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "limit": "10",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_cwm8b-ckpt400-test-v3-recovery_20260516T011402",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "limit": "10",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T01:15:32.581760+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"cls8b-s42-resume-ckpt3600-mutation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:34:55.660Z\", \"updated_at\": \"2026-05-16T01:14:03.311Z\", \"failure_reason\": \"CLEARED: was false positive from cron. Experiment still in PREPARING, awaiting GPU allocation.\", \"conclusion\": \"success\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T23:35:02.463599+00:00\"}]}, \"spec\": {\"command\": \"python3 mutation_breakdown.py (analysis of existing ckpt-3600 test predictions)\", \"server\": \"seetacloud-westd-4x5090\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/swebench_full/swebench_test.jsonl\", \"data_count\": 9784, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-3600/\", \"eval_data\": \"swebench_test (full, n=9784)\"}, \"metrics\": {\"overall_accuracy\": 84.4849, \"overall_correct\": 8266, \"overall_total\": 9784, \"gold_accuracy\": 96.2443, \"gold_correct\": 4459, \"gold_total\": 4633, \"mutation_operator_swap_accuracy\": 81.3822, \"mutation_operator_swap_correct\": 2732, \"mutation_operator_swap_total\": 3357, \"mutation_off_by_one_accuracy\": 86.8852, \"mutation_off_by_one_correct\": 159, \"mutation_off_by_one_total\": 183, \"mutation_return_value_accuracy\": 75.4448, \"mutation_return_value_correct\": 424, \"mutation_return_value_total\": 562, \"mutation_boundary_removal_accuracy\": 46.9018, \"mutation_boundary_removal_correct\": 492, \"mutation_boundary_removal_total\": 1049}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-3600/\", \"log_path\": \"/root/autodl-tmp/eval_results/cls8b_s42_resume_test_ckpt3600_mutation/\", \"completed_at\": \"2026-05-16T01:13:58.493Z\"}, \"cwm8b-ckpt400-test-eval-v3\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T00:46:28.45
…[truncated 12380 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_cwm8b-ckpt400-test-v3-recovery_20260516T011402",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T01:15:32.582047+00:00_

called mcp__agent-ml-research__register_cron

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_cron</summary>

```json
{
  "exp_id": "cwm8b-ckpt400-test-eval-v3",
  "server": "seetacloud-westd-4x5090",
  "pid": "443216",
  "log_path": "~/runs/exec-sim-repair-verifier/cwm8b-ckpt400-test-eval-v3.log",
  "project": "exec-sim-repair-verifier",
  "interval_seconds": "120"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_cwm8b-ckpt400-test-v3-recovery_20260516T011402",
  "tool": "mcp__agent-ml-research__register_cron",
  "tool_args": {
    "exp_id": "cwm8b-ckpt400-test-eval-v3",
    "server": "seetacloud-westd-4x5090",
    "pid": "443216",
    "log_path": "~/runs/exec-sim-repair-verifier/cwm8b-ckpt400-test-eval-v3.log",
    "project": "exec-sim-repair-verifier",
    "interval_seconds": "120"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T01:15:32.582202+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cron for 'cwm8b-ckpt400-test-eval-v3' already registered. Delete it first.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_cwm8b-ckpt400-test-v3-recovery_20260516T011402",
  "tool": "mcp__agent-ml-research__register_cron",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T01:15:32.582345+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,CronList,CronDelete",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_cwm8b-ckpt400-test-v3-recovery_20260516T011402",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute,CronList,CronDelete",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T01:15:32.582472+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_cwm8b-ckpt400-test-v3-recovery_20260516T011402",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-16T01:15:32.582681+00:00_

Cron 已存在，无需重新注册。实验状态正常。

**诊断结果：**

| 项目 | 状态 |
|------|------|
| PID 443216 | 存活，运行 27+ 分钟 |
| GPU:3 | 88% 利用率，21133/32607 MiB |
| 进度 | 5512/9784 (56.3%) |
| running_acc | 60.4% (new=225, resumed=5287) |
| Registry | 已是 RUNNING |
| Cron | 已注册（未丢失） |
| 速率 | ~8.4 samples/min |
| ETA | ~2026-05-16 17:30 UTC（剩余 ~508 min） |

**采取的行动：** 无需干预。进程正常运行，registry 状态正确，cron 监控已存在。

**注意：** running_acc 从 v2 的 ~65% 下降到 60.4%，但当前仅 225 个 new samples，统计尚不稳定，需等全部完成后看最终 accuracy。CLS 8B test=84.48% vs CWM 8B 当前趋势 ~60%，gap 可能在 ~24pp。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_eval_cwm8b-ckpt400-test-v3-recovery_20260516T011402"
}
```

</details>

---
