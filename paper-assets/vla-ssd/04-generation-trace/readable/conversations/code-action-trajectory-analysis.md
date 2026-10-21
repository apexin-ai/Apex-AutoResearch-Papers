# code action trajectory analysis

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 0
- **Tool calls:** 21
- **Original source:** `logs/chats/worker_code_action_trajectory_analysis_20260518T103905.jsonl`
- **Structured JSON:** [`15e66525a130072da4a6.json`](../../sessions/15/15e66525a130072da4a6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

43 recorded events

### Tool call

_source line 1 · 2026-05-18T10:45:46.176102+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_action_trajectory_analysis_20260518T103905",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-18T10:45:46.176834+00:00_

EISDIR: illegal operation on a directory, read '/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_action_trajectory_analysis_20260518T103905",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T10:45:46.177086+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__submit_training_job,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__read_registry",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_action_trajectory_analysis_20260518T103905",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__submit_training_job,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__read_registry",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-18T10:45:46.177251+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_action_trajectory_analysis_20260518T103905",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T10:45:46.177393+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/vla-ssd/scripts/behavioral_pilot.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_action_trajectory_analysis_20260518T103905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/vla-ssd/scripts/behavioral_pilot.py"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-18T10:45:46.177555+00:00_

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
  "session": "worker_code_action_trajectory_analysis_20260518T103905",
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

_source line 7 · 2026-05-18T10:45:46.177842+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Behavioral pilot: compare OpenVLA baseline vs L1-ablated on LIBERO-Goal tasks.\\\"\\\"\\\"\\n\\nimport os\\nimport sys\\nsys.path.insert(0, \\\"/root/autodl-tmp/LIBERO\\\")\\n\\nos.environ[\\\"MUJOCO_GL\\\"] = \\\"egl\\\"\\nos.environ[\\\"HDF5_USE_FILE_LOCKING\\\"] = \\\"FALSE\\\"\\n\\nimport gc\\nimport json\\nimport time\\n\\nimport numpy as np\\nimport torch\\nimport torch.nn as nn\\nfrom PIL import Image\\n\\nnp.random.seed(42)\\ntorch.manual_seed(42)\\n\\n# ── Config ──────────────────────────────────────────────────────────────────\\nMODEL_PATH = \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"\\nUNNORM_KEY = \\\"bridge_orig\\\"\\nTASK_IDS = [0, 3, 7]\\nN_EPISODES = 10\\nMAX_STEPS = 300\\nCONDITIONS = [\\\"baseline\\\", \\\"ablated\\\"]\\nRESULTS_DIR = \\\"/root/autodl-tmp/vla-ssd/results\\\"\\n\\nNUM_IMAGE_TOKENS = 256\\nINST_START = 1 + NUM_IMAGE_TOKENS  # BOS(1) + image(256) = 257\\nINSTRUCTION_HEADS_24 = [0, 1, 2, 4, 7, 8, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20,\\n                        22, 23, 25, 26, 27, 29, 30, 31]\\n\\nfrom libero.libero import benchmark\\nfrom libero.libero.envs import OffScreenRenderEnv\\nimport libero.libero\\n\\nLIB_DIR = os.path.dirname(libero.libero.__file__)\\n\\n\\ndef make_env(task_id):\\n    bench = benchmark.get_benchmark(\\\"libero_goal\\\")()\\n    task = bench.get_task(task_id)\\n    bddl_path = os.path.join(LIB_DIR, \\\"bddl_files\\\", task.problem_folder, task.bddl_file)\\n    env = OffScreenRenderEnv(\\n        bddl_file_name=bddl_path,\\n        camera_heights=224,\\n        camera_widths=224,\\n        camera_names=\\\"agentview\\\",\\n    )\\n    return env, task.language, task.name\\n\\n\\n# ── Manual autoregressive generation (bypasses generate() DynamicCache issues) ──\\ndef predict_action_manual(model, input_ids, pixel_values, unnorm_key):\\n    action_dim = model.get_action_dim(unnorm_key)\\n    if not torch.all(input_ids[:, -1] == 2987
…[truncated 7072 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_action_trajectory_analysis_20260518T103905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-18T10:45:46.178054+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"open_the_middle_drawer_of_the_cabinet_demo.hdf5\\nopen_the_top_drawer_and_put_the_bowl_inside_demo.hdf5\\npush_the_plate_to_the_front_of_the_stove_demo.hdf5\\nput_the_bowl_on_the_plate_demo.hdf5\\nput_the_bowl_on_the_stove_demo.hdf5\\nput_the_bowl_on_top_of_the_cabinet_demo.hdf5\\nput_the_cream_cheese_in_the_bowl_demo.hdf5\\nput_the_wine_bottle_on_the_rack_demo.hdf5\\nput_the_wine_bottle_on_top_of_the_cabinet_demo.hdf5\\nturn_on_the_stove_demo.hdf5\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_action_trajectory_analysis_20260518T103905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T10:45:46.178216+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "python3 -c \"import h5py; f=h5py.File('/root/autodl-tmp/vla-ssd/data/libero/libero_goal/open_the_middle_drawer_of_the_cabinet_demo.hdf5','r'); print(list(f.keys())); print(list(f['data'].keys())); d=f['data/demo_0']; print(list(d.keys())); print(list(d['obs'].keys())); print('actions shape:', d['actions'].shape); print('rgb shape:', d['obs/agentview_rgb'].shape); f.close()\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_action_trajectory_analysis_20260518T103905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "python3 -c \"import h5py; f=h5py.File('/root/autodl-tmp/vla-ssd/data/libero/libero_goal/open_the_middle_drawer_of_the_cabinet_demo.hdf5','r'); print(list(f.keys())); print(list(f['data'].keys())); d=f['data/demo_0']; print(list(d.keys())); print(list(d['obs'].keys())); print('actions shape:', d['actions'].shape); print('rgb shape:', d['obs/agentview_rgb'].shape); f.close()\""
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-18T10:45:46.178347+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_action_trajectory_analysis_20260518T103905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T10:45:46.178469+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "python3 -c \"import h5py; f=h5py.File('/root/autodl-tmp/vla-ssd/data/libero/libero_goal/open_the_middle_drawer_of_the_cabinet_demo.hdf5','r'); print('num demos:', len(f['data'].keys())); print('demo_0 actions shape:', f['data/demo_0/actions'].shape); print('attrs:', dict(f['data'].attrs))\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_action_trajectory_analysis_20260518T103905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "python3 -c \"import h5py; f=h5py.File('/root/autodl-tmp/vla-ssd/data/libero/libero_goal/open_the_middle_drawer_of_the_cabinet_demo.hdf5','r'); print('num demos:', len(f['data'].keys())); print('demo_0 actions shape:', f['data/demo_0/actions'].shape); print('attrs:', dict(f['data'].attrs))\""
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-18T10:45:46.178637+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_action_trajectory_analysis_20260518T103905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T10:45:46.179291+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19183",
  "command": "python3 -c \"\nimport h5py\nf = h5py.File('/root/autodl-tmp/vla-ssd/data/libero/libero_goal/open_the_middle_drawer_of_the_cabinet_demo.hdf5','r')\nprint('keys:', list(f.keys()))\nprint('data keys:', sorted(f['data'].keys()))\nprint('num demos:', len(f['data'].keys()))\nd = f['data/demo_0']\nprint('demo_0 keys:', list(d.keys()))\nprint('obs keys:', list(d['obs'].keys()))\nprint('actions shape:', d['actions'].shape)\nprint('rgb shape:', d['obs/agentview_rgb'].shape)\nprint('attrs:', dict(f['data'].attrs))\nf.close()\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_action_trajectory_analysis_20260518T103905",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19183",
    "command": "python3 -c \"\nimport h5py\nf = h5py.File('/root/autodl-tmp/vla-ssd/data/libero/libero_goal/open_the_middle_drawer_of_the_cabinet_demo.hdf5','r')\nprint('keys:', list(f.keys()))\nprint('data keys:', sorted(f['data'].keys()))\nprint('num demos:', len(f['data'].keys()))\nd = f['data/demo_0']\nprint('demo_0 keys:', list(d.keys()))\nprint('obs keys:', list(d['obs'].keys()))\nprint('actions shape:', d['actions'].shape)\nprint('rgb shape:', d['obs/agentview_rgb'].shape)\nprint('attrs:', dict(f['data'].attrs))\nf.close()\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-18T10:45:46.179547+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'python3 -c \\\"\\\\nimport h5py\\\\nf = h5py.File(\\\\'/root/autodl-tmp/vla-ssd/data/libero/libero_goal/open_the_middle_drawer_of_the_cabinet_demo.hdf5\\\\',\\\\'r\\\\')\\\\nprint(\\\\'keys:\\\\', list(f.keys()))\\\\nprint(\\\\'data keys:\\\\', sorted(f[\\\\'data\\\\'].keys()))\\\\nprint(\\\\'num demos:\\\\', len(f[\\\\'data\\\\'].keys()))\\\\nd = f[\\\\'data/demo_0\\\\']\\\\nprint(\\\\'demo_0 keys:\\\\', list(d.keys()))\\\\nprint(\\\\'obs keys:\\\\', list(d[\\\\'obs\\\\'].keys()))\\\\nprint(\\\\'actions shape:\\\\', d[\\\\'actions\\\\'].shape)\\\\nprint(\\\\'rgb shape:\\\\', d[\\\\'obs/agentview_rgb\\\\'].shape)\\\\nprint(\\\\'attrs:\\\\', dict(f[\\\\'data\\\\'].attrs))\\\\nf.close()\\\\n\\\"\\\\n'\\n\\nExit code: 127\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 1: python3: command not found\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_action_trajectory_analysis_20260518T103905",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-18T10:45:46.179796+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19183",
  "command": "python3 -c \"\nimport sys\nsys.path.insert(0, '/root/autodl-tmp/LIBERO')\nfrom libero.libero import benchmark\nbench = benchmark.get_benchmark('libero_goal')()\nfor i in range(10):\n    t = bench.get_task(i)\n    print(f'{i}: {t.name} | {t.language}')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_action_trajectory_analysis_20260518T103905",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19183",
    "command": "python3 -c \"\nimport sys\nsys.path.insert(0, '/root/autodl-tmp/LIBERO')\nfrom libero.libero import benchmark\nbench = benchmark.get_benchmark('libero_goal')()\nfor i in range(10):\n    t = bench.get_task(i)\n    print(f'{i}: {t.name} | {t.language}')\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-18T10:45:46.180119+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'python3 -c \\\"\\\\nimport sys\\\\nsys.path.insert(0, \\\\'/root/autodl-tmp/LIBERO\\\\')\\\\nfrom libero.libero import benchmark\\\\nbench = benchmark.get_benchmark(\\\\'libero_goal\\\\')()\\\\nfor i in range(10):\\\\n    t = bench.get_task(i)\\\\n    print(f\\\\'{i}: {t.name} | {t.language}\\\\')\\\\n\\\"\\\\n'\\n\\nExit code: 127\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 1: python3: command not found\\n\\n\", \"metadata\": {\"elapsed_seconds\": 1.11}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_action_trajectory_analysis_20260518T103905",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-18T10:45:46.180274+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19183",
  "command": "bash -c \"source /root/miniconda3/bin/activate base && python -c \\\"\nimport h5py\nf = h5py.File('/root/autodl-tmp/vla-ssd/data/libero/libero_goal/open_the_middle_drawer_of_the_cabinet_demo.hdf5','r')\nprint('keys:', list(f.keys()))\nprint('data keys:', sorted(f['data'].keys()))\nprint('num demos:', len(f['data'].keys()))\nd = f['data/demo_0']\nprint('demo_0 keys:', list(d.keys()))\nprint('obs keys:', list(d['obs'].keys()))\nprint('actions shape:', d['actions'].shape)\nprint('rgb shape:', d['obs/agentview_rgb'].shape)\nprint('attrs:', dict(f['data'].attrs))\nf.close()\n\\\"\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_action_trajectory_analysis_20260518T103905",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19183",
    "command": "bash -c \"source /root/miniconda3/bin/activate base && python -c \\\"\nimport h5py\nf = h5py.File('/root/autodl-tmp/vla-ssd/data/libero/libero_goal/open_the_middle_drawer_of_the_cabinet_demo.hdf5','r')\nprint('keys:', list(f.keys()))\nprint('data keys:', sorted(f['data'].keys()))\nprint('num demos:', len(f['data'].keys()))\nd = f['data/demo_0']\nprint('demo_0 keys:', list(d.keys()))\nprint('obs keys:', list(d['obs'].keys()))\nprint('actions shape:', d['actions'].shape)\nprint('rgb shape:', d['obs/agentview_rgb'].shape)\nprint('attrs:', dict(f['data'].attrs))\nf.close()\n\\\"\""
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-18T10:45:46.180460+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"keys: ['data']\\ndata keys: ['demo_0', 'demo_1', 'demo_10', 'demo_11', 'demo_12', 'demo_13', 'demo_14', 'demo_15', 'demo_16', 'demo_17', 'demo_18', 'demo_19', 'demo_2', 'demo_20', 'demo_21', 'demo_22', 'demo_23', 'demo_24', 'demo_25', 'demo_26', 'demo_27', 'demo_28', 'demo_29', 'demo_3', 'demo_30', 'demo_31', 'demo_32', 'demo_33', 'demo_34', 'demo_35', 'demo_36', 'demo_37', 'demo_38', 'demo_39', 'demo_4', 'demo_40', 'demo_41', 'demo_42', 'demo_43', 'demo_44', 'demo_45', 'demo_46', 'demo_47', 'demo_48', 'demo_49', 'demo_5', 'demo_6', 'demo_7', 'demo_8', 'demo_9']\\nnum demos: 50\\ndemo_0 keys: ['actions', 'dones', 'obs', 'rewards', 'robot_states', 'states']\\nobs keys: ['agentview_rgb', 'ee_ori', 'ee_pos', 'ee_states', 'eye_in_hand_rgb', 'gripper_states', 'joint_states']\\nactions shape: (138, 7)\\nrgb shape: (138, 128, 128, 3)\\nattrs: {'bddl_file_name': 'libero/libero/bddl_files/libero_goal/open_the_middle_drawer_of_the_cabinet.bddl', 'env_args': '{\\\"type\\\": 1, \\\"env_name\\\": \\\"Libero_Tabletop_Manipulation\\\", \\\"problem_name\\\": \\\"libero_tabletop_manipulation\\\", \\\"bddl_file\\\": \\\"chiliocosm/bddl_files/libero_goal/open_the_middle_layer_of_the_drawer.bddl\\\", \\\"env_kwargs\\\": {\\\"robots\\\": [\\\"Panda\\\"], \\\"controller_configs\\\": {\\\"type\\\": \\\"OSC_POSE\\\", \\\"input_max\\\": 1, \\\"input_min\\\": -1, \\\"output_max\\\": [0.05, 0.05, 0.05, 0.5, 0.5, 0.5], \\\"output_min\\\": [-0.05, -0.05, -0.05, -0.5, -0.5, -0.5], \\\"kp\\\": 150, \\\"damping_ratio\\\": 1, \\\"impedance_mode\\\": \\\"fixed\\\", \\\"kp_limits\\\": [0, 300], \\\"damping_ratio_limits\\\": [0, 10], \\\"position_limits\\\": null, \\\"orientation_limits\\\": null, \\\"uncouple_pos_ori\\\": true, \\\"control_delta\\\": true, \\\"interpolation\\\": null, \\\"ramp_ratio\\\": 0.2}, \\\"bddl_file_name\\\": \\\"chiliocosm/bddl_files/libero_goal/open_the_middle_layer_of_the_drawer.bddl\\\", \\\"has_renderer\\\": false, 
…[truncated 784 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_action_trajectory_analysis_20260518T103905",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-18T10:45:46.180668+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19183",
  "command": "bash -c \"source /root/miniconda3/bin/activate base && head -160 /root/vla-ssd/scripts/behavioral_pilot.py | tail -80\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_action_trajectory_analysis_20260518T103905",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19183",
    "command": "bash -c \"source /root/miniconda3/bin/activate base && head -160 /root/vla-ssd/scripts/behavioral_pilot.py | tail -80\""
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-18T10:45:46.180877+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"            device=input_ids.device, dtype=input_ids.dtype,\\n        )\\n        with torch.no_grad():\\n            outputs = model(\\n                input_ids=next_token,\\n                attention_mask=attn_mask,\\n                pixel_values=None,\\n                past_key_values=past_key_values,\\n                use_cache=True,\\n            )\\n        past_key_values = outputs.past_key_values\\n        next_token_logits = outputs.logits[:, -1, :]\\n\\n    predicted_action_token_ids = np.array(generated_ids)\\n    discretized_actions = model.vocab_size - predicted_action_token_ids\\n    discretized_actions = np.clip(discretized_actions - 1, a_min=0, a_max=model.bin_centers.shape[0] - 1)\\n    normalized_actions = model.bin_centers[discretized_actions]\\n    action_norm_stats = model.get_action_stats(unnorm_key)\\n    mask = action_norm_stats.get(\\\"mask\\\", np.ones_like(action_norm_stats[\\\"q01\\\"], dtype=bool))\\n    action_high, action_low = np.array(action_norm_stats[\\\"q99\\\"]), np.array(action_norm_stats[\\\"q01\\\"])\\n    return np.where(\\n        mask,\\n        0.5 * (normalized_actions + 1) * (action_high - action_low) + action_low,\\n        normalized_actions,\\n    )\\n\\n\\n# ── Ablation hook ──────────────────────────────────────────────────────────\\ndef install_ablation_hook(model, heads_to_ablate):\\n    import transformers.models.llama.modeling_llama as llama_mod\\n    from transformers.models.llama.modeling_llama import repeat_kv\\n\\n    layer1_attn = model.language_model.model.layers[1].self_attn\\n    layer1_attn._ablate_heads = heads_to_ablate\\n\\n    original_fn = llama_mod.eager_attention_forward\\n\\n    def ablated_eager_attention_forward(module, query, key, value, attention_mask,\\n                                        scaling, dropout=0.0, **kwargs):\\n        key_states = repeat_kv(key, module.num_key_value_groups)\\n        value_states = repeat_kv(value, mo
…[truncated 2174 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_action_trajectory_analysis_20260518T103905",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-18T10:45:46.181106+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19183",
  "command": "bash -c \"source /root/miniconda3/bin/activate base && python -c \\\"\nimport h5py, json\nf = h5py.File('/root/autodl-tmp/vla-ssd/data/libero/libero_goal/open_the_middle_drawer_of_the_cabinet_demo.hdf5','r')\ninfo = json.loads(f['data'].attrs['problem_info'])\nprint('language_instruction:', info['language_instruction'])\nf.close()\n\\\"\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_action_trajectory_analysis_20260518T103905",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19183",
    "command": "bash -c \"source /root/miniconda3/bin/activate base && python -c \\\"\nimport h5py, json\nf = h5py.File('/root/autodl-tmp/vla-ssd/data/libero/libero_goal/open_the_middle_drawer_of_the_cabinet_demo.hdf5','r')\ninfo = json.loads(f['data'].attrs['problem_info'])\nprint('language_instruction:', info['language_instruction'])\nf.close()\n\\\"\""
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-18T10:45:46.181258+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"language_instruction: open the middle drawer of the cabinet\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.62}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_action_trajectory_analysis_20260518T103905",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-18T10:45:46.181417+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19183",
  "command": "bash -c \"source /root/miniconda3/bin/activate base && sed -n '155,185p' /root/vla-ssd/scripts/behavioral_pilot.py\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_action_trajectory_analysis_20260518T103905",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19183",
    "command": "bash -c \"source /root/miniconda3/bin/activate base && sed -n '155,185p' /root/vla-ssd/scripts/behavioral_pilot.py\""
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-18T10:45:46.181680+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    return model, processor\\n\\n\\ndef get_action(model, processor, image_array, instruction):\\n    img = Image.fromarray(image_array)\\n    prompt = f\\\"In: What action should the robot take to {instruction}?\\\\nOut:\\\"\\n    inputs = processor(prompt, img).to(\\\"cuda:0\\\", dtype=torch.bfloat16)\\n    return predict_action_manual(model, inputs[\\\"input_ids\\\"], inputs[\\\"pixel_values\\\"], UNNORM_KEY)\\n\\n\\n# ── Main ───────────────────────────────────────────────────────────────────\\ndef main():\\n    os.makedirs(RESULTS_DIR, exist_ok=True)\\n    print(\\\"Loading model...\\\")\\n    model, processor = load_model()\\n    print(\\\"Model loaded.\\\")\\n\\n    import transformers.models.llama.modeling_llama as llama_mod\\n    original_eager_fn = llama_mod.eager_attention_forward\\n\\n    model.language_model.model.layers[1].self_attn._ablate_heads = None\\n\\n    bench = benchmark.get_benchmark(\\\"libero_goal\\\")()\\n    all_results = {}\\n    task_names = []\\n\\n    for task_id in TASK_IDS:\\n        task = bench.get_task(task_id)\\n        task_name = task.name\\n        task_lang = task.language\\n        task_names.append(task_name)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_action_trajectory_analysis_20260518T103905",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-18T10:45:46.181844+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

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
  "session": "worker_code_action_trajectory_analysis_20260518T103905",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19183",
    "command": "ls /root/autodl-tmp/vla-ssd/results/"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-18T10:45:46.182047+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"ablations\\naction_baselines.json\\naction_probe\\nanalysis\\narchitecture_audit\\nattention\\nbootstrap_ci_values.json\\ncka\\ncross_instruction\\ncross_instruction_dense\\ncross_instruction_spatial\\ndemo_sensitivity_25\\ndinov2\\ndinov2_libero_goal\\ndinov2_libero_goal_frame0\\ndinov2_libero_goal_linear\\ndinov2_libero_goal_pca1024\\ndinov2_shuffle\\nfigure_data\\nfigures\\nfunctional_validation\\nl1_head_ablation\\nlinear_probe.log\\nlinear_probe_last_preaction.json\\nlinear_probe_results.json\\nllama2base_action_probe\\nood_diagnostics.json\\nood_diagnostics.log\\noracle\\noutput_head_analysis.json\\npca1024_linear_perlayer.json\\npca1024_linear_pertimestep.json\\nperlayer_rsa\\nqa_probe\\nrandom_subset_ablation.json\\nrandom_subset_ablation.log\\nrsa\\nshuffled_token_control.json\\nthreecond_multiseed.json\\nthreecond_multiseed.log\\nthreecond_multiseed_v2.json\\nthreecond_multiseed_v2.log\\ntrained\\ntrained_label_perm\\ntrained_libero_goal\\ntrained_libero_goal_frame0\\ntrained_libero_goal_linear\\ntrained_libero_goal_pca1024\\nuntrained\\nuntrained_label_perm\\nuntrained_libero_goal\\nuntrained_libero_goal_frame0\\nuntrained_libero_goal_linear\\nvisual_similarity_gate.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_action_trajectory_analysis_20260518T103905",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-18T10:45:46.182391+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/action_trajectory_analysis.py",
  "content": "\"\"\"Open-loop action trajectory analysis: baseline vs L1-ablated on LIBERO demo observations.\"\"\"\n\nimport argparse\nimport gc\nimport glob\nimport json\nimport os\nimport sys\nimport time\n\nsys.path.insert(0, \"/root/autodl-tmp/LIBERO\")\n\nos.environ[\"MUJOCO_GL\"] = \"egl\"\nos.environ[\"HDF5_USE_FILE_LOCKING\"] = \"FALSE\"\n\nimport h5py\nimport numpy as np\nimport torch\nimport torch.nn as nn\nimport torch.nn.functional as F\nfrom PIL import Image\nfrom scipy import stats\n\nnp.random.seed(42)\ntorch.manual_seed(42)\n\n# ── Config ──────────────────────────────────────────────────────────────────\nMODEL_PATH = \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\"\nUNNORM_KEY = \"bridge_orig\"\nDATA_DIR = \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal\"\nRESULTS_DIR = \"/root/autodl-tmp/vla-ssd/results\"\n\nNUM_IMAGE_TOKENS = 256\nINST_START = 1 + NUM_IMAGE_TOKENS\n\nINSTRUCTION_HEADS_24 = [\n    0, 1, 2, 4, 7, 8, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20,\n    22, 23, 25, 26, 27, 29, 30, 31,\n]\n\nDIM_NAMES = [\"dx\", \"dy\", \"dz\", \"rx\", \"ry\", \"rz\", \"gripper\"]\n\n\n# ── Model loading ───────────────────────────────────────────────────────────\ndef load_model():\n    from transformers import AutoModelForVision2Seq, AutoProcessor\n\n    processor = AutoProcessor.from_pretrained(MODEL_PATH, trust_remote_code=True)\n    model = AutoModelForVision2Seq.from_pretrained(\n        MODEL_PATH,\n        torch_dtype=torch.bfloat16,\n        trust_remote_code=True,\n        low_cpu_mem_usage=True,\n    ).to(\"cuda:0\").eval()\n    return model, processor\n\n\n# ── Manual autoregressive generation (bypasses generate() DynamicCache bug) ─\ndef predict_action_with_logits(model, input_ids, pixel_values, unnorm_key):\n    action_dim = model.get_action_dim(unnorm_key)\n    if not torch.all(input_ids[:, -1] == 29871):\n        input_ids = torch.cat(\n            (input_ids, torch.tensor([[29871]], device=input_ids.device, dtype=input_ids.dtype)),\n            dim=1,\n        )\n    with torch.no_grad():\n        outputs = model(\n            input_ids=input_ids,\n            attention_mask=torch.ones_like(input_ids),\n            pixel_values=pixel_values,\n            past_key_values=None,\n            use_cache=True,\n        )\n    past_key_values = outputs.past_key_values\n    next_token_logits = outputs.logits[:, -1, :]\n\n    generated_ids = []\n    all_logits = []\n\n    for _ in range(action_dim):\n        all_logits.append(next_token_logits.float().cpu())\n        next_token = torch.argmax(next_token_logits, dim=-1, keepdim=True)\n        generated_ids.append(next_token.squeeze().item())\n        attn_mask = torch.ones(\n            (1, past_key_values[0][0].shape[2] + 1),\n            device=input_ids.device,\n            dtype=input_ids.dtype,\n        )\n        with torch.no_grad():\n            outputs = model(\n                input_ids=next_token,\n                attention_mask=attn_mask,\n                pixel_values=None,\n                past_key_values=past_key_values,\n                use_cache=True,\n            )\n        past_key_values = outputs.past_key_values\n        next_token_logits = outputs.logits[:, -1, :]\n\n    predicted_action_token_ids = np.array(generated_ids)\n    discretized_actions = model.vocab_size - predicted_action_token_ids\n    discretized_actions = np.clip(\n        discretized_actions - 1, a_min=0, a_max=model.bin_centers.shape[0] - 1\n    )\n    normalized_actions = model.bin_centers[discretized_actions]\n    action_norm_stats = model.get_action_stats(unnorm_key)\n    mask = action_norm_stats.get(\"mask\", np.ones_like(action_norm_stats[\"q01\"], dtype=bool))\n    action_high = np.array(action_norm_stats[\"q99\"])\n    action_low = np.array(action_norm_stats[\"q01\"])\n    action = np.where(\n        mask,\n        0.5 * (normalized_actions + 1) * (action_high - action_low) + action_low,\n        normalized_actions,\n    )\n\n    logits_tensor = torch.cat(all_logits, dim=0)  # (action_dim, vocab_size)\n    return action, predicted_action_token_ids, logits_tensor\n\n\n# ── Ablation hook ───────────────────────────────────────────────────────────\ndef install_ablation_hook(model, heads_to_ablate):\n    import transformers.models.llama.modeling_llama as llama_mod\n    from transformers.models.llama.modeling_llama import repeat_kv\n\n    layer_attn = model.language_model.model.layers[1].self_attn\n    layer_attn._ablate_heads = heads_to_ablate\n\n    original_fn = llama_mod.eager_attention_forward\n\n    def ablated_eager_attention_forward(\n        module, query, key, value, attention_mask, scaling, dropout=0.0, **kwargs\n    ):\n        key_states = repeat_kv(key, module.num_key_value_groups)\n        value_states = repeat_kv(value, module.num_key_value_groups)\n        attn_weights = torch.matmul(query, key_states.transpose(2, 3)) * scaling\n        if attention_mask is not None:\n            causal_mask = attention_mask[:, :, :, : key_states.shape[-2]]\n            attn_weights = attn_weights + causal_mask\n        attn_weights = nn.functional.softmax(attn_weights, dim=-1, dtype=torch.float32).to(\n            query.dtype\n        )\n        attn_weights = nn.functional.dropout(attn_weights, p=dropout, training=module.training)\n        if hasattr(module, \"_ablate_heads\") and module._ablate_heads is not None:\n            kv_len = attn_weights.shape[-1]\n            if INST_START < kv_len:\n                attn_weights[:, module._ablate_heads, :, INST_START:] = 0.0\n                row_sums = attn_weights.sum(dim=-1, keepdim=True).clamp(min=1e-9)\n                attn_weights = attn_weights / row_sums\n        attn_output = torch.matmul(attn_weights, value_states)\n        attn_output = attn_output.transpose(1, 2).contiguous()\n        return attn_output, attn_weights\n\n    llama_mod.eager_attention_forward = ablated_eager_attention_forward\n    return original_fn\n\n\ndef remove_ablation_hook(model, original_fn):\n    import transformers.models.llama.modeling_llama as llama_mod\n\n    llama_mod.eager_attention_forward = original_fn\n    model.language_model.model.layers[1].self_attn._ablate_heads = None\n\n\n# ── KL divergence ───────────────────────────────────────────────────────────\ndef compute_kl_divergence(logits_p, logits_q):\n    log_p = F.log_softmax(logits_p, dim=-1)\n    log_q = F.log_softmax(logits_q, dim=-1)\n    p = F.softmax(logits_p, dim=-1)\n    kl = (p * (log_p - log_q)).sum(dim=-1)\n    return kl.numpy()\n\n\n# ── Helpers ─────────────────────────────────────────────────────────────────\ndef get_task_files(n_tasks):\n    hdf5_files = sorted(glob.glob(os.path.join(DATA_DIR, \"*.hdf5\")))\n    return hdf5_files[:n_tasks]\n\n\ndef get_language_instruction(hdf5_path):\n    with h5py.File(hdf5_path, \"r\") as f:\n        info = json.loads(f[\"data\"].attrs[\"problem_info\"])\n    return info[\"language_instruction\"]\n\n\ndef compute_task_metrics(task_b, task_a, task_b_ids, task_a_ids, task_kls):\n    paired_mse = np.mean((task_b - task_a) ** 2, axis=1)\n    t_res = stats.ttest_1samp(paired_mse, 0)\n    cohens_d = np.mean(paired_mse) / (np.std(paired_mse, ddof=1) + 1e-12)\n\n    per_dim_shift = np.abs(task_b - task_a)\n    token_div = np.mean(task_b_ids != task_a_ids)\n\n    return {\n        \"paired_mse\": {\n            \"mean\": float(np.mean(paired_mse)),\n            \"std\": float(np.std(paired_mse)),\n            \"t_stat\": float(t_res.statistic),\n            \"p_value\": float(t_res.pvalue),\n            \"cohens_d\": float(cohens_d),\n        },\n        \"per_dim_shift\": {\n            \"means\": [float(x) for x in np.mean(per_dim_shift, axis=0)],\n            \"stds\": [float(x) for x in np.std(per_dim_shift, axis=0)],\n        },\n        \"token_divergence_rate\": float(token_div),\n        \"kl_divergence\": {\n            \"mean\": float(np.mean(task_kls)),\n            \"std\": float(np.std(task_kls)),\n        },\n        \"n_samples\": int(len(task_b)),\n    }\n\n\n# ── Main ────────────────────────────────────────────────────────────────────\ndef main():\n    parser = argparse.ArgumentParser()\n    parser.add_argument(\"--dry-run\", action=\"store_true\")\n    args = parser.parse_args()\n\n    n_tasks = 1 if args.dry_run else 5\n    n_demos = 1 if args.dry_run else 10\n    n_timesteps = 2 if args.dry_run else 50\n\n    os.makedirs(RESULTS_DIR, exist_ok=True)\n\n    print(\"Loading model...\")\n    model, processor = load_model()\n    print(\"Model loaded.\")\n\n    original_eager_fn = install_ablation_hook(model, INSTRUCTION_HEADS_24)\n    layer1_attn = model.language_model.model.layers[1].self_attn\n\n    task_files = get_task_files(n_tasks)\n    print(f\"Tasks ({n_tasks}): {[os.path.basename(f) for f in task_files]}\")\n    print(f\"Config: {n_demos} demos/task, {n_timesteps} timesteps/demo\")\n\n    all_baseline_actions = []\n    all_ablated_actions = []\n    all_gt_actions = []\n    all_baseline_token_ids = []\n    all_ablated_token_ids = []\n    all_kl_divs = []\n    per_task_data = {}\n\n    total_passes = 0\n    t_start = time.time()\n\n    for task_idx, hdf5_path in enumerate(task_files):\n        task_name = os.path.basename(hdf5_path).replace(\"_demo.hdf5\", \"\")\n        instruction = get_language_instruction(hdf5_path)\n        print(f\"\\n{'='*60}\")\n        print(f\"Task {task_idx}: {task_name}\")\n        print(f\"  Instruction: {instruction}\")\n\n        task_baseline_actions = []\n        task_ablated_actions = []\n        task_gt_actions = []\n        task_baseline_token_ids = []\n        task_ablated_token_ids = []\n        task_kl_divs = []\n\n        prompt = f\"In: What action should the robot take to {instruction}?\\nOut:\"\n\n        with h5py.File(hdf5_path, \"r\") as f:\n            for demo_idx in range(n_demos):\n                demo_key = f\"data/demo_{demo_idx}\"\n                actions_data = f[f\"{demo_key}/actions\"][:]\n                images_data = f[f\"{demo_key}/obs/agentview_rgb\"][:]\n                n_steps = min(n_timesteps, len(actions_data))\n\n                for step_idx in range(n_steps):\n                    image_np = images_data[step_idx]\n                    gt_action = actions_data[step_idx]\n\n                    img = Image.fromarray(image_np)\n                    inputs = processor(prompt, img).to(\"cuda:0\", dtype=torch.bfloat16)\n                    input_ids = inputs[\"input_ids\"]\n                    pixel_values = inputs[\"pixel_values\"]\n\n                    # Baseline (ablation disabled)\n                    layer1_attn._ablate_heads = None\n                    b_action, b_ids, b_logits = predict_action_with_logits(\n                        model, input_ids, pixel_values, UNNORM_KEY\n                    )\n\n                    # Ablated\n                    layer1_attn._ablate_heads = INSTRUCTION_HEADS_24\n                    a_action, a_ids, a_logits = predict_action_with_logits(\n                        model, input_ids, pixel_values, UNNORM_KEY\n                    )\n\n                    kl_per_token = compute_kl_divergence(b_logits, a_logits)\n\n                    task_baseline_actions.append(b_action)\n                    task_ablated_actions.append(a_action)\n                    task_gt_actions.append(gt_action)\n                    task_baseline_token_ids.append(b_ids)\n                    task_ablated_token_ids.append(a_ids)\n                    task_kl_divs.append(kl_per_token)\n\n                    total_passes += 2\n                    if total_passes % 100 == 0:\n                        elapsed = time.time() - t_start\n                        rate = total_passes / elapsed\n                        eta = (n_tasks * n_demos * n_timesteps * 2 - total_passes) / rate\n                        print(\n                            f\"  [{total_passes} passes, {elapsed:.0f}s, \"\n                            f\"{rate:.1f} pass/s, ETA {eta:.0f}s]\"\n                        )\n\n                    del b_logits, a_logits\n                    torch.cuda.empty_cache()\n\n        task_b = np.array(task_baseline_actions)\n        task_a = np.array(task_ablated_actions)\n        task_b_ids = np.array(task_baseline_token_ids)\n        task_a_ids = np.array(task_ablated_token_ids)\n        task_kls = np.array(task_kl_divs)\n\n        per_task_data[task_name] = compute_task_metrics(\n            task_b, task_a, task_b_ids, task_a_ids, task_kls\n        )\n        m = per_task_data[task_name]\n        print(\n            f\"  >> paired_mse={m['paired_mse']['mean']:.6f}, \"\n            f\"token_div={m['token_divergence_rate']:.4f}, \"\n            f\"kl={m['kl_divergence']['mean']:.4f}\"\n        )\n\n        all_baseline_actions.extend(task_baseline_actions)\n        all_ablated_actions.extend(task_ablated_actions)\n        all_gt_actions.extend(task_gt_actions)\n        all_baseline_token_ids.extend(task_baseline_token_ids)\n        all_ablated_token_ids.extend(task_ablated_token_ids)\n        all_kl_divs.extend(task_kl_divs)\n\n        gc.collect()\n        torch.cuda.empty_cache()\n\n    # ── Global metrics ──────────────────────────────────────────────────────\n    layer1_attn._ablate_heads = None\n    remove_ablation_hook(model, original_eager_fn)\n\n    all_b = np.array(all_baseline_actions)\n    all_a = np.array(all_ablated_actions)\n    all_gt = np.array(all_gt_actions)\n    all_b_ids = np.array(all_baseline_token_ids)\n    all_a_ids = np.array(all_ablated_token_ids)\n    all_kls = np.array(all_kl_divs)\n\n    paired_mse_all = np.mean((all_b - all_a) ** 2, axis=1)\n    t_res_all = stats.ttest_1samp(paired_mse_all, 0)\n    cohens_d_all = np.mean(paired_mse_all) / (np.std(paired_mse_all, ddof=1) + 1e-12)\n\n    per_dim_shift_all = np.abs(all_b - all_a)\n    token_div_all = np.mean(all_b_ids != all_a_ids)\n\n    kl_per_position = np.mean(all_kls, axis=0)\n\n    mse_gt_baseline = np.mean((all_b - all_gt) ** 2, axis=1)\n    mse_gt_ablated = np.mean((all_a - all_gt) ** 2, axis=1)\n\n    try:\n        wilcoxon_res = stats.wilcoxon(paired_mse_all)\n        wilcoxon_p = float(wilcoxon_res.pvalue)\n    except Exception:\n        wilcoxon_p = None\n\n    output = {\n        \"config\": {\n            \"n_tasks\": n_tasks,\n            \"n_demos_per_task\": n_demos,\n            \"n_timesteps_per_demo\": n_timesteps,\n            \"total_forward_passes\": total_passes,\n            \"model\": \"openvla-7b\",\n            \"ablation\": \"L1_dominant_24_heads_zeroed\",\n            \"ablated_heads\": INSTRUCTION_HEADS_24,\n            \"unnorm_key\": UNNORM_KEY,\n        },\n        \"main_metrics\": {\n            \"paired_action_mse\": {\n                \"mean\": float(np.mean(paired_mse_all)),\n                \"std\": float(np.std(paired_mse_all)),\n                \"t_stat\": float(t_res_all.statistic),\n                \"p_value\": float(t_res_all.pvalue),\n                \"cohens_d\": float(cohens_d_all),\n            },\n            \"per_dim_action_shift\": {\n                \"means\": [float(x) for x in np.mean(per_dim_shift_all, axis=0)],\n                \"stds\": [float(x) for x in np.std(per_dim_shift_all, axis=0)],\n                \"dim_names\": DIM_NAMES,\n            },\n            \"token_divergence_rate\": float(token_div_all),\n        },\n        \"secondary_metrics\": {\n            \"kl_divergence\": {\n                \"mean\": float(np.mean(all_kls)),\n                \"std\": float(np.std(all_kls)),\n                \"per_token_position\": [float(x) for x in kl_per_position],\n            },\n            \"mse_vs_gt_baseline\": {\n                \"mean\": float(np.mean(mse_gt_baseline)),\n                \"std\": float(np.std(mse_gt_baseline)),\n                \"note\": \"OOD, secondary\",\n            },\n            \"mse_vs_gt_ablated\": {\n                \"mean\": float(np.mean(mse_gt_ablated)),\n                \"std\": float(np.std(mse_gt_ablated)),\n                \"note\": \"OOD, secondary\",\n            },\n            \"wilcoxon_p\": wilcoxon_p,\n        },\n        \"per_task\": per_task_data,\n    }\n\n    elapsed_total = time.time() - t_start\n    print(f\"\\n{'='*60}\")\n    print(f\"Done. {total_passes} forward passes in {elapsed_total:.0f}s\")\n    print(\n        f\"Paired MSE: {np.mean(paired_mse_all):.6f} \"\n        f\"(p={t_res_all.pvalue:.2e}, d={cohens_d_all:.3f})\"\n    )\n    print(f\"Token divergence: {token_div_all:.4f}\")\n    print(f\"KL divergence: {np.mean(all_kls):.4f}\")\n    print(f\"MSE vs GT - baseline: {np.mean(mse_gt_baseline):.6f}, ablated: {np.mean(mse_gt_ablated):.6f}\")\n\n    out_path = os.path.join(RESULTS_DIR, \"action_trajectory_analysis.json\")\n    with open(out_path, \"w\") as f:\n        json.dump(output, f, indent=2)\n    print(f\"Results saved to {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_action_trajectory_analysis_20260518T103905",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/action_trajectory_analysis.py",
    "content": "\"\"\"Open-loop action trajectory analysis: baseline vs L1-ablated on LIBERO demo observations.\"\"\"\n\nimport argparse\nimport gc\nimport glob\nimport json\nimport os\nimport sys\nimport time\n\nsys.path.insert(0, \"/root/autodl-tmp/LIBERO\")\n\nos.environ[\"MUJOCO_GL\"] = \"egl\"\nos.environ[\"HDF5_USE_FILE_LOCKING\"] = \"FALSE\"\n\nimport h5py\nimport numpy as np\nimport torch\nimport torch.nn as nn\nimport torch.nn.functional as F\nfrom PIL import Image\nfrom scipy import stats\n\nnp.random.seed(42)\ntorch.manual_seed(42)\n\n# ── Config ──────────────────────────────────────────────────────────────────\nMODEL_PATH = \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\"\nUNNORM_KEY = \"bridge_orig\"\nDATA_DIR = \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal\"\nRESULTS_DIR = \"/root/autodl-tmp/vla-ssd/results\"\n\nNUM_IMAGE_TOKENS = 256\nINST_START = 1 + NUM_IMAGE_TOKENS\n\nINSTRUCTION_HEADS_24 = [\n    0, 1, 2, 4, 7, 8, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20,\n    22, 23, 25, 26, 27, 29, 30, 31,\n]\n\nDIM_NAMES = [\"dx\", \"dy\", \"dz\", \"rx\", \"ry\", \"rz\", \"gripper\"]\n\n\n# ── Model loading ───────────────────────────────────────────────────────────\ndef load_model():\n    from transformers import AutoModelForVision2Seq, AutoProcessor\n\n    processor = AutoProcessor.from_pretrained(MODEL_PATH, trust_remote_code=True)\n    model = AutoModelForVision2Seq.from_pretrained(\n        MODEL_PATH,\n        torch_dtype=torch.bfloat16,\n        trust_remote_code=True,\n        low_cpu_mem_usage=True,\n    ).to(\"cuda:0\").eval()\n    return model, processor\n\n\n# ── Manual autoregressive generation (bypasses generate() DynamicCache bug) ─\ndef predict_action_with_logits(model, input_ids, pixel_values, unnorm_key):\n    action_dim = model.get_action_dim(unnorm_key)\n    if not torch.all(input_ids[:, -1] == 29871):\n        input_ids = torch.cat(\n            (input_ids, torch.tensor([[29871]], device=input_ids.device, dtype=input_ids.dtype)),\n            dim=1,\n        )\n    with torch.no_grad():\n        outputs = model(\n            input_ids=input_ids,\n            attention_mask=torch.ones_like(input_ids),\n            pixel_values=pixel_values,\n            past_key_values=None,\n            use_cache=True,\n        )\n    past_key_values = outputs.past_key_values\n    next_token_logits = outputs.logits[:, -1, :]\n\n    generated_ids = []\n    all_logits = []\n\n    for _ in range(action_dim):\n        all_logits.append(next_token_logits.float().cpu())\n        next_token = torch.argmax(next_token_logits, dim=-1, keepdim=True)\n        generated_ids.append(next_token.squeeze().item())\n        attn_mask = torch.ones(\n            (1, past_key_values[0][0].shape[2] + 1),\n            device=input_ids.device,\n            dtype=input_ids.dtype,\n        )\n        with torch.no_grad():\n            outputs = model(\n                input_ids=next_token,\n                attention_mask=attn_mask,\n                pixel_values=None,\n                past_key_values=past_key_values,\n                use_cache=True,\n            )\n        past_key_values = outputs.past_key_values\n        next_token_logits = outputs.logits[:, -1, :]\n\n    predicted_action_token_ids = np.array(generated_ids)\n    discretized_actions = model.vocab_size - predicted_action_token_ids\n    discretized_actions = np.clip(\n        discretized_actions - 1, a_min=0, a_max=model.bin_centers.shape[0] - 1\n    )\n    normalized_actions = model.bin_centers[discretized_actions]\n    action_norm_stats = model.get_action_stats(unnorm_key)\n    mask = action_norm_stats.get(\"mask\", np.ones_like(action_norm_stats[\"q01\"], dtype=bool))\n    action_high = np.array(action_norm_stats[\"q99\"])\n    action_low = np.array(action_norm_stats[\"q01\"])\n    action = np.where(\n        mask,\n        0.5 * (normalized_actions + 1) * (action_high - action_low) + action_low,\n        normalized_actions,\n    )\n\n    logits_tensor = torch.cat(all_logits, dim=0)  # (action_dim, vocab_size)\n    return action, predicted_action_token_ids, logits_tensor\n\n\n# ── Ablation hook ───────────────────────────────────────────────────────────\ndef install_ablation_hook(model, heads_to_ablate):\n    import transformers.models.llama.modeling_llama as llama_mod\n    from transformers.models.llama.modeling_llama import repeat_kv\n\n    layer_attn = model.language_model.model.layers[1].self_attn\n    layer_attn._ablate_heads = heads_to_ablate\n\n    original_fn = llama_mod.eager_attention_forward\n\n    def ablated_eager_attention_forward(\n        module, query, key, value, attention_mask, scaling, dropout=0.0, **kwargs\n    ):\n        key_states = repeat_kv(key, module.num_key_value_groups)\n        value_states = repeat_kv(value, module.num_key_value_groups)\n        attn_weights = torch.matmul(query, key_states.transpose(2, 3)) * scaling\n        if attention_mask is not None:\n            causal_mask = attention_mask[:, :, :, : key_states.shape[-2]]\n            attn_weights = attn_weights + causal_mask\n        attn_weights = nn.functional.softmax(attn_weights, dim=-1, dtype=torch.float32).to(\n            query.dtype\n        )\n        attn_weights = nn.functional.dropout(attn_weights, p=dropout, training=module.training)\n        if hasattr(module, \"_ablate_heads\") and module._ablate_heads is not None:\n            kv_len = attn_weights.shape[-1]\n            if INST_START < kv_len:\n                attn_weights[:, module._ablate_heads, :, INST_START:] = 0.0\n                row_sums = attn_weights.sum(dim=-1, keepdim=True).clamp(min=1e-9)\n                attn_weights = attn_weights / row_sums\n        attn_output = torch.matmul(attn_weights, value_states)\n        attn_output = attn_output.transpose(1, 2).contiguous()\n        return attn_output, attn_weights\n\n    llama_mod.eager_attention_forward = ablated_eager_attention_forward\n    return original_fn\n\n\ndef remove_ablation_hook(model, original_fn):\n    import transformers.models.llama.modeling_llama as llama_mod\n\n    llama_mod.eager_attention_forward = original_fn\n    model.language_model.model.layers[1].self_attn._ablate_heads = None\n\n\n# ── KL divergence ───────────────────────────────────────────────────────────\ndef compute_kl_divergence(logits_p, logits_q):\n    log_p = F.log_softmax(logits_p, dim=-1)\n    log_q = F.log_softmax(logits_q, dim=-1)\n    p = F.softmax(logits_p, dim=-1)\n    kl = (p * (log_p - log_q)).sum(dim=-1)\n    return kl.numpy()\n\n\n# ── Helpers ─────────────────────────────────────────────────────────────────\ndef get_task_files(n_tasks):\n    hdf5_files = sorted(glob.glob(os.path.join(DATA_DIR, \"*.hdf5\")))\n    return hdf5_files[:n_tasks]\n\n\ndef get_language_instruction(hdf5_path):\n    with h5py.File(hdf5_path, \"r\") as f:\n        info = json.loads(f[\"data\"].attrs[\"problem_info\"])\n    return info[\"language_instruction\"]\n\n\ndef compute_task_metrics(task_b, task_a, task_b_ids, task_a_ids, task_kls):\n    paired_mse = np.mean((task_b - task_a) ** 2, axis=1)\n    t_res = stats.ttest_1samp(paired_mse, 0)\n    cohens_d = np.mean(paired_mse) / (np.std(paired_mse, ddof=1) + 1e-12)\n\n    per_dim_shift = np.abs(task_b - task_a)\n    token_div = np.mean(task_b_ids != task_a_ids)\n\n    return {\n        \"paired_mse\": {\n            \"mean\": float(np.mean(paired_mse)),\n            \"std\": float(np.std(paired_mse)),\n            \"t_stat\": float(t_res.statistic),\n            \"p_value\": float(t_res.pvalue),\n            \"cohens_d\": float(cohens_d),\n        },\n        \"per_dim_shift\": {\n            \"means\": [float(x) for x in np.mean(per_dim_shift, axis=0)],\n            \"stds\": [float(x) for x in np.std(per_dim_shift, axis=0)],\n        },\n        \"token_divergence_rate\": float(token_div),\n        \"kl_divergence\": {\n            \"mean\": float(np.mean(task_kls)),\n            \"std\": float(np.std(task_kls)),\n        },\n        \"n_samples\": int(len(task_b)),\n    }\n\n\n# ── Main ────────────────────────────────────────────────────────────────────\ndef main():\n    parser = argparse.ArgumentParser()\n    parser.add_argument(\"--dry-run\", action=\"store_true\")\n    args = parser.parse_args()\n\n    n_tasks = 1 if args.dry_run else 5\n    n_demos = 1 if args.dry_run else 10\n    n_timesteps = 2 if args.dry_run else 50\n\n    os.makedirs(RESULTS_DIR, exist_ok=True)\n\n    print(\"Loading model...\")\n    model, processor = load_model()\n    print(\"Model loaded.\")\n\n    original_eager_fn = install_ablation_hook(model, INSTRUCTION_HEADS_24)\n    layer1_attn = model.language_model.model.layers[1].self_attn\n\n    task_files = get_task_files(n_tasks)\n    print(f\"Tasks ({n_tasks}): {[os.path.basename(f) for f in task_files]}\")\n    print(f\"Config: {n_demos} demos/task, {n_timesteps} timesteps/demo\")\n\n    all_baseline_actions = []\n    all_ablated_actions = []\n    all_gt_actions = []\n    all_baseline_token_ids = []\n    all_ablated_token_ids = []\n    all_kl_divs = []\n    per_task_data = {}\n\n    total_passes = 0\n    t_start = time.time()\n\n    for task_idx, hdf5_path in enumerate(task_files):\n        task_name = os.path.basename(hdf5_path).replace(\"_demo.hdf5\", \"\")\n        instruction = get_language_instruction(hdf5_path)\n        print(f\"\\n{'='*60}\")\n        print(f\"Task {task_idx}: {task_name}\")\n        print(f\"  Instruction: {instruction}\")\n\n        task_baseline_actions = []\n        task_ablated_actions = []\n        task_gt_actions = []\n        task_baseline_token_ids = []\n        task_ablated_token_ids = []\n        task_kl_divs = []\n\n        prompt = f\"In: What action should the robot take to {instruction}?\\nOut:\"\n\n        with h5py.File(hdf5_path, \"r\") as f:\n            for demo_idx in range(n_demos):\n                demo_key = f\"data/demo_{demo_idx}\"\n                actions_data = f[f\"{demo_key}/actions\"][:]\n                images_data = f[f\"{demo_key}/obs/agentview_rgb\"][:]\n                n_steps = min(n_timesteps, len(actions_data))\n\n                for step_idx in range(n_steps):\n                    image_np = images_data[step_idx]\n                    gt_action = actions_data[step_idx]\n\n                    img = Image.fromarray(image_np)\n                    inputs = processor(prompt, img).to(\"cuda:0\", dtype=torch.bfloat16)\n                    input_ids = inputs[\"input_ids\"]\n                    pixel_values = inputs[\"pixel_values\"]\n\n                    # Baseline (ablation disabled)\n                    layer1_attn._ablate_heads = None\n                    b_action, b_ids, b_logits = predict_action_with_logits(\n                        model, input_ids, pixel_values, UNNORM_KEY\n                    )\n\n                    # Ablated\n                    layer1_attn._ablate_heads = INSTRUCTION_HEADS_24\n                    a_action, a_ids, a_logits = predict_action_with_logits(\n                        model, input_ids, pixel_values, UNNORM_KEY\n                    )\n\n                    kl_per_token = compute_kl_divergence(b_logits, a_logits)\n\n                    task_baseline_actions.append(b_action)\n                    task_ablated_actions.append(a_action)\n                    task_gt_actions.append(gt_action)\n                    task_baseline_token_ids.append(b_ids)\n                    task_ablated_token_ids.append(a_ids)\n                    task_kl_divs.append(kl_per_token)\n\n                    total_passes += 2\n                    if total_passes % 100 == 0:\n                        elapsed = time.time() - t_start\n                        rate = total_passes / elapsed\n                        eta = (n_tasks * n_demos * n_timesteps * 2 - total_passes) / rate\n                        print(\n                            f\"  [{total_passes} passes, {elapsed:.0f}s, \"\n                            f\"{rate:.1f} pass/s, ETA {eta:.0f}s]\"\n                        )\n\n                    del b_logits, a_logits\n                    torch.cuda.empty_cache()\n\n        task_b = np.array(task_baseline_actions)\n        task_a = np.array(task_ablated_actions)\n        task_b_ids = np.array(task_baseline_token_ids)\n        task_a_ids = np.array(task_ablated_token_ids)\n        task_kls = np.array(task_kl_divs)\n\n        per_task_data[task_name] = compute_task_metrics(\n            task_b, task_a, task_b_ids, task_a_ids, task_kls\n        )\n        m = per_task_data[task_name]\n        print(\n            f\"  >> paired_mse={m['paired_mse']['mean']:.6f}, \"\n            f\"token_div={m['token_divergence_rate']:.4f}, \"\n            f\"kl={m['kl_divergence']['mean']:.4f}\"\n        )\n\n        all_baseline_actions.extend(task_baseline_actions)\n        all_ablated_actions.extend(task_ablated_actions)\n        all_gt_actions.extend(task_gt_actions)\n        all_baseline_token_ids.extend(task_baseline_token_ids)\n        all_ablated_token_ids.extend(task_ablated_token_ids)\n        all_kl_divs.extend(task_kl_divs)\n\n        gc.collect()\n        torch.cuda.empty_cache()\n\n    # ── Global metrics ──────────────────────────────────────────────────────\n    layer1_attn._ablate_heads = None\n    remove_ablation_hook(model, original_eager_fn)\n\n    all_b = np.array(all_baseline_actions)\n    all_a = np.array(all_ablated_actions)\n    all_gt = np.array(all_gt_actions)\n    all_b_ids = np.array(all_baseline_token_ids)\n    all_a_ids = np.array(all_ablated_token_ids)\n    all_kls = np.array(all_kl_divs)\n\n    paired_mse_all = np.mean((all_b - all_a) ** 2, axis=1)\n    t_res_all = stats.ttest_1samp(paired_mse_all, 0)\n    cohens_d_all = np.mean(paired_mse_all) / (np.std(paired_mse_all, ddof=1) + 1e-12)\n\n    per_dim_shift_all = np.abs(all_b - all_a)\n    token_div_all = np.mean(all_b_ids != all_a_ids)\n\n    kl_per_position = np.mean(all_kls, axis=0)\n\n    mse_gt_baseline = np.mean((all_b - all_gt) ** 2, axis=1)\n    mse_gt_ablated = np.mean((all_a - all_gt) ** 2, axis=1)\n\n    try:\n        wilcoxon_res = stats.wilcoxon(paired_mse_all)\n        wilcoxon_p = float(wilcoxon_res.pvalue)\n    except Exception:\n        wilcoxon_p = None\n\n    output = {\n        \"config\": {\n            \"n_tasks\": n_tasks,\n            \"n_demos_per_task\": n_demos,\n            \"n_timesteps_per_demo\": n_timesteps,\n            \"total_forward_passes\": total_passes,\n            \"model\": \"openvla-7b\",\n            \"ablation\": \"L1_dominant_24_heads_zeroed\",\n            \"ablated_heads\": INSTRUCTION_HEADS_24,\n            \"unnorm_key\": UNNORM_KEY,\n        },\n        \"main_metrics\": {\n            \"paired_action_mse\": {\n                \"mean\": float(np.mean(paired_mse_all)),\n                \"std\": float(np.std(paired_mse_all)),\n                \"t_stat\": float(t_res_all.statistic),\n                \"p_value\": float(t_res_all.pvalue),\n                \"cohens_d\": float(cohens_d_all),\n            },\n            \"per_dim_action_shift\": {\n                \"means\": [float(x) for x in np.mean(per_dim_shift_all, axis=0)],\n                \"stds\": [float(x) for x in np.std(per_dim_shift_all, axis=0)],\n                \"dim_names\": DIM_NAMES,\n            },\n            \"token_divergence_rate\": float(token_div_all),\n        },\n        \"secondary_metrics\": {\n            \"kl_divergence\": {\n                \"mean\": float(np.mean(all_kls)),\n                \"std\": float(np.std(all_kls)),\n                \"per_token_position\": [float(x) for x in kl_per_position],\n            },\n            \"mse_vs_gt_baseline\": {\n                \"mean\": float(np.mean(mse_gt_baseline)),\n                \"std\": float(np.std(mse_gt_baseline)),\n                \"note\": \"OOD, secondary\",\n            },\n            \"mse_vs_gt_ablated\": {\n                \"mean\": float(np.mean(mse_gt_ablated)),\n                \"std\": float(np.std(mse_gt_ablated)),\n                \"note\": \"OOD, secondary\",\n            },\n            \"wilcoxon_p\": wilcoxon_p,\n        },\n        \"per_task\": per_task_data,\n    }\n\n    elapsed_total = time.time() - t_start\n    print(f\"\\n{'='*60}\")\n    print(f\"Done. {total_passes} forward passes in {elapsed_total:.0f}s\")\n    print(\n        f\"Paired MSE: {np.mean(paired_mse_all):.6f} \"\n        f\"(p={t_res_all.pvalue:.2e}, d={cohens_d_all:.3f})\"\n    )\n    print(f\"Token divergence: {token_div_all:.4f}\")\n    print(f\"KL divergence: {np.mean(all_kls):.4f}\")\n    print(f\"MSE vs GT - baseline: {np.mean(mse_gt_baseline):.6f}, ablated: {np.mean(mse_gt_ablated):.6f}\")\n\n    out_path = os.path.join(RESULTS_DIR, \"action_trajectory_analysis.json\")\n    with open(out_path, \"w\") as f:\n        json.dump(output, f, indent=2)\n    print(f\"Results saved to {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-18T10:45:46.182790+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/action_trajectory_analysis.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_action_trajectory_analysis_20260518T103905",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-18T10:45:46.182991+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19183",
  "command": "bash -c \"mkdir -p /root/vla-ssd/scripts\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_action_trajectory_analysis_20260518T103905",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19183",
    "command": "bash -c \"mkdir -p /root/vla-ssd/scripts\""
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-18T10:45:46.183166+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_action_trajectory_analysis_20260518T103905",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-18T10:45:46.183298+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "scp /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/action_trajectory_analysis.py connect.westd.seetacloud.com:/root/vla-ssd/scripts/action_trajectory_analysis.py",
  "description": "Upload script to remote server"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_action_trajectory_analysis_20260518T103905",
  "tool": "Bash",
  "tool_args": {
    "command": "scp /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/action_trajectory_analysis.py connect.westd.seetacloud.com:/root/vla-ssd/scripts/action_trajectory_analysis.py",
    "description": "Upload script to remote server"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-18T10:45:46.183424+00:00_

Exit code 255
ssh_askpass: exec(/usr/bin/ssh-askpass): No such file or directory
Permission denied, please try again.
ssh_askpass: exec(/usr/bin/ssh-askpass): No such file or directory
Permission denied, please try again.
ssh_askpass: exec(/usr/bin/ssh-askpass): No such file or directory
ubuntu@connect.westd.seetacloud.com: Permission denied ().
scp: Connection closed

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_action_trajectory_analysis_20260518T103905",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-18T10:45:46.183570+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/action_trajectory_analysis.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_action_trajectory_analysis_20260518T103905",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/action_trajectory_analysis.py"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-18T10:45:46.183824+00:00_

1	"""Open-loop action trajectory analysis: baseline vs L1-ablated on LIBERO demo observations."""
2	
3	import argparse
4	import gc
5	import glob
6	import json
7	import os
8	import sys
9	import time
10	
11	sys.path.insert(0, "/root/autodl-tmp/LIBERO")
12	
13	os.environ["MUJOCO_GL"] = "egl"
14	os.environ["HDF5_USE_FILE_LOCKING"] = "FALSE"
15	
16	import h5py
17	import numpy as np
18	import torch
19	import torch.nn as nn
20	import torch.nn.functional as F
21	from PIL import Image
22	from scipy import stats
23	
24	np.random.seed(42)
25	torch.manual_seed(42)
26	
27	# ── Config ──────────────────────────────────────────────────────────────────
28	MODEL_PATH = "/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b"
29	UNNORM_KEY = "bridge_orig"
30	DATA_DIR = "/root/autodl-tmp/vla-ssd/data/libero/libero_goal"
31	RESULTS_DIR = "/root/autodl-tmp/vla-ssd/results"
32	
33	NUM_IMAGE_TOKENS = 256
34	INST_START = 1 + NUM_IMAGE_TOKENS
35	
36	INSTRUCTION_HEADS_24 = [
37	    0, 1, 2, 4, 7, 8, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20,
38	    22, 23, 25, 26, 27, 29, 30, 31,
39	]
40	
41	DIM_NAMES = ["dx", "dy", "dz", "rx", "ry", "rz", "gripper"]
42	
43	
44	# ── Model loading ───────────────────────────────────────────────────────────
45	def load_model():
46	    from transformers import AutoModelForVision2Seq, AutoProcessor
47	
48	    processor = AutoProcessor.from_pretrained(MODEL_PATH, trust_remote_code=True)
49	    model = AutoModelForVision2Seq.from_pretrained(
50	        MODEL_PATH,
51	        torch_dtype=torch.bfloat16,
52	        trust_remote_code=True,
53	        low_cpu_mem_usage=True,
54	    ).to("cuda:0").eval()
55	    return model, processor
56	
57	
58	# ── Manual autoregressive generation (bypasses generate() DynamicCache bug) ─
59	def predict_action_with_logits(model, input_ids, pixel_values, unnorm_key):
60	    action_dim = model.get_action_dim(unnorm_key)
61	    if not torch.all(input_ids[:, -1] == 29871):
62	        input_ids = torch.cat(
63	            (input_ids, torch.tensor([[
…[truncated 15822 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_action_trajectory_analysis_20260518T103905",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-18T10:45:46.184116+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19183",
  "command": "bash -c \"cat > /root/vla-ssd/scripts/action_trajectory_analysis.py << 'HEREDOC_EOF'\n\\\"\\\"\\\"Open-loop action trajectory analysis: baseline vs L1-ablated on LIBERO demo observations.\\\"\\\"\\\"\n\nimport argparse\nimport gc\nimport glob\nimport json\nimport os\nimport sys\nimport time\n\nsys.path.insert(0, \\\"/root/autodl-tmp/LIBERO\\\")\n\nos.environ[\\\"MUJOCO_GL\\\"] = \\\"egl\\\"\nos.environ[\\\"HDF5_USE_FILE_LOCKING\\\"] = \\\"FALSE\\\"\n\nimport h5py\nimport numpy as np\nimport torch\nimport torch.nn as nn\nimport torch.nn.functional as F\nfrom PIL import Image\nfrom scipy import stats\n\nnp.random.seed(42)\ntorch.manual_seed(42)\n\n# ── Config ──────────────────────────────────────────────────────────────────\nMODEL_PATH = \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"\nUNNORM_KEY = \\\"bridge_orig\\\"\nDATA_DIR = \\\"/root/autodl-tmp/vla-ssd/data/libero/libero_goal\\\"\nRESULTS_DIR = \\\"/root/autodl-tmp/vla-ssd/results\\\"\n\nNUM_IMAGE_TOKENS = 256\nINST_START = 1 + NUM_IMAGE_TOKENS\n\nINSTRUCTION_HEADS_24 = [\n    0, 1, 2, 4, 7, 8, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20,\n    22, 23, 25, 26, 27, 29, 30, 31,\n]\n\nDIM_NAMES = [\\\"dx\\\", \\\"dy\\\", \\\"dz\\\", \\\"rx\\\", \\\"ry\\\", \\\"rz\\\", \\\"gripper\\\"]\n\n\n# ── Model loading ───────────────────────────────────────────────────────────\ndef load_model():\n    from transformers import AutoModelForVision2Seq, AutoProcessor\n\n    processor = AutoProcessor.from_pretrained(MODEL_PATH, trust_remote_code=True)\n    model = AutoModelForVision2Seq.from_pretrained(\n        MODEL_PATH,\n        torch_dtype=torch.bfloat16,\n        trust_remote_code=True,\n        low_cpu_mem_usage=True,\n    ).to(\\\"cuda:0\\\").eval()\n    return model, processor\n\n\n# ── Manual autoregressive generation (bypasses generate() DynamicCache bug) ─\ndef predict_action_with_logits(model, input_ids, pixel_values, unnorm_key):\n    action_dim = model.get_action_dim(unnorm_key)\n    if not torch.all(input_ids[:, -1] == 29871):\n        input_ids = torch.cat(\n            (input_ids, torch.tensor([[29871]], device=input_ids.device, dtype=input_ids.dtype)),\n            dim=1,\n        )\n    with torch.no_grad():\n        outputs = model(\n            input_ids=input_ids,\n            attention_mask=torch.ones_like(input_ids),\n            pixel_values=pixel_values,\n            past_key_values=None,\n            use_cache=True,\n        )\n    past_key_values = outputs.past_key_values\n    next_token_logits = outputs.logits[:, -1, :]\n\n    generated_ids = []\n    all_logits = []\n\n    for _ in range(action_dim):\n        all_logits.append(next_token_logits.float().cpu())\n        next_token = torch.argmax(next_token_logits, dim=-1, keepdim=True)\n        generated_ids.append(next_token.squeeze().item())\n        attn_mask = torch.ones(\n            (1, past_key_values[0][0].shape[2] + 1),\n            device=input_ids.device,\n            dtype=input_ids.dtype,\n        )\n        with torch.no_grad():\n            outputs = model(\n                input_ids=next_token,\n                attention_mask=attn_mask,\n                pixel_values=None,\n                past_key_values=past_key_values,\n                use_cache=True,\n            )\n        past_key_values = outputs.past_key_values\n        next_token_logits = outputs.logits[:, -1, :]\n\n    predicted_action_token_ids = np.array(generated_ids)\n    discretized_actions = model.vocab_size - predicted_action_token_ids\n    discretized_actions = np.clip(\n        discretized_actions - 1, a_min=0, a_max=model.bin_centers.shape[0] - 1\n    )\n    normalized_actions = model.bin_centers[discretized_actions]\n    action_norm_stats = model.get_action_stats(unnorm_key)\n    mask = action_norm_stats.get(\\\"mask\\\", np.ones_like(action_norm_stats[\\\"q01\\\"], dtype=bool))\n    action_high = np.array(action_norm_stats[\\\"q99\\\"])\n    action_low = np.array(action_norm_stats[\\\"q01\\\"])\n    action = np.where(\n        mask,\n        0.5 * (normalized_actions + 1) * (action_high - action_low) + action_low,\n        normalized_actions,\n    )\n\n    logits_tensor = torch.cat(all_logits, dim=0)\n    return action, predicted_action_token_ids, logits_tensor\n\n\n# ── Ablation hook ───────────────────────────────────────────────────────────\ndef install_ablation_hook(model, heads_to_ablate):\n    import transformers.models.llama.modeling_llama as llama_mod\n    from transformers.models.llama.modeling_llama import repeat_kv\n\n    layer_attn = model.language_model.model.layers[1].self_attn\n    layer_attn._ablate_heads = heads_to_ablate\n\n    original_fn = llama_mod.eager_attention_forward\n\n    def ablated_eager_attention_forward(\n        module, query, key, value, attention_mask, scaling, dropout=0.0, **kwargs\n    ):\n        key_states = repeat_kv(key, module.num_key_value_groups)\n        value_states = repeat_kv(value, module.num_key_value_groups)\n        attn_weights = torch.matmul(query, key_states.transpose(2, 3)) * scaling\n        if attention_mask is not None:\n            causal_mask = attention_mask[:, :, :, : key_states.shape[-2]]\n            attn_weights = attn_weights + causal_mask\n        attn_weights = nn.functional.softmax(attn_weights, dim=-1, dtype=torch.float32).to(\n            query.dtype\n        )\n        attn_weights = nn.functional.dropout(attn_weights, p=dropout, training=module.training)\n        if hasattr(module, \\\"_ablate_heads\\\") and module._ablate_heads is not None:\n            kv_len = attn_weights.shape[-1]\n            if INST_START < kv_len:\n                attn_weights[:, module._ablate_heads, :, INST_START:] = 0.0\n                row_sums = attn_weights.sum(dim=-1, keepdim=True).clamp(min=1e-9)\n                attn_weights = attn_weights / row_sums\n        attn_output = torch.matmul(attn_weights, value_states)\n        attn_output = attn_output.transpose(1, 2).contiguous()\n        return attn_output, attn_weights\n\n    llama_mod.eager_attention_forward = ablated_eager_attention_forward\n    return original_fn\n\n\ndef remove_ablation_hook(model, original_fn):\n    import transformers.models.llama.modeling_llama as llama_mod\n\n    llama_mod.eager_attention_forward = original_fn\n    model.language_model.model.layers[1].self_attn._ablate_heads = None\n\n\n# ── KL divergence ───────────────────────────────────────────────────────────\ndef compute_kl_divergence(logits_p, logits_q):\n    log_p = F.log_softmax(logits_p, dim=-1)\n    log_q = F.log_softmax(logits_q, dim=-1)\n    p = F.softmax(logits_p, dim=-1)\n    kl = (p * (log_p - log_q)).sum(dim=-1)\n    return kl.numpy()\n\n\n# ── Helpers ─────────────────────────────────────────────────────────────────\ndef get_task_files(n_tasks):\n    hdf5_files = sorted(glob.glob(os.path.join(DATA_DIR, \\\"*.hdf5\\\")))\n    return hdf5_files[:n_tasks]\n\n\ndef get_language_instruction(hdf5_path):\n    with h5py.File(hdf5_path, \\\"r\\\") as f:\n        info = json.loads(f[\\\"data\\\"].attrs[\\\"problem_info\\\"])\n    return info[\\\"language_instruction\\\"]\n\n\ndef compute_task_metrics(task_b, task_a, task_b_ids, task_a_ids, task_kls):\n    paired_mse = np.mean((task_b - task_a) ** 2, axis=1)\n    t_res = stats.ttest_1samp(paired_mse, 0)\n    cohens_d = np.mean(paired_mse) / (np.std(paired_mse, ddof=1) + 1e-12)\n\n    per_dim_shift = np.abs(task_b - task_a)\n    token_div = np.mean(task_b_ids != task_a_ids)\n\n    return {\n        \\\"paired_mse\\\": {\n            \\\"mean\\\": float(np.mean(paired_mse)),\n            \\\"std\\\": float(np.std(paired_mse)),\n            \\\"t_stat\\\": float(t_res.statistic),\n            \\\"p_value\\\": float(t_res.pvalue),\n            \\\"cohens_d\\\": float(cohens_d),\n        },\n        \\\"per_dim_shift\\\": {\n            \\\"means\\\": [float(x) for x in np.mean(per_dim_shift, axis=0)],\n            \\\"stds\\\": [float(x) for x in np.std(per_dim_shift, axis=0)],\n        },\n        \\\"token_divergence_rate\\\": float(token_div),\n        \\\"kl_divergence\\\": {\n            \\\"mean\\\": float(np.mean(task_kls)),\n            \\\"std\\\": float(np.std(task_kls)),\n        },\n        \\\"n_samples\\\": int(len(task_b)),\n    }\n\n\n# ── Main ────────────────────────────────────────────────────────────────────\ndef main():\n    parser = argparse.ArgumentParser()\n    parser.add_argument(\\\"--dry-run\\\", action=\\\"store_true\\\")\n    args = parser.parse_args()\n\n    n_tasks = 1 if args.dry_run else 5\n    n_demos = 1 if args.dry_run else 10\n    n_timesteps = 2 if args.dry_run else 50\n\n    os.makedirs(RESULTS_DIR, exist_ok=True)\n\n    print(\\\"Loading model...\\\")\n    model, processor = load_model()\n    print(\\\"Model loaded.\\\")\n\n    original_eager_fn = install_ablation_hook(model, INSTRUCTION_HEADS_24)\n    layer1_attn = model.language_model.model.layers[1].self_attn\n\n    task_files = get_task_files(n_tasks)\n    print(f\\\"Tasks ({n_tasks}): {[os.path.basename(f) for f in task_files]}\\\")\n    print(f\\\"Config: {n_demos} demos/task, {n_timesteps} timesteps/demo\\\")\n\n    all_baseline_actions = []\n    all_ablated_actions = []\n    all_gt_actions = []\n    all_baseline_token_ids = []\n    all_ablated_token_ids = []\n    all_kl_divs = []\n    per_task_data = {}\n\n    total_passes = 0\n    t_start = time.time()\n\n    for task_idx, hdf5_path in enumerate(task_files):\n        task_name = os.path.basename(hdf5_path).replace(\\\"_demo.hdf5\\\", \\\"\\\")\n        instruction = get_language_instruction(hdf5_path)\n        print(f\\\"\\\\n{'='*60}\\\")\n        print(f\\\"Task {task_idx}: {task_name}\\\")\n        print(f\\\"  Instruction: {instruction}\\\")\n\n        task_baseline_actions = []\n        task_ablated_actions = []\n        task_gt_actions = []\n        task_baseline_token_ids = []\n        task_ablated_token_ids = []\n        task_kl_divs = []\n\n        prompt = f\\\"In: What action should the robot take to {instruction}?\\\\nOut:\\\"\n\n        with h5py.File(hdf5_path, \\\"r\\\") as f:\n            for demo_idx in range(n_demos):\n                demo_key = f\\\"data/demo_{demo_idx}\\\"\n                actions_data = f[f\\\"{demo_key}/actions\\\"][:]\n                images_data = f[f\\\"{demo_key}/obs/agentview_rgb\\\"][:]\n                n_steps = min(n_timesteps, len(actions_data))\n\n                for step_idx in range(n_steps):\n                    image_np = images_data[step_idx]\n                    gt_action = actions_data[step_idx]\n\n                    img = Image.fromarray(image_np)\n                    inputs = processor(prompt, img).to(\\\"cuda:0\\\", dtype=torch.bfloat16)\n                    input_ids = inputs[\\\"input_ids\\\"]\n                    pixel_values = inputs[\\\"pixel_values\\\"]\n\n                    # Baseline (ablation disabled)\n                    layer1_attn._ablate_heads = None\n                    b_action, b_ids, b_logits = predict_action_with_logits(\n                        model, input_ids, pixel_values, UNNORM_KEY\n                    )\n\n                    # Ablated\n                    layer1_attn._ablate_heads = INSTRUCTION_HEADS_24\n                    a_action, a_ids, a_logits = predict_action_with_logits(\n                        model, input_ids, pixel_values, UNNORM_KEY\n                    )\n\n                    kl_per_token = compute_kl_divergence(b_logits, a_logits)\n\n                    task_baseline_actions.append(b_action)\n                    task_ablated_actions.append(a_action)\n                    task_gt_actions.append(gt_action)\n                    task_baseline_token_ids.append(b_ids)\n                    task_ablated_token_ids.append(a_ids)\n                    task_kl_divs.append(kl_per_token)\n\n                    total_passes += 2\n                    if total_passes % 100 == 0:\n                        elapsed = time.time() - t_start\n                        rate = total_passes / elapsed\n                        eta = (n_tasks * n_demos * n_timesteps * 2 - total_passes) / rate\n                        print(\n                            f\\\"  [{total_passes} passes, {elapsed:.0f}s, \\\"\n                            f\\\"{rate:.1f} pass/s, ETA {eta:.0f}s]\\\"\n                        )\n\n                    del b_logits, a_logits\n                    torch.cuda.empty_cache()\n\n        task_b = np.array(task_baseline_actions)\n        task_a = np.array(task_ablated_actions)\n        task_b_ids = np.array(task_baseline_token_ids)\n        task_a_ids = np.array(task_ablated_token_ids)\n        task_kls = np.array(task_kl_divs)\n\n        per_task_data[task_name] = compute_task_metrics(\n            task_b, task_a, task_b_ids, task_a_ids, task_kls\n        )\n        m = per_task_data[task_name]\n        print(\n            f\\\"  >> paired_mse={m['paired_mse']['mean']:.6f}, \\\"\n            f\\\"token_div={m['token_divergence_rate']:.4f}, \\\"\n            f\\\"kl={m['kl_divergence']['mean']:.4f}\\\"\n        )\n\n        all_baseline_actions.extend(task_baseline_actions)\n        all_ablated_actions.extend(task_ablated_actions)\n        all_gt_actions.extend(task_gt_actions)\n        all_baseline_token_ids.extend(task_baseline_token_ids)\n        all_ablated_token_ids.extend(task_ablated_token_ids)\n        all_kl_divs.extend(task_kl_divs)\n\n        gc.collect()\n        torch.cuda.empty_cache()\n\n    # ── Global metrics ──────────────────────────────────────────────────────\n    layer1_attn._ablate_heads = None\n    remove_ablation_hook(model, original_eager_fn)\n\n    all_b = np.array(all_baseline_actions)\n    all_a = np.array(all_ablated_actions)\n    all_gt = np.array(all_gt_actions)\n    all_b_ids = np.array(all_baseline_token_ids)\n    all_a_ids = np.array(all_ablated_token_ids)\n    all_kls = np.array(all_kl_divs)\n\n    paired_mse_all = np.mean((all_b - all_a) ** 2, axis=1)\n    t_res_all = stats.ttest_1samp(paired_mse_all, 0)\n    cohens_d_all = np.mean(paired_mse_all) / (np.std(paired_mse_all, ddof=1) + 1e-12)\n\n    per_dim_shift_all = np.abs(all_b - all_a)\n    token_div_all = np.mean(all_b_ids != all_a_ids)\n\n    kl_per_position = np.mean(all_kls, axis=0)\n\n    mse_gt_baseline = np.mean((all_b - all_gt) ** 2, axis=1)\n    mse_gt_ablated = np.mean((all_a - all_gt) ** 2, axis=1)\n\n    try:\n        wilcoxon_res = stats.wilcoxon(paired_mse_all)\n        wilcoxon_p = float(wilcoxon_res.pvalue)\n    except Exception:\n        wilcoxon_p = None\n\n    output = {\n        \\\"config\\\": {\n            \\\"n_tasks\\\": n_tasks,\n            \\\"n_demos_per_task\\\": n_demos,\n            \\\"n_timesteps_per_demo\\\": n_timesteps,\n            \\\"total_forward_passes\\\": total_passes,\n            \\\"model\\\": \\\"openvla-7b\\\",\n            \\\"ablation\\\": \\\"L1_dominant_24_heads_zeroed\\\",\n            \\\"ablated_heads\\\": INSTRUCTION_HEADS_24,\n            \\\"unnorm_key\\\": UNNORM_KEY,\n        },\n        \\\"main_metrics\\\": {\n            \\\"paired_action_mse\\\": {\n                \\\"mean\\\": float(np.mean(paired_mse_all)),\n                \\\"std\\\": float(np.std(paired_mse_all)),\n                \\\"t_stat\\\": float(t_res_all.statistic),\n                \\\"p_value\\\": float(t_res_all.pvalue),\n                \\\"cohens_d\\\": float(cohens_d_all),\n            },\n            \\\"per_dim_action_shift\\\": {\n                \\\"means\\\": [float(x) for x in np.mean(per_dim_shift_all, axis=0)],\n                \\\"stds\\\": [float(x) for x in np.std(per_dim_shift_all, axis=0)],\n                \\\"dim_names\\\": DIM_NAMES,\n            },\n            \\\"token_divergence_rate\\\": float(token_div_all),\n        },\n        \\\"secondary_metrics\\\": {\n            \\\"kl_divergence\\\": {\n                \\\"mean\\\": float(np.mean(all_kls)),\n                \\\"std\\\": float(np.std(all_kls)),\n                \\\"per_token_position\\\": [float(x) for x in kl_per_position],\n            },\n            \\\"mse_vs_gt_baseline\\\": {\n                \\\"mean\\\": float(np.mean(mse_gt_baseline)),\n                \\\"std\\\": float(np.std(mse_gt_baseline)),\n                \\\"note\\\": \\\"OOD, secondary\\\",\n            },\n            \\\"mse_vs_gt_ablated\\\": {\n                \\\"mean\\\": float(np.mean(mse_gt_ablated)),\n                \\\"std\\\": float(np.std(mse_gt_ablated)),\n                \\\"note\\\": \\\"OOD, secondary\\\",\n            },\n            \\\"wilcoxon_p\\\": wilcoxon_p,\n        },\n        \\\"per_task\\\": per_task_data,\n    }\n\n    elapsed_total = time.time() - t_start\n    print(f\\\"\\\\n{'='*60}\\\")\n    print(f\\\"Done. {total_passes} forward passes in {elapsed_total:.0f}s\\\")\n    print(\n        f\\\"Paired MSE: {np.mean(paired_mse_all):.6f} \\\"\n        f\\\"(p={t_res_all.pvalue:.2e}, d={cohens_d_all:.3f})\\\"\n    )\n    print(f\\\"Token divergence: {token_div_all:.4f}\\\")\n    print(f\\\"KL divergence: {np.mean(all_kls):.4f}\\\")\n    print(f\\\"MSE vs GT - baseline: {np.mean(mse_gt_baseline):.6f}, ablated: {np.mean(mse_gt_ablated):.6f}\\\")\n\n    out_path = os.path.join(RESULTS_DIR, \\\"action_trajectory_analysis.json\\\")\n    with open(out_path, \\\"w\\\") as f:\n        json.dump(output, f, indent=2)\n    print(f\\\"Results saved to {out_path}\\\")\n\n\nif __name__ == \\\"__main__\\\":\n    main()\nHEREDOC_EOF\"",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_action_trajectory_analysis_20260518T103905",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19183",
    "command": "bash -c \"cat > /root/vla-ssd/scripts/action_trajectory_analysis.py << 'HEREDOC_EOF'\n\\\"\\\"\\\"Open-loop action trajectory analysis: baseline vs L1-ablated on LIBERO demo observations.\\\"\\\"\\\"\n\nimport argparse\nimport gc\nimport glob\nimport json\nimport os\nimport sys\nimport time\n\nsys.path.insert(0, \\\"/root/autodl-tmp/LIBERO\\\")\n\nos.environ[\\\"MUJOCO_GL\\\"] = \\\"egl\\\"\nos.environ[\\\"HDF5_USE_FILE_LOCKING\\\"] = \\\"FALSE\\\"\n\nimport h5py\nimport numpy as np\nimport torch\nimport torch.nn as nn\nimport torch.nn.functional as F\nfrom PIL import Image\nfrom scipy import stats\n\nnp.random.seed(42)\ntorch.manual_seed(42)\n\n# ── Config ──────────────────────────────────────────────────────────────────\nMODEL_PATH = \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"\nUNNORM_KEY = \\\"bridge_orig\\\"\nDATA_DIR = \\\"/root/autodl-tmp/vla-ssd/data/libero/libero_goal\\\"\nRESULTS_DIR = \\\"/root/autodl-tmp/vla-ssd/results\\\"\n\nNUM_IMAGE_TOKENS = 256\nINST_START = 1 + NUM_IMAGE_TOKENS\n\nINSTRUCTION_HEADS_24 = [\n    0, 1, 2, 4, 7, 8, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20,\n    22, 23, 25, 26, 27, 29, 30, 31,\n]\n\nDIM_NAMES = [\\\"dx\\\", \\\"dy\\\", \\\"dz\\\", \\\"rx\\\", \\\"ry\\\", \\\"rz\\\", \\\"gripper\\\"]\n\n\n# ── Model loading ───────────────────────────────────────────────────────────\ndef load_model():\n    from transformers import AutoModelForVision2Seq, AutoProcessor\n\n    processor = AutoProcessor.from_pretrained(MODEL_PATH, trust_remote_code=True)\n    model = AutoModelForVision2Seq.from_pretrained(\n        MODEL_PATH,\n        torch_dtype=torch.bfloat16,\n        trust_remote_code=True,\n        low_cpu_mem_usage=True,\n    ).to(\\\"cuda:0\\\").eval()\n    return model, processor\n\n\n# ── Manual autoregressive generation (bypasses generate() DynamicCache bug) ─\ndef predict_action_with_logits(model, input_ids, pixel_values, unnorm_key):\n    action_dim = model.get_action_dim(unnorm_key)\n    if not torch.all(input_ids[:, -1] == 29871):\n        input_ids = torch.cat(\n            (input_ids, torch.tensor([[29871]], device=input_ids.device, dtype=input_ids.dtype)),\n            dim=1,\n        )\n    with torch.no_grad():\n        outputs = model(\n            input_ids=input_ids,\n            attention_mask=torch.ones_like(input_ids),\n            pixel_values=pixel_values,\n            past_key_values=None,\n            use_cache=True,\n        )\n    past_key_values = outputs.past_key_values\n    next_token_logits = outputs.logits[:, -1, :]\n\n    generated_ids = []\n    all_logits = []\n\n    for _ in range(action_dim):\n        all_logits.append(next_token_logits.float().cpu())\n        next_token = torch.argmax(next_token_logits, dim=-1, keepdim=True)\n        generated_ids.append(next_token.squeeze().item())\n        attn_mask = torch.ones(\n            (1, past_key_values[0][0].shape[2] + 1),\n            device=input_ids.device,\n            dtype=input_ids.dtype,\n        )\n        with torch.no_grad():\n            outputs = model(\n                input_ids=next_token,\n                attention_mask=attn_mask,\n                pixel_values=None,\n                past_key_values=past_key_values,\n                use_cache=True,\n            )\n        past_key_values = outputs.past_key_values\n        next_token_logits = outputs.logits[:, -1, :]\n\n    predicted_action_token_ids = np.array(generated_ids)\n    discretized_actions = model.vocab_size - predicted_action_token_ids\n    discretized_actions = np.clip(\n        discretized_actions - 1, a_min=0, a_max=model.bin_centers.shape[0] - 1\n    )\n    normalized_actions = model.bin_centers[discretized_actions]\n    action_norm_stats = model.get_action_stats(unnorm_key)\n    mask = action_norm_stats.get(\\\"mask\\\", np.ones_like(action_norm_stats[\\\"q01\\\"], dtype=bool))\n    action_high = np.array(action_norm_stats[\\\"q99\\\"])\n    action_low = np.array(action_norm_stats[\\\"q01\\\"])\n    action = np.where(\n        mask,\n        0.5 * (normalized_actions + 1) * (action_high - action_low) + action_low,\n        normalized_actions,\n    )\n\n    logits_tensor = torch.cat(all_logits, dim=0)\n    return action, predicted_action_token_ids, logits_tensor\n\n\n# ── Ablation hook ───────────────────────────────────────────────────────────\ndef install_ablation_hook(model, heads_to_ablate):\n    import transformers.models.llama.modeling_llama as llama_mod\n    from transformers.models.llama.modeling_llama import repeat_kv\n\n    layer_attn = model.language_model.model.layers[1].self_attn\n    layer_attn._ablate_heads = heads_to_ablate\n\n    original_fn = llama_mod.eager_attention_forward\n\n    def ablated_eager_attention_forward(\n        module, query, key, value, attention_mask, scaling, dropout=0.0, **kwargs\n    ):\n        key_states = repeat_kv(key, module.num_key_value_groups)\n        value_states = repeat_kv(value, module.num_key_value_groups)\n        attn_weights = torch.matmul(query, key_states.transpose(2, 3)) * scaling\n        if attention_mask is not None:\n            causal_mask = attention_mask[:, :, :, : key_states.shape[-2]]\n            attn_weights = attn_weights + causal_mask\n        attn_weights = nn.functional.softmax(attn_weights, dim=-1, dtype=torch.float32).to(\n            query.dtype\n        )\n        attn_weights = nn.functional.dropout(attn_weights, p=dropout, training=module.training)\n        if hasattr(module, \\\"_ablate_heads\\\") and module._ablate_heads is not None:\n            kv_len = attn_weights.shape[-1]\n            if INST_START < kv_len:\n                attn_weights[:, module._ablate_heads, :, INST_START:] = 0.0\n                row_sums = attn_weights.sum(dim=-1, keepdim=True).clamp(min=1e-9)\n                attn_weights = attn_weights / row_sums\n        attn_output = torch.matmul(attn_weights, value_states)\n        attn_output = attn_output.transpose(1, 2).contiguous()\n        return attn_output, attn_weights\n\n    llama_mod.eager_attention_forward = ablated_eager_attention_forward\n    return original_fn\n\n\ndef remove_ablation_hook(model, original_fn):\n    import transformers.models.llama.modeling_llama as llama_mod\n\n    llama_mod.eager_attention_forward = original_fn\n    model.language_model.model.layers[1].self_attn._ablate_heads = None\n\n\n# ── KL divergence ───────────────────────────────────────────────────────────\ndef compute_kl_divergence(logits_p, logits_q):\n    log_p = F.log_softmax(logits_p, dim=-1)\n    log_q = F.log_softmax(logits_q, dim=-1)\n    p = F.softmax(logits_p, dim=-1)\n    kl = (p * (log_p - log_q)).sum(dim=-1)\n    return kl.numpy()\n\n\n# ── Helpers ─────────────────────────────────────────────────────────────────\ndef get_task_files(n_tasks):\n    hdf5_files = sorted(glob.glob(os.path.join(DATA_DIR, \\\"*.hdf5\\\")))\n    return hdf5_files[:n_tasks]\n\n\ndef get_language_instruction(hdf5_path):\n    with h5py.File(hdf5_path, \\\"r\\\") as f:\n        info = json.loads(f[\\\"data\\\"].attrs[\\\"problem_info\\\"])\n    return info[\\\"language_instruction\\\"]\n\n\ndef compute_task_metrics(task_b, task_a, task_b_ids, task_a_ids, task_kls):\n    paired_mse = np.mean((task_b - task_a) ** 2, axis=1)\n    t_res = stats.ttest_1samp(paired_mse, 0)\n    cohens_d = np.mean(paired_mse) / (np.std(paired_mse, ddof=1) + 1e-12)\n\n    per_dim_shift = np.abs(task_b - task_a)\n    token_div = np.mean(task_b_ids != task_a_ids)\n\n    return {\n        \\\"paired_mse\\\": {\n            \\\"mean\\\": float(np.mean(paired_mse)),\n            \\\"std\\\": float(np.std(paired_mse)),\n            \\\"t_stat\\\": float(t_res.statistic),\n            \\\"p_value\\\": float(t_res.pvalue),\n            \\\"cohens_d\\\": float(cohens_d),\n        },\n        \\\"per_dim_shift\\\": {\n            \\\"means\\\": [float(x) for x in np.mean(per_dim_shift, axis=0)],\n            \\\"stds\\\": [float(x) for x in np.std(per_dim_shift, axis=0)],\n        },\n        \\\"token_divergence_rate\\\": float(token_div),\n        \\\"kl_divergence\\\": {\n            \\\"mean\\\": float(np.mean(task_kls)),\n            \\\"std\\\": float(np.std(task_kls)),\n        },\n        \\\"n_samples\\\": int(len(task_b)),\n    }\n\n\n# ── Main ────────────────────────────────────────────────────────────────────\ndef main():\n    parser = argparse.ArgumentParser()\n    parser.add_argument(\\\"--dry-run\\\", action=\\\"store_true\\\")\n    args = parser.parse_args()\n\n    n_tasks = 1 if args.dry_run else 5\n    n_demos = 1 if args.dry_run else 10\n    n_timesteps = 2 if args.dry_run else 50\n\n    os.makedirs(RESULTS_DIR, exist_ok=True)\n\n    print(\\\"Loading model...\\\")\n    model, processor = load_model()\n    print(\\\"Model loaded.\\\")\n\n    original_eager_fn = install_ablation_hook(model, INSTRUCTION_HEADS_24)\n    layer1_attn = model.language_model.model.layers[1].self_attn\n\n    task_files = get_task_files(n_tasks)\n    print(f\\\"Tasks ({n_tasks}): {[os.path.basename(f) for f in task_files]}\\\")\n    print(f\\\"Config: {n_demos} demos/task, {n_timesteps} timesteps/demo\\\")\n\n    all_baseline_actions = []\n    all_ablated_actions = []\n    all_gt_actions = []\n    all_baseline_token_ids = []\n    all_ablated_token_ids = []\n    all_kl_divs = []\n    per_task_data = {}\n\n    total_passes = 0\n    t_start = time.time()\n\n    for task_idx, hdf5_path in enumerate(task_files):\n        task_name = os.path.basename(hdf5_path).replace(\\\"_demo.hdf5\\\", \\\"\\\")\n        instruction = get_language_instruction(hdf5_path)\n        print(f\\\"\\\\n{'='*60}\\\")\n        print(f\\\"Task {task_idx}: {task_name}\\\")\n        print(f\\\"  Instruction: {instruction}\\\")\n\n        task_baseline_actions = []\n        task_ablated_actions = []\n        task_gt_actions = []\n        task_baseline_token_ids = []\n        task_ablated_token_ids = []\n        task_kl_divs = []\n\n        prompt = f\\\"In: What action should the robot take to {instruction}?\\\\nOut:\\\"\n\n        with h5py.File(hdf5_path, \\\"r\\\") as f:\n            for demo_idx in range(n_demos):\n                demo_key = f\\\"data/demo_{demo_idx}\\\"\n                actions_data = f[f\\\"{demo_key}/actions\\\"][:]\n                images_data = f[f\\\"{demo_key}/obs/agentview_rgb\\\"][:]\n                n_steps = min(n_timesteps, len(actions_data))\n\n                for step_idx in range(n_steps):\n                    image_np = images_data[step_idx]\n                    gt_action = actions_data[step_idx]\n\n                    img = Image.fromarray(image_np)\n                    inputs = processor(prompt, img).to(\\\"cuda:0\\\", dtype=torch.bfloat16)\n                    input_ids = inputs[\\\"input_ids\\\"]\n                    pixel_values = inputs[\\\"pixel_values\\\"]\n\n                    # Baseline (ablation disabled)\n                    layer1_attn._ablate_heads = None\n                    b_action, b_ids, b_logits = predict_action_with_logits(\n                        model, input_ids, pixel_values, UNNORM_KEY\n                    )\n\n                    # Ablated\n                    layer1_attn._ablate_heads = INSTRUCTION_HEADS_24\n                    a_action, a_ids, a_logits = predict_action_with_logits(\n                        model, input_ids, pixel_values, UNNORM_KEY\n                    )\n\n                    kl_per_token = compute_kl_divergence(b_logits, a_logits)\n\n                    task_baseline_actions.append(b_action)\n                    task_ablated_actions.append(a_action)\n                    task_gt_actions.append(gt_action)\n                    task_baseline_token_ids.append(b_ids)\n                    task_ablated_token_ids.append(a_ids)\n                    task_kl_divs.append(kl_per_token)\n\n                    total_passes += 2\n                    if total_passes % 100 == 0:\n                        elapsed = time.time() - t_start\n                        rate = total_passes / elapsed\n                        eta = (n_tasks * n_demos * n_timesteps * 2 - total_passes) / rate\n                        print(\n                            f\\\"  [{total_passes} passes, {elapsed:.0f}s, \\\"\n                            f\\\"{rate:.1f} pass/s, ETA {eta:.0f}s]\\\"\n                        )\n\n                    del b_logits, a_logits\n                    torch.cuda.empty_cache()\n\n        task_b = np.array(task_baseline_actions)\n        task_a = np.array(task_ablated_actions)\n        task_b_ids = np.array(task_baseline_token_ids)\n        task_a_ids = np.array(task_ablated_token_ids)\n        task_kls = np.array(task_kl_divs)\n\n        per_task_data[task_name] = compute_task_metrics(\n            task_b, task_a, task_b_ids, task_a_ids, task_kls\n        )\n        m = per_task_data[task_name]\n        print(\n            f\\\"  >> paired_mse={m['paired_mse']['mean']:.6f}, \\\"\n            f\\\"token_div={m['token_divergence_rate']:.4f}, \\\"\n            f\\\"kl={m['kl_divergence']['mean']:.4f}\\\"\n        )\n\n        all_baseline_actions.extend(task_baseline_actions)\n        all_ablated_actions.extend(task_ablated_actions)\n        all_gt_actions.extend(task_gt_actions)\n        all_baseline_token_ids.extend(task_baseline_token_ids)\n        all_ablated_token_ids.extend(task_ablated_token_ids)\n        all_kl_divs.extend(task_kl_divs)\n\n        gc.collect()\n        torch.cuda.empty_cache()\n\n    # ── Global metrics ──────────────────────────────────────────────────────\n    layer1_attn._ablate_heads = None\n    remove_ablation_hook(model, original_eager_fn)\n\n    all_b = np.array(all_baseline_actions)\n    all_a = np.array(all_ablated_actions)\n    all_gt = np.array(all_gt_actions)\n    all_b_ids = np.array(all_baseline_token_ids)\n    all_a_ids = np.array(all_ablated_token_ids)\n    all_kls = np.array(all_kl_divs)\n\n    paired_mse_all = np.mean((all_b - all_a) ** 2, axis=1)\n    t_res_all = stats.ttest_1samp(paired_mse_all, 0)\n    cohens_d_all = np.mean(paired_mse_all) / (np.std(paired_mse_all, ddof=1) + 1e-12)\n\n    per_dim_shift_all = np.abs(all_b - all_a)\n    token_div_all = np.mean(all_b_ids != all_a_ids)\n\n    kl_per_position = np.mean(all_kls, axis=0)\n\n    mse_gt_baseline = np.mean((all_b - all_gt) ** 2, axis=1)\n    mse_gt_ablated = np.mean((all_a - all_gt) ** 2, axis=1)\n\n    try:\n        wilcoxon_res = stats.wilcoxon(paired_mse_all)\n        wilcoxon_p = float(wilcoxon_res.pvalue)\n    except Exception:\n        wilcoxon_p = None\n\n    output = {\n        \\\"config\\\": {\n            \\\"n_tasks\\\": n_tasks,\n            \\\"n_demos_per_task\\\": n_demos,\n            \\\"n_timesteps_per_demo\\\": n_timesteps,\n            \\\"total_forward_passes\\\": total_passes,\n            \\\"model\\\": \\\"openvla-7b\\\",\n            \\\"ablation\\\": \\\"L1_dominant_24_heads_zeroed\\\",\n            \\\"ablated_heads\\\": INSTRUCTION_HEADS_24,\n            \\\"unnorm_key\\\": UNNORM_KEY,\n        },\n        \\\"main_metrics\\\": {\n            \\\"paired_action_mse\\\": {\n                \\\"mean\\\": float(np.mean(paired_mse_all)),\n                \\\"std\\\": float(np.std(paired_mse_all)),\n                \\\"t_stat\\\": float(t_res_all.statistic),\n                \\\"p_value\\\": float(t_res_all.pvalue),\n                \\\"cohens_d\\\": float(cohens_d_all),\n            },\n            \\\"per_dim_action_shift\\\": {\n                \\\"means\\\": [float(x) for x in np.mean(per_dim_shift_all, axis=0)],\n                \\\"stds\\\": [float(x) for x in np.std(per_dim_shift_all, axis=0)],\n                \\\"dim_names\\\": DIM_NAMES,\n            },\n            \\\"token_divergence_rate\\\": float(token_div_all),\n        },\n        \\\"secondary_metrics\\\": {\n            \\\"kl_divergence\\\": {\n                \\\"mean\\\": float(np.mean(all_kls)),\n                \\\"std\\\": float(np.std(all_kls)),\n                \\\"per_token_position\\\": [float(x) for x in kl_per_position],\n            },\n            \\\"mse_vs_gt_baseline\\\": {\n                \\\"mean\\\": float(np.mean(mse_gt_baseline)),\n                \\\"std\\\": float(np.std(mse_gt_baseline)),\n                \\\"note\\\": \\\"OOD, secondary\\\",\n            },\n            \\\"mse_vs_gt_ablated\\\": {\n                \\\"mean\\\": float(np.mean(mse_gt_ablated)),\n                \\\"std\\\": float(np.std(mse_gt_ablated)),\n                \\\"note\\\": \\\"OOD, secondary\\\",\n            },\n            \\\"wilcoxon_p\\\": wilcoxon_p,\n        },\n        \\\"per_task\\\": per_task_data,\n    }\n\n    elapsed_total = time.time() - t_start\n    print(f\\\"\\\\n{'='*60}\\\")\n    print(f\\\"Done. {total_passes} forward passes in {elapsed_total:.0f}s\\\")\n    print(\n        f\\\"Paired MSE: {np.mean(paired_mse_all):.6f} \\\"\n        f\\\"(p={t_res_all.pvalue:.2e}, d={cohens_d_all:.3f})\\\"\n    )\n    print(f\\\"Token divergence: {token_div_all:.4f}\\\")\n    print(f\\\"KL divergence: {np.mean(all_kls):.4f}\\\")\n    print(f\\\"MSE vs GT - baseline: {np.mean(mse_gt_baseline):.6f}, ablated: {np.mean(mse_gt_ablated):.6f}\\\")\n\n    out_path = os.path.join(RESULTS_DIR, \\\"action_trajectory_analysis.json\\\")\n    with open(out_path, \\\"w\\\") as f:\n        json.dump(output, f, indent=2)\n    print(f\\\"Results saved to {out_path}\\\")\n\n\nif __name__ == \\\"__main__\\\":\n    main()\nHEREDOC_EOF\"",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-18T10:45:46.184447+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_action_trajectory_analysis_20260518T103905",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-18T10:45:46.184604+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19183",
  "command": "bash -c \"source /root/miniconda3/bin/activate base && cd /root/vla-ssd && MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=0 python scripts/action_trajectory_analysis.py --dry-run 2>&1\"",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_action_trajectory_analysis_20260518T103905",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19183",
    "command": "bash -c \"source /root/miniconda3/bin/activate base && cd /root/vla-ssd && MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=0 python scripts/action_trajectory_analysis.py --dry-run 2>&1\"",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-18T10:45:46.184767+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Using a slow image processor as `use_fast` is unset and a slow processor was saved with this model. `use_fast=True` will be the default behavior in v4.52, even if the model was saved with a slow processor. This will result in minor differences in outputs. You'll still be able to use a slow processor with `use_fast=False`.\\n/root/miniconda3/lib/python3.12/site-packages/transformers/models/auto/modeling_auto.py:2284: FutureWarning: The class `AutoModelForVision2Seq` is deprecated and will be removed in v5.0. Please use `AutoModelForImageTextToText` instead.\\n  warnings.warn(\\n`torch_dtype` is deprecated! Use `dtype` instead!\\nExpected `transformers==4.40.1` and `tokenizers==0.19.1` but got `transformers==4.57.6` and `tokenizers==0.22.2`; there might be inference-time regressions due to dependency changes. If in doubt, pleaseuse the above versions.\\nLoading model...\\n\\rLoading checkpoint shards:   0%|          | 0/3 [00:00<?, ?it/s]\\rLoading checkpoint shards: 100%|██████████| 3/3 [00:00<00:00, 59.99it/s]\\nModel loaded.\\nTasks (1): ['open_the_middle_drawer_of_the_cabinet_demo.hdf5']\\nConfig: 1 demos/task, 2 timesteps/demo\\n\\n============================================================\\nTask 0: open_the_middle_drawer_of_the_cabinet\\n  Instruction: open the middle drawer of the cabinet\\n  >> paired_mse=0.141834, token_div=0.7857, kl=5.1910\\n\\n============================================================\\nDone. 4 forward passes in 1s\\nPaired MSE: 0.141834 (p=1.77e-04, d=2547.956)\\nToken divergence: 0.7857\\nKL divergence: 5.1910\\nMSE vs GT - baseline: 0.160171, ablated: 0.587655\\nResults saved to /root/autodl-tmp/vla-ssd/results/action_trajectory_analysis.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 11.77}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_action_trajectory_analysis_20260518T103905",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-18T10:45:46.184974+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19183",
  "command": "bash -c \"source /root/miniconda3/bin/activate base && python -c \\\"\nimport json\nwith open('/root/autodl-tmp/vla-ssd/results/action_trajectory_analysis.json') as f:\n    d = json.load(f)\nprint(json.dumps(d, indent=2))\n\\\"\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_action_trajectory_analysis_20260518T103905",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19183",
    "command": "bash -c \"source /root/miniconda3/bin/activate base && python -c \\\"\nimport json\nwith open('/root/autodl-tmp/vla-ssd/results/action_trajectory_analysis.json') as f:\n    d = json.load(f)\nprint(json.dumps(d, indent=2))\n\\\"\""
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-18T10:45:46.185183+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": {\\n    \\\"n_tasks\\\": 1,\\n    \\\"n_demos_per_task\\\": 1,\\n    \\\"n_timesteps_per_demo\\\": 2,\\n    \\\"total_forward_passes\\\": 4,\\n    \\\"model\\\": \\\"openvla-7b\\\",\\n    \\\"ablation\\\": \\\"L1_dominant_24_heads_zeroed\\\",\\n    \\\"ablated_heads\\\": [\\n      0,\\n      1,\\n      2,\\n      4,\\n      7,\\n      8,\\n      10,\\n      11,\\n      12,\\n      14,\\n      15,\\n      16,\\n      17,\\n      18,\\n      19,\\n      20,\\n      22,\\n      23,\\n      25,\\n      26,\\n      27,\\n      29,\\n      30,\\n      31\\n    ],\\n    \\\"unnorm_key\\\": \\\"bridge_orig\\\"\\n  },\\n  \\\"main_metrics\\\": {\\n    \\\"paired_action_mse\\\": {\\n      \\\"mean\\\": 0.1418343763892459,\\n      \\\"std\\\": 3.936176185465046e-05,\\n      \\\"t_stat\\\": 3603.354364903477,\\n      \\\"p_value\\\": 0.00017667420174511224,\\n      \\\"cohens_d\\\": 2547.9562606691247\\n    },\\n    \\\"per_dim_action_shift\\\": {\\n      \\\"means\\\": [\\n        0.0008946969649370959,\\n        0.0,\\n        0.005846068712280075,\\n        0.008621022089439268,\\n        0.019426076506867118,\\n        0.009670788442387293,\\n        0.996078431372549\\n      ],\\n      \\\"stds\\\": [\\n        0.0008946969649370959,\\n        0.0,\\n        0.0006495631902533397,\\n        0.0067052394028972034,\\n        0.000669864707133358,\\n        0.006447192294924867,\\n        0.0\\n      ],\\n      \\\"dim_names\\\": [\\n        \\\"dx\\\",\\n        \\\"dy\\\",\\n        \\\"dz\\\",\\n        \\\"rx\\\",\\n        \\\"ry\\\",\\n        \\\"rz\\\",\\n        \\\"gripper\\\"\\n      ]\\n    },\\n    \\\"token_divergence_rate\\\": 0.7857142857142857\\n  },\\n  \\\"secondary_metrics\\\": {\\n    \\\"kl_divergence\\\": {\\n      \\\"mean\\\": 5.190959930419922,\\n      \\\"std\\\": 5.776741981506348,\\n      \\\"per_token_position\\\": [\\n        0.06576032936573029,\\n        1.8091733455
…[truncated 1795 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_action_trajectory_analysis_20260518T103905",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-18T10:45:46.185363+00:00_

called mcp__agent-ml-research__submit_training_job

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_training_job</summary>

```json
{
  "server": "westd-19183",
  "gpu_ids": "['cuda:0']",
  "exp_id": "action_trajectory_analysis",
  "command": "bash -c \"source /root/miniconda3/bin/activate base && cd /root/vla-ssd && MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=0 python scripts/action_trajectory_analysis.py 2>&1 | tee /root/autodl-tmp/vla-ssd/results/action_trajectory_analysis.log\"",
  "project": "vla-ssd",
  "timeout_hours": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_action_trajectory_analysis_20260518T103905",
  "tool": "mcp__agent-ml-research__submit_training_job",
  "tool_args": {
    "server": "westd-19183",
    "gpu_ids": "['cuda:0']",
    "exp_id": "action_trajectory_analysis",
    "command": "bash -c \"source /root/miniconda3/bin/activate base && cd /root/vla-ssd && MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=0 python scripts/action_trajectory_analysis.py 2>&1 | tee /root/autodl-tmp/vla-ssd/results/action_trajectory_analysis.log\"",
    "project": "vla-ssd",
    "timeout_hours": "2"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-18T10:45:46.185548+00:00_

{"result":"{\"success\": true, \"data\": {\"pid\": \"29086\", \"log_file\": \"~/runs/vla-ssd/action_trajectory_analysis.log\", \"gpu_ids\": [\"cuda:0\"], \"server\": \"westd-19183\", \"account\": \"root\", \"cuda_visible_devices\": \"0\", \"backend\": \"tmux\", \"tmux_session\": \"action_trajectory_analysis\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.34}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_action_trajectory_analysis_20260518T103905",
  "tool": "mcp__agent-ml-research__submit_training_job",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-18T10:45:46.185746+00:00_

已提交。

- **exp_id**: `action_trajectory_analysis`
- **tmux session**: `action_trajectory_analysis`
- **GPU**: cuda:0
- **预计时间**: ~20-40 分钟（5000 forward passes）
- **日志**: `/root/autodl-tmp/vla-ssd/results/action_trajectory_analysis.log`
- **结果**: `/root/autodl-tmp/vla-ssd/results/action_trajectory_analysis.json`

Dry-run 验证通过：ablation 使 78.6% action tokens 发生变化，paired MSE=0.14，KL divergence=5.19。gripper 维度受影响最大。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_action_trajectory_analysis_20260518T103905"
}
```

</details>

---
