# cron hook eval obs only object norm02 seed51 20260521T115724 025146

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 62
- **Recorded user turns:** 3
- **Tool calls:** 29
- **Original source:** `logs/chats/archive/cron_hook_eval-obs-only-object-norm02-seed51_20260521T115724_025146.jsonl`
- **Structured JSON:** [`878b5437dfd8dd2522c9.json`](../../sessions/87/878b5437dfd8dd2522c9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

36 recorded events

### User

_source line 1 · 2026-05-20T19:32:22.078874+00:00_

[CRON] 实验进程异常退出（失败），需要你诊断原因。
详情: Process exited without valid W&B metrics

- exp_id: eval-obs-only-object-norm02-seed51
- project: acr-vla-conformal-refinement
- server: bjb1-32546

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "source": "cron:hook"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-20T19:32:39.286433+00:00_

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
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
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

_source line 3 · 2026-05-20T19:32:39.346477+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "ToolSearch",
  "elapsed_ms": 60
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-20T19:32:42.622620+00:00_

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
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
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

_source line 5 · 2026-05-20T19:32:42.924403+00:00_

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
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-20T19:32:43.711474+00:00_

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
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
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

_source line 7 · 2026-05-20T19:32:43.999510+00:00_

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
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T19:32:46.581336+00:00_

Error: result (740,073 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-a5c20e02/fef65db8-c832-4afa-a70d-44ad365f8968/tool-results/mcp-agent-ml-research-read_registry-1779305566343.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-a5c20e02/fef65db8-c832-4afa-a70d-44ad365f8968/tool-results/mcp-agent-ml-research-read_registry-1779305566343.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 3958
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-20T19:33:06.566992+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 6, \"results\": [{\"exp_id\": \"eval-adaptive-unc-head-object-seed42\", \"success\": true, \"actions\": [\"Skipped — pending escalation retry\"]}, {\"exp_id\": \"eval-adaptive-unc-head-object-seed43\", \"success\": true, \"actions\": [\"Skipped — pending escalation retry\"]}, {\"exp_id\": \"eval-obs-only-object-norm003-seed43\", \"success\": true, \"actions\": [\"Skipped — pending escalation retry\"]}, {\"exp_id\": \"eval-obs-only-object-norm02-seed43-r3\", \"success\": true, \"actions\": [\"Job still running (pid=758482)\"]}, {\"exp_id\": \"eval-random-selection-object-seed48\", \"success\": true, \"actions\": [\"Job still running (pid=759093)\"]}, {\"exp_id\": \"eval-obs-only-object-norm01-seed48\", \"success\": true, \"actions\": [\"Job still running (pid=507385)\"]}]}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 23642
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T19:33:06.618259+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-20T19:32:55Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 483 个实验 — ANALYZING 1, DEPLOYED 4, DONE 434, PREPARING 33, RUNNING 11\\n**DONE 分布**: failed 47, killed 85, negative 34, success 268\\n\\n### GPU 占用\\n- **实际运行**: 11 张 — bjb2-28827:cuda:4(eval-obs-only-object-norm003-seed43), bjb1-18228:cuda:1(eval-obs-only-object-norm01-seed48), bjb2-28827:cuda:2(eval-obs-only-object-norm02-seed43-r3), bjb2-28827:cuda:0(D088-eval-adaptive-unc-head-object-seed42), bjb2-28827:cuda:1(D088-eval-adaptive-unc-head-object-seed43), bjb2-28827:cuda:4(D088-eval-adaptive-unc-head-object-seed44), bjb2-28827:cuda:0(eval-adaptive-unc-head-object-seed42), bjb2-28827:cuda:1(eval-adaptive-unc-head-object-seed43), bjb1-32546:cuda:2(eval-k5-obs-only-object-seed44), bjb1-32546:cuda:5(eval-k20-obs-only-object-seed44), bjb2-40593:cuda:0(eval-random-selection-object-seed48)\\n\\n### 💾 磁盘余量\\n- **bjb2-40593**:\\n  - `/init`: 150M/150M 可用（已用 0%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 46G/437G 可用（已用 89%）\\n- **bjb1-18228**:\\n  - `/autodl-pub`: 708G/7.0T 可用（已用 91%） ⚠️\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 400G/438G 可用（已用 4%）\\n- **bjb1-32546**:\\n  - `/autodl-pub`: 888G/7.0T 可用（已用 88%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 400G/438G 可用（已用 4%）\\n- **bjb2-28827**:\\n  - `/autodl-pub`: 4.5T/14T 可用（已用 69%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 399G/439G 可用（已用 5%）\\n\\n### 🏃 RUNNING\\n| exp_id | server | gpu | pid | log |\\n|--------|--------|-----|-----|-----|\\n| `eval-obs-only-object-norm003-seed43` | bjb2-28827 | cuda:4 | ? | `logs/eval-obs-only-object-norm003-seed43.log` |\\n| `eval-obs
…[truncated 9146 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 22906
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-20T19:33:06.619126+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-20 17:34 UTC | 更新原因: 补录 Reviewer #12 指出的遗漏结果 (K-sweep, Random Selection, Spatial CRM r2) + OpenVLA precompute ETA\\n\\n> 详见 paper_framing.md（D077: Adaptive K 核心, D088: Learned Uncertainty Head, D089: Round 2 Holistic Pass）\\n\\n## 核心方向\\n**Adaptive inference-time compute for frozen VLAs** — Learned Uncertainty Head (15.6K params) 预测每步是否需要 CRM 矫正。K=2 L2 作为 fallback 信号。CRM correction>selection 分析作为支撑。\\n\\n## 投稿目标\\n**CoRL 2026** DDL **2026-05-29**。剩余 **9 天**。\\n\\n## Round 2 审稿：weak reject (3/3 unanimous)\\n已解决 Round 1 的 4/7 criticals。持续 + 新增 = **7 criticals + 8 warnings**。\\n三个 SYSTEMIC_ISSUE 见 D089。\\n\\n## D088 方法升级（等待结果，~1.5h）\\n- **B: Learned Uncertainty Head** — 3-layer MLP, Val AUC=0.8131, F1=0.7674, τ=0.42\\n- 3 seeds 评估 RUNNING on bjb2-28827 (seed42/43/44)\\n- GO: SR ≥ ~15% → 核心贡献升级为 learned adaptive compute\\n- NO-GO → fallback A (K=2 Conformal Score + selective CRM)，Adaptive K 数据已充分\\n- ⚠️ Reviewer #12 指出: head 用 K=10 variance 训练但 K=1 推理，跨 regime 泛化有风险\\n\\n## OpenVLA 实验线（最高 impact，解决 3 个 review criticals）\\n- plan_801 ✅ OpenVLA v2 baseline: SR=69%\\n- Precompute: **87.8%**, ETA ~31min → 完成后立即启动 plan_802 CRM training\\n- plan_802 🔜 OpenVLA + CRM training + eval\\n\\n## 核心实验结果\\n| Evidence | 结果 | 状态 |\\n|----------|------|------|\\n| Object CRM K=10 (norm02) | 16.8%±1.8% (n=6) vs VLA 10.9%, p=9.5e-5*** | LOCKED |\\n| K=10 decomposition | correction +5.3pp, selection ≈0 | LOCKED |\\n| **Random Selection (Object)** | **seed45=10%, seed47=7% → ≈VLA-only** | ✅ NEW |\\n| **Random Selection (Spatial)** | **seed42=34%, seed43=26%, seed44=28% → ≈VLA-only** | ✅ NEW |\\n| **K=5 obs_only** | **seed43=17%** | ✅ NEW |\\n| **K=20 obs_only** | **seed42=20%, seed43=18% → diminishing returns from K=10** | ✅ NEW |\\n| Adaptive K P50 (Obj
…[truncated 2999 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 22619
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-20T19:33:11.889817+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'exp_id': 'eval-obs-only-object-norm02-seed51'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'exp_id': 'eval-obs-only-object-norm02-seed51'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T19:33:12.544558+00:00_

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
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/skills/on-experiment-failed.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T19:33:13.148833+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.2503}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1259
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-20T19:33:13.149260+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/sessions/agent_a5c20e02.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "Read",
  "elapsed_ms": 604
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-20T19:33:17.742430+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A 30 \"eval-obs-only-object-norm02-seed51\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml | head -50",
  "description": "Search for experiment in registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A 30 \"eval-obs-only-object-norm02-seed51\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml | head -50",
    "description": "Search for experiment in registry.yaml"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-20T19:33:18.194228+00:00_

  eval-obs-only-object-norm02-seed51:
    status: DONE
    retry_count: 0
    created_at: '2026-05-20T17:31:57.442Z'
    updated_at: '2026-05-20T19:32:30.677Z'
    hypothesis: CRM obs_only (ε=0.2) K=10 on LIBERO-Object seed51. Expanding Object
      CRM seed coverage.
    spec:
      command: python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed
        51 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt
        --max_correction_norm 0.2 --output_file logs/eval_obs_only_object_norm02_seed51.json
      server: bjb1-32546
      gpu:
      - cuda:4
      data_path: LIBERO-Object
      data_count: 100
      model_name: CRM_obs_only
      seed: 51
      checkpoint_source: crm_v3_norm/obs_only/crm_best.pt
      backend: tmux
      account: root
      log_path: logs/eval-obs-only-object-norm02-seed51.log
    pid: 542894
    reproduce:
      finished_at: '2026-05-20T19:32:05.562Z'
    failure_reason: process dead 5× with no sentinel/W&B — auto-resolved as failed
    conclusion: failed
    completed_at: '2026-05-20T19:31:59.898Z'
    extra:
      hook_events:
      - event: on_failed
        action: agent
        ts: '2026-05-20T19:33:00.043805+00:00'
  eval-random-selection-object-seed48:
    status: RUNNING
    retry_count: 0
    created_at: '2026-05-20T18:36:46.646Z'
    updated_at: '2026-05-20T18:37:19.746Z'
    hypothesis: Random selection baseline (K=10 uniform random) on LIBERO-Object seed48.
      Expanding random selection seed coverage for seed balance (plan_600, target
      n≥5).
    spec:
      command: python -u src/evaluate.py --mode random_selection --benchmark object
        --seed 48 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt
        --max_correction_norm 0.2
      server: bjb2-40593
      gpu:
      - cuda:0
      data_path: LIBERO-Object
      data_count: 100

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "Bash",
  "elapsed_ms": 451
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-20T19:33:18.295079+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/on-experiment-failed.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/on-experiment-failed.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-20T19:33:18.345633+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-20T19:33:32.439469+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__load_project_config",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__load_project_config",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-20T19:33:32.439902+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-20T19:33:59.614131+00:00_

called mcp__agent-ml-research__spawn_worker

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker</summary>

```json
{
  "task_type": "diagnose:eval-obs-only-object-norm02-seed51",
  "project": "acr-vla-conformal-refinement",
  "task_prompt": "## 任务：诊断实验失败原因\n\n实验 `eval-obs-only-object-norm02-seed51` 在 bjb1-32546 上失败，需要查日志找出根因。\n\n### 实验信息\n- **exp_id**: eval-obs-only-object-norm02-seed51\n- **服务器**: bjb1-32546\n- **GPU**: cuda:4\n- **PID**: 542894 (已退出)\n- **命令**: `python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 51 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_object_norm02_seed51.json`\n- **失败原因**: process dead 5× with no sentinel/W&B — auto-resolved as failed\n- **日志文件**: `logs/eval-obs-only-object-norm02-seed51.log`\n\n### 诊断步骤\n\n1. **SSH 到 bjb1-32546，读日志文件**：\n   - `cat logs/eval-obs-only-object-norm02-seed51.log` 查看完整日志（尾部重点看）\n   - 如果日志为空或不存在，检查 tmux session：`tmux ls` 和 `tmux capture-pane -t &lt;session> -p`\n   \n2. **检查输出文件**：\n   - `ls -la logs/eval_obs_only_object_norm02_seed51.json` — 看是否有输出文件（可能实际完成了但 W&B 没上报）\n   - 如果 json 存在，`cat logs/eval_obs_only_object_norm02_seed51.json` 读取结果\n\n3. **检查系统级原因**：\n   - `dmesg | grep -i \"oom\\|killed\\|error\" | tail -20` — OOM killer?\n   - `nvidia-smi` — GPU 状态是否正常\n   - `df -h /root` — 磁盘空间\n\n4. **同时检查 eval-perdof-object-norm02-seed50 的日志**（同时期同服务器也失败了）：\n   - `cat logs/eval-perdof-object-norm02-seed50.log | tail -50`\n\n### 产出\n- 用 `save_project_file` 写一段简短的诊断报告到 `memory.md`（append 模式），包含：失败根因、是否可重试、建议\n- 如果发现输出 json 文件存在且有有效结果，将结果一并报告（SR 值等）",
  "tool_groups": "['ssh', 'knowledge']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "tool_args": {
    "task_type": "diagnose:eval-obs-only-object-norm02-seed51",
    "project": "acr-vla-conformal-refinement",
    "task_prompt": "## 任务：诊断实验失败原因\n\n实验 `eval-obs-only-object-norm02-seed51` 在 bjb1-32546 上失败，需要查日志找出根因。\n\n### 实验信息\n- **exp_id**: eval-obs-only-object-norm02-seed51\n- **服务器**: bjb1-32546\n- **GPU**: cuda:4\n- **PID**: 542894 (已退出)\n- **命令**: `python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 51 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_object_norm02_seed51.json`\n- **失败原因**: process dead 5× with no sentinel/W&B — auto-resolved as failed\n- **日志文件**: `logs/eval-obs-only-object-norm02-seed51.log`\n\n### 诊断步骤\n\n1. **SSH 到 bjb1-32546，读日志文件**：\n   - `cat logs/eval-obs-only-object-norm02-seed51.log` 查看完整日志（尾部重点看）\n   - 如果日志为空或不存在，检查 tmux session：`tmux ls` 和 `tmux capture-pane -t &lt;session> -p`\n   \n2. **检查输出文件**：\n   - `ls -la logs/eval_obs_only_object_norm02_seed51.json` — 看是否有输出文件（可能实际完成了但 W&B 没上报）\n   - 如果 json 存在，`cat logs/eval_obs_only_object_norm02_seed51.json` 读取结果\n\n3. **检查系统级原因**：\n   - `dmesg | grep -i \"oom\\|killed\\|error\" | tail -20` — OOM killer?\n   - `nvidia-smi` — GPU 状态是否正常\n   - `df -h /root` — 磁盘空间\n\n4. **同时检查 eval-perdof-object-norm02-seed50 的日志**（同时期同服务器也失败了）：\n   - `cat logs/eval-perdof-object-norm02-seed50.log | tail -50`\n\n### 产出\n- 用 `save_project_file` 写一段简短的诊断报告到 `memory.md`（append 模式），包含：失败根因、是否可重试、建议\n- 如果发现输出 json 文件存在且有有效结果，将结果一并报告（SR 值等）",
    "tool_groups": "['ssh', 'knowledge']"
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T19:33:59.664836+00:00_

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
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/skills/resource-saturation.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-20T19:34:02.835559+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_diagnose_eval-obs-only-object-norm02-seed51_20260520T193400\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_diagnose_eval-obs-only-object-norm02-seed51_20260520T193400.log\", \"setup_data\": {}, \"message\": \"Worker worker_diagnose_eval-obs-only-object-norm02-seed51_20260520T193400 started. Use get_worker_status('worker_diagnose_eval-obs-only-object-norm02-seed51_20260520T193400') to check progress.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "elapsed_ms": 3221
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-20T19:34:02.835985+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/sessions/agent_a5c20e02.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "Read",
  "elapsed_ms": 3171
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-20T19:34:05.847545+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/resource-saturation.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/resource-saturation.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-20T19:34:05.898494+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-20T19:34:08.613845+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/resource-saturation*",
  "path": "/home/ubuntu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/resource-saturation*",
    "path": "/home/ubuntu"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-20T19:34:12.177674+00:00_

/home/ubuntu/agent-ml-research/skills/global/resource-saturation.skill.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "Glob",
  "elapsed_ms": 3563
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-20T19:34:14.586536+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/resource-saturation.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/resource-saturation.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-20T19:34:14.637444+00:00_

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
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-20T19:34:52.327795+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__get_project_resource_usage,mcp__agent-ml-research__list_workers",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__get_project_resource_usage,mcp__agent-ml-research__list_workers",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-20T19:34:52.378481+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-20T19:34:55.602564+00:00_

called mcp__agent-ml-research__get_project_resource_usage

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_project_resource_usage</summary>

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
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "mcp__agent-ml-research__get_project_resource_usage",
  "tool_args": {
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-20T19:34:55.753285+00:00_

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
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "mcp__agent-ml-research__list_workers",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "status": "running"
  }
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-20T19:52:24.797472+00:00_

Worker 已派出诊断。现在检查资源状态，然后向 Director 汇报。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval-obs-only-object-norm02-seed51"
}
```

</details>

---

## Round 2

24 recorded events

### User

_source line 37 · 2026-05-20T19:52:24.823429+00:00_

[CRON] 实验进程异常退出（失败），需要你诊断原因。
详情: Process exited without valid W&B metrics

- exp_id: eval-obs-only-object-norm02-seed51
- project: acr-vla-conformal-refinement
- server: bjb1-32546

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "source": "cron:hook"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-20T19:52:37.563217+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__send_progress,mcp__agent-ml-research__get_worker_status",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__send_progress,mcp__agent-ml-research__get_worker_status",
    "max_results": "10"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-20T19:52:37.563733+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-20T19:52:40.978000+00:00_

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
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
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

_source line 41 · 2026-05-20T19:52:40.978449+00:00_

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
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-20T19:52:41.430928+00:00_

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
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
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

_source line 43 · 2026-05-20T19:52:41.732029+00:00_

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
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-20T19:52:42.847406+00:00_

Error: result (744,192 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-a5c20e02/3a8f3635-0880-4dc9-8a47-f355345dce5c/tool-results/mcp-agent-ml-research-read_registry-1779306762777.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-a5c20e02/3a8f3635-0880-4dc9-8a47-f355345dce5c/tool-results/mcp-agent-ml-research-read_registry-1779306762777.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1869
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-20T19:53:13.490573+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 8, \"results\": [{\"exp_id\": \"eval-random-selection-object-seed48\", \"success\": true, \"actions\": [\"Job still running (pid=759093)\"]}, {\"exp_id\": \"eval-obs-only-object-norm02-seed53\", \"success\": true, \"actions\": [\"Job still running (pid=797335)\"]}, {\"exp_id\": \"eval-obs-only-object-norm003-seed45\", \"success\": true, \"actions\": [\"Job still running (pid=798783)\"]}, {\"exp_id\": \"eval-obs-only-object-norm005-seed47\", \"success\": true, \"actions\": [\"Job still running (pid=800192)\"]}, {\"exp_id\": \"eval-obs-only-object-norm02-seed54\", \"success\": true, \"actions\": [\"Job still running (pid=803103)\"]}, {\"exp_id\": \"eval-obs-only-object-norm005-seed45\", \"success\": true, \"actions\": [\"Job still running (pid=524561)\"]}, {\"exp_id\": \"eval-obs-only-object-norm01-seed50\", \"success\": true, \"actions\": [\"Job still running (pid=526048)\"]}, {\"exp_id\": \"eval-obs-only-object-norm003-seed46\", \"success\": true, \"actions\": [\"Job still running (pid=527531)\"]}]}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 32512
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-20T19:53:13.491582+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-20T19:51:35Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 486 个实验 — ANALYZING 1, DEPLOYED 6, DONE 435, PREPARING 33, RUNNING 11\\n**DONE 分布**: failed 46, killed 84, negative 37, success 268\\n\\n### GPU 占用\\n- **实际运行**: 8 张 — bjb2-28827:cuda:3(eval-obs-only-object-norm003-seed45), bjb2-28827:cuda:0(D088-eval-adaptive-unc-head-object-seed42), bjb2-28827:cuda:1(D088-eval-adaptive-unc-head-object-seed43), bjb2-28827:cuda:4(D088-eval-adaptive-unc-head-object-seed44), bjb1-32546:cuda:2(eval-k5-obs-only-object-seed44), bjb1-32546:cuda:5(eval-k20-obs-only-object-seed44), bjb2-40593:cuda:0(eval-random-selection-object-seed48), bjb1-18228:cuda:2(eval-obs-only-object-norm01-seed50)\\n\\n### 💾 磁盘余量\\n- **bjb2-40593**:\\n  - `/init`: 150M/150M 可用（已用 0%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 46G/437G 可用（已用 89%）\\n- **bjb1-18228**:\\n  - `/autodl-pub`: 708G/7.0T 可用（已用 91%） ⚠️\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 400G/438G 可用（已用 4%）\\n- **bjb1-32546**:\\n  - `/autodl-pub`: 888G/7.0T 可用（已用 88%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 400G/438G 可用（已用 4%）\\n- **bjb2-28827**:\\n  - `/autodl-pub`: 4.5T/14T 可用（已用 69%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 399G/439G 可用（已用 5%）\\n\\n### 🏃 RUNNING\\n| exp_id | server | gpu | pid | log |\\n|--------|--------|-----|-----|-----|\\n| `eval-obs-only-object-norm003-seed45` | bjb2-28827 | cuda:3 | ? | `—` |\\n| `eval-obs-only-object-norm005-seed47` | bjb2-28827 | ? | ? | `—` |\\n| `D088-eval-adaptive-unc-head-object-seed42` | bjb2-28827 | cuda:0 | ? | `logs/eval-adaptive-unc-head-object-seed42.log` |\\n| `D088-eval-adaptive-unc-head
…[truncated 8733 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 32060
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-20T19:53:13.542460+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-20 17:34 UTC | 更新原因: 补录 Reviewer #12 指出的遗漏结果 (K-sweep, Random Selection, Spatial CRM r2) + OpenVLA precompute ETA\\n\\n> 详见 paper_framing.md（D077: Adaptive K 核心, D088: Learned Uncertainty Head, D089: Round 2 Holistic Pass）\\n\\n## 核心方向\\n**Adaptive inference-time compute for frozen VLAs** — Learned Uncertainty Head (15.6K params) 预测每步是否需要 CRM 矫正。K=2 L2 作为 fallback 信号。CRM correction>selection 分析作为支撑。\\n\\n## 投稿目标\\n**CoRL 2026** DDL **2026-05-29**。剩余 **9 天**。\\n\\n## Round 2 审稿：weak reject (3/3 unanimous)\\n已解决 Round 1 的 4/7 criticals。持续 + 新增 = **7 criticals + 8 warnings**。\\n三个 SYSTEMIC_ISSUE 见 D089。\\n\\n## D088 方法升级（等待结果，~1.5h）\\n- **B: Learned Uncertainty Head** — 3-layer MLP, Val AUC=0.8131, F1=0.7674, τ=0.42\\n- 3 seeds 评估 RUNNING on bjb2-28827 (seed42/43/44)\\n- GO: SR ≥ ~15% → 核心贡献升级为 learned adaptive compute\\n- NO-GO → fallback A (K=2 Conformal Score + selective CRM)，Adaptive K 数据已充分\\n- ⚠️ Reviewer #12 指出: head 用 K=10 variance 训练但 K=1 推理，跨 regime 泛化有风险\\n\\n## OpenVLA 实验线（最高 impact，解决 3 个 review criticals）\\n- plan_801 ✅ OpenVLA v2 baseline: SR=69%\\n- Precompute: **87.8%**, ETA ~31min → 完成后立即启动 plan_802 CRM training\\n- plan_802 🔜 OpenVLA + CRM training + eval\\n\\n## 核心实验结果\\n| Evidence | 结果 | 状态 |\\n|----------|------|------|\\n| Object CRM K=10 (norm02) | 16.8%±1.8% (n=6) vs VLA 10.9%, p=9.5e-5*** | LOCKED |\\n| K=10 decomposition | correction +5.3pp, selection ≈0 | LOCKED |\\n| **Random Selection (Object)** | **seed45=10%, seed47=7% → ≈VLA-only** | ✅ NEW |\\n| **Random Selection (Spatial)** | **seed42=34%, seed43=26%, seed44=28% → ≈VLA-only** | ✅ NEW |\\n| **K=5 obs_only** | **seed43=17%** | ✅ NEW |\\n| **K=20 obs_only** | **seed42=20%, seed43=18% → diminishing returns from K=10** | ✅ NEW |\\n| Adaptive K P50 (Obj
…[truncated 2999 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 31810
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-20T19:53:18.367133+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'exp_id': 'eval-obs-only-object-norm02-seed51'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'exp_id': 'eval-obs-only-object-norm02-seed51'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-20T19:53:18.719448+00:00_

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
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/skills/on-experiment-failed.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-20T19:53:19.574907+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.2089}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1207
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-20T19:53:19.576482+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/sessions/agent_a5c20e02.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "Read",
  "elapsed_ms": 857
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-20T19:53:24.748982+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*on-experiment-failed*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*on-experiment-failed*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8"
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-20T19:53:25.752572+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "Glob",
  "elapsed_ms": 1003
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-20T19:53:25.903800+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -l \"norm02-seed51\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/*.yaml 2>/dev/null || echo \"NOT_FOUND\"",
  "description": "Search for norm02-seed51 in project yaml files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -l \"norm02-seed51\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/*.yaml 2>/dev/null || echo \"NOT_FOUND\"",
    "description": "Search for norm02-seed51 in project yaml files"
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-20T19:53:26.105037+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-20T19:53:29.768869+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A 30 \"eval-obs-only-object-norm02-seed51\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml | head -40",
  "description": "Get registry entry for the failed experiment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A 30 \"eval-obs-only-object-norm02-seed51\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml | head -40",
    "description": "Get registry entry for the failed experiment"
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-20T19:53:30.120989+00:00_

  eval-obs-only-object-norm02-seed51:
    status: DONE
    retry_count: 0
    created_at: '2026-05-20T17:31:57.442Z'
    updated_at: '2026-05-20T19:35:23.508Z'
    hypothesis: CRM obs_only (ε=0.2) K=10 on LIBERO-Object seed51. Expanding Object
      CRM seed coverage.
    spec:
      command: python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed
        51 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt
        --max_correction_norm 0.2 --output_file logs/eval_obs_only_object_norm02_seed51.json
      server: bjb1-32546
      gpu:
      - cuda:4
      data_path: LIBERO-Object
      data_count: 100
      model_name: CRM_obs_only
      seed: 51
      checkpoint_source: crm_v3_norm/obs_only/crm_best.pt
      backend: tmux
      account: root
      log_path: logs/eval-obs-only-object-norm02-seed51.log
    pid: 542894
    reproduce:
      finished_at: '2026-05-20T19:32:05.562Z'
    failure_reason: process dead 5× with no sentinel/W&B — auto-resolved as failed
    conclusion: success
    completed_at: '2026-05-20T19:31:59.898Z'
    extra:
      hook_events:
      - event: on_failed
        action: agent
        ts: '2026-05-20T19:33:00.043805+00:00'
    metrics:
      success_rate: 0.17
      n_rollouts: 100
    notes: 'Cron false positive: 实验正常完成但无 W&B/sentinel 被误判 failed。实际 SR=17% (17/100)，与
      obs_only norm02 均值 (16.8%±1.8%) 一致。新增第 7 个 seed 数据点。'
  eval-random-selection-object-seed48:
    status: RUNNING

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "Bash",
  "elapsed_ms": 352
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-20T19:53:30.271889+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/skills/**/on-experiment-failed*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/skills/**/on-experiment-failed*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-20T19:53:30.322535+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---

### Assistant

_source line 60 · 2026-05-20T19:53:53.947532+00:00_

实验 `eval-obs-only-object-norm02-seed51` 的 cron 回调已经是旧消息——registry 显示该实验已被处理：

- **status**: DONE
- **conclusion**: success
- **metrics**: SR=17% (17/100)
- **notes**: Cron false positive — 实验正常完成但无 W&B/sentinel 被误判 failed

这是反复出现的 cron 监控误报模式（evaluate.py 不写 W&B/sentinel，cron 检测到进程退出 + 无 metrics 就触发 on_failed）。实际结果 SR=17% 与 obs_only norm02 均值 (16.8%±1.8%) 一致。

无需额外诊断。当前 8 个 RUNNING 实验均正常（reconcile_crons 确认所有进程存活）。

关键状态总结：
- **D090**: D088 Learned Uncertainty Head 已 NO-GO
- **RUNNING**: 11 个实验（包括 D088 eval ×3、OpenVLA precompute、K-sweep、多 norm/seed eval）
- **GPU**: 17/17 填满
- **DDL**: CoRL 2026-05-29，剩余 9 天

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval-obs-only-object-norm02-seed51"
}
```

</details>

---

## Round 3

2 recorded events

### User

_source line 61 · 2026-05-21T11:56:28.221498+00:00_

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
  "session": "cron:hook:eval-obs-only-object-norm02-seed51",
  "source": "system:ralph_loop"
}
```

</details>

---

### Assistant

_source line 62 · 2026-05-21T11:57:24.022580+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- GPU 白名单严格按 `get_project_status` 的 `execution.gpu_ids`，当前 4 台服务器共 17 张卡全部已分配，不可用白名单外的卡
- bjb1-32546 上多个实验共享磁盘，清理前必须 `list_large_dirs` 确认，禁止删除其他 seed 的 checkpoint
- CRM checkpoint 统一路径 `/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt`，不同服务器路径一致，不要改
- evaluate.py 无 W&B/sentinel 输出，cron 会误判 failed——实际需要 Worker SSH 检查 JSON 输出文件确认真实结果。**大量 "failed" 实验实际是 cron false positive，必须 SSH 验证再定 conclusion**
- CoRL 2026 DDL 2026-05-29，剩 8 天，所有决策以此为锚

### 2. 🖥️ 基础设施快照
- **bjb2-28827** (6 GPU): 工作目录 `/root/autodl-tmp/acr-vla/`，conda base (`/root/miniconda3/bin/python`)
  - 运行中: D088 adaptive-unc-head ×3 seeds (cuda:0/1/4), norm003-seed45 (cuda:3), norm02-seed53/54
- **bjb1-32546** (6 GPU): 同上路径结构
  - 运行中: K=5 seed44 (cuda:2), K=20 seed44 (cuda:5), norm005-seed47, norm003-seed45/46
  - **失败实验 eval-obs-only-object-norm02-seed51 在此服务器**，实际已 conclusion=success (SR=17%, cron false positive)
- **bjb2-40593** (1 GPU): random-selection-object-seed48 (cuda:0, pid=759093)
- **bjb1-18228** (5 GPU): norm01-seed50 (cuda:2, pid=526048) 等多项
- 模型: `/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt`
- 数据: LIBERO suite (Object/Spatial/Goal/Long)，各 100 rollouts per seed
- 活跃 cron: 8 个，全部 reconcile 确认 still running

### 3. 📊 当前状态
- **刚收到 cron 回调**: eval-obs-only-object-norm02-seed51 报 failed，但 registry 已标记 conclusion=success (SR=17%)，是之前已处理的 cron false positive（notes 里有记录）。**无需再处理此实验。**
- **RUNNING 实验** (11 个): 8 个 cron 确认存活（见 reconcile 结果），另有 3 个在 bjb2-28827 未被 cron 覆盖（D088 seeds）
- **D088 Learned Uncertainty Head**: 3 seeds 评估中 (bjb2-28827)，这是 **P0 决策点**——GO/NO-GO 决定核心方法是否升级
  - D090 已记录 NO-GO 决策，但 ROADMAP 仍显示"等待结果"——可能是 ROADMAP 未更新，需确认
- **D090 决策已做出**: Learned Uncertainty Head NO-GO，fallback 到 K=2 Conformal Score + selective CRM (Adaptive K)
- **OpenVLA precompute**: 87.8% 完成时写入 ROADMAP，plan_802 CRM training 待 precompute 完成后启动
- 无活跃 Worker 回调在等待

### 4. 📋 待办（条件触发式）
- D088 eval seeds 完成回调到达 → 确认 D090 NO-GO 已生效，更新 ROADMAP 状态为 closed
- OpenVLA precompute 完成 → 立即 spawn Worker 启动 plan_802 CRM training + eval（**P0，解决 3 个 review criticals**）
- eval-random-selection-object-seed48 完成 → 收割结果，补充 Random Selection 数据点，整合入论文
- K=5/K=20 seed44 完成 → 更新 K-sweep 表格，确认 diminishing returns pattern
- norm 系列 seeds (003/005/01/02) 完成 → 补充 Figure 2 error bars，锁定 magnitude curve
- 所有 Object CRM 数据收齐 → 更新 Table 1 统计（当前 n=6→7，mean=16.8%±1.8%）
- GPU 空出 → 优先铺 Spatial Adaptive K P50 ×3 seeds (P1) 和 Leave-task-out 验证 (P1)

### 5. 🎯 战略上下文
- **核心结论**: CRM obs_only (ε=0.2, K=10) 在 Object 上 16.8%±1.8% vs VLA 10.9% (p=9.5e-5)；correction > selection 是核心 claim（Random Selection ≈ VLA-only 直接支撑）
- **D090 NO-GO**: Learned Uncertainty Head 被否决，方法回到 Adaptive K (K=2 L2 conformal score)。ROADMAP 里 D088 段可能显示旧状态，以 D090 决策为准
- **Round 2 审稿**: weak reject 3/3，7 criticals + 8 warnings。OpenVLA 实验线是解决 3 个 criticals 的关键（跨模型泛化）
- **易错点 1**: evaluate.py 不输出 W&B metrics，cron 会持续误报 failed。收到 failed 回调时必须 SSH 查 JSON 文件确认真实结果，大量 "failed" 实际是 success/negative
- **易错点 2**: D088/D090 状态可能混淆——D088 提出 Learned Uncertainty Head，D090 否决了它。不要再启动相关实验
- **易错点 3**: norm02-seed42 (SR=20%) 被 D084 排除出 Table 1（outlier），不要重新纳入
- **决策链**: D081(Long OOD cautious)→D082(batched inference)→D083(Spatial n=8 clean)→D084(seed42 outlier排除)→D085(跨benchmark P50)→D086→D087(OpenVLA恢复)→D088(Uncertainty Head提出)→D089(Round 2 holistic)→D090(Uncertainty Head NO-GO)
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval-obs-only-object-norm02-seed51"
}
```

</details>

---
