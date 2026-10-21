# cron hook precompute v4 shard2 20260514T031350 703795

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 67
- **Recorded user turns:** 2
- **Tool calls:** 32
- **Original source:** `logs/chats/archive/cron_hook_precompute-v4-shard2_20260514T031350_703795.jsonl`
- **Structured JSON:** [`ec28a81ed2e83dfe0e27.json`](../../sessions/ec/ec28a81ed2e83dfe0e27.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

47 recorded events

### User

_source line 1 · 2026-05-13T23:18:21.196797+00:00_

[HANDOFF] 你是 Main Agent，这是 Loop #2。

## 上一轮交接 (task_context)

### 1. 🔴 硬约束 / 红线
- GPU 白名单: bjb1-18228:cuda:0/1/2/3, bjb2-40593:cuda:0。其他卡一律不能用
- precompute cache 路径必须是 `/root/autodl-tmp/crm_cache/`（v4 版本），不要用 crm_cache_v3（已 killed/无效）
- AutoDL 服务器必须 `HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1`，否则 AutoProcessor 联网失败导致静默崩溃
- SmolVLA evaluate.py 必须在 env_args 里指定 `camera_names=["agentview", "robot0_eye_in_hand"]`，缺少会导致只收到单摄像头、结果系统性偏低（D015 教训）
- submit_training_job 的 command 用 `bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && ..."`，不要假设 .venv 存在

### 2. 🖥️ 基础设施快照
- **bjb1-18228** (autodl-4090x4, 4× RTX 4090): 工作目录 `/root/acr-vla-conformal-refinement`, Python `/root/miniconda3/bin/python`, conda base
  - 模型: `/root/autodl-tmp/models/smolvla_libero/`
  - 数据: `/root/autodl-tmp/libero_data/` (spatial + object)
  - Precompute cache: `/root/autodl-tmp/crm_cache/` (v4, 3 shard 已完成)
  - 活跃进程: eval-spatial-v5-full (PID 73756, cuda:0, tmux session)
- **bjb2-40593** (autodl-4090, 1× RTX 4090 D): 同样路径结构
  - 活跃进程: eval-object-v4-full (PID 103778, cuda:0, tmux session)
- 两台 cron 都在 reconcile 中：eval-spatial-v5-full + eval-object-v4-full
- HF cache: `/root/autodl-tmp/.hf_cache`
- GPU 预算 ~200h，已用 ~25h

### 3. 📊 当前状态
**刚做完**: precompute-v4-shard2 CRON 回调处理。3 个 v4 shard 全部 success（cache 写入 `/root/autodl-tmp/crm_cache/`）。shard2 conclusion=success 已写入 registry（status 卡在 PREPARING，状态机不允许 PREPARING→DONE 跳转，但 conclusion 已正确）。

**正在跑的实验**:
- `eval-spatial-v5-full` (PREPARING, bjb1 cuda:0) — SmolVLA 修复版 wrapper 在 spatial 上的 10×10 full eval，决定 SFT gate
- `eval-object-v4-full` (PREPARING, bjb2 cuda:0) — SmolVLA 在 object 上的 full eval

**等待中的 Worker 回调** (4 个 Worker running):
1. `worker_infra_check-precompute-v4-completion` — 之前 session 遗留的 infra 检查
2. `worker_analyze_precompute-v4-shard2` — 分析 shard2 日志 + cache 完整性
3. `worker_code_crm-train-v1-prep` — **关键**: 验证 cache → 提交 CRM 训练到 bjb1 cuda:1
4. `worker_code_ablation-prep` — 检查 train_crm.py 是否支持 plan_002/003 ablation 模式

**已向 Director 汇报**: precompute 全部完成 + CRM 训练启动中 + 空闲 GPU 利用建议。等 Director 回复。

### 4. 📋 待办（条件触发式）
- `worker_code_crm-train-v1-prep` 回调 → 确认 CRM 训练已提交（exp_id=crm-train-v1），更新 registry，注册 cron 监控
- `worker_code_ablation-prep` 回调 → 如果 ablation 已支持 → 立即在 cuda:2/3 提交 plan_002 + plan_003；如果不支持 → 派 Worker 改代码加 `--input_mode` 参数
- eval-spatial-v5-full cron 回调 → 按 on-experiment-done 分叉：≥80% 按计划推进, 50-80% 可继续调低期望, <30% 换模型（SFT gate）
- eval-object-v4-full cron 回调 → 同上处理
- CRM 训练完成（预计 4-6h 后）→ 启动 ACR-VLA full pipeline eval（plan_001 的 eval 阶段）
- cuda:2/3 空闲超过 30min 且无 ablation 可跑 → 不同 seed CRM 训练 或 plan_014 ReconVLA baseline 重跑
- Director 回复空闲 GPU 建议 → 按指令执行

### 5. 🎯 战略上下文
- **核心假设已验证**: MVP (plan_000) 确认 per-DOF > scalar > none，PASS
- **目标**: ICLR 2027 (DDL Sep-Oct 2026)，CoRL 2026 已放弃 (D011)
- **关键路径**: Precompute ✅ → CRM 训练 (正在启动) → ACR-VLA Eval → ablations
- **Wrapper 血泪史**: 前 3 轮实验全部无效（v1 precompute killed, v2 killed, v3 killed），根因是 SmolVLA wrapper 有 7 个 bug（图像翻转/尺寸/归一化, state 6D→8D, state/action normalization, 双摄像头）。D014 完成修复并部署，v4 是第一批有效数据
- **registry 状态机问题**: 所有 precompute-v4 和 eval-v4/v5 实验的 status 都卡在 PREPARING（submit_training_job 没正确推进），但 conclusion 和 finished_at 是准确的。不要被 status=PREPARING 迷惑
- **易错点**: (1) 不要用 crm_cache_v3 路径，那是 killed 数据 (2) 不要在 evaluate.py 里漏掉 camera_names 参数 (3) GPU 编号脚本内永远从 0 开始（CUDA_VISIBLE_DEVICES 自动映射）
- **决策链**: D008(SmolVLA 需 SFT) → D009(先试社区 checkpoint) → D010(SFT fallback) → D012(55.6% 不可靠) → D013(wrapper 需完全对齐 lerobot) → D014(修复部署, v4 启动)

## 可查的历史
前 2 轮 handoff 在 `task_context/history/agent/loop_*.md`，如有疑问可 Read 回查。
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

_source line 2 · 2026-05-13T23:18:34.509409+00:00_

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
  "session": "cron:hook:precompute-v4-shard2",
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

_source line 3 · 2026-05-13T23:18:34.509750+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-13T23:18:37.827385+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "limit": "0"
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
    "project": "acr-vla-conformal-refinement",
    "limit": "0"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-13T23:18:38.328983+00:00_

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

_source line 6 · 2026-05-13T23:18:38.331795+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-object-v5-full\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-13T23:17:35.776Z\", \"updated_at\": \"2026-05-13T23:17:40.750Z\"}, \"eval-acr-vla-spatial-v1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T22:56:40.287Z\", \"updated_at\": \"2026-05-13T23:14:22.561Z\", \"conclusion\": \"killed\"}, \"eval-reconvla-spatial-v3\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-13T23:04:34.297Z\", \"updated_at\": \"2026-05-13T23:13:37.736Z\"}, \"eval-acr-spatial-v2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-13T23:04:32.138Z\", \"updated_at\": \"2026-05-13T23:13:34.142Z\"}, \"eval-spatial-v6-full\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-13T23:04:28.766Z\", \"updated_at\": \"2026-05-13T23:13:29.780Z\"}, \"eval-acr-spatial-v1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T22:54:28.535Z\", \"updated_at\": \"2026-05-13T23:12:11.315Z\", \"conclusion\": \"killed\"}, \"eval-reconvla-spatial-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T20:29:41.730Z\", \"updated_at\": \"2026-05-13T23:12:10.958Z\", \"conclusion\": \"killed\"}, \"eval-object-v4-full\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T19:13:26.341Z\", \"updated_at\": \"2026-05-13T23:12:10.037Z\", \"conclusion\": \"killed\"}, \"eval-spatial-v5-full\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T19:16:58.052Z\", \"updated_at\": \"2026-05-13T23:12:09.066Z\", \"conclusion\": \"killed\"}, \"eval-reconvla-spatial-v1\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-13T20:15:35.450Z\", \"updated_at\": \"2026-05-13T22:59:43.788Z\", \"conclusion\": \"failed\"}, \"crm-train-a3-obs-only\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-13T22:56:28.643Z\", \"updated_at\": \"2026-05-13T22:56:35.164Z\"}, \"crm-train-v1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-13T20:10:36.535Z\", \"updated_at\": \"2026-05-13T22:50:54.738Z\", \"conclusion\": \"success\", \"metrics\": {\"
…[truncated 6512 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 504
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-13T23:18:38.783804+00:00_

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

_source line 8 · 2026-05-13T23:18:38.784247+00:00_

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

### Tool result

_source line 9 · 2026-05-13T23:18:42.898032+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 4, \"results\": [{\"exp_id\": \"eval-spatial-v6-full\", \"success\": true, \"actions\": [\"Job still running (pid=109802)\"]}, {\"exp_id\": \"eval-acr-spatial-v2\", \"success\": true, \"actions\": [\"Job still running (pid=110073)\"]}, {\"exp_id\": \"eval-reconvla-spatial-v3\", \"success\": true, \"actions\": [\"Job still running (pid=110280)\"]}, {\"exp_id\": \"crm-train-a3-obs-only\", \"success\": true, \"actions\": [\"Job still running (pid=104611)\"]}]}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 4569
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-13T23:18:42.899046+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md\", \"content\": \"# Handover — 2026-05-13\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| eval-object-v5-full | — | — | — | — |\\n| eval-reconvla-spatial-v3 | — | — | — | — |\\n| eval-acr-spatial-v2 | — | — | — | — |\\n\\n## 待处理\\n- eval-reconvla-spatial-v1（准备中）\\n- precompute-v4-shard2（准备中）\\n- precompute-v4-shard1（准备中）\\n- precompute-v4-shard0（准备中）\\n- eval-spatial-v4-full（准备中）\\n- precompute-v3-shard2（准备中）\\n- precompute-v3-shard1（准备中）\\n- precompute-v3-shard0（准备中）\\n- precompute-v2-shard2（准备中）\\n- precompute-v2-shard1（准备中）\\n- …另有 1 项\\n\\n## 近期结论\\n- **eval-acr-vla-spatial-v1** (killed): —\\n- **eval-acr-spatial-v1** (killed): —\\n- **eval-reconvla-spatial-v2** (killed): —\\n\\n## 趋势\\n成功 6 / 负向 0 / 失败 3 / 共 16\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nbjb1-18228: 无 GPU 信息\\nbjb2-40593: 无 GPU 信息\\n\\n## 告警\\n- plan_001-crm-smolvla: 训练失败 — unknown\\n- plan_014-reconvla-baseline: 训练失败 — unknown\\n- eval-smolvla-libero-spatial: 训练失败 — unknown\\n- eval-spatial-reeval-v2: 已被终止 — unknown\\n- eval-spatial-v3-full: 已被终止 — unknown\\n- eval-object-v4-full: 已被终止 — unknown\\n- eval-spatial-v5-full: 已被终止 — unknown\\n- eval-reconvla-spatial-v2: 已被终止 — unknown\\n- eval-acr-spatial-v1: 已被终止 — unknown\\n- eval-acr-vla-spatial-v1: 已被终止 — unknown\\n\", \"total_chars\": 1238, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 4115
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-13T23:18:42.949696+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-13 19:10 UTC | 更新原因: D014: wrapper+evaluate.py 部署到服务器，v4 实验已启动\\n\\n## 核心方向\\nPer-DOF conformal statistics from multivariate CP on flow-matching VLA samples enable dimension-selective action correction. 详见 paper_framing.md。\\n\\n## 投稿目标\\n**ICLR 2027**（预计 DDL Sep-Oct 2026）。CoRL 2026 已放弃（D011）。\\n\\n## 当前进展\\n- **阶段**: Phase 1 — Eval + Precompute（修复版代码已部署验证）\\n- **MVP**: PASS（plan_000, per-DOF > scalar > none 确认）\\n- **D014**: wrapper+evaluate.py 修复版已部署到 bjb1-18228，grep 验证通过，v4 实验已启动\\n- **Wrapper 重构**: 完成，281 行，对齐 lerobot SmolVLAPolicy（flip+resize_with_pad+normalize[-1,1]+8D state+MEAN_STD+unnormalize）\\n- **Paper**: references.bib (31 entries) + related_work.tex (870 words) 已完成\\n\\n## 近期任务\\n- [x] ~~诊断 smolvla_libero 0% 根因~~ → 7 个 wrapper bug\\n- [x] ~~部分修复 + re-eval~~ → 55.6% 但不可靠（D013）\\n- [x] ~~Kill ghost 进程~~ → 多次清理完成\\n- [x] ~~Wrapper 重构~~ → 对齐 lerobot SmolVLAPolicy，Phase 4 验证 33%/67%\\n- [x] ~~部署修复版代码到服务器~~ → D014 wrapper+evaluate.py 部署验证通过\\n- [x] ~~Paper: bibliography + Related Work~~ → 完成\\n- [ ] **eval-spatial-v4-full** 运行中（cuda:0, PID 69379, ~2h）\\n- [ ] **precompute-v4-shard0/1/2** 运行中（cuda:1/2/3, ~35min）\\n- [ ] Precompute 完成后验证 cache 数据 + CRM 训练\\n- [ ] Full eval 完成后确认 SFT gate\\n- [ ] autodl-4090 部署 + object eval\\n\\n## SFT Gate（待重新评估）\\nD014: wrapper+evaluate.py 修复版已部署。等 eval-spatial-v4-full 结果（10 tasks × 10 rollouts）。\\n- ≥80% → 按计划推进\\n- 50-80% → 可继续，调低期望\\n- <30% → 换模型\\n\\n## GPU 预算\\n- autodl-4090x4 (bjb1-18228): 4× RTX 4090 → eval-spatial-v4(cuda:0) + precompute-v4(cuda:1/2/3)\\n- autodl-4090 (bjb2-40593): 1× RTX 4090 D → 代码部署中，待启动 object eval\\n- 总预算 ~200 GPU·h, 已用 ~25h, 剩余 ~175h\\n\\n## 关键路径\\n~~Wrapper 重构~~ → **Eval v4 (~2h)** + **Precompute v4 (~35min)** → CRM 训练 (4-6h) → ACR-VLA Eval (8-10h)\\nplan_
…[truncated 1157 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 4165
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-13T23:19:10.164719+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__list_workers,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__save_project_file",
  "max_results": "4"
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
    "query": "select:mcp__agent-ml-research__list_workers,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__save_project_file",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-13T23:19:10.165132+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-13T23:19:13.476112+00:00_

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
  "session": "cron:hook:precompute-v4-shard2",
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

### Tool result

_source line 15 · 2026-05-13T23:19:13.928452+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-object-v5-full\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:17:35.776Z\", \"updated_at\": \"2026-05-13T23:17:40.750Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 42 --smolvla_path /root/autodl-tmp/models/smolvla_libero/\", \"server\": \"bjb2-40593\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_object/\", \"data_count\": 10, \"model_name\": \"smolvla_libero\", \"seed\": 42, \"pid\": 115623, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-object-v5-full.log\", \"description\": \"VLA-only baseline eval on LIBERO object benchmark (v5, post env.reset P0 fix)\", \"gpu\": \"cuda:0\"}}, \"eval-reconvla-spatial-v3\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:04:34.297Z\", \"updated_at\": \"2026-05-13T23:13:37.736Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts 10 --seed 42 --K 10\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"110280\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-reconvla-spatial-v3.log\", \"submitted_at\": \"2026-05-13T23:04:34.240Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"SampleConsensus (scalar Euclidean nonconformity + argmin)\", \"seed\": 42, \"hypothesis\": \"SampleConsensus baseline with fixed evaluate.py - scalar comparison for ACR-VLA\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"libero_spatial 10 tasks x 10 rollouts\"}}, \"eval-acr-spatial-v2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:04:32.138Z\", \"updated_at\": \"2026-05-13T23:13:34.142Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode acr_vla --benchmark spatial
…[truncated 2590 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 452
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-13T23:19:13.928882+00:00_

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

_source line 17 · 2026-05-13T23:19:14.481142+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [], \"count\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 552
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-13T23:19:14.581969+00:00_

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
  "session": "cron:hook:precompute-v4-shard2",
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

_source line 19 · 2026-05-13T23:19:14.633646+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md\", \"content\": \"# Memory — acr-vla-conformal-refinement\\n\\n## SmolVLA Wrapper 正确预处理规范（2026-05-13 16:00，7 个 bug 修复后验证通过）\\n\\n### 教训\\n初次 eval 0% 成功率，**7 个 wrapper bug 全部是预处理/后处理不匹配**。必须完全对齐 lerobot 官方推理管线。\\n\\n### 正确预处理（已验证 55.6% success）\\n| 步骤 | 正确做法 | 之前的 bug |\\n|------|----------|-----------|\\n| 图像翻转 | `torch.flip(dims=[2,3])` 翻转 H+W | 无翻转 |\\n| 图像尺寸 | `resize_with_pad(512, 512)` | `Resize(256,256)` |\\n| 图像值域 | `img * 2.0 - 1.0` → [-1,1] | `ToTensor()` → [0,1] |\\n| State 维度 | **8D**: eef_pos(3) + eef_axisangle(3) + gripper_qpos(2) | 6D（缺 gripper） |\\n| State 归一化 | `(s - mean) / (std + ε)` MEAN_STD | 原始值直接传入 |\\n| Action 反归一化 | `a * std + mean` MEAN_STD | 模型原始输出 |\\n| Camera names | env_args 指定 `[\\\"agentview\\\", \\\"robot0_eye_in_hand\\\"]` | 只有 agentview |\\n\\n### Normalizer 文件\\n- State: `policy_preprocessor_step_5_normalizer_processor.safetensors` (8D mean/std)\\n- Action: `policy_postprocessor_step_0_unnormalizer_processor.safetensors` (7D mean/std)\\n- 路径: 模型目录下\\n\\n### ⚠️ Precompute 数据需重做\\n之前 3-shard precompute（spatial + object）用的是 buggy wrapper → K-samples 和 obs_features 全部错误。**必须用修复后的 wrapper 重新 precompute 才能训练 CRM。**\\n\\n## smolvla_libero checkpoint 信息\\n\\n- `lerobot/smolvla_libero`：25K 步全参数微调 on libero_spatial, action_dim=7\\n- 验证结果：spatial 前 3 tasks **55.6% (5/9)** with K=1\\n- smolvla_base (6D, 无 gripper) 只是预训练基座，不能直接用于 LIBERO\\n- 需要同时下载 VLM backbone `SmolVLM2-500M-Video-Instruct` 到本地\\n\\n## 评估崩溃根因（2026-05-13 11:00）\\n\\n- **根因：HuggingFace AutoProcessor.from_pretrained 联网失败**（AutoDL 网络不通）\\n- `tee` 掩盖退出码 → 看似\\\"无声崩溃\\\"\\n- **修复**：HF_HUB_OFFLINE=1 + TRANSFORMERS_OFFLINE=1 + try/except + SIGSEGV handler\\n\\n## MVP 实验关键洞察 (2026-05-13)\\n\\n### Per-DOF vs 标量 uncertainty\\n- Per-DOF (B) 在所有轴上都优于标量 (A)，说明 per-DOF 特征的价值是\\\"信息增益\\\"而非仅\\\"选择性校正\\\"\\n- 即使 1.5:1 低各向异性比率，per-DOF 仍显著优于标量\\n- K
…[truncated 1968 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-13T23:19:49.039436+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_cron,mcp__agent-ml-research__list_constraints",
  "max_results": "2"
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
    "query": "select:mcp__agent-ml-research__register_cron,mcp__agent-ml-research__list_constraints",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-13T23:19:49.039844+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-13T23:19:50.343407+00:00_

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

_source line 23 · 2026-05-13T23:19:50.394162+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/sessions/agent_f7022f78.

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

_source line 24 · 2026-05-13T23:19:53.305437+00:00_

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
  "session": "cron:hook:precompute-v4-shard2",
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

_source line 25 · 2026-05-13T23:19:53.406222+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-13T23:19:55.764702+00:00_

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

_source line 27 · 2026-05-13T23:19:55.815367+00:00_

No files found

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

_source line 28 · 2026-05-13T23:19:59.131453+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/skills/**/*.skill.md",
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
    "pattern": "**/skills/**/*.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-13T23:19:59.232241+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-13T23:20:01.140354+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/skills/**/*",
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
    "pattern": "**/skills/**/*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-13T23:20:01.241176+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-13T23:20:03.853516+00:00_

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
  "session": "cron:hook:precompute-v4-shard2",
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

_source line 33 · 2026-05-13T23:20:04.055723+00:00_

/home/ubuntu/agent-ml-research/skills/global/resource-saturation.skill.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Glob",
  "elapsed_ms": 202
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-13T23:20:07.016471+00:00_

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

_source line 35 · 2026-05-13T23:20:07.117692+00:00_

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
  "elapsed_ms": 101
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-13T23:20:30.354443+00:00_

called mcp__agent-ml-research__register_cron

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_cron</summary>

```json
{
  "exp_id": "eval-object-v5-full",
  "server": "bjb2-40593",
  "pid": "115623",
  "log_path": "/root/acr-vla-conformal-refinement/logs/eval-object-v5-full.log",
  "project": "acr-vla-conformal-refinement",
  "interval_seconds": "120"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__register_cron",
  "tool_args": {
    "exp_id": "eval-object-v5-full",
    "server": "bjb2-40593",
    "pid": "115623",
    "log_path": "/root/acr-vla-conformal-refinement/logs/eval-object-v5-full.log",
    "project": "acr-vla-conformal-refinement",
    "interval_seconds": "120"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-13T23:20:30.455353+00:00_

{"result":"{\"success\": true, \"data\": {\"registered\": {\"exp_id\": \"eval-object-v5-full\", \"server\": \"bjb2-40593\", \"pid\": \"115623\", \"wandb_run_id\": null, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-object-v5-full.log\", \"interval_seconds\": 120, \"project\": \"acr-vla-conformal-refinement\", \"tracked_metrics\": null, \"chat_id\": null, \"hooks\": null, \"last_checked\": null, \"created_at\": \"2026-05-13T23:20:30.364Z\"}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__register_cron",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-13T23:20:39.516723+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__get_project_resource_usage",
  "max_results": "2"
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
    "query": "select:mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__get_project_resource_usage",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-13T23:20:39.567348+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-13T23:20:42.027250+00:00_

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
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__get_project_resource_usage",
  "tool_args": {
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-13T23:20:42.128396+00:00_

{"result":"{\"success\": true, \"data\": {\"allocated_gpus\": [], \"actually_running_gpus\": [{\"server\": \"bjb1-18228\", \"gpu_id\": \"cuda:0\", \"exp_id\": \"eval-spatial-v6-full\"}, {\"server\": \"bjb1-18228\", \"gpu_id\": \"cuda:1\", \"exp_id\": \"eval-acr-spatial-v2\"}, {\"server\": \"bjb1-18228\", \"gpu_id\": \"cuda:2\", \"exp_id\": \"eval-reconvla-spatial-v3\"}, {\"server\": \"bjb2-40593\", \"gpu_id\": \"cuda:0\", \"exp_id\": \"eval-object-v5-full\"}], \"allocated_but_idle\": [], \"running_experiments\": [{\"exp_id\": \"eval-spatial-v6-full\", \"gpus\": [\"cuda:0\"], \"util_avg\": null}, {\"exp_id\": \"eval-acr-spatial-v2\", \"gpus\": [\"cuda:1\"], \"util_avg\": null}, {\"exp_id\": \"eval-reconvla-spatial-v3\", \"gpus\": [\"cuda:2\"], \"util_avg\": null}, {\"exp_id\": \"eval-object-v5-full\", \"gpus\": [\"cuda:0\"], \"util_avg\": null}], \"worker_pool\": {\"total\": 0, \"gpu_tasks\": 0, \"cpu_tasks\": 0, \"details\": []}, \"summary\": \"分配 0 张, 实际跑 4 张 | Worker 0 (GPU 0 / CPU 0)\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__get_project_resource_usage",
  "elapsed_ms": 101
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-13T23:21:17.885941+00:00_

called mcp__agent-ml-research__spawn_worker

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker</summary>

```json
{
  "task_type": "monitor:spatial-eval-progress",
  "project": "acr-vla-conformal-refinement",
  "task_prompt": "## 任务：检查 bjb1-18228 上 3 个 spatial eval 的运行进度\n\n### 背景\nbjb1-18228 上同时跑着 3 个 LIBERO spatial eval（10 tasks × 10 rollouts each）:\n- eval-spatial-v6-full (cuda:0, pid 109802, tmux) — SmolVLA VLA-only baseline\n- eval-acr-spatial-v2 (cuda:1, pid 110073, tmux) — ACR-VLA (SmolVLA + CRM per-DOF correction)\n- eval-reconvla-spatial-v3 (cuda:2, pid 110280, tmux) — SampleConsensus baseline (scalar argmin)\n\n另外还有一个 CRM ablation 训练:\n- crm-train-a3-obs-only (cuda:3, pid 104611, tmux) — CRM obs_only ablation\n\n### 你要做的\n1. SSH 到 bjb1-18228，检查这 4 个进程是否还在跑（ps -p PID）\n2. Tail 每个 eval 的日志，看完成了多少 tasks/rollouts，有无报错:\n   - eval-spatial-v6-full: `~/runs/acr-vla-conformal-refinement/eval-spatial-v6-full.log`\n   - eval-acr-spatial-v2: `~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v2.log`\n   - eval-reconvla-spatial-v3: `~/runs/acr-vla-conformal-refinement/eval-reconvla-spatial-v3.log`\n   - crm-train-a3-obs-only: 检查 tmux session 或 stdout log\n3. 如果有 eval 已经输出了部分 task 的成功率，记录下来（例如 \"Task 0: 7/10, Task 1: 5/10...\"）\n4. 检查 nvidia-smi 确认 4 张卡都在被使用\n\n### 产出\n写一个简洁的进度报告，包含:\n- 每个实验的进程状态（running/completed/error）\n- 已完成的 task 数 / 总 task 数\n- 任何已有的中间成功率数据\n- GPU 利用率\n- 预估剩余时间（如果能判断的话）\n\n### 服务器信息\n- 服务器: bjb1-18228\n- Python: /root/miniconda3/bin/python\n- 环境激活: source /root/miniconda3/etc/profile.d/conda.sh && conda activate base\n- 工作目录: /root/acr-vla-conformal-refinement",
  "tool_groups": "['ssh']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "tool_args": {
    "task_type": "monitor:spatial-eval-progress",
    "project": "acr-vla-conformal-refinement",
    "task_prompt": "## 任务：检查 bjb1-18228 上 3 个 spatial eval 的运行进度\n\n### 背景\nbjb1-18228 上同时跑着 3 个 LIBERO spatial eval（10 tasks × 10 rollouts each）:\n- eval-spatial-v6-full (cuda:0, pid 109802, tmux) — SmolVLA VLA-only baseline\n- eval-acr-spatial-v2 (cuda:1, pid 110073, tmux) — ACR-VLA (SmolVLA + CRM per-DOF correction)\n- eval-reconvla-spatial-v3 (cuda:2, pid 110280, tmux) — SampleConsensus baseline (scalar argmin)\n\n另外还有一个 CRM ablation 训练:\n- crm-train-a3-obs-only (cuda:3, pid 104611, tmux) — CRM obs_only ablation\n\n### 你要做的\n1. SSH 到 bjb1-18228，检查这 4 个进程是否还在跑（ps -p PID）\n2. Tail 每个 eval 的日志，看完成了多少 tasks/rollouts，有无报错:\n   - eval-spatial-v6-full: `~/runs/acr-vla-conformal-refinement/eval-spatial-v6-full.log`\n   - eval-acr-spatial-v2: `~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v2.log`\n   - eval-reconvla-spatial-v3: `~/runs/acr-vla-conformal-refinement/eval-reconvla-spatial-v3.log`\n   - crm-train-a3-obs-only: 检查 tmux session 或 stdout log\n3. 如果有 eval 已经输出了部分 task 的成功率，记录下来（例如 \"Task 0: 7/10, Task 1: 5/10...\"）\n4. 检查 nvidia-smi 确认 4 张卡都在被使用\n\n### 产出\n写一个简洁的进度报告，包含:\n- 每个实验的进程状态（running/completed/error）\n- 已完成的 task 数 / 总 task 数\n- 任何已有的中间成功率数据\n- GPU 利用率\n- 预估剩余时间（如果能判断的话）\n\n### 服务器信息\n- 服务器: bjb1-18228\n- Python: /root/miniconda3/bin/python\n- 环境激活: source /root/miniconda3/etc/profile.d/conda.sh && conda activate base\n- 工作目录: /root/acr-vla-conformal-refinement",
    "tool_groups": "['ssh']"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-13T23:21:33.156552+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_monitor_spatial-eval-progress_20260513T232118\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_monitor_spatial-eval-progress_20260513T232118.log\", \"setup_data\": {}, \"message\": \"Worker worker_monitor_spatial-eval-progress_20260513T232118 started. Use get_worker_status('worker_monitor_spatial-eval-progress_20260513T232118') to check progress.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "elapsed_ms": 15270
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-13T23:21:33.508422+00:00_

called mcp__agent-ml-research__spawn_worker

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker</summary>

```json
{
  "task_type": "research:next-batch-planning",
  "project": "acr-vla-conformal-refinement",
  "task_prompt": "## 任务：规划当前批次完成后的下一批实验\n\n### 背景\n项目 acr-vla-conformal-refinement 正在做 ACR-VLA（per-DOF conformal action correction for VLAs）的实验验证。\n\n当前正在运行:\n1. **3-way spatial comparison** (bjb1 cuda:0/1/2):\n   - eval-spatial-v6-full: SmolVLA VLA-only baseline\n   - eval-acr-spatial-v2: ACR-VLA (SmolVLA + CRM, checkpoint /root/autodl-tmp/checkpoints/crm/crm_best.pt)\n   - eval-reconvla-spatial-v3: SampleConsensus baseline (scalar argmin)\n2. **CRM ablation** (bjb1 cuda:3): crm-train-a3-obs-only (obs_only, no conformal features)\n3. **Object eval** (bjb2 cuda:0): eval-object-v5-full (VLA-only on object benchmark)\n\n已完成的关键结果:\n- MVP (plan_000): per-DOF > scalar > none, PASS\n- CRM v1 训练: val_loss=0.009046, 50 epochs, checkpoint ready\n- Precompute v4: 26737 samples (spatial 12167 + object 14570), 233MB cache\n\n### 你要做的\n1. 读 experiment_plan.yaml（用 read_experiment_plan_with_status）了解完整实验计划\n2. 读 paper_framing.md 了解论文 core claims\n3. 分析当前运行的实验覆盖了 plan 中的哪些格子\n4. 列出当前批次完成后，下一优先级的实验是什么:\n   - 如果 spatial 结果 positive（ACR-VLA > VLA-only）→ 下一步是什么\n   - 如果 spatial 结果 negative → 需要什么诊断实验\n   - obs_only ablation 完成后 → 还需要哪些 ablation\n   - object benchmark 的 ACR-VLA eval 什么时候跑（需要先 precompute object 的 cache 吗？已有 precompute-k5 包含 object）\n\n### 产出\n写一个优先级排序的下一批实验计划:\n- 每个实验: exp_id 建议、hypothesis、command sketch、预估时间、所需 GPU\n- 分 positive/negative 两个场景\n- 标注哪些实验可以并行",
  "tool_groups": "['knowledge', 'registry']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "tool_args": {
    "task_type": "research:next-batch-planning",
    "project": "acr-vla-conformal-refinement",
    "task_prompt": "## 任务：规划当前批次完成后的下一批实验\n\n### 背景\n项目 acr-vla-conformal-refinement 正在做 ACR-VLA（per-DOF conformal action correction for VLAs）的实验验证。\n\n当前正在运行:\n1. **3-way spatial comparison** (bjb1 cuda:0/1/2):\n   - eval-spatial-v6-full: SmolVLA VLA-only baseline\n   - eval-acr-spatial-v2: ACR-VLA (SmolVLA + CRM, checkpoint /root/autodl-tmp/checkpoints/crm/crm_best.pt)\n   - eval-reconvla-spatial-v3: SampleConsensus baseline (scalar argmin)\n2. **CRM ablation** (bjb1 cuda:3): crm-train-a3-obs-only (obs_only, no conformal features)\n3. **Object eval** (bjb2 cuda:0): eval-object-v5-full (VLA-only on object benchmark)\n\n已完成的关键结果:\n- MVP (plan_000): per-DOF > scalar > none, PASS\n- CRM v1 训练: val_loss=0.009046, 50 epochs, checkpoint ready\n- Precompute v4: 26737 samples (spatial 12167 + object 14570), 233MB cache\n\n### 你要做的\n1. 读 experiment_plan.yaml（用 read_experiment_plan_with_status）了解完整实验计划\n2. 读 paper_framing.md 了解论文 core claims\n3. 分析当前运行的实验覆盖了 plan 中的哪些格子\n4. 列出当前批次完成后，下一优先级的实验是什么:\n   - 如果 spatial 结果 positive（ACR-VLA > VLA-only）→ 下一步是什么\n   - 如果 spatial 结果 negative → 需要什么诊断实验\n   - obs_only ablation 完成后 → 还需要哪些 ablation\n   - object benchmark 的 ACR-VLA eval 什么时候跑（需要先 precompute object 的 cache 吗？已有 precompute-k5 包含 object）\n\n### 产出\n写一个优先级排序的下一批实验计划:\n- 每个实验: exp_id 建议、hypothesis、command sketch、预估时间、所需 GPU\n- 分 positive/negative 两个场景\n- 标注哪些实验可以并行",
    "tool_groups": "['knowledge', 'registry']"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-13T23:21:35.717689+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_research_next-batch-planning_20260513T232133\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_research_next-batch-planning_20260513T232133.log\", \"setup_data\": {}, \"message\": \"Worker worker_research_next-batch-planning_20260513T232133 started. Use get_worker_status('worker_research_next-batch-planning_20260513T232133') to check progress.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "elapsed_ms": 2209
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-13T23:22:19.446209+00:00_

called mcp__agent-ml-research__main_agent_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__main_agent_post_to_director</summary>

```json
{
  "text": "[资源] GPU 分配 5 / 实际在跑 5 (bjb1 cuda:0/1/2/3 + bjb2 cuda:0) | Worker 池 2 (GPU 0 / CPU 2)\n\n## Session 初始化状态汇报\n\n### 里程碑进展\n1. **CRM v1 训练完成** ✅ — val_loss=0.009046 (50 epochs), checkpoint: `/root/autodl-tmp/checkpoints/crm/crm_best.pt`\n2. **Precompute-k5 完成** ✅ — 26,737 samples (spatial 12,167 + object 14,570), 233MB cache, 用时 107min\n\n### 当前运行中（5 GPU 全满）\n\n**bjb1-18228 (4× RTX 4090):**\n| GPU | exp_id | 模式 | 说明 |\n|-----|--------|------|------|\n| cuda:0 | eval-spatial-v6-full | VLA-only | SmolVLA baseline (SFT gate) |\n| cuda:1 | eval-acr-spatial-v2 | ACR-VLA | **首次 ACR-VLA full eval**，用 crm-train-v1 checkpoint |\n| cuda:2 | eval-reconvla-spatial-v3 | SampleConsensus | 标量 argmin baseline 对比 |\n| cuda:3 | crm-train-a3-obs-only | CRM ablation | obs_only (无 conformal 特征), 验证 per-DOF 特征必要性 |\n\n**bjb2-40593 (1× RTX 4090 D):**\n| GPU | exp_id | 模式 | 说明 |\n|-----|--------|------|------|\n| cuda:0 | eval-object-v5-full | VLA-only | SmolVLA 在 object benchmark 的 baseline |\n\n### 关键路径\n这是项目启动以来**第一次 3-way 对比** (VLA-only vs ACR-VLA vs SampleConsensus) 在 LIBERO spatial 上同时运行。结果将决定:\n- ACR-VLA 是否有效（核心 hypothesis 验证）\n- SFT gate 是否通过（SmolVLA baseline 水平）\n- SampleConsensus 对比强度（scalar vs per-DOF 差异）\n\n### Worker 任务\n1. `monitor:spatial-eval-progress` — 检查 3 个 spatial eval 进度 + crm-train-a3-obs-only 状态\n2. `research:next-batch-planning` — 规划 positive/negative 两种场景的下一批实验\n\n### 待 Director 决策\n无阻塞项。等 eval 结果回调后按 on-experiment-done 分叉处理。",
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
    "text": "[资源] GPU 分配 5 / 实际在跑 5 (bjb1 cuda:0/1/2/3 + bjb2 cuda:0) | Worker 池 2 (GPU 0 / CPU 2)\n\n## Session 初始化状态汇报\n\n### 里程碑进展\n1. **CRM v1 训练完成** ✅ — val_loss=0.009046 (50 epochs), checkpoint: `/root/autodl-tmp/checkpoints/crm/crm_best.pt`\n2. **Precompute-k5 完成** ✅ — 26,737 samples (spatial 12,167 + object 14,570), 233MB cache, 用时 107min\n\n### 当前运行中（5 GPU 全满）\n\n**bjb1-18228 (4× RTX 4090):**\n| GPU | exp_id | 模式 | 说明 |\n|-----|--------|------|------|\n| cuda:0 | eval-spatial-v6-full | VLA-only | SmolVLA baseline (SFT gate) |\n| cuda:1 | eval-acr-spatial-v2 | ACR-VLA | **首次 ACR-VLA full eval**，用 crm-train-v1 checkpoint |\n| cuda:2 | eval-reconvla-spatial-v3 | SampleConsensus | 标量 argmin baseline 对比 |\n| cuda:3 | crm-train-a3-obs-only | CRM ablation | obs_only (无 conformal 特征), 验证 per-DOF 特征必要性 |\n\n**bjb2-40593 (1× RTX 4090 D):**\n| GPU | exp_id | 模式 | 说明 |\n|-----|--------|------|------|\n| cuda:0 | eval-object-v5-full | VLA-only | SmolVLA 在 object benchmark 的 baseline |\n\n### 关键路径\n这是项目启动以来**第一次 3-way 对比** (VLA-only vs ACR-VLA vs SampleConsensus) 在 LIBERO spatial 上同时运行。结果将决定:\n- ACR-VLA 是否有效（核心 hypothesis 验证）\n- SFT gate 是否通过（SmolVLA baseline 水平）\n- SampleConsensus 对比强度（scalar vs per-DOF 差异）\n\n### Worker 任务\n1. `monitor:spatial-eval-progress` — 检查 3 个 spatial eval 进度 + crm-train-a3-obs-only 状态\n2. `research:next-batch-planning` — 规划 positive/negative 两种场景的下一批实验\n\n### 待 Director 决策\n无阻塞项。等 eval 结果回调后按 on-experiment-done 分叉处理。",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-13T23:38:21.497419+00:00_

2 个 Worker 已派出。现在向 Director 汇报当前状态。

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

20 recorded events

### User

_source line 48 · 2026-05-14T03:12:13.382344+00:00_

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

_source line 49 · 2026-05-14T03:12:28.599603+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__list_workers",
  "max_results": "5"
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
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__list_workers",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-14T03:12:28.650220+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-14T03:12:32.078441+00:00_

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
  "session": "cron:hook:precompute-v4-shard2",
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

_source line 52 · 2026-05-14T03:12:32.130547+00:00_

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

_source line 53 · 2026-05-14T03:12:32.587174+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-vla-mean-spatial\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T03:10:44.114Z\", \"updated_at\": \"2026-05-14T03:11:46.546Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode vla_only --baseline_mode mean --benchmark spatial --n_rollouts 10 --seed 42\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"143106\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"SmolVLA K=10 mean action (no conformal)\", \"seed\": 42, \"hypothesis\": \"K=10 mean baseline isolates multi-sampling averaging contribution vs conformal correction. Expected between vla_only K=1 (30%) and ACR-VLA.\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"log_path\": \"/root/autodl-tmp/eval_results/eval-vla-mean-spatial.log\"}}, \"eval-object-v8-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T00:05:25.647Z\", \"updated_at\": \"2026-05-14T03:10:30.457Z\", \"spec\": {\"hypothesis\": \"SmolVLA baseline on libero_object with K=1 fix (vla_only single inference)\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 42\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"125830\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_object/\", \"data_count\": 100, \"model_name\": \"smolvla_libero\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/eval_results/eval-object-v6.log\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13, \"total_successes\": 13, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"s
…[truncated 44226 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 508
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-14T03:12:33.039118+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "report.md",
  "max_chars": "12000"
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
    "file": "report.md",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-14T03:12:33.592906+00:00_

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

_source line 56 · 2026-05-14T03:12:33.643466+00:00_

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

_source line 57 · 2026-05-14T03:12:39.218124+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 6, \"results\": [{\"exp_id\": \"eval-acr-spatial-v2\", \"success\": true, \"actions\": [\"Job still running (pid=117814)\"]}, {\"exp_id\": \"eval-reconvla-spatial-v3\", \"success\": true, \"actions\": [\"Job still running (pid=118108)\"]}, {\"exp_id\": \"eval-object-v8-full\", \"success\": true, \"actions\": [\"Stale cron removed (registry status=DONE)\"]}, {\"exp_id\": \"crm-train-k5\", \"success\": true, \"actions\": [\"Job still running (pid=139839)\"]}, {\"exp_id\": \"eval-scalar-unc-spatial\", \"success\": true, \"actions\": [\"Job still running (pid=143206)\"]}, {\"exp_id\": \"eval-vla-mean-spatial\", \"success\": true, \"actions\": [\"Skipped (created 45s ago < interval 300s)\"]}]}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 7087
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-14T03:12:39.268922+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md\", \"content\": \"# Handover — 2026-05-14\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| eval-vla-mean-spatial | — | — | — | — |\\n| eval-scalar-unc-spatial | — | — | — | — |\\n| crm-train-k5 | — | — | — | — |\\n\\n## 待处理\\n- eval-object-v6-full（准备中）\\n- eval-reconvla-spatial-v1（准备中）\\n- precompute-v4-shard2（准备中）\\n- precompute-v4-shard1（准备中）\\n- precompute-v4-shard0（准备中）\\n- eval-spatial-v4-full（准备中）\\n- precompute-v3-shard2（准备中）\\n- precompute-v3-shard1（准备中）\\n- precompute-v3-shard0（准备中）\\n- precompute-v2-shard2（准备中）\\n- …另有 2 项\\n\\n## 近期结论\\n- **eval-object-v8-full** (success): —\\n- **crm-train-a4-scalar-unc** (success): —\\n- **eval-spatial-v7-full** (success): —\\n\\n## 趋势\\n成功 10 / 负向 0 / 失败 3 / 共 23\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nbjb1-18228: 无 GPU 信息\\nbjb2-40593: 无 GPU 信息\\n\\n## 告警\\n- plan_001-crm-smolvla: 训练失败 — unknown\\n- plan_014-reconvla-baseline: 训练失败 — unknown\\n- eval-smolvla-libero-spatial: 训练失败 — unknown\\n- eval-spatial-reeval-v2: 已被终止 — unknown\\n- eval-spatial-v3-full: 已被终止 — unknown\\n- eval-object-v4-full: 已被终止 — unknown\\n- eval-spatial-v5-full: 已被终止 — unknown\\n- eval-reconvla-spatial-v2: 已被终止 — unknown\\n- eval-acr-spatial-v1: 已被终止 — unknown\\n- eval-acr-vla-spatial-v1: 已被终止 — unknown\\n- eval-spatial-v6-full: 已被终止 — unknown\\n- eval-object-v5-full: 已被终止 — unknown\\n- eval-object-v7-full: 已被终止 — unknown\\n\", \"total_chars\": 1346, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 6229
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-14T03:12:39.269474+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-13 19:10 UTC | 更新原因: D014: wrapper+evaluate.py 部署到服务器，v4 实验已启动\\n\\n## 核心方向\\nPer-DOF conformal statistics from multivariate CP on flow-matching VLA samples enable dimension-selective action correction. 详见 paper_framing.md。\\n\\n## 投稿目标\\n**ICLR 2027**（预计 DDL Sep-Oct 2026）。CoRL 2026 已放弃（D011）。\\n\\n## 当前进展\\n- **阶段**: Phase 1 — Eval + Precompute（修复版代码已部署验证）\\n- **MVP**: PASS（plan_000, per-DOF > scalar > none 确认）\\n- **D014**: wrapper+evaluate.py 修复版已部署到 bjb1-18228，grep 验证通过，v4 实验已启动\\n- **Wrapper 重构**: 完成，281 行，对齐 lerobot SmolVLAPolicy（flip+resize_with_pad+normalize[-1,1]+8D state+MEAN_STD+unnormalize）\\n- **Paper**: references.bib (31 entries) + related_work.tex (870 words) 已完成\\n\\n## 近期任务\\n- [x] ~~诊断 smolvla_libero 0% 根因~~ → 7 个 wrapper bug\\n- [x] ~~部分修复 + re-eval~~ → 55.6% 但不可靠（D013）\\n- [x] ~~Kill ghost 进程~~ → 多次清理完成\\n- [x] ~~Wrapper 重构~~ → 对齐 lerobot SmolVLAPolicy，Phase 4 验证 33%/67%\\n- [x] ~~部署修复版代码到服务器~~ → D014 wrapper+evaluate.py 部署验证通过\\n- [x] ~~Paper: bibliography + Related Work~~ → 完成\\n- [ ] **eval-spatial-v4-full** 运行中（cuda:0, PID 69379, ~2h）\\n- [ ] **precompute-v4-shard0/1/2** 运行中（cuda:1/2/3, ~35min）\\n- [ ] Precompute 完成后验证 cache 数据 + CRM 训练\\n- [ ] Full eval 完成后确认 SFT gate\\n- [ ] autodl-4090 部署 + object eval\\n\\n## SFT Gate（待重新评估）\\nD014: wrapper+evaluate.py 修复版已部署。等 eval-spatial-v4-full 结果（10 tasks × 10 rollouts）。\\n- ≥80% → 按计划推进\\n- 50-80% → 可继续，调低期望\\n- <30% → 换模型\\n\\n## GPU 预算\\n- autodl-4090x4 (bjb1-18228): 4× RTX 4090 → eval-spatial-v4(cuda:0) + precompute-v4(cuda:1/2/3)\\n- autodl-4090 (bjb2-40593): 1× RTX 4090 D → 代码部署中，待启动 object eval\\n- 总预算 ~200 GPU·h, 已用 ~25h, 剩余 ~175h\\n\\n## 关键路径\\n~~Wrapper 重构~~ → **Eval v4 (~2h)** + **Precompute v4 (~35min)** → CRM 训练 (4-6h) → ACR-VLA Eval (8-10h)\\nplan_
…[truncated 1157 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 5676
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-14T03:12:39.319969+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [], \"count\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 5676
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-14T03:12:44.339987+00:00_

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
  "session": "cron:hook:precompute-v4-shard2",
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

_source line 62 · 2026-05-14T03:12:45.094947+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md\", \"content\": \"# Memory — acr-vla-conformal-refinement\\n\\n## SmolVLA Wrapper 正确预处理规范（2026-05-13 16:00，7 个 bug 修复后验证通过）\\n\\n### 教训\\n初次 eval 0% 成功率，**7 个 wrapper bug 全部是预处理/后处理不匹配**。必须完全对齐 lerobot 官方推理管线。\\n\\n### 正确预处理（已验证 55.6% success）\\n| 步骤 | 正确做法 | 之前的 bug |\\n|------|----------|-----------|\\n| 图像翻转 | `torch.flip(dims=[2,3])` 翻转 H+W | 无翻转 |\\n| 图像尺寸 | `resize_with_pad(512, 512)` | `Resize(256,256)` |\\n| 图像值域 | `img * 2.0 - 1.0` → [-1,1] | `ToTensor()` → [0,1] |\\n| State 维度 | **8D**: eef_pos(3) + eef_axisangle(3) + gripper_qpos(2) | 6D（缺 gripper） |\\n| State 归一化 | `(s - mean) / (std + ε)` MEAN_STD | 原始值直接传入 |\\n| Action 反归一化 | `a * std + mean` MEAN_STD | 模型原始输出 |\\n| Camera names | env_args 指定 `[\\\"agentview\\\", \\\"robot0_eye_in_hand\\\"]` | 只有 agentview |\\n\\n### Normalizer 文件\\n- State: `policy_preprocessor_step_5_normalizer_processor.safetensors` (8D mean/std)\\n- Action: `policy_postprocessor_step_0_unnormalizer_processor.safetensors` (7D mean/std)\\n- 路径: 模型目录下\\n\\n### ⚠️ Precompute 数据需重做\\n之前 3-shard precompute（spatial + object）用的是 buggy wrapper → K-samples 和 obs_features 全部错误。**必须用修复后的 wrapper 重新 precompute 才能训练 CRM。**\\n\\n## evaluate.py rollout_single 正确初始化顺序（2026-05-13 23:35，两轮修复后确认）\\n\\n**正确顺序**:\\n```python\\nenv.reset()                           # 1. 清除 terminated flag\\nobs = env.set_init_state(init_state)  # 2. 设目标初始状态（覆盖 reset 的随机状态）\\nfor _ in range(5):\\n    obs, _, _, _ = env.step(np.zeros(7))  # 3. 物理稳定\\n```\\n\\n**两个 bug 历史**:\\n1. 原始 bug: `env.reset()` 在 `set_init_state()` **之后**调用 → 覆盖了 demo 初始状态\\n2. 过度修复: 完全删除 `env.reset()` → 前一个 rollout terminated 后 env.step() 抛 ValueError\\n\\n**教训**: env.reset() 必须存在（清 terminated flag），但必须在 set_init_state 之前。两台服务器代码必须同步验证。eval 脚本修改后做 init_state 保持验证。\\n\\n## vla_only 模式 K=1 修复（2026-05-14 00:00）\\n\\n**问题**: evaluate.py 默认 K=10 多采样，即使 vla_
…[truncated 3474 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 754
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-14T03:12:45.095496+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__load_project_config",
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
    "query": "select:mcp__agent-ml-research__load_project_config",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-14T03:12:45.146311+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-14T03:12:47.661728+00:00_

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
  "session": "cron:hook:precompute-v4-shard2",
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

_source line 66 · 2026-05-14T03:12:47.712434+00:00_

{"result":"{\"success\": true, \"data\": {\"project\": \"acr-vla-conformal-refinement\", \"section\": \"execution\", \"config\": {\"execution\": {\"account\": \"root\", \"gpu_constraint\": [\"autodl-4090:cuda:0\"], \"gpu_ids\": [\"bjb2-40593:cuda:0\", \"bjb1-18228:cuda:0\", \"bjb1-18228:cuda:1\", \"bjb1-18228:cuda:2\", \"bjb1-18228:cuda:3\"], \"project_path\": \"/root/acr-vla-conformal-refinement\", \"servers\": [\"bjb2-40593\", \"bjb1-18228\"]}}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__load_project_config",
  "elapsed_ms": 50
}
```

</details>

---

### Assistant

_source line 67 · 2026-05-14T03:13:50.702032+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- GPU 白名单：bjb2-40593:cuda:0, bjb1-18228:cuda:0/1/2/3。禁止使用白名单外 GPU
- Ablation 系列实验必须用 baseline 超参 bs=32/lr=1e-3，否则 confound 对比
- evaluate.py 的 env.reset() 必须在 set_init_state() **之前**，顺序不可改（两次踩坑）
- vla_only 模式必须 K=1（已加强制代码），其他模式 K=10
- ReconVLA baseline 实际命名为 SampleConsensus（scalar Euclidean argmin），不要混淆为完整 CQR 版 ReconVLA
- crm-train-a4-scalar-unc 的 val_loss(0.008379) < per-DOF(0.009046) 不代表 scalar 更好——**必须看 task success rate**（eval-scalar-unc-spatial 正在跑）

### 2. 🖥️ 基础设施快照
- **bjb1-18228**（4× RTX 4090）：工作目录 `/root/acr-vla-conformal-refinement`，Python `/root/miniconda3/bin/python`，conda base
  - 数据：`/root/autodl-tmp/libero_data/`（spatial + object）
  - CRM cache K=10：`/root/autodl-tmp/crm_cache/`（26737 samples）
  - CRM cache K=5：`/root/autodl-tmp/crm_cache_k5/`（26737 samples）
  - Checkpoints：`/root/autodl-tmp/checkpoints/crm/`（crm_best.pt = per-DOF baseline）
  - Scalar CRM：`/root/autodl-tmp/checkpoints/crm/scalar_unc/crm_best.pt`
  - K=5 CRM：`/root/autodl-tmp/checkpoints/crm/k5/`（训练中）
  - 模型：`/root/autodl-tmp/models/smolvla_libero/`
  - Eval 输出：`/root/autodl-tmp/eval_results/`
- **bjb2-40593**（1× RTX 4090 D）：同路径结构，`/root/autodl-tmp/` 下数据+模型
- **活跃进程**（cron 监控中）：
  - eval-acr-spatial-v2: PID 117814, bjb1 cuda:1
  - eval-reconvla-spatial-v3: PID 118108, bjb1 cuda:2
  - eval-scalar-unc-spatial: PID 143206, bjb1 cuda:3
  - crm-train-k5: PID 139839, bjb1 cuda:0
  - eval-vla-mean-spatial: PID 143106, bjb2 cuda:0
- **HF 环境变量**：HF_HUB_OFFLINE=1, TRANSFORMERS_OFFLINE=1（AutoDL 网络隔离）

### 3. 📊 当前状态
5/5 GPU 全部在跑，0 个 Worker 活跃。所有 5 个 RUNNING 实验由 cron 监控，等回调即可。

**RUNNING 实验（全部是 spatial benchmark 评估 + K=5 训练）**：
| exp_id | GPU | 内容 | 预计产出 |
|--------|-----|------|---------|
| eval-acr-spatial-v2 | bjb1:1 | **ACR-VLA 主实验**（per-DOF CRM + SmolVLA） | 核心数据点：ACR-VLA vs 30% baseline |
| eval-reconvla-spatial-v3 | bjb1:2 | SampleConsensus baseline（scalar argmin） | 对比基准 |
| eval-scalar-unc-spatial | bjb1:3 | Scalar CRM（3D unc）eval | Ablation A4 task-level 验证 |
| crm-train-k5 | bjb1:0 | K=5 CRM 训练 | K 敏感性 ablation |
| eval-vla-mean-spatial | bjb2:0 | K=10 mean action baseline | 隔离 multi-sampling 贡献 |

**已完成关键结果**：
- SmolVLA spatial baseline = **30%**（eval-spatial-v7-full）
- SmolVLA object baseline = **13%**（eval-object-v8-full）
- CRM per-DOF val_loss = 0.009046，obs_only = 0.018312（2x 差距，conformal features 价值确认）
- CRM scalar_unc val_loss = 0.008379（略好于 per-DOF，但 hypothesis 是 per-DOF 在 task success 上胜出）
- MVP 通过：per-DOF > scalar > none（6.75% / 16.71% improvement）

### 4. 📋 待办（条件触发式）
- **eval-acr-spatial-v2 完成** → 这是最关键数据点。≥35% (>30% baseline) = success claim 成立 → 汇报 Director + 铺 object benchmark eval。<30% = negative → 按 red-section 产 Framing 提案
- **eval-reconvla-spatial-v3 完成** → 与 ACR-VLA 对比，计算 improvement over SampleConsensus
- **eval-scalar-unc-spatial 完成** → 对比 per-DOF vs scalar task success rate（val_loss 逆转 hypothesis，task success 是决定性的）
- **crm-train-k5 完成** → spawn worker eval-k5-spatial（用 K=5 checkpoint 跑 spatial eval），与 K=10 对比 K 敏感性
- **eval-vla-mean-spatial 完成** → 与 vla_only K=1 (30%) 对比，量化 multi-sampling averaging 贡献
- **所有 spatial 评估完成** → 铺 object benchmark 全系列（ACR-VLA / SampleConsensus / scalar / mean / K=5）
- **ACR-VLA 显著 >30%** → 启动论文 Experiments section 写作 + 画图

### 5. 🎯 战略上下文
- **项目核心**：ACR-VLA = SmolVLA + per-DOF conformal CRM。从"选最好的 sample"（ReconVLA/SampleConsensus）到"合成修正 action"的范式跃迁
- **投稿目标**：ICLR 2027（DDL Sep-Oct 2026），时间充裕
- **当前阶段**：Phase 1 eval 矩阵正在填充。spatial benchmark 5 个实验并行跑，结果出来后铺 object benchmark
- **最容易判断错的事**：
  1. scalar CRM val_loss 比 per-DOF 好（0.008 vs 0.009）但这不意味 scalar 赢——必须等 task success rate。如果 scalar 在 task success 上也赢了，核心 claim 需要 reframe
  2. 30% SmolVLA baseline 偏低（文献报告 ~80%+），但这是社区 checkpoint 不是我们自己训的。不要因为 baseline 低就怀疑整个 pipeline——ACR-VLA 的 improvement 才是 claim
  3. SampleConsensus baseline（我们实现的）低估了真实 ReconVLA（用 CQR 分位数回归），后续可能需要更强的 ReconVLA Medium baseline
- **决策链**：D008(用社区 checkpoint) → D011(放弃 CoRL，目标 ICLR) → D013(wrapper 需对齐 lerobot) → D014(修复版部署验证通过)
- **代码坑已填**：evaluate.py env.reset 顺序 bug、wrapper 7 个预处理 bug、vla_only K=10 浪费问题——全部修复并验证
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
