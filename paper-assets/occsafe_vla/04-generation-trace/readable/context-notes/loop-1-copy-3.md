# reviewer / loop_1.md

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`296cdd60ee0dc9af0584.json`](../../sessions/29/296cdd60ee0dc9af0584.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-21T01:38:49+00:00'
---

### 1. 🔴 硬约束 / 红线
- **occ 实验只在 westd-34685**，vanilla 实验只在 westd-10894。多次有 Worker 在错误服务器上操作（M018 事故），务必核对 hostname。
- **occ_s1 恢复命令必须包含全部超参数**，特别是 `--num_images_in_input 2` 和 `--use_proprio True`（default 分别是 1 和 False）。已因此浪费 3 次重启。验证时必须检查 **子进程** `/proc/{PID}/cmdline`，不是 wrapper bash PID。
- **westd-34685 的 cleanup_checkpoints.sh 已 rename 为 .DISABLED**，但文件仍在磁盘。绝对不能重新启动任何 cleanup 脚本——已导致 occ_s1 crash + 所有 occ seed 丢失 10K-27.5K checkpoint。
- **cron on_failed 对 torchrun 进程会产生假阳性**——EXIT_CODE=143 是 torchrun destroy_process_group 的正常行为，不是真 crash。收到 on_failed 先查 log 里有无 "Max step 50005 reached!"。

### 2. 🖥️ 基础设施快照
- **westd-10894** (root): vanilla 实验，代码 `/root/occsafe_vla/openvla-oft/`，数据 `/root/autodl-tmp/data/modified_libero_rlds/`，checkpoint `/root/autodl-tmp/checkpoints/vanilla_s{0,1,2}/`，eval 结果 `/root/occsafe_vla/eval_results/`，conda env `occsafe`
- **westd-34685** (root): occ 实验，同样代码/数据路径结构，checkpoint `/root/autodl-tmp/checkpoints/occ_s{0,1,2}/`，conda env `occsafe`
- **活跃进程 (westd-34685)**:
  - occ_s0: PID 27667→子进程 27740, cuda:0, ~57% (~28K/50K)
  - occ_s1: PID 58875 (第3次正确重启), cuda:1, ~15% (从 7500 resume)
  - occ_s2: PID 29970→子进程 30044, cuda:2, ~57% (~28K/50K)
  - cuda:3 卡死，不可用
- **westd-10894**: 全部 vanilla 训练+eval 已完成，GPU 空闲（可能有 s0 intermediate eval 残余）
- 本地 workspace: `/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/`

### 3. 📊 当前状态
**Vanilla baseline 完整确立（3 seeds）**: TSR=91.8%±1.2%, CAR=77.0%±0.4%

Per-task 数据（3-seed mean）:
- Easy tasks (T0/T1/T2/T4/T7/T8/T9): CAR ≥90%，上限效应
- Hard tasks: T3=26.7%, T5=8.3%, T6=45.0%（方差极大：T3 range=35pp, T6 range=25pp）
- T5 TSR 系统性退化：35K 85-95% → 50K 40-65%（3 seeds 一致）

**Learning curve 已收集**:
- s0: 35K(69.5%)→40K(70%)→45K(74.5%)→50K(77.5%) — CAR 单调递增
- s1: 35K(70%)→40K(72.5%)→45K(73%)→50K(76.5%) — CAR 单调递增

**等待中**:
- occ_s0/s2 训练完成 → ETA ~05:30 UTC May 21 → auto-eval
- occ_s1 训练完成 → ETA ~12:30 UTC May 21 → eval
- MVP gate 判定 → ~13:00 UTC May 21

**Registry**: mvp_vanilla_s0/s1/s2 全部 DONE；mvp_occ_s0/s1/s2 RUNNING（registry notes 可能过时，occ 重启信息未完全同步）

**method.tex 第 7 个 bug 未修**: L24/L42 仍写 "DINOv2 patch features"，应为 "DINOv2+SigLIP concatenated features (dim=2176)"

### 4. 📋 待办（条件触发式）
- **occ_s0/s2 训练完成（~05:30 UTC）→** 核实 50000_chkpt 存在 + eval 自动触发 + 确认 GPU 白名单
- **occ eval 结果出来 →** 立即做 per-task CAR/TSR 对比 vanilla baseline，计算 overall delta + hard-task delta，判定 MVP gate（CAR≥82%, hard-task CAR≥39%, TSR≥88.8%）
- **occ CAR delta < 5pp →** 这是 existential risk（概率 30-40%），需要评估 paper narrative pivot 选项
- **occ CAR delta ≥ 5pp but hard-task variance > delta →** 建议追加 rollouts 到 50/task 或 bootstrap CI
- **s0 intermediate eval 40K/45K 结果出来 →** 合并 s0+s1 learning curve 数据，验证 CAR 单调性
- **任何 occ cron on_failed →** 先查 log 确认是否假阳性（143），再查 cleanup 是否复活

### 5. 🎯 战略上下文
**核心假设已被部分证伪**: 原假设 "vanilla VLA CAR ~15%" 完全错误，实际 77%。Paper narrative 必须从 "VLA 缺乏安全意识" 转向 "VLA 在特定高碰撞风险场景（T3/T5/T6）下安全性不足"——claim 范围大幅缩窄。

**MVP gate 的真正战场是 3 个 hard tasks**：7 个 easy tasks 已被 vanilla ceiling 封死（CAR≥90%），occ 只能在 T3/T5/T6 上拉分。整体 +5pp 需要 hard-task mean +17pp。

**最容易判断错的事**:
1. tqdm 显示的 step 是 relative（从 resume 点算起），不是 actual step。actual = resume_step + tqdm_step。多次有 Worker 误读。
2. occ_s1 比 s0/s2 晚 ~7h 完成（从 7500 resume vs s0/s2 从 0 跑），不要等 s1 才做 s0/s2 的分析。
3. Hard-task CAR 的 seed 间方差极大且非单调（T3 在 s1 中 35K→50K 反而下降），不要对单 seed 数据下结论。
4. 速度是配置正确性的强信号：occ 正确配置 ~1.08 it/s，错误配置（缺 num_images=2）~2.07 it/s。GPU 显存也是：正确 ~62GB，错误 ~43GB。


---
