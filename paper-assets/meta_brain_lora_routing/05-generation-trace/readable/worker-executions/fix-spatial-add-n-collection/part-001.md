# fix spatial add n collection — Part 1 of 2

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Worker execution logs

[Transcript overview](../fix-spatial-add-n-collection.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/8e/8e6aeb930bc2af2a390f.json)

## Before a recorded user message

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
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
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
  "uuid": "754f5a76-9c43-405d-bb7e-ef276465f9bc",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-meta-brain-lora-routing/memory/"
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
    "resetsAt": 1778880600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "82cb963a-bacc-44a8-b909-720a7e6c0231",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7"
}
```

---


### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by understanding the current state of the code and the LIBERO-Plus `_add_N` mechanism. I need to:

1. Read the current `collect_expert_demos.py`
2. Understand how Phase 0 handles `_add_N` tasks
3. Understand the LIBERO-Plus benchmark structure for `_add` tasks
4. Modify the script accordingly
5. Dry-run on cuda:1

Let me start by reading the relevant files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "d351a68b-0451-4adf-9301-9a8fc8ad5cd5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DfuQnYhv2PnTXg1THo4swH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11980,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11980
      },
      "output_tokens": 42,
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

先读取相关文件，了解现有代码和 `_add_N` 机制。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "134f9339-396c-40b2-a297-b736aac44cc1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DfuQnYhv2PnTXg1THo4swH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11980,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11980
      },
      "output_tokens": 42,
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

<details open><summary>🔧 Tool call — Agent · `toolu_013TqJ2cNFWJaMr9ra2qxnch`</summary>

```json
{
  "description": "Read collect_expert_demos.py",
  "subagent_type": "Explore",
  "prompt": "Read the full contents of /root/meta_brain_lora_routing/phase1/collect_expert_demos.py on the remote server. Since I can't SSH directly, read the local copy at /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/phase1/collect_expert_demos.py. If that doesn't exist, search for collect_expert_demos.py anywhere under /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/. Read the ENTIRE file, every line."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "7cbfd78a-0ad8-471b-a1d3-d5cd7deef57e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DfuQnYhv2PnTXg1THo4swH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11980,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11980
      },
      "output_tokens": 42,
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
  "task_id": "a2406d27283cd9ab4",
  "tool_use_id": "toolu_013TqJ2cNFWJaMr9ra2qxnch",
  "description": "Read collect_expert_demos.py",
  "task_type": "local_agent",
  "prompt": "Read the full contents of /root/meta_brain_lora_routing/phase1/collect_expert_demos.py on the remote server. Since I can't SSH directly, read the local copy at /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/phase1/collect_expert_demos.py. If that doesn't exist, search for collect_expert_demos.py anywhere under /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/. Read the ENTIRE file, every line.",
  "uuid": "271469f1-d0db-45b1-ba5a-2f70dc7a64d2",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7"
}
```

---


## Round 1

## Round 1

3 recorded events


### User

_source line 8 · 2026-05-15T17:50:18.433Z_

Read the full contents of /root/meta_brain_lora_routing/phase1/collect_expert_demos.py on the remote server. Since I can't SSH directly, read the local copy at /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/phase1/collect_expert_demos.py. If that doesn't exist, search for collect_expert_demos.py anywhere under /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/. Read the ENTIRE file, every line.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013TqJ2cNFWJaMr9ra2qxnch",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "cd29eab9-6220-4132-855e-4fc36d4da6f7"
}
```

</details>

---


### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Agent · `toolu_017LfjCZ3RrydbQw6jDiBQJj`</summary>

```json
{
  "description": "Read Phase 0 collect_activations",
  "subagent_type": "Explore",
  "prompt": "Read the full contents of /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/collect_activations.py. Read the ENTIRE file. I need to understand how Phase 0 handles objects_layout and _add_N tasks for LIBERO-Plus."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "b459e247-4d62-4252-b85d-a2018a274cb3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DfuQnYhv2PnTXg1THo4swH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11980,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11980
      },
      "output_tokens": 42,
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

_source line 10_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a2868964c1f8b5d5d",
  "tool_use_id": "toolu_017LfjCZ3RrydbQw6jDiBQJj",
  "description": "Read Phase 0 collect_activations",
  "task_type": "local_agent",
  "prompt": "Read the full contents of /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/collect_activations.py. Read the ENTIRE file. I need to understand how Phase 0 handles objects_layout and _add_N tasks for LIBERO-Plus.",
  "uuid": "b960e15c-6884-4f95-86ad-d6f7fc87a5c6",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7"
}
```

---


## Round 2

## Round 2

12 recorded events


### User

_source line 11 · 2026-05-15T17:50:20.488Z_

Read the full contents of /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/collect_activations.py. Read the ENTIRE file. I need to understand how Phase 0 handles objects_layout and _add_N tasks for LIBERO-Plus.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_017LfjCZ3RrydbQw6jDiBQJj",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "11e0aed9-c0bc-4e39-8f01-d0da1975d601"
}
```

</details>

---


### System

_source line 12_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2406d27283cd9ab4",
  "tool_use_id": "toolu_013TqJ2cNFWJaMr9ra2qxnch",
  "description": "Reading phase1/collect_expert_demos.py",
  "usage": {
    "total_tokens": 15694,
    "tool_uses": 1,
    "duration_ms": 2091
  },
  "last_tool_name": "Read",
  "uuid": "7281864f-22fb-4235-bbf6-b92e6ac07d85",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7"
}
```

---


### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_01V7hwHbbEJHzHdZMGW1SRNp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/phase1/collect_expert_demos.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013TqJ2cNFWJaMr9ra2qxnch",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "52c1d309-94aa-453e-a16f-4394048d35ee",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FjVkfGP5rSppPjkZK4poUs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15685,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15685,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 14 · 2026-05-15T17:50:20.544Z_

<details><summary>↩ Tool result · reported error · `toolu_01V7hwHbbEJHzHdZMGW1SRNp`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013TqJ2cNFWJaMr9ra2qxnch",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "f3369041-338f-4336-9f62-47c667857226",
  "tool_use_result": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing."
}
```

</details>

---


### System

_source line 15_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2868964c1f8b5d5d",
  "tool_use_id": "toolu_017LfjCZ3RrydbQw6jDiBQJj",
  "description": "Reading artifacts/phase0/collect_activations.py",
  "usage": {
    "total_tokens": 15636,
    "tool_uses": 1,
    "duration_ms": 1301
  },
  "last_tool_name": "Read",
  "uuid": "68ac6b8c-a901-4ce6-897b-e49ade32cdf1",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7"
}
```

---


### System

_source line 16_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2406d27283cd9ab4",
  "tool_use_id": "toolu_013TqJ2cNFWJaMr9ra2qxnch",
  "description": "Finding /home/ubuntu/.agent-ml-research-be-idea-gen-0515/…",
  "usage": {
    "total_tokens": 16715,
    "tool_uses": 2,
    "duration_ms": 3924
  },
  "last_tool_name": "Glob",
  "uuid": "46df40ac-9e48-4566-9e7f-03fa416da0c0",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7"
}
```

---


### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Glob · `toolu_01DJvdnoVNUsbwuGkKVTHBGM`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/**/collect_expert_demos.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013TqJ2cNFWJaMr9ra2qxnch",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "3769653e-1763-41ab-95bd-807ab6143abf",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BLbi6giNzw2ynosDKPegjV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1015,
      "cache_read_input_tokens": 15685,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1015,
        "ephemeral_1h_input_tokens": 0
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

_source line 18 · 2026-05-15T17:50:22.378Z_

<details><summary>↩ Tool result · `toolu_01DJvdnoVNUsbwuGkKVTHBGM`</summary>

```text
artifacts/phase1/collect_expert_demos.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013TqJ2cNFWJaMr9ra2qxnch",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "314517a0-1379-4c18-a5be-c8c1ed51c52b"
}
```

</details>

---


### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_01KeA6rw1WmChZrVyGNDzRS1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/collect_activations.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_017LfjCZ3RrydbQw6jDiBQJj",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "25cb3ae7-6627-417d-8bc8-e84cdf7b18db",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011kz1EjKaKVMKSpuQ5NupY2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 507,
      "cache_read_input_tokens": 15114,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 507,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 20 · 2026-05-15T17:50:21.802Z_

<details><summary>↩ Tool result · `toolu_01KeA6rw1WmChZrVyGNDzRS1`</summary>

```text
1	"""
2	Collect frozen π₀ activations from LIBERO-Plus rollouts.
3	
4	Registers forward hooks on PaliGemma LLM layers and Action Expert layers,
5	runs episodes under each perturbation type (or nominal), and saves per-layer
6	activations with 4 pooling strategies in fp16.
7	
8	Usage:
9	    # Collect camera perturbation episodes
10	    python collect_activations.py \
11	        --checkpoint /path/to/pi0_base \
12	        --output_dir ./activations \
13	        --perturbation_type camera_viewpoints \
14	        --num_episodes 50 \
15	        --device cuda:0
16	
17	    # Collect all perturbation types
18	    python collect_activations.py \
19	        --checkpoint /path/to/pi0_base \
20	        --output_dir ./activations \
21	        --perturbation_type all \
22	        --num_episodes 50
23	
24	    # Collect nominal (no perturbation) baseline
25	    python collect_activations.py \
26	        --checkpoint /path/to/pi0_base \
27	        --output_dir ./activations \
28	        --perturbation_type nominal \
29	        --num_episodes 100
30	
31	Dependencies:
32	    torch, safetensors, openpi (for model loading), libero
33	"""
34	
35	import argparse
36	import logging
37	import os
38	from pathlib import Path
39	from typing import Any
40	
41	import torch
42	import torch.nn as nn
43	
44	from configs import (
45	    CLASS_6_TO_3_MAPPING,
46	    EXPERT_LAYER_TEMPLATE,
47	    EXPERT_LAYERS,
48	    PALIGEMMA_LAYER_TEMPLATE,
49	    PALIGEMMA_LAYERS,
50	    PERTURBATION_TYPES_6CLASS,
51	    POOLING_STRATEGIES,
52	)
53	from libero_integration import (
54	    load_pi0_for_collection,
55	    obs_to_model_input,
56	    run_episode,
57	)
58	
59	log = logging.getLogger(__name__)
60	
61	
62	# ---------------------------------------------------------------------------
63	# Pooling helpers
64	# ---------------------------------------------------------------------------
65	
66	def pool_activation(hidden_states: torch.Tensor, strategy: str) -> torch.Tensor:
67	    """Pool a (batch, seq_len, hidden_dim) tensor into (batch, D).
68	
69	    Strategies:
70	        mean       — mean over seq_len → (batch, hidden_dim)
71	        first      — first token       → (batch, hidden_dim)
72	        last       — last token        → (batch, hidden_dim)
73	        first_last — concat first+last → (batch, hidden_dim*2)
74	    """
75	    if strategy == "mean":
76	        return hidden_states.mean(dim=1)
77	    elif strategy == "first":
78	        return hidden_states[:, 0]
79	    elif strategy == "last":
80	        return hidden_states[:, -1]
81	    elif strategy == "first_last":
82	        return torch.cat([hidden_states[:, 0], hidden_states[:, -1]], dim=-1)
83	    raise ValueError(f"Unknown pooling strategy: {strategy}")
84	
85	
86	# ---------------------------------------------------------------------------
87	# Hook manager
88	# ---------------------------------------------------------------------------
89	
90	class ActivationCollector:
91	    """Registers hooks on specified layers and stores pooled activations."""
92	
93	    def __init__(self, model: nn.Module):
94	        self.model = model
95	        self._hooks: list[torch.utils.hooks.RemovableHook] = []
96	        self._raw: dict[str, torch.Tensor] = {}  # layer_name -> last hidden_states
97	
98	    def register_hooks(self) -> None:
99	        for i in PALIGEMMA_LAYERS:
100	            name = f"paligemma_layer_{i}"
101	            module_path = PALIGEMMA_LAYER_TEMPLATE.format(i=i)
102	            module = _get_submodule(self.model, module_path)
103	            self._hooks.append(
104	                module.register_forward_hook(self._make_hook(name))
105	            )
106	            log.info("Hooked %s -> %s", name, module_path)
107	
108	        for i in EXPERT_LAYERS:
109	            name = f"expert_layer_{i}"
110	            module_path = EXPERT_LAYER_TEMPLATE.format(i=i)
111	            module = _get_submodule(self.model, module_path)
112	            self._hooks.append(
113	                module.register_forward_hook(self._make_hook(name))
114	            )
115	            log.info("Hooked %s -> %s", name, module_path)
116	
117	    def _make_hook(self, name: str):
118	        def hook_fn(_module, _input, output):
119	            # Gemma layers return (hidden_states, ...) or just hidden_states
120	            if isinstance(output, tuple):
121	                h = output[0]
122	            else:
123	                h = output
124	            self._raw[name] = h.detach()
125	        return hook_fn
126	
127	    def get_pooled(self) -> dict[str, dict[str, torch.Tensor]]:
128	        """Return {layer_name: {pooling_strategy: tensor(fp16)}} from last forward."""
129	        result = {}
130	        for name, h in self._raw.items():
131	            result[name] = {}
132	            for strat in POOLING_STRATEGIES:
133	                pooled = pool_activation(h, strat)
134	                result[name][strat] = pooled.half().cpu()
135	        return result
136	
137	    def clear(self) -> None:
138	        self._raw.clear()
139	
140	    def remove_hooks(self) -> None:
141	        for h in self._hooks:
142	            h.remove()
143	        self._hooks.clear()
144	
145	
146	def _get_submodule(model: nn.Module, path: str) -> nn.Module:
147	    parts = path.split(".")
148	    m = model
149	    for p in parts:
150	        if p.isdigit():
151	            m = m[int(p)]
152	        else:
153	            m = getattr(m, p)
154	    return m
155	
156	
157	# load_pi0_model, rollout_episode, _obs_to_model_input replaced by
158	# load_pi0_for_collection, run_episode, obs_to_model_input from libero_integration
159	
160	
161	# ---------------------------------------------------------------------------
162	# Data saving
163	# ---------------------------------------------------------------------------
164	
165	def save_episodes(
166	    episodes: list[dict[str, Any]],
167	    perturbation_type: str,
168	    output_dir: Path,
169	) -> None:
170	    output_dir.mkdir(parents=True, exist_ok=True)
171	    out_path = output_dir / f"{perturbation_type}.pt"
172	
173	    # Support incremental collection: append to existing file
174	    if out_path.exists():
175	        existing = torch.load(out_path, weights_only=False)
176	        log.info("Appending %d episodes to existing %d in %s",
177	                 len(episodes), len(existing), out_path)
178	        episodes = existing + episodes
179	
180	    torch.save(episodes, out_path)
181	    log.info("Saved %d episodes to %s", len(episodes), out_path)
182	
183	
184	# ---------------------------------------------------------------------------
185	# Main
186	# ---------------------------------------------------------------------------
187	
188	def make_labels(perturbation_type: str) -> dict[str, int]:
189	    if perturbation_type == "nominal":
190	        return {"label_6class": -1, "label_3class": -1, "label_binary": 0}
191	
192	    label_6 = PERTURBATION_TYPES_6CLASS[perturbation_type]
193	    label_3 = CLASS_6_TO_3_MAPPING[label_6]
194	    return {"label_6class": label_6, "label_3class": label_3, "label_binary": 1}
195	
196	
197	def _set_seed(seed: int) -> None:
198	    import random
199	    import numpy as np
200	    random.seed(seed)
201	    np.random.seed(seed)
202	    torch.manual_seed(seed)
203	    if torch.cuda.is_available():
204	        torch.cuda.manual_seed_all(seed)
205	
206	
207	def collect(args: argparse.Namespace) -> None:
208	    _set_seed(args.seed)
209	    device = args.device
210	    output_dir = Path(args.output_dir)
211	
212	    log.info("Seed=%d, loading model from %s", args.seed, args.checkpoint)
213	    policy, model = load_pi0_for_collection(args.checkpoint, device)
214	
215	    collector = ActivationCollector(model)
216	    collector.register_hooks()
217	
218	    perturbation_types: list[str]
219	    if args.perturbation_type == "all":
220	        perturbation_types = list(PERTURBATION_TYPES_6CLASS.keys())
221	    else:
222	        perturbation_types = [args.perturbation_type]
223	
224	    for ptype in perturbation_types:
225	        is_nominal = ptype == "nominal"
226	        log.info("Collecting %d episodes for %s", args.num_episodes, ptype)
227	
228	        episodes = []
229	        for ep_idx in range(args.num_episodes):
230	            log.info("  Episode %d/%d", ep_idx + 1, args.num_episodes)
231	            try:
232	                result = run_episode(
233	                    policy, collector,
234	                    perturbation_type=None if is_nominal else ptype,
235	                    device=device,
236	                    task_suite=args.task_suite,
237	                    seed=args.seed + ep_idx,
238	                )
239	            except Exception:
240	                log.exception("Episode %d failed, skipping", ep_idx)
241	                continue
242	
243	            labels = make_labels(ptype)
244	            episode_data = {
245	                "activations": result["activations"],
246	                **labels,
247	                "metadata": {
248	                    "perturbation_type": ptype,
249	                    "task_name": result["task_name"],
250	                    "num_steps": result["num_steps"],
251	                    "success": result["success"],
252	                    "episode_idx": ep_idx,
253	                },
254	            }
255	            episodes.append(episode_data)
256	
257	        save_episodes(episodes, ptype, output_dir)
258	
259	    collector.remove_hooks()
260	    log.info("Collection complete.")
261	
262	
263	def parse_args() -> argparse.Namespace:
264	    p = argparse.ArgumentParser(
265	        description="Collect π₀ activations from LIBERO-Plus rollouts"
266	    )
267	    p.add_argument(
268	        "--checkpoint", type=str, required=True,
269	        help="Path to π₀ checkpoint directory (with .safetensors files)",
270	    )
271	    p.add_argument(
272	        "--output_dir", type=str, default="./activations",
273	        help="Directory to save activation .pt files",
274	    )
275	    valid_types = list(PERTURBATION_TYPES_6CLASS.keys()) + ["all", "nominal"]
276	    p.add_argument(
277	        "--perturbation_type", type=str, default="all",
278	        choices=valid_types,
279	        help="Perturbation type to collect, 'all' for all 6, or 'nominal'",
280	    )
281	    p.add_argument(
282	        "--num_episodes", type=int, default=50,
283	        help="Number of episodes per perturbation type",
284	    )
285	    p.add_argument(
286	        "--task_suite", type=str, default="libero_spatial",
287	        choices=["libero_spatial", "libero_object", "libero_goal", "libero_10", "libero_90"],
288	        help="LIBERO-Plus suite (libero_90 has no perturbation variants)",
289	    )
290	    p.add_argument(
291	        "--device", type=str, default="cuda:0",
292	        help="Device for model inference",
293	    )
294	    p.add_argument(
295	        "--seed", type=int, default=42,
296	        help="Global random seed for reproducibility",
297	    )
298	    return p.parse_args()
299	
300	
301	if __name__ == "__main__":
302	    logging.basicConfig(
303	        level=logging.INFO,
304	        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
305	    )
306	    args = parse_args()
307	    collect(args)
308	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_017LfjCZ3RrydbQw6jDiBQJj",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "7d9f4df0-0ebe-4ece-b5de-7b60b34cce17"
}
```

</details>

---


### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Agent · `toolu_01AAzcHk6Tcmrn7a4QSKE2eu`</summary>

```json
{
  "description": "Explore LIBERO-Plus _add mechanism",
  "subagent_type": "Explore",
  "prompt": "Search broadly under /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/ for any references to \"_add\", \"objects_layout\", \"add_n\", \"distractor\", \"new_objects\", \"perturb_region\" in Python files. Also look for any LIBERO-Plus related code or configuration. I want to understand:\n1. How _add_N tasks work in LIBERO-Plus\n2. How perturb_region_info() is currently used\n3. What the benchmark API looks like for loading _add tasks\nSearch breadth: very thorough"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "6749a9d3-f824-4919-a7fc-5a858b90f8ad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DfuQnYhv2PnTXg1THo4swH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11980,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11980
      },
      "output_tokens": 42,
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

_source line 22_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a3acedec04983e0ad",
  "tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "description": "Explore LIBERO-Plus _add mechanism",
  "task_type": "local_agent",
  "prompt": "Search broadly under /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/ for any references to \"_add\", \"objects_layout\", \"add_n\", \"distractor\", \"new_objects\", \"perturb_region\" in Python files. Also look for any LIBERO-Plus related code or configuration. I want to understand:\n1. How _add_N tasks work in LIBERO-Plus\n2. How perturb_region_info() is currently used\n3. What the benchmark API looks like for loading _add tasks\nSearch breadth: very thorough",
  "uuid": "79008256-d8b8-43f2-8198-f0ea52aeca55",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7"
}
```

---


## Round 3

## Round 3

203 recorded events


### User

_source line 23 · 2026-05-15T17:50:23.127Z_

Search broadly under /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/ for any references to "_add", "objects_layout", "add_n", "distractor", "new_objects", "perturb_region" in Python files. Also look for any LIBERO-Plus related code or configuration. I want to understand:
1. How _add_N tasks work in LIBERO-Plus
2. How perturb_region_info() is currently used
3. What the benchmark API looks like for loading _add tasks
Search breadth: very thorough

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "4a16e5ec-97ca-4355-8d0d-efdfeb231479"
}
```

</details>

---


### System

_source line 24_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2406d27283cd9ab4",
  "tool_use_id": "toolu_013TqJ2cNFWJaMr9ra2qxnch",
  "description": "Reading artifacts/phase1/collect_expert_demos.py",
  "usage": {
    "total_tokens": 16857,
    "tool_uses": 3,
    "duration_ms": 5374
  },
  "last_tool_name": "Read",
  "uuid": "32e4b53e-9b4a-4ebf-add0-d5ceb1de1655",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7"
}
```

---


### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Read · `toolu_01HvQRbAkbwdhXRwFvLkr4Bw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013TqJ2cNFWJaMr9ra2qxnch",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "e69515d0-57a5-47d9-b569-f9e446ae78bf",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BcCMV9K6PcdBjWZUp15RWp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 141,
      "cache_read_input_tokens": 16700,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 141,
        "ephemeral_1h_input_tokens": 0
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

_source line 26 · 2026-05-15T17:50:23.844Z_

<details><summary>↩ Tool result · `toolu_01HvQRbAkbwdhXRwFvLkr4Bw`</summary>

```text
1	"""
2	Collect expert demonstrations by rolling out frozen π₀ in perturbed LIBERO environments.
3	
4	Only successful episodes are saved. Two perturbation types are supported:
5	  - physical: vary robot initial state (init_states index 1-49)
6	  - spatial:  perturb object layout via BDDL region_info modifications
7	
8	Output: pickle files with (observations, actions, metadata) per episode.
9	
10	Usage:
11	    # Physical perturbation dry-run
12	    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \
13	        --perturbation_type physical --dry_run
14	
15	    # Spatial perturbation dry-run
16	    CUDA_VISIBLE_DEVICES=2 python collect_expert_demos.py \
17	        --perturbation_type spatial --dry_run
18	
19	    # Full physical collection
20	    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \
21	        --perturbation_type physical
22	"""
23	
24	import argparse
25	import collections
26	import copy
27	import logging
28	import math
29	import os
30	import pickle
31	import random
32	import re
33	import sys
34	import time
35	import types
36	from pathlib import Path
37	from typing import Any
38	
39	import numpy as np
40	import torch
41	
42	log = logging.getLogger(__name__)
43	
44	# ---------------------------------------------------------------------------
45	# Constants
46	# ---------------------------------------------------------------------------
47	
48	LIBERO_DUMMY_ACTION = [0.0] * 6 + [-1.0]
49	LIBERO_ENV_RESOLUTION = 256
50	MODEL_INPUT_RESOLUTION = 224
51	REPLAN_STEPS = 5
52	NUM_STEPS_WAIT = 10
53	MAX_STEPS = 220  # libero_spatial default
54	
55	# 10 base tasks in libero_spatial (no perturbation suffix)
56	BASE_TASK_SUITE = "libero_spatial"
57	
58	# Spatial perturbation grid: 10 configurations with varying XY shifts and yaw
59	# Magnitudes chosen to be noticeable but within feasible reach of the robot.
60	SPATIAL_PERTURBATION_CONFIGS = [
61	    {"delta_xy": ( 0.05,  0.00), "delta_half_len": 0.0,  "delta_yaw": (0.0, 0.0)},
62	    {"delta_xy": (-0.05,  0.00), "delta_half_len": 0.0,  "delta_yaw": (0.0, 0.0)},
63	    {"delta_xy": ( 0.00,  0.05), "delta_half_len": 0.0,  "delta_yaw": (0.0, 0.0)},
64	    {"delta_xy": ( 0.00, -0.05), "delta_half_len": 0.0,  "delta_yaw": (0.0, 0.0)},
65	    {"delta_xy": ( 0.03,  0.03), "delta_half_len": 0.0,  "delta_yaw": (0.0, 0.0)},
66	    {"delta_xy": (-0.03, -0.03), "delta_half_len": 0.0,  "delta_yaw": (0.0, 0.0)},
67	    {"delta_xy": ( 0.04,  0.00), "delta_half_len": 0.01, "delta_yaw": (0.3, 0.0)},
68	    {"delta_xy": (-0.04,  0.00), "delta_half_len": 0.01, "delta_yaw": (-0.3, 0.0)},
69	    {"delta_xy": ( 0.00,  0.04), "delta_half_len": 0.0,  "delta_yaw": (0.0, 0.3)},
70	    {"delta_xy": ( 0.00, -0.04), "delta_half_len": 0.0,  "delta_yaw": (0.0, -0.3)},
71	]
72	
73	
74	# ---------------------------------------------------------------------------
75	# Geometry / image helpers (from libero_integration.py)
76	# ---------------------------------------------------------------------------
77	
78	def _quat2axisangle(quat: np.ndarray) -> np.ndarray:
79	    """Quaternion [x,y,z,w] -> axis-angle [ax,ay,az]."""
80	    q = np.asarray(quat, dtype=np.float64)
81	    norm = np.linalg.norm(q)
82	    if norm < 1e-8:
83	        return np.zeros(3, dtype=np.float32)
84	    q /= norm
85	    sin_half = np.linalg.norm(q[:3])
86	    if sin_half < 1e-8:
87	        return np.zeros(3, dtype=np.float32)
88	    angle = 2.0 * math.atan2(sin_half, q[3])
89	    axis = q[:3] / sin_half
90	    return (axis * angle).astype(np.float32)
91	
92	
93	def _resize_with_pad(img: np.ndarray, size: int) -> np.ndarray:
94	    """Resize image with aspect-preserving padding to (size, size, 3) uint8."""
95	    try:
96	        from openpi_client.image_tools import resize_with_pad, convert_to_uint8
97	        return convert_to_uint8(resize_with_pad(img, size, size))
98	    except ImportError:
99	        from PIL import Image as PILImage
100	        h, w = img.shape[:2]
101	        scale = min(size / h, size / w)
102	        new_h, new_w = int(h * scale), int(w * scale)
103	        resized = np.array(
104	            PILImage.fromarray(img).resize((new_w, new_h), PILImage.BILINEAR)
105	        )
106	        canvas = np.zeros((size, size, 3), dtype=np.uint8)
107	        y0, x0 = (size - new_h) // 2, (size - new_w) // 2
108	        canvas[y0 : y0 + new_h, x0 : x0 + new_w] = resized
109	        return canvas
110	
111	
112	def obs_to_model_input(obs: dict, task_description: str) -> dict:
113	    """Convert LIBERO observation to the dict format expected by policy.infer()."""
114	    base_img = np.ascontiguousarray(obs["agentview_image"][::-1, ::-1])
115	    wrist_img = np.ascontiguousarray(obs["robot0_eye_in_hand_image"][::-1, ::-1])
116	
117	    base_img = _resize_with_pad(base_img, MODEL_INPUT_RESOLUTION)
118	    wrist_img = _resize_with_pad(wrist_img, MODEL_INPUT_RESOLUTION)
119	
120	    state = np.concatenate([
121	        obs["robot0_eef_pos"].astype(np.float32),
122	        _quat2axisangle(obs["robot0_eef_quat"]),
123	        obs["robot0_gripper_qpos"].astype(np.float32),
124	    ])
125	
126	    return {
127	        "observation/image": base_img,
128	        "observation/wrist_image": wrist_img,
129	        "observation/state": state,
130	        "prompt": task_description,
131	    }
132	
133	
134	def extract_obs_for_saving(obs: dict) -> dict:
135	    """Extract observation fields to save in demo data (images stored as uint8)."""
136	    return {
137	        "agentview_image": obs["agentview_image"].copy(),
138	        "robot0_eye_in_hand_image": obs["robot0_eye_in_hand_image"].copy(),
139	        "robot0_eef_pos": obs["robot0_eef_pos"].astype(np.float32).copy(),
140	        "robot0_eef_quat": obs["robot0_eef_quat"].astype(np.float32).copy(),
141	        "robot0_gripper_qpos": obs["robot0_gripper_qpos"].astype(np.float32).copy(),
142	    }
143	
144	
145	# ---------------------------------------------------------------------------
146	# Model loading
147	# ---------------------------------------------------------------------------
148	
149	def _ensure_openpi_imports():
150	    """Stub out lerobot (training-only dep) before importing OpenPI."""
151	    for mod in [
152	        "lerobot", "lerobot.common", "lerobot.common.datasets",
153	        "lerobot.common.datasets.lerobot_dataset",
154	    ]:
155	        if mod not in sys.modules:
156	            sys.modules[mod] = types.ModuleType(mod)
157	
158	
159	def load_pi0_policy(checkpoint_path: str, device: str) -> object:
160	    """Load pi0 policy via OpenPI. Returns the Policy object for inference."""
161	    _ensure_openpi_imports()
162	    from openpi.training import config as _config
163	    from openpi.policies import policy_config
164	
165	    train_config = _config.get_config("pi0_libero")
166	    policy = policy_config.create_trained_policy(
167	        train_config, checkpoint_path, pytorch_device=device
168	    )
169	    log.info("Loaded pi0 policy on %s", device)
170	    return policy
171	
172	
173	# ---------------------------------------------------------------------------
174	# Task discovery
175	# ---------------------------------------------------------------------------
176	
177	def find_base_tasks(bddl_dir: str, num_tasks: int = 10) -> list[dict]:
178	    """Find base (unperturbed) BDDL files in libero_spatial.
179	
180	    Returns list of dicts with keys: name, bddl_path, init_states_path.
181	    """
182	    all_files = [f for f in os.listdir(bddl_dir) if f.endswith(".bddl")]
183	
184	    base_names = []
185	    for f in sorted(all_files):
186	        name = f.replace(".bddl", "")
187	        # Skip any file with perturbation suffixes
188	        if re.search(
189	            r"(_add_\d+|_table_\d+|_tb_\d+|_light_\d+|_language_\d+"
190	            r"|_view_|_noise_|_level\d+| copy)",
191	            name,
192	        ):
193	            continue
194	        base_names.append(name)
195	
196	    init_dir = bddl_dir.replace("bddl_files", "init_files")
197	    tasks = []
198	    for name in base_names[:num_tasks]:
199	        bddl_path = os.path.join(bddl_dir, f"{name}.bddl")
200	        init_path = os.path.join(init_dir, f"{name}.pruned_init")
201	        if not os.path.exists(init_path):
202	            log.warning("init_states not found for %s, skipping", name)
203	            continue
204	        tasks.append({
205	            "name": name,
206	            "bddl_path": bddl_path,
207	            "init_states_path": init_path,
208	        })
209	
210	    log.info("Found %d base tasks", len(tasks))
211	    return tasks
212	
213	
214	def get_task_language(bddl_path: str) -> str:
215	    """Extract language instruction from a BDDL file."""
216	    from libero.libero.envs.bddl_utils import get_problem_info
217	    info = get_problem_info(bddl_path)
218	    return info["language_instruction"]
219	
220	
221	# ---------------------------------------------------------------------------
222	# Environment creation
223	# ---------------------------------------------------------------------------
224	
225	def create_env(bddl_path: str) -> object:
226	    """Create a LIBERO OffScreenRenderEnv from a BDDL file."""
227	    from libero.libero.envs import OffScreenRenderEnv
228	    env = OffScreenRenderEnv(
229	        bddl_file_name=bddl_path,
230	        camera_heights=LIBERO_ENV_RESOLUTION,
231	        camera_widths=LIBERO_ENV_RESOLUTION,
232	    )
233	    return env
234	
235	
236	def create_spatial_bddl(
237	    base_bddl_path: str,
238	    perturbation_config: dict,
239	    output_dir: str,
240	) -> str:
241	    """Create a perturbed BDDL file by applying spatial perturbation to all regions.
242	
243	    Returns the path to the new BDDL file.
244	    """
245	    sys.path.insert(0, "/root/LIBERO-plus/libero")
246	    from libero.randomizer.bddl_operators import (
247	        load_bddl_file,
248	        save_bddl_file,
249	        perturb_region_info,
250	    )
251	
252	    spec = load_bddl_file(base_bddl_path)
253	    delta_xy = perturbation_config["delta_xy"]
254	    delta_half = perturbation_config["delta_half_len"]
255	    delta_yaw = perturbation_config["delta_yaw"]
256	
257	    for i in range(len(spec.region_infos)):
258	        spec.region_infos[i] = perturb_region_info(
259	            spec.region_infos[i],
260	            delta_region_centroid_xy=delta_xy,
261	            delta_region_half_len=delta_half,
262	            delta_yaw_rotation=delta_yaw,
263	        )
264	
265	    os.makedirs(output_dir, exist_ok=True)
266	    base_name = Path(base_bddl_path).stem
267	    dx, dy = delta_xy
268	    filename = f"{base_name}_spatial_dx{dx:.2f}_dy{dy:.2f}.bddl"
269	    _, filepath = save_bddl_file(spec, bddl_filename=filename, bddl_dirpath=output_dir)
270	    return filepath
271	
272	
273	# ---------------------------------------------------------------------------
274	# Episode rollout
275	# ---------------------------------------------------------------------------
276	
277	def rollout_episode(
278	    policy: object,
279	    env: object,
280	    task_description: str,
281	    init_states: np.ndarray,
282	    init_state_idx: int,
283	    seed: int,
284	) -> dict[str, Any]:
285	    """Run one episode, collecting (obs, action) pairs.
286	
287	    Returns dict with observations, actions, success, num_steps.
288	    """
289	    env.seed(seed)
290	    obs = env.set_init_state(init_states[init_state_idx])
291	
292	    for _ in range(NUM_STEPS_WAIT):
293	        obs, _, _, _ = env.step(LIBERO_DUMMY_ACTION)
294	
295	    all_obs = [extract_obs_for_saving(obs)]
296	    all_actions = []
297	    action_plan = collections.deque()
298	    step = 0
299	    success = False
300	    done = False
301	
302	    while not done and step < MAX_STEPS:
303	        if len(action_plan) == 0:
304	            obs_dict = obs_to_model_input(obs, task_description)
305	            result = policy.infer(obs_dict)
306	            action_chunk = result["actions"]
307	            action_plan.extend(action_chunk[:REPLAN_STEPS])
308	
309	        action = action_plan.popleft()
310	        if isinstance(action, torch.Tensor):
311	            action = action.cpu().numpy()
312	        action_np = np.asarray(action, dtype=np.float32)
313	
314	        obs, reward, done, info = env.step(
315	            action_np.tolist() if hasattr(action_np, "tolist") else list(action_np)
316	        )
317	        step += 1
318	
319	        all_obs.append(extract_obs_for_saving(obs))
320	        all_actions.append(action_np)
321	
322	        if done or reward > 0:
323	            success = info.get("success", reward > 0)
324	
325	    return {
326	        "observations": all_obs,
327	        "actions": np.stack(all_actions) if all_actions else np.zeros((0, 7)),
328	        "success": success,
329	        "num_steps": step,
330	    }
331	
332	
333	# ---------------------------------------------------------------------------
334	# Collection loops
335	# ---------------------------------------------------------------------------
336	
337	def collect_physical(
338	    policy: object,
339	    tasks: list[dict],
340	    episodes_per_config: int,
341	    output_dir: str,
342	    dry_run: bool,
343	) -> dict:
344	    """Collect expert demos with physical (robot initial state) perturbation.
345	
346	    Uses init_states indices 1-49 (index 0 is nominal).
347	    """
348	    os.makedirs(output_dir, exist_ok=True)
349	    stats = {"total": 0, "success": 0, "saved_files": []}
350	
351	    init_state_indices = list(range(1, 50))  # 49 perturbed states
352	    if dry_run:
353	        tasks = tasks[:1]
354	        init_state_indices = [1]
355	        episodes_per_config = 1
356	
357	    for task_info in tasks:
358	        task_name = task_info["name"]
359	        init_states = torch.load(task_info["init_states_path"], weights_only=False)
360	        language = get_task_language(task_info["bddl_path"])
361	        log.info("Task: %s (%d init_states available)", task_name, len(init_states))
362	
363	        for idx in init_state_indices:
364	            if idx >= len(init_states):
365	                continue
366	
367	            for ep in range(episodes_per_config):
368	                seed = hash((task_name, idx, ep)) % (2**31)
369	                stats["total"] += 1
370	
371	                try:
372	                    env = create_env(task_info["bddl_path"])
373	                    result = rollout_episode(
374	                        policy, env, language, init_states, idx, seed
375	                    )
376	                    env.close()
377	                except Exception:
378	                    log.exception(
379	                        "Episode failed: task=%s idx=%d ep=%d", task_name, idx, ep
380	                    )
381	                    continue
382	
383	                if result["success"]:
384	                    stats["success"] += 1
385	                    demo = {
386	                        "observations": result["observations"],
387	                        "actions": result["actions"],
388	                        "task_name": task_name,
389	                        "perturbation_config": {
390	                            "type": "physical",
391	                            "init_state_idx": idx,
392	                        },
393	                        "success": True,
394	                        "num_steps": result["num_steps"],
395	                    }
396	                    fname = f"{task_name}_initstate{idx}_ep{ep}.pkl"
397	                    fpath = os.path.join(output_dir, fname)
398	                    with open(fpath, "wb") as f:
399	                        pickle.dump(demo, f, protocol=pickle.HIGHEST_PROTOCOL)
400	                    stats["saved_files"].append(fpath)
401	
402	                rate = stats["success"] / stats["total"] * 100
403	                log.info(
404	                    "[physical] task=%s idx=%d ep=%d | %s | "
405	                    "cumulative %d/%d (%.1f%%)",
406	                    task_name, idx, ep,
407	                    "SUCCESS" if result["success"] else "FAIL",
408	                    stats["success"], stats["total"], rate,
409	                )
410	
411	    return stats
412	
413	
414	def collect_spatial(
415	    policy: object,
416	    tasks: list[dict],
417	    episodes_per_config: int,
418	    output_dir: str,
419	    dry_run: bool,
420	) -> dict:
421	    """Collect expert demos with spatial (objects layout) perturbation.
422	
423	    Applies 10 predefined spatial perturbation configs to each base task.
424	    """
425	    os.makedirs(output_dir, exist_ok=True)
426	    tmp_bddl_dir = os.path.join(output_dir, "_tmp_bddl")
427	    os.makedirs(tmp_bddl_dir, exist_ok=True)
428	    stats = {"total": 0, "success": 0, "saved_files": []}
429	
430	    configs = SPATIAL_PERTURBATION_CONFIGS
431	    if dry_run:
432	        tasks = tasks[:1]
433	        configs = configs[:1]
434	        episodes_per_config = 1
435	
436	    for task_info in tasks:
437	        task_name = task_info["name"]
438	        init_states = torch.load(task_info["init_states_path"], weights_only=False)
439	        log.info("Task: %s", task_name)
440	
441	        for cfg_idx, cfg in enumerate(configs):
442	            try:
443	                perturbed_bddl = create_spatial_bddl(
444	                    task_info["bddl_path"], cfg, tmp_bddl_dir
445	                )
446	                language = get_task_language(perturbed_bddl)
447	            except Exception:
448	                log.exception(
449	                    "BDDL perturbation failed: task=%s cfg=%d", task_name, cfg_idx
450	                )
451	                continue
452	
453	            for ep in range(episodes_per_config):
454	                seed = hash((task_name, cfg_idx, ep)) % (2**31)
455	                stats["total"] += 1
456	
457	                try:
458	                    env = create_env(perturbed_bddl)
459	                    # Use nominal init_state (index 0) for spatial perturbation
460	                    result = rollout_episode(
461	                        policy, env, language, init_states, 0, seed
462	                    )
463	                    env.close()
464	                except Exception:
465	                    log.exception(
466	                        "Episode failed: task=%s cfg=%d ep=%d",
467	                        task_name, cfg_idx, ep,
468	                    )
469	                    continue
470	
471	                if result["success"]:
472	                    stats["success"] += 1
473	                    demo = {
474	                        "observations": result["observations"],
475	                        "actions": result["actions"],
476	                        "task_name": task_name,
477	                        "perturbation_config": {
478	                            "type": "spatial",
479	                            "config_idx": cfg_idx,
480	                            "delta_xy": cfg["delta_xy"],
481	                            "delta_half_len": cfg["delta_half_len"],
482	                            "delta_yaw": cfg["delta_yaw"],
483	                        },
484	                        "success": True,
485	                        "num_steps": result["num_steps"],
486	                    }
487	                    fname = f"{task_name}_spatial{cfg_idx}_ep{ep}.pkl"
488	                    fpath = os.path.join(output_dir, fname)
489	                    with open(fpath, "wb") as f:
490	                        pickle.dump(demo, f, protocol=pickle.HIGHEST_PROTOCOL)
491	                    stats["saved_files"].append(fpath)
492	
493	                rate = stats["success"] / stats["total"] * 100
494	                log.info(
495	                    "[spatial] task=%s cfg=%d ep=%d | %s | "
496	                    "cumulative %d/%d (%.1f%%)",
497	                    task_name, cfg_idx, ep,
498	                    "SUCCESS" if result["success"] else "FAIL",
499	                    stats["success"], stats["total"], rate,
500	                )
501	
502	    return stats
503	
504	
505	# ---------------------------------------------------------------------------
506	# Main
507	# ---------------------------------------------------------------------------
508	
509	def main():
510	    parser = argparse.ArgumentParser(
511	        description="Collect expert demos from π₀ in perturbed LIBERO environments"
512	    )
513	    parser.add_argument(
514	        "--perturbation_type", type=str, required=True,
515	        choices=["physical", "spatial"],
516	    )
517	    parser.add_argument("--gpu_id", type=int, default=0)
518	    parser.add_argument("--num_tasks", type=int, default=10)
519	    parser.add_argument("--episodes_per_config", type=int, default=3)
520	    parser.add_argument(
521	        "--output_dir", type=str, default=None,
522	        help="Override output directory (default: auto from perturbation_type)",
523	    )
524	    parser.add_argument(
525	        "--checkpoint", type=str,
526	        default="/root/autodl-tmp/checkpoints/pi0_base",
527	    )
528	    parser.add_argument("--dry_run", action="store_true")
529	    parser.add_argument("--seed", type=int, default=42)
530	    args = parser.parse_args()
531	
532	    logging.basicConfig(
533	        level=logging.INFO,
534	        format="%(asctime)s [%(levelname)s] %(message)s",
535	    )
536	
537	    random.seed(args.seed)
538	    np.random.seed(args.seed)
539	    torch.manual_seed(args.seed)
540	
541	    if args.output_dir is None:
542	        args.output_dir = (
543	            f"/root/meta_brain_lora_routing/data/expert_demos/{args.perturbation_type}"
544	        )
545	
546	    device = f"cuda:{args.gpu_id}"
547	    log.info(
548	        "Config: type=%s device=%s num_tasks=%d eps_per_cfg=%d dry_run=%s",
549	        args.perturbation_type, device, args.num_tasks,
550	        args.episodes_per_config, args.dry_run,
551	    )
552	
553	    log.info("Loading π₀ from %s", args.checkpoint)
554	    policy = load_pi0_policy(args.checkpoint, device)
555	
556	    from libero.libero import get_libero_path
557	    bddl_dir = os.path.join(get_libero_path("bddl_files"), BASE_TASK_SUITE)
558	    tasks = find_base_tasks(bddl_dir, num_tasks=args.num_tasks)
559	
560	    if not tasks:
561	        log.error("No base tasks found in %s", bddl_dir)
562	        sys.exit(1)
563	
564	    t0 = time.time()
565	
566	    if args.perturbation_type == "physical":
567	        stats = collect_physical(
568	            policy, tasks, args.episodes_per_config,
569	            args.output_dir, args.dry_run,
570	        )
571	    else:
572	        stats = collect_spatial(
573	            policy, tasks, args.episodes_per_config,
574	            args.output_dir, args.dry_run,
575	        )
576	
577	    elapsed = time.time() - t0
578	
579	    total_size = sum(
580	        os.path.getsize(f) for f in stats["saved_files"] if os.path.exists(f)
581	    )
582	    log.info("=" * 60)
583	    log.info("Collection complete: %s", args.perturbation_type)
584	    log.info("  Total episodes:  %d", stats["total"])
585	    log.info("  Successful:      %d", stats["success"])
586	    log.info(
587	        "  Success rate:    %.1f%%",
588	        stats["success"] / max(stats["total"], 1) * 100,
589	    )
590	    log.info("  Files saved:     %d", len(stats["saved_files"]))
591	    log.info("  Total size:      %.1f MB", total_size / 1024 / 1024)
592	    log.info("  Elapsed:         %.1f min", elapsed / 60)
593	    log.info("  Output dir:      %s", args.output_dir)
594	
595	
596	if __name__ == "__main__":
597	    main()
598	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013TqJ2cNFWJaMr9ra2qxnch",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "4b56c1d9-895f-4eb2-956f-dd0576e2c5fa"
}
```

</details>

---


### System

_source line 27_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3acedec04983e0ad",
  "tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "description": "Finding **/*.py",
  "usage": {
    "total_tokens": 15693,
    "tool_uses": 1,
    "duration_ms": 2251
  },
  "last_tool_name": "Glob",
  "uuid": "ef4aa0b7-f815-4632-83a5-868179e220be",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7"
}
```

---


### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Glob · `toolu_01GPp7Fg9F6bUridD4Gssaz6`</summary>

```json
{
  "pattern": "**/*.py",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "6a034c70-1f06-45a1-9935-a608ad5cfd9d",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0196pzsCn3sSvUZb1U3GdkCp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 570,
      "cache_read_input_tokens": 15114,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 570,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 29 · 2026-05-15T17:50:25.443Z_

<details><summary>↩ Tool result · `toolu_01GPp7Fg9F6bUridD4Gssaz6`</summary>

```text
artifacts/_project/intermediate/configs.py
artifacts/_project/intermediate/collect_activations.py
artifacts/_project/intermediate/train_classifier.py
artifacts/_project/intermediate/eval_classifier.py
artifacts/phase0/eval_classifier.py
artifacts/_project/intermediate/configs_5dd29d.py
artifacts/phase0/train_classifier.py
artifacts/phase0/configs.py
artifacts/phase0/collect_activations.py
artifacts/phase0/libero_integration.py
artifacts/phase1/configs.py
phase1/data_loader.py
artifacts/_project/intermediate/data_loader.py
artifacts/phase1/train_lora_expert.py
phase1/train_lora_expert.py
artifacts/_project/intermediate/train_lora_expert.py
artifacts/phase1/collect_expert_demos.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "78390622-d897-4916-b8cb-a3bc82d7545d"
}
```

</details>

---


### System

_source line 30_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3acedec04983e0ad",
  "tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "description": "Searching for _add|objects_layout|add_n|distractor|new_objects|…",
  "usage": {
    "total_tokens": 15696,
    "tool_uses": 2,
    "duration_ms": 2758
  },
  "last_tool_name": "Grep",
  "uuid": "cfef1889-442c-4663-83c8-c1dd898135f5",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7"
}
```

---


### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Grep · `toolu_01KtCziUtzvwhpakbaxz7Joj`</summary>

```json
{
  "pattern": "_add|objects_layout|add_n|distractor|new_objects|perturb_region",
  "type": "py",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "6239b7ae-5643-4fa0-a73a-4b4db85f4e49",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0196pzsCn3sSvUZb1U3GdkCp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 570,
      "cache_read_input_tokens": 15114,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 570,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 32 · 2026-05-15T17:50:25.922Z_

<details><summary>↩ Tool result · `toolu_01KtCziUtzvwhpakbaxz7Joj`</summary>

```text
Found 7 files
artifacts/phase1/collect_expert_demos.py
artifacts/_project/intermediate/data_loader.py
phase1/data_loader.py
artifacts/phase0/libero_integration.py
artifacts/phase0/configs.py
artifacts/_project/intermediate/configs_5dd29d.py
artifacts/_project/intermediate/configs.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "f4bf610d-4f3c-43f3-8a4b-ba1488510ae7"
}
```

</details>

---


### System

_source line 33_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3acedec04983e0ad",
  "tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "description": "Searching for LIBERO|libero",
  "usage": {
    "total_tokens": 15699,
    "tool_uses": 3,
    "duration_ms": 3085
  },
  "last_tool_name": "Grep",
  "uuid": "6c5cf61e-f76a-4da3-b4c9-994edbd897d5",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7"
}
```

---


### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Grep · `toolu_01HVQhsBe6kcauSRM3imYVmv`</summary>

```json
{
  "pattern": "LIBERO|libero",
  "type": "py",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "c8a58695-4b33-4e24-94fc-4749c4b0cb25",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0196pzsCn3sSvUZb1U3GdkCp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 570,
      "cache_read_input_tokens": 15114,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 570,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 35 · 2026-05-15T17:50:26.230Z_

<details><summary>↩ Tool result · `toolu_01HVQhsBe6kcauSRM3imYVmv`</summary>

```text
Found 10 files
artifacts/phase1/collect_expert_demos.py
artifacts/_project/intermediate/train_lora_expert.py
phase1/train_lora_expert.py
artifacts/phase1/train_lora_expert.py
artifacts/_project/intermediate/data_loader.py
phase1/data_loader.py
artifacts/phase1/configs.py
artifacts/phase0/libero_integration.py
artifacts/phase0/collect_activations.py
artifacts/_project/intermediate/collect_activations.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "76c6248e-cffd-46ce-a09b-dae9d9415ee8"
}
```

</details>

---


### System

_source line 36_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3acedec04983e0ad",
  "tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "description": "Reading artifacts/phase0/libero_integration.py",
  "usage": {
    "total_tokens": 17437,
    "tool_uses": 4,
    "duration_ms": 5381
  },
  "last_tool_name": "Read",
  "uuid": "4a48735a-c9c2-4d7e-91d5-e1d26d7790c7",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7"
}
```

---


### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Read · `toolu_016jZrMa7YjfHaHaEUC7448R`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "7766140a-82d9-45f9-944d-172c52ce0644",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011yFkL41cfnUXgwgau1AB4G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1732,
      "cache_read_input_tokens": 15684,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1732,
        "ephemeral_1h_input_tokens": 0
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

_source line 38 · 2026-05-15T17:50:28.519Z_

<details><summary>↩ Tool result · `toolu_016jZrMa7YjfHaHaEUC7448R`</summary>

```text
1	"""
2	OpenPI/LIBERO-Plus integration for pi0 activation collection.
3	
4	Bridges LIBERO-Plus simulation environments with the pi0 model, handling
5	observation preprocessing, action chunking, and perturbation-specific
6	task selection. Designed for direct model inference (no WebSocket server)
7	so that ActivationCollector hooks fire during forward passes.
8	
9	Input:
10	    LIBERO-Plus env observations: agentview_image [256,256,3],
11	    robot0_eye_in_hand_image [256,256,3], robot0_eef_pos [3],
12	    robot0_eef_quat [4], robot0_gripper_qpos [2], plus task language.
13	
14	Output:
15	    Per-episode activation dict (via ActivationCollector hooks on the
16	    underlying PI0Pytorch model) and task metadata.
17	
18	Integration with collect_activations.py:
19	    from libero_integration import load_pi0_for_collection, run_episode
20	
21	    policy, model = load_pi0_for_collection(checkpoint_path, device)
22	    collector = ActivationCollector(model)
23	    collector.register_hooks()
24	    result = run_episode(policy, collector, "camera_viewpoints", device)
25	"""
26	
27	import collections
28	import logging
29	import math
30	import re
31	import random
32	from pathlib import Path
33	from typing import Any
34	
35	import numpy as np
36	import torch
37	import torch.nn as nn
38	
39	log = logging.getLogger(__name__)
40	
41	# ---------------------------------------------------------------------------
42	# Constants (from OpenPI's examples/libero/main.py)
43	# ---------------------------------------------------------------------------
44	
45	LIBERO_DUMMY_ACTION = [0.0] * 6 + [-1.0]
46	LIBERO_ENV_RESOLUTION = 256
47	MODEL_INPUT_RESOLUTION = 224
48	DEFAULT_REPLAN_STEPS = 5
49	DEFAULT_NUM_STEPS_WAIT = 10
50	
51	MAX_STEPS = {
52	    "libero_spatial": 220,
53	    "libero_object": 280,
54	    "libero_goal": 300,
55	    "libero_10": 520,
56	    "libero_90": 400,
57	}
58	
59	VALID_PERTURBATION_TYPES = [
60	    "camera_viewpoints",
61	    "light_conditions",
62	    "background_textures",
63	    "objects_layout",
64	    "robot_initial_states",
65	    "sensor_noise",
66	]
67	
68	
69	# ---------------------------------------------------------------------------
70	# Geometry helpers
71	# ---------------------------------------------------------------------------
72	
73	def _quat2axisangle(quat: np.ndarray) -> np.ndarray:
74	    """Quaternion [x,y,z,w] -> axis-angle [ax,ay,az]."""
75	    q = np.asarray(quat, dtype=np.float64)
76	    norm = np.linalg.norm(q)
77	    if norm < 1e-8:
78	        return np.zeros(3, dtype=np.float32)
79	    q /= norm
80	    sin_half = np.linalg.norm(q[:3])
81	    if sin_half < 1e-8:
82	        return np.zeros(3, dtype=np.float32)
83	    angle = 2.0 * math.atan2(sin_half, q[3])
84	    axis = q[:3] / sin_half
85	    return (axis * angle).astype(np.float32)
86	
87	
88	# ---------------------------------------------------------------------------
89	# Image preprocessing
90	# ---------------------------------------------------------------------------
91	
92	def _resize_with_pad(img: np.ndarray, size: int) -> np.ndarray:
93	    """Resize image with aspect-preserving padding to (size, size, 3) uint8."""
94	    try:
95	        from openpi_client.image_tools import resize_with_pad, convert_to_uint8
96	        return convert_to_uint8(resize_with_pad(img, size, size))
97	    except ImportError:
98	        from PIL import Image as PILImage
99	        h, w = img.shape[:2]
100	        scale = min(size / h, size / w)
101	        new_h, new_w = int(h * scale), int(w * scale)
102	        resized = np.array(
103	            PILImage.fromarray(img).resize((new_w, new_h), PILImage.BILINEAR)
104	        )
105	        canvas = np.zeros((size, size, 3), dtype=np.uint8)
106	        y0, x0 = (size - new_h) // 2, (size - new_w) // 2
107	        canvas[y0 : y0 + new_h, x0 : x0 + new_w] = resized
108	        return canvas
109	
110	
111	# ---------------------------------------------------------------------------
112	# Observation -> model input
113	# ---------------------------------------------------------------------------
114	
115	def obs_to_model_input(
116	    obs: dict,
117	    task_description: str,
118	    resize_size: int = MODEL_INPUT_RESOLUTION,
119	) -> dict:
120	    """Convert LIBERO observation to the dict format expected by policy.infer().
121	
122	    LIBERO obs keys used:
123	        agentview_image          [H, W, 3] uint8
124	        robot0_eye_in_hand_image [H, W, 3] uint8
125	        robot0_eef_pos           [3] float
126	        robot0_eef_quat          [4] float (x,y,z,w)
127	        robot0_gripper_qpos      [2] float
128	
129	    Returns dict with keys:
130	        observation/image        [224, 224, 3] uint8
131	        observation/wrist_image  [224, 224, 3] uint8
132	        observation/state        [8] float32
133	        prompt                   str
134	
135	    Note: sensor noise is applied by the LIBERO-Plus environment itself
136	    (motion_blur, gaussian_blur, zoom_blur, fog, glass_blur at various
137	    severity levels), not at the observation preprocessing stage.
138	    """
139	    # Flip images 180 degrees (OpenPI training convention)
140	    base_img = np.ascontiguousarray(obs["agentview_image"][::-1, ::-1])
141	    wrist_img = np.ascontiguousarray(obs["robot0_eye_in_hand_image"][::-1, ::-1])
142	
143	    base_img = _resize_with_pad(base_img, resize_size)
144	    wrist_img = _resize_with_pad(wrist_img, resize_size)
145	
146	    state = np.concatenate([
147	        obs["robot0_eef_pos"].astype(np.float32),
148	        _quat2axisangle(obs["robot0_eef_quat"]),
149	        obs["robot0_gripper_qpos"].astype(np.float32),
150	    ])  # [8]
151	
152	    return {
153	        "observation/image": base_img,
154	        "observation/wrist_image": wrist_img,
155	        "observation/state": state,
156	        "prompt": task_description,
157	    }
158	
159	
160	# ---------------------------------------------------------------------------
161	# Model loading
162	# ---------------------------------------------------------------------------
163	
164	def _extract_model(policy: object) -> nn.Module:
165	    """Extract the underlying PI0Pytorch nn.Module from an OpenPI Policy."""
166	    for attr in ("_model", "model", "_network", "network"):
167	        candidate = getattr(policy, attr, None)
168	        if isinstance(candidate, nn.Module):
169	            return candidate
170	
171	    for attr in dir(policy):
172	        if attr.startswith("__"):
173	            continue
174	        try:
175	            candidate = getattr(policy, attr)
176	            if isinstance(candidate, nn.Module):
177	                log.warning(
178	                    "Found model at policy.%s (unexpected attribute name)", attr
179	                )
180	                return candidate
181	        except Exception:
182	            continue
183	
184	    raise AttributeError(
185	        "Cannot find nn.Module in Policy object. "
186	        "Inspect the OpenPI Policy class and update _extract_model()."
187	    )
188	
189	
190	def _ensure_openpi_imports():
191	    """Stub out lerobot (training-only dep) before importing OpenPI inference code."""
192	    import sys
193	    import types
194	    for mod in [
195	        "lerobot", "lerobot.common", "lerobot.common.datasets",
196	        "lerobot.common.datasets.lerobot_dataset",
197	    ]:
198	        if mod not in sys.modules:
199	            sys.modules[mod] = types.ModuleType(mod)
200	
201	
202	def load_pi0_for_collection(
203	    checkpoint_path: str,
204	    device: str,
205	    config_name: str = "pi0_libero",
206	) -> tuple[object, nn.Module]:
207	    """Load pi0 via OpenPI's policy system for activation collection.
208	
209	    Uses create_trained_policy() so all transforms (LiberoInputs, Normalize,
210	    TokenizePrompt, PadStatesAndActions, ResizeImages) and normalization
211	    statistics are applied correctly.
212	
213	    Returns:
214	        (policy, model) where
215	        - policy: OpenPI Policy; call policy.infer(obs_dict)
216	        - model:  PI0Pytorch nn.Module; pass to ActivationCollector
217	    """
218	    _ensure_openpi_imports()
219	
220	    try:
221	        from openpi.training import config as _config
222	        from openpi.policies import policy_config
223	    except ImportError:
224	        raise ImportError(
225	            "openpi package required. "
226	            "Clone https://github.com/Physical-Intelligence/openpi "
227	            "and install with: pip install -e ."
228	        )
229	
230	    train_config = _config.get_config(config_name)
231	    policy = policy_config.create_trained_policy(
232	        train_config, checkpoint_path, pytorch_device=device
233	    )
234	
235	    model = _extract_model(policy)
236	    log.info("Loaded pi0 policy (config=%s) on %s", config_name, device)
237	    return policy, model
238	
239	
240	# ---------------------------------------------------------------------------
241	# LIBERO-Plus environment
242	# ---------------------------------------------------------------------------
243	
244	def _classify_task(task_name: str) -> str | None:
245	    """Classify a LIBERO-Plus task name into its perturbation type.
246	
247	    LIBERO-Plus task naming conventions:
248	      Compound: {base}_[language_N_]view_{H}_{V}_{S}_{R}_{E}_initstate_{I}[_noise_{N}]
249	        - camera_viewpoints:    (H,V,S,R,E) != (0,0,100,0,0), I==0, no noise
250	        - robot_initial_states: default view, I != 0, no noise
251	        - sensor_noise:         default view, I==0, N > 0
252	        - base (nominal):       all defaults
253	      Simple suffixes:
254	        - light_conditions:     _light_\\d+
255	        - background_textures:  _table_\\d+ or _tb_\\d+
256	        - objects_layout:       _add_\\d+ or _level\\d+
257	
258	    Returns perturbation type string, or None for base/nominal tasks.
259	    """
260	    if "_view_" in task_name:
261	        m = re.search(
262	            r"_view_(-?\d+)_(-?\d+)_(\d+)_(-?\d+)_(-?\d+)_initstate_(\d+)(?:_noise_(\d+))?",
263	            task_name,
264	        )
265	        if not m:
266	            return None
267	        H, V, S, R, E = int(m[1]), int(m[2]), int(m[3]), int(m[4]), int(m[5])
268	        initstate = int(m[6])
269	        noise = int(m[7]) if m[7] else 0
270	
271	        if noise > 0:
272	            return "sensor_noise"
273	        if (H, V, S, R, E) != (0, 0, 100, 0, 0):
274	            return "camera_viewpoints"
275	        if initstate != 0:
276	            return "robot_initial_states"
277	        return None
278	
279	    if re.search(r"_light_\d+$", task_name):
280	        return "light_conditions"
281	    if re.search(r"_(?:table|tb)_\d+$", task_name):
282	        return "background_textures"
283	    if re.search(r"_add_\d+$", task_name) or re.search(r"_level\d+", task_name):
284	        return "objects_layout"
285	
286	    return None
287	
288	
289	def _get_task_indices(
290	    suite: object,
291	    perturbation_type: str | None,
292	    num_tasks: int,
293	) -> list[int]:
294	    """Return task indices matching the requested perturbation type."""
295	    if perturbation_type is not None and perturbation_type not in VALID_PERTURBATION_TYPES:
296	        raise ValueError(
297	            f"Unknown perturbation_type={perturbation_type!r}. "
298	            f"Valid: {VALID_PERTURBATION_TYPES}"
299	        )
300	
301	    indices = []
302	    matched_names = []
303	    for i in range(num_tasks):
304	        task = suite.get_task(i)
305	        name = getattr(task, "name", "") or getattr(task, "bddl_file", "")
306	        classified = _classify_task(name)
307	
308	        if perturbation_type is None:
309	            if classified is None:
310	                indices.append(i)
311	                matched_names.append(name)
312	        elif classified == perturbation_type:
313	            indices.append(i)
314	            matched_names.append(name)
315	
316	    if not indices:
317	        raise RuntimeError(
318	            f"No tasks match perturbation_type={perturbation_type!r} "
319	            f"among {num_tasks} tasks. Verify the suite contains "
320	            f"LIBERO-Plus perturbation variants (not base libero_90)."
321	        )
322	
323	    log.info(
324	        "%s: matched %d/%d tasks (e.g. %s)",
325	        perturbation_type or "nominal",
326	        len(indices),
327	        num_tasks,
328	        matched_names[:3],
329	    )
330	    return indices
331	
332	
333	def create_libero_env(
334	    task_suite_name: str = "libero_spatial",
335	    perturbation_type: str | None = None,
336	    task_idx: int | None = None,
337	    seed: int = 42,
338	) -> tuple[Any, str, np.ndarray, int]:
339	    """Create a LIBERO / LIBERO-Plus evaluation environment.
340	
341	    Returns:
342	        (env, task_description, init_states, selected_task_idx)
343	    """
344	    from libero.libero import benchmark, get_libero_path
345	    from libero.libero.envs import OffScreenRenderEnv
346	
347	    benchmark_dict = benchmark.get_benchmark_dict()
348	    suite = benchmark_dict[task_suite_name]()
349	    num_tasks = suite.n_tasks
350	
351	    valid_indices = _get_task_indices(suite, perturbation_type, num_tasks)
352	
353	    if task_idx is not None and task_idx in valid_indices:
354	        selected_idx = task_idx
355	    else:
356	        selected_idx = random.choice(valid_indices)
357	
358	    task = suite.get_task(selected_idx)
359	    task_description = task.language
360	
361	    task_bddl_file = (
362	        Path(get_libero_path("bddl_files")) / task.problem_folder / task.bddl_file
363	    )
364	    env = OffScreenRenderEnv(
365	        bddl_file_name=str(task_bddl_file),
366	        camera_heights=LIBERO_ENV_RESOLUTION,
367	        camera_widths=LIBERO_ENV_RESOLUTION,
368	    )
369	    env.seed(seed)
370	
371	    init_states = suite.get_task_init_states(selected_idx)
372	    return env, task_description, init_states, selected_idx
373	
374	
375	# ---------------------------------------------------------------------------
376	# Episode rollout
377	# ---------------------------------------------------------------------------
378	
379	def run_episode(
380	    policy: object,
381	    collector: object,
382	    perturbation_type: str | None,
383	    device: str,
384	    task_suite: str = "libero_spatial",
385	    seed: int = 42,
386	    replan_steps: int = DEFAULT_REPLAN_STEPS,
387	    num_steps_wait: int = DEFAULT_NUM_STEPS_WAIT,
388	) -> dict[str, Any]:
389	    """Run one LIBERO-Plus episode, collecting activations at each replan point.
390	
391	    Every replan_steps env steps, the policy is queried for a new action chunk.
392	    ActivationCollector hooks capture layer outputs during each policy.infer()
393	    call. Activations are averaged across all replan points.
394	
395	    Sensor noise is applied by the LIBERO-Plus environment itself (via task
396	    name suffix _noise_N), not at the observation level.
397	
398	    Returns dict with keys: activations, task_name, task_description,
399	    num_steps, success.
400	    """
401	    env, task_description, init_states, task_idx = create_libero_env(
402	        task_suite_name=task_suite,
403	        perturbation_type=perturbation_type,
404	        seed=seed,
405	    )
406	
407	    max_steps = MAX_STEPS.get(task_suite, 400)
408	
409	    step = 0
410	    success = False
411	
412	    try:
413	        trial_idx = random.randint(0, len(init_states) - 1)
414	        obs = env.set_init_state(init_states[trial_idx])
415	
416	        for _ in range(num_steps_wait):
417	            obs, _, _, _ = env.step(LIBERO_DUMMY_ACTION)
418	
419	        action_plan: collections.deque = collections.deque()
420	        step_activations: list[dict] = []
421	        done = False
422	
423	        while not done and step < max_steps:
424	            if len(action_plan) == 0:
425	                collector.clear()
426	
427	                obs_dict = obs_to_model_input(obs, task_description)
428	                result = policy.infer(obs_dict)
429	                action_chunk = result["actions"]  # [horizon, 7]
430	                action_plan.extend(action_chunk[:replan_steps])
431	
432	                pooled = collector.get_pooled()
433	                if pooled:
434	                    step_activations.append(pooled)
435	
436	            action = action_plan.popleft()
437	            if isinstance(action, torch.Tensor):
438	                action = action.cpu().numpy()
439	            obs, reward, done, info = env.step(
440	                action.tolist() if hasattr(action, "tolist") else list(action)
441	            )
442	            step += 1
443	
444	            if done or reward > 0:
445	                success = info.get("success", reward > 0)
446	    finally:
447	        env.close()
448	
449	    return {
450	        "activations": _average_activations(step_activations),
451	        "task_name": f"{task_suite}/task_{task_idx}",
452	        "task_description": task_description,
453	        "num_steps": step,
454	        "success": success,
455	    }
456	
457	
458	def _average_activations(
459	    step_activations: list[dict[str, dict[str, torch.Tensor]]],
460	) -> dict[str, dict[str, torch.Tensor]]:
461	    """Average activation tensors across replan steps."""
462	    if not step_activations:
463	        return {}
464	    result: dict[str, dict[str, torch.Tensor]] = {}
465	    for layer in step_activations[0]:
466	        result[layer] = {}
467	        for strat in step_activations[0][layer]:
468	            tensors = [sa[layer][strat] for sa in step_activations]
469	            result[layer][strat] = torch.stack(tensors).mean(dim=0)
470	    return result
471	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "206fa41e-55ac-422c-a2ad-0ea46e4dbd2d"
}
```

</details>

---


### System

_source line 39_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3acedec04983e0ad",
  "tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "description": "Reading artifacts/phase1/collect_expert_demos.py",
  "usage": {
    "total_tokens": 17438,
    "tool_uses": 5,
    "duration_ms": 5591
  },
  "last_tool_name": "Read",
  "uuid": "8c4ddf6e-70ce-4463-bbac-1d0a8beb0e9a",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7"
}
```

---


### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Read · `toolu_01HjeyTQgVNfDAuAq6NTujFg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "25514ba1-293f-43fe-9393-880693d5bfe5",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011yFkL41cfnUXgwgau1AB4G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1732,
      "cache_read_input_tokens": 15684,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1732,
        "ephemeral_1h_input_tokens": 0
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

_source line 41 · 2026-05-15T17:50:28.725Z_

<details><summary>↩ Tool result · `toolu_01HjeyTQgVNfDAuAq6NTujFg`</summary>

```text
1	"""
2	Collect expert demonstrations by rolling out frozen π₀ in perturbed LIBERO environments.
3	
4	Only successful episodes are saved. Two perturbation types are supported:
5	  - physical: vary robot initial state (init_states index 1-49)
6	  - spatial:  perturb object layout via BDDL region_info modifications
7	
8	Output: pickle files with (observations, actions, metadata) per episode.
9	
10	Usage:
11	    # Physical perturbation dry-run
12	    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \
13	        --perturbation_type physical --dry_run
14	
15	    # Spatial perturbation dry-run
16	    CUDA_VISIBLE_DEVICES=2 python collect_expert_demos.py \
17	        --perturbation_type spatial --dry_run
18	
19	    # Full physical collection
20	    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \
21	        --perturbation_type physical
22	"""
23	
24	import argparse
25	import collections
26	import copy
27	import logging
28	import math
29	import os
30	import pickle
31	import random
32	import re
33	import sys
34	import time
35	import types
36	from pathlib import Path
37	from typing import Any
38	
39	import numpy as np
40	import torch
41	
42	log = logging.getLogger(__name__)
43	
44	# ---------------------------------------------------------------------------
45	# Constants
46	# ---------------------------------------------------------------------------
47	
48	LIBERO_DUMMY_ACTION = [0.0] * 6 + [-1.0]
49	LIBERO_ENV_RESOLUTION = 256
50	MODEL_INPUT_RESOLUTION = 224
51	REPLAN_STEPS = 5
52	NUM_STEPS_WAIT = 10
53	MAX_STEPS = 220  # libero_spatial default
54	
55	# 10 base tasks in libero_spatial (no perturbation suffix)
56	BASE_TASK_SUITE = "libero_spatial"
57	
58	# Spatial perturbation grid: 10 configurations with varying XY shifts and yaw
59	# Magnitudes chosen to be noticeable but within feasible reach of the robot.
60	SPATIAL_PERTURBATION_CONFIGS = [
61	    {"delta_xy": ( 0.05,  0.00), "delta_half_len": 0.0,  "delta_yaw": (0.0, 0.0)},
62	    {"delta_xy": (-0.05,  0.00), "delta_half_len": 0.0,  "delta_yaw": (0.0, 0.0)},
63	    {"delta_xy": ( 0.00,  0.05), "delta_half_len": 0.0,  "delta_yaw": (0.0, 0.0)},
64	    {"delta_xy": ( 0.00, -0.05), "delta_half_len": 0.0,  "delta_yaw": (0.0, 0.0)},
65	    {"delta_xy": ( 0.03,  0.03), "delta_half_len": 0.0,  "delta_yaw": (0.0, 0.0)},
66	    {"delta_xy": (-0.03, -0.03), "delta_half_len": 0.0,  "delta_yaw": (0.0, 0.0)},
67	    {"delta_xy": ( 0.04,  0.00), "delta_half_len": 0.01, "delta_yaw": (0.3, 0.0)},
68	    {"delta_xy": (-0.04,  0.00), "delta_half_len": 0.01, "delta_yaw": (-0.3, 0.0)},
69	    {"delta_xy": ( 0.00,  0.04), "delta_half_len": 0.0,  "delta_yaw": (0.0, 0.3)},
70	    {"delta_xy": ( 0.00, -0.04), "delta_half_len": 0.0,  "delta_yaw": (0.0, -0.3)},
71	]
72	
73	
74	# ---------------------------------------------------------------------------
75	# Geometry / image helpers (from libero_integration.py)
76	# ---------------------------------------------------------------------------
77	
78	def _quat2axisangle(quat: np.ndarray) -> np.ndarray:
79	    """Quaternion [x,y,z,w] -> axis-angle [ax,ay,az]."""
80	    q = np.asarray(quat, dtype=np.float64)
81	    norm = np.linalg.norm(q)
82	    if norm < 1e-8:
83	        return np.zeros(3, dtype=np.float32)
84	    q /= norm
85	    sin_half = np.linalg.norm(q[:3])
86	    if sin_half < 1e-8:
87	        return np.zeros(3, dtype=np.float32)
88	    angle = 2.0 * math.atan2(sin_half, q[3])
89	    axis = q[:3] / sin_half
90	    return (axis * angle).astype(np.float32)
91	
92	
93	def _resize_with_pad(img: np.ndarray, size: int) -> np.ndarray:
94	    """Resize image with aspect-preserving padding to (size, size, 3) uint8."""
95	    try:
96	        from openpi_client.image_tools import resize_with_pad, convert_to_uint8
97	        return convert_to_uint8(resize_with_pad(img, size, size))
98	    except ImportError:
99	        from PIL import Image as PILImage
100	        h, w = img.shape[:2]
101	        scale = min(size / h, size / w)
102	        new_h, new_w = int(h * scale), int(w * scale)
103	        resized = np.array(
104	            PILImage.fromarray(img).resize((new_w, new_h), PILImage.BILINEAR)
105	        )
106	        canvas = np.zeros((size, size, 3), dtype=np.uint8)
107	        y0, x0 = (size - new_h) // 2, (size - new_w) // 2
108	        canvas[y0 : y0 + new_h, x0 : x0 + new_w] = resized
109	        return canvas
110	
111	
112	def obs_to_model_input(obs: dict, task_description: str) -> dict:
113	    """Convert LIBERO observation to the dict format expected by policy.infer()."""
114	    base_img = np.ascontiguousarray(obs["agentview_image"][::-1, ::-1])
115	    wrist_img = np.ascontiguousarray(obs["robot0_eye_in_hand_image"][::-1, ::-1])
116	
117	    base_img = _resize_with_pad(base_img, MODEL_INPUT_RESOLUTION)
118	    wrist_img = _resize_with_pad(wrist_img, MODEL_INPUT_RESOLUTION)
119	
120	    state = np.concatenate([
121	        obs["robot0_eef_pos"].astype(np.float32),
122	        _quat2axisangle(obs["robot0_eef_quat"]),
123	        obs["robot0_gripper_qpos"].astype(np.float32),
124	    ])
125	
126	    return {
127	        "observation/image": base_img,
128	        "observation/wrist_image": wrist_img,
129	        "observation/state": state,
130	        "prompt": task_description,
131	    }
132	
133	
134	def extract_obs_for_saving(obs: dict) -> dict:
135	    """Extract observation fields to save in demo data (images stored as uint8)."""
136	    return {
137	        "agentview_image": obs["agentview_image"].copy(),
138	        "robot0_eye_in_hand_image": obs["robot0_eye_in_hand_image"].copy(),
139	        "robot0_eef_pos": obs["robot0_eef_pos"].astype(np.float32).copy(),
140	        "robot0_eef_quat": obs["robot0_eef_quat"].astype(np.float32).copy(),
141	        "robot0_gripper_qpos": obs["robot0_gripper_qpos"].astype(np.float32).copy(),
142	    }
143	
144	
145	# ---------------------------------------------------------------------------
146	# Model loading
147	# ---------------------------------------------------------------------------
148	
149	def _ensure_openpi_imports():
150	    """Stub out lerobot (training-only dep) before importing OpenPI."""
151	    for mod in [
152	        "lerobot", "lerobot.common", "lerobot.common.datasets",
153	        "lerobot.common.datasets.lerobot_dataset",
154	    ]:
155	        if mod not in sys.modules:
156	            sys.modules[mod] = types.ModuleType(mod)
157	
158	
159	def load_pi0_policy(checkpoint_path: str, device: str) -> object:
160	    """Load pi0 policy via OpenPI. Returns the Policy object for inference."""
161	    _ensure_openpi_imports()
162	    from openpi.training import config as _config
163	    from openpi.policies import policy_config
164	
165	    train_config = _config.get_config("pi0_libero")
166	    policy = policy_config.create_trained_policy(
167	        train_config, checkpoint_path, pytorch_device=device
168	    )
169	    log.info("Loaded pi0 policy on %s", device)
170	    return policy
171	
172	
173	# ---------------------------------------------------------------------------
174	# Task discovery
175	# ---------------------------------------------------------------------------
176	
177	def find_base_tasks(bddl_dir: str, num_tasks: int = 10) -> list[dict]:
178	    """Find base (unperturbed) BDDL files in libero_spatial.
179	
180	    Returns list of dicts with keys: name, bddl_path, init_states_path.
181	    """
182	    all_files = [f for f in os.listdir(bddl_dir) if f.endswith(".bddl")]
183	
184	    base_names = []
185	    for f in sorted(all_files):
186	        name = f.replace(".bddl", "")
187	        # Skip any file with perturbation suffixes
188	        if re.search(
189	            r"(_add_\d+|_table_\d+|_tb_\d+|_light_\d+|_language_\d+"
190	            r"|_view_|_noise_|_level\d+| copy)",
191	            name,
192	        ):
193	            continue
194	        base_names.append(name)
195	
196	    init_dir = bddl_dir.replace("bddl_files", "init_files")
197	    tasks = []
198	    for name in base_names[:num_tasks]:
199	        bddl_path = os.path.join(bddl_dir, f"{name}.bddl")
200	        init_path = os.path.join(init_dir, f"{name}.pruned_init")
201	        if not os.path.exists(init_path):
202	            log.warning("init_states not found for %s, skipping", name)
203	            continue
204	        tasks.append({
205	            "name": name,
206	            "bddl_path": bddl_path,
207	            "init_states_path": init_path,
208	        })
209	
210	    log.info("Found %d base tasks", len(tasks))
211	    return tasks
212	
213	
214	def get_task_language(bddl_path: str) -> str:
215	    """Extract language instruction from a BDDL file."""
216	    from libero.libero.envs.bddl_utils import get_problem_info
217	    info = get_problem_info(bddl_path)
218	    return info["language_instruction"]
219	
220	
221	# ---------------------------------------------------------------------------
222	# Environment creation
223	# ---------------------------------------------------------------------------
224	
225	def create_env(bddl_path: str) -> object:
226	    """Create a LIBERO OffScreenRenderEnv from a BDDL file."""
227	    from libero.libero.envs import OffScreenRenderEnv
228	    env = OffScreenRenderEnv(
229	        bddl_file_name=bddl_path,
230	        camera_heights=LIBERO_ENV_RESOLUTION,
231	        camera_widths=LIBERO_ENV_RESOLUTION,
232	    )
233	    return env
234	
235	
236	def create_spatial_bddl(
237	    base_bddl_path: str,
238	    perturbation_config: dict,
239	    output_dir: str,
240	) -> str:
241	    """Create a perturbed BDDL file by applying spatial perturbation to all regions.
242	
243	    Returns the path to the new BDDL file.
244	    """
245	    sys.path.insert(0, "/root/LIBERO-plus/libero")
246	    from libero.randomizer.bddl_operators import (
247	        load_bddl_file,
248	        save_bddl_file,
249	        perturb_region_info,
250	    )
251	
252	    spec = load_bddl_file(base_bddl_path)
253	    delta_xy = perturbation_config["delta_xy"]
254	    delta_half = perturbation_config["delta_half_len"]
255	    delta_yaw = perturbation_config["delta_yaw"]
256	
257	    for i in range(len(spec.region_infos)):
258	        spec.region_infos[i] = perturb_region_info(
259	            spec.region_infos[i],
260	            delta_region_centroid_xy=delta_xy,
261	            delta_region_half_len=delta_half,
262	            delta_yaw_rotation=delta_yaw,
263	        )
264	
265	    os.makedirs(output_dir, exist_ok=True)
266	    base_name = Path(base_bddl_path).stem
267	    dx, dy = delta_xy
268	    filename = f"{base_name}_spatial_dx{dx:.2f}_dy{dy:.2f}.bddl"
269	    _, filepath = save_bddl_file(spec, bddl_filename=filename, bddl_dirpath=output_dir)
270	    return filepath
271	
272	
273	# ---------------------------------------------------------------------------
274	# Episode rollout
275	# ---------------------------------------------------------------------------
276	
277	def rollout_episode(
278	    policy: object,
279	    env: object,
280	    task_description: str,
281	    init_states: np.ndarray,
282	    init_state_idx: int,
283	    seed: int,
284	) -> dict[str, Any]:
285	    """Run one episode, collecting (obs, action) pairs.
286	
287	    Returns dict with observations, actions, success, num_steps.
288	    """
289	    env.seed(seed)
290	    obs = env.set_init_state(init_states[init_state_idx])
291	
292	    for _ in range(NUM_STEPS_WAIT):
293	        obs, _, _, _ = env.step(LIBERO_DUMMY_ACTION)
294	
295	    all_obs = [extract_obs_for_saving(obs)]
296	    all_actions = []
297	    action_plan = collections.deque()
298	    step = 0
299	    success = False
300	    done = False
301	
302	    while not done and step < MAX_STEPS:
303	        if len(action_plan) == 0:
304	            obs_dict = obs_to_model_input(obs, task_description)
305	            result = policy.infer(obs_dict)
306	            action_chunk = result["actions"]
307	            action_plan.extend(action_chunk[:REPLAN_STEPS])
308	
309	        action = action_plan.popleft()
310	        if isinstance(action, torch.Tensor):
311	            action = action.cpu().numpy()
312	        action_np = np.asarray(action, dtype=np.float32)
313	
314	        obs, reward, done, info = env.step(
315	            action_np.tolist() if hasattr(action_np, "tolist") else list(action_np)
316	        )
317	        step += 1
318	
319	        all_obs.append(extract_obs_for_saving(obs))
320	        all_actions.append(action_np)
321	
322	        if done or reward > 0:
323	            success = info.get("success", reward > 0)
324	
325	    return {
326	        "observations": all_obs,
327	        "actions": np.stack(all_actions) if all_actions else np.zeros((0, 7)),
328	        "success": success,
329	        "num_steps": step,
330	    }
331	
332	
333	# ---------------------------------------------------------------------------
334	# Collection loops
335	# ---------------------------------------------------------------------------
336	
337	def collect_physical(
338	    policy: object,
339	    tasks: list[dict],
340	    episodes_per_config: int,
341	    output_dir: str,
342	    dry_run: bool,
343	) -> dict:
344	    """Collect expert demos with physical (robot initial state) perturbation.
345	
346	    Uses init_states indices 1-49 (index 0 is nominal).
347	    """
348	    os.makedirs(output_dir, exist_ok=True)
349	    stats = {"total": 0, "success": 0, "saved_files": []}
350	
351	    init_state_indices = list(range(1, 50))  # 49 perturbed states
352	    if dry_run:
353	        tasks = tasks[:1]
354	        init_state_indices = [1]
355	        episodes_per_config = 1
356	
357	    for task_info in tasks:
358	        task_name = task_info["name"]
359	        init_states = torch.load(task_info["init_states_path"], weights_only=False)
360	        language = get_task_language(task_info["bddl_path"])
361	        log.info("Task: %s (%d init_states available)", task_name, len(init_states))
362	
363	        for idx in init_state_indices:
364	            if idx >= len(init_states):
365	                continue
366	
367	            for ep in range(episodes_per_config):
368	                seed = hash((task_name, idx, ep)) % (2**31)
369	                stats["total"] += 1
370	
371	                try:
372	                    env = create_env(task_info["bddl_path"])
373	                    result = rollout_episode(
374	                        policy, env, language, init_states, idx, seed
375	                    )
376	                    env.close()
377	                except Exception:
378	                    log.exception(
379	                        "Episode failed: task=%s idx=%d ep=%d", task_name, idx, ep
380	                    )
381	                    continue
382	
383	                if result["success"]:
384	                    stats["success"] += 1
385	                    demo = {
386	                        "observations": result["observations"],
387	                        "actions": result["actions"],
388	                        "task_name": task_name,
389	                        "perturbation_config": {
390	                            "type": "physical",
391	                            "init_state_idx": idx,
392	                        },
393	                        "success": True,
394	                        "num_steps": result["num_steps"],
395	                    }
396	                    fname = f"{task_name}_initstate{idx}_ep{ep}.pkl"
397	                    fpath = os.path.join(output_dir, fname)
398	                    with open(fpath, "wb") as f:
399	                        pickle.dump(demo, f, protocol=pickle.HIGHEST_PROTOCOL)
400	                    stats["saved_files"].append(fpath)
401	
402	                rate = stats["success"] / stats["total"] * 100
403	                log.info(
404	                    "[physical] task=%s idx=%d ep=%d | %s | "
405	                    "cumulative %d/%d (%.1f%%)",
406	                    task_name, idx, ep,
407	                    "SUCCESS" if result["success"] else "FAIL",
408	                    stats["success"], stats["total"], rate,
409	                )
410	
411	    return stats
412	
413	
414	def collect_spatial(
415	    policy: object,
416	    tasks: list[dict],
417	    episodes_per_config: int,
418	    output_dir: str,
419	    dry_run: bool,
420	) -> dict:
421	    """Collect expert demos with spatial (objects layout) perturbation.
422	
423	    Applies 10 predefined spatial perturbation configs to each base task.
424	    """
425	    os.makedirs(output_dir, exist_ok=True)
426	    tmp_bddl_dir = os.path.join(output_dir, "_tmp_bddl")
427	    os.makedirs(tmp_bddl_dir, exist_ok=True)
428	    stats = {"total": 0, "success": 0, "saved_files": []}
429	
430	    configs = SPATIAL_PERTURBATION_CONFIGS
431	    if dry_run:
432	        tasks = tasks[:1]
433	        configs = configs[:1]
434	        episodes_per_config = 1
435	
436	    for task_info in tasks:
437	        task_name = task_info["name"]
438	        init_states = torch.load(task_info["init_states_path"], weights_only=False)
439	        log.info("Task: %s", task_name)
440	
441	        for cfg_idx, cfg in enumerate(configs):
442	            try:
443	                perturbed_bddl = create_spatial_bddl(
444	                    task_info["bddl_path"], cfg, tmp_bddl_dir
445	                )
446	                language = get_task_language(perturbed_bddl)
447	            except Exception:
448	                log.exception(
449	                    "BDDL perturbation failed: task=%s cfg=%d", task_name, cfg_idx
450	                )
451	                continue
452	
453	            for ep in range(episodes_per_config):
454	                seed = hash((task_name, cfg_idx, ep)) % (2**31)
455	                stats["total"] += 1
456	
457	                try:
458	                    env = create_env(perturbed_bddl)
459	                    # Use nominal init_state (index 0) for spatial perturbation
460	                    result = rollout_episode(
461	                        policy, env, language, init_states, 0, seed
462	                    )
463	                    env.close()
464	                except Exception:
465	                    log.exception(
466	                        "Episode failed: task=%s cfg=%d ep=%d",
467	                        task_name, cfg_idx, ep,
468	                    )
469	                    continue
470	
471	                if result["success"]:
472	                    stats["success"] += 1
473	                    demo = {
474	                        "observations": result["observations"],
475	                        "actions": result["actions"],
476	                        "task_name": task_name,
477	                        "perturbation_config": {
478	                            "type": "spatial",
479	                            "config_idx": cfg_idx,
480	                            "delta_xy": cfg["delta_xy"],
481	                            "delta_half_len": cfg["delta_half_len"],
482	                            "delta_yaw": cfg["delta_yaw"],
483	                        },
484	                        "success": True,
485	                        "num_steps": result["num_steps"],
486	                    }
487	                    fname = f"{task_name}_spatial{cfg_idx}_ep{ep}.pkl"
488	                    fpath = os.path.join(output_dir, fname)
489	                    with open(fpath, "wb") as f:
490	                        pickle.dump(demo, f, protocol=pickle.HIGHEST_PROTOCOL)
491	                    stats["saved_files"].append(fpath)
492	
493	                rate = stats["success"] / stats["total"] * 100
494	                log.info(
495	                    "[spatial] task=%s cfg=%d ep=%d | %s | "
496	                    "cumulative %d/%d (%.1f%%)",
497	                    task_name, cfg_idx, ep,
498	                    "SUCCESS" if result["success"] else "FAIL",
499	                    stats["success"], stats["total"], rate,
500	                )
501	
502	    return stats
503	
504	
505	# ---------------------------------------------------------------------------
506	# Main
507	# ---------------------------------------------------------------------------
508	
509	def main():
510	    parser = argparse.ArgumentParser(
511	        description="Collect expert demos from π₀ in perturbed LIBERO environments"
512	    )
513	    parser.add_argument(
514	        "--perturbation_type", type=str, required=True,
515	        choices=["physical", "spatial"],
516	    )
517	    parser.add_argument("--gpu_id", type=int, default=0)
518	    parser.add_argument("--num_tasks", type=int, default=10)
519	    parser.add_argument("--episodes_per_config", type=int, default=3)
520	    parser.add_argument(
521	        "--output_dir", type=str, default=None,
522	        help="Override output directory (default: auto from perturbation_type)",
523	    )
524	    parser.add_argument(
525	        "--checkpoint", type=str,
526	        default="/root/autodl-tmp/checkpoints/pi0_base",
527	    )
528	    parser.add_argument("--dry_run", action="store_true")
529	    parser.add_argument("--seed", type=int, default=42)
530	    args = parser.parse_args()
531	
532	    logging.basicConfig(
533	        level=logging.INFO,
534	        format="%(asctime)s [%(levelname)s] %(message)s",
535	    )
536	
537	    random.seed(args.seed)
538	    np.random.seed(args.seed)
539	    torch.manual_seed(args.seed)
540	
541	    if args.output_dir is None:
542	        args.output_dir = (
543	            f"/root/meta_brain_lora_routing/data/expert_demos/{args.perturbation_type}"
544	        )
545	
546	    device = f"cuda:{args.gpu_id}"
547	    log.info(
548	        "Config: type=%s device=%s num_tasks=%d eps_per_cfg=%d dry_run=%s",
549	        args.perturbation_type, device, args.num_tasks,
550	        args.episodes_per_config, args.dry_run,
551	    )
552	
553	    log.info("Loading π₀ from %s", args.checkpoint)
554	    policy = load_pi0_policy(args.checkpoint, device)
555	
556	    from libero.libero import get_libero_path
557	    bddl_dir = os.path.join(get_libero_path("bddl_files"), BASE_TASK_SUITE)
558	    tasks = find_base_tasks(bddl_dir, num_tasks=args.num_tasks)
559	
560	    if not tasks:
561	        log.error("No base tasks found in %s", bddl_dir)
562	        sys.exit(1)
563	
564	    t0 = time.time()
565	
566	    if args.perturbation_type == "physical":
567	        stats = collect_physical(
568	            policy, tasks, args.episodes_per_config,
569	            args.output_dir, args.dry_run,
570	        )
571	    else:
572	        stats = collect_spatial(
573	            policy, tasks, args.episodes_per_config,
574	            args.output_dir, args.dry_run,
575	        )
576	
577	    elapsed = time.time() - t0
578	
579	    total_size = sum(
580	        os.path.getsize(f) for f in stats["saved_files"] if os.path.exists(f)
581	    )
582	    log.info("=" * 60)
583	    log.info("Collection complete: %s", args.perturbation_type)
584	    log.info("  Total episodes:  %d", stats["total"])
585	    log.info("  Successful:      %d", stats["success"])
586	    log.info(
587	        "  Success rate:    %.1f%%",
588	        stats["success"] / max(stats["total"], 1) * 100,
589	    )
590	    log.info("  Files saved:     %d", len(stats["saved_files"]))
591	    log.info("  Total size:      %.1f MB", total_size / 1024 / 1024)
592	    log.info("  Elapsed:         %.1f min", elapsed / 60)
593	    log.info("  Output dir:      %s", args.output_dir)
594	
595	
596	if __name__ == "__main__":
597	    main()
598	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "455850bd-5d3b-4372-a4c9-9365d204c281"
}
```

</details>

---


### System

_source line 42_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3acedec04983e0ad",
  "tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "description": "Reading phase1/data_loader.py",
  "usage": {
    "total_tokens": 17439,
    "tool_uses": 6,
    "duration_ms": 5981
  },
  "last_tool_name": "Read",
  "uuid": "aad87934-fd5e-4609-bd55-9bc968688ed9",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7"
}
```

---


### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Read · `toolu_013BrBhX3LFJvXYoEYRyeGhE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/phase1/data_loader.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "7bf97a0a-3929-4ab9-abaa-ded6d5fddc3f",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011yFkL41cfnUXgwgau1AB4G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1732,
      "cache_read_input_tokens": 15684,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1732,
        "ephemeral_1h_input_tokens": 0
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

_source line 44 · 2026-05-15T17:50:29.114Z_

<details><summary>↩ Tool result · `toolu_013BrBhX3LFJvXYoEYRyeGhE`</summary>

```text
1	"""
2	Data loading for Phase 1 LoRA expert training.
3	
4	Provides datasets and augmentation for perturbation-specific LoRA fine-tuning
5	of the pi0 model. Supports synthetic data for dry-run validation and will
6	support real LIBERO-Plus rollout data for actual training.
7	
8	Input:  Rollout .pt files from LIBERO-Plus (or synthetic for dry-run)
9	Output: (Observation, actions) batches for PI0Pytorch.forward()
10	
11	Dependencies: torch, torchvision
12	"""
13	
14	import dataclasses
15	import logging
16	from pathlib import Path
17	
18	import torch
19	from torch.utils.data import DataLoader, Dataset
20	
21	log = logging.getLogger(__name__)
22	
23	IMAGE_KEYS = ("base_0_rgb", "left_wrist_0_rgb", "right_wrist_0_rgb")
24	IMAGE_RESOLUTION = 224
25	STATE_DIM = 32
26	ACTION_DIM = 32
27	ACTION_HORIZON = 50
28	MAX_TOKEN_LEN = 48
29	
30	PERTURBATION_TO_6CLASS = {
31	    "visual": ["camera_viewpoints", "light_conditions", "background_textures", "sensor_noise"],
32	    "spatial": ["objects_layout"],
33	    "physical": ["robot_initial_states"],
34	    "universal": [
35	        "camera_viewpoints", "light_conditions", "background_textures",
36	        "sensor_noise", "objects_layout", "robot_initial_states",
37	    ],
38	}
39	
40	
41	@dataclasses.dataclass
42	class Observation:
43	    """Minimal observation container matching PI0Pytorch's expected input.
44	
45	    This is a lightweight replacement for openpi.models.model.Observation
46	    to avoid pulling in JAX/Flax dependencies from the original class.
47	    Works with jax.tree.map for device transfer.
48	    """
49	    images: dict
50	    image_masks: dict
51	    state: torch.Tensor
52	    tokenized_prompt: torch.Tensor
53	    tokenized_prompt_mask: torch.Tensor
54	    token_ar_mask: object = None
55	    token_loss_mask: object = None
56	
57	
58	# ---------------------------------------------------------------------------
59	# Synthetic dataset (dry-run validation)
60	# ---------------------------------------------------------------------------
61	
62	class SyntheticRolloutDataset(Dataset):
63	    """Generates random observation-action pairs for dry-run validation.
64	
65	    Produces correctly-shaped tensors that exercise the full PI0Pytorch
66	    forward pass without requiring real LIBERO data.
67	    """
68	
69	    def __init__(self, num_samples=100, seed=42):
70	        self.num_samples = num_samples
71	        self.seed = seed
72	
73	    def __len__(self):
74	        return self.num_samples
75	
76	    def __getitem__(self, idx):
77	        g = torch.Generator().manual_seed(self.seed + idx)
78	
79	        images = {
80	            key: torch.randn(3, IMAGE_RESOLUTION, IMAGE_RESOLUTION, generator=g)
81	            for key in IMAGE_KEYS
82	        }
83	        image_masks = {
84	            "base_0_rgb": torch.tensor(True),
85	            "left_wrist_0_rgb": torch.tensor(True),
86	            "right_wrist_0_rgb": torch.tensor(False),
87	        }
88	        state = torch.randn(STATE_DIM, generator=g)
89	
90	        prompt_len = 5 + idx % (MAX_TOKEN_LEN - 5)
91	        tokenized_prompt = torch.zeros(MAX_TOKEN_LEN, dtype=torch.long)
92	        tokenized_prompt[:prompt_len] = torch.randint(
93	            0, 10000, (prompt_len,), generator=g
94	        )
95	        tokenized_prompt_mask = torch.zeros(MAX_TOKEN_LEN, dtype=torch.bool)
96	        tokenized_prompt_mask[:prompt_len] = True
97	
98	        actions = torch.randn(ACTION_HORIZON, ACTION_DIM, generator=g)
99	
100	        obs = Observation(
101	            images=images,
102	            image_masks=image_masks,
103	            state=state,
104	            tokenized_prompt=tokenized_prompt,
105	            tokenized_prompt_mask=tokenized_prompt_mask,
106	        )
107	        return obs, actions
108	
109	
110	# ---------------------------------------------------------------------------
111	# Real rollout dataset (placeholder for collected data)
112	# ---------------------------------------------------------------------------
113	
114	class LIBERORolloutDataset(Dataset):
115	    """Loads LIBERO-Plus rollout data for LoRA training.
116	
117	    Expected rollout file format (.pt):
118	    [
119	        {
120	            'images': {
121	                'base_0_rgb': tensor (T, 3, 224, 224),  # float32 [-1,1]
122	                'left_wrist_0_rgb': tensor (T, 3, 224, 224),
123	            },
124	            'state': tensor (T, 32),        # padded robot state
125	            'actions': tensor (T, 32),       # padded actions
126	            'prompt_tokens': tensor (L,),    # pre-tokenized instruction
127	            'prompt_mask': tensor (L,),      # token mask
128	            'perturbation_type': str,
129	            'metadata': dict,
130	        },
131	        ...
132	    ]
133	    """
134	
135	    def __init__(self, data_dir, perturbation_type, seed=42):
136	        self.data_dir = Path(data_dir)
137	        self.perturbation_type = perturbation_type
138	        self.episodes = []
139	        self._load_episodes()
140	        log.info(
141	            f"Loaded {len(self.episodes)} steps from "
142	            f"{self.perturbation_type} rollouts"
143	        )
144	
145	    def _load_episodes(self):
146	        target_types = PERTURBATION_TO_6CLASS[self.perturbation_type]
147	        for pt_type in target_types:
148	            path = self.data_dir / f"{pt_type}.pt"
149	            if not path.exists():
150	                log.warning(f"Rollout file not found: {path}")
151	                continue
152	            data = torch.load(path, map_location="cpu", weights_only=False)
153	            for episode in data:
154	                if episode.get("perturbation_type") in target_types:
155	                    self._flatten_episode(episode)
156	
157	    def _flatten_episode(self, episode):
158	        """Convert episode to per-step training samples."""
159	        T = episode["actions"].shape[0]
160	        for t in range(T - ACTION_HORIZON):
161	            self.episodes.append({
162	                "images": {
163	                    k: episode["images"][k][t]
164	                    for k in episode["images"]
165	                    if k in IMAGE_KEYS
166	                },
167	                "state": episode["state"][t],
168	                "actions": episode["actions"][t : t + ACTION_HORIZON],
169	                "prompt_tokens": episode["prompt_tokens"],
170	                "prompt_mask": episode["prompt_mask"],
171	            })
172	
173	    def __len__(self):
174	        return len(self.episodes)
175	
176	    def __getitem__(self, idx):
177	        sample = self.episodes[idx]
178	        images = dict(sample["images"])
179	        if "right_wrist_0_rgb" not in images:
180	            images["right_wrist_0_rgb"] = torch.zeros(
181	                3, IMAGE_RESOLUTION, IMAGE_RESOLUTION
182	            )
183	
184	        image_masks = {
185	            "base_0_rgb": torch.tensor(True),
186	            "left_wrist_0_rgb": torch.tensor(True),
187	            "right_wrist_0_rgb": torch.tensor(False),
188	        }
189	
190	        prompt = sample["prompt_tokens"]
191	        mask = sample["prompt_mask"]
192	        if prompt.shape[0] < MAX_TOKEN_LEN:
193	            prompt = torch.nn.functional.pad(
194	                prompt, (0, MAX_TOKEN_LEN - prompt.shape[0])
195	            )
196	            mask = torch.nn.functional.pad(
197	                mask, (0, MAX_TOKEN_LEN - mask.shape[0])
198	            )
199	
200	        obs = Observation(
201	            images=images,
202	            image_masks=image_masks,
203	            state=sample["state"],
204	            tokenized_prompt=prompt[:MAX_TOKEN_LEN],
205	            tokenized_prompt_mask=mask[:MAX_TOKEN_LEN],
206	        )
207	        actions = sample["actions"]
208	        if actions.shape[0] < ACTION_HORIZON:
209	            actions = torch.nn.functional.pad(
210	                actions, (0, 0, 0, ACTION_HORIZON - actions.shape[0])
211	            )
212	        return obs, actions[:ACTION_HORIZON]
213	
214	
215	# ---------------------------------------------------------------------------
216	# Visual augmentation (for LoRA-V)
217	# ---------------------------------------------------------------------------
218	
219	class VisualAugmentation:
220	    """Online visual augmentation for LoRA-V training.
221	
222	    Applies camera jitter, brightness/contrast shifts, and Gaussian noise
223	    to simulate visual perturbations. Applied to batched image tensors
224	    (B, C, H, W) in [-1, 1] range.
225	    """
226	
227	    def __init__(self, severity=0.5):
228	        self.severity = severity
229	
230	    def __call__(self, images):
231	        """Augment a dict of (B, C, H, W) image tensors in-place."""
232	        aug = {}
233	        for key, img in images.items():
234	            if img.ndim == 3:
235	                img = img.unsqueeze(0)
236	            if "wrist" not in key:
237	                img = self._camera_jitter(img)
238	            img = self._brightness_contrast(img)
239	            img = self._gaussian_noise(img)
240	            aug[key] = img.clamp(-1.0, 1.0)
241	        return aug
242	
243	    def _camera_jitter(self, img):
244	        B, C, H, W = img.shape
245	        pad = max(1, int(H * 0.05 * self.severity))
246	        img = torch.nn.functional.pad(img, [pad] * 4, mode="replicate")
247	        cy = torch.randint(0, 2 * pad + 1, (1,)).item()
248	        cx = torch.randint(0, 2 * pad + 1, (1,)).item()
249	        return img[:, :, cy : cy + H, cx : cx + W]
250	
251	    def _brightness_contrast(self, img):
252	        s = self.severity
253	        brightness = 1.0 + (torch.rand(1, device=img.device).item() - 0.5) * 0.6 * s
254	        contrast = 1.0 + (torch.rand(1, device=img.device).item() - 0.5) * 0.6 * s
255	        mean = img.mean(dim=(2, 3), keepdim=True)
256	        return (img - mean) * contrast + mean + (brightness - 1.0)
257	
258	    def _gaussian_noise(self, img):
259	        return img + torch.randn_like(img) * 0.05 * self.severity
260	
261	
262	# ---------------------------------------------------------------------------
263	# Collate function
264	# ---------------------------------------------------------------------------
265	
266	def collate_observations(batch):
267	    """Collate list of (Observation, actions) into batched tensors."""
268	    observations, actions_list = zip(*batch)
269	
270	    images = {
271	        key: torch.stack([obs.images[key] for obs in observations])
272	        for key in IMAGE_KEYS
273	    }
274	    image_masks = {
275	        key: torch.stack([obs.image_masks[key] for obs in observations])
276	        for key in IMAGE_KEYS
277	    }
278	
279	    obs = Observation(
280	        images=images,
281	        image_masks=image_masks,
282	        state=torch.stack([o.state for o in observations]),
283	        tokenized_prompt=torch.stack([o.tokenized_prompt for o in observations]),
284	        tokenized_prompt_mask=torch.stack(
285	            [o.tokenized_prompt_mask for o in observations]
286	        ),
287	    )
288	    return obs, torch.stack(actions_list)
289	
290	
291	# ---------------------------------------------------------------------------
292	# Factory
293	# ---------------------------------------------------------------------------
294	
295	def create_dataloader(
296	    perturbation_type,
297	    batch_size=2,
298	    num_workers=0,
299	    dry_run=False,
300	    data_dir=None,
301	    seed=42,
302	):
303	    """Create DataLoader for a specific perturbation type.
304	
305	    Args:
306	        perturbation_type: one of visual/spatial/physical/universal
307	        dry_run: if True, use synthetic data
308	        data_dir: path to rollout .pt files (required if not dry_run)
309	    """
310	    if dry_run:
311	        dataset = SyntheticRolloutDataset(num_samples=100, seed=seed)
312	    else:
313	        if data_dir is None:
314	            raise ValueError("data_dir required for non-dry-run training")
315	        data_path = Path(data_dir)
316	        if not data_path.exists():
317	            raise FileNotFoundError(
318	                f"Rollout data directory not found: {data_path}. "
319	                f"Collect LIBERO-Plus rollout data first, or use --dry_run."
320	            )
321	        dataset = LIBERORolloutDataset(data_path, perturbation_type, seed=seed)
322	
323	    return DataLoader(
324	        dataset,
325	        batch_size=batch_size,
326	        shuffle=True,
327	        num_workers=num_workers,
328	        collate_fn=collate_observations,
329	        pin_memory=True,
330	        drop_last=True,
331	    )
332	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "dc0b2c4a-1710-4f39-add0-95101c7fc8bd"
}
```

</details>

---


### System

_source line 45_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3acedec04983e0ad",
  "tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "description": "Reading artifacts/phase0/configs.py",
  "usage": {
    "total_tokens": 17440,
    "tool_uses": 7,
    "duration_ms": 6169
  },
  "last_tool_name": "Read",
  "uuid": "685b5838-1493-4f55-9aa8-be175bee0343",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7"
}
```

---


### Tool call

_source line 46_

<details open><summary>🔧 Tool call — Read · `toolu_01KXSe1UPemaCSwZ6UMxWbRq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/configs.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "c8ee4662-c4bd-4aac-ab8d-538ae41b5621",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011yFkL41cfnUXgwgau1AB4G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1732,
      "cache_read_input_tokens": 15684,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1732,
        "ephemeral_1h_input_tokens": 0
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

_source line 47 · 2026-05-15T17:50:29.307Z_

<details><summary>↩ Tool result · `toolu_01KXSe1UPemaCSwZ6UMxWbRq`</summary>

```text
1	"""
2	Configuration constants for Meta-Brain Phase 0 perturbation classifier.
3	
4	Defines perturbation taxonomies, layer indices, model dimensions,
5	and hyperparameter defaults shared across collect/train/eval scripts.
6	"""
7	
8	# ---------------------------------------------------------------------------
9	# Perturbation taxonomy
10	# ---------------------------------------------------------------------------
11	
12	PERTURBATION_TYPES_6CLASS = {
13	    "camera_viewpoints": 0,
14	    "light_conditions": 1,
15	    "background_textures": 2,
16	    "sensor_noise": 3,
17	    "objects_layout": 4,
18	    "robot_initial_states": 5,
19	}
20	
21	PERTURBATION_TYPES_3CLASS = {
22	    "visual": 0,   # camera + light + background + noise
23	    "spatial": 1,  # layout
24	    "physical": 2, # robot
25	}
26	
27	CLASS_6_TO_3_MAPPING = {
28	    0: 0,  # camera_viewpoints   -> visual
29	    1: 0,  # light_conditions    -> visual
30	    2: 0,  # background_textures -> visual
31	    3: 0,  # sensor_noise        -> visual
32	    4: 1,  # objects_layout      -> spatial
33	    5: 2,  # robot_initial_states -> physical
34	}
35	
36	CLASS_6_NAMES = [
37	    "camera_viewpoints",
38	    "light_conditions",
39	    "background_textures",
40	    "sensor_noise",
41	    "objects_layout",
42	    "robot_initial_states",
43	]
44	
45	CLASS_3_NAMES = ["visual", "spatial", "physical"]
46	
47	BINARY_NAMES = ["nominal", "perturbed"]
48	
49	# ---------------------------------------------------------------------------
50	# π₀ architecture constants
51	# ---------------------------------------------------------------------------
52	
53	PALIGEMMA_LAYERS = [2, 4, 6, 8, 10, 12, 14, 16]
54	EXPERT_LAYERS = [2, 6, 10, 14]
55	
56	PALIGEMMA_HIDDEN_DIM = 2048
57	EXPERT_HIDDEN_DIM = 1024
58	
59	PALIGEMMA_NUM_LAYERS = 18  # layers[0..17]
60	EXPERT_NUM_LAYERS = 18
61	
62	# PyTorch module path templates
63	PALIGEMMA_LAYER_TEMPLATE = (
64	    "paligemma_with_expert.paligemma.language_model.layers.{i}"
65	)
66	EXPERT_LAYER_TEMPLATE = (
67	    "paligemma_with_expert.gemma_expert.model.layers.{i}"
68	)
69	
70	# ---------------------------------------------------------------------------
71	# Pooling strategies
72	# ---------------------------------------------------------------------------
73	
74	POOLING_STRATEGIES = ["mean", "first", "last", "first_last"]
75	
76	def pooling_output_dim(pooling: str, hidden_dim: int) -> int:
77	    """Return output dimension for a given pooling strategy."""
78	    if pooling == "first_last":
79	        return hidden_dim * 2
80	    return hidden_dim
81	
82	# ---------------------------------------------------------------------------
83	# Classifier defaults
84	# ---------------------------------------------------------------------------
85	
86	CLASSIFIER_HIDDEN_DIM = 256
87	DEFAULT_LR = 1e-3
88	DEFAULT_EPOCHS = 50
89	DEFAULT_BATCH_SIZE = 64
90	NUM_FOLDS = 5
91	
92	# Activation source → input dimension calculation
93	ACTIVATION_SOURCES = ["paligemma_only", "expert_only", "both"]
94	
95	def compute_input_dim(activation_source: str, pooling: str) -> int:
96	    """Compute classifier input dimension from source and pooling strategy."""
97	    pg_dim = len(PALIGEMMA_LAYERS) * pooling_output_dim(pooling, PALIGEMMA_HIDDEN_DIM)
98	    ex_dim = len(EXPERT_LAYERS) * pooling_output_dim(pooling, EXPERT_HIDDEN_DIM)
99	    if activation_source == "paligemma_only":
100	        return pg_dim
101	    elif activation_source == "expert_only":
102	        return ex_dim
103	    elif activation_source == "both":
104	        return pg_dim + ex_dim
105	    raise ValueError(f"Unknown activation_source: {activation_source}")
106	
107	# ---------------------------------------------------------------------------
108	# Sweep grid
109	# ---------------------------------------------------------------------------
110	
111	SWEEP_POOLINGS = ["mean", "first", "first_last"]
112	SWEEP_SOURCES = ["paligemma_only", "expert_only", "both"]
113	SWEEP_LRS = [1e-2, 1e-3, 1e-4]
114	
115	# ---------------------------------------------------------------------------
116	# Go / No-Go thresholds (Phase 0 success criteria)
117	# ---------------------------------------------------------------------------
118	
119	GO_NOGO = {
120	    "3class_macro_f1_go": 0.70,    # macro-F1 >70% + confusion off-diag <30% → GO
121	    "3class_macro_f1_augment": 0.50, # macro-F1 50-70% → AUGMENT (add proprioception + visual change)
122	    "6class_macro_f1_viable": 0.50,  # macro-F1 >50% → finer-grained routing viable
123	    "binary_roc_auc_sanity": 0.75, # ≥0.75 → activations encode perturbation signal
124	    "confusion_max_offdiag": 0.30, # any off-diagonal cell must be <30%
125	}
126	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "07e7ad4c-5a14-4ba6-b21a-7d0d6749c326"
}
```

</details>

---


### System

_source line 48_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a2868964c1f8b5d5d",
  "tool_use_id": "toolu_017LfjCZ3RrydbQw6jDiBQJj",
  "status": "completed",
  "output_file": "",
  "summary": "Read Phase 0 collect_activations",
  "usage": {
    "total_tokens": 20187,
    "tool_uses": 1,
    "duration_ms": 9138
  },
  "uuid": "090fde97-f004-485d-91a6-f92b46efb562",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7"
}
```

---


### Tool result

_source line 49 · 2026-05-15T17:50:29.629Z_

<details><summary>↩ Tool result · `toolu_017LfjCZ3RrydbQw6jDiBQJj`</summary>

```text
I've read the complete `collect_activations.py` file. Here's how Phase 0 handles objects_layout and _add_N tasks for LIBERO-Plus:

## Key Findings:

**1. Task Suite Support (Lines 286-289):**
The script supports multiple LIBERO-Plus task suites via the `--task_suite` parameter:
- `libero_spatial`
- `libero_object`
- `libero_goal`
- `libero_10`
- `libero_90` (noted as having no perturbation variants)

**2. Task Execution Flow (Lines 232-241):**
Tasks are executed through the `run_episode()` function (imported from `libero_integration`), which:
- Takes the `task_suite` parameter directly
- Runs episodes under specified perturbation types (or nominal baseline)
- Returns task metadata including `task_name`, `num_steps`, and `success` status

**3. Perturbation Handling (Lines 224-241):**
The code distinguishes between:
- **Nominal runs** (no perturbation, `perturbation_type=None`)
- **Perturbation runs** (camera_viewpoints, object_position, etc.)
- Each perturbation maps to labels via `PERTURBATION_TYPES_6CLASS` and `CLASS_6_TO_3_MAPPING` configs

**4. Activation Collection (Lines 243-255):**
For each episode, metadata stored includes:
- `task_name` - the specific task executed (e.g., objects_layout, _add_N variants)
- `num_steps` - trajectory length
- `success` - whether the task succeeded
- `perturbation_type` - which variant was applied

**5. The Actual Task Logic:**
The file **delegates task handling to `libero_integration.py`**. The specifics of how `objects_layout` and `_add_N` tasks are instantiated, randomized, and executed is NOT in this file—it's in the `run_episode()` function and the LIBERO library integration.

To fully understand how Phase 0 handles these specific tasks, you'll need to examine:
- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py` (contains `run_episode()`)
- The LIBERO-Plus benchmark definitions for task initialization and perturbation application
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "173fce94-9591-4d1c-91f8-a106400cf594",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Read the full contents of /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/collect_activations.py. Read the ENTIRE file. I need to understand how Phase 0 handles objects_layout and _add_N tasks for LIBERO-Plus.",
    "agentId": "a2868964c1f8b5d5d",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "I've read the complete `collect_activations.py` file. Here's how Phase 0 handles objects_layout and _add_N tasks for LIBERO-Plus:\n\n## Key Findings:\n\n**1. Task Suite Support (Lines 286-289):**\nThe script supports multiple LIBERO-Plus task suites via the `--task_suite` parameter:\n- `libero_spatial`\n- `libero_object`\n- `libero_goal`\n- `libero_10`\n- `libero_90` (noted as having no perturbation variants)\n\n**2. Task Execution Flow (Lines 232-241):**\nTasks are executed through the `run_episode()` function (imported from `libero_integration`), which:\n- Takes the `task_suite` parameter directly\n- Runs episodes under specified perturbation types (or nominal baseline)\n- Returns task metadata including `task_name`, `num_steps`, and `success` status\n\n**3. Perturbation Handling (Lines 224-241):**\nThe code distinguishes between:\n- **Nominal runs** (no perturbation, `perturbation_type=None`)\n- **Perturbation runs** (camera_viewpoints, object_position, etc.)\n- Each perturbation maps to labels via `PERTURBATION_TYPES_6CLASS` and `CLASS_6_TO_3_MAPPING` configs\n\n**4. Activation Collection (Lines 243-255):**\nFor each episode, metadata stored includes:\n- `task_name` - the specific task executed (e.g., objects_layout, _add_N variants)\n- `num_steps` - trajectory length\n- `success` - whether the task succeeded\n- `perturbation_type` - which variant was applied\n\n**5. The Actual Task Logic:**\nThe file **delegates task handling to `libero_integration.py`**. The specifics of how `objects_layout` and `_add_N` tasks are instantiated, randomized, and executed is NOT in this file—it's in the `run_episode()` function and the LIBERO library integration.\n\nTo fully understand how Phase 0 handles these specific tasks, you'll need to examine:\n- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py` (contains `run_episode()`)\n- The LIBERO-Plus benchmark definitions for task initialization and perturbation application"
      }
    ],
    "totalDurationMs": 9139,
    "totalTokens": 20759,
    "totalToolUseCount": 1,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 4548,
      "cache_read_input_tokens": 15621,
      "output_tokens": 585,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4548
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 585,
          "cache_read_input_tokens": 15621,
          "cache_creation_input_tokens": 4548,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4548,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 1,
      "searchCount": 0,
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


### System

_source line 50_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a2406d27283cd9ab4",
  "tool_use_id": "toolu_013TqJ2cNFWJaMr9ra2qxnch",
  "status": "completed",
  "output_file": "",
  "summary": "Read collect_expert_demos.py",
  "usage": {
    "total_tokens": 24872,
    "tool_uses": 3,
    "duration_ms": 13275
  },
  "uuid": "87c469ee-2374-4d7b-be63-6a3fd93f58c1",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7"
}
```

---


### Tool result

_source line 51 · 2026-05-15T17:50:31.710Z_

<details><summary>↩ Tool result · `toolu_013TqJ2cNFWJaMr9ra2qxnch`</summary>

```text
Perfect! I have read the entire file. Here's the complete contents:

## File: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py`

This is a comprehensive script for collecting expert demonstrations by rolling out a frozen π₀ (pi-zero) policy in perturbed LIBERO environments. Here's a summary of the key components:

**Purpose:**
- Collects expert demonstrations from successful episodes only
- Supports two perturbation types:
  1. **Physical**: Varies robot initial state (using init_states indices 1-49)
  2. **Spatial**: Perturbs object layout via BDDL region modifications

**Key Constants:**
- LIBERO_ENV_RESOLUTION: 256
- MODEL_INPUT_RESOLUTION: 224
- REPLAN_STEPS: 5
- MAX_STEPS: 220
- 10 base tasks in libero_spatial suite
- 10 spatial perturbation configurations with varying XY shifts and yaw

**Major Functions:**
1. **Geometry/Image Helpers**: `_quat2axisangle()`, `_resize_with_pad()`, `obs_to_model_input()`, `extract_obs_for_saving()`
2. **Model Loading**: `load_pi0_policy()` loads the policy checkpoint
3. **Task Discovery**: `find_base_tasks()` locates base BDDL files, `get_task_language()` extracts instructions
4. **Environment Creation**: `create_env()` creates LIBERO OffScreenRenderEnv, `create_spatial_bddl()` generates perturbed BDDL files
5. **Episode Rollout**: `rollout_episode()` runs a single episode collecting observations and actions
6. **Collection Loops**: `collect_physical()` and `collect_spatial()` are the main collection functions
7. **Main**: Argument parsing and orchestration

**Output Format:**
- Pickle files containing dictionaries with:
  - `observations`: List of extracted obs dicts with images and state
  - `actions`: Numpy array of actions
  - `task_name`, `perturbation_config`, `success`, `num_steps`
  - Metadata about perturbation type and configuration

**Features:**
- Supports dry-run mode for testing
- Logs success rates and collection statistics
- Handles environment exceptions gracefully
- Uses deterministic seeding based on task/episode parameters
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "76957846-d8ce-424b-88d6-9d106776bd4e",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Read the full contents of /root/meta_brain_lora_routing/phase1/collect_expert_demos.py on the remote server. Since I can't SSH directly, read the local copy at /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/phase1/collect_expert_demos.py. If that doesn't exist, search for collect_expert_demos.py anywhere under /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/. Read the ENTIRE file, every line.",
    "agentId": "a2406d27283cd9ab4",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! I have read the entire file. Here's the complete contents:\n\n## File: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py`\n\nThis is a comprehensive script for collecting expert demonstrations by rolling out a frozen π₀ (pi-zero) policy in perturbed LIBERO environments. Here's a summary of the key components:\n\n**Purpose:**\n- Collects expert demonstrations from successful episodes only\n- Supports two perturbation types:\n  1. **Physical**: Varies robot initial state (using init_states indices 1-49)\n  2. **Spatial**: Perturbs object layout via BDDL region modifications\n\n**Key Constants:**\n- LIBERO_ENV_RESOLUTION: 256\n- MODEL_INPUT_RESOLUTION: 224\n- REPLAN_STEPS: 5\n- MAX_STEPS: 220\n- 10 base tasks in libero_spatial suite\n- 10 spatial perturbation configurations with varying XY shifts and yaw\n\n**Major Functions:**\n1. **Geometry/Image Helpers**: `_quat2axisangle()`, `_resize_with_pad()`, `obs_to_model_input()`, `extract_obs_for_saving()`\n2. **Model Loading**: `load_pi0_policy()` loads the policy checkpoint\n3. **Task Discovery**: `find_base_tasks()` locates base BDDL files, `get_task_language()` extracts instructions\n4. **Environment Creation**: `create_env()` creates LIBERO OffScreenRenderEnv, `create_spatial_bddl()` generates perturbed BDDL files\n5. **Episode Rollout**: `rollout_episode()` runs a single episode collecting observations and actions\n6. **Collection Loops**: `collect_physical()` and `collect_spatial()` are the main collection functions\n7. **Main**: Argument parsing and orchestration\n\n**Output Format:**\n- Pickle files containing dictionaries with:\n  - `observations`: List of extracted obs dicts with images and state\n  - `actions`: Numpy array of actions\n  - `task_name`, `perturbation_config`, `success`, `num_steps`\n  - Metadata about perturbation type and configuration\n\n**Features:**\n- Supports dry-run mode for testing\n- Logs success rates and collection statistics\n- Handles environment exceptions gracefully\n- Uses deterministic seeding based on task/episode parameters"
      }
    ],
    "totalDurationMs": 13277,
    "totalTokens": 25456,
    "totalToolUseCount": 3,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 8014,
      "cache_read_input_tokens": 16841,
      "output_tokens": 595,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8014
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 595,
          "cache_read_input_tokens": 16841,
          "cache_creation_input_tokens": 8014,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8014,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 2,
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


### System

_source line 52_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3acedec04983e0ad",
  "tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "description": "Searching for _add_|add_n",
  "usage": {
    "total_tokens": 37114,
    "tool_uses": 8,
    "duration_ms": 9182
  },
  "last_tool_name": "Grep",
  "uuid": "0716ec12-3c35-47b7-b29c-f1ab1902a2ea",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7"
}
```

---


### Tool call

_source line 53_

<details open><summary>🔧 Tool call — Grep · `toolu_01Haqw5NiMtqqya6X7HEW6Db`</summary>

```json
{
  "pattern": "_add_|add_n",
  "type": "py",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing",
  "output_mode": "content",
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "d85190be-32da-4d63-9e72-b577eeca88c8",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011jc6FfqZCPMeeN7emBaz4m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 19672,
      "cache_read_input_tokens": 17416,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19672,
        "ephemeral_1h_input_tokens": 0
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

_source line 54 · 2026-05-15T17:50:32.328Z_

<details><summary>↩ Tool result · `toolu_01Haqw5NiMtqqya6X7HEW6Db`</summary>

```text
artifacts/phase0/libero_integration.py-253-      Simple suffixes:
artifacts/phase0/libero_integration.py-254-        - light_conditions:     _light_\\d+
artifacts/phase0/libero_integration.py-255-        - background_textures:  _table_\\d+ or _tb_\\d+
artifacts/phase0/libero_integration.py:256:        - objects_layout:       _add_\\d+ or _level\\d+
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py-257-
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py-258-    Returns perturbation type string, or None for base/nominal tasks.
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py-259-    """
--
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py-280-        return "light_conditions"
artifacts/phase0/libero_integration.py-281-    if re.search(r"_(?:table|tb)_\d+$", task_name):
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py-282-        return "background_textures"
artifacts/phase0/libero_integration.py:283:    if re.search(r"_add_\d+$", task_name) or re.search(r"_level\d+", task_name):
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py-284-        return "objects_layout"
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py-285-
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py-286-    return None
--
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py-186-        name = f.replace(".bddl", "")
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py-187-        # Skip any file with perturbation suffixes
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py-188-        if re.search(
artifacts/phase1/collect_expert_demos.py:189:            r"(_add_\d+|_table_\d+|_tb_\d+|_light_\d+|_language_\d+"
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py-190-            r"|_view_|_noise_|_level\d+| copy)",
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py-191-            name,
artifacts/phase1/collect_expert_demos.py-192-        ):
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "5e36c0e0-e42a-465a-af44-ae85326ef41d"
}
```

</details>

---


### System

_source line 55_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3acedec04983e0ad",
  "tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "description": "Searching for perturb_region_info",
  "usage": {
    "total_tokens": 37115,
    "tool_uses": 9,
    "duration_ms": 9809
  },
  "last_tool_name": "Grep",
  "uuid": "aa0a228a-1f54-49bd-abc7-6dd92c4ef8e8",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7"
}
```

---


### Tool call

_source line 56_

<details open><summary>🔧 Tool call — Grep · `toolu_01Kyc7i9dEn6u7MoRTdfvNhV`</summary>

```json
{
  "pattern": "perturb_region_info",
  "type": "py",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing",
  "output_mode": "content",
  "context": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "5c758024-f326-4cc5-9715-8287aafd82fe",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011jc6FfqZCPMeeN7emBaz4m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 19672,
      "cache_read_input_tokens": 17416,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19672,
        "ephemeral_1h_input_tokens": 0
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

_source line 57 · 2026-05-15T17:50:32.964Z_

<details><summary>↩ Tool result · `toolu_01Kyc7i9dEn6u7MoRTdfvNhV`</summary>

```text
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py-244-    """
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py-245-    sys.path.insert(0, "/root/LIBERO-plus/libero")
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py-246-    from libero.randomizer.bddl_operators import (
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py-247-        load_bddl_file,
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py-248-        save_bddl_file,
artifacts/phase1/collect_expert_demos.py:249:        perturb_region_info,
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py-250-    )
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py-251-
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py-252-    spec = load_bddl_file(base_bddl_path)
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py-253-    delta_xy = perturbation_config["delta_xy"]
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py-254-    delta_half = perturbation_config["delta_half_len"]
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py-255-    delta_yaw = perturbation_config["delta_yaw"]
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py-256-
artifacts/phase1/collect_expert_demos.py-257-    for i in range(len(spec.region_infos)):
artifacts/phase1/collect_expert_demos.py:258:        spec.region_infos[i] = perturb_region_info(
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py-259-            spec.region_infos[i],
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py-260-            delta_region_centroid_xy=delta_xy,
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py-261-            delta_region_half_len=delta_half,
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py-262-            delta_yaw_rotation=delta_yaw,
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py-263-        )
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "9424ecfe-256f-459a-9193-1905561e5d8d"
}
```

</details>

---


### System

_source line 58_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3acedec04983e0ad",
  "tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "description": "Reading artifacts/_project/intermediate/data_loader.py",
  "usage": {
    "total_tokens": 37116,
    "tool_uses": 10,
    "duration_ms": 10178
  },
  "last_tool_name": "Read",
  "uuid": "d1ae6144-38ee-4937-86e6-8bc158d3b881",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7"
}
```

---


### Tool call

_source line 59_

<details open><summary>🔧 Tool call — Read · `toolu_01CBcEYkEgqEg4ToQfveqaBJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/_project/intermediate/data_loader.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "3d40b134-c97b-42a9-a455-836ecc23022a",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011jc6FfqZCPMeeN7emBaz4m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 19672,
      "cache_read_input_tokens": 17416,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19672,
        "ephemeral_1h_input_tokens": 0
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

_source line 60 · 2026-05-15T17:50:33.312Z_

<details><summary>↩ Tool result · `toolu_01CBcEYkEgqEg4ToQfveqaBJ`</summary>

```text
1	"""
2	Data loading for Phase 1 LoRA expert training.
3	
4	Provides datasets and augmentation for perturbation-specific LoRA fine-tuning
5	of the pi0 model. Supports synthetic data for dry-run validation and will
6	support real LIBERO-Plus rollout data for actual training.
7	
8	Input:  Rollout .pt files from LIBERO-Plus (or synthetic for dry-run)
9	Output: (Observation, actions) batches for PI0Pytorch.forward()
10	
11	Dependencies: torch, torchvision
12	"""
13	
14	import dataclasses
15	import logging
16	from pathlib import Path
17	
18	import torch
19	from torch.utils.data import DataLoader, Dataset
20	
21	log = logging.getLogger(__name__)
22	
23	IMAGE_KEYS = ("base_0_rgb", "left_wrist_0_rgb", "right_wrist_0_rgb")
24	IMAGE_RESOLUTION = 224
25	STATE_DIM = 32
26	ACTION_DIM = 32
27	ACTION_HORIZON = 50
28	MAX_TOKEN_LEN = 48
29	
30	PERTURBATION_TO_6CLASS = {
31	    "visual": ["camera_viewpoints", "light_conditions", "background_textures", "sensor_noise"],
32	    "spatial": ["objects_layout"],
33	    "physical": ["robot_initial_states"],
34	    "universal": [
35	        "camera_viewpoints", "light_conditions", "background_textures",
36	        "sensor_noise", "objects_layout", "robot_initial_states",
37	    ],
38	}
39	
40	
41	@dataclasses.dataclass
42	class Observation:
43	    """Minimal observation container matching PI0Pytorch's expected input.
44	
45	    This is a lightweight replacement for openpi.models.model.Observation
46	    to avoid pulling in JAX/Flax dependencies from the original class.
47	    Works with jax.tree.map for device transfer.
48	    """
49	    images: dict
50	    image_masks: dict
51	    state: torch.Tensor
52	    tokenized_prompt: torch.Tensor
53	    tokenized_prompt_mask: torch.Tensor
54	    token_ar_mask: object = None
55	    token_loss_mask: object = None
56	
57	
58	# ---------------------------------------------------------------------------
59	# Synthetic dataset (dry-run validation)
60	# ---------------------------------------------------------------------------
61	
62	class SyntheticRolloutDataset(Dataset):
63	    """Generates random observation-action pairs for dry-run validation.
64	
65	    Produces correctly-shaped tensors that exercise the full PI0Pytorch
66	    forward pass without requiring real LIBERO data.
67	    """
68	
69	    def __init__(self, num_samples=100, seed=42):
70	        self.num_samples = num_samples
71	        self.seed = seed
72	
73	    def __len__(self):
74	        return self.num_samples
75	
76	    def __getitem__(self, idx):
77	        g = torch.Generator().manual_seed(self.seed + idx)
78	
79	        images = {
80	            key: torch.randn(3, IMAGE_RESOLUTION, IMAGE_RESOLUTION, generator=g)
81	            for key in IMAGE_KEYS
82	        }
83	        image_masks = {
84	            "base_0_rgb": torch.tensor(True),
85	            "left_wrist_0_rgb": torch.tensor(True),
86	            "right_wrist_0_rgb": torch.tensor(False),
87	        }
88	        state = torch.randn(STATE_DIM, generator=g)
89	
90	        prompt_len = 5 + idx % (MAX_TOKEN_LEN - 5)
91	        tokenized_prompt = torch.zeros(MAX_TOKEN_LEN, dtype=torch.long)
92	        tokenized_prompt[:prompt_len] = torch.randint(
93	            0, 10000, (prompt_len,), generator=g
94	        )
95	        tokenized_prompt_mask = torch.zeros(MAX_TOKEN_LEN, dtype=torch.bool)
96	        tokenized_prompt_mask[:prompt_len] = True
97	
98	        actions = torch.randn(ACTION_HORIZON, ACTION_DIM, generator=g)
99	
100	        obs = Observation(
101	            images=images,
102	            image_masks=image_masks,
103	            state=state,
104	            tokenized_prompt=tokenized_prompt,
105	            tokenized_prompt_mask=tokenized_prompt_mask,
106	        )
107	        return obs, actions
108	
109	
110	# ---------------------------------------------------------------------------
111	# Real rollout dataset (placeholder for collected data)
112	# ---------------------------------------------------------------------------
113	
114	class LIBERORolloutDataset(Dataset):
115	    """Loads LIBERO-Plus rollout data for LoRA training.
116	
117	    Expected rollout file format (.pt):
118	    [
119	        {
120	            'images': {
121	                'base_0_rgb': tensor (T, 3, 224, 224),  # float32 [-1,1]
122	                'left_wrist_0_rgb': tensor (T, 3, 224, 224),
123	            },
124	            'state': tensor (T, 32),        # padded robot state
125	            'actions': tensor (T, 32),       # padded actions
126	            'prompt_tokens': tensor (L,),    # pre-tokenized instruction
127	            'prompt_mask': tensor (L,),      # token mask
128	            'perturbation_type': str,
129	            'metadata': dict,
130	        },
131	        ...
132	    ]
133	    """
134	
135	    def __init__(self, data_dir, perturbation_type, seed=42):
136	        self.data_dir = Path(data_dir)
137	        self.perturbation_type = perturbation_type
138	        self.episodes = []
139	        self._load_episodes()
140	        log.info(
141	            f"Loaded {len(self.episodes)} steps from "
142	            f"{self.perturbation_type} rollouts"
143	        )
144	
145	    def _load_episodes(self):
146	        target_types = PERTURBATION_TO_6CLASS[self.perturbation_type]
147	        for pt_type in target_types:
148	            path = self.data_dir / f"{pt_type}.pt"
149	            if not path.exists():
150	                log.warning(f"Rollout file not found: {path}")
151	                continue
152	            data = torch.load(path, map_location="cpu", weights_only=False)
153	            for episode in data:
154	                if episode.get("perturbation_type") in target_types:
155	                    self._flatten_episode(episode)
156	
157	    def _flatten_episode(self, episode):
158	        """Convert episode to per-step training samples."""
159	        T = episode["actions"].shape[0]
160	        for t in range(T - ACTION_HORIZON):
161	            self.episodes.append({
162	                "images": {
163	                    k: episode["images"][k][t]
164	                    for k in episode["images"]
165	                    if k in IMAGE_KEYS
166	                },
167	                "state": episode["state"][t],
168	                "actions": episode["actions"][t : t + ACTION_HORIZON],
169	                "prompt_tokens": episode["prompt_tokens"],
170	                "prompt_mask": episode["prompt_mask"],
171	            })
172	
173	    def __len__(self):
174	        return len(self.episodes)
175	
176	    def __getitem__(self, idx):
177	        sample = self.episodes[idx]
178	        images = dict(sample["images"])
179	        if "right_wrist_0_rgb" not in images:
180	            images["right_wrist_0_rgb"] = torch.zeros(
181	                3, IMAGE_RESOLUTION, IMAGE_RESOLUTION
182	            )
183	
184	        image_masks = {
185	            "base_0_rgb": torch.tensor(True),
186	            "left_wrist_0_rgb": torch.tensor(True),
187	            "right_wrist_0_rgb": torch.tensor(False),
188	        }
189	
190	        prompt = sample["prompt_tokens"]
191	        mask = sample["prompt_mask"]
192	        if prompt.shape[0] < MAX_TOKEN_LEN:
193	            prompt = torch.nn.functional.pad(
194	                prompt, (0, MAX_TOKEN_LEN - prompt.shape[0])
195	            )
196	            mask = torch.nn.functional.pad(
197	                mask, (0, MAX_TOKEN_LEN - mask.shape[0])
198	            )
199	
200	        obs = Observation(
201	            images=images,
202	            image_masks=image_masks,
203	            state=sample["state"],
204	            tokenized_prompt=prompt[:MAX_TOKEN_LEN],
205	            tokenized_prompt_mask=mask[:MAX_TOKEN_LEN],
206	        )
207	        actions = sample["actions"]
208	        if actions.shape[0] < ACTION_HORIZON:
209	            actions = torch.nn.functional.pad(
210	                actions, (0, 0, 0, ACTION_HORIZON - actions.shape[0])
211	            )
212	        return obs, actions[:ACTION_HORIZON]
213	
214	
215	# ---------------------------------------------------------------------------
216	# Visual augmentation (for LoRA-V)
217	# ---------------------------------------------------------------------------
218	
219	class VisualAugmentation:
220	    """Online visual augmentation for LoRA-V training.
221	
222	    Applies camera jitter, brightness/contrast shifts, and Gaussian noise
223	    to simulate visual perturbations. Applied to batched image tensors
224	    (B, C, H, W) in [-1, 1] range.
225	    """
226	
227	    def __init__(self, severity=0.5):
228	        self.severity = severity
229	
230	    def __call__(self, images):
231	        """Augment a dict of (B, C, H, W) image tensors in-place."""
232	        aug = {}
233	        for key, img in images.items():
234	            if img.ndim == 3:
235	                img = img.unsqueeze(0)
236	            if "wrist" not in key:
237	                img = self._camera_jitter(img)
238	            img = self._brightness_contrast(img)
239	            img = self._gaussian_noise(img)
240	            aug[key] = img.clamp(-1.0, 1.0)
241	        return aug
242	
243	    def _camera_jitter(self, img):
244	        B, C, H, W = img.shape
245	        pad = max(1, int(H * 0.05 * self.severity))
246	        img = torch.nn.functional.pad(img, [pad] * 4, mode="replicate")
247	        cy = torch.randint(0, 2 * pad + 1, (1,)).item()
248	        cx = torch.randint(0, 2 * pad + 1, (1,)).item()
249	        return img[:, :, cy : cy + H, cx : cx + W]
250	
251	    def _brightness_contrast(self, img):
252	        s = self.severity
253	        brightness = 1.0 + (torch.rand(1, device=img.device).item() - 0.5) * 0.6 * s
254	        contrast = 1.0 + (torch.rand(1, device=img.device).item() - 0.5) * 0.6 * s
255	        mean = img.mean(dim=(2, 3), keepdim=True)
256	        return (img - mean) * contrast + mean + (brightness - 1.0)
257	
258	    def _gaussian_noise(self, img):
259	        return img + torch.randn_like(img) * 0.05 * self.severity
260	
261	
262	# ---------------------------------------------------------------------------
263	# Collate function
264	# ---------------------------------------------------------------------------
265	
266	def collate_observations(batch):
267	    """Collate list of (Observation, actions) into batched tensors."""
268	    observations, actions_list = zip(*batch)
269	
270	    images = {
271	        key: torch.stack([obs.images[key] for obs in observations])
272	        for key in IMAGE_KEYS
273	    }
274	    image_masks = {
275	        key: torch.stack([obs.image_masks[key] for obs in observations])
276	        for key in IMAGE_KEYS
277	    }
278	
279	    obs = Observation(
280	        images=images,
281	        image_masks=image_masks,
282	        state=torch.stack([o.state for o in observations]),
283	        tokenized_prompt=torch.stack([o.tokenized_prompt for o in observations]),
284	        tokenized_prompt_mask=torch.stack(
285	            [o.tokenized_prompt_mask for o in observations]
286	        ),
287	    )
288	    return obs, torch.stack(actions_list)
289	
290	
291	# ---------------------------------------------------------------------------
292	# Factory
293	# ---------------------------------------------------------------------------
294	
295	def create_dataloader(
296	    perturbation_type,
297	    batch_size=2,
298	    num_workers=0,
299	    dry_run=False,
300	    data_dir=None,
301	    seed=42,
302	):
303	    """Create DataLoader for a specific perturbation type.
304	
305	    Args:
306	        perturbation_type: one of visual/spatial/physical/universal
307	        dry_run: if True, use synthetic data
308	        data_dir: path to rollout .pt files (required if not dry_run)
309	    """
310	    if dry_run:
311	        dataset = SyntheticRolloutDataset(num_samples=100, seed=seed)
312	    else:
313	        if data_dir is None:
314	            raise ValueError("data_dir required for non-dry-run training")
315	        data_path = Path(data_dir)
316	        if not data_path.exists():
317	            raise FileNotFoundError(
318	                f"Rollout data directory not found: {data_path}. "
319	                f"Collect LIBERO-Plus rollout data first, or use --dry_run."
320	            )
321	        dataset = LIBERORolloutDataset(data_path, perturbation_type, seed=seed)
322	
323	    return DataLoader(
324	        dataset,
325	        batch_size=batch_size,
326	        shuffle=True,
327	        num_workers=num_workers,
328	        collate_fn=collate_observations,
329	        pin_memory=True,
330	        drop_last=True,
331	    )
332	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "85fafbbd-3b1a-4fa2-91cb-ba1ff976f257"
}
```

</details>

---


### System

_source line 61_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3acedec04983e0ad",
  "tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "description": "Searching for benchmark\\.get_benchmark_dict|suite\\.get_task|get…",
  "usage": {
    "total_tokens": 43614,
    "tool_uses": 11,
    "duration_ms": 13445
  },
  "last_tool_name": "Grep",
  "uuid": "c6bc5986-ae2c-49ca-9cbb-f510525eab80",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7"
}
```

---


### Tool call

_source line 62_

<details open><summary>🔧 Tool call — Grep · `toolu_01TWGYrKa6B54jspRsXG892C`</summary>

```json
{
  "pattern": "benchmark\\.get_benchmark_dict|suite\\.get_task|get_libero_path",
  "type": "py",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing",
  "output_mode": "content",
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "6764d40d-fd41-4f35-82a5-540a71e4ffa4",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Dt1mfY6Vk6hQwUXZVu5b9z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 6496,
      "cache_read_input_tokens": 37088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6496,
        "ephemeral_1h_input_tokens": 0
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

_source line 63 · 2026-05-15T17:50:36.585Z_

<details><summary>↩ Tool result · `toolu_01TWGYrKa6B54jspRsXG892C`</summary>

```text
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py-301-    indices = []
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py-302-    matched_names = []
artifacts/phase0/libero_integration.py-303-    for i in range(num_tasks):
artifacts/phase0/libero_integration.py:304:        task = suite.get_task(i)
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py-305-        name = getattr(task, "name", "") or getattr(task, "bddl_file", "")
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py-306-        classified = _classify_task(name)
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py-307-
--
artifacts/phase0/libero_integration.py-341-    Returns:
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py-342-        (env, task_description, init_states, selected_task_idx)
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py-343-    """
artifacts/phase0/libero_integration.py:344:    from libero.libero import benchmark, get_libero_path
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py-345-    from libero.libero.envs import OffScreenRenderEnv
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py-346-
artifacts/phase0/libero_integration.py:347:    benchmark_dict = benchmark.get_benchmark_dict()
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py-348-    suite = benchmark_dict[task_suite_name]()
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py-349-    num_tasks = suite.n_tasks
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py-350-
--
artifacts/phase0/libero_integration.py-355-    else:
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py-356-        selected_idx = random.choice(valid_indices)
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py-357-
artifacts/phase0/libero_integration.py:358:    task = suite.get_task(selected_idx)
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py-359-    task_description = task.language
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py-360-
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py-361-    task_bddl_file = (
artifacts/phase0/libero_integration.py:362:        Path(get_libero_path("bddl_files")) / task.problem_folder / task.bddl_file
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py-363-    )
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py-364-    env = OffScreenRenderEnv(
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py-365-        bddl_file_name=str(task_bddl_file),
--
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py-368-    )
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py-369-    env.seed(seed)
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py-370-
artifacts/phase0/libero_integration.py:371:    init_states = suite.get_task_init_states(selected_idx)
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py-372-    return env, task_description, init_states, selected_idx
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py-373-
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py-374-
--
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py-553-    log.info("Loading π₀ from %s", args.checkpoint)
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py-554-    policy = load_pi0_policy(args.checkpoint, device)
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py-555-
artifacts/phase1/collect_expert_demos.py:556:    from libero.libero import get_libero_path
artifacts/phase1/collect_expert_demos.py:557:    bddl_dir = os.path.join(get_libero_path("bddl_files"), BASE_TASK_SUITE)
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py-558-    tasks = find_base_tasks(bddl_dir, num_tasks=args.num_tasks)
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py-559-
artifacts/phase1/collect_expert_demos.py-560-    if not tasks:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "0c1fd1f3-4d7a-4aad-92ff-333c21a3ff1b"
}
```

</details>

---


### System

_source line 64_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3acedec04983e0ad",
  "tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "description": "Reading artifacts/_project/intermediate/configs.py",
  "usage": {
    "total_tokens": 43615,
    "tool_uses": 12,
    "duration_ms": 13901
  },
  "last_tool_name": "Read",
  "uuid": "0948c870-9a34-47c4-a71b-5ceae57bbd36",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7"
}
```

---


### Tool call

_source line 65_

<details open><summary>🔧 Tool call — Read · `toolu_01Kq24Zpw63cGPQFj3U9uBgr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/_project/intermediate/configs.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "eb608ec3-8dcc-4f88-91e8-310108af2322",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Dt1mfY6Vk6hQwUXZVu5b9z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 6496,
      "cache_read_input_tokens": 37088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6496,
        "ephemeral_1h_input_tokens": 0
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

_source line 66 · 2026-05-15T17:50:37.041Z_

<details><summary>↩ Tool result · `toolu_01Kq24Zpw63cGPQFj3U9uBgr`</summary>

```text
1	"""
2	Configuration constants for Meta-Brain Phase 0 perturbation classifier.
3	
4	Defines perturbation taxonomies, layer indices, model dimensions,
5	and hyperparameter defaults shared across collect/train/eval scripts.
6	"""
7	
8	# ---------------------------------------------------------------------------
9	# Perturbation taxonomy
10	# ---------------------------------------------------------------------------
11	
12	PERTURBATION_TYPES_6CLASS = {
13	    "camera_viewpoints": 0,
14	    "light_conditions": 1,
15	    "background_textures": 2,
16	    "sensor_noise": 3,
17	    "objects_layout": 4,
18	    "robot_initial_states": 5,
19	}
20	
21	PERTURBATION_TYPES_3CLASS = {
22	    "visual": 0,   # camera + light + background + noise
23	    "spatial": 1,  # layout
24	    "physical": 2, # robot
25	}
26	
27	CLASS_6_TO_3_MAPPING = {
28	    0: 0,  # camera_viewpoints   -> visual
29	    1: 0,  # light_conditions    -> visual
30	    2: 0,  # background_textures -> visual
31	    3: 0,  # sensor_noise        -> visual
32	    4: 1,  # objects_layout      -> spatial
33	    5: 2,  # robot_initial_states -> physical
34	}
35	
36	CLASS_6_NAMES = [
37	    "camera_viewpoints",
38	    "light_conditions",
39	    "background_textures",
40	    "sensor_noise",
41	    "objects_layout",
42	    "robot_initial_states",
43	]
44	
45	CLASS_3_NAMES = ["visual", "spatial", "physical"]
46	
47	BINARY_NAMES = ["nominal", "perturbed"]
48	
49	# ---------------------------------------------------------------------------
50	# π₀ architecture constants
51	# ---------------------------------------------------------------------------
52	
53	PALIGEMMA_LAYERS = [2, 4, 6, 8, 10, 12, 14, 16]
54	EXPERT_LAYERS = [2, 6, 10, 14]
55	
56	PALIGEMMA_HIDDEN_DIM = 2048
57	EXPERT_HIDDEN_DIM = 1024
58	
59	PALIGEMMA_NUM_LAYERS = 18  # layers[0..17]
60	EXPERT_NUM_LAYERS = 18
61	
62	# PyTorch module path templates
63	PALIGEMMA_LAYER_TEMPLATE = (
64	    "model.paligemma_with_expert.paligemma.language_model.layers.{i}"
65	)
66	EXPERT_LAYER_TEMPLATE = (
67	    "model.paligemma_with_expert.gemma_expert.model.layers.{i}"
68	)
69	
70	# ---------------------------------------------------------------------------
71	# Pooling strategies
72	# ---------------------------------------------------------------------------
73	
74	POOLING_STRATEGIES = ["mean", "first", "last", "first_last"]
75	
76	def pooling_output_dim(pooling: str, hidden_dim: int) -> int:
77	    """Return output dimension for a given pooling strategy."""
78	    if pooling == "first_last":
79	        return hidden_dim * 2
80	    return hidden_dim
81	
82	# ---------------------------------------------------------------------------
83	# Classifier defaults
84	# ---------------------------------------------------------------------------
85	
86	CLASSIFIER_HIDDEN_DIM = 256
87	DEFAULT_LR = 1e-3
88	DEFAULT_EPOCHS = 50
89	DEFAULT_BATCH_SIZE = 64
90	NUM_FOLDS = 5
91	
92	# Activation source → input dimension calculation
93	ACTIVATION_SOURCES = ["paligemma_only", "expert_only", "both"]
94	
95	def compute_input_dim(activation_source: str, pooling: str) -> int:
96	    """Compute classifier input dimension from source and pooling strategy."""
97	    pg_dim = len(PALIGEMMA_LAYERS) * pooling_output_dim(pooling, PALIGEMMA_HIDDEN_DIM)
98	    ex_dim = len(EXPERT_LAYERS) * pooling_output_dim(pooling, EXPERT_HIDDEN_DIM)
99	    if activation_source == "paligemma_only":
100	        return pg_dim
101	    elif activation_source == "expert_only":
102	        return ex_dim
103	    elif activation_source == "both":
104	        return pg_dim + ex_dim
105	    raise ValueError(f"Unknown activation_source: {activation_source}")
106	
107	# ---------------------------------------------------------------------------
108	# Sweep grid
109	# ---------------------------------------------------------------------------
110	
111	SWEEP_POOLINGS = ["mean", "first", "first_last"]
112	SWEEP_SOURCES = ["paligemma_only", "expert_only", "both"]
113	SWEEP_LRS = [1e-2, 1e-3, 1e-4]
114	
115	# ---------------------------------------------------------------------------
116	# Go / No-Go thresholds (Phase 0 success criteria)
117	# ---------------------------------------------------------------------------
118	
119	GO_NOGO = {
120	    "6class_accuracy_min": 0.50,   # >50% on 6-class (chance=16.7%)
121	    "3class_accuracy_min": 0.65,   # >65% on 3-class (chance=33.3%)
122	    "binary_accuracy_min": 0.80,   # >80% on binary (chance=50%)
123	    "binary_roc_auc_min": 0.85,
124	}
125	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "1560dcbb-ec63-4144-8405-b2fd91eaddbd"
}
```

</details>

---


### System

_source line 67_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3acedec04983e0ad",
  "tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "description": "Reading artifacts/_project/intermediate/configs_5dd29d.py",
  "usage": {
    "total_tokens": 43616,
    "tool_uses": 13,
    "duration_ms": 14149
  },
  "last_tool_name": "Read",
  "uuid": "b5ff26ac-a53a-4faa-ab5a-31fac19c3fb9",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7"
}
```

---


### Tool call

_source line 68_

<details open><summary>🔧 Tool call — Read · `toolu_01VCX2N9yHM56qnij52etNDS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/_project/intermediate/configs_5dd29d.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "9a1916c1-5579-459a-b7d3-7ecbbcbd1c13",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Dt1mfY6Vk6hQwUXZVu5b9z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 6496,
      "cache_read_input_tokens": 37088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6496,
        "ephemeral_1h_input_tokens": 0
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

_source line 69 · 2026-05-15T17:50:37.281Z_

<details><summary>↩ Tool result · `toolu_01VCX2N9yHM56qnij52etNDS`</summary>

```text
1	"""
2	Configuration constants for Meta-Brain Phase 0 perturbation classifier.
3	
4	Defines perturbation taxonomies, layer indices, model dimensions,
5	and hyperparameter defaults shared across collect/train/eval scripts.
6	"""
7	
8	# ---------------------------------------------------------------------------
9	# Perturbation taxonomy
10	# ---------------------------------------------------------------------------
11	
12	PERTURBATION_TYPES_6CLASS = {
13	    "camera_viewpoints": 0,
14	    "light_conditions": 1,
15	    "background_textures": 2,
16	    "sensor_noise": 3,
17	    "objects_layout": 4,
18	    "robot_initial_states": 5,
19	}
20	
21	PERTURBATION_TYPES_3CLASS = {
22	    "visual": 0,   # camera + light + background + noise
23	    "spatial": 1,  # layout
24	    "physical": 2, # robot
25	}
26	
27	CLASS_6_TO_3_MAPPING = {
28	    0: 0,  # camera_viewpoints   -> visual
29	    1: 0,  # light_conditions    -> visual
30	    2: 0,  # background_textures -> visual
31	    3: 0,  # sensor_noise        -> visual
32	    4: 1,  # objects_layout      -> spatial
33	    5: 2,  # robot_initial_states -> physical
34	}
35	
36	CLASS_6_NAMES = [
37	    "camera_viewpoints",
38	    "light_conditions",
39	    "background_textures",
40	    "sensor_noise",
41	    "objects_layout",
42	    "robot_initial_states",
43	]
44	
45	CLASS_3_NAMES = ["visual", "spatial", "physical"]
46	
47	BINARY_NAMES = ["nominal", "perturbed"]
48	
49	# ---------------------------------------------------------------------------
50	# π₀ architecture constants
51	# ---------------------------------------------------------------------------
52	
53	PALIGEMMA_LAYERS = [2, 4, 6, 8, 10, 12, 14, 16]
54	EXPERT_LAYERS = [2, 6, 10, 14]
55	
56	PALIGEMMA_HIDDEN_DIM = 2048
57	EXPERT_HIDDEN_DIM = 1024
58	
59	PALIGEMMA_NUM_LAYERS = 18  # layers[0..17]
60	EXPERT_NUM_LAYERS = 18
61	
62	# PyTorch module path templates
63	PALIGEMMA_LAYER_TEMPLATE = (
64	    "paligemma_with_expert.paligemma.language_model.layers.{i}"
65	)
66	EXPERT_LAYER_TEMPLATE = (
67	    "paligemma_with_expert.gemma_expert.model.layers.{i}"
68	)
69	
70	# ---------------------------------------------------------------------------
71	# Pooling strategies
72	# ---------------------------------------------------------------------------
73	
74	POOLING_STRATEGIES = ["mean", "first", "last", "first_last"]
75	
76	def pooling_output_dim(pooling: str, hidden_dim: int) -> int:
77	    """Return output dimension for a given pooling strategy."""
78	    if pooling == "first_last":
79	        return hidden_dim * 2
80	    return hidden_dim
81	
82	# ---------------------------------------------------------------------------
83	# Classifier defaults
84	# ---------------------------------------------------------------------------
85	
86	CLASSIFIER_HIDDEN_DIM = 256
87	DEFAULT_LR = 1e-3
88	DEFAULT_EPOCHS = 50
89	DEFAULT_BATCH_SIZE = 64
90	NUM_FOLDS = 5
91	
92	# Activation source → input dimension calculation
93	ACTIVATION_SOURCES = ["paligemma_only", "expert_only", "both"]
94	
95	def compute_input_dim(activation_source: str, pooling: str) -> int:
96	    """Compute classifier input dimension from source and pooling strategy."""
97	    pg_dim = len(PALIGEMMA_LAYERS) * pooling_output_dim(pooling, PALIGEMMA_HIDDEN_DIM)
98	    ex_dim = len(EXPERT_LAYERS) * pooling_output_dim(pooling, EXPERT_HIDDEN_DIM)
99	    if activation_source == "paligemma_only":
100	        return pg_dim
101	    elif activation_source == "expert_only":
102	        return ex_dim
103	    elif activation_source == "both":
104	        return pg_dim + ex_dim
105	    raise ValueError(f"Unknown activation_source: {activation_source}")
106	
107	# ---------------------------------------------------------------------------
108	# Sweep grid
109	# ---------------------------------------------------------------------------
110	
111	SWEEP_POOLINGS = ["mean", "first", "first_last"]
112	SWEEP_SOURCES = ["paligemma_only", "expert_only", "both"]
113	SWEEP_LRS = [1e-2, 1e-3, 1e-4]
114	
115	# ---------------------------------------------------------------------------
116	# Go / No-Go thresholds (Phase 0 success criteria)
117	# ---------------------------------------------------------------------------
118	
119	GO_NOGO = {
120	    "3class_go": 0.70,             # >70% 3-class + confusion off-diag <30% → GO
121	    "3class_augment": 0.50,        # 50-70% → AUGMENT (add proprioception + visual change)
122	    "6class_viable": 0.50,         # >50% 6-class → finer-grained routing viable
123	    "binary_roc_auc_sanity": 0.75, # ≥0.75 → activations encode perturbation signal
124	    "confusion_max_offdiag": 0.30, # any off-diagonal cell must be <30%
125	}
126	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "7c5d864d-1eaa-4e0a-8f51-f019da448a0e"
}
```

</details>

---


### System

_source line 70_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3acedec04983e0ad",
  "tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "description": "Searching for new_objects|distractor",
  "usage": {
    "total_tokens": 49127,
    "tool_uses": 14,
    "duration_ms": 17151
  },
  "last_tool_name": "Grep",
  "uuid": "4d005c54-96ed-4c49-83a8-bd805952f016",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7"
}
```

---


### Tool call

_source line 71_

<details open><summary>🔧 Tool call — Grep · `toolu_01VmLDuNF9XEj382q7mccqCi`</summary>

```json
{
  "pattern": "new_objects|distractor",
  "type": "py",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing",
  "output_mode": "content",
  "context": 4
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "a8ccbcab-c0b0-451c-8f2a-be07eb1e58a0",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NPEe9bJGNb9NVBoyX6qNt7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5507,
      "cache_read_input_tokens": 43584,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5507,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 72 · 2026-05-15T17:50:40.301Z_

<details><summary>↩ Tool result · `toolu_01VmLDuNF9XEj382q7mccqCi`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "ee05a5b8-132f-4ed9-8fa6-71c36fde9ab6"
}
```

</details>

---


### System

_source line 73_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3acedec04983e0ad",
  "tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "description": "Reading phase1/train_lora_expert.py",
  "usage": {
    "total_tokens": 49129,
    "tool_uses": 15,
    "duration_ms": 17511
  },
  "last_tool_name": "Read",
  "uuid": "a4893779-d31d-455b-9256-e48023041a5f",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7"
}
```

---


### Tool call

_source line 74_

<details open><summary>🔧 Tool call — Read · `toolu_01Lf7bsrsaju2RQZT3Vsz1TR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/phase1/train_lora_expert.py",
  "limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "76052228-f564-4bc8-acd0-5f06a916cb4f",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NPEe9bJGNb9NVBoyX6qNt7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5507,
      "cache_read_input_tokens": 43584,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5507,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 75 · 2026-05-15T17:50:40.644Z_

<details><summary>↩ Tool result · `toolu_01Lf7bsrsaju2RQZT3Vsz1TR`</summary>

```text
1	"""
2	Phase 1 LoRA Expert Training for Meta-Brain Perturbation-Adaptive Routing.
3	
4	Trains perturbation-specific LoRA adapters on frozen pi0 base model using
5	flow-matching action prediction loss. Each adapter specializes in one
6	perturbation type (visual/spatial/physical) or all types (universal).
7	
8	Input:
9	    - pi0_base checkpoint: /root/autodl-tmp/checkpoints/pi0_base/model.safetensors
10	    - LIBERO-Plus rollout data (or synthetic for --dry_run)
11	Output:
12	    - PEFT LoRA adapter in /root/meta_brain_lora_routing/checkpoints/lora_{type}_r16/
13	
14	Usage:
15	    # Dry-run (validate model loading, LoRA injection, forward/backward)
16	    python phase1/train_lora_expert.py --perturbation_type visual --gpu_id 0 --dry_run
17	
18	    # Full training (4 GPUs in parallel, one adapter per GPU)
19	    python phase1/train_lora_expert.py --perturbation_type visual   --gpu_id 0 &
20	    python phase1/train_lora_expert.py --perturbation_type spatial  --gpu_id 1 &
21	    python phase1/train_lora_expert.py --perturbation_type physical --gpu_id 2 &
22	    python phase1/train_lora_expert.py --perturbation_type universal --gpu_id 3 &
23	
24	Dependencies: torch, peft, safetensors, wandb, openpi (PI0Pytorch model)
25	"""
26	
27	import sys
28	
29	sys.path.insert(0, "/root/openpi/src")
30	
31	import argparse
32	import logging
33	import math
34	import os
35	import time
36	from pathlib import Path
37	
38	import safetensors.torch
39	import torch
40	import wandb
41	from peft import LoraConfig, get_peft_model
42	
43	import openpi.models.pi0_config as pi0_config
44	import openpi.models_pytorch.pi0_pytorch as pi0_pytorch
45	
46	sys.path.insert(0, str(Path(__file__).resolve().parent))
47	from data_loader import VisualAugmentation, create_dataloader
48	
49	log = logging.getLogger(__name__)
50	
51	# LoRA targets: PaliGemma attention Q/K/V/O on all 18 layers.
52	# Regex must fullmatch against module paths from model.named_modules().
53	# Excludes action expert (gemma_expert) -- Phase 0 showed it doesn't encode
54	# perturbation differences.
55	PALIGEMMA_ATTN_REGEX = (
56	    r"paligemma_with_expert\.paligemma\.model\.language_model\."
57	    r"layers\.\d+\.self_attn\.(q|k|v|o)_proj"
58	)
59	
60	PERTURBATION_TYPES = ["visual", "spatial", "physical", "universal"]
61	
62	DEFAULT_CHECKPOINT = "/root/autodl-tmp/checkpoints/pi0_base"
63	DEFAULT_OUTPUT_DIR = "/root/meta_brain_lora_routing/checkpoints"
64	
65	
66	def parse_args():
67	    p = argparse.ArgumentParser(
68	        description="Train perturbation-specific LoRA adapter on frozen pi0"
69	    )
70	    p.add_argument(
71	        "--perturbation_type",
72	        required=True,
73	        choices=PERTURBATION_TYPES,
74	    )
75	    p.add_argument("--gpu_id", type=int, default=0)
76	    p.add_argument(
77	        "--dry_run",
78	        action="store_true",
79	        help="Run 2 steps with synthetic data to validate code path",
80	    )
81	
82	    g = p.add_argument_group("model")
83	    g.add_argument("--checkpoint", default=DEFAULT_CHECKPOINT)
84	    g.add_argument("--output_dir", default=DEFAULT_OUTPUT_DIR)
85	
86	    g = p.add_argument_group("lora")
87	    g.add_argument("--lora_rank", type=int, default=16)
88	    g.add_argument("--lora_alpha", type=int, default=32)
89	    g.add_argument("--lora_dropout", type=float, default=0.05)
90	
91	    g = p.add_argument_group("training")
92	    g.add_argument("--lr", type=float, default=2e-4)
93	    g.add_argument("--batch_size", type=int, default=2)
94	    g.add_argument("--num_train_steps", type=int, default=30000)
95	    g.add_argument("--warmup_steps", type=int, default=100)
96	    g.add_argument("--log_interval", type=int, default=50)
97	    g.add_argument("--save_interval", type=int, default=1000)
98	    g.add_argument("--eval_interval", type=int, default=500)
99	    g.add_argument("--grad_clip_norm", type=float, default=1.0)
100	    g.add_argument("--weight_decay", type=float, default=0.01)
101	    g.add_argument(
102	        "--patience",
103	        type=int,
104	        default=3,
105	        help="Early stop after N eval checkpoints without improvement",
106	    )
107	
108	    g = p.add_argument_group("wandb")
109	    g.add_argument("--wandb_project", default="meta_brain_lora_routing")
110	    g.add_argument("--no_wandb", action="store_true")
111	
112	    g = p.add_argument_group("data")
113	    g.add_argument(
114	        "--data_dir", default="/root/meta_brain_lora_routing/rollouts"
115	    )
116	    g.add_argument("--seed", type=int, default=42)
117	
118	    return p.parse_args()
119	
120	
121	def setup_logging():
122	    handler = logging.StreamHandler()
123	    handler.setFormatter(
124	        logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", datefmt="%H:%M:%S")
125	    )
126	    handler.flush = lambda: handler.stream.flush()
127	    logging.root.addHandler(handler)
128	    logging.root.setLevel(logging.INFO)
129	
130	
131	# ---------------------------------------------------------------------------
132	# Model loading
133	# ---------------------------------------------------------------------------
134	
135	
136	def load_pi0_model(checkpoint_path, device):
137	    """Load PI0Pytorch model and weights from safetensors checkpoint."""
138	    log.info("Creating PI0 model (gemma_2b + gemma_300m)...")
139	    config = pi0_config.Pi0Config(
140	        dtype="bfloat16",
141	        action_dim=32,
142	        action_horizon=50,
143	    )
144	    model = pi0_pytorch.PI0Pytorch(config)
145	
146	    model_path = os.path.join(checkpoint_path, "model.safetensors")
147	    log.info(f"Loading weights from {model_path}...")
148	    safetensors.torch.load_model(model, model_path)
149	    model = model.to(device)
150	    log.info("PI0 model loaded")
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "d0494068-49ac-4e6e-90e7-76dd85f530cc"
}
```

</details>

---


### System

_source line 76_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3acedec04983e0ad",
  "tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "description": "Running find /home/ubuntu/.agent-ml-research-be-idea-gen-…",
  "usage": {
    "total_tokens": 51531,
    "tool_uses": 16,
    "duration_ms": 19931
  },
  "last_tool_name": "Bash",
  "uuid": "7053d29c-ac81-41bf-8ebf-f16f1fb089b3",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7"
}
```

---


### Tool call

_source line 77_

<details open><summary>🔧 Tool call — Bash · `toolu_01B9b1Sd5a4uKbLKr35GU6bL`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing -type f \\( -name \"README*\" -o -name \"*.md\" \\) 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "26ec2722-ff6b-4399-a7f3-def9bc6af84b",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01L1mcGC8DB3rmdKaPyK4UKN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2392,
      "cache_read_input_tokens": 49091,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2392,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 78 · 2026-05-15T17:50:43.221Z_

<details><summary>↩ Tool result · `toolu_01B9b1Sd5a4uKbLKr35GU6bL`</summary>

```text
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/docs/IDEA_BRIEF.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/task_context/agent.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/memory.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/report.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/AGENTS.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/.claude/sessions/reviewer_e812f902/CLAUDE.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/.claude/sessions/reviewer_e812f902/AGENTS.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/.claude/sessions/agent_69d1ca07/CLAUDE.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/.claude/sessions/agent_69d1ca07/AGENTS.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/.claude/sessions/director_3525982a/CLAUDE.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/.claude/sessions/director_3525982a/AGENTS.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/.claude/CLAUDE.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/_project/report/phase0_experiment_spec.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/README.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/dream_reports/dream_20260515T154653/median/review_report.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/dream_reports/dream_20260515T154653/median/paper_framing.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/dream_reports/dream_20260515T154653/worst/review_report.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/dream_reports/dream_20260515T154653/worst/paper_framing.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/dream_reports/dream_20260515T154653/best/review_report.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/dream_reports/dream_20260515T154653/best/paper_framing.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "9bc4598b-ccf9-48bd-9ebe-44aef7dd38ad"
}
```

</details>

---


### System

_source line 79_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3acedec04983e0ad",
  "tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "description": "Finding **/*.md",
  "usage": {
    "total_tokens": 51536,
    "tool_uses": 17,
    "duration_ms": 20222
  },
  "last_tool_name": "Glob",
  "uuid": "e80948ee-6a8f-48a6-b21c-da8dba8fe237",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7"
}
```

---


### Tool call

_source line 80_

<details open><summary>🔧 Tool call — Glob · `toolu_01RqSEp4x8DVXG4iDKBREiL7`</summary>

```json
{
  "pattern": "**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "d88c63af-7bfb-426b-89fc-a0ff99c28a45",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01L1mcGC8DB3rmdKaPyK4UKN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2392,
      "cache_read_input_tokens": 49091,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2392,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 81 · 2026-05-15T17:50:43.364Z_

<details><summary>↩ Tool result · `toolu_01RqSEp4x8DVXG4iDKBREiL7`</summary>

```text
artifacts/openpi_research_report.md
artifacts/phase0/README.md
artifacts/_project/report/phase0_experiment_spec.md
artifacts/phase0_experiment_spec.md
docs/IDEA_BRIEF.md
task_context/agent.md
artifacts/dream_reports/dream_20260515T154653/best/paper_framing.md
artifacts/dream_reports/dream_20260515T154653/median/paper_framing.md
artifacts/dream_reports/dream_20260515T154653/worst/paper_framing.md
memory.md
artifacts/dream_reports/dream_20260515T154653/best/review_report.md
report.md
artifacts/dream_reports/dream_20260515T154653/median/review_report.md
artifacts/dream_reports/dream_20260515T154653/worst/review_report.md
paper_framing.md
ROADMAP.md
.claude/sessions/reviewer_e812f902/CLAUDE.md
.claude/sessions/reviewer_e812f902/AGENTS.md
.claude/sessions/agent_69d1ca07/CLAUDE.md
.claude/sessions/agent_69d1ca07/AGENTS.md
.claude/CLAUDE.md
AGENTS.md
.claude/sessions/director_3525982a/CLAUDE.md
.claude/sessions/director_3525982a/AGENTS.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "b36403a7-0b16-45eb-a62d-3252d95e37e8"
}
```

</details>

---


### System

_source line 82_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3acedec04983e0ad",
  "tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "description": "Reading docs/IDEA_BRIEF.md",
  "usage": {
    "total_tokens": 53068,
    "tool_uses": 18,
    "duration_ms": 21922
  },
  "last_tool_name": "Read",
  "uuid": "47da353e-4c90-475a-a940-fa70255d05a6",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7"
}
```

---


### Tool call

_source line 83_

<details open><summary>🔧 Tool call — Read · `toolu_01A1xLWqNqjdZz4k8jWgsHM6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/docs/IDEA_BRIEF.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "4a66dae9-3d53-4ee6-86e8-7ec156f4183e",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012wRJPBGaXRjiuE7Hx37qDh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1530,
      "cache_read_input_tokens": 51483,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1530,
        "ephemeral_1h_input_tokens": 0
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


### System

_source line 84_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3acedec04983e0ad",
  "tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "description": "Reading artifacts/phase0/README.md",
  "usage": {
    "total_tokens": 53069,
    "tool_uses": 19,
    "duration_ms": 22133
  },
  "last_tool_name": "Read",
  "uuid": "7eb1f9b8-0974-41f6-8370-afcd8c60c917",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7"
}
```

---


### Tool call

_source line 85_

<details open><summary>🔧 Tool call — Read · `toolu_013oq3hPqLhDvH4qGePGiU1C`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/README.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "c386dd7d-d5eb-416d-8065-4f840c99e5c3",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012wRJPBGaXRjiuE7Hx37qDh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1530,
      "cache_read_input_tokens": 51483,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1530,
        "ephemeral_1h_input_tokens": 0
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

_source line 86 · 2026-05-15T17:50:45.270Z_

<details><summary>↩ Tool result · `toolu_013oq3hPqLhDvH4qGePGiU1C`</summary>

````text
1	# Meta-Brain Phase 0: Perturbation Classifier on π₀ Activations
2	
3	Validates whether frozen π₀ internal activations contain sufficient signal to distinguish perturbation types in LIBERO-Plus — a prerequisite for downstream LoRA routing.
4	
5	## Pipeline
6	
7	```
8	collect_activations.py → train_classifier.py → eval_classifier.py
9	```
10	
11	### 1. Collect activations
12	
13	```bash
14	# All 6 perturbation types (50 episodes each)
15	python collect_activations.py \
16	    --checkpoint /path/to/pi0_base \
17	    --output_dir ./activations \
18	    --perturbation_type all \
19	    --num_episodes 50 \
20	    --device cuda:0
21	
22	# Nominal baseline (100 episodes)
23	python collect_activations.py \
24	    --checkpoint /path/to/pi0_base \
25	    --output_dir ./activations \
26	    --perturbation_type nominal \
27	    --num_episodes 100
28	```
29	
30	Output: `activations/{camera_viewpoints,light_conditions,...,nominal}.pt`
31	
32	Each `.pt` file is a list of dicts with keys:
33	- `activations`: `{layer_name: {pooling_type: tensor(fp16)}}`
34	- `label_6class`, `label_3class`, `label_binary`: int labels
35	- `metadata`: episode info (task, steps, success)
36	
37	Incremental: run collection per perturbation type across sessions — files append automatically.
38	
39	### 2. Train classifier
40	
41	```bash
42	# Single config
43	python train_classifier.py \
44	    --data_dir ./activations \
45	    --mode 6class \
46	    --activation_source both \
47	    --pooling mean \
48	    --lr 1e-3 \
49	    --output_dir ./models
50	
51	# Full sweep (27 configs: 3 pooling × 3 source × 3 lr)
52	python train_classifier.py \
53	    --data_dir ./activations \
54	    --mode 6class \
55	    --sweep \
56	    --output_dir ./models
57	```
58	
59	Each config saves `best_model.pt` + `result.json` under `models/&lt;config_name>/`.
60	
61	### 3. Evaluate
62	
63	```bash
64	# Single model
65	python eval_classifier.py \
66	    --model_path ./models/6class__mean__both__lr0.001/best_model.pt \
67	    --data_dir ./activations \
68	    --mode 6class \
69	    --activation_source both \
70	    --pooling mean \
71	    --output_dir ./eval_results
72	
73	# Per-layer breakdown (which layers carry the most signal)
74	python eval_classifier.py \
75	    --model_path ./models/6class__mean__both__lr0.001/best_model.pt \
76	    --data_dir ./activations \
77	    --mode 6class \
78	    --activation_source both \
79	    --pooling mean \
80	    --per_layer \
81	    --output_dir ./eval_results
82	
83	# Sweep leaderboard
84	python eval_classifier.py \
85	    --sweep_results_dir ./models \
86	    --mode 6class \
87	    --output_dir ./eval_results
88	```
89	
90	Outputs:
91	- `classification_report.txt` — per-class precision/recall/F1
92	- `confusion_matrix.png` + `.csv` — normalized confusion matrix
93	- `roc_curve.png` + `pr_curve.png` — (binary mode only)
94	- `tsne.png` — activation space visualization
95	- `per_layer_accuracy.png` + `.json` — layer-level informativeness
96	- `sweep_leaderboard_{mode}.csv` — all configs ranked by accuracy
97	
98	## Architecture
99	
100	**π₀ hooks** (12 layers total):
101	- PaliGemma LLM: layers {2,4,6,8,10,12,14,16} — hidden_dim=2048
102	- Action Expert: layers {2,6,10,14} — hidden_dim=1024
103	
104	**Classifier**: 2-layer MLP, hidden_dim=256, dropout=0.3
105	
106	**Input dimensions** (with mean/first/last pooling):
107	- `paligemma_only`: 8×2048 = 16,384
108	- `expert_only`: 4×1024 = 4,096
109	- `both`: 20,480
110	
111	With `first_last` pooling, dimensions double.
112	
113	## Perturbation Taxonomy
114	
115	| 6-class | 3-class | Binary |
116	|---------|---------|--------|
117	| camera_viewpoints | visual (0) | perturbed (1) |
118	| light_conditions | visual (0) | perturbed (1) |
119	| background_textures | visual (0) | perturbed (1) |
120	| sensor_noise | visual (0) | perturbed (1) |
121	| objects_layout | spatial (1) | perturbed (1) |
122	| robot_initial_states | physical (2) | perturbed (1) |
123	| *(nominal)* | — | nominal (0) |
124	
125	## Go/No-Go Thresholds
126	
127	| Mode | Minimum Accuracy | Notes |
128	|------|-----------------|-------|
129	| 6-class | 50% | chance = 16.7% |
130	| 3-class | 65% | chance = 33.3% |
131	| Binary | 80% accuracy, 0.85 AUC | chance = 50% |
132	
133	## Dependencies
134	
135	```
136	torch
137	safetensors
138	scikit-learn
139	matplotlib
140	numpy
141	openpi          # π₀ model loading
142	libero          # LIBERO-Plus environment
143	```
144	
145	Optional: `umap-learn` for UMAP visualization.
146	
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "c9c557bb-48f8-4630-88be-3d01e91e4290"
}
```

</details>

---


### Tool result

_source line 87 · 2026-05-15T17:50:45.310Z_

<details><summary>↩ Tool result · `toolu_01A1xLWqNqjdZz4k8jWgsHM6`</summary>

```text
1	# Idea Brief: Meta-Brain: Perturbation-Adaptive LoRA Routing for Robust Vision-Language-Action Models
2	
3	
4	- **Idea ID**: `idea_007`
5	- **Created**: 2026-05-15
6	- **Approved**: 2026-05-15
7	- **Source**: foreign:be-idea-gen-0509-15
8	- **Level**: top-tier
9	
10	## Seed Topic
11	
12	按照以下方向，生成1-2个优质idea，保质不求量：Seed 3: Meta-Brain — LLM Role-Switching as Adaptive Robustness Controller for VLA
13	Target: CoRL 2026 (Austin, Nov 9–12, 2026). Abstract deadline 2026-05-26 (12 days from today 2026-05-14); paper deadline 2026-05-29 (15 days).
14	Direction: LLM-as-Meta-Brain for VLA robustness — an architecture where a frozen LLM dynamically switches between specialized roles (perception enhancement, logic decomposition, anomaly intervention) and feeds unified modified visual tokens back to a VLA backbone, enabling robust operation across diverse perturbation scenarios without retraining the VLA. The core motivation is that different robustness failures require qualitatively different interventions: visual noise needs perceptual re-grounding, ambiguous instructions need task decomposition, and execution uncertainty needs reflective error correction. Rather than training a single monolithic robust VLA, we leverage the LLM's pre-existing world knowledge and reasoning capabilities as an external "meta-brain" that diagnoses the current failure mode and provides targeted representational guidance. The key architectural innovation is a Unified Representation Interface: regardless of which role the LLM assumes, it outputs through a shared Adapter into a fixed-dimensional token modification that directly reshapes the VLA's visual tokens — this means the VLA backbone sees the same token format but with role-specific semantic content baked in. This avoids the fragility of language-mediated VLA guidance (which breaks under paraphrasing) and instead operates in continuous representation space.
15	Recent landscape (do not duplicate): SOMA: Strategic Orchestration and Memory-Augmented System for Vision-Language-Action Model Robustness via In-Context Adaptation
16	CoRAL: Contact-Rich Adaptive LLM-Based Control for Robotic Manipulation
17	VLA-Pilot: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion
18	Observing and Controlling Features in Vision-Language-Action Models
19	ON ROBUSTNESS OF VISION-LANGUAGE-ACTION MODEL AGAINST MULTI-MODAL PERTURBATIONS
20	STRONG-VLA: Decoupled Robustness Learning for Vision-Language-Action Models under Multimodal Perturbations
21	ControlVLA: Few-shot Object-centric Adaptation for Pre-trained Vision-Language-Action Models
22	Contribution type: METHOD ONLY. A three-component architecture: (1) Role Router — a lightweight classifier on top of the VLA's current state embedding that detects the perturbation regime: high visual entropy → perception mode, high instruction ambiguity → logic mode, high action uncertainty → intervention mode. Trained with meta-learning across perturbation types. (2) Role-Conditioned Adapter — a shared Adapter between the frozen LLM and VLA that outputs one of three representation modalities through the same interface: (a) Hybrid Semantic Tokens — role-conditioned embedding vectors that reshape visual tokens to emphasize task-relevant features; (b) Function Prefix — a role embedding prepended to the modified tokens that biases VLA attention heads toward the appropriate processing mode; (c) Attention Mask — a spatial weight matrix that gates visual token importance (suppress distractors, enhance depth features, highlight skill-relevant objects). (3) Dynamic Skill Library — when the meta-brain's intervention produces a novel solution pattern, it is distilled into a reusable skill embedding stored persistently; future encounters of similar perturbations route directly to the skill without full LLM inference. Training: two-phase — Phase 1 trains the Adapter with meta-learning across role-switching datasets; Phase 2 trains end-to-end with the VLA backbone frozen, optimizing only the Router + Adapter for action prediction under perturbation.
23	EVAL PROTOCOL — IMPORTANT:
24	TRAIN on standard LIBERO suites (Object/Spatial/Goal/Long/90).
25	EVALUATE on existing LIBERO-PLUS / LIBERO-PRO style perturbation benchmarks (and similar community-released robustness benchmark series). DO NOT spend time constructing your own robustness benchmark — use existing perturbation suites and route the budget into the method.
26	Report robustness gap (Δ between nominal LIBERO success and perturbed-suite success) AND nominal preservation (must not regress on base LIBERO).
27	Additionally report: per-perturbation-type breakdown (visual/language/action noise) with role activation frequency, latency overhead of meta-brain inference, ablation of individual roles and combined system.
28	Experiments can be extended to CALVIN or RLBench perturbation variants to verify cross-benchmark robustness and role generalization.
29	SIM-ONLY MITIGATION: Robustness eval in sim is well-accepted at CoRL — established LIBERO-PLUS / LIBERO-PRO style suites are a recognized sim-only pattern. The meta-brain architecture operates on representations, not physical hardware, making sim evaluation methodologically sufficient.
30	HARD CONSTRAINTS:
31	Compute: ≤200 H100-hours total. LLM is frozen (e.g., Qwen-2.5-7B or LLaMA-3-8B); VLA backbone is frozen (OpenVLA/SmolVLA/OpenPi/π0 checkpoint). Only train Router (~2M params) + Adapter (~15M params). Show the math: Adapter training ≈ 50 H100-hrs, Router meta-learning ≈ 30 H100-hrs, evaluation ≈ 40 H100-hrs.
32	Time: ≤20 days. Build on OpenVLA, OpenPi and other proper codebases, LeRobot, HF Transformers. LLM integration via HuggingFace model loading.
33	Eval datasets: LIBERO base (training/nominal eval) + LIBERO-PLUS / LIBERO-PRO and similar existing perturbation suites (perturbed eval). No custom benchmark construction.
34	Look for: meta-learning for role router that generalizes to unseen perturbation types, unified adapter architecture that maps heterogeneous LLM guidance into a common token-modification interface, attention masking as a differentiable robustness mechanism, skill library as amortized robustness (one-time LLM cost → reusable embedding), theoretical connections between role diversity and minimax robustness over perturbation sets. Avoid: language-only LLM guidance that is itself fragile to paraphrasing, requiring LLM inference at every VLA timestep (must amortize via skill caching), plain ensembling of multiple VLAs, custom robustness benchmark construction, approaches requiring real-robot data for the meta-brain training.
35	Tag: direction=robust_vla, contribution_type=method, sub_direction=meta_brain_role_switching, target_venues=["CoRL 2026"].
36	
37	## Core Problem
38	
39	Vision-Language-Action (VLA) models achieve >90% success on standard LIBERO benchmarks but suffer catastrophic performance drops under perturbation: π₀ falls from >90% nominal to 53.6% average on LIBERO-Plus, with camera perturbations at 13.8% and robot initial-state perturbations at 6.0%. This brittleness stems from VLAs memorizing fixed vision-action mappings rather than developing genuine environmental understanding. Critically, different perturbation types disrupt different processing stages: visual perturbations (camera, lighting) corrupt early visual token representations, spatial perturbations (object rearrangement) invalidate learned action trajectories, and physical perturbations (object mass, friction) break force-compliance assumptions. Current robustness methods either address a single perturbation modality (FTM for visual, AFI for spatial, AnyCamVLA for camera viewpoint) or apply uniform correction across all perturbation types (RobustVLA's adversarial training, VLA-GSE's per-token capacity routing), leaving a fundamental question unanswered: does perturbation-type-aware diagnostic routing outperform one-size-fits-all adaptation?
40	
41	## Opportunity / Why Now
42	
43	Four concurrent lines of evidence from 2025-2026 converge to make perturbation-adaptive internal correction newly feasible: (1) SAFE (NeurIPS 2025) demonstrates that VLA intermediate activations encode rich, task-generic signals about execution state — a lightweight MLP on frozen features achieves SOTA failure detection across unseen tasks with <1% overhead, proving that perturbation-relevant information is extractable from VLA internals; (2) Linear probing of OpenVLA (Geier et al., 2502.04558) shows >0.90 accuracy for spatial object states and relations across layers 1-32 of the LLM backbone, establishing that spatial information sufficient for correction is linearly accessible; (3) Feature steering on π₀.₅ and OpenVLA (Buurmeijer et al., 2603.05487) demonstrates that minimal linear interventions on internal representations can reliably steer robot behavior with ~100% constraint satisfaction while preserving closed-loop task performance — proving that the representations are not just readable but controllable; (4) VLA-GSE (2605.06175) achieves 81.2% on LIBERO-Plus with spectral MoE routing using 114M trainable parameters on Qwen3-VL-4B, demonstrating that expert routing on frozen VLA backbones is highly effective — but its per-token capacity routing is perturbation-agnostic, leaving room for perturbation-diagnostic routing as an orthogonal design dimension. Together, these findings establish that VLA internals contain sufficient perturbation-diagnostic information AND that lightweight internal interventions can correct behavior without disrupting the frozen backbone's capabilities.
44	
45	## Landscape (SOTA & Limitations)
46	
47	The VLA robustness landscape in early 2026 features complementary but incomplete solutions across seven categories:
48	
49	**Single-modality correction:** FTM/FLA (Li et al., 2512.02902) achieves 87-91% viewpoint recovery via visual token modulation with only 4K-4.7M parameters — highly efficient for visual perturbations but architecturally limited to recalibrating ViT outputs, with no mechanism for spatial or physical corrections. AFI (Chen et al., 2512.07472) achieves +20.2% on LIBERO-PRO through external 3D Spatial Affordance Fields that detect 'memory traps' via proprioception and propose affordance-driven waypoints — effective for spatial perturbations but requires an external geometric module and does not address visual or physical perturbations. AnyCamVLA (Heo et al., 2603.05868) provides zero-shot camera adaptation via feed-forward novel view synthesis, achieving 94.5% average success under camera perturbations by virtually transforming test-time observations to match training camera configuration — a plug-and-play visual-specific solution requiring no fine-tuning but limited to camera viewpoint changes.
50	
51	**Multi-modal but uniform correction:** RobustVLA (ICLR 2026, 2510.00037) formulates multi-perturbation robustness as a multi-armed bandit problem, achieving +12.6% on π₀ across 17 perturbation types. However, it applies a single adversarial training strategy uniformly, potentially underperforming on perturbations that require qualitatively different corrections.
52	
53	**Capacity-based expert routing (perturbation-agnostic):** VLA-GSE (2605.06175) decomposes frozen VLA weights via SVD into generalized (shared) and specialized (routed) experts, achieving 81.2% on LIBERO-Plus with 114M trainable parameters (2.51% of model) on Qwen3-VL-4B. VLA-GSE uses top-2 per-token gating across 7 specialized + 1 generalized expert per block for capacity allocation. This is the current strongest parameter-efficient method on LIBERO-Plus but routes by input-dependent capacity needs, not by perturbation type — the same routing configuration handles camera perturbations (64.4%) and layout perturbations (82.6%) without perturbation-type awareness. Importantly, VLA-GSE's standard LoRA baseline on the same Qwen3-VL-4B backbone achieves 69.2%, providing a controlled reference for the value of routing (+12.0% over LoRA).
54	
55	**Capacity-based LoRA adaptation:** LoRA-SP (2603.07404) adapts LoRA rank per layer and per input on π₀ and SmolVLA via an SVD-style parameterization with a small router whose nonnegative scores act as singular values over a shared vector bank. The active rank set is selected by an energy threshold on cumulative squared scores, discovering that vision towers require the highest ranks while language layers remain low and stable. On real-robot manipulation tasks, LoRA-SP matches or exceeds full fine-tuning with far fewer trainable parameters and improves multi-task success by up to 31.6% over standard LoRA. LoRA-SP adapts HOW MUCH LoRA capacity to allocate (adaptive rank); Meta-Brain adapts WHAT TYPE of correction to apply (perturbation-specific experts). These are orthogonal dimensions that could be composed — adaptive rank within each perturbation-specific expert — representing a natural extension.
56	
57	**Task-based LoRA routing (not perturbation-based):** CORAL (2603.09298) freezes the VLA backbone and attaches one LoRA expert per task, with a language-based manager routing instructions to experts. MoIRA (2507.01843) routes LoRA experts on π₀/GR00T-N1 using text-based similarity for task specialization. Both achieve strong multi-task performance but route by task identity/instruction — they cannot distinguish or adapt to different perturbation types within the same task.
58	
59	**Spatial-aware VLA architectures:** SpatialVLA (2501.15830) injects 3D position encodings into VLA input, achieving 88.2% on LIBERO-Spatial; Spatial Forcing (ICLR 2026, 2510.12276) aligns intermediate VLA representations with 3D foundation model features, achieving 98.5% on standard LIBERO and 3.8× training speedup — both enhance spatial understanding at training time but are complementary to, not competitive with, post-hoc perturbation correction on frozen backbones. CorridorVLA (2604.21241) uses explicit spatial anchor constraints to guide action generation; its GR00T-Corr variant achieves 83.21% on the LIBERO-Plus dataset, though reported by task category (Long/Goal/Object/Spatial) rather than by perturbation type (Camera/Robot/Light/Background/Noise/Layout), making direct per-perturbation comparison with VLA-GSE or Meta-Brain's target metrics not straightforward. CorridorVLA demonstrates that spatial corrections at the action-planning level via explicit geometric constraints are feasible and effective.
60	
61	**Test-time adaptation:** PDF (2604.18107) achieves +7.4% on LIBERO via test-time perturbation learning with delayed feedback — a lightweight perturbation head adjusts action logits using REINFORCE-style optimization guided by post-action observations, requiring no fine-tuning. PDF and Meta-Brain are complementary: training-time LoRA routing (Meta-Brain) for strong per-perturbation-type correction + test-time adaptation (PDF) for novel perturbation instances.
62	
63	**VLA internal analysis:** SAFE (NeurIPS 2025, 2506.09937) probes VLA final-layer activations for binary failure detection using a 2-layer MLP (hidden dim 256, 2.3M params), achieving 78.0% ROC-AUC on unseen tasks. Probing work (2502.04558) extracts symbolic spatial states. Feature steering (2603.05487) demonstrates behavioral control through linear interventions on end-effector position and gripper state, achieving ~100% constraint satisfaction. These works establish feasibility but stop at detection/analysis — none close the loop from perturbation diagnosis to targeted correction.
64	
65	**Gap:** No existing method combines (a) perturbation-type detection from VLA internals with (b) type-specific corrective adaptation. VLA-GSE routes by input capacity (perturbation-agnostic); LoRA-SP adapts rank per layer/input (capacity-agnostic to perturbation type); MoIRA/CORAL route by task instruction; PDF adapts at test-time without perturbation classification. Meta-Brain uniquely routes corrective LoRA experts by diagnosed perturbation type, testing the hypothesis that perturbation-aware specialization achieves comparable robustness gains at dramatically fewer trainable parameters through targeted correction rather than capacity expansion.
66	
67	## Proposed Approach
68	
69	**Meta-Brain** is a modular correction framework for frozen VLA backbones (π₀, π₀-FAST) comprising four components. The design departs from the user's original specification of an external frozen LLM (Qwen-2.5-7B) as 'meta-brain' with role-switching and a Unified Representation Interface. Through iterative analysis (Rounds 1-3), we determined that internal LoRA routing on the VLA's own backbone is superior for this problem: it avoids the prohibitive cross-model embedding alignment problem between an external LLM and the VLA's learned representation space, eliminates external LLM inference latency (critical for real-time control at 10-50Hz), and preserves the perturbation-adaptive routing insight from the original specification while simplifying the architecture. The 'meta-brain' concept is retained as the Perturbation-Adaptive Router — a lightweight internal module that fulfills the original spec's goal of diagnosing the perturbation type and orchestrating a type-specific response.
70	
71	**Phase 0: Early-Kill Validation Gate (Days 1-4).**
72	Before committing to the full training pipeline, we validate the core assumption: that perturbation types are classifiable from π₀ internal activations. Procedure: (a) Roll out frozen π₀ on a subset of LIBERO-Plus tasks under all 7 perturbation categories (~200 rollouts). Record intermediate activations at layers 4, 8, 12, 16, 20, 24, 28, 32. (b) Train 2-layer MLP classifier (hidden dim 256) on mean-pooled activations for 3-class perturbation-type classification (visual / spatial / physical). (c) Report classification accuracy. GO/NO-GO criterion: if accuracy >70%, proceed to full pipeline. If 50-70%, augment router inputs with proprioception history and visual change detection features, re-evaluate (Days 5-6 reserved as contingency). If <50%, pivot to universal LoRA + Correction Memory (dropping perturbation-type routing). This gate costs ~5 H100-hrs (from buffer) and prevents wasting 185 H100-hrs on a falsified premise. Evidence supporting feasibility: SAFE achieves 78.0% ROC-AUC for binary failure detection from the same activations using the same architecture (2-layer MLP, hidden 256), and 3-class perturbation type classification is a coarser signal than binary failure prediction, so should be easier.
73	
74	**1. Perturbation-Adaptive Router (PAR).**
75	Inspired by SAFE's demonstration that VLA internals encode execution-relevant signals, PAR trains lightweight classifiers (2-layer MLP, hidden dim 256, following SAFE's architecture) on intermediate activations from the frozen VLA backbone. Unlike SAFE's binary failure detection, PAR performs multi-class perturbation-type classification (visual / spatial / physical / nominal) with soft routing weights. The router operates on mean-pooled hidden states from layers selected via Phase 0 validation (following SAFE's aggregation protocol, evaluating first-token, last-token, mean, and first+last pooling strategies). PAR outputs a perturbation-type probability distribution p(type | h_l) used to softly weight LoRA expert contributions. PAR is trained with cross-entropy loss; optionally, meta-learning (Reptile across perturbation types) can improve generalization to unseen perturbation instances, at ~10 additional H100-hrs.
76	
77	**2. Adaptive LoRA Bank (ALB).**
78	Three perturbation-specific LoRA experts (rank 16) are applied to the attention layers of the frozen LLM backbone:
79	- **Visual LoRA (LoRA-V):** Corrects visual distribution shifts (camera viewpoint, lighting, background texture). Positioned on early-to-mid LLM layers where visual tokens are first integrated, analogous to FTM's visual recalibration but operating at the cross-modal fusion level rather than ViT output. For camera-only deployments, AnyCamVLA's zero-shot approach is more efficient; LoRA-V's value is unified handling of camera + lighting + background within the routing framework.
80	- **Spatial LoRA (LoRA-S):** Corrects spatial rearrangement perturbations (object repositioning, initial state changes). LoRA-S targets representational recalibration — biasing attention patterns toward correct spatial features under rearranged configurations — rather than explicit trajectory replanning. The mechanistic justification rests on converging evidence at two levels. At the representational level: Geier et al. (2502.04558) show >0.90 probing accuracy for spatial object relations across LLM layers, confirming spatial state is linearly encoded; Buurmeijer et al. (2603.05487) demonstrate that linear interventions on π₀.₅ achieve ~100% constraint satisfaction for end-effector position and gripper state. At the architectural level: LoRA-S operates on mid-to-late attention layers where spatial-action mappings are computed, modifying the query-key-value projections that determine how spatial token representations are attended to during trajectory planning. This is mechanistically distinct from simply shifting a spatial feature — it alters the attention patterns through which the model routes spatial information into action predictions. However, we acknowledge that for perturbations requiring qualitatively different trajectories (e.g., navigating around a repositioned obstacle rather than merely recalibrating spatial feature attention), representational-level correction may be insufficient — such cases likely require explicit 3D geometric reasoning as demonstrated by AFI's external affordance fields. The Phase 0 validation gate partially tests whether representational-level correction is sufficient: if PAR can classify spatial perturbations from internal activations, this indicates the backbone encodes the perturbation signal, but the adequacy of LoRA-level correction for trajectory-altering spatial changes remains an empirical question resolved in the ablation phase. Hence our pre-planned pivot to hybrid AFI integration if LoRA-S underperforms.
81	- **Physical LoRA (LoRA-P):** Corrects physical property changes (object mass, friction, deformability). Targets late LLM layers near action decoding.
82	
83	Expert outputs are combined via PAR's soft routing weights: h_corrected = h_frozen + Σ_k p(type_k) · LoRA_k(h_frozen), enabling smooth interpolation when perturbation types co-occur.
84	
85	Total trainable parameters: ~6M (3 × rank-16 LoRA experts at ~1.5M each + PAR at ~0.5M). This count excludes Correction Memory, which adds only a single learned scalar (α) and a non-parametric FAISS index. Note that Meta-Brain's fixed-rank experts could be further enhanced by composing with LoRA-SP's adaptive rank allocation within each perturbation-specific expert — a natural extension where LoRA-SP determines how much capacity each expert allocates per layer/input while Meta-Brain determines which expert type to activate.
86	
87	**3. Correction Memory (CM).**
88	A retrieval-augmented module that stores embeddings of (perturbation_context, correction_outcome, perturbation_type_label) tuples from successful training rollouts. CM's injection mechanism uses routing-weight modulation rather than cross-attention or prefix tokens: at inference, CM retrieves the k-nearest correction exemplars (k=5) based on cosine similarity between the current PAR activation embedding and stored perturbation context embeddings via a FAISS index. The retrieval results modulate PAR's routing distribution by injecting a correction bias derived from the perturbation-type labels of retrieved exemplars:
89	
90	  p_refined(type_k) = softmax(logits_PAR + α · Σ_j sim_j · one_hot(type_k^j))
91	
92	where sim_j is the cosine similarity of the j-th retrieved exemplar, type_k^j is its perturbation-type label, and α is a single learned scaling parameter. This mechanism biases routing toward experts that succeeded on historically similar perturbation instances, providing few-shot adaptation to novel perturbation instances within a known type without requiring additional model parameters. The design is motivated by two considerations: (a) it avoids the architectural mismatch of injecting retrieved embeddings via cross-attention into LoRA's additive weight perturbation framework, and (b) it elegantly connects CM to the routing pathway rather than creating a parallel conditioning channel. The FAISS index is CPU-bound at inference with <1ms lookup latency, adding no GPU overhead.
93	
94	**4. Training Protocol (18-Day Schedule for CoRL 2026, 2 researchers: 1 lead, 1 supporting).**
95	
96	The schedule is organized into three tiers of deliverables with graceful degradation:
97	- **Tier 1 (abstract submission, Day 12):** Phase 0 validation + LoRA training results + projected ablation plan. Does NOT require full routing validation or Correction Memory results.
98	- **Tier 2 (full paper submission, Day 15):** Main ablation ladder (a-d) + FTM comparison (e). Routing assembly and end-to-end evaluation must be complete.
99	- **Tier 3 (supplementary / camera-ready):** Additional ablations (f-h: CM ablation, router architecture comparison, layer placement). These are deferred if schedule slips without compromising the core contribution.
100	
101	**Detailed Schedule:**
102	- **Days 1-2 (May 15-16):** Setup π₀ + LIBERO-Plus environment using OpenPI codebase. Begin Phase 1 data collection: roll out frozen π₀ under all 7 perturbation categories, recording intermediate activations. ~500 rollouts with activation recording. [GPU 0-3 parallel rollouts, 15 H100-hrs] (Lead: environment setup; Support: data collection scripts)
103	- **Days 3-4 (May 17-18):** Phase 0 validation gate: train PAR classifier on collected activations, evaluate 3-class accuracy. Hyperparameter sweep: 3 pooling strategies × 4 layer subsets × 3 learning rates = 36 runs (<15 min each). GO/NO-GO decision by end of Day 4. [5 H100-hrs] (Lead: PAR training; Support: analysis scripts + begin paper skeleton)
104	- **Days 5-6 (May 19-20):** If Phase 0 GO (>70%): begin LoRA expert training (overlaps with Days 7-8). If Phase 0 AUGMENT (50-70%): implement router augmentation with proprioception history and visual change detection, re-evaluate PAR by end of Day 6. This 2-day contingency buffer a
105	
106	## Resource Estimate
107	
108	- **Timeline**: 15 working days primary (May 15-29) + 3 days Tier 3 (May 30 - Jun 1) with 4× H100 node. Team: 2 researchers (1 lead: architecture + experiments, 1 support: infrastructure + paper + baselines). Targeting CoRL 2026 (abstract May 26, paper May 29).
109	- **breakdown**: {'buffer': {'detail': 'Unexpected reruns, debugging, infrastructure issues. Reduced from 15 hrs since Phase 0 contingency is now explicitly budgeted separately.', 'h100_hours': 10}, 'phase0_contingency': {'detail': 'Contingency buffer for router augmentation if Phase 0 accuracy is 50-70%. Implement proprioception history features and visual change detection, retrain PAR. If >70% after augmentation, proceed to LoRA training on Day 7. If still <50%, pivot to universal LoRA + CM. This 2-day buffer prevents the augmentation path from delaying LoRA training.', 'h100_hours': 5, 'wall_days': 'Days 5-6 (only if Phase 0 result is 50-70%)'}, 'phase0_validation': {'detail': 'Early-kill gate: collect π₀ activations on LIBERO-Plus perturbation subset (~200 rollouts), train 2-layer MLP classifier (matching SAFE architecture: hidden 256), report 3-class accuracy. 36 hyperparameter configurations × <15 min each. GO/NO-GO decision by end of Day 4. Budget drawn from buffer.', 'h100_hours': 5, 'wall_days': 'Days 3-4'}, 'phase1_data_collection': {'detail': 'Roll out frozen π₀ on LIBERO-Plus under all 7 perturbation categories. Collect intermediate activations at layers 4, 8, 12, 16, 20, 24, 28, 32. ~500 rollouts × 7 perturbation types. Parallelized across 4 GPUs for ~4 hrs wall time. Uses OpenPI codebase with existing LIBERO configs.', 'h100_hours': 15, 'wall_days': 'Days 1-2'}, 'phase2_par_router': {'detail': 'Train perturbation classifier (2-layer MLP) on frozen activations. Full hyperparameter sweep after Phase 0 GO decision: 3 pooling strategies × 4 layer subsets × 3 learning rates = 36 runs. Each run <15 min on single H100.', 'h100_hours': 10, 'wall_days': 'Days 3-6 (overlaps with Phase 0 + contingency)'}, 'phase3_lora_experts': {'detail': '3 perturbation-specific LoRA experts (rank 16, attention layers) trained in parallel on 3 GPUs — one per perturbation type. ~18 H100-hrs each including per-expert hyperparameter tuning (rank {8,16,32} × layer subset × lr). GPU 4 runs universal LoRA baseline (ablation b) simultaneously. Wall time: ~20 hrs via 3-way parallelism.', 'h100_hours': 55, 'wall_days': 'Days 7-9'}, 'phase4_correction_memory_and_routing': {'detail': 'Populate Correction Memory FAISS index from successful training rollouts (5 H100-hrs). Assemble PAR + ALB + CM routing-modulation, end-to-end routing fine-tuning with frozen LoRA parameters (15 H100-hrs). FAISS index construction is CPU-bound. CM adds only 1 learned parameter (α scaling).', 'h100_hours': 20, 'wall_days': 'Days 10-11'}, 'phase5_tier2_experiments': {'detail': 'Tier 2 ablation ladder parallelized across 4 GPUs: (a) Frozen baseline eval: 3 hrs. (b) Universal LoRA eval: 5 hrs. (c) Meta-Brain full eval: 5 hrs. (d) Oracle routing eval: 5 hrs. (e) FTM reproduction: 10 hrs. Additional evaluation on LIBERO-PRO: 10 hrs. 10 seeds × key conditions. Wall time: ~13 hrs via 4-GPU parallelism.', 'h100_hours': 50, 'wall_days': 'Days 12-14'}, 'phase6_tier3_experiments': {'detail': 'Tier 3 ablations: (f) CM ablation: 5 hrs. (g) Router architecture comparison: 5 hrs. (h) Layer placement: 5 hrs. (i) Optional cross-backbone Qwen3-VL-4B experiment: 10 hrs (only if time permits). These are deferred to supplementary/camera-ready without compromising core contribution.', 'h100_hours': 20, 'wall_days': 'Days 16-18 (deferred if schedule slips)'}, 'phase7_paper_writing': {'detail': 'Paper skeleton begins Day 4 (Support researcher). Abstract submitted Day 12 (May 26, CoRL abstract deadline) using Phase 0 + LoRA training results + projected ablation plan. Full paper by Day 15 (May 29, CoRL paper deadline) with Tier 2 ablation results (a-e). Tier 3 results added to camera-ready if available.', 'h100_hours': 0, 'wall_days': 'Days 4-15 (overlaps with experiments)'}}
110	- **note**: Budget assumes π₀ backbone is frozen throughout — no backbone training cost. All LoRA training operates on <2M trainable parameters per expert (~6M total). LIBERO simulation runs on CPU alongside GPU training. OpenPI codebase provides existing π₀ + LIBERO training configs and LoRA fine-tuning support, eliminating setup overhead. Pure compute: 190 H100-hrs ÷ 4 GPUs = 48 GPU-hrs ≈ 2 days. Sequential pipeline dependencies + debugging + paper writing extend to 15-18 days. Tiered delivery ensures graceful degradation: Tier 1 (abstract) requires only Phase 0 + LoRA results; Tier 2 (paper) requires ablations a-e; Tier 3 (supplementary) contains additional ablations f-i.
111	- **total_h100_hours**: 190
112	
113	## Key References
114	
115	- {'id': '2605.06175', 'name': 'VLA-GSE', 'role': 'Secondary reference point (different backbone). Achieves 81.2% on LIBERO-Plus with 114M trainable params on Qwen3-VL-4B, demonstrating that expert routing on frozen VLA backbones is highly effective. Standard LoRA baseline on the same backbone: 69.2% (+12.0% from routing). Per-perturbation: Camera 64.4%, Robot 68.5%, Light 97.3%, Background 97.3%, Noise 79.4%, Layout 82.6%. Uses top-2 per-token gating across 7 specialized + 1 generalized expert per block — perturbation-agnostic capacity routing. Meta-Brain explores whether perturbation-diagnostic routing achieves comparable gains-over-LoRA at 20× fewer parameters through targeted specialization. Cross-backbone comparison (π₀ vs Qwen3-VL-4B) is acknowledged as confounded; gain-over-baseline metric enables contextualized comparison.'}
116	- {'id': '2603.07404', 'name': 'LoRA-SP', 'role': 'Capacity-based LoRA adaptation on π₀ and SmolVLA. Adapts LoRA rank per layer and per input via SVD-style parameterization with a small router whose nonneg scores act as singular values over a shared vector bank. Discovers that vision towers require highest ranks while language layers remain low. Matches or exceeds full fine-tuning on real-robot tasks with far fewer parameters, improving multi-task success by up to 31.6% over standard LoRA. Key distinction from Meta-Brain: LoRA-SP adapts HOW MUCH capacity to allocate (adaptive rank); Meta-Brain adapts WHAT TYPE of correction to apply (perturbation-specific experts). These orthogonal dimensions could be composed — adaptive rank within each perturbation-specific expert.'}
117	- {'id': '2604.18107', 'name': 'PDF (Test-Time Perturbation Learning)', 'role': 'Complementary test-time approach achieving +7.4% on standard LIBERO via uncertainty-based augmentation and delayed-feedback perturbation head on OpenVLA. No fine-tuning required. Meta-Brain and PDF address orthogonal deployment phases: training-time LoRA routing for strong per-type correction vs. test-time adaptation for zero-cost deployment. A Meta-Brain + PDF pipeline is a natural combination.'}
118	- {'id': '2603.05868', 'name': 'AnyCamVLA', 'role': "Zero-shot camera adaptation via feed-forward novel view synthesis, achieving 94.5% under camera perturbations. Plug-and-play with no fine-tuning. Overlaps with LoRA-V's visual perturbation correction for camera viewpoints specifically. Meta-Brain's LoRA-V additionally handles lighting and background perturbations; AnyCamVLA is superior for camera-only deployment. Complementary visual-specific approach."}
119	- {'id': '2512.07472', 'name': 'AFI', 'role': "Primary spatial-perturbation competitor. Achieves +20.2% LIBERO-PRO via external 3D Spatial Affordance Fields on frozen π₀/π₀.₅. Provides the upper bound for spatial perturbation correction and the pivot target if LoRA-S proves insufficient. Meta-Brain is the internal, multi-perturbation complement to AFI's external, spatial-specific approach."}
120	- {'id': '2506.09937', 'name': 'SAFE (NeurIPS 2025)', 'role': "Foundational evidence that VLA internals encode task-generic execution signals extractable by lightweight probes. Uses 2-layer MLP (hidden 256) on final-layer activations, achieving 78.0% ROC-AUC for binary failure detection on unseen tasks with 2.3M parameters. Directly motivates PAR's architecture (identical MLP design, extended to multi-class) and Phase 0 validation protocol. SAFE detects failure; PAR classifies perturbation type and routes to correction."}
121	- {'id': '2507.01843', 'name': 'MoIRA', 'role': 'Closest architectural analog — LoRA expert routing on π₀/GR00T-N1. Key difference: MoIRA routes by task instruction (text similarity); Meta-Brain routes by perturbation type (internal activation classification). Orthogonal routing dimensions.'}
122	- {'id': '2512.02902', 'name': 'FTM/FLA', 'role': 'Strongest simplicity baseline. Achieves ~90% visual robustness with 4K parameters via token modulation. Meta-Brain must demonstrate value beyond FTM for visual perturbations AND justify the routing overhead by additionally handling spatial/physical perturbations.'}
123	- {'id': '2603.05487', 'name': 'Feature Steering (Buurmeijer et al.)', 'role': 'Mechanistic evidence for internal correction feasibility. Linear interventions on π₀.₅/OpenVLA representations achieve ~100% constraint satisfaction for end-effector position and gripper state while maintaining >90% task success. Validates that LoRA-level corrections can manipulate spatial representations. Limitation: tested on standard tasks, not on rearranged-object scenarios — the harder spatial perturbation case remains empirically unvalidated.'}
124	- {'id': '2502.04558', 'name': 'VLA Probing (Geier et al.)', 'role': 'Probing evidence: >0.90 accuracy for spatial object states/relations across LLM layers 1-32. Confirms spatial information is linearly encoded and accessible for correction.'}
125	- {'id': '2603.19183', 'name': 'SAE-VLA', 'role': 'Sparse autoencoders reveal steerable motion primitives in VLA representations. Complementary evidence that VLA internals contain interpretable, controllable features beyond what linear probes capture.'}
126	- {'id': '2510.00037', 'name': 'RobustVLA (ICLR 2026)', 'role': 'Multi-modal perturbation baseline. Achieves +12.6% on π₀ across 17 perturbation types via uniform adversarial training. Meta-Brain hypothesizes type-specific routing outperforms this uniform approach.'}
127	- {'id': '2603.09298', 'name': 'CORAL', 'role': 'Task-based LoRA routing on frozen VLA. Demonstrates that per-task LoRA isolation outperforms joint fine-tuning. Motivates LoRA bank architecture but routes by task, not perturbation.'}
128	- {'id': '2510.13626', 'name': 'LIBERO-Plus', 'role': 'Primary evaluation benchmark (CVPR 2026). Defines 7 perturbation categories for systematic VLA robustness evaluation. Current SOTA: SRPO 82.1%, VLA-GSE 81.2%, CorridorVLA 83.21% (by task category, not per-perturbation), OpenVLA-OFT+ 79.6%, AVA-VLA 74.7%, MergeVLA 72.2%, π₀ frozen baseline 53.6%.'}
129	- {'id': '2510.03827', 'name': 'LIBERO-PRO', 'role': 'Secondary evaluation benchmark. Tests generalization across object positions, initial states, instructions, and environments.'}
130	- {'id': '2511.09516', 'name': 'MAP-VLA', 'role': 'Memory-augmented VLA prompting using learnable soft prompts as prefix tokens, retrieved via trajectory similarity. Inspires Correction Memory concept but uses a different injection mechanism: MAP-VLA prepends retrieved prompts as prefix tokens; CM modulates router probability distributions via retrieval similarity. Both are plug-and-play on frozen backbones.'}
131	- {'id': '2511.15605', 'name': 'SRPO', 'role': 'Current LIBERO-Plus SOTA at 82.1% (by perturbation category) via self-referential RL policy optimization using latent world model progress signals. Uses full RL training (not parameter-efficient), representing the upper bound for what VLA adaptation can achieve on this benchmark.'}
132	- {'id': '2604.21241', 'name': 'CorridorVLA', 'role': "Demonstrates explicit spatial constraints (anchor-defined corridors) can guide VLA action generation. GR00T-Corr achieves 83.21% on the LIBERO-Plus dataset, but reported by task category (Long 74.55%, Goal 85.75%, Object 88.4%, Spatial 84.14%) rather than by perturbation type (Camera/Robot/Light/Background/Noise/Layout), so direct per-perturbation comparison with VLA-GSE or Meta-Brain's target metrics is not straightforward. Evidence that spatial corrections at the action-planning level via explicit geometric constraints are feasible and effective."}
133	- {'id': '2510.12276', 'name': 'Spatial Forcing (ICLR 2026)', 'role': 'Aligns intermediate VLA representations with 3D foundation model features during training, achieving 98.5% on standard LIBERO and 3.8× training speedup. Shows that spatial representation quality directly impacts action precision. Complementary training-time strategy; Meta-Brain operates post-hoc on frozen backbones.'}
134	
135	## Reviewer Evaluation
136	
137	**Scores**:
138	  - clarity: **{'rationale': "Exceptionally well-structured across all dimensions: comprehensive 17-reference landscape with per-competitor differentiation, clean ablation ladder with explicit falsification criteria and pivot strategies, honest framing of cross-backbone confounds (VLA-GSE comparison), detailed per-phase compute accounting, and the CM routing-modulation mechanism is now precisely specified. Among the clearest VLA robustness proposals I've reviewed.", 'score': 5}**/5
139	  - feasibility: **{'rationale': 'Phase 0 validation gate at Day 3-4 is excellent risk management. Tiered delivery (abstract needs only Phase 0 + LoRA results; Tier 3 deferred to camera-ready) provides realistic contingency. 190 H100-hrs with 4×H100 is tight but the compute math is internally consistent. The 2-day contingency buffer and pre-planned pivots (AFI hybrid for spatial, universal LoRA + CM if routing fails) demonstrate mature project management.', 'score': 4}**/5
140	  - impact: **{'rationale': 'The routing principle (perturbation-type-specific correction > universal correction) is a useful design insight, but the target performance (72-80% on LIBERO-Plus) lands below current SOTA (SRPO 82.1%, CorridorVLA 83.21%, VLA-GSE 81.2%). The parameter efficiency argument (6M vs 114M) is strong but may not fully compensate for the absolute performance gap in reviewer reception. Sim-only evaluation is accepted at CoRL but limits practical impact claims.', 'score': 3}**/5
141	  - novelty: **{'rationale': 'Perturbation-type-aware diagnostic routing is a genuinely new routing dimension, orthogonal to all existing work (task-based: MoIRA/CORAL, capacity-based: VLA-GSE, rank-based: LoRA-SP). The CM routing-modulation mechanism adds secondary novelty. Components are borrowed (SAFE-style probing, LoRA, MoE routing) but the combination and the specific hypothesis it tests are novel.', 'score': 4}**/5
142	
143	
144	## MVP Validation Results
145	
146	- **Date**: 2026-05-15
147	- **Hypothesis Supported**: Yes
148	
149	### Key Metrics
150	
151	3-class macro-F1: 0.993 (threshold 0.70) | Binary ROC-AUC: 1.0 (threshold 0.85) | K=1 few-shot F1: 0.898 | Layer 6 K=1 F1: 1.0 | Best router: PaliGemma layer 6, mean pooling | PaliGemma signal: 98.8% vs Action Expert: 75.9%
152	
153	### Summary
154	
155	Phase 0 early-kill gate 通过。在 LIBERO-Plus 6 种扰动（camera/light/background/noise/layout/robot）上，从 π₀ PaliGemma 冻结激活中提取特征，训练 2-layer MLP 分类器。3-class (Visual/Spatial/Physical) macro-F1=0.993（阈值 0.70），binary ROC-AUC=1.0（阈值 0.85）。关键发现：PaliGemma layer 6 单层即可完美分类，Action Expert 仅 75.9%。Few-shot K=1 单次前向 F1=0.898，layer 6 K=1 达到 1.0，证明路由器在线推理可行。
156	
157	### Recommendation
158	
159	GO — 核心假设（扰动类型可从 VLA 冻结激活分类）得到强有力验证。Router 架构确定：PaliGemma layer 6 单层，mean pooling。进入 Phase 1 LoRA expert 训练。
160	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "60dc922f-032d-4793-b20d-fef526de395a"
}
```

</details>

---


### System

_source line 88_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3acedec04983e0ad",
  "tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "description": "Running grep -r \"task_suite_name\\|libero_spatial\\|libero_…",
  "usage": {
    "total_tokens": 66764,
    "tool_uses": 20,
    "duration_ms": 25245
  },
  "last_tool_name": "Bash",
  "uuid": "20adf7e5-80f3-4e18-b2e0-7f5f1cfe8871",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7"
}
```

---


### Tool call

_source line 89_

<details open><summary>🔧 Tool call — Bash · `toolu_01LZaLbe4hQq2vyAyCdRL9J8`</summary>

```json
{
  "command": "grep -r \"task_suite_name\\|libero_spatial\\|libero_object\\|libero_goal\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing --include=\"*.py\" 2>/dev/null | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "178149e4-9244-489c-99f5-735c1e8088c0",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TZv2gpqFeThh3sMjFBnJbH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1706,
      "cache_creation_input_tokens": 11994,
      "cache_read_input_tokens": 53013,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11994,
        "ephemeral_1h_input_tokens": 0
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

_source line 90 · 2026-05-15T17:50:48.431Z_

<details><summary>↩ Tool result · `toolu_01LZaLbe4hQq2vyAyCdRL9J8`</summary>

```text
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py:MAX_STEPS = 220  # libero_spatial default
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py:# 10 base tasks in libero_spatial (no perturbation suffix)
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py:BASE_TASK_SUITE = "libero_spatial"
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py:    """Find base (unperturbed) BDDL files in libero_spatial.
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py:    "libero_spatial": 220,
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py:    "libero_object": 280,
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py:    "libero_goal": 300,
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py:    task_suite_name: str = "libero_spatial",
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py:    suite = benchmark_dict[task_suite_name]()
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py:    task_suite: str = "libero_spatial",
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py:        task_suite_name=task_suite,
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/collect_activations.py:        "--task_suite", type=str, default="libero_spatial",
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/collect_activations.py:        choices=["libero_spatial", "libero_object", "libero_goal", "libero_10", "libero_90"],
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "06b60bdb-0f23-4ea2-b3eb-e6cd00ca843c"
}
```

</details>

---


### System

_source line 91_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3acedec04983e0ad",
  "tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "description": "Searching for load_bddl_file|save_bddl_file",
  "usage": {
    "total_tokens": 66765,
    "tool_uses": 21,
    "duration_ms": 25802
  },
  "last_tool_name": "Grep",
  "uuid": "e7834cb8-b37d-4937-af1b-efa36069db84",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7"
}
```

---


### Tool call

_source line 92_

<details open><summary>🔧 Tool call — Grep · `toolu_01A5VpdZ1JpJPm8Mxczr9aih`</summary>

```json
{
  "pattern": "load_bddl_file|save_bddl_file",
  "type": "py",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing",
  "output_mode": "content",
  "context": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "7a893441-f82a-4b45-83b3-1beb2f39924f",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TZv2gpqFeThh3sMjFBnJbH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1706,
      "cache_creation_input_tokens": 11994,
      "cache_read_input_tokens": 53013,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11994,
        "ephemeral_1h_input_tokens": 0
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

_source line 93 · 2026-05-15T17:50:48.948Z_

<details><summary>↩ Tool result · `toolu_01A5VpdZ1JpJPm8Mxczr9aih`</summary>

```text
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py-245-    sys.path.insert(0, "/root/LIBERO-plus/libero")
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py-246-    from libero.randomizer.bddl_operators import (
artifacts/phase1/collect_expert_demos.py:247:        load_bddl_file,
artifacts/phase1/collect_expert_demos.py:248:        save_bddl_file,
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py-249-        perturb_region_info,
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py-250-    )
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py-251-
artifacts/phase1/collect_expert_demos.py:252:    spec = load_bddl_file(base_bddl_path)
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py-253-    delta_xy = perturbation_config["delta_xy"]
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py-254-    delta_half = perturbation_config["delta_half_len"]
--
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py-267-    dx, dy = delta_xy
artifacts/phase1/collect_expert_demos.py-268-    filename = f"{base_name}_spatial_dx{dx:.2f}_dy{dy:.2f}.bddl"
artifacts/phase1/collect_expert_demos.py:269:    _, filepath = save_bddl_file(spec, bddl_filename=filename, bddl_dirpath=output_dir)
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py-270-    return filepath
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py-271-
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "3e59b700-502a-45ba-a457-2b158ae19adb"
}
```

</details>

---


### System

_source line 94_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a3acedec04983e0ad",
  "tool_use_id": "toolu_01AAzcHk6Tcmrn7a4QSKE2eu",
  "status": "completed",
  "output_file": "",
  "summary": "Explore LIBERO-Plus _add mechanism",
  "usage": {
    "total_tokens": 68635,
    "tool_uses": 21,
    "duration_ms": 49925
  },
  "uuid": "fa1b9c32-b2c1-48c0-8c7c-b2efa03f8847",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7"
}
```

---


### Tool result

_source line 95 · 2026-05-15T17:51:13.055Z_

<details><summary>↩ Tool result · `toolu_01AAzcHk6Tcmrn7a4QSKE2eu`</summary>

````text
Excellent! Now let me create a comprehensive summary document by gathering all the findings:

## Summary

Based on my thorough search of the project, here's what I found regarding your three questions about LIBERO-Plus:

### 1. How _add_N tasks work in LIBERO-Plus

**Task Naming Convention:**
The `_add_N` suffix is used to denote **objects_layout** perturbations in LIBERO-Plus task names. According to the classification logic in `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py` (lines 256, 283):

```python
# From _classify_task():
if re.search(r"_add_\d+$", task_name) or re.search(r"_level\d+", task_name):
    return "objects_layout"
```

This pattern matches tasks like:
- `task_name_add_0`
- `task_name_add_1`
- `task_name_level0`, `task_name_level1`, etc.

**What _add_N means:**
- `_add_N` tasks represent **spatial/layout perturbations** where objects are placed in different positions than the nominal configuration
- These are distinct from the other 6 perturbation types: camera_viewpoints, light_conditions, background_textures, sensor_noise, and robot_initial_states
- They fall under the broader **"spatial" class** (along with other layout/positioning changes)

**Distinguishing _add from other layouts:**
The code filters out base tasks that contain perturbation suffixes including `_add_\d+` to isolate nominal/unperturbed tasks (see lines 188-192 of collect_expert_demos.py).

---

### 2. How perturb_region_info() is currently used

**Location and Import:**
Found in `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py` (lines 236-270):

```python
from libero.randomizer.bddl_operators import (
    load_bddl_file,
    save_bddl_file,
    perturb_region_info,
)
```

**Current Usage Pattern:**
The `perturb_region_info()` function is used in the `create_spatial_bddl()` function for **spatial perturbation generation**:

```python
def create_spatial_bddl(
    base_bddl_path: str,
    perturbation_config: dict,
    output_dir: str,
) -> str:
    """Create a perturbed BDDL file by applying spatial perturbation to all regions.
    
    Returns the path to the new BDDL file.
    """
    spec = load_bddl_file(base_bddl_path)
    delta_xy = perturbation_config["delta_xy"]
    delta_half = perturbation_config["delta_half_len"]
    delta_yaw = perturbation_config["delta_yaw"]

    # Apply perturbation to ALL regions in the BDDL spec
    for i in range(len(spec.region_infos)):
        spec.region_infos[i] = perturb_region_info(
            spec.region_infos[i],
            delta_region_centroid_xy=delta_xy,
            delta_region_half_len=delta_half,
            delta_yaw_rotation=delta_yaw,
        )

    # Save modified BDDL
    os.makedirs(output_dir, exist_ok=True)
    base_name = Path(base_bddl_path).stem
    dx, dy = delta_xy
    filename = f"{base_name}_spatial_dx{dx:.2f}_dy{dy:.2f}.bddl"
    _, filepath = save_bddl_file(spec, bddl_filename=filename, bddl_dirpath=output_dir)
    return filepath
```

**What it does:**
- Takes a base BDDL file and applies **3D geometric transformations** to object placement regions:
  - `delta_region_centroid_xy`: shifts region center by (dx, dy) in the XY plane
  - `delta_region_half_len`: adjusts the region's half-length (size)
  - `delta_yaw_rotation`: rotates regions by delta_yaw radians

**Spatial Perturbation Grid:**
The project defines 10 predefined configurations (lines 60-71 of collect_expert_demos.py):

```python
SPATIAL_PERTURBATION_CONFIGS = [
    {"delta_xy": ( 0.05,  0.00), "delta_half_len": 0.0,  "delta_yaw": (0.0, 0.0)},
    {"delta_xy": (-0.05,  0.00), "delta_half_len": 0.0,  "delta_yaw": (0.0, 0.0)},
    {"delta_xy": ( 0.00,  0.05), "delta_half_len": 0.0,  "delta_yaw": (0.0, 0.0)},
    # ... 7 more configurations with varying magnitude
]
```

These magnitudes (±0.05m shifts, ±0.3 radian rotations) are chosen to be "noticeable but within feasible reach of the robot."

---

### 3. What the benchmark API looks like for loading _add tasks

**Core LIBERO-Plus Benchmark API:**
From `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py` (lines 333-373):

```python
def create_libero_env(
    task_suite_name: str = "libero_spatial",
    perturbation_type: str | None = None,
    task_idx: int | None = None,
    seed: int = 42,
) -> tuple[Any, str, np.ndarray, int]:
    """Create a LIBERO / LIBERO-Plus evaluation environment.

    Returns:
        (env, task_description, init_states, selected_task_idx)
    """
    # 1. Get benchmark dictionary
    from libero.libero import benchmark, get_libero_path
    from libero.libero.envs import OffScreenRenderEnv

    benchmark_dict = benchmark.get_benchmark_dict()
    suite = benchmark_dict[task_suite_name]()
    num_tasks = suite.n_tasks

    # 2. Filter tasks by perturbation type
    valid_indices = _get_task_indices(suite, perturbation_type, num_tasks)

    # 3. Select task
    if task_idx is not None and task_idx in valid_indices:
        selected_idx = task_idx
    else:
        selected_idx = random.choice(valid_indices)

    # 4. Load task metadata
    task = suite.get_task(selected_idx)
    task_description = task.language

    # 5. Load BDDL file
    task_bddl_file = (
        Path(get_libero_path("bddl_files")) / task.problem_folder / task.bddl_file
    )

    # 6. Create environment
    env = OffScreenRenderEnv(
        bddl_file_name=str(task_bddl_file),
        camera_heights=256,
        camera_widths=256,
    )
    env.seed(seed)

    # 7. Load init states
    init_states = suite.get_task_init_states(selected_idx)
    return env, task_description, init_states, selected_idx
```

**Task Filtering by Perturbation Type:**
The `_get_task_indices()` function (lines 289-330) filters the suite's tasks:

```python
def _get_task_indices(
    suite: object,
    perturbation_type: str | None,
    num_tasks: int,
) -> list[int]:
    """Return task indices matching the requested perturbation type."""
    VALID_PERTURBATION_TYPES = [
        "camera_viewpoints",
        "light_conditions",
        "background_textures",
        "objects_layout",    # <-- _add_N tasks fall here
        "robot_initial_states",
        "sensor_noise",
    ]
    
    indices = []
    for i in range(num_tasks):
        task = suite.get_task(i)
        name = getattr(task, "name", "") or getattr(task, "bddl_file", "")
        classified = _classify_task(name)  # Uses regex to identify type

        if perturbation_type is None:
            if classified is None:  # Nominal tasks only
                indices.append(i)
        elif classified == perturbation_type:  # Match specific type
            indices.append(i)
    
    return indices
```

**Task Naming Convention for Filtering:**
The `_classify_task()` function (lines 244-286) uses regex patterns:

```python
VALID_PERTURBATION_TYPES = [
    "camera_viewpoints",    # _view_H_V_S_R_E_initstate_I pattern
    "light_conditions",     # _light_\d+$
    "background_textures",  # _table_\d+$ or _tb_\d+$
    "objects_layout",       # _add_\d+$ OR _level\d+  <-- KEY LINE
    "robot_initial_states", # view defaults with I != 0
    "sensor_noise",         # view defaults with noise > 0
]
```

**Available Task Suites:**
From the code, supported suites are:

```python
MAX_STEPS = {
    "libero_spatial": 220,   # 10 base tasks
    "libero_object": 280,
    "libero_goal": 300,
    "libero_10": 520,        # 10 tasks from various categories
    "libero_90": 400,        # 90 tasks (full LIBERO)
}
```

**Complete Workflow for Loading _add Tasks:**

```python
# Load LIBERO-Plus benchmark
from libero.libero import benchmark, get_libero_path

benchmark_dict = benchmark.get_benchmark_dict()
suite = benchmark_dict["libero_spatial"]()  # or any suite name

# Get all _add_N (objects_layout) tasks
all_tasks = []
for i in range(suite.n_tasks):
    task = suite.get_task(i)
    task_name = task.name or task.bddl_file
    if "_add_" in task_name:  # Filter for _add_N tasks
        all_tasks.append({
            "idx": i,
            "name": task_name,
            "language": task.language,
            "problem_folder": task.problem_folder,
            "bddl_file": task.bddl_file,
        })

# Use one specific _add task
task = suite.get_task(all_tasks[0]["idx"])
init_states = suite.get_task_init_states(all_tasks[0]["idx"])
task_description = task.language
```

---

### Key Files Reference

1. **Main LIBERO Integration**: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py` — Complete benchmark API and perturbation classification
2. **Expert Demo Collection**: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py` — Practical examples of spatial perturbation with `perturb_region_info()`
3. **Configuration**: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/configs.py` — Perturbation taxonomy definitions
4. **IDEA Brief**: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/docs/IDEA_BRIEF.md` — Full context on the Meta-Brain project's use of LIBERO-Plus
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "7bdd9550-3873-46d7-bf3a-2703be1055e9",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Search broadly under /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/ for any references to \"_add\", \"objects_layout\", \"add_n\", \"distractor\", \"new_objects\", \"perturb_region\" in Python files. Also look for any LIBERO-Plus related code or configuration. I want to understand:\n1. How _add_N tasks work in LIBERO-Plus\n2. How perturb_region_info() is currently used\n3. What the benchmark API looks like for loading _add tasks\nSearch breadth: very thorough",
    "agentId": "a3acedec04983e0ad",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Excellent! Now let me create a comprehensive summary document by gathering all the findings:\n\n## Summary\n\nBased on my thorough search of the project, here's what I found regarding your three questions about LIBERO-Plus:\n\n### 1. How _add_N tasks work in LIBERO-Plus\n\n**Task Naming Convention:**\nThe `_add_N` suffix is used to denote **objects_layout** perturbations in LIBERO-Plus task names. According to the classification logic in `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py` (lines 256, 283):\n\n```python\n# From _classify_task():\nif re.search(r\"_add_\\d+$\", task_name) or re.search(r\"_level\\d+\", task_name):\n    return \"objects_layout\"\n```\n\nThis pattern matches tasks like:\n- `task_name_add_0`\n- `task_name_add_1`\n- `task_name_level0`, `task_name_level1`, etc.\n\n**What _add_N means:**\n- `_add_N` tasks represent **spatial/layout perturbations** where objects are placed in different positions than the nominal configuration\n- These are distinct from the other 6 perturbation types: camera_viewpoints, light_conditions, background_textures, sensor_noise, and robot_initial_states\n- They fall under the broader **\"spatial\" class** (along with other layout/positioning changes)\n\n**Distinguishing _add from other layouts:**\nThe code filters out base tasks that contain perturbation suffixes including `_add_\\d+` to isolate nominal/unperturbed tasks (see lines 188-192 of collect_expert_demos.py).\n\n---\n\n### 2. How perturb_region_info() is currently used\n\n**Location and Import:**\nFound in `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py` (lines 236-270):\n\n```python\nfrom libero.randomizer.bddl_operators import (\n    load_bddl_file,\n    save_bddl_file,\n    perturb_region_info,\n)\n```\n\n**Current Usage Pattern:**\nThe `perturb_region_info()` function is used in the `create_spatial_bddl()` function for **spatial perturbation generation**:\n\n```python\ndef create_spatial_bddl(\n    base_bddl_path: str,\n    perturbation_config: dict,\n    output_dir: str,\n) -> str:\n    \"\"\"Create a perturbed BDDL file by applying spatial perturbation to all regions.\n    \n    Returns the path to the new BDDL file.\n    \"\"\"\n    spec = load_bddl_file(base_bddl_path)\n    delta_xy = perturbation_config[\"delta_xy\"]\n    delta_half = perturbation_config[\"delta_half_len\"]\n    delta_yaw = perturbation_config[\"delta_yaw\"]\n\n    # Apply perturbation to ALL regions in the BDDL spec\n    for i in range(len(spec.region_infos)):\n        spec.region_infos[i] = perturb_region_info(\n            spec.region_infos[i],\n            delta_region_centroid_xy=delta_xy,\n            delta_region_half_len=delta_half,\n            delta_yaw_rotation=delta_yaw,\n        )\n\n    # Save modified BDDL\n    os.makedirs(output_dir, exist_ok=True)\n    base_name = Path(base_bddl_path).stem\n    dx, dy = delta_xy\n    filename = f\"{base_name}_spatial_dx{dx:.2f}_dy{dy:.2f}.bddl\"\n    _, filepath = save_bddl_file(spec, bddl_filename=filename, bddl_dirpath=output_dir)\n    return filepath\n```\n\n**What it does:**\n- Takes a base BDDL file and applies **3D geometric transformations** to object placement regions:\n  - `delta_region_centroid_xy`: shifts region center by (dx, dy) in the XY plane\n  - `delta_region_half_len`: adjusts the region's half-length (size)\n  - `delta_yaw_rotation`: rotates regions by delta_yaw radians\n\n**Spatial Perturbation Grid:**\nThe project defines 10 predefined configurations (lines 60-71 of collect_expert_demos.py):\n\n```python\nSPATIAL_PERTURBATION_CONFIGS = [\n    {\"delta_xy\": ( 0.05,  0.00), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.0)},\n    {\"delta_xy\": (-0.05,  0.00), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.0)},\n    {\"delta_xy\": ( 0.00,  0.05), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.0)},\n    # ... 7 more configurations with varying magnitude\n]\n```\n\nThese magnitudes (±0.05m shifts, ±0.3 radian rotations) are chosen to be \"noticeable but within feasible reach of the robot.\"\n\n---\n\n### 3. What the benchmark API looks like for loading _add tasks\n\n**Core LIBERO-Plus Benchmark API:**\nFrom `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py` (lines 333-373):\n\n```python\ndef create_libero_env(\n    task_suite_name: str = \"libero_spatial\",\n    perturbation_type: str | None = None,\n    task_idx: int | None = None,\n    seed: int = 42,\n) -> tuple[Any, str, np.ndarray, int]:\n    \"\"\"Create a LIBERO / LIBERO-Plus evaluation environment.\n\n    Returns:\n        (env, task_description, init_states, selected_task_idx)\n    \"\"\"\n    # 1. Get benchmark dictionary\n    from libero.libero import benchmark, get_libero_path\n    from libero.libero.envs import OffScreenRenderEnv\n\n    benchmark_dict = benchmark.get_benchmark_dict()\n    suite = benchmark_dict[task_suite_name]()\n    num_tasks = suite.n_tasks\n\n    # 2. Filter tasks by perturbation type\n    valid_indices = _get_task_indices(suite, perturbation_type, num_tasks)\n\n    # 3. Select task\n    if task_idx is not None and task_idx in valid_indices:\n        selected_idx = task_idx\n    else:\n        selected_idx = random.choice(valid_indices)\n\n    # 4. Load task metadata\n    task = suite.get_task(selected_idx)\n    task_description = task.language\n\n    # 5. Load BDDL file\n    task_bddl_file = (\n        Path(get_libero_path(\"bddl_files\")) / task.problem_folder / task.bddl_file\n    )\n\n    # 6. Create environment\n    env = OffScreenRenderEnv(\n        bddl_file_name=str(task_bddl_file),\n        camera_heights=256,\n        camera_widths=256,\n    )\n    env.seed(seed)\n\n    # 7. Load init states\n    init_states = suite.get_task_init_states(selected_idx)\n    return env, task_description, init_states, selected_idx\n```\n\n**Task Filtering by Perturbation Type:**\nThe `_get_task_indices()` function (lines 289-330) filters the suite's tasks:\n\n```python\ndef _get_task_indices(\n    suite: object,\n    perturbation_type: str | None,\n    num_tasks: int,\n) -> list[int]:\n    \"\"\"Return task indices matching the requested perturbation type.\"\"\"\n    VALID_PERTURBATION_TYPES = [\n        \"camera_viewpoints\",\n        \"light_conditions\",\n        \"background_textures\",\n        \"objects_layout\",    # <-- _add_N tasks fall here\n        \"robot_initial_states\",\n        \"sensor_noise\",\n    ]\n    \n    indices = []\n    for i in range(num_tasks):\n        task = suite.get_task(i)\n        name = getattr(task, \"name\", \"\") or getattr(task, \"bddl_file\", \"\")\n        classified = _classify_task(name)  # Uses regex to identify type\n\n        if perturbation_type is None:\n            if classified is None:  # Nominal tasks only\n                indices.append(i)\n        elif classified == perturbation_type:  # Match specific type\n            indices.append(i)\n    \n    return indices\n```\n\n**Task Naming Convention for Filtering:**\nThe `_classify_task()` function (lines 244-286) uses regex patterns:\n\n```python\nVALID_PERTURBATION_TYPES = [\n    \"camera_viewpoints\",    # _view_H_V_S_R_E_initstate_I pattern\n    \"light_conditions\",     # _light_\\d+$\n    \"background_textures\",  # _table_\\d+$ or _tb_\\d+$\n    \"objects_layout\",       # _add_\\d+$ OR _level\\d+  <-- KEY LINE\n    \"robot_initial_states\", # view defaults with I != 0\n    \"sensor_noise\",         # view defaults with noise > 0\n]\n```\n\n**Available Task Suites:**\nFrom the code, supported suites are:\n\n```python\nMAX_STEPS = {\n    \"libero_spatial\": 220,   # 10 base tasks\n    \"libero_object\": 280,\n    \"libero_goal\": 300,\n    \"libero_10\": 520,        # 10 tasks from various categories\n    \"libero_90\": 400,        # 90 tasks (full LIBERO)\n}\n```\n\n**Complete Workflow for Loading _add Tasks:**\n\n```python\n# Load LIBERO-Plus benchmark\nfrom libero.libero import benchmark, get_libero_path\n\nbenchmark_dict = benchmark.get_benchmark_dict()\nsuite = benchmark_dict[\"libero_spatial\"]()  # or any suite name\n\n# Get all _add_N (objects_layout) tasks\nall_tasks = []\nfor i in range(suite.n_tasks):\n    task = suite.get_task(i)\n    task_name = task.name or task.bddl_file\n    if \"_add_\" in task_name:  # Filter for _add_N tasks\n        all_tasks.append({\n            \"idx\": i,\n            \"name\": task_name,\n            \"language\": task.language,\n            \"problem_folder\": task.problem_folder,\n            \"bddl_file\": task.bddl_file,\n        })\n\n# Use one specific _add task\ntask = suite.get_task(all_tasks[0][\"idx\"])\ninit_states = suite.get_task_init_states(all_tasks[0][\"idx\"])\ntask_description = task.language\n```\n\n---\n\n### Key Files Reference\n\n1. **Main LIBERO Integration**: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py` — Complete benchmark API and perturbation classification\n2. **Expert Demo Collection**: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py` — Practical examples of spatial perturbation with `perturb_region_info()`\n3. **Configuration**: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/configs.py` — Perturbation taxonomy definitions\n4. **IDEA Brief**: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/docs/IDEA_BRIEF.md` — Full context on the Meta-Brain project's use of LIBERO-Plus"
      }
    ],
    "totalDurationMs": 49927,
    "totalTokens": 71656,
    "totalToolUseCount": 21,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3565,
      "cache_read_input_tokens": 65007,
      "output_tokens": 3077,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3565
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 3077,
          "cache_read_input_tokens": 65007,
          "cache_creation_input_tokens": 3565,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3565,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 10,
      "searchCount": 9,
      "bashCount": 2,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
````

</details>

---


### Assistant

_source line 96_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good understanding of the codebase. Let me read the actual full source files to make precise edits.

Key findings:
1. `collect_expert_demos.py` is at `artifacts/phase1/collect_expert_demos.py`
2. Phase 0's `libero_integration.py` has `create_libero_env()` and `_get_task_indices()` / `_classify_task()` that already handle `_add_N` tasks via `objects_layout` perturbation type


3. The current spatial mode generates BDDL modifications on the fly using geometric transforms, but I need to switch to loading pre-existing `_add_N` BDDL files from the benchmark instead

Let me examine the actual source files now to understand exactly where to make these changes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "39b6d7b6-fa45-49f4-a016-64fa21771588",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011QJ8ibccB2Euntg6tygeJB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5109,
      "cache_read_input_tokens": 23821,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5109
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

_source line 97_

<details open><summary>🔧 Tool call — Read · `toolu_01HezrJEzUkJ6hon7cWLePPA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "1ca1fd9c-ca72-47ef-8eab-6ff5eba7586c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011QJ8ibccB2Euntg6tygeJB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5109,
      "cache_read_input_tokens": 23821,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5109
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

_source line 98_

<details open><summary>🔧 Tool call — Read · `toolu_01WjxwLeN3wnEH8KFdNDWGha`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "6814068f-d05a-48e0-9030-cfbe4d9fe63f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011QJ8ibccB2Euntg6tygeJB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5109,
      "cache_read_input_tokens": 23821,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5109
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

_source line 99 · 2026-05-15T17:51:19.651Z_

<details><summary>↩ Tool result · `toolu_01HezrJEzUkJ6hon7cWLePPA`</summary>

```text
1	"""
2	Collect expert demonstrations by rolling out frozen π₀ in perturbed LIBERO environments.
3	
4	Only successful episodes are saved. Two perturbation types are supported:
5	  - physical: vary robot initial state (init_states index 1-49)
6	  - spatial:  perturb object layout via BDDL region_info modifications
7	
8	Output: pickle files with (observations, actions, metadata) per episode.
9	
10	Usage:
11	    # Physical perturbation dry-run
12	    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \
13	        --perturbation_type physical --dry_run
14	
15	    # Spatial perturbation dry-run
16	    CUDA_VISIBLE_DEVICES=2 python collect_expert_demos.py \
17	        --perturbation_type spatial --dry_run
18	
19	    # Full physical collection
20	    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \
21	        --perturbation_type physical
22	"""
23	
24	import argparse
25	import collections
26	import copy
27	import logging
28	import math
29	import os
30	import pickle
31	import random
32	import re
33	import sys
34	import time
35	import types
36	from pathlib import Path
37	from typing import Any
38	
39	import numpy as np
40	import torch
41	
42	log = logging.getLogger(__name__)
43	
44	# ---------------------------------------------------------------------------
45	# Constants
46	# ---------------------------------------------------------------------------
47	
48	LIBERO_DUMMY_ACTION = [0.0] * 6 + [-1.0]
49	LIBERO_ENV_RESOLUTION = 256
50	MODEL_INPUT_RESOLUTION = 224
51	REPLAN_STEPS = 5
52	NUM_STEPS_WAIT = 10
53	MAX_STEPS = 220  # libero_spatial default
54	
55	# 10 base tasks in libero_spatial (no perturbation suffix)
56	BASE_TASK_SUITE = "libero_spatial"
57	
58	# Spatial perturbation grid: 10 configurations with varying XY shifts and yaw
59	# Magnitudes chosen to be noticeable but within feasible reach of the robot.
60	SPATIAL_PERTURBATION_CONFIGS = [
61	    {"delta_xy": ( 0.05,  0.00), "delta_half_len": 0.0,  "delta_yaw": (0.0, 0.0)},
62	    {"delta_xy": (-0.05,  0.00), "delta_half_len": 0.0,  "delta_yaw": (0.0, 0.0)},
63	    {"delta_xy": ( 0.00,  0.05), "delta_half_len": 0.0,  "delta_yaw": (0.0, 0.0)},
64	    {"delta_xy": ( 0.00, -0.05), "delta_half_len": 0.0,  "delta_yaw": (0.0, 0.0)},
65	    {"delta_xy": ( 0.03,  0.03), "delta_half_len": 0.0,  "delta_yaw": (0.0, 0.0)},
66	    {"delta_xy": (-0.03, -0.03), "delta_half_len": 0.0,  "delta_yaw": (0.0, 0.0)},
67	    {"delta_xy": ( 0.04,  0.00), "delta_half_len": 0.01, "delta_yaw": (0.3, 0.0)},
68	    {"delta_xy": (-0.04,  0.00), "delta_half_len": 0.01, "delta_yaw": (-0.3, 0.0)},
69	    {"delta_xy": ( 0.00,  0.04), "delta_half_len": 0.0,  "delta_yaw": (0.0, 0.3)},
70	    {"delta_xy": ( 0.00, -0.04), "delta_half_len": 0.0,  "delta_yaw": (0.0, -0.3)},
71	]
72	
73	
74	# ---------------------------------------------------------------------------
75	# Geometry / image helpers (from libero_integration.py)
76	# ---------------------------------------------------------------------------
77	
78	def _quat2axisangle(quat: np.ndarray) -> np.ndarray:
79	    """Quaternion [x,y,z,w] -> axis-angle [ax,ay,az]."""
80	    q = np.asarray(quat, dtype=np.float64)
81	    norm = np.linalg.norm(q)
82	    if norm < 1e-8:
83	        return np.zeros(3, dtype=np.float32)
84	    q /= norm
85	    sin_half = np.linalg.norm(q[:3])
86	    if sin_half < 1e-8:
87	        return np.zeros(3, dtype=np.float32)
88	    angle = 2.0 * math.atan2(sin_half, q[3])
89	    axis = q[:3] / sin_half
90	    return (axis * angle).astype(np.float32)
91	
92	
93	def _resize_with_pad(img: np.ndarray, size: int) -> np.ndarray:
94	    """Resize image with aspect-preserving padding to (size, size, 3) uint8."""
95	    try:
96	        from openpi_client.image_tools import resize_with_pad, convert_to_uint8
97	        return convert_to_uint8(resize_with_pad(img, size, size))
98	    except ImportError:
99	        from PIL import Image as PILImage
100	        h, w = img.shape[:2]
101	        scale = min(size / h, size / w)
102	        new_h, new_w = int(h * scale), int(w * scale)
103	        resized = np.array(
104	            PILImage.fromarray(img).resize((new_w, new_h), PILImage.BILINEAR)
105	        )
106	        canvas = np.zeros((size, size, 3), dtype=np.uint8)
107	        y0, x0 = (size - new_h) // 2, (size - new_w) // 2
108	        canvas[y0 : y0 + new_h, x0 : x0 + new_w] = resized
109	        return canvas
110	
111	
112	def obs_to_model_input(obs: dict, task_description: str) -> dict:
113	    """Convert LIBERO observation to the dict format expected by policy.infer()."""
114	    base_img = np.ascontiguousarray(obs["agentview_image"][::-1, ::-1])
115	    wrist_img = np.ascontiguousarray(obs["robot0_eye_in_hand_image"][::-1, ::-1])
116	
117	    base_img = _resize_with_pad(base_img, MODEL_INPUT_RESOLUTION)
118	    wrist_img = _resize_with_pad(wrist_img, MODEL_INPUT_RESOLUTION)
119	
120	    state = np.concatenate([
121	        obs["robot0_eef_pos"].astype(np.float32),
122	        _quat2axisangle(obs["robot0_eef_quat"]),
123	        obs["robot0_gripper_qpos"].astype(np.float32),
124	    ])
125	
126	    return {
127	        "observation/image": base_img,
128	        "observation/wrist_image": wrist_img,
129	        "observation/state": state,
130	        "prompt": task_description,
131	    }
132	
133	
134	def extract_obs_for_saving(obs: dict) -> dict:
135	    """Extract observation fields to save in demo data (images stored as uint8)."""
136	    return {
137	        "agentview_image": obs["agentview_image"].copy(),
138	        "robot0_eye_in_hand_image": obs["robot0_eye_in_hand_image"].copy(),
139	        "robot0_eef_pos": obs["robot0_eef_pos"].astype(np.float32).copy(),
140	        "robot0_eef_quat": obs["robot0_eef_quat"].astype(np.float32).copy(),
141	        "robot0_gripper_qpos": obs["robot0_gripper_qpos"].astype(np.float32).copy(),
142	    }
143	
144	
145	# ---------------------------------------------------------------------------
146	# Model loading
147	# ---------------------------------------------------------------------------
148	
149	def _ensure_openpi_imports():
150	    """Stub out lerobot (training-only dep) before importing OpenPI."""
151	    for mod in [
152	        "lerobot", "lerobot.common", "lerobot.common.datasets",
153	        "lerobot.common.datasets.lerobot_dataset",
154	    ]:
155	        if mod not in sys.modules:
156	            sys.modules[mod] = types.ModuleType(mod)
157	
158	
159	def load_pi0_policy(checkpoint_path: str, device: str) -> object:
160	    """Load pi0 policy via OpenPI. Returns the Policy object for inference."""
161	    _ensure_openpi_imports()
162	    from openpi.training import config as _config
163	    from openpi.policies import policy_config
164	
165	    train_config = _config.get_config("pi0_libero")
166	    policy = policy_config.create_trained_policy(
167	        train_config, checkpoint_path, pytorch_device=device
168	    )
169	    log.info("Loaded pi0 policy on %s", device)
170	    return policy
171	
172	
173	# ---------------------------------------------------------------------------
174	# Task discovery
175	# ---------------------------------------------------------------------------
176	
177	def find_base_tasks(bddl_dir: str, num_tasks: int = 10) -> list[dict]:
178	    """Find base (unperturbed) BDDL files in libero_spatial.
179	
180	    Returns list of dicts with keys: name, bddl_path, init_states_path.
181	    """
182	    all_files = [f for f in os.listdir(bddl_dir) if f.endswith(".bddl")]
183	
184	    base_names = []
185	    for f in sorted(all_files):
186	        name = f.replace(".bddl", "")
187	        # Skip any file with perturbation suffixes
188	        if re.search(
189	            r"(_add_\d+|_table_\d+|_tb_\d+|_light_\d+|_language_\d+"
190	            r"|_view_|_noise_|_level\d+| copy)",
191	            name,
192	        ):
193	            continue
194	        base_names.append(name)
195	
196	    init_dir = bddl_dir.replace("bddl_files", "init_files")
197	    tasks = []
198	    for name in base_names[:num_tasks]:
199	        bddl_path = os.path.join(bddl_dir, f"{name}.bddl")
200	        init_path = os.path.join(init_dir, f"{name}.pruned_init")
201	        if not os.path.exists(init_path):
202	            log.warning("init_states not found for %s, skipping", name)
203	            continue
204	        tasks.append({
205	            "name": name,
206	            "bddl_path": bddl_path,
207	            "init_states_path": init_path,
208	        })
209	
210	    log.info("Found %d base tasks", len(tasks))
211	    return tasks
212	
213	
214	def get_task_language(bddl_path: str) -> str:
215	    """Extract language instruction from a BDDL file."""
216	    from libero.libero.envs.bddl_utils import get_problem_info
217	    info = get_problem_info(bddl_path)
218	    return info["language_instruction"]
219	
220	
221	# ---------------------------------------------------------------------------
222	# Environment creation
223	# ---------------------------------------------------------------------------
224	
225	def create_env(bddl_path: str) -> object:
226	    """Create a LIBERO OffScreenRenderEnv from a BDDL file."""
227	    from libero.libero.envs import OffScreenRenderEnv
228	    env = OffScreenRenderEnv(
229	        bddl_file_name=bddl_path,
230	        camera_heights=LIBERO_ENV_RESOLUTION,
231	        camera_widths=LIBERO_ENV_RESOLUTION,
232	    )
233	    return env
234	
235	
236	def create_spatial_bddl(
237	    base_bddl_path: str,
238	    perturbation_config: dict,
239	    output_dir: str,
240	) -> str:
241	    """Create a perturbed BDDL file by applying spatial perturbation to all regions.
242	
243	    Returns the path to the new BDDL file.
244	    """
245	    sys.path.insert(0, "/root/LIBERO-plus/libero")
246	    from libero.randomizer.bddl_operators import (
247	        load_bddl_file,
248	        save_bddl_file,
249	        perturb_region_info,
250	    )
251	
252	    spec = load_bddl_file(base_bddl_path)
253	    delta_xy = perturbation_config["delta_xy"]
254	    delta_half = perturbation_config["delta_half_len"]
255	    delta_yaw = perturbation_config["delta_yaw"]
256	
257	    for i in range(len(spec.region_infos)):
258	        spec.region_infos[i] = perturb_region_info(
259	            spec.region_infos[i],
260	            delta_region_centroid_xy=delta_xy,
261	            delta_region_half_len=delta_half,
262	            delta_yaw_rotation=delta_yaw,
263	        )
264	
265	    os.makedirs(output_dir, exist_ok=True)
266	    base_name = Path(base_bddl_path).stem
267	    dx, dy = delta_xy
268	    filename = f"{base_name}_spatial_dx{dx:.2f}_dy{dy:.2f}.bddl"
269	    _, filepath = save_bddl_file(spec, bddl_filename=filename, bddl_dirpath=output_dir)
270	    return filepath
271	
272	
273	# ---------------------------------------------------------------------------
274	# Episode rollout
275	# ---------------------------------------------------------------------------
276	
277	def rollout_episode(
278	    policy: object,
279	    env: object,
280	    task_description: str,
281	    init_states: np.ndarray,
282	    init_state_idx: int,
283	    seed: int,
284	) -> dict[str, Any]:
285	    """Run one episode, collecting (obs, action) pairs.
286	
287	    Returns dict with observations, actions, success, num_steps.
288	    """
289	    env.seed(seed)
290	    obs = env.set_init_state(init_states[init_state_idx])
291	
292	    for _ in range(NUM_STEPS_WAIT):
293	        obs, _, _, _ = env.step(LIBERO_DUMMY_ACTION)
294	
295	    all_obs = [extract_obs_for_saving(obs)]
296	    all_actions = []
297	    action_plan = collections.deque()
298	    step = 0
299	    success = False
300	    done = False
301	
302	    while not done and step < MAX_STEPS:
303	        if len(action_plan) == 0:
304	            obs_dict = obs_to_model_input(obs, task_description)
305	            result = policy.infer(obs_dict)
306	            action_chunk = result["actions"]
307	            action_plan.extend(action_chunk[:REPLAN_STEPS])
308	
309	        action = action_plan.popleft()
310	        if isinstance(action, torch.Tensor):
311	            action = action.cpu().numpy()
312	        action_np = np.asarray(action, dtype=np.float32)
313	
314	        obs, reward, done, info = env.step(
315	            action_np.tolist() if hasattr(action_np, "tolist") else list(action_np)
316	        )
317	        step += 1
318	
319	        all_obs.append(extract_obs_for_saving(obs))
320	        all_actions.append(action_np)
321	
322	        if done or reward > 0:
323	            success = info.get("success", reward > 0)
324	
325	    return {
326	        "observations": all_obs,
327	        "actions": np.stack(all_actions) if all_actions else np.zeros((0, 7)),
328	        "success": success,
329	        "num_steps": step,
330	    }
331	
332	
333	# ---------------------------------------------------------------------------
334	# Collection loops
335	# ---------------------------------------------------------------------------
336	
337	def collect_physical(
338	    policy: object,
339	    tasks: list[dict],
340	    episodes_per_config: int,
341	    output_dir: str,
342	    dry_run: bool,
343	) -> dict:
344	    """Collect expert demos with physical (robot initial state) perturbation.
345	
346	    Uses init_states indices 1-49 (index 0 is nominal).
347	    """
348	    os.makedirs(output_dir, exist_ok=True)
349	    stats = {"total": 0, "success": 0, "saved_files": []}
350	
351	    init_state_indices = list(range(1, 50))  # 49 perturbed states
352	    if dry_run:
353	        tasks = tasks[:1]
354	        init_state_indices = [1]
355	        episodes_per_config = 1
356	
357	    for task_info in tasks:
358	        task_name = task_info["name"]
359	        init_states = torch.load(task_info["init_states_path"], weights_only=False)
360	        language = get_task_language(task_info["bddl_path"])
361	        log.info("Task: %s (%d init_states available)", task_name, len(init_states))
362	
363	        for idx in init_state_indices:
364	            if idx >= len(init_states):
365	                continue
366	
367	            for ep in range(episodes_per_config):
368	                seed = hash((task_name, idx, ep)) % (2**31)
369	                stats["total"] += 1
370	
371	                try:
372	                    env = create_env(task_info["bddl_path"])
373	                    result = rollout_episode(
374	                        policy, env, language, init_states, idx, seed
375	                    )
376	                    env.close()
377	                except Exception:
378	                    log.exception(
379	                        "Episode failed: task=%s idx=%d ep=%d", task_name, idx, ep
380	                    )
381	                    continue
382	
383	                if result["success"]:
384	                    stats["success"] += 1
385	                    demo = {
386	                        "observations": result["observations"],
387	                        "actions": result["actions"],
388	                        "task_name": task_name,
389	                        "perturbation_config": {
390	                            "type": "physical",
391	                            "init_state_idx": idx,
392	                        },
393	                        "success": True,
394	                        "num_steps": result["num_steps"],
395	                    }
396	                    fname = f"{task_name}_initstate{idx}_ep{ep}.pkl"
397	                    fpath = os.path.join(output_dir, fname)
398	                    with open(fpath, "wb") as f:
399	                        pickle.dump(demo, f, protocol=pickle.HIGHEST_PROTOCOL)
400	                    stats["saved_files"].append(fpath)
401	
402	                rate = stats["success"] / stats["total"] * 100
403	                log.info(
404	                    "[physical] task=%s idx=%d ep=%d | %s | "
405	                    "cumulative %d/%d (%.1f%%)",
406	                    task_name, idx, ep,
407	                    "SUCCESS" if result["success"] else "FAIL",
408	                    stats["success"], stats["total"], rate,
409	                )
410	
411	    return stats
412	
413	
414	def collect_spatial(
415	    policy: object,
416	    tasks: list[dict],
417	    episodes_per_config: int,
418	    output_dir: str,
419	    dry_run: bool,
420	) -> dict:
421	    """Collect expert demos with spatial (objects layout) perturbation.
422	
423	    Applies 10 predefined spatial perturbation configs to each base task.
424	    """
425	    os.makedirs(output_dir, exist_ok=True)
426	    tmp_bddl_dir = os.path.join(output_dir, "_tmp_bddl")
427	    os.makedirs(tmp_bddl_dir, exist_ok=True)
428	    stats = {"total": 0, "success": 0, "saved_files": []}
429	
430	    configs = SPATIAL_PERTURBATION_CONFIGS
431	    if dry_run:
432	        tasks = tasks[:1]
433	        configs = configs[:1]
434	        episodes_per_config = 1
435	
436	    for task_info in tasks:
437	        task_name = task_info["name"]
438	        init_states = torch.load(task_info["init_states_path"], weights_only=False)
439	        log.info("Task: %s", task_name)
440	
441	        for cfg_idx, cfg in enumerate(configs):
442	            try:
443	                perturbed_bddl = create_spatial_bddl(
444	                    task_info["bddl_path"], cfg, tmp_bddl_dir
445	                )
446	                language = get_task_language(perturbed_bddl)
447	            except Exception:
448	                log.exception(
449	                    "BDDL perturbation failed: task=%s cfg=%d", task_name, cfg_idx
450	                )
451	                continue
452	
453	            for ep in range(episodes_per_config):
454	                seed = hash((task_name, cfg_idx, ep)) % (2**31)
455	                stats["total"] += 1
456	
457	                try:
458	                    env = create_env(perturbed_bddl)
459	                    # Use nominal init_state (index 0) for spatial perturbation
460	                    result = rollout_episode(
461	                        policy, env, language, init_states, 0, seed
462	                    )
463	                    env.close()
464	                except Exception:
465	                    log.exception(
466	                        "Episode failed: task=%s cfg=%d ep=%d",
467	                        task_name, cfg_idx, ep,
468	                    )
469	                    continue
470	
471	                if result["success"]:
472	                    stats["success"] += 1
473	                    demo = {
474	                        "observations": result["observations"],
475	                        "actions": result["actions"],
476	                        "task_name": task_name,
477	                        "perturbation_config": {
478	                            "type": "spatial",
479	                            "config_idx": cfg_idx,
480	                            "delta_xy": cfg["delta_xy"],
481	                            "delta_half_len": cfg["delta_half_len"],
482	                            "delta_yaw": cfg["delta_yaw"],
483	                        },
484	                        "success": True,
485	                        "num_steps": result["num_steps"],
486	                    }
487	                    fname = f"{task_name}_spatial{cfg_idx}_ep{ep}.pkl"
488	                    fpath = os.path.join(output_dir, fname)
489	                    with open(fpath, "wb") as f:
490	                        pickle.dump(demo, f, protocol=pickle.HIGHEST_PROTOCOL)
491	                    stats["saved_files"].append(fpath)
492	
493	                rate = stats["success"] / stats["total"] * 100
494	                log.info(
495	                    "[spatial] task=%s cfg=%d ep=%d | %s | "
496	                    "cumulative %d/%d (%.1f%%)",
497	                    task_name, cfg_idx, ep,
498	                    "SUCCESS" if result["success"] else "FAIL",
499	                    stats["success"], stats["total"], rate,
500	                )
501	
502	    return stats
503	
504	
505	# ---------------------------------------------------------------------------
506	# Main
507	# ---------------------------------------------------------------------------
508	
509	def main():
510	    parser = argparse.ArgumentParser(
511	        description="Collect expert demos from π₀ in perturbed LIBERO environments"
512	    )
513	    parser.add_argument(
514	        "--perturbation_type", type=str, required=True,
515	        choices=["physical", "spatial"],
516	    )
517	    parser.add_argument("--gpu_id", type=int, default=0)
518	    parser.add_argument("--num_tasks", type=int, default=10)
519	    parser.add_argument("--episodes_per_config", type=int, default=3)
520	    parser.add_argument(
521	        "--output_dir", type=str, default=None,
522	        help="Override output directory (default: auto from perturbation_type)",
523	    )
524	    parser.add_argument(
525	        "--checkpoint", type=str,
526	        default="/root/autodl-tmp/checkpoints/pi0_base",
527	    )
528	    parser.add_argument("--dry_run", action="store_true")
529	    parser.add_argument("--seed", type=int, default=42)
530	    args = parser.parse_args()
531	
532	    logging.basicConfig(
533	        level=logging.INFO,
534	        format="%(asctime)s [%(levelname)s] %(message)s",
535	    )
536	
537	    random.seed(args.seed)
538	    np.random.seed(args.seed)
539	    torch.manual_seed(args.seed)
540	
541	    if args.output_dir is None:
542	        args.output_dir = (
543	            f"/root/meta_brain_lora_routing/data/expert_demos/{args.perturbation_type}"
544	        )
545	
546	    device = f"cuda:{args.gpu_id}"
547	    log.info(
548	        "Config: type=%s device=%s num_tasks=%d eps_per_cfg=%d dry_run=%s",
549	        args.perturbation_type, device, args.num_tasks,
550	        args.episodes_per_config, args.dry_run,
551	    )
552	
553	    log.info("Loading π₀ from %s", args.checkpoint)
554	    policy = load_pi0_policy(args.checkpoint, device)
555	
556	    from libero.libero import get_libero_path
557	    bddl_dir = os.path.join(get_libero_path("bddl_files"), BASE_TASK_SUITE)
558	    tasks = find_base_tasks(bddl_dir, num_tasks=args.num_tasks)
559	
560	    if not tasks:
561	        log.error("No base tasks found in %s", bddl_dir)
562	        sys.exit(1)
563	
564	    t0 = time.time()
565	
566	    if args.perturbation_type == "physical":
567	        stats = collect_physical(
568	            policy, tasks, args.episodes_per_config,
569	            args.output_dir, args.dry_run,
570	        )
571	    else:
572	        stats = collect_spatial(
573	            policy, tasks, args.episodes_per_config,
574	            args.output_dir, args.dry_run,
575	        )
576	
577	    elapsed = time.time() - t0
578	
579	    total_size = sum(
580	        os.path.getsize(f) for f in stats["saved_files"] if os.path.exists(f)
581	    )
582	    log.info("=" * 60)
583	    log.info("Collection complete: %s", args.perturbation_type)
584	    log.info("  Total episodes:  %d", stats["total"])
585	    log.info("  Successful:      %d", stats["success"])
586	    log.info(
587	        "  Success rate:    %.1f%%",
588	        stats["success"] / max(stats["total"], 1) * 100,
589	    )
590	    log.info("  Files saved:     %d", len(stats["saved_files"]))
591	    log.info("  Total size:      %.1f MB", total_size / 1024 / 1024)
592	    log.info("  Elapsed:         %.1f min", elapsed / 60)
593	    log.info("  Output dir:      %s", args.output_dir)
594	
595	
596	if __name__ == "__main__":
597	    main()
598	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "3b0b9e47-d2b6-496a-ba16-7b22bb79587f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py",
      "content": "\"\"\"\nCollect expert demonstrations by rolling out frozen π₀ in perturbed LIBERO environments.\n\nOnly successful episodes are saved. Two perturbation types are supported:\n  - physical: vary robot initial state (init_states index 1-49)\n  - spatial:  perturb object layout via BDDL region_info modifications\n\nOutput: pickle files with (observations, actions, metadata) per episode.\n\nUsage:\n    # Physical perturbation dry-run\n    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \\\n        --perturbation_type physical --dry_run\n\n    # Spatial perturbation dry-run\n    CUDA_VISIBLE_DEVICES=2 python collect_expert_demos.py \\\n        --perturbation_type spatial --dry_run\n\n    # Full physical collection\n    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \\\n        --perturbation_type physical\n\"\"\"\n\nimport argparse\nimport collections\nimport copy\nimport logging\nimport math\nimport os\nimport pickle\nimport random\nimport re\nimport sys\nimport time\nimport types\nfrom pathlib import Path\nfrom typing import Any\n\nimport numpy as np\nimport torch\n\nlog = logging.getLogger(__name__)\n\n# ---------------------------------------------------------------------------\n# Constants\n# ---------------------------------------------------------------------------\n\nLIBERO_DUMMY_ACTION = [0.0] * 6 + [-1.0]\nLIBERO_ENV_RESOLUTION = 256\nMODEL_INPUT_RESOLUTION = 224\nREPLAN_STEPS = 5\nNUM_STEPS_WAIT = 10\nMAX_STEPS = 220  # libero_spatial default\n\n# 10 base tasks in libero_spatial (no perturbation suffix)\nBASE_TASK_SUITE = \"libero_spatial\"\n\n# Spatial perturbation grid: 10 configurations with varying XY shifts and yaw\n# Magnitudes chosen to be noticeable but within feasible reach of the robot.\nSPATIAL_PERTURBATION_CONFIGS = [\n    {\"delta_xy\": ( 0.05,  0.00), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.0)},\n    {\"delta_xy\": (-0.05,  0.00), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.0)},\n    {\"delta_xy\": ( 0.00,  0.05), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.0)},\n    {\"delta_xy\": ( 0.00, -0.05), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.0)},\n    {\"delta_xy\": ( 0.03,  0.03), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.0)},\n    {\"delta_xy\": (-0.03, -0.03), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.0)},\n    {\"delta_xy\": ( 0.04,  0.00), \"delta_half_len\": 0.01, \"delta_yaw\": (0.3, 0.0)},\n    {\"delta_xy\": (-0.04,  0.00), \"delta_half_len\": 0.01, \"delta_yaw\": (-0.3, 0.0)},\n    {\"delta_xy\": ( 0.00,  0.04), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.3)},\n    {\"delta_xy\": ( 0.00, -0.04), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, -0.3)},\n]\n\n\n# ---------------------------------------------------------------------------\n# Geometry / image helpers (from libero_integration.py)\n# ---------------------------------------------------------------------------\n\ndef _quat2axisangle(quat: np.ndarray) -> np.ndarray:\n    \"\"\"Quaternion [x,y,z,w] -> axis-angle [ax,ay,az].\"\"\"\n    q = np.asarray(quat, dtype=np.float64)\n    norm = np.linalg.norm(q)\n    if norm < 1e-8:\n        return np.zeros(3, dtype=np.float32)\n    q /= norm\n    sin_half = np.linalg.norm(q[:3])\n    if sin_half < 1e-8:\n        return np.zeros(3, dtype=np.float32)\n    angle = 2.0 * math.atan2(sin_half, q[3])\n    axis = q[:3] / sin_half\n    return (axis * angle).astype(np.float32)\n\n\ndef _resize_with_pad(img: np.ndarray, size: int) -> np.ndarray:\n    \"\"\"Resize image with aspect-preserving padding to (size, size, 3) uint8.\"\"\"\n    try:\n        from openpi_client.image_tools import resize_with_pad, convert_to_uint8\n        return convert_to_uint8(resize_with_pad(img, size, size))\n    except ImportError:\n        from PIL import Image as PILImage\n        h, w = img.shape[:2]\n        scale = min(size / h, size / w)\n        new_h, new_w = int(h * scale), int(w * scale)\n        resized = np.array(\n            PILImage.fromarray(img).resize((new_w, new_h), PILImage.BILINEAR)\n        )\n        canvas = np.zeros((size, size, 3), dtype=np.uint8)\n        y0, x0 = (size - new_h) // 2, (size - new_w) // 2\n        canvas[y0 : y0 + new_h, x0 : x0 + new_w] = resized\n        return canvas\n\n\ndef obs_to_model_input(obs: dict, task_description: str) -> dict:\n    \"\"\"Convert LIBERO observation to the dict format expected by policy.infer().\"\"\"\n    base_img = np.ascontiguousarray(obs[\"agentview_image\"][::-1, ::-1])\n    wrist_img = np.ascontiguousarray(obs[\"robot0_eye_in_hand_image\"][::-1, ::-1])\n\n    base_img = _resize_with_pad(base_img, MODEL_INPUT_RESOLUTION)\n    wrist_img = _resize_with_pad(wrist_img, MODEL_INPUT_RESOLUTION)\n\n    state = np.concatenate([\n        obs[\"robot0_eef_pos\"].astype(np.float32),\n        _quat2axisangle(obs[\"robot0_eef_quat\"]),\n        obs[\"robot0_gripper_qpos\"].astype(np.float32),\n    ])\n\n    return {\n        \"observation/image\": base_img,\n        \"observation/wrist_image\": wrist_img,\n        \"observation/state\": state,\n        \"prompt\": task_description,\n    }\n\n\ndef extract_obs_for_saving(obs: dict) -> dict:\n    \"\"\"Extract observation fields to save in demo data (images stored as uint8).\"\"\"\n    return {\n        \"agentview_image\": obs[\"agentview_image\"].copy(),\n        \"robot0_eye_in_hand_image\": obs[\"robot0_eye_in_hand_image\"].copy(),\n        \"robot0_eef_pos\": obs[\"robot0_eef_pos\"].astype(np.float32).copy(),\n        \"robot0_eef_quat\": obs[\"robot0_eef_quat\"].astype(np.float32).copy(),\n        \"robot0_gripper_qpos\": obs[\"robot0_gripper_qpos\"].astype(np.float32).copy(),\n    }\n\n\n# ---------------------------------------------------------------------------\n# Model loading\n# ---------------------------------------------------------------------------\n\ndef _ensure_openpi_imports():\n    \"\"\"Stub out lerobot (training-only dep) before importing OpenPI.\"\"\"\n    for mod in [\n        \"lerobot\", \"lerobot.common\", \"lerobot.common.datasets\",\n        \"lerobot.common.datasets.lerobot_dataset\",\n    ]:\n        if mod not in sys.modules:\n            sys.modules[mod] = types.ModuleType(mod)\n\n\ndef load_pi0_policy(checkpoint_path: str, device: str) -> object:\n    \"\"\"Load pi0 policy via OpenPI. Returns the Policy object for inference.\"\"\"\n    _ensure_openpi_imports()\n    from openpi.training import config as _config\n    from openpi.policies import policy_config\n\n    train_config = _config.get_config(\"pi0_libero\")\n    policy = policy_config.create_trained_policy(\n        train_config, checkpoint_path, pytorch_device=device\n    )\n    log.info(\"Loaded pi0 policy on %s\", device)\n    return policy\n\n\n# ---------------------------------------------------------------------------\n# Task discovery\n# ---------------------------------------------------------------------------\n\ndef find_base_tasks(bddl_dir: str, num_tasks: int = 10) -> list[dict]:\n    \"\"\"Find base (unperturbed) BDDL files in libero_spatial.\n\n    Returns list of dicts with keys: name, bddl_path, init_states_path.\n    \"\"\"\n    all_files = [f for f in os.listdir(bddl_dir) if f.endswith(\".bddl\")]\n\n    base_names = []\n    for f in sorted(all_files):\n        name = f.replace(\".bddl\", \"\")\n        # Skip any file with perturbation suffixes\n        if re.search(\n            r\"(_add_\\d+|_table_\\d+|_tb_\\d+|_light_\\d+|_language_\\d+\"\n            r\"|_view_|_noise_|_level\\d+| copy)\",\n            name,\n        ):\n            continue\n        base_names.append(name)\n\n    init_dir = bddl_dir.replace(\"bddl_files\", \"init_files\")\n    tasks = []\n    for name in base_names[:num_tasks]:\n        bddl_path = os.path.join(bddl_dir, f\"{name}.bddl\")\n        init_path = os.path.join(init_dir, f\"{name}.pruned_init\")\n        if not os.path.exists(init_path):\n            log.warning(\"init_states not found for %s, skipping\", name)\n            continue\n        tasks.append({\n            \"name\": name,\n            \"bddl_path\": bddl_path,\n            \"init_states_path\": init_path,\n        })\n\n    log.info(\"Found %d base tasks\", len(tasks))\n    return tasks\n\n\ndef get_task_language(bddl_path: str) -> str:\n    \"\"\"Extract language instruction from a BDDL file.\"\"\"\n    from libero.libero.envs.bddl_utils import get_problem_info\n    info = get_problem_info(bddl_path)\n    return info[\"language_instruction\"]\n\n\n# ---------------------------------------------------------------------------\n# Environment creation\n# ---------------------------------------------------------------------------\n\ndef create_env(bddl_path: str) -> object:\n    \"\"\"Create a LIBERO OffScreenRenderEnv from a BDDL file.\"\"\"\n    from libero.libero.envs import OffScreenRenderEnv\n    env = OffScreenRenderEnv(\n        bddl_file_name=bddl_path,\n        camera_heights=LIBERO_ENV_RESOLUTION,\n        camera_widths=LIBERO_ENV_RESOLUTION,\n    )\n    return env\n\n\ndef create_spatial_bddl(\n    base_bddl_path: str,\n    perturbation_config: dict,\n    output_dir: str,\n) -> str:\n    \"\"\"Create a perturbed BDDL file by applying spatial perturbation to all regions.\n\n    Returns the path to the new BDDL file.\n    \"\"\"\n    sys.path.insert(0, \"/root/LIBERO-plus/libero\")\n    from libero.randomizer.bddl_operators import (\n        load_bddl_file,\n        save_bddl_file,\n        perturb_region_info,\n    )\n\n    spec = load_bddl_file(base_bddl_path)\n    delta_xy = perturbation_config[\"delta_xy\"]\n    delta_half = perturbation_config[\"delta_half_len\"]\n    delta_yaw = perturbation_config[\"delta_yaw\"]\n\n    for i in range(len(spec.region_infos)):\n        spec.region_infos[i] = perturb_region_info(\n            spec.region_infos[i],\n            delta_region_centroid_xy=delta_xy,\n            delta_region_half_len=delta_half,\n            delta_yaw_rotation=delta_yaw,\n        )\n\n    os.makedirs(output_dir, exist_ok=True)\n    base_name = Path(base_bddl_path).stem\n    dx, dy = delta_xy\n    filename = f\"{base_name}_spatial_dx{dx:.2f}_dy{dy:.2f}.bddl\"\n    _, filepath = save_bddl_file(spec, bddl_filename=filename, bddl_dirpath=output_dir)\n    return filepath\n\n\n# ---------------------------------------------------------------------------\n# Episode rollout\n# ---------------------------------------------------------------------------\n\ndef rollout_episode(\n    policy: object,\n    env: object,\n    task_description: str,\n    init_states: np.ndarray,\n    init_state_idx: int,\n    seed: int,\n) -> dict[str, Any]:\n    \"\"\"Run one episode, collecting (obs, action) pairs.\n\n    Returns dict with observations, actions, success, num_steps.\n    \"\"\"\n    env.seed(seed)\n    obs = env.set_init_state(init_states[init_state_idx])\n\n    for _ in range(NUM_STEPS_WAIT):\n        obs, _, _, _ = env.step(LIBERO_DUMMY_ACTION)\n\n    all_obs = [extract_obs_for_saving(obs)]\n    all_actions = []\n    action_plan = collections.deque()\n    step = 0\n    success = False\n    done = False\n\n    while not done and step < MAX_STEPS:\n        if len(action_plan) == 0:\n            obs_dict = obs_to_model_input(obs, task_description)\n            result = policy.infer(obs_dict)\n            action_chunk = result[\"actions\"]\n            action_plan.extend(action_chunk[:REPLAN_STEPS])\n\n        action = action_plan.popleft()\n        if isinstance(action, torch.Tensor):\n            action = action.cpu().numpy()\n        action_np = np.asarray(action, dtype=np.float32)\n\n        obs, reward, done, info = env.step(\n            action_np.tolist() if hasattr(action_np, \"tolist\") else list(action_np)\n        )\n        step += 1\n\n        all_obs.append(extract_obs_for_saving(obs))\n        all_actions.append(action_np)\n\n        if done or reward > 0:\n            success = info.get(\"success\", reward > 0)\n\n    return {\n        \"observations\": all_obs,\n        \"actions\": np.stack(all_actions) if all_actions else np.zeros((0, 7)),\n        \"success\": success,\n        \"num_steps\": step,\n    }\n\n\n# ---------------------------------------------------------------------------\n# Collection loops\n# ---------------------------------------------------------------------------\n\ndef collect_physical(\n    policy: object,\n    tasks: list[dict],\n    episodes_per_config: int,\n    output_dir: str,\n    dry_run: bool,\n) -> dict:\n    \"\"\"Collect expert demos with physical (robot initial state) perturbation.\n\n    Uses init_states indices 1-49 (index 0 is nominal).\n    \"\"\"\n    os.makedirs(output_dir, exist_ok=True)\n    stats = {\"total\": 0, \"success\": 0, \"saved_files\": []}\n\n    init_state_indices = list(range(1, 50))  # 49 perturbed states\n    if dry_run:\n        tasks = tasks[:1]\n        init_state_indices = [1]\n        episodes_per_config = 1\n\n    for task_info in tasks:\n        task_name = task_info[\"name\"]\n        init_states = torch.load(task_info[\"init_states_path\"], weights_only=False)\n        language = get_task_language(task_info[\"bddl_path\"])\n        log.info(\"Task: %s (%d init_states available)\", task_name, len(init_states))\n\n        for idx in init_state_indices:\n            if idx >= len(init_states):\n                continue\n\n            for ep in range(episodes_per_config):\n                seed = hash((task_name, idx, ep)) % (2**31)\n                stats[\"total\"] += 1\n\n                try:\n                    env = create_env(task_info[\"bddl_path\"])\n                    result = rollout_episode(\n                        policy, env, language, init_states, idx, seed\n                    )\n                    env.close()\n                except Exception:\n                    log.exception(\n                        \"Episode failed: task=%s idx=%d ep=%d\", task_name, idx, ep\n                    )\n                    continue\n\n                if result[\"success\"]:\n                    stats[\"success\"] += 1\n                    demo = {\n                        \"observations\": result[\"observations\"],\n                        \"actions\": result[\"actions\"],\n                        \"task_name\": task_name,\n                        \"perturbation_config\": {\n                            \"type\": \"physical\",\n                            \"init_state_idx\": idx,\n                        },\n                        \"success\": True,\n                        \"num_steps\": result[\"num_steps\"],\n                    }\n                    fname = f\"{task_name}_initstate{idx}_ep{ep}.pkl\"\n                    fpath = os.path.join(output_dir, fname)\n                    with open(fpath, \"wb\") as f:\n                        pickle.dump(demo, f, protocol=pickle.HIGHEST_PROTOCOL)\n                    stats[\"saved_files\"].append(fpath)\n\n                rate = stats[\"success\"] / stats[\"total\"] * 100\n                log.info(\n                    \"[physical] task=%s idx=%d ep=%d | %s | \"\n                    \"cumulative %d/%d (%.1f%%)\",\n                    task_name, idx, ep,\n                    \"SUCCESS\" if result[\"success\"] else \"FAIL\",\n                    stats[\"success\"], stats[\"total\"], rate,\n                )\n\n    return stats\n\n\ndef collect_spatial(\n    policy: object,\n    tasks: list[dict],\n    episodes_per_config: int,\n    output_dir: str,\n    dry_run: bool,\n) -> dict:\n    \"\"\"Collect expert demos with spatial (objects layout) perturbation.\n\n    Applies 10 predefined spatial perturbation configs to each base task.\n    \"\"\"\n    os.makedirs(output_dir, exist_ok=True)\n    tmp_bddl_dir = os.path.join(output_dir, \"_tmp_bddl\")\n    os.makedirs(tmp_bddl_dir, exist_ok=True)\n    stats = {\"total\": 0, \"success\": 0, \"saved_files\": []}\n\n    configs = SPATIAL_PERTURBATION_CONFIGS\n    if dry_run:\n        tasks = tasks[:1]\n        configs = configs[:1]\n        episodes_per_config = 1\n\n    for task_info in tasks:\n        task_name = task_info[\"name\"]\n        init_states = torch.load(task_info[\"init_states_path\"], weights_only=False)\n        log.info(\"Task: %s\", task_name)\n\n        for cfg_idx, cfg in enumerate(configs):\n            try:\n                perturbed_bddl = create_spatial_bddl(\n                    task_info[\"bddl_path\"], cfg, tmp_bddl_dir\n                )\n                language = get_task_language(perturbed_bddl)\n            except Exception:\n                log.exception(\n                    \"BDDL perturbation failed: task=%s cfg=%d\", task_name, cfg_idx\n                )\n                continue\n\n            for ep in range(episodes_per_config):\n                seed = hash((task_name, cfg_idx, ep)) % (2**31)\n                stats[\"total\"] += 1\n\n                try:\n                    env = create_env(perturbed_bddl)\n                    # Use nominal init_state (index 0) for spatial perturbation\n                    result = rollout_episode(\n                        policy, env, language, init_states, 0, seed\n                    )\n                    env.close()\n                except Exception:\n                    log.exception(\n                        \"Episode failed: task=%s cfg=%d ep=%d\",\n                        task_name, cfg_idx, ep,\n                    )\n                    continue\n\n                if result[\"success\"]:\n                    stats[\"success\"] += 1\n                    demo = {\n                        \"observations\": result[\"observations\"],\n                        \"actions\": result[\"actions\"],\n                        \"task_name\": task_name,\n                        \"perturbation_config\": {\n                            \"type\": \"spatial\",\n                            \"config_idx\": cfg_idx,\n                            \"delta_xy\": cfg[\"delta_xy\"],\n                            \"delta_half_len\": cfg[\"delta_half_len\"],\n                            \"delta_yaw\": cfg[\"delta_yaw\"],\n                        },\n                        \"success\": True,\n                        \"num_steps\": result[\"num_steps\"],\n                    }\n                    fname = f\"{task_name}_spatial{cfg_idx}_ep{ep}.pkl\"\n                    fpath = os.path.join(output_dir, fname)\n                    with open(fpath, \"wb\") as f:\n                        pickle.dump(demo, f, protocol=pickle.HIGHEST_PROTOCOL)\n                    stats[\"saved_files\"].append(fpath)\n\n                rate = stats[\"success\"] / stats[\"total\"] * 100\n                log.info(\n                    \"[spatial] task=%s cfg=%d ep=%d | %s | \"\n                    \"cumulative %d/%d (%.1f%%)\",\n                    task_name, cfg_idx, ep,\n                    \"SUCCESS\" if result[\"success\"] else \"FAIL\",\n                    stats[\"success\"], stats[\"total\"], rate,\n                )\n\n    return stats\n\n\n# ---------------------------------------------------------------------------\n# Main\n# ---------------------------------------------------------------------------\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Collect expert demos from π₀ in perturbed LIBERO environments\"\n    )\n    parser.add_argument(\n        \"--perturbation_type\", type=str, required=True,\n        choices=[\"physical\", \"spatial\"],\n    )\n    parser.add_argument(\"--gpu_id\", type=int, default=0)\n    parser.add_argument(\"--num_tasks\", type=int, default=10)\n    parser.add_argument(\"--episodes_per_config\", type=int, default=3)\n    parser.add_argument(\n        \"--output_dir\", type=str, default=None,\n        help=\"Override output directory (default: auto from perturbation_type)\",\n    )\n    parser.add_argument(\n        \"--checkpoint\", type=str,\n        default=\"/root/autodl-tmp/checkpoints/pi0_base\",\n    )\n    parser.add_argument(\"--dry_run\", action=\"store_true\")\n    parser.add_argument(\"--seed\", type=int, default=42)\n    args = parser.parse_args()\n\n    logging.basicConfig(\n        level=logging.INFO,\n        format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    )\n\n    random.seed(args.seed)\n    np.random.seed(args.seed)\n    torch.manual_seed(args.seed)\n\n    if args.output_dir is None:\n        args.output_dir = (\n            f\"/root/meta_brain_lora_routing/data/expert_demos/{args.perturbation_type}\"\n        )\n\n    device = f\"cuda:{args.gpu_id}\"\n    log.info(\n        \"Config: type=%s device=%s num_tasks=%d eps_per_cfg=%d dry_run=%s\",\n        args.perturbation_type, device, args.num_tasks,\n        args.episodes_per_config, args.dry_run,\n    )\n\n    log.info(\"Loading π₀ from %s\", args.checkpoint)\n    policy = load_pi0_policy(args.checkpoint, device)\n\n    from libero.libero import get_libero_path\n    bddl_dir = os.path.join(get_libero_path(\"bddl_files\"), BASE_TASK_SUITE)\n    tasks = find_base_tasks(bddl_dir, num_tasks=args.num_tasks)\n\n    if not tasks:\n        log.error(\"No base tasks found in %s\", bddl_dir)\n        sys.exit(1)\n\n    t0 = time.time()\n\n    if args.perturbation_type == \"physical\":\n        stats = collect_physical(\n            policy, tasks, args.episodes_per_config,\n            args.output_dir, args.dry_run,\n        )\n    else:\n        stats = collect_spatial(\n            policy, tasks, args.episodes_per_config,\n            args.output_dir, args.dry_run,\n        )\n\n    elapsed = time.time() - t0\n\n    total_size = sum(\n        os.path.getsize(f) for f in stats[\"saved_files\"] if os.path.exists(f)\n    )\n    log.info(\"=\" * 60)\n    log.info(\"Collection complete: %s\", args.perturbation_type)\n    log.info(\"  Total episodes:  %d\", stats[\"total\"])\n    log.info(\"  Successful:      %d\", stats[\"success\"])\n    log.info(\n        \"  Success rate:    %.1f%%\",\n        stats[\"success\"] / max(stats[\"total\"], 1) * 100,\n    )\n    log.info(\"  Files saved:     %d\", len(stats[\"saved_files\"]))\n    log.info(\"  Total size:      %.1f MB\", total_size / 1024 / 1024)\n    log.info(\"  Elapsed:         %.1f min\", elapsed / 60)\n    log.info(\"  Output dir:      %s\", args.output_dir)\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 598,
      "startLine": 1,
      "totalLines": 598
    }
  }
}
```

</details>

---


### Tool result

_source line 100 · 2026-05-15T17:51:19.650Z_

<details><summary>↩ Tool result · `toolu_01WjxwLeN3wnEH8KFdNDWGha`</summary>

```text
1	"""
2	OpenPI/LIBERO-Plus integration for pi0 activation collection.
3	
4	Bridges LIBERO-Plus simulation environments with the pi0 model, handling
5	observation preprocessing, action chunking, and perturbation-specific
6	task selection. Designed for direct model inference (no WebSocket server)
7	so that ActivationCollector hooks fire during forward passes.
8	
9	Input:
10	    LIBERO-Plus env observations: agentview_image [256,256,3],
11	    robot0_eye_in_hand_image [256,256,3], robot0_eef_pos [3],
12	    robot0_eef_quat [4], robot0_gripper_qpos [2], plus task language.
13	
14	Output:
15	    Per-episode activation dict (via ActivationCollector hooks on the
16	    underlying PI0Pytorch model) and task metadata.
17	
18	Integration with collect_activations.py:
19	    from libero_integration import load_pi0_for_collection, run_episode
20	
21	    policy, model = load_pi0_for_collection(checkpoint_path, device)
22	    collector = ActivationCollector(model)
23	    collector.register_hooks()
24	    result = run_episode(policy, collector, "camera_viewpoints", device)
25	"""
26	
27	import collections
28	import logging
29	import math
30	import re
31	import random
32	from pathlib import Path
33	from typing import Any
34	
35	import numpy as np
36	import torch
37	import torch.nn as nn
38	
39	log = logging.getLogger(__name__)
40	
41	# ---------------------------------------------------------------------------
42	# Constants (from OpenPI's examples/libero/main.py)
43	# ---------------------------------------------------------------------------
44	
45	LIBERO_DUMMY_ACTION = [0.0] * 6 + [-1.0]
46	LIBERO_ENV_RESOLUTION = 256
47	MODEL_INPUT_RESOLUTION = 224
48	DEFAULT_REPLAN_STEPS = 5
49	DEFAULT_NUM_STEPS_WAIT = 10
50	
51	MAX_STEPS = {
52	    "libero_spatial": 220,
53	    "libero_object": 280,
54	    "libero_goal": 300,
55	    "libero_10": 520,
56	    "libero_90": 400,
57	}
58	
59	VALID_PERTURBATION_TYPES = [
60	    "camera_viewpoints",
61	    "light_conditions",
62	    "background_textures",
63	    "objects_layout",
64	    "robot_initial_states",
65	    "sensor_noise",
66	]
67	
68	
69	# ---------------------------------------------------------------------------
70	# Geometry helpers
71	# ---------------------------------------------------------------------------
72	
73	def _quat2axisangle(quat: np.ndarray) -> np.ndarray:
74	    """Quaternion [x,y,z,w] -> axis-angle [ax,ay,az]."""
75	    q = np.asarray(quat, dtype=np.float64)
76	    norm = np.linalg.norm(q)
77	    if norm < 1e-8:
78	        return np.zeros(3, dtype=np.float32)
79	    q /= norm
80	    sin_half = np.linalg.norm(q[:3])
81	    if sin_half < 1e-8:
82	        return np.zeros(3, dtype=np.float32)
83	    angle = 2.0 * math.atan2(sin_half, q[3])
84	    axis = q[:3] / sin_half
85	    return (axis * angle).astype(np.float32)
86	
87	
88	# ---------------------------------------------------------------------------
89	# Image preprocessing
90	# ---------------------------------------------------------------------------
91	
92	def _resize_with_pad(img: np.ndarray, size: int) -> np.ndarray:
93	    """Resize image with aspect-preserving padding to (size, size, 3) uint8."""
94	    try:
95	        from openpi_client.image_tools import resize_with_pad, convert_to_uint8
96	        return convert_to_uint8(resize_with_pad(img, size, size))
97	    except ImportError:
98	        from PIL import Image as PILImage
99	        h, w = img.shape[:2]
100	        scale = min(size / h, size / w)
101	        new_h, new_w = int(h * scale), int(w * scale)
102	        resized = np.array(
103	            PILImage.fromarray(img).resize((new_w, new_h), PILImage.BILINEAR)
104	        )
105	        canvas = np.zeros((size, size, 3), dtype=np.uint8)
106	        y0, x0 = (size - new_h) // 2, (size - new_w) // 2
107	        canvas[y0 : y0 + new_h, x0 : x0 + new_w] = resized
108	        return canvas
109	
110	
111	# ---------------------------------------------------------------------------
112	# Observation -> model input
113	# ---------------------------------------------------------------------------
114	
115	def obs_to_model_input(
116	    obs: dict,
117	    task_description: str,
118	    resize_size: int = MODEL_INPUT_RESOLUTION,
119	) -> dict:
120	    """Convert LIBERO observation to the dict format expected by policy.infer().
121	
122	    LIBERO obs keys used:
123	        agentview_image          [H, W, 3] uint8
124	        robot0_eye_in_hand_image [H, W, 3] uint8
125	        robot0_eef_pos           [3] float
126	        robot0_eef_quat          [4] float (x,y,z,w)
127	        robot0_gripper_qpos      [2] float
128	
129	    Returns dict with keys:
130	        observation/image        [224, 224, 3] uint8
131	        observation/wrist_image  [224, 224, 3] uint8
132	        observation/state        [8] float32
133	        prompt                   str
134	
135	    Note: sensor noise is applied by the LIBERO-Plus environment itself
136	    (motion_blur, gaussian_blur, zoom_blur, fog, glass_blur at various
137	    severity levels), not at the observation preprocessing stage.
138	    """
139	    # Flip images 180 degrees (OpenPI training convention)
140	    base_img = np.ascontiguousarray(obs["agentview_image"][::-1, ::-1])
141	    wrist_img = np.ascontiguousarray(obs["robot0_eye_in_hand_image"][::-1, ::-1])
142	
143	    base_img = _resize_with_pad(base_img, resize_size)
144	    wrist_img = _resize_with_pad(wrist_img, resize_size)
145	
146	    state = np.concatenate([
147	        obs["robot0_eef_pos"].astype(np.float32),
148	        _quat2axisangle(obs["robot0_eef_quat"]),
149	        obs["robot0_gripper_qpos"].astype(np.float32),
150	    ])  # [8]
151	
152	    return {
153	        "observation/image": base_img,
154	        "observation/wrist_image": wrist_img,
155	        "observation/state": state,
156	        "prompt": task_description,
157	    }
158	
159	
160	# ---------------------------------------------------------------------------
161	# Model loading
162	# ---------------------------------------------------------------------------
163	
164	def _extract_model(policy: object) -> nn.Module:
165	    """Extract the underlying PI0Pytorch nn.Module from an OpenPI Policy."""
166	    for attr in ("_model", "model", "_network", "network"):
167	        candidate = getattr(policy, attr, None)
168	        if isinstance(candidate, nn.Module):
169	            return candidate
170	
171	    for attr in dir(policy):
172	        if attr.startswith("__"):
173	            continue
174	        try:
175	            candidate = getattr(policy, attr)
176	            if isinstance(candidate, nn.Module):
177	                log.warning(
178	                    "Found model at policy.%s (unexpected attribute name)", attr
179	                )
180	                return candidate
181	        except Exception:
182	            continue
183	
184	    raise AttributeError(
185	        "Cannot find nn.Module in Policy object. "
186	        "Inspect the OpenPI Policy class and update _extract_model()."
187	    )
188	
189	
190	def _ensure_openpi_imports():
191	    """Stub out lerobot (training-only dep) before importing OpenPI inference code."""
192	    import sys
193	    import types
194	    for mod in [
195	        "lerobot", "lerobot.common", "lerobot.common.datasets",
196	        "lerobot.common.datasets.lerobot_dataset",
197	    ]:
198	        if mod not in sys.modules:
199	            sys.modules[mod] = types.ModuleType(mod)
200	
201	
202	def load_pi0_for_collection(
203	    checkpoint_path: str,
204	    device: str,
205	    config_name: str = "pi0_libero",
206	) -> tuple[object, nn.Module]:
207	    """Load pi0 via OpenPI's policy system for activation collection.
208	
209	    Uses create_trained_policy() so all transforms (LiberoInputs, Normalize,
210	    TokenizePrompt, PadStatesAndActions, ResizeImages) and normalization
211	    statistics are applied correctly.
212	
213	    Returns:
214	        (policy, model) where
215	        - policy: OpenPI Policy; call policy.infer(obs_dict)
216	        - model:  PI0Pytorch nn.Module; pass to ActivationCollector
217	    """
218	    _ensure_openpi_imports()
219	
220	    try:
221	        from openpi.training import config as _config
222	        from openpi.policies import policy_config
223	    except ImportError:
224	        raise ImportError(
225	            "openpi package required. "
226	            "Clone https://github.com/Physical-Intelligence/openpi "
227	            "and install with: pip install -e ."
228	        )
229	
230	    train_config = _config.get_config(config_name)
231	    policy = policy_config.create_trained_policy(
232	        train_config, checkpoint_path, pytorch_device=device
233	    )
234	
235	    model = _extract_model(policy)
236	    log.info("Loaded pi0 policy (config=%s) on %s", config_name, device)
237	    return policy, model
238	
239	
240	# ---------------------------------------------------------------------------
241	# LIBERO-Plus environment
242	# ---------------------------------------------------------------------------
243	
244	def _classify_task(task_name: str) -> str | None:
245	    """Classify a LIBERO-Plus task name into its perturbation type.
246	
247	    LIBERO-Plus task naming conventions:
248	      Compound: {base}_[language_N_]view_{H}_{V}_{S}_{R}_{E}_initstate_{I}[_noise_{N}]
249	        - camera_viewpoints:    (H,V,S,R,E) != (0,0,100,0,0), I==0, no noise
250	        - robot_initial_states: default view, I != 0, no noise
251	        - sensor_noise:         default view, I==0, N > 0
252	        - base (nominal):       all defaults
253	      Simple suffixes:
254	        - light_conditions:     _light_\\d+
255	        - background_textures:  _table_\\d+ or _tb_\\d+
256	        - objects_layout:       _add_\\d+ or _level\\d+
257	
258	    Returns perturbation type string, or None for base/nominal tasks.
259	    """
260	    if "_view_" in task_name:
261	        m = re.search(
262	            r"_view_(-?\d+)_(-?\d+)_(\d+)_(-?\d+)_(-?\d+)_initstate_(\d+)(?:_noise_(\d+))?",
263	            task_name,
264	        )
265	        if not m:
266	            return None
267	        H, V, S, R, E = int(m[1]), int(m[2]), int(m[3]), int(m[4]), int(m[5])
268	        initstate = int(m[6])
269	        noise = int(m[7]) if m[7] else 0
270	
271	        if noise > 0:
272	            return "sensor_noise"
273	        if (H, V, S, R, E) != (0, 0, 100, 0, 0):
274	            return "camera_viewpoints"
275	        if initstate != 0:
276	            return "robot_initial_states"
277	        return None
278	
279	    if re.search(r"_light_\d+$", task_name):
280	        return "light_conditions"
281	    if re.search(r"_(?:table|tb)_\d+$", task_name):
282	        return "background_textures"
283	    if re.search(r"_add_\d+$", task_name) or re.search(r"_level\d+", task_name):
284	        return "objects_layout"
285	
286	    return None
287	
288	
289	def _get_task_indices(
290	    suite: object,
291	    perturbation_type: str | None,
292	    num_tasks: int,
293	) -> list[int]:
294	    """Return task indices matching the requested perturbation type."""
295	    if perturbation_type is not None and perturbation_type not in VALID_PERTURBATION_TYPES:
296	        raise ValueError(
297	            f"Unknown perturbation_type={perturbation_type!r}. "
298	            f"Valid: {VALID_PERTURBATION_TYPES}"
299	        )
300	
301	    indices = []
302	    matched_names = []
303	    for i in range(num_tasks):
304	        task = suite.get_task(i)
305	        name = getattr(task, "name", "") or getattr(task, "bddl_file", "")
306	        classified = _classify_task(name)
307	
308	        if perturbation_type is None:
309	            if classified is None:
310	                indices.append(i)
311	                matched_names.append(name)
312	        elif classified == perturbation_type:
313	            indices.append(i)
314	            matched_names.append(name)
315	
316	    if not indices:
317	        raise RuntimeError(
318	            f"No tasks match perturbation_type={perturbation_type!r} "
319	            f"among {num_tasks} tasks. Verify the suite contains "
320	            f"LIBERO-Plus perturbation variants (not base libero_90)."
321	        )
322	
323	    log.info(
324	        "%s: matched %d/%d tasks (e.g. %s)",
325	        perturbation_type or "nominal",
326	        len(indices),
327	        num_tasks,
328	        matched_names[:3],
329	    )
330	    return indices
331	
332	
333	def create_libero_env(
334	    task_suite_name: str = "libero_spatial",
335	    perturbation_type: str | None = None,
336	    task_idx: int | None = None,
337	    seed: int = 42,
338	) -> tuple[Any, str, np.ndarray, int]:
339	    """Create a LIBERO / LIBERO-Plus evaluation environment.
340	
341	    Returns:
342	        (env, task_description, init_states, selected_task_idx)
343	    """
344	    from libero.libero import benchmark, get_libero_path
345	    from libero.libero.envs import OffScreenRenderEnv
346	
347	    benchmark_dict = benchmark.get_benchmark_dict()
348	    suite = benchmark_dict[task_suite_name]()
349	    num_tasks = suite.n_tasks
350	
351	    valid_indices = _get_task_indices(suite, perturbation_type, num_tasks)
352	
353	    if task_idx is not None and task_idx in valid_indices:
354	        selected_idx = task_idx
355	    else:
356	        selected_idx = random.choice(valid_indices)
357	
358	    task = suite.get_task(selected_idx)
359	    task_description = task.language
360	
361	    task_bddl_file = (
362	        Path(get_libero_path("bddl_files")) / task.problem_folder / task.bddl_file
363	    )
364	    env = OffScreenRenderEnv(
365	        bddl_file_name=str(task_bddl_file),
366	        camera_heights=LIBERO_ENV_RESOLUTION,
367	        camera_widths=LIBERO_ENV_RESOLUTION,
368	    )
369	    env.seed(seed)
370	
371	    init_states = suite.get_task_init_states(selected_idx)
372	    return env, task_description, init_states, selected_idx
373	
374	
375	# ---------------------------------------------------------------------------
376	# Episode rollout
377	# ---------------------------------------------------------------------------
378	
379	def run_episode(
380	    policy: object,
381	    collector: object,
382	    perturbation_type: str | None,
383	    device: str,
384	    task_suite: str = "libero_spatial",
385	    seed: int = 42,
386	    replan_steps: int = DEFAULT_REPLAN_STEPS,
387	    num_steps_wait: int = DEFAULT_NUM_STEPS_WAIT,
388	) -> dict[str, Any]:
389	    """Run one LIBERO-Plus episode, collecting activations at each replan point.
390	
391	    Every replan_steps env steps, the policy is queried for a new action chunk.
392	    ActivationCollector hooks capture layer outputs during each policy.infer()
393	    call. Activations are averaged across all replan points.
394	
395	    Sensor noise is applied by the LIBERO-Plus environment itself (via task
396	    name suffix _noise_N), not at the observation level.
397	
398	    Returns dict with keys: activations, task_name, task_description,
399	    num_steps, success.
400	    """
401	    env, task_description, init_states, task_idx = create_libero_env(
402	        task_suite_name=task_suite,
403	        perturbation_type=perturbation_type,
404	        seed=seed,
405	    )
406	
407	    max_steps = MAX_STEPS.get(task_suite, 400)
408	
409	    step = 0
410	    success = False
411	
412	    try:
413	        trial_idx = random.randint(0, len(init_states) - 1)
414	        obs = env.set_init_state(init_states[trial_idx])
415	
416	        for _ in range(num_steps_wait):
417	            obs, _, _, _ = env.step(LIBERO_DUMMY_ACTION)
418	
419	        action_plan: collections.deque = collections.deque()
420	        step_activations: list[dict] = []
421	        done = False
422	
423	        while not done and step < max_steps:
424	            if len(action_plan) == 0:
425	                collector.clear()
426	
427	                obs_dict = obs_to_model_input(obs, task_description)
428	                result = policy.infer(obs_dict)
429	                action_chunk = result["actions"]  # [horizon, 7]
430	                action_plan.extend(action_chunk[:replan_steps])
431	
432	                pooled = collector.get_pooled()
433	                if pooled:
434	                    step_activations.append(pooled)
435	
436	            action = action_plan.popleft()
437	            if isinstance(action, torch.Tensor):
438	                action = action.cpu().numpy()
439	            obs, reward, done, info = env.step(
440	                action.tolist() if hasattr(action, "tolist") else list(action)
441	            )
442	            step += 1
443	
444	            if done or reward > 0:
445	                success = info.get("success", reward > 0)
446	    finally:
447	        env.close()
448	
449	    return {
450	        "activations": _average_activations(step_activations),
451	        "task_name": f"{task_suite}/task_{task_idx}",
452	        "task_description": task_description,
453	        "num_steps": step,
454	        "success": success,
455	    }
456	
457	
458	def _average_activations(
459	    step_activations: list[dict[str, dict[str, torch.Tensor]]],
460	) -> dict[str, dict[str, torch.Tensor]]:
461	    """Average activation tensors across replan steps."""
462	    if not step_activations:
463	        return {}
464	    result: dict[str, dict[str, torch.Tensor]] = {}
465	    for layer in step_activations[0]:
466	        result[layer] = {}
467	        for strat in step_activations[0][layer]:
468	            tensors = [sa[layer][strat] for sa in step_activations]
469	            result[layer][strat] = torch.stack(tensors).mean(dim=0)
470	    return result
471	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "3e4d36cb-909f-4758-bf30-d40ab46212c7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/libero_integration.py",
      "content": "\"\"\"\nOpenPI/LIBERO-Plus integration for pi0 activation collection.\n\nBridges LIBERO-Plus simulation environments with the pi0 model, handling\nobservation preprocessing, action chunking, and perturbation-specific\ntask selection. Designed for direct model inference (no WebSocket server)\nso that ActivationCollector hooks fire during forward passes.\n\nInput:\n    LIBERO-Plus env observations: agentview_image [256,256,3],\n    robot0_eye_in_hand_image [256,256,3], robot0_eef_pos [3],\n    robot0_eef_quat [4], robot0_gripper_qpos [2], plus task language.\n\nOutput:\n    Per-episode activation dict (via ActivationCollector hooks on the\n    underlying PI0Pytorch model) and task metadata.\n\nIntegration with collect_activations.py:\n    from libero_integration import load_pi0_for_collection, run_episode\n\n    policy, model = load_pi0_for_collection(checkpoint_path, device)\n    collector = ActivationCollector(model)\n    collector.register_hooks()\n    result = run_episode(policy, collector, \"camera_viewpoints\", device)\n\"\"\"\n\nimport collections\nimport logging\nimport math\nimport re\nimport random\nfrom pathlib import Path\nfrom typing import Any\n\nimport numpy as np\nimport torch\nimport torch.nn as nn\n\nlog = logging.getLogger(__name__)\n\n# ---------------------------------------------------------------------------\n# Constants (from OpenPI's examples/libero/main.py)\n# ---------------------------------------------------------------------------\n\nLIBERO_DUMMY_ACTION = [0.0] * 6 + [-1.0]\nLIBERO_ENV_RESOLUTION = 256\nMODEL_INPUT_RESOLUTION = 224\nDEFAULT_REPLAN_STEPS = 5\nDEFAULT_NUM_STEPS_WAIT = 10\n\nMAX_STEPS = {\n    \"libero_spatial\": 220,\n    \"libero_object\": 280,\n    \"libero_goal\": 300,\n    \"libero_10\": 520,\n    \"libero_90\": 400,\n}\n\nVALID_PERTURBATION_TYPES = [\n    \"camera_viewpoints\",\n    \"light_conditions\",\n    \"background_textures\",\n    \"objects_layout\",\n    \"robot_initial_states\",\n    \"sensor_noise\",\n]\n\n\n# ---------------------------------------------------------------------------\n# Geometry helpers\n# ---------------------------------------------------------------------------\n\ndef _quat2axisangle(quat: np.ndarray) -> np.ndarray:\n    \"\"\"Quaternion [x,y,z,w] -> axis-angle [ax,ay,az].\"\"\"\n    q = np.asarray(quat, dtype=np.float64)\n    norm = np.linalg.norm(q)\n    if norm < 1e-8:\n        return np.zeros(3, dtype=np.float32)\n    q /= norm\n    sin_half = np.linalg.norm(q[:3])\n    if sin_half < 1e-8:\n        return np.zeros(3, dtype=np.float32)\n    angle = 2.0 * math.atan2(sin_half, q[3])\n    axis = q[:3] / sin_half\n    return (axis * angle).astype(np.float32)\n\n\n# ---------------------------------------------------------------------------\n# Image preprocessing\n# ---------------------------------------------------------------------------\n\ndef _resize_with_pad(img: np.ndarray, size: int) -> np.ndarray:\n    \"\"\"Resize image with aspect-preserving padding to (size, size, 3) uint8.\"\"\"\n    try:\n        from openpi_client.image_tools import resize_with_pad, convert_to_uint8\n        return convert_to_uint8(resize_with_pad(img, size, size))\n    except ImportError:\n        from PIL import Image as PILImage\n        h, w = img.shape[:2]\n        scale = min(size / h, size / w)\n        new_h, new_w = int(h * scale), int(w * scale)\n        resized = np.array(\n            PILImage.fromarray(img).resize((new_w, new_h), PILImage.BILINEAR)\n        )\n        canvas = np.zeros((size, size, 3), dtype=np.uint8)\n        y0, x0 = (size - new_h) // 2, (size - new_w) // 2\n        canvas[y0 : y0 + new_h, x0 : x0 + new_w] = resized\n        return canvas\n\n\n# ---------------------------------------------------------------------------\n# Observation -> model input\n# ---------------------------------------------------------------------------\n\ndef obs_to_model_input(\n    obs: dict,\n    task_description: str,\n    resize_size: int = MODEL_INPUT_RESOLUTION,\n) -> dict:\n    \"\"\"Convert LIBERO observation to the dict format expected by policy.infer().\n\n    LIBERO obs keys used:\n        agentview_image          [H, W, 3] uint8\n        robot0_eye_in_hand_image [H, W, 3] uint8\n        robot0_eef_pos           [3] float\n        robot0_eef_quat          [4] float (x,y,z,w)\n        robot0_gripper_qpos      [2] float\n\n    Returns dict with keys:\n        observation/image        [224, 224, 3] uint8\n        observation/wrist_image  [224, 224, 3] uint8\n        observation/state        [8] float32\n        prompt                   str\n\n    Note: sensor noise is applied by the LIBERO-Plus environment itself\n    (motion_blur, gaussian_blur, zoom_blur, fog, glass_blur at various\n    severity levels), not at the observation preprocessing stage.\n    \"\"\"\n    # Flip images 180 degrees (OpenPI training convention)\n    base_img = np.ascontiguousarray(obs[\"agentview_image\"][::-1, ::-1])\n    wrist_img = np.ascontiguousarray(obs[\"robot0_eye_in_hand_image\"][::-1, ::-1])\n\n    base_img = _resize_with_pad(base_img, resize_size)\n    wrist_img = _resize_with_pad(wrist_img, resize_size)\n\n    state = np.concatenate([\n        obs[\"robot0_eef_pos\"].astype(np.float32),\n        _quat2axisangle(obs[\"robot0_eef_quat\"]),\n        obs[\"robot0_gripper_qpos\"].astype(np.float32),\n    ])  # [8]\n\n    return {\n        \"observation/image\": base_img,\n        \"observation/wrist_image\": wrist_img,\n        \"observation/state\": state,\n        \"prompt\": task_description,\n    }\n\n\n# ---------------------------------------------------------------------------\n# Model loading\n# ---------------------------------------------------------------------------\n\ndef _extract_model(policy: object) -> nn.Module:\n    \"\"\"Extract the underlying PI0Pytorch nn.Module from an OpenPI Policy.\"\"\"\n    for attr in (\"_model\", \"model\", \"_network\", \"network\"):\n        candidate = getattr(policy, attr, None)\n        if isinstance(candidate, nn.Module):\n            return candidate\n\n    for attr in dir(policy):\n        if attr.startswith(\"__\"):\n            continue\n        try:\n            candidate = getattr(policy, attr)\n            if isinstance(candidate, nn.Module):\n                log.warning(\n                    \"Found model at policy.%s (unexpected attribute name)\", attr\n                )\n                return candidate\n        except Exception:\n            continue\n\n    raise AttributeError(\n        \"Cannot find nn.Module in Policy object. \"\n        \"Inspect the OpenPI Policy class and update _extract_model().\"\n    )\n\n\ndef _ensure_openpi_imports():\n    \"\"\"Stub out lerobot (training-only dep) before importing OpenPI inference code.\"\"\"\n    import sys\n    import types\n    for mod in [\n        \"lerobot\", \"lerobot.common\", \"lerobot.common.datasets\",\n        \"lerobot.common.datasets.lerobot_dataset\",\n    ]:\n        if mod not in sys.modules:\n            sys.modules[mod] = types.ModuleType(mod)\n\n\ndef load_pi0_for_collection(\n    checkpoint_path: str,\n    device: str,\n    config_name: str = \"pi0_libero\",\n) -> tuple[object, nn.Module]:\n    \"\"\"Load pi0 via OpenPI's policy system for activation collection.\n\n    Uses create_trained_policy() so all transforms (LiberoInputs, Normalize,\n    TokenizePrompt, PadStatesAndActions, ResizeImages) and normalization\n    statistics are applied correctly.\n\n    Returns:\n        (policy, model) where\n        - policy: OpenPI Policy; call policy.infer(obs_dict)\n        - model:  PI0Pytorch nn.Module; pass to ActivationCollector\n    \"\"\"\n    _ensure_openpi_imports()\n\n    try:\n        from openpi.training import config as _config\n        from openpi.policies import policy_config\n    except ImportError:\n        raise ImportError(\n            \"openpi package required. \"\n            \"Clone https://github.com/Physical-Intelligence/openpi \"\n            \"and install with: pip install -e .\"\n        )\n\n    train_config = _config.get_config(config_name)\n    policy = policy_config.create_trained_policy(\n        train_config, checkpoint_path, pytorch_device=device\n    )\n\n    model = _extract_model(policy)\n    log.info(\"Loaded pi0 policy (config=%s) on %s\", config_name, device)\n    return policy, model\n\n\n# ---------------------------------------------------------------------------\n# LIBERO-Plus environment\n# ---------------------------------------------------------------------------\n\ndef _classify_task(task_name: str) -> str | None:\n    \"\"\"Classify a LIBERO-Plus task name into its perturbation type.\n\n    LIBERO-Plus task naming conventions:\n      Compound: {base}_[language_N_]view_{H}_{V}_{S}_{R}_{E}_initstate_{I}[_noise_{N}]\n        - camera_viewpoints:    (H,V,S,R,E) != (0,0,100,0,0), I==0, no noise\n        - robot_initial_states: default view, I != 0, no noise\n        - sensor_noise:         default view, I==0, N > 0\n        - base (nominal):       all defaults\n      Simple suffixes:\n        - light_conditions:     _light_\\\\d+\n        - background_textures:  _table_\\\\d+ or _tb_\\\\d+\n        - objects_layout:       _add_\\\\d+ or _level\\\\d+\n\n    Returns perturbation type string, or None for base/nominal tasks.\n    \"\"\"\n    if \"_view_\" in task_name:\n        m = re.search(\n            r\"_view_(-?\\d+)_(-?\\d+)_(\\d+)_(-?\\d+)_(-?\\d+)_initstate_(\\d+)(?:_noise_(\\d+))?\",\n            task_name,\n        )\n        if not m:\n            return None\n        H, V, S, R, E = int(m[1]), int(m[2]), int(m[3]), int(m[4]), int(m[5])\n        initstate = int(m[6])\n        noise = int(m[7]) if m[7] else 0\n\n        if noise > 0:\n            return \"sensor_noise\"\n        if (H, V, S, R, E) != (0, 0, 100, 0, 0):\n            return \"camera_viewpoints\"\n        if initstate != 0:\n            return \"robot_initial_states\"\n        return None\n\n    if re.search(r\"_light_\\d+$\", task_name):\n        return \"light_conditions\"\n    if re.search(r\"_(?:table|tb)_\\d+$\", task_name):\n        return \"background_textures\"\n    if re.search(r\"_add_\\d+$\", task_name) or re.search(r\"_level\\d+\", task_name):\n        return \"objects_layout\"\n\n    return None\n\n\ndef _get_task_indices(\n    suite: object,\n    perturbation_type: str | None,\n    num_tasks: int,\n) -> list[int]:\n    \"\"\"Return task indices matching the requested perturbation type.\"\"\"\n    if perturbation_type is not None and perturbation_type not in VALID_PERTURBATION_TYPES:\n        raise ValueError(\n            f\"Unknown perturbation_type={perturbation_type!r}. \"\n            f\"Valid: {VALID_PERTURBATION_TYPES}\"\n        )\n\n    indices = []\n    matched_names = []\n    for i in range(num_tasks):\n        task = suite.get_task(i)\n        name = getattr(task, \"name\", \"\") or getattr(task, \"bddl_file\", \"\")\n        classified = _classify_task(name)\n\n        if perturbation_type is None:\n            if classified is None:\n                indices.append(i)\n                matched_names.append(name)\n        elif classified == perturbation_type:\n            indices.append(i)\n            matched_names.append(name)\n\n    if not indices:\n        raise RuntimeError(\n            f\"No tasks match perturbation_type={perturbation_type!r} \"\n            f\"among {num_tasks} tasks. Verify the suite contains \"\n            f\"LIBERO-Plus perturbation variants (not base libero_90).\"\n        )\n\n    log.info(\n        \"%s: matched %d/%d tasks (e.g. %s)\",\n        perturbation_type or \"nominal\",\n        len(indices),\n        num_tasks,\n        matched_names[:3],\n    )\n    return indices\n\n\ndef create_libero_env(\n    task_suite_name: str = \"libero_spatial\",\n    perturbation_type: str | None = None,\n    task_idx: int | None = None,\n    seed: int = 42,\n) -> tuple[Any, str, np.ndarray, int]:\n    \"\"\"Create a LIBERO / LIBERO-Plus evaluation environment.\n\n    Returns:\n        (env, task_description, init_states, selected_task_idx)\n    \"\"\"\n    from libero.libero import benchmark, get_libero_path\n    from libero.libero.envs import OffScreenRenderEnv\n\n    benchmark_dict = benchmark.get_benchmark_dict()\n    suite = benchmark_dict[task_suite_name]()\n    num_tasks = suite.n_tasks\n\n    valid_indices = _get_task_indices(suite, perturbation_type, num_tasks)\n\n    if task_idx is not None and task_idx in valid_indices:\n        selected_idx = task_idx\n    else:\n        selected_idx = random.choice(valid_indices)\n\n    task = suite.get_task(selected_idx)\n    task_description = task.language\n\n    task_bddl_file = (\n        Path(get_libero_path(\"bddl_files\")) / task.problem_folder / task.bddl_file\n    )\n    env = OffScreenRenderEnv(\n        bddl_file_name=str(task_bddl_file),\n        camera_heights=LIBERO_ENV_RESOLUTION,\n        camera_widths=LIBERO_ENV_RESOLUTION,\n    )\n    env.seed(seed)\n\n    init_states = suite.get_task_init_states(selected_idx)\n    return env, task_description, init_states, selected_idx\n\n\n# ---------------------------------------------------------------------------\n# Episode rollout\n# ---------------------------------------------------------------------------\n\ndef run_episode(\n    policy: object,\n    collector: object,\n    perturbation_type: str | None,\n    device: str,\n    task_suite: str = \"libero_spatial\",\n    seed: int = 42,\n    replan_steps: int = DEFAULT_REPLAN_STEPS,\n    num_steps_wait: int = DEFAULT_NUM_STEPS_WAIT,\n) -> dict[str, Any]:\n    \"\"\"Run one LIBERO-Plus episode, collecting activations at each replan point.\n\n    Every replan_steps env steps, the policy is queried for a new action chunk.\n    ActivationCollector hooks capture layer outputs during each policy.infer()\n    call. Activations are averaged across all replan points.\n\n    Sensor noise is applied by the LIBERO-Plus environment itself (via task\n    name suffix _noise_N), not at the observation level.\n\n    Returns dict with keys: activations, task_name, task_description,\n    num_steps, success.\n    \"\"\"\n    env, task_description, init_states, task_idx = create_libero_env(\n        task_suite_name=task_suite,\n        perturbation_type=perturbation_type,\n        seed=seed,\n    )\n\n    max_steps = MAX_STEPS.get(task_suite, 400)\n\n    step = 0\n    success = False\n\n    try:\n        trial_idx = random.randint(0, len(init_states) - 1)\n        obs = env.set_init_state(init_states[trial_idx])\n\n        for _ in range(num_steps_wait):\n            obs, _, _, _ = env.step(LIBERO_DUMMY_ACTION)\n\n        action_plan: collections.deque = collections.deque()\n        step_activations: list[dict] = []\n        done = False\n\n        while not done and step < max_steps:\n            if len(action_plan) == 0:\n                collector.clear()\n\n                obs_dict = obs_to_model_input(obs, task_description)\n                result = policy.infer(obs_dict)\n                action_chunk = result[\"actions\"]  # [horizon, 7]\n                action_plan.extend(action_chunk[:replan_steps])\n\n                pooled = collector.get_pooled()\n                if pooled:\n                    step_activations.append(pooled)\n\n            action = action_plan.popleft()\n            if isinstance(action, torch.Tensor):\n                action = action.cpu().numpy()\n            obs, reward, done, info = env.step(\n                action.tolist() if hasattr(action, \"tolist\") else list(action)\n            )\n            step += 1\n\n            if done or reward > 0:\n                success = info.get(\"success\", reward > 0)\n    finally:\n        env.close()\n\n    return {\n        \"activations\": _average_activations(step_activations),\n        \"task_name\": f\"{task_suite}/task_{task_idx}\",\n        \"task_description\": task_description,\n        \"num_steps\": step,\n        \"success\": success,\n    }\n\n\ndef _average_activations(\n    step_activations: list[dict[str, dict[str, torch.Tensor]]],\n) -> dict[str, dict[str, torch.Tensor]]:\n    \"\"\"Average activation tensors across replan steps.\"\"\"\n    if not step_activations:\n        return {}\n    result: dict[str, dict[str, torch.Tensor]] = {}\n    for layer in step_activations[0]:\n        result[layer] = {}\n        for strat in step_activations[0][layer]:\n            tensors = [sa[layer][strat] for sa in step_activations]\n            result[layer][strat] = torch.stack(tensors).mean(dim=0)\n    return result\n",
      "numLines": 471,
      "startLine": 1,
      "totalLines": 471
    }
  }
}
```

</details>

---


### Assistant

_source line 101_

<details><summary>Logged reasoning block</summary>

```text
Now I have a complete picture. Let me understand what needs to change:

1. The current `collect_spatial()` function uses `perturb_region_info()` to create modified BDDL files with XY shifts and yaw rotations.
2. We need to switch to using LIBERO-Plus's built-in `_add_N` tasks, which have distractor objects already defined in their BDDL files.
3. Phase 0's `libero_integration.py` already has the machinery to load `_add_N` tasks via `create_libero_env()` with `perturbation_type="objects_layout"`.


4. I'll add a `--spatial_mode` flag to toggle between the two approaches, then create a new function that discovers all `_add_N` tasks from the benchmark, iterates through them to generate episodes with their built-in distractor configurations, and saves the resulting demonstrations with proper metadata. Wire it up in `main()`. I need to add the `_classify_task()` function to filter for `_add_N` tasks, create a `discover_add_n_tasks()` function to find them, and write a `collect_spatial_add_n()` function to gather the data. Then I'll add the `--spatial_mode` argument and update the routing logic in `main()`.

Writing the modified script...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "9045da6d-2a8e-414b-bed0-0479762ddc80",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cbgjw9AidLhe2FM8hVJfEh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14130,
      "cache_read_input_tokens": 28930,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14130
      },
      "output_tokens": 9,
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

_source line 102_

Now I have the full picture. Let me modify `collect_expert_demos.py`:
- Add `_add_N` task discovery via LIBERO-Plus benchmark API
- New `collect_spatial_add_n()` function
- `--spatial_mode` argument (default `add_n`, fallback `perturb_region`)
- Keep old `perturb_region` code as alternative

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "b3fff3bf-607b-47df-b4ce-aac076f916c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cbgjw9AidLhe2FM8hVJfEh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14130,
      "cache_read_input_tokens": 28930,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14130
      },
      "output_tokens": 9,
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

_source line 103_

<details open><summary>🔧 Tool call — Edit · `toolu_01JRAUD81JxAdeZs7RP8Cnmb`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py",
  "old_string": "\"\"\"\nCollect expert demonstrations by rolling out frozen π₀ in perturbed LIBERO environments.\n\nOnly successful episodes are saved. Two perturbation types are supported:\n  - physical: vary robot initial state (init_states index 1-49)\n  - spatial:  perturb object layout via BDDL region_info modifications\n\nOutput: pickle files with (observations, actions, metadata) per episode.\n\nUsage:\n    # Physical perturbation dry-run\n    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \\\n        --perturbation_type physical --dry_run\n\n    # Spatial perturbation dry-run\n    CUDA_VISIBLE_DEVICES=2 python collect_expert_demos.py \\\n        --perturbation_type spatial --dry_run\n\n    # Full physical collection\n    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \\\n        --perturbation_type physical\n\"\"\"",
  "new_string": "\"\"\"\nCollect expert demonstrations by rolling out frozen π₀ in perturbed LIBERO environments.\n\nOnly successful episodes are saved. Two perturbation types are supported:\n  - physical: vary robot initial state (init_states index 1-49)\n  - spatial:  LIBERO-Plus _add_N distractor objects (default) or perturb_region fallback\n\nOutput: pickle files with (observations, actions, metadata) per episode.\n\nUsage:\n    # Physical perturbation dry-run\n    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \\\n        --perturbation_type physical --dry_run\n\n    # Spatial perturbation dry-run (uses _add_N by default)\n    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \\\n        --perturbation_type spatial --dry_run\n\n    # Spatial with legacy perturb_region mode\n    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \\\n        --perturbation_type spatial --spatial_mode perturb_region --dry_run\n\n    # Full physical collection\n    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \\\n        --perturbation_type physical\n\"\"\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "ab629fb4-2b21-4648-a940-b9528ca9bb2a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cbgjw9AidLhe2FM8hVJfEh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14130,
      "cache_read_input_tokens": 28930,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14130
      },
      "output_tokens": 9,
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

_source line 104 · 2026-05-15T17:51:44.823Z_

<details><summary>↩ Tool result · `toolu_01JRAUD81JxAdeZs7RP8Cnmb`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "5a8d3dff-3c19-41c5-b6b1-e6bdb8fb0eb2",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py",
    "oldString": "\"\"\"\nCollect expert demonstrations by rolling out frozen π₀ in perturbed LIBERO environments.\n\nOnly successful episodes are saved. Two perturbation types are supported:\n  - physical: vary robot initial state (init_states index 1-49)\n  - spatial:  perturb object layout via BDDL region_info modifications\n\nOutput: pickle files with (observations, actions, metadata) per episode.\n\nUsage:\n    # Physical perturbation dry-run\n    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \\\n        --perturbation_type physical --dry_run\n\n    # Spatial perturbation dry-run\n    CUDA_VISIBLE_DEVICES=2 python collect_expert_demos.py \\\n        --perturbation_type spatial --dry_run\n\n    # Full physical collection\n    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \\\n        --perturbation_type physical\n\"\"\"",
    "newString": "\"\"\"\nCollect expert demonstrations by rolling out frozen π₀ in perturbed LIBERO environments.\n\nOnly successful episodes are saved. Two perturbation types are supported:\n  - physical: vary robot initial state (init_states index 1-49)\n  - spatial:  LIBERO-Plus _add_N distractor objects (default) or perturb_region fallback\n\nOutput: pickle files with (observations, actions, metadata) per episode.\n\nUsage:\n    # Physical perturbation dry-run\n    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \\\n        --perturbation_type physical --dry_run\n\n    # Spatial perturbation dry-run (uses _add_N by default)\n    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \\\n        --perturbation_type spatial --dry_run\n\n    # Spatial with legacy perturb_region mode\n    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \\\n        --perturbation_type spatial --spatial_mode perturb_region --dry_run\n\n    # Full physical collection\n    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \\\n        --perturbation_type physical\n\"\"\"",
    "originalFile": "\"\"\"\nCollect expert demonstrations by rolling out frozen π₀ in perturbed LIBERO environments.\n\nOnly successful episodes are saved. Two perturbation types are supported:\n  - physical: vary robot initial state (init_states index 1-49)\n  - spatial:  perturb object layout via BDDL region_info modifications\n\nOutput: pickle files with (observations, actions, metadata) per episode.\n\nUsage:\n    # Physical perturbation dry-run\n    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \\\n        --perturbation_type physical --dry_run\n\n    # Spatial perturbation dry-run\n    CUDA_VISIBLE_DEVICES=2 python collect_expert_demos.py \\\n        --perturbation_type spatial --dry_run\n\n    # Full physical collection\n    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \\\n        --perturbation_type physical\n\"\"\"\n\nimport argparse\nimport collections\nimport copy\nimport logging\nimport math\nimport os\nimport pickle\nimport random\nimport re\nimport sys\nimport time\nimport types\nfrom pathlib import Path\nfrom typing import Any\n\nimport numpy as np\nimport torch\n\nlog = logging.getLogger(__name__)\n\n# ---------------------------------------------------------------------------\n# Constants\n# ---------------------------------------------------------------------------\n\nLIBERO_DUMMY_ACTION = [0.0] * 6 + [-1.0]\nLIBERO_ENV_RESOLUTION = 256\nMODEL_INPUT_RESOLUTION = 224\nREPLAN_STEPS = 5\nNUM_STEPS_WAIT = 10\nMAX_STEPS = 220  # libero_spatial default\n\n# 10 base tasks in libero_spatial (no perturbation suffix)\nBASE_TASK_SUITE = \"libero_spatial\"\n\n# Spatial perturbation grid: 10 configurations with varying XY shifts and yaw\n# Magnitudes chosen to be noticeable but within feasible reach of the robot.\nSPATIAL_PERTURBATION_CONFIGS = [\n    {\"delta_xy\": ( 0.05,  0.00), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.0)},\n    {\"delta_xy\": (-0.05,  0.00), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.0)},\n    {\"delta_xy\": ( 0.00,  0.05), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.0)},\n    {\"delta_xy\": ( 0.00, -0.05), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.0)},\n    {\"delta_xy\": ( 0.03,  0.03), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.0)},\n    {\"delta_xy\": (-0.03, -0.03), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.0)},\n    {\"delta_xy\": ( 0.04,  0.00), \"delta_half_len\": 0.01, \"delta_yaw\": (0.3, 0.0)},\n    {\"delta_xy\": (-0.04,  0.00), \"delta_half_len\": 0.01, \"delta_yaw\": (-0.3, 0.0)},\n    {\"delta_xy\": ( 0.00,  0.04), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.3)},\n    {\"delta_xy\": ( 0.00, -0.04), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, -0.3)},\n]\n\n\n# ---------------------------------------------------------------------------\n# Geometry / image helpers (from libero_integration.py)\n# ---------------------------------------------------------------------------\n\ndef _quat2axisangle(quat: np.ndarray) -> np.ndarray:\n    \"\"\"Quaternion [x,y,z,w] -> axis-angle [ax,ay,az].\"\"\"\n    q = np.asarray(quat, dtype=np.float64)\n    norm = np.linalg.norm(q)\n    if norm < 1e-8:\n        return np.zeros(3, dtype=np.float32)\n    q /= norm\n    sin_half = np.linalg.norm(q[:3])\n    if sin_half < 1e-8:\n        return np.zeros(3, dtype=np.float32)\n    angle = 2.0 * math.atan2(sin_half, q[3])\n    axis = q[:3] / sin_half\n    return (axis * angle).astype(np.float32)\n\n\ndef _resize_with_pad(img: np.ndarray, size: int) -> np.ndarray:\n    \"\"\"Resize image with aspect-preserving padding to (size, size, 3) uint8.\"\"\"\n    try:\n        from openpi_client.image_tools import resize_with_pad, convert_to_uint8\n        return convert_to_uint8(resize_with_pad(img, size, size))\n    except ImportError:\n        from PIL import Image as PILImage\n        h, w = img.shape[:2]\n        scale = min(size / h, size / w)\n        new_h, new_w = int(h * scale), int(w * scale)\n        resized = np.array(\n            PILImage.fromarray(img).resize((new_w, new_h), PILImage.BILINEAR)\n        )\n        canvas = np.zeros((size, size, 3), dtype=np.uint8)\n        y0, x0 = (size - new_h) // 2, (size - new_w) // 2\n        canvas[y0 : y0 + new_h, x0 : x0 + new_w] = resized\n        return canvas\n\n\ndef obs_to_model_input(obs: dict, task_description: str) -> dict:\n    \"\"\"Convert LIBERO observation to the dict format expected by policy.infer().\"\"\"\n    base_img = np.ascontiguousarray(obs[\"agentview_image\"][::-1, ::-1])\n    wrist_img = np.ascontiguousarray(obs[\"robot0_eye_in_hand_image\"][::-1, ::-1])\n\n    base_img = _resize_with_pad(base_img, MODEL_INPUT_RESOLUTION)\n    wrist_img = _resize_with_pad(wrist_img, MODEL_INPUT_RESOLUTION)\n\n    state = np.concatenate([\n        obs[\"robot0_eef_pos\"].astype(np.float32),\n        _quat2axisangle(obs[\"robot0_eef_quat\"]),\n        obs[\"robot0_gripper_qpos\"].astype(np.float32),\n    ])\n\n    return {\n        \"observation/image\": base_img,\n        \"observation/wrist_image\": wrist_img,\n        \"observation/state\": state,\n        \"prompt\": task_description,\n    }\n\n\ndef extract_obs_for_saving(obs: dict) -> dict:\n    \"\"\"Extract observation fields to save in demo data (images stored as uint8).\"\"\"\n    return {\n        \"agentview_image\": obs[\"agentview_image\"].copy(),\n        \"robot0_eye_in_hand_image\": obs[\"robot0_eye_in_hand_image\"].copy(),\n        \"robot0_eef_pos\": obs[\"robot0_eef_pos\"].astype(np.float32).copy(),\n        \"robot0_eef_quat\": obs[\"robot0_eef_quat\"].astype(np.float32).copy(),\n        \"robot0_gripper_qpos\": obs[\"robot0_gripper_qpos\"].astype(np.float32).copy(),\n    }\n\n\n# ---------------------------------------------------------------------------\n# Model loading\n# ---------------------------------------------------------------------------\n\ndef _ensure_openpi_imports():\n    \"\"\"Stub out lerobot (training-only dep) before importing OpenPI.\"\"\"\n    for mod in [\n        \"lerobot\", \"lerobot.common\", \"lerobot.common.datasets\",\n        \"lerobot.common.datasets.lerobot_dataset\",\n    ]:\n        if mod not in sys.modules:\n            sys.modules[mod] = types.ModuleType(mod)\n\n\ndef load_pi0_policy(checkpoint_path: str, device: str) -> object:\n    \"\"\"Load pi0 policy via OpenPI. Returns the Policy object for inference.\"\"\"\n    _ensure_openpi_imports()\n    from openpi.training import config as _config\n    from openpi.policies import policy_config\n\n    train_config = _config.get_config(\"pi0_libero\")\n    policy = policy_config.create_trained_policy(\n        train_config, checkpoint_path, pytorch_device=device\n    )\n    log.info(\"Loaded pi0 policy on %s\", device)\n    return policy\n\n\n# ---------------------------------------------------------------------------\n# Task discovery\n# ---------------------------------------------------------------------------\n\ndef find_base_tasks(bddl_dir: str, num_tasks: int = 10) -> list[dict]:\n    \"\"\"Find base (unperturbed) BDDL files in libero_spatial.\n\n    Returns list of dicts with keys: name, bddl_path, init_states_path.\n    \"\"\"\n    all_files = [f for f in os.listdir(bddl_dir) if f.endswith(\".bddl\")]\n\n    base_names = []\n    for f in sorted(all_files):\n        name = f.replace(\".bddl\", \"\")\n        # Skip any file with perturbation suffixes\n        if re.search(\n            r\"(_add_\\d+|_table_\\d+|_tb_\\d+|_light_\\d+|_language_\\d+\"\n            r\"|_view_|_noise_|_level\\d+| copy)\",\n            name,\n        ):\n            continue\n        base_names.append(name)\n\n    init_dir = bddl_dir.replace(\"bddl_files\", \"init_files\")\n    tasks = []\n    for name in base_names[:num_tasks]:\n        bddl_path = os.path.join(bddl_dir, f\"{name}.bddl\")\n        init_path = os.path.join(init_dir, f\"{name}.pruned_init\")\n        if not os.path.exists(init_path):\n            log.warning(\"init_states not found for %s, skipping\", name)\n            continue\n        tasks.append({\n            \"name\": name,\n            \"bddl_path\": bddl_path,\n            \"init_states_path\": init_path,\n        })\n\n    log.info(\"Found %d base tasks\", len(tasks))\n    return tasks\n\n\ndef get_task_language(bddl_path: str) -> str:\n    \"\"\"Extract language instruction from a BDDL file.\"\"\"\n    from libero.libero.envs.bddl_utils import get_problem_info\n    info = get_problem_info(bddl_path)\n    return info[\"language_instruction\"]\n\n\n# ---------------------------------------------------------------------------\n# Environment creation\n# ---------------------------------------------------------------------------\n\ndef create_env(bddl_path: str) -> object:\n    \"\"\"Create a LIBERO OffScreenRenderEnv from a BDDL file.\"\"\"\n    from libero.libero.envs import OffScreenRenderEnv\n    env = OffScreenRenderEnv(\n        bddl_file_name=bddl_path,\n        camera_heights=LIBERO_ENV_RESOLUTION,\n        camera_widths=LIBERO_ENV_RESOLUTION,\n    )\n    return env\n\n\ndef create_spatial_bddl(\n    base_bddl_path: str,\n    perturbation_config: dict,\n    output_dir: str,\n) -> str:\n    \"\"\"Create a perturbed BDDL file by applying spatial perturbation to all regions.\n\n    Returns the path to the new BDDL file.\n    \"\"\"\n    sys.path.insert(0, \"/root/LIBERO-plus/libero\")\n    from libero.randomizer.bddl_operators import (\n        load_bddl_file,\n        save_bddl_file,\n        perturb_region_info,\n    )\n\n    spec = load_bddl_file(base_bddl_path)\n    delta_xy = perturbation_config[\"delta_xy\"]\n    delta_half = perturbation_config[\"delta_half_len\"]\n    delta_yaw = perturbation_config[\"delta_yaw\"]\n\n    for i in range(len(spec.region_infos)):\n        spec.region_infos[i] = perturb_region_info(\n            spec.region_infos[i],\n            delta_region_centroid_xy=delta_xy,\n            delta_region_half_len=delta_half,\n            delta_yaw_rotation=delta_yaw,\n        )\n\n    os.makedirs(output_dir, exist_ok=True)\n    base_name = Path(base_bddl_path).stem\n    dx, dy = delta_xy\n    filename = f\"{base_name}_spatial_dx{dx:.2f}_dy{dy:.2f}.bddl\"\n    _, filepath = save_bddl_file(spec, bddl_filename=filename, bddl_dirpath=output_dir)\n    return filepath\n\n\n# ---------------------------------------------------------------------------\n# Episode rollout\n# ---------------------------------------------------------------------------\n\ndef rollout_episode(\n    policy: object,\n    env: object,\n    task_description: str,\n    init_states: np.ndarray,\n    init_state_idx: int,\n    seed: int,\n) -> dict[str, Any]:\n    \"\"\"Run one episode, collecting (obs, action) pairs.\n\n    Returns dict with observations, actions, success, num_steps.\n    \"\"\"\n    env.seed(seed)\n    obs = env.set_init_state(init_states[init_state_idx])\n\n    for _ in range(NUM_STEPS_WAIT):\n        obs, _, _, _ = env.step(LIBERO_DUMMY_ACTION)\n\n    all_obs = [extract_obs_for_saving(obs)]\n    all_actions = []\n    action_plan = collections.deque()\n    step = 0\n    success = False\n    done = False\n\n    while not done and step < MAX_STEPS:\n        if len(action_plan) == 0:\n            obs_dict = obs_to_model_input(obs, task_description)\n            result = policy.infer(obs_dict)\n            action_chunk = result[\"actions\"]\n            action_plan.extend(action_chunk[:REPLAN_STEPS])\n\n        action = action_plan.popleft()\n        if isinstance(action, torch.Tensor):\n            action = action.cpu().numpy()\n        action_np = np.asarray(action, dtype=np.float32)\n\n        obs, reward, done, info = env.step(\n            action_np.tolist() if hasattr(action_np, \"tolist\") else list(action_np)\n        )\n        step += 1\n\n        all_obs.append(extract_obs_for_saving(obs))\n        all_actions.append(action_np)\n\n        if done or reward > 0:\n            success = info.get(\"success\", reward > 0)\n\n    return {\n        \"observations\": all_obs,\n        \"actions\": np.stack(all_actions) if all_actions else np.zeros((0, 7)),\n        \"success\": success,\n        \"num_steps\": step,\n    }\n\n\n# ---------------------------------------------------------------------------\n# Collection loops\n# ---------------------------------------------------------------------------\n\ndef collect_physical(\n    policy: object,\n    tasks: list[dict],\n    episodes_per_config: int,\n    output_dir: str,\n    dry_run: bool,\n) -> dict:\n    \"\"\"Collect expert demos with physical (robot initial state) perturbation.\n\n    Uses init_states indices 1-49 (index 0 is nominal).\n    \"\"\"\n    os.makedirs(output_dir, exist_ok=True)\n    stats = {\"total\": 0, \"success\": 0, \"saved_files\": []}\n\n    init_state_indices = list(range(1, 50))  # 49 perturbed states\n    if dry_run:\n        tasks = tasks[:1]\n        init_state_indices = [1]\n        episodes_per_config = 1\n\n    for task_info in tasks:\n        task_name = task_info[\"name\"]\n        init_states = torch.load(task_info[\"init_states_path\"], weights_only=False)\n        language = get_task_language(task_info[\"bddl_path\"])\n        log.info(\"Task: %s (%d init_states available)\", task_name, len(init_states))\n\n        for idx in init_state_indices:\n            if idx >= len(init_states):\n                continue\n\n            for ep in range(episodes_per_config):\n                seed = hash((task_name, idx, ep)) % (2**31)\n                stats[\"total\"] += 1\n\n                try:\n                    env = create_env(task_info[\"bddl_path\"])\n                    result = rollout_episode(\n                        policy, env, language, init_states, idx, seed\n                    )\n                    env.close()\n                except Exception:\n                    log.exception(\n                        \"Episode failed: task=%s idx=%d ep=%d\", task_name, idx, ep\n                    )\n                    continue\n\n                if result[\"success\"]:\n                    stats[\"success\"] += 1\n                    demo = {\n                        \"observations\": result[\"observations\"],\n                        \"actions\": result[\"actions\"],\n                        \"task_name\": task_name,\n                        \"perturbation_config\": {\n                            \"type\": \"physical\",\n                            \"init_state_idx\": idx,\n                        },\n                        \"success\": True,\n                        \"num_steps\": result[\"num_steps\"],\n                    }\n                    fname = f\"{task_name}_initstate{idx}_ep{ep}.pkl\"\n                    fpath = os.path.join(output_dir, fname)\n                    with open(fpath, \"wb\") as f:\n                        pickle.dump(demo, f, protocol=pickle.HIGHEST_PROTOCOL)\n                    stats[\"saved_files\"].append(fpath)\n\n                rate = stats[\"success\"] / stats[\"total\"] * 100\n                log.info(\n                    \"[physical] task=%s idx=%d ep=%d | %s | \"\n                    \"cumulative %d/%d (%.1f%%)\",\n                    task_name, idx, ep,\n                    \"SUCCESS\" if result[\"success\"] else \"FAIL\",\n                    stats[\"success\"], stats[\"total\"], rate,\n                )\n\n    return stats\n\n\ndef collect_spatial(\n    policy: object,\n    tasks: list[dict],\n    episodes_per_config: int,\n    output_dir: str,\n    dry_run: bool,\n) -> dict:\n    \"\"\"Collect expert demos with spatial (objects layout) perturbation.\n\n    Applies 10 predefined spatial perturbation configs to each base task.\n    \"\"\"\n    os.makedirs(output_dir, exist_ok=True)\n    tmp_bddl_dir = os.path.join(output_dir, \"_tmp_bddl\")\n    os.makedirs(tmp_bddl_dir, exist_ok=True)\n    stats = {\"total\": 0, \"success\": 0, \"saved_files\": []}\n\n    configs = SPATIAL_PERTURBATION_CONFIGS\n    if dry_run:\n        tasks = tasks[:1]\n        configs = configs[:1]\n        episodes_per_config = 1\n\n    for task_info in tasks:\n        task_name = task_info[\"name\"]\n        init_states = torch.load(task_info[\"init_states_path\"], weights_only=False)\n        log.info(\"Task: %s\", task_name)\n\n        for cfg_idx, cfg in enumerate(configs):\n            try:\n                perturbed_bddl = create_spatial_bddl(\n                    task_info[\"bddl_path\"], cfg, tmp_bddl_dir\n                )\n                language = get_task_language(perturbed_bddl)\n            except Exception:\n                log.exception(\n                    \"BDDL perturbation failed: task=%s cfg=%d\", task_name, cfg_idx\n                )\n                continue\n\n            for ep in range(episodes_per_config):\n                seed = hash((task_name, cfg_idx, ep)) % (2**31)\n                stats[\"total\"] += 1\n\n                try:\n                    env = create_env(perturbed_bddl)\n                    # Use nominal init_state (index 0) for spatial perturbation\n                    result = rollout_episode(\n                        policy, env, language, init_states, 0, seed\n                    )\n                    env.close()\n                except Exception:\n                    log.exception(\n                        \"Episode failed: task=%s cfg=%d ep=%d\",\n                        task_name, cfg_idx, ep,\n                    )\n                    continue\n\n                if result[\"success\"]:\n                    stats[\"success\"] += 1\n                    demo = {\n                        \"observations\": result[\"observations\"],\n                        \"actions\": result[\"actions\"],\n                        \"task_name\": task_name,\n                        \"perturbation_config\": {\n                            \"type\": \"spatial\",\n                            \"config_idx\": cfg_idx,\n                            \"delta_xy\": cfg[\"delta_xy\"],\n                            \"delta_half_len\": cfg[\"delta_half_len\"],\n                            \"delta_yaw\": cfg[\"delta_yaw\"],\n                        },\n                        \"success\": True,\n                        \"num_steps\": result[\"num_steps\"],\n                    }\n                    fname = f\"{task_name}_spatial{cfg_idx}_ep{ep}.pkl\"\n                    fpath = os.path.join(output_dir, fname)\n                    with open(fpath, \"wb\") as f:\n                        pickle.dump(demo, f, protocol=pickle.HIGHEST_PROTOCOL)\n                    stats[\"saved_files\"].append(fpath)\n\n                rate = stats[\"success\"] / stats[\"total\"] * 100\n                log.info(\n                    \"[spatial] task=%s cfg=%d ep=%d | %s | \"\n                    \"cumulative %d/%d (%.1f%%)\",\n                    task_name, cfg_idx, ep,\n                    \"SUCCESS\" if result[\"success\"] else \"FAIL\",\n                    stats[\"success\"], stats[\"total\"], rate,\n                )\n\n    return stats\n\n\n# ---------------------------------------------------------------------------\n# Main\n# ---------------------------------------------------------------------------\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Collect expert demos from π₀ in perturbed LIBERO environments\"\n    )\n    parser.add_argument(\n        \"--perturbation_type\", type=str, required=True,\n        choices=[\"physical\", \"spatial\"],\n    )\n    parser.add_argument(\"--gpu_id\", type=int, default=0)\n    parser.add_argument(\"--num_tasks\", type=int, default=10)\n    parser.add_argument(\"--episodes_per_config\", type=int, default=3)\n    parser.add_argument(\n        \"--output_dir\", type=str, default=None,\n        help=\"Override output directory (default: auto from perturbation_type)\",\n    )\n    parser.add_argument(\n        \"--checkpoint\", type=str,\n        default=\"/root/autodl-tmp/checkpoints/pi0_base\",\n    )\n    parser.add_argument(\"--dry_run\", action=\"store_true\")\n    parser.add_argument(\"--seed\", type=int, default=42)\n    args = parser.parse_args()\n\n    logging.basicConfig(\n        level=logging.INFO,\n        format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    )\n\n    random.seed(args.seed)\n    np.random.seed(args.seed)\n    torch.manual_seed(args.seed)\n\n    if args.output_dir is None:\n        args.output_dir = (\n            f\"/root/meta_brain_lora_routing/data/expert_demos/{args.perturbation_type}\"\n        )\n\n    device = f\"cuda:{args.gpu_id}\"\n    log.info(\n        \"Config: type=%s device=%s num_tasks=%d eps_per_cfg=%d dry_run=%s\",\n        args.perturbation_type, device, args.num_tasks,\n        args.episodes_per_config, args.dry_run,\n    )\n\n    log.info(\"Loading π₀ from %s\", args.checkpoint)\n    policy = load_pi0_policy(args.checkpoint, device)\n\n    from libero.libero import get_libero_path\n    bddl_dir = os.path.join(get_libero_path(\"bddl_files\"), BASE_TASK_SUITE)\n    tasks = find_base_tasks(bddl_dir, num_tasks=args.num_tasks)\n\n    if not tasks:\n        log.error(\"No base tasks found in %s\", bddl_dir)\n        sys.exit(1)\n\n    t0 = time.time()\n\n    if args.perturbation_type == \"physical\":\n        stats = collect_physical(\n            policy, tasks, args.episodes_per_config,\n            args.output_dir, args.dry_run,\n        )\n    else:\n        stats = collect_spatial(\n            policy, tasks, args.episodes_per_config,\n            args.output_dir, args.dry_run,\n        )\n\n    elapsed = time.time() - t0\n\n    total_size = sum(\n        os.path.getsize(f) for f in stats[\"saved_files\"] if os.path.exists(f)\n    )\n    log.info(\"=\" * 60)\n    log.info(\"Collection complete: %s\", args.perturbation_type)\n    log.info(\"  Total episodes:  %d\", stats[\"total\"])\n    log.info(\"  Successful:      %d\", stats[\"success\"])\n    log.info(\n        \"  Success rate:    %.1f%%\",\n        stats[\"success\"] / max(stats[\"total\"], 1) * 100,\n    )\n    log.info(\"  Files saved:     %d\", len(stats[\"saved_files\"]))\n    log.info(\"  Total size:      %.1f MB\", total_size / 1024 / 1024)\n    log.info(\"  Elapsed:         %.1f min\", elapsed / 60)\n    log.info(\"  Output dir:      %s\", args.output_dir)\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 3,
        "oldLines": 7,
        "newStart": 3,
        "newLines": 7,
        "lines": [
          " ",
          " Only successful episodes are saved. Two perturbation types are supported:",
          "   - physical: vary robot initial state (init_states index 1-49)",
          "-  - spatial:  perturb object layout via BDDL region_info modifications",
          "+  - spatial:  LIBERO-Plus _add_N distractor objects (default) or perturb_region fallback",
          " ",
          " Output: pickle files with (observations, actions, metadata) per episode.",
          " "
        ]
      },
      {
        "oldStart": 12,
        "oldLines": 10,
        "newStart": 12,
        "newLines": 14,
        "lines": [
          "     CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \\",
          "         --perturbation_type physical --dry_run",
          " ",
          "-    # Spatial perturbation dry-run",
          "-    CUDA_VISIBLE_DEVICES=2 python collect_expert_demos.py \\",
          "+    # Spatial perturbation dry-run (uses _add_N by default)",
          "+    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \\",
          "         --perturbation_type spatial --dry_run",
          " ",
          "+    # Spatial with legacy perturb_region mode",
          "+    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \\",
          "+        --perturbation_type spatial --spatial_mode perturb_region --dry_run",
          "+",
          "     # Full physical collection",
          "     CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \\",
          "         --perturbation_type physical"
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

_source line 105_

Now add the `_add_N` task discovery functions after the existing `find_base_tasks` and `get_task_language` functions:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "16b3e542-3d1b-4b6b-a123-114074e28f6c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TPoxd317FWMimrdCDdvScB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1395,
      "cache_read_input_tokens": 43060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1395
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

_source line 106_

<details open><summary>🔧 Tool call — Edit · `toolu_014xKVvCpSsbbaDPMF2BweTb`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py",
  "old_string": "def get_task_language(bddl_path: str) -> str:\n    \"\"\"Extract language instruction from a BDDL file.\"\"\"\n    from libero.libero.envs.bddl_utils import get_problem_info\n    info = get_problem_info(bddl_path)\n    return info[\"language_instruction\"]\n\n\n# ---------------------------------------------------------------------------\n# Environment creation\n# ---------------------------------------------------------------------------",
  "new_string": "def get_task_language(bddl_path: str) -> str:\n    \"\"\"Extract language instruction from a BDDL file.\"\"\"\n    from libero.libero.envs.bddl_utils import get_problem_info\n    info = get_problem_info(bddl_path)\n    return info[\"language_instruction\"]\n\n\ndef discover_add_n_tasks(task_suite: str = BASE_TASK_SUITE) -> list[dict]:\n    \"\"\"Discover all _add_N (distractor-object) tasks from the LIBERO-Plus benchmark.\n\n    Returns list of dicts with: idx, name, language, bddl_path, init_states.\n    \"\"\"\n    from libero.libero import benchmark, get_libero_path\n    benchmark_dict = benchmark.get_benchmark_dict()\n    suite = benchmark_dict[task_suite]()\n    bddl_root = Path(get_libero_path(\"bddl_files\"))\n\n    tasks = []\n    skipped = 0\n    for i in range(suite.n_tasks):\n        task = suite.get_task(i)\n        name = getattr(task, \"name\", \"\") or getattr(task, \"bddl_file\", \"\")\n        if not re.search(r\"_add_\\d+$\", name.replace(\".bddl\", \"\")):\n            continue\n\n        bddl_path = str(bddl_root / task.problem_folder / task.bddl_file)\n        if not os.path.exists(bddl_path):\n            log.warning(\"BDDL not found, skipping: %s\", bddl_path)\n            skipped += 1\n            continue\n\n        try:\n            init_states = suite.get_task_init_states(i)\n        except Exception:\n            log.warning(\"init_states failed for %s, skipping\", name)\n            skipped += 1\n            continue\n\n        tasks.append({\n            \"idx\": i,\n            \"name\": name.replace(\".bddl\", \"\"),\n            \"language\": task.language,\n            \"bddl_path\": bddl_path,\n            \"init_states\": init_states,\n        })\n\n    log.info(\n        \"Discovered %d _add_N tasks (%d skipped) from %s\",\n        len(tasks), skipped, task_suite,\n    )\n    return tasks\n\n\n# ---------------------------------------------------------------------------\n# Environment creation\n# ---------------------------------------------------------------------------"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "77eb8126-5929-4a36-9089-2bdd960e960c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TPoxd317FWMimrdCDdvScB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1395,
      "cache_read_input_tokens": 43060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1395
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

_source line 107 · 2026-05-15T17:51:56.337Z_

<details><summary>↩ Tool result · `toolu_014xKVvCpSsbbaDPMF2BweTb`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "3cb41453-7993-4b9a-8f3c-a9e1907bf482",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py",
    "oldString": "def get_task_language(bddl_path: str) -> str:\n    \"\"\"Extract language instruction from a BDDL file.\"\"\"\n    from libero.libero.envs.bddl_utils import get_problem_info\n    info = get_problem_info(bddl_path)\n    return info[\"language_instruction\"]\n\n\n# ---------------------------------------------------------------------------\n# Environment creation\n# ---------------------------------------------------------------------------",
    "newString": "def get_task_language(bddl_path: str) -> str:\n    \"\"\"Extract language instruction from a BDDL file.\"\"\"\n    from libero.libero.envs.bddl_utils import get_problem_info\n    info = get_problem_info(bddl_path)\n    return info[\"language_instruction\"]\n\n\ndef discover_add_n_tasks(task_suite: str = BASE_TASK_SUITE) -> list[dict]:\n    \"\"\"Discover all _add_N (distractor-object) tasks from the LIBERO-Plus benchmark.\n\n    Returns list of dicts with: idx, name, language, bddl_path, init_states.\n    \"\"\"\n    from libero.libero import benchmark, get_libero_path\n    benchmark_dict = benchmark.get_benchmark_dict()\n    suite = benchmark_dict[task_suite]()\n    bddl_root = Path(get_libero_path(\"bddl_files\"))\n\n    tasks = []\n    skipped = 0\n    for i in range(suite.n_tasks):\n        task = suite.get_task(i)\n        name = getattr(task, \"name\", \"\") or getattr(task, \"bddl_file\", \"\")\n        if not re.search(r\"_add_\\d+$\", name.replace(\".bddl\", \"\")):\n            continue\n\n        bddl_path = str(bddl_root / task.problem_folder / task.bddl_file)\n        if not os.path.exists(bddl_path):\n            log.warning(\"BDDL not found, skipping: %s\", bddl_path)\n            skipped += 1\n            continue\n\n        try:\n            init_states = suite.get_task_init_states(i)\n        except Exception:\n            log.warning(\"init_states failed for %s, skipping\", name)\n            skipped += 1\n            continue\n\n        tasks.append({\n            \"idx\": i,\n            \"name\": name.replace(\".bddl\", \"\"),\n            \"language\": task.language,\n            \"bddl_path\": bddl_path,\n            \"init_states\": init_states,\n        })\n\n    log.info(\n        \"Discovered %d _add_N tasks (%d skipped) from %s\",\n        len(tasks), skipped, task_suite,\n    )\n    return tasks\n\n\n# ---------------------------------------------------------------------------\n# Environment creation\n# ---------------------------------------------------------------------------",
    "originalFile": "\"\"\"\nCollect expert demonstrations by rolling out frozen π₀ in perturbed LIBERO environments.\n\nOnly successful episodes are saved. Two perturbation types are supported:\n  - physical: vary robot initial state (init_states index 1-49)\n  - spatial:  LIBERO-Plus _add_N distractor objects (default) or perturb_region fallback\n\nOutput: pickle files with (observations, actions, metadata) per episode.\n\nUsage:\n    # Physical perturbation dry-run\n    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \\\n        --perturbation_type physical --dry_run\n\n    # Spatial perturbation dry-run (uses _add_N by default)\n    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \\\n        --perturbation_type spatial --dry_run\n\n    # Spatial with legacy perturb_region mode\n    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \\\n        --perturbation_type spatial --spatial_mode perturb_region --dry_run\n\n    # Full physical collection\n    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \\\n        --perturbation_type physical\n\"\"\"\n\nimport argparse\nimport collections\nimport copy\nimport logging\nimport math\nimport os\nimport pickle\nimport random\nimport re\nimport sys\nimport time\nimport types\nfrom pathlib import Path\nfrom typing import Any\n\nimport numpy as np\nimport torch\n\nlog = logging.getLogger(__name__)\n\n# ---------------------------------------------------------------------------\n# Constants\n# ---------------------------------------------------------------------------\n\nLIBERO_DUMMY_ACTION = [0.0] * 6 + [-1.0]\nLIBERO_ENV_RESOLUTION = 256\nMODEL_INPUT_RESOLUTION = 224\nREPLAN_STEPS = 5\nNUM_STEPS_WAIT = 10\nMAX_STEPS = 220  # libero_spatial default\n\n# 10 base tasks in libero_spatial (no perturbation suffix)\nBASE_TASK_SUITE = \"libero_spatial\"\n\n# Spatial perturbation grid: 10 configurations with varying XY shifts and yaw\n# Magnitudes chosen to be noticeable but within feasible reach of the robot.\nSPATIAL_PERTURBATION_CONFIGS = [\n    {\"delta_xy\": ( 0.05,  0.00), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.0)},\n    {\"delta_xy\": (-0.05,  0.00), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.0)},\n    {\"delta_xy\": ( 0.00,  0.05), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.0)},\n    {\"delta_xy\": ( 0.00, -0.05), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.0)},\n    {\"delta_xy\": ( 0.03,  0.03), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.0)},\n    {\"delta_xy\": (-0.03, -0.03), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.0)},\n    {\"delta_xy\": ( 0.04,  0.00), \"delta_half_len\": 0.01, \"delta_yaw\": (0.3, 0.0)},\n    {\"delta_xy\": (-0.04,  0.00), \"delta_half_len\": 0.01, \"delta_yaw\": (-0.3, 0.0)},\n    {\"delta_xy\": ( 0.00,  0.04), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.3)},\n    {\"delta_xy\": ( 0.00, -0.04), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, -0.3)},\n]\n\n\n# ---------------------------------------------------------------------------\n# Geometry / image helpers (from libero_integration.py)\n# ---------------------------------------------------------------------------\n\ndef _quat2axisangle(quat: np.ndarray) -> np.ndarray:\n    \"\"\"Quaternion [x,y,z,w] -> axis-angle [ax,ay,az].\"\"\"\n    q = np.asarray(quat, dtype=np.float64)\n    norm = np.linalg.norm(q)\n    if norm < 1e-8:\n        return np.zeros(3, dtype=np.float32)\n    q /= norm\n    sin_half = np.linalg.norm(q[:3])\n    if sin_half < 1e-8:\n        return np.zeros(3, dtype=np.float32)\n    angle = 2.0 * math.atan2(sin_half, q[3])\n    axis = q[:3] / sin_half\n    return (axis * angle).astype(np.float32)\n\n\ndef _resize_with_pad(img: np.ndarray, size: int) -> np.ndarray:\n    \"\"\"Resize image with aspect-preserving padding to (size, size, 3) uint8.\"\"\"\n    try:\n        from openpi_client.image_tools import resize_with_pad, convert_to_uint8\n        return convert_to_uint8(resize_with_pad(img, size, size))\n    except ImportError:\n        from PIL import Image as PILImage\n        h, w = img.shape[:2]\n        scale = min(size / h, size / w)\n        new_h, new_w = int(h * scale), int(w * scale)\n        resized = np.array(\n            PILImage.fromarray(img).resize((new_w, new_h), PILImage.BILINEAR)\n        )\n        canvas = np.zeros((size, size, 3), dtype=np.uint8)\n        y0, x0 = (size - new_h) // 2, (size - new_w) // 2\n        canvas[y0 : y0 + new_h, x0 : x0 + new_w] = resized\n        return canvas\n\n\ndef obs_to_model_input(obs: dict, task_description: str) -> dict:\n    \"\"\"Convert LIBERO observation to the dict format expected by policy.infer().\"\"\"\n    base_img = np.ascontiguousarray(obs[\"agentview_image\"][::-1, ::-1])\n    wrist_img = np.ascontiguousarray(obs[\"robot0_eye_in_hand_image\"][::-1, ::-1])\n\n    base_img = _resize_with_pad(base_img, MODEL_INPUT_RESOLUTION)\n    wrist_img = _resize_with_pad(wrist_img, MODEL_INPUT_RESOLUTION)\n\n    state = np.concatenate([\n        obs[\"robot0_eef_pos\"].astype(np.float32),\n        _quat2axisangle(obs[\"robot0_eef_quat\"]),\n        obs[\"robot0_gripper_qpos\"].astype(np.float32),\n    ])\n\n    return {\n        \"observation/image\": base_img,\n        \"observation/wrist_image\": wrist_img,\n        \"observation/state\": state,\n        \"prompt\": task_description,\n    }\n\n\ndef extract_obs_for_saving(obs: dict) -> dict:\n    \"\"\"Extract observation fields to save in demo data (images stored as uint8).\"\"\"\n    return {\n        \"agentview_image\": obs[\"agentview_image\"].copy(),\n        \"robot0_eye_in_hand_image\": obs[\"robot0_eye_in_hand_image\"].copy(),\n        \"robot0_eef_pos\": obs[\"robot0_eef_pos\"].astype(np.float32).copy(),\n        \"robot0_eef_quat\": obs[\"robot0_eef_quat\"].astype(np.float32).copy(),\n        \"robot0_gripper_qpos\": obs[\"robot0_gripper_qpos\"].astype(np.float32).copy(),\n    }\n\n\n# ---------------------------------------------------------------------------\n# Model loading\n# ---------------------------------------------------------------------------\n\ndef _ensure_openpi_imports():\n    \"\"\"Stub out lerobot (training-only dep) before importing OpenPI.\"\"\"\n    for mod in [\n        \"lerobot\", \"lerobot.common\", \"lerobot.common.datasets\",\n        \"lerobot.common.datasets.lerobot_dataset\",\n    ]:\n        if mod not in sys.modules:\n            sys.modules[mod] = types.ModuleType(mod)\n\n\ndef load_pi0_policy(checkpoint_path: str, device: str) -> object:\n    \"\"\"Load pi0 policy via OpenPI. Returns the Policy object for inference.\"\"\"\n    _ensure_openpi_imports()\n    from openpi.training import config as _config\n    from openpi.policies import policy_config\n\n    train_config = _config.get_config(\"pi0_libero\")\n    policy = policy_config.create_trained_policy(\n        train_config, checkpoint_path, pytorch_device=device\n    )\n    log.info(\"Loaded pi0 policy on %s\", device)\n    return policy\n\n\n# ---------------------------------------------------------------------------\n# Task discovery\n# ---------------------------------------------------------------------------\n\ndef find_base_tasks(bddl_dir: str, num_tasks: int = 10) -> list[dict]:\n    \"\"\"Find base (unperturbed) BDDL files in libero_spatial.\n\n    Returns list of dicts with keys: name, bddl_path, init_states_path.\n    \"\"\"\n    all_files = [f for f in os.listdir(bddl_dir) if f.endswith(\".bddl\")]\n\n    base_names = []\n    for f in sorted(all_files):\n        name = f.replace(\".bddl\", \"\")\n        # Skip any file with perturbation suffixes\n        if re.search(\n            r\"(_add_\\d+|_table_\\d+|_tb_\\d+|_light_\\d+|_language_\\d+\"\n            r\"|_view_|_noise_|_level\\d+| copy)\",\n            name,\n        ):\n            continue\n        base_names.append(name)\n\n    init_dir = bddl_dir.replace(\"bddl_files\", \"init_files\")\n    tasks = []\n    for name in base_names[:num_tasks]:\n        bddl_path = os.path.join(bddl_dir, f\"{name}.bddl\")\n        init_path = os.path.join(init_dir, f\"{name}.pruned_init\")\n        if not os.path.exists(init_path):\n            log.warning(\"init_states not found for %s, skipping\", name)\n            continue\n        tasks.append({\n            \"name\": name,\n            \"bddl_path\": bddl_path,\n            \"init_states_path\": init_path,\n        })\n\n    log.info(\"Found %d base tasks\", len(tasks))\n    return tasks\n\n\ndef get_task_language(bddl_path: str) -> str:\n    \"\"\"Extract language instruction from a BDDL file.\"\"\"\n    from libero.libero.envs.bddl_utils import get_problem_info\n    info = get_problem_info(bddl_path)\n    return info[\"language_instruction\"]\n\n\n# ---------------------------------------------------------------------------\n# Environment creation\n# ---------------------------------------------------------------------------\n\ndef create_env(bddl_path: str) -> object:\n    \"\"\"Create a LIBERO OffScreenRenderEnv from a BDDL file.\"\"\"\n    from libero.libero.envs import OffScreenRenderEnv\n    env = OffScreenRenderEnv(\n        bddl_file_name=bddl_path,\n        camera_heights=LIBERO_ENV_RESOLUTION,\n        camera_widths=LIBERO_ENV_RESOLUTION,\n    )\n    return env\n\n\ndef create_spatial_bddl(\n    base_bddl_path: str,\n    perturbation_config: dict,\n    output_dir: str,\n) -> str:\n    \"\"\"Create a perturbed BDDL file by applying spatial perturbation to all regions.\n\n    Returns the path to the new BDDL file.\n    \"\"\"\n    sys.path.insert(0, \"/root/LIBERO-plus/libero\")\n    from libero.randomizer.bddl_operators import (\n        load_bddl_file,\n        save_bddl_file,\n        perturb_region_info,\n    )\n\n    spec = load_bddl_file(base_bddl_path)\n    delta_xy = perturbation_config[\"delta_xy\"]\n    delta_half = perturbation_config[\"delta_half_len\"]\n    delta_yaw = perturbation_config[\"delta_yaw\"]\n\n    for i in range(len(spec.region_infos)):\n        spec.region_infos[i] = perturb_region_info(\n            spec.region_infos[i],\n            delta_region_centroid_xy=delta_xy,\n            delta_region_half_len=delta_half,\n            delta_yaw_rotation=delta_yaw,\n        )\n\n    os.makedirs(output_dir, exist_ok=True)\n    base_name = Path(base_bddl_path).stem\n    dx, dy = delta_xy\n    filename = f\"{base_name}_spatial_dx{dx:.2f}_dy{dy:.2f}.bddl\"\n    _, filepath = save_bddl_file(spec, bddl_filename=filename, bddl_dirpath=output_dir)\n    return filepath\n\n\n# ---------------------------------------------------------------------------\n# Episode rollout\n# ---------------------------------------------------------------------------\n\ndef rollout_episode(\n    policy: object,\n    env: object,\n    task_description: str,\n    init_states: np.ndarray,\n    init_state_idx: int,\n    seed: int,\n) -> dict[str, Any]:\n    \"\"\"Run one episode, collecting (obs, action) pairs.\n\n    Returns dict with observations, actions, success, num_steps.\n    \"\"\"\n    env.seed(seed)\n    obs = env.set_init_state(init_states[init_state_idx])\n\n    for _ in range(NUM_STEPS_WAIT):\n        obs, _, _, _ = env.step(LIBERO_DUMMY_ACTION)\n\n    all_obs = [extract_obs_for_saving(obs)]\n    all_actions = []\n    action_plan = collections.deque()\n    step = 0\n    success = False\n    done = False\n\n    while not done and step < MAX_STEPS:\n        if len(action_plan) == 0:\n            obs_dict = obs_to_model_input(obs, task_description)\n            result = policy.infer(obs_dict)\n            action_chunk = result[\"actions\"]\n            action_plan.extend(action_chunk[:REPLAN_STEPS])\n\n        action = action_plan.popleft()\n        if isinstance(action, torch.Tensor):\n            action = action.cpu().numpy()\n        action_np = np.asarray(action, dtype=np.float32)\n\n        obs, reward, done, info = env.step(\n            action_np.tolist() if hasattr(action_np, \"tolist\") else list(action_np)\n        )\n        step += 1\n\n        all_obs.append(extract_obs_for_saving(obs))\n        all_actions.append(action_np)\n\n        if done or reward > 0:\n            success = info.get(\"success\", reward > 0)\n\n    return {\n        \"observations\": all_obs,\n        \"actions\": np.stack(all_actions) if all_actions else np.zeros((0, 7)),\n        \"success\": success,\n        \"num_steps\": step,\n    }\n\n\n# ---------------------------------------------------------------------------\n# Collection loops\n# ---------------------------------------------------------------------------\n\ndef collect_physical(\n    policy: object,\n    tasks: list[dict],\n    episodes_per_config: int,\n    output_dir: str,\n    dry_run: bool,\n) -> dict:\n    \"\"\"Collect expert demos with physical (robot initial state) perturbation.\n\n    Uses init_states indices 1-49 (index 0 is nominal).\n    \"\"\"\n    os.makedirs(output_dir, exist_ok=True)\n    stats = {\"total\": 0, \"success\": 0, \"saved_files\": []}\n\n    init_state_indices = list(range(1, 50))  # 49 perturbed states\n    if dry_run:\n        tasks = tasks[:1]\n        init_state_indices = [1]\n        episodes_per_config = 1\n\n    for task_info in tasks:\n        task_name = task_info[\"name\"]\n        init_states = torch.load(task_info[\"init_states_path\"], weights_only=False)\n        language = get_task_language(task_info[\"bddl_path\"])\n        log.info(\"Task: %s (%d init_states available)\", task_name, len(init_states))\n\n        for idx in init_state_indices:\n            if idx >= len(init_states):\n                continue\n\n            for ep in range(episodes_per_config):\n                seed = hash((task_name, idx, ep)) % (2**31)\n                stats[\"total\"] += 1\n\n                try:\n                    env = create_env(task_info[\"bddl_path\"])\n                    result = rollout_episode(\n                        policy, env, language, init_states, idx, seed\n                    )\n                    env.close()\n                except Exception:\n                    log.exception(\n                        \"Episode failed: task=%s idx=%d ep=%d\", task_name, idx, ep\n                    )\n                    continue\n\n                if result[\"success\"]:\n                    stats[\"success\"] += 1\n                    demo = {\n                        \"observations\": result[\"observations\"],\n                        \"actions\": result[\"actions\"],\n                        \"task_name\": task_name,\n                        \"perturbation_config\": {\n                            \"type\": \"physical\",\n                            \"init_state_idx\": idx,\n                        },\n                        \"success\": True,\n                        \"num_steps\": result[\"num_steps\"],\n                    }\n                    fname = f\"{task_name}_initstate{idx}_ep{ep}.pkl\"\n                    fpath = os.path.join(output_dir, fname)\n                    with open(fpath, \"wb\") as f:\n                        pickle.dump(demo, f, protocol=pickle.HIGHEST_PROTOCOL)\n                    stats[\"saved_files\"].append(fpath)\n\n                rate = stats[\"success\"] / stats[\"total\"] * 100\n                log.info(\n                    \"[physical] task=%s idx=%d ep=%d | %s | \"\n                    \"cumulative %d/%d (%.1f%%)\",\n                    task_name, idx, ep,\n                    \"SUCCESS\" if result[\"success\"] else \"FAIL\",\n                    stats[\"success\"], stats[\"total\"], rate,\n                )\n\n    return stats\n\n\ndef collect_spatial(\n    policy: object,\n    tasks: list[dict],\n    episodes_per_config: int,\n    output_dir: str,\n    dry_run: bool,\n) -> dict:\n    \"\"\"Collect expert demos with spatial (objects layout) perturbation.\n\n    Applies 10 predefined spatial perturbation configs to each base task.\n    \"\"\"\n    os.makedirs(output_dir, exist_ok=True)\n    tmp_bddl_dir = os.path.join(output_dir, \"_tmp_bddl\")\n    os.makedirs(tmp_bddl_dir, exist_ok=True)\n    stats = {\"total\": 0, \"success\": 0, \"saved_files\": []}\n\n    configs = SPATIAL_PERTURBATION_CONFIGS\n    if dry_run:\n        tasks = tasks[:1]\n        configs = configs[:1]\n        episodes_per_config = 1\n\n    for task_info in tasks:\n        task_name = task_info[\"name\"]\n        init_states = torch.load(task_info[\"init_states_path\"], weights_only=False)\n        log.info(\"Task: %s\", task_name)\n\n        for cfg_idx, cfg in enumerate(configs):\n            try:\n                perturbed_bddl = create_spatial_bddl(\n                    task_info[\"bddl_path\"], cfg, tmp_bddl_dir\n                )\n                language = get_task_language(perturbed_bddl)\n            except Exception:\n                log.exception(\n                    \"BDDL perturbation failed: task=%s cfg=%d\", task_name, cfg_idx\n                )\n                continue\n\n            for ep in range(episodes_per_config):\n                seed = hash((task_name, cfg_idx, ep)) % (2**31)\n                stats[\"total\"] += 1\n\n                try:\n                    env = create_env(perturbed_bddl)\n                    # Use nominal init_state (index 0) for spatial perturbation\n                    result = rollout_episode(\n                        policy, env, language, init_states, 0, seed\n                    )\n                    env.close()\n                except Exception:\n                    log.exception(\n                        \"Episode failed: task=%s cfg=%d ep=%d\",\n                        task_name, cfg_idx, ep,\n                    )\n                    continue\n\n                if result[\"success\"]:\n                    stats[\"success\"] += 1\n                    demo = {\n                        \"observations\": result[\"observations\"],\n                        \"actions\": result[\"actions\"],\n                        \"task_name\": task_name,\n                        \"perturbation_config\": {\n                            \"type\": \"spatial\",\n                            \"config_idx\": cfg_idx,\n                            \"delta_xy\": cfg[\"delta_xy\"],\n                            \"delta_half_len\": cfg[\"delta_half_len\"],\n                            \"delta_yaw\": cfg[\"delta_yaw\"],\n                        },\n                        \"success\": True,\n                        \"num_steps\": result[\"num_steps\"],\n                    }\n                    fname = f\"{task_name}_spatial{cfg_idx}_ep{ep}.pkl\"\n                    fpath = os.path.join(output_dir, fname)\n                    with open(fpath, \"wb\") as f:\n                        pickle.dump(demo, f, protocol=pickle.HIGHEST_PROTOCOL)\n                    stats[\"saved_files\"].append(fpath)\n\n                rate = stats[\"success\"] / stats[\"total\"] * 100\n                log.info(\n                    \"[spatial] task=%s cfg=%d ep=%d | %s | \"\n                    \"cumulative %d/%d (%.1f%%)\",\n                    task_name, cfg_idx, ep,\n                    \"SUCCESS\" if result[\"success\"] else \"FAIL\",\n                    stats[\"success\"], stats[\"total\"], rate,\n                )\n\n    return stats\n\n\n# ---------------------------------------------------------------------------\n# Main\n# ---------------------------------------------------------------------------\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Collect expert demos from π₀ in perturbed LIBERO environments\"\n    )\n    parser.add_argument(\n        \"--perturbation_type\", type=str, required=True,\n        choices=[\"physical\", \"spatial\"],\n    )\n    parser.add_argument(\"--gpu_id\", type=int, default=0)\n    parser.add_argument(\"--num_tasks\", type=int, default=10)\n    parser.add_argument(\"--episodes_per_config\", type=int, default=3)\n    parser.add_argument(\n        \"--output_dir\", type=str, default=None,\n        help=\"Override output directory (default: auto from perturbation_type)\",\n    )\n    parser.add_argument(\n        \"--checkpoint\", type=str,\n        default=\"/root/autodl-tmp/checkpoints/pi0_base\",\n    )\n    parser.add_argument(\"--dry_run\", action=\"store_true\")\n    parser.add_argument(\"--seed\", type=int, default=42)\n    args = parser.parse_args()\n\n    logging.basicConfig(\n        level=logging.INFO,\n        format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    )\n\n    random.seed(args.seed)\n    np.random.seed(args.seed)\n    torch.manual_seed(args.seed)\n\n    if args.output_dir is None:\n        args.output_dir = (\n            f\"/root/meta_brain_lora_routing/data/expert_demos/{args.perturbation_type}\"\n        )\n\n    device = f\"cuda:{args.gpu_id}\"\n    log.info(\n        \"Config: type=%s device=%s num_tasks=%d eps_per_cfg=%d dry_run=%s\",\n        args.perturbation_type, device, args.num_tasks,\n        args.episodes_per_config, args.dry_run,\n    )\n\n    log.info(\"Loading π₀ from %s\", args.checkpoint)\n    policy = load_pi0_policy(args.checkpoint, device)\n\n    from libero.libero import get_libero_path\n    bddl_dir = os.path.join(get_libero_path(\"bddl_files\"), BASE_TASK_SUITE)\n    tasks = find_base_tasks(bddl_dir, num_tasks=args.num_tasks)\n\n    if not tasks:\n        log.error(\"No base tasks found in %s\", bddl_dir)\n        sys.exit(1)\n\n    t0 = time.time()\n\n    if args.perturbation_type == \"physical\":\n        stats = collect_physical(\n            policy, tasks, args.episodes_per_config,\n            args.output_dir, args.dry_run,\n        )\n    else:\n        stats = collect_spatial(\n            policy, tasks, args.episodes_per_config,\n            args.output_dir, args.dry_run,\n        )\n\n    elapsed = time.time() - t0\n\n    total_size = sum(\n        os.path.getsize(f) for f in stats[\"saved_files\"] if os.path.exists(f)\n    )\n    log.info(\"=\" * 60)\n    log.info(\"Collection complete: %s\", args.perturbation_type)\n    log.info(\"  Total episodes:  %d\", stats[\"total\"])\n    log.info(\"  Successful:      %d\", stats[\"success\"])\n    log.info(\n        \"  Success rate:    %.1f%%\",\n        stats[\"success\"] / max(stats[\"total\"], 1) * 100,\n    )\n    log.info(\"  Files saved:     %d\", len(stats[\"saved_files\"]))\n    log.info(\"  Total size:      %.1f MB\", total_size / 1024 / 1024)\n    log.info(\"  Elapsed:         %.1f min\", elapsed / 60)\n    log.info(\"  Output dir:      %s\", args.output_dir)\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 222,
        "oldLines": 6,
        "newStart": 222,
        "newLines": 52,
        "lines": [
          "     return info[\"language_instruction\"]",
          " ",
          " ",
          "+def discover_add_n_tasks(task_suite: str = BASE_TASK_SUITE) -> list[dict]:",
          "+    \"\"\"Discover all _add_N (distractor-object) tasks from the LIBERO-Plus benchmark.",
          "+",
          "+    Returns list of dicts with: idx, name, language, bddl_path, init_states.",
          "+    \"\"\"",
          "+    from libero.libero import benchmark, get_libero_path",
          "+    benchmark_dict = benchmark.get_benchmark_dict()",
          "+    suite = benchmark_dict[task_suite]()",
          "+    bddl_root = Path(get_libero_path(\"bddl_files\"))",
          "+",
          "+    tasks = []",
          "+    skipped = 0",
          "+    for i in range(suite.n_tasks):",
          "+        task = suite.get_task(i)",
          "+        name = getattr(task, \"name\", \"\") or getattr(task, \"bddl_file\", \"\")",
          "+        if not re.search(r\"_add_\\d+$\", name.replace(\".bddl\", \"\")):",
          "+            continue",
          "+",
          "+        bddl_path = str(bddl_root / task.problem_folder / task.bddl_file)",
          "+        if not os.path.exists(bddl_path):",
          "+            log.warning(\"BDDL not found, skipping: %s\", bddl_path)",
          "+            skipped += 1",
          "+            continue",
          "+",
          "+        try:",
          "+            init_states = suite.get_task_init_states(i)",
          "+        except Exception:",
          "+            log.warning(\"init_states failed for %s, skipping\", name)",
          "+            skipped += 1",
          "+            continue",
          "+",
          "+        tasks.append({",
          "+            \"idx\": i,",
          "+            \"name\": name.replace(\".bddl\", \"\"),",
          "+            \"language\": task.language,",
          "+            \"bddl_path\": bddl_path,",
          "+            \"init_states\": init_states,",
          "+        })",
          "+",
          "+    log.info(",
          "+        \"Discovered %d _add_N tasks (%d skipped) from %s\",",
          "+        len(tasks), skipped, task_suite,",
          "+    )",
          "+    return tasks",
          "+",
          "+",
          " # ---------------------------------------------------------------------------",
          " # Environment creation",
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


### Assistant

_source line 108_

Now add the `collect_spatial_add_n()` function after the existing `collect_spatial()`:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "b44c2801-b551-4a1d-8323-6731077ca7cc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GL6iT2eTXHDiykP1ypnpQs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1029,
      "cache_read_input_tokens": 44455,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1029
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

_source line 109_

<details open><summary>🔧 Tool call — Edit · `toolu_0176tYAbv81KgEQ4RXjzyEDi`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py",
  "old_string": "    return stats\n\n\n# ---------------------------------------------------------------------------\n# Main\n# ---------------------------------------------------------------------------",
  "new_string": "    return stats\n\n\ndef collect_spatial_add_n(\n    policy: object,\n    episodes_per_task: int,\n    output_dir: str,\n    dry_run: bool,\n) -> dict:\n    \"\"\"Collect expert demos using LIBERO-Plus _add_N distractor-object tasks.\n\n    Each _add_N task is a pre-built BDDL with extra objects in the scene.\n    208 tasks × 3 episodes = 624 rollouts.\n    \"\"\"\n    os.makedirs(output_dir, exist_ok=True)\n    stats = {\"total\": 0, \"success\": 0, \"saved_files\": [], \"load_errors\": 0}\n\n    add_tasks = discover_add_n_tasks()\n    if not add_tasks:\n        log.error(\"No _add_N tasks found. Check LIBERO-Plus installation.\")\n        return stats\n\n    if dry_run:\n        add_tasks = add_tasks[:2]\n        episodes_per_task = 1\n\n    log.info(\n        \"Collecting spatial (_add_N): %d tasks × %d eps = %d rollouts\",\n        len(add_tasks), episodes_per_task, len(add_tasks) * episodes_per_task,\n    )\n\n    for task_info in add_tasks:\n        task_name = task_info[\"name\"]\n        language = task_info[\"language\"]\n        init_states = task_info[\"init_states\"]\n\n        for ep in range(episodes_per_task):\n            seed = hash((task_name, ep)) % (2**31)\n            stats[\"total\"] += 1\n\n            try:\n                env = create_env(task_info[\"bddl_path\"])\n                init_idx = ep % len(init_states)\n                result = rollout_episode(\n                    policy, env, language, init_states, init_idx, seed\n                )\n                env.close()\n            except FileNotFoundError as e:\n                stats[\"load_errors\"] += 1\n                log.warning(\"Asset missing for %s: %s\", task_name, e)\n                continue\n            except Exception:\n                log.exception(\"Episode failed: task=%s ep=%d\", task_name, ep)\n                continue\n\n            if result[\"success\"]:\n                stats[\"success\"] += 1\n                demo = {\n                    \"observations\": result[\"observations\"],\n                    \"actions\": result[\"actions\"],\n                    \"task_name\": task_name,\n                    \"perturbation_config\": {\n                        \"type\": \"spatial_add_n\",\n                        \"source_task_idx\": task_info[\"idx\"],\n                    },\n                    \"success\": True,\n                    \"num_steps\": result[\"num_steps\"],\n                }\n                fname = f\"{task_name}_ep{ep}.pkl\"\n                fpath = os.path.join(output_dir, fname)\n                with open(fpath, \"wb\") as f:\n                    pickle.dump(demo, f, protocol=pickle.HIGHEST_PROTOCOL)\n                stats[\"saved_files\"].append(fpath)\n\n            rate = stats[\"success\"] / stats[\"total\"] * 100\n            log.info(\n                \"[spatial_add_n] task=%s ep=%d | %s | cumulative %d/%d (%.1f%%) | load_errors=%d\",\n                task_name, ep,\n                \"SUCCESS\" if result[\"success\"] else \"FAIL\",\n                stats[\"success\"], stats[\"total\"], rate,\n                stats[\"load_errors\"],\n            )\n\n    return stats\n\n\n# ---------------------------------------------------------------------------\n# Main\n# ---------------------------------------------------------------------------"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "dde69369-40d7-4f75-beca-be1ac2179e6e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GL6iT2eTXHDiykP1ypnpQs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1029,
      "cache_read_input_tokens": 44455,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1029
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

_source line 110 · 2026-05-15T17:52:12.681Z_

<details><summary>↩ Tool result · `toolu_0176tYAbv81KgEQ4RXjzyEDi`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "c0e9d9b3-c7ed-4494-a13f-c6d1faafe4a0",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py",
    "oldString": "    return stats\n\n\n# ---------------------------------------------------------------------------\n# Main\n# ---------------------------------------------------------------------------",
    "newString": "    return stats\n\n\ndef collect_spatial_add_n(\n    policy: object,\n    episodes_per_task: int,\n    output_dir: str,\n    dry_run: bool,\n) -> dict:\n    \"\"\"Collect expert demos using LIBERO-Plus _add_N distractor-object tasks.\n\n    Each _add_N task is a pre-built BDDL with extra objects in the scene.\n    208 tasks × 3 episodes = 624 rollouts.\n    \"\"\"\n    os.makedirs(output_dir, exist_ok=True)\n    stats = {\"total\": 0, \"success\": 0, \"saved_files\": [], \"load_errors\": 0}\n\n    add_tasks = discover_add_n_tasks()\n    if not add_tasks:\n        log.error(\"No _add_N tasks found. Check LIBERO-Plus installation.\")\n        return stats\n\n    if dry_run:\n        add_tasks = add_tasks[:2]\n        episodes_per_task = 1\n\n    log.info(\n        \"Collecting spatial (_add_N): %d tasks × %d eps = %d rollouts\",\n        len(add_tasks), episodes_per_task, len(add_tasks) * episodes_per_task,\n    )\n\n    for task_info in add_tasks:\n        task_name = task_info[\"name\"]\n        language = task_info[\"language\"]\n        init_states = task_info[\"init_states\"]\n\n        for ep in range(episodes_per_task):\n            seed = hash((task_name, ep)) % (2**31)\n            stats[\"total\"] += 1\n\n            try:\n                env = create_env(task_info[\"bddl_path\"])\n                init_idx = ep % len(init_states)\n                result = rollout_episode(\n                    policy, env, language, init_states, init_idx, seed\n                )\n                env.close()\n            except FileNotFoundError as e:\n                stats[\"load_errors\"] += 1\n                log.warning(\"Asset missing for %s: %s\", task_name, e)\n                continue\n            except Exception:\n                log.exception(\"Episode failed: task=%s ep=%d\", task_name, ep)\n                continue\n\n            if result[\"success\"]:\n                stats[\"success\"] += 1\n                demo = {\n                    \"observations\": result[\"observations\"],\n                    \"actions\": result[\"actions\"],\n                    \"task_name\": task_name,\n                    \"perturbation_config\": {\n                        \"type\": \"spatial_add_n\",\n                        \"source_task_idx\": task_info[\"idx\"],\n                    },\n                    \"success\": True,\n                    \"num_steps\": result[\"num_steps\"],\n                }\n                fname = f\"{task_name}_ep{ep}.pkl\"\n                fpath = os.path.join(output_dir, fname)\n                with open(fpath, \"wb\") as f:\n                    pickle.dump(demo, f, protocol=pickle.HIGHEST_PROTOCOL)\n                stats[\"saved_files\"].append(fpath)\n\n            rate = stats[\"success\"] / stats[\"total\"] * 100\n            log.info(\n                \"[spatial_add_n] task=%s ep=%d | %s | cumulative %d/%d (%.1f%%) | load_errors=%d\",\n                task_name, ep,\n                \"SUCCESS\" if result[\"success\"] else \"FAIL\",\n                stats[\"success\"], stats[\"total\"], rate,\n                stats[\"load_errors\"],\n            )\n\n    return stats\n\n\n# ---------------------------------------------------------------------------\n# Main\n# ---------------------------------------------------------------------------",
    "originalFile": "\"\"\"\nCollect expert demonstrations by rolling out frozen π₀ in perturbed LIBERO environments.\n\nOnly successful episodes are saved. Two perturbation types are supported:\n  - physical: vary robot initial state (init_states index 1-49)\n  - spatial:  LIBERO-Plus _add_N distractor objects (default) or perturb_region fallback\n\nOutput: pickle files with (observations, actions, metadata) per episode.\n\nUsage:\n    # Physical perturbation dry-run\n    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \\\n        --perturbation_type physical --dry_run\n\n    # Spatial perturbation dry-run (uses _add_N by default)\n    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \\\n        --perturbation_type spatial --dry_run\n\n    # Spatial with legacy perturb_region mode\n    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \\\n        --perturbation_type spatial --spatial_mode perturb_region --dry_run\n\n    # Full physical collection\n    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \\\n        --perturbation_type physical\n\"\"\"\n\nimport argparse\nimport collections\nimport copy\nimport logging\nimport math\nimport os\nimport pickle\nimport random\nimport re\nimport sys\nimport time\nimport types\nfrom pathlib import Path\nfrom typing import Any\n\nimport numpy as np\nimport torch\n\nlog = logging.getLogger(__name__)\n\n# ---------------------------------------------------------------------------\n# Constants\n# ---------------------------------------------------------------------------\n\nLIBERO_DUMMY_ACTION = [0.0] * 6 + [-1.0]\nLIBERO_ENV_RESOLUTION = 256\nMODEL_INPUT_RESOLUTION = 224\nREPLAN_STEPS = 5\nNUM_STEPS_WAIT = 10\nMAX_STEPS = 220  # libero_spatial default\n\n# 10 base tasks in libero_spatial (no perturbation suffix)\nBASE_TASK_SUITE = \"libero_spatial\"\n\n# Spatial perturbation grid: 10 configurations with varying XY shifts and yaw\n# Magnitudes chosen to be noticeable but within feasible reach of the robot.\nSPATIAL_PERTURBATION_CONFIGS = [\n    {\"delta_xy\": ( 0.05,  0.00), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.0)},\n    {\"delta_xy\": (-0.05,  0.00), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.0)},\n    {\"delta_xy\": ( 0.00,  0.05), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.0)},\n    {\"delta_xy\": ( 0.00, -0.05), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.0)},\n    {\"delta_xy\": ( 0.03,  0.03), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.0)},\n    {\"delta_xy\": (-0.03, -0.03), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.0)},\n    {\"delta_xy\": ( 0.04,  0.00), \"delta_half_len\": 0.01, \"delta_yaw\": (0.3, 0.0)},\n    {\"delta_xy\": (-0.04,  0.00), \"delta_half_len\": 0.01, \"delta_yaw\": (-0.3, 0.0)},\n    {\"delta_xy\": ( 0.00,  0.04), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.3)},\n    {\"delta_xy\": ( 0.00, -0.04), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, -0.3)},\n]\n\n\n# ---------------------------------------------------------------------------\n# Geometry / image helpers (from libero_integration.py)\n# ---------------------------------------------------------------------------\n\ndef _quat2axisangle(quat: np.ndarray) -> np.ndarray:\n    \"\"\"Quaternion [x,y,z,w] -> axis-angle [ax,ay,az].\"\"\"\n    q = np.asarray(quat, dtype=np.float64)\n    norm = np.linalg.norm(q)\n    if norm < 1e-8:\n        return np.zeros(3, dtype=np.float32)\n    q /= norm\n    sin_half = np.linalg.norm(q[:3])\n    if sin_half < 1e-8:\n        return np.zeros(3, dtype=np.float32)\n    angle = 2.0 * math.atan2(sin_half, q[3])\n    axis = q[:3] / sin_half\n    return (axis * angle).astype(np.float32)\n\n\ndef _resize_with_pad(img: np.ndarray, size: int) -> np.ndarray:\n    \"\"\"Resize image with aspect-preserving padding to (size, size, 3) uint8.\"\"\"\n    try:\n        from openpi_client.image_tools import resize_with_pad, convert_to_uint8\n        return convert_to_uint8(resize_with_pad(img, size, size))\n    except ImportError:\n        from PIL import Image as PILImage\n        h, w = img.shape[:2]\n        scale = min(size / h, size / w)\n        new_h, new_w = int(h * scale), int(w * scale)\n        resized = np.array(\n            PILImage.fromarray(img).resize((new_w, new_h), PILImage.BILINEAR)\n        )\n        canvas = np.zeros((size, size, 3), dtype=np.uint8)\n        y0, x0 = (size - new_h) // 2, (size - new_w) // 2\n        canvas[y0 : y0 + new_h, x0 : x0 + new_w] = resized\n        return canvas\n\n\ndef obs_to_model_input(obs: dict, task_description: str) -> dict:\n    \"\"\"Convert LIBERO observation to the dict format expected by policy.infer().\"\"\"\n    base_img = np.ascontiguousarray(obs[\"agentview_image\"][::-1, ::-1])\n    wrist_img = np.ascontiguousarray(obs[\"robot0_eye_in_hand_image\"][::-1, ::-1])\n\n    base_img = _resize_with_pad(base_img, MODEL_INPUT_RESOLUTION)\n    wrist_img = _resize_with_pad(wrist_img, MODEL_INPUT_RESOLUTION)\n\n    state = np.concatenate([\n        obs[\"robot0_eef_pos\"].astype(np.float32),\n        _quat2axisangle(obs[\"robot0_eef_quat\"]),\n        obs[\"robot0_gripper_qpos\"].astype(np.float32),\n    ])\n\n    return {\n        \"observation/image\": base_img,\n        \"observation/wrist_image\": wrist_img,\n        \"observation/state\": state,\n        \"prompt\": task_description,\n    }\n\n\ndef extract_obs_for_saving(obs: dict) -> dict:\n    \"\"\"Extract observation fields to save in demo data (images stored as uint8).\"\"\"\n    return {\n        \"agentview_image\": obs[\"agentview_image\"].copy(),\n        \"robot0_eye_in_hand_image\": obs[\"robot0_eye_in_hand_image\"].copy(),\n        \"robot0_eef_pos\": obs[\"robot0_eef_pos\"].astype(np.float32).copy(),\n        \"robot0_eef_quat\": obs[\"robot0_eef_quat\"].astype(np.float32).copy(),\n        \"robot0_gripper_qpos\": obs[\"robot0_gripper_qpos\"].astype(np.float32).copy(),\n    }\n\n\n# ---------------------------------------------------------------------------\n# Model loading\n# ---------------------------------------------------------------------------\n\ndef _ensure_openpi_imports():\n    \"\"\"Stub out lerobot (training-only dep) before importing OpenPI.\"\"\"\n    for mod in [\n        \"lerobot\", \"lerobot.common\", \"lerobot.common.datasets\",\n        \"lerobot.common.datasets.lerobot_dataset\",\n    ]:\n        if mod not in sys.modules:\n            sys.modules[mod] = types.ModuleType(mod)\n\n\ndef load_pi0_policy(checkpoint_path: str, device: str) -> object:\n    \"\"\"Load pi0 policy via OpenPI. Returns the Policy object for inference.\"\"\"\n    _ensure_openpi_imports()\n    from openpi.training import config as _config\n    from openpi.policies import policy_config\n\n    train_config = _config.get_config(\"pi0_libero\")\n    policy = policy_config.create_trained_policy(\n        train_config, checkpoint_path, pytorch_device=device\n    )\n    log.info(\"Loaded pi0 policy on %s\", device)\n    return policy\n\n\n# ---------------------------------------------------------------------------\n# Task discovery\n# ---------------------------------------------------------------------------\n\ndef find_base_tasks(bddl_dir: str, num_tasks: int = 10) -> list[dict]:\n    \"\"\"Find base (unperturbed) BDDL files in libero_spatial.\n\n    Returns list of dicts with keys: name, bddl_path, init_states_path.\n    \"\"\"\n    all_files = [f for f in os.listdir(bddl_dir) if f.endswith(\".bddl\")]\n\n    base_names = []\n    for f in sorted(all_files):\n        name = f.replace(\".bddl\", \"\")\n        # Skip any file with perturbation suffixes\n        if re.search(\n            r\"(_add_\\d+|_table_\\d+|_tb_\\d+|_light_\\d+|_language_\\d+\"\n            r\"|_view_|_noise_|_level\\d+| copy)\",\n            name,\n        ):\n            continue\n        base_names.append(name)\n\n    init_dir = bddl_dir.replace(\"bddl_files\", \"init_files\")\n    tasks = []\n    for name in base_names[:num_tasks]:\n        bddl_path = os.path.join(bddl_dir, f\"{name}.bddl\")\n        init_path = os.path.join(init_dir, f\"{name}.pruned_init\")\n        if not os.path.exists(init_path):\n            log.warning(\"init_states not found for %s, skipping\", name)\n            continue\n        tasks.append({\n            \"name\": name,\n            \"bddl_path\": bddl_path,\n            \"init_states_path\": init_path,\n        })\n\n    log.info(\"Found %d base tasks\", len(tasks))\n    return tasks\n\n\ndef get_task_language(bddl_path: str) -> str:\n    \"\"\"Extract language instruction from a BDDL file.\"\"\"\n    from libero.libero.envs.bddl_utils import get_problem_info\n    info = get_problem_info(bddl_path)\n    return info[\"language_instruction\"]\n\n\ndef discover_add_n_tasks(task_suite: str = BASE_TASK_SUITE) -> list[dict]:\n    \"\"\"Discover all _add_N (distractor-object) tasks from the LIBERO-Plus benchmark.\n\n    Returns list of dicts with: idx, name, language, bddl_path, init_states.\n    \"\"\"\n    from libero.libero import benchmark, get_libero_path\n    benchmark_dict = benchmark.get_benchmark_dict()\n    suite = benchmark_dict[task_suite]()\n    bddl_root = Path(get_libero_path(\"bddl_files\"))\n\n    tasks = []\n    skipped = 0\n    for i in range(suite.n_tasks):\n        task = suite.get_task(i)\n        name = getattr(task, \"name\", \"\") or getattr(task, \"bddl_file\", \"\")\n        if not re.search(r\"_add_\\d+$\", name.replace(\".bddl\", \"\")):\n            continue\n\n        bddl_path = str(bddl_root / task.problem_folder / task.bddl_file)\n        if not os.path.exists(bddl_path):\n            log.warning(\"BDDL not found, skipping: %s\", bddl_path)\n            skipped += 1\n            continue\n\n        try:\n            init_states = suite.get_task_init_states(i)\n        except Exception:\n            log.warning(\"init_states failed for %s, skipping\", name)\n            skipped += 1\n            continue\n\n        tasks.append({\n            \"idx\": i,\n            \"name\": name.replace(\".bddl\", \"\"),\n            \"language\": task.language,\n            \"bddl_path\": bddl_path,\n            \"init_states\": init_states,\n        })\n\n    log.info(\n        \"Discovered %d _add_N tasks (%d skipped) from %s\",\n        len(tasks), skipped, task_suite,\n    )\n    return tasks\n\n\n# ---------------------------------------------------------------------------\n# Environment creation\n# ---------------------------------------------------------------------------\n\ndef create_env(bddl_path: str) -> object:\n    \"\"\"Create a LIBERO OffScreenRenderEnv from a BDDL file.\"\"\"\n    from libero.libero.envs import OffScreenRenderEnv\n    env = OffScreenRenderEnv(\n        bddl_file_name=bddl_path,\n        camera_heights=LIBERO_ENV_RESOLUTION,\n        camera_widths=LIBERO_ENV_RESOLUTION,\n    )\n    return env\n\n\ndef create_spatial_bddl(\n    base_bddl_path: str,\n    perturbation_config: dict,\n    output_dir: str,\n) -> str:\n    \"\"\"Create a perturbed BDDL file by applying spatial perturbation to all regions.\n\n    Returns the path to the new BDDL file.\n    \"\"\"\n    sys.path.insert(0, \"/root/LIBERO-plus/libero\")\n    from libero.randomizer.bddl_operators import (\n        load_bddl_file,\n        save_bddl_file,\n        perturb_region_info,\n    )\n\n    spec = load_bddl_file(base_bddl_path)\n    delta_xy = perturbation_config[\"delta_xy\"]\n    delta_half = perturbation_config[\"delta_half_len\"]\n    delta_yaw = perturbation_config[\"delta_yaw\"]\n\n    for i in range(len(spec.region_infos)):\n        spec.region_infos[i] = perturb_region_info(\n            spec.region_infos[i],\n            delta_region_centroid_xy=delta_xy,\n            delta_region_half_len=delta_half,\n            delta_yaw_rotation=delta_yaw,\n        )\n\n    os.makedirs(output_dir, exist_ok=True)\n    base_name = Path(base_bddl_path).stem\n    dx, dy = delta_xy\n    filename = f\"{base_name}_spatial_dx{dx:.2f}_dy{dy:.2f}.bddl\"\n    _, filepath = save_bddl_file(spec, bddl_filename=filename, bddl_dirpath=output_dir)\n    return filepath\n\n\n# ---------------------------------------------------------------------------\n# Episode rollout\n# ---------------------------------------------------------------------------\n\ndef rollout_episode(\n    policy: object,\n    env: object,\n    task_description: str,\n    init_states: np.ndarray,\n    init_state_idx: int,\n    seed: int,\n) -> dict[str, Any]:\n    \"\"\"Run one episode, collecting (obs, action) pairs.\n\n    Returns dict with observations, actions, success, num_steps.\n    \"\"\"\n    env.seed(seed)\n    obs = env.set_init_state(init_states[init_state_idx])\n\n    for _ in range(NUM_STEPS_WAIT):\n        obs, _, _, _ = env.step(LIBERO_DUMMY_ACTION)\n\n    all_obs = [extract_obs_for_saving(obs)]\n    all_actions = []\n    action_plan = collections.deque()\n    step = 0\n    success = False\n    done = False\n\n    while not done and step < MAX_STEPS:\n        if len(action_plan) == 0:\n            obs_dict = obs_to_model_input(obs, task_description)\n            result = policy.infer(obs_dict)\n            action_chunk = result[\"actions\"]\n            action_plan.extend(action_chunk[:REPLAN_STEPS])\n\n        action = action_plan.popleft()\n        if isinstance(action, torch.Tensor):\n            action = action.cpu().numpy()\n        action_np = np.asarray(action, dtype=np.float32)\n\n        obs, reward, done, info = env.step(\n            action_np.tolist() if hasattr(action_np, \"tolist\") else list(action_np)\n        )\n        step += 1\n\n        all_obs.append(extract_obs_for_saving(obs))\n        all_actions.append(action_np)\n\n        if done or reward > 0:\n            success = info.get(\"success\", reward > 0)\n\n    return {\n        \"observations\": all_obs,\n        \"actions\": np.stack(all_actions) if all_actions else np.zeros((0, 7)),\n        \"success\": success,\n        \"num_steps\": step,\n    }\n\n\n# ---------------------------------------------------------------------------\n# Collection loops\n# ---------------------------------------------------------------------------\n\ndef collect_physical(\n    policy: object,\n    tasks: list[dict],\n    episodes_per_config: int,\n    output_dir: str,\n    dry_run: bool,\n) -> dict:\n    \"\"\"Collect expert demos with physical (robot initial state) perturbation.\n\n    Uses init_states indices 1-49 (index 0 is nominal).\n    \"\"\"\n    os.makedirs(output_dir, exist_ok=True)\n    stats = {\"total\": 0, \"success\": 0, \"saved_files\": []}\n\n    init_state_indices = list(range(1, 50))  # 49 perturbed states\n    if dry_run:\n        tasks = tasks[:1]\n        init_state_indices = [1]\n        episodes_per_config = 1\n\n    for task_info in tasks:\n        task_name = task_info[\"name\"]\n        init_states = torch.load(task_info[\"init_states_path\"], weights_only=False)\n        language = get_task_language(task_info[\"bddl_path\"])\n        log.info(\"Task: %s (%d init_states available)\", task_name, len(init_states))\n\n        for idx in init_state_indices:\n            if idx >= len(init_states):\n                continue\n\n            for ep in range(episodes_per_config):\n                seed = hash((task_name, idx, ep)) % (2**31)\n                stats[\"total\"] += 1\n\n                try:\n                    env = create_env(task_info[\"bddl_path\"])\n                    result = rollout_episode(\n                        policy, env, language, init_states, idx, seed\n                    )\n                    env.close()\n                except Exception:\n                    log.exception(\n                        \"Episode failed: task=%s idx=%d ep=%d\", task_name, idx, ep\n                    )\n                    continue\n\n                if result[\"success\"]:\n                    stats[\"success\"] += 1\n                    demo = {\n                        \"observations\": result[\"observations\"],\n                        \"actions\": result[\"actions\"],\n                        \"task_name\": task_name,\n                        \"perturbation_config\": {\n                            \"type\": \"physical\",\n                            \"init_state_idx\": idx,\n                        },\n                        \"success\": True,\n                        \"num_steps\": result[\"num_steps\"],\n                    }\n                    fname = f\"{task_name}_initstate{idx}_ep{ep}.pkl\"\n                    fpath = os.path.join(output_dir, fname)\n                    with open(fpath, \"wb\") as f:\n                        pickle.dump(demo, f, protocol=pickle.HIGHEST_PROTOCOL)\n                    stats[\"saved_files\"].append(fpath)\n\n                rate = stats[\"success\"] / stats[\"total\"] * 100\n                log.info(\n                    \"[physical] task=%s idx=%d ep=%d | %s | \"\n                    \"cumulative %d/%d (%.1f%%)\",\n                    task_name, idx, ep,\n                    \"SUCCESS\" if result[\"success\"] else \"FAIL\",\n                    stats[\"success\"], stats[\"total\"], rate,\n                )\n\n    return stats\n\n\ndef collect_spatial(\n    policy: object,\n    tasks: list[dict],\n    episodes_per_config: int,\n    output_dir: str,\n    dry_run: bool,\n) -> dict:\n    \"\"\"Collect expert demos with spatial (objects layout) perturbation.\n\n    Applies 10 predefined spatial perturbation configs to each base task.\n    \"\"\"\n    os.makedirs(output_dir, exist_ok=True)\n    tmp_bddl_dir = os.path.join(output_dir, \"_tmp_bddl\")\n    os.makedirs(tmp_bddl_dir, exist_ok=True)\n    stats = {\"total\": 0, \"success\": 0, \"saved_files\": []}\n\n    configs = SPATIAL_PERTURBATION_CONFIGS\n    if dry_run:\n        tasks = tasks[:1]\n        configs = configs[:1]\n        episodes_per_config = 1\n\n    for task_info in tasks:\n        task_name = task_info[\"name\"]\n        init_states = torch.load(task_info[\"init_states_path\"], weights_only=False)\n        log.info(\"Task: %s\", task_name)\n\n        for cfg_idx, cfg in enumerate(configs):\n            try:\n                perturbed_bddl = create_spatial_bddl(\n                    task_info[\"bddl_path\"], cfg, tmp_bddl_dir\n                )\n                language = get_task_language(perturbed_bddl)\n            except Exception:\n                log.exception(\n                    \"BDDL perturbation failed: task=%s cfg=%d\", task_name, cfg_idx\n                )\n                continue\n\n            for ep in range(episodes_per_config):\n                seed = hash((task_name, cfg_idx, ep)) % (2**31)\n                stats[\"total\"] += 1\n\n                try:\n                    env = create_env(perturbed_bddl)\n                    # Use nominal init_state (index 0) for spatial perturbation\n                    result = rollout_episode(\n                        policy, env, language, init_states, 0, seed\n                    )\n                    env.close()\n                except Exception:\n                    log.exception(\n                        \"Episode failed: task=%s cfg=%d ep=%d\",\n                        task_name, cfg_idx, ep,\n                    )\n                    continue\n\n                if result[\"success\"]:\n                    stats[\"success\"] += 1\n                    demo = {\n                        \"observations\": result[\"observations\"],\n                        \"actions\": result[\"actions\"],\n                        \"task_name\": task_name,\n                        \"perturbation_config\": {\n                            \"type\": \"spatial\",\n                            \"config_idx\": cfg_idx,\n                            \"delta_xy\": cfg[\"delta_xy\"],\n                            \"delta_half_len\": cfg[\"delta_half_len\"],\n                            \"delta_yaw\": cfg[\"delta_yaw\"],\n                        },\n                        \"success\": True,\n                        \"num_steps\": result[\"num_steps\"],\n                    }\n                    fname = f\"{task_name}_spatial{cfg_idx}_ep{ep}.pkl\"\n                    fpath = os.path.join(output_dir, fname)\n                    with open(fpath, \"wb\") as f:\n                        pickle.dump(demo, f, protocol=pickle.HIGHEST_PROTOCOL)\n                    stats[\"saved_files\"].append(fpath)\n\n                rate = stats[\"success\"] / stats[\"total\"] * 100\n                log.info(\n                    \"[spatial] task=%s cfg=%d ep=%d | %s | \"\n                    \"cumulative %d/%d (%.1f%%)\",\n                    task_name, cfg_idx, ep,\n                    \"SUCCESS\" if result[\"success\"] else \"FAIL\",\n                    stats[\"success\"], stats[\"total\"], rate,\n                )\n\n    return stats\n\n\n# ---------------------------------------------------------------------------\n# Main\n# ---------------------------------------------------------------------------\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Collect expert demos from π₀ in perturbed LIBERO environments\"\n    )\n    parser.add_argument(\n        \"--perturbation_type\", type=str, required=True,\n        choices=[\"physical\", \"spatial\"],\n    )\n    parser.add_argument(\"--gpu_id\", type=int, default=0)\n    parser.add_argument(\"--num_tasks\", type=int, default=10)\n    parser.add_argument(\"--episodes_per_config\", type=int, default=3)\n    parser.add_argument(\n        \"--output_dir\", type=str, default=None,\n        help=\"Override output directory (default: auto from perturbation_type)\",\n    )\n    parser.add_argument(\n        \"--checkpoint\", type=str,\n        default=\"/root/autodl-tmp/checkpoints/pi0_base\",\n    )\n    parser.add_argument(\"--dry_run\", action=\"store_true\")\n    parser.add_argument(\"--seed\", type=int, default=42)\n    args = parser.parse_args()\n\n    logging.basicConfig(\n        level=logging.INFO,\n        format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    )\n\n    random.seed(args.seed)\n    np.random.seed(args.seed)\n    torch.manual_seed(args.seed)\n\n    if args.output_dir is None:\n        args.output_dir = (\n            f\"/root/meta_brain_lora_routing/data/expert_demos/{args.perturbation_type}\"\n        )\n\n    device = f\"cuda:{args.gpu_id}\"\n    log.info(\n        \"Config: type=%s device=%s num_tasks=%d eps_per_cfg=%d dry_run=%s\",\n        args.perturbation_type, device, args.num_tasks,\n        args.episodes_per_config, args.dry_run,\n    )\n\n    log.info(\"Loading π₀ from %s\", args.checkpoint)\n    policy = load_pi0_policy(args.checkpoint, device)\n\n    from libero.libero import get_libero_path\n    bddl_dir = os.path.join(get_libero_path(\"bddl_files\"), BASE_TASK_SUITE)\n    tasks = find_base_tasks(bddl_dir, num_tasks=args.num_tasks)\n\n    if not tasks:\n        log.error(\"No base tasks found in %s\", bddl_dir)\n        sys.exit(1)\n\n    t0 = time.time()\n\n    if args.perturbation_type == \"physical\":\n        stats = collect_physical(\n            policy, tasks, args.episodes_per_config,\n            args.output_dir, args.dry_run,\n        )\n    else:\n        stats = collect_spatial(\n            policy, tasks, args.episodes_per_config,\n            args.output_dir, args.dry_run,\n        )\n\n    elapsed = time.time() - t0\n\n    total_size = sum(\n        os.path.getsize(f) for f in stats[\"saved_files\"] if os.path.exists(f)\n    )\n    log.info(\"=\" * 60)\n    log.info(\"Collection complete: %s\", args.perturbation_type)\n    log.info(\"  Total episodes:  %d\", stats[\"total\"])\n    log.info(\"  Successful:      %d\", stats[\"success\"])\n    log.info(\n        \"  Success rate:    %.1f%%\",\n        stats[\"success\"] / max(stats[\"total\"], 1) * 100,\n    )\n    log.info(\"  Files saved:     %d\", len(stats[\"saved_files\"]))\n    log.info(\"  Total size:      %.1f MB\", total_size / 1024 / 1024)\n    log.info(\"  Elapsed:         %.1f min\", elapsed / 60)\n    log.info(\"  Output dir:      %s\", args.output_dir)\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 552,
        "oldLines": 6,
        "newStart": 552,
        "newLines": 89,
        "lines": [
          "     return stats",
          " ",
          " ",
          "+def collect_spatial_add_n(",
          "+    policy: object,",
          "+    episodes_per_task: int,",
          "+    output_dir: str,",
          "+    dry_run: bool,",
          "+) -> dict:",
          "+    \"\"\"Collect expert demos using LIBERO-Plus _add_N distractor-object tasks.",
          "+",
          "+    Each _add_N task is a pre-built BDDL with extra objects in the scene.",
          "+    208 tasks × 3 episodes = 624 rollouts.",
          "+    \"\"\"",
          "+    os.makedirs(output_dir, exist_ok=True)",
          "+    stats = {\"total\": 0, \"success\": 0, \"saved_files\": [], \"load_errors\": 0}",
          "+",
          "+    add_tasks = discover_add_n_tasks()",
          "+    if not add_tasks:",
          "+        log.error(\"No _add_N tasks found. Check LIBERO-Plus installation.\")",
          "+        return stats",
          "+",
          "+    if dry_run:",
          "+        add_tasks = add_tasks[:2]",
          "+        episodes_per_task = 1",
          "+",
          "+    log.info(",
          "+        \"Collecting spatial (_add_N): %d tasks × %d eps = %d rollouts\",",
          "+        len(add_tasks), episodes_per_task, len(add_tasks) * episodes_per_task,",
          "+    )",
          "+",
          "+    for task_info in add_tasks:",
          "+        task_name = task_info[\"name\"]",
          "+        language = task_info[\"language\"]",
          "+        init_states = task_info[\"init_states\"]",
          "+",
          "+        for ep in range(episodes_per_task):",
          "+            seed = hash((task_name, ep)) % (2**31)",
          "+            stats[\"total\"] += 1",
          "+",
          "+            try:",
          "+                env = create_env(task_info[\"bddl_path\"])",
          "+                init_idx = ep % len(init_states)",
          "+                result = rollout_episode(",
          "+                    policy, env, language, init_states, init_idx, seed",
          "+                )",
          "+                env.close()",
          "+            except FileNotFoundError as e:",
          "+                stats[\"load_errors\"] += 1",
          "+                log.warning(\"Asset missing for %s: %s\", task_name, e)",
          "+                continue",
          "+            except Exception:",
          "+                log.exception(\"Episode failed: task=%s ep=%d\", task_name, ep)",
          "+                continue",
          "+",
          "+            if result[\"success\"]:",
          "+                stats[\"success\"] += 1",
          "+                demo = {",
          "+                    \"observations\": result[\"observations\"],",
          "+                    \"actions\": result[\"actions\"],",
          "+                    \"task_name\": task_name,",
          "+                    \"perturbation_config\": {",
          "+                        \"type\": \"spatial_add_n\",",
          "+                        \"source_task_idx\": task_info[\"idx\"],",
          "+                    },",
          "+                    \"success\": True,",
          "+                    \"num_steps\": result[\"num_steps\"],",
          "+                }",
          "+                fname = f\"{task_name}_ep{ep}.pkl\"",
          "+                fpath = os.path.join(output_dir, fname)",
          "+                with open(fpath, \"wb\") as f:",
          "+                    pickle.dump(demo, f, protocol=pickle.HIGHEST_PROTOCOL)",
          "+                stats[\"saved_files\"].append(fpath)",
          "+",
          "+            rate = stats[\"success\"] / stats[\"total\"] * 100",
          "+            log.info(",
          "+                \"[spatial_add_n] task=%s ep=%d | %s | cumulative %d/%d (%.1f%%) | load_errors=%d\",",
          "+                task_name, ep,",
          "+                \"SUCCESS\" if result[\"success\"] else \"FAIL\",",
          "+                stats[\"success\"], stats[\"total\"], rate,",
          "+                stats[\"load_errors\"],",
          "+            )",
          "+",
          "+    return stats",
          "+",
          "+",
          " # ---------------------------------------------------------------------------",
          " # Main",
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


### Assistant

_source line 111_

Now update `main()` to add `--spatial_mode` argument and route accordingly:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "133acf06-27d6-48a1-854c-b02483d7e4fd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K1Uv7sZffGoVVaVTXQZxKm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1109,
      "cache_read_input_tokens": 45484,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1109
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

_source line 112_

<details open><summary>🔧 Tool call — Edit · `toolu_01EHS5CKmQVtWYHvgAZndh9m`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py",
  "old_string": "    parser.add_argument(\n        \"--perturbation_type\", type=str, required=True,\n        choices=[\"physical\", \"spatial\"],\n    )\n    parser.add_argument(\"--gpu_id\", type=int, default=0)\n    parser.add_argument(\"--num_tasks\", type=int, default=10)\n    parser.add_argument(\"--episodes_per_config\", type=int, default=3)",
  "new_string": "    parser.add_argument(\n        \"--perturbation_type\", type=str, required=True,\n        choices=[\"physical\", \"spatial\"],\n    )\n    parser.add_argument(\n        \"--spatial_mode\", type=str, default=\"add_n\",\n        choices=[\"add_n\", \"perturb_region\"],\n        help=\"Spatial perturbation mode: add_n (LIBERO-Plus distractors, default) \"\n             \"or perturb_region (legacy BDDL region shifts)\",\n    )\n    parser.add_argument(\"--gpu_id\", type=int, default=0)\n    parser.add_argument(\"--num_tasks\", type=int, default=10)\n    parser.add_argument(\"--episodes_per_config\", type=int, default=3)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "2398fa97-5bdb-48b9-9462-cdbd0281ec28",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K1Uv7sZffGoVVaVTXQZxKm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1109,
      "cache_read_input_tokens": 45484,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1109
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

_source line 113 · 2026-05-15T17:52:18.884Z_

<details><summary>↩ Tool result · `toolu_01EHS5CKmQVtWYHvgAZndh9m`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "45fd3f08-6f04-43b7-a6dd-9fd68c8cb3cb",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py",
    "oldString": "    parser.add_argument(\n        \"--perturbation_type\", type=str, required=True,\n        choices=[\"physical\", \"spatial\"],\n    )\n    parser.add_argument(\"--gpu_id\", type=int, default=0)\n    parser.add_argument(\"--num_tasks\", type=int, default=10)\n    parser.add_argument(\"--episodes_per_config\", type=int, default=3)",
    "newString": "    parser.add_argument(\n        \"--perturbation_type\", type=str, required=True,\n        choices=[\"physical\", \"spatial\"],\n    )\n    parser.add_argument(\n        \"--spatial_mode\", type=str, default=\"add_n\",\n        choices=[\"add_n\", \"perturb_region\"],\n        help=\"Spatial perturbation mode: add_n (LIBERO-Plus distractors, default) \"\n             \"or perturb_region (legacy BDDL region shifts)\",\n    )\n    parser.add_argument(\"--gpu_id\", type=int, default=0)\n    parser.add_argument(\"--num_tasks\", type=int, default=10)\n    parser.add_argument(\"--episodes_per_config\", type=int, default=3)",
    "originalFile": "\"\"\"\nCollect expert demonstrations by rolling out frozen π₀ in perturbed LIBERO environments.\n\nOnly successful episodes are saved. Two perturbation types are supported:\n  - physical: vary robot initial state (init_states index 1-49)\n  - spatial:  LIBERO-Plus _add_N distractor objects (default) or perturb_region fallback\n\nOutput: pickle files with (observations, actions, metadata) per episode.\n\nUsage:\n    # Physical perturbation dry-run\n    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \\\n        --perturbation_type physical --dry_run\n\n    # Spatial perturbation dry-run (uses _add_N by default)\n    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \\\n        --perturbation_type spatial --dry_run\n\n    # Spatial with legacy perturb_region mode\n    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \\\n        --perturbation_type spatial --spatial_mode perturb_region --dry_run\n\n    # Full physical collection\n    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \\\n        --perturbation_type physical\n\"\"\"\n\nimport argparse\nimport collections\nimport copy\nimport logging\nimport math\nimport os\nimport pickle\nimport random\nimport re\nimport sys\nimport time\nimport types\nfrom pathlib import Path\nfrom typing import Any\n\nimport numpy as np\nimport torch\n\nlog = logging.getLogger(__name__)\n\n# ---------------------------------------------------------------------------\n# Constants\n# ---------------------------------------------------------------------------\n\nLIBERO_DUMMY_ACTION = [0.0] * 6 + [-1.0]\nLIBERO_ENV_RESOLUTION = 256\nMODEL_INPUT_RESOLUTION = 224\nREPLAN_STEPS = 5\nNUM_STEPS_WAIT = 10\nMAX_STEPS = 220  # libero_spatial default\n\n# 10 base tasks in libero_spatial (no perturbation suffix)\nBASE_TASK_SUITE = \"libero_spatial\"\n\n# Spatial perturbation grid: 10 configurations with varying XY shifts and yaw\n# Magnitudes chosen to be noticeable but within feasible reach of the robot.\nSPATIAL_PERTURBATION_CONFIGS = [\n    {\"delta_xy\": ( 0.05,  0.00), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.0)},\n    {\"delta_xy\": (-0.05,  0.00), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.0)},\n    {\"delta_xy\": ( 0.00,  0.05), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.0)},\n    {\"delta_xy\": ( 0.00, -0.05), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.0)},\n    {\"delta_xy\": ( 0.03,  0.03), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.0)},\n    {\"delta_xy\": (-0.03, -0.03), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.0)},\n    {\"delta_xy\": ( 0.04,  0.00), \"delta_half_len\": 0.01, \"delta_yaw\": (0.3, 0.0)},\n    {\"delta_xy\": (-0.04,  0.00), \"delta_half_len\": 0.01, \"delta_yaw\": (-0.3, 0.0)},\n    {\"delta_xy\": ( 0.00,  0.04), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.3)},\n    {\"delta_xy\": ( 0.00, -0.04), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, -0.3)},\n]\n\n\n# ---------------------------------------------------------------------------\n# Geometry / image helpers (from libero_integration.py)\n# ---------------------------------------------------------------------------\n\ndef _quat2axisangle(quat: np.ndarray) -> np.ndarray:\n    \"\"\"Quaternion [x,y,z,w] -> axis-angle [ax,ay,az].\"\"\"\n    q = np.asarray(quat, dtype=np.float64)\n    norm = np.linalg.norm(q)\n    if norm < 1e-8:\n        return np.zeros(3, dtype=np.float32)\n    q /= norm\n    sin_half = np.linalg.norm(q[:3])\n    if sin_half < 1e-8:\n        return np.zeros(3, dtype=np.float32)\n    angle = 2.0 * math.atan2(sin_half, q[3])\n    axis = q[:3] / sin_half\n    return (axis * angle).astype(np.float32)\n\n\ndef _resize_with_pad(img: np.ndarray, size: int) -> np.ndarray:\n    \"\"\"Resize image with aspect-preserving padding to (size, size, 3) uint8.\"\"\"\n    try:\n        from openpi_client.image_tools import resize_with_pad, convert_to_uint8\n        return convert_to_uint8(resize_with_pad(img, size, size))\n    except ImportError:\n        from PIL import Image as PILImage\n        h, w = img.shape[:2]\n        scale = min(size / h, size / w)\n        new_h, new_w = int(h * scale), int(w * scale)\n        resized = np.array(\n            PILImage.fromarray(img).resize((new_w, new_h), PILImage.BILINEAR)\n        )\n        canvas = np.zeros((size, size, 3), dtype=np.uint8)\n        y0, x0 = (size - new_h) // 2, (size - new_w) // 2\n        canvas[y0 : y0 + new_h, x0 : x0 + new_w] = resized\n        return canvas\n\n\ndef obs_to_model_input(obs: dict, task_description: str) -> dict:\n    \"\"\"Convert LIBERO observation to the dict format expected by policy.infer().\"\"\"\n    base_img = np.ascontiguousarray(obs[\"agentview_image\"][::-1, ::-1])\n    wrist_img = np.ascontiguousarray(obs[\"robot0_eye_in_hand_image\"][::-1, ::-1])\n\n    base_img = _resize_with_pad(base_img, MODEL_INPUT_RESOLUTION)\n    wrist_img = _resize_with_pad(wrist_img, MODEL_INPUT_RESOLUTION)\n\n    state = np.concatenate([\n        obs[\"robot0_eef_pos\"].astype(np.float32),\n        _quat2axisangle(obs[\"robot0_eef_quat\"]),\n        obs[\"robot0_gripper_qpos\"].astype(np.float32),\n    ])\n\n    return {\n        \"observation/image\": base_img,\n        \"observation/wrist_image\": wrist_img,\n        \"observation/state\": state,\n        \"prompt\": task_description,\n    }\n\n\ndef extract_obs_for_saving(obs: dict) -> dict:\n    \"\"\"Extract observation fields to save in demo data (images stored as uint8).\"\"\"\n    return {\n        \"agentview_image\": obs[\"agentview_image\"].copy(),\n        \"robot0_eye_in_hand_image\": obs[\"robot0_eye_in_hand_image\"].copy(),\n        \"robot0_eef_pos\": obs[\"robot0_eef_pos\"].astype(np.float32).copy(),\n        \"robot0_eef_quat\": obs[\"robot0_eef_quat\"].astype(np.float32).copy(),\n        \"robot0_gripper_qpos\": obs[\"robot0_gripper_qpos\"].astype(np.float32).copy(),\n    }\n\n\n# ---------------------------------------------------------------------------\n# Model loading\n# ---------------------------------------------------------------------------\n\ndef _ensure_openpi_imports():\n    \"\"\"Stub out lerobot (training-only dep) before importing OpenPI.\"\"\"\n    for mod in [\n        \"lerobot\", \"lerobot.common\", \"lerobot.common.datasets\",\n        \"lerobot.common.datasets.lerobot_dataset\",\n    ]:\n        if mod not in sys.modules:\n            sys.modules[mod] = types.ModuleType(mod)\n\n\ndef load_pi0_policy(checkpoint_path: str, device: str) -> object:\n    \"\"\"Load pi0 policy via OpenPI. Returns the Policy object for inference.\"\"\"\n    _ensure_openpi_imports()\n    from openpi.training import config as _config\n    from openpi.policies import policy_config\n\n    train_config = _config.get_config(\"pi0_libero\")\n    policy = policy_config.create_trained_policy(\n        train_config, checkpoint_path, pytorch_device=device\n    )\n    log.info(\"Loaded pi0 policy on %s\", device)\n    return policy\n\n\n# ---------------------------------------------------------------------------\n# Task discovery\n# ---------------------------------------------------------------------------\n\ndef find_base_tasks(bddl_dir: str, num_tasks: int = 10) -> list[dict]:\n    \"\"\"Find base (unperturbed) BDDL files in libero_spatial.\n\n    Returns list of dicts with keys: name, bddl_path, init_states_path.\n    \"\"\"\n    all_files = [f for f in os.listdir(bddl_dir) if f.endswith(\".bddl\")]\n\n    base_names = []\n    for f in sorted(all_files):\n        name = f.replace(\".bddl\", \"\")\n        # Skip any file with perturbation suffixes\n        if re.search(\n            r\"(_add_\\d+|_table_\\d+|_tb_\\d+|_light_\\d+|_language_\\d+\"\n            r\"|_view_|_noise_|_level\\d+| copy)\",\n            name,\n        ):\n            continue\n        base_names.append(name)\n\n    init_dir = bddl_dir.replace(\"bddl_files\", \"init_files\")\n    tasks = []\n    for name in base_names[:num_tasks]:\n        bddl_path = os.path.join(bddl_dir, f\"{name}.bddl\")\n        init_path = os.path.join(init_dir, f\"{name}.pruned_init\")\n        if not os.path.exists(init_path):\n            log.warning(\"init_states not found for %s, skipping\", name)\n            continue\n        tasks.append({\n            \"name\": name,\n            \"bddl_path\": bddl_path,\n            \"init_states_path\": init_path,\n        })\n\n    log.info(\"Found %d base tasks\", len(tasks))\n    return tasks\n\n\ndef get_task_language(bddl_path: str) -> str:\n    \"\"\"Extract language instruction from a BDDL file.\"\"\"\n    from libero.libero.envs.bddl_utils import get_problem_info\n    info = get_problem_info(bddl_path)\n    return info[\"language_instruction\"]\n\n\ndef discover_add_n_tasks(task_suite: str = BASE_TASK_SUITE) -> list[dict]:\n    \"\"\"Discover all _add_N (distractor-object) tasks from the LIBERO-Plus benchmark.\n\n    Returns list of dicts with: idx, name, language, bddl_path, init_states.\n    \"\"\"\n    from libero.libero import benchmark, get_libero_path\n    benchmark_dict = benchmark.get_benchmark_dict()\n    suite = benchmark_dict[task_suite]()\n    bddl_root = Path(get_libero_path(\"bddl_files\"))\n\n    tasks = []\n    skipped = 0\n    for i in range(suite.n_tasks):\n        task = suite.get_task(i)\n        name = getattr(task, \"name\", \"\") or getattr(task, \"bddl_file\", \"\")\n        if not re.search(r\"_add_\\d+$\", name.replace(\".bddl\", \"\")):\n            continue\n\n        bddl_path = str(bddl_root / task.problem_folder / task.bddl_file)\n        if not os.path.exists(bddl_path):\n            log.warning(\"BDDL not found, skipping: %s\", bddl_path)\n            skipped += 1\n            continue\n\n        try:\n            init_states = suite.get_task_init_states(i)\n        except Exception:\n            log.warning(\"init_states failed for %s, skipping\", name)\n            skipped += 1\n            continue\n\n        tasks.append({\n            \"idx\": i,\n            \"name\": name.replace(\".bddl\", \"\"),\n            \"language\": task.language,\n            \"bddl_path\": bddl_path,\n            \"init_states\": init_states,\n        })\n\n    log.info(\n        \"Discovered %d _add_N tasks (%d skipped) from %s\",\n        len(tasks), skipped, task_suite,\n    )\n    return tasks\n\n\n# ---------------------------------------------------------------------------\n# Environment creation\n# ---------------------------------------------------------------------------\n\ndef create_env(bddl_path: str) -> object:\n    \"\"\"Create a LIBERO OffScreenRenderEnv from a BDDL file.\"\"\"\n    from libero.libero.envs import OffScreenRenderEnv\n    env = OffScreenRenderEnv(\n        bddl_file_name=bddl_path,\n        camera_heights=LIBERO_ENV_RESOLUTION,\n        camera_widths=LIBERO_ENV_RESOLUTION,\n    )\n    return env\n\n\ndef create_spatial_bddl(\n    base_bddl_path: str,\n    perturbation_config: dict,\n    output_dir: str,\n) -> str:\n    \"\"\"Create a perturbed BDDL file by applying spatial perturbation to all regions.\n\n    Returns the path to the new BDDL file.\n    \"\"\"\n    sys.path.insert(0, \"/root/LIBERO-plus/libero\")\n    from libero.randomizer.bddl_operators import (\n        load_bddl_file,\n        save_bddl_file,\n        perturb_region_info,\n    )\n\n    spec = load_bddl_file(base_bddl_path)\n    delta_xy = perturbation_config[\"delta_xy\"]\n    delta_half = perturbation_config[\"delta_half_len\"]\n    delta_yaw = perturbation_config[\"delta_yaw\"]\n\n    for i in range(len(spec.region_infos)):\n        spec.region_infos[i] = perturb_region_info(\n            spec.region_infos[i],\n            delta_region_centroid_xy=delta_xy,\n            delta_region_half_len=delta_half,\n            delta_yaw_rotation=delta_yaw,\n        )\n\n    os.makedirs(output_dir, exist_ok=True)\n    base_name = Path(base_bddl_path).stem\n    dx, dy = delta_xy\n    filename = f\"{base_name}_spatial_dx{dx:.2f}_dy{dy:.2f}.bddl\"\n    _, filepath = save_bddl_file(spec, bddl_filename=filename, bddl_dirpath=output_dir)\n    return filepath\n\n\n# ---------------------------------------------------------------------------\n# Episode rollout\n# ---------------------------------------------------------------------------\n\ndef rollout_episode(\n    policy: object,\n    env: object,\n    task_description: str,\n    init_states: np.ndarray,\n    init_state_idx: int,\n    seed: int,\n) -> dict[str, Any]:\n    \"\"\"Run one episode, collecting (obs, action) pairs.\n\n    Returns dict with observations, actions, success, num_steps.\n    \"\"\"\n    env.seed(seed)\n    obs = env.set_init_state(init_states[init_state_idx])\n\n    for _ in range(NUM_STEPS_WAIT):\n        obs, _, _, _ = env.step(LIBERO_DUMMY_ACTION)\n\n    all_obs = [extract_obs_for_saving(obs)]\n    all_actions = []\n    action_plan = collections.deque()\n    step = 0\n    success = False\n    done = False\n\n    while not done and step < MAX_STEPS:\n        if len(action_plan) == 0:\n            obs_dict = obs_to_model_input(obs, task_description)\n            result = policy.infer(obs_dict)\n            action_chunk = result[\"actions\"]\n            action_plan.extend(action_chunk[:REPLAN_STEPS])\n\n        action = action_plan.popleft()\n        if isinstance(action, torch.Tensor):\n            action = action.cpu().numpy()\n        action_np = np.asarray(action, dtype=np.float32)\n\n        obs, reward, done, info = env.step(\n            action_np.tolist() if hasattr(action_np, \"tolist\") else list(action_np)\n        )\n        step += 1\n\n        all_obs.append(extract_obs_for_saving(obs))\n        all_actions.append(action_np)\n\n        if done or reward > 0:\n            success = info.get(\"success\", reward > 0)\n\n    return {\n        \"observations\": all_obs,\n        \"actions\": np.stack(all_actions) if all_actions else np.zeros((0, 7)),\n        \"success\": success,\n        \"num_steps\": step,\n    }\n\n\n# ---------------------------------------------------------------------------\n# Collection loops\n# ---------------------------------------------------------------------------\n\ndef collect_physical(\n    policy: object,\n    tasks: list[dict],\n    episodes_per_config: int,\n    output_dir: str,\n    dry_run: bool,\n) -> dict:\n    \"\"\"Collect expert demos with physical (robot initial state) perturbation.\n\n    Uses init_states indices 1-49 (index 0 is nominal).\n    \"\"\"\n    os.makedirs(output_dir, exist_ok=True)\n    stats = {\"total\": 0, \"success\": 0, \"saved_files\": []}\n\n    init_state_indices = list(range(1, 50))  # 49 perturbed states\n    if dry_run:\n        tasks = tasks[:1]\n        init_state_indices = [1]\n        episodes_per_config = 1\n\n    for task_info in tasks:\n        task_name = task_info[\"name\"]\n        init_states = torch.load(task_info[\"init_states_path\"], weights_only=False)\n        language = get_task_language(task_info[\"bddl_path\"])\n        log.info(\"Task: %s (%d init_states available)\", task_name, len(init_states))\n\n        for idx in init_state_indices:\n            if idx >= len(init_states):\n                continue\n\n            for ep in range(episodes_per_config):\n                seed = hash((task_name, idx, ep)) % (2**31)\n                stats[\"total\"] += 1\n\n                try:\n                    env = create_env(task_info[\"bddl_path\"])\n                    result = rollout_episode(\n                        policy, env, language, init_states, idx, seed\n                    )\n                    env.close()\n                except Exception:\n                    log.exception(\n                        \"Episode failed: task=%s idx=%d ep=%d\", task_name, idx, ep\n                    )\n                    continue\n\n                if result[\"success\"]:\n                    stats[\"success\"] += 1\n                    demo = {\n                        \"observations\": result[\"observations\"],\n                        \"actions\": result[\"actions\"],\n                        \"task_name\": task_name,\n                        \"perturbation_config\": {\n                            \"type\": \"physical\",\n                            \"init_state_idx\": idx,\n                        },\n                        \"success\": True,\n                        \"num_steps\": result[\"num_steps\"],\n                    }\n                    fname = f\"{task_name}_initstate{idx}_ep{ep}.pkl\"\n                    fpath = os.path.join(output_dir, fname)\n                    with open(fpath, \"wb\") as f:\n                        pickle.dump(demo, f, protocol=pickle.HIGHEST_PROTOCOL)\n                    stats[\"saved_files\"].append(fpath)\n\n                rate = stats[\"success\"] / stats[\"total\"] * 100\n                log.info(\n                    \"[physical] task=%s idx=%d ep=%d | %s | \"\n                    \"cumulative %d/%d (%.1f%%)\",\n                    task_name, idx, ep,\n                    \"SUCCESS\" if result[\"success\"] else \"FAIL\",\n                    stats[\"success\"], stats[\"total\"], rate,\n                )\n\n    return stats\n\n\ndef collect_spatial(\n    policy: object,\n    tasks: list[dict],\n    episodes_per_config: int,\n    output_dir: str,\n    dry_run: bool,\n) -> dict:\n    \"\"\"Collect expert demos with spatial (objects layout) perturbation.\n\n    Applies 10 predefined spatial perturbation configs to each base task.\n    \"\"\"\n    os.makedirs(output_dir, exist_ok=True)\n    tmp_bddl_dir = os.path.join(output_dir, \"_tmp_bddl\")\n    os.makedirs(tmp_bddl_dir, exist_ok=True)\n    stats = {\"total\": 0, \"success\": 0, \"saved_files\": []}\n\n    configs = SPATIAL_PERTURBATION_CONFIGS\n    if dry_run:\n        tasks = tasks[:1]\n        configs = configs[:1]\n        episodes_per_config = 1\n\n    for task_info in tasks:\n        task_name = task_info[\"name\"]\n        init_states = torch.load(task_info[\"init_states_path\"], weights_only=False)\n        log.info(\"Task: %s\", task_name)\n\n        for cfg_idx, cfg in enumerate(configs):\n            try:\n                perturbed_bddl = create_spatial_bddl(\n                    task_info[\"bddl_path\"], cfg, tmp_bddl_dir\n                )\n                language = get_task_language(perturbed_bddl)\n            except Exception:\n                log.exception(\n                    \"BDDL perturbation failed: task=%s cfg=%d\", task_name, cfg_idx\n                )\n                continue\n\n            for ep in range(episodes_per_config):\n                seed = hash((task_name, cfg_idx, ep)) % (2**31)\n                stats[\"total\"] += 1\n\n                try:\n                    env = create_env(perturbed_bddl)\n                    # Use nominal init_state (index 0) for spatial perturbation\n                    result = rollout_episode(\n                        policy, env, language, init_states, 0, seed\n                    )\n                    env.close()\n                except Exception:\n                    log.exception(\n                        \"Episode failed: task=%s cfg=%d ep=%d\",\n                        task_name, cfg_idx, ep,\n                    )\n                    continue\n\n                if result[\"success\"]:\n                    stats[\"success\"] += 1\n                    demo = {\n                        \"observations\": result[\"observations\"],\n                        \"actions\": result[\"actions\"],\n                        \"task_name\": task_name,\n                        \"perturbation_config\": {\n                            \"type\": \"spatial\",\n                            \"config_idx\": cfg_idx,\n                            \"delta_xy\": cfg[\"delta_xy\"],\n                            \"delta_half_len\": cfg[\"delta_half_len\"],\n                            \"delta_yaw\": cfg[\"delta_yaw\"],\n                        },\n                        \"success\": True,\n                        \"num_steps\": result[\"num_steps\"],\n                    }\n                    fname = f\"{task_name}_spatial{cfg_idx}_ep{ep}.pkl\"\n                    fpath = os.path.join(output_dir, fname)\n                    with open(fpath, \"wb\") as f:\n                        pickle.dump(demo, f, protocol=pickle.HIGHEST_PROTOCOL)\n                    stats[\"saved_files\"].append(fpath)\n\n                rate = stats[\"success\"] / stats[\"total\"] * 100\n                log.info(\n                    \"[spatial] task=%s cfg=%d ep=%d | %s | \"\n                    \"cumulative %d/%d (%.1f%%)\",\n                    task_name, cfg_idx, ep,\n                    \"SUCCESS\" if result[\"success\"] else \"FAIL\",\n                    stats[\"success\"], stats[\"total\"], rate,\n                )\n\n    return stats\n\n\ndef collect_spatial_add_n(\n    policy: object,\n    episodes_per_task: int,\n    output_dir: str,\n    dry_run: bool,\n) -> dict:\n    \"\"\"Collect expert demos using LIBERO-Plus _add_N distractor-object tasks.\n\n    Each _add_N task is a pre-built BDDL with extra objects in the scene.\n    208 tasks × 3 episodes = 624 rollouts.\n    \"\"\"\n    os.makedirs(output_dir, exist_ok=True)\n    stats = {\"total\": 0, \"success\": 0, \"saved_files\": [], \"load_errors\": 0}\n\n    add_tasks = discover_add_n_tasks()\n    if not add_tasks:\n        log.error(\"No _add_N tasks found. Check LIBERO-Plus installation.\")\n        return stats\n\n    if dry_run:\n        add_tasks = add_tasks[:2]\n        episodes_per_task = 1\n\n    log.info(\n        \"Collecting spatial (_add_N): %d tasks × %d eps = %d rollouts\",\n        len(add_tasks), episodes_per_task, len(add_tasks) * episodes_per_task,\n    )\n\n    for task_info in add_tasks:\n        task_name = task_info[\"name\"]\n        language = task_info[\"language\"]\n        init_states = task_info[\"init_states\"]\n\n        for ep in range(episodes_per_task):\n            seed = hash((task_name, ep)) % (2**31)\n            stats[\"total\"] += 1\n\n            try:\n                env = create_env(task_info[\"bddl_path\"])\n                init_idx = ep % len(init_states)\n                result = rollout_episode(\n                    policy, env, language, init_states, init_idx, seed\n                )\n                env.close()\n            except FileNotFoundError as e:\n                stats[\"load_errors\"] += 1\n                log.warning(\"Asset missing for %s: %s\", task_name, e)\n                continue\n            except Exception:\n                log.exception(\"Episode failed: task=%s ep=%d\", task_name, ep)\n                continue\n\n            if result[\"success\"]:\n                stats[\"success\"] += 1\n                demo = {\n                    \"observations\": result[\"observations\"],\n                    \"actions\": result[\"actions\"],\n                    \"task_name\": task_name,\n                    \"perturbation_config\": {\n                        \"type\": \"spatial_add_n\",\n                        \"source_task_idx\": task_info[\"idx\"],\n                    },\n                    \"success\": True,\n                    \"num_steps\": result[\"num_steps\"],\n                }\n                fname = f\"{task_name}_ep{ep}.pkl\"\n                fpath = os.path.join(output_dir, fname)\n                with open(fpath, \"wb\") as f:\n                    pickle.dump(demo, f, protocol=pickle.HIGHEST_PROTOCOL)\n                stats[\"saved_files\"].append(fpath)\n\n            rate = stats[\"success\"] / stats[\"total\"] * 100\n            log.info(\n                \"[spatial_add_n] task=%s ep=%d | %s | cumulative %d/%d (%.1f%%) | load_errors=%d\",\n                task_name, ep,\n                \"SUCCESS\" if result[\"success\"] else \"FAIL\",\n                stats[\"success\"], stats[\"total\"], rate,\n                stats[\"load_errors\"],\n            )\n\n    return stats\n\n\n# ---------------------------------------------------------------------------\n# Main\n# ---------------------------------------------------------------------------\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Collect expert demos from π₀ in perturbed LIBERO environments\"\n    )\n    parser.add_argument(\n        \"--perturbation_type\", type=str, required=True,\n        choices=[\"physical\", \"spatial\"],\n    )\n    parser.add_argument(\"--gpu_id\", type=int, default=0)\n    parser.add_argument(\"--num_tasks\", type=int, default=10)\n    parser.add_argument(\"--episodes_per_config\", type=int, default=3)\n    parser.add_argument(\n        \"--output_dir\", type=str, default=None,\n        help=\"Override output directory (default: auto from perturbation_type)\",\n    )\n    parser.add_argument(\n        \"--checkpoint\", type=str,\n        default=\"/root/autodl-tmp/checkpoints/pi0_base\",\n    )\n    parser.add_argument(\"--dry_run\", action=\"store_true\")\n    parser.add_argument(\"--seed\", type=int, default=42)\n    args = parser.parse_args()\n\n    logging.basicConfig(\n        level=logging.INFO,\n        format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    )\n\n    random.seed(args.seed)\n    np.random.seed(args.seed)\n    torch.manual_seed(args.seed)\n\n    if args.output_dir is None:\n        args.output_dir = (\n            f\"/root/meta_brain_lora_routing/data/expert_demos/{args.perturbation_type}\"\n        )\n\n    device = f\"cuda:{args.gpu_id}\"\n    log.info(\n        \"Config: type=%s device=%s num_tasks=%d eps_per_cfg=%d dry_run=%s\",\n        args.perturbation_type, device, args.num_tasks,\n        args.episodes_per_config, args.dry_run,\n    )\n\n    log.info(\"Loading π₀ from %s\", args.checkpoint)\n    policy = load_pi0_policy(args.checkpoint, device)\n\n    from libero.libero import get_libero_path\n    bddl_dir = os.path.join(get_libero_path(\"bddl_files\"), BASE_TASK_SUITE)\n    tasks = find_base_tasks(bddl_dir, num_tasks=args.num_tasks)\n\n    if not tasks:\n        log.error(\"No base tasks found in %s\", bddl_dir)\n        sys.exit(1)\n\n    t0 = time.time()\n\n    if args.perturbation_type == \"physical\":\n        stats = collect_physical(\n            policy, tasks, args.episodes_per_config,\n            args.output_dir, args.dry_run,\n        )\n    else:\n        stats = collect_spatial(\n            policy, tasks, args.episodes_per_config,\n            args.output_dir, args.dry_run,\n        )\n\n    elapsed = time.time() - t0\n\n    total_size = sum(\n        os.path.getsize(f) for f in stats[\"saved_files\"] if os.path.exists(f)\n    )\n    log.info(\"=\" * 60)\n    log.info(\"Collection complete: %s\", args.perturbation_type)\n    log.info(\"  Total episodes:  %d\", stats[\"total\"])\n    log.info(\"  Successful:      %d\", stats[\"success\"])\n    log.info(\n        \"  Success rate:    %.1f%%\",\n        stats[\"success\"] / max(stats[\"total\"], 1) * 100,\n    )\n    log.info(\"  Files saved:     %d\", len(stats[\"saved_files\"]))\n    log.info(\"  Total size:      %.1f MB\", total_size / 1024 / 1024)\n    log.info(\"  Elapsed:         %.1f min\", elapsed / 60)\n    log.info(\"  Output dir:      %s\", args.output_dir)\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 647,
        "oldLines": 6,
        "newStart": 647,
        "newLines": 12,
        "lines": [
          "         \"--perturbation_type\", type=str, required=True,",
          "         choices=[\"physical\", \"spatial\"],",
          "     )",
          "+    parser.add_argument(",
          "+        \"--spatial_mode\", type=str, default=\"add_n\",",
          "+        choices=[\"add_n\", \"perturb_region\"],",
          "+        help=\"Spatial perturbation mode: add_n (LIBERO-Plus distractors, default) \"",
          "+             \"or perturb_region (legacy BDDL region shifts)\",",
          "+    )",
          "     parser.add_argument(\"--gpu_id\", type=int, default=0)",
          "     parser.add_argument(\"--num_tasks\", type=int, default=10)",
          "     parser.add_argument(\"--episodes_per_config\", type=int, default=3)"
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

_source line 114_

Now update the routing in `main()`:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "f3a8636e-4d22-4659-8b0c-e301ce2fa788",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KmxFwmLS4sJYQqFjoa8rmv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 522,
      "cache_read_input_tokens": 46593,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 522
      },
      "output_tokens": 5,
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

_source line 115_

<details open><summary>🔧 Tool call — Edit · `toolu_01E66bPgEjvwTQF1QjNpeyLb`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py",
  "old_string": "    log.info(\n        \"Config: type=%s device=%s num_tasks=%d eps_per_cfg=%d dry_run=%s\",\n        args.perturbation_type, device, args.num_tasks,\n        args.episodes_per_config, args.dry_run,\n    )\n\n    log.info(\"Loading π₀ from %s\", args.checkpoint)\n    policy = load_pi0_policy(args.checkpoint, device)\n\n    from libero.libero import get_libero_path\n    bddl_dir = os.path.join(get_libero_path(\"bddl_files\"), BASE_TASK_SUITE)\n    tasks = find_base_tasks(bddl_dir, num_tasks=args.num_tasks)\n\n    if not tasks:\n        log.error(\"No base tasks found in %s\", bddl_dir)\n        sys.exit(1)\n\n    t0 = time.time()\n\n    if args.perturbation_type == \"physical\":\n        stats = collect_physical(\n            policy, tasks, args.episodes_per_config,\n            args.output_dir, args.dry_run,\n        )\n    else:\n        stats = collect_spatial(\n            policy, tasks, args.episodes_per_config,\n            args.output_dir, args.dry_run,\n        )",
  "new_string": "    log.info(\n        \"Config: type=%s spatial_mode=%s device=%s num_tasks=%d eps_per_cfg=%d dry_run=%s\",\n        args.perturbation_type, args.spatial_mode, device, args.num_tasks,\n        args.episodes_per_config, args.dry_run,\n    )\n\n    log.info(\"Loading π₀ from %s\", args.checkpoint)\n    policy = load_pi0_policy(args.checkpoint, device)\n\n    t0 = time.time()\n\n    if args.perturbation_type == \"physical\":\n        from libero.libero import get_libero_path\n        bddl_dir = os.path.join(get_libero_path(\"bddl_files\"), BASE_TASK_SUITE)\n        tasks = find_base_tasks(bddl_dir, num_tasks=args.num_tasks)\n        if not tasks:\n            log.error(\"No base tasks found in %s\", bddl_dir)\n            sys.exit(1)\n        stats = collect_physical(\n            policy, tasks, args.episodes_per_config,\n            args.output_dir, args.dry_run,\n        )\n    elif args.spatial_mode == \"add_n\":\n        stats = collect_spatial_add_n(\n            policy, args.episodes_per_config,\n            args.output_dir, args.dry_run,\n        )\n    else:\n        from libero.libero import get_libero_path\n        bddl_dir = os.path.join(get_libero_path(\"bddl_files\"), BASE_TASK_SUITE)\n        tasks = find_base_tasks(bddl_dir, num_tasks=args.num_tasks)\n        if not tasks:\n            log.error(\"No base tasks found in %s\", bddl_dir)\n            sys.exit(1)\n        stats = collect_spatial(\n            policy, tasks, args.episodes_per_config,\n            args.output_dir, args.dry_run,\n        )"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "6db3be72-3b5b-41a4-9cc3-29865acf2c80",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KmxFwmLS4sJYQqFjoa8rmv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 522,
      "cache_read_input_tokens": 46593,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 522
      },
      "output_tokens": 5,
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

_source line 116 · 2026-05-15T17:52:29.784Z_

<details><summary>↩ Tool result · `toolu_01E66bPgEjvwTQF1QjNpeyLb`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "8794d27d-f89b-4098-bda2-d14d90cf1296",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py",
    "oldString": "    log.info(\n        \"Config: type=%s device=%s num_tasks=%d eps_per_cfg=%d dry_run=%s\",\n        args.perturbation_type, device, args.num_tasks,\n        args.episodes_per_config, args.dry_run,\n    )\n\n    log.info(\"Loading π₀ from %s\", args.checkpoint)\n    policy = load_pi0_policy(args.checkpoint, device)\n\n    from libero.libero import get_libero_path\n    bddl_dir = os.path.join(get_libero_path(\"bddl_files\"), BASE_TASK_SUITE)\n    tasks = find_base_tasks(bddl_dir, num_tasks=args.num_tasks)\n\n    if not tasks:\n        log.error(\"No base tasks found in %s\", bddl_dir)\n        sys.exit(1)\n\n    t0 = time.time()\n\n    if args.perturbation_type == \"physical\":\n        stats = collect_physical(\n            policy, tasks, args.episodes_per_config,\n            args.output_dir, args.dry_run,\n        )\n    else:\n        stats = collect_spatial(\n            policy, tasks, args.episodes_per_config,\n            args.output_dir, args.dry_run,\n        )",
    "newString": "    log.info(\n        \"Config: type=%s spatial_mode=%s device=%s num_tasks=%d eps_per_cfg=%d dry_run=%s\",\n        args.perturbation_type, args.spatial_mode, device, args.num_tasks,\n        args.episodes_per_config, args.dry_run,\n    )\n\n    log.info(\"Loading π₀ from %s\", args.checkpoint)\n    policy = load_pi0_policy(args.checkpoint, device)\n\n    t0 = time.time()\n\n    if args.perturbation_type == \"physical\":\n        from libero.libero import get_libero_path\n        bddl_dir = os.path.join(get_libero_path(\"bddl_files\"), BASE_TASK_SUITE)\n        tasks = find_base_tasks(bddl_dir, num_tasks=args.num_tasks)\n        if not tasks:\n            log.error(\"No base tasks found in %s\", bddl_dir)\n            sys.exit(1)\n        stats = collect_physical(\n            policy, tasks, args.episodes_per_config,\n            args.output_dir, args.dry_run,\n        )\n    elif args.spatial_mode == \"add_n\":\n        stats = collect_spatial_add_n(\n            policy, args.episodes_per_config,\n            args.output_dir, args.dry_run,\n        )\n    else:\n        from libero.libero import get_libero_path\n        bddl_dir = os.path.join(get_libero_path(\"bddl_files\"), BASE_TASK_SUITE)\n        tasks = find_base_tasks(bddl_dir, num_tasks=args.num_tasks)\n        if not tasks:\n            log.error(\"No base tasks found in %s\", bddl_dir)\n            sys.exit(1)\n        stats = collect_spatial(\n            policy, tasks, args.episodes_per_config,\n            args.output_dir, args.dry_run,\n        )",
    "originalFile": "\"\"\"\nCollect expert demonstrations by rolling out frozen π₀ in perturbed LIBERO environments.\n\nOnly successful episodes are saved. Two perturbation types are supported:\n  - physical: vary robot initial state (init_states index 1-49)\n  - spatial:  LIBERO-Plus _add_N distractor objects (default) or perturb_region fallback\n\nOutput: pickle files with (observations, actions, metadata) per episode.\n\nUsage:\n    # Physical perturbation dry-run\n    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \\\n        --perturbation_type physical --dry_run\n\n    # Spatial perturbation dry-run (uses _add_N by default)\n    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \\\n        --perturbation_type spatial --dry_run\n\n    # Spatial with legacy perturb_region mode\n    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \\\n        --perturbation_type spatial --spatial_mode perturb_region --dry_run\n\n    # Full physical collection\n    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \\\n        --perturbation_type physical\n\"\"\"\n\nimport argparse\nimport collections\nimport copy\nimport logging\nimport math\nimport os\nimport pickle\nimport random\nimport re\nimport sys\nimport time\nimport types\nfrom pathlib import Path\nfrom typing import Any\n\nimport numpy as np\nimport torch\n\nlog = logging.getLogger(__name__)\n\n# ---------------------------------------------------------------------------\n# Constants\n# ---------------------------------------------------------------------------\n\nLIBERO_DUMMY_ACTION = [0.0] * 6 + [-1.0]\nLIBERO_ENV_RESOLUTION = 256\nMODEL_INPUT_RESOLUTION = 224\nREPLAN_STEPS = 5\nNUM_STEPS_WAIT = 10\nMAX_STEPS = 220  # libero_spatial default\n\n# 10 base tasks in libero_spatial (no perturbation suffix)\nBASE_TASK_SUITE = \"libero_spatial\"\n\n# Spatial perturbation grid: 10 configurations with varying XY shifts and yaw\n# Magnitudes chosen to be noticeable but within feasible reach of the robot.\nSPATIAL_PERTURBATION_CONFIGS = [\n    {\"delta_xy\": ( 0.05,  0.00), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.0)},\n    {\"delta_xy\": (-0.05,  0.00), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.0)},\n    {\"delta_xy\": ( 0.00,  0.05), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.0)},\n    {\"delta_xy\": ( 0.00, -0.05), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.0)},\n    {\"delta_xy\": ( 0.03,  0.03), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.0)},\n    {\"delta_xy\": (-0.03, -0.03), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.0)},\n    {\"delta_xy\": ( 0.04,  0.00), \"delta_half_len\": 0.01, \"delta_yaw\": (0.3, 0.0)},\n    {\"delta_xy\": (-0.04,  0.00), \"delta_half_len\": 0.01, \"delta_yaw\": (-0.3, 0.0)},\n    {\"delta_xy\": ( 0.00,  0.04), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.3)},\n    {\"delta_xy\": ( 0.00, -0.04), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, -0.3)},\n]\n\n\n# ---------------------------------------------------------------------------\n# Geometry / image helpers (from libero_integration.py)\n# ---------------------------------------------------------------------------\n\ndef _quat2axisangle(quat: np.ndarray) -> np.ndarray:\n    \"\"\"Quaternion [x,y,z,w] -> axis-angle [ax,ay,az].\"\"\"\n    q = np.asarray(quat, dtype=np.float64)\n    norm = np.linalg.norm(q)\n    if norm < 1e-8:\n        return np.zeros(3, dtype=np.float32)\n    q /= norm\n    sin_half = np.linalg.norm(q[:3])\n    if sin_half < 1e-8:\n        return np.zeros(3, dtype=np.float32)\n    angle = 2.0 * math.atan2(sin_half, q[3])\n    axis = q[:3] / sin_half\n    return (axis * angle).astype(np.float32)\n\n\ndef _resize_with_pad(img: np.ndarray, size: int) -> np.ndarray:\n    \"\"\"Resize image with aspect-preserving padding to (size, size, 3) uint8.\"\"\"\n    try:\n        from openpi_client.image_tools import resize_with_pad, convert_to_uint8\n        return convert_to_uint8(resize_with_pad(img, size, size))\n    except ImportError:\n        from PIL import Image as PILImage\n        h, w = img.shape[:2]\n        scale = min(size / h, size / w)\n        new_h, new_w = int(h * scale), int(w * scale)\n        resized = np.array(\n            PILImage.fromarray(img).resize((new_w, new_h), PILImage.BILINEAR)\n        )\n        canvas = np.zeros((size, size, 3), dtype=np.uint8)\n        y0, x0 = (size - new_h) // 2, (size - new_w) // 2\n        canvas[y0 : y0 + new_h, x0 : x0 + new_w] = resized\n        return canvas\n\n\ndef obs_to_model_input(obs: dict, task_description: str) -> dict:\n    \"\"\"Convert LIBERO observation to the dict format expected by policy.infer().\"\"\"\n    base_img = np.ascontiguousarray(obs[\"agentview_image\"][::-1, ::-1])\n    wrist_img = np.ascontiguousarray(obs[\"robot0_eye_in_hand_image\"][::-1, ::-1])\n\n    base_img = _resize_with_pad(base_img, MODEL_INPUT_RESOLUTION)\n    wrist_img = _resize_with_pad(wrist_img, MODEL_INPUT_RESOLUTION)\n\n    state = np.concatenate([\n        obs[\"robot0_eef_pos\"].astype(np.float32),\n        _quat2axisangle(obs[\"robot0_eef_quat\"]),\n        obs[\"robot0_gripper_qpos\"].astype(np.float32),\n    ])\n\n    return {\n        \"observation/image\": base_img,\n        \"observation/wrist_image\": wrist_img,\n        \"observation/state\": state,\n        \"prompt\": task_description,\n    }\n\n\ndef extract_obs_for_saving(obs: dict) -> dict:\n    \"\"\"Extract observation fields to save in demo data (images stored as uint8).\"\"\"\n    return {\n        \"agentview_image\": obs[\"agentview_image\"].copy(),\n        \"robot0_eye_in_hand_image\": obs[\"robot0_eye_in_hand_image\"].copy(),\n        \"robot0_eef_pos\": obs[\"robot0_eef_pos\"].astype(np.float32).copy(),\n        \"robot0_eef_quat\": obs[\"robot0_eef_quat\"].astype(np.float32).copy(),\n        \"robot0_gripper_qpos\": obs[\"robot0_gripper_qpos\"].astype(np.float32).copy(),\n    }\n\n\n# ---------------------------------------------------------------------------\n# Model loading\n# ---------------------------------------------------------------------------\n\ndef _ensure_openpi_imports():\n    \"\"\"Stub out lerobot (training-only dep) before importing OpenPI.\"\"\"\n    for mod in [\n        \"lerobot\", \"lerobot.common\", \"lerobot.common.datasets\",\n        \"lerobot.common.datasets.lerobot_dataset\",\n    ]:\n        if mod not in sys.modules:\n            sys.modules[mod] = types.ModuleType(mod)\n\n\ndef load_pi0_policy(checkpoint_path: str, device: str) -> object:\n    \"\"\"Load pi0 policy via OpenPI. Returns the Policy object for inference.\"\"\"\n    _ensure_openpi_imports()\n    from openpi.training import config as _config\n    from openpi.policies import policy_config\n\n    train_config = _config.get_config(\"pi0_libero\")\n    policy = policy_config.create_trained_policy(\n        train_config, checkpoint_path, pytorch_device=device\n    )\n    log.info(\"Loaded pi0 policy on %s\", device)\n    return policy\n\n\n# ---------------------------------------------------------------------------\n# Task discovery\n# ---------------------------------------------------------------------------\n\ndef find_base_tasks(bddl_dir: str, num_tasks: int = 10) -> list[dict]:\n    \"\"\"Find base (unperturbed) BDDL files in libero_spatial.\n\n    Returns list of dicts with keys: name, bddl_path, init_states_path.\n    \"\"\"\n    all_files = [f for f in os.listdir(bddl_dir) if f.endswith(\".bddl\")]\n\n    base_names = []\n    for f in sorted(all_files):\n        name = f.replace(\".bddl\", \"\")\n        # Skip any file with perturbation suffixes\n        if re.search(\n            r\"(_add_\\d+|_table_\\d+|_tb_\\d+|_light_\\d+|_language_\\d+\"\n            r\"|_view_|_noise_|_level\\d+| copy)\",\n            name,\n        ):\n            continue\n        base_names.append(name)\n\n    init_dir = bddl_dir.replace(\"bddl_files\", \"init_files\")\n    tasks = []\n    for name in base_names[:num_tasks]:\n        bddl_path = os.path.join(bddl_dir, f\"{name}.bddl\")\n        init_path = os.path.join(init_dir, f\"{name}.pruned_init\")\n        if not os.path.exists(init_path):\n            log.warning(\"init_states not found for %s, skipping\", name)\n            continue\n        tasks.append({\n            \"name\": name,\n            \"bddl_path\": bddl_path,\n            \"init_states_path\": init_path,\n        })\n\n    log.info(\"Found %d base tasks\", len(tasks))\n    return tasks\n\n\ndef get_task_language(bddl_path: str) -> str:\n    \"\"\"Extract language instruction from a BDDL file.\"\"\"\n    from libero.libero.envs.bddl_utils import get_problem_info\n    info = get_problem_info(bddl_path)\n    return info[\"language_instruction\"]\n\n\ndef discover_add_n_tasks(task_suite: str = BASE_TASK_SUITE) -> list[dict]:\n    \"\"\"Discover all _add_N (distractor-object) tasks from the LIBERO-Plus benchmark.\n\n    Returns list of dicts with: idx, name, language, bddl_path, init_states.\n    \"\"\"\n    from libero.libero import benchmark, get_libero_path\n    benchmark_dict = benchmark.get_benchmark_dict()\n    suite = benchmark_dict[task_suite]()\n    bddl_root = Path(get_libero_path(\"bddl_files\"))\n\n    tasks = []\n    skipped = 0\n    for i in range(suite.n_tasks):\n        task = suite.get_task(i)\n        name = getattr(task, \"name\", \"\") or getattr(task, \"bddl_file\", \"\")\n        if not re.search(r\"_add_\\d+$\", name.replace(\".bddl\", \"\")):\n            continue\n\n        bddl_path = str(bddl_root / task.problem_folder / task.bddl_file)\n        if not os.path.exists(bddl_path):\n            log.warning(\"BDDL not found, skipping: %s\", bddl_path)\n            skipped += 1\n            continue\n\n        try:\n            init_states = suite.get_task_init_states(i)\n        except Exception:\n            log.warning(\"init_states failed for %s, skipping\", name)\n            skipped += 1\n            continue\n\n        tasks.append({\n            \"idx\": i,\n            \"name\": name.replace(\".bddl\", \"\"),\n            \"language\": task.language,\n            \"bddl_path\": bddl_path,\n            \"init_states\": init_states,\n        })\n\n    log.info(\n        \"Discovered %d _add_N tasks (%d skipped) from %s\",\n        len(tasks), skipped, task_suite,\n    )\n    return tasks\n\n\n# ---------------------------------------------------------------------------\n# Environment creation\n# ---------------------------------------------------------------------------\n\ndef create_env(bddl_path: str) -> object:\n    \"\"\"Create a LIBERO OffScreenRenderEnv from a BDDL file.\"\"\"\n    from libero.libero.envs import OffScreenRenderEnv\n    env = OffScreenRenderEnv(\n        bddl_file_name=bddl_path,\n        camera_heights=LIBERO_ENV_RESOLUTION,\n        camera_widths=LIBERO_ENV_RESOLUTION,\n    )\n    return env\n\n\ndef create_spatial_bddl(\n    base_bddl_path: str,\n    perturbation_config: dict,\n    output_dir: str,\n) -> str:\n    \"\"\"Create a perturbed BDDL file by applying spatial perturbation to all regions.\n\n    Returns the path to the new BDDL file.\n    \"\"\"\n    sys.path.insert(0, \"/root/LIBERO-plus/libero\")\n    from libero.randomizer.bddl_operators import (\n        load_bddl_file,\n        save_bddl_file,\n        perturb_region_info,\n    )\n\n    spec = load_bddl_file(base_bddl_path)\n    delta_xy = perturbation_config[\"delta_xy\"]\n    delta_half = perturbation_config[\"delta_half_len\"]\n    delta_yaw = perturbation_config[\"delta_yaw\"]\n\n    for i in range(len(spec.region_infos)):\n        spec.region_infos[i] = perturb_region_info(\n            spec.region_infos[i],\n            delta_region_centroid_xy=delta_xy,\n            delta_region_half_len=delta_half,\n            delta_yaw_rotation=delta_yaw,\n        )\n\n    os.makedirs(output_dir, exist_ok=True)\n    base_name = Path(base_bddl_path).stem\n    dx, dy = delta_xy\n    filename = f\"{base_name}_spatial_dx{dx:.2f}_dy{dy:.2f}.bddl\"\n    _, filepath = save_bddl_file(spec, bddl_filename=filename, bddl_dirpath=output_dir)\n    return filepath\n\n\n# ---------------------------------------------------------------------------\n# Episode rollout\n# ---------------------------------------------------------------------------\n\ndef rollout_episode(\n    policy: object,\n    env: object,\n    task_description: str,\n    init_states: np.ndarray,\n    init_state_idx: int,\n    seed: int,\n) -> dict[str, Any]:\n    \"\"\"Run one episode, collecting (obs, action) pairs.\n\n    Returns dict with observations, actions, success, num_steps.\n    \"\"\"\n    env.seed(seed)\n    obs = env.set_init_state(init_states[init_state_idx])\n\n    for _ in range(NUM_STEPS_WAIT):\n        obs, _, _, _ = env.step(LIBERO_DUMMY_ACTION)\n\n    all_obs = [extract_obs_for_saving(obs)]\n    all_actions = []\n    action_plan = collections.deque()\n    step = 0\n    success = False\n    done = False\n\n    while not done and step < MAX_STEPS:\n        if len(action_plan) == 0:\n            obs_dict = obs_to_model_input(obs, task_description)\n            result = policy.infer(obs_dict)\n            action_chunk = result[\"actions\"]\n            action_plan.extend(action_chunk[:REPLAN_STEPS])\n\n        action = action_plan.popleft()\n        if isinstance(action, torch.Tensor):\n            action = action.cpu().numpy()\n        action_np = np.asarray(action, dtype=np.float32)\n\n        obs, reward, done, info = env.step(\n            action_np.tolist() if hasattr(action_np, \"tolist\") else list(action_np)\n        )\n        step += 1\n\n        all_obs.append(extract_obs_for_saving(obs))\n        all_actions.append(action_np)\n\n        if done or reward > 0:\n            success = info.get(\"success\", reward > 0)\n\n    return {\n        \"observations\": all_obs,\n        \"actions\": np.stack(all_actions) if all_actions else np.zeros((0, 7)),\n        \"success\": success,\n        \"num_steps\": step,\n    }\n\n\n# ---------------------------------------------------------------------------\n# Collection loops\n# ---------------------------------------------------------------------------\n\ndef collect_physical(\n    policy: object,\n    tasks: list[dict],\n    episodes_per_config: int,\n    output_dir: str,\n    dry_run: bool,\n) -> dict:\n    \"\"\"Collect expert demos with physical (robot initial state) perturbation.\n\n    Uses init_states indices 1-49 (index 0 is nominal).\n    \"\"\"\n    os.makedirs(output_dir, exist_ok=True)\n    stats = {\"total\": 0, \"success\": 0, \"saved_files\": []}\n\n    init_state_indices = list(range(1, 50))  # 49 perturbed states\n    if dry_run:\n        tasks = tasks[:1]\n        init_state_indices = [1]\n        episodes_per_config = 1\n\n    for task_info in tasks:\n        task_name = task_info[\"name\"]\n        init_states = torch.load(task_info[\"init_states_path\"], weights_only=False)\n        language = get_task_language(task_info[\"bddl_path\"])\n        log.info(\"Task: %s (%d init_states available)\", task_name, len(init_states))\n\n        for idx in init_state_indices:\n            if idx >= len(init_states):\n                continue\n\n            for ep in range(episodes_per_config):\n                seed = hash((task_name, idx, ep)) % (2**31)\n                stats[\"total\"] += 1\n\n                try:\n                    env = create_env(task_info[\"bddl_path\"])\n                    result = rollout_episode(\n                        policy, env, language, init_states, idx, seed\n                    )\n                    env.close()\n                except Exception:\n                    log.exception(\n                        \"Episode failed: task=%s idx=%d ep=%d\", task_name, idx, ep\n                    )\n                    continue\n\n                if result[\"success\"]:\n                    stats[\"success\"] += 1\n                    demo = {\n                        \"observations\": result[\"observations\"],\n                        \"actions\": result[\"actions\"],\n                        \"task_name\": task_name,\n                        \"perturbation_config\": {\n                            \"type\": \"physical\",\n                            \"init_state_idx\": idx,\n                        },\n                        \"success\": True,\n                        \"num_steps\": result[\"num_steps\"],\n                    }\n                    fname = f\"{task_name}_initstate{idx}_ep{ep}.pkl\"\n                    fpath = os.path.join(output_dir, fname)\n                    with open(fpath, \"wb\") as f:\n                        pickle.dump(demo, f, protocol=pickle.HIGHEST_PROTOCOL)\n                    stats[\"saved_files\"].append(fpath)\n\n                rate = stats[\"success\"] / stats[\"total\"] * 100\n                log.info(\n                    \"[physical] task=%s idx=%d ep=%d | %s | \"\n                    \"cumulative %d/%d (%.1f%%)\",\n                    task_name, idx, ep,\n                    \"SUCCESS\" if result[\"success\"] else \"FAIL\",\n                    stats[\"success\"], stats[\"total\"], rate,\n                )\n\n    return stats\n\n\ndef collect_spatial(\n    policy: object,\n    tasks: list[dict],\n    episodes_per_config: int,\n    output_dir: str,\n    dry_run: bool,\n) -> dict:\n    \"\"\"Collect expert demos with spatial (objects layout) perturbation.\n\n    Applies 10 predefined spatial perturbation configs to each base task.\n    \"\"\"\n    os.makedirs(output_dir, exist_ok=True)\n    tmp_bddl_dir = os.path.join(output_dir, \"_tmp_bddl\")\n    os.makedirs(tmp_bddl_dir, exist_ok=True)\n    stats = {\"total\": 0, \"success\": 0, \"saved_files\": []}\n\n    configs = SPATIAL_PERTURBATION_CONFIGS\n    if dry_run:\n        tasks = tasks[:1]\n        configs = configs[:1]\n        episodes_per_config = 1\n\n    for task_info in tasks:\n        task_name = task_info[\"name\"]\n        init_states = torch.load(task_info[\"init_states_path\"], weights_only=False)\n        log.info(\"Task: %s\", task_name)\n\n        for cfg_idx, cfg in enumerate(configs):\n            try:\n                perturbed_bddl = create_spatial_bddl(\n                    task_info[\"bddl_path\"], cfg, tmp_bddl_dir\n                )\n                language = get_task_language(perturbed_bddl)\n            except Exception:\n                log.exception(\n                    \"BDDL perturbation failed: task=%s cfg=%d\", task_name, cfg_idx\n                )\n                continue\n\n            for ep in range(episodes_per_config):\n                seed = hash((task_name, cfg_idx, ep)) % (2**31)\n                stats[\"total\"] += 1\n\n                try:\n                    env = create_env(perturbed_bddl)\n                    # Use nominal init_state (index 0) for spatial perturbation\n                    result = rollout_episode(\n                        policy, env, language, init_states, 0, seed\n                    )\n                    env.close()\n                except Exception:\n                    log.exception(\n                        \"Episode failed: task=%s cfg=%d ep=%d\",\n                        task_name, cfg_idx, ep,\n                    )\n                    continue\n\n                if result[\"success\"]:\n                    stats[\"success\"] += 1\n                    demo = {\n                        \"observations\": result[\"observations\"],\n                        \"actions\": result[\"actions\"],\n                        \"task_name\": task_name,\n                        \"perturbation_config\": {\n                            \"type\": \"spatial\",\n                            \"config_idx\": cfg_idx,\n                            \"delta_xy\": cfg[\"delta_xy\"],\n                            \"delta_half_len\": cfg[\"delta_half_len\"],\n                            \"delta_yaw\": cfg[\"delta_yaw\"],\n                        },\n                        \"success\": True,\n                        \"num_steps\": result[\"num_steps\"],\n                    }\n                    fname = f\"{task_name}_spatial{cfg_idx}_ep{ep}.pkl\"\n                    fpath = os.path.join(output_dir, fname)\n                    with open(fpath, \"wb\") as f:\n                        pickle.dump(demo, f, protocol=pickle.HIGHEST_PROTOCOL)\n                    stats[\"saved_files\"].append(fpath)\n\n                rate = stats[\"success\"] / stats[\"total\"] * 100\n                log.info(\n                    \"[spatial] task=%s cfg=%d ep=%d | %s | \"\n                    \"cumulative %d/%d (%.1f%%)\",\n                    task_name, cfg_idx, ep,\n                    \"SUCCESS\" if result[\"success\"] else \"FAIL\",\n                    stats[\"success\"], stats[\"total\"], rate,\n                )\n\n    return stats\n\n\ndef collect_spatial_add_n(\n    policy: object,\n    episodes_per_task: int,\n    output_dir: str,\n    dry_run: bool,\n) -> dict:\n    \"\"\"Collect expert demos using LIBERO-Plus _add_N distractor-object tasks.\n\n    Each _add_N task is a pre-built BDDL with extra objects in the scene.\n    208 tasks × 3 episodes = 624 rollouts.\n    \"\"\"\n    os.makedirs(output_dir, exist_ok=True)\n    stats = {\"total\": 0, \"success\": 0, \"saved_files\": [], \"load_errors\": 0}\n\n    add_tasks = discover_add_n_tasks()\n    if not add_tasks:\n        log.error(\"No _add_N tasks found. Check LIBERO-Plus installation.\")\n        return stats\n\n    if dry_run:\n        add_tasks = add_tasks[:2]\n        episodes_per_task = 1\n\n    log.info(\n        \"Collecting spatial (_add_N): %d tasks × %d eps = %d rollouts\",\n        len(add_tasks), episodes_per_task, len(add_tasks) * episodes_per_task,\n    )\n\n    for task_info in add_tasks:\n        task_name = task_info[\"name\"]\n        language = task_info[\"language\"]\n        init_states = task_info[\"init_states\"]\n\n        for ep in range(episodes_per_task):\n            seed = hash((task_name, ep)) % (2**31)\n            stats[\"total\"] += 1\n\n            try:\n                env = create_env(task_info[\"bddl_path\"])\n                init_idx = ep % len(init_states)\n                result = rollout_episode(\n                    policy, env, language, init_states, init_idx, seed\n                )\n                env.close()\n            except FileNotFoundError as e:\n                stats[\"load_errors\"] += 1\n                log.warning(\"Asset missing for %s: %s\", task_name, e)\n                continue\n            except Exception:\n                log.exception(\"Episode failed: task=%s ep=%d\", task_name, ep)\n                continue\n\n            if result[\"success\"]:\n                stats[\"success\"] += 1\n                demo = {\n                    \"observations\": result[\"observations\"],\n                    \"actions\": result[\"actions\"],\n                    \"task_name\": task_name,\n                    \"perturbation_config\": {\n                        \"type\": \"spatial_add_n\",\n                        \"source_task_idx\": task_info[\"idx\"],\n                    },\n                    \"success\": True,\n                    \"num_steps\": result[\"num_steps\"],\n                }\n                fname = f\"{task_name}_ep{ep}.pkl\"\n                fpath = os.path.join(output_dir, fname)\n                with open(fpath, \"wb\") as f:\n                    pickle.dump(demo, f, protocol=pickle.HIGHEST_PROTOCOL)\n                stats[\"saved_files\"].append(fpath)\n\n            rate = stats[\"success\"] / stats[\"total\"] * 100\n            log.info(\n                \"[spatial_add_n] task=%s ep=%d | %s | cumulative %d/%d (%.1f%%) | load_errors=%d\",\n                task_name, ep,\n                \"SUCCESS\" if result[\"success\"] else \"FAIL\",\n                stats[\"success\"], stats[\"total\"], rate,\n                stats[\"load_errors\"],\n            )\n\n    return stats\n\n\n# ---------------------------------------------------------------------------\n# Main\n# ---------------------------------------------------------------------------\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Collect expert demos from π₀ in perturbed LIBERO environments\"\n    )\n    parser.add_argument(\n        \"--perturbation_type\", type=str, required=True,\n        choices=[\"physical\", \"spatial\"],\n    )\n    parser.add_argument(\n        \"--spatial_mode\", type=str, default=\"add_n\",\n        choices=[\"add_n\", \"perturb_region\"],\n        help=\"Spatial perturbation mode: add_n (LIBERO-Plus distractors, default) \"\n             \"or perturb_region (legacy BDDL region shifts)\",\n    )\n    parser.add_argument(\"--gpu_id\", type=int, default=0)\n    parser.add_argument(\"--num_tasks\", type=int, default=10)\n    parser.add_argument(\"--episodes_per_config\", type=int, default=3)\n    parser.add_argument(\n        \"--output_dir\", type=str, default=None,\n        help=\"Override output directory (default: auto from perturbation_type)\",\n    )\n    parser.add_argument(\n        \"--checkpoint\", type=str,\n        default=\"/root/autodl-tmp/checkpoints/pi0_base\",\n    )\n    parser.add_argument(\"--dry_run\", action=\"store_true\")\n    parser.add_argument(\"--seed\", type=int, default=42)\n    args = parser.parse_args()\n\n    logging.basicConfig(\n        level=logging.INFO,\n        format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    )\n\n    random.seed(args.seed)\n    np.random.seed(args.seed)\n    torch.manual_seed(args.seed)\n\n    if args.output_dir is None:\n        args.output_dir = (\n            f\"/root/meta_brain_lora_routing/data/expert_demos/{args.perturbation_type}\"\n        )\n\n    device = f\"cuda:{args.gpu_id}\"\n    log.info(\n        \"Config: type=%s device=%s num_tasks=%d eps_per_cfg=%d dry_run=%s\",\n        args.perturbation_type, device, args.num_tasks,\n        args.episodes_per_config, args.dry_run,\n    )\n\n    log.info(\"Loading π₀ from %s\", args.checkpoint)\n    policy = load_pi0_policy(args.checkpoint, device)\n\n    from libero.libero import get_libero_path\n    bddl_dir = os.path.join(get_libero_path(\"bddl_files\"), BASE_TASK_SUITE)\n    tasks = find_base_tasks(bddl_dir, num_tasks=args.num_tasks)\n\n    if not tasks:\n        log.error(\"No base tasks found in %s\", bddl_dir)\n        sys.exit(1)\n\n    t0 = time.time()\n\n    if args.perturbation_type == \"physical\":\n        stats = collect_physical(\n            policy, tasks, args.episodes_per_config,\n            args.output_dir, args.dry_run,\n        )\n    else:\n        stats = collect_spatial(\n            policy, tasks, args.episodes_per_config,\n            args.output_dir, args.dry_run,\n        )\n\n    elapsed = time.time() - t0\n\n    total_size = sum(\n        os.path.getsize(f) for f in stats[\"saved_files\"] if os.path.exists(f)\n    )\n    log.info(\"=\" * 60)\n    log.info(\"Collection complete: %s\", args.perturbation_type)\n    log.info(\"  Total episodes:  %d\", stats[\"total\"])\n    log.info(\"  Successful:      %d\", stats[\"success\"])\n    log.info(\n        \"  Success rate:    %.1f%%\",\n        stats[\"success\"] / max(stats[\"total\"], 1) * 100,\n    )\n    log.info(\"  Files saved:     %d\", len(stats[\"saved_files\"]))\n    log.info(\"  Total size:      %.1f MB\", total_size / 1024 / 1024)\n    log.info(\"  Elapsed:         %.1f min\", elapsed / 60)\n    log.info(\"  Output dir:      %s\", args.output_dir)\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 684,
        "oldLines": 30,
        "newStart": 684,
        "newLines": 39,
        "lines": [
          " ",
          "     device = f\"cuda:{args.gpu_id}\"",
          "     log.info(",
          "-        \"Config: type=%s device=%s num_tasks=%d eps_per_cfg=%d dry_run=%s\",",
          "-        args.perturbation_type, device, args.num_tasks,",
          "+        \"Config: type=%s spatial_mode=%s device=%s num_tasks=%d eps_per_cfg=%d dry_run=%s\",",
          "+        args.perturbation_type, args.spatial_mode, device, args.num_tasks,",
          "         args.episodes_per_config, args.dry_run,",
          "     )",
          " ",
          "     log.info(\"Loading π₀ from %s\", args.checkpoint)",
          "     policy = load_pi0_policy(args.checkpoint, device)",
          " ",
          "-    from libero.libero import get_libero_path",
          "-    bddl_dir = os.path.join(get_libero_path(\"bddl_files\"), BASE_TASK_SUITE)",
          "-    tasks = find_base_tasks(bddl_dir, num_tasks=args.num_tasks)",
          "-",
          "-    if not tasks:",
          "-        log.error(\"No base tasks found in %s\", bddl_dir)",
          "-        sys.exit(1)",
          "-",
          "     t0 = time.time()",
          " ",
          "     if args.perturbation_type == \"physical\":",
          "+        from libero.libero import get_libero_path",
          "+        bddl_dir = os.path.join(get_libero_path(\"bddl_files\"), BASE_TASK_SUITE)",
          "+        tasks = find_base_tasks(bddl_dir, num_tasks=args.num_tasks)",
          "+        if not tasks:",
          "+            log.error(\"No base tasks found in %s\", bddl_dir)",
          "+            sys.exit(1)",
          "         stats = collect_physical(",
          "             policy, tasks, args.episodes_per_config,",
          "             args.output_dir, args.dry_run,",
          "         )",
          "+    elif args.spatial_mode == \"add_n\":",
          "+        stats = collect_spatial_add_n(",
          "+            policy, args.episodes_per_config,",
          "+            args.output_dir, args.dry_run,",
          "+        )",
          "     else:",
          "+        from libero.libero import get_libero_path",
          "+        bddl_dir = os.path.join(get_libero_path(\"bddl_files\"), BASE_TASK_SUITE)",
          "+        tasks = find_base_tasks(bddl_dir, num_tasks=args.num_tasks)",
          "+        if not tasks:",
          "+            log.error(\"No base tasks found in %s\", bddl_dir)",
          "+            sys.exit(1)",
          "         stats = collect_spatial(",
          "             policy, tasks, args.episodes_per_config,",
          "             args.output_dir, args.dry_run,"
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

_source line 117_

Let me verify the final file looks correct:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "3220fc8f-ba77-4e23-a56d-d81346a9ee28",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SQzSnkBrSKKWnchKPstCDg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1043,
      "cache_read_input_tokens": 47115,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1043
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

_source line 118_

<details open><summary>🔧 Tool call — Read · `toolu_01MHHG8aWoanLU3yL2Jyr9Qx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "f341ac5d-3009-4d23-9755-4c86011dda50",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SQzSnkBrSKKWnchKPstCDg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1043,
      "cache_read_input_tokens": 47115,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1043
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

_source line 119 · 2026-05-15T17:52:32.904Z_

<details><summary>↩ Tool result · `toolu_01MHHG8aWoanLU3yL2Jyr9Qx`</summary>

```text
1	"""
2	Collect expert demonstrations by rolling out frozen π₀ in perturbed LIBERO environments.
3	
4	Only successful episodes are saved. Two perturbation types are supported:
5	  - physical: vary robot initial state (init_states index 1-49)
6	  - spatial:  LIBERO-Plus _add_N distractor objects (default) or perturb_region fallback
7	
8	Output: pickle files with (observations, actions, metadata) per episode.
9	
10	Usage:
11	    # Physical perturbation dry-run
12	    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \
13	        --perturbation_type physical --dry_run
14	
15	    # Spatial perturbation dry-run (uses _add_N by default)
16	    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \
17	        --perturbation_type spatial --dry_run
18	
19	    # Spatial with legacy perturb_region mode
20	    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \
21	        --perturbation_type spatial --spatial_mode perturb_region --dry_run
22	
23	    # Full physical collection
24	    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \
25	        --perturbation_type physical
26	"""
27	
28	import argparse
29	import collections
30	import copy
31	import logging
32	import math
33	import os
34	import pickle
35	import random
36	import re
37	import sys
38	import time
39	import types
40	from pathlib import Path
41	from typing import Any
42	
43	import numpy as np
44	import torch
45	
46	log = logging.getLogger(__name__)
47	
48	# ---------------------------------------------------------------------------
49	# Constants
50	# ---------------------------------------------------------------------------
51	
52	LIBERO_DUMMY_ACTION = [0.0] * 6 + [-1.0]
53	LIBERO_ENV_RESOLUTION = 256
54	MODEL_INPUT_RESOLUTION = 224
55	REPLAN_STEPS = 5
56	NUM_STEPS_WAIT = 10
57	MAX_STEPS = 220  # libero_spatial default
58	
59	# 10 base tasks in libero_spatial (no perturbation suffix)
60	BASE_TASK_SUITE = "libero_spatial"
61	
62	# Spatial perturbation grid: 10 configurations with varying XY shifts and yaw
63	# Magnitudes chosen to be noticeable but within feasible reach of the robot.
64	SPATIAL_PERTURBATION_CONFIGS = [
65	    {"delta_xy": ( 0.05,  0.00), "delta_half_len": 0.0,  "delta_yaw": (0.0, 0.0)},
66	    {"delta_xy": (-0.05,  0.00), "delta_half_len": 0.0,  "delta_yaw": (0.0, 0.0)},
67	    {"delta_xy": ( 0.00,  0.05), "delta_half_len": 0.0,  "delta_yaw": (0.0, 0.0)},
68	    {"delta_xy": ( 0.00, -0.05), "delta_half_len": 0.0,  "delta_yaw": (0.0, 0.0)},
69	    {"delta_xy": ( 0.03,  0.03), "delta_half_len": 0.0,  "delta_yaw": (0.0, 0.0)},
70	    {"delta_xy": (-0.03, -0.03), "delta_half_len": 0.0,  "delta_yaw": (0.0, 0.0)},
71	    {"delta_xy": ( 0.04,  0.00), "delta_half_len": 0.01, "delta_yaw": (0.3, 0.0)},
72	    {"delta_xy": (-0.04,  0.00), "delta_half_len": 0.01, "delta_yaw": (-0.3, 0.0)},
73	    {"delta_xy": ( 0.00,  0.04), "delta_half_len": 0.0,  "delta_yaw": (0.0, 0.3)},
74	    {"delta_xy": ( 0.00, -0.04), "delta_half_len": 0.0,  "delta_yaw": (0.0, -0.3)},
75	]
76	
77	
78	# ---------------------------------------------------------------------------
79	# Geometry / image helpers (from libero_integration.py)
80	# ---------------------------------------------------------------------------
81	
82	def _quat2axisangle(quat: np.ndarray) -> np.ndarray:
83	    """Quaternion [x,y,z,w] -> axis-angle [ax,ay,az]."""
84	    q = np.asarray(quat, dtype=np.float64)
85	    norm = np.linalg.norm(q)
86	    if norm < 1e-8:
87	        return np.zeros(3, dtype=np.float32)
88	    q /= norm
89	    sin_half = np.linalg.norm(q[:3])
90	    if sin_half < 1e-8:
91	        return np.zeros(3, dtype=np.float32)
92	    angle = 2.0 * math.atan2(sin_half, q[3])
93	    axis = q[:3] / sin_half
94	    return (axis * angle).astype(np.float32)
95	
96	
97	def _resize_with_pad(img: np.ndarray, size: int) -> np.ndarray:
98	    """Resize image with aspect-preserving padding to (size, size, 3) uint8."""
99	    try:
100	        from openpi_client.image_tools import resize_with_pad, convert_to_uint8
101	        return convert_to_uint8(resize_with_pad(img, size, size))
102	    except ImportError:
103	        from PIL import Image as PILImage
104	        h, w = img.shape[:2]
105	        scale = min(size / h, size / w)
106	        new_h, new_w = int(h * scale), int(w * scale)
107	        resized = np.array(
108	            PILImage.fromarray(img).resize((new_w, new_h), PILImage.BILINEAR)
109	        )
110	        canvas = np.zeros((size, size, 3), dtype=np.uint8)
111	        y0, x0 = (size - new_h) // 2, (size - new_w) // 2
112	        canvas[y0 : y0 + new_h, x0 : x0 + new_w] = resized
113	        return canvas
114	
115	
116	def obs_to_model_input(obs: dict, task_description: str) -> dict:
117	    """Convert LIBERO observation to the dict format expected by policy.infer()."""
118	    base_img = np.ascontiguousarray(obs["agentview_image"][::-1, ::-1])
119	    wrist_img = np.ascontiguousarray(obs["robot0_eye_in_hand_image"][::-1, ::-1])
120	
121	    base_img = _resize_with_pad(base_img, MODEL_INPUT_RESOLUTION)
122	    wrist_img = _resize_with_pad(wrist_img, MODEL_INPUT_RESOLUTION)
123	
124	    state = np.concatenate([
125	        obs["robot0_eef_pos"].astype(np.float32),
126	        _quat2axisangle(obs["robot0_eef_quat"]),
127	        obs["robot0_gripper_qpos"].astype(np.float32),
128	    ])
129	
130	    return {
131	        "observation/image": base_img,
132	        "observation/wrist_image": wrist_img,
133	        "observation/state": state,
134	        "prompt": task_description,
135	    }
136	
137	
138	def extract_obs_for_saving(obs: dict) -> dict:
139	    """Extract observation fields to save in demo data (images stored as uint8)."""
140	    return {
141	        "agentview_image": obs["agentview_image"].copy(),
142	        "robot0_eye_in_hand_image": obs["robot0_eye_in_hand_image"].copy(),
143	        "robot0_eef_pos": obs["robot0_eef_pos"].astype(np.float32).copy(),
144	        "robot0_eef_quat": obs["robot0_eef_quat"].astype(np.float32).copy(),
145	        "robot0_gripper_qpos": obs["robot0_gripper_qpos"].astype(np.float32).copy(),
146	    }
147	
148	
149	# ---------------------------------------------------------------------------
150	# Model loading
151	# ---------------------------------------------------------------------------
152	
153	def _ensure_openpi_imports():
154	    """Stub out lerobot (training-only dep) before importing OpenPI."""
155	    for mod in [
156	        "lerobot", "lerobot.common", "lerobot.common.datasets",
157	        "lerobot.common.datasets.lerobot_dataset",
158	    ]:
159	        if mod not in sys.modules:
160	            sys.modules[mod] = types.ModuleType(mod)
161	
162	
163	def load_pi0_policy(checkpoint_path: str, device: str) -> object:
164	    """Load pi0 policy via OpenPI. Returns the Policy object for inference."""
165	    _ensure_openpi_imports()
166	    from openpi.training import config as _config
167	    from openpi.policies import policy_config
168	
169	    train_config = _config.get_config("pi0_libero")
170	    policy = policy_config.create_trained_policy(
171	        train_config, checkpoint_path, pytorch_device=device
172	    )
173	    log.info("Loaded pi0 policy on %s", device)
174	    return policy
175	
176	
177	# ---------------------------------------------------------------------------
178	# Task discovery
179	# ---------------------------------------------------------------------------
180	
181	def find_base_tasks(bddl_dir: str, num_tasks: int = 10) -> list[dict]:
182	    """Find base (unperturbed) BDDL files in libero_spatial.
183	
184	    Returns list of dicts with keys: name, bddl_path, init_states_path.
185	    """
186	    all_files = [f for f in os.listdir(bddl_dir) if f.endswith(".bddl")]
187	
188	    base_names = []
189	    for f in sorted(all_files):
190	        name = f.replace(".bddl", "")
191	        # Skip any file with perturbation suffixes
192	        if re.search(
193	            r"(_add_\d+|_table_\d+|_tb_\d+|_light_\d+|_language_\d+"
194	            r"|_view_|_noise_|_level\d+| copy)",
195	            name,
196	        ):
197	            continue
198	        base_names.append(name)
199	
200	    init_dir = bddl_dir.replace("bddl_files", "init_files")
201	    tasks = []
202	    for name in base_names[:num_tasks]:
203	        bddl_path = os.path.join(bddl_dir, f"{name}.bddl")
204	        init_path = os.path.join(init_dir, f"{name}.pruned_init")
205	        if not os.path.exists(init_path):
206	            log.warning("init_states not found for %s, skipping", name)
207	            continue
208	        tasks.append({
209	            "name": name,
210	            "bddl_path": bddl_path,
211	            "init_states_path": init_path,
212	        })
213	
214	    log.info("Found %d base tasks", len(tasks))
215	    return tasks
216	
217	
218	def get_task_language(bddl_path: str) -> str:
219	    """Extract language instruction from a BDDL file."""
220	    from libero.libero.envs.bddl_utils import get_problem_info
221	    info = get_problem_info(bddl_path)
222	    return info["language_instruction"]
223	
224	
225	def discover_add_n_tasks(task_suite: str = BASE_TASK_SUITE) -> list[dict]:
226	    """Discover all _add_N (distractor-object) tasks from the LIBERO-Plus benchmark.
227	
228	    Returns list of dicts with: idx, name, language, bddl_path, init_states.
229	    """
230	    from libero.libero import benchmark, get_libero_path
231	    benchmark_dict = benchmark.get_benchmark_dict()
232	    suite = benchmark_dict[task_suite]()
233	    bddl_root = Path(get_libero_path("bddl_files"))
234	
235	    tasks = []
236	    skipped = 0
237	    for i in range(suite.n_tasks):
238	        task = suite.get_task(i)
239	        name = getattr(task, "name", "") or getattr(task, "bddl_file", "")
240	        if not re.search(r"_add_\d+$", name.replace(".bddl", "")):
241	            continue
242	
243	        bddl_path = str(bddl_root / task.problem_folder / task.bddl_file)
244	        if not os.path.exists(bddl_path):
245	            log.warning("BDDL not found, skipping: %s", bddl_path)
246	            skipped += 1
247	            continue
248	
249	        try:
250	            init_states = suite.get_task_init_states(i)
251	        except Exception:
252	            log.warning("init_states failed for %s, skipping", name)
253	            skipped += 1
254	            continue
255	
256	        tasks.append({
257	            "idx": i,
258	            "name": name.replace(".bddl", ""),
259	            "language": task.language,
260	            "bddl_path": bddl_path,
261	            "init_states": init_states,
262	        })
263	
264	    log.info(
265	        "Discovered %d _add_N tasks (%d skipped) from %s",
266	        len(tasks), skipped, task_suite,
267	    )
268	    return tasks
269	
270	
271	# ---------------------------------------------------------------------------
272	# Environment creation
273	# ---------------------------------------------------------------------------
274	
275	def create_env(bddl_path: str) -> object:
276	    """Create a LIBERO OffScreenRenderEnv from a BDDL file."""
277	    from libero.libero.envs import OffScreenRenderEnv
278	    env = OffScreenRenderEnv(
279	        bddl_file_name=bddl_path,
280	        camera_heights=LIBERO_ENV_RESOLUTION,
281	        camera_widths=LIBERO_ENV_RESOLUTION,
282	    )
283	    return env
284	
285	
286	def create_spatial_bddl(
287	    base_bddl_path: str,
288	    perturbation_config: dict,
289	    output_dir: str,
290	) -> str:
291	    """Create a perturbed BDDL file by applying spatial perturbation to all regions.
292	
293	    Returns the path to the new BDDL file.
294	    """
295	    sys.path.insert(0, "/root/LIBERO-plus/libero")
296	    from libero.randomizer.bddl_operators import (
297	        load_bddl_file,
298	        save_bddl_file,
299	        perturb_region_info,
300	    )
301	
302	    spec = load_bddl_file(base_bddl_path)
303	    delta_xy = perturbation_config["delta_xy"]
304	    delta_half = perturbation_config["delta_half_len"]
305	    delta_yaw = perturbation_config["delta_yaw"]
306	
307	    for i in range(len(spec.region_infos)):
308	        spec.region_infos[i] = perturb_region_info(
309	            spec.region_infos[i],
310	            delta_region_centroid_xy=delta_xy,
311	            delta_region_half_len=delta_half,
312	            delta_yaw_rotation=delta_yaw,
313	        )
314	
315	    os.makedirs(output_dir, exist_ok=True)
316	    base_name = Path(base_bddl_path).stem
317	    dx, dy = delta_xy
318	    filename = f"{base_name}_spatial_dx{dx:.2f}_dy{dy:.2f}.bddl"
319	    _, filepath = save_bddl_file(spec, bddl_filename=filename, bddl_dirpath=output_dir)
320	    return filepath
321	
322	
323	# ---------------------------------------------------------------------------
324	# Episode rollout
325	# ---------------------------------------------------------------------------
326	
327	def rollout_episode(
328	    policy: object,
329	    env: object,
330	    task_description: str,
331	    init_states: np.ndarray,
332	    init_state_idx: int,
333	    seed: int,
334	) -> dict[str, Any]:
335	    """Run one episode, collecting (obs, action) pairs.
336	
337	    Returns dict with observations, actions, success, num_steps.
338	    """
339	    env.seed(seed)
340	    obs = env.set_init_state(init_states[init_state_idx])
341	
342	    for _ in range(NUM_STEPS_WAIT):
343	        obs, _, _, _ = env.step(LIBERO_DUMMY_ACTION)
344	
345	    all_obs = [extract_obs_for_saving(obs)]
346	    all_actions = []
347	    action_plan = collections.deque()
348	    step = 0
349	    success = False
350	    done = False
351	
352	    while not done and step < MAX_STEPS:
353	        if len(action_plan) == 0:
354	            obs_dict = obs_to_model_input(obs, task_description)
355	            result = policy.infer(obs_dict)
356	            action_chunk = result["actions"]
357	            action_plan.extend(action_chunk[:REPLAN_STEPS])
358	
359	        action = action_plan.popleft()
360	        if isinstance(action, torch.Tensor):
361	            action = action.cpu().numpy()
362	        action_np = np.asarray(action, dtype=np.float32)
363	
364	        obs, reward, done, info = env.step(
365	            action_np.tolist() if hasattr(action_np, "tolist") else list(action_np)
366	        )
367	        step += 1
368	
369	        all_obs.append(extract_obs_for_saving(obs))
370	        all_actions.append(action_np)
371	
372	        if done or reward > 0:
373	            success = info.get("success", reward > 0)
374	
375	    return {
376	        "observations": all_obs,
377	        "actions": np.stack(all_actions) if all_actions else np.zeros((0, 7)),
378	        "success": success,
379	        "num_steps": step,
380	    }
381	
382	
383	# ---------------------------------------------------------------------------
384	# Collection loops
385	# ---------------------------------------------------------------------------
386	
387	def collect_physical(
388	    policy: object,
389	    tasks: list[dict],
390	    episodes_per_config: int,
391	    output_dir: str,
392	    dry_run: bool,
393	) -> dict:
394	    """Collect expert demos with physical (robot initial state) perturbation.
395	
396	    Uses init_states indices 1-49 (index 0 is nominal).
397	    """
398	    os.makedirs(output_dir, exist_ok=True)
399	    stats = {"total": 0, "success": 0, "saved_files": []}
400	
401	    init_state_indices = list(range(1, 50))  # 49 perturbed states
402	    if dry_run:
403	        tasks = tasks[:1]
404	        init_state_indices = [1]
405	        episodes_per_config = 1
406	
407	    for task_info in tasks:
408	        task_name = task_info["name"]
409	        init_states = torch.load(task_info["init_states_path"], weights_only=False)
410	        language = get_task_language(task_info["bddl_path"])
411	        log.info("Task: %s (%d init_states available)", task_name, len(init_states))
412	
413	        for idx in init_state_indices:
414	            if idx >= len(init_states):
415	                continue
416	
417	            for ep in range(episodes_per_config):
418	                seed = hash((task_name, idx, ep)) % (2**31)
419	                stats["total"] += 1
420	
421	                try:
422	                    env = create_env(task_info["bddl_path"])
423	                    result = rollout_episode(
424	                        policy, env, language, init_states, idx, seed
425	                    )
426	                    env.close()
427	                except Exception:
428	                    log.exception(
429	                        "Episode failed: task=%s idx=%d ep=%d", task_name, idx, ep
430	                    )
431	                    continue
432	
433	                if result["success"]:
434	                    stats["success"] += 1
435	                    demo = {
436	                        "observations": result["observations"],
437	                        "actions": result["actions"],
438	                        "task_name": task_name,
439	                        "perturbation_config": {
440	                            "type": "physical",
441	                            "init_state_idx": idx,
442	                        },
443	                        "success": True,
444	                        "num_steps": result["num_steps"],
445	                    }
446	                    fname = f"{task_name}_initstate{idx}_ep{ep}.pkl"
447	                    fpath = os.path.join(output_dir, fname)
448	                    with open(fpath, "wb") as f:
449	                        pickle.dump(demo, f, protocol=pickle.HIGHEST_PROTOCOL)
450	                    stats["saved_files"].append(fpath)
451	
452	                rate = stats["success"] / stats["total"] * 100
453	                log.info(
454	                    "[physical] task=%s idx=%d ep=%d | %s | "
455	                    "cumulative %d/%d (%.1f%%)",
456	                    task_name, idx, ep,
457	                    "SUCCESS" if result["success"] else "FAIL",
458	                    stats["success"], stats["total"], rate,
459	                )
460	
461	    return stats
462	
463	
464	def collect_spatial(
465	    policy: object,
466	    tasks: list[dict],
467	    episodes_per_config: int,
468	    output_dir: str,
469	    dry_run: bool,
470	) -> dict:
471	    """Collect expert demos with spatial (objects layout) perturbation.
472	
473	    Applies 10 predefined spatial perturbation configs to each base task.
474	    """
475	    os.makedirs(output_dir, exist_ok=True)
476	    tmp_bddl_dir = os.path.join(output_dir, "_tmp_bddl")
477	    os.makedirs(tmp_bddl_dir, exist_ok=True)
478	    stats = {"total": 0, "success": 0, "saved_files": []}
479	
480	    configs = SPATIAL_PERTURBATION_CONFIGS
481	    if dry_run:
482	        tasks = tasks[:1]
483	        configs = configs[:1]
484	        episodes_per_config = 1
485	
486	    for task_info in tasks:
487	        task_name = task_info["name"]
488	        init_states = torch.load(task_info["init_states_path"], weights_only=False)
489	        log.info("Task: %s", task_name)
490	
491	        for cfg_idx, cfg in enumerate(configs):
492	            try:
493	                perturbed_bddl = create_spatial_bddl(
494	                    task_info["bddl_path"], cfg, tmp_bddl_dir
495	                )
496	                language = get_task_language(perturbed_bddl)
497	            except Exception:
498	                log.exception(
499	                    "BDDL perturbation failed: task=%s cfg=%d", task_name, cfg_idx
500	                )
501	                continue
502	
503	            for ep in range(episodes_per_config):
504	                seed = hash((task_name, cfg_idx, ep)) % (2**31)
505	                stats["total"] += 1
506	
507	                try:
508	                    env = create_env(perturbed_bddl)
509	                    # Use nominal init_state (index 0) for spatial perturbation
510	                    result = rollout_episode(
511	                        policy, env, language, init_states, 0, seed
512	                    )
513	                    env.close()
514	                except Exception:
515	                    log.exception(
516	                        "Episode failed: task=%s cfg=%d ep=%d",
517	                        task_name, cfg_idx, ep,
518	                    )
519	                    continue
520	
521	                if result["success"]:
522	                    stats["success"] += 1
523	                    demo = {
524	                        "observations": result["observations"],
525	                        "actions": result["actions"],
526	                        "task_name": task_name,
527	                        "perturbation_config": {
528	                            "type": "spatial",
529	                            "config_idx": cfg_idx,
530	                            "delta_xy": cfg["delta_xy"],
531	                            "delta_half_len": cfg["delta_half_len"],
532	                            "delta_yaw": cfg["delta_yaw"],
533	                        },
534	                        "success": True,
535	                        "num_steps": result["num_steps"],
536	                    }
537	                    fname = f"{task_name}_spatial{cfg_idx}_ep{ep}.pkl"
538	                    fpath = os.path.join(output_dir, fname)
539	                    with open(fpath, "wb") as f:
540	                        pickle.dump(demo, f, protocol=pickle.HIGHEST_PROTOCOL)
541	                    stats["saved_files"].append(fpath)
542	
543	                rate = stats["success"] / stats["total"] * 100
544	                log.info(
545	                    "[spatial] task=%s cfg=%d ep=%d | %s | "
546	                    "cumulative %d/%d (%.1f%%)",
547	                    task_name, cfg_idx, ep,
548	                    "SUCCESS" if result["success"] else "FAIL",
549	                    stats["success"], stats["total"], rate,
550	                )
551	
552	    return stats
553	
554	
555	def collect_spatial_add_n(
556	    policy: object,
557	    episodes_per_task: int,
558	    output_dir: str,
559	    dry_run: bool,
560	) -> dict:
561	    """Collect expert demos using LIBERO-Plus _add_N distractor-object tasks.
562	
563	    Each _add_N task is a pre-built BDDL with extra objects in the scene.
564	    208 tasks × 3 episodes = 624 rollouts.
565	    """
566	    os.makedirs(output_dir, exist_ok=True)
567	    stats = {"total": 0, "success": 0, "saved_files": [], "load_errors": 0}
568	
569	    add_tasks = discover_add_n_tasks()
570	    if not add_tasks:
571	        log.error("No _add_N tasks found. Check LIBERO-Plus installation.")
572	        return stats
573	
574	    if dry_run:
575	        add_tasks = add_tasks[:2]
576	        episodes_per_task = 1
577	
578	    log.info(
579	        "Collecting spatial (_add_N): %d tasks × %d eps = %d rollouts",
580	        len(add_tasks), episodes_per_task, len(add_tasks) * episodes_per_task,
581	    )
582	
583	    for task_info in add_tasks:
584	        task_name = task_info["name"]
585	        language = task_info["language"]
586	        init_states = task_info["init_states"]
587	
588	        for ep in range(episodes_per_task):
589	            seed = hash((task_name, ep)) % (2**31)
590	            stats["total"] += 1
591	
592	            try:
593	                env = create_env(task_info["bddl_path"])
594	                init_idx = ep % len(init_states)
595	                result = rollout_episode(
596	                    policy, env, language, init_states, init_idx, seed
597	                )
598	                env.close()
599	            except FileNotFoundError as e:
600	                stats["load_errors"] += 1
601	                log.warning("Asset missing for %s: %s", task_name, e)
602	                continue
603	            except Exception:
604	                log.exception("Episode failed: task=%s ep=%d", task_name, ep)
605	                continue
606	
607	            if result["success"]:
608	                stats["success"] += 1
609	                demo = {
610	                    "observations": result["observations"],
611	                    "actions": result["actions"],
612	                    "task_name": task_name,
613	                    "perturbation_config": {
614	                        "type": "spatial_add_n",
615	                        "source_task_idx": task_info["idx"],
616	                    },
617	                    "success": True,
618	                    "num_steps": result["num_steps"],
619	                }
620	                fname = f"{task_name}_ep{ep}.pkl"
621	                fpath = os.path.join(output_dir, fname)
622	                with open(fpath, "wb") as f:
623	                    pickle.dump(demo, f, protocol=pickle.HIGHEST_PROTOCOL)
624	                stats["saved_files"].append(fpath)
625	
626	            rate = stats["success"] / stats["total"] * 100
627	            log.info(
628	                "[spatial_add_n] task=%s ep=%d | %s | cumulative %d/%d (%.1f%%) | load_errors=%d",
629	                task_name, ep,
630	                "SUCCESS" if result["success"] else "FAIL",
631	                stats["success"], stats["total"], rate,
632	                stats["load_errors"],
633	            )
634	
635	    return stats
636	
637	
638	# ---------------------------------------------------------------------------
639	# Main
640	# ---------------------------------------------------------------------------
641	
642	def main():
643	    parser = argparse.ArgumentParser(
644	        description="Collect expert demos from π₀ in perturbed LIBERO environments"
645	    )
646	    parser.add_argument(
647	        "--perturbation_type", type=str, required=True,
648	        choices=["physical", "spatial"],
649	    )
650	    parser.add_argument(
651	        "--spatial_mode", type=str, default="add_n",
652	        choices=["add_n", "perturb_region"],
653	        help="Spatial perturbation mode: add_n (LIBERO-Plus distractors, default) "
654	             "or perturb_region (legacy BDDL region shifts)",
655	    )
656	    parser.add_argument("--gpu_id", type=int, default=0)
657	    parser.add_argument("--num_tasks", type=int, default=10)
658	    parser.add_argument("--episodes_per_config", type=int, default=3)
659	    parser.add_argument(
660	        "--output_dir", type=str, default=None,
661	        help="Override output directory (default: auto from perturbation_type)",
662	    )
663	    parser.add_argument(
664	        "--checkpoint", type=str,
665	        default="/root/autodl-tmp/checkpoints/pi0_base",
666	    )
667	    parser.add_argument("--dry_run", action="store_true")
668	    parser.add_argument("--seed", type=int, default=42)
669	    args = parser.parse_args()
670	
671	    logging.basicConfig(
672	        level=logging.INFO,
673	        format="%(asctime)s [%(levelname)s] %(message)s",
674	    )
675	
676	    random.seed(args.seed)
677	    np.random.seed(args.seed)
678	    torch.manual_seed(args.seed)
679	
680	    if args.output_dir is None:
681	        args.output_dir = (
682	            f"/root/meta_brain_lora_routing/data/expert_demos/{args.perturbation_type}"
683	        )
684	
685	    device = f"cuda:{args.gpu_id}"
686	    log.info(
687	        "Config: type=%s spatial_mode=%s device=%s num_tasks=%d eps_per_cfg=%d dry_run=%s",
688	        args.perturbation_type, args.spatial_mode, device, args.num_tasks,
689	        args.episodes_per_config, args.dry_run,
690	    )
691	
692	    log.info("Loading π₀ from %s", args.checkpoint)
693	    policy = load_pi0_policy(args.checkpoint, device)
694	
695	    t0 = time.time()
696	
697	    if args.perturbation_type == "physical":
698	        from libero.libero import get_libero_path
699	        bddl_dir = os.path.join(get_libero_path("bddl_files"), BASE_TASK_SUITE)
700	        tasks = find_base_tasks(bddl_dir, num_tasks=args.num_tasks)
701	        if not tasks:
702	            log.error("No base tasks found in %s", bddl_dir)
703	            sys.exit(1)
704	        stats = collect_physical(
705	            policy, tasks, args.episodes_per_config,
706	            args.output_dir, args.dry_run,
707	        )
708	    elif args.spatial_mode == "add_n":
709	        stats = collect_spatial_add_n(
710	            policy, args.episodes_per_config,
711	            args.output_dir, args.dry_run,
712	        )
713	    else:
714	        from libero.libero import get_libero_path
715	        bddl_dir = os.path.join(get_libero_path("bddl_files"), BASE_TASK_SUITE)
716	        tasks = find_base_tasks(bddl_dir, num_tasks=args.num_tasks)
717	        if not tasks:
718	            log.error("No base tasks found in %s", bddl_dir)
719	            sys.exit(1)
720	        stats = collect_spatial(
721	            policy, tasks, args.episodes_per_config,
722	            args.output_dir, args.dry_run,
723	        )
724	
725	    elapsed = time.time() - t0
726	
727	    total_size = sum(
728	        os.path.getsize(f) for f in stats["saved_files"] if os.path.exists(f)
729	    )
730	    log.info("=" * 60)
731	    log.info("Collection complete: %s", args.perturbation_type)
732	    log.info("  Total episodes:  %d", stats["total"])
733	    log.info("  Successful:      %d", stats["success"])
734	    log.info(
735	        "  Success rate:    %.1f%%",
736	        stats["success"] / max(stats["total"], 1) * 100,
737	    )
738	    log.info("  Files saved:     %d", len(stats["saved_files"]))
739	    log.info("  Total size:      %.1f MB", total_size / 1024 / 1024)
740	    log.info("  Elapsed:         %.1f min", elapsed / 60)
741	    log.info("  Output dir:      %s", args.output_dir)
742	
743	
744	if __name__ == "__main__":
745	    main()
746	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "59a342d4-e180-485d-b939-53766e9dd5d7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py",
      "content": "\"\"\"\nCollect expert demonstrations by rolling out frozen π₀ in perturbed LIBERO environments.\n\nOnly successful episodes are saved. Two perturbation types are supported:\n  - physical: vary robot initial state (init_states index 1-49)\n  - spatial:  LIBERO-Plus _add_N distractor objects (default) or perturb_region fallback\n\nOutput: pickle files with (observations, actions, metadata) per episode.\n\nUsage:\n    # Physical perturbation dry-run\n    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \\\n        --perturbation_type physical --dry_run\n\n    # Spatial perturbation dry-run (uses _add_N by default)\n    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \\\n        --perturbation_type spatial --dry_run\n\n    # Spatial with legacy perturb_region mode\n    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \\\n        --perturbation_type spatial --spatial_mode perturb_region --dry_run\n\n    # Full physical collection\n    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \\\n        --perturbation_type physical\n\"\"\"\n\nimport argparse\nimport collections\nimport copy\nimport logging\nimport math\nimport os\nimport pickle\nimport random\nimport re\nimport sys\nimport time\nimport types\nfrom pathlib import Path\nfrom typing import Any\n\nimport numpy as np\nimport torch\n\nlog = logging.getLogger(__name__)\n\n# ---------------------------------------------------------------------------\n# Constants\n# ---------------------------------------------------------------------------\n\nLIBERO_DUMMY_ACTION = [0.0] * 6 + [-1.0]\nLIBERO_ENV_RESOLUTION = 256\nMODEL_INPUT_RESOLUTION = 224\nREPLAN_STEPS = 5\nNUM_STEPS_WAIT = 10\nMAX_STEPS = 220  # libero_spatial default\n\n# 10 base tasks in libero_spatial (no perturbation suffix)\nBASE_TASK_SUITE = \"libero_spatial\"\n\n# Spatial perturbation grid: 10 configurations with varying XY shifts and yaw\n# Magnitudes chosen to be noticeable but within feasible reach of the robot.\nSPATIAL_PERTURBATION_CONFIGS = [\n    {\"delta_xy\": ( 0.05,  0.00), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.0)},\n    {\"delta_xy\": (-0.05,  0.00), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.0)},\n    {\"delta_xy\": ( 0.00,  0.05), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.0)},\n    {\"delta_xy\": ( 0.00, -0.05), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.0)},\n    {\"delta_xy\": ( 0.03,  0.03), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.0)},\n    {\"delta_xy\": (-0.03, -0.03), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.0)},\n    {\"delta_xy\": ( 0.04,  0.00), \"delta_half_len\": 0.01, \"delta_yaw\": (0.3, 0.0)},\n    {\"delta_xy\": (-0.04,  0.00), \"delta_half_len\": 0.01, \"delta_yaw\": (-0.3, 0.0)},\n    {\"delta_xy\": ( 0.00,  0.04), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, 0.3)},\n    {\"delta_xy\": ( 0.00, -0.04), \"delta_half_len\": 0.0,  \"delta_yaw\": (0.0, -0.3)},\n]\n\n\n# ---------------------------------------------------------------------------\n# Geometry / image helpers (from libero_integration.py)\n# ---------------------------------------------------------------------------\n\ndef _quat2axisangle(quat: np.ndarray) -> np.ndarray:\n    \"\"\"Quaternion [x,y,z,w] -> axis-angle [ax,ay,az].\"\"\"\n    q = np.asarray(quat, dtype=np.float64)\n    norm = np.linalg.norm(q)\n    if norm < 1e-8:\n        return np.zeros(3, dtype=np.float32)\n    q /= norm\n    sin_half = np.linalg.norm(q[:3])\n    if sin_half < 1e-8:\n        return np.zeros(3, dtype=np.float32)\n    angle = 2.0 * math.atan2(sin_half, q[3])\n    axis = q[:3] / sin_half\n    return (axis * angle).astype(np.float32)\n\n\ndef _resize_with_pad(img: np.ndarray, size: int) -> np.ndarray:\n    \"\"\"Resize image with aspect-preserving padding to (size, size, 3) uint8.\"\"\"\n    try:\n        from openpi_client.image_tools import resize_with_pad, convert_to_uint8\n        return convert_to_uint8(resize_with_pad(img, size, size))\n    except ImportError:\n        from PIL import Image as PILImage\n        h, w = img.shape[:2]\n        scale = min(size / h, size / w)\n        new_h, new_w = int(h * scale), int(w * scale)\n        resized = np.array(\n            PILImage.fromarray(img).resize((new_w, new_h), PILImage.BILINEAR)\n        )\n        canvas = np.zeros((size, size, 3), dtype=np.uint8)\n        y0, x0 = (size - new_h) // 2, (size - new_w) // 2\n        canvas[y0 : y0 + new_h, x0 : x0 + new_w] = resized\n        return canvas\n\n\ndef obs_to_model_input(obs: dict, task_description: str) -> dict:\n    \"\"\"Convert LIBERO observation to the dict format expected by policy.infer().\"\"\"\n    base_img = np.ascontiguousarray(obs[\"agentview_image\"][::-1, ::-1])\n    wrist_img = np.ascontiguousarray(obs[\"robot0_eye_in_hand_image\"][::-1, ::-1])\n\n    base_img = _resize_with_pad(base_img, MODEL_INPUT_RESOLUTION)\n    wrist_img = _resize_with_pad(wrist_img, MODEL_INPUT_RESOLUTION)\n\n    state = np.concatenate([\n        obs[\"robot0_eef_pos\"].astype(np.float32),\n        _quat2axisangle(obs[\"robot0_eef_quat\"]),\n        obs[\"robot0_gripper_qpos\"].astype(np.float32),\n    ])\n\n    return {\n        \"observation/image\": base_img,\n        \"observation/wrist_image\": wrist_img,\n        \"observation/state\": state,\n        \"prompt\": task_description,\n    }\n\n\ndef extract_obs_for_saving(obs: dict) -> dict:\n    \"\"\"Extract observation fields to save in demo data (images stored as uint8).\"\"\"\n    return {\n        \"agentview_image\": obs[\"agentview_image\"].copy(),\n        \"robot0_eye_in_hand_image\": obs[\"robot0_eye_in_hand_image\"].copy(),\n        \"robot0_eef_pos\": obs[\"robot0_eef_pos\"].astype(np.float32).copy(),\n        \"robot0_eef_quat\": obs[\"robot0_eef_quat\"].astype(np.float32).copy(),\n        \"robot0_gripper_qpos\": obs[\"robot0_gripper_qpos\"].astype(np.float32).copy(),\n    }\n\n\n# ---------------------------------------------------------------------------\n# Model loading\n# ---------------------------------------------------------------------------\n\ndef _ensure_openpi_imports():\n    \"\"\"Stub out lerobot (training-only dep) before importing OpenPI.\"\"\"\n    for mod in [\n        \"lerobot\", \"lerobot.common\", \"lerobot.common.datasets\",\n        \"lerobot.common.datasets.lerobot_dataset\",\n    ]:\n        if mod not in sys.modules:\n            sys.modules[mod] = types.ModuleType(mod)\n\n\ndef load_pi0_policy(checkpoint_path: str, device: str) -> object:\n    \"\"\"Load pi0 policy via OpenPI. Returns the Policy object for inference.\"\"\"\n    _ensure_openpi_imports()\n    from openpi.training import config as _config\n    from openpi.policies import policy_config\n\n    train_config = _config.get_config(\"pi0_libero\")\n    policy = policy_config.create_trained_policy(\n        train_config, checkpoint_path, pytorch_device=device\n    )\n    log.info(\"Loaded pi0 policy on %s\", device)\n    return policy\n\n\n# ---------------------------------------------------------------------------\n# Task discovery\n# ---------------------------------------------------------------------------\n\ndef find_base_tasks(bddl_dir: str, num_tasks: int = 10) -> list[dict]:\n    \"\"\"Find base (unperturbed) BDDL files in libero_spatial.\n\n    Returns list of dicts with keys: name, bddl_path, init_states_path.\n    \"\"\"\n    all_files = [f for f in os.listdir(bddl_dir) if f.endswith(\".bddl\")]\n\n    base_names = []\n    for f in sorted(all_files):\n        name = f.replace(\".bddl\", \"\")\n        # Skip any file with perturbation suffixes\n        if re.search(\n            r\"(_add_\\d+|_table_\\d+|_tb_\\d+|_light_\\d+|_language_\\d+\"\n            r\"|_view_|_noise_|_level\\d+| copy)\",\n            name,\n        ):\n            continue\n        base_names.append(name)\n\n    init_dir = bddl_dir.replace(\"bddl_files\", \"init_files\")\n    tasks = []\n    for name in base_names[:num_tasks]:\n        bddl_path = os.path.join(bddl_dir, f\"{name}.bddl\")\n        init_path = os.path.join(init_dir, f\"{name}.pruned_init\")\n        if not os.path.exists(init_path):\n            log.warning(\"init_states not found for %s, skipping\", name)\n            continue\n        tasks.append({\n            \"name\": name,\n            \"bddl_path\": bddl_path,\n            \"init_states_path\": init_path,\n        })\n\n    log.info(\"Found %d base tasks\", len(tasks))\n    return tasks\n\n\ndef get_task_language(bddl_path: str) -> str:\n    \"\"\"Extract language instruction from a BDDL file.\"\"\"\n    from libero.libero.envs.bddl_utils import get_problem_info\n    info = get_problem_info(bddl_path)\n    return info[\"language_instruction\"]\n\n\ndef discover_add_n_tasks(task_suite: str = BASE_TASK_SUITE) -> list[dict]:\n    \"\"\"Discover all _add_N (distractor-object) tasks from the LIBERO-Plus benchmark.\n\n    Returns list of dicts with: idx, name, language, bddl_path, init_states.\n    \"\"\"\n    from libero.libero import benchmark, get_libero_path\n    benchmark_dict = benchmark.get_benchmark_dict()\n    suite = benchmark_dict[task_suite]()\n    bddl_root = Path(get_libero_path(\"bddl_files\"))\n\n    tasks = []\n    skipped = 0\n    for i in range(suite.n_tasks):\n        task = suite.get_task(i)\n        name = getattr(task, \"name\", \"\") or getattr(task, \"bddl_file\", \"\")\n        if not re.search(r\"_add_\\d+$\", name.replace(\".bddl\", \"\")):\n            continue\n\n        bddl_path = str(bddl_root / task.problem_folder / task.bddl_file)\n        if not os.path.exists(bddl_path):\n            log.warning(\"BDDL not found, skipping: %s\", bddl_path)\n            skipped += 1\n            continue\n\n        try:\n            init_states = suite.get_task_init_states(i)\n        except Exception:\n            log.warning(\"init_states failed for %s, skipping\", name)\n            skipped += 1\n            continue\n\n        tasks.append({\n            \"idx\": i,\n            \"name\": name.replace(\".bddl\", \"\"),\n            \"language\": task.language,\n            \"bddl_path\": bddl_path,\n            \"init_states\": init_states,\n        })\n\n    log.info(\n        \"Discovered %d _add_N tasks (%d skipped) from %s\",\n        len(tasks), skipped, task_suite,\n    )\n    return tasks\n\n\n# ---------------------------------------------------------------------------\n# Environment creation\n# ---------------------------------------------------------------------------\n\ndef create_env(bddl_path: str) -> object:\n    \"\"\"Create a LIBERO OffScreenRenderEnv from a BDDL file.\"\"\"\n    from libero.libero.envs import OffScreenRenderEnv\n    env = OffScreenRenderEnv(\n        bddl_file_name=bddl_path,\n        camera_heights=LIBERO_ENV_RESOLUTION,\n        camera_widths=LIBERO_ENV_RESOLUTION,\n    )\n    return env\n\n\ndef create_spatial_bddl(\n    base_bddl_path: str,\n    perturbation_config: dict,\n    output_dir: str,\n) -> str:\n    \"\"\"Create a perturbed BDDL file by applying spatial perturbation to all regions.\n\n    Returns the path to the new BDDL file.\n    \"\"\"\n    sys.path.insert(0, \"/root/LIBERO-plus/libero\")\n    from libero.randomizer.bddl_operators import (\n        load_bddl_file,\n        save_bddl_file,\n        perturb_region_info,\n    )\n\n    spec = load_bddl_file(base_bddl_path)\n    delta_xy = perturbation_config[\"delta_xy\"]\n    delta_half = perturbation_config[\"delta_half_len\"]\n    delta_yaw = perturbation_config[\"delta_yaw\"]\n\n    for i in range(len(spec.region_infos)):\n        spec.region_infos[i] = perturb_region_info(\n            spec.region_infos[i],\n            delta_region_centroid_xy=delta_xy,\n            delta_region_half_len=delta_half,\n            delta_yaw_rotation=delta_yaw,\n        )\n\n    os.makedirs(output_dir, exist_ok=True)\n    base_name = Path(base_bddl_path).stem\n    dx, dy = delta_xy\n    filename = f\"{base_name}_spatial_dx{dx:.2f}_dy{dy:.2f}.bddl\"\n    _, filepath = save_bddl_file(spec, bddl_filename=filename, bddl_dirpath=output_dir)\n    return filepath\n\n\n# ---------------------------------------------------------------------------\n# Episode rollout\n# ---------------------------------------------------------------------------\n\ndef rollout_episode(\n    policy: object,\n    env: object,\n    task_description: str,\n    init_states: np.ndarray,\n    init_state_idx: int,\n    seed: int,\n) -> dict[str, Any]:\n    \"\"\"Run one episode, collecting (obs, action) pairs.\n\n    Returns dict with observations, actions, success, num_steps.\n    \"\"\"\n    env.seed(seed)\n    obs = env.set_init_state(init_states[init_state_idx])\n\n    for _ in range(NUM_STEPS_WAIT):\n        obs, _, _, _ = env.step(LIBERO_DUMMY_ACTION)\n\n    all_obs = [extract_obs_for_saving(obs)]\n    all_actions = []\n    action_plan = collections.deque()\n    step = 0\n    success = False\n    done = False\n\n    while not done and step < MAX_STEPS:\n        if len(action_plan) == 0:\n            obs_dict = obs_to_model_input(obs, task_description)\n            result = policy.infer(obs_dict)\n            action_chunk = result[\"actions\"]\n            action_plan.extend(action_chunk[:REPLAN_STEPS])\n\n        action = action_plan.popleft()\n        if isinstance(action, torch.Tensor):\n            action = action.cpu().numpy()\n        action_np = np.asarray(action, dtype=np.float32)\n\n        obs, reward, done, info = env.step(\n            action_np.tolist() if hasattr(action_np, \"tolist\") else list(action_np)\n        )\n        step += 1\n\n        all_obs.append(extract_obs_for_saving(obs))\n        all_actions.append(action_np)\n\n        if done or reward > 0:\n            success = info.get(\"success\", reward > 0)\n\n    return {\n        \"observations\": all_obs,\n        \"actions\": np.stack(all_actions) if all_actions else np.zeros((0, 7)),\n        \"success\": success,\n        \"num_steps\": step,\n    }\n\n\n# ---------------------------------------------------------------------------\n# Collection loops\n# ---------------------------------------------------------------------------\n\ndef collect_physical(\n    policy: object,\n    tasks: list[dict],\n    episodes_per_config: int,\n    output_dir: str,\n    dry_run: bool,\n) -> dict:\n    \"\"\"Collect expert demos with physical (robot initial state) perturbation.\n\n    Uses init_states indices 1-49 (index 0 is nominal).\n    \"\"\"\n    os.makedirs(output_dir, exist_ok=True)\n    stats = {\"total\": 0, \"success\": 0, \"saved_files\": []}\n\n    init_state_indices = list(range(1, 50))  # 49 perturbed states\n    if dry_run:\n        tasks = tasks[:1]\n        init_state_indices = [1]\n        episodes_per_config = 1\n\n    for task_info in tasks:\n        task_name = task_info[\"name\"]\n        init_states = torch.load(task_info[\"init_states_path\"], weights_only=False)\n        language = get_task_language(task_info[\"bddl_path\"])\n        log.info(\"Task: %s (%d init_states available)\", task_name, len(init_states))\n\n        for idx in init_state_indices:\n            if idx >= len(init_states):\n                continue\n\n            for ep in range(episodes_per_config):\n                seed = hash((task_name, idx, ep)) % (2**31)\n                stats[\"total\"] += 1\n\n                try:\n                    env = create_env(task_info[\"bddl_path\"])\n                    result = rollout_episode(\n                        policy, env, language, init_states, idx, seed\n                    )\n                    env.close()\n                except Exception:\n                    log.exception(\n                        \"Episode failed: task=%s idx=%d ep=%d\", task_name, idx, ep\n                    )\n                    continue\n\n                if result[\"success\"]:\n                    stats[\"success\"] += 1\n                    demo = {\n                        \"observations\": result[\"observations\"],\n                        \"actions\": result[\"actions\"],\n                        \"task_name\": task_name,\n                        \"perturbation_config\": {\n                            \"type\": \"physical\",\n                            \"init_state_idx\": idx,\n                        },\n                        \"success\": True,\n                        \"num_steps\": result[\"num_steps\"],\n                    }\n                    fname = f\"{task_name}_initstate{idx}_ep{ep}.pkl\"\n                    fpath = os.path.join(output_dir, fname)\n                    with open(fpath, \"wb\") as f:\n                        pickle.dump(demo, f, protocol=pickle.HIGHEST_PROTOCOL)\n                    stats[\"saved_files\"].append(fpath)\n\n                rate = stats[\"success\"] / stats[\"total\"] * 100\n                log.info(\n                    \"[physical] task=%s idx=%d ep=%d | %s | \"\n                    \"cumulative %d/%d (%.1f%%)\",\n                    task_name, idx, ep,\n                    \"SUCCESS\" if result[\"success\"] else \"FAIL\",\n                    stats[\"success\"], stats[\"total\"], rate,\n                )\n\n    return stats\n\n\ndef collect_spatial(\n    policy: object,\n    tasks: list[dict],\n    episodes_per_config: int,\n    output_dir: str,\n    dry_run: bool,\n) -> dict:\n    \"\"\"Collect expert demos with spatial (objects layout) perturbation.\n\n    Applies 10 predefined spatial perturbation configs to each base task.\n    \"\"\"\n    os.makedirs(output_dir, exist_ok=True)\n    tmp_bddl_dir = os.path.join(output_dir, \"_tmp_bddl\")\n    os.makedirs(tmp_bddl_dir, exist_ok=True)\n    stats = {\"total\": 0, \"success\": 0, \"saved_files\": []}\n\n    configs = SPATIAL_PERTURBATION_CONFIGS\n    if dry_run:\n        tasks = tasks[:1]\n        configs = configs[:1]\n        episodes_per_config = 1\n\n    for task_info in tasks:\n        task_name = task_info[\"name\"]\n        init_states = torch.load(task_info[\"init_states_path\"], weights_only=False)\n        log.info(\"Task: %s\", task_name)\n\n        for cfg_idx, cfg in enumerate(configs):\n            try:\n                perturbed_bddl = create_spatial_bddl(\n                    task_info[\"bddl_path\"], cfg, tmp_bddl_dir\n                )\n                language = get_task_language(perturbed_bddl)\n            except Exception:\n                log.exception(\n                    \"BDDL perturbation failed: task=%s cfg=%d\", task_name, cfg_idx\n                )\n                continue\n\n            for ep in range(episodes_per_config):\n                seed = hash((task_name, cfg_idx, ep)) % (2**31)\n                stats[\"total\"] += 1\n\n                try:\n                    env = create_env(perturbed_bddl)\n                    # Use nominal init_state (index 0) for spatial perturbation\n                    result = rollout_episode(\n                        policy, env, language, init_states, 0, seed\n                    )\n                    env.close()\n                except Exception:\n                    log.exception(\n                        \"Episode failed: task=%s cfg=%d ep=%d\",\n                        task_name, cfg_idx, ep,\n                    )\n                    continue\n\n                if result[\"success\"]:\n                    stats[\"success\"] += 1\n                    demo = {\n                        \"observations\": result[\"observations\"],\n                        \"actions\": result[\"actions\"],\n                        \"task_name\": task_name,\n                        \"perturbation_config\": {\n                            \"type\": \"spatial\",\n                            \"config_idx\": cfg_idx,\n                            \"delta_xy\": cfg[\"delta_xy\"],\n                            \"delta_half_len\": cfg[\"delta_half_len\"],\n                            \"delta_yaw\": cfg[\"delta_yaw\"],\n                        },\n                        \"success\": True,\n                        \"num_steps\": result[\"num_steps\"],\n                    }\n                    fname = f\"{task_name}_spatial{cfg_idx}_ep{ep}.pkl\"\n                    fpath = os.path.join(output_dir, fname)\n                    with open(fpath, \"wb\") as f:\n                        pickle.dump(demo, f, protocol=pickle.HIGHEST_PROTOCOL)\n                    stats[\"saved_files\"].append(fpath)\n\n                rate = stats[\"success\"] / stats[\"total\"] * 100\n                log.info(\n                    \"[spatial] task=%s cfg=%d ep=%d | %s | \"\n                    \"cumulative %d/%d (%.1f%%)\",\n                    task_name, cfg_idx, ep,\n                    \"SUCCESS\" if result[\"success\"] else \"FAIL\",\n                    stats[\"success\"], stats[\"total\"], rate,\n                )\n\n    return stats\n\n\ndef collect_spatial_add_n(\n    policy: object,\n    episodes_per_task: int,\n    output_dir: str,\n    dry_run: bool,\n) -> dict:\n    \"\"\"Collect expert demos using LIBERO-Plus _add_N distractor-object tasks.\n\n    Each _add_N task is a pre-built BDDL with extra objects in the scene.\n    208 tasks × 3 episodes = 624 rollouts.\n    \"\"\"\n    os.makedirs(output_dir, exist_ok=True)\n    stats = {\"total\": 0, \"success\": 0, \"saved_files\": [], \"load_errors\": 0}\n\n    add_tasks = discover_add_n_tasks()\n    if not add_tasks:\n        log.error(\"No _add_N tasks found. Check LIBERO-Plus installation.\")\n        return stats\n\n    if dry_run:\n        add_tasks = add_tasks[:2]\n        episodes_per_task = 1\n\n    log.info(\n        \"Collecting spatial (_add_N): %d tasks × %d eps = %d rollouts\",\n        len(add_tasks), episodes_per_task, len(add_tasks) * episodes_per_task,\n    )\n\n    for task_info in add_tasks:\n        task_name = task_info[\"name\"]\n        language = task_info[\"language\"]\n        init_states = task_info[\"init_states\"]\n\n        for ep in range(episodes_per_task):\n            seed = hash((task_name, ep)) % (2**31)\n            stats[\"total\"] += 1\n\n            try:\n                env = create_env(task_info[\"bddl_path\"])\n                init_idx = ep % len(init_states)\n                result = rollout_episode(\n                    policy, env, language, init_states, init_idx, seed\n                )\n                env.close()\n            except FileNotFoundError as e:\n                stats[\"load_errors\"] += 1\n                log.warning(\"Asset missing for %s: %s\", task_name, e)\n                continue\n            except Exception:\n                log.exception(\"Episode failed: task=%s ep=%d\", task_name, ep)\n                continue\n\n            if result[\"success\"]:\n                stats[\"success\"] += 1\n                demo = {\n                    \"observations\": result[\"observations\"],\n                    \"actions\": result[\"actions\"],\n                    \"task_name\": task_name,\n                    \"perturbation_config\": {\n                        \"type\": \"spatial_add_n\",\n                        \"source_task_idx\": task_info[\"idx\"],\n                    },\n                    \"success\": True,\n                    \"num_steps\": result[\"num_steps\"],\n                }\n                fname = f\"{task_name}_ep{ep}.pkl\"\n                fpath = os.path.join(output_dir, fname)\n                with open(fpath, \"wb\") as f:\n                    pickle.dump(demo, f, protocol=pickle.HIGHEST_PROTOCOL)\n                stats[\"saved_files\"].append(fpath)\n\n            rate = stats[\"success\"] / stats[\"total\"] * 100\n            log.info(\n                \"[spatial_add_n] task=%s ep=%d | %s | cumulative %d/%d (%.1f%%) | load_errors=%d\",\n                task_name, ep,\n                \"SUCCESS\" if result[\"success\"] else \"FAIL\",\n                stats[\"success\"], stats[\"total\"], rate,\n                stats[\"load_errors\"],\n            )\n\n    return stats\n\n\n# ---------------------------------------------------------------------------\n# Main\n# ---------------------------------------------------------------------------\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Collect expert demos from π₀ in perturbed LIBERO environments\"\n    )\n    parser.add_argument(\n        \"--perturbation_type\", type=str, required=True,\n        choices=[\"physical\", \"spatial\"],\n    )\n    parser.add_argument(\n        \"--spatial_mode\", type=str, default=\"add_n\",\n        choices=[\"add_n\", \"perturb_region\"],\n        help=\"Spatial perturbation mode: add_n (LIBERO-Plus distractors, default) \"\n             \"or perturb_region (legacy BDDL region shifts)\",\n    )\n    parser.add_argument(\"--gpu_id\", type=int, default=0)\n    parser.add_argument(\"--num_tasks\", type=int, default=10)\n    parser.add_argument(\"--episodes_per_config\", type=int, default=3)\n    parser.add_argument(\n        \"--output_dir\", type=str, default=None,\n        help=\"Override output directory (default: auto from perturbation_type)\",\n    )\n    parser.add_argument(\n        \"--checkpoint\", type=str,\n        default=\"/root/autodl-tmp/checkpoints/pi0_base\",\n    )\n    parser.add_argument(\"--dry_run\", action=\"store_true\")\n    parser.add_argument(\"--seed\", type=int, default=42)\n    args = parser.parse_args()\n\n    logging.basicConfig(\n        level=logging.INFO,\n        format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    )\n\n    random.seed(args.seed)\n    np.random.seed(args.seed)\n    torch.manual_seed(args.seed)\n\n    if args.output_dir is None:\n        args.output_dir = (\n            f\"/root/meta_brain_lora_routing/data/expert_demos/{args.perturbation_type}\"\n        )\n\n    device = f\"cuda:{args.gpu_id}\"\n    log.info(\n        \"Config: type=%s spatial_mode=%s device=%s num_tasks=%d eps_per_cfg=%d dry_run=%s\",\n        args.perturbation_type, args.spatial_mode, device, args.num_tasks,\n        args.episodes_per_config, args.dry_run,\n    )\n\n    log.info(\"Loading π₀ from %s\", args.checkpoint)\n    policy = load_pi0_policy(args.checkpoint, device)\n\n    t0 = time.time()\n\n    if args.perturbation_type == \"physical\":\n        from libero.libero import get_libero_path\n        bddl_dir = os.path.join(get_libero_path(\"bddl_files\"), BASE_TASK_SUITE)\n        tasks = find_base_tasks(bddl_dir, num_tasks=args.num_tasks)\n        if not tasks:\n            log.error(\"No base tasks found in %s\", bddl_dir)\n            sys.exit(1)\n        stats = collect_physical(\n            policy, tasks, args.episodes_per_config,\n            args.output_dir, args.dry_run,\n        )\n    elif args.spatial_mode == \"add_n\":\n        stats = collect_spatial_add_n(\n            policy, args.episodes_per_config,\n            args.output_dir, args.dry_run,\n        )\n    else:\n        from libero.libero import get_libero_path\n        bddl_dir = os.path.join(get_libero_path(\"bddl_files\"), BASE_TASK_SUITE)\n        tasks = find_base_tasks(bddl_dir, num_tasks=args.num_tasks)\n        if not tasks:\n            log.error(\"No base tasks found in %s\", bddl_dir)\n            sys.exit(1)\n        stats = collect_spatial(\n            policy, tasks, args.episodes_per_config,\n            args.output_dir, args.dry_run,\n        )\n\n    elapsed = time.time() - t0\n\n    total_size = sum(\n        os.path.getsize(f) for f in stats[\"saved_files\"] if os.path.exists(f)\n    )\n    log.info(\"=\" * 60)\n    log.info(\"Collection complete: %s\", args.perturbation_type)\n    log.info(\"  Total episodes:  %d\", stats[\"total\"])\n    log.info(\"  Successful:      %d\", stats[\"success\"])\n    log.info(\n        \"  Success rate:    %.1f%%\",\n        stats[\"success\"] / max(stats[\"total\"], 1) * 100,\n    )\n    log.info(\"  Files saved:     %d\", len(stats[\"saved_files\"]))\n    log.info(\"  Total size:      %.1f MB\", total_size / 1024 / 1024)\n    log.info(\"  Elapsed:         %.1f min\", elapsed / 60)\n    log.info(\"  Output dir:      %s\", args.output_dir)\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 746,
      "startLine": 1,
      "totalLines": 746
    }
  }
}
```

</details>

---


### Assistant

_source line 120_

<details><summary>Logged reasoning block</summary>

```text
The file looks good. Now I need to sync this to the server and do a dry-run. Let me first sync the file to the server, then run the dry-run.

Let me use ssh_execute to push the file to the server, then run the dry-run.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "88620eee-0c8a-41dc-b714-14d2c6d1f926",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U2V5haZ46yWzWZM7MnVjPW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10010,
      "cache_read_input_tokens": 48158,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10010
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

_source line 121_

文件修改完成。现在同步到服务器并 dry-run。先把修改后的脚本推送到服务器。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "24d6c310-aa71-4847-a6a3-827f629a5c89",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U2V5haZ46yWzWZM7MnVjPW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10010,
      "cache_read_input_tokens": 48158,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10010
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

_source line 122_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_016bQPakVsAk1L2GrQqeYzX7`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
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
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "ad03b420-9129-492e-b56a-bdb04d0c38ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U2V5haZ46yWzWZM7MnVjPW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10010,
      "cache_read_input_tokens": 48158,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10010
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

_source line 123 · 2026-05-15T17:52:37.810Z_

<details><summary>↩ Tool result · `toolu_016bQPakVsAk1L2GrQqeYzX7`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_execute"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_read_only"
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
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "42d5de9b-4ae8-48f9-be12-2826caf6b529",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__ssh_read_only"
    ],
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
    "total_deferred_tools": 23
  }
}
```

</details>

---


### Assistant

_source line 124_

<details><summary>Logged reasoning block</summary>

```text
Now I need to sync the modified file to the server. Let me read the file content and push it via ssh_execute.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "b772ab68-d05b-497b-8325-f712f2fd89b6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GdqY6QTQ8HuymbkywSjL6w",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 884,
      "cache_read_input_tokens": 58168,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 884
      },
      "output_tokens": 27,
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

_source line 125_

先把修改后的脚本推到服务器，再验证 `_add_N` 任务发现。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "673810ac-c650-4762-b4c5-249492966a65",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GdqY6QTQ8HuymbkywSjL6w",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 884,
      "cache_read_input_tokens": 58168,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 884
      },
      "output_tokens": 27,
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

_source line 126_

<details open><summary>🔧 Tool call — Bash · `toolu_01146oxTY99ZrT9denermXqv`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py | base64 -w0",
  "description": "Base64 encode the script for transfer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "ab4819c1-2d19-4ee4-8245-a55390fdb54d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GdqY6QTQ8HuymbkywSjL6w",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 884,
      "cache_read_input_tokens": 58168,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 884
      },
      "output_tokens": 27,
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

_source line 127 · 2026-05-15T17:52:43.153Z_

<details><summary>↩ Tool result · `toolu_01146oxTY99ZrT9denermXqv`</summary>

```text
&lt;persisted-output>
Output too large (34.8KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-meta-brain-lora-routing/cb7ab164-b336-4232-adb7-15a7c03a9fa7/tool-results/bfejf4c19.txt

Preview (first 2KB):
IiIiCkNvbGxlY3QgZXhwZXJ0IGRlbW9uc3RyYXRpb25zIGJ5IHJvbGxpbmcgb3V0IGZyb3plbiDPgOKCgCBpbiBwZXJ0dXJiZWQgTElCRVJPIGVudmlyb25tZW50cy4KCk9ubHkgc3VjY2Vzc2Z1bCBlcGlzb2RlcyBhcmUgc2F2ZWQuIFR3byBwZXJ0dXJiYXRpb24gdHlwZXMgYXJlIHN1cHBvcnRlZDoKICAtIHBoeXNpY2FsOiB2YXJ5IHJvYm90IGluaXRpYWwgc3RhdGUgKGluaXRfc3RhdGVzIGluZGV4IDEtNDkpCiAgLSBzcGF0aWFsOiAgTElCRVJPLVBsdXMgX2FkZF9OIGRpc3RyYWN0b3Igb2JqZWN0cyAoZGVmYXVsdCkgb3IgcGVydHVyYl9yZWdpb24gZmFsbGJhY2sKCk91dHB1dDogcGlja2xlIGZpbGVzIHdpdGggKG9ic2VydmF0aW9ucywgYWN0aW9ucywgbWV0YWRhdGEpIHBlciBlcGlzb2RlLgoKVXNhZ2U6CiAgICAjIFBoeXNpY2FsIHBlcnR1cmJhdGlvbiBkcnktcnVuCiAgICBDVURBX1ZJU0lCTEVfREVWSUNFUz0xIHB5dGhvbiBjb2xsZWN0X2V4cGVydF9kZW1vcy5weSBcCiAgICAgICAgLS1wZXJ0dXJiYXRpb25fdHlwZSBwaHlzaWNhbCAtLWRyeV9ydW4KCiAgICAjIFNwYXRpYWwgcGVydHVyYmF0aW9uIGRyeS1ydW4gKHVzZXMgX2FkZF9OIGJ5IGRlZmF1bHQpCiAgICBDVURBX1ZJU0lCTEVfREVWSUNFUz0xIHB5dGhvbiBjb2xsZWN0X2V4cGVydF9kZW1vcy5weSBcCiAgICAgICAgLS1wZXJ0dXJiYXRpb25fdHlwZSBzcGF0aWFsIC0tZHJ5X3J1bgoKICAgICMgU3BhdGlhbCB3aXRoIGxlZ2FjeSBwZXJ0dXJiX3JlZ2lvbiBtb2RlCiAgICBDVURBX1ZJU0lCTEVfREVWSUNFUz0xIHB5dGhvbiBjb2xsZWN0X2V4cGVydF9kZW1vcy5weSBcCiAgICAgICAgLS1wZXJ0dXJiYXRpb25fdHlwZSBzcGF0aWFsIC0tc3BhdGlhbF9tb2RlIHBlcnR1cmJfcmVnaW9uIC0tZHJ5X3J1bgoKICAgICMgRnVsbCBwaHlzaWNhbCBjb2xsZWN0aW9uCiAgICBDVURBX1ZJU0lCTEVfREVWSUNFUz0xIHB5dGhvbiBjb2xsZWN0X2V4cGVydF9kZW1vcy5weSBcCiAgICAgICAgLS1wZXJ0dXJiYXRpb25fdHlwZSBwaHlzaWNhbAoiIiIKCmltcG9ydCBhcmdwYXJzZQppbXBvcnQgY29sbGVjdGlvbnMKaW1wb3J0IGNvcHkKaW1wb3J0IGxvZ2dpbmcKaW1wb3J0IG1hdGgKaW1wb3J0IG9zCmltcG9ydCBwaWNrbGUKaW1wb3J0IHJhbmRvbQppbXBvcnQgcmUKaW1wb3J0IHN5cwppbXBvcnQgdGltZQppbXBvcnQgdHlwZXMKZnJvbSBwYXRobGliIGltcG9ydCBQYXRoCmZyb20gdHlwaW5nIGltcG9ydCBBbnkKCmltcG9ydCBudW1weSBhcyBucAppbXBvcnQgdG9yY2gKCmxvZyA9IGxvZ2dpbmcuZ2V0TG9nZ2VyKF9fbmFtZV9fKQoKIyAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KIyBDb25zdGFudHMKIyAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KCkxJQkVST19EVU1NWV9BQ1RJT04gPSBb
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "57c36e6c-d485-4f24-bc96-dc546cde8571",
  "tool_use_result": {
    "stdout": "[ATTACHMENT_DATA_REDACTED]",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false,
    "persistedOutputPath": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-meta-brain-lora-routing/cb7ab164-b336-4232-adb7-15a7c03a9fa7/tool-results/bfejf4c19.txt",
    "persistedOutputSize": 35616
  }
}
```

</details>

---


### Tool call

_source line 128_

<details open><summary>🔧 Tool call — Read · `toolu_01HEf16Q3JFcftn3KLTN8FQt`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-meta-brain-lora-routing/cb7ab164-b336-4232-adb7-15a7c03a9fa7/tool-results/bfejf4c19.txt",
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "d14a69bb-bbcf-4db5-a5c0-6f95943ae1be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EzMRrvMFZWmJ7Sb6KbX4CC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2054,
      "cache_read_input_tokens": 59052,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2054
      },
      "output_tokens": 65,
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

_source line 129 · 2026-05-15T17:52:47.794Z_

<details><summary>↩ Tool result · reported error · `toolu_01HEf16Q3JFcftn3KLTN8FQt`</summary>

```text
File content (28527 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "6dfbe442-ab06-434e-955b-dc28724281e1",
  "tool_use_result": "Error: File content (28527 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---


### Assistant

_source line 130_

<details><summary>Logged reasoning block</summary>

```text
The base64 output is too large. Let me use a different approach - write the file directly via ssh_execute using a heredoc, or better yet, use scp-like approach. Actually, let me just use ssh_execute to write the file with a cat heredoc.

Actually, let me try a different approach. I'll read the local file and use ssh_execute to write it on the server using python3 -c to write from base64.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "a9498fd2-8105-4aed-a098-f11eff5491c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BG1shjadbP61EwpDuUXafz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 211,
      "cache_read_input_tokens": 61106,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 211
      },
      "output_tokens": 9,
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

_source line 131_

Let me use a different approach - transfer the file in chunks via ssh_execute.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "f48e153a-0c36-4db7-b63f-200243e420b1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BG1shjadbP61EwpDuUXafz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 211,
      "cache_read_input_tokens": 61106,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 211
      },
      "output_tokens": 9,
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

_source line 132_

<details open><summary>🔧 Tool call — Bash · `toolu_01E1PgRMsNgaCw1F9c1cXMAv`</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py",
  "description": "Count lines in the modified script"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "92e97c8b-de8c-4de8-97e2-1915b7e3da33",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BG1shjadbP61EwpDuUXafz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 211,
      "cache_read_input_tokens": 61106,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 211
      },
      "output_tokens": 9,
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

_source line 133 · 2026-05-15T17:52:54.350Z_

<details><summary>↩ Tool result · `toolu_01E1PgRMsNgaCw1F9c1cXMAv`</summary>

```text
745 /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "b3f3e468-1e8c-4f52-9d65-0a65d8d83595",
  "tool_use_result": {
    "stdout": "745 /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 134_

<details open><summary>🔧 Tool call — Bash · `toolu_01KCBgVwEZdGDrqusHDKTPLA`</summary>

```json
{
  "command": "scp -o StrictHostKeyChecking=no /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py connect.westd.seetacloud.com:/root/meta_brain_lora_routing/phase1/collect_expert_demos.py",
  "description": "SCP the modified script to the server",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "049bc448-fac8-4181-b15a-4dfd6e378a43",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MivhVsD3M8vVWbVmo35vKQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 308,
      "cache_read_input_tokens": 61317,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 308
      },
      "output_tokens": 70,
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

_source line 135 · 2026-05-15T17:53:00.026Z_

<details><summary>↩ Tool result · reported error · `toolu_01KCBgVwEZdGDrqusHDKTPLA`</summary>

```text
Exit code 255
Warning: Permanently added 'connect.westd.seetacloud.com' (ED25519) to the list of known hosts.
ssh_askpass: exec(/usr/bin/ssh-askpass): No such file or directory
Permission denied, please try again.
ssh_askpass: exec(/usr/bin/ssh-askpass): No such file or directory
Permission denied, please try again.
ssh_askpass: exec(/usr/bin/ssh-askpass): No such file or directory
ubuntu@connect.westd.seetacloud.com: Permission denied ().
scp: Connection closed
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "9eb27a89-4bc2-4f0a-9e72-bee61db23955",
  "tool_use_result": "Error: Exit code 255\nWarning: Permanently added 'connect.westd.seetacloud.com' (ED25519) to the list of known hosts.\r\nssh_askpass: exec(/usr/bin/ssh-askpass): No such file or directory\r\nPermission denied, please try again.\r\nssh_askpass: exec(/usr/bin/ssh-askpass): No such file or directory\r\nPermission denied, please try again.\r\nssh_askpass: exec(/usr/bin/ssh-askpass): No such file or directory\r\nubuntu@connect.westd.seetacloud.com: Permission denied ().\r\nscp: Connection closed"
}
```

</details>

---


### Assistant

_source line 136_

<details><summary>Logged reasoning block</summary>

```text
Direct SCP doesn't work because we don't have the right SSH config for SCP. Let me use the MCP ssh_execute tool instead - I'll write the file via base64 decoding on the server.

Let me split the base64 content into manageable chunks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "42a5a386-a92f-4c2d-a2a1-981684c974e6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F6eEUZ12FiHHtHpEnKrjrL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 343,
      "cache_read_input_tokens": 61625,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 343
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

_source line 137_

SCP 不行，用 ssh_execute 通过 base64 传输。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "8c66451e-f982-41f6-a05f-213783d49ca4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F6eEUZ12FiHHtHpEnKrjrL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 343,
      "cache_read_input_tokens": 61625,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 343
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

_source line 138_

<details open><summary>🔧 Tool call — Bash · `toolu_01C5Ahh5Sb7xe6AMwCaaZPou`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py | base64 -w0 | wc -c",
  "description": "Check base64 size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "1dda1e65-e305-42d3-a27e-1e4ac0c3bbc2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F6eEUZ12FiHHtHpEnKrjrL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 343,
      "cache_read_input_tokens": 61625,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 343
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

_source line 139 · 2026-05-15T17:53:05.395Z_

<details><summary>↩ Tool result · `toolu_01C5Ahh5Sb7xe6AMwCaaZPou`</summary>

```text
35616
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "a2d31fb2-4026-459e-b637-ba8d6aad1b07",
  "tool_use_result": {
    "stdout": "35616",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 140_

<details open><summary>🔧 Tool call — Bash · `toolu_01FUhQcRg3GkKhTvfnC1XqKA`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py | base64 -w0 | head -c 18000",
  "description": "Get first half of base64"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "73a5eed7-9cd7-4d0b-8e00-b4b87b1d6126",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JWj1zkL8pEqJiMHKLqVfXj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 240,
      "cache_read_input_tokens": 61968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 240
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

_source line 141 · 2026-05-15T17:53:09.195Z_

<details><summary>↩ Tool result · `toolu_01FUhQcRg3GkKhTvfnC1XqKA`</summary>

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
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "9a83b050-1ac2-4fd5-8f39-9b6f76a0c37e",
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


### Tool call

_source line 142_

<details open><summary>🔧 Tool call — Bash · `toolu_01S2oh7eSEcs2BfYoWZLHizd`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase1/collect_expert_demos.py | base64 -w0 | tail -c +18001",
  "description": "Get second half of base64"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "87588eaa-495d-4ac6-bc61-41d75ced1135",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JWj1zkL8pEqJiMHKLqVfXj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 240,
      "cache_read_input_tokens": 61968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 240
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

_source line 143 · 2026-05-15T17:53:09.890Z_

<details><summary>↩ Tool result · `toolu_01S2oh7eSEcs2BfYoWZLHizd`</summary>

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
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "0ffa302a-a087-41e2-a97b-695084eb20d0",
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

_source line 144_

<details><summary>Logged reasoning block</summary>

```text
Let me get both halves and send them to the server via ssh_execute. I'll use python3 to decode base64 and write the file.

Actually, let me try a cleaner approach - write the file content through ssh_execute using a Python one-liner that decodes base64.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "cbec6d60-9603-4815-b00a-f547b0cab9b8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pnmekxf22u7DpFYk6FB8iW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 28931,
      "cache_read_input_tokens": 62208,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 28931
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

_source line 145_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_0137VdpUEh5QhW5s1c2KHkdG`</summary>

```json
{
  "server": "westd-34142",
  "account": "root",
  "command": "python3 -c \"\nimport base64, sys\n# Read base64 from stdin and write decoded file\ndata = sys.stdin.read()\nwith open('/root/meta_brain_lora_routing/phase1/collect_expert_demos.py', 'wb') as f:\n    f.write(base64.b64decode(data))\nprint('Written', len(base64.b64decode(data)), 'bytes')\n\" << 'ENDOFBASE64'\nIiIiCkNvbGxlY3QgZXhwZXJ0IGRlbW9uc3RyYXRpb25zIGJ5IHJvbGxpbmcgb3V0IGZyb3plbiDPgOKCgCBpbiBwZXJ0dXJiZWQgTElCRVJPIGVudmlyb25tZW50cy4KCk9ubHkgc3VjY2Vzc2Z1bCBlcGlzb2RlcyBhcmUgc2F2ZWQuIFR3byBwZXJ0dXJiYXRpb24gdHlwZXMgYXJlIHN1cHBvcnRlZDoKICAtIHBoeXNpY2FsOiB2YXJ5IHJvYm90IGluaXRpYWwgc3RhdGUgKGluaXRfc3RhdGVzIGluZGV4IDEtNDkpCiAgLSBzcGF0aWFsOiAgTElCRVJPLVBsdXMgX2FkZF9OIGRpc3RyYWN0b3Igb2JqZWN0cyAoZGVmYXVsdCkgb3IgcGVydHVyYl9yZWdpb24gZmFsbGJhY2sKCk91dHB1dDogcGlja2xlIGZpbGVzIHdpdGggKG9ic2VydmF0aW9ucywgYWN0aW9ucywgbWV0YWRhdGEpIHBlciBlcGlzb2RlLgoKVXNhZ2U6CiAgICAjIFBoeXNpY2FsIHBlcnR1cmJhdGlvbiBkcnktcnVuCiAgICBDVURBX1ZJU0lCTEVfREVWSUNFUz0xIHB5dGhvbiBjb2xsZWN0X2V4cGVydF9kZW1vcy5weSBcCiAgICAgICAgLS1wZXJ0dXJiYXRpb25fdHlwZSBwaHlzaWNhbCAtLWRyeV9ydW4KCiAgICAjIFNwYXRpYWwgcGVydHVyYmF0aW9uIGRyeS1ydW4gKHVzZXMgX2FkZF9OIGJ5IGRlZmF1bHQpCiAgICBDVURBX1ZJU0lCTEVfREVWSUNFUz0xIHB5dGhvbiBjb2xsZWN0X2V4cGVydF9kZW1vcy5weSBcCiAgICAgICAgLS1wZXJ0dXJiYXRpb25fdHlwZSBzcGF0aWFsIC0tZHJ5X3J1bgoKICAgICMgU3BhdGlhbCB3aXRoIGxlZ2FjeSBwZXJ0dXJiX3JlZ2lvbiBtb2RlCiAgICBDVURBX1ZJU0lCTEVfREVWSUNFUz0xIHB5dGhvbiBjb2xsZWN0X2V4cGVydF9kZW1vcy5weSBcCiAgICAgICAgLS1wZXJ0dXJiYXRpb25fdHlwZSBzcGF0aWFsIC0tc3BhdGlhbF9tb2RlIHBlcnR1cmJfcmVnaW9uIC0tZHJ5X3J1bgoKICAgICMgRnVsbCBwaHlzaWNhbCBjb2xsZWN0aW9uCiAgICBDVURBX1ZJU0lCTEVfREVWSUNFUz0xIHB5dGhvbiBjb2xsZWN0X2V4cGVydF9kZW1vcy5weSBcCiAgICAgICAgLS1wZXJ0dXJiYXRpb25fdHlwZSBwaHlzaWNhbAoiIiIKCmltcG9ydCBhcmdwYXJzZQppbXBvcnQgY29sbGVjdGlvbnMKaW1wb3J0IGNvcHkKaW1wb3J0IGxvZ2dpbmcKaW1wb3J0IG1hdGgKaW1wb3J0IG9zCmltcG9ydCBwaWNrbGUKaW1wb3J0IHJhbmRvbQppbXBvcnQgcmUKaW1wb3J0IHN5cwppbXBvcnQgdGltZQppbXBvcnQgdHlwZXMKZnJvbSBwYXRobGliIGltcG9ydCBQYXRoCmZyb20gdHlwaW5nIGltcG9ydCBBbnkKCmltcG9ydCBudW1weSBhcyBucAppbXBvcnQgdG9yY2gKCmxvZyA9IGxvZ2dpbmcuZ2V0TG9nZ2VyKF9fbmFtZV9fKQoKIyAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KIyBDb25zdGFudHMKIyAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KCkxJQkVST19EVU1NWV9BQ1RJT04gPSBbMC4wXSAqIDYgKyBbLTEuMF0KTElCRVJPX0VOVl9SRVNPTFVUSU9OID0gMjU2Ck1PREVMX0lOUFVUX1JFU09MVVRJT04gPSAyMjQKUkVQTEFOX1NURVBTID0gNQpOVU1fU1RFUFNfV0FJVCA9IDEwCk1BWF9TVEVQUyA9IDIyMCAgIyBsaWJlcm9fc3BhdGlhbCBkZWZhdWx0CgojIDEwIGJhc2UgdGFza3MgaW4gbGliZXJvX3NwYXRpYWwgKG5vIHBlcnR1cmJhdGlvbiBzdWZmaXgpCkJBU0VfVEFTS19TVUlURSA9ICJsaWJlcm9fc3BhdGlhbCIKCiMgU3BhdGlhbCBwZXJ0dXJiYXRpb24gZ3JpZDogMTAgY29uZmlndXJhdGlvbnMgd2l0aCB2YXJ5aW5nIFhZIHNoaWZ0cyBhbmQgeWF3CiMgTWFnbml0dWRlcyBjaG9zZW4gdG8gYmUgbm90aWNlYWJsZSBidXQgd2l0aGluIGZlYXNpYmxlIHJlYWNoIG9mIHRoZSByb2JvdC4KU1BBVElBTF9QRVJUVVJCQVRJT05fQ09ORklHUyA9IFsKICAgIHsiZGVsdGFfeHkiOiAoIDAuMDUsICAwLjAwKSwgImRlbHRhX2hhbGZfbGVuIjogMC4wLCAgImRlbHRhX3lhdyI6ICgwLjAsIDAuMCl9LAogICAgeyJkZWx0YV94eSI6ICgtMC4wNSwgIDAuMDApLCAiZGVsdGFfaGFsZl9sZW4iOiAwLjAsICAiZGVsdGFfeWF3IjogKDAuMCwgMC4wKX0sCiAgICB7ImRlbHRhX3h5IjogKCAwLjAwLCAgMC4wNSksICJkZWx0YV9oYWxmX2xlbiI6IDAuMCwgICJkZWx0YV95YXciOiAoMC4wLCAwLjApfSwKICAgIHsiZGVsdGFfeHkiOiAoIDAuMDAsIC0wLjA1KSwgImRlbHRhX2hhbGZfbGVuIjogMC4wLCAgImRlbHRhX3lhdyI6ICgwLjAsIDAuMCl9LAogICAgeyJkZWx0YV94eSI6ICggMC4wMywgIDAuMDMpLCAiZGVsdGFfaGFsZl9sZW4iOiAwLjAsICAiZGVsdGFfeWF3IjogKDAuMCwgMC4wKX0sCiAgICB7ImRlbHRhX3h5IjogKC0wLjAzLCAtMC4wMyksICJkZWx0YV9oYWxmX2xlbiI6IDAuMCwgICJkZWx0YV95YXciOiAoMC4wLCAwLjApfSwKICAgIHsiZGVsdGFfeHkiOiAoIDAuMDQsICAwLjAwKSwgImRlbHRhX2hhbGZfbGVuIjogMC4wMSwgImRlbHRhX3lhdyI6ICgwLjMsIDAuMCl9LAogICAgeyJkZWx0YV94eSI6ICgtMC4wNCwgIDAuMDApLCAiZGVsdGFfaGFsZl9sZW4iOiAwLjAxLCAiZGVsdGFfeWF3IjogKC0wLjMsIDAuMCl9LAogICAgeyJkZWx0YV94eSI6ICggMC4wMCwgIDAuMDQpLCAiZGVsdGFfaGFsZl9sZW4iOiAwLjAsICAiZGVsdGFfeWF3IjogKDAuMCwgMC4zKX0sCiAgICB7ImRlbHRhX3h5IjogKCAwLjAwLCAtMC4wNCksICJkZWx0YV9oYWxmX2xlbiI6IDAuMCwgICJkZWx0YV95YXciOiAoMC4wLCAtMC4zKX0sCl0KCgojIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQojIEdlb21ldHJ5IC8gaW1hZ2UgaGVscGVycyAoZnJvbSBsaWJlcm9faW50ZWdyYXRpb24ucHkpCiMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCgpkZWYgX3F1YXQyYXhpc2FuZ2xlKHF1YXQ6IG5wLm5kYXJyYXkpIC0+IG5wLm5kYXJyYXk6CiAgICAiIiJRdWF0ZXJuaW9uIFt4LHkseix3XSAtPiBheGlzLWFuZ2xlIFtheCxheSxhel0uIiIiCiAgICBxID0gbnAuYXNhcnJheShxdWF0LCBkdHlwZT1ucC5mbG9hdDY0KQogICAgbm9ybSA9IG5wLmxpbmFsZy5ub3JtKHEpCiAgICBpZiBub3JtIDwgMWUtODoKICAgICAgICByZXR1cm4gbnAuemVyb3MoMywgZHR5cGU9bnAuZmxvYXQzMikKICAgIHEgLz0gbm9ybQogICAgc2luX2hhbGYgPSBucC5saW5hbGcubm9ybShxWzozXSkKICAgIGlmIHNpbl9oYWxmIDwgMWUtODoKICAgICAgICByZXR1cm4gbnAuemVyb3MoMywgZHR5cGU9bnAuZmxvYXQzMikKICAgIGFuZ2xlID0gMi4wICogbWF0aC5hdGFuMihzaW5faGFsZiwgcVszXSkKICAgIGF4aXMgPSBxWzozXSAvIHNpbl9oYWxmCiAgICByZXR1cm4gKGF4aXMgKiBhbmdsZSkuYXN0eXBlKG5wLmZsb2F0MzIpCgoKZGVmIF9yZXNpemVfd2l0aF9wYWQoaW1nOiBucC5uZGFycmF5LCBzaXplOiBpbnQpIC0+IG5wLm5kYXJyYXk6CiAgICAiIiJSZXNpemUgaW1hZ2Ugd2l0aCBhc3BlY3QtcHJlc2VydmluZyBwYWRkaW5nIHRvIChzaXplLCBzaXplLCAzKSB1aW50OC4iIiIKICAgIHRyeToKICAgICAgICBmcm9tIG9wZW5waV9jbGllbnQuaW1hZ2VfdG9vbHMgaW1wb3J0IHJlc2l6ZV93aXRoX3BhZCwgY29udmVydF90b191aW50OAogICAgICAgIHJldHVybiBjb252ZXJ0X3RvX3VpbnQ4KHJlc2l6ZV93aXRoX3BhZChpbWcsIHNpemUsIHNpemUpKQogICAgZXhjZXB0IEltcG9ydEVycm9yOgogICAgICAgIGZyb20gUElMIGltcG9ydCBJbWFnZSBhcyBQSUxJbWFnZQogICAgICAgIGgsIHcgPSBpbWcuc2hhcGVbOjJdCiAgICAgICAgc2NhbGUgPSBtaW4oc2l6ZSAvIGgsIHNpemUgLyB3KQogICAgICAgIG5ld19oLCBuZXdfdyA9IGludChoICogc2NhbGUpLCBpbnQodyAqIHNjYWxlKQogICAgICAgIHJlc2l6ZWQgPSBucC5hcnJheSgKICAgICAgICAgICAgUElMSW1hZ2UuZnJvbWFycmF5KGltZykucmVzaXplKChuZXdfdywgbmV3X2gpLCBQSUxJbWFnZS5CSUxJTkVBUikKICAgICAgICApCiAgICAgICAgY2FudmFzID0gbnAuemVyb3MoKHNpemUsIHNpemUsIDMpLCBkdHlwZT1ucC51aW50OCkKICAgICAgICB5MCwgeDAgPSAoc2l6ZSAtIG5ld19oKSAvLyAyLCAoc2l6ZSAtIG5ld193KSAvLyAyCiAgICAgICAgY2FudmFzW3kwIDogeTAgKyBuZXdfaCwgeDAgOiB4MCArIG5ld193XSA9IHJlc2l6ZWQKICAgICAgICByZXR1cm4gY2FudmFzCgoKZGVmIG9ic190b19tb2RlbF9pbnB1dChvYnM6IGRpY3QsIHRhc2tfZGVzY3JpcHRpb246IHN0cikgLT4gZGljdDoKICAgICIiIkNvbnZlcnQgTElCRVJPIG9ic2VydmF0aW9uIHRvIHRoZSBkaWN0IGZvcm1hdCBleHBlY3RlZCBieSBwb2xpY3kuaW5mZXIoKS4iIiIKICAgIGJhc2VfaW1nID0gbnAuYXNjb250aWd1b3VzYXJyYXkob2JzWyJhZ2VudHZpZXdfaW1hZ2UiXVs6Oi0xLCA6Oi0xXSkKICAgIHdyaXN0X2ltZyA9IG5wLmFzY29udGlndW91c2FycmF5KG9ic1sicm9ib3QwX2V5ZV9pbl9oYW5kX2ltYWdlIl1bOjotMSwgOjotMV0pCgogICAgYmFzZV9pbWcgPSBfcmVzaXplX3dpdGhfcGFkKGJhc2VfaW1nLCBNT0RFTF9JTlBVVF9SRVNPTFVUSU9OKQogICAgd3Jpc3RfaW1nID0gX3Jlc2l6ZV93aXRoX3BhZCh3cmlzdF9pbWcsIE1PREVMX0lOUFVUX1JFU09MVVRJT04pCgogICAgc3RhdGUgPSBucC5jb25jYXRlbmF0ZShbCiAgICAgICAgb2JzWyJyb2JvdDBfZWVmX3BvcyJdLmFzdHlwZShucC5mbG9hdDMyKSwKICAgICAgICBfcXVhdDJheGlzYW5nbGUob2JzWyJyb2JvdDBfZWVmX3F1YXQiXSksCiAgICAgICAgb2JzWyJyb2JvdDBfZ3JpcHBlcl9xcG9zIl0uYXN0eXBlKG5wLmZsb2F0MzIpLAogICAgXSkKCiAgICByZXR1cm4gewogICAgICAgICJvYnNlcnZhdGlvbi9pbWFnZSI6IGJhc2VfaW1nLAogICAgICAgICJvYnNlcnZhdGlvbi93cmlzdF9pbWFnZSI6IHdyaXN0X2ltZywKICAgICAgICAib2JzZXJ2YXRpb24vc3RhdGUiOiBzdGF0ZSwKICAgICAgICAicHJvbXB0IjogdGFza19kZXNjcmlwdGlvbiwKICAgIH0KCgpkZWYgZXh0cmFjdF9vYnNfZm9yX3NhdmluZyhvYnM6IGRpY3QpIC0+IGRpY3Q6CiAgICAiIiJFeHRyYWN0IG9ic2VydmF0aW9uIGZpZWxkcyB0byBzYXZlIGluIGRlbW8gZGF0YSAoaW1hZ2VzIHN0b3JlZCBhcyB1aW50OCkuIiIiCiAgICByZXR1cm4gewogICAgICAgICJhZ2VudHZpZXdfaW1hZ2UiOiBvYnNbImFnZW50dmlld19pbWFnZSJdLmNvcHkoKSwKICAgICAgICAicm9ib3QwX2V5ZV9pbl9oYW5kX2ltYWdlIjogb2JzWyJyb2JvdDBfZXllX2luX2hhbmRfaW1hZ2UiXS5jb3B5KCksCiAgICAgICAgInJvYm90MF9lZWZfcG9zIjogb2JzWyJyb2JvdDBfZWVmX3BvcyJdLmFzdHlwZShucC5mbG9hdDMyKS5jb3B5KCksCiAgICAgICAgInJvYm90MF9lZWZfcXVhdCI6IG9ic1sicm9ib3QwX2VlZl9xdWF0Il0uYXN0eXBlKG5wLmZsb2F0MzIpLmNvcHkoKSwKICAgICAgICAicm9ib3QwX2dyaXBwZXJfcXBvcyI6IG9ic1sicm9ib3QwX2dyaXBwZXJfcXBvcyJdLmFzdHlwZShucC5mbG9hdDMyKS5jb3B5KCksCiAgICB9CgoKIyAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KIyBNb2RlbCBsb2FkaW5nCiMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCgpkZWYgX2Vuc3VyZV9vcGVucGlfaW1wb3J0cygpOgogICAgIiIiU3R1YiBvdXQgbGVyb2JvdCAodHJhaW5pbmctb25seSBkZXApIGJlZm9yZSBpbXBvcnRpbmcgT3BlblBJLiIiIgogICAgZm9yIG1vZCBpbiBbCiAgICAgICAgImxlcm9ib3QiLCAibGVyb2JvdC5jb21tb24iLCAibGVyb2JvdC5jb21tb24uZGF0YXNldHMiLAogICAgICAgICJsZXJvYm90LmNvbW1vbi5kYXRhc2V0cy5sZXJvYm90X2RhdGFzZXQiLAogICAgXToKICAgICAgICBpZiBtb2Qgbm90IGluIHN5cy5tb2R1bGVzOgogICAgICAgICAgICBzeXMubW9kdWxlc1ttb2RdID0gdHlwZXMuTW9kdWxlVHlwZShtb2QpCgoKZGVmIGxvYWRfcGkwX3BvbGljeShjaGVja3BvaW50X3BhdGg6IHN0ciwgZGV2aWNlOiBzdHIpIC0+IG9iamVjdDoKICAgICIiIkxvYWQgcGkwIHBvbGljeSB2aWEgT3BlblBJLiBSZXR1cm5zIHRoZSBQb2xpY3kgb2JqZWN0IGZvciBpbmZlcmVuY2UuIiIiCiAgICBfZW5zdXJlX29wZW5waV9pbXBvcnRzKCkKICAgIGZyb20gb3BlbnBpLnRyYWluaW5nIGltcG9ydCBjb25maWcgYXMgX2NvbmZpZwogICAgZnJvbSBvcGVucGkucG9saWNpZXMgaW1wb3J0IHBvbGljeV9jb25maWcKCiAgICB0cmFpbl9jb25maWcgPSBfY29uZmlnLmdldF9jb25maWcoInBpMF9saWJlcm8iKQogICAgcG9saWN5ID0gcG9saWN5X2NvbmZpZy5jcmVhdGVfdHJhaW5lZF9wb2xpY3koCiAgICAgICAgdHJhaW5fY29uZmlnLCBjaGVja3BvaW50X3BhdGgsIHB5dG9yY2hfZGV2aWNlPWRldmljZQogICAgKQogICAgbG9nLmluZm8oIkxvYWRlZCBwaTAgcG9saWN5IG9uICVzIiwgZGV2aWNlKQogICAgcmV0dXJuIHBvbGljeQoKCiMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCiMgVGFzayBkaXNjb3ZlcnkKIyAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KCmRlZiBmaW5kX2Jhc2VfdGFza3MoYmRkbF9kaXI6IHN0ciwgbnVtX3Rhc2tzOiBpbnQgPSAxMCkgLT4gbGlzdFtkaWN0XToKICAgICIiIkZpbmQgYmFzZSAodW5wZXJ0dXJiZWQpIEJEREwgZmlsZXMgaW4gbGliZXJvX3NwYXRpYWwuCgogICAgUmV0dXJucyBsaXN0IG9mIGRpY3RzIHdpdGgga2V5czogbmFtZSwgYmRkbF9wYXRoLCBpbml0X3N0YXRlc19wYXRoLgogICAgIiIiCiAgICBhbGxfZmlsZXMgPSBbZiBmb3IgZiBpbiBvcy5saXN0ZGlyKGJkZGxfZGlyKSBpZiBmLmVuZHN3aXRoKCIuYmRkbCIpXQoKICAgIGJhc2VfbmFtZXMgPSBbXQogICAgZm9yIGYgaW4gc29ydGVkKGFsbF9maWxlcyk6CiAgICAgICAgbmFtZSA9IGYucmVwbGFjZSgiLmJkZGwiLCAiIikKICAgICAgICAjIFNraXAgYW55IGZpbGUgd2l0aCBwZXJ0dXJiYXRpb24gc3VmZml4ZXMKICAgICAgICBpZiByZS5zZWFyY2goCiAgICAgICAgICAgIHIiKF9hZGRfXGQrfF90YWJsZV9cZCt8X3RiX1xkK3xfbGlnaHRfXGQrfF9sYW5ndWFnZV9cZCsiCiAgICAgICAgICAgIHIifF92aWV3X3xfbm9pc2VffF9sZXZlbFxkK3wgY29weSkiLAogICAgICAgICAgICBuYW1lLAogICAgICAgICk6CiAgICAgICAgICAgIGNvbnRpbnVlCiAgICAgICAgYmFzZV9uYW1lcy5hcHBlbmQobmFtZSkKCiAgICBpbml0X2RpciA9IGJkZGxfZGlyLnJlcGxhY2UoImJkZGxfZmlsZXMiLCAiaW5pdF9maWxlcyIpCiAgICB0YXNrcyA9IFtdCiAgICBmb3IgbmFtZSBpbiBiYXNlX25hbWVzWzpudW1fdGFza3NdOgogICAgICAgIGJkZGxfcGF0aCA9IG9zLnBhdGguam9pbihiZGRsX2RpciwgZiJ7bmFtZX0uYmRkbCIpCiAgICAgICAgaW5pdF9wYXRoID0gb3MucGF0aC5qb2luKGluaXRfZGlyLCBmIntuYW1lfS5wcnVuZWRfaW5pdCIpCiAgICAgICAgaWYgbm90IG9zLnBhdGguZXhpc3RzKGluaXRfcGF0aCk6CiAgICAgICAgICAgIGxvZy53YXJuaW5nKCJpbml0X3N0YXRlcyBub3QgZm91bmQgZm9yICVzLCBza2lwcGluZyIsIG5hbWUpCiAgICAgICAgICAgIGNvbnRpbnVlCiAgICAgICAgdGFza3MuYXBwZW5kKHsKICAgICAgICAgICAgIm5hbWUiOiBuYW1lLAogICAgICAgICAgICAiYmRkbF9wYXRoIjogYmRkbF9wYXRoLAogICAgICAgICAgICAiaW5pdF9zdGF0ZXNfcGF0aCI6IGluaXRfcGF0aCwKICAgICAgICB9KQoKICAgIGxvZy5pbmZvKCJGb3VuZCAlZCBiYXNlIHRhc2tzIiwgbGVuKHRhc2tzKSkKICAgIHJldHVybiB0YXNrcwoKCmRlZiBnZXRfdGFza19sYW5ndWFnZShiZGRsX3BhdGg6IHN0cikgLT4gc3RyOgogICAgIiIiRXh0cmFjdCBsYW5ndWFnZSBpbnN0cnVjdGlvbiBmcm9tIGEgQkRETCBmaWxlLiIiIgogICAgZnJvbSBsaWJlcm8ubGliZXJvLmVudnMuYmRkbF91dGlscyBpbXBvcnQgZ2V0X3Byb2JsZW1faW5mbwogICAgaW5mbyA9IGdldF9wcm9ibGVtX2luZm8oYmRkbF9wYXRoKQogICAgcmV0dXJuIGluZm9bImxhbmd1YWdlX2luc3RydWN0aW9uIl0KCgpkZWYgZGlzY292ZXJfYWRkX25fdGFza3ModGFza19zdWl0ZTogc3RyID0gQkFTRV9UQVNLX1NVSVRFKSAtPiBsaXN0W2RpY3RdOgogICAgIiIiRGlzY292ZXIgYWxsIF9hZGRfTiAoZGlzdHJhY3Rvci1vYmplY3QpIHRhc2tzIGZyb20gdGhlIExJQkVSTy1QbHVzIGJlbmNobWFyay4KCiAgICBSZXR1cm5zIGxpc3Qgb2YgZGljdHMgd2l0aDogaWR4LCBuYW1lLCBsYW5ndWFnZSwgYmRkbF9wYXRoLCBpbml0X3N0YXRlcy4KICAgICIiIgogICAgZnJvbSBsaWJlcm8ubGliZXJvIGltcG9ydCBiZW5jaG1hcmssIGdldF9saWJlcm9fcGF0aAogICAgYmVuY2htYXJrX2RpY3QgPSBiZW5jaG1hcmsuZ2V0X2JlbmNobWFya19kaWN0KCkKICAgIHN1aXRlID0gYmVuY2htYXJrX2RpY3RbdGFza19zdWl0ZV0oKQogICAgYmRkbF9yb290ID0gUGF0aChnZXRfbGliZXJvX3BhdGgoImJkZGxfZmlsZXMiKSkKCiAgICB0YXNrcyA9IFtdCiAgICBza2lwcGVkID0gMAogICAgZm9yIGkgaW4gcmFuZ2Uoc3VpdGUubl90YXNrcyk6CiAgICAgICAgdGFzayA9IHN1aXRlLmdldF90YXNrKGkpCiAgICAgICAgbmFtZSA9IGdldGF0dHIodGFzaywgIm5hbWUiLCAiIikgb3IgZ2V0YXR0cih0YXNrLCAiYmRkbF9maWxlIiwgIiIpCiAgICAgICAgaWYgbm90IHJlLnNlYXJjaChyIl9hZGRfXGQrJCIsIG5hbWUucmVwbGFjZSgiLmJkZGwiLCAiIikpOgogICAgICAgICAgICBjb250aW51ZQoKICAgICAgICBiZGRsX3BhdGggPSBzdHIoYmRkbF9yb290IC8gdGFzay5wcm9ibGVtX2ZvbGRlciAvIHRhc2suYmRkbF9maWxlKQogICAgICAgIGlmIG5vdCBvcy5wYXRoLmV4aXN0cyhiZGRsX3BhdGgpOgogICAgICAgICAgICBsb2cud2FybmluZygiQkRETCBub3QgZm91bmQsIHNraXBwaW5nOiAlcyIsIGJkZGxfcGF0aCkKICAgICAgICAgICAgc2tpcHBlZCArPSAxCiAgICAgICAgICAgIGNvbnRpbnVlCgogICAgICAgIHRyeToKICAgICAgICAgICAgaW5pdF9zdGF0ZXMgPSBzdWl0ZS5nZXRfdGFza19pbml0X3N0YXRlcyhpKQogICAgICAgIGV4Y2VwdCBFeGNlcHRpb246CiAgICAgICAgICAgIGxvZy53YXJuaW5nKCJpbml0X3N0YXRlcyBmYWlsZWQgZm9yICVzLCBza2lwcGluZyIsIG5hbWUpCiAgICAgICAgICAgIHNraXBwZWQgKz0gMQogICAgICAgICAgICBjb250aW51ZQoKICAgICAgICB0YXNrcy5hcHBlbmQoewogICAgICAgICAgICAiaWR4IjogaSwKICAgICAgICAgICAgIm5hbWUiOiBuYW1lLnJlcGxhY2UoIi5iZGRsIiwgIiIpLAogICAgICAgICAgICAibGFuZ3VhZ2UiOiB0YXNrLmxhbmd1YWdlLAogICAgICAgICAgICAiYmRkbF9wYXRoIjogYmRkbF9wYXRoLAogICAgICAgICAgICAiaW5pdF9zdGF0ZXMiOiBpbml0X3N0YXRlcywKICAgICAgICB9KQoKICAgIGxvZy5pbmZvKAogICAgICAgICJEaXNjb3ZlcmVkICVkIF9hZGRfTiB0YXNrcyAoJWQgc2tpcHBlZCkgZnJvbSAlcyIsCiAgICAgICAgbGVuKHRhc2tzKSwgc2tpcHBlZCwgdGFza19zdWl0ZSwKICAgICkKICAgIHJldHVybiB0YXNrcwoKCiMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCiMgRW52aXJvbm1lbnQgY3JlYXRpb24KIyAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KCmRlZiBjcmVhdGVfZW52KGJkZGxfcGF0aDogc3RyKSAtPiBvYmplY3Q6CiAgICAiIiJDcmVhdGUgYSBMSUJFUk8gT2ZmU2NyZWVuUmVuZGVyRW52IGZyb20gYSBCRERMIGZpbGUuIiIiCiAgICBmcm9tIGxpYmVyby5saWJlcm8uZW52cyBpbXBvcnQgT2ZmU2NyZWVuUmVuZGVyRW52CiAgICBlbnYgPSBPZmZTY3JlZW5SZW5kZXJFbnYoCiAgICAgICAgYmRkbF9maWxlX25hbWU9YmRkbF9wYXRoLAogICAgICAgIGNhbWVyYV9oZWlnaHRzPUxJQkVST19FTlZfUkVTT0xVVElPTiwKICAgICAgICBjYW1lcmFfd2lkdGhzPUxJQkVST19FTlZfUkVTT0xVVElPTiwKICAgICkKICAgIHJldHVybiBlbnYKCgpkZWYgY3JlYXRlX3NwYXRpYWxfYmRkbCgKICAgIGJhc2VfYmRkbF9wYXRoOiBzdHIsCiAgICBwZXJ0dXJiYXRpb25fY29uZmlnOiBkaWN0LAogICAgb3V0cHV0X2Rpcjogc3RyLAopIC0+IHN0cjoKICAgICIiIkNyZWF0ZSBhIHBlcnR1cmJlZCBCRERMIGZpbGUgYnkgYXBwbHlpbmcgc3BhdGlhbCBwZXJ0dXJiYXRpb24gdG8gYWxsIHJlZ2lvbnMuCgogICAgUmV0dXJucyB0aGUgcGF0aCB0byB0aGUgbmV3IEJEREwgZmlsZS4KICAgICIiIgogICAgc3lzLnBhdGguaW5zZXJ0KDAsICIvcm9vdC9MSUJFUk8tcGx1cy9saWJlcm8iKQogICAgZnJvbSBsaWJlcm8ucmFuZG9taXplci5iZGRsX29wZXJhdG9ycyBpbXBvcnQgKAogICAgICAgIGxvYWRfYmRkbF9maWxlLAogICAgICAgIHNhdmVfYmRkbF9maWxlLAogICAgICAgIHBlcnR1cmJfcmVnaW9uX2luZm8sCiAgICApCgogICAgc3BlYyA9IGxvYWRfYmRkbF9maWxlKGJhc2VfYmRkbF9wYXRoKQogICAgZGVsdGFfeHkgPSBwZXJ0dXJiYXRpb25fY29uZmlnWyJkZWx0YV94eSJdCiAgICBkZWx0YV9oYWxmID0gcGVydHVyYmF0aW9uX2NvbmZpZ1siZGVsdGFfaGFsZl9sZW4iXQogICAgZGVsdGFfeWF3ID0gcGVydHVyYmF0aW9uX2NvbmZpZ1siZGVsdGFfeWF3Il0KCiAgICBmb3IgaSBpbiByYW5nZShsZW4oc3BlYy5yZWdpb25faW5mb3MpKToKICAgICAgICBzcGVjLnJlZ2lvbl9pbmZvc1tpXSA9IHBlcnR1cmJfcmVnaW9uX2luZm8oCiAgICAgICAgICAgIHNwZWMucmVnaW9uX2luZm9zW2ldLAogICAgICAgICAgICBkZWx0YV9yZWdpb25fY2VudHJvaWRfeHk9ZGVsdGFfeHksCiAgICAgICAgICAgIGRlbHRhX3JlZ2lvbl9oYWxmX2xlbj1kZWx0YV9oYWxmLAogICAgICAgICAgICBkZWx0YV95YXdfcm90YXRpb249ZGVsdGFfeWF3LAogICAgICAgICkKCiAgICBvcy5tYWtlZGlycyhvdXRwdXRfZGlyLCBleGlzdF9vaz1UcnVlKQogICAgYmFzZV9uYW1lID0gUGF0aChiYXNlX2JkZGxfcGF0aCkuc3RlbQogICAgZHgsIGR5ID0gZGVsdGFfeHkKICAgIGZpbGVuYW1lID0gZiJ7YmFzZV9uYW1lfV9zcGF0aWFsX2R4e2R4Oi4yZn1fZHl7ZHk6LjJmfS5iZGRsIgogICAgXywgZmlsZXBhdGggPSBzYXZlX2JkZGxfZmlsZShzcGVjLCBiZGRsX2ZpbGVuYW1lPWZpbGVuYW1lLCBiZGRsX2RpcnBhdGg9b3V0cHV0X2RpcikKICAgIHJldHVybiBmaWxlcGF0aAoKCiMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCiMgRXBpc29kZSByb2xsb3V0CiMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCgpkZWYgcm9sbG91dF9lcGlzb2RlKAogICAgcG9saWN5OiBvYmplY3QsCiAgICBlbnY6IG9iamVjdCwKICAgIHRhc2tfZGVzY3JpcHRpb246IHN0ciwKICAgIGluaXRfc3RhdGVzOiBucC5uZGFycmF5LAogICAgaW5pdF9zdGF0ZV9pZHg6IGludCwKICAgIHNlZWQ6IGludCwKKSAtPiBkaWN0W3N0ciwgQW55XToKICAgICIiIlJ1biBvbmUgZXBpc29kZSwgY29sbGVjdGluZyAob2JzLCBhY3Rpb24pIHBhaXJzLgoKICAgIFJldHVybnMgZGljdCB3aXRoIG9ic2VydmF0aW9ucywgYWN0aW9ucywgc3VjY2VzcywgbnVtX3N0ZXBzLgogICAgIiIiCiAgICBlbnYuc2VlZChzZWVkKQogICAgb2JzID0gZW52LnNldF9pbml0X3N0YXRlKGluaXRfc3RhdGVzW2luaXRfc3RhdGVfaWR4XSkKCiAgICBmb3IgXyBpbiByYW5nZShOVU1fU1RFUFNfV0FJVCk6CiAgICAgICAgb2JzLCBfLCBfLCBfID0gZW52LnN0ZXAoTElCRVJPX0RVTU1ZX0FDVElPTikKCiAgICBhbGxfb2JzID0gW2V4dHJhY3Rfb2JzX2Zvcl9zYXZpbmcob2JzKV0KICAgIGFsbF9hY3Rpb25zID0gW10KICAgIGFjdGlvbl9wbGFuID0gY29sbGVjdGlvbnMuZGVxdWUoKQogICAgc3RlcCA9IDAKICAgIHN1Y2Nlc3MgPSBGYWxzZQogICAgZG9uZSA9IEZhbHNlCgogICAgd2hpbGUgbm90IGRvbmUgYW5kIHN0ZXAgPCBNQVhfU1RFUFM6CiAgICAgICAgaWYgbGVuKGFjdGlvbl9wbGFuKSA9PSAwOgogICAgICAgICAgICBvYnNfZGljdCA9IG9ic190b19tb2RlbF9pbnB1dChvYnMsIHRhc2tfZGVzY3JpcHRpb24pCiAgICAgICAgICAgIHJlc3VsdCA9IHBvbGljeS5pbmZlcihvYnNfZGljdCkKICAgICAgICAgICAgYWN0aW9uX2NodW5rID0gcmVzdWx0WyJhY3Rpb25zIl0KICAgICAgICAgICAgYWN0aW9uX3BsYW4uZXh0ZW5kKGFjdGlvbl9jaHVua1s6UkVQTEFOX1NURVBTXSkKCiAgICAgICAgYWN0aW9uID0gYWN0aW9uX3BsYW4ucG9wbGVmdCgpCiAgICAgICAgaWYgaXNpbnN0YW5jZShhY3Rpb24sIHRvcmNoLlRlbnNvcik6CiAgICAgICAgICAgIGFjdGlvbiA9IGFjdGlvbi5jcHUoKS5udW1weSgpCiAgICAgICAgYWN0aW9uX25wID0gbnAuYXNhcnJheShhY3Rpb24sIGR0eXBlPW5wLmZsb2F0MzIpCgogICAgICAgIG9icywgcmV3YXJkLCBkb25lLCBpbmZvID0gZW52LnN0ZXAoCiAgICAgICAgICAgIGFjdGlvbl9ucC50b2xpc3QoKSBpZiBoYXNhdHRyKGFjdGlvbl9ucCwgInRvbGlzdCIpIGVsc2UgbGlzdChhY3Rpb25fbnApCiAgICAgICAgKQogICAgICAgIHN0ZXAgKz0gMQoKICAgICAgICBhbGxfb2JzLmFwcGVuZChleHRyYWN0X29ic19mb3Jfc2F2aW5nKG9icykpCiAgICAgICAgYWxsX2FjdGlvbnMuYXBwZW5kKGFjdGlvbl9ucCkKCiAgICAgICAgaWYgZG9uZSBvciByZXdhcmQgPiAwOgogICAgICAgICAgICBzdWNjZXNzID0gaW5mby5nZXQoInN1Y2Nlc3MiLCByZXdhcmQgPiAwKQoKICAgIHJldHVybiB7CiAgICAgICAgIm9ic2VydmF0aW9ucyI6IGFsbF9vYnMsCiAgICAgICAgImFjdGlvbnMiOiBucC5zdGFjayhhbGxfYWN0aW9ucykgaWYgYWxsX2FjdGlvbnMgZWxzZSBucC56ZXJvcygoMCwgNykpLAogICAgICAgICJzdWNjZXNzIjogc3VjY2VzcywKICAgICAgICAibnVtX3N0ZXBzIjogc3RlcCwKICAgIH0KCgojIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQojIENvbGxlY3Rpb24gbG9vcHMKIyAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KCmRlZiBjb2xsZWN0X3BoeXNpY2FsKAogICAgcG9saWN5OiBvYmplY3QsCiAgICB0YXNrczogbGlzdFtkaWN0XSwKICAgIGVwaXNvZGVzX3Blcl9jb25maWc6IGludCwKICAgIG91dHB1dF9kaXI6IHN0ciwKICAgIGRyeV9ydW46IGJvb2wsCikgLT4gZGljdDoKICAgICIiIkNvbGxlY3QgZXhwZXJ0IGRlbW9zIHdpdGggcGh5c2ljYWwgKHJvYm90IGluaXRpYWwgc3RhdGUpIHBlcnR1cmJhdGlvbi4KCiAgICBVc2VzIGluaXRfc3RhdGVzIGluZGljZXMgMS00OSAoaW5kZXggMCBpcyBub21pbmFsKS4KICAgICIiIgogICAgb3MubWFrZWRpcnMob3V0cHV0X2RpciwgZXhpc3Rfb2s9VHJ1ZSkKICAgIHN0YXRzID0geyJ0b3RhbCI6IDAsICJzdWNjZXNzIjogMCwgInNhdmVkX2ZpbGVzIjogW119CgogICAgaW5pdF9zdGF0ZV9pbmRpY2VzID0gbGlzdChyYW5nZSgxLCA1MCkpICAjIDQ5IHBlcnR1cmJlZCBzdGF0ZXMKICAgIGlmIGRyeV9ydW46CiAgICAgICAgdGFza3MgPSB0YXNrc1s6MV0KICAgICAgICBpbml0X3N0YXRlX2luZGljZXMgPSBbMV0KICAgICAgICBlcGlzb2Rlc19wZXJfY29uZmlnID0gMQoKICAgIGZvciB0YXNrX2luZm8gaW4gdGFza3M6CiAgICAgICAgdGFza19uYW1lID0gdGFza19pbmZvWyJuYW1lIl0KICAgICAgICBpbml0X3N0YXRlcyA9IHRvcmNoLmxvYWQodGFza19pbmZvWyJpbml0X3N0YXRlc19wYXRoIl0sIHdlaWdodHNfb25seT1GYWxzZSkKICAgICAgICBsYW5ndWFnZSA9IGdldF90YXNrX2xhbmd1YWdlKHRhc2tfaW5mb1siYmRkbF9wYXRoIl0pCiAgICAgICAgbG9nLmluZm8oIlRhc2s6ICVzICglZCBpbml0X3N0YXRlcyBhdmFpbGFibGUpIiwgdGFza19uYW1lLCBsZW4oaW5pdF9zdGF0ZXMpKQoKICAgICAgICBmb3IgaWR4IGluIGluaXRfc3RhdGVfaW5kaWNlczoKICAgICAgICAgICAgaWYgaWR4ID49IGxlbihpbml0X3N0YXRlcyk6CiAgICAgICAgICAgICAgICBjb250aW51ZQoKICAgICAgICAgICAgZm9yIGVwIGluIHJhbmdlKGVwaXNvZGVzX3Blcl9jb25maWcpOgogICAgICAgICAgICAgICAgc2VlZCA9IGhhc2goKHRhc2tfbmFtZSwgaWR4LCBlcCkpICUgKDIqKjMxKQogICAgICAgICAgICAgICAgc3RhdHNbInRvdGFsIl0gKz0gMQoKICAgICAgICAgICAgICAgIHRyeToKICAgICAgICAgICAgICAgICAgICBlbnYgPSBjcmVhdGVfZW52KHRhc2tfaW5mb1siYmRkbF9wYXRoIl0pCiAgICAgICAgICAgICAgICAgICAgcmVzdWx0ID0gcm9sbG91dF9lcGlzb2RlKAogICAgICAgICAgICAgICAgICAgICAgICBwb2xpY3ksIGVudiwgbGFuZ3VhZ2UsIGluaXRfc3RhdGVzLCBpZHgsIHNlZWQKICAgICAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAgICAgZW52LmNsb3NlKCkKICAgICAgICAgICAgICAgIGV4Y2VwdCBFeGNlcHRpb246CiAgICAgICAgICAgICAgICAgICAgbG9nLmV4Y2VwdGlvbigKICAgICAgICAgICAgICAgICAgICAgICAgIkVwaXNvZGUgZmFpbGVkOiB0YXNrPSVzIGlkeD0lZCBlcD0lZCIsIHRhc2tfbmFtZSwgaWR4LCBlcAogICAgICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgICAgICBjb250aW51ZQoKICAgICAgICAgICAgICAgIGlmIHJlc3VsdFsic3VjY2VzcyJdOgogICAgICAgICAgICAgICAgICAgIHN0YXRzWyJzdWNjZXNzIl0gKz0gMQogICAgICAgICAgICAgICAgICAgIGRlbW8gPSB7CiAgICAgICAgICAgICAgICAgICAgICAgICJvYnNlcnZhdGlvbnMiOiByZXN1bHRbIm9ic2VydmF0aW9ucyJdLAogICAgICAgICAgICAgICAgICAgICAgICAiYWN0aW9ucyI6IHJlc3VsdFsiYWN0aW9ucyJdLAogICAgICAgICAgICAgICAgICAgICAgICAidGFza19uYW1lIjogdGFza19uYW1lLAogICAgICAgICAgICAgICAgICAgICAgICAicGVydHVyYmF0aW9uX2NvbmZpZyI6IHsKICAgICAgICAgICAgICAgICAgICAgICAgICAgICJ0eXBlIjogInBoeXNpY2FsIiwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICJpbml0X3N0YXRlX2lkeCI6IGlkeCwKICAgICAgICAgICAgICAgICAgICAgICAgfSwKICAgICAgICAgICAgICAgICAgICAgICAgInN1Y2Nlc3MiOiBUcnVlLAogICAgICAgICAgICAgICAgICAgICAgICAibnVtX3N0ZXBzIjogcmVzdWx0WyJudW1fc3RlcHMiXSwKICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICAgICAgZm5hbWUgPSBmInt0YXNrX25hbWV9X2luaXRzdGF0ZXtpZHh9X2Vwe2VwfS5wa2wiCiAgICAgICAgICAgICAgICAgICAgZnBhdGggPSBvcy5wYXRoLmpvaW4ob3V0cHV0X2RpciwgZm5hbWUpCiAgICAgICAgICAgICAgICAgICAgd2l0aCBvcGVuKGZwYXRoLCAid2IiKSBhcyBmOgogICAgICAgICAgICAgICAgICAgICAgICBwaWNrbGUuZHVtcChkZW1vLCBmLCBwcm90b2NvbD1waWNrbGUuSElHSEVTVF9QUk9UT0NPTCkKICAgICAgICAgICAgICAgICAgICBzdGF0c1sic2F2ZWRfZmlsZXMiXS5hcHBlbmQoZnBhdGgpCgogICAgICAgICAgICAgICAgcmF0ZSA9IHN0YXRzWyJzdWNjZXNzIl0gLyBzdGF0c1sidG90YWwiXSAqIDEwMAogICAgICAgICAgICAgICAgbG9nLmluZm8oCiAgICAgICAgICAgICAgICAgICAgIltwaHlzaWNhbF0gdGFzaz0lcyBpZHg9JWQgZXA9JWQgfCAlcyB8ICIKICAgICAgICAgICAgICAgICAgICAiY3VtdWxhdGl2ZSAlZC8lZCAoJS4xZiUlKSIsCiAgICAgICAgICAgICAgICAgICAgdGFza19uYW1lLCBpZHgsIGVwLAogICAgICAgICAgICAgICAgICAgICJTVUNDRVNTIiBpZiByZXN1bHRbInN1Y2Nlc3MiXSBlbHNlICJGQUlMIiwKICAgICAgICAgICAgICAgICAgICBzdGF0c1sic3VjY2VzcyJdLCBzdGF0c1sidG90YWwiXSwgcmF0ZSwKICAgICAgICAgICAgICAgICkKCiAgICByZXR1cm4gc3RhdHMKCgpkZWYgY29sbGVjdF9zcGF0aWFsKAogICAgcG9saWN5OiBvYmplY3QsCiAgICB0YXNrczogbGlzdFtkaWN0XSwKICAgIGVwaXNvZGVzX3Blcl9jb25maWc6IGludCwKICAgIG91dHB1dF9kaXI6IHN0ciwKICAgIGRyeV9ydW46IGJvb2wsCikgLT4gZGljdDoKICAgICIiIkNvbGxlY3QgZXhwZXJ0IGRlbW9zIHdpdGggc3BhdGlhbCAob2JqZWN0cyBsYXlvdXQpIHBlcnR1cmJhdGlvbi4KCiAgICBBcHBsaWVzIDEwIHByZWRlZmluZWQgc3BhdGlhbCBwZXJ0dXJiYXRpb24gY29uZmlncyB0byBlYWNoIGJhc2UgdGFzay4KICAgICIiIgogICAgb3MubWFrZWRpcnMob3V0cHV0X2RpciwgZXhpc3Rfb2s9VHJ1ZSkKICAgIHRtcF9iZGRsX2RpciA9IG9zLnBhdGguam9pbihvdXRwdXRfZGlyLCAiX3RtcF9iZGRsIikKICAgIG9zLm1ha2VkaXJzKHRtcF9iZGRsX2RpciwgZXhpc3Rfb2s9VHJ1ZSkKICAgIHN0YXRzID0geyJ0b3RhbCI6IDAsICJzdWNjZXNzIjogMCwgInNhdmVkX2ZpbGVzIjogW119CgogICAgY29uZmlncyA9IFNQQVRJQUxfUEVSVFVSQkFUSU9OX0NPTkZJR1MKICAgIGlmIGRyeV9ydW46CiAgICAgICAgdGFza3MgPSB0YXNrc1s6MV0KICAgICAgICBjb25maWdzID0gY29uZmlnc1s6MV0KICAgICAgICBlcGlzb2Rlc19wZXJfY29uZmlnID0gMQoKICAgIGZvciB0YXNrX2luZm8gaW4gdGFza3M6CiAgICAgICAgdGFza19uYW1lID0gdGFza19pbmZvWyJuYW1lIl0KICAgICAgICBpbml0X3N0YXRlcyA9IHRvcmNoLmxvYWQodGFza19pbmZvWyJpbml0X3N0YXRlc19wYXRoIl0sIHdlaWdodHNfb25seT1GYWxzZSkKICAgICAgICBsb2cuaW5mbygiVGFzazogJXMiLCB0YXNrX25hbWUpCgogICAgICAgIGZvciBjZmdfaWR4LCBjZmcgaW4gZW51bWVyYXRlKGNvbmZpZ3MpOgogICAgICAgICAgICB0cnk6CiAgICAgICAgICAgICAgICBwZXJ0dXJiZWRfYmRkbCA9IGNyZWF0ZV9zcGF0aWFsX2JkZGwoCiAgICAgICAgICAgICAgICAgICAgdGFza19pbmZvWyJiZGRsX3BhdGgiXSwgY2ZnLCB0bXBfYmRkbF9kaXIKICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgIGxhbmd1YWdlID0gZ2V0X3Rhc2tfbGFuZ3VhZ2UocGVydHVyYmVkX2JkZGwpCiAgICAgICAgICAgIGV4Y2VwdCBFeGNlcHRpb246CiAgICAgICAgICAgICAgICBsb2cuZXhjZXB0aW9uKAogICAgICAgICAgICAgICAgICAgICJCRERMIHBlcnR1cmJhdGlvbiBmYWlsZWQ6IHRhc2s9JXMgY2ZnPSVkIiwgdGFza19uYW1lLCBjZmdfaWR4CiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICBjb250aW51ZQoKICAgICAgICAgICAgZm9yIGVwIGluIHJhbmdlKGVwaXNvZGVzX3Blcl9jb25maWcpOgogICAgICAgICAgICAgICAgc2VlZCA9IGhhc2goKHRhc2tfbmFtZSwgY2ZnX2lkeCwgZXApKSAlICgyKiozMSkKICAgICAgICAgICAgICAgIHN0YXRzWyJ0b3RhbCJdICs9IDEKCiAgICAgICAgICAgICAgICB0cnk6CiAgICAgICAgICAgICAgICAgICAgZW52ID0gY3JlYXRlX2VudihwZXJ0dXJiZWRfYmRkbCkKICAgICAgICAgICAgICAgICAgICAjIFVzZSBub21pbmFsIGluaXRfc3RhdGUgKGluZGV4IDApIGZvciBzcGF0aWFsIHBlcnR1cmJhdGlvbgogICAgICAgICAgICAgICAgICAgIHJlc3VsdCA9IHJvbGxvdXRfZXBpc29kZSgKICAgICAgICAgICAgICAgICAgICAgICAgcG9saWN5LCBlbnYsIGxhbmd1YWdlLCBpbml0X3N0YXRlcywgMCwgc2VlZAogICAgICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgICAgICBlbnYuY2xvc2UoKQogICAgICAgICAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbjoKICAgICAgICAgICAgICAgICAgICBsb2cuZXhjZXB0aW9uKAogICAgICAgICAgICAgICAgICAgICAgICAiRXBpc29kZSBmYWlsZWQ6IHRhc2s9JXMgY2ZnPSVkIGVwPSVkIiwKICAgICAgICAgICAgICAgICAgICAgICAgdGFza19uYW1lLCBjZmdfaWR4LCBlcCwKICAgICAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAgICAgY29udGludWUKCiAgICAgICAgICAgICAgICBpZiByZXN1bHRbInN1Y2Nlc3MiXToKICAgICAgICAgICAgICAgICAgICBzdGF0c1sic3VjY2VzcyJdICs9IDEKICAgICAgICAgICAgICAgICAgICBkZW1vID0gewogICAgICAgICAgICAgICAgICAgICAgICAib2JzZXJ2YXRpb25zIjogcmVzdWx0WyJvYnNlcnZhdGlvbnMiXSwKICAgICAgICAgICAgICAgICAgICAgICAgImFjdGlvbnMiOiByZXN1bHRbImFjdGlvbnMiXSwKICAgICAgICAgICAgICAgICAgICAgICAgInRhc2tfbmFtZSI6IHRhc2tfbmFtZSwKICAgICAgICAgICAgICAgICAgICAgICAgInBlcnR1cmJhdGlvbl9jb25maWciOiB7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAidHlwZSI6ICJzcGF0aWFsIiwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICJjb25maWdfaWR4IjogY2ZnX2lkeCwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICJkZWx0YV94eSI6IGNmZ1siZGVsdGFfeHkiXSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICJkZWx0YV9oYWxmX2xlbiI6IGNmZ1siZGVsdGFfaGFsZl9sZW4iXSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICJkZWx0YV95YXciOiBjZmdbImRlbHRhX3lhdyJdLAogICAgICAgICAgICAgICAgICAgICAgICB9LAogICAgICAgICAgICAgICAgICAgICAgICAic3VjY2VzcyI6IFRydWUsCiAgICAgICAgICAgICAgICAgICAgICAgICJudW1fc3RlcHMiOiByZXN1bHRbIm51bV9zdGVwcyJdLAogICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgICAgICBmbmFtZSA9IGYie3Rhc2tfbmFtZX1fc3BhdGlhbHtjZmdfaWR4fV9lcHtlcH0ucGtsIgogICAgICAgICAgICAgICAgICAgIGZwYXRoID0gb3MucGF0aC5qb2luKG91dHB1dF9kaXIsIGZuYW1lKQogICAgICAgICAgICAgICAgICAgIHdpdGggb3BlbihmcGF0aCwgIndiIikgYXMgZjoKICAgICAgICAgICAgICAgICAgICAgICAgcGlja2xlLmR1bXAoZGVtbywgZiwgcHJvdG9jb2w9cGlja2xlLkhJR0hFU1RfUFJPVE9DT0wpCiAgICAgICAgICAgICAgICAgICAgc3RhdHNbInNhdmVkX2ZpbGVzIl0uYXBwZW5kKGZwYXRoKQoKICAgICAgICAgICAgICAgIHJhdGUgPSBzdGF0c1sic3VjY2VzcyJdIC8gc3RhdHNbInRvdGFsIl0gKiAxMDAKICAgICAgICAgICAgICAgIGxvZy5pbmZvKAogICAgICAgICAgICAgICAgICAgICJbc3BhdGlhbF0gdGFzaz0lcyBjZmc9JWQgZXA9JWQgfCAlcyB8ICIKICAgICAgICAgICAgICAgICAgICAiY3VtdWxhdGl2ZSAlZC8lZCAoJS4xZiUlKSIsCiAgICAgICAgICAgICAgICAgICAgdGFza19uYW1lLCBjZmdfaWR4LCBlcCwKICAgICAgICAgICAgICAgICAgICAiU1VDQ0VTUyIgaWYgcmVzdWx0WyJzdWNjZXNzIl0gZWxzZSAiRkFJTCIsCiAgICAgICAgICAgICAgICAgICAgc3RhdHNbInN1Y2Nlc3MiXSwgc3RhdHNbInRvdGFsIl0sIHJhdGUsCiAgICAgICAgICAgICAgICApCgogICAgcmV0dXJuIHN0YXRzCgoKZGVmIGNvbGxlY3Rfc3BhdGlhbF9hZGRfbigKICAgIHBvbGljeTogb2JqZWN0LAogICAgZXBpc29kZXNfcGVyX3Rhc2s6IGludCwKICAgIG91dHB1dF9kaXI6IHN0ciwKICAgIGRyeV9ydW46IGJvb2wsCikgLT4gZGljdDoKICAgICIiIkNvbGxlY3QgZXhwZXJ0IGRlbW9zIHVzaW5nIExJQkVSTy1QbHVzIF9hZGRfTiBkaXN0cmFjdG9yLW9iamVjdCB0YXNrcy4KCiAgICBFYWNoIF9hZGRfTiB0YXNrIGlzIGEgcHJlLWJ1aWx0IEJEREwgd2l0aCBleHRyYSBvYmplY3RzIGluIHRoZSBzY2VuZS4KICAgIDIwOCB0YXNrcyDDlyAzIGVwaXNvZGVzID0gNjI0IHJvbGxvdXRzLgogICAgIiIiCiAgICBvcy5tYWtlZGlycyhvdXRwdXRfZGlyLCBleGlzdF9vaz1UcnVlKQogICAgc3RhdHMgPSB7InRvdGFsIjogMCwgInN1Y2Nlc3MiOiAwLCAic2F2ZWRfZmlsZXMiOiBbXSwgImxvYWRfZXJyb3JzIjogMH0KCiAgICBhZGRfdGFza3MgPSBkaXNjb3Zlcl9hZGRfbl90YXNrcygpCiAgICBpZiBub3QgYWRkX3Rhc2tzOgogICAgICAgIGxvZy5lcnJvcigiTm8gX2FkZF9OIHRhc2tzIGZvdW5kLiBDaGVjayBMSUJFUk8tUGx1cyBpbnN0YWxsYXRpb24uIikKICAgICAgICByZXR1cm4gc3RhdHMKCiAgICBpZiBkcnlfcnVuOgogICAgICAgIGFkZF90YXNrcyA9IGFkZF90YXNrc1s6Ml0KICAgICAgICBlcGlzb2Rlc19wZXJfdGFzayA9IDEKCiAgICBsb2cuaW5mbygKICAgICAgICAiQ29sbGVjdGluZyBzcGF0aWFsIChfYWRkX04pOiAlZCB0YXNrcyDDlyAlZCBlcHMgPSAlZCByb2xsb3V0cyIsCiAgICAgICAgbGVuKGFkZF90YXNrcyksIGVwaXNvZGVzX3Blcl90YXNrLCBsZW4oYWRkX3Rhc2tzKSAqIGVwaXNvZGVzX3Blcl90YXNrLAogICAgKQoKICAgIGZvciB0YXNrX2luZm8gaW4gYWRkX3Rhc2tzOgogICAgICAgIHRhc2tfbmFtZSA9IHRhc2tfaW5mb1sibmFtZSJdCiAgICAgICAgbGFuZ3VhZ2UgPSB0YXNrX2luZm9bImxhbmd1YWdlIl0KICAgICAgICBpbml0X3N0YXRlcyA9IHRhc2tfaW5mb1siaW5pdF9zdGF0ZXMiXQoKICAgICAgICBmb3IgZXAgaW4gcmFuZ2UoZXBpc29kZXNfcGVyX3Rhc2spOgogICAgICAgICAgICBzZWVkID0gaGFzaCgodGFza19uYW1lLCBlcCkpICUgKDIqKjMxKQogICAgICAgICAgICBzdGF0c1sidG90YWwiXSArPSAxCgogICAgICAgICAgICB0cnk6CiAgICAgICAgICAgICAgICBlbnYgPSBjcmVhdGVfZW52KHRhc2tfaW5mb1siYmRkbF9wYXRoIl0pCiAgICAgICAgICAgICAgICBpbml0X2lkeCA9IGVwICUgbGVuKGluaXRfc3RhdGVzKQogICAgICAgICAgICAgICAgcmVzdWx0ID0gcm9sbG91dF9lcGlzb2RlKAogICAgICAgICAgICAgICAgICAgIHBvbGljeSwgZW52LCBsYW5ndWFnZSwgaW5pdF9zdGF0ZXMsIGluaXRfaWR4LCBzZWVkCiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICBlbnYuY2xvc2UoKQogICAgICAgICAgICBleGNlcHQgRmlsZU5vdEZvdW5kRXJyb3IgYXMgZToKICAgICAgICAgICAgICAgIHN0YXRzWyJsb2FkX2Vycm9ycyJdICs9IDEKICAgICAgICAgICAgICAgIGxvZy53YXJuaW5nKCJBc3NldCBtaXNzaW5nIGZvciAlczogJXMiLCB0YXNrX25hbWUsIGUpCiAgICAgICAgICAgICAgICBjb250aW51ZQogICAgICAgICAgICBleGNlcHQgRXhjZXB0aW9uOgogICAgICAgICAgICAgICAgbG9nLmV4Y2VwdGlvbigiRXBpc29kZSBmYWlsZWQ6IHRhc2s9JXMgZXA9JWQiLCB0YXNrX25hbWUsIGVwKQogICAgICAgICAgICAgICAgY29udGludWUKCiAgICAgICAgICAgIGlmIHJlc3VsdFsic3VjY2VzcyJdOgogICAgICAgICAgICAgICAgc3RhdHNbInN1Y2Nlc3MiXSArPSAxCiAgICAgICAgICAgICAgICBkZW1vID0gewogICAgICAgICAgICAgICAgICAgICJvYnNlcnZhdGlvbnMiOiByZXN1bHRbIm9ic2VydmF0aW9ucyJdLAogICAgICAgICAgICAgICAgICAgICJhY3Rpb25zIjogcmVzdWx0WyJhY3Rpb25zIl0sCiAgICAgICAgICAgICAgICAgICAgInRhc2tfbmFtZSI6IHRhc2tfbmFtZSwKICAgICAgICAgICAgICAgICAgICAicGVydHVyYmF0aW9uX2NvbmZpZyI6IHsKICAgICAgICAgICAgICAgICAgICAgICAgInR5cGUiOiAic3BhdGlhbF9hZGRfbiIsCiAgICAgICAgICAgICAgICAgICAgICAgICJzb3VyY2VfdGFza19pZHgiOiB0YXNrX2luZm9bImlkeCJdLAogICAgICAgICAgICAgICAgICAgIH0sCiAgICAgICAgICAgICAgICAgICAgInN1Y2Nlc3MiOiBUcnVlLAogICAgICAgICAgICAgICAgICAgICJudW1fc3RlcHMiOiByZXN1bHRbIm51bV9zdGVwcyJdLAogICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgZm5hbWUgPSBmInt0YXNrX25hbWV9X2Vwe2VwfS5wa2wiCiAgICAgICAgICAgICAgICBmcGF0aCA9IG9zLnBhdGguam9pbihvdXRwdXRfZGlyLCBmbmFtZSkKICAgICAgICAgICAgICAgIHdpdGggb3BlbihmcGF0aCwgIndiIikgYXMgZjoKICAgICAgICAgICAgICAgICAgICBwaWNrbGUuZHVtcChkZW1vLCBmLCBwcm90b2NvbD1waWNrbGUuSElHSEVTVF9QUk9UT0NPTCkKICAgICAgICAgICAgICAgIHN0YXRzWyJzYXZlZF9maWxlcyJdLmFwcGVuZChmcGF0aCkKCiAgICAgICAgICAgIHJhdGUgPSBzdGF0c1sic3VjY2VzcyJdIC8gc3RhdHNbInRvdGFsIl0gKiAxMDAKICAgICAgICAgICAgbG9nLmluZm8oCiAgICAgICAgICAgICAgICAiW3NwYXRpYWxfYWRkX25dIHRhc2s9JXMgZXA9JWQgfCAlcyB8IGN1bXVsYXRpdmUgJWQvJWQgKCUuMWYlJSkgfCBsb2FkX2Vycm9ycz0lZCIsCiAgICAgICAgICAgICAgICB0YXNrX25hbWUsIGVwLAogICAgICAgICAgICAgICAgIlNVQ0NFU1MiIGlmIHJlc3VsdFsic3VjY2VzcyJdIGVsc2UgIkZBSUwiLAogICAgICAgICAgICAgICAgc3RhdHNbInN1Y2Nlc3MiXSwgc3RhdHNbInRvdGFsIl0sIHJhdGUsCiAgICAgICAgICAgICAgICBzdGF0c1sibG9hZF9lcnJvcnMiXSwKICAgICAgICAgICAgKQoKICAgIHJldHVybiBzdGF0cwoKCiMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCiMgTWFpbgojIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQoKZGVmIG1haW4oKToKICAgIHBhcnNlciA9IGFyZ3BhcnNlLkFyZ3VtZW50UGFyc2VyKAogICAgICAgIGRlc2NyaXB0aW9uPSJDb2xsZWN0IGV4cGVydCBkZW1vcyBmcm9tIM+A4oKAIGluIHBlcnR1cmJlZCBMSUJFUk8gZW52aXJvbm1lbnRzIgogICAgKQogICAgcGFyc2VyLmFkZF9hcmd1bWVudCgKICAgICAgICAiLS1wZXJ0dXJiYXRpb25fdHlwZSIsIHR5cGU9c3RyLCByZXF1aXJlZD1UcnVlLAogICAgICAgIGNob2ljZXM9WyJwaHlzaWNhbCIsICJzcGF0aWFsIl0sCiAgICApCiAgICBwYXJzZXIuYWRkX2FyZ3VtZW50KAogICAgICAgICItLXNwYXRpYWxfbW9kZSIsIHR5cGU9c3RyLCBkZWZhdWx0PSJhZGRfbiIsCiAgICAgICAgY2hvaWNlcz1bImFkZF9uIiwgInBlcnR1cmJfcmVnaW9uIl0sCiAgICAgICAgaGVscD0iU3BhdGlhbCBwZXJ0dXJiYXRpb24gbW9kZTogYWRkX24gKExJQkVSTy1QbHVzIGRpc3RyYWN0b3JzLCBkZWZhdWx0KSAiCiAgICAgICAgICAgICAib3IgcGVydHVyYl9yZWdpb24gKGxlZ2FjeSBCRERMIHJlZ2lvbiBzaGlmdHMpIiwKICAgICkKICAgIHBhcnNlci5hZGRfYXJndW1lbnQoIi0tZ3B1X2lkIiwgdHlwZT1pbnQsIGRlZmF1bHQ9MCkKICAgIHBhcnNlci5hZGRfYXJndW1lbnQoIi0tbnVtX3Rhc2tzIiwgdHlwZT1pbnQsIGRlZmF1bHQ9MTApCiAgICBwYXJzZXIuYWRkX2FyZ3VtZW50KCItLWVwaXNvZGVzX3Blcl9jb25maWciLCB0eXBlPWludCwgZGVmYXVsdD0zKQogICAgcGFyc2VyLmFkZF9hcmd1bWVudCgKICAgICAgICAiLS1vdXRwdXRfZGlyIiwgdHlwZT1zdHIsIGRlZmF1bHQ9Tm9uZSwKICAgICAgICBoZWxwPSJPdmVycmlkZSBvdXRwdXQgZGlyZWN0b3J5IChkZWZhdWx0OiBhdXRvIGZyb20gcGVydHVyYmF0aW9uX3R5cGUpIiwKICAgICkKICAgIHBhcnNlci5hZGRfYXJndW1lbnQoCiAgICAgICAgIi0tY2hlY2twb2ludCIsIHR5cGU9c3RyLAogICAgICAgIGRlZmF1bHQ9Ii9yb290L2F1dG9kbC10bXAvY2hlY2twb2ludHMvcGkwX2Jhc2UiLAogICAgKQogICAgcGFyc2VyLmFkZF9hcmd1bWVudCgiLS1kcnlfcnVuIiwgYWN0aW9uPSJzdG9yZV90cnVlIikKICAgIHBhcnNlci5hZGRfYXJndW1lbnQoIi0tc2VlZCIsIHR5cGU9aW50LCBkZWZhdWx0PTQyKQogICAgYXJncyA9IHBhcnNlci5wYXJzZV9hcmdzKCkKCiAgICBsb2dnaW5nLmJhc2ljQ29uZmlnKAogICAgICAgIGxldmVsPWxvZ2dpbmcuSU5GTywKICAgICAgICBmb3JtYXQ9IiUoYXNjdGltZSlzIFslKGxldmVsbmFtZSlzXSAlKG1lc3NhZ2UpcyIsCiAgICApCgogICAgcmFuZG9tLnNlZWQoYXJncy5zZWVkKQogICAgbnAucmFuZG9tLnNlZWQoYXJncy5zZWVkKQogICAgdG9yY2gubWFudWFsX3NlZWQoYXJncy5zZWVkKQoKICAgIGlmIGFyZ3Mub3V0cHV0X2RpciBpcyBOb25lOgogICAgICAgIGFyZ3Mub3V0cHV0X2RpciA9ICgKICAgICAgICAgICAgZiIvcm9vdC9tZXRhX2JyYWluX2xvcmFfcm91dGluZy9kYXRhL2V4cGVydF9kZW1vcy97YXJncy5wZXJ0dXJiYXRpb25fdHlwZX0iCiAgICAgICAgKQoKICAgIGRldmljZSA9IGYiY3VkYTp7YXJncy5ncHVfaWR9IgogICAgbG9nLmluZm8oCiAgICAgICAgIkNvbmZpZzogdHlwZT0lcyBzcGF0aWFsX21vZGU9JXMgZGV2aWNlPSVzIG51bV90YXNrcz0lZCBlcHNfcGVyX2NmZz0lZCBkcnlfcnVuPSVzIiwKICAgICAgICBhcmdzLnBlcnR1cmJhdGlvbl90eXBlLCBhcmdzLnNwYXRpYWxfbW9kZSwgZGV2aWNlLCBhcmdzLm51bV90YXNrcywKICAgICAgICBhcmdzLmVwaXNvZGVzX3Blcl9jb25maWcsIGFyZ3MuZHJ5X3J1biwKICAgICkKCiAgICBsb2cuaW5mbygiTG9hZGluZyDPgOKCgCBmcm9tICVzIiwgYXJncy5jaGVja3BvaW50KQogICAgcG9saWN5ID0gbG9hZF9waTBfcG9saWN5KGFyZ3MuY2hlY2twb2ludCwgZGV2aWNlKQoKICAgIHQwID0gdGltZS50aW1lKCkKCiAgICBpZiBhcmdzLnBlcnR1cmJhdGlvbl90eXBlID09ICJwaHlzaWNhbCI6CiAgICAgICAgZnJvbSBsaWJlcm8ubGliZXJvIGltcG9ydCBnZXRfbGliZXJvX3BhdGgKICAgICAgICBiZGRsX2RpciA9IG9zLnBhdGguam9pbihnZXRfbGliZXJvX3BhdGgoImJkZGxfZmlsZXMiKSwgQkFTRV9UQVNLX1NVSVRFKQogICAgICAgIHRhc2tzID0gZmluZF9iYXNlX3Rhc2tzKGJkZGxfZGlyLCBudW1fdGFza3M9YXJncy5udW1fdGFza3MpCiAgICAgICAgaWYgbm90IHRhc2tzOgogICAgICAgICAgICBsb2cuZXJyb3IoIk5vIGJhc2UgdGFza3MgZm91bmQgaW4gJXMiLCBiZGRsX2RpcikKICAgICAgICAgICAgc3lzLmV4aXQoMSkKICAgICAgICBzdGF0cyA9IGNvbGxlY3RfcGh5c2ljYWwoCiAgICAgICAgICAgIHBvbGljeSwgdGFza3MsIGFyZ3MuZXBpc29kZXNfcGVyX2NvbmZpZywKICAgICAgICAgICAgYXJncy5vdXRwdXRfZGlyLCBhcmdzLmRyeV9ydW4sCiAgICAgICAgKQogICAgZWxpZiBhcmdzLnNwYXRpYWxfbW9kZSA9PSAiYWRkX24iOgogICAgICAgIHN0YXRzID0gY29sbGVjdF9zcGF0aWFsX2FkZF9uKAogICAgICAgICAgICBwb2xpY3ksIGFyZ3MuZXBpc29kZXNfcGVyX2NvbmZpZywKICAgICAgICAgICAgYXJncy5vdXRwdXRfZGlyLCBhcmdzLmRyeV9ydW4sCiAgICAgICAgKQogICAgZWxzZToKICAgICAgICBmcm9tIGxpYmVyby5saWJlcm8gaW1wb3J0IGdldF9saWJlcm9fcGF0aAogICAgICAgIGJkZGxfZGlyID0gb3MucGF0aC5qb2luKGdldF9saWJlcm9fcGF0aCgiYmRkbF9maWxlcyIpLCBCQVNFX1RBU0tfU1VJVEUpCiAgICAgICAgdGFza3MgPSBmaW5kX2Jhc2VfdGFza3MoYmRkbF9kaXIsIG51bV90YXNrcz1hcmdzLm51bV90YXNrcykKICAgICAgICBpZiBub3QgdGFza3M6CiAgICAgICAgICAgIGxvZy5lcnJvcigiTm8gYmFzZSB0YXNrcyBmb3VuZCBpbiAlcyIsIGJkZGxfZGlyKQogICAgICAgICAgICBzeXMuZXhpdCgxKQogICAgICAgIHN0YXRzID0gY29sbGVjdF9zcGF0aWFsKAogICAgICAgICAgICBwb2xpY3ksIHRhc2tzLCBhcmdzLmVwaXNvZGVzX3Blcl9jb25maWcsCiAgICAgICAgICAgIGFyZ3Mub3V0cHV0X2RpciwgYXJncy5kcnlfcnVuLAogICAgICAgICkKCiAgICBlbGFwc2VkID0gdGltZS50aW1lKCkgLSB0MAoKICAgIHRvdGFsX3NpemUgPSBzdW0oCiAgICAgICAgb3MucGF0aC5nZXRzaXplKGYpIGZvciBmIGluIHN0YXRzWyJzYXZlZF9maWxlcyJdIGlmIG9zLnBhdGguZXhpc3RzKGYpCiAgICApCiAgICBsb2cuaW5mbygiPSIgKiA2MCkKICAgIGxvZy5pbmZvKCJDb2xsZWN0aW9uIGNvbXBsZXRlOiAlcyIsIGFyZ3MucGVydHVyYmF0aW9uX3R5cGUpCiAgICBsb2cuaW5mbygiICBUb3RhbCBlcGlzb2RlczogICVkIiwgc3RhdHNbInRvdGFsIl0pCiAgICBsb2cuaW5mbygiICBTdWNjZXNzZnVsOiAgICAgICVkIiwgc3RhdHNbInN1Y2Nlc3MiXSkKICAgIGxvZy5pbmZvKAogICAgICAgICIgIFN1Y2Nlc3MgcmF0ZTogICAgJS4xZiUlIiwKICAgICAgICBzdGF0c1sic3VjY2VzcyJdIC8gbWF4KHN0YXRzWyJ0b3RhbCJdLCAxKSAqIDEwMCwKICAgICkKICAgIGxvZy5pbmZvKCIgIEZpbGVzIHNhdmVkOiAgICAgJWQiLCBsZW4oc3RhdHNbInNhdmVkX2ZpbGVzIl0pKQogICAgbG9nLmluZm8oIiAgVG90YWwgc2l6ZTogICAgICAlLjFmIE1CIiwgdG90YWxfc2l6ZSAvIDEwMjQgLyAxMDI0KQogICAgbG9nLmluZm8oIiAgRWxhcHNlZDogICAgICAgICAlLjFmIG1pbiIsIGVsYXBzZWQgLyA2MCkKICAgIGxvZy5pbmZvKCIgIE91dHB1dCBkaXI6ICAgICAgJXMiLCBhcmdzLm91dHB1dF9kaXIpCgoKaWYgX19uYW1lX18gPT0gIl9fbWFpbl9fIjoKICAgIG1haW4oKQo=\nENDOFBASE64"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "0c497a87-5789-4eb3-a2f4-ae3d5b45f1cd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pnmekxf22u7DpFYk6FB8iW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 28931,
      "cache_read_input_tokens": 62208,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 28931
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

_source line 146 · 2026-05-15T18:02:00.836Z_

<details><summary>↩ Tool result · `toolu_0137VdpUEh5QhW5s1c2KHkdG`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"Written 26711 bytes\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.19}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "9d92f012-d4d5-4943-a7a7-6b7c37b6615e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"Written 26711 bytes\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.19}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"Written 26711 bytes\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.19}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 147_

文件已传输（26711 bytes）。验证行数和 `_add_N` 任务发现。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "38aa925f-86cf-49b6-94da-cfd0986240ad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FPTJsJDDBRmCZf3vtY7UzY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 28897,
      "cache_read_input_tokens": 91139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 28897
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

_source line 148_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_019Zej1NdtD1YXNiCwW9JEpb`</summary>

```json
{
  "server": "westd-34142",
  "account": "root",
  "command": "wc -l /root/meta_brain_lora_routing/phase1/collect_expert_demos.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "d0608e03-5d4e-43e5-9f4d-9af7be84b17e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FPTJsJDDBRmCZf3vtY7UzY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 28897,
      "cache_read_input_tokens": 91139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 28897
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

_source line 149 · 2026-05-15T18:02:08.386Z_

<details><summary>↩ Tool result · `toolu_019Zej1NdtD1YXNiCwW9JEpb`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"745 /root/meta_brain_lora_routing/phase1/collect_expert_demos.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "12639fb0-2d49-4531-b84a-505a6658144d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"745 /root/meta_brain_lora_routing/phase1/collect_expert_demos.py\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"745 /root/meta_brain_lora_routing/phase1/collect_expert_demos.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 150_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01LvHypVxzXRHNzscDK9KYFV`</summary>

```json
{
  "server": "westd-34142",
  "account": "root",
  "command": "grep -n \"discover_add_n_tasks\\|collect_spatial_add_n\\|spatial_mode\" /root/meta_brain_lora_routing/phase1/collect_expert_demos.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "4962efa6-0c86-43ba-b3e4-8c091d47e100",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FPTJsJDDBRmCZf3vtY7UzY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 28897,
      "cache_read_input_tokens": 91139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 28897
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


### Runtime record

_source line 151_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1778886000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "b44a5a11-9b76-45f6-bfa7-804758fe3b0a",
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7"
}
```

---


### Tool result

_source line 152 · 2026-05-15T18:02:08.822Z_

<details><summary>↩ Tool result · `toolu_01LvHypVxzXRHNzscDK9KYFV`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "9b764fad-18cf-4592-bf2e-62123c2939d1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 153_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_018ZSYpypyDypHquvcET26zf`</summary>

```json
{
  "server": "westd-34142",
  "account": "root",
  "command": "grep -n \"discover_add_n_tasks\\|collect_spatial_add_n\\|spatial_mode\" /root/meta_brain_lora_routing/phase1/collect_expert_demos.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "a1e7be9d-199f-42fd-8a36-19492d7efe94",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0123LL5zQdVrGoWkgSTYk3fM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 543,
      "cache_read_input_tokens": 120036,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 543
      },
      "output_tokens": 69,
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

_source line 154 · 2026-05-15T18:02:12.569Z_

<details><summary>↩ Tool result · `toolu_018ZSYpypyDypHquvcET26zf`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "fa6d38a9-7754-4bd1-8d60-6f73aaffc147",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 155_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_011EqcKSgS9mhrLvcZuivR7v`</summary>

```json
{
  "server": "westd-34142",
  "account": "root",
  "command": "grep -n \"discover_add_n_tasks\" /root/meta_brain_lora_routing/phase1/collect_expert_demos.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "1375e0a7-651e-4b93-aebe-6f4f9cc0f466",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TADxLHF4XbmUXaxL5XAv6f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 242,
      "cache_read_input_tokens": 120579,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 242
      },
      "output_tokens": 69,
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

_source line 156 · 2026-05-15T18:02:16.564Z_

<details><summary>↩ Tool result · `toolu_011EqcKSgS9mhrLvcZuivR7v`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"225:def discover_add_n_tasks(task_suite: str = BASE_TASK_SUITE) -> list[dict]:\\n569:    add_tasks = discover_add_n_tasks()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "4ac1e305-348f-4ace-a1c9-5b4711d61371",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"225:def discover_add_n_tasks(task_suite: str = BASE_TASK_SUITE) -> list[dict]:\\\\n569:    add_tasks = discover_add_n_tasks()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"225:def discover_add_n_tasks(task_suite: str = BASE_TASK_SUITE) -> list[dict]:\\n569:    add_tasks = discover_add_n_tasks()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 157_

745 行，关键函数就位。现在先测试 `_add_N` 任务发现（不加载 policy，纯 benchmark 验证）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "0b439c1f-4178-46db-b5e8-02cad52a01b9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KHVTMQqty4drVGiGf6oVkt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 257,
      "cache_read_input_tokens": 120821,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 257
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

_source line 158_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01ExEx8Li8m5JhNFgoP91bwG`</summary>

```json
{
  "server": "westd-34142",
  "account": "root",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/meta_brain_lora_routing && python3 -c \"\nimport sys, os, re, logging\nlogging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')\nsys.path.insert(0, '/root/LIBERO-plus/libero')\nfrom pathlib import Path\nfrom libero.libero import benchmark, get_libero_path\n\nbenchmark_dict = benchmark.get_benchmark_dict()\nsuite = benchmark_dict['libero_spatial']()\nbddl_root = Path(get_libero_path('bddl_files'))\nprint(f'Total tasks in libero_spatial suite: {suite.n_tasks}')\n\nadd_tasks = []\nskipped = 0\nfor i in range(suite.n_tasks):\n    task = suite.get_task(i)\n    name = getattr(task, 'name', '') or getattr(task, 'bddl_file', '')\n    if not re.search(r'_add_\\d+$', name.replace('.bddl', '')):\n        continue\n    bddl_path = str(bddl_root / task.problem_folder / task.bddl_file)\n    if not os.path.exists(bddl_path):\n        skipped += 1\n        continue\n    add_tasks.append({'idx': i, 'name': name.replace('.bddl',''), 'lang': task.language, 'bddl': bddl_path})\n\nprint(f'Found {len(add_tasks)} _add_N tasks ({skipped} skipped)')\nfor t in add_tasks[:5]:\n    print(f'  [{t[\\\"idx\\\"]}] {t[\\\"name\\\"]} -> {t[\\\"lang\\\"][:60]}')\nprint('...')\nfor t in add_tasks[-3:]:\n    print(f'  [{t[\\\"idx\\\"]}] {t[\\\"name\\\"]} -> {t[\\\"lang\\\"][:60]}')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "35377fbe-ba63-40d7-ae4e-1496ed5f4e0e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KHVTMQqty4drVGiGf6oVkt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 257,
      "cache_read_input_tokens": 120821,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 257
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

_source line 159 · 2026-05-15T18:02:29.216Z_

<details><summary>↩ Tool result · `toolu_01ExEx8Li8m5JhNFgoP91bwG`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/meta_brain_lora_routing && python3 -c \\\"\\\\nimport sys, os, re, logging\\\\nlogging.basicConfig(level=logging.INFO, format=\\\\'%(asctime)s [%(levelname)s] %(message)s\\\\')\\\\nsys.path.insert(0, \\\\'/root/LIBERO-plus/libero\\\\')\\\\nfrom pathlib import Path\\\\nfrom libero.libero import benchmark, get_libero_path\\\\n\\\\nbenchmark_dict = benchmark.get_benchmark_dict()\\\\nsuite = benchmark_dict[\\\\'libero_spatial\\\\']()\\\\nbddl_root = Path(get_libero_path(\\\\'bddl_files\\\\'))\\\\nprint(f\\\\'Total tasks in libero_spatial suite: {suite.n_tasks}\\\\')\\\\n\\\\nadd_tasks = []\\\\nskipped = 0\\\\nfor i in range(suite.n_tasks):\\\\n    task = suite.get_task(i)\\\\n    name = getattr(task, \\\\'name\\\\', \\\\'\\\\') or getattr(task, \\\\'bddl_file\\\\', \\\\'\\\\')\\\\n    if not re.search(r\\\\'_add_\\\\\\\\d+$\\\\', name.replace(\\\\'.bddl\\\\', \\\\'\\\\')):\\\\n        continue\\\\n    bddl_path = str(bddl_root / task.problem_folder / task.bddl_file)\\\\n    if not os.path.exists(bddl_path):\\\\n        skipped += 1\\\\n        continue\\\\n    add_tasks.append({\\\\'idx\\\\': i, \\\\'name\\\\': name.replace(\\\\'.bddl\\\\',\\\\'\\\\'), \\\\'lang\\\\': task.language, \\\\'bddl\\\\': bddl_path})\\\\n\\\\nprint(f\\\\'Found {len(add_tasks)} _add_N tasks ({skipped} skipped)\\\\')\\\\nfor t in add_tasks[:5]:\\\\n    print(f\\\\'  [{t[\\\\\\\\\\\"idx\\\\\\\\\\\"]}] {t[\\\\\\\\\\\"name\\\\\\\\\\\"]} -> {t[\\\\\\\\\\\"lang\\\\\\\\\\\"][:60]}\\\\')\\\\nprint(\\\\'...\\\\')\\\\nfor t in add_tasks[-3:]:\\\\n    print(f\\\\'  [{t[\\\\\\\\\\\"idx\\\\\\\\\\\"]}] {t[\\\\\\\\\\\"name\\\\\\\\\\\"]} -> {t[\\\\\\\\\\\"lang\\\\\\\\\\\"][:60]}\\\\')\\\\n\\\"\\\\n'\\n\\nExit code: 1\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nTraceback (most recent call last):\\n  File \\\"&lt;string>\\\", line 6, in &lt;module>\\nModuleNotFoundError: No module named 'libero.libero'\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.56}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "5968adb3-2a6d-4958-b6e5-39ab1a4ac23f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Encountered a bad command exit code!\\\\n\\\\nCommand: 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/meta_brain_lora_routing && python3 -c \\\\\\\"\\\\\\\\nimport sys, os, re, logging\\\\\\\\nlogging.basicConfig(level=logging.INFO, format=\\\\\\\\'%(asctime)s [%(levelname)s] %(message)s\\\\\\\\')\\\\\\\\nsys.path.insert(0, \\\\\\\\'/root/LIBERO-plus/libero\\\\\\\\')\\\\\\\\nfrom pathlib import Path\\\\\\\\nfrom libero.libero import benchmark, get_libero_path\\\\\\\\n\\\\\\\\nbenchmark_dict = benchmark.get_benchmark_dict()\\\\\\\\nsuite = benchmark_dict[\\\\\\\\'libero_spatial\\\\\\\\']()\\\\\\\\nbddl_root = Path(get_libero_path(\\\\\\\\'bddl_files\\\\\\\\'))\\\\\\\\nprint(f\\\\\\\\'Total tasks in libero_spatial suite: {suite.n_tasks}\\\\\\\\')\\\\\\\\n\\\\\\\\nadd_tasks = []\\\\\\\\nskipped = 0\\\\\\\\nfor i in range(suite.n_tasks):\\\\\\\\n    task = suite.get_task(i)\\\\\\\\n    name = getattr(task, \\\\\\\\'name\\\\\\\\', \\\\\\\\'\\\\\\\\') or getattr(task, \\\\\\\\'bddl_file\\\\\\\\', \\\\\\\\'\\\\\\\\')\\\\\\\\n    if not re.search(r\\\\\\\\'_add_\\\\\\\\\\\\\\\\d+$\\\\\\\\', name.replace(\\\\\\\\'.bddl\\\\\\\\', \\\\\\\\'\\\\\\\\')):\\\\\\\\n        continue\\\\\\\\n    bddl_path = str(bddl_root / task.problem_folder / task.bddl_file)\\\\\\\\n    if not os.path.exists(bddl_path):\\\\\\\\n        skipped += 1\\\\\\\\n        continue\\\\\\\\n    add_tasks.append({\\\\\\\\'idx\\\\\\\\': i, \\\\\\\\'name\\\\\\\\': name.replace(\\\\\\\\'.bddl\\\\\\\\',\\\\\\\\'\\\\\\\\'), \\\\\\\\'lang\\\\\\\\': task.language, \\\\\\\\'bddl\\\\\\\\': bddl_path})\\\\\\\\n\\\\\\\\nprint(f\\\\\\\\'Found {len(add_tasks)} _add_N tasks ({skipped} skipped)\\\\\\\\')\\\\\\\\nfor t in add_tasks[:5]:\\\\\\\\n    print(f\\\\\\\\'  [{t[\\\\\\\\\\\\\\\\\\\\\\\"idx\\\\\\\\\\\\\\\\\\\\\\\"]}] {t[\\\\\\\\\\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\\\\\\\\\\"]} -> {t[\\\\\\\\\\\\\\\\\\\\\\\"lang\\\\\\\\\\\\\\\\\\\\\\\"][:60]}\\\\\\\\')\\\\\\\\nprint(\\\\\\\\'...\\\\\\\\')\\\\\\\\nfor t in add_tasks[-3:]:\\\\\\\\n    print(f\\\\\\\\'  [{t[\\\\\\\\\\\\\\\\\\\\\\\"idx\\\\\\\\\\\\\\\\\\\\\\\"]}] {t[\\\\\\\\\\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\\\\\\\\\\"]} -> {t[\\\\\\\\\\\\\\\\\\\\\\\"lang\\\\\\\\\\\\\\\\\\\\\\\"][:60]}\\\\\\\\')\\\\\\\\n\\\\\\\"\\\\\\\\n'\\\\n\\\\nExit code: 1\\\\n\\\\nStdout:\\\\n\\\\n\\\\n\\\\nStderr:\\\\n\\\\nTraceback (most recent call last):\\\\n  File \\\\\\\"&lt;string>\\\\\\\", line 6, in &lt;module>\\\\nModuleNotFoundError: No module named 'libero.libero'\\\\n\\\\n\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.56}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/meta_brain_lora_routing && python3 -c \\\"\\\\nimport sys, os, re, logging\\\\nlogging.basicConfig(level=logging.INFO, format=\\\\'%(asctime)s [%(levelname)s] %(message)s\\\\')\\\\nsys.path.insert(0, \\\\'/root/LIBERO-plus/libero\\\\')\\\\nfrom pathlib import Path\\\\nfrom libero.libero import benchmark, get_libero_path\\\\n\\\\nbenchmark_dict = benchmark.get_benchmark_dict()\\\\nsuite = benchmark_dict[\\\\'libero_spatial\\\\']()\\\\nbddl_root = Path(get_libero_path(\\\\'bddl_files\\\\'))\\\\nprint(f\\\\'Total tasks in libero_spatial suite: {suite.n_tasks}\\\\')\\\\n\\\\nadd_tasks = []\\\\nskipped = 0\\\\nfor i in range(suite.n_tasks):\\\\n    task = suite.get_task(i)\\\\n    name = getattr(task, \\\\'name\\\\', \\\\'\\\\') or getattr(task, \\\\'bddl_file\\\\', \\\\'\\\\')\\\\n    if not re.search(r\\\\'_add_\\\\\\\\d+$\\\\', name.replace(\\\\'.bddl\\\\', \\\\'\\\\')):\\\\n        continue\\\\n    bddl_path = str(bddl_root / task.problem_folder / task.bddl_file)\\\\n    if not os.path.exists(bddl_path):\\\\n        skipped += 1\\\\n        continue\\\\n    add_tasks.append({\\\\'idx\\\\': i, \\\\'name\\\\': name.replace(\\\\'.bddl\\\\',\\\\'\\\\'), \\\\'lang\\\\': task.language, \\\\'bddl\\\\': bddl_path})\\\\n\\\\nprint(f\\\\'Found {len(add_tasks)} _add_N tasks ({skipped} skipped)\\\\')\\\\nfor t in add_tasks[:5]:\\\\n    print(f\\\\'  [{t[\\\\\\\\\\\"idx\\\\\\\\\\\"]}] {t[\\\\\\\\\\\"name\\\\\\\\\\\"]} -> {t[\\\\\\\\\\\"lang\\\\\\\\\\\"][:60]}\\\\')\\\\nprint(\\\\'...\\\\')\\\\nfor t in add_tasks[-3:]:\\\\n    print(f\\\\'  [{t[\\\\\\\\\\\"idx\\\\\\\\\\\"]}] {t[\\\\\\\\\\\"name\\\\\\\\\\\"]} -> {t[\\\\\\\\\\\"lang\\\\\\\\\\\"][:60]}\\\\')\\\\n\\\"\\\\n'\\n\\nExit code: 1\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nTraceback (most recent call last):\\n  File \\\"&lt;string>\\\", line 6, in &lt;module>\\nModuleNotFoundError: No module named 'libero.libero'\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.56}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 160_

<details><summary>Logged reasoning block</summary>

```text
The LIBERO-Plus module path issue. The import path should be just `libero` not `libero.libero`. Let me check how the original script does it - it uses `from libero.libero import benchmark, get_libero_path`. But the script has `sys.path.insert(0, '/root/LIBERO-plus/libero')` which means inside that directory there should be another `libero` package.

Actually wait, the script file at `/root/meta_brain_lora_routing/phase1/collect_expert_demos.py` does `from libero.libero import ...` and it works during runtime. 

So the directory structure is `/root/LIBERO-plus/` as the repo root, `/root/LIBERO-plus/libero/` as the installable package directory, and `/root/LIBERO-plus/libero/libero/` as the actual Python package - which explains why the `new_objects/` directory is nested at `/root/LIBERO-plus/libero/libero/assets/new_objects/`.

Given this structure, I should check whether LIBERO-Plus is installed as a pip package or if I need to adjust the sys.path to point to `/root/LIBERO-plus/libero/` so that `from libero import ...` resolves correctly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "20221bb4-b7cc-4a12-a2cc-ac1db5f4dd40",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q6xRKHJ9CbmUKeu6FydGKN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1550,
      "cache_read_input_tokens": 121078,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1550
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

_source line 161_

import 路径问题。先检查 LIBERO-Plus 的安装方式。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "8e2f0760-d5e8-41d1-9b6d-e186557c6b8b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q6xRKHJ9CbmUKeu6FydGKN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1550,
      "cache_read_input_tokens": 121078,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1550
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

_source line 162_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01LXerJ2oQqvBTgeSdUUbF4J`</summary>

```json
{
  "server": "westd-34142",
  "account": "root",
  "command": "find /root/LIBERO-plus -name \"__init__.py\" -maxdepth 4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "fbe6d6f9-63a7-4b5a-98c5-3f8ebd1f1653",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q6xRKHJ9CbmUKeu6FydGKN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1550,
      "cache_read_input_tokens": 121078,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1550
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

_source line 163_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01CSZsbUejdgj2AXC3d7MGir`</summary>

```json
{
  "server": "westd-34142",
  "account": "root",
  "command": "ls /root/LIBERO-plus/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "b9569bc8-e2e0-41f8-9925-f68a883242a0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q6xRKHJ9CbmUKeu6FydGKN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1550,
      "cache_read_input_tokens": 121078,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1550
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

_source line 164 · 2026-05-15T18:02:42.639Z_

<details><summary>↩ Tool result · `toolu_01LXerJ2oQqvBTgeSdUUbF4J`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/LIBERO-plus/libero/configs/__init__.py\\n/root/LIBERO-plus/libero/libero/__init__.py\\n/root/LIBERO-plus/libero/libero/benchmark/__init__.py\\n/root/LIBERO-plus/libero/libero/envs/__init__.py\\n/root/LIBERO-plus/libero/libero/utils/__init__.py\\n/root/LIBERO-plus/libero/lifelong/__init__.py\\n/root/LIBERO-plus/libero/lifelong/algos/__init__.py\\n/root/LIBERO-plus/libero/lifelong/models/__init__.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.87}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "c857a2e3-7682-4833-abc1-52f33039a500",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/LIBERO-plus/libero/configs/__init__.py\\\\n/root/LIBERO-plus/libero/libero/__init__.py\\\\n/root/LIBERO-plus/libero/libero/benchmark/__init__.py\\\\n/root/LIBERO-plus/libero/libero/envs/__init__.py\\\\n/root/LIBERO-plus/libero/libero/utils/__init__.py\\\\n/root/LIBERO-plus/libero/lifelong/__init__.py\\\\n/root/LIBERO-plus/libero/lifelong/algos/__init__.py\\\\n/root/LIBERO-plus/libero/lifelong/models/__init__.py\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.87}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/LIBERO-plus/libero/configs/__init__.py\\n/root/LIBERO-plus/libero/libero/__init__.py\\n/root/LIBERO-plus/libero/libero/benchmark/__init__.py\\n/root/LIBERO-plus/libero/libero/envs/__init__.py\\n/root/LIBERO-plus/libero/libero/utils/__init__.py\\n/root/LIBERO-plus/libero/lifelong/__init__.py\\n/root/LIBERO-plus/libero/lifelong/algos/__init__.py\\n/root/LIBERO-plus/libero/lifelong/models/__init__.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.87}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 165 · 2026-05-15T18:02:43.170Z_

<details><summary>↩ Tool result · `toolu_01CSZsbUejdgj2AXC3d7MGir`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"README.md\\nbenchmark_scripts\\nextra_requirements.txt\\nindex.html\\nlibero\\nlibero.egg-info\\nlibero_res.md\\nnotebooks\\nrequirements.txt\\nscripts\\nsetup.py\\nstatic\\ntemplates\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "3c4c9d8e-8697-4508-bf8a-a0398cacae89",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"README.md\\\\nbenchmark_scripts\\\\nextra_requirements.txt\\\\nindex.html\\\\nlibero\\\\nlibero.egg-info\\\\nlibero_res.md\\\\nnotebooks\\\\nrequirements.txt\\\\nscripts\\\\nsetup.py\\\\nstatic\\\\ntemplates\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.52}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"README.md\\nbenchmark_scripts\\nextra_requirements.txt\\nindex.html\\nlibero\\nlibero.egg-info\\nlibero_res.md\\nnotebooks\\nrequirements.txt\\nscripts\\nsetup.py\\nstatic\\ntemplates\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 166_

<details><summary>Logged reasoning block</summary>

```text
The structure is:
- `/root/LIBERO-plus/` - repo root (has setup.py)
- `/root/LIBERO-plus/libero/` - top-level Python package (has `libero.__init__.py` at `/root/LIBERO-plus/libero/libero/__init__.py`)
- So from `/root/LIBERO-plus/`, `import libero.libero` would work

There's `libero.egg-info` which means it was installed with `pip install -e .`. So the package should be importable. Let me check if the conda env has it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "ff9c2a82-2a9e-47f2-a37e-bcc7f8eb9ae9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019jbE3n91QuGKv1yDaLN85i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1220,
      "cache_read_input_tokens": 122628,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1220
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

_source line 167_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_014psHXhfcfTpCRJgvHXF63d`</summary>

```json
{
  "server": "westd-34142",
  "account": "root",
  "command": "ls /root/LIBERO-plus/libero.egg-info/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "dbf5c22a-49f6-4377-bfac-38c358a7b9f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019jbE3n91QuGKv1yDaLN85i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1220,
      "cache_read_input_tokens": 122628,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1220
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

_source line 168 · 2026-05-15T18:02:50.830Z_

<details><summary>↩ Tool result · `toolu_014psHXhfcfTpCRJgvHXF63d`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"PKG-INFO\\nSOURCES.txt\\ndependency_links.txt\\neager_resources.txt\\nentry_points.txt\\ntop_level.txt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "2dd4c930-3cf6-4ffb-82af-103308c06d4c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"PKG-INFO\\\\nSOURCES.txt\\\\ndependency_links.txt\\\\neager_resources.txt\\\\nentry_points.txt\\\\ntop_level.txt\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"PKG-INFO\\nSOURCES.txt\\ndependency_links.txt\\neager_resources.txt\\nentry_points.txt\\ntop_level.txt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 169_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01XkkxTwNbdUqfasBq7hwxYm`</summary>

```json
{
  "server": "westd-34142",
  "account": "root",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"import libero; print(libero.__file__)\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "b4fa2f0f-b40f-4b40-b890-73179464f0ed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019jbE3n91QuGKv1yDaLN85i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1220,
      "cache_read_input_tokens": 122628,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1220
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

_source line 170 · 2026-05-15T18:02:51.430Z_

<details><summary>↩ Tool result · `toolu_01XkkxTwNbdUqfasBq7hwxYm`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"None\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.58}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "d0ab40fb-c17d-4c21-8f4c-94495c88d49e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"None\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.58}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"None\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.58}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 171_

<details><summary>Logged reasoning block</summary>

```text
`import libero` works (returns None for `__file__` which means it's a namespace package). The issue was that my inline Python used `sys.path.insert(0, '/root/LIBERO-plus/libero')` which made Python find `/root/LIBERO-plus/libero/libero/` as the `libero` package directly, bypassing the egg-info setup.

Since the package is pip-installed, I just need to remove the `sys.path.insert` line. Let me re-run the test with the proper import path.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "980ab91b-3637-4052-a71b-b2a9597f0188",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016asLyq7nwuxY2aw3B5Y7t5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 648,
      "cache_read_input_tokens": 123848,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 648
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

_source line 172_

Package 已 pip 安装。重新跑 `_add_N` 发现测试（不插 sys.path）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "cbaef8d9-7bbc-42cd-b41f-fad4933401f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016asLyq7nwuxY2aw3B5Y7t5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 648,
      "cache_read_input_tokens": 123848,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 648
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

_source line 173_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_017J3rV4P83kKCVyRaZejBSu`</summary>

```json
{
  "server": "westd-34142",
  "account": "root",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/meta_brain_lora_routing && python3 << 'PYEOF'\nimport sys, os, re\nfrom pathlib import Path\nfrom libero.libero import benchmark, get_libero_path\n\nbenchmark_dict = benchmark.get_benchmark_dict()\nsuite = benchmark_dict[\"libero_spatial\"]()\nbddl_root = Path(get_libero_path(\"bddl_files\"))\nprint(f\"Total tasks in libero_spatial suite: {suite.n_tasks}\")\n\nadd_tasks = []\nskipped = 0\nfor i in range(suite.n_tasks):\n    task = suite.get_task(i)\n    name = getattr(task, \"name\", \"\") or getattr(task, \"bddl_file\", \"\")\n    clean = name.replace(\".bddl\", \"\")\n    if not re.search(r\"_add_\\d+$\", clean):\n        continue\n    bddl_path = str(bddl_root / task.problem_folder / task.bddl_file)\n    if not os.path.exists(bddl_path):\n        skipped += 1\n        continue\n    add_tasks.append({\"idx\": i, \"name\": clean, \"lang\": task.language, \"bddl\": bddl_path})\n\nprint(f\"Found {len(add_tasks)} _add_N tasks ({skipped} skipped)\")\nfor t in add_tasks[:5]:\n    print(f'  [{t[\"idx\"]}] {t[\"name\"]} -> {t[\"lang\"][:70]}')\nprint(\"...\")\nfor t in add_tasks[-3:]:\n    print(f'  [{t[\"idx\"]}] {t[\"name\"]} -> {t[\"lang\"][:70]}')\nPYEOF"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "0aa19ebe-738b-488e-a69d-4e8e7bbc4b2b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016asLyq7nwuxY2aw3B5Y7t5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 648,
      "cache_read_input_tokens": 123848,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 648
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

_source line 174 · 2026-05-15T18:03:05.902Z_

<details><summary>↩ Tool result · `toolu_017J3rV4P83kKCVyRaZejBSu`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816,\\n\\n... [截断: 输出过长，省略 6754 字符] ...\\n\\n1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036, 2037, 2038, 2039, 2040, 2041, 2042, 2043, 2044, 2045, 2046, 2047, 2048, 2049, 2050, 2051, 2052, 2053, 2054, 2055, 2056, 2057, 2058, 2059, 2060, 2061, 2062, 2063, 2064, 2065, 2066, 2067, 2068, 2069, 2070, 2071, 2072, 2073, 2074, 2075, 2076, 2077, 2078, 2079, 2080, 2081, 2082, 2083, 2084, 2085, 2086, 2087, 2088, 2089, 2090, 2091, 2092, 2093, 2094, 2095, 2096, 2097, 2098, 2099, 2100, 2101, 2102, 2103, 2104, 2105, 2106, 2107, 2108, 2109, 2110, 2111, 2112, 2113, 2114, 2115, 2116, 2117, 2118, 2119, 2120, 2121, 2122, 2123, 2124, 2125, 2126, 2127, 2128, 2129, 2130, 2131, 2132, 2133, 2134, 2135, 2136, 2137, 2138, 2139, 2140, 2141, 2142, 2143, 2144, 2145, 2146, 2147, 2148, 2149, 2150, 2151, 2152, 2153, 2154, 2155, 2156, 2157, 2158, 2159, 2160, 2161, 2162, 2163, 2164, 2165, 2166, 2167, 2168, 2169, 2170, 2171, 2172, 2173, 2174, 2175, 2176, 2177, 2178, 2179, 2180, 2181, 2182, 2183, 2184, 2185, 2186, 2187, 2188, 2189, 2190, 2191, 2192, 2193, 2194, 2195, 2196, 2197, 2198, 2199, 2200, 2201, 2202, 2203, 2204, 2205, 2206, 2207, 2208, 2209, 2210, 2211, 2212, 2213, 2214, 2215, 2216, 2217, 2218, 2219, 2220, 2221, 2222, 2223, 2224, 2225, 2226, 2227, 2228, 2229, 2230, 2231, 2232, 2233, 2234, 2235, 2236, 2237, 2238, 2239, 2240, 2241, 2242, 2243, 2244, 2245, 2246, 2247, 2248, 2249, 2250, 2251, 2252, 2253, 2254, 2255, 2256, 2257, 2258, 2259, 2260, 2261, 2262, 2263, 2264, 2265, 2266, 2267, 2268, 2269, 2270, 2271, 2272, 2273, 2274, 2275, 2276, 2277, 2278, 2279, 2280, 2281, 2282, 2283, 2284, 2285, 2286, 2287, 2288, 2289, 2290, 2291, 2292, 2293, 2294, 2295, 2296, 2297, 2298, 2299, 2300, 2301, 2302, 2303, 2304, 2305, 2306, 2307, 2308, 2309, 2310, 2311, 2312, 2313, 2314, 2315, 2316, 2317, 2318, 2319, 2320, 2321, 2322, 2323, 2324, 2325, 2326, 2327, 2328, 2329, 2330, 2331, 2332, 2333, 2334, 2335, 2336, 2337, 2338, 2339, 2340, 2341, 2342, 2343, 2344, 2345, 2346, 2347, 2348, 2349, 2350, 2351, 2352, 2353, 2354, 2355, 2356, 2357, 2358, 2359, 2360, 2361, 2362, 2363, 2364, 2365, 2366, 2367, 2368, 2369, 2370, 2371, 2372, 2373, 2374, 2375, 2376, 2377, 2378, 2379, 2380, 2381, 2382, 2383, 2384, 2385, 2386, 2387, 2388, 2389, 2390, 2391, 2392, 2393, 2394, 2395, 2396, 2397, 2398, 2399, 2400, 2401]\\nTotal tasks in libero_spatial suite: 2402\\nFound 208 _add_N tasks (0 skipped)\\n  [1725] pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate_add_10 -> pick up the black bowl between the plate and the ramekin and place it \\n  [1726] pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate_add_11 -> pick up the black bowl between the plate and the ramekin and place it \\n  [1727] pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate_add_12 -> pick up the black bowl between the plate and the ramekin and place it \\n  [1728] pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate_add_13 -> pick up the black bowl between the plate and the ramekin and place it \\n  [1729] pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate_add_14 -> pick up the black bowl between the plate and the ramekin and place it \\n...\\n  [2088] pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate_add_7 -> pick up the black bowl on the wooden cabinet and place it on the plate\\n  [2089] pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate_add_8 -> pick up the black bowl on the wooden cabinet and place it on the plate\\n  [2090] pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate_add_9 -> pick up the black bowl on the wooden cabinet and place it on the plate\\n\", \"stderr\": \"[robosuite WARNING] No private macro file found! (__init__.py:7)\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\nGym has been unmaintained since 2022 and does not support NumPy 2.0 amongst other critical functionality.\\nPlease upgrade to Gymnasium, the maintained drop-in replacement of Gym, or contact the authors of your software and request that they upgrade.\\nSee the migration guide at https://gymnasium.farama.org/introduction/migration_guide/ for additional information.\\n\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.21}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "bb926432-1d12-48ee-bc0e-d0861cfea790",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816,\\\\n\\\\n... [截断: 输出过长，省略 6754 字符] ...\\\\n\\\\n1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036, 2037, 2038, 2039, 2040, 2041, 2042, 2043, 2044, 2045, 2046, 2047, 2048, 2049, 2050, 2051, 2052, 2053, 2054, 2055, 2056, 2057, 2058, 2059, 2060, 2061, 2062, 2063, 2064, 2065, 2066, 2067, 2068, 2069, 2070, 2071, 2072, 2073, 2074, 2075, 2076, 2077, 2078, 2079, 2080, 2081, 2082, 2083, 2084, 2085, 2086, 2087, 2088, 2089, 2090, 2091, 2092, 2093, 2094, 2095, 2096, 2097, 2098, 2099, 2100, 2101, 2102, 2103, 2104, 2105, 2106, 2107, 2108, 2109, 2110, 2111, 2112, 2113, 2114, 2115, 2116, 2117, 2118, 2119, 2120, 2121, 2122, 2123, 2124, 2125, 2126, 2127, 2128, 2129, 2130, 2131, 2132, 2133, 2134, 2135, 2136, 2137, 2138, 2139, 2140, 2141, 2142, 2143, 2144, 2145, 2146, 2147, 2148, 2149, 2150, 2151, 2152, 2153, 2154, 2155, 2156, 2157, 2158, 2159, 2160, 2161, 2162, 2163, 2164, 2165, 2166, 2167, 2168, 2169, 2170, 2171, 2172, 2173, 2174, 2175, 2176, 2177, 2178, 2179, 2180, 2181, 2182, 2183, 2184, 2185, 2186, 2187, 2188, 2189, 2190, 2191, 2192, 2193, 2194, 2195, 2196, 2197, 2198, 2199, 2200, 2201, 2202, 2203, 2204, 2205, 2206, 2207, 2208, 2209, 2210, 2211, 2212, 2213, 2214, 2215, 2216, 2217, 2218, 2219, 2220, 2221, 2222, 2223, 2224, 2225, 2226, 2227, 2228, 2229, 2230, 2231, 2232, 2233, 2234, 2235, 2236, 2237, 2238, 2239, 2240, 2241, 2242, 2243, 2244, 2245, 2246, 2247, 2248, 2249, 2250, 2251, 2252, 2253, 2254, 2255, 2256, 2257, 2258, 2259, 2260, 2261, 2262, 2263, 2264, 2265, 2266, 2267, 2268, 2269, 2270, 2271, 2272, 2273, 2274, 2275, 2276, 2277, 2278, 2279, 2280, 2281, 2282, 2283, 2284, 2285, 2286, 2287, 2288, 2289, 2290, 2291, 2292, 2293, 2294, 2295, 2296, 2297, 2298, 2299, 2300, 2301, 2302, 2303, 2304, 2305, 2306, 2307, 2308, 2309, 2310, 2311, 2312, 2313, 2314, 2315, 2316, 2317, 2318, 2319, 2320, 2321, 2322, 2323, 2324, 2325, 2326, 2327, 2328, 2329, 2330, 2331, 2332, 2333, 2334, 2335, 2336, 2337, 2338, 2339, 2340, 2341, 2342, 2343, 2344, 2345, 2346, 2347, 2348, 2349, 2350, 2351, 2352, 2353, 2354, 2355, 2356, 2357, 2358, 2359, 2360, 2361, 2362, 2363, 2364, 2365, 2366, 2367, 2368, 2369, 2370, 2371, 2372, 2373, 2374, 2375, 2376, 2377, 2378, 2379, 2380, 2381, 2382, 2383, 2384, 2385, 2386, 2387, 2388, 2389, 2390, 2391, 2392, 2393, 2394, 2395, 2396, 2397, 2398, 2399, 2400, 2401]\\\\nTotal tasks in libero_spatial suite: 2402\\\\nFound 208 _add_N tasks (0 skipped)\\\\n  [1725] pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate_add_10 -> pick up the black bowl between the plate and the ramekin and place it \\\\n  [1726] pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate_add_11 -> pick up the black bowl between the plate and the ramekin and place it \\\\n  [1727] pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate_add_12 -> pick up the black bowl between the plate and the ramekin and place it \\\\n  [1728] pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate_add_13 -> pick up the black bowl between the plate and the ramekin and place it \\\\n  [1729] pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate_add_14 -> pick up the black bowl between the plate and the ramekin and place it \\\\n...\\\\n  [2088] pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate_add_7 -> pick up the black bowl on the wooden cabinet and place it on the plate\\\\n  [2089] pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate_add_8 -> pick up the black bowl on the wooden cabinet and place it on the plate\\\\n  [2090] pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate_add_9 -> pick up the black bowl on the wooden cabinet and place it on the plate\\\\n\\\", \\\"stderr\\\": \\\"[robosuite WARNING] No private macro file found! (__init__.py:7)\\\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\\\nGym has been unmaintained since 2022 and does not support NumPy 2.0 amongst other critical functionality.\\\\nPlease upgrade to Gymnasium, the maintained drop-in replacement of Gym, or contact the authors of your software and request that they upgrade.\\\\nSee the migration guide at https://gymnasium.farama.org/introduction/migration_guide/ for additional information.\\\\n\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 4.21}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816,\\n\\n... [截断: 输出过长，省略 6754 字符] ...\\n\\n1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036, 2037, 2038, 2039, 2040, 2041, 2042, 2043, 2044, 2045, 2046, 2047, 2048, 2049, 2050, 2051, 2052, 2053, 2054, 2055, 2056, 2057, 2058, 2059, 2060, 2061, 2062, 2063, 2064, 2065, 2066, 2067, 2068, 2069, 2070, 2071, 2072, 2073, 2074, 2075, 2076, 2077, 2078, 2079, 2080, 2081, 2082, 2083, 2084, 2085, 2086, 2087, 2088, 2089, 2090, 2091, 2092, 2093, 2094, 2095, 2096, 2097, 2098, 2099, 2100, 2101, 2102, 2103, 2104, 2105, 2106, 2107, 2108, 2109, 2110, 2111, 2112, 2113, 2114, 2115, 2116, 2117, 2118, 2119, 2120, 2121, 2122, 2123, 2124, 2125, 2126, 2127, 2128, 2129, 2130, 2131, 2132, 2133, 2134, 2135, 2136, 2137, 2138, 2139, 2140, 2141, 2142, 2143, 2144, 2145, 2146, 2147, 2148, 2149, 2150, 2151, 2152, 2153, 2154, 2155, 2156, 2157, 2158, 2159, 2160, 2161, 2162, 2163, 2164, 2165, 2166, 2167, 2168, 2169, 2170, 2171, 2172, 2173, 2174, 2175, 2176, 2177, 2178, 2179, 2180, 2181, 2182, 2183, 2184, 2185, 2186, 2187, 2188, 2189, 2190, 2191, 2192, 2193, 2194, 2195, 2196, 2197, 2198, 2199, 2200, 2201, 2202, 2203, 2204, 2205, 2206, 2207, 2208, 2209, 2210, 2211, 2212, 2213, 2214, 2215, 2216, 2217, 2218, 2219, 2220, 2221, 2222, 2223, 2224, 2225, 2226, 2227, 2228, 2229, 2230, 2231, 2232, 2233, 2234, 2235, 2236, 2237, 2238, 2239, 2240, 2241, 2242, 2243, 2244, 2245, 2246, 2247, 2248, 2249, 2250, 2251, 2252, 2253, 2254, 2255, 2256, 2257, 2258, 2259, 2260, 2261, 2262, 2263, 2264, 2265, 2266, 2267, 2268, 2269, 2270, 2271, 2272, 2273, 2274, 2275, 2276, 2277, 2278, 2279, 2280, 2281, 2282, 2283, 2284, 2285, 2286, 2287, 2288, 2289, 2290, 2291, 2292, 2293, 2294, 2295, 2296, 2297, 2298, 2299, 2300, 2301, 2302, 2303, 2304, 2305, 2306, 2307, 2308, 2309, 2310, 2311, 2312, 2313, 2314, 2315, 2316, 2317, 2318, 2319, 2320, 2321, 2322, 2323, 2324, 2325, 2326, 2327, 2328, 2329, 2330, 2331, 2332, 2333, 2334, 2335, 2336, 2337, 2338, 2339, 2340, 2341, 2342, 2343, 2344, 2345, 2346, 2347, 2348, 2349, 2350, 2351, 2352, 2353, 2354, 2355, 2356, 2357, 2358, 2359, 2360, 2361, 2362, 2363, 2364, 2365, 2366, 2367, 2368, 2369, 2370, 2371, 2372, 2373, 2374, 2375, 2376, 2377, 2378, 2379, 2380, 2381, 2382, 2383, 2384, 2385, 2386, 2387, 2388, 2389, 2390, 2391, 2392, 2393, 2394, 2395, 2396, 2397, 2398, 2399, 2400, 2401]\\nTotal tasks in libero_spatial suite: 2402\\nFound 208 _add_N tasks (0 skipped)\\n  [1725] pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate_add_10 -> pick up the black bowl between the plate and the ramekin and place it \\n  [1726] pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate_add_11 -> pick up the black bowl between the plate and the ramekin and place it \\n  [1727] pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate_add_12 -> pick up the black bowl between the plate and the ramekin and place it \\n  [1728] pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate_add_13 -> pick up the black bowl between the plate and the ramekin and place it \\n  [1729] pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate_add_14 -> pick up the black bowl between the plate and the ramekin and place it \\n...\\n  [2088] pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate_add_7 -> pick up the black bowl on the wooden cabinet and place it on the plate\\n  [2089] pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate_add_8 -> pick up the black bowl on the wooden cabinet and place it on the plate\\n  [2090] pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate_add_9 -> pick up the black bowl on the wooden cabinet and place it on the plate\\n\", \"stderr\": \"[robosuite WARNING] No private macro file found! (__init__.py:7)\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\nGym has been unmaintained since 2022 and does not support NumPy 2.0 amongst other critical functionality.\\nPlease upgrade to Gymnasium, the maintained drop-in replacement of Gym, or contact the authors of your software and request that they upgrade.\\nSee the migration guide at https://gymnasium.farama.org/introduction/migration_guide/ for additional information.\\n\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.21}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 175_

**208 个 `_add_N` 任务全部发现，0 跳过。** 总 suite 有 2402 个任务。现在验证 `_add_N` 环境能正确创建（不需要 policy，纯环境加载测试）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "aa2db597-cd21-4410-9a76-188f16cd8271",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014skiHJ1C7akjmmCVwt5Hfo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5723,
      "cache_read_input_tokens": 124496,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5723
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

_source line 176_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_018zBmPd37jhJ9g7MMSokst4`</summary>

```json
{
  "server": "westd-34142",
  "account": "root",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=1 python3 << 'PYEOF'\nimport sys, os, re\nfrom pathlib import Path\nfrom libero.libero import benchmark, get_libero_path\nfrom libero.libero.envs import OffScreenRenderEnv\nimport numpy as np\n\nbenchmark_dict = benchmark.get_benchmark_dict()\nsuite = benchmark_dict[\"libero_spatial\"]()\nbddl_root = Path(get_libero_path(\"bddl_files\"))\n\n# Find first 2 _add tasks\nadd_tasks = []\nfor i in range(suite.n_tasks):\n    task = suite.get_task(i)\n    name = getattr(task, \"name\", \"\") or getattr(task, \"bddl_file\", \"\")\n    clean = name.replace(\".bddl\", \"\")\n    if re.search(r\"_add_\\d+$\", clean):\n        bddl_path = str(bddl_root / task.problem_folder / task.bddl_file)\n        add_tasks.append({\"idx\": i, \"name\": clean, \"lang\": task.language, \"bddl\": bddl_path})\n    if len(add_tasks) >= 2:\n        break\n\nfor t in add_tasks:\n    print(f\"\\nTesting: {t['name']}\")\n    print(f\"  BDDL: {t['bddl']}\")\n    try:\n        env = OffScreenRenderEnv(\n            bddl_file_name=t[\"bddl\"],\n            camera_heights=256,\n            camera_widths=256,\n        )\n        init_states = suite.get_task_init_states(t[\"idx\"])\n        print(f\"  init_states shape: {init_states.shape}\")\n        obs = env.set_init_state(init_states[0])\n        print(f\"  obs keys: {list(obs.keys())}\")\n        print(f\"  agentview_image shape: {obs['agentview_image'].shape}\")\n        \n        # Check that env has extra objects (distractor signal)\n        n_objects = len(env.env.model.mujoco_objects) if hasattr(env.env, 'model') else 'N/A'\n        print(f\"  mujoco_objects count: {n_objects}\")\n        \n        env.close()\n        print(f\"  ENV LOAD OK\")\n    except Exception as e:\n        print(f\"  FAILED: {e}\")\n\nprint(\"\\nEnvironment creation test passed!\")\nPYEOF",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "b82fa6e0-283c-48a1-8cbc-714cba793fb6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014skiHJ1C7akjmmCVwt5Hfo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5723,
      "cache_read_input_tokens": 124496,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5723
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

_source line 177 · 2026-05-15T18:03:30.451Z_

<details><summary>↩ Tool result · `toolu_018zBmPd37jhJ9g7MMSokst4`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816,\\n\\n... [截断: 输出过长，省略 8449 字符] ...\\n\\n5, 2256, 2257, 2258, 2259, 2260, 2261, 2262, 2263, 2264, 2265, 2266, 2267, 2268, 2269, 2270, 2271, 2272, 2273, 2274, 2275, 2276, 2277, 2278, 2279, 2280, 2281, 2282, 2283, 2284, 2285, 2286, 2287, 2288, 2289, 2290, 2291, 2292, 2293, 2294, 2295, 2296, 2297, 2298, 2299, 2300, 2301, 2302, 2303, 2304, 2305, 2306, 2307, 2308, 2309, 2310, 2311, 2312, 2313, 2314, 2315, 2316, 2317, 2318, 2319, 2320, 2321, 2322, 2323, 2324, 2325, 2326, 2327, 2328, 2329, 2330, 2331, 2332, 2333, 2334, 2335, 2336, 2337, 2338, 2339, 2340, 2341, 2342, 2343, 2344, 2345, 2346, 2347, 2348, 2349, 2350, 2351, 2352, 2353, 2354, 2355, 2356, 2357, 2358, 2359, 2360, 2361, 2362, 2363, 2364, 2365, 2366, 2367, 2368, 2369, 2370, 2371, 2372, 2373, 2374, 2375, 2376, 2377, 2378, 2379, 2380, 2381, 2382, 2383, 2384, 2385, 2386, 2387, 2388, 2389, 2390, 2391, 2392, 2393, 2394, 2395, 2396, 2397, 2398, 2399, 2400, 2401]\\n\\nTesting: pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate_add_10\\n  BDDL: /root/LIBERO-plus/libero/libero/bddl_files/libero_spatial/pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate_add_10.bddl\\n  init_states shape: (1, 118)\\n  obs keys: ['robot0_joint_pos', 'robot0_joint_pos_cos', 'robot0_joint_pos_sin', 'robot0_joint_vel', 'robot0_eef_pos', 'robot0_eef_quat', 'robot0_gripper_qpos', 'robot0_gripper_qvel', 'agentview_image', 'robot0_eye_in_hand_image', 'akita_black_bowl_1_pos', 'akita_black_bowl_1_quat', 'akita_black_bowl_1_to_robot0_eef_pos', 'akita_black_bowl_1_to_robot0_eef_quat', 'akita_black_bowl_2_pos', 'akita_black_bowl_2_quat', 'akita_black_bowl_2_to_robot0_eef_pos', 'akita_black_bowl_2_to_robot0_eef_quat', 'cookies_1_pos', 'cookies_1_quat', 'cookies_1_to_robot0_eef_pos', 'cookies_1_to_robot0_eef_quat', 'glazed_rim_porcelain_ramekin_1_pos', 'glazed_rim_porcelain_ramekin_1_quat', 'glazed_rim_porcelain_ramekin_1_to_robot0_eef_pos', 'glazed_rim_porcelain_ramekin_1_to_robot0_eef_quat', 'plate_1_pos', 'plate_1_quat', 'plate_1_to_robot0_eef_pos', 'plate_1_to_robot0_eef_quat', 'box_of_yogurt__1_1_pos', 'box_of_yogurt__1_1_quat', 'box_of_yogurt__1_1_to_robot0_eef_pos', 'box_of_yogurt__1_1_to_robot0_eef_quat', 'box_of_shampoo__1_1_pos', 'box_of_shampoo__1_1_quat', 'box_of_shampoo__1_1_to_robot0_eef_pos', 'box_of_shampoo__1_1_to_robot0_eef_quat', 'robot0_proprio-state', 'object-state']\\n  agentview_image shape: (256, 256, 3)\\n  mujoco_objects count: 9\\n  ENV LOAD OK\\n\\nTesting: pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate_add_11\\n  BDDL: /root/LIBERO-plus/libero/libero/bddl_files/libero_spatial/pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate_add_11.bddl\\n  init_states shape: (1, 118)\\n  obs keys: ['robot0_joint_pos', 'robot0_joint_pos_cos', 'robot0_joint_pos_sin', 'robot0_joint_vel', 'robot0_eef_pos', 'robot0_eef_quat', 'robot0_gripper_qpos', 'robot0_gripper_qvel', 'agentview_image', 'robot0_eye_in_hand_image', 'akita_black_bowl_1_pos', 'akita_black_bowl_1_quat', 'akita_black_bowl_1_to_robot0_eef_pos', 'akita_black_bowl_1_to_robot0_eef_quat', 'akita_black_bowl_2_pos', 'akita_black_bowl_2_quat', 'akita_black_bowl_2_to_robot0_eef_pos', 'akita_black_bowl_2_to_robot0_eef_quat', 'cookies_1_pos', 'cookies_1_quat', 'cookies_1_to_robot0_eef_pos', 'cookies_1_to_robot0_eef_quat', 'glazed_rim_porcelain_ramekin_1_pos', 'glazed_rim_porcelain_ramekin_1_quat', 'glazed_rim_porcelain_ramekin_1_to_robot0_eef_pos', 'glazed_rim_porcelain_ramekin_1_to_robot0_eef_quat', 'plate_1_pos', 'plate_1_quat', 'plate_1_to_robot0_eef_pos', 'plate_1_to_robot0_eef_quat', 'bottle_of_aspirin_1_pos', 'bottle_of_aspirin_1_quat', 'bottle_of_aspirin_1_to_robot0_eef_pos', 'bottle_of_aspirin_1_to_robot0_eef_quat', 'bag_of_yeast_1_pos', 'bag_of_yeast_1_quat', 'bag_of_yeast_1_to_robot0_eef_pos', 'bag_of_yeast_1_to_robot0_eef_quat', 'robot0_proprio-state', 'object-state']\\n  agentview_image shape: (256, 256, 3)\\n  mujoco_objects count: 9\\n  ENV LOAD OK\\n\\nEnvironment creation test passed!\\n\", \"stderr\": \"[robosuite WARNING] No private macro file found! (__init__.py:7)\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\nGym has been unmaintained since 2022 and does not support NumPy 2.0 amongst other critical functionality.\\nPlease upgrade to Gymnasium, the maintained drop-in replacement of Gym, or contact the authors of your software and request that they upgrade.\\nSee the migration guide at https://gymnasium.farama.org/introduction/migration_guide/ for additional information.\\n\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.05}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "03a8313c-1983-4f0f-b626-20519a75814a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816,\\\\n\\\\n... [截断: 输出过长，省略 8449 字符] ...\\\\n\\\\n5, 2256, 2257, 2258, 2259, 2260, 2261, 2262, 2263, 2264, 2265, 2266, 2267, 2268, 2269, 2270, 2271, 2272, 2273, 2274, 2275, 2276, 2277, 2278, 2279, 2280, 2281, 2282, 2283, 2284, 2285, 2286, 2287, 2288, 2289, 2290, 2291, 2292, 2293, 2294, 2295, 2296, 2297, 2298, 2299, 2300, 2301, 2302, 2303, 2304, 2305, 2306, 2307, 2308, 2309, 2310, 2311, 2312, 2313, 2314, 2315, 2316, 2317, 2318, 2319, 2320, 2321, 2322, 2323, 2324, 2325, 2326, 2327, 2328, 2329, 2330, 2331, 2332, 2333, 2334, 2335, 2336, 2337, 2338, 2339, 2340, 2341, 2342, 2343, 2344, 2345, 2346, 2347, 2348, 2349, 2350, 2351, 2352, 2353, 2354, 2355, 2356, 2357, 2358, 2359, 2360, 2361, 2362, 2363, 2364, 2365, 2366, 2367, 2368, 2369, 2370, 2371, 2372, 2373, 2374, 2375, 2376, 2377, 2378, 2379, 2380, 2381, 2382, 2383, 2384, 2385, 2386, 2387, 2388, 2389, 2390, 2391, 2392, 2393, 2394, 2395, 2396, 2397, 2398, 2399, 2400, 2401]\\\\n\\\\nTesting: pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate_add_10\\\\n  BDDL: /root/LIBERO-plus/libero/libero/bddl_files/libero_spatial/pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate_add_10.bddl\\\\n  init_states shape: (1, 118)\\\\n  obs keys: ['robot0_joint_pos', 'robot0_joint_pos_cos', 'robot0_joint_pos_sin', 'robot0_joint_vel', 'robot0_eef_pos', 'robot0_eef_quat', 'robot0_gripper_qpos', 'robot0_gripper_qvel', 'agentview_image', 'robot0_eye_in_hand_image', 'akita_black_bowl_1_pos', 'akita_black_bowl_1_quat', 'akita_black_bowl_1_to_robot0_eef_pos', 'akita_black_bowl_1_to_robot0_eef_quat', 'akita_black_bowl_2_pos', 'akita_black_bowl_2_quat', 'akita_black_bowl_2_to_robot0_eef_pos', 'akita_black_bowl_2_to_robot0_eef_quat', 'cookies_1_pos', 'cookies_1_quat', 'cookies_1_to_robot0_eef_pos', 'cookies_1_to_robot0_eef_quat', 'glazed_rim_porcelain_ramekin_1_pos', 'glazed_rim_porcelain_ramekin_1_quat', 'glazed_rim_porcelain_ramekin_1_to_robot0_eef_pos', 'glazed_rim_porcelain_ramekin_1_to_robot0_eef_quat', 'plate_1_pos', 'plate_1_quat', 'plate_1_to_robot0_eef_pos', 'plate_1_to_robot0_eef_quat', 'box_of_yogurt__1_1_pos', 'box_of_yogurt__1_1_quat', 'box_of_yogurt__1_1_to_robot0_eef_pos', 'box_of_yogurt__1_1_to_robot0_eef_quat', 'box_of_shampoo__1_1_pos', 'box_of_shampoo__1_1_quat', 'box_of_shampoo__1_1_to_robot0_eef_pos', 'box_of_shampoo__1_1_to_robot0_eef_quat', 'robot0_proprio-state', 'object-state']\\\\n  agentview_image shape: (256, 256, 3)\\\\n  mujoco_objects count: 9\\\\n  ENV LOAD OK\\\\n\\\\nTesting: pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate_add_11\\\\n  BDDL: /root/LIBERO-plus/libero/libero/bddl_files/libero_spatial/pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate_add_11.bddl\\\\n  init_states shape: (1, 118)\\\\n  obs keys: ['robot0_joint_pos', 'robot0_joint_pos_cos', 'robot0_joint_pos_sin', 'robot0_joint_vel', 'robot0_eef_pos', 'robot0_eef_quat', 'robot0_gripper_qpos', 'robot0_gripper_qvel', 'agentview_image', 'robot0_eye_in_hand_image', 'akita_black_bowl_1_pos', 'akita_black_bowl_1_quat', 'akita_black_bowl_1_to_robot0_eef_pos', 'akita_black_bowl_1_to_robot0_eef_quat', 'akita_black_bowl_2_pos', 'akita_black_bowl_2_quat', 'akita_black_bowl_2_to_robot0_eef_pos', 'akita_black_bowl_2_to_robot0_eef_quat', 'cookies_1_pos', 'cookies_1_quat', 'cookies_1_to_robot0_eef_pos', 'cookies_1_to_robot0_eef_quat', 'glazed_rim_porcelain_ramekin_1_pos', 'glazed_rim_porcelain_ramekin_1_quat', 'glazed_rim_porcelain_ramekin_1_to_robot0_eef_pos', 'glazed_rim_porcelain_ramekin_1_to_robot0_eef_quat', 'plate_1_pos', 'plate_1_quat', 'plate_1_to_robot0_eef_pos', 'plate_1_to_robot0_eef_quat', 'bottle_of_aspirin_1_pos', 'bottle_of_aspirin_1_quat', 'bottle_of_aspirin_1_to_robot0_eef_pos', 'bottle_of_aspirin_1_to_robot0_eef_quat', 'bag_of_yeast_1_pos', 'bag_of_yeast_1_quat', 'bag_of_yeast_1_to_robot0_eef_pos', 'bag_of_yeast_1_to_robot0_eef_quat', 'robot0_proprio-state', 'object-state']\\\\n  agentview_image shape: (256, 256, 3)\\\\n  mujoco_objects count: 9\\\\n  ENV LOAD OK\\\\n\\\\nEnvironment creation test passed!\\\\n\\\", \\\"stderr\\\": \\\"[robosuite WARNING] No private macro file found! (__init__.py:7)\\\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\\\nGym has been unmaintained since 2022 and does not support NumPy 2.0 amongst other critical functionality.\\\\nPlease upgrade to Gymnasium, the maintained drop-in replacement of Gym, or contact the authors of your software and request that they upgrade.\\\\nSee the migration guide at https://gymnasium.farama.org/introduction/migration_guide/ for additional information.\\\\n\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 7.05}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816,\\n\\n... [截断: 输出过长，省略 8449 字符] ...\\n\\n5, 2256, 2257, 2258, 2259, 2260, 2261, 2262, 2263, 2264, 2265, 2266, 2267, 2268, 2269, 2270, 2271, 2272, 2273, 2274, 2275, 2276, 2277, 2278, 2279, 2280, 2281, 2282, 2283, 2284, 2285, 2286, 2287, 2288, 2289, 2290, 2291, 2292, 2293, 2294, 2295, 2296, 2297, 2298, 2299, 2300, 2301, 2302, 2303, 2304, 2305, 2306, 2307, 2308, 2309, 2310, 2311, 2312, 2313, 2314, 2315, 2316, 2317, 2318, 2319, 2320, 2321, 2322, 2323, 2324, 2325, 2326, 2327, 2328, 2329, 2330, 2331, 2332, 2333, 2334, 2335, 2336, 2337, 2338, 2339, 2340, 2341, 2342, 2343, 2344, 2345, 2346, 2347, 2348, 2349, 2350, 2351, 2352, 2353, 2354, 2355, 2356, 2357, 2358, 2359, 2360, 2361, 2362, 2363, 2364, 2365, 2366, 2367, 2368, 2369, 2370, 2371, 2372, 2373, 2374, 2375, 2376, 2377, 2378, 2379, 2380, 2381, 2382, 2383, 2384, 2385, 2386, 2387, 2388, 2389, 2390, 2391, 2392, 2393, 2394, 2395, 2396, 2397, 2398, 2399, 2400, 2401]\\n\\nTesting: pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate_add_10\\n  BDDL: /root/LIBERO-plus/libero/libero/bddl_files/libero_spatial/pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate_add_10.bddl\\n  init_states shape: (1, 118)\\n  obs keys: ['robot0_joint_pos', 'robot0_joint_pos_cos', 'robot0_joint_pos_sin', 'robot0_joint_vel', 'robot0_eef_pos', 'robot0_eef_quat', 'robot0_gripper_qpos', 'robot0_gripper_qvel', 'agentview_image', 'robot0_eye_in_hand_image', 'akita_black_bowl_1_pos', 'akita_black_bowl_1_quat', 'akita_black_bowl_1_to_robot0_eef_pos', 'akita_black_bowl_1_to_robot0_eef_quat', 'akita_black_bowl_2_pos', 'akita_black_bowl_2_quat', 'akita_black_bowl_2_to_robot0_eef_pos', 'akita_black_bowl_2_to_robot0_eef_quat', 'cookies_1_pos', 'cookies_1_quat', 'cookies_1_to_robot0_eef_pos', 'cookies_1_to_robot0_eef_quat', 'glazed_rim_porcelain_ramekin_1_pos', 'glazed_rim_porcelain_ramekin_1_quat', 'glazed_rim_porcelain_ramekin_1_to_robot0_eef_pos', 'glazed_rim_porcelain_ramekin_1_to_robot0_eef_quat', 'plate_1_pos', 'plate_1_quat', 'plate_1_to_robot0_eef_pos', 'plate_1_to_robot0_eef_quat', 'box_of_yogurt__1_1_pos', 'box_of_yogurt__1_1_quat', 'box_of_yogurt__1_1_to_robot0_eef_pos', 'box_of_yogurt__1_1_to_robot0_eef_quat', 'box_of_shampoo__1_1_pos', 'box_of_shampoo__1_1_quat', 'box_of_shampoo__1_1_to_robot0_eef_pos', 'box_of_shampoo__1_1_to_robot0_eef_quat', 'robot0_proprio-state', 'object-state']\\n  agentview_image shape: (256, 256, 3)\\n  mujoco_objects count: 9\\n  ENV LOAD OK\\n\\nTesting: pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate_add_11\\n  BDDL: /root/LIBERO-plus/libero/libero/bddl_files/libero_spatial/pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate_add_11.bddl\\n  init_states shape: (1, 118)\\n  obs keys: ['robot0_joint_pos', 'robot0_joint_pos_cos', 'robot0_joint_pos_sin', 'robot0_joint_vel', 'robot0_eef_pos', 'robot0_eef_quat', 'robot0_gripper_qpos', 'robot0_gripper_qvel', 'agentview_image', 'robot0_eye_in_hand_image', 'akita_black_bowl_1_pos', 'akita_black_bowl_1_quat', 'akita_black_bowl_1_to_robot0_eef_pos', 'akita_black_bowl_1_to_robot0_eef_quat', 'akita_black_bowl_2_pos', 'akita_black_bowl_2_quat', 'akita_black_bowl_2_to_robot0_eef_pos', 'akita_black_bowl_2_to_robot0_eef_quat', 'cookies_1_pos', 'cookies_1_quat', 'cookies_1_to_robot0_eef_pos', 'cookies_1_to_robot0_eef_quat', 'glazed_rim_porcelain_ramekin_1_pos', 'glazed_rim_porcelain_ramekin_1_quat', 'glazed_rim_porcelain_ramekin_1_to_robot0_eef_pos', 'glazed_rim_porcelain_ramekin_1_to_robot0_eef_quat', 'plate_1_pos', 'plate_1_quat', 'plate_1_to_robot0_eef_pos', 'plate_1_to_robot0_eef_quat', 'bottle_of_aspirin_1_pos', 'bottle_of_aspirin_1_quat', 'bottle_of_aspirin_1_to_robot0_eef_pos', 'bottle_of_aspirin_1_to_robot0_eef_quat', 'bag_of_yeast_1_pos', 'bag_of_yeast_1_quat', 'bag_of_yeast_1_to_robot0_eef_pos', 'bag_of_yeast_1_to_robot0_eef_quat', 'robot0_proprio-state', 'object-state']\\n  agentview_image shape: (256, 256, 3)\\n  mujoco_objects count: 9\\n  ENV LOAD OK\\n\\nEnvironment creation test passed!\\n\", \"stderr\": \"[robosuite WARNING] No private macro file found! (__init__.py:7)\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\nGym has been unmaintained since 2022 and does not support NumPy 2.0 amongst other critical functionality.\\nPlease upgrade to Gymnasium, the maintained drop-in replacement of Gym, or contact the authors of your software and request that they upgrade.\\nSee the migration guide at https://gymnasium.farama.org/introduction/migration_guide/ for additional information.\\n\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.05}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 178_

环境创建验证通过：
- `_add_10`: 9 个 mujoco_objects（含 `box_of_yogurt`, `box_of_shampoo` 等干扰物体）
- `_add_11`: 9 个 mujoco_objects（含 `bottle_of_aspirin`, `bag_of_yeast` 等不同干扰物体）
- obs 格式正确，agentview_image `(256,256,3)`

现在跑完整 dry-run（加载 policy + 2 个 `_add` 任务 × 1 episode）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "8b1324b9-9bac-4bd5-8c34-ca1320fc750f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bcw4rZ4Bd4raKLAKLyRAHS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5758,
      "cache_read_input_tokens": 130219,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5758
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

_source line 179_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_017NZzdD4oPGfigneSzdSpFT`</summary>

```json
{
  "server": "westd-34142",
  "account": "root",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/meta_brain_lora_routing && CUDA_VISIBLE_DEVICES=1 python3 phase1/collect_expert_demos.py --perturbation_type spatial --gpu_id 0 --dry_run 2>&1",
  "timeout": 300000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "27bacc16-b016-4a4c-ab52-565c79f7371b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bcw4rZ4Bd4raKLAKLyRAHS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5758,
      "cache_read_input_tokens": 130219,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5758
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

_source line 180 · 2026-05-15T18:04:10.342Z_

<details><summary>↩ Tool result · `toolu_017NZzdD4oPGfigneSzdSpFT`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/meta_brain_lora_routing && CUDA_VISIBLE_DEVICES=1 python3 phase1/collect_expert_demos.py --perturbation_type spatial --gpu_id 0 --dry_run 2>&1'\\n\\nStdout:\\n\\n2026-05-16 02:03:41,391 [INFO] Config: type=spatial spatial_mode=add_n device=cuda:0 num_tasks=10 eps_per_cfg=3 dry_run=True\\n2026-05-16 02:03:41,391 [INFO] Loading π₀ from /root/autodl-tmp/checkpoints/pi0_base\\n2026-05-16 02:03:45,796 [INFO] Loading model...\\n2026-05-16 02:03:45,796 [INFO] train_config: TrainConfig(name='pi0_libero', project_name='openpi', exp_name=tyro.MISSING, model=Pi0Config(action_dim=32, action_horizon=50, max_token_len=48, dtype='bfloat16', paligemma_variant='gemma_2b', action_expert_variant='gemma_300m', pi05=False, discrete_state_input=False, pytorch_compile_mode='max-autotune'), weight_loader=CheckpointWeightLoader(params_path='gs://openpi-assets/checkpoints/pi0_base/params'), pytorch_weight_path=None, pytorch_training_precision='bfloat16', lr_schedule=CosineDecaySchedule(warmup_steps=1000, peak_lr=2.5e-05, decay_steps=30000, decay_lr=2.5e-06), optimizer=AdamW(b1=0.9, b2=0.95, eps=1e-08, weight_decay=1e-10, clip_gradient_norm=1.0), ema_decay=0.99, freeze_filter=Nothing(), data=LeRobotLiberoDataConfig(repo_id='physical-intelligence/libero', assets=AssetsConfig(assets_dir=None, asset_id=None), base_config=DataConfig(repo_id=None, asset_id=None, norm_stats=None, repack_transforms=Group(inputs=(), outputs=()), data_transforms=Group(inputs=(), outputs=()), model_transforms=Group(inputs=(), outputs=()), use_quantile_norm=False, action_sequence_keys=('actions',), prompt_from_task=True, rlds_data_dir=None, action_space=None, datasets=()), extra_delta_transform=True), assets_base_dir='./assets', checkpoint_base_dir='./checkpoints', seed=42, batch_size=32, num_workers=2, num_train_steps=30000, log_interval=100, save_interval=1000, keep_period=5000, overwrite=False, resume=False, wandb_enabled=True, policy_metadata=None, fsdp_devices=1)\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "ec65bdfd-be54-4b63-be0a-b7ea617530ec",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Command did not complete within 30 seconds!\\\\n\\\\nCommand: 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/meta_brain_lora_routing && CUDA_VISIBLE_DEVICES=1 python3 phase1/collect_expert_demos.py --perturbation_type spatial --gpu_id 0 --dry_run 2>&1'\\\\n\\\\nStdout:\\\\n\\\\n2026-05-16 02:03:41,391 [INFO] Config: type=spatial spatial_mode=add_n device=cuda:0 num_tasks=10 eps_per_cfg=3 dry_run=True\\\\n2026-05-16 02:03:41,391 [INFO] Loading π₀ from /root/autodl-tmp/checkpoints/pi0_base\\\\n2026-05-16 02:03:45,796 [INFO] Loading model...\\\\n2026-05-16 02:03:45,796 [INFO] train_config: TrainConfig(name='pi0_libero', project_name='openpi', exp_name=tyro.MISSING, model=Pi0Config(action_dim=32, action_horizon=50, max_token_len=48, dtype='bfloat16', paligemma_variant='gemma_2b', action_expert_variant='gemma_300m', pi05=False, discrete_state_input=False, pytorch_compile_mode='max-autotune'), weight_loader=CheckpointWeightLoader(params_path='gs://openpi-assets/checkpoints/pi0_base/params'), pytorch_weight_path=None, pytorch_training_precision='bfloat16', lr_schedule=CosineDecaySchedule(warmup_steps=1000, peak_lr=2.5e-05, decay_steps=30000, decay_lr=2.5e-06), optimizer=AdamW(b1=0.9, b2=0.95, eps=1e-08, weight_decay=1e-10, clip_gradient_norm=1.0), ema_decay=0.99, freeze_filter=Nothing(), data=LeRobotLiberoDataConfig(repo_id='physical-intelligence/libero', assets=AssetsConfig(assets_dir=None, asset_id=None), base_config=DataConfig(repo_id=None, asset_id=None, norm_stats=None, repack_transforms=Group(inputs=(), outputs=()), data_transforms=Group(inputs=(), outputs=()), model_transforms=Group(inputs=(), outputs=()), use_quantile_norm=False, action_sequence_keys=('actions',), prompt_from_task=True, rlds_data_dir=None, action_space=None, datasets=()), extra_delta_transform=True), assets_base_dir='./assets', checkpoint_base_dir='./checkpoints', seed=42, batch_size=32, num_workers=2, num_train_steps=30000, log_interval=100, save_interval=1000, keep_period=5000, overwrite=False, resume=False, wandb_enabled=True, policy_metadata=None, fsdp_devices=1)\\\\n\\\\nStderr:\\\\n\\\\n\\\\n\\\\n\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 30.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/meta_brain_lora_routing && CUDA_VISIBLE_DEVICES=1 python3 phase1/collect_expert_demos.py --perturbation_type spatial --gpu_id 0 --dry_run 2>&1'\\n\\nStdout:\\n\\n2026-05-16 02:03:41,391 [INFO] Config: type=spatial spatial_mode=add_n device=cuda:0 num_tasks=10 eps_per_cfg=3 dry_run=True\\n2026-05-16 02:03:41,391 [INFO] Loading π₀ from /root/autodl-tmp/checkpoints/pi0_base\\n2026-05-16 02:03:45,796 [INFO] Loading model...\\n2026-05-16 02:03:45,796 [INFO] train_config: TrainConfig(name='pi0_libero', project_name='openpi', exp_name=tyro.MISSING, model=Pi0Config(action_dim=32, action_horizon=50, max_token_len=48, dtype='bfloat16', paligemma_variant='gemma_2b', action_expert_variant='gemma_300m', pi05=False, discrete_state_input=False, pytorch_compile_mode='max-autotune'), weight_loader=CheckpointWeightLoader(params_path='gs://openpi-assets/checkpoints/pi0_base/params'), pytorch_weight_path=None, pytorch_training_precision='bfloat16', lr_schedule=CosineDecaySchedule(warmup_steps=1000, peak_lr=2.5e-05, decay_steps=30000, decay_lr=2.5e-06), optimizer=AdamW(b1=0.9, b2=0.95, eps=1e-08, weight_decay=1e-10, clip_gradient_norm=1.0), ema_decay=0.99, freeze_filter=Nothing(), data=LeRobotLiberoDataConfig(repo_id='physical-intelligence/libero', assets=AssetsConfig(assets_dir=None, asset_id=None), base_config=DataConfig(repo_id=None, asset_id=None, norm_stats=None, repack_transforms=Group(inputs=(), outputs=()), data_transforms=Group(inputs=(), outputs=()), model_transforms=Group(inputs=(), outputs=()), use_quantile_norm=False, action_sequence_keys=('actions',), prompt_from_task=True, rlds_data_dir=None, action_space=None, datasets=()), extra_delta_transform=True), assets_base_dir='./assets', checkpoint_base_dir='./checkpoints', seed=42, batch_size=32, num_workers=2, num_train_steps=30000, log_interval=100, save_interval=1000, keep_period=5000, overwrite=False, resume=False, wandb_enabled=True, policy_metadata=None, fsdp_devices=1)\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.43}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 181_

<details><summary>Logged reasoning block</summary>

```text
The command timed out after 30 seconds, but it was in the process of loading the model (pi0). The model loading takes time. I need to use a longer timeout or run it in the background with nohup. Let me use nohup + background approach.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "076b1108-3df4-46ff-bf3a-6d00ec9774f9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014qqr4V9P9Br3LESP9PB9yB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1206,
      "cache_read_input_tokens": 135977,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1206
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

_source line 182_

Model 加载中，需要更多时间。用 nohup 后台运行。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "c063ce39-1828-41f6-b232-353955c1e594",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014qqr4V9P9Br3LESP9PB9yB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1206,
      "cache_read_input_tokens": 135977,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1206
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

_source line 183_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_0155NHWEZamnv54LZThLk84R`</summary>

```json
{
  "server": "westd-34142",
  "account": "root",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/meta_brain_lora_routing && nohup bash -c 'CUDA_VISIBLE_DEVICES=1 python3 phase1/collect_expert_demos.py --perturbation_type spatial --gpu_id 0 --dry_run' > /tmp/spatial_dryrun.log 2>&1 & echo \"PID=$!\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "f0d256e0-5408-4699-85f7-05f7ca9abe8a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014qqr4V9P9Br3LESP9PB9yB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1206,
      "cache_read_input_tokens": 135977,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1206
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

_source line 184 · 2026-05-15T18:04:48.115Z_

<details><summary>↩ Tool result · `toolu_0155NHWEZamnv54LZThLk84R`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/meta_brain_lora_routing && nohup bash -c \\\\'CUDA_VISIBLE_DEVICES=1 python3 phase1/collect_expert_demos.py --perturbation_type spatial --gpu_id 0 --dry_run\\\\' > /tmp/spatial_dryrun.log 2>&1 & echo \\\"PID=$!\\\"'\\n\\nStdout:\\n\\nPID=242662\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.95}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cb7ab164-b336-4232-adb7-15a7c03a9fa7",
  "uuid": "22a6e51e-1521-4519-95bf-0ecfbee339bb",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Command did not complete within 30 seconds!\\\\n\\\\nCommand: 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/meta_brain_lora_routing && nohup bash -c \\\\\\\\'CUDA_VISIBLE_DEVICES=1 python3 phase1/collect_expert_demos.py --perturbation_type spatial --gpu_id 0 --dry_run\\\\\\\\' > /tmp/spatial_dryrun.log 2>&1 & echo \\\\\\\"PID=$!\\\\\\\"'\\\\n\\\\nStdout:\\\\n\\\\nPID=242662\\\\n\\\\nStderr:\\\\n\\\\n\\\\n\\\\n\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 30.95}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/meta_brain_lora_routing && nohup bash -c \\\\'CUDA_VISIBLE_DEVICES=1 python3 phase1/collect_expert_demos.py --perturbation_type spatial --gpu_id 0 --dry_run\\\\' > /tmp/spatial_dryrun.log 2>&1 & echo \\\"PID=$!\\\"'\\n\\nStdout:\\n\\nPID=242662\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.95}}"
    }
  }
}
```

</details>

---
