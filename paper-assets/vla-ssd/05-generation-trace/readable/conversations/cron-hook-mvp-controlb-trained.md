# cron hook mvp controlb trained

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 62
- **Recorded user turns:** 1
- **Tool calls:** 30
- **Original source:** `logs/chats/cron_hook_mvp_controlb_trained.jsonl`
- **Structured JSON:** [`43a1b2efc9f2a25f0f71.json`](../../sessions/43/43a1b2efc9f2a25f0f71.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

62 recorded events

### User

_source line 1 · 2026-05-16T02:32:42.298442+00:00_

[HANDOFF] 你是 Main Agent，这是 Loop #6。

## 上一轮交接 (task_context)

### 1. 🔴 硬约束 / 红线
- GPU 白名单：仅 `cuda:0` 和 `cuda:1`（westd-19183）
- 服务器 **无外网**：所有 HF/AutoProcessor 操作必须 `local_files_only=True`，不能 pip install / git clone
- westd 是 **SeetaCloud**（非 AutoDL），不适用 `network_turbo` / ModelScope 等 AutoDL 方案
- 统一 action probe 超参已锁定：50ep/patience5/lr1e-3/hidden256/seed42, MLP input→256→7, predict a_{t+1}。任何新 probe 必须用此配置，否则 R² 不可比（之前 CLIP 100ep 导致虚高 0.814 vs 真实 0.587 的事故）
- 论文数值只能来自 registry，不能凭记忆编造
- CoRL Abstract DDL = 5/26，Paper DDL = 5/29，**不允许讨论降级 venue**

### 2. 🖥️ 基础设施快照
- **服务器**：westd-19183，工作目录 `/root/vla-ssd`
- **Python**：`/root/miniconda3/bin/python`（conda base env，不是 venv）
- **模型 checkpoint**：`/root/autodl-tmp/vla-ssd/`（大文件存储）
- **W&B**：项目中无 W&B 训练（全部是离线 probe/RSA 分析脚本）
- **HF cache**：服务器无网，模型已预下载到本地
- **活跃进程**：无 RUNNING 实验，0 active crons
- **活跃 Worker**：`worker_ssh_patch-mean-probe_20260516T022703`（status=running，任务 ssh:patch-mean-probe）——可能正在修补 image_mean probe 相关代码，接手后检查其完成状态

### 3. 📊 当前状态
**所有 45 个实验均 DONE**（31 success / 7 negative / 7 killed）。无 RUNNING/PREPARING 实验，0 active crons。

刚完成的关键里程碑：
- `unified_action_probe`（success）：统一超参重跑所有 vision encoder，修正了之前 CLIP R² 虚高问题。发现 geometric-functional dissociation 比预期更极端
- `plan_012_clip_vit_control`（success）：CLIP ViT-L/14 RSA=0.557 确认 VL pretraining 通用性
- `plan_008_random_inst_control`（success）：四种 instruction 条件 RSA 完全收敛，instruction content invariance 证据闭合
- `plan_009_cka_verification`（success）：CKA 部分验证 RSA，发现指标依赖性

**paper_framing.md 三条 Claim 已定稿**，所有 P0 实验证据链完整。

等待中：
- 1 个 running worker（patch-mean-probe）未回调
- ROADMAP 说"re-dream + Paper Agent Full Draft"是下一步，D035 决策已批准并行启动

### 4. 📋 待办（条件触发式）
- `worker_ssh_patch-mean-probe` 回调完成 → 检查产出，更新 registry/report.md
- 上述 worker 完成 → 立即启动 Paper Agent Full Draft（D035 已批准，不需要额外审批）
- Paper Agent 启动 → 按 paper_framing.md 三条 Claim + Story Spine 写作，同时可并行 plan_010 LIBERO-Spatial（P2 优先级）
- 如需 re-dream → dream 验证新 framing 是否达 acceptance threshold（D030 记录上次 dream 结果为 borderline reject）
- Paper 写作中发现数值空缺 → 查 registry 补充，不要编造

### 5. 🎯 战略上下文
**核心结论链**：D027 Instruction Ablation FAIL → Option A2 锁定 → D028 SigLIP smoking gun PASS → D029 聚合伪影排除 → D031 Redistribution framing → D032 Option A 确认 → D033 Geometric-Functional Dissociation → D034 Training-Dependent Redistribution → D036 统一超参修正（dissociation 更极端）

**三条 Claim 总结**：
1. Vision encoder 是 action info 源头，但 geometric alignment (RSA) 与 predictive capacity (R²) **方向相反**——VL pretraining 给几何不给功能
2. LLM 降解分布式表征但通过 training-dependent attention 将信号 concentrate 到 readout token
3. Training = routing（readout concentration），not creating（distributed structure invariant）

**最容易判断错的事**：
- **不要混淆两组 probe 数据**：5-model 对比用 `unified_action_probe` 数字；trained/untrained 对比用 `p0_functional_probe_v2` 数字。两组绝对值不同（超参/数据处理差异），但组内排序一致
- **聚合口径依赖**：image_mean 下 Projector > LLM；last_preaction 下 LLM > Projector。主文用 image_mean（公平），last_preaction 放 supplementary。必须在论文中讨论
- **D030 dream 结果是 borderline reject**——re-dream 时注意新 framing（geometric-functional dissociation）是否足够提升 novelty score
- **CLIP R² < DINO 是反直觉但真实的**——统一超参后确认，不要怀疑数据
- Projector vs trained CKA gap 被压缩（RSA 下显著，CKA 下 ≈），论文措辞不能说 projector "dominance" 是 metric-independent 的

## 项目硬约束 (memory.md 节选)

## 技术约束

- Untrained model: from_config() 重新初始化 LLM（6.74B random），保留 SigLIP（0.80B）
- D017: 统一用 LIBERO-10 fine-tuned checkpoint（LIBERO-Goal 是 OOD 测试）
- Token 聚合：Primary = last pre-action token
- 存储：根分区 ~30GB，大文件在 /root/autodl-tmp/vla-ssd/
- **服务器无外网**：AutoProcessor/HF 操作必须 `local_files_only=True`
- **westd 是 SeetaCloud（非 AutoDL）**，不适用 network_turbo/ModelScope 等 AutoDL 专用方案
- **统一 action probe 超参**：50ep/patience5/lr1e-3/hidden256/seed42, MLP input→256→7

## 可查的历史
前 34 轮 handoff 在 `task_context/history/agent/loop_*.md`，如有疑问可 Read 回查。
完整聊天归档可用 `recall_session_history("关键词")` 搜索。

## 第一个动作要求
1. 用 `read_registry` 确认当前 RUNNING/PREPARING 实验状态（防止幻觉记忆过时状态）
2. 回复一句话确认你看到了上面的硬约束 + 当前活跃实验，再开始任何工具调用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:mvp_controlb_trained",
  "source": "system:ralph_loop"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-16T02:32:54.446988+00:00_

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
  "session": "cron:hook:mvp_controlb_trained",
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

_source line 3 · 2026-05-16T02:32:54.598071+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "ToolSearch",
  "elapsed_ms": 151
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-16T02:32:57.359232+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "vla-ssd",
  "filters": "{'status': 'RUNNING'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "vla-ssd",
    "filters": "{'status': 'RUNNING'}"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-16T02:32:57.814387+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1828}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 455
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-16T02:32:57.814788+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "vla-ssd",
  "filters": "{'status': 'PREPARING'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "vla-ssd",
    "filters": "{'status': 'PREPARING'}"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T02:32:58.317323+00:00_

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
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T02:32:58.317771+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1693}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 502
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-16T02:32:58.870135+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 0, \"results\": []}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 552
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-16T02:32:58.921228+00:00_

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
  "session": "cron:hook:mvp_controlb_trained",
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

_source line 11 · 2026-05-16T02:32:58.921746+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/report.md\", \"content\": \"# Handover — 2026-05-16\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **unified_action_probe** (success): Unified hyperparameter action probe (50ep/patience5/seed42) across all vision encoders on LIBERO-Goal. Resolves cross-experiment R² incomparability caused by differing probe configs. Tests geometric-functional dissociation: does VL pretraining RSA advantage translate to R² advantage?\\n- **plan_012_clip_vit_control** (success): —\\n  [rsa_clip_results](/api/workspace-files/projects/vla-ssd/artifacts/plan_012_clip_vit_control/data/rsa_clip_results.txt) | [action_probe_clip_results](/api/workspace-files/projects/vla-ssd/artifacts/plan_012_clip_vit_control/data/action_probe_clip_summary.txt) | [unified_action_probe_results](/api/workspace-files/projects/vla-ssd/artifacts/plan_012_clip_vit_control/data/unified_action_probe.py)\\n- **lg_instruction_ablation** (killed): D021 Exp-1: Instruction Ablation. Extract LIBERO-Goal features with empty instruction (trained + untrained VLA), then run RSA. If instruction pathway is the source of action-relevant structure, RSA should collapse from ρ≈0.49 to <0.15. PASS: ρ<0.15; PARTIAL: 0.15<ρ<0.30; FAIL: ρ≥0.30.\\n\\n## 趋势\\n成功 31 / 负向 7 / 失败 0 / 共 46\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-19183: 无 GPU 信息\\n\\n## 告警\\n- mvp2_action_probe: 已被终止 — unknown\\n- lg_extract_trained_r2: 已被终止 — unknown\\n- lg_extract_untrained_r2: 已被终止 — unknown\\n- lg_extract_trained_r1: 已被终止 — unknown\\n- lg_extract_untrained_r1: 已被终止 — unknown\\n- lg_shuffled_token_control: 已被终止 — unknown\\n- lg_instruction_ablation: 已被终止 — unknown\\n- lg_output_head_analysis: 已被终止 — unknown\\n\", \"total_chars\": 1621, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-16T02:32:58.921988+00:00_

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
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-16T02:32:59.023261+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/ROADMAP.md\", \"content\": \"# vla-ssd — Research Dashboard\\n\\n> 最后更新: 2026-05-16 00:14 UTC | 更新原因: Sync with D033/D034, CKA results, plan_008 running, updated Claims\\n\\n## 核心方向\\nVLA 中 action-relevant 表征的来源与 LLM 的 redistribution 机制。三层发现：(1) Vision encoder 是 action info 的通用源头，VL pretraining 赋予 geometric alignment 而非额外 predictive content；(2) LLM 降解分布式 image token 几何结构（RSA）但保留全局结构（CKA），通过训练依赖的 attention 将信号 concentrate 到 readout token；(3) Training 教会 routing（readout concentration），而非 creating new knowledge（distributed structure invariant）。详见 paper_framing.md。\\n\\n## 当前阶段\\n**Research phase, post-D034**。三条 Claim 完整成型，所有 P0 实验完成。等待：(1) untrained vs trained last_preaction bootstrap CI（已派 Agent）；(2) plan_008 random instruction control（RUNNING）。两者完成后 re-dream 验证新 framing，达标则启动 Paper Agent。\\n\\n## 已完成核心实验\\n- ✅ plan_001-007: RSA 组件分解 + 2×2 matrix + per-layer curve + instruction ablation\\n- ✅ plan_011: Functional action probe — Proj R²=0.706 > LLM img_mean 0.683 (p=0.001); readout 0.731 > Proj (p=0.001)\\n- ✅ plan_009: CKA verification — ordering reversal vs RSA (partial). RSA-CKA dissociation 成为新 finding\\n- ✅ D033: DINO R²=0.712 ≈ Projector 0.706 (p=0.22) — geometric-functional dissociation\\n- ✅ D034: Untrained readout R²=0.686 < projector 0.706 — redistribution is training-dependent\\n- ✅ Aggregation robustness: image_mean RSA 0.501 vs SigLIP 0.615, gap=0.114\\n- ✅ Bootstrap CI: training effect on image_mean CI includes 0, distributed structure invariant\\n\\n## 近期任务\\n- [ ] Untrained vs trained last_preaction bootstrap CI（Agent 已派，分钟级）\\n- [ ] plan_008 random instruction control 结果分析（RUNNING，等完成）\\n- [ ] Re-dream with updated framing（上述两项完成后立即触发）\\n- [ ] Paper Agent Full Draft（re-dream 达标后启动）\\n- [ ] plan_012 CLIP-ViT control（P1，Paper Agent 启动后并行）\\n\\n## GPU 预算\\nwestd-19183: 2× GPU（plan_008 占用中）\\n剩余预算: ~7 GPU·h\\n\\n## 关键里程碑\\n| 日期 | 事件 |\\n|
…[truncated 1853 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 101
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-16T02:33:09.524765+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__get_worker_status,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__read_experiment_plan_with_status",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__get_worker_status,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__read_experiment_plan_with_status",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-16T02:33:09.525143+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-16T02:33:12.535807+00:00_

called mcp__agent-ml-research__list_workers

<details open><summary>🔧 Tool call — mcp__agent-ml-research__list_workers</summary>

```json
{
  "project": "vla-ssd",
  "status": "running"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__list_workers",
  "tool_args": {
    "project": "vla-ssd",
    "status": "running"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-16T02:33:12.987813+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [{\"worker_id\": \"worker_ssh_patch-mean-probe_20260516T022703\", \"task_type\": \"ssh:patch-mean-probe\", \"project\": \"vla-ssd\", \"status\": \"running\", \"started_at\": \"2026-05-16T02:27:04.067388+00:00\", \"ended_at\": null}], \"count\": 1}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 452
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-16T02:33:13.290088+00:00_

called mcp__agent-ml-research__list_workers

<details open><summary>🔧 Tool call — mcp__agent-ml-research__list_workers</summary>

```json
{
  "project": "vla-ssd",
  "status": "done",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__list_workers",
  "tool_args": {
    "project": "vla-ssd",
    "status": "done",
    "limit": "5"
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T02:33:13.340717+00:00_

called mcp__agent-ml-research__read_experiment_plan_with_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_experiment_plan_with_status</summary>

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
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__read_experiment_plan_with_status",
  "tool_args": {
    "project": "vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T02:33:13.493289+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [{\"worker_id\": \"worker_ssh_unified-action-probe_20260516T020715\", \"task_type\": \"ssh:unified-action-probe\", \"project\": \"vla-ssd\", \"status\": \"done\", \"started_at\": \"2026-05-16T02:07:15.319637+00:00\", \"ended_at\": \"2026-05-16T02:12:33.089843+00:00\"}, {\"worker_id\": \"worker_ssh_check-probe-target_20260516T021626\", \"task_type\": \"ssh:check-probe-target\", \"project\": \"vla-ssd\", \"status\": \"done\", \"started_at\": \"2026-05-16T02:16:26.163365+00:00\", \"ended_at\": \"2026-05-16T02:20:03.379193+00:00\"}, {\"worker_id\": \"worker_paper_writing_experiments_20260516T021635\", \"task_type\": \"paper_writing:experiments\", \"project\": \"vla-ssd\", \"status\": \"done\", \"started_at\": \"2026-05-16T02:16:35.914061+00:00\", \"ended_at\": \"2026-05-16T02:23:23.728486+00:00\"}, {\"worker_id\": \"worker_paper_writing_method_20260516T022801\", \"task_type\": \"paper_writing:method\", \"project\": \"vla-ssd\", \"status\": \"done\", \"started_at\": \"2026-05-16T02:28:01.818163+00:00\", \"ended_at\": \"2026-05-16T02:29:29.179014+00:00\"}, {\"worker_id\": \"worker_paper_writing_introduction_20260516T022839\", \"task_type\": \"paper_writing:introduction\", \"project\": \"vla-ssd\", \"status\": \"done\", \"started_at\": \"2026-05-16T02:28:39.464376+00:00\", \"ended_at\": \"2026-05-16T02:30:23.555187+00:00\"}], \"count\": 5}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 203
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-16T02:33:13.494373+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": [{\"id\": \"plan_001\", \"claim\": 1, \"description\": \"SigLIP+Projector RSA vs Full VLA vs DINO — 证明 action-relevant 结构源自 frozen vision encoder\", \"priority\": \"P0\", \"gpu_budget_hours\": 1, \"deps\": [], \"registry_id\": \"d027_siglip_only_rsa\", \"status\": \"DONE\", \"result\": \"RSA=0.615 >> VLA 0.488 >> DINO 0.388\", \"conclusion\": \"success\", \"metrics\": {\"siglip_projector_rsa\": 0.6153, \"bootstrap_95_ci\": [0.5257, 0.6954], \"comparison\": {\"siglip_projector\": 0.6153, \"trained_with_inst\": 0.4876, \"untrained_with_inst\": 0.4846, \"untrained_no_inst\": 0.4802, \"trained_no_inst\": 0.489, \"dino\": 0.388}, \"llm_degradation\": \"LLM reduces RSA from 0.615 (projector output) to ~0.488 (LLM hidden states)\", \"gate_judgment\": \"PASS — SigLIP+projector RSA=0.6153 >> 0.45-0.50 threshold. Vision encoder is the source of action-relevant structure. LLM is not passthrough but actually degrades action alignment.\"}}, {\"id\": \"plan_002\", \"claim\": 1, \"description\": \"DINO baseline RSA — standalone vision model 参照\", \"priority\": \"P0\", \"gpu_budget_hours\": 0.5, \"deps\": [], \"registry_id\": \"dinov2_baseline\", \"status\": \"DONE\", \"result\": \"RSA=0.388\", \"conclusion\": \"success\", \"metrics\": {\"temporal_distance_rho\": 0.833, \"temporal_distance_rho_pooled\": 0.833, \"per_task_rho_mean\": 0.9008, \"per_task_rho_range\": [0.41, 0.68], \"per_task_n_pairs\": 500, \"R2\": 0.687, \"MAE\": 0.127, \"feature_dim\": 1024, \"num_layers\": 1, \"probe_type\": \"mlp_adam_early_stopping\", \"training_time_seconds\": 7.5, \"note\": \"pooled ρ=0.833 inflated by cross-task variance; per-task mean ρ=0.9008 is correct comparison baseline (updated per D005/D006)\", \"subtask_macro_auc\": 0.9717, \"subtask_auc_per_predicate\": {\"subtask_0\": 0.9694, \"subtask_1\": 0.9739}, \"subtask_labels\": \"auto-extracted from MuJoCo state transitions (2 subtasks per task)\", \"subtask_probe_type\": \"sklearn_lo
…[truncated 9915 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__read_experiment_plan_with_status",
  "elapsed_ms": 153
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-16T02:33:26.992434+00:00_

called mcp__agent-ml-research__get_worker_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_worker_status</summary>

```json
{
  "worker_id": "worker_ssh_patch-mean-probe_20260516T022703",
  "verbose": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "tool_args": {
    "worker_id": "worker_ssh_patch-mean-probe_20260516T022703",
    "verbose": "True"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-16T02:33:27.043137+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_ssh_patch-mean-probe_20260516T022703\", \"status\": \"running\", \"task_type\": \"ssh:patch-mean-probe\", \"project\": \"vla-ssd\", \"started_at\": \"2026-05-16T02:27:04.067388+00:00\", \"ended_at\": null, \"setup\": null, \"teardown\": null, \"setup_data\": {}, \"progress\": {\"recent_tools\": [\"ssh_read_only\", \"ssh_read_only\", \"ssh_read_only\", \"ssh_read_only\", \"ssh_read_only\"], \"last_text\": \"执行完毕。出现重要发现：DINO RSA=0.388 与我用 rsa_clip.py 相同方法重算的值（cls_token=0.6915, patch_mean=0.6307）差异巨大。需要确认0.388的来源方法。\", \"turn_count\": 9}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-16T02:33:40.298959+00:00_

called mcp__agent-ml-research__get_worker_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_worker_status</summary>

```json
{
  "worker_id": "worker_paper_writing_experiments_20260516T021635",
  "verbose": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "tool_args": {
    "worker_id": "worker_paper_writing_experiments_20260516T021635",
    "verbose": "True"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-16T02:33:40.801270+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_paper_writing_experiments_20260516T021635\", \"status\": \"done\", \"task_type\": \"paper_writing:experiments\", \"project\": \"vla-ssd\", \"started_at\": \"2026-05-16T02:16:35.914061+00:00\", \"ended_at\": \"2026-05-16T02:23:23.728486+00:00\", \"setup\": null, \"teardown\": null, \"setup_data\": {}, \"result\": {\"raw\": \"已完成。两个文件已写入 `docs/paper/`:\\n\\n**`experiments.tex`** — Section 3 完整 LaTeX，包含:\\n- **3.1 Experimental Setup**: LIBERO-Goal, OpenVLA-7B, 5 种表征源, 2×2 实验设计, RSA + functional probe 方法\\n- **3.2 Vision Encoder Dominance**: Table 1 (RSA 排序), Figure 2, geometric-functional dissociation (DINO R²≈Proj 但 RSA<<), CKA 排序反转负向结果 (Figure 6)\\n- **3.3 LLM Redistributes Action Structure**: Table 2 (probe R²), Figure 3 (per-layer curves), Figure 4 (probe bars), distributed degradation + readout concentration\\n- **3.4 Training Routes, Not Creates**: Table 3 (训练效应), Figure 5 (2×2 matrix + instruction control), geometric null + functional concentration dissociation\\n\\n**`references.bib`** — 12 条 BibTeX，其中 `grant2026` 和 `haon2025` 标记了 `[VERIFY]`，需要补全真实书目信息。其余 10 条基于已知信息填写。\"}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "elapsed_ms": 502
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-16T02:33:40.801813+00:00_

called mcp__agent-ml-research__get_worker_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_worker_status</summary>

```json
{
  "worker_id": "worker_paper_writing_method_20260516T022801",
  "verbose": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "tool_args": {
    "worker_id": "worker_paper_writing_method_20260516T022801",
    "verbose": "True"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-16T02:33:41.253975+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_paper_writing_method_20260516T022801\", \"status\": \"done\", \"task_type\": \"paper_writing:method\", \"project\": \"vla-ssd\", \"started_at\": \"2026-05-16T02:28:01.818163+00:00\", \"ended_at\": \"2026-05-16T02:29:29.179014+00:00\", \"setup\": null, \"teardown\": null, \"setup_data\": {}, \"result\": {\"raw\": \"`register_artifact` 工具不可用。文件已写入指定路径。\\n\\n`method.tex` 已生成：`/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/method.tex`\\n\\n结构：\\n- **2.1 Model and Data** — OpenVLA-7B 架构、LIBERO-10/Goal 数据、untrained control 设计\\n- **2.2 Representation Extraction** — 5 个表征源 (a)-(e) + 2×2 factorial design\\n- **2.3 RSA** — RDM 构建、Spearman ρ、bootstrap CI\\n- **2.4 Functional Action Probes** — MLP 探针架构/训练、R²、action-delta probes、统计检验\\n- **2.5 CKA** — Linear CKA + RDM kernel CKA、维度不匹配 caveat\\n\\n术语和引用格式与 `experiments.tex` 保持一致，无实验结果数字。\"}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "elapsed_ms": 452
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-16T02:33:41.255853+00:00_

called mcp__agent-ml-research__get_worker_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_worker_status</summary>

```json
{
  "worker_id": "worker_paper_writing_introduction_20260516T022839",
  "verbose": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "tool_args": {
    "worker_id": "worker_paper_writing_introduction_20260516T022839",
    "verbose": "True"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-16T02:33:41.808398+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_paper_writing_introduction_20260516T022839\", \"status\": \"done\", \"task_type\": \"paper_writing:introduction\", \"project\": \"vla-ssd\", \"started_at\": \"2026-05-16T02:28:39.464376+00:00\", \"ended_at\": \"2026-05-16T02:30:23.555187+00:00\", \"setup\": null, \"teardown\": null, \"setup_data\": {}, \"result\": {\"raw\": \"`introduction.tex` 已写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/introduction.tex`。\\n\\n5 段结构：Problem → Gap → Approach → Findings (with headline numbers) → Implications + 3 contributions（enumerate）。约 ~650 词，符合 1-1.5 页目标。所有引用 key 均按指定使用，包括 `hou2026` 和 `fei2025`。数值用 p0_probe_v2 口径（R² 0.706/0.683/0.731/0.686，RSA 0.615/0.557/0.388）。\\n\\n`register_artifact` 工具不在当前可用 MCP 工具列表中，无法注册。如需注册请手动操作或确认工具名称。\"}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "elapsed_ms": 552
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-16T02:33:42.661112+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/**",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-16T02:33:42.661669+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/figures/paper/fig3.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/figures/paper/fig3.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/figures/paper/fig2.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/figures/paper/fig2.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/figures/paper/fig4.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/figures/paper/fig4.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/figures/paper/fig5.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/figures/paper/fig5.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/figures/paper/fig6.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/figures/paper/fig6.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/references.bib
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/introduction.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-16T02:33:56.323842+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__get_project_resource_usage,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__load_project_config",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__get_project_resource_usage,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__load_project_config",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-16T02:33:56.374448+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-16T02:33:59.487134+00:00_

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
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__get_project_resource_usage",
  "tool_args": {
    "project": "vla-ssd"
  }
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-16T02:33:59.537755+00:00_

called mcp__agent-ml-research__load_project_config

<details open><summary>🔧 Tool call — mcp__agent-ml-research__load_project_config</summary>

```json
{
  "project_name": "vla-ssd",
  "section": "execution"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__load_project_config",
  "tool_args": {
    "project_name": "vla-ssd",
    "section": "execution"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-16T02:33:59.638827+00:00_

{"result":"{\"success\": true, \"data\": {\"allocated_gpus\": [{\"server\": \"westd-19183\", \"gpu_id\": \"cuda:0\"}, {\"server\": \"westd-19183\", \"gpu_id\": \"cuda:1\"}], \"actually_running_gpus\": [], \"allocated_but_idle\": [{\"server\": \"westd-19183\", \"gpu_id\": \"cuda:0\", \"idle_min\": null}, {\"server\": \"westd-19183\", \"gpu_id\": \"cuda:1\", \"idle_min\": null}], \"running_experiments\": [], \"worker_pool\": {\"total\": 1, \"gpu_tasks\": 0, \"cpu_tasks\": 1, \"details\": [{\"worker_id\": \"worker_ssh_patch-mean-probe_20260516T022703\", \"task\": \"ssh:patch-mean-probe\"}]}, \"summary\": \"分配 2 张, 实际跑 0 张 ⚠️ | Worker 1 (GPU 0 / CPU 1)\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__get_project_resource_usage",
  "elapsed_ms": 151
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-16T02:33:59.689567+00:00_

{"result":"{\"success\": true, \"data\": {\"project\": \"vla-ssd\", \"section\": \"execution\", \"config\": {\"execution\": {\"gpu_ids\": [\"cuda:0\", \"cuda:1\"], \"project_path\": \"/root/vla-ssd\", \"servers\": [\"westd-19183\"]}}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__load_project_config",
  "elapsed_ms": 151
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-16T02:34:28.451678+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/.claude/skills/resource-saturation.skill.md",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/.claude/skills/resource-saturation.skill.md",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-16T02:34:28.954398+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/.claude/sessions/agent_17452cf3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-16T02:34:29.205765+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "vla-ssd",
  "file": "paper_framing.md",
  "max_chars": "6000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "vla-ssd",
    "file": "paper_framing.md",
    "max_chars": "6000"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-16T02:34:29.306901+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper_framing.md\", \"content\": \"# Paper Framing — vla-ssd\\n\\n## Target Venue\\n- Primary: CoRL 2026\\n- Deadline: Abstract May 26, Paper May 29\\n- Format: 8 pages + references\\n\\n## Core Claims (3 条)\\n\\n1. **Vision Encoder Dominance + Geometric-Functional Dissociation**: VLA 中 action-relevant 表征结构由 frozen vision encoder 决定。RSA geometric alignment: SigLIP (0.615) > CLIP (0.557) >> DINO (0.388)——VL pretrained encoders 显著优于 vision-only。但 functional capacity (R²) 方向相反: DINO (0.634) ≈ Projector (0.630) > CLIP (0.587)。**Geometric alignment 和 predictive capacity 是可分离的独立维度**。VL pretraining 提供 geometric alignment（表征结构匹配 action 空间），不增加甚至略降低 functional capacity。\\n2. **LLM Redistributes Action-Relevant Structure (Training-Dependent)**: LLM 降解 distributed image token 的 **geometric alignment**（RSA: 0.615→0.501）和 functional capacity（R²: 0.630→0.599, p<0.001），但 global structure 保留（CKA 单调上升）。**训练后** LLM 学会将 action 信号 concentrate 到 readout token（trained R²=0.671 > projector 0.630, p=0.002），但 **untrained LLM 做不到**（untrained readout best=0.686 < projector）。Readout concentration 是 learned behavior，不是架构固有属性。\\n3. **Training: Routing Without Creating**: VLA fine-tuning 不改变 distributed representation structure（image_mean RSA: trained 0.501 ≈ untrained 0.485, bootstrap CI includes 0, p=0.20），但提升 readout concentration（trained last_preaction 0.731 >> untrained 0.686，Δ=0.045, bootstrap CI=[0.032, 0.058], p<0.0001）。Instruction input 对两者均无影响。综合解读：**Training 的贡献是学习信息路由（routing），而非注入新的 action knowledge（creating）**。\\n\\n## Paper 主数值基准（image_mean 聚合，公平对比）\\n\\n| Model / Condition | RSA (image_mean) | Notes |\\n|---|---|---|\\n| **SigLIP+Projector** | **0.615** | Smoking gun, LLM input |\\n| VLA trained with-inst | 0.501 | Peak L23 |\\n| VLA untrained with-inst | 0.485 | Peak L23 |\\n| VLA trained no-inst | 0.501 | Peak L23, identical to with-inst |\\n| VLA untrained no-
…[truncated 4474 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 101
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-16T02:34:34.784117+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/resource-saturation.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/resource-saturation.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-16T02:34:34.834769+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-16T02:34:37.476675+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "resource-saturation",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "Grep",
  "tool_args": {
    "pattern": "resource-saturation",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-16T02:34:37.728024+00:00_

Found 63 files
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/logs/chats/cron_hook_mvp_controlb_trained.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/.claude/sessions/agent_98133724/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/.claude/sessions/agent_98133724/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/global/logs/skill_usage.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/logs/chats/feishu_group_oc_9e9aef1687e6abd097aa0edaf0551ee3.jsonl
AGENTS.md
CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/logs/chats/archive/cron_hook_mvp_controlb_trained_20260516T023241_656735.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/.claude/sessions/director_62a591ad/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/.claude/sessions/director_62a591ad/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/logs/chats/cron_hook_mvp_probe_untrained.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/logs/chats/cron_hook_mvp_probe_trained.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/.claude/sessions/agent_89bf97d0/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/.claude/sessions/agent_89bf97d0/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/logs/chats/archive/cron_hook_mvp_probe_untrained_20260516T022853_364694.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/.claude/sessions/agent_3dde598c/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/.claude/sessions/agent_3dde598c/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/logs/chats/archive/cron_hook_mvp_probe_trained_20260516T022341_029642.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/logs/chats/cron_hook_openvla-trained-extract.json
…[truncated 5722 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "Grep",
  "elapsed_ms": 251
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-16T02:35:09.060356+00:00_

called mcp__agent-ml-research__main_agent_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__main_agent_post_to_director</summary>

```json
{
  "text": "[资源] GPU 分配 2 / 实际跑 0（论文写作阶段，无训练需求）| Worker 池 1 (GPU 0 / CPU 1)\n\n**Loop #6 Session Start 汇报**\n\n**实验**: 全部 DONE（31 success / 7 negative / 7 killed），0 RUNNING，0 active crons。\n\n**论文进展**: D035 批准后，三个核心章节已完成初稿：\n- Introduction.tex ✅（5段结构，~650词，headline numbers 用 p0_probe_v2 口径）\n- Method.tex ✅（2.1-2.5，5个表征源 + RSA/probe/CKA 方法）\n- Experiments.tex ✅（3.1-3.4，三条 Claim 对应三个 subsection + tables/figures）\n- references.bib ✅（12条，2条需 VERIFY）\n- fig2-fig6 ✅（PDF+PNG）\n\n**缺失**: Abstract、Conclusion/Discussion、Related Work、fig1（主概念图）\n\n**⚠️ 潜在问题**: 1 个 running worker（patch-mean-probe，turn 9）发现 DINO RSA 可能存在方法差异——原始 0.388 vs 用 rsa_clip.py 重算 cls_token=0.69/patch_mean=0.63。正在调查是聚合方法差异还是真实错误。如果 DINO RSA 显著升高，Claim 1 中 \"VL >> vision-only\" 的幅度会缩小。等该 worker 完成后评估影响。\n\n**下一步**:\n1. 等 patch-mean-probe worker 回调，评估 DINO RSA 影响\n2. 先派 Worker 写 Related Work（不依赖具体数字）\n3. DINO 问题澄清后写 Abstract + Conclusion\n4. plan_010 LIBERO-Spatial（P2）视时间决定\n\n请问 Director 是否有优先级调整？",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "tool_args": {
    "text": "[资源] GPU 分配 2 / 实际跑 0（论文写作阶段，无训练需求）| Worker 池 1 (GPU 0 / CPU 1)\n\n**Loop #6 Session Start 汇报**\n\n**实验**: 全部 DONE（31 success / 7 negative / 7 killed），0 RUNNING，0 active crons。\n\n**论文进展**: D035 批准后，三个核心章节已完成初稿：\n- Introduction.tex ✅（5段结构，~650词，headline numbers 用 p0_probe_v2 口径）\n- Method.tex ✅（2.1-2.5，5个表征源 + RSA/probe/CKA 方法）\n- Experiments.tex ✅（3.1-3.4，三条 Claim 对应三个 subsection + tables/figures）\n- references.bib ✅（12条，2条需 VERIFY）\n- fig2-fig6 ✅（PDF+PNG）\n\n**缺失**: Abstract、Conclusion/Discussion、Related Work、fig1（主概念图）\n\n**⚠️ 潜在问题**: 1 个 running worker（patch-mean-probe，turn 9）发现 DINO RSA 可能存在方法差异——原始 0.388 vs 用 rsa_clip.py 重算 cls_token=0.69/patch_mean=0.63。正在调查是聚合方法差异还是真实错误。如果 DINO RSA 显著升高，Claim 1 中 \"VL >> vision-only\" 的幅度会缩小。等该 worker 完成后评估影响。\n\n**下一步**:\n1. 等 patch-mean-probe worker 回调，评估 DINO RSA 影响\n2. 先派 Worker 写 Related Work（不依赖具体数字）\n3. DINO 问题澄清后写 Abstract + Conclusion\n4. plan_010 LIBERO-Spatial（P2）视时间决定\n\n请问 Director 是否有优先级调整？",
    "project": "vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-16T02:35:13.078454+00:00_

{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_a1d032cbe70bdd2058438e67e0d57613:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "elapsed_ms": 4018
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-16T02:35:21.019377+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "vla-ssd",
  "file": "literature_map.yaml",
  "max_chars": "6000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "vla-ssd",
    "file": "literature_map.yaml",
    "max_chars": "6000"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-16T02:35:21.070267+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/literature_map.yaml\", \"content\": \"papers:\\n  # ============================================================\\n  # DIRECT COMPETITORS — VLA Representation Analysis / Interpretability\\n  # ============================================================\\n  - id: grant2026\\n    title: \\\"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models\\\"\\n    authors: \\\"Bryce Grant, Xijia Zhao, Peng Wang\\\"\\n    year: 2026\\n    venue: \\\"arXiv preprint (under review)\\\"\\n    arxiv_id: \\\"2603.19233\\\"\\n    category: direct-competitor\\n    role: competitor\\n    key_findings: >\\n      Visual pathway dominates action generation across all 6 tested VLA architectures (80M–7B params, 394K+ rollout episodes, 4 benchmarks).\\n      Language sensitivity depends on task structure: when visual context uniquely specifies the task, language is IGNORED;\\n      when multiple goals share a scene, language becomes essential (\\\"encoded but not used\\\").\\n      Cross-task activation injection steers robots toward source-task positions (99.8% trajectory alignment with source in X-VLA).\\n      Multi-pathway architectures (pi0.5, SmolVLA, GR00T) separate motor programs (expert pathway) from goal semantics (VLM pathway).\\n    relevance_to_us: >\\n      Most direct competitor. Behavioral intervention (activation injection, SAE, probing) reveals vision dominance + language encoded but not used.\\n      Uses OpenVLA-OFT checkpoint; we use standard fine-tuning — must qualify this difference in Related Work.\\n    novelty_gap: >\\n      No trained vs untrained representation analysis. They compare different model architectures,\\n      we compare trained vs untrained representation structure within the same architecture.\\n      Their \\\"encoded but not used\\\" is a behavioral-level conclusion; we demonstrate at the represent
…[truncated 4648 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-16T02:35:22.475693+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/experiments.tex",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/experiments.tex",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-16T02:35:22.476130+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Benchmark and model.}
8	We evaluate on the LIBERO-Goal suite~\cite{liu2023_libero}, comprising 10 tabletop manipulation tasks with 50 human demonstrations each.
9	We use OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, a vision-language-action model consisting of a SigLIP-SO400M vision encoder~\cite{zhai2023_siglip}, an MLP projector, and a Llama-2 7B language backbone, fine-tuned on the LIBERO-10 split.
10	
11	\paragraph{Representation sources.}
12	We extract representations from five sources:
13	(a)~\textbf{SigLIP+Projector}---the vision encoder output after MLP projection into LLM input space;
14	(b)~\textbf{LLM image\_mean}---the mean of image token activations at each LLM layer, capturing distributed visual information;
15	(c)~\textbf{LLM last\_preaction}---the final token position before action decoding (readout token) at each LLM layer;
16	(d)~\textbf{DINOv2 ViT-L/14}~\cite{oquab2024_dinov2} \texttt{cls\_token}; and
17	(e)~\textbf{CLIP ViT-L/14}~\cite{radford2021_clip} \texttt{patch\_mean}.
18	Sources (d) and (e) serve as external baselines with no VLA training signal.
19	
20	\paragraph{Experimental conditions.}
21	We use a $2 \times 2$ factorial design crossing \emph{training status} (trained vs.\ untrained) with \emph{instruction presence} (with vs.\ without language instruction).
22	The untrained control applies \texttt{from\_config()} to reinitialize the LLM parameters (6.74B random weights) while preserving the frozen SigLIP encoder (0.80B pretrained weights), isolating the LLM's learned contribution from the vision encoder's pretrained geometry.
23	
24	\paragraph{Representational Similarity Analysis (RSA).}
25	Following~\cite{kriegeskorte2008}, we compute pairwise representational dissimilarity matrices (RDMs) for each representation source and for the 7-dimensional action space.
26	We report Spearman rank correlation $\rho$ betwee
…[truncated 394 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-16T02:35:22.877827+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/introduction.tex",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/introduction.tex",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-16T02:35:22.878266+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Vision-language-action models (VLAs) achieve impressive robotic manipulation performance by fine-tuning large language models on robot demonstration data~\cite{brohan2023_rt2,kim2024_openvla}.
5	The dominant architecture grafts a frozen vision encoder onto a pretrained LLM backbone, then fine-tunes the system end-to-end to map visual observations and language instructions to continuous actions~\cite{karamcheti2024}.
6	An implicit assumption underlies this paradigm: fine-tuning injects action-relevant representational knowledge into the LLM.
7	But where do action representations actually come from?
8	Do they originate in the vision encoder's pretrained features, emerge through LLM processing, or arise from task-specific fine-tuning?
9	
10	Recent work reveals cracks in this assumption.
11	Grant et al.~\cite{grant2026} showed that the visual pathway dominates action generation across multiple VLA architectures, with ablations to the language stream producing minimal behavioral degradation.
12	Independently, Hou et al.~\cite{hou2026} and Fei et al.~\cite{fei2025} demonstrated that VLAs largely ignore language instructions during policy execution.
13	These findings challenge the prevailing narrative but remain at the behavioral level---they reveal \emph{what} drives VLA outputs without explaining \emph{where} action-relevant structure resides in the representation space.
14	No prior work has performed a representational decomposition that measures each component's independent contribution to action-relevant structure.
15	Without this, we cannot determine whether fine-tuning truly injects action knowledge or merely learns to route pre-existing structure.
16	
17	We present the first systematic representational and functional analysis of a VLA.
18	Taking OpenVLA-7B~\cite{kim2024_openvla} as a case study, we decompose its processing pipeline into constituent components: the frozen SigLIP vision encoder~\cite{zhai2023_s
…[truncated 1894 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-16T02:35:47.710068+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__spawn_worker",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__spawn_worker",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-16T02:35:47.710404+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-16T02:36:20.983179+00:00_

called mcp__agent-ml-research__spawn_worker

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker</summary>

```json
{
  "task_type": "paper_writing:related_work",
  "project": "vla-ssd",
  "task_prompt": "## 任务：撰写 Related Work 章节\n\n写一个完整的 Related Work section（LaTeX 格式），保存到：\n`/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/related_work.tex`\n\n### 论文背景\n本文首次对 VLA (Vision-Language-Action model) 进行系统性表征分析，发现三个核心结论：\n1. Vision encoder 是 action-relevant 结构的主要来源，VL pretraining 提供 geometric alignment 但不增加 predictive capacity（geometric-functional dissociation）\n2. LLM 降解分布式表征的几何对齐但通过训练依赖的 attention 将信号集中到 readout token（redistribution）\n3. Training 教会 routing 而非 creating new knowledge\n\n目标会议：CoRL 2026（8 页 + references）\n\n### Related Work 结构要求\n分 3-4 个小节，建议：\n1. **Vision-Language-Action Models** — VLA 架构演进（RT-2, OpenVLA, pi0 等），强调 end-to-end fine-tuning 范式的隐性假设\n2. **Understanding VLA Representations** — VLA 内部表征分析的最新工作（Grant 2026, Swann 2026, Rizzardo 2026, Haon 2025, Molinari 2025），指出它们是 behavioral-level 或 feature-level 的，缺乏系统性 representational decomposition\n3. **Representational Analysis in Deep Learning** — RSA (Kriegeskorte 2008), CKA (Kornblith 2019), probing (Alain 2017, Belinkov 2022) 作为方法论基础\n4. （可选）**Vision-Language Pretraining and Representation Transfer** — CLIP, SigLIP, DINOv2 的预训练范式差异，与我们 geometric-functional dissociation 发现的联系\n\n### 关键文献（必须引用）\n\n**Direct competitors:**\n- Grant et al. 2026 (arxiv 2603.19233) — visual pathway dominance, behavioral level, 6 VLA architectures\n- Swann et al. 2026 (arxiv 2603.19183) — SAE on OpenVLA, feature-level\n- Rizzardo et al. 2026 (arxiv 2603.05487) — feature observability/controllability\n- Haon et al. 2025 (CoRL, arxiv 2509.00328) — first VLA mechanistic interp, activation steering\n- Molinari et al. 2025 (arxiv 2509.24559) — world model probing in OpenVLA\n\n**Methodology:**\n- Kriegeskorte et al. 2008 — RSA\n- Kornblith et al. 2019 — CKA\n- Alain & Bengio 2017 — linear probes\n- Belinkov 2022 — probing survey\n\n**VLA/VLM architectures:**\n- Brohan et al. 2023 — RT-2\n- Kim et al. 2024 — OpenVLA\n- Karamcheti et al. 2024 — Prismatic VLMs\n- Black et al. 2024 — pi0\n\n**Vision encoders:**\n- Zhai et al. 2023 — SigLIP\n- Radford et al. 2021 — CLIP\n- Oquab et al. 2024 — DINOv2\n\n### 写作规范\n- 每段开头用一句话点明本段要传达的信息（topic sentence）\n- 引用格式用 \\cite{key}，key 用上面提到的 id（如 grant2026, haon2025 等）\n- 最后一段必须明确说明我们的工作与已有工作的差异：我们是 representational-level（不是 behavioral-level），我们做 trained vs untrained comparison（没人做过），我们发现 geometric-functional dissociation（新发现）\n- 控制在 1-1.5 页（CoRL 格式），约 600-800 词\n- 语言简洁，不要过度引用，每个引用必须有明确目的\n- 不要编造任何论文或引用——只用上面列出的文献。如果某个领域需要更多引用但你不确定具体论文，用 `[CITE-NEEDED]` 标记\n\n### 已有章节引用 key 参考\n已写好的 experiments.tex 使用的 cite key 包括：liu2023_libero, kim2024_openvla, karamcheti2024, zhai2023_siglip, oquab2024_dinov2, radford2021_clip, kriegeskorte2008, alain2017。请与这些 key 保持一致（同一篇论文用相同 key）。\n\n### 产出\n1. `related_work.tex` 文件（LaTeX，\\section{Related Work}）\n2. 如有新增引用 key，列出需要添加到 references.bib 的条目",
  "tool_groups": "['knowledge']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "tool_args": {
    "task_type": "paper_writing:related_work",
    "project": "vla-ssd",
    "task_prompt": "## 任务：撰写 Related Work 章节\n\n写一个完整的 Related Work section（LaTeX 格式），保存到：\n`/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/related_work.tex`\n\n### 论文背景\n本文首次对 VLA (Vision-Language-Action model) 进行系统性表征分析，发现三个核心结论：\n1. Vision encoder 是 action-relevant 结构的主要来源，VL pretraining 提供 geometric alignment 但不增加 predictive capacity（geometric-functional dissociation）\n2. LLM 降解分布式表征的几何对齐但通过训练依赖的 attention 将信号集中到 readout token（redistribution）\n3. Training 教会 routing 而非 creating new knowledge\n\n目标会议：CoRL 2026（8 页 + references）\n\n### Related Work 结构要求\n分 3-4 个小节，建议：\n1. **Vision-Language-Action Models** — VLA 架构演进（RT-2, OpenVLA, pi0 等），强调 end-to-end fine-tuning 范式的隐性假设\n2. **Understanding VLA Representations** — VLA 内部表征分析的最新工作（Grant 2026, Swann 2026, Rizzardo 2026, Haon 2025, Molinari 2025），指出它们是 behavioral-level 或 feature-level 的，缺乏系统性 representational decomposition\n3. **Representational Analysis in Deep Learning** — RSA (Kriegeskorte 2008), CKA (Kornblith 2019), probing (Alain 2017, Belinkov 2022) 作为方法论基础\n4. （可选）**Vision-Language Pretraining and Representation Transfer** — CLIP, SigLIP, DINOv2 的预训练范式差异，与我们 geometric-functional dissociation 发现的联系\n\n### 关键文献（必须引用）\n\n**Direct competitors:**\n- Grant et al. 2026 (arxiv 2603.19233) — visual pathway dominance, behavioral level, 6 VLA architectures\n- Swann et al. 2026 (arxiv 2603.19183) — SAE on OpenVLA, feature-level\n- Rizzardo et al. 2026 (arxiv 2603.05487) — feature observability/controllability\n- Haon et al. 2025 (CoRL, arxiv 2509.00328) — first VLA mechanistic interp, activation steering\n- Molinari et al. 2025 (arxiv 2509.24559) — world model probing in OpenVLA\n\n**Methodology:**\n- Kriegeskorte et al. 2008 — RSA\n- Kornblith et al. 2019 — CKA\n- Alain & Bengio 2017 — linear probes\n- Belinkov 2022 — probing survey\n\n**VLA/VLM architectures:**\n- Brohan et al. 2023 — RT-2\n- Kim et al. 2024 — OpenVLA\n- Karamcheti et al. 2024 — Prismatic VLMs\n- Black et al. 2024 — pi0\n\n**Vision encoders:**\n- Zhai et al. 2023 — SigLIP\n- Radford et al. 2021 — CLIP\n- Oquab et al. 2024 — DINOv2\n\n### 写作规范\n- 每段开头用一句话点明本段要传达的信息（topic sentence）\n- 引用格式用 \\cite{key}，key 用上面提到的 id（如 grant2026, haon2025 等）\n- 最后一段必须明确说明我们的工作与已有工作的差异：我们是 representational-level（不是 behavioral-level），我们做 trained vs untrained comparison（没人做过），我们发现 geometric-functional dissociation（新发现）\n- 控制在 1-1.5 页（CoRL 格式），约 600-800 词\n- 语言简洁，不要过度引用，每个引用必须有明确目的\n- 不要编造任何论文或引用——只用上面列出的文献。如果某个领域需要更多引用但你不确定具体论文，用 `[CITE-NEEDED]` 标记\n\n### 已有章节引用 key 参考\n已写好的 experiments.tex 使用的 cite key 包括：liu2023_libero, kim2024_openvla, karamcheti2024, zhai2023_siglip, oquab2024_dinov2, radford2021_clip, kriegeskorte2008, alain2017。请与这些 key 保持一致（同一篇论文用相同 key）。\n\n### 产出\n1. `related_work.tex` 文件（LaTeX，\\section{Related Work}）\n2. 如有新增引用 key，列出需要添加到 references.bib 的条目",
    "tool_groups": "['knowledge']"
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-16T02:36:24.447276+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_paper_writing_related_work_20260516T023622\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/logs/workers/worker_paper_writing_related_work_20260516T023622.log\", \"setup_data\": {}, \"message\": \"Worker worker_paper_writing_related_work_20260516T023622 started. Use get_worker_status('worker_paper_writing_related_work_20260516T023622') to check progress.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "elapsed_ms": 3464
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-16T02:36:57.820697+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/introduction.tex",
  "offset": "25",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/introduction.tex",
    "offset": "25",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-16T02:36:58.573636+00:00_

25	SigLIP+Projector achieves the highest action-space alignment (RSA $\rho = 0.615$), followed by CLIP ($\rho = 0.557$), both far exceeding the vision-only DINOv2 ($\rho = 0.388$).
26	Yet DINOv2 matches SigLIP+Projector in action prediction capacity ($R^2 = 0.712$ vs.\ $0.706$, $p = 0.22$), revealing a geometric-functional dissociation: VL pretraining provides geometric alignment with the action space without increasing raw decodability.
27	\textbf{Second}, the LLM degrades distributed geometric alignment (RSA $0.615 \to 0.501$) but concentrates a functionally superior signal at the readout token ($R^2 = 0.731$, exceeding the projector's $0.706$).
28	This concentration is training-dependent: an untrained LLM's readout achieves only $R^2 = 0.686$, falling below the projector baseline.
29	\textbf{Third}, training teaches routing, not creating.
30	Distributed RSA is training-invariant ($\Delta = 0.021$, 95\% CI includes zero, $p = 0.20$), while readout concentration shows a large training effect ($\Delta = 0.045$, $p < 0.0001$).
31	Language instructions affect neither metric.
32	
33	These results reframe how we understand VLA representations and carry direct design implications: vision encoder pretraining quality---not LLM fine-tuning---is the primary lever for action-relevant structure~\cite{haon2025}.
34	Our contributions are:
35	\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]
36	    \item The first systematic representational decomposition of a VLA, quantifying each component's contribution to action-relevant structure with both geometric (RSA) and functional (probe $R^2$) metrics.
37	    \item Discovery of a geometric-functional dissociation: vision-language pretraining provides geometric alignment with the action space beyond what raw information content predicts, while vision-only features are functionally rich but geometrically dissimilar.
38	    \item Evidence that LLM fine-tuning teaches information routing---concentrating pre-existing vision-encoder st
…[truncated 114 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "Read",
  "elapsed_ms": 752
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-16T02:36:58.674420+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/experiments.tex",
  "offset": "30",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/experiments.tex",
    "offset": "30",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-16T02:36:58.775398+00:00_

30	
31	%------------------------------------------------------------------
32	\subsection{Vision Encoder Dominance}
33	\label{sec:vision_dominance}
34	
35	This experiment tests whether vision-language pretrained encoders provide the dominant source of action-relevant geometric structure in VLA representations.
36	
37	Table~\ref{tab:rsa_overview} reports RSA $\rho$ between each representation source and the action space.
38	The SigLIP+Projector output achieves the highest alignment ($\rho = 0.615$, 95\% CI $[0.526, 0.695]$), followed by CLIP ViT-L/14 ($\rho = 0.557$, $[0.442, 0.660]$).
39	Both vision-language pretrained encoders substantially exceed DINOv2 ($\rho = 0.388$), a vision-only model.
40	The VLA's LLM layers (best image\_mean: $\rho = 0.501$ trained, $\rho = 0.485$ untrained) fall between VL-pretrained encoders and DINOv2 (Figure~\ref{fig:rsa_bar}).
41	
42	Three findings emerge.
43	First, VL pretraining---not LLM processing---is the primary source of action-relevant structure.
44	SigLIP and CLIP, both pretrained on image-text pairs, achieve $\rho \geq 0.557$, while DINOv2, pretrained with self-supervised vision objectives alone, reaches only $\rho = 0.388$.
45	This 0.169-point gap indicates that language-grounded visual features carry substantially more action-relevant geometry than features learned without language, consistent with behavioral evidence of visual dominance in VLA policies~\cite{grant2026}.
46	
47	Second, the MLP projector provides incremental alignment: SigLIP+Projector ($0.615$) exceeds CLIP ($0.557$) by $\Delta = 0.058$, consistent with the projector mapping vision features into the LLM's embedding space.
48	
49	Third, the LLM degrades rather than enhances vision encoder geometry.
50	Processing through the LLM reduces RSA from $0.615$ (projector output) to $0.501$ (best LLM image\_mean), a drop of $\Delta = 0.114$.
51	
52	\paragraph{Geometric-functional dissociation.}
53	Functional probes reveal a dissociation between geometric similarity 
…[truncated 5181 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---

### Assistant

_source line 62 · 2026-05-16T02:37:53.093177+00:00_

我注意到一个潜在的数值一致性问题：Experiments 章节 Table 2 使用 p0_probe_v2 口径（Proj R²=0.706, DINO=0.712），但 paper_framing.md 规定 5-model 对比应用 unified_action_probe 口径（Proj=0.630, DINO=0.634）。这两组数字在同一篇论文中出现会让 reviewer 困惑。需要在 DINO RSA 问题澄清后统一处理。

当前状态：
- **Worker 池**: 2（patch-mean-probe 调查 DINO RSA 差异 + related_work 写作）
- **待处理**: patch-mean-probe 回调 → 评估影响 → 统一数字口径 → abstract/conclusion
- **已完成论文**: Introduction, Method, Experiments 初稿 + fig2-6 + references.bib
- **缺失**: Abstract, Conclusion/Discussion, Related Work (writing), fig1 概念图

等待 Worker 回调。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:mvp_controlb_trained"
}
```

</details>

---
