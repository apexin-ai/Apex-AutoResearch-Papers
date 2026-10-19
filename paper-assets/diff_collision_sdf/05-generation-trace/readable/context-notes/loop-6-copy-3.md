# reviewer / loop_6.md

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_6.md`
- **Structured JSON:** [`c742798dda629e0c842a.json`](../../sessions/c7/c742798dda629e0c842a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_wall_time
updated: '2026-05-26T12:32:02+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单（C001）：westd-35807:cuda:0-3 + westd-45947:cuda:0-1，共 6 张。越界即 CRITICAL。
- >24h 训练必须用 tmux 启动（C002），禁止 submit_training_job（24h timeout）。
- eval_safelibero.py 必须包含 180° 旋转修复（`[::-1, ::-1]`）+ camera 256×256。无修复的 eval 数据全部无效（D030）。
- `eval_lora_baseline_30k_s0_reeval` registry 条目缺 metrics 字段——引用该实验数据时必须从 JSON 文件交叉验证，不能只看 registry。
- Frozen rate 定义：必须用 **EE displacement < 0.1mm**（论文定义），不是 obstacle displacement。Worker 反复搞混这两个。所有模型 EE-based frozen rate = 0%。

### 2. 🖥️ 基础设施快照
- **westd-35807** (root): `/root/colliforce-vla`, conda base (`/root/miniconda3`)
  - GPU 0: PID 3717, spatial_bowl SDF s0, tmux=`train_pi05_a1_spatial_bowl_s0_l005`, step ~22K/30K
  - GPU 1: PID 271266, λ=0.1 s0, log=`/root/colliforce-vla/logs/train_lambda01_s0_gpu1.log`, step ~13.8K/30K
  - GPU 2: PID 274407, λ=0.1 s1, log=`/root/colliforce-vla/logs/train_lambda01_s1_gpu2.log`, step ~13.3K/30K
  - GPU 3: PID 341425, Plan 015 spatial_bowl LoRA control, tmux=`plan015`, log=`/root/runs/diff_collision_sdf/plan015_lora_baseline_spatial_bowl_s0.log`, 刚启动
- **westd-45947** (root): `/root/colliforce-vla`, conda base
  - GPU 0: LoRA seed2 训练, tmux=`train_pi05_lora_baseline_s2`, step ~11.1K/30K, log=`~/runs/diff_collision_sdf/train_pi05_lora_baseline_s2.log`
  - GPU 1: reeval batch2, tmux=`reeval_batch2`, 串行跑 4 个 eval（SDF l005 s1/s2, l01 s1/s2），log=`/root/reeval_batch2.log`
- Eval 结果输出：`/root/autodl-tmp/eval_results/reeval_*.json`
- Checkpoint 保留策略：SAVE_TOTAL_LIMIT=2，中间 checkpoint 已被清理

### 3. 📊 当前状态
我刚确认 Plan 015 在 westd-35807 cuda:3 成功启动（GPU 合规 ✅），并向 Director 报告了 GPU 3 空闲问题（已解决）。

**Registry RUNNING (4)**:
- `train_pi05_a1_spatial_bowl_s0_l005` — spatial_bowl SDF, 74%, ~10h
- `train_pi05_a1_obj_s0_l01_high` — λ=0.1 s0, 46%, ~21h
- `train_pi05_a1_obj_s1_l01_high` — λ=0.1 s1, 44%, ~21.5h
- `train_pi05_lora_baseline_s2` — LoRA seed2, 37%, ~24h
- (Plan 015 刚启动，可能还未注册或刚注册)

**等待中**:
- reeval batch2 (4 eval)：SDF l005 s1 正在跑 Task 0 Ep 10/50，预计全部完成 ~22:45 CST（约 2h）
- 无活跃 cron

### 4. 📋 待办（条件触发式）
- **reeval batch2 完成（4 个 JSON 出现）→** 交叉验证所有 7/7 reeval TSR/CAR/EE disp，计算 SDF vs LoRA-only 的 per-condition mean±std。关键判断：SDF l005 的 3-seed 均值是否显著高于 LoRA-only（当前 s0 单点 +4pp TSR，需 s1/s2 确认）。
- **reeval 7/7 全部到位 →** 执行 post-reeval Claim 3 系统性审查框架（已在前一轮提供给 Director），包括：(1) 新主表数据验证 (2) TSR drop 叙事更新（~20pp moderate, 非 catastrophic）(3) SDF attribution 最终判定 (4) per-task pattern 分析。
- **λ=0.1 训练完成 (~21-22h) →** 这是 Claim 3 最终叙事的决定性实验。eval 时必须确认用 rotation-fixed 脚本。如果 λ=0.1 CAR ≈ LoRA-only → Scenario A（SDF 全面 redundant）；如果 λ=0.1 CAR 显著 > LoRA-only → Scenario B（dose-dependent）。
- **spatial_bowl SDF s0 完成 (~10h) →** 等 Plan 015 也完成后做跨场景 SDF vs LoRA-only 对比。Plan 015 刚启动（~46h），所以 spatial_bowl 的 eval 对比要等较久。
- **LoRA seed2 完成 (~24h) →** 用 rotation-fixed 脚本 eval，获得 LoRA-only 3-seed 完整数据集。

### 5. 🎯 战略上下文
**核心决策链**: D025 (SDF=0pp at λ≤0.01) → D026 (三场景 contingency) → D029 (Phase2 无持久效应) → D030 (TSR collapse 是 eval bug) → **λ=0.1 结果**（决定最终叙事）

**已确立的结论（post-reeval）**:
- Claim 1 (Fake Safety): Pi0.5 base 0% fake safe，A1-LoRA 99.6% fake safe ✅
- Claim 4 (SDF Attribution): SDF λ≤0.01 CAR ≈ LoRA-only ±2.5pp → SDF 在低 λ 无 avoidance 贡献，CAR 来自 SafeLIBERO demo imitation ✅ (已存 memory)
- D030: "catastrophic TSR collapse" (74.7→<7%) 完全是 eval rotation bug 伪影。实际降幅 74.7→51.5% (~20pp) ✅

**最容易判断错的事**:
1. **不要混用 v1 (no-rotation) 和 v2 (rotation-fixed) eval 数据**。registry 中大量旧 eval（eval_*_v2, eval_*_v3 等命名）都是 buggy 的。只有 `reeval_*` 前缀和 `eval_phase2_lambda0_s2` 是可信数据。
2. **Frozen rate**: Worker 会报 obstacle-based 的 frozen rate（如 55.5%），这不是论文定义。论文用 EE-based，所有模型都是 0%。看到 >0% frozen rate 时先确认是哪种定义。
3. **λ=0.1 是最高优先级**。不要被 spatial_bowl 或 LoRA seed2 分散注意力——λ=0.1 决定论文最终走 Scenario A 还是 B。
4. **ROADMAP 中的 ETA 已过时**（写于 12:04 UTC）。实际进度：spatial_bowl ~74%（非 ROADMAP 中的 ~18h），λ=0.1 ~44-46%。
5. **displacement_metric_confusion memory** 和 **claim4_sdf_attribution_falsified memory** 是两个关键 memory 文件，包含反复出现的指标混淆问题和 SDF attribution 的核心否定证据。


---
