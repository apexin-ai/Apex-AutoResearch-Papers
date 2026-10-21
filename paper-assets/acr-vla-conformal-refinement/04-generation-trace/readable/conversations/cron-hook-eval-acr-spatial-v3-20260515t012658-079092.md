# cron hook eval acr spatial v3 20260515T012658 079092

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 69
- **Recorded user turns:** 5
- **Tool calls:** 32
- **Original source:** `logs/chats/archive/cron_hook_eval-acr-spatial-v3_20260515T012658_079092.jsonl`
- **Structured JSON:** [`9e5c8b28b81e97269b4e.json`](../../sessions/9e/9e5c8b28b81e97269b4e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

40 recorded events

### User

_source line 1 · 2026-05-14T20:18:46.950463+00:00_

[CRON] 实验进程异常退出（失败），需要你诊断原因。
详情: Process exited without valid W&B metrics

- exp_id: eval-acr-spatial-v3
- project: acr-vla-conformal-refinement
- server: bjb1-18228

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:eval-acr-spatial-v3",
  "source": "cron:hook"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-14T20:18:57.654098+00:00_

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
  "session": "cron:hook:eval-acr-spatial-v3",
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

_source line 3 · 2026-05-14T20:18:57.654514+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-14T20:18:58.865164+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__load_project_config",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__load_project_config",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-14T20:18:58.916564+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T20:19:04.738321+00:00_

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
  "session": "cron:hook:eval-acr-spatial-v3",
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

_source line 7 · 2026-05-14T20:19:04.788911+00:00_

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
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-14T20:19:04.889645+00:00_

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
  "session": "cron:hook:eval-acr-spatial-v3",
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

_source line 9 · 2026-05-14T20:19:04.940353+00:00_

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
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T20:19:05.292395+00:00_

Error: result (79,147 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-699cc919/76674e92-79de-4779-b8e4-4a6638a902ed/tool-results/mcp-agent-ml-research-read_registry-1778789945230.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-699cc919/76674e92-79de-4779-b8e4-4a6638a902ed/tool-results/mcp-agent-ml-research-read_registry-1778789945230.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 554
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-14T20:19:10.161192+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 3, \"results\": [{\"exp_id\": \"eval-vla-mean-spatial\", \"success\": true, \"actions\": [\"Job still running (pid=143106)\"]}, {\"exp_id\": \"eval-argmin-only-spatial\", \"success\": true, \"actions\": [\"Job still running (pid=231421)\"]}, {\"exp_id\": \"eval-tiny-correction-spatial\", \"success\": true, \"actions\": [\"Job still running (pid=232815)\"]}]}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 5372
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T20:19:10.161845+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-14T20:18:54Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 63 个实验 — DONE 44, PREPARING 16, RUNNING 3\\n**DONE 分布**: failed 7, killed 22, success 15\\n\\n### GPU 占用\\n- **实际运行**: 3 张 — bjb2-40593:cuda:0(eval-vla-mean-spatial), bjb1-18228:cuda:1(eval-argmin-only-spatial), bjb1-18228:cuda:2(eval-tiny-correction-spatial)\\n\\n### 🏃 RUNNING\\n| exp_id | server | gpu | pid | log |\\n|--------|--------|-----|-----|-----|\\n| `eval-vla-mean-spatial` | bjb2-40593 | cuda:0 | 143106 | `/root/autodl-tmp/eval_results/eval-vla-mean-spatial.log` |\\n| `eval-argmin-only-spatial` | bjb1-18228 | cuda:1 | 231421 | `…s/acr-vla-conformal-refinement/eval-argmin-only-spatial.log` |\\n| `eval-tiny-correction-spatial` | bjb1-18228 | cuda:2 | 232815 | `…r-vla-conformal-refinement/eval-tiny-correction-spatial.log` |\\n\\n### 📌 最近完成 (top 5)\\n- `eval-acr-object-v3` [failed] — 2026-05-14T20:18:54 — process dead 5× with no sentinel/W&B — auto-resolved as failed\\n- `eval-acr-spatial-v3` [failed] — 2026-05-14T20:18:45 — process dead 5× with no sentinel/W&B — auto-resolved as failed\\n- `crm-train-v3-norm` [success] — 2026-05-14T20:05:22\\n- `crm-train-v3-scalar-unc` [killed] — 2026-05-14T18:37:14\\n- `crm-train-v3-obs-only` [killed] — 2026-05-14T18:37:04\\n\\n### 🔴 最近失败原因 (top 3)\\n- `eval-acr-object-v3`: process dead 5× with no sentinel/W&B — auto-resolved as failed\\n- `eval-acr-spatial-v3`: process dead 5× with no sentinel/W&B — auto-resolved as failed\\n- `crm-train-v3-scalar-unc`: _(no failure_reason — pre-2026-04-24 entry)_\\n\\n&lt;!-- AUTO-FACTS-END -->\\n\\n---\\n\\n# Handover — 2026-05-14\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n
…[truncated 2962 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 5272
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-14T20:19:10.212622+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-14 16:00 UTC | 更新原因: crm-train-k5 完成 + eval-k5-spatial 启动，竞品分析完成，CRM correction 退化现象确认\\n\\n## 核心方向\\nPer-DOF conformal statistics from multivariate CP on flow-matching VLA samples enable dimension-selective action correction. 详见 paper_framing.md。\\n\\n## 投稿目标\\n**ICLR 2027**（预计 DDL Sep-Oct 2026）。CoRL 2026 已放弃（D011）。\\n\\n## 当前进展\\n- **阶段**: Phase 2 — Spatial Eval 四路对比（ACR-VLA / SampleConsensus / Scalar-CRM / VLA-mean）\\n- **MVP**: PASS（plan_000, per-DOF > scalar > none 确认）\\n- **SFT Gate**: 30% baseline，决定继续（D015）\\n- **CRM 训练完成**: per-DOF val_loss=0.009, scalar_unc=0.008, obs_only=0.018（conformal features 2× 改善确认）\\n- **Baselines 锁定**: spatial 30% (K=1), object 13% (K=1)\\n- **早期信号（2/10 tasks，不构成结论）**: ACR-VLA 在简单任务上低于 baseline，per-DOF CRM 可能在简单任务上引入有害 correction\\n- **竞品分析完成** (art_20260514_621600): 核心竞品 ReconVLA（最直接）、SC-VLA、VLA-Pilot、ACoT-VLA\\n- **CRM correction 退化现象**: ACR-VLA 中间结果 (23-26%) 低于 baseline (30%)，SampleConsensus 领先 (42.9%)\\n- **文献调研完成** (art_20260514_d21dd2): correction degradation 可能原因与补救方向（correction clipping/gating 等）\\n\\n## 近期任务\\n- [ ] eval-acr-spatial-v2 完成 → 核心 claim 判定（ACR-VLA vs baseline 30%）\\n- [ ] eval-reconvla-spatial-v3 完成 → SampleConsensus 对比\\n- [ ] eval-scalar-unc-spatial 完成 → scalar vs per-DOF 最终裁决\\n- [x] crm-train-k5 完成 → K sensitivity ablation + eval-k5-spatial 已启动\\n- [ ] eval-k5-spatial 完成 → K=5 sensitivity ablation 结果\\n- [ ] eval-vla-mean-spatial 完成 → 隔离多采样平均贡献\\n- [x] 代码同步 bjb1→bjb2（evaluate.py + train_crm.py）— MD5 verified\\n- [ ] 完整 spatial 四路对比表出炉 → 决定是否铺 object benchmark\\n- [ ] paper_framing.md 更新竞品定位（SC-VLA, VLA-Pilot, ACoT-VLA SOTA）\\n\\n## SFT Gate\\nD015: 30% baseline 继续推进。核心关注相对提升，非绝对值。\\n\\n## GPU 预算\\n- bjb1-18228 (4× RTX 4090): eval-k5-spatial(cuda:0) + eval-acr(cuda:1) 
…[truncated 1734 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 5272
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-14T20:19:15.935614+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'exp_id': 'eval-acr-spatial-v3'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'exp_id': 'eval-acr-spatial-v3'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-14T20:19:16.337052+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.128}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 401
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-14T20:19:16.538459+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'exp_id': 'eval-acr-object-v3'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'exp_id': 'eval-acr-object-v3'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-14T20:19:16.689284+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1349}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 150
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-14T20:19:24.601459+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-699cc919/76674e92-79de-4779-b8e4-4a6638a902ed/tool-results/mcp-agent-ml-research-read_registry-1778789945230.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\nfor eid in ['eval-acr-spatial-v3', 'eval-acr-object-v3']:\n    if eid in exps:\n        print(f'=== {eid} ===')\n        print(json.dumps(exps[eid], indent=2))\n    else:\n        print(f'{eid}: NOT FOUND')\n\"",
  "description": "Extract eval-acr-spatial-v3 and eval-acr-object-v3 from registry dump"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-699cc919/76674e92-79de-4779-b8e4-4a6638a902ed/tool-results/mcp-agent-ml-research-read_registry-1778789945230.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\nfor eid in ['eval-acr-spatial-v3', 'eval-acr-object-v3']:\n    if eid in exps:\n        print(f'=== {eid} ===')\n        print(json.dumps(exps[eid], indent=2))\n    else:\n        print(f'{eid}: NOT FOUND')\n\"",
    "description": "Extract eval-acr-spatial-v3 and eval-acr-object-v3 from registry dump"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-14T20:19:24.854138+00:00_

=== eval-acr-spatial-v3 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-14T12:17:06.073Z",
  "updated_at": "2026-05-14T20:18:45.380Z",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt\"",
    "server": "bjb1-18228",
    "gpu": [
      "cuda:0"
    ],
    "pid": "197057",
    "log_path": "~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v3.log",
    "submitted_at": "2026-05-14T12:17:05.974Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "/root/autodl-tmp/libero_data/ (spatial benchmark)",
    "data_count": 100,
    "model_name": "ACR-VLA (CRM v2 per-DOF + SmolVLA K=10)",
    "seed": 42,
    "hypothesis": "Per-DOF conformal correction (ACR-VLA with D016 4-bug fix) outperforms VLA K=1 (30%) and SampleConsensus (34%) on LIBERO spatial. CORE CLAIM experiment.",
    "checkpoint_source": "/root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt",
    "eval_data": "LIBERO spatial 10 tasks x 10 rollouts",
    "wall_clock_seconds": 28899.4,
    "gpu_hours": 8.03
  },
  "metrics": {
    "tasks_done": "4/10",
    "overall_success_rate": 0.025,
    "total_successes": 1,
    "total_rollouts": 40,
    "per_task_partial": {
      "pick_up_black_bowl_between_plate_and_ramekin": 0.1,
      "pick_up_black_bowl_next_to_ramekin": 0,
      "pick_up_black_bowl_from_table_center": 0,
      "pick_up_black_bowl_on_cookie_box": 0
    },
    "snapshot_time": "2026-05-14T18:15Z"
  },
  "conclusion": "failed",
  "reproduce": {
    "finished_at": "2026-05-14T20:18:44.725Z"
  },
  "failure_reason": "process dead 5\u00d7 with no sentinel/W&B \u2014 auto-resolved as failed",
  "completed_at"
…[truncated 2253 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "Bash",
  "elapsed_ms": 252
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-14T20:19:42.463648+00:00_

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
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/skills/on-experiment-failed.skill.md"
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T20:19:42.464301+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/skills/resource-saturation.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/skills/resource-saturation.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T20:19:42.516433+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/sessions/agent_699cc919.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-14T20:19:42.516841+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/sessions/agent_699cc919.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-14T20:19:45.276828+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-14T20:19:45.328430+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "Glob",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-14T20:19:48.590230+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/skills/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/skills/**",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-14T20:19:48.640930+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-14T20:19:52.111332+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_8 -name \"*.skill.md\" -type f 2>/dev/null | head -5; find /home/ubuntu/agent-ml-research -name \"on-experiment-failed.skill.md\" -type f 2>/dev/null | head -5",
  "description": "Find skill files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_8 -name \"*.skill.md\" -type f 2>/dev/null | head -5; find /home/ubuntu/agent-ml-research -name \"on-experiment-failed.skill.md\" -type f 2>/dev/null | head -5",
    "description": "Find skill files"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-14T20:19:52.312458+00:00_

/home/ubuntu/agent-ml-research/skills/global/on-experiment-failed.skill.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-14T20:19:55.727495+00:00_

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
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/on-experiment-failed.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-14T20:19:55.728077+00:00_

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
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-14T20:20:15.196322+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "file": "memory.md"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-14T20:20:15.598684+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md\", \"content\": \"# Memory — acr-vla-conformal-refinement\\n\\n## Correction Magnitude 是核心问题（2026-05-14 18:15，早期信号）\\n\\n### 发现\\neval-tiny-correction-spatial（max_correction_norm=0.05，约默认 1.42 的 1/28）在首个 task 上 4/5 成功，而 full ACR 同一 task 只有 1/10。这说明 CRM correction 的方向可能是对的，但幅度太大导致 compounding error。\\n\\n### 含义\\n- correction clipping / gating 是正确的补救方向\\n- Gated CRM 代码已就绪（`src/gated_crm.py` + `--mode acr_gated` + `--gate_threshold/mode/temperature`）\\n- 等完整 eval 结果确认后，下一步应该是 correction magnitude sweep（0.01, 0.05, 0.1, 0.2, 0.5）或 Gated CRM eval\\n- **不改变目标 venue（ICLR 2027）**，narrative 可从 \\\"per-DOF correction always helps\\\" 调整为 \\\"per-DOF correction with magnitude control\\\"\\n\\n### ⚠️ 注意\\n这是 1 个 task 的 5 个 rollout 的早期数据。需要完整 10 tasks 确认。\\n\\n## Correction Magnitude 文献支撑（2026-05-14 18:37）\\n\\n### 核心竞品/支撑论文\\n1. **PLD (ICLR 2026)**: scheduled ξ bound，LIBERO ξ=0.5 / SimplerEnv ξ=0.1——不同环境需不同 correction scale，完全验证我们的发现\\n2. **TRANSIC (CoRL 2024)**: 无 gate 时 fine-tuning 导致 model collapse——与我们 40%→2.5% 退化一致\\n3. **ResiP (CoRL-W 2024)**: scaling α≤1，关键不是精确值而是 order of magnitude\\n4. **DRC (2025)**: temporal decay of correction\\n5. **DAWN (2026)**: scale mismatch → residual 学不好\\n\\n### 独特贡献角度\\n**没有现有方法提供 per-DOF, per-timestep, calibrated magnitude bounds。** ACR-VLA 的 conformal intervals 天然提供 calibrated bounds on expected action range。\\n\\n### 推荐 Framing 调整方向\\n\\\"Conformally-Calibrated Correction Magnitude\\\" — CP intervals 作为 correction 幅度的自然上界，不依赖固定超参数（α, ξ）或 binary gate。\\n\\n### 对比表（可用于论文 Table 1）\\n| Method | Bound Type | Per-DOF | Per-Timestep | Calibrated |\\n|--------|-----------|---------|-------------|------------|\\n| Silver 2018 | Action space | ✗ | ✗ | ✗ |\\n| Johannink 2019 | Fixed tube | ✗ | ✗ | ✗ |\\n| TRANSIC 2024 | Binary gate | ✗ | ✓ | ✗ |\\n| PLD 2026 | Scheduled ξ | ✗ | ~ | ✗ |\\n| **ACR-VLA*
…[truncated 5515 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 402
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-14T20:20:15.599168+00:00_

called mcp__agent-ml-research__load_project_config

<details open><summary>🔧 Tool call — mcp__agent-ml-research__load_project_config</summary>

```json
{
  "project_name": "acr-vla-conformal-refinement",
  "section": "execution"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "mcp__agent-ml-research__load_project_config",
  "tool_args": {
    "project_name": "acr-vla-conformal-refinement",
    "section": "execution"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-14T20:20:15.649890+00:00_

{"result":"{\"success\": true, \"data\": {\"project\": \"acr-vla-conformal-refinement\", \"section\": \"execution\", \"config\": {\"execution\": {\"account\": \"root\", \"gpu_constraint\": [\"autodl-4090:cuda:0\"], \"gpu_ids\": [\"bjb2-40593:cuda:0\", \"bjb1-18228:cuda:0\", \"bjb1-18228:cuda:1\", \"bjb1-18228:cuda:2\", \"bjb1-18228:cuda:3\"], \"project_path\": \"/root/acr-vla-conformal-refinement\", \"servers\": [\"bjb2-40593\", \"bjb1-18228\"]}}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "mcp__agent-ml-research__load_project_config",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-14T20:20:53.205833+00:00_

called mcp__agent-ml-research__spawn_worker

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker</summary>

```json
{
  "task_type": "diagnose:eval-acr-spatial-v3",
  "project": "acr-vla-conformal-refinement",
  "task_prompt": "SSH 到服务器 bjb1-18228，诊断两个失败实验的 crash 原因。\n\n## 背景\n两个 eval 实验在跑到 4/10 tasks 后进程死亡（process dead 5× with no sentinel/W&B）。\n- eval-acr-spatial-v3: pid 197057, cuda:0, 8h wall time, 2.5% success (1/40)\n- eval-acr-object-v3: pid 197803, cuda:3, 8h wall time, 0% success (0/40)\n\n项目路径: /root/acr-vla-conformal-refinement\n\n## 执行步骤\n\n1. 检查 eval-acr-spatial-v3 日志:\n   - `tail -100 ~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v3.log`\n   - 找 Traceback / OOM / CUDA error / Segfault / 任何异常\n   - 如果尾部没有错误，看 `head -50` 检查初始化\n\n2. 检查 eval-acr-object-v3 日志:\n   - `tail -100 ~/runs/acr-vla-conformal-refinement/eval-acr-object-v3.log`\n   - 同样找错误信息\n\n3. 检查系统层面:\n   - `dmesg | grep -i \"oom\\|killed\\|segfault\" | tail -20` 看是否 OOM killer\n   - `nvidia-smi` 当前 GPU 状态\n   - `df -h /root` 和 `df -h /root/autodl-tmp` 检查磁盘\n\n4. 检查进程是否还有残留: `ps aux | grep evaluate`\n\n5. 检查 tmux sessions: `tmux ls` 和如果相关 session 存在则 `tmux capture-pane -t &lt;session> -p`\n\n最后输出一行 JSON：\n{\"root_cause\":\"<引用具体报错行>\",\"error_type\":\"infrastructure|hyperparameter|resource|data\",\"fix_steps\":[\"步骤1\",\"步骤2\"],\"can_auto_fix\":true,\"affects_both\":true}\n\n注意：这两个实验用的是旧的 un-normalized CRM checkpoint，已被 D018 判定为有根本性 scale 问题。诊断主要是为了记录 crash 原因，不需要修复——后续会用 v3-norm checkpoint 重新跑。",
  "tool_groups": "['ssh']",
  "context": "服务器 bjb1-18228 使用 conda 环境: source /root/miniconda3/etc/profile.d/conda.sh && conda activate base。项目路径 /root/acr-vla-conformal-refinement。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "tool_args": {
    "task_type": "diagnose:eval-acr-spatial-v3",
    "project": "acr-vla-conformal-refinement",
    "task_prompt": "SSH 到服务器 bjb1-18228，诊断两个失败实验的 crash 原因。\n\n## 背景\n两个 eval 实验在跑到 4/10 tasks 后进程死亡（process dead 5× with no sentinel/W&B）。\n- eval-acr-spatial-v3: pid 197057, cuda:0, 8h wall time, 2.5% success (1/40)\n- eval-acr-object-v3: pid 197803, cuda:3, 8h wall time, 0% success (0/40)\n\n项目路径: /root/acr-vla-conformal-refinement\n\n## 执行步骤\n\n1. 检查 eval-acr-spatial-v3 日志:\n   - `tail -100 ~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v3.log`\n   - 找 Traceback / OOM / CUDA error / Segfault / 任何异常\n   - 如果尾部没有错误，看 `head -50` 检查初始化\n\n2. 检查 eval-acr-object-v3 日志:\n   - `tail -100 ~/runs/acr-vla-conformal-refinement/eval-acr-object-v3.log`\n   - 同样找错误信息\n\n3. 检查系统层面:\n   - `dmesg | grep -i \"oom\\|killed\\|segfault\" | tail -20` 看是否 OOM killer\n   - `nvidia-smi` 当前 GPU 状态\n   - `df -h /root` 和 `df -h /root/autodl-tmp` 检查磁盘\n\n4. 检查进程是否还有残留: `ps aux | grep evaluate`\n\n5. 检查 tmux sessions: `tmux ls` 和如果相关 session 存在则 `tmux capture-pane -t &lt;session> -p`\n\n最后输出一行 JSON：\n{\"root_cause\":\"<引用具体报错行>\",\"error_type\":\"infrastructure|hyperparameter|resource|data\",\"fix_steps\":[\"步骤1\",\"步骤2\"],\"can_auto_fix\":true,\"affects_both\":true}\n\n注意：这两个实验用的是旧的 un-normalized CRM checkpoint，已被 D018 判定为有根本性 scale 问题。诊断主要是为了记录 crash 原因，不需要修复——后续会用 v3-norm checkpoint 重新跑。",
    "tool_groups": "['ssh']",
    "context": "服务器 bjb1-18228 使用 conda 环境: source /root/miniconda3/etc/profile.d/conda.sh && conda activate base。项目路径 /root/acr-vla-conformal-refinement。"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-14T20:20:55.818516+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_diagnose_eval-acr-spatial-v3_20260514T202053\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_diagnose_eval-acr-spatial-v3_20260514T202053.log\", \"setup_data\": {}, \"message\": \"Worker worker_diagnose_eval-acr-spatial-v3_20260514T202053 started. Use get_worker_status('worker_diagnose_eval-acr-spatial-v3_20260514T202053') to check progress.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "elapsed_ms": 2612
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-14T20:21:10.104459+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-acr-spatial-v3",
  "field": "notes",
  "value": "失败原因: 进程在完成 4/10 tasks 后死亡（process dead 5×，无 W&B sentinel）| 已有成果: 4 tasks 完成，overall 2.5% (1/40)，per_task: pick_up_black_bowl_between_plate_and_ramekin=10%, 其余 3 个=0% | 背景: 使用旧 un-normalized CRM checkpoint (crm_v2/perdof)，D018 已确认 1500x scale 失衡为根因。此实验结果不具参考价值 | 后续: 等 v3-norm checkpoint eval (v4 系列)",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-acr-spatial-v3",
    "field": "notes",
    "value": "失败原因: 进程在完成 4/10 tasks 后死亡（process dead 5×，无 W&B sentinel）| 已有成果: 4 tasks 完成，overall 2.5% (1/40)，per_task: pick_up_black_bowl_between_plate_and_ramekin=10%, 其余 3 个=0% | 背景: 使用旧 un-normalized CRM checkpoint (crm_v2/perdof)，D018 已确认 1500x scale 失衡为根因。此实验结果不具参考价值 | 后续: 等 v3-norm checkpoint eval (v4 系列)",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-14T20:21:11.760768+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-acr-object-v3",
  "field": "notes",
  "value": "失败原因: 进程在完成 4/10 tasks 后死亡（process dead 5×，无 W&B sentinel）| 已有成果: 4 tasks 完成，overall 0% (0/40) | 背景: 使用旧 un-normalized CRM checkpoint (crm_v2/perdof)，D018 已确认 1500x scale 失衡为根因。此实验结果不具参考价值 | 后续: 等 v3-norm checkpoint eval (v4 系列)",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-acr-object-v3",
    "field": "notes",
    "value": "失败原因: 进程在完成 4/10 tasks 后死亡（process dead 5×，无 W&B sentinel）| 已有成果: 4 tasks 完成，overall 0% (0/40) | 背景: 使用旧 un-normalized CRM checkpoint (crm_v2/perdof)，D018 已确认 1500x scale 失衡为根因。此实验结果不具参考价值 | 后续: 等 v3-norm checkpoint eval (v4 系列)",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-14T20:38:47.323032+00:00_

Worker 已派出诊断。现在更新两个实验的 registry notes，然后向 Director 汇报。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval-acr-spatial-v3"
}
```

</details>

---

## Round 2

1 recorded events

### User

_source line 41 · 2026-05-15T00:11:40.938643+00:00_

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
  "session": "cron:hook:eval-acr-spatial-v3",
  "source": "system:ralph_loop"
}
```

</details>

---

## Round 3

1 recorded events

### User

_source line 42 · 2026-05-15T00:11:47.741943+00:00_

你上一条回复没有用 &lt;handoff>...&lt;/handoff> 标签包裹(第 1/2 次提醒)。这是硬约束，请重新写,整条回复只能是 &lt;handoff>...&lt;/handoff> 包裹的正文,禁止任何标签外的寒暄或说明。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:eval-acr-spatial-v3",
  "source": "system:ralph_loop"
}
```

</details>

---

## Round 4

1 recorded events

### User

_source line 43 · 2026-05-15T00:11:51.584648+00:00_

你上一条回复没有用 &lt;handoff>...&lt;/handoff> 标签包裹(第 2/2 次提醒)。这是硬约束，请重新写,整条回复只能是 &lt;handoff>...&lt;/handoff> 包裹的正文,禁止任何标签外的寒暄或说明。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:eval-acr-spatial-v3",
  "source": "system:ralph_loop"
}
```

</details>

---

## Round 5

26 recorded events

### User

_source line 44 · 2026-05-15T01:24:34.641795+00:00_

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
  "session": "cron:hook:eval-acr-spatial-v3",
  "source": "system:ralph_loop"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-15T01:25:09.768517+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__load_project_config",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__load_project_config",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-15T01:25:09.769023+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-15T01:25:16.710406+00:00_

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
  "session": "cron:hook:eval-acr-spatial-v3",
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

_source line 48 · 2026-05-15T01:25:17.163446+00:00_

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
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "file": "report.md"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-15T01:25:17.666804+00:00_

Error: result (89,846 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-699cc919/cf8a45d0-439c-47cd-9ec3-c571a93e3702/tool-results/mcp-agent-ml-research-read_registry-1778808317383.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-699cc919/cf8a45d0-439c-47cd-9ec3-c571a93e3702/tool-results/mcp-agent-ml-research-read_registry-1778808317383.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 956
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-15T01:25:17.667718+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md\", \"content\": \"# Handover — 2026-05-14\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| eval-acr-spatial-v4-default-r2 | D018 retry: Normalization alone fixes CRM correction degradation. v3-norm per-DOF checkpoint with default max_correction_norm (~1.42). If >30% baseline → normalization was the main fix. If still < 30% → magnitude control also needed (compare with v4-small at 0.1). | — | — | — |\\n| eval-vla-mean-spatial-t10 | — | — | — | — |\\n| eval-acr-spatial-v4-small | D018: Normalization + moderate correction scaling (max_correction_norm=0.1, 14x smaller than default). If v4-small > v4-default → magnitude control needed on top of normalization. | — | — | — |\\n\\n## 待处理\\n- eval-acr-spatial-v4-scalar: D020: scalar_unc CRM (val_loss 0.0374) with max_correction_norm=0.1. Three-way ablation: perdof vs scalar_unc vs obs_only under identical correction magnitude.（准备中）\\n- eval-object-v6-full（准备中）\\n- eval-reconvla-spatial-v1（准备中）\\n- precompute-v4-shard2（准备中）\\n- precompute-v4-shard1（准备中）\\n- precompute-v4-shard0（准备中）\\n- eval-spatial-v4-full（准备中）\\n- precompute-v3-shard2（准备中）\\n- precompute-v3-shard1（准备中）\\n- precompute-v3-shard0（准备中）\\n- …另有 3 项\\n\\n## 近期结论\\n- **eval-acr-spatial-v4-obs-only-r2** (killed): D020: obs_only CRM v3-norm (val_loss 0.0165) with max_correction_norm=0.1. If obs_only >= v4-small (perdof) → Claim 1 needs restructuring. If obs_only < v4-small → conformal features have unique value under distribution shift.\\n- **eval-acr-spatial-v4-obs-only** (failed): D020: obs_only CRM (val_loss 0.0165, 54% better than perdof 0.0358) with max_correction_norm=0.1. If obs_only >= v4-small (perdof) → Claim 1 needs restructuring. If obs_only < v4-small → conformal features have unique value under distribution shift.\\n- **
…[truncated 1632 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 504
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-15T01:25:17.769092+00:00_

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
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-15T01:25:17.920239+00:00_

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
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-15T01:25:17.920855+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-14 16:00 UTC | 更新原因: crm-train-k5 完成 + eval-k5-spatial 启动，竞品分析完成，CRM correction 退化现象确认\\n\\n## 核心方向\\nPer-DOF conformal statistics from multivariate CP on flow-matching VLA samples enable dimension-selective action correction. 详见 paper_framing.md。\\n\\n## 投稿目标\\n**ICLR 2027**（预计 DDL Sep-Oct 2026）。CoRL 2026 已放弃（D011）。\\n\\n## 当前进展\\n- **阶段**: Phase 2 — Spatial Eval 四路对比（ACR-VLA / SampleConsensus / Scalar-CRM / VLA-mean）\\n- **MVP**: PASS（plan_000, per-DOF > scalar > none 确认）\\n- **SFT Gate**: 30% baseline，决定继续（D015）\\n- **CRM 训练完成**: per-DOF val_loss=0.009, scalar_unc=0.008, obs_only=0.018（conformal features 2× 改善确认）\\n- **Baselines 锁定**: spatial 30% (K=1), object 13% (K=1)\\n- **早期信号（2/10 tasks，不构成结论）**: ACR-VLA 在简单任务上低于 baseline，per-DOF CRM 可能在简单任务上引入有害 correction\\n- **竞品分析完成** (art_20260514_621600): 核心竞品 ReconVLA（最直接）、SC-VLA、VLA-Pilot、ACoT-VLA\\n- **CRM correction 退化现象**: ACR-VLA 中间结果 (23-26%) 低于 baseline (30%)，SampleConsensus 领先 (42.9%)\\n- **文献调研完成** (art_20260514_d21dd2): correction degradation 可能原因与补救方向（correction clipping/gating 等）\\n\\n## 近期任务\\n- [ ] eval-acr-spatial-v2 完成 → 核心 claim 判定（ACR-VLA vs baseline 30%）\\n- [ ] eval-reconvla-spatial-v3 完成 → SampleConsensus 对比\\n- [ ] eval-scalar-unc-spatial 完成 → scalar vs per-DOF 最终裁决\\n- [x] crm-train-k5 完成 → K sensitivity ablation + eval-k5-spatial 已启动\\n- [ ] eval-k5-spatial 完成 → K=5 sensitivity ablation 结果\\n- [ ] eval-vla-mean-spatial 完成 → 隔离多采样平均贡献\\n- [x] 代码同步 bjb1→bjb2（evaluate.py + train_crm.py）— MD5 verified\\n- [ ] 完整 spatial 四路对比表出炉 → 决定是否铺 object benchmark\\n- [ ] paper_framing.md 更新竞品定位（SC-VLA, VLA-Pilot, ACoT-VLA SOTA）\\n\\n## SFT Gate\\nD015: 30% baseline 继续推进。核心关注相对提升，非绝对值。\\n\\n## GPU 预算\\n- bjb1-18228 (4× RTX 4090): eval-k5-spatial(cuda:0) + eval-acr(cuda:1) 
…[truncated 1923 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 151
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-15T01:25:18.172656+00:00_

called mcp__agent-ml-research__load_project_config

<details open><summary>🔧 Tool call — mcp__agent-ml-research__load_project_config</summary>

```json
{
  "project_name": "acr-vla-conformal-refinement",
  "section": "execution"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "mcp__agent-ml-research__load_project_config",
  "tool_args": {
    "project_name": "acr-vla-conformal-refinement",
    "section": "execution"
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-15T01:25:26.797989+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 4, \"results\": [{\"exp_id\": \"eval-argmin-only-spatial\", \"success\": true, \"actions\": [\"Job still running (pid=231421)\"]}, {\"exp_id\": \"eval-tiny-correction-spatial\", \"success\": true, \"actions\": [\"Job still running (pid=232815)\"]}, {\"exp_id\": \"eval-acr-spatial-v4-small\", \"success\": true, \"actions\": [\"Job still running (pid=253085)\"]}, {\"exp_id\": \"eval-acr-spatial-v4-obs-only-r2\", \"success\": true, \"actions\": [\"Job still running (pid=270097)\"]}]}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 8877
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-15T01:25:26.850501+00:00_

{"result":"{\"success\": true, \"data\": {\"project\": \"acr-vla-conformal-refinement\", \"section\": \"execution\", \"config\": {\"execution\": {\"account\": \"root\", \"gpu_constraint\": [\"autodl-4090:cuda:0\"], \"gpu_ids\": [\"bjb2-40593:cuda:0\", \"bjb1-18228:cuda:0\", \"bjb1-18228:cuda:1\", \"bjb1-18228:cuda:2\", \"bjb1-18228:cuda:3\"], \"project_path\": \"/root/acr-vla-conformal-refinement\", \"servers\": [\"bjb2-40593\", \"bjb1-18228\"]}}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "mcp__agent-ml-research__load_project_config",
  "elapsed_ms": 8677
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-15T01:25:39.034930+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-699cc919/cf8a45d0-439c-47cd-9ec3-c571a93e3702/tool-results/mcp-agent-ml-research-read_registry-1778808317383.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\nprint(f'Total experiments: {len(exps)}')\nprint()\nfor e in exps:\n    status = e.get('status', '?')\n    exp_id = e.get('exp_id', '?')\n    conclusion = e.get('conclusion', '')\n    server = e.get('server', '')\n    gpu = e.get('gpu', '')\n    hypothesis = e.get('hypothesis', '')[:80] if e.get('hypothesis') else ''\n    print(f'{exp_id} | {status} | {conclusion} | {server}:{gpu} | {hypothesis}')\n\"",
  "description": "Parse registry to get experiment summary"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-699cc919/cf8a45d0-439c-47cd-9ec3-c571a93e3702/tool-results/mcp-agent-ml-research-read_registry-1778808317383.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\nprint(f'Total experiments: {len(exps)}')\nprint()\nfor e in exps:\n    status = e.get('status', '?')\n    exp_id = e.get('exp_id', '?')\n    conclusion = e.get('conclusion', '')\n    server = e.get('server', '')\n    gpu = e.get('gpu', '')\n    hypothesis = e.get('hypothesis', '')[:80] if e.get('hypothesis') else ''\n    print(f'{exp_id} | {status} | {conclusion} | {server}:{gpu} | {hypothesis}')\n\"",
    "description": "Parse registry to get experiment summary"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-15T01:25:39.490921+00:00_

Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 9, in &lt;module>
    status = e.get('status', '?')
             ^^^^^
AttributeError: 'str' object has no attribute 'get'
Total experiments: 68

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "Bash",
  "elapsed_ms": 455
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-15T01:25:39.691807+00:00_

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
  "session": "cron:hook:eval-acr-spatial-v3",
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

### Tool result

_source line 60 · 2026-05-15T01:25:39.692132+00:00_

&lt;tool_use_error>Cancelled: parallel tool call Bash(cat /home/ubuntu/.claude-account-2/proje…) errored&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-15T01:25:45.818197+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-699cc919/cf8a45d0-439c-47cd-9ec3-c571a93e3702/tool-results/mcp-agent-ml-research-read_registry-1778808317383.txt | python3 -c \"\nimport json, sys\nraw = sys.stdin.read()\ndata = json.loads(raw)\nresult_str = data['result']\nresult = json.loads(result_str)\nexps = result['data']['experiments']\nprint(f'Total: {len(exps)}')\nfor e in exps:\n    if isinstance(e, dict):\n        print(f\\\"{e.get('exp_id','?')} | {e.get('status','?')} | {e.get('conclusion','')} | {e.get('server','')}\\\")\n    else:\n        print(f'Non-dict entry: {type(e)}: {str(e)[:100]}')\n\" 2>&1 | head -80",
  "description": "Parse registry experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-699cc919/cf8a45d0-439c-47cd-9ec3-c571a93e3702/tool-results/mcp-agent-ml-research-read_registry-1778808317383.txt | python3 -c \"\nimport json, sys\nraw = sys.stdin.read()\ndata = json.loads(raw)\nresult_str = data['result']\nresult = json.loads(result_str)\nexps = result['data']['experiments']\nprint(f'Total: {len(exps)}')\nfor e in exps:\n    if isinstance(e, dict):\n        print(f\\\"{e.get('exp_id','?')} | {e.get('status','?')} | {e.get('conclusion','')} | {e.get('server','')}\\\")\n    else:\n        print(f'Non-dict entry: {type(e)}: {str(e)[:100]}')\n\" 2>&1 | head -80",
    "description": "Parse registry experiments"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-15T01:25:46.222759+00:00_

Total: 68
Non-dict entry: &lt;class 'str'>: eval-acr-spatial-v4-obs-only-r2
Non-dict entry: &lt;class 'str'>: eval-acr-spatial-v4-default-r2
Non-dict entry: &lt;class 'str'>: eval-vla-mean-spatial-t10
Non-dict entry: &lt;class 'str'>: eval-acr-spatial-v4-obs-only
Non-dict entry: &lt;class 'str'>: eval-acr-spatial-v4-scalar
Non-dict entry: &lt;class 'str'>: eval-vla-mean-spatial
Non-dict entry: &lt;class 'str'>: eval-acr-spatial-v4-default
Non-dict entry: &lt;class 'str'>: crm-train-v3-norm-scalar-unc
Non-dict entry: &lt;class 'str'>: crm-train-v3-norm-obs-only
Non-dict entry: &lt;class 'str'>: eval-acr-spatial-v4-small
Non-dict entry: &lt;class 'str'>: eval-tiny-correction-spatial
Non-dict entry: &lt;class 'str'>: eval-argmin-only-spatial
Non-dict entry: &lt;class 'str'>: eval-acr-object-v3
Non-dict entry: &lt;class 'str'>: eval-acr-spatial-v3
Non-dict entry: &lt;class 'str'>: crm-train-v3-norm
Non-dict entry: &lt;class 'str'>: crm-train-v3-scalar-unc
Non-dict entry: &lt;class 'str'>: crm-train-v3-obs-only
Non-dict entry: &lt;class 'str'>: crm-train-v3-perdof
Non-dict entry: &lt;class 'str'>: eval-obs-only-spatial-v3
Non-dict entry: &lt;class 'str'>: eval-scalar-unc-spatial-v2
Non-dict entry: &lt;class 'str'>: eval-obs-only-spatial-v2
Non-dict entry: &lt;class 'str'>: eval-obs-only-spatial
Non-dict entry: &lt;class 'str'>: crm-train-v2-obs-only
Non-dict entry: &lt;class 'str'>: crm-train-v2-scalar-unc
Non-dict entry: &lt;class 'str'>: crm-train-v2-perdof
Non-dict entry: &lt;class 'str'>: eval-reconvla-spatial-v3
Non-dict entry: &lt;class 'str'>: precompute-v5-shard2
Non-dict entry: &lt;class 'str'>: precompute-v5-shard1
Non-dict entry: &lt;class 'str'>: precompute-v5-shard0
Non-dict entry: &lt;class 'str'>: crm-train-a4-scalar-unc
Non-dict entry: &lt;class 'str'>: crm-train-a3-obs-only
Non-dict entry: &lt;class 'str'>: crm-train-v1
Non-dict entry: &lt;class 'str'>: crm-train-k5
Non-dict entry: &lt;class 'str'>: eval-scalar-unc-spatial
Non-dict entry: &lt;class 'str'>: eval-acr-spatial-v2
Non-dict entry: &lt;class 'str'>: eval-k5-spatial
Non-dict entry: &lt;class 'str'>: eval
…[truncated 1630 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "Bash",
  "elapsed_ms": 404
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-15T01:25:46.323522+00:00_

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
  "session": "cron:hook:eval-acr-spatial-v3",
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

### Tool result

_source line 64 · 2026-05-15T01:25:46.376217+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md\", \"content\": \"# Memory — acr-vla-conformal-refinement\\n\\n## VLA-mean Baseline 定稿：多采样平均无收益（2026-05-15）\\n\\n### 发现\\neval-vla-mean-spatial: K=10 平均 ≈ 31%（9/10 tasks），与 K=1 baseline 30% 无显著差异（+1pp，噪声范围）。\\n\\n### 含义\\n- **多采样平均不是 ACR-VLA 改善的来源**。flow-matching VLA 的 K 个样本虽然不同，但 averaging 消除的噪声对 task success 无帮助\\n- ACR-VLA 的任何改善必须来自 intelligent selection（argmin）或 CRM correction\\n- argmin-only 早期信号 53.3%（3/10 tasks）>> VLA-mean 31% → **sample selection 本身就有强贡献**\\n- Narrative 可分层：(1) sample selection > averaging (2) CRM correction adds calibrated precision\\n\\n### 论文定位\\n这证实了 Section 1 (Intro) 的动机：naive aggregation 不够，需要 structured uncertainty-guided selection。\\n\\n## Correction Magnitude 是核心问题（2026-05-14 18:15，早期信号）\\n\\n### 发现\\neval-tiny-correction-spatial（max_correction_norm=0.05，约默认 1.42 的 1/28）在首个 task 上 4/5 成功，而 full ACR 同一 task 只有 1/10。这说明 CRM correction 的方向可能是对的，但幅度太大导致 compounding error。\\n\\n### 含义\\n- correction clipping / gating 是正确的补救方向\\n- Gated CRM 代码已就绪（`src/gated_crm.py` + `--mode acr_gated` + `--gate_threshold/mode/temperature`）\\n- 等完整 eval 结果确认后，下一步应该是 correction magnitude sweep（0.01, 0.05, 0.1, 0.2, 0.5）或 Gated CRM eval\\n- **不改变目标 venue（ICLR 2027）**，narrative 可从 \\\"per-DOF correction always helps\\\" 调整为 \\\"per-DOF correction with magnitude control\\\"\\n\\n### ⚠️ 注意\\n这是 1 个 task 的 5 个 rollout 的早期数据。需要完整 10 tasks 确认。\\n\\n## Correction Magnitude 文献支撑（2026-05-14 18:37）\\n\\n### 核心竞品/支撑论文\\n1. **PLD (ICLR 2026)**: scheduled ξ bound，LIBERO ξ=0.5 / SimplerEnv ξ=0.1——不同环境需不同 correction scale，完全验证我们的发现\\n2. **TRANSIC (CoRL 2024)**: 无 gate 时 fine-tuning 导致 model collapse——与我们 40%→2.5% 退化一致\\n3. **ResiP (CoRL-W 2024)**: scaling α≤1，关键不是精确值而是 order of magnitude\\n4. **DRC (2025)**: temporal decay of correction\\n5. **DAWN (2026)**: scale mismatch → residual 学不好\\n\\n### 独特贡献角度\\n**没有现有方法提供 per-DOF,
…[truncated 6130 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 52
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-15T01:25:55.079489+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'status': 'RUNNING'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'status': 'RUNNING'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-15T01:25:55.232307+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'status': 'PREPARING'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'status': 'PREPARING'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-15T01:25:55.433718+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-argmin-only-spatial\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:47:58.683Z\", \"updated_at\": \"2026-05-15T01:25:37.336Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts 10 --seed 42 --K 10\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"231421\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-only-spatial.log\", \"submitted_at\": \"2026-05-14T17:47:58.583Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_ids\": [\"cuda:1\"], \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"SmolVLA K=10 argmin selection (no CRM correction)\", \"seed\": 42, \"hypothesis\": \"Isolate argmin base action selection from CRM correction. If argmin-only ≈ VLA mean (40%), CRM delta is the sole culprit. If argmin-only << VLA mean, argmin selection itself is problematic.\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\"}, \"metrics\": {\"tasks_done\": \"5/10\", \"task6_status\": \"in progress\", \"partial_results\": {\"T1_between_plate_ramekin\": \"60% (6/10)\", \"T2_next_to_ramekin\": \"100% (10/10)\", \"T3_from_table_center\": \"0% (0/10)\", \"T4_on_cookie_box\": \"30% (3/10)\", \"T5_in_top_drawer\": \"10% (1/10)\"}, \"running_avg_5tasks\": \"40% (20/50)\", \"snapshot_time\": \"2026-05-15T00:16Z\"}}, \"eval-acr-spatial-v4-obs-only-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:16:06.636Z\", \"updated_at\": \"2026-05-14T22:40:00.000Z\", \"hypothesis\": \"D020: obs_only CRM v3-norm (val_loss 0.0165) with max_correction_norm=0.1. If obs_only >= v4-small (perdof) → Claim 1 needs restructuring. If obs_only < v4-small → conformal features have unique value under distribution shift.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/cond
…[truncated 4572 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 354
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-15T01:25:55.685975+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-acr-spatial-v4-scalar\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:15:49.209Z\", \"updated_at\": \"2026-05-14T22:15:51.527Z\", \"hypothesis\": \"D020: scalar_unc CRM (val_loss 0.0374) with max_correction_norm=0.1. Three-way ablation: perdof vs scalar_unc vs obs_only under identical correction magnitude.\"}, \"eval-object-v6-full\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:28:33.119Z\", \"updated_at\": \"2026-05-13T23:29:33.175Z\", \"spec\": {\"data_path\": \"/root/autodl-tmp/libero_data/ (object)\", \"data_count\": 100, \"model_name\": \"lerobot/smolvla_libero\", \"seed\": 42, \"hypothesis\": \"SmolVLA baseline success rate on libero_object with fixed evaluate.py (env.reset bug removed, 5-step zero-action stabilization)\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"libero_object 10 tasks x 10 rollouts\"}, \"conclusion\": \"killed\"}, \"eval-reconvla-spatial-v1\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:15:35.450Z\", \"updated_at\": \"2026-05-13T22:59:43.788Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"87787\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-reconvla-spatial-v1.log\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": \"10 tasks x 10 rollouts x 300 steps\", \"model_name\": \"lerobot/smolvla_libero (450M) + ReconVLA argmin selection K=10\", \"seed\": 42, \"hypothesis\": \"ReconVLA (scalar Euclidean nonconformity + argmin) as baseline for ACR-VLA comparison\", \"checkpoint_source\": \"lerobot/smolvla_libero\"}, \"reproduce\": {\"finished_at\": \"2026-05-13T22:59:43.231Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM
…[truncated 10284 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-spatial-v3",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 453
}
```

</details>

---

### Assistant

_source line 69 · 2026-05-15T01:26:58.075908+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- GPU 白名单：bjb1-18228:cuda:0/1/2/3 + bjb2-40593:cuda:0，禁止用其他 GPU
- 目标 venue 已切回 **CoRL 2026**（D021），abstract DDL ~May 26，时间极紧
- CRM v2 checkpoint（/root/autodl-tmp/checkpoints/crm_v2/）有 state dim mismatch bug（D016），禁止用于新实验；只用 v3-norm（/root/autodl-tmp/checkpoints/crm_v3_norm/）
- SmolVLA 推理必须 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl，否则 AutoDL 网络崩溃
- eval-vla-mean-spatial 已确认：K=10 平均 ≈ 31%，与 K=1 baseline 30% 无显著差异——多采样平均无收益已定论，不要再跑

### 2. 🖥️ 基础设施快照
- **bjb1-18228** (4× RTX 4090): 工作目录 `/root/acr-vla-conformal-refinement`，Python `/root/miniconda3/bin/python`，conda base
- **bjb2-40593** (1× RTX 4090 D): 同上路径布局
- 模型：`/root/autodl-tmp/models/smolvla_libero/`（SmolVLA 450M, 7D action）
- CRM checkpoints：`/root/autodl-tmp/checkpoints/crm_v3_norm/{perdof,scalar_unc,obs_only}/crm_best.pt`
- 数据：`/root/autodl-tmp/libero_data/`，CRM cache `/root/autodl-tmp/crm_cache_v5/`
- 活跃进程（bjb1）：
  - eval-argmin-only-spatial: PID 231421, tmux, cuda:1
  - eval-tiny-correction-spatial: PID 232815, tmux, cuda:2
  - eval-acr-spatial-v4-small: PID 253085, tmux, cuda:3
  - eval-acr-spatial-v4-obs-only-r2: PID 270097, tmux, cuda:0
- 活跃进程（bjb2）：
  - eval-vla-mean-spatial-t10: cuda:0（补跑 T10）
- Cron 监控：上述 4 个 bjb1 实验均有活跃 cron

### 3. 📊 当前状态
5 路 eval 全部在跑，这是 D018-D020 normalization + magnitude control 消融的核心对比批次：

| exp_id | GPU | 进度 | 早期信号 | 目的 |
|--------|-----|------|---------|------|
| eval-argmin-only-spatial | bjb1:1 | 5/10 tasks | 40% (20/50) | 隔离 argmin selection 贡献（无 CRM correction） |
| eval-tiny-correction-spatial | bjb1:2 | 3/10 tasks | 53.3% (16/30) | CRM v2 + 极小 correction (0.05) |
| eval-acr-spatial-v4-small | bjb1:3 | 1/10 tasks | 60% on T1 | CRM v3-norm perdof + correction 0.1 |
| eval-acr-spatial-v4-obs-only-r2 | bjb1:0 | 刚启动 | — | CRM v3-norm obs_only + correction 0.1 |
| eval-vla-mean-spatial-t10 | bjb2:0 | 补跑 T10 | — | VLA-mean 补最后 1 个 task |

**等待中**：5 个 cron 回调（上述实验完成时触发）。eval-acr-spatial-v4-scalar (PREPARING) 等 GPU 空出。

### 4. 📋 待办（条件触发式）
- **eval-argmin-only-spatial 完成** → 更新 registry metrics → 与 baseline 30% 对比 → 如果 argmin-only > 35% 则 argmin selection 本身有强贡献，narrative 分层："selection > averaging > CRM correction adds precision"
- **eval-tiny-correction-spatial 完成** → 与 argmin-only 对比 → 如果 tiny-correction > argmin-only → CRM correction 方向对但需 magnitude control → 支持 "Conformally-Calibrated Correction Magnitude" framing
- **eval-acr-spatial-v4-small 完成** → 这是 v3-norm + 0.1 correction 的核心实验 → 与 tiny-correction (v2+0.05) 对比验证 normalization 是否真正改善 correction 质量
- **eval-acr-spatial-v4-obs-only-r2 完成** → 与 v4-small (perdof) 对比 → obs_only >= perdof 则 Claim 1 (per-DOF conformal features are essential) 需要重构
- **任一 bjb1 GPU 空出** → 立即提交 eval-acr-spatial-v4-scalar（D020 三路消融最后一格：scalar_unc CRM + correction 0.1）
- **全部 5 路 eval 完成** → 汇总完整对比表 → 向 Director 汇报 → 决定 framing 方向 + 是否铺 object benchmark

### 5. 🎯 战略上下文
**核心问题链**：CRM correction 在闭环 eval 中导致退化（40%→3%）→ D018 确认根因是 input 未归一化 → D019 发现 normalization alone 不够 → 当前 batch 测试 normalization + magnitude control 能否救回来。

**关键数据点**：
- Baseline (K=1): 30%
- VLA-mean (K=10 avg): 31%（无收益，已定论）
- Argmin-only (K=10 select): 40% 早期（5/10 tasks）→ **selection 本身就有强贡献**
- Tiny-correction (0.05): 53.3% 早期（3/10 tasks）→ **方向对，幅度是问题**
- v4-small (v3-norm perdof, 0.1): 60% on T1 only（太早）

**决策链**：D015(SFT gate 30%) → D016(state dim bug) → D017(CRM全面拖累) → D018(normalization缺失) → D019(normalization alone不够) → D020(三路消融) → D021(回瞄CoRL 2026)

**易错点**：
1. eval-tiny-correction-spatial 用的是 CRM **v2**（buggy cache 训练），eval-acr-spatial-v4-small 用的是 CRM **v3-norm**（clean）。两者的对比**不是**纯 correction magnitude 消融——如果 v4-small < tiny-correction，可能是 v3-norm CRM 本身质量不如 v2
2. CoRL 2026 abstract DDL ~May 26，只剩 ~11 天，完整 eval 每个约 10h，来不及做太多轮
3. obs_only CRM val_loss (0.0165) 远优于 perdof (0.0358)，但闭环 eval 才是真相——不要被 val_loss 误导
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval-acr-spatial-v3"
}
```

</details>

---
