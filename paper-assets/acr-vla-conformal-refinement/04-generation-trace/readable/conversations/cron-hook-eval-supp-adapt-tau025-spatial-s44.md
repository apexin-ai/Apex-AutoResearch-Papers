# cron hook eval supp adapt tau025 spatial s44

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 4
- **Recorded user turns:** 1
- **Tool calls:** 1
- **Original source:** `logs/chats/cron_hook_eval-supp-adapt-tau025-spatial-s44.jsonl`
- **Structured JSON:** [`9bd4eab3da269777b078.json`](../../sessions/9b/9bd4eab3da269777b078.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

4 recorded events

### User

_source line 1 · 2026-05-24T00:55:47.655348+00:00_

[HANDOFF] 你是 Main Agent，这是 Loop #26。

## 上一轮交接 (task_context)

### 1. 🔴 硬约束 / 红线
- GPU 白名单由 `get_project_status` 的 `execution.gpu_ids` 决定，当前 5 台服务器各自分配不同。即使 Director 说"用 cuda:X"也必须 push back 如果不在白名单
- SmolVLA precompute 必须基于 lerobot 官方代码修改的 wrapper pipeline，禁止使用 native precompute（D120/D123）
- Adaptive CRM 的 τ=0.25 是确认的最优值（D129）；Object Suite 之前用了错误的 τ=0.074855 导致 negative（77.5%），必须用 correct τ=0.25 重跑
- CRM checkpoint 路径：SmolVLA 3-suite 统一用 `/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt`；4-suite 版本 `train-crm-unified-4suite-r6` 正在训练中（bjb1-32546:cuda:3）
- π0.5 precompute 是 best-effort 背景任务（D126），不要为它抢 SmolVLA 评估的 GPU

### 2. 🖥️ 基础设施快照
- **bjb1-32546**: 6×GPU，工作目录 `/root/acr-vla-conformal-refinement`，conda base（`/root/miniconda3/bin/python`）
  - 活跃：`train-crm-unified-4suite-r6` (cuda:3, PID 668382), `eval-supp-crm-norm005-spatial-s44` (cuda:5, PID 759215)
  - π0.5 precompute ×4 running (PID 113456/113796/114159/114507)
- **bjb2-28827**: 6×GPU，同路径同环境
  - 活跃 6 个 eval：goal-adapt-tau025-s42(cuda:2), k2mean-object-s42(cuda:1), k2mean-spatial-s42(cuda:4), goal-reconvla-s42(cuda:3), obj-adapt-tau025-s42(cuda:0), goal-vla-only-wrapper-s42(cuda:5)
- **cqa1-32758**: 6×RTX 4090D，同路径同环境
  - 活跃 6 个 eval：k2mean-spatial-s43(cuda:0), reconvla-spatial-s43(cuda:1), k2mean-object-s43(cuda:2), reconvla-spatial-s44(cuda:3), k2mean-goal-s43(cuda:4), goal-reconvla-s43(cuda:5)
- **bjb2-40593**: eval-supp-k2mean-goal-s42-r2 running
- **bjb1-18228**: 无活跃实验，磁盘 95% ⚠️
- CRM checkpoint: `/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt`
- W&B: 项目配置中有 entity/project，用 `fetch_wandb_metrics` 查询
- 磁盘告警：bjb2-40593 根分区 90%，cqa1-32758 autodl-pub 97%

### 3. 📊 当前状态
**刚做完**：收到 `eval-supp-adapt-tau025-spatial-s44` (Adaptive CRM τ=0.25, Spatial seed44) 完成回调，已派 Worker (`worker_analyze_eval-supp-adapt-tau025-spatial-s44_20260523T084318`) 去读日志提取 metrics 并更新 registry。**Worker 尚未回调**。

**等待中的 Worker 回调**：
- `worker_analyze_eval-supp-adapt-tau025-spatial-s44_20260523T084318` — 分析 seed44 结果

**RUNNING 实验（19 个 cron 监控中）**：
| 类别 | 实验 | 摘要 |
|------|------|------|
| 训练 | train-crm-unified-4suite-r6 | 4-suite CRM 训练，完成后解锁 Long Suite 全套评估 |
| Spatial 补充 | eval-supp-crm-norm005-spatial-s44, eval-supp-reconvla-spatial-s43/s44 | multi-seed 填矩阵 |
| Object 补充 | eval-supp-k2mean-object-s42/s43, eval-supp-obj-adapt-tau025-s42 | Object Suite 覆盖 |
| Goal 补充 | eval-supp-goal-adapt-tau025-s42, eval-supp-k2mean-goal-s42-r2/s43, eval-supp-goal-reconvla-s42/s43, eval-goal-vla-only-wrapper-s42 | Goal Suite 覆盖 |
| K=2 mean | eval-supp-k2mean-spatial-s42/s43 | Spatial K=2 mean 补充 |
| π0.5 | precompute-pi05-{object,spatial,goal,long}-2048-r2 ×4 | 背景 precompute（预计 25-60h） |

**PENDING/QUEUED**：
- eval-smolvla-crm-goal-seed44 (PENDING，等人工审批)
- eval-smolvla-lerobot-goal-seed44 (QUEUED，等 GPU)

### 4. 📋 待办（条件触发式）
- Worker `analyze_eval-supp-adapt-tau025-spatial-s44` 回调 → 确认 metrics → 计算 Spatial Adaptive 3-seed mean±std → 更新 ROADMAP → 汇报 Director（含 3-seed 统计显著性判断）
- 每个 eval-supp-* 完成回调 → on-experiment-done 流程（提取 metrics → update registry → 判断 conclusion → 更新 report.md → 汇报 Director）
- train-crm-unified-4suite-r6 完成 → 解锁 Long Suite 全套评估（VLA-only/CRM/Reconvla/Adaptive/K=2mean），需立即规划并提交 Long 评估实验
- Spatial 3-seed 全收齐（s42✅ s43✅ s44 pending Worker） → 计算 5 种方法的 3-seed mean±std，更新 ROADMAP 矩阵
- Object/Goal 各方法 seed42 全收齐 → 开始 multi-seed 补充
- 所有 SmolVLA 矩阵填满 → 开始论文 Results 撰写

### 5. 🎯 战略上下文
- **DDL: CoRL 2026 = 2026-05-29（≤6天）**，2-model paper (SmolVLA 0.4B + π0.5 3.6B)
- **核心 story**：Adaptive CRM 用不确定性门控选择性校正（τ=0.25 时 trigger_rate 仅 ~19%），在保持/提升 SR 的同时大幅降低计算开销
- **D129 关键发现**：Spatial Adaptive CRM 3-seed（s42=82%, s43=80%, s44=pending）仅 +1.0pp over VLA-only（79.8%），p=0.25 不显著。但 Goal Suite CRM always-on 有 +14.5pp 大幅提升——**Goal 可能是论文最强 claim 的来源**
- **D128**：CRM 问题确认为 overcorrection magnitude（非方向错误），norm=0.05 比 norm=0.2/0.3 好
- **易错点**：
  - Object Suite 之前有 τ=0.074855 的错误实验（negative），必须用 τ=0.25
  - K=2 argmin 因 centroid bug（K=2 → d1==d2 → always picks sample 0）等价于 K=1 VLA-only，这证明了 CRM correction 是提升来源而非 sampling diversity
  - VLA-only baseline 各 suite 有不同的 3-seed mean：Spatial 79.8%±1.2%, Object 77.8%±1.0%, Goal 用的是单 seed 71.0%（需补 multi-seed）
  - π0.5 VLA-only 全 4 suite 饱和 (94-99%)，CRM 在高 baseline 上的 headroom 很小，π0.5 的 narrative 需要聚焦在"即使强模型也能从 conformal refinement 获益"

## 可查的历史
前 262 轮 handoff 在 `task_context/history/agent/loop_*.md`，如有疑问可 Read 回查。
完整聊天归档可用 `recall_session_history("关键词")` 搜索。

## 第一个动作要求
1. 用 `read_registry` 确认当前 RUNNING/PREPARING 实验状态（防止幻觉记忆过时状态）
2. 回复一句话确认你看到了上面的硬约束 + 当前活跃实验，再开始任何工具调用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:eval-supp-adapt-tau025-spatial-s44",
  "source": "system:ralph_loop"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-24T00:56:03.924638+00:00_

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
  "session": "cron:hook:eval-supp-adapt-tau025-spatial-s44",
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

_source line 3 · 2026-05-24T00:56:03.925255+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-supp-adapt-tau025-spatial-s44",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 4 · 2026-05-24T00:56:04.475542+00:00_

You've hit your limit · resets 3pm (UTC)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval-supp-adapt-tau025-spatial-s44"
}
```

</details>

---
