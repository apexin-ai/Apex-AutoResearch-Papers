# cron hook eval supp adapt tau035 spatial s42 r2 20260523T222123 121505

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 3
- **Tool calls:** 11
- **Original source:** `logs/chats/archive/cron_hook_eval-supp-adapt-tau035-spatial-s42-r2_20260523T222123_121505.jsonl`
- **Structured JSON:** [`b02b4412f3a92dd695ee.json`](../../sessions/b0/b02b4412f3a92dd695ee.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

24 recorded events

### User

_source line 1 · 2026-05-23T06:17:16.736713+00:00_

[CRON] 实验进程已正常退出，状态已转为 ANALYZING，需要你分析结果并推进到 DONE。
详情: Process exited cleanly, W&B data available

- exp_id: eval-supp-adapt-tau035-spatial-s42-r2
- project: acr-vla-conformal-refinement
- server: bjb1-32546
- log_path: /root/acr-vla-conformal-refinement/logs/eval-supp-adapt-tau035-spatial-s42-r2.log

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:eval-supp-adapt-tau035-spatial-s42-r2",
  "source": "cron:hook"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-23T06:17:31.845545+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__read_experiment_plan_with_status,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__load_project_config,mcp__agent-ml-research__get_worker_status,mcp__agent-ml-research__list_workers",
  "max_results": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-supp-adapt-tau035-spatial-s42-r2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__read_experiment_plan_with_status,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__load_project_config,mcp__agent-ml-research__get_worker_status,mcp__agent-ml-research__list_workers",
    "max_results": "15"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-23T06:17:31.901352+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-supp-adapt-tau035-spatial-s42-r2",
  "tool": "ToolSearch",
  "elapsed_ms": 55
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-23T06:17:37.578483+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "fields": "['*']",
  "limit": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-supp-adapt-tau035-spatial-s42-r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "fields": "['*']",
    "limit": "0"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T06:17:38.116642+00:00_

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
  "session": "cron:hook:eval-supp-adapt-tau035-spatial-s42-r2",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-23T06:17:38.566495+00:00_

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
  "session": "cron:hook:eval-supp-adapt-tau035-spatial-s42-r2",
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

_source line 7 · 2026-05-23T06:17:38.987676+00:00_

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
  "session": "cron:hook:eval-supp-adapt-tau035-spatial-s42-r2",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T06:17:42.007455+00:00_

Error: result (1,058,723 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-786353b3/24d7b21e-b85b-40a2-bb81-39b2333b738b/tool-results/mcp-agent-ml-research-read_registry-1779517061611.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-786353b3/24d7b21e-b85b-40a2-bb81-39b2333b738b/tool-results/mcp-agent-ml-research-read_registry-1779517061611.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-786353b3/24d7b21e-b85b-40a2-bb81-39b2333b738b/tool-results/mcp-agent-ml-research-read_registry-1779517061611.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-supp-adapt-tau035-spatial-s42-r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 4428
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-23T06:18:34.208724+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 11, \"results\": [{\"exp_id\": \"eval-supp-obj-crm005-s42-r2\", \"success\": true, \"actions\": [\"Job still running (pid=669419)\"]}, {\"exp_id\": \"eval-supp-obj-adapt-s42-r2\", \"success\": true, \"actions\": [\"Job still running (pid=522259)\"]}, {\"exp_id\": \"eval-supp-obj-reconvla-s42\", \"success\": true, \"actions\": [\"Job still running (pid=523238)\"]}, {\"exp_id\": \"eval-supp-goal-crm005-s42\", \"success\": true, \"actions\": [\"Job still running (pid=524322)\"]}, {\"exp_id\": \"eval-object-vla-only-wrapper-s42-r2\", \"success\": true, \"actions\": [\"Job still running (pid=519749)\"]}, {\"exp_id\": \"eval-object-vla-only-wrapper-s43-r2\", \"success\": true, \"actions\": [\"Job still running (pid=520493)\"]}, {\"exp_id\": \"eval-object-vla-only-wrapper-s44-r2\", \"success\": true, \"actions\": [\"Job still running (pid=521785)\"]}, {\"exp_id\": \"precompute-pi05-object-2048-r2\", \"success\": true, \"actions\": [\"Job still running (pid=113456)\"]}, {\"exp_id\": \"precompute-pi05-spatial-2048-r2\", \"success\": true, \"actions\": [\"Job still running (pid=113796)\"]}, {\"exp_id\": \"precompute-pi05-goal-2048-r2\", \"success\": true, \"actions\": [\"Job still running (pid=114159)\"]}, {\"exp_id\": \"precompute-pi05-long-2048-r2\", \"success\": true, \"actions\": [\"Job still running (pid=114507)\"]}]}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-supp-adapt-tau035-spatial-s42-r2",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 56092
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T06:18:34.259961+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-23T06:17:13Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 760 个实验 — ALLOCATED 1, ANALYZING 1, DEPLOYED 5, DONE 647, PENDING 1, PREPARING 96, QUEUED 1, RUNNING 8\\n**DONE 分布**: failed 82, killed 149, negative 49, success 367\\n\\n### GPU 占用\\n- **实际运行**: 8 张 — bjb2-28827:cuda:3(eval-object-vla-only-wrapper-s42-r2), bjb2-28827:cuda:4(eval-object-vla-only-wrapper-s43-r2), bjb1-32546:cuda:3(train-crm-unified-4suite-r6), bjb2-28827:cuda:5(eval-object-vla-only-wrapper-s44-r2), bjb1-32546:cuda:5(eval-supp-obj-crm005-s42-r2), bjb2-28827:cuda:0(eval-supp-obj-adapt-s42-r2), bjb2-28827:cuda:1(eval-supp-obj-reconvla-s42), bjb2-28827:cuda:2(eval-supp-goal-crm005-s42)\\n\\n### 💾 磁盘余量\\n- **bjb2-40593**:\\n  - `/init`: 150M/150M 可用（已用 0%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 45G/437G 可用（已用 90%） ⚠️\\n- **bjb1-18228**:\\n  - `/autodl-pub`: 356G/7.0T 可用（已用 96%） ⚠️\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 400G/438G 可用（已用 4%）\\n- **bjb1-32546**:\\n  - `/autodl-pub`: 1.1T/7.0T 可用（已用 86%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 400G/438G 可用（已用 4%）\\n- **bjb2-28827**:\\n  - `/autodl-pub`: 4.4T/14T 可用（已用 69%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 399G/439G 可用（已用 5%）\\n\\n### 🏃 RUNNING\\n| exp_id | server | gpu | pid | log |\\n|--------|--------|-----|-----|-----|\\n| `eval-object-vla-only-wrapper-s42-r2` | bjb2-28827 | cuda:3 | 519749 | `…onformal-refinement/eval-object-vla-only-wrapper-s42-r2.log` |\\n| `eval-object-vla-only-wrapper-s43-r2` | bjb2-28827 | cuda:4 | 520493 | `…onformal-refinement/eval-object-vla-only-wrapper-s43-r2.log` |\\n| `train-crm-unified-4suite-r6` | bjb1
…[truncated 8580 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-supp-adapt-tau035-spatial-s42-r2",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 55693
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-23T06:18:34.260743+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-23 03:58 UTC | 更新原因: 修正 GPU 实际状态 + 提升 multi-seed 为 P0 + 修正 π0.5 framing\\n\\n> 详见 paper_framing.md（最高权限叙述逻辑 + D077→D119）\\n\\n## 核心方向\\n**ACR-VLA: Adaptive Conformal Refinement for Frozen Flow-Matching VLAs** — CRM + Adaptive K 作为核心方法贡献。**Method paper 定位**。\\n\\n## 投稿目标\\n**CoRL 2026** DDL **2026-05-29**。剩余 **≤6 天**。时间线可行（Reviewer 确认）。\\n\\n## 已确认核心结果 — Spatial Seed42 方法对比 ✅\\n| Mode | K | norm | SR | vs VLA-only |\\n|------|---|------|----|-------------|\\n| VLA-only (wrapper) | 1 | — | 78.5% | baseline |\\n| CRM norm=0.1 | 10 | 0.1 | 79.0% | +0.5pp |\\n| CRM norm=0.05 | 10 | 0.05 | 80.0% | +1.5pp |\\n| **Adaptive CRM** | **2** | **0.2** | **81.0%** | **+2.5pp** |\\n| Reconvla K=10 | 10 | — | 79.0% | +0.5pp |\\n\\n⚠️ **单 seed 统计力不足**：200 trials 上 +2.5pp ≈ 0.86σ，multi-seed 是 P0。\\n\\n## SmolVLA VLA-only Wrapper Baseline (Spatial)\\n| Seed | SR |\\n|------|----|\\n| 42 | 78.5% |\\n| 43 | 80.5% |\\n| 44 | 80.5% |\\n| **Mean** | **79.8%±1.2%** |\\n\\n## π0.5 Baseline ✅ COMPLETE（94-99% 饱和，仅适合 no-harm 验证）\\n| Suite | Mean |\\n|-------|------|\\n| Object | 99.3%±0.8% |\\n| Spatial | 98.0%±0.5% |\\n| Goal | 97.8%±0.3% |\\n| Long | 95.0%±0.9% |\\n\\n## 🟢 RUNNING — 当前 GPU 状态\\n### bjb1-32546 (6×4090) — 6/6 占用\\n| GPU | 实验 | 优先级 | 备注 |\\n|-----|------|--------|------|\\n| cuda:0 | CRM norm=0.2 always-on Spatial s42 | P0 | 隔离 gating 贡献 |\\n| cuda:1 | Adaptive tau=0.15 Spatial s42 | P0 | threshold sweep |\\n| cuda:2 | Adaptive tau=0.25 Spatial s42 | P0 | threshold sweep |\\n| cuda:4 | Adaptive tau=0.35 Spatial s42 | P0 | threshold sweep |\\n| cuda:3 | 4-suite CRM 训练 (epoch ~38/50) | P1 | registry 路径待修复 |\\n| cuda:5 | Object CRM norm=0.05 s42 | P1 | n_action_steps=10 |\\n\\n### bjb2-28827 (6×4090) — 6/6 占用\\n| GPU | 实验 | 优先级 | 备注 |\\n|-----|
…[truncated 2696 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-supp-adapt-tau035-spatial-s42-r2",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 55273
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-23T06:18:40.032581+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'exp_id': 'eval-supp-adapt-tau035-spatial-s42-r2'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-supp-adapt-tau035-spatial-s42-r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'exp_id': 'eval-supp-adapt-tau035-spatial-s42-r2'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T06:18:40.384153+00:00_

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
  "session": "cron:hook:eval-supp-adapt-tau035-spatial-s42-r2",
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

_source line 14 · 2026-05-23T06:18:41.741428+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.7007}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-supp-adapt-tau035-spatial-s42-r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1708
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-23T06:18:41.892568+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [], \"count\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-supp-adapt-tau035-spatial-s42-r2",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 1508
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-23T06:18:48.733460+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml | python3 -c \"\nimport sys, yaml\ndata = yaml.safe_load(sys.stdin)\nfor exp in data.get('experiments', []):\n    if exp.get('exp_id') == 'eval-supp-adapt-tau035-spatial-s42-r2':\n        import json\n        print(json.dumps(exp, indent=2, default=str))\n        break\nelse:\n    print('NOT FOUND')\n\"",
  "description": "Search registry.yaml for the specific experiment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-supp-adapt-tau035-spatial-s42-r2",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml | python3 -c \"\nimport sys, yaml\ndata = yaml.safe_load(sys.stdin)\nfor exp in data.get('experiments', []):\n    if exp.get('exp_id') == 'eval-supp-adapt-tau035-spatial-s42-r2':\n        import json\n        print(json.dumps(exp, indent=2, default=str))\n        break\nelse:\n    print('NOT FOUND')\n\"",
    "description": "Search registry.yaml for the specific experiment"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-23T06:18:50.754984+00:00_

Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 5, in &lt;module>
    if exp.get('exp_id') == 'eval-supp-adapt-tau035-spatial-s42-r2':
       ^^^^^^^
AttributeError: 'str' object has no attribute 'get'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-supp-adapt-tau035-spatial-s42-r2",
  "tool": "Bash",
  "elapsed_ms": 2021
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-23T06:18:56.929139+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport yaml, json\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml') as f:\n    data = yaml.safe_load(f)\n# Check structure\nif isinstance(data, dict):\n    exps = data.get('experiments', data)\n    if isinstance(exps, dict):\n        exp = exps.get('eval-supp-adapt-tau035-spatial-s42-r2')\n        if exp:\n            print(json.dumps(exp, indent=2, default=str))\n        else:\n            # search keys containing the substring\n            matches = [k for k in exps.keys() if 'tau035' in k or 'tau0.35' in k]\n            print('No exact match. Keys with tau035:', matches)\n            matches2 = [k for k in exps.keys() if 'adapt' in k and 'spatial' in k and 'r2' in k]\n            print('Keys with adapt+spatial+r2:', matches2)\n\"\n",
  "description": "Parse registry YAML to find the experiment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-supp-adapt-tau035-spatial-s42-r2",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport yaml, json\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml') as f:\n    data = yaml.safe_load(f)\n# Check structure\nif isinstance(data, dict):\n    exps = data.get('experiments', data)\n    if isinstance(exps, dict):\n        exp = exps.get('eval-supp-adapt-tau035-spatial-s42-r2')\n        if exp:\n            print(json.dumps(exp, indent=2, default=str))\n        else:\n            # search keys containing the substring\n            matches = [k for k in exps.keys() if 'tau035' in k or 'tau0.35' in k]\n            print('No exact match. Keys with tau035:', matches)\n            matches2 = [k for k in exps.keys() if 'adapt' in k and 'spatial' in k and 'r2' in k]\n            print('Keys with adapt+spatial+r2:', matches2)\n\"\n",
    "description": "Parse registry YAML to find the experiment"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-23T06:18:58.638544+00:00_

{
  "status": "ANALYZING",
  "retry_count": 0,
  "created_at": "2026-05-23T04:11:54.911Z",
  "updated_at": "2026-05-23T06:16:56.728Z",
  "spec": {
    "command": "evaluate.py --mode adaptive_conformal_crm --conformal_threshold 0.35",
    "server": "bjb1-32546",
    "gpu": "cuda:4",
    "pid": 667018,
    "log_path": "~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau035-spatial-s42-r2.log",
    "submitted_at": "2026-05-23T04:11:49.182Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "/root/acr-vla-conformal-refinement",
    "data_count": 200,
    "model_name": "smolvla",
    "seed": 42,
    "checkpoint_source": "/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt",
    "eval_data": "LIBERO-Spatial"
  },
  "hypothesis": "Adaptive CRM with tau=0.35 (conservative, ~10% trigger rate) tests whether very selective CRM application still provides benefit on LIBERO-Spatial",
  "parent": "eval-3dir-adaptive-spatial-s42",
  "reproduce": {
    "finished_at": "2026-05-23T06:16:49.605Z"
  },
  "extra": {
    "hook_events": [
      {
        "event": "on_complete",
        "action": "agent",
        "ts": "2026-05-23T06:17:16.809341+00:00"
      }
    ]
  }
}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-supp-adapt-tau035-spatial-s42-r2",
  "tool": "Bash",
  "elapsed_ms": 1709
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-23T06:19:09.079788+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport yaml, json\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml') as f:\n    data = yaml.safe_load(f)\nexps = data.get('experiments', data)\n\n# Find all tau sweep and related experiments\nkeys_of_interest = []\nfor k, v in exps.items():\n    if any(x in k for x in ['adapt-tau', 'adaptive', '3dir-adaptive', 'supp-crm-norm', 'supp-adapt']):\n        if 'spatial' in k and 's42' in k:\n            keys_of_interest.append(k)\n\nfor k in sorted(keys_of_interest):\n    v = exps[k]\n    status = v.get('status', '?')\n    conclusion = v.get('conclusion', '')\n    metrics = v.get('metrics', {})\n    print(f'{k}: status={status} conclusion={conclusion} metrics={json.dumps(metrics, default=str)}')\n\"\n",
  "description": "Find all related tau sweep experiments for comparison"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-supp-adapt-tau035-spatial-s42-r2",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport yaml, json\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml') as f:\n    data = yaml.safe_load(f)\nexps = data.get('experiments', data)\n\n# Find all tau sweep and related experiments\nkeys_of_interest = []\nfor k, v in exps.items():\n    if any(x in k for x in ['adapt-tau', 'adaptive', '3dir-adaptive', 'supp-crm-norm', 'supp-adapt']):\n        if 'spatial' in k and 's42' in k:\n            keys_of_interest.append(k)\n\nfor k in sorted(keys_of_interest):\n    v = exps[k]\n    status = v.get('status', '?')\n    conclusion = v.get('conclusion', '')\n    metrics = v.get('metrics', {})\n    print(f'{k}: status={status} conclusion={conclusion} metrics={json.dumps(metrics, default=str)}')\n\"\n",
    "description": "Find all related tau sweep experiments for comparison"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-23T06:19:10.785882+00:00_

eval-3dir-adaptive-spatial-s42: status=DONE conclusion=success metrics={"success_rate": 81, "successes": 162, "total": 200, "n_tasks": 10, "n_rollouts": 20, "trigger_rate": 0.918, "tau": 0.074855, "mean_uncertainty": 0.183, "crm_applied_steps": 26589, "total_steps": 28955, "per_task_sr": {"between_plate_and_ramekin": 0.95, "next_to_ramekin": 1, "from_table_center": 1, "on_cookie_box": 0.9, "in_top_drawer": 0.8, "on_ramekin": 0, "next_to_cookie_box": 1, "on_stove": 0.9, "next_to_plate": 0.75, "on_wooden_cabinet": 0.8}}
eval-adaptive-tau015-spatial-s42: status=DONE conclusion=killed metrics={}
eval-adaptive-tau025-spatial-s42: status=DONE conclusion=killed metrics={}
eval-adaptive-tau035-spatial-s42: status=DONE conclusion=killed metrics={}
eval-supp-adapt-tau015-spatial-s42: status=DONE conclusion=killed metrics={}
eval-supp-adapt-tau015-spatial-s42-r2: status=DONE conclusion=success metrics={"overall_sr": 80.5, "n_success": 161, "n_total": 200, "trigger_rate": 40.7, "mean_unc": 0.1852, "conformal_threshold": 0.15, "max_correction_norm": 0.2, "per_task_sr": {"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate": 100, "pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate": 90, "pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate": 95, "pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate": 95, "pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate": 75, "pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate": 0, "pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate": 95, "pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate": 90, "pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate": 80, "pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate": 85}}
eval-supp-adapt-tau025-spatial-s42: status=DONE conclusion=killed metrics={}
eval-supp-adapt-tau025-spatial-s42-r2: status=DONE conclusion=succe
…[truncated 959 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-supp-adapt-tau035-spatial-s42-r2",
  "tool": "Bash",
  "elapsed_ms": 1706
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-23T06:19:39.963441+00:00_

called mcp__agent-ml-research__spawn_worker

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker</summary>

```json
{
  "task_type": "analyze:eval-supp-adapt-tau035-spatial-s42-r2",
  "project": "acr-vla-conformal-refinement",
  "task_prompt": "## 任务：分析已完成的 eval 实验日志，提取 metrics\n\n### 实验信息\n- exp_id: eval-supp-adapt-tau035-spatial-s42-r2\n- server: bjb1-32546\n- log_path: /root/acr-vla-conformal-refinement/logs/eval-supp-adapt-tau035-spatial-s42-r2.log\n- 备选 log 路径: ~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau035-spatial-s42-r2.log\n- 模式: adaptive_conformal_crm, conformal_threshold=0.35\n- 数据: LIBERO-Spatial, 200 trials (10 tasks × 20 rollouts), seed=42\n\n### 需要提取的 metrics\n1. overall_sr (总成功率，百分比)\n2. n_success / n_total\n3. trigger_rate (CRM 被触发的比例，百分比)\n4. mean_unc (平均 uncertainty)\n5. conformal_threshold (确认是 0.35)\n6. max_correction_norm\n7. per_task_sr (每个 task 的成功率)\n8. crm_applied_steps / total_steps (如果有)\n\n### 操作步骤\n1. SSH 到 bjb1-32546，读取 log 文件（先试第一个路径，不存在就试第二个）\n2. 从 log 尾部提取最终 evaluation summary\n3. 提取上述所有 metrics\n4. 用 update_registry 更新：\n   - field=metrics, value={提取的 metrics dict}\n   - field=conclusion, value=根据结果判断：\n     - SR ≥ 78.5% (VLA-only baseline) → \"success\"\n     - SR < 78.5% → \"negative\"\n   - field=status, value=DONE\n   - spec 补充: checkpoint_path 和 log_path（用实际路径）\n\n### 对比参考（用于判断 conclusion）\n- VLA-only baseline: 78.5%\n- Adaptive tau=default (0.075): 81.0%, trigger_rate=91.8%\n- Adaptive tau=0.15: 80.5%, trigger_rate=40.7%\n- Adaptive tau=0.25: 82.0%, trigger_rate=19.4%\n- CRM norm=0.2 always-on: 79.0%\n\n### 注意\n- 用 ssh_read_only 读 log，不要用 ssh_execute\n- 确保提取的数字准确，不要猜测\n- per_task_sr 用短名称（如 \"between_plate_and_ramekin\" 而非完整 task 描述）\n",
  "tool_groups": "['ssh', 'registry']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-supp-adapt-tau035-spatial-s42-r2",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "tool_args": {
    "task_type": "analyze:eval-supp-adapt-tau035-spatial-s42-r2",
    "project": "acr-vla-conformal-refinement",
    "task_prompt": "## 任务：分析已完成的 eval 实验日志，提取 metrics\n\n### 实验信息\n- exp_id: eval-supp-adapt-tau035-spatial-s42-r2\n- server: bjb1-32546\n- log_path: /root/acr-vla-conformal-refinement/logs/eval-supp-adapt-tau035-spatial-s42-r2.log\n- 备选 log 路径: ~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau035-spatial-s42-r2.log\n- 模式: adaptive_conformal_crm, conformal_threshold=0.35\n- 数据: LIBERO-Spatial, 200 trials (10 tasks × 20 rollouts), seed=42\n\n### 需要提取的 metrics\n1. overall_sr (总成功率，百分比)\n2. n_success / n_total\n3. trigger_rate (CRM 被触发的比例，百分比)\n4. mean_unc (平均 uncertainty)\n5. conformal_threshold (确认是 0.35)\n6. max_correction_norm\n7. per_task_sr (每个 task 的成功率)\n8. crm_applied_steps / total_steps (如果有)\n\n### 操作步骤\n1. SSH 到 bjb1-32546，读取 log 文件（先试第一个路径，不存在就试第二个）\n2. 从 log 尾部提取最终 evaluation summary\n3. 提取上述所有 metrics\n4. 用 update_registry 更新：\n   - field=metrics, value={提取的 metrics dict}\n   - field=conclusion, value=根据结果判断：\n     - SR ≥ 78.5% (VLA-only baseline) → \"success\"\n     - SR < 78.5% → \"negative\"\n   - field=status, value=DONE\n   - spec 补充: checkpoint_path 和 log_path（用实际路径）\n\n### 对比参考（用于判断 conclusion）\n- VLA-only baseline: 78.5%\n- Adaptive tau=default (0.075): 81.0%, trigger_rate=91.8%\n- Adaptive tau=0.15: 80.5%, trigger_rate=40.7%\n- Adaptive tau=0.25: 82.0%, trigger_rate=19.4%\n- CRM norm=0.2 always-on: 79.0%\n\n### 注意\n- 用 ssh_read_only 读 log，不要用 ssh_execute\n- 确保提取的数字准确，不要猜测\n- per_task_sr 用短名称（如 \"between_plate_and_ramekin\" 而非完整 task 描述）\n",
    "tool_groups": "['ssh', 'registry']"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-23T06:19:43.240784+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_analyze_eval-supp-adapt-tau035-spatial-s42-r2_20260523T061940\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_analyze_eval-supp-adapt-tau035-spatial-s42-r2_20260523T061940.log\", \"setup_data\": {}, \"message\": \"Worker worker_analyze_eval-supp-adapt-tau035-spatial-s42-r2_20260523T061940 started. Use get_worker_status('worker_analyze_eval-supp-adapt-tau035-spatial-s42-r2_20260523T061940') to check progress.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-supp-adapt-tau035-spatial-s42-r2",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "elapsed_ms": 3277
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-23T06:19:49.526379+00:00_

Worker 已派发分析 eval-supp-adapt-tau035-spatial-s42-r2 日志。当前状态：

- **11 个 cron 活跃**：8 个 eval 实验 RUNNING + 3 个 π0.5 precompute RUNNING
- **0 个 Worker 在跑**（刚派了 1 个分析 Worker）
- 目标实验是 threshold sweep 最后一个点（tau=0.35），完成后 Pareto 曲线数据齐全

等待 Worker 回调后继续处理。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval-supp-adapt-tau035-spatial-s42-r2"
}
```

</details>

---

## Round 2

2 recorded events

### User

_source line 25 · 2026-05-23T06:19:49.539551+00:00_

[CRON] 实验进程已正常退出，状态已转为 ANALYZING，需要你分析结果并推进到 DONE。
详情: Process exited cleanly, W&B data available

- exp_id: eval-supp-adapt-tau035-spatial-s42-r2
- project: acr-vla-conformal-refinement
- server: bjb1-32546
- log_path: /root/acr-vla-conformal-refinement/logs/eval-supp-adapt-tau035-spatial-s42-r2.log

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:eval-supp-adapt-tau035-spatial-s42-r2",
  "source": "cron:hook"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-23T06:19:57.113692+00:00_

已有 Worker `worker_analyze_eval-supp-adapt-tau035-spatial-s42-r2_20260523T061940` 正在分析此实验，无需重复处理。等待 Worker 回调。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval-supp-adapt-tau035-spatial-s42-r2"
}
```

</details>

---

## Round 3

2 recorded events

### User

_source line 27 · 2026-05-23T22:20:26.725512+00:00_

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
  "session": "cron:hook:eval-supp-adapt-tau035-spatial-s42-r2",
  "source": "system:ralph_loop"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-23T22:21:23.119732+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- GPU 白名单：bjb1-32546 cuda:0-5, bjb2-28827 cuda:0-5, bjb1-18228 cuda:0-3。bjb2-40593 磁盘满，excluded
- n_action_steps 必须一致：Object suite 用 10（之前 n_action_steps=50 导致 SR~51.8% 不可比，决策 M063）
- π0.5 baseline 已饱和（94-99%），只做 no-harm 验证，不要当 cross-model generalization claim
- Worker 两次假报部署成功（M065），Worker 完成后必须 SSH 验证进程实际在跑
- CRM checkpoint 路径：SmolVLA 3-suite → `/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt`

### 2. 🖥️ 基础设施快照
- **bjb1-32546** (6×4090)：工作目录 `/root/acr-vla-conformal-refinement`，Python `/root/miniconda3/bin/python`，conda base 环境
  - 活跃：train-crm-unified-4suite-r6 (PID 668372, cuda:3), eval-supp-obj-crm005-s42-r2 (PID 669419, cuda:5)
  - cuda:0/1/2/4 刚释放（threshold sweep tau=0.15/0.25/0.35 + CRM norm=0.2 always-on 已完成）
- **bjb2-28827** (6×4090)：同上结构
  - 活跃：eval-object-vla-only-wrapper s42/s43/s44 (PID 519749/520493/521785, cuda:3/4/5), eval-supp-obj-adapt-s42-r2 (PID 522259, cuda:0), eval-supp-obj-reconvla-s42 (PID 523238, cuda:1), eval-supp-goal-crm005-s42 (PID 524322, cuda:2)
- **bjb1-18228** (4×4090)：π0.5 precompute 2048D (object/spatial/goal/long), PID 113456/113796/114159/114507, cuda:0-3，预计剩余 26-32h
- W&B entity/project：需从 project config 确认
- HF cache：`/root/autodl-tmp/.hf_cache`（AutoDL 实例）

### 3. 📊 当前状态
**刚做完**：收到 eval-supp-adapt-tau035-spatial-s42-r2 (Adaptive tau=0.35 Spatial s42) 的 CRON 完成回调，已 spawn Worker 分析日志提取 metrics，Worker 尚未回调。

**RUNNING 实验**（11个）：
- train-crm-unified-4suite-r6：4-suite CRM 训练 (epoch ~38/50)，bjb1-32546 cuda:3
- eval-object-vla-only-wrapper s42/s43/s44：Object VLA-only 3-seed baseline，bjb2-28827 cuda:3/4/5
- eval-supp-obj-crm005-s42-r2：Object CRM norm=0.05，bjb1-32546 cuda:5
- eval-supp-obj-adapt-s42-r2：Object Adaptive CRM，bjb2-28827 cuda:0
- eval-supp-obj-reconvla-s42：Object Reconvla K=10，bjb2-28827 cuda:1
- eval-supp-goal-crm005-s42：Goal CRM norm=0.05，bjb2-28827 cuda:2
- precompute-pi05-{object,spatial,goal,long}-2048-r2：π0.5 precompute，bjb1-18228 cuda:0-3

**等待中**：
- Worker `worker_analyze_eval-supp-adapt-tau035-spatial-s42-r2_20260523T061940` 回调（分析 tau=0.35 日志）
- bjb1-32546 cuda:0/1/2/4 已空闲，等 tau=0.35 分析完成后即可部署 Spatial multi-seed (s43/s44)

### 4. 📋 待办（条件触发式）
- Worker 分析 tau=0.35 回调到达 → 更新 registry 到 DONE → 汇总 threshold sweep Pareto 曲线 → 向 Director 汇报完整 sweep 结果 + 推荐最优 tau
- Threshold sweep 全部完成（tau=0.15/0.25/0.35 + always-on 已有结果） → **立即用 bjb1-32546 空闲 GPU (cuda:0/1/2/4) 部署 Spatial multi-seed**：Adaptive CRM s43 + Adaptive CRM s44 + CRM norm=0.05 s43 + CRM norm=0.05 s44（或 Reconvla s43/s44），这是 P0
- Object VLA-only 3-seed 完成 → 建立 Object baseline mean±std → 对比 Object cross-suite 方法结果
- eval-supp-obj-adapt/reconvla/crm005 完成 → 更新 Object 方法对比表
- 4-suite CRM 训练完成 → 决定是否跑 4-suite eval
- π0.5 precompute 完成（~26-32h后） → CRM 训练 → no-harm eval

### 5. 🎯 战略上下文
- **投稿目标**：CoRL 2026，DDL 2026-05-29，剩余 ≤6 天
- **核心方法**：ACR-VLA = CRM (Conformal Refinement Module) + Adaptive K (uncertainty-gated selective correction)。Method paper 定位
- **关键发现**：Adaptive tau=0.25 目前最优（SR=82.0%, trigger_rate=19.4%），比 always-on (91.8% trigger) 更好——选择性修正优于全量修正
- **Threshold sweep Pareto 趋势**（Spatial s42）：
  - tau=0.075 (default): SR=81.0%, trigger=91.8%
  - tau=0.15: SR=80.5%, trigger=40.7%
  - tau=0.25: SR=82.0%, trigger=19.4% ← 当前最优
  - tau=0.35: ANALYZING（等 Worker 回调）
  - CRM always-on norm=0.2: SR=79.0%
- **单 seed 统计力不足**（+2.5pp ≈ 0.86σ on 200 trials），multi-seed 是 P0 优先级
- **易错点**：
  1. 不要混淆 SmolVLA precompute 数据 (960D) 和 π0.5 precompute (2048D)——D125 确认 crm_cache_v5 是 SmolVLA 数据
  2. Registry 有 7 个未注册/误标进程（M064/M065），部署前先 reconcile
  3. submit_on_allocated 的命令必须自带环境激活 `source /root/miniconda3/bin/activate && python ...`
  4. 决策链关键节点：D128 (overcorrection magnitude 非方向错误) → D127 (CRM always-correct negative → 3方向改进) → D119 (lerobot 官方 repo 修改)
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval-supp-adapt-tau035-spatial-s42-r2"
}
```

</details>

---
