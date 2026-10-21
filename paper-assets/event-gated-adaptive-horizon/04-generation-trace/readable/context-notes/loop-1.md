# director / loop_1.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_1.md`
- **Structured JSON:** [`f07d906a7a0ac079ba7d.json`](../../sessions/f0/f07d906a7a0ac079ba7d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-13T18:34:31+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：只能用 bjb1-45299 的 cuda:0 和 cuda:1，不可越界
- 启动实验必须 `CUDA_VISIBLE_DEVICES=X`（X=0或1），防止 CUDA context 泄漏
- 必须传 `--compile False`（PyTorch 2.10 torch.compile 有断言错误）
- 必须设 `LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6`
- GPU 预算已达 ~30 GPU·h，30h 上限待用户确认扩至 40h（尚未确认）
- exp_005 启动前已做 gate_max_dt vs effective_max_dt 全量审计（18 处，8 处已修），后续任何涉及 gate 参数的代码修改必须重新审计

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-45299 (connect.bjb1.seetacloud.com)，SSH 名从 autodl-rtx6000 改过来的（同一物理机）
- 工作目录：`/root/autodl-tmp/event-gated-adaptive-horizon`
- Python：`/root/miniconda3/bin/python`（conda base，不是 venv）
- 环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa`
- GPU: 2× RTX PRO 6000 (96GB each), CUDA 12.8
- 活跃进程：
  - exp_001_baseline: PID 9409, cuda:0, step ~376K/500K, eval_return ~920
  - exp_005_event_gated_v4: PID 51721, cuda:1, tmux=exp_005_event_gated_v4, step ~40K, logdir=`logdir/event_gated_v5_s1`
- Cron：两个实验均已注册监控

### 3. 📊 当前状态
所有等待期任务已完成，正在等 exp_005 到达 60-70K 验证窗口（约 5-6h 后）。

已完成的等待期工作：
- narrative_frameworks.md：成功线/失败线/gray zone 三条叙事，已按 Reviewer 修正（去 rationalization、加单任务 caveat）
- related_work_section.md：15 篇论文正式初稿，四类分组，Reviewer 四点修正已落地
- Reviewer 已独立评估 pivot 方案（结论：Option 2 K=2 优先，等 exp_005 Phase 2 结果再决策）

Registry: exp_001 RUNNING, exp_005 RUNNING, exp_002 DONE(failed), exp_003 DONE(negative), exp_004 DONE(negative)

### 4. 📋 待办
- exp_005 step 到 50-55K → 主动检查 gate_scale 是否开始上升（Phase 2 启动确认）
- exp_005 step 到 60-70K → **关键验证**：gate_loss 是否正常（<10，非百万级）+ eval_return 是否 ≥ 60% baseline（~550）。稳定 → 继续跑到 200K；崩塌 → 立即汇报 Director
- exp_005 step 到 200K + return ≥ 80% baseline → MVP PASS，调 complete_mvp()，进入 post-MVP kickoff（paper_framing.md → experiment_plan.yaml → dream_simulate）
- exp_005 return < 80% baseline 且 bug 全修完 → 执行 pivot：先跑 K=2 binary skip（~10h，最低成本诊断），结果决定后续走 sparse task 还是 soft mixture
- exp_001 baseline 到 500K → 锁定最终 metrics，cuda:0 空出后可启动 Cheetah Run baseline（D007，暂缓中）
- 用户确认 GPU 预算扩容 → 更新 ROADMAP

### 5. 🎯 战略上下文
- 核心假设：学习型事件门控在 DreamerV3 RSSM 上可行。3/4 MVP 标准已 PASS（gate entropy/H_eff/dt autocorr），criterion 1（return ≥ 80% baseline）因连续 3 个实现 bug 失败，exp_005 是 bug 全修后的首次验证
- 决策链：D001(MVP 方案) → D002(量化标准) → D003(subsample curriculum) → D004(中期评估 3/4 PASS) → D005/D006(imagination dt + λ-return 修复) → D007(Cheetah Run baseline，暂缓) → D008(gate_loss 爆炸，全量审计+架构改进)
- **最容易判断错的事**：exp_005 Phase 2 gate_loss 如果出现异常值（>100），不要立即判断为新 bug——先确认是瞬态还是持续。但如果持续 >1000 步，确实是新 bug
- **容易踩的坑**：SSH 配置名是 bjb1-45299 不是 autodl-rtx6000（同一台机器，已改名）；DreamerV3 GPU 利用率 6-40% 是正常的（CPU-bound 架构）不要误报
- Reviewer pivot 评估已完成：K=2 binary skip 最优先（成本最低的诊断实验），soft attention mixture 最后考虑（新代码新 bug 风险高）


---
