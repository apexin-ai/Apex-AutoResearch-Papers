# cron hook alpha sweep a045 s42 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 154
- **Recorded user turns:** 1
- **Tool calls:** 76
- **Original source:** `logs/chats/cron_hook_alpha_sweep_a045_s42_fp32.jsonl`
- **Structured JSON:** [`ba5dfe44ec6777e7ce9b.json`](../../sessions/ba/ba5dfe44ec6777e7ce9b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

154 recorded events

### User

_source line 1 · 2026-05-19T22:42:06.436007+00:00_

[CRON] 实验进程已正常退出，状态已转为 ANALYZING，需要你分析结果并推进到 DONE。
详情: Process exited cleanly, W&B data available

- exp_id: alpha_sweep_a045_s42_fp32
- project: distrib_canary_collapse
- server: westd-17855

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "source": "cron:hook"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-19T22:42:21.708431+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__get_project_resource_usage",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__get_project_resource_usage",
    "max_results": "10"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-19T22:42:21.708770+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-19T22:42:24.793661+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "distrib_canary_collapse",
  "limit": "0",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "distrib_canary_collapse",
    "limit": "0",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T22:42:25.295819+00:00_

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
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T22:42:25.851661+00:00_

Error: result (209,947 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse--claude-sessions-agent-f6701116/1625055f-e5f2-4c87-984e-779469cea8ba/tool-results/mcp-agent-ml-research-read_registry-1779230545488.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse--claude-sessions-agent-f6701116/1625055f-e5f2-4c87-984e-779469cea8ba/tool-results/mcp-agent-ml-research-read_registry-1779230545488.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse--claude-sessions-agent-f6701116/1625055f-e5f2-4c87-984e-779469cea8ba/tool-results/mcp-agent-ml-research-read_registry-1779230545488.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1057
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T22:42:26.253794+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "distrib_canary_collapse",
  "file": "report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "distrib_canary_collapse",
    "file": "report.md"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-19T22:42:26.254139+00:00_

called mcp__agent-ml-research__read_roadmap

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_roadmap</summary>

```json
{
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T22:42:26.705979+00:00_

called mcp__agent-ml-research__get_project_resource_usage

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_project_resource_usage</summary>

```json
{
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "mcp__agent-ml-research__get_project_resource_usage",
  "tool_args": {
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-19T22:42:27.107714+00:00_

called mcp__agent-ml-research__list_workers

<details open><summary>🔧 Tool call — mcp__agent-ml-research__list_workers</summary>

```json
{
  "project": "distrib_canary_collapse",
  "status": "running"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "mcp__agent-ml-research__list_workers",
  "tool_args": {
    "project": "distrib_canary_collapse",
    "status": "running"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-19T22:42:39.716700+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 7, \"results\": [{\"exp_id\": \"opt13b_wiki_a100_s43_fp32\", \"success\": true, \"actions\": [\"Job still running (pid=452614)\"]}, {\"exp_id\": \"pythia410m_wiki_a100_s43_fp32\", \"success\": true, \"actions\": [\"Job still running (pid=183582)\"]}, {\"exp_id\": \"smollm3_3b_wiki_a100_s43_fp32\", \"success\": true, \"actions\": [\"Job still running (pid=466636)\"]}, {\"exp_id\": \"qwen35_08b_wiki_a100_s43_fp32\", \"success\": true, \"actions\": [\"Job still running (pid=174458)\"]}, {\"exp_id\": \"scale_69b_a100_s43\", \"success\": true, \"actions\": [\"Job still running (pid=177515)\"]}, {\"exp_id\": \"interv_pred_14b_s42_fp32\", \"success\": true, \"actions\": [\"Job still running (pid=191999)\"]}, {\"exp_id\": \"scale_14b_c4_s42_fp32\", \"success\": true, \"actions\": [\"Job still running (pid=201974)\"]}]}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 14420
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T22:42:39.717542+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-19T22:42:05Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 110 个实验 — ANALYZING 1, DONE 95, PREPARING 7, RUNNING 7\\n**DONE 分布**: failed 9, killed 22, negative 2, success 62\\n\\n### GPU 占用\\n- **实际运行**: 7 张 — westd-19828:cuda:0(opt13b_wiki_a100_s43_fp32), westd-17855:cuda:1(qwen35_08b_wiki_a100_s43_fp32), westd-17855:cuda:2(scale_69b_a100_s43), westd-17855:cuda:3(pythia410m_wiki_a100_s43_fp32), westd-19828:cuda:1(smollm3_3b_wiki_a100_s43_fp32), westd-17855:cuda:0(interv_pred_14b_s42_fp32), westd-17855:cuda:5(scale_14b_c4_s42_fp32)\\n\\n### 💾 磁盘余量\\n- **westd-19828**:\\n  - `/init`: 150M/150M 可用（已用 0%）\\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\\n  - `/usr/bin/nvidia-smi`: 817G/879G 可用（已用 3%）\\n- **westd-17855**:\\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\\n  - `/init`: 150M/150M 可用（已用 0%）\\n  - `/usr/bin/nvidia-smi`: 816G/879G 可用（已用 3%）\\n\\n### 🏃 RUNNING\\n| exp_id | server | gpu | pid | log |\\n|--------|--------|-----|-----|-----|\\n| `opt13b_wiki_a100_s43_fp32` | westd-19828 | cuda:0 | 452614 | `—` |\\n| `qwen35_08b_wiki_a100_s43_fp32` | westd-17855 | cuda:1 | 174458 | `—` |\\n| `scale_69b_a100_s43` | westd-17855 | cuda:2 | 177515 | `—` |\\n| `pythia410m_wiki_a100_s43_fp32` | westd-17855 | cuda:3 | 183582 | `—` |\\n| `smollm3_3b_wiki_a100_s43_fp32` | westd-19828 | cuda:1 | 466636 | `—` |\\n| `interv_pred_14b_s42_fp32` | westd-17855 | cuda:0 | 191999 | `—` |\\n| `scale_14b_c4_s42_fp32` | westd-17855 | cuda:5 | 201974 | `—` |\\n\\n### 📌 最近完成 (top 5)\\n- `c4_a075_s42_fp32` [success] — 2026-05-19T22:37:48\\n- `c4_a050_s42_fp32` [success] — 2026-05-19T22:37:46\\n- `c4_a025_s42_fp32` [success] — 2026-05-19T22:30:28\\n- `alpha_sweep_a030_s42_fp32` [success] — 2026-05-19T20:33:35\\n- `method_ablation_phase3
…[truncated 5371 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 13463
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-19T22:42:39.718114+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/ROADMAP.md\", \"content\": \"# distrib_canary_collapse — Research Dashboard\\n\\n> 最后更新: 2026-05-19 22:40 UTC | 更新原因: D113 C4 D111 global audit complete, plan_035 confirmed done, C4 dose-response table added\\n\\n> **阶段**: Research Day 2 — D107-D113 完成 + 8 实验 RUNNING + D111 全局审计完成\\n\\n## 核心方向\\n**D067 升级**: analysis → method paper。核心贡献：\\n1. **MMCT** — 5 方法框架，**PermG fwd 主指标**（6-8/8 跨 10/12 架构-seed 组合），K≥3(3σ) 辅助\\n2. **Regime map + 盲区 (D075/D110)** — onset **[0.40, 0.50]**（a035=0/8, a040=0/8, a050=6/8）\\n3. **Downstream 指标选择 (D085)** — perplexity 极端 collapse 下丧失 lag structure\\n4. **threshold_onset limitation (D105)** — T=11/3σ 下 ≈0/8，MMCT 实质 4 方法共识\\n5. **D108 同步坍缩区** — α=0.60 PermG 0-3/8 + K≥4 峰值 87.5%（TY 互补）\\n6. **D109 canary 指标选择** — SmolLM3 PermG=3/8, K≥3=**0/8**，canary 分裂无共识\\n7. **D112-D113 C4 域** — perplexity-dominated collapse + diff_xcorr 系统性反向（24/24 pair lag≤0）\\n\\n**Target**: EMNLP 2026 main track（ARR June cycle, DDL ~June 15, ~26 days）\\n\\n## 当前进展\\n- **D111 全局审计完成（D113）**: 三个 C4 实验 direction-checked 修正，Reviewer 独立核实 PASS\\n  - c4_a025: K≥3 8→0, K≥4 3→0; c4_a050: K≥4 8→2; c4_a075: K≥4 8→**0**, naive 8→0\\n  - C4 diff_xcorr 24/24 pair 全部 lag≤0——域特异时间结构（丰富 Claim 3）\\n  - PermG 不受影响（c4_a050=8/8, c4_a075=8/8）\\n- **plan_035 已确认完成**: c4_a075_s42_fp32 = plan_035（PermG=8/8）\\n- **plan_036 RUNNING**: Pythia-1.4B × C4 on cuda:5 (~12h)\\n- **分析脚本修复中**: batch_analysis.py/run_5method_s43.py 加 D111 direction filter\\n- 63+ 成功 / 8 RUNNING (8/8 GPU)\\n\\n## Table 7 权威数据（D105 pipeline, 统一方法论）\\n\\n| 模型 | Seed | PermG↑ | K≥3(3σ) | K≥4(3σ) | 备注 |\\n|------|------|--------|---------|---------|------|\\n| Pythia-6.9B | s42 | 7/8 | 8/8 | 3/8 | bf16 |\\n| Qwen3.5-0.8B | s42 | 8/8 | 8/8 | 6/8 | |\\n| Pythia-1.4B | s42 | **2/8** | 2/8 | 0/8 | seed sensitive |\\n| Pythia-1.4B | s43 | 6/8 | 6/8 | 3/8 | |\\n| Pythia-410M | s42 | 6/8 | 6/8 | 1
…[truncated 4819 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 13463
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T22:42:40.121533+00:00_

{"result":"{\"success\": true, \"data\": {\"allocated_gpus\": [], \"actually_running_gpus\": [{\"server\": \"westd-19828\", \"gpu_id\": \"cuda:0\", \"exp_id\": \"opt13b_wiki_a100_s43_fp32\"}, {\"server\": \"westd-17855\", \"gpu_id\": \"cuda:1\", \"exp_id\": \"qwen35_08b_wiki_a100_s43_fp32\"}, {\"server\": \"westd-17855\", \"gpu_id\": \"cuda:2\", \"exp_id\": \"scale_69b_a100_s43\"}, {\"server\": \"westd-17855\", \"gpu_id\": \"cuda:3\", \"exp_id\": \"pythia410m_wiki_a100_s43_fp32\"}, {\"server\": \"westd-19828\", \"gpu_id\": \"cuda:1\", \"exp_id\": \"smollm3_3b_wiki_a100_s43_fp32\"}, {\"server\": \"westd-17855\", \"gpu_id\": \"cuda:0\", \"exp_id\": \"interv_pred_14b_s42_fp32\"}, {\"server\": \"westd-17855\", \"gpu_id\": \"cuda:5\", \"exp_id\": \"scale_14b_c4_s42_fp32\"}], \"allocated_but_idle\": [], \"registered_but_hw_idle\": [], \"unregistered_but_hw_active\": [], \"running_experiments\": [{\"exp_id\": \"opt13b_wiki_a100_s43_fp32\", \"gpus\": [\"cuda:0\"], \"util_avg\": null}, {\"exp_id\": \"qwen35_08b_wiki_a100_s43_fp32\", \"gpus\": [\"cuda:1\"], \"util_avg\": null}, {\"exp_id\": \"scale_69b_a100_s43\", \"gpus\": [\"cuda:2\"], \"util_avg\": null}, {\"exp_id\": \"pythia410m_wiki_a100_s43_fp32\", \"gpus\": [\"cuda:3\"], \"util_avg\": null}, {\"exp_id\": \"smollm3_3b_wiki_a100_s43_fp32\", \"gpus\": [\"cuda:1\"], \"util_avg\": null}, {\"exp_id\": \"interv_pred_14b_s42_fp32\", \"gpus\": [\"cuda:0\"], \"util_avg\": null}, {\"exp_id\": \"scale_14b_c4_s42_fp32\", \"gpus\": [\"cuda:5\"], \"util_avg\": null}], \"worker_pool\": {\"total\": 0, \"gpu_tasks\": 0, \"cpu_tasks\": 0, \"details\": []}, \"summary\": \"分配 0 张, 实际跑 7 张 | Worker 0 (GPU 0 / CPU 0)\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "mcp__agent-ml-research__get_project_resource_usage",
  "elapsed_ms": 13415
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-19T22:42:40.172248+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [], \"count\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 13064
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-19T22:42:50.615429+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "distrib_canary_collapse",
  "filters": "{'exp_id': 'alpha_sweep_a045_s42_fp32'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "distrib_canary_collapse",
    "filters": "{'exp_id': 'alpha_sweep_a045_s42_fp32'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-19T22:42:50.967029+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3416}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 351
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-19T22:42:59.614332+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse--claude-sessions-agent-f6701116/1625055f-e5f2-4c87-984e-779469cea8ba/tool-results/mcp-agent-ml-research-read_registry-1779230545488.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\nfor eid, exp in exps.items():\n    if 'a045' in eid:\n        print(json.dumps({eid: exp}, indent=2))\n\"",
  "description": "Extract alpha_sweep_a045 experiment from registry dump"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse--claude-sessions-agent-f6701116/1625055f-e5f2-4c87-984e-779469cea8ba/tool-results/mcp-agent-ml-research-read_registry-1779230545488.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\nfor eid, exp in exps.items():\n    if 'a045' in eid:\n        print(json.dumps({eid: exp}, indent=2))\n\"",
    "description": "Extract alpha_sweep_a045 experiment from registry dump"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-19T22:42:59.818602+00:00_

{
  "alpha_sweep_a045_s42_fp32": {
    "status": "ANALYZING",
    "retry_count": 0,
    "created_at": "2026-05-19T18:30:38.128Z",
    "updated_at": "2026-05-19T22:42:03.118Z",
    "hypothesis": "PermG onset \u7cbe\u5316\u81f3 \u00b10.025\uff1a\u03b1=0.40 PermG=0/8, \u03b1=0.50 PermG=6/8\u3002\u03b1=0.45 \u5982\u679c PermG=0/8 \u2192 onset \u2208 [0.45, 0.50]\uff1b\u5982\u679c PermG>0 \u2192 onset \u2208 [0.40, 0.45]\u3002Claim 2 dose-response boundary\u3002",
    "parent": "alpha_sweep_a040_s42_fp32_v2",
    "spec": {
      "command": "python -u iterative_train.py --model_name EleutherAI/pythia-410m --seed 42 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.45 --output_dir results/alpha_sweep/a045_s42_fp32",
      "server": "westd-17855",
      "data_path": "data/wikitext103_5k",
      "data_count": 5000,
      "model_name": "EleutherAI/pythia-410m",
      "seed": 42,
      "precision": "fp32",
      "gpu": [
        "cuda:4"
      ],
      "pid": "178545",
      "checkpoint_source": "EleutherAI/pythia-410m (training from scratch)",
      "eval_data": "N/A (training experiment)"
    },
    "reproduce": {
      "finished_at": "2026-05-19T22:42:02.573Z"
    },
    "extra": {
      "hook_events": [
        {
          "event": "on_complete",
          "action": "agent",
          "ts": "2026-05-19T22:42:06.533436+00:00"
        }
      ]
    }
  }
}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "elapsed_ms": 204
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-19T22:43:12.005873+00:00_

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
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
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

_source line 21 · 2026-05-19T22:43:12.056559+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-19T22:43:22.152666+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "distrib_canary_collapse",
  "file": "memory.md",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "distrib_canary_collapse",
    "file": "memory.md",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-19T22:43:23.625760+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/memory.md\", \"content\": \"# Memory\\n\\n## D079 精度规则（2026-05-18，替代旧 bf16 硬约束）\\n\\n### bf16 vs fp32 系统性差异（Reviewer critical 发现）\\nGPT-2m fp32 (s42) vs bf16 (s43) 在 α=1.0：entropy drift 差 5.2×（-86.6% vs -16.6%），ppl drift 差 ~730×（+50,527% vs +68.6%）。bf16 的 stochastic rounding 提供强隐式正则化，系统性抑制 collapse。\\n\\n### 精度规则\\n- **≤3B 模型一律 fp32**（不传 --bf16）\\n- **>3B 模型**（如 Pythia-6.9B）允许 bf16，论文中 framing 为\\\"bf16 条件下 pattern 是否持续\\\"\\n- Table 7 和 dose-response map 主轴只用 fp32 数据\\n- bf16 实验作为补充证据，论文中明确标注\\n\\n### westd-17855 fp32 支持\\n- 旧问题：不带 --bf16 时 fp16 GradScaler crash（Blackwell 不兼容）\\n- 已修复：iterative_train.py 修改为不带 --bf16 时使用纯 fp32（禁用 GradScaler + autocast）\\n- dry-run 通过：westd-17855 cuda:4 上 Pythia-410M fp32 训练成功\\n\\n## D080 torch_dtype bug 及修复（2026-05-19）\\n\\n### 根因\\niterative_train.py 中 `_DTYPE_KWARG: torch.bfloat16 if args.bf16 else None`。`torch_dtype=None` 导致模型以原生 dtype 加载：\\n- Pythia-410M/1.4B: 原生 float16 → 无 GradScaler → loss=0, grad_norm=nan\\n- SmolLM3-3B: 原生 bfloat16 → 训练正常但精度不是 D079 要求的 fp32\\n- Qwen3.5-0.8B: safetensors 存储为 bfloat16 → 同上\\n\\n### 修复（两轮）\\n1. `else None` → `else torch.float32`：对大多数模型有效（SmolLM3 确认 13.8GB = fp32）\\n2. 添加 `model.to(dtype=target_dtype)` 强制转换：Qwen3.5 的 safetensors 格式导致 transformers 5.8.1 忽略 `torch_dtype` 参数，必须显式 `.to()` 才能转 float32\\n\\n### iterative_train.py 当前版本\\n- md5: `5b37837e7a6378f42bcb740f8f5e4773`（两台服务器一致）\\n- 包含: fp16=False + `else torch.float32` + `.to(dtype=target_dtype)` 强制转换\\n\\n### 教训\\n- `torch_dtype` 参数在 transformers 中对不同模型行为不一致，`.to()` 是唯一可靠的 dtype 转换方式\\n- 内存用量可以验证 dtype：3B fp32 ≈ 12-14GB, 3B bf16 ≈ 6-7GB\\n\\n## westd-17855 环境提交规范（2026-05-18）\\n\\n### 问题\\nwestd-17855 的 `.bashrc` 无 conda init 块且有 `[ -z \\\"$PS1\\\" ] && return` 导致非交互 shell 跳过所有配置。裸 `python` 命令和缺少 HF 环境变量均导致失败。\\n\\n### 完整提交命令模板\\n```\\nbash -c \\\"cd /root/autodl-tmp/distrib_canary_collapse && source /root/m
…[truncated 3597 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1473
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-19T22:43:23.677677+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/skills/resource-saturation.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/skills/resource-saturation.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-19T22:43:23.779335+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_f6701116.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-19T22:43:27.442598+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/resource-saturation.skill.md",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/resource-saturation.skill.md",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-19T22:43:27.493363+00:00_

1	---
2	name: resource-saturation
3	description: "当你准备向 Director 汇报前、收到 cron/worker 回调、审批通过准备开跑、怀疑 Worker 池不够饱和时,立即使用本 skill。四部分:A) GPU 分配率(分配了没跑=失职) B) GPU 效率 C) 非 GPU 任务并行(Worker 池<2=失职) D) 汇报必须带 [资源] 行。"
4	always: false
5	roles:
6	  - director
7	  - agent
8	---
9	
10	# 资源饱和度自检（硬约束）
11	
12	## A. GPU 分配率检查
13	
14	调 `get_project_resource_usage(project)` 看:
15	- 已分配给本项目的 GPU 总数和具体卡号
16	- 实际在跑任务的 GPU 数和具体卡号（交叉 registry RUNNING + nvidia-smi 进程）
17	- 分配了但没跑的 GPU 清单 ⚠️
18	
19	任何"分配了但没跑"的 GPU = 失职。必须立即:
20	- 派 Worker 铺 dry-run / 下一批实验代码准备
21	- 铺 ablation（从 experiment-matrix 空白格子里挑）
22	- 确实无实验可铺 → 向 Director 汇报"暂无可铺实验"+ 建议下一步方向(扩 ablation 维度 / 加 baseline / 加 benchmark)。**不要建议归还 GPU**——项目级 GPU 归还只在归档时由 `archive_project` 自动触发, 不是 Director 中途的动作
23	
24	**单实验不占多卡**: 分配 4 卡但实验只用 1 卡 → 另 3 卡必须并行跑其他实验,不能空占。
25	
26	## B. GPU 效率检查
27	
28	调 `get_gpu_health(server)`:
29	- 空闲 GPU（util < 10% 持续 > 5 min）→ 立即铺任务
30	- 低利用率（util < 50% 持续 > 15 min）→ spawn_worker 诊断（batch / IO / 同步）
31	- OOM 风险（显存 > 90% 持续 10 min）→ 主动降 batch / 调优
32	
33	## C. 非 GPU 任务并行
34	
35	GPU 在跑 ≠ 你空闲。以下 CPU / 网络任务**必须**派独立 Worker 并行:
36	- 下一批实验的数据集下载 / 预处理 / fingerprint
37	- 下一批实验的代码准备 / dry-run / 环境配置
38	- 论文文献调研 / related work 检索
39	- 已完成实验的 log 深度分析 / metric 聚合
40	- 论文章节起草
41	- 代码 review / refactor
42	
43	**硬约束**: 任一时刻 Worker 池 < 2 个 = 失职（除非真的全部下游阻塞在等 GPU,这时应当向 Director 申请扩 GPU）。
44	
45	## D. 汇报格式
46	
47	向 Director 汇报时开头必须带资源声明行:
48	
49	    [资源] GPU 分配 N / 实际在跑 M | Worker 池 K (其中 GPU 任务 A / CPU 任务 B)
50	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-19T22:43:38.843532+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/ | head -20",
  "description": "List recent artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/ | head -20",
    "description": "List recent artifacts"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-19T22:43:38.894214+00:00_

D040
D105_3sigma_recompute_combined.json
_project
a050_fp32_3seed_5method_analysis.md
a050_fp32_3seed_metrics_summary.md
a050_s44_draft_versions.tex
a075_analysis_prep.md
alpha_sweep
alpha_sweep_a000_s43
alpha_sweep_a000_s44
alpha_sweep_a005_s42
alpha_sweep_a010_s42_v2
alpha_sweep_a010_s43
alpha_sweep_a010_s43_fp32
alpha_sweep_a025_s43_fp32
alpha_sweep_a025_s44_fp32
alpha_sweep_a030_s42_fp32
alpha_sweep_a050_s42
alpha_sweep_a050_s43
alpha_sweep_a050_s44

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-19T22:43:42.711231+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/ | grep -i \"a030\\|a035\\|a040\\|a050_s42_fp32\"",
  "description": "Find nearby alpha experiment artifacts for reference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/ | grep -i \"a030\\|a035\\|a040\\|a050_s42_fp32\"",
    "description": "Find nearby alpha experiment artifacts for reference"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-19T22:43:42.762055+00:00_

alpha_sweep_a030_s42_fp32
c4_a050_s42_fp32

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-19T22:43:47.032478+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/alpha_sweep_a030_s42_fp32/",
  "description": "Check a030 artifact structure for analysis pattern"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/alpha_sweep_a030_s42_fp32/",
    "description": "Check a030 artifact structure for analysis pattern"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-19T22:43:47.083207+00:00_

report

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-19T22:43:49.696418+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/alpha_sweep_a030_s42_fp32/report/",
  "description": "Check a030 report files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/alpha_sweep_a030_s42_fp32/report/",
    "description": "Check a030 report files"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-19T22:43:49.746997+00:00_

alpha_sweep_a030_s42_fp32_analysis.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-19T22:43:52.610473+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/alpha_sweep_a030_s42_fp32/report/alpha_sweep_a030_s42_fp32_analysis.md",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/alpha_sweep_a030_s42_fp32/report/alpha_sweep_a030_s42_fp32_analysis.md",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-19T22:43:52.661834+00:00_

1	# Analysis: alpha_sweep_a030_s42_fp32
2	
3	## Config
4	- Model: Pythia-410M, WikiText-103, α=0.30, seed=42, fp32
5	- 11 generations (gen_0–gen_10), EXIT_CODE=0
6	- Server: westd-17855, 6.3 GPU-hours
7	- No W&B run
8	
9	## Hypothesis
10	α=0.30 仍在 blind zone（预期 PermG=0/8），将 onset 下界从 0.25 收紧到 0.30。
11	
12	## Result: CONFIRMED — PermG=0/8, blind zone 扩展至 α≤0.30
13	
14	## Drift (gen0→gen10)
15	| Metric | Drift |
16	|--------|-------|
17	| token_entropy | -17.32% |
18	| ECE | +549.38% |
19	| distinct_1 | -36.72% |
20	| distinct_2 | -49.75% |
21	| distinct_3 | -50.09% |
22	| mauve | -26.09% |
23	| perplexity | -8.37% |
24	| effective_rank | +17.28% |
25	
26	## 5-Method Lead-Lag (8 pairs: entropy/ECE × d1/d2/d3/mauve)
27	
28	### Summary
29	| Method | Sig/Total |
30	|--------|-----------|
31	| naive_xcorr | 8/8 |
32	| diff_xcorr | 4/8 |
33	| threshold_onset | 8/8 |
34	| **PermG fwd** | **0/8** |
35	| PermG rev | 0/8 |
36	| TY Granger | 5/8 (C003: unreliable at α≤0.50) |
37	| **K≥3** | **6/8** |
38	| **K≥4** | **3/8** |
39	
40	### Per-Pair Detail
41	
42	| Pair | naive | diff | thresh | PermG(p_fdr) | TY | Votes |
43	|------|-------|------|--------|--------------|-----|-------|
44	| entropy→d1 | ✓ lag=1 | ✓ lag=5 | ✓ lead=1 | ✗ (0.106) | ✓ d_max=0,df=7 | **4** |
45	| entropy→d2 | ✓ lag=1 | ✓ lag=5 | ✓ lead=1 | ✗ (0.106) | ✓ d_max=0,df=7 | **4** |
46	| entropy→d3 | ✓ lag=1 | ✗ | ✓ lead=1 | ✗ (0.106) | ✗ d_max=2,df=1 | 2 |
47	| entropy→mauve | ✓ lag=1 | ✗ | ✓ lead=7 | ✗ (0.128) | ✗ d_max=0,df=7 | 2 |
48	| ece→d1 | ✓ lag=-1 | ✓ lag=-1 | ✓ lead=1 | ✗ (0.106) | ✗ d_max=2,df=1 | 3 |
49	| ece→d2 | ✓ lag=-5 | ✗ | ✓ lead=1 | ✗ (0.106) | ✓ d_max=2,df=1 | 3 |
50	| ece→d3 | ✓ lag=-5 | ✗ | ✓ lead=1 | ✗ (0.106) | ✓ d_max=2,df=1 | 3 |
51	| ece→mauve | ✓ lag=2 | ✓ lag=2 | ✓ lead=7 | ✗ (0.106) | ✓ d_max=2,df=1 | **4** |
52	
53	### PermG FDR-adjusted p-values (all non-significant)
54	- entropy→d1: 0.106, entropy→d2: 0.106, entropy→d3: 0.106, entropy→mauve: 0.128
55	- ece→d1: 0.106, ece→d2: 0
…[truncated 799 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-19T22:44:08.344464+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse--claude-sessions-agent-f6701116/1625055f-e5f2-4c87-984e-779469cea8ba/tool-results/mcp-agent-ml-research-read_registry-1779230545488.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n# Find a recent similar experiment that was successfully analyzed\nfor eid in ['alpha_sweep_a030_s42_fp32', 'alpha_sweep_a035_s42_fp32', 'alpha_sweep_a040_v2_s42_fp32', 'alpha_sweep_a050_s42_fp32']:\n    if eid in exps:\n        e = exps[eid]\n        print(f'{eid}: status={e.get(\\\"status\\\")}, conclusion={e.get(\\\"conclusion\\\")}, metrics={json.dumps(e.get(\\\"metrics\\\",{}), indent=2)[:500]}')\n        print()\n\" 2>&1 | head -60",
  "description": "Get nearby alpha experiments for metric comparison"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse--claude-sessions-agent-f6701116/1625055f-e5f2-4c87-984e-779469cea8ba/tool-results/mcp-agent-ml-research-read_registry-1779230545488.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n# Find a recent similar experiment that was successfully analyzed\nfor eid in ['alpha_sweep_a030_s42_fp32', 'alpha_sweep_a035_s42_fp32', 'alpha_sweep_a040_v2_s42_fp32', 'alpha_sweep_a050_s42_fp32']:\n    if eid in exps:\n        e = exps[eid]\n        print(f'{eid}: status={e.get(\\\"status\\\")}, conclusion={e.get(\\\"conclusion\\\")}, metrics={json.dumps(e.get(\\\"metrics\\\",{}), indent=2)[:500]}')\n        print()\n\" 2>&1 | head -60",
    "description": "Get nearby alpha experiments for metric comparison"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-19T22:44:08.445345+00:00_

alpha_sweep_a030_s42_fp32: status=DONE, conclusion=success, metrics={
  "permg_fwd": "0/8",
  "permg_rev": "0/8",
  "k_ge3": "6/8",
  "k_ge4": "3/8",
  "naive_xcorr": "8/8",
  "diff_xcorr": "4/8",
  "threshold_onset": "8/8",
  "ty_granger": "5/8",
  "drift_entropy_pct": -17.32,
  "drift_ece_pct": 549.38,
  "drift_d1_pct": -36.72,
  "drift_d2_pct": -49.75,
  "drift_d3_pct": -50.09,
  "drift_mauve_pct": -26.09,
  "n_generations": 11,
  "n_perm": 5000,
  "alpha_bh": 0.05,
  "precision": "fp32"
}

alpha_sweep_a035_s42_fp32: status=DONE, conclusion=success, metrics={
  "PermG_fwd": "0/8",
  "PermG_rev": "0/8",
  "K_ge3_3sigma": "6/8",
  "K_ge4_3sigma": "2/8",
  "threshold_onset": "8/8",
  "TY_granger": "4/8",
  "naive_xcorr_fwd": "8/8",
  "diff_xcorr_fwd": "4/8",
  "detection_rate_k4": 0.25,
  "drift_pct": {
    "token_entropy": -18.53,
    "ece": 651.26,
    "perplexity": -1.27,
    "distinct_1": -36.38,
    "distinct_2": -49.45,
    "distinct_3": -50.04,
    "effective_rank": 22.21,
    "mauve": -17.78
  },
  "gen0": {
    "token_entropy": 3.234,
    "ec

alpha_sweep_a050_s42_fp32: status=DONE, conclusion=success, metrics={
  "token_entropy_gen0": 3.2342,
  "token_entropy_gen10": 2.7075,
  "token_entropy_drift_pct": -16.3,
  "distinct_1_gen0": 0.0916,
  "distinct_1_gen10": 0.0649,
  "distinct_1_drift_pct": -29.2,
  "perplexity_gen0": 26.95,
  "perplexity_gen10": 31.46,
  "perplexity_drift_pct": 16.8,
  "ece_gen0": 0.0108,
  "ece_gen10": 0.0868,
  "ece_drift_pct": 703.4,
  "perm_granger_fwd": "6/8",
  "perm_granger_rev": "0/8",

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-19T22:44:19.999477+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/c4_a050_s42_fp32/report/",
  "description": "Check recent analysis report structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/c4_a050_s42_fp32/report/",
    "description": "Check recent analysis report structure"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-19T22:44:20.100815+00:00_

analysis_c4_a050_s42_fp32.md
analysis_c4_a050_s42_fp32_2bf704.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-19T22:44:22.911054+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/c4_a050_s42_fp32/report/analysis_c4_a050_s42_fp32_2bf704.md",
  "limit": "40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/c4_a050_s42_fp32/report/analysis_c4_a050_s42_fp32_2bf704.md",
    "limit": "40"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-19T22:44:22.961771+00:00_

1	# Analysis: c4_a050_s42_fp32
2	
3	**Date**: 2026-05-19
4	**Server**: westd-17855
5	**Precision**: fp32
6	**Parent (bf16)**: alpha_sweep_c4_a050_s42_bf16
7	
8	## Purpose
9	
10	Determine whether the bf16 parent's PermG fwd=0/8 at C4 α=0.50 is a precision artifact or a true blind zone.
11	
12	## Result Summary
13	
14	**Conclusion: bf16 precision artifact confirmed.** fp32 rerun yields PermG fwd=8/8, K≥4=8/8. C4 α=0.50 has strong causal lead-lag signal; bf16 completely masked it.
15	
16	## Training Completion
17	
18	- EXIT_CODE=0 (normal exit)
19	- 11 generations (gen 0–10)
20	- All metrics computed, sentinel written
21	
22	## Per-Generation Metrics
23	
24	| Gen | token_entropy | distinct_1 | distinct_2 | distinct_3 | perplexity | mauve | ece |
25	|-----|--------------|------------|------------|------------|------------|-------|-----|
26	| 0 | 3.109 | 0.1149 | 0.5570 | 0.8388 | 24.01 | 0.829 | 0.012 |
27	| 1 | 2.327 | 0.1162 | 0.5571 | 0.8363 | 53.65 | 0.876 | 0.166 |
28	| 2 | 2.024 | 0.0987 | 0.4830 | 0.7562 | 112.74 | 0.494 | 0.260 |
29	| 3 | 1.831 | 0.0955 | 0.4583 | 0.7134 | 188.29 | 0.450 | 0.311 |
30	| 4 | 1.725 | 0.0951 | 0.4460 | 0.6873 | 260.55 | 0.367 | 0.339 |
31	| 5 | 1.679 | 0.0971 | 0.4469 | 0.6781 | 331.59 | 0.382 | 0.353 |
32	| 6 | 1.650 | 0.0990 | 0.4511 | 0.6785 | 407.93 | 0.420 | 0.364 |
33	| 7 | 1.626 | 0.1007 | 0.4579 | 0.6801 | 480.53 | 0.393 | 0.375 |
34	| 8 | 1.617 | 0.1020 | 0.4634 | 0.6858 | 559.26 | 0.402 | 0.383 |
35	| 9 | 1.610 | 0.1035 | 0.4698 | 0.6934 | 637.24 | 0.377 | 0.387 |
36	| 10 | 1.617 | 0.1037 | 0.4695 | 0.6899 | 727.95 | 0.379 | 0.390 |
37	
38	## Drift (gen 0 → gen 10)
39	
40	| Metric | gen 0 | gen 10 | Δ% |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-19T22:44:39.303554+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Find analysis scripts",
  "subagent_type": "Explore",
  "prompt": "In the repository at /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/, find the Python analysis scripts used for MMCT 5-method lead-lag analysis. Look for files like run_5method.py, batch_analysis.py, or any script that computes PermG, K≥3, K≥4 metrics. I need to know:\n1. The exact file paths of the analysis scripts\n2. How they are invoked (command line arguments)\n3. Whether they include D111 direction checking\n\nSearch breadth: medium"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Agent",
  "tool_args": {
    "description": "Find analysis scripts",
    "subagent_type": "Explore",
    "prompt": "In the repository at /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/, find the Python analysis scripts used for MMCT 5-method lead-lag analysis. Look for files like run_5method.py, batch_analysis.py, or any script that computes PermG, K≥3, K≥4 metrics. I need to know:\n1. The exact file paths of the analysis scripts\n2. How they are invoked (command line arguments)\n3. Whether they include D111 direction checking\n\nSearch breadth: medium"
  }
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-19T22:44:41.462712+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.py",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-19T22:44:41.664495+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/prepare_data.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analyze_mvp.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/test_alpha_sweep.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/bootstrap_ty_validation.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/detrending_utils.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/data/permutation_granger.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/permutation_granger.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analyze_extended.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/cross_alpha_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/data/cross_alpha_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/data/consensus_framework.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/cross_alpha_analysis_v4.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analysis/cross_alpha/cross_alpha_analysis_v4.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/consensus_framework.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analysis/consensus_framework/consensus_framework.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/scripts/plot_regime_map.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/scripts/plot_consensus_workflow.py
/home/ubuntu/.
…[truncated 1167 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Glob",
  "elapsed_ms": 201
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-19T22:44:42.168209+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "run_5method|batch_analysis|PermG|K≥3|K≥4",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "type": "py",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Grep",
  "tool_args": {
    "pattern": "run_5method|batch_analysis|PermG|K≥3|K≥4",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
    "type": "py",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-19T22:44:42.319426+00:00_

Found 2 files
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/figures/paper/gen_dose_response.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/figures/paper/gen_consensus_heatmap.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Grep",
  "elapsed_ms": 151
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-19T22:44:42.420233+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "D111|direction.*check",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "type": "py",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Grep",
  "tool_args": {
    "pattern": "D111|direction.*check",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
    "type": "py",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-19T22:44:42.470958+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-19T22:44:45.181734+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "5.*method|five.*method|MMCT|lead.*lag",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "type": "py",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Grep",
  "tool_args": {
    "pattern": "5.*method|five.*method|MMCT|lead.*lag",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
    "type": "py",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-19T22:44:45.483485+00:00_

Found 8 files
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/figures/paper/gen_dose_response.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/figures/paper/gen_consensus_heatmap.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/scripts/gen_single_method_table.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analysis/cross_alpha/cross_alpha_analysis_v4.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/cross_alpha_analysis_v4.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/data/cross_alpha_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/cross_alpha_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analyze_mvp.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Grep",
  "elapsed_ms": 301
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-19T22:44:45.484791+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -name \"*5method*\" -o -name \"*run_*\" -o -name \"*batch*\" 2>/dev/null | grep -E \"\\.py$\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -name \"*5method*\" -o -name \"*run_*\" -o -name \"*batch*\" 2>/dev/null | grep -E \"\\.py$\""
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-19T22:44:45.536428+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/lag_sensitivity/run_lag_sensitivity.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-19T22:44:48.748286+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/figures/paper/gen_dose_response.py",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/figures/paper/gen_dose_response.py",
    "limit": "100"
  }
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-19T22:44:48.748788+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/figures/paper/gen_consensus_heatmap.py",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/figures/paper/gen_consensus_heatmap.py",
    "limit": "100"
  }
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-19T22:44:48.749084+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/scripts/gen_single_method_table.py",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/scripts/gen_single_method_table.py",
    "limit": "100"
  }
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-19T22:44:48.799712+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analyze_mvp.py",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analyze_mvp.py",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-19T22:44:48.800296+00:00_

1	#!/usr/bin/env python3
2	"""Dose-response figure: Single panel — PermG fwd detection rate with 4-regime bands."""
3	
4	import matplotlib
5	matplotlib.use('Agg')
6	import matplotlib.pyplot as plt
7	import numpy as np
8	import csv
9	import sys
10	import os
11	
12	plt.rcParams.update({
13	    'font.family': 'DejaVu Sans',
14	    'font.size': 11,
15	    'axes.titlesize': 12,
16	    'axes.labelsize': 11,
17	    'xtick.labelsize': 10,
18	    'ytick.labelsize': 10,
19	    'legend.fontsize': 9,
20	    'figure.dpi': 300,
21	    'savefig.dpi': 300,
22	    'savefig.bbox': 'tight',
23	    'savefig.pad_inches': 0.05,
24	    'axes.spines.top': False,
25	    'axes.spines.right': False,
26	    'lines.linewidth': 1.8,
27	})
28	
29	csv_path = sys.argv[1] if len(sys.argv) > 1 else 'dose_response_5method_regime.csv'
30	out_dir = sys.argv[2] if len(sys.argv) > 2 else '.'
31	
32	rows = []
33	with open(csv_path) as f:
34	    reader = csv.DictReader(f)
35	    for r in reader:
36	        if 'RUNNING' in r.get('regime', ''):
37	            continue
38	        rows.append(r)
39	
40	alphas = np.array([float(r['alpha']) for r in rows])
41	permG = np.array([float(r['permG_fwd_rate']) for r in rows])
42	regimes = [r['regime'] for r in rows]
43	
44	n = len(alphas)
45	x_idx = np.arange(n)
46	alpha_labels = [f'{a:.2f}' for a in alphas]
47	
48	regime_map = {}
49	for i, reg in enumerate(regimes):
50	    regime_map.setdefault(reg, []).append(i)
51	
52	fig, ax = plt.subplots(figsize=(7.0, 3.2))
53	
54	# 4-regime background bands
55	null_end = max(regime_map.get('null', [0])) + 0.5
56	onset_indices = regime_map.get('onset', [])
57	onset_start = min(onset_indices) - 0.5 if onset_indices else null_end
58	onset_end = max(onset_indices) + 0.5 if onset_indices else null_end
59	sync_indices = regime_map.get('sync_collapse', [])
60	sync_start = min(sync_indices) - 0.5 if sync_indices else onset_end
61	sync_end = max(sync_indices) + 0.5 if sync_indices else onset_end
62	det_indices = regime_map.get('detection'
…[truncated 1710 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-19T22:44:48.800687+00:00_

1	"""Generate Single-Method Error Consequence table from 5method_leadlag.json files."""
2	import json
3	import os
4	import glob
5	
6	BASE = "/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep"
7	
8	files = sorted(glob.glob(os.path.join(BASE, "a*_s*/analysis/5method_leadlag.json")))
9	
10	METHOD_KEYS = ["naive_xcorr", "diff_xcorr", "threshold_onset", "perm_granger", "ty_granger"]
11	METHOD_LABELS = {
12	    "naive_xcorr": "Naive XCorr",
13	    "diff_xcorr": "Diff XCorr (FDR)",
14	    "threshold_onset": "Threshold Onset",
15	    "perm_granger": "Perm Granger (FDR)",
16	    "ty_granger": "TY Granger",
17	}
18	
19	def get_sig(method_data, method_key):
20	    if method_key in ("diff_xcorr", "perm_granger"):
21	        return method_data.get("significant_fdr", method_data.get("significant", False))
22	    return method_data.get("significant", False)
23	
24	results = {}
25	data_sources = {}
26	
27	for f in files:
28	    with open(f) as fh:
29	        d = json.load(fh)
30	    if "meta" in d:
31	        alpha = d["meta"]["alpha"]
32	        seed = d["meta"]["seed"]
33	    else:
34	        alpha = d["alpha"]
35	        seed = d["seed"]
36	    alpha_str = f"a{int(alpha*100):03d}"
37	    key = (alpha_str, seed)
38	    data_sources[key] = f
39	
40	    method_sig = {m: 0 for m in METHOD_KEYS}
41	    n_pairs = len(d["pairs"])
42	
43	    for pair in d["pairs"]:
44	        fwd = pair["forward"]
45	        for m in METHOD_KEYS:
46	            if m in fwd and isinstance(fwd[m], dict) and get_sig(fwd[m], m):
47	                method_sig[m] += 1
48	
49	    results[key] = {"method_sig": method_sig, "n_pairs": n_pairs}
50	
51	ALPHAS = ["a000", "a025", "a050", "a075", "a100"]
52	ALPHA_LABELS = {"a000": "0.00", "a025": "0.25", "a050": "0.50", "a075": "0.75", "a100": "1.00"}
53	
54	print("=" * 80)
55	print("Per-seed, per-method forward significant pair counts (out of 8)")
56	print("=" * 80)
57	
58	for alpha in ALPHAS:
59	    seeds = sorted([k[1] for k in results if k[0] == alpha])
…[truncated 1372 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-19T22:44:48.802507+00:00_

1	#!/usr/bin/env python3
2	"""Consensus heatmap: 7 rows (5 methods + K≥3 + K≥4) × 11 α values."""
3	
4	import matplotlib
5	matplotlib.use('Agg')
6	import matplotlib.pyplot as plt
7	import matplotlib.colors as mcolors
8	import numpy as np
9	import csv
10	import sys
11	import os
12	
13	plt.rcParams.update({
14	    'font.family': 'DejaVu Sans',
15	    'font.size': 11,
16	    'axes.titlesize': 12,
17	    'axes.labelsize': 11,
18	    'xtick.labelsize': 9.5,
19	    'ytick.labelsize': 10,
20	    'legend.fontsize': 9,
21	    'figure.dpi': 300,
22	    'savefig.dpi': 300,
23	    'savefig.bbox': 'tight',
24	    'savefig.pad_inches': 0.05,
25	})
26	
27	csv_path = sys.argv[1] if len(sys.argv) > 1 else 'consensus_heatmap_data.csv'
28	out_dir = sys.argv[2] if len(sys.argv) > 2 else '.'
29	
30	rows = []
31	with open(csv_path) as f:
32	    reader = csv.DictReader(f)
33	    for r in reader:
34	        rows.append(r)
35	
36	alphas = [float(r['alpha']) for r in rows]
37	n = len(alphas)
38	alpha_labels = [f'{a:.2f}' for a in alphas]
39	
40	method_keys = ['naive_rate', 'diff_rate', 'threshold_rate', 'permG_rate', 'TY_rate', 'K3_rate', 'K4_rate']
41	method_labels = ['Naive XCorr', 'Diff. XCorr', 'Threshold (3σ)', 'Perm. Granger', 'Toda–Yamamoto',
42	                  '$K{\\geq}3$ consensus', '$K{\\geq}4$ consensus']
43	
44	data = np.array([[float(r[k]) for r in rows] for k in method_keys]) * 100
45	regimes = [r['regime'] for r in rows]
46	
47	fig, ax = plt.subplots(figsize=(7.5, 3.8))
48	
49	cmap = plt.cm.YlOrRd
50	im = ax.imshow(data, cmap=cmap, aspect='auto', vmin=0, vmax=100, interpolation='nearest')
51	
52	for i in range(len(method_labels)):
53	    for j in range(n):
54	        val = data[i, j]
55	        color = 'white' if val > 65 else 'black'
56	        ax.text(j, i, f'{val:.0f}', ha='center', va='center',
57	                fontsize=7.5, color=color, fontweight='bold' if val >= 75 else 'normal')
58	
59	ax.set_yticks(range(len(method_labels)))
60	ax.set_yticklabels(method_labels)
6
…[truncated 1830 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Read",
  "elapsed_ms": 53
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-19T22:44:48.802860+00:00_

1	"""Analyze MVP experiment: metric trends, cross-correlation, lead time.
2	
3	Reads all_metrics.json from each rep, produces:
4	  - metric_trends.png : canary + downstream metrics vs generation
5	  - cross_correlation.png : cross-correlation heatmap
6	  - lead_time_table.csv : lead time estimates per canary-downstream pair
7	  - analysis_summary.json : machine-readable summary with graded verdict
8	
9	Evaluation pipeline (per mvp_evaluation_criteria.md):
10	  1. MAUVE floor effect detection (§4) — demote if Gen 0 < 0.10 and CV < 0.50
11	  2. effective_rank monotonicity check (§3) — Gen 4-9 OLS slope consistency
12	  3. Permutation test (§1) — per-triplet significance via 10k permutations
13	  4. Per-seed significance filtering (§2) — 3/3 consistency requirement
14	  5. Graded verdict (§5) — STRONG PASS / PASS / CONDITIONAL PASS / FAIL
15	  6. Lag dispersion statistics — mean, std, min, max per consistent pair
16	
17	Usage:
18	    python analyze_mvp.py --results_dir results/mvp --seeds 42 43 44
19	    python analyze_mvp.py --results_dir results/mvp --n_permutations 5000
20	"""
21	
22	import argparse
23	import json
24	import os
25	import sys
26	
27	import matplotlib.pyplot as plt
28	import numpy as np
29	import pandas as pd
30	
31	
32	CANARY_METRICS = ["token_entropy", "self_bleu", "ece", "effective_rank"]
33	DOWNSTREAM_METRICS = ["perplexity", "distinct_1", "distinct_2", "distinct_3", "mauve"]
34	
35	HIGHER_IS_WORSE = {"self_bleu", "ece", "perplexity"}
36	LOWER_IS_WORSE = {"token_entropy", "effective_rank", "distinct_1", "distinct_2",
37	                   "distinct_3", "mauve"}
38	
39	
40	def load_metrics(results_dir, seeds):
41	    """Load all_metrics.json from each rep, return dict {seed: [metrics_per_gen]}."""
42	    data = {}
43	    for seed in seeds:
44	        path = os.path.join(results_dir, f"rep_{seed}", "all_metrics.json")
45	        with open(path) as f:
46	            data[seed] = json.load(f)
47	    return data
48	
49	
50	def metrics_to_df(data):
51	  
…[truncated 1869 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Read",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-19T22:44:51.864303+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -type f -name \"*.py\" | xargs grep -l \"PermG\\|permG\\|permutation.*granger\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -type f -name \"*.py\" | xargs grep -l \"PermG\\|permG\\|permutation.*granger\" 2>/dev/null | head -20"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-19T22:44:52.216286+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/figures/paper/gen_dose_response.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/figures/paper/gen_consensus_heatmap.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/cross_alpha_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/data/cross_alpha_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/data/consensus_framework.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/data/permutation_granger.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/cross_alpha_analysis_v4.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analyze_extended.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/lag_sensitivity/run_lag_sensitivity.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/permutation_granger.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analysis/cross_alpha/cross_alpha_analysis_v4.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analysis/consensus_framework/consensus_framework.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/consensus_framework.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "elapsed_ms": 351
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-19T22:44:52.267060+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -type f -name \"*.py\" | xargs grep -l \"K3\\|K4\\|K.*≥\\|consensus\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -type f -name \"*.py\" | xargs grep -l \"K3\\|K4\\|K.*≥\\|consensus\" 2>/dev/null | head -20"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-19T22:44:52.368057+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/figures/paper/gen_consensus_heatmap.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/scripts/plot_consensus_workflow.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/scripts/plot_regime_map.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/scripts/gen_single_method_table.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/data/consensus_framework.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/figures/plot_regime_map.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/cross_alpha_analysis_v4.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analysis/cross_alpha/cross_alpha_analysis_v4.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analysis/consensus_framework/consensus_framework.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/consensus_framework.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-19T22:44:54.043333+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/cross_alpha_analysis.py",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/cross_alpha_analysis.py",
    "limit": "150"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-19T22:44:54.294781+00:00_

1	"""Cross-alpha analysis for distributional canary collapse experiments.
2	
3	Scans results/alpha_sweep/a*_s42/ directories, computes:
4	  1. Dose-response table (gen0→genN drift% per metric per α)
5	  2. Bidirectional permutation Granger causality with BH FDR correction
6	  3. Cross-correlation lead-lag analysis (Δmetric pairs)
7	  4. Per-generation velocity analysis for distinct_1
8	
9	Input:  results/alpha_sweep/a{NNN}_s42/all_metrics.json
10	Output: results/analysis/cross_alpha_v{VERSION}.json + terminal summary
11	
12	Dependencies: numpy, scipy, pandas, statsmodels
13	"""
14	
15	import argparse
16	import glob
17	import json
18	import os
19	import re
20	import sys
21	from datetime import datetime
22	
23	import numpy as np
24	from statsmodels.stats.multitest import multipletests
25	
26	
27	# ---------------------------------------------------------------------------
28	# Data loading
29	# ---------------------------------------------------------------------------
30	
31	BASE_DIR = os.path.dirname(os.path.abspath(__file__))
32	SWEEP_DIR = os.path.join(BASE_DIR, "results", "alpha_sweep")
33	ANALYSIS_DIR = os.path.join(BASE_DIR, "results", "analysis")
34	
35	METRICS = ["distinct_1", "distinct_2", "distinct_3", "token_entropy", "ece", "perplexity"]
36	
37	# Granger test pairs: (cause, effect, label)
38	GRANGER_PAIRS = [
39	    ("token_entropy", "distinct_1", "entropy→d1"),
40	    ("ece",           "distinct_1", "ECE→d1"),
41	    ("token_entropy", "distinct_2", "entropy→d2"),
42	    ("ece",           "distinct_2", "ECE→d2"),
43	    ("distinct_1", "token_entropy", "d1→entropy"),
44	    ("distinct_1", "ece",           "d1→ECE"),
45	    ("distinct_2", "token_entropy", "d2→entropy"),
46	    ("distinct_2", "ece",           "d2→ECE"),
47	]
48	
49	XCORR_PAIRS = [
50	    ("token_entropy", "distinct_1", "entropy_vs_d1"),
51	    ("ece",           "distinct_1", "ece_vs_d1"),
52	]
53	
54	
55	def discover_alpha_dirs(explicit=None):
56	    """Find alpha experiment directories. Ret
…[truncated 3707 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-19T22:44:54.295174+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/consensus_framework.py",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/consensus_framework.py",
    "limit": "150"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-19T22:44:54.446073+00:00_

1	"""
2	Multi-method consensus framework for canary→downstream association robustness.
3	
4	Formalizes "robust association": a pair is robust only when ≥method_threshold
5	independent statistical methods agree (each requiring ≥seed_threshold seeds
6	significant). Two-stage aggregation: seed→method verdict, then method→consensus.
7	
8	Input:  results/mvp/analysis/method_ablation.json
9	Output: consensus classification, sensitivity heatmap, FPR/FNR table (JSON)
10	
11	Dependencies: numpy, json (stdlib)
12	"""
13	
14	import json
15	import os
16	
17	import numpy as np
18	
19	METHOD_NAMES = [
20	    "naive_pearson",
21	    "differenced_xcorr",
22	    "threshold_onset",
23	    "toda_yamamoto",
24	    "permutation_granger",
25	]
26	
27	# differenced_xcorr is the FP ground truth (index 1)
28	DIFF_INDEX = 1
29	
30	
31	def _to_native(obj):
32	    """Convert numpy types to Python native for JSON serialization."""
33	    if isinstance(obj, (np.integer,)):
34	        return int(obj)
35	    if isinstance(obj, (np.floating,)):
36	        return float(obj)
37	    if isinstance(obj, (np.bool_,)):
38	        return bool(obj)
39	    if isinstance(obj, np.ndarray):
40	        return obj.tolist()
41	    return obj
42	
43	
44	class NumpyEncoder(json.JSONEncoder):
45	    """JSON encoder that handles numpy types."""
46	    def default(self, obj):
47	        native = _to_native(obj)
48	        if native is not obj:
49	            return native
50	        return super().default(obj)
51	
52	
53	def load_sig_matrix(ablation_path, apply_fdr=True):
54	    """
55	    Load method_ablation.json into a boolean significance tensor.
56	
57	    Args:
58	        ablation_path: path to method_ablation.json
59	
60	    Returns:
61	        sig_matrix: np.ndarray, shape (5, 16, 4), dtype bool
62	                    axes = (method, pair, seed)
63	        pair_names: list of (canary, downstream) tuples, len 16
64	        method_names: list of str, len 5
65	        seeds: list of int, e.g. [42, 43, 44, 45]
66	 
…[truncated 3445 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-19T22:44:54.547071+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/permutation_granger.py",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/permutation_granger.py",
    "limit": "150"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-19T22:44:54.547687+00:00_

1	"""Permutation-based Granger causality test.
2	
3	Uses permutation to build a null distribution of the Granger F-statistic,
4	avoiding asymptotic assumptions that fail on short series (T<20).
5	First-differences the series to handle non-stationarity, then uses random
6	shuffle (not circular shift) since differencing removes autocorrelation.
7	"""
8	
9	import numpy as np
10	
11	
12	def _build_lag_matrix(y, x, max_lag):
13	    """Build design matrices for restricted and unrestricted Granger models."""
14	    T = len(y)
15	    n = T - max_lag
16	    Y = y[max_lag:]
17	
18	    cols_r = [np.ones(n)]
19	    for lag in range(1, max_lag + 1):
20	        cols_r.append(y[max_lag - lag: T - lag])
21	
22	    cols_u = list(cols_r)
23	    for lag in range(1, max_lag + 1):
24	        cols_u.append(x[max_lag - lag: T - lag])
25	
26	    X_r = np.column_stack(cols_r)
27	    X_u = np.column_stack(cols_u)
28	    return Y, X_r, X_u
29	
30	
31	def _granger_f_stat(y, x, max_lag):
32	    """Compute Granger F-statistic: does x help predict y beyond y's own lags?"""
33	    Y, X_r, X_u = _build_lag_matrix(y, x, max_lag)
34	    n = len(Y)
35	    q = max_lag
36	
37	    try:
38	        beta_r = np.linalg.lstsq(X_r, Y, rcond=None)[0]
39	        beta_u = np.linalg.lstsq(X_u, Y, rcond=None)[0]
40	    except np.linalg.LinAlgError:
41	        return np.nan
42	
43	    rss_r = np.sum((Y - X_r @ beta_r) ** 2)
44	    rss_u = np.sum((Y - X_u @ beta_u) ** 2)
45	
46	    k_u = X_u.shape[1]
47	    df_resid = n - k_u
48	
49	    if df_resid <= 0 or rss_u < 1e-15:
50	        return np.nan
51	
52	    F = ((rss_r - rss_u) / q) / (rss_u / df_resid)
53	    return F
54	
55	
56	def permutation_granger_test(x, y, max_lag=1, n_perm=1000, seed=42,
57	                              difference=True):
58	    """Permutation-based Granger causality test.
59	
60	    Tests whether x Granger-causes y using permutation null distribution.
61	    First-differences series by default to handle non-stationarity, then
62	    uses rand
…[truncated 3238 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-19T22:44:57.608454+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -type f -name \"*.py\" | xargs grep -l \"5method\\|five.method\\|run.*analysis\\|main.*analysis\" 2>/dev/null | grep -v __pycache__"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -type f -name \"*.py\" | xargs grep -l \"5method\\|five.method\\|run.*analysis\\|main.*analysis\" 2>/dev/null | grep -v __pycache__"
  }
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-19T22:44:57.711446+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"D111\\|direction\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse --include=\"*.py\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"D111\\|direction\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse --include=\"*.py\" 2>/dev/null | head -20"
  }
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-19T22:44:57.711891+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/figures/paper/gen_dose_response.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/scripts/gen_single_method_table.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "elapsed_ms": 103
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-19T22:44:57.762381+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/scripts/plot_regime_map.py:                label = DIRECTION_TO_LABEL.get(entry['direction'])
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/cross_alpha_analysis.py:  2. Bidirectional permutation Granger causality with BH FDR correction
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/cross_alpha_analysis.py:    """Run bidirectional Granger for all α × all pairs. Returns list of result dicts."""
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/cross_alpha_analysis.py:                "direction": label,
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/cross_alpha_analysis.py:    print(f"\n{'GRANGER CAUSALITY (bidirectional, differenced, permutation)'}")
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/cross_alpha_analysis.py:    directions = list(dict.fromkeys(r["direction"] for r in gc))
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/cross_alpha_analysis.py:    for d in directions:
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/cross_alpha_analysis.py:            match = [r for r in gc if r["alpha_key"] == ak and r["direction"] == d]
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/cross_alpha_analysis.py:    print(f"\nRunning bidirectional Granger ({len(GRANGER_PAIRS)} pairs × {len(all_data)} alphas, "
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/bootstrap_ty_validation.py:statistical power (under H1: VAR(2) with unidirectional causality) for
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/bootstrap_ty_validation.py:    """Run TY Granger causality test (x -> y direction).
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts
…[truncated 1672 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-19T22:44:59.720827+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/cross_alpha_analysis.py",
  "offset": "150",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/cross_alpha_analysis.py",
    "offset": "150",
    "limit": "200"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-19T22:45:00.073564+00:00_

150	
151	
152	def permutation_granger_test(x, y, max_lag=1, n_perm=5000, seed=42, difference=True):
153	    """Permutation-based Granger causality: does x Granger-cause y?"""
154	    x = np.asarray(x, dtype=float)
155	    y = np.asarray(y, dtype=float)
156	    if difference:
157	        x, y = np.diff(x), np.diff(y)
158	    T = len(x)
159	    if T <= max_lag + 2:
160	        return {"f_stat": None, "p_raw": None, "note": f"Series too short: T={T}"}
161	
162	    f_obs = _granger_f_stat(y, x, max_lag)
163	    if np.isnan(f_obs):
164	        return {"f_stat": None, "p_raw": None, "note": "F-stat computation failed"}
165	
166	    # Effect size f²
167	    Y, X_r, X_u = _build_lag_matrix(y, x, max_lag)
168	    rss_r = np.sum((Y - X_r @ np.linalg.lstsq(X_r, Y, rcond=None)[0]) ** 2)
169	    rss_u = np.sum((Y - X_u @ np.linalg.lstsq(X_u, Y, rcond=None)[0]) ** 2)
170	    f2 = (rss_r - rss_u) / rss_u if rss_u > 1e-15 else None
171	
172	    rng = np.random.default_rng(seed)
173	    null_f = np.empty(n_perm)
174	    for i in range(n_perm):
175	        null_f[i] = _granger_f_stat(y, rng.permutation(x), max_lag)
176	    valid = null_f[~np.isnan(null_f)]
177	    if len(valid) == 0:
178	        return {"f_stat": round(float(f_obs), 4), "p_raw": None, "note": "All permutations failed"}
179	
180	    p_value = (np.sum(valid >= f_obs) + 1) / (len(valid) + 1)
181	    return {
182	        "f_stat": round(float(f_obs), 4),
183	        "p_raw": round(float(p_value), 6),
184	        "n_perm": n_perm,
185	        "effect_size_f2": round(float(f2), 4) if f2 is not None else None,
186	    }
187	
188	
189	def run_granger_all(all_data, max_lag=1, n_perms=5000):
190	    """Run bidirectional Granger for all α × all pairs. Returns list of result dicts."""
191	    results = []
192	    for alpha_key, alpha_val, metrics_list in all_data:
193	        for cause_key, effect_key, label in GRANGER_PAIRS:
194	            x = extract_series(metrics_list, cause_key)
195	            y = extract_series(metrics_l
…[truncated 6492 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-19T22:45:00.124397+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -path \"*analysis*\" -name \"*.py\" | grep -E \"5method|five|consensus|framework\" | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -path \"*analysis*\" -name \"*.py\" | grep -E \"5method|five|consensus|framework\" | head -10"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-19T22:45:00.175141+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analysis/consensus_framework/consensus_framework.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-19T22:45:02.136992+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -type f -name \"*.py\" | xargs grep -l \"5method_leadlag\\|five.*method.*lead\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -type f -name \"*.py\" | xargs grep -l \"5method_leadlag\\|five.*method.*lead\" 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-19T22:45:02.237863+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/scripts/gen_single_method_table.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-19T22:45:02.489291+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/cross_alpha_analysis.py",
  "offset": "350",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/cross_alpha_analysis.py",
    "offset": "350",
    "limit": "150"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-19T22:45:02.489732+00:00_

350	        line = f"{d:<20}"
351	        for ak in alpha_keys:
352	            match = [r for r in gc if r["alpha_key"] == ak and r["direction"] == d]
353	            if match:
354	                r = match[0]
355	                p_raw = f"{r['p_raw']:.4f}" if r.get("p_raw") is not None else "  N/A "
356	                p_fdr = f"{r.get('p_fdr', 'N/A')}" if r.get("p_fdr") is not None else "  N/A "
357	                if isinstance(p_fdr, float):
358	                    p_fdr = f"{p_fdr:.4f}"
359	                sig = "*" if r.get("p_fdr") is not None and r["p_fdr"] < 0.05 else " "
360	                fp = "FP?" if r.get("note", "").startswith("consistent") else "   "
361	                line += f" | {p_raw} {p_fdr:>7} {sig}{fp}"
362	            else:
363	                line += f" |    --       --     "
364	        print(line)
365	
366	    # FDR summary
367	    valid = [r for r in gc if r.get("p_raw") is not None]
368	    n_total = len(valid)
369	    n_raw_sig = sum(1 for r in valid if r["p_raw"] < 0.05)
370	    n_fdr_sig = sum(1 for r in valid if r.get("p_fdr") is not None and r["p_fdr"] < 0.05)
371	    print(f"\nFDR: {n_raw_sig}/{n_total} raw-sig → {n_fdr_sig}/{n_total} FDR-sig (BH correction across all {n_total} tests)")
372	
373	    # Cross-correlation
374	    xcorr = output["cross_correlation"]
375	    print(f"\n{'CROSS-CORRELATION (Δmetric, peak lag)'}")
376	    print("-" * 60)
377	    for pair_label in ["entropy_vs_d1", "ece_vs_d1"]:
378	        line = f"  {pair_label:<18}"
379	        for ak in sorted(xcorr.keys()):
380	            p = xcorr[ak].get(pair_label, {})
381	            line += f" | α={xcorr[ak]['alpha']}: lag={p.get('peak_lag','?'):>2} r={p.get('peak_r','?'):>7}"
382	        print(line)
383	
384	    # Velocity
385	    vel = output["per_gen_velocity"]
386	    print(f"\n{'D1 VELOCITY'}")
387	    print("-" * 60)
388	    for ak in sorted(vel.keys()):
389	        v = vel[ak]
390	        decel = f"{v['deceleration_ratio']:.2f}" if v.get("deceleration_
…[truncated 4384 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-19T22:45:05.060011+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/scripts/gen_single_method_table.py",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/scripts/gen_single_method_table.py",
    "limit": "200"
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-19T22:45:05.261609+00:00_

1	"""Generate Single-Method Error Consequence table from 5method_leadlag.json files."""
2	import json
3	import os
4	import glob
5	
6	BASE = "/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep"
7	
8	files = sorted(glob.glob(os.path.join(BASE, "a*_s*/analysis/5method_leadlag.json")))
9	
10	METHOD_KEYS = ["naive_xcorr", "diff_xcorr", "threshold_onset", "perm_granger", "ty_granger"]
11	METHOD_LABELS = {
12	    "naive_xcorr": "Naive XCorr",
13	    "diff_xcorr": "Diff XCorr (FDR)",
14	    "threshold_onset": "Threshold Onset",
15	    "perm_granger": "Perm Granger (FDR)",
16	    "ty_granger": "TY Granger",
17	}
18	
19	def get_sig(method_data, method_key):
20	    if method_key in ("diff_xcorr", "perm_granger"):
21	        return method_data.get("significant_fdr", method_data.get("significant", False))
22	    return method_data.get("significant", False)
23	
24	results = {}
25	data_sources = {}
26	
27	for f in files:
28	    with open(f) as fh:
29	        d = json.load(fh)
30	    if "meta" in d:
31	        alpha = d["meta"]["alpha"]
32	        seed = d["meta"]["seed"]
33	    else:
34	        alpha = d["alpha"]
35	        seed = d["seed"]
36	    alpha_str = f"a{int(alpha*100):03d}"
37	    key = (alpha_str, seed)
38	    data_sources[key] = f
39	
40	    method_sig = {m: 0 for m in METHOD_KEYS}
41	    n_pairs = len(d["pairs"])
42	
43	    for pair in d["pairs"]:
44	        fwd = pair["forward"]
45	        for m in METHOD_KEYS:
46	            if m in fwd and isinstance(fwd[m], dict) and get_sig(fwd[m], m):
47	                method_sig[m] += 1
48	
49	    results[key] = {"method_sig": method_sig, "n_pairs": n_pairs}
50	
51	ALPHAS = ["a000", "a025", "a050", "a075", "a100"]
52	ALPHA_LABELS = {"a000": "0.00", "a025": "0.25", "a050": "0.50", "a075": "0.75", "a100": "1.00"}
53	
54	print("=" * 80)
55	print("Per-seed, per-method forward significant pair counts (out of 8)")
56	print("=" * 80)
57	
58	for alpha in ALPHAS:
59	    seeds = sorted([k[1] for k in results if k[0] == alpha])
…[truncated 4095 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-19T22:45:05.312650+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -type d -name \"analysis\" | head -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -type d -name \"analysis\" | head -5"
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-19T22:45:05.664982+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analysis

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "elapsed_ms": 352
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-19T22:45:05.665475+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -type f -name \"*.json\" -path \"*/5method*\" 2>/dev/null | head -3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -type f -name \"*.json\" -path \"*/5method*\" 2>/dev/null | head -3"
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-19T22:45:05.766202+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-19T22:45:08.058530+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -type f -name \"*.py\" | xargs grep -l \"5method_leadlag\\|naive_xcorr\\|diff_xcorr\\|threshold_onset\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -type f -name \"*.py\" | xargs grep -l \"5method_leadlag\\|naive_xcorr\\|diff_xcorr\\|threshold_onset\" 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-19T22:45:08.221076+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/scripts/gen_single_method_table.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/data/consensus_framework.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/cross_alpha_analysis_v4.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analysis/cross_alpha/cross_alpha_analysis_v4.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analysis/consensus_framework/consensus_framework.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/consensus_framework.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "elapsed_ms": 162
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-19T22:45:08.221553+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -type f -name \"*.py\" -path \"*/analysis/*\" | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -type f -name \"*.py\" -path \"*/analysis/*\" | head -10"
  }
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-19T22:45:08.333564+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analysis/cross_alpha/cross_alpha_analysis_v4.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analysis/consensus_framework/consensus_framework.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "elapsed_ms": 112
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-19T22:45:11.226477+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -type f \\( -name \"README*\" -o -name \"ANALYSIS*\" -o -name \"*.md\" \\) 2>/dev/null | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -type f \\( -name \"README*\" -o -name \"ANALYSIS*\" -o -name \"*.md\" \\) 2>/dev/null | head -10"
  }
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-19T22:45:11.277171+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/*.py 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/*.py 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-19T22:45:11.327862+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/IDEA_BRIEF.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/task_context/agent.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/task_context/director.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/task_context/reviewer.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/task_context/history/director/loop_3.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/task_context/history/director/loop_4.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/task_context/history/director/loop_7.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/task_context/history/director/loop_9.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/task_context/history/director/loop_6.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/task_context/history/director/loop_5.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-19T22:45:11.328327+00:00_

-rw-r--r-- 1 ubuntu ubuntu  8465 May 14 21:29 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/bootstrap_ty_validation.py
-rw-r--r-- 1 ubuntu ubuntu 23204 May 15 10:06 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/consensus_framework.py
-rw-r--r-- 1 ubuntu ubuntu 18765 May 15 06:43 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/cross_alpha_analysis.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-19T22:45:13.051880+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -type f -name \"*.py\" | xargs grep -l \"forward\\|backward\\|lead.*lag\" 2>/dev/null | grep -v __pycache__"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -type f -name \"*.py\" | xargs grep -l \"forward\\|backward\\|lead.*lag\" 2>/dev/null | grep -v __pycache__"
  }
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-19T22:45:13.270608+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/scripts/gen_single_method_table.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/cross_alpha_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analyze_mvp.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/data/cross_alpha_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/figures/plot_regime_map.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/cross_alpha_analysis_v4.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analysis/cross_alpha/cross_alpha_analysis_v4.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "elapsed_ms": 218
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-19T22:45:13.326599+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/results/analysis/ 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/results/analysis/ 2>/dev/null | head -20"
  }
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-19T22:45:13.379210+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "elapsed_ms": 52
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-19T22:45:15.276188+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -maxdepth 2 -name \"*.py\" -type f | sort"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -maxdepth 2 -name \"*.py\" -type f | sort"
  }
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-19T22:45:15.527283+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analyze_extended.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analyze_mvp.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/cross_alpha_analysis_v4.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/detrending_utils.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/iterative_train.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/metrics.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/permutation_granger.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/prepare_data.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/test_alpha_sweep.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/bootstrap_ty_validation.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/consensus_framework.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/cross_alpha_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/scripts/gen_single_method_table.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/scripts/plot_consensus_workflow.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/scripts/plot_regime_map.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "elapsed_ms": 251
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-19T22:45:15.578111+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"def.*5method\\|def.*five\\|def.*lead_lag\\|def.*leadlag\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse --include=\"*.py\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"def.*5method\\|def.*five\\|def.*lead_lag\\|def.*leadlag\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse --include=\"*.py\" 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-19T22:45:15.628749+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 107 · 2026-05-19T22:45:17.335451+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analyze_extended.py",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analyze_extended.py",
    "limit": "150"
  }
}
```

</details>

---

### Tool result

_source line 108 · 2026-05-19T22:45:17.487139+00:00_

1	# analyze_extended.py — Plan-006 extended 20-gen analysis
2	# Input:  results/extended_20gen/s{seed}/all_metrics.json
3	# Output: results/extended_20gen/analysis/{extended_analysis.json, summary.txt, mvp_comparison.json}
4	
5	import argparse
6	import json
7	import os
8	import sys
9	import warnings
10	from datetime import datetime
11	
12	import numpy as np
13	from scipy import stats
14	from statsmodels.stats.multitest import multipletests
15	from statsmodels.tsa.stattools import adfuller
16	
17	from permutation_granger import permutation_granger_test
18	from detrending_utils import detrend, cross_correlate, detrend_and_crosscorr
19	
20	warnings.filterwarnings("ignore")
21	
22	CANARY_METRICS = ["token_entropy", "ece"]
23	DOWNSTREAM_METRICS = ["distinct_1", "distinct_2", "distinct_3", "perplexity"]
24	HIGHER_IS_WORSE = {"self_bleu", "ece", "perplexity"}
25	LOWER_IS_WORSE = {"token_entropy", "effective_rank", "distinct_1", "distinct_2",
26	                   "distinct_3", "mauve"}
27	ALPHA_SIG = 0.05
28	N_PERM = 5000
29	
30	
31	# ── helpers ──────────────────────────────────────────────────────────────
32	
33	def load_metrics(path):
34	    """Load all_metrics.json, return sorted list of dicts."""
35	    with open(path) as f:
36	        data = json.load(f)
37	    return sorted(data, key=lambda m: m["generation"])
38	
39	
40	def extract(metrics_list, name):
41	    return np.array([m[name] for m in metrics_list])
42	
43	
44	def orient(series, name):
45	    return -series.copy() if name in LOWER_IS_WORSE else series.copy()
46	
47	
48	def cohen_r_label(r):
49	    r = abs(r)
50	    if r >= 0.5:   return "large"
51	    if r >= 0.3:   return "medium"
52	    if r >= 0.1:   return "small"
53	    return "negligible"
54	
55	
56	def cohen_f2_label(f2):
57	    if f2 is None: return "N/A"
58	    if f2 >= 0.35: return "large"
59	    if f2 >= 0.15: return "medium"
60	    if f2 >= 0.02: return "small"
61	    return "negligible"
62	
63	
64	def adf_order(series, max_d=2):
65	    for d in
…[truncated 3307 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---

### Tool call

_source line 109 · 2026-05-19T22:45:17.487701+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/bootstrap_ty_validation.py",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/bootstrap_ty_validation.py",
    "limit": "150"
  }
}
```

</details>

---

### Tool result

_source line 110 · 2026-05-19T22:45:17.488086+00:00_

1	"""Monte Carlo validation of Toda-Yamamoto Granger causality test under short T.
2	
3	Estimates Type I error rate (under H0: independent AR(1) processes) and
4	statistical power (under H1: VAR(2) with unidirectional causality) for
5	TY Granger tests at T ∈ {10, 15, 20, 30} and d_max ∈ {0, 1, adaptive}.
6	
7	Motivated by reviewer concern that T=10 (11 observations) may be too short
8	for reliable TY inference in the distrib_canary_collapse project.
9	"""
10	
11	import json
12	import os
13	import warnings
14	from itertools import product
15	
16	import numpy as np
17	from scipy import stats
18	from statsmodels.tsa.stattools import adfuller
19	
20	warnings.filterwarnings("ignore")
21	
22	ALPHA = 0.05
23	N_SIM = 1000
24	T_VALUES = [10, 15, 20, 30]
25	DMAX_OPTIONS = [0, 1, "adaptive"]
26	SEED_BASE = 20260514
27	
28	
29	def _adf_order(series, max_d=2):
30	    """Determine integration order via sequential ADF tests."""
31	    for d in range(max_d + 1):
32	        s = series.copy()
33	        for _ in range(d):
34	            s = np.diff(s)
35	        if len(s) < 5:
36	            return d
37	        try:
38	            if adfuller(s, maxlag=1, autolag=None)[1] < 0.05:
39	                return d
40	        except Exception:
41	            pass
42	    return max_d
43	
44	
45	def generate_h0(T, phi=0.8, sigma=0.1, rng=None):
46	    """H0 DGP: two independent AR(1) processes."""
47	    if rng is None:
48	        rng = np.random.default_rng()
49	    n = T + 1
50	    x = np.zeros(n)
51	    y = np.zeros(n)
52	    x[0] = rng.normal(0, sigma / np.sqrt(1 - phi**2))
53	    y[0] = rng.normal(0, sigma / np.sqrt(1 - phi**2))
54	    for t in range(1, n):
55	        x[t] = phi * x[t - 1] + rng.normal(0, sigma)
56	        y[t] = phi * y[t - 1] + rng.normal(0, sigma)
57	    return x, y
58	
59	
60	def generate_h1(T, phi=0.8, beta_cause=0.3, sigma=0.1, rng=None):
61	    """H1 DGP: VAR(2) with x -> y at lag 1, no reverse causality."""
62	    if rng is None:
63	        rng = np.random.default
…[truncated 2588 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 111 · 2026-05-19T22:45:21.155497+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"K.*≥.*3\\|K.*>=.*3\\|K3\\|K4\\|K≥4\\|K>=4\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse --include=\"*.py\" 2>/dev/null | head -15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"K.*≥.*3\\|K.*>=.*3\\|K3\\|K4\\|K≥4\\|K>=4\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse --include=\"*.py\" 2>/dev/null | head -15"
  }
}
```

</details>

---

### Tool result

_source line 112 · 2026-05-19T22:45:21.206136+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/figures/paper/gen_consensus_heatmap.py:"""Consensus heatmap: 7 rows (5 methods + K≥3 + K≥4) × 11 α values."""
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/figures/paper/gen_consensus_heatmap.py:method_keys = ['naive_rate', 'diff_rate', 'threshold_rate', 'permG_rate', 'TY_rate', 'K3_rate', 'K4_rate']
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/figures/paper/gen_consensus_heatmap.py:# Highlight K≥4 peak at α=0.60
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/scripts/gen_single_method_table.py:print(f"  {'Consensus (K>=3)':<25} " + " ".join(row))
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/scripts/gen_single_method_table.py:    print(f"    {'Consensus (K>=3)':<25}: {consensus_verdicts.get(alpha)}")

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 113 · 2026-05-19T22:45:23.162536+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/figures/paper/gen_consensus_heatmap.py",
  "offset": "30",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/figures/paper/gen_consensus_heatmap.py",
    "offset": "30",
    "limit": "150"
  }
}
```

</details>

---

### Tool result

_source line 114 · 2026-05-19T22:45:23.213339+00:00_

30	rows = []
31	with open(csv_path) as f:
32	    reader = csv.DictReader(f)
33	    for r in reader:
34	        rows.append(r)
35	
36	alphas = [float(r['alpha']) for r in rows]
37	n = len(alphas)
38	alpha_labels = [f'{a:.2f}' for a in alphas]
39	
40	method_keys = ['naive_rate', 'diff_rate', 'threshold_rate', 'permG_rate', 'TY_rate', 'K3_rate', 'K4_rate']
41	method_labels = ['Naive XCorr', 'Diff. XCorr', 'Threshold (3σ)', 'Perm. Granger', 'Toda–Yamamoto',
42	                  '$K{\\geq}3$ consensus', '$K{\\geq}4$ consensus']
43	
44	data = np.array([[float(r[k]) for r in rows] for k in method_keys]) * 100
45	regimes = [r['regime'] for r in rows]
46	
47	fig, ax = plt.subplots(figsize=(7.5, 3.8))
48	
49	cmap = plt.cm.YlOrRd
50	im = ax.imshow(data, cmap=cmap, aspect='auto', vmin=0, vmax=100, interpolation='nearest')
51	
52	for i in range(len(method_labels)):
53	    for j in range(n):
54	        val = data[i, j]
55	        color = 'white' if val > 65 else 'black'
56	        ax.text(j, i, f'{val:.0f}', ha='center', va='center',
57	                fontsize=7.5, color=color, fontweight='bold' if val >= 75 else 'normal')
58	
59	ax.set_yticks(range(len(method_labels)))
60	ax.set_yticklabels(method_labels)
61	ax.set_xticks(range(n))
62	ax.set_xticklabels(alpha_labels)
63	ax.set_xlabel('Contamination level (α)')
64	
65	# Horizontal separator between individual methods and consensus
66	ax.axhline(4.5, color='white', linewidth=2.5)
67	
68	# Regime band indicators at top
69	regime_colors = {'null': '#FDEDEC', 'onset': '#FEF9E7', 'sync_collapse': '#F4ECF7', 'detection': '#EBF5FB'}
70	regime_names = {'null': 'Blind spot', 'onset': 'Onset', 'sync_collapse': 'Sync.', 'detection': 'Detection'}
71	for j, reg in enumerate(regimes):
72	    color = regime_colors.get(reg, '#FFFFFF')
73	    rect = plt.Rectangle((j - 0.5, -0.9), 1, 0.4, facecolor=color, edgecolor='none',
74	                           clip_on=False, zorder=10)
75	    ax.add_patch(rect)
76	
77	# Regime labels
78	regime_spans = {}
…[truncated 1903 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 115 · 2026-05-19T22:45:25.679601+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"K3_rate\\|K4_rate\\|consensus_heatmap_data\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse --include=\"*.py\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"K3_rate\\|K4_rate\\|consensus_heatmap_data\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse --include=\"*.py\" 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 116 · 2026-05-19T22:45:25.830529+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/figures/paper/gen_consensus_heatmap.py:csv_path = sys.argv[1] if len(sys.argv) > 1 else 'consensus_heatmap_data.csv'
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/figures/paper/gen_consensus_heatmap.py:method_keys = ['naive_rate', 'diff_rate', 'threshold_rate', 'permG_rate', 'TY_rate', 'K3_rate', 'K4_rate']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "elapsed_ms": 150
}
```

</details>

---

### Tool call

_source line 117 · 2026-05-19T22:45:25.882465+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -name \"*consensus*\" -type f 2>/dev/null | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -name \"*consensus*\" -type f 2>/dev/null | head -10"
  }
}
```

</details>

---

### Tool result

_source line 118 · 2026-05-19T22:45:25.933123+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/figures/paper/consensus_heatmap.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/figures/paper/gen_consensus_heatmap.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/scripts/plot_consensus_workflow.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/figures/consensus_workflow.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/figures/consensus_heatmap.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/figures/consensus_heatmap.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/logs/workers/worker_code_consensus_doc_fix_20260515T095358_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/logs/workers/worker_analysis_consensus_framework_formalization_20260515T085017_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/logs/workers/worker_code_consensus_framework_formalization_20260515T083742_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/logs/workers/worker_code_consensus_doc_sig_seeds_fdr_fix_20260515T111624_result.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 119 · 2026-05-19T22:45:27.438714+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/scripts/plot_consensus_workflow.py",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/scripts/plot_consensus_workflow.py",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 120 · 2026-05-19T22:45:27.740362+00:00_

1	#!/usr/bin/env python3
2	"""Generate Consensus Framework Workflow figure (Fig 5 candidate)."""
3	
4	import matplotlib
5	matplotlib.use('Agg')
6	import matplotlib.pyplot as plt
7	import matplotlib.gridspec as gridspec
8	import matplotlib.patches as mpatches
9	import numpy as np
10	import json
11	import os
12	
13	plt.rcParams.update({
14	    'font.family': 'DejaVu Sans',
15	    'font.size': 11,
16	    'axes.titlesize': 13,
17	    'axes.labelsize': 12,
18	    'xtick.labelsize': 10,
19	    'ytick.labelsize': 10,
20	    'legend.fontsize': 10,
21	    'figure.dpi': 300,
22	    'savefig.dpi': 300,
23	    'savefig.bbox': 'tight',
24	    'savefig.pad_inches': 0.05,
25	    'axes.spines.top': False,
26	    'axes.spines.right': False,
27	    'lines.linewidth': 1.8,
28	})
29	
30	C_FPR = '#D55E00'
31	C_FNR = '#0072B2'
32	C_SWEET = '#009E73'
33	STAGE_FILLS = ['#E8F4FD', '#A8D8EA', '#56B4E9', '#0072B2']
34	STAGE_EDGES = ['#A8D8EA', '#56B4E9', '#0072B2', '#004C6D']
35	
36	# ── Load data ──────────────────────────────────────────
37	DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
38	                        'artifacts', 'D040', 'data')
39	with open(os.path.join(DATA_DIR, 'filtering_pipeline_data.json')) as f:
40	    pipe = json.load(f)
41	with open(os.path.join(DATA_DIR, 'fpr_fnr_calibration.json')) as f:
42	    cal = json.load(f)
43	
44	# Panel (a): funnel A stages + conceptual stage 4
45	funnel = pipe['pipeline_funnels']['funnel_A_null_control']['stages'][:]
46	funnel.append({'stage': 4, 'name': 'Multi-seed Consensus',
47	               'sig': 0, 'eliminated': 0, 'fpr': 0.0})
48	STAGE_NAMES = [
49	    'Stage 1: Naive Scan',
50	    'Stage 2: Differencing',
51	    'Stage 3: Perm Granger + FDR',
52	    'Stage 4: Multi-seed Consensus',
53	]
54	PITFALLS = [
55	    'Spurious regression',
56	    'Shared trends',
57	    'Non-causal coincidence',
58	    'Seed-specific artifacts',
59	]
60	
61	# Panel (b): FPR / FNR
62	fpr_k = [d['method_threshold'] for d 
…[truncated 1244 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---

### Tool call

_source line 121 · 2026-05-19T22:45:27.791136+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"consensus_heatmap_data\\|dose_response_5method\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse --include=\"*.py\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"consensus_heatmap_data\\|dose_response_5method\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse --include=\"*.py\" 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 122 · 2026-05-19T22:45:27.841881+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/figures/paper/gen_dose_response.py:csv_path = sys.argv[1] if len(sys.argv) > 1 else 'dose_response_5method_regime.csv'
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/figures/paper/gen_consensus_heatmap.py:csv_path = sys.argv[1] if len(sys.argv) > 1 else 'consensus_heatmap_data.csv'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 123 · 2026-05-19T22:45:29.952327+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"dose_response_5method\\|consensus_heatmap_data\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse --include=\"*.py\" -B 5 -A 5 2>/dev/null | head -40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"dose_response_5method\\|consensus_heatmap_data\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse --include=\"*.py\" -B 5 -A 5 2>/dev/null | head -40"
  }
}
```

</details>

---

### Tool result

_source line 124 · 2026-05-19T22:45:30.003019+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/figures/paper/gen_dose_response.py-    'axes.spines.top': False,
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/figures/paper/gen_dose_response.py-    'axes.spines.right': False,
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/figures/paper/gen_dose_response.py-    'lines.linewidth': 1.8,
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/figures/paper/gen_dose_response.py-})
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/figures/paper/gen_dose_response.py-
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/figures/paper/gen_dose_response.py:csv_path = sys.argv[1] if len(sys.argv) > 1 else 'dose_response_5method_regime.csv'
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/figures/paper/gen_dose_response.py-out_dir = sys.argv[2] if len(sys.argv) > 2 else '.'
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/figures/paper/gen_dose_response.py-
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/figures/paper/gen_dose_response.py-rows = []
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/figures/paper/gen_dose_response.py-with open(csv_path) as f:
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/figures/paper/gen_dose_response.py-    reader = csv.DictReader(f)
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/figures/paper/gen_consensus_heatmap.py-    'savefig.dpi': 300,
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/figures/paper/gen_consensus_heatmap.py-    'savefig.bbox': 'tight',
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/figures/paper/gen_consensus_heatmap.py-    'savef
…[truncated 1183 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 125 · 2026-05-19T22:45:32.061615+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"\\.write\\|\\.to_csv\\|csv.writer\\|csv.DictWriter\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse --include=\"*.py\" 2>/dev/null | grep -E \"dose_response|consensus_heatmap|K3|K4\" | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"\\.write\\|\\.to_csv\\|csv.writer\\|csv.DictWriter\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse --include=\"*.py\" 2>/dev/null | grep -E \"dose_response|consensus_heatmap|K3|K4\" | head -10"
  }
}
```

</details>

---

### Tool result

_source line 126 · 2026-05-19T22:45:32.313223+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "elapsed_ms": 251
}
```

</details>

---

### Tool call

_source line 127 · 2026-05-19T22:45:32.363954+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -type f -name \"*.py\" | xargs grep -l \"\\.write.*csv\\|DictWriter\" 2>/dev/null | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -type f -name \"*.py\" | xargs grep -l \"\\.write.*csv\\|DictWriter\" 2>/dev/null | head -10"
  }
}
```

</details>

---

### Tool result

_source line 128 · 2026-05-19T22:45:32.414796+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/lag_sensitivity/run_lag_sensitivity.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 129 · 2026-05-19T22:45:34.221640+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/lag_sensitivity/run_lag_sensitivity.py",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/lag_sensitivity/run_lag_sensitivity.py",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 130 · 2026-05-19T22:45:34.623695+00:00_

1	"""Lag sensitivity analysis for permutation Granger causality.
2	
3	Runs permutation Granger test with lag=1,2,3 across all alpha-sweep experiments
4	and the alpha=1.00 generalize experiment, then applies per-alpha BH FDR correction.
5	"""
6	
7	import json
8	import os
9	import csv
10	import sys
11	import numpy as np
12	
13	sys.path.insert(0, "/root/autodl-tmp/distrib_canary_collapse")
14	from permutation_granger import permutation_granger_test
15	
16	N_PERM = 5000
17	ALPHA_FDR = 0.05
18	
19	CANARIES = ["token_entropy", "ece"]
20	DOWNSTREAMS = ["distinct_1", "distinct_2", "distinct_3", "perplexity"]
21	PAIRS = [(c, d) for c in CANARIES for d in DOWNSTREAMS]
22	
23	EXPERIMENTS = {
24	    0.00: [
25	        ("a000_s42", 42, "results/alpha_sweep/a000_s42"),
26	        ("a000_s43", 43, "results/alpha_sweep/a000_s43"),
27	        ("a000_s44", 44, "results/alpha_sweep/a000_s44"),
28	    ],
29	    0.25: [
30	        ("a025_s43", 43, "results/alpha_sweep/a025_s43"),
31	        ("a025_s44", 44, "results/alpha_sweep/a025_s44"),
32	    ],
33	    0.50: [
34	        ("a050_s42", 42, "results/alpha_sweep/a050_s42"),
35	        ("a050_s43", 43, "results/alpha_sweep/a050_s43"),
36	        ("a050_s44", 44, "results/alpha_sweep/a050_s44"),
37	    ],
38	    0.75: [
39	        ("a075_s42", 42, "results/alpha_sweep/a075_s42"),
40	        ("a075_s43", 43, "results/alpha_sweep/a075_s43"),
41	        ("a075_s44", 44, "results/alpha_sweep/a075_s44"),
42	    ],
43	    1.00: [
44	        ("pythia410m_wiki_a100_s42", 42, "results/generalize/pythia410m_wiki_a100_s42"),
45	    ],
46	}
47	
48	LAGS = [1, 2, 3]
49	BASE = "/root/autodl-tmp/distrib_canary_collapse"
50	
51	
52	def load_series(data_dir):
53	    all_path = os.path.join(data_dir, "all_metrics.json")
54	    with open(all_path) as f:
55	        data = json.load(f)
56	    data.sort(key=lambda x: x["generation"])
57	    out = {}
58	    for k in CANARIES + DOWNSTREAMS:
59	        out[k] = np.array([d[k] for d in data])
60	    return out, len
…[truncated 1530 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---

### Tool call

_source line 131 · 2026-05-19T22:45:34.674381+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -type f -name \"*.md\" | xargs grep -l \"5method\\|PermG\\|lead.*lag\\|K≥\" 2>/dev/null | head -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -type f -name \"*.md\" | xargs grep -l \"5method\\|PermG\\|lead.*lag\\|K≥\" 2>/dev/null | head -5"
  }
}
```

</details>

---

### Tool result

_source line 132 · 2026-05-19T22:45:34.725097+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/IDEA_BRIEF.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/task_context/agent.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/task_context/director.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/task_context/reviewer.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/task_context/history/director/loop_9.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 133 · 2026-05-19T22:45:36.783488+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/cross_alpha_analysis.py",
  "offset": "402",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/cross_alpha_analysis.py",
    "offset": "402",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 134 · 2026-05-19T22:45:37.034944+00:00_

402	def main():
403	    parser = argparse.ArgumentParser(
404	        description="Cross-alpha analysis for distributional canary collapse experiments."
405	    )
406	    parser.add_argument("--alpha-dirs", nargs="*", default=None,
407	                        help="Specific alpha dirs (e.g. a000_s42 a025_s42). Default: auto-discover all.")
408	    parser.add_argument("--n-perms", type=int, default=5000,
409	                        help="Number of permutations for Granger test (default: 5000)")
410	    parser.add_argument("--max-lag", type=int, default=1,
411	                        help="Max lag for Granger test (default: 1)")
412	    parser.add_argument("--version", type=int, default=None,
413	                        help="Output version number (default: auto-increment)")
414	    parser.add_argument("--update-registry", action="store_true",
415	                        help="Print registry update commands after analysis")
416	    args = parser.parse_args()
417	
418	    alpha_dirs = discover_alpha_dirs(args.alpha_dirs)
419	    if not alpha_dirs:
420	        print("ERROR: No alpha directories found.", file=sys.stderr)
421	        sys.exit(1)
422	
423	    print(f"Found {len(alpha_dirs)} alpha points: {[a[0] for a in alpha_dirs]}")
424	
425	    all_data = []
426	    for alpha_key, alpha_val, path in alpha_dirs:
427	        metrics = load_metrics(path)
428	        print(f"  {alpha_key} (α={alpha_val}): {len(metrics)} generations")
429	        all_data.append((alpha_key, alpha_val, metrics))
430	
431	    # 1. Dose-response
432	    dose_resp = compute_dose_response(all_data)
433	
434	    # 2. Granger
435	    print(f"\nRunning bidirectional Granger ({len(GRANGER_PAIRS)} pairs × {len(all_data)} alphas, "
436	          f"n_perms={args.n_perms})...")
437	    granger = run_granger_all(all_data, max_lag=args.max_lag, n_perms=args.n_perms)
438	    granger = apply_fdr(granger)
439	
440	    # 3. Cross-correlation
441	    xcorr = cross_correlation(all_data)
442	
443	    # 4. Velocit
…[truncated 297 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---

### Tool call

_source line 135 · 2026-05-19T22:45:37.035495+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A 10 \"if __name__\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/consensus_framework.py | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A 10 \"if __name__\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/consensus_framework.py | head -20"
  }
}
```

</details>

---

### Tool result

_source line 136 · 2026-05-19T22:45:37.086004+00:00_

if __name__ == "__main__":
    main()

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 137 · 2026-05-19T22:45:39.395576+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"forward\\|backward\\|reverse\\|direction\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/cross_alpha_analysis.py | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"forward\\|backward\\|reverse\\|direction\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/cross_alpha_analysis.py | head -20"
  }
}
```

</details>

---

### Tool result

_source line 138 · 2026-05-19T22:45:39.447030+00:00_

5:  2. Bidirectional permutation Granger causality with BH FDR correction
190:    """Run bidirectional Granger for all α × all pairs. Returns list of result dicts."""
200:                "direction": label,
339:    print(f"\n{'GRANGER CAUSALITY (bidirectional, differenced, permutation)'}")
348:    directions = list(dict.fromkeys(r["direction"] for r in gc))
349:    for d in directions:
352:            match = [r for r in gc if r["alpha_key"] == ak and r["direction"] == d]
435:    print(f"\nRunning bidirectional Granger ({len(GRANGER_PAIRS)} pairs × {len(all_data)} alphas, "

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 139 · 2026-05-19T22:45:41.655603+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/cross_alpha_analysis.py",
  "offset": "37",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/cross_alpha_analysis.py",
    "offset": "37",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 140 · 2026-05-19T22:45:41.706298+00:00_

37	# Granger test pairs: (cause, effect, label)
38	GRANGER_PAIRS = [
39	    ("token_entropy", "distinct_1", "entropy→d1"),
40	    ("ece",           "distinct_1", "ECE→d1"),
41	    ("token_entropy", "distinct_2", "entropy→d2"),
42	    ("ece",           "distinct_2", "ECE→d2"),
43	    ("distinct_1", "token_entropy", "d1→entropy"),
44	    ("distinct_1", "ece",           "d1→ECE"),
45	    ("distinct_2", "token_entropy", "d2→entropy"),
46	    ("distinct_2", "ece",           "d2→ECE"),
47	]
48	
49	XCORR_PAIRS = [
50	    ("token_entropy", "distinct_1", "entropy_vs_d1"),
51	    ("ece",           "distinct_1", "ece_vs_d1"),
52	]
53	
54	
55	def discover_alpha_dirs(explicit=None):
56	    """Find alpha experiment directories. Returns sorted list of (alpha_key, alpha_float, path)."""

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool result

_source line 141 · 2026-05-19T22:45:54.830519+00:00_

Perfect. Now I have enough information. Let me provide the comprehensive findings:

## Report: MMCT 5-Method Lead-Lag Analysis Scripts

Based on my thorough search of the repository, here are the Python analysis scripts used for the MMCT 5-method lead-lag analysis:

### 1. **Core Analysis Scripts**

#### Primary Analysis Engine:
- **File Path**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/cross_alpha_analysis.py`
- **Purpose**: Computes dose-response, bidirectional permutation Granger causality, cross-correlation lead-lag analysis, and per-generation velocity metrics

#### Supporting Consensus Framework:
- **File Path**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/consensus_framework.py`
- **Purpose**: Multi-method consensus classification with K≥3 and K≥4 aggregation (two-stage: seed→method verdict, then method→consensus)

#### Permutation Granger Implementation:
- **File Path**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/permutation_granger.py`
- **Purpose**: Core permutation-based Granger causality test with first-difference preprocessing

### 2. **Invocation Details**

**cross_alpha_analysis.py** command-line arguments:
```bash
python cross_alpha_analysis.py [--alpha-dirs DIRS...] [--n-perms N] [--max-lag LAG] [--version V] [--update-registry]
```

Specific arguments:
- `--alpha-dirs`: Specific alpha directories to analyze (e.g., `a000_s42 a025_s42`). Default: auto-discover all
- `--n-perms`: Number of permutations for Granger test (default: 5000)
- `--max-lag`: Maximum lag for Granger test (default: 1)
- `--version`: Output version number (default: auto-increment)
- `--update-registry`: Print registry update commands after analysis

### 3. **Computed Metrics**

The analysis computes:
- **PermG (Permutation Granger)**: Bidirectional Granger causality with Benjamini-Hochberg FDR correction
- **K≥3 consensus**: Agreement among 3 or more of t
…[truncated 2175 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Agent",
  "elapsed_ms": 75526
}
```

</details>

---

### Tool call

_source line 142 · 2026-05-19T22:46:06.179510+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/run_5method*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/run_5method*.py",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
  }
}
```

</details>

---

### Tool call

_source line 143 · 2026-05-19T22:46:06.179934+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/analyze_*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/analyze_*.py",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
  }
}
```

</details>

---

### Tool result

_source line 144 · 2026-05-19T22:46:06.230421+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---

### Tool result

_source line 145 · 2026-05-19T22:46:06.230841+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analyze_mvp.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analyze_extended.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 146 · 2026-05-19T22:46:10.146172+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/batch_analysis*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/batch_analysis*.py",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
  }
}
```

</details>

---

### Tool result

_source line 147 · 2026-05-19T22:46:10.648439+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Glob",
  "elapsed_ms": 502
}
```

</details>

---

### Tool call

_source line 148 · 2026-05-19T22:46:10.749140+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/5method*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/5method*.py",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
  }
}
```

</details>

---

### Tool result

_source line 149 · 2026-05-19T22:46:10.799907+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 150 · 2026-05-19T22:46:15.848231+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "5method_leadlag",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "output_mode": "files_with_matches",
  "head_limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Grep",
  "tool_args": {
    "pattern": "5method_leadlag",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
    "output_mode": "files_with_matches",
    "head_limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 151 · 2026-05-19T22:46:15.899028+00:00_

Found 10 files limit: 10
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/logs/chats/cron_hook_alpha_sweep_a045_s42_fp32.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/logs/chats/feishu_group_oc_1f489e32588225ae3672d716b94662a8_reviewer.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/logs/chats/feishu_group_oc_150c7ce908e05d7932315e0288cf5bfb_director.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/logs/chats/feishu_group_oc_1f489e32588225ae3672d716b94662a8.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/logs/workers/worker_fix_batch_analysis_d111_direction_20260519T223814.log
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/logs/workers/worker_audit_c4_d111_direction_check_20260519T223059.log
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/manifest.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/report/d111_c4_audit_report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 152 · 2026-05-19T22:47:06.938497+00:00_

called mcp__agent-ml-research__spawn_worker

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker</summary>

````json
{
  "task_type": "analysis:alpha_sweep_a045_s42_fp32",
  "project": "distrib_canary_collapse",
  "task_prompt": "## 任务：分析实验 alpha_sweep_a045_s42_fp32\n\n### 背景\n这是 onset 精化实验。当前 onset boundary 在 [0.40, 0.50]：\n- α=0.40: PermG=0/8（blind zone）\n- α=0.45: **本实验**（刚完成，需分析）\n- α=0.50: PermG=6/8（detected）\n\n如果 PermG=0/8 → onset ∈ [0.45, 0.50]\n如果 PermG>0 → onset ∈ [0.40, 0.45]\n\n### 实验信息\n- exp_id: alpha_sweep_a045_s42_fp32\n- 服务器: westd-17855\n- 结果目录: /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a045_s42_fp32\n- 模型: Pythia-410M, WikiText-103, α=0.45, seed=42, fp32\n- 10 generations (gen_0 到 gen_10)\n\n### SSH 环境\n连接 westd-17855，conda 激活：\n```\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base\n```\n\n### 分析步骤\n\n1. **检查训练完成**：\n   - 确认 EXIT_CODE=0\n   - 确认所有 gen 目录存在（gen_0 到 gen_10）\n   - 检查每个 gen 的 metrics.json 存在\n\n2. **读取 per-generation metrics**：\n   - 从每个 gen 的 metrics.json 读取: token_entropy, ece, distinct_1, distinct_2, distinct_3, mauve, perplexity, effective_rank\n   - 列出 per-gen 表格\n\n3. **计算 drift**：gen_0 → gen_10 的百分比变化\n\n4. **运行 5-method MMCT lead-lag 分析**：\n   检查结果目录是否已有 `5method_leadlag.json`（训练脚本可能已自动生成）。\n   \n   如果有，直接读取结果。\n   如果没有，用项目中的分析脚本运行。分析脚本位于 `/root/autodl-tmp/distrib_canary_collapse/`，可能是 `cross_alpha_analysis.py` 或类似脚本。\n   \n   先检查：\n   ```bash\n   ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a045_s42_fp32/5method_leadlag.json 2>/dev/null\n   ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a045_s42_fp32/mmct_analysis*.json 2>/dev/null\n   find /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a045_s42_fp32/ -name \"*.json\" -type f\n   ```\n   \n   如果需要运行分析：\n   ```bash\n   cd /root/autodl-tmp/distrib_canary_collapse\n   python cross_alpha_analysis.py --alpha-dirs a045_s42_fp32 --n-perms 5000\n   ```\n\n5. **D111 方向检查**（mandatory）：\n   对 diff_xcorr 和 naive_xcorr，检查 lag 方向是否与预期一致（canary 应 lead downstream）。如果方向相反（lag ≤ 0），标记为无效。\n\n6. **提取关键指标**（8 pairs: {entropy, ece} × {d1, d2, d3, mauve}）：\n   - PermG fwd (FDR-adjusted): X/8\n   - PermG rev (FDR-adjusted): X/8\n   - K≥3 (3σ consensus): X/8\n   - K≥4 (3σ consensus): X/8\n   - naive_xcorr: X/8\n   - diff_xcorr: X/8\n   - threshold_onset: X/8\n   - TY granger: X/8\n   - Per-pair detail table with p-values\n\n7. **检查 W&B**：\n   查看是否有 wandb run（`ls /root/autodl-tmp/distrib_canary_collapse/wandb/` 或检查 run_id）\n\n### 产出\n\n1. 写分析报告到本地: `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/alpha_sweep_a045_s42_fp32/report/analysis_alpha_sweep_a045_s42_fp32.md`\n\n   报告格式参考（alpha_sweep_a030_s42_fp32_analysis.md）：\n   - Config（模型、数据、α、seed、precision）\n   - Hypothesis\n   - Result summary（一行结论）\n   - Per-gen metrics table\n   - Drift table\n   - 5-Method Lead-Lag summary table\n   - Per-pair detail table（含 PermG p-values）\n   - Updated onset boundary table\n   - Notes\n\n2. 用 `update_registry` 更新以下字段：\n   - metrics: 包含 permg_fwd, permg_rev, k_ge3, k_ge4, naive_xcorr, diff_xcorr, threshold_onset, ty_granger, drift_entropy_pct, drift_d1_pct 等\n   - conclusion: \"success\"（无论 PermG 是否 >0，这是 informative result）\n   - status: \"DONE\"\n   - spec 补充 checkpoint_path 和 log_path\n\n3. 用 `register_artifact` 注册分析报告\n\n### 关键约束\n- D086: per-alpha BH FDR, n_perm=5000\n- D102: 统一 8-pair (entropy/ECE × d1/d2/d3/mauve)\n- D105: 全局 true 3σ\n- D106: PermG fwd 主指标 + K≥3(3σ) 辅助\n- D111: direction checking mandatory\n",
  "tool_groups": "['ssh', 'wandb', 'registry']",
  "tools": "['register_artifact']",
  "context": "## 环境信息\n- westd-17855: RTX PRO 6000 Blackwell (98GB), conda base env\n- 项目路径: /root/autodl-tmp/distrib_canary_collapse/\n- Python 在 conda base 中\n- 结果目录: results/alpha_sweep/a045_s42_fp32\n\n## 参考：邻近 alpha 实验结果\n- α=0.30: PermG=0/8, K≥3=6/8, K≥4=3/8\n- α=0.35: PermG=0/8, K≥3=6/8, K≥4=2/8  \n- α=0.40: PermG=0/8\n- α=0.50: PermG=6/8, K≥3=6/8, K≥4=1/8\n- α=0.60: PermG=0-3/8（同步坍缩区）\n\n## SSH 提交命令模板\nbash -c \"cd /root/autodl-tmp/distrib_canary_collapse && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && ...\""
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "tool_args": {
    "task_type": "analysis:alpha_sweep_a045_s42_fp32",
    "project": "distrib_canary_collapse",
    "task_prompt": "## 任务：分析实验 alpha_sweep_a045_s42_fp32\n\n### 背景\n这是 onset 精化实验。当前 onset boundary 在 [0.40, 0.50]：\n- α=0.40: PermG=0/8（blind zone）\n- α=0.45: **本实验**（刚完成，需分析）\n- α=0.50: PermG=6/8（detected）\n\n如果 PermG=0/8 → onset ∈ [0.45, 0.50]\n如果 PermG>0 → onset ∈ [0.40, 0.45]\n\n### 实验信息\n- exp_id: alpha_sweep_a045_s42_fp32\n- 服务器: westd-17855\n- 结果目录: /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a045_s42_fp32\n- 模型: Pythia-410M, WikiText-103, α=0.45, seed=42, fp32\n- 10 generations (gen_0 到 gen_10)\n\n### SSH 环境\n连接 westd-17855，conda 激活：\n```\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base\n```\n\n### 分析步骤\n\n1. **检查训练完成**：\n   - 确认 EXIT_CODE=0\n   - 确认所有 gen 目录存在（gen_0 到 gen_10）\n   - 检查每个 gen 的 metrics.json 存在\n\n2. **读取 per-generation metrics**：\n   - 从每个 gen 的 metrics.json 读取: token_entropy, ece, distinct_1, distinct_2, distinct_3, mauve, perplexity, effective_rank\n   - 列出 per-gen 表格\n\n3. **计算 drift**：gen_0 → gen_10 的百分比变化\n\n4. **运行 5-method MMCT lead-lag 分析**：\n   检查结果目录是否已有 `5method_leadlag.json`（训练脚本可能已自动生成）。\n   \n   如果有，直接读取结果。\n   如果没有，用项目中的分析脚本运行。分析脚本位于 `/root/autodl-tmp/distrib_canary_collapse/`，可能是 `cross_alpha_analysis.py` 或类似脚本。\n   \n   先检查：\n   ```bash\n   ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a045_s42_fp32/5method_leadlag.json 2>/dev/null\n   ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a045_s42_fp32/mmct_analysis*.json 2>/dev/null\n   find /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a045_s42_fp32/ -name \"*.json\" -type f\n   ```\n   \n   如果需要运行分析：\n   ```bash\n   cd /root/autodl-tmp/distrib_canary_collapse\n   python cross_alpha_analysis.py --alpha-dirs a045_s42_fp32 --n-perms 5000\n   ```\n\n5. **D111 方向检查**（mandatory）：\n   对 diff_xcorr 和 naive_xcorr，检查 lag 方向是否与预期一致（canary 应 lead downstream）。如果方向相反（lag ≤ 0），标记为无效。\n\n6. **提取关键指标**（8 pairs: {entropy, ece} × {d1, d2, d3, mauve}）：\n   - PermG fwd (FDR-adjusted): X/8\n   - PermG rev (FDR-adjusted): X/8\n   - K≥3 (3σ consensus): X/8\n   - K≥4 (3σ consensus): X/8\n   - naive_xcorr: X/8\n   - diff_xcorr: X/8\n   - threshold_onset: X/8\n   - TY granger: X/8\n   - Per-pair detail table with p-values\n\n7. **检查 W&B**：\n   查看是否有 wandb run（`ls /root/autodl-tmp/distrib_canary_collapse/wandb/` 或检查 run_id）\n\n### 产出\n\n1. 写分析报告到本地: `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/alpha_sweep_a045_s42_fp32/report/analysis_alpha_sweep_a045_s42_fp32.md`\n\n   报告格式参考（alpha_sweep_a030_s42_fp32_analysis.md）：\n   - Config（模型、数据、α、seed、precision）\n   - Hypothesis\n   - Result summary（一行结论）\n   - Per-gen metrics table\n   - Drift table\n   - 5-Method Lead-Lag summary table\n   - Per-pair detail table（含 PermG p-values）\n   - Updated onset boundary table\n   - Notes\n\n2. 用 `update_registry` 更新以下字段：\n   - metrics: 包含 permg_fwd, permg_rev, k_ge3, k_ge4, naive_xcorr, diff_xcorr, threshold_onset, ty_granger, drift_entropy_pct, drift_d1_pct 等\n   - conclusion: \"success\"（无论 PermG 是否 >0，这是 informative result）\n   - status: \"DONE\"\n   - spec 补充 checkpoint_path 和 log_path\n\n3. 用 `register_artifact` 注册分析报告\n\n### 关键约束\n- D086: per-alpha BH FDR, n_perm=5000\n- D102: 统一 8-pair (entropy/ECE × d1/d2/d3/mauve)\n- D105: 全局 true 3σ\n- D106: PermG fwd 主指标 + K≥3(3σ) 辅助\n- D111: direction checking mandatory\n",
    "tool_groups": "['ssh', 'wandb', 'registry']",
    "tools": "['register_artifact']",
    "context": "## 环境信息\n- westd-17855: RTX PRO 6000 Blackwell (98GB), conda base env\n- 项目路径: /root/autodl-tmp/distrib_canary_collapse/\n- Python 在 conda base 中\n- 结果目录: results/alpha_sweep/a045_s42_fp32\n\n## 参考：邻近 alpha 实验结果\n- α=0.30: PermG=0/8, K≥3=6/8, K≥4=3/8\n- α=0.35: PermG=0/8, K≥3=6/8, K≥4=2/8  \n- α=0.40: PermG=0/8\n- α=0.50: PermG=6/8, K≥3=6/8, K≥4=1/8\n- α=0.60: PermG=0-3/8（同步坍缩区）\n\n## SSH 提交命令模板\nbash -c \"cd /root/autodl-tmp/distrib_canary_collapse && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && ...\""
  }
}
````

</details>

---

### Tool result

_source line 153 · 2026-05-19T22:47:09.800026+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_analysis_alpha_sweep_a045_s42_fp32_20260519T224707\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/logs/workers/worker_analysis_alpha_sweep_a045_s42_fp32_20260519T224707.log\", \"setup_data\": {}, \"message\": \"Worker worker_analysis_alpha_sweep_a045_s42_fp32_20260519T224707 started. Use get_worker_status('worker_analysis_alpha_sweep_a045_s42_fp32_20260519T224707') to check progress.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "elapsed_ms": 2861
}
```

</details>

---

### Assistant

_source line 154 · 2026-05-19T22:47:35.395113+00:00_

已派 Worker `worker_analysis_alpha_sweep_a045_s42_fp32_20260519T224707` 分析 onset 精化实验。

当前状态：
- 7 个实验 RUNNING（8/8 GPU 满载）
- 1 个 Worker 分析 a045
- 等待 Worker 回调后更新 registry + 汇报 Director onset boundary 精化结果

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:alpha_sweep_a045_s42_fp32"
}
```

</details>

---
