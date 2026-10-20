# code cross layer L8 ablation

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 0
- **Tool calls:** 16
- **Original source:** `logs/chats/worker_code_cross_layer_L8_ablation_20260518T133705.jsonl`
- **Structured JSON:** [`9837720173536451e7cd.json`](../../sessions/98/9837720173536451e7cd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

33 recorded events

### Tool call

_source line 1 · 2026-05-18T13:40:11.194487+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__register_artifact",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cross_layer_L8_ablation_20260518T133705",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__register_artifact",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-18T13:40:11.195001+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cross_layer_L8_ablation_20260518T133705",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T13:40:11.195316+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/vla-ssd/scripts/action_trajectory_analysis.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cross_layer_L8_ablation_20260518T133705",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/vla-ssd/scripts/action_trajectory_analysis.py"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-18T13:40:11.195548+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/vla-ssd/scripts/action_trajectory_control.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cross_layer_L8_ablation_20260518T133705",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/vla-ssd/scripts/action_trajectory_control.py"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-18T13:40:11.196005+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Open-loop action trajectory analysis: baseline vs L1-ablated on LIBERO demo observations.\\\"\\\"\\\"\\n\\nimport argparse\\nimport gc\\nimport glob\\nimport json\\nimport os\\nimport sys\\nimport time\\n\\nsys.path.insert(0, \\\"/root/autodl-tmp/LIBERO\\\")\\n\\nos.environ[\\\"MUJOCO_GL\\\"] = \\\"egl\\\"\\nos.environ[\\\"HDF5_USE_FILE_LOCKING\\\"] = \\\"FALSE\\\"\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nimport torch.nn as nn\\nimport torch.nn.functional as F\\nfrom PIL import Image\\nfrom scipy import stats\\n\\nnp.random.seed(42)\\ntorch.manual_seed(42)\\n\\n# ── Config ──────────────────────────────────────────────────────────────────\\nMODEL_PATH = \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"\\nUNNORM_KEY = \\\"bridge_orig\\\"\\nDATA_DIR = \\\"/root/autodl-tmp/vla-ssd/data/libero/libero_goal\\\"\\nRESULTS_DIR = \\\"/root/autodl-tmp/vla-ssd/results\\\"\\n\\nNUM_IMAGE_TOKENS = 256\\nINST_START = 1 + NUM_IMAGE_TOKENS\\n\\nINSTRUCTION_HEADS_24 = [\\n    0, 1, 2, 4, 7, 8, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20,\\n    22, 23, 25, 26, 27, 29, 30, 31,\\n]\\n\\nDIM_NAMES = [\\\"dx\\\", \\\"dy\\\", \\\"dz\\\", \\\"rx\\\", \\\"ry\\\", \\\"rz\\\", \\\"gripper\\\"]\\n\\n\\n# ── Model loading ───────────────────────────────────────────────────────────\\ndef load_model():\\n    from transformers import AutoModelForVision2Seq, AutoProcessor\\n\\n    processor = AutoProcessor.from_pretrained(MODEL_PATH, trust_remote_code=True)\\n    model = AutoModelForVision2Seq.from_pretrained(\\n        MODEL_PATH,\\n        torch_dtype=torch.bfloat16,\\n        trust_remote_code=True,\\n        low_cpu_mem_usage=True,\\n    ).to(\\\"cuda:0\\\").eval()\\n    return model, processor\\n\\n\\n# ── Manual autoregressive generation (bypasses generate() DynamicCache bug) ─\\ndef predict_action_with_logits(model, input_ids, pixel_values, unnorm_key):\\n    action_dim = model.get_action_dim(unnorm_key)\\n   
…[truncated 7113 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cross_layer_L8_ablation_20260518T133705",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-18T13:40:11.196480+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Open-loop action trajectory analysis: baseline vs L1-ablated on LIBERO demo observations.\\\"\\\"\\\"\\n\\nimport argparse\\nimport gc\\nimport glob\\nimport json\\nimport os\\nimport sys\\nimport time\\n\\nsys.path.insert(0, \\\"/root/autodl-tmp/LIBERO\\\")\\n\\nos.environ[\\\"MUJOCO_GL\\\"] = \\\"egl\\\"\\nos.environ[\\\"HDF5_USE_FILE_LOCKING\\\"] = \\\"FALSE\\\"\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nimport torch.nn as nn\\nimport torch.nn.functional as F\\nfrom PIL import Image\\nfrom scipy import stats\\n\\nnp.random.seed(42)\\ntorch.manual_seed(42)\\n\\n# ── Config ──────────────────────────────────────────────────────────────────\\nMODEL_PATH = \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"\\nUNNORM_KEY = \\\"bridge_orig\\\"\\nDATA_DIR = \\\"/root/autodl-tmp/vla-ssd/data/libero/libero_goal\\\"\\nRESULTS_DIR = \\\"/root/autodl-tmp/vla-ssd/results\\\"\\n\\nNUM_IMAGE_TOKENS = 256\\nINST_START = 1 + NUM_IMAGE_TOKENS\\n\\nCONTROL_HEADS_8 = [\\n    3, 5, 6, 9, 13, 21, 24, 28,\\n\\n]\\n\\nDIM_NAMES = [\\\"dx\\\", \\\"dy\\\", \\\"dz\\\", \\\"rx\\\", \\\"ry\\\", \\\"rz\\\", \\\"gripper\\\"]\\n\\n\\n# ── Model loading ───────────────────────────────────────────────────────────\\ndef load_model():\\n    from transformers import AutoModelForVision2Seq, AutoProcessor\\n\\n    processor = AutoProcessor.from_pretrained(MODEL_PATH, trust_remote_code=True)\\n    model = AutoModelForVision2Seq.from_pretrained(\\n        MODEL_PATH,\\n        torch_dtype=torch.bfloat16,\\n        trust_remote_code=True,\\n        low_cpu_mem_usage=True,\\n    ).to(\\\"cuda:0\\\").eval()\\n    return model, processor\\n\\n\\n# ── Manual autoregressive generation (bypasses generate() DynamicCache bug) ─\\ndef predict_action_with_logits(model, input_ids, pixel_values, unnorm_key):\\n    action_dim = model.get_action_dim(unnorm_key)\\n    if not torch.all(input_ids[:, -1] == 29871):\\n        input_ids = to
…[truncated 7117 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cross_layer_L8_ablation_20260518T133705",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-18T13:40:11.196809+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "head -200 /root/vla-ssd/scripts/action_trajectory_control.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cross_layer_L8_ablation_20260518T133705",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "head -200 /root/vla-ssd/scripts/action_trajectory_control.py"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-18T13:40:11.197064+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "head -200 /root/vla-ssd/scripts/action_trajectory_analysis.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cross_layer_L8_ablation_20260518T133705",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "head -200 /root/vla-ssd/scripts/action_trajectory_analysis.py"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-18T13:40:11.197459+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Open-loop action trajectory analysis: baseline vs L1-ablated on LIBERO demo observations.\\\"\\\"\\\"\\n\\nimport argparse\\nimport gc\\nimport glob\\nimport json\\nimport os\\nimport sys\\nimport time\\n\\nsys.path.insert(0, \\\"/root/autodl-tmp/LIBERO\\\")\\n\\nos.environ[\\\"MUJOCO_GL\\\"] = \\\"egl\\\"\\nos.environ[\\\"HDF5_USE_FILE_LOCKING\\\"] = \\\"FALSE\\\"\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nimport torch.nn as nn\\nimport torch.nn.functional as F\\nfrom PIL import Image\\nfrom scipy import stats\\n\\nnp.random.seed(42)\\ntorch.manual_seed(42)\\n\\n# ── Config ──────────────────────────────────────────────────────────────────\\nMODEL_PATH = \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"\\nUNNORM_KEY = \\\"bridge_orig\\\"\\nDATA_DIR = \\\"/root/autodl-tmp/vla-ssd/data/libero/libero_goal\\\"\\nRESULTS_DIR = \\\"/root/autodl-tmp/vla-ssd/results\\\"\\n\\nNUM_IMAGE_TOKENS = 256\\nINST_START = 1 + NUM_IMAGE_TOKENS\\n\\nCONTROL_HEADS_8 = [\\n    3, 5, 6, 9, 13, 21, 24, 28,\\n\\n]\\n\\nDIM_NAMES = [\\\"dx\\\", \\\"dy\\\", \\\"dz\\\", \\\"rx\\\", \\\"ry\\\", \\\"rz\\\", \\\"gripper\\\"]\\n\\n\\n# ── Model loading ───────────────────────────────────────────────────────────\\ndef load_model():\\n    from transformers import AutoModelForVision2Seq, AutoProcessor\\n\\n    processor = AutoProcessor.from_pretrained(MODEL_PATH, trust_remote_code=True)\\n    model = AutoModelForVision2Seq.from_pretrained(\\n        MODEL_PATH,\\n        torch_dtype=torch.bfloat16,\\n        trust_remote_code=True,\\n        low_cpu_mem_usage=True,\\n    ).to(\\\"cuda:0\\\").eval()\\n    return model, processor\\n\\n\\n# ── Manual autoregressive generation (bypasses generate() DynamicCache bug) ─\\ndef predict_action_with_logits(model, input_ids, pixel_values, unnorm_key):\\n    action_dim = model.get_action_dim(unnorm_key)\\n    if not torch.all(input_ids[:, -1] == 29871):\\n        input_ids = to
…[truncated 6286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cross_layer_L8_ablation_20260518T133705",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-18T13:40:11.197895+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Open-loop action trajectory analysis: baseline vs L1-ablated on LIBERO demo observations.\\\"\\\"\\\"\\n\\nimport argparse\\nimport gc\\nimport glob\\nimport json\\nimport os\\nimport sys\\nimport time\\n\\nsys.path.insert(0, \\\"/root/autodl-tmp/LIBERO\\\")\\n\\nos.environ[\\\"MUJOCO_GL\\\"] = \\\"egl\\\"\\nos.environ[\\\"HDF5_USE_FILE_LOCKING\\\"] = \\\"FALSE\\\"\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nimport torch.nn as nn\\nimport torch.nn.functional as F\\nfrom PIL import Image\\nfrom scipy import stats\\n\\nnp.random.seed(42)\\ntorch.manual_seed(42)\\n\\n# ── Config ──────────────────────────────────────────────────────────────────\\nMODEL_PATH = \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"\\nUNNORM_KEY = \\\"bridge_orig\\\"\\nDATA_DIR = \\\"/root/autodl-tmp/vla-ssd/data/libero/libero_goal\\\"\\nRESULTS_DIR = \\\"/root/autodl-tmp/vla-ssd/results\\\"\\n\\nNUM_IMAGE_TOKENS = 256\\nINST_START = 1 + NUM_IMAGE_TOKENS\\n\\nINSTRUCTION_HEADS_24 = [\\n    0, 1, 2, 4, 7, 8, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20,\\n    22, 23, 25, 26, 27, 29, 30, 31,\\n]\\n\\nDIM_NAMES = [\\\"dx\\\", \\\"dy\\\", \\\"dz\\\", \\\"rx\\\", \\\"ry\\\", \\\"rz\\\", \\\"gripper\\\"]\\n\\n\\n# ── Model loading ───────────────────────────────────────────────────────────\\ndef load_model():\\n    from transformers import AutoModelForVision2Seq, AutoProcessor\\n\\n    processor = AutoProcessor.from_pretrained(MODEL_PATH, trust_remote_code=True)\\n    model = AutoModelForVision2Seq.from_pretrained(\\n        MODEL_PATH,\\n        torch_dtype=torch.bfloat16,\\n        trust_remote_code=True,\\n        low_cpu_mem_usage=True,\\n    ).to(\\\"cuda:0\\\").eval()\\n    return model, processor\\n\\n\\n# ── Manual autoregressive generation (bypasses generate() DynamicCache bug) ─\\ndef predict_action_with_logits(model, input_ids, pixel_values, unnorm_key):\\n    action_dim = model.get_action_dim(unnorm_key)\\n   
…[truncated 6046 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cross_layer_L8_ablation_20260518T133705",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T13:40:11.198254+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "tail -n +200 /root/vla-ssd/scripts/action_trajectory_control.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cross_layer_L8_ablation_20260518T133705",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "tail -n +200 /root/vla-ssd/scripts/action_trajectory_control.py"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-18T13:40:11.198682+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    log_p = F.log_softmax(logits_p, dim=-1)\\n    log_q = F.log_softmax(logits_q, dim=-1)\\n    p = F.softmax(logits_p, dim=-1)\\n    kl = (p * (log_p - log_q)).sum(dim=-1)\\n    return kl.numpy()\\n\\n\\n# ── Helpers ─────────────────────────────────────────────────────────────────\\ndef get_task_files(n_tasks):\\n    hdf5_files = sorted(glob.glob(os.path.join(DATA_DIR, \\\"*.hdf5\\\")))\\n    return hdf5_files[:n_tasks]\\n\\n\\ndef get_language_instruction(hdf5_path):\\n    with h5py.File(hdf5_path, \\\"r\\\") as f:\\n        info = json.loads(f[\\\"data\\\"].attrs[\\\"problem_info\\\"])\\n    return info[\\\"language_instruction\\\"]\\n\\n\\ndef compute_task_metrics(task_b, task_a, task_b_ids, task_a_ids, task_kls):\\n    paired_mse = np.mean((task_b - task_a) ** 2, axis=1)\\n    t_res = stats.ttest_1samp(paired_mse, 0)\\n    cohens_d = np.mean(paired_mse) / (np.std(paired_mse, ddof=1) + 1e-12)\\n\\n    per_dim_shift = np.abs(task_b - task_a)\\n    token_div = np.mean(task_b_ids != task_a_ids)\\n\\n    return {\\n        \\\"paired_mse\\\": {\\n            \\\"mean\\\": float(np.mean(paired_mse)),\\n            \\\"std\\\": float(np.std(paired_mse)),\\n            \\\"t_stat\\\": float(t_res.statistic),\\n            \\\"p_value\\\": float(t_res.pvalue),\\n            \\\"cohens_d\\\": float(cohens_d),\\n        },\\n        \\\"per_dim_shift\\\": {\\n            \\\"means\\\": [float(x) for x in np.mean(per_dim_shift, axis=0)],\\n            \\\"stds\\\": [float(x) for x in np.std(per_dim_shift, axis=0)],\\n        },\\n        \\\"token_divergence_rate\\\": float(token_div),\\n        \\\"kl_divergence\\\": {\\n            \\\"mean\\\": float(np.mean(task_kls)),\\n            \\\"std\\\": float(np.std(task_kls)),\\n        },\\n        \\\"n_samples\\\": int(len(task_b)),\\n    }\\n\\n\\n# ── Main ────────────────────────────────────────────────────────────────────\\ndef main():\\n    parser = argparse.Arg
…[truncated 7191 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cross_layer_L8_ablation_20260518T133705",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T13:40:11.199016+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "head -n 340 /root/vla-ssd/scripts/action_trajectory_control.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cross_layer_L8_ablation_20260518T133705",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "head -n 340 /root/vla-ssd/scripts/action_trajectory_control.py"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-18T13:40:11.199438+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Open-loop action trajectory analysis: baseline vs L1-ablated on LIBERO demo observations.\\\"\\\"\\\"\\n\\nimport argparse\\nimport gc\\nimport glob\\nimport json\\nimport os\\nimport sys\\nimport time\\n\\nsys.path.insert(0, \\\"/root/autodl-tmp/LIBERO\\\")\\n\\nos.environ[\\\"MUJOCO_GL\\\"] = \\\"egl\\\"\\nos.environ[\\\"HDF5_USE_FILE_LOCKING\\\"] = \\\"FALSE\\\"\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nimport torch.nn as nn\\nimport torch.nn.functional as F\\nfrom PIL import Image\\nfrom scipy import stats\\n\\nnp.random.seed(42)\\ntorch.manual_seed(42)\\n\\n# ── Config ──────────────────────────────────────────────────────────────────\\nMODEL_PATH = \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"\\nUNNORM_KEY = \\\"bridge_orig\\\"\\nDATA_DIR = \\\"/root/autodl-tmp/vla-ssd/data/libero/libero_goal\\\"\\nRESULTS_DIR = \\\"/root/autodl-tmp/vla-ssd/results\\\"\\n\\nNUM_IMAGE_TOKENS = 256\\nINST_START = 1 + NUM_IMAGE_TOKENS\\n\\nCONTROL_HEADS_8 = [\\n    3, 5, 6, 9, 13, 21, 24, 28,\\n\\n]\\n\\nDIM_NAMES = [\\\"dx\\\", \\\"dy\\\", \\\"dz\\\", \\\"rx\\\", \\\"ry\\\", \\\"rz\\\", \\\"gripper\\\"]\\n\\n\\n# ── Model loading ───────────────────────────────────────────────────────────\\ndef load_model():\\n    from transformers import AutoModelForVision2Seq, AutoProcessor\\n\\n    processor = AutoProcessor.from_pretrained(MODEL_PATH, trust_remote_code=True)\\n    model = AutoModelForVision2Seq.from_pretrained(\\n        MODEL_PATH,\\n        torch_dtype=torch.bfloat16,\\n        trust_remote_code=True,\\n        low_cpu_mem_usage=True,\\n    ).to(\\\"cuda:0\\\").eval()\\n    return model, processor\\n\\n\\n# ── Manual autoregressive generation (bypasses generate() DynamicCache bug) ─\\ndef predict_action_with_logits(model, input_ids, pixel_values, unnorm_key):\\n    action_dim = model.get_action_dim(unnorm_key)\\n    if not torch.all(input_ids[:, -1] == 29871):\\n        input_ids = to
…[truncated 6954 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cross_layer_L8_ablation_20260518T133705",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-18T13:40:11.199870+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19183",
  "command": "cat > /root/vla-ssd/scripts/action_trajectory_L8_ablation.py << 'SCRIPT_EOF'\n\"\"\"Open-loop action trajectory analysis: baseline vs L8-full-ablation on LIBERO demo observations.\"\"\"\n\nimport argparse\nimport gc\nimport glob\nimport json\nimport os\nimport sys\nimport time\n\nsys.path.insert(0, \"/root/autodl-tmp/LIBERO\")\n\nos.environ[\"MUJOCO_GL\"] = \"egl\"\nos.environ[\"HDF5_USE_FILE_LOCKING\"] = \"FALSE\"\n\nimport h5py\nimport numpy as np\nimport torch\nimport torch.nn as nn\nimport torch.nn.functional as F\nfrom PIL import Image\nfrom scipy import stats\n\nnp.random.seed(42)\ntorch.manual_seed(42)\n\n# ── Config ──────────────────────────────────────────────────────────────────\nMODEL_PATH = \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\"\nUNNORM_KEY = \"bridge_orig\"\nDATA_DIR = \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal\"\nRESULTS_DIR = \"/root/autodl-tmp/vla-ssd/results\"\n\nLAYER_IDX = 8\nALL_HEADS = list(range(32))\n\nDIM_NAMES = [\"dx\", \"dy\", \"dz\", \"rx\", \"ry\", \"rz\", \"gripper\"]\n\n\n# ── Model loading ───────────────────────────────────────────────────────────\ndef load_model():\n    from transformers import AutoModelForVision2Seq, AutoProcessor\n\n    processor = AutoProcessor.from_pretrained(MODEL_PATH, trust_remote_code=True)\n    model = AutoModelForVision2Seq.from_pretrained(\n        MODEL_PATH,\n        torch_dtype=torch.bfloat16,\n        trust_remote_code=True,\n        low_cpu_mem_usage=True,\n    ).to(\"cuda:0\").eval()\n    return model, processor\n\n\n# ── Manual autoregressive generation (bypasses generate() DynamicCache bug) ─\ndef predict_action_with_logits(model, input_ids, pixel_values, unnorm_key):\n    action_dim = model.get_action_dim(unnorm_key)\n    if not torch.all(input_ids[:, -1] == 29871):\n        input_ids = torch.cat(\n            (input_ids, torch.tensor([[29871]], device=input_ids.device, dtype=input_ids.dtype)),\n            dim=1,\n        )\n    with torch.no_grad():\n        outputs = model(\n            input_ids=input_ids,\n            attention_mask=torch.ones_like(input_ids),\n            pixel_values=pixel_values,\n            past_key_values=None,\n            use_cache=True,\n        )\n    past_key_values = outputs.past_key_values\n    next_token_logits = outputs.logits[:, -1, :]\n\n    generated_ids = []\n    all_logits = []\n\n    for _ in range(action_dim):\n        all_logits.append(next_token_logits.float().cpu())\n        next_token = torch.argmax(next_token_logits, dim=-1, keepdim=True)\n        generated_ids.append(next_token.squeeze().item())\n        attn_mask = torch.ones(\n            (1, past_key_values[0][0].shape[2] + 1),\n            device=input_ids.device,\n            dtype=input_ids.dtype,\n        )\n        with torch.no_grad():\n            outputs = model(\n                input_ids=next_token,\n                attention_mask=attn_mask,\n                pixel_values=None,\n                past_key_values=past_key_values,\n                use_cache=True,\n            )\n        past_key_values = outputs.past_key_values\n        next_token_logits = outputs.logits[:, -1, :]\n\n    predicted_action_token_ids = np.array(generated_ids)\n    discretized_actions = model.vocab_size - predicted_action_token_ids\n    discretized_actions = np.clip(\n        discretized_actions - 1, a_min=0, a_max=model.bin_centers.shape[0] - 1\n    )\n    normalized_actions = model.bin_centers[discretized_actions]\n    action_norm_stats = model.get_action_stats(unnorm_key)\n    mask = action_norm_stats.get(\"mask\", np.ones_like(action_norm_stats[\"q01\"], dtype=bool))\n    action_high = np.array(action_norm_stats[\"q99\"])\n    action_low = np.array(action_norm_stats[\"q01\"])\n    action = np.where(\n        mask,\n        0.5 * (normalized_actions + 1) * (action_high - action_low) + action_low,\n        normalized_actions,\n    )\n\n    logits_tensor = torch.cat(all_logits, dim=0)\n    return action, predicted_action_token_ids, logits_tensor\n\n\n# ── Ablation hook (monkey-patch LlamaAttention.forward for transformers 4.40.1) ─\ndef install_ablation_hook(model):\n    import math\n    from transformers.models.llama.modeling_llama import repeat_kv, apply_rotary_pos_emb\n\n    layer_attn = model.language_model.model.layers[LAYER_IDX].self_attn\n    layer_attn._ablate_active = False\n    original_forward = layer_attn.forward.__func__ if hasattr(layer_attn.forward, '__func__') else layer_attn.forward\n\n    def ablated_forward(\n        self_attn,\n        hidden_states,\n        attention_mask=None,\n        position_ids=None,\n        past_key_value=None,\n        output_attentions=False,\n        use_cache=False,\n        cache_position=None,\n        **kwargs,\n    ):\n        bsz, q_len, _ = hidden_states.size()\n        query_states = self_attn.q_proj(hidden_states)\n        key_states = self_attn.k_proj(hidden_states)\n        value_states = self_attn.v_proj(hidden_states)\n\n        query_states = query_states.view(bsz, q_len, self_attn.num_heads, self_attn.head_dim).transpose(1, 2)\n        key_states = key_states.view(bsz, q_len, self_attn.num_key_value_heads, self_attn.head_dim).transpose(1, 2)\n        value_states = value_states.view(bsz, q_len, self_attn.num_key_value_heads, self_attn.head_dim).transpose(1, 2)\n\n        past_key_value = getattr(self_attn, \"past_key_value\", past_key_value)\n        cos, sin = self_attn.rotary_emb(value_states, position_ids)\n        query_states, key_states = apply_rotary_pos_emb(query_states, key_states, cos, sin)\n\n        if past_key_value is not None:\n            cache_kwargs = {\"sin\": sin, \"cos\": cos, \"cache_position\": cache_position}\n            key_states, value_states = past_key_value.update(key_states, value_states, self_attn.layer_idx, cache_kwargs)\n\n        key_states = repeat_kv(key_states, self_attn.num_key_value_groups)\n        value_states = repeat_kv(value_states, self_attn.num_key_value_groups)\n\n        attn_weights = torch.matmul(query_states, key_states.transpose(2, 3)) / math.sqrt(self_attn.head_dim)\n\n        if attention_mask is not None:\n            causal_mask = attention_mask[:, :, :, : key_states.shape[-2]]\n            attn_weights = attn_weights + causal_mask\n\n        attn_weights = nn.functional.softmax(attn_weights, dim=-1, dtype=torch.float32).to(query_states.dtype)\n        attn_weights = nn.functional.dropout(attn_weights, p=self_attn.attention_dropout, training=self_attn.training)\n\n        attn_output = torch.matmul(attn_weights, value_states)\n        attn_output = attn_output.transpose(1, 2).contiguous()\n        attn_output = attn_output.reshape(bsz, q_len, self_attn.hidden_size)\n\n        if hasattr(self_attn, \"_ablate_active\") and self_attn._ablate_active:\n            attn_output = torch.zeros_like(attn_output)\n\n        attn_output = self_attn.o_proj(attn_output)\n\n        if not output_attentions:\n            attn_weights = None\n\n        return attn_output, attn_weights, past_key_value\n\n    import types\n    layer_attn.forward = types.MethodType(ablated_forward, layer_attn)\n    return original_forward\n\n\ndef remove_ablation_hook(model, original_fn):\n    import types\n    layer_attn = model.language_model.model.layers[LAYER_IDX].self_attn\n    layer_attn.forward = types.MethodType(original_fn, layer_attn)\n    layer_attn._ablate_active = False\n\n\n# ── KL divergence ───────────────────────────────────────────────────────────\ndef compute_kl_divergence(logits_p, logits_q):\n    log_p = F.log_softmax(logits_p, dim=-1)\n    log_q = F.log_softmax(logits_q, dim=-1)\n    p = F.softmax(logits_p, dim=-1)\n    kl = (p * (log_p - log_q)).sum(dim=-1)\n    return kl.numpy()\n\n\n# ── Helpers ─────────────────────────────────────────────────────────────────\ndef get_task_files(n_tasks):\n    hdf5_files = sorted(glob.glob(os.path.join(DATA_DIR, \"*.hdf5\")))\n    return hdf5_files[:n_tasks]\n\n\ndef get_language_instruction(hdf5_path):\n    with h5py.File(hdf5_path, \"r\") as f:\n        info = json.loads(f[\"data\"].attrs[\"problem_info\"])\n    return info[\"language_instruction\"]\n\n\ndef compute_task_metrics(task_b, task_a, task_b_ids, task_a_ids, task_kls):\n    paired_mse = np.mean((task_b - task_a) ** 2, axis=1)\n    t_res = stats.ttest_1samp(paired_mse, 0)\n    cohens_d = np.mean(paired_mse) / (np.std(paired_mse, ddof=1) + 1e-12)\n\n    per_dim_shift = np.abs(task_b - task_a)\n    token_div = np.mean(task_b_ids != task_a_ids)\n\n    return {\n        \"paired_mse\": {\n            \"mean\": float(np.mean(paired_mse)),\n            \"std\": float(np.std(paired_mse)),\n            \"t_stat\": float(t_res.statistic),\n            \"p_value\": float(t_res.pvalue),\n            \"cohens_d\": float(cohens_d),\n        },\n        \"per_dim_shift\": {\n            \"means\": [float(x) for x in np.mean(per_dim_shift, axis=0)],\n            \"stds\": [float(x) for x in np.std(per_dim_shift, axis=0)],\n        },\n        \"token_divergence_rate\": float(token_div),\n        \"kl_divergence\": {\n            \"mean\": float(np.mean(task_kls)),\n            \"std\": float(np.std(task_kls)),\n        },\n        \"n_samples\": int(len(task_b)),\n    }\n\n\n# ── Main ────────────────────────────────────────────────────────────────────\ndef main():\n    parser = argparse.ArgumentParser()\n    parser.add_argument(\"--dry-run\", action=\"store_true\")\n    args = parser.parse_args()\n\n    n_tasks = 1 if args.dry_run else 5\n    n_demos = 1 if args.dry_run else 10\n    n_timesteps = 2 if args.dry_run else 50\n\n    os.makedirs(RESULTS_DIR, exist_ok=True)\n\n    print(\"Loading model...\")\n    model, processor = load_model()\n    print(\"Model loaded.\")\n\n    original_forward_fn = install_ablation_hook(model)\n    layer_attn = model.language_model.model.layers[LAYER_IDX].self_attn\n\n    task_files = get_task_files(n_tasks)\n    print(f\"Tasks ({n_tasks}): {[os.path.basename(f) for f in task_files]}\")\n    print(f\"Config: {n_demos} demos/task, {n_timesteps} timesteps/demo\")\n    print(f\"Ablation: L{LAYER_IDX} all {len(ALL_HEADS)} heads, zero attention output\")\n\n    all_baseline_actions = []\n    all_ablated_actions = []\n    all_gt_actions = []\n    all_baseline_token_ids = []\n    all_ablated_token_ids = []\n    all_kl_divs = []\n    per_task_data = {}\n\n    total_passes = 0\n    t_start = time.time()\n\n    for task_idx, hdf5_path in enumerate(task_files):\n        task_name = os.path.basename(hdf5_path).replace(\"_demo.hdf5\", \"\")\n        instruction = get_language_instruction(hdf5_path)\n        print(f\"\\n{'='*60}\")\n        print(f\"Task {task_idx}: {task_name}\")\n        print(f\"  Instruction: {instruction}\")\n\n        task_baseline_actions = []\n        task_ablated_actions = []\n        task_gt_actions = []\n        task_baseline_token_ids = []\n        task_ablated_token_ids = []\n        task_kl_divs = []\n\n        prompt = f\"In: What action should the robot take to {instruction}?\\nOut:\"\n\n        with h5py.File(hdf5_path, \"r\") as f:\n            for demo_idx in range(n_demos):\n                demo_key = f\"data/demo_{demo_idx}\"\n                actions_data = f[f\"{demo_key}/actions\"][:]\n                images_data = f[f\"{demo_key}/obs/agentview_rgb\"][:]\n                n_steps = min(n_timesteps, len(actions_data))\n\n                for step_idx in range(n_steps):\n                    image_np = images_data[step_idx]\n                    gt_action = actions_data[step_idx]\n\n                    img = Image.fromarray(image_np)\n                    inputs = processor(prompt, img).to(\"cuda:0\", dtype=torch.bfloat16)\n                    input_ids = inputs[\"input_ids\"]\n                    pixel_values = inputs[\"pixel_values\"]\n\n                    layer_attn._ablate_active = False\n                    b_action, b_ids, b_logits = predict_action_with_logits(\n                        model, input_ids, pixel_values, UNNORM_KEY\n                    )\n\n                    layer_attn._ablate_active = True\n                    a_action, a_ids, a_logits = predict_action_with_logits(\n                        model, input_ids, pixel_values, UNNORM_KEY\n                    )\n\n                    kl_per_token = compute_kl_divergence(b_logits, a_logits)\n\n                    task_baseline_actions.append(b_action)\n                    task_ablated_actions.append(a_action)\n                    task_gt_actions.append(gt_action)\n                    task_baseline_token_ids.append(b_ids)\n                    task_ablated_token_ids.append(a_ids)\n                    task_kl_divs.append(kl_per_token)\n\n                    total_passes += 2\n                    if total_passes % 100 == 0:\n                        elapsed = time.time() - t_start\n                        rate = total_passes / elapsed\n                        eta = (n_tasks * n_demos * n_timesteps * 2 - total_passes) / rate\n                        print(\n                            f\"  [{total_passes}/{n_tasks*n_demos*n_timesteps*2}] \"\n                            f\"{rate:.1f} passes/s, ETA {eta/60:.1f}min\"\n                        )\n\n        task_b = np.array(task_baseline_actions)\n        task_a = np.array(task_ablated_actions)\n        task_b_ids = np.array(task_baseline_token_ids)\n        task_a_ids = np.array(task_ablated_token_ids)\n        task_kls = np.array(task_kl_divs)\n\n        task_metrics = compute_task_metrics(task_b, task_a, task_b_ids, task_a_ids, task_kls)\n        per_task_data[task_name] = task_metrics\n\n        print(\n            f\"  Task MSE: {task_metrics['paired_mse']['mean']:.6f} \"\n            f\"(d={task_metrics['paired_mse']['cohens_d']:.3f}), \"\n            f\"token_div={task_metrics['token_divergence_rate']:.4f}, \"\n            f\"KL={task_metrics['kl_divergence']['mean']:.4f}\"\n        )\n\n        all_baseline_actions.extend(task_baseline_actions)\n        all_ablated_actions.extend(task_ablated_actions)\n        all_gt_actions.extend(task_gt_actions)\n        all_baseline_token_ids.extend(task_baseline_token_ids)\n        all_ablated_token_ids.extend(task_ablated_token_ids)\n        all_kl_divs.extend(task_kl_divs)\n\n        gc.collect()\n        torch.cuda.empty_cache()\n\n    # ── Global metrics ──────────────────────────────────────────────────────\n    layer_attn._ablate_active = False\n    remove_ablation_hook(model, original_forward_fn)\n\n    all_b = np.array(all_baseline_actions)\n    all_a = np.array(all_ablated_actions)\n    all_gt = np.array(all_gt_actions)\n    all_b_ids = np.array(all_baseline_token_ids)\n    all_a_ids = np.array(all_ablated_token_ids)\n    all_kls = np.array(all_kl_divs)\n\n    paired_mse_all = np.mean((all_b - all_a) ** 2, axis=1)\n    t_res_all = stats.ttest_1samp(paired_mse_all, 0)\n    cohens_d_all = np.mean(paired_mse_all) / (np.std(paired_mse_all, ddof=1) + 1e-12)\n\n    per_dim_shift_all = np.abs(all_b - all_a)\n    token_div_all = np.mean(all_b_ids != all_a_ids)\n\n    kl_per_position = np.mean(all_kls, axis=0)\n\n    mse_gt_baseline = np.mean((all_b - all_gt) ** 2, axis=1)\n    mse_gt_ablated = np.mean((all_a - all_gt) ** 2, axis=1)\n\n    try:\n        wilcoxon_res = stats.wilcoxon(paired_mse_all)\n        wilcoxon_p = float(wilcoxon_res.pvalue)\n    except Exception:\n        wilcoxon_p = None\n\n    output = {\n        \"config\": {\n            \"n_tasks\": n_tasks,\n            \"n_demos_per_task\": n_demos,\n            \"n_timesteps_per_demo\": n_timesteps,\n            \"total_forward_passes\": total_passes,\n            \"model\": \"openvla-7b\",\n            \"ablation\": f\"L{LAYER_IDX}_all_32_heads_zero_attn_output\",\n            \"ablated_heads\": ALL_HEADS,\n            \"layer_idx\": LAYER_IDX,\n            \"unnorm_key\": UNNORM_KEY,\n        },\n        \"main_metrics\": {\n            \"paired_action_mse\": {\n                \"mean\": float(np.mean(paired_mse_all)),\n                \"std\": float(np.std(paired_mse_all)),\n                \"t_stat\": float(t_res_all.statistic),\n                \"p_value\": float(t_res_all.pvalue),\n                \"cohens_d\": float(cohens_d_all),\n            },\n            \"per_dim_action_shift\": {\n                \"means\": [float(x) for x in np.mean(per_dim_shift_all, axis=0)],\n                \"stds\": [float(x) for x in np.std(per_dim_shift_all, axis=0)],\n                \"dim_names\": DIM_NAMES,\n            },\n            \"token_divergence_rate\": float(token_div_all),\n        },\n        \"secondary_metrics\": {\n            \"kl_divergence\": {\n                \"mean\": float(np.mean(all_kls)),\n                \"std\": float(np.std(all_kls)),\n                \"per_token_position\": [float(x) for x in kl_per_position],\n            },\n            \"mse_vs_gt_baseline\": {\n                \"mean\": float(np.mean(mse_gt_baseline)),\n                \"std\": float(np.std(mse_gt_baseline)),\n                \"note\": \"OOD, secondary\",\n            },\n            \"mse_vs_gt_ablated\": {\n                \"mean\": float(np.mean(mse_gt_ablated)),\n                \"std\": float(np.std(mse_gt_ablated)),\n                \"note\": \"OOD, secondary\",\n            },\n            \"wilcoxon_p\": wilcoxon_p,\n        },\n        \"per_task\": per_task_data,\n    }\n\n    elapsed_total = time.time() - t_start\n    print(f\"\\n{'='*60}\")\n    print(f\"Done. {total_passes} forward passes in {elapsed_total:.0f}s\")\n    print(\n        f\"Paired MSE: {np.mean(paired_mse_all):.6f} \"\n        f\"(p={t_res_all.pvalue:.2e}, d={cohens_d_all:.3f})\"\n    )\n    print(f\"Token divergence: {token_div_all:.4f}\")\n    print(f\"KL divergence: {np.mean(all_kls):.4f}\")\n    print(f\"MSE vs GT - baseline: {np.mean(mse_gt_baseline):.6f}, ablated: {np.mean(mse_gt_ablated):.6f}\")\n\n    out_path = os.path.join(RESULTS_DIR, \"action_trajectory_L8_ablation.json\")\n    with open(out_path, \"w\") as f:\n        json.dump(output, f, indent=2)\n    print(f\"Results saved to {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT_EOF"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cross_layer_L8_ablation_20260518T133705",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat > /root/vla-ssd/scripts/action_trajectory_L8_ablation.py << 'SCRIPT_EOF'\n\"\"\"Open-loop action trajectory analysis: baseline vs L8-full-ablation on LIBERO demo observations.\"\"\"\n\nimport argparse\nimport gc\nimport glob\nimport json\nimport os\nimport sys\nimport time\n\nsys.path.insert(0, \"/root/autodl-tmp/LIBERO\")\n\nos.environ[\"MUJOCO_GL\"] = \"egl\"\nos.environ[\"HDF5_USE_FILE_LOCKING\"] = \"FALSE\"\n\nimport h5py\nimport numpy as np\nimport torch\nimport torch.nn as nn\nimport torch.nn.functional as F\nfrom PIL import Image\nfrom scipy import stats\n\nnp.random.seed(42)\ntorch.manual_seed(42)\n\n# ── Config ──────────────────────────────────────────────────────────────────\nMODEL_PATH = \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\"\nUNNORM_KEY = \"bridge_orig\"\nDATA_DIR = \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal\"\nRESULTS_DIR = \"/root/autodl-tmp/vla-ssd/results\"\n\nLAYER_IDX = 8\nALL_HEADS = list(range(32))\n\nDIM_NAMES = [\"dx\", \"dy\", \"dz\", \"rx\", \"ry\", \"rz\", \"gripper\"]\n\n\n# ── Model loading ───────────────────────────────────────────────────────────\ndef load_model():\n    from transformers import AutoModelForVision2Seq, AutoProcessor\n\n    processor = AutoProcessor.from_pretrained(MODEL_PATH, trust_remote_code=True)\n    model = AutoModelForVision2Seq.from_pretrained(\n        MODEL_PATH,\n        torch_dtype=torch.bfloat16,\n        trust_remote_code=True,\n        low_cpu_mem_usage=True,\n    ).to(\"cuda:0\").eval()\n    return model, processor\n\n\n# ── Manual autoregressive generation (bypasses generate() DynamicCache bug) ─\ndef predict_action_with_logits(model, input_ids, pixel_values, unnorm_key):\n    action_dim = model.get_action_dim(unnorm_key)\n    if not torch.all(input_ids[:, -1] == 29871):\n        input_ids = torch.cat(\n            (input_ids, torch.tensor([[29871]], device=input_ids.device, dtype=input_ids.dtype)),\n            dim=1,\n        )\n    with torch.no_grad():\n        outputs = model(\n            input_ids=input_ids,\n            attention_mask=torch.ones_like(input_ids),\n            pixel_values=pixel_values,\n            past_key_values=None,\n            use_cache=True,\n        )\n    past_key_values = outputs.past_key_values\n    next_token_logits = outputs.logits[:, -1, :]\n\n    generated_ids = []\n    all_logits = []\n\n    for _ in range(action_dim):\n        all_logits.append(next_token_logits.float().cpu())\n        next_token = torch.argmax(next_token_logits, dim=-1, keepdim=True)\n        generated_ids.append(next_token.squeeze().item())\n        attn_mask = torch.ones(\n            (1, past_key_values[0][0].shape[2] + 1),\n            device=input_ids.device,\n            dtype=input_ids.dtype,\n        )\n        with torch.no_grad():\n            outputs = model(\n                input_ids=next_token,\n                attention_mask=attn_mask,\n                pixel_values=None,\n                past_key_values=past_key_values,\n                use_cache=True,\n            )\n        past_key_values = outputs.past_key_values\n        next_token_logits = outputs.logits[:, -1, :]\n\n    predicted_action_token_ids = np.array(generated_ids)\n    discretized_actions = model.vocab_size - predicted_action_token_ids\n    discretized_actions = np.clip(\n        discretized_actions - 1, a_min=0, a_max=model.bin_centers.shape[0] - 1\n    )\n    normalized_actions = model.bin_centers[discretized_actions]\n    action_norm_stats = model.get_action_stats(unnorm_key)\n    mask = action_norm_stats.get(\"mask\", np.ones_like(action_norm_stats[\"q01\"], dtype=bool))\n    action_high = np.array(action_norm_stats[\"q99\"])\n    action_low = np.array(action_norm_stats[\"q01\"])\n    action = np.where(\n        mask,\n        0.5 * (normalized_actions + 1) * (action_high - action_low) + action_low,\n        normalized_actions,\n    )\n\n    logits_tensor = torch.cat(all_logits, dim=0)\n    return action, predicted_action_token_ids, logits_tensor\n\n\n# ── Ablation hook (monkey-patch LlamaAttention.forward for transformers 4.40.1) ─\ndef install_ablation_hook(model):\n    import math\n    from transformers.models.llama.modeling_llama import repeat_kv, apply_rotary_pos_emb\n\n    layer_attn = model.language_model.model.layers[LAYER_IDX].self_attn\n    layer_attn._ablate_active = False\n    original_forward = layer_attn.forward.__func__ if hasattr(layer_attn.forward, '__func__') else layer_attn.forward\n\n    def ablated_forward(\n        self_attn,\n        hidden_states,\n        attention_mask=None,\n        position_ids=None,\n        past_key_value=None,\n        output_attentions=False,\n        use_cache=False,\n        cache_position=None,\n        **kwargs,\n    ):\n        bsz, q_len, _ = hidden_states.size()\n        query_states = self_attn.q_proj(hidden_states)\n        key_states = self_attn.k_proj(hidden_states)\n        value_states = self_attn.v_proj(hidden_states)\n\n        query_states = query_states.view(bsz, q_len, self_attn.num_heads, self_attn.head_dim).transpose(1, 2)\n        key_states = key_states.view(bsz, q_len, self_attn.num_key_value_heads, self_attn.head_dim).transpose(1, 2)\n        value_states = value_states.view(bsz, q_len, self_attn.num_key_value_heads, self_attn.head_dim).transpose(1, 2)\n\n        past_key_value = getattr(self_attn, \"past_key_value\", past_key_value)\n        cos, sin = self_attn.rotary_emb(value_states, position_ids)\n        query_states, key_states = apply_rotary_pos_emb(query_states, key_states, cos, sin)\n\n        if past_key_value is not None:\n            cache_kwargs = {\"sin\": sin, \"cos\": cos, \"cache_position\": cache_position}\n            key_states, value_states = past_key_value.update(key_states, value_states, self_attn.layer_idx, cache_kwargs)\n\n        key_states = repeat_kv(key_states, self_attn.num_key_value_groups)\n        value_states = repeat_kv(value_states, self_attn.num_key_value_groups)\n\n        attn_weights = torch.matmul(query_states, key_states.transpose(2, 3)) / math.sqrt(self_attn.head_dim)\n\n        if attention_mask is not None:\n            causal_mask = attention_mask[:, :, :, : key_states.shape[-2]]\n            attn_weights = attn_weights + causal_mask\n\n        attn_weights = nn.functional.softmax(attn_weights, dim=-1, dtype=torch.float32).to(query_states.dtype)\n        attn_weights = nn.functional.dropout(attn_weights, p=self_attn.attention_dropout, training=self_attn.training)\n\n        attn_output = torch.matmul(attn_weights, value_states)\n        attn_output = attn_output.transpose(1, 2).contiguous()\n        attn_output = attn_output.reshape(bsz, q_len, self_attn.hidden_size)\n\n        if hasattr(self_attn, \"_ablate_active\") and self_attn._ablate_active:\n            attn_output = torch.zeros_like(attn_output)\n\n        attn_output = self_attn.o_proj(attn_output)\n\n        if not output_attentions:\n            attn_weights = None\n\n        return attn_output, attn_weights, past_key_value\n\n    import types\n    layer_attn.forward = types.MethodType(ablated_forward, layer_attn)\n    return original_forward\n\n\ndef remove_ablation_hook(model, original_fn):\n    import types\n    layer_attn = model.language_model.model.layers[LAYER_IDX].self_attn\n    layer_attn.forward = types.MethodType(original_fn, layer_attn)\n    layer_attn._ablate_active = False\n\n\n# ── KL divergence ───────────────────────────────────────────────────────────\ndef compute_kl_divergence(logits_p, logits_q):\n    log_p = F.log_softmax(logits_p, dim=-1)\n    log_q = F.log_softmax(logits_q, dim=-1)\n    p = F.softmax(logits_p, dim=-1)\n    kl = (p * (log_p - log_q)).sum(dim=-1)\n    return kl.numpy()\n\n\n# ── Helpers ─────────────────────────────────────────────────────────────────\ndef get_task_files(n_tasks):\n    hdf5_files = sorted(glob.glob(os.path.join(DATA_DIR, \"*.hdf5\")))\n    return hdf5_files[:n_tasks]\n\n\ndef get_language_instruction(hdf5_path):\n    with h5py.File(hdf5_path, \"r\") as f:\n        info = json.loads(f[\"data\"].attrs[\"problem_info\"])\n    return info[\"language_instruction\"]\n\n\ndef compute_task_metrics(task_b, task_a, task_b_ids, task_a_ids, task_kls):\n    paired_mse = np.mean((task_b - task_a) ** 2, axis=1)\n    t_res = stats.ttest_1samp(paired_mse, 0)\n    cohens_d = np.mean(paired_mse) / (np.std(paired_mse, ddof=1) + 1e-12)\n\n    per_dim_shift = np.abs(task_b - task_a)\n    token_div = np.mean(task_b_ids != task_a_ids)\n\n    return {\n        \"paired_mse\": {\n            \"mean\": float(np.mean(paired_mse)),\n            \"std\": float(np.std(paired_mse)),\n            \"t_stat\": float(t_res.statistic),\n            \"p_value\": float(t_res.pvalue),\n            \"cohens_d\": float(cohens_d),\n        },\n        \"per_dim_shift\": {\n            \"means\": [float(x) for x in np.mean(per_dim_shift, axis=0)],\n            \"stds\": [float(x) for x in np.std(per_dim_shift, axis=0)],\n        },\n        \"token_divergence_rate\": float(token_div),\n        \"kl_divergence\": {\n            \"mean\": float(np.mean(task_kls)),\n            \"std\": float(np.std(task_kls)),\n        },\n        \"n_samples\": int(len(task_b)),\n    }\n\n\n# ── Main ────────────────────────────────────────────────────────────────────\ndef main():\n    parser = argparse.ArgumentParser()\n    parser.add_argument(\"--dry-run\", action=\"store_true\")\n    args = parser.parse_args()\n\n    n_tasks = 1 if args.dry_run else 5\n    n_demos = 1 if args.dry_run else 10\n    n_timesteps = 2 if args.dry_run else 50\n\n    os.makedirs(RESULTS_DIR, exist_ok=True)\n\n    print(\"Loading model...\")\n    model, processor = load_model()\n    print(\"Model loaded.\")\n\n    original_forward_fn = install_ablation_hook(model)\n    layer_attn = model.language_model.model.layers[LAYER_IDX].self_attn\n\n    task_files = get_task_files(n_tasks)\n    print(f\"Tasks ({n_tasks}): {[os.path.basename(f) for f in task_files]}\")\n    print(f\"Config: {n_demos} demos/task, {n_timesteps} timesteps/demo\")\n    print(f\"Ablation: L{LAYER_IDX} all {len(ALL_HEADS)} heads, zero attention output\")\n\n    all_baseline_actions = []\n    all_ablated_actions = []\n    all_gt_actions = []\n    all_baseline_token_ids = []\n    all_ablated_token_ids = []\n    all_kl_divs = []\n    per_task_data = {}\n\n    total_passes = 0\n    t_start = time.time()\n\n    for task_idx, hdf5_path in enumerate(task_files):\n        task_name = os.path.basename(hdf5_path).replace(\"_demo.hdf5\", \"\")\n        instruction = get_language_instruction(hdf5_path)\n        print(f\"\\n{'='*60}\")\n        print(f\"Task {task_idx}: {task_name}\")\n        print(f\"  Instruction: {instruction}\")\n\n        task_baseline_actions = []\n        task_ablated_actions = []\n        task_gt_actions = []\n        task_baseline_token_ids = []\n        task_ablated_token_ids = []\n        task_kl_divs = []\n\n        prompt = f\"In: What action should the robot take to {instruction}?\\nOut:\"\n\n        with h5py.File(hdf5_path, \"r\") as f:\n            for demo_idx in range(n_demos):\n                demo_key = f\"data/demo_{demo_idx}\"\n                actions_data = f[f\"{demo_key}/actions\"][:]\n                images_data = f[f\"{demo_key}/obs/agentview_rgb\"][:]\n                n_steps = min(n_timesteps, len(actions_data))\n\n                for step_idx in range(n_steps):\n                    image_np = images_data[step_idx]\n                    gt_action = actions_data[step_idx]\n\n                    img = Image.fromarray(image_np)\n                    inputs = processor(prompt, img).to(\"cuda:0\", dtype=torch.bfloat16)\n                    input_ids = inputs[\"input_ids\"]\n                    pixel_values = inputs[\"pixel_values\"]\n\n                    layer_attn._ablate_active = False\n                    b_action, b_ids, b_logits = predict_action_with_logits(\n                        model, input_ids, pixel_values, UNNORM_KEY\n                    )\n\n                    layer_attn._ablate_active = True\n                    a_action, a_ids, a_logits = predict_action_with_logits(\n                        model, input_ids, pixel_values, UNNORM_KEY\n                    )\n\n                    kl_per_token = compute_kl_divergence(b_logits, a_logits)\n\n                    task_baseline_actions.append(b_action)\n                    task_ablated_actions.append(a_action)\n                    task_gt_actions.append(gt_action)\n                    task_baseline_token_ids.append(b_ids)\n                    task_ablated_token_ids.append(a_ids)\n                    task_kl_divs.append(kl_per_token)\n\n                    total_passes += 2\n                    if total_passes % 100 == 0:\n                        elapsed = time.time() - t_start\n                        rate = total_passes / elapsed\n                        eta = (n_tasks * n_demos * n_timesteps * 2 - total_passes) / rate\n                        print(\n                            f\"  [{total_passes}/{n_tasks*n_demos*n_timesteps*2}] \"\n                            f\"{rate:.1f} passes/s, ETA {eta/60:.1f}min\"\n                        )\n\n        task_b = np.array(task_baseline_actions)\n        task_a = np.array(task_ablated_actions)\n        task_b_ids = np.array(task_baseline_token_ids)\n        task_a_ids = np.array(task_ablated_token_ids)\n        task_kls = np.array(task_kl_divs)\n\n        task_metrics = compute_task_metrics(task_b, task_a, task_b_ids, task_a_ids, task_kls)\n        per_task_data[task_name] = task_metrics\n\n        print(\n            f\"  Task MSE: {task_metrics['paired_mse']['mean']:.6f} \"\n            f\"(d={task_metrics['paired_mse']['cohens_d']:.3f}), \"\n            f\"token_div={task_metrics['token_divergence_rate']:.4f}, \"\n            f\"KL={task_metrics['kl_divergence']['mean']:.4f}\"\n        )\n\n        all_baseline_actions.extend(task_baseline_actions)\n        all_ablated_actions.extend(task_ablated_actions)\n        all_gt_actions.extend(task_gt_actions)\n        all_baseline_token_ids.extend(task_baseline_token_ids)\n        all_ablated_token_ids.extend(task_ablated_token_ids)\n        all_kl_divs.extend(task_kl_divs)\n\n        gc.collect()\n        torch.cuda.empty_cache()\n\n    # ── Global metrics ──────────────────────────────────────────────────────\n    layer_attn._ablate_active = False\n    remove_ablation_hook(model, original_forward_fn)\n\n    all_b = np.array(all_baseline_actions)\n    all_a = np.array(all_ablated_actions)\n    all_gt = np.array(all_gt_actions)\n    all_b_ids = np.array(all_baseline_token_ids)\n    all_a_ids = np.array(all_ablated_token_ids)\n    all_kls = np.array(all_kl_divs)\n\n    paired_mse_all = np.mean((all_b - all_a) ** 2, axis=1)\n    t_res_all = stats.ttest_1samp(paired_mse_all, 0)\n    cohens_d_all = np.mean(paired_mse_all) / (np.std(paired_mse_all, ddof=1) + 1e-12)\n\n    per_dim_shift_all = np.abs(all_b - all_a)\n    token_div_all = np.mean(all_b_ids != all_a_ids)\n\n    kl_per_position = np.mean(all_kls, axis=0)\n\n    mse_gt_baseline = np.mean((all_b - all_gt) ** 2, axis=1)\n    mse_gt_ablated = np.mean((all_a - all_gt) ** 2, axis=1)\n\n    try:\n        wilcoxon_res = stats.wilcoxon(paired_mse_all)\n        wilcoxon_p = float(wilcoxon_res.pvalue)\n    except Exception:\n        wilcoxon_p = None\n\n    output = {\n        \"config\": {\n            \"n_tasks\": n_tasks,\n            \"n_demos_per_task\": n_demos,\n            \"n_timesteps_per_demo\": n_timesteps,\n            \"total_forward_passes\": total_passes,\n            \"model\": \"openvla-7b\",\n            \"ablation\": f\"L{LAYER_IDX}_all_32_heads_zero_attn_output\",\n            \"ablated_heads\": ALL_HEADS,\n            \"layer_idx\": LAYER_IDX,\n            \"unnorm_key\": UNNORM_KEY,\n        },\n        \"main_metrics\": {\n            \"paired_action_mse\": {\n                \"mean\": float(np.mean(paired_mse_all)),\n                \"std\": float(np.std(paired_mse_all)),\n                \"t_stat\": float(t_res_all.statistic),\n                \"p_value\": float(t_res_all.pvalue),\n                \"cohens_d\": float(cohens_d_all),\n            },\n            \"per_dim_action_shift\": {\n                \"means\": [float(x) for x in np.mean(per_dim_shift_all, axis=0)],\n                \"stds\": [float(x) for x in np.std(per_dim_shift_all, axis=0)],\n                \"dim_names\": DIM_NAMES,\n            },\n            \"token_divergence_rate\": float(token_div_all),\n        },\n        \"secondary_metrics\": {\n            \"kl_divergence\": {\n                \"mean\": float(np.mean(all_kls)),\n                \"std\": float(np.std(all_kls)),\n                \"per_token_position\": [float(x) for x in kl_per_position],\n            },\n            \"mse_vs_gt_baseline\": {\n                \"mean\": float(np.mean(mse_gt_baseline)),\n                \"std\": float(np.std(mse_gt_baseline)),\n                \"note\": \"OOD, secondary\",\n            },\n            \"mse_vs_gt_ablated\": {\n                \"mean\": float(np.mean(mse_gt_ablated)),\n                \"std\": float(np.std(mse_gt_ablated)),\n                \"note\": \"OOD, secondary\",\n            },\n            \"wilcoxon_p\": wilcoxon_p,\n        },\n        \"per_task\": per_task_data,\n    }\n\n    elapsed_total = time.time() - t_start\n    print(f\"\\n{'='*60}\")\n    print(f\"Done. {total_passes} forward passes in {elapsed_total:.0f}s\")\n    print(\n        f\"Paired MSE: {np.mean(paired_mse_all):.6f} \"\n        f\"(p={t_res_all.pvalue:.2e}, d={cohens_d_all:.3f})\"\n    )\n    print(f\"Token divergence: {token_div_all:.4f}\")\n    print(f\"KL divergence: {np.mean(all_kls):.4f}\")\n    print(f\"MSE vs GT - baseline: {np.mean(mse_gt_baseline):.6f}, ablated: {np.mean(mse_gt_ablated):.6f}\")\n\n    out_path = os.path.join(RESULTS_DIR, \"action_trajectory_L8_ablation.json\")\n    with open(out_path, \"w\") as f:\n        json.dump(output, f, indent=2)\n    print(f\"Results saved to {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT_EOF"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-18T13:40:11.200425+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cross_layer_L8_ablation_20260518T133705",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-18T13:40:11.200674+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19183",
  "command": "source /root/miniconda3/bin/activate base && python /root/vla-ssd/scripts/action_trajectory_L8_ablation.py --help"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cross_layer_L8_ablation_20260518T133705",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19183",
    "command": "source /root/miniconda3/bin/activate base && python /root/vla-ssd/scripts/action_trajectory_L8_ablation.py --help"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-18T13:40:11.200908+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"usage: action_trajectory_L8_ablation.py [-h] [--dry-run]\\n\\noptions:\\n  -h, --help  show this help message and exit\\n  --dry-run\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.73}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cross_layer_L8_ablation_20260518T133705",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-18T13:40:11.201174+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__update_registry",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cross_layer_L8_ablation_20260518T133705",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__update_registry",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-18T13:40:11.201600+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cross_layer_L8_ablation_20260518T133705",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-18T13:40:11.201832+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "cross_layer_L8_ablation",
  "field": "status",
  "value": "RUNNING",
  "project": "vla-ssd",
  "spec": "{'command': 'bash -c \"source /root/miniconda3/bin/activate base && cd /root/vla-ssd && MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=0 python -u scripts/action_trajectory_L8_ablation.py 2>&1 | tee /root/autodl-tmp/vla-ssd/results/action_trajectory_L8_ablation.log\"', 'server': 'westd-19183', 'data_path': '/root/autodl-tmp/vla-ssd/data/libero/libero_goal', 'data_count': 2500, 'model_name': 'openvla-7b', 'seed': 42}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cross_layer_L8_ablation_20260518T133705",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "cross_layer_L8_ablation",
    "field": "status",
    "value": "RUNNING",
    "project": "vla-ssd",
    "spec": "{'command': 'bash -c \"source /root/miniconda3/bin/activate base && cd /root/vla-ssd && MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=0 python -u scripts/action_trajectory_L8_ablation.py 2>&1 | tee /root/autodl-tmp/vla-ssd/results/action_trajectory_L8_ablation.log\"', 'server': 'westd-19183', 'data_path': '/root/autodl-tmp/vla-ssd/data/libero/libero_goal', 'data_count': 2500, 'model_name': 'openvla-7b', 'seed': 42}"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-18T13:40:11.202111+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.2442}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cross_layer_L8_ablation_20260518T133705",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-18T13:40:11.202337+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "cross_layer_L8_ablation",
  "field": "status",
  "value": "QUEUED",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cross_layer_L8_ablation_20260518T133705",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "cross_layer_L8_ablation",
    "field": "status",
    "value": "QUEUED",
    "project": "vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-18T13:40:11.202577+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"cross_layer_L8_ablation\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:35:43.212Z\", \"updated_at\": \"2026-05-18T13:39:46.259Z\", \"hypothesis\": \"L8 full-layer ablation (all 32 heads) produces significantly smaller action divergence (d << 0.65) than L1 instruction-head ablation (24 heads, d=0.65), demonstrating that L1's causal impact on action output is layer-position-specific, not merely a function of head count. Based on R² gradient prediction: L8 Δ=+0.018 vs L1 Δ=+0.059.\", \"parent\": \"action_trajectory_control\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.831}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cross_layer_L8_ablation_20260518T133705",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-18T13:40:11.202812+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "cross_layer_L8_ablation",
  "field": "status",
  "value": "RUNNING",
  "project": "vla-ssd",
  "spec": "{'command': 'bash -c \"source /root/miniconda3/bin/activate base && cd /root/vla-ssd && MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=0 python -u scripts/action_trajectory_L8_ablation.py 2>&1 | tee /root/autodl-tmp/vla-ssd/results/action_trajectory_L8_ablation.log\"', 'server': 'westd-19183', 'data_path': '/root/autodl-tmp/vla-ssd/data/libero/libero_goal', 'data_count': 2500, 'model_name': 'openvla-7b', 'seed': 42}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cross_layer_L8_ablation_20260518T133705",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "cross_layer_L8_ablation",
    "field": "status",
    "value": "RUNNING",
    "project": "vla-ssd",
    "spec": "{'command': 'bash -c \"source /root/miniconda3/bin/activate base && cd /root/vla-ssd && MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=0 python -u scripts/action_trajectory_L8_ablation.py 2>&1 | tee /root/autodl-tmp/vla-ssd/results/action_trajectory_L8_ablation.log\"', 'server': 'westd-19183', 'data_path': '/root/autodl-tmp/vla-ssd/data/libero/libero_goal', 'data_count': 2500, 'model_name': 'openvla-7b', 'seed': 42}"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-18T13:40:11.203071+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Eval experiment requires additional spec fields: ['checkpoint_source', 'eval_data']. Eval spec must include: ['checkpoint_source', 'eval_data']\", \"metadata\": {\"elapsed_seconds\": 0.2859}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cross_layer_L8_ablation_20260518T133705",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-18T13:40:11.203298+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "cross_layer_L8_ablation",
  "field": "status",
  "value": "RUNNING",
  "project": "vla-ssd",
  "spec": "{'command': 'bash -c \"source /root/miniconda3/bin/activate base && cd /root/vla-ssd && MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=0 python -u scripts/action_trajectory_L8_ablation.py 2>&1 | tee /root/autodl-tmp/vla-ssd/results/action_trajectory_L8_ablation.log\"', 'server': 'westd-19183', 'data_path': '/root/autodl-tmp/vla-ssd/data/libero/libero_goal', 'data_count': 2500, 'model_name': 'openvla-7b', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b', 'eval_data': '/root/autodl-tmp/vla-ssd/data/libero/libero_goal'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cross_layer_L8_ablation_20260518T133705",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "cross_layer_L8_ablation",
    "field": "status",
    "value": "RUNNING",
    "project": "vla-ssd",
    "spec": "{'command': 'bash -c \"source /root/miniconda3/bin/activate base && cd /root/vla-ssd && MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=0 python -u scripts/action_trajectory_L8_ablation.py 2>&1 | tee /root/autodl-tmp/vla-ssd/results/action_trajectory_L8_ablation.log\"', 'server': 'westd-19183', 'data_path': '/root/autodl-tmp/vla-ssd/data/libero/libero_goal', 'data_count': 2500, 'model_name': 'openvla-7b', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b', 'eval_data': '/root/autodl-tmp/vla-ssd/data/libero/libero_goal'}"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-18T13:40:11.203557+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"cross_layer_L8_ablation\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:35:43.212Z\", \"updated_at\": \"2026-05-18T13:39:55.404Z\", \"hypothesis\": \"L8 full-layer ablation (all 32 heads) produces significantly smaller action divergence (d << 0.65) than L1 instruction-head ablation (24 heads, d=0.65), demonstrating that L1's causal impact on action output is layer-position-specific, not merely a function of head count. Based on R² gradient prediction: L8 Δ=+0.018 vs L1 Δ=+0.059.\", \"parent\": \"action_trajectory_control\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/vla-ssd && MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=0 python -u scripts/action_trajectory_L8_ablation.py 2>&1 | tee /root/autodl-tmp/vla-ssd/results/action_trajectory_L8_ablation.log\\\"\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal\", \"data_count\": 2500, \"model_name\": \"openvla-7b\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\", \"eval_data\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8274}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cross_layer_L8_ablation_20260518T133705",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-18T13:40:11.203813+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19183",
  "command": "nohup bash -c \"source /root/miniconda3/bin/activate base && cd /root/vla-ssd && MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=0 python -u scripts/action_trajectory_L8_ablation.py 2>&1 | tee /root/autodl-tmp/vla-ssd/results/action_trajectory_L8_ablation.log\" > /dev/null 2>&1 & echo \"PID=$!\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cross_layer_L8_ablation_20260518T133705",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19183",
    "command": "nohup bash -c \"source /root/miniconda3/bin/activate base && cd /root/vla-ssd && MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=0 python -u scripts/action_trajectory_L8_ablation.py 2>&1 | tee /root/autodl-tmp/vla-ssd/results/action_trajectory_L8_ablation.log\" > /dev/null 2>&1 & echo \"PID=$!\""
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-18T13:40:11.204063+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"PID=53738\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cross_layer_L8_ablation_20260518T133705",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-18T13:40:11.204298+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "tail -5 /root/autodl-tmp/vla-ssd/results/action_trajectory_L8_ablation.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cross_layer_L8_ablation_20260518T133705",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "tail -5 /root/autodl-tmp/vla-ssd/results/action_trajectory_L8_ablation.log"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-18T13:40:11.204515+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Loading model...\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cross_layer_L8_ablation_20260518T133705",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-18T13:40:11.204783+00:00_

实验已提交并正在运行：

- **脚本**: `/root/vla-ssd/scripts/action_trajectory_L8_ablation.py`
- **PID**: 53738
- **exp_id**: `cross_layer_L8_ablation` (RUNNING)
- **配置**: L8 全层 ablation (32 heads), 5 tasks × 10 demos × 50 timesteps
- **ablation 方式**: monkey-patch `LlamaAttention.forward`, 正常计算 attention + KV cache，但将 `attn_output` 置零后再过 `o_proj`，使该层 attention 贡献为零
- **输出**: `/root/autodl-tmp/vla-ssd/results/action_trajectory_L8_ablation.json`
- **日志**: `/root/autodl-tmp/vla-ssd/results/action_trajectory_L8_ablation.log`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_cross_layer_L8_ablation_20260518T133705"
}
```

</details>

---
