# director / loop_1.md

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_1.md`
- **Structured JSON:** [`08311589eecc2c282258.json`](../../sessions/08/08311589eecc2c282258.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-21T01:38:59+00:00'
---

### 1. 🔴 硬约束 / 红线
- **GPU 分配**: westd-10894 (cuda:0/1/2/3) 跑 vanilla + eval; westd-34685 (cuda:0/1/2) 跑 occ 训练。cuda:3 on 34685 卡死不可用，等 occ 完成后重启实例才能恢复
- **occ 训练在 westd-34685**，vanilla 训练在 westd-10894。之前 Worker 搞混服务器导致 M018，任何 occ 相关操作必须明确指定 westd-34685
- **checkpoint 路径**: westd-34685 上 occ checkpoint 在 `/root/autodl-tmp/checkpoints/occ_s{0,1,2}/`（不是 `/root/occsafe_vla/checkpoints/`）
- **cleanup 脚本已全部 kill**，但脚本文件仍在磁盘 (`/root/autodl-tmp/cleanup_*.sh`)，绝不能重启它们
- **kill 训练进程必须 kill 子进程**（不是 wrapper），验证用子进程 `/proc/PID/cmdline`，用 nvidia-smi 确认 GPU 释放
- **恢复训练必须从同组 seed 的 /proc/PID/cmdline 复制完整参数**，只改 seed + resume_step，禁止手写命令

### 2. 🖥️ 基础设施快照
- **westd-10894** (connect.westd.seetacloud.com:10894, root): vanilla 训练+eval 服务器
  - 工作目录: `/root/occsafe_vla/`
  - eval 结果: `/root/occsafe_vla/eval_results/`
  - Checkpoints: `/root/occsafe_vla/checkpoints/vanilla_s{0,1,2}/50000_chkpt/`
  - monitor_and_eval.sh (PID 226828) 可能仍在运行（vanilla 已全部完成，不再需要）
  - 4 卡全空闲，可用于 occ eval
- **westd-34685** (connect.westd.seetacloud.com:18685, root): occ 训练服务器
  - 工作目录: `/root/occsafe_vla/`
  - Checkpoints: `/root/autodl-tmp/checkpoints/occ_s{0,1,2}/`
  - eval 结果目录: `/root/occsafe_vla/eval_results/`
  - monitor_and_eval_occ.sh 存在但**未启动**（需在 occ 完成前 ~1h 手动启动）
  - 活跃进程:
    - occ_s0: PID 27667 (wrapper) → 子进程 27740, cuda:0, ~57%, ETA ~05:30 UTC May 21
    - occ_s1: PID 58875 (子进程), cuda:1, 从 7500 恢复, ~15%, ETA ~12:30 UTC May 21
    - occ_s2: PID 29970 (wrapper) → 子进程 30044, cuda:2, ~57%, ETA ~05:30 UTC May 21
  - cuda:3 卡死（compute 100% 但 0 MiB memory，无进程）
- **Post-MVP ablation 脚本已准备好** (westd-10894):
  - `scripts/run_occ_detach.sh` ✅ 可直接跑
  - `scripts/run_random_occ.sh` ✅ 可直接跑
  - `scripts/run_depth.sh` + `depth_head.py` ⚠️ 需集成 + depth GT labels（Depth Anything V2，~半天）

### 3. 📊 当前状态
**刚完成**:
- Vanilla 3-seed baseline 完整确立: TSR=91.8%±1.2%, CAR=77.0%±0.4%
- Vanilla CAR learning curve (s0+s1, 35K/40K/45K/50K): CAR 单调递增 69.75%→77.0%
- occ_s1 经 4 次事故(M015-M018)后用正确参数从 7500 成功重启
- Paper framing 更新: Scenario B confirmed, per-task 叙事为核心, 6 个 contingency scenario 已规划
- D007: MVP gate 追加 hard-task CAR ≥10pp 辅助判据

**等待中**:
- occ_s0/s2 训练完成 (~05:30 UTC May 21) → 需启动 eval
- occ_s1 训练完成 (~12:30 UTC May 21) → eval → MVP gate 判定 (~13:00 UTC)
- s0 intermediate eval 数据可能已完成（Worker 之前在跑，结果未汇报）

### 4. 📋 待办（条件触发式）
- **occ_s0/s2 接近完成 (~04:30 UTC)** → 在 westd-34685 启动 `monitor_and_eval_occ.sh`（或手动触发 eval）
- **occ_s0/s2 eval 完成** → 读取 per-task TSR/CAR，与 vanilla baseline 初步对比；如果 CAR 差异在 CI 内（<5pp），考虑追加到 50 rollouts/task
- **occ_s1 训练完成 (~12:30 UTC)** → eval → 三 seed 汇总 → MVP gate 判定
- **MVP gate PASS (CAR≥82%, hard-task CAR≥39%, TSR≥88.8%)** → `complete_mvp()` → 进入 research 阶段 → 写 experiment_plan.yaml → dream_simulate
- **MVP gate FAIL (CAR<82%)** → 检查 hard-task-only CAR 是否满足辅助判据(≥10pp)；如果硬任务改善明显但 overall 不够 → 讨论是否通过；如果完全无效(<5pp) → existential risk #1 触发，讨论 pivot
- **occ_s0/s2 eval 出来且 CAR 信号强** → 可以不等 s1，先开始 paper framing 升级和论文写作准备

### 5. 🎯 战略上下文
- **核心假设**: BEV occ auxiliary supervision 在 VLA fine-tuning 时诱发 implicit collision avoidance。尚未验证——全部取决于 occ eval 结果。
- **Vanilla baseline 比预期强**: 原假设预测 ~15% CAR，实际 77%。Reviewer 的 Scenario B (CAR≈75-80%) 命中。叙事已从 "overall 高碰撞" 调整为 "per-task: physically challenging tasks 碰撞率 53-92%"
- **最大 existential risk**: occ CAR 提升 <5pp（概率 30-40%）→ 无论文
- **最容易判断错的事**: (1) 不要被 overall CAR 数字迷惑——真正的差异只在 T3/T5/T6 三个 hard tasks 上；(2) occ_s1 比 s0/s2 晚 ~7h，不要因此只看 2 seed 就下结论；(3) 20 rollouts 的 per-task CI 很宽(±21pp)，如果结果模糊必须追加 rollouts
- **决策链**: D001(MVP方案) → D002(判定标准) → D003(范围缩小) → D004(AAAI 2027) → D005(post-MVP 扩展) → D006(vanilla_s2 重启) → D007(追加 hard-task gate)
- **错题本 M012-M018**: 核心教训是 (1) tqdm 显示不等于实际 step（有 resume offset）；(2) 技术写作必须 SSH 读代码不能凭记忆；(3) cleanup 脚本是定时炸弹；(4) kill 要 kill 子进程树；(5) 操作前确认服务器
- **Paper 预写部分已完成**: method.tex, experiments.tex, related_work.tex, discussion.tex 全部 code-aligned（经 Reviewer 3 轮审查）


---
