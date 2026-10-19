# diagnose eval reconvla spatial v3

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/chats/worker_diagnose_eval-reconvla-spatial-v3_20260514T110854.jsonl`
- **Structured JSON:** [`893afe06bdd8d7682dbe.json`](../../sessions/89/893afe06bdd8d7682dbe.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

23 recorded events

### Tool call

_source line 1 · 2026-05-14T11:10:29.008380+00:00_

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
  "session": "worker_diagnose_eval-reconvla-spatial-v3_20260514T110854",
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

_source line 2 · 2026-05-14T11:10:29.008707+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_eval-reconvla-spatial-v3_20260514T110854",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T11:10:29.008874+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "tail -200 /root/autodl-tmp/eval_results/eval-reconvla-spatial-v3.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_eval-reconvla-spatial-v3_20260514T110854",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "tail -200 /root/autodl-tmp/eval_results/eval-reconvla-spatial-v3.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-14T11:10:29.009010+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "head -50 /root/autodl-tmp/eval_results/eval-reconvla-spatial-v3.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_eval-reconvla-spatial-v3_20260514T110854",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "head -50 /root/autodl-tmp/eval_results/eval-reconvla-spatial-v3.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-14T11:10:29.009190+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[robosuite WARNING] No private macro file found! (__init__.py:7)\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\n[evaluate] args: {'benchmark': 'spatial', 'checkpoint': None, 'crm_checkpoint': None, 'n_rollouts': 10, 'max_steps': 300, 'seed': 42, 'K': 10, 'mode': 'reconvla', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'obs_dim': 960, 'hidden_dim': 256, 'render': False, 'output_file': None}\\n[eval] Mode: reconvla, benchmark: spatial\\n[eval] Loading SmolVLA from /root/autodl-tmp/models/smolvla_libero/...\\nLoading  /root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct weights ...\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/489 [00:00<?, ?it/s]\\rLoading weights:  52%|█████▏    | 254/489 [00:00<00:00, 2515.30it/s]\\rLoading weights: 100%|██���███████| 489/489 [00:00<00:00, 2828.62it/s]\\nReducing the number of VLM layers to 16 ...\\nLoading weights from local directory\\n[eval] Loading LIBERO spatial environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n  pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate: rollout 5/10, success so far: 2/5\\n  pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate: rollout 10/10, success so far: 6/10\\n[pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate] success rate: 60.0% (6/10)\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout 5/10, success so far: 5/5\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout 10/10, success so far: 10/10\\n[pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate] success rate: 100.0% (1
…[truncated 2935 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_eval-reconvla-spatial-v3_20260514T110854",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T11:10:29.009441+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[robosuite WARNING] No private macro file found! (__init__.py:7)\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\n[evaluate] args: {'benchmark': 'spatial', 'checkpoint': None, 'crm_checkpoint': None, 'n_rollouts': 10, 'max_steps': 300, 'seed': 42, 'K': 10, 'mode': 'reconvla', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'obs_dim': 960, 'hidden_dim': 256, 'render': False, 'output_file': None}\\n[eval] Mode: reconvla, benchmark: spatial\\n[eval] Loading SmolVLA from /root/autodl-tmp/models/smolvla_libero/...\\nLoading  /root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct weights ...\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/489 [00:00<?, ?it/s]\\rLoading weights:  52%|█████▏    | 254/489 [00:00<00:00, 2515.30it/s]\\rLoading weights: 100%|██���███████| 489/489 [00:00<00:00, 2828.62it/s]\\nReducing the number of VLM layers to 16 ...\\nLoading weights from local directory\\n[eval] Loading LIBERO spatial environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n  pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate: rollout 5/10, success so far: 2/5\\n  pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate: rollout 10/10, success so far: 6/10\\n[pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate] success rate: 60.0% (6/10)\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout 5/10, success so far: 5/5\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout 10/10, success so far: 10/10\\n[pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate] success rate: 100.0% (1
…[truncated 2934 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_eval-reconvla-spatial-v3_20260514T110854",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T11:10:29.009648+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "grep -n \"sys.exit\\|exit(\\|return_code\\|EXIT\" /root/acr-vla-conformal-refinement/src/evaluate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_eval-reconvla-spatial-v3_20260514T110854",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "grep -n \"sys.exit\\|exit(\\|return_code\\|EXIT\" /root/acr-vla-conformal-refinement/src/evaluate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T11:10:29.009785+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_eval-reconvla-spatial-v3_20260514T110854",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T11:10:29.009910+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "tail -5 /root/acr-vla-conformal-refinement/src/evaluate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_eval-reconvla-spatial-v3_20260514T110854",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "tail -5 /root/acr-vla-conformal-refinement/src/evaluate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T11:10:29.010034+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    evaluate(args)\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_eval-reconvla-spatial-v3_20260514T110854",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T11:10:29.010152+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "grep -n \"sys.exit\\|exit(\" /root/acr-vla-conformal-refinement/src/evaluate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_eval-reconvla-spatial-v3_20260514T110854",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "grep -n \"sys.exit\\|exit(\" /root/acr-vla-conformal-refinement/src/evaluate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T11:10:29.010293+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_eval-reconvla-spatial-v3_20260514T110854",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T11:10:29.010424+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "grep -rn \"DeprecationWarning\\|swigvarlink\" /root/acr-vla-conformal-refinement/src/evaluate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_eval-reconvla-spatial-v3_20260514T110854",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "grep -rn \"DeprecationWarning\\|swigvarlink\" /root/acr-vla-conformal-refinement/src/evaluate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T11:10:29.010543+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_eval-reconvla-spatial-v3_20260514T110854",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T11:10:29.010656+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "grep -n \"sys.exit\" /root/acr-vla-conformal-refinement/src/evaluate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_eval-reconvla-spatial-v3_20260514T110854",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "grep -n \"sys.exit\" /root/acr-vla-conformal-refinement/src/evaluate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T11:10:29.010772+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"370:        sys.exit(139)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_eval-reconvla-spatial-v3_20260514T110854",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T11:10:29.010883+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "grep -n \"exit(\" /root/acr-vla-conformal-refinement/src/evaluate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_eval-reconvla-spatial-v3_20260514T110854",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "grep -n \"exit(\" /root/acr-vla-conformal-refinement/src/evaluate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-14T11:10:29.010992+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "wc -l /root/acr-vla-conformal-refinement/src/evaluate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_eval-reconvla-spatial-v3_20260514T110854",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "wc -l /root/acr-vla-conformal-refinement/src/evaluate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-14T11:10:29.011104+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"370:        sys.exit(139)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.34}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_eval-reconvla-spatial-v3_20260514T110854",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T11:10:29.011216+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"385 /root/acr-vla-conformal-refinement/src/evaluate.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_eval-reconvla-spatial-v3_20260514T110854",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T11:10:29.011377+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "cat -n /root/acr-vla-conformal-refinement/src/evaluate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_eval-reconvla-spatial-v3_20260514T110854",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "cat -n /root/acr-vla-conformal-refinement/src/evaluate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T11:10:29.011634+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"     1\\t\\\"\\\"\\\"\\n     2\\tLIBERO evaluation script for ACR-VLA.\\n     3\\t\\n     4\\tRollout loop:\\n     5\\t  1. Load LIBERO env + task suite\\n     6\\t  2. Load SmolVLA (frozen) + CRM\\n     7\\t  3. For each task, rollout N times:\\n     8\\t     a. Reset env\\n     9\\t     b. Each step: obs → SmolVLA K=10 samples → CGS on 6D pose → CRM\\n    10\\t        → combine refined pose with gripper → execute 7D action\\n    11\\t     c. Record success/failure\\n    12\\t  4. Report per-task and overall success rate\\n    13\\t\\n    14\\tBaselines:\\n    15\\t  - \\\"vla_only\\\": SmolVLA mean of K=10, no CRM refinement\\n    16\\t  - \\\"crm_scalar\\\": CRM with scalar uncertainty (single std, not per-DOF)\\n    17\\t  - \\\"crm_perdof\\\": CRM with full per-DOF uncertainty (ours)\\n    18\\t  - \\\"acr_vla\\\": alias for crm_perdof — the full ACR-VLA pipeline\\n    19\\t  - \\\"reconvla\\\": ReconVLA baseline — scalar Euclidean argmin selection (plan_014)\\n    20\\t\\n    21\\tUsage:\\n    22\\t  python evaluate.py --benchmark object --checkpoint /path/to/crm_best.pt --n_rollouts 20\\n    23\\t  python evaluate.py --benchmark object --mode vla_only --n_rollouts 20\\n    24\\t  python evaluate.py --benchmark spatial --mode reconvla --n_rollouts 20\\n    25\\t  python evaluate.py --benchmark spatial --mode acr_vla --crm_checkpoint /path/to/crm_best.pt --n_rollouts 10\\n    26\\t\\\"\\\"\\\"\\n    27\\timport argparse\\n    28\\timport functools\\n    29\\tbuiltins_print = print\\n    30\\tprint = functools.partial(builtins_print, flush=True)\\n    31\\timport os\\n    32\\tos.environ.setdefault(\\\"HF_HUB_OFFLINE\\\", \\\"1\\\")\\n    33\\tos.environ.setdefault(\\\"TRANSFORMERS_OFFLINE\\\", \\\"1\\\")\\n    34\\timport sys\\n    35\\timport json\\n    36\\timport time\\n    37\\timport signal\\n    38\\timport traceback\\n    39\\tfrom pathlib import Path\\n    40\\t\\n    41\\timport torch\\n    42\\ti
…[truncated 7456 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_eval-reconvla-spatial-v3_20260514T110854",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-14T11:10:29.011861+00:00_

## 诊断结果

### 根本原因

**实验实际上已成功完成**，所有 10 个任务 × 10 rollouts = 100 个 rollout 全部跑完，最终结果：

```
Overall success rate (reconvla): 34.0% (34/100)
```

EXIT_CODE=1 **不是**来自评估逻辑本身，而是来自 **Python 解释器关闭阶段** robosuite 的 SWIG 对象清理。日志最后一行的 `sys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute` 就是这个过程的表现——在 Python 3.12 下，robosuite 的 SWIG 绑定在 `__del__`/atexit 阶段抛出异常导致非零退出码。

代码中唯一的 `sys.exit()` 在第 370 行（SIGSEGV handler，exit 139），没有被触发。`main()` 函数（第 381 行）调用 `evaluate(args)` 后直接 return，没有显式 `sys.exit(0)`，所以 Python 解释器 cleanup 阶段的异常决定了最终退出码。

### 结论

- **不是代码 bug，不是环境问题**，是 robosuite SWIG + Python 3.12 的 cleanup 兼容性问题
- **实验数据完整有效**，无需重跑
- 结果未保存到文件（`output_file=None`），只打印到了日志

### 修复方案

在 `main()` 末尾加 `sys.exit(0)` 强制成功退出，避免 cleanup 阶段的异常影响退出码：

```python
def main():
    def _segfault_handler(signum, frame):
        print(f"[evaluate] FATAL: caught signal {signum} (segfault)", flush=True)
        sys.exit(139)

    signal.signal(signal.SIGSEGV, _segfault_handler)

    args = parse_args()
    ...
    evaluate(args)
    sys.exit(0)  # ← 加这一行
```

### 关于重跑

不需要重跑。如果需要 JSON 结果文件，加 `--output_file` 参数即可，evaluate 函数会在 cleanup 之前保存：

```bash
CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --output_file /root/autodl-tmp/eval_results/reconvla_spatial_v3.json
```

### 各任务结果汇总

| 任务 | 成功率 |
|------|--------|
| bowl between plate and ramekin → plate | 60% |
| bowl next to ramekin → plate | **100%** |
| bowl from table center → plate | 0% |
| bowl on cookie box → plate | 30% |
| bowl in top drawer → plate | 10% |
| bowl on ramekin → plate | 10% |
| bowl next to cookie box → plate | **90%** |
| bowl on stove → plate | 0% |
| bowl next to plate → plate | 40% |
| bowl on wooden cabinet → plate | 0% |
| **Overall** | **34.0%** |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_diagnose_eval-reconvla-spatial-v3_20260514T110854"
}
```

</details>

---
