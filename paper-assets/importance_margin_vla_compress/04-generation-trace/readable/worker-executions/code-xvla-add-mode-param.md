# code xvla add mode param

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 52
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/workers/worker_code_xvla-add-mode-param_20260521T022105.log`
- **Structured JSON:** [`a00895089d2ff0b3112c.json`](../../sessions/a0/a00895089d2ff0b3112c.json)

## Before a recorded user message

7 recorded events

### Log line

_source line 1_

Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.

---

### System

_source line 2_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress",
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a",
  "tools": [
    "Task",
    "AskUserQuestion",
    "Bash",
    "CronCreate",
    "CronDelete",
    "CronList",
    "Edit",
    "EnterPlanMode",
    "EnterWorktree",
    "ExitPlanMode",
    "ExitWorktree",
    "Glob",
    "Grep",
    "ListMcpResourcesTool",
    "Monitor",
    "NotebookEdit",
    "PushNotification",
    "Read",
    "ReadMcpResourceTool",
    "RemoteTrigger",
    "ScheduleWakeup",
    "Skill",
    "TaskOutput",
    "TaskStop",
    "TodoWrite",
    "ToolSearch",
    "WebFetch",
    "WebSearch",
    "Write",
    "mcp__agent-ml-research__detect_image",
    "mcp__agent-ml-research__kill_job",
    "mcp__agent-ml-research__ssh_execute",
    "mcp__agent-ml-research__ssh_read_only"
  ],
  "mcp_servers": [
    {
      "name": "agent-ml-research",
      "status": "connected"
    }
  ],
  "model": "claude-opus-4-6",
  "permissionMode": "bypassPermissions",
  "slash_commands": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api",
    "clear",
    "compact",
    "context",
    "heapdump",
    "init",
    "review",
    "security-review",
    "extra-usage",
    "usage",
    "insights",
    "team-onboarding"
  ],
  "apiKeySource": "none",
  "claude_code_version": "2.1.126",
  "output_style": "default",
  "agents": [
    "claude",
    "Explore",
    "general-purpose",
    "Plan",
    "statusline-setup"
  ],
  "skills": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api"
  ],
  "plugins": [],
  "analytics_disabled": false,
  "uuid": "3f771f61-55cc-4cd6-a7d2-bcfd3c8cae02",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Runtime record

_source line 3_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1779341400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "daa2ba20-537a-4aff-a83e-ceed194fb2c2",
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the current eval_xvla_pruning_libero.py to understand the existing implementation before making changes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a",
  "uuid": "82f4e6a9-715e-4370-bf99-80ebbb51383f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YT6C8e5BZvKsiBPrFfddeL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11939,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11939
      },
      "output_tokens": 36,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 5_

先读取本地脚本，了解当前 pruning 实现。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a",
  "uuid": "e0ee22ca-7a76-4315-b9fc-8a26a39abd7a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YT6C8e5BZvKsiBPrFfddeL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11939,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11939
      },
      "output_tokens": 36,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 6_

<details open><summary>🔧 Tool call — Agent · `toolu_01GN21kjZf2R5skEMqadpe3o`</summary>

```json
{
  "description": "Find eval script location",
  "subagent_type": "Explore",
  "prompt": "Find the file eval_xvla_pruning_libero.py in /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/ and its surrounding directory. Search broadly - it might be in artifacts/ or the project root or subdirectories. Return the full path(s) found."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a",
  "uuid": "4df37287-3f37-440d-aa72-fdfbfc35300d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YT6C8e5BZvKsiBPrFfddeL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11939,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11939
      },
      "output_tokens": 36,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### System

_source line 7_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a83baf340b2e72de3",
  "tool_use_id": "toolu_01GN21kjZf2R5skEMqadpe3o",
  "description": "Find eval script location",
  "task_type": "local_agent",
  "prompt": "Find the file eval_xvla_pruning_libero.py in /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/ and its surrounding directory. Search broadly - it might be in artifacts/ or the project root or subdirectories. Return the full path(s) found.",
  "uuid": "e9072e0c-40fb-4cd9-a1dd-dd200a6d4b46",
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a"
}
```

---

## Round 1

45 recorded events

### User

_source line 8 · 2026-05-21T02:21:22.882Z_

Find the file eval_xvla_pruning_libero.py in /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/ and its surrounding directory. Search broadly - it might be in artifacts/ or the project root or subdirectories. Return the full path(s) found.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GN21kjZf2R5skEMqadpe3o",
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a",
  "uuid": "7fddaf38-d01a-4274-b7cd-ed7a03a93e64"
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015WaKvYstPhewn7omKj3xm1`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a",
  "uuid": "5b5f7e02-7d76-42d8-80e0-1a28d900f233",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YT6C8e5BZvKsiBPrFfddeL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11939,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11939
      },
      "output_tokens": 36,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T02:21:23.822Z_

<details><summary>↩ Tool result · `toolu_015WaKvYstPhewn7omKj3xm1`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_read_only"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_execute"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a",
  "uuid": "ce8d1667-7dba-49c5-8b5e-5db0b79aae77",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__ssh_execute"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### System

_source line 11_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a83baf340b2e72de3",
  "tool_use_id": "toolu_01GN21kjZf2R5skEMqadpe3o",
  "description": "Finding **/*eval_xvla_pruning_libero.py",
  "usage": {
    "total_tokens": 18006,
    "tool_uses": 1,
    "duration_ms": 1603
  },
  "last_tool_name": "Glob",
  "uuid": "b436ee9c-8e69-4440-af4e-a8e12728ff33",
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a"
}
```

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Glob · `toolu_01Gm6NqnU95SAFefyXDySxzw`</summary>

```json
{
  "pattern": "**/*eval_xvla_pruning_libero.py",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01GN21kjZf2R5skEMqadpe3o",
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a",
  "uuid": "19144ffd-d559-4c69-a923-8a68fa4f7d1d",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HsVPPea5gEoWhkfx5U4jWo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17987,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17987,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-21T02:21:24.547Z_

<details><summary>↩ Tool result · `toolu_01Gm6NqnU95SAFefyXDySxzw`</summary>

```text
artifacts/eval_xvla_pruning_libero.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GN21kjZf2R5skEMqadpe3o",
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a",
  "uuid": "4e6f169e-0e20-43f5-be4d-77836484b4f4"
}
```

</details>

---

### System

_source line 14_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a83baf340b2e72de3",
  "tool_use_id": "toolu_01GN21kjZf2R5skEMqadpe3o",
  "status": "completed",
  "output_file": "",
  "summary": "Find eval script location",
  "usage": {
    "total_tokens": 19022,
    "tool_uses": 1,
    "duration_ms": 3064
  },
  "uuid": "ffe899fd-4b8c-4b52-b7c4-b5bd2140f436",
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a"
}
```

---

### Tool result

_source line 15 · 2026-05-21T02:21:25.949Z_

<details><summary>↩ Tool result · `toolu_01GN21kjZf2R5skEMqadpe3o`</summary>

```text
Perfect! I found the file. Here's the result:

**Full Path Found:**
`/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/eval_xvla_pruning_libero.py`

The file is located in the `artifacts/` subdirectory within the project root.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a",
  "uuid": "05863a62-a573-4406-a1ab-8a6dcad85bbe",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Find the file eval_xvla_pruning_libero.py in /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/ and its surrounding directory. Search broadly - it might be in artifacts/ or the project root or subdirectories. Return the full path(s) found.",
    "agentId": "a83baf340b2e72de3",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! I found the file. Here's the result:\n\n**Full Path Found:**\n`/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/eval_xvla_pruning_libero.py`\n\nThe file is located in the `artifacts/` subdirectory within the project root."
      }
    ],
    "totalDurationMs": 3065,
    "totalTokens": 19096,
    "totalToolUseCount": 1,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1013,
      "cache_read_input_tokens": 17987,
      "output_tokens": 91,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1013
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 91,
          "cache_read_input_tokens": 17987,
          "cache_creation_input_tokens": 1013,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1013,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 1,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Read · `toolu_01EMrMk3G5JyuYTiRfpcD9uR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/eval_xvla_pruning_libero.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a",
  "uuid": "d8815392-e51d-4d44-82c8-bd25184ebc0b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EiauGpc8iehVcghgyaA65p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1019,
      "cache_read_input_tokens": 23780,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1019
      },
      "output_tokens": 60,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-21T02:21:28.075Z_

<details><summary>↩ Tool result · `toolu_01EMrMk3G5JyuYTiRfpcD9uR`</summary>

```text
1	"""X-VLA Vision Token Pruning Evaluation on LIBERO.
2	
3	Prunes vision tokens by L2 norm after Florence2's image encoder + linear projection,
4	before they enter the Florence2 language encoder. Evaluates on LIBERO suites.
5	
6	Follows official X-VLA evaluation protocol:
7	  - Absolute EEF control (use_delta=False)
8	  - 20D action space: [arm1: pos(3)+rot6d(6)+grip(1)] + [arm2: zeros(10)]
9	  - 20D proprio: [pos(3)+rot6d(6)+0.0] + zeros(10)
10	  - domain_id=3 for LIBERO
11	  - Closed-loop proprio update from last predicted action
12	
13	Usage:
14	    CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl python eval_xvla_pruning_libero.py \
15	        --model_path /path/to/X-VLA-Libero \
16	        --suite libero_object \
17	        --keep_ratio 0.5 \
18	        --num_episodes 50 \
19	        --gpu 0
20	"""
21	
22	from __future__ import annotations
23	
24	import argparse
25	import json
26	import logging
27	import os
28	import sys
29	import time as time_mod
30	from pathlib import Path
31	from functools import wraps
32	
33	os.environ.setdefault("MUJOCO_GL", "egl")
34	
35	import numpy as np
36	import torch
37	from PIL import Image
38	
39	sys.path.insert(0, str(Path(__file__).resolve().parent))
40	
41	logging.basicConfig(
42	    level=logging.INFO,
43	    format="%(asctime)s [%(levelname)s] %(message)s",
44	    datefmt="%Y-%m-%d %H:%M:%S",
45	)
46	log = logging.getLogger(__name__)
47	
48	SUITE_MAX_STEPS = {
49	    "libero_spatial": 800,
50	    "libero_object": 800,
51	    "libero_goal": 800,
52	    "libero_10": 900,
53	    "libero_90": 800,
54	}
55	
56	EPS = 1e-6
57	
58	
59	def parse_args():
60	    p = argparse.ArgumentParser(description="X-VLA pruning eval on LIBERO")
61	    p.add_argument("--model_path", type=str, default="2toINF/X-VLA-Libero",
62	                   help="HuggingFace model path or local dir")
63	    p.add_argument("--suite", type=str, default="libero_object",
64	                   choices=list(SUITE_MAX_STEPS.keys()))
65	    p.add_argument("--keep_ratio", type=float, default=1.0,
66	                   help="Fraction of vision tokens to keep (1.0 = no pruning)")
67	    p.add_argument("--num_episodes", type=int, default=50)
68	    p.add_argument("--gpu", type=int, default=0)
69	    p.add_argument("--seed", type=int, default=42)
70	    p.add_argument("--max_steps", type=int, default=None)
71	    p.add_argument("--output", type=str, default=None)
72	    p.add_argument("--task_ids", type=str, default=None)
73	    p.add_argument("--domain_id", type=int, default=3)
74	    p.add_argument("--denoise_steps", type=int, default=10,
75	                   help="Flow matching denoising steps")
76	    return p.parse_args()
77	
78	
79	# ---------------------------------------------------------------------------
80	# Pruning hook
81	# ---------------------------------------------------------------------------
82	
83	def install_vision_pruning(model, keep_ratio: float):
84	    if keep_ratio >= 1.0:
85	        log.info("keep_ratio=%.2f, no pruning applied", keep_ratio)
86	        return
87	
88	    original_encode = model.vlm._encode_image
89	
90	    @wraps(original_encode)
91	    def pruned_encode(pixel_values):
92	        features = original_encode(pixel_values)
93	        N = features.shape[1]
94	        k = max(1, int(keep_ratio * N))
95	        if k >= N:
96	            return features
97	        norms = features.norm(dim=-1)
98	        _, indices = norms.topk(k, dim=-1)
99	        indices_sorted = indices.sort(dim=-1).values
100	        pruned = features.gather(
101	            1, indices_sorted.unsqueeze(-1).expand(-1, -1, features.shape[-1])
102	        )
103	        return pruned
104	
105	    model.vlm._encode_image = pruned_encode
106	    log.info("Vision pruning installed: keep_ratio=%.2f", keep_ratio)
107	
108	
109	# ---------------------------------------------------------------------------
110	# Model loading
111	# ---------------------------------------------------------------------------
112	
113	def load_model(model_path: str, device: torch.device):
114	    model_dir = str(Path(model_path).resolve())
115	    sys.path.insert(0, model_dir)
116	
117	    from configuration_xvla import XVLAConfig
118	    from modeling_xvla import XVLA
119	    from processing_xvla import XVLAProcessor
120	    from safetensors.torch import load_file
121	
122	    log.info("Loading X-VLA from %s", model_dir)
123	    config = XVLAConfig.from_pretrained(model_dir)
124	    model = XVLA(config)
125	
126	    safetensors_path = Path(model_dir) / "model.safetensors"
127	    if safetensors_path.exists():
128	        state_dict = load_file(str(safetensors_path))
129	    else:
130	        import torch as _torch
131	        state_dict = _torch.load(Path(model_dir) / "pytorch_model.bin", map_location="cpu")
132	    model.load_state_dict(state_dict, strict=False)
133	    model = model.to(device).eval()
134	
135	    processor = XVLAProcessor.from_pretrained(model_dir, trust_remote_code=True)
136	    if processor.tokenizer.pad_token is None:
137	        processor.tokenizer.pad_token = "&lt;pad>"
138	        processor.tokenizer.pad_token_id = 1
139	
140	    n_params = sum(p.numel() for p in model.parameters())
141	    log.info("Model loaded: %.1fM params, dtype=%s", n_params / 1e6, model.dtype)
142	    return model, processor
143	
144	
145	# ---------------------------------------------------------------------------
146	# 6D rotation utilities (following X-VLA's convention)
147	# ---------------------------------------------------------------------------
148	
149	def mat_to_rot6d(R: np.ndarray) -> np.ndarray:
150	    """Extract 6D rotation from 3x3 rotation matrix: first two columns."""
151	    return np.concatenate([R[:3, 0], R[:3, 1]], axis=-1).astype(np.float32)
152	
153	
154	def rot6d_to_axis_angle(r6d: np.ndarray) -> np.ndarray:
155	    """Convert 6D rotation representation to axis-angle via Gram-Schmidt."""
156	    import robosuite.utils.transform_utils as T
157	
158	    single = r6d.ndim == 1
159	    if single:
160	        r6d = r6d[None, :]
161	
162	    a1 = r6d[:, 0:3]
163	    a2 = r6d[:, 3:6]
164	
165	    b1 = a1 / (np.linalg.norm(a1, axis=-1, keepdims=True) + EPS)
166	    dot_prod = np.sum(b1 * a2, axis=-1, keepdims=True)
167	    b2_orth = a2 - dot_prod * b1
168	    b2 = b2_orth / (np.linalg.norm(b2_orth, axis=-1, keepdims=True) + EPS)
169	    b3 = np.cross(b1, b2, axis=-1)
170	
171	    R = np.stack([b1, b2, b3], axis=-1)  # (N, 3, 3)
172	
173	    results = []
174	    for i in range(R.shape[0]):
175	        quat = T.mat2quat(R[i])
176	        aa = T.quat2axisangle(quat)
177	        results.append(aa)
178	
179	    result = np.stack(results, axis=0)
180	    return result[0] if single else result
181	
182	
183	# ---------------------------------------------------------------------------
184	# Observation processing
185	# ---------------------------------------------------------------------------
186	
187	def extract_proprio_20d(env) -> np.ndarray:
188	    """Extract 20D proprio: [pos(3)+rot6d(6)+0.0] + zeros(10) from env robot state."""
189	    robot = env.env.robots[0]
190	    ee_pos = robot.controller.ee_pos.copy()         # (3,)
191	    ee_ori_mat = robot.controller.ee_ori_mat.copy()  # (3, 3)
192	    ee_rot6d = mat_to_rot6d(ee_ori_mat)              # (6,)
193	
194	    arm1 = np.concatenate([ee_pos, ee_rot6d, np.array([0.0], dtype=np.float32)])  # (10,)
195	    arm2 = np.zeros(10, dtype=np.float32)
196	    return np.concatenate([arm1, arm2])  # (20,)
197	
198	
199	def decode_action_20d_to_7d(action_20d: np.ndarray) -> np.ndarray:
200	    """Convert 20D X-VLA action to 7D LIBERO action.
201	
202	    Input:  [pos(3), rot6d(6), grip(1), arm2(10)]  — only arm1 used
203	    Output: [pos(3), axis_angle(3), grip(1)]
204	    """
205	    single = action_20d.ndim == 1
206	    if single:
207	        action_20d = action_20d[None, :]
208	
209	    pos = action_20d[:, :3]
210	    rot6d = action_20d[:, 3:9]
211	    grip = action_20d[:, 9:10]
212	
213	    axis_angle = rot6d_to_axis_angle(rot6d)
214	
215	    # Discretize gripper: >0.5 → 1.0 (open), else -1.0 (close)
216	    grip_disc = np.where(grip > 0.5, 1.0, -1.0)
217	
218	    result = np.concatenate([pos, axis_angle, grip_disc], axis=-1).astype(np.float32)
219	    return result[0] if single else result
220	
221	
222	def get_images_from_obs(obs) -> list:
223	    """Extract camera images from LIBERO observation, apply agentview flip."""
224	    images = []
225	    for cam_name in ["agentview_image", "robot0_eye_in_hand_image"]:
226	        img = obs.get(cam_name, None)
227	        if img is None:
228	            for k, v in obs.items():
229	                if cam_name in k and isinstance(v, np.ndarray):
230	                    img = v
231	                    break
232	        if img is not None:
233	            if img.dtype in (np.float32, np.float64):
234	                img = (np.clip(img, 0, 1) * 255).astype(np.uint8)
235	            if cam_name == "agentview_image":
236	                img = np.flip(np.flip(img, 0), 1).copy()
237	            images.append(Image.fromarray(img))
238	    return images
239	
240	
241	# ---------------------------------------------------------------------------
242	# Action prediction
243	# ---------------------------------------------------------------------------
244	
245	@torch.no_grad()
246	def predict_actions(model, processor, images, task_desc, proprio_20d, domain_id,
247	                    device, denoise_steps=10):
248	    inputs = processor(images=images, language_instruction=task_desc)
249	
250	    proprio_t = torch.tensor(proprio_20d, dtype=torch.float32).unsqueeze(0).to(device)
251	    domain_t = torch.tensor([domain_id], dtype=torch.long).to(device)
252	
253	    for k, v in inputs.items():
254	        if isinstance(v, torch.Tensor):
255	            if v.is_floating_point():
256	                inputs[k] = v.to(device=device, dtype=torch.float32)
257	            else:
258	                inputs[k] = v.to(device=device)
259	
260	    actions = model.generate_actions(
261	        input_ids=inputs["input_ids"],
262	        image_input=inputs["image_input"],
263	        image_mask=inputs["image_mask"],
264	        proprio=proprio_t,
265	        domain_id=domain_t,
266	        steps=denoise_steps,
267	    )  # [1, 30, 20]
268	
269	    return actions.squeeze(0).float().cpu().numpy()  # [30, 20]
270	
271	
272	# ---------------------------------------------------------------------------
273	# Wilson CI
274	# ---------------------------------------------------------------------------
275	
276	def wilson_ci(successes, total, z=1.96):
277	    if total == 0:
278	        return 0.0, 0.0, 1.0
279	    p = successes / total
280	    denom = 1 + z ** 2 / total
281	    center = (p + z ** 2 / (2 * total)) / denom
282	    spread = z * np.sqrt((p * (1 - p) + z ** 2 / (4 * total)) / total) / denom
283	    return center, max(0.0, center - spread), min(1.0, center + spread)
284	
285	
286	# ---------------------------------------------------------------------------
287	# Main evaluation
288	# ---------------------------------------------------------------------------
289	
290	def run_evaluation(args):
291	    device = torch.device(f"cuda:{args.gpu}" if torch.cuda.is_available() else "cpu")
292	    max_steps = args.max_steps or SUITE_MAX_STEPS.get(args.suite, 800)
293	    output_path = Path(args.output or
294	                       f"eval_results/xvla_prune_k{args.keep_ratio}_{args.suite}.json")
295	
296	    log.info("Suite: %s | Device: %s | keep_ratio=%.2f | Episodes/task: %d | Max steps: %d",
297	             args.suite, device, args.keep_ratio, args.num_episodes, max_steps)
298	
299	    np.random.seed(args.seed)
300	    torch.manual_seed(args.seed)
301	
302	    t0 = time_mod.time()
303	    model, processor = load_model(args.model_path, device)
304	    log.info("Model loaded in %.1fs", time_mod.time() - t0)
305	
306	    dummy_img = torch.randn(1, 3, 224, 224, device=device)
307	    with torch.no_grad():
308	        dummy_feats = model.vlm._encode_image(dummy_img)
309	    n_vis_tokens = dummy_feats.shape[1]
310	    k_tokens = max(1, int(args.keep_ratio * n_vis_tokens))
311	    log.info("Vision tokens: %d total, keeping %d (%.0f%%)",
312	             n_vis_tokens, k_tokens, args.keep_ratio * 100)
313	
314	    install_vision_pruning(model, args.keep_ratio)
315	
316	    num_actions_per_chunk = model.num_actions  # 30
317	
318	    # LIBERO setup — use OffScreenRenderEnv directly (matching official X-VLA eval)
319	    from libero.libero import benchmark, get_libero_path
320	    from libero.libero.envs import OffScreenRenderEnv
321	
322	    task_suite = benchmark.get_benchmark(args.suite)()
323	    n_tasks = task_suite.n_tasks
324	
325	    if args.task_ids:
326	        task_id_list = [int(x) for x in args.task_ids.split(",")]
327	    else:
328	        task_id_list = list(range(n_tasks))
329	
330	    eval_start = time_mod.time()
331	    all_task_results = {}
332	    total_successes = 0
333	    total_episodes = 0
334	
335	    for task_id in task_id_list:
336	        task = task_suite.get_task(task_id)
337	        task_desc = task.language
338	        task_bddl = os.path.join(
339	            get_libero_path("bddl_files"), task.problem_folder, task.bddl_file
340	        )
341	        log.info("--- Task %d: %s ---", task_id, task_desc)
342	
343	        init_states = task_suite.get_task_init_states(task_id)
344	
345	        task_successes = []
346	        task_lengths = []
347	
348	        for ep in range(args.num_episodes):
349	            env = OffScreenRenderEnv(
350	                bddl_file_name=task_bddl,
351	                camera_heights=256,
352	                camera_widths=256,
353	            )
354	            env.seed(args.seed + ep + 100)
355	            obs = env.reset()
356	
357	            init_state_id = ep % init_states.shape[0]
358	            obs = env.set_init_state(init_states[init_state_id])
359	
360	            # Settle the robot with neutral actions
361	            for _ in range(10):
362	                neutral = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0], dtype=np.float32)
363	                obs, _, _, _ = env.step(neutral)
364	
365	            # Switch to absolute control
366	            for robot in env.env.robots:
367	                robot.controller.use_delta = False
368	
369	            action_queue = []
370	            proprio_state = None
371	            success = False
372	
373	            for step_idx in range(max_steps):
374	                if not action_queue:
375	                    # Extract proprio from env
376	                    proprio_20d = extract_proprio_20d(env)
377	                    if proprio_state is not None:
378	                        proprio_20d[:9] = proprio_state[:9]
379	
380	                    images = get_images_from_obs(obs)
381	                    if not images:
382	                        raise ValueError(f"No images found in obs keys: {list(obs.keys())}")
383	
384	                    raw_actions = predict_actions(
385	                        model, processor, images, task_desc, proprio_20d,
386	                        args.domain_id, device, args.denoise_steps,
387	                    )  # [30, 20]
388	
389	                    # Update closed-loop proprio with last predicted action
390	                    proprio_state = proprio_20d.copy()
391	                    proprio_state[:9] = raw_actions[-1, :9].copy()
392	
393	                    actions_7d = decode_action_20d_to_7d(raw_actions)  # [30, 7]
394	                    action_queue = list(actions_7d)
395	
396	                action = action_queue.pop(0)
397	                obs, reward, done, info = env.step(action)
398	
399	                if done or reward > 0.5:
400	                    success = True
401	                    break
402	
403	            ep_steps = step_idx + 1
404	            task_successes.append(success)
405	            task_lengths.append(ep_steps)
406	            log.info("  Ep %d/%d | %s | steps=%d",
407	                     ep + 1, args.num_episodes,
408	                     "SUCCESS" if success else "FAIL", ep_steps)
409	
410	            env.close()
411	
412	        n_succ = sum(task_successes)
413	        n_total = len(task_successes)
414	        sr = n_succ / n_total if n_total > 0 else 0.0
415	
416	        all_task_results[task_id] = {
417	            "task_id": task_id,
418	            "task_description": task_desc,
419	            "success_count": n_succ,
420	            "total_episodes": n_total,
421	            "success_rate": round(sr, 4),
422	            "mean_steps": round(float(np.mean(task_lengths)), 1),
423	        }
424	        total_successes += n_succ
425	        total_episodes += n_total
426	        log.info("  Task %d SR: %d/%d (%.1f%%)", task_id, n_succ, n_total, sr * 100)
427	
428	    elapsed = time_mod.time() - eval_start
429	    overall_sr = total_successes / total_episodes if total_episodes > 0 else 0.0
430	    _, ci_lo, ci_hi = wilson_ci(total_successes, total_episodes)
431	
432	    log.info("=" * 60)
433	    log.info("SUITE: %s | MODEL: xvla | keep_ratio: %.2f", args.suite, args.keep_ratio)
434	    log.info("Overall SR: %d/%d (%.1f%%)", total_successes, total_episodes, overall_sr * 100)
435	    log.info("95%% Wilson CI: [%.1f%%, %.1f%%]", ci_lo * 100, ci_hi * 100)
436	    for tid, tr in sorted(all_task_results.items()):
437	        log.info("  Task %d: %.0f%% (%d/%d) -- %s",
438	                 tid, tr["success_rate"] * 100, tr["success_count"],
439	                 tr["total_episodes"], tr["task_description"])
440	    log.info("Elapsed: %.1f min", elapsed / 60)
441	    log.info("=" * 60)
442	
443	    summary = {
444	        "model": "xvla",
445	        "model_path": args.model_path,
446	        "mode": "l2_norm_prune",
447	        "suite": args.suite,
448	        "keep_ratio": args.keep_ratio,
449	        "n_vision_tokens_original": n_vis_tokens,
450	        "n_vision_tokens_kept": k_tokens,
451	        "total_episodes": total_episodes,
452	        "total_successes": total_successes,
453	        "overall_success_rate": round(overall_sr, 4),
454	        "wilson_ci_95": [round(ci_lo, 4), round(ci_hi, 4)],
455	        "num_episodes_per_task": args.num_episodes,
456	        "max_steps": max_steps,
457	        "num_actions_per_chunk": num_actions_per_chunk,
458	        "domain_id": args.domain_id,
459	        "denoise_steps": args.denoise_steps,
460	        "seed": args.seed,
461	        "elapsed_seconds": round(elapsed, 1),
462	        "per_task": all_task_results,
463	    }
464	
465	    output_path.parent.mkdir(parents=True, exist_ok=True)
466	    with open(output_path, "w") as f:
467	        json.dump(summary, f, indent=2)
468	    log.info("Results saved to %s", output_path)
469	
470	    return summary
471	
472	
473	if __name__ == "__main__":
474	    args = parse_args()
475	    run_evaluation(args)
476	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a",
  "uuid": "b9573716-a3d4-48ae-a2c5-062a3f447ec2",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/eval_xvla_pruning_libero.py",
      "content": "\"\"\"X-VLA Vision Token Pruning Evaluation on LIBERO.\n\nPrunes vision tokens by L2 norm after Florence2's image encoder + linear projection,\nbefore they enter the Florence2 language encoder. Evaluates on LIBERO suites.\n\nFollows official X-VLA evaluation protocol:\n  - Absolute EEF control (use_delta=False)\n  - 20D action space: [arm1: pos(3)+rot6d(6)+grip(1)] + [arm2: zeros(10)]\n  - 20D proprio: [pos(3)+rot6d(6)+0.0] + zeros(10)\n  - domain_id=3 for LIBERO\n  - Closed-loop proprio update from last predicted action\n\nUsage:\n    CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl python eval_xvla_pruning_libero.py \\\n        --model_path /path/to/X-VLA-Libero \\\n        --suite libero_object \\\n        --keep_ratio 0.5 \\\n        --num_episodes 50 \\\n        --gpu 0\n\"\"\"\n\nfrom __future__ import annotations\n\nimport argparse\nimport json\nimport logging\nimport os\nimport sys\nimport time as time_mod\nfrom pathlib import Path\nfrom functools import wraps\n\nos.environ.setdefault(\"MUJOCO_GL\", \"egl\")\n\nimport numpy as np\nimport torch\nfrom PIL import Image\n\nsys.path.insert(0, str(Path(__file__).resolve().parent))\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    datefmt=\"%Y-%m-%d %H:%M:%S\",\n)\nlog = logging.getLogger(__name__)\n\nSUITE_MAX_STEPS = {\n    \"libero_spatial\": 800,\n    \"libero_object\": 800,\n    \"libero_goal\": 800,\n    \"libero_10\": 900,\n    \"libero_90\": 800,\n}\n\nEPS = 1e-6\n\n\ndef parse_args():\n    p = argparse.ArgumentParser(description=\"X-VLA pruning eval on LIBERO\")\n    p.add_argument(\"--model_path\", type=str, default=\"2toINF/X-VLA-Libero\",\n                   help=\"HuggingFace model path or local dir\")\n    p.add_argument(\"--suite\", type=str, default=\"libero_object\",\n                   choices=list(SUITE_MAX_STEPS.keys()))\n    p.add_argument(\"--keep_ratio\", type=float, default=1.0,\n                   help=\"Fraction of vision tokens to keep (1.0 = no pruning)\")\n    p.add_argument(\"--num_episodes\", type=int, default=50)\n    p.add_argument(\"--gpu\", type=int, default=0)\n    p.add_argument(\"--seed\", type=int, default=42)\n    p.add_argument(\"--max_steps\", type=int, default=None)\n    p.add_argument(\"--output\", type=str, default=None)\n    p.add_argument(\"--task_ids\", type=str, default=None)\n    p.add_argument(\"--domain_id\", type=int, default=3)\n    p.add_argument(\"--denoise_steps\", type=int, default=10,\n                   help=\"Flow matching denoising steps\")\n    return p.parse_args()\n\n\n# ---------------------------------------------------------------------------\n# Pruning hook\n# ---------------------------------------------------------------------------\n\ndef install_vision_pruning(model, keep_ratio: float):\n    if keep_ratio >= 1.0:\n        log.info(\"keep_ratio=%.2f, no pruning applied\", keep_ratio)\n        return\n\n    original_encode = model.vlm._encode_image\n\n    @wraps(original_encode)\n    def pruned_encode(pixel_values):\n        features = original_encode(pixel_values)\n        N = features.shape[1]\n        k = max(1, int(keep_ratio * N))\n        if k >= N:\n            return features\n        norms = features.norm(dim=-1)\n        _, indices = norms.topk(k, dim=-1)\n        indices_sorted = indices.sort(dim=-1).values\n        pruned = features.gather(\n            1, indices_sorted.unsqueeze(-1).expand(-1, -1, features.shape[-1])\n        )\n        return pruned\n\n    model.vlm._encode_image = pruned_encode\n    log.info(\"Vision pruning installed: keep_ratio=%.2f\", keep_ratio)\n\n\n# ---------------------------------------------------------------------------\n# Model loading\n# ---------------------------------------------------------------------------\n\ndef load_model(model_path: str, device: torch.device):\n    model_dir = str(Path(model_path).resolve())\n    sys.path.insert(0, model_dir)\n\n    from configuration_xvla import XVLAConfig\n    from modeling_xvla import XVLA\n    from processing_xvla import XVLAProcessor\n    from safetensors.torch import load_file\n\n    log.info(\"Loading X-VLA from %s\", model_dir)\n    config = XVLAConfig.from_pretrained(model_dir)\n    model = XVLA(config)\n\n    safetensors_path = Path(model_dir) / \"model.safetensors\"\n    if safetensors_path.exists():\n        state_dict = load_file(str(safetensors_path))\n    else:\n        import torch as _torch\n        state_dict = _torch.load(Path(model_dir) / \"pytorch_model.bin\", map_location=\"cpu\")\n    model.load_state_dict(state_dict, strict=False)\n    model = model.to(device).eval()\n\n    processor = XVLAProcessor.from_pretrained(model_dir, trust_remote_code=True)\n    if processor.tokenizer.pad_token is None:\n        processor.tokenizer.pad_token = \"&lt;pad>\"\n        processor.tokenizer.pad_token_id = 1\n\n    n_params = sum(p.numel() for p in model.parameters())\n    log.info(\"Model loaded: %.1fM params, dtype=%s\", n_params / 1e6, model.dtype)\n    return model, processor\n\n\n# ---------------------------------------------------------------------------\n# 6D rotation utilities (following X-VLA's convention)\n# ---------------------------------------------------------------------------\n\ndef mat_to_rot6d(R: np.ndarray) -> np.ndarray:\n    \"\"\"Extract 6D rotation from 3x3 rotation matrix: first two columns.\"\"\"\n    return np.concatenate([R[:3, 0], R[:3, 1]], axis=-1).astype(np.float32)\n\n\ndef rot6d_to_axis_angle(r6d: np.ndarray) -> np.ndarray:\n    \"\"\"Convert 6D rotation representation to axis-angle via Gram-Schmidt.\"\"\"\n    import robosuite.utils.transform_utils as T\n\n    single = r6d.ndim == 1\n    if single:\n        r6d = r6d[None, :]\n\n    a1 = r6d[:, 0:3]\n    a2 = r6d[:, 3:6]\n\n    b1 = a1 / (np.linalg.norm(a1, axis=-1, keepdims=True) + EPS)\n    dot_prod = np.sum(b1 * a2, axis=-1, keepdims=True)\n    b2_orth = a2 - dot_prod * b1\n    b2 = b2_orth / (np.linalg.norm(b2_orth, axis=-1, keepdims=True) + EPS)\n    b3 = np.cross(b1, b2, axis=-1)\n\n    R = np.stack([b1, b2, b3], axis=-1)  # (N, 3, 3)\n\n    results = []\n    for i in range(R.shape[0]):\n        quat = T.mat2quat(R[i])\n        aa = T.quat2axisangle(quat)\n        results.append(aa)\n\n    result = np.stack(results, axis=0)\n    return result[0] if single else result\n\n\n# ---------------------------------------------------------------------------\n# Observation processing\n# ---------------------------------------------------------------------------\n\ndef extract_proprio_20d(env) -> np.ndarray:\n    \"\"\"Extract 20D proprio: [pos(3)+rot6d(6)+0.0] + zeros(10) from env robot state.\"\"\"\n    robot = env.env.robots[0]\n    ee_pos = robot.controller.ee_pos.copy()         # (3,)\n    ee_ori_mat = robot.controller.ee_ori_mat.copy()  # (3, 3)\n    ee_rot6d = mat_to_rot6d(ee_ori_mat)              # (6,)\n\n    arm1 = np.concatenate([ee_pos, ee_rot6d, np.array([0.0], dtype=np.float32)])  # (10,)\n    arm2 = np.zeros(10, dtype=np.float32)\n    return np.concatenate([arm1, arm2])  # (20,)\n\n\ndef decode_action_20d_to_7d(action_20d: np.ndarray) -> np.ndarray:\n    \"\"\"Convert 20D X-VLA action to 7D LIBERO action.\n\n    Input:  [pos(3), rot6d(6), grip(1), arm2(10)]  — only arm1 used\n    Output: [pos(3), axis_angle(3), grip(1)]\n    \"\"\"\n    single = action_20d.ndim == 1\n    if single:\n        action_20d = action_20d[None, :]\n\n    pos = action_20d[:, :3]\n    rot6d = action_20d[:, 3:9]\n    grip = action_20d[:, 9:10]\n\n    axis_angle = rot6d_to_axis_angle(rot6d)\n\n    # Discretize gripper: >0.5 → 1.0 (open), else -1.0 (close)\n    grip_disc = np.where(grip > 0.5, 1.0, -1.0)\n\n    result = np.concatenate([pos, axis_angle, grip_disc], axis=-1).astype(np.float32)\n    return result[0] if single else result\n\n\ndef get_images_from_obs(obs) -> list:\n    \"\"\"Extract camera images from LIBERO observation, apply agentview flip.\"\"\"\n    images = []\n    for cam_name in [\"agentview_image\", \"robot0_eye_in_hand_image\"]:\n        img = obs.get(cam_name, None)\n        if img is None:\n            for k, v in obs.items():\n                if cam_name in k and isinstance(v, np.ndarray):\n                    img = v\n                    break\n        if img is not None:\n            if img.dtype in (np.float32, np.float64):\n                img = (np.clip(img, 0, 1) * 255).astype(np.uint8)\n            if cam_name == \"agentview_image\":\n                img = np.flip(np.flip(img, 0), 1).copy()\n            images.append(Image.fromarray(img))\n    return images\n\n\n# ---------------------------------------------------------------------------\n# Action prediction\n# ---------------------------------------------------------------------------\n\n@torch.no_grad()\ndef predict_actions(model, processor, images, task_desc, proprio_20d, domain_id,\n                    device, denoise_steps=10):\n    inputs = processor(images=images, language_instruction=task_desc)\n\n    proprio_t = torch.tensor(proprio_20d, dtype=torch.float32).unsqueeze(0).to(device)\n    domain_t = torch.tensor([domain_id], dtype=torch.long).to(device)\n\n    for k, v in inputs.items():\n        if isinstance(v, torch.Tensor):\n            if v.is_floating_point():\n                inputs[k] = v.to(device=device, dtype=torch.float32)\n            else:\n                inputs[k] = v.to(device=device)\n\n    actions = model.generate_actions(\n        input_ids=inputs[\"input_ids\"],\n        image_input=inputs[\"image_input\"],\n        image_mask=inputs[\"image_mask\"],\n        proprio=proprio_t,\n        domain_id=domain_t,\n        steps=denoise_steps,\n    )  # [1, 30, 20]\n\n    return actions.squeeze(0).float().cpu().numpy()  # [30, 20]\n\n\n# ---------------------------------------------------------------------------\n# Wilson CI\n# ---------------------------------------------------------------------------\n\ndef wilson_ci(successes, total, z=1.96):\n    if total == 0:\n        return 0.0, 0.0, 1.0\n    p = successes / total\n    denom = 1 + z ** 2 / total\n    center = (p + z ** 2 / (2 * total)) / denom\n    spread = z * np.sqrt((p * (1 - p) + z ** 2 / (4 * total)) / total) / denom\n    return center, max(0.0, center - spread), min(1.0, center + spread)\n\n\n# ---------------------------------------------------------------------------\n# Main evaluation\n# ---------------------------------------------------------------------------\n\ndef run_evaluation(args):\n    device = torch.device(f\"cuda:{args.gpu}\" if torch.cuda.is_available() else \"cpu\")\n    max_steps = args.max_steps or SUITE_MAX_STEPS.get(args.suite, 800)\n    output_path = Path(args.output or\n                       f\"eval_results/xvla_prune_k{args.keep_ratio}_{args.suite}.json\")\n\n    log.info(\"Suite: %s | Device: %s | keep_ratio=%.2f | Episodes/task: %d | Max steps: %d\",\n             args.suite, device, args.keep_ratio, args.num_episodes, max_steps)\n\n    np.random.seed(args.seed)\n    torch.manual_seed(args.seed)\n\n    t0 = time_mod.time()\n    model, processor = load_model(args.model_path, device)\n    log.info(\"Model loaded in %.1fs\", time_mod.time() - t0)\n\n    dummy_img = torch.randn(1, 3, 224, 224, device=device)\n    with torch.no_grad():\n        dummy_feats = model.vlm._encode_image(dummy_img)\n    n_vis_tokens = dummy_feats.shape[1]\n    k_tokens = max(1, int(args.keep_ratio * n_vis_tokens))\n    log.info(\"Vision tokens: %d total, keeping %d (%.0f%%)\",\n             n_vis_tokens, k_tokens, args.keep_ratio * 100)\n\n    install_vision_pruning(model, args.keep_ratio)\n\n    num_actions_per_chunk = model.num_actions  # 30\n\n    # LIBERO setup — use OffScreenRenderEnv directly (matching official X-VLA eval)\n    from libero.libero import benchmark, get_libero_path\n    from libero.libero.envs import OffScreenRenderEnv\n\n    task_suite = benchmark.get_benchmark(args.suite)()\n    n_tasks = task_suite.n_tasks\n\n    if args.task_ids:\n        task_id_list = [int(x) for x in args.task_ids.split(\",\")]\n    else:\n        task_id_list = list(range(n_tasks))\n\n    eval_start = time_mod.time()\n    all_task_results = {}\n    total_successes = 0\n    total_episodes = 0\n\n    for task_id in task_id_list:\n        task = task_suite.get_task(task_id)\n        task_desc = task.language\n        task_bddl = os.path.join(\n            get_libero_path(\"bddl_files\"), task.problem_folder, task.bddl_file\n        )\n        log.info(\"--- Task %d: %s ---\", task_id, task_desc)\n\n        init_states = task_suite.get_task_init_states(task_id)\n\n        task_successes = []\n        task_lengths = []\n\n        for ep in range(args.num_episodes):\n            env = OffScreenRenderEnv(\n                bddl_file_name=task_bddl,\n                camera_heights=256,\n                camera_widths=256,\n            )\n            env.seed(args.seed + ep + 100)\n            obs = env.reset()\n\n            init_state_id = ep % init_states.shape[0]\n            obs = env.set_init_state(init_states[init_state_id])\n\n            # Settle the robot with neutral actions\n            for _ in range(10):\n                neutral = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0], dtype=np.float32)\n                obs, _, _, _ = env.step(neutral)\n\n            # Switch to absolute control\n            for robot in env.env.robots:\n                robot.controller.use_delta = False\n\n            action_queue = []\n            proprio_state = None\n            success = False\n\n            for step_idx in range(max_steps):\n                if not action_queue:\n                    # Extract proprio from env\n                    proprio_20d = extract_proprio_20d(env)\n                    if proprio_state is not None:\n                        proprio_20d[:9] = proprio_state[:9]\n\n                    images = get_images_from_obs(obs)\n                    if not images:\n                        raise ValueError(f\"No images found in obs keys: {list(obs.keys())}\")\n\n                    raw_actions = predict_actions(\n                        model, processor, images, task_desc, proprio_20d,\n                        args.domain_id, device, args.denoise_steps,\n                    )  # [30, 20]\n\n                    # Update closed-loop proprio with last predicted action\n                    proprio_state = proprio_20d.copy()\n                    proprio_state[:9] = raw_actions[-1, :9].copy()\n\n                    actions_7d = decode_action_20d_to_7d(raw_actions)  # [30, 7]\n                    action_queue = list(actions_7d)\n\n                action = action_queue.pop(0)\n                obs, reward, done, info = env.step(action)\n\n                if done or reward > 0.5:\n                    success = True\n                    break\n\n            ep_steps = step_idx + 1\n            task_successes.append(success)\n            task_lengths.append(ep_steps)\n            log.info(\"  Ep %d/%d | %s | steps=%d\",\n                     ep + 1, args.num_episodes,\n                     \"SUCCESS\" if success else \"FAIL\", ep_steps)\n\n            env.close()\n\n        n_succ = sum(task_successes)\n        n_total = len(task_successes)\n        sr = n_succ / n_total if n_total > 0 else 0.0\n\n        all_task_results[task_id] = {\n            \"task_id\": task_id,\n            \"task_description\": task_desc,\n            \"success_count\": n_succ,\n            \"total_episodes\": n_total,\n            \"success_rate\": round(sr, 4),\n            \"mean_steps\": round(float(np.mean(task_lengths)), 1),\n        }\n        total_successes += n_succ\n        total_episodes += n_total\n        log.info(\"  Task %d SR: %d/%d (%.1f%%)\", task_id, n_succ, n_total, sr * 100)\n\n    elapsed = time_mod.time() - eval_start\n    overall_sr = total_successes / total_episodes if total_episodes > 0 else 0.0\n    _, ci_lo, ci_hi = wilson_ci(total_successes, total_episodes)\n\n    log.info(\"=\" * 60)\n    log.info(\"SUITE: %s | MODEL: xvla | keep_ratio: %.2f\", args.suite, args.keep_ratio)\n    log.info(\"Overall SR: %d/%d (%.1f%%)\", total_successes, total_episodes, overall_sr * 100)\n    log.info(\"95%% Wilson CI: [%.1f%%, %.1f%%]\", ci_lo * 100, ci_hi * 100)\n    for tid, tr in sorted(all_task_results.items()):\n        log.info(\"  Task %d: %.0f%% (%d/%d) -- %s\",\n                 tid, tr[\"success_rate\"] * 100, tr[\"success_count\"],\n                 tr[\"total_episodes\"], tr[\"task_description\"])\n    log.info(\"Elapsed: %.1f min\", elapsed / 60)\n    log.info(\"=\" * 60)\n\n    summary = {\n        \"model\": \"xvla\",\n        \"model_path\": args.model_path,\n        \"mode\": \"l2_norm_prune\",\n        \"suite\": args.suite,\n        \"keep_ratio\": args.keep_ratio,\n        \"n_vision_tokens_original\": n_vis_tokens,\n        \"n_vision_tokens_kept\": k_tokens,\n        \"total_episodes\": total_episodes,\n        \"total_successes\": total_successes,\n        \"overall_success_rate\": round(overall_sr, 4),\n        \"wilson_ci_95\": [round(ci_lo, 4), round(ci_hi, 4)],\n        \"num_episodes_per_task\": args.num_episodes,\n        \"max_steps\": max_steps,\n        \"num_actions_per_chunk\": num_actions_per_chunk,\n        \"domain_id\": args.domain_id,\n        \"denoise_steps\": args.denoise_steps,\n        \"seed\": args.seed,\n        \"elapsed_seconds\": round(elapsed, 1),\n        \"per_task\": all_task_results,\n    }\n\n    output_path.parent.mkdir(parents=True, exist_ok=True)\n    with open(output_path, \"w\") as f:\n        json.dump(summary, f, indent=2)\n    log.info(\"Results saved to %s\", output_path)\n\n    return summary\n\n\nif __name__ == \"__main__\":\n    args = parse_args()\n    run_evaluation(args)\n",
      "numLines": 476,
      "startLine": 1,
      "totalLines": 476
    }
  }
}
```

</details>

---

### Assistant

_source line 18_

<details><summary>Logged reasoning block</summary>

```text
Now I understand the current implementation. The pruning logic is in `install_vision_pruning` (line 83-106). It uses L2 norm (`features.norm(dim=-1)` then `norms.topk(k)`) to select tokens.

I need to:
1. Add `--mode` argument to `parse_args()`
2. Modify `install_vision_pruning` to accept and use the `mode` parameter
3. Pass `mode` from args to `install_vision_pruning`

Let me make the changes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a",
  "uuid": "d9df2060-0902-491e-893b-13ce08beceb6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cj5S2HTDkqtTvfLZocvFb5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6774,
      "cache_read_input_tokens": 24799,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6774
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 19_

代码结构清晰。需要改三处：`parse_args` 加参数、`install_vision_pruning` 加 mode 逻辑、调用处传参。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a",
  "uuid": "63dc0530-4829-453b-af64-41ab9d49bc16",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cj5S2HTDkqtTvfLZocvFb5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6774,
      "cache_read_input_tokens": 24799,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6774
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Edit · `toolu_019sTwFRUB8YKkGtCVWSNtQ6`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/eval_xvla_pruning_libero.py",
  "old_string": "    p.add_argument(\"--denoise_steps\", type=int, default=10,\n                   help=\"Flow matching denoising steps\")\n    return p.parse_args()",
  "new_string": "    p.add_argument(\"--denoise_steps\", type=int, default=10,\n                   help=\"Flow matching denoising steps\")\n    p.add_argument(\"--mode\", type=str, default=\"l2_norm\",\n                   choices=[\"l2_norm\", \"random\"],\n                   help=\"Pruning method: l2_norm (keep highest L2 norm tokens) or random (random selection)\")\n    return p.parse_args()"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a",
  "uuid": "01f82203-1de8-4560-96f9-2aeae2822325",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cj5S2HTDkqtTvfLZocvFb5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6774,
      "cache_read_input_tokens": 24799,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6774
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-21T02:21:38.727Z_

<details><summary>↩ Tool result · `toolu_019sTwFRUB8YKkGtCVWSNtQ6`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/eval_xvla_pruning_libero.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a",
  "uuid": "f6618603-a7c0-4bf6-bf67-50354cb4c51f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/eval_xvla_pruning_libero.py",
    "oldString": "    p.add_argument(\"--denoise_steps\", type=int, default=10,\n                   help=\"Flow matching denoising steps\")\n    return p.parse_args()",
    "newString": "    p.add_argument(\"--denoise_steps\", type=int, default=10,\n                   help=\"Flow matching denoising steps\")\n    p.add_argument(\"--mode\", type=str, default=\"l2_norm\",\n                   choices=[\"l2_norm\", \"random\"],\n                   help=\"Pruning method: l2_norm (keep highest L2 norm tokens) or random (random selection)\")\n    return p.parse_args()",
    "originalFile": "\"\"\"X-VLA Vision Token Pruning Evaluation on LIBERO.\n\nPrunes vision tokens by L2 norm after Florence2's image encoder + linear projection,\nbefore they enter the Florence2 language encoder. Evaluates on LIBERO suites.\n\nFollows official X-VLA evaluation protocol:\n  - Absolute EEF control (use_delta=False)\n  - 20D action space: [arm1: pos(3)+rot6d(6)+grip(1)] + [arm2: zeros(10)]\n  - 20D proprio: [pos(3)+rot6d(6)+0.0] + zeros(10)\n  - domain_id=3 for LIBERO\n  - Closed-loop proprio update from last predicted action\n\nUsage:\n    CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl python eval_xvla_pruning_libero.py \\\n        --model_path /path/to/X-VLA-Libero \\\n        --suite libero_object \\\n        --keep_ratio 0.5 \\\n        --num_episodes 50 \\\n        --gpu 0\n\"\"\"\n\nfrom __future__ import annotations\n\nimport argparse\nimport json\nimport logging\nimport os\nimport sys\nimport time as time_mod\nfrom pathlib import Path\nfrom functools import wraps\n\nos.environ.setdefault(\"MUJOCO_GL\", \"egl\")\n\nimport numpy as np\nimport torch\nfrom PIL import Image\n\nsys.path.insert(0, str(Path(__file__).resolve().parent))\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    datefmt=\"%Y-%m-%d %H:%M:%S\",\n)\nlog = logging.getLogger(__name__)\n\nSUITE_MAX_STEPS = {\n    \"libero_spatial\": 800,\n    \"libero_object\": 800,\n    \"libero_goal\": 800,\n    \"libero_10\": 900,\n    \"libero_90\": 800,\n}\n\nEPS = 1e-6\n\n\ndef parse_args():\n    p = argparse.ArgumentParser(description=\"X-VLA pruning eval on LIBERO\")\n    p.add_argument(\"--model_path\", type=str, default=\"2toINF/X-VLA-Libero\",\n                   help=\"HuggingFace model path or local dir\")\n    p.add_argument(\"--suite\", type=str, default=\"libero_object\",\n                   choices=list(SUITE_MAX_STEPS.keys()))\n    p.add_argument(\"--keep_ratio\", type=float, default=1.0,\n                   help=\"Fraction of vision tokens to keep (1.0 = no pruning)\")\n    p.add_argument(\"--num_episodes\", type=int, default=50)\n    p.add_argument(\"--gpu\", type=int, default=0)\n    p.add_argument(\"--seed\", type=int, default=42)\n    p.add_argument(\"--max_steps\", type=int, default=None)\n    p.add_argument(\"--output\", type=str, default=None)\n    p.add_argument(\"--task_ids\", type=str, default=None)\n    p.add_argument(\"--domain_id\", type=int, default=3)\n    p.add_argument(\"--denoise_steps\", type=int, default=10,\n                   help=\"Flow matching denoising steps\")\n    return p.parse_args()\n\n\n# ---------------------------------------------------------------------------\n# Pruning hook\n# ---------------------------------------------------------------------------\n\ndef install_vision_pruning(model, keep_ratio: float):\n    if keep_ratio >= 1.0:\n        log.info(\"keep_ratio=%.2f, no pruning applied\", keep_ratio)\n        return\n\n    original_encode = model.vlm._encode_image\n\n    @wraps(original_encode)\n    def pruned_encode(pixel_values):\n        features = original_encode(pixel_values)\n        N = features.shape[1]\n        k = max(1, int(keep_ratio * N))\n        if k >= N:\n            return features\n        norms = features.norm(dim=-1)\n        _, indices = norms.topk(k, dim=-1)\n        indices_sorted = indices.sort(dim=-1).values\n        pruned = features.gather(\n            1, indices_sorted.unsqueeze(-1).expand(-1, -1, features.shape[-1])\n        )\n        return pruned\n\n    model.vlm._encode_image = pruned_encode\n    log.info(\"Vision pruning installed: keep_ratio=%.2f\", keep_ratio)\n\n\n# ---------------------------------------------------------------------------\n# Model loading\n# ---------------------------------------------------------------------------\n\ndef load_model(model_path: str, device: torch.device):\n    model_dir = str(Path(model_path).resolve())\n    sys.path.insert(0, model_dir)\n\n    from configuration_xvla import XVLAConfig\n    from modeling_xvla import XVLA\n    from processing_xvla import XVLAProcessor\n    from safetensors.torch import load_file\n\n    log.info(\"Loading X-VLA from %s\", model_dir)\n    config = XVLAConfig.from_pretrained(model_dir)\n    model = XVLA(config)\n\n    safetensors_path = Path(model_dir) / \"model.safetensors\"\n    if safetensors_path.exists():\n        state_dict = load_file(str(safetensors_path))\n    else:\n        import torch as _torch\n        state_dict = _torch.load(Path(model_dir) / \"pytorch_model.bin\", map_location=\"cpu\")\n    model.load_state_dict(state_dict, strict=False)\n    model = model.to(device).eval()\n\n    processor = XVLAProcessor.from_pretrained(model_dir, trust_remote_code=True)\n    if processor.tokenizer.pad_token is None:\n        processor.tokenizer.pad_token = \"&lt;pad>\"\n        processor.tokenizer.pad_token_id = 1\n\n    n_params = sum(p.numel() for p in model.parameters())\n    log.info(\"Model loaded: %.1fM params, dtype=%s\", n_params / 1e6, model.dtype)\n    return model, processor\n\n\n# ---------------------------------------------------------------------------\n# 6D rotation utilities (following X-VLA's convention)\n# ---------------------------------------------------------------------------\n\ndef mat_to_rot6d(R: np.ndarray) -> np.ndarray:\n    \"\"\"Extract 6D rotation from 3x3 rotation matrix: first two columns.\"\"\"\n    return np.concatenate([R[:3, 0], R[:3, 1]], axis=-1).astype(np.float32)\n\n\ndef rot6d_to_axis_angle(r6d: np.ndarray) -> np.ndarray:\n    \"\"\"Convert 6D rotation representation to axis-angle via Gram-Schmidt.\"\"\"\n    import robosuite.utils.transform_utils as T\n\n    single = r6d.ndim == 1\n    if single:\n        r6d = r6d[None, :]\n\n    a1 = r6d[:, 0:3]\n    a2 = r6d[:, 3:6]\n\n    b1 = a1 / (np.linalg.norm(a1, axis=-1, keepdims=True) + EPS)\n    dot_prod = np.sum(b1 * a2, axis=-1, keepdims=True)\n    b2_orth = a2 - dot_prod * b1\n    b2 = b2_orth / (np.linalg.norm(b2_orth, axis=-1, keepdims=True) + EPS)\n    b3 = np.cross(b1, b2, axis=-1)\n\n    R = np.stack([b1, b2, b3], axis=-1)  # (N, 3, 3)\n\n    results = []\n    for i in range(R.shape[0]):\n        quat = T.mat2quat(R[i])\n        aa = T.quat2axisangle(quat)\n        results.append(aa)\n\n    result = np.stack(results, axis=0)\n    return result[0] if single else result\n\n\n# ---------------------------------------------------------------------------\n# Observation processing\n# ---------------------------------------------------------------------------\n\ndef extract_proprio_20d(env) -> np.ndarray:\n    \"\"\"Extract 20D proprio: [pos(3)+rot6d(6)+0.0] + zeros(10) from env robot state.\"\"\"\n    robot = env.env.robots[0]\n    ee_pos = robot.controller.ee_pos.copy()         # (3,)\n    ee_ori_mat = robot.controller.ee_ori_mat.copy()  # (3, 3)\n    ee_rot6d = mat_to_rot6d(ee_ori_mat)              # (6,)\n\n    arm1 = np.concatenate([ee_pos, ee_rot6d, np.array([0.0], dtype=np.float32)])  # (10,)\n    arm2 = np.zeros(10, dtype=np.float32)\n    return np.concatenate([arm1, arm2])  # (20,)\n\n\ndef decode_action_20d_to_7d(action_20d: np.ndarray) -> np.ndarray:\n    \"\"\"Convert 20D X-VLA action to 7D LIBERO action.\n\n    Input:  [pos(3), rot6d(6), grip(1), arm2(10)]  — only arm1 used\n    Output: [pos(3), axis_angle(3), grip(1)]\n    \"\"\"\n    single = action_20d.ndim == 1\n    if single:\n        action_20d = action_20d[None, :]\n\n    pos = action_20d[:, :3]\n    rot6d = action_20d[:, 3:9]\n    grip = action_20d[:, 9:10]\n\n    axis_angle = rot6d_to_axis_angle(rot6d)\n\n    # Discretize gripper: >0.5 → 1.0 (open), else -1.0 (close)\n    grip_disc = np.where(grip > 0.5, 1.0, -1.0)\n\n    result = np.concatenate([pos, axis_angle, grip_disc], axis=-1).astype(np.float32)\n    return result[0] if single else result\n\n\ndef get_images_from_obs(obs) -> list:\n    \"\"\"Extract camera images from LIBERO observation, apply agentview flip.\"\"\"\n    images = []\n    for cam_name in [\"agentview_image\", \"robot0_eye_in_hand_image\"]:\n        img = obs.get(cam_name, None)\n        if img is None:\n            for k, v in obs.items():\n                if cam_name in k and isinstance(v, np.ndarray):\n                    img = v\n                    break\n        if img is not None:\n            if img.dtype in (np.float32, np.float64):\n                img = (np.clip(img, 0, 1) * 255).astype(np.uint8)\n            if cam_name == \"agentview_image\":\n                img = np.flip(np.flip(img, 0), 1).copy()\n            images.append(Image.fromarray(img))\n    return images\n\n\n# ---------------------------------------------------------------------------\n# Action prediction\n# ---------------------------------------------------------------------------\n\n@torch.no_grad()\ndef predict_actions(model, processor, images, task_desc, proprio_20d, domain_id,\n                    device, denoise_steps=10):\n    inputs = processor(images=images, language_instruction=task_desc)\n\n    proprio_t = torch.tensor(proprio_20d, dtype=torch.float32).unsqueeze(0).to(device)\n    domain_t = torch.tensor([domain_id], dtype=torch.long).to(device)\n\n    for k, v in inputs.items():\n        if isinstance(v, torch.Tensor):\n            if v.is_floating_point():\n                inputs[k] = v.to(device=device, dtype=torch.float32)\n            else:\n                inputs[k] = v.to(device=device)\n\n    actions = model.generate_actions(\n        input_ids=inputs[\"input_ids\"],\n        image_input=inputs[\"image_input\"],\n        image_mask=inputs[\"image_mask\"],\n        proprio=proprio_t,\n        domain_id=domain_t,\n        steps=denoise_steps,\n    )  # [1, 30, 20]\n\n    return actions.squeeze(0).float().cpu().numpy()  # [30, 20]\n\n\n# ---------------------------------------------------------------------------\n# Wilson CI\n# ---------------------------------------------------------------------------\n\ndef wilson_ci(successes, total, z=1.96):\n    if total == 0:\n        return 0.0, 0.0, 1.0\n    p = successes / total\n    denom = 1 + z ** 2 / total\n    center = (p + z ** 2 / (2 * total)) / denom\n    spread = z * np.sqrt((p * (1 - p) + z ** 2 / (4 * total)) / total) / denom\n    return center, max(0.0, center - spread), min(1.0, center + spread)\n\n\n# ---------------------------------------------------------------------------\n# Main evaluation\n# ---------------------------------------------------------------------------\n\ndef run_evaluation(args):\n    device = torch.device(f\"cuda:{args.gpu}\" if torch.cuda.is_available() else \"cpu\")\n    max_steps = args.max_steps or SUITE_MAX_STEPS.get(args.suite, 800)\n    output_path = Path(args.output or\n                       f\"eval_results/xvla_prune_k{args.keep_ratio}_{args.suite}.json\")\n\n    log.info(\"Suite: %s | Device: %s | keep_ratio=%.2f | Episodes/task: %d | Max steps: %d\",\n             args.suite, device, args.keep_ratio, args.num_episodes, max_steps)\n\n    np.random.seed(args.seed)\n    torch.manual_seed(args.seed)\n\n    t0 = time_mod.time()\n    model, processor = load_model(args.model_path, device)\n    log.info(\"Model loaded in %.1fs\", time_mod.time() - t0)\n\n    dummy_img = torch.randn(1, 3, 224, 224, device=device)\n    with torch.no_grad():\n        dummy_feats = model.vlm._encode_image(dummy_img)\n    n_vis_tokens = dummy_feats.shape[1]\n    k_tokens = max(1, int(args.keep_ratio * n_vis_tokens))\n    log.info(\"Vision tokens: %d total, keeping %d (%.0f%%)\",\n             n_vis_tokens, k_tokens, args.keep_ratio * 100)\n\n    install_vision_pruning(model, args.keep_ratio)\n\n    num_actions_per_chunk = model.num_actions  # 30\n\n    # LIBERO setup — use OffScreenRenderEnv directly (matching official X-VLA eval)\n    from libero.libero import benchmark, get_libero_path\n    from libero.libero.envs import OffScreenRenderEnv\n\n    task_suite = benchmark.get_benchmark(args.suite)()\n    n_tasks = task_suite.n_tasks\n\n    if args.task_ids:\n        task_id_list = [int(x) for x in args.task_ids.split(\",\")]\n    else:\n        task_id_list = list(range(n_tasks))\n\n    eval_start = time_mod.time()\n    all_task_results = {}\n    total_successes = 0\n    total_episodes = 0\n\n    for task_id in task_id_list:\n        task = task_suite.get_task(task_id)\n        task_desc = task.language\n        task_bddl = os.path.join(\n            get_libero_path(\"bddl_files\"), task.problem_folder, task.bddl_file\n        )\n        log.info(\"--- Task %d: %s ---\", task_id, task_desc)\n\n        init_states = task_suite.get_task_init_states(task_id)\n\n        task_successes = []\n        task_lengths = []\n\n        for ep in range(args.num_episodes):\n            env = OffScreenRenderEnv(\n                bddl_file_name=task_bddl,\n                camera_heights=256,\n                camera_widths=256,\n            )\n            env.seed(args.seed + ep + 100)\n            obs = env.reset()\n\n            init_state_id = ep % init_states.shape[0]\n            obs = env.set_init_state(init_states[init_state_id])\n\n            # Settle the robot with neutral actions\n            for _ in range(10):\n                neutral = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0], dtype=np.float32)\n                obs, _, _, _ = env.step(neutral)\n\n            # Switch to absolute control\n            for robot in env.env.robots:\n                robot.controller.use_delta = False\n\n            action_queue = []\n            proprio_state = None\n            success = False\n\n            for step_idx in range(max_steps):\n                if not action_queue:\n                    # Extract proprio from env\n                    proprio_20d = extract_proprio_20d(env)\n                    if proprio_state is not None:\n                        proprio_20d[:9] = proprio_state[:9]\n\n                    images = get_images_from_obs(obs)\n                    if not images:\n                        raise ValueError(f\"No images found in obs keys: {list(obs.keys())}\")\n\n                    raw_actions = predict_actions(\n                        model, processor, images, task_desc, proprio_20d,\n                        args.domain_id, device, args.denoise_steps,\n                    )  # [30, 20]\n\n                    # Update closed-loop proprio with last predicted action\n                    proprio_state = proprio_20d.copy()\n                    proprio_state[:9] = raw_actions[-1, :9].copy()\n\n                    actions_7d = decode_action_20d_to_7d(raw_actions)  # [30, 7]\n                    action_queue = list(actions_7d)\n\n                action = action_queue.pop(0)\n                obs, reward, done, info = env.step(action)\n\n                if done or reward > 0.5:\n                    success = True\n                    break\n\n            ep_steps = step_idx + 1\n            task_successes.append(success)\n            task_lengths.append(ep_steps)\n            log.info(\"  Ep %d/%d | %s | steps=%d\",\n                     ep + 1, args.num_episodes,\n                     \"SUCCESS\" if success else \"FAIL\", ep_steps)\n\n            env.close()\n\n        n_succ = sum(task_successes)\n        n_total = len(task_successes)\n        sr = n_succ / n_total if n_total > 0 else 0.0\n\n        all_task_results[task_id] = {\n            \"task_id\": task_id,\n            \"task_description\": task_desc,\n            \"success_count\": n_succ,\n            \"total_episodes\": n_total,\n            \"success_rate\": round(sr, 4),\n            \"mean_steps\": round(float(np.mean(task_lengths)), 1),\n        }\n        total_successes += n_succ\n        total_episodes += n_total\n        log.info(\"  Task %d SR: %d/%d (%.1f%%)\", task_id, n_succ, n_total, sr * 100)\n\n    elapsed = time_mod.time() - eval_start\n    overall_sr = total_successes / total_episodes if total_episodes > 0 else 0.0\n    _, ci_lo, ci_hi = wilson_ci(total_successes, total_episodes)\n\n    log.info(\"=\" * 60)\n    log.info(\"SUITE: %s | MODEL: xvla | keep_ratio: %.2f\", args.suite, args.keep_ratio)\n    log.info(\"Overall SR: %d/%d (%.1f%%)\", total_successes, total_episodes, overall_sr * 100)\n    log.info(\"95%% Wilson CI: [%.1f%%, %.1f%%]\", ci_lo * 100, ci_hi * 100)\n    for tid, tr in sorted(all_task_results.items()):\n        log.info(\"  Task %d: %.0f%% (%d/%d) -- %s\",\n                 tid, tr[\"success_rate\"] * 100, tr[\"success_count\"],\n                 tr[\"total_episodes\"], tr[\"task_description\"])\n    log.info(\"Elapsed: %.1f min\", elapsed / 60)\n    log.info(\"=\" * 60)\n\n    summary = {\n        \"model\": \"xvla\",\n        \"model_path\": args.model_path,\n        \"mode\": \"l2_norm_prune\",\n        \"suite\": args.suite,\n        \"keep_ratio\": args.keep_ratio,\n        \"n_vision_tokens_original\": n_vis_tokens,\n        \"n_vision_tokens_kept\": k_tokens,\n        \"total_episodes\": total_episodes,\n        \"total_successes\": total_successes,\n        \"overall_success_rate\": round(overall_sr, 4),\n        \"wilson_ci_95\": [round(ci_lo, 4), round(ci_hi, 4)],\n        \"num_episodes_per_task\": args.num_episodes,\n        \"max_steps\": max_steps,\n        \"num_actions_per_chunk\": num_actions_per_chunk,\n        \"domain_id\": args.domain_id,\n        \"denoise_steps\": args.denoise_steps,\n        \"seed\": args.seed,\n        \"elapsed_seconds\": round(elapsed, 1),\n        \"per_task\": all_task_results,\n    }\n\n    output_path.parent.mkdir(parents=True, exist_ok=True)\n    with open(output_path, \"w\") as f:\n        json.dump(summary, f, indent=2)\n    log.info(\"Results saved to %s\", output_path)\n\n    return summary\n\n\nif __name__ == \"__main__\":\n    args = parse_args()\n    run_evaluation(args)\n",
    "structuredPatch": [
      {
        "oldStart": 73,
        "oldLines": 6,
        "newStart": 73,
        "newLines": 9,
        "lines": [
          "     p.add_argument(\"--domain_id\", type=int, default=3)",
          "     p.add_argument(\"--denoise_steps\", type=int, default=10,",
          "                    help=\"Flow matching denoising steps\")",
          "+    p.add_argument(\"--mode\", type=str, default=\"l2_norm\",",
          "+                   choices=[\"l2_norm\", \"random\"],",
          "+                   help=\"Pruning method: l2_norm (keep highest L2 norm tokens) or random (random selection)\")",
          "     return p.parse_args()",
          " ",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Edit · `toolu_01TcqEGxZST4KrN7bFbtxAuz`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/eval_xvla_pruning_libero.py",
  "old_string": "def install_vision_pruning(model, keep_ratio: float):\n    if keep_ratio >= 1.0:\n        log.info(\"keep_ratio=%.2f, no pruning applied\", keep_ratio)\n        return\n\n    original_encode = model.vlm._encode_image\n\n    @wraps(original_encode)\n    def pruned_encode(pixel_values):\n        features = original_encode(pixel_values)\n        N = features.shape[1]\n        k = max(1, int(keep_ratio * N))\n        if k >= N:\n            return features\n        norms = features.norm(dim=-1)\n        _, indices = norms.topk(k, dim=-1)\n        indices_sorted = indices.sort(dim=-1).values\n        pruned = features.gather(\n            1, indices_sorted.unsqueeze(-1).expand(-1, -1, features.shape[-1])\n        )\n        return pruned\n\n    model.vlm._encode_image = pruned_encode\n    log.info(\"Vision pruning installed: keep_ratio=%.2f\", keep_ratio)",
  "new_string": "def install_vision_pruning(model, keep_ratio: float, mode: str = \"l2_norm\"):\n    if keep_ratio >= 1.0:\n        log.info(\"keep_ratio=%.2f, no pruning applied\", keep_ratio)\n        return\n\n    original_encode = model.vlm._encode_image\n\n    @wraps(original_encode)\n    def pruned_encode(pixel_values):\n        features = original_encode(pixel_values)\n        N = features.shape[1]\n        k = max(1, int(keep_ratio * N))\n        if k >= N:\n            return features\n        if mode == \"l2_norm\":\n            norms = features.norm(dim=-1)\n            _, indices = norms.topk(k, dim=-1)\n        elif mode == \"random\":\n            indices = torch.stack([\n                torch.randperm(N, device=features.device)[:k]\n                for _ in range(features.shape[0])\n            ], dim=0)\n        indices_sorted = indices.sort(dim=-1).values\n        pruned = features.gather(\n            1, indices_sorted.unsqueeze(-1).expand(-1, -1, features.shape[-1])\n        )\n        return pruned\n\n    model.vlm._encode_image = pruned_encode\n    log.info(\"Vision pruning installed: keep_ratio=%.2f, mode=%s\", keep_ratio, mode)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a",
  "uuid": "5e1683eb-7e47-44d8-9402-d2bd94d43020",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DM6tRdvRZvwJuAqRLyFXQf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 560,
      "cache_read_input_tokens": 31573,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 560
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-21T02:21:49.662Z_

<details><summary>↩ Tool result · `toolu_01TcqEGxZST4KrN7bFbtxAuz`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/eval_xvla_pruning_libero.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a",
  "uuid": "618e737c-9fec-4003-88f3-7a8c2b2a68d1",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/eval_xvla_pruning_libero.py",
    "oldString": "def install_vision_pruning(model, keep_ratio: float):\n    if keep_ratio >= 1.0:\n        log.info(\"keep_ratio=%.2f, no pruning applied\", keep_ratio)\n        return\n\n    original_encode = model.vlm._encode_image\n\n    @wraps(original_encode)\n    def pruned_encode(pixel_values):\n        features = original_encode(pixel_values)\n        N = features.shape[1]\n        k = max(1, int(keep_ratio * N))\n        if k >= N:\n            return features\n        norms = features.norm(dim=-1)\n        _, indices = norms.topk(k, dim=-1)\n        indices_sorted = indices.sort(dim=-1).values\n        pruned = features.gather(\n            1, indices_sorted.unsqueeze(-1).expand(-1, -1, features.shape[-1])\n        )\n        return pruned\n\n    model.vlm._encode_image = pruned_encode\n    log.info(\"Vision pruning installed: keep_ratio=%.2f\", keep_ratio)",
    "newString": "def install_vision_pruning(model, keep_ratio: float, mode: str = \"l2_norm\"):\n    if keep_ratio >= 1.0:\n        log.info(\"keep_ratio=%.2f, no pruning applied\", keep_ratio)\n        return\n\n    original_encode = model.vlm._encode_image\n\n    @wraps(original_encode)\n    def pruned_encode(pixel_values):\n        features = original_encode(pixel_values)\n        N = features.shape[1]\n        k = max(1, int(keep_ratio * N))\n        if k >= N:\n            return features\n        if mode == \"l2_norm\":\n            norms = features.norm(dim=-1)\n            _, indices = norms.topk(k, dim=-1)\n        elif mode == \"random\":\n            indices = torch.stack([\n                torch.randperm(N, device=features.device)[:k]\n                for _ in range(features.shape[0])\n            ], dim=0)\n        indices_sorted = indices.sort(dim=-1).values\n        pruned = features.gather(\n            1, indices_sorted.unsqueeze(-1).expand(-1, -1, features.shape[-1])\n        )\n        return pruned\n\n    model.vlm._encode_image = pruned_encode\n    log.info(\"Vision pruning installed: keep_ratio=%.2f, mode=%s\", keep_ratio, mode)",
    "originalFile": "\"\"\"X-VLA Vision Token Pruning Evaluation on LIBERO.\n\nPrunes vision tokens by L2 norm after Florence2's image encoder + linear projection,\nbefore they enter the Florence2 language encoder. Evaluates on LIBERO suites.\n\nFollows official X-VLA evaluation protocol:\n  - Absolute EEF control (use_delta=False)\n  - 20D action space: [arm1: pos(3)+rot6d(6)+grip(1)] + [arm2: zeros(10)]\n  - 20D proprio: [pos(3)+rot6d(6)+0.0] + zeros(10)\n  - domain_id=3 for LIBERO\n  - Closed-loop proprio update from last predicted action\n\nUsage:\n    CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl python eval_xvla_pruning_libero.py \\\n        --model_path /path/to/X-VLA-Libero \\\n        --suite libero_object \\\n        --keep_ratio 0.5 \\\n        --num_episodes 50 \\\n        --gpu 0\n\"\"\"\n\nfrom __future__ import annotations\n\nimport argparse\nimport json\nimport logging\nimport os\nimport sys\nimport time as time_mod\nfrom pathlib import Path\nfrom functools import wraps\n\nos.environ.setdefault(\"MUJOCO_GL\", \"egl\")\n\nimport numpy as np\nimport torch\nfrom PIL import Image\n\nsys.path.insert(0, str(Path(__file__).resolve().parent))\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    datefmt=\"%Y-%m-%d %H:%M:%S\",\n)\nlog = logging.getLogger(__name__)\n\nSUITE_MAX_STEPS = {\n    \"libero_spatial\": 800,\n    \"libero_object\": 800,\n    \"libero_goal\": 800,\n    \"libero_10\": 900,\n    \"libero_90\": 800,\n}\n\nEPS = 1e-6\n\n\ndef parse_args():\n    p = argparse.ArgumentParser(description=\"X-VLA pruning eval on LIBERO\")\n    p.add_argument(\"--model_path\", type=str, default=\"2toINF/X-VLA-Libero\",\n                   help=\"HuggingFace model path or local dir\")\n    p.add_argument(\"--suite\", type=str, default=\"libero_object\",\n                   choices=list(SUITE_MAX_STEPS.keys()))\n    p.add_argument(\"--keep_ratio\", type=float, default=1.0,\n                   help=\"Fraction of vision tokens to keep (1.0 = no pruning)\")\n    p.add_argument(\"--num_episodes\", type=int, default=50)\n    p.add_argument(\"--gpu\", type=int, default=0)\n    p.add_argument(\"--seed\", type=int, default=42)\n    p.add_argument(\"--max_steps\", type=int, default=None)\n    p.add_argument(\"--output\", type=str, default=None)\n    p.add_argument(\"--task_ids\", type=str, default=None)\n    p.add_argument(\"--domain_id\", type=int, default=3)\n    p.add_argument(\"--denoise_steps\", type=int, default=10,\n                   help=\"Flow matching denoising steps\")\n    p.add_argument(\"--mode\", type=str, default=\"l2_norm\",\n                   choices=[\"l2_norm\", \"random\"],\n                   help=\"Pruning method: l2_norm (keep highest L2 norm tokens) or random (random selection)\")\n    return p.parse_args()\n\n\n# ---------------------------------------------------------------------------\n# Pruning hook\n# ---------------------------------------------------------------------------\n\ndef install_vision_pruning(model, keep_ratio: float):\n    if keep_ratio >= 1.0:\n        log.info(\"keep_ratio=%.2f, no pruning applied\", keep_ratio)\n        return\n\n    original_encode = model.vlm._encode_image\n\n    @wraps(original_encode)\n    def pruned_encode(pixel_values):\n        features = original_encode(pixel_values)\n        N = features.shape[1]\n        k = max(1, int(keep_ratio * N))\n        if k >= N:\n            return features\n        norms = features.norm(dim=-1)\n        _, indices = norms.topk(k, dim=-1)\n        indices_sorted = indices.sort(dim=-1).values\n        pruned = features.gather(\n            1, indices_sorted.unsqueeze(-1).expand(-1, -1, features.shape[-1])\n        )\n        return pruned\n\n    model.vlm._encode_image = pruned_encode\n    log.info(\"Vision pruning installed: keep_ratio=%.2f\", keep_ratio)\n\n\n# ---------------------------------------------------------------------------\n# Model loading\n# ---------------------------------------------------------------------------\n\ndef load_model(model_path: str, device: torch.device):\n    model_dir = str(Path(model_path).resolve())\n    sys.path.insert(0, model_dir)\n\n    from configuration_xvla import XVLAConfig\n    from modeling_xvla import XVLA\n    from processing_xvla import XVLAProcessor\n    from safetensors.torch import load_file\n\n    log.info(\"Loading X-VLA from %s\", model_dir)\n    config = XVLAConfig.from_pretrained(model_dir)\n    model = XVLA(config)\n\n    safetensors_path = Path(model_dir) / \"model.safetensors\"\n    if safetensors_path.exists():\n        state_dict = load_file(str(safetensors_path))\n    else:\n        import torch as _torch\n        state_dict = _torch.load(Path(model_dir) / \"pytorch_model.bin\", map_location=\"cpu\")\n    model.load_state_dict(state_dict, strict=False)\n    model = model.to(device).eval()\n\n    processor = XVLAProcessor.from_pretrained(model_dir, trust_remote_code=True)\n    if processor.tokenizer.pad_token is None:\n        processor.tokenizer.pad_token = \"&lt;pad>\"\n        processor.tokenizer.pad_token_id = 1\n\n    n_params = sum(p.numel() for p in model.parameters())\n    log.info(\"Model loaded: %.1fM params, dtype=%s\", n_params / 1e6, model.dtype)\n    return model, processor\n\n\n# ---------------------------------------------------------------------------\n# 6D rotation utilities (following X-VLA's convention)\n# ---------------------------------------------------------------------------\n\ndef mat_to_rot6d(R: np.ndarray) -> np.ndarray:\n    \"\"\"Extract 6D rotation from 3x3 rotation matrix: first two columns.\"\"\"\n    return np.concatenate([R[:3, 0], R[:3, 1]], axis=-1).astype(np.float32)\n\n\ndef rot6d_to_axis_angle(r6d: np.ndarray) -> np.ndarray:\n    \"\"\"Convert 6D rotation representation to axis-angle via Gram-Schmidt.\"\"\"\n    import robosuite.utils.transform_utils as T\n\n    single = r6d.ndim == 1\n    if single:\n        r6d = r6d[None, :]\n\n    a1 = r6d[:, 0:3]\n    a2 = r6d[:, 3:6]\n\n    b1 = a1 / (np.linalg.norm(a1, axis=-1, keepdims=True) + EPS)\n    dot_prod = np.sum(b1 * a2, axis=-1, keepdims=True)\n    b2_orth = a2 - dot_prod * b1\n    b2 = b2_orth / (np.linalg.norm(b2_orth, axis=-1, keepdims=True) + EPS)\n    b3 = np.cross(b1, b2, axis=-1)\n\n    R = np.stack([b1, b2, b3], axis=-1)  # (N, 3, 3)\n\n    results = []\n    for i in range(R.shape[0]):\n        quat = T.mat2quat(R[i])\n        aa = T.quat2axisangle(quat)\n        results.append(aa)\n\n    result = np.stack(results, axis=0)\n    return result[0] if single else result\n\n\n# ---------------------------------------------------------------------------\n# Observation processing\n# ---------------------------------------------------------------------------\n\ndef extract_proprio_20d(env) -> np.ndarray:\n    \"\"\"Extract 20D proprio: [pos(3)+rot6d(6)+0.0] + zeros(10) from env robot state.\"\"\"\n    robot = env.env.robots[0]\n    ee_pos = robot.controller.ee_pos.copy()         # (3,)\n    ee_ori_mat = robot.controller.ee_ori_mat.copy()  # (3, 3)\n    ee_rot6d = mat_to_rot6d(ee_ori_mat)              # (6,)\n\n    arm1 = np.concatenate([ee_pos, ee_rot6d, np.array([0.0], dtype=np.float32)])  # (10,)\n    arm2 = np.zeros(10, dtype=np.float32)\n    return np.concatenate([arm1, arm2])  # (20,)\n\n\ndef decode_action_20d_to_7d(action_20d: np.ndarray) -> np.ndarray:\n    \"\"\"Convert 20D X-VLA action to 7D LIBERO action.\n\n    Input:  [pos(3), rot6d(6), grip(1), arm2(10)]  — only arm1 used\n    Output: [pos(3), axis_angle(3), grip(1)]\n    \"\"\"\n    single = action_20d.ndim == 1\n    if single:\n        action_20d = action_20d[None, :]\n\n    pos = action_20d[:, :3]\n    rot6d = action_20d[:, 3:9]\n    grip = action_20d[:, 9:10]\n\n    axis_angle = rot6d_to_axis_angle(rot6d)\n\n    # Discretize gripper: >0.5 → 1.0 (open), else -1.0 (close)\n    grip_disc = np.where(grip > 0.5, 1.0, -1.0)\n\n    result = np.concatenate([pos, axis_angle, grip_disc], axis=-1).astype(np.float32)\n    return result[0] if single else result\n\n\ndef get_images_from_obs(obs) -> list:\n    \"\"\"Extract camera images from LIBERO observation, apply agentview flip.\"\"\"\n    images = []\n    for cam_name in [\"agentview_image\", \"robot0_eye_in_hand_image\"]:\n        img = obs.get(cam_name, None)\n        if img is None:\n            for k, v in obs.items():\n                if cam_name in k and isinstance(v, np.ndarray):\n                    img = v\n                    break\n        if img is not None:\n            if img.dtype in (np.float32, np.float64):\n                img = (np.clip(img, 0, 1) * 255).astype(np.uint8)\n            if cam_name == \"agentview_image\":\n                img = np.flip(np.flip(img, 0), 1).copy()\n            images.append(Image.fromarray(img))\n    return images\n\n\n# ---------------------------------------------------------------------------\n# Action prediction\n# ---------------------------------------------------------------------------\n\n@torch.no_grad()\ndef predict_actions(model, processor, images, task_desc, proprio_20d, domain_id,\n                    device, denoise_steps=10):\n    inputs = processor(images=images, language_instruction=task_desc)\n\n    proprio_t = torch.tensor(proprio_20d, dtype=torch.float32).unsqueeze(0).to(device)\n    domain_t = torch.tensor([domain_id], dtype=torch.long).to(device)\n\n    for k, v in inputs.items():\n        if isinstance(v, torch.Tensor):\n            if v.is_floating_point():\n                inputs[k] = v.to(device=device, dtype=torch.float32)\n            else:\n                inputs[k] = v.to(device=device)\n\n    actions = model.generate_actions(\n        input_ids=inputs[\"input_ids\"],\n        image_input=inputs[\"image_input\"],\n        image_mask=inputs[\"image_mask\"],\n        proprio=proprio_t,\n        domain_id=domain_t,\n        steps=denoise_steps,\n    )  # [1, 30, 20]\n\n    return actions.squeeze(0).float().cpu().numpy()  # [30, 20]\n\n\n# ---------------------------------------------------------------------------\n# Wilson CI\n# ---------------------------------------------------------------------------\n\ndef wilson_ci(successes, total, z=1.96):\n    if total == 0:\n        return 0.0, 0.0, 1.0\n    p = successes / total\n    denom = 1 + z ** 2 / total\n    center = (p + z ** 2 / (2 * total)) / denom\n    spread = z * np.sqrt((p * (1 - p) + z ** 2 / (4 * total)) / total) / denom\n    return center, max(0.0, center - spread), min(1.0, center + spread)\n\n\n# ---------------------------------------------------------------------------\n# Main evaluation\n# ---------------------------------------------------------------------------\n\ndef run_evaluation(args):\n    device = torch.device(f\"cuda:{args.gpu}\" if torch.cuda.is_available() else \"cpu\")\n    max_steps = args.max_steps or SUITE_MAX_STEPS.get(args.suite, 800)\n    output_path = Path(args.output or\n                       f\"eval_results/xvla_prune_k{args.keep_ratio}_{args.suite}.json\")\n\n    log.info(\"Suite: %s | Device: %s | keep_ratio=%.2f | Episodes/task: %d | Max steps: %d\",\n             args.suite, device, args.keep_ratio, args.num_episodes, max_steps)\n\n    np.random.seed(args.seed)\n    torch.manual_seed(args.seed)\n\n    t0 = time_mod.time()\n    model, processor = load_model(args.model_path, device)\n    log.info(\"Model loaded in %.1fs\", time_mod.time() - t0)\n\n    dummy_img = torch.randn(1, 3, 224, 224, device=device)\n    with torch.no_grad():\n        dummy_feats = model.vlm._encode_image(dummy_img)\n    n_vis_tokens = dummy_feats.shape[1]\n    k_tokens = max(1, int(args.keep_ratio * n_vis_tokens))\n    log.info(\"Vision tokens: %d total, keeping %d (%.0f%%)\",\n             n_vis_tokens, k_tokens, args.keep_ratio * 100)\n\n    install_vision_pruning(model, args.keep_ratio)\n\n    num_actions_per_chunk = model.num_actions  # 30\n\n    # LIBERO setup — use OffScreenRenderEnv directly (matching official X-VLA eval)\n    from libero.libero import benchmark, get_libero_path\n    from libero.libero.envs import OffScreenRenderEnv\n\n    task_suite = benchmark.get_benchmark(args.suite)()\n    n_tasks = task_suite.n_tasks\n\n    if args.task_ids:\n        task_id_list = [int(x) for x in args.task_ids.split(\",\")]\n    else:\n        task_id_list = list(range(n_tasks))\n\n    eval_start = time_mod.time()\n    all_task_results = {}\n    total_successes = 0\n    total_episodes = 0\n\n    for task_id in task_id_list:\n        task = task_suite.get_task(task_id)\n        task_desc = task.language\n        task_bddl = os.path.join(\n            get_libero_path(\"bddl_files\"), task.problem_folder, task.bddl_file\n        )\n        log.info(\"--- Task %d: %s ---\", task_id, task_desc)\n\n        init_states = task_suite.get_task_init_states(task_id)\n\n        task_successes = []\n        task_lengths = []\n\n        for ep in range(args.num_episodes):\n            env = OffScreenRenderEnv(\n                bddl_file_name=task_bddl,\n                camera_heights=256,\n                camera_widths=256,\n            )\n            env.seed(args.seed + ep + 100)\n            obs = env.reset()\n\n            init_state_id = ep % init_states.shape[0]\n            obs = env.set_init_state(init_states[init_state_id])\n\n            # Settle the robot with neutral actions\n            for _ in range(10):\n                neutral = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0], dtype=np.float32)\n                obs, _, _, _ = env.step(neutral)\n\n            # Switch to absolute control\n            for robot in env.env.robots:\n                robot.controller.use_delta = False\n\n            action_queue = []\n            proprio_state = None\n            success = False\n\n            for step_idx in range(max_steps):\n                if not action_queue:\n                    # Extract proprio from env\n                    proprio_20d = extract_proprio_20d(env)\n                    if proprio_state is not None:\n                        proprio_20d[:9] = proprio_state[:9]\n\n                    images = get_images_from_obs(obs)\n                    if not images:\n                        raise ValueError(f\"No images found in obs keys: {list(obs.keys())}\")\n\n                    raw_actions = predict_actions(\n                        model, processor, images, task_desc, proprio_20d,\n                        args.domain_id, device, args.denoise_steps,\n                    )  # [30, 20]\n\n                    # Update closed-loop proprio with last predicted action\n                    proprio_state = proprio_20d.copy()\n                    proprio_state[:9] = raw_actions[-1, :9].copy()\n\n                    actions_7d = decode_action_20d_to_7d(raw_actions)  # [30, 7]\n                    action_queue = list(actions_7d)\n\n                action = action_queue.pop(0)\n                obs, reward, done, info = env.step(action)\n\n                if done or reward > 0.5:\n                    success = True\n                    break\n\n            ep_steps = step_idx + 1\n            task_successes.append(success)\n            task_lengths.append(ep_steps)\n            log.info(\"  Ep %d/%d | %s | steps=%d\",\n                     ep + 1, args.num_episodes,\n                     \"SUCCESS\" if success else \"FAIL\", ep_steps)\n\n            env.close()\n\n        n_succ = sum(task_successes)\n        n_total = len(task_successes)\n        sr = n_succ / n_total if n_total > 0 else 0.0\n\n        all_task_results[task_id] = {\n            \"task_id\": task_id,\n            \"task_description\": task_desc,\n            \"success_count\": n_succ,\n            \"total_episodes\": n_total,\n            \"success_rate\": round(sr, 4),\n            \"mean_steps\": round(float(np.mean(task_lengths)), 1),\n        }\n        total_successes += n_succ\n        total_episodes += n_total\n        log.info(\"  Task %d SR: %d/%d (%.1f%%)\", task_id, n_succ, n_total, sr * 100)\n\n    elapsed = time_mod.time() - eval_start\n    overall_sr = total_successes / total_episodes if total_episodes > 0 else 0.0\n    _, ci_lo, ci_hi = wilson_ci(total_successes, total_episodes)\n\n    log.info(\"=\" * 60)\n    log.info(\"SUITE: %s | MODEL: xvla | keep_ratio: %.2f\", args.suite, args.keep_ratio)\n    log.info(\"Overall SR: %d/%d (%.1f%%)\", total_successes, total_episodes, overall_sr * 100)\n    log.info(\"95%% Wilson CI: [%.1f%%, %.1f%%]\", ci_lo * 100, ci_hi * 100)\n    for tid, tr in sorted(all_task_results.items()):\n        log.info(\"  Task %d: %.0f%% (%d/%d) -- %s\",\n                 tid, tr[\"success_rate\"] * 100, tr[\"success_count\"],\n                 tr[\"total_episodes\"], tr[\"task_description\"])\n    log.info(\"Elapsed: %.1f min\", elapsed / 60)\n    log.info(\"=\" * 60)\n\n    summary = {\n        \"model\": \"xvla\",\n        \"model_path\": args.model_path,\n        \"mode\": \"l2_norm_prune\",\n        \"suite\": args.suite,\n        \"keep_ratio\": args.keep_ratio,\n        \"n_vision_tokens_original\": n_vis_tokens,\n        \"n_vision_tokens_kept\": k_tokens,\n        \"total_episodes\": total_episodes,\n        \"total_successes\": total_successes,\n        \"overall_success_rate\": round(overall_sr, 4),\n        \"wilson_ci_95\": [round(ci_lo, 4), round(ci_hi, 4)],\n        \"num_episodes_per_task\": args.num_episodes,\n        \"max_steps\": max_steps,\n        \"num_actions_per_chunk\": num_actions_per_chunk,\n        \"domain_id\": args.domain_id,\n        \"denoise_steps\": args.denoise_steps,\n        \"seed\": args.seed,\n        \"elapsed_seconds\": round(elapsed, 1),\n        \"per_task\": all_task_results,\n    }\n\n    output_path.parent.mkdir(parents=True, exist_ok=True)\n    with open(output_path, \"w\") as f:\n        json.dump(summary, f, indent=2)\n    log.info(\"Results saved to %s\", output_path)\n\n    return summary\n\n\nif __name__ == \"__main__\":\n    args = parse_args()\n    run_evaluation(args)\n",
    "structuredPatch": [
      {
        "oldStart": 83,
        "oldLines": 7,
        "newStart": 83,
        "newLines": 7,
        "lines": [
          " # Pruning hook",
          " # ---------------------------------------------------------------------------",
          " ",
          "-def install_vision_pruning(model, keep_ratio: float):",
          "+def install_vision_pruning(model, keep_ratio: float, mode: str = \"l2_norm\"):",
          "     if keep_ratio >= 1.0:",
          "         log.info(\"keep_ratio=%.2f, no pruning applied\", keep_ratio)",
          "         return"
        ]
      },
      {
        "oldStart": 97,
        "oldLines": 8,
        "newStart": 97,
        "newLines": 14,
        "lines": [
          "         k = max(1, int(keep_ratio * N))",
          "         if k >= N:",
          "             return features",
          "-        norms = features.norm(dim=-1)",
          "-        _, indices = norms.topk(k, dim=-1)",
          "+        if mode == \"l2_norm\":",
          "+            norms = features.norm(dim=-1)",
          "+            _, indices = norms.topk(k, dim=-1)",
          "+        elif mode == \"random\":",
          "+            indices = torch.stack([",
          "+                torch.randperm(N, device=features.device)[:k]",
          "+                for _ in range(features.shape[0])",
          "+            ], dim=0)",
          "         indices_sorted = indices.sort(dim=-1).values",
          "         pruned = features.gather(",
          "             1, indices_sorted.unsqueeze(-1).expand(-1, -1, features.shape[-1])"
        ]
      },
      {
        "oldStart": 106,
        "oldLines": 7,
        "newStart": 112,
        "newLines": 7,
        "lines": [
          "         return pruned",
          " ",
          "     model.vlm._encode_image = pruned_encode",
          "-    log.info(\"Vision pruning installed: keep_ratio=%.2f\", keep_ratio)",
          "+    log.info(\"Vision pruning installed: keep_ratio=%.2f, mode=%s\", keep_ratio, mode)",
          " ",
          " ",
          " # ---------------------------------------------------------------------------"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Edit · `toolu_019CsyntrL52QQbVGddizY6S`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/eval_xvla_pruning_libero.py",
  "old_string": "    install_vision_pruning(model, args.keep_ratio)",
  "new_string": "    install_vision_pruning(model, args.keep_ratio, args.mode)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a",
  "uuid": "b9b3eaf0-b301-48a3-9435-8768f9eb0f38",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015NffScvmNkmZR4yzTfV1wZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 834,
      "cache_read_input_tokens": 32133,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 834
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-21T02:21:52.943Z_

<details><summary>↩ Tool result · `toolu_019CsyntrL52QQbVGddizY6S`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/eval_xvla_pruning_libero.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a",
  "uuid": "aecd2c84-c4dd-4e02-98bd-1b3e4944dcc2",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/eval_xvla_pruning_libero.py",
    "oldString": "    install_vision_pruning(model, args.keep_ratio)",
    "newString": "    install_vision_pruning(model, args.keep_ratio, args.mode)",
    "originalFile": "\"\"\"X-VLA Vision Token Pruning Evaluation on LIBERO.\n\nPrunes vision tokens by L2 norm after Florence2's image encoder + linear projection,\nbefore they enter the Florence2 language encoder. Evaluates on LIBERO suites.\n\nFollows official X-VLA evaluation protocol:\n  - Absolute EEF control (use_delta=False)\n  - 20D action space: [arm1: pos(3)+rot6d(6)+grip(1)] + [arm2: zeros(10)]\n  - 20D proprio: [pos(3)+rot6d(6)+0.0] + zeros(10)\n  - domain_id=3 for LIBERO\n  - Closed-loop proprio update from last predicted action\n\nUsage:\n    CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl python eval_xvla_pruning_libero.py \\\n        --model_path /path/to/X-VLA-Libero \\\n        --suite libero_object \\\n        --keep_ratio 0.5 \\\n        --num_episodes 50 \\\n        --gpu 0\n\"\"\"\n\nfrom __future__ import annotations\n\nimport argparse\nimport json\nimport logging\nimport os\nimport sys\nimport time as time_mod\nfrom pathlib import Path\nfrom functools import wraps\n\nos.environ.setdefault(\"MUJOCO_GL\", \"egl\")\n\nimport numpy as np\nimport torch\nfrom PIL import Image\n\nsys.path.insert(0, str(Path(__file__).resolve().parent))\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    datefmt=\"%Y-%m-%d %H:%M:%S\",\n)\nlog = logging.getLogger(__name__)\n\nSUITE_MAX_STEPS = {\n    \"libero_spatial\": 800,\n    \"libero_object\": 800,\n    \"libero_goal\": 800,\n    \"libero_10\": 900,\n    \"libero_90\": 800,\n}\n\nEPS = 1e-6\n\n\ndef parse_args():\n    p = argparse.ArgumentParser(description=\"X-VLA pruning eval on LIBERO\")\n    p.add_argument(\"--model_path\", type=str, default=\"2toINF/X-VLA-Libero\",\n                   help=\"HuggingFace model path or local dir\")\n    p.add_argument(\"--suite\", type=str, default=\"libero_object\",\n                   choices=list(SUITE_MAX_STEPS.keys()))\n    p.add_argument(\"--keep_ratio\", type=float, default=1.0,\n                   help=\"Fraction of vision tokens to keep (1.0 = no pruning)\")\n    p.add_argument(\"--num_episodes\", type=int, default=50)\n    p.add_argument(\"--gpu\", type=int, default=0)\n    p.add_argument(\"--seed\", type=int, default=42)\n    p.add_argument(\"--max_steps\", type=int, default=None)\n    p.add_argument(\"--output\", type=str, default=None)\n    p.add_argument(\"--task_ids\", type=str, default=None)\n    p.add_argument(\"--domain_id\", type=int, default=3)\n    p.add_argument(\"--denoise_steps\", type=int, default=10,\n                   help=\"Flow matching denoising steps\")\n    p.add_argument(\"--mode\", type=str, default=\"l2_norm\",\n                   choices=[\"l2_norm\", \"random\"],\n                   help=\"Pruning method: l2_norm (keep highest L2 norm tokens) or random (random selection)\")\n    return p.parse_args()\n\n\n# ---------------------------------------------------------------------------\n# Pruning hook\n# ---------------------------------------------------------------------------\n\ndef install_vision_pruning(model, keep_ratio: float, mode: str = \"l2_norm\"):\n    if keep_ratio >= 1.0:\n        log.info(\"keep_ratio=%.2f, no pruning applied\", keep_ratio)\n        return\n\n    original_encode = model.vlm._encode_image\n\n    @wraps(original_encode)\n    def pruned_encode(pixel_values):\n        features = original_encode(pixel_values)\n        N = features.shape[1]\n        k = max(1, int(keep_ratio * N))\n        if k >= N:\n            return features\n        if mode == \"l2_norm\":\n            norms = features.norm(dim=-1)\n            _, indices = norms.topk(k, dim=-1)\n        elif mode == \"random\":\n            indices = torch.stack([\n                torch.randperm(N, device=features.device)[:k]\n                for _ in range(features.shape[0])\n            ], dim=0)\n        indices_sorted = indices.sort(dim=-1).values\n        pruned = features.gather(\n            1, indices_sorted.unsqueeze(-1).expand(-1, -1, features.shape[-1])\n        )\n        return pruned\n\n    model.vlm._encode_image = pruned_encode\n    log.info(\"Vision pruning installed: keep_ratio=%.2f, mode=%s\", keep_ratio, mode)\n\n\n# ---------------------------------------------------------------------------\n# Model loading\n# ---------------------------------------------------------------------------\n\ndef load_model(model_path: str, device: torch.device):\n    model_dir = str(Path(model_path).resolve())\n    sys.path.insert(0, model_dir)\n\n    from configuration_xvla import XVLAConfig\n    from modeling_xvla import XVLA\n    from processing_xvla import XVLAProcessor\n    from safetensors.torch import load_file\n\n    log.info(\"Loading X-VLA from %s\", model_dir)\n    config = XVLAConfig.from_pretrained(model_dir)\n    model = XVLA(config)\n\n    safetensors_path = Path(model_dir) / \"model.safetensors\"\n    if safetensors_path.exists():\n        state_dict = load_file(str(safetensors_path))\n    else:\n        import torch as _torch\n        state_dict = _torch.load(Path(model_dir) / \"pytorch_model.bin\", map_location=\"cpu\")\n    model.load_state_dict(state_dict, strict=False)\n    model = model.to(device).eval()\n\n    processor = XVLAProcessor.from_pretrained(model_dir, trust_remote_code=True)\n    if processor.tokenizer.pad_token is None:\n        processor.tokenizer.pad_token = \"&lt;pad>\"\n        processor.tokenizer.pad_token_id = 1\n\n    n_params = sum(p.numel() for p in model.parameters())\n    log.info(\"Model loaded: %.1fM params, dtype=%s\", n_params / 1e6, model.dtype)\n    return model, processor\n\n\n# ---------------------------------------------------------------------------\n# 6D rotation utilities (following X-VLA's convention)\n# ---------------------------------------------------------------------------\n\ndef mat_to_rot6d(R: np.ndarray) -> np.ndarray:\n    \"\"\"Extract 6D rotation from 3x3 rotation matrix: first two columns.\"\"\"\n    return np.concatenate([R[:3, 0], R[:3, 1]], axis=-1).astype(np.float32)\n\n\ndef rot6d_to_axis_angle(r6d: np.ndarray) -> np.ndarray:\n    \"\"\"Convert 6D rotation representation to axis-angle via Gram-Schmidt.\"\"\"\n    import robosuite.utils.transform_utils as T\n\n    single = r6d.ndim == 1\n    if single:\n        r6d = r6d[None, :]\n\n    a1 = r6d[:, 0:3]\n    a2 = r6d[:, 3:6]\n\n    b1 = a1 / (np.linalg.norm(a1, axis=-1, keepdims=True) + EPS)\n    dot_prod = np.sum(b1 * a2, axis=-1, keepdims=True)\n    b2_orth = a2 - dot_prod * b1\n    b2 = b2_orth / (np.linalg.norm(b2_orth, axis=-1, keepdims=True) + EPS)\n    b3 = np.cross(b1, b2, axis=-1)\n\n    R = np.stack([b1, b2, b3], axis=-1)  # (N, 3, 3)\n\n    results = []\n    for i in range(R.shape[0]):\n        quat = T.mat2quat(R[i])\n        aa = T.quat2axisangle(quat)\n        results.append(aa)\n\n    result = np.stack(results, axis=0)\n    return result[0] if single else result\n\n\n# ---------------------------------------------------------------------------\n# Observation processing\n# ---------------------------------------------------------------------------\n\ndef extract_proprio_20d(env) -> np.ndarray:\n    \"\"\"Extract 20D proprio: [pos(3)+rot6d(6)+0.0] + zeros(10) from env robot state.\"\"\"\n    robot = env.env.robots[0]\n    ee_pos = robot.controller.ee_pos.copy()         # (3,)\n    ee_ori_mat = robot.controller.ee_ori_mat.copy()  # (3, 3)\n    ee_rot6d = mat_to_rot6d(ee_ori_mat)              # (6,)\n\n    arm1 = np.concatenate([ee_pos, ee_rot6d, np.array([0.0], dtype=np.float32)])  # (10,)\n    arm2 = np.zeros(10, dtype=np.float32)\n    return np.concatenate([arm1, arm2])  # (20,)\n\n\ndef decode_action_20d_to_7d(action_20d: np.ndarray) -> np.ndarray:\n    \"\"\"Convert 20D X-VLA action to 7D LIBERO action.\n\n    Input:  [pos(3), rot6d(6), grip(1), arm2(10)]  — only arm1 used\n    Output: [pos(3), axis_angle(3), grip(1)]\n    \"\"\"\n    single = action_20d.ndim == 1\n    if single:\n        action_20d = action_20d[None, :]\n\n    pos = action_20d[:, :3]\n    rot6d = action_20d[:, 3:9]\n    grip = action_20d[:, 9:10]\n\n    axis_angle = rot6d_to_axis_angle(rot6d)\n\n    # Discretize gripper: >0.5 → 1.0 (open), else -1.0 (close)\n    grip_disc = np.where(grip > 0.5, 1.0, -1.0)\n\n    result = np.concatenate([pos, axis_angle, grip_disc], axis=-1).astype(np.float32)\n    return result[0] if single else result\n\n\ndef get_images_from_obs(obs) -> list:\n    \"\"\"Extract camera images from LIBERO observation, apply agentview flip.\"\"\"\n    images = []\n    for cam_name in [\"agentview_image\", \"robot0_eye_in_hand_image\"]:\n        img = obs.get(cam_name, None)\n        if img is None:\n            for k, v in obs.items():\n                if cam_name in k and isinstance(v, np.ndarray):\n                    img = v\n                    break\n        if img is not None:\n            if img.dtype in (np.float32, np.float64):\n                img = (np.clip(img, 0, 1) * 255).astype(np.uint8)\n            if cam_name == \"agentview_image\":\n                img = np.flip(np.flip(img, 0), 1).copy()\n            images.append(Image.fromarray(img))\n    return images\n\n\n# ---------------------------------------------------------------------------\n# Action prediction\n# ---------------------------------------------------------------------------\n\n@torch.no_grad()\ndef predict_actions(model, processor, images, task_desc, proprio_20d, domain_id,\n                    device, denoise_steps=10):\n    inputs = processor(images=images, language_instruction=task_desc)\n\n    proprio_t = torch.tensor(proprio_20d, dtype=torch.float32).unsqueeze(0).to(device)\n    domain_t = torch.tensor([domain_id], dtype=torch.long).to(device)\n\n    for k, v in inputs.items():\n        if isinstance(v, torch.Tensor):\n            if v.is_floating_point():\n                inputs[k] = v.to(device=device, dtype=torch.float32)\n            else:\n                inputs[k] = v.to(device=device)\n\n    actions = model.generate_actions(\n        input_ids=inputs[\"input_ids\"],\n        image_input=inputs[\"image_input\"],\n        image_mask=inputs[\"image_mask\"],\n        proprio=proprio_t,\n        domain_id=domain_t,\n        steps=denoise_steps,\n    )  # [1, 30, 20]\n\n    return actions.squeeze(0).float().cpu().numpy()  # [30, 20]\n\n\n# ---------------------------------------------------------------------------\n# Wilson CI\n# ---------------------------------------------------------------------------\n\ndef wilson_ci(successes, total, z=1.96):\n    if total == 0:\n        return 0.0, 0.0, 1.0\n    p = successes / total\n    denom = 1 + z ** 2 / total\n    center = (p + z ** 2 / (2 * total)) / denom\n    spread = z * np.sqrt((p * (1 - p) + z ** 2 / (4 * total)) / total) / denom\n    return center, max(0.0, center - spread), min(1.0, center + spread)\n\n\n# ---------------------------------------------------------------------------\n# Main evaluation\n# ---------------------------------------------------------------------------\n\ndef run_evaluation(args):\n    device = torch.device(f\"cuda:{args.gpu}\" if torch.cuda.is_available() else \"cpu\")\n    max_steps = args.max_steps or SUITE_MAX_STEPS.get(args.suite, 800)\n    output_path = Path(args.output or\n                       f\"eval_results/xvla_prune_k{args.keep_ratio}_{args.suite}.json\")\n\n    log.info(\"Suite: %s | Device: %s | keep_ratio=%.2f | Episodes/task: %d | Max steps: %d\",\n             args.suite, device, args.keep_ratio, args.num_episodes, max_steps)\n\n    np.random.seed(args.seed)\n    torch.manual_seed(args.seed)\n\n    t0 = time_mod.time()\n    model, processor = load_model(args.model_path, device)\n    log.info(\"Model loaded in %.1fs\", time_mod.time() - t0)\n\n    dummy_img = torch.randn(1, 3, 224, 224, device=device)\n    with torch.no_grad():\n        dummy_feats = model.vlm._encode_image(dummy_img)\n    n_vis_tokens = dummy_feats.shape[1]\n    k_tokens = max(1, int(args.keep_ratio * n_vis_tokens))\n    log.info(\"Vision tokens: %d total, keeping %d (%.0f%%)\",\n             n_vis_tokens, k_tokens, args.keep_ratio * 100)\n\n    install_vision_pruning(model, args.keep_ratio)\n\n    num_actions_per_chunk = model.num_actions  # 30\n\n    # LIBERO setup — use OffScreenRenderEnv directly (matching official X-VLA eval)\n    from libero.libero import benchmark, get_libero_path\n    from libero.libero.envs import OffScreenRenderEnv\n\n    task_suite = benchmark.get_benchmark(args.suite)()\n    n_tasks = task_suite.n_tasks\n\n    if args.task_ids:\n        task_id_list = [int(x) for x in args.task_ids.split(\",\")]\n    else:\n        task_id_list = list(range(n_tasks))\n\n    eval_start = time_mod.time()\n    all_task_results = {}\n    total_successes = 0\n    total_episodes = 0\n\n    for task_id in task_id_list:\n        task = task_suite.get_task(task_id)\n        task_desc = task.language\n        task_bddl = os.path.join(\n            get_libero_path(\"bddl_files\"), task.problem_folder, task.bddl_file\n        )\n        log.info(\"--- Task %d: %s ---\", task_id, task_desc)\n\n        init_states = task_suite.get_task_init_states(task_id)\n\n        task_successes = []\n        task_lengths = []\n\n        for ep in range(args.num_episodes):\n            env = OffScreenRenderEnv(\n                bddl_file_name=task_bddl,\n                camera_heights=256,\n                camera_widths=256,\n            )\n            env.seed(args.seed + ep + 100)\n            obs = env.reset()\n\n            init_state_id = ep % init_states.shape[0]\n            obs = env.set_init_state(init_states[init_state_id])\n\n            # Settle the robot with neutral actions\n            for _ in range(10):\n                neutral = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0], dtype=np.float32)\n                obs, _, _, _ = env.step(neutral)\n\n            # Switch to absolute control\n            for robot in env.env.robots:\n                robot.controller.use_delta = False\n\n            action_queue = []\n            proprio_state = None\n            success = False\n\n            for step_idx in range(max_steps):\n                if not action_queue:\n                    # Extract proprio from env\n                    proprio_20d = extract_proprio_20d(env)\n                    if proprio_state is not None:\n                        proprio_20d[:9] = proprio_state[:9]\n\n                    images = get_images_from_obs(obs)\n                    if not images:\n                        raise ValueError(f\"No images found in obs keys: {list(obs.keys())}\")\n\n                    raw_actions = predict_actions(\n                        model, processor, images, task_desc, proprio_20d,\n                        args.domain_id, device, args.denoise_steps,\n                    )  # [30, 20]\n\n                    # Update closed-loop proprio with last predicted action\n                    proprio_state = proprio_20d.copy()\n                    proprio_state[:9] = raw_actions[-1, :9].copy()\n\n                    actions_7d = decode_action_20d_to_7d(raw_actions)  # [30, 7]\n                    action_queue = list(actions_7d)\n\n                action = action_queue.pop(0)\n                obs, reward, done, info = env.step(action)\n\n                if done or reward > 0.5:\n                    success = True\n                    break\n\n            ep_steps = step_idx + 1\n            task_successes.append(success)\n            task_lengths.append(ep_steps)\n            log.info(\"  Ep %d/%d | %s | steps=%d\",\n                     ep + 1, args.num_episodes,\n                     \"SUCCESS\" if success else \"FAIL\", ep_steps)\n\n            env.close()\n\n        n_succ = sum(task_successes)\n        n_total = len(task_successes)\n        sr = n_succ / n_total if n_total > 0 else 0.0\n\n        all_task_results[task_id] = {\n            \"task_id\": task_id,\n            \"task_description\": task_desc,\n            \"success_count\": n_succ,\n            \"total_episodes\": n_total,\n            \"success_rate\": round(sr, 4),\n            \"mean_steps\": round(float(np.mean(task_lengths)), 1),\n        }\n        total_successes += n_succ\n        total_episodes += n_total\n        log.info(\"  Task %d SR: %d/%d (%.1f%%)\", task_id, n_succ, n_total, sr * 100)\n\n    elapsed = time_mod.time() - eval_start\n    overall_sr = total_successes / total_episodes if total_episodes > 0 else 0.0\n    _, ci_lo, ci_hi = wilson_ci(total_successes, total_episodes)\n\n    log.info(\"=\" * 60)\n    log.info(\"SUITE: %s | MODEL: xvla | keep_ratio: %.2f\", args.suite, args.keep_ratio)\n    log.info(\"Overall SR: %d/%d (%.1f%%)\", total_successes, total_episodes, overall_sr * 100)\n    log.info(\"95%% Wilson CI: [%.1f%%, %.1f%%]\", ci_lo * 100, ci_hi * 100)\n    for tid, tr in sorted(all_task_results.items()):\n        log.info(\"  Task %d: %.0f%% (%d/%d) -- %s\",\n                 tid, tr[\"success_rate\"] * 100, tr[\"success_count\"],\n                 tr[\"total_episodes\"], tr[\"task_description\"])\n    log.info(\"Elapsed: %.1f min\", elapsed / 60)\n    log.info(\"=\" * 60)\n\n    summary = {\n        \"model\": \"xvla\",\n        \"model_path\": args.model_path,\n        \"mode\": \"l2_norm_prune\",\n        \"suite\": args.suite,\n        \"keep_ratio\": args.keep_ratio,\n        \"n_vision_tokens_original\": n_vis_tokens,\n        \"n_vision_tokens_kept\": k_tokens,\n        \"total_episodes\": total_episodes,\n        \"total_successes\": total_successes,\n        \"overall_success_rate\": round(overall_sr, 4),\n        \"wilson_ci_95\": [round(ci_lo, 4), round(ci_hi, 4)],\n        \"num_episodes_per_task\": args.num_episodes,\n        \"max_steps\": max_steps,\n        \"num_actions_per_chunk\": num_actions_per_chunk,\n        \"domain_id\": args.domain_id,\n        \"denoise_steps\": args.denoise_steps,\n        \"seed\": args.seed,\n        \"elapsed_seconds\": round(elapsed, 1),\n        \"per_task\": all_task_results,\n    }\n\n    output_path.parent.mkdir(parents=True, exist_ok=True)\n    with open(output_path, \"w\") as f:\n        json.dump(summary, f, indent=2)\n    log.info(\"Results saved to %s\", output_path)\n\n    return summary\n\n\nif __name__ == \"__main__\":\n    args = parse_args()\n    run_evaluation(args)\n",
    "structuredPatch": [
      {
        "oldStart": 320,
        "oldLines": 7,
        "newStart": 320,
        "newLines": 7,
        "lines": [
          "     log.info(\"Vision tokens: %d total, keeping %d (%.0f%%)\",",
          "              n_vis_tokens, k_tokens, args.keep_ratio * 100)",
          " ",
          "-    install_vision_pruning(model, args.keep_ratio)",
          "+    install_vision_pruning(model, args.keep_ratio, args.mode)",
          " ",
          "     num_actions_per_chunk = model.num_actions  # 30",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 26_

同时更新 summary 中的 mode 字段，使其反映实际参数：

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a",
  "uuid": "5aaf1d25-a3f1-4e69-a68d-88cfa5b93822",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019P1JJYyQ6ibin6VmJ3X6LC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 255,
      "cache_read_input_tokens": 32967,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 255
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Edit · `toolu_01UfMUYxMWU1BXHHBCefSb9P`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/eval_xvla_pruning_libero.py",
  "old_string": "        \"mode\": \"l2_norm_prune\",",
  "new_string": "        \"mode\": args.mode,"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a",
  "uuid": "19c0de55-302e-4ef8-9c90-e2066b51c472",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019P1JJYyQ6ibin6VmJ3X6LC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 255,
      "cache_read_input_tokens": 32967,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 255
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-21T02:21:57.181Z_

<details><summary>↩ Tool result · `toolu_01UfMUYxMWU1BXHHBCefSb9P`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/eval_xvla_pruning_libero.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a",
  "uuid": "302e136d-f4f9-4771-989d-00a740d97c2e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/eval_xvla_pruning_libero.py",
    "oldString": "        \"mode\": \"l2_norm_prune\",",
    "newString": "        \"mode\": args.mode,",
    "originalFile": "\"\"\"X-VLA Vision Token Pruning Evaluation on LIBERO.\n\nPrunes vision tokens by L2 norm after Florence2's image encoder + linear projection,\nbefore they enter the Florence2 language encoder. Evaluates on LIBERO suites.\n\nFollows official X-VLA evaluation protocol:\n  - Absolute EEF control (use_delta=False)\n  - 20D action space: [arm1: pos(3)+rot6d(6)+grip(1)] + [arm2: zeros(10)]\n  - 20D proprio: [pos(3)+rot6d(6)+0.0] + zeros(10)\n  - domain_id=3 for LIBERO\n  - Closed-loop proprio update from last predicted action\n\nUsage:\n    CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl python eval_xvla_pruning_libero.py \\\n        --model_path /path/to/X-VLA-Libero \\\n        --suite libero_object \\\n        --keep_ratio 0.5 \\\n        --num_episodes 50 \\\n        --gpu 0\n\"\"\"\n\nfrom __future__ import annotations\n\nimport argparse\nimport json\nimport logging\nimport os\nimport sys\nimport time as time_mod\nfrom pathlib import Path\nfrom functools import wraps\n\nos.environ.setdefault(\"MUJOCO_GL\", \"egl\")\n\nimport numpy as np\nimport torch\nfrom PIL import Image\n\nsys.path.insert(0, str(Path(__file__).resolve().parent))\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    datefmt=\"%Y-%m-%d %H:%M:%S\",\n)\nlog = logging.getLogger(__name__)\n\nSUITE_MAX_STEPS = {\n    \"libero_spatial\": 800,\n    \"libero_object\": 800,\n    \"libero_goal\": 800,\n    \"libero_10\": 900,\n    \"libero_90\": 800,\n}\n\nEPS = 1e-6\n\n\ndef parse_args():\n    p = argparse.ArgumentParser(description=\"X-VLA pruning eval on LIBERO\")\n    p.add_argument(\"--model_path\", type=str, default=\"2toINF/X-VLA-Libero\",\n                   help=\"HuggingFace model path or local dir\")\n    p.add_argument(\"--suite\", type=str, default=\"libero_object\",\n                   choices=list(SUITE_MAX_STEPS.keys()))\n    p.add_argument(\"--keep_ratio\", type=float, default=1.0,\n                   help=\"Fraction of vision tokens to keep (1.0 = no pruning)\")\n    p.add_argument(\"--num_episodes\", type=int, default=50)\n    p.add_argument(\"--gpu\", type=int, default=0)\n    p.add_argument(\"--seed\", type=int, default=42)\n    p.add_argument(\"--max_steps\", type=int, default=None)\n    p.add_argument(\"--output\", type=str, default=None)\n    p.add_argument(\"--task_ids\", type=str, default=None)\n    p.add_argument(\"--domain_id\", type=int, default=3)\n    p.add_argument(\"--denoise_steps\", type=int, default=10,\n                   help=\"Flow matching denoising steps\")\n    p.add_argument(\"--mode\", type=str, default=\"l2_norm\",\n                   choices=[\"l2_norm\", \"random\"],\n                   help=\"Pruning method: l2_norm (keep highest L2 norm tokens) or random (random selection)\")\n    return p.parse_args()\n\n\n# ---------------------------------------------------------------------------\n# Pruning hook\n# ---------------------------------------------------------------------------\n\ndef install_vision_pruning(model, keep_ratio: float, mode: str = \"l2_norm\"):\n    if keep_ratio >= 1.0:\n        log.info(\"keep_ratio=%.2f, no pruning applied\", keep_ratio)\n        return\n\n    original_encode = model.vlm._encode_image\n\n    @wraps(original_encode)\n    def pruned_encode(pixel_values):\n        features = original_encode(pixel_values)\n        N = features.shape[1]\n        k = max(1, int(keep_ratio * N))\n        if k >= N:\n            return features\n        if mode == \"l2_norm\":\n            norms = features.norm(dim=-1)\n            _, indices = norms.topk(k, dim=-1)\n        elif mode == \"random\":\n            indices = torch.stack([\n                torch.randperm(N, device=features.device)[:k]\n                for _ in range(features.shape[0])\n            ], dim=0)\n        indices_sorted = indices.sort(dim=-1).values\n        pruned = features.gather(\n            1, indices_sorted.unsqueeze(-1).expand(-1, -1, features.shape[-1])\n        )\n        return pruned\n\n    model.vlm._encode_image = pruned_encode\n    log.info(\"Vision pruning installed: keep_ratio=%.2f, mode=%s\", keep_ratio, mode)\n\n\n# ---------------------------------------------------------------------------\n# Model loading\n# ---------------------------------------------------------------------------\n\ndef load_model(model_path: str, device: torch.device):\n    model_dir = str(Path(model_path).resolve())\n    sys.path.insert(0, model_dir)\n\n    from configuration_xvla import XVLAConfig\n    from modeling_xvla import XVLA\n    from processing_xvla import XVLAProcessor\n    from safetensors.torch import load_file\n\n    log.info(\"Loading X-VLA from %s\", model_dir)\n    config = XVLAConfig.from_pretrained(model_dir)\n    model = XVLA(config)\n\n    safetensors_path = Path(model_dir) / \"model.safetensors\"\n    if safetensors_path.exists():\n        state_dict = load_file(str(safetensors_path))\n    else:\n        import torch as _torch\n        state_dict = _torch.load(Path(model_dir) / \"pytorch_model.bin\", map_location=\"cpu\")\n    model.load_state_dict(state_dict, strict=False)\n    model = model.to(device).eval()\n\n    processor = XVLAProcessor.from_pretrained(model_dir, trust_remote_code=True)\n    if processor.tokenizer.pad_token is None:\n        processor.tokenizer.pad_token = \"&lt;pad>\"\n        processor.tokenizer.pad_token_id = 1\n\n    n_params = sum(p.numel() for p in model.parameters())\n    log.info(\"Model loaded: %.1fM params, dtype=%s\", n_params / 1e6, model.dtype)\n    return model, processor\n\n\n# ---------------------------------------------------------------------------\n# 6D rotation utilities (following X-VLA's convention)\n# ---------------------------------------------------------------------------\n\ndef mat_to_rot6d(R: np.ndarray) -> np.ndarray:\n    \"\"\"Extract 6D rotation from 3x3 rotation matrix: first two columns.\"\"\"\n    return np.concatenate([R[:3, 0], R[:3, 1]], axis=-1).astype(np.float32)\n\n\ndef rot6d_to_axis_angle(r6d: np.ndarray) -> np.ndarray:\n    \"\"\"Convert 6D rotation representation to axis-angle via Gram-Schmidt.\"\"\"\n    import robosuite.utils.transform_utils as T\n\n    single = r6d.ndim == 1\n    if single:\n        r6d = r6d[None, :]\n\n    a1 = r6d[:, 0:3]\n    a2 = r6d[:, 3:6]\n\n    b1 = a1 / (np.linalg.norm(a1, axis=-1, keepdims=True) + EPS)\n    dot_prod = np.sum(b1 * a2, axis=-1, keepdims=True)\n    b2_orth = a2 - dot_prod * b1\n    b2 = b2_orth / (np.linalg.norm(b2_orth, axis=-1, keepdims=True) + EPS)\n    b3 = np.cross(b1, b2, axis=-1)\n\n    R = np.stack([b1, b2, b3], axis=-1)  # (N, 3, 3)\n\n    results = []\n    for i in range(R.shape[0]):\n        quat = T.mat2quat(R[i])\n        aa = T.quat2axisangle(quat)\n        results.append(aa)\n\n    result = np.stack(results, axis=0)\n    return result[0] if single else result\n\n\n# ---------------------------------------------------------------------------\n# Observation processing\n# ---------------------------------------------------------------------------\n\ndef extract_proprio_20d(env) -> np.ndarray:\n    \"\"\"Extract 20D proprio: [pos(3)+rot6d(6)+0.0] + zeros(10) from env robot state.\"\"\"\n    robot = env.env.robots[0]\n    ee_pos = robot.controller.ee_pos.copy()         # (3,)\n    ee_ori_mat = robot.controller.ee_ori_mat.copy()  # (3, 3)\n    ee_rot6d = mat_to_rot6d(ee_ori_mat)              # (6,)\n\n    arm1 = np.concatenate([ee_pos, ee_rot6d, np.array([0.0], dtype=np.float32)])  # (10,)\n    arm2 = np.zeros(10, dtype=np.float32)\n    return np.concatenate([arm1, arm2])  # (20,)\n\n\ndef decode_action_20d_to_7d(action_20d: np.ndarray) -> np.ndarray:\n    \"\"\"Convert 20D X-VLA action to 7D LIBERO action.\n\n    Input:  [pos(3), rot6d(6), grip(1), arm2(10)]  — only arm1 used\n    Output: [pos(3), axis_angle(3), grip(1)]\n    \"\"\"\n    single = action_20d.ndim == 1\n    if single:\n        action_20d = action_20d[None, :]\n\n    pos = action_20d[:, :3]\n    rot6d = action_20d[:, 3:9]\n    grip = action_20d[:, 9:10]\n\n    axis_angle = rot6d_to_axis_angle(rot6d)\n\n    # Discretize gripper: >0.5 → 1.0 (open), else -1.0 (close)\n    grip_disc = np.where(grip > 0.5, 1.0, -1.0)\n\n    result = np.concatenate([pos, axis_angle, grip_disc], axis=-1).astype(np.float32)\n    return result[0] if single else result\n\n\ndef get_images_from_obs(obs) -> list:\n    \"\"\"Extract camera images from LIBERO observation, apply agentview flip.\"\"\"\n    images = []\n    for cam_name in [\"agentview_image\", \"robot0_eye_in_hand_image\"]:\n        img = obs.get(cam_name, None)\n        if img is None:\n            for k, v in obs.items():\n                if cam_name in k and isinstance(v, np.ndarray):\n                    img = v\n                    break\n        if img is not None:\n            if img.dtype in (np.float32, np.float64):\n                img = (np.clip(img, 0, 1) * 255).astype(np.uint8)\n            if cam_name == \"agentview_image\":\n                img = np.flip(np.flip(img, 0), 1).copy()\n            images.append(Image.fromarray(img))\n    return images\n\n\n# ---------------------------------------------------------------------------\n# Action prediction\n# ---------------------------------------------------------------------------\n\n@torch.no_grad()\ndef predict_actions(model, processor, images, task_desc, proprio_20d, domain_id,\n                    device, denoise_steps=10):\n    inputs = processor(images=images, language_instruction=task_desc)\n\n    proprio_t = torch.tensor(proprio_20d, dtype=torch.float32).unsqueeze(0).to(device)\n    domain_t = torch.tensor([domain_id], dtype=torch.long).to(device)\n\n    for k, v in inputs.items():\n        if isinstance(v, torch.Tensor):\n            if v.is_floating_point():\n                inputs[k] = v.to(device=device, dtype=torch.float32)\n            else:\n                inputs[k] = v.to(device=device)\n\n    actions = model.generate_actions(\n        input_ids=inputs[\"input_ids\"],\n        image_input=inputs[\"image_input\"],\n        image_mask=inputs[\"image_mask\"],\n        proprio=proprio_t,\n        domain_id=domain_t,\n        steps=denoise_steps,\n    )  # [1, 30, 20]\n\n    return actions.squeeze(0).float().cpu().numpy()  # [30, 20]\n\n\n# ---------------------------------------------------------------------------\n# Wilson CI\n# ---------------------------------------------------------------------------\n\ndef wilson_ci(successes, total, z=1.96):\n    if total == 0:\n        return 0.0, 0.0, 1.0\n    p = successes / total\n    denom = 1 + z ** 2 / total\n    center = (p + z ** 2 / (2 * total)) / denom\n    spread = z * np.sqrt((p * (1 - p) + z ** 2 / (4 * total)) / total) / denom\n    return center, max(0.0, center - spread), min(1.0, center + spread)\n\n\n# ---------------------------------------------------------------------------\n# Main evaluation\n# ---------------------------------------------------------------------------\n\ndef run_evaluation(args):\n    device = torch.device(f\"cuda:{args.gpu}\" if torch.cuda.is_available() else \"cpu\")\n    max_steps = args.max_steps or SUITE_MAX_STEPS.get(args.suite, 800)\n    output_path = Path(args.output or\n                       f\"eval_results/xvla_prune_k{args.keep_ratio}_{args.suite}.json\")\n\n    log.info(\"Suite: %s | Device: %s | keep_ratio=%.2f | Episodes/task: %d | Max steps: %d\",\n             args.suite, device, args.keep_ratio, args.num_episodes, max_steps)\n\n    np.random.seed(args.seed)\n    torch.manual_seed(args.seed)\n\n    t0 = time_mod.time()\n    model, processor = load_model(args.model_path, device)\n    log.info(\"Model loaded in %.1fs\", time_mod.time() - t0)\n\n    dummy_img = torch.randn(1, 3, 224, 224, device=device)\n    with torch.no_grad():\n        dummy_feats = model.vlm._encode_image(dummy_img)\n    n_vis_tokens = dummy_feats.shape[1]\n    k_tokens = max(1, int(args.keep_ratio * n_vis_tokens))\n    log.info(\"Vision tokens: %d total, keeping %d (%.0f%%)\",\n             n_vis_tokens, k_tokens, args.keep_ratio * 100)\n\n    install_vision_pruning(model, args.keep_ratio, args.mode)\n\n    num_actions_per_chunk = model.num_actions  # 30\n\n    # LIBERO setup — use OffScreenRenderEnv directly (matching official X-VLA eval)\n    from libero.libero import benchmark, get_libero_path\n    from libero.libero.envs import OffScreenRenderEnv\n\n    task_suite = benchmark.get_benchmark(args.suite)()\n    n_tasks = task_suite.n_tasks\n\n    if args.task_ids:\n        task_id_list = [int(x) for x in args.task_ids.split(\",\")]\n    else:\n        task_id_list = list(range(n_tasks))\n\n    eval_start = time_mod.time()\n    all_task_results = {}\n    total_successes = 0\n    total_episodes = 0\n\n    for task_id in task_id_list:\n        task = task_suite.get_task(task_id)\n        task_desc = task.language\n        task_bddl = os.path.join(\n            get_libero_path(\"bddl_files\"), task.problem_folder, task.bddl_file\n        )\n        log.info(\"--- Task %d: %s ---\", task_id, task_desc)\n\n        init_states = task_suite.get_task_init_states(task_id)\n\n        task_successes = []\n        task_lengths = []\n\n        for ep in range(args.num_episodes):\n            env = OffScreenRenderEnv(\n                bddl_file_name=task_bddl,\n                camera_heights=256,\n                camera_widths=256,\n            )\n            env.seed(args.seed + ep + 100)\n            obs = env.reset()\n\n            init_state_id = ep % init_states.shape[0]\n            obs = env.set_init_state(init_states[init_state_id])\n\n            # Settle the robot with neutral actions\n            for _ in range(10):\n                neutral = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0], dtype=np.float32)\n                obs, _, _, _ = env.step(neutral)\n\n            # Switch to absolute control\n            for robot in env.env.robots:\n                robot.controller.use_delta = False\n\n            action_queue = []\n            proprio_state = None\n            success = False\n\n            for step_idx in range(max_steps):\n                if not action_queue:\n                    # Extract proprio from env\n                    proprio_20d = extract_proprio_20d(env)\n                    if proprio_state is not None:\n                        proprio_20d[:9] = proprio_state[:9]\n\n                    images = get_images_from_obs(obs)\n                    if not images:\n                        raise ValueError(f\"No images found in obs keys: {list(obs.keys())}\")\n\n                    raw_actions = predict_actions(\n                        model, processor, images, task_desc, proprio_20d,\n                        args.domain_id, device, args.denoise_steps,\n                    )  # [30, 20]\n\n                    # Update closed-loop proprio with last predicted action\n                    proprio_state = proprio_20d.copy()\n                    proprio_state[:9] = raw_actions[-1, :9].copy()\n\n                    actions_7d = decode_action_20d_to_7d(raw_actions)  # [30, 7]\n                    action_queue = list(actions_7d)\n\n                action = action_queue.pop(0)\n                obs, reward, done, info = env.step(action)\n\n                if done or reward > 0.5:\n                    success = True\n                    break\n\n            ep_steps = step_idx + 1\n            task_successes.append(success)\n            task_lengths.append(ep_steps)\n            log.info(\"  Ep %d/%d | %s | steps=%d\",\n                     ep + 1, args.num_episodes,\n                     \"SUCCESS\" if success else \"FAIL\", ep_steps)\n\n            env.close()\n\n        n_succ = sum(task_successes)\n        n_total = len(task_successes)\n        sr = n_succ / n_total if n_total > 0 else 0.0\n\n        all_task_results[task_id] = {\n            \"task_id\": task_id,\n            \"task_description\": task_desc,\n            \"success_count\": n_succ,\n            \"total_episodes\": n_total,\n            \"success_rate\": round(sr, 4),\n            \"mean_steps\": round(float(np.mean(task_lengths)), 1),\n        }\n        total_successes += n_succ\n        total_episodes += n_total\n        log.info(\"  Task %d SR: %d/%d (%.1f%%)\", task_id, n_succ, n_total, sr * 100)\n\n    elapsed = time_mod.time() - eval_start\n    overall_sr = total_successes / total_episodes if total_episodes > 0 else 0.0\n    _, ci_lo, ci_hi = wilson_ci(total_successes, total_episodes)\n\n    log.info(\"=\" * 60)\n    log.info(\"SUITE: %s | MODEL: xvla | keep_ratio: %.2f\", args.suite, args.keep_ratio)\n    log.info(\"Overall SR: %d/%d (%.1f%%)\", total_successes, total_episodes, overall_sr * 100)\n    log.info(\"95%% Wilson CI: [%.1f%%, %.1f%%]\", ci_lo * 100, ci_hi * 100)\n    for tid, tr in sorted(all_task_results.items()):\n        log.info(\"  Task %d: %.0f%% (%d/%d) -- %s\",\n                 tid, tr[\"success_rate\"] * 100, tr[\"success_count\"],\n                 tr[\"total_episodes\"], tr[\"task_description\"])\n    log.info(\"Elapsed: %.1f min\", elapsed / 60)\n    log.info(\"=\" * 60)\n\n    summary = {\n        \"model\": \"xvla\",\n        \"model_path\": args.model_path,\n        \"mode\": \"l2_norm_prune\",\n        \"suite\": args.suite,\n        \"keep_ratio\": args.keep_ratio,\n        \"n_vision_tokens_original\": n_vis_tokens,\n        \"n_vision_tokens_kept\": k_tokens,\n        \"total_episodes\": total_episodes,\n        \"total_successes\": total_successes,\n        \"overall_success_rate\": round(overall_sr, 4),\n        \"wilson_ci_95\": [round(ci_lo, 4), round(ci_hi, 4)],\n        \"num_episodes_per_task\": args.num_episodes,\n        \"max_steps\": max_steps,\n        \"num_actions_per_chunk\": num_actions_per_chunk,\n        \"domain_id\": args.domain_id,\n        \"denoise_steps\": args.denoise_steps,\n        \"seed\": args.seed,\n        \"elapsed_seconds\": round(elapsed, 1),\n        \"per_task\": all_task_results,\n    }\n\n    output_path.parent.mkdir(parents=True, exist_ok=True)\n    with open(output_path, \"w\") as f:\n        json.dump(summary, f, indent=2)\n    log.info(\"Results saved to %s\", output_path)\n\n    return summary\n\n\nif __name__ == \"__main__\":\n    args = parse_args()\n    run_evaluation(args)\n",
    "structuredPatch": [
      {
        "oldStart": 452,
        "oldLines": 7,
        "newStart": 452,
        "newLines": 7,
        "lines": [
          "     summary = {",
          "         \"model\": \"xvla\",",
          "         \"model_path\": args.model_path,",
          "-        \"mode\": \"l2_norm_prune\",",
          "+        \"mode\": args.mode,",
          "         \"suite\": args.suite,",
          "         \"keep_ratio\": args.keep_ratio,",
          "         \"n_vision_tokens_original\": n_vis_tokens,"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 29_

本地修改完成。现在部署到两台服务器。先查找脚本位置。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a",
  "uuid": "da609759-6944-4671-8495-fb55bb5786c8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012487CVRTiegYXpmYs7w8C1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 371,
      "cache_read_input_tokens": 33222,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 371
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01M77B1KhtZhuiVr4AMifYKE`</summary>

```json
{
  "server": "cqa1-33015",
  "command": "find /root/autodl-tmp -name \"eval_xvla_pruning_libero.py\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a",
  "uuid": "231b0357-e1ad-4d4a-b24d-32713b5085ed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012487CVRTiegYXpmYs7w8C1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 371,
      "cache_read_input_tokens": 33222,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 371
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_016t93M4CDecRpUDc68F2avQ`</summary>

```json
{
  "server": "westd-38929",
  "command": "find /root/autodl-tmp -name \"eval_xvla_pruning_libero.py\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a",
  "uuid": "781e93f6-59fb-490f-af74-81028b804d38",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012487CVRTiegYXpmYs7w8C1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 371,
      "cache_read_input_tokens": 33222,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 371
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-21T02:22:03.413Z_

<details><summary>↩ Tool result · `toolu_01M77B1KhtZhuiVr4AMifYKE`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_xvla_pruning_libero.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.2}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a",
  "uuid": "4dac12b2-0afa-4be9-b9db-d14e9a285fe2",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/eval_xvla_pruning_libero.py\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.2}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_xvla_pruning_libero.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.2}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-21T02:22:04.365Z_

<details><summary>↩ Tool result · `toolu_016t93M4CDecRpUDc68F2avQ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_xvla_pruning_libero.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.94}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a",
  "uuid": "720b82ad-7dbb-4ca4-beb4-37527c58673c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/eval_xvla_pruning_libero.py\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.94}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_xvla_pruning_libero.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.94}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 34_

两台服务器路径一致。读取修改后的本地文件内容，然后部署。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a",
  "uuid": "b557d054-5eb4-42bf-bfe0-901c285553f1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bp9GSRHgusig832xsG1xT2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 541,
      "cache_read_input_tokens": 33593,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 541
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Read · `toolu_01MGGc49fGqPJJcoEhRWaJVf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/eval_xvla_pruning_libero.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a",
  "uuid": "bcbbebd7-82bd-4a7f-aa98-8e979841329b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bp9GSRHgusig832xsG1xT2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 541,
      "cache_read_input_tokens": 33593,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 541
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-21T02:22:09.043Z_

<details><summary>↩ Tool result · `toolu_01MGGc49fGqPJJcoEhRWaJVf`</summary>

```text
1	"""X-VLA Vision Token Pruning Evaluation on LIBERO.
2	
3	Prunes vision tokens by L2 norm after Florence2's image encoder + linear projection,
4	before they enter the Florence2 language encoder. Evaluates on LIBERO suites.
5	
6	Follows official X-VLA evaluation protocol:
7	  - Absolute EEF control (use_delta=False)
8	  - 20D action space: [arm1: pos(3)+rot6d(6)+grip(1)] + [arm2: zeros(10)]
9	  - 20D proprio: [pos(3)+rot6d(6)+0.0] + zeros(10)
10	  - domain_id=3 for LIBERO
11	  - Closed-loop proprio update from last predicted action
12	
13	Usage:
14	    CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl python eval_xvla_pruning_libero.py \
15	        --model_path /path/to/X-VLA-Libero \
16	        --suite libero_object \
17	        --keep_ratio 0.5 \
18	        --num_episodes 50 \
19	        --gpu 0
20	"""
21	
22	from __future__ import annotations
23	
24	import argparse
25	import json
26	import logging
27	import os
28	import sys
29	import time as time_mod
30	from pathlib import Path
31	from functools import wraps
32	
33	os.environ.setdefault("MUJOCO_GL", "egl")
34	
35	import numpy as np
36	import torch
37	from PIL import Image
38	
39	sys.path.insert(0, str(Path(__file__).resolve().parent))
40	
41	logging.basicConfig(
42	    level=logging.INFO,
43	    format="%(asctime)s [%(levelname)s] %(message)s",
44	    datefmt="%Y-%m-%d %H:%M:%S",
45	)
46	log = logging.getLogger(__name__)
47	
48	SUITE_MAX_STEPS = {
49	    "libero_spatial": 800,
50	    "libero_object": 800,
51	    "libero_goal": 800,
52	    "libero_10": 900,
53	    "libero_90": 800,
54	}
55	
56	EPS = 1e-6
57	
58	
59	def parse_args():
60	    p = argparse.ArgumentParser(description="X-VLA pruning eval on LIBERO")
61	    p.add_argument("--model_path", type=str, default="2toINF/X-VLA-Libero",
62	                   help="HuggingFace model path or local dir")
63	    p.add_argument("--suite", type=str, default="libero_object",
64	                   choices=list(SUITE_MAX_STEPS.keys()))
65	    p.add_argument("--keep_ratio", type=float, default=1.0,
66	                   help="Fraction of vision tokens to keep (1.0 = no pruning)")
67	    p.add_argument("--num_episodes", type=int, default=50)
68	    p.add_argument("--gpu", type=int, default=0)
69	    p.add_argument("--seed", type=int, default=42)
70	    p.add_argument("--max_steps", type=int, default=None)
71	    p.add_argument("--output", type=str, default=None)
72	    p.add_argument("--task_ids", type=str, default=None)
73	    p.add_argument("--domain_id", type=int, default=3)
74	    p.add_argument("--denoise_steps", type=int, default=10,
75	                   help="Flow matching denoising steps")
76	    p.add_argument("--mode", type=str, default="l2_norm",
77	                   choices=["l2_norm", "random"],
78	                   help="Pruning method: l2_norm (keep highest L2 norm tokens) or random (random selection)")
79	    return p.parse_args()
80	
81	
82	# ---------------------------------------------------------------------------
83	# Pruning hook
84	# ---------------------------------------------------------------------------
85	
86	def install_vision_pruning(model, keep_ratio: float, mode: str = "l2_norm"):
87	    if keep_ratio >= 1.0:
88	        log.info("keep_ratio=%.2f, no pruning applied", keep_ratio)
89	        return
90	
91	    original_encode = model.vlm._encode_image
92	
93	    @wraps(original_encode)
94	    def pruned_encode(pixel_values):
95	        features = original_encode(pixel_values)
96	        N = features.shape[1]
97	        k = max(1, int(keep_ratio * N))
98	        if k >= N:
99	            return features
100	        if mode == "l2_norm":
101	            norms = features.norm(dim=-1)
102	            _, indices = norms.topk(k, dim=-1)
103	        elif mode == "random":
104	            indices = torch.stack([
105	                torch.randperm(N, device=features.device)[:k]
106	                for _ in range(features.shape[0])
107	            ], dim=0)
108	        indices_sorted = indices.sort(dim=-1).values
109	        pruned = features.gather(
110	            1, indices_sorted.unsqueeze(-1).expand(-1, -1, features.shape[-1])
111	        )
112	        return pruned
113	
114	    model.vlm._encode_image = pruned_encode
115	    log.info("Vision pruning installed: keep_ratio=%.2f, mode=%s", keep_ratio, mode)
116	
117	
118	# ---------------------------------------------------------------------------
119	# Model loading
120	# ---------------------------------------------------------------------------
121	
122	def load_model(model_path: str, device: torch.device):
123	    model_dir = str(Path(model_path).resolve())
124	    sys.path.insert(0, model_dir)
125	
126	    from configuration_xvla import XVLAConfig
127	    from modeling_xvla import XVLA
128	    from processing_xvla import XVLAProcessor
129	    from safetensors.torch import load_file
130	
131	    log.info("Loading X-VLA from %s", model_dir)
132	    config = XVLAConfig.from_pretrained(model_dir)
133	    model = XVLA(config)
134	
135	    safetensors_path = Path(model_dir) / "model.safetensors"
136	    if safetensors_path.exists():
137	        state_dict = load_file(str(safetensors_path))
138	    else:
139	        import torch as _torch
140	        state_dict = _torch.load(Path(model_dir) / "pytorch_model.bin", map_location="cpu")
141	    model.load_state_dict(state_dict, strict=False)
142	    model = model.to(device).eval()
143	
144	    processor = XVLAProcessor.from_pretrained(model_dir, trust_remote_code=True)
145	    if processor.tokenizer.pad_token is None:
146	        processor.tokenizer.pad_token = "&lt;pad>"
147	        processor.tokenizer.pad_token_id = 1
148	
149	    n_params = sum(p.numel() for p in model.parameters())
150	    log.info("Model loaded: %.1fM params, dtype=%s", n_params / 1e6, model.dtype)
151	    return model, processor
152	
153	
154	# ---------------------------------------------------------------------------
155	# 6D rotation utilities (following X-VLA's convention)
156	# ---------------------------------------------------------------------------
157	
158	def mat_to_rot6d(R: np.ndarray) -> np.ndarray:
159	    """Extract 6D rotation from 3x3 rotation matrix: first two columns."""
160	    return np.concatenate([R[:3, 0], R[:3, 1]], axis=-1).astype(np.float32)
161	
162	
163	def rot6d_to_axis_angle(r6d: np.ndarray) -> np.ndarray:
164	    """Convert 6D rotation representation to axis-angle via Gram-Schmidt."""
165	    import robosuite.utils.transform_utils as T
166	
167	    single = r6d.ndim == 1
168	    if single:
169	        r6d = r6d[None, :]
170	
171	    a1 = r6d[:, 0:3]
172	    a2 = r6d[:, 3:6]
173	
174	    b1 = a1 / (np.linalg.norm(a1, axis=-1, keepdims=True) + EPS)
175	    dot_prod = np.sum(b1 * a2, axis=-1, keepdims=True)
176	    b2_orth = a2 - dot_prod * b1
177	    b2 = b2_orth / (np.linalg.norm(b2_orth, axis=-1, keepdims=True) + EPS)
178	    b3 = np.cross(b1, b2, axis=-1)
179	
180	    R = np.stack([b1, b2, b3], axis=-1)  # (N, 3, 3)
181	
182	    results = []
183	    for i in range(R.shape[0]):
184	        quat = T.mat2quat(R[i])
185	        aa = T.quat2axisangle(quat)
186	        results.append(aa)
187	
188	    result = np.stack(results, axis=0)
189	    return result[0] if single else result
190	
191	
192	# ---------------------------------------------------------------------------
193	# Observation processing
194	# ---------------------------------------------------------------------------
195	
196	def extract_proprio_20d(env) -> np.ndarray:
197	    """Extract 20D proprio: [pos(3)+rot6d(6)+0.0] + zeros(10) from env robot state."""
198	    robot = env.env.robots[0]
199	    ee_pos = robot.controller.ee_pos.copy()         # (3,)
200	    ee_ori_mat = robot.controller.ee_ori_mat.copy()  # (3, 3)
201	    ee_rot6d = mat_to_rot6d(ee_ori_mat)              # (6,)
202	
203	    arm1 = np.concatenate([ee_pos, ee_rot6d, np.array([0.0], dtype=np.float32)])  # (10,)
204	    arm2 = np.zeros(10, dtype=np.float32)
205	    return np.concatenate([arm1, arm2])  # (20,)
206	
207	
208	def decode_action_20d_to_7d(action_20d: np.ndarray) -> np.ndarray:
209	    """Convert 20D X-VLA action to 7D LIBERO action.
210	
211	    Input:  [pos(3), rot6d(6), grip(1), arm2(10)]  — only arm1 used
212	    Output: [pos(3), axis_angle(3), grip(1)]
213	    """
214	    single = action_20d.ndim == 1
215	    if single:
216	        action_20d = action_20d[None, :]
217	
218	    pos = action_20d[:, :3]
219	    rot6d = action_20d[:, 3:9]
220	    grip = action_20d[:, 9:10]
221	
222	    axis_angle = rot6d_to_axis_angle(rot6d)
223	
224	    # Discretize gripper: >0.5 → 1.0 (open), else -1.0 (close)
225	    grip_disc = np.where(grip > 0.5, 1.0, -1.0)
226	
227	    result = np.concatenate([pos, axis_angle, grip_disc], axis=-1).astype(np.float32)
228	    return result[0] if single else result
229	
230	
231	def get_images_from_obs(obs) -> list:
232	    """Extract camera images from LIBERO observation, apply agentview flip."""
233	    images = []
234	    for cam_name in ["agentview_image", "robot0_eye_in_hand_image"]:
235	        img = obs.get(cam_name, None)
236	        if img is None:
237	            for k, v in obs.items():
238	                if cam_name in k and isinstance(v, np.ndarray):
239	                    img = v
240	                    break
241	        if img is not None:
242	            if img.dtype in (np.float32, np.float64):
243	                img = (np.clip(img, 0, 1) * 255).astype(np.uint8)
244	            if cam_name == "agentview_image":
245	                img = np.flip(np.flip(img, 0), 1).copy()
246	            images.append(Image.fromarray(img))
247	    return images
248	
249	
250	# ---------------------------------------------------------------------------
251	# Action prediction
252	# ---------------------------------------------------------------------------
253	
254	@torch.no_grad()
255	def predict_actions(model, processor, images, task_desc, proprio_20d, domain_id,
256	                    device, denoise_steps=10):
257	    inputs = processor(images=images, language_instruction=task_desc)
258	
259	    proprio_t = torch.tensor(proprio_20d, dtype=torch.float32).unsqueeze(0).to(device)
260	    domain_t = torch.tensor([domain_id], dtype=torch.long).to(device)
261	
262	    for k, v in inputs.items():
263	        if isinstance(v, torch.Tensor):
264	            if v.is_floating_point():
265	                inputs[k] = v.to(device=device, dtype=torch.float32)
266	            else:
267	                inputs[k] = v.to(device=device)
268	
269	    actions = model.generate_actions(
270	        input_ids=inputs["input_ids"],
271	        image_input=inputs["image_input"],
272	        image_mask=inputs["image_mask"],
273	        proprio=proprio_t,
274	        domain_id=domain_t,
275	        steps=denoise_steps,
276	    )  # [1, 30, 20]
277	
278	    return actions.squeeze(0).float().cpu().numpy()  # [30, 20]
279	
280	
281	# ---------------------------------------------------------------------------
282	# Wilson CI
283	# ---------------------------------------------------------------------------
284	
285	def wilson_ci(successes, total, z=1.96):
286	    if total == 0:
287	        return 0.0, 0.0, 1.0
288	    p = successes / total
289	    denom = 1 + z ** 2 / total
290	    center = (p + z ** 2 / (2 * total)) / denom
291	    spread = z * np.sqrt((p * (1 - p) + z ** 2 / (4 * total)) / total) / denom
292	    return center, max(0.0, center - spread), min(1.0, center + spread)
293	
294	
295	# ---------------------------------------------------------------------------
296	# Main evaluation
297	# ---------------------------------------------------------------------------
298	
299	def run_evaluation(args):
300	    device = torch.device(f"cuda:{args.gpu}" if torch.cuda.is_available() else "cpu")
301	    max_steps = args.max_steps or SUITE_MAX_STEPS.get(args.suite, 800)
302	    output_path = Path(args.output or
303	                       f"eval_results/xvla_prune_k{args.keep_ratio}_{args.suite}.json")
304	
305	    log.info("Suite: %s | Device: %s | keep_ratio=%.2f | Episodes/task: %d | Max steps: %d",
306	             args.suite, device, args.keep_ratio, args.num_episodes, max_steps)
307	
308	    np.random.seed(args.seed)
309	    torch.manual_seed(args.seed)
310	
311	    t0 = time_mod.time()
312	    model, processor = load_model(args.model_path, device)
313	    log.info("Model loaded in %.1fs", time_mod.time() - t0)
314	
315	    dummy_img = torch.randn(1, 3, 224, 224, device=device)
316	    with torch.no_grad():
317	        dummy_feats = model.vlm._encode_image(dummy_img)
318	    n_vis_tokens = dummy_feats.shape[1]
319	    k_tokens = max(1, int(args.keep_ratio * n_vis_tokens))
320	    log.info("Vision tokens: %d total, keeping %d (%.0f%%)",
321	             n_vis_tokens, k_tokens, args.keep_ratio * 100)
322	
323	    install_vision_pruning(model, args.keep_ratio, args.mode)
324	
325	    num_actions_per_chunk = model.num_actions  # 30
326	
327	    # LIBERO setup — use OffScreenRenderEnv directly (matching official X-VLA eval)
328	    from libero.libero import benchmark, get_libero_path
329	    from libero.libero.envs import OffScreenRenderEnv
330	
331	    task_suite = benchmark.get_benchmark(args.suite)()
332	    n_tasks = task_suite.n_tasks
333	
334	    if args.task_ids:
335	        task_id_list = [int(x) for x in args.task_ids.split(",")]
336	    else:
337	        task_id_list = list(range(n_tasks))
338	
339	    eval_start = time_mod.time()
340	    all_task_results = {}
341	    total_successes = 0
342	    total_episodes = 0
343	
344	    for task_id in task_id_list:
345	        task = task_suite.get_task(task_id)
346	        task_desc = task.language
347	        task_bddl = os.path.join(
348	            get_libero_path("bddl_files"), task.problem_folder, task.bddl_file
349	        )
350	        log.info("--- Task %d: %s ---", task_id, task_desc)
351	
352	        init_states = task_suite.get_task_init_states(task_id)
353	
354	        task_successes = []
355	        task_lengths = []
356	
357	        for ep in range(args.num_episodes):
358	            env = OffScreenRenderEnv(
359	                bddl_file_name=task_bddl,
360	                camera_heights=256,
361	                camera_widths=256,
362	            )
363	            env.seed(args.seed + ep + 100)
364	            obs = env.reset()
365	
366	            init_state_id = ep % init_states.shape[0]
367	            obs = env.set_init_state(init_states[init_state_id])
368	
369	            # Settle the robot with neutral actions
370	            for _ in range(10):
371	                neutral = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0], dtype=np.float32)
372	                obs, _, _, _ = env.step(neutral)
373	
374	            # Switch to absolute control
375	            for robot in env.env.robots:
376	                robot.controller.use_delta = False
377	
378	            action_queue = []
379	            proprio_state = None
380	            success = False
381	
382	            for step_idx in range(max_steps):
383	                if not action_queue:
384	                    # Extract proprio from env
385	                    proprio_20d = extract_proprio_20d(env)
386	                    if proprio_state is not None:
387	                        proprio_20d[:9] = proprio_state[:9]
388	
389	                    images = get_images_from_obs(obs)
390	                    if not images:
391	                        raise ValueError(f"No images found in obs keys: {list(obs.keys())}")
392	
393	                    raw_actions = predict_actions(
394	                        model, processor, images, task_desc, proprio_20d,
395	                        args.domain_id, device, args.denoise_steps,
396	                    )  # [30, 20]
397	
398	                    # Update closed-loop proprio with last predicted action
399	                    proprio_state = proprio_20d.copy()
400	                    proprio_state[:9] = raw_actions[-1, :9].copy()
401	
402	                    actions_7d = decode_action_20d_to_7d(raw_actions)  # [30, 7]
403	                    action_queue = list(actions_7d)
404	
405	                action = action_queue.pop(0)
406	                obs, reward, done, info = env.step(action)
407	
408	                if done or reward > 0.5:
409	                    success = True
410	                    break
411	
412	            ep_steps = step_idx + 1
413	            task_successes.append(success)
414	            task_lengths.append(ep_steps)
415	            log.info("  Ep %d/%d | %s | steps=%d",
416	                     ep + 1, args.num_episodes,
417	                     "SUCCESS" if success else "FAIL", ep_steps)
418	
419	            env.close()
420	
421	        n_succ = sum(task_successes)
422	        n_total = len(task_successes)
423	        sr = n_succ / n_total if n_total > 0 else 0.0
424	
425	        all_task_results[task_id] = {
426	            "task_id": task_id,
427	            "task_description": task_desc,
428	            "success_count": n_succ,
429	            "total_episodes": n_total,
430	            "success_rate": round(sr, 4),
431	            "mean_steps": round(float(np.mean(task_lengths)), 1),
432	        }
433	        total_successes += n_succ
434	        total_episodes += n_total
435	        log.info("  Task %d SR: %d/%d (%.1f%%)", task_id, n_succ, n_total, sr * 100)
436	
437	    elapsed = time_mod.time() - eval_start
438	    overall_sr = total_successes / total_episodes if total_episodes > 0 else 0.0
439	    _, ci_lo, ci_hi = wilson_ci(total_successes, total_episodes)
440	
441	    log.info("=" * 60)
442	    log.info("SUITE: %s | MODEL: xvla | keep_ratio: %.2f", args.suite, args.keep_ratio)
443	    log.info("Overall SR: %d/%d (%.1f%%)", total_successes, total_episodes, overall_sr * 100)
444	    log.info("95%% Wilson CI: [%.1f%%, %.1f%%]", ci_lo * 100, ci_hi * 100)
445	    for tid, tr in sorted(all_task_results.items()):
446	        log.info("  Task %d: %.0f%% (%d/%d) -- %s",
447	                 tid, tr["success_rate"] * 100, tr["success_count"],
448	                 tr["total_episodes"], tr["task_description"])
449	    log.info("Elapsed: %.1f min", elapsed / 60)
450	    log.info("=" * 60)
451	
452	    summary = {
453	        "model": "xvla",
454	        "model_path": args.model_path,
455	        "mode": args.mode,
456	        "suite": args.suite,
457	        "keep_ratio": args.keep_ratio,
458	        "n_vision_tokens_original": n_vis_tokens,
459	        "n_vision_tokens_kept": k_tokens,
460	        "total_episodes": total_episodes,
461	        "total_successes": total_successes,
462	        "overall_success_rate": round(overall_sr, 4),
463	        "wilson_ci_95": [round(ci_lo, 4), round(ci_hi, 4)],
464	        "num_episodes_per_task": args.num_episodes,
465	        "max_steps": max_steps,
466	        "num_actions_per_chunk": num_actions_per_chunk,
467	        "domain_id": args.domain_id,
468	        "denoise_steps": args.denoise_steps,
469	        "seed": args.seed,
470	        "elapsed_seconds": round(elapsed, 1),
471	        "per_task": all_task_results,
472	    }
473	
474	    output_path.parent.mkdir(parents=True, exist_ok=True)
475	    with open(output_path, "w") as f:
476	        json.dump(summary, f, indent=2)
477	    log.info("Results saved to %s", output_path)
478	
479	    return summary
480	
481	
482	if __name__ == "__main__":
483	    args = parse_args()
484	    run_evaluation(args)
485	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a",
  "uuid": "4645eabb-7763-43d5-8934-c3480007363b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/eval_xvla_pruning_libero.py",
      "content": "\"\"\"X-VLA Vision Token Pruning Evaluation on LIBERO.\n\nPrunes vision tokens by L2 norm after Florence2's image encoder + linear projection,\nbefore they enter the Florence2 language encoder. Evaluates on LIBERO suites.\n\nFollows official X-VLA evaluation protocol:\n  - Absolute EEF control (use_delta=False)\n  - 20D action space: [arm1: pos(3)+rot6d(6)+grip(1)] + [arm2: zeros(10)]\n  - 20D proprio: [pos(3)+rot6d(6)+0.0] + zeros(10)\n  - domain_id=3 for LIBERO\n  - Closed-loop proprio update from last predicted action\n\nUsage:\n    CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl python eval_xvla_pruning_libero.py \\\n        --model_path /path/to/X-VLA-Libero \\\n        --suite libero_object \\\n        --keep_ratio 0.5 \\\n        --num_episodes 50 \\\n        --gpu 0\n\"\"\"\n\nfrom __future__ import annotations\n\nimport argparse\nimport json\nimport logging\nimport os\nimport sys\nimport time as time_mod\nfrom pathlib import Path\nfrom functools import wraps\n\nos.environ.setdefault(\"MUJOCO_GL\", \"egl\")\n\nimport numpy as np\nimport torch\nfrom PIL import Image\n\nsys.path.insert(0, str(Path(__file__).resolve().parent))\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    datefmt=\"%Y-%m-%d %H:%M:%S\",\n)\nlog = logging.getLogger(__name__)\n\nSUITE_MAX_STEPS = {\n    \"libero_spatial\": 800,\n    \"libero_object\": 800,\n    \"libero_goal\": 800,\n    \"libero_10\": 900,\n    \"libero_90\": 800,\n}\n\nEPS = 1e-6\n\n\ndef parse_args():\n    p = argparse.ArgumentParser(description=\"X-VLA pruning eval on LIBERO\")\n    p.add_argument(\"--model_path\", type=str, default=\"2toINF/X-VLA-Libero\",\n                   help=\"HuggingFace model path or local dir\")\n    p.add_argument(\"--suite\", type=str, default=\"libero_object\",\n                   choices=list(SUITE_MAX_STEPS.keys()))\n    p.add_argument(\"--keep_ratio\", type=float, default=1.0,\n                   help=\"Fraction of vision tokens to keep (1.0 = no pruning)\")\n    p.add_argument(\"--num_episodes\", type=int, default=50)\n    p.add_argument(\"--gpu\", type=int, default=0)\n    p.add_argument(\"--seed\", type=int, default=42)\n    p.add_argument(\"--max_steps\", type=int, default=None)\n    p.add_argument(\"--output\", type=str, default=None)\n    p.add_argument(\"--task_ids\", type=str, default=None)\n    p.add_argument(\"--domain_id\", type=int, default=3)\n    p.add_argument(\"--denoise_steps\", type=int, default=10,\n                   help=\"Flow matching denoising steps\")\n    p.add_argument(\"--mode\", type=str, default=\"l2_norm\",\n                   choices=[\"l2_norm\", \"random\"],\n                   help=\"Pruning method: l2_norm (keep highest L2 norm tokens) or random (random selection)\")\n    return p.parse_args()\n\n\n# ---------------------------------------------------------------------------\n# Pruning hook\n# ---------------------------------------------------------------------------\n\ndef install_vision_pruning(model, keep_ratio: float, mode: str = \"l2_norm\"):\n    if keep_ratio >= 1.0:\n        log.info(\"keep_ratio=%.2f, no pruning applied\", keep_ratio)\n        return\n\n    original_encode = model.vlm._encode_image\n\n    @wraps(original_encode)\n    def pruned_encode(pixel_values):\n        features = original_encode(pixel_values)\n        N = features.shape[1]\n        k = max(1, int(keep_ratio * N))\n        if k >= N:\n            return features\n        if mode == \"l2_norm\":\n            norms = features.norm(dim=-1)\n            _, indices = norms.topk(k, dim=-1)\n        elif mode == \"random\":\n            indices = torch.stack([\n                torch.randperm(N, device=features.device)[:k]\n                for _ in range(features.shape[0])\n            ], dim=0)\n        indices_sorted = indices.sort(dim=-1).values\n        pruned = features.gather(\n            1, indices_sorted.unsqueeze(-1).expand(-1, -1, features.shape[-1])\n        )\n        return pruned\n\n    model.vlm._encode_image = pruned_encode\n    log.info(\"Vision pruning installed: keep_ratio=%.2f, mode=%s\", keep_ratio, mode)\n\n\n# ---------------------------------------------------------------------------\n# Model loading\n# ---------------------------------------------------------------------------\n\ndef load_model(model_path: str, device: torch.device):\n    model_dir = str(Path(model_path).resolve())\n    sys.path.insert(0, model_dir)\n\n    from configuration_xvla import XVLAConfig\n    from modeling_xvla import XVLA\n    from processing_xvla import XVLAProcessor\n    from safetensors.torch import load_file\n\n    log.info(\"Loading X-VLA from %s\", model_dir)\n    config = XVLAConfig.from_pretrained(model_dir)\n    model = XVLA(config)\n\n    safetensors_path = Path(model_dir) / \"model.safetensors\"\n    if safetensors_path.exists():\n        state_dict = load_file(str(safetensors_path))\n    else:\n        import torch as _torch\n        state_dict = _torch.load(Path(model_dir) / \"pytorch_model.bin\", map_location=\"cpu\")\n    model.load_state_dict(state_dict, strict=False)\n    model = model.to(device).eval()\n\n    processor = XVLAProcessor.from_pretrained(model_dir, trust_remote_code=True)\n    if processor.tokenizer.pad_token is None:\n        processor.tokenizer.pad_token = \"&lt;pad>\"\n        processor.tokenizer.pad_token_id = 1\n\n    n_params = sum(p.numel() for p in model.parameters())\n    log.info(\"Model loaded: %.1fM params, dtype=%s\", n_params / 1e6, model.dtype)\n    return model, processor\n\n\n# ---------------------------------------------------------------------------\n# 6D rotation utilities (following X-VLA's convention)\n# ---------------------------------------------------------------------------\n\ndef mat_to_rot6d(R: np.ndarray) -> np.ndarray:\n    \"\"\"Extract 6D rotation from 3x3 rotation matrix: first two columns.\"\"\"\n    return np.concatenate([R[:3, 0], R[:3, 1]], axis=-1).astype(np.float32)\n\n\ndef rot6d_to_axis_angle(r6d: np.ndarray) -> np.ndarray:\n    \"\"\"Convert 6D rotation representation to axis-angle via Gram-Schmidt.\"\"\"\n    import robosuite.utils.transform_utils as T\n\n    single = r6d.ndim == 1\n    if single:\n        r6d = r6d[None, :]\n\n    a1 = r6d[:, 0:3]\n    a2 = r6d[:, 3:6]\n\n    b1 = a1 / (np.linalg.norm(a1, axis=-1, keepdims=True) + EPS)\n    dot_prod = np.sum(b1 * a2, axis=-1, keepdims=True)\n    b2_orth = a2 - dot_prod * b1\n    b2 = b2_orth / (np.linalg.norm(b2_orth, axis=-1, keepdims=True) + EPS)\n    b3 = np.cross(b1, b2, axis=-1)\n\n    R = np.stack([b1, b2, b3], axis=-1)  # (N, 3, 3)\n\n    results = []\n    for i in range(R.shape[0]):\n        quat = T.mat2quat(R[i])\n        aa = T.quat2axisangle(quat)\n        results.append(aa)\n\n    result = np.stack(results, axis=0)\n    return result[0] if single else result\n\n\n# ---------------------------------------------------------------------------\n# Observation processing\n# ---------------------------------------------------------------------------\n\ndef extract_proprio_20d(env) -> np.ndarray:\n    \"\"\"Extract 20D proprio: [pos(3)+rot6d(6)+0.0] + zeros(10) from env robot state.\"\"\"\n    robot = env.env.robots[0]\n    ee_pos = robot.controller.ee_pos.copy()         # (3,)\n    ee_ori_mat = robot.controller.ee_ori_mat.copy()  # (3, 3)\n    ee_rot6d = mat_to_rot6d(ee_ori_mat)              # (6,)\n\n    arm1 = np.concatenate([ee_pos, ee_rot6d, np.array([0.0], dtype=np.float32)])  # (10,)\n    arm2 = np.zeros(10, dtype=np.float32)\n    return np.concatenate([arm1, arm2])  # (20,)\n\n\ndef decode_action_20d_to_7d(action_20d: np.ndarray) -> np.ndarray:\n    \"\"\"Convert 20D X-VLA action to 7D LIBERO action.\n\n    Input:  [pos(3), rot6d(6), grip(1), arm2(10)]  — only arm1 used\n    Output: [pos(3), axis_angle(3), grip(1)]\n    \"\"\"\n    single = action_20d.ndim == 1\n    if single:\n        action_20d = action_20d[None, :]\n\n    pos = action_20d[:, :3]\n    rot6d = action_20d[:, 3:9]\n    grip = action_20d[:, 9:10]\n\n    axis_angle = rot6d_to_axis_angle(rot6d)\n\n    # Discretize gripper: >0.5 → 1.0 (open), else -1.0 (close)\n    grip_disc = np.where(grip > 0.5, 1.0, -1.0)\n\n    result = np.concatenate([pos, axis_angle, grip_disc], axis=-1).astype(np.float32)\n    return result[0] if single else result\n\n\ndef get_images_from_obs(obs) -> list:\n    \"\"\"Extract camera images from LIBERO observation, apply agentview flip.\"\"\"\n    images = []\n    for cam_name in [\"agentview_image\", \"robot0_eye_in_hand_image\"]:\n        img = obs.get(cam_name, None)\n        if img is None:\n            for k, v in obs.items():\n                if cam_name in k and isinstance(v, np.ndarray):\n                    img = v\n                    break\n        if img is not None:\n            if img.dtype in (np.float32, np.float64):\n                img = (np.clip(img, 0, 1) * 255).astype(np.uint8)\n            if cam_name == \"agentview_image\":\n                img = np.flip(np.flip(img, 0), 1).copy()\n            images.append(Image.fromarray(img))\n    return images\n\n\n# ---------------------------------------------------------------------------\n# Action prediction\n# ---------------------------------------------------------------------------\n\n@torch.no_grad()\ndef predict_actions(model, processor, images, task_desc, proprio_20d, domain_id,\n                    device, denoise_steps=10):\n    inputs = processor(images=images, language_instruction=task_desc)\n\n    proprio_t = torch.tensor(proprio_20d, dtype=torch.float32).unsqueeze(0).to(device)\n    domain_t = torch.tensor([domain_id], dtype=torch.long).to(device)\n\n    for k, v in inputs.items():\n        if isinstance(v, torch.Tensor):\n            if v.is_floating_point():\n                inputs[k] = v.to(device=device, dtype=torch.float32)\n            else:\n                inputs[k] = v.to(device=device)\n\n    actions = model.generate_actions(\n        input_ids=inputs[\"input_ids\"],\n        image_input=inputs[\"image_input\"],\n        image_mask=inputs[\"image_mask\"],\n        proprio=proprio_t,\n        domain_id=domain_t,\n        steps=denoise_steps,\n    )  # [1, 30, 20]\n\n    return actions.squeeze(0).float().cpu().numpy()  # [30, 20]\n\n\n# ---------------------------------------------------------------------------\n# Wilson CI\n# ---------------------------------------------------------------------------\n\ndef wilson_ci(successes, total, z=1.96):\n    if total == 0:\n        return 0.0, 0.0, 1.0\n    p = successes / total\n    denom = 1 + z ** 2 / total\n    center = (p + z ** 2 / (2 * total)) / denom\n    spread = z * np.sqrt((p * (1 - p) + z ** 2 / (4 * total)) / total) / denom\n    return center, max(0.0, center - spread), min(1.0, center + spread)\n\n\n# ---------------------------------------------------------------------------\n# Main evaluation\n# ---------------------------------------------------------------------------\n\ndef run_evaluation(args):\n    device = torch.device(f\"cuda:{args.gpu}\" if torch.cuda.is_available() else \"cpu\")\n    max_steps = args.max_steps or SUITE_MAX_STEPS.get(args.suite, 800)\n    output_path = Path(args.output or\n                       f\"eval_results/xvla_prune_k{args.keep_ratio}_{args.suite}.json\")\n\n    log.info(\"Suite: %s | Device: %s | keep_ratio=%.2f | Episodes/task: %d | Max steps: %d\",\n             args.suite, device, args.keep_ratio, args.num_episodes, max_steps)\n\n    np.random.seed(args.seed)\n    torch.manual_seed(args.seed)\n\n    t0 = time_mod.time()\n    model, processor = load_model(args.model_path, device)\n    log.info(\"Model loaded in %.1fs\", time_mod.time() - t0)\n\n    dummy_img = torch.randn(1, 3, 224, 224, device=device)\n    with torch.no_grad():\n        dummy_feats = model.vlm._encode_image(dummy_img)\n    n_vis_tokens = dummy_feats.shape[1]\n    k_tokens = max(1, int(args.keep_ratio * n_vis_tokens))\n    log.info(\"Vision tokens: %d total, keeping %d (%.0f%%)\",\n             n_vis_tokens, k_tokens, args.keep_ratio * 100)\n\n    install_vision_pruning(model, args.keep_ratio, args.mode)\n\n    num_actions_per_chunk = model.num_actions  # 30\n\n    # LIBERO setup — use OffScreenRenderEnv directly (matching official X-VLA eval)\n    from libero.libero import benchmark, get_libero_path\n    from libero.libero.envs import OffScreenRenderEnv\n\n    task_suite = benchmark.get_benchmark(args.suite)()\n    n_tasks = task_suite.n_tasks\n\n    if args.task_ids:\n        task_id_list = [int(x) for x in args.task_ids.split(\",\")]\n    else:\n        task_id_list = list(range(n_tasks))\n\n    eval_start = time_mod.time()\n    all_task_results = {}\n    total_successes = 0\n    total_episodes = 0\n\n    for task_id in task_id_list:\n        task = task_suite.get_task(task_id)\n        task_desc = task.language\n        task_bddl = os.path.join(\n            get_libero_path(\"bddl_files\"), task.problem_folder, task.bddl_file\n        )\n        log.info(\"--- Task %d: %s ---\", task_id, task_desc)\n\n        init_states = task_suite.get_task_init_states(task_id)\n\n        task_successes = []\n        task_lengths = []\n\n        for ep in range(args.num_episodes):\n            env = OffScreenRenderEnv(\n                bddl_file_name=task_bddl,\n                camera_heights=256,\n                camera_widths=256,\n            )\n            env.seed(args.seed + ep + 100)\n            obs = env.reset()\n\n            init_state_id = ep % init_states.shape[0]\n            obs = env.set_init_state(init_states[init_state_id])\n\n            # Settle the robot with neutral actions\n            for _ in range(10):\n                neutral = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0], dtype=np.float32)\n                obs, _, _, _ = env.step(neutral)\n\n            # Switch to absolute control\n            for robot in env.env.robots:\n                robot.controller.use_delta = False\n\n            action_queue = []\n            proprio_state = None\n            success = False\n\n            for step_idx in range(max_steps):\n                if not action_queue:\n                    # Extract proprio from env\n                    proprio_20d = extract_proprio_20d(env)\n                    if proprio_state is not None:\n                        proprio_20d[:9] = proprio_state[:9]\n\n                    images = get_images_from_obs(obs)\n                    if not images:\n                        raise ValueError(f\"No images found in obs keys: {list(obs.keys())}\")\n\n                    raw_actions = predict_actions(\n                        model, processor, images, task_desc, proprio_20d,\n                        args.domain_id, device, args.denoise_steps,\n                    )  # [30, 20]\n\n                    # Update closed-loop proprio with last predicted action\n                    proprio_state = proprio_20d.copy()\n                    proprio_state[:9] = raw_actions[-1, :9].copy()\n\n                    actions_7d = decode_action_20d_to_7d(raw_actions)  # [30, 7]\n                    action_queue = list(actions_7d)\n\n                action = action_queue.pop(0)\n                obs, reward, done, info = env.step(action)\n\n                if done or reward > 0.5:\n                    success = True\n                    break\n\n            ep_steps = step_idx + 1\n            task_successes.append(success)\n            task_lengths.append(ep_steps)\n            log.info(\"  Ep %d/%d | %s | steps=%d\",\n                     ep + 1, args.num_episodes,\n                     \"SUCCESS\" if success else \"FAIL\", ep_steps)\n\n            env.close()\n\n        n_succ = sum(task_successes)\n        n_total = len(task_successes)\n        sr = n_succ / n_total if n_total > 0 else 0.0\n\n        all_task_results[task_id] = {\n            \"task_id\": task_id,\n            \"task_description\": task_desc,\n            \"success_count\": n_succ,\n            \"total_episodes\": n_total,\n            \"success_rate\": round(sr, 4),\n            \"mean_steps\": round(float(np.mean(task_lengths)), 1),\n        }\n        total_successes += n_succ\n        total_episodes += n_total\n        log.info(\"  Task %d SR: %d/%d (%.1f%%)\", task_id, n_succ, n_total, sr * 100)\n\n    elapsed = time_mod.time() - eval_start\n    overall_sr = total_successes / total_episodes if total_episodes > 0 else 0.0\n    _, ci_lo, ci_hi = wilson_ci(total_successes, total_episodes)\n\n    log.info(\"=\" * 60)\n    log.info(\"SUITE: %s | MODEL: xvla | keep_ratio: %.2f\", args.suite, args.keep_ratio)\n    log.info(\"Overall SR: %d/%d (%.1f%%)\", total_successes, total_episodes, overall_sr * 100)\n    log.info(\"95%% Wilson CI: [%.1f%%, %.1f%%]\", ci_lo * 100, ci_hi * 100)\n    for tid, tr in sorted(all_task_results.items()):\n        log.info(\"  Task %d: %.0f%% (%d/%d) -- %s\",\n                 tid, tr[\"success_rate\"] * 100, tr[\"success_count\"],\n                 tr[\"total_episodes\"], tr[\"task_description\"])\n    log.info(\"Elapsed: %.1f min\", elapsed / 60)\n    log.info(\"=\" * 60)\n\n    summary = {\n        \"model\": \"xvla\",\n        \"model_path\": args.model_path,\n        \"mode\": args.mode,\n        \"suite\": args.suite,\n        \"keep_ratio\": args.keep_ratio,\n        \"n_vision_tokens_original\": n_vis_tokens,\n        \"n_vision_tokens_kept\": k_tokens,\n        \"total_episodes\": total_episodes,\n        \"total_successes\": total_successes,\n        \"overall_success_rate\": round(overall_sr, 4),\n        \"wilson_ci_95\": [round(ci_lo, 4), round(ci_hi, 4)],\n        \"num_episodes_per_task\": args.num_episodes,\n        \"max_steps\": max_steps,\n        \"num_actions_per_chunk\": num_actions_per_chunk,\n        \"domain_id\": args.domain_id,\n        \"denoise_steps\": args.denoise_steps,\n        \"seed\": args.seed,\n        \"elapsed_seconds\": round(elapsed, 1),\n        \"per_task\": all_task_results,\n    }\n\n    output_path.parent.mkdir(parents=True, exist_ok=True)\n    with open(output_path, \"w\") as f:\n        json.dump(summary, f, indent=2)\n    log.info(\"Results saved to %s\", output_path)\n\n    return summary\n\n\nif __name__ == \"__main__\":\n    args = parse_args()\n    run_evaluation(args)\n",
      "numLines": 485,
      "startLine": 1,
      "totalLines": 485
    }
  }
}
```

</details>

---

### Assistant

_source line 37_

文件确认无误。现在用 `cat <<'PYEOF'` 方式部署到两台服务器。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a",
  "uuid": "fbd188d5-23aa-44a5-9f47-c9071da2b52a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011zqFrFkRJRVEocQ7jM3LAw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6965,
      "cache_read_input_tokens": 34134,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6965
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Bash · `toolu_0174LMTUZaHgPP6CKgiF78NH`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/eval_xvla_pruning_libero.py | base64 -w0",
  "description": "Base64 encode script for safe SSH transfer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a",
  "uuid": "e679663d-9521-495c-8286-b45d66ff03b1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011zqFrFkRJRVEocQ7jM3LAw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6965,
      "cache_read_input_tokens": 34134,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6965
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-21T02:22:15.554Z_

<details><summary>↩ Tool result · `toolu_0174LMTUZaHgPP6CKgiF78NH`</summary>

```text
[ATTACHMENT_DATA_REDACTED]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a",
  "uuid": "e3e29628-4cc2-4b40-aaa7-b1f566563a5d",
  "tool_use_result": {
    "stdout": "[ATTACHMENT_DATA_REDACTED]",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 40_

<details><summary>Logged reasoning block</summary>

```text
Now I need to deploy this file to both servers. I'll use the base64 encoded content to write it via ssh_execute.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a",
  "uuid": "e7f0861b-c536-4b73-a544-640ac0472fb0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T3fbFXHpmCJPQ6RGmcBui6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19339,
      "cache_read_input_tokens": 41099,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19339
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 41_

现在同时部署到两台服务器。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a",
  "uuid": "37b6bd5b-8314-40c8-a25a-2423004db44e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T3fbFXHpmCJPQ6RGmcBui6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19339,
      "cache_read_input_tokens": 41099,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19339
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 42_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01AsEF4BgjkVZhDNkR5GKMkJ`</summary>

```json
{
  "server": "cqa1-33015",
  "command": "cat > /root/autodl-tmp/importance_margin_vla_compress/eval_xvla_pruning_libero.py << 'PYEOF'\n\"\"\"X-VLA Vision Token Pruning Evaluation on LIBERO.\n\nPrunes vision tokens by L2 norm after Florence2's image encoder + linear projection,\nbefore they enter the Florence2 language encoder. Evaluates on LIBERO suites.\n\nFollows official X-VLA evaluation protocol:\n  - Absolute EEF control (use_delta=False)\n  - 20D action space: [arm1: pos(3)+rot6d(6)+grip(1)] + [arm2: zeros(10)]\n  - 20D proprio: [pos(3)+rot6d(6)+0.0] + zeros(10)\n  - domain_id=3 for LIBERO\n  - Closed-loop proprio update from last predicted action\n\nUsage:\n    CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl python eval_xvla_pruning_libero.py \\\n        --model_path /path/to/X-VLA-Libero \\\n        --suite libero_object \\\n        --keep_ratio 0.5 \\\n        --num_episodes 50 \\\n        --gpu 0\n\"\"\"\n\nfrom __future__ import annotations\n\nimport argparse\nimport json\nimport logging\nimport os\nimport sys\nimport time as time_mod\nfrom pathlib import Path\nfrom functools import wraps\n\nos.environ.setdefault(\"MUJOCO_GL\", \"egl\")\n\nimport numpy as np\nimport torch\nfrom PIL import Image\n\nsys.path.insert(0, str(Path(__file__).resolve().parent))\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    datefmt=\"%Y-%m-%d %H:%M:%S\",\n)\nlog = logging.getLogger(__name__)\n\nSUITE_MAX_STEPS = {\n    \"libero_spatial\": 800,\n    \"libero_object\": 800,\n    \"libero_goal\": 800,\n    \"libero_10\": 900,\n    \"libero_90\": 800,\n}\n\nEPS = 1e-6\n\n\ndef parse_args():\n    p = argparse.ArgumentParser(description=\"X-VLA pruning eval on LIBERO\")\n    p.add_argument(\"--model_path\", type=str, default=\"2toINF/X-VLA-Libero\",\n                   help=\"HuggingFace model path or local dir\")\n    p.add_argument(\"--suite\", type=str, default=\"libero_object\",\n                   choices=list(SUITE_MAX_STEPS.keys()))\n    p.add_argument(\"--keep_ratio\", type=float, default=1.0,\n                   help=\"Fraction of vision tokens to keep (1.0 = no pruning)\")\n    p.add_argument(\"--num_episodes\", type=int, default=50)\n    p.add_argument(\"--gpu\", type=int, default=0)\n    p.add_argument(\"--seed\", type=int, default=42)\n    p.add_argument(\"--max_steps\", type=int, default=None)\n    p.add_argument(\"--output\", type=str, default=None)\n    p.add_argument(\"--task_ids\", type=str, default=None)\n    p.add_argument(\"--domain_id\", type=int, default=3)\n    p.add_argument(\"--denoise_steps\", type=int, default=10,\n                   help=\"Flow matching denoising steps\")\n    p.add_argument(\"--mode\", type=str, default=\"l2_norm\",\n                   choices=[\"l2_norm\", \"random\"],\n                   help=\"Pruning method: l2_norm (keep highest L2 norm tokens) or random (random selection)\")\n    return p.parse_args()\n\n\n# ---------------------------------------------------------------------------\n# Pruning hook\n# ---------------------------------------------------------------------------\n\ndef install_vision_pruning(model, keep_ratio: float, mode: str = \"l2_norm\"):\n    if keep_ratio >= 1.0:\n        log.info(\"keep_ratio=%.2f, no pruning applied\", keep_ratio)\n        return\n\n    original_encode = model.vlm._encode_image\n\n    @wraps(original_encode)\n    def pruned_encode(pixel_values):\n        features = original_encode(pixel_values)\n        N = features.shape[1]\n        k = max(1, int(keep_ratio * N))\n        if k >= N:\n            return features\n        if mode == \"l2_norm\":\n            norms = features.norm(dim=-1)\n            _, indices = norms.topk(k, dim=-1)\n        elif mode == \"random\":\n            indices = torch.stack([\n                torch.randperm(N, device=features.device)[:k]\n                for _ in range(features.shape[0])\n            ], dim=0)\n        indices_sorted = indices.sort(dim=-1).values\n        pruned = features.gather(\n            1, indices_sorted.unsqueeze(-1).expand(-1, -1, features.shape[-1])\n        )\n        return pruned\n\n    model.vlm._encode_image = pruned_encode\n    log.info(\"Vision pruning installed: keep_ratio=%.2f, mode=%s\", keep_ratio, mode)\n\n\n# ---------------------------------------------------------------------------\n# Model loading\n# ---------------------------------------------------------------------------\n\ndef load_model(model_path: str, device: torch.device):\n    model_dir = str(Path(model_path).resolve())\n    sys.path.insert(0, model_dir)\n\n    from configuration_xvla import XVLAConfig\n    from modeling_xvla import XVLA\n    from processing_xvla import XVLAProcessor\n    from safetensors.torch import load_file\n\n    log.info(\"Loading X-VLA from %s\", model_dir)\n    config = XVLAConfig.from_pretrained(model_dir)\n    model = XVLA(config)\n\n    safetensors_path = Path(model_dir) / \"model.safetensors\"\n    if safetensors_path.exists():\n        state_dict = load_file(str(safetensors_path))\n    else:\n        import torch as _torch\n        state_dict = _torch.load(Path(model_dir) / \"pytorch_model.bin\", map_location=\"cpu\")\n    model.load_state_dict(state_dict, strict=False)\n    model = model.to(device).eval()\n\n    processor = XVLAProcessor.from_pretrained(model_dir, trust_remote_code=True)\n    if processor.tokenizer.pad_token is None:\n        processor.tokenizer.pad_token = \"&lt;pad>\"\n        processor.tokenizer.pad_token_id = 1\n\n    n_params = sum(p.numel() for p in model.parameters())\n    log.info(\"Model loaded: %.1fM params, dtype=%s\", n_params / 1e6, model.dtype)\n    return model, processor\n\n\n# ---------------------------------------------------------------------------\n# 6D rotation utilities (following X-VLA's convention)\n# ---------------------------------------------------------------------------\n\ndef mat_to_rot6d(R: np.ndarray) -> np.ndarray:\n    \"\"\"Extract 6D rotation from 3x3 rotation matrix: first two columns.\"\"\"\n    return np.concatenate([R[:3, 0], R[:3, 1]], axis=-1).astype(np.float32)\n\n\ndef rot6d_to_axis_angle(r6d: np.ndarray) -> np.ndarray:\n    \"\"\"Convert 6D rotation representation to axis-angle via Gram-Schmidt.\"\"\"\n    import robosuite.utils.transform_utils as T\n\n    single = r6d.ndim == 1\n    if single:\n        r6d = r6d[None, :]\n\n    a1 = r6d[:, 0:3]\n    a2 = r6d[:, 3:6]\n\n    b1 = a1 / (np.linalg.norm(a1, axis=-1, keepdims=True) + EPS)\n    dot_prod = np.sum(b1 * a2, axis=-1, keepdims=True)\n    b2_orth = a2 - dot_prod * b1\n    b2 = b2_orth / (np.linalg.norm(b2_orth, axis=-1, keepdims=True) + EPS)\n    b3 = np.cross(b1, b2, axis=-1)\n\n    R = np.stack([b1, b2, b3], axis=-1)  # (N, 3, 3)\n\n    results = []\n    for i in range(R.shape[0]):\n        quat = T.mat2quat(R[i])\n        aa = T.quat2axisangle(quat)\n        results.append(aa)\n\n    result = np.stack(results, axis=0)\n    return result[0] if single else result\n\n\n# ---------------------------------------------------------------------------\n# Observation processing\n# ---------------------------------------------------------------------------\n\ndef extract_proprio_20d(env) -> np.ndarray:\n    \"\"\"Extract 20D proprio: [pos(3)+rot6d(6)+0.0] + zeros(10) from env robot state.\"\"\"\n    robot = env.env.robots[0]\n    ee_pos = robot.controller.ee_pos.copy()         # (3,)\n    ee_ori_mat = robot.controller.ee_ori_mat.copy()  # (3, 3)\n    ee_rot6d = mat_to_rot6d(ee_ori_mat)              # (6,)\n\n    arm1 = np.concatenate([ee_pos, ee_rot6d, np.array([0.0], dtype=np.float32)])  # (10,)\n    arm2 = np.zeros(10, dtype=np.float32)\n    return np.concatenate([arm1, arm2])  # (20,)\n\n\ndef decode_action_20d_to_7d(action_20d: np.ndarray) -> np.ndarray:\n    \"\"\"Convert 20D X-VLA action to 7D LIBERO action.\n\n    Input:  [pos(3), rot6d(6), grip(1), arm2(10)]  — only arm1 used\n    Output: [pos(3), axis_angle(3), grip(1)]\n    \"\"\"\n    single = action_20d.ndim == 1\n    if single:\n        action_20d = action_20d[None, :]\n\n    pos = action_20d[:, :3]\n    rot6d = action_20d[:, 3:9]\n    grip = action_20d[:, 9:10]\n\n    axis_angle = rot6d_to_axis_angle(rot6d)\n\n    # Discretize gripper: >0.5 → 1.0 (open), else -1.0 (close)\n    grip_disc = np.where(grip > 0.5, 1.0, -1.0)\n\n    result = np.concatenate([pos, axis_angle, grip_disc], axis=-1).astype(np.float32)\n    return result[0] if single else result\n\n\ndef get_images_from_obs(obs) -> list:\n    \"\"\"Extract camera images from LIBERO observation, apply agentview flip.\"\"\"\n    images = []\n    for cam_name in [\"agentview_image\", \"robot0_eye_in_hand_image\"]:\n        img = obs.get(cam_name, None)\n        if img is None:\n            for k, v in obs.items():\n                if cam_name in k and isinstance(v, np.ndarray):\n                    img = v\n                    break\n        if img is not None:\n            if img.dtype in (np.float32, np.float64):\n                img = (np.clip(img, 0, 1) * 255).astype(np.uint8)\n            if cam_name == \"agentview_image\":\n                img = np.flip(np.flip(img, 0), 1).copy()\n            images.append(Image.fromarray(img))\n    return images\n\n\n# ---------------------------------------------------------------------------\n# Action prediction\n# ---------------------------------------------------------------------------\n\n@torch.no_grad()\ndef predict_actions(model, processor, images, task_desc, proprio_20d, domain_id,\n                    device, denoise_steps=10):\n    inputs = processor(images=images, language_instruction=task_desc)\n\n    proprio_t = torch.tensor(proprio_20d, dtype=torch.float32).unsqueeze(0).to(device)\n    domain_t = torch.tensor([domain_id], dtype=torch.long).to(device)\n\n    for k, v in inputs.items():\n        if isinstance(v, torch.Tensor):\n            if v.is_floating_point():\n                inputs[k] = v.to(device=device, dtype=torch.float32)\n            else:\n                inputs[k] = v.to(device=device)\n\n    actions = model.generate_actions(\n        input_ids=inputs[\"input_ids\"],\n        image_input=inputs[\"image_input\"],\n        image_mask=inputs[\"image_mask\"],\n        proprio=proprio_t,\n        domain_id=domain_t,\n        steps=denoise_steps,\n    )  # [1, 30, 20]\n\n    return actions.squeeze(0).float().cpu().numpy()  # [30, 20]\n\n\n# ---------------------------------------------------------------------------\n# Wilson CI\n# ---------------------------------------------------------------------------\n\ndef wilson_ci(successes, total, z=1.96):\n    if total == 0:\n        return 0.0, 0.0, 1.0\n    p = successes / total\n    denom = 1 + z ** 2 / total\n    center = (p + z ** 2 / (2 * total)) / denom\n    spread = z * np.sqrt((p * (1 - p) + z ** 2 / (4 * total)) / total) / denom\n    return center, max(0.0, center - spread), min(1.0, center + spread)\n\n\n# ---------------------------------------------------------------------------\n# Main evaluation\n# ---------------------------------------------------------------------------\n\ndef run_evaluation(args):\n    device = torch.device(f\"cuda:{args.gpu}\" if torch.cuda.is_available() else \"cpu\")\n    max_steps = args.max_steps or SUITE_MAX_STEPS.get(args.suite, 800)\n    output_path = Path(args.output or\n                       f\"eval_results/xvla_prune_k{args.keep_ratio}_{args.suite}.json\")\n\n    log.info(\"Suite: %s | Device: %s | keep_ratio=%.2f | Episodes/task: %d | Max steps: %d\",\n             args.suite, device, args.keep_ratio, args.num_episodes, max_steps)\n\n    np.random.seed(args.seed)\n    torch.manual_seed(args.seed)\n\n    t0 = time_mod.time()\n    model, processor = load_model(args.model_path, device)\n    log.info(\"Model loaded in %.1fs\", time_mod.time() - t0)\n\n    dummy_img = torch.randn(1, 3, 224, 224, device=device)\n    with torch.no_grad():\n        dummy_feats = model.vlm._encode_image(dummy_img)\n    n_vis_tokens = dummy_feats.shape[1]\n    k_tokens = max(1, int(args.keep_ratio * n_vis_tokens))\n    log.info(\"Vision tokens: %d total, keeping %d (%.0f%%)\",\n             n_vis_tokens, k_tokens, args.keep_ratio * 100)\n\n    install_vision_pruning(model, args.keep_ratio, args.mode)\n\n    num_actions_per_chunk = model.num_actions  # 30\n\n    # LIBERO setup — use OffScreenRenderEnv directly (matching official X-VLA eval)\n    from libero.libero import benchmark, get_libero_path\n    from libero.libero.envs import OffScreenRenderEnv\n\n    task_suite = benchmark.get_benchmark(args.suite)()\n    n_tasks = task_suite.n_tasks\n\n    if args.task_ids:\n        task_id_list = [int(x) for x in args.task_ids.split(\",\")]\n    else:\n        task_id_list = list(range(n_tasks))\n\n    eval_start = time_mod.time()\n    all_task_results = {}\n    total_successes = 0\n    total_episodes = 0\n\n    for task_id in task_id_list:\n        task = task_suite.get_task(task_id)\n        task_desc = task.language\n        task_bddl = os.path.join(\n            get_libero_path(\"bddl_files\"), task.problem_folder, task.bddl_file\n        )\n        log.info(\"--- Task %d: %s ---\", task_id, task_desc)\n\n        init_states = task_suite.get_task_init_states(task_id)\n\n        task_successes = []\n        task_lengths = []\n\n        for ep in range(args.num_episodes):\n            env = OffScreenRenderEnv(\n                bddl_file_name=task_bddl,\n                camera_heights=256,\n                camera_widths=256,\n            )\n            env.seed(args.seed + ep + 100)\n            obs = env.reset()\n\n            init_state_id = ep % init_states.shape[0]\n            obs = env.set_init_state(init_states[init_state_id])\n\n            # Settle the robot with neutral actions\n            for _ in range(10):\n                neutral = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0], dtype=np.float32)\n                obs, _, _, _ = env.step(neutral)\n\n            # Switch to absolute control\n            for robot in env.env.robots:\n                robot.controller.use_delta = False\n\n            action_queue = []\n            proprio_state = None\n            success = False\n\n            for step_idx in range(max_steps):\n                if not action_queue:\n                    # Extract proprio from env\n                    proprio_20d = extract_proprio_20d(env)\n                    if proprio_state is not None:\n                        proprio_20d[:9] = proprio_state[:9]\n\n                    images = get_images_from_obs(obs)\n                    if not images:\n                        raise ValueError(f\"No images found in obs keys: {list(obs.keys())}\")\n\n                    raw_actions = predict_actions(\n                        model, processor, images, task_desc, proprio_20d,\n                        args.domain_id, device, args.denoise_steps,\n                    )  # [30, 20]\n\n                    # Update closed-loop proprio with last predicted action\n                    proprio_state = proprio_20d.copy()\n                    proprio_state[:9] = raw_actions[-1, :9].copy()\n\n                    actions_7d = decode_action_20d_to_7d(raw_actions)  # [30, 7]\n                    action_queue = list(actions_7d)\n\n                action = action_queue.pop(0)\n                obs, reward, done, info = env.step(action)\n\n                if done or reward > 0.5:\n                    success = True\n                    break\n\n            ep_steps = step_idx + 1\n            task_successes.append(success)\n            task_lengths.append(ep_steps)\n            log.info(\"  Ep %d/%d | %s | steps=%d\",\n                     ep + 1, args.num_episodes,\n                     \"SUCCESS\" if success else \"FAIL\", ep_steps)\n\n            env.close()\n\n        n_succ = sum(task_successes)\n        n_total = len(task_successes)\n        sr = n_succ / n_total if n_total > 0 else 0.0\n\n        all_task_results[task_id] = {\n            \"task_id\": task_id,\n            \"task_description\": task_desc,\n            \"success_count\": n_succ,\n            \"total_episodes\": n_total,\n            \"success_rate\": round(sr, 4),\n            \"mean_steps\": round(float(np.mean(task_lengths)), 1),\n        }\n        total_successes += n_succ\n        total_episodes += n_total\n        log.info(\"  Task %d SR: %d/%d (%.1f%%)\", task_id, n_succ, n_total, sr * 100)\n\n    elapsed = time_mod.time() - eval_start\n    overall_sr = total_successes / total_episodes if total_episodes > 0 else 0.0\n    _, ci_lo, ci_hi = wilson_ci(total_successes, total_episodes)\n\n    log.info(\"=\" * 60)\n    log.info(\"SUITE: %s | MODEL: xvla | keep_ratio: %.2f\", args.suite, args.keep_ratio)\n    log.info(\"Overall SR: %d/%d (%.1f%%)\", total_successes, total_episodes, overall_sr * 100)\n    log.info(\"95%% Wilson CI: [%.1f%%, %.1f%%]\", ci_lo * 100, ci_hi * 100)\n    for tid, tr in sorted(all_task_results.items()):\n        log.info(\"  Task %d: %.0f%% (%d/%d) -- %s\",\n                 tid, tr[\"success_rate\"] * 100, tr[\"success_count\"],\n                 tr[\"total_episodes\"], tr[\"task_description\"])\n    log.info(\"Elapsed: %.1f min\", elapsed / 60)\n    log.info(\"=\" * 60)\n\n    summary = {\n        \"model\": \"xvla\",\n        \"model_path\": args.model_path,\n        \"mode\": args.mode,\n        \"suite\": args.suite,\n        \"keep_ratio\": args.keep_ratio,\n        \"n_vision_tokens_original\": n_vis_tokens,\n        \"n_vision_tokens_kept\": k_tokens,\n        \"total_episodes\": total_episodes,\n        \"total_successes\": total_successes,\n        \"overall_success_rate\": round(overall_sr, 4),\n        \"wilson_ci_95\": [round(ci_lo, 4), round(ci_hi, 4)],\n        \"num_episodes_per_task\": args.num_episodes,\n        \"max_steps\": max_steps,\n        \"num_actions_per_chunk\": num_actions_per_chunk,\n        \"domain_id\": args.domain_id,\n        \"denoise_steps\": args.denoise_steps,\n        \"seed\": args.seed,\n        \"elapsed_seconds\": round(elapsed, 1),\n        \"per_task\": all_task_results,\n    }\n\n    output_path.parent.mkdir(parents=True, exist_ok=True)\n    with open(output_path, \"w\") as f:\n        json.dump(summary, f, indent=2)\n    log.info(\"Results saved to %s\", output_path)\n\n    return summary\n\n\nif __name__ == \"__main__\":\n    args = parse_args()\n    run_evaluation(args)\nPYEOF\necho \"DEPLOY_OK\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a",
  "uuid": "2d4e2ded-3555-463c-96e2-660ec7a20d8e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T3fbFXHpmCJPQ6RGmcBui6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19339,
      "cache_read_input_tokens": 41099,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19339
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-21T02:23:51.602Z_

<details><summary>↩ Tool result · `toolu_01AsEF4BgjkVZhDNkR5GKMkJ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"DEPLOY_OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a",
  "uuid": "627daf90-6250-46d8-9bf2-ffaae29fe23c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"DEPLOY_OK\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"DEPLOY_OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 44_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01JwmuCS8ZVU5cLxofrjv9w7`</summary>

```json
{
  "server": "westd-38929",
  "command": "cat > /root/autodl-tmp/importance_margin_vla_compress/eval_xvla_pruning_libero.py << 'PYEOF'\n\"\"\"X-VLA Vision Token Pruning Evaluation on LIBERO.\n\nPrunes vision tokens by L2 norm after Florence2's image encoder + linear projection,\nbefore they enter the Florence2 language encoder. Evaluates on LIBERO suites.\n\nFollows official X-VLA evaluation protocol:\n  - Absolute EEF control (use_delta=False)\n  - 20D action space: [arm1: pos(3)+rot6d(6)+grip(1)] + [arm2: zeros(10)]\n  - 20D proprio: [pos(3)+rot6d(6)+0.0] + zeros(10)\n  - domain_id=3 for LIBERO\n  - Closed-loop proprio update from last predicted action\n\nUsage:\n    CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl python eval_xvla_pruning_libero.py \\\n        --model_path /path/to/X-VLA-Libero \\\n        --suite libero_object \\\n        --keep_ratio 0.5 \\\n        --num_episodes 50 \\\n        --gpu 0\n\"\"\"\n\nfrom __future__ import annotations\n\nimport argparse\nimport json\nimport logging\nimport os\nimport sys\nimport time as time_mod\nfrom pathlib import Path\nfrom functools import wraps\n\nos.environ.setdefault(\"MUJOCO_GL\", \"egl\")\n\nimport numpy as np\nimport torch\nfrom PIL import Image\n\nsys.path.insert(0, str(Path(__file__).resolve().parent))\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    datefmt=\"%Y-%m-%d %H:%M:%S\",\n)\nlog = logging.getLogger(__name__)\n\nSUITE_MAX_STEPS = {\n    \"libero_spatial\": 800,\n    \"libero_object\": 800,\n    \"libero_goal\": 800,\n    \"libero_10\": 900,\n    \"libero_90\": 800,\n}\n\nEPS = 1e-6\n\n\ndef parse_args():\n    p = argparse.ArgumentParser(description=\"X-VLA pruning eval on LIBERO\")\n    p.add_argument(\"--model_path\", type=str, default=\"2toINF/X-VLA-Libero\",\n                   help=\"HuggingFace model path or local dir\")\n    p.add_argument(\"--suite\", type=str, default=\"libero_object\",\n                   choices=list(SUITE_MAX_STEPS.keys()))\n    p.add_argument(\"--keep_ratio\", type=float, default=1.0,\n                   help=\"Fraction of vision tokens to keep (1.0 = no pruning)\")\n    p.add_argument(\"--num_episodes\", type=int, default=50)\n    p.add_argument(\"--gpu\", type=int, default=0)\n    p.add_argument(\"--seed\", type=int, default=42)\n    p.add_argument(\"--max_steps\", type=int, default=None)\n    p.add_argument(\"--output\", type=str, default=None)\n    p.add_argument(\"--task_ids\", type=str, default=None)\n    p.add_argument(\"--domain_id\", type=int, default=3)\n    p.add_argument(\"--denoise_steps\", type=int, default=10,\n                   help=\"Flow matching denoising steps\")\n    p.add_argument(\"--mode\", type=str, default=\"l2_norm\",\n                   choices=[\"l2_norm\", \"random\"],\n                   help=\"Pruning method: l2_norm (keep highest L2 norm tokens) or random (random selection)\")\n    return p.parse_args()\n\n\n# ---------------------------------------------------------------------------\n# Pruning hook\n# ---------------------------------------------------------------------------\n\ndef install_vision_pruning(model, keep_ratio: float, mode: str = \"l2_norm\"):\n    if keep_ratio >= 1.0:\n        log.info(\"keep_ratio=%.2f, no pruning applied\", keep_ratio)\n        return\n\n    original_encode = model.vlm._encode_image\n\n    @wraps(original_encode)\n    def pruned_encode(pixel_values):\n        features = original_encode(pixel_values)\n        N = features.shape[1]\n        k = max(1, int(keep_ratio * N))\n        if k >= N:\n            return features\n        if mode == \"l2_norm\":\n            norms = features.norm(dim=-1)\n            _, indices = norms.topk(k, dim=-1)\n        elif mode == \"random\":\n            indices = torch.stack([\n                torch.randperm(N, device=features.device)[:k]\n                for _ in range(features.shape[0])\n            ], dim=0)\n        indices_sorted = indices.sort(dim=-1).values\n        pruned = features.gather(\n            1, indices_sorted.unsqueeze(-1).expand(-1, -1, features.shape[-1])\n        )\n        return pruned\n\n    model.vlm._encode_image = pruned_encode\n    log.info(\"Vision pruning installed: keep_ratio=%.2f, mode=%s\", keep_ratio, mode)\n\n\n# ---------------------------------------------------------------------------\n# Model loading\n# ---------------------------------------------------------------------------\n\ndef load_model(model_path: str, device: torch.device):\n    model_dir = str(Path(model_path).resolve())\n    sys.path.insert(0, model_dir)\n\n    from configuration_xvla import XVLAConfig\n    from modeling_xvla import XVLA\n    from processing_xvla import XVLAProcessor\n    from safetensors.torch import load_file\n\n    log.info(\"Loading X-VLA from %s\", model_dir)\n    config = XVLAConfig.from_pretrained(model_dir)\n    model = XVLA(config)\n\n    safetensors_path = Path(model_dir) / \"model.safetensors\"\n    if safetensors_path.exists():\n        state_dict = load_file(str(safetensors_path))\n    else:\n        import torch as _torch\n        state_dict = _torch.load(Path(model_dir) / \"pytorch_model.bin\", map_location=\"cpu\")\n    model.load_state_dict(state_dict, strict=False)\n    model = model.to(device).eval()\n\n    processor = XVLAProcessor.from_pretrained(model_dir, trust_remote_code=True)\n    if processor.tokenizer.pad_token is None:\n        processor.tokenizer.pad_token = \"&lt;pad>\"\n        processor.tokenizer.pad_token_id = 1\n\n    n_params = sum(p.numel() for p in model.parameters())\n    log.info(\"Model loaded: %.1fM params, dtype=%s\", n_params / 1e6, model.dtype)\n    return model, processor\n\n\n# ---------------------------------------------------------------------------\n# 6D rotation utilities (following X-VLA's convention)\n# ---------------------------------------------------------------------------\n\ndef mat_to_rot6d(R: np.ndarray) -> np.ndarray:\n    \"\"\"Extract 6D rotation from 3x3 rotation matrix: first two columns.\"\"\"\n    return np.concatenate([R[:3, 0], R[:3, 1]], axis=-1).astype(np.float32)\n\n\ndef rot6d_to_axis_angle(r6d: np.ndarray) -> np.ndarray:\n    \"\"\"Convert 6D rotation representation to axis-angle via Gram-Schmidt.\"\"\"\n    import robosuite.utils.transform_utils as T\n\n    single = r6d.ndim == 1\n    if single:\n        r6d = r6d[None, :]\n\n    a1 = r6d[:, 0:3]\n    a2 = r6d[:, 3:6]\n\n    b1 = a1 / (np.linalg.norm(a1, axis=-1, keepdims=True) + EPS)\n    dot_prod = np.sum(b1 * a2, axis=-1, keepdims=True)\n    b2_orth = a2 - dot_prod * b1\n    b2 = b2_orth / (np.linalg.norm(b2_orth, axis=-1, keepdims=True) + EPS)\n    b3 = np.cross(b1, b2, axis=-1)\n\n    R = np.stack([b1, b2, b3], axis=-1)  # (N, 3, 3)\n\n    results = []\n    for i in range(R.shape[0]):\n        quat = T.mat2quat(R[i])\n        aa = T.quat2axisangle(quat)\n        results.append(aa)\n\n    result = np.stack(results, axis=0)\n    return result[0] if single else result\n\n\n# ---------------------------------------------------------------------------\n# Observation processing\n# ---------------------------------------------------------------------------\n\ndef extract_proprio_20d(env) -> np.ndarray:\n    \"\"\"Extract 20D proprio: [pos(3)+rot6d(6)+0.0] + zeros(10) from env robot state.\"\"\"\n    robot = env.env.robots[0]\n    ee_pos = robot.controller.ee_pos.copy()         # (3,)\n    ee_ori_mat = robot.controller.ee_ori_mat.copy()  # (3, 3)\n    ee_rot6d = mat_to_rot6d(ee_ori_mat)              # (6,)\n\n    arm1 = np.concatenate([ee_pos, ee_rot6d, np.array([0.0], dtype=np.float32)])  # (10,)\n    arm2 = np.zeros(10, dtype=np.float32)\n    return np.concatenate([arm1, arm2])  # (20,)\n\n\ndef decode_action_20d_to_7d(action_20d: np.ndarray) -> np.ndarray:\n    \"\"\"Convert 20D X-VLA action to 7D LIBERO action.\n\n    Input:  [pos(3), rot6d(6), grip(1), arm2(10)]  — only arm1 used\n    Output: [pos(3), axis_angle(3), grip(1)]\n    \"\"\"\n    single = action_20d.ndim == 1\n    if single:\n        action_20d = action_20d[None, :]\n\n    pos = action_20d[:, :3]\n    rot6d = action_20d[:, 3:9]\n    grip = action_20d[:, 9:10]\n\n    axis_angle = rot6d_to_axis_angle(rot6d)\n\n    # Discretize gripper: >0.5 → 1.0 (open), else -1.0 (close)\n    grip_disc = np.where(grip > 0.5, 1.0, -1.0)\n\n    result = np.concatenate([pos, axis_angle, grip_disc], axis=-1).astype(np.float32)\n    return result[0] if single else result\n\n\ndef get_images_from_obs(obs) -> list:\n    \"\"\"Extract camera images from LIBERO observation, apply agentview flip.\"\"\"\n    images = []\n    for cam_name in [\"agentview_image\", \"robot0_eye_in_hand_image\"]:\n        img = obs.get(cam_name, None)\n        if img is None:\n            for k, v in obs.items():\n                if cam_name in k and isinstance(v, np.ndarray):\n                    img = v\n                    break\n        if img is not None:\n            if img.dtype in (np.float32, np.float64):\n                img = (np.clip(img, 0, 1) * 255).astype(np.uint8)\n            if cam_name == \"agentview_image\":\n                img = np.flip(np.flip(img, 0), 1).copy()\n            images.append(Image.fromarray(img))\n    return images\n\n\n# ---------------------------------------------------------------------------\n# Action prediction\n# ---------------------------------------------------------------------------\n\n@torch.no_grad()\ndef predict_actions(model, processor, images, task_desc, proprio_20d, domain_id,\n                    device, denoise_steps=10):\n    inputs = processor(images=images, language_instruction=task_desc)\n\n    proprio_t = torch.tensor(proprio_20d, dtype=torch.float32).unsqueeze(0).to(device)\n    domain_t = torch.tensor([domain_id], dtype=torch.long).to(device)\n\n    for k, v in inputs.items():\n        if isinstance(v, torch.Tensor):\n            if v.is_floating_point():\n                inputs[k] = v.to(device=device, dtype=torch.float32)\n            else:\n                inputs[k] = v.to(device=device)\n\n    actions = model.generate_actions(\n        input_ids=inputs[\"input_ids\"],\n        image_input=inputs[\"image_input\"],\n        image_mask=inputs[\"image_mask\"],\n        proprio=proprio_t,\n        domain_id=domain_t,\n        steps=denoise_steps,\n    )  # [1, 30, 20]\n\n    return actions.squeeze(0).float().cpu().numpy()  # [30, 20]\n\n\n# ---------------------------------------------------------------------------\n# Wilson CI\n# ---------------------------------------------------------------------------\n\ndef wilson_ci(successes, total, z=1.96):\n    if total == 0:\n        return 0.0, 0.0, 1.0\n    p = successes / total\n    denom = 1 + z ** 2 / total\n    center = (p + z ** 2 / (2 * total)) / denom\n    spread = z * np.sqrt((p * (1 - p) + z ** 2 / (4 * total)) / total) / denom\n    return center, max(0.0, center - spread), min(1.0, center + spread)\n\n\n# ---------------------------------------------------------------------------\n# Main evaluation\n# ---------------------------------------------------------------------------\n\ndef run_evaluation(args):\n    device = torch.device(f\"cuda:{args.gpu}\" if torch.cuda.is_available() else \"cpu\")\n    max_steps = args.max_steps or SUITE_MAX_STEPS.get(args.suite, 800)\n    output_path = Path(args.output or\n                       f\"eval_results/xvla_prune_k{args.keep_ratio}_{args.suite}.json\")\n\n    log.info(\"Suite: %s | Device: %s | keep_ratio=%.2f | Episodes/task: %d | Max steps: %d\",\n             args.suite, device, args.keep_ratio, args.num_episodes, max_steps)\n\n    np.random.seed(args.seed)\n    torch.manual_seed(args.seed)\n\n    t0 = time_mod.time()\n    model, processor = load_model(args.model_path, device)\n    log.info(\"Model loaded in %.1fs\", time_mod.time() - t0)\n\n    dummy_img = torch.randn(1, 3, 224, 224, device=device)\n    with torch.no_grad():\n        dummy_feats = model.vlm._encode_image(dummy_img)\n    n_vis_tokens = dummy_feats.shape[1]\n    k_tokens = max(1, int(args.keep_ratio * n_vis_tokens))\n    log.info(\"Vision tokens: %d total, keeping %d (%.0f%%)\",\n             n_vis_tokens, k_tokens, args.keep_ratio * 100)\n\n    install_vision_pruning(model, args.keep_ratio, args.mode)\n\n    num_actions_per_chunk = model.num_actions  # 30\n\n    # LIBERO setup — use OffScreenRenderEnv directly (matching official X-VLA eval)\n    from libero.libero import benchmark, get_libero_path\n    from libero.libero.envs import OffScreenRenderEnv\n\n    task_suite = benchmark.get_benchmark(args.suite)()\n    n_tasks = task_suite.n_tasks\n\n    if args.task_ids:\n        task_id_list = [int(x) for x in args.task_ids.split(\",\")]\n    else:\n        task_id_list = list(range(n_tasks))\n\n    eval_start = time_mod.time()\n    all_task_results = {}\n    total_successes = 0\n    total_episodes = 0\n\n    for task_id in task_id_list:\n        task = task_suite.get_task(task_id)\n        task_desc = task.language\n        task_bddl = os.path.join(\n            get_libero_path(\"bddl_files\"), task.problem_folder, task.bddl_file\n        )\n        log.info(\"--- Task %d: %s ---\", task_id, task_desc)\n\n        init_states = task_suite.get_task_init_states(task_id)\n\n        task_successes = []\n        task_lengths = []\n\n        for ep in range(args.num_episodes):\n            env = OffScreenRenderEnv(\n                bddl_file_name=task_bddl,\n                camera_heights=256,\n                camera_widths=256,\n            )\n            env.seed(args.seed + ep + 100)\n            obs = env.reset()\n\n            init_state_id = ep % init_states.shape[0]\n            obs = env.set_init_state(init_states[init_state_id])\n\n            # Settle the robot with neutral actions\n            for _ in range(10):\n                neutral = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0], dtype=np.float32)\n                obs, _, _, _ = env.step(neutral)\n\n            # Switch to absolute control\n            for robot in env.env.robots:\n                robot.controller.use_delta = False\n\n            action_queue = []\n            proprio_state = None\n            success = False\n\n            for step_idx in range(max_steps):\n                if not action_queue:\n                    # Extract proprio from env\n                    proprio_20d = extract_proprio_20d(env)\n                    if proprio_state is not None:\n                        proprio_20d[:9] = proprio_state[:9]\n\n                    images = get_images_from_obs(obs)\n                    if not images:\n                        raise ValueError(f\"No images found in obs keys: {list(obs.keys())}\")\n\n                    raw_actions = predict_actions(\n                        model, processor, images, task_desc, proprio_20d,\n                        args.domain_id, device, args.denoise_steps,\n                    )  # [30, 20]\n\n                    # Update closed-loop proprio with last predicted action\n                    proprio_state = proprio_20d.copy()\n                    proprio_state[:9] = raw_actions[-1, :9].copy()\n\n                    actions_7d = decode_action_20d_to_7d(raw_actions)  # [30, 7]\n                    action_queue = list(actions_7d)\n\n                action = action_queue.pop(0)\n                obs, reward, done, info = env.step(action)\n\n                if done or reward > 0.5:\n                    success = True\n                    break\n\n            ep_steps = step_idx + 1\n            task_successes.append(success)\n            task_lengths.append(ep_steps)\n            log.info(\"  Ep %d/%d | %s | steps=%d\",\n                     ep + 1, args.num_episodes,\n                     \"SUCCESS\" if success else \"FAIL\", ep_steps)\n\n            env.close()\n\n        n_succ = sum(task_successes)\n        n_total = len(task_successes)\n        sr = n_succ / n_total if n_total > 0 else 0.0\n\n        all_task_results[task_id] = {\n            \"task_id\": task_id,\n            \"task_description\": task_desc,\n            \"success_count\": n_succ,\n            \"total_episodes\": n_total,\n            \"success_rate\": round(sr, 4),\n            \"mean_steps\": round(float(np.mean(task_lengths)), 1),\n        }\n        total_successes += n_succ\n        total_episodes += n_total\n        log.info(\"  Task %d SR: %d/%d (%.1f%%)\", task_id, n_succ, n_total, sr * 100)\n\n    elapsed = time_mod.time() - eval_start\n    overall_sr = total_successes / total_episodes if total_episodes > 0 else 0.0\n    _, ci_lo, ci_hi = wilson_ci(total_successes, total_episodes)\n\n    log.info(\"=\" * 60)\n    log.info(\"SUITE: %s | MODEL: xvla | keep_ratio: %.2f\", args.suite, args.keep_ratio)\n    log.info(\"Overall SR: %d/%d (%.1f%%)\", total_successes, total_episodes, overall_sr * 100)\n    log.info(\"95%% Wilson CI: [%.1f%%, %.1f%%]\", ci_lo * 100, ci_hi * 100)\n    for tid, tr in sorted(all_task_results.items()):\n        log.info(\"  Task %d: %.0f%% (%d/%d) -- %s\",\n                 tid, tr[\"success_rate\"] * 100, tr[\"success_count\"],\n                 tr[\"total_episodes\"], tr[\"task_description\"])\n    log.info(\"Elapsed: %.1f min\", elapsed / 60)\n    log.info(\"=\" * 60)\n\n    summary = {\n        \"model\": \"xvla\",\n        \"model_path\": args.model_path,\n        \"mode\": args.mode,\n        \"suite\": args.suite,\n        \"keep_ratio\": args.keep_ratio,\n        \"n_vision_tokens_original\": n_vis_tokens,\n        \"n_vision_tokens_kept\": k_tokens,\n        \"total_episodes\": total_episodes,\n        \"total_successes\": total_successes,\n        \"overall_success_rate\": round(overall_sr, 4),\n        \"wilson_ci_95\": [round(ci_lo, 4), round(ci_hi, 4)],\n        \"num_episodes_per_task\": args.num_episodes,\n        \"max_steps\": max_steps,\n        \"num_actions_per_chunk\": num_actions_per_chunk,\n        \"domain_id\": args.domain_id,\n        \"denoise_steps\": args.denoise_steps,\n        \"seed\": args.seed,\n        \"elapsed_seconds\": round(elapsed, 1),\n        \"per_task\": all_task_results,\n    }\n\n    output_path.parent.mkdir(parents=True, exist_ok=True)\n    with open(output_path, \"w\") as f:\n        json.dump(summary, f, indent=2)\n    log.info(\"Results saved to %s\", output_path)\n\n    return summary\n\n\nif __name__ == \"__main__\":\n    args = parse_args()\n    run_evaluation(args)\nPYEOF\necho \"DEPLOY_OK\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a",
  "uuid": "20748470-c59a-4a8c-b139-507dea69350b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T3fbFXHpmCJPQ6RGmcBui6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19339,
      "cache_read_input_tokens": 41099,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19339
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-21T02:24:50.098Z_

<details><summary>↩ Tool result · `toolu_01JwmuCS8ZVU5cLxofrjv9w7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"DEPLOY_OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a",
  "uuid": "a9ae101f-131e-459f-888d-6af91b8089e5",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"DEPLOY_OK\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.52}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"DEPLOY_OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 46_

两台都部署成功。验证 `--help` 输出。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a",
  "uuid": "27be09e2-66b5-44e6-9780-3d4689566a61",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Rvgnnr9smVfgrTAXcaxq8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12167,
      "cache_read_input_tokens": 60438,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12167
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 47_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01VgNP3YSC9wL4rr19eXpfRD`</summary>

```json
{
  "server": "cqa1-33015",
  "command": "head -80 /root/autodl-tmp/importance_margin_vla_compress/eval_xvla_pruning_libero.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a",
  "uuid": "7c34da5a-3a9f-4eb3-98ea-ab89e78a9b24",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Rvgnnr9smVfgrTAXcaxq8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12167,
      "cache_read_input_tokens": 60438,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12167
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-21T02:24:57.753Z_

<details><summary>↩ Tool result · `toolu_01VgNP3YSC9wL4rr19eXpfRD`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"X-VLA Vision Token Pruning Evaluation on LIBERO.\\n\\nPrunes vision tokens by L2 norm after Florence2's image encoder + linear projection,\\nbefore they enter the Florence2 language encoder. Evaluates on LIBERO suites.\\n\\nFollows official X-VLA evaluation protocol:\\n  - Absolute EEF control (use_delta=False)\\n  - 20D action space: [arm1: pos(3)+rot6d(6)+grip(1)] + [arm2: zeros(10)]\\n  - 20D proprio: [pos(3)+rot6d(6)+0.0] + zeros(10)\\n  - domain_id=3 for LIBERO\\n  - Closed-loop proprio update from last predicted action\\n\\nUsage:\\n    CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl python eval_xvla_pruning_libero.py \\\\\\n        --model_path /path/to/X-VLA-Libero \\\\\\n        --suite libero_object \\\\\\n        --keep_ratio 0.5 \\\\\\n        --num_episodes 50 \\\\\\n        --gpu 0\\n\\\"\\\"\\\"\\n\\nfrom __future__ import annotations\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport sys\\nimport time as time_mod\\nfrom pathlib import Path\\nfrom functools import wraps\\n\\nos.environ.setdefault(\\\"MUJOCO_GL\\\", \\\"egl\\\")\\n\\nimport numpy as np\\nimport torch\\nfrom PIL import Image\\n\\nsys.path.insert(0, str(Path(__file__).resolve().parent))\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n    datefmt=\\\"%Y-%m-%d %H:%M:%S\\\",\\n)\\nlog = logging.getLogger(__name__)\\n\\nSUITE_MAX_STEPS = {\\n    \\\"libero_spatial\\\": 800,\\n    \\\"libero_object\\\": 800,\\n    \\\"libero_goal\\\": 800,\\n    \\\"libero_10\\\": 900,\\n    \\\"libero_90\\\": 800,\\n}\\n\\nEPS = 1e-6\\n\\n\\ndef parse_args():\\n    p = argparse.ArgumentParser(description=\\\"X-VLA pruning eval on LIBERO\\\")\\n    p.add_argument(\\\"--model_path\\\", type=str, default=\\\"2toINF/X-VLA-Libero\\\",\\n                   help=\\\"HuggingFace model path or local dir\\\")\\n    p.add_argument(\\\"--suite\\\", type=str, default=\\\"libero_object\\\",\\n                   choices=list(SUITE_MAX_STEPS.keys()))\\n    p.add_argument(\\\"--keep_ratio\\\", type=float, default=1.0,\\n                   help=\\\"Fraction of vision tokens to keep (1.0 = no pruning)\\\")\\n    p.add_argument(\\\"--num_episodes\\\", type=int, default=50)\\n    p.add_argument(\\\"--gpu\\\", type=int, default=0)\\n    p.add_argument(\\\"--seed\\\", type=int, default=42)\\n    p.add_argument(\\\"--max_steps\\\", type=int, default=None)\\n    p.add_argument(\\\"--output\\\", type=str, default=None)\\n    p.add_argument(\\\"--task_ids\\\", type=str, default=None)\\n    p.add_argument(\\\"--domain_id\\\", type=int, default=3)\\n    p.add_argument(\\\"--denoise_steps\\\", type=int, default=10,\\n                   help=\\\"Flow matching denoising steps\\\")\\n    p.add_argument(\\\"--mode\\\", type=str, default=\\\"l2_norm\\\",\\n                   choices=[\\\"l2_norm\\\", \\\"random\\\"],\\n                   help=\\\"Pruning method: l2_norm (keep highest L2 norm tokens) or random (random selection)\\\")\\n    return p.parse_args()\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a",
  "uuid": "60a42a1f-19b4-4969-83f9-6bcc33b4c0f6",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\"\\\\\\\"\\\\\\\"X-VLA Vision Token Pruning Evaluation on LIBERO.\\\\n\\\\nPrunes vision tokens by L2 norm after Florence2's image encoder + linear projection,\\\\nbefore they enter the Florence2 language encoder. Evaluates on LIBERO suites.\\\\n\\\\nFollows official X-VLA evaluation protocol:\\\\n  - Absolute EEF control (use_delta=False)\\\\n  - 20D action space: [arm1: pos(3)+rot6d(6)+grip(1)] + [arm2: zeros(10)]\\\\n  - 20D proprio: [pos(3)+rot6d(6)+0.0] + zeros(10)\\\\n  - domain_id=3 for LIBERO\\\\n  - Closed-loop proprio update from last predicted action\\\\n\\\\nUsage:\\\\n    CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl python eval_xvla_pruning_libero.py \\\\\\\\\\\\n        --model_path /path/to/X-VLA-Libero \\\\\\\\\\\\n        --suite libero_object \\\\\\\\\\\\n        --keep_ratio 0.5 \\\\\\\\\\\\n        --num_episodes 50 \\\\\\\\\\\\n        --gpu 0\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nfrom __future__ import annotations\\\\n\\\\nimport argparse\\\\nimport json\\\\nimport logging\\\\nimport os\\\\nimport sys\\\\nimport time as time_mod\\\\nfrom pathlib import Path\\\\nfrom functools import wraps\\\\n\\\\nos.environ.setdefault(\\\\\\\"MUJOCO_GL\\\\\\\", \\\\\\\"egl\\\\\\\")\\\\n\\\\nimport numpy as np\\\\nimport torch\\\\nfrom PIL import Image\\\\n\\\\nsys.path.insert(0, str(Path(__file__).resolve().parent))\\\\n\\\\nlogging.basicConfig(\\\\n    level=logging.INFO,\\\\n    format=\\\\\\\"%(asctime)s [%(levelname)s] %(message)s\\\\\\\",\\\\n    datefmt=\\\\\\\"%Y-%m-%d %H:%M:%S\\\\\\\",\\\\n)\\\\nlog = logging.getLogger(__name__)\\\\n\\\\nSUITE_MAX_STEPS = {\\\\n    \\\\\\\"libero_spatial\\\\\\\": 800,\\\\n    \\\\\\\"libero_object\\\\\\\": 800,\\\\n    \\\\\\\"libero_goal\\\\\\\": 800,\\\\n    \\\\\\\"libero_10\\\\\\\": 900,\\\\n    \\\\\\\"libero_90\\\\\\\": 800,\\\\n}\\\\n\\\\nEPS = 1e-6\\\\n\\\\n\\\\ndef parse_args():\\\\n    p = argparse.ArgumentParser(description=\\\\\\\"X-VLA pruning eval on LIBERO\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--model_path\\\\\\\", type=str, default=\\\\\\\"2toINF/X-VLA-Libero\\\\\\\",\\\\n                   help=\\\\\\\"HuggingFace model path or local dir\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--suite\\\\\\\", type=str, default=\\\\\\\"libero_object\\\\\\\",\\\\n                   choices=list(SUITE_MAX_STEPS.keys()))\\\\n    p.add_argument(\\\\\\\"--keep_ratio\\\\\\\", type=float, default=1.0,\\\\n                   help=\\\\\\\"Fraction of vision tokens to keep (1.0 = no pruning)\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--num_episodes\\\\\\\", type=int, default=50)\\\\n    p.add_argument(\\\\\\\"--gpu\\\\\\\", type=int, default=0)\\\\n    p.add_argument(\\\\\\\"--seed\\\\\\\", type=int, default=42)\\\\n    p.add_argument(\\\\\\\"--max_steps\\\\\\\", type=int, default=None)\\\\n    p.add_argument(\\\\\\\"--output\\\\\\\", type=str, default=None)\\\\n    p.add_argument(\\\\\\\"--task_ids\\\\\\\", type=str, default=None)\\\\n    p.add_argument(\\\\\\\"--domain_id\\\\\\\", type=int, default=3)\\\\n    p.add_argument(\\\\\\\"--denoise_steps\\\\\\\", type=int, default=10,\\\\n                   help=\\\\\\\"Flow matching denoising steps\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--mode\\\\\\\", type=str, default=\\\\\\\"l2_norm\\\\\\\",\\\\n                   choices=[\\\\\\\"l2_norm\\\\\\\", \\\\\\\"random\\\\\\\"],\\\\n                   help=\\\\\\\"Pruning method: l2_norm (keep highest L2 norm tokens) or random (random selection)\\\\\\\")\\\\n    return p.parse_args()\\\\n\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"X-VLA Vision Token Pruning Evaluation on LIBERO.\\n\\nPrunes vision tokens by L2 norm after Florence2's image encoder + linear projection,\\nbefore they enter the Florence2 language encoder. Evaluates on LIBERO suites.\\n\\nFollows official X-VLA evaluation protocol:\\n  - Absolute EEF control (use_delta=False)\\n  - 20D action space: [arm1: pos(3)+rot6d(6)+grip(1)] + [arm2: zeros(10)]\\n  - 20D proprio: [pos(3)+rot6d(6)+0.0] + zeros(10)\\n  - domain_id=3 for LIBERO\\n  - Closed-loop proprio update from last predicted action\\n\\nUsage:\\n    CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl python eval_xvla_pruning_libero.py \\\\\\n        --model_path /path/to/X-VLA-Libero \\\\\\n        --suite libero_object \\\\\\n        --keep_ratio 0.5 \\\\\\n        --num_episodes 50 \\\\\\n        --gpu 0\\n\\\"\\\"\\\"\\n\\nfrom __future__ import annotations\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport sys\\nimport time as time_mod\\nfrom pathlib import Path\\nfrom functools import wraps\\n\\nos.environ.setdefault(\\\"MUJOCO_GL\\\", \\\"egl\\\")\\n\\nimport numpy as np\\nimport torch\\nfrom PIL import Image\\n\\nsys.path.insert(0, str(Path(__file__).resolve().parent))\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n    datefmt=\\\"%Y-%m-%d %H:%M:%S\\\",\\n)\\nlog = logging.getLogger(__name__)\\n\\nSUITE_MAX_STEPS = {\\n    \\\"libero_spatial\\\": 800,\\n    \\\"libero_object\\\": 800,\\n    \\\"libero_goal\\\": 800,\\n    \\\"libero_10\\\": 900,\\n    \\\"libero_90\\\": 800,\\n}\\n\\nEPS = 1e-6\\n\\n\\ndef parse_args():\\n    p = argparse.ArgumentParser(description=\\\"X-VLA pruning eval on LIBERO\\\")\\n    p.add_argument(\\\"--model_path\\\", type=str, default=\\\"2toINF/X-VLA-Libero\\\",\\n                   help=\\\"HuggingFace model path or local dir\\\")\\n    p.add_argument(\\\"--suite\\\", type=str, default=\\\"libero_object\\\",\\n                   choices=list(SUITE_MAX_STEPS.keys()))\\n    p.add_argument(\\\"--keep_ratio\\\", type=float, default=1.0,\\n                   help=\\\"Fraction of vision tokens to keep (1.0 = no pruning)\\\")\\n    p.add_argument(\\\"--num_episodes\\\", type=int, default=50)\\n    p.add_argument(\\\"--gpu\\\", type=int, default=0)\\n    p.add_argument(\\\"--seed\\\", type=int, default=42)\\n    p.add_argument(\\\"--max_steps\\\", type=int, default=None)\\n    p.add_argument(\\\"--output\\\", type=str, default=None)\\n    p.add_argument(\\\"--task_ids\\\", type=str, default=None)\\n    p.add_argument(\\\"--domain_id\\\", type=int, default=3)\\n    p.add_argument(\\\"--denoise_steps\\\", type=int, default=10,\\n                   help=\\\"Flow matching denoising steps\\\")\\n    p.add_argument(\\\"--mode\\\", type=str, default=\\\"l2_norm\\\",\\n                   choices=[\\\"l2_norm\\\", \\\"random\\\"],\\n                   help=\\\"Pruning method: l2_norm (keep highest L2 norm tokens) or random (random selection)\\\")\\n    return p.parse_args()\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 49_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01F8vBLb4riihHn3ci47sgus`</summary>

```json
{
  "server": "westd-38929",
  "command": "head -80 /root/autodl-tmp/importance_margin_vla_compress/eval_xvla_pruning_libero.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a",
  "uuid": "35db7f89-ae80-4068-a07b-699687e15e63",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Rvgnnr9smVfgrTAXcaxq8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12167,
      "cache_read_input_tokens": 60438,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12167
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-21T02:24:58.528Z_

<details><summary>↩ Tool result · `toolu_01F8vBLb4riihHn3ci47sgus`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"X-VLA Vision Token Pruning Evaluation on LIBERO.\\n\\nPrunes vision tokens by L2 norm after Florence2's image encoder + linear projection,\\nbefore they enter the Florence2 language encoder. Evaluates on LIBERO suites.\\n\\nFollows official X-VLA evaluation protocol:\\n  - Absolute EEF control (use_delta=False)\\n  - 20D action space: [arm1: pos(3)+rot6d(6)+grip(1)] + [arm2: zeros(10)]\\n  - 20D proprio: [pos(3)+rot6d(6)+0.0] + zeros(10)\\n  - domain_id=3 for LIBERO\\n  - Closed-loop proprio update from last predicted action\\n\\nUsage:\\n    CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl python eval_xvla_pruning_libero.py \\\\\\n        --model_path /path/to/X-VLA-Libero \\\\\\n        --suite libero_object \\\\\\n        --keep_ratio 0.5 \\\\\\n        --num_episodes 50 \\\\\\n        --gpu 0\\n\\\"\\\"\\\"\\n\\nfrom __future__ import annotations\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport sys\\nimport time as time_mod\\nfrom pathlib import Path\\nfrom functools import wraps\\n\\nos.environ.setdefault(\\\"MUJOCO_GL\\\", \\\"egl\\\")\\n\\nimport numpy as np\\nimport torch\\nfrom PIL import Image\\n\\nsys.path.insert(0, str(Path(__file__).resolve().parent))\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n    datefmt=\\\"%Y-%m-%d %H:%M:%S\\\",\\n)\\nlog = logging.getLogger(__name__)\\n\\nSUITE_MAX_STEPS = {\\n    \\\"libero_spatial\\\": 800,\\n    \\\"libero_object\\\": 800,\\n    \\\"libero_goal\\\": 800,\\n    \\\"libero_10\\\": 900,\\n    \\\"libero_90\\\": 800,\\n}\\n\\nEPS = 1e-6\\n\\n\\ndef parse_args():\\n    p = argparse.ArgumentParser(description=\\\"X-VLA pruning eval on LIBERO\\\")\\n    p.add_argument(\\\"--model_path\\\", type=str, default=\\\"2toINF/X-VLA-Libero\\\",\\n                   help=\\\"HuggingFace model path or local dir\\\")\\n    p.add_argument(\\\"--suite\\\", type=str, default=\\\"libero_object\\\",\\n                   choices=list(SUITE_MAX_STEPS.keys()))\\n    p.add_argument(\\\"--keep_ratio\\\", type=float, default=1.0,\\n                   help=\\\"Fraction of vision tokens to keep (1.0 = no pruning)\\\")\\n    p.add_argument(\\\"--num_episodes\\\", type=int, default=50)\\n    p.add_argument(\\\"--gpu\\\", type=int, default=0)\\n    p.add_argument(\\\"--seed\\\", type=int, default=42)\\n    p.add_argument(\\\"--max_steps\\\", type=int, default=None)\\n    p.add_argument(\\\"--output\\\", type=str, default=None)\\n    p.add_argument(\\\"--task_ids\\\", type=str, default=None)\\n    p.add_argument(\\\"--domain_id\\\", type=int, default=3)\\n    p.add_argument(\\\"--denoise_steps\\\", type=int, default=10,\\n                   help=\\\"Flow matching denoising steps\\\")\\n    p.add_argument(\\\"--mode\\\", type=str, default=\\\"l2_norm\\\",\\n                   choices=[\\\"l2_norm\\\", \\\"random\\\"],\\n                   help=\\\"Pruning method: l2_norm (keep highest L2 norm tokens) or random (random selection)\\\")\\n    return p.parse_args()\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a",
  "uuid": "a6291b8a-272e-48ef-826f-eef44ff91cac",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\"\\\\\\\"\\\\\\\"X-VLA Vision Token Pruning Evaluation on LIBERO.\\\\n\\\\nPrunes vision tokens by L2 norm after Florence2's image encoder + linear projection,\\\\nbefore they enter the Florence2 language encoder. Evaluates on LIBERO suites.\\\\n\\\\nFollows official X-VLA evaluation protocol:\\\\n  - Absolute EEF control (use_delta=False)\\\\n  - 20D action space: [arm1: pos(3)+rot6d(6)+grip(1)] + [arm2: zeros(10)]\\\\n  - 20D proprio: [pos(3)+rot6d(6)+0.0] + zeros(10)\\\\n  - domain_id=3 for LIBERO\\\\n  - Closed-loop proprio update from last predicted action\\\\n\\\\nUsage:\\\\n    CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl python eval_xvla_pruning_libero.py \\\\\\\\\\\\n        --model_path /path/to/X-VLA-Libero \\\\\\\\\\\\n        --suite libero_object \\\\\\\\\\\\n        --keep_ratio 0.5 \\\\\\\\\\\\n        --num_episodes 50 \\\\\\\\\\\\n        --gpu 0\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nfrom __future__ import annotations\\\\n\\\\nimport argparse\\\\nimport json\\\\nimport logging\\\\nimport os\\\\nimport sys\\\\nimport time as time_mod\\\\nfrom pathlib import Path\\\\nfrom functools import wraps\\\\n\\\\nos.environ.setdefault(\\\\\\\"MUJOCO_GL\\\\\\\", \\\\\\\"egl\\\\\\\")\\\\n\\\\nimport numpy as np\\\\nimport torch\\\\nfrom PIL import Image\\\\n\\\\nsys.path.insert(0, str(Path(__file__).resolve().parent))\\\\n\\\\nlogging.basicConfig(\\\\n    level=logging.INFO,\\\\n    format=\\\\\\\"%(asctime)s [%(levelname)s] %(message)s\\\\\\\",\\\\n    datefmt=\\\\\\\"%Y-%m-%d %H:%M:%S\\\\\\\",\\\\n)\\\\nlog = logging.getLogger(__name__)\\\\n\\\\nSUITE_MAX_STEPS = {\\\\n    \\\\\\\"libero_spatial\\\\\\\": 800,\\\\n    \\\\\\\"libero_object\\\\\\\": 800,\\\\n    \\\\\\\"libero_goal\\\\\\\": 800,\\\\n    \\\\\\\"libero_10\\\\\\\": 900,\\\\n    \\\\\\\"libero_90\\\\\\\": 800,\\\\n}\\\\n\\\\nEPS = 1e-6\\\\n\\\\n\\\\ndef parse_args():\\\\n    p = argparse.ArgumentParser(description=\\\\\\\"X-VLA pruning eval on LIBERO\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--model_path\\\\\\\", type=str, default=\\\\\\\"2toINF/X-VLA-Libero\\\\\\\",\\\\n                   help=\\\\\\\"HuggingFace model path or local dir\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--suite\\\\\\\", type=str, default=\\\\\\\"libero_object\\\\\\\",\\\\n                   choices=list(SUITE_MAX_STEPS.keys()))\\\\n    p.add_argument(\\\\\\\"--keep_ratio\\\\\\\", type=float, default=1.0,\\\\n                   help=\\\\\\\"Fraction of vision tokens to keep (1.0 = no pruning)\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--num_episodes\\\\\\\", type=int, default=50)\\\\n    p.add_argument(\\\\\\\"--gpu\\\\\\\", type=int, default=0)\\\\n    p.add_argument(\\\\\\\"--seed\\\\\\\", type=int, default=42)\\\\n    p.add_argument(\\\\\\\"--max_steps\\\\\\\", type=int, default=None)\\\\n    p.add_argument(\\\\\\\"--output\\\\\\\", type=str, default=None)\\\\n    p.add_argument(\\\\\\\"--task_ids\\\\\\\", type=str, default=None)\\\\n    p.add_argument(\\\\\\\"--domain_id\\\\\\\", type=int, default=3)\\\\n    p.add_argument(\\\\\\\"--denoise_steps\\\\\\\", type=int, default=10,\\\\n                   help=\\\\\\\"Flow matching denoising steps\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--mode\\\\\\\", type=str, default=\\\\\\\"l2_norm\\\\\\\",\\\\n                   choices=[\\\\\\\"l2_norm\\\\\\\", \\\\\\\"random\\\\\\\"],\\\\n                   help=\\\\\\\"Pruning method: l2_norm (keep highest L2 norm tokens) or random (random selection)\\\\\\\")\\\\n    return p.parse_args()\\\\n\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"X-VLA Vision Token Pruning Evaluation on LIBERO.\\n\\nPrunes vision tokens by L2 norm after Florence2's image encoder + linear projection,\\nbefore they enter the Florence2 language encoder. Evaluates on LIBERO suites.\\n\\nFollows official X-VLA evaluation protocol:\\n  - Absolute EEF control (use_delta=False)\\n  - 20D action space: [arm1: pos(3)+rot6d(6)+grip(1)] + [arm2: zeros(10)]\\n  - 20D proprio: [pos(3)+rot6d(6)+0.0] + zeros(10)\\n  - domain_id=3 for LIBERO\\n  - Closed-loop proprio update from last predicted action\\n\\nUsage:\\n    CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl python eval_xvla_pruning_libero.py \\\\\\n        --model_path /path/to/X-VLA-Libero \\\\\\n        --suite libero_object \\\\\\n        --keep_ratio 0.5 \\\\\\n        --num_episodes 50 \\\\\\n        --gpu 0\\n\\\"\\\"\\\"\\n\\nfrom __future__ import annotations\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport sys\\nimport time as time_mod\\nfrom pathlib import Path\\nfrom functools import wraps\\n\\nos.environ.setdefault(\\\"MUJOCO_GL\\\", \\\"egl\\\")\\n\\nimport numpy as np\\nimport torch\\nfrom PIL import Image\\n\\nsys.path.insert(0, str(Path(__file__).resolve().parent))\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n    datefmt=\\\"%Y-%m-%d %H:%M:%S\\\",\\n)\\nlog = logging.getLogger(__name__)\\n\\nSUITE_MAX_STEPS = {\\n    \\\"libero_spatial\\\": 800,\\n    \\\"libero_object\\\": 800,\\n    \\\"libero_goal\\\": 800,\\n    \\\"libero_10\\\": 900,\\n    \\\"libero_90\\\": 800,\\n}\\n\\nEPS = 1e-6\\n\\n\\ndef parse_args():\\n    p = argparse.ArgumentParser(description=\\\"X-VLA pruning eval on LIBERO\\\")\\n    p.add_argument(\\\"--model_path\\\", type=str, default=\\\"2toINF/X-VLA-Libero\\\",\\n                   help=\\\"HuggingFace model path or local dir\\\")\\n    p.add_argument(\\\"--suite\\\", type=str, default=\\\"libero_object\\\",\\n                   choices=list(SUITE_MAX_STEPS.keys()))\\n    p.add_argument(\\\"--keep_ratio\\\", type=float, default=1.0,\\n                   help=\\\"Fraction of vision tokens to keep (1.0 = no pruning)\\\")\\n    p.add_argument(\\\"--num_episodes\\\", type=int, default=50)\\n    p.add_argument(\\\"--gpu\\\", type=int, default=0)\\n    p.add_argument(\\\"--seed\\\", type=int, default=42)\\n    p.add_argument(\\\"--max_steps\\\", type=int, default=None)\\n    p.add_argument(\\\"--output\\\", type=str, default=None)\\n    p.add_argument(\\\"--task_ids\\\", type=str, default=None)\\n    p.add_argument(\\\"--domain_id\\\", type=int, default=3)\\n    p.add_argument(\\\"--denoise_steps\\\", type=int, default=10,\\n                   help=\\\"Flow matching denoising steps\\\")\\n    p.add_argument(\\\"--mode\\\", type=str, default=\\\"l2_norm\\\",\\n                   choices=[\\\"l2_norm\\\", \\\"random\\\"],\\n                   help=\\\"Pruning method: l2_norm (keep highest L2 norm tokens) or random (random selection)\\\")\\n    return p.parse_args()\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 51_

两台服务器文件内容一致，`--mode` 参数已就位（默认 `l2_norm`，choices `[l2_norm, random]`）。

修改总结：
- **`parse_args()`**: 添加 `--mode` 参数，默认 `l2_norm`，choices `["l2_norm", "random"]`
- **`install_vision_pruning()`**: 新增 `mode` 参数，`l2_norm` 走原有 topk 逻辑，`random` 用 `torch.randperm` 随机选 k 个 token 并 sort 保持位置顺序
- **`summary["mode"]`**: 从硬编码 `"l2_norm_prune"` 改为 `args.mode`，反映实际使用的模式
- 已部署到 cqa1-33015 和 westd-38929

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a",
  "uuid": "c6a013e3-66fa-408f-92cb-162b64bb86f5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FaPubFY4KeMAivJf2G1Gdq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2817,
      "cache_read_input_tokens": 72605,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2817
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Task result

_source line 52_

两台服务器文件内容一致，`--mode` 参数已就位（默认 `l2_norm`，choices `[l2_norm, random]`）。

修改总结：
- **`parse_args()`**: 添加 `--mode` 参数，默认 `l2_norm`，choices `["l2_norm", "random"]`
- **`install_vision_pruning()`**: 新增 `mode` 参数，`l2_norm` 走原有 topk 逻辑，`random` 用 `torch.randperm` 随机选 k 个 token 并 sort 保持位置顺序
- **`summary["mode"]`**: 从硬编码 `"l2_norm_prune"` 改为 `args.mode`，反映实际使用的模式
- 已部署到 cqa1-33015 和 westd-38929

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 231050,
  "duration_api_ms": 230830,
  "num_turns": 16,
  "stop_reason": "end_turn",
  "session_id": "234f3a8c-b78f-4f7f-8fb2-ae24b22dd97a",
  "total_cost_usd": 1.0169929500000001,
  "usage": {
    "input_tokens": 15,
    "cache_creation_input_tokens": 63581,
    "cache_read_input_tokens": 432184,
    "output_tokens": 14997,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 63581,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 246,
        "cache_read_input_tokens": 72605,
        "cache_creation_input_tokens": 2817,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2817
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1676,
      "outputTokens": 259,
      "cacheReadInputTokens": 17987,
      "cacheCreationInputTokens": 19000,
      "webSearchRequests": 0,
      "costUSD": 0.0285197,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 15,
      "outputTokens": 14997,
      "cacheReadInputTokens": 432184,
      "cacheCreationInputTokens": 63581,
      "webSearchRequests": 0,
      "costUSD": 0.98847325,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "42ed97c3-4977-40ff-bb61-01560bcbeb08"
}
```

</details>

---
