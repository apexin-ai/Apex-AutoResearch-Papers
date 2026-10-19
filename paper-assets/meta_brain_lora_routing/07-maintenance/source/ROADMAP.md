# meta_brain_lora_routing — Research Dashboard

> 最后更新: 2026-05-17 01:41 UTC | 更新原因: Reviewer验证完成，pivot确认，启动rank sweep，更新全面状态

> CoRL 2026 — Paper DDL: 2026-05-29 (12天)

## 核心方向
**Universal LoRA Robustness for VLA Deployment**：单一 rank-16 universal LoRA adapter (3.7M params) 是 VLA 部署鲁棒性的最优方案。Rank scaling 过拟合，专家化导致灾难性遗忘。详见 `paper_framing.md`。

## 当前进展
- 阶段：**Post-Pivot Research**（routing falsified → universal LoRA story）
- Phase 0 ✅ PAR Router F1=1.0（虽routing无价值，但证明VLA内部编码环境信息）
- Phase 1 训练 ✅ 4路 LoRA 全部训完（visual/spatial/physical/universal r16 + universal r48）
- Eval 完成 ✅ 7类扰动 × 6方法 对比表完整（仅 r48 sensor_noise 待补）
- Reviewer 独立验证 ✅ 所有关键数据点核实通过（D018）
- **Rank sweep 进行中**：r8/r32 训练已派（4 GPU 并行）

## 关键结论（Reviewer 验证）
| 方法 | 结论 |
|------|------|
| Universal r16 | **唯一正向干预** 6/7类优于baseline，+15pp lighting |
| Universal r48 | 过拟合，全类 ≤ baseline |
| Visual expert | 目标领域 -10pp vs universal |
| Spatial expert | 目标领域 -5.8pp vs universal |
| Physical expert | 仅 robot_initial_states +3.8pp，nominal -1.7pp |

## 近期任务
- [ ] Universal LoRA r8 训练 + 7类 eval（cuda:0）
- [ ] Universal LoRA r32 训练 + 7类 eval（cuda:1）
- [ ] r48 early stopping 消融（step 1k/2k/3k/5k eval）（cuda:2）
- [ ] 确认 r16 eval 为 3-seed，补 sensor_noise r48（cuda:3）
- [ ] 澄清 physical expert 两组数据来源
- [ ] 启动论文写作（Paper Agent，与实验并行）
- [ ] 等用户确认是否冲 CoRL

## 已放弃计划
plan_003(routing assembly)、004(oracle routing)、005(routing ablation ladder)、008(correction memory)、009/010(router variants)、011(cross-backbone)、016(compound perturbation)

## GPU 预算
- 服务器：4× RTX PRO 6000 96GB @ westd-34142
- 当前：4 卡全满（r8 训练 / r32 训练 / r48 early stop eval / 数据确认+补eval）
- 预计 r8/r32 训练 ~2-3h → eval ~2h → 全部完成 ~5h

## Checkpoints
- **r16**: `/root/meta_brain_lora_routing/checkpoints/lora_universal_r16/final`
- **r48**: `/root/autodl-tmp/checkpoints/v3_lora_universal_r48/v3_r48lora_universal_r48/final`
- **r8 (训练中)**: `/root/autodl-tmp/checkpoints/v3_lora_universal_r8/`
- **r32 (训练中)**: `/root/autodl-tmp/checkpoints/v3_lora_universal_r32/`

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D018 | 2026-05-17 | Reviewer 独立验证确认 pivot。启动 rank sweep (r8/r32) + ear | phase1_lora_universal_r16, v3_lora_universal_r48, phase1_lora_visual, phase1_lora_physical |
| D017 | 2026-05-17 | Routing 核心 claim 放弃。Pivot to universal LoRA robust | worker_code_par_router_real_env_v4, worker_eval_visual_expert_oracle, worker_eval_physical_expert_oracle, worker_eval_baseline_3seed_v2 |
| D016 | 2026-05-17 | Paper framing 从 "Perturbation-Aware Routing" 调整为 " | worker_code_par_router_train_v3, phase0_activation_collection, worker_eval_baseline_3seed_v2 |
| D015 | 2026-05-16 | Router 训练改用真实 LIBERO-Plus 环境观测（非合成增强），因 PaliGemma  | worker_code_par_router_train_v3, phase0_activation_collection |
| D014 | 2026-05-16 | 真实 nominal baseline 52%（非 70%），采用 3-seed×20eps 确定性 | worker_debug_p0_noise_fix, worker_eval_baseline_full_coverage |
| D013 | 2026-05-16 | +40pp 发现无效（eval bug），暂停 claim-level 结论，优先修复 eval 可 | eval_perturbation_degradation, eval_lora_v3_universal |
| D012 | 2026-05-16 | Language perturbation -56pp 发现：验证 universal LoRA 恢 | eval_perturbation_language |
| D011 | 2026-05-16 | v3 LoRA 训练确认有效：step-0 loss=2.0 是 OOD 预期行为，权重 bit-e | v3_lora_visual_r16, v3_lora_physical_r16 |
| D010 | 2026-05-16 | 换 base checkpoint: pi0_base → pi05_libero，重训所有 LoR | eval_par_v1, eval_univ_r16, eval_univ_r48, eval_no_routing |
| D009 | 2026-05-16 | 加入 compound perturbation 实验 (plan_016) + 强化方法包装定位 | plan_016 |


