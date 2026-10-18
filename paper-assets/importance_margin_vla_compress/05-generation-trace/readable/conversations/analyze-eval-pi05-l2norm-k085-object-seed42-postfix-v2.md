# analyze eval pi05 l2norm k085 object seed42 postfix v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/chats/worker_analyze_eval_pi05_l2norm_k085_object_seed42_postfix_v2_20260525T091407.jsonl`
- **Structured JSON:** [`9b82415dc4f0790444c1.json`](../../sessions/9b/9b82415dc4f0790444c1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

13 recorded events

### Tool call

_source line 1 · 2026-05-25T09:15:33.229503+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__read_registry",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_pi05_l2norm_k085_object_seed42_postfix_v2_20260525T091407",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__read_registry",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-25T09:15:33.229997+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_l2norm_k085_object_seed42_postfix_v2_20260525T091407",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-25T09:15:33.230304+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-33015",
  "command": "cat ~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k085_object_seed42_postfix_v2.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_pi05_l2norm_k085_object_seed42_postfix_v2_20260525T091407",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-33015",
    "command": "cat ~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k085_object_seed42_postfix_v2.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-25T09:15:33.230525+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'DONE'}",
  "project": "importance_margin_vla_compress",
  "limit": "0",
  "fields": "['name', 'status', 'conclusion', 'metrics', 'config']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_pi05_l2norm_k085_object_seed42_postfix_v2_20260525T091407",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'DONE'}",
    "project": "importance_margin_vla_compress",
    "limit": "0",
    "fields": "['name', 'status', 'conclusion', 'metrics', 'config']"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-25T09:15:33.230917+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-25 15:29:12,236 Config: suite=libero_object, prune=l2norm, keep=0.85, eps=50, gpu=1\\n2026-05-25 15:29:12,236 Loading pi0.5 from /root/autodl-tmp/pi05_libero_finetuned ...\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\n2026-05-25 15:31:07,052 Enabled gradient checkpointing for PI05Pytorch model\\nLoading model from: /root/autodl-tmp/pi05_libero_finetuned\\n✓ Loaded state dict from model.safetensors\\n2026-05-25 15:31:09,932 Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\n2026-05-25 15:31:09,932 Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\nAll keys loaded successfully!\\n2026-05-25 15:31:16,442 Patched embed_image\\n2026-05-25 15:31:16,457 Model: 4143.4M params\\n2026-05-25 15:31:16,457 Vision tokens: 256/image, 3 slots -> 768 total\\n2026-05-25 15:31:16,457 Pruning: l2norm, keep 217/256 tokens/image (651 total)\\n2026-05-25 15:31:17,822 Preprocessor/postprocessor loaded\\n[robosuite WARNING] No private macro file found! (macros.py:53)\\n2026-05-25 15:31:17,848 No private macro file found!\\n[robosuite WARNING] It is recommended to use a private macro file (macros.py:54)\\n2026-05-25 15:31:17,848 It is recommended to use a private macro file\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (macros.py:55)\\n2026-05-25 15:31:17,848 To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py\\n2026-05-25 15:31:17,902 No OpenGL_accelerate module loaded: No module named 'OpenGL_accelerate'\\n[info] using task orders [0, 1, 2,
…[truncated 6292 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_l2norm_k085_object_seed42_postfix_v2_20260525T091407",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-25T09:15:33.233180+00:00_

Error: result (172,462 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/5f8cca85-67ae-4284-b298-e63610bb7542/tool-results/mcp-agent-ml-research-read_registry-1779700469871.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/5f8cca85-67ae-4284-b298-e63610bb7542/tool-results/mcp-agent-ml-research-read_registry-1779700469871.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_l2norm_k085_object_seed42_postfix_v2_20260525T091407",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-25T09:15:33.233587+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/5f8cca85-67ae-4284-b298-e63610bb7542/tool-results/mcp-agent-ml-research-read_registry-1779700469871.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nexperiments = json.loads(data['result'])\n# Filter for pi05 object-related experiments\nkeywords = ['pi05', 'object']\nfor exp in experiments:\n    name = exp.get('name', '')\n    if 'pi05' in name.lower() and 'object' in name.lower():\n        print(f\\\"Name: {name}\\\")\n        print(f\\\"  Status: {exp.get('status')}\\\")\n        print(f\\\"  Conclusion: {exp.get('conclusion')}\\\")\n        print(f\\\"  Metrics: {json.dumps(exp.get('metrics', {}))}\\\")\n        print()\n\"\n",
  "description": "Filter registry for pi05 object experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_pi05_l2norm_k085_object_seed42_postfix_v2_20260525T091407",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/5f8cca85-67ae-4284-b298-e63610bb7542/tool-results/mcp-agent-ml-research-read_registry-1779700469871.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nexperiments = json.loads(data['result'])\n# Filter for pi05 object-related experiments\nkeywords = ['pi05', 'object']\nfor exp in experiments:\n    name = exp.get('name', '')\n    if 'pi05' in name.lower() and 'object' in name.lower():\n        print(f\\\"Name: {name}\\\")\n        print(f\\\"  Status: {exp.get('status')}\\\")\n        print(f\\\"  Conclusion: {exp.get('conclusion')}\\\")\n        print(f\\\"  Metrics: {json.dumps(exp.get('metrics', {}))}\\\")\n        print()\n\"\n",
    "description": "Filter registry for pi05 object experiments"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-25T09:15:33.233824+00:00_

Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 8, in &lt;module>
    name = exp.get('name', '')
           ^^^^^^^
AttributeError: 'str' object has no attribute 'get'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_l2norm_k085_object_seed42_postfix_v2_20260525T091407",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-25T09:15:33.234031+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -c 2000 /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/5f8cca85-67ae-4284-b298-e63610bb7542/tool-results/mcp-agent-ml-research-read_registry-1779700469871.txt",
  "description": "Inspect registry output format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_pi05_l2norm_k085_object_seed42_postfix_v2_20260525T091407",
  "tool": "Bash",
  "tool_args": {
    "command": "head -c 2000 /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/5f8cca85-67ae-4284-b298-e63610bb7542/tool-results/mcp-agent-ml-research-read_registry-1779700469871.txt",
    "description": "Inspect registry output format"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-25T09:15:33.234311+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval_pi05_l2norm_k085_object_seed42_postfix_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 98.4, \"total_episodes\": 500}}, \"eval_openvla_random_k09_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.628, \"total_successes\": 314, \"total_episodes\": 500, \"elapsed_minutes\": 246.3}}, \"eval_openvla_baseline_object_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.74, \"total_episodes\": 500}}, \"eval_pi05_l2norm_k085_long_seed42_postfix_v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_pi05_l2norm_k085_object_seed42_postfix\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_pi05_random_k085_long_seed42_postfix_v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_pi05_random_k085_goal_seed42_postfix_v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_pi05_random_k085_long_seed43_postfix\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 45.6, \"task_sr\": [56, 52, 50, 66, 28, 26, 48, 52, 8, 70], \"total_success\": 228, \"total_episodes\": 500, \"time_minutes\": 160.6}, \"conclusion\": \"success\"}, \"eval_pi05_l2norm_k03_long_seed42_postfix\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"metrics\": {\"overall_sr\": 36.6, \"total_episodes\": 500}}, \"eval_openvla_l2norm_k09_long_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_openvla_random_k09_long_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_openvla_attn_k085_long_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_openvla_attn_k09_long_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_openvla_random_k09_long_seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_pi05_l2norm_k085_long_seed43_postfix_v2\": {\"status\": \"DONE\", \"conclu

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_l2norm_k085_object_seed42_postfix_v2_20260525T091407",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-25T09:15:33.234558+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/5f8cca85-67ae-4284-b298-e63610bb7542/tool-results/mcp-agent-ml-research-read_registry-1779700469871.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\ninner = json.loads(data['result'])\nexperiments = inner['data']['experiments']\n# Find pi05 object experiments and pi05 baseline\nfor name, exp in experiments.items():\n    nl = name.lower()\n    if 'pi05' in nl and ('object' in nl or 'baseline' in nl):\n        print(f'{name}')\n        print(f'  status={exp.get(\\\"status\\\")} conclusion={exp.get(\\\"conclusion\\\")}')\n        print(f'  metrics={json.dumps(exp.get(\\\"metrics\\\", {}))}')\n        print()\n\"\n",
  "description": "Filter pi05 object and baseline experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_pi05_l2norm_k085_object_seed42_postfix_v2_20260525T091407",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/5f8cca85-67ae-4284-b298-e63610bb7542/tool-results/mcp-agent-ml-research-read_registry-1779700469871.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\ninner = json.loads(data['result'])\nexperiments = inner['data']['experiments']\n# Find pi05 object experiments and pi05 baseline\nfor name, exp in experiments.items():\n    nl = name.lower()\n    if 'pi05' in nl and ('object' in nl or 'baseline' in nl):\n        print(f'{name}')\n        print(f'  status={exp.get(\\\"status\\\")} conclusion={exp.get(\\\"conclusion\\\")}')\n        print(f'  metrics={json.dumps(exp.get(\\\"metrics\\\", {}))}')\n        print()\n\"\n",
    "description": "Filter pi05 object and baseline experiments"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-25T09:15:33.235007+00:00_

eval_pi05_l2norm_k085_object_seed42_postfix_v2
  status=DONE conclusion=success
  metrics={"success_rate": 98.4, "total_episodes": 500}

eval_pi05_l2norm_k085_object_seed42_postfix
  status=DONE conclusion=failed
  metrics={}

eval_pi05_random_k085_object_seed42_postfix
  status=DONE conclusion=success
  metrics={"success_rate": 5.6, "total_episodes": 500, "total_successes": 28, "per_task_sr": {"T0_alphabet_soup": 6, "T1_cream_cheese": 2, "T2_salad_dressing": 2, "T3_bbq_sauce": 2, "T4_ketchup": 12, "T5_tomato_sauce": 8, "T6_butter": 4, "T7_milk": 8, "T8_chocolate_pudding": 4, "T9_orange_juice": 8}}

eval_pi05_l2norm_k085_object_seed43_postfix
  status=DONE conclusion=success
  metrics={"success_rate": 99, "total_episodes": 500, "total_successes": 495}

eval_pi05_random_k085_object_seed43_postfix
  status=DONE conclusion=success
  metrics={"overall_sr": 0.048, "total_successes": 24, "total_episodes": 500, "elapsed_min": 164.83}

pi05_baseline_long_seed42
  status=DONE conclusion=success
  metrics={"overall_sr": 92.8, "total_episodes": 500}

eval_pi05_baseline_spatial_seed42
  status=DONE conclusion=success
  metrics={"overall_sr": 97.2, "total_episodes": 500}

eval_pi05_baseline_long_seed42
  status=DONE conclusion=success
  metrics={"overall_sr": 92.8, "total_successes": 464, "total_episodes": 500, "per_task": {"alphabet_soup_tomato_basket": 0.96, "cream_cheese_butter_basket": 0.96, "stove_moka_pot": 0.98, "bowl_bottom_drawer": 1, "mugs_on_plates": 1, "book_in_caddy": 0.98, "mug_plate_chocolate": 0.88, "alphabet_soup_cream_cheese_basket": 0.9, "moka_pots_stove": 0.64, "mug_microwave": 0.98}, "source_file": "westd-38929:/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_baseline_libero_10_seed42.json", "note": "Result from westd-38929 run (2026-05-22). Original cqa1-33015 run was stale. Second cqa1-33015 run=91.6%."}

eval_pi05_baseline_object_seed42
  status=DONE conclusion=success
  metrics={"overall_sr": 98.2, "total_successes": 491, "total_episodes
…[truncated 13900 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_pi05_l2norm_k085_object_seed42_postfix_v2_20260525T091407",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-25T09:15:33.235429+00:00_

All data collected. Here's the analysis:

---

## eval_pi05_l2norm_k085_object_seed42_postfix_v2 — 结果分析

### 本实验结果

**Overall SR: 98.4% (492/500)** | 无错误 | 耗时 98.7min

| Task | Description | SR |
|------|------------|-----|
| T0 | alphabet soup → basket | **100%** (50/50) |
| T1 | cream cheese → basket | **100%** (50/50) |
| T2 | salad dressing → basket | **100%** (50/50) |
| T3 | bbq sauce → basket | **98%** (49/50) |
| T4 | ketchup → basket | **96%** (48/50) |
| T5 | tomato sauce → basket | **98%** (49/50) |
| T6 | butter → basket | **100%** (50/50) |
| T7 | milk → basket | **92%** (46/50) |
| T8 | chocolate pudding → basket | **100%** (50/50) |
| T9 | orange juice → basket | **100%** (50/50) |

Pruning config: L2norm, keep 217/256 tokens/image (651/768 total, 15% pruned)

### 对比表 (π0.5 Object Suite, seed42)

| Method | k | Tokens Kept | SR | vs Baseline |
|--------|-----|------------|------|-------------|
| **Baseline** | 1.0 | 256/256 | **98.2%** | — |
| L2norm | 0.95 | 243 | 98.2% | +0.0pp |
| L2norm | 0.925 | 237 | 99.2% | +1.0pp |
| L2norm | 0.9 | 230 | 98.2% | +0.0pp |
| **L2norm** | **0.85** | **217** | **98.4%** | **+0.2pp** |
| L2norm | 0.7 | 179 | 56.4% | -41.8pp |
| Random | 0.95 | 243 | 74.0% | -24.2pp |
| Random | 0.925 | 237 | 27.2% | -71.0pp |
| Random | 0.9 | 230 | 9.0% | -89.2pp |
| **Random** | **0.85** | **217** | **5.6%** | **-92.6pp** |
| Random | 0.7 | 179 | 77.2% | -21.0pp |

### 跨 seed 一致性 (L2norm k=0.85 Object)

| Run | Seed | SR |
|-----|------|-----|
| postfix_v2 (本次) | 42 | 98.4% |
| v4 | 42 | 98.0% |
| seed43 | 43 | 98.4% |
| seed43_postfix | 43 | 99.0% |

**均值 ≈ 98.5%**, 跨 seed 极其稳定。

### 关键发现

**结论: SUCCESS** — L2norm k=0.85 在 Object suite 上完全保持 baseline 性能（98.4% vs 98.2%），pruning 15% vision tokens 无损。

**Cliff zone 分析要点:**

1. **L2norm 的安全区间延伸到 k=0.85**: L2norm 从 k=0.95 到 k=0.85 全部保持 98%+ SR，说明 importance-based pruning 在移除 15% 低重要性 token 时完全无损。
2. **Random 的 cliff zone 确认在 k=0.85-0.95**: Random 在此区间急剧崩溃（74% → 27% → 9% → 5.6%），而 L2norm 稳如磐石。**k=0.85 处的 gap 达到 92.8pp**（98.4% vs 5.6%），是所有 keep ratio 中 L2norm vs Random 差距最大的点。
3. **Random 的非单调现象**: Random k=0.7 (77.2%) > k=0.95 (74.0%) > k=0.85 (5.6%)，cliff zone 之下反而回升，这暗示 cliff zone 不是简单的"token 不够"，而是特定 keep ratio 区间破坏了某种关键 token 配置。
4. **L2norm cliff 在 k=0.7-0.85 之间**: L2norm 从 k=0.85 (98.4%) 骤降到 k=0.7 (56.4%)，表明 L2norm 的 cliff 比 Random 晚约 10-15pp 才出现，但一旦触及也很剧烈。

**这个数据点的核心价值**: k=0.85 是 L2norm vs Random 差距最极端的点，直接证明 importance-based token selection 能在 Random 完全失效的 regime 下维持接近满分的性能。这对论文的 cliff zone narrative 是最有力的证据之一。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analyze_eval_pi05_l2norm_k085_object_seed42_postfix_v2_20260525T091407"
}
```

</details>

---
