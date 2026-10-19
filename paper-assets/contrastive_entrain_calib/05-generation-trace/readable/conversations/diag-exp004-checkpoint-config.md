# diag exp004 checkpoint config

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/chats/worker_diag_exp004-checkpoint-config_20260518T191111.jsonl`
- **Structured JSON:** [`e8aa6678a037bf393c12.json`](../../sessions/e8/e8aa6678a037bf393c12.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

25 recorded events

### Tool call

_source line 1 · 2026-05-18T19:11:59.005996+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_exp004-checkpoint-config_20260518T191111",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-18T19:11:59.006411+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_exp004-checkpoint-config_20260518T191111",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T19:11:59.006596+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-28034",
  "command": "grep -n \"save_steps\\|save_every\\|checkpoint\\|save_strategy\" /root/contrastive_entrain_calib/training/run_exp004_act_baseline.py | head -20",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_exp004-checkpoint-config_20260518T191111",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-28034",
    "command": "grep -n \"save_steps\\|save_every\\|checkpoint\\|save_strategy\" /root/contrastive_entrain_calib/training/run_exp004_act_baseline.py | head -20",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-18T19:11:59.006747+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"184:    model.gradient_checkpointing_enable(\\n185:        gradient_checkpointing_kwargs={\\\"use_reentrant\\\": False}\\n298:                if step % args.save_steps == 0:\\n299:                    ckpt_dir = os.path.join(args.output_dir, f\\\"checkpoint-{step}\\\")\\n302:                    logger.info(\\\"Saved checkpoint: %s\\\", ckpt_dir)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.14}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_exp004-checkpoint-config_20260518T191111",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T19:11:59.006929+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-28034",
  "command": "ls -la /root/contrastive_entrain_calib/checkpoints/exp004*/ 2>/dev/null || find /root/contrastive_entrain_calib -path \"*exp004*\" -type d 2>/dev/null || find /root/contrastive_entrain_calib -path \"*exp-004*\" -type d 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_exp004-checkpoint-config_20260518T191111",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-28034",
    "command": "ls -la /root/contrastive_entrain_calib/checkpoints/exp004*/ 2>/dev/null || find /root/contrastive_entrain_calib -path \"*exp004*\" -type d 2>/dev/null || find /root/contrastive_entrain_calib -path \"*exp-004*\" -type d 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-18T19:11:59.007086+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_exp004-checkpoint-config_20260518T191111",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-18T19:11:59.007212+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-28034",
  "command": "tail -30 ~/runs/contrastive_entrain_calib/exp-004.log 2>/dev/null || tail -30 ~/runs/contrastive_entrain_calib/exp004.log 2>/dev/null || echo \"No log file found\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_exp004-checkpoint-config_20260518T191111",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-28034",
    "command": "tail -30 ~/runs/contrastive_entrain_calib/exp-004.log 2>/dev/null || tail -30 ~/runs/contrastive_entrain_calib/exp004.log 2>/dev/null || echo \"No log file found\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-18T19:11:59.007339+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"No log file found\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_exp004-checkpoint-config_20260518T191111",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T19:11:59.007486+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-28034",
  "command": "grep -n \"save_steps\\|output_dir\" /root/contrastive_entrain_calib/training/run_exp004_act_baseline.py | head -20",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_exp004-checkpoint-config_20260518T191111",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-28034",
    "command": "grep -n \"save_steps\\|output_dir\" /root/contrastive_entrain_calib/training/run_exp004_act_baseline.py | head -20",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-18T19:11:59.007617+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"157:    os.makedirs(args.output_dir, exist_ok=True)\\n160:    with open(os.path.join(args.output_dir, \\\"config.json\\\"), \\\"w\\\") as f:\\n221:    log_path = os.path.join(args.output_dir, \\\"train_log.jsonl\\\")\\n298:                if step % args.save_steps == 0:\\n299:                    ckpt_dir = os.path.join(args.output_dir, f\\\"checkpoint-{step}\\\")\\n304:    final_dir = os.path.join(args.output_dir, \\\"final\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.55}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_exp004-checkpoint-config_20260518T191111",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T19:11:59.007754+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-28034",
  "command": "grep -rn \"save_steps\" /root/contrastive_entrain_calib/training/run_exp004_act_baseline.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_exp004-checkpoint-config_20260518T191111",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-28034",
    "command": "grep -rn \"save_steps\" /root/contrastive_entrain_calib/training/run_exp004_act_baseline.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-18T19:11:59.007922+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"298:                if step % args.save_steps == 0:\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_exp004-checkpoint-config_20260518T191111",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T19:11:59.008063+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-28034",
  "command": "find /root/contrastive_entrain_calib -name \"checkpoint-*\" -type d 2>/dev/null; find /root -name \"exp*004*\" -type d -maxdepth 4 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_exp004-checkpoint-config_20260518T191111",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-28034",
    "command": "find /root/contrastive_entrain_calib -name \"checkpoint-*\" -type d 2>/dev/null; find /root -name \"exp*004*\" -type d -maxdepth 4 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-18T19:11:59.008194+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/contrastive_entrain_calib/checkpoints/exp014_dryrun/checkpoint-2\\n/root/contrastive_entrain_calib/checkpoints/exp014_dryrun_v2/checkpoint-2\\n/root/contrastive_entrain_calib/outputs/exp-004-act-baseline/checkpoint-500\\n/root/contrastive_entrain_calib/outputs/exp-004-act-baseline/checkpoint-1000\\n/root/contrastive_entrain_calib/outputs/exp-004-act-baseline\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_exp004-checkpoint-config_20260518T191111",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-18T19:11:59.008315+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-28034",
  "command": "find ~/runs -name \"*.log\" -type f 2>/dev/null | head -20",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_exp004-checkpoint-config_20260518T191111",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-28034",
    "command": "find ~/runs -name \"*.log\" -type f 2>/dev/null | head -20",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-18T19:11:59.008437+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/runs/contrastive_entrain_calib/exp-014.log\\n/root/runs/contrastive_entrain_calib/exp-008.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_exp004-checkpoint-config_20260518T191111",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-18T19:11:59.008585+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-28034",
  "command": "grep -n \"add_argument.*save_steps\\|default.*save_steps\\|save.steps\" /root/contrastive_entrain_calib/training/run_exp004_act_baseline.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_exp004-checkpoint-config_20260518T191111",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-28034",
    "command": "grep -n \"add_argument.*save_steps\\|default.*save_steps\\|save.steps\" /root/contrastive_entrain_calib/training/run_exp004_act_baseline.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-18T19:11:59.008717+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"146:    parser.add_argument(\\\"--save-steps\\\", type=int, default=500)\\n298:                if step % args.save_steps == 0:\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_exp004-checkpoint-config_20260518T191111",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-18T19:11:59.008834+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-28034",
  "command": "cat /root/contrastive_entrain_calib/outputs/exp-004-act-baseline/config.json 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_exp004-checkpoint-config_20260518T191111",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-28034",
    "command": "cat /root/contrastive_entrain_calib/outputs/exp-004-act-baseline/config.json 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-18T19:11:59.008996+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_path\\\": \\\"/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B\\\",\\n  \\\"data_path\\\": \\\"/root/contrastive_entrain_calib/data/calibration_v2_1_expanded.jsonl\\\",\\n  \\\"output_dir\\\": \\\"/root/contrastive_entrain_calib/outputs/exp-004-act-baseline\\\",\\n  \\\"max_steps\\\": 2,\\n  \\\"grad_accum\\\": 16,\\n  \\\"lr\\\": 5e-05,\\n  \\\"warmup_steps\\\": 200,\\n  \\\"lambda_l2\\\": 0.1,\\n  \\\"max_seq_len\\\": 1024,\\n  \\\"logging_steps\\\": 10,\\n  \\\"save_steps\\\": 500,\\n  \\\"seed\\\": 42,\\n  \\\"lora_rank\\\": 64\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_exp004-checkpoint-config_20260518T191111",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-18T19:11:59.009117+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-28034",
  "command": "tail -5 /root/contrastive_entrain_calib/outputs/exp-004-act-baseline/train_log.jsonl 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_exp004-checkpoint-config_20260518T191111",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-28034",
    "command": "tail -5 /root/contrastive_entrain_calib/outputs/exp-004-act-baseline/train_log.jsonl 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-18T19:11:59.009231+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-28034",
  "command": "ls -la /root/contrastive_entrain_calib/outputs/exp-004-act-baseline/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_exp004-checkpoint-config_20260518T191111",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-28034",
    "command": "ls -la /root/contrastive_entrain_calib/outputs/exp-004-act-baseline/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-18T19:11:59.009375+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"step\\\": 1310, \\\"sft_loss\\\": 2.1e-05, \\\"l2_loss\\\": 0.00264516, \\\"total_loss\\\": 0.000285, \\\"lr\\\": 4.288461538461538e-05, \\\"elapsed_s\\\": 11374.2}\\n{\\\"step\\\": 1320, \\\"sft_loss\\\": 2.2e-05, \\\"l2_loss\\\": 0.00257263, \\\"total_loss\\\": 0.00028, \\\"lr\\\": 4.282051282051282e-05, \\\"elapsed_s\\\": 11475.1}\\n{\\\"step\\\": 1330, \\\"sft_loss\\\": 2.3e-05, \\\"l2_loss\\\": 0.00264025, \\\"total_loss\\\": 0.000288, \\\"lr\\\": 4.275641025641026e-05, \\\"elapsed_s\\\": 11577.5}\\n{\\\"step\\\": 1340, \\\"sft_loss\\\": 2e-05, \\\"l2_loss\\\": 0.00270305, \\\"total_loss\\\": 0.000291, \\\"lr\\\": 4.269230769230769e-05, \\\"elapsed_s\\\": 11677.0}\\n{\\\"step\\\": 1350, \\\"sft_loss\\\": 2.2e-05, \\\"l2_loss\\\": 0.0027029, \\\"total_loss\\\": 0.000292, \\\"lr\\\": 4.262820512820513e-05, \\\"elapsed_s\\\": 11775.4}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_exp004-checkpoint-config_20260518T191111",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-18T19:11:59.009519+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 32\\ndrwxr-xr-x 4 root root   113 May 19 02:16 .\\ndrwxr-xr-x 3 root root    71 May 18 23:55 ..\\ndrwxr-xr-x 2 root root  4096 May 19 02:16 checkpoint-1000\\ndrwxr-xr-x 2 root root  4096 May 19 01:05 checkpoint-500\\n-rw-r--r-- 1 root root   425 May 19 00:28 config.json\\n-rw-r--r-- 1 root root 17637 May 19 03:11 train_log.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_exp004-checkpoint-config_20260518T191111",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-18T19:11:59.009681+00:00_

汇总结果：

## exp-004 Checkpoint 状态

| 项目 | 值 |
|---|---|
| **save_steps** | 500 |
| **max_steps** | config.json 写的 2（可能是 dry-run 残留），实际在跑 8000 |
| **当前进度** | step 1350 / 8000 |
| **SFT loss** | ~2.2e-05（已完全记忆，符合预期） |

### 已保存的 checkpoint
- `checkpoint-500` ✅
- `checkpoint-1000` ✅

### Director 要求的 checkpoint 覆盖情况

| 要求 step | 状态 |
|---|---|
| 500 | ✅ 已保存 |
| 1000 | ✅ 已保存 |
| 2000 | ⏳ 将在 ~step 2000 自动保存（save_steps=500 整除 2000） |
| 4000 | ⏳ 将自动保存（save_steps=500 整除 4000） |
| 8000 | ⏳ 将自动保存（save_steps=500 整除 8000） |

### 结论

**save_steps=500 无需修改。** 500 能整除 500、1000、2000、4000、8000，所有 Director 要求的 checkpoint 都会被自动保存。额外还会保存 1500、2500、3000、3500、4500、5000、5500、6000、6500、7000、7500 这些中间点（磁盘空间允许的话无害，还能提供更细粒度的分析选项）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_diag_exp004-checkpoint-config_20260518T191111"
}
```

</details>

---
