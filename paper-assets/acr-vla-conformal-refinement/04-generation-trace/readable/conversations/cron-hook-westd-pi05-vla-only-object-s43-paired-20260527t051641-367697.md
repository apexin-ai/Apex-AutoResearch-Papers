# cron hook westd pi05 vla only object s43 paired 20260527T051641 367697

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 4
- **Tool calls:** 12
- **Original source:** `logs/chats/archive/cron_hook_westd-pi05-vla-only-object-s43-paired_20260527T051641_367697.jsonl`
- **Structured JSON:** [`28b3b1e87af9800273dd.json`](../../sessions/28/28b3b1e87af9800273dd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

26 recorded events

### User

_source line 1 · 2026-05-26T11:46:50.691741+00:00_

[CRON] 实验进程已正常退出，状态已转为 ANALYZING，需要你分析结果并推进到 DONE。
详情: Process exited cleanly, W&B data available

- exp_id: westd-pi05-vla-only-object-s43-paired
- project: acr-vla-conformal-refinement
- server: westd-49937
- log_path: ~/runs/acr-vla-conformal-refinement/westd-pi05-vla-only-object-s43-paired.log

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:westd-pi05-vla-only-object-s43-paired",
  "source": "cron:hook"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-26T11:47:27.017552+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__load_project_config",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:westd-pi05-vla-only-object-s43-paired",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__load_project_config",
    "max_results": "10"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-26T11:47:27.018019+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:westd-pi05-vla-only-object-s43-paired",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-26T11:47:30.623858+00:00_

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
  "session": "cron:hook:westd-pi05-vla-only-object-s43-paired",
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

_source line 5 · 2026-05-26T11:47:30.624297+00:00_

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
  "session": "cron:hook:westd-pi05-vla-only-object-s43-paired",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-26T11:47:31.606571+00:00_

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
  "session": "cron:hook:westd-pi05-vla-only-object-s43-paired",
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

_source line 7 · 2026-05-26T11:47:31.839571+00:00_

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
  "session": "cron:hook:westd-pi05-vla-only-object-s43-paired",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-26T11:47:49.301726+00:00_

Error: result (1,574,342 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-f8682bef/fe44cc13-fae1-4638-a13d-971c16ecac4f/tool-results/mcp-agent-ml-research-read_registry-1779796068888.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-f8682bef/fe44cc13-fae1-4638-a13d-971c16ecac4f/tool-results/mcp-agent-ml-research-read_registry-1779796068888.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:westd-pi05-vla-only-object-s43-paired",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 18677
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-26T11:57:07.711145+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 23, \"results\": [{\"exp_id\": \"pi05-crm-k2-long-s44-cqa1\", \"success\": true, \"actions\": [\"Job still running (pid=pi05-crm-k2-long-s44-cqa1)\"]}, {\"exp_id\": \"pi05-crm-k2-spatial-s42-bjb2-r2\", \"success\": true, \"actions\": [\"Job still running (pid=334539)\"]}, {\"exp_id\": \"pi05-crm-k2-spatial-s43-bjb2-r2\", \"success\": true, \"actions\": [\"Job still running (pid=334906)\"]}, {\"exp_id\": \"pi05-crm-k2-spatial-s44-bjb2-r2\", \"success\": true, \"actions\": [\"Job still running (pid=335268)\"]}, {\"exp_id\": \"pi05-adaptive-spatial-s42-bjb2-r2\", \"success\": true, \"actions\": [\"Job still running (pid=335649)\"]}, {\"exp_id\": \"pi05-adaptive-spatial-s43-bjb2-r2\", \"success\": true, \"actions\": [\"Job still running (pid=336003)\"]}, {\"exp_id\": \"pi05-adaptive-spatial-s44-bjb2-r2\", \"success\": true, \"actions\": [\"Job still running (pid=337564)\"]}, {\"exp_id\": \"pi05-crm-k2-goal-s42-bjb1-r2\", \"success\": true, \"actions\": [\"Job still running (pid=690807)\"]}, {\"exp_id\": \"pi05-crm-k2-goal-s43-bjb1-r2\", \"success\": true, \"actions\": [\"Job still running (pid=691080)\"]}, {\"exp_id\": \"pi05-crm-k2-goal-s44-bjb1-r2\", \"success\": true, \"actions\": [\"Job still running (pid=691360)\"]}, {\"exp_id\": \"pi05-crm-k2-object-s42-bjb1-r2\", \"success\": true, \"actions\": [\"Job still running (pid=691701)\"]}, {\"exp_id\": \"pi05-crm-k2-object-s43-bjb1-r2\", \"success\": true, \"actions\": [\"Job still running (pid=692172)\"]}, {\"exp_id\": \"pi05-crm-k2-object-s44-bjb1-r2\", \"success\": true, \"actions\": [\"Job still running (pid=692577)\"]}, {\"exp_id\": \"pi05-crm-k2-long-s42-r2\", \"success\": true, \"actions\": [\"Process gone, no sentinel, no W&B — escalating to agent (miss 2/5)\"]}, {\"exp_id\": \"pi05-crm-k2-long-s43-r2\", \"success\": true, \"actions\": [\"Job still running (pid=2916)\"]}, {\"exp_id\": \"pi05-adaptive-long-s42-r2\", \"success\": true, \"actions\": [\"Job s
…[truncated 989 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:westd-pi05-vla-only-object-s43-paired",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 577086
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-26T11:57:07.769075+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-26T11:53:40Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 1140 个实验 — ANALYZING 7, DEPLOYED 6, DONE 928, PREPARING 167, QUEUED 11, RUNNING 21\\n**DONE 分布**: failed 92, killed 209, negative 80, success 547\\n\\n### GPU 占用\\n- **实际运行**: 21 张 — bjb1-18228:cuda:0(pi05-crm-k2-long-s42-r2), bjb1-18228:cuda:1(pi05-crm-k2-long-s43-r2), bjb1-18228:cuda:3(pi05-adaptive-long-s42-r2), cqa1-32758:cuda:0(pi05-crm-k2-long-s44-cqa1), bjb1-32546:cuda:0(pi05-crm-k2-goal-s42-bjb1-r2), bjb1-32546:cuda:1(pi05-crm-k2-goal-s43-bjb1-r2), bjb1-32546:cuda:2(pi05-crm-k2-goal-s44-bjb1-r2), bjb1-32546:cuda:3(pi05-crm-k2-object-s42-bjb1-r2), bjb1-32546:cuda:4(pi05-crm-k2-object-s43-bjb1-r2), bjb1-32546:cuda:5(pi05-crm-k2-object-s44-bjb1-r2), bjb2-28827:cuda:0(pi05-crm-k2-spatial-s42-bjb2-r2), bjb2-28827:cuda:1(pi05-crm-k2-spatial-s43-bjb2-r2), bjb2-28827:cuda:2(pi05-crm-k2-spatial-s44-bjb2-r2), bjb2-28827:cuda:3(pi05-adaptive-spatial-s42-bjb2-r2), bjb2-28827:cuda:4(pi05-adaptive-spatial-s43-bjb2-r2), bjb2-28827:cuda:5(pi05-adaptive-spatial-s44-bjb2-r2), bjb1-18228:cuda:2(pi05-adaptive-goal-s44-bjb1), cqa1-32758:cuda:4(pi05-adaptive-long-s43-cqa1-r3), cqa1-32758:cuda:5(pi05-adaptive-long-s44-cqa1-r3), cqa1-32758:cuda:3(pi05-adaptive-object-s44-cqa1-r3), cqa1-32758:cuda:2(pi05-adaptive-object-s43-cqa1-r3)\\n\\n### 💾 磁盘余量\\n- **bjb1-18228**:\\n  - `/init`: 150M/150M 可用（已用 1%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 399G/438G 可用（已用 4%）\\n- **bjb1-32546**:\\n  - `/autodl-pub`: 1015G/7.0T 可用（已用 86%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 399G/438G 可用（已用 4%）\\n- **bjb2-28827**:\\n  - `/autodl-pub`: 4.2T/14T 可用（已用 71%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）
…[truncated 10712 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:westd-pi05-vla-only-object-s43-paired",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 576162
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-26T11:57:07.769787+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-26 06:39 UTC | 更新原因: Loop #24: D157-D159 修正 + MC1 consistency claim + π0.5 进度 + GPU 集群扩展到 29 卡\\n\\n> 详见 paper_framing.md（D146 narrative + D159 修正）\\n\\n## 核心方向\\n**ACR-VLA: Adaptive Conformal Refinement for Frozen Flow-Matching VLAs**。CoRL 2026 DDL **2026-05-29**（3天）。\\n\\n## 当前进展\\n- **SmolVLA Table 1**: 36/36 cells 完成（D157 统一 s42/43/44）。D159 修正 Spatial VLA-only 79.3±0.8\\n- **MC1 Claim 调整**: 从 magnitude claim (p<0.05) → **consistency claim**（Adaptive ≥ CRM on ALL 4 suites）。n=3 p≈0.27 n.s.；附录保留 8-seed paired p=0.017\\n- **MC3 Reframe (D155)**: π0.5 CRM/Adaptive 全 suite 负向 → 改为\\\"模型能力依赖性分析\\\"，不 claim cross-model generalization\\n- **π0.5 Table 2**: 实验进行中（~24 GPU 活跃），预计 12-24h 完成全部 4 suite × 3 mode × 3 seed\\n- **D158 westd Blackwell 偏差**: RTX PRO 6000 vs 4090 存在 3pp 系统性偏差 → Table 2 必须 same-server paired\\n- **Paper Agent**: 已激活（Reframe 模式），D159 修正已应用到 experiments/intro/abstract/discussion.tex\\n- **Agent**: 综合指令已发（P0 部署 5 空闲 GPU + P1 registry 清理 + P2 数据溯源 + P3 集群状态）\\n\\n## Table 1 — SmolVLA (D157 s42/43/44 统一, D159 修正)\\n| Suite | VLA-only | CRM | Adaptive | Δ(A-V) | 叙事角色 |\\n|-------|---------|-----|----------|--------|---------|\\n| Spatial | 79.3±0.8% | 80.3% | 80.8% | **+1.5pp** | consistency (n.s. p≈0.27) |\\n| Goal | 83.7% | 82.2% | 84.8% | **+1.1pp** | mechanism (trigger 8%) |\\n| Object | 77.8% | 76.5% | 77.8% | ±0.0pp | CRM harmful → gating necessary |\\n| Long | 57.2% | ~55.5% | ~56.0% | ~-1.2pp | CRM harmful → gating necessary |\\n\\n**核心 pattern**: CRM always-on 在 Object/Long 有害 → Adaptive gating 必要性。Spatial/Goal Adaptive ≥ VLA-only。\\n\\n## π0.5 Table 2 进度\\n- **VLA-only baseline**: 需补跑（westd 需 same-server paired）\\n- **CRM K=2**: Goal s42-44 运行中, Object/Long/Spatial 部署中\\n- **Adaptive**: Spatial s42-44 运行中, Goa
…[truncated 2717 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:westd-pi05-vla-only-object-s43-paired",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 575930
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-26T11:57:16.847760+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'exp_id': 'westd-pi05-vla-only-object-s43-paired'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:westd-pi05-vla-only-object-s43-paired",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'exp_id': 'westd-pi05-vla-only-object-s43-paired'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-26T11:57:18.015581+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'exp_id': 'westd-pi05-vla-only-object-s42-paired'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:westd-pi05-vla-only-object-s43-paired",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'exp_id': 'westd-pi05-vla-only-object-s42-paired'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-26T11:57:18.401708+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'exp_id': 'westd-pi05-vla-only-object-s44-paired'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:westd-pi05-vla-only-object-s43-paired",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'exp_id': 'westd-pi05-vla-only-object-s44-paired'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-26T11:57:23.950142+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.0095}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:westd-pi05-vla-only-object-s43-paired",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 7102
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-26T11:57:33.085796+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.1417}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:westd-pi05-vla-only-object-s43-paired",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 15070
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-26T11:57:42.901455+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.7781}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:westd-pi05-vla-only-object-s43-paired",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 24499
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-26T11:57:49.006584+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement && grep -n \"westd-pi05-vla-only-object\" registry.yaml | head -30",
  "description": "Search for westd vla-only object experiments in registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:westd-pi05-vla-only-object-s43-paired",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement && grep -n \"westd-pi05-vla-only-object\" registry.yaml | head -30",
    "description": "Search for westd vla-only object experiments in registry"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-26T11:57:49.388678+00:00_

38733:  westd-pi05-vla-only-object-s42-paired:
38763:      log_path: ~/runs/acr-vla-conformal-refinement/westd-pi05-vla-only-object-s42-paired.log
38769:    log_path: ~/runs/acr-vla-conformal-refinement/westd-pi05-vla-only-object-s42-paired.log
38770:  westd-pi05-vla-only-object-s43-paired:
38800:      log_path: ~/runs/acr-vla-conformal-refinement/westd-pi05-vla-only-object-s43-paired.log
38806:    log_path: ~/runs/acr-vla-conformal-refinement/westd-pi05-vla-only-object-s43-paired.log
38812:  westd-pi05-vla-only-object-s44-paired:
38842:      log_path: ~/runs/acr-vla-conformal-refinement/westd-pi05-vla-only-object-s44-paired.log
38848:    log_path: ~/runs/acr-vla-conformal-refinement/westd-pi05-vla-only-object-s44-paired.log
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/sessions/agent_f8682bef

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:westd-pi05-vla-only-object-s43-paired",
  "tool": "Bash",
  "elapsed_ms": 382
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-26T11:57:51.657057+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "offset": "38730",
  "limit": "130"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:westd-pi05-vla-only-object-s43-paired",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
    "offset": "38730",
    "limit": "130"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-26T11:57:51.719853+00:00_

38730	      account: root
38731	    pid: '199149'
38732	    log_path: ~/runs/acr-vla-conformal-refinement/westd-pi05-vla-only-goal-s44-paired.log
38733	  westd-pi05-vla-only-object-s42-paired:
38734	    status: ANALYZING
38735	    retry_count: 0
38736	    created_at: '2026-05-26T11:02:15.888Z'
38737	    updated_at: '2026-05-26T11:48:56.824Z'
38738	    hypothesis: π0.5 VLA-only baseline on Object s42 (westd same-server paired). Blackwell
38739	      paired comparison for cross-hardware validation.
38740	    server: westd-49937
38741	    gpu: cuda:3
38742	    account: root
38743	    reproduce:
38744	      server: westd-49937
38745	      gpu: cuda:3
38746	      started_at: '2026-05-26T11:19:04.337Z'
38747	      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
38748	        base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py
38749	        --model pi05 --mode vla_only --benchmark object --seed 42 --n_rollouts 20
38750	        --output_file logs/eval_object_vla_only_pi05_seed42_westd.json"
38751	      code_commit: a594db578deeeeddc0ab068549e315c5a3bb4d6a
38752	      finished_at: '2026-05-26T11:48:36.048Z'
38753	      training_hours: 0.49
38754	    spec:
38755	      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
38756	        base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py
38757	        --model pi05 --mode vla_only --benchmark object --seed 42 --n_rollouts 20
38758	        --output_file logs/eval_object_vla_only_pi05_seed42_westd.json"
38759	      server: westd-49937
38760	      gpu:
38761	      - cuda:3
38762	      pid: '201673'
38763	      log_path: ~/runs/acr-vla-conformal-refinement/westd-pi05-vla-only-object-s42-paired.log
38764	      submitted_at: '2026-05-26T11:19:17.346Z'
38765	      submitted_via: submit_training_job
38766	      backend: tmux
38767	      account: root
38768	    pid: '201673'
38769	    log_path: ~/runs/acr-vla-conformal-refinement
…[truncated 4321 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:westd-pi05-vla-only-object-s43-paired",
  "tool": "Read",
  "elapsed_ms": 62
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-26T11:58:01.498586+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:westd-pi05-vla-only-object-s43-paired",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__save_project_file",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-26T11:58:01.552619+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:westd-pi05-vla-only-object-s43-paired",
  "tool": "ToolSearch",
  "elapsed_ms": 54
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-26T11:58:16.576752+00:00_

called mcp__agent-ml-research__spawn_worker

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker</summary>

```json
{
  "task_type": "analyze:westd-pi05-vla-only-object-paired",
  "project": "acr-vla-conformal-refinement",
  "task_prompt": "## 任务\n读取 westd-49937 上 3 个已完成的 π0.5 VLA-only Object baseline 实验的结果，提取 success rate。\n\n## 实验信息\n服务器: westd-49937\n三个实验:\n1. westd-pi05-vla-only-object-s42-paired — seed 42, output: logs/eval_object_vla_only_pi05_seed42_westd.json\n2. westd-pi05-vla-only-object-s43-paired — seed 43, output: logs/eval_object_vla_only_pi05_seed43_westd.json  \n3. westd-pi05-vla-only-object-s44-paired — seed 44, output: logs/eval_object_vla_only_pi05_seed44_westd.json\n\n工作目录: /root/acr-vla-conformal-refinement\n\n## 步骤\n1. SSH 到 westd-49937，读取这 3 个 JSON 文件内容（在 /root/acr-vla-conformal-refinement/logs/ 下）\n2. 如果 JSON 文件不存在，检查日志文件: ~/runs/acr-vla-conformal-refinement/westd-pi05-vla-only-object-s{42,43,44}-paired.log\n3. 提取每个实验的 success_rate（通常在 JSON 的 summary 或 results 字段中）\n4. 同时检查 W&B 是否有对应 run（搜索 run name 包含 \"object\" \"vla_only\" \"pi05\" \"seed{42,43,44}\" \"westd\"）\n5. 用 update_registry 更新每个实验:\n   - 如果有有效 success rate → conclusion=success, metrics={\"success_rate\": X}\n   - 如果结果明显失败（如 0% 或异常） → conclusion=failed, 记录 failure_reason\n   - status 设为 DONE\n   - 设置 checkpoint_path（无 checkpoint 则设 \"N/A - eval only\"）和 log_path\n\n## 产出\n在任务结果中报告:\n- 三个 seed 的 success_rate\n- 均值和标准差\n- 与其他已知 π0.5 Object 结果的对比（如果在 registry 中能看到）\n\n## 注意\n- 这些是 eval-only 实验（无 checkpoint），所以 checkpoint_path 设为 \"N/A - eval only\"\n- 这些是 westd Blackwell GPU 的 same-server paired 实验，用于 Table 2 cross-hardware validation\n",
  "tool_groups": "['ssh', 'wandb', 'registry']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:westd-pi05-vla-only-object-s43-paired",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "tool_args": {
    "task_type": "analyze:westd-pi05-vla-only-object-paired",
    "project": "acr-vla-conformal-refinement",
    "task_prompt": "## 任务\n读取 westd-49937 上 3 个已完成的 π0.5 VLA-only Object baseline 实验的结果，提取 success rate。\n\n## 实验信息\n服务器: westd-49937\n三个实验:\n1. westd-pi05-vla-only-object-s42-paired — seed 42, output: logs/eval_object_vla_only_pi05_seed42_westd.json\n2. westd-pi05-vla-only-object-s43-paired — seed 43, output: logs/eval_object_vla_only_pi05_seed43_westd.json  \n3. westd-pi05-vla-only-object-s44-paired — seed 44, output: logs/eval_object_vla_only_pi05_seed44_westd.json\n\n工作目录: /root/acr-vla-conformal-refinement\n\n## 步骤\n1. SSH 到 westd-49937，读取这 3 个 JSON 文件内容（在 /root/acr-vla-conformal-refinement/logs/ 下）\n2. 如果 JSON 文件不存在，检查日志文件: ~/runs/acr-vla-conformal-refinement/westd-pi05-vla-only-object-s{42,43,44}-paired.log\n3. 提取每个实验的 success_rate（通常在 JSON 的 summary 或 results 字段中）\n4. 同时检查 W&B 是否有对应 run（搜索 run name 包含 \"object\" \"vla_only\" \"pi05\" \"seed{42,43,44}\" \"westd\"）\n5. 用 update_registry 更新每个实验:\n   - 如果有有效 success rate → conclusion=success, metrics={\"success_rate\": X}\n   - 如果结果明显失败（如 0% 或异常） → conclusion=failed, 记录 failure_reason\n   - status 设为 DONE\n   - 设置 checkpoint_path（无 checkpoint 则设 \"N/A - eval only\"）和 log_path\n\n## 产出\n在任务结果中报告:\n- 三个 seed 的 success_rate\n- 均值和标准差\n- 与其他已知 π0.5 Object 结果的对比（如果在 registry 中能看到）\n\n## 注意\n- 这些是 eval-only 实验（无 checkpoint），所以 checkpoint_path 设为 \"N/A - eval only\"\n- 这些是 westd Blackwell GPU 的 same-server paired 实验，用于 Table 2 cross-hardware validation\n",
    "tool_groups": "['ssh', 'wandb', 'registry']"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-26T11:58:24.408505+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_analyze_westd-pi05-vla-only-object-paired_20260526T115819\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_analyze_westd-pi05-vla-only-object-paired_20260526T115819.log\", \"setup_data\": {}, \"message\": \"Worker worker_analyze_westd-pi05-vla-only-object-paired_20260526T115819 started. Use get_worker_status('worker_analyze_westd-pi05-vla-only-object-paired_20260526T115819') to check progress.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:westd-pi05-vla-only-object-s43-paired",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "elapsed_ms": 7831
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-26T11:58:37.716116+00:00_

Worker 已派发处理三个 westd VLA-only Object paired 实验结果。

同时注意到 reconcile 结果中 `pi05-crm-k2-long-s42-r2` 报告 "Process gone, no sentinel, no W&B — escalating to agent (miss 2/5)"——这个需要关注，但目前是 miss 2/5，还未达到自动判定失败的阈值，下一轮 cron 会继续检测。

等待 Worker 回调后汇总结果并向 Director 汇报。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:westd-pi05-vla-only-object-s43-paired"
}
```

</details>

---

## Round 2

2 recorded events

### User

_source line 27 · 2026-05-26T11:58:37.976902+00:00_

[CRON] 实验进程已正常退出，状态已转为 ANALYZING，需要你分析结果并推进到 DONE。
详情: Process exited cleanly, W&B data available

- exp_id: westd-pi05-vla-only-object-s43-paired
- project: acr-vla-conformal-refinement
- server: westd-49937
- log_path: ~/runs/acr-vla-conformal-refinement/westd-pi05-vla-only-object-s43-paired.log

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:westd-pi05-vla-only-object-s43-paired",
  "source": "cron:hook"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-26T11:58:53.988827+00:00_

已在处理中——之前收到同一实验的回调时已派 Worker `worker_analyze_westd-pi05-vla-only-object-paired` 读取 s42/s43/s44 三个实验结果，等待 Worker 完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:westd-pi05-vla-only-object-s43-paired"
}
```

</details>

---

## Round 3

1 recorded events

### User

_source line 29 · 2026-05-27T04:18:19.361667+00:00_

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
  "session": "cron:hook:westd-pi05-vla-only-object-s43-paired",
  "source": "system:ralph_loop"
}
```

</details>

---

## Round 4

2 recorded events

### User

_source line 30 · 2026-05-27T05:14:33.410705+00:00_

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
  "session": "cron:hook:westd-pi05-vla-only-object-s43-paired",
  "source": "system:ralph_loop"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-27T05:16:41.283103+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- **westd-49937 (RTX PRO 6000 Blackwell) 存在 ~3pp 系统性偏差**（D158）：Table 2 必须 same-server paired comparison，不能和 4090 服务器数据混用
- **evaluate.py 必须用 commit a594db5**（D163）：所有补跑用旧代码，确保 Table 一致性。不要 git pull 到新版本
- **GPU 脚本内 `--gpu 0` 起始**：框架自动注入 CUDA_VISIBLE_DEVICES，脚本内永远从 0 开始编号
- **pi05-crm-k2-long-s42-r2 (bjb1-18228:cuda:0)**：reconcile 报 "Process gone, no sentinel, no W&B — miss 2/5"，可能需要重启或标记 failed
- **cqa1-32758 /autodl-pub 已用 94%**：提交新实验到 cqa1 前必须先清理磁盘

### 2. 🖥️ 基础设施快照
- **bjb1-18228** (4×4090): 工作目录 `/root/acr-vla-conformal-refinement`, conda base, 3 RUNNING (long-s42-r2 cuda:0, long-s43-r2 cuda:1, adaptive-long-s42-r2 cuda:3) + adaptive-goal-s44-bjb1 cuda:2
- **bjb1-32546** (6×4090): 同上路径, 6 RUNNING — CRM K=2 goal s42-44 (cuda:0-2) + CRM K=2 object s42-44 (cuda:3-5)
- **bjb2-28827** (6×4090): 6 RUNNING — CRM K=2 spatial s42-44 (cuda:0-2) + Adaptive spatial s42-44 (cuda:3-5)
- **cqa1-32758** (6×4090D): CRM K=2 long-s44 (cuda:0), adaptive-object-s43-r3 (cuda:2), adaptive-object-s44-r3 (cuda:3), adaptive-long-s43-r3 (cuda:4), adaptive-long-s44-r3 (cuda:5). cuda:1 空闲
- **westd-49937** (6×RTX PRO 6000): VLA-only Object s42/43/44 paired 刚完成 (ANALYZING)。全 6 卡即将空闲
- Python 路径统一: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 代码 commit: a594db578dee (D163 锁定版本)

### 3. 📊 当前状态
**刚做完**: 收到 westd-pi05-vla-only-object-s43-paired 完成回调（连续收到 4 次相同 CRON），已派 Worker `worker_analyze_westd-pi05-vla-only-object-paired_20260526T115819` 去读取 3 个 Object VLA-only paired 实验结果（s42/s43/s44 全部 ANALYZING）。**Worker 回调尚未返回。**

**RUNNING 实验 (21 张卡)**:
- bjb1-18228: pi05-crm-k2-long-s42-r2, s43-r2, adaptive-long-s42-r2, adaptive-goal-s44-bjb1
- bjb1-32546: pi05-crm-k2-goal-s42/43/44-bjb1-r2, pi05-crm-k2-object-s42/43/44-bjb1-r2
- bjb2-28827: pi05-crm-k2-spatial-s42/43/44-bjb2-r2, pi05-adaptive-spatial-s42/43/44-bjb2-r2
- cqa1-32758: pi05-crm-k2-long-s44-cqa1, adaptive-object-s43/s44-cqa1-r3, adaptive-long-s43/s44-cqa1-r3

**等待中**:
- Worker 回调: `worker_analyze_westd-pi05-vla-only-object-paired` — 读取 westd Object VLA-only 结果
- pi05-crm-k2-long-s42-r2 可能已死（cron miss 2/5），需要诊断
- 167 个 PREPARING 实验排队（大部分是 Table 2 补跑）
- **未向 Director 汇报本轮状态**（session 启动后 MCP 断连，无法 post_to_director）

### 4. 📋 待办（条件触发式）
- Worker `worker_analyze_westd-pi05-vla-only-object-paired` 回调 → 读取 3 seed success_rate → update_registry DONE → 计算均值±std → 对比 Table 2 其他 VLA-only baseline → 汇报 Director
- westd 6 卡空闲 → 部署下一批 π0.5 实验（但注意 Blackwell 偏差，只能跑 same-server paired 对比）
- pi05-crm-k2-long-s42-r2 miss 达 5 → 标记 failed，用空出的 bjb1-18228:cuda:0 重跑
- 各服务器 CRM/Adaptive 实验陆续完成 → 按 on-experiment-done 流程分析 + 填 Table 2 格子
- Table 2 全部 4 suite × 3 mode × 3 seed 完成 → 汇报 Director + 触发 Paper Agent 更新 experiments.tex
- CoRL DDL 2026-05-29（还剩 ~2.5 天）→ 所有实验必须在 ~24h 内完成才有时间写论文

### 5. 🎯 战略上下文
**CoRL 2026 DDL = 2026-05-29，仅剩 ~2.5 天。**

**核心 claim 策略**:
- MC1 (Consistency): Adaptive ≥ CRM on ALL 4 suites → gating 消除 CRM 退化（n=3 p≈0.27 n.s.，改为 consistency claim 而非 magnitude claim）
- MC2 (Mechanism): trigger_rate ↔ Δ 单调正相关
- MC3 (Cross-VLA): π0.5 负向 → D155 reframe 为"模型能力依赖性分析"，不 claim cross-model generalization

**关键决策链**: D158 Blackwell 偏差 → D159 Spatial VLA-only 修正 79.3±0.8 → D162 CRM K=10 reframe → D163 evaluate.py 锁版本 a594db5

**易踩坑**:
- 不要把 westd (Blackwell) 和 bjb/cqa (4090) 的数据直接对比——硬件偏差 ~3pp
- Table 1 是 SmolVLA (K=10, 已完成 36/36)，Table 2 是 π0.5 (K=2, 进行中)——不要混淆
- π0.5 的 K=2 argmin 选择本身对强 VLA 有害（τ=0.90 时 SR=89% vs VLA-only 96%），这不是 CRM 的问题
- cqa1 磁盘紧张（94%），新实验优先放其他服务器
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:westd-pi05-vla-only-object-s43-paired"
}
```

</details>

---
