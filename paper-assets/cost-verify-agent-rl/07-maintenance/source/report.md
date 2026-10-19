# Handover — 2026-05-25

> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。

## 运行中
（无）

## 待处理
- exp029_seed200_step5_ood_eval: seed200 episode-level GRPO step5 OOD eval. seed200 训练完成后的 OOD 泛化能力评估. 与其他 healthy seeds (seed100 step5=11.19%, seed300 step5=10.45%) 和 collapsed seeds 对比, 确定 seed200 分类并补充 Table 1 数据.（排队等待 GPU）
- cell_b_1gpu_seed300: R6-N2: Cell B 多种子验证 OOD 5.97% 可靠性，plan_id 关联 factorial design claim。Cell B (h=2, episode-level advantage, M1 only) 在不同 seed 下应保持 OOD 性能近 SFT baseline（~5-7%），验证 M1 alone bounds but does not collapse。（准备中）
- cell_b_1gpu_seed200: R6-N2: Cell B 多种子验证 OOD 5.97% 可靠性，plan_id 关联 factorial design claim。Cell B (h=2, episode-level advantage, M1 only) 在不同 seed 下应保持 OOD 性能近 SFT baseline（~5-7%），验证 M1 alone bounds but does not collapse。（准备中）
- ood_eval_sft_baseline_v3（准备中）
- exp029_seed7_high_kl_step7_ood_v3: D134 协议 re-eval (retry): high_kl step7 checkpoint OOD eval. v2 因 GPU OOM crash. 现在 GPU 3 完全空闲, 重新提交. 原始 eval 得 12.69% (17/134).（准备中）
- exp029_seed100_step10_ood_eval: seed100 step5→step10 纵向 OOD 变化验证 later-emerging property. step5 OOD=11.19% (NS vs SFT). 若 step10 OOD 显著上升 (>20%, p<0.05), 支持 gradual emergence claim; 若仍 NS, 需修正 claim 或增加 step15 数据点.（准备中）
- exp029_seed7_high_kl_step5_ood_v3: D134 协议 re-eval (retry): high_kl step5 checkpoint OOD eval. v2 因 GPU 显存不足 OOM crash (seed100 训练初始化阶段临时占用 cuda:2 显存). 现在 GPU 2/3 完全空闲, 重新提交. 原始 eval 得 8.21% (11/134).（准备中）
- exp029_seed5_response_mask_check: Ablation: eval seed5 step10 with enable_response_mask=true (vs baseline 25.37% with mask=false). Tests whether response_mask setting affects OOD eval results, resolving data consistency concern for Table 1.（准备中）
- ood_eval_high_kl_step7（准备中）
- ood_eval_high_kl_step5（准备中）
- …另有 26 项

## 近期结论
- **scienceworld_cell_d_episode** (killed): Episode-level advantage (full context window) generalizes beyond ALFWorld to ScienceWorld: the same mechanism that boosted ALFWorld performance will yield ≥2x improvement over step-independent baseline on ScienceWorld, demonstrating environment-agnostic benefit of episode-level credit assignment.
- **cell_b_1gpu_seed100** (killed): R6-N2: Cell B 多种子验证 OOD 5.97% 可靠性，plan_id 关联 factorial design claim。Cell B (h=2, episode-level advantage, M1 only) 在不同 seed 下应保持 OOD 性能近 SFT baseline（~5-7%），验证 M1 alone bounds but does not collapse。 ← 基于 factorial_h2_episodeadv_seed1
- **scienceworld_sft_bjb1_v2** (success): SFT on ScienceWorld expert trajectories (3586 samples) teaches Qwen3-1.7B environment interaction format. Retry of scienceworld_sft_bjb1 with per_device_eval_batch_size=1 fix (v1 OOM at step 112 eval). ← 基于 scienceworld_sft_bjb1
  [scienceworld_sft_v2_diagnosis](/api/workspace-files/projects/cost-verify-agent-rl/artifacts/scienceworld_sft_bjb1_v2/report/scienceworld_sft_v2_diagnosis.md)

## 趋势
成功 47 / 负向 23 / 失败 66 / 共 159

## 下一步
（无活跃 idea，请通过 ideas.md 添加）

## 资源状态
bjb1-17606: 无 GPU 信息

## 告警
- exp_001: 训练失败 — unknown
- exp_001b: 训练失败 — unknown
- exp_002: 训练失败 — unknown
- exp003: 训练失败 — unknown
- exp007: 训练失败 — unknown
- exp009: 训练失败 — unknown
- exp010: 训练失败 — unknown
- exp011: 已被终止 — unknown
- exp012: 训练失败 — unknown
- exp012b: 已被终止 — unknown
- exp013: 已被终止 — unknown
- exp013b: 训练失败 — unknown
- exp013c: 已被终止 — unknown
- exp013d: 训练失败 — unknown
- exp013e: 训练失败 — unknown
- exp015: 已被终止 — unknown
- exp016: 训练失败 — unknown
- exp019_expert_sft_v2: 已被终止 — unknown
- exp020_grpo_from_sft: 训练失败 — unknown
- exp022_grpo_from_sft_v4: 已被终止 — unknown
- exp023_grpo_parallel: 训练失败 — unknown
- exp023c_grpo_serial: 训练失败 — unknown
- exp024_success_gated_grpo: 已被终止 — unknown
- exp025: 训练失败 — unknown
- exp025b: 训练失败 — unknown
- exp025c: 已被终止 — unknown
- exp027_stable_grpo: 训练失败 — unknown
- exp028a_recipe_fix: 已被终止 — unknown
- exp028c_selfguide_recipe: 训练失败 — unknown
- gsweep_g050_h5_seed1: 已被终止 — unknown
- gae_baseline_seed1: 已被终止 — unknown
- hsweep_h10_seed1: 已被终止 — unknown
- exp029_episode_level_seed2: 已被终止 — unknown
- exp029_seed2_westd_resume: 已被终止 — unknown
- exp029_seed2_ood_reeval: 训练失败 — unknown
- exp029_seed2_ood_reeval_v3: 训练失败 — unknown
- 7b_zeroshot_eval_v2: 训练失败 — unknown
- exp029_seed2_ood_reeval_v4: 训练失败 — unknown
- 7b_cell_a_h2: 已被终止 — unknown
- 8b_sft_clean_eval: 训练失败 — unknown
- 8b_cell_c_episode: 训练失败 — unknown
- 8b_cell_c_episode_v2: 训练失败 — unknown
- 8b_cell_c_v3: 训练失败 — unknown
- 8b_cell_c_episode_v5: 训练失败 — unknown
- 8b_cell_c_episode_v6: 训练失败 — unknown
- 8b_cell_c_episode_v7: 训练失败 — unknown
- 8b_cell_c_episode_v8: 训练失败 — unknown
- exp029_per_task_t04: 训练失败 — unknown
- scienceworld_sft_eval: 已被终止 — unknown
- 8b_cell_c_episode_v9: 训练失败 — unknown
- 8b_cell_c_episode_v9b: 训练失败 — unknown
- 8b_cell_c_episode_v9c: 训练失败 — unknown
- 8b_v9d_ood_eval: 训练失败 — unknown
- 8b_v9d_ood_eval_v2: 训练失败 — unknown
- 8b_v9d_ood_eval_v3: 训练失败 — unknown
- 8b_v9d_ood_eval_v4: 训练失败 — unknown
- scienceworld_grpo_cell_c: 训练失败 — unknown
- scienceworld_info_loss_full: 训练失败 — unknown
- scienceworld_info_loss_h2: 已被终止 — unknown
- sw_info_loss_full_v2: 训练失败 — unknown
- scienceworld_grpo_cell_c_v2: 训练失败 — unknown
- exp029_seed3_episode: 训练失败 — unknown
- exp029_seed3_ood: 训练失败 — unknown
- exp029_seed4_episode: 训练失败 — unknown
- exp029_seed5_episode: 训练失败 — unknown
- exp029_seed6_episode: 训练失败 — unknown
- exp029_seed5_v2: 训练失败 — unknown
- sft_baseline_ood_eval: 训练失败 — unknown
- exp029_seed6_ood_eval: 训练失败 — unknown
- exp029_seed7_ood_precollapse: 已被终止 — unknown
- seed7_high_kl_step5_ood: 训练失败 — unknown
- c_prime_step5_ood: 训练失败 — unknown
- exp029_c_prime_resume_mt50: 训练失败 — unknown
- scienceworld_grpo_cell_c_v4: 训练失败 — unknown
- scienceworld_grpo_cell_c_v4b: 已被终止 — unknown
- exp029_seed200_episode: 训练失败 — unknown
- scienceworld_grpo_cell_c_v6: 训练失败 — unknown
- exp029_seed300_step5_ood_eval: 训练失败 — unknown
- exp029_seed300_step5_ood_eval_v2: 训练失败 — unknown
- exp029_seed200_episode_v3: 训练失败 — unknown
- exp029_seed300_step5_id_eval_diag: 训练失败 — unknown
- exp029_seed7_high_kl_step5_ood_v2: 训练失败 — unknown
- exp029_seed7_high_kl_step7_ood_v2: 训练失败 — unknown
- eval_variance_seed7hk_fix: 训练失败 — unknown
- hsweep_h10_seed2: 训练失败 — unknown
- hsweep_h10_seed2_retry: 已被终止 — unknown
- scienceworld_sft_bjb1: 训练失败 — unknown
- cell_b_1gpu_seed100: 已被终止 — unknown
- scienceworld_cell_d_episode: 已被终止 — unknown
