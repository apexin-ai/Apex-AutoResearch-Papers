# cron hook eval supp adapt tau025 spatial s44 20260524T005546 856213

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 2
- **Tool calls:** 12
- **Original source:** `logs/chats/archive/cron_hook_eval-supp-adapt-tau025-spatial-s44_20260524T005546_856213.jsonl`
- **Structured JSON:** [`3ddabfb9fba23eb8f618.json`](../../sessions/3d/3ddabfb9fba23eb8f618.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

26 recorded events

### User

_source line 1 · 2026-05-23T08:39:36.212191+00:00_

[CRON] 实验进程已正常退出，状态已转为 ANALYZING，需要你分析结果并推进到 DONE。
详情: Process exited cleanly, W&B data available

- exp_id: eval-supp-adapt-tau025-spatial-s44
- project: acr-vla-conformal-refinement
- server: bjb1-32546

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:eval-supp-adapt-tau025-spatial-s44",
  "source": "cron:hook"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-23T08:39:48.758525+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-supp-adapt-tau025-spatial-s44",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-23T08:39:48.764765+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-supp-adapt-tau025-spatial-s44",
  "tool": "ToolSearch",
  "elapsed_ms": 6
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-23T08:39:51.739744+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "limit": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-supp-adapt-tau025-spatial-s44",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "limit": "0"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T08:39:51.740157+00:00_

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
  "session": "cron:hook:eval-supp-adapt-tau025-spatial-s44",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-23T08:39:52.802161+00:00_

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
  "session": "cron:hook:eval-supp-adapt-tau025-spatial-s44",
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

_source line 7 · 2026-05-23T08:39:52.863091+00:00_

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
  "session": "cron:hook:eval-supp-adapt-tau025-spatial-s44",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T08:39:55.764285+00:00_

Error: result (386,345 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-a5fe17a5/5cfee8a3-dcdb-4e5d-8140-b9c6e6cec655/tool-results/mcp-agent-ml-research-read_registry-1779525595657.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-a5fe17a5/5cfee8a3-dcdb-4e5d-8140-b9c6e6cec655/tool-results/mcp-agent-ml-research-read_registry-1779525595657.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-a5fe17a5/5cfee8a3-dcdb-4e5d-8140-b9c6e6cec655/tool-results/mcp-agent-ml-research-read_registry-1779525595657.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-supp-adapt-tau025-spatial-s44",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 4024
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-23T08:42:00.961243+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 19, \"results\": [{\"exp_id\": \"precompute-pi05-object-2048-r2\", \"success\": true, \"actions\": [\"Job still running (pid=113456)\"]}, {\"exp_id\": \"precompute-pi05-spatial-2048-r2\", \"success\": true, \"actions\": [\"Job still running (pid=113796)\"]}, {\"exp_id\": \"precompute-pi05-goal-2048-r2\", \"success\": true, \"actions\": [\"Job still running (pid=114159)\"]}, {\"exp_id\": \"precompute-pi05-long-2048-r2\", \"success\": true, \"actions\": [\"Job still running (pid=114507)\"]}, {\"exp_id\": \"eval-supp-goal-adapt-tau025-s42\", \"success\": true, \"actions\": [\"Job still running (pid=603657)\"]}, {\"exp_id\": \"eval-supp-k2mean-spatial-s43\", \"success\": true, \"actions\": [\"Job still running (pid=16439)\"]}, {\"exp_id\": \"eval-supp-k2mean-object-s43\", \"success\": true, \"actions\": [\"Job still running (pid=16441)\"]}, {\"exp_id\": \"eval-supp-k2mean-goal-s43\", \"success\": true, \"actions\": [\"Job still running (pid=16445)\"]}, {\"exp_id\": \"eval-supp-reconvla-spatial-s43\", \"success\": true, \"actions\": [\"Job still running (pid=34387)\"]}, {\"exp_id\": \"eval-supp-reconvla-spatial-s44\", \"success\": true, \"actions\": [\"Job still running (pid=34383)\"]}, {\"exp_id\": \"eval-supp-goal-reconvla-s43\", \"success\": true, \"actions\": [\"Job still running (pid=34385)\"]}, {\"exp_id\": \"eval-supp-crm-norm005-spatial-s44\", \"success\": true, \"actions\": [\"Job still running (pid=759215)\"]}, {\"exp_id\": \"train-crm-unified-4suite-r6\", \"success\": true, \"actions\": [\"Job still running (pid=668382)\"]}, {\"exp_id\": \"eval-supp-obj-adapt-tau025-s42\", \"success\": true, \"actions\": [\"Job still running (pid=620549)\"]}, {\"exp_id\": \"eval-supp-k2mean-object-s42\", \"success\": true, \"actions\": [\"Job still running (pid=618927)\"]}, {\"exp_id\": \"eval-supp-goal-reconvla-s42\", \"success\": true, \"actions\": [\"Job still running (pid=620827)\"]}, {\"exp_id\": \"eval-supp-k2mean
…[truncated 363 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-supp-adapt-tau025-spatial-s44",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 129221
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T08:42:00.962203+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-23T08:39:32Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 777 个实验 — ALLOCATED 1, ANALYZING 1, DEPLOYED 5, DONE 659, PENDING 1, PREPARING 94, QUEUED 1, RUNNING 15\\n**DONE 分布**: failed 83, killed 149, negative 50, success 377\\n\\n### GPU 占用\\n- **实际运行**: 14 张 — bjb1-32546:cuda:3(train-crm-unified-4suite-r6), bjb2-28827:cuda:2(eval-supp-goal-adapt-tau025-s42), bjb1-32546:cuda:5(eval-supp-crm-norm005-spatial-s44), bjb2-28827:cuda:4(eval-supp-k2mean-spatial-s42), bjb2-28827:cuda:1(eval-supp-k2mean-object-s42), bjb2-28827:cuda:3(eval-supp-goal-reconvla-s42), bjb2-28827:cuda:5(eval-goal-vla-only-wrapper-s42), cqa1-32758:cuda:1(eval-supp-reconvla-spatial-s43), cqa1-32758:cuda:3(eval-supp-reconvla-spatial-s44), bjb2-28827:cuda:0(eval-supp-obj-adapt-tau025-s42), cqa1-32758:cuda:0(eval-supp-k2mean-spatial-s43), cqa1-32758:cuda:2(eval-supp-k2mean-object-s43), cqa1-32758:cuda:4(eval-supp-k2mean-goal-s43), cqa1-32758:cuda:5(eval-supp-goal-reconvla-s43)\\n\\n### 💾 磁盘余量\\n- **bjb2-40593**:\\n  - `/init`: 150M/150M 可用（已用 0%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 45G/437G 可用（已用 90%） ⚠️\\n- **bjb1-18228**:\\n  - `/autodl-pub`: 380G/7.0T 可用（已用 95%） ⚠️\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 400G/438G 可用（已用 4%）\\n- **bjb1-32546**:\\n  - `/autodl-pub`: 1.1T/7.0T 可用（已用 85%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 400G/438G 可用（已用 4%）\\n- **bjb2-28827**:\\n  - `/autodl-pub`: 4.4T/14T 可用（已用 69%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 399G/439G 可用（已用 5%）\\n- **cqa1-32758**:\\n  - `/autodl-pub`: 282G/7.0T 可用（已用 97%） ⚠️\\n  - `/autodl-pub/data`: 1.5T/4.0T 可用（已用 65%）\\n  - `/usr/bin
…[truncated 9553 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-supp-adapt-tau025-spatial-s44",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 128160
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-23T08:42:01.013074+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-23 UTC | 更新原因: Object Suite 结果更新 + GPU 状态更新\\n\\n> 详见 paper_framing.md\\n\\n## 核心方向\\n**ACR-VLA: Adaptive Conformal Refinement for Frozen Flow-Matching VLAs**。Method paper，CoRL 2026 DDL **2026-05-29**（≤6天）。\\n\\n## 用户最高指令\\n**所有 suite × 两个模型，统一 5 组核心实验**：VLA-only / CRM always-on (norm=0.05) / Reconvla K=10 / Adaptive CRM (τ=0.25) / K=2 mean\\n\\n## 已确认结果\\n\\n### Spatial Suite seed42 ✅ COMPLETE\\n| 方法 | K | SR | trigger_rate |\\n|------|---|-----|-------------|\\n| VLA-only | 1 | 78.5% | — |\\n| CRM always-on (norm=0.05) | 10 | 80.0% | 100% |\\n| Reconvla K=10 | 10 | 79.0% | — |\\n| **Adaptive CRM (τ=0.25)** | **2** | **82.0%** | **19.4%** |\\n| K=2 mean | 2 | 🔄 running | — |\\n\\nVLA-only 3-seed: 79.8% ± 1.2%\\n\\n### Goal Suite seed42 (partial)\\n| 方法 | SR |\\n|------|-----|\\n| VLA-only* | 71.0% |\\n| CRM always-on (norm=0.05) | **85.5%** (+14.5pp) |\\n| Adaptive CRM (τ=0.25) | 🔄 running |\\n\\n### Object Suite seed42\\n| 方法 | SR |\\n|------|-----|\\n| VLA-only | 77.8% ± 1.0% (3-seed) |\\n| CRM always-on (norm=0.05) | 77.0% |\\n| Reconvla K=10 | 79.0% |\\n| Adaptive CRM (τ=0.25) | 🔄 running (correct τ; wrong-τ=0.074855 got 77.5% negative) |\\n| K=2 mean | 🔄 running |\\n\\nVLA-only 3-seed: 77.8% ± 1.0%\\n\\n### π0.5 3.6B — VLA-only only\\n全4 suite baseline 完成 (94-99%)。CRM 等 precompute 完（~25-60h）。\\n\\n## 实验矩阵覆盖率\\n\\n| | VLA-only | CRM | Reconvla | Adaptive | K=2 mean |\\n|--|----------|-----|----------|----------|----------|\\n| SmolVLA Spatial | ✅ | ✅ | ✅ | ✅ | 🔄 |\\n| SmolVLA Object | ✅ | ✅ | ✅ | 🔄 | 🔄 |\\n| SmolVLA Goal | ✅* | ✅ | 🔄 | 🔄 | 🔄 |\\n| SmolVLA Long | ❌ | ❌ | ❌ | ❌ | ❌ |\\n| π0.5 all | ✅ | ❌ | ❌ | ❌ | ❌ |\\n\\n## GPU 状态\\n23 GPU / 5 服务器全满载（含新增 cqa1-32758 6×RTX 4090D）\\n\\n## 近期任务\\n- [x] **P0** 修 evaluate.py K=2 
…[truncated 1657 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-supp-adapt-tau025-spatial-s44",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 128149
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-23T08:42:11.775959+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-a5fe17a5/5cfee8a3-dcdb-4e5d-8140-b9c6e6cec655/tool-results/mcp-agent-ml-research-read_registry-1779525595657.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\nfor e in exps:\n    if e.get('exp_id') == 'eval-supp-adapt-tau025-spatial-s44':\n        print(json.dumps(e, indent=2, ensure_ascii=False))\n        break\n\"",
  "description": "Extract eval-supp-adapt-tau025-spatial-s44 from registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-supp-adapt-tau025-spatial-s44",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-a5fe17a5/5cfee8a3-dcdb-4e5d-8140-b9c6e6cec655/tool-results/mcp-agent-ml-research-read_registry-1779525595657.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\nfor e in exps:\n    if e.get('exp_id') == 'eval-supp-adapt-tau025-spatial-s44':\n        print(json.dumps(e, indent=2, ensure_ascii=False))\n        break\n\"",
    "description": "Extract eval-supp-adapt-tau025-spatial-s44 from registry"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-23T08:42:12.128803+00:00_

Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 7, in &lt;module>
    if e.get('exp_id') == 'eval-supp-adapt-tau025-spatial-s44':
       ^^^^^
AttributeError: 'str' object has no attribute 'get'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-supp-adapt-tau025-spatial-s44",
  "tool": "Bash",
  "elapsed_ms": 352
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-23T08:42:25.255352+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-a5fe17a5/5cfee8a3-dcdb-4e5d-8140-b9c6e6cec655/tool-results/mcp-agent-ml-research-read_registry-1779525595657.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\n# check structure\nif isinstance(result, dict) and 'data' in result:\n    d = result['data']\n    if isinstance(d, dict):\n        print(type(d.get('experiments')))\n        exps = d.get('experiments', {})\n        if isinstance(exps, dict):\n            e = exps.get('eval-supp-adapt-tau025-spatial-s44')\n            if e:\n                print(json.dumps(e, indent=2, ensure_ascii=False))\n            else:\n                print('NOT FOUND in dict keys')\n                # try partial match\n                for k in exps:\n                    if 'adapt-tau025-spatial-s44' in k:\n                        print(f'Found key: {k}')\n                        print(json.dumps(exps[k], indent=2, ensure_ascii=False))\n        elif isinstance(exps, list):\n            for e in exps:\n                if isinstance(e, dict) and e.get('exp_id') == 'eval-supp-adapt-tau025-spatial-s44':\n                    print(json.dumps(e, indent=2, ensure_ascii=False))\n                    break\n    else:\n        print('data is not dict:', type(d))\nelse:\n    print('unexpected structure:', type(result))\n\" 2>&1 | head -80",
  "description": "Extract experiment details from registry JSON"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-supp-adapt-tau025-spatial-s44",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-a5fe17a5/5cfee8a3-dcdb-4e5d-8140-b9c6e6cec655/tool-results/mcp-agent-ml-research-read_registry-1779525595657.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\n# check structure\nif isinstance(result, dict) and 'data' in result:\n    d = result['data']\n    if isinstance(d, dict):\n        print(type(d.get('experiments')))\n        exps = d.get('experiments', {})\n        if isinstance(exps, dict):\n            e = exps.get('eval-supp-adapt-tau025-spatial-s44')\n            if e:\n                print(json.dumps(e, indent=2, ensure_ascii=False))\n            else:\n                print('NOT FOUND in dict keys')\n                # try partial match\n                for k in exps:\n                    if 'adapt-tau025-spatial-s44' in k:\n                        print(f'Found key: {k}')\n                        print(json.dumps(exps[k], indent=2, ensure_ascii=False))\n        elif isinstance(exps, list):\n            for e in exps:\n                if isinstance(e, dict) and e.get('exp_id') == 'eval-supp-adapt-tau025-spatial-s44':\n                    print(json.dumps(e, indent=2, ensure_ascii=False))\n                    break\n    else:\n        print('data is not dict:', type(d))\nelse:\n    print('unexpected structure:', type(result))\n\" 2>&1 | head -80",
    "description": "Extract experiment details from registry JSON"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-23T08:42:25.357619+00:00_

&lt;class 'dict'>
{
  "status": "ANALYZING",
  "created_at": "2026-05-23T06:12:35.946Z",
  "updated_at": "2026-05-23T08:39:22.566Z",
  "hypothesis": "Adaptive CRM tau=0.25 multi-seed validation on Spatial (seed44). tau=0.25 confirmed optimal on seed42 (82% SR, +3.5pp over VLA-only, trigger_rate 19.4%). Testing reproducibility across seeds.",
  "parent": "eval-supp-adapt-tau025-spatial-s42-r2"
}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-supp-adapt-tau025-spatial-s44",
  "tool": "Bash",
  "elapsed_ms": 102
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-23T08:42:28.771441+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'exp_id': 'eval-supp-adapt-tau025-spatial-s44'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-supp-adapt-tau025-spatial-s44",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'exp_id': 'eval-supp-adapt-tau025-spatial-s44'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-23T08:42:30.538816+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.7417}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-supp-adapt-tau025-spatial-s44",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1767
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-23T08:42:34.805225+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'status': 'ANALYZING'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-supp-adapt-tau025-spatial-s44",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'status': 'ANALYZING'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-23T08:42:36.511022+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-supp-adapt-tau025-spatial-s44\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T06:12:35.946Z\", \"updated_at\": \"2026-05-23T08:39:22.566Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 multi-seed validation on Spatial (seed44). tau=0.25 confirmed optimal on seed42 (82% SR, +3.5pp over VLA-only, trigger_rate 19.4%). Testing reproducibility across seeds.\", \"parent\": \"eval-supp-adapt-tau025-spatial-s42-r2\", \"spec\": {\"command\": \"bash -c \\\"set -o pipefail; cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark spatial --seed 44 --n_rollouts 20 --max_correction_norm 0.2 2>&1 | tee logs/eval-supp-adapt-tau025-spatial-s44.log\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"742219\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau025-spatial-s44.log\", \"submitted_at\": \"2026-05-23T06:33:10.257Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_count\": 200, \"data_path\": \"/root/acr-vla-conformal-refinement\", \"model_name\": \"smolvla\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}, \"reproduce\": {\"finished_at\": \"2026-05-23T08:39:19.493Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-23T08:39:34.533288+00:00\"}]}}}, \"count\": 1, \"total\": 1, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.7074}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-supp-adapt-tau025-spatial-s44",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1705
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-23T08:42:50.746619+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-a5fe17a5/5cfee8a3-dcdb-4e5d-8140-b9c6e6cec655/tool-results/mcp-agent-ml-research-read_registry-1779525595657.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\ntargets = ['eval-supp-adapt-tau025-spatial-s42-r2', 'eval-supp-adapt-tau025-spatial-s43', 'eval-3dir-adaptive-spatial-s42']\nfor t in targets:\n    if t in exps:\n        print(f'=== {t} ===')\n        print(json.dumps(exps[t], indent=2, ensure_ascii=False))\n        print()\n\" 2>&1 | head -80",
  "description": "Get parent and sibling experiment details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-supp-adapt-tau025-spatial-s44",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-a5fe17a5/5cfee8a3-dcdb-4e5d-8140-b9c6e6cec655/tool-results/mcp-agent-ml-research-read_registry-1779525595657.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\ntargets = ['eval-supp-adapt-tau025-spatial-s42-r2', 'eval-supp-adapt-tau025-spatial-s43', 'eval-3dir-adaptive-spatial-s42']\nfor t in targets:\n    if t in exps:\n        print(f'=== {t} ===')\n        print(json.dumps(exps[t], indent=2, ensure_ascii=False))\n        print()\n\" 2>&1 | head -80",
    "description": "Get parent and sibling experiment details"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-23T08:42:50.897636+00:00_

=== eval-supp-adapt-tau025-spatial-s42-r2 ===
{
  "status": "DONE",
  "created_at": "2026-05-23T04:11:39.644Z",
  "updated_at": "2026-05-23T06:12:07.119Z",
  "hypothesis": "Adaptive CRM with tau=0.25 (~P90) reduces trigger rate to ~20-30% while maintaining SR, mapping the Pareto frontier of trigger_rate vs SR",
  "parent": "eval-3dir-adaptive-spatial-s42",
  "metrics": {
    "overall_sr": 82,
    "n_success": 164,
    "n_total": 200,
    "trigger_rate": 19.4,
    "mean_unc": 0.1847,
    "per_task_sr": {
      "between_plate_and_ramekin": 95,
      "next_to_ramekin": 95,
      "from_table_center": 100,
      "on_cookie_box": 100,
      "in_top_drawer": 75,
      "on_ramekin": 0,
      "next_to_cookie_box": 90,
      "on_stove": 90,
      "next_to_plate": 90,
      "on_wooden_cabinet": 85
    }
  },
  "conclusion": "success"
}

=== eval-supp-adapt-tau025-spatial-s43 ===
{
  "status": "DONE",
  "created_at": "2026-05-23T06:12:16.652Z",
  "updated_at": "2026-05-23T08:36:15.063Z",
  "hypothesis": "Adaptive CRM tau=0.25 multi-seed validation on Spatial (seed43). tau=0.25 confirmed optimal on seed42 (82% SR, +3.5pp over VLA-only, trigger_rate 19.4%). Testing reproducibility across seeds.",
  "parent": "eval-supp-adapt-tau025-spatial-s42-r2",
  "metrics": {
    "success_rate": 80,
    "trigger_rate": 19.4,
    "mean_unc": 0.1845,
    "total_rollouts": 200,
    "total_successes": 160,
    "per_task": {
      "between_plate_and_ramekin": 95,
      "next_to_ramekin": 95,
      "from_table_center": 95,
      "on_cookie_box": 100,
      "in_top_drawer_wooden_cabinet": 70,
      "on_ramekin": 0,
      "next_to_cookie_box": 100,
      "on_stove": 80,
      "next_to_plate": 85,
      "on_wooden_cabinet": 80
    }
  },
  "conclusion": "success"
}

=== eval-3dir-adaptive-spatial-s42 ===
{
  "status": "DONE",
  "created_at": "2026-05-23T01:37:54.656Z",
  "updated_at": "2026-05-23T03:54:21.349Z",
  "hypothesis": "Adaptive CRM (conformal tau=0.074855, K=10 argmin + selective CRM correct
…[truncated 511 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-supp-adapt-tau025-spatial-s44",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-23T08:42:58.203090+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__main_agent_post_to_director",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-supp-adapt-tau025-spatial-s44",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__main_agent_post_to_director",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-23T08:42:58.253772+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-supp-adapt-tau025-spatial-s44",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-23T08:43:17.658466+00:00_

called mcp__agent-ml-research__spawn_worker

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker</summary>

```json
{
  "task_type": "analyze:eval-supp-adapt-tau025-spatial-s44",
  "project": "acr-vla-conformal-refinement",
  "task_prompt": "## 任务\n分析已完成的实验 `eval-supp-adapt-tau025-spatial-s44` 的结果，提取所有关键 metrics。\n\n## 实验信息\n- exp_id: eval-supp-adapt-tau025-spatial-s44\n- server: bjb1-32546\n- log_path: ~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau025-spatial-s44.log (也可能在 /root/acr-vla-conformal-refinement/logs/eval-supp-adapt-tau025-spatial-s44.log)\n- 方法: Adaptive CRM with tau=0.25 on LIBERO-Spatial, seed=44\n- 200 rollouts (10 tasks × 20 rollouts each)\n\n## 需要提取的 metrics\n1. overall success_rate (%)\n2. trigger_rate (CRM 触发率)\n3. mean_unc (平均不确定性)\n4. total_rollouts, total_successes\n5. per_task success rate (每个 task 的 SR)\n6. 任何其他有用的 metrics (如 crm_applied_steps, total_steps 等)\n\n## 步骤\n1. SSH 到 bjb1-32546，读取 log 文件尾部（最后 100-200 行），找到最终汇总结果\n2. 如果 log 文件不在上述路径，尝试 `find /root -name \"eval-supp-adapt-tau025-spatial-s44.log\" 2>/dev/null`\n3. 提取所有 metrics，以 JSON 格式输出\n\n## 对比基准\n- seed42: SR=82.0%, trigger_rate=19.4%\n- seed43: SR=80.0%, trigger_rate=19.4%\n\n## 产出\n用 `update_registry` 更新：\n1. field=\"metrics\", value={所有提取的 metrics}\n2. field=\"conclusion\", value=\"success\" 或 \"negative\"（与 VLA-only baseline 79.8%±1.2% 对比判断）\n3. field=\"status\", value=\"DONE\"\n\n注意：spec 中已有 checkpoint_source 和 log_path，但如果 log_path 不对请用 spec 更新正确路径。\n",
  "tool_groups": "['ssh', 'registry']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-supp-adapt-tau025-spatial-s44",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "tool_args": {
    "task_type": "analyze:eval-supp-adapt-tau025-spatial-s44",
    "project": "acr-vla-conformal-refinement",
    "task_prompt": "## 任务\n分析已完成的实验 `eval-supp-adapt-tau025-spatial-s44` 的结果，提取所有关键 metrics。\n\n## 实验信息\n- exp_id: eval-supp-adapt-tau025-spatial-s44\n- server: bjb1-32546\n- log_path: ~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau025-spatial-s44.log (也可能在 /root/acr-vla-conformal-refinement/logs/eval-supp-adapt-tau025-spatial-s44.log)\n- 方法: Adaptive CRM with tau=0.25 on LIBERO-Spatial, seed=44\n- 200 rollouts (10 tasks × 20 rollouts each)\n\n## 需要提取的 metrics\n1. overall success_rate (%)\n2. trigger_rate (CRM 触发率)\n3. mean_unc (平均不确定性)\n4. total_rollouts, total_successes\n5. per_task success rate (每个 task 的 SR)\n6. 任何其他有用的 metrics (如 crm_applied_steps, total_steps 等)\n\n## 步骤\n1. SSH 到 bjb1-32546，读取 log 文件尾部（最后 100-200 行），找到最终汇总结果\n2. 如果 log 文件不在上述路径，尝试 `find /root -name \"eval-supp-adapt-tau025-spatial-s44.log\" 2>/dev/null`\n3. 提取所有 metrics，以 JSON 格式输出\n\n## 对比基准\n- seed42: SR=82.0%, trigger_rate=19.4%\n- seed43: SR=80.0%, trigger_rate=19.4%\n\n## 产出\n用 `update_registry` 更新：\n1. field=\"metrics\", value={所有提取的 metrics}\n2. field=\"conclusion\", value=\"success\" 或 \"negative\"（与 VLA-only baseline 79.8%±1.2% 对比判断）\n3. field=\"status\", value=\"DONE\"\n\n注意：spec 中已有 checkpoint_source 和 log_path，但如果 log_path 不对请用 spec 更新正确路径。\n",
    "tool_groups": "['ssh', 'registry']"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-23T08:43:21.559490+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_analyze_eval-supp-adapt-tau025-spatial-s44_20260523T084318\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_analyze_eval-supp-adapt-tau025-spatial-s44_20260523T084318.log\", \"setup_data\": {}, \"message\": \"Worker worker_analyze_eval-supp-adapt-tau025-spatial-s44_20260523T084318 started. Use get_worker_status('worker_analyze_eval-supp-adapt-tau025-spatial-s44_20260523T084318') to check progress.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-supp-adapt-tau025-spatial-s44",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "elapsed_ms": 3901
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-23T08:43:25.926429+00:00_

Worker 已派出分析 eval-supp-adapt-tau025-spatial-s44 结果。Worker 完成后系统会回调，届时我更新 registry、report.md 并汇报 Director Spatial Adaptive CRM 3-seed 汇总结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval-supp-adapt-tau025-spatial-s44"
}
```

</details>

---

## Round 2

2 recorded events

### User

_source line 27 · 2026-05-24T00:54:33.334220+00:00_

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
  "session": "cron:hook:eval-supp-adapt-tau025-spatial-s44",
  "source": "system:ralph_loop"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-24T00:55:46.850609+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- GPU 白名单由 `get_project_status` 的 `execution.gpu_ids` 决定，当前 5 台服务器各自分配不同。即使 Director 说"用 cuda:X"也必须 push back 如果不在白名单
- SmolVLA precompute 必须基于 lerobot 官方代码修改的 wrapper pipeline，禁止使用 native precompute（D120/D123）
- Adaptive CRM 的 τ=0.25 是确认的最优值（D129）；Object Suite 之前用了错误的 τ=0.074855 导致 negative（77.5%），必须用 correct τ=0.25 重跑
- CRM checkpoint 路径：SmolVLA 3-suite 统一用 `/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt`；4-suite 版本 `train-crm-unified-4suite-r6` 正在训练中（bjb1-32546:cuda:3）
- π0.5 precompute 是 best-effort 背景任务（D126），不要为它抢 SmolVLA 评估的 GPU

### 2. 🖥️ 基础设施快照
- **bjb1-32546**: 6×GPU，工作目录 `/root/acr-vla-conformal-refinement`，conda base（`/root/miniconda3/bin/python`）
  - 活跃：`train-crm-unified-4suite-r6` (cuda:3, PID 668382), `eval-supp-crm-norm005-spatial-s44` (cuda:5, PID 759215)
  - π0.5 precompute ×4 running (PID 113456/113796/114159/114507)
- **bjb2-28827**: 6×GPU，同路径同环境
  - 活跃 6 个 eval：goal-adapt-tau025-s42(cuda:2), k2mean-object-s42(cuda:1), k2mean-spatial-s42(cuda:4), goal-reconvla-s42(cuda:3), obj-adapt-tau025-s42(cuda:0), goal-vla-only-wrapper-s42(cuda:5)
- **cqa1-32758**: 6×RTX 4090D，同路径同环境
  - 活跃 6 个 eval：k2mean-spatial-s43(cuda:0), reconvla-spatial-s43(cuda:1), k2mean-object-s43(cuda:2), reconvla-spatial-s44(cuda:3), k2mean-goal-s43(cuda:4), goal-reconvla-s43(cuda:5)
- **bjb2-40593**: eval-supp-k2mean-goal-s42-r2 running
- **bjb1-18228**: 无活跃实验，磁盘 95% ⚠️
- CRM checkpoint: `/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt`
- W&B: 项目配置中有 entity/project，用 `fetch_wandb_metrics` 查询
- 磁盘告警：bjb2-40593 根分区 90%，cqa1-32758 autodl-pub 97%

### 3. 📊 当前状态
**刚做完**：收到 `eval-supp-adapt-tau025-spatial-s44` (Adaptive CRM τ=0.25, Spatial seed44) 完成回调，已派 Worker (`worker_analyze_eval-supp-adapt-tau025-spatial-s44_20260523T084318`) 去读日志提取 metrics 并更新 registry。**Worker 尚未回调**。

**等待中的 Worker 回调**：
- `worker_analyze_eval-supp-adapt-tau025-spatial-s44_20260523T084318` — 分析 seed44 结果

**RUNNING 实验（19 个 cron 监控中）**：
| 类别 | 实验 | 摘要 |
|------|------|------|
| 训练 | train-crm-unified-4suite-r6 | 4-suite CRM 训练，完成后解锁 Long Suite 全套评估 |
| Spatial 补充 | eval-supp-crm-norm005-spatial-s44, eval-supp-reconvla-spatial-s43/s44 | multi-seed 填矩阵 |
| Object 补充 | eval-supp-k2mean-object-s42/s43, eval-supp-obj-adapt-tau025-s42 | Object Suite 覆盖 |
| Goal 补充 | eval-supp-goal-adapt-tau025-s42, eval-supp-k2mean-goal-s42-r2/s43, eval-supp-goal-reconvla-s42/s43, eval-goal-vla-only-wrapper-s42 | Goal Suite 覆盖 |
| K=2 mean | eval-supp-k2mean-spatial-s42/s43 | Spatial K=2 mean 补充 |
| π0.5 | precompute-pi05-{object,spatial,goal,long}-2048-r2 ×4 | 背景 precompute（预计 25-60h） |

**PENDING/QUEUED**：
- eval-smolvla-crm-goal-seed44 (PENDING，等人工审批)
- eval-smolvla-lerobot-goal-seed44 (QUEUED，等 GPU)

### 4. 📋 待办（条件触发式）
- Worker `analyze_eval-supp-adapt-tau025-spatial-s44` 回调 → 确认 metrics → 计算 Spatial Adaptive 3-seed mean±std → 更新 ROADMAP → 汇报 Director（含 3-seed 统计显著性判断）
- 每个 eval-supp-* 完成回调 → on-experiment-done 流程（提取 metrics → update registry → 判断 conclusion → 更新 report.md → 汇报 Director）
- train-crm-unified-4suite-r6 完成 → 解锁 Long Suite 全套评估（VLA-only/CRM/Reconvla/Adaptive/K=2mean），需立即规划并提交 Long 评估实验
- Spatial 3-seed 全收齐（s42✅ s43✅ s44 pending Worker） → 计算 5 种方法的 3-seed mean±std，更新 ROADMAP 矩阵
- Object/Goal 各方法 seed42 全收齐 → 开始 multi-seed 补充
- 所有 SmolVLA 矩阵填满 → 开始论文 Results 撰写

### 5. 🎯 战略上下文
- **DDL: CoRL 2026 = 2026-05-29（≤6天）**，2-model paper (SmolVLA 0.4B + π0.5 3.6B)
- **核心 story**：Adaptive CRM 用不确定性门控选择性校正（τ=0.25 时 trigger_rate 仅 ~19%），在保持/提升 SR 的同时大幅降低计算开销
- **D129 关键发现**：Spatial Adaptive CRM 3-seed（s42=82%, s43=80%, s44=pending）仅 +1.0pp over VLA-only（79.8%），p=0.25 不显著。但 Goal Suite CRM always-on 有 +14.5pp 大幅提升——**Goal 可能是论文最强 claim 的来源**
- **D128**：CRM 问题确认为 overcorrection magnitude（非方向错误），norm=0.05 比 norm=0.2/0.3 好
- **易错点**：
  - Object Suite 之前有 τ=0.074855 的错误实验（negative），必须用 τ=0.25
  - K=2 argmin 因 centroid bug（K=2 → d1==d2 → always picks sample 0）等价于 K=1 VLA-only，这证明了 CRM correction 是提升来源而非 sampling diversity
  - VLA-only baseline 各 suite 有不同的 3-seed mean：Spatial 79.8%±1.2%, Object 77.8%±1.0%, Goal 用的是单 seed 71.0%（需补 multi-seed）
  - π0.5 VLA-only 全 4 suite 饱和 (94-99%)，CRM 在高 baseline 上的 headroom 很小，π0.5 的 narrative 需要聚焦在"即使强模型也能从 conformal refinement 获益"
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval-supp-adapt-tau025-spatial-s44"
}
```

</details>

---
