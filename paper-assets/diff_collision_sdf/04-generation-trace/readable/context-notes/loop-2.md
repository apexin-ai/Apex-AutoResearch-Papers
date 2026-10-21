# director / loop_2.md

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_2.md`
- **Structured JSON:** [`d8603f91c84c261ce95d.json`](../../sessions/d8/d8603f91c84c261ce95d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-22T18:33:54+00:00'
---

### 1. 🔴 硬约束 / 红线
- eval_safelibero.py 必须用 `--gpu N` 指定物理 GPU，禁止仅依赖 CUDA_VISIBLE_DEVICES（M013/M023 两次复现）
- train_a1_sdf_aux.py 内部覆盖 CUDA_VISIBLE_DEVICES，必须用 `--gpu N` 直接指定（M013）
- WANDB_MODE=disabled/offline 时 cron 会误判训练完成为 failed，收到 cron failed 回调先 tail log 检查实际状态（M016）
- westd-35807 autodl-tmp 磁盘保持 < 70%（当前 ~32%）
- A3 eval 所有结果（v10/v11/oracle_pre-M024fix）均无效——M024 坐标 bug 导致 refinement 从未正确执行
- A1 object eval 只有 12 episodes 有效数据（M025 文件覆盖），需要 rerun 的干净数据

### 2. 🖥️ 基础设施快照
- **westd-35807**: connect.westd.seetacloud.com, root, conda env `libero`, 4× RTX PRO 6000 98GB
  - 代码: `/root/colliforce-vla/`
  - Checkpoints: `/root/autodl-tmp/checkpoints/`
  - Eval 结果: `/root/autodl-tmp/eval_results/`
  - 磁盘: ~570GB 可用 (32%)
- **westd-45947**: connect.westd.seetacloud.com, root, conda env `base`, 2× RTX PRO 6000 98GB
  - 代码: `/root/colliforce-vla/`
  - 磁盘: ~128GB 可用 (40%)
- **活跃进程 (westd-35807)**:
  - cuda:0: eval_a1_lora_spatial_v11 (PID 727358, tmux eval_a1_spatial) — 决定性实验
  - cuda:1: eval_baseline_fullft_spatial_v11 (PID 697980, tmux eval_baseline_spatial)
  - cuda:2: eval_a3_object_m024fix_v11 (PID 780772, tmux eval_a3_m024fix) — 首次正确 A3 eval
  - cuda:3: oracle_a3_m024fix_object_v11 (PID 859190, tmux oracle_m024fix) — 正确坐标 oracle
- **活跃进程 (westd-45947)**:
  - cuda:0: a3_gradient_spatial_bowl_s0 (tmux train_a3_spatial) — 训练 ~92%, ETA ~2.5h
  - cuda:1: 空闲，pi0.5 下载进程丢失需重启

### 3. 📊 当前状态
刚完成 M024 修复（eval_safelibero.py `_refine_action_a3()` 坐标 bug：delta→absolute）并部署到两台服务器。A3 M024fix eval + oracle 已在 westd-35807 启动。等待 5 个实验结果：

| 实验 | GPU | 意义 | 预计完成 |
|------|-----|------|---------|
| eval_a3_object_m024fix_v11 | 35807:cuda:2 | 首次正确 A3 eval，Task 0 中间结果 CAR=88.5%, refined=0, SDF 0.18-0.77 | ~1-2h |
| oracle_a3_m024fix_object_v11 | 35807:cuda:3 | 正确坐标下 gradient 方向验证 | <1h |
| eval_a1_lora_spatial_v11 | 35807:cuda:0 | 决定性实验，Task 0 早期 CAR=1.5% (弱) | ~8h |
| eval_baseline_fullft_spatial_v11 | 35807:cuda:1 | baseline 对照，Task 0-1 CAR=0% | ~6h |
| a3_gradient_spatial_bowl_s0 | 45947:cuda:0 | A3 spatial 训练 | ~2.5h |

pi0.5 官方 eval 下载反复失败/消失，需要重启。用户明确要求过官方验证。

### 4. 📋 待办（条件触发式）
- oracle_a3_m024fix 完成 → 看 CAR 和 gradient magnitude。CAR 显著 > 88.5% → SDF gradient 有用，调 refine_margin；CAR 无变化 → SDF gradient 方向可能有问题
- eval_a3_object_m024fix 完成 → 如果 refined_count > 0 且 CAR > baseline(83%) → A3 方向验证成功；如果 refined=0 → 需要调 refine_margin 重跑
- a3_spatial 训练完成 → 用 M024 修复版 eval 代码在 westd-45947 跑 A3 spatial eval（含 --force_refine），spatial baseline CAR=0% 是最佳验证场景
- eval_a1_spatial 完成 → 如果 CAR 显著 > 0% → A1 方向在 spatial 有效，论文核心 claim 成立；如果 CAR ≈ 0% → A1 spatial 无效，focus 回 object_pudding
- pi0.5 libero checkpoint 下载完成 → 立即启动官方 eval (serve_policy.py + examples/libero/main.py)，验证 eval 环境
- 碰撞部位诊断结果 → 如果碰撞主要在 arm body（非 EE）→ EE-only SDF refinement 天然无法解决 spatial 碰撞，scope 调整到 EE-dominant 场景
- a1_lora cron failed 回调 → M016 误报，tail log 确认后更新 registry 为 success

### 5. 🎯 战略上下文
**核心发现链**：M019(state格式) → M020(action chunking) → M022(A3 norm_stats) → M024(delta当absolute坐标) = eval pipeline 连续 4 个 bug，A3 runtime refinement 从未被正确测试。

**两条方向并行验证中**：
- **A1 (SDF auxiliary loss, 训练时)**: object_pudding CAR=90% vs baseline 82% (+8pp)，但 Reviewer 质疑"假安全"（位移从 13mm 降到 3mm）。spatial_bowl 是决定性验证。
- **A3 (SDF gradient refinement, 推理时)**: M024 修复后正在首次正确测试。M024fix Task 0 中间数据：CAR=88.5%, refined=0, SDF 0.18-0.77。refinement 仍未自然触发（SDF >> margin），但 oracle force_refine 正在测试 gradient 方向。

**MVP gate**: baseline CAR=83% (object) / 0% (spatial), TSR=0.5%/0%。原始 gate +15pp CAR 改善尚未达到。

**最容易判断错的事**：
1. 不要把之前的 A3 eval 结果（v10/v11/pre-M024 oracle）当作有效数据——全部被 M024 坐标 bug 污染
2. A1 object CAR=90% 可能是假安全（所有 LoRA 模型位移都极低），spatial 结果才能定论
3. spatial_bowl CAR=0% 可能是 arm-body 碰撞而非 EE 碰撞——碰撞部位诊断还没做
4. pi0.5 下载已经丢失过多次，重启时用 nohup + 日志 + PID 记录


---
