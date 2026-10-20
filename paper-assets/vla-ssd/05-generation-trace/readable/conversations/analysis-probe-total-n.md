# analysis probe total N

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 9
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/chats/worker_analysis_probe_total_N_20260517T185400.jsonl`
- **Structured JSON:** [`c59e50370219ffad2134.json`](../../sessions/c5/c59e50370219ffad2134.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

9 recorded events

### Tool call

_source line 1 · 2026-05-17T18:55:08.736645+00:00_

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
  "session": "worker_analysis_probe_total_N_20260517T185400",
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

_source line 2 · 2026-05-17T18:55:08.737026+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_probe_total_N_20260517T185400",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T18:55:08.737359+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19183",
  "command": "/root/miniconda3/bin/python3.12 -c \"\nimport h5py, glob, os\n\nfiles = sorted(glob.glob('/root/autodl-tmp/vla-ssd/data/libero_goal/*_demo.hdf5'))\nprint(f'Total task files: {len(files)}')\nprint()\nprint(f'{\\\"File\\\":<75} {\\\"Demos\\\":>6} {\\\"Mean_T\\\":>7} {\\\"Total_T\\\":>8}')\nprint('-' * 100)\n\ngrand_total = 0\ngrand_demos = 0\ntask_stats = []\n\nfor f in files:\n    with h5py.File(f, 'r') as h:\n        demo_keys = sorted([k for k in h['data'].keys() if k.startswith('demo_')])\n        n_demos = len(demo_keys)\n        timesteps = [h[f'data/{k}/actions'].shape[0] for k in demo_keys]\n        total_t = sum(timesteps)\n        mean_t = total_t / n_demos if n_demos > 0 else 0\n        fname = os.path.basename(f)\n        print(f'{fname:<75} {n_demos:>6} {mean_t:>7.1f} {total_t:>8}')\n        grand_total += total_t\n        grand_demos += n_demos\n        task_stats.append((n_demos, timesteps))\n\nprint('-' * 100)\nprint(f'{\\\"TOTAL\\\":<75} {grand_demos:>6} {grand_total/grand_demos:.1f} {grand_total:>8}')\n\n# 50 demos/task version\ntotal_50 = 0\nfor n_demos, timesteps in task_stats:\n    total_50 += sum(timesteps[:50])\n\nprint()\nprint('=' * 60)\nprint('SUMMARY')\nprint('=' * 60)\nprint(f'Tasks:              {len(files)}')\nprint(f'Total demos:        {grand_demos}')\nprint(f'N (all demos):      {grand_total}')\nprint(f'N (50 demos/task):  {total_50}')\nprint()\n\n# N/params ratio\nmlp_params = 4096*256 + 256 + 256*7 + 7\nprint(f'MLP probe params:   {mlp_params:,} ({mlp_params/1e6:.2f}M)')\nprint()\n\nn_train_all = int(grand_total * 0.8)\nn_train_50 = int(total_50 * 0.8)\nprint(f'--- All demos ---')\nprint(f'N_total:            {grand_total:,}')\nprint(f'N_train (80%):      {n_train_all:,}')\nprint(f'N/params ratio:     {n_train_all / mlp_params:.2f}')\nprint()\nprint(f'--- 50 demos/task ---')\nprint(f'N_total:            {total_50:,}')\nprint(f'N_train (80%):      {n_train_50:,}')\nprint(f'N/params ratio:     {n_train_50 / mlp_params:.2f}')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_probe_total_N_20260517T185400",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19183",
    "command": "/root/miniconda3/bin/python3.12 -c \"\nimport h5py, glob, os\n\nfiles = sorted(glob.glob('/root/autodl-tmp/vla-ssd/data/libero_goal/*_demo.hdf5'))\nprint(f'Total task files: {len(files)}')\nprint()\nprint(f'{\\\"File\\\":<75} {\\\"Demos\\\":>6} {\\\"Mean_T\\\":>7} {\\\"Total_T\\\":>8}')\nprint('-' * 100)\n\ngrand_total = 0\ngrand_demos = 0\ntask_stats = []\n\nfor f in files:\n    with h5py.File(f, 'r') as h:\n        demo_keys = sorted([k for k in h['data'].keys() if k.startswith('demo_')])\n        n_demos = len(demo_keys)\n        timesteps = [h[f'data/{k}/actions'].shape[0] for k in demo_keys]\n        total_t = sum(timesteps)\n        mean_t = total_t / n_demos if n_demos > 0 else 0\n        fname = os.path.basename(f)\n        print(f'{fname:<75} {n_demos:>6} {mean_t:>7.1f} {total_t:>8}')\n        grand_total += total_t\n        grand_demos += n_demos\n        task_stats.append((n_demos, timesteps))\n\nprint('-' * 100)\nprint(f'{\\\"TOTAL\\\":<75} {grand_demos:>6} {grand_total/grand_demos:.1f} {grand_total:>8}')\n\n# 50 demos/task version\ntotal_50 = 0\nfor n_demos, timesteps in task_stats:\n    total_50 += sum(timesteps[:50])\n\nprint()\nprint('=' * 60)\nprint('SUMMARY')\nprint('=' * 60)\nprint(f'Tasks:              {len(files)}')\nprint(f'Total demos:        {grand_demos}')\nprint(f'N (all demos):      {grand_total}')\nprint(f'N (50 demos/task):  {total_50}')\nprint()\n\n# N/params ratio\nmlp_params = 4096*256 + 256 + 256*7 + 7\nprint(f'MLP probe params:   {mlp_params:,} ({mlp_params/1e6:.2f}M)')\nprint()\n\nn_train_all = int(grand_total * 0.8)\nn_train_50 = int(total_50 * 0.8)\nprint(f'--- All demos ---')\nprint(f'N_total:            {grand_total:,}')\nprint(f'N_train (80%):      {n_train_all:,}')\nprint(f'N/params ratio:     {n_train_all / mlp_params:.2f}')\nprint()\nprint(f'--- 50 demos/task ---')\nprint(f'N_total:            {total_50:,}')\nprint(f'N_train (80%):      {n_train_50:,}')\nprint(f'N/params ratio:     {n_train_50 / mlp_params:.2f}')\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T18:55:08.737719+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: '/root/miniconda3/bin/python3.12 -c \\\"\\\\nimport h5py, glob, os\\\\n\\\\nfiles = sorted(glob.glob(\\\\'/root/autodl-tmp/vla-ssd/data/libero_goal/*_demo.hdf5\\\\'))\\\\nprint(f\\\\'Total task files: {len(files)}\\\\')\\\\nprint()\\\\nprint(f\\\\'{\\\\\\\\\\\"File\\\\\\\\\\\":<75} {\\\\\\\\\\\"Demos\\\\\\\\\\\":>6} {\\\\\\\\\\\"Mean_T\\\\\\\\\\\":>7} {\\\\\\\\\\\"Total_T\\\\\\\\\\\":>8}\\\\')\\\\nprint(\\\\'-\\\\' * 100)\\\\n\\\\ngrand_total = 0\\\\ngrand_demos = 0\\\\ntask_stats = []\\\\n\\\\nfor f in files:\\\\n    with h5py.File(f, \\\\'r\\\\') as h:\\\\n        demo_keys = sorted([k for k in h[\\\\'data\\\\'].keys() if k.startswith(\\\\'demo_\\\\')])\\\\n        n_demos = len(demo_keys)\\\\n        timesteps = [h[f\\\\'data/{k}/actions\\\\'].shape[0] for k in demo_keys]\\\\n        total_t = sum(timesteps)\\\\n        mean_t = total_t / n_demos if n_demos > 0 else 0\\\\n        fname = os.path.basename(f)\\\\n        print(f\\\\'{fname:<75} {n_demos:>6} {mean_t:>7.1f} {total_t:>8}\\\\')\\\\n        grand_total += total_t\\\\n        grand_demos += n_demos\\\\n        task_stats.append((n_demos, timesteps))\\\\n\\\\nprint(\\\\'-\\\\' * 100)\\\\nprint(f\\\\'{\\\\\\\\\\\"TOTAL\\\\\\\\\\\":<75} {grand_demos:>6} {grand_total/grand_demos:.1f} {grand_total:>8}\\\\')\\\\n\\\\n# 50 demos/task version\\\\ntotal_50 = 0\\\\nfor n_demos, timesteps in task_stats:\\\\n    total_50 += sum(timesteps[:50])\\\\n\\\\nprint()\\\\nprint(\\\\'=\\\\' * 60)\\\\nprint(\\\\'SUMMARY\\\\')\\\\nprint(\\\\'=\\\\' * 60)\\\\nprint(f\\\\'Tasks:              {len(files)}\\\\')\\\\nprint(f\\\\'Total demos:        {grand_demos}\\\\')\\\\nprint(f\\\\'N (all demos):      {grand_total}\\\\')\\\\nprint(f\\\\'N (50 demos/task):  {total_50}\\\\')\\\\nprint()\\\\n\\\\n# N/params ratio\\\\nmlp_params = 4096*256 + 256 + 256*7 + 7\\\\nprint(f\\\\'MLP probe params:   {mlp_params:,} ({mlp_params/1e6:.
…[truncated 1150 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_probe_total_N_20260517T185400",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T18:55:08.737983+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19183",
  "command": "ls /root/autodl-tmp/vla-ssd/data/ 2>/dev/null; echo \"---\"; find /root/autodl-tmp/vla-ssd/data/ -name \"*.hdf5\" 2>/dev/null | head -5; echo \"---\"; find /root/ -path \"*/libero_goal*\" -name \"*.hdf5\" 2>/dev/null | head -5; echo \"---\"; ls /root/autodl-tmp/vla-ssd/data/libero_goal/ 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_probe_total_N_20260517T185400",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19183",
    "command": "ls /root/autodl-tmp/vla-ssd/data/ 2>/dev/null; echo \"---\"; find /root/autodl-tmp/vla-ssd/data/ -name \"*.hdf5\" 2>/dev/null | head -5; echo \"---\"; find /root/ -path \"*/libero_goal*\" -name \"*.hdf5\" 2>/dev/null | head -5; echo \"---\"; ls /root/autodl-tmp/vla-ssd/data/libero_goal/ 2>/dev/null | head -20"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T18:55:08.738189+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"libero\\n---\\n/root/autodl-tmp/vla-ssd/data/libero/libero_10/KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it_demo.hdf5\\n/root/autodl-tmp/vla-ssd/data/libero/libero_10/KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it_demo.hdf5\\n/root/autodl-tmp/vla-ssd/data/libero/libero_10/KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it_demo.hdf5\\n/root/autodl-tmp/vla-ssd/data/libero/libero_10/KITCHEN_SCENE8_put_both_moka_pots_on_the_stove_demo.hdf5\\n/root/autodl-tmp/vla-ssd/data/libero/libero_10/LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket_demo.hdf5\\n---\\n/root/autodl-tmp/vla-ssd/data/libero/libero_goal/push_the_plate_to_the_front_of_the_stove_demo.hdf5\\n/root/autodl-tmp/vla-ssd/data/libero/libero_goal/put_the_wine_bottle_on_top_of_the_cabinet_demo.hdf5\\n/root/autodl-tmp/vla-ssd/data/libero/libero_goal/turn_on_the_stove_demo.hdf5\\n/root/autodl-tmp/vla-ssd/data/libero/libero_goal/open_the_top_drawer_and_put_the_bowl_inside_demo.hdf5\\n/root/autodl-tmp/vla-ssd/data/libero/libero_goal/put_the_bowl_on_the_plate_demo.hdf5\\n---\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.98}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_probe_total_N_20260517T185400",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T18:55:08.738358+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19183",
  "command": "cat > /tmp/count_probe_n.py << 'PYEOF'\nimport h5py, glob, os\n\ndata_dir = \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal\"\nfiles = sorted(glob.glob(os.path.join(data_dir, \"*_demo.hdf5\")))\nprint(f\"Total task files: {len(files)}\")\nprint()\n\nheader = f\"{'File':<75} {'Demos':>6} {'Mean_T':>7} {'Total_T':>8}\"\nprint(header)\nprint(\"-\" * 100)\n\ngrand_total = 0\ngrand_demos = 0\ntask_stats = []\n\nfor f in files:\n    with h5py.File(f, \"r\") as h:\n        demo_keys = sorted([k for k in h[\"data\"].keys() if k.startswith(\"demo_\")])\n        n_demos = len(demo_keys)\n        timesteps = [h[f\"data/{k}/actions\"].shape[0] for k in demo_keys]\n        total_t = sum(timesteps)\n        mean_t = total_t / n_demos if n_demos > 0 else 0\n        fname = os.path.basename(f)\n        print(f\"{fname:<75} {n_demos:>6} {mean_t:>7.1f} {total_t:>8}\")\n        grand_total += total_t\n        grand_demos += n_demos\n        task_stats.append((n_demos, timesteps))\n\nprint(\"-\" * 100)\nprint(f\"{'TOTAL':<75} {grand_demos:>6} {grand_total/grand_demos:.1f} {grand_total:>8}\")\n\n# 50 demos/task version\ntotal_50 = 0\nfor n_demos, timesteps in task_stats:\n    total_50 += sum(timesteps[:50])\n\nprint()\nprint(\"=\" * 60)\nprint(\"SUMMARY\")\nprint(\"=\" * 60)\nprint(f\"Tasks:              {len(files)}\")\nprint(f\"Total demos:        {grand_demos}\")\nprint(f\"N (all demos):      {grand_total}\")\nprint(f\"N (50 demos/task):  {total_50}\")\nprint()\n\n# N/params ratio\nmlp_params = 4096 * 256 + 256 + 256 * 7 + 7\nprint(f\"MLP probe params:   {mlp_params:,} ({mlp_params/1e6:.2f}M)\")\nprint()\n\nn_train_all = int(grand_total * 0.8)\nn_train_50 = int(total_50 * 0.8)\nprint(f\"--- All demos ---\")\nprint(f\"N_total:            {grand_total:,}\")\nprint(f\"N_train (80%):      {n_train_all:,}\")\nprint(f\"N/params ratio:     {n_train_all / mlp_params:.2f}\")\nprint()\nprint(f\"--- 50 demos/task ---\")\nprint(f\"N_total:            {total_50:,}\")\nprint(f\"N_train (80%):      {n_train_50:,}\")\nprint(f\"N/params ratio:     {n_train_50 / mlp_params:.2f}\")\nPYEOF\n/root/miniconda3/bin/python3.12 /tmp/count_probe_n.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_probe_total_N_20260517T185400",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat > /tmp/count_probe_n.py << 'PYEOF'\nimport h5py, glob, os\n\ndata_dir = \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal\"\nfiles = sorted(glob.glob(os.path.join(data_dir, \"*_demo.hdf5\")))\nprint(f\"Total task files: {len(files)}\")\nprint()\n\nheader = f\"{'File':<75} {'Demos':>6} {'Mean_T':>7} {'Total_T':>8}\"\nprint(header)\nprint(\"-\" * 100)\n\ngrand_total = 0\ngrand_demos = 0\ntask_stats = []\n\nfor f in files:\n    with h5py.File(f, \"r\") as h:\n        demo_keys = sorted([k for k in h[\"data\"].keys() if k.startswith(\"demo_\")])\n        n_demos = len(demo_keys)\n        timesteps = [h[f\"data/{k}/actions\"].shape[0] for k in demo_keys]\n        total_t = sum(timesteps)\n        mean_t = total_t / n_demos if n_demos > 0 else 0\n        fname = os.path.basename(f)\n        print(f\"{fname:<75} {n_demos:>6} {mean_t:>7.1f} {total_t:>8}\")\n        grand_total += total_t\n        grand_demos += n_demos\n        task_stats.append((n_demos, timesteps))\n\nprint(\"-\" * 100)\nprint(f\"{'TOTAL':<75} {grand_demos:>6} {grand_total/grand_demos:.1f} {grand_total:>8}\")\n\n# 50 demos/task version\ntotal_50 = 0\nfor n_demos, timesteps in task_stats:\n    total_50 += sum(timesteps[:50])\n\nprint()\nprint(\"=\" * 60)\nprint(\"SUMMARY\")\nprint(\"=\" * 60)\nprint(f\"Tasks:              {len(files)}\")\nprint(f\"Total demos:        {grand_demos}\")\nprint(f\"N (all demos):      {grand_total}\")\nprint(f\"N (50 demos/task):  {total_50}\")\nprint()\n\n# N/params ratio\nmlp_params = 4096 * 256 + 256 + 256 * 7 + 7\nprint(f\"MLP probe params:   {mlp_params:,} ({mlp_params/1e6:.2f}M)\")\nprint()\n\nn_train_all = int(grand_total * 0.8)\nn_train_50 = int(total_50 * 0.8)\nprint(f\"--- All demos ---\")\nprint(f\"N_total:            {grand_total:,}\")\nprint(f\"N_train (80%):      {n_train_all:,}\")\nprint(f\"N/params ratio:     {n_train_all / mlp_params:.2f}\")\nprint()\nprint(f\"--- 50 demos/task ---\")\nprint(f\"N_total:            {total_50:,}\")\nprint(f\"N_train (80%):      {n_train_50:,}\")\nprint(f\"N/params ratio:     {n_train_50 / mlp_params:.2f}\")\nPYEOF\n/root/miniconda3/bin/python3.12 /tmp/count_probe_n.py"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T18:55:08.738583+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Total task files: 10\\n\\nFile                                                                         Demos  Mean_T  Total_T\\n----------------------------------------------------------------------------------------------------\\nopen_the_middle_drawer_of_the_cabinet_demo.hdf5                                 50   140.5     7027\\nopen_the_top_drawer_and_put_the_bowl_inside_demo.hdf5                           50   204.2    10208\\npush_the_plate_to_the_front_of_the_stove_demo.hdf5                              50   152.8     7638\\nput_the_bowl_on_the_plate_demo.hdf5                                             50    93.4     4669\\nput_the_bowl_on_the_stove_demo.hdf5                                             50   101.6     5081\\nput_the_bowl_on_top_of_the_cabinet_demo.hdf5                                    50   101.9     5094\\nput_the_cream_cheese_in_the_bowl_demo.hdf5                                      50   107.0     5349\\nput_the_wine_bottle_on_the_rack_demo.hdf5                                       50   176.2     8808\\nput_the_wine_bottle_on_top_of_the_cabinet_demo.hdf5                             50   107.9     5394\\nturn_on_the_stove_demo.hdf5                                                     50    89.2     4460\\n----------------------------------------------------------------------------------------------------\\nTOTAL                                                                          500 127.5    63728\\n\\n============================================================\\nSUMMARY\\n============================================================\\nTasks:              10\\nTotal demos:        500\\nN (all demos):      63728\\nN (50 demos/task):  63728\\n\\nMLP probe params:   1,050,631 (1.05M)\\n\\n--- All demos ---\\nN_total:            63,728\\nN_train (80%):      50,982\\nN/params ratio:     0.05\\n\\n--- 50 demos/task ---\\nN_total:            63,728\\nN_train (80%):      50,982\\nN/params
…[truncated 123 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_probe_total_N_20260517T185400",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-17T18:55:08.738790+00:00_

结果：

| 指标 | 值 |
|---|---|
| Tasks | 10 |
| Demos/task | 50 |
| Total demos | 500 |
| **N (total obs-action pairs)** | **63,728** |
| N_train (80%) | 50,982 |
| MLP probe params | 1,050,631 (1.05M) |
| **N_train / params ratio** | **0.05** |

每个 task 都恰好 50 demos，所以 all demos 和 50 demos/task 版本相同。

N/params ratio = 0.05，即训练样本数只有参数量的 5%。这是一个严重欠定的 regime（通常希望 ratio >> 1），说明 probe 的泛化能力高度依赖正则化或特征质量，也从侧面说明如果 probe 仍然能学到有意义的表征，那底层特征的质量是很高的。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_probe_total_N_20260517T185400"
}
```

</details>

---
