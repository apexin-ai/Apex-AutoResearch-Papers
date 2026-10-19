# reviewer / loop_5.md

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_5.md`
- **Structured JSON:** [`53ddfa4299bbebe7bb1a.json`](../../sessions/53/53ddfa4299bbebe7bb1a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_wall_time
updated: '2026-05-25T20:29:16+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 C001：westd-35807 仅 cuda:0-3，westd-45947 仅 cuda:0-1。越界即 CRITICAL。
- eval_safelibero.py 已修复 CUDA_VISIBLE_DEVICES override bug（L1141-1146），新启动 eval 时确认脚本是修复后版本（条件检查外部 CUDA_VISIBLE_DEVICES），否则进程会全落在 --gpu 指定的卡上导致冲突。
- seed0_l005 和 seed0_l01 无 best/ checkpoint（只有 30000/），不要安排 best checkpoint eval。
- "frozen_pct" 在 registry 和 displacement_analysis 中含义不同：registry 里指 obstacle displacement < threshold；displacement_analysis_30k_summary.txt 里指 EE displacement < threshold（机械臂冻结）。引用时必须区分。

### 2. 🖥️ 基础设施快照
- **westd-35807**（root）：代码 `/root/colliforce-vla`，checkpoint `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/`，eval 输出 `/root/autodl-tmp/eval_results/`，conda env `libero`
- **westd-45947**（root）：同上路径结构，LoRA baseline checkpoint 在 `a1_sdf_pi05_object_pudding/pi05_lora_baseline_object_pudding_seed{0,1}/`
- 服务器 westd-35807 约 2026-05-26 01:11 UTC 重启过，所有进程均为重启后恢复
- 活跃进程（westd-35807）：
  - GPU 0: PID 3717, tmux=train_pi05_a1_spatial_bowl_s0_l005, step ~9790/30000, ~4.63s/it
  - GPU 1: PID 142394, eval_pi05_a1_30k_s1_l005_disp（displacement 验证重跑）
  - GPU 2: PID 134344, eval_pi05_a1_best_s1_l005_16k（seed1 best checkpoint）
  - GPU 3: PID 151915, eval_pi05_a1_30k_s0_l005_r4（seed0 30K 带 displacement）
- 活跃进程（westd-45947）：
  - GPU 0: PID 3634, train_pi05_lora_baseline_s0（从 step 24000 恢复，ETA ~09:30 UTC）
  - GPU 1: PID 3724, train_pi05_lora_baseline_s1（从 step 24000 恢复，ETA ~09:30 UTC）

### 3. 📊 当前状态
刚完成 eval_pi05_a1_best_s2_l005_10k 的 EE displacement 全量分析审查，已 post 给 Director（WARNING）。核心发现：
- 10K best checkpoint 确认 learned avoidance（EE 0.39-0.58m，机械臂真实运动）
- 30K 全部 100% frozen（EE < 10mm），3 seeds × 2 lambdas 一致
- 已标记 registry 中 `task2_fake_safety: true` 与分析结论矛盾的命名问题

Registry RUNNING 实验（13 个，多数是旧版已完成但未更新状态的）：
- **真正活跃的 6 个**：上面基础设施快照中列出的 3 eval + 1 training（westd-35807）+ 2 LoRA baseline（westd-45947）
- eval 预计 ~10:30 UTC 完成（重启后刚跑 12-26 分钟，还需 ~6h）
- LoRA baseline ETA ~09:30 UTC

### 4. 📋 待办（条件触发式）
- eval_pi05_a1_best_s1_l005_16k 完成 → 独立核实 seed1 best(16K) 的 EE displacement 模式是否与 seed2 best(10K) 一致（期望 EE > 0.3m = learned avoidance），交叉验证 action collapse 是 training step 问题而非 seed 特异性
- eval_pi05_a1_30k_s1_l005_disp 完成 → 验证 30K displacement 数据加入后 frozen 100% 模式是否持续（预期是），确认修复脚本正确输出 max_ee_displacement 字段
- eval_pi05_a1_30k_s0_l005_r4 完成 → 同上，seed0 的 30K displacement 数据
- LoRA baseline s0/s1 训练完成 → 关注 eval 安排，LoRA baseline 的 CAR 应接近 Pi0.5 baseline (~27%)，如果显著高于 baseline 说明 LoRA 本身就有避障效果（会削弱 SDF 归因）
- Agent 注册 eval_pi05_a1_best_s0_l005 → 拦截：seed0 无 best/ checkpoint，应 KILL

### 5. 🎯 战略上下文
- **核心叙事**：ColliForce SDF auxiliary loss 在 10K sweet-spot 产生真实碰撞避免（EE 运动 + 低障碍物碰触），但 30K 退化为 action collapse（机械臂冻结）。论文需要同时讲清楚 positive（10K learned avoidance）和 limitation（30K collapse + TSR 仅 9%）
- **决策链**：D020（30K TSR 退化 = safety-performance tradeoff）→ D021（EE displacement 替代 obstacle displacement 作为真/假安全判据）
- **最易判断错的事**：
  1. 不要把 registry 中的 `frozen_pct` 和 displacement analysis 中的 `Frozen%` 等同——前者是 obstacle displacement，后者是 EE displacement
  2. 10K best checkpoint 不是"纯粹成功"——avg_TSR 仅 9%，Task 0/2/3 的 TSR 全为 0%。论文不能过度宣称 10K 的实用性
  3. 服务器可能再次重启（已发生一次），重启后所有 eval PID 会变，需要重新核实进程
  4. LoRA baseline 日志文件为空（0 bytes）——输出在 tmux 中，tail_training_logs 看不到。验证进度需看 checkpoint 目录时间戳


---
