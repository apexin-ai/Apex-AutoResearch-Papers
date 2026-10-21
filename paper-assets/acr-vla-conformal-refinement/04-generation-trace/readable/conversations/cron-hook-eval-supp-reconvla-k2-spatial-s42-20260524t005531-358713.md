# cron hook eval supp reconvla k2 spatial s42 20260524T005531 358713

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 24
- **Recorded user turns:** 2
- **Tool calls:** 10
- **Original source:** `logs/chats/archive/cron_hook_eval-supp-reconvla-k2-spatial-s42_20260524T005531_358713.jsonl`
- **Structured JSON:** [`6cc5d520dffb4c0dc0b4.json`](../../sessions/6c/6cc5d520dffb4c0dc0b4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

22 recorded events

### User

_source line 1 · 2026-05-23T08:29:25.020130+00:00_

[CRON] 实验进程已正常退出，状态已转为 ANALYZING，需要你分析结果并推进到 DONE。
详情: Process exited cleanly, W&B data available

- exp_id: eval-supp-reconvla-k2-spatial-s42
- project: acr-vla-conformal-refinement
- server: bjb1-32546

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:eval-supp-reconvla-k2-spatial-s42",
  "source": "cron:hook"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-23T08:29:42.606411+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__load_project_config",
  "max_results": "11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-supp-reconvla-k2-spatial-s42",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__load_project_config",
    "max_results": "11"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-23T08:29:42.657092+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-supp-reconvla-k2-spatial-s42",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-23T08:29:46.257656+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "limit": "0",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-supp-reconvla-k2-spatial-s42",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "limit": "0",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T08:29:46.847625+00:00_

called mcp__agent-ml-research__reconcile_crons

<details open><summary>🔧 Tool call — mcp__agent-ml-research__reconcile_crons</summary>

```json
Arguments not recorded in this source.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-supp-reconvla-k2-spatial-s42",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-23T08:29:47.182488+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-supp-reconvla-k2-spatial-s42",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "file": "report.md"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T08:29:47.690651+00:00_

called mcp__agent-ml-research__read_roadmap

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_roadmap</summary>

```json
{
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-supp-reconvla-k2-spatial-s42",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-23T08:29:47.919045+00:00_

called mcp__agent-ml-research__list_workers

<details open><summary>🔧 Tool call — mcp__agent-ml-research__list_workers</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "status": "running"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-supp-reconvla-k2-spatial-s42",
  "tool": "mcp__agent-ml-research__list_workers",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "status": "running"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-23T08:29:51.372391+00:00_

Error: result (1,085,189 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-603d8490/b46a0b83-b02c-45d2-acb6-3d8e034e8fc5/tool-results/mcp-agent-ml-research-read_registry-1779524991135.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-603d8490/b46a0b83-b02c-45d2-acb6-3d8e034e8fc5/tool-results/mcp-agent-ml-research-read_registry-1779524991135.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-603d8490/b46a0b83-b02c-45d2-acb6-3d8e034e8fc5/tool-results/mcp-agent-ml-research-read_registry-1779524991135.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-supp-reconvla-k2-spatial-s42",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 5114
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T08:33:15.388307+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 21, \"results\": [{\"exp_id\": \"precompute-pi05-object-2048-r2\", \"success\": true, \"actions\": [\"Job still running (pid=113456)\"]}, {\"exp_id\": \"precompute-pi05-spatial-2048-r2\", \"success\": true, \"actions\": [\"Job still running (pid=113796)\"]}, {\"exp_id\": \"precompute-pi05-goal-2048-r2\", \"success\": true, \"actions\": [\"Job still running (pid=114159)\"]}, {\"exp_id\": \"precompute-pi05-long-2048-r2\", \"success\": true, \"actions\": [\"Job still running (pid=114507)\"]}, {\"exp_id\": \"eval-supp-adapt-tau025-spatial-s43\", \"success\": true, \"actions\": [\"Sentinel EXIT_CODE=0 → Registry → ANALYZING\", \"Cron deleted\"]}, {\"exp_id\": \"eval-supp-adapt-tau025-spatial-s44\", \"success\": true, \"actions\": [\"Job still running (pid=742219)\"]}, {\"exp_id\": \"eval-supp-crm-norm005-spatial-s43\", \"success\": false, \"actions\": [\"No cron registered for 'eval-supp-crm-norm005-spatial-s43'.\"]}, {\"exp_id\": \"eval-supp-goal-adapt-tau025-s42\", \"success\": true, \"actions\": [\"Job still running (pid=603657)\"]}, {\"exp_id\": \"eval-supp-k2mean-spatial-s43\", \"success\": true, \"actions\": [\"Job still running (pid=16439)\"]}, {\"exp_id\": \"eval-supp-k2mean-object-s43\", \"success\": true, \"actions\": [\"Job still running (pid=16441)\"]}, {\"exp_id\": \"eval-supp-k2mean-goal-s43\", \"success\": true, \"actions\": [\"Job still running (pid=16445)\"]}, {\"exp_id\": \"eval-supp-reconvla-spatial-s43\", \"success\": true, \"actions\": [\"Job still running (pid=34387)\"]}, {\"exp_id\": \"eval-supp-reconvla-spatial-s44\", \"success\": true, \"actions\": [\"Job still running (pid=34383)\"]}, {\"exp_id\": \"eval-supp-goal-reconvla-s43\", \"success\": true, \"actions\": [\"Job still running (pid=34385)\"]}, {\"exp_id\": \"eval-supp-crm-norm005-spatial-s44\", \"success\": true, \"actions\": [\"Skipped (created 98s ago < interval 180s)\"]}, {\"exp_id\": \"train-crm-unified-4suite-r6\", \"success\": 
…[truncated 754 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-supp-reconvla-k2-spatial-s42",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 208540
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-23T08:33:15.389257+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-23T08:31:26Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 776 个实验 — ALLOCATED 1, ANALYZING 3, DEPLOYED 5, DONE 656, PENDING 1, PREPARING 94, QUEUED 1, RUNNING 15\\n**DONE 分布**: failed 83, killed 149, negative 50, success 374\\n\\n### GPU 占用\\n- **实际运行**: 15 张 — bjb1-32546:cuda:3(train-crm-unified-4suite-r6), bjb1-32546:cuda:1(eval-supp-adapt-tau025-spatial-s44), bjb2-28827:cuda:2(eval-supp-goal-adapt-tau025-s42), bjb1-32546:cuda:5(eval-supp-crm-norm005-spatial-s44), bjb2-28827:cuda:4(eval-supp-k2mean-spatial-s42), bjb2-28827:cuda:1(eval-supp-k2mean-object-s42), bjb2-28827:cuda:3(eval-supp-goal-reconvla-s42), bjb2-28827:cuda:5(eval-goal-vla-only-wrapper-s42), cqa1-32758:cuda:1(eval-supp-reconvla-spatial-s43), cqa1-32758:cuda:3(eval-supp-reconvla-spatial-s44), bjb2-28827:cuda:0(eval-supp-obj-adapt-tau025-s42), cqa1-32758:cuda:0(eval-supp-k2mean-spatial-s43), cqa1-32758:cuda:2(eval-supp-k2mean-object-s43), cqa1-32758:cuda:4(eval-supp-k2mean-goal-s43), cqa1-32758:cuda:5(eval-supp-goal-reconvla-s43)\\n\\n### 💾 磁盘余量\\n- **bjb2-40593**:\\n  - `/init`: 150M/150M 可用（已用 0%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 45G/437G 可用（已用 90%） ⚠️\\n- **bjb1-18228**:\\n  - `/autodl-pub`: 380G/7.0T 可用（已用 95%） ⚠️\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 400G/438G 可用（已用 4%）\\n- **bjb1-32546**:\\n  - `/autodl-pub`: 1.1T/7.0T 可用（已用 85%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 400G/438G 可用（已用 4%）\\n- **bjb2-28827**:\\n  - `/autodl-pub`: 4.4T/14T 可用（已用 69%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 399G/439G 可用（已用 5%）\\n- **cqa1-32758**:\\n  - `/autodl-pub`: 288G/7.0T 可用（已用 96%） ⚠️\\n  - `
…[truncated 9761 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-supp-reconvla-k2-spatial-s42",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 208206
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T08:33:15.440660+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-23 UTC | 更新原因: Object Suite 结果更新 + GPU 状态更新\\n\\n> 详见 paper_framing.md\\n\\n## 核心方向\\n**ACR-VLA: Adaptive Conformal Refinement for Frozen Flow-Matching VLAs**。Method paper，CoRL 2026 DDL **2026-05-29**（≤6天）。\\n\\n## 用户最高指令\\n**所有 suite × 两个模型，统一 5 组核心实验**：VLA-only / CRM always-on (norm=0.05) / Reconvla K=10 / Adaptive CRM (τ=0.25) / K=2 mean\\n\\n## 已确认结果\\n\\n### Spatial Suite seed42 ✅ COMPLETE\\n| 方法 | K | SR | trigger_rate |\\n|------|---|-----|-------------|\\n| VLA-only | 1 | 78.5% | — |\\n| CRM always-on (norm=0.05) | 10 | 80.0% | 100% |\\n| Reconvla K=10 | 10 | 79.0% | — |\\n| **Adaptive CRM (τ=0.25)** | **2** | **82.0%** | **19.4%** |\\n| K=2 mean | 2 | 🔄 running | — |\\n\\nVLA-only 3-seed: 79.8% ± 1.2%\\n\\n### Goal Suite seed42 (partial)\\n| 方法 | SR |\\n|------|-----|\\n| VLA-only* | 71.0% |\\n| CRM always-on (norm=0.05) | **85.5%** (+14.5pp) |\\n| Adaptive CRM (τ=0.25) | 🔄 running |\\n\\n### Object Suite seed42\\n| 方法 | SR |\\n|------|-----|\\n| VLA-only | 77.8% ± 1.0% (3-seed) |\\n| CRM always-on (norm=0.05) | 77.0% |\\n| Reconvla K=10 | 79.0% |\\n| Adaptive CRM (τ=0.25) | 🔄 running (correct τ; wrong-τ=0.074855 got 77.5% negative) |\\n| K=2 mean | 🔄 running |\\n\\nVLA-only 3-seed: 77.8% ± 1.0%\\n\\n### π0.5 3.6B — VLA-only only\\n全4 suite baseline 完成 (94-99%)。CRM 等 precompute 完（~25-60h）。\\n\\n## 实验矩阵覆盖率\\n\\n| | VLA-only | CRM | Reconvla | Adaptive | K=2 mean |\\n|--|----------|-----|----------|----------|----------|\\n| SmolVLA Spatial | ✅ | ✅ | ✅ | ✅ | 🔄 |\\n| SmolVLA Object | ✅ | ✅ | ✅ | 🔄 | 🔄 |\\n| SmolVLA Goal | ✅* | ✅ | 🔄 | 🔄 | 🔄 |\\n| SmolVLA Long | ❌ | ❌ | ❌ | ❌ | ❌ |\\n| π0.5 all | ✅ | ❌ | ❌ | ❌ | ❌ |\\n\\n## GPU 状态\\n23 GPU / 5 服务器全满载（含新增 cqa1-32758 6×RTX 4090D）\\n\\n## 近期任务\\n- [x] **P0** 修 evaluate.py K=2 
…[truncated 1538 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-supp-reconvla-k2-spatial-s42",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 207750
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-23T08:33:15.642652+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [{\"worker_id\": \"worker_deploy_bjb2-40593-fix-redeploy-k2mean_20260523T083034\", \"task_type\": \"deploy:bjb2-40593-fix-redeploy-k2mean\", \"project\": \"acr-vla-conformal-refinement\", \"status\": \"running\", \"started_at\": \"2026-05-23T08:30:35.558950+00:00\", \"ended_at\": null}], \"count\": 1}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-supp-reconvla-k2-spatial-s42",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 207723
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-23T08:33:26.900453+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-603d8490/b46a0b83-b02c-45d2-acb6-3d8e034e8fc5/tool-results/mcp-agent-ml-research-read_registry-1779524991135.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# Find the target experiment\ntarget = 'eval-supp-reconvla-k2-spatial-s42'\nfor exp in experiments:\n    if exp.get('exp_id') == target:\n        print('=== TARGET EXPERIMENT ===')\n        print(json.dumps(exp, indent=2))\n        break\n\n# Find all ANALYZING experiments\nprint('\\n=== ALL ANALYZING ===')\nfor exp in experiments:\n    if exp.get('status') == 'ANALYZING':\n        print(f'{exp[\\\"exp_id\\\"]}: conclusion={exp.get(\\\"conclusion\\\")}, server={exp.get(\\\"server\\\")}, metrics={exp.get(\\\"metrics\\\")}')\n\"\n",
  "description": "Extract target experiment and ANALYZING experiments from registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-supp-reconvla-k2-spatial-s42",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-603d8490/b46a0b83-b02c-45d2-acb6-3d8e034e8fc5/tool-results/mcp-agent-ml-research-read_registry-1779524991135.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# Find the target experiment\ntarget = 'eval-supp-reconvla-k2-spatial-s42'\nfor exp in experiments:\n    if exp.get('exp_id') == target:\n        print('=== TARGET EXPERIMENT ===')\n        print(json.dumps(exp, indent=2))\n        break\n\n# Find all ANALYZING experiments\nprint('\\n=== ALL ANALYZING ===')\nfor exp in experiments:\n    if exp.get('status') == 'ANALYZING':\n        print(f'{exp[\\\"exp_id\\\"]}: conclusion={exp.get(\\\"conclusion\\\")}, server={exp.get(\\\"server\\\")}, metrics={exp.get(\\\"metrics\\\")}')\n\"\n",
    "description": "Extract target experiment and ANALYZING experiments from registry"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-23T08:33:27.252871+00:00_

Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 10, in &lt;module>
    if exp.get('exp_id') == target:
       ^^^^^^^
AttributeError: 'str' object has no attribute 'get'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-supp-reconvla-k2-spatial-s42",
  "tool": "Bash",
  "elapsed_ms": 352
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-23T08:33:35.009476+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-603d8490/b46a0b83-b02c-45d2-acb6-3d8e034e8fc5/tool-results/mcp-agent-ml-research-read_registry-1779524991135.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult_str = data['result']\nresult = json.loads(result_str)\n# Check structure\nif isinstance(result, dict) and 'data' in result:\n    d = result['data']\n    if isinstance(d, dict) and 'experiments' in d:\n        exps = d['experiments']\n        print(f'Type: {type(exps)}, len: {len(exps) if isinstance(exps, list) else \\\"N/A\\\"}')\n        if isinstance(exps, list) and len(exps) > 0:\n            print(f'First element type: {type(exps[0])}')\n            print(f'First element (first 200 chars): {str(exps[0])[:200]}')\n        elif isinstance(exps, dict):\n            keys = list(exps.keys())[:5]\n            print(f'Dict keys (first 5): {keys}')\n            first_key = keys[0]\n            print(f'First value type: {type(exps[first_key])}')\n            print(f'First value (first 300 chars): {str(exps[first_key])[:300]}')\n    else:\n        print(f'data keys: {list(d.keys()) if isinstance(d, dict) else type(d)}')\nelse:\n    print(f'result keys: {list(result.keys()) if isinstance(result, dict) else type(result)}')\n\" 2>&1 | head -20\n",
  "description": "Probe registry data structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-supp-reconvla-k2-spatial-s42",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-603d8490/b46a0b83-b02c-45d2-acb6-3d8e034e8fc5/tool-results/mcp-agent-ml-research-read_registry-1779524991135.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult_str = data['result']\nresult = json.loads(result_str)\n# Check structure\nif isinstance(result, dict) and 'data' in result:\n    d = result['data']\n    if isinstance(d, dict) and 'experiments' in d:\n        exps = d['experiments']\n        print(f'Type: {type(exps)}, len: {len(exps) if isinstance(exps, list) else \\\"N/A\\\"}')\n        if isinstance(exps, list) and len(exps) > 0:\n            print(f'First element type: {type(exps[0])}')\n            print(f'First element (first 200 chars): {str(exps[0])[:200]}')\n        elif isinstance(exps, dict):\n            keys = list(exps.keys())[:5]\n            print(f'Dict keys (first 5): {keys}')\n            first_key = keys[0]\n            print(f'First value type: {type(exps[first_key])}')\n            print(f'First value (first 300 chars): {str(exps[first_key])[:300]}')\n    else:\n        print(f'data keys: {list(d.keys()) if isinstance(d, dict) else type(d)}')\nelse:\n    print(f'result keys: {list(result.keys()) if isinstance(result, dict) else type(result)}')\n\" 2>&1 | head -20\n",
    "description": "Probe registry data structure"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-23T08:33:35.161879+00:00_

Type: &lt;class 'dict'>, len: N/A
Dict keys (first 5): ['eval-supp-k2mean-goal-s42', 'eval-supp-crm-norm005-spatial-s43', 'eval-supp-reconvla-k2-spatial-s42', 'eval-supp-goal-reconvla-s43', 'eval-supp-reconvla-spatial-s44']
First value type: &lt;class 'dict'>
First value (first 300 chars): {'status': 'RUNNING', 'retry_count': 0, 'created_at': '2026-05-23T06:56:46.277Z', 'updated_at': '2026-05-23T08:29:42.272Z', 'hypothesis': 'K=2 mean baseline (vla_only mode, 2-sample action average) on Goal suite seed42. Isolates the effect of multi-sample averaging from CRM correction. If K=2 mean ≈

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-supp-reconvla-k2-spatial-s42",
  "tool": "Bash",
  "elapsed_ms": 152
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-23T08:33:40.961447+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-603d8490/b46a0b83-b02c-45d2-acb6-3d8e034e8fc5/tool-results/mcp-agent-ml-research-read_registry-1779524991135.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Target experiment\ntarget_id = 'eval-supp-reconvla-k2-spatial-s42'\ntarget = exps.get(target_id, {})\nprint('=== TARGET: eval-supp-reconvla-k2-spatial-s42 ===')\nprint(json.dumps(target, indent=2))\n\n# All ANALYZING experiments  \nprint('\\n=== ALL ANALYZING ===')\nfor eid, exp in exps.items():\n    if exp.get('status') == 'ANALYZING':\n        print(f'{eid}: conclusion={exp.get(\\\"conclusion\\\")}, metrics={exp.get(\\\"metrics\\\")}, server={exp.get(\\\"server\\\")}')\n\"\n",
  "description": "Extract target experiment and all ANALYZING experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-supp-reconvla-k2-spatial-s42",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-603d8490/b46a0b83-b02c-45d2-acb6-3d8e034e8fc5/tool-results/mcp-agent-ml-research-read_registry-1779524991135.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Target experiment\ntarget_id = 'eval-supp-reconvla-k2-spatial-s42'\ntarget = exps.get(target_id, {})\nprint('=== TARGET: eval-supp-reconvla-k2-spatial-s42 ===')\nprint(json.dumps(target, indent=2))\n\n# All ANALYZING experiments  \nprint('\\n=== ALL ANALYZING ===')\nfor eid, exp in exps.items():\n    if exp.get('status') == 'ANALYZING':\n        print(f'{eid}: conclusion={exp.get(\\\"conclusion\\\")}, metrics={exp.get(\\\"metrics\\\")}, server={exp.get(\\\"server\\\")}')\n\"\n",
    "description": "Extract target experiment and all ANALYZING experiments"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-23T08:33:41.313155+00:00_

=== TARGET: eval-supp-reconvla-k2-spatial-s42 ===
{
  "status": "ANALYZING",
  "retry_count": 0,
  "created_at": "2026-05-23T06:30:30.881Z",
  "updated_at": "2026-05-23T08:29:13.243Z",
  "hypothesis": "K=2 argmin baseline (reconvla mode, --K 2) on Spatial seed42. Due to centroid bug (K=2 \u2192 d1==d2 \u2192 always picks sample 0), K=2 argmin effectively equals K=1 VLA-only (~78.5%). If confirmed, proves 82% improvement comes entirely from CRM correction, not K=2 sampling diversity.",
  "parent": "eval-supp-adapt-tau025-spatial-s42-r2",
  "spec": {
    "command": "bash -c \"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode reconvla --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --K 2 --benchmark spatial --seed 42 --n_rollouts 20 2>&1 | tee logs/eval-supp-reconvla-k2-spatial-s42.log\"",
    "server": "bjb1-32546",
    "gpu": [
      "cuda:2"
    ],
    "pid": "742499",
    "log_path": "~/runs/acr-vla-conformal-refinement/eval-supp-reconvla-k2-spatial-s42.log",
    "submitted_at": "2026-05-23T06:33:15.223Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_count": 200,
    "data_path": "/root/acr-vla-conformal-refinement",
    "model_name": "smolvla",
    "seed": 42,
    "checkpoint_source": "/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt",
    "eval_data": "LIBERO-Spatial"
  },
  "reproduce": {
    "finished_at": "2026-05-23T08:29:06.156Z"
  },
  "extra": {
    "hook_events": [
      {
        "event": "on_complete",
        "action": "agent",
        "ts": "2026-05-23T08:29:26.670985+00:00"
      }
    ]
  }
}

=== ALL ANALYZING ===
eval-supp-reconvla-k2-spatial-s42: conclusion=None, metrics=None, server=None

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-supp-reconvla-k2-spatial-s42",
  "tool": "Bash",
  "elapsed_ms": 351
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-23T08:34:08.744591+00:00_

called mcp__agent-ml-research__spawn_worker

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker</summary>

````json
{
  "task_type": "analyze:eval-supp-reconvla-k2-spatial-s42",
  "project": "acr-vla-conformal-refinement",
  "task_prompt": "## 任务：分析两个已完成实验的日志，提取结果指标\n\n### 实验 1: eval-supp-reconvla-k2-spatial-s42\n- **服务器**: bjb1-32546\n- **假设**: K=2 argmin baseline (reconvla mode, --K 2) on Spatial seed42。由于 centroid bug（K=2 → d1==d2 → always picks sample 0），K=2 argmin 实际等于 K=1 VLA-only (~78.5%)。如果确认，证明 82% 的改进完全来自 CRM correction，不是 K=2 sampling diversity。\n- **日志路径**: 先检查 `/root/acr-vla-conformal-refinement/logs/eval-supp-reconvla-k2-spatial-s42.log`，如果不存在再检查 `~/runs/acr-vla-conformal-refinement/eval-supp-reconvla-k2-spatial-s42.log`\n- **命令**: `python -u src/evaluate.py --mode reconvla --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --K 2 --benchmark spatial --seed 42 --n_rollouts 20`\n\n### 实验 2: eval-supp-adapt-tau025-spatial-s43\n- **服务器**: bjb1-32546\n- **假设**: Adaptive CRM tau=0.25 on Spatial seed43，multi-seed validation\n- **日志路径**: 先检查 `/root/acr-vla-conformal-refinement/logs/eval-supp-adapt-tau025-spatial-s43.log`，如果不存在再检查 `~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau025-spatial-s43.log`\n\n### 需要提取的信息\n对每个实验：\n1. **整体 success rate** (SR%)：通常在日志末尾有汇总，格式类似 \"Success rate: X/200 = Y%\" 或 \"overall_success_rate\"\n2. **每个 task 的 success rate**（如果有）\n3. **trigger_rate**（adaptive 模式下 CRM 被触发的比例，如果有）\n4. **是否有错误或异常**\n5. 确认日志显示进程正常完成（exit code 0 或 \"Evaluation complete\" 之类的标志）\n\n### 操作步骤\n1. SSH (read_only) 到 bjb1-32546\n2. 读取两个实验的日志文件尾部（最后 100 行应该包含汇总）\n3. 如果汇总不在尾部，搜索关键词 \"success\" / \"rate\" / \"summary\" / \"overall\"\n4. 提取所有数值指标\n5. 汇总报告\n\n### 输出格式\n```\n实验: eval-supp-reconvla-k2-spatial-s42\n状态: [正常完成/异常]\n整体 SR: X/200 = Y%\ntrigger_rate: Z% (如有)\n各 task SR: [列表]\n备注: [任何异常或值得注意的信息]\n\n实验: eval-supp-adapt-tau025-spatial-s43\n状态: [正常完成/异常]\n整体 SR: X/200 = Y%\ntrigger_rate: Z% (如有)\n各 task SR: [列表]\n备注: [任何异常或值得注意的信息]\n```\n",
  "tool_groups": "['ssh']"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-supp-reconvla-k2-spatial-s42",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "tool_args": {
    "task_type": "analyze:eval-supp-reconvla-k2-spatial-s42",
    "project": "acr-vla-conformal-refinement",
    "task_prompt": "## 任务：分析两个已完成实验的日志，提取结果指标\n\n### 实验 1: eval-supp-reconvla-k2-spatial-s42\n- **服务器**: bjb1-32546\n- **假设**: K=2 argmin baseline (reconvla mode, --K 2) on Spatial seed42。由于 centroid bug（K=2 → d1==d2 → always picks sample 0），K=2 argmin 实际等于 K=1 VLA-only (~78.5%)。如果确认，证明 82% 的改进完全来自 CRM correction，不是 K=2 sampling diversity。\n- **日志路径**: 先检查 `/root/acr-vla-conformal-refinement/logs/eval-supp-reconvla-k2-spatial-s42.log`，如果不存在再检查 `~/runs/acr-vla-conformal-refinement/eval-supp-reconvla-k2-spatial-s42.log`\n- **命令**: `python -u src/evaluate.py --mode reconvla --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --K 2 --benchmark spatial --seed 42 --n_rollouts 20`\n\n### 实验 2: eval-supp-adapt-tau025-spatial-s43\n- **服务器**: bjb1-32546\n- **假设**: Adaptive CRM tau=0.25 on Spatial seed43，multi-seed validation\n- **日志路径**: 先检查 `/root/acr-vla-conformal-refinement/logs/eval-supp-adapt-tau025-spatial-s43.log`，如果不存在再检查 `~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau025-spatial-s43.log`\n\n### 需要提取的信息\n对每个实验：\n1. **整体 success rate** (SR%)：通常在日志末尾有汇总，格式类似 \"Success rate: X/200 = Y%\" 或 \"overall_success_rate\"\n2. **每个 task 的 success rate**（如果有）\n3. **trigger_rate**（adaptive 模式下 CRM 被触发的比例，如果有）\n4. **是否有错误或异常**\n5. 确认日志显示进程正常完成（exit code 0 或 \"Evaluation complete\" 之类的标志）\n\n### 操作步骤\n1. SSH (read_only) 到 bjb1-32546\n2. 读取两个实验的日志文件尾部（最后 100 行应该包含汇总）\n3. 如果汇总不在尾部，搜索关键词 \"success\" / \"rate\" / \"summary\" / \"overall\"\n4. 提取所有数值指标\n5. 汇总报告\n\n### 输出格式\n```\n实验: eval-supp-reconvla-k2-spatial-s42\n状态: [正常完成/异常]\n整体 SR: X/200 = Y%\ntrigger_rate: Z% (如有)\n各 task SR: [列表]\n备注: [任何异常或值得注意的信息]\n\n实验: eval-supp-adapt-tau025-spatial-s43\n状态: [正常完成/异常]\n整体 SR: X/200 = Y%\ntrigger_rate: Z% (如有)\n各 task SR: [列表]\n备注: [任何异常或值得注意的信息]\n```\n",
    "tool_groups": "['ssh']"
  }
}
````

</details>

---

### Tool result

_source line 21 · 2026-05-23T08:34:14.029211+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_analyze_eval-supp-reconvla-k2-spatial-s42_20260523T083410\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_analyze_eval-supp-reconvla-k2-spatial-s42_20260523T083410.log\", \"setup_data\": {}, \"message\": \"Worker worker_analyze_eval-supp-reconvla-k2-spatial-s42_20260523T083410 started. Use get_worker_status('worker_analyze_eval-supp-reconvla-k2-spatial-s42_20260523T083410') to check progress.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-supp-reconvla-k2-spatial-s42",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "elapsed_ms": 5284
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-23T08:34:18.582161+00:00_

Worker 已派出分析两个实验日志。等待 Worker 回调后处理结果、更新 registry 并汇报 Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval-supp-reconvla-k2-spatial-s42"
}
```

</details>

---

## Round 2

2 recorded events

### User

_source line 23 · 2026-05-24T00:54:29.487073+00:00_

[WRITE HANDOFF] 请立即写你的 handoff。

**格式硬约束**:
- 整条回复**只能**是 &lt;handoff>...&lt;/handoff> 标签包裹
- 禁止在标签外写任何寒暄 / 说明 / 确认（"好的"/"我开始写"/"写完了"等）

**必须覆盖以下 5 个 section（缺一不可，无内容写 N/A）**:

### 1. 🔴 硬约束 / 红线
  本项目特定的不可违反约束（GPU 设备号、服务器名、账号、路径限制等）。
  写本项目特定的，不要抄 CLAUDE.md 通用 L1 红线。
  下一个"你"第一眼看到的就是这里，写错了会被 Director CRITICAL。

### 2. 🖥️ 基础设施快照
  - 服务器名 + 工作目录 + Python 路径 + conda env
  - 模型路径 / 数据集路径 / wandb config / HF cache
  - 活跃进程：PID + tmux session + cron 任务 ID
  写一次就稳定，下一个"你"不用再 SSH 探查。

### 3. 📊 当前状态
  - 你刚做完什么 / 正在做什么
  - registry 里 RUNNING/PREPARING 的实验列表 + 一句话摘要
  - 等待中的 Worker 回调 / Cron / Director 决策

### 4. 📋 待办（条件触发式）
  格式 "条件 X 满足 → 动作 Y"。例如:
  - "Falcon-H1R 下载完成 → sed 修 MODEL_PATH → dry-run → 提交"
  - "pilot_011 出 GC4 结果 → ≥2pp 转架构 narrative，<2pp 写 null-result"

### 5. 🎯 战略上下文
  - 项目核心结论 / 决策链（D001..）
  - 下一个"你"最容易判断错的事 / 容易踩的坑

**写作原则**：
- 第 1 节必须是项目特定的（不是通用 L1 红线）
- 第 2 节让下一轮 BOOT 后能立即开工，避免重新 SSH 探查
- 简洁 > 完整：每节 5-10 行足够，长 handoff 不等于好 handoff

示例格式:
&lt;handoff>
### 1. 🔴 硬约束 / 红线
- 本项目只能用 cuda:4 / cuda:5（之前两次违规 cuda:0 被 Director CRITICAL）
- submit_training_job 不支持 shell builtin（source/conda activate 全不行）

### 2. 🖥️ 基础设施快照
- 服务器：westd-8x6000，工作目录 /root/autodl-tmp/hybrid_reasoning_phases
- Python：/root/miniconda3/bin/python（绝对路径，不走 conda activate）
- 模型：/root/autodl-tmp/qwen35_4b_direct
- 活跃：pilot_011 (PID 203221, tmux=pilot_011, cuda:4)

### 3. 📊 当前状态
我刚完成 pilot_010 分析，正在等 pilot_011 (Falcon-H1R) CoT 生成完成（6/50）。
registry: pilot_011 RUNNING；其他全 DONE。

### 4. 📋 待办
- pilot_011 cron 回调 → spawn worker 跑 probe + GC4 计算
- GC4 ≥2pp → 转架构 narrative；<2pp → null-result paper outline 已就绪

### 5. 🎯 战略上下文
Falcon-H1R 是最后一个数据点。已知 4B/9B GC4 都 FAIL。
易错：不要把 GC4-par (Falcon parallel) 和 GC4-seq (Qwen sequential) 直接对比。
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:eval-supp-reconvla-k2-spatial-s42",
  "source": "system:ralph_loop"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-24T00:55:31.356917+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- GPU 白名单按服务器：bjb1-32546 cuda:0-5, bjb2-28827 cuda:0-5, cqa1-32758 cuda:0-5, bjb1-18228（precompute 专用）, bjb2-40593（precompute 专用）
- SmolVLA precompute 数据在 `/root/autodl-tmp/crm_cache_v5/`（960D obs-only 格式），**不是** π0.5 数据
- CRM checkpoint 路径：SmolVLA 3-suite = `/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt`；4-suite 正在训练 (`train-crm-unified-4suite-r6`)
- evaluate.py K=2 mean 模式需要 `--mode vla_only --K 2`（不是 reconvla），已修复部署
- Adaptive CRM τ 值必须精确：spatial/goal/long 用 τ=0.25，object 用校正后的 τ（之前 τ=0.074855 是错误值导致 negative）
- π0.5 precompute 是 best-effort 背景任务（D126），不阻塞 SmolVLA 主线

### 2. 🖥️ 基础设施快照
- **bjb1-32546**（6×RTX 4090D）：`/root/acr-vla-conformal-refinement/`，conda base `/root/miniconda3/bin/python`
  - 活跃：train-crm-unified-4suite-r6 (PID 668372, cuda:3)，eval-supp-adapt-tau025-spatial-s44 (PID 742219, cuda:1)，eval-supp-crm-norm005-spatial-s44 (PID 759205, cuda:5)
- **bjb2-28827**（6×GPU）：同路径结构
  - 活跃：eval-supp-goal-adapt-tau025-s42 (cuda:2), eval-supp-k2mean-spatial/object-s42 (cuda:4/1), eval-supp-goal-reconvla-s42 (cuda:3), eval-goal-vla-only-wrapper-s42 (cuda:5), eval-supp-obj-adapt-tau025-s42 (cuda:0)
- **cqa1-32758**（6×RTX 4090D，新增）：同路径结构
  - 活跃：eval-supp-reconvla-spatial-s43 (cuda:1), eval-supp-reconvla-spatial-s44 (cuda:3), eval-supp-k2mean-spatial/object/goal-s43 (cuda:0/2/4), eval-supp-goal-reconvla-s43 (cuda:5)
- **bjb1-18228 / bjb2-40593**：precompute π0.5 专用（precompute-pi05-object/spatial/goal/long-2048-r2 运行中）
- W&B：数据可用（cron 提示 W&B data available）
- 磁盘警告：bjb2-40593 根分区 90%⚠️，cqa1-32758 autodl-pub 96%⚠️

### 3. 📊 当前状态
**刚做完**：session-start 初始化，reconcile crons（21 个），派出 Worker 分析 `eval-supp-reconvla-k2-spatial-s42` 和 `eval-supp-adapt-tau025-spatial-s43` 的日志。

**ANALYZING（待处理）**：
- `eval-supp-reconvla-k2-spatial-s42`：K=2 argmin on Spatial s42，验证 centroid bug 导致 K=2≈K=1（预期 ~78.5%）
- `eval-supp-adapt-tau025-spatial-s43`：Adaptive τ=0.25 Spatial s43，multi-seed 验证（reconcile 刚转 ANALYZING）

**RUNNING（15个）**：全部是 SmolVLA 补充实验矩阵——K=2 mean / Reconvla / Adaptive / CRM-norm005 的多 seed 跑法，覆盖 Spatial/Object/Goal suites。

**等待中**：
- Worker `worker_analyze_eval-supp-reconvla-k2-spatial-s42_20260523T083410` 正在读日志提取 SR，回调后更新 registry + 汇报 Director
- Worker `worker_deploy_bjb2-40593-fix-redeploy-k2mean` 仍在运行
- `train-crm-unified-4suite-r6`（4-suite CRM 训练）完成后才能解锁 Long suite 全套实验

### 4. 📋 待办（条件触发式）
- **Worker 分析回调到达** → 用结果更新 registry（conclusion + metrics），刷新 report.md，汇报 Director（如 K=2 argmin ≈ 78.5% 则 success 确认 CRM 是改进来源）
- **eval-supp-adapt-tau025-spatial-s43 结果就绪** → 与 s42(82.0%) 对比算 multi-seed mean±std，更新 ROADMAP Spatial 行
- **所有 Spatial 3-seed 完成**（s42+s43+s44）→ 计算 VLA-only/Adaptive/CRM/Reconvla/K2mean 各方法的 3-seed mean±std 汇总
- **train-crm-unified-4suite-r6 完成** → 立即铺 Long suite 全套 5 个方法的 eval
- **cqa1-32758 上的 6 个 eval 完成** → 收集 s43 seed 结果，与 s42 对比
- **bjb2-28827 上的 6 个 eval 完成** → 收集 Object/Goal 各方法 s42 结果，更新矩阵
- **π0.5 precompute 完成** → 开始 π0.5 CRM 训练 + eval（best-effort，DDL 前能跑多少跑多少）

### 5. 🎯 战略上下文
- **DDL: CoRL 2026 = 2026-05-29**，≤5 天，所有实验必须在此前完成
- **核心 story**：ACR-VLA = Adaptive Conformal Refinement for frozen flow-matching VLAs。Adaptive CRM τ=0.25 是明星方法（Spatial 82% vs VLA-only 78.5%，仅 19.4% trigger rate）
- **当前瓶颈**：SmolVLA 实验矩阵大量 seed 在跑，Long suite 被 4-suite CRM 训练阻塞
- **关键决策链**：D128(overcorrection 是 magnitude 问题不是方向) → D127(CRM always-correct negative → 3方向并行改进) → D126(π0.5 precompute 降级 best-effort) → D124(放弃第三模型 OFT，锁定 2-model paper)
- **易错点**：
  - Object suite 的 adaptive τ 值与 spatial/goal 不同，之前用错 τ=0.074855 导致 negative
  - K=2 mean 用 `--mode vla_only --K 2`，K=2 argmin 用 `--mode reconvla --K 2`——两个是不同的 baseline，别搞混
  - `eval-supp-goal-crm005-s42` 被标为 success 但实际是 cron 误判（进程还在跑，只完成 ~35%），需要重新评估
  - cqa1-32758 磁盘 96% 使用率，提交新实验前先检查空间
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval-supp-reconvla-k2-spatial-s42"
}
```

</details>

---
