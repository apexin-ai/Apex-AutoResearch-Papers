# cron hook eval pi05 attn k075 long seed43 strict cqa1 20260529T072106 745292

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 16
- **Recorded user turns:** 2
- **Tool calls:** 6
- **Original source:** `logs/chats/archive/cron_hook_eval_pi05_attn_k075_long_seed43_strict_cqa1_20260529T072106_745292.jsonl`
- **Structured JSON:** [`933e7973fb22fdbd4f54.json`](../../sessions/93/933e7973fb22fdbd4f54.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

14 recorded events

### User

_source line 1 · 2026-05-28T14:50:30.805464+00:00_

[HANDOFF] 你是 Main Agent，这是 Loop #16。

## 上一轮交接 (task_context)

### 1. 🔴 硬约束 / 红线
- **CoRL 2026 paper deadline: May 29（明天）。** 一切以 submission 为优先，不要启动新实验。
- GPU 白名单: cuda:0, cuda:1, cuda:2, cuda:3。4 台服务器: westd-27271, cqa1-33015, westd-41074, westd-38929。
- 论文数据已锁定：5-seed 90/90 cell 零缺失，build_5seed_tables.py 交叉验证通过。**不要修改任何已验证的 metrics 数据。**
- 论文 error bar 标准: sample std (n-1)，统一百分比格式 (D301)。
- Registry 中 96 个 PREPARING 实验全是历史残留（早期 debug/abandoned/superseded），不要尝试恢复或提交它们。
- CoRL 2026 要求 Limitations section 计入 8-page 限制内。

### 2. 🖥️ 基础设施快照
- **服务器**: westd-27271, cqa1-33015 (root), westd-41074 (root), westd-38929 (root)
- **工作目录**: /root/autodl-tmp/importance_margin_vla_compress（所有服务器）
- **GPU**: 14 张，分布在 4 台服务器，cuda:0-3 为项目配额
- **活跃进程**: 无。0 RUNNING 实验，0 active crons，0 running workers
- **cqa1** 支持 attention pruning；**westd-41074** 支持 attention pruning；**westd-27271** 历史上代码未同步（仅 none/random/l2norm）；**westd-38929** attention 支持未确认
- **评估耗时**: π0.5 ~2.5h/run, OpenVLA ~8.3h/run

### 3. 📊 当前状态
所有实验数据收集完毕，项目处于 **submission-ready** 状态：
- ✅ π0.5 Cliff Curve 18/18, OpenVLA Long Curve 18/18, Crossover table 16/16
- ✅ Importance Margin Inverted-U 6/6 全闭合, Attn cliff+plateau 全 6 点闭合
- ✅ 5-seed 90/90 cell 零缺失，数据验证通过 (May 28)
- ✅ Abstract 已提交 (May 26), Narrative 定稿 (D276)
- ✅ Figures 已在前序轮次生成完毕
- **Registry 总计**: 890 实验 (575 success / 110 negative / 118 failed)
- **无任何 RUNNING 实验、无 active worker、无 active cron**
- w38 有 s47 bonus seeds（revision 备用，非 deadline 必须）

唯一待办: **Paper Agent 最终 submission 准备 → May 29**

### 4. 📋 待办（条件触发式）
- Director 指令 "开始 submission 准备" → spawn Paper Agent worker，生成最终 LaTeX，检查 Limitations section（CoRL 硬约束），格式校验，生成 submission PDF
- Director 要求补数据/re-run → 查 ROADMAP 确认是否真有缺口（当前 90/90 完整，大概率不需要）
- 任何新实验请求 → push back："deadline 明天，数据已锁定，建议 revision 阶段再补"
- w38 bonus seed (s47) 完成回调 → 更新 registry，不影响 submission（revision 备用）

### 5. 🎯 战略上下文
- **核心框架**: 2-axis framework (D171) — Axis 1: Token Coupling (token-independent vs token-entangling connectors), Axis 2: Task Complexity (simple vs complex suites)。替代了早期 4-class taxonomy。
- **论文 title**: "Why Token Pruning Crashes Some Robot Policies but Not Others: The Role of Vision Connectors in VLA Token Compressibility"
- **关键数据锚点**: π0.5 Long 表格（ROADMAP 中完整 6×3 表）；Importance margin peak 在 k=0.9 (+46.9pp)；crossover 在 k=0.7 (-1.4pp)
- **易错点**: 96 个 PREPARING 实验看起来很多但都是历史垃圾——不要被它们分心，不要试图清理或恢复。项目的数据已完整。
- **易错点 2**: paper_framing.md 非常长 (~52K chars)，读取时注意 max_chars=0 才能拿完整内容。
- **决策链**: D276 narrative 定稿 → D291 Inverted-U 闭合 → D301 error bar 标准确定 → 数据验证通过 → submission ready

## 项目硬约束 (memory.md 节选)

## 服务器能力备忘

- **cqa1-33015**: 支持 attention pruning mode（已验证）
- **westd-41074**: 支持 attention pruning mode（已验证）
- **westd-27271**: ⚠️ 代码未同步，仅支持 none/random/l2norm（Worker 正在修复）
- **westd-38929**: attention 支持未确认，待 w27 修复后一并验证

## 评估耗时约束 (2026-05-28)

- **π0.5**: LIBERO-10 50eps × 10tasks ≈ 2.5h
- **OpenVLA**: LIBERO-10 50eps × 10tasks ≈ 8.3h (~1.0 eps/min，比 π0.5 慢 ~3.3x)
- OV 评估提交时 timeout_hours 必须 ≥ 9h，否则会被 EXIT_CODE=124 kill

## 可查的历史
前 99 轮 handoff 在 `task_context/history/agent/loop_*.md`，如有疑问可 Read 回查。
完整聊天归档可用 `recall_session_history("关键词")` 搜索。

## 第一个动作要求
1. 用 `read_registry` 确认当前 RUNNING/PREPARING 实验状态（防止幻觉记忆过时状态）
2. 回复一句话确认你看到了上面的硬约束 + 当前活跃实验，再开始任何工具调用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:eval_pi05_attn_k075_long_seed43_strict_cqa1",
  "source": "system:ralph_loop"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-28T14:50:42.955567+00:00_

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
  "session": "cron:hook:eval_pi05_attn_k075_long_seed43_strict_cqa1",
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

_source line 3 · 2026-05-28T14:50:43.006165+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_pi05_attn_k075_long_seed43_strict_cqa1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-28T14:50:45.944318+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'RUNNING'}",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_pi05_attn_k075_long_seed43_strict_cqa1",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'RUNNING'}",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-28T14:50:46.446482+00:00_

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
  "session": "cron:hook:eval_pi05_attn_k075_long_seed43_strict_cqa1",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-28T14:50:46.898937+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "importance_margin_vla_compress",
  "file": "report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_pi05_attn_k075_long_seed43_strict_cqa1",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "importance_margin_vla_compress",
    "file": "report.md"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-28T14:50:46.999775+00:00_

called mcp__agent-ml-research__read_roadmap

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_roadmap</summary>

```json
{
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_pi05_attn_k075_long_seed43_strict_cqa1",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-28T14:50:48.355301+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.3607}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_pi05_attn_k075_long_seed43_strict_cqa1",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 2410
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-28T14:50:48.405961+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 0, \"results\": []}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_pi05_attn_k075_long_seed43_strict_cqa1",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 1959
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-28T14:50:48.406645+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/report.md\", \"content\": \"# Handover — 2026-05-28\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- eval_pi05_l2norm_k07_long_seed46_strict_w38_v2: π0.5 L2norm k=0.7 Long strict seed46 — v1 被 GPU OOM kill (w38:cuda:1 三进程共享)。重试部署到独占 GPU。5th seed for crossover point, 4-seed mean=63.5±1.57pp（准备中）\\n- eval_openvla_random_k095_goal_seed42_v3: OV Random k=0.95 Goal v3 retry on cqa1 — v2 cqa1 transformers 版本问题, v3 w41 模型文件缺失。cqa1 环境已修复，重新部署。Goal Random cliff curve 顶端数据点（准备中）\\n- …另有 94 项\\n\\n## 近期结论\\n- **eval_pi05_l2norm_k05_long_seed47_w38** (killed): π0.5 L2norm k=0.5 Long seed47 — 6th seed bonus data，high variance 点 (s42-s46 std ~1.8pp)。填充 w38 空闲 GPU，不在 CoRL deadline 内但可用于 revision\\n\\n## 趋势\\n成功 575 / 负向 110 / 失败 118 / 共 890\\ntotal_episodes: 500 →（近 3 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\ncqa1-33015: 无 GPU 信息\\nwestd-27271: 无 GPU 信息\\nwestd-38929: 无 GPU 信息\\nwestd-41074: 无 GPU 信息\\n\\n## 告警\\n- eval_acis_k05_supplement_200eps: 训练失败 — unknown\\n- eval_e5_xvla_attn_last_goal_k03: 已被终止 — unknown\\n- eval_e5_xvla_attn_mean_goal_k03: 已被终止 — unknown\\n- eval_k07_bypass_v2: 训练失败 — unknown\\n- eval_official_smolvla_prune_k05_spatial: 训练失败 — unknown\\n- eval_official_smolvla_pruning: 训练失败 — unknown\\n- eval_oft_baseline_k10: 训练失败 — unknown\\n- eval_oft_baseline_object_seed42: 已被终止 — unknown\\n- eval_oft_baseline_object_seed42_v2: 训练失败 — unknown\\n- eval_openvla_attn_k05_object_seed42_v2: 训练失败 — unknown\\n- eval_openvla_attn_k085_goal_seed42: 训练失败 — unknown\\n- eval_openvla_attn_k085_goal_seed42_v2: 已被终止 — unknown\\n- eval_openvla_attn_k085_long_seed42: 训练失败 — unknown\\n- eval_openvla_attn_k085_long_seed42_v2: 已被终止 — unknown\\n- eval_openvla_attn_k085_long_seed42_v3: 已被终止 — unknown\\n- eval_openvla_attn_k085_spatial_seed42: 训练失败 — unknown\\n- eval_openvla_attn_k085_spatial_seed4
…[truncated 5902 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_pi05_attn_k075_long_seed43_strict_cqa1",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1507
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-28T14:50:48.457431+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/ROADMAP.md\", \"content\": \"# importance_margin_vla_compress — Research Dashboard\\n\\n> 最后更新: 2026-05-28 14:44 UTC | 更新原因: 数据验证通过，ROADMAP 精简为 submission-ready 状态\\n\\n> 详见 paper_framing.md。\\n\\n## 核心方向\\nVLA vision token compressibility: **scoring method × connector × task 三维交互**。5+ 模型 × 4 LIBERO suites。\\n\\n## 当前阶段\\n✅ **π0.5 Cliff Curve 18/18 完成**\\n✅ **OpenVLA Long Curve 18/18 完成** (D288)\\n✅ **Crossover table 16/16 完成**\\n✅ **Abstract 已提交** (May 26)\\n✅ **Narrative 定稿** (D276)\\n✅ **Importance Margin Inverted-U 6/6 全闭合** (D291)\\n✅ **Attn cliff+plateau 全 6 点闭合** (D290)\\n✅ **5-seed 90/90 cell 零缺失，数据验证通过** (May 28)\\n✅ **Figures 已在前序轮次生成完毕**\\n\\n## Deadlines\\n- **CoRL 2026 Paper**: May 29\\n\\n## 🏁 π0.5 LIBERO-Long 最终汇总表 (5-seed, sample std n-1)\\n\\n| k | L2norm (mean±std) | n | Random (mean±std) | n | Attn (mean±std) | n | Margin L2-Rand |\\n|---|-------------------|---|-------------------|---|-----------------|---|----------------|\\n| 0.95 | **86.8±0.8** | 5 | **61.2±0.7** | 5 | **77.3±1.2** | 5 | **+25.6pp** |\\n| 0.9 | **80.4±0.5** | 5 | **33.6±1.2** | 5 | **64.2±1.0** | 5 | **+46.9pp** ⭐peak |\\n| 0.85 | **78.1±1.0** | 5 | **44.9±1.3** | 5 | **50.8±1.3** | 5 | **+33.2pp** |\\n| 0.75 | **70.6±2.7** | 5 | **63.0±1.7** | 5 | **51.4±1.2** | 5 | **+7.6pp** |\\n| 0.7 | **63.2±1.5** | 5 | **64.6±1.8** | 5 | **53.0±1.1** | 5 | **-1.4pp** 🔄cross |\\n| 0.5 | **51.7±1.5** | 5 | **50.4±0.6** | 5 | **49.4±1.5** | 5 | **+1.3pp** ≈0 |\\n\\n数据来源: s42-s43 硬编码验证值(42cell) + s44-s46 registry提取(47cell) + build_5seed_tables.py 交叉验证。\\n\\n## 待处理\\n- [x] 5-seed 数据验证 (build_5seed_tables.py) — ✅ 90/90 一致\\n- [x] Figures 生成 — ✅ 前序轮次已完成\\n- [ ] Paper Agent 最终 submission 准备 → May 29\\n\\n## GPU 分配\\n14 张 GPU (4 servers)。实验硬截止已过，仅 w38 跑 s47 bonus seeds（revision 备用）。\\n\\n## 数据整合注意事项（全部已处理）\\n- [x] Attn k=0.75 seed43: cqa1=52.0%\\n- [x] A
…[truncated 1585 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_pi05_attn_k075_long_seed43_strict_cqa1",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 1457
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-28T14:51:08.639306+00:00_

called mcp__agent-ml-research__main_agent_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__main_agent_post_to_director</summary>

```json
{
  "text": "[资源] GPU 0/14 active | Worker 0 | 磁盘: 未查（无活跃任务）\n\n**Loop #16 Session Start — Submission Day**\n\n状态确认：\n- 0 RUNNING 实验，0 active crons，0 workers\n- Registry 890 实验，5-seed 90/90 零缺失，数据验证通过\n- ROADMAP 唯一待办：Paper Agent 最终 submission 准备\n\n**CoRL 2026 deadline 明天 May 29。** 数据已锁定，等待 Director 指令启动 submission 准备（spawn Paper Agent worker 生成最终 LaTeX、检查 Limitations section、格式校验、生成 submission PDF）。\n\n请指示何时开始 submission 流程。",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_pi05_attn_k075_long_seed43_strict_cqa1",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "tool_args": {
    "text": "[资源] GPU 0/14 active | Worker 0 | 磁盘: 未查（无活跃任务）\n\n**Loop #16 Session Start — Submission Day**\n\n状态确认：\n- 0 RUNNING 实验，0 active crons，0 workers\n- Registry 890 实验，5-seed 90/90 零缺失，数据验证通过\n- ROADMAP 唯一待办：Paper Agent 最终 submission 准备\n\n**CoRL 2026 deadline 明天 May 29。** 数据已锁定，等待 Director 指令启动 submission 准备（spawn Paper Agent worker 生成最终 LaTeX、检查 Limitations section、格式校验、生成 submission PDF）。\n\n请指示何时开始 submission 流程。",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-28T14:51:12.352647+00:00_

{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_6ea0e93e255655758819bea2ab1f224d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_pi05_attn_k075_long_seed43_strict_cqa1",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "elapsed_ms": 3713
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-28T14:51:15.138280+00:00_

初始化完成。当前状态：submission-ready，0 活跃任务。已向 Director 汇报并请求 submission 准备指令。等待 Director 回复。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval_pi05_attn_k075_long_seed43_strict_cqa1"
}
```

</details>

---

## Round 2

2 recorded events

### User

_source line 15 · 2026-05-29T07:20:30.190968+00:00_

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
  "session": "cron:hook:eval_pi05_attn_k075_long_seed43_strict_cqa1",
  "source": "system:ralph_loop"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-29T07:21:06.725709+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- **CoRL 2026 deadline: May 29（今天）。** 一切以 submission 为最高优先级，不启动新实验。
- GPU 白名单: cuda:0, cuda:1, cuda:2, cuda:3。不得使用白名单外 GPU。
- 论文数据已锁定：5-seed 90/90 cell 零缺失，build_5seed_tables.py 交叉验证通过。**不得修改任何已验证的 metrics 数据。**
- Error bar 标准: sample std (n-1)，统一百分比格式 (D301)。
- Registry 中 96 个 PREPARING 实验全是历史残留，不要尝试恢复或提交。
- CoRL 2026 要求 Limitations section 计入 8-page 限制内。
- paper_framing.md ~52K chars，读取时必须 max_chars=0。

### 2. 🖥️ 基础设施快照
- **服务器**: westd-27271, cqa1-33015 (root), westd-41074 (root), westd-38929 (root)
- **工作目录**: /root/autodl-tmp/importance_margin_vla_compress（所有服务器）
- **GPU**: 14 张分布在 4 台服务器，cuda:0-3 为项目配额
- **活跃进程**: 无。0 RUNNING 实验，0 active crons，0 running workers
- **服务器能力**: cqa1 + westd-41074 支持 attention pruning；westd-27271 仅 none/random/l2norm；westd-38929 attention 未确认
- **评估耗时**: π0.5 ~2.5h/run, OpenVLA ~8.3h/run

### 3. 📊 当前状态
Loop #16 刚完成 session-start 初始化，已向 Director 汇报 submission-ready 状态并请求 submission 指令。**尚未收到 Director 回复。**
- Registry: 890 实验 (575 success / 110 negative / 118 failed)，0 RUNNING
- 所有数据收集完毕：π0.5 Cliff 18/18, OV Long 18/18, Crossover 16/16, Inverted-U 6/6, Attn cliff+plateau 6/6
- Abstract 已提交 (May 26), Narrative 定稿 (D276), Figures 已生成
- w38 有 s47 bonus seeds（revision 备用，非 deadline 必须）
- 无等待中的 Worker 回调 / Cron / Director 决策（除刚发的汇报）

### 4. 📋 待办（条件触发式）
- Director 指令"开始 submission 准备" → spawn Paper Agent worker：生成最终 LaTeX，检查 Limitations section（CoRL 硬约束），格式校验，生成 submission PDF
- Director 要求补数据/re-run → push back："deadline 今天，数据已锁定，建议 revision 阶段再补"（90/90 完整，大概率不需要）
- w38 s47 bonus seed 完成回调 → 更新 registry，不影响 submission（revision 备用）
- 任何新实验请求 → push back 到 revision 阶段

### 5. 🎯 战略上下文
- **核心框架**: 2-axis framework (D171) — Axis 1: Token Coupling (token-independent vs token-entangling), Axis 2: Task Complexity (simple vs complex suites)
- **论文 title**: "Why Token Pruning Crashes Some Robot Policies but Not Others: The Role of Vision Connectors in VLA Token Compressibility"
- **关键数据锚点**: π0.5 Long 表格完整 6×3；Importance margin peak 在 k=0.9 (+46.9pp)；crossover 在 k=0.7 (-1.4pp)
- **决策链**: D276 narrative 定稿 → D291 Inverted-U 闭合 → D301 error bar 标准确定 → 数据验证通过 → submission ready
- **易错点**: 96 个 PREPARING 实验看起来很多但都是历史垃圾——不要被它们分心。项目数据已完整，唯一任务是 submission。
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval_pi05_attn_k075_long_seed43_strict_cqa1"
}
```

</details>

---
