# analyze tracvla spatial untrained v1

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/chats/worker_analyze_tracvla_spatial_untrained_v1_20260521T160910.jsonl`
- **Structured JSON:** [`632792d65a898441075e.json`](../../sessions/63/632792d65a898441075e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

15 recorded events

### Tool call

_source line 1 · 2026-05-21T16:11:06.572511+00:00_

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
  "session": "worker_analyze_tracvla_spatial_untrained_v1_20260521T160910",
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

_source line 2 · 2026-05-21T16:11:06.573013+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_tracvla_spatial_untrained_v1_20260521T160910",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T16:11:06.573207+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "tail -200 ~/runs/vla-ssd/tracvla_spatial_untrained_v1.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_tracvla_spatial_untrained_v1_20260521T160910",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "tail -200 ~/runs/vla-ssd/tracvla_spatial_untrained_v1.log"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-21T16:11:06.573437+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[23:44:42] Pipeline conditions: ['untrained']\\n[23:44:42] Loading untrained model from /root/autodl-tmp/vla-ssd/checkpoints/phi3v-base/ ...\\n\\rLoading checkpoint shards:   0%|          | 0/2 [00:00<?, ?it/s]\\rLoading checkpoint shards:  50%|█████     | 1/2 [00:00<00:00,  7.69it/s]\\rLoading checkpoint shards: 100%|██████████| 2/2 [00:00<00:00,  9.70it/s]\\n/root/miniconda3/lib/python3.12/site-packages/transformers/models/auto/image_processing_auto.py:590: FutureWarning: The image_processor_class argument is deprecated and will be removed in v4.42. Please use `slow_image_processor_class`, or `fast_image_processor_class` instead\\n  warnings.warn(\\n[23:44:45]   Model loaded in 3.0s\\n[23:44:45] === UNTRAINED pipeline ===\\n[23:44:45] Config: tasks=10 demos=10 timesteps=50 seeds=15 dry_run=False\\n[23:44:45] Output: /root/autodl-tmp/vla-ssd/results/tracvla_spatial/untrained\\n[23:44:45]   Image token ID: -1\\n[23:44:45] Validating token layout ...\\n[23:44:45]   input_ids shape: torch.Size([1, 352])\\n[23:44:45]   pixel_values shape: torch.Size([1, 2, 3, 336, 336])\\n[23:44:45]   image_sizes: tensor([[336, 336]], device='cuda:0')\\n/root/.cache/huggingface/modules/transformers_modules/image_embedding_phi3_v.py:197: UserWarning: Phi-3-V modifies `input_ids` in-place and the tokens indicating images will be removed after model forward. If your workflow requires multiple forward passes on the same `input_ids`, please make a copy of `input_ids` before passing it to the model.\\n  warnings.warn(\\nYou are not running the flash-attention implementation, expect numerical differences.\\n[23:44:46]   hidden_states[0] shape: torch.Size([1, 352, 3072])\\n[23:44:46]   Token regions: bos=(0, 4) image=(4, 317) text=(317, 352)\\n[23:44:46]   N_IMG_TOKENS=313\\n[23:44:46]   Total seq_len: input_ids=352, hidden=352\\n[23:44:46]   Attention: 32 layers, shape=torch.Size([1, 32, 352, 352])\\n[23:44:46] Phase 1: representation ex
…[truncated 4744 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_tracvla_spatial_untrained_v1_20260521T160910",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T16:11:06.573648+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/tracvla_spatial/untrained/action_r2_probing.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_tracvla_spatial_untrained_v1_20260521T160910",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/results/tracvla_spatial/untrained/action_r2_probing.json"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T16:11:06.573965+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"L0_image_mean\\\": {\\n    \\\"mean\\\": 0.7761,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.7761\\n    ]\\n  },\\n  \\\"L0_last_preaction\\\": {\\n    \\\"mean\\\": 0.5911,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.5911\\n    ]\\n  },\\n  \\\"L1_image_mean\\\": {\\n    \\\"mean\\\": 0.7761,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.7761\\n    ]\\n  },\\n  \\\"L1_last_preaction\\\": {\\n    \\\"mean\\\": 0.6226,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.6226\\n    ]\\n  },\\n  \\\"L2_image_mean\\\": {\\n    \\\"mean\\\": 0.7779,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.7779\\n    ]\\n  },\\n  \\\"L2_last_preaction\\\": {\\n    \\\"mean\\\": 0.6833,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.6833\\n    ]\\n  },\\n  \\\"L3_image_mean\\\": {\\n    \\\"mean\\\": 0.7789,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.7789\\n    ]\\n  },\\n  \\\"L3_last_preaction\\\": {\\n    \\\"mean\\\": 0.6868,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.6868\\n    ]\\n  },\\n  \\\"L4_image_mean\\\": {\\n    \\\"mean\\\": 0.7812,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.7812\\n    ]\\n  },\\n  \\\"L4_last_preaction\\\": {\\n    \\\"mean\\\": 0.7132,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.7132\\n    ]\\n  },\\n  \\\"L5_image_mean\\\": {\\n    \\\"mean\\\": 0.7839,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.7839\\n    ]\\n  },\\n  \\\"L5_last_preaction\\\": {\\n    \\\"mean\\\": 0.7177,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.7177\\n    ]\\n  },\\n  \\\"L6_image_mean\\\": {\\n    \\\"mean\\\": 0.7856,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.7856\\n    ]\\n  },\\n  \\\"L6_last_preaction\\\": {\\n    \\\"mean\\\": 0.7189,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.7189\\n    ]\\n  },\\n  \\\"L7_image_mean\\\
…[truncated 6970 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_tracvla_spatial_untrained_v1_20260521T160910",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T16:11:06.574176+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/tracvla_spatial/untrained/l1_attention_profile.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_tracvla_spatial_untrained_v1_20260521T160910",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/results/tracvla_spatial/untrained/l1_attention_profile.json"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-21T16:11:06.574320+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/tracvla_spatial/untrained/cross_instruction_classification.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_tracvla_spatial_untrained_v1_20260521T160910",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/results/tracvla_spatial/untrained/cross_instruction_classification.json"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-21T16:11:06.574554+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"per_head\\\": {\\n    \\\"head_0\\\": {\\n      \\\"instruction_ratio_mean\\\": 0.9532,\\n      \\\"instruction_ratio_std\\\": 0.0028,\\n      \\\"category\\\": \\\"instruction_dominant\\\"\\n    },\\n    \\\"head_1\\\": {\\n      \\\"instruction_ratio_mean\\\": 0.9592,\\n      \\\"instruction_ratio_std\\\": 0.0038,\\n      \\\"category\\\": \\\"instruction_dominant\\\"\\n    },\\n    \\\"head_2\\\": {\\n      \\\"instruction_ratio_mean\\\": 0.569,\\n      \\\"instruction_ratio_std\\\": 0.0111,\\n      \\\"category\\\": \\\"instruction_dominant\\\"\\n    },\\n    \\\"head_3\\\": {\\n      \\\"instruction_ratio_mean\\\": 0.7949,\\n      \\\"instruction_ratio_std\\\": 0.0128,\\n      \\\"category\\\": \\\"instruction_dominant\\\"\\n    },\\n    \\\"head_4\\\": {\\n      \\\"instruction_ratio_mean\\\": 0.7255,\\n      \\\"instruction_ratio_std\\\": 0.0106,\\n      \\\"category\\\": \\\"instruction_dominant\\\"\\n    },\\n    \\\"head_5\\\": {\\n      \\\"instruction_ratio_mean\\\": 0.6261,\\n      \\\"instruction_ratio_std\\\": 0.0288,\\n      \\\"category\\\": \\\"instruction_dominant\\\"\\n    },\\n    \\\"head_6\\\": {\\n      \\\"instruction_ratio_mean\\\": 0.7003,\\n      \\\"instruction_ratio_std\\\": 0.0164,\\n      \\\"category\\\": \\\"instruction_dominant\\\"\\n    },\\n    \\\"head_7\\\": {\\n      \\\"instruction_ratio_mean\\\": 0.7976,\\n      \\\"instruction_ratio_std\\\": 0.009,\\n      \\\"category\\\": \\\"instruction_dominant\\\"\\n    },\\n    \\\"head_8\\\": {\\n      \\\"instruction_ratio_mean\\\": 0.9961,\\n      \\\"instruction_ratio_std\\\": 0.0004,\\n      \\\"category\\\": \\\"instruction_dominant\\\"\\n    },\\n    \\\"head_9\\\": {\\n      \\\"instruction_ratio_mean\\\": 0.912,\\n      \\\"instruction_ratio_std\\\": 0.0042,\\n      \\\"category\\\": \\\"instruction_dominant\\\"\\n    },\\n    \\\"head_10\\\": {\\n      \\\"instruction_ratio_mean\\\": 0.8347,\\n      \\\"instru
…[truncated 4655 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_tracvla_spatial_untrained_v1_20260521T160910",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T16:11:06.574765+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"chance\\\": 0.1,\\n  \\\"L0_image_mean\\\": 1.0,\\n  \\\"L0_last_preaction\\\": 0.977,\\n  \\\"L1_image_mean\\\": 1.0,\\n  \\\"L1_last_preaction\\\": 1.0,\\n  \\\"L2_image_mean\\\": 1.0,\\n  \\\"L2_last_preaction\\\": 1.0,\\n  \\\"L3_image_mean\\\": 1.0,\\n  \\\"L3_last_preaction\\\": 1.0,\\n  \\\"L4_image_mean\\\": 1.0,\\n  \\\"L4_last_preaction\\\": 1.0,\\n  \\\"L5_image_mean\\\": 1.0,\\n  \\\"L5_last_preaction\\\": 1.0,\\n  \\\"L6_image_mean\\\": 1.0,\\n  \\\"L6_last_preaction\\\": 1.0,\\n  \\\"L7_image_mean\\\": 1.0,\\n  \\\"L7_last_preaction\\\": 1.0,\\n  \\\"L8_image_mean\\\": 1.0,\\n  \\\"L8_last_preaction\\\": 1.0,\\n  \\\"L9_image_mean\\\": 1.0,\\n  \\\"L9_last_preaction\\\": 1.0,\\n  \\\"L10_image_mean\\\": 1.0,\\n  \\\"L10_last_preaction\\\": 1.0,\\n  \\\"L11_image_mean\\\": 1.0,\\n  \\\"L11_last_preaction\\\": 1.0,\\n  \\\"L12_image_mean\\\": 1.0,\\n  \\\"L12_last_preaction\\\": 1.0,\\n  \\\"L13_image_mean\\\": 1.0,\\n  \\\"L13_last_preaction\\\": 1.0,\\n  \\\"L14_image_mean\\\": 1.0,\\n  \\\"L14_last_preaction\\\": 1.0,\\n  \\\"L15_image_mean\\\": 1.0,\\n  \\\"L15_last_preaction\\\": 1.0,\\n  \\\"L16_image_mean\\\": 1.0,\\n  \\\"L16_last_preaction\\\": 1.0,\\n  \\\"L17_image_mean\\\": 1.0,\\n  \\\"L17_last_preaction\\\": 1.0,\\n  \\\"L18_image_mean\\\": 1.0,\\n  \\\"L18_last_preaction\\\": 1.0,\\n  \\\"L19_image_mean\\\": 1.0,\\n  \\\"L19_last_preaction\\\": 1.0,\\n  \\\"L20_image_mean\\\": 1.0,\\n  \\\"L20_last_preaction\\\": 1.0,\\n  \\\"L21_image_mean\\\": 1.0,\\n  \\\"L21_last_preaction\\\": 1.0,\\n  \\\"L22_image_mean\\\": 1.0,\\n  \\\"L22_last_preaction\\\": 1.0,\\n  \\\"L23_image_mean\\\": 1.0,\\n  \\\"L23_last_preaction\\\": 1.0,\\n  \\\"L24_image_mean\\\": 1.0,\\n  \\\"L24_last_preaction\\\": 1.0,\\n  \\\"L25_image_mean\\\": 1.0,\\n  \\\"L25_last_preaction\\\": 1.0,\\n  \\\"L26_image_mean\\\": 1.0,\\n  \\\"L26_last_preaction\\\": 1.0,\\n  \\\"L27_image_mean\\\": 1.0,\\n  \\\"L27_
…[truncated 411 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_tracvla_spatial_untrained_v1_20260521T160910",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T16:11:06.575015+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ls /root/autodl-tmp/vla-ssd/results/tracvla_spatial/untrained/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_tracvla_spatial_untrained_v1_20260521T160910",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ls /root/autodl-tmp/vla-ssd/results/tracvla_spatial/untrained/"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T16:11:06.575179+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"action_r2_probing.json\\ncross_instruction_classification.json\\nl1_attention_profile.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_tracvla_spatial_untrained_v1_20260521T160910",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T16:11:06.575315+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/tracvla_spatial/trained/action_r2_probing.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_tracvla_spatial_untrained_v1_20260521T160910",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/results/tracvla_spatial/trained/action_r2_probing.json"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T16:11:06.575627+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"L0_image_mean\\\": {\\n    \\\"mean\\\": 0.8059,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.8059\\n    ]\\n  },\\n  \\\"L0_last_preaction\\\": {\\n    \\\"mean\\\": 0.6656,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.6656\\n    ]\\n  },\\n  \\\"L1_image_mean\\\": {\\n    \\\"mean\\\": 0.8055,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.8055\\n    ]\\n  },\\n  \\\"L1_last_preaction\\\": {\\n    \\\"mean\\\": 0.7359,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.7359\\n    ]\\n  },\\n  \\\"L2_image_mean\\\": {\\n    \\\"mean\\\": 0.8053,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.8053\\n    ]\\n  },\\n  \\\"L2_last_preaction\\\": {\\n    \\\"mean\\\": 0.7681,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.7681\\n    ]\\n  },\\n  \\\"L3_image_mean\\\": {\\n    \\\"mean\\\": 0.8064,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.8064\\n    ]\\n  },\\n  \\\"L3_last_preaction\\\": {\\n    \\\"mean\\\": 0.791,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.791\\n    ]\\n  },\\n  \\\"L4_image_mean\\\": {\\n    \\\"mean\\\": 0.8091,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.8091\\n    ]\\n  },\\n  \\\"L4_last_preaction\\\": {\\n    \\\"mean\\\": 0.7954,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.7954\\n    ]\\n  },\\n  \\\"L5_image_mean\\\": {\\n    \\\"mean\\\": 0.8117,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.8117\\n    ]\\n  },\\n  \\\"L5_last_preaction\\\": {\\n    \\\"mean\\\": 0.794,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.794\\n    ]\\n  },\\n  \\\"L6_image_mean\\\": {\\n    \\\"mean\\\": 0.8145,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.8145\\n    ]\\n  },\\n  \\\"L6_last_preaction\\\": {\\n    \\\"mean\\\": 0.8009,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.8009\\n    ]\\n  },\\n  \\\"L7_image_mean\\\": {
…[truncated 6954 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_tracvla_spatial_untrained_v1_20260521T160910",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-21T16:11:06.575905+00:00_

所有数据已获取。没有 RSA 或 counterfactual 结果（Phase 5 被跳过）。下面汇总。

## Metrics Summary

### Phase 2: R² Probing (Ridge, all 32 layers)

| Layer | Trained img_mean | Untrained img_mean | Trained last_pre | Untrained last_pre |
|-------|-----|------|------|------|
| L0 | 0.8059 | 0.7761 | 0.6656 | 0.5911 |
| L4 | 0.8091 | 0.7812 | 0.7954 | 0.7132 |
| L8 | 0.8134 | 0.7892 | 0.7908 | 0.6942 |
| L12 | 0.8231 | 0.7806 | 0.7980 | 0.7195 |
| L16 | 0.8311 | 0.7961 | 0.8035 | 0.7207 |
| **L17** | **0.8317** | 0.7919 | **0.8090** (peak) | 0.7156 |
| **L19** | **0.8347** (peak) | 0.7901 | 0.8051 | 0.7178 |
| L24 | 0.8169 | 0.7694 | 0.7463 | 0.7116 |
| L28 | 0.8223 | 0.7714 | **0.6150** | 0.7036 |
| L29 | 0.8136 | 0.7731 | **0.5040** | 0.7037 |
| L30 | 0.7970 | 0.7696 | **0.4472** | 0.6969 |
| **L31** | 0.7907 | 0.7589 | **0.6712** | **0.7065** |

### Phase 3: L1 Attention Profile

| Metric | Trained | Untrained |
|--------|---------|-----------|
| Instruction-dominant heads | 30/32 | 32/32 |
| Image-dominant heads | 2/32 | 0/32 |

### Phase 4: Cross-instruction Classification

| Layer | Trained img | Untrained img | Trained last_pre | Untrained last_pre |
|-------|-------------|---------------|-------------------|---------------------|
| L0 | 1.000 | 1.000 | 0.923 | 0.977 |
| L1+ | 1.000 | 1.000 | 1.000 | 1.000 |

### Phase 5: Counterfactual
- Trained: empty d=1.3268, shuffled d=1.2947
- Untrained: **skipped** (untrained model cannot generate meaningful actions)

---

## Trained vs Untrained Comparison

### 1. R² Collapse — **Training-induced (CONFIRMED)**

The defining finding. Trained last_preaction shows dramatic late-layer collapse; untrained is flat:

| Metric | Trained | Untrained |
|--------|---------|-----------|
| last_pre peak | 0.8090 (L17) | 0.7224 (L18) |
| last_pre @ L30 (nadir) | **0.4472** | 0.6969 |
| last_pre @ L31 (exit) | 0.6712 | 0.7065 |
| Peak→L30 drop | **-0.3618** | **-0.0255** |
| img_mean @ L31 | 0.7907 | 0.7589 |
| L31 gap (img - last_pre) | **0.1195** | 0.0524 |
| L30 gap (img - last_pre) | **0.3498** | 0.0727 |

Trained model develops a massive **routing divergence**: image tokens maintain R² while last_preaction collapses in layers 26–30, then partially recovers at L31. Untrained model has no such pattern — both modalities decline gently and in parallel.

### 2. L1 Instruction Dominance — **Pre-existing architectural property (NOT training-induced)**

Untrained: 32/32 instruction-dominant. Trained: 30/32. Training actually *reduces* instruction dominance slightly (introduces 2 image-dominant heads). This is an architectural bias of Phi-3-Vision, not an emergent training effect.

### 3. Cross-instruction Classification — **Pre-existing (NOT training-induced)**

Both conditions achieve near-perfect classification (1.0) at all layers. Task-discriminative representations exist in the pretrained model already.

### 4. Counterfactual — **No comparison possible**

Skipped for untrained (no meaningful action generation without fine-tuning).

---

## Conclusion

**success** — Hypothesis partially confirmed with one important nuance.

The core claim holds: the **R² collapse pattern is training-induced**. The trained model develops a dramatic routing divergence where last_preaction R² collapses by 0.36 (L17→L30) while image_mean stays elevated, creating a late-layer gap of up to 0.35. The untrained model shows no such pattern — both modalities follow a flat, parallel trajectory (max drop 0.026). This is the strongest evidence that VLA fine-tuning creates specialized information routing.

However, **L1 instruction dominance is NOT training-induced** — it's a pre-existing architectural property of Phi-3-Vision (32/32 untrained vs 30/32 trained). Similarly, cross-instruction classification is pre-existing. These should not be cited as training-induced effects.

The counterfactual comparison is unavailable (untrained cannot generate actions), but the R² probing contrast alone is decisive for the routing hypothesis.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analyze_tracvla_spatial_untrained_v1_20260521T160910"
}
```

</details>

---
