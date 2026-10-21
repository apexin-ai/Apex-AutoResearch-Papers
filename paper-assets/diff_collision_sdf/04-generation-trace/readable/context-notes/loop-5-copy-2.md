# agent / loop_5.md

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_5.md`
- **Structured JSON:** [`63ebf36dc7780c46b929.json`](../../sessions/63/63ebf36dc7780c46b929.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: idle_timeout
updated: '2026-05-28T06:18:59+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单: westd-35807 cuda:0/1/2/3, westd-45947 cuda:0/1（共 6 张）
- submit_training_job 命令必须自带 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate libero`，不能假设 .venv
- GPU 编号脚本内始终从 0 开始（框架自动 CUDA_VISIBLE_DEVICES 映射）
- 模型/数据/checkpoint 必须放 `/root/autodl-tmp/`，根分区只有 ~30GB
- DDL 是 **2026-05-28 12:00 UTC**（北京 20:00），今天就是截止日

### 2. 🖥️ 基础设施快照
- **westd-35807**: 工作目录 `/root/colliforce-vla`，Python `/root/miniconda3/envs/libero/bin/python`，conda env `libero`
- **westd-45947**: 同上结构
- Checkpoint 路径: `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/`
- 磁盘: westd-35807 根盘 570G/879G 可用; westd-45947 根盘 400G/439G 可用
- 活跃进程:
  - train_spatial_bowl_lora_control_s0: PID 341425, westd-35807 cuda:3, cron 活跃
  - train_pi05_a1_obj_s2_l01_high: PID 425058, westd-45947 cuda:1, cron 活跃（λ=0.1 s2 训练，预计 ~01:00 UTC 5/28 完成）
  - eval_lora_s2_30k_v2: PID 519125, westd-45947 cuda:0（LoRA s2 30K eval）
  - train_phase2_lambda0_s2_v3: PID 849401, westd-35807 cuda:2（Phase 2 λ=0 s2 extended）
- 空闲 GPU: westd-35807 cuda:0, cuda:1

### 3. 📊 当前状态
刚收到 `train_phase2_lambda0_extra_seed` 失败回调（EXIT_CODE=1, 仅跑 74.5 秒——启动阶段崩溃）。已派 Worker `worker_diagnose_train_phase2_lambda0_extra_seed_20260527T141518` 去 westd-35807 读日志诊断，**尚未收到 Worker 回调**。

**RUNNING 实验:**
| exp_id | 服务器/GPU | 摘要 |
|--------|-----------|------|
| train_pi05_a1_obj_s2_l01_high | westd-45947 cuda:1 | λ=0.1 s2 训练，3-seed 最终一块拼图 |
| eval_lora_s2_30k_v2 | westd-45947 cuda:0 | LoRA s2 30K eval，完成 null distribution |
| train_phase2_lambda0_s2_v3 | westd-35807 cuda:2 | Phase 2 λ=0 s2 extended training |
| train_spatial_bowl_lora_control_s0 | westd-35807 cuda:3 | spatial_bowl LoRA control baseline |

**PREPARING:** eval_pi05_a1_best_s0_l005（Pi0.5+A1 best checkpoint eval）

**等待中:**
- Worker 诊断回调（train_phase2_lambda0_extra_seed 失败原因）
- eval_lora_s2_30k_v2 完成回调 → 补全 LoRA 3-seed null distribution
- train_pi05_a1_obj_s2_l01_high 完成回调 → λ=0.1 s2 eval → 3-seed 最终判定

### 4. 📋 待办（条件触发式）
- 诊断 Worker 回调到 → 根据失败原因决定是否重试 train_phase2_lambda0_extra_seed（cuda:1 空闲可用）
- eval_lora_s2_30k_v2 完成 → 提取 CAR，更新 null distribution（已有 s0=57%, s1=52.5%），更新 registry + report
- train_pi05_a1_obj_s2_l01_high 完成 → 立即在 westd-35807 cuda:0 或 cuda:1 提交 λ=0.1 s2 30K eval → 结果出来后做 3-seed 统计判定
- 3-seed λ=0.1 结果出齐 → 若 mean≥56% 且 z≥1.65 → Scenario C 确认，更新论文数字 + Fig 5；否则降级 narrative
- Reviewer 审查修正（s1 per-task 数字 + LoRA Table 行 + EE Disp + std 一致性）仍 pending
- Fig 5 需重新生成（加 λ=0.1 30K 数据点）
- 最终: s2 结果 → 二次 patch → 编译 → 提交（DDL 12:00 UTC）

### 5. 🎯 战略上下文
- **核心结论链**: D032 低 λ(0.005) SDF 完全冗余 → D033 λ=0.1 可能有效 → D038 Scenario C 初步确认（2-seed mean=58.25%, z=2.27, p≈0.023）
- **Null distribution**: LoRA-only mean=54.6%, σ=2.27%（基于 s0=57% reeval, s1=52.5%；s2 待出）
- **Phase 2 (SDF→λ=0)**: D029 已确认无持久效应，Phase 2 ≈ LoRA-only。train_phase2_lambda0_extra_seed 是补充 seed 验证，优先级低于 λ=0.1 s2
- **易错点**: 
  - 不要混淆 rotation-fixed (D033 后) 和 rotation-broken (D033 前) 的 eval 数据——只用 D033 后的可信数据
  - LoRA s0 的可信值是 reeval_v2 的 57%，不是旧的 54.5%
  - train_phase2_lambda0_s2_v2 已失败（lerobot 版本不匹配），v3 正在跑修复版本，不要再重复 v2 的错误
  - 时间极紧（DDL 今天），λ=0.1 s2 是关键路径——所有 GPU 调度优先保障这条线


---
