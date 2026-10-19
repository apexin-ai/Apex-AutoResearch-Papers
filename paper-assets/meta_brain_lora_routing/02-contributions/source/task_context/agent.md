---
loop: 3
reason: idle_timeout
updated: '2026-05-16T20:41:46+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：`cuda:0, cuda:1, cuda:2, cuda:3` @ westd-34142，**不可用其他 GPU**
- **废弃 checkpoint**：`/root/autodl-tmp/checkpoints/pi0_libero/`（lerobot base model）和 `/root/autodl-tmp/checkpoints/pi0_libero_finetuned/`（lm_head zeroed）**绝对不能用**。所有 v2 实验因此作废
- 正确 base checkpoint **唯一来源**：`/root/autodl-tmp/checkpoints/pi0_libero_openpi/`（JAX→PT 转换，777 keys，bit-exact 验证通过）
- 老 phase1 checkpoint 目录 `/root/meta_brain_lora_routing/checkpoints/` 下的 LoRA 是基于错误 base 训练的，**不可用于 eval**。v3 checkpoint 在 `/root/autodl-tmp/checkpoints/v3_lora_*/`
- 根分区只有 ~30GB，大文件必须写 `/root/autodl-tmp/`
- jaxtyping 兼容性问题已通过 `jaxtyping_disable = True` 修复（eval_base_no_lora.py, evaluate_libero_plus.py, openpi_metabrain_policy.py），**不要升级 jaxtyping/beartype**

### 2. 🖥️ 基础设施快照
- **服务器**：westd-34142，4× RTX PRO 6000 96GB
- **工作目录**：`/root/meta_brain_lora_routing`
- **Python**：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`（conda 环境，非 venv）
- **正确 base model**：`/root/autodl-tmp/checkpoints/pi0_libero_openpi/`（safetensors 7GB）
- **训练数据**：`/root/autodl-tmp/libero_demos/libero_object_image/`（66984 samples）
- **LIBERO-Plus 环境**：`/root/LIBERO-plus/`（包含原版 suites：libero_spatial/object/goal/10/90）
- **v3 checkpoints**（正确 base 训练）：
  - `/root/autodl-tmp/checkpoints/v3_lora_visual_r16/v3lora_visual_r16/final`
  - `/root/autodl-tmp/checkpoints/v3_lora_spatial_r16/v3lora_spatial_r16/final`
  - `/root/autodl-tmp/checkpoints/v3_lora_physical_r16/v3lora_physical_r16/final`
  - `/root/autodl-tmp/checkpoints/v3_lora_universal_r16/v3lora_universal_r16/final`
  - v3_lora_universal_r48：训练中，输出到 `/root/autodl-tmp/checkpoints/v3_lora_universal_r48/`
- **PAR Router**（旧 base 训练）：`/root/meta_brain_lora_routing/checkpoints/phase1/par_router/best_router.pt`——**需要用 v3 checkpoint 的 activations 重训**
- **活跃进程**：v3_lora_universal_r48 PID=118481, tmux session, cuda:1, cron 监控中
- **W&B**：当前 v3 训练全部 `--no_wandb`

### 3. 📊 当前状态
**刚完成**：v3 LoRA r16 四路训练（visual/spatial/physical/universal），全部 success。Final loss ~0.59-0.61（OOD 扰动数据），训练时间 ~170min/each。Physical init_loss 最高（2.37 vs 1.95），说明 physical perturbation 对 base model 偏离最大。

**正在跑**：`v3_lora_universal_r48`（RUNNING, pid=118481, cuda:1）——rank-48 parameter-matched universal LoRA，作为 Claim 3（参数效率）的 control。预计 ~3h 完成（提交于 20:30 UTC）。

**Registry 杂项**：
- 3 个 ALLOCATED 实验（phase1_physical_demo_collection, phase1_spatial_demo_collection, phase1_lora_spatial）是旧方案残留，已无意义，可清理
- phase_b5_activation_collection（PREPARING）、eval_no_routing（PREPARING）是旧计划残留

**等待中**：
- v3_lora_universal_r48 的 cron 完成回调
- 无 Worker 在运行
- 无待处理 Director 决策

### 4. 📋 待办（条件触发式）
- **v3_lora_universal_r48 cron 回调到达** → 记录 metrics → 比较 r48 vs r16 final_loss（预期 r48 更低，验证 rank 与 capacity 关系）→ 更新 registry + report.md → 汇报 Director
- **v3 全部完成后（含 r48）** → 关键路径是 **eval pipeline 端到端验证**：
  1. 先跑 nominal eval（无扰动，用 v3 base checkpoint 在原版 LIBERO tasks 上验证 >80%）
  2. 用 v3 checkpoint activations 重训 PAR Router（旧 router 基于错误 base 的 activations）
  3. 完整 eval matrix：PAR routing（3 expert） vs universal r16 vs universal r48 vs frozen baseline，在 LIBERO-Plus 各扰动类型上
- **Eval 0% 风险** → jaxtyping fix 已做但 **eval pipeline 从未在 v3 checkpoint 上端到端跑通过**。第一步是 dry-run 单 episode 验证不报错
- **PAR Router 重训** → 需新 activation collection（用正确 base + v3 LoRA）→ 训 router → 才能跑 PAR routing eval
- **CoRL DDL 2026-05-29**（13 天）→ eval + router retrain + paper writing 全部要在此前完成

### 5. 🎯 战略上下文
**项目核心**：Perturbation-Adaptive LoRA Routing (PAR)——冻结 π₀ VLA 的内部激活可诊断扰动类型（Phase 0 已验证 F1=1.0），路由到专用 LoRA expert 做针对性修正。

**决策链**：D002(Reviewer 建议)→D003(层索引修正)→D004(Phase 0 GO)→D005(进入 Research)→D006(first-token pooling)→D007(Dream 审稿 reject，加 r48 control)→D008(数据策略转向)→D009(compound perturbation)→D010(⚠️ checkpoint 大翻车：lerobot/pi0_libero 是 base model)→D011(v3 训练确认有效)

**最容易判断错的事**：
1. **老 checkpoint 目录里的东西看起来都能用但全是错的**。`/root/meta_brain_lora_routing/checkpoints/` 下的 phase1 era LoRA 和 PAR Router 都基于错误 base，形式上完整但实质无效。只用 `/root/autodl-tmp/checkpoints/v3_*` 的 checkpoint
2. **PAR Router 需要重训**。当前 `best_router.pt` 是基于旧 base activations 训练的，虽然 F1=1.0 但 activation 分布已变（v3 用不同 base）。不能直接拿来 eval
3. **Eval pipeline 从未成功跑出过有效数据**。之前所有 eval 实验要么因为错误 base（0% 成功率）被 kill，要么因为 jaxtyping bug 失败。v3 eval 是**首次尝试**，要做好排查准备
4. **LIBERO-Plus `_add_N` = spatial（distractor objects），不是 physical**。`_table_N`/`_tb_N` = visual，`_language_N` = 可能不需要 LoRA。这个映射决定 eval 时哪个 expert 对应哪个 task variant
5. **Nominal baseline 只有 60%（10 eps）**，官方 ~80%，高方差区间内一致但不确定。eval 时需要更多 episodes（≥50）来降低方差
