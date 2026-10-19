# agent / loop_4.md

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_4.md`
- **Structured JSON:** [`5fcc638c5065f15d4f06.json`](../../sessions/5f/5fcc638c5065f15d4f06.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: idle_timeout
updated: '2026-05-27T09:49:31+00:00'
---

### 1. 🔴 硬约束 / 红线
- **westd-45947 只有 cuda:0, cuda:1**；**westd-35807 只有 cuda:0-3**——gpu_ids 白名单外的 GPU 绝对不碰
- LoRA baseline 实验用 `WANDB_MODE=offline`，不要试图从 W&B cloud 拉指标，必须 SSH 读日志/checkpoint
- Checkpoint 路径固定在 `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/` 下，不要写到根分区
- Phase 2 实验的 resume checkpoint 来自 SDF 训练的 best checkpoint（非 LoRA baseline），不要搞混
- LoRA baseline checkpoint 在 `pi05_lora_baseline_object_pudding_seed*/` 下，SDF checkpoint 在不同目录，eval 时不要搞混

### 2. 🖥️ 基础设施快照
- **westd-35807**: 工作目录 `/root/colliforce-vla`，conda env `libero`（不是 base），4× RTX PRO 6000 Blackwell 96GB
  - cuda:0 → `train_pi05_a1_spatial_bowl_s0_l005` (PID 3708, cron 活跃)
  - cuda:1 → `train_pi05_a1_obj_s0_l01_high` (PID 271266, log: `/root/colliforce-vla/logs/train_lambda01_s0_gpu1.log`)
  - cuda:2 → `train_pi05_a1_obj_s1_l01_high` (PID 274407, log: `/root/colliforce-vla/logs/train_lambda01_s1_gpu2.log`)
  - cuda:3 → `train_spatial_bowl_lora_control_s0` (PID 341425, cron 活跃)
  - wandb 未配置，训练命令需 `export WANDB_MODE=disabled`；eval 命令必须加 `--suite safelibero_object`
- **westd-45947**: 工作目录 `/root/colliforce-vla`，conda env `base`（`/root/miniconda3/bin/python`），2× RTX PRO 6000 96GB
  - cuda:0 → `train_pi05_lora_baseline_s2` (PID 78558, cron 活跃)
  - cuda:1 → `train_pi05_a1_obj_s2_l01_high` (PID 425058, cron 活跃)
  - LoRA baseline s0/s1 checkpoints: `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/pi05_lora_baseline_object_pudding_seed{0,1}/`
- 数据集: `safelibero_object_pudding` (200 episodes), `safelibero_spatial_bowl`
- HF cache: `/root/autodl-tmp/.hf_cache`
- threshold_sensitivity 分析产出: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/threshold_sensitivity/`

### 3. 📊 当前状态
Loop #4 刚完成 session-start 初始化 + 向 Director 汇报。所有 6 GPU 满载，6 cron 全部正常，0 活跃 Worker。

**RUNNING (6)**:
- `train_pi05_a1_spatial_bowl_s0_l005` — 跨场景 SDF (westd-35807:cuda:0, ~06:30 5/27)
- `train_pi05_a1_obj_s0_l01_high` — λ=0.1 seed0 (westd-35807:cuda:1, ~17:05 5/27)
- `train_pi05_a1_obj_s1_l01_high` — λ=0.1 seed1 (westd-35807:cuda:2, ~17:50 5/27)
- `train_spatial_bowl_lora_control_s0` — 跨场景 LoRA ctrl (westd-35807:cuda:3, ~06:10 5/28)
- `train_pi05_lora_baseline_s2` — LoRA s2 (westd-45947:cuda:0, ~20:20 5/27)
- `train_pi05_a1_obj_s2_l01_high` — λ=0.1 seed2 (westd-45947:cuda:1, ~5/28)

**PREPARING (2)**: `reeval_lora_s0_30k_v2`, `eval_pi05_a1_best_s0_l005` — 等 GPU 空闲

**论文**: method/claim1/claim2/related_work/intro/discussion/abstract 全部完成 + Reviewer 审查通过。claim3 阻塞于 λ=0.1 A/B/C 判定。

### 4. 📋 待办（条件触发式）
- **spatial_bowl SDF 完成 (~06:30 5/27)** → 立即在同 GPU 启动 plan_008 eval；westd-35807:cuda:0 释放后可跑 reeval_lora_s0_30k_v2 或 eval_pi05_a1_best_s0_l005
- **λ=0.1 s0/s1 完成 (~17:05-17:50 5/27)** → **最高优先级**：立即 eval (plan_010)，A/B/C 场景判定（D033 阈值：≤57% B全域negative / 57-60% C灰区 / 60-65% A- / >65% A+），硬约束 TSR<35%/frozen>0% → CAR 无效
- **LoRA s2 完成 (~20:20 5/27)** → eval 获取第 3 seed CAR，完成 3v3 统计对比
- **λ=0.1 eval 全部完成** → 确定场景 → 立即写 claim3.tex + 更新 Fig 5 + 论文定稿
- **spatial_bowl LoRA ctrl 完成 (~06:10 5/28)** → eval + 与 spatial_bowl SDF 对比，完成跨场景归因

### 5. 🎯 战略上下文
- **核心决策链**: D018→D019→D020-D023→D024(Dream)→D025-D033 → 等 λ=0.1 判定
- **D033 定义了 A/B/C 场景量化阈值**：λ=0.1 3-seed CAR 均值决定论文最终 framing（analysis paper vs dose-response story vs 强正向叙事）
- **D032**: 低 λ (0.005) SDF 完全 redundant，3-seed CAR=54.5% = LoRA-only CAR=54.5%
- **D030**: "catastrophic TSR collapse" 是 eval rotation bug 伪影，已修正
- **已有可信数据**: Pi0.5 base CAR=28.5% | LoRA-only CAR=54.5%±2.83 | SDF λ=0.005 CAR=54.5%±2.29 | SDF λ=0.01 CAR=56.33%±1.61 (p≈0.12, 噪声) | Phase 2 λ=0 CAR=57.5% (single seed)
- **plan_014 (threshold sensitivity) 已完成**：所有 1200 SDF episodes 的 max EE disp > 239mm，δ∈[2mm,200mm] dfCAR 完全不变——这对论文是好消息（SDF 模型确实运动，阈值鲁棒）
- **易错点**: (1) eval 脚本必须用 rotation-fixed 版本 + `--seed 7` (2) westd-35807 用 conda env `libero` 不是 `base` (3) λ=0.1 eval 检查清单已在 ROADMAP 中定义，严格执行 (4) 不要把 Phase 2 checkpoint 和 LoRA baseline checkpoint 搞混


---
