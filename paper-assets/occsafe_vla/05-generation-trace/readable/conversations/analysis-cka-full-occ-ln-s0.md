# analysis cka full occ ln s0

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 55
- **Recorded user turns:** 0
- **Tool calls:** 27
- **Original source:** `logs/chats/worker_analysis_cka_full_occ_ln_s0_20260525T014618.jsonl`
- **Structured JSON:** [`a79a59565604cce4f884.json`](../../sessions/a7/a79a59565604cce4f884.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

55 recorded events

### Tool call

_source line 1 · 2026-05-25T01:49:04.990155+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__update_registry,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__register_artifact",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__update_registry,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__register_artifact",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-25T01:49:04.990499+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-25T01:49:04.990732+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "cka_full_occ_ln_s0",
  "field": "status",
  "value": "PREPARING",
  "project": "occsafe_vla"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "cka_full_occ_ln_s0",
    "field": "status",
    "value": "PREPARING",
    "project": "occsafe_vla"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-25T01:49:04.990880+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "cka_full_occ_ln_s0",
  "field": "hypothesis",
  "value": "CKA analysis of Full OCC+LN (seed 42) vs pretrained. Tests whether gradient flow + LayerNorm combination preserves encoder representations similarly to gradient flow + BN (Full OCC BN CKA ~0.96). Completes the 2×2 factorial representation dimension.",
  "project": "occsafe_vla"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "cka_full_occ_ln_s0",
    "field": "hypothesis",
    "value": "CKA analysis of Full OCC+LN (seed 42) vs pretrained. Tests whether gradient flow + LayerNorm combination preserves encoder representations similarly to gradient flow + BN (Full OCC BN CKA ~0.96). Completes the 2×2 factorial representation dimension.",
    "project": "occsafe_vla"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-25T01:49:04.991029+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"cka_full_occ_ln_s0\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T01:46:40.104Z\", \"updated_at\": \"2026-05-25T01:46:40.104Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.5457}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-25T01:49:04.991170+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"cka_full_occ_ln_s0\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T01:46:40.104Z\", \"updated_at\": \"2026-05-25T01:46:41.389Z\", \"hypothesis\": \"CKA analysis of Full OCC+LN (seed 42) vs pretrained. Tests whether gradient flow + LayerNorm combination preserves encoder representations similarly to gradient flow + BN (Full OCC BN CKA ~0.96). Completes the 2×2 factorial representation dimension.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5084}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-25T01:49:04.991300+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-10894",
  "command": "ls /root/autodl-tmp/models/openvla-7b/ 2>/dev/null && echo \"PRETRAINED_OK\" || echo \"PRETRAINED_MISSING\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-10894",
    "command": "ls /root/autodl-tmp/models/openvla-7b/ 2>/dev/null && echo \"PRETRAINED_OK\" || echo \"PRETRAINED_MISSING\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-25T01:49:04.991427+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '&&' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-25T01:49:04.991546+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-10894",
  "command": "ls /root/autodl-tmp/checkpoints/full_occ_ln_s0/ 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-10894",
    "command": "ls /root/autodl-tmp/checkpoints/full_occ_ln_s0/ 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-25T01:49:04.991694+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-25T01:49:04.991827+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-10894",
  "command": "find /root/autodl-tmp/ -name \"libero_spatial\" -type d 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-10894",
    "command": "find /root/autodl-tmp/ -name \"libero_spatial\" -type d 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-25T01:49:04.991949+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-25T01:49:04.992070+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-10894",
  "command": "find /root/occsafe_vla/ -name \"cka_analysis.py\" 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-10894",
    "command": "find /root/occsafe_vla/ -name \"cka_analysis.py\" 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-25T01:49:04.992189+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-25T01:49:04.992334+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-10894",
  "command": "ls /root/autodl-tmp/models/openvla-7b/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-10894",
    "command": "ls /root/autodl-tmp/models/openvla-7b/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-25T01:49:04.992454+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-10894",
  "command": "ls /root/autodl-tmp/checkpoints/full_occ_ln_s0/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-10894",
    "command": "ls /root/autodl-tmp/checkpoints/full_occ_ln_s0/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-25T01:49:04.992604+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"README.md\\nadded_tokens.json\\nconfig.json\\nconfig.json.back.20260520_150144\\nconfig.json.back.20260520_154539\\nconfig.json.back.20260520_154609\\nconfig.json.back.20260520_154614\\nconfig.json.back.20260520_164752\\nconfig.json.back.20260520_165710\\nconfig.json.back.20260520_171716\\nconfig.json.back.20260520_171723\\nconfig.json.back.20260520_171725\\nconfig.json.back.20260520_172038\\nconfig.json.back.20260520_172043\\nconfig.json.back.20260520_172229\\nconfig.json.back.20260520_181903\\nconfig.json.back.20260520_182218\\nconfig.json.back.20260520_194407\\nconfig.json.back.20260520_203559\\nconfig.json.back.20260520_203637\\nconfig.json.back.20260520_203843\\nconfig.json.back.20260520_215004\\nconfig.json.back.20260520_215044\\nconfig.json.back.20260520_215354\\nconfig.json.back.20260521_100159\\nconfig.json.back.20260521_100239\\nconfig.json.back.20260521_100428\\nconfig.json.back.20260521_114422\\nconfig.json.back.20260521_114424\\nconfig.json.back.20260521_122249\\nconfig.json.back.20260521_122252\\nconfig.json.back.20260521_142517\\nconfig.json.back.20260521_142521\\nconfig.json.back.20260521_182240\\nconfig.json.back.20260521_182321\\nconfig.json.back.20260521_185613\\nconfig.json.back.20260521_190252\\nconfig.json.back.20260521_190256\\nconfig.json.back.20260521_190300\\nconfig.json.back.20260522_141210\\nconfig.json.back.20260522_141214\\nconfig.json.back.20260522_150136\\nconfig.json.back.20260522_150139\\nconfig.json.back.20260523_083407\\nconfig.json.back.20260523_083705\\nconfig.json.back.20260523_083828\\nconfig.json.back.20260523_132736\\nconfig.json.back.20260523_132739\\nconfig.json.back.20260523_132743\\nconfig.json.back.20260523_173952\\nconfig.json.back.20260523_221210\\nconfig.json.back.20260523_221213\\nconfig.json.back.20260523_221217\\nconfig.json.back.20260523_221221\\nconfig.json.back.20260524_011110\\nconfig.json.back.20260524_011114\\nconfig.json.back.20260524_011120\\nconfig.j
…[truncated 772 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-25T01:49:04.992780+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug\\nopenvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-25T01:49:04.992908+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-10894",
  "command": "find /root/autodl-tmp/ -name \"libero_spatial\" -type d",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-10894",
    "command": "find /root/autodl-tmp/ -name \"libero_spatial\" -type d",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-25T01:49:04.993028+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-10894",
  "command": "find /root/occsafe_vla/ -name \"cka_analysis.py\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-10894",
    "command": "find /root/occsafe_vla/ -name \"cka_analysis.py\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-25T01:49:04.993146+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/libero_datasets/.cache/huggingface/download/libero_spatial\\n/root/autodl-tmp/libero_datasets/libero_spatial\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-25T01:49:04.993267+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/occsafe_vla/analysis/cka_analysis.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-25T01:49:04.993424+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-10894",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla && nohup bash -c 'CUDA_VISIBLE_DEVICES=1 python analysis/cka_analysis.py --pretrained_path /root/autodl-tmp/models/openvla-7b --checkpoint_paths /root/autodl-tmp/checkpoints/full_occ_ln_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt --condition_names \"Full OCC+LN\" --libero_data_dir /root/autodl-tmp/libero_datasets/libero_spatial --output_dir /root/autodl-tmp/analysis/cka_full_occ_ln --gpu 0 --num_samples 200' > /root/autodl-tmp/analysis/cka_full_occ_ln/cka_run.log 2>&1 & echo \"PID=$!\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-10894",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla && nohup bash -c 'CUDA_VISIBLE_DEVICES=1 python analysis/cka_analysis.py --pretrained_path /root/autodl-tmp/models/openvla-7b --checkpoint_paths /root/autodl-tmp/checkpoints/full_occ_ln_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt --condition_names \"Full OCC+LN\" --libero_data_dir /root/autodl-tmp/libero_datasets/libero_spatial --output_dir /root/autodl-tmp/analysis/cka_full_occ_ln --gpu 0 --num_samples 200' > /root/autodl-tmp/analysis/cka_full_occ_ln/cka_run.log 2>&1 & echo \"PID=$!\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-25T01:49:04.993561+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"PID=853920\\n\", \"stderr\": \"bash: line 1: /root/autodl-tmp/analysis/cka_full_occ_ln/cka_run.log: No such file or directory\\n\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-25T01:49:04.993731+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-10894",
  "command": "mkdir -p /root/autodl-tmp/analysis/cka_full_occ_ln && source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla && nohup bash -c 'CUDA_VISIBLE_DEVICES=1 python analysis/cka_analysis.py --pretrained_path /root/autodl-tmp/models/openvla-7b --checkpoint_paths /root/autodl-tmp/checkpoints/full_occ_ln_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt --condition_names \"Full OCC+LN\" --libero_data_dir /root/autodl-tmp/libero_datasets/libero_spatial --output_dir /root/autodl-tmp/analysis/cka_full_occ_ln --gpu 0 --num_samples 200' > /root/autodl-tmp/analysis/cka_full_occ_ln/cka_run.log 2>&1 & echo \"PID=$!\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-10894",
    "command": "mkdir -p /root/autodl-tmp/analysis/cka_full_occ_ln && source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla && nohup bash -c 'CUDA_VISIBLE_DEVICES=1 python analysis/cka_analysis.py --pretrained_path /root/autodl-tmp/models/openvla-7b --checkpoint_paths /root/autodl-tmp/checkpoints/full_occ_ln_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt --condition_names \"Full OCC+LN\" --libero_data_dir /root/autodl-tmp/libero_datasets/libero_spatial --output_dir /root/autodl-tmp/analysis/cka_full_occ_ln --gpu 0 --num_samples 200' > /root/autodl-tmp/analysis/cka_full_occ_ln/cka_run.log 2>&1 & echo \"PID=$!\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-25T01:49:04.993876+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'mkdir -p /root/autodl-tmp/analysis/cka_full_occ_ln && source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla && nohup bash -c \\\\'CUDA_VISIBLE_DEVICES=1 python analysis/cka_analysis.py --pretrained_path /root/autodl-tmp/models/openvla-7b --checkpoint_paths /root/autodl-tmp/checkpoints/full_occ_ln_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt --condition_names \\\"Full OCC+LN\\\" --libero_data_dir /root/autodl-tmp/libero_datasets/libero_spatial --output_dir /root/autodl-tmp/analysis/cka_full_occ_ln --gpu 0 --num_samples 200\\\\' > /root/autodl-tmp/analysis/cka_full_occ_ln/cka_run.log 2>&1 & echo \\\"PID=$!\\\"'\\n\\nStdout:\\n\\nPID=853932\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-25T01:49:04.994030+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-10894",
  "command": "ps -p 853932 -o pid,cmd",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-10894",
    "command": "ps -p 853932 -o pid,cmd",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-25T01:49:04.994154+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-10894",
  "command": "tail -30 /root/autodl-tmp/analysis/cka_full_occ_ln/cka_run.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-10894",
    "command": "tail -30 /root/autodl-tmp/analysis/cka_full_occ_ln/cka_run.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-25T01:49:04.994277+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"   PID CMD\\n\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 1.06}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-25T01:49:04.994441+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[09:47:37]   Result: 51 layers x 200 samples\\n[09:47:37] === Extracting: Full OCC+LN ===\\n[09:47:37]   Loading model from /root/autodl-tmp/checkpoints/full_occ_ln_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt\\n\\rLoading checkpoint shards:   0%|          | 0/4 [00:00<?, ?it/s]\\rLoading checkpoint shards:  25%|██▌       | 1/4 [00:00<00:00,  4.99it/s]\\rLoading checkpoint shards:  50%|█████     | 2/4 [00:00<00:00,  6.15it/s]\\rLoading checkpoint shards:  75%|███████▌  | 3/4 [00:00<00:00,  6.64it/s]\\rLoading checkpoint shards: 100%|██████████| 4/4 [00:00<00:00,  5.90it/s]\\rLoading checkpoint shards: 100%|██████████| 4/4 [00:00<00:00,  5.96it/s]\\n[09:47:38]   Model loaded, extracting vision backbone\\n[09:47:38]   Vision backbone on GPU\\n[09:47:38]   Freed base model\\n[09:47:38]   DINOv2: 24 blocks, SigLIP: 27 blocks\\n[09:47:38]   Running forward pass on 200 samples (25 batches)...\\n[09:47:38]   Batch 5/25 done\\n[09:47:38]   Batch 10/25 done\\n[09:47:39]   Batch 15/25 done\\n[09:47:39]   Batch 20/25 done\\n[09:47:39]   Batch 25/25 done\\n[09:47:39]   Forward pass complete\\n[09:47:39]   Cleaned up, GPU cache cleared\\n[09:47:39]   Result: 51 layers x 200 samples\\n[09:47:39] Computing CKA...\\n[09:47:40] Saved: /root/autodl-tmp/analysis/cka_full_occ_ln/cka_results.json\\n[09:47:40] Generating plots...\\n[09:47:40] Saved: cka_analysis.pdf, cka_analysis.png\\n[09:47:40] \\n[09:47:40] =================================================================\\n[09:47:40] CKA Summary (higher = more similar to pretrained)\\n[09:47:40] =================================================================\\n[09:47:40] Condition         DINOv2 mean  DINOv2 min   SigLIP mean  SigLIP min\\n[09:47:40] -----------------------------------------------------------------\\n[09:47:40] Full OCC+LN            0.6404      0.2558        0.9497      0.8479\\n[09:47:40] ===================
…[truncated 170 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-25T01:49:04.994645+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "cka_full_occ_ln_s0",
  "field": "status",
  "value": "DONE",
  "project": "occsafe_vla",
  "spec": "{'command': \"CUDA_VISIBLE_DEVICES=1 python analysis/cka_analysis.py --pretrained_path /root/autodl-tmp/models/openvla-7b --checkpoint_paths /root/autodl-tmp/checkpoints/full_occ_ln_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt --condition_names 'Full OCC+LN' --libero_data_dir /root/autodl-tmp/libero_datasets/libero_spatial --output_dir /root/autodl-tmp/analysis/cka_full_occ_ln --gpu 0 --num_samples 200\", 'server': 'westd-10894', 'data_path': '/root/autodl-tmp/libero_datasets/libero_spatial', 'data_count': 200, 'model_name': 'openvla-7b', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/checkpoints/full_occ_ln_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt', 'checkpoint_path': '/root/autodl-tmp/analysis/cka_full_occ_ln/cka_results.json', 'log_path': '/root/autodl-tmp/analysis/cka_full_occ_ln/cka_run.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "cka_full_occ_ln_s0",
    "field": "status",
    "value": "DONE",
    "project": "occsafe_vla",
    "spec": "{'command': \"CUDA_VISIBLE_DEVICES=1 python analysis/cka_analysis.py --pretrained_path /root/autodl-tmp/models/openvla-7b --checkpoint_paths /root/autodl-tmp/checkpoints/full_occ_ln_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt --condition_names 'Full OCC+LN' --libero_data_dir /root/autodl-tmp/libero_datasets/libero_spatial --output_dir /root/autodl-tmp/analysis/cka_full_occ_ln --gpu 0 --num_samples 200\", 'server': 'westd-10894', 'data_path': '/root/autodl-tmp/libero_datasets/libero_spatial', 'data_count': 200, 'model_name': 'openvla-7b', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/checkpoints/full_occ_ln_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt', 'checkpoint_path': '/root/autodl-tmp/analysis/cka_full_occ_ln/cka_results.json', 'log_path': '/root/autodl-tmp/analysis/cka_full_occ_ln/cka_run.log'}"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-25T01:49:04.994826+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → DONE. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.2871}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-25T01:49:04.994961+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "cka_full_occ_ln_s0",
  "field": "conclusion",
  "value": "Full OCC+LN shows significant DINOv2 representation drift (mean CKA=0.6404, min=0.2558) compared to high SigLIP preservation (mean=0.9497, min=0.8479). Unlike Full OCC BN (~0.96 CKA), LayerNorm causes substantial DINOv2 divergence from pretrained, suggesting LN destabilizes DINOv2 features while SigLIP remains robust.",
  "project": "occsafe_vla"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "cka_full_occ_ln_s0",
    "field": "conclusion",
    "value": "Full OCC+LN shows significant DINOv2 representation drift (mean CKA=0.6404, min=0.2558) compared to high SigLIP preservation (mean=0.9497, min=0.8479). Unlike Full OCC BN (~0.96 CKA), LayerNorm causes substantial DINOv2 divergence from pretrained, suggesting LN destabilizes DINOv2 features while SigLIP remains robust.",
    "project": "occsafe_vla"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-25T01:49:04.995094+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid conclusion 'Full OCC+LN shows significant DINOv2 representation drift (mean CKA=0.6404, min=0.2558) compared to high SigLIP preservation (mean=0.9497, min=0.8479). Unlike Full OCC BN (~0.96 CKA), LayerNorm causes substantial DINOv2 divergence from pretrained, suggesting LN destabilizes DINOv2 features while SigLIP remains robust.'. Valid: ['failed', 'killed', 'negative', 'success']\", \"metadata\": {\"elapsed_seconds\": 0.2863}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-25T01:49:04.995221+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "CKA Analysis Full OCC+LN Results",
  "type": "data",
  "description": "CKA similarity results for Full OCC+LN (seed 42, 50K checkpoint) vs pretrained OpenVLA-7B. DINOv2 mean=0.6404, SigLIP mean=0.9497.",
  "project": "occsafe_vla",
  "exp_id": "cka_full_occ_ln_s0",
  "content": "{\n  \"condition\": \"Full OCC+LN\",\n  \"checkpoint\": \"full_occ_ln_s0 50K\",\n  \"num_samples\": 200,\n  \"results\": {\n    \"DINOv2_mean_CKA\": 0.6404,\n    \"DINOv2_min_CKA\": 0.2558,\n    \"SigLIP_mean_CKA\": 0.9497,\n    \"SigLIP_min_CKA\": 0.8479\n  },\n  \"server_paths\": {\n    \"results_json\": \"/root/autodl-tmp/analysis/cka_full_occ_ln/cka_results.json\",\n    \"plot_pdf\": \"/root/autodl-tmp/analysis/cka_full_occ_ln/cka_analysis.pdf\",\n    \"plot_png\": \"/root/autodl-tmp/analysis/cka_full_occ_ln/cka_analysis.png\"\n  }\n}",
  "content_filename": "cka_full_occ_ln_s0_results.json",
  "tags": "['cka', 'representation', 'layernorm', 'factorial']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "CKA Analysis Full OCC+LN Results",
    "type": "data",
    "description": "CKA similarity results for Full OCC+LN (seed 42, 50K checkpoint) vs pretrained OpenVLA-7B. DINOv2 mean=0.6404, SigLIP mean=0.9497.",
    "project": "occsafe_vla",
    "exp_id": "cka_full_occ_ln_s0",
    "content": "{\n  \"condition\": \"Full OCC+LN\",\n  \"checkpoint\": \"full_occ_ln_s0 50K\",\n  \"num_samples\": 200,\n  \"results\": {\n    \"DINOv2_mean_CKA\": 0.6404,\n    \"DINOv2_min_CKA\": 0.2558,\n    \"SigLIP_mean_CKA\": 0.9497,\n    \"SigLIP_min_CKA\": 0.8479\n  },\n  \"server_paths\": {\n    \"results_json\": \"/root/autodl-tmp/analysis/cka_full_occ_ln/cka_results.json\",\n    \"plot_pdf\": \"/root/autodl-tmp/analysis/cka_full_occ_ln/cka_analysis.pdf\",\n    \"plot_png\": \"/root/autodl-tmp/analysis/cka_full_occ_ln/cka_analysis.png\"\n  }\n}",
    "content_filename": "cka_full_occ_ln_s0_results.json",
    "tags": "['cka', 'representation', 'layernorm', 'factorial']"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-25T01:49:04.995353+00:00_

Error executing tool register_artifact: 1 validation error for register_artifactArguments
content
  Input should be a valid string [type=string_type, input_value={'condition': 'Full OCC+L...c_ln/cka_analysis.png'}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-25T01:49:04.995509+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "cka_full_occ_ln_s0",
  "field": "status",
  "value": "RUNNING",
  "project": "occsafe_vla",
  "spec": "{'command': \"CUDA_VISIBLE_DEVICES=1 python analysis/cka_analysis.py --pretrained_path /root/autodl-tmp/models/openvla-7b --checkpoint_paths /root/autodl-tmp/checkpoints/full_occ_ln_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt --condition_names 'Full OCC+LN' --libero_data_dir /root/autodl-tmp/libero_datasets/libero_spatial --output_dir /root/autodl-tmp/analysis/cka_full_occ_ln --gpu 0 --num_samples 200\", 'server': 'westd-10894', 'data_path': '/root/autodl-tmp/libero_datasets/libero_spatial', 'data_count': 200, 'model_name': 'openvla-7b', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/checkpoints/full_occ_ln_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "cka_full_occ_ln_s0",
    "field": "status",
    "value": "RUNNING",
    "project": "occsafe_vla",
    "spec": "{'command': \"CUDA_VISIBLE_DEVICES=1 python analysis/cka_analysis.py --pretrained_path /root/autodl-tmp/models/openvla-7b --checkpoint_paths /root/autodl-tmp/checkpoints/full_occ_ln_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt --condition_names 'Full OCC+LN' --libero_data_dir /root/autodl-tmp/libero_datasets/libero_spatial --output_dir /root/autodl-tmp/analysis/cka_full_occ_ln --gpu 0 --num_samples 200\", 'server': 'westd-10894', 'data_path': '/root/autodl-tmp/libero_datasets/libero_spatial', 'data_count': 200, 'model_name': 'openvla-7b', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/checkpoints/full_occ_ln_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt'}"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-25T01:49:04.995675+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.2881}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-25T01:49:04.995819+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "CKA Analysis Full OCC+LN Results",
  "type": "data",
  "description": "CKA similarity results for Full OCC+LN (seed 42, 50K checkpoint) vs pretrained OpenVLA-7B. DINOv2 mean=0.6404, SigLIP mean=0.9497.",
  "project": "occsafe_vla",
  "exp_id": "cka_full_occ_ln_s0",
  "content": "{\"condition\": \"Full OCC+LN\", \"checkpoint\": \"full_occ_ln_s0 50K\", \"num_samples\": 200, \"results\": {\"DINOv2_mean_CKA\": 0.6404, \"DINOv2_min_CKA\": 0.2558, \"SigLIP_mean_CKA\": 0.9497, \"SigLIP_min_CKA\": 0.8479}, \"server_paths\": {\"results_json\": \"/root/autodl-tmp/analysis/cka_full_occ_ln/cka_results.json\", \"plot_pdf\": \"/root/autodl-tmp/analysis/cka_full_occ_ln/cka_analysis.pdf\", \"plot_png\": \"/root/autodl-tmp/analysis/cka_full_occ_ln/cka_analysis.png\"}}",
  "content_filename": "cka_full_occ_ln_s0_results.json",
  "tags": "['cka', 'representation', 'layernorm', 'factorial']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "CKA Analysis Full OCC+LN Results",
    "type": "data",
    "description": "CKA similarity results for Full OCC+LN (seed 42, 50K checkpoint) vs pretrained OpenVLA-7B. DINOv2 mean=0.6404, SigLIP mean=0.9497.",
    "project": "occsafe_vla",
    "exp_id": "cka_full_occ_ln_s0",
    "content": "{\"condition\": \"Full OCC+LN\", \"checkpoint\": \"full_occ_ln_s0 50K\", \"num_samples\": 200, \"results\": {\"DINOv2_mean_CKA\": 0.6404, \"DINOv2_min_CKA\": 0.2558, \"SigLIP_mean_CKA\": 0.9497, \"SigLIP_min_CKA\": 0.8479}, \"server_paths\": {\"results_json\": \"/root/autodl-tmp/analysis/cka_full_occ_ln/cka_results.json\", \"plot_pdf\": \"/root/autodl-tmp/analysis/cka_full_occ_ln/cka_analysis.pdf\", \"plot_png\": \"/root/autodl-tmp/analysis/cka_full_occ_ln/cka_analysis.png\"}}",
    "content_filename": "cka_full_occ_ln_s0_results.json",
    "tags": "['cka', 'representation', 'layernorm', 'factorial']"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-25T01:49:04.995952+00:00_

Error executing tool register_artifact: 1 validation error for register_artifactArguments
content
  Input should be a valid string [type=string_type, input_value={'condition': 'Full OCC+L...c_ln/cka_analysis.png'}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-25T01:49:04.996091+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "cka_full_occ_ln_s0",
  "field": "status",
  "value": "QUEUED",
  "project": "occsafe_vla"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "cka_full_occ_ln_s0",
    "field": "status",
    "value": "QUEUED",
    "project": "occsafe_vla"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-25T01:49:04.996226+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"cka_full_occ_ln_s0\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-25T01:46:40.104Z\", \"updated_at\": \"2026-05-25T01:48:26.718Z\", \"hypothesis\": \"CKA analysis of Full OCC+LN (seed 42) vs pretrained. Tests whether gradient flow + LayerNorm combination preserves encoder representations similarly to gradient flow + BN (Full OCC BN CKA ~0.96). Completes the 2×2 factorial representation dimension.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9131}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-25T01:49:04.996355+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "CKA Analysis Full OCC+LN Results",
  "type": "data",
  "description": "CKA similarity results for Full OCC+LN (seed 42, 50K checkpoint) vs pretrained OpenVLA-7B. DINOv2 mean=0.6404, SigLIP mean=0.9497.",
  "project": "occsafe_vla",
  "exp_id": "cka_full_occ_ln_s0",
  "content": "{\"condition\":\"Full OCC+LN\",\"checkpoint\":\"full_occ_ln_s0 50K\",\"num_samples\":200,\"results\":{\"DINOv2_mean_CKA\":0.6404,\"DINOv2_min_CKA\":0.2558,\"SigLIP_mean_CKA\":0.9497,\"SigLIP_min_CKA\":0.8479},\"server_paths\":{\"results_json\":\"/root/autodl-tmp/analysis/cka_full_occ_ln/cka_results.json\",\"plot_pdf\":\"/root/autodl-tmp/analysis/cka_full_occ_ln/cka_analysis.pdf\",\"plot_png\":\"/root/autodl-tmp/analysis/cka_full_occ_ln/cka_analysis.png\"}}",
  "content_filename": "cka_full_occ_ln_s0_results.json",
  "tags": "['cka', 'representation', 'layernorm', 'factorial']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "CKA Analysis Full OCC+LN Results",
    "type": "data",
    "description": "CKA similarity results for Full OCC+LN (seed 42, 50K checkpoint) vs pretrained OpenVLA-7B. DINOv2 mean=0.6404, SigLIP mean=0.9497.",
    "project": "occsafe_vla",
    "exp_id": "cka_full_occ_ln_s0",
    "content": "{\"condition\":\"Full OCC+LN\",\"checkpoint\":\"full_occ_ln_s0 50K\",\"num_samples\":200,\"results\":{\"DINOv2_mean_CKA\":0.6404,\"DINOv2_min_CKA\":0.2558,\"SigLIP_mean_CKA\":0.9497,\"SigLIP_min_CKA\":0.8479},\"server_paths\":{\"results_json\":\"/root/autodl-tmp/analysis/cka_full_occ_ln/cka_results.json\",\"plot_pdf\":\"/root/autodl-tmp/analysis/cka_full_occ_ln/cka_analysis.pdf\",\"plot_png\":\"/root/autodl-tmp/analysis/cka_full_occ_ln/cka_analysis.png\"}}",
    "content_filename": "cka_full_occ_ln_s0_results.json",
    "tags": "['cka', 'representation', 'layernorm', 'factorial']"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-25T01:49:04.996489+00:00_

Error executing tool register_artifact: 1 validation error for register_artifactArguments
content
  Input should be a valid string [type=string_type, input_value={'condition': 'Full OCC+L...c_ln/cka_analysis.png'}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-25T01:49:04.996632+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "CKA Analysis Full OCC+LN Results",
  "type": "data",
  "description": "CKA similarity results for Full OCC+LN (seed 42, 50K checkpoint) vs pretrained OpenVLA-7B. DINOv2 mean=0.6404, SigLIP mean=0.9497.",
  "project": "occsafe_vla",
  "exp_id": "cka_full_occ_ln_s0",
  "content": "Condition: Full OCC+LN\\nCheckpoint: full_occ_ln_s0 50K\\nNum samples: 200\\n\\nResults:\\n  DINOv2 mean CKA: 0.6404\\n  DINOv2 min CKA: 0.2558\\n  SigLIP mean CKA: 0.9497\\n  SigLIP min CKA: 0.8479\\n\\nServer paths:\\n  results_json: /root/autodl-tmp/analysis/cka_full_occ_ln/cka_results.json\\n  plot_pdf: /root/autodl-tmp/analysis/cka_full_occ_ln/cka_analysis.pdf\\n  plot_png: /root/autodl-tmp/analysis/cka_full_occ_ln/cka_analysis.png",
  "content_filename": "cka_full_occ_ln_s0_results.txt",
  "tags": "['cka', 'representation', 'layernorm', 'factorial']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "CKA Analysis Full OCC+LN Results",
    "type": "data",
    "description": "CKA similarity results for Full OCC+LN (seed 42, 50K checkpoint) vs pretrained OpenVLA-7B. DINOv2 mean=0.6404, SigLIP mean=0.9497.",
    "project": "occsafe_vla",
    "exp_id": "cka_full_occ_ln_s0",
    "content": "Condition: Full OCC+LN\\nCheckpoint: full_occ_ln_s0 50K\\nNum samples: 200\\n\\nResults:\\n  DINOv2 mean CKA: 0.6404\\n  DINOv2 min CKA: 0.2558\\n  SigLIP mean CKA: 0.9497\\n  SigLIP min CKA: 0.8479\\n\\nServer paths:\\n  results_json: /root/autodl-tmp/analysis/cka_full_occ_ln/cka_results.json\\n  plot_pdf: /root/autodl-tmp/analysis/cka_full_occ_ln/cka_analysis.pdf\\n  plot_png: /root/autodl-tmp/analysis/cka_full_occ_ln/cka_analysis.png",
    "content_filename": "cka_full_occ_ln_s0_results.txt",
    "tags": "['cka', 'representation', 'layernorm', 'factorial']"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-25T01:49:04.996804+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260525_b011ed\", \"name\": \"CKA Analysis Full OCC+LN Results\", \"type\": \"data\", \"description\": \"CKA similarity results for Full OCC+LN (seed 42, 50K checkpoint) vs pretrained OpenVLA-7B. DINOv2 mean=0.6404, SigLIP mean=0.9497.\", \"path\": \"projects/occsafe_vla/artifacts/cka_full_occ_ln_s0/data/cka_full_occ_ln_s0_results.txt\", \"url\": null, \"project\": \"occsafe_vla\", \"exp_id\": \"cka_full_occ_ln_s0\", \"skill\": \"\", \"created_at\": \"2026-05-25T01:48:40.311715+00:00\", \"tags\": [\"cka\", \"representation\", \"layernorm\", \"factorial\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-25T01:49:04.996936+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "cka_full_occ_ln_s0",
  "field": "status",
  "value": "RUNNING",
  "project": "occsafe_vla",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=1 python analysis/cka_analysis.py --pretrained_path /root/autodl-tmp/models/openvla-7b --checkpoint_paths /root/autodl-tmp/checkpoints/full_occ_ln_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt --condition_names Full_OCC+LN --libero_data_dir /root/autodl-tmp/libero_datasets/libero_spatial --output_dir /root/autodl-tmp/analysis/cka_full_occ_ln --gpu 0 --num_samples 200', 'server': 'westd-10894', 'data_path': '/root/autodl-tmp/libero_datasets/libero_spatial', 'data_count': 200, 'model_name': 'openvla-7b', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/checkpoints/full_occ_ln_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "cka_full_occ_ln_s0",
    "field": "status",
    "value": "RUNNING",
    "project": "occsafe_vla",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=1 python analysis/cka_analysis.py --pretrained_path /root/autodl-tmp/models/openvla-7b --checkpoint_paths /root/autodl-tmp/checkpoints/full_occ_ln_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt --condition_names Full_OCC+LN --libero_data_dir /root/autodl-tmp/libero_datasets/libero_spatial --output_dir /root/autodl-tmp/analysis/cka_full_occ_ln --gpu 0 --num_samples 200', 'server': 'westd-10894', 'data_path': '/root/autodl-tmp/libero_datasets/libero_spatial', 'data_count': 200, 'model_name': 'openvla-7b', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/checkpoints/full_occ_ln_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt'}"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-25T01:49:04.997098+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"cka_full_occ_ln_s0\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T01:46:40.104Z\", \"updated_at\": \"2026-05-25T01:48:44.209Z\", \"hypothesis\": \"CKA analysis of Full OCC+LN (seed 42) vs pretrained. Tests whether gradient flow + LayerNorm combination preserves encoder representations similarly to gradient flow + BN (Full OCC BN CKA ~0.96). Completes the 2×2 factorial representation dimension.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python analysis/cka_analysis.py --pretrained_path /root/autodl-tmp/models/openvla-7b --checkpoint_paths /root/autodl-tmp/checkpoints/full_occ_ln_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt --condition_names Full_OCC+LN --libero_data_dir /root/autodl-tmp/libero_datasets/libero_spatial --output_dir /root/autodl-tmp/analysis/cka_full_occ_ln --gpu 0 --num_samples 200\", \"server\": \"westd-10894\", \"data_path\": \"/root/autodl-tmp/libero_datasets/libero_spatial\", \"data_count\": 200, \"model_name\": \"openvla-7b\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/full_occ_ln_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.2467}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-25T01:49:04.997252+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "cka_full_occ_ln_s0",
  "field": "status",
  "value": "DONE",
  "project": "occsafe_vla",
  "spec": "{'checkpoint_path': '/root/autodl-tmp/analysis/cka_full_occ_ln/cka_results.json', 'log_path': '/root/autodl-tmp/analysis/cka_full_occ_ln/cka_run.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "cka_full_occ_ln_s0",
    "field": "status",
    "value": "DONE",
    "project": "occsafe_vla",
    "spec": "{'checkpoint_path': '/root/autodl-tmp/analysis/cka_full_occ_ln/cka_results.json', 'log_path': '/root/autodl-tmp/analysis/cka_full_occ_ln/cka_run.log'}"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-25T01:49:04.997382+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 0.2977}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-25T01:49:04.997501+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "cka_full_occ_ln_s0",
  "field": "conclusion",
  "value": "success",
  "project": "occsafe_vla"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "cka_full_occ_ln_s0",
    "field": "conclusion",
    "value": "success",
    "project": "occsafe_vla"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-25T01:49:04.997644+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"cka_full_occ_ln_s0\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T01:46:40.104Z\", \"updated_at\": \"2026-05-25T01:48:51.231Z\", \"hypothesis\": \"CKA analysis of Full OCC+LN (seed 42) vs pretrained. Tests whether gradient flow + LayerNorm combination preserves encoder representations similarly to gradient flow + BN (Full OCC BN CKA ~0.96). Completes the 2×2 factorial representation dimension.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python analysis/cka_analysis.py --pretrained_path /root/autodl-tmp/models/openvla-7b --checkpoint_paths /root/autodl-tmp/checkpoints/full_occ_ln_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt --condition_names Full_OCC+LN --libero_data_dir /root/autodl-tmp/libero_datasets/libero_spatial --output_dir /root/autodl-tmp/analysis/cka_full_occ_ln --gpu 0 --num_samples 200\", \"server\": \"westd-10894\", \"data_path\": \"/root/autodl-tmp/libero_datasets/libero_spatial\", \"data_count\": 200, \"model_name\": \"openvla-7b\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/full_occ_ln_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt\"}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7839}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-25T01:49:04.997809+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "cka_full_occ_ln_s0",
  "field": "status",
  "value": "DONE",
  "project": "occsafe_vla",
  "spec": "{'checkpoint_path': '/root/autodl-tmp/analysis/cka_full_occ_ln/cka_results.json', 'log_path': '/root/autodl-tmp/analysis/cka_full_occ_ln/cka_run.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "cka_full_occ_ln_s0",
    "field": "status",
    "value": "DONE",
    "project": "occsafe_vla",
    "spec": "{'checkpoint_path': '/root/autodl-tmp/analysis/cka_full_occ_ln/cka_results.json', 'log_path': '/root/autodl-tmp/analysis/cka_full_occ_ln/cka_run.log'}"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-25T01:49:04.997965+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"cka_full_occ_ln_s0\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T01:46:40.104Z\", \"updated_at\": \"2026-05-25T01:48:55.643Z\", \"hypothesis\": \"CKA analysis of Full OCC+LN (seed 42) vs pretrained. Tests whether gradient flow + LayerNorm combination preserves encoder representations similarly to gradient flow + BN (Full OCC BN CKA ~0.96). Completes the 2×2 factorial representation dimension.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python analysis/cka_analysis.py --pretrained_path /root/autodl-tmp/models/openvla-7b --checkpoint_paths /root/autodl-tmp/checkpoints/full_occ_ln_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt --condition_names Full_OCC+LN --libero_data_dir /root/autodl-tmp/libero_datasets/libero_spatial --output_dir /root/autodl-tmp/analysis/cka_full_occ_ln --gpu 0 --num_samples 200\", \"server\": \"westd-10894\", \"data_path\": \"/root/autodl-tmp/libero_datasets/libero_spatial\", \"data_count\": 200, \"model_name\": \"openvla-7b\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/full_occ_ln_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt\", \"checkpoint_path\": \"/root/autodl-tmp/analysis/cka_full_occ_ln/cka_results.json\", \"log_path\": \"/root/autodl-tmp/analysis/cka_full_occ_ln/cka_run.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T01:48:55.643Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9154}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 55 · 2026-05-25T01:49:04.998141+00:00_

任务完成。

**CKA 分析结果 (Full OCC+LN vs Pretrained)**:

| 指标 | DINOv2 | SigLIP |
|------|--------|--------|
| Mean CKA | **0.6404** | **0.9497** |
| Min CKA | 0.2558 | 0.8479 |

**关键发现**: Full OCC+LN 的 DINOv2 表征漂移显著（mean CKA=0.64），远低于 Full OCC BN 的 ~0.96。SigLIP 保持高度相似（0.95）。这说明 LayerNorm 在全梯度流条件下会导致 DINOv2 特征大幅偏离预训练表征，而 BatchNorm 能更好地保持 DINOv2 稳定性。2×2 factorial 表征维度数据完整。

**产出文件**（服务器 westd-10894）:
- `/root/autodl-tmp/analysis/cka_full_occ_ln/cka_results.json`
- `/root/autodl-tmp/analysis/cka_full_occ_ln/cka_analysis.pdf`
- `/root/autodl-tmp/analysis/cka_full_occ_ln/cka_analysis.png`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_cka_full_occ_ln_s0_20260525T014618"
}
```

</details>

---
