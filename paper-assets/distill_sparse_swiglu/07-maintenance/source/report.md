# Handover — 2026-05-25

> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。

## 运行中
（无）

## 待处理
（无）

## 近期结论
- **qwen14b_kl30_s123_gsm8k_v6** (success): Final attempt at s123 GSM8K eval with batch_size=1 (v5 had OOM with batch_size=8 on 14B). Data confirmed cached locally. If successful, Qwen table upgrades from 2-seed to 3-seed. ← 基于 qwen14b_kl30_s123_gsm8k_v5

## 趋势
成功 258 / 负向 26 / 失败 43 / 共 411
gsm8k_exact_match: 0.3609 ↑（近 3 次 success）

## 下一步
（无活跃 idea，请通过 ideas.md 添加）

## 资源状态
westd-34887: 无 GPU 信息

## 告警
- mvp_kl_s123: 已被终止 — unknown
- mvp_kl_s456: 已被终止 — unknown
- kl_lagrangian_v2: 已被终止 — unknown
- kl_normalized_quicktest: 训练失败 — unknown
- mvp_kl_norm_s42: 训练失败 — unknown
- mvp_kl_norm_s123: 训练失败 — unknown
- mvp_kl_norm_s456: 已被终止 — unknown
- kl_norm_v3_quicktest: 已被终止 — unknown
- spon_kl_s42: 已被终止 — unknown
- spon_training_seq2048: 已被终止 — unknown
- spon_2048_s42: 已被终止 — unknown
- ste_kl_s42: 已被终止 — unknown
- bce_isocompute_s42: 训练失败 — unknown
- eval_spon_supp_retry: 训练失败 — unknown
- bce_isocompute_s42_v2: 已被终止 — unknown
- spon_supp_eval_retry: 训练失败 — unknown
- bce_isocompute_v2_s42: 已被终止 — unknown
- kl_sparsity30_s42: 已被终止 — unknown
- kl_sparsity70_s42: 已被终止 — unknown
- kl_sparsity70_s42_v2: 已被终止 — unknown
- lm_eval_dense_test: 训练失败 — unknown
- lm_eval_mistral_downstream: 训练失败 — unknown
- diag_30pct_downstream: 已被终止 — unknown
- diag_gsm8k_gencomp: 已被终止 — unknown
- diag_teal_downstream: 已被终止 — unknown
- bench_mistral_kl50_s42: 已被终止 — unknown
- longbench_kl30_uniform: 训练失败 — unknown
- longbench_dense: 训练失败 — unknown
- longbench_kl30_uniform_v2: 训练失败 — unknown
- longbench_dense_v2: 训练失败 — unknown
- longbench_kl30_uniform_v3: 训练失败 — unknown
- longbench_dense_v3: 训练失败 — unknown
- longbench_dense_v4: 训练失败 — unknown
- longbench_dense_v5: 已被终止 — unknown
- steps_curve_s42: 已被终止 — unknown
- steps_curve_s42_v2: 已被终止 — unknown
- mag_preservation_reg: 训练失败 — unknown
- reverse_kl_50pct_s42: 已被终止 — unknown
- jsd_50pct_s42: 已被终止 — unknown
- kl50_s456_train_eval: 已被终止 — unknown
- c4_download: 已被终止 — unknown
- qwen14b_kl30_uniform_eval: 训练失败 — unknown
- qwen14b_teal30_uniform_eval: 训练失败 — unknown
- qwen14b_kl30_uniform_eval_4task: 已被终止 — unknown
- qwen14b_teal30_uniform_eval_4task: 已被终止 — unknown
- c4_ood_dense_baseline: 训练失败 — unknown
- downstream_ext_kl50_uniform_s42: 训练失败 — unknown
- downstream_ext_kl30_uniform_s123: 训练失败 — unknown
- kl_sparsity40_s42_eval_teal_uniform: 已被终止 — unknown
- c1_ablation_30pct_s42: 训练失败 — unknown
- c1_ablation_30pct_s42_eval: 训练失败 — unknown
- bce_isocompute_hellaswag_piqa: 训练失败 — unknown
- c1_ablation_30pct_eval_34887: 已被终止 — unknown
- c1_eval_30pct_s456: 已被终止 — unknown
- qwen14b_kl30_s123_eval: 已被终止 — unknown
- qwen14b_kl30_s456_eval: 已被终止 — unknown
- qwen14b_kl30_s123_eval_v2: 训练失败 — unknown
- qwen14b_kl30_s123_eval_v3: 训练失败 — unknown
- qwen14b_kl30_s42_eval_uniform: 训练失败 — unknown
- qwen14b_kl30_s42_eval_uniform_v2: 已被终止 — unknown
- qwen14b_teal275_uniform_eval: 已被终止 — unknown
- qwen14b_teal275_uniform_eval_v2: 训练失败 — unknown
- flashinfer_benchmark_llama8b: 训练失败 — unknown
- flashinfer_benchmark_llama8b_v2: 已被终止 — unknown
- qwen14b_kl30_s42_gsm8k: 已被终止 — unknown
- qwen14b_dense_4task: 训练失败 — unknown
- qwen14b_kl30_s123_gsm8k: 已被终止 — unknown
- bench_kl30_uniform_gsm8k_d075: 已被终止 — unknown
- bench_teal30_uniform_gsm8k: 已被终止 — unknown
- bench_teal30_uniform_6task: 已被终止 — unknown
- bench_teal50_uniform_6task: 已被终止 — unknown
- kl30_uniform_hspiqa_s123: 已被终止 — unknown
- kl30_uniform_hspiqa_s456: 已被终止 — unknown
- kl_sparsity40_s42_global_eval: 训练失败 — unknown
- kl50_global_s456_eval: 已被终止 — unknown
- revkl_30_s42_uniform_eval: 已被终止 — unknown
- mse50_s123_eval_retry: 已被终止 — Director ordered kill - PPL=15789 (random level), MSE sparsity collapsed to 5.1% during training, forced 50% mask produces garbage. Not re-running.
- debug_find_revkl_logs: 已被终止 — unknown
- debug_read_revkl_results: 已被终止 — unknown
- debug_find_bce_ckpt_34887: 已被终止 — unknown
- debug_grep_bce_ppl: 已被终止 — unknown
- debug_list_ckpts_41718: 已被终止 — unknown
- debug_list_ckpts_34887: 已被终止 — unknown
- debug_check_bce_iso_ckpts: 已被终止 — unknown
- perlayer_kl_30_s42: 已被终止 — unknown
- perlayer_kl_30_s123: 已被终止 — unknown
- perlayer_kl_30_s456: 已被终止 — unknown
- perlayer_kl_30_s42_v2: 已被终止 — unknown
- perlayer_kl_30_s123_v2: 已被终止 — unknown
- perlayer_kl_30_s456_v2: 已被终止 — unknown
- perlayer_kl_30_s42_v3: 已被终止 — unknown
- perlayer_kl_30_s123_v3: 已被终止 — unknown
- perlayer_kl_30_s456_v3: 已被终止 — unknown
- perlayer_kl_30_s42_v4: 已被终止 — unknown
- revkl_30_s456_downstream: 已被终止 — unknown
- perlayer_kl_30_s42_v5: 已被终止 — unknown
- diag_41718_processes: 已被终止 — unknown
- diag_34887_processes: 已被终止 — unknown
- kill_old_41718: 已被终止 — unknown
- kill_old_34887: 已被终止 — unknown
- diag_ckpt_41718: 已被终止 — unknown
- diag_ckpt_34887: 已被终止 — unknown
- read_boolq_results: 已被终止 — unknown
- perlayer_kl_s456_boolq: 已被终止 — unknown
- diag_status_41718: 已被终止 — unknown
- diag_status_34887: 已被终止 — unknown
- diag_eval_env_34887: 已被终止 — unknown
- perlayer_kl_s123_downstream: 训练失败 — unknown
- revkl_30_s42_boolq_uniform: 训练失败 — unknown
- perlayer_kl_50_s42_ppl: 已被终止 — unknown
- perlayer_kl_50_s42_boolq: 已被终止 — unknown
- perlayer_kl_k4_s42: 已被终止 — unknown
- perlayer_kl_k4_s456: 已被终止 — unknown
- perlayer_kl_k4_s123: 已被终止 — unknown
- constraint_remove_valley_kl30_s42: 已被终止 — unknown
- constraint_protect_late_kl30_s42: 已被终止 — unknown
- perlayer_kl_k4_50_s42_ppl: 训练失败 — unknown
- perlayer_kl_k16_s42: 训练失败 — unknown
- perlayer_kl_k16_s42_v2: 训练失败 — unknown
- perlayer_kl_k16_s42_v3_eval: 训练失败 — unknown
- perlayer_kl_k16_eval_v2: 训练失败 — unknown
- perlayer_kl_k16_s42_eval_final: 训练失败 — unknown
- perlayer_kl_k16_s456: 训练失败 — unknown
- qwen14b_kl30_s123_gsm8k_v2: 训练失败 — unknown
- qwen14b_kl30_s123_gsm8k_v3: 训练失败 — unknown
<!-- 已截断：超过 150 行限制，已执行 Pre-compaction Flush -->
