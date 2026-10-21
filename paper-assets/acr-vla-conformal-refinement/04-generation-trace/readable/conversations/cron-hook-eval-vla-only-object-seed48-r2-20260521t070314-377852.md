# cron hook eval vla only object seed48 r2 20260521T070314 377852

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 40
- **Recorded user turns:** 3
- **Tool calls:** 17
- **Original source:** `logs/chats/archive/cron_hook_eval-vla-only-object-seed48-r2_20260521T070314_377852.jsonl`
- **Structured JSON:** [`cd78919095e097faadb0.json`](../../sessions/cd/cd78919095e097faadb0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

36 recorded events

### User

_source line 1 · 2026-05-20T14:53:35.214885+00:00_

[CRON] 实验进程已正常退出，状态已转为 ANALYZING，需要你分析结果并推进到 DONE。
详情: Process exited cleanly, W&B data available

- exp_id: eval-vla-only-object-seed48-r2
- project: acr-vla-conformal-refinement
- server: bjb1-32546

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:eval-vla-only-object-seed48-r2",
  "source": "cron:hook"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-20T14:53:55.566567+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__read_experiment_plan_with_status",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-object-seed48-r2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__read_experiment_plan_with_status",
    "max_results": "10"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-20T14:53:55.625513+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-object-seed48-r2",
  "tool": "ToolSearch",
  "elapsed_ms": 58
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-20T14:53:59.215804+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-object-seed48-r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T14:53:59.496437+00:00_

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
  "session": "cron:hook:eval-vla-only-object-seed48-r2",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-20T14:53:59.995412+00:00_

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
  "session": "cron:hook:eval-vla-only-object-seed48-r2",
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

_source line 7 · 2026-05-20T14:54:00.107759+00:00_

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
  "session": "cron:hook:eval-vla-only-object-seed48-r2",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T14:54:02.829088+00:00_

Error: result (706,137 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-4dbb3434/89b94665-f857-4ec3-be68-7f7db8df7d27/tool-results/mcp-agent-ml-research-read_registry-1779288842627.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-4dbb3434/89b94665-f857-4ec3-be68-7f7db8df7d27/tool-results/mcp-agent-ml-research-read_registry-1779288842627.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-4dbb3434/89b94665-f857-4ec3-be68-7f7db8df7d27/tool-results/mcp-agent-ml-research-read_registry-1779288842627.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-object-seed48-r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 3613
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-20T14:55:45.743580+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 10, \"results\": [{\"exp_id\": \"eval-perdof-object-norm02-seed49\", \"success\": true, \"actions\": [\"Job still running (pid=450375)\"]}, {\"exp_id\": \"eval-adaptive-k-spatial-p90-seed44\", \"success\": true, \"actions\": [\"Sentinel EXIT_CODE=0 → Registry → ANALYZING\", \"Cron deleted\"]}, {\"exp_id\": \"eval-obs-only-spatial-norm02-seed49\", \"success\": true, \"actions\": [\"Job still running (pid=357304)\"]}, {\"exp_id\": \"eval-random-selection-object-seed43\", \"success\": true, \"actions\": [\"Job still running (pid=707407)\"]}, {\"exp_id\": \"eval-argmin-object-seed50\", \"success\": true, \"actions\": [\"Job still running (pid=423622)\"]}, {\"exp_id\": \"eval-vla-only-goal-seed51\", \"success\": false, \"actions\": [\"No cron registered for 'eval-vla-only-goal-seed51'.\"]}, {\"exp_id\": \"eval-random-selection-object-seed45\", \"success\": true, \"actions\": [\"Job still running (pid=468175)\"]}, {\"exp_id\": \"eval-crm-k1-object-seed42-plan702\", \"success\": true, \"actions\": [\"Job still running (pid=401372)\"]}, {\"exp_id\": \"eval-crm-k1-object-seed43-plan702\", \"success\": true, \"actions\": [\"Job still running (pid=401666)\"]}, {\"exp_id\": \"eval-crm-k1-object-seed44-plan702\", \"success\": true, \"actions\": [\"Job still running (pid=402276)\"]}]}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-object-seed48-r2",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 106247
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T14:55:45.744546+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-20T14:54:48Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 461 个实验 — ANALYZING 5, DEPLOYED 4, DONE 412, PREPARING 33, RUNNING 7\\n**DONE 分布**: failed 47, killed 85, negative 33, success 247\\n\\n### GPU 占用\\n- **实际运行**: 8 张 — bjb1-18228:cuda:0(eval-adaptive-k-spatial-p90-seed44), bjb1-32546:cuda:3(eval-argmin-object-seed50), bjb2-28827:cuda:2(eval-obs-only-spatial-norm02-seed49), bjb2-28827:cuda:3(openvla-precompute-k1), bjb2-28827:cuda:0(eval-crm-k1-object-seed42-plan702), bjb2-28827:cuda:1(eval-crm-k1-object-seed43-plan702), bjb2-28827:cuda:5(eval-crm-k1-object-seed44-plan702), bjb1-32546:cuda:2(eval-perdof-object-norm02-seed49)\\n\\n### 💾 磁盘余量\\n- **bjb2-40593**:\\n  - `/init`: 150M/150M 可用（已用 0%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 46G/437G 可用（已用 89%）\\n- **bjb1-18228**:\\n  - `/autodl-pub`: 773G/7.0T 可用（已用 90%） ⚠️\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 400G/438G 可用（已用 4%）\\n- **bjb1-32546**:\\n  - `/autodl-pub`: 890G/7.0T 可用（已用 88%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 400G/438G 可用（已用 4%）\\n- **bjb2-28827**:\\n  - `/autodl-pub`: 4.5T/14T 可用（已用 69%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 399G/439G 可用（已用 5%）\\n\\n### 🏃 RUNNING\\n| exp_id | server | gpu | pid | log |\\n|--------|--------|-----|-----|-----|\\n| `eval-argmin-object-seed50` | bjb1-32546 | cuda:3 | 423608 | `…/acr-vla-conformal-refinement/eval-argmin-object-seed50.log` |\\n| `eval-obs-only-spatial-norm02-seed49` | bjb2-28827 | cuda:2 | 357291 | `…onformal-refinement/eval-obs-only-spatial-norm02-seed49.log` |\\n| `openvla-precompute-k1` | bjb2-28827 | cuda:3 | 365142 | `…runs/acr-vla-co
…[truncated 8779 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-object-seed48-r2",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 105749
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-20T14:55:45.745149+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-20 06:17 UTC | 更新原因: Fix Long OOD data to match D081, update RUNNING section per Reviewer observation\\n\\n> 详见 paper_framing.md（D077: Adaptive K 升级为核心贡献）\\n\\n## 核心方向\\n**Adaptive inference-time compute for frozen VLAs** — K=2 L2 distance 作为不确定性信号，自适应决定每步推理次数。CRM correction>selection 分析作为支撑。\\n\\n## 投稿目标\\n**CoRL 2026** DDL **2026-05-29**。剩余 ~9 天。\\n\\n## D077 方向转换（用户硬要求）\\n- Adaptive K = 论文**核心贡献**（方法）\\n- K=10 分析降为 supporting evidence\\n\\n## 信号候选 (CLOSED)\\n| 信号 | ρ vs K10_var | 结论 |\\n|------|-------------|------|\\n| **K=2 L2 distance** | **0.9979** | **✅ GO — 唯一可用信号** |\\n| CRM correction magnitude | 0.1523 | ❌ NO-GO (D079) |\\n| FMVD | 0.0825 | ❌ NO-GO |\\n\\n## Adaptive K Sweep (Object) — 12/12 DONE ✅\\n| 阈值 | seeds | SR (mean) | avg_K | fast_path% | vs K=10 |\\n|------|-------|-----------|-------|-----------|---------|\\n| P90 | 3/3 ✅ | 13.3% | ~2.6 | ~93% | 74% |\\n| P75 | 3/3 ✅ | 13.7% | ~3.1 | ~87% | 79% |\\n| **P50** | **3/3 ✅** | **15.3%** | **~3.8** | **~77%** | **~91%** |\\n| P25 | 3/3 ✅ | 14.3% | ~4.8 | ~65% | ~85% |\\n\\n**P50 = Pareto 最优 (D078)**。\\n\\n## RUNNING 实验\\n- bjb2-40593: Spatial Adaptive K P50 seed42 (rollout 中)\\n- bjb1-18228: Long VLA-only seed54, Long CRM seed53, Spatial VLA-only seed53\\n- bjb1-32546: Long CRM seed54, Spatial VLA-only seed54\\n- 更多部署中（Agent 处理综合指令）\\n\\n## 待部署\\n1. **Spatial Adaptive K P50 seed43, seed44**\\n2. **Random Selection baseline seed42, seed44** (plan_600)\\n3. **CRM Object K=10 norm02 seed42** (Table 1 n=6→n=7)\\n4. **fig3_kvalue 重新生成**\\n\\n## 论文 CRITICAL 待解决\\n1. **evaluate.py 推理模式确认** — Agent P0\\n2. **Spatial CRM K=10 n=8 溯源** — registry 只有 n=7, Agent 调查中\\n3. **OOD Long/Goal 数据全量更新** — Paper Agent 处理中\\n4. **P25 n=3 更新** — Paper Agent 处理中\\n\\n## 核心实验结果 (LOCKED,
…[truncated 2698 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-object-seed48-r2",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 105637
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-20T14:55:58.881582+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-4dbb3434/89b94665-f857-4ec3-be68-7f7db8df7d27/tool-results/mcp-agent-ml-research-read_registry-1779288842627.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# Find the target experiment\nfor exp in experiments:\n    if exp['exp_id'] == 'eval-vla-only-object-seed48-r2':\n        print(json.dumps(exp, indent=2))\n        break\n\"",
  "description": "Extract eval-vla-only-object-seed48-r2 from registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-object-seed48-r2",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-4dbb3434/89b94665-f857-4ec3-be68-7f7db8df7d27/tool-results/mcp-agent-ml-research-read_registry-1779288842627.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# Find the target experiment\nfor exp in experiments:\n    if exp['exp_id'] == 'eval-vla-only-object-seed48-r2':\n        print(json.dumps(exp, indent=2))\n        break\n\"",
    "description": "Extract eval-vla-only-object-seed48-r2 from registry"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-20T14:56:01.249423+00:00_

Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 9, in &lt;module>
    if exp['exp_id'] == 'eval-vla-only-object-seed48-r2':
       ~~~^^^^^^^^^^
TypeError: string indices must be integers, not 'str'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-object-seed48-r2",
  "tool": "Bash",
  "elapsed_ms": 2367
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T14:56:01.701239+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-4dbb3434/89b94665-f857-4ec3-be68-7f7db8df7d27/tool-results/mcp-agent-ml-research-read_registry-1779288842627.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# Find all vla-only-object experiments for context\nvla_only = [e for e in experiments if 'vla-only-object' in e['exp_id']]\nfor exp in vla_only:\n    print(f\\\"{exp['exp_id']}: status={exp.get('status')}, conclusion={exp.get('conclusion')}, metrics={exp.get('metrics')}\\\")\n\"",
  "description": "List all vla-only-object experiments for context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-object-seed48-r2",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-4dbb3434/89b94665-f857-4ec3-be68-7f7db8df7d27/tool-results/mcp-agent-ml-research-read_registry-1779288842627.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# Find all vla-only-object experiments for context\nvla_only = [e for e in experiments if 'vla-only-object' in e['exp_id']]\nfor exp in vla_only:\n    print(f\\\"{exp['exp_id']}: status={exp.get('status')}, conclusion={exp.get('conclusion')}, metrics={exp.get('metrics')}\\\")\n\"",
    "description": "List all vla-only-object experiments for context"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-20T14:56:01.701719+00:00_

&lt;tool_use_error>Cancelled: parallel tool call Bash(cat /home/ubuntu/.claude-account-1/proje…) errored&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-object-seed48-r2",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-20T14:56:03.966042+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-4dbb3434/89b94665-f857-4ec3-be68-7f7db8df7d27/tool-results/mcp-agent-ml-research-read_registry-1779288842627.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# Also check eval-adaptive-k-spatial-p90-seed44 which just moved to ANALYZING\nfor exp in experiments:\n    if exp['exp_id'] == 'eval-adaptive-k-spatial-p90-seed44':\n        print(json.dumps(exp, indent=2))\n        break\n\"",
  "description": "Extract eval-adaptive-k-spatial-p90-seed44 from registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-object-seed48-r2",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-4dbb3434/89b94665-f857-4ec3-be68-7f7db8df7d27/tool-results/mcp-agent-ml-research-read_registry-1779288842627.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# Also check eval-adaptive-k-spatial-p90-seed44 which just moved to ANALYZING\nfor exp in experiments:\n    if exp['exp_id'] == 'eval-adaptive-k-spatial-p90-seed44':\n        print(json.dumps(exp, indent=2))\n        break\n\"",
    "description": "Extract eval-adaptive-k-spatial-p90-seed44 from registry"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-20T14:56:03.966548+00:00_

&lt;tool_use_error>Cancelled: parallel tool call Bash(cat /home/ubuntu/.claude-account-1/proje…) errored&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-object-seed48-r2",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-20T14:56:10.915876+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-4dbb3434/89b94665-f857-4ec3-be68-7f7db8df7d27/tool-results/mcp-agent-ml-research-read_registry-1779288842627.txt') as f:\n    data = json.load(f)\n# Check structure\nresult_str = data['result']\nresult = json.loads(result_str)\nprint(type(result))\nprint(type(result.get('data')))\nif isinstance(result['data'], dict):\n    print(list(result['data'].keys())[:5])\n    exps = result['data'].get('experiments', [])\n    print(f'experiments type: {type(exps)}, len: {len(exps) if isinstance(exps, list) else \\\"n/a\\\"}')\n    if isinstance(exps, list) and len(exps) > 0:\n        print(f'first exp type: {type(exps[0])}')\n        print(str(exps[0])[:200])\n    elif isinstance(exps, dict):\n        keys = list(exps.keys())[:3]\n        print(f'dict keys sample: {keys}')\n        for k in keys:\n            print(f'{k}: {str(exps[k])[:200]}')\n\"\n",
  "description": "Probe registry JSON structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-object-seed48-r2",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-4dbb3434/89b94665-f857-4ec3-be68-7f7db8df7d27/tool-results/mcp-agent-ml-research-read_registry-1779288842627.txt') as f:\n    data = json.load(f)\n# Check structure\nresult_str = data['result']\nresult = json.loads(result_str)\nprint(type(result))\nprint(type(result.get('data')))\nif isinstance(result['data'], dict):\n    print(list(result['data'].keys())[:5])\n    exps = result['data'].get('experiments', [])\n    print(f'experiments type: {type(exps)}, len: {len(exps) if isinstance(exps, list) else \\\"n/a\\\"}')\n    if isinstance(exps, list) and len(exps) > 0:\n        print(f'first exp type: {type(exps[0])}')\n        print(str(exps[0])[:200])\n    elif isinstance(exps, dict):\n        keys = list(exps.keys())[:3]\n        print(f'dict keys sample: {keys}')\n        for k in keys:\n            print(f'{k}: {str(exps[k])[:200]}')\n\"\n",
    "description": "Probe registry JSON structure"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-20T14:56:11.017606+00:00_

&lt;class 'dict'>
&lt;class 'dict'>
['experiments', 'count', 'total', 'baseline']
experiments type: &lt;class 'dict'>, len: n/a
dict keys sample: ['eval-vla-only-goal-seed51', 'eval-vla-only-object-seed48-r2', 'eval-obs-only-object-norm02-seed50']
eval-vla-only-goal-seed51: {'status': 'RUNNING', 'retry_count': 0, 'created_at': '2026-05-20T05:16:21.107Z', 'updated_at': '2026-05-20T14:53:54.414Z', 'hypothesis': 'VLA-only baseline on LIBERO-Goal seed51. Paired baseline for 
eval-vla-only-object-seed48-r2: {'status': 'ANALYZING', 'retry_count': 0, 'created_at': '2026-05-20T13:08:11.387Z', 'updated_at': '2026-05-20T14:53:19.813Z', 'hypothesis': 'VLA-only baseline on LIBERO-Object seed48 re-run. Prior run
eval-obs-only-object-norm02-seed50: {'status': 'ANALYZING', 'retry_count': 0, 'created_at': '2026-05-20T13:07:41.505Z', 'updated_at': '2026-05-20T14:52:51.145Z', 'hypothesis': 'CRM obs_only (ε=0.2) K=10 on LIBERO-Object seed50. Expandin

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-object-seed48-r2",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-20T14:56:16.686983+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-4dbb3434/89b94665-f857-4ec3-be68-7f7db8df7d27/tool-results/mcp-agent-ml-research-read_registry-1779288842627.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Target experiment\nexp = exps.get('eval-vla-only-object-seed48-r2', {})\nprint('=== eval-vla-only-object-seed48-r2 ===')\nprint(json.dumps(exp, indent=2))\n\"\n",
  "description": "Get full details of target experiment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-object-seed48-r2",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-4dbb3434/89b94665-f857-4ec3-be68-7f7db8df7d27/tool-results/mcp-agent-ml-research-read_registry-1779288842627.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Target experiment\nexp = exps.get('eval-vla-only-object-seed48-r2', {})\nprint('=== eval-vla-only-object-seed48-r2 ===')\nprint(json.dumps(exp, indent=2))\n\"\n",
    "description": "Get full details of target experiment"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-20T14:56:19.404052+00:00_

=== eval-vla-only-object-seed48-r2 ===
{
  "status": "ANALYZING",
  "retry_count": 0,
  "created_at": "2026-05-20T13:08:11.387Z",
  "updated_at": "2026-05-20T14:53:19.813Z",
  "hypothesis": "VLA-only baseline on LIBERO-Object seed48 re-run. Prior run (sr=0.1) had process death issues. Redeploy for reliable VLA-only baseline data.",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode vla_only --benchmark object --seed 48 --n_rollouts 10 --K 1 --output_file logs/eval_vla_only_object_seed48.json 2>&1 | tee logs/eval-vla-only-object-seed48-r2.log\"",
    "server": "bjb1-32546",
    "gpu": [
      "cuda:4"
    ],
    "pid": "423884",
    "log_path": "~/runs/acr-vla-conformal-refinement/eval-vla-only-object-seed48-r2.log",
    "submitted_at": "2026-05-20T13:08:28.020Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root"
  },
  "reproduce": {
    "finished_at": "2026-05-20T14:53:14.771Z"
  },
  "extra": {
    "hook_events": [
      {
        "event": "on_complete",
        "action": "agent",
        "ts": "2026-05-20T14:53:44.084405+00:00"
      }
    ]
  }
}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-object-seed48-r2",
  "tool": "Bash",
  "elapsed_ms": 2717
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-20T14:56:20.040195+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-4dbb3434/89b94665-f857-4ec3-be68-7f7db8df7d27/tool-results/mcp-agent-ml-research-read_registry-1779288842627.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# All vla-only-object experiments for context\nprint('=== All vla-only-object experiments ===')\nfor eid, e in exps.items():\n    if 'vla-only-object' in eid:\n        print(f\\\"{eid}: status={e.get('status')}, conclusion={e.get('conclusion')}, metrics={e.get('metrics')}\\\")\n\"\n",
  "description": "List all vla-only-object experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-object-seed48-r2",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-4dbb3434/89b94665-f857-4ec3-be68-7f7db8df7d27/tool-results/mcp-agent-ml-research-read_registry-1779288842627.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# All vla-only-object experiments for context\nprint('=== All vla-only-object experiments ===')\nfor eid, e in exps.items():\n    if 'vla-only-object' in eid:\n        print(f\\\"{eid}: status={e.get('status')}, conclusion={e.get('conclusion')}, metrics={e.get('metrics')}\\\")\n\"\n",
    "description": "List all vla-only-object experiments"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-20T14:56:21.896627+00:00_

=== All vla-only-object experiments ===
eval-vla-only-object-seed48-r2: status=ANALYZING, conclusion=None, metrics=None
eval-vla-only-object-seed50: status=DONE, conclusion=success, metrics={'success_rate': 0.09, 'total_rollouts': 100, 'successes': 9, 'per_task': {'alphabet_soup': 0, 'cream_cheese': 0.1, 'salad_dressing': 0.1, 'bbq_sauce': 0.2, 'ketchup': 0, 'tomato_sauce': 0.1, 'butter': 0, 'milk': 0.1, 'chocolate_pudding': 0.1, 'orange_juice': 0.2}}
eval-vla-only-object-seed48: status=DONE, conclusion=success, metrics={'success_rate': 0.1, 'n_episodes': 100}
eval-vla-only-object-seed51: status=PREPARING, conclusion=None, metrics=None
eval-vla-only-object-seed49-r2: status=PREPARING, conclusion=None, metrics=None
eval-vla-only-object-seed49: status=DONE, conclusion=killed, metrics=None
eval-vla-only-object-seed47: status=DONE, conclusion=success, metrics={'overall_success_rate': 0.1, 'n_tasks': 10, 'n_rollouts': 10, 'total_episodes': 100, 'per_task': {'salad_dressing': 0.2, 'bbq_sauce': 0.2, 'milk': 0.2, 'chocolate_pudding': 0.2, 'orange_juice': 0.2, 'alphabet_soup': 0, 'cream_cheese': 0, 'ketchup': 0, 'tomato_sauce': 0, 'butter': 0}}
eval-vla-only-object-seed46: status=DONE, conclusion=success, metrics={'success_rate': 0.13, 'n_tasks': 10, 'n_rollouts': 10, 'total_rollouts': 100}
eval-vla-only-object-seed45-r2: status=DONE, conclusion=success, metrics={'overall_success_rate': 0.11, 'n_tasks': 10, 'n_rollouts_per_task': 10, 'total_rollouts': 100, 'per_task': {'alphabet_soup': 0, 'cream_cheese': 0.3, 'salad_dressing': 0.2, 'bbq_sauce': 0.2, 'ketchup': 0, 'tomato_sauce': 0.1, 'butter': 0, 'milk': 0, 'chocolate_pudding': 0.1, 'orange_juice': 0.2}}
eval-vla-only-object-seed45: status=DONE, conclusion=success, metrics={'overall_sr': 0.09, 'successes': 18, 'total': 200, 'tasks_done': 10}
eval-vla-only-object-seed43: status=DONE, conclusion=success, metrics={'overall_sr': 0.12, 'tasks_done': 10, 'tasks_total': 10, 'per_task_sr': {'alphabet_soup': 0, 'cream_cheese': 0.1, '
…[truncated 997 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-object-seed48-r2",
  "tool": "Bash",
  "elapsed_ms": 1856
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-20T14:56:22.047928+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-4dbb3434/89b94665-f857-4ec3-be68-7f7db8df7d27/tool-results/mcp-agent-ml-research-read_registry-1779288842627.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Also check eval-adaptive-k-spatial-p90-seed44 and eval-obs-only-object-norm02-seed50 (also ANALYZING)\nfor eid in ['eval-adaptive-k-spatial-p90-seed44', 'eval-obs-only-object-norm02-seed50']:\n    exp = exps.get(eid, {})\n    print(f'=== {eid} ===')\n    print(json.dumps(exp, indent=2))\n    print()\n\"\n",
  "description": "Get details of other ANALYZING experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-object-seed48-r2",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-4dbb3434/89b94665-f857-4ec3-be68-7f7db8df7d27/tool-results/mcp-agent-ml-research-read_registry-1779288842627.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Also check eval-adaptive-k-spatial-p90-seed44 and eval-obs-only-object-norm02-seed50 (also ANALYZING)\nfor eid in ['eval-adaptive-k-spatial-p90-seed44', 'eval-obs-only-object-norm02-seed50']:\n    exp = exps.get(eid, {})\n    print(f'=== {eid} ===')\n    print(json.dumps(exp, indent=2))\n    print()\n\"\n",
    "description": "Get details of other ANALYZING experiments"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-20T14:56:22.148838+00:00_

=== eval-adaptive-k-spatial-p90-seed44 ===
{
  "status": "RUNNING",
  "retry_count": 0,
  "created_at": "2026-05-20T13:06:33.103Z",
  "updated_at": "2026-05-20T13:50:08.589Z",
  "hypothesis": "Adaptive K with \u03c4=P90 (0.125870) on LIBERO-Spatial seed44. Third seed completing Spatial P90 cross-benchmark sweep.",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode adaptive_k --adaptive_threshold 0.125870 --k_full 10 --benchmark spatial --seed 44 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_adaptive_k_spatial_p90_seed44.json 2>&1 | tee logs/eval-adaptive-k-spatial-p90-seed44.log\"",
    "server": "bjb1-18228",
    "gpu": [
      "cuda:0"
    ],
    "pid": "384493",
    "log_path": "~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p90-seed44.log",
    "submitted_at": "2026-05-20T13:07:04.948Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root"
  }
}

=== eval-obs-only-object-norm02-seed50 ===
{
  "status": "ANALYZING",
  "retry_count": 0,
  "created_at": "2026-05-20T13:07:41.505Z",
  "updated_at": "2026-05-20T14:52:51.145Z",
  "hypothesis": "CRM obs_only (\u03b5=0.2) K=10 on LIBERO-Object seed50. Expanding Object CRM norm02 from n=7 to n=8 for seed balance.",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 50 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --outpu
…[truncated 668 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-object-seed48-r2",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-20T14:56:42.338948+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__get_worker_status,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__load_project_config",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-object-seed48-r2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__get_worker_status,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__load_project_config",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-20T14:56:42.390221+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-object-seed48-r2",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-20T14:56:47.759988+00:00_

called mcp__agent-ml-research__list_workers

<details open><summary>🔧 Tool call — mcp__agent-ml-research__list_workers</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "status": "running",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-object-seed48-r2",
  "tool": "mcp__agent-ml-research__list_workers",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "status": "running",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-20T14:56:47.911941+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [], \"count\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-object-seed48-r2",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 151
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-20T14:57:06.902866+00:00_

called mcp__agent-ml-research__spawn_worker

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker</summary>

```json
{
  "task_type": "analyze:eval-vla-only-object-seed48-r2",
  "project": "acr-vla-conformal-refinement",
  "task_prompt": "## 任务：分析实验 eval-vla-only-object-seed48-r2 结果\n\n实验已完成（进程正常退出），需要读取结果并更新 registry。\n\n### 实验信息\n- exp_id: eval-vla-only-object-seed48-r2\n- 类型: VLA-only baseline on LIBERO-Object seed48 (re-run)\n- 服务器: bjb1-32546\n- hypothesis: \"VLA-only baseline on LIBERO-Object seed48 re-run. Prior run (sr=0.1) had process death issues. Redeploy for reliable VLA-only baseline data.\"\n\n### 步骤\n\n1. SSH 到 bjb1-32546，读取结果文件：\n   - JSON 输出: `/root/acr-vla-conformal-refinement/logs/eval_vla_only_object_seed48.json`\n   - 日志文件尾部: `tail -50 ~/runs/acr-vla-conformal-refinement/eval-vla-only-object-seed48-r2.log`\n\n2. 从 JSON 文件提取：\n   - overall_success_rate (或 success_rate)\n   - per_task success rates\n   - total rollouts / successes count\n\n3. 用 `update_registry` 更新：\n   - field=\"metrics\", value={success_rate: X, total_rollouts: N, successes: N, per_task: {...}}\n   - field=\"conclusion\", value=\"success\"（只要实验正常跑完且有有效数据）\n   - field=\"spec\", value 补充 checkpoint_path=\"\" 和 log_path=\"~/runs/acr-vla-conformal-refinement/eval-vla-only-object-seed48-r2.log\"\n   注意：conclusion 必须在 metrics 之后设置\n\n4. 已有 VLA-only Object baseline 参考（用于验证数据合理性）：\n   - seed42: 0.12, seed43: 0.12, seed44: 0.10, seed45: 0.11, seed46: 0.13, seed47: 0.10, seed48(prior): 0.10, seed50: 0.09\n   - 预期范围: 0.08-0.14\n\n如果 JSON 文件不存在或为空，检查日志文件最后的输出，看是否有 success rate 信息。\n",
  "tool_groups": "['ssh', 'registry']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-object-seed48-r2",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "tool_args": {
    "task_type": "analyze:eval-vla-only-object-seed48-r2",
    "project": "acr-vla-conformal-refinement",
    "task_prompt": "## 任务：分析实验 eval-vla-only-object-seed48-r2 结果\n\n实验已完成（进程正常退出），需要读取结果并更新 registry。\n\n### 实验信息\n- exp_id: eval-vla-only-object-seed48-r2\n- 类型: VLA-only baseline on LIBERO-Object seed48 (re-run)\n- 服务器: bjb1-32546\n- hypothesis: \"VLA-only baseline on LIBERO-Object seed48 re-run. Prior run (sr=0.1) had process death issues. Redeploy for reliable VLA-only baseline data.\"\n\n### 步骤\n\n1. SSH 到 bjb1-32546，读取结果文件：\n   - JSON 输出: `/root/acr-vla-conformal-refinement/logs/eval_vla_only_object_seed48.json`\n   - 日志文件尾部: `tail -50 ~/runs/acr-vla-conformal-refinement/eval-vla-only-object-seed48-r2.log`\n\n2. 从 JSON 文件提取：\n   - overall_success_rate (或 success_rate)\n   - per_task success rates\n   - total rollouts / successes count\n\n3. 用 `update_registry` 更新：\n   - field=\"metrics\", value={success_rate: X, total_rollouts: N, successes: N, per_task: {...}}\n   - field=\"conclusion\", value=\"success\"（只要实验正常跑完且有有效数据）\n   - field=\"spec\", value 补充 checkpoint_path=\"\" 和 log_path=\"~/runs/acr-vla-conformal-refinement/eval-vla-only-object-seed48-r2.log\"\n   注意：conclusion 必须在 metrics 之后设置\n\n4. 已有 VLA-only Object baseline 参考（用于验证数据合理性）：\n   - seed42: 0.12, seed43: 0.12, seed44: 0.10, seed45: 0.11, seed46: 0.13, seed47: 0.10, seed48(prior): 0.10, seed50: 0.09\n   - 预期范围: 0.08-0.14\n\n如果 JSON 文件不存在或为空，检查日志文件最后的输出，看是否有 success rate 信息。\n",
    "tool_groups": "['ssh', 'registry']"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-20T14:57:13.092499+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_analyze_eval-vla-only-object-seed48-r2_20260520T145707\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_analyze_eval-vla-only-object-seed48-r2_20260520T145707.log\", \"setup_data\": {}, \"message\": \"Worker worker_analyze_eval-vla-only-object-seed48-r2_20260520T145707 started. Use get_worker_status('worker_analyze_eval-vla-only-object-seed48-r2_20260520T145707') to check progress.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-object-seed48-r2",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "elapsed_ms": 6189
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-20T14:57:13.246571+00:00_

called mcp__agent-ml-research__spawn_worker

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker</summary>

```json
{
  "task_type": "analyze:eval-obs-only-object-norm02-seed50",
  "project": "acr-vla-conformal-refinement",
  "task_prompt": "## 任务：分析实验 eval-obs-only-object-norm02-seed50 结果\n\n实验已完成（进程正常退出），需要读取结果并更新 registry。\n\n### 实验信息\n- exp_id: eval-obs-only-object-norm02-seed50\n- 类型: CRM obs_only (ε=0.2) K=10 on LIBERO-Object seed50\n- 服务器: bjb1-32546\n- hypothesis: \"CRM obs_only (ε=0.2) K=10 on LIBERO-Object seed50. Expanding Object CRM norm02 from n=7 to n=8 for seed balance.\"\n\n### 步骤\n\n1. SSH 到 bjb1-32546，读取结果文件：\n   - JSON 输出: `/root/acr-vla-conformal-refinement/logs/eval_obs_only_object_norm02_seed50.json`\n   - 日志文件尾部: `tail -50 ~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed50.log`\n\n2. 从 JSON 文件提取：\n   - overall_success_rate\n   - per_task success rates\n   - total rollouts / successes count\n   - 如果有 correction magnitude 等额外 metrics 也提取\n\n3. 用 `update_registry` 更新：\n   - field=\"metrics\", value={success_rate: X, total_rollouts: N, successes: N, per_task: {...}}\n   - field=\"conclusion\", value=\"success\"（只要实验正常跑完且有有效数据）\n   - field=\"spec\", value 补充 log_path=\"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed50.log\"\n   注意：conclusion 必须在 metrics 之后设置\n\n4. 已有 CRM obs_only Object norm02 参考（用于验证数据合理性）：\n   - 已有 n=7 平均 16.8%±1.8%\n   - 预期范围: 0.13-0.22\n\n如果 JSON 文件不存在或为空，检查日志文件最后的输出。\n",
  "tool_groups": "['ssh', 'registry']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-object-seed48-r2",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "tool_args": {
    "task_type": "analyze:eval-obs-only-object-norm02-seed50",
    "project": "acr-vla-conformal-refinement",
    "task_prompt": "## 任务：分析实验 eval-obs-only-object-norm02-seed50 结果\n\n实验已完成（进程正常退出），需要读取结果并更新 registry。\n\n### 实验信息\n- exp_id: eval-obs-only-object-norm02-seed50\n- 类型: CRM obs_only (ε=0.2) K=10 on LIBERO-Object seed50\n- 服务器: bjb1-32546\n- hypothesis: \"CRM obs_only (ε=0.2) K=10 on LIBERO-Object seed50. Expanding Object CRM norm02 from n=7 to n=8 for seed balance.\"\n\n### 步骤\n\n1. SSH 到 bjb1-32546，读取结果文件：\n   - JSON 输出: `/root/acr-vla-conformal-refinement/logs/eval_obs_only_object_norm02_seed50.json`\n   - 日志文件尾部: `tail -50 ~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed50.log`\n\n2. 从 JSON 文件提取：\n   - overall_success_rate\n   - per_task success rates\n   - total rollouts / successes count\n   - 如果有 correction magnitude 等额外 metrics 也提取\n\n3. 用 `update_registry` 更新：\n   - field=\"metrics\", value={success_rate: X, total_rollouts: N, successes: N, per_task: {...}}\n   - field=\"conclusion\", value=\"success\"（只要实验正常跑完且有有效数据）\n   - field=\"spec\", value 补充 log_path=\"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed50.log\"\n   注意：conclusion 必须在 metrics 之后设置\n\n4. 已有 CRM obs_only Object norm02 参考（用于验证数据合理性）：\n   - 已有 n=7 平均 16.8%±1.8%\n   - 预期范围: 0.13-0.22\n\n如果 JSON 文件不存在或为空，检查日志文件最后的输出。\n",
    "tool_groups": "['ssh', 'registry']"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-20T14:57:20.376557+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Worker of type 'analyze:eval-obs-only-object-norm02-seed50' is already active for project 'acr-vla-conformal-refinement'. worker_id=worker_analyze_eval-obs-only-object-norm02-seed50_20260520T145649\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-object-seed48-r2",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "elapsed_ms": 7129
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-20T14:57:20.529067+00:00_

called mcp__agent-ml-research__spawn_worker

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker</summary>

```json
{
  "task_type": "analyze:eval-adaptive-k-spatial-p90-seed44",
  "project": "acr-vla-conformal-refinement",
  "task_prompt": "## 任务：分析实验 eval-adaptive-k-spatial-p90-seed44 结果\n\n实验已完成（进程正常退出，cron reconcile 检测到 EXIT_CODE=0），需要读取结果并更新 registry。\n\n### 实验信息\n- exp_id: eval-adaptive-k-spatial-p90-seed44\n- 类型: Adaptive K with τ=P90 (0.125870) on LIBERO-Spatial seed44\n- 服务器: bjb1-18228\n- hypothesis: \"Adaptive K with τ=P90 (0.125870) on LIBERO-Spatial seed44. Third seed completing Spatial P90 cross-benchmark sweep.\"\n\n### 步骤\n\n1. SSH 到 bjb1-18228，读取结果文件：\n   - JSON 输出: `/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_spatial_p90_seed44.json`\n   - 日志文件尾部: `tail -50 ~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p90-seed44.log`\n\n2. 从 JSON 文件提取：\n   - overall_success_rate\n   - per_task success rates\n   - avg_K (平均使用的 K 值)\n   - fast_path_ratio (K=1 即 fast path 的比例)\n   - total rollouts / successes count\n\n3. 用 `update_registry` 更新：\n   - field=\"metrics\", value={success_rate: X, avg_K: Y, fast_path_ratio: Z, total_rollouts: N, successes: N, per_task: {...}}\n   - field=\"conclusion\", value=\"success\"（只要实验正常跑完且有有效数据）\n   - field=\"spec\", value 补充 log_path=\"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p90-seed44.log\"\n   注意：conclusion 必须在 metrics 之后设置\n\n4. 已有 Adaptive K Spatial P90 参考：\n   - Object P90 平均: SR 13.3%, avg_K ~2.6, fast_path ~93%\n   - Spatial P90 前两个 seed 可能已有数据，用于交叉验证\n\n如果 JSON 文件不存在或为空，检查日志文件最后的输出。\n",
  "tool_groups": "['ssh', 'registry']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-object-seed48-r2",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "tool_args": {
    "task_type": "analyze:eval-adaptive-k-spatial-p90-seed44",
    "project": "acr-vla-conformal-refinement",
    "task_prompt": "## 任务：分析实验 eval-adaptive-k-spatial-p90-seed44 结果\n\n实验已完成（进程正常退出，cron reconcile 检测到 EXIT_CODE=0），需要读取结果并更新 registry。\n\n### 实验信息\n- exp_id: eval-adaptive-k-spatial-p90-seed44\n- 类型: Adaptive K with τ=P90 (0.125870) on LIBERO-Spatial seed44\n- 服务器: bjb1-18228\n- hypothesis: \"Adaptive K with τ=P90 (0.125870) on LIBERO-Spatial seed44. Third seed completing Spatial P90 cross-benchmark sweep.\"\n\n### 步骤\n\n1. SSH 到 bjb1-18228，读取结果文件：\n   - JSON 输出: `/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_spatial_p90_seed44.json`\n   - 日志文件尾部: `tail -50 ~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p90-seed44.log`\n\n2. 从 JSON 文件提取：\n   - overall_success_rate\n   - per_task success rates\n   - avg_K (平均使用的 K 值)\n   - fast_path_ratio (K=1 即 fast path 的比例)\n   - total rollouts / successes count\n\n3. 用 `update_registry` 更新：\n   - field=\"metrics\", value={success_rate: X, avg_K: Y, fast_path_ratio: Z, total_rollouts: N, successes: N, per_task: {...}}\n   - field=\"conclusion\", value=\"success\"（只要实验正常跑完且有有效数据）\n   - field=\"spec\", value 补充 log_path=\"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p90-seed44.log\"\n   注意：conclusion 必须在 metrics 之后设置\n\n4. 已有 Adaptive K Spatial P90 参考：\n   - Object P90 平均: SR 13.3%, avg_K ~2.6, fast_path ~93%\n   - Spatial P90 前两个 seed 可能已有数据，用于交叉验证\n\n如果 JSON 文件不存在或为空，检查日志文件最后的输出。\n",
    "tool_groups": "['ssh', 'registry']"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-20T14:57:23.292470+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_analyze_eval-adaptive-k-spatial-p90-seed44_20260520T145720\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_analyze_eval-adaptive-k-spatial-p90-seed44_20260520T145720.log\", \"setup_data\": {}, \"message\": \"Worker worker_analyze_eval-adaptive-k-spatial-p90-seed44_20260520T145720 started. Use get_worker_status('worker_analyze_eval-adaptive-k-spatial-p90-seed44_20260520T145720') to check progress.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-object-seed48-r2",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "elapsed_ms": 2763
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-20T14:57:41.609460+00:00_

已派发 Worker：
- `eval-vla-only-object-seed48-r2` → 新 Worker 分析中
- `eval-obs-only-object-norm02-seed50` → 已有 Worker 在处理（前序 cron 已触发）
- `eval-adaptive-k-spatial-p90-seed44` → 新 Worker 分析中

当前还有 7 个实验 RUNNING（含 3 个 CRM K=1 plan702、perdof-object-norm02-seed49、argmin-object-seed50、obs-only-spatial-norm02-seed49、openvla-precompute-k1）。

等待 Worker 回调后更新 registry 并汇报 Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval-vla-only-object-seed48-r2"
}
```

</details>

---

## Round 2

2 recorded events

### User

_source line 37 · 2026-05-20T14:57:41.680901+00:00_

[CRON] 实验进程已正常退出，状态已转为 ANALYZING，需要你分析结果并推进到 DONE。
详情: Process exited cleanly, W&B data available

- exp_id: eval-vla-only-object-seed48-r2
- project: acr-vla-conformal-refinement
- server: bjb1-32546

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:eval-vla-only-object-seed48-r2",
  "source": "cron:hook"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-20T14:57:50.611844+00:00_

这个实验的分析 Worker 已经在运行中（`worker_analyze_eval-vla-only-object-seed48-r2_20260520T145707`），是上一轮 cron 回调时派发的。等 Worker 完成后会自动回调，无需重复处理。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval-vla-only-object-seed48-r2"
}
```

</details>

---

## Round 3

2 recorded events

### User

_source line 39 · 2026-05-21T07:02:13.028772+00:00_

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
  "session": "cron:hook:eval-vla-only-object-seed48-r2",
  "source": "system:ralph_loop"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-21T07:03:14.375950+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- GPU 白名单必须查 `load_project_config("acr-vla-conformal-refinement", section="execution")` 的 gpu_ids，不要假设
- CRM checkpoint 路径固定: `/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt`，所有 CRM eval 必须用这个
- evaluate.py 使用 batched inference（D082 已确认），附录延迟表需按此更新
- Object CRM Table 1 只用 norm02 数据（D080），不混入 norm01/norm03 的 seed
- seed42 的 CRM Object norm02 (SR=20%) 不纳入 Table 1（D084 决策，outlier）
- Long OOD 只能用 cautious wording（MW-U p=0.061 不显著，D081）

### 2. 🖥️ 基础设施快照
- **bjb1-18228**: 工作目录 `/root/acr-vla-conformal-refinement`，Python `/root/miniconda3/bin/python`，conda base。HF_HOME=/root/autodl-tmp/.hf_cache。磁盘 /autodl-pub 90% ⚠️
- **bjb1-32546**: 同上结构。磁盘健康（4% used）
- **bjb2-28827**: 同上结构。磁盘健康（5% used）。6 GPU 可用
- **bjb2-40593**: 磁盘 /nvidia-smi 89% ⚠️
- 所有服务器: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base` 激活环境，HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl
- 活跃进程（reconcile 时刻）:
  - eval-perdof-object-norm02-seed49: bjb1-32546 PID 450375
  - eval-argmin-object-seed50: bjb1-32546 PID 423622 cuda:3
  - eval-obs-only-spatial-norm02-seed49: bjb2-28827 PID 357304 cuda:2
  - eval-random-selection-object-seed43: bjb2-28827 PID 707407
  - eval-random-selection-object-seed45: bjb2-28827 PID 468175
  - eval-crm-k1-object-seed42/43/44-plan702: bjb2-28827 PID 401372/401666/402276 cuda:0/1/5
  - openvla-precompute-k1: bjb2-28827 cuda:3
  - eval-vla-only-goal-seed51: RUNNING（无 cron 注册，需要检查）

### 3. 📊 当前状态
本 session 刚启动，收到 cron 回调 eval-vla-only-object-seed48-r2 完成。Reconcile 还发现 eval-adaptive-k-spatial-p90-seed44 也完成（EXIT_CODE=0 → ANALYZING）。eval-obs-only-object-norm02-seed50 也处于 ANALYZING（已有 worker 在跑）。

**已派 Worker（等回调）:**
- `worker_analyze_eval-vla-only-object-seed48-r2_20260520T145707` — 分析 VLA-only Object seed48 r2
- `worker_analyze_eval-obs-only-object-norm02-seed50_20260520T145649` — 分析 CRM obs_only Object seed50（前 session 派的）
- `worker_analyze_eval-adaptive-k-spatial-p90-seed44_20260520T145720` — 分析 Adaptive K Spatial P90 seed44

**RUNNING (7):** eval-argmin-object-seed50, eval-obs-only-spatial-norm02-seed49, openvla-precompute-k1, eval-crm-k1-object-seed42/43/44-plan702, eval-perdof-object-norm02-seed49, eval-vla-only-goal-seed51

**PREPARING (~33):** 包括 Spatial Adaptive K seeds、更多 VLA-only baselines、OOD Goal seeds 等

**尚未向 Director 汇报本轮结果**——三个 Worker 都还在跑，等回调后再汇报。

### 4. 📋 待办（条件触发式）
- 3 个分析 Worker 回调到达 → 读 metrics、更新 report.md、向 Director 汇报（带 [资源] 行）
- eval-vla-only-object-seed48-r2 结果确认 → VLA-only Object baseline 扩展到 n=9（seed42-48,50），计算新的均值±std
- eval-obs-only-object-norm02-seed50 结果确认 → CRM Object norm02 从 n=7 扩到 n=8，更新 Table 1 统计
- eval-adaptive-k-spatial-p90-seed44 结果确认 → Spatial P90 三 seed 齐全，计算 cross-benchmark 迁移效果，与 Object P90 (SR 13.3%, avg_K ~2.6) 对比
- eval-crm-k1-object-seed42/43/44-plan702 完成 → CRM K=1 数据用于 correction vs selection decomposition
- eval-vla-only-goal-seed51 无 cron → 需要检查是否还在跑，可能需要手动注册 cron 或 SSH 检查
- GPU 释放后 → 从 PREPARING 队列中优先部署 Spatial Adaptive K P50 seeds（论文核心贡献）

### 5. 🎯 战略上下文
- **投稿目标: CoRL 2026，DDL 2026-05-29（~8天）**
- **核心贡献（D077）:** Adaptive K（K=2 L2 distance 信号，自适应推理次数）。K=10 分析降为 supporting evidence
- **P50 = Pareto 最优（D078）:** Object 上 SR 15.3%, avg_K ~3.8, fast_path ~77%, 保留 K=10 的 91% 性能
- **信号选择已 CLOSED:** K=2 L2 distance (ρ=0.9979) 是唯一可用信号，CRM magnitude (ρ=0.15) 和 FMVD (ρ=0.08) 都 NO-GO
- **Object CRM K=10 基准（D080）:** 16.8%±1.8% (n=6, norm02-only)，VLA-only ~10.9%，p=9.5e-5***
- **OOD 结果:** Goal neutral (-0.7pp n.s.)，Long marginal (+2.3pp, MW-U p=0.061 n.s.)，LTO catastrophic (-12pp)
- **易错点:** (1) seed42 CRM Object norm02 是 outlier (20%)，D084 决策不纳入 Table 1 (2) Adaptive K 阈值是从 Object 校准的，跨 benchmark 迁移到 Spatial 是关键验证——如果 Spatial P50 效果差，可能需要 per-benchmark 校准的 framing (3) eval-vla-only-goal-seed51 没有 cron，可能是孤儿进程 (4) 论文 CRITICAL 待解决：OOD 数据全量更新、附录延迟表更新、fig3_kvalue 重新生成
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval-vla-only-object-seed48-r2"
}
```

</details>

---
