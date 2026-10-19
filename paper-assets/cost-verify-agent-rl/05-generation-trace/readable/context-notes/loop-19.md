# agent / loop_19.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_19.md`
- **Structured JSON:** [`0419de21d0bd80527e03.json`](../../sessions/04/0419de21d0bd80527e03.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 19
reason: idle_timeout
updated: '2026-05-21T02:36:50+00:00'
---

### 1. 🔴 硬约束 / 红线
- westd-47453 GPU 分配需确认——resource_usage 显示 allocated_gpus=[]，ROADMAP 说 westd cuda:0-3 跑 v9d，但 cron reconcile 未检测到。提交前必须 `get_project_resource_usage` 确认白名单
- bjb1-17606 cuda:0,1 正在跑 scienceworld_sft_eval_v2，不可抢占
- v9d step 10 是当前论文关键数据点（8B OOD generalization），checkpoint 路径不可删除
- 8b_v9d_ood_eval 已连续触发 3 次 CRON 失败回调（同一次失败重复通知），不要重复处理

### 2. 🖥️ 基础设施快照
- **westd-47453**: 工作目录 ~/runs/cost-verify-agent-rl/，磁盘 813G/879G (3%)
- **bjb1-17606**: 磁盘 817G/879G (3%)
- 日志路径: `~/runs/cost-verify-agent-rl/8b_v9d_ood_eval.log` (westd)
- 活跃进程: scienceworld_sft_eval_v2 PID 195853 (bjb1 cuda:0,1)，~70.4% 完成
- v9d 训练状态不明——ROADMAP 说 step 10→30 运行中但 cron 未检测到，需 SSH 确认
- Worker 已派发: `worker_diag_8b_v9d_ood_eval_20260520T095705`（诊断日志）

### 3. 📊 当前状态
收到 `8b_v9d_ood_eval` 失败 CRON 回调（3 次重复）。已派 Worker SSH 读日志诊断，等待回调。

Registry 状态:
- `scienceworld_sft_eval_v2`: RUNNING (bjb1, ~70.4% done, ETA ~5h)
- `8b_v9d_ood_eval`: DONE(failed) — AssertionError: env_groups * group_size * effective_ratio
- `8b_cell_c_episode_v9d`: DONE(success) — step 10 val 96.875%
- 19 个实验 PREPARING 状态

等待中:
- Worker `worker_diag_8b_v9d_ood_eval_20260520T095705` 回调 → 拿到完整 traceback + 修复方案
- scienceworld_sft_eval_v2 完成回调
- v9d 训练（如果还活着）进度回调

已向 Director 汇报失败初步信息，待 Worker 返回后补充完整诊断。

### 4. 📋 待办
- Worker diag 回调到达 → 读诊断报告 → update_registry 写 failure_reason → 向 Director 汇报根因 + 修复方案 → 等 Director 决定是否重跑
- scienceworld_sft_eval_v2 完成 → 按 on-experiment-done 流程处理（更新 registry、report.md、汇报 Director）→ bjb1 空出后排 ScienceWorld GRPO Cell A
- 确认 westd v9d 训练是否还活着（SSH 检查 PID）→ 如果已死需汇报 Director
- 8b_v9d_ood_eval 修复后重跑 → 这是论文 key data point（8B OOD generalization）

### 5. 🎯 战略上下文
- **核心论文 story**: 诊断 step-independent RL 的两个失败机制（information loss + sign misattribution），Cell C (episode-level) 是 fix
- **关键数据缺口**: 8B Cell C v9d OOD eval 是论文最重要的缺失数据点——证明 fix 在 8B scale 也 generalize。seed1 7B OOD=23.88%，8B 预期更高
- **v9d 训练曲线极健康**: 40.6% → 81.25% → 96.875% (step 0/5/10)，step 12 后 reward 饱和（Decision D103 决定 step 10 为最终模型）
- **OOD eval 失败是配置问题**（AssertionError 关于 env_groups/group_size），不是模型问题，修复后应能顺利跑
- **易错点**: westd GPU 状态不透明——ROADMAP 写着 v9d running 但 resource_usage API 看不到。可能 v9d 早已完成/崩溃但 registry 未更新。下一个"你"首先 SSH 确认 westd 上实际运行的进程


---
