# cron hook action trajectory control

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/cron_hook_action_trajectory_control.jsonl`
- **Structured JSON:** [`6025bd1df271344d46ae.json`](../../sessions/60/6025bd1df271344d46ae.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

28 recorded events

### User

_source line 1 · 2026-05-18T11:42:57.924051+00:00_

[CRON] 实验进程已正常退出，状态已转为 ANALYZING，需要你分析结果并推进到 DONE。
详情: Process exited cleanly, W&B data available

- exp_id: action_trajectory_control
- project: vla-ssd
- server: westd-19183
- log_path: /root/autodl-tmp/vla-ssd/results/action_trajectory_control.log

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:action_trajectory_control",
  "source": "cron:hook"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-18T11:43:14.057037+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__read_experiment_plan_with_status",
  "max_results": "8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:action_trajectory_control",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__read_experiment_plan_with_status",
    "max_results": "8"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-18T11:43:14.107599+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:action_trajectory_control",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-18T11:43:19.137727+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "vla-ssd",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:action_trajectory_control",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "vla-ssd",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T11:43:19.138176+00:00_

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
  "session": "cron:hook:action_trajectory_control",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-18T11:43:19.590809+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "vla-ssd",
  "file": "report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:action_trajectory_control",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "vla-ssd",
    "file": "report.md"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-18T11:43:19.893617+00:00_

Error: result (141,864 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-agent-9301ad3d/7c53841f-30a7-46d8-a58c-28513b6668bb/tool-results/mcp-agent-ml-research-read_registry-1779104599731.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-agent-9301ad3d/7c53841f-30a7-46d8-a58c-28513b6668bb/tool-results/mcp-agent-ml-research-read_registry-1779104599731.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:action_trajectory_control",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 755
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-18T11:43:19.893976+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 0, \"results\": []}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:action_trajectory_control",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 755
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-18T11:43:19.894276+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-18T11:42:56Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 81 个实验 — ANALYZING 1, DONE 75, PREPARING 5\\n**DONE 分布**: killed 10, negative 7, success 58\\n\\n### GPU 占用\\n- **分配**: 2 张 — westd-19183:cuda:0, westd-19183:cuda:1\\n- **空闲（分配了没跑）**: westd-19183:cuda:0\\n\\n### 💾 磁盘余量\\n- **westd-19183**:\\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\\n  - `/init`: 150M/150M 可用（已用 0%）\\n  - `/usr/bin/nvidia-smi`: 816G/879G 可用（已用 3%）\\n\\n### 🏃 RUNNING\\n_（无）_\\n\\n### 📌 最近完成 (top 5)\\n- `action_trajectory_analysis` [success] — 2026-05-18T11:02:27\\n- `behavioral_pilot_w4` [killed] — 2026-05-18T10:34:21 — EXIT_CODE=129 (non-zero)\\n- `threecond_multiseed_r2_v2` [success] — 2026-05-18T09:11:34\\n- `threecond_multiseed_r2` [killed] — 2026-05-18T08:50:31\\n- `random_subset_ablation` [success] — 2026-05-18T08:27:15\\n\\n### 🔴 最近失败原因 (top 3)\\n- `behavioral_pilot_w4`: EXIT_CODE=129 (non-zero)\\n- `threecond_multiseed_r2`: _(no failure_reason — pre-2026-04-24 entry)_\\n\\n&lt;!-- AUTO-FACTS-END -->\\n\\n---\\n\\n# Handover — 2026-05-18\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| action_trajectory_control | Ablating 8 non-instruction heads (control) produces significantly smaller action divergence (especially gripper dimension) than ablating 24 instruction-dominant heads, proving the action output effect is instruction-specific rather than generic perturbation. | — | — | — |\\n\\n## 待处理\\n- behavioral_pilot_v2: Ablating L1 instruction-dominant heads (24/32) during VLA inference on LIBERO-Goal fine-tuned OpenVLA reduces task success rate, providing behavioral evidence that attention head specialization has functional consequences for task execution.（
…[truncated 1955 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:action_trajectory_control",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 303
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-18T11:43:19.894496+00:00_

called mcp__agent-ml-research__read_roadmap

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_roadmap</summary>

```json
{
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:action_trajectory_control",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-18T11:43:19.944977+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/ROADMAP.md\", \"content\": \"# vla-ssd — Research Dashboard\\n\\n> 最后更新: 2026-05-18 05:35 UTC | 更新原因: Round 5 全部 critical/warning resolved + Plan C 完成，准备 Round 6\\n\\n## 核心方向\\nToken-level functional specialization in VLA: C2 (instruction routing reorganization) 为唯一核心 claim，C1 为方法论框架，C3 为 qualified observation。详见 paper_framing.md。\\n\\n## 当前进展\\n**Round 5 审稿响应全部完成 — 准备提交 Round 6 验证**\\n\\n- Round 5 评分 Borderline 6/10，2 critical + 6 warning + 4 info\\n- **所有 critical/warning 已 resolved**，仅剩 2 个 info 级 open (R4-I2 引用格式, R5-I1 单seed appendix)\\n- **D061 Plan C 已执行**：ablation 叙事从 \\\"capacity trade-off / 3.5× specificity\\\" 全面转向 \\\"dual routing-encoding function\\\"\\n  - Random-subset ablation: 10 seeds, z=-2.73, p=0.003, dominant-24 (+0.042) < random-24 (+0.077±0.013)\\n  - 全文 5 处重写，旧术语 grep 验证归零\\n- 补充实验全部完成：T1 random-subset ablation + T2 linear probe + T3 OOD diagnostics + T4 Bootstrap CI\\n- 4 个新 appendix section + 3 张新图（random-subset histogram, linear vs MLP probe, OOD 3-panel）\\n- 论文编译 PASS: 0 warnings, 0 undefined refs, 8pp main + appendix\\n- Abstract 228 words (≤250 ✓)\\n\\n## 近期任务\\n- [x] Round 5 审稿响应：2 critical + 6 warning 全部 resolved ✓\\n- [x] Plan C narrative rewrite + Reviewer PASS ✓\\n- [x] T1-T4 补充实验完成 + paper 整合 ✓\\n- [x] review_issues.yaml 更新 ✓\\n- [ ] 提交 Round 6 内部审稿（验证 Plan C + 所有修改的累积效果）\\n- [ ] R4-I2: alain2017 年份 + nostalgebraist2020 blog 格式（info, 低优先）\\n- [ ] R5-I1: Appendix A.6 三条件多 seed（info, 低优先）\\n\\n## GPU 预算\\nwestd-19183: cuda:0 + cuda:1（2× GPU）\\n已用 ~23.1 GPU·h / 总预算 26 GPU·h，剩余 ~2.9h\\n**策略**：保留给 Round 6 审稿后精准响应。\\n\\n## 投稿信息\\n- 目标: CoRL 2026\\n- Abstract DDL: 2026-05-26（8 天）\\n- Paper DDL: 2026-05-29（11 天）\\n- 当前状态: Round 5 所有 issues addressed，准备 Round 6 验证\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D063 | 2026-05-18 | W4 behavioral 方案：放弃闭环 rollout，改用 open-loop action  | behav
…[truncated 1142 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:action_trajectory_control",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-18T11:43:30.837090+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "vla-ssd",
  "filters": "{'exp_id': 'action_trajectory_control'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:action_trajectory_control",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "vla-ssd",
    "filters": "{'exp_id': 'action_trajectory_control'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T11:43:30.939091+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "vla-ssd",
  "filters": "{'exp_id': 'action_trajectory_analysis'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:action_trajectory_control",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "vla-ssd",
    "filters": "{'exp_id': 'action_trajectory_analysis'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-18T11:43:31.140842+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2792}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:action_trajectory_control",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 303
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-18T11:43:31.392109+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2435}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:action_trajectory_control",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 453
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-18T11:43:37.215111+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A 30 \"action_trajectory_control\" /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/registry.yaml | head -60",
  "description": "Search for action_trajectory_control in registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:action_trajectory_control",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A 30 \"action_trajectory_control\" /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/registry.yaml | head -60",
    "description": "Search for action_trajectory_control in registry"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-18T11:43:37.416672+00:00_

  action_trajectory_control:
    status: ANALYZING
    retry_count: 0
    created_at: '2026-05-18T11:34:36.585Z'
    updated_at: '2026-05-18T11:42:55.145Z'
    hypothesis: Ablating 8 non-instruction heads (control) produces significantly
      smaller action divergence (especially gripper dimension) than ablating 24 instruction-dominant
      heads, proving the action output effect is instruction-specific rather than
      generic perturbation.
    parent: action_trajectory_analysis
    spec:
      command: bash -c "source /root/miniconda3/bin/activate base && cd /root/vla-ssd
        && MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=0 python scripts/action_trajectory_control.py"
      server: westd-19183
      gpu:
      - cuda:0
      pid: '34588'
      log_path: /root/autodl-tmp/vla-ssd/results/action_trajectory_control.log
      submitted_at: '2026-05-18T11:36:51.464Z'
      submitted_via: submit_training_job
      backend: tmux
      account: root
      data_path: /root/autodl-tmp/vla-ssd/data/libero/libero_goal/
      data_count: 5 tasks x 10 demos x 50 timesteps = 2500 forward passes x 2 conditions
      model_name: OpenVLA-7b (openvla-7b base pretrained)
      seed: '42'
      checkpoint_source: /root/autodl-tmp/vla-ssd/checkpoints/openvla-7b
      eval_data: LIBERO-Goal demo observations (open-loop, no execution)
      checkpoint_path: N/A (inference only)
    reproduce:
      finished_at: '2026-05-18T11:42:54.772Z'
    extra:
      hook_events:
      - event: on_complete
        action: agent
        ts: '2026-05-18T11:42:57.559215+00:00'
  behavioral_pilot_v2:
    status: PREPARING
    retry_count: 0
    created_at: '2026-05-18T11:40:18.951Z'
    updated_at: '2026-05-18T11:40:25.510Z'
    hypothesis: Ablating L1 instruction-dominant heads (24/32) during VLA inference
      on LIBERO-Goal fine-tuned OpenVLA reduces task success rate, providing behavioral
      evidence that attention head specialization has functional consequences for
      task execution.
    parent:
…[truncated 20 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:action_trajectory_control",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-18T11:43:44.745109+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A 40 \"action_trajectory_analysis:\" /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/registry.yaml | head -50",
  "description": "Read parent experiment action_trajectory_analysis from registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:action_trajectory_control",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A 40 \"action_trajectory_analysis:\" /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/registry.yaml | head -50",
    "description": "Read parent experiment action_trajectory_analysis from registry"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-18T11:43:44.846136+00:00_

  action_trajectory_analysis:
    status: DONE
    retry_count: 0
    created_at: '2026-05-18T10:35:18.923Z'
    updated_at: '2026-05-18T11:02:27.281Z'
    hypothesis: L1 instruction-dominant head ablation significantly changes OpenVLA
      action predictions (measured by action token divergence and per-dimension MSE),
      demonstrating that instruction routing heads directly influence model output,
      not just intermediate representations.
    parent: ablation_50demos_main
    spec:
      command: bash -c "source /root/miniconda3/bin/activate base && cd /root/vla-ssd
        && MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=0 python scripts/action_trajectory_analysis.py"
      server: westd-19183
      data_path: /root/autodl-tmp/vla-ssd/data/libero/libero_goal/
      data_count: 5 tasks x 10 demos x 50 timesteps = 2500 forward passes x 2 conditions
      model_name: OpenVLA-7b (openvla-7b base pretrained)
      seed: '42'
      checkpoint_source: /root/autodl-tmp/vla-ssd/checkpoints/openvla-7b
      eval_data: LIBERO-Goal demo observations (open-loop, no execution)
      checkpoint_path: N/A (inference only)
      log_path: /root/autodl-tmp/vla-ssd/results/action_trajectory_analysis.log
    metrics:
      paired_action_mse:
        mean: 0.0416
        std: 0.0639
        t_stat: 32.56
        p_value: 3.99e-194
        cohens_d: 0.651
      token_divergence_rate: 0.723
      per_dim_action_shift_means:
      - 0.0019
      - 0.0053
      - 0.0076
      - 0.0206
      - 0.0307
      - 0.0339
      - 0.2907
      per_dim_names:
      - dx
      - dy

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:action_trajectory_control",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-18T11:43:47.970092+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A 70 \"action_trajectory_analysis:\" /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/registry.yaml | tail -40",
  "description": "Read rest of parent experiment metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:action_trajectory_control",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A 70 \"action_trajectory_analysis:\" /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/registry.yaml | tail -40",
    "description": "Read rest of parent experiment metrics"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-18T11:43:48.020782+00:00_

      - 0.0019
      - 0.0053
      - 0.0076
      - 0.0206
      - 0.0307
      - 0.0339
      - 0.2907
      per_dim_names:
      - dx
      - dy
      - dz
      - rx
      - ry
      - rz
      - gripper
      kl_divergence:
        mean: 5.079
        std: 4.961
      mse_vs_gt_baseline: 0.432
      mse_vs_gt_ablated: 0.436
      wilcoxon_p: 0
      n_tasks: 5
      n_samples: 2500
      all_tasks_significant: true
      per_task_cohens_d_range:
      - 0.433
      - 0.729
      result_path: /root/autodl-tmp/vla-ssd/results/action_trajectory_analysis.json
    conclusion: success
    completed_at: '2026-05-18T11:02:27.281Z'
  action_trajectory_control:
    status: ANALYZING
    retry_count: 0
    created_at: '2026-05-18T11:34:36.585Z'
    updated_at: '2026-05-18T11:42:55.145Z'
    hypothesis: Ablating 8 non-instruction heads (control) produces significantly
      smaller action divergence (especially gripper dimension) than ablating 24 instruction-dominant
      heads, proving the action output effect is instruction-specific rather than
      generic perturbation.
    parent: action_trajectory_analysis

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:action_trajectory_control",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-18T11:43:56.246896+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__get_worker_status,mcp__agent-ml-research__compute_coverage_matrix,mcp__agent-ml-research__get_project_resource_usage",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:action_trajectory_control",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__get_worker_status,mcp__agent-ml-research__compute_coverage_matrix,mcp__agent-ml-research__get_project_resource_usage",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-18T11:43:56.298426+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:action_trajectory_control",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-18T11:44:13.617948+00:00_

called mcp__agent-ml-research__spawn_worker

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker</summary>

```json
{
  "task_type": "analysis:action_trajectory_control",
  "project": "vla-ssd",
  "task_prompt": "## 任务：分析 action_trajectory_control 实验结果\n\n### 背景\n这是一个 **control 实验**，用来证明 instruction-dominant head ablation 对 action output 的影响是 instruction-specific 的，而非 generic perturbation。\n\n**Parent 实验 (action_trajectory_analysis)** 已完成 (success)：\n- 消融 24 个 instruction-dominant heads → paired action MSE mean=0.0416, t=32.56, p<1e-193, Cohen's d=0.651\n- Token divergence rate: 72.3%\n- Per-dim shift: dx=0.0019, dy=0.0053, dz=0.0076, rx=0.0206, ry=0.0307, rz=0.0339, **gripper=0.2907**\n- KL divergence: mean=5.079\n\n**本实验 (action_trajectory_control)**：\n- 消融 8 个 non-instruction heads (control group)\n- Hypothesis: control ablation 产生的 action divergence 显著小于 instruction-dominant head ablation，尤其是 gripper 维度\n\n### 你要做的\n\n1. SSH 到 westd-19183，读取结果文件：\n   - `/root/autodl-tmp/vla-ssd/results/action_trajectory_control.log` (完整日志)\n   - 检查 `/root/autodl-tmp/vla-ssd/results/` 目录下是否有 `action_trajectory_control.json` 结果文件，如果有也读取\n\n2. 提取关键指标（与 parent 对比）：\n   - paired_action_mse (mean, std, t_stat, p_value, cohens_d)\n   - token_divergence_rate\n   - per_dim_action_shift (7 个维度，特别关注 gripper)\n   - kl_divergence (mean, std)\n   - 任何 control vs dominant 的统计对比结果\n\n3. 判断 conclusion：\n   - 如果 control 的 action divergence 显著小于 parent（尤其 gripper），hypothesis 成立 → **success**\n   - 如果 control 的 divergence 与 parent 差不多甚至更大 → **negative**（说明效应不是 instruction-specific）\n\n4. 将完整分析结果写入 `save_project_file(file=\"memory.md\")` 的相关段落（追加，不覆盖已有内容——先 read_project_file 读当前内容再追加）\n\n5. 用 `update_registry` 更新实验：\n   - field=\"metrics\", value={提取的指标 dict}\n   - field=\"conclusion\", value=\"success\" 或 \"negative\"\n   - field=\"status\", value=\"DONE\"\n\n### 服务器信息\n- server: westd-19183\n- Python env: `source /root/miniconda3/bin/activate base`\n- 项目路径: /root/vla-ssd\n",
  "tool_groups": "['ssh', 'registry', 'knowledge']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:action_trajectory_control",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "tool_args": {
    "task_type": "analysis:action_trajectory_control",
    "project": "vla-ssd",
    "task_prompt": "## 任务：分析 action_trajectory_control 实验结果\n\n### 背景\n这是一个 **control 实验**，用来证明 instruction-dominant head ablation 对 action output 的影响是 instruction-specific 的，而非 generic perturbation。\n\n**Parent 实验 (action_trajectory_analysis)** 已完成 (success)：\n- 消融 24 个 instruction-dominant heads → paired action MSE mean=0.0416, t=32.56, p<1e-193, Cohen's d=0.651\n- Token divergence rate: 72.3%\n- Per-dim shift: dx=0.0019, dy=0.0053, dz=0.0076, rx=0.0206, ry=0.0307, rz=0.0339, **gripper=0.2907**\n- KL divergence: mean=5.079\n\n**本实验 (action_trajectory_control)**：\n- 消融 8 个 non-instruction heads (control group)\n- Hypothesis: control ablation 产生的 action divergence 显著小于 instruction-dominant head ablation，尤其是 gripper 维度\n\n### 你要做的\n\n1. SSH 到 westd-19183，读取结果文件：\n   - `/root/autodl-tmp/vla-ssd/results/action_trajectory_control.log` (完整日志)\n   - 检查 `/root/autodl-tmp/vla-ssd/results/` 目录下是否有 `action_trajectory_control.json` 结果文件，如果有也读取\n\n2. 提取关键指标（与 parent 对比）：\n   - paired_action_mse (mean, std, t_stat, p_value, cohens_d)\n   - token_divergence_rate\n   - per_dim_action_shift (7 个维度，特别关注 gripper)\n   - kl_divergence (mean, std)\n   - 任何 control vs dominant 的统计对比结果\n\n3. 判断 conclusion：\n   - 如果 control 的 action divergence 显著小于 parent（尤其 gripper），hypothesis 成立 → **success**\n   - 如果 control 的 divergence 与 parent 差不多甚至更大 → **negative**（说明效应不是 instruction-specific）\n\n4. 将完整分析结果写入 `save_project_file(file=\"memory.md\")` 的相关段落（追加，不覆盖已有内容——先 read_project_file 读当前内容再追加）\n\n5. 用 `update_registry` 更新实验：\n   - field=\"metrics\", value={提取的指标 dict}\n   - field=\"conclusion\", value=\"success\" 或 \"negative\"\n   - field=\"status\", value=\"DONE\"\n\n### 服务器信息\n- server: westd-19183\n- Python env: `source /root/miniconda3/bin/activate base`\n- 项目路径: /root/vla-ssd\n",
    "tool_groups": "['ssh', 'registry', 'knowledge']"
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-18T11:44:13.618442+00:00_

called mcp__agent-ml-research__get_project_resource_usage

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_project_resource_usage</summary>

```json
{
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:action_trajectory_control",
  "tool": "mcp__agent-ml-research__get_project_resource_usage",
  "tool_args": {
    "project": "vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-18T11:44:16.432349+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_analysis_action_trajectory_control_20260518T114414\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/logs/workers/worker_analysis_action_trajectory_control_20260518T114414.log\", \"setup_data\": {}, \"message\": \"Worker worker_analysis_action_trajectory_control_20260518T114414 started. Use get_worker_status('worker_analysis_action_trajectory_control_20260518T114414') to check progress.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:action_trajectory_control",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "elapsed_ms": 2814
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-18T11:44:16.735163+00:00_

{"result":"{\"success\": true, \"data\": {\"allocated_gpus\": [{\"server\": \"westd-19183\", \"gpu_id\": \"cuda:0\"}, {\"server\": \"westd-19183\", \"gpu_id\": \"cuda:1\"}], \"actually_running_gpus\": [], \"allocated_but_idle\": [{\"server\": \"westd-19183\", \"gpu_id\": \"cuda:0\", \"idle_min\": null, \"util_pct\": null}, {\"server\": \"westd-19183\", \"gpu_id\": \"cuda:1\", \"idle_min\": null, \"util_pct\": null}], \"registered_but_hw_idle\": [], \"unregistered_but_hw_active\": [], \"running_experiments\": [], \"worker_pool\": {\"total\": 3, \"gpu_tasks\": 0, \"cpu_tasks\": 3, \"details\": [{\"worker_id\": \"worker_debug_checkpoint_identity_and_behavioral_restart_20260518T105748\", \"task\": \"debug:checkpoint_identity_and_behavioral_restart\"}, {\"worker_id\": \"worker_debug_kill_duplicate_and_behavioral_pilot_v2_20260518T114002\", \"task\": \"debug:kill_duplicate_and_behavioral_pilot_v2\"}, {\"worker_id\": \"worker_analysis_action_trajectory_control_20260518T114414\", \"task\": \"analysis:action_trajectory_control\"}]}, \"summary\": \"分配 2 张, 实际跑 0 张 ⚠️ | Worker 3 (GPU 0 / CPU 3)\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:action_trajectory_control",
  "tool": "mcp__agent-ml-research__get_project_resource_usage",
  "elapsed_ms": 3116
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-18T11:44:35.359419+00:00_

已派 Worker 分析 `action_trajectory_control` 实验结果。

当前资源状态：
- GPU: 2 张分配（westd-19183 cuda:0/1），均空闲 — 按 ROADMAP 策略保留给 Round 6 响应（剩余 ~2.9h 预算）
- Worker 池: 3 个 CPU 任务运行中

等待 Worker 完成分析后汇报 Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:action_trajectory_control"
}
```

</details>

---
