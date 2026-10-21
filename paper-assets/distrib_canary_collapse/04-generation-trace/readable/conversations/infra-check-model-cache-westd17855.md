# infra check model cache westd17855

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/chats/worker_infra_check_model_cache_westd17855_20260518T164248.jsonl`
- **Structured JSON:** [`37457e7bb71e14be2cbe.json`](../../sessions/37/37457e7bb71e14be2cbe.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

23 recorded events

### Tool call

_source line 1 · 2026-05-18T16:43:38.066887+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_infra_check_model_cache_westd17855_20260518T164248",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-18T16:43:38.067166+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_infra_check_model_cache_westd17855_20260518T164248",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T16:43:38.067384+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "ls -la /root/autodl-tmp/.hf_cache/hub/ | grep -E \"pythia-6.9b|gpt2-medium|pythia-1.4b\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_infra_check_model_cache_westd17855_20260518T164248",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "ls -la /root/autodl-tmp/.hf_cache/hub/ | grep -E \"pythia-6.9b|gpt2-medium|pythia-1.4b\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-18T16:43:38.067531+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_infra_check_model_cache_westd17855_20260518T164248",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T16:43:38.067662+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/configs/launch_6.9b.sh",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_infra_check_model_cache_westd17855_20260518T164248",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/configs/launch_6.9b.sh",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-18T16:43:38.067808+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/bin/bash\\n# Pythia-6.9B iterative training — single RTX PRO 6000 (98GB)\\n# bf16 + gradient_checkpointing required\\n\\nset -euo pipefail\\ncd /root/autodl-tmp/distrib_canary_collapse\\n\\nexport HF_ENDPOINT=https://hf-mirror.com\\n\\nSEED=${1:-42}\\nOUTPUT_DIR=\\\"results/generalize/pythia69b_wiki_rtxpro_s${SEED}\\\"\\n\\nCUDA_VISIBLE_DEVICES=0 python iterative_train.py \\\\\\n    --model_name EleutherAI/pythia-6.9b \\\\\\n    --data_dir data/wikitext103_5k \\\\\\n    --output_dir \\\"$OUTPUT_DIR\\\" \\\\\\n    --num_generations 10 \\\\\\n    --steps_per_gen 5000 \\\\\\n    --synthetic_ratio 1.0 \\\\\\n    --seed \\\"$SEED\\\" \\\\\\n    --batch_size 4 \\\\\\n    --max_length 512 \\\\\\n    --lr 5e-5 \\\\\\n    --gen_batch_size 4 \\\\\\n    --gen_max_new_tokens 256 \\\\\\n    --gradient_checkpointing \\\\\\n    --bf16 \\\\\\n    --optim adamw_torch\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.07}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_infra_check_model_cache_westd17855_20260518T164248",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-18T16:43:38.067958+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "python3 /root/autodl-tmp/distrib_canary_collapse/iterative_train.py --help",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_infra_check_model_cache_westd17855_20260518T164248",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "python3 /root/autodl-tmp/distrib_canary_collapse/iterative_train.py --help",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-18T16:43:38.068084+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: python script execution not allowed; use -c for inline expressions only. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_infra_check_model_cache_westd17855_20260518T164248",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T16:43:38.068201+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "ls -la /root/autodl-tmp/distrib_canary_collapse/data/c4_5k/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_infra_check_model_cache_westd17855_20260518T164248",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "ls -la /root/autodl-tmp/distrib_canary_collapse/data/c4_5k/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-18T16:43:38.068388+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 0\\ndrwxr-xr-x 5 root root 62 May 15 16:51 .\\ndrwxr-xr-x 6 root root 99 May 19 00:14 ..\\ndrwxr-xr-x 2 root root 98 May 15 16:51 eval\\ndrwxr-xr-x 2 root root 98 May 15 16:51 prompts\\ndrwxr-xr-x 2 root root 98 May 15 16:51 train\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_infra_check_model_cache_westd17855_20260518T164248",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T16:43:38.068540+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "ls -la /root/autodl-tmp/.hf_cache/hub/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_infra_check_model_cache_westd17855_20260518T164248",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "ls -la /root/autodl-tmp/.hf_cache/hub/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-18T16:43:38.068671+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 12\\ndrwxr-xr-x 9 root root 4096 May 19 00:38 .\\ndrwxr-xr-x 4 root root   45 May 19 00:05 ..\\ndrwxr-xr-x 8 root root 4096 May 19 00:38 .locks\\n-rw-r--r-- 1 root root  191 May 19 00:00 CACHEDIR.TAG\\ndrwxr-xr-x 6 root root   85 May 19 00:09 datasets--wikitext\\ndrwxr-xr-x 6 root root   85 May 19 00:38 models--EleutherAI--pythia-1.4b\\ndrwxr-xr-x 6 root root   85 May 19 00:05 models--EleutherAI--pythia-410m\\ndrwxr-xr-x 6 root root   85 May 19 00:38 models--EleutherAI--pythia-6.9b\\ndrwxr-xr-x 6 root root   85 May 19 00:34 models--gpt2-large\\ndrwxr-xr-x 6 root root   85 May 19 00:38 models--openai-community--gpt2-medium\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_infra_check_model_cache_westd17855_20260518T164248",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T16:43:38.068793+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "grep -i \"batch\" /root/autodl-tmp/distrib_canary_collapse/iterative_train.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_infra_check_model_cache_westd17855_20260518T164248",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "grep -i \"batch\" /root/autodl-tmp/distrib_canary_collapse/iterative_train.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-18T16:43:38.068917+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    p.add_argument(\\\"--batch_size\\\", type=int, default=4)\\n    p.add_argument(\\\"--gen_batch_size\\\", type=int, default=16)\\n    for i in range(0, len(prompt_texts), args.gen_batch_size):\\n        batch_prompts = prompt_texts[i:i + args.gen_batch_size]\\n        enc = tokenizer(batch_prompts, return_tensors=\\\"pt\\\", truncation=True,\\n    tokenized = dataset.map(tokenize_fn, batched=True,\\n        per_device_train_batch_size=args.batch_size,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_infra_check_model_cache_westd17855_20260518T164248",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-18T16:43:38.069050+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "find /root/autodl-tmp/.hf_cache/hub/models--EleutherAI--pythia-6.9b -name \"*.lock\" -o -name \"*.incomplete\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_infra_check_model_cache_westd17855_20260518T164248",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "find /root/autodl-tmp/.hf_cache/hub/models--EleutherAI--pythia-6.9b -name \"*.lock\" -o -name \"*.incomplete\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-18T16:43:38.069176+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/.hf_cache/hub/models--EleutherAI--pythia-6.9b/blobs/34782c3cf3cd80d1eae11d42f1b23c024226651da9c3f2ad61e35afbd724f62b.incomplete\\n/root/autodl-tmp/.hf_cache/hub/models--EleutherAI--pythia-6.9b/blobs/f73019e3a2ce46f8a57f3a35509900df3bb21051da3d28408c646487e6c4451c.incomplete\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_infra_check_model_cache_westd17855_20260518T164248",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-18T16:43:38.069324+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "find /root/autodl-tmp/.hf_cache/hub/models--openai-community--gpt2-medium -name \"*.lock\" -o -name \"*.incomplete\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_infra_check_model_cache_westd17855_20260518T164248",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "find /root/autodl-tmp/.hf_cache/hub/models--openai-community--gpt2-medium -name \"*.lock\" -o -name \"*.incomplete\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-18T16:43:38.069458+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/.hf_cache/hub/models--openai-community--gpt2-medium/blobs/fc5a354a19255ad494f3d71549390baca1ccf61d1d822b9408971705c687c9cd.incomplete\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_infra_check_model_cache_westd17855_20260518T164248",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-18T16:43:38.069580+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "find /root/autodl-tmp/.hf_cache/hub/models--EleutherAI--pythia-1.4b -name \"*.lock\" -o -name \"*.incomplete\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_infra_check_model_cache_westd17855_20260518T164248",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "find /root/autodl-tmp/.hf_cache/hub/models--EleutherAI--pythia-1.4b -name \"*.lock\" -o -name \"*.incomplete\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-18T16:43:38.069697+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_infra_check_model_cache_westd17855_20260518T164248",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-18T16:43:38.069808+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "find /root/autodl-tmp/.hf_cache/hub/.locks -name \"*.lock\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_infra_check_model_cache_westd17855_20260518T164248",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "find /root/autodl-tmp/.hf_cache/hub/.locks -name \"*.lock\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-18T16:43:38.069959+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/.hf_cache/hub/.locks/models--EleutherAI--pythia-410m/0425fa136ba3f95d9428d832cfd7bfd82c78bf1f.lock\\n/root/autodl-tmp/.hf_cache/hub/.locks/models--EleutherAI--pythia-410m/f1860edb10f80bcaf7b023fce47c68a23b724c23.lock\\n/root/autodl-tmp/.hf_cache/hub/.locks/models--EleutherAI--pythia-410m/f74dfbfab8f97770a87769c739fb080c21c8bacc.lock\\n/root/autodl-tmp/.hf_cache/hub/.locks/models--EleutherAI--pythia-410m/0204ed10c186a4c7c68f55dff8f26087a45898d6.lock\\n/root/autodl-tmp/.hf_cache/hub/.locks/models--EleutherAI--pythia-410m/3e09001631bb18ec8a6f4522f8e6ab26a53099e69228f9822adc91bfbe27511b.lock\\n/root/autodl-tmp/.hf_cache/hub/.locks/datasets--wikitext/2a4fec2bc8df76c9d4da1c8e8865b625eb221c76.lock\\n/root/autodl-tmp/.hf_cache/hub/.locks/datasets--wikitext/5f1bea067869d04849c0f975a2b29c4ff47d867f484f5010ea5e861eab246d91.lock\\n/root/autodl-tmp/.hf_cache/hub/.locks/datasets--wikitext/74da360f23826045b3e6ac6375411fdb15f003030aa74f2596ed08b857cb9212.lock\\n/root/autodl-tmp/.hf_cache/hub/.locks/datasets--wikitext/ba090ac30dbf5461e8dcbdd1a1b8e6f3cf9c2c756d64f0c1220450acd514f720.lock\\n/root/autodl-tmp/.hf_cache/hub/.locks/datasets--wikitext/204929b7ff9d6184953f867dedb860e40aa69c078fc1e54b3baaa8fb28511c4c.lock\\n/root/autodl-tmp/.hf_cache/hub/.locks/models--EleutherAI--pythia-1.4b/76f45dd29f6ae40ae5d4960a8df6386aa9cd8d5a.lock\\n/root/autodl-tmp/.hf_cache/hub/.locks/models--EleutherAI--pythia-1.4b/f1860edb10f80bcaf7b023fce47c68a23b724c23.lock\\n/root/autodl-tmp/.hf_cache/hub/.locks/models--EleutherAI--pythia-1.4b/f74dfbfab8f97770a87769c739fb080c21c8bacc.lock\\n/root/autodl-tmp/.hf_cache/hub/.locks/models--EleutherAI--pythia-1.4b/0204ed10c186a4c7c68f55dff8f26087a45898d6.lock\\n/root/autodl-tmp/.hf_cache/hub/.locks/models--EleutherAI--pythia-1.4b/ad4388632e922d0c58c23cb315292d516deb70af0573f9c1543ce84158bff59c.lock\\n/root/autodl-tmp/.hf_cache/hub/.locks/models--gpt2-large/31587029033088429a7e344901883fa792f75b
…[truncated 2305 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_infra_check_model_cache_westd17855_20260518T164248",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-18T16:43:38.070168+00:00_

## 汇总报告

### 1. HF 模型缓存状态

| 模型 | 状态 | 说明 |
|------|------|------|
| EleutherAI/pythia-6.9b | **incomplete** | 2 个 `.incomplete` blob 文件残留 |
| openai-community/gpt2-medium | **incomplete** | 1 个 `.incomplete` blob 文件残留 |
| EleutherAI/pythia-1.4b | **ready** | 无 incomplete/lock 异常 |

pythia-6.9b 和 gpt2-medium 的下载中断了，需要重新触发下载（HF 会自动续传）。

### 2. 6.9B 完整启动命令

```bash
CUDA_VISIBLE_DEVICES=0 python iterative_train.py \
    --model_name EleutherAI/pythia-6.9b \
    --data_dir data/wikitext103_5k \
    --output_dir "results/generalize/pythia69b_wiki_rtxpro_s${SEED}" \
    --num_generations 10 \
    --steps_per_gen 5000 \
    --synthetic_ratio 1.0 \
    --seed "$SEED" \
    --batch_size 4 \
    --max_length 512 \
    --lr 5e-5 \
    --gen_batch_size 4 \
    --gen_max_new_tokens 256 \
    --gradient_checkpointing \
    --bf16 \
    --optim adamw_torch
```

默认 SEED=42，通过 `bash launch_6.9b.sh &lt;seed>` 传参。数据用 wikitext103_5k（不是 c4_5k）。

### 3. batch_size 参数名

| 参数 | 用途 | 默认值 |
|------|------|--------|
| `--batch_size` | 训练 per_device_train_batch_size | 4 |
| `--gen_batch_size` | 生成合成数据时的 batch size | 16（launch_6.9b.sh 覆盖为 4） |

### 4. C4 数据目录

`data/c4_5k/` 存在，含 `train/`、`eval/`、`prompts/` 三个子目录。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_infra_check_model_cache_westd17855_20260518T164248"
}
```

</details>

---
