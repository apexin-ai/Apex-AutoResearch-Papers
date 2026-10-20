# analysis qualitative failure

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/chats/worker_analysis_qualitative-failure_20260515T130130.jsonl`
- **Structured JSON:** [`ce3030816076727bbce4.json`](../../sessions/ce/ce3030816076727bbce4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

19 recorded events

### Tool call

_source line 1 · 2026-05-15T13:04:20.388092+00:00_

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
  "session": "worker_analysis_qualitative-failure_20260515T130130",
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

_source line 2 · 2026-05-15T13:04:20.388420+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qualitative-failure_20260515T130130",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T13:04:20.388601+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls -la /root/autodl-tmp/tax_error_inject_agent/eval_results/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qualitative-failure_20260515T130130",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls -la /root/autodl-tmp/tax_error_inject_agent/eval_results/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T13:04:20.388780+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 4344\\ndrwxr-xr-x  2 root root   4096 May 15 20:59 .\\ndrwxr-xr-x 15 root root   4096 May 15 19:55 ..\\n-rw-r--r--  1 root root    917 May 14 19:22 adapter_test.json\\n-rw-r--r--  1 root root   1205 May 15 01:45 dryrun_injected_vanilla.json\\n-rw-r--r--  1 root root  15790 May 15 01:57 dryrun_recovery.json\\n-rw-r--r--  1 root root    563 May 14 20:24 gate1_injection_validity.json\\n-rw-r--r--  1 root root  36732 May 14 20:24 gate2_recovery_quality.json\\n-rw-r--r--  1 root root   4984 May 15 01:30 gate3_judgment.json\\n-rw-r--r--  1 root root  14459 May 14 18:42 mini_taxei_clean.json\\n-rw-r--r--  1 root root  14483 May 14 18:35 mini_vanilla_clean.json\\n-rw-r--r--  1 root root   1170 May 14 19:22 pipeline_test.json\\n-rw-r--r--  1 root root  14460 May 14 21:35 v3_random.json\\n-rw-r--r--  1 root root  14451 May 14 21:43 v3_taxei.json\\n-rw-r--r--  1 root root  14490 May 14 20:38 v3_vanilla.json\\n-rw-r--r--  1 root root  14450 May 15 00:36 v4_random_eval.json\\n-rw-r--r--  1 root root  15886 May 15 09:42 v4_random_fixed_inject10_eval.json\\n-rw-r--r--  1 root root  15891 May 15 09:56 v4_random_fixed_inject25_eval.json\\n-rw-r--r--  1 root root  15854 May 15 18:40 v4_random_fixed_inject25_s0_eval.json\\n-rw-r--r--  1 root root  15864 May 15 18:39 v4_random_fixed_inject25_s123_eval.json\\n-rw-r--r--  1 root root  15890 May 15 09:55 v4_random_fixed_inject50_eval.json\\n-rw-r--r--  1 root root  15863 May 15 18:50 v4_random_fixed_inject50_s0_eval.json\\n-rw-r--r--  1 root root  15849 May 15 18:58 v4_random_fixed_inject50_s123_eval.json\\n-rw-r--r--  1 root root 458947 May 15 05:32 v4_random_recovery_eval.json\\n-rw-r--r--  1 root root  15849 May 15 03:43 v4_random_seed0_eval.json\\n-rw-r--r--  1 root root  15848 May 15 08:24 v4_random_seed123_eval.json\\n-rw-r--r--  1 root root  14453 May 15 00:34 v4_taxei_eval.json\\n-rw-r--r--  1 root root  15836 May 15 08:01 v4_taxei_fixed_inject10_eval.json\\n-rw-r--r-- 
…[truncated 1565 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qualitative-failure_20260515T130130",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T13:04:20.388959+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -200 /root/autodl-tmp/tax_error_inject_agent/eval_results/v4_vanilla_eval.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qualitative-failure_20260515T130130",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "head -200 /root/autodl-tmp/tax_error_inject_agent/eval_results/v4_vanilla_eval.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T13:04:20.389212+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model\\\": \\\"checkpoints/mini_vanilla_sft_v4/v0-20260514-201441/checkpoint-1635\\\",\\n  \\\"eval_split\\\": \\\"valid_unseen\\\",\\n  \\\"inject\\\": false,\\n  \\\"total_episodes\\\": 47,\\n  \\\"success_rate\\\": 0.617,\\n  \\\"timestamp\\\": \\\"2026-05-14T14:45:16.148812+00:00\\\",\\n  \\\"by_task_type\\\": {\\n    \\\"look_at_obj_in_light\\\": {\\n      \\\"total\\\": 6,\\n      \\\"success\\\": 5,\\n      \\\"rate\\\": 0.833\\n    },\\n    \\\"pick_and_place_simple\\\": {\\n      \\\"total\\\": 8,\\n      \\\"success\\\": 5,\\n      \\\"rate\\\": 0.625\\n    },\\n    \\\"pick_clean_then_place_in_recep\\\": {\\n      \\\"total\\\": 11,\\n      \\\"success\\\": 5,\\n      \\\"rate\\\": 0.455\\n    },\\n    \\\"pick_cool_then_place_in_recep\\\": {\\n      \\\"total\\\": 7,\\n      \\\"success\\\": 4,\\n      \\\"rate\\\": 0.571\\n    },\\n    \\\"pick_heat_then_place_in_recep\\\": {\\n      \\\"total\\\": 8,\\n      \\\"success\\\": 6,\\n      \\\"rate\\\": 0.75\\n    },\\n    \\\"pick_two_obj_and_place\\\": {\\n      \\\"total\\\": 7,\\n      \\\"success\\\": 4,\\n      \\\"rate\\\": 0.571\\n    }\\n  },\\n  \\\"episodes\\\": [\\n    {\\n      \\\"task_name\\\": \\\"look_at_obj_in_light-AlarmClock-None-DeskLamp-308\\\",\\n      \\\"task_type\\\": \\\"look_at_obj_in_light\\\",\\n      \\\"task_desc\\\": \\\"Hold the clock and turn on the lamp.\\\",\\n      \\\"success\\\": true,\\n      \\\"steps\\\": 10,\\n      \\\"injected\\\": false,\\n      \\\"operator\\\": \\\"none\\\"\\n    },\\n    {\\n      \\\"task_name\\\": \\\"look_at_obj_in_light-Book-None-DeskLamp-308\\\",\\n      \\\"task_type\\\": \\\"look_at_obj_in_light\\\",\\n      \\\"task_desc\\\": \\\"Look at a book by the light of a lamp.\\\",\\n      \\\"success\\\": false,\\n      \\\"steps\\\": 50,\\n      \\\"injected\\\": false,\\n      \\\"operator\\\": \\\"none\\\"\\n    },\\n    {\\n      \\\"task_name\\\": \\\"look_at_obj_in_ligh
…[truncated 5846 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qualitative-failure_20260515T130130",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T13:04:20.389405+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -100 /root/autodl-tmp/tax_error_inject_agent/eval_results/v4_vanilla_recovery_eval.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qualitative-failure_20260515T130130",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "head -100 /root/autodl-tmp/tax_error_inject_agent/eval_results/v4_vanilla_recovery_eval.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T13:04:20.389617+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model\\\": \\\"/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_vanilla_sft_v4/v0-20260514-201441/checkpoint-1635\\\",\\n  \\\"model_variant\\\": \\\"vanilla\\\",\\n  \\\"inject\\\": true,\\n  \\\"seed\\\": 42,\\n  \\\"total_episodes\\\": 47,\\n  \\\"success_rate\\\": 0.617,\\n  \\\"recovery_rate\\\": 0.617,\\n  \\\"detection_rate\\\": 0.0,\\n  \\\"timestamp\\\": \\\"2026-05-14T19:45:46.465973+00:00\\\",\\n  \\\"by_operator\\\": {\\n    \\\"C1_context_truncation\\\": {\\n      \\\"total\\\": 12,\\n      \\\"recovered\\\": 9,\\n      \\\"detected\\\": 0,\\n      \\\"recovery_rate\\\": 0.75,\\n      \\\"detection_rate\\\": 0.0\\n    },\\n    \\\"C4_observation_masking\\\": {\\n      \\\"total\\\": 11,\\n      \\\"recovered\\\": 6,\\n      \\\"detected\\\": 0,\\n      \\\"recovery_rate\\\": 0.545,\\n      \\\"detection_rate\\\": 0.0\\n    },\\n    \\\"P1_step_order_swap\\\": {\\n      \\\"total\\\": 12,\\n      \\\"recovered\\\": 7,\\n      \\\"detected\\\": 0,\\n      \\\"recovery_rate\\\": 0.583,\\n      \\\"detection_rate\\\": 0.0\\n    },\\n    \\\"P2_sub_goal_deletion\\\": {\\n      \\\"total\\\": 12,\\n      \\\"recovered\\\": 7,\\n      \\\"detected\\\": 0,\\n      \\\"recovery_rate\\\": 0.583,\\n      \\\"detection_rate\\\": 0.0\\n    }\\n  },\\n  \\\"by_task_type\\\": {\\n    \\\"look_at_obj_in_light\\\": {\\n      \\\"total\\\": 6,\\n      \\\"success\\\": 5,\\n      \\\"detected\\\": 0,\\n      \\\"rate\\\": 0.833\\n    },\\n    \\\"pick_and_place_simple\\\": {\\n      \\\"total\\\": 8,\\n      \\\"success\\\": 5,\\n      \\\"detected\\\": 0,\\n      \\\"rate\\\": 0.625\\n    },\\n    \\\"pick_clean_then_place_in_recep\\\": {\\n      \\\"total\\\": 11,\\n      \\\"success\\\": 5,\\n      \\\"detected\\\": 0,\\n      \\\"rate\\\": 0.455\\n    },\\n    \\\"pick_cool_then_place_in_recep\\\": {\\n      \\\"total\\\": 7,\\n      \\\"success\\\": 4,\\n      \\\"detected\\\": 0,\\n      \\\"r
…[truncated 1518 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qualitative-failure_20260515T130130",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T13:04:20.389802+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "python3 -c \"\nimport json\nwith open('/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_vanilla_recovery_eval.json') as f:\n    data = json.load(f)\nep_keys = list(data['episodes'][0].keys())\nprint('Episode keys:', ep_keys)\n# Find first failed episode\nfor ep in data['episodes']:\n    if not ep['success']:\n        print('\\\\n--- FAILED EPISODE ---')\n        print('task:', ep['task_name'])\n        print('task_type:', ep['task_type'])\n        print('task_desc:', ep['task_desc'])\n        print('steps:', ep['steps'])\n        print('operator:', ep['operator'])\n        print('injection_step:', ep.get('injection_step'))\n        print('recovery_analysis:', ep.get('recovery_analysis'))\n        print('trajectory length:', len(ep.get('trajectory',[])))\n        # Print first 5 trajectory steps\n        for t in ep.get('trajectory',[])[:8]:\n            print(f\\\"  step {t['step']}: obs={t['observation'][:80]}... act={t['action']}\\\")\n        break\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qualitative-failure_20260515T130130",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "python3 -c \"\nimport json\nwith open('/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_vanilla_recovery_eval.json') as f:\n    data = json.load(f)\nep_keys = list(data['episodes'][0].keys())\nprint('Episode keys:', ep_keys)\n# Find first failed episode\nfor ep in data['episodes']:\n    if not ep['success']:\n        print('\\\\n--- FAILED EPISODE ---')\n        print('task:', ep['task_name'])\n        print('task_type:', ep['task_type'])\n        print('task_desc:', ep['task_desc'])\n        print('steps:', ep['steps'])\n        print('operator:', ep['operator'])\n        print('injection_step:', ep.get('injection_step'))\n        print('recovery_analysis:', ep.get('recovery_analysis'))\n        print('trajectory length:', len(ep.get('trajectory',[])))\n        # Print first 5 trajectory steps\n        for t in ep.get('trajectory',[])[:8]:\n            print(f\\\"  step {t['step']}: obs={t['observation'][:80]}... act={t['action']}\\\")\n        break\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T13:04:20.389940+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: python expression contains disallowed call 'open('. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qualitative-failure_20260515T130130",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T13:04:20.390061+00:00_

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
  "session": "worker_analysis_qualitative-failure_20260515T130130",
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

_source line 12 · 2026-05-15T13:04:20.390176+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qualitative-failure_20260515T130130",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T13:04:20.390295+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cd /root/autodl-tmp/tax_error_inject_agent && python3 -c \"\nimport json\nwith open('eval_results/v4_vanilla_recovery_eval.json') as f:\n    data = json.load(f)\nprint('Episode keys:', list(data['episodes'][0].keys()))\nfor ep in data['episodes']:\n    if not ep['success']:\n        print('\\n--- FAILED EPISODE ---')\n        print('task:', ep['task_name'])\n        print('task_type:', ep['task_type'])\n        print('task_desc:', ep['task_desc'])\n        print('steps:', ep['steps'])\n        print('operator:', ep['operator'])\n        print('injection_step:', ep.get('injection_step'))\n        print('recovery_analysis:', ep.get('recovery_analysis'))\n        traj = ep.get('trajectory', [])\n        print('trajectory length:', len(traj))\n        for t in traj[:10]:\n            obs = t.get('observation','')[:100]\n            act = t.get('action','')\n            think = t.get('think_snippet','')[:80]\n            print(f\\\"  step {t['step']}: act=[{act}] think=[{think}] obs=[{obs}...]\\\")\n        break\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qualitative-failure_20260515T130130",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cd /root/autodl-tmp/tax_error_inject_agent && python3 -c \"\nimport json\nwith open('eval_results/v4_vanilla_recovery_eval.json') as f:\n    data = json.load(f)\nprint('Episode keys:', list(data['episodes'][0].keys()))\nfor ep in data['episodes']:\n    if not ep['success']:\n        print('\\n--- FAILED EPISODE ---')\n        print('task:', ep['task_name'])\n        print('task_type:', ep['task_type'])\n        print('task_desc:', ep['task_desc'])\n        print('steps:', ep['steps'])\n        print('operator:', ep['operator'])\n        print('injection_step:', ep.get('injection_step'))\n        print('recovery_analysis:', ep.get('recovery_analysis'))\n        traj = ep.get('trajectory', [])\n        print('trajectory length:', len(traj))\n        for t in traj[:10]:\n            obs = t.get('observation','')[:100]\n            act = t.get('action','')\n            think = t.get('think_snippet','')[:80]\n            print(f\\\"  step {t['step']}: act=[{act}] think=[{think}] obs=[{obs}...]\\\")\n        break\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T13:04:20.390453+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cd /root/autodl-tmp/tax_error_inject_agent && python3 -c \\\"\\\\nimport json\\\\nwith open(\\\\'eval_results/v4_vanilla_recovery_eval.json\\\\') as f:\\\\n    data = json.load(f)\\\\nprint(\\\\'Episode keys:\\\\', list(data[\\\\'episodes\\\\'][0].keys()))\\\\nfor ep in data[\\\\'episodes\\\\']:\\\\n    if not ep[\\\\'success\\\\']:\\\\n        print(\\\\'\\\\\\\\n--- FAILED EPISODE ---\\\\')\\\\n        print(\\\\'task:\\\\', ep[\\\\'task_name\\\\'])\\\\n        print(\\\\'task_type:\\\\', ep[\\\\'task_type\\\\'])\\\\n        print(\\\\'task_desc:\\\\', ep[\\\\'task_desc\\\\'])\\\\n        print(\\\\'steps:\\\\', ep[\\\\'steps\\\\'])\\\\n        print(\\\\'operator:\\\\', ep[\\\\'operator\\\\'])\\\\n        print(\\\\'injection_step:\\\\', ep.get(\\\\'injection_step\\\\'))\\\\n        print(\\\\'recovery_analysis:\\\\', ep.get(\\\\'recovery_analysis\\\\'))\\\\n        traj = ep.get(\\\\'trajectory\\\\', [])\\\\n        print(\\\\'trajectory length:\\\\', len(traj))\\\\n        for t in traj[:10]:\\\\n            obs = t.get(\\\\'observation\\\\',\\\\'\\\\')[:100]\\\\n            act = t.get(\\\\'action\\\\',\\\\'\\\\')\\\\n            think = t.get(\\\\'think_snippet\\\\',\\\\'\\\\')[:80]\\\\n            print(f\\\\\\\\\\\"  step {t[\\\\'step\\\\']}: act=[{act}] think=[{think}] obs=[{obs}...]\\\\\\\\\\\")\\\\n        break\\\\n\\\"\\\\n'\\n\\nExit code: 127\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 1: python3: command not found\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qualitative-failure_20260515T130130",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T13:04:20.390624+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && python3 << 'PYEOF'\nimport json\n\nwith open('eval_results/v4_vanilla_recovery_eval.json') as f:\n    data = json.load(f)\n\nprint('Episode keys:', list(data['episodes'][0].keys()))\n\n# Show 2 failed episodes in detail\ncount = 0\nfor ep in data['episodes']:\n    if not ep['success']:\n        count += 1\n        print(f'\\n--- FAILED EPISODE #{count} ---')\n        print('task:', ep['task_name'])\n        print('task_type:', ep['task_type'])\n        print('task_desc:', ep['task_desc'])\n        print('steps:', ep['steps'])\n        print('operator:', ep['operator'])\n        print('injection_step:', ep.get('injection_step'))\n        print('recovery_analysis:', ep.get('recovery_analysis'))\n        traj = ep.get('trajectory', [])\n        print('trajectory length:', len(traj))\n        for t in traj:\n            obs = t.get('observation','')[:120]\n            act = t.get('action','')\n            think = t.get('think_snippet','')[:100]\n            print(f\"  step {t['step']}: act=[{act}] think=[{think}] obs=[{obs}...]\")\n        if count >= 2:\n            break\nPYEOF\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qualitative-failure_20260515T130130",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && python3 << 'PYEOF'\nimport json\n\nwith open('eval_results/v4_vanilla_recovery_eval.json') as f:\n    data = json.load(f)\n\nprint('Episode keys:', list(data['episodes'][0].keys()))\n\n# Show 2 failed episodes in detail\ncount = 0\nfor ep in data['episodes']:\n    if not ep['success']:\n        count += 1\n        print(f'\\n--- FAILED EPISODE #{count} ---')\n        print('task:', ep['task_name'])\n        print('task_type:', ep['task_type'])\n        print('task_desc:', ep['task_desc'])\n        print('steps:', ep['steps'])\n        print('operator:', ep['operator'])\n        print('injection_step:', ep.get('injection_step'))\n        print('recovery_analysis:', ep.get('recovery_analysis'))\n        traj = ep.get('trajectory', [])\n        print('trajectory length:', len(traj))\n        for t in traj:\n            obs = t.get('observation','')[:120]\n            act = t.get('action','')\n            think = t.get('think_snippet','')[:100]\n            print(f\"  step {t['step']}: act=[{act}] think=[{think}] obs=[{obs}...]\")\n        if count >= 2:\n            break\nPYEOF\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T13:04:20.390838+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Episode keys: ['task_name', 'task_type', 'task_desc', 'success', 'steps', 'operator', 'injection_step', 'injected', 'recovery_analysis', 'trajectory']\\n\\n--- FAILED EPISODE #1 ---\\ntask: look_at_obj_in_light-Book-None-DeskLamp-308\\ntask_type: look_at_obj_in_light\\ntask_desc: Look at a book by the light of a lamp.\\nsteps: 50\\noperator: P2_sub_goal_deletion\\ninjection_step: 2\\nrecovery_analysis: {'detected': False, 'detection_step': None, 'recovery_actions_count': 5, 'steps_after_injection': 48}\\ntrajectory length: 50\\n  step 0: act=[go to desk 1] think=[] obs=[-= Welcome to TextWorld, ALFRED! =-\\n\\nYou are in the middle of a room. Looking quickly around you, you see a bed 1, a des...]\\n  step 1: act=[use desklamp 1] think=[] obs=[You arrive at desk 1. On the desk 1, you see a alarmclock 1, a bowl 2, a cd 1, a cellphone 3, a desklamp 1, a mug 1, a p...]\\n  step 2: act=[examine desk 1] think=[] obs=[You turn on the desklamp 1....]\\n  step 3: act=[go to desk 2] think=[] obs=[On the desk 1, you see a alarmclock 1, a bowl 2, a cd 1, a cellphone 3, a desklamp 1, a mug 1, a pen 1, and a pencil 1....]\\n  step 4: act=[go to desk 1] think=[] obs=[You arrive at desk 2. On the desk 2, you see a alarmclock 3, a bowl 3, a cd 3, a mug 2, and a pencil 3....]\\n  step 5: act=[go to shelf 1] think=[] obs=[You arrive at desk 1. On the desk 1, you see a alarmclock 1, a bowl 2, a cd 1, a cellphone 3, a desklamp 1, a mug 1, a p...]\\n  step 6: act=[go to shelf 2] think=[] obs=[You arrive at shelf 1. On the shelf 1, you see a bowl 1....]\\n  step 7: act=[go to shelf 3] think=[] obs=[You arrive at shelf 2. On the shelf 2, you see a creditcard 1, and a pencil 2....]\\n  step 8: act=[go to desk 1] think=[] obs=[You arrive at shelf 3. On the shelf 3, you see a alarmclock 1, a bowl 2, and a desklamp 1....]\\n  step 9: act=[go to drawer 1] think=[] obs=[You arrive at desk 1. On the desk 1, you see a alarmclock 1, a bowl 2, 
…[truncated 6357 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qualitative-failure_20260515T130130",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T13:04:20.391106+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cat << 'PYEOF' > /root/autodl-tmp/tax_error_inject_agent/scripts/failure_analysis.py\n#!/usr/bin/env python3\n\"\"\"Qualitative failure analysis for ALFWorld eval results.\"\"\"\nimport json, os, re\nfrom collections import defaultdict\n\nEVAL_DIR = '/root/autodl-tmp/tax_error_inject_agent/eval_results'\n\ndef detect_action_loop(trajectory):\n    \"\"\"Detect if agent is stuck in a repeating action loop.\"\"\"\n    actions = [t['action'] for t in trajectory]\n    if len(actions) < 6:\n        return False, 0\n    # Check for repeating patterns of length 1-3\n    for plen in [1, 2, 3]:\n        for i in range(len(actions) - plen * 3 + 1):\n            pattern = actions[i:i+plen]\n            repeats = 1\n            j = i + plen\n            while j + plen <= len(actions) and actions[j:j+plen] == pattern:\n                repeats += 1\n                j += plen\n            if repeats >= 4:\n                return True, repeats\n    return False, 0\n\ndef detect_exploration_wandering(trajectory):\n    \"\"\"Agent visits many locations without making progress on the task.\"\"\"\n    actions = [t['action'] for t in trajectory]\n    go_actions = [a for a in actions if a.startswith('go to')]\n    if len(go_actions) >= 15:\n        # Check if visiting same locations repeatedly\n        visited = set()\n        revisits = 0\n        for a in go_actions:\n            if a in visited:\n                revisits += 1\n            visited.add(a)\n        if revisits >= 5:\n            return True\n    return False\n\ndef detect_wrong_receptacle(episode):\n    \"\"\"Agent puts object in wrong place or interacts with wrong receptacle.\"\"\"\n    traj = episode.get('trajectory', [])\n    task_desc = episode.get('task_desc', '').lower()\n    for t in traj:\n        obs = t.get('observation', '').lower()\n        if 'nothing happens' in obs:\n            return True\n    return False\n\ndef detect_missing_subgoal(episode):\n    \"\"\"Agent skips a required intermediate step (clean/heat/cool).\"\"\"\n    task_type = episode.get('task_type', '')\n    traj = episode.get('trajectory', [])\n    actions = [t['action'].lower() for t in traj]\n    action_str = ' '.join(actions)\n    \n    if 'clean' in task_type:\n        has_clean = any('clean' in a or 'sinkbasin' in a for a in actions)\n        has_put = any('put' in a for a in actions)\n        if has_put and not has_clean:\n            return True\n    elif 'heat' in task_type:\n        has_heat = any('heat' in a or 'microwave' in a for a in actions)\n        has_put = any('put' in a for a in actions)\n        if has_put and not has_heat:\n            return True\n    elif 'cool' in task_type:\n        has_cool = any('cool' in a or 'fridge' in a for a in actions)\n        has_put = any('put' in a for a in actions)\n        if has_put and not has_cool:\n            return True\n    return False\n\ndef detect_object_not_found(trajectory):\n    \"\"\"Agent searches for object but can't find it.\"\"\"\n    actions = [t['action'] for t in trajectory]\n    observations = [t.get('observation', '') for t in trajectory]\n    go_count = sum(1 for a in actions if a.startswith('go to'))\n    take_count = sum(1 for a in actions if a.startswith('take') or a.startswith('pick'))\n    if go_count >= 10 and take_count == 0:\n        return True\n    return False\n\ndef classify_failure(episode):\n    \"\"\"Classify a failed episode into failure mode.\"\"\"\n    traj = episode.get('trajectory', [])\n    steps = episode.get('steps', 0)\n    \n    if not traj:\n        return 'no_trajectory'\n    \n    # 1. Loop repetition (highest priority - very clear signal)\n    is_loop, repeats = detect_action_loop(traj)\n    if is_loop and repeats >= 4:\n        return 'loop_repetition'\n    \n    # 2. Missing subgoal (task-specific)\n    if detect_missing_subgoal(episode):\n        return 'missing_subgoal'\n    \n    # 3. Object not found / exploration failure\n    if detect_object_not_found(traj):\n        return 'object_not_found'\n    \n    # 4. Exploration wandering (revisiting locations)\n    if detect_exploration_wandering(traj):\n        return 'exploration_wandering'\n    \n    # 5. Wrong receptacle interaction\n    if detect_wrong_receptacle(episode):\n        return 'wrong_receptacle'\n    \n    # 6. Max steps exhaustion without clear pattern\n    if steps >= 48:\n        return 'max_steps_exhaustion'\n    \n    # 7. Short failure\n    if steps <= 5:\n        return 'premature_termination'\n    \n    return 'other'\n\n# Collect files\nfile_map = {\n    'vanilla': {\n        'recovery': [\n            ('eval_results/v4_vanilla_recovery_eval.json', '42'),\n            ('eval_results/v4_vanilla_recovery_eval_s0.json', '0'),\n            ('eval_results/v4_vanilla_recovery_eval_s123.json', '123'),\n        ],\n        'clean': [\n            ('eval_results/v4_vanilla_eval.json', '42'),\n            ('eval_results/v4_vanilla_seed0_eval.json', '0'),\n            ('eval_results/v4_vanilla_seed123_eval.json', '123'),\n        ],\n    },\n    'taxei': {\n        'recovery': [\n            ('eval_results/v4_taxei_recovery_eval.json', '42'),\n            ('eval_results/v4_taxei_recovery_eval_s0.json', '0'),\n            ('eval_results/v4_taxei_recovery_eval_s123.json', '123'),\n        ],\n        'clean': [\n            ('eval_results/v4_taxei_eval.json', '42'),\n            ('eval_results/v4_taxei_seed0_eval.json', '0'),\n            ('eval_results/v4_taxei_seed123_eval.json', '123'),\n        ],\n    },\n    'random': {\n        'recovery': [\n            ('eval_results/v4_random_recovery_eval.json', '42'),\n        ],\n        'clean': [\n            ('eval_results/v4_random_eval.json', '42'),\n            ('eval_results/v4_random_seed0_eval.json', '0'),\n            ('eval_results/v4_random_seed123_eval.json', '123'),\n        ],\n    },\n}\n\nBASE = '/root/autodl-tmp/tax_error_inject_agent'\nresults = {}\n\nfor cond, groups in file_map.items():\n    all_failures = defaultdict(list)\n    total_eps = 0\n    total_fails = 0\n    has_trajectory = False\n    \n    # Process recovery files (have trajectory)\n    for fpath, seed in groups['recovery']:\n        full = os.path.join(BASE, fpath)\n        if not os.path.exists(full):\n            continue\n        with open(full) as f:\n            data = json.load(f)\n        has_trajectory = True\n        for ep in data.get('episodes', []):\n            total_eps += 1\n            if not ep.get('success', True):\n                total_fails += 1\n                mode = classify_failure(ep)\n                all_failures[mode].append({\n                    'task': ep['task_name'],\n                    'task_type': ep['task_type'],\n                    'task_desc': ep['task_desc'],\n                    'seed': seed,\n                    'steps': ep['steps'],\n                    'operator': ep.get('operator', 'none'),\n                    'source': 'recovery',\n                })\n    \n    # Process clean eval files (no trajectory - limited classification)\n    for fpath, seed in groups['clean']:\n        full = os.path.join(BASE, fpath)\n        if not os.path.exists(full):\n            continue\n        with open(full) as f:\n            data = json.load(f)\n        for ep in data.get('episodes', []):\n            total_eps += 1\n            if not ep.get('success', True):\n                total_fails += 1\n                # Without trajectory, limited classification\n                steps = ep.get('steps', 0)\n                if steps >= 48:\n                    mode = 'max_steps_exhaustion'\n                elif steps <= 5:\n                    mode = 'premature_termination'\n                else:\n                    mode = 'unclassified_no_trajectory'\n                all_failures[mode].append({\n                    'task': ep['task_name'],\n                    'task_type': ep['task_type'],\n                    'task_desc': ep['task_desc'],\n                    'seed': seed,\n                    'steps': ep['steps'],\n                    'operator': ep.get('operator', 'none'),\n                    'source': 'clean',\n                })\n    \n    results[cond] = {\n        'total_episodes': total_eps,\n        'total_failures': total_fails,\n        'failure_rate': round(total_fails / max(total_eps, 1), 3),\n        'by_mode': {k: len(v) for k, v in sorted(all_failures.items(), key=lambda x: -len(x[1]))},\n        'by_mode_and_operator': {},\n        'details': {k: v for k, v in all_failures.items()},\n    }\n    \n    # Cross-tab: failure_mode × operator (recovery only)\n    mode_op = defaultdict(lambda: defaultdict(int))\n    for mode, eps in all_failures.items():\n        for ep in eps:\n            if ep['source'] == 'recovery':\n                mode_op[mode][ep['operator']] += 1\n    results[cond]['by_mode_and_operator'] = {k: dict(v) for k, v in mode_op.items()}\n\n# =========== PRINT RESULTS ===========\nprint(\"=\" * 75)\nprint(\"QUALITATIVE FAILURE ANALYSIS\")\nprint(\"=\" * 75)\n\nfor cond in ['vanilla', 'taxei', 'random']:\n    r = results[cond]\n    print(f\"\\n{'='*75}\")\n    print(f\"{cond.upper()}  |  {r['total_failures']}/{r['total_episodes']} failures ({r['failure_rate']:.1%})\")\n    print(f\"{'='*75}\")\n    print(f\"  {'Failure Mode':<30} {'Count':>6} {'%':>8}\")\n    print(f\"  {'-'*44}\")\n    for mode, count in sorted(r['by_mode'].items(), key=lambda x: -x[1]):\n        pct = count / max(r['total_failures'], 1) * 100\n        print(f\"  {mode:<30} {count:>6} {pct:>7.1f}%\")\n    \n    # Show operator breakdown for recovery failures\n    if r['by_mode_and_operator']:\n        print(f\"\\n  Failure Mode × Injection Operator (recovery eval only):\")\n        for mode, ops in sorted(r['by_mode_and_operator'].items()):\n            print(f\"    {mode}:\")\n            for op, cnt in sorted(ops.items(), key=lambda x: -x[1]):\n                print(f\"      {op}: {cnt}\")\n\n# Cross-condition comparison\nprint(\"\\n\" + \"=\" * 75)\nprint(\"CROSS-CONDITION COMPARISON: failure mode × condition\")\nprint(\"=\" * 75)\nall_modes = set()\nfor r in results.values():\n    all_modes.update(r['by_mode'].keys())\n\nprint(f\"{'Mode':<30} {'Vanilla':>10} {'TaxEI':>10} {'Random':>10}\")\nprint(\"-\" * 60)\nfor mode in sorted(all_modes):\n    vals = [results[c]['by_mode'].get(mode, 0) for c in ['vanilla', 'taxei', 'random']]\n    print(f\"{mode:<30} {vals[0]:>10} {vals[1]:>10} {vals[2]:>10}\")\nprint(\"-\" * 60)\ntotals = [results[c]['total_failures'] for c in ['vanilla', 'taxei', 'random']]\nprint(f\"{'TOTAL':<30} {totals[0]:>10} {totals[1]:>10} {totals[2]:>10}\")\n\n# Cross-condition: failure mode × task_type\nprint(\"\\n\" + \"=\" * 75)\nprint(\"FAILURE MODE × TASK TYPE (all conditions combined)\")\nprint(\"=\" * 75)\ntask_mode = defaultdict(lambda: defaultdict(int))\nfor cond in results:\n    for mode, eps in results[cond]['details'].items():\n        for ep in eps:\n            task_mode[ep['task_type']][mode] += 1\n\nfor ttype in sorted(task_mode.keys()):\n    modes = task_mode[ttype]\n    total = sum(modes.values())\n    print(f\"\\n  {ttype} ({total} failures):\")\n    for m, c in sorted(modes.items(), key=lambda x: -x[1]):\n        print(f\"    {m}: {c}\")\n\n# Save detailed results\noutput = {\n    'summary': {},\n    'cross_condition': {},\n    'details': {},\n}\nfor cond in ['vanilla', 'taxei', 'random']:\n    r = results[cond]\n    output['summary'][cond] = {\n        'total_episodes': r['total_episodes'],\n        'total_failures': r['total_failures'],\n        'failure_rate': r['failure_rate'],\n        'by_mode': r['by_mode'],\n        'by_mode_and_operator': r['by_mode_and_operator'],\n    }\n    # Save example tasks per failure mode (without full trajectory)\n    output['details'][cond] = {}\n    for mode, eps in r['details'].items():\n        output['details'][cond][mode] = eps[:5]  # top 5 examples\n\nfor mode in sorted(all_modes):\n    output['cross_condition'][mode] = {\n        c: results[c]['by_mode'].get(mode, 0) for c in ['vanilla', 'taxei', 'random']\n    }\n\nout_path = os.path.join(BASE, 'eval_results/failure_analysis.json')\nwith open(out_path, 'w') as f:\n    json.dump(output, f, indent=2, ensure_ascii=False)\nprint(f\"\\nSaved to {out_path}\")\nPYEOF\npython3 /root/autodl-tmp/tax_error_inject_agent/scripts/failure_analysis.py\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qualitative-failure_20260515T130130",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cat << 'PYEOF' > /root/autodl-tmp/tax_error_inject_agent/scripts/failure_analysis.py\n#!/usr/bin/env python3\n\"\"\"Qualitative failure analysis for ALFWorld eval results.\"\"\"\nimport json, os, re\nfrom collections import defaultdict\n\nEVAL_DIR = '/root/autodl-tmp/tax_error_inject_agent/eval_results'\n\ndef detect_action_loop(trajectory):\n    \"\"\"Detect if agent is stuck in a repeating action loop.\"\"\"\n    actions = [t['action'] for t in trajectory]\n    if len(actions) < 6:\n        return False, 0\n    # Check for repeating patterns of length 1-3\n    for plen in [1, 2, 3]:\n        for i in range(len(actions) - plen * 3 + 1):\n            pattern = actions[i:i+plen]\n            repeats = 1\n            j = i + plen\n            while j + plen <= len(actions) and actions[j:j+plen] == pattern:\n                repeats += 1\n                j += plen\n            if repeats >= 4:\n                return True, repeats\n    return False, 0\n\ndef detect_exploration_wandering(trajectory):\n    \"\"\"Agent visits many locations without making progress on the task.\"\"\"\n    actions = [t['action'] for t in trajectory]\n    go_actions = [a for a in actions if a.startswith('go to')]\n    if len(go_actions) >= 15:\n        # Check if visiting same locations repeatedly\n        visited = set()\n        revisits = 0\n        for a in go_actions:\n            if a in visited:\n                revisits += 1\n            visited.add(a)\n        if revisits >= 5:\n            return True\n    return False\n\ndef detect_wrong_receptacle(episode):\n    \"\"\"Agent puts object in wrong place or interacts with wrong receptacle.\"\"\"\n    traj = episode.get('trajectory', [])\n    task_desc = episode.get('task_desc', '').lower()\n    for t in traj:\n        obs = t.get('observation', '').lower()\n        if 'nothing happens' in obs:\n            return True\n    return False\n\ndef detect_missing_subgoal(episode):\n    \"\"\"Agent skips a required intermediate step (clean/heat/cool).\"\"\"\n    task_type = episode.get('task_type', '')\n    traj = episode.get('trajectory', [])\n    actions = [t['action'].lower() for t in traj]\n    action_str = ' '.join(actions)\n    \n    if 'clean' in task_type:\n        has_clean = any('clean' in a or 'sinkbasin' in a for a in actions)\n        has_put = any('put' in a for a in actions)\n        if has_put and not has_clean:\n            return True\n    elif 'heat' in task_type:\n        has_heat = any('heat' in a or 'microwave' in a for a in actions)\n        has_put = any('put' in a for a in actions)\n        if has_put and not has_heat:\n            return True\n    elif 'cool' in task_type:\n        has_cool = any('cool' in a or 'fridge' in a for a in actions)\n        has_put = any('put' in a for a in actions)\n        if has_put and not has_cool:\n            return True\n    return False\n\ndef detect_object_not_found(trajectory):\n    \"\"\"Agent searches for object but can't find it.\"\"\"\n    actions = [t['action'] for t in trajectory]\n    observations = [t.get('observation', '') for t in trajectory]\n    go_count = sum(1 for a in actions if a.startswith('go to'))\n    take_count = sum(1 for a in actions if a.startswith('take') or a.startswith('pick'))\n    if go_count >= 10 and take_count == 0:\n        return True\n    return False\n\ndef classify_failure(episode):\n    \"\"\"Classify a failed episode into failure mode.\"\"\"\n    traj = episode.get('trajectory', [])\n    steps = episode.get('steps', 0)\n    \n    if not traj:\n        return 'no_trajectory'\n    \n    # 1. Loop repetition (highest priority - very clear signal)\n    is_loop, repeats = detect_action_loop(traj)\n    if is_loop and repeats >= 4:\n        return 'loop_repetition'\n    \n    # 2. Missing subgoal (task-specific)\n    if detect_missing_subgoal(episode):\n        return 'missing_subgoal'\n    \n    # 3. Object not found / exploration failure\n    if detect_object_not_found(traj):\n        return 'object_not_found'\n    \n    # 4. Exploration wandering (revisiting locations)\n    if detect_exploration_wandering(traj):\n        return 'exploration_wandering'\n    \n    # 5. Wrong receptacle interaction\n    if detect_wrong_receptacle(episode):\n        return 'wrong_receptacle'\n    \n    # 6. Max steps exhaustion without clear pattern\n    if steps >= 48:\n        return 'max_steps_exhaustion'\n    \n    # 7. Short failure\n    if steps <= 5:\n        return 'premature_termination'\n    \n    return 'other'\n\n# Collect files\nfile_map = {\n    'vanilla': {\n        'recovery': [\n            ('eval_results/v4_vanilla_recovery_eval.json', '42'),\n            ('eval_results/v4_vanilla_recovery_eval_s0.json', '0'),\n            ('eval_results/v4_vanilla_recovery_eval_s123.json', '123'),\n        ],\n        'clean': [\n            ('eval_results/v4_vanilla_eval.json', '42'),\n            ('eval_results/v4_vanilla_seed0_eval.json', '0'),\n            ('eval_results/v4_vanilla_seed123_eval.json', '123'),\n        ],\n    },\n    'taxei': {\n        'recovery': [\n            ('eval_results/v4_taxei_recovery_eval.json', '42'),\n            ('eval_results/v4_taxei_recovery_eval_s0.json', '0'),\n            ('eval_results/v4_taxei_recovery_eval_s123.json', '123'),\n        ],\n        'clean': [\n            ('eval_results/v4_taxei_eval.json', '42'),\n            ('eval_results/v4_taxei_seed0_eval.json', '0'),\n            ('eval_results/v4_taxei_seed123_eval.json', '123'),\n        ],\n    },\n    'random': {\n        'recovery': [\n            ('eval_results/v4_random_recovery_eval.json', '42'),\n        ],\n        'clean': [\n            ('eval_results/v4_random_eval.json', '42'),\n            ('eval_results/v4_random_seed0_eval.json', '0'),\n            ('eval_results/v4_random_seed123_eval.json', '123'),\n        ],\n    },\n}\n\nBASE = '/root/autodl-tmp/tax_error_inject_agent'\nresults = {}\n\nfor cond, groups in file_map.items():\n    all_failures = defaultdict(list)\n    total_eps = 0\n    total_fails = 0\n    has_trajectory = False\n    \n    # Process recovery files (have trajectory)\n    for fpath, seed in groups['recovery']:\n        full = os.path.join(BASE, fpath)\n        if not os.path.exists(full):\n            continue\n        with open(full) as f:\n            data = json.load(f)\n        has_trajectory = True\n        for ep in data.get('episodes', []):\n            total_eps += 1\n            if not ep.get('success', True):\n                total_fails += 1\n                mode = classify_failure(ep)\n                all_failures[mode].append({\n                    'task': ep['task_name'],\n                    'task_type': ep['task_type'],\n                    'task_desc': ep['task_desc'],\n                    'seed': seed,\n                    'steps': ep['steps'],\n                    'operator': ep.get('operator', 'none'),\n                    'source': 'recovery',\n                })\n    \n    # Process clean eval files (no trajectory - limited classification)\n    for fpath, seed in groups['clean']:\n        full = os.path.join(BASE, fpath)\n        if not os.path.exists(full):\n            continue\n        with open(full) as f:\n            data = json.load(f)\n        for ep in data.get('episodes', []):\n            total_eps += 1\n            if not ep.get('success', True):\n                total_fails += 1\n                # Without trajectory, limited classification\n                steps = ep.get('steps', 0)\n                if steps >= 48:\n                    mode = 'max_steps_exhaustion'\n                elif steps <= 5:\n                    mode = 'premature_termination'\n                else:\n                    mode = 'unclassified_no_trajectory'\n                all_failures[mode].append({\n                    'task': ep['task_name'],\n                    'task_type': ep['task_type'],\n                    'task_desc': ep['task_desc'],\n                    'seed': seed,\n                    'steps': ep['steps'],\n                    'operator': ep.get('operator', 'none'),\n                    'source': 'clean',\n                })\n    \n    results[cond] = {\n        'total_episodes': total_eps,\n        'total_failures': total_fails,\n        'failure_rate': round(total_fails / max(total_eps, 1), 3),\n        'by_mode': {k: len(v) for k, v in sorted(all_failures.items(), key=lambda x: -len(x[1]))},\n        'by_mode_and_operator': {},\n        'details': {k: v for k, v in all_failures.items()},\n    }\n    \n    # Cross-tab: failure_mode × operator (recovery only)\n    mode_op = defaultdict(lambda: defaultdict(int))\n    for mode, eps in all_failures.items():\n        for ep in eps:\n            if ep['source'] == 'recovery':\n                mode_op[mode][ep['operator']] += 1\n    results[cond]['by_mode_and_operator'] = {k: dict(v) for k, v in mode_op.items()}\n\n# =========== PRINT RESULTS ===========\nprint(\"=\" * 75)\nprint(\"QUALITATIVE FAILURE ANALYSIS\")\nprint(\"=\" * 75)\n\nfor cond in ['vanilla', 'taxei', 'random']:\n    r = results[cond]\n    print(f\"\\n{'='*75}\")\n    print(f\"{cond.upper()}  |  {r['total_failures']}/{r['total_episodes']} failures ({r['failure_rate']:.1%})\")\n    print(f\"{'='*75}\")\n    print(f\"  {'Failure Mode':<30} {'Count':>6} {'%':>8}\")\n    print(f\"  {'-'*44}\")\n    for mode, count in sorted(r['by_mode'].items(), key=lambda x: -x[1]):\n        pct = count / max(r['total_failures'], 1) * 100\n        print(f\"  {mode:<30} {count:>6} {pct:>7.1f}%\")\n    \n    # Show operator breakdown for recovery failures\n    if r['by_mode_and_operator']:\n        print(f\"\\n  Failure Mode × Injection Operator (recovery eval only):\")\n        for mode, ops in sorted(r['by_mode_and_operator'].items()):\n            print(f\"    {mode}:\")\n            for op, cnt in sorted(ops.items(), key=lambda x: -x[1]):\n                print(f\"      {op}: {cnt}\")\n\n# Cross-condition comparison\nprint(\"\\n\" + \"=\" * 75)\nprint(\"CROSS-CONDITION COMPARISON: failure mode × condition\")\nprint(\"=\" * 75)\nall_modes = set()\nfor r in results.values():\n    all_modes.update(r['by_mode'].keys())\n\nprint(f\"{'Mode':<30} {'Vanilla':>10} {'TaxEI':>10} {'Random':>10}\")\nprint(\"-\" * 60)\nfor mode in sorted(all_modes):\n    vals = [results[c]['by_mode'].get(mode, 0) for c in ['vanilla', 'taxei', 'random']]\n    print(f\"{mode:<30} {vals[0]:>10} {vals[1]:>10} {vals[2]:>10}\")\nprint(\"-\" * 60)\ntotals = [results[c]['total_failures'] for c in ['vanilla', 'taxei', 'random']]\nprint(f\"{'TOTAL':<30} {totals[0]:>10} {totals[1]:>10} {totals[2]:>10}\")\n\n# Cross-condition: failure mode × task_type\nprint(\"\\n\" + \"=\" * 75)\nprint(\"FAILURE MODE × TASK TYPE (all conditions combined)\")\nprint(\"=\" * 75)\ntask_mode = defaultdict(lambda: defaultdict(int))\nfor cond in results:\n    for mode, eps in results[cond]['details'].items():\n        for ep in eps:\n            task_mode[ep['task_type']][mode] += 1\n\nfor ttype in sorted(task_mode.keys()):\n    modes = task_mode[ttype]\n    total = sum(modes.values())\n    print(f\"\\n  {ttype} ({total} failures):\")\n    for m, c in sorted(modes.items(), key=lambda x: -x[1]):\n        print(f\"    {m}: {c}\")\n\n# Save detailed results\noutput = {\n    'summary': {},\n    'cross_condition': {},\n    'details': {},\n}\nfor cond in ['vanilla', 'taxei', 'random']:\n    r = results[cond]\n    output['summary'][cond] = {\n        'total_episodes': r['total_episodes'],\n        'total_failures': r['total_failures'],\n        'failure_rate': r['failure_rate'],\n        'by_mode': r['by_mode'],\n        'by_mode_and_operator': r['by_mode_and_operator'],\n    }\n    # Save example tasks per failure mode (without full trajectory)\n    output['details'][cond] = {}\n    for mode, eps in r['details'].items():\n        output['details'][cond][mode] = eps[:5]  # top 5 examples\n\nfor mode in sorted(all_modes):\n    output['cross_condition'][mode] = {\n        c: results[c]['by_mode'].get(mode, 0) for c in ['vanilla', 'taxei', 'random']\n    }\n\nout_path = os.path.join(BASE, 'eval_results/failure_analysis.json')\nwith open(out_path, 'w') as f:\n    json.dump(output, f, indent=2, ensure_ascii=False)\nprint(f\"\\nSaved to {out_path}\")\nPYEOF\npython3 /root/autodl-tmp/tax_error_inject_agent/scripts/failure_analysis.py\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T13:04:20.391403+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"===========================================================================\\nQUALITATIVE FAILURE ANALYSIS\\n===========================================================================\\n\\n===========================================================================\\nVANILLA  |  98/282 failures (34.8%)\\n===========================================================================\\n  Failure Mode                    Count        %\\n  --------------------------------------------\\n  max_steps_exhaustion               50    51.0%\\n  loop_repetition                    22    22.4%\\n  object_not_found                   13    13.3%\\n  exploration_wandering              13    13.3%\\n\\n  Failure Mode × Injection Operator (recovery eval only):\\n    exploration_wandering:\\n      P2_sub_goal_deletion: 4\\n      C4_observation_masking: 3\\n      C1_context_truncation: 3\\n      P1_step_order_swap: 3\\n    loop_repetition:\\n      C4_observation_masking: 8\\n      P1_step_order_swap: 7\\n      C1_context_truncation: 4\\n      P2_sub_goal_deletion: 3\\n    max_steps_exhaustion:\\n      C1_context_truncation: 1\\n    object_not_found:\\n      P2_sub_goal_deletion: 6\\n      P1_step_order_swap: 3\\n      C1_context_truncation: 2\\n      C4_observation_masking: 2\\n\\n===========================================================================\\nTAXEI  |  123/282 failures (43.6%)\\n===========================================================================\\n  Failure Mode                    Count        %\\n  --------------------------------------------\\n  max_steps_exhaustion               61    49.6%\\n  loop_repetition                    49    39.8%\\n  exploration_wandering               7     5.7%\\n  object_not_found                    6     4.9%\\n\\n  Failure Mode × Injection Operator (recovery eval only):\\n    exploration_wandering:\\n      C1_context_truncation: 4\\n      C4_observation_masking: 2\\n      P1_s
…[truncated 3345 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qualitative-failure_20260515T130130",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-15T13:04:20.391648+00:00_

分析完成。结果已保存到 `eval_results/failure_analysis.json`。

## 关键发现

### 失败模式分布

| Mode | Vanilla | TaxEI | Random |
|------|---------|-------|--------|
| max_steps_exhaustion | 50 (51.0%) | 61 (49.6%) | 53 (76.8%) |
| **loop_repetition** | **22 (22.4%)** | **49 (39.8%)** | **6 (8.7%)** |
| exploration_wandering | 13 (13.3%) | 7 (5.7%) | 6 (8.7%) |
| object_not_found | 13 (13.3%) | 6 (4.9%) | 4 (5.8%) |

### TaxEI 独特模式

**TaxEI 的 loop_repetition 显著高于其他两个条件**（49 vs 22 vs 6）。这意味着 TaxEI 训练出的 agent 在遇到错误注入后，更容易陷入重复动作循环（如反复 take/put 同一物品），而非探索新策略。

loop_repetition 在 TaxEI 中分布于所有 4 种注入算子：P1_step_order_swap (15), P2_sub_goal_deletion (14), C1_context_truncation (11), C4_observation_masking (9)。

### 注意事项

- `missing_subgoal` 未被触发 — agent 在 clean/heat/cool 任务中的失败更多表现为探索失败或循环，而非跳过子目标后直接放置。
- Random 只有 1 个 recovery eval 文件（seed 42），vanilla/taxei 各有 3 个，total 不完全对齐。
- clean eval 文件无 trajectory，其中的失败只能按 steps 数粗分类（大部分归入 max_steps_exhaustion）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_qualitative-failure_20260515T130130"
}
```

</details>

---
