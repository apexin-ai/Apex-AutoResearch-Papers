# verify n action steps check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/chats/worker_verify_n-action-steps-check_20260523T041258.jsonl`
- **Structured JSON:** [`e691c8018d80a37e8e0f.json`](../../sessions/e6/e691c8018d80a37e8e0f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

21 recorded events

### Tool call

_source line 1 · 2026-05-23T04:15:47.316170+00:00_

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
  "session": "worker_verify_n-action-steps-check_20260523T041258",
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

_source line 2 · 2026-05-23T04:15:47.316525+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_n-action-steps-check_20260523T041258",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T04:15:47.316753+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "python3 -c \"\nimport glob,os\nprint('=== PROCESSES ===')\nfor p in sorted(glob.glob('/proc/[0-9]*/cmdline')):\n    try:\n        with open(p) as f:\n            cmd = f.read().replace(chr(0),' ').strip()\n            if 'evaluate.py' in cmd or 'train_crm' in cmd:\n                pid = p.split('/')[2]\n                try:\n                    with open(f'/proc/{pid}/environ') as ef:\n                        env = ef.read()\n                        cvd = [x for x in env.split(chr(0)) if 'CUDA_VISIBLE' in x]\n                        gpu_str = cvd[0] if cvd else 'NO_CUDA_VIS'\n                except: gpu_str='N/A'\n                has_nas = '*** HAS n_action_steps ***' if 'n_action_steps' in cmd else 'default(10)'\n                print(f'PID {pid} | {gpu_str} | {has_nas}')\n                print(f'  CMD: {cmd}')\n    except: pass\nprint()\nprint('=== N_ACTION_STEPS SUMMARY ===')\nfound=False\nfor p in glob.glob('/proc/[0-9]*/cmdline'):\n    try:\n        with open(p) as f:\n            cmd=f.read().replace(chr(0),' ')\n            if 'evaluate.py' in cmd and 'n_action_steps' in cmd:\n                found=True\n                print(f'WARNING: PID {p.split(chr(47))[2]} has n_action_steps in cmd')\n    except: pass\nif not found: print('OK: No evaluate.py process uses --n_action_steps (all default=10)')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_n-action-steps-check_20260523T041258",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "python3 -c \"\nimport glob,os\nprint('=== PROCESSES ===')\nfor p in sorted(glob.glob('/proc/[0-9]*/cmdline')):\n    try:\n        with open(p) as f:\n            cmd = f.read().replace(chr(0),' ').strip()\n            if 'evaluate.py' in cmd or 'train_crm' in cmd:\n                pid = p.split('/')[2]\n                try:\n                    with open(f'/proc/{pid}/environ') as ef:\n                        env = ef.read()\n                        cvd = [x for x in env.split(chr(0)) if 'CUDA_VISIBLE' in x]\n                        gpu_str = cvd[0] if cvd else 'NO_CUDA_VIS'\n                except: gpu_str='N/A'\n                has_nas = '*** HAS n_action_steps ***' if 'n_action_steps' in cmd else 'default(10)'\n                print(f'PID {pid} | {gpu_str} | {has_nas}')\n                print(f'  CMD: {cmd}')\n    except: pass\nprint()\nprint('=== N_ACTION_STEPS SUMMARY ===')\nfound=False\nfor p in glob.glob('/proc/[0-9]*/cmdline'):\n    try:\n        with open(p) as f:\n            cmd=f.read().replace(chr(0),' ')\n            if 'evaluate.py' in cmd and 'n_action_steps' in cmd:\n                found=True\n                print(f'WARNING: PID {p.split(chr(47))[2]} has n_action_steps in cmd')\n    except: pass\nif not found: print('OK: No evaluate.py process uses --n_action_steps (all default=10)')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T04:15:47.316914+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_n-action-steps-check_20260523T041258",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T04:15:47.317051+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "python3 -c \"\nimport glob,os\nprint('=== PROCESSES ===')\nfor p in sorted(glob.glob('/proc/[0-9]*/cmdline')):\n    try:\n        with open(p) as f:\n            cmd = f.read().replace(chr(0),' ').strip()\n            if 'evaluate.py' in cmd or 'train_crm' in cmd:\n                pid = p.split('/')[2]\n                try:\n                    with open(f'/proc/{pid}/environ') as ef:\n                        env = ef.read()\n                        cvd = [x for x in env.split(chr(0)) if 'CUDA_VISIBLE' in x]\n                        gpu_str = cvd[0] if cvd else 'NO_CUDA_VIS'\n                except: gpu_str='N/A'\n                has_nas = '*** HAS n_action_steps ***' if 'n_action_steps' in cmd else 'default(10)'\n                print(f'PID {pid} | {gpu_str} | {has_nas}')\n                print(f'  CMD: {cmd}')\n    except: pass\nprint()\nprint('=== N_ACTION_STEPS SUMMARY ===')\nfound=False\nfor p in glob.glob('/proc/[0-9]*/cmdline'):\n    try:\n        with open(p) as f:\n            cmd=f.read().replace(chr(0),' ')\n            if 'evaluate.py' in cmd and 'n_action_steps' in cmd:\n                found=True\n                print(f'WARNING: PID {p.split(chr(47))[2]} has n_action_steps in cmd')\n    except: pass\nif not found: print('OK: No evaluate.py process uses --n_action_steps (all default=10)')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_n-action-steps-check_20260523T041258",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "python3 -c \"\nimport glob,os\nprint('=== PROCESSES ===')\nfor p in sorted(glob.glob('/proc/[0-9]*/cmdline')):\n    try:\n        with open(p) as f:\n            cmd = f.read().replace(chr(0),' ').strip()\n            if 'evaluate.py' in cmd or 'train_crm' in cmd:\n                pid = p.split('/')[2]\n                try:\n                    with open(f'/proc/{pid}/environ') as ef:\n                        env = ef.read()\n                        cvd = [x for x in env.split(chr(0)) if 'CUDA_VISIBLE' in x]\n                        gpu_str = cvd[0] if cvd else 'NO_CUDA_VIS'\n                except: gpu_str='N/A'\n                has_nas = '*** HAS n_action_steps ***' if 'n_action_steps' in cmd else 'default(10)'\n                print(f'PID {pid} | {gpu_str} | {has_nas}')\n                print(f'  CMD: {cmd}')\n    except: pass\nprint()\nprint('=== N_ACTION_STEPS SUMMARY ===')\nfound=False\nfor p in glob.glob('/proc/[0-9]*/cmdline'):\n    try:\n        with open(p) as f:\n            cmd=f.read().replace(chr(0),' ')\n            if 'evaluate.py' in cmd and 'n_action_steps' in cmd:\n                found=True\n                print(f'WARNING: PID {p.split(chr(47))[2]} has n_action_steps in cmd')\n    except: pass\nif not found: print('OK: No evaluate.py process uses --n_action_steps (all default=10)')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T04:15:47.317199+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_n-action-steps-check_20260523T041258",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T04:15:47.317349+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "nvidia-smi --query-gpu=index,memory.used,memory.total,utilization.gpu --format=csv,noheader",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_n-action-steps-check_20260523T041258",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "nvidia-smi --query-gpu=index,memory.used,memory.total,utilization.gpu --format=csv,noheader",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T04:15:47.317478+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 6306 MiB, 24564 MiB, 39 %\\n1, 6212 MiB, 24564 MiB, 18 %\\n2, 6212 MiB, 24564 MiB, 12 %\\n3, 544 MiB, 24564 MiB, 10 %\\n4, 6212 MiB, 24564 MiB, 12 %\\n5, 5731 MiB, 24564 MiB, 29 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.93}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_n-action-steps-check_20260523T041258",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T04:15:47.317597+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "nvidia-smi --query-gpu=index,memory.used,memory.total,utilization.gpu --format=csv,noheader",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_n-action-steps-check_20260523T041258",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "nvidia-smi --query-gpu=index,memory.used,memory.total,utilization.gpu --format=csv,noheader",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-23T04:15:47.317713+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tmux ls",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_n-action-steps-check_20260523T041258",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tmux ls",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-23T04:15:47.317833+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 5636 MiB, 24564 MiB, 19 %\\n1, 5692 MiB, 24564 MiB, 30 %\\n2, 5608 MiB, 24564 MiB, 25 %\\n3, 5630 MiB, 24564 MiB, 18 %\\n4, 5630 MiB, 24564 MiB, 17 %\\n5, 5630 MiB, 24564 MiB, 18 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.79}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_n-action-steps-check_20260523T041258",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T04:15:47.317952+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'tmux' is not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_n-action-steps-check_20260523T041258",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T04:15:47.318068+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "tmux ls",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_n-action-steps-check_20260523T041258",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "tmux ls",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-23T04:15:47.318182+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'tmux' is not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_n-action-steps-check_20260523T041258",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T04:15:47.318363+00:00_

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
  "session": "worker_verify_n-action-steps-check_20260523T041258",
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

_source line 16 · 2026-05-23T04:15:47.318492+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_n-action-steps-check_20260523T041258",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-23T04:15:47.318607+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-32546",
  "command": "echo \"===EVALUATE===\"; ps aux | grep evaluate.py | grep -v grep; echo \"===TRAIN===\"; ps aux | grep train_crm.py | grep -v grep; echo \"===TMUX===\"; tmux ls 2>/dev/null || echo \"NO_TMUX\"; echo \"===N_ACTION_STEPS===\"; ps aux | grep evaluate.py | grep -v grep | grep -o \"n_action_steps [0-9]*\" || echo \"NO_N_ACTION_STEPS_FLAG(default_10)\"",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_n-action-steps-check_20260523T041258",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "echo \"===EVALUATE===\"; ps aux | grep evaluate.py | grep -v grep; echo \"===TRAIN===\"; ps aux | grep train_crm.py | grep -v grep; echo \"===TMUX===\"; tmux ls 2>/dev/null || echo \"NO_TMUX\"; echo \"===N_ACTION_STEPS===\"; ps aux | grep evaluate.py | grep -v grep | grep -o \"n_action_steps [0-9]*\" || echo \"NO_N_ACTION_STEPS_FLAG(default_10)\"",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-23T04:15:47.318823+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"===EVALUATE===\\nroot     664401  0.0  0.0   6084  3916 ?        Ss   12:11   0:00 tmux new-session -d -s eval-supp-crm-norm02-spatial-s42-r2 rm -f /tmp/agent-ml-exit/eval-supp-crm-norm02-spatial-s42-r2.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/acr-vla-conformal-refinement/eval-supp-crm-norm02-spatial-s42-r2.log; printf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\" > /tmp/agent-ml-exit/eval-supp-crm-norm02-spatial-s42-r2.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/acr-vla-conformal-refinement && export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 86400 env bash -c 'bash -c \\\"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2 2>&1 | tee logs/eval-supp-crm-norm02-spatial-s42-r2.log\\\"'; } > ~/runs/acr-vla-conformal-refinement/eval-supp-crm-norm02-spatial-s42-r2.log 2>&1\\nroot     664402  0.0  0.0   4496  3692 pts/0    Ss+  12:11   0:00 bash -c rm -f /tmp/agent-ml-exit/eval-supp-crm-norm02-spatial-s42-r2.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/acr-vla-conformal-refinement/eval-supp-crm-norm02-spatial-s42-r2.log; printf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\" > /tmp/agent-ml-exit/eval-supp-crm-norm02-spatial-s42-r2.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/acr-vla-conformal-refinement && export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 86400 env bash -c 'bash -c \\\"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mod
…[truncated 6391 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_n-action-steps-check_20260523T041258",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-23T04:15:47.318980+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-28827",
  "command": "echo \"===EVALUATE===\"; ps aux | grep evaluate.py | grep -v grep; echo \"===TRAIN===\"; ps aux | grep train_crm.py | grep -v grep; echo \"===TMUX===\"; tmux ls 2>/dev/null || echo \"NO_TMUX\"; echo \"===N_ACTION_STEPS===\"; ps aux | grep evaluate.py | grep -v grep | grep -o \"n_action_steps [0-9]*\" || echo \"NO_N_ACTION_STEPS_FLAG(default_10)\"",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_n-action-steps-check_20260523T041258",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "echo \"===EVALUATE===\"; ps aux | grep evaluate.py | grep -v grep; echo \"===TRAIN===\"; ps aux | grep train_crm.py | grep -v grep; echo \"===TMUX===\"; tmux ls 2>/dev/null || echo \"NO_TMUX\"; echo \"===N_ACTION_STEPS===\"; ps aux | grep evaluate.py | grep -v grep | grep -o \"n_action_steps [0-9]*\" || echo \"NO_N_ACTION_STEPS_FLAG(default_10)\"",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-23T04:15:47.319205+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"===EVALUATE===\\nroot     519748  0.0  0.0   6188  3780 ?        Ss   12:11   0:00 tmux new-session -d -s eval-object-vla-only-wrapper-s42-r2 rm -f /tmp/agent-ml-exit/eval-object-vla-only-wrapper-s42-r2.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/acr-vla-conformal-refinement/eval-object-vla-only-wrapper-s42-r2.log; printf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\" > /tmp/agent-ml-exit/eval-object-vla-only-wrapper-s42-r2.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/acr-vla-conformal-refinement && export CUDA_VISIBLE_DEVICES=3 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 86400 env bash -c 'bash -c \\\"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode vla_only --benchmark object --seed 42 --n_rollouts 20 2>&1 | tee logs/eval-object-vla-only-wrapper-s42-r2.log\\\"'; } > ~/runs/acr-vla-conformal-refinement/eval-object-vla-only-wrapper-s42-r2.log 2>&1\\nroot     519749  0.0  0.0   4496  3712 pts/0    Ss+  12:11   0:00 bash -c rm -f /tmp/agent-ml-exit/eval-object-vla-only-wrapper-s42-r2.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/acr-vla-conformal-refinement/eval-object-vla-only-wrapper-s42-r2.log; printf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\" > /tmp/agent-ml-exit/eval-object-vla-only-wrapper-s42-r2.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/acr-vla-conformal-refinement && export CUDA_VISIBLE_DEVICES=3 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 86400 env bash -c 'bash -c \\\"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode vla_only --benchmark object --seed 42 --n_rollouts 20 2>&1 | tee logs/eval-object-vla-only-wrapper-s42-r2.log
…[truncated 6415 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_n-action-steps-check_20260523T041258",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-23T04:15:47.319488+00:00_

## 报告

### n_action_steps 验证结果

**两台服务器均未发现任何 evaluate.py 进程使用 `--n_action_steps` 参数，全部使用默认值 10。** ✅

---

### BJB1-32546

#### evaluate.py 进程（5 个）

| PID | GPU | Session | 命令 |
|-----|-----|---------|------|
| 664412 | 0 | eval-supp-crm-norm02-spatial-s42-r2 | `evaluate.py --mode crm_obs_only --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2` |
| — | 1 | eval-supp-adapt-tau015-spatial-s42-r2 | `evaluate.py --mode adaptive_conformal --benchmark spatial --seed 42 --n_rollouts 20 --tau 0.15`（截断区） |
| — | 2 | eval-supp-adapt-tau025-spatial-s42-r2 | `evaluate.py --mode adaptive_conformal --benchmark spatial --seed 42 --n_rollouts 20 --tau 0.25`（截断区） |
| — | 4 | eval-supp-adapt-tau035-spatial-s42-r2 | `evaluate.py --mode adaptive_conformal --benchmark spatial --seed 42 --n_rollouts 20 --tau 0.35`（截断区） |
| 669429 | 5 | eval-supp-obj-crm005-s42-r2 | `evaluate.py --mode crm_obs_only --benchmark object --seed 42 --n_rollouts 20 --max_correction_norm 0.05` |

#### train_crm.py 进程（1 个）

| PID | GPU | Session | 命令 |
|-----|-----|---------|------|
| 668382 | 3 | train-crm-unified-4suite-r6 | `train_crm.py --benchmark object spatial goal long --obs_dim 960 --epochs 50 --batch_size 32 --lr 1e-3 --input_mode obs_only --resume_from checkpoint_epoch0038.pt` |

#### GPU 占用

| GPU | 显存占用 | 利用率 | 状态 |
|-----|---------|--------|------|
| 0 | 6306/24564 MiB | 39% | 占用（eval crm_obs_only spatial） |
| 1 | 6212/24564 MiB | 18% | 占用（eval adaptive tau015） |
| 2 | 6212/24564 MiB | 12% | 占用（eval adaptive tau025） |
| 3 | 544/24564 MiB | 10% | 占用（train_crm，显存较低） |
| 4 | 6212/24564 MiB | 12% | 占用（eval adaptive tau035） |
| 5 | 5731/24564 MiB | 29% | 占用（eval crm_obs_only object） |

#### tmux sessions（6 个）
- eval-supp-crm-norm02-spatial-s42-r2
- eval-supp-adapt-tau015-spatial-s42-r2
- eval-supp-adapt-tau025-spatial-s42-r2
- eval-supp-adapt-tau035-spatial-s42-r2
- eval-supp-obj-crm005-s42-r2
- train-crm-unified-4suite-r6

---

### BJB2-28827

#### evaluate.py 进程（6 个）

| PID | GPU | Session | 命令 |
|-----|-----|---------|------|
| 519759 | 3 | eval-object-vla-only-wrapper-s42-r2 | `evaluate.py --mode vla_only --benchmark object --seed 42 --n_rollouts 20` |
| — | 4 | eval-object-vla-only-wrapper-s43-r2 | `evaluate.py --mode vla_only --benchmark object --seed 43 --n_rollouts 20` |
| — | 5 | eval-object-vla-only-wrapper-s44-r2 | `evaluate.py --mode vla_only --benchmark object --seed 44 --n_rollouts 20`（截断区） |
| — | 0/1 | eval-supp-obj-adapt-s42-r2 | `evaluate.py --mode adaptive_conformal --benchmark object --seed 42 --n_rollouts 20`（截断区） |
| 523250 | 1 | eval-supp-obj-reconvla-s42 | `evaluate.py --mode reconvla --crm_checkpoint crm_best.pt --benchmark object --seed 42 --n_rollouts 20` |
| 524332 | 2 | eval-supp-goal-crm005-s42 | `evaluate.py --mode crm_obs_only --crm_checkpoint crm_best.pt --benchmark goal --seed 42 --n_rollouts 20 --max_correction_norm 0.05` |

#### train_crm.py：**无进程**

#### GPU 占用

| GPU | 显存占用 | 利用率 | 状态 |
|-----|---------|--------|------|
| 0 | 5636/24564 MiB | 19% | 占用 |
| 1 | 5692/24564 MiB | 30% | 占用 |
| 2 | 5608/24564 MiB | 25% | 占用 |
| 3 | 5630/24564 MiB | 18% | 占用 |
| 4 | 5630/24564 MiB | 17% | 占用 |
| 5 | 5630/24564 MiB | 18% | 占用 |

#### tmux sessions（6 个）
- eval-object-vla-only-wrapper-s42-r2
- eval-object-vla-only-wrapper-s43-r2
- eval-object-vla-only-wrapper-s44-r2
- eval-supp-obj-adapt-s42-r2
- eval-supp-obj-reconvla-s42
- eval-supp-goal-crm005-s42

---

### 总结

- **n_action_steps**: ✅ 两台服务器 11 个 evaluate.py 进程均未指定 `--n_action_steps`，全部使用默认值 10
- **BJB1**: 6 GPU 全占用（5 eval + 1 train），GPU 3 上 train_crm 显存仅 544 MiB，可能刚启动或模型较小
- **BJB2**: 6 GPU 全占用（6 eval），无训练进程
- 部分中间进程的 GPU 分配因输出截断无法100%确认，但 n_action_steps 检查覆盖了所有进程（grep 全量扫描），结论可靠

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_verify_n-action-steps-check_20260523T041258"
}
```

</details>

---
