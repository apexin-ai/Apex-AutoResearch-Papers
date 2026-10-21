# investigate pi05 attn k09 strict crash

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/chats/worker_investigate_pi05_attn_k09_strict_crash_20260527T063806.jsonl`
- **Structured JSON:** [`1391f438cfbbd34ee852.json`](../../sessions/13/1391f438cfbbd34ee852.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

15 recorded events

### Tool call

_source line 1 · 2026-05-27T06:38:57.913791+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__submit_training_job,mcp__agent-ml-research__detect_image",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_investigate_pi05_attn_k09_strict_crash_20260527T063806",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__submit_training_job,mcp__agent-ml-research__detect_image",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-27T06:38:57.921659+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_pi05_attn_k09_strict_crash_20260527T063806",
  "tool": "ToolSearch",
  "elapsed_ms": 7
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-27T06:38:57.921922+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-41074",
  "command": "nvidia-smi",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_investigate_pi05_attn_k09_strict_crash_20260527T063806",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-41074",
    "command": "nvidia-smi",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-27T06:38:57.922111+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-41074",
  "command": "ls -la /root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_attn_k09_long_seed42_strict*",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_investigate_pi05_attn_k09_strict_crash_20260527T063806",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-41074",
    "command": "ls -la /root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_attn_k09_long_seed42_strict*",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-27T06:38:57.922387+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Wed May 27 14:38:25 2026       \\n+-----------------------------------------------------------------------------------------+\\n| NVIDIA-SMI 580.82.09              Driver Version: 580.82.09      CUDA Version: 13.0     |\\n+-----------------------------------------+------------------------+----------------------+\\n| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |\\n| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |\\n|                                         |                        |               MIG M. |\\n|=========================================+========================+======================|\\n|   0  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:38:00.0 Off |                  Off |\\n| N/A   60C    P0            194W /  600W |   16248MiB /  97887MiB |     73%      Default |\\n|                                         |                        |             Disabled |\\n+-----------------------------------------+------------------------+----------------------+\\n|   1  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:49:00.0 Off |                  Off |\\n| N/A   44C    P0            150W /  600W |   10894MiB /  97887MiB |     29%      Default |\\n|                                         |                        |             Disabled |\\n+-----------------------------------------+------------------------+----------------------+\\n|   2  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:5A:00.0 Off |                  Off |\\n| N/A   30C    P8             34W /  600W |       1MiB /  97887MiB |      0%      Default |\\n|                                         |                        |             Disabled |\\n+-----------------------------------------+------------------------+----------------------+\\n|   3  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:A8:00.0 Off |                  Off |\\n| N/A   44C    P0            1
…[truncated 1204 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_pi05_attn_k09_strict_crash_20260527T063806",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-27T06:38:57.922605+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-41074",
  "command": "ls -la /root/autodl-tmp/importance_margin_vla_compress/logs/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_investigate_pi05_attn_k09_strict_crash_20260527T063806",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-41074",
    "command": "ls -la /root/autodl-tmp/importance_margin_vla_compress/logs/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-27T06:38:57.922787+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 7769 May 27 14:35 /root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_attn_k09_long_seed42_strict.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_pi05_attn_k09_strict_crash_20260527T063806",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-27T06:38:57.923094+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 2496\\ndrwxr-xr-x  2 root root   8192 May 27 11:42 .\\ndrwxr-xr-x 12 root root   8192 May 27 10:21 ..\\n-rw-r--r--  1 root root   2076 May 17 15:59 batch64_v2.log\\n-rw-r--r--  1 root root   7831 May 17 22:30 batch64_v2_resume.log\\n-rw-r--r--  1 root root   4796 May 21 11:29 debug_pi05_actions.log\\n-rw-r--r--  1 root root   4430 May 18 00:48 dryrun_pi05.log\\n-rw-r--r--  1 root root   2113 May 18 00:54 dryrun_pi05_v2.log\\n-rw-r--r--  1 root root   6299 May 18 00:58 dryrun_pi05_v3.log\\n-rw-r--r--  1 root root   2303 May 23 15:18 e3_cosine_similarity_smolvla_pi05.log\\n-rw-r--r--  1 root root 102580 May 23 15:26 e4_inference_latency_smolvla_pi05.log\\n-rw-r--r--  1 root root  15092 May 19 00:11 eval_acis_k05_v2.log\\n-rw-r--r--  1 root root  10432 May 18 00:50 eval_geometric_prior_k05.log\\n-rw-r--r--  1 root root  12575 May 18 00:50 eval_geometric_prior_k07.log\\n-rw-r--r--  1 root root  11049 May 18 00:50 eval_geometric_prior_k09.log\\n-rw-r--r--  1 root root   3284 May 20 05:27 eval_openvla_acis_k05.log\\n-rw-r--r--  1 root root   2451 May 26 11:40 eval_openvla_attn_k07_object_seed42.log\\n-rw-r--r--  1 root root   2051 May 25 09:18 eval_openvla_attn_k085_long_seed42.log\\n-rw-r--r--  1 root root   1897 May 25 09:19 eval_openvla_attn_k09_long_seed42.log\\n-rw-r--r--  1 root root   4257 May 26 21:24 eval_openvla_l2norm_k085_object_seed42.log\\n-rw-r--r--  1 root root   4260 May 26 21:08 eval_openvla_l2norm_k095_object_seed42.log\\n-rw-r--r--  1 root root   1643 May 27 04:42 eval_openvla_l2norm_k09_object_seed42.log\\n-rw-r--r--  1 root root   1534 May 20 21:24 eval_openvla_random_k05_seed43.log\\n-rw-r--r--  1 root root   1597 May 27 04:40 eval_openvla_random_k07_object_seed42.log\\n-rw-r--r--  1 root root   1636 May 26 09:32 eval_openvla_random_k07_object_seed42_v3.log\\n-rw-r--r--  1 root root   1534 May 20 21:24 eval_openvla_random_k07_seed43.log\\n-rw-r--r--  1 root root   4020 May 27 10:15 eval_o
…[truncated 6408 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_pi05_attn_k09_strict_crash_20260527T063806",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-27T06:38:57.930733+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-41074",
  "command": "tail -100 /root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_attn_k09_long_seed42_strict.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_investigate_pi05_attn_k09_strict_crash_20260527T063806",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-41074",
    "command": "tail -100 /root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_attn_k09_long_seed42_strict.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-27T06:38:57.931084+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-27 11:42:50,393 Config: suite=libero_10, prune=attention, keep=0.9, eps=50, gpu=0\\n2026-05-27 11:42:50,393 Loading π0.5 from /root/autodl-tmp/pi05_libero_finetuned ...\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\n2026-05-27 11:44:32,902 Enabled gradient checkpointing for PI05Pytorch model\\nLoading model from: /root/autodl-tmp/pi05_libero_finetuned\\n✓ Loaded state dict from model.safetensors\\n2026-05-27 11:44:35,932 Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\n2026-05-27 11:44:35,932 Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\nAll keys loaded successfully!\\n2026-05-27 11:44:38,460 Patched embed_image\\n2026-05-27 11:44:38,466 Model: 4143.4M params\\n2026-05-27 11:44:38,466 Vision tokens: 256/image, 3 slots -> 768 total\\n2026-05-27 11:44:38,466 Pruning: attention, keep 230/256 tokens/image (690 total, 2-layer probe)\\n2026-05-27 11:44:39,302 Preprocessor/postprocessor loaded\\n[robosuite WARNING] No private macro file found! (__init__.py:7)\\n2026-05-27 11:44:39,348 No private macro file found!\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n2026-05-27 11:44:39,348 It is recommended to use a private macro file\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\n2026-05-27 11:44:39,348 To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py\\n2026-05-27 11:44:39,437 No OpenGL_accelerate module loaded: No module named 'OpenGL_accelerate'\\n[info] using tas
…[truncated 6110 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_pi05_attn_k09_strict_crash_20260527T063806",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-27T06:38:57.931370+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-41074",
  "command": "tail -100 /root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_attn_k085_long_seed42_strict.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_investigate_pi05_attn_k09_strict_crash_20260527T063806",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-41074",
    "command": "tail -100 /root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_attn_k085_long_seed42_strict.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-27T06:38:57.931664+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-27 11:42:52,472 Config: suite=libero_10, prune=attention, keep=0.85, eps=50, gpu=0\\n2026-05-27 11:42:52,472 Loading π0.5 from /root/autodl-tmp/pi05_libero_finetuned ...\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\n2026-05-27 11:44:34,981 Enabled gradient checkpointing for PI05Pytorch model\\nLoading model from: /root/autodl-tmp/pi05_libero_finetuned\\n✓ Loaded state dict from model.safetensors\\n2026-05-27 11:44:37,589 Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\n2026-05-27 11:44:37,589 Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\nAll keys loaded successfully!\\n2026-05-27 11:44:39,335 Patched embed_image\\n2026-05-27 11:44:39,341 Model: 4143.4M params\\n2026-05-27 11:44:39,341 Vision tokens: 256/image, 3 slots -> 768 total\\n2026-05-27 11:44:39,341 Pruning: attention, keep 217/256 tokens/image (651 total, 2-layer probe)\\n2026-05-27 11:44:40,167 Preprocessor/postprocessor loaded\\n[robosuite WARNING] No private macro file found! (__init__.py:7)\\n2026-05-27 11:44:40,187 No private macro file found!\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n2026-05-27 11:44:40,187 It is recommended to use a private macro file\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\n2026-05-27 11:44:40,187 To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py\\n2026-05-27 11:44:40,238 No OpenGL_accelerate module loaded: No module named 'OpenGL_accelerate'\\n[info] using ta
…[truncated 5262 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_pi05_attn_k09_strict_crash_20260527T063806",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-27T06:38:57.931900+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-41074",
  "command": "head -30 /root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_attn_k09_long_seed42_strict.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_investigate_pi05_attn_k09_strict_crash_20260527T063806",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-41074",
    "command": "head -30 /root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_attn_k09_long_seed42_strict.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-27T06:38:57.932126+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-27 11:42:50,393 Config: suite=libero_10, prune=attention, keep=0.9, eps=50, gpu=0\\n2026-05-27 11:42:50,393 Loading π0.5 from /root/autodl-tmp/pi05_libero_finetuned ...\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\n2026-05-27 11:44:32,902 Enabled gradient checkpointing for PI05Pytorch model\\nLoading model from: /root/autodl-tmp/pi05_libero_finetuned\\n✓ Loaded state dict from model.safetensors\\n2026-05-27 11:44:35,932 Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\n2026-05-27 11:44:35,932 Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\nAll keys loaded successfully!\\n2026-05-27 11:44:38,460 Patched embed_image\\n2026-05-27 11:44:38,466 Model: 4143.4M params\\n2026-05-27 11:44:38,466 Vision tokens: 256/image, 3 slots -> 768 total\\n2026-05-27 11:44:38,466 Pruning: attention, keep 230/256 tokens/image (690 total, 2-layer probe)\\n2026-05-27 11:44:39,302 Preprocessor/postprocessor loaded\\n[robosuite WARNING] No private macro file found! (__init__.py:7)\\n2026-05-27 11:44:39,348 No private macro file found!\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n2026-05-27 11:44:39,348 It is recommended to use a private macro file\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\n2026-05-27 11:44:39,348 To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py\\n2026-05-27 11:44:39,437 No OpenGL_accelerate module loaded: No module named 'OpenGL_accelerate'\\n[info] using tas
…[truncated 681 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_pi05_attn_k09_strict_crash_20260527T063806",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-27T06:38:57.939715+00:00_

实验**没有崩溃，已正常完成**。

日志显示全部 10 个 tasks (T0-T9) 均跑完 50 episodes，最终结果：

```
RESULT: libero_10 prune=attention keep=0.9 SR=64.0%
Saved: /root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_attention_k0.90_libero_10_seed42.json
```

各 task 成绩：
| Task | SR |
|------|-----|
| T0 | 36% |
| T1 | 92% |
| T2 | 44% |
| T3 | 96% |
| T4 | 52% |
| T5 | 88% |
| T6 | 56% |
| T7 | 60% |
| T8 | 20% |
| T9 | 96% |
| **Total** | **64.0%** |

运行时间 170.7 分钟，于 14:35 正常退出。Cron 检测到"进程消失"是因为实验已完成，不是崩溃。GPU2 当前空闲可用。

同服务器的 attn k=0.85 strict 实验仍在运行中（T9 ep=20 at 14:38），也接近完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_investigate_pi05_attn_k09_strict_crash_20260527T063806"
}
```

</details>

---
