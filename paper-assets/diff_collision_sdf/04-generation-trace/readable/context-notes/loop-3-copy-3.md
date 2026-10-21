# reviewer / loop_3.md

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_3.md`
- **Structured JSON:** [`da3875fac7cfa88180ec.json`](../../sessions/da/da3875fac7cfa88180ec.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_wall_time
updated: '2026-05-22T18:33:47+00:00'
---

### 1. 🔴 硬约束 / 红线
- westd-35807 允许 cuda:0-3，westd-45947 允许 cuda:0-1（C001 约束）
- CUDA_VISIBLE_DEVICES 在 tmux session 中可能被覆盖失效（本 session 已发现 3 次），必须用 nvidia-smi 独立验证实际 GPU 分配，不能只信环境变量
- A1 eval 用 `model_type=lora_baseline`，输出文件名会和 LoRA baseline 撞名——已发生一次覆盖事故（A1 object eval 覆盖了 LoRA baseline JSON）
- Cron 在 WANDB_MODE=disabled 时会误判完成的实验为 "failed"——所有 cron:on_failed 通知必须先验证实际进程状态再判断

### 2. 🖥️ 基础设施快照
- **westd-35807**: `/root/colliforce-vla`, conda env `libero`, Python `/root/miniconda3/envs/libero/bin/python`
  - checkpoints: `/root/autodl-tmp/checkpoints/`（baseline_*/a1_sdf_*/a3_grad_refine_*）
  - eval results: `/root/autodl-tmp/eval_results/`
  - 活跃进程（截至 handoff）:
    - PID 727358 cuda:0: A1 spatial eval（Task 2 ~60/200）
    - PID 697980 cuda:1: baseline full-FT spatial eval（Task 3 刚开始）
    - PID 780772 cuda:2: A3 M024fix object eval（Task 1 ~150/200）
    - PID 859190 cuda:3: oracle A3 M024fix force refine（Task 3 ~20/40，即将完成）
- **westd-45947**: `/root/colliforce-vla`, conda env `base`
  - PID 191747 cuda:0: a3_gradient_spatial_bowl 训练（85%→预计 ~20:15 UTC 完成）
  - cuda:1: 空闲
- WANDB: 多数实验 disabled

### 3. 📊 当前状态
**刚完成的关键分析**:
- Oracle A3 force refine (pre-M024fix): CAR=81.2%, TSR=0%——比 baseline v11 (83%) 低 1.8pp，force refine 有 modest 效果但不超越 baseline
- A1 object eval: CAR=90%, TSR=0%, 但 displacement 极低 (~3mm)——CAR 提升是假象（不动=不碰）
- A3 M024fix eval 中间结果: refined=0 仍未触发（sdf_min 0.18-0.69，margin 0.01 太低），但 SDF 值比 pre-fix 低
- Oracle M024fix 中间结果: Task 2 CAR=97.5% 但 displacement=0.0000m——M024 fix 后 gradient 方向可能更偏向"不动"
- Baseline full-FT spatial: Tasks 0-2 CAR=0%（600/600 碰撞），TSR=1.5% (3/200) 仅在 Task 0

**等待中**:
- oracle_a3_m024fix_object_v11: ~5min 完成
- eval_a3_object_m024fix_v11: ~1.5h
- eval_a1_lora_spatial_v11: ~1.5h
- eval_baseline_fullft_spatial_v11: ~1h (Task 3)
- a3_gradient_spatial_bowl 训练: ~2h
- eval_a1_lora_object_v11_rerun: 排队等 cuda:3 释放（cron 已误报 failed）

### 4. 📋 待办（条件触发式）
- oracle_a3_m024fix 完成 → 对比 pre-fix oracle (CAR=81.2%)，评估 M024 坐标修复对 gradient refinement 的实际影响
- eval_a3_object_m024fix_v11 完成 → 对比 A3 v11 (CAR=74.5%) 和 baseline (83%)，M024 fix 是否改善 non-force-refine 的 CAR
- eval_a1_lora_spatial_v11 完成 → 对比 baseline spatial (CAR=0%) 和 LoRA baseline spatial (CAR=0%)，看 A1 是否在 spatial 有任何改善（已见 1 success + 1 non-collision）
- baseline_fullft_spatial 完成 → 综合报告 spatial_bowl 场景各方法对比
- a3_gradient_spatial_bowl 训练完成 → cron 可能误报 failed（WANDB disabled），验证 30000 checkpoint 存在即确认完成
- eval_a1_object_rerun 启动后 → 核查 GPU 分配是否正确（CUDA_VISIBLE_DEVICES 失效风险）

### 5. 🎯 战略上下文
**核心发现链**:
1. A3 gradient refinement 从未触发过（refine_count=0）——根因是 SDF decoder 输出 0.3-0.97，远 > refine_margin=0.01
2. M024 坐标 bug（delta→absolute）已修复，SDF 值降到 0.18-0.69 但 margin 仍太低
3. 即使 force refine（oracle），A3 仅 +6.7pp over no-refine，且不超越 baseline
4. A1 SDF auxiliary loss 导致 action collapse——位移 ~3mm，CAR 高但无意义
5. spatial_bowl Level II 所有方法 CAR=0%（碰撞阈值 0.001m 极严），是全面失败的场景

**最易判错的点**:
- **不要把 A1 CAR=90% 当成成功** — 位移 3mm 意味着机器人没在动，CAR 高是因为不运动
- **不要把 A3 "refine_count=0" 当成 A3 无效** — 是阈值问题，但 oracle 测试显示即使修复阈值效果也有限
- **Oracle M024fix displacement=0.0000m** — M024 坐标修复可能使 gradient 方向更偏向"不动"，这比 pre-fix 更差
- spatial_bowl 的 200 ep/task 评估需要 ~3.5h，不要因为没快速出结果就以为卡住


---
