# cron hook eval mag perdof norm03 object 20260516T004353 014739

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 85
- **Recorded user turns:** 2
- **Tool calls:** 41
- **Original source:** `logs/chats/archive/cron_hook_eval-mag-perdof-norm03-object_20260516T004353_014739.jsonl`
- **Structured JSON:** [`b6a191345769c0cb730e.json`](../../sessions/b6/b6a191345769c0cb730e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

31 recorded events

### User

_source line 1 · 2026-05-15T20:42:28.537163+00:00_

[HANDOFF] 你是 Main Agent，这是 Loop #12。

## 上一轮交接 (task_context)

### 1. 🔴 硬约束 / 红线
- GPU 白名单：`bjb2-40593:cuda:0`, `bjb1-18228:cuda:0-3`, `bjb1-32546:cuda:0-5`, `bjb2-28827:cuda:0-5`（共 17 张）。白名单外的 GPU 即使 Director 指令也必须 push back
- exp_id 中 norm 值禁止歧义缩写：`norm03` 已导致事故（被误判为 0.03 而非 0.3）。必须用 `norm0p3`=0.3, `norm003`=0.03 格式
- submit_training_job 命令必须 `bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && ..."` 包裹，裸 `python` 会 EXIT_CODE=127
- kill 实验前必须 `ps aux | grep` 完整命令行逐参数比对（mode, norm, checkpoint, benchmark），名字相似 ≠ 同一实验
- perdof CRM claim 已死，不要在 spatial 上声称 perdof > argmin（D027 confirmed 0pp delta）

### 2. 🖥️ 基础设施快照
- **bjb1-18228** (4× 4090): 工作目录 `/root/acr-vla-conformal-refinement`, conda base, account=root
- **bjb1-32546** (6× 4090): 同上
- **bjb2-28827** (6× 4090): 同上
- **bjb2-40593** (1× 4090 D): 同上，但无 .git repo，CRM cache 在旧路径
- 模型：`/root/autodl-tmp/models/smolvla_libero/` (SmolVLA), CRM checkpoints 在 `/root/autodl-tmp/checkpoints/crm_v3_norm/{perdof,obs_only,scalar_unc}/crm_best.pt`
- HF cache: `/root/autodl-tmp/.hf_cache`
- 活跃 cron 监控（reconcile 确认）：eval-mag-obsonly-norm003-b2 (bjb2-40593), eval-obs-only-object-seed43 / eval-argmin-object-seed43 / eval-perdof-object-seed43 (bjb1-18228), eval-mag-obsonly-norm03-object / eval-mag-obsonly-norm005-object / eval-vla-mean-object-seed43 / eval-scalar-object-seed43 / eval-obs-only-object-norm02-seed43 / eval-mag-obsonly-norm003-object (bjb1-32546/bjb2-28827)
- 刚提交：eval-mag-perdof-norm0p3-object (bjb2-28827 cuda:2 pid=117269), eval-acr-object-obs-only-default (bjb1-32546 cuda:4 pid=134094)

### 3. 📊 当前状态
**刚完成：**
- `eval-acr-object-obs-only-norm02` → **22.0% SUCCESS (NEW PROJECT HIGH)**，obs_only norm=0.2 object。Registry DONE，结果卡片已发，Director 已汇报
- `eval-mag-perdof-norm03-object` → killed (SIGTERM EXIT_CODE=143)，已诊断，已重启为 `eval-mag-perdof-norm0p3-object`
- `eval-mag-perdof-norm02` → DONE(failed) EXIT_CODE=143，reconcile 自动处理

**RUNNING 实验（16 个，17/17 GPU 满载）：**

| 服务器 | GPU | exp_id | 摘要 |
|--------|-----|--------|------|
| bjb1-18228 | 0 | eval-mag-obsonly-norm03-r2 | obs_only norm=0.3 spatial (已完成?) |
| bjb1-18228 | 1 | eval-perdof-object-seed43 | perdof seed=43 object |
| bjb1-18228 | 2 | eval-obs-only-object-seed43 | obs_only seed=43 object ⭐关键 |
| bjb1-18228 | 3 | eval-argmin-object-seed43 | argmin seed=43 object |
| bjb1-32546 | 0 | eval-mag-obsonly-norm003-object | obs_only norm=0.03 object |
| bjb1-32546 | 1 | eval-vla-mean-object-seed43 | VLA-mean seed=43 object |
| bjb1-32546 | 2 | eval-scalar-object-seed43 | scalar seed=43 object |
| bjb1-32546 | 3 | eval-obs-only-object-norm02-seed43 | obs_only norm=0.2 seed=43 ⭐最关键 |
| bjb1-32546 | 4 | eval-acr-object-obs-only-default | obs_only 默认 norm object (刚提交) |
| bjb1-32546 | 5 | eval-mag-perdof-norm02-object | perdof norm=0.2 object |
| bjb2-28827 | 0 | eval-mag-perdof-norm003-object | perdof norm=0.03 object |
| bjb2-28827 | 1 | eval-mag-perdof-norm005-object | perdof norm=0.05 object |
| bjb2-28827 | 2 | eval-mag-perdof-norm0p3-object | perdof norm=0.3 object (刚重启) |
| bjb2-28827 | 3 | eval-acr-object-v4-default | perdof 默认 norm object |
| bjb2-28827 | 4 | eval-mag-obsonly-norm005-object | obs_only norm=0.05 object |
| bjb2-28827 | 5 | eval-mag-obsonly-norm03-object | obs_only norm=0.3 object |
| bjb2-40593 | 0 | eval-mag-obsonly-norm003-b2 | obs_only norm=0.03 spatial |

**无等待中的 Worker 回调。** 所有实验由 cron 监控，完成后自动触发回调。

### 4. 📋 待办（条件触发式）
- eval-obs-only-object-seed43 完成 → **最关键**：与 seed=42 (19%) 合并做 Fisher exact test vs argmin seed=42+43。p < 0.05 → 项目存活；p > 0.1 → 项目 dead
- eval-obs-only-object-norm02-seed43 完成 → 与 seed=42 (22%) 合并统计检验。norm=0.2 可能是最强 config
- eval-mag-obsonly-norm03-object 完成 → 如果 >22% → norm=0.3 是 object 峰值；如果 <19% → norm=0.2 是峰值，object magnitude curve 完整
- eval-acr-object-obs-only-default 完成 → 与 eval-acr-object-v4-default (perdof default) 对比。obs_only_default > perdof_default → obs_only 本质更鲁棒
- 全部 object magnitude sweep 完成 → 绘制 fig3 (obs_only vs perdof across norms, both spatial+object)
- 全部 seed=43 完成 → 7-way comparison table + Fisher exact tests，决定项目存亡
- Director 确认 paper story → spawn paper writing workers (CoRL DDL ~11 天)

### 5. 🎯 战略上下文
**核心结论链：**
- D027: perdof = argmin on spatial (per-DOF claim 死了)
- D030: Spatial ALL CRM variants dead (均收敛 ~35% = argmin)
- D032: Spatial magnitude sweep null (obs_only 全 norm 35%)
- **新发现**: Object 域 obs_only norm=0.2 = 22% = PROJECT HIGH (+10pp vs argmin)。Object 是 paper 真正的 story 载体

**项目存活条件 (D030)**: Object obs_only +6pp+ 维持 + seed=43 复现 → p < 0.05。目前 seed=42 已确认 +10pp (22% vs 12%)。等 seed=43。

**易判断错的事：**
- 不要被 spatial 35% 误导以为 CRM 无用——spatial 是 VLA backbone 瓶颈（hard tasks 全 0%），不是 CRM 问题
- obs_only norm 响应跨域不同：spatial 平坦 (35% everywhere)，object 递增 (19%→22%)。不要从 spatial 的 null 推断 object 也 null
- eval-mag-perdof-norm03-object 的 DEPLOYED 状态卡住了（状态机不允许 DEPLOYED→DONE），conclusion=killed 和 notes 已写，但 status 仍是 DEPLOYED——不影响功能但看起来奇怪
- CoRL DDL ~May 26 abstract / ~Jun 2 full paper，只剩 11 天。seed=43 结果到手后必须立即启动论文写作

## 项目硬约束 (memory.md 节选)

## bjb2-40593 环境问题 (2026-05-14-15)

- 无 .git repo
- CRM cache 路径 /root/autodl-tmp/crm_cache/spatial/（旧路径，非 v5）
- Ghost PID 211962 已 kill，eval-mag-obsonly-norm003-b2 恢复运行

## [失败模式] submit_training_job EXIT_CODE=127 (2026-05-15)

tmux 用 `sh` 而非 `bash` 执行命令，`python` 等 conda/venv 命令不在 `sh` PATH 中。修复：命令必须用 `bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && ..."` 包裹。裸 `python -u ...` 有时可行（取决于服务器 PATH 配置），但不可靠。

## [失败模式] Kill 操作前必须逐参数比对 (2026-05-15)

**事故**: Worker 将 norm=0.3 (norm03) 误判为 norm=0.03 (norm003) 的重复实验，kill 了有效进程。cuda:0 空闲 9 小时。
**根因**: Worker 只看 session 名和 output_file 路径，未核对 `--max_correction_norm` 参数值。
**规则**: kill 实验前必须 `ps aux | grep` 完整命令行，逐一比对关键参数（mode, norm, checkpoint, benchmark）。名字相似 ≠ 同一实验。

## 可查的历史
前 94 轮 handoff 在 `task_context/history/agent/loop_*.md`，如有疑问可 Read 回查。
完整聊天归档可用 `recall_session_history("关键词")` 搜索。

## 第一个动作要求
1. 用 `read_registry` 确认当前 RUNNING/PREPARING 实验状态（防止幻觉记忆过时状态）
2. 回复一句话确认你看到了上面的硬约束 + 当前活跃实验，再开始任何工具调用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "source": "system:ralph_loop"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-15T20:42:41.470363+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__main_agent_post_to_director",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__main_agent_post_to_director",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-15T20:42:41.470872+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-15T20:42:46.695523+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'RUNNING'}",
  "project": "acr-vla-conformal-refinement",
  "fields": "['exp_id', 'status', 'conclusion', 'server', 'gpu', 'metrics', 'updated_at']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'RUNNING'}",
    "project": "acr-vla-conformal-refinement",
    "fields": "['exp_id', 'status', 'conclusion', 'server', 'gpu', 'metrics', 'updated_at']"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T20:42:46.695944+00:00_

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
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T20:42:47.450997+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-mag-obsonly-norm003-b2\": {\"status\": \"RUNNING\", \"updated_at\": \"2026-05-15T20:37:54.341Z\", \"metrics\": {\"tasks_done\": 8, \"tasks_total\": 10, \"partial_sr\": {\"between_plate_and_ramekin\": 0.9, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.8, \"on_stove\": 0}, \"server\": \"bjb2-40593\", \"pid\": 227434, \"gpu\": \"cuda:0\", \"process_status\": \"alive\", \"checked_at\": \"2026-05-16T04:40:00\"}}, \"eval-mag-obsonly-norm03-object\": {\"status\": \"RUNNING\", \"updated_at\": \"2026-05-15T20:37:52.085Z\", \"metrics\": {\"tasks_done\": 2, \"tasks_total\": 10, \"partial_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0}, \"server\": \"bjb2-28827\", \"pid\": 103034, \"gpu\": \"cuda:5\", \"process_status\": \"alive\", \"checked_at\": \"2026-05-16T04:40:00\"}}, \"eval-mag-obsonly-norm005-object\": {\"status\": \"RUNNING\", \"updated_at\": \"2026-05-15T20:37:50.525Z\", \"metrics\": {\"tasks_done\": 2, \"tasks_total\": 10, \"partial_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0}, \"server\": \"bjb2-28827\", \"pid\": 101616, \"gpu\": \"cuda:4\", \"process_status\": \"alive\", \"checked_at\": \"2026-05-16T04:40:00\"}}, \"eval-mag-perdof-norm02-seed43-object-r3\": {\"status\": \"RUNNING\", \"updated_at\": \"2026-05-15T20:37:49.133Z\", \"metrics\": {\"tasks_done\": 0, \"tasks_total\": 10, \"partial_sr\": {}, \"server\": \"bjb2-28827\", \"pid\": 144513, \"gpu\": \"cuda:3\", \"process_status\": \"alive\", \"checked_at\": \"2026-05-16T04:40:00\"}}, \"eval-mag-perdof-norm03-object-r3\": {\"status\": \"RUNNING\", \"updated_at\": \"2026-05-15T20:37:47.309Z\", \"metrics\": {\"tasks_done\": 0, \"tasks_total\": 10, \"partial_sr\": {}, \"server\": \"bjb2-28827\", \"pid\": 140759, \"gpu\": \"cuda:2\", \"process_status\": \"alive\", \"checked_at\": \"2026-05-16T04:40:00\"}}, \"eval-mag-perdof-norm005-object\": {\"sta
…[truncated 4657 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 755
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T20:42:47.503314+00:00_

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
  "session": "cron:hook:eval-mag-perdof-norm03-object",
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

_source line 8 · 2026-05-15T20:42:47.553892+00:00_

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
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-15T20:43:24.419257+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 17, \"results\": [{\"exp_id\": \"eval-mag-obsonly-norm003-b2\", \"success\": true, \"actions\": [\"Job still running (pid=227434)\"]}, {\"exp_id\": \"eval-obs-only-object-seed43\", \"success\": true, \"actions\": [\"Job still running (pid=356490)\"]}, {\"exp_id\": \"eval-argmin-object-seed43\", \"success\": true, \"actions\": [\"Job still running (pid=356696)\"]}, {\"exp_id\": \"eval-perdof-object-seed43\", \"success\": true, \"actions\": [\"Job still running (pid=365925)\"]}, {\"exp_id\": \"eval-mag-obsonly-norm03-object\", \"success\": true, \"actions\": [\"Job still running (pid=103028)\"]}, {\"exp_id\": \"eval-mag-obsonly-norm005-object\", \"success\": true, \"actions\": [\"Job still running (pid=101610)\"]}, {\"exp_id\": \"eval-vla-mean-object-seed43\", \"success\": true, \"actions\": [\"Job still running (pid=111709)\"]}, {\"exp_id\": \"eval-scalar-object-seed43\", \"success\": true, \"actions\": [\"Job still running (pid=114664)\"]}, {\"exp_id\": \"eval-mag-obsonly-norm003-object\", \"success\": true, \"actions\": [\"Job still running (pid=121325)\"]}, {\"exp_id\": \"eval-acr-object-v4-default-r2\", \"success\": true, \"actions\": [\"Job still running (pid=390936)\"]}, {\"exp_id\": \"eval-mag-perdof-norm02-object\", \"success\": true, \"actions\": [\"Job still running (pid=127732)\"]}, {\"exp_id\": \"eval-mag-perdof-norm005-object\", \"success\": true, \"actions\": [\"Job still running (pid=109650)\"]}, {\"exp_id\": \"eval-mag-perdof-norm003-object\", \"success\": true, \"actions\": [\"Job still running (pid=105938)\"]}, {\"exp_id\": \"eval-acr-object-obs-only-default\", \"success\": true, \"actions\": [\"Job still running (pid=134103)\"]}, {\"exp_id\": \"eval-obs-only-object-norm02-seed43-r2\", \"success\": true, \"actions\": [\"Job still running (pid=148788)\"]}, {\"exp_id\": \"eval-mag-perdof-norm02-seed43-object-r3\", \"success\": true, \"actions\": [\"Job still running (pid=144504)\"]}, {\"exp_id\
…[truncated 150 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 37723
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T20:43:24.419983+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md\", \"content\": \"# Handover — 2026-05-15\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| eval-mag-perdof-norm02-seed43-object-r3 | — | — | — | — |\\n| eval-mag-perdof-norm03-object-r3 | — | — | — | — |\\n| eval-acr-object-obs-only-default | obs_only CRM v3-norm with DEFAULT max_correction_norm (~1.42, no magnitude control) on LIBERO object benchmark. Paired with eval-acr-object-v4-default (perdof default). Tests whether obs_only robustness holds even without magnitude capping — if yes, obs_only is fundamentally more robust than perdof regardless of norm setting. | — | — | — |\\n\\n## 待处理\\n- eval-mag-obsonly-norm03-b2: Magnitude sweep: obs_only CRM v3-norm at norm=0.3 on spatial. Retry of eval-mag-obsonly-norm03 (EXIT_CODE=127). Fills obs_only norm=0.3 gap. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade, strong evidence for obs_only robustness.（等待人工审批）\\n\\n## 近期结论\\n- **eval-mag-perdof-norm02-seed43-object-r2** (killed): Object magnitude sweep: perdof CRM v3-norm norm=0.2 seed=43. Moved from bjb2-28827:cuda:3 (GPU conflict with obs_only spatial) to cuda:2. Tests perdof norm sensitivity with second seed.\\n- **eval-mag-obsonly-norm03** (killed): Magnitude sweep: obs_only CRM v3-norm at norm=0.3 on spatial. Fills obs_only norm=0.3 gap. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade at same norm, strong evidence for obs_only robustness. ← 基于 eval-mag-obsonly-norm02\\n- **eval-mag-obsonly-norm02-object** (killed): —\\n\\n## 趋势\\n成功 35 / 负向 5 / 失败 17 / 共 106\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nbjb1-18228: 无 GPU 信息\\nbjb1-32546: 空闲 cuda:0, cuda:1, cuda:2, cuda:3, cuda:4, cuda:5\\nbjb2-28827: 空闲 cuda:0, cuda:1, cuda:2, cuda:3, cuda:4, cuda:5\\nbjb2-40593: 无 GPU 信息\\n\\n## 告警\\n- 
…[truncated 3046 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 36916
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T20:43:24.471009+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-15 20:13 UTC | 更新原因: 引用审计降级为未完成（方法归因未验证）; norm=0.03 数据更新至 7t 44.3%\\n\\n## 核心方向\\nobs_only CRM（基于观测特征的 learned correction）是唯一存活路径。Per-DOF conformal claim 已死。论文 story：sample-then-correct > sample-then-select，obs features > conformal features（honest negative）。详见 paper_framing.md。\\n\\n## 投稿目标\\n**CoRL 2026**（abstract DDL ~May 26, full paper DDL ~Jun 2）。剩余 ~11 天。\\n\\n## 当前进展\\n- **阶段**: Phase 3 — Paper writing + seed=43 statistical validation\\n- **MVP**: PASS\\n- **Object 10/10 FINAL ✅**: obs_only 19.0% vs argmin 12.0% (+7.0pp) — 超过 5pp claim 门槛 (D033)\\n- **Object obs_only norm=0.2 FINAL ✅**: **22.0%** (+10.0pp over argmin) — **PROJECT HIGH**\\n- **Spatial LOCKED ✅**: 全部 CRM 变体确认 dead（argmin 34%, perdof 35%, obs_only 35%, scalar 32%）\\n- **Magnitude sweep**: obs_only stable 35-36% across norms, perdof collapses away from 0.1 (D032)\\n- **Seed=43 部署中**: 6 方在跑，obs_only 6/10, argmin 6/10, 预计 ~12h\\n- **Paper Agent**: Intro ✅ Method ✅ Experiments ✅ Related Work ✅ → Abstract + Discussion 进行中\\n- **引用审计**: ⚠️ 论文存在性已验证，但**方法归因准确性未验证**。chen2026reconvla 归因错误已确认。Paper Agent 正在重做全量方法归因审计。**提交前 blocking item。**\\n\\n## Object Benchmark（seed=42, ALL FINAL ✅）\\n\\n| 方法 | SR | vs argmin | 状态 |\\n|------|-----|-----------|------|\\n| **obs_only 0.2** | **22.0%** | **+10.0pp** | FINAL ✅ PROJECT HIGH |\\n| **obs_only 0.1** | **19.0%** | **+7.0pp** | FINAL ✅ |\\n| argmin K=10 | 12.0% | baseline | FINAL ✅ |\\n| VLA-only K=1 | 12.0% | 0pp | FINAL ✅ |\\n| VLA-mean K=10 | 12.0% | 0pp | FINAL ✅ |\\n| perdof 0.1 | 11.0% | -1.0pp | FINAL ✅ |\\n| scalar 0.1 | 9.0% | -3.0pp | FINAL ✅ (negative) |\\n\\n## Spatial 最终结果（LOCKED ✅）\\n\\n| 方法 | 10-task SR | vs argmin |\\n|------|-----------|-----------|\\n| argmin K=10 | 34% | baseline |\\n| perdof 0.1 | 35% | +
…[truncated 3709 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 36917
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T20:43:42.440391+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'DONE'}",
  "project": "acr-vla-conformal-refinement",
  "fields": "['exp_id', 'status', 'conclusion', 'metrics', 'updated_at']",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'DONE'}",
    "project": "acr-vla-conformal-refinement",
    "fields": "['exp_id', 'status', 'conclusion', 'metrics', 'updated_at']",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-15T20:43:42.793921+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-mag-perdof-norm02-seed43-object-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:38:38.710Z\", \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm03\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:38:31.587Z\", \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm02-object\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:34:07.651Z\", \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm03-b4\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:27:30.465Z\", \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm03-b3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:27:28.479Z\", \"conclusion\": \"killed\"}, \"eval-mag-perdof-norm02-seed43-object\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:25:28.957Z\", \"conclusion\": \"killed\"}, \"eval-mag-perdof-norm03-object-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:25:28.055Z\", \"conclusion\": \"killed\"}, \"eval-acr-object-v4-scalar-b2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:17:41.948Z\", \"conclusion\": \"killed\"}, \"eval-acr-object-v4-obs-only-b2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:17:40.199Z\", \"conclusion\": \"killed\"}, \"eval-spatial-v4-full\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:17:39.068Z\", \"conclusion\": \"killed\"}, \"eval-reconvla-spatial-v1\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:17:37.622Z\", \"conclusion\": \"killed\"}, \"eval-object-v6-full\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:17:36.369Z\", \"conclusion\": \"killed\"}, \"precompute-v4-shard2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:17:35.000Z\", \"conclusion\": \"success\"}, \"precompute-v4-shard1\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:17:33.288Z\", \"conclusion\": \"success\"}, \"precompute-v4-shard0\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:17:32.128Z\", \"conclusion\"
…[truncated 132 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 353
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T20:44:19.269559+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__list_workers,mcp__agent-ml-research__read_project_file",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__list_workers,mcp__agent-ml-research__read_project_file",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-15T20:44:19.320301+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-15T20:44:23.339217+00:00_

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
  "session": "cron:hook:eval-mag-perdof-norm03-object",
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

_source line 17 · 2026-05-15T20:44:23.590510+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [], \"count\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 251
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T20:44:23.590928+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "memory.md",
  "max_chars": "6000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "file": "memory.md",
    "max_chars": "6000"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-15T20:44:23.641616+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md\", \"content\": \"# Project Memory\\n\\n## Spatial Baselines 锁定 (2026-05-15)\\n\\n| 方法 | SR | 来源 |\\n|------|-----|------|\\n| VLA-only K=1 | 30% | eval-spatial-v7-full |\\n| VLA-mean K=10 | 32% | eval-vla-mean-spatial |\\n| Argmin K=10 | 34% | eval-argmin-only-spatial-r2 (与 reconvla-v3 独立复现一致) |\\n\\n**关键发现**: K=10 采样 + scalar argmin 选择增益有限 (+2pp over mean, +4pp over K=1)。CRM correction 的 bar 是 34%。\\n\\n## Hard Tasks 普遍失败 (2026-05-15)\\n\\nT2 (from_table_center), T7 (on_stove): 所有方法 0%。T4 (in_top_drawer), T5 (on_ramekin): 所有方法 0-10%。这是 VLA backbone 限制，不是 CRM 问题。论文不应在这些 tasks 上 claim CRM 改进。\\n\\n## D027 CRITICAL: perdof = argmin on matched tasks (2026-05-15)\\n\\nT0-T6 matched comparison: perdof 42.9% = argmin ~43% (0pp delta)。Per-DOF claim 在 spatial 上已死。项目存活依赖：\\n1. Magnitude sweep 找到 perdof 显著优于 argmin 的 norm 点\\n2. Object benchmark 跨域验证\\n3. obs_only CRM +5pp 稳定 → 转向 \\\"learned correction\\\" narrative\\n\\n## obs_only 走势 (2026-05-15)\\n\\nobs_only 从 57.5%@4tasks 降到 40%@6tasks（hard tasks 拖累）。但 obs_only 在 magnitude sweep 中每个已测 norm 下都 >= perdof (+10-20pp，仅 2 tasks)。如果趋势在 5+ tasks 后仍保持，论文可转向 \\\"obs-only CRM correction\\\" narrative。\\n\\n## Object magnitude 与 spatial 不同 (2026-05-15)\\n\\n**关键发现**: obs_only 对 correction norm 的响应跨域差异显著：\\n- Spatial: obs_only 在所有 norm (0.05/0.1/0.2/0.3) 下收敛到 ~35%，与 argmin 持平，magnitude 无效应\\n- Object: obs_only norm=0.1=19%, norm=0.2=**22%** (PROJECT HIGH)，更大 correction 产生更高 SR\\n- **论文角度**: Object 域 CRM correction 有真实增益空间（baseline 12%），spatial 域 VLA backbone 是瓶颈（hard tasks 全 0%）。Paper 应以 object 结果为主故事载体，spatial 作为 robustness/generalization 验证。\\n\\n## Object Baseline (2026-05-15)\\n\\nVLA-only K=1 object = 12%。CRM 在 object benchmark 有更大提升空间（baseline 低）。\\n\\n## bjb2-40593 环境问题 (2026-05-14-15)\\n\\n- 无 .git repo\\n- CRM cache 路径 /root/autodl-tmp/crm_cache/spatial/（旧路径，非 v5）\\n- Ghost P
…[truncated 938 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-15T20:44:42.079554+00:00_

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
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/skills/resource-saturation.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-15T20:44:42.080086+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/sessions/agent_4ef5111f.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-15T20:44:44.338878+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/resource-saturation*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/resource-saturation*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-15T20:44:44.389544+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-15T20:44:46.345511+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/skills/**/*resource*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/skills/**/*resource*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-15T20:44:46.396172+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-15T20:45:03.106099+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__save_project_file",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__save_project_file",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-15T20:45:03.206931+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-15T20:45:42.030459+00:00_

called mcp__agent-ml-research__spawn_worker

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker</summary>

```json
{
  "task_type": "research:reference-audit-r2",
  "project": "acr-vla-conformal-refinement",
  "task_prompt": "## 任务：论文方法归因全量审计（blocking item for CoRL submission）\n\n### 背景\n论文已完成 Intro/Method/Experiments/Related Work 四个章节。之前的引用审计验证了论文存在性，但**方法归因准确性未验证**。已确认一个错误：chen2026reconvla 的方法归因有误。\n\n这是 CoRL 提交前的 blocking item。DDL ~May 26 abstract / ~Jun 2 full paper。\n\n### 任务目标\n1. 读取所有已写的论文章节（Intro, Method, Experiments, Related Work）\n2. 对每个引用，检查：\n   - 论文中对该引用方法的描述是否准确（例如\"X proposed Y method\" → 验证 X 确实提出了 Y）\n   - 特别关注：方法分类（selection-based vs correction-based vs UQ-based）是否正确\n   - chen2026reconvla 已知归因有误（之前被标记为 selection-only，但实际是 UQ-guided approach）→ 确认是否已修复，未修复则修复\n3. 用 WebSearch 验证每个方法归因的准确性（搜索论文 title + 关键方法词）\n4. 输出：\n   - 每个引用的归因检查结果（✅ 正确 / ⚠️ 需修正 + 修正建议）\n   - 直接修复发现的错误（edit paper sections）\n   - 汇总报告写入 artifacts/reference_audit_r2.md\n\n### 论文文件位置\n用 read_project_file(project=\"acr-vla-conformal-refinement\", file=\"paper/intro.md\") 等读取。章节名: intro.md, method.md, experiments.md, related_work.md\n\n### 关键上下文\n- 项目方向：obs_only CRM（基于观测特征的 learned correction）用于 VLA action refinement\n- Paper story: sample-then-correct > sample-then-select; obs features > conformal features\n- D034 决策：ReconVLA 重新定位为\"同领域不同路线(UQ-guided)\"，不是\"直接竞品(selection-only)\"\n- per-DOF conformal claim 已死（D027），论文不应强调 perdof",
  "tool_groups": "['knowledge']",
  "tools": "['WebSearch', 'read_project_file', 'edit_paper_section', 'register_artifact']",
  "context": "D034: ReconVLA 重新定位为同领域不同路线(UQ-guided approach)，不是直接竞品(selection-only)。chen2026reconvla 归因已知有误，需要修复。论文 story: obs_only CRM correction >> argmin selection on object benchmark (+7-10pp)。Spatial 所有 CRM 变体 dead (35% = argmin baseline)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "tool_args": {
    "task_type": "research:reference-audit-r2",
    "project": "acr-vla-conformal-refinement",
    "task_prompt": "## 任务：论文方法归因全量审计（blocking item for CoRL submission）\n\n### 背景\n论文已完成 Intro/Method/Experiments/Related Work 四个章节。之前的引用审计验证了论文存在性，但**方法归因准确性未验证**。已确认一个错误：chen2026reconvla 的方法归因有误。\n\n这是 CoRL 提交前的 blocking item。DDL ~May 26 abstract / ~Jun 2 full paper。\n\n### 任务目标\n1. 读取所有已写的论文章节（Intro, Method, Experiments, Related Work）\n2. 对每个引用，检查：\n   - 论文中对该引用方法的描述是否准确（例如\"X proposed Y method\" → 验证 X 确实提出了 Y）\n   - 特别关注：方法分类（selection-based vs correction-based vs UQ-based）是否正确\n   - chen2026reconvla 已知归因有误（之前被标记为 selection-only，但实际是 UQ-guided approach）→ 确认是否已修复，未修复则修复\n3. 用 WebSearch 验证每个方法归因的准确性（搜索论文 title + 关键方法词）\n4. 输出：\n   - 每个引用的归因检查结果（✅ 正确 / ⚠️ 需修正 + 修正建议）\n   - 直接修复发现的错误（edit paper sections）\n   - 汇总报告写入 artifacts/reference_audit_r2.md\n\n### 论文文件位置\n用 read_project_file(project=\"acr-vla-conformal-refinement\", file=\"paper/intro.md\") 等读取。章节名: intro.md, method.md, experiments.md, related_work.md\n\n### 关键上下文\n- 项目方向：obs_only CRM（基于观测特征的 learned correction）用于 VLA action refinement\n- Paper story: sample-then-correct > sample-then-select; obs features > conformal features\n- D034 决策：ReconVLA 重新定位为\"同领域不同路线(UQ-guided)\"，不是\"直接竞品(selection-only)\"\n- per-DOF conformal claim 已死（D027），论文不应强调 perdof",
    "tool_groups": "['knowledge']",
    "tools": "['WebSearch', 'read_project_file', 'edit_paper_section', 'register_artifact']",
    "context": "D034: ReconVLA 重新定位为同领域不同路线(UQ-guided approach)，不是直接竞品(selection-only)。chen2026reconvla 归因已知有误，需要修复。论文 story: obs_only CRM correction >> argmin selection on object benchmark (+7-10pp)。Spatial 所有 CRM 变体 dead (35% = argmin baseline)。"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-15T20:46:00.870351+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_research_reference-audit-r2_20260515T204542\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_research_reference-audit-r2_20260515T204542.log\", \"setup_data\": {}, \"message\": \"Worker worker_research_reference-audit-r2_20260515T204542 started. Use get_worker_status('worker_research_reference-audit-r2_20260515T204542') to check progress.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "elapsed_ms": 18839
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-15T20:46:02.317701+00:00_

called mcp__agent-ml-research__spawn_worker

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker</summary>

```json
{
  "task_type": "code:stat-analysis-prep",
  "project": "acr-vla-conformal-refinement",
  "task_prompt": "## 任务：准备统计分析代码（Fisher exact test + Bootstrap CI）\n\n### 背景\n项目正在跑 seed=43 复现实验（object benchmark，7 个方法）。seed=42 已完成。两轮 seed 完成后需要立即做统计检验，判断项目存活。\n\n### 数据结构\n每个方法在每个 seed 下跑 10 个 LIBERO object tasks，每个 task 10 episodes。\n- 成功率 = 总成功 episodes / 总 episodes = successes / 100\n\nSeed=42 已知结果（object benchmark, 10 tasks, 100 episodes each）：\n| 方法 | SR | 成功数/100 |\n|------|-----|-----------|\n| obs_only 0.1 | 19% | 19/100 |\n| obs_only 0.2 | 22% | 22/100 |\n| argmin | 12% | 12/100 |\n| VLA-only K=1 | 12% | 12/100 |\n| VLA-mean K=10 | 12% | 12/100 |\n| perdof 0.1 | 11% | 11/100 |\n| scalar 0.1 | 9% | 9/100 |\n\nSeed=43 正在跑，预计 ~12h 完成。\n\n### 需要写的代码\n写一个 Python 脚本 `stat_analysis.py`，放在本地 artifacts/ 目录下：\n\n1. **Fisher exact test (2x2)**:\n   - 主检验: obs_only vs argmin (pooled across seeds)\n   - 例: obs_only 19+X successes out of 200 vs argmin 12+Y out of 200\n   - 输出 p-value, odds ratio, 95% CI for odds ratio\n   \n2. **Bootstrap CI for SR difference**:\n   - 10000 bootstrap resamples\n   - 95% CI for (obs_only_SR - argmin_SR)\n   - 也算 obs_only_0.2 vs argmin\n\n3. **7-way comparison table**:\n   - 所有方法 pairwise Fisher test (with Bonferroni correction)\n   - Format as LaTeX table\n\n4. **输入方式**:\n   - 脚本接受 JSON 输入文件，格式: {\"method_name\": {\"seed42\": {\"successes\": N, \"total\": 100}, \"seed43\": {\"successes\": M, \"total\": 100}}}\n   - 也提供一个 template JSON 文件 `seed_results_template.json`，seed=42 数据预填，seed=43 留空待填\n\n5. **输出**:\n   - Console: 关键 p-values 和 CI\n   - LaTeX table string (可直接粘贴到论文)\n   - JSON summary\n\n### 依赖\n仅用标准库 + scipy + numpy（服务器已有）。\n\n### 验证\n写完后用 seed=42 数据做 dry-run（假设 seed=43 = seed=42），确认脚本能正常运行。",
  "tool_groups": "['knowledge']",
  "tools": "['register_artifact']",
  "repo_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "tool_args": {
    "task_type": "code:stat-analysis-prep",
    "project": "acr-vla-conformal-refinement",
    "task_prompt": "## 任务：准备统计分析代码（Fisher exact test + Bootstrap CI）\n\n### 背景\n项目正在跑 seed=43 复现实验（object benchmark，7 个方法）。seed=42 已完成。两轮 seed 完成后需要立即做统计检验，判断项目存活。\n\n### 数据结构\n每个方法在每个 seed 下跑 10 个 LIBERO object tasks，每个 task 10 episodes。\n- 成功率 = 总成功 episodes / 总 episodes = successes / 100\n\nSeed=42 已知结果（object benchmark, 10 tasks, 100 episodes each）：\n| 方法 | SR | 成功数/100 |\n|------|-----|-----------|\n| obs_only 0.1 | 19% | 19/100 |\n| obs_only 0.2 | 22% | 22/100 |\n| argmin | 12% | 12/100 |\n| VLA-only K=1 | 12% | 12/100 |\n| VLA-mean K=10 | 12% | 12/100 |\n| perdof 0.1 | 11% | 11/100 |\n| scalar 0.1 | 9% | 9/100 |\n\nSeed=43 正在跑，预计 ~12h 完成。\n\n### 需要写的代码\n写一个 Python 脚本 `stat_analysis.py`，放在本地 artifacts/ 目录下：\n\n1. **Fisher exact test (2x2)**:\n   - 主检验: obs_only vs argmin (pooled across seeds)\n   - 例: obs_only 19+X successes out of 200 vs argmin 12+Y out of 200\n   - 输出 p-value, odds ratio, 95% CI for odds ratio\n   \n2. **Bootstrap CI for SR difference**:\n   - 10000 bootstrap resamples\n   - 95% CI for (obs_only_SR - argmin_SR)\n   - 也算 obs_only_0.2 vs argmin\n\n3. **7-way comparison table**:\n   - 所有方法 pairwise Fisher test (with Bonferroni correction)\n   - Format as LaTeX table\n\n4. **输入方式**:\n   - 脚本接受 JSON 输入文件，格式: {\"method_name\": {\"seed42\": {\"successes\": N, \"total\": 100}, \"seed43\": {\"successes\": M, \"total\": 100}}}\n   - 也提供一个 template JSON 文件 `seed_results_template.json`，seed=42 数据预填，seed=43 留空待填\n\n5. **输出**:\n   - Console: 关键 p-values 和 CI\n   - LaTeX table string (可直接粘贴到论文)\n   - JSON summary\n\n### 依赖\n仅用标准库 + scipy + numpy（服务器已有）。\n\n### 验证\n写完后用 seed=42 数据做 dry-run（假设 seed=43 = seed=42），确认脚本能正常运行。",
    "tool_groups": "['knowledge']",
    "tools": "['register_artifact']",
    "repo_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-15T21:02:28.906390+00:00_

Worker 池 = 0，需要立即 spawn。开两个非 GPU worker：引用审计（blocking）+ 统计分析代码准备。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval-mag-perdof-norm03-object"
}
```

</details>

---

## Round 2

54 recorded events

### User

_source line 32 · 2026-05-16T00:38:22.582731+00:00_

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
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "source": "system:ralph_loop"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-16T00:38:49.499207+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Read project state files",
  "subagent_type": "Explore",
  "prompt": "I need to read several project files to understand the current state of the \"acr-vla-conformal-refinement\" project. Find and read the following files:\n\n1. Any registry.yaml or registry file under /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/\n2. report.md under the same project directory\n3. ROADMAP.md under the same project directory\n4. memory.md under the same project directory\n5. experiment_plan.yaml under the same project directory\n6. paper_framing.md under the same project directory\n\nSearch broadly - these files might be in subdirectories. Read as much content as possible from each file found. Report the full contents of each file."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "Agent",
  "tool_args": {
    "description": "Read project state files",
    "subagent_type": "Explore",
    "prompt": "I need to read several project files to understand the current state of the \"acr-vla-conformal-refinement\" project. Find and read the following files:\n\n1. Any registry.yaml or registry file under /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/\n2. report.md under the same project directory\n3. ROADMAP.md under the same project directory\n4. memory.md under the same project directory\n5. experiment_plan.yaml under the same project directory\n6. paper_framing.md under the same project directory\n\nSearch broadly - these files might be in subdirectories. Read as much content as possible from each file found. Report the full contents of each file."
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-16T00:38:51.837220+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/**/registry*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/**/registry*"
  }
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-16T00:38:51.867761+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/**/report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/**/report.md"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-16T00:38:52.000688+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.lock
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "Glob",
  "elapsed_ms": 163
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-16T00:38:52.061039+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/**/ROADMAP.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/**/ROADMAP.md"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-16T00:38:52.317908+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "Glob",
  "elapsed_ms": 450
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-16T00:38:52.380493+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "Glob",
  "elapsed_ms": 319
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-16T00:38:52.688460+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/**/memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/**/memory.md"
  }
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-16T00:38:52.821591+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/**/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/**/experiment_plan.yaml"
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-16T00:38:53.124109+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/**/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/**/paper_framing.md"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-16T00:38:53.142701+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "Glob",
  "elapsed_ms": 454
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-16T00:38:53.143292+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/experiment_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "Glob",
  "elapsed_ms": 321
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-16T00:38:53.198186+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/dream_reports/dream_20260513T023849/best/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/dream_reports/dream_20260513T023849/median/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/dream_reports/dream_20260513T023849/worst/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "Glob",
  "elapsed_ms": 74
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-16T00:38:54.976827+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml"
  }
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-16T00:38:55.185704+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-16T00:38:55.612471+00:00_

File content (71437 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "Read",
  "elapsed_ms": 635
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-16T00:38:55.612972+00:00_

1	# Handover — 2026-05-16
2	
3	> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。
4	
5	## 运行中
6	| exp_id | 假设 | 状态 | 关键指标 | W&B |
7	|--------|------|------|---------|-----|
8	| eval-mag-obsonly-norm003-b2 | — | — | — | — |
9	| eval-mag-obsonly-norm03-object | — | — | — | — |
10	| eval-mag-obsonly-norm005-object | — | — | — | — |
11	
12	## 待处理
13	- eval-mag-obsonly-norm03-b2: Magnitude sweep: obs_only CRM v3-norm at norm=0.3 on spatial. Retry of eval-mag-obsonly-norm03 (EXIT_CODE=127). Fills obs_only norm=0.3 gap. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade, strong evidence for obs_only robustness.（等待人工审批）
14	
15	## 近期结论
16	- **eval-argmin-object-seed43** (success): D031: argmin baseline (K=10, scalar Euclidean argmin) seed=43 on LIBERO object benchmark. Paired with eval-obs-only-object-seed43 for Fisher exact test. Need both conditions under same seed for valid comparison. ← 基于 eval-reconvla-object
17	- **eval-mag-perdof-norm02-seed43-object-r2** (killed): Object magnitude sweep: perdof CRM v3-norm norm=0.2 seed=43. Moved from bjb2-28827:cuda:3 (GPU conflict with obs_only spatial) to cuda:2. Tests perdof norm sensitivity with second seed.
18	- **eval-mag-obsonly-norm03** (killed): Magnitude sweep: obs_only CRM v3-norm at norm=0.3 on spatial. Fills obs_only norm=0.3 gap. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade at same norm, strong evidence for obs_only robustness. ← 基于 eval-mag-obsonly-norm02
19	
20	## 趋势
21	成功 36 / 负向 5 / 失败 17 / 共 107
22	
23	## 下一步
24	（无活跃 idea，请通过 ideas.md 添加）
25	
26	## 资源状态
27	bjb1-18228: 无 GPU 信息
28	bjb1-32546: 空闲 cuda:0, cuda:1, cuda:2, cuda:3, cuda:4, cuda:5
29	bjb2-28827: 空闲 cuda:0, cuda:1, cuda:2, cuda:3, cuda:4, cuda:5
30	bjb2-40593: 无 GPU 信息
31	
32	## 告警
33	- plan_001-crm-smolvla: 训练失败 — unknown
34	- plan_014-reconvla-baseline: 训练失败 — unknown
35	- eval-smolvla-libero-spatial: 训练失败 — unknown
36	- eval-spatial-reeval-v2: 已被终止 — unknown
37	- precompute-v2-shard0: 已被终止 — unknown
38	- precompute-v2-shard1: 已被终止
…[truncated 2775 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "Read",
  "elapsed_ms": 427
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-16T00:38:55.673519+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-16T00:38:55.802879+00:00_

1	# acr-vla-conformal-refinement — Research Dashboard
2	
3	> 最后更新: 2026-05-15 20:48 UTC | 更新原因: 引用审计 PASSED + ±1pp 统一完成 + Discussion/Conclusion 完成; 更新近期任务清单
4	
5	## 核心方向
6	obs_only CRM（基于观测特征的 learned correction）是唯一存活路径。Per-DOF conformal claim 已死。论文 story：sample-then-correct > sample-then-select，obs features > conformal features（honest negative）。详见 paper_framing.md。
7	
8	## 投稿目标
9	**CoRL 2026**（abstract DDL ~May 26, full paper DDL ~Jun 2）。剩余 ~11 天。
10	
11	## 当前进展
12	- **阶段**: Phase 3 — Paper writing + seed=43 statistical validation
13	- **MVP**: PASS
14	- **Object 10/10 FINAL ✅**: obs_only 19.0% vs argmin 12.0% (+7.0pp) — 超过 5pp claim 门槛 (D033)
15	- **Object obs_only norm=0.2 FINAL ✅**: **22.0%** (+10.0pp over argmin) — **PROJECT HIGH**
16	- **Spatial LOCKED ✅**: 全部 CRM 变体确认 dead（argmin 34%, perdof 35%, obs_only 35%, scalar 32%）
17	- **Magnitude sweep**: obs_only stable 35-44% across norms, perdof collapses away from 0.1 (D032)
18	- **Seed=43 部署中**: 6 方在跑，obs_only 6/10, argmin 6/10, 预计 ~4-5h
19	- **Paper Agent**: Intro ✅ Method ✅ Experiments ✅ Related Work ✅ Discussion/Conclusion ✅ → Figures 进行中 (fig1 WIP, fig2/fig3 pending)
20	- **引用审计**: ✅ PASSED — 29 cited keys 全部验证, 22 方法归因验证通过, 0 NEEDS_REVIEW, chen2026reconvla + braun2025cgs 两个 blocking issue 已修复
21	- **±1pp 措辞**: ✅ 全文统一为 `best CRM within 1\,pp of the selection baseline`
22	
23	## Object Benchmark（seed=42, ALL FINAL ✅）
24	
25	| 方法 | SR | vs argmin | 状态 |
26	|------|-----|-----------|------|
27	| **obs_only 0.2** | **22.0%** | **+10.0pp** | FINAL ✅ PROJECT HIGH |
28	| **obs_only 0.1** | **19.0%** | **+7.0pp** | FINAL ✅ |
29	| argmin K=10 | 12.0% | baseline | FINAL ✅ |
30	| VLA-only K=1 | 12.0% | 0pp | FINAL ✅ |
31	| VLA-mean K=10 | 12.0% | 0pp | FINAL ✅ |
32	| perdof 0.1 | 11.0% | -1.0pp | FINAL ✅ |
33	| scalar 0.1 | 9.0% | -3.0pp | FINAL ✅ (negative) |
34	
35	## Spatial 最终结果（LOCKED ✅）
36	
37	| 方法 | 10-task SR | vs argmin |
38	|------|-----------|-----------|
39	| argmin K=10 | 34% | baseline |
40	| perdof 0.1 |
…[truncated 3809 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "Read",
  "elapsed_ms": 129
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-16T00:38:55.878154+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md"
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-16T00:38:56.020655+00:00_

1	# Project Memory
2	
3	## Spatial Baselines 锁定 (2026-05-15)
4	
5	| 方法 | SR | 来源 |
6	|------|-----|------|
7	| VLA-only K=1 | 30% | eval-spatial-v7-full |
8	| VLA-mean K=10 | 32% | eval-vla-mean-spatial |
9	| Argmin K=10 | 34% | eval-argmin-only-spatial-r2 (与 reconvla-v3 独立复现一致) |
10	
11	**关键发现**: K=10 采样 + scalar argmin 选择增益有限 (+2pp over mean, +4pp over K=1)。CRM correction 的 bar 是 34%。
12	
13	## Hard Tasks 普遍失败 (2026-05-15)
14	
15	T2 (from_table_center), T7 (on_stove): 所有方法 0%。T4 (in_top_drawer), T5 (on_ramekin): 所有方法 0-10%。这是 VLA backbone 限制，不是 CRM 问题。论文不应在这些 tasks 上 claim CRM 改进。
16	
17	## D027 CRITICAL: perdof = argmin on matched tasks (2026-05-15)
18	
19	T0-T6 matched comparison: perdof 42.9% = argmin ~43% (0pp delta)。Per-DOF claim 在 spatial 上已死。项目存活依赖：
20	1. Magnitude sweep 找到 perdof 显著优于 argmin 的 norm 点
21	2. Object benchmark 跨域验证
22	3. obs_only CRM +5pp 稳定 → 转向 "learned correction" narrative
23	
24	## obs_only 走势 (2026-05-15)
25	
26	obs_only 从 57.5%@4tasks 降到 40%@6tasks（hard tasks 拖累）。但 obs_only 在 magnitude sweep 中每个已测 norm 下都 >= perdof (+10-20pp，仅 2 tasks)。如果趋势在 5+ tasks 后仍保持，论文可转向 "obs-only CRM correction" narrative。
27	
28	## Object magnitude 与 spatial 不同 (2026-05-15)
29	
30	**关键发现**: obs_only 对 correction norm 的响应跨域差异显著：
31	- Spatial: obs_only 在所有 norm (0.05/0.1/0.2/0.3) 下收敛到 ~35%，与 argmin 持平，magnitude 无效应
32	- Object: obs_only norm=0.1=19%, norm=0.2=**22%** (PROJECT HIGH)，更大 correction 产生更高 SR
33	- **论文角度**: Object 域 CRM correction 有真实增益空间（baseline 12%），spatial 域 VLA backbone 是瓶颈（hard tasks 全 0%）。Paper 应以 object 结果为主故事载体，spatial 作为 robustness/generalization 验证。
34	
35	## Object Baseline (2026-05-15)
36	
37	VLA-only K=1 object = 12%。CRM 在 object benchmark 有更大提升空间（baseline 低）。
38	
39	## bjb2-40593 环境问题 (2026-05-14-15)
40	
41	- 无 .git repo
42	- CRM cache 路径 /root/autodl-tmp/crm_cache/spatial/（旧路径，非 v5）
43	- Ghost PID 211962 已 kill，eval-mag-obsonly-norm003-b2 恢复运行
44	
45	## [失败模式] submit_training_job EXIT_CODE=127 (2026-05-15)
46	
47	tmux 用 `sh` 而非 `bash` 执
…[truncated 719 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "Read",
  "elapsed_ms": 142
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-16T00:38:56.077543+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/experiment_plan.yaml"
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-16T00:38:56.269499+00:00_

1	experiments:
2	- id: plan_000
3	  claim: 1
4	  description: 'Motivating experiment: 3D point-reaching, per-DOF vs scalar vs no
5	    uncertainty conditioning'
6	  priority: P0
7	  gpu_budget_hours: 0.5
8	  deps: []
9	  registry_id: mvp-point-reaching
10	- id: plan_001
11	  claim: 1
12	  description: 'ACR-VLA full pipeline on SmolVLA base: CGS + ACI/COC + CRM. Train
13	    CRM on LIBERO demos + synthetic augmentation. Evaluate on LIBERO (nominal preservation)
14	    + LIBERO-Plus L3-L5 (robustness gain).'
15	  priority: P0
16	  gpu_budget_hours: 25
17	  deps: []
18	  registry_id: crm-train-v1
19	- id: plan_002
20	  claim: 1
21	  description: Ablation A3 — CRM without conformal features (observation-conditioned
22	    residual only, equivalent to A2C2-style generic residual). MAKE-OR-BREAK for Claim
23	    1.
24	  priority: P0
25	  gpu_budget_hours: 8
26	  deps:
27	  - plan_001
28	  registry_id: crm-train-a3-obs-only
29	- id: plan_003
30	  claim: 1
31	  description: Ablation A4 — CRM with scalar uncertainty (Euclidean distance like
32	    ReconVLA) replacing 40D per-DOF features. Validates per-DOF > scalar.
33	  priority: P0
34	  gpu_budget_hours: 8
35	  deps:
36	  - plan_001
37	- id: plan_004
38	  claim: 3
39	  description: 'ACR-VLA stacked on SRPO-finetuned VLA. Train new CRM on SRPO checkpoint
40	    + LIBERO demos. Evaluate on LIBERO-Plus. Primary impact argument: orthogonal to
41	    training-time optimization.'
42	  priority: P0
43	  gpu_budget_hours: 18
44	  deps:
45	  - plan_001
46	- id: plan_005
47	  claim: 2
48	  description: 'COC signal validation: (a) Spearman ρ between episode COC coverage
49	    fraction and task success, (b) ACI convergence plot, (c) ellipsoid volume comparison
50	    vs static calibration at matched coverage.'
51	  priority: P1
52	  gpu_budget_hours: 15
53	  deps:
54	  - plan_001
55	- id: plan_006
56	  claim: 2
57	  description: Ablation A1 — CRM without ACI (static CGS calibration, no online adaptation).
58	    Isolates ACI contribu
…[truncated 3117 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "Read",
  "elapsed_ms": 191
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-16T00:38:56.335572+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md"
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-16T00:38:56.336064+00:00_

1	# Paper Framing — acr-vla-conformal-refinement
2	
3	## Target Venue
4	- **Primary: CoRL 2026** (Abstract DDL ~May 26, Full paper DDL ~Jun 2) — D021
5	- ~~ICLR 2027~~ — 不再是首要目标
6	
7	## Core Insight (Scenario C — ACTIVE, D029+D030 confirmed)
8	A lightweight observation-conditioned learned correction module (CRM), applied after conformal sample selection, can synthesize actions better than any individual VLA sample. The key contribution is the **sample-then-correct** pipeline itself and the discovery that **correction magnitude control is critical for closed-loop stability**. Per-DOF conformal features as CRM input offer no additional value over observation features — an honest negative result that challenges the intuition from synthetic experiments.
9	
10	## Active Framing: Scenario C
11	**Confirmed by data**: obs_only CRM > perdof CRM ≈ scalar CRM ≈ argmin on spatial (D029-D030); obs_only CRM **+7.0pp** over argmin on object 10/10 tasks FINAL (19.0% vs 12.0%); magnitude sweep shows obs_only robust to norm while perdof collapses at high norm (D032).
12	
13	Story: "Observation-conditioned residual correction is the key contribution. The sample-then-correct pipeline (K=10 conformal selection + learned CRM correction) significantly outperforms pure sample selection on object manipulation tasks. Per-DOF conformal statistics as direct CRM input offer no advantage over observation features — but conformal prediction remains essential for the sample selection stage. Correction magnitude control is a critical and previously unrecognized factor for closed-loop VLA correction."
14	
15	## Core Claims (CoRL 单 Claim 论文)
16	
17	1. **Observation-conditioned learned correction (CRM) significantly improves VLA robustness beyond sample selection**
18	   - **主 claim**: obs_only CRM vs argmin-only ≥ 5pp on object benchmark + p < 0.05
19	   - **Spatial**: DEAD — all CRM variants 32-35% vs argmin 34%, no signal (D030)
20	   - **Object 10/10 FINAL**: obs_only 0.1: **19.0%** vs argmin **12
…[truncated 6688 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-16T00:38:59.362706+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
    "limit": "500"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-16T00:38:59.363369+00:00_

1	baseline: null
2	experiments:
3	  mvp-point-reaching:
4	    status: DONE
5	    retry_count: 0
6	    created_at: '2026-05-13T01:22:10.415Z'
7	    updated_at: '2026-05-13T22:06:11.073Z'
8	    spec:
9	      hypothesis: Per-DOF uncertainty features carry more actionable information than
10	        scalar uncertainty summaries, enabling dimension-selective correction
11	      description: '3D point-reaching MVP: 3 MLP variants (scalar/per-DOF/no uncertainty)
12	        x 6 groups (3 anisotropy ratios x 2 uncertainty sources)'
13	      server: bjb2-40593
14	      gpu: cuda:0
15	      data_count: 20000
16	      model_name: CorrectionMLP(2-layer, 64-hidden)
17	      seed: 42
18	      command: python -u run_mvp.py
19	      data_path: synthetic (generated in-script)
20	      checkpoint_path: /root/acr-vla-conformal-refinement/mvp/
21	      log_path: /root/acr-vla-conformal-refinement/mvp/mvp_results.log
22	    conclusion: success
23	    completed_at: '2026-05-13T01:44:00.055Z'
24	    metrics:
25	      group1_oracle:
26	        A_scalar:
27	          mse_x: 0.180218
28	          mse_y: 0.02497
29	          mse_z: 0.024232
30	          total: 0.076473
31	        B_perDOF:
32	          mse_x: 0.172652
33	          mse_y: 0.015544
34	          mse_z: 0.01561
35	          total: 0.067935
36	        C_none:
37	          mse_x: 0.22706
38	          mse_y: 0.025542
39	          mse_z: 0.024753
40	          total: 0.092451
41	      group2_oracle:
42	        A_scalar:
43	          mse_x: 0.064642
44	          mse_y: 0.023836
45	          mse_z: 0.022967
46	          total: 0.037148
47	        B_perDOF:
48	          mse_x: 0.053403
49	          mse_y: 0.015695
50	          mse_z: 0.01573
51	          total: 0.028276
52	        C_none:
53	          mse_x: 0.084178
54	          mse_y: 0.025427
55	          mse_z: 0.024798
56	          total: 0.044801
57	      group3_oracle:
58	        A_scalar:
59	          mse_x: 0.042948
60	          mse_y: 0.023218
61	          mse_z: 0.022365
62	   
…[truncated 18455 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-16T00:39:07.932469+00:00_

## Summary of Project Files

I've successfully located and read the key project files for **acr-vla-conformal-refinement**. Here's what I found:

### File Locations
- **registry.yaml**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml` (71K+ tokens, truncated to 500 lines)
- **report.md**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md` (complete, 99 lines)
- **ROADMAP.md**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md` (complete, 118 lines)
- **memory.md**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md` (complete, 60 lines)
- **experiment_plan.yaml**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/experiment_plan.yaml` (complete, 152 lines)
- **paper_framing.md**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md` (complete, 88 lines)

### Project Status (as of 2026-05-16)

**Core Research**: Observation-conditioned learned correction modules (CRM) for VLA action refinement. The project has pivoted to "Scenario C" — obs_only CRM is the winning approach, defeating per-DOF conformal features.

**Key Results**:
- **Object benchmark (FINAL ✅)**: obs_only CRM achieves 19.0% vs argmin baseline 12.0% (+7.0pp)
- **Object obs_only norm=0.2**: **22.0% (+10.0pp)** — PROJECT HIGH
- **Spatial**: All CRM variants (35%) tied with argmin (34%) — magnitude sweep shows obs_only stable 35-44% while perdof collapses
- **Statistics**: 36 success / 5 negative / 17 failed / 107 total experiments
- **Phase**: Paper writing + seed=43 statistical validation in progress
- **Target**: CoRL 2026 (Abstract DDL ~May 26, Full paper DDL ~Jun 2)

**Immediate Priorities**:
1. Complete seed=43 statistical validation (6 methods across 2 benchmarks, ~4-5h estimated)
2. Figure generation (fig1 WIP, fig2/fig3 
…[truncated 130 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "Agent",
  "elapsed_ms": 18433
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-16T00:39:10.664572+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-16T00:39:11.103067+00:00_

1	# Handover — 2026-05-16
2	
3	> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。
4	
5	## 运行中
6	| exp_id | 假设 | 状态 | 关键指标 | W&B |
7	|--------|------|------|---------|-----|
8	| eval-mag-obsonly-norm003-b2 | — | — | — | — |
9	| eval-mag-obsonly-norm03-object | — | — | — | — |
10	| eval-mag-obsonly-norm005-object | — | — | — | — |
11	
12	## 待处理
13	- eval-mag-obsonly-norm03-b2: Magnitude sweep: obs_only CRM v3-norm at norm=0.3 on spatial. Retry of eval-mag-obsonly-norm03 (EXIT_CODE=127). Fills obs_only norm=0.3 gap. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade, strong evidence for obs_only robustness.（等待人工审批）
14	
15	## 近期结论
16	- **eval-argmin-object-seed43** (success): D031: argmin baseline (K=10, scalar Euclidean argmin) seed=43 on LIBERO object benchmark. Paired with eval-obs-only-object-seed43 for Fisher exact test. Need both conditions under same seed for valid comparison. ← 基于 eval-reconvla-object
17	- **eval-mag-perdof-norm02-seed43-object-r2** (killed): Object magnitude sweep: perdof CRM v3-norm norm=0.2 seed=43. Moved from bjb2-28827:cuda:3 (GPU conflict with obs_only spatial) to cuda:2. Tests perdof norm sensitivity with second seed.
18	- **eval-mag-obsonly-norm03** (killed): Magnitude sweep: obs_only CRM v3-norm at norm=0.3 on spatial. Fills obs_only norm=0.3 gap. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade at same norm, strong evidence for obs_only robustness. ← 基于 eval-mag-obsonly-norm02
19	
20	## 趋势
21	成功 36 / 负向 5 / 失败 17 / 共 107
22	
23	## 下一步
24	（无活跃 idea，请通过 ideas.md 添加）
25	
26	## 资源状态
27	bjb1-18228: 无 GPU 信息
28	bjb1-32546: 空闲 cuda:0, cuda:1, cuda:2, cuda:3, cuda:4, cuda:5
29	bjb2-28827: 空闲 cuda:0, cuda:1, cuda:2, cuda:3, cuda:4, cuda:5
30	bjb2-40593: 无 GPU 信息
31	
32	## 告警
33	- plan_001-crm-smolvla: 训练失败 — unknown
34	- plan_014-reconvla-baseline: 训练失败 — unknown
35	- eval-smolvla-libero-spatial: 训练失败 — unknown
36	- eval-spatial-reeval-v2: 已被终止 — unknown
37	- precompute-v2-shard0: 已被终止 — unknown
38	- precompute-v2-shard1: 已被终止
…[truncated 2775 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "Read",
  "elapsed_ms": 438
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-16T00:39:11.103785+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-16T00:39:11.426240+00:00_

1	# Project Memory
2	
3	## Spatial Baselines 锁定 (2026-05-15)
4	
5	| 方法 | SR | 来源 |
6	|------|-----|------|
7	| VLA-only K=1 | 30% | eval-spatial-v7-full |
8	| VLA-mean K=10 | 32% | eval-vla-mean-spatial |
9	| Argmin K=10 | 34% | eval-argmin-only-spatial-r2 (与 reconvla-v3 独立复现一致) |
10	
11	**关键发现**: K=10 采样 + scalar argmin 选择增益有限 (+2pp over mean, +4pp over K=1)。CRM correction 的 bar 是 34%。
12	
13	## Hard Tasks 普遍失败 (2026-05-15)
14	
15	T2 (from_table_center), T7 (on_stove): 所有方法 0%。T4 (in_top_drawer), T5 (on_ramekin): 所有方法 0-10%。这是 VLA backbone 限制，不是 CRM 问题。论文不应在这些 tasks 上 claim CRM 改进。
16	
17	## D027 CRITICAL: perdof = argmin on matched tasks (2026-05-15)
18	
19	T0-T6 matched comparison: perdof 42.9% = argmin ~43% (0pp delta)。Per-DOF claim 在 spatial 上已死。项目存活依赖：
20	1. Magnitude sweep 找到 perdof 显著优于 argmin 的 norm 点
21	2. Object benchmark 跨域验证
22	3. obs_only CRM +5pp 稳定 → 转向 "learned correction" narrative
23	
24	## obs_only 走势 (2026-05-15)
25	
26	obs_only 从 57.5%@4tasks 降到 40%@6tasks（hard tasks 拖累）。但 obs_only 在 magnitude sweep 中每个已测 norm 下都 >= perdof (+10-20pp，仅 2 tasks)。如果趋势在 5+ tasks 后仍保持，论文可转向 "obs-only CRM correction" narrative。
27	
28	## Object magnitude 与 spatial 不同 (2026-05-15)
29	
30	**关键发现**: obs_only 对 correction norm 的响应跨域差异显著：
31	- Spatial: obs_only 在所有 norm (0.05/0.1/0.2/0.3) 下收敛到 ~35%，与 argmin 持平，magnitude 无效应
32	- Object: obs_only norm=0.1=19%, norm=0.2=**22%** (PROJECT HIGH)，更大 correction 产生更高 SR
33	- **论文角度**: Object 域 CRM correction 有真实增益空间（baseline 12%），spatial 域 VLA backbone 是瓶颈（hard tasks 全 0%）。Paper 应以 object 结果为主故事载体，spatial 作为 robustness/generalization 验证。
34	
35	## Object Baseline (2026-05-15)
36	
37	VLA-only K=1 object = 12%。CRM 在 object benchmark 有更大提升空间（baseline 低）。
38	
39	## bjb2-40593 环境问题 (2026-05-14-15)
40	
41	- 无 .git repo
42	- CRM cache 路径 /root/autodl-tmp/crm_cache/spatial/（旧路径，非 v5）
43	- Ghost PID 211962 已 kill，eval-mag-obsonly-norm003-b2 恢复运行
44	
45	## [失败模式] submit_training_job EXIT_CODE=127 (2026-05-15)
46	
47	tmux 用 `sh` 而非 `bash` 执
…[truncated 719 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "Read",
  "elapsed_ms": 322
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-16T00:39:11.426761+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-16T00:39:11.483701+00:00_

1	# acr-vla-conformal-refinement — Research Dashboard
2	
3	> 最后更新: 2026-05-15 20:48 UTC | 更新原因: 引用审计 PASSED + ±1pp 统一完成 + Discussion/Conclusion 完成; 更新近期任务清单
4	
5	## 核心方向
6	obs_only CRM（基于观测特征的 learned correction）是唯一存活路径。Per-DOF conformal claim 已死。论文 story：sample-then-correct > sample-then-select，obs features > conformal features（honest negative）。详见 paper_framing.md。
7	
8	## 投稿目标
9	**CoRL 2026**（abstract DDL ~May 26, full paper DDL ~Jun 2）。剩余 ~11 天。
10	
11	## 当前进展
12	- **阶段**: Phase 3 — Paper writing + seed=43 statistical validation
13	- **MVP**: PASS
14	- **Object 10/10 FINAL ✅**: obs_only 19.0% vs argmin 12.0% (+7.0pp) — 超过 5pp claim 门槛 (D033)
15	- **Object obs_only norm=0.2 FINAL ✅**: **22.0%** (+10.0pp over argmin) — **PROJECT HIGH**
16	- **Spatial LOCKED ✅**: 全部 CRM 变体确认 dead（argmin 34%, perdof 35%, obs_only 35%, scalar 32%）
17	- **Magnitude sweep**: obs_only stable 35-44% across norms, perdof collapses away from 0.1 (D032)
18	- **Seed=43 部署中**: 6 方在跑，obs_only 6/10, argmin 6/10, 预计 ~4-5h
19	- **Paper Agent**: Intro ✅ Method ✅ Experiments ✅ Related Work ✅ Discussion/Conclusion ✅ → Figures 进行中 (fig1 WIP, fig2/fig3 pending)
20	- **引用审计**: ✅ PASSED — 29 cited keys 全部验证, 22 方法归因验证通过, 0 NEEDS_REVIEW, chen2026reconvla + braun2025cgs 两个 blocking issue 已修复
21	- **±1pp 措辞**: ✅ 全文统一为 `best CRM within 1\,pp of the selection baseline`
22	
23	## Object Benchmark（seed=42, ALL FINAL ✅）
24	
25	| 方法 | SR | vs argmin | 状态 |
26	|------|-----|-----------|------|
27	| **obs_only 0.2** | **22.0%** | **+10.0pp** | FINAL ✅ PROJECT HIGH |
28	| **obs_only 0.1** | **19.0%** | **+7.0pp** | FINAL ✅ |
29	| argmin K=10 | 12.0% | baseline | FINAL ✅ |
30	| VLA-only K=1 | 12.0% | 0pp | FINAL ✅ |
31	| VLA-mean K=10 | 12.0% | 0pp | FINAL ✅ |
32	| perdof 0.1 | 11.0% | -1.0pp | FINAL ✅ |
33	| scalar 0.1 | 9.0% | -3.0pp | FINAL ✅ (negative) |
34	
35	## Spatial 最终结果（LOCKED ✅）
36	
37	| 方法 | 10-task SR | vs argmin |
38	|------|-----------|-----------|
39	| argmin K=10 | 34% | baseline |
40	| perdof 0.1 |
…[truncated 3809 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "Read",
  "elapsed_ms": 56
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-16T00:39:15.508524+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-16T00:39:15.785988+00:00_

1	# Paper Framing — acr-vla-conformal-refinement
2	
3	## Target Venue
4	- **Primary: CoRL 2026** (Abstract DDL ~May 26, Full paper DDL ~Jun 2) — D021
5	- ~~ICLR 2027~~ — 不再是首要目标
6	
7	## Core Insight (Scenario C — ACTIVE, D029+D030 confirmed)
8	A lightweight observation-conditioned learned correction module (CRM), applied after conformal sample selection, can synthesize actions better than any individual VLA sample. The key contribution is the **sample-then-correct** pipeline itself and the discovery that **correction magnitude control is critical for closed-loop stability**. Per-DOF conformal features as CRM input offer no additional value over observation features — an honest negative result that challenges the intuition from synthetic experiments.
9	
10	## Active Framing: Scenario C
11	**Confirmed by data**: obs_only CRM > perdof CRM ≈ scalar CRM ≈ argmin on spatial (D029-D030); obs_only CRM **+7.0pp** over argmin on object 10/10 tasks FINAL (19.0% vs 12.0%); magnitude sweep shows obs_only robust to norm while perdof collapses at high norm (D032).
12	
13	Story: "Observation-conditioned residual correction is the key contribution. The sample-then-correct pipeline (K=10 conformal selection + learned CRM correction) significantly outperforms pure sample selection on object manipulation tasks. Per-DOF conformal statistics as direct CRM input offer no advantage over observation features — but conformal prediction remains essential for the sample selection stage. Correction magnitude control is a critical and previously unrecognized factor for closed-loop VLA correction."
14	
15	## Core Claims (CoRL 单 Claim 论文)
16	
17	1. **Observation-conditioned learned correction (CRM) significantly improves VLA robustness beyond sample selection**
18	   - **主 claim**: obs_only CRM vs argmin-only ≥ 5pp on object benchmark + p < 0.05
19	   - **Spatial**: DEAD — all CRM variants 32-35% vs argmin 34%, no signal (D030)
20	   - **Object 10/10 FINAL**: obs_only 0.1: **19.0%** vs argmin **12
…[truncated 6688 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "Read",
  "elapsed_ms": 277
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-16T00:39:15.786482+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/experiment_plan.yaml"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-16T00:39:15.979581+00:00_

1	experiments:
2	- id: plan_000
3	  claim: 1
4	  description: 'Motivating experiment: 3D point-reaching, per-DOF vs scalar vs no
5	    uncertainty conditioning'
6	  priority: P0
7	  gpu_budget_hours: 0.5
8	  deps: []
9	  registry_id: mvp-point-reaching
10	- id: plan_001
11	  claim: 1
12	  description: 'ACR-VLA full pipeline on SmolVLA base: CGS + ACI/COC + CRM. Train
13	    CRM on LIBERO demos + synthetic augmentation. Evaluate on LIBERO (nominal preservation)
14	    + LIBERO-Plus L3-L5 (robustness gain).'
15	  priority: P0
16	  gpu_budget_hours: 25
17	  deps: []
18	  registry_id: crm-train-v1
19	- id: plan_002
20	  claim: 1
21	  description: Ablation A3 — CRM without conformal features (observation-conditioned
22	    residual only, equivalent to A2C2-style generic residual). MAKE-OR-BREAK for Claim
23	    1.
24	  priority: P0
25	  gpu_budget_hours: 8
26	  deps:
27	  - plan_001
28	  registry_id: crm-train-a3-obs-only
29	- id: plan_003
30	  claim: 1
31	  description: Ablation A4 — CRM with scalar uncertainty (Euclidean distance like
32	    ReconVLA) replacing 40D per-DOF features. Validates per-DOF > scalar.
33	  priority: P0
34	  gpu_budget_hours: 8
35	  deps:
36	  - plan_001
37	- id: plan_004
38	  claim: 3
39	  description: 'ACR-VLA stacked on SRPO-finetuned VLA. Train new CRM on SRPO checkpoint
40	    + LIBERO demos. Evaluate on LIBERO-Plus. Primary impact argument: orthogonal to
41	    training-time optimization.'
42	  priority: P0
43	  gpu_budget_hours: 18
44	  deps:
45	  - plan_001
46	- id: plan_005
47	  claim: 2
48	  description: 'COC signal validation: (a) Spearman ρ between episode COC coverage
49	    fraction and task success, (b) ACI convergence plot, (c) ellipsoid volume comparison
50	    vs static calibration at matched coverage.'
51	  priority: P1
52	  gpu_budget_hours: 15
53	  deps:
54	  - plan_001
55	- id: plan_006
56	  claim: 2
57	  description: Ablation A1 — CRM without ACI (static CGS calibration, no online adaptation).
58	    Isolates ACI contribu
…[truncated 3117 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "Read",
  "elapsed_ms": 193
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-16T00:39:20.502425+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__list_workers",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__list_workers",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-16T00:39:20.610557+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "ToolSearch",
  "elapsed_ms": 108
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-16T00:39:24.377933+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'RUNNING'}",
  "project": "acr-vla-conformal-refinement",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'RUNNING'}",
    "project": "acr-vla-conformal-refinement",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-16T00:39:24.406707+00:00_

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
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-16T00:39:24.801110+00:00_

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
  "session": "cron:hook:eval-mag-perdof-norm03-object",
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

_source line 76 · 2026-05-16T00:39:27.992720+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-mag-obsonly-norm003-b2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:20:45.606Z\", \"updated_at\": \"2026-05-15T20:37:54.341Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_mag_obsonly_norm003.json\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"225139\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm003-b2.log\", \"submitted_at\": \"2026-05-15T05:20:45.407Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_spatial\", \"data_count\": 10, \"model_name\": \"crm_v3_norm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"libero_spatial\"}, \"pid\": 227426, \"notes\": \"Ghost PID 211962 killed, b2 now running solo on bjb2-40593 cuda:0. PID 227434 confirmed alive (15min uptime, model loaded, eval executing, GPU 6185MiB/24564MiB, 12% util).\", \"metrics\": {\"tasks_done\": 8, \"tasks_total\": 10, \"partial_sr\": {\"between_plate_and_ramekin\": 0.9, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.8, \"on_stove\": 0}, \"server\": \"bjb2-40593\", \"pid\": 227434, \"gpu\": \"cuda:0\", \"process_status\": \"alive\", \"checked_at\": \"2026-05-16T04:40:00\"}}, \"eval-mag-obsonly-norm03-object\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:29:02.155Z\", \"updated_at\": \"2026-05-15T20:37:52.085Z\", \"spec\": {\"hypothesis\": \"Object magnitude sweep: obs_only CRM v3-norm at norm=0.3 on LIBERO object benchmark. Tests degradation a
…[truncated 21677 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 3614
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-16T00:42:06.561878+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 16, \"results\": [{\"exp_id\": \"eval-mag-obsonly-norm003-b2\", \"success\": true, \"actions\": [\"Job still running (pid=227434)\"]}, {\"exp_id\": \"eval-obs-only-object-seed43\", \"success\": true, \"actions\": [\"Job still running (pid=356490)\"]}, {\"exp_id\": \"eval-perdof-object-seed43\", \"success\": true, \"actions\": [\"Job still running (pid=365925)\"]}, {\"exp_id\": \"eval-mag-obsonly-norm03-object\", \"success\": true, \"actions\": [\"Job still running (pid=103028)\"]}, {\"exp_id\": \"eval-mag-obsonly-norm005-object\", \"success\": true, \"actions\": [\"Job still running (pid=101610)\"]}, {\"exp_id\": \"eval-vla-mean-object-seed43\", \"success\": true, \"actions\": [\"Job still running (pid=111709)\"]}, {\"exp_id\": \"eval-scalar-object-seed43\", \"success\": true, \"actions\": [\"Job still running (pid=114664)\"]}, {\"exp_id\": \"eval-mag-obsonly-norm003-object\", \"success\": true, \"actions\": [\"Job still running (pid=121325)\"]}, {\"exp_id\": \"eval-acr-object-v4-default-r2\", \"success\": true, \"actions\": [\"Job still running (pid=390936)\"]}, {\"exp_id\": \"eval-mag-perdof-norm02-object\", \"success\": true, \"actions\": [\"Job still running (pid=127732)\"]}, {\"exp_id\": \"eval-mag-perdof-norm005-object\", \"success\": true, \"actions\": [\"Job still running (pid=109650)\"]}, {\"exp_id\": \"eval-mag-perdof-norm003-object\", \"success\": true, \"actions\": [\"Job still running (pid=105938)\"]}, {\"exp_id\": \"eval-acr-object-obs-only-default\", \"success\": true, \"actions\": [\"Job still running (pid=134103)\"]}, {\"exp_id\": \"eval-obs-only-object-norm02-seed43-r2\", \"success\": true, \"actions\": [\"Job still running (pid=148788)\"]}, {\"exp_id\": \"eval-mag-perdof-norm02-seed43-object-r3\", \"success\": true, \"actions\": [\"Job still running (pid=144504)\"]}, {\"exp_id\": \"eval-mag-perdof-norm03-object-r3\", \"success\": true, \"actions\": [\"Job still running (pid=140759)\"]}]}, \
…[truncated 35 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 162155
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-16T00:42:06.884533+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [], \"count\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 162083
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-16T00:42:12.305545+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'PENDING'}",
  "project": "acr-vla-conformal-refinement",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'PENDING'}",
    "project": "acr-vla-conformal-refinement",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-16T00:42:12.991088+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'ANALYZING'}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'ANALYZING'}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-16T00:42:15.505510+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-mag-obsonly-norm03-b2\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:05:41.192Z\", \"updated_at\": \"2026-05-15T19:11:50.648Z\", \"hypothesis\": \"Magnitude sweep: obs_only CRM v3-norm at norm=0.3 on spatial. Retry of eval-mag-obsonly-norm03 (EXIT_CODE=127). Fills obs_only norm=0.3 gap. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade, strong evidence for obs_only robustness.\", \"parent\": \"eval-mag-obsonly-norm03\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_mag_obsonly_norm03_b2.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"130104\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm03-b2.log\", \"submitted_at\": \"2026-05-15T19:11:50.323Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"failed\", \"notes\": \"Killed: duplicate of eval-mag-obsonly-norm03-r2 on same cuda:0. r2 had 15min more progress. Both wrote same output_file, causing potential corruption.\", \"reproduce\": {\"finished_at\": \"2026-05-15T07:10:36.759Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T07:10:39.645469+00:00\"}]}}}, \"count\": 1, \"total\": 1, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.152}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 3199
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-16T00:42:18.386642+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-obs-only-object-seed43\": {\"status\": \"ANALYZING\", \"created_at\": \"2026-05-15T11:58:46.063Z\", \"updated_at\": \"2026-05-16T00:41:30.930Z\", \"hypothesis\": \"D031: obs_only CRM v3-norm seed=43 on LIBERO object benchmark. Doubles sample size for Fisher exact test. seed=42 shows obs_only 16% vs argmin 8% (+8pp, p≈0.19). Combined 200 trials target p < 0.05.\", \"parent\": \"eval-acr-object-v4-obs-only\", \"metrics\": {\"tasks_done\": 6, \"tasks_total\": 10, \"partial_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0}, \"server\": \"bjb1-18228\", \"pid\": 356495, \"gpu\": \"cuda:2\", \"process_status\": \"alive\", \"checked_at\": \"2026-05-16T04:40:00\"}}}, \"count\": 1, \"total\": 1, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.8052}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 5395
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-16T00:42:22.872443+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'DONE'}",
  "project": "acr-vla-conformal-refinement",
  "limit": "10",
  "fields": "['status', 'conclusion', 'metrics', 'hypothesis']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'DONE'}",
    "project": "acr-vla-conformal-refinement",
    "limit": "10",
    "fields": "['status', 'conclusion', 'metrics', 'hypothesis']"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-16T00:42:25.131534+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-argmin-object-seed43\": {\"status\": \"DONE\", \"hypothesis\": \"D031: argmin baseline (K=10, scalar Euclidean argmin) seed=43 on LIBERO object benchmark. Paired with eval-obs-only-object-seed43 for Fisher exact test. Need both conditions under same seed for valid comparison.\", \"metrics\": {\"overall_success_rate\": 0.17, \"total_successes\": 17, \"total_trials\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.3, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"conclusion\": \"success\"}, \"eval-mag-perdof-norm02-seed43-object-r2\": {\"status\": \"DONE\", \"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm norm=0.2 seed=43. Moved from bjb2-28827:cuda:3 (GPU conflict with obs_only spatial) to cuda:2. Tests perdof norm sensitivity with second seed.\", \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm03\": {\"status\": \"DONE\", \"hypothesis\": \"Magnitude sweep: obs_only CRM v3-norm at norm=0.3 on spatial. Fills obs_only norm=0.3 gap. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade at same norm, strong evidence for obs_only robustness.\", \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm02-object\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm03-b4\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm03-b3\": {\"status\": \"DONE\", \"hypothesis\": \"Retry of eval-mag-obsonly-norm03-b2 (spatial magnitude sweep obs_only norm=0.3). Submitted on bjb2-28827:cuda:2 instead of bjb1-32546:cuda:3 (cuda:3 occupied by P0 obs-only-norm02-seed43-r2). Director approved.\", \"conclusion\": \"killed\"}, \"eval-mag-perdof-norm02-seed43-object\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-perdof-norm03-object-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-ac
…[truncated 281 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-perdof-norm03-object",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 2259
}
```

</details>

---

### Assistant

_source line 85 · 2026-05-16T00:43:52.994015+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- **GPU 白名单强制**：只能用 `get_project_status` 返回的 `execution.gpu_ids`。bjb1-18228 有 4 卡 (cuda:0-3)，bjb1-32546 有 6 卡 (cuda:0-5)，bjb2-28827 有 6 卡 (cuda:0-5)，bjb2-40593 仅 cuda:0
- **submit_training_job 命令必须 bash -c 包裹**：`bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u ..."`。裸 `python -u` 在 tmux 下 PATH 不可靠，已多次 EXIT_CODE=127
- **Kill 前逐参数比对**：曾误 kill norm=0.3 当成 norm=0.03。必须 `ps aux | grep` 完整命令行核对 mode/norm/benchmark/seed/output_file
- **exp_id 命名**：norm 用 `p` 替代小数点（norm0p3 = 0.3），禁止 norm03 歧义写法
- **eval-obs-only-object-seed43 状态异常**：registry 显示 ANALYZING 但 cron 报 process alive (pid=356495)。接手后先核实——可能是 cron 推进状态后进程仍在跑，或 status 被误改

### 2. 🖥️ 基础设施快照
- **bjb1-18228**: 4× RTX 4090, `/root/acr-vla-conformal-refinement`, Python `/root/miniconda3/bin/python`, conda base
- **bjb1-32546**: 6× RTX 4090, 同上路径结构
- **bjb2-28827**: 6× RTX 4090, 同上路径结构
- **bjb2-40593**: 1× RTX 4090 D, 同上。无 .git repo，CRM cache 在旧路径 `/root/autodl-tmp/crm_cache/spatial/`
- **CRM checkpoints**: `/root/autodl-tmp/checkpoints/crm_v3_norm/{obs_only,perdof,scalar_unc}/crm_best.pt`（所有服务器同路径）
- **数据**: `/root/autodl-tmp/libero_data/`，HF cache `/root/autodl-tmp/.hf_cache`
- **活跃进程 (16 RUNNING)**:
  - bjb1-18228: cuda:0 perdof-default-r2 (PID 390936), cuda:1 perdof-seed43 (PID 365930), cuda:2 obs-only-seed43 (PID 356495, ⚠️ ANALYZING 状态)。**cuda:3 可能空闲**（argmin-seed43 已 DONE）
  - bjb1-32546: cuda:0-5 全占（obsonly-norm003-object / vla-mean-seed43 / scalar-seed43 / obsonly-norm02-seed43-r2 / obsonly-default / perdof-norm02-object）
  - bjb2-28827: cuda:0-5 全占（perdof-norm003-object / perdof-norm005-object / perdof-norm03-r3 / perdof-norm02-seed43-r3 / obsonly-norm005-object / obsonly-norm03-object）
  - bjb2-40593: cuda:0 obsonly-norm003-b2 spatial (PID 227426, 8/10 tasks)
- **Worker 池**: 0 active（全部是 cron 监控的 submit_training_job）

### 3. 📊 当前状态
**Phase 3: Paper writing + seed=43 statistical validation + object magnitude sweep**

**Seed=43 六方进度（P0，Fisher exact test 关键）**:
| 方法 | 进度 | partial SR | seed=42 参照 |
|------|------|-----------|-------------|
| VLA-only | ✅ DONE | 12% | 12% |
| argmin | ✅ DONE | **17%** | 12% |
| obs_only 0.1 | 6/10 ⚠️ ANALYZING | 8.3% | 19% |
| perdof | 5/10 | 10% | 11% |
| VLA-mean | 3/10 | 6.7% | 12% |
| scalar | 3/10 | 0% | 9% |

⚠️ argmin seed=43 = 17% (高于 seed=42 的 12%)，obs_only seed=43 partial 8.3% (低于 seed=42 的 19%)。Fisher test 结果取决于最终 10-task 数字。

**Object magnitude sweep（fig3 数据）**: obs_only 和 perdof 各 4 个 norm 点在跑，均 2/10 tasks。加上已有 norm=0.1 数据，完成后可绘制 5 点曲线。

**Default norm ablation**: obs_only-default 和 perdof-default-r2 各 1-2/10，确认 norm≈1.42 catastrophic failure。

**Paper 状态**: Intro ✅ Method ✅ Experiments ✅ Related Work ✅ Discussion/Conclusion ✅ 引用审计 ✅。待做：fig1 WIP / fig2 / fig3 + seed=43 结果补入 + Abstract 最终版。

**等待中**: 无 Worker 回调。16 个 cron 监控 RUNNING 实验。1 个 PENDING（eval-mag-obsonly-norm03-b2 spatial，已有替代 norm=0.3 数据 36%，可能无需再跑）。

### 4. 📋 待办（条件触发式）
- **eval-obs-only-object-seed43 完成 (或状态修正)** → spawn Worker 提取 10-task SR → 与 argmin seed43 (17%) 做 Fisher exact test → 若 pooled p<0.05 claim 成立；p=0.05-0.10 加 seed=44；p>0.10 调整 claim 强度
- **seed=43 六方全部 DONE** → spawn Worker 生成 seed=42+43 combined table + Fisher exact test + bootstrap CI → 更新 paper Experiments section + Abstract
- **Object magnitude sweep 全 10/10** → spawn Worker 绘制 fig3 norm sensitivity curve (obs_only vs perdof, 5 点) → register_artifact
- **Default norm ablation 完成** → 确认 0% catastrophic failure → 补入 paper magnitude section
- **bjb1-18228:cuda:3 确认空闲** → 立即提交下一个排队实验（优先 VLA-mean seed43 或 obs_only norm=0.2 spatial，按优先级选）
- **eval-mag-obsonly-norm03-b2 PENDING** → 评估是否仍需要（spatial norm=0.3 已有 36% 数据）；如不需要则 kill+DONE
- **所有数据就绪后** → fig1 pipeline diagram + fig2 per-task breakdown + fig3 magnitude curve → 论文定稿 → Abstract 最终版

### 5. 🎯 战略上下文
- **唯一存活 claim**: obs_only CRM 在 object benchmark 上 +7-10pp over argmin。Spatial 全死（所有变体 ±1pp of argmin）。论文以 object 为主故事，spatial 作 generalization/robustness。
- **CoRL DDL**: abstract ~May 26 (10天), full paper ~Jun 2 (17天)。时间充裕但 seed=43 统计结果是 make-or-break gate。
- **最大风险**: argmin seed=43=17% 而 obs_only seed=43 partial 仅 8.3%。如果最终 obs_only seed=43 < argmin seed=43，pooled Fisher test 可能不显著。**这是目前唯一的项目级风险**。应对方案已在 paper_framing.md: p>0.10 调整 claim 为 "suggestive evidence"。
- **决策链**: D027(perdof=argmin 已死) → D029/D030(obs_only 唯一存活) → D031(seed=43 doubling) → D032(magnitude narrative) → D033(+7pp 超门槛) → D034(ReconVLA 重定位)
- **易错点**:
  - 不要把 spatial 结果 (35% obs_only) 和 object 结果 (19% obs_only) 混为一谈——claim 只在 object 上成立
  - 不要把 partial SR (进行中) 当作 FINAL 结果汇报
  - obs_only norm=0.03 spatial (bjb2-40593, 8/10) 快完了——这个是 magnitude sweep 的极端点，spatial 44.3%@7tasks 可能因最后 2 tasks 下降
  - eval-mag-obsonly-norm03-b2 PENDING 是旧实验重试，spatial norm=0.3 已有 36% 数据(10t ✅)，大概率可以取消
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval-mag-perdof-norm03-object"
}
```

</details>

---
