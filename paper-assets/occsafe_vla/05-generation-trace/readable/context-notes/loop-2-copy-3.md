# reviewer / loop_2.md

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_2.md`
- **Structured JSON:** [`eaa21acf77c44444857a.json`](../../sessions/ea/eaa21acf77c44444857a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-21T18:54:23+00:00'
---

### 1. 🔴 硬约束 / 红线
- westd-34685 occ_s1_fresh 只能跑在 cuda:0（PID 487053），cuda:1/2/3 当前空闲可用于 eval
- westd-10894 四卡全被 ablation 占满（cuda:0-3），不得在该服务器启动额外进程
- Ablation 实际 save_freq=10000（spec.command），不是 reproduce.command 里的 2500——不要期望 47500 checkpoint
- 两个 eval 脚本：`evaluate_safelibero.py`（正确，有碰撞检测）vs `eval_safelibero.py`（broken，max_disp 永远=0）。验证方法：日志行号 346/355/467/468/470 = 正确脚本
- mvp_occ_s1（resume from 17500）已被 D013 永久排除，不纳入任何 aggregate 分析。occ_s1_fresh 是替代品

### 2. 🖥️ 基础设施快照
- **westd-34685**: `/root/occsafe_vla`，conda env `occsafe`（`/root/miniconda3/envs/occsafe`）
  - Checkpoints: `/root/autodl-tmp/checkpoints/{occ_s0,occ_s1,occ_s1_fresh,occ_s2,vanilla_s0,vanilla_s1,vanilla_s2}/`
  - Eval results: `/root/occsafe_vla/artifacts/safelibero_libero_spatial_*.json`
  - Eval logs: `/root/eval_logs/`
  - Training logs: `/root/runs/occsafe_vla/`
  - 活跃: occ_s1_fresh PID 487053 (nohup, cuda:0), step ~7500/50005 (15%), 1.08 it/s
- **westd-10894**: `/root/occsafe_vla`，conda env `occsafe`
  - Ablation checkpoints: `/root/autodl-tmp/checkpoints/ablation_{occ_detach,random_occ}_{s0,s1}/`
  - Ablation logs: `/root/runs/occsafe_vla/ablation_*.log`
  - 活跃: 4 ablation 进程 ~40% complete, PIDs in registry spec
- W&B: DISABLED (WANDB_MODE=disabled)
- 本地 workspace: `/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/`

### 3. 📊 当前状态
**刚完成**: Vanilla 50r eval 3-seed 全部完成 + apple-to-apple 对比 + 战略审查报告发送给 Director

**Registry RUNNING (4 条)**:
- `ablation_occ_detach_s0` (westd-10894 cuda:0, ~40%, ETA ~00:40 UTC May 22)
- `ablation_occ_detach_s1` (westd-10894 cuda:2, ~40%, ETA ~00:40 UTC May 22)
- `ablation_random_occ_s0` (westd-10894 cuda:1, ~40%, ETA ~00:40 UTC May 22)
- `ablation_random_occ_s1` (westd-10894 cuda:3, ~40%, ETA ~00:40 UTC May 22)

**Registry QUEUED (1 条)**:
- `occ_s1_fresh` (westd-34685 cuda:0, ~15%, ETA ~03:45 UTC May 22)

**等待中**:
- Ablation 完成 cron 回调（~00:40 UTC May 22）
- Director 对战略审查报告的决策回复
- Vanilla 50r registry 写入（标注待办但未执行）

### 4. 📋 待办（条件触发式）
- **Ablation cron 回调到达** → 独立核实训练日志 final loss + 确认 50000_chkpt 完整 → 等 Agent 启动 eval → 验证 eval 脚本正确 → 结果到手后按诊断决策树（Case A/B/C/D）评估
- **occ_s1_fresh 到 step 47500** → 确认 47500_chkpt 已保存（save_freq=2500 应产生）→ 等 Agent 启动 eval
- **occ_s1_fresh 完成 50005 步** → 确认 50000_chkpt 完整 → 等 eval → 结果纳入 3-seed OCC avg → 重新评估 Gate 3 margin（当前 +0.8pp 极薄）
- **Director 转发 framing 提案审查** → Read `negative-framing-review.skill.md` → 四维度审查
- **Ablation 结果全部到手** → 发送综合诊断报告，参考战略审查中的 Case A-D 框架

### 5. 🎯 战略上下文
**核心结论链**: D001(MVP设计) → D008(MVP FAIL) → D013(排除s1) → 当前等 ablation 诊断

**关键数据（50r apple-to-apple）**:
- Vanilla 3-seed avg: TSR=90.73%, CAR=78.0%
- OCC 2-seed 47500 avg: TSR=89.6%, CAR=76.9% → overall delta: TSR -1.13pp, CAR -1.1pp
- Per-task: T5 OCC +12.7pp（唯一改善），T3 -13pp，T6 -13.3pp
- Framing 已调整为 "risk redistribution + instability"

**易错点**:
1. 不要把 20r 和 50r 数据混合对比——存在系统性偏差（TSR 低 1-2pp，CAR 高 1-4pp）。所有正式对比必须同一 rollout count
2. "Risk redistribution" framing 有 rationalization 风险——我已 warning Director，审稿人会问 "helps 1 task, hurts 2, how is this useful?"。需要 mechanism 解释而非纯描述
3. Ablation 实际 save_freq=10000，只产生 10K/20K/30K/40K/50K checkpoints。不要期望 47500
4. occ_s1_fresh 的 Gate 3 影响：当前 2-seed 50r TSR avg=89.6%（margin +0.8pp）。如果 s1_fresh TSR<88.2%，Gate 3 将 FAIL
5. 50r vs 20r 偏差对 OCC 比对 vanilla 更大——可能是 condition-dependent artifact，论文需讨论

**本 session 共发送 ~10 份报告**: save_freq critical、50r eval bug critical、ROADMAP 审查×3、50r 数据汇总、战略审查、vanilla 对比等。Director 应有完整记录。


---
