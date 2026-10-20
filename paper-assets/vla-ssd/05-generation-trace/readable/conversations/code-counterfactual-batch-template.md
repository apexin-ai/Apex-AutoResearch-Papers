# code counterfactual batch template

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 85
- **Recorded user turns:** 0
- **Tool calls:** 42
- **Original source:** `logs/chats/worker_code_counterfactual_batch_template_20260521T164440.jsonl`
- **Structured JSON:** [`91b576f5739954374f72.json`](../../sessions/91/91b576f5739954374f72.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

85 recorded events

### Tool call

_source line 1 · 2026-05-21T16:54:02.839587+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T16:54:02.840112+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T16:54:02.840501+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ls /root/autodl-tmp/vla-ssd/scripts/*pipeline*.py /root/autodl-tmp/vla-ssd/scripts/*counterfactual*.py 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ls /root/autodl-tmp/vla-ssd/scripts/*pipeline*.py /root/autodl-tmp/vla-ssd/scripts/*counterfactual*.py 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-21T16:54:02.840663+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T16:54:02.840799+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "find /root/autodl-tmp/vla-ssd/scripts -name \"*pipeline*.py\" -o -name \"*counterfactual*.py\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "find /root/autodl-tmp/vla-ssd/scripts -name \"*pipeline*.py\" -o -name \"*counterfactual*.py\""
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T16:54:02.841049+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py\\n/root/autodl-tmp/vla-ssd/scripts/tracvla_spatial_full_pipeline.py\\n/root/autodl-tmp/vla-ssd/scripts/nora_goal_full_pipeline.py\\n/root/autodl-tmp/vla-ssd/scripts/nora_spatial_full_pipeline.py\\n/root/autodl-tmp/vla-ssd/scripts/tracvla_object_full_pipeline.py\\n/root/autodl-tmp/vla-ssd/scripts/libero_long_full_pipeline.py\\n/root/autodl-tmp/vla-ssd/scripts/nora_goal_untrained_counterfactual_only.py\\n/root/autodl-tmp/vla-ssd/scripts/libero_object_untrained_full_pipeline.py\\n/root/autodl-tmp/vla-ssd/scripts/tracvla_long_full_pipeline.py\\n/root/autodl-tmp/vla-ssd/scripts/tracvla_goal_full_pipeline.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T16:54:02.841324+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/scripts/nora_goal_untrained_counterfactual_only.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/scripts/nora_goal_untrained_counterfactual_only.py"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T16:54:02.841628+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Standalone: run counterfactual phase only for untrained Qwen2.5-VL-3B on LIBERO-Goal.\\\"\\\"\\\"\\n\\nimport json, os, random, sys, time\\nfrom collections import defaultdict\\n\\nos.environ[\\\"HDF5_USE_FILE_LOCKING\\\"] = \\\"FALSE\\\"\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nimport torch.nn.functional as F\\nfrom PIL import Image\\nfrom transformers import AutoModelForImageTextToText, AutoProcessor\\n\\nCKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base/\\\"\\nDATA = \\\"/root/autodl-tmp/vla-ssd/data/libero/libero_goal\\\"\\nRESULTS_DIR = \\\"/root/autodl-tmp/vla-ssd/results/nora_goal/untrained\\\"\\nDEVICE = \\\"cuda:0\\\"\\n\\nN_LAYERS = 36\\nN_HEADS = 16\\nHIDDEN = 2048\\nN_DEMOS = 10\\nN_TIMESTEPS = 50\\n\\nTASKS = [\\n    \\\"open_the_middle_drawer_of_the_cabinet\\\",\\n    \\\"open_the_top_drawer_and_put_the_bowl_inside\\\",\\n    \\\"push_the_plate_to_the_front_of_the_stove\\\",\\n    \\\"put_the_bowl_on_the_plate\\\",\\n    \\\"put_the_bowl_on_the_stove\\\",\\n    \\\"put_the_bowl_on_top_of_the_cabinet\\\",\\n    \\\"put_the_cream_cheese_in_the_bowl\\\",\\n    \\\"put_the_wine_bottle_on_the_rack\\\",\\n    \\\"put_the_wine_bottle_on_top_of_the_cabinet\\\",\\n    \\\"turn_on_the_stove\\\",\\n]\\nINSTRUCTIONS = [t.replace(\\\"_\\\", \\\" \\\") for t in TASKS]\\nPARAPHRASES = [\\n    \\\"open the cabinet's middle drawer\\\",\\n    \\\"open the top drawer and place the bowl in it\\\",\\n    \\\"slide the plate to the stove's front\\\",\\n    \\\"place the bowl onto the plate\\\",\\n    \\\"place the bowl onto the stove\\\",\\n    \\\"place the bowl on the cabinet top\\\",\\n    \\\"put cream cheese into the bowl\\\",\\n    \\\"place the wine bottle on the rack\\\",\\n    \\\"place the wine bottle on the cabinet top\\\",\\n    \\\"switch on the stove\\\",\\n]\\n\\n\\ndef log(msg):\\n    print(f\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\", f
…[truncated 7339 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T16:54:02.841842+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -n \"counterfactual\\|Phase 6\\|def run_counterfactual\\|CONDITION_MAP\\|predict_action\\|action_mse\\|cosine_dist\\|CHECKPOINT\\|checkpoint\\|model_path\\|TRAINED\\|UNTRAINED\\|norm_stats\\|dataset_statistics\\|CKPT\\|SUITE\\|DATA_DIR\\|RESULTS\" /root/autodl-tmp/vla-ssd/scripts/tracvla_object_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "grep -n \"counterfactual\\|Phase 6\\|def run_counterfactual\\|CONDITION_MAP\\|predict_action\\|action_mse\\|cosine_dist\\|CHECKPOINT\\|checkpoint\\|model_path\\|TRAINED\\|UNTRAINED\\|norm_stats\\|dataset_statistics\\|CKPT\\|SUITE\\|DATA_DIR\\|RESULTS\" /root/autodl-tmp/vla-ssd/scripts/tracvla_object_full_pipeline.py"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T16:54:02.842009+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T16:54:02.842154+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -n \"CKPT\\|CHECKPOINT\\|DATA\\|RESULTS\\|SUITE\\|counterfactual\\|Phase 6\\|def run_counterfactual\\|predict_action\\|cosine_dist\\|norm_stats\\|dataset_statistics\\|TRAINED\\|UNTRAINED\" /root/autodl-tmp/vla-ssd/scripts/tracvla_object_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "grep -n \"CKPT\\|CHECKPOINT\\|DATA\\|RESULTS\\|SUITE\\|counterfactual\\|Phase 6\\|def run_counterfactual\\|predict_action\\|cosine_dist\\|norm_stats\\|dataset_statistics\\|TRAINED\\|UNTRAINED\" /root/autodl-tmp/vla-ssd/scripts/tracvla_object_full_pipeline.py"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T16:54:02.842291+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T16:54:02.842417+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -n \"CKPT\\|CHECKPOINT\\|DATA\\|RESULTS\\|SUITE\\|counterfactual\\|Phase 6\\|predict_action\\|cosine_dist\\|norm_stats\\|TRAINED\\|UNTRAINED\" /root/autodl-tmp/vla-ssd/scripts/tracvla_object_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "grep -n \"CKPT\\|CHECKPOINT\\|DATA\\|RESULTS\\|SUITE\\|counterfactual\\|Phase 6\\|predict_action\\|cosine_dist\\|norm_stats\\|TRAINED\\|UNTRAINED\" /root/autodl-tmp/vla-ssd/scripts/tracvla_object_full_pipeline.py"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T16:54:02.842549+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T16:54:02.842687+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -nE \"CKPT|CHECKPOINT|RESULTS_DIR|DATA_DIR|SUITE|counterfactual|Phase.6|predict_action|cosine|norm_stats\" /root/autodl-tmp/vla-ssd/scripts/tracvla_object_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "grep -nE \"CKPT|CHECKPOINT|RESULTS_DIR|DATA_DIR|SUITE|counterfactual|Phase.6|predict_action|cosine|norm_stats\" /root/autodl-tmp/vla-ssd/scripts/tracvla_object_full_pipeline.py"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T16:54:02.842810+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T16:54:02.842960+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "wc -l /root/autodl-tmp/vla-ssd/scripts/tracvla_object_full_pipeline.py /root/autodl-tmp/vla-ssd/scripts/libero_long_full_pipeline.py /root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py /root/autodl-tmp/vla-ssd/scripts/nora_goal_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "wc -l /root/autodl-tmp/vla-ssd/scripts/tracvla_object_full_pipeline.py /root/autodl-tmp/vla-ssd/scripts/libero_long_full_pipeline.py /root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py /root/autodl-tmp/vla-ssd/scripts/nora_goal_full_pipeline.py"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-21T16:54:02.843100+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  642 /root/autodl-tmp/vla-ssd/scripts/tracvla_object_full_pipeline.py\\n  665 /root/autodl-tmp/vla-ssd/scripts/libero_long_full_pipeline.py\\n  633 /root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py\\n  622 /root/autodl-tmp/vla-ssd/scripts/nora_goal_full_pipeline.py\\n 2562 total\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T16:54:02.843222+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "head -100 /root/autodl-tmp/vla-ssd/scripts/tracvla_object_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "head -100 /root/autodl-tmp/vla-ssd/scripts/tracvla_object_full_pipeline.py"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T16:54:02.843394+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nLIBERO-Object Full Analysis Pipeline for TracVLA-Phi3V\\n\\nPhases:\\n  1. Representation extraction: forward passes -> hidden states + L1 attention\\n  2. Action R2 probing: per-layer Ridge probe\\n  3. L1 attention profile: per-head instruction/image attention classification\\n  4. Cross-instruction classification: 10-way per-layer\\n  5. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased), paired Cohen's d\\n\\nRuns both trained (TracVLA-Phi3V) and untrained (base Phi-3-Vision) sequentially.\\nAll results -> RESULTS_DIR/{trained,untrained}/*.json\\nNo intermediate features saved to disk.\\n\\\"\\\"\\\"\\n\\nimport argparse, json, os, random, sys, time\\nfrom collections import defaultdict\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nfrom PIL import Image\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.linear_model import RidgeCV\\nfrom transformers import AutoModelForCausalLM, AutoProcessor\\n\\n# --- Checkpoints ---\\nTRAINED_CKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v/\\\"\\nUNTRAINED_CKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base/\\\"\\nUNTRAINED_CACHE = \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base/\\\"\\n\\n# --- Data ---\\nDATA = \\\"/root/autodl-tmp/vla-ssd/data/libero/libero_object\\\"\\nRESULTS_BASE = \\\"/root/autodl-tmp/vla-ssd/results/tracvla_object\\\"\\nDEVICE = \\\"cuda:0\\\"  # submit_training_job sets CUDA_VISIBLE_DEVICES\\n\\n# --- Architecture ---\\nN_LAYERS = 32\\nN_HEADS = 32\\nHIDDEN = 3072\\nN_IMG_TOKENS = 0  # auto-detected\\nIMG_TOKEN_ID = -1  # auto-detected\\n\\n# --- Data config ---\\nN_DEMOS = 10\\nN_TIMESTEPS = 50\\nN_PROBE_SEEDS = 15\\n\\nTASKS = [\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_
…[truncated 1985 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T16:54:02.843576+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "head -100 /root/autodl-tmp/vla-ssd/scripts/libero_long_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "head -100 /root/autodl-tmp/vla-ssd/scripts/libero_long_full_pipeline.py"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-21T16:54:02.843741+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "head -100 /root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "head -100 /root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-21T16:54:02.843947+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nLIBERO-Long Full Analysis Pipeline (Streaming)\\n\\nPhases:\\n  1. Representation extraction: forward passes -> hidden states + L1 attention\\n  2. Action R2 probing: per-layer Ridge probe\\n  3. L1 attention profile: per-head instruction/image attention classification\\n  4. Cross-instruction classification: 10-way per-layer\\n  5. RSA: representational similarity across conditions\\n  6. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased), paired Cohen's d\\n\\nAll results -> RESULTS_DIR/*.json\\nNo intermediate features saved to disk.\\n\\\"\\\"\\\"\\n\\nimport argparse, json, os, random, sys, time\\nfrom collections import defaultdict\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nfrom PIL import Image\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.linear_model import RidgeCV\\nfrom transformers import AutoModelForVision2Seq, AutoProcessor\\n\\nTRAINED_CKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-oft-finetuned-libero-10\\\"\\nUNTRAINED_CKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"\\nDATA = \\\"/root/autodl-tmp/vla-ssd/data/libero/libero_10\\\"\\nRESULTS_BASE = \\\"/root/autodl-tmp/vla-ssd/results/libero_long\\\"\\nDEVICE = \\\"cuda:0\\\"\\nUNNORM_TRAINED = \\\"libero_10_no_noops\\\"\\nUNNORM_UNTRAINED = \\\"bridge_orig\\\"\\nUNNORM = UNNORM_TRAINED\\n\\nTASKS = [\\n    \\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\",\\n    \\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\",\\n    \\\"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\\\",\\n    \\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\",\\n    \\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\\\",\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\\\",\\n    \\\"LIVING_ROOM_S
…[truncated 2881 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-21T16:54:02.844114+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "head -100 /root/autodl-tmp/vla-ssd/scripts/nora_goal_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "head -100 /root/autodl-tmp/vla-ssd/scripts/nora_goal_full_pipeline.py"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-21T16:54:02.844299+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nLIBERO-Object Full Analysis Pipeline (Streaming)\\n\\nPhases:\\n  1. Representation extraction: forward passes -> hidden states + L1 attention\\n  2. Action R2 probing: per-layer Ridge probe\\n  3. L1 attention profile: per-head instruction/image attention classification\\n  4. Cross-instruction classification: 10-way per-layer\\n  5. RSA: representational similarity across conditions\\n  6. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased), paired Cohen's d\\n\\nAll results -> RESULTS_DIR/*.json\\nNo intermediate features saved to disk.\\n\\\"\\\"\\\"\\n\\nimport argparse, json, os, random, sys, time\\nfrom collections import defaultdict\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nfrom PIL import Image\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.linear_model import RidgeCV\\nfrom transformers import AutoModelForVision2Seq, AutoProcessor\\n\\nTRAINED_CKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-object\\\"\\nUNTRAINED_CKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"\\nDATA = \\\"/root/autodl-tmp/vla-ssd/data/libero/libero_object\\\"\\nRESULTS_BASE = \\\"/root/autodl-tmp/vla-ssd/results/libero_object\\\"\\nDEVICE = \\\"cuda:0\\\"\\nUNNORM = \\\"libero_object\\\"\\n\\nTASKS = [\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_oran
…[truncated 2197 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-21T16:54:02.844493+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nNORA LIBERO-Goal Full Analysis Pipeline\\n\\nPhases:\\n  1. Representation extraction: forward passes -> hidden states + L1 attention\\n  2. Action R2 probing: per-layer Ridge probe\\n  3. L1 attention profile: per-head instruction/image attention classification\\n  4. Cross-instruction classification: 10-way per-layer\\n  5. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased)\\n\\nRuns both trained (NORA) and untrained (Qwen2.5-VL-3B base) sequentially.\\nNORA uses FAST+ action tokenizer, so counterfactual uses representation-based\\ncosine distance instead of action MSE.\\n\\\"\\\"\\\"\\n\\nimport argparse, json, os, random, sys, time\\nfrom collections import defaultdict\\n\\nos.environ[\\\"HDF5_USE_FILE_LOCKING\\\"] = \\\"FALSE\\\"\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nimport torch.nn.functional as F\\nfrom PIL import Image\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.linear_model import RidgeCV\\nfrom transformers import AutoModelForImageTextToText, AutoProcessor\\n\\n# --- Checkpoints ---\\nTRAINED_CKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-goal/\\\"\\nUNTRAINED_CKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base/\\\"\\n\\n# --- Data ---\\nDATA = \\\"/root/autodl-tmp/vla-ssd/data/libero/libero_goal\\\"\\nRESULTS_BASE = \\\"/root/autodl-tmp/vla-ssd/results/nora_goal\\\"\\nDEVICE = \\\"cuda:0\\\"\\n\\n# --- Architecture (Qwen2.5-VL-3B) ---\\nN_LAYERS = 36\\nN_HEADS = 16\\nHIDDEN = 2048\\n\\n# --- Data config ---\\nN_DEMOS = 10\\nN_TIMESTEPS = 50\\nN_PROBE_SEEDS = 15\\n\\nTASKS = [\\n    \\\"open_the_middle_drawer_of_the_cabinet\\\",\\n    \\\"open_the_top_drawer_and_put_the_bowl_inside\\\",\\n    \\\"push_the_plate_to_the_front_of_the_stove\\\",\\n    \\\"put_the_bowl_on_the_plate\\\",\\n    \\\"put_the_bowl_on_the_stove\\\",\\n    \\\"put_the_bowl_on_top_of_the_cabinet\\\",\\n    \\\"
…[truncated 1737 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-21T16:54:02.844686+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "tail -200 /root/autodl-tmp/vla-ssd/scripts/tracvla_object_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "tail -200 /root/autodl-tmp/vla-ssd/scripts/tracvla_object_full_pipeline.py"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-21T16:54:02.844942+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"                \\\"n_samples\\\": len(tm),\\n                \\\"mean_mse\\\": round(float(tm.mean()), 6),\\n                \\\"demo_mses\\\": [round(v, 6) for v in demo_means],\\n                \\\"instruction_correct\\\": INSTRUCTIONS[ti],\\n                \\\"instruction_counterfactual\\\": _cf_instruction(ti, cond),\\n            }\\n            cond_res[\\\"per_task\\\"][TASKS[ti]] = entry\\n\\n        cond_res[\\\"cross_task_variance\\\"] = {\\n            \\\"cohens_d\\\": {\\n                \\\"values\\\": [round(v, 4) for v in per_task_ds],\\n                \\\"mean\\\": round(float(np.mean(per_task_ds)), 4),\\n                \\\"std\\\": round(float(np.std(per_task_ds)), 4),\\n                \\\"cv\\\": (\\n                    round(float(np.std(per_task_ds) / np.mean(per_task_ds)), 4)\\n                    if np.mean(per_task_ds) > 0\\n                    else 0.0\\n                ),\\n            }\\n        }\\n        all_res[cond] = cond_res\\n        log(\\n            f\\\"  {cond}: global d={global_d:.4f}  \\\"\\n            f\\\"cross-task mean={np.mean(per_task_ds):.4f}  \\\"\\n            f\\\"token_div={np.mean(all_tok_div):.3f}\\\"\\n        )\\n\\n    ranking = sorted(\\n        conditions,\\n        key=lambda c: all_res[c][\\\"global_metrics\\\"][\\\"paired_mse\\\"][\\\"cohens_d\\\"],\\n        reverse=True,\\n    )\\n    all_res[\\\"ranking_by_cohens_d\\\"] = [\\n        {\\n            \\\"condition\\\": c,\\n            \\\"cohens_d\\\": all_res[c][\\\"global_metrics\\\"][\\\"paired_mse\\\"][\\\"cohens_d\\\"],\\n            \\\"paired_mse_mean\\\": all_res[c][\\\"global_metrics\\\"][\\\"paired_mse\\\"][\\\"mean\\\"],\\n        }\\n        for c in ranking\\n    ]\\n    return all_res\\n\\n\\ndef load_model(ckpt_path, condition):\\n    log(f\\\"Loading {condition} model from {ckpt_path} ...\\\")\\n    t0 = time.time()\\n\\n    model = AutoModelForCausalLM.from_pretrained(\\n
…[truncated 6410 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-21T16:54:02.845228+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "tail -250 /root/autodl-tmp/vla-ssd/scripts/libero_long_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "tail -250 /root/autodl-tmp/vla-ssd/scripts/libero_long_full_pipeline.py"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-21T16:54:02.845453+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "tail -250 /root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "tail -250 /root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-21T16:54:02.845736+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"                \\\"values\\\": [round(v, 4) for v in per_task_ds],\\n                \\\"mean\\\": round(float(np.mean(per_task_ds)), 4),\\n                \\\"std\\\": round(float(np.std(per_task_ds)), 4),\\n                \\\"cv\\\": round(float(np.std(per_task_ds) / np.mean(per_task_ds)), 4)\\n                     if np.mean(per_task_ds) > 0 else 0.0,\\n            }\\n        }\\n        all_res[cond] = cond_res\\n        log(f\\\"  {cond}: global d={global_d:.4f}  \\\"\\n            f\\\"cross-task mean={np.mean(per_task_ds):.4f}  \\\"\\n            f\\\"token_div={np.mean(all_tok_div):.3f}\\\")\\n\\n    ranking = sorted(conditions,\\n                     key=lambda c: all_res[c][\\\"global_metrics\\\"][\\\"paired_mse\\\"][\\\"cohens_d\\\"],\\n                     reverse=True)\\n    all_res[\\\"ranking_by_cohens_d\\\"] = [\\n        {\\\"condition\\\": c,\\n         \\\"cohens_d\\\": all_res[c][\\\"global_metrics\\\"][\\\"paired_mse\\\"][\\\"cohens_d\\\"],\\n         \\\"paired_mse_mean\\\": all_res[c][\\\"global_metrics\\\"][\\\"paired_mse\\\"][\\\"mean\\\"]}\\n        for c in ranking\\n    ]\\n    return all_res\\n\\n\\n\\ndef run_rsa(reps, actions, task_labels, n_sample=20, bootstrap_n=1000, seed=42):\\n    log(\\\"Phase 5: RSA analysis\\\")\\n    from scipy.spatial.distance import pdist\\n    from scipy.stats import spearmanr\\n\\n    rng = np.random.RandomState(seed)\\n    n_tasks = int(task_labels.max()) + 1\\n    layers_to_check = [0, 4, 8, 12, 16, 20, 24, 28, 31]\\n\\n    results = {\\n        \\\"method\\\": {\\n            \\\"pairing\\\": \\\"within-task\\\",\\n            \\\"rep_distance\\\": \\\"cosine\\\",\\n            \\\"act_distance\\\": \\\"euclidean\\\",\\n            \\\"n_sample\\\": n_sample,\\n            \\\"bootstrap_n\\\": bootstrap_n,\\n            \\\"seed\\\": seed,\\n            \\\"n_tasks\\\": n_tasks,\\n            \\\"layers\\\": layers_to_check,\\n        },\\n     
…[truncated 7168 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-21T16:54:02.846069+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n            demo_means = [float(np.mean(per_task_demo_mses[ti][di]))\\n                          for di in range(n_demos)]\\n            da = np.array(demo_means)\\n            dd = float(da.mean() / da.std(ddof=1)) if da.std(ddof=1) > 0 else 0.0\\n\\n            entry = {\\n                \\\"cohens_d\\\": round(td, 4),\\n                \\\"demo_level_cohens_d\\\": round(dd, 4),\\n                \\\"n_samples\\\": len(tm),\\n                \\\"mean_mse\\\": round(float(tm.mean()), 6),\\n                \\\"demo_mses\\\": [round(v, 6) for v in demo_means],\\n                \\\"instruction_correct\\\": INSTRUCTIONS[ti],\\n                \\\"instruction_counterfactual\\\": _cf_instruction(ti, cond),\\n            }\\n            cond_res[\\\"per_task\\\"][TASKS[ti]] = entry\\n\\n        cond_res[\\\"cross_task_variance\\\"] = {\\n            \\\"cohens_d\\\": {\\n                \\\"values\\\": [round(v, 4) for v in per_task_ds],\\n                \\\"mean\\\": round(float(np.mean(per_task_ds)), 4),\\n                \\\"std\\\": round(float(np.std(per_task_ds)), 4),\\n                \\\"cv\\\": round(float(np.std(per_task_ds) / np.mean(per_task_ds)), 4)\\n                     if np.mean(per_task_ds) > 0 else 0.0,\\n            }\\n        }\\n        all_res[cond] = cond_res\\n        log(f\\\"  {cond}: global d={global_d:.4f}  \\\"\\n            f\\\"cross-task mean={np.mean(per_task_ds):.4f}  \\\"\\n            f\\\"token_div={np.mean(all_tok_div):.3f}\\\")\\n\\n    ranking = sorted(conditions,\\n                     key=lambda c: all_res[c][\\\"global_metrics\\\"][\\\"paired_mse\\\"][\\\"cohens_d\\\"],\\n                     reverse=True)\\n    all_res[\\\"ranking_by_cohens_d\\\"] = [\\n        {\\\"condition\\\": c,\\n         \\\"cohens_d\\\": all_res[c][\\\"global_metrics\\\"][\\\"paired_mse\\\"][\\\"cohens_d\\\"],\\n         \\\"paired_mse_mean\\\": all_res[c][\\\"global_metrics\\\"][\\\"paired_
…[truncated 7105 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-21T16:54:02.846283+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -n \"def run_counterfactual\" /root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py /root/autodl-tmp/vla-ssd/scripts/tracvla_object_full_pipeline.py /root/autodl-tmp/vla-ssd/scripts/nora_goal_full_pipeline.py /root/autodl-tmp/vla-ssd/scripts/libero_long_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "grep -n \"def run_counterfactual\" /root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py /root/autodl-tmp/vla-ssd/scripts/tracvla_object_full_pipeline.py /root/autodl-tmp/vla-ssd/scripts/nora_goal_full_pipeline.py /root/autodl-tmp/vla-ssd/scripts/libero_long_full_pipeline.py"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-21T16:54:02.846433+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py:296:def run_counterfactual(model, processor, n_tasks, n_demos, n_timesteps):\\n/root/autodl-tmp/vla-ssd/scripts/tracvla_object_full_pipeline.py:328:def run_counterfactual(model, processor, n_tasks, n_demos, n_timesteps):\\n/root/autodl-tmp/vla-ssd/scripts/nora_goal_full_pipeline.py:299:def run_counterfactual(model, processor, config, n_tasks, n_demos, n_timesteps):\\n/root/autodl-tmp/vla-ssd/scripts/libero_long_full_pipeline.py:309:def run_counterfactual(model, processor, n_tasks, n_demos, n_timesteps):\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-21T16:54:02.846571+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "sed -n '296,420p' /root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "sed -n '296,420p' /root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-21T16:54:02.846699+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'sed' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-21T16:54:02.846820+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "sed -n '328,460p' /root/autodl-tmp/vla-ssd/scripts/tracvla_object_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "sed -n '328,460p' /root/autodl-tmp/vla-ssd/scripts/tracvla_object_full_pipeline.py"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-21T16:54:02.846958+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'sed' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-21T16:54:02.847085+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "sed -n '299,430p' /root/autodl-tmp/vla-ssd/scripts/nora_goal_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "sed -n '299,430p' /root/autodl-tmp/vla-ssd/scripts/nora_goal_full_pipeline.py"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-21T16:54:02.847205+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'sed' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-21T16:54:02.847322+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "tail -n +296 /root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "tail -n +296 /root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py"
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-21T16:54:02.847439+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "tail -n +328 /root/autodl-tmp/vla-ssd/scripts/tracvla_object_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "tail -n +328 /root/autodl-tmp/vla-ssd/scripts/tracvla_object_full_pipeline.py"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-21T16:54:02.847701+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"def run_counterfactual(model, processor, n_tasks, n_demos, n_timesteps):\\n    log(\\\"Phase 6: counterfactual analysis\\\")\\n    conditions = [\\\"wrong\\\", \\\"empty\\\", \\\"shuffled\\\", \\\"paraphrased\\\"]\\n\\n    all_res = {\\n        \\\"config\\\": {\\n            \\\"experiment\\\": \\\"counterfactual_libero_object\\\",\\n            \\\"conditions\\\": conditions,\\n            \\\"n_tasks\\\": n_tasks, \\\"n_demos_per_task\\\": n_demos,\\n            \\\"n_timesteps_per_demo\\\": n_timesteps,\\n            \\\"model\\\": \\\"openvla-7b-finetuned-libero-object\\\",\\n            \\\"unnorm_key\\\": UNNORM, \\\"seed\\\": 42,\\n            \\\"task_names\\\": TASKS[:n_tasks],\\n        }\\n    }\\n\\n    for cond in conditions:\\n        log(f\\\"  Condition: {cond}\\\")\\n        all_mses, all_tok_div = [], []\\n        per_task_mses = defaultdict(list)\\n        per_task_demo_mses = defaultdict(lambda: defaultdict(list))\\n        per_task_correct = defaultdict(list)\\n        per_task_cf = defaultdict(list)\\n        sample_n = 0\\n\\n        for ti in range(n_tasks):\\n            cf_instr = _cf_instruction(ti, cond)\\n            hdf5_path = os.path.join(DATA, f\\\"{TASKS[ti]}_demo.hdf5\\\")\\n\\n            with h5py.File(hdf5_path, \\\"r\\\") as hf:\\n                for di in range(n_demos):\\n                    n_avail = hf[f\\\"data/demo_{di}/actions\\\"].shape[0]\\n                    for t in range(min(n_timesteps, n_avail)):\\n                        img = Image.fromarray(\\n                            hf[f\\\"data/demo_{di}/obs/agentview_rgb\\\"][t])\\n\\n                        c_act, c_tok = generate_action(\\n                            model, processor, INSTRUCTIONS[ti], img)\\n                        f_act, f_tok = generate_action(\\n                            model, processor, cf_instr, img)\\n\\n                        mse = float(np.mean((c_act - f_act) ** 2))\\n             
…[truncated 7011 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-21T16:54:02.847884+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "tail -n +299 /root/autodl-tmp/vla-ssd/scripts/nora_goal_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "tail -n +299 /root/autodl-tmp/vla-ssd/scripts/nora_goal_full_pipeline.py"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-21T16:54:02.848182+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"def run_counterfactual(model, processor, n_tasks, n_demos, n_timesteps):\\n    log(\\\"Phase 5: counterfactual analysis\\\")\\n    conditions = [\\\"wrong\\\", \\\"empty\\\", \\\"shuffled\\\", \\\"paraphrased\\\"]\\n\\n    all_res = {\\n        \\\"config\\\": {\\n            \\\"experiment\\\": \\\"counterfactual_tracvla_object\\\",\\n            \\\"conditions\\\": conditions,\\n            \\\"n_tasks\\\": n_tasks,\\n            \\\"n_demos_per_task\\\": n_demos,\\n            \\\"n_timesteps_per_demo\\\": n_timesteps,\\n            \\\"model\\\": \\\"tracevla-phi3v\\\",\\n            \\\"action_space\\\": \\\"normalized_bins\\\",\\n            \\\"seed\\\": 42,\\n            \\\"task_names\\\": TASKS[:n_tasks],\\n        }\\n    }\\n\\n    for cond in conditions:\\n        log(f\\\"  Condition: {cond}\\\")\\n        all_mses, all_tok_div = [], []\\n        per_task_mses = defaultdict(list)\\n        per_task_demo_mses = defaultdict(lambda: defaultdict(list))\\n        per_task_correct = defaultdict(list)\\n        per_task_cf = defaultdict(list)\\n        sample_n = 0\\n\\n        for ti in range(n_tasks):\\n            cf_instr = _cf_instruction(ti, cond)\\n            hdf5_path = os.path.join(DATA, f\\\"{TASKS[ti]}_demo.hdf5\\\")\\n\\n            with h5py.File(hdf5_path, \\\"r\\\") as hf:\\n                for di in range(n_demos):\\n                    n_avail = hf[f\\\"data/demo_{di}/actions\\\"].shape[0]\\n                    for t in range(min(n_timesteps, n_avail)):\\n                        img = Image.fromarray(\\n                            hf[f\\\"data/demo_{di}/obs/agentview_rgb\\\"][t]\\n                        )\\n\\n                        c_act, c_tok = generate_action_phi3v(\\n                            model, processor, INSTRUCTIONS[ti], img\\n                        )\\n                        f_act, f_tok = generate_action_phi3v(\\n                            model, processor, cf_instr
…[truncated 7173 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-21T16:54:02.848553+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"def run_counterfactual(model, processor, config, n_tasks, n_demos, n_timesteps):\\n    log(\\\"Phase 5: counterfactual analysis (representation-based)\\\")\\n    conditions = [\\\"wrong\\\", \\\"empty\\\", \\\"shuffled\\\", \\\"paraphrased\\\"]\\n\\n    cf_layers = sorted(set(list(range(0, N_LAYERS, 3)) + [N_LAYERS - 1]))\\n\\n    all_res = {\\n        \\\"config\\\": {\\n            \\\"experiment\\\": \\\"counterfactual_nora_goal\\\",\\n            \\\"conditions\\\": conditions,\\n            \\\"n_tasks\\\": n_tasks,\\n            \\\"n_demos_per_task\\\": n_demos,\\n            \\\"n_timesteps_per_demo\\\": n_timesteps,\\n            \\\"model\\\": \\\"nora-libero-goal\\\",\\n            \\\"method\\\": \\\"representation_cosine_distance\\\",\\n            \\\"note\\\": \\\"NORA uses FAST+ action tokens; MSE-based counterfactual \\\"\\n                    \\\"not applicable. Using readout cosine distance instead.\\\",\\n            \\\"layers_analyzed\\\": cf_layers,\\n            \\\"seed\\\": 42,\\n            \\\"task_names\\\": TASKS[:n_tasks],\\n        }\\n    }\\n\\n    for cond in conditions:\\n        log(f\\\"  Condition: {cond}\\\")\\n        per_layer_dists = {l: [] for l in cf_layers}\\n        per_task_dists = defaultdict(list)\\n        per_task_demo_dists = defaultdict(lambda: defaultdict(list))\\n        sample_n = 0\\n\\n        for ti in range(n_tasks):\\n            cf_instr = _cf_instruction(ti, cond)\\n            hdf5_path = os.path.join(DATA, f\\\"{TASKS[ti]}_demo.hdf5\\\")\\n\\n            with h5py.File(hdf5_path, \\\"r\\\") as hf:\\n                for di in range(n_demos):\\n                    n_avail = hf[f\\\"data/demo_{di}/actions\\\"].shape[0]\\n                    for t in range(min(n_timesteps, n_avail)):\\n                        img = Image.fromarray(\\n                            hf[f\\\"data/demo_{di}/obs/agentview_rgb\\\"][t]\\n                        )\\n\\n        
…[truncated 7152 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-21T16:54:02.848779+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -n \"def generate_action\" /root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py /root/autodl-tmp/vla-ssd/scripts/tracvla_object_full_pipeline.py /root/autodl-tmp/vla-ssd/scripts/libero_long_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "grep -n \"def generate_action\" /root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py /root/autodl-tmp/vla-ssd/scripts/tracvla_object_full_pipeline.py /root/autodl-tmp/vla-ssd/scripts/libero_long_full_pipeline.py"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-21T16:54:02.848946+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py:86:def generate_action(model, processor, instruction, image):\\n/root/autodl-tmp/vla-ssd/scripts/tracvla_object_full_pipeline.py:118:def generate_action_phi3v(model, processor, instruction, image):\\n/root/autodl-tmp/vla-ssd/scripts/libero_long_full_pipeline.py:99:def generate_action(model, processor, instruction, image):\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-21T16:54:02.849092+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "head -100 /root/autodl-tmp/vla-ssd/scripts/tracvla_spatial_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "head -100 /root/autodl-tmp/vla-ssd/scripts/tracvla_spatial_full_pipeline.py"
  }
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-21T16:54:02.849219+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "head -100 /root/autodl-tmp/vla-ssd/scripts/nora_spatial_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "head -100 /root/autodl-tmp/vla-ssd/scripts/nora_spatial_full_pipeline.py"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-21T16:54:02.849395+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nLIBERO-Spatial Full Analysis Pipeline for TracVLA-Phi3V\\n\\nPhases:\\n  1. Representation extraction: forward passes -> hidden states + L1 attention\\n  2. Action R2 probing: per-layer Ridge probe\\n  3. L1 attention profile: per-head instruction/image attention classification\\n  4. Cross-instruction classification: 10-way per-layer\\n  5. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased), paired Cohen's d\\n\\nRuns both trained (TracVLA-Phi3V) and untrained (base Phi-3-Vision) sequentially.\\nAll results -> RESULTS_DIR/{trained,untrained}/*.json\\nNo intermediate features saved to disk.\\n\\\"\\\"\\\"\\n\\nimport argparse, json, os, random, sys, time\\nfrom collections import defaultdict\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nfrom PIL import Image\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.linear_model import RidgeCV\\nfrom transformers import AutoModelForCausalLM, AutoProcessor\\n\\n# --- Checkpoints ---\\nTRAINED_CKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v/\\\"\\nUNTRAINED_CKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base/\\\"\\nUNTRAINED_CACHE = \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base/\\\"\\n\\n# --- Data ---\\nDATA = \\\"/root/autodl-tmp/vla-ssd/data/libero/libero_spatial\\\"\\nRESULTS_BASE = \\\"/root/autodl-tmp/vla-ssd/results/tracvla_spatial\\\"\\nDEVICE = \\\"cuda:0\\\"  # submit_training_job sets CUDA_VISIBLE_DEVICES\\n\\n# --- Architecture ---\\nN_LAYERS = 32\\nN_HEADS = 32\\nHIDDEN = 3072\\nN_IMG_TOKENS = 0  # auto-detected\\nIMG_TOKEN_ID = -1  # auto-detected\\n\\n# --- Data config ---\\nN_DEMOS = 10\\nN_TIMESTEPS = 50\\nN_PROBE_SEEDS = 15\\n\\nTASKS = [\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_on
…[truncated 2385 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-21T16:54:02.849740+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nNORA LIBERO-Spatial Full Analysis Pipeline\\n\\nPhases:\\n  1. Representation extraction: forward passes -> hidden states + L1 attention\\n  2. Action R2 probing: per-layer Ridge probe\\n  3. L1 attention profile: per-head instruction/image attention classification\\n  4. Cross-instruction classification: 10-way per-layer\\n  5. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased)\\n\\nRuns both trained (NORA) and untrained (Qwen2.5-VL-3B base) sequentially.\\nNORA uses FAST+ action tokenizer, so counterfactual uses representation-based\\ncosine distance instead of action MSE.\\n\\\"\\\"\\\"\\n\\nimport argparse, json, os, random, sys, time\\nfrom collections import defaultdict\\n\\nos.environ[\\\"HDF5_USE_FILE_LOCKING\\\"] = \\\"FALSE\\\"\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nimport torch.nn.functional as F\\nfrom PIL import Image\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.linear_model import RidgeCV\\nfrom transformers import AutoModelForImageTextToText, AutoProcessor\\n\\n# --- Checkpoints ---\\nTRAINED_CKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-spatial/\\\"\\nUNTRAINED_CKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base/\\\"\\n\\n# --- Data ---\\nDATA = \\\"/root/autodl-tmp/vla-ssd/data/libero/libero_spatial\\\"\\nRESULTS_BASE = \\\"/root/autodl-tmp/vla-ssd/results/nora_spatial\\\"\\nDEVICE = \\\"cuda:0\\\"\\n\\n# --- Architecture (Qwen2.5-VL-3B) ---\\nN_LAYERS = 36\\nN_HEADS = 16\\nHIDDEN = 2048\\n\\n# --- Data config ---\\nN_DEMOS = 10\\nN_TIMESTEPS = 50\\nN_PROBE_SEEDS = 15\\n\\nTASKS = [\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\",\\n    \\\"pick
…[truncated 2458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-21T16:54:02.849941+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "tail -n +86 /root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "tail -n +86 /root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py"
  }
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-21T16:54:02.850081+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "tail -n +99 /root/autodl-tmp/vla-ssd/scripts/libero_long_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "tail -n +99 /root/autodl-tmp/vla-ssd/scripts/libero_long_full_pipeline.py"
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-21T16:54:02.850329+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"def generate_action(model, processor, instruction, image):\\n    inputs = prepare_inputs(processor, instruction, image)\\n    input_ids = inputs[\\\"input_ids\\\"]\\n\\n    if not torch.all(input_ids[:, -1] == 29871):\\n        input_ids = torch.cat(\\n            (input_ids, torch.tensor([[29871]], device=DEVICE, dtype=input_ids.dtype)), dim=1\\n        )\\n        if \\\"attention_mask\\\" in inputs:\\n            inputs[\\\"attention_mask\\\"] = torch.cat(\\n                (inputs[\\\"attention_mask\\\"],\\n                 torch.ones(1, 1, device=DEVICE, dtype=inputs[\\\"attention_mask\\\"].dtype)), dim=1\\n            )\\n    inputs[\\\"input_ids\\\"] = input_ids\\n\\n    with torch.no_grad():\\n        gen_ids = model.generate(\\n            inputs[\\\"input_ids\\\"],\\n            attention_mask=inputs.get(\\\"attention_mask\\\"),\\n            pixel_values=inputs.get(\\\"pixel_values\\\"),\\n            max_new_tokens=7, do_sample=False,\\n        )\\n    token_ids = gen_ids[0, -7:].cpu().numpy()\\n\\n    vocab_size = model.vocab_size\\n    disc = np.clip(vocab_size - token_ids - 1, 0, model.bin_centers.shape[0] - 1)\\n    norm_act = model.bin_centers[disc]\\n\\n    stats = model.get_action_stats(UNNORM)\\n    mask = np.array(stats.get(\\\"mask\\\", [True] * 7))\\n    high, low = np.array(stats[\\\"q99\\\"]), np.array(stats[\\\"q01\\\"])\\n    action = np.where(mask, 0.5 * (norm_act + 1) * (high - low) + low, norm_act)\\n\\n    del inputs, gen_ids\\n    return action.astype(np.float64), token_ids\\n\\n\\ndef extract_features(model, processor, n_tasks, n_demos, n_timesteps):\\n    log(\\\"Phase 1: representation extraction\\\")\\n    total = n_tasks * n_demos * n_timesteps\\n\\n    reps = {\\n        l: {\\n            \\\"image_mean\\\": np.zeros((total, HIDDEN), dtype=np.float32),\\n            \\\"last_preaction\\\": np.zeros((total, HIDDEN), dtype=np.float32),\\n        }\\n        for l in range(N_
…[truncated 6892 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-21T16:54:02.850492+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "tail -n +118 /root/autodl-tmp/vla-ssd/scripts/tracvla_object_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "tail -n +118 /root/autodl-tmp/vla-ssd/scripts/tracvla_object_full_pipeline.py"
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-21T16:54:02.850746+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"def generate_action(model, processor, instruction, image):\\n    inputs = prepare_inputs(processor, instruction, image)\\n    input_ids = inputs[\\\"input_ids\\\"]\\n\\n    if not torch.all(input_ids[:, -1] == 29871):\\n        input_ids = torch.cat(\\n            (input_ids, torch.tensor([[29871]], device=DEVICE, dtype=input_ids.dtype)), dim=1\\n        )\\n        if \\\"attention_mask\\\" in inputs:\\n            inputs[\\\"attention_mask\\\"] = torch.cat(\\n                (inputs[\\\"attention_mask\\\"],\\n                 torch.ones(1, 1, device=DEVICE, dtype=inputs[\\\"attention_mask\\\"].dtype)), dim=1\\n            )\\n    inputs[\\\"input_ids\\\"] = input_ids\\n\\n    with torch.no_grad():\\n        gen_ids = model.generate(\\n            inputs[\\\"input_ids\\\"],\\n            attention_mask=inputs.get(\\\"attention_mask\\\"),\\n            pixel_values=inputs.get(\\\"pixel_values\\\"),\\n            max_new_tokens=7, do_sample=False,\\n        )\\n    token_ids = gen_ids[0, -7:].cpu().numpy()\\n\\n    vocab_size = model.vocab_size\\n    disc = np.clip(vocab_size - token_ids - 1, 0, model.bin_centers.shape[0] - 1)\\n    norm_act = model.bin_centers[disc]\\n\\n    stats = model.get_action_stats(UNNORM)\\n    mask = np.array(stats.get(\\\"mask\\\", [True] * 7))\\n    high, low = np.array(stats[\\\"q99\\\"]), np.array(stats[\\\"q01\\\"])\\n    action = np.where(mask, 0.5 * (norm_act + 1) * (high - low) + low, norm_act)\\n\\n    del inputs, gen_ids\\n    return action.astype(np.float64), token_ids\\n\\n\\ndef extract_features(model, processor, n_tasks, n_demos, n_timesteps):\\n    log(\\\"Phase 1: representation extraction\\\")\\n    total = n_tasks * n_demos * n_timesteps\\n\\n    reps = {\\n        l: {\\n            \\\"image_mean\\\": np.zeros((total, HIDDEN), dtype=np.float32),\\n            \\\"last_preaction\\\": np.zeros((total, HIDDEN), dtype=np.float32),\\n        }\\n        for l in range(N_
…[truncated 6903 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-21T16:54:02.851058+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"def generate_action_phi3v(model, processor, instruction, image):\\n    inputs = prepare_inputs(processor, instruction, image)\\n\\n    with torch.no_grad():\\n        gen_ids = model.generate(\\n            input_ids=inputs[\\\"input_ids\\\"],\\n            attention_mask=inputs.get(\\\"attention_mask\\\"),\\n            pixel_values=inputs.get(\\\"pixel_values\\\"),\\n            image_sizes=inputs.get(\\\"image_sizes\\\"),\\n            max_new_tokens=7,\\n            do_sample=False,\\n        )\\n\\n    token_ids = gen_ids[0, -7:].cpu().numpy()\\n    vocab_size = model.config.vocab_size\\n    n_bins = 256\\n    bins = np.linspace(-1, 1, n_bins)\\n    bin_centers = (bins[:-1] + bins[1:]) / 2.0\\n\\n    disc = np.clip(vocab_size - token_ids - 1, a_min=0, a_max=bin_centers.shape[0] - 1)\\n    norm_act = bin_centers[disc]\\n\\n    del inputs, gen_ids\\n    return norm_act.astype(np.float64), token_ids\\n\\n\\ndef extract_features(model, processor, n_tasks, n_demos, n_timesteps, img_token_id):\\n    log(\\\"Phase 1: representation extraction\\\")\\n    total = n_tasks * n_demos * n_timesteps\\n\\n    reps = {\\n        l: {\\n            \\\"image_mean\\\": np.zeros((total, HIDDEN), dtype=np.float32),\\n            \\\"last_preaction\\\": np.zeros((total, HIDDEN), dtype=np.float32),\\n        }\\n        for l in range(N_LAYERS)\\n    }\\n    actions_arr = np.zeros((total, 7), dtype=np.float32)\\n    task_labels = np.zeros(total, dtype=np.int64)\\n    head_instr_ratio_sum = np.zeros(N_HEADS, dtype=np.float64)\\n    head_instr_ratio_sq_sum = np.zeros(N_HEADS, dtype=np.float64)\\n    attn_count = 0\\n\\n    idx = 0\\n    for ti in range(n_tasks):\\n        hdf5_path = os.path.join(DATA, f\\\"{TASKS[ti]}_demo.hdf5\\\")\\n        log(f\\\"  Task {ti}/{n_tasks}: {TASKS[ti]}\\\")\\n\\n        with h5py.File(hdf5_path, \\\"r\\\") as hf:\\n            for di in range(n_demos):\\n                demo = f\\\"data/demo_{di
…[truncated 7024 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-21T16:54:02.851258+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "head -90 /root/autodl-tmp/vla-ssd/scripts/tracvla_long_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "head -90 /root/autodl-tmp/vla-ssd/scripts/tracvla_long_full_pipeline.py"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-21T16:54:02.851444+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nLIBERO-Long Full Analysis Pipeline for TracVLA-Phi3V\\n\\nPhases:\\n  1. Representation extraction: forward passes -> hidden states + L1 attention\\n  2. Action R2 probing: per-layer Ridge probe\\n  3. L1 attention profile: per-head instruction/image attention classification\\n  4. Cross-instruction classification: 10-way per-layer\\n  5. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased), paired Cohen's d\\n\\nRuns both trained (TracVLA-Phi3V) and untrained (base Phi-3-Vision) sequentially.\\nAll results -> RESULTS_DIR/{trained,untrained}/*.json\\nNo intermediate features saved to disk.\\n\\\"\\\"\\\"\\n\\nimport argparse, json, os, random, sys, time\\nfrom collections import defaultdict\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nfrom PIL import Image\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.linear_model import RidgeCV\\nfrom transformers import AutoModelForCausalLM, AutoProcessor\\n\\n# --- Checkpoints ---\\nTRAINED_CKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v/\\\"\\nUNTRAINED_CKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base/\\\"\\nUNTRAINED_CACHE = \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base/\\\"\\n\\n# --- Data ---\\nDATA = \\\"/root/autodl-tmp/vla-ssd/data/libero/libero_10\\\"\\nRESULTS_BASE = \\\"/root/autodl-tmp/vla-ssd/results/tracvla_long\\\"\\nDEVICE = \\\"cuda:0\\\"  # submit_training_job sets CUDA_VISIBLE_DEVICES\\n\\n# --- Architecture ---\\nN_LAYERS = 32\\nN_HEADS = 32\\nHIDDEN = 3072\\nN_IMG_TOKENS = 0  # auto-detected\\nIMG_TOKEN_ID = -1  # auto-detected\\n\\n# --- Data config ---\\nN_DEMOS = 10\\nN_TIMESTEPS = 50\\nN_PROBE_SEEDS = 15\\n\\nTASKS = [\\n    \\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\",\\n    \\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\",\\n    \\\"KITCHEN_SCENE6_put_the_yellow_and_white_
…[truncated 2524 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-21T16:54:02.851627+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "head -90 /root/autodl-tmp/vla-ssd/scripts/tracvla_goal_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "head -90 /root/autodl-tmp/vla-ssd/scripts/tracvla_goal_full_pipeline.py"
  }
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-21T16:54:02.851767+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "find /root/autodl-tmp/vla-ssd/scripts -name \"*goal*pipeline*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "find /root/autodl-tmp/vla-ssd/scripts -name \"*goal*pipeline*\""
  }
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-21T16:54:02.851953+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nLIBERO-Goal Full Analysis Pipeline for TracVLA-Phi3V\\n\\nPhases:\\n  1. Representation extraction: forward passes -> hidden states + L1 attention\\n  2. Action R2 probing: per-layer Ridge probe\\n  3. L1 attention profile: per-head instruction/image attention classification\\n  4. Cross-instruction classification: 10-way per-layer\\n  5. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased), paired Cohen's d\\n\\nRuns both trained (TracVLA-Phi3V) and untrained (base Phi-3-Vision) sequentially.\\nAll results -> RESULTS_DIR/{trained,untrained}/*.json\\nNo intermediate features saved to disk.\\n\\\"\\\"\\\"\\n\\nimport argparse, json, os, random, sys, time\\nfrom collections import defaultdict\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nfrom PIL import Image\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.linear_model import RidgeCV\\nfrom transformers import AutoModelForCausalLM, AutoProcessor\\n\\n# --- Checkpoints ---\\nTRAINED_CKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v/\\\"\\nUNTRAINED_CKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base/\\\"\\nUNTRAINED_CACHE = \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base/\\\"\\n\\n# --- Data ---\\nDATA = \\\"/root/autodl-tmp/vla-ssd/data/libero/libero_goal\\\"\\nRESULTS_BASE = \\\"/root/autodl-tmp/vla-ssd/results/tracvla_goal\\\"\\nDEVICE = \\\"cuda:0\\\"  # submit_training_job sets CUDA_VISIBLE_DEVICES\\n\\n# --- Architecture ---\\nN_LAYERS = 32\\nN_HEADS = 32\\nHIDDEN = 3072\\nN_IMG_TOKENS = 0  # auto-detected\\nIMG_TOKEN_ID = -1  # auto-detected\\n\\n# --- Data config ---\\nN_DEMOS = 10\\nN_TIMESTEPS = 50\\nN_PROBE_SEEDS = 15\\n\\nTASKS = [\\n    \\\"open_the_middle_drawer_of_the_cabinet\\\",\\n    \\\"open_the_top_drawer_and_put_the_bowl_inside\\\",\\n    \\\"push_the_plate_to_the_front_of_the_stove\\\",\\n    \\\"put_the_bowl_on_the_plate\\\",\\n    \\\"pu
…[truncated 1369 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-21T16:54:02.852120+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/vla-ssd/scripts/nora_goal_full_pipeline.py\\n/root/autodl-tmp/vla-ssd/scripts/nora_goal_full_pipeline.py.bak\\n/root/autodl-tmp/vla-ssd/scripts/tracvla_goal_full_pipeline.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.59}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-21T16:54:02.852267+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "head -100 /root/autodl-tmp/vla-ssd/scripts/libero_object_untrained_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "head -100 /root/autodl-tmp/vla-ssd/scripts/libero_object_untrained_full_pipeline.py"
  }
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-21T16:54:02.852393+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -n \"def _cf_instruction\" /root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "grep -n \"def _cf_instruction\" /root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py"
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-21T16:54:02.852568+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nLIBERO-Object Full Analysis Pipeline (Streaming)\\n\\nPhases:\\n  1. Representation extraction: forward passes -> hidden states + L1 attention\\n  2. Action R2 probing: per-layer Ridge probe\\n  3. L1 attention profile: per-head instruction/image attention classification\\n  4. Cross-instruction classification: 10-way per-layer\\n  5. RSA: representational similarity across conditions\\n  6. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased), paired Cohen's d\\n\\nAll results -> RESULTS_DIR/*.json\\nNo intermediate features saved to disk.\\n\\\"\\\"\\\"\\n\\nimport argparse, json, os, random, sys, time\\nfrom collections import defaultdict\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nfrom PIL import Image\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.linear_model import RidgeCV\\nfrom transformers import AutoModelForVision2Seq, AutoProcessor\\n\\nCKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"\\nDATA = \\\"/root/autodl-tmp/vla-ssd/data/libero/libero_object\\\"\\nRESULTS_DIR = \\\"/root/autodl-tmp/vla-ssd/results/libero_object_untrained\\\"\\nDEVICE = \\\"cuda:0\\\"\\nUNNORM = \\\"bridge_orig\\\"\\n\\nTASKS = [\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\",\\n]\\nINSTRUCTIONS = [t.replace(\\\"_\\\", \\\" \\\") for t
…[truncated 2125 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-21T16:54:02.852724+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"283:def _cf_instruction(task_idx, condition):\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.58}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-21T16:54:02.852850+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -n \"counterfactual\" /root/autodl-tmp/vla-ssd/scripts/libero_object_untrained_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "grep -n \"counterfactual\" /root/autodl-tmp/vla-ssd/scripts/libero_object_untrained_full_pipeline.py"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-21T16:54:02.853027+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"295:def run_counterfactual(model, processor, n_tasks, n_demos, n_timesteps):\\n296:    log(\\\"Phase 6: counterfactual analysis\\\")\\n301:            \\\"experiment\\\": \\\"counterfactual_libero_object\\\",\\n396:                \\\"instruction_counterfactual\\\": _cf_instruction(ti, cond),\\n508:    p.add_argument(\\\"--skip-counterfactual\\\", action=\\\"store_true\\\")\\n594:    if not args.skip_counterfactual:\\n596:        cf_res = run_counterfactual(model, processor, nt, nd, ns)\\n597:        with open(os.path.join(RESULTS_DIR, \\\"counterfactual_combined.json\\\"), \\\"w\\\") as f:\\n599:        log(f\\\"Phase 6: {time.time()-t5:.1f}s -> counterfactual_combined.json\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-21T16:54:02.853185+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ls /root/autodl-tmp/vla-ssd/data/libero/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ls /root/autodl-tmp/vla-ssd/data/libero/"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-21T16:54:02.853314+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"libero_10\\nlibero_90\\nlibero_goal\\nlibero_object\\nlibero_spatial\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.54}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-21T16:54:02.853434+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ls /root/autodl-tmp/vla-ssd/checkpoints/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ls /root/autodl-tmp/vla-ssd/checkpoints/"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-21T16:54:02.853558+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"dinov2-large\\nnora-libero-goal\\nnora-libero-spatial\\nopenvla-7b\\nopenvla-7b-finetuned-libero-goal\\nopenvla-7b-finetuned-libero-object\\nopenvla-7b-oft-finetuned-libero-10\\nopenvla-phi3v\\nphi3v-base\\nphi3v-base-ms\\nqwen25-vl-3b-base\\ntracevla-phi3v\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.58}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-21T16:54:02.853692+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "find /root/autodl-tmp/vla-ssd/scripts -name \"*libero*\" -name \"*pipeline*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "find /root/autodl-tmp/vla-ssd/scripts -name \"*libero*\" -name \"*pipeline*\""
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-21T16:54:02.853821+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py\\n/root/autodl-tmp/vla-ssd/scripts/libero_long_full_pipeline.py\\n/root/autodl-tmp/vla-ssd/scripts/libero_object_untrained_full_pipeline.py\\n/root/autodl-tmp/vla-ssd/scripts/libero_long_full_pipeline.py.bak\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.54}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-21T16:54:02.854256+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19183",
  "command": "cat << 'SCRIPT_EOF' > /root/autodl-tmp/vla-ssd/scripts/counterfactual_batch.py\n#!/usr/bin/env python3\n\"\"\"\nCounterfactual-only batch runner for VLA-SSD experiments.\n\nSupports openvla/tracvla/nora architectures across goal/spatial/object/long suites.\nAuto-selects method: action_mse for trained openvla/tracvla, cosine_dist for nora\nand all untrained models. Override with --method.\n\nUsage:\n  python counterfactual_batch.py --arch tracvla --suite spatial --condition untrained\n  python counterfactual_batch.py --arch openvla --suite long --condition trained\n  python counterfactual_batch.py --arch openvla --suite object --condition untrained\n  python counterfactual_batch.py --arch nora --suite goal --condition untrained\n\"\"\"\n\nimport argparse, json, os, random, sys, time\nfrom collections import defaultdict\n\nos.environ[\"HDF5_USE_FILE_LOCKING\"] = \"FALSE\"\n\nimport h5py\nimport numpy as np\nimport torch\nimport torch.nn.functional as F\nfrom PIL import Image\n\nDEVICE = \"cuda:0\"\n\ndef log(msg):\n    print(f\"[{time.strftime('%H:%M:%S')}] {msg}\", flush=True)\n\n# ============================================================\n# Architecture configs\n# ============================================================\nARCH_CFG = {\n    \"openvla\": {\"n_layers\": 32, \"n_heads\": 32, \"hidden\": 4096},\n    \"tracvla\": {\"n_layers\": 32, \"n_heads\": 32, \"hidden\": 3072},\n    \"nora\":    {\"n_layers\": 36, \"n_heads\": 16, \"hidden\": 2048},\n}\n\n# ============================================================\n# Checkpoint registry\n# ============================================================\nCKPT_MAP = {\n    (\"openvla\", \"object\", \"trained\"):   \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-object\",\n    (\"openvla\", \"object\", \"untrained\"): \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\",\n    (\"openvla\", \"long\", \"trained\"):     \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-oft-finetuned-libero-10\",\n    (\"openvla\", \"long\", \"untrained\"):   \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\",\n    (\"openvla\", \"goal\", \"trained\"):     \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-goal\",\n    (\"openvla\", \"goal\", \"untrained\"):   \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\",\n    (\"tracvla\", \"object\", \"trained\"):   \"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v/\",\n    (\"tracvla\", \"object\", \"untrained\"): \"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base/\",\n    (\"tracvla\", \"spatial\", \"trained\"):  \"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v/\",\n    (\"tracvla\", \"spatial\", \"untrained\"):\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base/\",\n    (\"tracvla\", \"goal\", \"trained\"):     \"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v/\",\n    (\"tracvla\", \"goal\", \"untrained\"):   \"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base/\",\n    (\"tracvla\", \"long\", \"trained\"):     \"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v/\",\n    (\"tracvla\", \"long\", \"untrained\"):   \"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base/\",\n    (\"nora\", \"goal\", \"trained\"):        \"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-goal/\",\n    (\"nora\", \"goal\", \"untrained\"):      \"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base/\",\n    (\"nora\", \"spatial\", \"trained\"):     \"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-spatial/\",\n    (\"nora\", \"spatial\", \"untrained\"):   \"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base/\",\n}\n\n# ============================================================\n# Data directories\n# ============================================================\nDATA_MAP = {\n    \"goal\":    \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal\",\n    \"spatial\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_spatial\",\n    \"object\":  \"/root/autodl-tmp/vla-ssd/data/libero/libero_object\",\n    \"long\":    \"/root/autodl-tmp/vla-ssd/data/libero/libero_10\",\n}\n\n# ============================================================\n# Results directories\n# ============================================================\nRESULTS_MAP = {\n    (\"openvla\", \"object\", \"trained\"):   \"/root/autodl-tmp/vla-ssd/results/libero_object/trained\",\n    (\"openvla\", \"object\", \"untrained\"): \"/root/autodl-tmp/vla-ssd/results/libero_object_untrained\",\n    (\"openvla\", \"long\", \"trained\"):     \"/root/autodl-tmp/vla-ssd/results/libero_long/trained\",\n    (\"openvla\", \"long\", \"untrained\"):   \"/root/autodl-tmp/vla-ssd/results/libero_long/untrained\",\n    (\"openvla\", \"goal\", \"trained\"):     \"/root/autodl-tmp/vla-ssd/results/libero_goal/trained\",\n    (\"openvla\", \"goal\", \"untrained\"):   \"/root/autodl-tmp/vla-ssd/results/libero_goal/untrained\",\n    (\"tracvla\", \"object\", \"trained\"):   \"/root/autodl-tmp/vla-ssd/results/tracvla_object/trained\",\n    (\"tracvla\", \"object\", \"untrained\"): \"/root/autodl-tmp/vla-ssd/results/tracvla_object/untrained\",\n    (\"tracvla\", \"spatial\", \"trained\"):  \"/root/autodl-tmp/vla-ssd/results/tracvla_spatial/trained\",\n    (\"tracvla\", \"spatial\", \"untrained\"):\"/root/autodl-tmp/vla-ssd/results/tracvla_spatial/untrained\",\n    (\"tracvla\", \"goal\", \"trained\"):     \"/root/autodl-tmp/vla-ssd/results/tracvla_goal/trained\",\n    (\"tracvla\", \"goal\", \"untrained\"):   \"/root/autodl-tmp/vla-ssd/results/tracvla_goal/untrained\",\n    (\"tracvla\", \"long\", \"trained\"):     \"/root/autodl-tmp/vla-ssd/results/tracvla_long/trained\",\n    (\"tracvla\", \"long\", \"untrained\"):   \"/root/autodl-tmp/vla-ssd/results/tracvla_long/untrained\",\n    (\"nora\", \"goal\", \"trained\"):        \"/root/autodl-tmp/vla-ssd/results/nora_goal/trained\",\n    (\"nora\", \"goal\", \"untrained\"):      \"/root/autodl-tmp/vla-ssd/results/nora_goal/untrained\",\n    (\"nora\", \"spatial\", \"trained\"):     \"/root/autodl-tmp/vla-ssd/results/nora_spatial/trained\",\n    (\"nora\", \"spatial\", \"untrained\"):   \"/root/autodl-tmp/vla-ssd/results/nora_spatial/untrained\",\n}\n\n# ============================================================\n# Unnorm keys (only for action_mse on OpenVLA)\n# ============================================================\nUNNORM_MAP = {\n    (\"openvla\", \"object\", \"trained\"):   \"libero_object\",\n    (\"openvla\", \"object\", \"untrained\"): \"bridge_orig\",\n    (\"openvla\", \"long\", \"trained\"):     \"libero_10_no_noops\",\n    (\"openvla\", \"long\", \"untrained\"):   \"bridge_orig\",\n    (\"openvla\", \"goal\", \"trained\"):     \"libero_goal\",\n    (\"openvla\", \"goal\", \"untrained\"):   \"bridge_orig\",\n}\n\n# ============================================================\n# Task configurations per (arch, suite)\n# Tasks and paraphrases must match the ordering used in the\n# original full_pipeline scripts so \"wrong\" condition is consistent.\n# ============================================================\n\n_GOAL_TASKS = [\n    \"open_the_middle_drawer_of_the_cabinet\",\n    \"open_the_top_drawer_and_put_the_bowl_inside\",\n    \"push_the_plate_to_the_front_of_the_stove\",\n    \"put_the_bowl_on_the_plate\",\n    \"put_the_bowl_on_the_stove\",\n    \"put_the_bowl_on_top_of_the_cabinet\",\n    \"put_the_cream_cheese_in_the_bowl\",\n    \"put_the_wine_bottle_on_the_rack\",\n    \"put_the_wine_bottle_on_top_of_the_cabinet\",\n    \"turn_on_the_stove\",\n]\n_GOAL_PARA = [\n    \"open the cabinet's middle drawer\",\n    \"open the top drawer and place the bowl in it\",\n    \"slide the plate to the stove's front\",\n    \"place the bowl onto the plate\",\n    \"place the bowl onto the stove\",\n    \"place the bowl on the cabinet top\",\n    \"put cream cheese into the bowl\",\n    \"place the wine bottle on the rack\",\n    \"place the wine bottle on the cabinet top\",\n    \"switch on the stove\",\n]\n\n_LONG_TASKS = [\n    \"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\",\n    \"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\",\n    \"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\",\n    \"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\",\n    \"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\",\n    \"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\",\n    \"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\",\n    \"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\",\n    \"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\",\n    \"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\",\n]\n_LONG_INSTR = [\n    \"turn on the stove and put the moka pot on it\",\n    \"put the black bowl in the bottom drawer of the cabinet and close it\",\n    \"put the yellow and white mug in the microwave and close it\",\n    \"put both moka pots on the stove\",\n    \"put both the alphabet soup and the cream cheese box in the basket\",\n    \"put both the alphabet soup and the tomato sauce in the basket\",\n    \"put both the cream cheese box and the butter in the basket\",\n    \"put the white mug on the left plate and put the yellow and white mug on the right plate\",\n    \"put the white mug on the plate and put the chocolate pudding to the right of the plate\",\n    \"pick up the book and place it in the back compartment of the caddy\",\n]\n_LONG_PARA = [\n    \"switch on the stove and place the moka pot on it\",\n    \"place the black bowl in the bottom drawer of the cabinet and shut it\",\n    \"place the yellow and white mug in the microwave and shut it\",\n    \"put both of the moka pots on the stove\",\n    \"place the alphabet soup and cream cheese box into the basket\",\n    \"place the alphabet soup and tomato sauce into the basket\",\n    \"place the cream cheese box and butter into the basket\",\n    \"place the white mug on the left plate and the yellow white mug on the right plate\",\n    \"place the white mug on the plate and the chocolate pudding to the right of the plate\",\n    \"grab the book and put it in the back section of the caddy\",\n]\n\n_OBJECT_OPENVLA_TASKS = [\n    \"pick_up_the_alphabet_soup_and_place_it_in_the_basket\",\n    \"pick_up_the_cream_cheese_and_place_it_in_the_basket\",\n    \"pick_up_the_salad_dressing_and_place_it_in_the_basket\",\n    \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\",\n    \"pick_up_the_ketchup_and_place_it_in_the_basket\",\n    \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\",\n    \"pick_up_the_butter_and_place_it_in_the_basket\",\n    \"pick_up_the_milk_and_place_it_in_the_basket\",\n    \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\",\n    \"pick_up_the_orange_juice_and_place_it_in_the_basket\",\n]\n_OBJECT_OPENVLA_PARA = [\n    \"grab the alphabet soup and put it into the basket\",\n    \"grab the cream cheese and put it into the basket\",\n    \"grab the salad dressing and put it into the basket\",\n    \"grab the bbq sauce and put it into the basket\",\n    \"grab the ketchup and put it into the basket\",\n    \"grab the tomato sauce and put it into the basket\",\n    \"grab the butter and put it into the basket\",\n    \"grab the milk and put it into the basket\",\n    \"grab the chocolate pudding and put it into the basket\",\n    \"grab the orange juice and put it into the basket\",\n]\n\n_OBJECT_TRACVLA_TASKS = [\n    \"pick_up_the_alphabet_soup_and_place_it_in_the_basket\",\n    \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\",\n    \"pick_up_the_butter_and_place_it_in_the_basket\",\n    \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\",\n    \"pick_up_the_cream_cheese_and_place_it_in_the_basket\",\n    \"pick_up_the_ketchup_and_place_it_in_the_basket\",\n    \"pick_up_the_milk_and_place_it_in_the_basket\",\n    \"pick_up_the_orange_juice_and_place_it_in_the_basket\",\n    \"pick_up_the_salad_dressing_and_place_it_in_the_basket\",\n    \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\",\n]\n_OBJECT_TRACVLA_PARA = [\n    \"grab the alphabet soup and put it into the basket\",\n    \"grab the bbq sauce and put it into the basket\",\n    \"grab the butter and put it into the basket\",\n    \"grab the chocolate pudding and put it into the basket\",\n    \"grab the cream cheese and put it into the basket\",\n    \"grab the ketchup and put it into the basket\",\n    \"grab the milk and put it into the basket\",\n    \"grab the orange juice and put it into the basket\",\n    \"grab the salad dressing and put it into the basket\",\n    \"grab the tomato sauce and put it into the basket\",\n]\n\n_SPATIAL_TRACVLA_TASKS = [\n    \"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\",\n    \"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\",\n    \"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\",\n    \"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\",\n    \"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\",\n    \"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\",\n    \"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\",\n    \"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\",\n    \"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\",\n    \"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\",\n]\n_SPATIAL_TRACVLA_PARA = [\n    \"grab the black bowl between the plate and ramekin and put it on the plate\",\n    \"grab the black bowl on the ramekin and put it on the plate\",\n    \"grab the black bowl on the cookie box and put it on the plate\",\n    \"grab the black bowl in the top drawer of the wooden cabinet and put it on the plate\",\n    \"grab the black bowl from the center of the table and put it on the plate\",\n    \"grab the black bowl next to the cookie box and put it on the plate\",\n    \"grab the black bowl on the stove and put it on the plate\",\n    \"grab the black bowl on the wooden cabinet and put it on the plate\",\n    \"grab the black bowl next to the plate and put it on the plate\",\n    \"grab the black bowl next to the ramekin and put it on the plate\",\n]\n\n_SPATIAL_NORA_TASKS = [\n    \"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\",\n    \"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\",\n    \"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\",\n    \"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\",\n    \"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\",\n    \"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\",\n    \"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\",\n    \"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\",\n    \"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\",\n    \"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\",\n]\n_SPATIAL_NORA_PARA = [\n    \"grab the black bowl between the plate and ramekin and put it on the plate\",\n    \"grab the black bowl from the center of the table and put it on the plate\",\n    \"grab the black bowl in the top drawer of the wooden cabinet and put it on the plate\",\n    \"grab the black bowl next to the cookie box and put it on the plate\",\n    \"grab the black bowl next to the plate and put it on the plate\",\n    \"grab the black bowl next to the ramekin and put it on the plate\",\n    \"grab the black bowl on the cookie box and put it on the plate\",\n    \"grab the black bowl on the ramekin and put it on the plate\",\n    \"grab the black bowl on the stove and put it on the plate\",\n    \"grab the black bowl on the wooden cabinet and put it on the plate\",\n]\n\n\ndef _make_instr(tasks):\n    return [t.replace(\"_\", \" \") for t in tasks]\n\n\ndef _get_task_config(arch, suite):\n    if suite == \"goal\":\n        return _GOAL_TASKS, _make_instr(_GOAL_TASKS), _GOAL_PARA\n    elif suite == \"long\":\n        return _LONG_TASKS, _LONG_INSTR, _LONG_PARA\n    elif suite == \"object\":\n        if arch == \"openvla\":\n            return _OBJECT_OPENVLA_TASKS, _make_instr(_OBJECT_OPENVLA_TASKS), _OBJECT_OPENVLA_PARA\n        else:\n            return _OBJECT_TRACVLA_TASKS, _make_instr(_OBJECT_TRACVLA_TASKS), _OBJECT_TRACVLA_PARA\n    elif suite == \"spatial\":\n        if arch == \"nora\":\n            return _SPATIAL_NORA_TASKS, _make_instr(_SPATIAL_NORA_TASKS), _SPATIAL_NORA_PARA\n        else:\n            return _SPATIAL_TRACVLA_TASKS, _make_instr(_SPATIAL_TRACVLA_TASKS), _SPATIAL_TRACVLA_PARA\n    raise ValueError(f\"Unknown suite: {suite}\")\n\n\n# ============================================================\n# Model loading\n# ============================================================\n\ndef load_openvla(ckpt_path):\n    from transformers import AutoModelForVision2Seq\n    log(f\"Loading OpenVLA from {ckpt_path}\")\n    t0 = time.time()\n    model = AutoModelForVision2Seq.from_pretrained(\n        ckpt_path, torch_dtype=torch.bfloat16, trust_remote_code=True\n    ).to(DEVICE).eval()\n\n    import importlib.util\n    spec = importlib.util.spec_from_file_location(\n        'processing_prismatic',\n        os.path.join(ckpt_path, 'processing_prismatic.py'))\n    mod = importlib.util.module_from_spec(spec)\n    sys.modules['processing_prismatic'] = mod\n    spec.loader.exec_module(mod)\n    processor = mod.PrismaticProcessor.from_pretrained(\n        ckpt_path, trust_remote_code=True)\n\n    # OFT norm_stats merge (needed for openvla-7b-oft-finetuned-libero-10)\n    ds_path = os.path.join(ckpt_path, \"dataset_statistics.json\")\n    if os.path.exists(ds_path) and hasattr(model, 'norm_stats'):\n        with open(ds_path, \"r\") as f:\n            ds_stats = json.load(f)\n        for k, v in ds_stats.items():\n            if k not in model.norm_stats:\n                model.norm_stats[k] = v\n                log(f\"  Merged norm_stats key: {k}\")\n\n    log(f\"  Loaded in {time.time()-t0:.1f}s\")\n    return model, processor\n\n\ndef load_tracvla(ckpt_path):\n    from transformers import AutoModelForCausalLM, AutoProcessor\n    log(f\"Loading TracVLA from {ckpt_path}\")\n    t0 = time.time()\n    model = AutoModelForCausalLM.from_pretrained(\n        ckpt_path, torch_dtype=torch.bfloat16, trust_remote_code=True,\n        attn_implementation=\"eager\"\n    ).to(DEVICE).eval()\n    processor = AutoProcessor.from_pretrained(\n        ckpt_path, trust_remote_code=True, num_crops=1)\n    log(f\"  Loaded in {time.time()-t0:.1f}s\")\n    return model, processor\n\n\ndef load_nora(ckpt_path):\n    from transformers import AutoModelForImageTextToText, AutoProcessor\n    log(f\"Loading NORA/Qwen2.5-VL from {ckpt_path}\")\n    t0 = time.time()\n    model = AutoModelForImageTextToText.from_pretrained(\n        ckpt_path, torch_dtype=torch.bfloat16, attn_implementation=\"eager\",\n        low_cpu_mem_usage=True, local_files_only=True, device_map=DEVICE\n    ).eval()\n    processor = AutoProcessor.from_pretrained(ckpt_path, local_files_only=True)\n    log(f\"  Loaded in {time.time()-t0:.1f}s\")\n    return model, processor\n\n\nLOADER = {\"openvla\": load_openvla, \"tracvla\": load_tracvla, \"nora\": load_nora}\n\n\n# ============================================================\n# Input preparation\n# ============================================================\n\ndef prepare_openvla(processor, instruction, image):\n    prompt = f\"In: What action should the robot take to {instruction}?\\nOut:\"\n    inputs = processor(prompt, image).to(DEVICE)\n    if \"pixel_values\" in inputs:\n        inputs[\"pixel_values\"] = inputs[\"pixel_values\"].to(torch.bfloat16)\n    return inputs\n\n\ndef prepare_tracvla(processor, instruction, image):\n    prompt = (f\"<|user|>\\n<|image_1|>\\n\"\n              f\"What action should the robot take to {instruction}?<|end|>\\n\"\n              f\"<|assistant|>\\n\")\n    inputs = processor(prompt, [image], return_tensors=\"pt\").to(DEVICE)\n    if \"pixel_values\" in inputs:\n        inputs[\"pixel_values\"] = inputs[\"pixel_values\"].to(torch.bfloat16)\n    return inputs\n\n\ndef prepare_nora(processor, instruction, image):\n    messages = [{'role': 'user', 'content': [\n        {'type': 'image', 'image': image},\n        {'type': 'text', 'text': instruction}\n    ]}]\n    text = processor.apply_chat_template(\n        messages, tokenize=False, add_generation_prompt=True)\n    inputs = processor(\n        text=[text], images=[image], return_tensors='pt', padding=True)\n    return {k: v.to(DEVICE) if isinstance(v, torch.Tensor) else v\n            for k, v in inputs.items()}\n\n\nPREPARE = {\"openvla\": prepare_openvla, \"tracvla\": prepare_tracvla, \"nora\": prepare_nora}\n\n\n# ============================================================\n# Action generation (for action_mse method)\n# ============================================================\n\ndef gen_action_openvla(model, processor, instruction, image, unnorm_key):\n    inputs = prepare_openvla(processor, instruction, image)\n    input_ids = inputs[\"input_ids\"]\n    if not torch.all(input_ids[:, -1] == 29871):\n        input_ids = torch.cat(\n            (input_ids,\n             torch.tensor([[29871]], device=DEVICE, dtype=input_ids.dtype)),\n            dim=1)\n        if \"attention_mask\" in inputs:\n            inputs[\"attention_mask\"] = torch.cat(\n                (inputs[\"attention_mask\"],\n                 torch.ones(1, 1, device=DEVICE,\n                            dtype=inputs[\"attention_mask\"].dtype)),\n                dim=1)\n    inputs[\"input_ids\"] = input_ids\n    with torch.no_grad():\n        gen_ids = model.generate(\n            inputs[\"input_ids\"],\n            attention_mask=inputs.get(\"attention_mask\"),\n            pixel_values=inputs.get(\"pixel_values\"),\n            max_new_tokens=7, do_sample=False)\n    token_ids = gen_ids[0, -7:].cpu().numpy()\n    disc = np.clip(model.vocab_size - token_ids - 1, 0,\n                   model.bin_centers.shape[0] - 1)\n    norm_act = model.bin_centers[disc]\n    stats = model.get_action_stats(unnorm_key)\n    mask = np.array(stats.get(\"mask\", [True] * 7))\n    high, low = np.array(stats[\"q99\"]), np.array(stats[\"q01\"])\n    action = np.where(mask, 0.5 * (norm_act + 1) * (high - low) + low,\n                      norm_act)\n    del inputs, gen_ids\n    return action.astype(np.float64), token_ids\n\n\ndef gen_action_tracvla(model, processor, instruction, image, _unnorm_key=None):\n    inputs = prepare_tracvla(processor, instruction, image)\n    with torch.no_grad():\n        gen_ids = model.generate(\n            input_ids=inputs[\"input_ids\"],\n            attention_mask=inputs.get(\"attention_mask\"),\n            pixel_values=inputs.get(\"pixel_values\"),\n            image_sizes=inputs.get(\"image_sizes\"),\n            max_new_tokens=7, do_sample=False)\n    token_ids = gen_ids[0, -7:].cpu().numpy()\n    vocab_size = model.config.vocab_size\n    bins = np.linspace(-1, 1, 256)\n    bin_centers = (bins[:-1] + bins[1:]) / 2.0\n    disc = np.clip(vocab_size - token_ids - 1, a_min=0,\n                   a_max=bin_centers.shape[0] - 1)\n    norm_act = bin_centers[disc]\n    del inputs, gen_ids\n    return norm_act.astype(np.float64), token_ids\n\n\nGEN_ACTION = {\"openvla\": gen_action_openvla, \"tracvla\": gen_action_tracvla}\n\n\n# ============================================================\n# Counterfactual instruction\n# ============================================================\n\ndef cf_instruction(task_idx, cond, instructions, paraphrases):\n    if cond == \"wrong\":\n        return instructions[(task_idx + 1) % len(instructions)]\n    elif cond == \"empty\":\n        return \"\"\n    elif cond == \"shuffled\":\n        words = instructions[task_idx].split()\n        random.Random(42 + task_idx).shuffle(words)\n        return \" \".join(words)\n    elif cond == \"paraphrased\":\n        return paraphrases[task_idx]\n    raise ValueError(f\"Unknown condition: {cond}\")\n\n\n# ============================================================\n# Counterfactual: action MSE\n# ============================================================\n\ndef run_cf_action_mse(arch, model, processor, tasks, instructions,\n                      paraphrases, data_dir, unnorm_key, n_demos, n_timesteps):\n    log(\"Counterfactual analysis (action MSE)\")\n    conditions = [\"wrong\", \"empty\", \"shuffled\", \"paraphrased\"]\n    gen_fn = GEN_ACTION[arch]\n    n_tasks = len(tasks)\n\n    all_res = {\n        \"config\": {\n            \"experiment\": f\"counterfactual_{arch}\",\n            \"conditions\": conditions,\n            \"n_tasks\": n_tasks,\n            \"n_demos_per_task\": n_demos,\n            \"n_timesteps_per_demo\": n_timesteps,\n            \"method\": \"action_mse\",\n            \"unnorm_key\": unnorm_key,\n            \"seed\": 42,\n            \"task_names\": tasks,\n        }\n    }\n\n    for cond in conditions:\n        log(f\"  Condition: {cond}\")\n        all_mses, all_tok_div = [], []\n        per_task_mses = defaultdict(list)\n        per_task_demo_mses = defaultdict(lambda: defaultdict(list))\n        per_task_correct = defaultdict(list)\n        per_task_cf = defaultdict(list)\n        sample_n = 0\n\n        for ti in range(n_tasks):\n            cf_instr = cf_instruction(ti, cond, instructions, paraphrases)\n            hdf5_path = os.path.join(data_dir, f\"{tasks[ti]}_demo.hdf5\")\n\n            with h5py.File(hdf5_path, \"r\") as hf:\n                for di in range(n_demos):\n                    n_avail = hf[f\"data/demo_{di}/actions\"].shape[0]\n                    for t in range(min(n_timesteps, n_avail)):\n                        img = Image.fromarray(\n                            hf[f\"data/demo_{di}/obs/agentview_rgb\"][t])\n\n                        c_act, c_tok = gen_fn(\n                            model, processor, instructions[ti], img, unnorm_key)\n                        f_act, f_tok = gen_fn(\n                            model, processor, cf_instr, img, unnorm_key)\n\n                        mse = float(np.mean((c_act - f_act) ** 2))\n                        tok_div = int(not np.array_equal(c_tok, f_tok))\n\n                        all_mses.append(mse)\n                        all_tok_div.append(tok_div)\n                        per_task_mses[ti].append(mse)\n                        per_task_demo_mses[ti][di].append(mse)\n                        per_task_correct[ti].append(c_act)\n                        per_task_cf[ti].append(f_act)\n\n                        sample_n += 1\n                        if sample_n % 200 == 0:\n                            torch.cuda.empty_cache()\n                            log(f\"    {sample_n}/{n_tasks * n_demos * n_timesteps}\")\n\n        mse_arr = np.array(all_mses)\n        global_d = (float(mse_arr.mean() / mse_arr.std(ddof=1))\n                    if mse_arr.std(ddof=1) > 0 else 0.0)\n\n        ca_all = np.concatenate(\n            [np.array(per_task_correct[ti]) for ti in range(n_tasks)])\n        cf_all = np.concatenate(\n            [np.array(per_task_cf[ti]) for ti in range(n_tasks)])\n        pdm = np.abs(ca_all - cf_all).mean(0).tolist()\n        pds = np.abs(ca_all - cf_all).std(0).tolist()\n\n        cond_res = {\n            \"global_metrics\": {\n                \"paired_mse\": {\n                    \"mean\": round(float(mse_arr.mean()), 6),\n                    \"std\": round(float(mse_arr.std()), 6),\n                    \"cohens_d\": round(global_d, 4),\n                },\n                \"per_dim_shift\": {\n                    \"means\": [round(v, 6) for v in pdm],\n                    \"stds\": [round(v, 6) for v in pds],\n                    \"dim_names\": [\"dx\",\"dy\",\"dz\",\"rx\",\"ry\",\"rz\",\"gripper\"],\n                },\n                \"token_divergence_rate\": round(float(np.mean(all_tok_div)), 4),\n                \"n_samples\": len(mse_arr),\n            },\n            \"per_task\": {},\n            \"cross_task_variance\": {},\n        }\n\n        per_task_ds = []\n        for ti in range(n_tasks):\n            tm = np.array(per_task_mses[ti])\n            td = (float(tm.mean() / tm.std(ddof=1))\n                  if tm.std(ddof=1) > 0 else 0.0)\n            per_task_ds.append(td)\n\n            demo_means = [float(np.mean(per_task_demo_mses[ti][di]))\n                          for di in range(n_demos)]\n            da = np.array(demo_means)\n            dd = (float(da.mean() / da.std(ddof=1))\n                  if da.std(ddof=1) > 0 else 0.0)\n\n            entry = {\n                \"cohens_d\": round(td, 4),\n                \"demo_level_cohens_d\": round(dd, 4),\n                \"n_samples\": len(tm),\n                \"mean_mse\": round(float(tm.mean()), 6),\n                \"demo_mses\": [round(v, 6) for v in demo_means],\n                \"instruction_correct\": instructions[ti],\n                \"instruction_counterfactual\": cf_instruction(\n                    ti, cond, instructions, paraphrases),\n            }\n            cond_res[\"per_task\"][tasks[ti]] = entry\n\n        cond_res[\"cross_task_variance\"] = {\n            \"cohens_d\": {\n                \"values\": [round(v, 4) for v in per_task_ds],\n                \"mean\": round(float(np.mean(per_task_ds)), 4),\n                \"std\": round(float(np.std(per_task_ds)), 4),\n                \"cv\": (round(float(np.std(per_task_ds) /\n                                   np.mean(per_task_ds)), 4)\n                       if np.mean(per_task_ds) > 0 else 0.0),\n            }\n        }\n        all_res[cond] = cond_res\n        log(f\"  {cond}: global d={global_d:.4f}  \"\n            f\"cross-task mean={np.mean(per_task_ds):.4f}  \"\n            f\"token_div={np.mean(all_tok_div):.3f}\")\n\n    ranking = sorted(\n        conditions,\n        key=lambda c: all_res[c][\"global_metrics\"][\"paired_mse\"][\"cohens_d\"],\n        reverse=True)\n    all_res[\"ranking_by_cohens_d\"] = [\n        {\"condition\": c,\n         \"cohens_d\": all_res[c][\"global_metrics\"][\"paired_mse\"][\"cohens_d\"],\n         \"paired_mse_mean\": all_res[c][\"global_metrics\"][\"paired_mse\"][\"mean\"]}\n        for c in ranking\n    ]\n    return all_res\n\n\n# ============================================================\n# Counterfactual: cosine distance\n# ============================================================\n\ndef run_cf_cosine_dist(arch, model, processor, tasks, instructions,\n                       paraphrases, data_dir, n_layers, n_demos, n_timesteps):\n    log(\"Counterfactual analysis (cosine distance)\")\n    conditions = [\"wrong\", \"empty\", \"shuffled\", \"paraphrased\"]\n    prep_fn = PREPARE[arch]\n    cf_layers = sorted(set(list(range(0, n_layers, 3)) + [n_layers - 1]))\n    n_tasks = len(tasks)\n\n    all_res = {\n        \"config\": {\n            \"experiment\": f\"counterfactual_{arch}\",\n            \"conditions\": conditions,\n            \"n_tasks\": n_tasks,\n            \"n_demos_per_task\": n_demos,\n            \"n_timesteps_per_demo\": n_timesteps,\n            \"method\": \"representation_cosine_distance\",\n            \"layers_analyzed\": cf_layers,\n            \"seed\": 42,\n            \"task_names\": tasks,\n        }\n    }\n\n    for cond in conditions:\n        log(f\"  Condition: {cond}\")\n        per_layer_dists = {l: [] for l in cf_layers}\n        per_task_dists = defaultdict(list)\n        per_task_demo_dists = defaultdict(lambda: defaultdict(list))\n        sample_n = 0\n\n        for ti in range(n_tasks):\n            cf_instr = cf_instruction(ti, cond, instructions, paraphrases)\n            hdf5_path = os.path.join(data_dir, f\"{tasks[ti]}_demo.hdf5\")\n\n            with h5py.File(hdf5_path, \"r\") as hf:\n                for di in range(n_demos):\n                    n_avail = hf[f\"data/demo_{di}/actions\"].shape[0]\n                    for t in range(min(n_timesteps, n_avail)):\n                        img = Image.fromarray(\n                            hf[f\"data/demo_{di}/obs/agentview_rgb\"][t])\n\n                        c_inputs = prep_fn(processor, instructions[ti], img)\n                        with torch.no_grad():\n                            c_out = model(**c_inputs,\n                                          output_hidden_states=True)\n\n                        f_inputs = prep_fn(processor, cf_instr, img)\n                        with torch.no_grad():\n                            f_out = model(**f_inputs,\n                                          output_hidden_states=True)\n\n                        for l in cf_layers:\n                            c_r = c_out.hidden_states[l + 1][0, -1].float()\n                            f_r = f_out.hidden_states[l + 1][0, -1].float()\n                            cos_sim = F.cosine_similarity(\n                                c_r.unsqueeze(0), f_r.unsqueeze(0)).item()\n                            per_layer_dists[l].append(1.0 - cos_sim)\n\n                        last_dist = per_layer_dists[cf_layers[-1]][-1]\n                        per_task_dists[ti].append(last_dist)\n                        per_task_demo_dists[ti][di].append(last_dist)\n\n                        sample_n += 1\n                        del c_out, f_out, c_inputs, f_inputs\n                        if sample_n % 200 == 0:\n                            torch.cuda.empty_cache()\n                            log(f\"    {sample_n}/\"\n                                f\"{n_tasks * n_demos * n_timesteps}\")\n\n        cond_res = {\n            \"global_metrics\": {\"per_layer_cosine_distance\": {}},\n            \"per_task\": {},\n            \"cross_task_variance\": {},\n        }\n\n        for l in cf_layers:\n            arr = np.array(per_layer_dists[l])\n            cond_res[\"global_metrics\"][\"per_layer_cosine_distance\"][\n                f\"L{l}\"] = {\n                \"mean\": round(float(arr.mean()), 6),\n                \"std\": round(float(arr.std()), 6),\n                \"n_samples\": len(arr),\n            }\n\n        last_l = cf_layers[-1]\n        last_arr = np.array(per_layer_dists[last_l])\n        global_d = (float(last_arr.mean() / last_arr.std(ddof=1))\n                    if last_arr.std(ddof=1) > 0 else 0.0)\n        cond_res[\"global_metrics\"][\"last_layer_summary\"] = {\n            \"layer\": last_l,\n            \"mean\": round(float(last_arr.mean()), 6),\n            \"std\": round(float(last_arr.std()), 6),\n            \"cohens_d\": round(global_d, 4),\n            \"n_samples\": len(last_arr),\n        }\n\n        per_task_ds = []\n        for ti in range(n_tasks):\n            tm = np.array(per_task_dists[ti])\n            td = (float(tm.mean() / tm.std(ddof=1))\n                  if tm.std(ddof=1) > 0 else 0.0)\n            per_task_ds.append(td)\n\n            demo_means = [float(np.mean(per_task_demo_dists[ti][di]))\n                          for di in range(n_demos)]\n            da = np.array(demo_means)\n            dd = (float(da.mean() / da.std(ddof=1))\n                  if da.std(ddof=1) > 0 else 0.0)\n\n            entry = {\n                \"cohens_d\": round(td, 4),\n                \"demo_level_cohens_d\": round(dd, 4),\n                \"n_samples\": len(tm),\n                \"mean_cosine_distance\": round(float(tm.mean()), 6),\n                \"demo_distances\": [round(v, 6) for v in demo_means],\n                \"instruction_correct\": instructions[ti],\n                \"instruction_counterfactual\": cf_instruction(\n                    ti, cond, instructions, paraphrases),\n            }\n            cond_res[\"per_task\"][tasks[ti]] = entry\n\n        cond_res[\"cross_task_variance\"] = {\n            \"cohens_d\": {\n                \"values\": [round(v, 4) for v in per_task_ds],\n                \"mean\": round(float(np.mean(per_task_ds)), 4),\n                \"std\": round(float(np.std(per_task_ds)), 4),\n                \"cv\": (round(float(np.std(per_task_ds) /\n                                   np.mean(per_task_ds)), 4)\n                       if np.mean(per_task_ds) > 0 else 0.0),\n            }\n        }\n        all_res[cond] = cond_res\n        log(f\"  {cond}: last-layer cos_dist={last_arr.mean():.4f}  \"\n            f\"cross-task d={np.mean(per_task_ds):.4f}\")\n\n    ranking = sorted(\n        conditions,\n        key=lambda c: all_res[c][\"global_metrics\"][\"last_layer_summary\"][\"mean\"],\n        reverse=True)\n    all_res[\"ranking_by_cosine_distance\"] = [\n        {\"condition\": c,\n         \"mean_cosine_distance\": all_res[c][\"global_metrics\"][\n             \"last_layer_summary\"][\"mean\"]}\n        for c in ranking\n    ]\n    return all_res\n\n\n# ============================================================\n# Method selection\n# ============================================================\n\ndef resolve_method(arch, condition, method):\n    if method != \"auto\":\n        return method\n    if arch == \"nora\":\n        return \"cosine_dist\"\n    if condition == \"untrained\":\n        return \"cosine_dist\"\n    return \"action_mse\"\n\n\n# ============================================================\n# Main\n# ============================================================\n\ndef main():\n    global DEVICE\n\n    p = argparse.ArgumentParser(\n        description=\"Counterfactual-only batch runner for VLA-SSD\")\n    p.add_argument(\"--arch\", required=True,\n                   choices=[\"openvla\", \"tracvla\", \"nora\"])\n    p.add_argument(\"--suite\", required=True,\n                   choices=[\"goal\", \"spatial\", \"object\", \"long\"])\n    p.add_argument(\"--condition\", required=True,\n                   choices=[\"trained\", \"untrained\"])\n    p.add_argument(\"--method\", default=\"auto\",\n                   choices=[\"auto\", \"action_mse\", \"cosine_dist\"])\n    p.add_argument(\"--gpu\", type=int, default=0)\n    p.add_argument(\"--n-demos\", type=int, default=10)\n    p.add_argument(\"--n-timesteps\", type=int, default=50)\n    p.add_argument(\"--results-dir\", default=None,\n                   help=\"Override output directory\")\n    p.add_argument(\"--dry-run\", action=\"store_true\",\n                   help=\"Run with 2 tasks, 1 demo, 2 timesteps\")\n    args = p.parse_args()\n\n    DEVICE = f\"cuda:{args.gpu}\"\n    key = (args.arch, args.suite, args.condition)\n\n    if key not in CKPT_MAP:\n        print(f\"ERROR: Unsupported combination: {key}\")\n        print(f\"Available: {sorted(CKPT_MAP.keys())}\")\n        sys.exit(1)\n\n    ckpt_path = CKPT_MAP[key]\n    data_dir = DATA_MAP[args.suite]\n    results_dir = args.results_dir or RESULTS_MAP[key]\n    method = resolve_method(args.arch, args.condition, args.method)\n    tasks, instructions, paraphrases = _get_task_config(args.arch, args.suite)\n    n_layers = ARCH_CFG[args.arch][\"n_layers\"]\n\n    n_demos = 1 if args.dry_run else args.n_demos\n    n_timesteps = 2 if args.dry_run else args.n_timesteps\n    if args.dry_run:\n        tasks = tasks[:2]\n        instructions = instructions[:2]\n        paraphrases = paraphrases[:2]\n\n    log(f\"Config: arch={args.arch} suite={args.suite} \"\n        f\"condition={args.condition} method={method}\")\n    log(f\"Checkpoint: {ckpt_path}\")\n    log(f\"Data: {data_dir}\")\n    log(f\"Results: {results_dir}\")\n    log(f\"Tasks: {len(tasks)}  Demos: {n_demos}  Timesteps: {n_timesteps}\")\n\n    os.makedirs(results_dir, exist_ok=True)\n\n    model, processor = LOADER[args.arch](ckpt_path)\n\n    t0 = time.time()\n    if method == \"action_mse\":\n        unnorm_key = UNNORM_MAP.get(key)\n        if unnorm_key is None:\n            print(f\"ERROR: No unnorm_key for {key}. \"\n                  f\"Use --method cosine_dist or add key to UNNORM_MAP.\")\n            sys.exit(1)\n        cf_res = run_cf_action_mse(\n            args.arch, model, processor, tasks, instructions, paraphrases,\n            data_dir, unnorm_key, n_demos, n_timesteps)\n    else:\n        cf_res = run_cf_cosine_dist(\n            args.arch, model, processor, tasks, instructions, paraphrases,\n            data_dir, n_layers, n_demos, n_timesteps)\n\n    out_path = os.path.join(results_dir, \"counterfactual_combined.json\")\n    with open(out_path, \"w\") as f:\n        json.dump(cf_res, f, indent=2)\n\n    log(f\"Saved -> {out_path}\")\n    log(f\"Total: {(time.time()-t0)/60:.1f} min\")\n\n    del model, processor\n    torch.cuda.empty_cache()\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT_EOF"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat << 'SCRIPT_EOF' > /root/autodl-tmp/vla-ssd/scripts/counterfactual_batch.py\n#!/usr/bin/env python3\n\"\"\"\nCounterfactual-only batch runner for VLA-SSD experiments.\n\nSupports openvla/tracvla/nora architectures across goal/spatial/object/long suites.\nAuto-selects method: action_mse for trained openvla/tracvla, cosine_dist for nora\nand all untrained models. Override with --method.\n\nUsage:\n  python counterfactual_batch.py --arch tracvla --suite spatial --condition untrained\n  python counterfactual_batch.py --arch openvla --suite long --condition trained\n  python counterfactual_batch.py --arch openvla --suite object --condition untrained\n  python counterfactual_batch.py --arch nora --suite goal --condition untrained\n\"\"\"\n\nimport argparse, json, os, random, sys, time\nfrom collections import defaultdict\n\nos.environ[\"HDF5_USE_FILE_LOCKING\"] = \"FALSE\"\n\nimport h5py\nimport numpy as np\nimport torch\nimport torch.nn.functional as F\nfrom PIL import Image\n\nDEVICE = \"cuda:0\"\n\ndef log(msg):\n    print(f\"[{time.strftime('%H:%M:%S')}] {msg}\", flush=True)\n\n# ============================================================\n# Architecture configs\n# ============================================================\nARCH_CFG = {\n    \"openvla\": {\"n_layers\": 32, \"n_heads\": 32, \"hidden\": 4096},\n    \"tracvla\": {\"n_layers\": 32, \"n_heads\": 32, \"hidden\": 3072},\n    \"nora\":    {\"n_layers\": 36, \"n_heads\": 16, \"hidden\": 2048},\n}\n\n# ============================================================\n# Checkpoint registry\n# ============================================================\nCKPT_MAP = {\n    (\"openvla\", \"object\", \"trained\"):   \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-object\",\n    (\"openvla\", \"object\", \"untrained\"): \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\",\n    (\"openvla\", \"long\", \"trained\"):     \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-oft-finetuned-libero-10\",\n    (\"openvla\", \"long\", \"untrained\"):   \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\",\n    (\"openvla\", \"goal\", \"trained\"):     \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-goal\",\n    (\"openvla\", \"goal\", \"untrained\"):   \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\",\n    (\"tracvla\", \"object\", \"trained\"):   \"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v/\",\n    (\"tracvla\", \"object\", \"untrained\"): \"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base/\",\n    (\"tracvla\", \"spatial\", \"trained\"):  \"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v/\",\n    (\"tracvla\", \"spatial\", \"untrained\"):\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base/\",\n    (\"tracvla\", \"goal\", \"trained\"):     \"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v/\",\n    (\"tracvla\", \"goal\", \"untrained\"):   \"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base/\",\n    (\"tracvla\", \"long\", \"trained\"):     \"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v/\",\n    (\"tracvla\", \"long\", \"untrained\"):   \"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base/\",\n    (\"nora\", \"goal\", \"trained\"):        \"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-goal/\",\n    (\"nora\", \"goal\", \"untrained\"):      \"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base/\",\n    (\"nora\", \"spatial\", \"trained\"):     \"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-spatial/\",\n    (\"nora\", \"spatial\", \"untrained\"):   \"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base/\",\n}\n\n# ============================================================\n# Data directories\n# ============================================================\nDATA_MAP = {\n    \"goal\":    \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal\",\n    \"spatial\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_spatial\",\n    \"object\":  \"/root/autodl-tmp/vla-ssd/data/libero/libero_object\",\n    \"long\":    \"/root/autodl-tmp/vla-ssd/data/libero/libero_10\",\n}\n\n# ============================================================\n# Results directories\n# ============================================================\nRESULTS_MAP = {\n    (\"openvla\", \"object\", \"trained\"):   \"/root/autodl-tmp/vla-ssd/results/libero_object/trained\",\n    (\"openvla\", \"object\", \"untrained\"): \"/root/autodl-tmp/vla-ssd/results/libero_object_untrained\",\n    (\"openvla\", \"long\", \"trained\"):     \"/root/autodl-tmp/vla-ssd/results/libero_long/trained\",\n    (\"openvla\", \"long\", \"untrained\"):   \"/root/autodl-tmp/vla-ssd/results/libero_long/untrained\",\n    (\"openvla\", \"goal\", \"trained\"):     \"/root/autodl-tmp/vla-ssd/results/libero_goal/trained\",\n    (\"openvla\", \"goal\", \"untrained\"):   \"/root/autodl-tmp/vla-ssd/results/libero_goal/untrained\",\n    (\"tracvla\", \"object\", \"trained\"):   \"/root/autodl-tmp/vla-ssd/results/tracvla_object/trained\",\n    (\"tracvla\", \"object\", \"untrained\"): \"/root/autodl-tmp/vla-ssd/results/tracvla_object/untrained\",\n    (\"tracvla\", \"spatial\", \"trained\"):  \"/root/autodl-tmp/vla-ssd/results/tracvla_spatial/trained\",\n    (\"tracvla\", \"spatial\", \"untrained\"):\"/root/autodl-tmp/vla-ssd/results/tracvla_spatial/untrained\",\n    (\"tracvla\", \"goal\", \"trained\"):     \"/root/autodl-tmp/vla-ssd/results/tracvla_goal/trained\",\n    (\"tracvla\", \"goal\", \"untrained\"):   \"/root/autodl-tmp/vla-ssd/results/tracvla_goal/untrained\",\n    (\"tracvla\", \"long\", \"trained\"):     \"/root/autodl-tmp/vla-ssd/results/tracvla_long/trained\",\n    (\"tracvla\", \"long\", \"untrained\"):   \"/root/autodl-tmp/vla-ssd/results/tracvla_long/untrained\",\n    (\"nora\", \"goal\", \"trained\"):        \"/root/autodl-tmp/vla-ssd/results/nora_goal/trained\",\n    (\"nora\", \"goal\", \"untrained\"):      \"/root/autodl-tmp/vla-ssd/results/nora_goal/untrained\",\n    (\"nora\", \"spatial\", \"trained\"):     \"/root/autodl-tmp/vla-ssd/results/nora_spatial/trained\",\n    (\"nora\", \"spatial\", \"untrained\"):   \"/root/autodl-tmp/vla-ssd/results/nora_spatial/untrained\",\n}\n\n# ============================================================\n# Unnorm keys (only for action_mse on OpenVLA)\n# ============================================================\nUNNORM_MAP = {\n    (\"openvla\", \"object\", \"trained\"):   \"libero_object\",\n    (\"openvla\", \"object\", \"untrained\"): \"bridge_orig\",\n    (\"openvla\", \"long\", \"trained\"):     \"libero_10_no_noops\",\n    (\"openvla\", \"long\", \"untrained\"):   \"bridge_orig\",\n    (\"openvla\", \"goal\", \"trained\"):     \"libero_goal\",\n    (\"openvla\", \"goal\", \"untrained\"):   \"bridge_orig\",\n}\n\n# ============================================================\n# Task configurations per (arch, suite)\n# Tasks and paraphrases must match the ordering used in the\n# original full_pipeline scripts so \"wrong\" condition is consistent.\n# ============================================================\n\n_GOAL_TASKS = [\n    \"open_the_middle_drawer_of_the_cabinet\",\n    \"open_the_top_drawer_and_put_the_bowl_inside\",\n    \"push_the_plate_to_the_front_of_the_stove\",\n    \"put_the_bowl_on_the_plate\",\n    \"put_the_bowl_on_the_stove\",\n    \"put_the_bowl_on_top_of_the_cabinet\",\n    \"put_the_cream_cheese_in_the_bowl\",\n    \"put_the_wine_bottle_on_the_rack\",\n    \"put_the_wine_bottle_on_top_of_the_cabinet\",\n    \"turn_on_the_stove\",\n]\n_GOAL_PARA = [\n    \"open the cabinet's middle drawer\",\n    \"open the top drawer and place the bowl in it\",\n    \"slide the plate to the stove's front\",\n    \"place the bowl onto the plate\",\n    \"place the bowl onto the stove\",\n    \"place the bowl on the cabinet top\",\n    \"put cream cheese into the bowl\",\n    \"place the wine bottle on the rack\",\n    \"place the wine bottle on the cabinet top\",\n    \"switch on the stove\",\n]\n\n_LONG_TASKS = [\n    \"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\",\n    \"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\",\n    \"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\",\n    \"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\",\n    \"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\",\n    \"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\",\n    \"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\",\n    \"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\",\n    \"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\",\n    \"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\",\n]\n_LONG_INSTR = [\n    \"turn on the stove and put the moka pot on it\",\n    \"put the black bowl in the bottom drawer of the cabinet and close it\",\n    \"put the yellow and white mug in the microwave and close it\",\n    \"put both moka pots on the stove\",\n    \"put both the alphabet soup and the cream cheese box in the basket\",\n    \"put both the alphabet soup and the tomato sauce in the basket\",\n    \"put both the cream cheese box and the butter in the basket\",\n    \"put the white mug on the left plate and put the yellow and white mug on the right plate\",\n    \"put the white mug on the plate and put the chocolate pudding to the right of the plate\",\n    \"pick up the book and place it in the back compartment of the caddy\",\n]\n_LONG_PARA = [\n    \"switch on the stove and place the moka pot on it\",\n    \"place the black bowl in the bottom drawer of the cabinet and shut it\",\n    \"place the yellow and white mug in the microwave and shut it\",\n    \"put both of the moka pots on the stove\",\n    \"place the alphabet soup and cream cheese box into the basket\",\n    \"place the alphabet soup and tomato sauce into the basket\",\n    \"place the cream cheese box and butter into the basket\",\n    \"place the white mug on the left plate and the yellow white mug on the right plate\",\n    \"place the white mug on the plate and the chocolate pudding to the right of the plate\",\n    \"grab the book and put it in the back section of the caddy\",\n]\n\n_OBJECT_OPENVLA_TASKS = [\n    \"pick_up_the_alphabet_soup_and_place_it_in_the_basket\",\n    \"pick_up_the_cream_cheese_and_place_it_in_the_basket\",\n    \"pick_up_the_salad_dressing_and_place_it_in_the_basket\",\n    \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\",\n    \"pick_up_the_ketchup_and_place_it_in_the_basket\",\n    \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\",\n    \"pick_up_the_butter_and_place_it_in_the_basket\",\n    \"pick_up_the_milk_and_place_it_in_the_basket\",\n    \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\",\n    \"pick_up_the_orange_juice_and_place_it_in_the_basket\",\n]\n_OBJECT_OPENVLA_PARA = [\n    \"grab the alphabet soup and put it into the basket\",\n    \"grab the cream cheese and put it into the basket\",\n    \"grab the salad dressing and put it into the basket\",\n    \"grab the bbq sauce and put it into the basket\",\n    \"grab the ketchup and put it into the basket\",\n    \"grab the tomato sauce and put it into the basket\",\n    \"grab the butter and put it into the basket\",\n    \"grab the milk and put it into the basket\",\n    \"grab the chocolate pudding and put it into the basket\",\n    \"grab the orange juice and put it into the basket\",\n]\n\n_OBJECT_TRACVLA_TASKS = [\n    \"pick_up_the_alphabet_soup_and_place_it_in_the_basket\",\n    \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\",\n    \"pick_up_the_butter_and_place_it_in_the_basket\",\n    \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\",\n    \"pick_up_the_cream_cheese_and_place_it_in_the_basket\",\n    \"pick_up_the_ketchup_and_place_it_in_the_basket\",\n    \"pick_up_the_milk_and_place_it_in_the_basket\",\n    \"pick_up_the_orange_juice_and_place_it_in_the_basket\",\n    \"pick_up_the_salad_dressing_and_place_it_in_the_basket\",\n    \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\",\n]\n_OBJECT_TRACVLA_PARA = [\n    \"grab the alphabet soup and put it into the basket\",\n    \"grab the bbq sauce and put it into the basket\",\n    \"grab the butter and put it into the basket\",\n    \"grab the chocolate pudding and put it into the basket\",\n    \"grab the cream cheese and put it into the basket\",\n    \"grab the ketchup and put it into the basket\",\n    \"grab the milk and put it into the basket\",\n    \"grab the orange juice and put it into the basket\",\n    \"grab the salad dressing and put it into the basket\",\n    \"grab the tomato sauce and put it into the basket\",\n]\n\n_SPATIAL_TRACVLA_TASKS = [\n    \"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\",\n    \"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\",\n    \"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\",\n    \"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\",\n    \"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\",\n    \"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\",\n    \"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\",\n    \"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\",\n    \"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\",\n    \"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\",\n]\n_SPATIAL_TRACVLA_PARA = [\n    \"grab the black bowl between the plate and ramekin and put it on the plate\",\n    \"grab the black bowl on the ramekin and put it on the plate\",\n    \"grab the black bowl on the cookie box and put it on the plate\",\n    \"grab the black bowl in the top drawer of the wooden cabinet and put it on the plate\",\n    \"grab the black bowl from the center of the table and put it on the plate\",\n    \"grab the black bowl next to the cookie box and put it on the plate\",\n    \"grab the black bowl on the stove and put it on the plate\",\n    \"grab the black bowl on the wooden cabinet and put it on the plate\",\n    \"grab the black bowl next to the plate and put it on the plate\",\n    \"grab the black bowl next to the ramekin and put it on the plate\",\n]\n\n_SPATIAL_NORA_TASKS = [\n    \"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\",\n    \"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\",\n    \"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\",\n    \"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\",\n    \"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\",\n    \"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\",\n    \"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\",\n    \"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\",\n    \"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\",\n    \"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\",\n]\n_SPATIAL_NORA_PARA = [\n    \"grab the black bowl between the plate and ramekin and put it on the plate\",\n    \"grab the black bowl from the center of the table and put it on the plate\",\n    \"grab the black bowl in the top drawer of the wooden cabinet and put it on the plate\",\n    \"grab the black bowl next to the cookie box and put it on the plate\",\n    \"grab the black bowl next to the plate and put it on the plate\",\n    \"grab the black bowl next to the ramekin and put it on the plate\",\n    \"grab the black bowl on the cookie box and put it on the plate\",\n    \"grab the black bowl on the ramekin and put it on the plate\",\n    \"grab the black bowl on the stove and put it on the plate\",\n    \"grab the black bowl on the wooden cabinet and put it on the plate\",\n]\n\n\ndef _make_instr(tasks):\n    return [t.replace(\"_\", \" \") for t in tasks]\n\n\ndef _get_task_config(arch, suite):\n    if suite == \"goal\":\n        return _GOAL_TASKS, _make_instr(_GOAL_TASKS), _GOAL_PARA\n    elif suite == \"long\":\n        return _LONG_TASKS, _LONG_INSTR, _LONG_PARA\n    elif suite == \"object\":\n        if arch == \"openvla\":\n            return _OBJECT_OPENVLA_TASKS, _make_instr(_OBJECT_OPENVLA_TASKS), _OBJECT_OPENVLA_PARA\n        else:\n            return _OBJECT_TRACVLA_TASKS, _make_instr(_OBJECT_TRACVLA_TASKS), _OBJECT_TRACVLA_PARA\n    elif suite == \"spatial\":\n        if arch == \"nora\":\n            return _SPATIAL_NORA_TASKS, _make_instr(_SPATIAL_NORA_TASKS), _SPATIAL_NORA_PARA\n        else:\n            return _SPATIAL_TRACVLA_TASKS, _make_instr(_SPATIAL_TRACVLA_TASKS), _SPATIAL_TRACVLA_PARA\n    raise ValueError(f\"Unknown suite: {suite}\")\n\n\n# ============================================================\n# Model loading\n# ============================================================\n\ndef load_openvla(ckpt_path):\n    from transformers import AutoModelForVision2Seq\n    log(f\"Loading OpenVLA from {ckpt_path}\")\n    t0 = time.time()\n    model = AutoModelForVision2Seq.from_pretrained(\n        ckpt_path, torch_dtype=torch.bfloat16, trust_remote_code=True\n    ).to(DEVICE).eval()\n\n    import importlib.util\n    spec = importlib.util.spec_from_file_location(\n        'processing_prismatic',\n        os.path.join(ckpt_path, 'processing_prismatic.py'))\n    mod = importlib.util.module_from_spec(spec)\n    sys.modules['processing_prismatic'] = mod\n    spec.loader.exec_module(mod)\n    processor = mod.PrismaticProcessor.from_pretrained(\n        ckpt_path, trust_remote_code=True)\n\n    # OFT norm_stats merge (needed for openvla-7b-oft-finetuned-libero-10)\n    ds_path = os.path.join(ckpt_path, \"dataset_statistics.json\")\n    if os.path.exists(ds_path) and hasattr(model, 'norm_stats'):\n        with open(ds_path, \"r\") as f:\n            ds_stats = json.load(f)\n        for k, v in ds_stats.items():\n            if k not in model.norm_stats:\n                model.norm_stats[k] = v\n                log(f\"  Merged norm_stats key: {k}\")\n\n    log(f\"  Loaded in {time.time()-t0:.1f}s\")\n    return model, processor\n\n\ndef load_tracvla(ckpt_path):\n    from transformers import AutoModelForCausalLM, AutoProcessor\n    log(f\"Loading TracVLA from {ckpt_path}\")\n    t0 = time.time()\n    model = AutoModelForCausalLM.from_pretrained(\n        ckpt_path, torch_dtype=torch.bfloat16, trust_remote_code=True,\n        attn_implementation=\"eager\"\n    ).to(DEVICE).eval()\n    processor = AutoProcessor.from_pretrained(\n        ckpt_path, trust_remote_code=True, num_crops=1)\n    log(f\"  Loaded in {time.time()-t0:.1f}s\")\n    return model, processor\n\n\ndef load_nora(ckpt_path):\n    from transformers import AutoModelForImageTextToText, AutoProcessor\n    log(f\"Loading NORA/Qwen2.5-VL from {ckpt_path}\")\n    t0 = time.time()\n    model = AutoModelForImageTextToText.from_pretrained(\n        ckpt_path, torch_dtype=torch.bfloat16, attn_implementation=\"eager\",\n        low_cpu_mem_usage=True, local_files_only=True, device_map=DEVICE\n    ).eval()\n    processor = AutoProcessor.from_pretrained(ckpt_path, local_files_only=True)\n    log(f\"  Loaded in {time.time()-t0:.1f}s\")\n    return model, processor\n\n\nLOADER = {\"openvla\": load_openvla, \"tracvla\": load_tracvla, \"nora\": load_nora}\n\n\n# ============================================================\n# Input preparation\n# ============================================================\n\ndef prepare_openvla(processor, instruction, image):\n    prompt = f\"In: What action should the robot take to {instruction}?\\nOut:\"\n    inputs = processor(prompt, image).to(DEVICE)\n    if \"pixel_values\" in inputs:\n        inputs[\"pixel_values\"] = inputs[\"pixel_values\"].to(torch.bfloat16)\n    return inputs\n\n\ndef prepare_tracvla(processor, instruction, image):\n    prompt = (f\"<|user|>\\n<|image_1|>\\n\"\n              f\"What action should the robot take to {instruction}?<|end|>\\n\"\n              f\"<|assistant|>\\n\")\n    inputs = processor(prompt, [image], return_tensors=\"pt\").to(DEVICE)\n    if \"pixel_values\" in inputs:\n        inputs[\"pixel_values\"] = inputs[\"pixel_values\"].to(torch.bfloat16)\n    return inputs\n\n\ndef prepare_nora(processor, instruction, image):\n    messages = [{'role': 'user', 'content': [\n        {'type': 'image', 'image': image},\n        {'type': 'text', 'text': instruction}\n    ]}]\n    text = processor.apply_chat_template(\n        messages, tokenize=False, add_generation_prompt=True)\n    inputs = processor(\n        text=[text], images=[image], return_tensors='pt', padding=True)\n    return {k: v.to(DEVICE) if isinstance(v, torch.Tensor) else v\n            for k, v in inputs.items()}\n\n\nPREPARE = {\"openvla\": prepare_openvla, \"tracvla\": prepare_tracvla, \"nora\": prepare_nora}\n\n\n# ============================================================\n# Action generation (for action_mse method)\n# ============================================================\n\ndef gen_action_openvla(model, processor, instruction, image, unnorm_key):\n    inputs = prepare_openvla(processor, instruction, image)\n    input_ids = inputs[\"input_ids\"]\n    if not torch.all(input_ids[:, -1] == 29871):\n        input_ids = torch.cat(\n            (input_ids,\n             torch.tensor([[29871]], device=DEVICE, dtype=input_ids.dtype)),\n            dim=1)\n        if \"attention_mask\" in inputs:\n            inputs[\"attention_mask\"] = torch.cat(\n                (inputs[\"attention_mask\"],\n                 torch.ones(1, 1, device=DEVICE,\n                            dtype=inputs[\"attention_mask\"].dtype)),\n                dim=1)\n    inputs[\"input_ids\"] = input_ids\n    with torch.no_grad():\n        gen_ids = model.generate(\n            inputs[\"input_ids\"],\n            attention_mask=inputs.get(\"attention_mask\"),\n            pixel_values=inputs.get(\"pixel_values\"),\n            max_new_tokens=7, do_sample=False)\n    token_ids = gen_ids[0, -7:].cpu().numpy()\n    disc = np.clip(model.vocab_size - token_ids - 1, 0,\n                   model.bin_centers.shape[0] - 1)\n    norm_act = model.bin_centers[disc]\n    stats = model.get_action_stats(unnorm_key)\n    mask = np.array(stats.get(\"mask\", [True] * 7))\n    high, low = np.array(stats[\"q99\"]), np.array(stats[\"q01\"])\n    action = np.where(mask, 0.5 * (norm_act + 1) * (high - low) + low,\n                      norm_act)\n    del inputs, gen_ids\n    return action.astype(np.float64), token_ids\n\n\ndef gen_action_tracvla(model, processor, instruction, image, _unnorm_key=None):\n    inputs = prepare_tracvla(processor, instruction, image)\n    with torch.no_grad():\n        gen_ids = model.generate(\n            input_ids=inputs[\"input_ids\"],\n            attention_mask=inputs.get(\"attention_mask\"),\n            pixel_values=inputs.get(\"pixel_values\"),\n            image_sizes=inputs.get(\"image_sizes\"),\n            max_new_tokens=7, do_sample=False)\n    token_ids = gen_ids[0, -7:].cpu().numpy()\n    vocab_size = model.config.vocab_size\n    bins = np.linspace(-1, 1, 256)\n    bin_centers = (bins[:-1] + bins[1:]) / 2.0\n    disc = np.clip(vocab_size - token_ids - 1, a_min=0,\n                   a_max=bin_centers.shape[0] - 1)\n    norm_act = bin_centers[disc]\n    del inputs, gen_ids\n    return norm_act.astype(np.float64), token_ids\n\n\nGEN_ACTION = {\"openvla\": gen_action_openvla, \"tracvla\": gen_action_tracvla}\n\n\n# ============================================================\n# Counterfactual instruction\n# ============================================================\n\ndef cf_instruction(task_idx, cond, instructions, paraphrases):\n    if cond == \"wrong\":\n        return instructions[(task_idx + 1) % len(instructions)]\n    elif cond == \"empty\":\n        return \"\"\n    elif cond == \"shuffled\":\n        words = instructions[task_idx].split()\n        random.Random(42 + task_idx).shuffle(words)\n        return \" \".join(words)\n    elif cond == \"paraphrased\":\n        return paraphrases[task_idx]\n    raise ValueError(f\"Unknown condition: {cond}\")\n\n\n# ============================================================\n# Counterfactual: action MSE\n# ============================================================\n\ndef run_cf_action_mse(arch, model, processor, tasks, instructions,\n                      paraphrases, data_dir, unnorm_key, n_demos, n_timesteps):\n    log(\"Counterfactual analysis (action MSE)\")\n    conditions = [\"wrong\", \"empty\", \"shuffled\", \"paraphrased\"]\n    gen_fn = GEN_ACTION[arch]\n    n_tasks = len(tasks)\n\n    all_res = {\n        \"config\": {\n            \"experiment\": f\"counterfactual_{arch}\",\n            \"conditions\": conditions,\n            \"n_tasks\": n_tasks,\n            \"n_demos_per_task\": n_demos,\n            \"n_timesteps_per_demo\": n_timesteps,\n            \"method\": \"action_mse\",\n            \"unnorm_key\": unnorm_key,\n            \"seed\": 42,\n            \"task_names\": tasks,\n        }\n    }\n\n    for cond in conditions:\n        log(f\"  Condition: {cond}\")\n        all_mses, all_tok_div = [], []\n        per_task_mses = defaultdict(list)\n        per_task_demo_mses = defaultdict(lambda: defaultdict(list))\n        per_task_correct = defaultdict(list)\n        per_task_cf = defaultdict(list)\n        sample_n = 0\n\n        for ti in range(n_tasks):\n            cf_instr = cf_instruction(ti, cond, instructions, paraphrases)\n            hdf5_path = os.path.join(data_dir, f\"{tasks[ti]}_demo.hdf5\")\n\n            with h5py.File(hdf5_path, \"r\") as hf:\n                for di in range(n_demos):\n                    n_avail = hf[f\"data/demo_{di}/actions\"].shape[0]\n                    for t in range(min(n_timesteps, n_avail)):\n                        img = Image.fromarray(\n                            hf[f\"data/demo_{di}/obs/agentview_rgb\"][t])\n\n                        c_act, c_tok = gen_fn(\n                            model, processor, instructions[ti], img, unnorm_key)\n                        f_act, f_tok = gen_fn(\n                            model, processor, cf_instr, img, unnorm_key)\n\n                        mse = float(np.mean((c_act - f_act) ** 2))\n                        tok_div = int(not np.array_equal(c_tok, f_tok))\n\n                        all_mses.append(mse)\n                        all_tok_div.append(tok_div)\n                        per_task_mses[ti].append(mse)\n                        per_task_demo_mses[ti][di].append(mse)\n                        per_task_correct[ti].append(c_act)\n                        per_task_cf[ti].append(f_act)\n\n                        sample_n += 1\n                        if sample_n % 200 == 0:\n                            torch.cuda.empty_cache()\n                            log(f\"    {sample_n}/{n_tasks * n_demos * n_timesteps}\")\n\n        mse_arr = np.array(all_mses)\n        global_d = (float(mse_arr.mean() / mse_arr.std(ddof=1))\n                    if mse_arr.std(ddof=1) > 0 else 0.0)\n\n        ca_all = np.concatenate(\n            [np.array(per_task_correct[ti]) for ti in range(n_tasks)])\n        cf_all = np.concatenate(\n            [np.array(per_task_cf[ti]) for ti in range(n_tasks)])\n        pdm = np.abs(ca_all - cf_all).mean(0).tolist()\n        pds = np.abs(ca_all - cf_all).std(0).tolist()\n\n        cond_res = {\n            \"global_metrics\": {\n                \"paired_mse\": {\n                    \"mean\": round(float(mse_arr.mean()), 6),\n                    \"std\": round(float(mse_arr.std()), 6),\n                    \"cohens_d\": round(global_d, 4),\n                },\n                \"per_dim_shift\": {\n                    \"means\": [round(v, 6) for v in pdm],\n                    \"stds\": [round(v, 6) for v in pds],\n                    \"dim_names\": [\"dx\",\"dy\",\"dz\",\"rx\",\"ry\",\"rz\",\"gripper\"],\n                },\n                \"token_divergence_rate\": round(float(np.mean(all_tok_div)), 4),\n                \"n_samples\": len(mse_arr),\n            },\n            \"per_task\": {},\n            \"cross_task_variance\": {},\n        }\n\n        per_task_ds = []\n        for ti in range(n_tasks):\n            tm = np.array(per_task_mses[ti])\n            td = (float(tm.mean() / tm.std(ddof=1))\n                  if tm.std(ddof=1) > 0 else 0.0)\n            per_task_ds.append(td)\n\n            demo_means = [float(np.mean(per_task_demo_mses[ti][di]))\n                          for di in range(n_demos)]\n            da = np.array(demo_means)\n            dd = (float(da.mean() / da.std(ddof=1))\n                  if da.std(ddof=1) > 0 else 0.0)\n\n            entry = {\n                \"cohens_d\": round(td, 4),\n                \"demo_level_cohens_d\": round(dd, 4),\n                \"n_samples\": len(tm),\n                \"mean_mse\": round(float(tm.mean()), 6),\n                \"demo_mses\": [round(v, 6) for v in demo_means],\n                \"instruction_correct\": instructions[ti],\n                \"instruction_counterfactual\": cf_instruction(\n                    ti, cond, instructions, paraphrases),\n            }\n            cond_res[\"per_task\"][tasks[ti]] = entry\n\n        cond_res[\"cross_task_variance\"] = {\n            \"cohens_d\": {\n                \"values\": [round(v, 4) for v in per_task_ds],\n                \"mean\": round(float(np.mean(per_task_ds)), 4),\n                \"std\": round(float(np.std(per_task_ds)), 4),\n                \"cv\": (round(float(np.std(per_task_ds) /\n                                   np.mean(per_task_ds)), 4)\n                       if np.mean(per_task_ds) > 0 else 0.0),\n            }\n        }\n        all_res[cond] = cond_res\n        log(f\"  {cond}: global d={global_d:.4f}  \"\n            f\"cross-task mean={np.mean(per_task_ds):.4f}  \"\n            f\"token_div={np.mean(all_tok_div):.3f}\")\n\n    ranking = sorted(\n        conditions,\n        key=lambda c: all_res[c][\"global_metrics\"][\"paired_mse\"][\"cohens_d\"],\n        reverse=True)\n    all_res[\"ranking_by_cohens_d\"] = [\n        {\"condition\": c,\n         \"cohens_d\": all_res[c][\"global_metrics\"][\"paired_mse\"][\"cohens_d\"],\n         \"paired_mse_mean\": all_res[c][\"global_metrics\"][\"paired_mse\"][\"mean\"]}\n        for c in ranking\n    ]\n    return all_res\n\n\n# ============================================================\n# Counterfactual: cosine distance\n# ============================================================\n\ndef run_cf_cosine_dist(arch, model, processor, tasks, instructions,\n                       paraphrases, data_dir, n_layers, n_demos, n_timesteps):\n    log(\"Counterfactual analysis (cosine distance)\")\n    conditions = [\"wrong\", \"empty\", \"shuffled\", \"paraphrased\"]\n    prep_fn = PREPARE[arch]\n    cf_layers = sorted(set(list(range(0, n_layers, 3)) + [n_layers - 1]))\n    n_tasks = len(tasks)\n\n    all_res = {\n        \"config\": {\n            \"experiment\": f\"counterfactual_{arch}\",\n            \"conditions\": conditions,\n            \"n_tasks\": n_tasks,\n            \"n_demos_per_task\": n_demos,\n            \"n_timesteps_per_demo\": n_timesteps,\n            \"method\": \"representation_cosine_distance\",\n            \"layers_analyzed\": cf_layers,\n            \"seed\": 42,\n            \"task_names\": tasks,\n        }\n    }\n\n    for cond in conditions:\n        log(f\"  Condition: {cond}\")\n        per_layer_dists = {l: [] for l in cf_layers}\n        per_task_dists = defaultdict(list)\n        per_task_demo_dists = defaultdict(lambda: defaultdict(list))\n        sample_n = 0\n\n        for ti in range(n_tasks):\n            cf_instr = cf_instruction(ti, cond, instructions, paraphrases)\n            hdf5_path = os.path.join(data_dir, f\"{tasks[ti]}_demo.hdf5\")\n\n            with h5py.File(hdf5_path, \"r\") as hf:\n                for di in range(n_demos):\n                    n_avail = hf[f\"data/demo_{di}/actions\"].shape[0]\n                    for t in range(min(n_timesteps, n_avail)):\n                        img = Image.fromarray(\n                            hf[f\"data/demo_{di}/obs/agentview_rgb\"][t])\n\n                        c_inputs = prep_fn(processor, instructions[ti], img)\n                        with torch.no_grad():\n                            c_out = model(**c_inputs,\n                                          output_hidden_states=True)\n\n                        f_inputs = prep_fn(processor, cf_instr, img)\n                        with torch.no_grad():\n                            f_out = model(**f_inputs,\n                                          output_hidden_states=True)\n\n                        for l in cf_layers:\n                            c_r = c_out.hidden_states[l + 1][0, -1].float()\n                            f_r = f_out.hidden_states[l + 1][0, -1].float()\n                            cos_sim = F.cosine_similarity(\n                                c_r.unsqueeze(0), f_r.unsqueeze(0)).item()\n                            per_layer_dists[l].append(1.0 - cos_sim)\n\n                        last_dist = per_layer_dists[cf_layers[-1]][-1]\n                        per_task_dists[ti].append(last_dist)\n                        per_task_demo_dists[ti][di].append(last_dist)\n\n                        sample_n += 1\n                        del c_out, f_out, c_inputs, f_inputs\n                        if sample_n % 200 == 0:\n                            torch.cuda.empty_cache()\n                            log(f\"    {sample_n}/\"\n                                f\"{n_tasks * n_demos * n_timesteps}\")\n\n        cond_res = {\n            \"global_metrics\": {\"per_layer_cosine_distance\": {}},\n            \"per_task\": {},\n            \"cross_task_variance\": {},\n        }\n\n        for l in cf_layers:\n            arr = np.array(per_layer_dists[l])\n            cond_res[\"global_metrics\"][\"per_layer_cosine_distance\"][\n                f\"L{l}\"] = {\n                \"mean\": round(float(arr.mean()), 6),\n                \"std\": round(float(arr.std()), 6),\n                \"n_samples\": len(arr),\n            }\n\n        last_l = cf_layers[-1]\n        last_arr = np.array(per_layer_dists[last_l])\n        global_d = (float(last_arr.mean() / last_arr.std(ddof=1))\n                    if last_arr.std(ddof=1) > 0 else 0.0)\n        cond_res[\"global_metrics\"][\"last_layer_summary\"] = {\n            \"layer\": last_l,\n            \"mean\": round(float(last_arr.mean()), 6),\n            \"std\": round(float(last_arr.std()), 6),\n            \"cohens_d\": round(global_d, 4),\n            \"n_samples\": len(last_arr),\n        }\n\n        per_task_ds = []\n        for ti in range(n_tasks):\n            tm = np.array(per_task_dists[ti])\n            td = (float(tm.mean() / tm.std(ddof=1))\n                  if tm.std(ddof=1) > 0 else 0.0)\n            per_task_ds.append(td)\n\n            demo_means = [float(np.mean(per_task_demo_dists[ti][di]))\n                          for di in range(n_demos)]\n            da = np.array(demo_means)\n            dd = (float(da.mean() / da.std(ddof=1))\n                  if da.std(ddof=1) > 0 else 0.0)\n\n            entry = {\n                \"cohens_d\": round(td, 4),\n                \"demo_level_cohens_d\": round(dd, 4),\n                \"n_samples\": len(tm),\n                \"mean_cosine_distance\": round(float(tm.mean()), 6),\n                \"demo_distances\": [round(v, 6) for v in demo_means],\n                \"instruction_correct\": instructions[ti],\n                \"instruction_counterfactual\": cf_instruction(\n                    ti, cond, instructions, paraphrases),\n            }\n            cond_res[\"per_task\"][tasks[ti]] = entry\n\n        cond_res[\"cross_task_variance\"] = {\n            \"cohens_d\": {\n                \"values\": [round(v, 4) for v in per_task_ds],\n                \"mean\": round(float(np.mean(per_task_ds)), 4),\n                \"std\": round(float(np.std(per_task_ds)), 4),\n                \"cv\": (round(float(np.std(per_task_ds) /\n                                   np.mean(per_task_ds)), 4)\n                       if np.mean(per_task_ds) > 0 else 0.0),\n            }\n        }\n        all_res[cond] = cond_res\n        log(f\"  {cond}: last-layer cos_dist={last_arr.mean():.4f}  \"\n            f\"cross-task d={np.mean(per_task_ds):.4f}\")\n\n    ranking = sorted(\n        conditions,\n        key=lambda c: all_res[c][\"global_metrics\"][\"last_layer_summary\"][\"mean\"],\n        reverse=True)\n    all_res[\"ranking_by_cosine_distance\"] = [\n        {\"condition\": c,\n         \"mean_cosine_distance\": all_res[c][\"global_metrics\"][\n             \"last_layer_summary\"][\"mean\"]}\n        for c in ranking\n    ]\n    return all_res\n\n\n# ============================================================\n# Method selection\n# ============================================================\n\ndef resolve_method(arch, condition, method):\n    if method != \"auto\":\n        return method\n    if arch == \"nora\":\n        return \"cosine_dist\"\n    if condition == \"untrained\":\n        return \"cosine_dist\"\n    return \"action_mse\"\n\n\n# ============================================================\n# Main\n# ============================================================\n\ndef main():\n    global DEVICE\n\n    p = argparse.ArgumentParser(\n        description=\"Counterfactual-only batch runner for VLA-SSD\")\n    p.add_argument(\"--arch\", required=True,\n                   choices=[\"openvla\", \"tracvla\", \"nora\"])\n    p.add_argument(\"--suite\", required=True,\n                   choices=[\"goal\", \"spatial\", \"object\", \"long\"])\n    p.add_argument(\"--condition\", required=True,\n                   choices=[\"trained\", \"untrained\"])\n    p.add_argument(\"--method\", default=\"auto\",\n                   choices=[\"auto\", \"action_mse\", \"cosine_dist\"])\n    p.add_argument(\"--gpu\", type=int, default=0)\n    p.add_argument(\"--n-demos\", type=int, default=10)\n    p.add_argument(\"--n-timesteps\", type=int, default=50)\n    p.add_argument(\"--results-dir\", default=None,\n                   help=\"Override output directory\")\n    p.add_argument(\"--dry-run\", action=\"store_true\",\n                   help=\"Run with 2 tasks, 1 demo, 2 timesteps\")\n    args = p.parse_args()\n\n    DEVICE = f\"cuda:{args.gpu}\"\n    key = (args.arch, args.suite, args.condition)\n\n    if key not in CKPT_MAP:\n        print(f\"ERROR: Unsupported combination: {key}\")\n        print(f\"Available: {sorted(CKPT_MAP.keys())}\")\n        sys.exit(1)\n\n    ckpt_path = CKPT_MAP[key]\n    data_dir = DATA_MAP[args.suite]\n    results_dir = args.results_dir or RESULTS_MAP[key]\n    method = resolve_method(args.arch, args.condition, args.method)\n    tasks, instructions, paraphrases = _get_task_config(args.arch, args.suite)\n    n_layers = ARCH_CFG[args.arch][\"n_layers\"]\n\n    n_demos = 1 if args.dry_run else args.n_demos\n    n_timesteps = 2 if args.dry_run else args.n_timesteps\n    if args.dry_run:\n        tasks = tasks[:2]\n        instructions = instructions[:2]\n        paraphrases = paraphrases[:2]\n\n    log(f\"Config: arch={args.arch} suite={args.suite} \"\n        f\"condition={args.condition} method={method}\")\n    log(f\"Checkpoint: {ckpt_path}\")\n    log(f\"Data: {data_dir}\")\n    log(f\"Results: {results_dir}\")\n    log(f\"Tasks: {len(tasks)}  Demos: {n_demos}  Timesteps: {n_timesteps}\")\n\n    os.makedirs(results_dir, exist_ok=True)\n\n    model, processor = LOADER[args.arch](ckpt_path)\n\n    t0 = time.time()\n    if method == \"action_mse\":\n        unnorm_key = UNNORM_MAP.get(key)\n        if unnorm_key is None:\n            print(f\"ERROR: No unnorm_key for {key}. \"\n                  f\"Use --method cosine_dist or add key to UNNORM_MAP.\")\n            sys.exit(1)\n        cf_res = run_cf_action_mse(\n            args.arch, model, processor, tasks, instructions, paraphrases,\n            data_dir, unnorm_key, n_demos, n_timesteps)\n    else:\n        cf_res = run_cf_cosine_dist(\n            args.arch, model, processor, tasks, instructions, paraphrases,\n            data_dir, n_layers, n_demos, n_timesteps)\n\n    out_path = os.path.join(results_dir, \"counterfactual_combined.json\")\n    with open(out_path, \"w\") as f:\n        json.dump(cf_res, f, indent=2)\n\n    log(f\"Saved -> {out_path}\")\n    log(f\"Total: {(time.time()-t0)/60:.1f} min\")\n\n    del model, processor\n    torch.cuda.empty_cache()\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT_EOF"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-21T16:54:02.854746+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.94}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-21T16:54:02.854906+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19183",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /root/autodl-tmp/vla-ssd/scripts/counterfactual_batch.py --help"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19183",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /root/autodl-tmp/vla-ssd/scripts/counterfactual_batch.py --help"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-21T16:54:02.855071+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"usage: counterfactual_batch.py [-h] --arch {openvla,tracvla,nora} --suite\\n                               {goal,spatial,object,long} --condition\\n                               {trained,untrained}\\n                               [--method {auto,action_mse,cosine_dist}]\\n                               [--gpu GPU] [--n-demos N_DEMOS]\\n                               [--n-timesteps N_TIMESTEPS]\\n                               [--results-dir RESULTS_DIR] [--dry-run]\\n\\nCounterfactual-only batch runner for VLA-SSD\\n\\noptions:\\n  -h, --help            show this help message and exit\\n  --arch {openvla,tracvla,nora}\\n  --suite {goal,spatial,object,long}\\n  --condition {trained,untrained}\\n  --method {auto,action_mse,cosine_dist}\\n  --gpu GPU\\n  --n-demos N_DEMOS\\n  --n-timesteps N_TIMESTEPS\\n  --results-dir RESULTS_DIR\\n                        Override output directory\\n  --dry-run             Run with 2 tasks, 1 demo, 2 timesteps\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.73}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-21T16:54:02.855224+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19183",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -c \"\nimport sys; sys.argv = ['test']\nexec(open('/root/autodl-tmp/vla-ssd/scripts/counterfactual_batch.py').read().split('def main():')[0])\n\ncombos = [\n    ('tracvla', 'spatial', 'untrained'),\n    ('tracvla', 'object', 'untrained'),\n    ('openvla', 'object', 'untrained'),\n    ('openvla', 'long', 'trained'),\n    ('nora', 'goal', 'untrained'),\n]\nfor arch, suite, cond in combos:\n    key = (arch, suite, cond)\n    method = resolve_method(arch, cond, 'auto')\n    tasks, instr, para = _get_task_config(arch, suite)\n    print(f'{key} -> method={method}, ckpt={CKPT_MAP[key].split(\\\"/\\\")[-1]}, '\n          f'results={RESULTS_MAP[key].split(\\\"results/\\\")[-1]}, '\n          f'n_tasks={len(tasks)}, n_layers={ARCH_CFG[arch][\\\"n_layers\\\"]}')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19183",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -c \"\nimport sys; sys.argv = ['test']\nexec(open('/root/autodl-tmp/vla-ssd/scripts/counterfactual_batch.py').read().split('def main():')[0])\n\ncombos = [\n    ('tracvla', 'spatial', 'untrained'),\n    ('tracvla', 'object', 'untrained'),\n    ('openvla', 'object', 'untrained'),\n    ('openvla', 'long', 'trained'),\n    ('nora', 'goal', 'untrained'),\n]\nfor arch, suite, cond in combos:\n    key = (arch, suite, cond)\n    method = resolve_method(arch, cond, 'auto')\n    tasks, instr, para = _get_task_config(arch, suite)\n    print(f'{key} -> method={method}, ckpt={CKPT_MAP[key].split(\\\"/\\\")[-1]}, '\n          f'results={RESULTS_MAP[key].split(\\\"results/\\\")[-1]}, '\n          f'n_tasks={len(tasks)}, n_layers={ARCH_CFG[arch][\\\"n_layers\\\"]}')\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-21T16:54:02.855370+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"('tracvla', 'spatial', 'untrained') -> method=cosine_dist, ckpt=, results=tracvla_spatial/untrained, n_tasks=10, n_layers=32\\n('tracvla', 'object', 'untrained') -> method=cosine_dist, ckpt=, results=tracvla_object/untrained, n_tasks=10, n_layers=32\\n('openvla', 'object', 'untrained') -> method=cosine_dist, ckpt=openvla-7b, results=libero_object_untrained, n_tasks=10, n_layers=32\\n('openvla', 'long', 'trained') -> method=action_mse, ckpt=openvla-7b-oft-finetuned-libero-10, results=libero_long/trained, n_tasks=10, n_layers=32\\n('nora', 'goal', 'untrained') -> method=cosine_dist, ckpt=, results=nora_goal/untrained, n_tasks=10, n_layers=36\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 10.6}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-21T16:54:02.855549+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "wc -l /root/autodl-tmp/vla-ssd/scripts/counterfactual_batch.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "wc -l /root/autodl-tmp/vla-ssd/scripts/counterfactual_batch.py"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-21T16:54:02.855685+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"884 /root/autodl-tmp/vla-ssd/scripts/counterfactual_batch.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.59}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_counterfactual_batch_template_20260521T164440",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 85 · 2026-05-21T16:54:02.855848+00:00_

脚本已创建: `/root/autodl-tmp/vla-ssd/scripts/counterfactual_batch.py` (884 行)

功能:
- 支持 `--arch openvla/tracvla/nora`, `--suite goal/spatial/object/long`, `--condition trained/untrained`
- `--method auto` 自动选择: trained openvla/tracvla → action_mse, nora 和所有 untrained → cosine_dist
- 内置全部 checkpoint/data/results 路径映射，匹配现有 pipeline 脚本的 task 顺序
- OFT checkpoint 自动合并 dataset_statistics.json 到 norm_stats
- `--dry-run` 快速验证, `--results-dir` 可覆盖输出目录
- `--gpu`, `--n-demos`, `--n-timesteps` 可调

用法:
```bash
python counterfactual_batch.py --arch tracvla --suite spatial --condition untrained
python counterfactual_batch.py --arch openvla --suite long --condition trained
python counterfactual_batch.py --arch openvla --suite object --condition untrained
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_counterfactual_batch_template_20260521T164440"
}
```

</details>

---
