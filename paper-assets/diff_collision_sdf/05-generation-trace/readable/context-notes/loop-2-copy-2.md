# agent / loop_2.md

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_2.md`
- **Structured JSON:** [`1532487192eef8755359.json`](../../sessions/15/1532487192eef8755359.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-25T19:22:43+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-35807 cuda:0/1/2/3 + westd-45947 cuda:0/1，共 6 张，不得用白名单外 GPU
- Checkpoint 路径陷阱：实际路径是 `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed{X}_l{YYY}/`，不是 `/root/autodl-tmp/openpi/checkpoints/`（多个 Worker 踩过这个坑）
- eval_safelibero.py 的 `--checkpoint` 参数名不是 `--checkpoint_path`（部分 registry spec 写错了，以实际脚本 help 为准）
- LoRA baseline 已 3 次 crash-resume，checkpoint 链：首次→step16000 resume→tmux 崩溃停在 ~25700→从 24000 resume2。不要假设有连续 checkpoint
- Displacement 修复刚合入但当前 RUNNING eval 用的是旧代码（已加载到内存），输出 JSON **不含** `max_ee_displacement`。修复验证需等 GPU 空闲后重跑

### 2. 🖥️ 基础设施快照
- **westd-35807**（4×H800 97GB）
  - 工作目录：`/root/colliforce-vla/`
  - Python：`/root/miniconda3/bin/python`，conda env `libero`
  - 激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate libero`
  - Checkpoints：`/root/autodl-tmp/checkpoints/a1_sdf_pi05_*/`
  - Eval 输出：`/root/autodl-tmp/eval_results/`
  - 磁盘：32% 用（570GB 可用）
  - 活跃进程：
    - cuda:0: spatial_bowl 训练（tmux `train_pi05_a1_spatial_bowl_s0_l005`，从 step 8000 resume）
    - cuda:1: eval s0_l005（Worker 已派，等回调确认 PID）
    - cuda:2: eval s0_l01（Worker 已派，等回调确认 PID）
    - cuda:3: eval best_s2_10k（PID 75114/72596，多次重启，tmux `eval_pi05_a1_best_s2_l005_10k`）
  - Cron：eval_pi05_a1_best_s2_l005_10k 已通过 submit_training_job 自动注册

- **westd-45947**（2×H800 97GB）
  - 同上环境配置
  - 磁盘：4% 用（400GB 可用）
  - 活跃进程：
    - cuda:0: LoRA baseline s0（PID 3622，tmux，step 24000→30000，ETA ~09:30 UTC 5/26）
    - cuda:1: LoRA baseline s1（PID 3712，tmux，step 24000→30000，ETA ~09:30 UTC 5/26）
  - Cron：两个 LoRA baseline 已注册（interval 120s）

### 3. 📊 当前状态
刚完成服务器重启恢复：6/6 GPU 全部恢复运行。同时处理了 displacement 度量 bug（P0 发现 + 代码修复）。

**RUNNING 实验**：
| exp_id | 服务器 | GPU | 摘要 |
|--------|--------|-----|------|
| train_pi05_a1_spatial_bowl_s0_l005 | westd-35807 | 0 | 跨场景泛化训练，8K→30K |
| eval_pi05_a1_30k_s0_l005 | westd-35807 | 1 | 30K eval seed0 λ=0.005（待确认启动） |
| eval_pi05_a1_30k_s0_l01 | westd-35807 | 2 | 30K eval seed0 λ=0.01（待确认启动） |
| eval_pi05_a1_best_s2_l005_10k | westd-35807 | 3 | best checkpoint eval 200eps |
| train_pi05_lora_baseline_s0 | westd-45947 | 0 | LoRA-only baseline 24K→30K |
| train_pi05_lora_baseline_s1 | westd-45947 | 1 | LoRA-only baseline 24K→30K |

**等待中**：
- Worker `worker_ops_gpu_status_check_all_20260525T191845` 回调（全 GPU 状态确认）
- Worker `worker_ops_eval_s0_l005_cuda1` 和 `worker_ops_eval_s0_l01_cuda2` 回调
- Worker `worker_diag_lora_baseline_log_check` 回调（诊断日志，可能已过时因 resume 已完成）
- 多个旧 eval 实验（s1_l005_v2/v3, s1_l01_v2, s2_l005_v2/v3, s2_l01_v2）状态仍为 RUNNING 但已有 metrics 且进程已死——需要批量标记 DONE

### 4. 📋 待办（条件触发式）
- GPU status check Worker 回调 → 向 Director 汇报完整 GPU 分配表
- eval s0_l005 / s0_l01 Worker 回调 → 确认启动成功，注册 cron
- 任一 eval 完成（cron 回调）→ **立即用该 GPU 重跑 s1_l005_30k 验证 EE displacement 修复**（Director P2 指示）
- LoRA baseline s0/s1 完成（ETA 09:30 UTC）→ 启动 LoRA baseline eval + 填充论文 §5.4
- spatial_bowl 训练完成（ETA ~5/27）→ spatial_bowl eval
- 修复验证通过 → 铺开重跑所有需要 displacement 数据的 eval
- 批量清理：将已有 metrics 但进程已死的旧 eval 实验标记为 DONE(success)

### 5. 🎯 战略上下文
- **核心发现**：VLA safety 评估中 action collapse 导致 metric contamination（A1-openpi 91.5% CAR 中 99.6% 是 fake）。Pi0.5+A1 SDF auxiliary loss 在 10K 步时展示真实避碰（CAR +30pp, frozen=0%），但 30K 步出现 TSR 退化
- **P0 bug**：`analyze_displacement.py` 的 frozen 检测用障碍物位移而非 EE 位移，导致 Filtered CAR ≡ 0% 是数学恒等式。**代码已修复**（新增 `max_ee_displacement` + `total_ee_path_length`），但未经验证。所有已发布的 Filtered CAR=0% 数据需要用 EE displacement 重新计算
- **决策链**：D012(pass/fail 定义) → D015(10K positive) → D017(碰撞转移) → D018(gradient correction 失效) → D019(negative 结果分层) → D020(30K TSR 退化 = safety-performance tradeoff)
- **论文目标**：CoRL 2026 Main / ICRA 2027，15 页初稿已完成
- **易错点**：
  1. 不要引用任何 Filtered CAR=0% 数据作为 "action collapse" 证据——这是 bug 产物，需重跑验证
  2. checkpoint 路径在两台服务器上不一致（`checkpoints/` vs `openpi/checkpoints/`），始终用 `find` 确认
  3. LoRA baseline 已 3 次 crash，完成后立即备份 checkpoint
  4. 多个 eval 实验有 v2/v3/v4 版本（makedirs bug 和 JSON 覆盖导致），metrics 以最新版本为准


---
