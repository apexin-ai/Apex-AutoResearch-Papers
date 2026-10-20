# code check spatial cross inst progress

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/chats/worker_code_check_spatial_cross_inst_progress_20260517T091650.jsonl`
- **Structured JSON:** [`6a385f9553e1d9237fb2.json`](../../sessions/6a/6a385f9553e1d9237fb2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

19 recorded events

### Tool call

_source line 1 · 2026-05-17T09:17:52.953346+00:00_

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
  "session": "worker_code_check_spatial_cross_inst_progress_20260517T091650",
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

_source line 2 · 2026-05-17T09:17:52.953686+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_check_spatial_cross_inst_progress_20260517T091650",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T09:17:52.953867+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "nvidia-smi"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_check_spatial_cross_inst_progress_20260517T091650",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "nvidia-smi"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-17T09:17:52.954026+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "tmux ls"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_check_spatial_cross_inst_progress_20260517T091650",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "tmux ls"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T09:17:52.954153+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ps aux --no-headers -o pid,user,%cpu,%mem,etime,command --sort=-%cpu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_check_spatial_cross_inst_progress_20260517T091650",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ps aux --no-headers -o pid,user,%cpu,%mem,etime,command --sort=-%cpu"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T09:17:52.954312+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Sun May 17 17:17:13 2026       \\n+-----------------------------------------------------------------------------------------+\\n| NVIDIA-SMI 580.82.09              Driver Version: 580.82.09      CUDA Version: 13.0     |\\n+-----------------------------------------+------------------------+----------------------+\\n| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |\\n| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |\\n|                                         |                        |               MIG M. |\\n|=========================================+========================+======================|\\n|   0  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:98:00.0 Off |                  Off |\\n| N/A   29C    P8             34W /  600W |       0MiB /  97887MiB |      0%      Default |\\n|                                         |                        |             Disabled |\\n+-----------------------------------------+------------------------+----------------------+\\n|   1  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:D8:00.0 Off |                  Off |\\n| N/A   30C    P8             35W /  600W |       0MiB /  97887MiB |      0%      Default |\\n|                                         |                        |             Disabled |\\n+-----------------------------------------+------------------------+----------------------+\\n\\n+-----------------------------------------------------------------------------------------+\\n| Processes:                                                                              |\\n|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |\\n|        ID   ID                                                               Usage      |\\n|=========================================================================================|\\n|  No running processes fou
…[truncated 264 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_check_spatial_cross_inst_progress_20260517T091650",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-17T09:17:52.954462+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'tmux' is not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_check_spatial_cross_inst_progress_20260517T091650",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T09:17:52.954602+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"error: conflicting format options\\n\\nUsage:\\n ps [options]\\n\\n Try 'ps --help &lt;simple|list|output|threads|misc|all>'\\n  or 'ps --help &lt;s|l|o|t|m|a>'\\n for additional help text.\\n\\nFor more details see ps(1).\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 2.02}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_check_spatial_cross_inst_progress_20260517T091650",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T09:17:52.954759+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ls -la /root/autodl-tmp/vla-ssd/results/cross_instruction_spatial/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_check_spatial_cross_inst_progress_20260517T091650",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ls -la /root/autodl-tmp/vla-ssd/results/cross_instruction_spatial/"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-17T09:17:52.954882+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "find /root/autodl-tmp/vla-ssd/results/ -name \"*cross*\" -o -name \"*spatial*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_check_spatial_cross_inst_progress_20260517T091650",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "find /root/autodl-tmp/vla-ssd/results/ -name \"*cross*\" -o -name \"*spatial*\""
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T09:17:52.955026+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ls -la /root/runs/vla-ssd/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_check_spatial_cross_inst_progress_20260517T091650",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ls -la /root/runs/vla-ssd/"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T09:17:52.955155+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 5137624\\ndrwxr-xr-x  2 root root       4096 May 17 17:08 .\\ndrwxr-xr-x 34 root root       4096 May 17 16:58 ..\\n-rw-r--r--  1 root root       1305 May 17 17:08 classification_results.json\\n-rw-r--r--  1 root root      38860 May 17 17:04 extract_trained.log\\n-rw-r--r--  1 root root      39013 May 17 17:06 extract_untrained.log\\n-rw-r--r--  1 root root      17877 May 17 17:08 run.log\\n-rw-r--r--  1 root root 2630402616 May 17 17:04 trained_cross_inst_L0-L31.h5\\n-rw-r--r--  1 root root 2630402616 May 17 17:06 untrained_cross_inst_L0-L31.h5\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_check_spatial_cross_inst_progress_20260517T091650",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-17T09:17:52.955296+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/vla-ssd/results/figures/libero_spatial_rsa_perlayer.pdf\\n/root/autodl-tmp/vla-ssd/results/figures/libero_spatial_rsa_perlayer.png\\n/root/autodl-tmp/vla-ssd/results/figures/libero_spatial_r2_perlayer.pdf\\n/root/autodl-tmp/vla-ssd/results/figures/libero_spatial_r2_perlayer.png\\n/root/autodl-tmp/vla-ssd/results/figures/cross_benchmark_comparison.pdf\\n/root/autodl-tmp/vla-ssd/results/figures/cross_benchmark_comparison.png\\n/root/autodl-tmp/vla-ssd/results/rsa/rsa_libero_spatial.json\\n/root/autodl-tmp/vla-ssd/results/functional_validation/action_probe_libero_spatial.json\\n/root/autodl-tmp/vla-ssd/results/cross_instruction\\n/root/autodl-tmp/vla-ssd/results/cross_instruction/trained_cross_inst.h5\\n/root/autodl-tmp/vla-ssd/results/cross_instruction/untrained_cross_inst.h5\\n/root/autodl-tmp/vla-ssd/results/cross_instruction/fig2_cross_instruction_heatmap.pdf\\n/root/autodl-tmp/vla-ssd/results/cross_instruction/fig2_cross_instruction_heatmap.png\\n/root/autodl-tmp/vla-ssd/results/cross_instruction_dense\\n/root/autodl-tmp/vla-ssd/results/cross_instruction_dense/trained_cross_inst_dense.h5\\n/root/autodl-tmp/vla-ssd/results/cross_instruction_dense/untrained_cross_inst_dense.h5\\n/root/autodl-tmp/vla-ssd/results/cross_instruction_dense/llama2base_cross_inst_dense.h5\\n/root/autodl-tmp/vla-ssd/results/cross_instruction_dense/llama2base_cross_inst_L9-L31.h5\\n/root/autodl-tmp/vla-ssd/results/cross_instruction_spatial\\n/root/autodl-tmp/vla-ssd/results/cross_instruction_spatial/trained_cross_inst_L0-L31.h5\\n/root/autodl-tmp/vla-ssd/results/cross_instruction_spatial/untrained_cross_inst_L0-L31.h5\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_check_spatial_cross_inst_progress_20260517T091650",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T09:17:52.955450+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 11696\\ndrwxr-xr-x 2 root root    4096 May 17 06:02 .\\ndrwxr-xr-x 3 root root      29 May 15 15:14 ..\\n-rw-r--r-- 1 root root    3516 May 16 17:33 ablation_p1_seed_robustness.log\\n-rw-r--r-- 1 root root      25 May 16 18:33 ablation_p2_demo_sensitivity.log\\n-rw-r--r-- 1 root root    3005 May 16 19:00 ablation_p2_demo_sensitivity_v2.log\\n-rw-r--r-- 1 root root    8905 May 16 12:10 fulllayer_action_probe.log\\n-rw-r--r-- 1 root root    3413 May 16 01:49 lg_dino_extract.log\\n-rw-r--r-- 1 root root  972412 May 16 01:38 lg_extract_trained.log\\n-rw-r--r-- 1 root root  955828 May 16 01:41 lg_extract_untrained.log\\n-rw-r--r-- 1 root root     718 May 16 01:54 lg_gc_dino.log\\n-rw-r--r-- 1 root root    4193 May 16 01:51 lg_gc_trained.log\\n-rw-r--r-- 1 root root    4217 May 16 02:00 lg_gc_untrained.log\\n-rw-r--r-- 1 root root    4136 May 15 22:34 mvp2_action_trained.log\\n-rw-r--r-- 1 root root    4149 May 15 22:35 mvp2_action_untrained.log\\n-rw-r--r-- 1 root root    4126 May 15 23:11 mvp2_delta_trained.log\\n-rw-r--r-- 1 root root    4139 May 15 23:11 mvp2_delta_untrained.log\\n-rw-r--r-- 1 root root    3687 May 15 22:08 mvp_controlb_trained.log\\n-rw-r--r-- 1 root root   10714 May 15 22:09 mvp_controlb_untrained.log\\n-rw-r--r-- 1 root root    6453 May 15 21:45 mvp_probe_trained.log\\n-rw-r--r-- 1 root root    6097 May 15 21:44 mvp_probe_untrained.log\\n-rw-r--r-- 1 root root 4055009 May 15 21:06 openvla-trained-extract.log\\n-rw-r--r-- 1 root root 3638216 May 15 20:53 openvla-untrained-extract.log\\n-rw-r--r-- 1 root root      12 May 16 14:44 plan010_action_probe_spatial.log\\n-rw-r--r-- 1 root root      12 May 16 14:33 plan010_rsa_spatial.log\\n-rw-r--r-- 1 root root 1098095 May 16 14:10 plan_010_extract_trained.log\\n-rw-r--r-- 1 root root 1082737 May 16 14:09 plan_010_extract_untrained.log\\n-rw-r--r-- 1 root root   18121 May 17 07:04 qa_probe_classification.log\\n\", \"stderr\": \"\", \"return_code
…[truncated 68 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_check_spatial_cross_inst_progress_20260517T091650",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T09:17:52.955627+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/cross_instruction_spatial/classification_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_check_spatial_cross_inst_progress_20260517T091650",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/results/cross_instruction_spatial/classification_results.json"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-17T09:17:52.955750+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/cross_instruction_spatial/run.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_check_spatial_cross_inst_progress_20260517T091650",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/results/cross_instruction_spatial/run.log"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-17T09:17:52.955916+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"trained_image_mean\\\": {\\n    \\\"L0\\\": 0.1,\\n    \\\"L1\\\": 0.1,\\n    \\\"L4\\\": 0.1,\\n    \\\"L8\\\": 0.1,\\n    \\\"L12\\\": 0.1,\\n    \\\"L16\\\": 0.1,\\n    \\\"L20\\\": 0.1,\\n    \\\"L24\\\": 0.1,\\n    \\\"L28\\\": 0.102,\\n    \\\"L31\\\": 0.101\\n  },\\n  \\\"trained_last_preaction\\\": {\\n    \\\"L0\\\": 0.1,\\n    \\\"L1\\\": 0.989,\\n    \\\"L4\\\": 1.0,\\n    \\\"L8\\\": 1.0,\\n    \\\"L12\\\": 1.0,\\n    \\\"L16\\\": 1.0,\\n    \\\"L20\\\": 1.0,\\n    \\\"L24\\\": 1.0,\\n    \\\"L28\\\": 1.0,\\n    \\\"L31\\\": 1.0\\n  },\\n  \\\"untrained_image_mean\\\": {\\n    \\\"L0\\\": 0.1,\\n    \\\"L1\\\": 0.1,\\n    \\\"L4\\\": 0.1,\\n    \\\"L8\\\": 0.101,\\n    \\\"L12\\\": 0.099,\\n    \\\"L16\\\": 0.1,\\n    \\\"L20\\\": 0.099,\\n    \\\"L24\\\": 0.1,\\n    \\\"L28\\\": 0.1,\\n    \\\"L31\\\": 0.1\\n  },\\n  \\\"untrained_last_preaction\\\": {\\n    \\\"L0\\\": 0.1,\\n    \\\"L1\\\": 0.995,\\n    \\\"L4\\\": 0.862,\\n    \\\"L8\\\": 0.683,\\n    \\\"L12\\\": 0.795,\\n    \\\"L16\\\": 0.765,\\n    \\\"L20\\\": 0.689,\\n    \\\"L24\\\": 0.777,\\n    \\\"L28\\\": 0.76,\\n    \\\"L31\\\": 0.754\\n  },\\n  \\\"chance\\\": 0.1,\\n  \\\"metadata\\\": {\\n    \\\"n_train_samples\\\": 4000,\\n    \\\"n_test_samples\\\": 1000,\\n    \\\"n_classes\\\": 10,\\n    \\\"report_layers\\\": [\\n      \\\"L0\\\",\\n      \\\"L1\\\",\\n      \\\"L4\\\",\\n      \\\"L8\\\",\\n      \\\"L12\\\",\\n      \\\"L16\\\",\\n      \\\"L20\\\",\\n      \\\"L24\\\",\\n      \\\"L28\\\",\\n      \\\"L31\\\"\\n    ],\\n    \\\"train_tasks\\\": [\\n      0,\\n      1,\\n      2,\\n      3,\\n      4,\\n      5,\\n      6,\\n      7\\n    ],\\n    \\\"test_tasks\\\": [\\n      8,\\n      9\\n    ],\\n    \\\"pca_components\\\": 256,\\n    \\\"classifier\\\": \\\"LogisticRegression(C=1.0, max_iter=2000)\\\",\\n    \\\"seed\\\": 42\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {
…[truncated 29 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_check_spatial_cross_inst_progress_20260517T091650",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-17T09:17:52.956189+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== Starting LIBERO-Spatial cross-instruction extraction ===\\nTrained on cuda:0, Untrained on cuda:1\\nTrained PID: 880449, Untrained PID: 880450\\nWaiting for both to finish...\\nTrained finished with exit code 0\\nUntrained finished with exit code 0\\n=== Both extractions completed successfully ===\\nRunning classification...\\n\\n=== TRAINED_IMAGE_MEAN ===\\nLoading /root/autodl-tmp/vla-ssd/results/cross_instruction_spatial/trained_cross_inst_L0-L31.h5 [image_mean]...\\n  Loaded. Train: 4000, Test: 1000\\n/root/miniconda3/lib/python3.12/site-packages/sklearn/linear_model/_logistic.py:1184: FutureWarning: 'n_jobs' has no effect since 1.8 and will be removed in 1.10. You provided 'n_jobs=-1', please leave it unspecified.\\n  warnings.warn(msg, category=FutureWarning)\\n  L0: 0.1000\\n/root/miniconda3/lib/python3.12/site-packages/sklearn/linear_model/_logistic.py:1184: FutureWarning: 'n_jobs' has no effect since 1.8 and will be removed in 1.10. You provided 'n_jobs=-1', please leave it unspecified.\\n  warnings.warn(msg, category=FutureWarning)\\n  L1: 0.1000\\n/root/miniconda3/lib/python3.12/site-packages/sklearn/linear_model/_logistic.py:1184: FutureWarning: 'n_jobs' has no effect since 1.8 and will be removed in 1.10. You provided 'n_jobs=-1', please leave it unspecified.\\n  warnings.warn(msg, category=FutureWarning)\\n  L4: 0.1000\\n/root/miniconda3/lib/python3.12/site-packages/sklearn/linear_model/_logistic.py:1184: FutureWarning: 'n_jobs' has no effect since 1.8 and will be removed in 1.10. You provided 'n_jobs=-1', please leave it unspecified.\\n  warnings.warn(msg, category=FutureWarning)\\n  L8: 0.1000\\n/root/miniconda3/lib/python3.12/site-packages/sklearn/linear_model/_logistic.py:1184: FutureWarning: 'n_jobs' has no effect since 1.8 and will be removed in 1.10. You provided 'n_jobs=-1', please leave it unspecified.\\n  warnings.warn(msg, category=FutureWarning)\\n  L12: 0.1000\\n/root/miniconda3/l
…[truncated 6416 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_check_spatial_cross_inst_progress_20260517T091650",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-17T09:17:52.956394+00:00_

提取和分类全部完成。完整结果表格：

### LIBERO-Spatial Cross-Instruction 10-way Classification (10 classes, chance=0.1)

| Layer | trained_image_mean | trained_last_preaction | untrained_image_mean | untrained_last_preaction |
|-------|-------------------|----------------------|---------------------|------------------------|
| L0    | 0.100             | 0.100                | 0.100               | 0.100                  |
| L1    | 0.100             | **0.989**            | 0.100               | **0.995**              |
| L4    | 0.100             | **1.000**            | 0.100               | 0.862                  |
| L8    | 0.100             | **1.000**            | 0.101               | 0.683                  |
| L12   | 0.100             | **1.000**            | 0.099               | 0.795                  |
| L16   | 0.100             | **1.000**            | 0.100               | 0.765                  |
| L20   | 0.100             | **1.000**            | 0.099               | 0.689                  |
| L24   | 0.100             | **1.000**            | 0.100               | 0.777                  |
| L28   | 0.100             | **1.000**            | 0.100               | 0.760                  |
| L31   | 0.101             | **1.000**            | 0.100               | 0.754                  |

关键发现（数据呈现，遵守 C001 约束，trained + untrained 对照齐全）：

1. **image_mean token**: trained 和 untrained 都在 chance level (~0.1)，所有层均无 goal 信息。这与 LIBERO-Object 结果一致。

2. **last_preaction token**:
   - **Trained**: L1 即达 0.989，L4 起完美 1.000 并保持到 L31
   - **Untrained**: L1 高达 0.995（与 trained 相当），但 L4 开始显著下降至 0.862，L8 降至 0.683，中高层波动在 0.68-0.80 之间
   - **Trained vs Untrained gap**: L4 起 gap 显著（1.000 vs 0.862），L8 gap 最大（1.000 vs 0.683）

3. 模式与 LIBERO-Object 类似：训练使 last_preaction 位置的 goal classification 从不完美提升到完美，但 image_mean 始终不编码 goal 信息。

注意：untrained 中高层有 ConvergenceWarning（lbfgs 2000 iter 未收敛），实际 accuracy 可能略被低估。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_check_spatial_cross_inst_progress_20260517T091650"
}
```

</details>

---
