# ops check c4ext eval results

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/chats/worker_ops_check-c4ext-eval-results_20260521T025331.jsonl`
- **Structured JSON:** [`a8a5e6d093a9883af3b2.json`](../../sessions/a8/a8a5e6d093a9883af3b2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

21 recorded events

### Tool call

_source line 1 · 2026-05-21T02:54:25.635645+00:00_

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
  "session": "worker_ops_check-c4ext-eval-results_20260521T025331",
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

_source line 2 · 2026-05-21T02:54:25.636041+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-c4ext-eval-results_20260521T025331",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T02:54:25.636266+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-33015",
  "command": "ls -la /root/autodl-tmp/importance_margin_vla_compress/eval_results/eval_openvla_sc_m128_vtconly_20k_seed42_full.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-c4ext-eval-results_20260521T025331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-33015",
    "command": "ls -la /root/autodl-tmp/importance_margin_vla_compress/eval_results/eval_openvla_sc_m128_vtconly_20k_seed42_full.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-21T02:54:25.636418+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-33015",
  "command": "tail -50 /tmp/eval_full_openvla_sc_m128.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-c4ext-eval-results_20260521T025331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-33015",
    "command": "tail -50 /tmp/eval_full_openvla_sc_m128.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-21T02:54:25.636675+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/autodl-tmp/importance_margin_vla_compress/eval_results/eval_openvla_sc_m128_vtconly_20k_seed42_full.json': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 1.11}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-c4ext-eval-results_20260521T025331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T02:54:25.636853+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-20 20:33:21 [INFO]   Step 0/280\\n2026-05-20 20:33:21 [INFO]   Step 1/280\\n2026-05-20 20:33:21 [INFO]   Step 2/280\\n2026-05-20 20:33:31 [INFO]   Step 50/280\\n2026-05-20 20:33:41 [INFO]   Step 100/280\\n2026-05-20 20:33:51 [INFO]   Step 150/280\\n2026-05-20 20:34:01 [INFO]   Step 200/280\\n2026-05-20 20:34:11 [INFO]   Step 250/280\\n2026-05-20 20:34:17 [INFO]   Ep 37/50 | FAIL | steps=280\\n2026-05-20 20:34:19 [INFO]   Step 0/280\\n2026-05-20 20:34:19 [INFO]   Step 1/280\\n2026-05-20 20:34:19 [INFO]   Step 2/280\\n2026-05-20 20:34:28 [INFO]   Step 50/280\\n2026-05-20 20:34:37 [INFO]   Step 100/280\\n2026-05-20 20:34:45 [INFO]   Step 150/280\\n2026-05-20 20:34:55 [INFO]   Step 200/280\\n2026-05-20 20:35:04 [INFO]   Step 250/280\\n2026-05-20 20:35:09 [INFO]   Ep 38/50 | FAIL | steps=280\\n2026-05-20 20:35:11 [INFO]   Step 0/280\\n2026-05-20 20:35:11 [INFO]   Step 1/280\\n2026-05-20 20:35:11 [INFO]   Step 2/280\\n2026-05-20 20:35:21 [INFO]   Step 50/280\\n2026-05-20 20:35:30 [INFO]   Step 100/280\\n2026-05-20 20:35:39 [INFO]   Step 150/280\\n2026-05-20 20:35:49 [INFO]   Step 200/280\\n2026-05-20 20:36:00 [INFO]   Step 250/280\\n2026-05-20 20:36:06 [INFO]   Ep 39/50 | FAIL | steps=280\\n2026-05-20 20:36:08 [INFO]   Step 0/280\\n2026-05-20 20:36:08 [INFO]   Step 1/280\\n2026-05-20 20:36:08 [INFO]   Step 2/280\\n2026-05-20 20:36:18 [INFO]   Step 50/280\\n2026-05-20 20:36:27 [INFO]   Step 100/280\\n2026-05-20 20:36:37 [INFO]   Step 150/280\\n2026-05-20 20:36:46 [INFO]   Step 200/280\\n2026-05-20 20:36:56 [INFO]   Step 250/280\\n2026-05-20 20:37:02 [INFO]   Ep 40/50 | FAIL | steps=280\\n2026-05-20 20:37:04 [INFO]   Step 0/280\\n2026-05-20 20:37:04 [INFO]   Step 1/280\\n2026-05-20 20:37:04 [INFO]   Step 2/280\\n2026-05-20 20:37:13 [INFO]   Step 50/280\\n2026-05-20 20:37:22 [INFO]   Step 100/280\\n2026-05-20 20:37:31 [INFO]   Step 150/280\\n2026-05-20 20:37:41 [INFO]   Step 200/280\\n2026-05-20 20:37:51 [INFO] 
…[truncated 393 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-c4ext-eval-results_20260521T025331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T02:54:25.637035+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-33015",
  "command": "find /root/autodl-tmp/importance_margin_vla_compress/eval_results/ -name \"*m128*\" -o -name \"*20k*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-c4ext-eval-results_20260521T025331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-33015",
    "command": "find /root/autodl-tmp/importance_margin_vla_compress/eval_results/ -name \"*m128*\" -o -name \"*20k*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T02:54:25.637198+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/smart_compress_m128_libero_object.json\\n/root/autodl-tmp/importance_margin_vla_compress/eval_results/eval_smart_compress_m128_seed43.json\\n/root/autodl-tmp/importance_margin_vla_compress/eval_results/eval_openvla_sc_m128_vtconly_20k_seed42_dryrun.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-c4ext-eval-results_20260521T025331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T02:54:25.637333+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-33015",
  "command": "grep -c \"SUCCESS\\|FAIL\" /tmp/eval_full_openvla_sc_m128.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-c4ext-eval-results_20260521T025331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-33015",
    "command": "grep -c \"SUCCESS\\|FAIL\" /tmp/eval_full_openvla_sc_m128.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T02:54:25.637457+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-c4ext-eval-results_20260521T025331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T02:54:25.637576+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-33015",
  "command": "head -30 /tmp/eval_full_openvla_sc_m128.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-c4ext-eval-results_20260521T025331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-33015",
    "command": "head -30 /tmp/eval_full_openvla_sc_m128.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T02:54:25.637740+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-20 19:16:55 [INFO] Device: cuda:0\\n2026-05-20 19:17:10 [INFO] Loading OpenVLA from /root/autodl-tmp/openvla-libero-object\\n2026-05-20 19:17:11 [WARNING] Expected `transformers==4.40.1` and `tokenizers==0.19.1` but got `transformers==4.53.2` and `tokenizers==0.21.4`; there might be inference-time regressions due to dependency changes. If in doubt, pleaseuse the above versions.\\n\\rLoading checkpoint shards:   0%|          | 0/4 [00:00<?, ?it/s]\\rLoading checkpoint shards: 100%|██████████| 4/4 [00:00<00:00, 65.00it/s]\\nUsing a slow image processor as `use_fast` is unset and a slow processor was saved with this model. `use_fast=True` will be the default behavior in v4.52, even if the model was saved with a slow processor. This will result in minor differences in outputs. You'll still be able to use a slow processor with `use_fast=False`.\\n2026-05-20 19:17:22 [INFO] Checkpoint loaded with strict match\\n2026-05-20 19:17:22 [INFO] OpenVLASmartCompressWrapper loaded: M=128, compressor params=403308544\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n2026-05-20 19:17:23 [INFO] Suite: libero_object | Tasks: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] | Episodes: 50 | Max steps: 280\\n[robosuite WARNING] No private macro file found! (macros.py:53)\\n2026-05-20 19:17:23 [WARNING] No private macro file found!\\n[robosuite WARNING] It is recommended to use a private macro file (macros.py:54)\\n2026-05-20 19:17:23 [WARNING] It is recommended to use a private macro file\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (macros.py:55)\\n2026-05-20 19:17:23 [WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py\\n2026-05-20 19:17:23 [INFO] No OpenGL_accelerate module loaded: No module named 'OpenGL_accelerate'\\n2026-05-20 19:17:24 [INFO] --- Task 0: pick up the alphabet soup and place 
…[truncated 734 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-c4ext-eval-results_20260521T025331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T02:54:25.637899+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-33015",
  "command": "grep -c SUCCESS /tmp/eval_full_openvla_sc_m128.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-c4ext-eval-results_20260521T025331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-33015",
    "command": "grep -c SUCCESS /tmp/eval_full_openvla_sc_m128.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-21T02:54:25.638024+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-33015",
  "command": "grep -c FAIL /tmp/eval_full_openvla_sc_m128.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-c4ext-eval-results_20260521T025331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-33015",
    "command": "grep -c FAIL /tmp/eval_full_openvla_sc_m128.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T02:54:25.638158+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-33015",
  "command": "grep \"Task [0-9]\" /tmp/eval_full_openvla_sc_m128.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-c4ext-eval-results_20260521T025331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-33015",
    "command": "grep \"Task [0-9]\" /tmp/eval_full_openvla_sc_m128.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T02:54:25.638300+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"0\\n\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-c4ext-eval-results_20260521T025331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-21T02:54:25.638443+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"91\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-c4ext-eval-results_20260521T025331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-21T02:54:25.638567+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-20 19:17:24 [INFO] --- Task 0: pick up the alphabet soup and place it in the basket ---\\n2026-05-20 19:59:25 [INFO]   Task 0 SR: 0/50 (0.0%)\\n2026-05-20 19:59:25 [INFO] --- Task 1: pick up the cream cheese and place it in the basket ---\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-c4ext-eval-results_20260521T025331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T02:54:25.638688+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-33015",
  "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_results/eval_openvla_sc_m128_vtconly_20k_seed42_dryrun.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-c4ext-eval-results_20260521T025331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-33015",
    "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_results/eval_openvla_sc_m128_vtconly_20k_seed42_dryrun.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T02:54:25.638833+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model\\\": \\\"openvla_smart_compress\\\",\\n  \\\"suite\\\": \\\"libero_object\\\",\\n  \\\"n_queries\\\": 128,\\n  \\\"checkpoint\\\": \\\"checkpoints/openvla_sc_m128/checkpoint_step20000.pt\\\",\\n  \\\"total_episodes\\\": 2,\\n  \\\"total_successes\\\": 0,\\n  \\\"overall_success_rate\\\": 0.0,\\n  \\\"wilson_ci_95\\\": [\\n    0,\\n    0.6576\\n  ],\\n  \\\"num_episodes_per_task\\\": 2,\\n  \\\"max_steps\\\": 280,\\n  \\\"seed\\\": 42,\\n  \\\"per_task\\\": {\\n    \\\"0\\\": {\\n      \\\"task_id\\\": 0,\\n      \\\"task_description\\\": \\\"pick up the alphabet soup and place it in the basket\\\",\\n      \\\"success_count\\\": 0,\\n      \\\"total_episodes\\\": 2,\\n      \\\"success_rate\\\": 0.0,\\n      \\\"mean_steps\\\": 280.0\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-c4ext-eval-results_20260521T025331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-21T02:54:25.639028+00:00_

进程被 kill，未跑完。日志分析如下：

**已完成**：
- Task 0 ("pick up the alphabet soup and place it in the basket"): **0/50 (0.0%)**
- Task 1 ("pick up the cream cheese and place it in the basket"): 跑到 Ep 41/50 时中断

**未完成**：Task 2-9 全未跑。

**关键数据**：
- 总计 91 个 episode 全部 FAIL，0 个 SUCCESS
- 每个 episode 都跑满 280 步超时，说明模型动作完全不对（没有提前完成任务的情况）

**结论**：OpenVLA Smart Compress M=128 VTC-only 20K checkpoint 在 libero_object 上 success rate 为 **0%**（基于已完成的 91 episodes）。模型表现极差，即使跑完剩下的 episodes 结果也不会有意义改善。

**建议**：不需要重跑这个 eval。0/91 已经足够说明 20K checkpoint 的 VTC-only 方案不 work。需要排查训练是否有问题，或者 VTC-only 方案本身不可行。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ops_check-c4ext-eval-results_20260521T025331"
}
```

</details>

---
