# agent / loop_20.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_20.md`
- **Structured JSON:** [`1cfd846383a1893fca4b.json`](../../sessions/1c/1cfd846383a1893fca4b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 20
reason: idle_timeout
updated: '2026-05-21T20:47:26+00:00'
---

### 1. 🔴 硬约束 / 红线
- `get_project_resource_usage` 显示 allocated_gpus=[]（registry 未同步），但实际 westd 4 GPU 全在跑。提交新实验前必须确认 GPU 实际空闲
- bjb1-17606 cuda:0,1 当前空闲，seed4 prep worker 已派但尚未回调——不要重复派发同类型 worker
- v9d step 10 checkpoint 是论文关键数据点（8B OOD generalization），路径不可删除
- exp029_seed3_ood_v2 可能 hang（GPU 0%，日志停在 09:56），诊断 worker 正在跑——不要盲目 kill，等诊断结果
- Cell C v3 止损阈值：step 5 success=0% + action_is_valid<20% → 终止释放 GPU（ROADMAP 明确）

### 2. 🖥️ 基础设施快照
- **westd-47453**: 工作目录 ~/runs/cost-verify-agent-rl/，磁盘 813G/879G (3% free)
  - cuda:0,1 → exp029_seed3_ood_v2 (PID 530289，可能 hang)
  - cuda:2,3 → scienceworld_grpo_cell_c_v3 (PID 88226，step 3/15，已跑 ~8h)
  - 日志：~/runs/cost-verify-agent-rl/ 下各实验 .log 文件
- **bjb1-17606**: 磁盘 817G/879G (3% free)，cuda:0,1 空闲
  - 之前跑过 scienceworld_sft_eval_v2（已完成 success）
- Cron 活跃：scienceworld_grpo_cell_c_v3（reconcile 确认 pid=88226 alive）

### 3. 📊 当前状态
Session 20 初始化完成，已向 Director 汇报。

Registry RUNNING:
- `exp029_seed3_ood_v2`: westd cuda:0,1，seed3 OOD 134-task eval（⚠️ 疑似 hang）
- `scienceworld_grpo_cell_c_v3`: westd cuda:2,3，step 3/15，success=0, action_is_valid=9.4%, ETA step 5 约 4h

Worker 活跃:
- `worker_experiment_seed4-bjb1-prep_20260521T024319` — 在 bjb1 准备 seed4 episode-level GRPO
- `worker_ops_seed3-ood-v2-progress_20260521T024207` — 诊断 seed3 OOD eval 是否 hang（已 9 turns，发现 GPU 0%）

等待:
- 两个 Worker 回调
- Cell C v3 step 5 产出（~4h 后）→ 止损判断
- Director 回复 session 20 汇报

### 4. 📋 待办
- seed3-ood-v2-progress worker 回调 → 如确认 hang → kill PID 530289 → 重跑 eval → 更新 registry
- seed3-ood-v2-progress worker 回调 → 如正常运行 → 等完成回调 → 按 on-experiment-done 处理
- seed4-bjb1-prep worker 回调 → 确认环境就绪 → submit_training_job → 注册 cron
- Cell C v3 step 5 cron 回调 → 检查 val metrics → success=0% + action_is_valid<20% → kill + 向 Director 汇报 + 释放 westd cuda:2,3 → 排下一个实验（8b_v9d_ood_eval 修复重跑？）
- seed3 OOD eval 完成 → 关键数据点（seed3 OOD success rate）→ 更新论文 Table 1 multi-seed mean → westd cuda:0,1 释放排下一个

### 5. 🎯 战略上下文
- **论文 story**: 诊断 step-independent RL 的 dual failure mechanism (info loss + sign misattribution)，Cell C (episode-level) 是 fix
- **论文接近完成**: D108 已更新 multi-seed mean 17.2% [10.4-23.9%]，待 Reviewer 一致性审查 + Cell C v3 step 5 决定
- **Claim 强度**: 诊断 VERY STRONG / 修复 STRONG（D104）
- **Cell C v3 大概率止损**: step 3 success=0, action_is_valid=9.4%——ScienceWorld 环境下 episode-level GRPO 信号极弱，与 ALFWorld 的成功形成对比。止损后论文 narrative 不变（ScienceWorld Cell C 标注为 inconclusive / negative，Limitations 已覆盖 fix generality）
- **易错点**: seed3 OOD v2 看起来是 eval 但可能加载了完整模型做 rollout（FSDP config），GPU 0% 不一定 = hang，可能是 CPU-bound 阶段。等 worker 诊断再判断
- **8b_v9d_ood_eval 已失败 4 次**（v1-v4 全 AssertionError），但 8B OOD 已有 90.3% 数据（plan_021 7b_sft_eval_ood）。v9d OOD 是 nice-to-have 不是 blocker


---
