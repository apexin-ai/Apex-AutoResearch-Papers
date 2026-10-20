# code lg instruction probe

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 0
- **Tool calls:** 26
- **Original source:** `logs/chats/worker_code_lg-instruction-probe_20260515T165250.jsonl`
- **Structured JSON:** [`de2911897242f37392ef.json`](../../sessions/de/de2911897242f37392ef.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

53 recorded events

### Tool call

_source line 1 · 2026-05-15T16:58:12.271476+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T16:58:12.271815+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T16:58:12.272021+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/vla-ssd/scripts/train_probes.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/vla-ssd/scripts/train_probes.py"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-15T16:58:12.272175+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/vla-ssd/scripts/extract_features.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/vla-ssd/scripts/extract_features.py"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T16:58:12.272356+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ls /root/autodl-tmp/vla-ssd/data/libero/libero_goal/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ls /root/autodl-tmp/vla-ssd/data/libero/libero_goal/"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T16:58:12.272632+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"train_probes.py — Train probes (linear/MLP) on VLA/DINO-V2 hidden states.\\n\\nInput:  features/{mode}/{task}.h5 — per-task HDF5 with per-trajectory hidden states\\nOutput: results/{mode}/{probe_type}/ — per-layer JSON + summary CSV\\n\\nUsage:\\n  python train_probes.py --features_dir features/trained/ --output_dir results/trained/ --probe_type temporal_distance\\n  python train_probes.py --features_dir features/trained/ --output_dir results/trained/ --probe_type oracle\\n  python train_probes.py --features_dir features/trained/ --output_dir results/trained/ --probe_type subtask_predicate --label_file labels.json\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport csv\\nimport json\\nimport os\\nimport glob\\nimport time\\nfrom collections import defaultdict\\nfrom pathlib import Path\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nimport torch.nn as nn\\nfrom scipy.stats import spearmanr\\nfrom sklearn.metrics import (r2_score, mean_absolute_error, roc_auc_score,\\n                             accuracy_score, f1_score, confusion_matrix)\\nfrom sklearn.decomposition import PCA as SklearnPCA\\n\\n# OpenVLA: last_preaction / image_mean  shape (T, 33, 4096)\\n# DINO-V2: cls_token / patch_mean       shape (T, 1024)\\nAGG_MAP = {\\n    \\\"last_preaction\\\": (\\\"last_preaction\\\", \\\"cls_token\\\"),\\n    \\\"image_mean\\\": (\\\"image_mean\\\", \\\"patch_mean\\\"),\\n}\\n\\n\\ndef parse_args():\\n    p = argparse.ArgumentParser(description=\\\"Train probes (linear/MLP) on VLA/DINO-V2 features\\\")\\n    p.add_argument(\\\"--features_dir\\\", required=True,\\n                   help=\\\"Directory with per-task HDF5 feature files\\\")\\n    p.add_argument(\\\"--output_dir\\\", required=True,\\n                   help=\\\"Directory to save probe results\\\")\\n    p.add_argument(\\\"--probe_type\\\", required=True,\\n                   choices=[\\\"temporal_distance\\\", \\\"subtask_predicate\\\", \\\
…[truncated 7391 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T16:58:12.272793+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ls /root/autodl-tmp/vla-ssd/features/trained_libero_goal/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ls /root/autodl-tmp/vla-ssd/features/trained_libero_goal/"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T16:58:12.273101+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"extract_features.py — Extract OpenVLA hidden states for temporal distance probing.\\n\\nInput:  LIBERO HDF5 demos + OpenVLA checkpoint (or untrained variant)\\nOutput: Per-task HDF5 files with per-demo hidden states (T, num_layers, 4096) in fp16\\nDependencies: transformers, torch, h5py, tqdm, Pillow\\n\\nToken layout (Prismatic/OpenVLA): [BOS] [256 image tokens] [text tokens...]\\n  - last_preaction: hidden state at the last sequence position (pre-action)\\n  - image_mean: mean of 256 image token hidden states (positions 1:257)\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport gc\\nimport glob\\nimport os\\nimport re\\nimport time\\n\\nos.environ[\\\"HDF5_USE_FILE_LOCKING\\\"] = \\\"FALSE\\\"\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nfrom pathlib import Path\\nfrom PIL import Image\\nfrom tqdm import tqdm\\n\\nNUM_IMAGE_TOKENS = 256\\nNUM_HIDDEN_LAYERS = 33  # embedding + 32 transformer layers\\n\\n\\ndef parse_args():\\n    p = argparse.ArgumentParser(\\n        description=\\\"Extract OpenVLA hidden states for temporal distance probing\\\"\\n    )\\n    p.add_argument(\\\"--model_path\\\", required=True,\\n                   help=\\\"Path to OpenVLA checkpoint directory\\\")\\n    p.add_argument(\\\"--data_dir\\\", default=\\\"/root/autodl-tmp/vla-ssd/data/libero/libero_10/\\\",\\n                   help=\\\"Directory containing LIBERO HDF5 files\\\")\\n    p.add_argument(\\\"--output_dir\\\", required=True,\\n                   help=\\\"Output directory for extracted features\\\")\\n    p.add_argument(\\\"--gpu\\\", type=int, default=0)\\n    p.add_argument(\\\"--mode\\\", choices=[\\\"trained\\\", \\\"untrained\\\"], default=\\\"trained\\\",\\n                   help=\\\"'untrained' reinitializes LLM backbone randomly\\\")\\n    p.add_argument(\\\"--task_filter\\\", default=None,\\n                   help=\\\"Substring filter on HDF5 filename\\\")\\n    p.add_argument(\\\"--task_instruc
…[truncated 7073 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-15T16:58:12.273319+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"open_the_middle_drawer_of_the_cabinet_demo.hdf5\\nopen_the_top_drawer_and_put_the_bowl_inside_demo.hdf5\\npush_the_plate_to_the_front_of_the_stove_demo.hdf5\\nput_the_bowl_on_the_plate_demo.hdf5\\nput_the_bowl_on_the_stove_demo.hdf5\\nput_the_bowl_on_top_of_the_cabinet_demo.hdf5\\nput_the_cream_cheese_in_the_bowl_demo.hdf5\\nput_the_wine_bottle_on_the_rack_demo.hdf5\\nput_the_wine_bottle_on_top_of_the_cabinet_demo.hdf5\\nturn_on_the_stove_demo.hdf5\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T16:58:12.273458+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"open_the_middle_drawer_of_the_cabinet.h5\\nopen_the_top_drawer_and_put_the_bowl_inside.h5\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T16:58:12.273650+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -n \"run_goal_classification\\|def train_probe\\|class MLP\\|class Linear\" /root/vla-ssd/scripts/train_probes.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "grep -n \"run_goal_classification\\|def train_probe\\|class MLP\\|class Linear\" /root/vla-ssd/scripts/train_probes.py"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T16:58:12.273799+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T16:58:12.273942+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ls /root/autodl-tmp/vla-ssd/features/untrained_libero_goal/ 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ls /root/autodl-tmp/vla-ssd/features/untrained_libero_goal/ 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T16:58:12.274084+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T16:58:12.274203+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ls /root/autodl-tmp/vla-ssd/features/dinov2_libero_goal/ 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ls /root/autodl-tmp/vla-ssd/features/dinov2_libero_goal/ 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T16:58:12.274318+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T16:58:12.274442+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -n \"run_goal_classification\\|def train_probe\\|class MLP\\|class Linear\" /root/vla-ssd/scripts/train_probes.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "grep -n \"run_goal_classification\\|def train_probe\\|class MLP\\|class Linear\" /root/vla-ssd/scripts/train_probes.py"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T16:58:12.274558+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T16:58:12.274670+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ls /root/autodl-tmp/vla-ssd/features/untrained_libero_goal/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ls /root/autodl-tmp/vla-ssd/features/untrained_libero_goal/"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-15T16:58:12.274781+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ls /root/autodl-tmp/vla-ssd/features/dinov2_libero_goal/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ls /root/autodl-tmp/vla-ssd/features/dinov2_libero_goal/"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-15T16:58:12.274902+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"open_the_middle_drawer_of_the_cabinet.h5\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T16:58:12.275068+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/autodl-tmp/vla-ssd/features/dinov2_libero_goal/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T16:58:12.275239+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -n \"run_goal_classification\" /root/vla-ssd/scripts/train_probes.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "grep -n \"run_goal_classification\" /root/vla-ssd/scripts/train_probes.py"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T16:58:12.275367+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"894:def run_goal_classification(args, device):\\n1048:        goal_classification=run_goal_classification,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T16:58:12.275481+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -n \"def \" /root/vla-ssd/scripts/train_probes.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "grep -n \"def \" /root/vla-ssd/scripts/train_probes.py"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-15T16:58:12.275593+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ls /root/autodl-tmp/vla-ssd/features/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ls /root/autodl-tmp/vla-ssd/features/"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-15T16:58:12.275724+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"38:def parse_args():\\n78:def scan_features(features_dir, aggregation):\\n113:def split_by_task(traj_metas):\\n128:def load_layer_features(traj_metas, indices, layer):\\n151:def parse_layers(layers_str, max_layer):\\n160:def apply_pca(X_tr, X_val, pca_dim):\\n180:def sample_pairs(traj_metas, indices, n_bins, pairs_per_bin, seed):\\n212:def build_pair_tensors(feats, pairs):\\n224:def build_oracle_tensors(pairs):\\n231:def sample_cross_trajectory_pairs(traj_metas, indices, n_bins, pairs_per_bin, seed):\\n275:def build_cross_pair_tensors(feats, pairs):\\n292:    def __init__(self, in_dim):\\n296:    def forward(self, x):\\n301:    def __init__(self, in_dim, hidden_dim=256):\\n309:    def forward(self, x):\\n316:    def __init__(self, in_dim, out_dim=7, hidden_dim=256):\\n324:    def forward(self, x):\\n328:    def __init__(self, in_dim, n_labels):\\n332:    def forward(self, x):\\n337:    def __init__(self, in_dim, n_classes, hidden_dim=256, dropout=0.1):\\n346:    def forward(self, x):\\n352:def train_regression_probe(X_tr, y_tr, X_val, y_val, in_dim, args, device):\\n408:def train_classification_probe(X_tr, y_tr, X_val, y_val, in_dim, n_labels, args, device):\\n469:def train_goal_classification_probe(X_tr, y_tr, X_val, y_val, in_dim, n_classes, args, device):\\n543:def load_actions(traj_metas, indices, data_dir):\\n561:def run_action_prediction(args, device):\\n573:    def build_shifted(feats, acts, ids_list):\\n713:def run_temporal_distance(args, device):\\n808:def run_oracle(args, device):\\n825:def run_subtask_predicate(args, device):\\n845:        def gather(ids):\\n894:def run_goal_classification(args, device):\\n924:        def flatten(feats, ids):\\n967:def save_results(results, output_dir, probe_type):\\n1030:def main():\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.76}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T16:58:12.275860+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"dinov2\\ntrained\\ntrained_libero_goal\\nuntrained\\nuntrained_libero_goal\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T16:58:12.276053+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "head -966 /root/vla-ssd/scripts/train_probes.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "head -966 /root/vla-ssd/scripts/train_probes.py"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T16:58:12.276305+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"train_probes.py — Train probes (linear/MLP) on VLA/DINO-V2 hidden states.\\n\\nInput:  features/{mode}/{task}.h5 — per-task HDF5 with per-trajectory hidden states\\nOutput: results/{mode}/{probe_type}/ — per-layer JSON + summary CSV\\n\\nUsage:\\n  python train_probes.py --features_dir features/trained/ --output_dir results/trained/ --probe_type temporal_distance\\n  python train_probes.py --features_dir features/trained/ --output_dir results/trained/ --probe_type oracle\\n  python train_probes.py --features_dir features/trained/ --output_dir results/trained/ --probe_type subtask_predicate --label_file labels.json\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport csv\\nimport json\\nimport os\\nimport glob\\nimport time\\nfrom collections import defaultdict\\nfrom pathlib import Path\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nimport torch.nn as nn\\nfrom scipy.stats import spearmanr\\nfrom sklearn.metrics import (r2_score, mean_absolute_error, roc_auc_score,\\n                             accuracy_score, f1_score, confusion_matrix)\\nfrom sklearn.decomposition import PCA as SklearnPCA\\n\\n# OpenVLA: last_preaction / image_mean  shape (T, 33, 4096)\\n# DINO-V2: cls_token / patch_mean       shape (T, 1024)\\nAGG_MAP = {\\n    \\\"last_preaction\\\": (\\\"last_preaction\\\", \\\"cls_token\\\"),\\n    \\\"image_mean\\\": (\\\"image_mean\\\", \\\"patch_mean\\\"),\\n}\\n\\n\\ndef parse_args():\\n    p = argparse.ArgumentParser(description=\\\"Train probes (linear/MLP) on VLA/DINO-V2 features\\\")\\n    p.add_argument(\\\"--features_dir\\\", required=True,\\n                   help=\\\"Directory with per-task HDF5 feature files\\\")\\n    p.add_argument(\\\"--output_dir\\\", required=True,\\n                   help=\\\"Directory to save probe results\\\")\\n    p.add_argument(\\\"--probe_type\\\", required=True,\\n                   choices=[\\\"temporal_distance\\\", \\\"subtask_predicate\\\", \\\
…[truncated 7114 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T16:58:12.276485+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "head -542 /root/vla-ssd/scripts/train_probes.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "head -542 /root/vla-ssd/scripts/train_probes.py"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T16:58:12.276723+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"train_probes.py — Train probes (linear/MLP) on VLA/DINO-V2 hidden states.\\n\\nInput:  features/{mode}/{task}.h5 — per-task HDF5 with per-trajectory hidden states\\nOutput: results/{mode}/{probe_type}/ — per-layer JSON + summary CSV\\n\\nUsage:\\n  python train_probes.py --features_dir features/trained/ --output_dir results/trained/ --probe_type temporal_distance\\n  python train_probes.py --features_dir features/trained/ --output_dir results/trained/ --probe_type oracle\\n  python train_probes.py --features_dir features/trained/ --output_dir results/trained/ --probe_type subtask_predicate --label_file labels.json\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport csv\\nimport json\\nimport os\\nimport glob\\nimport time\\nfrom collections import defaultdict\\nfrom pathlib import Path\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nimport torch.nn as nn\\nfrom scipy.stats import spearmanr\\nfrom sklearn.metrics import (r2_score, mean_absolute_error, roc_auc_score,\\n                             accuracy_score, f1_score, confusion_matrix)\\nfrom sklearn.decomposition import PCA as SklearnPCA\\n\\n# OpenVLA: last_preaction / image_mean  shape (T, 33, 4096)\\n# DINO-V2: cls_token / patch_mean       shape (T, 1024)\\nAGG_MAP = {\\n    \\\"last_preaction\\\": (\\\"last_preaction\\\", \\\"cls_token\\\"),\\n    \\\"image_mean\\\": (\\\"image_mean\\\", \\\"patch_mean\\\"),\\n}\\n\\n\\ndef parse_args():\\n    p = argparse.ArgumentParser(description=\\\"Train probes (linear/MLP) on VLA/DINO-V2 features\\\")\\n    p.add_argument(\\\"--features_dir\\\", required=True,\\n                   help=\\\"Directory with per-task HDF5 feature files\\\")\\n    p.add_argument(\\\"--output_dir\\\", required=True,\\n                   help=\\\"Directory to save probe results\\\")\\n    p.add_argument(\\\"--probe_type\\\", required=True,\\n                   choices=[\\\"temporal_distance\\\", \\\"subtask_predicate\\\", \\\
…[truncated 7028 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T16:58:12.276903+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "head -350 /root/vla-ssd/scripts/train_probes.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "head -350 /root/vla-ssd/scripts/train_probes.py"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T16:58:12.277166+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"train_probes.py — Train probes (linear/MLP) on VLA/DINO-V2 hidden states.\\n\\nInput:  features/{mode}/{task}.h5 — per-task HDF5 with per-trajectory hidden states\\nOutput: results/{mode}/{probe_type}/ — per-layer JSON + summary CSV\\n\\nUsage:\\n  python train_probes.py --features_dir features/trained/ --output_dir results/trained/ --probe_type temporal_distance\\n  python train_probes.py --features_dir features/trained/ --output_dir results/trained/ --probe_type oracle\\n  python train_probes.py --features_dir features/trained/ --output_dir results/trained/ --probe_type subtask_predicate --label_file labels.json\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport csv\\nimport json\\nimport os\\nimport glob\\nimport time\\nfrom collections import defaultdict\\nfrom pathlib import Path\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nimport torch.nn as nn\\nfrom scipy.stats import spearmanr\\nfrom sklearn.metrics import (r2_score, mean_absolute_error, roc_auc_score,\\n                             accuracy_score, f1_score, confusion_matrix)\\nfrom sklearn.decomposition import PCA as SklearnPCA\\n\\n# OpenVLA: last_preaction / image_mean  shape (T, 33, 4096)\\n# DINO-V2: cls_token / patch_mean       shape (T, 1024)\\nAGG_MAP = {\\n    \\\"last_preaction\\\": (\\\"last_preaction\\\", \\\"cls_token\\\"),\\n    \\\"image_mean\\\": (\\\"image_mean\\\", \\\"patch_mean\\\"),\\n}\\n\\n\\ndef parse_args():\\n    p = argparse.ArgumentParser(description=\\\"Train probes (linear/MLP) on VLA/DINO-V2 features\\\")\\n    p.add_argument(\\\"--features_dir\\\", required=True,\\n                   help=\\\"Directory with per-task HDF5 feature files\\\")\\n    p.add_argument(\\\"--output_dir\\\", required=True,\\n                   help=\\\"Directory to save probe results\\\")\\n    p.add_argument(\\\"--probe_type\\\", required=True,\\n                   choices=[\\\"temporal_distance\\\", \\\"subtask_predicate\\\", \\\
…[truncated 7075 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T16:58:12.277373+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ls /root/autodl-tmp/vla-ssd/results/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ls /root/autodl-tmp/vla-ssd/results/"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-15T16:58:12.277517+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"action_baselines.json\\nanalysis\\ndinov2\\ndinov2_shuffle\\nfigures\\noracle\\ntrained\\ntrained_label_perm\\nuntrained\\nuntrained_label_perm\\nvisual_similarity_gate.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-15T16:58:12.277661+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "find /root/autodl-tmp/vla-ssd/results/ -name \"summary.json\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "find /root/autodl-tmp/vla-ssd/results/ -name \"summary.json\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-15T16:58:12.277848+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/vla-ssd/results/dinov2/temporal_distance/summary.json\\n/root/autodl-tmp/vla-ssd/results/dinov2/subtask_predicate/summary.json\\n/root/autodl-tmp/vla-ssd/results/dinov2/temporal_distance_old_backup/summary.json\\n/root/autodl-tmp/vla-ssd/results/dinov2/temporal_distance_old_backup/temporal_distance/summary.json\\n/root/autodl-tmp/vla-ssd/results/dinov2/action_prediction/summary.json\\n/root/autodl-tmp/vla-ssd/results/dinov2/action_delta/summary.json\\n/root/autodl-tmp/vla-ssd/results/oracle/oracle/summary.json\\n/root/autodl-tmp/vla-ssd/results/dinov2_shuffle/temporal_distance/summary.json\\n/root/autodl-tmp/vla-ssd/results/untrained/temporal_distance/summary.json\\n/root/autodl-tmp/vla-ssd/results/untrained/action_prediction/summary.json\\n/root/autodl-tmp/vla-ssd/results/untrained/action_delta/summary.json\\n/root/autodl-tmp/vla-ssd/results/trained/temporal_distance/summary.json\\n/root/autodl-tmp/vla-ssd/results/trained/action_delta/summary.json\\n/root/autodl-tmp/vla-ssd/results/trained/action_prediction/summary.json\\n/root/autodl-tmp/vla-ssd/results/analysis/summary.json\\n/root/autodl-tmp/vla-ssd/results/trained_label_perm/temporal_distance/summary.json\\n/root/autodl-tmp/vla-ssd/results/untrained_label_perm/temporal_distance/summary.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-15T16:58:12.278049+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ls /root/vla-ssd/scripts/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ls /root/vla-ssd/scripts/"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-15T16:58:12.278195+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"__init__.py\\n__pycache__\\nanalyze_action_probes.py\\nanalyze_goal_probes.py\\nanalyze_mvp_DEPRECATED.py\\nanalyze_results.py\\nanalyze_results.py.bak2\\nextract_dinov2.py\\nextract_features.py\\nextract_features.py.bak\\nextract_subtask_labels.py\\ninit_untrained.py\\nplot_action_probes.py\\npost_download_pipeline.py\\nsubtask_auc_dinov2.py\\ntest_forward.py\\ntrain_instruction_probes.py\\ntrain_probes.py\\ntrain_probes.py.bak2\\ntrain_probes.py.bak3\\nverify_and_continue.sh\\nverify_shard.py\\nvisual_similarity_gate.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-15T16:58:12.278347+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/vla-ssd/scripts/analyze_goal_probes.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/vla-ssd/scripts/analyze_goal_probes.py"
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-15T16:58:12.278468+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/vla-ssd/scripts/train_instruction_probes.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/vla-ssd/scripts/train_instruction_probes.py"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-15T16:58:12.278702+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"analyze_goal_probes.py — Compare goal classification probe results across trained/untrained/dinov2.\\n\\nReads summary.json from each model's goal_classification output directory.\\nOutputs: per-layer accuracy comparison, best layer summary, gate judgment.\\n\\nGate: trained accuracy > 50% AND trained-DINO gap > 40pp.\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport os\\nimport sys\\n\\n\\ndef load_summary(result_dir):\\n    path = os.path.join(result_dir, \\\"goal_classification\\\", \\\"summary.json\\\")\\n    if not os.path.exists(path):\\n        return None\\n    with open(path) as f:\\n        return json.load(f)\\n\\n\\ndef main():\\n    p = argparse.ArgumentParser(description=\\\"Analyze goal classification probe results\\\")\\n    p.add_argument(\\\"--trained_dir\\\", required=True, help=\\\"Results dir for trained VLA\\\")\\n    p.add_argument(\\\"--untrained_dir\\\", default=None, help=\\\"Results dir for untrained VLA\\\")\\n    p.add_argument(\\\"--dino_dir\\\", default=None, help=\\\"Results dir for DINO-V2\\\")\\n    p.add_argument(\\\"--acc_gate\\\", type=float, default=0.50, help=\\\"Min trained accuracy for gate (default: 0.50)\\\")\\n    p.add_argument(\\\"--gap_gate\\\", type=float, default=0.40, help=\\\"Min trained-DINO accuracy gap (default: 0.40)\\\")\\n    args = p.parse_args()\\n\\n    summaries = {}\\n    for name, path in [(\\\"trained\\\", args.trained_dir),\\n                        (\\\"untrained\\\", args.untrained_dir),\\n                        (\\\"dinov2\\\", args.dino_dir)]:\\n        if path is None:\\n            continue\\n        s = load_summary(path)\\n        if s is None:\\n            print(f\\\"WARNING: No goal_classification/summary.json in {path}\\\")\\n            continue\\n        summaries[name] = s\\n\\n    if not summaries:\\n        print(\\\"No results found. Exiting.\\\")\\n        sys.exit(1)\\n\\n    # Per-layer accuracy table\\n 
…[truncated 3006 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-15T16:58:12.279135+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"train_instruction_probes.py — Goal classification probes for LIBERO-Goal shared-scene analysis.\\n\\nTests whether VLA hidden states encode instruction/goal information by training\\nN-way classifiers on tasks sharing the same visual scene.\\n\\nUsage:\\n  python train_instruction_probes.py \\\\\\n    --feature_dir /root/autodl-tmp/vla-ssd/features/trained \\\\\\n    --output_dir /root/autodl-tmp/vla-ssd/results/trained/instruction_probe \\\\\\n    --model_type trained --num_layers 33 --feature_dim 4096\\n\\n  python train_instruction_probes.py \\\\\\n    --feature_dir /root/autodl-tmp/vla-ssd/features/dinov2 \\\\\\n    --output_dir /root/autodl-tmp/vla-ssd/results/dinov2/instruction_probe \\\\\\n    --model_type dinov2 --feature_dim 1024\\n\\n  # With visual gate check:\\n  python train_instruction_probes.py \\\\\\n    --feature_dir /root/autodl-tmp/vla-ssd/features/trained \\\\\\n    --output_dir /root/autodl-tmp/vla-ssd/results/trained/instruction_probe \\\\\\n    --model_type trained --dino_visual_gate\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport os\\nimport re\\nimport glob\\nimport time\\nfrom collections import defaultdict\\nfrom pathlib import Path\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nimport torch.nn as nn\\nfrom sklearn.decomposition import PCA as SklearnPCA\\nfrom sklearn.metrics import confusion_matrix\\n\\n\\n# ============================================================\\n# H5 key conventions\\n# ============================================================\\n# VLA (trained/untrained): demo_X/image_mean  shape (T, 33, 4096)\\n#                          demo_X/last_preaction  shape (T, 33, 4096)\\n# DINO-V2:                 traj_X/cls_token   shape (T, 1024)\\n#                          traj_X/patch_mean   shape (T, 1024)\\n\\nAGG_KEYS = {\\n    \\\"image_mean\\\": (\\\"image_mean\\\", \\\"patch_mean\\\"),\\n    \\\"last_preaction\\\": (\\\"last_preaction\\
…[truncated 7177 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-15T16:58:12.279571+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19183",
  "command": "cat > /root/vla-ssd/scripts/train_goal_probe.py << 'SCRIPT_EOF'\n\"\"\"train_goal_probe.py — Goal classification probing for LIBERO-Goal.\n\nTrains per-layer MLP classifiers to predict which goal/task a hidden state\nbelongs to. All LIBERO-Goal tasks share the same visual scene, so above-chance\naccuracy implies hidden states encode instruction/goal information.\n\nInput:  features/{model}/ — per-task HDF5 files (T, n_layers, dim) per demo\nOutput: results/{model}/goal_classification/ — per-layer JSON + summary CSV/JSON\n\nDependencies: torch, h5py, numpy, sklearn, scipy (via train_probes.py)\n\nUsage:\n  python train_goal_probe.py \\\n    --features_dir /root/autodl-tmp/vla-ssd/features/trained_libero_goal/ \\\n    --output_dir /root/autodl-tmp/vla-ssd/results/trained_libero_goal/ \\\n    --gpu 0\n\n  # Untrained baseline:\n  python train_goal_probe.py \\\n    --features_dir /root/autodl-tmp/vla-ssd/features/untrained_libero_goal/ \\\n    --output_dir /root/autodl-tmp/vla-ssd/results/untrained_libero_goal/ \\\n    --gpu 1\n\n  # DINO-V2 baseline:\n  python train_goal_probe.py \\\n    --features_dir /root/autodl-tmp/vla-ssd/features/dinov2_libero_goal/ \\\n    --output_dir /root/autodl-tmp/vla-ssd/results/dinov2_libero_goal/ \\\n    --gpu 0\n\n  # Permutation test (negative control):\n  python train_goal_probe.py \\\n    --features_dir /root/autodl-tmp/vla-ssd/features/trained_libero_goal/ \\\n    --output_dir /root/autodl-tmp/vla-ssd/results/trained_libero_goal_perm/ \\\n    --shuffle_labels --gpu 0\n\"\"\"\n\nimport argparse\nimport json\nimport os\nimport sys\nimport time\n\nimport numpy as np\nimport torch\n\nsys.path.insert(0, os.path.dirname(__file__))\nfrom train_probes import (\n    scan_features,\n    split_by_task,\n    load_layer_features,\n    parse_layers,\n    apply_pca,\n    train_goal_classification_probe,\n    save_results,\n)\n\n\ndef parse_args():\n    p = argparse.ArgumentParser(\n        description=\"Goal classification probing for LIBERO-Goal shared-scene tasks\")\n    p.add_argument(\"--features_dir\", required=True,\n                   help=\"Directory with per-task HDF5 feature files\")\n    p.add_argument(\"--output_dir\", required=True,\n                   help=\"Directory to save probe results\")\n    p.add_argument(\"--probe_type\", default=\"goal_classification\",\n                   help=\"(fixed) goal_classification\")\n    p.add_argument(\"--data_dir\",\n                   default=\"/root/autodl-tmp/vla-ssd/data/libero/libero_goal/\",\n                   help=\"LIBERO raw data directory (reserved for future use)\")\n    p.add_argument(\"--aggregation\", default=\"last_preaction\",\n                   choices=[\"last_preaction\", \"image_mean\"],\n                   help=\"Token aggregation strategy (default: last_preaction)\")\n    p.add_argument(\"--layers\", default=None,\n                   help=\"Layer range '0-32' or list '0,5,10'. Default: all\")\n    p.add_argument(\"--pca_dim\", type=int, default=None,\n                   help=\"PCA reduce features to N dims before probe\")\n    p.add_argument(\"--seed\", type=int, default=42)\n    p.add_argument(\"--batch_size\", type=int, default=256)\n    p.add_argument(\"--lr\", type=float, default=1e-3)\n    p.add_argument(\"--epochs\", type=int, default=50)\n    p.add_argument(\"--patience\", type=int, default=5)\n    p.add_argument(\"--gpu\", type=int, default=0)\n    p.add_argument(\"--shuffle_labels\", action=\"store_true\",\n                   help=\"Permutation test: randomly shuffle goal labels\")\n    return p.parse_args()\n\n\ndef run_goal_probe(args, device):\n    \"\"\"Per-layer goal classification with per-trajectory train/val split.\"\"\"\n    traj_metas, n_layers, hidden_dim = scan_features(\n        args.features_dir, args.aggregation)\n    layers = parse_layers(args.layers, n_layers - 1)\n\n    task_names = sorted(set(m[\"task\"] for m in traj_metas))\n    task_to_idx = {t: i for i, t in enumerate(task_names)}\n    n_classes = len(task_names)\n    chance = 1.0 / n_classes\n\n    train_ids, val_ids = split_by_task(traj_metas)\n\n    # Report class balance\n    train_counts = {}\n    val_counts = {}\n    for idx in train_ids:\n        t = traj_metas[idx][\"task\"]\n        train_counts[t] = train_counts.get(t, 0) + 1\n    for idx in val_ids:\n        t = traj_metas[idx][\"task\"]\n        val_counts[t] = val_counts.get(t, 0) + 1\n\n    print(f\"Features: {len(traj_metas)} trajs, {n_layers} layers, dim={hidden_dim}\")\n    print(f\"Tasks ({n_classes}):\")\n    for t in task_names:\n        print(f\"  [{task_to_idx[t]}] {t}  \"\n              f\"(train={train_counts.get(t,0)}, val={val_counts.get(t,0)} trajs)\")\n    print(f\"Chance level: {chance:.4f} ({n_classes}-way)\")\n    print(f\"Split: {len(train_ids)} train / {len(val_ids)} val trajs\")\n    if args.shuffle_labels:\n        print(\"** PERMUTATION TEST: goal labels will be shuffled **\")\n\n    results = {}\n    for li, layer in enumerate(layers):\n        print(f\"\\n[Layer {layer}] ({li+1}/{len(layers)})\", flush=True)\n        t0 = time.time()\n\n        train_feats = load_layer_features(traj_metas, train_ids, layer)\n        val_feats = load_layer_features(traj_metas, val_ids, layer)\n\n        def flatten(feats, ids):\n            Xs, Ys = [], []\n            for feat, idx in zip(feats, ids):\n                label = task_to_idx[traj_metas[idx][\"task\"]]\n                T = feat.shape[0]\n                Xs.append(torch.from_numpy(feat))\n                Ys.append(torch.full((T,), label, dtype=torch.long))\n            return torch.cat(Xs), torch.cat(Ys)\n\n        X_tr, y_tr = flatten(train_feats, train_ids)\n        X_val, y_val = flatten(val_feats, val_ids)\n        del train_feats, val_feats\n\n        if args.shuffle_labels:\n            perm = torch.randperm(len(y_tr))\n            y_tr = y_tr[perm]\n\n        probe_dim = hidden_dim\n        pca_info = None\n        if args.pca_dim is not None:\n            X_tr, X_val, pca_info = apply_pca(X_tr, X_val, args.pca_dim)\n            probe_dim = args.pca_dim\n            print(f\"  PCA {hidden_dim} -> {args.pca_dim}: \"\n                  f\"{pca_info['cumulative_variance_ratio']:.4f} variance retained\")\n\n        print(f\"  Samples: {len(X_tr)} train / {len(X_val)} val\")\n        met = train_goal_classification_probe(\n            X_tr, y_tr, X_val, y_val, probe_dim, n_classes, args, device)\n        met[\"layer\"] = layer\n        met[\"task_names\"] = task_names\n        met[\"n_classes\"] = n_classes\n        met[\"chance_level\"] = chance\n        met[\"shuffle_labels\"] = args.shuffle_labels\n        if pca_info is not None:\n            met[\"pca_dim\"] = args.pca_dim\n            met[\"pca_info\"] = pca_info\n        results[layer] = met\n\n        delta = met[\"accuracy\"] - chance\n        print(f\"  acc={met['accuracy']:.4f} (Δchance={delta:+.4f})  \"\n              f\"F1={met['macro_f1']:.4f}  ep={met['epochs_trained']}  \"\n              f\"{time.time()-t0:.1f}s\")\n\n    return results\n\n\ndef main():\n    args = parse_args()\n    torch.manual_seed(args.seed)\n    np.random.seed(args.seed)\n    device = torch.device(\n        f\"cuda:{args.gpu}\" if torch.cuda.is_available() else \"cpu\")\n\n    if args.pca_dim is not None:\n        args.output_dir = args.output_dir.rstrip(\"/\") + f\"_pca{args.pca_dim}\"\n\n    print(f\"=== Goal Classification Probe | device={device} ===\")\n    print(f\"  features: {args.features_dir}\")\n    print(f\"  output:   {args.output_dir}\")\n    print(f\"  aggregation: {args.aggregation}\")\n\n    results = run_goal_probe(args, device)\n    save_results(results, args.output_dir, \"goal_classification\")\n\n    if results:\n        best = max(results, key=lambda k: results[k][\"accuracy\"])\n        chance = results[best][\"chance_level\"]\n        print(f\"\\n{'='*60}\")\n        print(f\"Best layer: {best}\")\n        print(f\"  accuracy:  {results[best]['accuracy']:.4f}  \"\n              f\"(Δchance = {results[best]['accuracy']-chance:+.4f})\")\n        print(f\"  macro F1:  {results[best]['macro_f1']:.4f}\")\n        print(f\"  chance:    {chance:.4f}\")\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT_EOF\necho \"train_goal_probe.py written: $(wc -l < /root/vla-ssd/scripts/train_goal_probe.py) lines\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat > /root/vla-ssd/scripts/train_goal_probe.py << 'SCRIPT_EOF'\n\"\"\"train_goal_probe.py — Goal classification probing for LIBERO-Goal.\n\nTrains per-layer MLP classifiers to predict which goal/task a hidden state\nbelongs to. All LIBERO-Goal tasks share the same visual scene, so above-chance\naccuracy implies hidden states encode instruction/goal information.\n\nInput:  features/{model}/ — per-task HDF5 files (T, n_layers, dim) per demo\nOutput: results/{model}/goal_classification/ — per-layer JSON + summary CSV/JSON\n\nDependencies: torch, h5py, numpy, sklearn, scipy (via train_probes.py)\n\nUsage:\n  python train_goal_probe.py \\\n    --features_dir /root/autodl-tmp/vla-ssd/features/trained_libero_goal/ \\\n    --output_dir /root/autodl-tmp/vla-ssd/results/trained_libero_goal/ \\\n    --gpu 0\n\n  # Untrained baseline:\n  python train_goal_probe.py \\\n    --features_dir /root/autodl-tmp/vla-ssd/features/untrained_libero_goal/ \\\n    --output_dir /root/autodl-tmp/vla-ssd/results/untrained_libero_goal/ \\\n    --gpu 1\n\n  # DINO-V2 baseline:\n  python train_goal_probe.py \\\n    --features_dir /root/autodl-tmp/vla-ssd/features/dinov2_libero_goal/ \\\n    --output_dir /root/autodl-tmp/vla-ssd/results/dinov2_libero_goal/ \\\n    --gpu 0\n\n  # Permutation test (negative control):\n  python train_goal_probe.py \\\n    --features_dir /root/autodl-tmp/vla-ssd/features/trained_libero_goal/ \\\n    --output_dir /root/autodl-tmp/vla-ssd/results/trained_libero_goal_perm/ \\\n    --shuffle_labels --gpu 0\n\"\"\"\n\nimport argparse\nimport json\nimport os\nimport sys\nimport time\n\nimport numpy as np\nimport torch\n\nsys.path.insert(0, os.path.dirname(__file__))\nfrom train_probes import (\n    scan_features,\n    split_by_task,\n    load_layer_features,\n    parse_layers,\n    apply_pca,\n    train_goal_classification_probe,\n    save_results,\n)\n\n\ndef parse_args():\n    p = argparse.ArgumentParser(\n        description=\"Goal classification probing for LIBERO-Goal shared-scene tasks\")\n    p.add_argument(\"--features_dir\", required=True,\n                   help=\"Directory with per-task HDF5 feature files\")\n    p.add_argument(\"--output_dir\", required=True,\n                   help=\"Directory to save probe results\")\n    p.add_argument(\"--probe_type\", default=\"goal_classification\",\n                   help=\"(fixed) goal_classification\")\n    p.add_argument(\"--data_dir\",\n                   default=\"/root/autodl-tmp/vla-ssd/data/libero/libero_goal/\",\n                   help=\"LIBERO raw data directory (reserved for future use)\")\n    p.add_argument(\"--aggregation\", default=\"last_preaction\",\n                   choices=[\"last_preaction\", \"image_mean\"],\n                   help=\"Token aggregation strategy (default: last_preaction)\")\n    p.add_argument(\"--layers\", default=None,\n                   help=\"Layer range '0-32' or list '0,5,10'. Default: all\")\n    p.add_argument(\"--pca_dim\", type=int, default=None,\n                   help=\"PCA reduce features to N dims before probe\")\n    p.add_argument(\"--seed\", type=int, default=42)\n    p.add_argument(\"--batch_size\", type=int, default=256)\n    p.add_argument(\"--lr\", type=float, default=1e-3)\n    p.add_argument(\"--epochs\", type=int, default=50)\n    p.add_argument(\"--patience\", type=int, default=5)\n    p.add_argument(\"--gpu\", type=int, default=0)\n    p.add_argument(\"--shuffle_labels\", action=\"store_true\",\n                   help=\"Permutation test: randomly shuffle goal labels\")\n    return p.parse_args()\n\n\ndef run_goal_probe(args, device):\n    \"\"\"Per-layer goal classification with per-trajectory train/val split.\"\"\"\n    traj_metas, n_layers, hidden_dim = scan_features(\n        args.features_dir, args.aggregation)\n    layers = parse_layers(args.layers, n_layers - 1)\n\n    task_names = sorted(set(m[\"task\"] for m in traj_metas))\n    task_to_idx = {t: i for i, t in enumerate(task_names)}\n    n_classes = len(task_names)\n    chance = 1.0 / n_classes\n\n    train_ids, val_ids = split_by_task(traj_metas)\n\n    # Report class balance\n    train_counts = {}\n    val_counts = {}\n    for idx in train_ids:\n        t = traj_metas[idx][\"task\"]\n        train_counts[t] = train_counts.get(t, 0) + 1\n    for idx in val_ids:\n        t = traj_metas[idx][\"task\"]\n        val_counts[t] = val_counts.get(t, 0) + 1\n\n    print(f\"Features: {len(traj_metas)} trajs, {n_layers} layers, dim={hidden_dim}\")\n    print(f\"Tasks ({n_classes}):\")\n    for t in task_names:\n        print(f\"  [{task_to_idx[t]}] {t}  \"\n              f\"(train={train_counts.get(t,0)}, val={val_counts.get(t,0)} trajs)\")\n    print(f\"Chance level: {chance:.4f} ({n_classes}-way)\")\n    print(f\"Split: {len(train_ids)} train / {len(val_ids)} val trajs\")\n    if args.shuffle_labels:\n        print(\"** PERMUTATION TEST: goal labels will be shuffled **\")\n\n    results = {}\n    for li, layer in enumerate(layers):\n        print(f\"\\n[Layer {layer}] ({li+1}/{len(layers)})\", flush=True)\n        t0 = time.time()\n\n        train_feats = load_layer_features(traj_metas, train_ids, layer)\n        val_feats = load_layer_features(traj_metas, val_ids, layer)\n\n        def flatten(feats, ids):\n            Xs, Ys = [], []\n            for feat, idx in zip(feats, ids):\n                label = task_to_idx[traj_metas[idx][\"task\"]]\n                T = feat.shape[0]\n                Xs.append(torch.from_numpy(feat))\n                Ys.append(torch.full((T,), label, dtype=torch.long))\n            return torch.cat(Xs), torch.cat(Ys)\n\n        X_tr, y_tr = flatten(train_feats, train_ids)\n        X_val, y_val = flatten(val_feats, val_ids)\n        del train_feats, val_feats\n\n        if args.shuffle_labels:\n            perm = torch.randperm(len(y_tr))\n            y_tr = y_tr[perm]\n\n        probe_dim = hidden_dim\n        pca_info = None\n        if args.pca_dim is not None:\n            X_tr, X_val, pca_info = apply_pca(X_tr, X_val, args.pca_dim)\n            probe_dim = args.pca_dim\n            print(f\"  PCA {hidden_dim} -> {args.pca_dim}: \"\n                  f\"{pca_info['cumulative_variance_ratio']:.4f} variance retained\")\n\n        print(f\"  Samples: {len(X_tr)} train / {len(X_val)} val\")\n        met = train_goal_classification_probe(\n            X_tr, y_tr, X_val, y_val, probe_dim, n_classes, args, device)\n        met[\"layer\"] = layer\n        met[\"task_names\"] = task_names\n        met[\"n_classes\"] = n_classes\n        met[\"chance_level\"] = chance\n        met[\"shuffle_labels\"] = args.shuffle_labels\n        if pca_info is not None:\n            met[\"pca_dim\"] = args.pca_dim\n            met[\"pca_info\"] = pca_info\n        results[layer] = met\n\n        delta = met[\"accuracy\"] - chance\n        print(f\"  acc={met['accuracy']:.4f} (Δchance={delta:+.4f})  \"\n              f\"F1={met['macro_f1']:.4f}  ep={met['epochs_trained']}  \"\n              f\"{time.time()-t0:.1f}s\")\n\n    return results\n\n\ndef main():\n    args = parse_args()\n    torch.manual_seed(args.seed)\n    np.random.seed(args.seed)\n    device = torch.device(\n        f\"cuda:{args.gpu}\" if torch.cuda.is_available() else \"cpu\")\n\n    if args.pca_dim is not None:\n        args.output_dir = args.output_dir.rstrip(\"/\") + f\"_pca{args.pca_dim}\"\n\n    print(f\"=== Goal Classification Probe | device={device} ===\")\n    print(f\"  features: {args.features_dir}\")\n    print(f\"  output:   {args.output_dir}\")\n    print(f\"  aggregation: {args.aggregation}\")\n\n    results = run_goal_probe(args, device)\n    save_results(results, args.output_dir, \"goal_classification\")\n\n    if results:\n        best = max(results, key=lambda k: results[k][\"accuracy\"])\n        chance = results[best][\"chance_level\"]\n        print(f\"\\n{'='*60}\")\n        print(f\"Best layer: {best}\")\n        print(f\"  accuracy:  {results[best]['accuracy']:.4f}  \"\n              f\"(Δchance = {results[best]['accuracy']-chance:+.4f})\")\n        print(f\"  macro F1:  {results[best]['macro_f1']:.4f}\")\n        print(f\"  chance:    {chance:.4f}\")\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT_EOF\necho \"train_goal_probe.py written: $(wc -l < /root/vla-ssd/scripts/train_goal_probe.py) lines\""
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-15T16:58:12.279914+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"train_goal_probe.py written: 205 lines\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-15T16:58:12.280202+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19183",
  "command": "cat > /root/vla-ssd/scripts/analyze_goal_results.py << 'SCRIPT_EOF'\n\"\"\"analyze_goal_results.py — Compare goal classification probes: trained vs untrained vs DINO.\n\nReads goal_classification/summary.json from each model's results directory.\nEvaluates three verdicts:\n  G1: peak trained accuracy > chance + 20pp  (hidden states encode goal)\n  G2: Δacc(trained−untrained) > 10pp in ≥5 layers  (training improves discriminability)\n  G3: trained peak accuracy > DINO peak accuracy  (VLA > vision-only baseline)\n\nOutput: markdown summary to stdout (or file), plus machine-readable JSON.\n\nUsage:\n  python analyze_goal_results.py \\\n    --trained_dir /root/autodl-tmp/vla-ssd/results/trained_libero_goal/ \\\n    --untrained_dir /root/autodl-tmp/vla-ssd/results/untrained_libero_goal/ \\\n    --dino_dir /root/autodl-tmp/vla-ssd/results/dinov2_libero_goal/\n\n  # Save to file:\n  python analyze_goal_results.py \\\n    --trained_dir ... --untrained_dir ... --dino_dir ... \\\n    --output /root/autodl-tmp/vla-ssd/results/goal_analysis.md\n\"\"\"\n\nimport argparse\nimport json\nimport os\nimport sys\n\n\ndef load_summary(result_dir):\n    \"\"\"Load goal_classification summary.json.\"\"\"\n    path = os.path.join(result_dir, \"goal_classification\", \"summary.json\")\n    if not os.path.exists(path):\n        return None\n    with open(path) as f:\n        return json.load(f)\n\n\ndef get_layer_accuracies(summary):\n    \"\"\"Extract {layer_int: accuracy} from summary.\"\"\"\n    accs = {}\n    abl = summary.get(\"accuracy_by_layer\", {})\n    if abl:\n        for k, v in abl.items():\n            accs[int(k)] = v\n        return accs\n    for k, v in summary.get(\"results\", {}).items():\n        if isinstance(v, dict) and \"accuracy\" in v:\n            accs[int(k)] = v[\"accuracy\"]\n    return accs\n\n\ndef get_layer_f1s(summary):\n    \"\"\"Extract {layer_int: macro_f1} from summary.\"\"\"\n    f1s = {}\n    for k, v in summary.get(\"results\", {}).items():\n        if isinstance(v, dict) and \"macro_f1\" in v:\n            f1s[int(k)] = v[\"macro_f1\"]\n    return f1s\n\n\ndef pct(v):\n    \"\"\"Format as percentage string.\"\"\"\n    return f\"{v*100:.1f}%\"\n\n\ndef parse_args():\n    p = argparse.ArgumentParser(\n        description=\"Analyze goal classification probe results across models\")\n    p.add_argument(\"--trained_dir\", required=True,\n                   help=\"Results dir for trained VLA\")\n    p.add_argument(\"--untrained_dir\", default=None,\n                   help=\"Results dir for untrained VLA\")\n    p.add_argument(\"--dino_dir\", default=None,\n                   help=\"Results dir for DINO-V2\")\n    p.add_argument(\"--output\", default=None,\n                   help=\"Output markdown file (default: stdout)\")\n    p.add_argument(\"--chance\", type=float, default=None,\n                   help=\"Override chance level (default: infer from n_classes)\")\n    p.add_argument(\"--g1_margin\", type=float, default=0.20,\n                   help=\"G1: required margin above chance (default: 0.20)\")\n    p.add_argument(\"--g2_margin\", type=float, default=0.10,\n                   help=\"G2: per-layer Δacc threshold (default: 0.10)\")\n    p.add_argument(\"--g2_min_layers\", type=int, default=5,\n                   help=\"G2: minimum layers exceeding threshold (default: 5)\")\n    return p.parse_args()\n\n\ndef main():\n    args = parse_args()\n\n    # Load results\n    models = {}\n    for name, path in [(\"trained\", args.trained_dir),\n                        (\"untrained\", args.untrained_dir),\n                        (\"dinov2\", args.dino_dir)]:\n        if path is None:\n            continue\n        s = load_summary(path)\n        if s is None:\n            print(f\"WARNING: no goal_classification/summary.json in {path}\",\n                  file=sys.stderr)\n            continue\n        models[name] = s\n\n    if \"trained\" not in models:\n        print(\"ERROR: trained results required.\", file=sys.stderr)\n        sys.exit(1)\n\n    trained = models[\"trained\"]\n\n    # Infer chance level\n    n_classes = None\n    task_names = None\n    for v in trained.get(\"results\", {}).values():\n        if isinstance(v, dict):\n            if \"n_classes\" in v:\n                n_classes = v[\"n_classes\"]\n            if \"task_names\" in v:\n                task_names = v[\"task_names\"]\n            if n_classes and task_names:\n                break\n\n    chance = args.chance if args.chance is not None else (1.0 / n_classes if n_classes else 0.1)\n\n    # Per-layer data\n    accs = {name: get_layer_accuracies(s) for name, s in models.items()}\n    f1s = {name: get_layer_f1s(s) for name, s in models.items()}\n\n    peaks = {name: max(a.values()) if a else 0.0 for name, a in accs.items()}\n    peak_layers = {}\n    for name, a in accs.items():\n        if a:\n            peak_layers[name] = max(a, key=a.get)\n\n    model_names = [n for n in [\"trained\", \"untrained\", \"dinov2\"] if n in accs]\n    all_layers = sorted(set().union(*[set(a.keys()) for a in accs.values()]))\n\n    # ---- Build markdown report ----\n    lines = []\n    lines.append(\"# Goal Classification Probe — LIBERO-Goal Analysis\\n\")\n\n    # Metadata\n    lines.append(f\"**Tasks**: {n_classes or '?'}-way classification  \")\n    lines.append(f\"**Chance level**: {pct(chance)}  \")\n    lines.append(f\"**Models**: {', '.join(model_names)}\")\n    if task_names:\n        lines.append(\"\")\n        for i, t in enumerate(task_names):\n            lines.append(f\"  {i}. {t}\")\n    lines.append(\"\")\n\n    # Per-layer accuracy table\n    lines.append(\"## Per-Layer Accuracy\\n\")\n    has_delta = \"trained\" in accs and \"untrained\" in accs\n\n    header_cols = [\"Layer\"] + model_names\n    if has_delta:\n        header_cols.append(\"Δ(tr−untr)\")\n    lines.append(\"| \" + \" | \".join(header_cols) + \" |\")\n    lines.append(\"|\" + \"|\".join([\"------:\" for _ in header_cols]) + \"|\")\n\n    delta_above_threshold = 0\n    per_layer_delta = {}\n    for layer in all_layers:\n        cols = [str(layer)]\n        for name in model_names:\n            v = accs[name].get(layer)\n            cols.append(pct(v) if v is not None else \"—\")\n        if has_delta:\n            tr = accs[\"trained\"].get(layer)\n            un = accs[\"untrained\"].get(layer)\n            if tr is not None and un is not None:\n                d = tr - un\n                per_layer_delta[layer] = d\n                if d > args.g2_margin:\n                    delta_above_threshold += 1\n                cols.append(f\"{d*100:+.1f}pp\")\n            else:\n                cols.append(\"—\")\n        lines.append(\"| \" + \" | \".join(cols) + \" |\")\n    lines.append(\"\")\n\n    # Peak summary\n    lines.append(\"## Peak Accuracy\\n\")\n    lines.append(\"| Model | Peak Acc | Best Layer | Macro F1 |\")\n    lines.append(\"|-------|--------:|----------:|--------:|\")\n    for name in model_names:\n        bl = peak_layers.get(name, \"?\")\n        pa = peaks.get(name, 0)\n        f1_at_peak = f1s.get(name, {}).get(bl, 0) if isinstance(bl, int) else 0\n        lines.append(f\"| {name} | {pct(pa)} | {bl} | {pct(f1_at_peak)} |\")\n    lines.append(\"\")\n\n    # ---- Verdicts ----\n    lines.append(\"## Verdicts\\n\")\n\n    # G1\n    g1_threshold = chance + args.g1_margin\n    g1_val = peaks.get(\"trained\", 0)\n    g1_pass = g1_val > g1_threshold\n    lines.append(f\"### G1: Trained VLA encodes goal information\")\n    lines.append(f\"- Criterion: peak trained acc > chance + {int(args.g1_margin*100)}pp \"\n                 f\"= {pct(g1_threshold)}\")\n    lines.append(f\"- Result: {pct(g1_val)} {'>' if g1_pass else '≤'} {pct(g1_threshold)}\")\n    lines.append(f\"- **{'PASS ✓' if g1_pass else 'FAIL ✗'}**\\n\")\n\n    # G2\n    if \"untrained\" in accs:\n        g2_pass = delta_above_threshold >= args.g2_min_layers\n        lines.append(f\"### G2: Training improves goal discriminability\")\n        lines.append(f\"- Criterion: Δacc(trained−untrained) > {int(args.g2_margin*100)}pp \"\n                     f\"in ≥{args.g2_min_layers} layers\")\n        lines.append(f\"- Result: {delta_above_threshold}/{len(all_layers)} layers exceed threshold\")\n        if per_layer_delta:\n            mean_delta = sum(per_layer_delta.values()) / len(per_layer_delta)\n            lines.append(f\"- Mean Δacc across layers: {mean_delta*100:+.1f}pp\")\n        lines.append(f\"- **{'PASS ✓' if g2_pass else 'FAIL ✗'}**\\n\")\n    else:\n        g2_pass = None\n        lines.append(\"### G2: Training improves goal discriminability\")\n        lines.append(\"- **PENDING** (untrained results not available)\\n\")\n\n    # G3\n    if \"dinov2\" in peaks:\n        g3_pass = peaks[\"trained\"] > peaks[\"dinov2\"]\n        gap = peaks[\"trained\"] - peaks[\"dinov2\"]\n        lines.append(f\"### G3: Trained VLA > DINO vision-only baseline\")\n        lines.append(f\"- Trained peak: {pct(peaks['trained'])}\")\n        lines.append(f\"- DINO peak: {pct(peaks['dinov2'])}\")\n        lines.append(f\"- Gap: {gap*100:+.1f}pp\")\n        lines.append(f\"- **{'PASS ✓' if g3_pass else 'FAIL ✗'}**\\n\")\n    else:\n        g3_pass = None\n        lines.append(\"### G3: Trained VLA > DINO vision-only baseline\")\n        lines.append(\"- **PENDING** (DINO results not available)\\n\")\n\n    # Overall\n    lines.append(\"## Summary\\n\")\n    verdicts = {\"G1\": g1_pass, \"G2\": g2_pass, \"G3\": g3_pass}\n    for g, v in verdicts.items():\n        tag = \"PASS\" if v else (\"FAIL\" if v is False else \"PENDING\")\n        lines.append(f\"- **{g}**: {tag}\")\n    lines.append(\"\")\n\n    all_done = all(v is not None for v in verdicts.values())\n    all_pass = all(v is True for v in verdicts.values())\n    if all_done:\n        if all_pass:\n            lines.append(\"> **Conclusion**: All gates passed. Trained VLA hidden states \"\n                         \"encode instruction-conditioned goal information beyond what \"\n                         \"vision alone provides.\")\n        else:\n            failed = [g for g, v in verdicts.items() if not v]\n            lines.append(f\"> **Conclusion**: Gates {', '.join(failed)} failed. \"\n                         \"See per-layer table for diagnostic details.\")\n    else:\n        pending = [g for g, v in verdicts.items() if v is None]\n        lines.append(f\"> **Status**: Waiting for {', '.join(pending)} results.\")\n\n    report = \"\\n\".join(lines)\n\n    # Output\n    if args.output:\n        out_dir = os.path.dirname(args.output)\n        if out_dir:\n            os.makedirs(out_dir, exist_ok=True)\n        with open(args.output, \"w\") as f:\n            f.write(report + \"\\n\")\n        print(f\"Report saved to {args.output}\")\n    else:\n        print(report)\n\n    # Machine-readable JSON\n    json_out = {\n        \"chance_level\": chance,\n        \"n_classes\": n_classes,\n        \"task_names\": task_names,\n        \"peaks\": peaks,\n        \"peak_layers\": {k: int(v) if isinstance(v, int) else v\n                        for k, v in peak_layers.items()},\n        \"verdicts\": {k: v for k, v in verdicts.items()},\n        \"g1_threshold\": g1_threshold,\n        \"g2_layers_above\": delta_above_threshold if has_delta else None,\n        \"per_layer_accuracy\": {\n            name: {str(k): v for k, v in a.items()}\n            for name, a in accs.items()\n        },\n        \"per_layer_delta\": {str(k): v for k, v in per_layer_delta.items()},\n    }\n\n    json_path = args.output.replace(\".md\", \".json\") if args.output else None\n    if json_path:\n        with open(json_path, \"w\") as f:\n            json.dump(json_out, f, indent=2)\n        print(f\"JSON saved to {json_path}\")\n    else:\n        print(\"\\n--- Machine-readable JSON ---\")\n        print(json.dumps(json_out, indent=2))\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT_EOF\necho \"analyze_goal_results.py written: $(wc -l < /root/vla-ssd/scripts/analyze_goal_results.py) lines\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat > /root/vla-ssd/scripts/analyze_goal_results.py << 'SCRIPT_EOF'\n\"\"\"analyze_goal_results.py — Compare goal classification probes: trained vs untrained vs DINO.\n\nReads goal_classification/summary.json from each model's results directory.\nEvaluates three verdicts:\n  G1: peak trained accuracy > chance + 20pp  (hidden states encode goal)\n  G2: Δacc(trained−untrained) > 10pp in ≥5 layers  (training improves discriminability)\n  G3: trained peak accuracy > DINO peak accuracy  (VLA > vision-only baseline)\n\nOutput: markdown summary to stdout (or file), plus machine-readable JSON.\n\nUsage:\n  python analyze_goal_results.py \\\n    --trained_dir /root/autodl-tmp/vla-ssd/results/trained_libero_goal/ \\\n    --untrained_dir /root/autodl-tmp/vla-ssd/results/untrained_libero_goal/ \\\n    --dino_dir /root/autodl-tmp/vla-ssd/results/dinov2_libero_goal/\n\n  # Save to file:\n  python analyze_goal_results.py \\\n    --trained_dir ... --untrained_dir ... --dino_dir ... \\\n    --output /root/autodl-tmp/vla-ssd/results/goal_analysis.md\n\"\"\"\n\nimport argparse\nimport json\nimport os\nimport sys\n\n\ndef load_summary(result_dir):\n    \"\"\"Load goal_classification summary.json.\"\"\"\n    path = os.path.join(result_dir, \"goal_classification\", \"summary.json\")\n    if not os.path.exists(path):\n        return None\n    with open(path) as f:\n        return json.load(f)\n\n\ndef get_layer_accuracies(summary):\n    \"\"\"Extract {layer_int: accuracy} from summary.\"\"\"\n    accs = {}\n    abl = summary.get(\"accuracy_by_layer\", {})\n    if abl:\n        for k, v in abl.items():\n            accs[int(k)] = v\n        return accs\n    for k, v in summary.get(\"results\", {}).items():\n        if isinstance(v, dict) and \"accuracy\" in v:\n            accs[int(k)] = v[\"accuracy\"]\n    return accs\n\n\ndef get_layer_f1s(summary):\n    \"\"\"Extract {layer_int: macro_f1} from summary.\"\"\"\n    f1s = {}\n    for k, v in summary.get(\"results\", {}).items():\n        if isinstance(v, dict) and \"macro_f1\" in v:\n            f1s[int(k)] = v[\"macro_f1\"]\n    return f1s\n\n\ndef pct(v):\n    \"\"\"Format as percentage string.\"\"\"\n    return f\"{v*100:.1f}%\"\n\n\ndef parse_args():\n    p = argparse.ArgumentParser(\n        description=\"Analyze goal classification probe results across models\")\n    p.add_argument(\"--trained_dir\", required=True,\n                   help=\"Results dir for trained VLA\")\n    p.add_argument(\"--untrained_dir\", default=None,\n                   help=\"Results dir for untrained VLA\")\n    p.add_argument(\"--dino_dir\", default=None,\n                   help=\"Results dir for DINO-V2\")\n    p.add_argument(\"--output\", default=None,\n                   help=\"Output markdown file (default: stdout)\")\n    p.add_argument(\"--chance\", type=float, default=None,\n                   help=\"Override chance level (default: infer from n_classes)\")\n    p.add_argument(\"--g1_margin\", type=float, default=0.20,\n                   help=\"G1: required margin above chance (default: 0.20)\")\n    p.add_argument(\"--g2_margin\", type=float, default=0.10,\n                   help=\"G2: per-layer Δacc threshold (default: 0.10)\")\n    p.add_argument(\"--g2_min_layers\", type=int, default=5,\n                   help=\"G2: minimum layers exceeding threshold (default: 5)\")\n    return p.parse_args()\n\n\ndef main():\n    args = parse_args()\n\n    # Load results\n    models = {}\n    for name, path in [(\"trained\", args.trained_dir),\n                        (\"untrained\", args.untrained_dir),\n                        (\"dinov2\", args.dino_dir)]:\n        if path is None:\n            continue\n        s = load_summary(path)\n        if s is None:\n            print(f\"WARNING: no goal_classification/summary.json in {path}\",\n                  file=sys.stderr)\n            continue\n        models[name] = s\n\n    if \"trained\" not in models:\n        print(\"ERROR: trained results required.\", file=sys.stderr)\n        sys.exit(1)\n\n    trained = models[\"trained\"]\n\n    # Infer chance level\n    n_classes = None\n    task_names = None\n    for v in trained.get(\"results\", {}).values():\n        if isinstance(v, dict):\n            if \"n_classes\" in v:\n                n_classes = v[\"n_classes\"]\n            if \"task_names\" in v:\n                task_names = v[\"task_names\"]\n            if n_classes and task_names:\n                break\n\n    chance = args.chance if args.chance is not None else (1.0 / n_classes if n_classes else 0.1)\n\n    # Per-layer data\n    accs = {name: get_layer_accuracies(s) for name, s in models.items()}\n    f1s = {name: get_layer_f1s(s) for name, s in models.items()}\n\n    peaks = {name: max(a.values()) if a else 0.0 for name, a in accs.items()}\n    peak_layers = {}\n    for name, a in accs.items():\n        if a:\n            peak_layers[name] = max(a, key=a.get)\n\n    model_names = [n for n in [\"trained\", \"untrained\", \"dinov2\"] if n in accs]\n    all_layers = sorted(set().union(*[set(a.keys()) for a in accs.values()]))\n\n    # ---- Build markdown report ----\n    lines = []\n    lines.append(\"# Goal Classification Probe — LIBERO-Goal Analysis\\n\")\n\n    # Metadata\n    lines.append(f\"**Tasks**: {n_classes or '?'}-way classification  \")\n    lines.append(f\"**Chance level**: {pct(chance)}  \")\n    lines.append(f\"**Models**: {', '.join(model_names)}\")\n    if task_names:\n        lines.append(\"\")\n        for i, t in enumerate(task_names):\n            lines.append(f\"  {i}. {t}\")\n    lines.append(\"\")\n\n    # Per-layer accuracy table\n    lines.append(\"## Per-Layer Accuracy\\n\")\n    has_delta = \"trained\" in accs and \"untrained\" in accs\n\n    header_cols = [\"Layer\"] + model_names\n    if has_delta:\n        header_cols.append(\"Δ(tr−untr)\")\n    lines.append(\"| \" + \" | \".join(header_cols) + \" |\")\n    lines.append(\"|\" + \"|\".join([\"------:\" for _ in header_cols]) + \"|\")\n\n    delta_above_threshold = 0\n    per_layer_delta = {}\n    for layer in all_layers:\n        cols = [str(layer)]\n        for name in model_names:\n            v = accs[name].get(layer)\n            cols.append(pct(v) if v is not None else \"—\")\n        if has_delta:\n            tr = accs[\"trained\"].get(layer)\n            un = accs[\"untrained\"].get(layer)\n            if tr is not None and un is not None:\n                d = tr - un\n                per_layer_delta[layer] = d\n                if d > args.g2_margin:\n                    delta_above_threshold += 1\n                cols.append(f\"{d*100:+.1f}pp\")\n            else:\n                cols.append(\"—\")\n        lines.append(\"| \" + \" | \".join(cols) + \" |\")\n    lines.append(\"\")\n\n    # Peak summary\n    lines.append(\"## Peak Accuracy\\n\")\n    lines.append(\"| Model | Peak Acc | Best Layer | Macro F1 |\")\n    lines.append(\"|-------|--------:|----------:|--------:|\")\n    for name in model_names:\n        bl = peak_layers.get(name, \"?\")\n        pa = peaks.get(name, 0)\n        f1_at_peak = f1s.get(name, {}).get(bl, 0) if isinstance(bl, int) else 0\n        lines.append(f\"| {name} | {pct(pa)} | {bl} | {pct(f1_at_peak)} |\")\n    lines.append(\"\")\n\n    # ---- Verdicts ----\n    lines.append(\"## Verdicts\\n\")\n\n    # G1\n    g1_threshold = chance + args.g1_margin\n    g1_val = peaks.get(\"trained\", 0)\n    g1_pass = g1_val > g1_threshold\n    lines.append(f\"### G1: Trained VLA encodes goal information\")\n    lines.append(f\"- Criterion: peak trained acc > chance + {int(args.g1_margin*100)}pp \"\n                 f\"= {pct(g1_threshold)}\")\n    lines.append(f\"- Result: {pct(g1_val)} {'>' if g1_pass else '≤'} {pct(g1_threshold)}\")\n    lines.append(f\"- **{'PASS ✓' if g1_pass else 'FAIL ✗'}**\\n\")\n\n    # G2\n    if \"untrained\" in accs:\n        g2_pass = delta_above_threshold >= args.g2_min_layers\n        lines.append(f\"### G2: Training improves goal discriminability\")\n        lines.append(f\"- Criterion: Δacc(trained−untrained) > {int(args.g2_margin*100)}pp \"\n                     f\"in ≥{args.g2_min_layers} layers\")\n        lines.append(f\"- Result: {delta_above_threshold}/{len(all_layers)} layers exceed threshold\")\n        if per_layer_delta:\n            mean_delta = sum(per_layer_delta.values()) / len(per_layer_delta)\n            lines.append(f\"- Mean Δacc across layers: {mean_delta*100:+.1f}pp\")\n        lines.append(f\"- **{'PASS ✓' if g2_pass else 'FAIL ✗'}**\\n\")\n    else:\n        g2_pass = None\n        lines.append(\"### G2: Training improves goal discriminability\")\n        lines.append(\"- **PENDING** (untrained results not available)\\n\")\n\n    # G3\n    if \"dinov2\" in peaks:\n        g3_pass = peaks[\"trained\"] > peaks[\"dinov2\"]\n        gap = peaks[\"trained\"] - peaks[\"dinov2\"]\n        lines.append(f\"### G3: Trained VLA > DINO vision-only baseline\")\n        lines.append(f\"- Trained peak: {pct(peaks['trained'])}\")\n        lines.append(f\"- DINO peak: {pct(peaks['dinov2'])}\")\n        lines.append(f\"- Gap: {gap*100:+.1f}pp\")\n        lines.append(f\"- **{'PASS ✓' if g3_pass else 'FAIL ✗'}**\\n\")\n    else:\n        g3_pass = None\n        lines.append(\"### G3: Trained VLA > DINO vision-only baseline\")\n        lines.append(\"- **PENDING** (DINO results not available)\\n\")\n\n    # Overall\n    lines.append(\"## Summary\\n\")\n    verdicts = {\"G1\": g1_pass, \"G2\": g2_pass, \"G3\": g3_pass}\n    for g, v in verdicts.items():\n        tag = \"PASS\" if v else (\"FAIL\" if v is False else \"PENDING\")\n        lines.append(f\"- **{g}**: {tag}\")\n    lines.append(\"\")\n\n    all_done = all(v is not None for v in verdicts.values())\n    all_pass = all(v is True for v in verdicts.values())\n    if all_done:\n        if all_pass:\n            lines.append(\"> **Conclusion**: All gates passed. Trained VLA hidden states \"\n                         \"encode instruction-conditioned goal information beyond what \"\n                         \"vision alone provides.\")\n        else:\n            failed = [g for g, v in verdicts.items() if not v]\n            lines.append(f\"> **Conclusion**: Gates {', '.join(failed)} failed. \"\n                         \"See per-layer table for diagnostic details.\")\n    else:\n        pending = [g for g, v in verdicts.items() if v is None]\n        lines.append(f\"> **Status**: Waiting for {', '.join(pending)} results.\")\n\n    report = \"\\n\".join(lines)\n\n    # Output\n    if args.output:\n        out_dir = os.path.dirname(args.output)\n        if out_dir:\n            os.makedirs(out_dir, exist_ok=True)\n        with open(args.output, \"w\") as f:\n            f.write(report + \"\\n\")\n        print(f\"Report saved to {args.output}\")\n    else:\n        print(report)\n\n    # Machine-readable JSON\n    json_out = {\n        \"chance_level\": chance,\n        \"n_classes\": n_classes,\n        \"task_names\": task_names,\n        \"peaks\": peaks,\n        \"peak_layers\": {k: int(v) if isinstance(v, int) else v\n                        for k, v in peak_layers.items()},\n        \"verdicts\": {k: v for k, v in verdicts.items()},\n        \"g1_threshold\": g1_threshold,\n        \"g2_layers_above\": delta_above_threshold if has_delta else None,\n        \"per_layer_accuracy\": {\n            name: {str(k): v for k, v in a.items()}\n            for name, a in accs.items()\n        },\n        \"per_layer_delta\": {str(k): v for k, v in per_layer_delta.items()},\n    }\n\n    json_path = args.output.replace(\".md\", \".json\") if args.output else None\n    if json_path:\n        with open(json_path, \"w\") as f:\n            json.dump(json_out, f, indent=2)\n        print(f\"JSON saved to {json_path}\")\n    else:\n        print(\"\\n--- Machine-readable JSON ---\")\n        print(json.dumps(json_out, indent=2))\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT_EOF\necho \"analyze_goal_results.py written: $(wc -l < /root/vla-ssd/scripts/analyze_goal_results.py) lines\""
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-15T16:58:12.280581+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"analyze_goal_results.py written: 302 lines\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-15T16:58:12.280792+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19183",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/train_goal_probe.py --help"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19183",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/train_goal_probe.py --help"
  }
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-15T16:58:12.280995+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19183",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/analyze_goal_results.py --help"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19183",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/analyze_goal_results.py --help"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-15T16:58:12.281215+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"usage: train_goal_probe.py [-h] --features_dir FEATURES_DIR --output_dir\\n                           OUTPUT_DIR [--probe_type PROBE_TYPE]\\n                           [--data_dir DATA_DIR]\\n                           [--aggregation {last_preaction,image_mean}]\\n                           [--layers LAYERS] [--pca_dim PCA_DIM] [--seed SEED]\\n                           [--batch_size BATCH_SIZE] [--lr LR]\\n                           [--epochs EPOCHS] [--patience PATIENCE] [--gpu GPU]\\n                           [--shuffle_labels]\\n\\nGoal classification probing for LIBERO-Goal shared-scene tasks\\n\\noptions:\\n  -h, --help            show this help message and exit\\n  --features_dir FEATURES_DIR\\n                        Directory with per-task HDF5 feature files\\n  --output_dir OUTPUT_DIR\\n                        Directory to save probe results\\n  --probe_type PROBE_TYPE\\n                        (fixed) goal_classification\\n  --data_dir DATA_DIR   LIBERO raw data directory (reserved for future use)\\n  --aggregation {last_preaction,image_mean}\\n                        Token aggregation strategy (default: last_preaction)\\n  --layers LAYERS       Layer range '0-32' or list '0,5,10'. Default: all\\n  --pca_dim PCA_DIM     PCA reduce features to N dims before probe\\n  --seed SEED\\n  --batch_size BATCH_SIZE\\n  --lr LR\\n  --epochs EPOCHS\\n  --patience PATIENCE\\n  --gpu GPU\\n  --shuffle_labels      Permutation test: randomly shuffle goal labels\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.57}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-15T16:58:12.281439+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"usage: analyze_goal_results.py [-h] --trained_dir TRAINED_DIR\\n                               [--untrained_dir UNTRAINED_DIR]\\n                               [--dino_dir DINO_DIR] [--output OUTPUT]\\n                               [--chance CHANCE] [--g1_margin G1_MARGIN]\\n                               [--g2_margin G2_MARGIN]\\n                               [--g2_min_layers G2_MIN_LAYERS]\\n\\nAnalyze goal classification probe results across models\\n\\noptions:\\n  -h, --help            show this help message and exit\\n  --trained_dir TRAINED_DIR\\n                        Results dir for trained VLA\\n  --untrained_dir UNTRAINED_DIR\\n                        Results dir for untrained VLA\\n  --dino_dir DINO_DIR   Results dir for DINO-V2\\n  --output OUTPUT       Output markdown file (default: stdout)\\n  --chance CHANCE       Override chance level (default: infer from n_classes)\\n  --g1_margin G1_MARGIN\\n                        G1: required margin above chance (default: 0.20)\\n  --g2_margin G2_MARGIN\\n                        G2: per-layer Δacc threshold (default: 0.10)\\n  --g2_min_layers G2_MIN_LAYERS\\n                        G2: minimum layers exceeding threshold (default: 5)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.92}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_lg-instruction-probe_20260515T165250",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-15T16:58:12.281702+00:00_

两个脚本参数解析均通过。

---

## 报告

### LIBERO-Goal 数据结构

10 个任务共享同一 kitchen scene，50 demos/task：

| # | Task |
|---|------|
| 0 | open_the_middle_drawer_of_the_cabinet |
| 1 | open_the_top_drawer_and_put_the_bowl_inside |
| 2 | push_the_plate_to_the_front_of_the_stove |
| 3 | put_the_bowl_on_the_plate |
| 4 | put_the_bowl_on_the_stove |
| 5 | put_the_bowl_on_top_of_the_cabinet |
| 6 | put_the_cream_cheese_in_the_bowl |
| 7 | put_the_wine_bottle_on_the_rack |
| 8 | put_the_wine_bottle_on_top_of_the_cabinet |
| 9 | turn_on_the_stove |

特征格式与 LIBERO-10 相同。Chance level = 10%。

特征提取进度：trained 2/10, untrained 1/10, DINO 目录尚未创建。

### 代码设计决策

1. **`train_goal_probe.py`** — 复用 `train_probes.py` 的 `scan_features`, `split_by_task`, `load_layer_features`, `parse_layers`, `apply_pca`, `train_goal_classification_probe`, `save_results`。不重复实现基础设施，只添加 goal-specific 逻辑：
   - 类别平衡报告（每个 task 的 train/val trajectory 数）
   - Chance level 计算和 Δchance 输出
   - `--shuffle_labels` 排列检验（阴性对照）
   - 输出兼容现有 `save_results` 格式（per-layer JSON + summary.csv + summary.json）

2. **`analyze_goal_results.py`** — 独立脚本，无 torch 依赖。三级判定：
   - **G1**: peak acc > chance + 20pp → trained 编码了 goal
   - **G2**: Δacc(trained−untrained) > 10pp 在 ≥5 层 → 训练提升了区分度
   - **G3**: trained peak > DINO peak → VLA > 纯视觉
   - 阈值可通过 `--g1_margin`, `--g2_margin`, `--g2_min_layers` 调节
   - 同时输出 markdown 和 JSON

3. **与现有代码的关系**：服务器上已有 `train_instruction_probes.py`（带场景分组）和 `analyze_goal_probes.py`（简单 gate）。新脚本的区别：`train_goal_probe.py` 更轻量（不做场景分组，LIBERO-Goal 全部同场景所以不需要），`analyze_goal_results.py` 增加了 G1/G2/G3 三级判定和 per-layer delta 分析。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_lg-instruction-probe_20260515T165250"
}
```

</details>

---
