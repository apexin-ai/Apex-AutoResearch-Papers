# cron hook k2 l2 calibration phase1

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 2
- **Tool calls:** 15
- **Original source:** `logs/chats/cron_hook_k2-l2-calibration-phase1.jsonl`
- **Structured JSON:** [`ad1e9bb5396d6f93311f.json`](../../sessions/ad/ad1e9bb5396d6f93311f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

32 recorded events

### User

_source line 1 · 2026-05-19T20:57:49.113380+00:00_

[CRON] 实验进程异常退出（失败），需要你诊断原因。
详情: Process exited without valid W&B metrics

- exp_id: k2-l2-calibration-phase1
- project: acr-vla-conformal-refinement
- server: bjb2-28827

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:k2-l2-calibration-phase1",
  "source": "cron:hook"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-19T20:58:01.639547+00:00_

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
  "session": "cron:hook:k2-l2-calibration-phase1",
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

_source line 3 · 2026-05-19T20:58:01.694657+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:k2-l2-calibration-phase1",
  "tool": "ToolSearch",
  "elapsed_ms": 55
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-19T20:58:05.052615+00:00_

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
  "session": "cron:hook:k2-l2-calibration-phase1",
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

_source line 5 · 2026-05-19T20:58:05.494408+00:00_

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
  "session": "cron:hook:k2-l2-calibration-phase1",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-19T20:58:05.938455+00:00_

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
  "session": "cron:hook:k2-l2-calibration-phase1",
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

_source line 7 · 2026-05-19T20:58:05.995491+00:00_

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
  "session": "cron:hook:k2-l2-calibration-phase1",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T20:58:07.473689+00:00_

Error: result (547,330 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-12e7e389/d9cb8685-3622-4654-bcff-e37f16e7e1bf/tool-results/mcp-agent-ml-research-read_registry-1779224287381.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-12e7e389/d9cb8685-3622-4654-bcff-e37f16e7e1bf/tool-results/mcp-agent-ml-research-read_registry-1779224287381.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:k2-l2-calibration-phase1",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 2421
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-19T20:59:15.406524+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 7, \"results\": [{\"exp_id\": \"eval-openvla-object-baseline-seed42\", \"success\": true, \"actions\": [\"Job still running (pid=eval-openvla-object-baseline-seed42)\"]}, {\"exp_id\": \"eval-vla-only-long-seed47\", \"success\": true, \"actions\": [\"Stale cron removed (registry status=DONE)\"]}, {\"exp_id\": \"eval-vla-only-spatial-seed48\", \"success\": true, \"actions\": [\"Process dead 5× with no signal → auto-resolved DONE(failed)\"]}, {\"exp_id\": \"eval-vla-only-object-seed48\", \"success\": true, \"actions\": [\"Job still running (pid=eval-vla-only-object-seed48)\"]}, {\"exp_id\": \"eval-crm-goal-seed42\", \"success\": true, \"actions\": [\"Job still running (pid=eval-crm-goal-seed42)\"]}, {\"exp_id\": \"eval-crm-goal-seed43\", \"success\": true, \"actions\": [\"Job still running (pid=eval-crm-goal-seed43)\"]}, {\"exp_id\": \"eval-crm-long-seed45\", \"success\": true, \"actions\": [\"Job still running (pid=eval-crm-long-seed45)\"]}]}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:k2-l2-calibration-phase1",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 69912
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T20:59:15.467046+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-19T20:59:14Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 353 个实验 — ANALYZING 1, DEPLOYED 4, DONE 334, PREPARING 3, RUNNING 11\\n**DONE 分布**: failed 45, killed 81, negative 31, success 177\\n\\n### GPU 占用\\n- **实际运行**: 7 张 — bjb2-28827:cuda:4(eval-openvla-object-baseline-seed42), bjb1-32546:cuda:0(eval-vla-only-spatial-seed46), bjb1-32546:cuda:2(eval-vla-only-spatial-seed47), bjb2-28827:cuda:0(eval-vla-only-object-seed47), bjb2-28827:cuda:2(eval-crm-long-seed42), bjb2-28827:cuda:3(eval-crm-long-seed43), bjb2-28827:cuda:5(eval-crm-long-seed44)\\n\\n### 💾 磁盘余量\\n- **bjb2-40593**:\\n  - `/init`: 150M/150M 可用（已用 0%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 47G/437G 可用（已用 89%）\\n- **bjb1-18228**:\\n  - `/autodl-pub`: 1.1T/7.0T 可用（已用 85%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 400G/438G 可用（已用 4%）\\n- **bjb1-32546**:\\n  - `/autodl-pub`: 566G/7.0T 可用（已用 93%） ⚠️\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 400G/438G 可用（已用 4%）\\n- **bjb2-28827**:\\n  - `/autodl-pub`: 4.4T/14T 可用（已用 70%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 399G/439G 可用（已用 5%）\\n\\n### 🏃 RUNNING\\n| exp_id | server | gpu | pid | log |\\n|--------|--------|-----|-----|-----|\\n| `eval-openvla-object-baseline-seed42` | bjb2-28827 | cuda:4 | 900134 | `…onformal-refinement/eval-openvla-object-baseline-seed42.log` |\\n| `eval-vla-only-spatial-seed46` | bjb1-32546 | cuda:0 | 47637 | `…r-vla-conformal-refinement/eval-vla-only-spatial-seed46.log` |\\n| `eval-vla-only-spatial-seed47` | bjb1-32546 | cuda:2 | 47706 | `…r-vla-conformal-refinement/eval-vla-only-spatial-seed47.log` |\\n| `eval-vla-only-object-seed47`
…[truncated 8871 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:k2-l2-calibration-phase1",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 69528
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-19T20:59:15.467720+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-19 16:52 UTC | 更新原因: Full state refresh: LIBERO-10/Goal deployed (D073), Random K=5 DONE, latency 170ms, adaptive K Phase 1 approved, OpenVLA eval starting\\n\\n> 详见 paper_framing.md（D072: Adaptive K 核心方法变更）\\n\\n## 核心方向\\n**Adaptive inference-time correction for frozen VLAs** — 根据 per-step 不确定性信号动态决定推理次数 + CRM 校正\\nTitle: TBD (原 \\\"Correction Over Selection\\\" 可能调整)\\n\\n## 投稿目标\\n**CoRL 2026** DDL **2026-05-29**（确认）。剩余 10 天。\\n\\n## 方法核心 (D072)\\n- 默认 K=1 单推理，FMVD 信号高时触发 K_full + CRM 校正\\n- FMVD = Flow Velocity Dispersion（ODE 轨迹湍流度，零额外开销）\\n- Phase 1 (signal validation) 已审批，正在部署\\n\\n## 关键进展\\n\\n### 实验证据 ✅ 近完整\\n| Evidence | 结果 | Status |\\n|----------|------|--------|\\n| K=10 obs_only (n=7) | 17.6% vs VLA 11.6%, p=0.0025 | ✅ |\\n| K=5 obs_only (n=7) | 16.0%±2.2% | ✅ |\\n| K=10 decomposition | selection≈0, correction +5.3pp | ✅ LOCKED |\\n| K=5 decomposition | random 10.5%<VLA, selection +3.2pp, correction +2.3pp | ✅ DONE (n=4 random) |\\n| K-value curve | K=1(10.3%)→K=5(16%)→K=10(17.6%) | ✅ |\\n| K=1 CRM eval | 10.3%±1.5% (NEGATIVE) | ✅ |\\n| Magnitude obs_only | stable 14-18% all ε, ε=0.03 n=4 | ✅ |\\n| Magnitude perdof | collapse at high ε | ✅ |\\n| LTO generalization | CRM 2% vs VLA 14% — harmful OOD | ✅ D069 |\\n| Spatial K=10 | 35.0%±1.0% (n=3), seed46/47 running | ✅ |\\n| Spatial VLA-only | 29.3%±1.7% (n=4) | ✅ DONE |\\n| Spatial K=5 | 34.5%±2.1% (n=4) | ✅ DONE |\\n| Random K=5 | 10.5%±2.9% — multi-sampling harmful | ✅ DONE |\\n| Latency (plan_602) | batched ~170ms all K, CRM 0.25ms | ✅ DONE |\\n| Adaptive K Phase 1 | FMVD validation | 🔄 部署中 |\\n| OpenVLA eval | 下载+环境搭建中 | 🔄 |\\n| LIBERO-10 VLA-only | 3 seeds running (D073) | 🔄 NEW |\\n| LIBERO-Goal VLA-only | 3 seeds running (D073) | 🔄 NEW |\\n\\n### 并行工作流 (4 线)\\n
…[truncated 2794 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:k2-l2-calibration-phase1",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 69472
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-19T20:59:23.528499+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'exp_id': 'k2-l2-calibration-phase1'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:k2-l2-calibration-phase1",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'exp_id': 'k2-l2-calibration-phase1'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-19T20:59:25.327609+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.7081}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:k2-l2-calibration-phase1",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1799
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-19T20:59:25.517384+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__read_experiment_plan_with_status,mcp__agent-ml-research__list_workers",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:k2-l2-calibration-phase1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__read_experiment_plan_with_status,mcp__agent-ml-research__list_workers",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-19T20:59:25.517789+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:k2-l2-calibration-phase1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-19T20:59:38.547106+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A 50 \"k2-l2-calibration-phase1\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml | head -80",
  "description": "Search registry for k2-l2-calibration-phase1 experiment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:k2-l2-calibration-phase1",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A 50 \"k2-l2-calibration-phase1\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml | head -80",
    "description": "Search registry for k2-l2-calibration-phase1 experiment"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-19T20:59:38.750376+00:00_

  k2-l2-calibration-phase1:
    status: DONE
    retry_count: 0
    created_at: '2026-05-19T20:32:52.408Z'
    updated_at: '2026-05-19T20:57:42.882Z'
    hypothesis: 'K=2 L2 divergence (mean pairwise L2 from K=10 samples) as uncertainty
      proxy for Adaptive K. Measures action-space disagreement directly. Go/no-go:
      Spearman ρ(mean_pair_l2, k10_variance) > 0.3.'
    spec:
      command: CUDA_VISIBLE_DEVICES=1 python -u src/calibrate_fmvd.py --benchmark
        object --n_episodes 5 --seed 42 --output logs/k2_l2_calibration.json
      server: bjb2-28827
      data_path: LIBERO object benchmark (10 tasks x 5 episodes)
      data_count: 50
      model_name: smolvla_libero
      seed: 42
    reproduce:
      finished_at: '2026-05-19T20:57:30.913Z'
    failure_reason: process dead 5× with no sentinel/W&B — auto-resolved as failed
    conclusion: failed
    completed_at: '2026-05-19T20:57:36.071Z'
    extra:
      hook_events:
      - event: on_failed
        action: agent
        ts: '2026-05-19T20:57:50.152755+00:00'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:k2-l2-calibration-phase1",
  "tool": "Bash",
  "elapsed_ms": 203
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-19T20:59:45.983045+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/skills/on-experiment-failed.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:k2-l2-calibration-phase1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/skills/on-experiment-failed.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-19T20:59:46.033903+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/sessions/agent_12e7e389.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:k2-l2-calibration-phase1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-19T20:59:48.597426+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/on-experiment-failed*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:k2-l2-calibration-phase1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/on-experiment-failed*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-19T20:59:48.650444+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:k2-l2-calibration-phase1",
  "tool": "Glob",
  "elapsed_ms": 53
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-19T20:59:51.162430+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/on-experiment-failed*",
  "path": "/home/ubuntu/agent-ml-research"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:k2-l2-calibration-phase1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/on-experiment-failed*",
    "path": "/home/ubuntu/agent-ml-research"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-19T20:59:51.414949+00:00_

/home/ubuntu/agent-ml-research/skills/global/on-experiment-failed.skill.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:k2-l2-calibration-phase1",
  "tool": "Glob",
  "elapsed_ms": 252
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-19T20:59:53.873298+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/on-experiment-failed.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:k2-l2-calibration-phase1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/on-experiment-failed.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-19T20:59:53.925231+00:00_

1	---
2	name: on-experiment-failed
3	description: 实验失败后的自动诊断工作流——查日志分析原因、更新 registry、通知 Director。[CRON] 实验失败消息到达时使用。
4	scope: global
5	tags:
6	- workflow
7	- diagnosis
8	- cron-hook
9	tools:
10	- read_registry
11	- tail_training_logs
12	- update_registry
13	- append_idea
14	- feishu_send_result_card
15	- spawn_worker
16	- check_job_status
17	version: 4
18	heavy: true
19	roles:
20	- agent
21	---
22	
23	# 实验失败诊断工作流
24	
25	## 触发方式
26	由 cron hook 自动触发：进程退出且 W&B 无数据 / W&B state=failed/crashed / NaN 检测到。
27	
28	## 步骤
29	
30	### Step 0: 读取项目上下文（诊断前必须执行）
31	先读文档，再看日志——否则诊断方向可能完全错误：
32	
33	- `read_project_file("memory.md")` — **最重要**：查是否有相同失败模式的历史记录和已知修复方案
34	- Worker 通过 `list_repo_tree` + `read_repo_file` 按需从代码仓库读取训练脚本结构
35	
36	读完后检查：
37	- memory.md 里有没有"此类实验曾失败，原因是 X"的记录？→ 直接按已知方案诊断，跳过 Step 2 通用流程
38	- 代码仓库中的训练入口和参数格式是否与本次实验配置匹配？（Worker 可用 `list_repo_tree` + `read_repo_file` 查看）
39	
40	### Step 1: 了解失败背景
41	- read_registry(exp_id) — 查看状态、conclusion、notes、metrics、log_path
42	
43	### Step 2: 浅层日志诊断
44	有 log_path 时：tail_training_logs(server, **绝对路径**, lines=80)
45	- 寻找：OOM、CUDA error、NaN、assertion error、数据加载错误、Python Traceback
46	- 没找到 → 增加行数再查
47	
48	### Step 2.5: 深查（满足以下任一条件时 spawn_worker）
49	- 运行时长 < 5 分钟（初始化阶段崩溃）
50	- tail 日志中未见明确 Traceback 或错误行
51	- 同类实验连续失败 ≥ 2 次
52	
53	```python
54	spawn_worker(
55	    task_type="diagnose:{exp_id}",
56	    task_prompt="""SSH 到服务器 {server}，诊断实验 {exp_id} 的失败原因。
57	
58	项目路径：{project_path}（绝对路径）
59	日志路径：{log_path}（可能为空）
60	
61	执行步骤（按顺序，有结论就停）：
62	
63	1. 如果有日志路径：
64	   - 先看结尾 50 行（找 Traceback / Error / CUDA OOM）
65	   - 没找到明确错误：再看开头 100 行（初始化崩溃在这里）
66	   - 日志文件不存在：说明任务启动即失败，跳到步骤 2
67	
68	2. 日志无错误或无日志时，检查基础设施：
69	   - 入口文件是否存在
70	   - 激活环境并验证 import
71	   - 检查 configs/ 目录
72	
73	3. 检查磁盘/内存（OOM 类）
74	
75	最后输出一行 JSON：
76	{"root_cause":"<引用具体报错行>","error_type":"infrastructure|hyperparameter|resource|data","fix_steps":["步骤1","步骤2"],"can_auto_fix":true}""",
77	    tool_groups=["ssh"],
78	)
79	```
80	
81	Worker 返回后，以其结论作为 Step 3 的诊断依据。
82	
83	### 
…[truncated 1766 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:k2-l2-calibration-phase1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-19T21:00:03.780461+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "memory.md",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:k2-l2-calibration-phase1",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "file": "memory.md",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-19T21:00:03.781020+00:00_

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
  "session": "cron:hook:k2-l2-calibration-phase1",
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

_source line 28 · 2026-05-19T21:00:03.932048+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md\", \"content\": \"# Project Memory\\n\\n## 失败模式记录\\n\\n- [失败模式] Cron false positive：eval 脚本不写 W&B 也不写 sentinel file，进程正常退出后 cron 5 次检测找不到标记 → 自动标记为 failed。受影响：eval-vla-only-long-seed46, eval-vla-only-goal-seed46。修复方案：tail 日志确认实际完成 → 手动修正 conclusion=success + 补录 metrics。预防：eval 实验应检查 output JSON 是否存在作为 sentinel。\\n\\n- [失败模式] FMVD 信号无效：ODE velocity dispersion 与 K=10 action variance 几乎无相关性 (ρ=0.0825, 远低于 0.3 阈值)。根因：flow matching 的确定性 ODE 轨迹的 velocity norm 变异编码的是 denoising dynamics，而非 action-level uncertainty。per-task 方向不一致 (milk ρ=-0.284)。FMVD 分布极窄 (std=0.040)，无法区分 uncertain vs confident steps。**教训：zero-cost signal 不能假设有效——denoising 空间的统计量不一定映射到 action 空间的 uncertainty。K=2 L2 divergence (直接在 action 空间测量) 是更直觉的替代方案。**\\n\\n## LIBERO VLA-only Baselines (SmolVLA, K=1)\\n\\n### LIBERO-Goal (n=5)\\n| Seed | SR |\\n|------|------|\\n| seed42 | 71% |\\n| seed43 | 69% |\\n| seed44 | 73% |\\n| seed45 | 63% |\\n| seed46 | 71% |\\n| **Mean±Std** | **69.4%±3.8%** |\\n\\n### LIBERO-10 / Long (n=5)\\n| Seed | SR |\\n|------|------|\\n| seed42 | 11% |\\n| seed43 | 13% |\\n| seed44 | 12% |\\n| seed45 | 17% |\\n| seed46 | 18% |\\n| **Mean±Std** | **14.2%±3.1%** |\\n\\n## Spatial obs_only CRM (ε=0.2, K=10) Cross-seed Results (n=6)\\n\\n| Seed | SR |\\n|------|------|\\n| seed42 | 35% |\\n| seed43 | 34% |\\n| seed44 | 36% |\\n| seed45 | 34% |\\n| seed46 | 33% |\\n| seed47 | 32% |\\n| **Mean±Std** | **34.0%±1.4%** |\\n\\nSpatial VLA-only baseline: 29.3%±1.7% (n=4). CRM K=10 提升 ~4.7pp，统计显著。\\n\\n**观察**:\\n- 强二分性：3 个 task ≥80%，4 个 task 0%——CRM 修正对某些空间关系有效（next_to, between），对其他无效（on_stove, on_cabinet, on_ramekin）\\n- 0% task 跨 seed 稳定为 0%，说明这不是随机波动而是 CRM 在这些 task 上的系统性局限\\n\\n## CRM Coverage 限制\\n\\nCRM v3 训练数据 = Object(10) + Spatial(10) = 20 tasks。LIBERO-Goal 和 LIBERO-10 (Long) 的 tasks 不在训练覆盖范围内。CRM-Goal 和 CRM-Long 实验是 OOD 泛化测试——Director 已知并批准
…[truncated 324 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:k2-l2-calibration-phase1",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 151
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-19T21:00:03.932507+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [], \"count\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:k2-l2-calibration-phase1",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 151
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-19T21:00:32.006830+00:00_

called mcp__agent-ml-research__spawn_worker

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker</summary>

```json
{
  "task_type": "diagnose:k2-l2-calibration-phase1",
  "project": "acr-vla-conformal-refinement",
  "task_prompt": "SSH 到服务器 bjb2-28827，诊断实验 k2-l2-calibration-phase1 的实际状态。\n\n**背景**：\n- 这个实验运行的是 K=2 L2 divergence calibration（测试 action-space 不确定性信号）\n- 命令：`CUDA_VISIBLE_DEVICES=1 python -u src/calibrate_fmvd.py --benchmark object --n_episodes 5 --seed 42 --output logs/k2_l2_calibration.json`\n- Cron 报告 \"process dead 5× with no sentinel/W&B — auto-resolved as failed\"\n- **已知失败模式**：这类 calibration 脚本输出 JSON 而非 W&B，cron 检测不到 W&B 标记就自动标 failed，但实际上可能已成功完成\n\n**执行步骤**（按顺序，有结论就停）：\n\n1. **检查输出文件**：\n   - `ls -la ~/runs/acr-vla-conformal-refinement/logs/k2_l2_calibration.json` 或项目目录下的 `logs/k2_l2_calibration.json`\n   - 如果文件存在，`cat` 它，看结果是否完整（应包含 Spearman ρ 等指标）\n\n2. **检查日志**：\n   - 在 `~/runs/acr-vla-conformal-refinement/` 下找 k2-l2 相关的 .log 文件\n   - `find ~/runs/acr-vla-conformal-refinement/ -name \"*k2*\" -o -name \"*l2*calibration*\" | head -10`\n   - 也检查 tmux 日志：`ls -la /tmp/tmux_k2*` 或 `/tmp/tmux_*calibration*`\n   - 查看日志结尾 80 行，看是否有 Traceback / Error / 正常完成标志\n\n3. **如果没找到日志或输出**：\n   - 检查进程是否还在运行：`ps aux | grep calibrate_fmvd`\n   - 检查 tmux sessions：`tmux ls`\n   - 检查 dmesg 是否有 OOM kill：`dmesg | tail -30`\n   - 检查磁盘空间：`df -h /`\n\n4. **也顺便检查这两个同时失败的实验**（同一台服务器）：\n   - eval-vla-only-spatial-seed48（如果它也在 bjb2-28827）\n   - 看看是否存在系统性问题（服务器重启？GPU 故障？）\n\n**输出**：\n最后输出一行 JSON：\n{\"root_cause\":\"<引用具体证据>\",\"error_type\":\"infrastructure|false_positive|resource|data\",\"actually_succeeded\":true/false,\"metrics\":{如果成功则填写关键指标},\"fix_steps\":[\"步骤1\",\"步骤2\"]}",
  "tool_groups": "['ssh']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:k2-l2-calibration-phase1",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "tool_args": {
    "task_type": "diagnose:k2-l2-calibration-phase1",
    "project": "acr-vla-conformal-refinement",
    "task_prompt": "SSH 到服务器 bjb2-28827，诊断实验 k2-l2-calibration-phase1 的实际状态。\n\n**背景**：\n- 这个实验运行的是 K=2 L2 divergence calibration（测试 action-space 不确定性信号）\n- 命令：`CUDA_VISIBLE_DEVICES=1 python -u src/calibrate_fmvd.py --benchmark object --n_episodes 5 --seed 42 --output logs/k2_l2_calibration.json`\n- Cron 报告 \"process dead 5× with no sentinel/W&B — auto-resolved as failed\"\n- **已知失败模式**：这类 calibration 脚本输出 JSON 而非 W&B，cron 检测不到 W&B 标记就自动标 failed，但实际上可能已成功完成\n\n**执行步骤**（按顺序，有结论就停）：\n\n1. **检查输出文件**：\n   - `ls -la ~/runs/acr-vla-conformal-refinement/logs/k2_l2_calibration.json` 或项目目录下的 `logs/k2_l2_calibration.json`\n   - 如果文件存在，`cat` 它，看结果是否完整（应包含 Spearman ρ 等指标）\n\n2. **检查日志**：\n   - 在 `~/runs/acr-vla-conformal-refinement/` 下找 k2-l2 相关的 .log 文件\n   - `find ~/runs/acr-vla-conformal-refinement/ -name \"*k2*\" -o -name \"*l2*calibration*\" | head -10`\n   - 也检查 tmux 日志：`ls -la /tmp/tmux_k2*` 或 `/tmp/tmux_*calibration*`\n   - 查看日志结尾 80 行，看是否有 Traceback / Error / 正常完成标志\n\n3. **如果没找到日志或输出**：\n   - 检查进程是否还在运行：`ps aux | grep calibrate_fmvd`\n   - 检查 tmux sessions：`tmux ls`\n   - 检查 dmesg 是否有 OOM kill：`dmesg | tail -30`\n   - 检查磁盘空间：`df -h /`\n\n4. **也顺便检查这两个同时失败的实验**（同一台服务器）：\n   - eval-vla-only-spatial-seed48（如果它也在 bjb2-28827）\n   - 看看是否存在系统性问题（服务器重启？GPU 故障？）\n\n**输出**：\n最后输出一行 JSON：\n{\"root_cause\":\"<引用具体证据>\",\"error_type\":\"infrastructure|false_positive|resource|data\",\"actually_succeeded\":true/false,\"metrics\":{如果成功则填写关键指标},\"fix_steps\":[\"步骤1\",\"步骤2\"]}",
    "tool_groups": "['ssh']"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-19T21:00:35.877687+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_diagnose_k2-l2-calibration-phase1_20260519T210033\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_diagnose_k2-l2-calibration-phase1_20260519T210033.log\", \"setup_data\": {}, \"message\": \"Worker worker_diagnose_k2-l2-calibration-phase1_20260519T210033 started. Use get_worker_status('worker_diagnose_k2-l2-calibration-phase1_20260519T210033') to check progress.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:k2-l2-calibration-phase1",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "elapsed_ms": 3870
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-19T21:00:40.254621+00:00_

Worker 已派出诊断 k2-l2-calibration-phase1。基于 memory.md 记录的已知模式（calibration 脚本不写 W&B → cron 误判 failed），大概率是 false positive。等 Worker 回调确认实际结果后更新 registry 并汇报 Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:k2-l2-calibration-phase1"
}
```

</details>

---

## Round 2

2 recorded events

### User

_source line 33 · 2026-05-19T21:00:40.268373+00:00_

[CRON] 实验进程异常退出（失败），需要你诊断原因。
详情: Process exited without valid W&B metrics

- exp_id: k2-l2-calibration-phase1
- project: acr-vla-conformal-refinement
- server: bjb2-28827

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:k2-l2-calibration-phase1",
  "source": "cron:hook"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-19T21:00:48.425651+00:00_

已在处理中——已派 Worker `worker_diagnose_k2-l2-calibration-phase1_20260519T210033` 诊断此实验，等待回调。这是同一个 cron 的重复通知，不再重复派发。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:k2-l2-calibration-phase1"
}
```

</details>

---
