# agent / loop_2.md

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_2.md`
- **Structured JSON:** [`3ef995ec5a88f5013773.json`](../../sessions/3e/3ef995ec5a88f5013773.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-16T01:09:05+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0/1/2/3（westd-34142），不可用其他设备
- submit_training_job 命令必须 `bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && ..."`（tmux 用 sh 不是 bash）
- sensor_noise 原始 episode-level .pt 已丢失（被 per_step worker 覆盖），不可假设存在
- Spatial 数据采集必须用 `_add_N`（干扰物体），**不能**用 `perturb_region_info()`（位置扰动）——train/eval 必须同分布（Director 紧急修正过一次）
- `phase1/` 是规范代码路径，`artifacts/phase1/` 是旧版残留
- light_conditions 数据是合成生成的，分析结论需标注 bias discount

### 2. 🖥️ 基础设施快照
- 服务器：westd-34142，工作目录 `/root/meta_brain_lora_routing`
- Python：conda base（`/root/miniconda3/bin/python`），PyTorch 2.8.0+cu128，CUDA 12.8
- 4× RTX PRO 6000 Blackwell 94GB，tmux 3.2a 已安装
- pi0 模型：`/root/autodl-tmp/checkpoints/pi0_base`（14GB）
- LIBERO-Plus：`/root/LIBERO-plus/`，`new_objects/` 已下载就位（6.3GB，208 个 `_add_N` 任务可用）
- Phase 1 代码：`/root/meta_brain_lora_routing/phase1/`（train_lora_expert.py, collect_expert_demos.py, par_router.py, meta_brain_assembly.py, evaluate_libero_plus.py, ablation_ladder.py, visual_augmentation.py, data_loader.py）
- 活跃进程：
  - cuda:0: LoRA-V 训练 PID 216556, tmux=phase1_lora_visual
  - cuda:1: Spatial demo 收集 PID 246213, tmux=phase1_spatial_demo_collection（`_add_N` 模式, 624 rollouts）
  - cuda:2: Physical demo 收集 PID 228345, tmux=phase1_physical_demo_collection（490 rollouts）
  - cuda:3: Universal r16 训练 PID 216633, tmux=phase1_lora_universal_r16（visual-only bootstrap）
- sensor_noise per-step 收集可能仍在 cuda:0 后台跑（PID 182966），需检查是否与 LoRA-V 冲突

### 3. 📊 当前状态
Phase 0 已标记 DONE(success)。4/4 GPU 全占满运行 Phase 1 任务。

**Registry：**
- `phase0_activation_collection`: DONE(success) — 3-class F1=0.993, K=1 F1=0.978, PAR Router F1=0.9963
- `phase1_lora_visual`: RUNNING — LoRA-V 训练（在线视觉增强）
- `phase1_lora_universal_r16`: RUNNING — Universal rank-16（visual-only bootstrap，后续需用全量数据重训）
- `phase1_physical_demo_collection`: RUNNING — Physical expert demo 收集（π₀ rollout + success filter）
- `phase1_spatial_demo_collection`: RUNNING — Spatial expert demo 收集（`_add_N` 模式）

**等待：** 4 个 cron 回调（上述 4 个任务完成时）

### 4. 📋 待办
- Physical demo 收集完成 → 确认成功 demo 数 ≥150 → 在 cuda:2 启动 LoRA-P 训练（`--perturbation_type physical`）
- Spatial demo 收集完成 → 确认成功 demo 数 ≥150 → 在 cuda:1 启动 LoRA-S 训练（`--perturbation_type spatial`）
- Universal r16 训练完成 → 在 cuda:3 启动 rank-48 universal（plan_013，命令：`--perturbation_type visual --lora_rank 48`）→ **先修 `--lora_alpha` 动态默认值**（当前硬编码 32，rank-48 需 alpha=96）
- LoRA-V 训练完成 → 记录 metrics → cuda:0 可接后续任务
- 所有 LoRA expert 训练完成 → 用 `meta_brain_assembly.py` 组装 Router + 3 LoRA → 跑 `ablation_ladder.py` 5 配置对比
- sensor_noise per-step 收集完成 → 补完 7-class sweep + 更新 PAR Router（加入 sensor_noise 到 Visual 类）

### 5. 🎯 战略上下文
- **目标**：CoRL 2026（Abstract DDL 2026-05-26，Paper DDL 2026-05-29，剩 ~13 天）
- **决策链**：D001(MVP定义) → D002(Reviewer增强) → D003(层索引修正) → D004(Phase 0 GO) → D005(进入Research) → D006(first-token pooling) → D007(Phase 1 批准)
- **Core Claims**：(1) Perturbation Diagnosability ✅已验证 (2) Targeted > Uniform Correction 待验证 (3) Parameter-Efficient Robustness 待验证
- **LoRA 参数**：3.7M trainable (0.11%)，72 modules（18 PaliGemma layers × Q/K/V/O），target regex: `paligemma_with_expert\.paligemma\.model\.language_model\.layers\.\d+\.self_attn\.(q|k|v|o)_proj`
- **易错点 1**：Universal r16 当前用 visual-only 数据训练——这只是 bootstrap，不是最终版。全量 Universal 需等 S/P demo 就绪后重训
- **易错点 2**：`--lora_alpha` 硬编码 32，rank-48 需要改为动态 `rank*2`。Worker 发现了问题但没改（问了"要修吗"然后结束了），**必须在 rank-48 启动前修好**
- **易错点 3**：`collect_expert_demos.py` 存在本地+远程双版本（`artifacts/phase1/` 和 `phase1/`），规范路径是远程 `phase1/`
- **Dream 模拟已完成**，framing/plan 已修复（加了 rank-48 control, rank sweep, clean eval），plan_013 = rank-48 universal 是 Dream 审稿标记的 #1 existential control


---
