# cron hook precompute v4 shard2 20260514T212345 157204

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 98
- **Recorded user turns:** 2
- **Tool calls:** 47
- **Original source:** `logs/chats/archive/cron_hook_precompute-v4-shard2_20260514T212345_157204.jsonl`
- **Structured JSON:** [`9cf4ef06f297bc29a90c.json`](../../sessions/9c/9cf4ef06f297bc29a90c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

40 recorded events

### User

_source line 1 · 2026-05-14T18:13:59.105916+00:00_

[HANDOFF] 你是 Main Agent，这是 Loop #4。

## 上一轮交接 (task_context)

### 1. 🔴 硬约束 / 红线
- GPU 白名单仅 5 张: `bjb1-18228:cuda:{0,1,2,3}` + `bjb2-40593:cuda:0`。白名单外禁止启动实验，即使 Director 指令也必须 push back
- 服务器仅 2 台: `bjb1-18228`、`bjb2-40593`，project_path = `/root/acr-vla-conformal-refinement`
- 当前 5 张 GPU 全部被 RUNNING 实验占满，新实验（如 CRM v3 训练）必须等现有 eval 完成释放 GPU
- eval-acr-spatial-v3 是 **CORE CLAIM** 实验——即使预期会因 CRM v2 未归一化而表现差，也不能提前 kill，需要完整结果作为 CRM v2 vs v3 对比基线
- CRM v3 normalization 是当前唯一修复路径，训练数据验证 worker 正在跑，验证通过前不得提交 CRM v3 训练

### 2. 🖥️ 基础设施快照
- **bjb1-18228**: 4× RTX 4090, `/root/acr-vla-conformal-refinement`
- **bjb2-40593**: 1× RTX 4090 D, `/root/acr-vla-conformal-refinement`
- Python: 两台均用 conda（`source /root/miniconda3/bin/activate`），不是 venv
- 模型: `lerobot/smolvla_libero` (25K步全参微调, 7D action), VLM backbone `SmolVLM2-500M-Video-Instruct`
- HF cache: `/root/autodl-tmp/.hf_cache`（如有 AutoDL 实例时）
- Baselines 已锁定: spatial 30% (K=1), object 13% (K=1), SampleConsensus 34%
- **活跃进程**:
  - eval-acr-spatial-v3: PID 197057, bjb1 cuda:0（核心 claim，CRM v2 + D016 fix）
  - eval-argmin-only-spatial: PID 231421, bjb1 cuda:1（诊断：隔离 argmin 选择 vs CRM correction）
  - eval-tiny-correction-spatial: PID 232815, bjb1 cuda:2（诊断：极小 correction clipping 0.05）
  - eval-acr-object-v3: PID 197803, bjb1 cuda:3（object benchmark 泛化验证）
  - eval-vla-mean-spatial: PID 143106, bjb2 cuda:0（K=10 mean baseline）
- **活跃 cron**: eval-vla-mean-spatial（1 个）
- **活跃 worker**: `worker_verify_crm-v3-training-data_20260514T180836`（验证 CRM v3 训练数据归一化）

### 3. 📊 当前状态
**刚做完**: 发现并确认 CRM 输入未归一化是 correction 退化的根因（D018）。CRM 1030D 输入中 uncertainty features 与 action/obs 量级差 1500x，导致 MLP 学不到有意义的 correction（训练集只帮助 49% 样本 ≈ 随机）。已派 worker 实现 CRM v3（内嵌 per-feature standardization）并验证训练数据。

**正在等待**:
1. 5 路 eval 全部 RUNNING（无 metrics 产出，等 cron 回调）
2. CRM v3 训练数据验证 worker（running）
3. CRM v3 三组训练实验 PREPARING（crm-train-v3-perdof / scalar-unc / obs-only）—— 等 GPU 释放 + 验证通过

**PREPARING 队列**: 15 个实验（含 CRM v3 训练 ×3、precompute v2/v3/v4 shards、eval-object-v6-full 等）

**Registry 统计**: 58 实验 — DONE 38 (success 12, killed 15, failed 4) / RUNNING 5 / PREPARING 15

### 4. 📋 待办（条件触发式）
- **CRM v3 验证 worker 完成 → 确认 normalization stats 正确 → update registry crm-train-v3-* 为 QUEUED → 向 Director 申请审批**
- **eval-vla-mean-spatial 完成 → 记录 K=10 mean baseline → 与 VLA K=1 (30%) 和 SampleConsensus (34%) 对比 → 判断多采样平均的贡献**
- **eval-argmin-only-spatial 完成 → 如果 ≈ VLA mean (预计 ~40%)，则 CRM delta 是唯一退化源；如果 << VLA mean，则 argmin selection 本身有问题**
- **eval-tiny-correction-spatial 完成 → 如果 tiny >> full-correction，确认 correction magnitude 是主要问题（支持 CRM v3 normalization 修复方向）**
- **eval-acr-spatial-v3 完成 → 记录 CRM v2 未归一化的 full eval 结果作为对比基线**
- **eval-acr-object-v3 完成 → object benchmark 交叉验证**
- **任意 bjb1 GPU 释放 + CRM v3 审批通过 → 立即提交 CRM v3 训练（3 组 ablation 可在 3 张卡并行，~15min 完成）**
- **CRM v3 训练完成 → 立即铺 eval-acr-spatial-v4 + eval-acr-object-v4（CRM v3 归一化后的核心 claim 实验）**
- **如果 CRM v3 eval 仍低于 baseline → 触发 red-section，产 Framing 调整提案，考虑 correction gating / clipping 方向或 pivot**

### 5. 🎯 战略上下文
**核心结论链**:
- D011: 放弃 CoRL 2026，目标 ICLR 2027（DDL Sep-Oct 2026，时间充裕）
- D015: SFT Gate 30% baseline 继续推进，关注相对提升
- D016: 发现 CRM train/eval state 维度不匹配 bug → 修复 + 重跑
- D017: 修复后 CRM correction 仍全面拖累 baseline → kill ablation 实验
- D018: 根因确认为输入未归一化（1500x scale 差异），批准 CRM v3 normalization

**项目处于关键十字路口**: CRM v3 normalization 是"per-DOF conformal correction"核心 claim 的最后一搏。MVP 阶段 per-DOF > scalar > none 的信号是在合成数据上验证的，闭环 eval 一直无法复现（CRM v1 bug → CRM v2 normalization 问题）。如果 CRM v3 仍然失败，需要认真考虑 pivot。

**最易判断错的事**:
1. **不要把当前 5 路 eval 的结果当作 CRM 方法的最终裁决**——eval-acr-spatial-v3 / eval-acr-object-v3 用的是 CRM v2（未归一化），预期表现差。真正的 claim 验证要等 CRM v3 训练 + eval
2. **诊断实验（argmin-only、tiny-correction、vla-mean）的价值独立于 CRM 版本**——它们帮助定位退化是 argmin 选择问题还是 correction 幅度问题
3. **SampleConsensus 34% 不等于 ReconVLA**——当前 SampleConsensus baseline 是 raw argmin，ReconVLA 实际用 CQR 分位数回归，更强。后续可能需要 ReconVLA Medium baseline
4. **CRM v3 训练很快（~15min MLP）**，瓶颈在 eval（每路 100 rollouts，数小时）。GPU 释放后应立即开训练，不等所有 eval 完成

## 可查的历史
前 22 轮 handoff 在 `task_context/history/agent/loop_*.md`，如有疑问可 Read 回查。
完整聊天归档可用 `recall_session_history("关键词")` 搜索。

## 第一个动作要求
1. 用 `read_registry` 确认当前 RUNNING/PREPARING 实验状态（防止幻觉记忆过时状态）
2. 回复一句话确认你看到了上面的硬约束 + 当前活跃实验，再开始任何工具调用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:precompute-v4-shard2",
  "source": "system:ralph_loop"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-14T18:14:15.316369+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__list_workers",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__list_workers",
    "max_results": "6"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-14T18:14:15.368439+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "ToolSearch",
  "elapsed_ms": 52
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-14T18:14:18.297460+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'RUNNING'}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'RUNNING'}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T18:14:18.751543+00:00_

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
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T18:14:18.751996+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-tiny-correction-spatial\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-14T17:48:35.421Z\", \"updated_at\": \"2026-05-14T17:49:00.253Z\"}, \"eval-argmin-only-spatial\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-14T17:47:58.683Z\", \"updated_at\": \"2026-05-14T17:48:54.942Z\"}, \"eval-acr-object-v3\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-14T12:17:13.095Z\", \"updated_at\": \"2026-05-14T12:22:43.768Z\"}, \"eval-acr-spatial-v3\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-14T12:17:06.073Z\", \"updated_at\": \"2026-05-14T12:22:36.712Z\"}, \"eval-vla-mean-spatial\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-14T03:10:44.114Z\", \"updated_at\": \"2026-05-14T03:11:46.546Z\"}}, \"count\": 5, \"total\": 5, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2115}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 454
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T18:14:19.203712+00:00_

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
  "session": "cron:hook:precompute-v4-shard2",
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

_source line 8 · 2026-05-14T18:14:19.712054+00:00_

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
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T18:14:20.015568+00:00_

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
  "session": "cron:hook:precompute-v4-shard2",
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

_source line 10 · 2026-05-14T18:14:21.521209+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 5, \"results\": [{\"exp_id\": \"eval-vla-mean-spatial\", \"success\": true, \"actions\": [\"Job still running (pid=143106)\"]}, {\"exp_id\": \"eval-acr-spatial-v3\", \"success\": true, \"actions\": [\"Skipped (created 102s ago < interval 120s)\"]}, {\"exp_id\": \"eval-argmin-only-spatial\", \"success\": true, \"actions\": [\"Skipped (created 100s ago < interval 120s)\"]}, {\"exp_id\": \"eval-tiny-correction-spatial\", \"success\": true, \"actions\": [\"Skipped (created 100s ago < interval 120s)\"]}, {\"exp_id\": \"eval-acr-object-v3\", \"success\": true, \"actions\": [\"Skipped (created 99s ago < interval 120s)\"]}]}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 2769
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-14T18:14:21.571783+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md\", \"content\": \"# Handover — 2026-05-14\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| eval-tiny-correction-spatial | — | — | — | — |\\n| eval-argmin-only-spatial | — | — | — | — |\\n| eval-acr-object-v3 | — | — | — | — |\\n\\n## 待处理\\n- eval-object-v6-full（准备中）\\n- eval-reconvla-spatial-v1（准备中）\\n- precompute-v4-shard2（准备中）\\n- precompute-v4-shard1（准备中）\\n- precompute-v4-shard0（准备中）\\n- eval-spatial-v4-full（准备中）\\n- precompute-v3-shard2（准备中）\\n- precompute-v3-shard1（准备中）\\n- precompute-v3-shard0（准备中）\\n- precompute-v2-shard2（准备中）\\n- …另有 2 项\\n\\n## 近期结论\\n- **eval-obs-only-spatial-v3** (killed): —\\n- **eval-scalar-unc-spatial-v2** (killed): —\\n- **eval-obs-only-spatial-v2** (failed): —\\n\\n## 趋势\\n成功 14 / 负向 0 / 失败 5 / 共 38\\nbest_epoch: 50 ↑（近 3 次 success）\\nbest_val_loss: 0.050501 ↓（近 3 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nbjb1-18228: 无 GPU 信息\\nbjb2-40593: 无 GPU 信息\\n\\n## 告警\\n- plan_001-crm-smolvla: 训练失败 — unknown\\n- plan_014-reconvla-baseline: 训练失败 — unknown\\n- eval-smolvla-libero-spatial: 训练失败 — unknown\\n- eval-spatial-reeval-v2: 已被终止 — unknown\\n- eval-spatial-v3-full: 已被终止 — unknown\\n- eval-object-v4-full: 已被终止 — unknown\\n- eval-spatial-v5-full: 已被终止 — unknown\\n- crm-train-v1: 已被终止 — unknown\\n- eval-reconvla-spatial-v2: 已被终止 — unknown\\n- eval-acr-spatial-v1: 已被终止 — unknown\\n- crm-train-a3-obs-only: 已被终止 — unknown\\n- eval-acr-vla-spatial-v1: 已被终止 — unknown\\n- eval-spatial-v6-full: 已被终止 — unknown\\n- eval-acr-spatial-v2: 已被终止 — unknown\\n- eval-object-v5-full: 已被终止 — unknown\\n- crm-train-a4-scalar-unc: 已被终止 — unknown\\n- eval-scalar-unc-spatial: 已被终止 — unknown\\n- eval-object-v7-full: 已被终止 — unknown\\n- crm-train-k5: 已被终止 — unknown\\n- eval-k5-spatial: 已被终止 — unknown\\n- eval-s
…[truncated 257 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 2368
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T18:14:21.676061+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-14 16:00 UTC | 更新原因: crm-train-k5 完成 + eval-k5-spatial 启动，竞品分析完成，CRM correction 退化现象确认\\n\\n## 核心方向\\nPer-DOF conformal statistics from multivariate CP on flow-matching VLA samples enable dimension-selective action correction. 详见 paper_framing.md。\\n\\n## 投稿目标\\n**ICLR 2027**（预计 DDL Sep-Oct 2026）。CoRL 2026 已放弃（D011）。\\n\\n## 当前进展\\n- **阶段**: Phase 2 — Spatial Eval 四路对比（ACR-VLA / SampleConsensus / Scalar-CRM / VLA-mean）\\n- **MVP**: PASS（plan_000, per-DOF > scalar > none 确认）\\n- **SFT Gate**: 30% baseline，决定继续（D015）\\n- **CRM 训练完成**: per-DOF val_loss=0.009, scalar_unc=0.008, obs_only=0.018（conformal features 2× 改善确认）\\n- **Baselines 锁定**: spatial 30% (K=1), object 13% (K=1)\\n- **早期信号（2/10 tasks，不构成结论）**: ACR-VLA 在简单任务上低于 baseline，per-DOF CRM 可能在简单任务上引入有害 correction\\n- **竞品分析完成** (art_20260514_621600): 核心竞品 ReconVLA（最直接）、SC-VLA、VLA-Pilot、ACoT-VLA\\n- **CRM correction 退化现象**: ACR-VLA 中间结果 (23-26%) 低于 baseline (30%)，SampleConsensus 领先 (42.9%)\\n- **文献调研完成** (art_20260514_d21dd2): correction degradation 可能原因与补救方向（correction clipping/gating 等）\\n\\n## 近期任务\\n- [ ] eval-acr-spatial-v2 完成 → 核心 claim 判定（ACR-VLA vs baseline 30%）\\n- [ ] eval-reconvla-spatial-v3 完成 → SampleConsensus 对比\\n- [ ] eval-scalar-unc-spatial 完成 → scalar vs per-DOF 最终裁决\\n- [x] crm-train-k5 完成 → K sensitivity ablation + eval-k5-spatial 已启动\\n- [ ] eval-k5-spatial 完成 → K=5 sensitivity ablation 结果\\n- [ ] eval-vla-mean-spatial 完成 → 隔离多采样平均贡献\\n- [x] 代码同步 bjb1→bjb2（evaluate.py + train_crm.py）— MD5 verified\\n- [ ] 完整 spatial 四路对比表出炉 → 决定是否铺 object benchmark\\n- [ ] paper_framing.md 更新竞品定位（SC-VLA, VLA-Pilot, ACoT-VLA SOTA）\\n\\n## SFT Gate\\nD015: 30% baseline 继续推进。核心关注相对提升，非绝对值。\\n\\n## GPU 预算\\n- bjb1-18228 (4× RTX 4090): eval-k5-spatial(cuda:0) + eval-acr(cuda:1) 
…[truncated 1734 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 1964
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-14T18:14:21.777581+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [{\"worker_id\": \"worker_monitor_bjb1-eval-progress_20260514T181345\", \"task_type\": \"monitor:bjb1-eval-progress\", \"project\": \"acr-vla-conformal-refinement\", \"status\": \"running\", \"started_at\": \"2026-05-14T18:13:45.683212+00:00\", \"ended_at\": null}, {\"worker_id\": \"worker_verify_bjb2-cache-and-training-status_20260514T181357\", \"task_type\": \"verify:bjb2-cache-and-training-status\", \"project\": \"acr-vla-conformal-refinement\", \"status\": \"running\", \"started_at\": \"2026-05-14T18:13:57.186785+00:00\", \"ended_at\": null}, {\"worker_id\": \"worker_verify_bjb1-eval-progress_20260514T181408\", \"task_type\": \"verify:bjb1-eval-progress\", \"project\": \"acr-vla-conformal-refinement\", \"status\": \"running\", \"started_at\": \"2026-05-14T18:14:09.253641+00:00\", \"ended_at\": null}, {\"worker_id\": \"worker_diagnose_bjb2-status_20260514T181415\", \"task_type\": \"diagnose:bjb2-status\", \"project\": \"acr-vla-conformal-refinement\", \"status\": \"running\", \"started_at\": \"2026-05-14T18:14:15.949757+00:00\", \"ended_at\": null}], \"count\": 4}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 1762
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-14T18:14:39.397550+00:00_

called mcp__agent-ml-research__list_workers

<details open><summary>🔧 Tool call — mcp__agent-ml-research__list_workers</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "status": "done",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__list_workers",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "status": "done",
    "limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-14T18:14:39.648955+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [{\"worker_id\": \"worker_code_fix-eval-obs-only-mode_20260514T124101\", \"task_type\": \"code:fix-eval-obs-only-mode\", \"project\": \"acr-vla-conformal-refinement\", \"status\": \"done\", \"started_at\": \"2026-05-14T12:41:01.482551+00:00\", \"ended_at\": \"2026-05-14T12:44:32.754768+00:00\"}, {\"worker_id\": \"worker_code_fix-eval-obs-only-crm-load_20260514T124633\", \"task_type\": \"code:fix-eval-obs-only-crm-load\", \"project\": \"acr-vla-conformal-refinement\", \"status\": \"done\", \"started_at\": \"2026-05-14T12:46:33.358538+00:00\", \"ended_at\": \"2026-05-14T12:50:33.001669+00:00\"}, {\"worker_id\": \"worker_monitor_urgent-eval-status-bjb1_20260514T131552\", \"task_type\": \"monitor:urgent-eval-status-bjb1\", \"project\": \"acr-vla-conformal-refinement\", \"status\": \"done\", \"started_at\": \"2026-05-14T13:15:52.395632+00:00\", \"ended_at\": \"2026-05-14T13:17:04.371076+00:00\"}, {\"worker_id\": \"worker_monitor_urgent-eval-status-bjb2_20260514T131558\", \"task_type\": \"monitor:urgent-eval-status-bjb2\", \"project\": \"acr-vla-conformal-refinement\", \"status\": \"done\", \"started_at\": \"2026-05-14T13:15:58.810692+00:00\", \"ended_at\": \"2026-05-14T13:17:05.935553+00:00\"}, {\"worker_id\": \"worker_monitor_eval-progress-check-2_20260514T174213\", \"task_type\": \"monitor:eval-progress-check-2\", \"project\": \"acr-vla-conformal-refinement\", \"status\": \"done\", \"started_at\": \"2026-05-14T17:42:13.560605+00:00\", \"ended_at\": \"2026-05-14T17:44:12.340745+00:00\"}, {\"worker_id\": \"worker_research_add-missing-references_20260514T174223\", \"task_type\": \"research:add-missing-references\", \"project\": \"acr-vla-conformal-refinement\", \"status\": \"done\", \"started_at\": \"2026-05-14T17:42:23.827530+00:00\", \"ended_at\": \"2026-05-14T17:44:13.634571+00:00\"}, {\"worker_id\": \"worker_exec_kill-and-start-diagnostics_20260514T174719\", \"task_type\": \"exec:kill-and-start-diagnostics\", \"pr
…[truncated 1125 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 251
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-14T18:14:39.649382+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'PREPARING'}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'PREPARING'}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-14T18:14:39.851000+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"crm-train-v3-obs-only\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-14T18:05:02.939Z\", \"updated_at\": \"2026-05-14T18:05:02.939Z\"}, \"crm-train-v3-scalar-unc\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-14T18:05:00.968Z\", \"updated_at\": \"2026-05-14T18:05:00.968Z\"}, \"crm-train-v3-perdof\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-14T18:04:54.552Z\", \"updated_at\": \"2026-05-14T18:04:54.552Z\"}, \"eval-object-v6-full\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-13T23:28:33.119Z\", \"updated_at\": \"2026-05-13T23:29:33.175Z\", \"conclusion\": \"killed\"}, \"eval-reconvla-spatial-v1\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-13T20:15:35.450Z\", \"updated_at\": \"2026-05-13T22:59:43.788Z\", \"conclusion\": \"failed\"}, \"precompute-v4-shard2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-13T18:58:14.301Z\", \"updated_at\": \"2026-05-13T20:12:23.934Z\", \"conclusion\": \"success\"}, \"precompute-v4-shard1\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-13T18:58:12.183Z\", \"updated_at\": \"2026-05-13T20:07:53.062Z\", \"conclusion\": \"success\"}, \"precompute-v4-shard0\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-13T18:58:09.830Z\", \"updated_at\": \"2026-05-13T20:07:52.129Z\", \"conclusion\": \"success\"}, \"eval-spatial-v4-full\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-13T18:58:07.302Z\", \"updated_at\": \"2026-05-13T19:36:15.903Z\", \"conclusion\": \"failed\"}, \"precompute-v3-shard2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-13T17:39:04.708Z\", \"updated_at\": \"2026-05-13T18:46:54.558Z\", \"conclusion\": \"killed\"}, \"precompute-v3-shard1\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-13T17:39:02.628Z\", \"updated_at\": \"2026-05-13T18:46:53.324Z\", \"conclusion\": \"killed\"}, \"precompute-v3-shard0\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-13T17:39:0
…[truncated 725 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 201
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-14T18:14:58.205637+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__get_worker_status",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__get_worker_status",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-14T18:14:58.325809+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "ToolSearch",
  "elapsed_ms": 120
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-14T18:15:00.735037+00:00_

called mcp__agent-ml-research__get_worker_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_worker_status</summary>

```json
{
  "worker_id": "worker_verify_crm-v3-training-data_20260514T180836"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "tool_args": {
    "worker_id": "worker_verify_crm-v3-training-data_20260514T180836"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-14T18:15:01.169135+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_verify_crm-v3-training-data_20260514T180836\", \"status\": \"cancelled\", \"task_type\": \"verify:crm-v3-training-data\", \"project\": \"acr-vla-conformal-refinement\", \"started_at\": \"2026-05-14T18:08:36.673460+00:00\", \"ended_at\": \"2026-05-14T18:13:00.790017+00:00\", \"setup\": null, \"teardown\": null, \"setup_data\": {}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "elapsed_ms": 434
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-14T18:15:01.169578+00:00_

called mcp__agent-ml-research__get_worker_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_worker_status</summary>

```json
{
  "worker_id": "worker_monitor_bjb1-eval-progress_20260514T181345",
  "verbose": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "tool_args": {
    "worker_id": "worker_monitor_bjb1-eval-progress_20260514T181345",
    "verbose": "True"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-14T18:15:01.623745+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_monitor_bjb1-eval-progress_20260514T181345\", \"status\": \"running\", \"task_type\": \"monitor:bjb1-eval-progress\", \"project\": \"acr-vla-conformal-refinement\", \"started_at\": \"2026-05-14T18:13:45.683212+00:00\", \"ended_at\": null, \"setup\": null, \"teardown\": null, \"setup_data\": {}, \"progress\": {\"recent_tools\": [\"ssh_read_only\", \"ssh_read_only\", \"ssh_read_only\", \"ssh_read_only\", \"ssh_read_only\"], \"last_text\": \"Let me check if the main experiments are still actively computing (GPU 0 is only at 11%).\", \"turn_count\": 19}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "elapsed_ms": 454
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-14T18:15:02.127352+00:00_

called mcp__agent-ml-research__get_worker_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_worker_status</summary>

```json
{
  "worker_id": "worker_verify_bjb2-cache-and-training-status_20260514T181357",
  "verbose": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "tool_args": {
    "worker_id": "worker_verify_bjb2-cache-and-training-status_20260514T181357",
    "verbose": "True"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-14T18:15:02.580652+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_verify_bjb2-cache-and-training-status_20260514T181357\", \"status\": \"running\", \"task_type\": \"verify:bjb2-cache-and-training-status\", \"project\": \"acr-vla-conformal-refinement\", \"started_at\": \"2026-05-14T18:13:57.186785+00:00\", \"ended_at\": null, \"setup\": null, \"teardown\": null, \"setup_data\": {}, \"progress\": {\"recent_tools\": [\"ssh_read_only\", \"ssh_read_only\", \"ssh_read_only\", \"ssh_read_only\", \"ToolSearch\"], \"last_text\": \"manifest.json 关键信息已获取：**`action_dim: 6`**。\\n\\n需要用 ssh_execute 来运行 python 检查 tensor shape（read_only 不允许分号）。\", \"turn_count\": 23}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "elapsed_ms": 453
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-14T18:15:02.581055+00:00_

called mcp__agent-ml-research__get_worker_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_worker_status</summary>

```json
{
  "worker_id": "worker_verify_bjb1-eval-progress_20260514T181408",
  "verbose": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "tool_args": {
    "worker_id": "worker_verify_bjb1-eval-progress_20260514T181408",
    "verbose": "True"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-14T18:15:02.877221+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_verify_bjb1-eval-progress_20260514T181408\", \"status\": \"running\", \"task_type\": \"verify:bjb1-eval-progress\", \"project\": \"acr-vla-conformal-refinement\", \"started_at\": \"2026-05-14T18:14:09.253641+00:00\", \"ended_at\": null, \"setup\": null, \"teardown\": null, \"setup_data\": {}, \"progress\": {\"recent_tools\": [\"ssh_read_only\", \"ssh_read_only\", \"ssh_read_only\", \"ssh_read_only\", \"ssh_read_only\"], \"last_text\": \"4 个进程全部存活。现在查看日志进度。\", \"turn_count\": 9}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "elapsed_ms": 296
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-14T18:15:02.940460+00:00_

called mcp__agent-ml-research__get_worker_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_worker_status</summary>

```json
{
  "worker_id": "worker_diagnose_bjb2-status_20260514T181415",
  "verbose": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "tool_args": {
    "worker_id": "worker_diagnose_bjb2-status_20260514T181415",
    "verbose": "True"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-14T18:15:03.111736+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_diagnose_bjb2-status_20260514T181415\", \"status\": \"running\", \"task_type\": \"diagnose:bjb2-status\", \"project\": \"acr-vla-conformal-refinement\", \"started_at\": \"2026-05-14T18:14:15.949757+00:00\", \"ended_at\": null, \"setup\": null, \"teardown\": null, \"setup_data\": {}, \"progress\": {\"recent_tools\": [\"ssh_read_only\", \"ssh_read_only\", \"ssh_read_only\", \"ssh_read_only\", \"ssh_read_only\"], \"last_text\": \"4 个进程全部存活，GPU 占用 4011/24564 MiB，利用率 96%。继续查日志。\", \"turn_count\": 12}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "elapsed_ms": 171
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-14T18:15:22.333542+00:00_

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
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/skills/resource-saturation.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-14T18:15:22.434513+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/sessions/agent_f7022f78.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-14T18:15:27.321813+00:00_

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
  "session": "cron:hook:precompute-v4-shard2",
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

_source line 33 · 2026-05-14T18:15:27.424409+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Glob",
  "elapsed_ms": 102
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-14T18:15:34.549715+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/skills/**/resource*",
  "path": "/home/ubuntu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/skills/**/resource*",
    "path": "/home/ubuntu"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-14T18:15:36.255705+00:00_

/home/ubuntu/agent-ml-research/skills/global/resource-saturation.skill.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Glob",
  "elapsed_ms": 1705
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-14T18:15:40.274117+00:00_

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
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/resource-saturation.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-14T18:15:40.325047+00:00_

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
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-14T18:16:12.231974+00:00_

called mcp__agent-ml-research__main_agent_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__main_agent_post_to_director</summary>

```json
{
  "text": "[资源] GPU 分配 5 / 实际在跑 5 | Worker 池 4 (GPU 0 / CPU 4)\n\n**Session #4 启动汇报**\n\n**实验状态**:\n- 5 路 eval 全部 RUNNING，cron 监控正常\n  - eval-acr-spatial-v3 (bjb1 cuda:0) — CRM v2 核心 claim 基线\n  - eval-argmin-only-spatial (bjb1 cuda:1) — 诊断：隔离 argmin 选择\n  - eval-tiny-correction-spatial (bjb1 cuda:2) — 诊断：极小 correction 验证\n  - eval-acr-object-v3 (bjb1 cuda:3) — object 泛化验证\n  - eval-vla-mean-spatial (bjb2 cuda:0) — K=10 mean baseline\n\n**CRM v3 进展**:\n- 代码实现完成（worker_code_crm-normalization-and-retrain, 18:07 done）\n- 训练数据验证 worker 被 cancelled（18:13），但当前 worker_verify_bjb2-cache-and-training-status（23 turns, still running）正在检查 training data manifest/shape，可能覆盖此验证\n- crm-train-v3-perdof / scalar-unc / obs-only 三组 PREPARING，等 GPU 释放 + 验证通过\n\n**待处理**: 等 worker 回调确认 CRM v3 训练数据 normalization 验证结果，以及 eval 进度。5 张 GPU 满跑，无空闲。",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "tool_args": {
    "text": "[资源] GPU 分配 5 / 实际在跑 5 | Worker 池 4 (GPU 0 / CPU 4)\n\n**Session #4 启动汇报**\n\n**实验状态**:\n- 5 路 eval 全部 RUNNING，cron 监控正常\n  - eval-acr-spatial-v3 (bjb1 cuda:0) — CRM v2 核心 claim 基线\n  - eval-argmin-only-spatial (bjb1 cuda:1) — 诊断：隔离 argmin 选择\n  - eval-tiny-correction-spatial (bjb1 cuda:2) — 诊断：极小 correction 验证\n  - eval-acr-object-v3 (bjb1 cuda:3) — object 泛化验证\n  - eval-vla-mean-spatial (bjb2 cuda:0) — K=10 mean baseline\n\n**CRM v3 进展**:\n- 代码实现完成（worker_code_crm-normalization-and-retrain, 18:07 done）\n- 训练数据验证 worker 被 cancelled（18:13），但当前 worker_verify_bjb2-cache-and-training-status（23 turns, still running）正在检查 training data manifest/shape，可能覆盖此验证\n- crm-train-v3-perdof / scalar-unc / obs-only 三组 PREPARING，等 GPU 释放 + 验证通过\n\n**待处理**: 等 worker 回调确认 CRM v3 训练数据 normalization 验证结果，以及 eval 进度。5 张 GPU 满跑，无空闲。",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-14T18:16:16.058687+00:00_

{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_5ee1fd6fcd3e57fe38e03d67d16d0bf4:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "elapsed_ms": 3826
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-14T18:16:27.181660+00:00_

Session #4 初始化完成。

**当前资源饱和状态**:
- GPU: 5/5 满跑（5 路 eval）
- Worker: 4 个 CPU 监控/验证任务活跃
- Cron: 5 个 eval 监控已同步

**关键等待项**:
1. 4 个 worker 回调（eval 进度监控 + CRM v3 数据验证）
2. Cron 回调（任一 eval 完成 → 释放 GPU → 提交 CRM v3 训练）

已向 Director 汇报。等待 worker/cron 回调推进下一步。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:precompute-v4-shard2"
}
```

</details>

---

## Round 2

58 recorded events

### User

_source line 41 · 2026-05-14T21:20:28.280093+00:00_

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
  "session": "cron:hook:precompute-v4-shard2",
  "source": "system:ralph_loop"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-14T21:20:52.417323+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Read project state files",
  "subagent_type": "Explore",
  "prompt": "I need to understand the current state of the project \"acr-vla-conformal-refinement\". Please find and read these files:\n\n1. Any registry.yaml or registry file in the project directory /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/\n2. report.md in the same project directory\n3. ROADMAP.md in the same project directory\n4. memory.md in the same project directory\n5. experiment_plan.yaml in the same project directory\n6. paper_framing.md in the same project directory\n\nAlso check for any artifacts/ directory contents and any .claude/sessions/ state files.\n\nRead as much of each file as possible. Report the full contents of each file found."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Agent",
  "tool_args": {
    "description": "Read project state files",
    "subagent_type": "Explore",
    "prompt": "I need to understand the current state of the project \"acr-vla-conformal-refinement\". Please find and read these files:\n\n1. Any registry.yaml or registry file in the project directory /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/\n2. report.md in the same project directory\n3. ROADMAP.md in the same project directory\n4. memory.md in the same project directory\n5. experiment_plan.yaml in the same project directory\n6. paper_framing.md in the same project directory\n\nAlso check for any artifacts/ directory contents and any .claude/sessions/ state files.\n\nRead as much of each file as possible. Report the full contents of each file found."
  }
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-14T21:20:53.072422+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-14T21:20:53.123320+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/chats/feishu_group_oc_5ee1fd6fcd3e57fe38e03d67d16d0bf4_director.lock
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/study_status.lock
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.lock
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/chats/feishu_group_oc_718f2ee7260b8649b47875a90c263a2a_reviewer.lock
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/decisions.lock
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/chats/feishu_group_oc_718f2ee7260b8649b47875a90c263a2a.lock
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.lock
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/checkpoints/mvp-point-reaching_PREPARING_20260513T012210.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/checkpoints/mvp-point-reaching_QUEUED_20260513T014344.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/checkpoints/mvp-point-reaching_RUNNING_20260513T014348.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/checkpoints/mvp-point-reaching_RUNNING_20260513T014355.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/checkpoints/mvp-point-reaching_DONE_20260513T014400.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/mvp-point-reaching/data/mvp_results.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_code_mvp-point-reaching_20260513T012320.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_code_
…[truncated 13090 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-14T21:20:54.335659+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement -type f -name \"registry*\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement -type f -name \"registry*\" 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-14T21:20:54.587910+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.lock

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Bash",
  "elapsed_ms": 252
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-14T21:20:56.845641+00:00_

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
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml"
  }
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-14T21:20:57.046651+00:00_

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
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-14T21:20:57.247767+00:00_

1	# Handover — 2026-05-14
2	
3	> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。
4	
5	## 运行中
6	| exp_id | 假设 | 状态 | 关键指标 | W&B |
7	|--------|------|------|---------|-----|
8	| crm-train-v3-norm-scalar-unc | Ablation: scalar_unc input mode (scalar uncertainty only) with normalization. Tests per-DOF vs scalar uncertainty contribution with proper normalization. | — | — | — |
9	| crm-train-v3-norm-obs-only | Ablation: obs_only input mode (no uncertainty features) with normalization. Isolates contribution of obs features vs conformal features. | — | — | — |
10	| eval-acr-spatial-v4-small | D018: Normalization + moderate correction scaling (max_correction_norm=0.1, 14x smaller than default). If v4-small > v4-default → magnitude control needed on top of normalization. | — | — | — |
11	
12	## 待处理
13	- eval-object-v6-full（准备中）
14	- eval-reconvla-spatial-v1（准备中）
15	- precompute-v4-shard2（准备中）
16	- precompute-v4-shard1（准备中）
17	- precompute-v4-shard0（准备中）
18	- eval-spatial-v4-full（准备中）
19	- precompute-v3-shard2（准备中）
20	- precompute-v3-shard1（准备中）
21	- precompute-v3-shard0（准备中）
22	- precompute-v2-shard2（准备中）
23	- …另有 2 项
24	
25	## 近期结论
26	- **eval-acr-object-v3** (failed): —
27	- **eval-acr-spatial-v3** (failed): —
28	- **crm-train-v3-norm** (success): D018: Input normalization fixes 1500x scale imbalance in CRM inputs, enabling proper gradient flow and meaningful per-DOF correction learning ← 基于 crm-train-v3-perdof
29	
30	## 趋势
31	成功 15 / 负向 0 / 失败 7 / 共 44
32	best_epoch: 50 ↑（近 3 次 success）
33	best_val_loss: 0.050501 ↓（近 3 次 success）
34	
35	## 下一步
36	（无活跃 idea，请通过 ideas.md 添加）
37	
38	## 资源状态
39	bjb1-18228: 无 GPU 信息
40	bjb2-40593: 无 GPU 信息
41	
42	## 告警
43	- plan_001-crm-smolvla: 训练失败 — unknown
44	- plan_014-reconvla-baseline: 训练失败 — unknown
45	- eval-smolvla-libero-spatial: 训练失败 — unknown
46	- eval-spatial-reeval-v2: 已被终止 — unknown
47	- eval-spatial-v3-full: 已被终止 — unknown
48	- eval-object-v4-full: 已被终止 — unknown
49	- eval-spatial-v5-full: 已被终止 — unknown
50	- crm-train-v1: 已被终止 — unknown
51	-
…[truncated 893 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-14T21:20:57.248308+00:00_

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
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-14T21:20:57.449944+00:00_

File content (31169 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "elapsed_ms": 604
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-14T21:20:57.450425+00:00_

1	# acr-vla-conformal-refinement — Research Dashboard
2	
3	> 最后更新: 2026-05-14 16:00 UTC | 更新原因: crm-train-k5 完成 + eval-k5-spatial 启动，竞品分析完成，CRM correction 退化现象确认
4	
5	## 核心方向
6	Per-DOF conformal statistics from multivariate CP on flow-matching VLA samples enable dimension-selective action correction. 详见 paper_framing.md。
7	
8	## 投稿目标
9	**ICLR 2027**（预计 DDL Sep-Oct 2026）。CoRL 2026 已放弃（D011）。
10	
11	## 当前进展
12	- **阶段**: Phase 2 — Spatial Eval 四路对比（ACR-VLA / SampleConsensus / Scalar-CRM / VLA-mean）
13	- **MVP**: PASS（plan_000, per-DOF > scalar > none 确认）
14	- **SFT Gate**: 30% baseline，决定继续（D015）
15	- **CRM 训练完成**: per-DOF val_loss=0.009, scalar_unc=0.008, obs_only=0.018（conformal features 2× 改善确认）
16	- **Baselines 锁定**: spatial 30% (K=1), object 13% (K=1)
17	- **早期信号（2/10 tasks，不构成结论）**: ACR-VLA 在简单任务上低于 baseline，per-DOF CRM 可能在简单任务上引入有害 correction
18	- **竞品分析完成** (art_20260514_621600): 核心竞品 ReconVLA（最直接）、SC-VLA、VLA-Pilot、ACoT-VLA
19	- **CRM correction 退化现象**: ACR-VLA 中间结果 (23-26%) 低于 baseline (30%)，SampleConsensus 领先 (42.9%)
20	- **文献调研完成** (art_20260514_d21dd2): correction degradation 可能原因与补救方向（correction clipping/gating 等）
21	
22	## 近期任务
23	- [ ] eval-acr-spatial-v2 完成 → 核心 claim 判定（ACR-VLA vs baseline 30%）
24	- [ ] eval-reconvla-spatial-v3 完成 → SampleConsensus 对比
25	- [ ] eval-scalar-unc-spatial 完成 → scalar vs per-DOF 最终裁决
26	- [x] crm-train-k5 完成 → K sensitivity ablation + eval-k5-spatial 已启动
27	- [ ] eval-k5-spatial 完成 → K=5 sensitivity ablation 结果
28	- [ ] eval-vla-mean-spatial 完成 → 隔离多采样平均贡献
29	- [x] 代码同步 bjb1→bjb2（evaluate.py + train_crm.py）— MD5 verified
30	- [ ] 完整 spatial 四路对比表出炉 → 决定是否铺 object benchmark
31	- [ ] paper_framing.md 更新竞品定位（SC-VLA, VLA-Pilot, ACoT-VLA SOTA）
32	
33	## SFT Gate
34	D015: 30% baseline 继续推进。核心关注相对提升，非绝对值。
35	
36	## GPU 预算
37	- bjb1-18228 (4× RTX 4090): eval-k5-spatial(cuda:0) + eval-acr(cuda:1) + eval-reconvla(cuda:2) + eval-scalar-unc(cuda:3)
38	- bjb2-40593 (1× RTX 4090 D): eval-vla-mean-spatial(cuda:0)
39	- 总预算 ~200 GPU·h, 已用 ~8
…[truncated 1563 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "elapsed_ms": 202
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-14T21:20:57.451663+00:00_

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
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-14T21:20:57.854087+00:00_

1	# Memory — acr-vla-conformal-refinement
2	
3	## Correction Magnitude 是核心问题（2026-05-14 18:15，早期信号）
4	
5	### 发现
6	eval-tiny-correction-spatial（max_correction_norm=0.05，约默认 1.42 的 1/28）在首个 task 上 4/5 成功，而 full ACR 同一 task 只有 1/10。这说明 CRM correction 的方向可能是对的，但幅度太大导致 compounding error。
7	
8	### 含义
9	- correction clipping / gating 是正确的补救方向
10	- Gated CRM 代码已就绪（`src/gated_crm.py` + `--mode acr_gated` + `--gate_threshold/mode/temperature`）
11	- 等完整 eval 结果确认后，下一步应该是 correction magnitude sweep（0.01, 0.05, 0.1, 0.2, 0.5）或 Gated CRM eval
12	- **不改变目标 venue（ICLR 2027）**，narrative 可从 "per-DOF correction always helps" 调整为 "per-DOF correction with magnitude control"
13	
14	### ⚠️ 注意
15	这是 1 个 task 的 5 个 rollout 的早期数据。需要完整 10 tasks 确认。
16	
17	## Correction Magnitude 文献支撑（2026-05-14 18:37）
18	
19	### 核心竞品/支撑论文
20	1. **PLD (ICLR 2026)**: scheduled ξ bound，LIBERO ξ=0.5 / SimplerEnv ξ=0.1——不同环境需不同 correction scale，完全验证我们的发现
21	2. **TRANSIC (CoRL 2024)**: 无 gate 时 fine-tuning 导致 model collapse——与我们 40%→2.5% 退化一致
22	3. **ResiP (CoRL-W 2024)**: scaling α≤1，关键不是精确值而是 order of magnitude
23	4. **DRC (2025)**: temporal decay of correction
24	5. **DAWN (2026)**: scale mismatch → residual 学不好
25	
26	### 独特贡献角度
27	**没有现有方法提供 per-DOF, per-timestep, calibrated magnitude bounds。** ACR-VLA 的 conformal intervals 天然提供 calibrated bounds on expected action range。
28	
29	### 推荐 Framing 调整方向
30	"Conformally-Calibrated Correction Magnitude" — CP intervals 作为 correction 幅度的自然上界，不依赖固定超参数（α, ξ）或 binary gate。
31	
32	### 对比表（可用于论文 Table 1）
33	| Method | Bound Type | Per-DOF | Per-Timestep | Calibrated |
34	|--------|-----------|---------|-------------|------------|
35	| Silver 2018 | Action space | ✗ | ✗ | ✗ |
36	| Johannink 2019 | Fixed tube | ✗ | ✗ | ✗ |
37	| TRANSIC 2024 | Binary gate | ✗ | ✓ | ✗ |
38	| PLD 2026 | Scheduled ξ | ✗ | ~ | ✗ |
39	| **ACR-VLA** | **CP intervals** | **✓** | **✓** | **✓** |
40	
41	## CRM v3-norm 训练结果（2026-05-14 20:06）
42	
43	### 结果
44	- best_val_loss=0.03578 (epoch 47/50)，收敛稳定
45
…[truncated 5423 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-14T21:20:57.854566+00:00_

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
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/experiment_plan.yaml"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-14T21:20:57.854880+00:00_

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
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-14T21:20:58.056686+00:00_

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
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-14T21:20:58.107405+00:00_

1	# Paper Framing — acr-vla-conformal-refinement
2	
3	## Target Venue
4	- **Primary: ICLR 2027** (expected deadline ~Sep-Oct 2026) — 充足时间
5	- ~~CoRL 2026~~ — 已放弃 (D011: GPU 未扩容 + 时间不足)
6	
7	## Core Insight
8	Per-DOF conformal statistics from multivariate CP on flow-matching VLA samples encode "which action dimensions are uncertain and how they co-vary" — fundamentally richer information than scalar uncertainty scores. A lightweight learned module conditioned on these structured features can perform dimension-selective action correction: aggressively correcting high-uncertainty DOFs while preserving confident predictions elsewhere.
9	
10	## Core Claims (3 条，均可证伪)
11	1. **Per-DOF conformal features enable dimension-selective correction**: CGS 提取的 40D 结构化 uncertainty 特征（per-DOF std + conformal radius + ellipsoid volume，action_dim=6, H_eff=5）比标量 uncertainty（ReconVLA 的 Euclidean distance）和无 uncertainty conditioning 的残差策略（A2C2 类）提供显著更好的 action correction。
12	   - 验证: MVP (✅ done) + A3 ablation (make-or-break) + A4 ablation + feature importance analysis
13	   - Kill criterion: A3 (CRM without conformal features) 与 full ACR-VLA 差距 <2% → claim 不成立
14	
15	2. **ACI+COC 在分布偏移下维持 calibrated uncertainty，无需外部监督**: Chunk Overlap Consistency 提供自参考覆盖信号，ACI 在线更新 conformal threshold，在任意分布偏移下维持长期平均覆盖保证。
16	   - 验证: COC-success Spearman ρ + ACI 收敛 + ellipsoid volume vs static
17	   - Kill criterion: Spearman ρ < 0.3 AND ellipsoid volume 无 >10% 收窄 → fallback to episode-level ACI
18	
19	3. **ACR-VLA 与 training-time 方法正交互补**: 作为 inference-time 模块可叠加在 SRPO (82.1% LIBERO-Plus SOTA) 上进一步提升。
20	   - 验证: ACR-VLA + SRPO > SRPO alone
21	   - Kill criterion: stacking gain < 2% → claim 降级为"complementary in principle"
22	
23	## Story Spine
24	- **Problem**: Flow-matching VLAs 在标准 benchmark 上接近饱和(97-99%)，但 LIBERO-Plus 暴露了分布偏移下的灾难性鲁棒性缺口。现有方法分别解决检测(SAFE)、样本选择(ReconVLA)、训练时增强(RobustVLA/DiG-Flow/SRPO)，但没有方法在推理时利用结构化 uncertainty 信息主动校正动作。
25	- **Gap**: 现有 inference-time 方法各有根本性局限：ReconVLA 用标量 CQR 做样本选择——丢弃
…[truncated 4235 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-14T21:21:01.423437+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "limit": "500",
  "offset": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
    "limit": "500",
    "offset": "0"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-14T21:21:01.474220+00:00_

0	baseline: null
1	experiments:
2	  mvp-point-reaching:
3	    status: DONE
4	    retry_count: 0
5	    created_at: '2026-05-13T01:22:10.415Z'
6	    updated_at: '2026-05-13T22:06:11.073Z'
7	    spec:
8	      hypothesis: Per-DOF uncertainty features carry more actionable information than
9	        scalar uncertainty summaries, enabling dimension-selective correction
10	      description: '3D point-reaching MVP: 3 MLP variants (scalar/per-DOF/no uncertainty)
11	        x 6 groups (3 anisotropy ratios x 2 uncertainty sources)'
12	      server: bjb2-40593
13	      gpu: cuda:0
14	      data_count: 20000
15	      model_name: CorrectionMLP(2-layer, 64-hidden)
16	      seed: 42
17	      command: python -u run_mvp.py
18	      data_path: synthetic (generated in-script)
19	      checkpoint_path: /root/acr-vla-conformal-refinement/mvp/
20	      log_path: /root/acr-vla-conformal-refinement/mvp/mvp_results.log
21	    conclusion: success
22	    completed_at: '2026-05-13T01:44:00.055Z'
23	    metrics:
24	      group1_oracle:
25	        A_scalar:
26	          mse_x: 0.180218
27	          mse_y: 0.02497
28	          mse_z: 0.024232
29	          total: 0.076473
30	        B_perDOF:
31	          mse_x: 0.172652
32	          mse_y: 0.015544
33	          mse_z: 0.01561
34	          total: 0.067935
35	        C_none:
36	          mse_x: 0.22706
37	          mse_y: 0.025542
38	          mse_z: 0.024753
39	          total: 0.092451
40	      group2_oracle:
41	        A_scalar:
42	          mse_x: 0.064642
43	          mse_y: 0.023836
44	          mse_z: 0.022967
45	          total: 0.037148
46	        B_perDOF:
47	          mse_x: 0.053403
48	          mse_y: 0.015695
49	          mse_z: 0.01573
50	          total: 0.028276
51	        C_none:
52	          mse_x: 0.084178
53	          mse_y: 0.025427
54	          mse_z: 0.024798
55	          total: 0.044801
56	      group3_oracle:
57	        A_scalar:
58	          mse_x: 0.042948
59	          mse_y: 0.023218
60	          mse_z: 0.022365
61	    
…[truncated 18490 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-14T21:21:01.876939+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts -type f 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts -type f 2>/dev/null | head -20"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-14T21:21:02.179486+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/precompute-k5-analysis.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/report_eval_progress.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/crm_bug_audit.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/introduction_c83872.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/references.bib
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/references_e9d4d2.bib
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/related_work_9c2927.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/method_section_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/experiments_c64a8c.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/norm_stats_v3_summary.txt
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/crm_bug_audit.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/competitor_analysis.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vl
…[truncated 632 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Bash",
  "elapsed_ms": 302
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-14T21:21:02.280219+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -lah /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/sessions/ 2>/dev/null | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -lah /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/sessions/ 2>/dev/null | head -30"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-14T21:21:02.381588+00:00_

total 84K
drwxr-xr-x 21 ubuntu ubuntu 4.0K May 14 20:18 .
drwxr-xr-x  3 ubuntu ubuntu 4.0K May 13 01:01 ..
drwxr-xr-x  2 ubuntu ubuntu 4.0K May 13 22:09 agent_0ccb089b
drwxr-xr-x  2 ubuntu ubuntu 4.0K May 13 23:31 agent_127bc435
drwxr-xr-x  2 ubuntu ubuntu 4.0K May 13 20:04 agent_327cd2f3
drwxr-xr-x  2 ubuntu ubuntu 4.0K May 14 20:18 agent_5301263f
drwxr-xr-x  2 ubuntu ubuntu 4.0K May 13 23:34 agent_64c9cd7c
drwxr-xr-x  2 ubuntu ubuntu 4.0K May 14 20:18 agent_699cc919
drwxr-xr-x  2 ubuntu ubuntu 4.0K May 13 20:26 agent_6a074051
drwxr-xr-x  2 ubuntu ubuntu 4.0K May 14 18:27 agent_721032b8
drwxr-xr-x  2 ubuntu ubuntu 4.0K May 14 18:27 agent_7b8c0fb2
drwxr-xr-x  2 ubuntu ubuntu 4.0K May 13 23:43 agent_84a6ef31
drwxr-xr-x  2 ubuntu ubuntu 4.0K May 13 22:40 agent_9c7d426f
drwxr-xr-x  2 ubuntu ubuntu 4.0K May 14 18:27 agent_9de5c916
drwxr-xr-x  2 ubuntu ubuntu 4.0K May 13 01:21 agent_bbd03d76
drwxr-xr-x  2 ubuntu ubuntu 4.0K May 13 23:34 agent_cdef8c2a
drwxr-xr-x  2 ubuntu ubuntu 4.0K May 14 04:12 agent_e215d0eb
drwxr-xr-x  2 ubuntu ubuntu 4.0K May 13 20:09 agent_f7022f78
drwxr-xr-x  2 ubuntu ubuntu 4.0K May 13 01:01 director_c68f3c17
drwxr-xr-x  3 ubuntu ubuntu 4.0K May 13 03:54 paper_agent_f11cbd51
drwxr-xr-x  2 ubuntu ubuntu 4.0K May 13 01:03 reviewer_4966e04b

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-14T21:21:08.725974+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "limit": "500",
  "offset": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
    "limit": "500",
    "offset": "500"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-14T21:21:09.028469+00:00_

500	    created_at: '2026-05-13T18:58:09.830Z'
501	    updated_at: '2026-05-13T20:07:52.129Z'
502	    spec:
503	      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
504	        base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1
505	        && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task
506	        10 --shard_id 0 --num_shards 3 --seed 42 --K 10 --cache_dir /root/autodl-tmp/crm_cache/
507	        2>&1"
508	      server: bjb1-18228
509	      gpu:
510	      - cuda:1
511	      pid: '69647'
512	      log_path: ~/runs/acr-vla-conformal-refinement/precompute-v4-shard0.log
513	      submitted_at: '2026-05-13T18:58:09.802Z'
514	      submitted_via: submit_training_job
515	      backend: tmux
516	      account: root
517	      checkpoint_path: /root/autodl-tmp/crm_cache/
518	    reproduce:
519	      finished_at: '2026-05-13T20:04:45.258Z'
520	    extra:
521	      hook_events:
522	      - event: on_complete
523	        action: agent
524	        ts: '2026-05-13T20:04:50.222546+00:00'
525	    conclusion: success
526	  precompute-v4-shard1:
527	    status: PREPARING
528	    retry_count: 0
529	    created_at: '2026-05-13T18:58:12.183Z'
530	    updated_at: '2026-05-13T20:07:53.062Z'
531	    spec:
532	      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
533	        base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1
534	        && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task
535	        10 --shard_id 1 --num_shards 3 --seed 42 --K 10 --cache_dir /root/autodl-tmp/crm_cache/
536	        2>&1"
537	      server: bjb1-18228
538	      gpu:
539	      - cuda:2
540	      pid: '69793'
541	      log_path: ~/runs/acr-vla-conformal-refinement/precompute-v4-shard1.log
542	      submitted_at: '2026-05-13T18:58:12.154Z'
543	      submitted_via: submit_trai
…[truncated 19526 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-14T21:21:09.028921+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/report_eval_progress.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/report_eval_progress.md"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-14T21:21:09.181552+00:00_

1	# Eval 进度检查 — 2026-05-14 02:17 UTC
2	
3	## 各实验状态
4	
5	| exp_id | server | GPU | PID alive? | tasks done/total | 当前成功率 | 最新 log 摘要 | 预计剩余时间 |
6	|--------|--------|-----|-----------|-----------------|-----------|--------------|-------------|
7	| eval-vla-mean-spatial | bjb2 | cuda:0 (4090D) | ✅ 143106, 15.1h | 7.5/10 | 28/70 = 40.0% | task 8 rollout 5/10, 0/5 | ~5h |
8	| eval-acr-spatial-v3 | bjb1 | cuda:0 (4090) | ✅ 197062, 6h | 4/10 | 1/40 = 2.5% | 完成 task 4, 正跑 task 5 | ~9h |
9	| eval-acr-object-v3 | bjb1 | cuda:3 (4090) | ✅ 197803, 6h | 4/10 | 0/40 = 0.0% | 完成 task 4, 正跑 task 5 | ~9h |
10	| eval-argmin-only-spatial | bjb1 | cuda:1 (4090) | ✅ 231426, 29min | 0/10 | — | task 1 运行中, 无 rollout 输出 | ~14h |
11	| eval-tiny-correction-spatial | bjb1 | cuda:2 (4090) | ✅ 232820, 28min | 0.5/10 | task1: 4/5 | task 1 rollout 5/10 | ~9h |
12	
13	### 各 task 成功率明细
14	
15	**eval-vla-mean-spatial** (vla_only, baseline_mode=mean, spatial):
16	| task | success |
17	|------|---------|
18	| bowl_between_plate_ramekin → plate | 7/10 (70%) |
19	| bowl_next_to_ramekin → plate | 10/10 (100%) |
20	| bowl_from_table_center → plate | 0/10 (0%) |
21	| bowl_on_cookie_box → plate | 3/10 (30%) |
22	| bowl_in_top_drawer → plate | 0/10 (0%) |
23	| bowl_on_ramekin → plate | 0/10 (0%) |
24	| bowl_next_to_cookie_box → plate | 8/10 (80%) |
25	| bowl_on_stove → plate | running (0/5 so far) |
26	
27	**eval-acr-spatial-v3** (acr_vla, crm_v2/perdof, spatial):
28	| task | success |
29	|------|---------|
30	| bowl_between_plate_ramekin → plate | 1/10 (10%) |
31	| bowl_next_to_ramekin → plate | 0/10 (0%) |
32	| bowl_from_table_center → plate | 0/10 (0%) |
33	| bowl_on_cookie_box → plate | 0/10 (0%) |
34	
35	**eval-acr-object-v3** (acr_vla, crm_v2/perdof, object):
36	| task | success |
37	|------|---------|
38	| alphabet_soup → basket | 0/10 (0%) |
39	| cream_cheese → basket | 0/10 (0%) |
40	| salad_dressing → basket | 0/10 (0%) |
41	| bbq_sauce → basket | 0/10 (0%) |
42	
43	**eval-tiny-correction-spatial**
…[truncated 1960 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "elapsed_ms": 152
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-14T21:21:09.182039+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/claim-strength-analysis.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/claim-strength-analysis.md"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-14T21:21:09.232614+00:00_

1	# Claim Strength Analysis — 2026-05-13 21:00 UTC
2	
3	## 1. 完整数据表
4	
5	### 1A. MVP — Point-Reaching Motivating Experiment (DONE ✅)
6	
7	| Condition | Aniso | Unc Source | Per-DOF (B) MSE | Scalar (A) MSE | None (C) MSE | B vs A Δ | B vs C Δ |
8	|-----------|-------|-----------|-----------------|----------------|--------------|----------|----------|
9	| Group 1   | 5:1   | Oracle    | 0.0679          | 0.0765         | 0.0925       | −11.2%   | −26.5%   |
10	| Group 2   | 2:1   | Oracle    | 0.0283          | 0.0371         | 0.0448       | −23.9%   | −36.9%   |
11	| Group 3   | 1.5:1 | Oracle    | 0.0214          | 0.0295         | 0.0344       | −27.4%   | −37.8%   |
12	| Group 4   | 5:1   | K=10 Est  | 0.0735          | 0.0788         | 0.0882       | −6.7%    | −16.7%   |
13	| Group 5   | 2:1   | K=10 Est  | 0.0320          | 0.0375         | 0.0422       | −14.7%   | −24.2%   |
14	| Group 6   | 1.5:1 | K=10 Est  | 0.0245          | 0.0295         | 0.0326       | −16.9%   | −24.8%   |
15	
16	**Key takeaways:**
17	- Per-DOF 在所有 6 个条件下一致优于 scalar 和 none
18	- Oracle→K=10 估计衰减约 5-15pp（Group 1→4: 11.2%→6.7%），但 B>A>C 排序不变
19	- 弱各向异性 (1.5:1) 下 per-DOF 优势反而更大（27.4% oracle, 16.9% K=10）
20	- **结论: MVP PASS — 核心假设初步验证**
21	
22	### 1B. eval-spatial-v5-full — SmolVLA Baseline (RUNNING 🔄, 2/10 tasks)
23	
24	| Task | Success Rate | n |
25	|------|-------------|---|
26	| pick_up_bowl_between_plate_and_ramekin → plate | **90%** | 9/10 |
27	| pick_up_bowl_next_to_ramekin → plate | **80%** | 8/10 |
28	| pick_up_bowl_from_table_center → plate | ⏳ 0/5 (进行中) | — |
29	| Tasks 4-10 | ⏳ 未开始 | — |
30	
31	- **部分均值 (2 tasks): 85%** — 但仅 2/10 tasks，Task 3 目前 0/5
32	- SmolVLA 论文报告 libero_spatial 78-85%（20 rollouts）
33	- 如果 Task 3+ 拉低均值，最终可能在 50-80% 区间
34	
35	### 1C. eval-reconvla-spatial-v2 — ReconVLA Baseline (RUNNING 🔄, 2/10 tasks)
36	
37	| Task | Success Rate | n |
38	|------|-------------|---|
39	| pick_up_bowl_between_plate_and_ramekin → plate | **90%** | 9/10 |
40	| pick_up_bowl_next
…[truncated 6351 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-14T21:21:12.351106+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "limit": "500",
  "offset": "1000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
    "limit": "500",
    "offset": "1000"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-14T21:21:12.502309+00:00_

1000	    retry_count: 0
1001	    created_at: '2026-05-13T23:28:33.119Z'
1002	    updated_at: '2026-05-13T23:29:33.175Z'
1003	    spec:
1004	      data_path: /root/autodl-tmp/libero_data/ (object)
1005	      data_count: 100
1006	      model_name: lerobot/smolvla_libero
1007	      seed: 42
1008	      hypothesis: SmolVLA baseline success rate on libero_object with fixed evaluate.py
1009	        (env.reset bug removed, 5-step zero-action stabilization)
1010	      checkpoint_source: lerobot/smolvla_libero
1011	      eval_data: libero_object 10 tasks x 10 rollouts
1012	    conclusion: killed
1013	  crm-train-a4-scalar-unc:
1014	    status: DONE
1015	    retry_count: 0
1016	    created_at: '2026-05-13T23:48:40.837Z'
1017	    updated_at: '2026-05-14T07:59:32.676Z'
1018	    spec:
1019	      command: CUDA_VISIBLE_DEVICES=3 python -u src/train_crm.py --benchmark spatial
1020	        object --epochs 50 --batch_size 32 --lr 0.001 --K 10 --seed 42 --input_mode
1021	        scalar_unc --output_dir /root/autodl-tmp/checkpoints/crm/scalar_unc/
1022	      server: bjb1-18228
1023	      gpu:
1024	      - cuda:3
1025	      pid: '121984'
1026	      data_path: /root/autodl-tmp/crm_cache/
1027	      data_count: 26737
1028	      model_name: CRM-scalar_unc (3D scalar uncertainty)
1029	      seed: 42
1030	      hypothesis: CRM with scalar Euclidean uncertainty (3D) performs worse than per-DOF
1031	        (40D), validating per-DOF advantage. Ablation A4, hyperparams matched to plan_001
1032	        (bs=32/lr=1e-3).
1033	      log_path: /root/autodl-tmp/checkpoints/crm/scalar_unc/train.log
1034	      checkpoint_path: /root/autodl-tmp/checkpoints/crm/scalar_unc/crm_best.pt
1035	      conclusion_note: Training converged. scalar val_loss 0.008379 < per-DOF 0.009046
1036	        — original hypothesis (scalar worse) NOT confirmed on val_loss. Hypothesis
1037	        pending eval-scalar-unc-spatial task success rate validation.
1038	    conclusion: killed
1039	    checkpoint_path: /root/autodl-tmp/c
…[truncated 21065 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-14T21:21:12.553518+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "limit": "500",
  "offset": "1500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
    "limit": "500",
    "offset": "1500"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-14T21:21:12.554168+00:00_

1500	        VLA K=1 (30%) and SampleConsensus (34%) on LIBERO spatial. CORE CLAIM experiment.
1501	      checkpoint_source: /root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt
1502	      eval_data: LIBERO spatial 10 tasks x 10 rollouts
1503	      wall_clock_seconds: 28899.4
1504	      gpu_hours: 8.03
1505	    metrics:
1506	      tasks_done: 4/10
1507	      overall_success_rate: 0.025
1508	      total_successes: 1
1509	      total_rollouts: 40
1510	      per_task_partial:
1511	        pick_up_black_bowl_between_plate_and_ramekin: 0.1
1512	        pick_up_black_bowl_next_to_ramekin: 0
1513	        pick_up_black_bowl_from_table_center: 0
1514	        pick_up_black_bowl_on_cookie_box: 0
1515	      snapshot_time: 2026-05-14T18:15Z
1516	    conclusion: failed
1517	    reproduce:
1518	      finished_at: '2026-05-14T20:18:44.725Z'
1519	    failure_reason: process dead 5× with no sentinel/W&B — auto-resolved as failed
1520	    completed_at: '2026-05-14T20:18:45.380Z'
1521	    extra:
1522	      hook_events:
1523	      - event: on_failed
1524	        action: agent
1525	        ts: '2026-05-14T20:18:46.631294+00:00'
1526	  eval-scalar-unc-spatial-v2:
1527	    status: DONE
1528	    retry_count: 0
1529	    created_at: '2026-05-14T12:17:08.413Z'
1530	    updated_at: '2026-05-14T17:47:53.188Z'
1531	    spec:
1532	      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
1533	        base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl
1534	        MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode crm_scalar --benchmark
1535	        spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/scalar_unc/crm_best.pt"
1536	      server: bjb1-18228
1537	      gpu:
1538	      - cuda:1
1539	      pid: '197324'
1540	      log_path: ~/runs/acr-vla-conformal-refinement/eval-scalar-unc-spatial-v2.log
1541	      submitted_at: '2026-05-14T12:17:08.325Z'
1542	      submitted_via: submit_tr
…[truncated 21394 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-14T21:21:47.292315+00:00_

Perfect! I now have a comprehensive view of the project. Let me compile the full state report for you.

## Project State Summary: acr-vla-conformal-refinement

### Project Overview
This is a research project focused on **Per-DOF Conformal Action Refinement for VLAs (ACR-VLA)** — using multivariate conformal statistics from flow-matching VLA samples to enable dimension-selective action correction on LIBERO benchmarks. Target venue: ICLR 2027 (Sep-Oct 2026 deadline).

---

### Core Research Direction
- **Main Idea**: Per-DOF conformal statistics from multivariate CP on flow-matching VLA samples enable learned correction modules to selectively correct uncertain action dimensions while preserving confident predictions.
- **Hypothesis Structure**: 3 core claims
  1. Per-DOF conformal features > scalar uncertainty > no uncertainty for action correction
  2. ACI+COC (Adaptive Conformal Intervals + Chunk Overlap Consistency) maintains calibrated uncertainty under distribution shift
  3. ACR-VLA stacks orthogonally on training-time methods (e.g., SRPO)

---

### Current Phase & Progress
**Phase 2: Spatial Eval (4-way comparison)**
- MVP (plan_000): ✅ PASS — Per-DOF > scalar > none on synthetic 3D point-reaching (6 conditions)
- Baseline locked: 30% spatial (K=1), 13% object (K=1)
- CRM training: ✅ Multiple versions trained with varying fixes
- Baselines: ReconVLA renamed "SampleConsensus" (34% spatial), VLA mean evaluated

---

### Critical Recent Findings (as of 2026-05-14 20:00 UTC)

**🔴 CORE PROBLEM IDENTIFIED: Correction Magnitude is Critical**
- **eval-acr-spatial-v3** (full ACR): 2.5% success (1/40 on 4 tasks) vs baseline 30% — **catastrophic degradation**
- **eval-tiny-correction-spatial** (max_norm=0.05, 28x smaller): 4/5 success on task 1 vs 1/10 for full ACR — **correction magnitude is the culprit, not direction**
- Memory note documents: Correction clipping/gating is correct supplementary direction; narrative reframe needed from "per-DOF always helps" → "per-DOF c
…[truncated 5739 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Agent",
  "elapsed_ms": 54874
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-14T21:21:51.197698+00:00_

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
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md"
  }
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-14T21:21:51.198080+00:00_

1	# Handover — 2026-05-14
2	
3	> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。
4	
5	## 运行中
6	| exp_id | 假设 | 状态 | 关键指标 | W&B |
7	|--------|------|------|---------|-----|
8	| crm-train-v3-norm-scalar-unc | Ablation: scalar_unc input mode (scalar uncertainty only) with normalization. Tests per-DOF vs scalar uncertainty contribution with proper normalization. | — | — | — |
9	| crm-train-v3-norm-obs-only | Ablation: obs_only input mode (no uncertainty features) with normalization. Isolates contribution of obs features vs conformal features. | — | — | — |
10	| eval-acr-spatial-v4-small | D018: Normalization + moderate correction scaling (max_correction_norm=0.1, 14x smaller than default). If v4-small > v4-default → magnitude control needed on top of normalization. | — | — | — |
11	
12	## 待处理
13	- eval-object-v6-full（准备中）
14	- eval-reconvla-spatial-v1（准备中）
15	- precompute-v4-shard2（准备中）
16	- precompute-v4-shard1（准备中）
17	- precompute-v4-shard0（准备中）
18	- eval-spatial-v4-full（准备中）
19	- precompute-v3-shard2（准备中）
20	- precompute-v3-shard1（准备中）
21	- precompute-v3-shard0（准备中）
22	- precompute-v2-shard2（准备中）
23	- …另有 2 项
24	
25	## 近期结论
26	- **eval-acr-object-v3** (failed): —
27	- **eval-acr-spatial-v3** (failed): —
28	- **crm-train-v3-norm** (success): D018: Input normalization fixes 1500x scale imbalance in CRM inputs, enabling proper gradient flow and meaningful per-DOF correction learning ← 基于 crm-train-v3-perdof
29	
30	## 趋势
31	成功 15 / 负向 0 / 失败 7 / 共 44
32	best_epoch: 50 ↑（近 3 次 success）
33	best_val_loss: 0.050501 ↓（近 3 次 success）
34	
35	## 下一步
36	（无活跃 idea，请通过 ideas.md 添加）
37	
38	## 资源状态
39	bjb1-18228: 无 GPU 信息
40	bjb2-40593: 无 GPU 信息
41	
42	## 告警
43	- plan_001-crm-smolvla: 训练失败 — unknown
44	- plan_014-reconvla-baseline: 训练失败 — unknown
45	- eval-smolvla-libero-spatial: 训练失败 — unknown
46	- eval-spatial-reeval-v2: 已被终止 — unknown
47	- eval-spatial-v3-full: 已被终止 — unknown
48	- eval-object-v4-full: 已被终止 — unknown
49	- eval-spatial-v5-full: 已被终止 — unknown
50	- crm-train-v1: 已被终止 — unknown
51	-
…[truncated 893 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-14T21:21:52.102096+00:00_

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
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md"
  }
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-14T21:21:52.453758+00:00_

1	# Memory — acr-vla-conformal-refinement
2	
3	## Correction Magnitude 是核心问题（2026-05-14 18:15，早期信号）
4	
5	### 发现
6	eval-tiny-correction-spatial（max_correction_norm=0.05，约默认 1.42 的 1/28）在首个 task 上 4/5 成功，而 full ACR 同一 task 只有 1/10。这说明 CRM correction 的方向可能是对的，但幅度太大导致 compounding error。
7	
8	### 含义
9	- correction clipping / gating 是正确的补救方向
10	- Gated CRM 代码已就绪（`src/gated_crm.py` + `--mode acr_gated` + `--gate_threshold/mode/temperature`）
11	- 等完整 eval 结果确认后，下一步应该是 correction magnitude sweep（0.01, 0.05, 0.1, 0.2, 0.5）或 Gated CRM eval
12	- **不改变目标 venue（ICLR 2027）**，narrative 可从 "per-DOF correction always helps" 调整为 "per-DOF correction with magnitude control"
13	
14	### ⚠️ 注意
15	这是 1 个 task 的 5 个 rollout 的早期数据。需要完整 10 tasks 确认。
16	
17	## Correction Magnitude 文献支撑（2026-05-14 18:37）
18	
19	### 核心竞品/支撑论文
20	1. **PLD (ICLR 2026)**: scheduled ξ bound，LIBERO ξ=0.5 / SimplerEnv ξ=0.1——不同环境需不同 correction scale，完全验证我们的发现
21	2. **TRANSIC (CoRL 2024)**: 无 gate 时 fine-tuning 导致 model collapse——与我们 40%→2.5% 退化一致
22	3. **ResiP (CoRL-W 2024)**: scaling α≤1，关键不是精确值而是 order of magnitude
23	4. **DRC (2025)**: temporal decay of correction
24	5. **DAWN (2026)**: scale mismatch → residual 学不好
25	
26	### 独特贡献角度
27	**没有现有方法提供 per-DOF, per-timestep, calibrated magnitude bounds。** ACR-VLA 的 conformal intervals 天然提供 calibrated bounds on expected action range。
28	
29	### 推荐 Framing 调整方向
30	"Conformally-Calibrated Correction Magnitude" — CP intervals 作为 correction 幅度的自然上界，不依赖固定超参数（α, ξ）或 binary gate。
31	
32	### 对比表（可用于论文 Table 1）
33	| Method | Bound Type | Per-DOF | Per-Timestep | Calibrated |
34	|--------|-----------|---------|-------------|------------|
35	| Silver 2018 | Action space | ✗ | ✗ | ✗ |
36	| Johannink 2019 | Fixed tube | ✗ | ✗ | ✗ |
37	| TRANSIC 2024 | Binary gate | ✗ | ✓ | ✗ |
38	| PLD 2026 | Scheduled ξ | ✗ | ~ | ✗ |
39	| **ACR-VLA** | **CP intervals** | **✓** | **✓** | **✓** |
40	
41	## CRM v3-norm 训练结果（2026-05-14 20:06）
42	
43	### 结果
44	- best_val_loss=0.03578 (epoch 47/50)，收敛稳定
45
…[truncated 5423 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-14T21:21:52.454577+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
    "limit": "200"
  }
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-14T21:21:52.506177+00:00_

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
…[truncated 4968 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 82 · 2026-05-14T21:21:57.974683+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "offset": "200",
  "limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
    "offset": "200",
    "limit": "500"
  }
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-14T21:21:58.327785+00:00_

200	      data_path: /root/autodl-tmp/libero_data/ (spatial)
201	      data_count: 10 tasks x 3 rollouts x 300 steps
202	      model_name: lerobot/smolvla_libero (450M, full fine-tuned on libero_spatial)
203	      seed: 42
204	      hypothesis: Validate smolvla_libero checkpoint with fixed wrapper (correct state
205	        repr, 256x256 images, 7D action) achieves >50% success on libero_spatial
206	      log_path: /tmp/eval_spatial_full.log
207	      checkpoint_source: lerobot/smolvla_libero (HuggingFace community checkpoint)
208	      failure_reason: 'smolvla_libero 0% on spatial - 6 wrapper bugs: image flip/size/normalization,
209	        state 6D→8D, state normalization, action denormalization all missing'
210	      checkpoint_path: N/A
211	    conclusion: failed
212	    completed_at: '2026-05-13T15:45:51.082Z'
213	  precompute-shard0:
214	    status: DONE
215	    retry_count: 0
216	    created_at: '2026-05-13T11:57:45.284Z'
217	    updated_at: '2026-05-13T15:26:05.433Z'
218	    spec:
219	      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
220	        base && cd /root/acr-vla-conformal-refinement && python -u src/train_crm.py
221	        --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id
222	        0 --num_shards 3 --seed 42 --K 10"
223	      server: bjb1-18228
224	      gpu:
225	      - cuda:1
226	      pid: '46966'
227	      log_path: ~/runs/acr-vla-conformal-refinement/precompute-shard0.log
228	      submitted_at: '2026-05-13T11:57:45.270Z'
229	      submitted_via: submit_training_job
230	      backend: tmux
231	      account: root
232	      checkpoint_path: /root/autodl-tmp/crm_cache/
233	      wall_clock_seconds: 12500.2
234	      gpu_hours: 3.47
235	    conclusion: success
236	    completed_at: '2026-05-13T15:26:05.433Z'
237	  precompute-shard1:
238	    status: DONE
239	    retry_count: 0
240	    created_at: '2026-05-13T11:57:46.669Z'
241	    updated_at: '2026-05-13T15:26:06.485Z'
242	    spec:

…[truncated 20103 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-14T21:21:58.478548+00:00_

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
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md"
  }
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-14T21:21:58.529238+00:00_

1	# acr-vla-conformal-refinement — Research Dashboard
2	
3	> 最后更新: 2026-05-14 16:00 UTC | 更新原因: crm-train-k5 完成 + eval-k5-spatial 启动，竞品分析完成，CRM correction 退化现象确认
4	
5	## 核心方向
6	Per-DOF conformal statistics from multivariate CP on flow-matching VLA samples enable dimension-selective action correction. 详见 paper_framing.md。
7	
8	## 投稿目标
9	**ICLR 2027**（预计 DDL Sep-Oct 2026）。CoRL 2026 已放弃（D011）。
10	
11	## 当前进展
12	- **阶段**: Phase 2 — Spatial Eval 四路对比（ACR-VLA / SampleConsensus / Scalar-CRM / VLA-mean）
13	- **MVP**: PASS（plan_000, per-DOF > scalar > none 确认）
14	- **SFT Gate**: 30% baseline，决定继续（D015）
15	- **CRM 训练完成**: per-DOF val_loss=0.009, scalar_unc=0.008, obs_only=0.018（conformal features 2× 改善确认）
16	- **Baselines 锁定**: spatial 30% (K=1), object 13% (K=1)
17	- **早期信号（2/10 tasks，不构成结论）**: ACR-VLA 在简单任务上低于 baseline，per-DOF CRM 可能在简单任务上引入有害 correction
18	- **竞品分析完成** (art_20260514_621600): 核心竞品 ReconVLA（最直接）、SC-VLA、VLA-Pilot、ACoT-VLA
19	- **CRM correction 退化现象**: ACR-VLA 中间结果 (23-26%) 低于 baseline (30%)，SampleConsensus 领先 (42.9%)
20	- **文献调研完成** (art_20260514_d21dd2): correction degradation 可能原因与补救方向（correction clipping/gating 等）
21	
22	## 近期任务
23	- [ ] eval-acr-spatial-v2 完成 → 核心 claim 判定（ACR-VLA vs baseline 30%）
24	- [ ] eval-reconvla-spatial-v3 完成 → SampleConsensus 对比
25	- [ ] eval-scalar-unc-spatial 完成 → scalar vs per-DOF 最终裁决
26	- [x] crm-train-k5 完成 → K sensitivity ablation + eval-k5-spatial 已启动
27	- [ ] eval-k5-spatial 完成 → K=5 sensitivity ablation 结果
28	- [ ] eval-vla-mean-spatial 完成 → 隔离多采样平均贡献
29	- [x] 代码同步 bjb1→bjb2（evaluate.py + train_crm.py）— MD5 verified
30	- [ ] 完整 spatial 四路对比表出炉 → 决定是否铺 object benchmark
31	- [ ] paper_framing.md 更新竞品定位（SC-VLA, VLA-Pilot, ACoT-VLA SOTA）
32	
33	## SFT Gate
34	D015: 30% baseline 继续推进。核心关注相对提升，非绝对值。
35	
36	## GPU 预算
37	- bjb1-18228 (4× RTX 4090): eval-k5-spatial(cuda:0) + eval-acr(cuda:1) + eval-reconvla(cuda:2) + eval-scalar-unc(cuda:3)
38	- bjb2-40593 (1× RTX 4090 D): eval-vla-mean-spatial(cuda:0)
39	- 总预算 ~200 GPU·h, 已用 ~8
…[truncated 1563 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-14T21:22:03.850686+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "offset": "700",
  "limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
    "offset": "700",
    "limit": "500"
  }
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-14T21:22:03.953012+00:00_

700	      - event: on_failed
701	        action: agent
702	        ts: '2026-05-13T20:26:37.521060+00:00'
703	      - event: on_failed
704	        action: agent
705	        ts: '2026-05-13T22:59:44.694612+00:00'
706	  precompute-k5:
707	    status: DONE
708	    retry_count: 0
709	    created_at: '2026-05-13T20:15:37.603Z'
710	    updated_at: '2026-05-13T22:12:39.543Z'
711	    spec:
712	      command: python -u src/train_crm.py --precompute --benchmark spatial object
713	        --K 5 --cache_dir /root/autodl-tmp/crm_cache_k5/
714	      server: bjb1-18228
715	      gpu:
716	      - cuda:3
717	      pid: '79517'
718	      log_path: ~/runs/acr-vla-conformal-refinement/precompute-k5.log
719	      data_path: /root/autodl-tmp/libero_data/
720	      data_count: 26737
721	      model_name: smolvla_libero
722	      seed: 42
723	      hypothesis: K=5 precompute for K sensitivity ablation (plan_015)
724	    reproduce:
725	      finished_at: '2026-05-13T22:09:33.445Z'
726	    extra:
727	      hook_events:
728	      - event: on_complete
729	        action: agent
730	        ts: '2026-05-13T22:09:34.396952+00:00'
731	    conclusion: success
732	    checkpoint_path: /root/autodl-tmp/crm_cache_k5/
733	    metrics:
734	      spatial_samples: 12167
735	      object_samples: 14570
736	      total_samples: 26737
737	      spatial_cache_mb: 106
738	      object_cache_mb: 127
739	      total_cache_mb: 233
740	      runtime_min: 107
741	    completed_at: '2026-05-13T22:12:39.543Z'
742	  eval-reconvla-spatial-v2:
743	    status: DONE
744	    retry_count: 0
745	    created_at: '2026-05-13T20:29:41.730Z'
746	    updated_at: '2026-05-13T23:12:10.958Z'
747	    spec:
748	      command: python -u src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts
749	        10 --seed 42 --K 10
750	      server: bjb1-18228
751	      gpu:
752	      - cuda:2
753	      pid: '87787'
754	      log_path: ~/runs/acr-vla-conformal-refinement/eval-reconvla-spatial-v1.log
755	      data_path: /root/autodl-tm
…[truncated 19834 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "elapsed_ms": 102
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-14T21:22:08.320831+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "offset": "1200",
  "limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
    "offset": "1200",
    "limit": "500"
  }
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-14T21:22:08.372956+00:00_

1200	      model_name: CRM (K=5, 337K params)
1201	      seed: 42
1202	      hypothesis: CRM with K=5 conformal samples for K sensitivity ablation (K=10
1203	        baseline val_loss=0.009046)
1204	      log_path: /root/autodl-tmp/checkpoints/crm/k5/train.log
1205	      checkpoint_source: from_scratch
1206	      checkpoint_path: /root/autodl-tmp/checkpoints/crm/k5/crm_best.pt
1207	    reproduce:
1208	      finished_at: '2026-05-14T04:12:42.247Z'
1209	    extra:
1210	      hook_events:
1211	      - event: on_complete
1212	        action: agent
1213	        ts: '2026-05-14T04:12:44.286094+00:00'
1214	    conclusion: killed
1215	    metrics:
1216	      best_val_loss: 0.008996
1217	      best_epoch: 50
1218	      total_epochs: 50
1219	      comparison: K=5 val_loss 0.008996 ≈ K=10 val_loss 0.009046, near identical
1220	    completed_at: '2026-05-14T07:21:32.072Z'
1221	    conclusion_note: invalidated by D016 C1 fix, 6D state mismatch — checkpoint trained
1222	      on wrong features
1223	  eval-vla-mean-spatial:
1224	    status: RUNNING
1225	    retry_count: 0
1226	    created_at: '2026-05-14T03:10:44.114Z'
1227	    updated_at: '2026-05-14T03:11:46.546Z'
1228	    spec:
1229	      command: CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python
1230	        -u src/evaluate.py --mode vla_only --baseline_mode mean --benchmark spatial
1231	        --n_rollouts 10 --seed 42
1232	      server: bjb2-40593
1233	      gpu:
1234	      - cuda:0
1235	      pid: '143106'
1236	      data_path: /root/autodl-tmp/libero_data/ (spatial)
1237	      data_count: 100
1238	      model_name: SmolVLA K=10 mean action (no conformal)
1239	      seed: 42
1240	      hypothesis: K=10 mean baseline isolates multi-sampling averaging contribution
1241	        vs conformal correction. Expected between vla_only K=1 (30%) and ACR-VLA.
1242	      checkpoint_source: lerobot/smolvla_libero
1243	      eval_data: LIBERO spatial 10 tasks x 10 rollouts
1244	      log_path: /root/autodl-tmp/eval_resul
…[truncated 21755 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---

### Tool call

_source line 90 · 2026-05-14T21:22:12.792238+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "offset": "1700",
  "limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
    "offset": "1700",
    "limit": "500"
  }
}
```

</details>

---

### Tool result

_source line 91 · 2026-05-14T21:22:12.842994+00:00_

1700	      submitted_via: submit_training_job
1701	      backend: tmux
1702	      account: root
1703	      data_path: /root/autodl-tmp/libero_data/
1704	      data_count: 100
1705	      model_name: CRM obs_only v2 (990D, no conformal features)
1706	      seed: 42
1707	      hypothesis: obs_only CRM ablation — CRM without conformal features tests whether
1708	        per-DOF conformal intervals are necessary
1709	      checkpoint_source: /root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt
1710	      eval_data: LIBERO spatial 10 tasks x 10 rollouts
1711	      parent: crm-train-v2-obs-only
1712	      conclusion_note: 'Director order: 0/30 after 3 tasks, no diagnostic value. Freed
1713	        bjb1:2 for eval-tiny-correction-spatial.'
1714	      metrics:
1715	        tasks_completed: 3
1716	        total_tasks: 10
1717	        success_rate: 0
1718	        successes: 0
1719	        rollouts: 30
1720	      checkpoint_path: /root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt
1721	      wall_clock_seconds: 17890.8
1722	      gpu_hours: 4.97
1723	    conclusion: killed
1724	    completed_at: '2026-05-14T17:47:54.523Z'
1725	  eval-argmin-only-spatial:
1726	    status: RUNNING
1727	    retry_count: 0
1728	    created_at: '2026-05-14T17:47:58.683Z'
1729	    updated_at: '2026-05-14T17:48:54.942Z'
1730	    spec:
1731	      command: python -u src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts
1732	        10 --seed 42 --K 10
1733	      server: bjb1-18228
1734	      gpu:
1735	      - cuda:1
1736	      pid: '231421'
1737	      log_path: ~/runs/acr-vla-conformal-refinement/eval-argmin-only-spatial.log
1738	      submitted_at: '2026-05-14T17:47:58.583Z'
1739	      submitted_via: submit_training_job
1740	      backend: tmux
1741	      account: root
1742	      gpu_ids:
1743	      - cuda:1
1744	      data_path: /root/autodl-tmp/libero_data/ (spatial)
1745	      data_count: 100
1746	      model_name: SmolVLA K=10 argmin selection (no CRM correction)
1747	      seed
…[truncated 12416 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-14T21:22:19.672959+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/decisions.yaml",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/decisions.yaml",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 93 · 2026-05-14T21:22:19.723700+00:00_

1	_next_id: 19
2	decisions:
3	- id: D001
4	  date: 2026-05-13 01:03 UTC
5	  summary: MVP 方案确定：3D Point-Reaching Motivating Experiment 验证 per-DOF conformal 特征的信息优势
6	  rationale: IDEA_BRIEF 已设计了完美的 go/no-go gate：用合成数据的 3D reaching task 对比 per-DOF vs
7	    标量 vs 无不确定性三种 conditioning，直接测试核心假设。成本极低（<0.5 GPU-hours），无需 VLA 基础设施，失败则提前止损。Pass
8	    标准明确：B 在非扰动轴 MSE 比 A 低 >10%。
9	  related_experiments: []
10	  depends_on: []
11	- id: D002
12	  date: 2026-05-13 01:06 UTC
13	  summary: 采纳 Reviewer 建议完善 MVP：增加 B vs C 对比（>5% MSE）、K=10 estimated uncertainty variant、2:1/1.5:1
14	    各向异性 sweep
15	  rationale: Reviewer 正确指出 (1) 缺少 B vs C 对比会遗漏"观测特征已足够"的可能性，这直接关系核心 claim；(2) oracle
16	    uncertainty 与实际 pipeline 存在 gap，K=10 variant 几乎零成本可验证；(3) 5:1 比率过极端，需测试更温和情况。三项改进均不增加显著成本。
17	  related_experiments: []
18	  depends_on:
19	  - D001
20	- id: D003
21	  date: 2026-05-13 01:47 UTC
22	  summary: MVP 通过，GO — 进入 research 阶段
23	  rationale: 全部 3 条 pass 标准满足且 margin 很大：per-DOF (B) 在非扰动轴 MSE 比标量 (A) 低 22-38%，比无
24	    uncertainty (C) 低 15-39%。K=10 estimated 和弱各向异性(1.5:1)下均成立。核心假设"per-DOF conformal
25	    特征携带更多可操作信息"得到验证。关注风险：oracle→K=10 衰减 ~15pp，真实 7-DOF 场景待验证。
26	  related_experiments:
27	  - exp_id: mvp-point-reaching
28	    role: MVP gate
29	    result: PASS — all 6 conditions met criteria
30	  depends_on:
31	  - D001
32	  - D002
33	- id: D004
34	  date: 2026-05-13 02:59 UTC
35	  summary: Horizon 策略：截取 chunk 前 H_eff=5 步，action_dim=6。CGS 输出 40D。
36	  rationale: SmolVLA chunk_size=50 远超原假设 H=5。receding-horizon 执行语义下只需关注近期 action 的
37	    uncertainty，远期 step 对当前校正无意义。H_eff=5 保持与 IDEA_BRIEF 设计一致，CGS 40D 可控（per-DOF std
38	    30 + radius 5 + volume 5），p/n=6/10=0.6 优于原假设 0.7。H_eff=10 留作 ablation。action_dim=6
39	    使 Ledoit-Wolf 更稳定。
40	  related_experiments: []
41	  depends_on:
42	  - D003
43	- id: D005
44	  date: 2026-05-13 03:00 UTC
45	  summary: 不等 Dream 重新提交，直接启动 P0 实验。Dream zombie 占槽，Reviewer 已两轮审核通过 framing/plan。
46	  rationale: Dream dream_20260513T015051 崩溃在 review 阶段（imagine+write 
…[truncated 2520 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 94 · 2026-05-14T21:22:24.191170+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/decisions.yaml",
  "offset": "100",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/decisions.yaml",
    "offset": "100",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 95 · 2026-05-14T21:22:24.241897+00:00_

100	    0 SFT
101	  rationale: HuggingFace 上已有 lerobot/smolvla_libero（SmolVLA fine-tuned on LIBERO,
102	    action_dim=7）。如果质量可靠（spatial >50%），可跳过 Phase 0 SFT 节省 8-12h GPU。同时并行诊断评估崩溃 bug
103	    和修复 gripper 透传代码。
104	  related_experiments:
105	  - exp_id: plan_001
106	    role: dependency
107	    result: needs fine-tuned SmolVLA checkpoint
108	  - exp_id: plan_014
109	    role: dependency
110	    result: needs eval crash fix + fine-tuned model
111	  depends_on:
112	  - D008
113	- id: D010
114	  date: 2026-05-13 15:25 UTC
115	  summary: 'D010: 正式触发 SFT fallback — smolvla_libero 0% 确认不可用，启动 LoRA SFT'
116	  rationale: smolvla_libero 社区 checkpoint 在 LIBERO spatial 上 0/21 rollouts（7/10 tasks
117	    完成），eval 已运行 3h47m 无任何 success。根据 D009 预设条件（<50% → SFT），正式启动 LoRA SFT。4090x4 全部
118	    4 卡分配给 SFT 训练。预计 8-12h。Precompute cache 基于旧 checkpoint 需重做，但 SFT 完成后再处理。
119	  related_experiments:
120	  - exp_id: eval-smolvla-libero-spatial
121	    role: trigger
122	    result: 0% success, community checkpoint unusable
123	  - exp_id: sft-smolvla-libero
124	    role: next
125	    result: pending
126	  depends_on:
127	  - D009
128	- id: D011
129	  date: 2026-05-13 15:28 UTC
130	  summary: 'D011: 正式放弃 CoRL 2026，目标 ICLR 2027'
131	  rationale: paper_framing.md 预设"3 天内 GPU 未扩容至 ≥2x H100 → 放弃 CoRL"。当前资源仍为 4×4090 +
132	    1×4090D，无 H100 扩容。CoRL abstract DDL May 26 仅剩 13 天，关键路径最乐观 26h 到 plan_001 首个结果，加
133	    ablations + paper 写作不可能在 13 天内完成。ICLR 2027 DDL 预计 Sep-Oct 2026，时间充足。
134	  related_experiments: []
135	  depends_on:
136	  - D010
137	- id: D012
138	  date: 2026-05-13 16:09 UTC
139	  summary: 'D012: smolvla_libero wrapper 修复后 55.6% — 取消 SFT，直接进 precompute+CRM'
140	  rationale: 诊断发现 7 个 wrapper bug（图像翻转/尺寸/值域、state 维度/归一化、action 反归一化、camera_names
141	    缺失）。修复后 re-eval 3 tasks×3 rollouts = 55.6% (5/9)，超过 50% gate。SmolVLA 论文报告 78-85%（20
142	    rollouts），当前小样本波动正常。SFT 路径取消，旧 precompute cache（基于 buggy wrapper）需用修复后代码重做。关键路径从
143	    SFT(8-12h)+Precompute+CRM+Eval 缩短为 Precompute+CRM+Eval
…[truncated 2624 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-14T21:22:28.656443+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/decisions.yaml",
  "offset": "200",
  "limit": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/decisions.yaml",
    "offset": "200",
    "limit": "60"
  }
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-14T21:22:28.707248+00:00_

200	    train/eval distribution shift 足以解释 ACR-VLA 23.3% < baseline 30% 的全部现象。同时修复 W2（mean→argmin
201	    select-then-refine）、W3（alpha 0.1→0.5 避免 conformal quantile 退化）、W4（CRM output L2
202	    clipping）。修复后重跑 precompute→CRM train→eval 全 pipeline。
203	  related_experiments:
204	  - exp_id: eval-acr-spatial-v2
205	    role: invalidated
206	    result: 23.3% — compromised by C1 bug
207	  - exp_id: eval-k5-spatial
208	    role: invalidated
209	    result: 26% — compromised by C1 bug
210	  - exp_id: eval-scalar-unc-spatial
211	    role: invalidated
212	    result: 35% — compromised by C1 bug
213	  depends_on:
214	  - D015
215	- id: D017
216	  date: 2026-05-14 17:46 UTC
217	  summary: 'D017: CRM correction 全面拖累 baseline — kill 两路 ablation，启动诊断实验（argmin-only
218	    + tiny correction），准备 Gated CRM'
219	  rationale: 3/10 tasks 数据：所有 CRM 变体（per-DOF 3.3%, scalar 0%, obs-only 0%）均远低于 VLA
220	    mean baseline 40%。问题在 CRM correction 机制（compounding error in closed-loop），不在 conformal
221	    features。Kill scalar-unc 和 obs-only（0% 无继续价值），释放 GPU 启动诊断：(1) argmin-only passthrough
222	    量化 CRM 损害，(2) max_norm=0.05 极保守 correction 测试是否缩小 delta 能避免 compounding。同时准备 Gated
223	    CRM 代码（低 uncertainty 时 correction→0）。
224	  related_experiments:
225	  - exp_id: eval-acr-spatial-v3
226	    role: core_claim
227	    result: 3.3% at 3/10 tasks (negative)
228	  - exp_id: eval-scalar-unc-spatial-v2
229	    role: ablation
230	    result: 0% at 3/10 tasks → killed
231	  - exp_id: eval-obs-only-spatial-v3
232	    role: ablation
233	    result: 0% at 3/10 tasks → killed
234	  - exp_id: eval-vla-mean-spatial
235	    role: baseline
236	    result: 40% at 7/10 tasks
237	  depends_on:
238	  - D016
239	- id: D018
240	  date: 2026-05-14 17:56 UTC
241	  summary: 'D018: CRM 失败根因确认为输入未归一化（1500x scale 差异），批准 normalization + retrain v3'
242	  rationale: 代码审查确认无 D016 级 train/eval 不匹配。真正问题：CRM 1030D 输入未做 standardization，log_volume(-25)
243	    vs per_dof_std(0.017) 量级差 1500x，2层MLP学不好——训练集上仅 49% 样本受益（随机水平），impr
…[truncated 488 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Assistant

_source line 98 · 2026-05-14T21:23:45.154538+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- GPU 白名单必须通过 `get_project_status` 的 `execution.gpu_ids` 确认，当前 bjb1 分配 cuda:0-3，bjb2 分配 cuda:0
- bjb2-40593 上的 crm_cache 是 v4（6D state，D016 之前），**不能用于训练**——只有 bjb1 的 `/root/autodl-tmp/crm_cache_v5/` 是 8D state 修复后的正确版本
- CRM v1/v2/a3/a4/k5 的所有 checkpoint 已被 D016 invalidate（6D state mismatch），绝不能用来 eval
- eval-acr-spatial-v3 结果（2.5%）是 v2 CRM（无 normalization）的结果，不代表 v3-norm 的表现——两者不可混为一谈
- `submit_training_job` 命令必须自带环境激活（`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`），bjb1/bjb2 均为 conda 环境

### 2. 🖥️ 基础设施快照
- **bjb1-18228** (4× RTX 4090): 工作目录 `/root/acr-vla-conformal-refinement`，Python `/root/miniconda3/bin/python`，conda base
- **bjb2-40593** (1× RTX 4090D): 同上路径结构
- 模型: `/root/autodl-tmp/models/smolvla_libero/`（SmolVLA 450M, libero fine-tuned）
- VLM backbone: `/root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct/`
- 正确 CRM cache: `/root/autodl-tmp/crm_cache_v5/`（bjb1 only, 8D state, 12167 spatial + 14570 object samples）
- CRM v3-norm checkpoint: `/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt`（val_loss=0.0358, 带 input_mean/input_std tensors）
- 数据: `/root/autodl-tmp/libero_data/`
- Gated CRM 代码: `src/gated_crm.py`（modes: clipping/gating/temperature，已就绪未启用）
- 活跃进程（截至 handoff 时刻）:
  - bjb1 cuda:0: eval-acr-spatial-v4-default（v3-norm, 默认 correction）
  - bjb1 cuda:1: eval-argmin-only-spatial (PID 231421)
  - bjb1 cuda:2: eval-tiny-correction-spatial (PID 232815, max_norm=0.05)
  - bjb1 cuda:3: eval-acr-spatial-v4-small (PID 253085, max_norm=0.1)
  - bjb2 cuda:0: eval-vla-mean-spatial (PID 143106)
  - bjb1 上还有 crm-train-v3-norm-obs-only 和 crm-train-v3-norm-scalar-unc 在跑（无 GPU 编号记录，应在 tmux 里确认）
- GPU 预算: ~200h 总量, ~80h 已用, ~120h 剩余

### 3. 📊 当前状态
刚完成 D018 修复（CRM 输入 normalization）和 v3-norm CRM 训练（val_loss=0.0358）。核心悬念：**v3-norm eval 是否解决 30%→2.5% 的灾难性退化**。7 个实验同时在跑，等 cron 回调。

**Registry RUNNING 实验**:
| exp_id | 摘要 | 服务器/GPU |
|--------|------|-----------|
| eval-acr-spatial-v4-default | v3-norm CRM，默认 correction，决定 normalization 是否够 | bjb1:0 |
| eval-acr-spatial-v4-small | v3-norm + max_norm=0.1，测 magnitude control 是否额外需要 | bjb1:3 |
| eval-argmin-only-spatial | 纯 argmin 无 CRM，隔离 argmin base 选择 vs CRM correction 的影响 | bjb1:1 |
| eval-tiny-correction-spatial | max_norm=0.05（28x 缩小），早期信号 task1 4/5 成功 | bjb1:2 |
| eval-vla-mean-spatial | K=10 均值 baseline，隔离多采样平均贡献 | bjb2:0 |
| crm-train-v3-norm-scalar-unc | scalar uncertainty ablation + normalization | bjb1 (GPU TBD) |
| crm-train-v3-norm-obs-only | obs-only ablation + normalization | bjb1 (GPU TBD) |

**等待中**: 所有 7 个实验的 cron 回调。无待处理的 Director 决策。

### 4. 📋 待办（条件触发式）
- eval-acr-spatial-v4-default 完成 → 对比 30% baseline：>30% 意味着 normalization 解决了主要问题；≤30% 意味着 magnitude control 不可或缺
- eval-acr-spatial-v4-small 完成 → 与 v4-default 对比：small > default 确认 magnitude clipping 有效，下一步做 correction sweep（0.01, 0.05, 0.1, 0.2, 0.5）
- v4-default ≤ 30% 且 v4-small > v4-default → 启用 Gated CRM（`src/gated_crm.py`），做 magnitude sweep + 温度 gating 实验
- v4-default > 30% → 立即铺 v3-norm-scalar-unc 和 v3-norm-obs-only 的 eval，完成 per-DOF vs scalar vs obs-only 三路对比表
- eval-vla-mean-spatial 完成 → 得到 K=10 mean baseline，四路对比表最后一格填上
- eval-argmin-only-spatial 完成 → 判断 argmin 选择本身是否引入损害
- crm-train-v3-norm-scalar-unc/obs-only 训练完成 → spawn eval Worker 跑对应的 spatial eval
- 四路对比表出齐（ACR-VLA / SampleConsensus 34% / VLA-mean / VLA-K1 30%）→ 向 Director 汇报核心 claim 判定，决定是否需要 Framing 调整
- 如果所有 CRM 变体仍 ≤ baseline → **必须走 Red Section Framing 提案流程**，禁止默默跑下一批

### 5. 🎯 战略上下文
- **项目核心**: Per-DOF conformal statistics → dimension-selective action correction for VLAs. 目标 ICLR 2027 (Sep-Oct 2026 DDL)
- **决策链**: D001→D003 MVP PASS → D015 SFT Gate 30% 继续 → D016 发现 6D/8D state bug → D017 确认 CRM correction 全面退化 → D018 根因=输入未归一化(1500x scale imbalance) → 当前等 v3-norm eval
- **核心结论**: MVP 验证 per-DOF > scalar > none（合成数据），但闭环 LIBERO eval 上 CRM correction 导致灾难性退化（30%→2.5%）。D018 normalization 是最新修复，尚未验证
- **文献支撑**: PLD(ICLR2026) scheduled ξ, TRANSIC(CoRL2024) 无gate=collapse, 均支持 correction magnitude control 的必要性。ACR-VLA 的独特贡献角度="Conformally-Calibrated Correction Magnitude"——CP intervals 作为 correction 幅度的自然上界
- **最易判断错的事**: (1) 不要把 v2 CRM（无 norm）的 2.5% 结果当作"per-DOF 方法失败"——v3-norm 是全新模型，结果可能完全不同；(2) CRM 的 val_loss 不可跨版本比较（v1=0.009 vs v3-norm=0.036），因为 input normalization 改变了 loss 的尺度；(3) eval-tiny-correction task1 4/5 是早期信号（5 rollouts），不构成结论
- **SampleConsensus 不是 ReconVLA**: D014 确认当前 reconvla mode 实际是 argmin-Euclidean 启发式，已重命名为 SampleConsensus(34%)，不要在论文中称其为 ReconVLA
- **Claim C2(ACI+COC) 和 C3(SRPO orthogonality) 零证据**: 目前全部精力在 C1(per-DOF correction)，C2/C3 尚未开始
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:precompute-v4-shard2"
}
```

</details>

---
