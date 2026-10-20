# Research conversation: [HANDOFF] 你是 Main Agent，这是 Loop #8。 ## 上一轮交接 (task_context) ### 1. 🔴 硬约束 / 红线 - GPU 白名单: autodl-5090 cuda:0-3 only，其他设备号 — Part 17 of 39

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

[← Part 16](part-016.md) · [Transcript overview](../research-conversation-handoff-main-agent-loop-8-task-context-1-gpu-autodl-5090-cuda-0-3-only.md) · [Part 18 →](part-018.md) · [Structured JSON](../../../sessions/f4/f4b5c108043649dc26e3.json)

## Round 257

### Tool result

_source line 3144 · 2026-05-19T05:24:57.572Z_

<details><summary>↩ Tool result · `toolu_012g6Ca86GQCpJskwiNNxHWR`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp_054_instruct_llama3_2_3b\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-18T03:06:07.150Z\", \"updated_at\": \"2026-05-18T07:58:31.553Z\", \"hypothesis\": \"Instruct-tuned Llama-3.2-3B-Instruct shows degraded depth signal vs base Llama-3.2-3B (F1=0.697), quantifying instruction-tuning's impact on DDR\", \"notes\": \"生成 59% (292/497 seeds) 后 Worker 与服务器断连。脚本有 resume 支持。模型已下载到 /root/autodl-tmp/models/Llama-3.2-3B-Instruct-ms/。Eval 脚本已准备: eval_exp054_instruct_llama.py\", \"conclusion\": \"success\", \"metrics\": {\"instruct_binary_f1\": 0.8381, \"instruct_binary_ci\": [0.828, 0.847], \"instruct_3class_f1\": 0.5437, \"instruct_3class_ci\": [0.53, 0.558], \"base_binary_f1\": 0.8488, \"base_3class_f1\": 0.7424, \"rho_instruct_entropy_mean\": 0.2299, \"rho_instruct_entropy_std\": 0.2623, \"rho_instruct_entropy_min\": -0.0027, \"rho_instruct_entropy_max\": 0.2036, \"rho_instruct_tail_decay\": 0.1198, \"rho_instruct_ttr\": -0.1411, \"rho_instruct_hapax_ratio\": -0.1157, \"rho_base_entropy_mean\": -0.627, \"rho_base_ttr\": -0.6856, \"rho_base_hapax_ratio\": -0.6975, \"direction_reversals\": 3, \"reversed_features\": [\"entropy_mean\", \"entropy_std\", \"tail_decay\"], \"data_count\": 4974}}, \"exp_050_temp_curve_t09\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T22:15:11.626Z\", \"updated_at\": \"2026-05-18T06:09:24.876Z\", \"hypothesis\": \"DDR signal at t=0.9 degrades relative to t=0.7 but less severely than t=1.0, establishing monotonic temperature sensitivity\", \"conclusion\": \"failed\", \"notes\": \"Registry 误标 failed（startup recovery 机制）。实际 tmux tc_fix 仍在运行中。Phase 2 (Pythia-2.8B t=0.9) 39% 完成 (392/995 seeds)，预计 ~76min。Phase 3 (Qwen3-1.7B t=0.9) 待执行。总计 ~5-6h 完成。\", \"metrics\": {\"records\": 4536, \"model\": \"pythia-2.8b\", \"temperature\": 0.9, \"top_p\": 0.9, \"within_cv_binary_f1\": 0.5821, \"within_cv_binary_ci\": [0.5655, 0.5985], \"logo_binary_f1\": 0.4804, \"logo_binary_ci\": [0.4645, 0.4976], \"entropy_mean_rho\": -0.3016, \"delta_vs_t07_cv\": -0.157, \"delta_vs_t07_logo\": -0.259}}, \"exp_049_temp_curve_t05\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T22:15:10.383Z\", \"updated_at\": \"2026-05-18T06:09:22.443Z\", \"hypothesis\": \"DDR signal at t=0.5 should be stronger than t=0.7 (less randomness preserves more distributional structure)\", \"conclusion\": \"success\", \"notes\": \"Registry 误标 failed（startup recovery 机制）。实际 tmux tc_fix 仍在运行中。Phase 1 (t=0.5 generation) 已完成 4708 records。等待 phase 2+3 完成后统一提取特征和评估。\", \"metrics\": {\"records\": 4708, \"skipped\": 113, \"seeds\": 995, \"model\": \"pythia-2.8b\", \"temperature\": 0.5, \"top_p\": 0.9, \"within_cv_binary_f1\": 0.8432, \"within_cv_binary_ci\": [0.8301, 0.8558], \"logo_binary_f1\": 0.8136, \"logo_binary_ci\": [0.7984, 0.8282], \"entropy_mean_rho\": -0.5844}}, \"exp_053_instruct_olmo2_1b\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-18T03:06:06.142Z\", \"updated_at\": \"2026-05-18T03:46:16.047Z\", \"hypothesis\": \"Instruct-tuned OLMo-2-1B-Instruct shows degraded depth signal vs base OLMo-2-1B (F1=0.695), quantifying instruction-tuning's impact on DDR\", \"conclusion\": \"success\", \"metrics\": {\"within_binary_f1\": 0.8131, \"within_binary_ci\": [0.8012, 0.8251], \"within_3class_f1\": 0.5748, \"within_3class_ci\": [0.5605, 0.5897], \"base_binary_f1\": 0.8454, \"base_3class_f1\": 0.7538, \"gen1_f1_instruct\": 0.256, \"gen1_f1_base\": 0.523, \"delta_within_binary\": -0.032, \"delta_within_3class\": -0.179, \"spearman_instruct\": {\"entropy_mean\": 0.482, \"entropy_std\": 0.296, \"entropy_min\": 0.08, \"entropy_max\": 0.306, \"tail_decay\": 0.228, \"ttr\": 0.006, \"hapax_ratio\": 0.025}, \"spearman_base\": {\"entropy_mean\": -0.639, \"entropy_std\": -0.296, \"entropy_min\": -0.387, \"entropy_max\": 0.067, \"tail_decay\": -0.141, \"ttr\": -0.7, \"hapax_ratio\": -0.712}, \"features_reversed\": \"6/7\", \"model_used\": \"allenai/OLMo-2-0425-1B-Instruct\"}}, \"exp_052_instruct_qwen3_1_7b\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-18T03:06:04.788Z\", \"updated_at\": \"2026-05-18T03:26:14.267Z\", \"hypothesis\": \"Instruct-tuned Qwen3-1.7B (chat template, thinking=off) shows degraded depth signal vs base Qwen3-1.7B (F1=0.709), quantifying instruction-tuning's impact on DDR\", \"conclusion\": \"success\", \"metrics\": {\"within_binary_f1\": 0.8753, \"within_binary_ci\": [0.8667, 0.8837], \"within_3class_f1\": 0.7324, \"within_3class_ci\": [0.7195, 0.745], \"base_binary_f1\": 0.8614, \"base_3class_f1\": 0.769, \"logo_instruct_binary\": 0.658, \"logo_instruct_3class\": 0.543, \"logo_base_binary\": 0.821, \"logo_base_3class\": 0.802, \"gen1_f1_instruct\": 0.438, \"gen1_f1_base\": 0.579, \"spearman_direction\": \"reversed (instruct ρ>0, base ρ<0)\", \"delta_within_binary\": 0.014, \"delta_within_3class\": -0.037, \"delta_logo_binary\": -0.163}}, \"exp_051_independent_seed\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T22:38:00.466Z\", \"updated_at\": \"2026-05-18T02:01:42.126Z\", \"hypothesis\": \"Cross-generator depth classification with non-overlapping seeds achieves comparable F1 to shared-seed LOGO, ruling out topic fingerprint leakage\", \"conclusion\": \"success\", \"metrics\": {\"pythia_to_olmo_binary_f1\": 0.6945, \"pythia_to_olmo_ci\": [0.6727, 0.7167], \"olmo_to_pythia_binary_f1\": 0.666, \"olmo_to_pythia_ci\": [0.6429, 0.6893], \"avg_binary_f1\": 0.6803, \"shared_seed_logo_ref\": 0.694, \"delta_vs_shared\": -0.014}}, \"exp_048_cross_temp_transfer\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T12:52:44.889Z\", \"updated_at\": \"2026-05-17T17:07:19.391Z\", \"hypothesis\": \"Cross-temperature transfer: XGBoost 7-feature classifier trained at one sampling temperature (t=0.7 or t=1.0) maintains depth discrimination when tested at a different temperature, demonstrating deployment robustness to unknown decoding parameters\", \"conclusion\": \"success\", \"metrics\": {\"6gen_logo\": {\"within_0.7_binary\": 0.9471, \"within_0.7_3class\": 0.7888, \"cross_0.7to1.0_binary\": 0.9001, \"cross_0.7to1.0_3class\": 0.7225, \"within_1.0_binary\": 0.9107, \"within_1.0_3class\": 0.7257, \"cross_1.0to0.7_binary\": 0.9581, \"cross_1.0to0.7_3class\": 0.7913, \"caveat\": \"Only Qwen3-1.7B differs between conditions; 5/6 generators share data\"}, \"qwen_only\": {\"within_0.7_binary\": 0.9262, \"within_0.7_binary_ci\": [0.916, 0.935], \"within_0.7_3class\": 0.769, \"within_0.7_3class_ci\": [0.756, 0.781], \"cross_0.7to1.0_binary\": 0.7574, \"cross_0.7to1.0_binary_ci\": [0.745, 0.77], \"cross_0.7to1.0_3class\": 0.4581, \"cross_0.7to1.0_3class_ci\": [0.445, 0.472], \"within_1.0_binary\": 0.8248, \"within_1.0_binary_ci\": [0.81, 0.838], \"within_1.0_3class\": 0.5738, \"within_1.0_3class_ci\": [0.56, 0.588], \"cross_1.0to0.7_binary\": 0.9443, \"cross_1.0to0.7_binary_ci\": [0.936, 0.953], \"cross_1.0to0.7_3class\": 0.6014, \"cross_1.0to0.7_3class_ci\": [0.593, 0.611], \"delta_0.7train_binary_pp\": -16.9, \"delta_0.7train_3class_pp\": -31.1, \"delta_1.0train_binary_pp\": 12, \"delta_1.0train_3class_pp\": 2.8, \"asymmetric_transfer\": true}}, \"parent\": \"exp_047_multi_domain_t07\"}, \"exp_047_multi_domain_t07\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T05:51:25.881Z\", \"updated_at\": \"2026-05-17T07:22:04.483Z\", \"hypothesis\": \"Depth fingerprint generalizes across domains (News, Academic, Code) under standard decoding (t=0.7, top_p=0.9) matching main experiment params, eliminating the temperature confound from t=1.0 results and producing directly comparable domain generalization numbers\", \"parent\": \"exp_043_multi_domain_seeds\", \"metrics\": {\"news_binary_f1\": 0.7119, \"news_binary_ci\": [0.6898, 0.7332], \"news_3class_f1\": 0.7149, \"academic_binary_f1\": 0.6279, \"academic_binary_ci\": [0.6027, 0.6515], \"academic_3class_f1\": 0.6564, \"code_binary_f1\": 0.6872, \"code_binary_ci\": [0.6641, 0.71], \"code_3class_f1\": 0.6729, \"overall_binary_f1\": 0.6757, \"overall_3class_f1\": 0.6814, \"delta_vs_t10_news\": -0.034, \"delta_vs_t10_academic\": -0.1107, \"delta_vs_t10_code\": -0.0663}, \"conclusion\": \"success\"}, \"multi_domain_t07\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-17T05:54:55.365Z\", \"updated_at\": \"2026-05-17T05:54:55.365Z\"}, \"multi-domain-seeds\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T03:38:54.349Z\", \"updated_at\": \"2026-05-17T05:05:40.584Z\", \"hypothesis\": \"Domain independence: depth fingerprint 的 differential depth response 不依赖 seed domain——在 News/Academic/Code 三个非 Wikipedia 域上，7-feature ensemble 的 binary F1 与 Wikipedia baseline 差异 <10pp，证明 DDR 是生成过程的固有特性而非特定域文本属性的 artifact\", \"metrics\": {\"news_binary_f1\": 0.7459, \"news_binary_ci\": [0.726, 0.764], \"news_multiclass_f1\": 0.6516, \"academic_binary_f1\": 0.7386, \"academic_binary_ci\": [0.72, 0.757], \"academic_multiclass_f1\": 0.6223, \"code_binary_f1\": 0.7535, \"code_binary_ci\": [0.737, 0.77], \"code_multiclass_f1\": 0.6344, \"wikipedia_baseline_binary_f1\": 0.8148, \"wikipedia_baseline_multiclass_f1\": 0.8632, \"max_gap_vs_wiki_pp\": 7.62, \"worst_domain\": \"academic\", \"best_domain\": \"code\", \"conclusion_label\": \"domain_independent\"}, \"conclusion\": \"success\"}, \"plan-008-seed-stratification\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T00:21:12.380Z\", \"updated_at\": \"2026-05-17T02:56:26.724Z\", \"hypothesis\": \"Seed complexity independence: depth fingerprint 的判别能力不依赖 seed 文本的词汇复杂度（按 gen-0 TTR terciles 分层验证）\", \"conclusion\": \"success\", \"metrics\": {\"low_complexity_binary\": 0.685, \"medium_binary\": 0.695, \"high_complexity_binary\": 0.695, \"low_complexity_multi\": 0.772, \"medium_multi\": 0.778, \"high_complexity_multi\": 0.779, \"max_diff_binary_pp\": 1.06, \"max_diff_multiclass_pp\": 0.68, \"conclusion_label\": \"seed_independent\"}, \"parent\": \"plan-010-robustness\"}, \"plan-002-qwen06b-r2-s1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T22:35:11.142Z\", \"updated_at\": \"2026-05-17T02:56:25.805Z\", \"hypothesis\": \"跨家族泛化数据生成（Qwen3-0.6B shard1）：Qwen3-0.6B continuation 链第二分片，补全 ~995 seeds 覆盖\", \"notes\": \"Orphan 进程 PID 118126 存活，shard1 进度 340/500 seeds (68%)，当前 1542 行，预计 ~23:00 UTC 完成。GPU cuda:3 利用率 33%。\", \"conclusion\": \"success\", \"metrics\": {\"records\": 2268, \"seeds\": 498, \"depth_dist\": {\"0\": 498, \"1\": 493, \"2\": 470, \"3\": 417, \"4\": 390}, \"file\": \"generations_shard1.jsonl\"}, \"parent\": \"plan-002\"}, \"plan-002-qwen06b-r2-s0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T22:35:10.950Z\", \"updated_at\": \"2026-05-17T02:56:23.413Z\", \"hypothesis\": \"跨家族泛化数据生成（Qwen3-0.6B shard0）：最小参数量(0.6B) Qwen 模型的 continuation 链，验证 depth signal 在极小模型中是否仍存在（小模型可能因容量不足而无法维持深层生成的分布稳定性）\", \"notes\": \"Orphan 进程 PID 117855 存活，shard0 进度 350/500 seeds (70%)，当前 1593 行，预计 ~23:00 UTC 完成。GPU cuda:2 利用率 34%。\", \"conclusion\": \"success\", \"metrics\": {\"records\": 2270, \"seeds\": 498, \"depth_dist\": {\"0\": 498, \"1\": 493, \"2\": 468, \"3\": 423, \"4\": 388}, \"file\": \"generations_shard0.jsonl\"}, \"parent\": \"plan-002\"}, \"review-exp-c-overall-ci\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T12:22:37.037Z\", \"updated_at\": \"2026-05-17T02:56:15.141Z\", \"hypothesis\": \"6-generator LOGO 的 overall bootstrap CI 窄且不跨越 chance level，entropy_max/entropy_min 的个体 Spearman ρ 验证其对 depth 的单调贡献方向（max 正相关因高 depth 分布更尖，min 负相关因低概率 tail 被压缩）\", \"conclusion\": \"success\", \"metrics\": {\"overall_logo_f1\": 0.7879, \"overall_ci95\": [0.783, 0.7929], \"spearman_entropy_max\": 0.0503, \"spearman_entropy_min\": -0.4061, \"spearman_hapax\": -0.6467, \"spearman_ttr\": -0.6302, \"spearman_entropy_mean\": -0.6098, \"spearman_entropy_std\": -0.1996, \"spearman_tail_decay\": -0.0403}}, \"review-exp-b-topic-drift\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T12:22:34.096Z\", \"updated_at\": \"2026-05-17T02:56:11.446Z\", \"hypothesis\": \"Depth fingerprint 不仅仅捕捉 topic shift：语义漂移(embedding cosine similarity)与 depth 相关性弱(|ρ|<0.3)，而 entropy/lexical features 与 depth 的相关性强(|ρ|>0.5)，证明 depth signal 来自生成过程的统计特性而非内容偏移\", \"conclusion\": \"success\", \"metrics\": {\"semantic_similarity_by_transition\": {\"0_to_1\": {\"mean\": 0.622, \"std\": 0.1647}, \"1_to_2\": {\"mean\": 0.6829, \"std\": 0.1837}, \"2_to_3\": {\"mean\": 0.801, \"std\": 0.2012}, \"3_to_4\": {\"mean\": 0.8587, \"std\": 0.1895}}, \"prompt_type_avg_sim\": {\"continuation\": 0.7168, \"elaboration\": 0.8093, \"inspired_rewriting\": 0.808}, \"shape_feature_correlations\": {\"entropy_std_rho\": -0.1639, \"tail_decay_rho\": 0.0675}, \"drifting_feature_correlations\": {\"hapax_ratio_rho\": -0.1242, \"ttr_rho\": -0.1784, \"entropy_mean_rho\": -0.2859}}}, \"plan-014\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T00:12:01.909Z\", \"updated_at\": \"2026-05-17T02:56:07.395Z\", \"hypothesis\": \"大模型规模泛化：Qwen3-8B (7B+参数) 的 continuation 链是否展现同样的 entropy 收敛和 lexical drift，验证 depth dynamics 不因模型容量增大而消失（更大模型可能有更强的分布记忆导致 depth signal 衰减）\", \"notes\": \"2026-05-15 04:25: ✅ 完整数据重算完成 (4409 records, 977 seeds)。与 82% 快照差异在统计噪声范围内：LOGO +0.0011, qwen8b held-out -0.0037。最终数字已确认，可用于论文。\", \"conclusion\": \"success\", \"metrics\": {\"total_records\": 4497, \"unique_seeds\": 995, \"depth_dist\": {\"0\": 995, \"1\": 979, \"2\": 937, \"3\": 831, \"4\": 755}, \"logo_6gen_avg_f1\": 0.7893, \"logo_per_generator\": {\"olmo-2-1b\": 0.7635, \"pythia-1b\": 0.8562, \"pythia-2.8b\": 0.8041, \"qwen3-0.6b\": 0.8243, \"qwen3-1.7b\": 0.8046, \"qwen3-8b\": 0.6832}, \"logo_qwen3_8b_held_out_f1\": 0.6832, \"logo_5gen_baseline_f1\": 0.8, \"spearman\": {\"hapax_ratio\": -0.5578, \"ttr\": -0.5419, \"entropy_mean\": -0.4754, \"entropy_min\": -0.3029, \"entropy_max\": 0.0946, \"tail_decay\": -0.0894, \"entropy_std\": -0.0755}, \"feature_importance\": {\"hapax_ratio\": 0.269, \"entropy_mean\": 0.1637, \"ttr\": 0.159, \"entropy_max\": 0.0634, \"entropy_std\": 0.0463, \"entropy_min\": 0.0153, \"tail_decay\": 0.0123}, \"revalidation_v2_vs_snapshot\": \"LOGO +0.0007 (0.7886→0.7893), qwen8b -0.0054 (0.6886→0.6832)\", \"revalidation_v2_conclusion\": \"complete_data_validates_snapshot_robustness\"}, \"parent\": \"plan-002\"}, \"plan-002-qwen17b-r2-s1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T21:58:14.195Z\", \"updated_at\": \"2026-05-17T02:56:03.576Z\", \"notes\": \"Orphan 进程 PID 120694 存活，shard1 进度 295/500 seeds (59%)，预计 ~22:55 UTC 完成。GPU cuda:1 利用率 44%。\", \"conclusion\": \"success\", \"metrics\": {\"records\": 2326, \"seeds\": 498, \"depth_dist\": {\"0\": 498, \"1\": 491, \"2\": 473, \"3\": 440, \"4\": 424}, \"skipped\": 53, \"duration_s\": 4228, \"file\": \"generations_shard1.jsonl\"}, \"hypothesis\": \"跨家族泛化数据生成（Qwen3-1.7B shard1）：Qwen3-1.7B continuation 链第二分片，补全 ~995 seeds 覆盖\", \"parent\": \"plan-002\"}, \"plan-002-qwen17b-r2-s0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T21:58:12.310Z\", \"updated_at\": \"2026-05-17T02:56:01.158Z\", \"notes\": \"Orphan 进程 PID 120617 存活，shard0 进度 289/500 seeds (58%)，预计 ~22:55 UTC 完成。GPU cuda:0 利用率 40%。\", \"conclusion\": \"success\", \"metrics\": {\"records\": 2291, \"seeds\": 498, \"depth_dist\": {\"0\": 498, \"1\": 492, \"2\": 468, \"3\": 435, \"4\": 398}, \"skipped\": 199, \"duration_s\": 4548.2, \"file_size_mb\": 2.5, \"file\": \"generations_shard0.jsonl\"}, \"hypothesis\": \"跨家族泛化数据生成（Qwen3-1.7B shard0）：Qwen 家族 1.7B 模型的 continuation 链 depth dynamics，验证中等规模非 Pythia 模型也产生可检测的 depth signal\", \"parent\": \"plan-002\"}, \"plan-002-olmo2-s1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T20:09:46.880Z\", \"updated_at\": \"2026-05-17T02:55:54.134Z\", \"conclusion\": \"success\", \"metrics\": {\"records\": 2334, \"seeds\": 498, \"skipped\": 70, \"wall_time_s\": 4081.2, \"depth_dist\": {\"gen0\": 498, \"gen1\": 494, \"gen2\": 470, \"gen3\": 444, \"gen4\": 428}, \"file\": \"generations_shard1.jsonl\", \"file_size_mb\": 2.57}, \"hypothesis\": \"跨家族泛化数据生成（OLMo-2-1B shard1）：OLMo-2-1B continuation 链第二分片，补全 ~995 seeds 覆盖\", \"parent\": \"plan-002\"}, \"plan-002-olmo2-s0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T20:09:45.173Z\", \"updated_at\": \"2026-05-17T02:55:52.145Z\", \"conclusion\": \"success\", \"metrics\": {\"records\": 2379, \"seeds\": 497, \"skipped\": 47, \"wall_time_s\": 3885.2, \"depth_dist\": {\"gen0\": 497, \"gen1\": 494, \"gen2\": 477, \"gen3\": 461, \"gen4\": 450}, \"file\": \"generations_shard0.jsonl\", \"file_size_mb\": 2.68}, \"hypothesis\": \"跨家族泛化数据生成（OLMo-2-1B shard0）：非 Pythia 架构(OLMo)的 continuation 链中 depth signal 是否存在，验证 depth dynamics 跨训练数据和架构的普遍性\", \"parent\": \"plan-002\"}, \"plan-002-pythia1b-s1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T20:09:42.815Z\", \"updated_at\": \"2026-05-17T02:55:49.321Z\", \"conclusion\": \"success\", \"metrics\": {\"records\": 2269, \"seeds\": 498, \"skipped\": 100, \"wall_time_s\": 2247.6, \"depth_dist\": {\"gen0\": 498, \"gen1\": 496, \"gen2\": 455, \"gen3\": 422, \"gen4\": 398}, \"file\": \"data/pythia-1b/generations_shard1.jsonl\", \"file_size_mb\": 2.44}, \"hypothesis\": \"跨模型泛化数据生成（Pythia-1B shard1）：Pythia-1B continuation 链第二分片，与 shard0 合并后提供完整 ~995 seeds 的 depth 数据\", \"parent\": \"plan-002\"}, \"plan-002-pythia1b-s0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T20:09:40.947Z\", \"updated_at\": \"2026-05-17T02:55:46.455Z\", \"conclusion\": \"success\", \"metrics\": {\"records\": 2286, \"seeds\": 497, \"skipped\": 91, \"wall_time_s\": 2296.7, \"depth_dist\": {\"gen0\": 497, \"gen1\": 497, \"gen2\": 457, \"gen3\": 429, \"gen4\": 406}, \"file\": \"data/pythia-1b/generations_shard0.jsonl\", \"file_size_mb\": 2.5}, \"hypothesis\": \"跨模型泛化数据生成（Pythia-1B shard0）：同家族更大模型 Pythia-1B 的 continuation 链是否展现与 Pythia-2.8B 相似的 depth dynamics，验证 depth signal 非特定参数量产物\", \"parent\": \"plan-002\"}, \"plan-002-eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T23:33:25.348Z\", \"updated_at\": \"2026-05-17T02:55:34.658Z\", \"hypothesis\": \"跨生成器泛化评估：Pythia-410M 深度特征在 leave-one-generator-out 设置下能否泛化到未见过的生成器\", \"conclusion\": \"success\", \"metrics\": {\"leave_one_out_avg_macro_f1\": 0.8037, \"best_held_out\": {\"model\": \"pythia-1b\", \"macro_f1\": 0.8507}, \"worst_held_out\": {\"model\": \"olmo-2-1b\", \"macro_f1\": 0.7519}, \"family_out_delta\": 0.0107, \"ablation_full_f1\": 0.8037, \"ablation_reference_only_f1\": 0.7543, \"ablation_surface_only_f1\": 0.7471, \"mcnemar_p\": 0, \"top_features\": [\"hapax_ratio_0.289\", \"ttr_0.168\", \"entropy_mean_0.160\"], \"entropy_std_drop\": 0.0049, \"entropy_std_drift\": 0.12, \"entropy_mean_drift\": 1.5}, \"parent\": \"plan-002\"}, \"plan-010-llm-rephrase\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T22:26:58.107Z\", \"updated_at\": \"2026-05-17T02:55:34.090Z\", \"hypothesis\": \"LLM-simulated editing robustness: Qwen3-0.6B rephrasing (1-3 sentences) 比 random word replacement 更接近真实人类编辑，预期 depth fingerprint 退化更小\", \"conclusion\": \"success\", \"notes\": \"v2 修复版：修正 binary task 定义(gen1-vs-gen2+)、3-class mapping、tail_decay 计算(rank 100-1000)。Original binary 0.6918 与 Table 3 (0.7014) 一致，确认修复正确。\", \"metrics\": {\"original_binary_f1\": 0.6918, \"original_binary_ci\": [0.6749, 0.7067], \"original_multiclass_f1\": 0.7385, \"original_multiclass_ci\": [0.7269, 0.7496], \"rephrased_binary_f1\": 0.6471, \"rephrased_binary_ci\": [0.6308, 0.6619], \"rephrased_multiclass_f1\": 0.6672, \"rephrased_multiclass_ci\": [0.6548, 0.6796], \"binary_drop\": -0.0447, \"multiclass_drop\": -0.0713, \"edit_distance_ratio\": 0.5071, \"avg_sentences_replaced\": 1.69, \"method\": \"7feature LOGO-CV, binary=gen1-vs-gen2+, 3class=gen0/gen1/gen2+\", \"bugs_fixed\": [\"binary_task_gen1_vs_gen2+\", \"3class_mapping\", \"tail_decay_rank100-1000\"]}, \"parent\": \"plan-010-robustness\"}, \"plan-015-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T00:56:20.612Z\", \"updated_at\": \"2026-05-17T02:55:33.529Z\", \"conclusion\": \"success\", \"hypothesis\": \"Ordinal baseline bugfix + bootstrap CI: 修复 Binoculars denominator bug，验证 7-feature ensemble 显著优于所有单一检测器\", \"metrics\": {\"seven_feature_logo_f1\": 0.798, \"seven_feature_ci95\": [0.786, 0.799], \"avg_logprob_logo_f1\": 0.7653, \"avg_logprob_ci95\": [0.616, 0.82], \"ld_score_logo_f1\": 0.7212, \"ld_score_ci95\": [0.588, 0.77], \"fastdetectgpt_logo_f1\": 0.6269, \"fastdetectgpt_ci95\": [0.511, 0.762], \"binoculars_logo_f1\": 0.579, \"binoculars_ci95\": [0.405, 0.664], \"binoculars_bug_fixed\": true, \"ld_score_corrected_cv_f1\": 0.7925, \"bootstrap_7feat_vs_avglogprob\": {\"delta\": 0.039, \"p\": 0, \"significant\": true}, \"bootstrap_7feat_vs_fastdetectgpt\": {\"delta\": 0.067, \"p\": 0, \"significant\": true}}, \"parent\": \"plan-015\"}, \"plan-004-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T00:45:17.861Z\", \"updated_at\": \"2026-05-17T02:55:33.296Z\", \"hypothesis\": \"Downstream utility (retry): depth-stratified 数据对 OLMo-2-0425-1B CLM fine-tuning 的影响——5 variants × 3 seeds，输出到数据盘\", \"notes\": \"15/15 runs 全部完成。Claim 3 (Downstream Utility) 负面结果：depth-aware curation 不优于随机抽样。排名 all(2.335) < size_matched(2.367) < depth01(2.387) ≈ binary_filtered(2.389) << depth0_only(2.681)。全量数据最优，depth filtering 反而损害 perplexity。跨 seed 方差极小(<0.002)。已由 D009 reframe 为 diagnostic-not-curative。\", \"conclusion\": \"negative\", \"metrics\": {\"total_runs\": 15, \"completed\": 15, \"variants\": {\"all\": {\"eval_loss_mean\": 0.848, \"perplexity_mean\": 2.335, \"seeds\": {\"42\": {\"eval_loss\": 0.848, \"ppl\": 2.335}, \"123\": {\"eval_loss\": 0.848, \"ppl\": 2.335}, \"456\": {\"eval_loss\": 0.8482, \"ppl\": 2.3354}}}, \"size_matched\": {\"eval_loss_mean\": 0.8617, \"perplexity_mean\": 2.367, \"seeds\": {\"42\": {\"eval_loss\": 0.8618, \"ppl\": 2.367}, \"123\": {\"eval_loss\": 0.8615, \"ppl\": 2.367}, \"456\": {\"eval_loss\": 0.8618, \"ppl\": 2.367}}}, \"depth01\": {\"eval_loss_mean\": 0.8701, \"perplexity_mean\": 2.387, \"seeds\": {\"42\": {\"eval_loss\": 0.8703, \"ppl\": 2.3877}, \"123\": {\"eval_loss\": 0.87, \"ppl\": 2.3869}, \"456\": {\"eval_loss\": 0.8699, \"ppl\": 2.387}}}, \"binary_filtered\": {\"eval_loss_mean\": 0.8709, \"perplexity_mean\": 2.389, \"seeds\": {\"42\": {\"eval_loss\": 0.8708, \"ppl\": 2.389}, \"123\": {\"eval_loss\": 0.871, \"ppl\": 2.389}, \"456\": {\"eval_loss\": 0.871, \"ppl\": 2.389}}}, \"depth0_only\": {\"eval_loss_mean\": 0.9864, \"perplexity_mean\": 2.681, \"seeds\": {\"42\": {\"eval_loss\": 0.9865, \"ppl\": 2.6818}, \"123\": {\"eval_loss\": 0.9863, \"ppl\": 2.68}, \"456\": {\"eval_loss\": 0.9865, \"ppl\": 2.6817}}}}, \"ranking_by_ppl\": \"all(2.335) < size_matched(2.367) < depth01(2.387) ≈ binary_filtered(2.389) << depth0_only(2.681)\", \"seed_variance\": \"极小（同 variant 跨 seed ppl 差 <0.002）\"}, \"parent\": \"plan-004\"}, \"plan-003-olmo2ref\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T00:09:31.145Z\", \"updated_at\": \"2026-05-17T02:55:33.041Z\", \"conclusion\": \"success\", \"hypothesis\": \"跨家族参考模型验证（OLMo-2-1B）：用 OLMo-2-1B 作为参考模型提取 differential entropy 特征，验证 depth signal 的参考模型无关性——不同训练数据和架构的模型仍能检测相同的 depth dynamics\", \"parent\": \"plan-003\"}, \"plan-003-qwen06bref\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T00:09:31.649Z\", \"updated_at\": \"2026-05-17T02:55:27.742Z\", \"conclusion\": \"success\", \"hypothesis\": \"跨家族参考模型验证（Qwen3-0.6B）：用非 Pythia 家族的 Qwen3-0.6B 作为参考模型提取 differential entropy 特征，验证 depth signal 不依赖于参考模型与生成器的家族匹配\", \"parent\": \"plan-003\"}, \"plan-005-rewrite\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T03:28:47.421Z\", \"updated_at\": \"2026-05-17T02:55:19.976Z\", \"metrics\": {\"total_records\": 4827, \"unique_seeds\": 995, \"skipped\": 61, \"depth_distribution\": {\"0\": 995, \"1\": 995, \"2\": 959, \"3\": 944, \"4\": 934}, \"output_file\": \"/root/gen-depth-fingerprint/data/pythia-2.8b-inspired_rewriting/generations_shard0.jsonl\", \"file_size_mb\": 5.41, \"runtime_seconds\": 8584, \"speed_seeds_per_sec\": 0.12, \"depth_retention_d4_d0\": 0.939, \"vs_continuation\": \"retention 93.9% vs 83.1%, rewriting produces significantly more stable depth chains\"}, \"conclusion\": \"success\", \"hypothesis\": \"Inspired rewriting 链数据生成：rewriting prompt 要求模型受启发重写而非逐字续写，预期 depth retention 介于 continuation 和 elaboration 之间，因为重写保留主题但改变表达\", \"parent\": \"plan-005\"}, \"plan-005-elab\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T03:28:45.680Z\", \"updated_at\": \"2026-05-17T02:55:17.294Z\", \"conclusion\": \"success\", \"metrics\": {\"total_records\": 4946, \"unique_seeds\": 995, \"skipped\": 14, \"depth_distribution\": {\"0\": 995, \"1\": 995, \"2\": 989, \"3\": 986, \"4\": 981}, \"output_file\": \"/root/gen-depth-fingerprint/data/pythia-2.8b-elaboration/generations_shard0.jsonl\", \"file_size_mb\": 5.53, \"runtime_seconds\": 8960.2, \"depth_retention_d4_d0\": 0.986, \"logo_cv_f1\": {\"mean\": 0.73, \"std\": 0.011}, \"lopto_f1\": 0.7622, \"feature_drift_entropy_mean\": -0.4705, \"feature_drift_ttr\": -0.6413, \"feature_drift_hapax\": -0.8284, \"vs_continuation\": \"retention 98.6% vs 83.1%; CV F1 0.730 vs 0.781 — elaboration chains more stable but depth signal weaker within-type\", \"vs_rewriting\": \"retention 98.6% vs 93.9%; CV F1 0.730 vs 0.737 — similar discriminability, elaboration slightly lower\"}, \"hypothesis\": \"Elaboration 链数据生成：elaboration prompt 要求模型展开而非续写，预期 depth signal 因语义锚定更强而衰减更慢（retention > continuation 的 83%）\", \"parent\": \"plan-005\"}, \"plan-005-cont\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T03:28:43.383Z\", \"updated_at\": \"2026-05-17T02:55:14.334Z\", \"conclusion\": \"success\", \"metrics\": {\"total_records\": 4620, \"unique_seeds\": 995, \"skipped\": 168, \"depth_distribution\": {\"0\": 995, \"1\": 992, \"2\": 932, \"3\": 874, \"4\": 827}, \"output_file\": \"/root/gen-depth-fingerprint/data/pythia-2.8b-continuation/generations_shard0.jsonl\", \"file_size_mb\": 4.93, \"runtime_seconds\": 7760, \"speed_seeds_per_sec\": 0.13}, \"hypothesis\": \"Continuation 链数据生成：Pythia-2.8B 在 continuation prompt 下生成 depth 0-4 链，验证递归续写中 entropy/lexical 特征的单调漂移模式是否在 1000 seeds 规模下稳定复现\", \"parent\": \"plan-005\"}, \"plan-001-fix\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T18:50:14.620Z\", \"updated_at\": \"2026-05-17T02:55:10.600Z\", \"conclusion\": \"success\", \"metrics\": {\"full_macro_f1\": 0.8204, \"reference_only_f1\": 0.7187, \"surface_only_f1\": 0.7628, \"ref_vs_surf_bootstrap_ci\": \"[0.706,0.733] vs [0.747,0.774]\", \"h2_features\": \"entropy_mean, ttr, hapax_ratio\", \"h1_features\": \"tail_decay, entropy_std, entropy_max, entropy_min\", \"median_ppl_by_depth\": \"13.50, 4.96, 3.00, 2.07, 1.72\"}, \"hypothesis\": \"Feature ablation 修复验证：reference-only features (entropy系列+tail_decay) 独立于 surface features 仍能区分 depth，且两组特征的 bootstrap CI 不重叠，证明 differential response 和 lexical drift 是互补的独立信号源\", \"parent\": \"plan-001\"}, \"plan-010-robustness\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T22:09:57.049Z\", \"updated_at\": \"2026-05-16T22:11:48.657Z\", \"hypothesis\": \"Human edit robustness: depth fingerprint 在 5-20% random word replacement 下的 F1 退化测试，验证实际编辑场景（通常 < 5%）不影响检测\", \"conclusion\": \"success\", \"metrics\": {\"baseline_binary_f1\": 0.695, \"5pct_binary_f1\": 0.65, \"10pct_binary_f1\": 0.614, \"20pct_binary_f1\": 0.591, \"5pct_drop\": -0.046, \"10pct_drop\": -0.081, \"20pct_drop\": -0.104}}, \"review-exp-a-baseline-ensemble\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-15T12:22:30.747Z\", \"updated_at\": \"2026-05-15T12:22:33.270Z\", \"hypothesis\": \"审稿回应实验A：4-baseline ensemble + 统一超参对比，验证 7-feature vs 4-baseline vs 6-feature 在公平条件下的性能差异\"}, \"plan-005\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T03:24:02.435Z\", \"updated_at\": \"2026-05-15T06:20:59.698Z\", \"hypothesis\": \"Prompt type comparison: continuation vs elaboration vs inspired_rewriting 链的 depth signal 强度差异。Pythia-2.8B, 1000 seeds, 3 prompt types × 5 depths = 15K texts\", \"notes\": \"plan-005 完成。3 种 prompt type 全部成功。关键发现：(1) depth signal 跨 prompt type 存在（CV F1 0.73-0.78）；(2) LOPTO 泛化良好（avg 0.7525）；(3) surface features (ttr, hapax) 最稳健；(4) shape features 在非 continuation 中信号消失；(5) continuation 衰减最大（16.9%），elaboration 几乎无衰减（1.4%）。\", \"conclusion\": \"success\", \"metrics\": {\"cv_f1\": {\"continuation\": 0.7806, \"inspired_rewriting\": 0.7368, \"elaboration\": 0.73}, \"lopto_f1\": {\"held_out_cont\": 0.762, \"held_out_elab\": 0.7622, \"held_out_rewrite\": 0.7334, \"avg\": 0.7525}, \"depth_retention_d4_d0\": {\"continuation\": 0.831, \"inspired_rewriting\": 0.939, \"elaboration\": 0.986}, \"drift_hapax_ratio\": {\"continuation\": -0.74, \"elaboration\": -0.828, \"rewriting\": -0.8}, \"drift_ttr\": {\"continuation\": -0.607, \"elaboration\": -0.641, \"rewriting\": -0.618}, \"drift_entropy_mean\": {\"continuation\": -0.557, \"elaboration\": -0.471, \"rewriting\": -0.477}, \"spearman_ttr\": {\"continuation\": -0.629, \"elaboration\": -0.666, \"rewriting\": -0.659}, \"spearman_hapax\": {\"continuation\": -0.651, \"elaboration\": -0.674, \"rewriting\": -0.67}, \"spearman_entropy_mean\": {\"continuation\": -0.665, \"elaboration\": -0.583, \"rewriting\": -0.564}}}, \"plan-015\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T23:58:41.890Z\", \"updated_at\": \"2026-05-15T01:25:59.552Z\", \"hypothesis\": \"现有检测器 ordinal baseline：FastDetectGPT/LD-Score 等检测器的连续分数是否已提供 ordinal depth signal\", \"conclusion\": \"success\", \"metrics\": {\"seven_feature_logo_f1\": 0.798, \"seven_feature_ci\": [0.786, 0.799], \"avg_logprob_logo_f1\": 0.7653, \"avg_logprob_ci\": [0.616, 0.82], \"avg_logprob_spearman\": 0.7876, \"ld_score_logo_f1\": 0.7212, \"ld_score_ci\": [0.588, 0.77], \"ld_score_spearman\": 0.7943, \"ld_score_pre_fix\": 0.6854, \"fast_detect_gpt_logo_f1\": 0.6269, \"fast_detect_gpt_ci\": [0.511, 0.762], \"fast_detect_gpt_spearman\": 0.4325, \"binoculars_logo_f1\": 0.579, \"binoculars_ci\": [0.405, 0.664], \"binoculars_spearman\": 0.1989, \"binoculars_bug_confirmed\": true, \"binoculars_bug_fix\": \"denominator changed from CE(performer, obs_argmax) to CE(performer, shifted_ids)\", \"bootstrap_n\": 1000, \"bootstrap_delta_7feat_vs_avglogprob\": {\"delta\": 0.039, \"p\": 0, \"significant\": true}, \"bootstrap_delta_7feat_vs_fdgpt\": {\"delta\": 0.067, \"p\": 0, \"significant\": true}, \"best_single_detector\": \"Avg-LogProb (0.7653)\", \"seven_feature_advantage_pp\": 3.3}}, \"plan-004\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T00:22:57.901Z\", \"updated_at\": \"2026-05-15T01:02:50.582Z\", \"hypothesis\": \"Downstream utility: depth-stratified 数据对 OLMo-2-0425-1B CLM fine-tuning 的影响——depth0_only vs depth01 vs all vs size_matched vs binary_filtered，5 variants × 3 seeds\", \"notes\": \"FAILED: 根因是 OOM on GPU0（与 Qwen3-8B 共享 16.5GB），非单纯磁盘满。日志有 5 个 OOM Traceback（尝试分配 784MiB 但 GPU 仅剩 307MB）。磁盘满是次因（旧 checkpoints 22GB 占满根分区）。已由 plan-004-v2 在 cuda:1/2/3 重跑。\", \"conclusion\": \"failed\"}, \"plan-004-prep\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-14T23:58:42.465Z\", \"updated_at\": \"2026-05-15T00:19:49.846Z\", \"hypothesis\": \"Downstream utility 准备：depth-stratified 数据集 + OLMo-1B fine-tuning 脚本（不开跑，等 Director 确认）\", \"conclusion\": \"success\", \"metrics\": {\"model\": \"OLMo-2-0425-1B (1485M)\", \"datasets\": {\"depth0_only\": {\"train\": 797, \"test\": 3138}, \"depth01\": {\"train\": 3951, \"test\": 3138}, \"all\": {\"train\": 12299, \"test\": 3138}, \"size_matched\": {\"train\": 3951, \"test\": 3138}, \"binary_filtered\": {\"train\": 3951, \"test\": 3138}}, \"dry_run_loss\": 2.18, \"script\": \"finetune_downstream.py\"}}, \"plan-001-restore\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-14T19:14:00.170Z\", \"updated_at\": \"2026-05-15T00:19:35.359Z\", \"notes\": \"历史遗留条目，实际已由 plan-001-fix 完成覆盖。可忽略。\"}, \"mvp-001-gen-s0\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-14T17:23:13.139Z\", \"updated_at\": \"2026-05-15T00:19:34.474Z\", \"notes\": \"历史遗留条目，实际已由 mvp-001 完成覆盖。可忽略。\"}, \"plan-003\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T23:58:40.949Z\", \"updated_at\": \"2026-05-15T00:09:28.999Z\", \"hypothesis\": \"跨家族参考模型伪证化：用 OLMo-2-1B 和 Qwen3-0.6B 作参考模型提取特征，验证 differential depth response 非 Pythia 特异\", \"conclusion\": \"success\", \"metrics\": {\"logo_f1_pythia_ref\": 0.8034, \"logo_f1_olmo_ref\": 0.8072, \"logo_f1_qwen_ref\": 0.8158, \"entropy_drift_all_refs_negative\": true, \"olmo_ref_drift_range\": [-0.608, -0.9089], \"qwen_ref_drift_range\": [-0.9557, -1.3458], \"pythia_ref_drift_range\": [-1.1872, -1.4017], \"dual_dynamics_is_pythia_artifact\": false}}, \"plan-013\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T23:33:25.590Z\", \"updated_at\": \"2026-05-14T23:53:38.901Z\", \"hypothesis\": \"文本长度混淆控制：深度特征的区分力是否独立于文本长度变化（长度归一化后趋势是否保持）\", \"conclusion\": \"success\", \"metrics\": {\"spearman_rho_range\": \"[-0.066, +0.134]\", \"length_depth_correlation\": \"weak (|ρ|<0.14)\", \"normalized_ttr_trend_preserved\": true, \"normalized_hapax_trend_preserved\": true, \"normalized_rho_stronger\": true, \"length_matched_f1_delta\": \"+0.041\", \"length_is_confound\": false, \"dropout_short_text_bias\": true}}, \"plan-002\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T20:08:55.258Z\", \"updated_at\": \"2026-05-14T23:19:42.066Z\", \"hypothesis\": \"跨模型泛化：Pythia-410M 参考模型下的深度特征能否区分不同架构/规模生成器（Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B）的 continuation 链\", \"conclusion\": \"success\", \"metrics\": {\"total_records\": 18423, \"models\": 4, \"pythia_1b\": {\"records\": 4555, \"seeds\": 995, \"file\": \"data/pythia-1b/generations.jsonl\"}, \"olmo_2_1b\": {\"records\": 4713, \"seeds\": 995, \"file\": \"data/olmo-2-1b/generations.jsonl\"}, \"qwen3_0_6b\": {\"records\": 4538, \"seeds\": 996, \"depth_dist\": {\"gen0\": 996, \"gen1\": 986, \"gen2\": 938, \"gen3\": 840, \"gen4\": 778}, \"file\": \"data/qwen3-0.6b/generations.jsonl\"}, \"qwen3_1_7b\": {\"records\": 4617, \"seeds\": 996, \"depth_dist\": {\"gen0\": 996, \"gen1\": 983, \"gen2\": 941, \"gen3\": 875, \"gen4\": 822}, \"file\": \"data/qwen3-1.7b/generations.jsonl\"}}}, \"plan-002-qwen17b-retry-s1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T21:25:19.756Z\", \"updated_at\": \"2026-05-14T22:24:07.274Z\", \"conclusion\": \"failed\", \"notes\": \"r2 进程 PID 120694 存活，resume 从 seed 143 继续。之前 failed 标记是对旧 retry 进程的判断，r2 是新提交。ETA ~07:30 UTC\"}, \"plan-002-qwen17b-retry-s0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T21:25:18.048Z\", \"updated_at\": \"2026-05-14T22:24:06.388Z\", \"conclusion\": \"failed\", \"notes\": \"r2 进程 PID 120617 存活，resume 从 seed 154 继续。之前 failed 标记是对旧 retry 进程的判断，r2 是新提交。ETA ~07:20 UTC\"}, \"plan-002-qwen06b-s1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T21:25:23.092Z\", \"updated_at\": \"2026-05-14T22:07:37.394Z\", \"conclusion\": \"failed\", \"notes\": \"失败原因: 进程在 218/498 seeds (44%) 正常运行中被外部终止，日志无任何 Python/CUDA 错误。与 s0 和 Qwen3-1.7B 同一 tmux session 死亡模式。系统性 tmux 问题。\"}, \"plan-002-qwen06b-s0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T21:25:21.697Z\", \"updated_at\": \"2026-05-14T22:07:33.758Z\", \"conclusion\": \"failed\", \"notes\": \"失败原因: 进程在 226/498 seeds (45%) 正常运行中被外部终止，日志无任何 Python/CUDA 错误。与 Qwen3-1.7B 同一 tmux session 死亡模式。系统性 tmux 问题，非代码问题。诊断 Worker worker_diagnose_tmux-death-root-cause_20260514T220718 正在深查。\"}, \"plan-002-qwen17b-s1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T20:53:21.708Z\", \"updated_at\": \"2026-05-14T21:53:51.130Z\", \"conclusion\": \"failed\", \"notes\": \"重复提交（与 plan-002-qwen3-1_7b-s1 冲突），争抢 cuda:1 + 写同一输出文件。已 kill。\"}, \"plan-002-qwen17b-s0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T20:53:19.356Z\", \"updated_at\": \"2026-05-14T21:53:49.671Z\", \"conclusion\": \"failed\", \"notes\": \"重复提交（与 plan-002-qwen3-1_7b-s0 冲突），争抢 cuda:0 + 写同一输出文件。已 kill。\"}, \"plan-002-qwen3-1_7b-s0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T20:52:58.460Z\", \"updated_at\": \"2026-05-14T21:53:48.299Z\", \"conclusion\": \"failed\", \"notes\": \"失败原因: SIGHUP (EXIT_CODE=129)，运行 ~21min 后被外部终止。日志无 Python/CUDA 错误，进度正常（104/498 seeds）。同时 s1 也被 SIGHUP。OLMo-2 (cuda:2/3) 不受影响 → 非服务器重启。诊断 Worker worker_diagnose_plan-002-qwen3-1_7b_20260514T211526 正在排查。\"}, \"plan-002-qwen3-1_7b-s1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T20:53:00.298Z\", \"updated_at\": \"2026-05-14T21:33:26.442Z\", \"conclusion\": \"killed\", \"notes\": \"失败原因: SIGHUP (EXIT_CODE=129)，运行 ~21min 后被外部终止。日志无 Python/CUDA 错误，进度正常（95/498 seeds）。与 s0 同时被终止。诊断 Worker 正在排查。\"}, \"plan-001\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T18:25:29.824Z\", \"updated_at\": \"2026-05-14T19:34:17.597Z\", \"hypothesis\": \"Feature ablation: 模型级特征（entropy系列+tail_decay）独立于表面特征仍能区分生成深度；H1/H2趋势分析确认特征随depth的变化模式；perplexity随depth显著变化\", \"conclusion\": \"success\", \"metrics\": {\"note\": \"initial_run_partial_issues_fixed_in_plan-001-fix\", \"ablation_full_macro_f1\": 0.82, \"ablation_surface_only_f1\": 0.76, \"ablation_reference_only_f1\": 0.72}}, \"mvp-001\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T16:17:16.218Z\", \"updated_at\": \"2026-05-14T18:08:20.940Z\", \"hypothesis\": \"Pythia-410M 参考模型的分布特征（entropy stats, tail-decay, TTR, hapax）能区分 Pythia-2.8B continuation 链的 gen-0/gen-1/gen-2+，3-class macro-F1 ≥ 0.45\", \"conclusion\": \"success\", \"metrics\": {\"macro_f1\": 0.8408, \"binary_f1_gen0_vs_gen2plus\": 0.8653, \"cv_macro_f1\": 0.806, \"cv_std\": 0.013, \"gen0_f1\": 0.9517, \"gen1_f1\": 0.7759, \"gen2plus_f1\": 0.7947, \"total_records\": 4609, \"seeds_used\": 995, \"skipped\": 173}}, \"mvp-001-gen-s3\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-14T17:23:17.526Z\", \"updated_at\": \"2026-05-14T17:25:51.261Z\", \"conclusion\": \"failed\", \"notes\": \"失败原因: CUDA error: invalid device ordinal — submit_training_job 注入 CUDA_VISIBLE_DEVICES 后脚本只能看到 cuda:0，但命令用了 --device cuda:3 | 修复: --device 应始终为 cuda:0\"}, \"mvp-001-gen-s2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-14T17:23:15.855Z\", \"updated_at\": \"2026-05-14T17:25:50.275Z\", \"conclusion\": \"failed\", \"notes\": \"失败原因: CUDA error: invalid device ordinal — submit_training_job 注入 CUDA_VISIBLE_DEVICES 后脚本只能看到 cuda:0，但命令用了 --device cuda:2 | 修复: --device 应始终为 cuda:0\"}, \"mvp-001-gen-s1\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-14T17:23:14.464Z\", \"updated_at\": \"2026-05-14T17:25:48.863Z\", \"conclusion\": \"failed\", \"notes\": \"失败原因: CUDA error: invalid device ordinal — submit_training_job 注入 CUDA_VISIBLE_DEVICES 后脚本只能看到 cuda:0，但命令用了 --device cuda:1 | 修复: --device 应始终为 cuda:0\"}}, \"count\": 56, \"total\": 56, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1594}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "036343ae-8380-4087-9a82-8be981fc7a27",
  "isSidechain": false,
  "promptId": "0ff41a4b-161b-457c-85f3-287146dda57a",
  "type": "user",
  "uuid": "98127156-d719-4295-9bf7-b40c4bc571e0",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"exp_054_instruct_llama3_2_3b\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-18T03:06:07.150Z\\\", \\\"updated_at\\\": \\\"2026-05-18T07:58:31.553Z\\\", \\\"hypothesis\\\": \\\"Instruct-tuned Llama-3.2-3B-Instruct shows degraded depth signal vs base Llama-3.2-3B (F1=0.697), quantifying instruction-tuning's impact on DDR\\\", \\\"notes\\\": \\\"生成 59% (292/497 seeds) 后 Worker 与服务器断连。脚本有 resume 支持。模型已下载到 /root/autodl-tmp/models/Llama-3.2-3B-Instruct-ms/。Eval 脚本已准备: eval_exp054_instruct_llama.py\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"instruct_binary_f1\\\": 0.8381, \\\"instruct_binary_ci\\\": [0.828, 0.847], \\\"instruct_3class_f1\\\": 0.5437, \\\"instruct_3class_ci\\\": [0.53, 0.558], \\\"base_binary_f1\\\": 0.8488, \\\"base_3class_f1\\\": 0.7424, \\\"rho_instruct_entropy_mean\\\": 0.2299, \\\"rho_instruct_entropy_std\\\": 0.2623, \\\"rho_instruct_entropy_min\\\": -0.0027, \\\"rho_instruct_entropy_max\\\": 0.2036, \\\"rho_instruct_tail_decay\\\": 0.1198, \\\"rho_instruct_ttr\\\": -0.1411, \\\"rho_instruct_hapax_ratio\\\": -0.1157, \\\"rho_base_entropy_mean\\\": -0.627, \\\"rho_base_ttr\\\": -0.6856, \\\"rho_base_hapax_ratio\\\": -0.6975, \\\"direction_reversals\\\": 3, \\\"reversed_features\\\": [\\\"entropy_mean\\\", \\\"entropy_std\\\", \\\"tail_decay\\\"], \\\"data_count\\\": 4974}}, \\\"exp_050_temp_curve_t09\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-17T22:15:11.626Z\\\", \\\"updated_at\\\": \\\"2026-05-18T06:09:24.876Z\\\", \\\"hypothesis\\\": \\\"DDR signal at t=0.9 degrades relative to t=0.7 but less severely than t=1.0, establishing monotonic temperature sensitivity\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"Registry 误标 failed（startup recovery 机制）。实际 tmux tc_fix 仍在运行中。Phase 2 (Pythia-2.8B t=0.9) 39% 完成 (392/995 seeds)，预计 ~76min。Phase 3 (Qwen3-1.7B t=0.9) 待执行。总计 ~5-6h 完成。\\\", \\\"metrics\\\": {\\\"records\\\": 4536, \\\"model\\\": \\\"pythia-2.8b\\\", \\\"temperature\\\": 0.9, \\\"top_p\\\": 0.9, \\\"within_cv_binary_f1\\\": 0.5821, \\\"within_cv_binary_ci\\\": [0.5655, 0.5985], \\\"logo_binary_f1\\\": 0.4804, \\\"logo_binary_ci\\\": [0.4645, 0.4976], \\\"entropy_mean_rho\\\": -0.3016, \\\"delta_vs_t07_cv\\\": -0.157, \\\"delta_vs_t07_logo\\\": -0.259}}, \\\"exp_049_temp_curve_t05\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-17T22:15:10.383Z\\\", \\\"updated_at\\\": \\\"2026-05-18T06:09:22.443Z\\\", \\\"hypothesis\\\": \\\"DDR signal at t=0.5 should be stronger than t=0.7 (less randomness preserves more distributional structure)\\\", \\\"conclusion\\\": \\\"success\\\", \\\"notes\\\": \\\"Registry 误标 failed（startup recovery 机制）。实际 tmux tc_fix 仍在运行中。Phase 1 (t=0.5 generation) 已完成 4708 records。等待 phase 2+3 完成后统一提取特征和评估。\\\", \\\"metrics\\\": {\\\"records\\\": 4708, \\\"skipped\\\": 113, \\\"seeds\\\": 995, \\\"model\\\": \\\"pythia-2.8b\\\", \\\"temperature\\\": 0.5, \\\"top_p\\\": 0.9, \\\"within_cv_binary_f1\\\": 0.8432, \\\"within_cv_binary_ci\\\": [0.8301, 0.8558], \\\"logo_binary_f1\\\": 0.8136, \\\"logo_binary_ci\\\": [0.7984, 0.8282], \\\"entropy_mean_rho\\\": -0.5844}}, \\\"exp_053_instruct_olmo2_1b\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-18T03:06:06.142Z\\\", \\\"updated_at\\\": \\\"2026-05-18T03:46:16.047Z\\\", \\\"hypothesis\\\": \\\"Instruct-tuned OLMo-2-1B-Instruct shows degraded depth signal vs base OLMo-2-1B (F1=0.695), quantifying instruction-tuning's impact on DDR\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"within_binary_f1\\\": 0.8131, \\\"within_binary_ci\\\": [0.8012, 0.8251], \\\"within_3class_f1\\\": 0.5748, \\\"within_3class_ci\\\": [0.5605, 0.5897], \\\"base_binary_f1\\\": 0.8454, \\\"base_3class_f1\\\": 0.7538, \\\"gen1_f1_instruct\\\": 0.256, \\\"gen1_f1_base\\\": 0.523, \\\"delta_within_binary\\\": -0.032, \\\"delta_within_3class\\\": -0.179, \\\"spearman_instruct\\\": {\\\"entropy_mean\\\": 0.482, \\\"entropy_std\\\": 0.296, \\\"entropy_min\\\": 0.08, \\\"entropy_max\\\": 0.306, \\\"tail_decay\\\": 0.228, \\\"ttr\\\": 0.006, \\\"hapax_ratio\\\": 0.025}, \\\"spearman_base\\\": {\\\"entropy_mean\\\": -0.639, \\\"entropy_std\\\": -0.296, \\\"entropy_min\\\": -0.387, \\\"entropy_max\\\": 0.067, \\\"tail_decay\\\": -0.141, \\\"ttr\\\": -0.7, \\\"hapax_ratio\\\": -0.712}, \\\"features_reversed\\\": \\\"6/7\\\", \\\"model_used\\\": \\\"allenai/OLMo-2-0425-1B-Instruct\\\"}}, \\\"exp_052_instruct_qwen3_1_7b\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-18T03:06:04.788Z\\\", \\\"updated_at\\\": \\\"2026-05-18T03:26:14.267Z\\\", \\\"hypothesis\\\": \\\"Instruct-tuned Qwen3-1.7B (chat template, thinking=off) shows degraded depth signal vs base Qwen3-1.7B (F1=0.709), quantifying instruction-tuning's impact on DDR\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"within_binary_f1\\\": 0.8753, \\\"within_binary_ci\\\": [0.8667, 0.8837], \\\"within_3class_f1\\\": 0.7324, \\\"within_3class_ci\\\": [0.7195, 0.745], \\\"base_binary_f1\\\": 0.8614, \\\"base_3class_f1\\\": 0.769, \\\"logo_instruct_binary\\\": 0.658, \\\"logo_instruct_3class\\\": 0.543, \\\"logo_base_binary\\\": 0.821, \\\"logo_base_3class\\\": 0.802, \\\"gen1_f1_instruct\\\": 0.438, \\\"gen1_f1_base\\\": 0.579, \\\"spearman_direction\\\": \\\"reversed (instruct ρ>0, base ρ<0)\\\", \\\"delta_within_binary\\\": 0.014, \\\"delta_within_3class\\\": -0.037, \\\"delta_logo_binary\\\": -0.163}}, \\\"exp_051_independent_seed\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-17T22:38:00.466Z\\\", \\\"updated_at\\\": \\\"2026-05-18T02:01:42.126Z\\\", \\\"hypothesis\\\": \\\"Cross-generator depth classification with non-overlapping seeds achieves comparable F1 to shared-seed LOGO, ruling out topic fingerprint leakage\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"pythia_to_olmo_binary_f1\\\": 0.6945, \\\"pythia_to_olmo_ci\\\": [0.6727, 0.7167], \\\"olmo_to_pythia_binary_f1\\\": 0.666, \\\"olmo_to_pythia_ci\\\": [0.6429, 0.6893], \\\"avg_binary_f1\\\": 0.6803, \\\"shared_seed_logo_ref\\\": 0.694, \\\"delta_vs_shared\\\": -0.014}}, \\\"exp_048_cross_temp_transfer\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-17T12:52:44.889Z\\\", \\\"updated_at\\\": \\\"2026-05-17T17:07:19.391Z\\\", \\\"hypothesis\\\": \\\"Cross-temperature transfer: XGBoost 7-feature classifier trained at one sampling temperature (t=0.7 or t=1.0) maintains depth discrimination when tested at a different temperature, demonstrating deployment robustness to unknown decoding parameters\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"6gen_logo\\\": {\\\"within_0.7_binary\\\": 0.9471, \\\"within_0.7_3class\\\": 0.7888, \\\"cross_0.7to1.0_binary\\\": 0.9001, \\\"cross_0.7to1.0_3class\\\": 0.7225, \\\"within_1.0_binary\\\": 0.9107, \\\"within_1.0_3class\\\": 0.7257, \\\"cross_1.0to0.7_binary\\\": 0.9581, \\\"cross_1.0to0.7_3class\\\": 0.7913, \\\"caveat\\\": \\\"Only Qwen3-1.7B differs between conditions; 5/6 generators share data\\\"}, \\\"qwen_only\\\": {\\\"within_0.7_binary\\\": 0.9262, \\\"within_0.7_binary_ci\\\": [0.916, 0.935], \\\"within_0.7_3class\\\": 0.769, \\\"within_0.7_3class_ci\\\": [0.756, 0.781], \\\"cross_0.7to1.0_binary\\\": 0.7574, \\\"cross_0.7to1.0_binary_ci\\\": [0.745, 0.77], \\\"cross_0.7to1.0_3class\\\": 0.4581, \\\"cross_0.7to1.0_3class_ci\\\": [0.445, 0.472], \\\"within_1.0_binary\\\": 0.8248, \\\"within_1.0_binary_ci\\\": [0.81, 0.838], \\\"within_1.0_3class\\\": 0.5738, \\\"within_1.0_3class_ci\\\": [0.56, 0.588], \\\"cross_1.0to0.7_binary\\\": 0.9443, \\\"cross_1.0to0.7_binary_ci\\\": [0.936, 0.953], \\\"cross_1.0to0.7_3class\\\": 0.6014, \\\"cross_1.0to0.7_3class_ci\\\": [0.593, 0.611], \\\"delta_0.7train_binary_pp\\\": -16.9, \\\"delta_0.7train_3class_pp\\\": -31.1, \\\"delta_1.0train_binary_pp\\\": 12, \\\"delta_1.0train_3class_pp\\\": 2.8, \\\"asymmetric_transfer\\\": true}}, \\\"parent\\\": \\\"exp_047_multi_domain_t07\\\"}, \\\"exp_047_multi_domain_t07\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-17T05:51:25.881Z\\\", \\\"updated_at\\\": \\\"2026-05-17T07:22:04.483Z\\\", \\\"hypothesis\\\": \\\"Depth fingerprint generalizes across domains (News, Academic, Code) under standard decoding (t=0.7, top_p=0.9) matching main experiment params, eliminating the temperature confound from t=1.0 results and producing directly comparable domain generalization numbers\\\", \\\"parent\\\": \\\"exp_043_multi_domain_seeds\\\", \\\"metrics\\\": {\\\"news_binary_f1\\\": 0.7119, \\\"news_binary_ci\\\": [0.6898, 0.7332], \\\"news_3class_f1\\\": 0.7149, \\\"academic_binary_f1\\\": 0.6279, \\\"academic_binary_ci\\\": [0.6027, 0.6515], \\\"academic_3class_f1\\\": 0.6564, \\\"code_binary_f1\\\": 0.6872, \\\"code_binary_ci\\\": [0.6641, 0.71], \\\"code_3class_f1\\\": 0.6729, \\\"overall_binary_f1\\\": 0.6757, \\\"overall_3class_f1\\\": 0.6814, \\\"delta_vs_t10_news\\\": -0.034, \\\"delta_vs_t10_academic\\\": -0.1107, \\\"delta_vs_t10_code\\\": -0.0663}, \\\"conclusion\\\": \\\"success\\\"}, \\\"multi_domain_t07\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-17T05:54:55.365Z\\\", \\\"updated_at\\\": \\\"2026-05-17T05:54:55.365Z\\\"}, \\\"multi-domain-seeds\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-17T03:38:54.349Z\\\", \\\"updated_at\\\": \\\"2026-05-17T05:05:40.584Z\\\", \\\"hypothesis\\\": \\\"Domain independence: depth fingerprint 的 differential depth response 不依赖 seed domain——在 News/Academic/Code 三个非 Wikipedia 域上，7-feature ensemble 的 binary F1 与 Wikipedia baseline 差异 <10pp，证明 DDR 是生成过程的固有特性而非特定域文本属性的 artifact\\\", \\\"metrics\\\": {\\\"news_binary_f1\\\": 0.7459, \\\"news_binary_ci\\\": [0.726, 0.764], \\\"news_multiclass_f1\\\": 0.6516, \\\"academic_binary_f1\\\": 0.7386, \\\"academic_binary_ci\\\": [0.72, 0.757], \\\"academic_multiclass_f1\\\": 0.6223, \\\"code_binary_f1\\\": 0.7535, \\\"code_binary_ci\\\": [0.737, 0.77], \\\"code_multiclass_f1\\\": 0.6344, \\\"wikipedia_baseline_binary_f1\\\": 0.8148, \\\"wikipedia_baseline_multiclass_f1\\\": 0.8632, \\\"max_gap_vs_wiki_pp\\\": 7.62, \\\"worst_domain\\\": \\\"academic\\\", \\\"best_domain\\\": \\\"code\\\", \\\"conclusion_label\\\": \\\"domain_independent\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"plan-008-seed-stratification\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-17T00:21:12.380Z\\\", \\\"updated_at\\\": \\\"2026-05-17T02:56:26.724Z\\\", \\\"hypothesis\\\": \\\"Seed complexity independence: depth fingerprint 的判别能力不依赖 seed 文本的词汇复杂度（按 gen-0 TTR terciles 分层验证）\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"low_complexity_binary\\\": 0.685, \\\"medium_binary\\\": 0.695, \\\"high_complexity_binary\\\": 0.695, \\\"low_complexity_multi\\\": 0.772, \\\"medium_multi\\\": 0.778, \\\"high_complexity_multi\\\": 0.779, \\\"max_diff_binary_pp\\\": 1.06, \\\"max_diff_multiclass_pp\\\": 0.68, \\\"conclusion_label\\\": \\\"seed_independent\\\"}, \\\"parent\\\": \\\"plan-010-robustness\\\"}, \\\"plan-002-qwen06b-r2-s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T22:35:11.142Z\\\", \\\"updated_at\\\": \\\"2026-05-17T02:56:25.805Z\\\", \\\"hypothesis\\\": \\\"跨家族泛化数据生成（Qwen3-0.6B shard1）：Qwen3-0.6B continuation 链第二分片，补全 ~995 seeds 覆盖\\\", \\\"notes\\\": \\\"Orphan 进程 PID 118126 存活，shard1 进度 340/500 seeds (68%)，当前 1542 行，预计 ~23:00 UTC 完成。GPU cuda:3 利用率 33%。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"records\\\": 2268, \\\"seeds\\\": 498, \\\"depth_dist\\\": {\\\"0\\\": 498, \\\"1\\\": 493, \\\"2\\\": 470, \\\"3\\\": 417, \\\"4\\\": 390}, \\\"file\\\": \\\"generations_shard1.jsonl\\\"}, \\\"parent\\\": \\\"plan-002\\\"}, \\\"plan-002-qwen06b-r2-s0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T22:35:10.950Z\\\", \\\"updated_at\\\": \\\"2026-05-17T02:56:23.413Z\\\", \\\"hypothesis\\\": \\\"跨家族泛化数据生成（Qwen3-0.6B shard0）：最小参数量(0.6B) Qwen 模型的 continuation 链，验证 depth signal 在极小模型中是否仍存在（小模型可能因容量不足而无法维持深层生成的分布稳定性）\\\", \\\"notes\\\": \\\"Orphan 进程 PID 117855 存活，shard0 进度 350/500 seeds (70%)，当前 1593 行，预计 ~23:00 UTC 完成。GPU cuda:2 利用率 34%。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"records\\\": 2270, \\\"seeds\\\": 498, \\\"depth_dist\\\": {\\\"0\\\": 498, \\\"1\\\": 493, \\\"2\\\": 468, \\\"3\\\": 423, \\\"4\\\": 388}, \\\"file\\\": \\\"generations_shard0.jsonl\\\"}, \\\"parent\\\": \\\"plan-002\\\"}, \\\"review-exp-c-overall-ci\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-15T12:22:37.037Z\\\", \\\"updated_at\\\": \\\"2026-05-17T02:56:15.141Z\\\", \\\"hypothesis\\\": \\\"6-generator LOGO 的 overall bootstrap CI 窄且不跨越 chance level，entropy_max/entropy_min 的个体 Spearman ρ 验证其对 depth 的单调贡献方向（max 正相关因高 depth 分布更尖，min 负相关因低概率 tail 被压缩）\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_logo_f1\\\": 0.7879, \\\"overall_ci95\\\": [0.783, 0.7929], \\\"spearman_entropy_max\\\": 0.0503, \\\"spearman_entropy_min\\\": -0.4061, \\\"spearman_hapax\\\": -0.6467, \\\"spearman_ttr\\\": -0.6302, \\\"spearman_entropy_mean\\\": -0.6098, \\\"spearman_entropy_std\\\": -0.1996, \\\"spearman_tail_decay\\\": -0.0403}}, \\\"review-exp-b-topic-drift\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-15T12:22:34.096Z\\\", \\\"updated_at\\\": \\\"2026-05-17T02:56:11.446Z\\\", \\\"hypothesis\\\": \\\"Depth fingerprint 不仅仅捕捉 topic shift：语义漂移(embedding cosine similarity)与 depth 相关性弱(|ρ|<0.3)，而 entropy/lexical features 与 depth 的相关性强(|ρ|>0.5)，证明 depth signal 来自生成过程的统计特性而非内容偏移\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"semantic_similarity_by_transition\\\": {\\\"0_to_1\\\": {\\\"mean\\\": 0.622, \\\"std\\\": 0.1647}, \\\"1_to_2\\\": {\\\"mean\\\": 0.6829, \\\"std\\\": 0.1837}, \\\"2_to_3\\\": {\\\"mean\\\": 0.801, \\\"std\\\": 0.2012}, \\\"3_to_4\\\": {\\\"mean\\\": 0.8587, \\\"std\\\": 0.1895}}, \\\"prompt_type_avg_sim\\\": {\\\"continuation\\\": 0.7168, \\\"elaboration\\\": 0.8093, \\\"inspired_rewriting\\\": 0.808}, \\\"shape_feature_correlations\\\": {\\\"entropy_std_rho\\\": -0.1639, \\\"tail_decay_rho\\\": 0.0675}, \\\"drifting_feature_correlations\\\": {\\\"hapax_ratio_rho\\\": -0.1242, \\\"ttr_rho\\\": -0.1784, \\\"entropy_mean_rho\\\": -0.2859}}}, \\\"plan-014\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-15T00:12:01.909Z\\\", \\\"updated_at\\\": \\\"2026-05-17T02:56:07.395Z\\\", \\\"hypothesis\\\": \\\"大模型规模泛化：Qwen3-8B (7B+参数) 的 continuation 链是否展现同样的 entropy 收敛和 lexical drift，验证 depth dynamics 不因模型容量增大而消失（更大模型可能有更强的分布记忆导致 depth signal 衰减）\\\", \\\"notes\\\": \\\"2026-05-15 04:25: ✅ 完整数据重算完成 (4409 records, 977 seeds)。与 82% 快照差异在统计噪声范围内：LOGO +0.0011, qwen8b held-out -0.0037。最终数字已确认，可用于论文。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"total_records\\\": 4497, \\\"unique_seeds\\\": 995, \\\"depth_dist\\\": {\\\"0\\\": 995, \\\"1\\\": 979, \\\"2\\\": 937, \\\"3\\\": 831, \\\"4\\\": 755}, \\\"logo_6gen_avg_f1\\\": 0.7893, \\\"logo_per_generator\\\": {\\\"olmo-2-1b\\\": 0.7635, \\\"pythia-1b\\\": 0.8562, \\\"pythia-2.8b\\\": 0.8041, \\\"qwen3-0.6b\\\": 0.8243, \\\"qwen3-1.7b\\\": 0.8046, \\\"qwen3-8b\\\": 0.6832}, \\\"logo_qwen3_8b_held_out_f1\\\": 0.6832, \\\"logo_5gen_baseline_f1\\\": 0.8, \\\"spearman\\\": {\\\"hapax_ratio\\\": -0.5578, \\\"ttr\\\": -0.5419, \\\"entropy_mean\\\": -0.4754, \\\"entropy_min\\\": -0.3029, \\\"entropy_max\\\": 0.0946, \\\"tail_decay\\\": -0.0894, \\\"entropy_std\\\": -0.0755}, \\\"feature_importance\\\": {\\\"hapax_ratio\\\": 0.269, \\\"entropy_mean\\\": 0.1637, \\\"ttr\\\": 0.159, \\\"entropy_max\\\": 0.0634, \\\"entropy_std\\\": 0.0463, \\\"entropy_min\\\": 0.0153, \\\"tail_decay\\\": 0.0123}, \\\"revalidation_v2_vs_snapshot\\\": \\\"LOGO +0.0007 (0.7886→0.7893), qwen8b -0.0054 (0.6886→0.6832)\\\", \\\"revalidation_v2_conclusion\\\": \\\"complete_data_validates_snapshot_robustness\\\"}, \\\"parent\\\": \\\"plan-002\\\"}, \\\"plan-002-qwen17b-r2-s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T21:58:14.195Z\\\", \\\"updated_at\\\": \\\"2026-05-17T02:56:03.576Z\\\", \\\"notes\\\": \\\"Orphan 进程 PID 120694 存活，shard1 进度 295/500 seeds (59%)，预计 ~22:55 UTC 完成。GPU cuda:1 利用率 44%。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"records\\\": 2326, \\\"seeds\\\": 498, \\\"depth_dist\\\": {\\\"0\\\": 498, \\\"1\\\": 491, \\\"2\\\": 473, \\\"3\\\": 440, \\\"4\\\": 424}, \\\"skipped\\\": 53, \\\"duration_s\\\": 4228, \\\"file\\\": \\\"generations_shard1.jsonl\\\"}, \\\"hypothesis\\\": \\\"跨家族泛化数据生成（Qwen3-1.7B shard1）：Qwen3-1.7B continuation 链第二分片，补全 ~995 seeds 覆盖\\\", \\\"parent\\\": \\\"plan-002\\\"}, \\\"plan-002-qwen17b-r2-s0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T21:58:12.310Z\\\", \\\"updated_at\\\": \\\"2026-05-17T02:56:01.158Z\\\", \\\"notes\\\": \\\"Orphan 进程 PID 120617 存活，shard0 进度 289/500 seeds (58%)，预计 ~22:55 UTC 完成。GPU cuda:0 利用率 40%。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"records\\\": 2291, \\\"seeds\\\": 498, \\\"depth_dist\\\": {\\\"0\\\": 498, \\\"1\\\": 492, \\\"2\\\": 468, \\\"3\\\": 435, \\\"4\\\": 398}, \\\"skipped\\\": 199, \\\"duration_s\\\": 4548.2, \\\"file_size_mb\\\": 2.5, \\\"file\\\": \\\"generations_shard0.jsonl\\\"}, \\\"hypothesis\\\": \\\"跨家族泛化数据生成（Qwen3-1.7B shard0）：Qwen 家族 1.7B 模型的 continuation 链 depth dynamics，验证中等规模非 Pythia 模型也产生可检测的 depth signal\\\", \\\"parent\\\": \\\"plan-002\\\"}, \\\"plan-002-olmo2-s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T20:09:46.880Z\\\", \\\"updated_at\\\": \\\"2026-05-17T02:55:54.134Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"records\\\": 2334, \\\"seeds\\\": 498, \\\"skipped\\\": 70, \\\"wall_time_s\\\": 4081.2, \\\"depth_dist\\\": {\\\"gen0\\\": 498, \\\"gen1\\\": 494, \\\"gen2\\\": 470, \\\"gen3\\\": 444, \\\"gen4\\\": 428}, \\\"file\\\": \\\"generations_shard1.jsonl\\\", \\\"file_size_mb\\\": 2.57}, \\\"hypothesis\\\": \\\"跨家族泛化数据生成（OLMo-2-1B shard1）：OLMo-2-1B continuation 链第二分片，补全 ~995 seeds 覆盖\\\", \\\"parent\\\": \\\"plan-002\\\"}, \\\"plan-002-olmo2-s0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T20:09:45.173Z\\\", \\\"updated_at\\\": \\\"2026-05-17T02:55:52.145Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"records\\\": 2379, \\\"seeds\\\": 497, \\\"skipped\\\": 47, \\\"wall_time_s\\\": 3885.2, \\\"depth_dist\\\": {\\\"gen0\\\": 497, \\\"gen1\\\": 494, \\\"gen2\\\": 477, \\\"gen3\\\": 461, \\\"gen4\\\": 450}, \\\"file\\\": \\\"generations_shard0.jsonl\\\", \\\"file_size_mb\\\": 2.68}, \\\"hypothesis\\\": \\\"跨家族泛化数据生成（OLMo-2-1B shard0）：非 Pythia 架构(OLMo)的 continuation 链中 depth signal 是否存在，验证 depth dynamics 跨训练数据和架构的普遍性\\\", \\\"parent\\\": \\\"plan-002\\\"}, \\\"plan-002-pythia1b-s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T20:09:42.815Z\\\", \\\"updated_at\\\": \\\"2026-05-17T02:55:49.321Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"records\\\": 2269, \\\"seeds\\\": 498, \\\"skipped\\\": 100, \\\"wall_time_s\\\": 2247.6, \\\"depth_dist\\\": {\\\"gen0\\\": 498, \\\"gen1\\\": 496, \\\"gen2\\\": 455, \\\"gen3\\\": 422, \\\"gen4\\\": 398}, \\\"file\\\": \\\"data/pythia-1b/generations_shard1.jsonl\\\", \\\"file_size_mb\\\": 2.44}, \\\"hypothesis\\\": \\\"跨模型泛化数据生成（Pythia-1B shard1）：Pythia-1B continuation 链第二分片，与 shard0 合并后提供完整 ~995 seeds 的 depth 数据\\\", \\\"parent\\\": \\\"plan-002\\\"}, \\\"plan-002-pythia1b-s0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T20:09:40.947Z\\\", \\\"updated_at\\\": \\\"2026-05-17T02:55:46.455Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"records\\\": 2286, \\\"seeds\\\": 497, \\\"skipped\\\": 91, \\\"wall_time_s\\\": 2296.7, \\\"depth_dist\\\": {\\\"gen0\\\": 497, \\\"gen1\\\": 497, \\\"gen2\\\": 457, \\\"gen3\\\": 429, \\\"gen4\\\": 406}, \\\"file\\\": \\\"data/pythia-1b/generations_shard0.jsonl\\\", \\\"file_size_mb\\\": 2.5}, \\\"hypothesis\\\": \\\"跨模型泛化数据生成（Pythia-1B shard0）：同家族更大模型 Pythia-1B 的 continuation 链是否展现与 Pythia-2.8B 相似的 depth dynamics，验证 depth signal 非特定参数量产物\\\", \\\"parent\\\": \\\"plan-002\\\"}, \\\"plan-002-eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T23:33:25.348Z\\\", \\\"updated_at\\\": \\\"2026-05-17T02:55:34.658Z\\\", \\\"hypothesis\\\": \\\"跨生成器泛化评估：Pythia-410M 深度特征在 leave-one-generator-out 设置下能否泛化到未见过的生成器\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"leave_one_out_avg_macro_f1\\\": 0.8037, \\\"best_held_out\\\": {\\\"model\\\": \\\"pythia-1b\\\", \\\"macro_f1\\\": 0.8507}, \\\"worst_held_out\\\": {\\\"model\\\": \\\"olmo-2-1b\\\", \\\"macro_f1\\\": 0.7519}, \\\"family_out_delta\\\": 0.0107, \\\"ablation_full_f1\\\": 0.8037, \\\"ablation_reference_only_f1\\\": 0.7543, \\\"ablation_surface_only_f1\\\": 0.7471, \\\"mcnemar_p\\\": 0, \\\"top_features\\\": [\\\"hapax_ratio_0.289\\\", \\\"ttr_0.168\\\", \\\"entropy_mean_0.160\\\"], \\\"entropy_std_drop\\\": 0.0049, \\\"entropy_std_drift\\\": 0.12, \\\"entropy_mean_drift\\\": 1.5}, \\\"parent\\\": \\\"plan-002\\\"}, \\\"plan-010-llm-rephrase\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-16T22:26:58.107Z\\\", \\\"updated_at\\\": \\\"2026-05-17T02:55:34.090Z\\\", \\\"hypothesis\\\": \\\"LLM-simulated editing robustness: Qwen3-0.6B rephrasing (1-3 sentences) 比 random word replacement 更接近真实人类编辑，预期 depth fingerprint 退化更小\\\", \\\"conclusion\\\": \\\"success\\\", \\\"notes\\\": \\\"v2 修复版：修正 binary task 定义(gen1-vs-gen2+)、3-class mapping、tail_decay 计算(rank 100-1000)。Original binary 0.6918 与 Table 3 (0.7014) 一致，确认修复正确。\\\", \\\"metrics\\\": {\\\"original_binary_f1\\\": 0.6918, \\\"original_binary_ci\\\": [0.6749, 0.7067], \\\"original_multiclass_f1\\\": 0.7385, \\\"original_multiclass_ci\\\": [0.7269, 0.7496], \\\"rephrased_binary_f1\\\": 0.6471, \\\"rephrased_binary_ci\\\": [0.6308, 0.6619], \\\"rephrased_multiclass_f1\\\": 0.6672, \\\"rephrased_multiclass_ci\\\": [0.6548, 0.6796], \\\"binary_drop\\\": -0.0447, \\\"multiclass_drop\\\": -0.0713, \\\"edit_distance_ratio\\\": 0.5071, \\\"avg_sentences_replaced\\\": 1.69, \\\"method\\\": \\\"7feature LOGO-CV, binary=gen1-vs-gen2+, 3class=gen0/gen1/gen2+\\\", \\\"bugs_fixed\\\": [\\\"binary_task_gen1_vs_gen2+\\\", \\\"3class_mapping\\\", \\\"tail_decay_rank100-1000\\\"]}, \\\"parent\\\": \\\"plan-010-robustness\\\"}, \\\"plan-015-v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-15T00:56:20.612Z\\\", \\\"updated_at\\\": \\\"2026-05-17T02:55:33.529Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"hypothesis\\\": \\\"Ordinal baseline bugfix + bootstrap CI: 修复 Binoculars denominator bug，验证 7-feature ensemble 显著优于所有单一检测器\\\", \\\"metrics\\\": {\\\"seven_feature_logo_f1\\\": 0.798, \\\"seven_feature_ci95\\\": [0.786, 0.799], \\\"avg_logprob_logo_f1\\\": 0.7653, \\\"avg_logprob_ci95\\\": [0.616, 0.82], \\\"ld_score_logo_f1\\\": 0.7212, \\\"ld_score_ci95\\\": [0.588, 0.77], \\\"fastdetectgpt_logo_f1\\\": 0.6269, \\\"fastdetectgpt_ci95\\\": [0.511, 0.762], \\\"binoculars_logo_f1\\\": 0.579, \\\"binoculars_ci95\\\": [0.405, 0.664], \\\"binoculars_bug_fixed\\\": true, \\\"ld_score_corrected_cv_f1\\\": 0.7925, \\\"bootstrap_7feat_vs_avglogprob\\\": {\\\"delta\\\": 0.039, \\\"p\\\": 0, \\\"significant\\\": true}, \\\"bootstrap_7feat_vs_fastdetectgpt\\\": {\\\"delta\\\": 0.067, \\\"p\\\": 0, \\\"significant\\\": true}}, \\\"parent\\\": \\\"plan-015\\\"}, \\\"plan-004-v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-15T00:45:17.861Z\\\", \\\"updated_at\\\": \\\"2026-05-17T02:55:33.296Z\\\", \\\"hypothesis\\\": \\\"Downstream utility (retry): depth-stratified 数据对 OLMo-2-0425-1B CLM fine-tuning 的影响——5 variants × 3 seeds，输出到数据盘\\\", \\\"notes\\\": \\\"15/15 runs 全部完成。Claim 3 (Downstream Utility) 负面结果：depth-aware curation 不优于随机抽样。排名 all(2.335) < size_matched(2.367) < depth01(2.387) ≈ binary_filtered(2.389) << depth0_only(2.681)。全量数据最优，depth filtering 反而损害 perplexity。跨 seed 方差极小(<0.002)。已由 D009 reframe 为 diagnostic-not-curative。\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"total_runs\\\": 15, \\\"completed\\\": 15, \\\"variants\\\": {\\\"all\\\": {\\\"eval_loss_mean\\\": 0.848, \\\"perplexity_mean\\\": 2.335, \\\"seeds\\\": {\\\"42\\\": {\\\"eval_loss\\\": 0.848, \\\"ppl\\\": 2.335}, \\\"123\\\": {\\\"eval_loss\\\": 0.848, \\\"ppl\\\": 2.335}, \\\"456\\\": {\\\"eval_loss\\\": 0.8482, \\\"ppl\\\": 2.3354}}}, \\\"size_matched\\\": {\\\"eval_loss_mean\\\": 0.8617, \\\"perplexity_mean\\\": 2.367, \\\"seeds\\\": {\\\"42\\\": {\\\"eval_loss\\\": 0.8618, \\\"ppl\\\": 2.367}, \\\"123\\\": {\\\"eval_loss\\\": 0.8615, \\\"ppl\\\": 2.367}, \\\"456\\\": {\\\"eval_loss\\\": 0.8618, \\\"ppl\\\": 2.367}}}, \\\"depth01\\\": {\\\"eval_loss_mean\\\": 0.8701, \\\"perplexity_mean\\\": 2.387, \\\"seeds\\\": {\\\"42\\\": {\\\"eval_loss\\\": 0.8703, \\\"ppl\\\": 2.3877}, \\\"123\\\": {\\\"eval_loss\\\": 0.87, \\\"ppl\\\": 2.3869}, \\\"456\\\": {\\\"eval_loss\\\": 0.8699, \\\"ppl\\\": 2.387}}}, \\\"binary_filtered\\\": {\\\"eval_loss_mean\\\": 0.8709, \\\"perplexity_mean\\\": 2.389, \\\"seeds\\\": {\\\"42\\\": {\\\"eval_loss\\\": 0.8708, \\\"ppl\\\": 2.389}, \\\"123\\\": {\\\"eval_loss\\\": 0.871, \\\"ppl\\\": 2.389}, \\\"456\\\": {\\\"eval_loss\\\": 0.871, \\\"ppl\\\": 2.389}}}, \\\"depth0_only\\\": {\\\"eval_loss_mean\\\": 0.9864, \\\"perplexity_mean\\\": 2.681, \\\"seeds\\\": {\\\"42\\\": {\\\"eval_loss\\\": 0.9865, \\\"ppl\\\": 2.6818}, \\\"123\\\": {\\\"eval_loss\\\": 0.9863, \\\"ppl\\\": 2.68}, \\\"456\\\": {\\\"eval_loss\\\": 0.9865, \\\"ppl\\\": 2.6817}}}}, \\\"ranking_by_ppl\\\": \\\"all(2.335) < size_matched(2.367) < depth01(2.387) ≈ binary_filtered(2.389) << depth0_only(2.681)\\\", \\\"seed_variance\\\": \\\"极小（同 variant 跨 seed ppl 差 <0.002）\\\"}, \\\"parent\\\": \\\"plan-004\\\"}, \\\"plan-003-olmo2ref\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-15T00:09:31.145Z\\\", \\\"updated_at\\\": \\\"2026-05-17T02:55:33.041Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"hypothesis\\\": \\\"跨家族参考模型验证（OLMo-2-1B）：用 OLMo-2-1B 作为参考模型提取 differential entropy 特征，验证 depth signal 的参考模型无关性——不同训练数据和架构的模型仍能检测相同的 depth dynamics\\\", \\\"parent\\\": \\\"plan-003\\\"}, \\\"plan-003-qwen06bref\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-15T00:09:31.649Z\\\", \\\"updated_at\\\": \\\"2026-05-17T02:55:27.742Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"hypothesis\\\": \\\"跨家族参考模型验证（Qwen3-0.6B）：用非 Pythia 家族的 Qwen3-0.6B 作为参考模型提取 differential entropy 特征，验证 depth signal 不依赖于参考模型与生成器的家族匹配\\\", \\\"parent\\\": \\\"plan-003\\\"}, \\\"plan-005-rewrite\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-15T03:28:47.421Z\\\", \\\"updated_at\\\": \\\"2026-05-17T02:55:19.976Z\\\", \\\"metrics\\\": {\\\"total_records\\\": 4827, \\\"unique_seeds\\\": 995, \\\"skipped\\\": 61, \\\"depth_distribution\\\": {\\\"0\\\": 995, \\\"1\\\": 995, \\\"2\\\": 959, \\\"3\\\": 944, \\\"4\\\": 934}, \\\"output_file\\\": \\\"/root/gen-depth-fingerprint/data/pythia-2.8b-inspired_rewriting/generations_shard0.jsonl\\\", \\\"file_size_mb\\\": 5.41, \\\"runtime_seconds\\\": 8584, \\\"speed_seeds_per_sec\\\": 0.12, \\\"depth_retention_d4_d0\\\": 0.939, \\\"vs_continuation\\\": \\\"retention 93.9% vs 83.1%, rewriting produces significantly more stable depth chains\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"hypothesis\\\": \\\"Inspired rewriting 链数据生成：rewriting prompt 要求模型受启发重写而非逐字续写，预期 depth retention 介于 continuation 和 elaboration 之间，因为重写保留主题但改变表达\\\", \\\"parent\\\": \\\"plan-005\\\"}, \\\"plan-005-elab\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-15T03:28:45.680Z\\\", \\\"updated_at\\\": \\\"2026-05-17T02:55:17.294Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"total_records\\\": 4946, \\\"unique_seeds\\\": 995, \\\"skipped\\\": 14, \\\"depth_distribution\\\": {\\\"0\\\": 995, \\\"1\\\": 995, \\\"2\\\": 989, \\\"3\\\": 986, \\\"4\\\": 981}, \\\"output_file\\\": \\\"/root/gen-depth-fingerprint/data/pythia-2.8b-elaboration/generations_shard0.jsonl\\\", \\\"file_size_mb\\\": 5.53, \\\"runtime_seconds\\\": 8960.2, \\\"depth_retention_d4_d0\\\": 0.986, \\\"logo_cv_f1\\\": {\\\"mean\\\": 0.73, \\\"std\\\": 0.011}, \\\"lopto_f1\\\": 0.7622, \\\"feature_drift_entropy_mean\\\": -0.4705, \\\"feature_drift_ttr\\\": -0.6413, \\\"feature_drift_hapax\\\": -0.8284, \\\"vs_continuation\\\": \\\"retention 98.6% vs 83.1%; CV F1 0.730 vs 0.781 — elaboration chains more stable but depth signal weaker within-type\\\", \\\"vs_rewriting\\\": \\\"retention 98.6% vs 93.9%; CV F1 0.730 vs 0.737 — similar discriminability, elaboration slightly lower\\\"}, \\\"hypothesis\\\": \\\"Elaboration 链数据生成：elaboration prompt 要求模型展开而非续写，预期 depth signal 因语义锚定更强而衰减更慢（retention > continuation 的 83%）\\\", \\\"parent\\\": \\\"plan-005\\\"}, \\\"plan-005-cont\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-15T03:28:43.383Z\\\", \\\"updated_at\\\": \\\"2026-05-17T02:55:14.334Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"total_records\\\": 4620, \\\"unique_seeds\\\": 995, \\\"skipped\\\": 168, \\\"depth_distribution\\\": {\\\"0\\\": 995, \\\"1\\\": 992, \\\"2\\\": 932, \\\"3\\\": 874, \\\"4\\\": 827}, \\\"output_file\\\": \\\"/root/gen-depth-fingerprint/data/pythia-2.8b-continuation/generations_shard0.jsonl\\\", \\\"file_size_mb\\\": 4.93, \\\"runtime_seconds\\\": 7760, \\\"speed_seeds_per_sec\\\": 0.13}, \\\"hypothesis\\\": \\\"Continuation 链数据生成：Pythia-2.8B 在 continuation prompt 下生成 depth 0-4 链，验证递归续写中 entropy/lexical 特征的单调漂移模式是否在 1000 seeds 规模下稳定复现\\\", \\\"parent\\\": \\\"plan-005\\\"}, \\\"plan-001-fix\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T18:50:14.620Z\\\", \\\"updated_at\\\": \\\"2026-05-17T02:55:10.600Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"full_macro_f1\\\": 0.8204, \\\"reference_only_f1\\\": 0.7187, \\\"surface_only_f1\\\": 0.7628, \\\"ref_vs_surf_bootstrap_ci\\\": \\\"[0.706,0.733] vs [0.747,0.774]\\\", \\\"h2_features\\\": \\\"entropy_mean, ttr, hapax_ratio\\\", \\\"h1_features\\\": \\\"tail_decay, entropy_std, entropy_max, entropy_min\\\", \\\"median_ppl_by_depth\\\": \\\"13.50, 4.96, 3.00, 2.07, 1.72\\\"}, \\\"hypothesis\\\": \\\"Feature ablation 修复验证：reference-only features (entropy系列+tail_decay) 独立于 surface features 仍能区分 depth，且两组特征的 bootstrap CI 不重叠，证明 differential response 和 lexical drift 是互补的独立信号源\\\", \\\"parent\\\": \\\"plan-001\\\"}, \\\"plan-010-robustness\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-16T22:09:57.049Z\\\", \\\"updated_at\\\": \\\"2026-05-16T22:11:48.657Z\\\", \\\"hypothesis\\\": \\\"Human edit robustness: depth fingerprint 在 5-20% random word replacement 下的 F1 退化测试，验证实际编辑场景（通常 < 5%）不影响检测\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"baseline_binary_f1\\\": 0.695, \\\"5pct_binary_f1\\\": 0.65, \\\"10pct_binary_f1\\\": 0.614, \\\"20pct_binary_f1\\\": 0.591, \\\"5pct_drop\\\": -0.046, \\\"10pct_drop\\\": -0.081, \\\"20pct_drop\\\": -0.104}}, \\\"review-exp-a-baseline-ensemble\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-15T12:22:30.747Z\\\", \\\"updated_at\\\": \\\"2026-05-15T12:22:33.270Z\\\", \\\"hypothesis\\\": \\\"审稿回应实验A：4-baseline ensemble + 统一超参对比，验证 7-feature vs 4-baseline vs 6-feature 在公平条件下的性能差异\\\"}, \\\"plan-005\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-15T03:24:02.435Z\\\", \\\"updated_at\\\": \\\"2026-05-15T06:20:59.698Z\\\", \\\"hypothesis\\\": \\\"Prompt type comparison: continuation vs elaboration vs inspired_rewriting 链的 depth signal 强度差异。Pythia-2.8B, 1000 seeds, 3 prompt types × 5 depths = 15K texts\\\", \\\"notes\\\": \\\"plan-005 完成。3 种 prompt type 全部成功。关键发现：(1) depth signal 跨 prompt type 存在（CV F1 0.73-0.78）；(2) LOPTO 泛化良好（avg 0.7525）；(3) surface features (ttr, hapax) 最稳健；(4) shape features 在非 continuation 中信号消失；(5) continuation 衰减最大（16.9%），elaboration 几乎无衰减（1.4%）。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"cv_f1\\\": {\\\"continuation\\\": 0.7806, \\\"inspired_rewriting\\\": 0.7368, \\\"elaboration\\\": 0.73}, \\\"lopto_f1\\\": {\\\"held_out_cont\\\": 0.762, \\\"held_out_elab\\\": 0.7622, \\\"held_out_rewrite\\\": 0.7334, \\\"avg\\\": 0.7525}, \\\"depth_retention_d4_d0\\\": {\\\"continuation\\\": 0.831, \\\"inspired_rewriting\\\": 0.939, \\\"elaboration\\\": 0.986}, \\\"drift_hapax_ratio\\\": {\\\"continuation\\\": -0.74, \\\"elaboration\\\": -0.828, \\\"rewriting\\\": -0.8}, \\\"drift_ttr\\\": {\\\"continuation\\\": -0.607, \\\"elaboration\\\": -0.641, \\\"rewriting\\\": -0.618}, \\\"drift_entropy_mean\\\": {\\\"continuation\\\": -0.557, \\\"elaboration\\\": -0.471, \\\"rewriting\\\": -0.477}, \\\"spearman_ttr\\\": {\\\"continuation\\\": -0.629, \\\"elaboration\\\": -0.666, \\\"rewriting\\\": -0.659}, \\\"spearman_hapax\\\": {\\\"continuation\\\": -0.651, \\\"elaboration\\\": -0.674, \\\"rewriting\\\": -0.67}, \\\"spearman_entropy_mean\\\": {\\\"continuation\\\": -0.665, \\\"elaboration\\\": -0.583, \\\"rewriting\\\": -0.564}}}, \\\"plan-015\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T23:58:41.890Z\\\", \\\"updated_at\\\": \\\"2026-05-15T01:25:59.552Z\\\", \\\"hypothesis\\\": \\\"现有检测器 ordinal baseline：FastDetectGPT/LD-Score 等检测器的连续分数是否已提供 ordinal depth signal\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"seven_feature_logo_f1\\\": 0.798, \\\"seven_feature_ci\\\": [0.786, 0.799], \\\"avg_logprob_logo_f1\\\": 0.7653, \\\"avg_logprob_ci\\\": [0.616, 0.82], \\\"avg_logprob_spearman\\\": 0.7876, \\\"ld_score_logo_f1\\\": 0.7212, \\\"ld_score_ci\\\": [0.588, 0.77], \\\"ld_score_spearman\\\": 0.7943, \\\"ld_score_pre_fix\\\": 0.6854, \\\"fast_detect_gpt_logo_f1\\\": 0.6269, \\\"fast_detect_gpt_ci\\\": [0.511, 0.762], \\\"fast_detect_gpt_spearman\\\": 0.4325, \\\"binoculars_logo_f1\\\": 0.579, \\\"binoculars_ci\\\": [0.405, 0.664], \\\"binoculars_spearman\\\": 0.1989, \\\"binoculars_bug_confirmed\\\": true, \\\"binoculars_bug_fix\\\": \\\"denominator changed from CE(performer, obs_argmax) to CE(performer, shifted_ids)\\\", \\\"bootstrap_n\\\": 1000, \\\"bootstrap_delta_7feat_vs_avglogprob\\\": {\\\"delta\\\": 0.039, \\\"p\\\": 0, \\\"significant\\\": true}, \\\"bootstrap_delta_7feat_vs_fdgpt\\\": {\\\"delta\\\": 0.067, \\\"p\\\": 0, \\\"significant\\\": true}, \\\"best_single_detector\\\": \\\"Avg-LogProb (0.7653)\\\", \\\"seven_feature_advantage_pp\\\": 3.3}}, \\\"plan-004\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-15T00:22:57.901Z\\\", \\\"updated_at\\\": \\\"2026-05-15T01:02:50.582Z\\\", \\\"hypothesis\\\": \\\"Downstream utility: depth-stratified 数据对 OLMo-2-0425-1B CLM fine-tuning 的影响——depth0_only vs depth01 vs all vs size_matched vs binary_filtered，5 variants × 3 seeds\\\", \\\"notes\\\": \\\"FAILED: 根因是 OOM on GPU0（与 Qwen3-8B 共享 16.5GB），非单纯磁盘满。日志有 5 个 OOM Traceback（尝试分配 784MiB 但 GPU 仅剩 307MB）。磁盘满是次因（旧 checkpoints 22GB 占满根分区）。已由 plan-004-v2 在 cuda:1/2/3 重跑。\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"plan-004-prep\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-14T23:58:42.465Z\\\", \\\"updated_at\\\": \\\"2026-05-15T00:19:49.846Z\\\", \\\"hypothesis\\\": \\\"Downstream utility 准备：depth-stratified 数据集 + OLMo-1B fine-tuning 脚本（不开跑，等 Director 确认）\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"model\\\": \\\"OLMo-2-0425-1B (1485M)\\\", \\\"datasets\\\": {\\\"depth0_only\\\": {\\\"train\\\": 797, \\\"test\\\": 3138}, \\\"depth01\\\": {\\\"train\\\": 3951, \\\"test\\\": 3138}, \\\"all\\\": {\\\"train\\\": 12299, \\\"test\\\": 3138}, \\\"size_matched\\\": {\\\"train\\\": 3951, \\\"test\\\": 3138}, \\\"binary_filtered\\\": {\\\"train\\\": 3951, \\\"test\\\": 3138}}, \\\"dry_run_loss\\\": 2.18, \\\"script\\\": \\\"finetune_downstream.py\\\"}}, \\\"plan-001-restore\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-14T19:14:00.170Z\\\", \\\"updated_at\\\": \\\"2026-05-15T00:19:35.359Z\\\", \\\"notes\\\": \\\"历史遗留条目，实际已由 plan-001-fix 完成覆盖。可忽略。\\\"}, \\\"mvp-001-gen-s0\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-14T17:23:13.139Z\\\", \\\"updated_at\\\": \\\"2026-05-15T00:19:34.474Z\\\", \\\"notes\\\": \\\"历史遗留条目，实际已由 mvp-001 完成覆盖。可忽略。\\\"}, \\\"plan-003\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T23:58:40.949Z\\\", \\\"updated_at\\\": \\\"2026-05-15T00:09:28.999Z\\\", \\\"hypothesis\\\": \\\"跨家族参考模型伪证化：用 OLMo-2-1B 和 Qwen3-0.6B 作参考模型提取特征，验证 differential depth response 非 Pythia 特异\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"logo_f1_pythia_ref\\\": 0.8034, \\\"logo_f1_olmo_ref\\\": 0.8072, \\\"logo_f1_qwen_ref\\\": 0.8158, \\\"entropy_drift_all_refs_negative\\\": true, \\\"olmo_ref_drift_range\\\": [-0.608, -0.9089], \\\"qwen_ref_drift_range\\\": [-0.9557, -1.3458], \\\"pythia_ref_drift_range\\\": [-1.1872, -1.4017], \\\"dual_dynamics_is_pythia_artifact\\\": false}}, \\\"plan-013\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T23:33:25.590Z\\\", \\\"updated_at\\\": \\\"2026-05-14T23:53:38.901Z\\\", \\\"hypothesis\\\": \\\"文本长度混淆控制：深度特征的区分力是否独立于文本长度变化（长度归一化后趋势是否保持）\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"spearman_rho_range\\\": \\\"[-0.066, +0.134]\\\", \\\"length_depth_correlation\\\": \\\"weak (|ρ|<0.14)\\\", \\\"normalized_ttr_trend_preserved\\\": true, \\\"normalized_hapax_trend_preserved\\\": true, \\\"normalized_rho_stronger\\\": true, \\\"length_matched_f1_delta\\\": \\\"+0.041\\\", \\\"length_is_confound\\\": false, \\\"dropout_short_text_bias\\\": true}}, \\\"plan-002\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T20:08:55.258Z\\\", \\\"updated_at\\\": \\\"2026-05-14T23:19:42.066Z\\\", \\\"hypothesis\\\": \\\"跨模型泛化：Pythia-410M 参考模型下的深度特征能否区分不同架构/规模生成器（Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B）的 continuation 链\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"total_records\\\": 18423, \\\"models\\\": 4, \\\"pythia_1b\\\": {\\\"records\\\": 4555, \\\"seeds\\\": 995, \\\"file\\\": \\\"data/pythia-1b/generations.jsonl\\\"}, \\\"olmo_2_1b\\\": {\\\"records\\\": 4713, \\\"seeds\\\": 995, \\\"file\\\": \\\"data/olmo-2-1b/generations.jsonl\\\"}, \\\"qwen3_0_6b\\\": {\\\"records\\\": 4538, \\\"seeds\\\": 996, \\\"depth_dist\\\": {\\\"gen0\\\": 996, \\\"gen1\\\": 986, \\\"gen2\\\": 938, \\\"gen3\\\": 840, \\\"gen4\\\": 778}, \\\"file\\\": \\\"data/qwen3-0.6b/generations.jsonl\\\"}, \\\"qwen3_1_7b\\\": {\\\"records\\\": 4617, \\\"seeds\\\": 996, \\\"depth_dist\\\": {\\\"gen0\\\": 996, \\\"gen1\\\": 983, \\\"gen2\\\": 941, \\\"gen3\\\": 875, \\\"gen4\\\": 822}, \\\"file\\\": \\\"data/qwen3-1.7b/generations.jsonl\\\"}}}, \\\"plan-002-qwen17b-retry-s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T21:25:19.756Z\\\", \\\"updated_at\\\": \\\"2026-05-14T22:24:07.274Z\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"r2 进程 PID 120694 存活，resume 从 seed 143 继续。之前 failed 标记是对旧 retry 进程的判断，r2 是新提交。ETA ~07:30 UTC\\\"}, \\\"plan-002-qwen17b-retry-s0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T21:25:18.048Z\\\", \\\"updated_at\\\": \\\"2026-05-14T22:24:06.388Z\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"r2 进程 PID 120617 存活，resume 从 seed 154 继续。之前 failed 标记是对旧 retry 进程的判断，r2 是新提交。ETA ~07:20 UTC\\\"}, \\\"plan-002-qwen06b-s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T21:25:23.092Z\\\", \\\"updated_at\\\": \\\"2026-05-14T22:07:37.394Z\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"失败原因: 进程在 218/498 seeds (44%) 正常运行中被外部终止，日志无任何 Python/CUDA 错误。与 s0 和 Qwen3-1.7B 同一 tmux session 死亡模式。系统性 tmux 问题。\\\"}, \\\"plan-002-qwen06b-s0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T21:25:21.697Z\\\", \\\"updated_at\\\": \\\"2026-05-14T22:07:33.758Z\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"失败原因: 进程在 226/498 seeds (45%) 正常运行中被外部终止，日志无任何 Python/CUDA 错误。与 Qwen3-1.7B 同一 tmux session 死亡模式。系统性 tmux 问题，非代码问题。诊断 Worker worker_diagnose_tmux-death-root-cause_20260514T220718 正在深查。\\\"}, \\\"plan-002-qwen17b-s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T20:53:21.708Z\\\", \\\"updated_at\\\": \\\"2026-05-14T21:53:51.130Z\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"重复提交（与 plan-002-qwen3-1_7b-s1 冲突），争抢 cuda:1 + 写同一输出文件。已 kill。\\\"}, \\\"plan-002-qwen17b-s0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T20:53:19.356Z\\\", \\\"updated_at\\\": \\\"2026-05-14T21:53:49.671Z\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"重复提交（与 plan-002-qwen3-1_7b-s0 冲突），争抢 cuda:0 + 写同一输出文件。已 kill。\\\"}, \\\"plan-002-qwen3-1_7b-s0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T20:52:58.460Z\\\", \\\"updated_at\\\": \\\"2026-05-14T21:53:48.299Z\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"失败原因: SIGHUP (EXIT_CODE=129)，运行 ~21min 后被外部终止。日志无 Python/CUDA 错误，进度正常（104/498 seeds）。同时 s1 也被 SIGHUP。OLMo-2 (cuda:2/3) 不受影响 → 非服务器重启。诊断 Worker worker_diagnose_plan-002-qwen3-1_7b_20260514T211526 正在排查。\\\"}, \\\"plan-002-qwen3-1_7b-s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T20:53:00.298Z\\\", \\\"updated_at\\\": \\\"2026-05-14T21:33:26.442Z\\\", \\\"conclusion\\\": \\\"killed\\\", \\\"notes\\\": \\\"失败原因: SIGHUP (EXIT_CODE=129)，运行 ~21min 后被外部终止。日志无 Python/CUDA 错误，进度正常（95/498 seeds）。与 s0 同时被终止。诊断 Worker 正在排查。\\\"}, \\\"plan-001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T18:25:29.824Z\\\", \\\"updated_at\\\": \\\"2026-05-14T19:34:17.597Z\\\", \\\"hypothesis\\\": \\\"Feature ablation: 模型级特征（entropy系列+tail_decay）独立于表面特征仍能区分生成深度；H1/H2趋势分析确认特征随depth的变化模式；perplexity随depth显著变化\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"note\\\": \\\"initial_run_partial_issues_fixed_in_plan-001-fix\\\", \\\"ablation_full_macro_f1\\\": 0.82, \\\"ablation_surface_only_f1\\\": 0.76, \\\"ablation_reference_only_f1\\\": 0.72}}, \\\"mvp-001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T16:17:16.218Z\\\", \\\"updated_at\\\": \\\"2026-05-14T18:08:20.940Z\\\", \\\"hypothesis\\\": \\\"Pythia-410M 参考模型的分布特征（entropy stats, tail-decay, TTR, hapax）能区分 Pythia-2.8B continuation 链的 gen-0/gen-1/gen-2+，3-class macro-F1 ≥ 0.45\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"macro_f1\\\": 0.8408, \\\"binary_f1_gen0_vs_gen2plus\\\": 0.8653, \\\"cv_macro_f1\\\": 0.806, \\\"cv_std\\\": 0.013, \\\"gen0_f1\\\": 0.9517, \\\"gen1_f1\\\": 0.7759, \\\"gen2plus_f1\\\": 0.7947, \\\"total_records\\\": 4609, \\\"seeds_used\\\": 995, \\\"skipped\\\": 173}}, \\\"mvp-001-gen-s3\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-14T17:23:17.526Z\\\", \\\"updated_at\\\": \\\"2026-05-14T17:25:51.261Z\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"失败原因: CUDA error: invalid device ordinal — submit_training_job 注入 CUDA_VISIBLE_DEVICES 后脚本只能看到 cuda:0，但命令用了 --device cuda:3 | 修复: --device 应始终为 cuda:0\\\"}, \\\"mvp-001-gen-s2\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-14T17:23:15.855Z\\\", \\\"updated_at\\\": \\\"2026-05-14T17:25:50.275Z\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"失败原因: CUDA error: invalid device ordinal — submit_training_job 注入 CUDA_VISIBLE_DEVICES 后脚本只能看到 cuda:0，但命令用了 --device cuda:2 | 修复: --device 应始终为 cuda:0\\\"}, \\\"mvp-001-gen-s1\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-14T17:23:14.464Z\\\", \\\"updated_at\\\": \\\"2026-05-14T17:25:48.863Z\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"失败原因: CUDA error: invalid device ordinal — submit_training_job 注入 CUDA_VISIBLE_DEVICES 后脚本只能看到 cuda:0，但命令用了 --device cuda:1 | 修复: --device 应始终为 cuda:0\\\"}}, \\\"count\\\": 56, \\\"total\\\": 56, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.1594}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp_054_instruct_llama3_2_3b\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-18T03:06:07.150Z\", \"updated_at\": \"2026-05-18T07:58:31.553Z\", \"hypothesis\": \"Instruct-tuned Llama-3.2-3B-Instruct shows degraded depth signal vs base Llama-3.2-3B (F1=0.697), quantifying instruction-tuning's impact on DDR\", \"notes\": \"生成 59% (292/497 seeds) 后 Worker 与服务器断连。脚本有 resume 支持。模型已下载到 /root/autodl-tmp/models/Llama-3.2-3B-Instruct-ms/。Eval 脚本已准备: eval_exp054_instruct_llama.py\", \"conclusion\": \"success\", \"metrics\": {\"instruct_binary_f1\": 0.8381, \"instruct_binary_ci\": [0.828, 0.847], \"instruct_3class_f1\": 0.5437, \"instruct_3class_ci\": [0.53, 0.558], \"base_binary_f1\": 0.8488, \"base_3class_f1\": 0.7424, \"rho_instruct_entropy_mean\": 0.2299, \"rho_instruct_entropy_std\": 0.2623, \"rho_instruct_entropy_min\": -0.0027, \"rho_instruct_entropy_max\": 0.2036, \"rho_instruct_tail_decay\": 0.1198, \"rho_instruct_ttr\": -0.1411, \"rho_instruct_hapax_ratio\": -0.1157, \"rho_base_entropy_mean\": -0.627, \"rho_base_ttr\": -0.6856, \"rho_base_hapax_ratio\": -0.6975, \"direction_reversals\": 3, \"reversed_features\": [\"entropy_mean\", \"entropy_std\", \"tail_decay\"], \"data_count\": 4974}}, \"exp_050_temp_curve_t09\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T22:15:11.626Z\", \"updated_at\": \"2026-05-18T06:09:24.876Z\", \"hypothesis\": \"DDR signal at t=0.9 degrades relative to t=0.7 but less severely than t=1.0, establishing monotonic temperature sensitivity\", \"conclusion\": \"failed\", \"notes\": \"Registry 误标 failed（startup recovery 机制）。实际 tmux tc_fix 仍在运行中。Phase 2 (Pythia-2.8B t=0.9) 39% 完成 (392/995 seeds)，预计 ~76min。Phase 3 (Qwen3-1.7B t=0.9) 待执行。总计 ~5-6h 完成。\", \"metrics\": {\"records\": 4536, \"model\": \"pythia-2.8b\", \"temperature\": 0.9, \"top_p\": 0.9, \"within_cv_binary_f1\": 0.5821, \"within_cv_binary_ci\": [0.5655, 0.5985], \"logo_binary_f1\": 0.4804, \"logo_binary_ci\": [0.4645, 0.4976], \"entropy_mean_rho\": -0.3016, \"delta_vs_t07_cv\": -0.157, \"delta_vs_t07_logo\": -0.259}}, \"exp_049_temp_curve_t05\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T22:15:10.383Z\", \"updated_at\": \"2026-05-18T06:09:22.443Z\", \"hypothesis\": \"DDR signal at t=0.5 should be stronger than t=0.7 (less randomness preserves more distributional structure)\", \"conclusion\": \"success\", \"notes\": \"Registry 误标 failed（startup recovery 机制）。实际 tmux tc_fix 仍在运行中。Phase 1 (t=0.5 generation) 已完成 4708 records。等待 phase 2+3 完成后统一提取特征和评估。\", \"metrics\": {\"records\": 4708, \"skipped\": 113, \"seeds\": 995, \"model\": \"pythia-2.8b\", \"temperature\": 0.5, \"top_p\": 0.9, \"within_cv_binary_f1\": 0.8432, \"within_cv_binary_ci\": [0.8301, 0.8558], \"logo_binary_f1\": 0.8136, \"logo_binary_ci\": [0.7984, 0.8282], \"entropy_mean_rho\": -0.5844}}, \"exp_053_instruct_olmo2_1b\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-18T03:06:06.142Z\", \"updated_at\": \"2026-05-18T03:46:16.047Z\", \"hypothesis\": \"Instruct-tuned OLMo-2-1B-Instruct shows degraded depth signal vs base OLMo-2-1B (F1=0.695), quantifying instruction-tuning's impact on DDR\", \"conclusion\": \"success\", \"metrics\": {\"within_binary_f1\": 0.8131, \"within_binary_ci\": [0.8012, 0.8251], \"within_3class_f1\": 0.5748, \"within_3class_ci\": [0.5605, 0.5897], \"base_binary_f1\": 0.8454, \"base_3class_f1\": 0.7538, \"gen1_f1_instruct\": 0.256, \"gen1_f1_base\": 0.523, \"delta_within_binary\": -0.032, \"delta_within_3class\": -0.179, \"spearman_instruct\": {\"entropy_mean\": 0.482, \"entropy_std\": 0.296, \"entropy_min\": 0.08, \"entropy_max\": 0.306, \"tail_decay\": 0.228, \"ttr\": 0.006, \"hapax_ratio\": 0.025}, \"spearman_base\": {\"entropy_mean\": -0.639, \"entropy_std\": -0.296, \"entropy_min\": -0.387, \"entropy_max\": 0.067, \"tail_decay\": -0.141, \"ttr\": -0.7, \"hapax_ratio\": -0.712}, \"features_reversed\": \"6/7\", \"model_used\": \"allenai/OLMo-2-0425-1B-Instruct\"}}, \"exp_052_instruct_qwen3_1_7b\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-18T03:06:04.788Z\", \"updated_at\": \"2026-05-18T03:26:14.267Z\", \"hypothesis\": \"Instruct-tuned Qwen3-1.7B (chat template, thinking=off) shows degraded depth signal vs base Qwen3-1.7B (F1=0.709), quantifying instruction-tuning's impact on DDR\", \"conclusion\": \"success\", \"metrics\": {\"within_binary_f1\": 0.8753, \"within_binary_ci\": [0.8667, 0.8837], \"within_3class_f1\": 0.7324, \"within_3class_ci\": [0.7195, 0.745], \"base_binary_f1\": 0.8614, \"base_3class_f1\": 0.769, \"logo_instruct_binary\": 0.658, \"logo_instruct_3class\": 0.543, \"logo_base_binary\": 0.821, \"logo_base_3class\": 0.802, \"gen1_f1_instruct\": 0.438, \"gen1_f1_base\": 0.579, \"spearman_direction\": \"reversed (instruct ρ>0, base ρ<0)\", \"delta_within_binary\": 0.014, \"delta_within_3class\": -0.037, \"delta_logo_binary\": -0.163}}, \"exp_051_independent_seed\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T22:38:00.466Z\", \"updated_at\": \"2026-05-18T02:01:42.126Z\", \"hypothesis\": \"Cross-generator depth classification with non-overlapping seeds achieves comparable F1 to shared-seed LOGO, ruling out topic fingerprint leakage\", \"conclusion\": \"success\", \"metrics\": {\"pythia_to_olmo_binary_f1\": 0.6945, \"pythia_to_olmo_ci\": [0.6727, 0.7167], \"olmo_to_pythia_binary_f1\": 0.666, \"olmo_to_pythia_ci\": [0.6429, 0.6893], \"avg_binary_f1\": 0.6803, \"shared_seed_logo_ref\": 0.694, \"delta_vs_shared\": -0.014}}, \"exp_048_cross_temp_transfer\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T12:52:44.889Z\", \"updated_at\": \"2026-05-17T17:07:19.391Z\", \"hypothesis\": \"Cross-temperature transfer: XGBoost 7-feature classifier trained at one sampling temperature (t=0.7 or t=1.0) maintains depth discrimination when tested at a different temperature, demonstrating deployment robustness to unknown decoding parameters\", \"conclusion\": \"success\", \"metrics\": {\"6gen_logo\": {\"within_0.7_binary\": 0.9471, \"within_0.7_3class\": 0.7888, \"cross_0.7to1.0_binary\": 0.9001, \"cross_0.7to1.0_3class\": 0.7225, \"within_1.0_binary\": 0.9107, \"within_1.0_3class\": 0.7257, \"cross_1.0to0.7_binary\": 0.9581, \"cross_1.0to0.7_3class\": 0.7913, \"caveat\": \"Only Qwen3-1.7B differs between conditions; 5/6 generators share data\"}, \"qwen_only\": {\"within_0.7_binary\": 0.9262, \"within_0.7_binary_ci\": [0.916, 0.935], \"within_0.7_3class\": 0.769, \"within_0.7_3class_ci\": [0.756, 0.781], \"cross_0.7to1.0_binary\": 0.7574, \"cross_0.7to1.0_binary_ci\": [0.745, 0.77], \"cross_0.7to1.0_3class\": 0.4581, \"cross_0.7to1.0_3class_ci\": [0.445, 0.472], \"within_1.0_binary\": 0.8248, \"within_1.0_binary_ci\": [0.81, 0.838], \"within_1.0_3class\": 0.5738, \"within_1.0_3class_ci\": [0.56, 0.588], \"cross_1.0to0.7_binary\": 0.9443, \"cross_1.0to0.7_binary_ci\": [0.936, 0.953], \"cross_1.0to0.7_3class\": 0.6014, \"cross_1.0to0.7_3class_ci\": [0.593, 0.611], \"delta_0.7train_binary_pp\": -16.9, \"delta_0.7train_3class_pp\": -31.1, \"delta_1.0train_binary_pp\": 12, \"delta_1.0train_3class_pp\": 2.8, \"asymmetric_transfer\": true}}, \"parent\": \"exp_047_multi_domain_t07\"}, \"exp_047_multi_domain_t07\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T05:51:25.881Z\", \"updated_at\": \"2026-05-17T07:22:04.483Z\", \"hypothesis\": \"Depth fingerprint generalizes across domains (News, Academic, Code) under standard decoding (t=0.7, top_p=0.9) matching main experiment params, eliminating the temperature confound from t=1.0 results and producing directly comparable domain generalization numbers\", \"parent\": \"exp_043_multi_domain_seeds\", \"metrics\": {\"news_binary_f1\": 0.7119, \"news_binary_ci\": [0.6898, 0.7332], \"news_3class_f1\": 0.7149, \"academic_binary_f1\": 0.6279, \"academic_binary_ci\": [0.6027, 0.6515], \"academic_3class_f1\": 0.6564, \"code_binary_f1\": 0.6872, \"code_binary_ci\": [0.6641, 0.71], \"code_3class_f1\": 0.6729, \"overall_binary_f1\": 0.6757, \"overall_3class_f1\": 0.6814, \"delta_vs_t10_news\": -0.034, \"delta_vs_t10_academic\": -0.1107, \"delta_vs_t10_code\": -0.0663}, \"conclusion\": \"success\"}, \"multi_domain_t07\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-17T05:54:55.365Z\", \"updated_at\": \"2026-05-17T05:54:55.365Z\"}, \"multi-domain-seeds\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T03:38:54.349Z\", \"updated_at\": \"2026-05-17T05:05:40.584Z\", \"hypothesis\": \"Domain independence: depth fingerprint 的 differential depth response 不依赖 seed domain——在 News/Academic/Code 三个非 Wikipedia 域上，7-feature ensemble 的 binary F1 与 Wikipedia baseline 差异 <10pp，证明 DDR 是生成过程的固有特性而非特定域文本属性的 artifact\", \"metrics\": {\"news_binary_f1\": 0.7459, \"news_binary_ci\": [0.726, 0.764], \"news_multiclass_f1\": 0.6516, \"academic_binary_f1\": 0.7386, \"academic_binary_ci\": [0.72, 0.757], \"academic_multiclass_f1\": 0.6223, \"code_binary_f1\": 0.7535, \"code_binary_ci\": [0.737, 0.77], \"code_multiclass_f1\": 0.6344, \"wikipedia_baseline_binary_f1\": 0.8148, \"wikipedia_baseline_multiclass_f1\": 0.8632, \"max_gap_vs_wiki_pp\": 7.62, \"worst_domain\": \"academic\", \"best_domain\": \"code\", \"conclusion_label\": \"domain_independent\"}, \"conclusion\": \"success\"}, \"plan-008-seed-stratification\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T00:21:12.380Z\", \"updated_at\": \"2026-05-17T02:56:26.724Z\", \"hypothesis\": \"Seed complexity independence: depth fingerprint 的判别能力不依赖 seed 文本的词汇复杂度（按 gen-0 TTR terciles 分层验证）\", \"conclusion\": \"success\", \"metrics\": {\"low_complexity_binary\": 0.685, \"medium_binary\": 0.695, \"high_complexity_binary\": 0.695, \"low_complexity_multi\": 0.772, \"medium_multi\": 0.778, \"high_complexity_multi\": 0.779, \"max_diff_binary_pp\": 1.06, \"max_diff_multiclass_pp\": 0.68, \"conclusion_label\": \"seed_independent\"}, \"parent\": \"plan-010-robustness\"}, \"plan-002-qwen06b-r2-s1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T22:35:11.142Z\", \"updated_at\": \"2026-05-17T02:56:25.805Z\", \"hypothesis\": \"跨家族泛化数据生成（Qwen3-0.6B shard1）：Qwen3-0.6B continuation 链第二分片，补全 ~995 seeds 覆盖\", \"notes\": \"Orphan 进程 PID 118126 存活，shard1 进度 340/500 seeds (68%)，当前 1542 行，预计 ~23:00 UTC 完成。GPU cuda:3 利用率 33%。\", \"conclusion\": \"success\", \"metrics\": {\"records\": 2268, \"seeds\": 498, \"depth_dist\": {\"0\": 498, \"1\": 493, \"2\": 470, \"3\": 417, \"4\": 390}, \"file\": \"generations_shard1.jsonl\"}, \"parent\": \"plan-002\"}, \"plan-002-qwen06b-r2-s0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T22:35:10.950Z\", \"updated_at\": \"2026-05-17T02:56:23.413Z\", \"hypothesis\": \"跨家族泛化数据生成（Qwen3-0.6B shard0）：最小参数量(0.6B) Qwen 模型的 continuation 链，验证 depth signal 在极小模型中是否仍存在（小模型可能因容量不足而无法维持深层生成的分布稳定性）\", \"notes\": \"Orphan 进程 PID 117855 存活，shard0 进度 350/500 seeds (70%)，当前 1593 行，预计 ~23:00 UTC 完成。GPU cuda:2 利用率 34%。\", \"conclusion\": \"success\", \"metrics\": {\"records\": 2270, \"seeds\": 498, \"depth_dist\": {\"0\": 498, \"1\": 493, \"2\": 468, \"3\": 423, \"4\": 388}, \"file\": \"generations_shard0.jsonl\"}, \"parent\": \"plan-002\"}, \"review-exp-c-overall-ci\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T12:22:37.037Z\", \"updated_at\": \"2026-05-17T02:56:15.141Z\", \"hypothesis\": \"6-generator LOGO 的 overall bootstrap CI 窄且不跨越 chance level，entropy_max/entropy_min 的个体 Spearman ρ 验证其对 depth 的单调贡献方向（max 正相关因高 depth 分布更尖，min 负相关因低概率 tail 被压缩）\", \"conclusion\": \"success\", \"metrics\": {\"overall_logo_f1\": 0.7879, \"overall_ci95\": [0.783, 0.7929], \"spearman_entropy_max\": 0.0503, \"spearman_entropy_min\": -0.4061, \"spearman_hapax\": -0.6467, \"spearman_ttr\": -0.6302, \"spearman_entropy_mean\": -0.6098, \"spearman_entropy_std\": -0.1996, \"spearman_tail_decay\": -0.0403}}, \"review-exp-b-topic-drift\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T12:22:34.096Z\", \"updated_at\": \"2026-05-17T02:56:11.446Z\", \"hypothesis\": \"Depth fingerprint 不仅仅捕捉 topic shift：语义漂移(embedding cosine similarity)与 depth 相关性弱(|ρ|<0.3)，而 entropy/lexical features 与 depth 的相关性强(|ρ|>0.5)，证明 depth signal 来自生成过程的统计特性而非内容偏移\", \"conclusion\": \"success\", \"metrics\": {\"semantic_similarity_by_transition\": {\"0_to_1\": {\"mean\": 0.622, \"std\": 0.1647}, \"1_to_2\": {\"mean\": 0.6829, \"std\": 0.1837}, \"2_to_3\": {\"mean\": 0.801, \"std\": 0.2012}, \"3_to_4\": {\"mean\": 0.8587, \"std\": 0.1895}}, \"prompt_type_avg_sim\": {\"continuation\": 0.7168, \"elaboration\": 0.8093, \"inspired_rewriting\": 0.808}, \"shape_feature_correlations\": {\"entropy_std_rho\": -0.1639, \"tail_decay_rho\": 0.0675}, \"drifting_feature_correlations\": {\"hapax_ratio_rho\": -0.1242, \"ttr_rho\": -0.1784, \"entropy_mean_rho\": -0.2859}}}, \"plan-014\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T00:12:01.909Z\", \"updated_at\": \"2026-05-17T02:56:07.395Z\", \"hypothesis\": \"大模型规模泛化：Qwen3-8B (7B+参数) 的 continuation 链是否展现同样的 entropy 收敛和 lexical drift，验证 depth dynamics 不因模型容量增大而消失（更大模型可能有更强的分布记忆导致 depth signal 衰减）\", \"notes\": \"2026-05-15 04:25: ✅ 完整数据重算完成 (4409 records, 977 seeds)。与 82% 快照差异在统计噪声范围内：LOGO +0.0011, qwen8b held-out -0.0037。最终数字已确认，可用于论文。\", \"conclusion\": \"success\", \"metrics\": {\"total_records\": 4497, \"unique_seeds\": 995, \"depth_dist\": {\"0\": 995, \"1\": 979, \"2\": 937, \"3\": 831, \"4\": 755}, \"logo_6gen_avg_f1\": 0.7893, \"logo_per_generator\": {\"olmo-2-1b\": 0.7635, \"pythia-1b\": 0.8562, \"pythia-2.8b\": 0.8041, \"qwen3-0.6b\": 0.8243, \"qwen3-1.7b\": 0.8046, \"qwen3-8b\": 0.6832}, \"logo_qwen3_8b_held_out_f1\": 0.6832, \"logo_5gen_baseline_f1\": 0.8, \"spearman\": {\"hapax_ratio\": -0.5578, \"ttr\": -0.5419, \"entropy_mean\": -0.4754, \"entropy_min\": -0.3029, \"entropy_max\": 0.0946, \"tail_decay\": -0.0894, \"entropy_std\": -0.0755}, \"feature_importance\": {\"hapax_ratio\": 0.269, \"entropy_mean\": 0.1637, \"ttr\": 0.159, \"entropy_max\": 0.0634, \"entropy_std\": 0.0463, \"entropy_min\": 0.0153, \"tail_decay\": 0.0123}, \"revalidation_v2_vs_snapshot\": \"LOGO +0.0007 (0.7886→0.7893), qwen8b -0.0054 (0.6886→0.6832)\", \"revalidation_v2_conclusion\": \"complete_data_validates_snapshot_robustness\"}, \"parent\": \"plan-002\"}, \"plan-002-qwen17b-r2-s1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T21:58:14.195Z\", \"updated_at\": \"2026-05-17T02:56:03.576Z\", \"notes\": \"Orphan 进程 PID 120694 存活，shard1 进度 295/500 seeds (59%)，预计 ~22:55 UTC 完成。GPU cuda:1 利用率 44%。\", \"conclusion\": \"success\", \"metrics\": {\"records\": 2326, \"seeds\": 498, \"depth_dist\": {\"0\": 498, \"1\": 491, \"2\": 473, \"3\": 440, \"4\": 424}, \"skipped\": 53, \"duration_s\": 4228, \"file\": \"generations_shard1.jsonl\"}, \"hypothesis\": \"跨家族泛化数据生成（Qwen3-1.7B shard1）：Qwen3-1.7B continuation 链第二分片，补全 ~995 seeds 覆盖\", \"parent\": \"plan-002\"}, \"plan-002-qwen17b-r2-s0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T21:58:12.310Z\", \"updated_at\": \"2026-05-17T02:56:01.158Z\", \"notes\": \"Orphan 进程 PID 120617 存活，shard0 进度 289/500 seeds (58%)，预计 ~22:55 UTC 完成。GPU cuda:0 利用率 40%。\", \"conclusion\": \"success\", \"metrics\": {\"records\": 2291, \"seeds\": 498, \"depth_dist\": {\"0\": 498, \"1\": 492, \"2\": 468, \"3\": 435, \"4\": 398}, \"skipped\": 199, \"duration_s\": 4548.2, \"file_size_mb\": 2.5, \"file\": \"generations_shard0.jsonl\"}, \"hypothesis\": \"跨家族泛化数据生成（Qwen3-1.7B shard0）：Qwen 家族 1.7B 模型的 continuation 链 depth dynamics，验证中等规模非 Pythia 模型也产生可检测的 depth signal\", \"parent\": \"plan-002\"}, \"plan-002-olmo2-s1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T20:09:46.880Z\", \"updated_at\": \"2026-05-17T02:55:54.134Z\", \"conclusion\": \"success\", \"metrics\": {\"records\": 2334, \"seeds\": 498, \"skipped\": 70, \"wall_time_s\": 4081.2, \"depth_dist\": {\"gen0\": 498, \"gen1\": 494, \"gen2\": 470, \"gen3\": 444, \"gen4\": 428}, \"file\": \"generations_shard1.jsonl\", \"file_size_mb\": 2.57}, \"hypothesis\": \"跨家族泛化数据生成（OLMo-2-1B shard1）：OLMo-2-1B continuation 链第二分片，补全 ~995 seeds 覆盖\", \"parent\": \"plan-002\"}, \"plan-002-olmo2-s0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T20:09:45.173Z\", \"updated_at\": \"2026-05-17T02:55:52.145Z\", \"conclusion\": \"success\", \"metrics\": {\"records\": 2379, \"seeds\": 497, \"skipped\": 47, \"wall_time_s\": 3885.2, \"depth_dist\": {\"gen0\": 497, \"gen1\": 494, \"gen2\": 477, \"gen3\": 461, \"gen4\": 450}, \"file\": \"generations_shard0.jsonl\", \"file_size_mb\": 2.68}, \"hypothesis\": \"跨家族泛化数据生成（OLMo-2-1B shard0）：非 Pythia 架构(OLMo)的 continuation 链中 depth signal 是否存在，验证 depth dynamics 跨训练数据和架构的普遍性\", \"parent\": \"plan-002\"}, \"plan-002-pythia1b-s1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T20:09:42.815Z\", \"updated_at\": \"2026-05-17T02:55:49.321Z\", \"conclusion\": \"success\", \"metrics\": {\"records\": 2269, \"seeds\": 498, \"skipped\": 100, \"wall_time_s\": 2247.6, \"depth_dist\": {\"gen0\": 498, \"gen1\": 496, \"gen2\": 455, \"gen3\": 422, \"gen4\": 398}, \"file\": \"data/pythia-1b/generations_shard1.jsonl\", \"file_size_mb\": 2.44}, \"hypothesis\": \"跨模型泛化数据生成（Pythia-1B shard1）：Pythia-1B continuation 链第二分片，与 shard0 合并后提供完整 ~995 seeds 的 depth 数据\", \"parent\": \"plan-002\"}, \"plan-002-pythia1b-s0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T20:09:40.947Z\", \"updated_at\": \"2026-05-17T02:55:46.455Z\", \"conclusion\": \"success\", \"metrics\": {\"records\": 2286, \"seeds\": 497, \"skipped\": 91, \"wall_time_s\": 2296.7, \"depth_dist\": {\"gen0\": 497, \"gen1\": 497, \"gen2\": 457, \"gen3\": 429, \"gen4\": 406}, \"file\": \"data/pythia-1b/generations_shard0.jsonl\", \"file_size_mb\": 2.5}, \"hypothesis\": \"跨模型泛化数据生成（Pythia-1B shard0）：同家族更大模型 Pythia-1B 的 continuation 链是否展现与 Pythia-2.8B 相似的 depth dynamics，验证 depth signal 非特定参数量产物\", \"parent\": \"plan-002\"}, \"plan-002-eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T23:33:25.348Z\", \"updated_at\": \"2026-05-17T02:55:34.658Z\", \"hypothesis\": \"跨生成器泛化评估：Pythia-410M 深度特征在 leave-one-generator-out 设置下能否泛化到未见过的生成器\", \"conclusion\": \"success\", \"metrics\": {\"leave_one_out_avg_macro_f1\": 0.8037, \"best_held_out\": {\"model\": \"pythia-1b\", \"macro_f1\": 0.8507}, \"worst_held_out\": {\"model\": \"olmo-2-1b\", \"macro_f1\": 0.7519}, \"family_out_delta\": 0.0107, \"ablation_full_f1\": 0.8037, \"ablation_reference_only_f1\": 0.7543, \"ablation_surface_only_f1\": 0.7471, \"mcnemar_p\": 0, \"top_features\": [\"hapax_ratio_0.289\", \"ttr_0.168\", \"entropy_mean_0.160\"], \"entropy_std_drop\": 0.0049, \"entropy_std_drift\": 0.12, \"entropy_mean_drift\": 1.5}, \"parent\": \"plan-002\"}, \"plan-010-llm-rephrase\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T22:26:58.107Z\", \"updated_at\": \"2026-05-17T02:55:34.090Z\", \"hypothesis\": \"LLM-simulated editing robustness: Qwen3-0.6B rephrasing (1-3 sentences) 比 random word replacement 更接近真实人类编辑，预期 depth fingerprint 退化更小\", \"conclusion\": \"success\", \"notes\": \"v2 修复版：修正 binary task 定义(gen1-vs-gen2+)、3-class mapping、tail_decay 计算(rank 100-1000)。Original binary 0.6918 与 Table 3 (0.7014) 一致，确认修复正确。\", \"metrics\": {\"original_binary_f1\": 0.6918, \"original_binary_ci\": [0.6749, 0.7067], \"original_multiclass_f1\": 0.7385, \"original_multiclass_ci\": [0.7269, 0.7496], \"rephrased_binary_f1\": 0.6471, \"rephrased_binary_ci\": [0.6308, 0.6619], \"rephrased_multiclass_f1\": 0.6672, \"rephrased_multiclass_ci\": [0.6548, 0.6796], \"binary_drop\": -0.0447, \"multiclass_drop\": -0.0713, \"edit_distance_ratio\": 0.5071, \"avg_sentences_replaced\": 1.69, \"method\": \"7feature LOGO-CV, binary=gen1-vs-gen2+, 3class=gen0/gen1/gen2+\", \"bugs_fixed\": [\"binary_task_gen1_vs_gen2+\", \"3class_mapping\", \"tail_decay_rank100-1000\"]}, \"parent\": \"plan-010-robustness\"}, \"plan-015-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T00:56:20.612Z\", \"updated_at\": \"2026-05-17T02:55:33.529Z\", \"conclusion\": \"success\", \"hypothesis\": \"Ordinal baseline bugfix + bootstrap CI: 修复 Binoculars denominator bug，验证 7-feature ensemble 显著优于所有单一检测器\", \"metrics\": {\"seven_feature_logo_f1\": 0.798, \"seven_feature_ci95\": [0.786, 0.799], \"avg_logprob_logo_f1\": 0.7653, \"avg_logprob_ci95\": [0.616, 0.82], \"ld_score_logo_f1\": 0.7212, \"ld_score_ci95\": [0.588, 0.77], \"fastdetectgpt_logo_f1\": 0.6269, \"fastdetectgpt_ci95\": [0.511, 0.762], \"binoculars_logo_f1\": 0.579, \"binoculars_ci95\": [0.405, 0.664], \"binoculars_bug_fixed\": true, \"ld_score_corrected_cv_f1\": 0.7925, \"bootstrap_7feat_vs_avglogprob\": {\"delta\": 0.039, \"p\": 0, \"significant\": true}, \"bootstrap_7feat_vs_fastdetectgpt\": {\"delta\": 0.067, \"p\": 0, \"significant\": true}}, \"parent\": \"plan-015\"}, \"plan-004-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T00:45:17.861Z\", \"updated_at\": \"2026-05-17T02:55:33.296Z\", \"hypothesis\": \"Downstream utility (retry): depth-stratified 数据对 OLMo-2-0425-1B CLM fine-tuning 的影响——5 variants × 3 seeds，输出到数据盘\", \"notes\": \"15/15 runs 全部完成。Claim 3 (Downstream Utility) 负面结果：depth-aware curation 不优于随机抽样。排名 all(2.335) < size_matched(2.367) < depth01(2.387) ≈ binary_filtered(2.389) << depth0_only(2.681)。全量数据最优，depth filtering 反而损害 perplexity。跨 seed 方差极小(<0.002)。已由 D009 reframe 为 diagnostic-not-curative。\", \"conclusion\": \"negative\", \"metrics\": {\"total_runs\": 15, \"completed\": 15, \"variants\": {\"all\": {\"eval_loss_mean\": 0.848, \"perplexity_mean\": 2.335, \"seeds\": {\"42\": {\"eval_loss\": 0.848, \"ppl\": 2.335}, \"123\": {\"eval_loss\": 0.848, \"ppl\": 2.335}, \"456\": {\"eval_loss\": 0.8482, \"ppl\": 2.3354}}}, \"size_matched\": {\"eval_loss_mean\": 0.8617, \"perplexity_mean\": 2.367, \"seeds\": {\"42\": {\"eval_loss\": 0.8618, \"ppl\": 2.367}, \"123\": {\"eval_loss\": 0.8615, \"ppl\": 2.367}, \"456\": {\"eval_loss\": 0.8618, \"ppl\": 2.367}}}, \"depth01\": {\"eval_loss_mean\": 0.8701, \"perplexity_mean\": 2.387, \"seeds\": {\"42\": {\"eval_loss\": 0.8703, \"ppl\": 2.3877}, \"123\": {\"eval_loss\": 0.87, \"ppl\": 2.3869}, \"456\": {\"eval_loss\": 0.8699, \"ppl\": 2.387}}}, \"binary_filtered\": {\"eval_loss_mean\": 0.8709, \"perplexity_mean\": 2.389, \"seeds\": {\"42\": {\"eval_loss\": 0.8708, \"ppl\": 2.389}, \"123\": {\"eval_loss\": 0.871, \"ppl\": 2.389}, \"456\": {\"eval_loss\": 0.871, \"ppl\": 2.389}}}, \"depth0_only\": {\"eval_loss_mean\": 0.9864, \"perplexity_mean\": 2.681, \"seeds\": {\"42\": {\"eval_loss\": 0.9865, \"ppl\": 2.6818}, \"123\": {\"eval_loss\": 0.9863, \"ppl\": 2.68}, \"456\": {\"eval_loss\": 0.9865, \"ppl\": 2.6817}}}}, \"ranking_by_ppl\": \"all(2.335) < size_matched(2.367) < depth01(2.387) ≈ binary_filtered(2.389) << depth0_only(2.681)\", \"seed_variance\": \"极小（同 variant 跨 seed ppl 差 <0.002）\"}, \"parent\": \"plan-004\"}, \"plan-003-olmo2ref\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T00:09:31.145Z\", \"updated_at\": \"2026-05-17T02:55:33.041Z\", \"conclusion\": \"success\", \"hypothesis\": \"跨家族参考模型验证（OLMo-2-1B）：用 OLMo-2-1B 作为参考模型提取 differential entropy 特征，验证 depth signal 的参考模型无关性——不同训练数据和架构的模型仍能检测相同的 depth dynamics\", \"parent\": \"plan-003\"}, \"plan-003-qwen06bref\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T00:09:31.649Z\", \"updated_at\": \"2026-05-17T02:55:27.742Z\", \"conclusion\": \"success\", \"hypothesis\": \"跨家族参考模型验证（Qwen3-0.6B）：用非 Pythia 家族的 Qwen3-0.6B 作为参考模型提取 differential entropy 特征，验证 depth signal 不依赖于参考模型与生成器的家族匹配\", \"parent\": \"plan-003\"}, \"plan-005-rewrite\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T03:28:47.421Z\", \"updated_at\": \"2026-05-17T02:55:19.976Z\", \"metrics\": {\"total_records\": 4827, \"unique_seeds\": 995, \"skipped\": 61, \"depth_distribution\": {\"0\": 995, \"1\": 995, \"2\": 959, \"3\": 944, \"4\": 934}, \"output_file\": \"/root/gen-depth-fingerprint/data/pythia-2.8b-inspired_rewriting/generations_shard0.jsonl\", \"file_size_mb\": 5.41, \"runtime_seconds\": 8584, \"speed_seeds_per_sec\": 0.12, \"depth_retention_d4_d0\": 0.939, \"vs_continuation\": \"retention 93.9% vs 83.1%, rewriting produces significantly more stable depth chains\"}, \"conclusion\": \"success\", \"hypothesis\": \"Inspired rewriting 链数据生成：rewriting prompt 要求模型受启发重写而非逐字续写，预期 depth retention 介于 continuation 和 elaboration 之间，因为重写保留主题但改变表达\", \"parent\": \"plan-005\"}, \"plan-005-elab\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T03:28:45.680Z\", \"updated_at\": \"2026-05-17T02:55:17.294Z\", \"conclusion\": \"success\", \"metrics\": {\"total_records\": 4946, \"unique_seeds\": 995, \"skipped\": 14, \"depth_distribution\": {\"0\": 995, \"1\": 995, \"2\": 989, \"3\": 986, \"4\": 981}, \"output_file\": \"/root/gen-depth-fingerprint/data/pythia-2.8b-elaboration/generations_shard0.jsonl\", \"file_size_mb\": 5.53, \"runtime_seconds\": 8960.2, \"depth_retention_d4_d0\": 0.986, \"logo_cv_f1\": {\"mean\": 0.73, \"std\": 0.011}, \"lopto_f1\": 0.7622, \"feature_drift_entropy_mean\": -0.4705, \"feature_drift_ttr\": -0.6413, \"feature_drift_hapax\": -0.8284, \"vs_continuation\": \"retention 98.6% vs 83.1%; CV F1 0.730 vs 0.781 — elaboration chains more stable but depth signal weaker within-type\", \"vs_rewriting\": \"retention 98.6% vs 93.9%; CV F1 0.730 vs 0.737 — similar discriminability, elaboration slightly lower\"}, \"hypothesis\": \"Elaboration 链数据生成：elaboration prompt 要求模型展开而非续写，预期 depth signal 因语义锚定更强而衰减更慢（retention > continuation 的 83%）\", \"parent\": \"plan-005\"}, \"plan-005-cont\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T03:28:43.383Z\", \"updated_at\": \"2026-05-17T02:55:14.334Z\", \"conclusion\": \"success\", \"metrics\": {\"total_records\": 4620, \"unique_seeds\": 995, \"skipped\": 168, \"depth_distribution\": {\"0\": 995, \"1\": 992, \"2\": 932, \"3\": 874, \"4\": 827}, \"output_file\": \"/root/gen-depth-fingerprint/data/pythia-2.8b-continuation/generations_shard0.jsonl\", \"file_size_mb\": 4.93, \"runtime_seconds\": 7760, \"speed_seeds_per_sec\": 0.13}, \"hypothesis\": \"Continuation 链数据生成：Pythia-2.8B 在 continuation prompt 下生成 depth 0-4 链，验证递归续写中 entropy/lexical 特征的单调漂移模式是否在 1000 seeds 规模下稳定复现\", \"parent\": \"plan-005\"}, \"plan-001-fix\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T18:50:14.620Z\", \"updated_at\": \"2026-05-17T02:55:10.600Z\", \"conclusion\": \"success\", \"metrics\": {\"full_macro_f1\": 0.8204, \"reference_only_f1\": 0.7187, \"surface_only_f1\": 0.7628, \"ref_vs_surf_bootstrap_ci\": \"[0.706,0.733] vs [0.747,0.774]\", \"h2_features\": \"entropy_mean, ttr, hapax_ratio\", \"h1_features\": \"tail_decay, entropy_std, entropy_max, entropy_min\", \"median_ppl_by_depth\": \"13.50, 4.96, 3.00, 2.07, 1.72\"}, \"hypothesis\": \"Feature ablation 修复验证：reference-only features (entropy系列+tail_decay) 独立于 surface features 仍能区分 depth，且两组特征的 bootstrap CI 不重叠，证明 differential response 和 lexical drift 是互补的独立信号源\", \"parent\": \"plan-001\"}, \"plan-010-robustness\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T22:09:57.049Z\", \"updated_at\": \"2026-05-16T22:11:48.657Z\", \"hypothesis\": \"Human edit robustness: depth fingerprint 在 5-20% random word replacement 下的 F1 退化测试，验证实际编辑场景（通常 < 5%）不影响检测\", \"conclusion\": \"success\", \"metrics\": {\"baseline_binary_f1\": 0.695, \"5pct_binary_f1\": 0.65, \"10pct_binary_f1\": 0.614, \"20pct_binary_f1\": 0.591, \"5pct_drop\": -0.046, \"10pct_drop\": -0.081, \"20pct_drop\": -0.104}}, \"review-exp-a-baseline-ensemble\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-15T12:22:30.747Z\", \"updated_at\": \"2026-05-15T12:22:33.270Z\", \"hypothesis\": \"审稿回应实验A：4-baseline ensemble + 统一超参对比，验证 7-feature vs 4-baseline vs 6-feature 在公平条件下的性能差异\"}, \"plan-005\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T03:24:02.435Z\", \"updated_at\": \"2026-05-15T06:20:59.698Z\", \"hypothesis\": \"Prompt type comparison: continuation vs elaboration vs inspired_rewriting 链的 depth signal 强度差异。Pythia-2.8B, 1000 seeds, 3 prompt types × 5 depths = 15K texts\", \"notes\": \"plan-005 完成。3 种 prompt type 全部成功。关键发现：(1) depth signal 跨 prompt type 存在（CV F1 0.73-0.78）；(2) LOPTO 泛化良好（avg 0.7525）；(3) surface features (ttr, hapax) 最稳健；(4) shape features 在非 continuation 中信号消失；(5) continuation 衰减最大（16.9%），elaboration 几乎无衰减（1.4%）。\", \"conclusion\": \"success\", \"metrics\": {\"cv_f1\": {\"continuation\": 0.7806, \"inspired_rewriting\": 0.7368, \"elaboration\": 0.73}, \"lopto_f1\": {\"held_out_cont\": 0.762, \"held_out_elab\": 0.7622, \"held_out_rewrite\": 0.7334, \"avg\": 0.7525}, \"depth_retention_d4_d0\": {\"continuation\": 0.831, \"inspired_rewriting\": 0.939, \"elaboration\": 0.986}, \"drift_hapax_ratio\": {\"continuation\": -0.74, \"elaboration\": -0.828, \"rewriting\": -0.8}, \"drift_ttr\": {\"continuation\": -0.607, \"elaboration\": -0.641, \"rewriting\": -0.618}, \"drift_entropy_mean\": {\"continuation\": -0.557, \"elaboration\": -0.471, \"rewriting\": -0.477}, \"spearman_ttr\": {\"continuation\": -0.629, \"elaboration\": -0.666, \"rewriting\": -0.659}, \"spearman_hapax\": {\"continuation\": -0.651, \"elaboration\": -0.674, \"rewriting\": -0.67}, \"spearman_entropy_mean\": {\"continuation\": -0.665, \"elaboration\": -0.583, \"rewriting\": -0.564}}}, \"plan-015\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T23:58:41.890Z\", \"updated_at\": \"2026-05-15T01:25:59.552Z\", \"hypothesis\": \"现有检测器 ordinal baseline：FastDetectGPT/LD-Score 等检测器的连续分数是否已提供 ordinal depth signal\", \"conclusion\": \"success\", \"metrics\": {\"seven_feature_logo_f1\": 0.798, \"seven_feature_ci\": [0.786, 0.799], \"avg_logprob_logo_f1\": 0.7653, \"avg_logprob_ci\": [0.616, 0.82], \"avg_logprob_spearman\": 0.7876, \"ld_score_logo_f1\": 0.7212, \"ld_score_ci\": [0.588, 0.77], \"ld_score_spearman\": 0.7943, \"ld_score_pre_fix\": 0.6854, \"fast_detect_gpt_logo_f1\": 0.6269, \"fast_detect_gpt_ci\": [0.511, 0.762], \"fast_detect_gpt_spearman\": 0.4325, \"binoculars_logo_f1\": 0.579, \"binoculars_ci\": [0.405, 0.664], \"binoculars_spearman\": 0.1989, \"binoculars_bug_confirmed\": true, \"binoculars_bug_fix\": \"denominator changed from CE(performer, obs_argmax) to CE(performer, shifted_ids)\", \"bootstrap_n\": 1000, \"bootstrap_delta_7feat_vs_avglogprob\": {\"delta\": 0.039, \"p\": 0, \"significant\": true}, \"bootstrap_delta_7feat_vs_fdgpt\": {\"delta\": 0.067, \"p\": 0, \"significant\": true}, \"best_single_detector\": \"Avg-LogProb (0.7653)\", \"seven_feature_advantage_pp\": 3.3}}, \"plan-004\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T00:22:57.901Z\", \"updated_at\": \"2026-05-15T01:02:50.582Z\", \"hypothesis\": \"Downstream utility: depth-stratified 数据对 OLMo-2-0425-1B CLM fine-tuning 的影响——depth0_only vs depth01 vs all vs size_matched vs binary_filtered，5 variants × 3 seeds\", \"notes\": \"FAILED: 根因是 OOM on GPU0（与 Qwen3-8B 共享 16.5GB），非单纯磁盘满。日志有 5 个 OOM Traceback（尝试分配 784MiB 但 GPU 仅剩 307MB）。磁盘满是次因（旧 checkpoints 22GB 占满根分区）。已由 plan-004-v2 在 cuda:1/2/3 重跑。\", \"conclusion\": \"failed\"}, \"plan-004-prep\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-14T23:58:42.465Z\", \"updated_at\": \"2026-05-15T00:19:49.846Z\", \"hypothesis\": \"Downstream utility 准备：depth-stratified 数据集 + OLMo-1B fine-tuning 脚本（不开跑，等 Director 确认）\", \"conclusion\": \"success\", \"metrics\": {\"model\": \"OLMo-2-0425-1B (1485M)\", \"datasets\": {\"depth0_only\": {\"train\": 797, \"test\": 3138}, \"depth01\": {\"train\": 3951, \"test\": 3138}, \"all\": {\"train\": 12299, \"test\": 3138}, \"size_matched\": {\"train\": 3951, \"test\": 3138}, \"binary_filtered\": {\"train\": 3951, \"test\": 3138}}, \"dry_run_loss\": 2.18, \"script\": \"finetune_downstream.py\"}}, \"plan-001-restore\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-14T19:14:00.170Z\", \"updated_at\": \"2026-05-15T00:19:35.359Z\", \"notes\": \"历史遗留条目，实际已由 plan-001-fix 完成覆盖。可忽略。\"}, \"mvp-001-gen-s0\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-14T17:23:13.139Z\", \"updated_at\": \"2026-05-15T00:19:34.474Z\", \"notes\": \"历史遗留条目，实际已由 mvp-001 完成覆盖。可忽略。\"}, \"plan-003\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T23:58:40.949Z\", \"updated_at\": \"2026-05-15T00:09:28.999Z\", \"hypothesis\": \"跨家族参考模型伪证化：用 OLMo-2-1B 和 Qwen3-0.6B 作参考模型提取特征，验证 differential depth response 非 Pythia 特异\", \"conclusion\": \"success\", \"metrics\": {\"logo_f1_pythia_ref\": 0.8034, \"logo_f1_olmo_ref\": 0.8072, \"logo_f1_qwen_ref\": 0.8158, \"entropy_drift_all_refs_negative\": true, \"olmo_ref_drift_range\": [-0.608, -0.9089], \"qwen_ref_drift_range\": [-0.9557, -1.3458], \"pythia_ref_drift_range\": [-1.1872, -1.4017], \"dual_dynamics_is_pythia_artifact\": false}}, \"plan-013\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T23:33:25.590Z\", \"updated_at\": \"2026-05-14T23:53:38.901Z\", \"hypothesis\": \"文本长度混淆控制：深度特征的区分力是否独立于文本长度变化（长度归一化后趋势是否保持）\", \"conclusion\": \"success\", \"metrics\": {\"spearman_rho_range\": \"[-0.066, +0.134]\", \"length_depth_correlation\": \"weak (|ρ|<0.14)\", \"normalized_ttr_trend_preserved\": true, \"normalized_hapax_trend_preserved\": true, \"normalized_rho_stronger\": true, \"length_matched_f1_delta\": \"+0.041\", \"length_is_confound\": false, \"dropout_short_text_bias\": true}}, \"plan-002\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T20:08:55.258Z\", \"updated_at\": \"2026-05-14T23:19:42.066Z\", \"hypothesis\": \"跨模型泛化：Pythia-410M 参考模型下的深度特征能否区分不同架构/规模生成器（Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B）的 continuation 链\", \"conclusion\": \"success\", \"metrics\": {\"total_records\": 18423, \"models\": 4, \"pythia_1b\": {\"records\": 4555, \"seeds\": 995, \"file\": \"data/pythia-1b/generations.jsonl\"}, \"olmo_2_1b\": {\"records\": 4713, \"seeds\": 995, \"file\": \"data/olmo-2-1b/generations.jsonl\"}, \"qwen3_0_6b\": {\"records\": 4538, \"seeds\": 996, \"depth_dist\": {\"gen0\": 996, \"gen1\": 986, \"gen2\": 938, \"gen3\": 840, \"gen4\": 778}, \"file\": \"data/qwen3-0.6b/generations.jsonl\"}, \"qwen3_1_7b\": {\"records\": 4617, \"seeds\": 996, \"depth_dist\": {\"gen0\": 996, \"gen1\": 983, \"gen2\": 941, \"gen3\": 875, \"gen4\": 822}, \"file\": \"data/qwen3-1.7b/generations.jsonl\"}}}, \"plan-002-qwen17b-retry-s1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T21:25:19.756Z\", \"updated_at\": \"2026-05-14T22:24:07.274Z\", \"conclusion\": \"failed\", \"notes\": \"r2 进程 PID 120694 存活，resume 从 seed 143 继续。之前 failed 标记是对旧 retry 进程的判断，r2 是新提交。ETA ~07:30 UTC\"}, \"plan-002-qwen17b-retry-s0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T21:25:18.048Z\", \"updated_at\": \"2026-05-14T22:24:06.388Z\", \"conclusion\": \"failed\", \"notes\": \"r2 进程 PID 120617 存活，resume 从 seed 154 继续。之前 failed 标记是对旧 retry 进程的判断，r2 是新提交。ETA ~07:20 UTC\"}, \"plan-002-qwen06b-s1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T21:25:23.092Z\", \"updated_at\": \"2026-05-14T22:07:37.394Z\", \"conclusion\": \"failed\", \"notes\": \"失败原因: 进程在 218/498 seeds (44%) 正常运行中被外部终止，日志无任何 Python/CUDA 错误。与 s0 和 Qwen3-1.7B 同一 tmux session 死亡模式。系统性 tmux 问题。\"}, \"plan-002-qwen06b-s0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T21:25:21.697Z\", \"updated_at\": \"2026-05-14T22:07:33.758Z\", \"conclusion\": \"failed\", \"notes\": \"失败原因: 进程在 226/498 seeds (45%) 正常运行中被外部终止，日志无任何 Python/CUDA 错误。与 Qwen3-1.7B 同一 tmux session 死亡模式。系统性 tmux 问题，非代码问题。诊断 Worker worker_diagnose_tmux-death-root-cause_20260514T220718 正在深查。\"}, \"plan-002-qwen17b-s1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T20:53:21.708Z\", \"updated_at\": \"2026-05-14T21:53:51.130Z\", \"conclusion\": \"failed\", \"notes\": \"重复提交（与 plan-002-qwen3-1_7b-s1 冲突），争抢 cuda:1 + 写同一输出文件。已 kill。\"}, \"plan-002-qwen17b-s0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T20:53:19.356Z\", \"updated_at\": \"2026-05-14T21:53:49.671Z\", \"conclusion\": \"failed\", \"notes\": \"重复提交（与 plan-002-qwen3-1_7b-s0 冲突），争抢 cuda:0 + 写同一输出文件。已 kill。\"}, \"plan-002-qwen3-1_7b-s0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T20:52:58.460Z\", \"updated_at\": \"2026-05-14T21:53:48.299Z\", \"conclusion\": \"failed\", \"notes\": \"失败原因: SIGHUP (EXIT_CODE=129)，运行 ~21min 后被外部终止。日志无 Python/CUDA 错误，进度正常（104/498 seeds）。同时 s1 也被 SIGHUP。OLMo-2 (cuda:2/3) 不受影响 → 非服务器重启。诊断 Worker worker_diagnose_plan-002-qwen3-1_7b_20260514T211526 正在排查。\"}, \"plan-002-qwen3-1_7b-s1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T20:53:00.298Z\", \"updated_at\": \"2026-05-14T21:33:26.442Z\", \"conclusion\": \"killed\", \"notes\": \"失败原因: SIGHUP (EXIT_CODE=129)，运行 ~21min 后被外部终止。日志无 Python/CUDA 错误，进度正常（95/498 seeds）。与 s0 同时被终止。诊断 Worker 正在排查。\"}, \"plan-001\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T18:25:29.824Z\", \"updated_at\": \"2026-05-14T19:34:17.597Z\", \"hypothesis\": \"Feature ablation: 模型级特征（entropy系列+tail_decay）独立于表面特征仍能区分生成深度；H1/H2趋势分析确认特征随depth的变化模式；perplexity随depth显著变化\", \"conclusion\": \"success\", \"metrics\": {\"note\": \"initial_run_partial_issues_fixed_in_plan-001-fix\", \"ablation_full_macro_f1\": 0.82, \"ablation_surface_only_f1\": 0.76, \"ablation_reference_only_f1\": 0.72}}, \"mvp-001\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T16:17:16.218Z\", \"updated_at\": \"2026-05-14T18:08:20.940Z\", \"hypothesis\": \"Pythia-410M 参考模型的分布特征（entropy stats, tail-decay, TTR, hapax）能区分 Pythia-2.8B continuation 链的 gen-0/gen-1/gen-2+，3-class macro-F1 ≥ 0.45\", \"conclusion\": \"success\", \"metrics\": {\"macro_f1\": 0.8408, \"binary_f1_gen0_vs_gen2plus\": 0.8653, \"cv_macro_f1\": 0.806, \"cv_std\": 0.013, \"gen0_f1\": 0.9517, \"gen1_f1\": 0.7759, \"gen2plus_f1\": 0.7947, \"total_records\": 4609, \"seeds_used\": 995, \"skipped\": 173}}, \"mvp-001-gen-s3\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-14T17:23:17.526Z\", \"updated_at\": \"2026-05-14T17:25:51.261Z\", \"conclusion\": \"failed\", \"notes\": \"失败原因: CUDA error: invalid device ordinal — submit_training_job 注入 CUDA_VISIBLE_DEVICES 后脚本只能看到 cuda:0，但命令用了 --device cuda:3 | 修复: --device 应始终为 cuda:0\"}, \"mvp-001-gen-s2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-14T17:23:15.855Z\", \"updated_at\": \"2026-05-14T17:25:50.275Z\", \"conclusion\": \"failed\", \"notes\": \"失败原因: CUDA error: invalid device ordinal — submit_training_job 注入 CUDA_VISIBLE_DEVICES 后脚本只能看到 cuda:0，但命令用了 --device cuda:2 | 修复: --device 应始终为 cuda:0\"}, \"mvp-001-gen-s1\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-14T17:23:14.464Z\", \"updated_at\": \"2026-05-14T17:25:48.863Z\", \"conclusion\": \"failed\", \"notes\": \"失败原因: CUDA error: invalid device ordinal — submit_training_job 注入 CUDA_VISIBLE_DEVICES 后脚本只能看到 cuda:0，但命令用了 --device cuda:1 | 修复: --device 应始终为 cuda:0\"}}, \"count\": 56, \"total\": 56, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1594}}"
    }
  },
  "sourceToolAssistantUUID": "036343ae-8380-4087-9a82-8be981fc7a27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth"
}
```

</details>

---


### Tool result

_source line 3145 · 2026-05-19T05:24:58.305Z_

<details><summary>↩ Tool result · `toolu_018xqGBNNyJ6bgt8RXuasNLY`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__reconcile_crons"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_roadmap"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a25427c2-195e-48b4-ae13-5ef484b137dc",
  "isSidechain": false,
  "promptId": "0ff41a4b-161b-457c-85f3-287146dda57a",
  "type": "user",
  "uuid": "51d2c36e-08d0-444d-8846-4b24f4ec36ae",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__reconcile_crons",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_roadmap"
    ],
    "query": "select:mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap",
    "total_deferred_tools": 82
  },
  "sourceToolAssistantUUID": "a25427c2-195e-48b4-ae13-5ef484b137dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth"
}
```

</details>

---


### Tool call

_source line 3146 · 2026-05-19T05:24:58.300Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018xqGBNNyJ6bgt8RXuasNLY`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98127156-d719-4295-9bf7-b40c4bc571e0",
  "isSidechain": false,
  "requestId": "req_011CbBNTUi5Ek1W56mvgjghY",
  "type": "assistant",
  "uuid": "a25427c2-195e-48b4-ae13-5ef484b137dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01APnksHxR23L8YpmTrTn1rP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 119,
      "cache_read_input_tokens": 106652,
      "output_tokens": 196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 119,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 196,
          "cache_read_input_tokens": 106652,
          "cache_creation_input_tokens": 119,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 119
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Runtime record

_source line 3147 · 2026-05-19T05:24:58.328Z_

```json
{
  "parentUuid": "51d2c36e-08d0-444d-8846-4b24f4ec36ae",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "5fcbdcea-677f-4927-ab61-6edc82dbd9e2",
  "timestamp": "2026-05-19T05:24:58.328Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth"
}
```

---


### Runtime record

_source line 3148_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[服务器重启后首条消息] 当前日期: 2026-05-19。服务器刚重启，项目状态可能已更新。不要依赖对话历史中的状态信息，以 registry 当前值为准。  **用户消息：** [系统通知] 服务重启，自动恢复 ralph loop。",
  "leafUuid": "5fcbdcea-677f-4927-ab61-6edc82dbd9e2",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96"
}
```

---


### Runtime record

_source line 3149_

```json
{
  "type": "ai-title",
  "aiTitle": "Await worker callbacks and sync paper updates",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96"
}
```

---


### Tool call

_source line 3150 · 2026-05-19T05:25:01.199Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__reconcile_crons · `toolu_01KkziZnb8QgkfkJMmYFqgbd`</summary>

```json
{}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5fcbdcea-677f-4927-ab61-6edc82dbd9e2",
  "isSidechain": false,
  "requestId": "req_011CbBNTphMnKQPJGHqiqvWF",
  "type": "assistant",
  "uuid": "7d7404ab-6825-4ddc-953c-c9f20d0c274c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CeRfhRGtqYeNZTF71kKhTk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19382,
      "cache_read_input_tokens": 106771,
      "output_tokens": 169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19382,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 169,
          "cache_read_input_tokens": 106771,
          "cache_creation_input_tokens": 19382,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19382
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 3151 · 2026-05-19T05:25:01.293Z_

<details><summary>↩ Tool result · `toolu_01KkziZnb8QgkfkJMmYFqgbd`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"reconciled\": 0, \"results\": []}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d7404ab-6825-4ddc-953c-c9f20d0c274c",
  "isSidechain": false,
  "promptId": "0ff41a4b-161b-457c-85f3-287146dda57a",
  "type": "user",
  "uuid": "3bd28bb4-f4fd-4b52-9eb2-19978aae9272",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"reconciled\\\": 0, \\\"results\\\": []}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"reconciled\": 0, \"results\": []}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "7d7404ab-6825-4ddc-953c-c9f20d0c274c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth"
}
```

</details>

---


### Tool call

_source line 3152 · 2026-05-19T05:25:02.209Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Hb88VFkN2zS5iLroA9bbAM`</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3bd28bb4-f4fd-4b52-9eb2-19978aae9272",
  "isSidechain": false,
  "requestId": "req_011CbBNTphMnKQPJGHqiqvWF",
  "type": "assistant",
  "uuid": "b4c21154-632e-426a-a56f-7afada66b5e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CeRfhRGtqYeNZTF71kKhTk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19382,
      "cache_read_input_tokens": 106771,
      "output_tokens": 169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19382,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 169,
          "cache_read_input_tokens": 106771,
          "cache_creation_input_tokens": 19382,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19382
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 3153 · 2026-05-19T05:25:02.220Z_

<details><summary>↩ Tool result · `toolu_01Hb88VFkN2zS5iLroA9bbAM`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/report.md\", \"content\": \"# Handover — 2026-05-18\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- 提交前最终检查（OpenReview form, AI disclosure）\\n\\n## 温度扩展实验结果（全部完成，已写入论文）\\n| Model | Temp | Binary F1 | 95% CI | ρ(ent_mean) |\\n|-------|------|-----------|--------|-------------|\\n| Pythia-2.8B | 0.5 | 0.814 | [.798,.828] | −0.584 |\\n| Pythia-2.8B | 0.7 | 0.740 | [.707,.742] | −0.600 |\\n| Pythia-2.8B | 0.9 | 0.480 | [.465,.498] | −0.302 |\\n| Qwen3-1.7B | 0.5 | 0.751 | — | −0.600 |\\n| Qwen3-1.7B | 0.7 | 0.751 | — | −0.600 |\\n| Qwen3-1.7B | 0.9 | 0.566 | — | −0.370 |\\n| OLMo-2-1B | 0.5 | 0.783 | [.768,.798] | −0.719 |\\n| OLMo-2-1B | 0.7 | 0.695 | [.679,.711] | −0.600 |\\n| OLMo-2-1B | 0.9 | 0.453 | [.437,.469] | −0.261 |\\n| Qwen3-0.6B | 0.5 | 0.711 | [.694,.729] | −0.669 |\\n| Qwen3-0.6B | 0.7 | 0.691 | [.673,.709] | −0.600 |\\n| Qwen3-0.6B | 0.9 | 0.598 | [.582,.615] | −0.294 |\\n\\n## 其他近期结论\\n- **exp_051_independent_seed** (success): Avg binary F1=0.680，已写入 results.tex\\n- **exp_054_instruct_llama** (数据完成): Within-CV binary F1=0.838, ρ 翻转至 +0.230\\n\\n## 论文状态\\n全部编辑完成，编译 0 errors，27 页。\\n- 温度消融表已包含 4 generators × 3 temperatures（appendix_classifier.tex）\\n- Discussion instruct 段落扩充到 4 句（3-family 数据）\\n- appendix_tost.tex（8×7 per-generator TOST table）\\n- appendix_classifier.tex OLMo 版本脚注\\n- ARR Responsible NLP Checklist 已起草（checklist.md）\\n- Placeholder 检查通过（0 matches for XX/TBD/TODO/PLACEHOLDER/FIXME）\\n- exp_051 independent-seed 数据已写入 results.tex\\n\\n## 趋势\\n成功 33 / 负向 1 / 失败 10 / 共 56\\n\\n## 资源状态\\nbjb2-18868: 4x RTX 5090 32GB，全部空闲（2026-05-18 确认）\\nautodl-5090: 已下线\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 1522, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b4c21154-632e-426a-a56f-7afada66b5e8",
  "isSidechain": false,
  "promptId": "0ff41a4b-161b-457c-85f3-287146dda57a",
  "type": "user",
  "uuid": "b6ab7a73-5ab7-4986-9a79-afc125e43fb7",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/report.md\\\", \\\"content\\\": \\\"# Handover — 2026-05-18\\\\n\\\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\\\n\\\\n## 运行中\\\\n（无）\\\\n\\\\n## 待处理\\\\n- 提交前最终检查（OpenReview form, AI disclosure）\\\\n\\\\n## 温度扩展实验结果（全部完成，已写入论文）\\\\n| Model | Temp | Binary F1 | 95% CI | ρ(ent_mean) |\\\\n|-------|------|-----------|--------|-------------|\\\\n| Pythia-2.8B | 0.5 | 0.814 | [.798,.828] | −0.584 |\\\\n| Pythia-2.8B | 0.7 | 0.740 | [.707,.742] | −0.600 |\\\\n| Pythia-2.8B | 0.9 | 0.480 | [.465,.498] | −0.302 |\\\\n| Qwen3-1.7B | 0.5 | 0.751 | — | −0.600 |\\\\n| Qwen3-1.7B | 0.7 | 0.751 | — | −0.600 |\\\\n| Qwen3-1.7B | 0.9 | 0.566 | — | −0.370 |\\\\n| OLMo-2-1B | 0.5 | 0.783 | [.768,.798] | −0.719 |\\\\n| OLMo-2-1B | 0.7 | 0.695 | [.679,.711] | −0.600 |\\\\n| OLMo-2-1B | 0.9 | 0.453 | [.437,.469] | −0.261 |\\\\n| Qwen3-0.6B | 0.5 | 0.711 | [.694,.729] | −0.669 |\\\\n| Qwen3-0.6B | 0.7 | 0.691 | [.673,.709] | −0.600 |\\\\n| Qwen3-0.6B | 0.9 | 0.598 | [.582,.615] | −0.294 |\\\\n\\\\n## 其他近期结论\\\\n- **exp_051_independent_seed** (success): Avg binary F1=0.680，已写入 results.tex\\\\n- **exp_054_instruct_llama** (数据完成): Within-CV binary F1=0.838, ρ 翻转至 +0.230\\\\n\\\\n## 论文状态\\\\n全部编辑完成，编译 0 errors，27 页。\\\\n- 温度消融表已包含 4 generators × 3 temperatures（appendix_classifier.tex）\\\\n- Discussion instruct 段落扩充到 4 句（3-family 数据）\\\\n- appendix_tost.tex（8×7 per-generator TOST table）\\\\n- appendix_classifier.tex OLMo 版本脚注\\\\n- ARR Responsible NLP Checklist 已起草（checklist.md）\\\\n- Placeholder 检查通过（0 matches for XX/TBD/TODO/PLACEHOLDER/FIXME）\\\\n- exp_051 independent-seed 数据已写入 results.tex\\\\n\\\\n## 趋势\\\\n成功 33 / 负向 1 / 失败 10 / 共 56\\\\n\\\\n## 资源状态\\\\nbjb2-18868: 4x RTX 5090 32GB，全部空闲（2026-05-18 确认）\\\\nautodl-5090: 已下线\\\\n\\\\n## 告警\\\\n（无）\\\\n\\\", \\\"total_chars\\\": 1522, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/report.md\", \"content\": \"# Handover — 2026-05-18\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- 提交前最终检查（OpenReview form, AI disclosure）\\n\\n## 温度扩展实验结果（全部完成，已写入论文）\\n| Model | Temp | Binary F1 | 95% CI | ρ(ent_mean) |\\n|-------|------|-----------|--------|-------------|\\n| Pythia-2.8B | 0.5 | 0.814 | [.798,.828] | −0.584 |\\n| Pythia-2.8B | 0.7 | 0.740 | [.707,.742] | −0.600 |\\n| Pythia-2.8B | 0.9 | 0.480 | [.465,.498] | −0.302 |\\n| Qwen3-1.7B | 0.5 | 0.751 | — | −0.600 |\\n| Qwen3-1.7B | 0.7 | 0.751 | — | −0.600 |\\n| Qwen3-1.7B | 0.9 | 0.566 | — | −0.370 |\\n| OLMo-2-1B | 0.5 | 0.783 | [.768,.798] | −0.719 |\\n| OLMo-2-1B | 0.7 | 0.695 | [.679,.711] | −0.600 |\\n| OLMo-2-1B | 0.9 | 0.453 | [.437,.469] | −0.261 |\\n| Qwen3-0.6B | 0.5 | 0.711 | [.694,.729] | −0.669 |\\n| Qwen3-0.6B | 0.7 | 0.691 | [.673,.709] | −0.600 |\\n| Qwen3-0.6B | 0.9 | 0.598 | [.582,.615] | −0.294 |\\n\\n## 其他近期结论\\n- **exp_051_independent_seed** (success): Avg binary F1=0.680，已写入 results.tex\\n- **exp_054_instruct_llama** (数据完成): Within-CV binary F1=0.838, ρ 翻转至 +0.230\\n\\n## 论文状态\\n全部编辑完成，编译 0 errors，27 页。\\n- 温度消融表已包含 4 generators × 3 temperatures（appendix_classifier.tex）\\n- Discussion instruct 段落扩充到 4 句（3-family 数据）\\n- appendix_tost.tex（8×7 per-generator TOST table）\\n- appendix_classifier.tex OLMo 版本脚注\\n- ARR Responsible NLP Checklist 已起草（checklist.md）\\n- Placeholder 检查通过（0 matches for XX/TBD/TODO/PLACEHOLDER/FIXME）\\n- exp_051 independent-seed 数据已写入 results.tex\\n\\n## 趋势\\n成功 33 / 负向 1 / 失败 10 / 共 56\\n\\n## 资源状态\\nbjb2-18868: 4x RTX 5090 32GB，全部空闲（2026-05-18 确认）\\nautodl-5090: 已下线\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 1522, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "b4c21154-632e-426a-a56f-7afada66b5e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth"
}
```

</details>

---


### Tool call

_source line 3154 · 2026-05-19T05:25:02.231Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_roadmap · `toolu_019UqPu3N3D871sDVaZRkR9b`</summary>

```json
{
  "project": "gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6ab7a73-5ab7-4986-9a79-afc125e43fb7",
  "isSidechain": false,
  "requestId": "req_011CbBNTphMnKQPJGHqiqvWF",
  "type": "assistant",
  "uuid": "02040c45-2bf0-4156-84b2-3d21bd6ed832",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CeRfhRGtqYeNZTF71kKhTk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19382,
      "cache_read_input_tokens": 106771,
      "output_tokens": 169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19382,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 169,
          "cache_read_input_tokens": 106771,
          "cache_creation_input_tokens": 19382,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19382
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 3155 · 2026-05-19T05:25:02.244Z_

<details><summary>↩ Tool result · `toolu_019UqPu3N3D871sDVaZRkR9b`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/ROADMAP.md\", \"content\": \"# gen-depth-fingerprint — Research Dashboard\\n\\n> 最后更新: 2026-05-19 02:04 UTC | 更新原因: R21 fixes all landed, page count confirmed ≤8, R22 submitted, ROADMAP synced\\n\\n> 详见 paper_framing.md\\n\\n## 核心方向\\n递归 LLM 生成链展现 **differential depth response (DDR)**：central-tendency/diversity 特征随深度漂移，shape 特征近稳态。7-feature ensemble 跨 8 generators / 5 families / 3 prompt types / 4 domains 验证。**Primary metric: LOGO binary F1=0.694 (leak-free), cross-model 0.764 (5-gen subset)。**\\n\\n## 投稿目标\\n- **主投: EMNLP 2026 ARR (DDL: 2026-05-25)** — 6 天\\n- **定位: Findings track**（R21 Overall 3.0, 报告称可达 3.5 if MF1/MF2/MF4/SF5 fixed）\\n\\n## 当前进展\\n- **阶段**: R21 全部文本修复已落地 → R22 continue-mode 审稿已提交（待审批）\\n- **审稿历程**: R1-R21, 稳定在 3.0 (Findings)。R21 的 6 MF + 10 SF 全部处理完毕\\n- **论文版本**: 正文 8.0 页（Conclusion 在 p8 右栏结束，Limitations 从 p8 右栏中部开始不计入限制）✅\\n- **编译**: 0 errors, 0 undefined refs\\n- **实验**: 33+ 成功 / ~62h GPU consumed\\n\\n## R21 修复状态\\n\\n### 已完成 ✅\\n- MF1: §4.2 clustering 引用精确化（k=2 binary split vs 3/1/3 domain-informed）\\n- MF2: Contribution 2 保持 confident tone，仅加 \\\"in base models\\\" scope\\n- MF3: SF1 baseline insight 加入 §4.3（detection scores implicitly encode depth）\\n- MF4: 保持 \\\"implications\\\" 用词（Reviewer 确认正确）\\n- MF5: Abstract + Contribution 2 加 base-model scope\\n- MF6: Limitations 更新引用 t=0.7 cross-domain 数据（已有于 appendix_domain.tex）\\n- SF5: 正文压缩至 ≤8 页（method §3.3 压缩, results §4.1/§4.2/§4.3 压缩, Fig 2 移至 appendix）\\n- SF9: Discussion 加 QLoRA vs handcrafted 讨论\\n- R1-W4: seed variance near-zero 解释（deterministic LOGO splits）\\n- R21-M1: Related work 加 SemEval Subtask B 引用\\n- R21-M2: 删除 orphan radar bib entry\\n- review_issues.yaml 全面更新\\n\\n### 遗留/deferred\\n- SF3: cross-reference DDR partition structure（数据在已关闭的 autodl-5090，用 Table 4 间接证据替代）\\n- R2-W2: cross-domain t=0.7 补充实验（DDL 前无法完成，Limitations 已说明 confound）\\n\\n## 近期任务\\n- [ ] 等待 R22 审稿报告\\n- [ ] R22 反馈后评估是否需要微调\\n- [ ] 最终投稿准备（checklist, ethics statement, formatting）\\n\\n## GPU 预算\\n- 分配: 4× RTX 5090 (autodl-5090) — 服务器已关闭\\n- 已消耗: ~62h\\n- 当前无 GPU 需求（剩余全为文本修改）\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D025 | 2026-05-19 | R22 action matrix: Glass's Δ/Cliff's δ computed, f | — |\\n| D024 | 2026-05-19 | R21 action matrix: text-only fixes addressing 6 MF | — |\\n| D023 | 2026-05-19 | R20 action matrix: keep 3/1/3 DDR partition, add h | — |\\n| D022 | 2026-05-18 | Instruct ρ 反转定位 Discussion C+（4-5 句），不升级核心 claim | exp_052_instruct_qwen3_1_7b, exp_053_instruct_olmo2_1b |\\n| D021 | 2026-05-17 | Title 加 \\\"Base\\\"：从 \\\"in LLM Text Chains\\\" 改为 \\\"in Base  | — |\\n| D020 | 2026-05-17 | D020: N1 grid search 确认 7-feature 非最优 — 改为 efficie | review-exp-a-baseline-ensemble |\\n| D019 | 2026-05-17 | D019: Round 7 审稿处理 — 保持 0.809 headline, Table 4 gr | plan-015-v2, plan-004-v2 |\\n| D018 | 2026-05-17 | D018: Headline metric 统一为 3-class F1（0.809 cross-m | plan-001, multi-domain-seeds |\\n| D017 | 2026-05-17 | D017: Multi-domain seeds 成功 — depth signal ���域验证通 | multi-domain-seeds |\\n| D016 | 2026-05-17 | D016: 启动 multi-domain seeds 实验 + error analysis ap | plan-010-robustness, error-analysis |\\n\\n\", \"lines\": 66}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "02040c45-2bf0-4156-84b2-3d21bd6ed832",
  "isSidechain": false,
  "promptId": "0ff41a4b-161b-457c-85f3-287146dda57a",
  "type": "user",
  "uuid": "bc708096-8bb9-4fe3-a476-9a7c2c572459",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/ROADMAP.md\\\", \\\"content\\\": \\\"# gen-depth-fingerprint — Research Dashboard\\\\n\\\\n> 最后更新: 2026-05-19 02:04 UTC | 更新原因: R21 fixes all landed, page count confirmed ≤8, R22 submitted, ROADMAP synced\\\\n\\\\n> 详见 paper_framing.md\\\\n\\\\n## 核心方向\\\\n递归 LLM 生成链展现 **differential depth response (DDR)**：central-tendency/diversity 特征随深度漂移，shape 特征近稳态。7-feature ensemble 跨 8 generators / 5 families / 3 prompt types / 4 domains 验证。**Primary metric: LOGO binary F1=0.694 (leak-free), cross-model 0.764 (5-gen subset)。**\\\\n\\\\n## 投稿目标\\\\n- **主投: EMNLP 2026 ARR (DDL: 2026-05-25)** — 6 天\\\\n- **定位: Findings track**（R21 Overall 3.0, 报告称可达 3.5 if MF1/MF2/MF4/SF5 fixed）\\\\n\\\\n## 当前进展\\\\n- **阶段**: R21 全部文本修复已落地 → R22 continue-mode 审稿已提交（待审批）\\\\n- **审稿历程**: R1-R21, 稳定在 3.0 (Findings)。R21 的 6 MF + 10 SF 全部处理完毕\\\\n- **论文版本**: 正文 8.0 页（Conclusion 在 p8 右栏结束，Limitations 从 p8 右栏中部开始不计入限制）✅\\\\n- **编译**: 0 errors, 0 undefined refs\\\\n- **实验**: 33+ 成功 / ~62h GPU consumed\\\\n\\\\n## R21 修复状态\\\\n\\\\n### 已完成 ✅\\\\n- MF1: §4.2 clustering 引用精确化（k=2 binary split vs 3/1/3 domain-informed）\\\\n- MF2: Contribution 2 保持 confident tone，仅加 \\\\\\\"in base models\\\\\\\" scope\\\\n- MF3: SF1 baseline insight 加入 §4.3（detection scores implicitly encode depth）\\\\n- MF4: 保持 \\\\\\\"implications\\\\\\\" 用词（Reviewer 确认正确）\\\\n- MF5: Abstract + Contribution 2 加 base-model scope\\\\n- MF6: Limitations 更新引用 t=0.7 cross-domain 数据（已有于 appendix_domain.tex）\\\\n- SF5: 正文压缩至 ≤8 页（method §3.3 压缩, results §4.1/§4.2/§4.3 压缩, Fig 2 移至 appendix）\\\\n- SF9: Discussion 加 QLoRA vs handcrafted 讨论\\\\n- R1-W4: seed variance near-zero 解释（deterministic LOGO splits）\\\\n- R21-M1: Related work 加 SemEval Subtask B 引用\\\\n- R21-M2: 删除 orphan radar bib entry\\\\n- review_issues.yaml 全面更新\\\\n\\\\n### 遗留/deferred\\\\n- SF3: cross-reference DDR partition structure（数据在已关闭的 autodl-5090，用 Table 4 间接证据替代）\\\\n- R2-W2: cross-domain t=0.7 补充实验（DDL 前无法完成，Limitations 已说明 confound）\\\\n\\\\n## 近期任务\\\\n- [ ] 等待 R22 审稿报告\\\\n- [ ] R22 反馈后评估是否需要微调\\\\n- [ ] 最终投稿准备（checklist, ethics statement, formatting）\\\\n\\\\n## GPU 预算\\\\n- 分配: 4× RTX 5090 (autodl-5090) — 服务器已关闭\\\\n- 已消耗: ~62h\\\\n- 当前无 GPU 需求（剩余全为文本修改）\\\\n\\\\n## 关键决策日志\\\\n\\\\n| ID | 日期 | 摘要 | 关联实验 |\\\\n|----|------|------|----------|\\\\n| D025 | 2026-05-19 | R22 action matrix: Glass's Δ/Cliff's δ computed, f | — |\\\\n| D024 | 2026-05-19 | R21 action matrix: text-only fixes addressing 6 MF | — |\\\\n| D023 | 2026-05-19 | R20 action matrix: keep 3/1/3 DDR partition, add h | — |\\\\n| D022 | 2026-05-18 | Instruct ρ 反转定位 Discussion C+（4-5 句），不升级核心 claim | exp_052_instruct_qwen3_1_7b, exp_053_instruct_olmo2_1b |\\\\n| D021 | 2026-05-17 | Title 加 \\\\\\\"Base\\\\\\\"：从 \\\\\\\"in LLM Text Chains\\\\\\\" 改为 \\\\\\\"in Base  | — |\\\\n| D020 | 2026-05-17 | D020: N1 grid search 确认 7-feature 非最优 — 改为 efficie | review-exp-a-baseline-ensemble |\\\\n| D019 | 2026-05-17 | D019: Round 7 审稿处理 — 保持 0.809 headline, Table 4 gr | plan-015-v2, plan-004-v2 |\\\\n| D018 | 2026-05-17 | D018: Headline metric 统一为 3-class F1（0.809 cross-m | plan-001, multi-domain-seeds |\\\\n| D017 | 2026-05-17 | D017: Multi-domain seeds 成功 — depth signal ���域验证通 | multi-domain-seeds |\\\\n| D016 | 2026-05-17 | D016: 启动 multi-domain seeds 实验 + error analysis ap | plan-010-robustness, error-analysis |\\\\n\\\\n\\\", \\\"lines\\\": 66}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/ROADMAP.md\", \"content\": \"# gen-depth-fingerprint — Research Dashboard\\n\\n> 最后更新: 2026-05-19 02:04 UTC | 更新原因: R21 fixes all landed, page count confirmed ≤8, R22 submitted, ROADMAP synced\\n\\n> 详见 paper_framing.md\\n\\n## 核心方向\\n递归 LLM 生成链展现 **differential depth response (DDR)**：central-tendency/diversity 特征随深度漂移，shape 特征近稳态。7-feature ensemble 跨 8 generators / 5 families / 3 prompt types / 4 domains 验证。**Primary metric: LOGO binary F1=0.694 (leak-free), cross-model 0.764 (5-gen subset)。**\\n\\n## 投稿目标\\n- **主投: EMNLP 2026 ARR (DDL: 2026-05-25)** — 6 天\\n- **定位: Findings track**（R21 Overall 3.0, 报告称可达 3.5 if MF1/MF2/MF4/SF5 fixed）\\n\\n## 当前进展\\n- **阶段**: R21 全部文本修复已落地 → R22 continue-mode 审稿已提交（待审批）\\n- **审稿历程**: R1-R21, 稳定在 3.0 (Findings)。R21 的 6 MF + 10 SF 全部处理完毕\\n- **论文版本**: 正文 8.0 页（Conclusion 在 p8 右栏结束，Limitations 从 p8 右栏中部开始不计入限制）✅\\n- **编译**: 0 errors, 0 undefined refs\\n- **实验**: 33+ 成功 / ~62h GPU consumed\\n\\n## R21 修复状态\\n\\n### 已完成 ✅\\n- MF1: §4.2 clustering 引用精确化（k=2 binary split vs 3/1/3 domain-informed）\\n- MF2: Contribution 2 保持 confident tone，仅加 \\\"in base models\\\" scope\\n- MF3: SF1 baseline insight 加入 §4.3（detection scores implicitly encode depth）\\n- MF4: 保持 \\\"implications\\\" 用词（Reviewer 确认正确）\\n- MF5: Abstract + Contribution 2 加 base-model scope\\n- MF6: Limitations 更新引用 t=0.7 cross-domain 数据（已有于 appendix_domain.tex）\\n- SF5: 正文压缩至 ≤8 页（method §3.3 压缩, results §4.1/§4.2/§4.3 压缩, Fig 2 移至 appendix）\\n- SF9: Discussion 加 QLoRA vs handcrafted 讨论\\n- R1-W4: seed variance near-zero 解释（deterministic LOGO splits）\\n- R21-M1: Related work 加 SemEval Subtask B 引用\\n- R21-M2: 删除 orphan radar bib entry\\n- review_issues.yaml 全面更新\\n\\n### 遗留/deferred\\n- SF3: cross-reference DDR partition structure（数据在已关闭的 autodl-5090，用 Table 4 间接证据替代）\\n- R2-W2: cross-domain t=0.7 补充实验（DDL 前无法完成，Limitations 已说明 confound）\\n\\n## 近期任务\\n- [ ] 等待 R22 审稿报告\\n- [ ] R22 反馈后评估是否需要微调\\n- [ ] 最终投稿准备（checklist, ethics statement, formatting）\\n\\n## GPU 预算\\n- 分配: 4× RTX 5090 (autodl-5090) — 服务器已关闭\\n- 已消耗: ~62h\\n- 当前无 GPU 需求（剩余全为文本修改）\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D025 | 2026-05-19 | R22 action matrix: Glass's Δ/Cliff's δ computed, f | — |\\n| D024 | 2026-05-19 | R21 action matrix: text-only fixes addressing 6 MF | — |\\n| D023 | 2026-05-19 | R20 action matrix: keep 3/1/3 DDR partition, add h | — |\\n| D022 | 2026-05-18 | Instruct ρ 反转定位 Discussion C+（4-5 句），不升级核心 claim | exp_052_instruct_qwen3_1_7b, exp_053_instruct_olmo2_1b |\\n| D021 | 2026-05-17 | Title 加 \\\"Base\\\"：从 \\\"in LLM Text Chains\\\" 改为 \\\"in Base  | — |\\n| D020 | 2026-05-17 | D020: N1 grid search 确认 7-feature 非最优 — 改为 efficie | review-exp-a-baseline-ensemble |\\n| D019 | 2026-05-17 | D019: Round 7 审稿处理 — 保持 0.809 headline, Table 4 gr | plan-015-v2, plan-004-v2 |\\n| D018 | 2026-05-17 | D018: Headline metric 统一为 3-class F1（0.809 cross-m | plan-001, multi-domain-seeds |\\n| D017 | 2026-05-17 | D017: Multi-domain seeds 成功 — depth signal ���域验证通 | multi-domain-seeds |\\n| D016 | 2026-05-17 | D016: 启动 multi-domain seeds 实验 + error analysis ap | plan-010-robustness, error-analysis |\\n\\n\", \"lines\": 66}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "02040c45-2bf0-4156-84b2-3d21bd6ed832",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth"
}
```

</details>

---


### Assistant

_source line 3156 · 2026-05-19T05:25:09.157Z_

<details><summary>Logged reasoning block</summary>

```text
Session-start initialization complete. State:

- Registry: 56 experiments, 0 running, no active crons
- Report: No running experiments, paper compilation clean
- ROADMAP: R22 审稿已提交待审批, DDL 2026-05-25 (6天后)

The last thing before the server restart was completing R25 instruct analysis and reporting to Director. Everything was done — no pending tasks.

The user message is just a system notification about server restart and auto-resume of ralph loop. No action needed beyond the initialization I just did. Let me report status to Director.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc708096-8bb9-4fe3-a476-9a7c2c572459",
  "isSidechain": false,
  "requestId": "req_011CbBNU7a7MdnZ64y2xKM25",
  "type": "assistant",
  "uuid": "fd021411-c5bf-4017-9e81-b322163cefad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012UJU6VaFB99obDfdR8kASN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3160,
      "cache_read_input_tokens": 126153,
      "output_tokens": 505,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3160,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 505,
          "cache_read_input_tokens": 126153,
          "cache_creation_input_tokens": 3160,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3160
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Assistant

_source line 3157 · 2026-05-19T05:25:12.009Z_

Session-start 初始化完成。

- Registry: 56 实验，0 运行中，0 active crons
- 论文状态: 编译 0 errors，所有 R19/R20/R21 修复已落地
- 最近完成: R25 instruct retrain 分析（结果已报 Director）
- 无待处理回调或 worker

当前无阻塞任务，等待 Director 指令。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd021411-c5bf-4017-9e81-b322163cefad",
  "isSidechain": false,
  "requestId": "req_011CbBNU7a7MdnZ64y2xKM25",
  "type": "assistant",
  "uuid": "139dbc88-c3b4-4be0-9b69-a1bc9296a217",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012UJU6VaFB99obDfdR8kASN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3160,
      "cache_read_input_tokens": 126153,
      "output_tokens": 505,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3160,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 505,
          "cache_read_input_tokens": 126153,
          "cache_creation_input_tokens": 3160,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3160
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 3158 · 2026-05-19T05:25:15.664Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__main_agent_post_to_director · `toolu_01247HSZ4fdDtzd3TBhk8o1F`</summary>

```json
{
  "text": "[资源] GPU 0/0 | Worker 0 (GPU 0 / CPU 0) | 磁盘: N/A\n\n**服务重启后状态同步**\n\n- Registry: 56 实验，0 运行中\n- Crons: 0 active（reconcile 确认）\n- 论文: 编译 0 errors, 32 页\n- 上次完成: R25 instruct retrain + feature ablation 分析（已报告）\n- 无待处理任务\n\n等待下一步指令。",
  "project": "gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "139dbc88-c3b4-4be0-9b69-a1bc9296a217",
  "isSidechain": false,
  "requestId": "req_011CbBNU7a7MdnZ64y2xKM25",
  "type": "assistant",
  "uuid": "52a601db-c3b9-43d5-9ffd-2077b71b5bbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012UJU6VaFB99obDfdR8kASN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3160,
      "cache_read_input_tokens": 126153,
      "output_tokens": 505,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3160,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 505,
          "cache_read_input_tokens": 126153,
          "cache_creation_input_tokens": 3160,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3160
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Runtime record

_source line 3159_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[服务器重启后首条消息] 当前日期: 2026-05-19。服务器刚重启，项目状态可能已更新。不要依赖对话历史中的状态信息，以 registry 当前值为准。  **用户消息：** [系统通知] 服务重启，自动恢复 ralph loop。",
  "leafUuid": "52a601db-c3b9-43d5-9ffd-2077b71b5bbc",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96"
}
```

---


### Runtime record

_source line 3160_

```json
{
  "type": "ai-title",
  "aiTitle": "Await worker callbacks and sync paper updates",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96"
}
```

---


### Tool result

_source line 3161 · 2026-05-19T05:25:19.201Z_

<details><summary>↩ Tool result · `toolu_01247HSZ4fdDtzd3TBhk8o1F`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_dbd68d7879a81efc0c108e9844b15d0b:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52a601db-c3b9-43d5-9ffd-2077b71b5bbc",
  "isSidechain": false,
  "promptId": "0ff41a4b-161b-457c-85f3-287146dda57a",
  "type": "user",
  "uuid": "9d97d4cb-ff7b-4b1b-8904-787a58fb1026",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"director_session\\\": \\\"feishu:group:oc_dbd68d7879a81efc0c108e9844b15d0b:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_dbd68d7879a81efc0c108e9844b15d0b:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "52a601db-c3b9-43d5-9ffd-2077b71b5bbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth"
}
```

</details>

---


### Runtime record

_source line 3162_

```json
{
  "type": "ai-title",
  "aiTitle": "Await worker callbacks and sync paper updates",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96"
}
```

---


### Runtime record

_source line 3163 · 2026-05-19T06:12:52.536Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T06:12:52.536Z",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "content": "[Director 指令] 投稿准备任务（不依赖 R26 审稿结果，现在就做）：\n\n1. **EMNLP 2026 ARR OpenReview 投稿材料清单**：\n   - 查 EMNLP 2026 ARR 的 OpenReview 投稿要求（WebSearch \"EMNLP 2026 ARR submission requirements OpenReview\"）\n   - 确认需要哪些材料：main paper PDF、supplementary materials、Responsible NLP Checklist、Author Response form 等\n   - 列出每项材料的当前状态（已有/需准备/缺失）\n\n2. **Responsible NLP Checklist**：\n   - 如果 EMNLP 2026 要求 Responsible NLP Research Checklist，准备一份完整的回答草稿\n   - 基于论文内容逐条回答（数据来源、人工标注、隐私、计算资源等）\n\n3. **匿名化检查**：\n   - 确认论文 PDF 中无作者身份泄露（文件 metadata、acknowledgments、自引格式等）\n   - 检查 \\documentclass 选项是否正确设置为 review/anonymous 模式\n\n4. **Supplementary 材料**：\n   - 如果附录超过正文页数限制，确认是否需要单独上传\n   - 检查是否需要匿名代码链接\n\n汇报每项的状态和所需行动。"
}
```

---


### Runtime record

_source line 3164 · 2026-05-19T06:12:52.536Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T06:12:52.536Z",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96"
}
```

---


## Round 258

## Round 258

2 recorded events


### User

_source line 3165 · 2026-05-19T06:12:52.527Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d97d4cb-ff7b-4b1b-8904-787a58fb1026",
  "isSidechain": false,
  "promptId": "52fa409d-a131-499b-b76f-82911a2f9bb6",
  "type": "user",
  "isMeta": true,
  "uuid": "d1ec70a8-6a54-4b21-93d6-ce4813e3676c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth"
}
```

</details>

---


### Assistant

_source line 3166 · 2026-05-19T06:12:52.527Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1ec70a8-6a54-4b21-93d6-ce4813e3676c",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "a8a24964-afcb-43a6-af15-5b897df439ed",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth",
  "message": {
    "id": "b9ad7f90-71ca-44eb-9489-fe5a313ecadd",
    "container": null,
    "model": "&lt;synthetic>",
    "stop_reason": "stop_sequence",
    "stop_sequence": "",
    "type": "message",
    "usage": {
      "input_tokens": 0,
      "output_tokens": 0,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 0,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": null,
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": null,
      "iterations": null,
      "speed": null
    },
    "context_management": null
  }
}
```

</details>

---


## Round 259

## Round 259

76 recorded events


### User

_source line 3167 · 2026-05-19T06:12:52.675Z_

[Director 指令] 投稿准备任务（不依赖 R26 审稿结果，现在就做）：

1. **EMNLP 2026 ARR OpenReview 投稿材料清单**：
   - 查 EMNLP 2026 ARR 的 OpenReview 投稿要求（WebSearch "EMNLP 2026 ARR submission requirements OpenReview"）
   - 确认需要哪些材料：main paper PDF、supplementary materials、Responsible NLP Checklist、Author Response form 等
   - 列出每项材料的当前状态（已有/需准备/缺失）

2. **Responsible NLP Checklist**：
   - 如果 EMNLP 2026 要求 Responsible NLP Research Checklist，准备一份完整的回答草稿
   - 基于论文内容逐条回答（数据来源、人工标注、隐私、计算资源等）

3. **匿名化检查**：
   - 确认论文 PDF 中无作者身份泄露（文件 metadata、acknowledgments、自引格式等）
   - 检查 \documentclass 选项是否正确设置为 review/anonymous 模式

4. **Supplementary 材料**：
   - 如果附录超过正文页数限制，确认是否需要单独上传
   - 检查是否需要匿名代码链接

汇报每项的状态和所需行动。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a8a24964-afcb-43a6-af15-5b897df439ed",
  "isSidechain": false,
  "promptId": "52fa409d-a131-499b-b76f-82911a2f9bb6",
  "type": "user",
  "uuid": "8e70402d-bc89-4d06-b4c3-7f7c89ad90a9",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth"
}
```

</details>

---


### Tool call

_source line 3168 · 2026-05-19T06:12:55.770Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_011T7xsG97RjSivfts8S5KNQ`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__spawn_worker",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e70402d-bc89-4d06-b4c3-7f7c89ad90a9",
  "isSidechain": false,
  "requestId": "req_011CbBS7htjkGS4kXefw5Giq",
  "type": "assistant",
  "uuid": "362c7dfe-9526-4b44-be48-6d58125ccd98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015B2BMBc97Y4YQeY5oYgxyb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 430,
      "cache_read_input_tokens": 129892,
      "output_tokens": 86,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 430,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 86,
          "cache_read_input_tokens": 129892,
          "cache_creation_input_tokens": 430,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 430
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 3169 · 2026-05-19T06:12:55.778Z_

<details><summary>↩ Tool result · `toolu_011T7xsG97RjSivfts8S5KNQ`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__spawn_worker"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "362c7dfe-9526-4b44-be48-6d58125ccd98",
  "isSidechain": false,
  "promptId": "52fa409d-a131-499b-b76f-82911a2f9bb6",
  "type": "user",
  "uuid": "350217fe-7223-4b19-af6d-732562f64fee",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__spawn_worker"
    ],
    "query": "select:mcp__agent-ml-research__spawn_worker",
    "total_deferred_tools": 82
  },
  "sourceToolAssistantUUID": "362c7dfe-9526-4b44-be48-6d58125ccd98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth"
}
```

</details>

---


### Assistant

_source line 3170 · 2026-05-19T06:13:05.032Z_

<details><summary>Logged reasoning block</summary>

```text
The Director wants 4 tasks for submission preparation. Let me handle them:

1. EMNLP 2026 ARR submission requirements - needs WebSearch
2. Responsible NLP Checklist - needs paper content knowledge
3. Anonymization check - can do locally
4. Supplementary materials check - can do locally

Tasks 1-2 require WebSearch and paper reading, which are research tasks. Tasks 3-4 are local file checks I can do myself.

Let me spawn a worker for tasks 1-2 (WebSearch + checklist drafting), and do tasks 3-4 myself in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "350217fe-7223-4b19-af6d-732562f64fee",
  "isSidechain": false,
  "requestId": "req_011CbBS7wHeCasbLVnPy7M3i",
  "type": "assistant",
  "uuid": "9dafe3fb-8acd-4aec-b2e3-aa9db417063e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EXFsCNwgHBjkNPqAEbKoJV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1285,
      "cache_read_input_tokens": 130322,
      "output_tokens": 1792,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1285,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1792,
          "cache_read_input_tokens": 130322,
          "cache_creation_input_tokens": 1285,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1285
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---


### Assistant

_source line 3171 · 2026-05-19T06:13:06.570Z_

并行处理：派 Worker 做 WebSearch 查投稿要求 + 起草 Checklist，我同时做匿名化检查和 supplementary 检查。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9dafe3fb-8acd-4aec-b2e3-aa9db417063e",
  "isSidechain": false,
  "requestId": "req_011CbBS7wHeCasbLVnPy7M3i",
  "type": "assistant",
  "uuid": "5b971fe9-5e1a-47b2-90da-446f4c12a6b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EXFsCNwgHBjkNPqAEbKoJV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1285,
      "cache_read_input_tokens": 130322,
      "output_tokens": 1792,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1285,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1792,
          "cache_read_input_tokens": 130322,
          "cache_creation_input_tokens": 1285,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1285
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---


### Tool call

_source line 3172 · 2026-05-19T06:13:25.102Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker · `toolu_01Cw8jfYaENHJvppqjcSJ72s`</summary>

```json
{
  "task_type": "research:emnlp2026-submission-prep",
  "project": "gen-depth-fingerprint",
  "task_prompt": "## 任务：EMNLP 2026 ARR 投稿要求调研 + Responsible NLP Checklist 草稿\n\n### 任务 1：投稿材料清单\n\n1. WebSearch \"EMNLP 2026 ARR submission requirements OpenReview\" 和 \"ACL Rolling Review 2025 2026 submission guidelines checklist\"\n2. 确认 EMNLP 2026 ARR OpenReview 投稿需要提交哪些材料：\n   - Main paper PDF\n   - Supplementary materials (appendix, code, data)\n   - Responsible NLP Research Checklist\n   - 其他（如 Author Response form, ethics statement 等）\n3. 确认每项材料的格式要求（页数限制、文件大小限制、匿名要求等）\n4. 确认 ARR 的 submission form 有哪些必填字段\n\n### 任务 2：Responsible NLP Research Checklist 草稿\n\n基于以下论文信息，逐条回答 ARR Responsible NLP Research Checklist：\n\n**论文概要**：\n- 标题：Depth Profiling: Classifying Recursive Generation Depth in Base LLM Text Chains\n- 任务：用 7 个统计特征（entropy mean/std/min/max, tail_decay, TTR, hapax_ratio）区分 LLM 递归生成链的深度（gen-0/gen-1/gen-2+）\n- 方法：XGBoost classifier + Pythia-410M 作为参考模型提取 differential entropy 特征\n- 数据：自建数据集，Wikipedia seeds → 8 generators (Pythia-2.8B/1B, OLMo-2-1B, Qwen3-0.6B/1.7B/8B, Llama-3.2-3B, Mistral-7B-v0.3) 生成 depth 0-4 chains，~37K texts\n- 评估：Leave-One-Generator-Out (LOGO) cross-validation, binary F1=0.694\n- 无人工标注（数据完全自动生成）\n- 无个人信息/隐私数据\n- 计算资源：4× RTX 5090 32GB，~62 GPU-hours\n- 代码：会提供匿名代码链接\n- 不涉及人类实验\n- 预训练模型来自 HuggingFace（公开模型）\n- Seeds 来自 Wikipedia（CC BY-SA 许可）\n\n请读取现有的 checklist 草稿（如果存在）：\n`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/checklist.md`\n\n然后生成完整的 Responsible NLP Checklist 回答，保存到：\n`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/responsible_nlp_checklist.md`\n\n### 输出要求\n将调研结果保存到：\n`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/submission_requirements.md`\n\n格式：每项材料列出 [状态] 标记（✅已有 / ⚠️需准备 / ❌缺失）",
  "tool_groups": [
    "knowledge"
  ],
  "tools": [
    "WebSearch",
    "WebFetch"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b971fe9-5e1a-47b2-90da-446f4c12a6b7",
  "isSidechain": false,
  "requestId": "req_011CbBS7wHeCasbLVnPy7M3i",
  "type": "assistant",
  "uuid": "01a7a00e-6eff-4244-9643-0a0f10fca694",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EXFsCNwgHBjkNPqAEbKoJV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1285,
      "cache_read_input_tokens": 130322,
      "output_tokens": 1792,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1285,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1792,
          "cache_read_input_tokens": 130322,
          "cache_creation_input_tokens": 1285,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1285
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---


### Tool call

_source line 3173 · 2026-05-19T06:13:26.996Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01G2i6Q5YBChcww8LehKuxs9`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper && grep -n \"\\\\\\\\documentclass\" main.tex && grep -n \"anonymous\\|review\\|author\\|\\\\\\\\name\\|\\\\\\\\affiliation\\|\\\\\\\\institute\\|acknowledgment\" main.tex | head -20",
  "description": "Check anonymization settings in LaTeX"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01a7a00e-6eff-4244-9643-0a0f10fca694",
  "isSidechain": false,
  "requestId": "req_011CbBS7wHeCasbLVnPy7M3i",
  "type": "assistant",
  "uuid": "b065553a-fe36-4f47-8bcc-fc7e43521760",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EXFsCNwgHBjkNPqAEbKoJV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1285,
      "cache_read_input_tokens": 130322,
      "output_tokens": 1792,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1285,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1792,
          "cache_read_input_tokens": 130322,
          "cache_creation_input_tokens": 1285,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1285
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---


### Tool call

_source line 3174 · 2026-05-19T06:13:29.500Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01RfvzoYPLjoqMKPahJA8NC8`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper && python3 -c \"\nimport subprocess\n# Check PDF metadata\nresult = subprocess.run(['pdfinfo', 'main.pdf'], capture_output=True, text=True)\nprint(result.stdout if result.returncode == 0 else 'pdfinfo not available')\n\" 2>&1 || echo \"pdfinfo not found, trying exiftool\" && exiftool main.pdf 2>/dev/null | head -30 || echo \"No metadata tools available\"",
  "description": "Check PDF metadata for author info leaks"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b065553a-fe36-4f47-8bcc-fc7e43521760",
  "isSidechain": false,
  "requestId": "req_011CbBS7wHeCasbLVnPy7M3i",
  "type": "assistant",
  "uuid": "638638ca-1a7a-464d-af43-9800d4cc1487",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EXFsCNwgHBjkNPqAEbKoJV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1285,
      "cache_read_input_tokens": 130322,
      "output_tokens": 1792,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1285,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1792,
          "cache_read_input_tokens": 130322,
          "cache_creation_input_tokens": 1285,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1285
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---


### Tool result

_source line 3175 · 2026-05-19T06:13:31.069Z_

<details><summary>↩ Tool result · `toolu_01Cw8jfYaENHJvppqjcSJ72s`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_research_emnlp2026-submission-prep_20260519T061325\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/logs/workers/worker_research_emnlp2026-submission-prep_20260519T061325.log\", \"setup_data\": {}, \"message\": \"Worker worker_research_emnlp2026-submission-prep_20260519T061325 started. Use get_worker_status('worker_research_emnlp2026-submission-prep_20260519T061325') to check progress.\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "01a7a00e-6eff-4244-9643-0a0f10fca694",
  "isSidechain": false,
  "promptId": "52fa409d-a131-499b-b76f-82911a2f9bb6",
  "type": "user",
  "uuid": "e513f708-f5b1-4ca2-a038-6ae3d9cb5e1e",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"worker_id\\\": \\\"worker_research_emnlp2026-submission-prep_20260519T061325\\\", \\\"status\\\": \\\"running\\\", \\\"log_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/logs/workers/worker_research_emnlp2026-submission-prep_20260519T061325.log\\\", \\\"setup_data\\\": {}, \\\"message\\\": \\\"Worker worker_research_emnlp2026-submission-prep_20260519T061325 started. Use get_worker_status('worker_research_emnlp2026-submission-prep_20260519T061325') to check progress.\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"worker_id\": \"worker_research_emnlp2026-submission-prep_20260519T061325\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/logs/workers/worker_research_emnlp2026-submission-prep_20260519T061325.log\", \"setup_data\": {}, \"message\": \"Worker worker_research_emnlp2026-submission-prep_20260519T061325 started. Use get_worker_status('worker_research_emnlp2026-submission-prep_20260519T061325') to check progress.\"}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "01a7a00e-6eff-4244-9643-0a0f10fca694",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth"
}
```

</details>

---


### Tool result

_source line 3176 · 2026-05-19T06:13:31.216Z_

<details><summary>↩ Tool result · `toolu_01G2i6Q5YBChcww8LehKuxs9`</summary>

```text
2:\documentclass[11pt]{article}
3:\usepackage[review]{acl}
20:\author{Anonymous}
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b065553a-fe36-4f47-8bcc-fc7e43521760",
  "isSidechain": false,
  "promptId": "52fa409d-a131-499b-b76f-82911a2f9bb6",
  "type": "user",
  "uuid": "71526d7f-6874-4d9e-ac66-3668a4c81a42",
  "toolUseResult": {
    "stdout": "2:\\documentclass[11pt]{article}\n3:\\usepackage[review]{acl}\n20:\\author{Anonymous}",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "b065553a-fe36-4f47-8bcc-fc7e43521760",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth"
}
```

</details>

---


### Tool result

_source line 3177 · 2026-05-19T06:13:31.300Z_

<details><summary>↩ Tool result · `toolu_01RfvzoYPLjoqMKPahJA8NC8`</summary>

```text
Title:           
Subject:         
Keywords:        
Author:          
Creator:         LaTeX with hyperref
Producer:        pdfTeX-1.40.28
CreationDate:    Tue May 19 05:39:56 2026 UTC
ModDate:         Tue May 19 05:39:56 2026 UTC
Custom Metadata: yes
Metadata Stream: no
Tagged:          no
UserProperties:  no
Suspects:        no
Form:            none
JavaScript:      no
Pages:           31
Encrypted:       no
Page size:       595.276 x 841.89 pts (A4)
Page rot:        0
File size:       2841671 bytes
Optimized:       no
PDF version:     1.7
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "638638ca-1a7a-464d-af43-9800d4cc1487",
  "isSidechain": false,
  "promptId": "52fa409d-a131-499b-b76f-82911a2f9bb6",
  "type": "user",
  "uuid": "92505950-395d-4b53-8e17-d836d6755de6",
  "toolUseResult": {
    "stdout": "Title:           \nSubject:         \nKeywords:        \nAuthor:          \nCreator:         LaTeX with hyperref\nProducer:        pdfTeX-1.40.28\nCreationDate:    Tue May 19 05:39:56 2026 UTC\nModDate:         Tue May 19 05:39:56 2026 UTC\nCustom Metadata: yes\nMetadata Stream: no\nTagged:          no\nUserProperties:  no\nSuspects:        no\nForm:            none\nJavaScript:      no\nPages:           31\nEncrypted:       no\nPage size:       595.276 x 841.89 pts (A4)\nPage rot:        0\nFile size:       2841671 bytes\nOptimized:       no\nPDF version:     1.7",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "638638ca-1a7a-464d-af43-9800d4cc1487",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth"
}
```

</details>

---


### Tool call

_source line 3178 · 2026-05-19T06:13:31.796Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01HNCTMqqtPUe47Q2EpBNUA7`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper && grep -rn \"\\\\\\\\thanks\\|\\\\\\\\footnote.*author\\|\\\\\\\\footnote.*affil\\|github\\.com\\|huggingface\\.co.*private\\|our previous\\|our earlier\\|we previously\\|Anonymous\\|acknowledgment\\|Acknowledgment\" *.tex | head -20",
  "description": "Search for identity leaks in tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92505950-395d-4b53-8e17-d836d6755de6",
  "isSidechain": false,
  "requestId": "req_011CbBS7wHeCasbLVnPy7M3i",
  "type": "assistant",
  "uuid": "3b65d7a4-c14e-4f68-b10d-1f80bfe5b7d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EXFsCNwgHBjkNPqAEbKoJV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1285,
      "cache_read_input_tokens": 130322,
      "output_tokens": 1792,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1285,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1792,
          "cache_read_input_tokens": 130322,
          "cache_creation_input_tokens": 1285,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1285
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---


### Tool result

_source line 3179 · 2026-05-19T06:13:31.881Z_

<details><summary>↩ Tool result · `toolu_01HNCTMqqtPUe47Q2EpBNUA7`</summary>

```text
main.tex:20:\author{Anonymous}
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b65d7a4-c14e-4f68-b10d-1f80bfe5b7d1",
  "isSidechain": false,
  "promptId": "52fa409d-a131-499b-b76f-82911a2f9bb6",
  "type": "user",
  "uuid": "bf576766-611d-4c33-af4c-cde44afab057",
  "toolUseResult": {
    "stdout": "main.tex:20:\\author{Anonymous}",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "3b65d7a4-c14e-4f68-b10d-1f80bfe5b7d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth"
}
```

</details>

---


### Runtime record

_source line 3180 · 2026-05-19T06:13:31.886Z_

```json
{
  "parentUuid": "bf576766-611d-4c33-af4c-cde44afab057",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "048434ec-9fba-4fae-a09d-c4262a92ec18",
  "timestamp": "2026-05-19T06:13:31.886Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth"
}
```

---


### Assistant

_source line 3181 · 2026-05-19T06:13:38.538Z_

<details><summary>Logged reasoning block</summary>

```text
Good results from the anonymization check:

1. `\documentclass[11pt]{article}` with `\usepackage[review]{acl}` - the `[review]` option enables anonymous mode ✅
2. `\author{Anonymous}` - correct for review ✅
3. PDF metadata: Author field is empty, Title is empty, Creator is "LaTeX with hyperref" - no identity leaks ✅
4. No self-citations, no github links, no acknowledgments found ✅

Now let me check the supplementary materials situation - page count, appendix vs main split, code links.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "048434ec-9fba-4fae-a09d-c4262a92ec18",
  "isSidechain": false,
  "requestId": "req_011CbBSAbWqx19azSEwcfTqo",
  "type": "assistant",
  "uuid": "c01e353d-94c5-4d06-825a-dc5e0965492d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TG9Dx48HXNhtyhnrR5bHfG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3856,
      "cache_read_input_tokens": 130322,
      "output_tokens": 605,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3856,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 605,
          "cache_read_input_tokens": 130322,
          "cache_creation_input_tokens": 3856,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3856
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---


### Assistant

_source line 3182 · 2026-05-19T06:13:38.610Z_

匿名化检查通过。继续检查 supplementary 材料和页数。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c01e353d-94c5-4d06-825a-dc5e0965492d",
  "isSidechain": false,
  "requestId": "req_011CbBSAbWqx19azSEwcfTqo",
  "type": "assistant",
  "uuid": "6d7c36a9-3d1e-4dbf-b37d-291a1c799a03",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TG9Dx48HXNhtyhnrR5bHfG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3856,
      "cache_read_input_tokens": 130322,
      "output_tokens": 605,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3856,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 605,
          "cache_read_input_tokens": 130322,
          "cache_creation_input_tokens": 3856,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3856
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---


### Tool call

_source line 3183 · 2026-05-19T06:13:39.651Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01WCuPtMU2KLckNQtXKEg1n1`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper && python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', 'main.pdf'], capture_output=True, text=True)\nfor line in result.stdout.split('\\n'):\n    if 'Pages' in line:\n        print(line)\n\"",
  "description": "Check total page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d7c36a9-3d1e-4dbf-b37d-291a1c799a03",
  "isSidechain": false,
  "requestId": "req_011CbBSAbWqx19azSEwcfTqo",
  "type": "assistant",
  "uuid": "561b3f65-3f1f-4d53-80ec-e65aec5c9885",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TG9Dx48HXNhtyhnrR5bHfG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3856,
      "cache_read_input_tokens": 130322,
      "output_tokens": 605,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3856,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 605,
          "cache_read_input_tokens": 130322,
          "cache_creation_input_tokens": 3856,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3856
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---


### Tool result

_source line 3184 · 2026-05-19T06:13:39.749Z_

<details><summary>↩ Tool result · `toolu_01WCuPtMU2KLckNQtXKEg1n1`</summary>

```text
Pages:           31
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "561b3f65-3f1f-4d53-80ec-e65aec5c9885",
  "isSidechain": false,
  "promptId": "52fa409d-a131-499b-b76f-82911a2f9bb6",
  "type": "user",
  "uuid": "ceffa70a-261e-4fab-ad5a-18ac4a41d0cc",
  "toolUseResult": {
    "stdout": "Pages:           31",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "561b3f65-3f1f-4d53-80ec-e65aec5c9885",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth"
}
```

</details>

---


### Tool call

_source line 3185 · 2026-05-19T06:13:41.017Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01ExQeiqvzt2h1Y5w5kZN2zm`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper && grep -n \"\\\\\\\\appendix\\|\\\\\\\\bibliography\\|\\\\\\\\section\\|\\\\\\\\end{document}\" main.tex",
  "description": "Check main/appendix/bibliography boundaries"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ceffa70a-261e-4fab-ad5a-18ac4a41d0cc",
  "isSidechain": false,
  "requestId": "req_011CbBSAbWqx19azSEwcfTqo",
  "type": "assistant",
  "uuid": "82eefc67-3e53-4c51-8786-d85aea6b5a5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TG9Dx48HXNhtyhnrR5bHfG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3856,
      "cache_read_input_tokens": 130322,
      "output_tokens": 605,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3856,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 605,
          "cache_read_input_tokens": 130322,
          "cache_creation_input_tokens": 3856,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3856
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---


### Tool result

_source line 3186 · 2026-05-19T06:13:41.055Z_

<details><summary>↩ Tool result · `toolu_01ExQeiqvzt2h1Y5w5kZN2zm`</summary>

```text
37:\bibliography{references}
39:\appendix
47:\section{Length Confound Analysis}
52:\section{Prompt Type Generalization}
57:\section{Finer-Grained Depth Classification}
62:\section{End-to-End Depth Classification (QLoRA)}
67:\section{Leave-One-Feature-Out Analysis}
72:\section{Confusion Matrix}
77:\section{Classifier Sensitivity}
82:\section{Robustness to Text Perturbation}
87:\section{Cross-Domain Generalization}
92:\section{Instruction-Tuned Model Analysis}
97:\section{Error Analysis of Binary Classification}
102:\section{Downstream Utility}
107:\section{Cross-Model Chain Per-Class Detail}
112:\section{Feature Distribution Analysis}
117:\section{Cross-Temperature Transfer}
122:\section{Feature Ablation}
137:\section{Cross-Family Reference Models}
148:\section{DDR Partition Validation}
153:\section{Generator Subset Summary}
160:\end{document}
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "82eefc67-3e53-4c51-8786-d85aea6b5a5f",
  "isSidechain": false,
  "promptId": "52fa409d-a131-499b-b76f-82911a2f9bb6",
  "type": "user",
  "uuid": "50ea703b-341c-4ebb-bfeb-e809261cd977",
  "toolUseResult": {
    "stdout": "37:\\bibliography{references}\n39:\\appendix\n47:\\section{Length Confound Analysis}\n52:\\section{Prompt Type Generalization}\n57:\\section{Finer-Grained Depth Classification}\n62:\\section{End-to-End Depth Classification (QLoRA)}\n67:\\section{Leave-One-Feature-Out Analysis}\n72:\\section{Confusion Matrix}\n77:\\section{Classifier Sensitivity}\n82:\\section{Robustness to Text Perturbation}\n87:\\section{Cross-Domain Generalization}\n92:\\section{Instruction-Tuned Model Analysis}\n97:\\section{Error Analysis of Binary Classification}\n102:\\section{Downstream Utility}\n107:\\section{Cross-Model Chain Per-Class Detail}\n112:\\section{Feature Distribution Analysis}\n117:\\section{Cross-Temperature Transfer}\n122:\\section{Feature Ablation}\n137:\\section{Cross-Family Reference Models}\n148:\\section{DDR Partition Validation}\n153:\\section{Generator Subset Summary}\n160:\\end{document}",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "82eefc67-3e53-4c51-8786-d85aea6b5a5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth"
}
```

</details>

---


### Tool call

_source line 3187 · 2026-05-19T06:13:42.667Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0195gEo5CSksh7FYryQm9xBg`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper && grep -rn \"github\\|code.*available\\|code.*release\\|anonymous.*link\\|supplementary\\|supplement\" *.tex | head -10",
  "description": "Check for code/supplement references in paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50ea703b-341c-4ebb-bfeb-e809261cd977",
  "isSidechain": false,
  "requestId": "req_011CbBSAbWqx19azSEwcfTqo",
  "type": "assistant",
  "uuid": "2a97d10a-aceb-4b04-8cf6-62201db27649",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TG9Dx48HXNhtyhnrR5bHfG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3856,
      "cache_read_input_tokens": 130322,
      "output_tokens": 605,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3856,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 605,
          "cache_read_input_tokens": 130322,
          "cache_creation_input_tokens": 3856,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3856
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---


### Tool result

_source line 3188 · 2026-05-19T06:13:42.726Z_

<details><summary>↩ Tool result · `toolu_0195gEo5CSksh7FYryQm9xBg`</summary>

```text
appendix_ddr_validation.tex:108:To verify that the DDR partition is robust to this heteroscedasticity, we supplement pooled Cohen's $d$ with Glass's $\Delta$ (using the gen-1 standard deviation as denominator) and Cliff's $\delta$ (a non-parametric ordinal effect size; Table~\ref{tab:effect-sizes}).
ethics.tex:9:All code, data, and trained models will be released upon publication.
method.tex:23:We address this with a supplementary binary evaluation excluding gen-0 entirely (\S\ref{sec:results-baselines}).
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a97d10a-aceb-4b04-8cf6-62201db27649",
  "isSidechain": false,
  "promptId": "52fa409d-a131-499b-b76f-82911a2f9bb6",
  "type": "user",
  "uuid": "92e82174-e961-4356-ba31-b0dc415e73ac",
  "toolUseResult": {
    "stdout": "appendix_ddr_validation.tex:108:To verify that the DDR partition is robust to this heteroscedasticity, we supplement pooled Cohen's $d$ with Glass's $\\Delta$ (using the gen-1 standard deviation as denominator) and Cliff's $\\delta$ (a non-parametric ordinal effect size; Table~\\ref{tab:effect-sizes}).\nethics.tex:9:All code, data, and trained models will be released upon publication.\nmethod.tex:23:We address this with a supplementary binary evaluation excluding gen-0 entirely (\\S\\ref{sec:results-baselines}).",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "2a97d10a-aceb-4b04-8cf6-62201db27649",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth"
}
```

</details>

---


### Runtime record

_source line 3189_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] 投稿准备任务（不依赖 R26 审稿结果，现在就做）：  1. **EMNLP 2026 ARR OpenReview 投稿材料清单**：    - 查 EMNLP 2026 ARR 的 OpenReview 投稿要求（WebSearch \"EMNLP 2026 ARR submission requirements OpenReview\"）    - 确认需要哪些材料：…",
  "leafUuid": "92e82174-e961-4356-ba31-b0dc415e73ac",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96"
}
```

---


### Runtime record

_source line 3190_

```json
{
  "type": "ai-title",
  "aiTitle": "Await worker callbacks and sync paper updates",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96"
}
```

---


### Tool call

_source line 3191 · 2026-05-19T06:13:46.234Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LgF9aBCWKVKzWHQYPsGipW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92e82174-e961-4356-ba31-b0dc415e73ac",
  "isSidechain": false,
  "requestId": "req_011CbBSBPq9sDxoSQxEJKmNE",
  "type": "assistant",
  "uuid": "bb84fb2c-bb9a-44ff-8963-f704f0066aaa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NNB9Qd83LpREUpPpt1cQAJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1219,
      "cache_read_input_tokens": 134178,
      "output_tokens": 163,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1219,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 163,
          "cache_read_input_tokens": 134178,
          "cache_creation_input_tokens": 1219,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1219
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 3192 · 2026-05-19T06:13:46.241Z_

<details><summary>↩ Tool result · `toolu_01LgF9aBCWKVKzWHQYPsGipW`</summary>

```text
1	\section*{Ethics Statement}
2	\label{sec:ethics}
3	
4	All texts analyzed in this work are LLM-generated from publicly available Wikipedia seeds; no personal or sensitive data is involved.
5	Our method estimates the generation depth of a text passage (how many recursive generation steps it has undergone), not the identity of its author.
6	Individual authorship attribution is outside both the scope and the capability of this approach; privacy implications are minimal.
7	We acknowledge that depth estimation tools could in principle be used to selectively suppress machine-generated text in contexts where such content is legitimate (e.g., accessibility tools, assistive writing).
8	We encourage deployment in data governance pipelines where provenance transparency, rather than content removal, is the objective.
9	All code, data, and trained models will be released upon publication.
10	
11	\paragraph{Licenses.}
12	All generator models are publicly available under permissive licenses (Apache 2.0 for Pythia, OLMo, and Mistral; Qwen License for Qwen3; Llama Community License for Llama 3.2).
13	Wikipedia seed passages are distributed under CC BY-SA 3.0.
14	
15	\paragraph{Compute budget.}
16	All experiments were conducted on 4$\times$ NVIDIA RTX 5090 GPUs (32\,GB each), totaling approximately 62 GPU-hours.
17	
18	\paragraph{Software.}
19	Experiments used Python 3.12.3, PyTorch 2.10.0 (CUDA 12.8), Transformers 4.57.6, XGBoost 3.2.0, scikit-learn 1.8.0, NumPy 2.2.6, pandas 3.0.2, and SciPy 1.17.1.
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bb84fb2c-bb9a-44ff-8963-f704f0066aaa",
  "isSidechain": false,
  "promptId": "52fa409d-a131-499b-b76f-82911a2f9bb6",
  "type": "user",
  "uuid": "11fff00c-41ed-44f3-9bd7-448e67925bbd",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/ethics.tex",
      "content": "\\section*{Ethics Statement}\n\\label{sec:ethics}\n\nAll texts analyzed in this work are LLM-generated from publicly available Wikipedia seeds; no personal or sensitive data is involved.\nOur method estimates the generation depth of a text passage (how many recursive generation steps it has undergone), not the identity of its author.\nIndividual authorship attribution is outside both the scope and the capability of this approach; privacy implications are minimal.\nWe acknowledge that depth estimation tools could in principle be used to selectively suppress machine-generated text in contexts where such content is legitimate (e.g., accessibility tools, assistive writing).\nWe encourage deployment in data governance pipelines where provenance transparency, rather than content removal, is the objective.\nAll code, data, and trained models will be released upon publication.\n\n\\paragraph{Licenses.}\nAll generator models are publicly available under permissive licenses (Apache 2.0 for Pythia, OLMo, and Mistral; Qwen License for Qwen3; Llama Community License for Llama 3.2).\nWikipedia seed passages are distributed under CC BY-SA 3.0.\n\n\\paragraph{Compute budget.}\nAll experiments were conducted on 4$\\times$ NVIDIA RTX 5090 GPUs (32\\,GB each), totaling approximately 62 GPU-hours.\n\n\\paragraph{Software.}\nExperiments used Python 3.12.3, PyTorch 2.10.0 (CUDA 12.8), Transformers 4.57.6, XGBoost 3.2.0, scikit-learn 1.8.0, NumPy 2.2.6, pandas 3.0.2, and SciPy 1.17.1.\n",
      "numLines": 20,
      "startLine": 1,
      "totalLines": 20
    }
  },
  "sourceToolAssistantUUID": "bb84fb2c-bb9a-44ff-8963-f704f0066aaa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth"
}
```

</details>

---


### Tool call

_source line 3193 · 2026-05-19T06:13:46.869Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NSjrHRMbRGG4d5waHuwbNn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11fff00c-41ed-44f3-9bd7-448e67925bbd",
  "isSidechain": false,
  "requestId": "req_011CbBSBPq9sDxoSQxEJKmNE",
  "type": "assistant",
  "uuid": "b6efab66-d31a-444c-92f9-5f3b23274140",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NNB9Qd83LpREUpPpt1cQAJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1219,
      "cache_read_input_tokens": 134178,
      "output_tokens": 163,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1219,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 163,
          "cache_read_input_tokens": 134178,
          "cache_creation_input_tokens": 1219,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1219
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 3194 · 2026-05-19T06:13:46.873Z_

<details><summary>↩ Tool result · `toolu_01NSjrHRMbRGG4d5waHuwbNn`</summary>

```text
1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	All eight generators are base (pretrained) models.
5	This is a deliberate design choice: base models isolate the generation mechanism from instruction-tuning effects and enable controlled study of recursive distributional drift.
6	However, web text is predominantly produced by instruction-tuned and RLHF-aligned models.
7	Preliminary instruct experiments confirm that depth signal degrades substantially under instruction tuning: OLMo-2-1B-Instruct drops to 3-class LOGO F1\,=\,0.338 (vs.\ 0.763 base; this is classification F1, distinct from the clustering silhouette of the same value reported in \S\ref{sec:discussion}) and Qwen3-0.6B with chat template to 0.667 (vs.\ 0.816 base); these comparisons use earlier LOGO subsets (5--6 generators) predating the full 8-generator expansion in Table~\ref{tab:logo-results}.
8	Length-matched analysis yields near-zero correlations ($|\rho| < 0.02$) and binary classification near chance (F1\,$\approx$\,0.5) for Qwen models, leaving interpretation ambiguous.
9	Extending depth profiling to instruct models requires addressing these confounds (length regulation, format constraints, safety-driven distribution shaping) that instruction tuning introduces.
10	
11	Our experiments include generators up to 8.2B parameters (Qwen3-8B).
12	Depth signal persists at this scale (Qwen3-8B 3-class F1\,=\,0.714), but cross-scale transfer incurs a moderate gap vs.\ $\leq$2.8B generators (F1\,=\,0.77--0.81).
13	Frontier models (70B+) and closed-source models remain untested; the consistent scale trend (Mistral-7B binary F1\,=\,0.633, lowest among all generators) suggests depth signal may weaken further at frontier scales, potentially approaching the detection floor.
14	
15	Differential depth response strength is prompt-type dependent: continuation chains show strongest drift (within-type binary F1\,=\,0.781) compared to elaboration (0.730) and rewriting (0.737), with within-prompt-type paraphrastic chains showing weaker signal (binary F1\,=\,0.671 vs.\ 0.749 for within-prompt-type continuation).
16	DDR is most reliably detected in continuation-style generation; near-paraphrastic settings approach the method's detection floor.
17	Cross-prompt-type transfer (LOPTO F1\,=\,0.753) confirms shared signal, yet additional prompt types (e.g., summarization, instruction following) and cross-generator $\times$ cross-prompt interactions remain untested.
18	
19	Our primary evaluation uses single-generator chains; cross-model chains (\S\ref{sec:results-classification}) confirm depth signal under generator heterogeneity (3-class F1\,=\,0.809, binary F1\,=\,0.764), though the eight generators represent a controlled laboratory setting rather than the full diversity of real-world contamination.
20	Simulated human editing (\S\ref{sec:discussion}) suggests graceful degradation, but the gap between simulated token replacement and real-world post-processing remains untested.
21	
22	The reference model is fixed to Pythia-410M throughout, although cross-family reference experiments (\S\ref{sec:results-differential}) confirm the phenomenon is not reference-specific (spread 0.013 across three references).
23	All seed texts in the main evaluation are English Wikipedia excerpts.
24	Cross-domain evaluation (Appendix~\ref{app:domain}) at both $t{=}1.0$ and $t{=}0.7$ shows that depth signal persists across News, Academic, and Code domains (binary F1 0.63--0.75 depending on domain and temperature), though a domain $\times$ temperature interaction exists: at $t{=}0.7$, Academic domain binary F1 drops to 0.628, suggesting that reference model calibration is critical for cross-domain deployment.
25	The reference model dependency (Pythia-410M, English-centric pretraining) limits non-English applicability and adds inference overhead relative to surface-feature-only approaches.
26	Generalization to other languages remains untested.
27	
28	Our default analysis uses fixed decoding parameters (temperature 0.7, nucleus $p{=}0.9$). A temperature ablation across four generators from three families (Appendix~\ref{app:sampling-sensitivity}) shows that the method operates reliably within $t \in [0.5, 0.7]$ but degrades at $t{=}0.9$ ($-9.3$ to $-26.0$\,pp across generators). Low-temperature improvement is model-dependent (Pythia/OLMo: $+7$--$9$\,pp; Qwen: $0$--$2$\,pp), indicating that depth profiling assumes standard decoding regimes and that the benefit of conservative temperature varies by model family.
29	Tokenizer differences across families may contribute to the observed temperature sensitivity pattern; within-family comparisons (two Qwen models showing consistent robustness) support a family-level effect, but controlling for tokenizer requires further study.
30	
31	Simpler features (character or word n-gram frequencies) were not explored; they may capture complementary surface-level patterns but would not contribute to the location/shape decomposition central to this analysis.
32	
33	We use 3-class granularity (gen-0\,/\,gen-1\,/\,gen-2+). A 5-class evaluation (Appendix~\ref{app:finer-depth}) yields LOGO F1\,$\approx$\,0.50, with depths 2--4 mutually indistinguishable, validating the 3-class design as the practical resolution limit.
34	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b6efab66-d31a-444c-92f9-5f3b23274140",
  "isSidechain": false,
  "promptId": "52fa409d-a131-499b-b76f-82911a2f9bb6",
  "type": "user",
  "uuid": "b8582508-e542-44a5-a48a-84f2f1896d98",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/limitations.tex",
      "content": "\\section*{Limitations}\n\\label{sec:limitations}\n\nAll eight generators are base (pretrained) models.\nThis is a deliberate design choice: base models isolate the generation mechanism from instruction-tuning effects and enable controlled study of recursive distributional drift.\nHowever, web text is predominantly produced by instruction-tuned and RLHF-aligned models.\nPreliminary instruct experiments confirm that depth signal degrades substantially under instruction tuning: OLMo-2-1B-Instruct drops to 3-class LOGO F1\\,=\\,0.338 (vs.\\ 0.763 base; this is classification F1, distinct from the clustering silhouette of the same value reported in \\S\\ref{sec:discussion}) and Qwen3-0.6B with chat template to 0.667 (vs.\\ 0.816 base); these comparisons use earlier LOGO subsets (5--6 generators) predating the full 8-generator expansion in Table~\\ref{tab:logo-results}.\nLength-matched analysis yields near-zero correlations ($|\\rho| < 0.02$) and binary classification near chance (F1\\,$\\approx$\\,0.5) for Qwen models, leaving interpretation ambiguous.\nExtending depth profiling to instruct models requires addressing these confounds (length regulation, format constraints, safety-driven distribution shaping) that instruction tuning introduces.\n\nOur experiments include generators up to 8.2B parameters (Qwen3-8B).\nDepth signal persists at this scale (Qwen3-8B 3-class F1\\,=\\,0.714), but cross-scale transfer incurs a moderate gap vs.\\ $\\leq$2.8B generators (F1\\,=\\,0.77--0.81).\nFrontier models (70B+) and closed-source models remain untested; the consistent scale trend (Mistral-7B binary F1\\,=\\,0.633, lowest among all generators) suggests depth signal may weaken further at frontier scales, potentially approaching the detection floor.\n\nDifferential depth response strength is prompt-type dependent: continuation chains show strongest drift (within-type binary F1\\,=\\,0.781) compared to elaboration (0.730) and rewriting (0.737), with within-prompt-type paraphrastic chains showing weaker signal (binary F1\\,=\\,0.671 vs.\\ 0.749 for within-prompt-type continuation).\nDDR is most reliably detected in continuation-style generation; near-paraphrastic settings approach the method's detection floor.\nCross-prompt-type transfer (LOPTO F1\\,=\\,0.753) confirms shared signal, yet additional prompt types (e.g., summarization, instruction following) and cross-generator $\\times$ cross-prompt interactions remain untested.\n\nOur primary evaluation uses single-generator chains; cross-model chains (\\S\\ref{sec:results-classification}) confirm depth signal under generator heterogeneity (3-class F1\\,=\\,0.809, binary F1\\,=\\,0.764), though the eight generators represent a controlled laboratory setting rather than the full diversity of real-world contamination.\nSimulated human editing (\\S\\ref{sec:discussion}) suggests graceful degradation, but the gap between simulated token replacement and real-world post-processing remains untested.\n\nThe reference model is fixed to Pythia-410M throughout, although cross-family reference experiments (\\S\\ref{sec:results-differential}) confirm the phenomenon is not reference-specific (spread 0.013 across three references).\nAll seed texts in the main evaluation are English Wikipedia excerpts.\nCross-domain evaluation (Appendix~\\ref{app:domain}) at both $t{=}1.0$ and $t{=}0.7$ shows that depth signal persists across News, Academic, and Code domains (binary F1 0.63--0.75 depending on domain and temperature), though a domain $\\times$ temperature interaction exists: at $t{=}0.7$, Academic domain binary F1 drops to 0.628, suggesting that reference model calibration is critical for cross-domain deployment.\nThe reference model dependency (Pythia-410M, English-centric pretraining) limits non-English applicability and adds inference overhead relative to surface-feature-only approaches.\nGeneralization to other languages remains untested.\n\nOur default analysis uses fixed decoding parameters (temperature 0.7, nucleus $p{=}0.9$). A temperature ablation across four generators from three families (Appendix~\\ref{app:sampling-sensitivity}) shows that the method operates reliably within $t \\in [0.5, 0.7]$ but degrades at $t{=}0.9$ ($-9.3$ to $-26.0$\\,pp across generators). Low-temperature improvement is model-dependent (Pythia/OLMo: $+7$--$9$\\,pp; Qwen: $0$--$2$\\,pp), indicating that depth profiling assumes standard decoding regimes and that the benefit of conservative temperature varies by model family.\nTokenizer differences across families may contribute to the observed temperature sensitivity pattern; within-family comparisons (two Qwen models showing consistent robustness) support a family-level effect, but controlling for tokenizer requires further study.\n\nSimpler features (character or word n-gram frequencies) were not explored; they may capture complementary surface-level patterns but would not contribute to the location/shape decomposition central to this analysis.\n\nWe use 3-class granularity (gen-0\\,/\\,gen-1\\,/\\,gen-2+). A 5-class evaluation (Appendix~\\ref{app:finer-depth}) yields LOGO F1\\,$\\approx$\\,0.50, with depths 2--4 mutually indistinguishable, validating the 3-class design as the practical resolution limit.\n",
      "numLines": 34,
      "startLine": 1,
      "totalLines": 34
    }
  },
  "sourceToolAssistantUUID": "b6efab66-d31a-444c-92f9-5f3b23274140",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth"
}
```

</details>

---


### Assistant

_source line 3195 · 2026-05-19T06:14:03.700Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I now have a thorough picture of the paper. Let me also check for self-citations, and verify the page count for main content vs appendix.

Key findings so far:

**Anonymization check** ✅:
1. `\usepackage[review]{acl}` - review/anonymous mode ✅
2. `\author{Anonymous}` ✅
3. PDF metadata: Author field empty, Title empty ✅
4. No github links, no acknowledgments, no self-citations found ✅


5. The ethics section mentions code and models will be released upon publication without providing any links, which maintains anonymity ✅

**Supplementary materials**: The paper spans 31 pages total with the main content occupying 8 pages (abstract through ethics and bibliography), while the appendix comprises 19 sections across the remaining pages. According to the ARR policy, I need to verify how the appendix is being handled.

The ROADMAP confirms the main text is exactly 8 pages with the Conclusion ending on page 8 and Limitations starting mid-page 8 (and notably, Limitations don't count toward the page limit). For ARR submissions, the standard allows 8 pages of main content plus unlimited references and appendix in a single PDF, with both Limitations and Ethics statements excluded from the page count. Now I should verify the references file exists and check its contents.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8582508-e542-44a5-a48a-84f2f1896d98",
  "isSidechain": false,
  "requestId": "req_011CbBSBhotZmyLyreCLWNTL",
  "type": "assistant",
  "uuid": "ffd0072c-5b00-4c83-b6be-08ecf0b7e8dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GxQKndv3ufoDx2yWo5WciY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2131,
      "cache_read_input_tokens": 135397,
      "output_tokens": 900,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2131,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 900,
          "cache_read_input_tokens": 135397,
          "cache_creation_input_tokens": 2131,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2131
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 3196 · 2026-05-19T06:14:03.856Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01WHsbvivbWSSVuThQ7zJwXB`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper && wc -l references.bib && grep -c \"@\" references.bib",
  "description": "Check references.bib entry count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ffd0072c-5b00-4c83-b6be-08ecf0b7e8dd",
  "isSidechain": false,
  "requestId": "req_011CbBSBhotZmyLyreCLWNTL",
  "type": "assistant",
  "uuid": "2dfa940f-78a4-45fb-b92f-c4346823ac9c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GxQKndv3ufoDx2yWo5WciY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2131,
      "cache_read_input_tokens": 135397,
      "output_tokens": 900,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2131,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 900,
          "cache_read_input_tokens": 135397,
          "cache_creation_input_tokens": 2131,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2131
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 3197 · 2026-05-19T06:14:03.866Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01CHvWomFgfpYKe4Tuq1kjqp`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper && ls -la checklist.md 2>/dev/null || echo \"No checklist.md found\"",
  "description": "Check if checklist draft exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2dfa940f-78a4-45fb-b92f-c4346823ac9c",
  "isSidechain": false,
  "requestId": "req_011CbBSBhotZmyLyreCLWNTL",
  "type": "assistant",
  "uuid": "59bbc60c-9178-41c7-aa8b-52ae97feca3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GxQKndv3ufoDx2yWo5WciY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2131,
      "cache_read_input_tokens": 135397,
      "output_tokens": 900,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2131,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 900,
          "cache_read_input_tokens": 135397,
          "cache_creation_input_tokens": 2131,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2131
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 3198 · 2026-05-19T06:14:03.946Z_

<details><summary>↩ Tool result · `toolu_01WHsbvivbWSSVuThQ7zJwXB`</summary>

```text
575 references.bib
71
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2dfa940f-78a4-45fb-b92f-c4346823ac9c",
  "isSidechain": false,
  "promptId": "52fa409d-a131-499b-b76f-82911a2f9bb6",
  "type": "user",
  "uuid": "cfd7e3d3-0a58-4417-b53a-4ac275ed68f7",
  "toolUseResult": {
    "stdout": "575 references.bib\n71",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "2dfa940f-78a4-45fb-b92f-c4346823ac9c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth"
}
```

</details>

---


### Tool result

_source line 3199 · 2026-05-19T06:14:03.939Z_

<details><summary>↩ Tool result · `toolu_01CHvWomFgfpYKe4Tuq1kjqp`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu 6230 May 18 23:13 checklist.md
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59bbc60c-9178-41c7-aa8b-52ae97feca3c",
  "isSidechain": false,
  "promptId": "52fa409d-a131-499b-b76f-82911a2f9bb6",
  "type": "user",
  "uuid": "49292b23-7e4f-483b-bc01-da7e730b2c96",
  "toolUseResult": {
    "stdout": "-rw-r--r-- 1 ubuntu ubuntu 6230 May 18 23:13 checklist.md",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "59bbc60c-9178-41c7-aa8b-52ae97feca3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth"
}
```

</details>

---


### Tool call

_source line 3200 · 2026-05-19T06:14:04.322Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01CMVRErTuLXQw3Ja8suyFu3`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper && grep -rn \"\\\\\\\\cite\\b\" *.tex | wc -l && echo \"---\" && grep -rn \"\\\\\\\\cite{\" *.tex | sed 's/.*\\\\\\\\cite{//' | sed 's/}.*//' | tr ',' '\\n' | sort -u | wc -l",
  "description": "Count citations used in paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49292b23-7e4f-483b-bc01-da7e730b2c96",
  "isSidechain": false,
  "requestId": "req_011CbBSBhotZmyLyreCLWNTL",
  "type": "assistant",
  "uuid": "9e835c0b-641f-4dd3-94da-d8a7b7c0e399",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GxQKndv3ufoDx2yWo5WciY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2131,
      "cache_read_input_tokens": 135397,
      "output_tokens": 900,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2131,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 900,
          "cache_read_input_tokens": 135397,
          "cache_creation_input_tokens": 2131,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2131
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 3201 · 2026-05-19T06:14:04.400Z_

<details><summary>↩ Tool result · `toolu_01CMVRErTuLXQw3Ja8suyFu3`</summary>

```text
30
---
56
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9e835c0b-641f-4dd3-94da-d8a7b7c0e399",
  "isSidechain": false,
  "promptId": "52fa409d-a131-499b-b76f-82911a2f9bb6",
  "type": "user",
  "uuid": "5ae92ffa-152c-46f1-a9dc-dbcf50c0766f",
  "toolUseResult": {
    "stdout": "30\n---\n56",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "9e835c0b-641f-4dd3-94da-d8a7b7c0e399",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth"
}
```

</details>

---


### Tool call

_source line 3202 · 2026-05-19T06:14:07.481Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BZgjggMSHY5R5oSjf7QUAR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/checklist.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ae92ffa-152c-46f1-a9dc-dbcf50c0766f",
  "isSidechain": false,
  "requestId": "req_011CbBSCzVGWuPtDknPRZaWd",
  "type": "assistant",
  "uuid": "4efe51ab-2f98-4958-bf7c-a5b364e7a358",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SN5X9Hvwarwo6B1TMbWPox",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1162,
      "cache_read_input_tokens": 137528,
      "output_tokens": 91,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1162,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 91,
          "cache_read_input_tokens": 137528,
          "cache_creation_input_tokens": 1162,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1162
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---


### Tool result

_source line 3203 · 2026-05-19T06:14:07.495Z_

<details><summary>↩ Tool result · `toolu_01BZgjggMSHY5R5oSjf7QUAR`</summary>

```text
1	# ARR Responsible NLP Research Checklist
2	
3	> For EMNLP 2026 via ACL Rolling Review. Answers reference specific paper sections.
4	
5	---
6	
7	## Section A: Did you describe the limitations of your work?
8	
9	**A1. Did you describe the limitations of your work?**
10	Yes. See the dedicated Limitations section (§Limitations, after Conclusion). Key limitations discussed:
11	- Restricted to base (pretrained) models; instruction-tuned models degrade substantially (OLMo-Instruct LOGO F1=0.338 vs 0.763 base)
12	- Generators tested up to 8.2B parameters; frontier models (70B+) untested
13	- Prompt-type dependent: continuation chains strongest (0.781), paraphrastic weakest (0.671)
14	- Temperature sensitivity: method reliable at t≤0.7, degrades at t=0.9 (−9.3 to −26.0pp)
15	- English-only evaluation; non-English generalization untested
16	- 3-class granularity is the practical ceiling (5-class F1≈0.50)
17	- Reference model fixed to Pythia-410M (cross-reference spread 0.013 confirms not reference-specific)
18	
19	**A2. Did you discuss any potential risks of your work?**
20	Yes. Ethics Statement discusses: (1) no personal/sensitive data involved, (2) method estimates depth not author identity, (3) potential misuse for suppressing legitimate AI-generated content, (4) recommended for provenance transparency rather than content removal.
21	
22	**A3. Do your abstract and introduction summarize the paper's main claims?**
23	Yes. Abstract states: DDR tri-partition finding, 7-feature ensemble binary F1=0.694 under LOGO, and instruction-tuning limitation. Introduction (§1) details the DDR tri-partition with effect sizes, cross-generator generalization, and positions the contribution as task formulation + DDR analysis.
24	
25	---
26	
27	## Section B: Did you use or create scientific artifacts?
28	
29	**B1. Did you cite the creators of artifacts you used?**
30	Yes. All models cited: Pythia (Biderman et al., 2023), OLMo (Groeneveld et al., 2024), Qwen3 (Yang et al., 2025), Llama 3 (Grattafiori et al., 2024), Mistral (Jiang et al., 2023). All baseline methods cited: FastDetectGPT, Binoculars, LD-Score, Avg-LogProb. Software versions listed in Ethics Statement.
31	
32	**B2. Did you discuss the license or terms for use and/or distribution of any artifacts?**
33	Yes. Ethics Statement §Licenses: Apache 2.0 (Pythia, OLMo, Mistral), Qwen License (Qwen3), Llama Community License (Llama 3.2), CC BY-SA 3.0 (Wikipedia seeds).
34	
35	**B3. Did you discuss if your use of existing artifacts is consistent with their intended use?**
36	Yes. All models used for text generation (intended use). Wikipedia used as seed text (public domain content).
37	
38	**B4. Did you discuss the steps taken to check whether the data/models contain information that names or uniquely identifies people or offensive content?**
39	Partially. Seed texts are Wikipedia excerpts (publicly available encyclopedic content). Generated text is model output conditioned on these seeds. No personal data collection or annotation involving human subjects.
40	
41	**B5. Did you provide documentation of the artifacts?**
42	Yes. §3 (Method) fully documents: generation chain construction, feature extraction pipeline, evaluation protocol. Appendix provides dataset statistics (Appendix A), per-generator breakdowns, and ablation details. Code/data/models will be released upon publication.
43	
44	---
45	
46	## Section C: Did you run computational experiments?
47	
48	**C1. Did you report the number of parameters in each model used?**
49	Yes. Table 1 lists parameter counts for all 8 generators (0.6B to 8.2B). Reference model: Pythia-410M (410M parameters). §3.2 specifies exact model identifiers.
50	
51	**C2. Did you report the computing infrastructure used?**
52	Yes. Ethics Statement §Compute budget: 4× NVIDIA RTX 5090 GPUs (32GB each), approximately 62 GPU-hours total.
53	
54	**C3. Did you report the average runtime for each approach?**
55	Partially. Table 2 reports inference time per text (ms/text): 7-feature ensemble 9.7ms, 4-detector ensemble 22.8ms. Training time not separately reported (XGBoost training is negligible, <1min per fold).
56	
57	**C4. Did you report the evaluation metrics, along with the values and confidence intervals?**
58	Yes. All primary results include 95% bootstrap CIs (n=1000). Tables 1-2 report CIs. McNemar tests for pairwise comparisons (§4.2). Bonferroni correction applied within test families (§3.4). Cohen's d effect sizes reported for DDR partition (§4.2).
59	
60	**C5. Did you report the hyperparameter search strategy?**
61	Partially. XGBoost uses standard defaults (n_estimators=200, max_depth=6, lr=0.1) without hyperparameter search (§3.4). Appendix C shows alternative classifiers (CORAL, CORN, Frank-Hall) yield comparable performance, confirming discriminative power resides in features not classifier.
62	
63	**C6. Did you report the number and range of values tried for each hyperparameter?**
64	N/A. No hyperparameter search conducted; default XGBoost parameters used throughout. Stability confirmed: LOGO F1 std < 0.001 over 5 random seeds (§3.4).
65	
66	---
67	
68	## Section D: Did you use or create data?
69	
70	**D1. Did you discuss how the data was collected or created?**
71	Yes. §3.2 describes chain construction: ~1000 Wikipedia seed passages per generator, iterative continuation with fixed prompt template, temperature 0.7, nucleus p=0.9, max 256 tokens. 37,058 texts after removing 2,746 chain breaks and 11 short passages. Appendix A provides full dataset statistics.
72	
73	**D2. Did you report the basic statistics of the data used?**
74	Yes. §3.2: total texts (37,058), chain breaks (2,746), depth distribution. Appendix A: per-generator breakdown, depth-class counts, token statistics.
75	
76	**D3. Did you discuss if the data you are using/creating contains personally identifiable information or offensive content?**
77	Yes. Ethics Statement: "All texts analyzed are LLM-generated from publicly available Wikipedia seeds; no personal or sensitive data is involved."
78	
79	**D4. Did you provide the data?**
80	Will release upon publication. Ethics Statement: "All code, data, and trained models will be released upon publication."
81	
82	---
83	
84	## Section E: Did you use human annotators or crowdworkers?
85	
86	**E1-E5.** N/A. No human annotation or crowdsourcing was used. All labels are automatically determined by the generation chain construction process (depth = position in the chain).
87	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4efe51ab-2f98-4958-bf7c-a5b364e7a358",
  "isSidechain": false,
  "promptId": "52fa409d-a131-499b-b76f-82911a2f9bb6",
  "type": "user",
  "uuid": "02ef3d2f-c6c0-4436-bfc7-16d8ec305823",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/checklist.md",
      "content": "# ARR Responsible NLP Research Checklist\n\n> For EMNLP 2026 via ACL Rolling Review. Answers reference specific paper sections.\n\n---\n\n## Section A: Did you describe the limitations of your work?\n\n**A1. Did you describe the limitations of your work?**\nYes. See the dedicated Limitations section (§Limitations, after Conclusion). Key limitations discussed:\n- Restricted to base (pretrained) models; instruction-tuned models degrade substantially (OLMo-Instruct LOGO F1=0.338 vs 0.763 base)\n- Generators tested up to 8.2B parameters; frontier models (70B+) untested\n- Prompt-type dependent: continuation chains strongest (0.781), paraphrastic weakest (0.671)\n- Temperature sensitivity: method reliable at t≤0.7, degrades at t=0.9 (−9.3 to −26.0pp)\n- English-only evaluation; non-English generalization untested\n- 3-class granularity is the practical ceiling (5-class F1≈0.50)\n- Reference model fixed to Pythia-410M (cross-reference spread 0.013 confirms not reference-specific)\n\n**A2. Did you discuss any potential risks of your work?**\nYes. Ethics Statement discusses: (1) no personal/sensitive data involved, (2) method estimates depth not author identity, (3) potential misuse for suppressing legitimate AI-generated content, (4) recommended for provenance transparency rather than content removal.\n\n**A3. Do your abstract and introduction summarize the paper's main claims?**\nYes. Abstract states: DDR tri-partition finding, 7-feature ensemble binary F1=0.694 under LOGO, and instruction-tuning limitation. Introduction (§1) details the DDR tri-partition with effect sizes, cross-generator generalization, and positions the contribution as task formulation + DDR analysis.\n\n---\n\n## Section B: Did you use or create scientific artifacts?\n\n**B1. Did you cite the creators of artifacts you used?**\nYes. All models cited: Pythia (Biderman et al., 2023), OLMo (Groeneveld et al., 2024), Qwen3 (Yang et al., 2025), Llama 3 (Grattafiori et al., 2024), Mistral (Jiang et al., 2023). All baseline methods cited: FastDetectGPT, Binoculars, LD-Score, Avg-LogProb. Software versions listed in Ethics Statement.\n\n**B2. Did you discuss the license or terms for use and/or distribution of any artifacts?**\nYes. Ethics Statement §Licenses: Apache 2.0 (Pythia, OLMo, Mistral), Qwen License (Qwen3), Llama Community License (Llama 3.2), CC BY-SA 3.0 (Wikipedia seeds).\n\n**B3. Did you discuss if your use of existing artifacts is consistent with their intended use?**\nYes. All models used for text generation (intended use). Wikipedia used as seed text (public domain content).\n\n**B4. Did you discuss the steps taken to check whether the data/models contain information that names or uniquely identifies people or offensive content?**\nPartially. Seed texts are Wikipedia excerpts (publicly available encyclopedic content). Generated text is model output conditioned on these seeds. No personal data collection or annotation involving human subjects.\n\n**B5. Did you provide documentation of the artifacts?**\nYes. §3 (Method) fully documents: generation chain construction, feature extraction pipeline, evaluation protocol. Appendix provides dataset statistics (Appendix A), per-generator breakdowns, and ablation details. Code/data/models will be released upon publication.\n\n---\n\n## Section C: Did you run computational experiments?\n\n**C1. Did you report the number of parameters in each model used?**\nYes. Table 1 lists parameter counts for all 8 generators (0.6B to 8.2B). Reference model: Pythia-410M (410M parameters). §3.2 specifies exact model identifiers.\n\n**C2. Did you report the computing infrastructure used?**\nYes. Ethics Statement §Compute budget: 4× NVIDIA RTX 5090 GPUs (32GB each), approximately 62 GPU-hours total.\n\n**C3. Did you report the average runtime for each approach?**\nPartially. Table 2 reports inference time per text (ms/text): 7-feature ensemble 9.7ms, 4-detector ensemble 22.8ms. Training time not separately reported (XGBoost training is negligible, <1min per fold).\n\n**C4. Did you report the evaluation metrics, along with the values and confidence intervals?**\nYes. All primary results include 95% bootstrap CIs (n=1000). Tables 1-2 report CIs. McNemar tests for pairwise comparisons (§4.2). Bonferroni correction applied within test families (§3.4). Cohen's d effect sizes reported for DDR partition (§4.2).\n\n**C5. Did you report the hyperparameter search strategy?**\nPartially. XGBoost uses standard defaults (n_estimators=200, max_depth=6, lr=0.1) without hyperparameter search (§3.4). Appendix C shows alternative classifiers (CORAL, CORN, Frank-Hall) yield comparable performance, confirming discriminative power resides in features not classifier.\n\n**C6. Did you report the number and range of values tried for each hyperparameter?**\nN/A. No hyperparameter search conducted; default XGBoost parameters used throughout. Stability confirmed: LOGO F1 std < 0.001 over 5 random seeds (§3.4).\n\n---\n\n## Section D: Did you use or create data?\n\n**D1. Did you discuss how the data was collected or created?**\nYes. §3.2 describes chain construction: ~1000 Wikipedia seed passages per generator, iterative continuation with fixed prompt template, temperature 0.7, nucleus p=0.9, max 256 tokens. 37,058 texts after removing 2,746 chain breaks and 11 short passages. Appendix A provides full dataset statistics.\n\n**D2. Did you report the basic statistics of the data used?**\nYes. §3.2: total texts (37,058), chain breaks (2,746), depth distribution. Appendix A: per-generator breakdown, depth-class counts, token statistics.\n\n**D3. Did you discuss if the data you are using/creating contains personally identifiable information or offensive content?**\nYes. Ethics Statement: \"All texts analyzed are LLM-generated from publicly available Wikipedia seeds; no personal or sensitive data is involved.\"\n\n**D4. Did you provide the data?**\nWill release upon publication. Ethics Statement: \"All code, data, and trained models will be released upon publication.\"\n\n---\n\n## Section E: Did you use human annotators or crowdworkers?\n\n**E1-E5.** N/A. No human annotation or crowdsourcing was used. All labels are automatically determined by the generation chain construction process (depth = position in the chain).\n",
      "numLines": 87,
      "startLine": 1,
      "totalLines": 87
    }
  },
  "sourceToolAssistantUUID": "4efe51ab-2f98-4958-bf7c-a5b364e7a358",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth"
}
```

</details>

---


### Runtime record

_source line 3204 · 2026-05-19T06:14:07.503Z_

```json
{
  "parentUuid": "02ef3d2f-c6c0-4436-bfc7-16d8ec305823",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "f8fda6c0-515b-4ece-8223-ffdc1296424c",
  "timestamp": "2026-05-19T06:14:07.503Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth"
}
```

---


### Runtime record

_source line 3205_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] 投稿准备任务（不依赖 R26 审稿结果，现在就做）：  1. **EMNLP 2026 ARR OpenReview 投稿材料清单**：    - 查 EMNLP 2026 ARR 的 OpenReview 投稿要求（WebSearch \"EMNLP 2026 ARR submission requirements OpenReview\"）    - 确认需要哪些材料：…",
  "leafUuid": "f8fda6c0-515b-4ece-8223-ffdc1296424c",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96"
}
```

---


### Runtime record

_source line 3206_

```json
{
  "type": "ai-title",
  "aiTitle": "Await worker callbacks and sync paper updates",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96"
}
```

---


### Assistant

_source line 3207 · 2026-05-19T06:14:19.808Z_

<details><summary>Logged reasoning block</summary>

```text
The existing checklist is comprehensive and well-written. Now let me check what the EMNLP 2026 page count is. I also need to verify the main content page count in the PDF.

Let me check if the main content is within the page limit. The ROADMAP says "正文 8.0 页" which should be fine for a long paper (8 pages).

Let me also check the current PDF to see where the appendix starts.

Now let me also look at the page count issue - the last compilation was 31 pages (with the recent additions of holdout split validation and generator subset table). 

I need to verify a few critical submission requirements: whether ARR requires the appendix in the same PDF file, if there's a separate supplementary materials upload for code and data, and what the exact OpenReview form fields are. The worker is handling the WebSearch for these details, so I'll wait for that before compiling my report. In the meantime, let me check the PDF to see where the main content transitions to the appendix and flag any issues that need attention.

The paper looks solid overall—the checklist is comprehensive, anonymization is correct, ethics and limitations statements are present, and there are 71 references with 56 unique citation keys. My main concern is verifying that the main content stays within the 8-page limit for ARR, even though the 31-page total is fine with an unlimited appendix. Let me examine the PDF to confirm where that boundary falls.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8fda6c0-515b-4ece-8223-ffdc1296424c",
  "isSidechain": false,
  "requestId": "req_011CbBSDDrwER8NsCGsMVa2W",
  "type": "assistant",
  "uuid": "b5d32ec9-3be3-45ce-9e51-9930df79f218",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ZpbeYpCqPCnsMz6w2Ke7Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3254,
      "cache_read_input_tokens": 137528,
      "output_tokens": 526,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3254,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 526,
          "cache_read_input_tokens": 137528,
          "cache_creation_input_tokens": 3254,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3254
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---


### Assistant

_source line 3208 · 2026-05-19T06:14:19.810Z_

Checklist 草稿已存在且内容全面。让我确认正文页数边界。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5d32ec9-3be3-45ce-9e51-9930df79f218",
  "isSidechain": false,
  "requestId": "req_011CbBSDDrwER8NsCGsMVa2W",
  "type": "assistant",
  "uuid": "d3b1357e-fdbb-4e72-b668-06ebcb8b742f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ZpbeYpCqPCnsMz6w2Ke7Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3254,
      "cache_read_input_tokens": 137528,
      "output_tokens": 526,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3254,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 526,
          "cache_read_input_tokens": 137528,
          "cache_creation_input_tokens": 3254,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3254
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---


### Tool call

_source line 3209 · 2026-05-19T06:14:19.943Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01DoWvCcBUNAKKXkDyKQd68R`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3b1357e-fdbb-4e72-b668-06ebcb8b742f",
  "isSidechain": false,
  "requestId": "req_011CbBSDDrwER8NsCGsMVa2W",
  "type": "assistant",
  "uuid": "bc989ddf-cb8f-460c-87b9-7fb166334625",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ZpbeYpCqPCnsMz6w2Ke7Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3254,
      "cache_read_input_tokens": 137528,
      "output_tokens": 526,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3254,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 526,
          "cache_read_input_tokens": 137528,
          "cache_creation_input_tokens": 3254,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3254
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---


### Tool result

_source line 3210 · 2026-05-19T06:14:19.947Z_

<details><summary>↩ Tool result · `toolu_01DoWvCcBUNAKKXkDyKQd68R`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__pdf_to_images"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc989ddf-cb8f-460c-87b9-7fb166334625",
  "isSidechain": false,
  "promptId": "52fa409d-a131-499b-b76f-82911a2f9bb6",
  "type": "user",
  "uuid": "af039932-960e-48df-ae0a-2a55111fad88",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__pdf_to_images"
    ],
    "query": "select:mcp__agent-ml-research__pdf_to_images",
    "total_deferred_tools": 82
  },
  "sourceToolAssistantUUID": "bc989ddf-cb8f-460c-87b9-7fb166334625",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth"
}
```

</details>

---


### Tool call

_source line 3211 · 2026-05-19T06:14:23.231Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images · `toolu_01VnvWEFW9JV2jeJk7SknLaP`</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.pdf",
  "pages": "8,9",
  "dpi": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af039932-960e-48df-ae0a-2a55111fad88",
  "isSidechain": false,
  "requestId": "req_011CbBSE9BviWt5GtVDUTa4X",
  "type": "assistant",
  "uuid": "790c0bf4-6cd0-4c6d-98a3-84e69d67daaf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "9ed98fdf-5dd0-4907-9f9e-09d632e3aa96",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "gleaming-bouncing-knuth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TJnAidFyXbHqkootb67Mj7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 898,
      "cache_read_input_tokens": 140782,
      "output_tokens": 141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 898,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 141,
          "cache_read_input_tokens": 140782,
          "cache_creation_input_tokens": 898,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 898
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Large event (continued)

````text
### Tool result

_source line 3212 · 2026-05-19T06:14:24.034Z_

&lt;details>&lt;summary>↩ Tool result · `toolu_01VnvWEFW9JV2jeJk7SknLaP`&lt;/summary>

```text
Error: result (1,371,662 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint--claude-sessions-agent-113cd425/9ed98fdf-5dd0-4907-9f9e-09d632e3aa96/tool-results/mcp-agent-ml-research-pdf_to_images-1779171264026.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint--claude-sessions-agent-113cd425/9ed98fdf-5dd0-4907-9f9e-09d632e3aa96/tool-results/mcp-agent-ml-research-pdf_to_images-1779171264026.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint--claude-sessions-agent-113cd425/9ed98fdf-5dd0-4907-9f9e-09d632e3aa96/tool-results/mcp-agent-ml-research-pdf_to_images-1779171264026.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

&lt;/details>

&lt;details>&lt;summary>Recorded metadata&lt;/summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "790c0bf4-6cd0-4c6d-98a3-84e69d67daaf",
  "isSidechain": false,
  "promptId": "52fa409d-a131-499b-b76f-82911a2f9bb6",
  "type": "user",
  "uuid": "1c8696f6-5d8e-4272-9f19-a1a7d93bff93",
  "toolUseResult": "Error: result (1,371,662 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint--claude-sessions-agent-113cd425/9ed98fdf-5dd0-4907-9f9e-09d632e3aa96/tool-results/mcp-agent-ml-research-pdf_to_images-1779171264026.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint--claude-sessions-agent-113cd425/9ed98fdf-5dd0-4907-9f9e-09d632e3aa96/tool-results/mcp-agent-ml-research-pdf_to_images-1779171264026.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint--claude-sessions-agent-113cd425/9ed98fdf-5dd0-4907-9f9e-09d632e3aa96/tool-results/mcp-agent-ml-research-pdf_to_images-1779171264026.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
  "mcpMeta": {
    "structuredContent": {

````

---

### Large event (continued)

```text
      "result": "{\"success\": true, \"data\": {\"images\": [{\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p8.png\", \"base64\": \"iVBORw0KGgoAAAANSUhEUgAABNkAAAbaCAIAAAB3QTY3AAAACXBIWXMAABcSAAAXEgFnn9JSAAfRkklEQVR4nOzddXgU1/s28AQLHly/uEvRFiiQ4kUCBQoUd3cpVgK9CAUKxUJxl+LuDgWCS3CKB5fiEIKz7/3b5825prOSTbI7CeT+/JErozs+5x4542YiIiIiIiIiMpZbZE8AERERERERRTvMokRERERERGQ0ZlEiIiIiIiIyGrMoERERERERGY1ZlIiIiIiIiIzGLEpERERERERGYxYlIiIiIiIiozGLEhERERERkdGYRYmIiIiIiMhozKJERERERERkNGZRIiIiIiIiMhqzKBERERERERmNWZSIiIiIiIiMxixKRERERERERmMWJSIiIiIiIqMxixIREREREZHRmEWJiIiIiIjIaMyiREREREREZDRmUSIiIiIiIjIasygREREREREZjVmUiIiIiIiIjMYsSkREREREREZjFiUiIiIiIiKjMYsSERERERGR0ZhFiYiIiIiIyGjMokRERERERGQ0ZlEiIiIiIiIyGrMoERERERERGY1ZlIiIiIiIiIzGLEpERERERERGYxYlIiIiIiIiozGLEhERERERkdGYRYmIiIiIiMhozKJERERERERkNGZRIiIiIiIiMhqzKBERERERERmNWZSIiIiIiIiMxixKRERERERERmMWJSIiIiIiIqMxixIREREREZHRmEWJiIiIiIjIaMyiREREREREZDRmUSIiIiIiIjIasygREREREREZjVmUiIiIiIiIjMYsSkREREREREZjFiUiIiIiIiKjMYsSERERERGR0ZhFiYiIiIiIyGjMokRERERERGQ0ZlEiIiIiIiIyGrMoERERERERGY1ZlIiIiIiIiIzGLEpERERERERGYxYlIiIiIiIiozGLEhERERERkdGYRYmIiIiIiMhozKJERERERERkNGZRIiIiIiIiMhqzKBERERERERmNWZSIiIiIiIiMxixKRERERERERmMWJSIiIiIiIqMxixIREREREZHRmEWJiIiIiIjIaMyiREREREREZDRmUSIiIiIiIjIasygREREREREZjVmUiIiIiIiIjMYsSkREREREREZjFiUiIiIiIiKjMYsSERERERGR0ZhFiYiIiIiIyGjMokRERERERGQ0ZlEiIiIiIiIyGrMoERERERERGY1ZlIiIiIiIiIzGLEpERERERERGYxYlIiIiIiIiozGLEhERERERkdGYRYmIiIiIiMhozKJERERERERkNGZRIiIiIiIiMhqzKBERERERERmNWZSIiIiIiIiMxixKRERERERERmMWJSIiIiIiIqMxixIREREREZHRmEWJiIiIiIjIaMyiREREREREZDRmUSIiIiIiIjIasygREREREREZjVmUiIiIiIiIjMYsSkREREREREZjFiUiIiIiIiKjMYsSERERERGR0ZhFiYiIiIiIyGjMokRERERERGQ0ZlEiIiIiIiIyGrMoERERERERGY1ZlIiIiIiIiIzGLEpERERERERGYxYlIiIiIiIiozGLEhERERERkdGYRYmIiIiIiMhozKJERERERERkNGZRIiIiIiIiMhqzKBERERERERmNWZSIiIiIiIiMxixKRERERERERmMWJSIiIiIiIqMxixIREREREZHRmEWJiIiIiIjIaMyiREREREREZDRmUSIiIiIiIjIasygREREREREZjVmUiIiIiIiIjMYsSkREREREREZjFiUiIiIiIiKjMYsSERERERGR0ZhFiYiIiIiIyGjMokRERERERGQ0ZlEiIiIiIiIyGrMoERERERERGY1ZlIiIiIiIiIzGLEpERERERERGYxYlIiIiIiIiozGLEhERERERkdGYRYmIiIiIiMhozKJERERERERkNGZRIiIiIiIiMhqzKBERERERERmNWZSIiIiIiIiMxixKRERERERERmMWJSIiIiIiIqMxixIREREREZHRmEWJiIiIiIjIaMyiREREREREZDRmUSIiIiIiIjIasygREREREREZjVmUiIiIiIiIjMYsSkREREREREZjFiUiIiIiIiKjMYsSERERERGR0ZhFiYiIiIiIyGjMokRERERERGQ0ZtEvwblz56YREVEYXb58ObKP30RERNEXs+iXYPLkyW5ERBRGCxcujOzjNxERUfTFLPol4H1RIqJw4H1RIiKiSMQsSkREREREREZjFiUiIiIiIiKjMYsSERGRdW/evLlw4cL79+8je0LC5jOdbCKi6IZZlIiIKHLMnz8/pzXDhw934q+MHTu2YMGCup/IlStXoUKFypcv36FDh0WLFgUFBVkOeOfOnQwZMri5uRUuXDg4ONiJk+RSn+lkExFFQ8yiREREkaNGjRpWK/j9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du3q06dPnK6BGxgYGBgYGBjcmjBc1MDAE/74448HH3xQNtbWq1evQYMG5cuX79Spk/ewSe7466+/ZFdkihQp9G2KcQQ5xTRDhgy1atVq3LhxpUqVGjZsKBGV/pug/u+9917qZNOmTXH0iW+//TZ79ux8olSpUvDe2rVrI0KjR4+OFSdnAwOPOHDggDNe2n8Hv/7667Rp02w7TRIRrly5Mn36dHVyWyzi2LFjEik9UYB2XLBggX4Z183qpePcsnVIzcybN0+PN56AuHz58tq1a19//XXqM37WEgxucRguamDgFTdu3NiwYcPYsWNfe+215cuXewzM4x3bt28fM2ZMsDNjYh3ff//95MmThw0b9v777+/bty9+PnprguGQZh1iYfjw4bbIq7EI7MilS5eOGjVq4sSJ69atU4FkDQziAR999FGxYsV8Nx+h9F+DHBBFH0zojEQIOV6rVq1asfhO6NMDDzzAa/XQ67csNm7cWLFiRXJ7zz33qJtx2qxeOs4tW4cnTpxo3bq1hMS7FaZgyE/t2rW3bds2ePBgCZCe0DkySHgYLmpgYGBgYJAwiCBgW0xeuHLlyv84F12/fn2jRo0S7+zbzz//3KRJk6VLl8bua+WM31uNRwXDoUOHbFw0smb13vu8dJzYqsNY0Qn6S27cuCEuObcCF61SpYo6AKx37979+/dP2PwY3AowXNTAwMDAwCABMHv27Nj1Cb906ZI6Iiggvv322/84FzUIiL///jsRcdG//vrLxkUjAMTVewx8Lx0nVuowVnSCs2hyKluCc9EDBw74rMOrEzYbBrcaDBc1MDAwMDCIb+zatStlypTejxH2ghYtWlSpUsUlgeGiBgHxX+OiFy5cKFy48JAhQzymjx8uGis6IWDRbhEuumjRIsNF4wF//vnn3r17v/rqq61bt/7www96lMrTp0/v2LFj06ZNmzdv/v77753hKhDj3bt379y5c8+ePfGWYcNFDQwMDAwM4hUYAbly5cIsmzp16tdff/3zzz+rn86ePbtixYoZM2Z88803KsDy/v37v9bAHfW/HDT177//9unThxeWLl1a7gc8bVU3qQ8ePMhXli9ffv78eWdKvj5z5kx+/f33352/njt37uOPP542bdq6deucLoUU4bPPPps+fTpWtTMwNS+U8GxXr17l8Xnz5p06dUp+unbtGvYTuaJ+nB89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yCfuueeeOPqEQbzBcNHEij///HPs2LHVq1fPnj17wATbt29/6aWXSpYs+dBDD8Vz3hIvrl69OnHixHr16iVPnhzr2T1xXNTwwYMHW7duPWHChLCeev7555944gn5/4cffhg0aFCtWrVqRKNOnTpt2rTp16/fli1bYiufiQJHjx4dMGCAYoOrVq0qX758ypQpc+fO/eKLL7q3L1yoZ8+eHTp06NKlC5U5bNiwgFSKl4waNapu3bp9+/ZFHtR9WoF2xOJs37591apVGaGdz06aNKlp06bSRphZwXIyZswYSfP000+vWbPGe/uS4d69ewdkyMFAcfhcw4YN5c1kb/z48f/884/3N4Bt27Z169YNm5veIXfoVlmzZi1btqzHN/BRLIyVK1d6fH9kIFeTJ0+m46RNm/b/snfmcTdVbdw/SOYpY1HxoIxRUSqSoSgKGTKkZMzQoNIonwghCiFUiCjjQ09pQpmpFIXwIBQZCyHysN/ve37vvd5l73P2Offtdt837d8f53P22muvvda1rnWt67em/cknn5xNUucdElunaQHnY569ePPNN/+ZXDRZqu/UqVOFChX653DRNKXzMTMzZ86cAgUKmCnrHTt2lC9f/t133z13WUINAi56YSDgoucrsAtbtmzBi7rkkksiRjh27NiSJUtoqDfccEMK5+38BV3dL7/8UrJkSeQWk4smr4Qx3EOGDMGqkuCrr74a/4OzZs3iEcNFBbgWgVAvMrlv374VK1ZAVwiBYPz1119nn9u0j++++65FixYnTpzQ5YgRI6666ipcwAceeCB37tyIolq1alR3xGdhKRCnQYMGmcuKFSs+8sgjrmiTJk2i6yXcJdLNmzfnyZMHyqRLKHG2bNlmzpzpfdHGjRtDYcAnI+bk4MGDPEuELFmy2Csg4qzfI0eOIARUy0dQXnzxxRfK1bp16xL1oECWoNk8brgicq5Vqxa0PM4UZs+eXaZMmVWrVsWZftJArnCb7rnnHpL6R3HRtWvXJsrCpAWgyV26dEntXCQD3n///X8gFx03btzChQuTJambb775H8JF01Q7jacBVqhQoX79+imTH4HOLuCiFwYCLnp+45prronGRYWMGTOmDBfF6e/bt28KvCgFIPc0JhcVkkvCEB5+J0yYkCguumvXrgYNGmTPnt3FRUeOHEk6d9xxhx3YrFkzAp999tmzz20a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gAABAgRIaQRcNECAAAECBAgQIECAAAECpDQCLhogQIAAAQIECBAgQIAAAVIaARe9AHHw4MHUzcCff/75999/p24eLlScPn36r7/+SpXvlFCnx44dS/n3+uDQoUOpnYX/i99++41KSe1cpGmcPHky/jM///jjjzhj0hB27NgRfL8hQIAAAQIEOE8RcNELBytXruzWrVuxYsWeeOKJVMzG8ePH8+fPf/3116diHtIy5s2bN3bs2OXLl7dp06ZmGN6vpwwdOvSee+7hVv369YcPH27fmjhx4sUXX+zlYIcPH77lllsivnHjxo29e/emXpKc5//85z8tW7bMnTv3l19+meREkhGrV69+9NFHixYt2qtXr9TNySeffNKlS5e2bdtmzJixc+fOqZuZtInp06e3atUqT548aJF/zK+//hrbdc0119x4443xpDxw4MAXX3yxWrVqOXPmfPfdd5MjswECBAgQIECAFEXARS8cHDt2DN4SCoVSl4ueOnWqVq1aHTp0SMU8pFm88847ffv21f+//vqrevXq1BfU/ZdffnHFhORwa+7cua7w+mF4U1bVz58/P+J7N2zY0Lp16xMnTiQt2/v372/YsCHppxEuevTo0VdeeYX8pC4X/f7777NkyaK5YhQ+Yr0E+P3331u0aEFlxeSiSHLJkiXEvOGGG2ImO3LkyJtvvtkJj8IQH16aPNm9UEBjx4Zs3LgxtTPixqZNmzCDI0aM+PHHH1M7LxcUaGiTJ0/m14SsXLny3XffTZVFNEnDyZMnFy1atHjx4tTOSPIAg/bvf//7119/TXIKtN85c+b4v2L06NG0KTswyZowbdq0NNLFB/inIeCiFxRwjuPnolu3bh0/fvzZvxSnx/CrAD748MMPYel2yMsvv5w+fXqqrFKlSq55yyNHjhDuWvl56NChiy++eOLEia6U6WOuuuoq4terVy/a26dPn/7QQw8lOfNkNXW5qEvN8FdSnYt27NixWLFiqZiB8wWvv/56PFxUyJgxYzxcFIU/G32+gIE1eOaZZ3LkyIHMcYVTOztnAE147rnnli9fXrRo0YhjbQGSAIxhgwYN1JX897//NeFXXHEFIUuXLk3FvMUJeroXXnghd+7cZPj5559P7eycLQ4cOIB1ypw5M8VB25OQAi23dOnSPH7HHXf4RMOFI07t2rV1eTaa8PPPPxMnS5YswQarACmPgIteUIifix47dqxChQqvvvrq2b8Uj/yuu+46+3QubOzevTtv3ryuqQAIXo8ePfLnz0+teR1rOmZXyKRJk/DUvfuBP/vssyZNmhQpUoR0XEOkBnio11133ZQpU5KW/1Tnoi41SwtcFHn+61//SsUMnC9IFBe9+OKLY3LRP//8kwTbtm2bHLm7QPC///3PvmzWrFla46JYD7KkaaIffvgBB3r9+vWOJ+cBkoBTp04VKlTIxUCGDRvWvHnz+PdpJzsSW7PqZS4ALipce+21SeaiTnjwOiYX3b59e8OGDWfMmGFC4tcEV+3wIE7IOe1Sg5YeIBoCLnre4++//4aKYMQnTJiwcuVKLxf9/PPP+/XrN3LkyC1btijk8OHDd955JzFbtmz5/vvvw2B9IhvgQ7z99tsvvvgifMbM1/Xs2ZN0KlasSDpkQ4H79u176623XI+vWrWKZPv27YtL6pruW7FihQbIcVYoyMyZM2OWmhTGjx//yiuvTJ06ddmyZfYtSBel4EUwbe8yMJ9srF27dt68eSdOnKCA9ozxmjVrcKYHDhxIPuPMgxePPfbY1Vdf7QqksG+88cbChQsvuugixDhq1Cj77iWXXOKKf/fdd0ek/fXr11+yZAmFIpGuXbtGy8PgwYMvv/zymCt1P/roIwo1btw4OtEDBw6YrIqLEoJ8+vTp4xpkRQ+pOMKRFRKzb+3Zs+eDDz5wwvU7ZMgQ1E/hO3fuRE969+5Np+t//IxXzQwXpTgoD++lFlxPHTt2jPe+9NJLEydOjHmgF5Gh+tTphg0bBg0atHnzZp9EvvvuO3JCl1+gQIH3w/CP74TV8osvvvjpp59oHVS6vUk4WqOL2S6OHj1KqRECmoOQk1x2XATyIJ+Jd5EZ3qsa2bVrFykQQs5dT/k0JSd8/hB5o3I/+eQTLxf1yV5MLvrpp5+++eabJHjbbbdJ+EajSAop8dKxY8e6Muwj/wsDDzzwgH3ZsWPHtMZF8YapXFcg/nGXLl1SJT8XGG6++WYXA0ld0J8mdrCb7uBC4qL33HPP2XBRTS34c9GIiFMTXBYjBZDybwxwviDgouc38KuqV68Oc8BlhEdpHM5wUVy0pk2bwlFxvJo1a5YlSxa5s/jNzzzzDDFbt249ffr0H374wSeygPMH4cE53rRp07/C4I2HDh3CfSed6667jnTmz5+/Y8cOfCCYle1z4He2adPmoYce+vnnn7/99lsyDCvDm+cWriGmlhQefPDBDh06NGrUiKS4xPf1KTUJli9fnjfiQ0OcyKq5Ra5q166Ni8y7YI8kNWDAgJjZgA3eeuutRO7WrRv8PHv27PzXHs4nn3yyf//+ixYtEtN7+umnY+bBC/gSaT7yyCOucHFR/vBL4sjNJnguLkoFZcqUiQpyJbJ161bqnT979+5F7FmzZo12DOnXX3/NW/DdfbLarl079AeSAyWDuBqOLS46bNiwG2+88f7777/iiivSpUtnltghdoSJiHgQjkFB5ARDrtCxDBkyXHPNNTDhggULkgg6wy0ILaqyYMECLnPnzl2jRg2ejZglr5o5CVz08ccfr1OnTpMmTSpXrszls88+a56CDxP+8ccfw4WoqSuvvNLLpgSq8oUXXsiZMycpzJo1q2TJkmbOLVoiq1evJicUJ1++fNPDEI2MFp9a06JE2hGOAqLThGq0RhdPu0ACVatWheBt27atcePGPGtmreMvuxNW/uuvv57EsQk0ENwFRMrliBEjqMSGDRt27dq1cOHCyMdsfPJpSgI0tWzZsggThgwtvOyyy2wu6p+9mFwUSjlmzBgS5L0SvrgoBrBChQo0RrQROdNYevToIUYdTf4XDEaNGkXp7JA0yEVLlSrl5aKoPbY3VfJzgSFNcdGDBw9iSBM7yRZwURvnlIt6Lca5Rsq/8Z8M+kQce5wEXLj169fb667plOm16feXLFmybt06jSOfPn16VRSYod5zikAzzm/UrVvXHmqaPHmyzUXxYs3xkjj62bJlg95onQZ+ITHtYUufyDjK0BKzoVGzHLiqTsJiOXuyDp2GqNg+B3SObslMfPEIri0JKvEff/yRFIoVK2bWa3GrUKFCPqWeNm1anjx5zCVusTbl81urVi1lzAnP1EEV8ubNG082PvvsM7JBBBxuSJ02+sOXSNy86LbbbjNdS7Q8RARUlgeHDh3qCjdcFODZE4eC40krxMVFqVw4npdnUi4zC92qVStXtdqgBkVvouWTghPBzGriwRt6Iy7aokULWS4IMJfmtJ7evXtzaSbY8fvNob7oUvr06XPkyAGFIAPvvffe/v37N2/eDG0wK3b0+CuvvBItY141ExclkR07djhhtYFdQPh1F/IP+4Wk6RKzG7NTr1KlCnEGDRrEfzg2ahkzEd6IqptL//jwZC4bNGhANBIXjfdpdP7tgpriv0aRnASvBUaatLLD34hTrVo1M0VJQ4DLjRw5UpfUna1X/k2Jy/z589srC9q3b2+4aMzsxbNG95dffuEp2/TRatAxtMuEyEyZ9hVR/hcGZsyYoYUVy8OQibC56Nq1a99++23Iv3f1AY1xzpw5Y8eO/eabb+I55IakMAtUJVWwe/du+xaJYzrQZ8zmhg0b7Ft4PGQMa5wxY0ZlkhDiP/XUU1rvoEBlj2xgMNWusTO8jkuTc96LJaTI3qn47du3v//++6NHjyb+yZMnFYhOLrfwSxjm0n9rHHmQAURKU6dOJXF02xXHp9QCgTRhos2aNYvqkJCxhFzqP34htaNmruKjn4QsWLDAm9p33303PgzT9g0iMhASR4bmcsWKFcs9wN20H9myZQsSnjRpklnrYUArQwgffPAB1ffbb79FkxsaWKNGDY3okb69OslfXC4uaufWLpdPDuOpMhdQFawBeoIy4J2TB3ulmLBv3z6dqEROUEjbO//5559nzpxJfdGCXOpkuCjhamXelJ0oeuucyUU3bdrE47Nnz7ZPJBIOHTr0+eef2yExNSGixTCicK2cQlfnz59P9vh1fdQNXcWAjxs3jlswHG/eDKK90QnXFN4X6VNxcdIeoiEKuidym+qfMEyDQCXQJeSpX0BTkrtFE1aIuQVZRT+pyi+jwKdakxEBFz2PIXccN9GE2PtFMXCaSHkzAVdeeSUh6uFcXNQ/crly5Z555hnzFmzTxIkTZU28JAHgShouihHPkCGDa0qwV69ePIWz6IS/zcj/Zs2ambtaP+zzDRI8TiL07dtXfTm9sjwVuoR06dLZ5pLuQT1TzGzI9e/UqZMdASaAv2tkcvvttxPnxRdf9MlDRGBniew9c8jmopQXuRHtpptuUmfg4qK40XXr1nWlQGFhRGZGEYtDChCkaBszIBjXXXddtHzCw3n87rvvVv+NRTO9l3e/aIECBcqWLav/KB5aZ3ria6+9FjpqYlIQ1/pkiDfczwi2a9eu4kLRMhaNi9rj7togR8fmhL98w0tN+jpkmL7QR6nuvfde4tjudcxEXFzUP76mvrVWWfBvdP7tolu3bq4Pn9A3a6twEsqOc2DP+QMdm2zcTWUVeuPE0ZR0IpdNFew1ujGzlzQu+thjjxFi95roDNw+d+7caqFe+acFQEho1Ndff/11Z4LKhfXFkwLF7N27d9asWdUcgM7OFRfFX8dqoVfInMtGjRrZz44ZM6ZFixYjRoyg8cIS69ev7+/YQRJIgcaO+0Lbtz9ihOOL4UKFMBGvvfZarly5MCOmNb3zzjtkzM4kIfCZLl26yF4pkLLwCu17x3fHLJQuXbpEiRIa9uIuuSWkVKlSofAKbfN2qvjxxx+/5ppr8IznzZvHH7iQjJjW8GsHHQZk7969OM1Vq1Yl/59++mk0O8kt4qgBwpouv/xy5apMmTJ2/+JTaowhus1dnoJFyDpJA9u1a6eTpeBU1D7WEpbO5ZAhQ2jCGEb0QRl+6aWXzLuompo1azZp0gT50/vkzJkTJm/n2WYgmME+ffpgde25caSE/X/00UdfTYCOtGnevLkiICvaEWIfNWpU06ZN6Ux79uxp0qdGKlWqhL8Bh2zcuDEVEU1PPv74Y0RNyrfeeivViprFoySOh4v+9NNPNGEqGq4lW+STwzirzMbOnTvRQAkfG4hKYHxUTTQf0UJKjTGkdbRs2ZKWoru0OCfMiNq0aUO/zKsxa7hJyASXw6QvLkobLF68eCgBrVq1MrbOR28di4tSRkqqx/PmzWv2F+icCOqUB+PXhIgWg8aIVCUKmyjqMCQq65VXXilYsCDpmEET6oLckjeUFqqJQk6bNi2inKPZKIqPzmPueJDeAWXAXNvjiRExefJkcjJ9+vRVq1ZRfCraZCmA8N1339HEaKfYNzpidHvJkiXab7Vy5UpuYXnwV9FDXeL4URf7zgStj1s8a4+PnDsEXPQ8huiBPfplc1FtfKcbdg1yyKa7uKhP5CNHjmAH6U0j5iEmF8WxDnnOmNE0y/333+9E8rllwX2GM8mSFlLSNdKWTHiPHj0uvfTSiI/EzIa4KP20uQsTI6R///4umWg9YbQ8RAR8IxTp7BabizphKqhVrA8//LBzJhdFGnQ5OHCuFOi8zUpFQSlE6xW4i2Pqk1V9fgMxuroELxfFj3EtdKRz4im4+mVhmHAK4uoscb/wJFyC9VnLFA8XhZmEElZWd+/endrxjvB551IMxEXtbjhmIi4u6h9fXMheM+nfQv3bReXKlampiAXxyQburK0qRiG9XFSus+Giysx9993nxNGU8Jjt2nfO5KIxpZo0LlqtWjXMlGs8SD6Zlk975Q+hsqXh3SF/rgEVx0lt3749kkf97rzzzqcTQHNL1AeBCxQoEIq0Rhf/GC/ECbcg+aPffvutIlBl5vhNoF0bPls38WyIYNy+1atXm7Ojfv/99/z589vjlWhUhgwZypcvb/sx3kxiS8VY7EC1RCpUU3+4UxqkI8Qs2VBbME45hMHuzt5+++1QeD22SfPL8LFJxYoVw0bt2rULfoKzFa2kAqrCI+R5wIAB6BW+GiaLEBKPp9RkmxdpKQ0cacWKFZ988gmuM/yHmsXAEt6hQwdlAz6WJUsWuBnl0ngK/Qt0FCZmzpuBtPCIoTpaAmMvbrcZCK2JNquF/UbneW+3bt1MfH02jCIYUUACUTwTQUtFaBq6JD/mRAPYHYXykZ52dNtWIh4lsbkoMu/cuTNs3J6u989hzCpz4e+//6bVSy2xeDQNnoITar/G6NGjnTCX05KKUqVKjRs3bu3atVg5DRfSfMiAyd7evXvpW6nHn3/+WSHSUgSFh3D06FEoep48eWyy7a+3cufoPSFydEzbtm1TH0f2NOTKr5bC+XDRiJrgeBoj3g6UEsptd4KoJUbDXEK5ZVJkZpEPiZjiDx061DvabsPb/PGL0HCjfiQLHSWO9+gHAwgVOmM8gc2bN7t6yQC0TcwdtjHioo+lS5dy11gVlIRLo7F2IosWLSIR76fszxECLnoeQ72RPSZkc9HXXnstFH3PgIuL+kRWmtE2cMbkoh988IE6XTuC3JqGDRs6SeKiTthK1qtXTyOFeLcyiDzIeyPOT8bMhpeLfvfdd4R4D2Hyz0NEDBkyxO4yDVxcFOA4aikLtNPmolOmTMEEm5OEDCpWrAgDf95Co0aNQuHJ1Yg5yZs3L+5vtHw64VU6JKhD4elrvWcXmZguLjpz5sw6depo0yA9nz8XzZEjR8uWLX2y4UJiuShdmosOxYSXi8ZMxMVF/eN7uZB/C/VvF7gjNpGw4ZMNXPmLLZjMx8lFlZmYTalw4cI4nfZdm4vGlGrSuKiIllnfLkCeQwlrzr3yhxjY0vBp6ecCtBScWrMcDuGLNCYN0bio7dWJbWrttJZ841ufTIC+7Jo9e/Zo6zvUZdj2Ss460PSmvRbUSVBXTZVHy2RELkr/FUrYVS7o6DKtnxc0nU4L0iVectasWWfPnq1LGYfHHnvMTvbhhx8mEDtWt25dWEHEMtpQx3f77bebEIRp9xHxlFoyt6c3BXED+7PSmtP7+uuvTYgsudmGjRBy585t9mzLIJsiO5FWZrZr187WeWrZkHlcTE0bmiNYqQu6GLiZUQkNod55551OggVu3Lix6eZM7UeEl4vGIy7DRWFQzZs3d5367p9DJ44qiwidsmHLTZzQ9G7iYNWrV7efojcnkBZkB8rQUSi7dPZ2ADUi+KoWo/rrrYpTuXJl8zjCr1SpEoFmNlhLmXy4qODSBCdSYwSavzWdIH00NtZI+/jx45rblJbSTtOlS7d69WpFhhh7PRwbrjfu2LEjc+bMrVu3tuOQGnEKFiwYbdQYwo87gYtiQvBVKlSo4PPefxrwS/HT4Jy0cdgBni2iNs1206ZN3CUQOkqVYfa/jLQ0Gt0j3GylSQEEXPQ8hlY22rNtNhfVIlJ7bFjQ6ggXF/WJLDfUuzpUq7liclEZF5cdp0c09jQJXNS0HIw4HlUoYeBT7pdrlhIbevTo0ZjZ8HJRWXnvkJsEGC0PEaHBS6+z6+WiTkIvjgAhbCYQL9+75e+rr76qUaOGK5B6UYcRcbaWvpyOKlo+8Yw1G/PDDz/ccsstofCCIpNVHy46dOhQKLRhAjG5KH1eoUKFXF4vvDfaZEViuai6XtfSHcxxtA/eOJG4aMxEXFzUP76XC/m3UP92cdVVV+XNm9d12pOaZBLKniguGrMplS1blv9292Zz0ZjZSxoXbdCgQciaKBNoNSi8vUY67ZzlM3/+fNvfQmhn8+2NaFzULi/WnpDBgwc7CWMHmIK7PHDtAjUgXIaFfse1a71YsWLI2dWcIRI2T4iYyTi5qHJub4PXZxXtSTaz2hauorKjaXayNBwtSY3zU0Dek2M0kWi0Lp5SQ6siWn4vF9WiVnuFpwwadMVbRhxNHbZnr17xMhCf86s6dOjAraZNm5oQuCXUwqsP5sQE5blWrVoRt8W64OWi8YhLXPThhx+mLN4z9mLmMGaVRYS3LrCrmiFUk9SiD9fgqc53WLhwoR1ID0hgtmzZzOB46Myziyh+4cKF7UAfvY14dtHYsWPtQFnmmFzUqwkRuai+Um5atxblegWufWHyIfFShg0bFs/HWlxvnDhxYihhtbMNLTezB2VcMO8in7Lq/sPr/zSgyfhpaCa9oVl2ZIYMdEaRvSLJDG8ZGDbr/3WD5EXARc9jvPPOO6GEA0sEGS+Nq61bty4UPgvHVjW0UyN5c+fODVmnxfhH1jY288kWJzy4Ih/62LFjXnNpc9G///6bTih9+vT2lMW0adMI0T7+JHDRkSNHmtT27NmDNdSOlwkTJoTC+4js5W19+vTBZsXMhpeL0mixnkSwDwbgcTlA0fIQEdu2bQuFN5e6wvFUIp4zpLNe8Px0iSgyZ87sdWjoFSJ+L1SPe/OjVcfdu3ePlk+EYDwAODx01ByW489FXVNh5cqV8+eiWjqlnbcCFdS5c+do35vxqpk/F9WRfTVr1rSXCA4YMMBnY4mXi8ZMxMVF/eN7uZB/o/NvFw8++GDozHOD8Z9eeOGFpJU9UVw0ZlO6//77Qwlnmwniohr+j5m9pHFRTWXYOxhB6dKlzQ7JtMZFbWzevLlUqVJnk0L8XFQGR7M6Ns+JB9QghogH8+XLZ86mom1qM5trV56Uyt43nuxc1PX1skWLFsEzhw8frrO4vJxTazhvvPHGeHwsf2ITZ6nPnovaY81kGw8eFkT1aYe2LaX4uej8+fNVifbYn+YtfXYx0OmLzF900UU9evTwiel4uGic4hIXrVChgqrJ1R3EzGFycVEnwefRLG5ELkr2QmfOeQqZMmUifPv27U6Uc3R16oQ9hRhNbyNy0WXLloXCm2B1ee646P79+0NnDvd4odXLoHz58jE/a+d6o5YM2DOcgg6QN0f6RQS8HVetZ8+eVBD9zgV2KPpZAt0Tydy4cSPNzRxWpHXdGzZs4D/uE3fXrFkj1upaiKtNpDt37kzJbAdc9DwGlhqnUJ007ItLzTlcf/31mhPTIp+rr74aXxB7SsdQr149uYBagFq/fn2e0iiXT2QNXtIDQWPgKk8++WTt2rVNlwANg3jQq2E61bdpYsQMX2Gv6YfMTiTCcT4ef/xxXYqnNWjQwJRLR/D5HN6FW2lvGsESyU0hZWy0JABXHD16NHbNkCv/bEggrqF0rQTLlSsXXj6MlP71pptuUqcVLQ/RULFiRXPqrAGUzPVGgUrhRYaLUoQMGTLIlBioT9q7d6/3ce1CwUa7vuQxb968kGfuyAZc1J5opVM0U5HPPfccz9JZmrswTEM4Ndb7zjvv7NixY9iwYTowk25SXTIa4hq5XL16tVyTDh06kNupU6dWr17dHuzwwqVmVAePo4omgsikOmBMsL4jgqLSq1H1rVu3tqmvF9qpYtPCmIlQTPssZf/4WpHr2oXr0+j82wV9sJyexo0b4572798fhdF8RRLKrsNsTVtwEs4uMsdU6uwiRKRL/6akpXTUF1Tn9OnTu3fv1rqyNm3akKB/9kiKlGksPrl1Emi8fRIPL8IDy5kzp/HA0HZarjQwmvzTCIYMGRJt92+cSCwX1Timd1FGTEBItAcSQIqccJXpxBfXxLu2clWpUsUnk8nFRemMKC8KoNahgSovF0XTtArRXjkcDf7EJs5SJyMXRZOrVq3arVs3dawaHEwCFz1y5IjcBteKSg0heb/IbQOftVOnTjLdNFKfk65cXDROcZk1ulpQ7TpKMGYOk5GLQq5weGSKI3LRmjVrhsKnUrlSoys0ByhG5KLaWqVhO3+9jchFJTGzDPjccVH4Hv/pVX1E54TPT8L5kb9hn53uheuN5mR+VzTJx8cZwLW74oor6AJ0GXBRFzQvCsx+0a+//vrL8HlF0ATdMquW1q9fryW75nHauAhqPHPdyYiAi57fwCWV3cmcOTM0bPLkydmzZ6fH1VQeCkdTxy8kAr9YdjPZKNctFD7DUJNdPpHBuHHjcufOLRcE93fPnj3mllgKdwcPHoz50/c51JEYFYf/lCpVCruGR9isWTM4nsk/Jj4U3qeEq0GuiKBOq3379t7FA8KIESPI9rPPPott5S2U18yxYJpvv/12dZbYPte0YbRsEK6uBV+WUphuify88sorWbJkUYnwnk1X6pOHiJg5cyYiMnFWrFgBC8WM0uF17drV+/nHXbt2lSxZUv/JcK1atey7s2bNkkN/3333mS1AAh2naFUovOPFdjhgbrB0n0xSX/ArOgPS79evH+RHopgxY4ZGxHEa0Bby1r17d70Cv4F+F1Khba5ly5ZduXKlupmiRYvCB9QLynE056Y44bMWdYAHoAv0J6LOmWqGbZVDXKhQIfo/jCbOZbZs2dR3ajCbmhIF0lM+3ifOWd++fbX+sH79+h9++KG5FS0RCqKDW0Ph417M6Hi0+BMmTFCHXbp0afwtM94frdHF0y6Qs1wH+YW2bOMvuxN2gPRB0SJFitBe6MDo7HV6By2dZOn1daIVgai9Mh+tKQnUuxau80jdunWxCbhoqJ/OhvWRKnxVoqDdubxDAyqINEPhbVcDBgwwn0k4evQoLiwywQPu2bMnNN5sd4km/zQCyJiWziYZieWiOsvHfHjJAPWLtpcS2256BKyKPsIsw6WJLBfP12CZzl6Olsnk4qJPP/10yNqVEJGLYoGxbLjyWcKIeVRVTGITT6mTkYvecMMNyNw4iEnmorBZAps0aWJCaA60ek20am2FDfoXqgkv1j62SpbHu7/AwLtGNx5xGS7K67SN096Q6Z9DJ1m5aJ48eaCj+h+Ri8r+u4aSMdRYaYSjy4hcFC+CODJB/nobkYsuXbo0ZO1APndcFF8FO0y36B1x0C50s5OZsrz44ovqjn1OzXC9cfbs2VyWKFHCFU3zxq6d/waq0IEDB5qQgIu6sHfvXsz7kiVLTF3QgxOC6dMt+m6zMGTnzp1ajmse37hxo4udpgwCLnoh4Pfff5fX9ddff3mPLycES+1d2YKtwVq5VitFi+yE7SzaHHEoFNc52rHpNg4cOJAsm6Flx8nkhg0bvMf5OOGhHbIabSFWYrNB90/7dG2RipkHL+iZEnU+iqHiePbxbNHxhw6rsBmLF/9LABVqJpTiBEqoTwIKSDieo8B5S7QRBy/iVDMbVA1KfpYjfIlNJLHxfRpdTOwMI1mykQT4NyX0QZP5tB1vYzxH2SNBuG5i9SQVQcPB54v4MUkBt8Bnr6+gc2jsUvtzUcy4hhvsQ+mwaS1atIimTiQ1a9YscwlJCCWcjTRy5Ej+16lTx44/bNgwymX7NPnz53e5v5p7sU9ncZLERXVylfHp5bDan4bevXt36dKlpY06Sa5GjRr+31ONSWziKXVycdE9e/ZoZMfMdYjG2EsZ42EgeKjp0qXLly+fvaBmxowZFBYPNRRe/WRvxMA4N23aFEHRhO3POOn70jrvPSI08W6vwIxHXPY5uvTgOXLkyJQpk+mz/HPoJB8X1SIpcypsRC4KASbnuXLlsjcEadu8oeheLoqRz5s3r1kG4q+3EbkoreCSSy4xi6uTzEW9FsPx7BetXr26qsy20oMGDZId6N69u73Gu3Xr1kS2ZylccL3x6NGjWgi9YsUKEwf1hrL6nIvbqVMnm4uSSOjMjQABkKF2ipoxBR1QhKpozhOYihNNtd1C1FXzDSmc7YCLBgiQQsDpvO2221LsjGwXHn30UbyBVHl1gAABokFHWLmGugw+/vjjUHj9m3dnmg15n9OnT4dk6huqzZs3d00raYOW8YP79++vqWlYEJQAH7d8+fI+27RwZO0JTPzmbNmyibieOnVK39QxmaQ4xYsXd20I18S+vdcAxxRqkTlz5u3bt2sjk5Pgbtpzbi+99BIhzz33nAkRsTGzUvqM57333qtPHWrp+/XXXw+pgDXhSeNPG2pBbrnlIrdeLFq0KBQ+3smEqKbMeT/xlFofYrFPABZEQuzlMPL77bMJmjRpYiYS8bm18IRa27hx4xtvvKH9ip07d543b54IqrbG6EM4dgoTJkzQJURIB8PYpytDpWA78k01JZU9e/b7779/7NixcELia90NRcuTJ49xYf/880900l5C4oL4GzSPKkaHYXrxiEvVag6S1Sm4+fPnN2t/fHIYT5VFhLio+QjqiRMneAs9tRk+054X+xQuQQMNZtM+fBiB2w82btw4dOZZx+hwpUqVzLCjv96uXbuWy2uvvdYkuG3btiuuuML+SLJ2K7i+0xZTE5xIFsMJ7zoh0Awv6mxt1WOfPn1GjRqFEMy0LR6FXXdPP/00WfWRs/eNaAJajVUxC1VQbNcBCi5oeZQqHcYFx8YKYVhWr17tc9zRPw1aebt48WJUaNmyZfznFzOIin7zzTdagsstKKioqWGeWBKFROuPzh0CLhogQMoBl+uBBx7w2Qp7jjB8+HDzabgAAQKkHeDblStXLtpd3AJROH27NRpwZPUdJrzbPXv2wFi0ZB1fXxxs8ODBcjRx9RSCXwJH0tJ0zS3MnDnT5xVw0SJFitxzzz2TJ08mNTxLmx7jTfbo0YPEKQ7UsXbt2vb+CJ6VN6x5ntGjR5vpETxaTXbx4OHDh4cOHapvMJYuXVpTo7in2o4OJ4Ez48dDmMWpLrnkkiFDhpAUXmmuXLlC4SNM+/Xrd/LkSW2JxM1dtWqV9izwrN6IE1a5cmVlhrdHPL4YNw7iRAS4E144HAxCVapUKb0CuWkizqfUlKVXr17KVcGCBQcOHKhlI//973/lT4fCG7DJ+e7du3v37i2qCQ/BWSdLpgbLly8v6khJtfeEWoAEwkh11itFwKfUofqh8KlgxOct5EcHTV111VU6SEyUPlOmTPckAPkUKFDAHDQIw2zVqpW2DITO/KArvinSvuGGG6i78ePHU1Jz8GFE4PiK48EbbZoXTVxUKyJSrZElFGz//v2ffPKJioAYH3nkkb179/rkMM4q80L5JEsIHzFWqVKlS5cuZv4ZxquBA15K5l2n06OiKGf9+vWpL5jkM888Y68GQtPQdmq/Xr16jz/+OAInBfurjz56KzJAIE24TJkykK6HHnqI1OyZc5i22bzdrVu377//Hm2PRxOcMy3GgQMHyIlOGwmFP5pgVoZ/+umn2g2kquzbt6+ZI33sscfIG69DYyGi5Dna98kivlGBFAcGi+RffvnlDh06wN4jHoFhQGPR5C3V0bJlS6SkY/yoBZt7/8Nx6tQpdM+clLtixQqzQZSGpu+1CJBSe2XTwYMHFZ6or1snCwIuGiBAigKj4O/zJTvwWvyX5gYIECC1gHflPwiN/41DbJ+ZHBE7d+5Mwg4IvJb169fzoP+CVSc8gUYcPNEtW7bg6ERcgU8ErE1i13dt2LDh7IfhkRLOqMkVtIecxCxUsiBppU4CUBV98EnAoY+2p/psgLe6evVq1+e1KKPcU4qJLxvP94cgXT/++KN3b/bZiytiDpMMs0YXedoqFD9oej7KRvjWrVuj8bR49BZpU17/L64nAfFbjO3bt2MlXJLRcBJ1gTVwfTY2sW88dOgQQohzG7/0ypYGBiStHQGQFoBMaCPI1rtB5ujRo3D+33//3R4ZSV0EXDRAgAABAgRIo8AFbNy48blgHQECBIh4dlGAAAFSEgEXDRAgQIAAAdIiTp8+3aZNm8WLF6d2RgIEuDARcNEAAVIdARcNECBAgAAB0iiOHj2a2lkIEOCChb72ZD4NFSBAgJRHwEUDBAgQIECAAAEC/IOwbt26tm3b5gzj5ptvHjBgQDz7YAMECJDsCLhogAABAgQIECBAgAABAgRIaQRcNECAAAECBAgQIECAAAECpDQCLhogETh58mSwiOVc4++//zYf30sWHDx4MM6Y5qtfScbZpxANf/75Z9o5f/zCA7JNm/sSfw0j4q34FTt5nw0QIECAAAECJBcCLhogLkyfPr1Vq1Z58uQxH0EOkOxAti1btsydO/eXX3559qmtXLmyW7duxYoVe+KJJ+KJ/9prr4VCoQ8//DDJbzz7FKLh+PHj+fPnv/7665M95X84EOwbb7xx77335siR45NPPknt7Px/nDx58plnnunVq9frr7+eL1++q6++evPmzbo1c+bMtm3bFi5c+Omnn05ssoltFAECBAgQIECAc4qAiwaIC7///nuLFi1gGgEXPXfYv39/w4YNEXKycNFjx44NHz6c1OJ0u2fPnl2mTJlVq1Yl+Y1nn0I0nDp1qlatWh06dEj2lP/hQLA07XvuuQc9SVNctF69eoMHD9Z/NAqq/MEHH+jyzz//fOWVV8hwErhoYhtFgAABAgQIEOCcIuCiAeLF66+/HnDRZMfWrVvHjx9vLl9++eXk4qLg+++/93G7Z8yYsXr16mR50YWKnj17pnYWkogTJ0707ds3zsj9+vVLU1wU/Sc/u3btMiGu5dlLly5NGhd1YjWKAAECBAgQIEBKIuCiAeJFwEWTHceOHatQocKrr75qQlKMi27YsCFHjhzffPNNsrzogsT777+fLVu21M5FEtGxY8e77rorzsiaZkw7XBSSSX589q8uX7484KIBAgQIECDABYCAi57H+PTTT98P49///rd9CbS3il9dHj58WI8sWrRo0KBB/fr1+/zzz+2kIEWTJk3666+/oChEMFuz/vjjj6lTp/bu3Rs/1YeLnjhxYvbs2Tz7+++/T548mfSXLl1qR/j7779nzpzZp08fElmzZo19i5eOHz8eb5gXLVu2LGb4wYMHR4wYEe04EzIwduxY8rNly5aRI0cOHTr0v//9rysOGSAbAwcOXLFihR2+du3aefPm8eyUKVPsuUoX/vzzz/fee2/Xrl3EnD59ev/+/b/77jvdWrdu3fDhw0mcbLieQuCIhSyRMYVQKXfeeScibdmyJXWkb20bLnrgwAGygcRckgTbtm179913X3rpJSLs3r3bdRdRf/bZZ6QzYcKElStXRnS7N27cqA98kyVevXPnTgJPnz69ePFi+3UIecyYMfzZu3fvW2+9hTB/+eUXJ7ywc+HChRScbPDfxPemQGHJBn/Wr18P5X7zzTddxzLxyJw5cyjL22+//dNPP0WTOdi3bx95sEMQO7qKSJcsWWI01gYVROI//PDD8ePHqSmEiUDiFCZ6njlz5osvvlgt6OTJk64Ho+knQJ5klVbz4Ycf2vKJqZw+zWTPnj1apIpuDBkyRC06WvyePXtSuRUrViTnKIMJj6b5NhelFRszYp5FwgrxnqpFWWjyTngr5oABA8aNG2crP/X7xRdfULNU3xtvvPHVV1+ZW6tWrUIIffv2RdQIU4Gkz1tuueUW8jNx4kS9lD+DBw+mmsyzEbloNLE78TWKAAECBAgQIEDKI+Ci5zFwsjNmzIhftXXrVifsil1zzTVc4pDJFcOBbtWqVZs2bfT/3nvvvfvuuyE50J58+fI99dRTTtj5e+GFF3LmzMmDs2bNKlmyJH/atm3rhJ3FsmXLEogfjA992WWXReSivC5v3rzcgmyULl26SpUqOPFcvvjii4oAbbv66qtxOo8ePYo/fdFFF4k86+3ly5eHJ/zvf//76KOPsmTJ4h8O8EpJ/KGHHnJlA3fz0UcflUBwXosWLXrdddelS5eOZ0nBRHvyySchUXBy8mPcWZjVrbfeymW3bt1ghtmzZ+e/eJcL+LL58+fnLtypYcOGnTp1KleuXPr06ZEVjniTJk3at2+fKVMm+5QdaEPTpk15EEe8WbNm5Af+4IRHCp555hmSat26NSWlNp0ELjps2LAbb7zx/vvvv+KKKyjC3LlzTWpwiapVq0LD4ABdunTJlSsXJMrcxeOvXr061AKZw6uvvfbaiG43rnz9+vW5BS3h1b/99huJUEeE8KzRigwZMqAYkyZNuueeezp37kwtkx/UrEOHDsi/QYMGxEeeStOVwsGDBxEml1dddRWkq06dOvXq1eOyVq1aJhtQxNtuu40ikwG0kbu8Ah2Gstq53bFjR8eOHVEbmKEJpIpr1KjBg3/88ccdd9xBnbrKCPkvXry41PKuu+5q3rx5kSJFqCnqOh5hwmeKFStGVU4PAz20E/fRT1IgtwsWLEBuuXPnJpOofTzKGa2ZkDc0hLpAMih/wYIFSYTEo8U/dOgQd4nDK8jh/PnzlX5EzRdsLoqh6N69O5c1a9Y0FBH+zNtdYwHbt2/HnhATNUOTS5UqJYFTOg24oPP8J4QKvfnmmynvv/71L0kPo4QK/fzzz99++y0aS0E0oCMuCovmKR7n/3vvvSdFQt9sBXYVIaLYdSvORpEWgPCh7jIFAswZEg6lT94XeZPdu3evzwBckjFt2rTkWuVxLoD6peXsBUgt0GtjUmKetn326n2O2l2yYPXq1fZQZmIRpwwDBHACLnq+A7qCX2WmRGj5XL7zzjsmQt26dTVlhAvOLZxvheML4ryaWQ4IJHcHDRrEf5jPjz/++Oeff0K6bCsJy4o2L/rSSy9xC96rBPFECxUqRIjm+nr37m3+A9zTW265Rf8x5Xny5DHpkCu5R9HCnfC8DaQalzqiQHA6edeIESPExskt9OPSSy+VV418xMwFiBCR8Wv5j83lP1T8119/pXvw8f/w6YmJv65XwM24hNubObfnn3+eELP8FeZmpnTwj7Nly3bJJZfo0zhkT2TJJC4u2qJFC2V469atXMIbdRfeAifBgzfxYYmEGNlS3Q888IC5O3ny5GhuN4F2JgFqY5ikAKMmxAwcSLtgOMhHIRCMHDlyGJ7mTQFuCZ2bPXu2LnX81caNG3XZr18/Mm/6KogKRCuizKkLaLDNRUuXLg1j138EggZ6n3rjjTd4HTRYr9i0aROXkFLdjSlMSpo1a9aI+Ymmn7S1ChUqGIFI841A/JXTp5mgNsRE1BAVCDz0bP/+/T7xabzcstfo+mi+41mjiw+RM2dOqLspCCHQRW+LgKNCsJGSSUrLaxs2bKjLZ599VjSSmFgVjarQgmhoZuqS3BYuXPjyyy8334si5zxFuC737NnDJa3evNfFRf3FHn+jSEVQrZiUXLlykTfb6qL2hHgXR5wl7GTpPmrXrp0uXTq7fSULaFy8JUuWLGnwa0yTJk0qVqwY2Xv00UdTOy8B0hDoc5s2bapxQ7t38OIs1fvctbuzx9ixYzWMaFvO+BG/DAMEEAIuen4DSiZepMsDBw5wWbVqVV3u27fP+KN//PEHna6xC5r62L59uy7x87i01yhCinB/zcSI47tf1HtLn/fQpBnuMp6fsdfXXnstZk7/8aqJ1rdvX7m5P/zwgzzUaOExoRNBjRcLNHWj2SecD2zrmwm4/fbbzfwtjjL/O3XqFPMV3s11uXPnvuqqq8wlzJMI77//vhOeO9JSWPPSK6+8kpAFCxY40bmoPdRaoECBsmXL6j8Od/ny5e3M6JQXSs3/xYsX8x+6Yu76bI3zclFK5GKSd9xxByFGB+g7uezYsaOJAL0h5LfffouWAmIh/+Zy0KBBRDBDrTVq1LDJHvrJ3Wirr2+44Qa7zy5evHiJEiXM0tyIhzBRBZqUMyH4DVWqVNF/f2E6vlw0mn4+9NBDpG/qumvXrkSrVq2anvJXTp9mAi655BLYoJ0Hn/heLuqj+U4kldaMvXTYCat0tGOcYK0IylzCObVwQMXUcIA5AtcJGyUI/yOPPGIn0qtXL3ukzMVFecSfi/qIPVGNItXRsmVLFxcdNmxY8+bN4/+qs2sCPxpcyR48eDC5fGI7AzQKqobKPftkzwVQlQuSi8apAwGiAateuHDhmDzq7NU7GdtdsuOtt95KMhd14pZhgABCwEXPe5QqVQrnT/vZxowZo5W08tFx/adOneqKDwvCB73pppuIZrariYvCV020mjVrkpT9YKK46Lp16wjB1TYhOKl48Lz6sjAUiDOkVcGVKlWy9/JFC48Jr7s/cuRIQuDGhw4d4k///v2/PBPapiguavslCGe6BbPFzuu4Q7dsLioKNHr0aCe81JP/c+fOdb1U/C0eLnrFFVdoZSMCxIm/9dZb7fISSPwiRYqYZ+0tiMnLRRGUi4vyn5ANGzZES8HFRV16oll9MyACY0+fPr13R6Lg4qJjx47l2UyZMqFR0R7xclFDnGIK0/HlotH0E0LYtGlTV12bOUMf5bTz4G0mTpiLXnPNNd6cRIzv4qL+mu9EUmn0E2kbklm3bl2zz9kFFxcFTZo0ITWtuRUXNVPrTtj+EOJy4OCKBKIPukwsF/URe6IaRapDs8pJXrOHWnbp0iVpz1KPZ+8Tjxs3zl4Dn8Yh+3CBcdGz0YEABnQ3KcOjkqXdnQuoN08yF3VSUIYBLgAEXPS8x5AhQ2jwc+bMOX36NJ4x7ILLnj17cgnhxFU1MX/44QfYxbRp05wEKuLDRQsXLgzFtV+UKC5KUqHwWlNdzpw5s06dOnJP8VxtJ3v37t3aSagJXrMOMFq4P7zuPn4wIVAX3h4Kb6aN+KCXi+JGX2zBOMpxclFRIM0Pe89PEhLFRRFIKLyK2JVIwYIFc+fOzZ9WrVoRYf369eZWynBRQ2kSy0VhIOnSpXv44Yd1WaNGja5du0YUlOPhok54lR0FJ0HkY5aq2vDhojGF6fhyUSeKfubIkaNly5bRHvFRTl36NJOIXDRafBcX9dd8J8o5uh06dAiFJ/D37t1bs2bNaM96uajmtzdt2uRE4qIffPABIa5PxW7YsCFkrexNLBf1EXuiGkWq4yy5aLNmzVzDK/Hj7H1i1CxTpkzn0fbLC5KLno0OBDAIuGjARc9rHD58GId/8eLFy5Yto/uzl5Hv2bPn22+/Xbhw4ZIlS9atW2cvfuSpNWvW8NSiRYvoKG1GcK4RcNHzHvv378eWNWjQYPbs2XLOqlatCoH5/PPPzbkyYMWKFUSbMWOGLmNy0bJlyxJiDuB1EslFtdERZsX/oUOHXnTRReZrgbbTbNIn85dffnkofCaQT3hMeN39cePGEULr+vXXX/lDV+16RNsXvVw0GhLFRbWY03UYj3lporioE14MjLdn2w4FalW2libatZDGuSj4+OOP8+fPD2Ho0aMHeuKzuszFRaUh0KR27dppMtM7WuHDRZ1YwnR8uWg0/SxevHihQoVc68kPHDgAm3J8ldPxbSZOJC7qE9/FRf0134nCRTEOBNatW3fEiBHkM6IcnEhctHXr1tSUqtLLRVevXk1I9erV7Ue0/NssA04sF/URe6IaRaqAfKJFSHjbtm0RuSh+g06nM1i7du2ECRMo1C+//KKNFZRdp39VrFhxeRhGGvB8fBEuZ82aRUWYZuJK1vjE5GfSpEkTJ04kP7pFv7A8AQrZsmWLLs2iAHwaLckbOXIk4Waxw8mTJ+fOnWsPiQp4qDNnzqTVYIK82+2gtZTRCe8ERjJoZsyxyOUW0D0y4Apxwqeg6fLQoUPOmVyUNjJlyhRCvEetIDr089133yWCWQNigzbIgx988AFCMBsWDCggxaSKZQTiAX36nDlzxo4dy7OuglME9Q7EmTp1Ku81zSQJOuBfNNXdkSNHqCDc1rfeesse8iNvRrwU3GRPIUYBosGrwwJVoz0L2Fj+oIfepKIV5/jx4/Pnzx89ejS/3sUypIO4uIuf7T0X3Qk7LbwOqfLqOHlURPWOVrSI8Gl3NijO0qVLx4wZQ7L2h5eNnpsqoI4U4jqXPp42RW+IdvEWjEM0Luqvz0mQoRdkDKZEJqlHiJPrqwQx22MAGhFKTlXqF+D/ywaiPAoxtyCrssBYEsROyFdffWX+pNjRUwEXvRBw33334ZXS8tURYgcxAfhnxtd0PPMDOprSh4tq/SRuqAkRkTDn0NjwcgxIL1lS+q4p1nLlyhmnGcfFGFaMTo4cOXS0TLRwwefDg153H2e0RIkS9BkYOHhR+vTp7e/Z8JZnnnnGOWdcVGuVcZTtbZC0cDn3dGMu8ubPRVWJmtkWIGOEDB8+3Ek4Oqhx48bmrtzuxx57zFsKuF/IOr3GSQ0uSjW1b9/e+/2biHBx0eeff978lwdva7vgz0X9hQkqV64cbcQ6mn42bdo0ZO3DdMLHO3fu3FnOio9yOr7NxInERX3i47jwIqpPl/6a70T/vqhW25KynWcXvFy0bNmyDz74oP57uSgCKVasGJmxPSpqgRDj6SaWi/qIPZ5GkYr76/Dvy5QpM3ny5Hnz5jVr1gxRGy4K2ejTp4/OprYFiOY3atSIUuBDIGqK6YTtTJcuXYiJuegVBhQCTdZeDFgNiWsO/8MPP4yYrHxi7mbLlk0xqREdD4YF0LllQLoK5Rg1ahSXpoHQIiiInFfe/tlnn5El1DtfvnyungUntU2bNg0aNPj0009xWyly6dKlzaAYeaZFiNM++eSTFEdrH7wHp7swcOBA5RBOiLeKQ4+UQuGjufGrxMrgBtWrV0cmLi767LPPEk2HtWBs7dzShREfTcMmv/baa7ly5br77rttggFprFSp0hdffIFbjJpRFnOL1yH2l156iUJdf/31SNgWeDTABFq0aEHP+8QTT2TMmLF+/fpyBxFX1apVNahEdVx++eVFihThErGLd8WvA1pH7VO0nTt3kpTqjraGmlHRehabLx1YsGABRokQrITZt8/jWELi+zOQiDqMu4wAM2XKRBWQJfKjl+JI6DhGGrVPcRYvXoxSURCsWcGCBdFw4+1gAB9//HHsJzFpaPypUaOGbdNIuUOHDnXq1Pn4449xXbCcOnzRpxTR1Dti0Xzg0+4MaE3oFS0OboZWIBA0Vn0KDBZTxlM333yzIuPJ6JhJY//jbFPIH6eRPhop4R7ceOONLi7qr89JkGFEUC5qp2fPnps2bSId3mL30THbYwAnPO6AfLBIdG1Yb5rwkiVLUBUnfII6t7Zs2YJJPH78uC7lneJB8X/16tVUJQ/SfLjU+EUKIOCiFwK0Bcsse4Oq4Ry7Zh7keRMHvkpvXaFCBXmf8uB1horNlyAYGTJkIB26QEw5rZ0elzi4Ed5vOYpjaBbUCfsu+PH6ZowTdppD4dN98WAwsphvuliysX37dlxV85QTPklVk4TRwp3wGj/vTj8DufuaaHLCo+958uTB0OsSG8pd7NcLL7yAXw5Lwa7p2y1ax9iuXbuY0tYpnbggJgTLThnNpc4uMpsA5RLRNSIlXBZchHr16qk710vxNrC/Ol7lueeeCyUcZiPQ3xuOgftOcegGzKAvBaFe5EyTiE6GRFZYGS41Z0h8755bLR6m2+ZZHaSE3Xc59DptVX6bkzB5hSKZCDq7yHxe1ZvClVdeaZa8ApzgUPjTQbqkny5VqhRe1+zZsyk+fSH+dzSxa6Le0AZYrvEAJk2ahJQosusRDcoMHTpUlzxLL27OK/IXppPQKLDjGPFVq1bZKUfTT+x4unTp1NDQkKlTp9IMzVlN/srp00yc8DJUHAU7DzHjozawOLwifn0030k4OshWaUEjKf7LtPAVeLX6OUDlUiiypEup2XvvvWc/MnfuXKRkdrUhcJozzqKJULNmTZ4y4+7kMxSeoTURdMqUecRH7DEbBW/BZ6KR+pTxHOHtt9/OmjWrvu7rhOWAchouihWlNuH5NmnUYmbjZFNwfX/LSRgqMoaR1NBwNWE4DI0Law9twAvxJuuE6xEnmBaNWv7+++8YK4nUHPtEtRouKpB5e7BG3MCMo2E38CZ1lqbtrNeuXbtKlSpmTmbv3r1YiSxZshifVWu8aeA4tU6Yu6oGo+10EEgQY2ILhz6L9s6zdrSmTZuaEomL0kxGjx6t/GgEdvDgwYqAHPLnz2+GbJzwIAi9D9Vk5IDyQBL0H0tiVlWQYLVq1Uxjx7JBNiBapmlEBHlDPuZSR4iZlqIl/QUKFBgwYACuJK/QKIxZNBSnDqBy/kXDGUVPeJGo77fffsvrYHH69puOQnASzqIzO3GEhg0bGgsfEdF0GIXXaCbKQMa2bdtGg8WyEYIqYot8ikNd08MaNcNpCYUH0TQGgU0IWeuPEFfozDFKOjU8FlOnGBzRYB8eFVG9fZpnNMRsdzp9jRKZRygIIWZvi/plw0Wd8NSlzUWdONoUlIMi212AxjWM8Y+pz0mQYUSgXSiesQ903xMnTtT/eNpjAKyQpjQjHu+8dOlS7ppT61AALlVHNDHDS51wz8hlxN1P5wIBF70QQLstU6aM3VV37NjRdWoRZlHnW+I4QpbQVCwgRp9offv2xasQKTKeMaDv0fpDzCWOIBwM9/fJJ5/0jpSIizZo0IB+FEuBK0lnae7yOnwCIkAn8P809Ve0aFFMOTzkiiuuePbZZ+llO3Xq1Lp1a9mUaOFOeFmjjHXERiJ3HwN67733PvHEExho24gjKNgXpdYAJLnVrjakIfeXkuKIRPyyqAAT1kcU6REXLVpEL6gvuAC8fJoxjr5IOzUiy47dp7fGYhLIL8UxI7LkhxyGwiPZNHu4nL61gK/GJf2ujjsGvEWUiR5azhwdUteuXUnNniXeunWrEsycObPmW7Jnz4707AkxgTJKH0iKUlAuZRu/cOzYsXS0sBd6GvV5SAkypslz+Ay+Fz79mDFjlAIy564rBXKl71iGwnNQ+AoQbJ0hTJemaRB0T4pnw3vwBoot/h8KH3T8448/OuGDYXG5IDm8C+Lh3aWGzVV+SpcujW+Eywv1DYVHnRGdzLS/MOm2M4SBOrm6Oh/95KlLL71UuaXvt7/P5q+c0ZoJzVDzz6HwylL8Qv/4UmkNauTOnVuOdTTNRw7Upmgt7p3d/AX8Of8dgDQZqrVevXodw6BdmFOOJkyYAEtXFbz11lv2SjZaHMwBOUBWcXbNXDTeJzxfHyiGGGBq/g973wHf0/X+/4m9IoIKNVulRhVVRUvt2qT27Nco/VqlVFHjTzU2FUpRe9asPUPFjC0RIQixJY2dZfX+39/7/HJ63Hs/93OzPoLn/corr88999wznvOcc5/3Pec8JyAggBgCAhEZBUa3+uyzzxCCYkMJKVkTsZt3CpQWTVy6dGmTOiYHMAjA5NJ8/AK7tr24RpeYsyCNtKofIhIRBDHQ8BACkRn9iUeaZBW1HTGuypNFtIxfkCvyiid3BM1WNw0XJdBoKYz1VatW4VKz5JteH8J/NV3KJwZjCNKU1hD0IMZhEUKnKB85coQu0bvLli0rzFziosKmV+I4jLC/yRzXLJCmXkw+n2kxfLNmzUSaojmg8OgXTyWQ82o6OM0Q4Fp44UI44pH9+/fjEagrcSqa0kc64hEMoTZpOY91HXBYNUV1CWZ78RMAsTixTgevCdIBsTL5/v376JXmZ5yY6DDelTb164Acnz6jC1JnWJ22bdvSKE3AMEJvFmp6NCsuxZIuYndiZQQGT5vuexkdceyQR2nU26Rq9uCw32F4h1bIj0C89OalL6S0mULmoqQnMhd12Kdg4L333ntyLkTgRV8w1+fEyFADVB8CEY7xQXoxaNBvK0rLgK2FQRj2D7pnUFAQ7KWrV6+KAQrvfdxFIOgoZIsRBpdixxN+oymhzwihyVUTYzhpwVz0NYE48pHw999/6xeexcTEYNiSnQOZLL0TgB7TbBUU1N7BKmLtJTRYzkLg7t278vdgcACyaciORMHOnTsnplZMwgl44cGK1U/PKtIySNTOXi+CZIKDg525LVtRP1bBUNDsTlTUDSeQmMUTa+TUMKbYW1sIadOeE2Rnz8esonpcNNya4jTgHTN9+nRUHwPi1q1bQcXx5ib/Ww6fJQ2BDYSmTOQaSxNhhoWFaXqWnLs9/VTUbTz6w2kcKqe9bmIP5vHxzta0fnw1H0X98MMPzbfq0RpdxEF28e1TEF3SaqCh2AkmneLmzZv6jpncIB9O0H85UL9flD5DCJMRmkNGds+ePTXSNuQh9KVM77ZKk6xi5EOFzuMFgScFSBgXLVq0qGysd+rUyRa3qFIA8kdg5syZKSN6m8hL/S26dII6oTz58uUTwyntWBPrJOfOnSsnq/ddRBNKDRo0oMt33nknderUmsGZlivXq1ePLmmGuWbNmpqta61atcqZM2d9HWSn2RrQrBpIhf4pWoWo5xiaTX3WdcB61eSRCmSeZgLFvAo1zeDBg4WEDbeEyDDRYeL2gusSyMk23gsm1aFFuXq5idlFMbyHhISQ8ovPQN988w0uxX5LgsW9jhr1NqmaPZj3OwzvNvXDt+YpcixHPNA6F7XXp8iTX/PmzeUsNKplrs+JkaEGxOddXV29vb01L2UrSstAh8UgjDF2z549wqu84PZQquPHj8sO5+U3Joxq+VZgYKBFp6GJB3NRRhLAxK1RcuD06dPyij4Z+i15jJSJ7du3a5bPERYvXuy0ZSFOxiunnN4qzOPo94syrGDYsGG2F09eVSxwUUV1l0XzxjAN5ZhJzkUBWmVHi6WThIvSJrQtW7ZoMqIlGLS8PMFcFGjdujVi0oz3vn376tatiwJky5aNFvBXqlRJ3lpmj4uS06/o6GhagKP5ckF7lcVZvmAOtJglTZo0AwYMEB81SpQogco6LLAMmjSW10pokFRc1GLV9FxUUbddyHNTdPiTu7s7sdMaNWr4+/s7rKk9HTbkoqGhoQgUc4P66kRERCBEXrppiL1793bu3Hnq1KmbNm2SJ1qrVKlie/FwdSWhXNSkavZg3u9oor58+fKaCLTDv2PHjkpScFHa5KU5XF2jWub6nBgZ6jFo0CCbilKlSh08eJACLSotA6MoMcng4GDISjgroimlc+fO4TfGRtxFVyXWSvuw0Jdpce+ZM2cwkhCV5XlRxqsEGun0C/ySA3fv3pU9KmlA5r7s/peRMvH111/jnS1WnBJOnDjx/fffO+1TnJPxqijn5MmTp0yZAppUvHhxh8wZtlTZsmWdU7DXCTSzITYzE6xwUUXlP7RrziY5IEkOLpo3b143Nzf6nSRclLZCiEOM5IxgaJKVmRguSlY1ORJr1KgRzKyxY8cS56ddBnJkcy767NkzogS0ml3g4sWLNnVrgwiBJQc7ngzlMmXKkKuhfPnygY3EaygjP1vyCk8NkoqLWqyaIRcFPQDrltUApM6munyD1VuuXDmLlTXUYUMuije+PDeor05ISIjtRd9mGsTExEDhwdbITx6t0RVclE6KFhNHhARzUXtVswfzfkdFzZMnjyYCLZYGZ1OSgovS1GKTJk3kLDSqZa7PiZGhIbZv3077O1KlSkWFtN4f33DQvCgglsofOXKE/BXFxsbSLWGEkIMi2vfk5+eH32KlFVHT/fv3O8ceYy7KSALQyquRI0e+3GLglUPuK16h89bfWOB96eHhgcYqXbo0SFrt2rXLly8Pw9H5qyWdg1dFOVFO8uiIF7/JFA0BdgZiuru7W3SGzBAgjiQcDhMcclHYneLrwKpVq7JkyWKLc2Sd5FwUJghChA+8JOGi5PNTs0uWMhKuyBPDRZFU4cKF06dPf+jQoUqVKimqRZU6dWrY5chUo8/mXBQgD3+aXXAHDx60xbkTh20nO6qhypJTHDQEfvv4+GhKuGbNGnsL78kj12effaYJR4uTy5kkXKPrsGqKHS6Kzi7cvxFoaXGhQoUmTJggNn6bwESHDbloQEAAAnv37m2vOpAnmjhTpkz68yfIawbpj3Dgp+GiderUweWCBQvkBxPGRU2qZg/m/Q41Ik6raYXRo0cjEAqsJAUXBQmhFpRZh0a1zPU5MTLUQLhCfPz4MS0eyZ07NxXMitIyaNunzCHJKRFIO93as2ePWOd848YN2lwK4ko0VShzVFQUhZicW5GEYC7KSCwwnA2Pw7Rp017WEkTkO3HiRCrGTz/9pBmwGCkQ0dHRq1ev9vLymjJlys6dO4XD3tcPr5ZyHjlyZNy4cZqP3HqcP38ebUeVgm2EN5xzivd6gJaWgTXJC9uIqtEJFgQNacQP2UkpnU9LBjfNDmmW8yWGixIxIyfbStzUh/Bk8/DhQxcXlzRp0oj45GJKs/5WY6z7+/uDNri5ucler8kRqPBrmhguqsSRfA8PD+GrpmHDhihqiRIlNB/4HXLR6dOn4xJ2tvyUt7c3qkAzCaiX4EhK3Kna5AxpxIgRNvXcY/nEUV9fX5OlpCAe5KgW3UoEwiJv06YNOVt2yEWt64DDqilGXJQcvwu/pgLNmjWjb1ImjtAFTHTYkItOnjwZaibcQxhWB8yNqiPvMBw/fjxlRCcYCS5KQqMFrkrceldUVt6ISLRHuGGzB416m1TNHhz2OzpYS3YGqajOikEdaR0BbbeWt0lv3rzZ9qKPK/M+FRkZSV6yZT+66D421YEcXZrrsxUZ4hY4j8NTdr/77js5TocOHZBIWFiYYk1pGWCVtLyW1JJcoOESDQcTi+ilkDDR1GPHjmFspBNHxQhPNBVwzplnzEUZDAaDwXA2YFDaVIfbsD5hMezatYv8llevXl2c6kSWqJhwgLErz3rBqs6cOTMRFRimMNkzZMhw5coV2hSkxDnm1ftu1SQL5MiRI1WqVIJLILWaNWv26tVLRCB3pk2bNg0ODka+4D/kfnnVqlX0FYlIQs+ePUGfYOOSVUoHMMoeqigaLS9U1FkgFKZatWrCiqWTn+QDhMnrrzg6xRx0lEuxYsUE8ySr+ueff9bEnDVrFsJh7IoQ2p5XpUoVukSR8Bs8VhBsmHeFCxcWx1bhEka8MOxApSBD2qsCmVDdYb6D7oI7de3atUKFCuZf3Gi+i/gwjOwJEyaUKlVq4cKFdBfGomYGbMmSJQhp0aIFXVrXAYdVU+K4KKREl2hW0Bu5pQTo8Cf5FF8TmOgwcdG0adMGBATQ3evXr0PNhg8fLuIbVoccDhMdgv5AVerVqydmPulIUqguHVlJp6yVK1cO1PrSpUtRUVGkyRAjrWPE4+SCqHv37ppdJBpo1NukavbgsN/h8bfeesvDw0PkcvLkSRRPPg6aTpqF8qCC6HromzSd6OfnR5PwDvsUnZ3j6uoKLh0TE4N0aCK0QIECixcvRruY67MVGX7//fc29bxfc4EgcVkJwZnFHhArSstQ4lbe7tu3LzAw8ODBg/iN/6CUGBLxrqE9oriFdiG2SWd9k4tdcnREW0kBjT+q5ANzUQaDwWAwnA3YnTCX6bSndOnS9ejRA+ba22+/3b9/f5ibFy5cGDFiBPlBKVq0KG2Sh7ELW7Bx48ZLly6dOHEiaIk8D0mnCIKNIFnYiLDg3dzcaJJw3LhxtBHIMFlFJWyw42F6tm7dGnwSrEMz/QV6U7x4cbL469ate+vWrZIlS+KRMWPG0NTuxYsXs2fPblPP5IDFs2fPHrJ3Kb7s2Q7WLSzXhg0bwnoGMRg4cKBYtgpyRYZ1njx5yFCeMmUKTGQqrfnBlQIwiAV/U9SZgUKFCsnzOYq6epNmesEWQFPRFpAAnWICAQ4ZMoR2W4GADRgwAGY9RAq51apVa9myZSIRmMKo8ieffDJz5kxwANyVp54gEPLVZFNPyOzYsaPDSSEYi2BZ4qQrFHvNmjV0C5YleYhBUqAWSGrz5s207B9VwFPEva3oAMG8akocF8Vd0DaoRMWKFaGi9s5rgTDlY7FNYKLDxEXpvF+U55tvvilTpozYXfzw4UOT6mzbto2WkdvUU3DQpmI+B6pIT0FQXl5e0Ac6XRN0i+aOoNuVK1emZ6FsUB40XOnSpSdMmGDPL7ehept3T0M47HeK+nmlSZMmKDOIGQYHkFWxkJWwY8eObNmy2dTdlf369YOqQwHq1KlDJ2lZ7FNTp06l3RlIBJJBFXDZvn17CJa+Ppjrs0MZQvJ0V173oUefPn1ALyGKVatWob4oiXyqkEOlZSgqaQfVFO5w/fz8xAbRmJgYvFzELZBS8Y0DT9EHLAEQUacd3MpclMFgMBiMlwMYBwEBAbQnJywszPx4p9jYWFAOGNkhISGwNvSGAoyJxJxWBaaBZGlFnB7INygoiD6iK+rJYZoIdKKdRV8XN27cCA4OTg7HGOHh4Roxmk/FOAQKiaKKisvhtNgYt2DhiZNOZNy5c+fUqVOGt+wBhYcYYSMmTDjx0gF7VVOkNbqoAlTUxCq9e/cuaLPFtXwmOiyv0QW30XipsQI8BdHpi4qU5SqA0uh1D7VAeagWmi8XFuGwe9qDeb8TZUYV7M2rR0dH+/v7E+VAARI2CJDi0TFmyMjwQDhzfTaXYUREBBisfPizYUUUdVREOpqjRAVMlJYhAIXBEI121L9T8LpBK6Ox9J+WoMMRKpzsuYO5KIPBYDAYDAbjXxj6LjLEuHHj5D2uCYbhflHGa4Pbt283aNAgvqepM94EMBdlMBgMBoPBYPwLcy4aHR29ZcuWy5cvBwUFFSxY0OHyYytgLvoa48aNGy1btkzYhDPjtQdzUQaDwWAwGAzGv6ADHk+ePGl4d9KkSbY4CP9GiQR4r031x8tTZ68fYmNjneORlfEqgrkog8FgMBgMBuN/OHPmTOfOnbOq+PTTT8eOHavfHxgSElK5cuXChQtbOVPUCrZs2VK7dm3KtFWrVnPmzEmSZBkMRsoHc1EGg8FgMBgMBoPBYDgbzEUZDAaDwWAwGAwGg+FsMBdlMBgMBoPBYDAYDIazwVyUwWAwGAwGg8FgMBjOBnNRBoPBYDAYDAaDwWA4G8xFGQwGg8FgMBgMBoPhbDAXZTAYDAaDwWAwGAyGs8FclMFgMBgMhjEOHz68cOHCf/7552UXJOlx7dq1pUuXisvo6OiZM2eeP3/e/KlkEshrLGeHCA0NXblypUkEk6YJCwtbtWrVxIkTfX19nz9/nphi3Lt3b9GiRbGxsYlJ5NVFeHj4/PnzX3YpGG8imIsyGAwGg8EwRoECBWw224EDB152QZISe/bsqVSpEuqF2olAGOIIqVWrlvmzySSQ11LODnHo0KEqVaqg4h9++KFJNHtNs3fv3mbNmp08ebJBgwaI8MMPPySsGDdu3GjXrl3q1KmRCBhpwhJ5deHv7w/Zuri4pEuX7mWXhfEmgrkog8FgMBgMY3h7e7du3ToyMvJlFySJceHCBQ0XvXLliqen5+rVqzUxnz17Jl8mk0BeVzk7xNmzZx1yUcOmefDgQZYsWZYsWYLfjx49aty48apVqxRde5lAjvnPP/94eHi8mVwUuH//flJxUevyf7XyYiQfmIsyGAwGg8F4sxATE6PhooYIDAycMGGCc4r0ZuLWrVsOuaghZs2ahQcPHTqkCf/qq6+sPK5v2aJFi76xXBTImjVr4rmoM/tLZGRkjx49nJMXI1nBXJTBYDAYDMabBStc9P79+0WKFBk+fLjTSvUGIsFc9L///a+ei86YMQOBDp81bFnmoonkok7uLy1btvz888+dk9erhYcPHwYEBOzbt+/gwYNBQUFPnjwRt8LCwo4dO+br67t///4zZ85gGBS3Hj16dOrUKTyFPnXu3LmnT586rcDMRRkMBoPBeAnA+x6GwvPnz9euXfvnn38KvzWxsbG7du2aOXMm/kdHR+sfvHTp0rJly37//fcTJ05QCAzoQ3GgkJCQELo8fPiw/Ozff/8Na0NRt+otWLAAVguFBwYG4nLjxo3Xrl27ffu2/AhsF+SoqD5mRC4i6zt37lAI7BjxSERExPr162fPnn306FHr/nj09ZJx+fLlNWvWzJkzB2nK1hXh6tWrf/31F2W9YsWK5cuXw7TSxIGoT548iVJt3bo1KipKz0UfPHiwY8cO+g2RVq9eHXE6d+6M2p0+fVovkKQtniZZ2IIo5927dyFANCKKbSiWyMjIzZs3Q1v27t1rqC32YCLtZ8+ekQauXLkSJdfcRXxoC35cvHhx3rx5KKTFJjbUMZmLQv6bNm2aO3euXrxy0+BxtMgXX3yBByFwofarV69OkyYNEVTAHqu017KCi6L5YKnPmjXryJEj+sfRs5YuXbp48WJU30qt0Z3RwUlEaGIUGL2ebiEQuSNk9+7d8c0IrTBfBViH5pYVZdNDcFH0aGS6aNEi9He6ZWV4MekveljUbZR/+/bt0ENUR4xUitqRv//+e+RVpkwZKkYi3Va9TkBPwVAAidF/wM/PjxYz37x5k0LELZBVGqygIXv27KFb9AO66jQ6ylyUwWAwGAznAe/+qVOnku8cGGEtW7a0qfD19cVdEMUmTZpMnjx5zJgxHh4e77//vrBcFZV4dO/evV27djDowSJcXFwaNGgABhITEwNeQemQAQF7lOaIxFwHyKGnp2fatGnbtm3766+/UuSRI0fi1o8//vjll1+Cp8E0KVmyJLJQVEPwp59+QgEQDVRZUWlD/fr1cenq6grGRcnC9Onfv3/mzJl9fHwoBEZ8mzZtkEW/fv2QXcOGDe/fv28uE3v1orswQzt27AixbNu2DSbyBx98ULx4cVEABFauXBmlgiQhhPz58+fLlw+XJUqUkLkZCl+xYsVvv/0Wdv/06dOJyQguCpO3efPm6dOnFxN0IHhU2c8//3z48OGolF4gSVI8fbJIsE+fPjly5CBvRijqe++9h3aEWMDlZLmBLBUrVgyBoHDIN2PGjBUqVECxoTwJlra/v3+hQoVGjRoFOgH1gEzAsekW9BYlQakgQDQ6pJctWzZcdurUybx9FTs6pkhcFIQNVUZ1UJ5MmTIhmr2mAU9Gi0CAePCrr74argJ6iNLiQQRSSHBwsGFJ9C1L4cRFQWxQRzRHhgwZcOnt7S0efPz4MdqlZ8+e6FktWrRAOYcOHWpS5cuXL3fp0gWdBemAvNWtW7ds2bI5c+bE5aRJk86fPw+FLFeuXO7cuREyYsQIixmhN9WoUQMygTCXLFkCDgliRrcs9gVDEBfdsGED+jINDqlSpaLqWxle7ElVA4u6DY4KEX300UcrV66EljZq1AiaRnuDgTNnzvTo0YP6L7U1JGZeuzcHYPVgkufOnQP/RMNBn/fv33/nzh1FddaNW1BFUPfY2Fi6vH79uqL2evzGf0gebyi6deXKFeeUmbkog8FgMBjOA0yEmzdvVqtWDbYUDEc/P7+tW7fCsrxx48bt27dhBIv5HFiWiAOOIb76t2/fvmvXriIp0DxEAOujS3d3d2EsEmCaC2MRnGfQoEGIAHN/3rx5gYGBSA3EDFYLAgXjPXXqVOfOnRXVAAVPgDkoUy8YLkgwderUMP1FLjNnzhQuTHfu3Cn7Ox04cCAed7ity7xeSBBWu5h8Cw8PL1iwIHgXbH0KQfEQP1euXGPHjoWsEBMWPE2aUQQYXoULF+7bt6/IYtWqVTIXhXCWLl2qWSz622+/EbGhS0OBJL54hslCScBbEFK9enU6ywRmIrhB3rx5Rb6PHj0C2WjcuDFdwsREfDAKGKMi6wRIu0yZMlAbcRdkxsPDQ9QOZB6RQdvAPRSVWrzzzjsIuXDhgkmO9nRMieOibm5uYKe0YhBiQQjoMUUwbBpFXaKJQJoAFICQrazR1bQsgbgopEHW+dmzZ9OkSQMKJGa5QadB0UV8NDrik8Mke4Di5cmTB9Eg8L///hsh6OPQDdQXDXf37l1F/TQAOgoGKDxXmWcENcal+NjRrl07XKK0dOmwL9gDNAcK1rFjRygPCvbLL7+AH+JB9GiKYD682JOqHlZ028vLCwIhiSnqRCjoKB5ZsWIFhZDLK16jq0F0dDR6xJ49e/RLMwCQf9wVaoY+i0saK/bt24ffYWFhdOvSpUu4FDqW3GAuymAwGAyGs0EkTZ4MAdq2bfvVV189jQMMWZrnobWCa9euxW/wWBH/2LFj4LRiJeHbb7+tMRY1e8CI3FatWlXOdOPGjQicNm2aCAG3FL+7dOmioV5gEQiB3SlCqlSpQsv5YGWCHYHoiirs378fkbNkyWKyiM68XkQakab8CAxlBAoadvLkSVzWrl1bRIDNihAQJ7ocN24cLoljEMClNWt0cdecixoKJEmKp08WwOMIEdODQLFixWzShkawQVzKpOXTTz9FCIifYh8Otahy5crly5cXd2vUqIH4YmabqjZ69GgRgfZtyiXXw0THiIsWL15c3ILaO2waJdm4qDDHgQoVKiCEjHWQn9SpU4PwC90GX8LdevXqmedFXxmuXbsmQmjqUl4A/OWXXyKE1qk6zGjo0KFgyEKZoQC4u27dOrq0omyGwFgB8imv5u3Xrx99L6NLh8OLRS6qONLtq1evZsiQoUOHDvIjp06dQgQPDw/6YMFc1BC3b99GjwDnxPgWFBR0+vRpCFN8SALzx10Ego5GRERgcKbFz4jg6+uL3wikmFBXWq/rnGIzF2UwGAwGw9n48ccfYUv9/vvvciAtyq2vA01NwDhDBJM0HRqLSAcRwHjlp2C+EOPt2bOnfotdt27dNEzD39/fpu7Uosvg4OC6devSb5r+AiPSV0GzB1WGeb06depki1vALAAqhcDMmTOTmUX29xdffCEibN261aYu4KRLSDVnzpxyCnrfRXonOoa2tUYgSVI8fbJKnL0u++b55JNPBDUCZs+erZlzpkRorskeHGrRPyoUdTE5mHb+/PllGk9cVF4D/MMPPyBk/vz5Jmma6Jih7yJEhvTM4yQTF5WLR4tOwdUVlTyDqukVu2PHjuZ56bkoJStPOkETELJt2zaLGYmzTMA6wMfwrFi/akXZDKH3XQRFwoOghaQPSc5F7en2okWLbHHbB2QUKVJEcHjmooYgDonhiPZ8EsROfrTj8ePH/5Ig+jWkikuaXZejOWcjLnNRBoPBYDCcDT0XjYiIQMjAgQPtPVKqVKl33nnHJM2EcVFg3bp1tDsOhE1DKvQcCfjss8+EjQ4qsnbtWgqnSUIyqa3DvF40N7VlyxZNePr06RFOO5rM7W9wqtSpU4OOyo8nFRdNfPEMk1UscFH6KFCoUCFhLzZq1AhkzNx8dKhFijpp7OXlBd548OBBmhcVVCphXFSxr2P2uKi8TvjlclEijbRBUfY7ahHWuejGjRstZoQmBmHr1KkTehxqgfiLFy+mW0nIRQGE4FlaK+s0LkprRgYMGKB5ivZ4L1y4UGEuagcYcIhDBgcHR0dHC2dFNOF57tw5/N63bx/u0gZRsFbabSFiQi3RLoKsWvc8lxgwF2UwGAwGw9nQc1Ha79e0aVN7j+TPnx+cynAjECHBXFRR50BoC6vtRVc0hlyUHJl07dqVtn6JHOfOnWt7cSmmFZjXi7jQ7NmzNeF58+Z1cXEhjyzm9jfNUrq5ucmPJxUXTXzxDJNVLHBRRV17nCpVqt69ez98+PDUqVMeHh67du0ykuK/cKhFME8LFiy4fPlyuYKJ56KKHR17Vbho+/bt8dvcPawh4stFHWYEvlG5cuVevXrR7Cit0U0mLgo1Fh3HaVyUatSmTRvNU7Qzdvv27QpzUTugeVFAdHCa8MTLJTY2lm4Jj8RBQUG0ZFdR50IvXbpEs6n79++nWwcOHHBOsZmLMhgMBoPhbOi5KIw8kASY4Hqvs+Sxo1atWngEPFBzV5h0CeOiFy5cEJvEVq1alSVLFpvkCsWQi8LQgdGfOXNmMJZBgwaJcJgviPzZZ59pSoj0ydWNIczr1adPH9zt0qWLfAuWE+oF8kCX5vY3ImfMmBGX4owKJem4aOKLZ5isYo2LAl9//TW4KJjJxIkTUQXFEcylffv2bVdXV7HoWkkiLmqiY68KF6XpxyFDhmiS8vf3F53FEPHlog4zghpAgGKZbvJxUVJjsb3caVx03bp1+P3ee+9pnqpdu7Ytbqszc1FDhIeHE5kU85lnzpxByMWLF+kW2KZYN3Hjxg0N4cStqKgoPHv9+nXcOn78uHOKzVyUwWAwGAxnw3C/KMw+BNapU0cYmsD48eNpESzRANAn+bxBWPbCDKX9VMKj6cOHD11cXNKkSSMiG3JR8B+xyBaYN2+eTfJXachFAdjKCHd3d5ePggSLhnmKcC8vLxH4+PHjNm3awO6xJwrzesEEB0V3c3OLjY0Vd2l5qvCf5ND+ptV9sh9dFBUh+fLlEyF6wkPTvJq1ghqBJEnx9Mkq1rgoKKhwc2oR5tL+448/cFfmopSpON0hYVzURMcSzEXJPayGi9IRJg7PLzFsWXMuCiMev9Gb5BxhsqMY5usY48tFzTMKCwuzqd6SxcQXyZ9WripJykVRQjwozj51OLwYStUQ5roNOlSwYEFc+vn5iQj0/atly5Z0SatIZCdbDEWVEs1tkhqT9zhcogc9ePCA5kWFd2KiqbTV4vz589Ac2j4KNaODYfhMFwaDwWAwXlvQwQzgmXIgeZ0FYL/+9NNPM2bMqFevnjj9AqSOzMFs2bJ17dp10qRJrVu3btKkiTCFaQ1b06ZNg4ODYYDC+sybN69NPQ2CNgWtX7/epvP8CZ4gTy/gwcyZMwvq2Lx5czyiOdZSUReDgYPJx7cQRo8eTVWAwe3t7T1hwoRSpUoJQ9kQDutFvF1MwCIcpapWrZr4wL93716b6jNJpLlkyRKEwHyny+PHj6dKlcqmOoCNiIi4e/cu7cpD4LRp02i+FJYZQmAEi0SIuqMtwG02b95MdEIvkMQXzzDZ6tWr26QTNYDChQvbpJNRSFvq1KkzYsQI1ALPgu+hFiaidijtHTt24FbatGm3bdsGRj148GA6sgUFptW/UEtcosoiQfIADF01ydREx6CreDx//vziLk1Zo2kE3dI3jZDP6tWr5UDyJAyFv3//Pni1vfIYtiyd8yl/W6HNwIKM0bxclixZ2rdvP3v2bAgBkoSUTCquqH6zbNJCAyXukxNELUKo9YX/IZOMwNNA/0iTITq0OxWye/fuPj4+kJgVZTNEjhw5IHPhSRWSqVmzZq9evUQEh8OLoVQN4VC3t2zZgmpCZ8TBoagpGkj42kEWiJAhQwbwJdoGaV67Nwe0vHbfvn2BgYEHDx7Eb/x/9uwZOvjRo0dpjyhugYISNaV5ZjrEBTw2ICCAokGR5O9ryQrmogwGg8FgOA8PHz4cPny4m5ubTT2iYNy4cVevXhV3wQFoLRwZoz///LM8RxoeHg4mSef+wRTr16+fPAUEs6x48eL0bN26dW/dulWyZEmYhmPGjLl9+zaMWjKLwSEHDBhw+PBhego8IV++fI0bN166dOnEiRNhxZInngsXLoDkkL+ZokWLivMnBTw9PUFuNYGweECwyWmqTfWss2bNGocyMa8XsHjxYhi+DRs2hAn+5ZdfDhw4UKwVhNVVpUoVPIjHwZT+/vtv2MF0RAQIDwpDLAvWVYECBahU+HHo0CFY3l988cWiRYsePXoEe11sZYT9ffLkSUX1VkqTWmiIWbNmmQgkMcU7f/68JlmQsVGjRoEQIqRSpUpojjt37nz33XeiZWkqA4yafKhqUL9+fZPtoObShqzofBEAJAd2LSgufqdLl2758uWQEk085smTh8jnlClTXF1dqeTyzKcG9nQMrUBT1sSmQkJCjh8/3qxZMwpp06YNVFrfNEeOHPn+++/p4wLyRRkEgQQ1pXDIDUKzVx5Ny4I19ezZk7KoVasWjHX0F/QREhHkANqvqEvNwcfQfSgmmtWciEJhQOYpcqNGjWDoI9mRI0cSmSxXrhxYXGRkJHQGmoCQUqVK0VyxeUaTJk2igkGkGzZsADMkVfn222/BH6z0BUOsW7cOMkHXaN26NaQBPoyuIUcwH170UjXMxaJuK+qsbNmyZSElxO/atSu0AnorJ0VH3UKYnTt3do6LnVcCz58/B9UUzof8/PzEBlEIH91H3IKei20LmqcwasknSCc3mIsyGAwGg5GyALMPNEDemiUDtgVsU8OFiDAH8aA4PVIsxzJBbGwsLDk8CCYAc8RepnrAGLVnAsKyQTFg6MTLRjSpF+HGjRuwvBNjd4L2o5qKSrpMjpkRAKk7ffq0mJwxR+KLFy+Ai3bq1Ak5gr9t374dVBDkAUQF5rtYYm0CE2mDHstbT9GO+j3M8UKCdSwBQCvIG4PtIV4tKwMG/alTp6z0rETCJCOoLtpdXILOmUxCxgsQCxpIPmRVhsPhJcFStQcwooCAAHsJnjt3Tn8MFUNRlz+gdSA9vVftqKgosHqMHvovVpGRkWh6POVkbs9clMFgMBgMBuNVAuxIcE7DXZp79+41XxTNYDAYKQfMRRkMBoPBYDBeJWzevNlms02YMEETHhMT06NHD81qRgaDwUixYC7KYDAYDAaD8Srh1q1b2bNnBx1t0qTJ5MmTFy5cOGXKlO7du3t6eibgDEwGg8F4WWAuymAwGAwGg/GKITQ0tFevXiVKlMiRI8dHH33UoUMH/dE7DAaDkcLBXJTBYDAYDAaDwWAwGM4Gc1EGg8FgMBgMBoPBYDgbzEUZDAaDwWAwGAwGg+FsMBdlMBgMBoPBYDAYDIazwVyUwWAwGAwGg8FgMBjOBnNRBoPBYDAYDAaDwWA4G8xFGQwGg8FgMBgMBoPhbDAXZTAYDAaDkfQIDQ1duXKlkzM9duzYX3/95eRM3xygQZNVvNeuXZsxY8a9e/eSL4uXAtRr6dKlVmIGBwevX78+ucuTTHjy5MkjC3j69CnFd9hbDx8+vHDhwn/++ccZpWe8JDAXZTAYDAaDkZQ4dOhQlSpVbDbbhx9+6LRMFy9e/M477yDTb7/91mmZvlG4fPkyxJsxY0ZQjmTK4quvvkIWXl5eyZS+87Fnz55KlSqhUgUKFDCP+eeffxYvXhwxv/jiC+eULckxbNgwm4pUqVJly5Yta9asdOnu7u7m5ubi4kKXi1VY6a0QGuIcOHDAaVVgOB/MRRkMBoPBYCQBnj17Jn6fPXvWyVwU+O2335iL2oPcOgnD8+fPO3XqNHz48OTL3cfHp3HjxoGBgQnIIsXiwoULVrgosGHDhleaiw4YMCBfvnyCOu7bt4/I561btxRVf7Zt2+bq6vr7778r1nqrt7d369atIyMjnVB4xssCc1EGg8FgMBiJBfjDhAkTxCWsT+dz0eXLlzMXNYSmdZyMefPm+fr6vqzcXzpiYmIsctGTJ0++0ly0d+/ef/zxh7jUcFHC2LFjp02bpnBvZcSBuSiDwWAwGIxE4f79+0WKFJFnzJiLphzoW8eZOHHiRPr06d/kTbxvDhcdNWrUw4cPxaUhFz179uz8+fMV7q3JBjRBQEAAhH/w4MGgoCB5RX14ePixY8d8fX2PHj0aGhoqb8R9/PjxmTNnDqgIDAyE0jqtwMxFGQwGg8F4OQgJCVm6dOnixYsvXryouRUdHb1x48YFCxYcPnz4xo0bmiWOd+7cwd0ZM2bs3LlTcwuXu3btmjlz5sqVK69evapJ9sqVK7BR8ANpIut169bp/cTExsZSCviPYjisBVKoXr06zMrOnTsfOnTo9OnTyotc9MGDB5s2bZo7d+6lS5f0j8MqmjNnDkry999/O8yLABMK5tS8efNQwrCwsLt371K4bN1ev3592bJlCAET0wsB4ajg3r17hRsVAi63bNkSGRkJA27//v2///476IG+ACYNZw5IAKVCsmBo+ruXL19es2YNpAGZ6PdkojWJ0UVERKxYsQJVePTokUOxGLYOAalBOLBc0TRQMxGOss1XAYtWUwaSD8xWOWTr1q3IC7kjkdmzZ8tVg3WbN29e5D59+nTkDsk7FBGqKRcGgGJs27ZNUTUTCr9o0aLbt2/TLZQE+oxMkZG+nA7bEeoNy3vWrFnoTTdv3tTctadmBPNu8vz5c+SIgkE4UVFRCeCi58+fx+PoFyJfpHNIwrVr1ygczIFCUprPJ0MuKmCxt4I7acYNtBRi/vHHH2h0w5TfZGCwxbCGrk3/AT8/P3pHYMynELQL/Th37hw9hf4C/UHInj17oPP4gUtouHPKzFyUwWAwGAxnAzZ0nz59evbsCT7ZokULFxeXoUOHirugOkWLFoVxhh+jR4+GxRYeHi7uTps2rWbNmuBCMKDffvvtIkWKCEbk7+9fqFChUaNGgXKMHDkyffr04DZ0C6lVrlyZOMmkSZPSpUtHrkQ8PDyOHDkiEoeZ0qRJk8mTJ48ZMwa33n///aCgIPO6bN68uX79+kjq888/Hz58OCx7ReKia9euzZEjR7FixZBdpkyZDh48KB6EMd2yZcsRI0ZMnTq1XLlyWbNm/fPPP62IDuQK4oKxvnr1ajwlvPUK63bQoEHIFKLA5bvvvitsdLCLvn37olSwt3x8fPADSRGjg6HWo0ePnDlz4hHYYSVLloSIyJLu1q2boKzmDWcC8KLu3bu3a9cOrQZqhAcbNGggOAwIYceOHSF5kC5wrQ8++KB48eJgpHQXgdR2EBfaMX/+/Pny5cNliRIlRAr2xKJvHTTNkCFDChcuTDVF05BHopiYGDCBGjVqNG/eHKRoyZIlSOT777+n9GH3o9YkH5InygxRQM7kXQYM6r333iO9WrBgAT0FCopCIsJXX32F3Ldv325PPiBvKBu5vBJzZbCnUfjUqVN/+umnsJLLlClTvnz5DBkypE2bFoqEqkH5K1SokCVLFoTs2LHDejsCKAyEjHYEmezXr1+aNGmgNoJmm6iZ4qibQMIVK1ZELXbv3g0JQDLx5aLIV3j6gYRRdyoS7bEEkK8YE4KDg1GANm3ayHOShoiIiIBwULaPXgR633fffeewePGFRS5q2FtR1J9++gn1QqA8LKxfv/7jjz/euXMneFSzZs3Qgkle7FcaJ06cIJIJ/okejS6wf//+O3fuoH8RBQ0NDUU0DHpQKlyCuyrqUIzf6FNPnjxBH8EbAZd4+zinzMxFGQwGg8FwNn788UcwRnEJ6xAm16pVq+iyVatW4DniLqxeMcM5d+7cUqVKiQVUYJV4EDYZXcJYB98TD4KxwFCmhViwOWDgInKePHlg9MPgg4ECaoQQcBsywW/fvg3jTzA3UCDcBS+CHWNeHTKR9Wt03dzcQMCotHPmzEEICBhFQKlAPGiSVlFNz8yZM4M86+dyNZg5c2auXLnE6rIpU6aAvNFvsm7BzxGHIrRv3x4hEydOpAgwZHEpdk5SkVB4RT2OArYXUibKd+zYMdQafJV8gSJBesS84UyAknTt2lVcNmzYEA/++uuvdFmrVi0kJSoFmlGwYEHww8uXL1MIzHHER/HGjh2LgiEmNAQhqIJDsWhaJyoqCjV1d3dHYIcOHSBw8KVOnTrhFog6AgUHJvU4e/asouoPWBkon+CiijoJX7ZsWYSAtuGuon4NSZUqVd68eUVNIUxEcLhGFyVHrf/73/9q1m0GBAQgBGxz3LhxNFcMMk+kBdFIM2F/I6Rq1aqK5XYkmkTTrQRoBUJQAIfyNO8msbGx4PmQpEgZ6hEvLpo9e/aRI0cifdAGciyMwqODUJx69eohZPbs2eIpkAfofFhYmHni9+/fBzOH4vXv3/+HH34Ajf8hDmCDybGI2goXtddbMWjgKfBkDRfNnTv3jBkz6Hd0dHTlypWTvNivLiAQmtvUr6qIjIykuVDxtYVY64ULF5S4w3XEaEPUVLM8IfnAXJTBYDAYDKcCxn3q1KlhMT+Ng5eXF0wuWJkUARaYPJu3detW+pgN2gDCtmzZMpEUGEKdOnXmzZtHl7DMypcvL+7WqFEDyYplb+Sls23btiICuASdmrB48WJc4hZsX1EqWNVgtrgrT5wawh4XlWctkJpskf/++++gW08l1K5dGxHGjx9vnle/fv1cXFxOnTpFl7DRBRUk61bQCSWOJ6BS4hI1WrduHV2SrdynTx8Rn5gV2WcE4qtoDsVCw9nD2rVrEU1eBQrjr1q1aiRY4iqiEQm//PILAhs3bkyXxFIgIhFhxYoVMm0zEYu+dYAKFSogkCbcBIYOHZotW7br16/TJVg34ghxATSbKq8FRQkRIk9300SriGORixKWLFmi4aKPHj0S8idA7DSRKz8Iau3q6iouzdsRACvLnz+/nALM97feegtxjh8/rpjK07ybgDPjt5ChonbSeHFRuQuDpH388ccIFNPvaDLbizuxMT4IPTEByiyaCUWqX7++w0cSCStc1KS3Al26dJG5KClDs2bNxDcC8XGBoahfSdDRDhw4gPYNCgo6ffo0XhkkK7wFiKaKpQG4ixBah09TpqKZwsPDKbJzTnZlLspgMBgMhlMB+wlmbn0dOnbsSBFgB8Pkgt0vz9soqj9ShItNPnr8o0JRDWuYzrC2ZbOYJpQ6d+4sP/Ljjz8ikJZi0mpDfcF27txpXiN7XFTjuwgmO7g0/W7VqlXOnDn1eU2ePNk8L6oFiIe3t7dmr6zeG8rRo0flyVhFOlwElLJbt264C3tX3KV5GLETT1FnEWkyMDIy0mHD2UOHDh0gW3t3O3XqhPQ1nmZBXBEIcVGD6r3agIHIhruJWAy56Keffqphaxr5wKL9/PPPEQf8UNwtWrSoIRc9dOiQCPnkk08QIuZY4sVF9S2o56KKqkjy/L8SdxCl2OFm3o4w0PGjWrVqmty7du0qvoaYyNO8m+AWFFuOn0jfRbNnz9YE0ncEWpOsqNOJ8vcCQ6D6u3fvFpcrVqwYMGCAw/IkEtb3ixL0vZV6qDwvSi1bs2ZNk2HwjQXNZ2IkofW3BPqegjcCXVJbPH78mPaF0pcXuiVWfd+5c4dCNNvpkwnMRRmvBp4/f75//34/Pz+TOOhasNvEV8z4Ah310YuwfqQVjAa8FTC4+/j4WHG/QcvxMbyuXbv28OHDtGQCbzuTCp49e3bTpk0wLiEHi/7NEO2RI+gHGjxFK7LiC0OvJCkTGK+XLl1qJWZYWBhaFpLH0GwxcYuP3L59W+8qgwBNgBpDN2h1mcV8ZVhpesD8k6cTOp2M0NB7GzacO3z4emys8csvKurJgQNX1607e+GCpbaIjo4Gc6B1gykNPXr0gDll0pEx+NSqVYvMONj6gkz27t0bIearWB88eODl5dWzZ8+DBw/SvKiwyA256IIFC2itZkREBH4MHDgwATWyzkUFhShRogRM6gTkBQwaNIiEU6pUKXlGzp51q5kC2rt3L4QwdepU9FONQPQcBihYsCACMcQ5bDh7QDnfeecde3eJWmzZskUTnj59eoSTvx+HXFSxL5Z4cVF0/EWLFoEe43WDR8ScOSGFc1HhzMm8HWn+TZ5+JIwZMwbh4suCoTzNuwkMidSpU4OOyoGJ5KLI2qbuDRYha9asEZPkGOggHP2aTHO0bdtWPnwlmZAwLir3Vj0XxZBObZ0mTRrQaWe6e035wFhBHDI4OBiKARuDLmmBd1BQEM12njhxQrgvgsrBEqDfwny9e/cuc1EG4wWMGjWK/BDgPWEYITQ0FIZXxowZEYfOUE4AMAjCzhBODurUqSP2JJgAtK1KlSq5cuVq1aoVXtt46WbNmhVvCPrUpAdeGEOHDnVTUbNmTYyz1apVy5EjB/5/9tlneFz/CKwlvGlgAXTt2vXHH3/EWypz5sxdunRx6D5u9erVnp6eVB2M2sWKFSuhAj/I7wUgU7LY2Nhp06blyZOnX79+DisuA8McKuLv7x+vp14KMApXqlTJilmAIXjw4MEQ1+zZs3/55Rc0gTw5kJhHQFYhYagriIH+Lvgn7B5bHMqWLWvF86QG5P8DgD5nz56dukaqVKnwG8ojEtcYajKc0+kIN28+rFNnsc32/+jv7bcnbt6sJZBLlwbkzDlOxGnVatWTJ88MUxOYP38+ygZGl5iyJRNoW5Ts0VQPUIIpU6a4uroipru7OxF+MEZzs97X1xcGN4w8urTCRWn56MiRI0NCQvCjadOmCahRArgoRiHoWILXgG3fvh1djBSbjohQLFi3sFwxWIGGkW9SspUdclF0SQyh6OBWGs4Q+fPnB0WxRxiomeQdgIS8efO6uLiQdyIrXFSxIxbrXBSjTeXKlXv16kUzgbRG97XhoqIdqd3xstPkTut4QUFFiF6e5t2EZrPxfpcDE8lFL168aJNWayvq4FCkSBEE4rULSinvTbUCNC6GFCd8p0sOLqqon9u++eYb8u1UpkwZvevdNxY0LwqIoUb2QgTNp3W5tBcUyoMf5IB6//79+C3cU4OU0vyqc4rNXJTxauC7774zMYsJ9MJLpFlMa6VgIWnW5BgCzC1Dhgz16tUTTgUUdSyoWrUq3lv6kqDn412IARSMRf7adPXqVfJz2LBhQzk+TJCvv/6aPsHK5Tl48CDMODBYKzvL6T0q+8wQ5QRrEt4Od+7ciRcwRY4XF8WYBSLtNH9riQdsLytmQf/+/dOnTy9WAUE+MCXNPyRbeWTevHm9e/cmQqjnohBjhQoVduzYERkZiXI2atRIb5dYQfny5WvWrCkahQxKGJF0Cb2aPHmy4ZSIDOd0usjIx0WLTu3WbcPChafGjdtfrNg0UM20aX/y978t4qxdG1S//hKEREf/b2r0/ff/F2fMmH3mKcOq9vT0XL16dYLLlnyg6aYhQ4ZowjFE0KoEcSpGeHg4qQF9qKLdifruDIMDQwQsCXDXunXrinArXHTq1KkIBCPFoASNhYmvt+1WrFhhXqMEcFFa/+nj46NJas2aNeYf44VwHj9+PGzYMCSSO3du4rQOrdsffvgBl2LktMhFYbhj6FYsNJw90Cy3vNGXQBSuT58+theXCivqcut06dKJbuuQi5qIxToXBY3MkiWLeN28ZlxUtCM03PB7HPmspk859uRp3k0Qgb7Q0QZvQiK56IEDBxA4YsQIOXDWrFk2dTkD5K8/esccaAsMFE7YCpjkXDQ2Nlb4Kz516hRpI/keYyhx+zxBLEXjgmoiRD56CjSVPm8FBgYKmoohEb9Fd6AJVXltRbKCuSjj1QB5cTA3i2nXUyK5KL1y6HVlDvICAktL/6kbryh6L8pfle7evevh4WGz43ERr7fq1avDcJQDiQx0795dH//YsWM0zaU58UwPjYt8GUuWLNGIiyiKdS6Kl3S5cuWcsNQnCWHFLAgODtZPOFSqVOmtt96SD9ZL8CPELvRcFDos+0KMiopyc3ODPWrly4iM0qVLywuANVyUUKdOHfPpHed0uh9/9Pntt6PiMjb2aaVKc0A127f/v5NInj//p0ePTc+e/btWGXQUEWrWXJjgTF86yPtImjRpZAP9+vXrLVq0IBsCJqYIf/78ecGCBYsVK6bE+QuFKQweIiKABYFi4Qd6Iu7KXJRYgZhaN+Si0MYiRYoQ/atatapNXRUiq9z48ePBVM1rNHfuXDwo70BzyEVhWyNCvnz5ZDsVY6bDRcIYGOWtEDRXTB3HoXVLR0QILkp0Tt7tqecwJHPyoeqw4eyBehOGHdkoxLuAaB6oLNoUnV0+0A+Bsp3tkIuaiEXfOooRF0Vkm+qyVbzUiLovXPhvX0sAF6XJZP0KZEMkHxeV2xFo3rw5LseOHSsn4unpWahQIbLUTeRp3k3oBBd5rpKoL1TdYfUNueiECRPwrtds/4Gq5M2bF6pYsWJFh8lqgLLBMDCJgCElYdtDNEA3IS5quCElAVwUite7d29x99KlS7YXvR+94UDPpZ2i1EMxqtOEJ8ZYNCjYOxSMvqHALKEDSOlMFxgwYr2uog4+YsrUCUh6LopqQDmgT3ijwFw29DF97ty54yr0pwMjPsIdHpHEeNPgNC5Kn7019pMekZGR5BREPnBMxrRp0ygdMaDD/kMIzD57aQYFBcE4EJcYFFKpsLersGnTpkiwV69e5kWlyQdDLooOqHm90edz61wUVuNnn31mMXIKgRUuStMUYoUbgfYO2dtoGq9HaKJAz0X1Uytly5bVuMGwAnEkIMGQi8ImCwwMNEnEOZ2uaVPth4zt2y+Can7wwXS6vH8/5ubNF94IDx/GIkKzZg5m6lI4yGdslixZYKnPnj0bkgQhFAvdS5cuvWvXLhEZxr04/Y/OeHBxcQH/gfkLywzjDPmc2LFjB26lTZt227ZtSGrw4MHvvPOOTfU9Q6kRF5WPo9i9e3eGDBmEhyQYLmQ7wpT/6aefZsyYUa9ePQ13NcTOnTvpKYwqmzdvBgegrzOyq1LqehjTiOrABqJ14LDRMUBBi7p27VqhQgWyjUyAyMOGDROX4EvoJvRbTBaJu7QzUFjetEQfgycdGvnll1/isly5ciAqtOOdOAwdkaqoFhtaqlq1amIkN284e0A6tKgyW7ZsqOakSZNat27dpEkTwWCpK4nVoQgHWZLzheGICPI7glzOirN/TMSibx1FPf7H9qKH5KioKHAbBI4ePRrNh7cYbWTt3r27j48PtRo1mTzpV716dYTI3q3I166Yv6Kq9ezZE0LACGlOcqZPn47I//nPf0TI7du3beopuCIEDBDU3SZ5KgLIBa7YWe2wHW/cuIFHkKyoC9654LfiK4+JPM27CYxYKDmJMSIi4u7du7TNGIEQqSw6PTAm29StGaKciI+3leEHX5KVOBbIOtBAsu9oDaZMmaLpRAnGwoULSVCGa7gc9lYl7pOBWMCFgcvd3V3YLY8ePYJUN2zYkPiivjagTaH79u2DLh08eJCmN+mjCR3iIt8CTaOnMOoSiSV2Rut4nbb4OYm5KEZPmg4GiHAD6PByHFqFTBBfsAioNjF4h1M9DBl37tyBhYHREC8D/fwJhsLt27fPnDkTgtWTfDQHWSEY0/E4zFOxXhxjN1QW71r9pxGoL15Uijr7P2fOHHltusCVK1eWL1+OfKEJmgVXyIs+kV6+fBmDkRiaUXgYTHgEBE/jnEM2i6EkoEzyKUkEe2bx0aNHUch169ZZ8SpkkYuS03aYg/b2zdPr0xa32oc+dgLmg6b8Oq9bty7iw3KyF5m+KWIgNndkYo+Lbtq0SR85XlwUXRtWL95bmnCMA76+vvPmzUNrhoWFyd0ZWkHHCeJZMDQ0ivx9nUAjIHR17ty58gsMmrx+/XooJBpUPwWBQXa+CsPVSnivownwLOwM2FsOuSidSaDRfJTWpltHnbBH7HFRDVBU2EYwX+RAiBRyiJenCkMuSni5nQ7tePWq9m135cp9UM3PPptr76k9ey6nTz/qyJHr9iII4P0qXE0SUEea0YI6rVixAp1I8xpyGpBvu3btyKQm80vmM+AAJUqU8PLyQiFhq7Vq1Up8usVwih5KXm1sqs9JMe0JeRK5ApACjBLyS5QuXToaiIiLVq5cGXfbqIAxLc9oKao5+Pbbb1MiYFw///yzlWl5xCHrH49gVEeaNDtETCYkJAT2TbNmzSgE+VKZL168SGyHhtOOHTtaGaVhRsOYBrdZtWoVGAKGOJrcg6yI72XOnBnFhsSggXS2ByjWkCFDaNLAzc2N4kC8ECbRdSRCYxHVArwCBBVZVKxYEURC7m7mDWeC8PBwMBba5IbyoBE1n+MXL16cN29eDBfgMGjHgQMHilcnhk1a4YLHQX4gJVBKGnNQkfHjx6Pp7YlF3zrnzp375ptvBJuC8SAqCJJMJcyXLx/eVnjRk+9ZvEHQceiADZs69w5dwusPYwtFwKsKr3VYI7Sch+KQpYtWzp49u009SVKcXKoHBIu3SaFChWyq91q0Dl6jeJUItenfvz/Kg5EcTJVCwOdhUqOaRPYAT09PWljosB0V9TXdpEkTKADEhcRr1qwp1uWaqBnBvJtAVjRPS+8adAe8qdEjYGI5HHBQceSL7t+tW7dOnTrhKXtCu3nzJrq2db96hGvXrqFUa9assReBRv5EclG8CqEJ9OXCpk5rDxo0SPZ94LC3YvgaMWJEhgwZ6OVFlBudFLr0ySef4J2F132tWrXMv5a+gYC1Q4tvCX5+fsLyh5Bp+ygBeiX3CIwq5FmX/Bs59EiShEhiLkqel1AZ8tCI1w8sGNnFImSEPnngwAENFz179iwtViYwF7UO2KkYQGHW48WAkRF9WywBQhPgvYIRGVYm7jZq1ChbtmzCmQooYv369fFC/fTTT6F2ZcqUKV++PLo93isYyvGeQ1KwEjDIIoTsOQy1I0eOpCU6MDRhTwtPPxjohTNo5Nu3b1/QOWiCj48PflSvXp3aGm8RDK/u7u4oKnoIErfF+VXH6xwvIbzYTp8+jVxgacljJQ2Ow4YNI4ZGQJnlFTh6sxh3UUgMZ1OnTsULKWvWrJod8HpY5KJE8DSnk2lAryKazaDVaDZpsZw58I4n2Zq8D8DkKU1zfmvIRTEAGc5nxouL4m1hizsGXQBcBc09dOhQmnaAzGnqeNmyZbCAyTiAWqJ2ZPF4eHjQh3kMfEiQPqhjlCAzK2PGjMT2YT/BfsXbCGWDQsJcE1/s8KNGjRrNmzeHdkG9kaNmVhApQz8hgd27d0+fPp1MZBMuioGbBCu+yxBo64vszDDBj1jhouhH6Cze3t6acGpQh+deyLDHRVNIp9Pg8OHr4KLDhu02vPvgQWytWgv/+uuyeSLbt2+HSqBGoi/DdiQNRPGgjei85MELraNfoeM0QL3xitQTMCoSDC9otRhaZaALBwQEGJqh6HqyGREaGio6i1iji8Ecpp5GXWVgpEKEeDlRRJGgSPYWsZsAtYAQrPstJ+FAdDC5EuC+Gy8jiE5UDQUGwxGft8TaTpRKjqaBvYZzCIwV6HcmKnfjxg25PNZhLhbrrQOtoG/NBMjBxMmZRdBph845q5BgsR0VVQEQQT8bb0XNzLvJ1atXaTMeKm7S1wyB7gAFMyeumzZtMvR36BBy+xoCrNuZjWUdKBVNhoOHY2y0Pmi8aYBWY3SCVmuWIUCAeB2EhYVFRUXpn0JkvHTQZZzjPlcgibkoTYqa+MNAfyZPTRouevz48QMqmIvGC3Pnzi1VqpSYmoOJb1NPAaZLLy+vzJkzi5cllIx2qQkvFBh/6ZPeuHHj6OsIWSrvvvsuDHfSYNpiUbVqVXoEbUemfNmyZbds2YKn0Nzk9rNVq1YUZ/369bicMGECXZJjOtr0Ai0Hy7Wp65RAV65fv96/f3+ytmHjyts/YCaCpYjRkMziggULgt7gDYExiL6fyYRKYxbj2SpVqtAsnKJOg0AasE3NZxEtclHa+SnEYgj63k87H2g9LXLXj++Qs+akDQy1586dI9Nf465ABsYaiiNEbQiiLmi1xXFAW9SrV8+QjMWLi+Jlnzp1ak3gzJkzc+XKJao5ZcoU2p+DMREtblNdF4JY0njXrl07ovSoC0ZGvLbd3d2JgaOZwBs7deqkqNPFsjfUgQMHIk6PHj3osm/fvrgUX44pTcGQIUzwW3nrDh0rb8JFyWmhTXdyg+gviX/EIRfFkFizZk3ifhqfzL169UJPQT+y96we9rhoCul0GowY8VemTD9fu6Y1DZ8//2f9+nPvvjsFTPXLL//4+2+DV6kAsl66dKmmL4MVIwT6OXbsWPQ7lLZFixb0Zc168V5pGO4XZcgw9HnDeOXwJrRj3bp1YTa/7FIwGIlFEnNRPz8/MEkQjNDQUBhhwcHB8kcdWDO+vr4wsvHDcI3us2fPmItaB8w72HmyXz6Y+3Xq1Jk3bx7dzZAhg2ZW7dSpUzQTRRaz3iXA06dPaTJKfgr0wNXVVVzSChx5JoQck4pJv23btsHAFScv09SQ2JwAbkBZaD4MV65cWT7si9w/is/5ZBbLrhfCw8NplZrYVaUxi/EDZvRTCbTPh46xtgeLXJTWjbRv394kDmVHHkdoR02RIkX00aDtkydPpmlAm7quac+ePYcPH6bLuXPtrlQEaHGU+cZ94qKoUY84/Oc//4FkEslFnzx5kipVKv1WRjzr4uIiVkOAEghfTeTtqW3btiIyujzNHgs/jUTgIQE5DsgqtFq0I+3VAcGjzyWguNmyZRPbhIh3CfWj1dTirqJ2E3MuSt1ET7PFRLR+TiO+j5hzUbT+4MGDaVrPproS0XxTj+9Rcva4aArpdDKio5/kzTvJ29vgUNMVKwIHDNhRo8YCOtalYsXfzb/co9E1fZmWytOhfHFprrDZ2U39WoK5qEO8CRzmTcDr2o63bt3aunUrXqzLly+XNw8zGK8ukpiL0h5RsVOU1hwLYgl2CiOSvAkzF008YJ1jqBUHSGiwaNEim3pknCacFujTqsh4uacTTgJANmwvOnlX4jzyibkasXEiJCSE3KAJb/VEd99++21Nwf5Roah2NtgLeQYSFMLQjUqbNm3kQI1Z3KpVKzCl+jqYL260yEVz586NaF9++aVJHHoXfvzxx0qcCz6Z0mtA08UAzWOT2w9g6tSp9h6h5gM0S1I1MFyje+/evdKlS+sjW+eidIqant6QsYuaent7a7aZGdrB1GqiCnrXjjRFjHB9UwqGJjI6cOAA1VesRX///fc1hNmh7yJBIDWUj7xK6AlnAh6xuF80NDSUOqzGAWZ8YY+LppBOJ+PHH32EB1178PEJyZjxZ9DRLVvMzsfT+3G1eELjawyM27YXDypkaEDnWkFVXnZBGInC69qODRs2pHdN2rRpE3DOLYORApHEXJS2vYJwwtKNjIwkX0y0di4iIgK/ySMoc9EkQe/evTEe2Vv8RusY9SYsrbAlF+0Jc5VuyEXJlwBNyRL27t0L1gEqtWnTJpmB2OOiijph5eXl1bNnz4MHD2qOxTM0i+koMLFWU2MWlyhRokKFCobCMYFFLkrF++STT0zi5MqVy6Z66RBFtcV5hNeD1kIDtEz/8ePHNPVKRzUY4uzZs/SI/oR0GfZ8F02cOFEf2ToXpfO+DQ+/IeexdFc+n8qQi5JvFTGBr+eitKRW+Pk0xPPnzxctWtSpUydEphYk/QTFAg8EHZUjO+SisbGx5ExSsxmMDnnLmzdv4h+xyEUV9fhBzVReAmDiuygldDqBHTsu1q27+PFjx55yxozZBy46evRekzjMRTWYPn16yZIls2bNmiNHjr59+2q8OjHOnDmD0SmrCgxEY8eO5d1oryJe73bEW6N48eJly5b9y9p5rQxGykcSc9F9+/ahe5w//3/fqunQVQCWIp3yclHFuXPnKBzGtLxfnLlovEBTbfbGI7I+iQjJoN1027dvV5KUixIxpuM0Yet369YN7wBqR81h4va4KJ4tWLAgOXtUdEe0G5rFtBMVt+hSYxbny5cvZ86c8d1/b5GL0jmcadOmteeCAr2A+BgJijyVm9AP4WhXbBmnzb2VK1e2VwZQUJvqVtHcR7zJmS56WOei9+7dM2F0UDD6LJ0qVSpxzIkhF127dq1NmsDXc1E6GU/jS1bGlStXIKVevXrR7Kh8ODtN3rq5ucnxrZzpQqcdaBw8UPntTYbH6xHrXBQAc6hTp46VmPZgj4umkE5HOHMmvFGjZVFRlpYfBwaGgYuOHbvPJA5zUQaDwWAwUjiSmIuSs2CxxCsqKoq4JWzEQ4cO/WUE+cQX5qLxgpeXF6yorl27asLRCpAkHSbx3nvvae7S9i2aoE5CLgprG6yDJoXodGxxGocVLnr79m1XV1f5iHYrZjFJQOwt1JjFxMF8fHw0ElizZo2JizBzLgoh0GJj8BkY8Ygp79eV4e3tbVMdz4jlo7RlFCGGlrqei54+fRoiTZ06tb2pb09PT1vizhfVI16+i8DxsmbNqgkUPvEfP348bNgwpJY7d26qsiEXnTp1KgLpiHDFiIv+pR6Wrff6i7agNeGffPJJlixZhJxlLop8M2bMaHvxNDwrXHTw4ME2aaEvgaozc+bMxD8SLy6aJ0+eoUOHWolpD4ZcNOV0OuV/0+x3mzRZ/vBhrBx4/77xgUnK/771RICL7tpl5kOVuSiDwWAwGCkcScxFYUHCcBQL9GH/4ZLOLgsLC7sZBwoHLl26JLsVZi4aL9CqTnAVcTSzoq7bpFWdECyRJT+/f72APHnyJFeuXMIJeFJx0djY2Jw5c5LLU0XdoSdzUbL2OnbsSJeGXPSPP/6wqW57RAgIhk06AcXQLK5fvz5sX3GpMYvpGJV8+fLJxxv4+voOHDjQQJpxIF+v9rgoiJ+YEVq9ejVilixZUn/E6L179/Lnzw8mKc4RVtR9j3RMi0hBhp6LAj179rRJW21lHDlyxMXFJW/evPozYzUAi7NCWQnx4qJEhjWnIX/33XfyOlWavaeVyYZctFGjRkWKFBG11nNRpA/Gi0CwIBEIotumTZsbN24gZZvq3Uds1KRPIbQKXYlblC770UWCpBgmVTt//jyaTyN5KBvot1juhTLLs6BWHhGwzkUxSKI/yhmha4MKxusYEvrConGdlXI63Y0bD0FE7959oUYxMU+//XaLvUfmzz9ZsuT02FgzfstclMFgMBiMFI4k5qIwuWjL6PHjx/39/YlYyh4sCbxfNKkAE4pWabZo0WL8+PG9e/eG4SUOo9uyZUuaNGlgOIojxaZNm5Y7d27RIrdv37apbnVFgmgCOsJbeCoC3nrrLZvk0YS4KJiAmN8bOXIkuKWIUKlSJURo2rQpnTBJZ6+XK1cO5BmGNXkxzZw5s3zq0Y4dO2zqktdt27ZBcwYPHkznjy9ZsoQ8dv766682yRmvoq4CBa+WD7ck5iac/SAjOmcZlvG3334Lc7lr164VKlTQHyMmg7iTu7u7zB/A90DpadYoKChIhC9YsMDV1bVBgwaym9OQkBDkgqxRd03i+/btI2G2bduWzlUXoJkrpCaLBa3Qv39/hA8ZMkQ+F87HxwethrYOCAgwqYuiTgySQ5omTZqYxyQQFYckrUReuXKlTXJYRYCohw0bJi7BDMuWLUu/iYu+//77ou67d+/OkCGDvBeUVrqSby0BsdsWRMjb23vChAmlSpUitgliRhs1EQeEDRpOnni7d+8OKYGgYiwCRaQIERERGFvoVHQEIrLJ8uYBAwZkzJhR7DhAUfEUWlxEgEhtL+6RdviIAB10qdeQb775BiUXpcJQiSrToTgCNPeIDqVxDWWCjh07EmOXtSiFdLqIiKgSJX4tXfq3GjUWiL/PP5/n5jZm9uz/fcoJD49s3HjZzz/7Pnr0f4W/cuX+Bx9MP3PG4NRNGWfOnLGpZ9KIkL1799pUP1giBJVFCMZPx0JkMBgMBoOR1EhiLqqoM0K0a5Rw8eJF/YpE5qJJhadPn4IZ0ikLAEiRmNMgHD16FEwAZiuoDozCZs2aCabq6+uLS3oQhAd2/MmTJ8kFEdC6deuDBw9euHCBDHfA09OT/NAQF23evDn4AEznevXq1a5dW54G2bNnj5ubGxFOLy8vFJJsXNjQf/75J81Tkf0nVmZCSYiyArBcwffIpU26dOloMxv0CvY0iDSMeBjH4HIogGCAyB0VpNmzd999F5YxzVVC/YiZEGNHCiZHkx84cADVJ2JjU88CRXbg2NmzZ7fFQT+ZdvnyZYg9R44cKD8kQ7/bt29veDy9ok7KgaoVKlQIXAisrGXLlrVq1QJdRDOhCoaejUBpwNBgUn/11Ve9e/euUqUKCC34v8ODPWBn161bV1QfpVq/fr29yFCVsWPHUsOhCuPGjUO+5umj1UqWLAnlkQPROoULFwZFWbVqFYgoGl1MchIXRQuiUdqo+Oijj2jdhKLOG0OdqLQInzFjhqggMho/fnymTJnoLqS3Zs2/rlYnTZqE2lHrbNiwAZpMR92AC9HggyGF5vZt6tJc5AjhQw/B8cxPEgfp/eCDD0BZIRk0luYUysaNG2u4qMNHFPX0XToQFShdujT4nvx1gyaxofbQcESDRoFQaVIQPUV/S4/Nmzd36tSJBAJAeaA5JJaU0OmePn3+8cez6IwWzV+WLF5EPm/cePjWW+MRgv89emzq2XPzqFG+YLDmFYfyV6tWjYrRq1cvDG54MaH6VKqffvoJpYJw6CwljFRQsJR5tjuDwWAwGK8xkp6LKqqJ8+DBA7zp5bk1RvIBJntAQMCdO3fsRUBzIII8JZIYiDW6UVFR/v7+hh7qYOIjR7HwElmDITg09c6fPy9z2tDQUM36T0V1iHX69GnzvWcaQDKnTp1KVk96sNpB1Ldu3Xrs2DH9kl1DgMTu3bt3x44dly5dkudC7eHatWvgVIgPBmIlvnOAWoMYy81Ea0chhMDAQFRNjizW6D579gzMR3NmpkOg1ngKWqFXJCQlr2JFi+uPlbt69WpISIiiDlDWs8Yg5ufnd+TIEf2aWNSCErT+iEOgbCdOnIAioaYm3xpQ/nLlykVERMQ3fT1eiU4XE/N0374rO3eGXLlynxkjg8FgMBivDZKFizJebxj6LmK8sZgwYcLgwYOtxDTcL8pIAEB09U7LGAwGg8FgMF4tMBdlxBvMRRka/PDDD/b8CctgLpokOHDgAGTIq04YCcPly5cdjt6nTp2ic79SAh4/frxt2zYUyWL86OjomTNnim3bLwXHjh1LpuMf0fEfvQjZAaQe//zzzyMdzNc46LNIwBIPEzx8+BDvC/36i5eLlFkqczhUs2vXrs2YMUPjnCLxyTIYSQvmoox4A3awzY4zWMYbi7lz5/7555/mcWABQ3MaN27snCK9rjA3PRkMe0AH/Oijj2xGxzsLzJ49u1ChQraU4Vs4NDS0Z8+edCyT8NXsEPPnz0f8WrVqJWvZ7AFCJv8IFo/Rii9Ay7t06UI75GnzPLLLkiWLh4dH3bp1x40bp3E68ODBAy8vL9oXDWTKlKlEiRI5c+Z0dXX94IMPunXrJruOI+zcubNt27bCS0LhwoWRRZ48ecqXL9+xY8cDBw4kuPCXLl1q0aIFbV+/fPlygtNJWqTMUpnDopqRe0vZBX2SJMtgJC2YizLiAbzVBg8enDt37qxZs+L9NHz4cNmjJoNhgunTp5csWRKakyNHjr59++7YseNll4jBeOOAEduciwJgfSmEixLoACTrXPTKlSuenp56J9VOA52MlazWPDl1l09dDgkJ6devHxhm+vTp8ZrWONmmU75t0tm/MTExEBE5vS9VqpR+2vnjjz+2SWc+PXnyBEQFpNem+iRPcMn/+eefvHnzpjTWl3JKZd07uhU1Q3M3btw4MDDQegGSRHut14LBUJiLMhgMBoPxhsDweGcNUtqZq5ozbFM+li9fntxctE2bNoZrTC5evFi4cGGb7hCv8+fPExcVx78LjBw5EuEZMmQgP/kCjRo1sqnHj8mBc+fORWCaNGkSw9noHOOXzvo0SAmlioyM7NGjh8XIyaRmiU923rx5vr6+SVgkxmsP5qIMBoPBYLwRYC7qBDiBi9IaWsP9DqCddMybfC7xhQsX7HFRoFOnTrhVrFgxeRc6nVml4aKhoaGUDh37lDCkBNanR0ooVcuWLT///HOLkVMmFz1x4gTUj7ebvlw8fPgwICBg3759Bw8e1PjkDw8PP3bsmK+v79GjRw1PJUCIv7+/fDCBE8BclMFgMBgMp+LMmTOH4nD37t179+4dkkAnbN+/f58u5QOKoqOjDxw4MGvWrI0bN968eVOEX7lyhSKLU2fBOihE3klhj4vGxMTAfESyMFMSwEVDQkKWLl26ePHiixcvisAjR46IGqFUDx48EJfycUQoOWwm5X8Hyd5AIuvWrdO4WjHkojC2EHP69OlbtmzR+5tBXppdAFevXiX7GFmvWLECBrf52cICCWgp2Zq/fv36smXLECIKeevWLTkFFFVR7T8RYuXILhMuCnz//fe4mz17dnGokjkXvXPnTrp06XB37NixItCQi546dYrSgfAtCO9fXLp0CdwYkkfDGbI+QxUSQCvMmzdv5cqVmnPCCH///TepEKS3YMECZEHh5kpipVTQlvXr18+ePRuGu8ZqR09EH0R2hw8fhupaX5UKhYc+zJw5c+/evcKJFBqdWq1MmTIW1cBczQSg+SihJhBDB2o9f/586IMmI4vJGgLNREudIXNUQT7uPjY2dteuXag1/mtcYeHW2rVrSbwYf+bMmSPO3Ebg6dOnEeLwtHOGAIYUqBaGO/oP+Pn5kX5CUSkE/YV+nDt3Tn4W0RCC8OPHjzuzzMxFGQwGg8FwKvbs2UOTV/369XuoYsSIEWTlw0AkmoT/sAjd3d3FJ+rt27cXL158xowZsOfwYJo0aQYNGkQHR4NO9OnTB49/+umnFBk23Ndff42QL774QuRryEVhqRQuXPiXX37x9fUdMGBAhQoVrHNR5I58e/bsiVK1aNHCxcVl6NChdAtctEqVKkgqT5484EIwQPv27evm5gbznQgYzNzKlSuTb+1JkyaBDpFLHg8PDzwrstBzUZAWxFm1ahUMpubNm+fPn18YrxARQiDbDz/8kEK2bdtGubRs2RI5InK+fPlwWaJECSvuYRPQUsKaR+vkyJGDfEG9++67xLHRUtQuqCzKRmWAzY2MEDJ58mQrJ+iac1GIhUoolt2ac1GgYcOGuFu7dm0RYshFBw8ejMCsWbOC/jksJOHJkyddu3atU6fO5s2bV69eDW3MnTu3zPpMVEhRJdO9e3cUD/IZNmyYTXXXhETq168PqgOi6OnpmTZtWpTz119/pTqOHDlSMVUSK6UCZs2a1aZNGySLpkcWKIOgZGDORYsWhTrhx+jRo/FgeHi4Q1GgLugC0Ex0NB8fH/yoXr06qRBYXI8ePZBOgQIFhqtweCC8uZqBYaL81AE1k5zQW2QN3cMPV1dXPFutWjXIc9OmTQ6TNQcoKLoVjR6ogvDFDebTpEkT6PaYMWPQKO+//z61BaTdpUsXlAGPQJJ169YtW7Zszpw5cYkB4fz58xUrVixXrhw1DfqdwwIwFHVqmkgmiGVMTMyhQ4f279+PYQcqQRQ0NDRUUUct9Clc0miM9sXgIOgrc1EGg8FgMF5zfPPNNzCwYH+LEBiICLl69aoIwV0wMfpN7mdkr6cTJkxAyH//+1+69Pf3l7kocPToUYdcNDAwECQQNr0IIZvYIhdF8UaNGiUuYTviWRAAuoSB/tZbb4FdwDCCJfT555/D1hGRYQOBdRBZhd0MYwgGU7t27RAC5iBscQ0XRZzUqVPDdKbLixcvEs+ky4iICJAQhAguCvz5558IyZUr19ixY1EMUAJwHoTMmTPHSh3j21JkzUPIM2fOJGLZvn17hEycOJEigH/CykeIfPAMmq9UqVJWyqM44qIgWsTKIFUKcchFScgw+kWIhotCzv379yciunHjRovlBNCg5cuXFxOA165dozlYwfrMVWjq1KlysTt06IDLAQMGIAR2NpoblIkWGM+bNw/KDFHv3r3bXEmslGrnzp2yK+aBAwfirtjM2apVK6iQuAuiJSuDPaCXIRF0W7qE+uHyt99+o0vyKxbfNbr21Awh6H0YHDRcFBwDkhHnIEBoiABKDHnS9wWH2msO8jQmr9G9ffs2yKegshjBEOGDDz6g+djY2Fh0f4R07dqVCoD4GTNmdHNzgwbSuoPIyEhoZubMmcU8P8MeMLZA+CCZ8rpcAqRHPFMMrcRaMTjgd1hY2AEVREeZizIYDAaD8ZoDxp/tRVeokyZNQsj48eNFSO3atYVxXLJkSTA0OQVYG2B6eITsBuIbMhelLMy5aN26dd977z05WbKYrXBRWM+wa0NCQp7GwcvLC8/Wq1dPxFmxYgVCatasOWbMGFAITQobNmzQTL49e/asQIECNukIaw0XhYWdPXt2OalUqVKVLl1aXF6/fl3DRUkO8qQflcriprj4thRZ8+IbgRJnf8sipcnV3r17i5AffvjB+klp5lwUyJYtGyKAQdGlQy7q7e1NEcSWUeKiSKd48eKg8fj90UcfjRs3DlTBYiGBw4cP48ElS5bIgWXKlBGsz6EKffzxx4gg5opBEXEXVFCkRrKtWrWqnIW5kjgsFZQQfQ08TZRq//79uJslSxZiUBCFPFW4detWmmsyB4qaKVMmsbyZvi716dOHLhPGRc3VDHXU6DmtBKYlzYrKT0DCPTw84pWsCfRcFLqKZ4UkoWAQAuKItQ900JS8E4EWMsiLI7788kuEgDtZKcObDHRPCB+U8sGDB0FBQadPn7569Sp1n/v37xNNFZ9gcBchAQEBcgoYK5iLMhgMBoPxRqBcuXLy5BjYCC5h+tMlbAJxogbsCdyqVq2aJoWuXbsKUpQALgrDBZfNmzeX07S+X3TmzJkuLi71dejYsaMcjezIEiVK6Jcdbty40aau0ZUDiXzCaJYv5TW6Ym8eyMC0adNs6hmY4u6tW7cMuagsh/juibXeUoqR9xeaoG7QoIEIiYiIyKSCZn5gLKIKVtZ5Esy5KPgSqJc8BeeQixI3RnlECHFRsL4nT56g5CRkKq110JSy2MNMkHdmOlQhmjQTS4Kpcdu0aSNSI3aqWUusmCqJw1KdO3eOupK+YETF+/XrRwnqT2c1hygV6He3bt2QSJcuXSgkYVzUXM30ccgDs5h2BooWLQohxytZE+i5KC3K1UsSDUcR9FwUdxGCfEUIHZQaX2m/gYAYIXxfX19af0ugE5vQkekSnUhR18Yjmp52MhdlJAEwwFl0yZCigP6zdOlS+XLGjBlW9ifECzduPNy0KdjP71ps7P8+Cz14EBsc/H8uNO7cuRPft2ySIDo6Gi9jeaWWIUJDQ1euXOmcIiUtkqkpEwkYHGLW5bXE4cOHFy5caGXjGeMlYtasWTCwBg8erKi7d2Da0gpV8jXSv3//NWvWUEyamihfvrwmhTFjxiCcDPcEcNHdu3fjEqa5nKZ1nkareWNiYsyjwfRJly6dm5ub7GyJYMhFFyxYgMAOHTrQpaHvIrzpYC4PHTr00qVL4F3vvvuunF2Sc1HrLaXYt+bFklFCr169bHFnde7du9fT09NiYRRHXBTjGzHPXbt2UYhDLkq2fuXKlUWIvEYXL0faN1i7du14HR1J+xU1U6ky63OoQvQhY/78+XR54sQJm+oaR0Swx0UV+0risFSgaubMJzIyslatWiRSCOr69evmcpCBtobCT506ddOmTbLyJxUXldVMH4fWPAvNR2u6u7vLX6Msaq89aLhoRESETZqfN4R1LkqLw9FwRV/E7NmzrZTtTcCVK1eIcAYHB8O8xJBLl+QuLigoiKZG0Y+E+yLNmMBclJEEQB+2uKw/hQC9go7bLlCggAikccfLyyupcnn69HnPnpvTpx/VqNGy1q1Xvfeed8WKv1epMm/kyD0UAeYFDLIDBw4kVY4WgVcsairvS9Hg0KFD9OKUTatXCEnelIkEKCi9+cyPtXjVQascna/PjHjh4cOHmTNnhio+f/588uTJI0eO9PPzI3IYGxtbsmRJsZiKlvPJ0xcE2nI2aNAgJUFcdNmyZTbdWZTWeRptJDt9+rR5tHnz5tGhl3ruZMhF165da4vzQKMYcVFQEWi4mNdyAhe13lKKZWs+NDQ0derUuXPnfvz4MdKRt+w6hDkX/eWXX3D3rbfeEnvGzLkoCp89e3bc9fb2FoGa/aKwTcmH03fffWe9nEWKFMEjNC0jILM+hyoEilKsWDEPDw/Qfoi6U6dOjRo1kl2/2uOiJkrisFR0jOq0adNMqoYyTJkyhfzugM5pUjMEKHe3bt3QQ+nDN3VqJ3NRKFvTpk2heAsXLsRv1BR9kybKrCdrAg0XDQkJwSVyNHkkvlz03r173V4Ez5cK0LwoIPr+kSNHcImGUNSeTutyAXQof39//NAsEGAuykgsLl686OLiUrBgwXh9uXzpoNekzEV9fHzwIgwMDEyqLAYOxOvq/+3Zc5kunz17Pnz4boR067ZBxEEvbd26texawwm4cuWKp6fn6tWrNeFyC9Ir6hXlovFtyuRQXU2aJM/XjItq6gibEsr8qnh6eLXGq6QFLFGysYoXL37nzh2ElChRws3NDSRTnky4f/8+cQnZYgPIhycd9pgALkqEqlChQvIUunWeNnz4cMQcMmSIJhwmjjhIBsY9bE2UH4QNkf/44w85piEXpakbMFK61HBRKt64ceNEfCdwUcVySynxsebRSW2qhyEkJbNZhzDhohA1OQr+9ddfRaA5F6Xtr3hKnp/U+9FFE1AioDEWy1mnTh3EX7BggRwosz4rKhQQEFCzZs2+ffsOGDBA7zbJkIuaK4nDUsEWt724Q5jw6NGjzZs3K+r0LIWEh4eDG9tedIxkD7S0W5yw8lK4KNWiVq1a/fv379OnD7RXPlTWYrIm0HBRaDV4b6ZMmfSnwqxYsYJ+xJeLMkwAhYTw9+/fL4Z0UE2EyEclgaaS+24YZoKmCjAXZSQWGKzpVaHnNikZeP9puGjSAn3S1XV0oUJatxD9+m1r0GCpHIJunD9/fisO8ZIVGCDEPh/FyLR6jREv6zBhado7YvHVhUZhXjkkR6O/KiA26OHhIVyYEDFwdXXVmAjNmze3vXgCJODp6QkmSYbFzZs3iVGIWSPYzbYXffZolD8yMtLd3R0h8qTcunXrENK+fXuHhd+zZw9ipkmTRt4edv369RYtWpAlhJJUrVoV0RT18zz4QM6cOeXjQAy5KIz7IkWKCG6m4aK02U/QjKioKKLT4vFk4qLWW8q6NX/69GmEZ/7/7J0J2E5V2/cvhERkCg8iKjI8NEc0qVCUCBkaVHgMfaYMRd4QmSpDhFCZHmNRoYHeCFGIkCGEEKL3VRQ96fp+3/4f9/qWva9rX/sehf0/HI57r2vttddwrrXO/xrOM2fOzp07B89JNInEerkoGj/NzU+mCYStW7fG46Jw/mzZsuXIkcM2FQN0R9S+mQkef/xxAolPbQTJp86QQzbsncxKlSpFHB8e0QAiBEOrX7++z3WDmFzUX0gS5opqzJ07d+T0Ez0nT56kNvbt2xd1zPmacBIpUaJE2bJlE9ZGmTJlbC4qITQ3Y7WF6D2HHw8p46IQ0Vq1avm45EklF9VG94IFC0wIIwAh8H97zXHw4MFmsSnkomkIeKZuiupilMxu6Y4ogrpu3TpGAK0LIM8ymSufLgbnCBdlyNi5cycytGTJktWrVx88eNAbZ8uWLWscGO9e1BFvMbpRiV988QV1kaw1whBRR6tAw5DVde963t8Z6c1F9+//JRL5rwsv7Pc//3PapZSjR0/ccssEV+RevXpVrVr1DF60Y5hAD+vdu7cJOX+46OjRoylpeqd5jnFRr8CcXUiPRj+7UKFCBXRxswR26NAhHmvUqOGKhhJcsGBBuJCx2IlWcdFFF6HRmjjaEBswYMC2bdvefPNNKXCFCxdmbtWUqutb8E/zigyoQqhQDRmKefHWW2/VgDx58uSE1gfEfHLlyoUOOm7cOHgj0rh+/Xr9iirfokULE1mrpfYZS3FR2+XDp59+euGFF9qH7tq1a0ecESNG6FEuLvUVFIZWrVrB5WBHqFliU5s2bSIC9MCkgMoVOX3HWPZFbbccQRCwpXS51KYruu5bvXp1b5paYkh4ztkFXdwwvIUJa/fu3VAsSk1VMBq4NChdDLZJwokTJ5Ac7WJVrlzZNJmB/Na48oyEiLPJZ2zCfEICixYtqqqGa/FR+rvMqLZp0wYVMZpIhKjeAgUKPP300zB/KnbatGmLFy+2N9lk9tk23RxNJCRBcqUTB+Jg9JEhQ4ZUrFjRbAhTCeYubtTZUw1ydFnXkaDW9LLZs2frKux11123du1aFGD0YcQJ4acpUZJtch4TQcRs1KhRhDz22GMm5MUXX8ycOTMEGGmh1PTxDz74wL7vmizp9UIrR/RZqA5DED1dJohF/vv27ctHaSx7+UkU3WyDR5Po68cff2xC1E1cpo9DxIQuhX7++ecbN25csWIFf/O/FgLkxMX+SdJu41zgogyI2g4GxmWqlpEMfvrpJ2PcycxzqjvtLOsPKig0vJEsjBkzpmXLlpD/rFmzupaUbDDMyZw37TJ16tS5c+e67MowhzFdwWz/+OMPmuONN96IeaqHEZzXGcjsrX8BcdeZTH6aOHEiE563KRmhSJaJh1+1Zuniosz3Zvlw//79X1g4evQoYqa/g1zS+PPPU9mz94OO1q077fffT5uh33tviysyk0TkdCtzAUGuTA5lIxv1whUSdbawFGK/aMZc2uKOO+7QRgFxpKDYXJTIzBwTJkxg6kpW9o4cOYLaxzTwySefeI9EMgsuX76cSYg4Xvsiv/zyi8zQo4h89NFHfN27dUy53nrrLV7/4YcfXDYh7KYU+MS///3v6dOn047mpgpzMzMxJVX92GKJAo3CgbQg1S5ZInHN2cSZMWMGydrac8w0XVx069attnQpEF1Hj0F0RBJEjH/++WfyRknJZ0zT8z5dJuoo0HSWmTNnxmxZmgzVhz5OBLvyYwqMwBCqpKAupnQmY8iDtwf51LM/UOaUPf43K4yCv/DEa3SmCQ1TBCJXJGJe+f777+fMmTN+/Hgy6XWhRqlpUNUncexrM6lv6HQCvdJleBbFy2wa2KBnPfDAA5dffnm3bt26dOmCmu6SNEYSOfNA3ezcuTOdi+qtWbMmwziqIY2r04kA7dxcJ4bmoanrLYgoUsojxAAd1N44igm6W7NmzbJkyaJkUVjFIhjV0c4JgYvqdhz/y95PxLHJibYdTeKi1apVu+mmm5o4QGE1rUP++/Xrpx2qUqVKkU+kSJZLCOGjTZs2RWZQtXmEXTDMoq3efvvt+kr79u2ZZRAkMbdMmTKhCiNa8+fPL1u2rDYkBw8eHFzUg7QUo5CuI5I4ej/dAfm/5pprtPvXs2dPl9BCrmAjATMQdahX48aNI0nInz9/4cKF8+bNW7JkSWTj1VdflZESA+qnR48ecFTFp4mZavPly1ewYEG+C2eApro+wRQjmiRA2GzLTAxfefLkIZxEEMKEGUblkIsOLXlA52hruBzsThQonggJkyZNEku0gUiIVDNYicnweteuXc1E4y8kQXKFVCAb5tNUr10JRC5Xrlz//v1pbmgbLeIa92ICVqyqQzZ4l4mDvhxxzuVq6Ps//+f/SE4Yz/3FMqGY0d2GDRsmi1MUkM9pXoZjGGEwQCrk4jW50usF4qG7x8ywRgtlJOFR38qVKxcpSwmB9mjVIOIsUVE/ZLJPnz6aFJBPNDF00QEDBmiAqlixojnZGyIeGLR1+FZYuXKlmUBpUF0fFWLOoecCF0X6ZU2YwYWOhO4FmbF1HeqIaYYp0OaizC56lBKsRIDPKYIQXpQvX14juG6SeK/yM+dp8GWYe/nll7Nly8bcHHEOHWk5GXbatm3bAgUKSDUkQXl/luJi1lnRaTp06MAcxsTMLEUivXr10k/oCldccUXEMXPHLMWcJ8XIXhqPOhrGzTffzLDLLEjMe+65J5LERZEQGJFUB3NKBJHgW5qrevfuTXdCrWR4bdCgQcAO07HjQrgo/669dsy6dT/6R2Zqv/7664MkawNh1tLdpZdeKgWRIeDqq6+WpmVuh5Nhapja429Uc17Jnj272fNESdLpFCYnSipP5YaLovSgeaBFUefMkStWrAiYt5EjR6K2omKi+TElMNnYdIhskE9qGCKB/so0gO4i7wvffvtto0aNyCGFQqsjmtoXVcD2SfXcc8+huxCBLCE2bdq0icZpyqijS1G9UGKUUVpQfhGoPWYgTfy9HYhRRJ1lWjTU1157jbxlzZq1Tp06WhRnepM8k0Nku3jx4toUQkWQWhAvTRcX3bZtG4pFxFlEN2uEaNJDhw698MIL/e8PM8TTF+S2nmENSaZ+1LPsy0g+XSbqKD3UGOViJn7++eel95AUkoDCFHWuThGCrgBfokQ0h9GKvAKDJorCLf3s3XfflfwoDl3GKAdHjx6lhzLBL1q0yL+eEwJdHyX4lVdeeemll2S+H7EJIjwxGwjxqFevHhlgBCMzGn9kxobahgnwLZoeDbVChQqkqRKh2RBH2icUlO+asYuhRq4yUtPQ6QrEQ/cPDXSeyic+Feg6WGWA8CMwUj6oloAmrPkc7aWKIuUgirUNJnEm+hRM2eaMLlklAwF9V6I/0RfsVScGE6/DmDRHclsqCOiGr7/+eurydRaASRz9WAzEtpRjEE+E4B6MLUxYKJaQ5OnTp9PBn3766YQHhYIIScJcqV/s2rXLxQzVQehcjGzBPfFEnUGPzmtrUwx6duJkMl3NzvN1ppsffvgBHQ8+D9l78803GTyLFCkSswZSAHm29HJppjPCwzOPGQNEi95EW7gGKNqFmf3gwYPMfWcqb16kMRfVpqjPyY2dO3cSQc5YDRdFeZKVYbNdo71j4zk6REJQXeZcLkOMFrFcG1wIJRpwxDldg97JeMe0qoVq9HgEl7F7x44d8mqNMoe6hhCjqmpZesyYMUoH4qElNAFVL2JtJGphD6VQV/xRibTyZ6TixIkTpUuX7tixo0lB9tPFReknjOz/+te/Ip4L93KAJo4Nfbr77ruDr2efPPln/frTRUczZ34Bavrrr3EVF9lsiHm83B979+6FMKOOm4zJIKRNxfmJCpGWj+TDDyOnn79FL5FqbkLERfPkycMUItsSMp4Z0N/XhAkTKlasaIxS6I4TJFCPMp9gn4gbMmRIxHJ1TSbhTjAKSiEFVwwByVEEuWIT/QDoEzp+E68pofpQMv3NjG57EZDs2ZmHstpGhrt3706Etm3b6hGuJfI/cOBAZJUvwvTERnzS9J7R1X2YokWL2qP28OHDbU/08cCopWXjO+64Q755YAKZM2cmNRPHv8vIUos5ffDII4/w2LVrV0LUapUrV7b9/kG5bRlzCQyvIDC6gSMuGnUkE26GcNoEhh7drVu3IPXsAwZz+4ClTnPBElWTCYUn6mkgXunRowchZcuWnThxIppi8+bNtXVDDqk6U3Ckq0SJEjly5NBMQU60qkVzoGMxmjHmIPkRx0eiXklNQ4dID8S8L3r+gAGQ2fBssTGW8Zg9e3apUqViTvTnrcykBlD6vHnzxjx607dvXy19hgiR8UhjLrpy5UpIEXrPrl27vvnmm61bt9qLUgy7S5YsQXPlD9e+KFqFOVjCuKON0zNuQuYswoMPPihTioIcc6MBu6K99957ri1TNGm5fzDuFqVY2wsKYj6yQbd582Y0Wijrf5LQv3//iHVbQ9bk5TNNEBsxavGgQYN4tO8noB9HTj+jq8s8Li6KcqkbLHPnzi1XrlyyPHpFHbl64401efMOFCMtWvTlzz+PPfLKXmKyLOwbiMeavSbynC9fvksuucSYqlu2bJl9yotSBOSixq961OHzkWA3bOlEOXPmnDZtmgmhtmvWrImWr8fy5csXL17cfoU8FyxYkPTNnnPu3LlhMiYCLN3Os7RJ2/y9WbaIepqSLi8mbNQLO7KLliCc5I2sGmHTzZNcuXKJS8gkiW2aZcaMGS7JCcJFo0kXVOzjdjfeeGM8X3wuqNHtbWqdABRDS9hlrr/+eiKYCpEpDkOfAHTdNmhx5513EsFsWnoFBjz55JN2p4smSbW9A1O9enXdPExYzz5gMHn00UfNi0im9jmNHRR/4YnGaiARWlrEDtSKlZFbQaONseCiQ6G28w9jPtSoWalp6BBpjvOTi6IdLV26lMGwbdu28lkaIiYYGwsXLuw9AvDZZ5+9/PLLZyRLZzWeeeaZSKwLXOgJQVYeQ4RIJ6QxF9UdUXNTVLuduisSdcZfVBxZE3bdF7UhV628mNCDdgiBcQTF2j72LV/h+fPnd9VhzIlfd80ZpPTotWl2/Phx3UE9duwYzCFTpkz3emD4lbTDl156ybwuO+bGV3WZMmUKFChgZ8BruyimIfKoc8BVJ3UNc04uDh061qTJbNHR7Nn7ffhhjD38zp0784mUeU+W92rD9o8cOZIjRw5CZs6cqZDmzZvbl0W9donicVHXkSQ0fkhmwvygu/OurmZ5geTw6+233+4Kb9myJeGDBw/Wo4tOuNrrwIEDoh/t2rXzHi7yNqUErEaNGt5cuWiJdlyrVq3qlTed5QtiHjMgF9WLVapU0eP27dsrV64cs9K8EBe1m9V2D5CwyxQpUoTI5nCamts2X/mXg6izTAAlgzfaqzkxuWirVq1cXHT9+vURx0iJHrdu3VqrVi39nbCefaBDud4XYdSK4C880Tib4RHPLYMWLVoQuGTJEjtQlmPpCKof9VzX4EC5CNQxjWjqGjpEmoPGisT3k3lO4tSpUzpqpBXe5B6HPq+gy4SMeF27dmVGHj9+/Isvvli3bl3+P9NZOyvB6Jc5c2YGzKeeemrUqFEoikOGDGGuefLJJwPeyAgRIj2QxlwURUH2h1BJ4S0wB92OjSYdxNWp0XhcFH0CzUBENFlH8M9z9OjRg8HlKgs6FuvaIojG4aIirsZsmpeLAl1237lzZ9u2bfnDZ5nAn4uiTEMmUV7tV4Jz0WjSGWBmpkS14oeZMzdecEEf6GiRIkO9h3Xl8Sxly67oGUWLFr3wwgs1svfr1699+/ZQEen9UFOXxfbUcFH73GY8PP3007wb74iBNqC8RuRl8t6QpYR0Yu7cuRSZwAIFCphFB8HblNu2bdNW/AUXXEA72rLkoiXaCvNxY52GXBToPKe2N/v27Wu7ffeHPxdN2GVkJsTU29q1ayPOjWs7ztGjR/v37w/bJ3vaFzU9NCAXBbfccguBuipJrzR7gwnrOR5klNXlXNGFtOKiuuppuwoQsmfPbrY9Y3JR2SyxN1RT3NAh0hYIefny5ZGQ/Pnzd+zY0TabeW6DvkwXYFIID38lBN25Ro0azKowUmrsueeeS6trjecn0M8bNWpUunRpBt7q1au3adMmPBUS4owjjbno559/DpPUpaloktNVgIIuLy/bHchcNdi8ebM5fXHixAlxV1HZtM3YOQzqjTFl/fr1P54OWfMvV66cHTkmF9WdRlkHicbhomhvMAeUeDmP8rE56c9FtY+RJ08e+5XgXPS3335DJUVxyZw5czxDwV7MmfOtN/Dtt9dpd3ThQvfWaIcOHbynAYND5mfGjh1Lua688kqdiSXDe/fuHTp0qH2WNZr+XFSXD+NZh9dl0SJFirjCdSq7R48eekxIJ6IOwzTmK+37sTGbkjpp3bq1TGdVrlzZrMi6aMmECRMip5/+dSFtuai2aGCGUcefQXBDLP5cNGGXoa+VLVu2UKFCq1atojtTe7bTi6izxleiRAlzCD/FXHTatGkEtmzZUndcjQ2JhPUcD3KIV79+fZ84acVFVWrvaQWUVARJm0sxuaiWY+wN1RQ3dIgQIUKECBEibZHGXFTGgs3hsePHj4tzovqgqP13LMjjy7Fjx+TNZe3atRlgDe9cArTB5VlL0JG8yOk+mmJyUZlO8fE7DPLmzQsdjSbtGfbs2dP7ObmH8ueif/31l86sGhd50eRw0fbt21Ne2fupUKFCQvPiQuPGsz777HtX4MmTf8rRy6xZm1w/iTyYO5/Jxe7du1GOYSPQUW0Zad9pwIABKL6udZb05qK6mgj9cIXTVemVkEAJiau55VrNkB9/OvHdd9+ZAw6UNFeuXBHLV5irKeFatpUjGT41lxhdtIQBIRLLWS6f05HLtOWihBcvXpy2mzlzpohKQPhz0YRdJurcX6hRo0bHjh27du3qcud94MCBiy++2JynjaaCi9JfqI2cOXPSKGahIRqgnuOBGsuSJQty6D3fZSzvpxUX1QrRk08+aQcynpA4UqTHmFyUpsycObNNOFPc0CFChAgRIkSItEUac1H5pTE7/vANHqWiHTx4cH8SFA527twJX5VTPrnBQVX9IwleL4ghXDh16lSZMmVst1c2dFHK1mJjctG6deteeeWVZpPEy0V1aHDSpElRx2aATlfaW2179+5t2LChrmwlvC8qW5e2HV0xomLFipmQmFwUDdV4FSfP9l6uP3r2XHzNNWN+++004goX1THdH35w20WoWbMmBTQGr/ft24dkBvmQnULE8cyh63YnT57Mnz8/HMD2Hy14eaY2qexDyKnhomo7CAMkzQRCgYwBVfmhGThwoP1WvXr1yLy5yORPJyA8tiUY3VA1VMTVlFBx22YpI0DEstkrpyzmuwiGLlbBqM0rVGaTJk20hhWEi7rSjMbnotEkK6+0lIsQ+sOfiybsMjRH/fr14xmFnj59uqsXK3FjjMcrMNE4XDT6//pCT8JdphQT1rMPZAoIgbeH68GDBxuRSMhFvQ0Uk4tC3RHjPHnyGDNg0aQVN7OW4eWiRC5QoIDLp1Q0pQ0dIkSIECFChEhbpDEXPXbsmK6MrlmzBi1BhNNr79R1X9Q4FHUhpuHpEDbeeOMNWyt1QXtiEcfzoULERW0fDJ9++umFF15oXxUTF5Vny6ijkt5999233367OTTIY8Sxsdm8efNx48Y999xzUFnjnLpv376R0034yqSnceOBbGTOnFn7hIcPH6b1daGOwJEjR2q/dNSoUYQ89thjJpGDBw9efvnlxrovKjJ6ZNasWU3RfKDjuPffP+3nn/+/vtu3Lwzhv7p3/8QVGZUafdfY0jhy5IgupCXL2uGcOXN4pXXr1iZEuzrLli1zxdy0aRPhJUqUMCFSxGkFusn8+fN/+OGHrVu3Rhz7DSaOFHpqLMjOsE5rZ8qUCfIDSZBnNnMfm5osWLBgoUKFzE41BA+Wa7grFUI9QwPMjUfZ/uUtPUJ4br31VvM5XqRpDIdxNSWCBxEym1SMAJTivffe06NWT2bNmgU7goNFk3Zowb333jt8+PAhQ4ZUrFjx7bffVvylS5dGHKM75usy20tJTYg3Td1yJBveukLaixYtSm0kywfaHXfcQYLGWg8oXbp0xPJz499latSoAV+iXV5++WX63bRp0xYvXmx2Gj/++GPepQnopLyCHOo2OCUlWjSWwESTlhhsH6cCv9KUtvsWwb+efSCLu8oAfZ9uXrt2bbPalVB4orEaaN68eRHLzrCBrKyZHV3YO8W0hyZxUSi0IfZ9+vT5xz/+4Z2DUtbQIUKECBEiRIi0RRpz0aija+rWqLB9+3bver+Li6IehVw0BZDX+4jj2PCDDz5w/QoRlWf5iGNRRjZRxUWrVat20003NXGABmnv50STuCja5HXXXdeuXbubb74ZrmhzHlqtWbNmsmcLqlevbrRq9GPtchQpUkTkc9iwYRdffHHE8ThqtkpoXFmv0Q4JGYCQ3HPPPZMmTfrxxx95pWTJkvzEi5TiwIEDixYtQjNGfzXqPoQnX758xOH/ESNG+FfUihV7rrpqRKNGM8uVe61p09mdO394yy0TcuXqP3To8j//dLusgNza7B39WA5O7G3bhEDBpVw7duwwIXBOr29uqsvcsWzfvr0OFKC+qwmgLjATKkc7yaBNmzakCZlv0KCBQmjBhD7ByAw6ukQl4ngldb1CDT/wwAMwnG7dunXp0gVqtHbtWv1EH5T90ohj3eobB6SgEOjT/v374aJUDux96tSpQ4cOhVrIwAxy4m1Kxgea7MYbbxwzZsybb74JKbK30GfPnq11iipVqsinPKMHois7vRFnq9mcAmCcQfZEs2FB8FuYmJypQIZ5SyOPK014jnatQatWrbxrGS1btqQSAjY0FKtfv36yMk36FJxPyLNIxNnMlKEgny4DEHtTQIPcuXOrGimFjBsBui38VsbGsmXLpkPULoH57rvvXnjhBZmSotO99tprrjzXq1fP66/Ip54TApIM39OL5OHFF1/UHmkQ4fE2EFy9TJkyEWczv2vXrqtWrbK/NXnyZDhknTp1IM9US/fu3W0yKS4KQWW4aN26NWz27rvvjmfpJFkNHSJEiBAhQoRID6Q9F406as3Ro0dRDe3DVCH+DjBndFEWUWpjOmwwZ3TRC9Ed4+0boIWvW7cuNWY/9uzZI7aGwCR0HZEa/PbbHzt3/qwPbdhw8MMPv1u//sDJk7FPgMMZXHfSqAFKapxABIRXA0543NEA5r9hw4a0vThNmrSmCF5M8DkieD25JQTdnIpFomjNjRs3+m80EVPDAjwE7u118k4t2XeJhVOnTiGuhMc7yOqPmGnGw/XXX2/2M9MW8brMjBkzXnnlle3bty9ZsuSDDz6YPn36+PHjtX1t4mzbts2WKIpjX9FMlsCQTrxqTE097969m3dTts2YrAZS/K1bt3ozac7oHj9+HLbvlS4b6dfQIUKECBEiRIiASBcuGuJviyCOxWPaLjpP8Nlnn11zzTVet7d9+vTxbiWFOPewatUq7/nVdMXs2bNLlSoVk/v599MQXsS0XRQTGd/QIUKECBEiRAgvQi56fiHkoj7YsmVLzZo1vdtWr7zyisvZY4hzDJ9++um6det+/vnnG2+8MYOdHF5//fWFCxf2bkd/9tlnKfNwez4jIRc9gw0dIkSIECFChPAi5KLnF+RYzxjmiYlSpUoR53xzf7xz585evXrZxjwNjEHdEOck1qxZY25pPvzwwxn89WeffTbiGKbq2rXruHHjxo8f/+KLL9atW5f/Mzgn5wCeeOIJKvPVV1+N+euZbegQ8cCoG+9Ob9SxQDFp0qSMv++zevXqeG6ZQ6QJZs6cmd41fPLkyQ8//HDdunXp+pUMgLHaeGbxn//855NPPvnmm2/SKf2w0523CLnoeYRRo0aVL18+d+7c+fPn79ixo3dbYNOmTShzuR1UrVp14MCB/heuQoQ4B8D82rBhw2LFiv3rX/8y5l4zEpMnT65Ro0bRokVhpLVq1Xruued8VPMQMXH06FFYfeHChRm7Spcu3bt3b+O71eCMN3QIL+AJLVu2jHmPfd++fcbil8stc7qC/ihT1V4H1yHSCt9//z01nCNHjoBOwpOLXbt2tWvXTs7M33jjjfT4REbi/fff79SpUzrVVRCcOHGCDOTJkydi+edLQ4Sd7jxHyEVDhAgRIkSI8wh/E9/dX3zxRe3atV3rAnbe/vrrr0KFCmUwFwWvv/56qBb7IPXyc+rUqRYtWvTu3Ttdv96oUaNzg4uCJUuWNGnS5Mz6oGratGk6cdFo2OnOb4RcNESIECFChDhfsHHjxiFDhpzpXER37NhRpEiR77//3g48duxY27Zt7ZCrrroq47nov//971AtjoczKz8TJ06ElQWMLI/E5wYXBV27dj2zbqi6deuWflw07HTnM0IuGiJEiBAhQpwX+N///d8rr7wyZftRaYhTp05VrVq1Z8+ervBGjRrdeuutdkjIRf9WOLPys3bt2uzZswe/UniOcdEjR47kyZPnww8/PFMZCLno2YJffvnlm2+++fzzz1esWPHtt9/ap7sPHTq0evXqJUuWfPXVVy7/bbz19ddf89bSpUvpaz4uANMcIRcNESJEiBAhzgDQCbZu3Rp17uqPHz8eJdt7JezEiROLFy8eM2YM/7uMq/HTggULos7tu7FjxxofrX/++ademTlz5p49e0x8GN0dd9whU+pffPHFhg0bdu/e/YUDMqA46CIKcV24JW/wEJSVCRMmrFq1Kkj2fDBr1iyyYRuVgZ0+88wzBFauXFkZICRqcVFqZtmyZRTzyy+/9Ca4Y8eOqVOnTp48efv27QHzEHXOAKOTTZw4kcwfPHjw559/VritFu/du3fatGmE2B59BWpj7ty5o0aNohVcv/7nP/8h8NixY8o2dCimOcDDhw/Pmzdv3Lhx6IXJdeq7Zs0aZGbKlCk0ovdXRGLOnDlEIGWvUKFobty4kT+oLoq/cOFC19dj1oxXfhQ5uXJoV5HtFVn1GXVcMX/00UdImv0WIlq0aFG+ToXz9ZildiEeF/WvnKhjT2v58uWU5f3339+/f7/r13hiY2ojXo/wL6BAu7z11lt894cffvD6XW/SpEmFChWCiwq1hOiSGdiF63wvj7Q7mSc1ejRCiFR4U4CQkGcKS7MG56JfWEAMzDhjQqKOh3k9yoy8f6f78ccf7RT0Cjk3IRouQkQd6wk0NyO2/gcrV65Une/bt08hEE79sWXLFr11/Pjxzz77jBBk27zIAJUxeQ65aIgQIUKECJFxQC3o06ePWBYKcaNGjbJlyyYDvzfffPOhQ4dMTDSGBx544JVXXnnppZcKFSpUpkyZb7/9NuowxlatWuXNm/cf//gHekauXLl49/bbb+en9evXlyxZsl+/flAFvpI9e3bUbqU2f/78e++9l5i33npr7969UbVRNDt06EBI1apVFYe3nnrqKULuueeeqKMC9uzZs3Tp0oSg8JUtW1YmZ3TJM172EuKWW24hvq1SwzTatm1L4pdddllvB2IpqiU+fcUVV5D+hRdeyOPw4cPNi0SjCO3atRs9enTDhg0zZcrUq1evIHngRZgVkbdt2zZ79uzcuXNDmfSTUYt79OiRP39+6pPHUqVK2duzUF+KAKmGEz700EPFixdX2dH2KEiBAgWU7fLly5vGpclsPkD9Qy1ee+21zp07Z82atU6dOl66GxM7d+6sWbMm7fLJJ588/fTTWbJkef75582vEJ7HH3+cdvnwww8nTZoEdbn66qshXfp1xIgR1KQYXZcuXajtSy65hMcWLVokrBmv/KRMDmlr2ktVpCql6ugFxLn00ktJkwwrk3zaWG0lw+XKlSPw0Ucf5etwuYQV5eWi/pUjkDKBiBNkkqa54IILEAPDmX3EJhq/RwQpoDL84IMPEmHFihVITps2bVwlglXyFg2RsOx0ro4dO/7zn/+EWixatIg/yLZ8p1MJdBkEm6Sg3PR0MoOU0negwXYiVB11jqiTAvmnugJy0UGDBknmp0+fDkuEx1IuHvko+RFvhGzfdtttVapUcXHRmJ2OkUrjEpmk7UTyKSP0iRAqPLlLOecw1q5dK5LJRMNAzSi0bNkyKpBqFwXVahHCIPKp+t+8eTN/r1q1ijGKmAghj66ukX4IuWiIECFChAiRoThw4AAqIKrVNddcs2DBgj/++OO7776rWLEiIY0bNzZx0GUN/0ED41fUQRQFAtFHeYRIoBbv3bsXXiGGVrly5Ysuush8qFixYjbrk4EQ+4wlnMHmogD9w3DR48eP79ixA7JByCOPPLJnzx4ogXiLT/b8y47qkzlz5jvvvNMVjjIknmMHiovC0yij4sANKLXZzkJ9h/CY+JB54kMR/fMQddR6iIGpmWHDhkFO9LfUYvgVcRShefPmhAwdOlQRUOxggBAzPW7fvp1fUdb5m4xRY6SskNWrV1MhqPKwDkJIUK9AI++66y6Tme7du/Or665sTNAi1Mm0adP0CDXKly8f72qfE5AslWDKdejQoRIlSuTIkcNczUXdJz6JiNLATGTC1DgO8akZl/ykTA4RAIgc9Ns+fX348GFIBWwN6SJLhMDSidCsWTOTiGwRpeaMbsLKQVnnFfsc7JAhQwj517/+lbBy/HtEwgJCHng0qznr1q3zuoKHIRDHy1G9mDdvHjHNzd7x48fzSPPpEZbCyEMIBJW2iDrjAL2yaNGiJgVeoQX37dtnXtEAFYSLUj9atzLFoXLouUiaHa1hw4Z0BP2dsNPBP8WflWGBbJOrhPk5f0At0UEgmd4N/2PHjmm30yysiLWq48uhDmOXftq/f7/SyRiSH3LRECFChAgRIqPRqVMnl6KMTqDNBJ0/bNq06aOPPvqfJJw4cQLVkF91SJVHbVG6zgFWq1bthhtuMI9QPqKZDTcvF9VHbS4qfVdcVLjpppsIQS+xP+SfPR8sXryYaA899JAr3IeLHjx40JUZkQdegROiP5ls9O/fn19r167tnwfQuXNnuIE5JwxVMAxWarGhH9EkXkF59QiHgQF27drVRECPr1SpknmUom+7hRQZKFWqVNRR64sXLz5x4kST7WXLlvFrrly5EjL5p59+mjqxFUS4Qc2aNdXEOvxMyvYrr776asTyK67HAQMGmAiUlJB33303Yc145Sdlcgi02W5vNUPXs2XLZh5pdCL885//NCGp5KJBKqd8+fI0jR0Bnb5gwYLEWbNmjX/lJOwR/gV8//33eRw5cqSJYFYuDH744YeIc449YdmRWL6uI8HRJI7doUMHE4EiE7JixQoTIvaoFvn111+h3E8++aSdZseOHQNy0WhSxdp3wuvUqWPXxvHjx+kmRpITdjrwwgsvEEIXMCHdunWL51D6/AScnw6yfPnyo0ePfvvttxs2bNizZ48qmd4nemlOZ/ArIdqZP3LkCMOasWqu07xLly7NmGyHXDREiBAhQoTIaKDUoldNnjzZDoQTmjN4OuN3rwfaSUCf0DaCK9m/HEQdHRotGcWaaNpUjKaUiypXNrNKmD0fTJs2TQdWXeE+XNRmLDomunr16qijrEMMvHl4/PHH/fMQTVL9L7744uHDh7vchHjNqGiv+L777jMh5hXyBn/gV8iV+fXaa68lBOZgQtC8tRN47Ngx7YBRq96ce68IukCDmp1zL1q0aEHKLkuz+/fvJzBnzpwSDJGEl156yURw3QP0qRmv/KRMDqOxWtZF1VCLI86ZbROSSi6asHLQ2iNJZ4xttGzZkvDBgwf7V07CHuFfQJpe3LVdu3bxjHVBEYlQpEiRIMU32duxYwfdjRdtbiku+sUXX5iQG2+80azyTJ8+PeIc5LYTTJbtIrgNhS1WrJhZXlH6ZlN3woQJthAG6XQw/4sc6I4uTUansy81hGDM0Z1Pnb8VtHRCT9SjHJifPHmSaDxqkcXGiRMnEAx+kjmDDEDIRc81MDEw8Nk3EGICeR09enTM8e7gwYPMHEOHDjXH+lMARPnX02GbKEg9yPmkSZP4SrwIv/32G2qKfZYjRNpi1apVMa1xuLBr1y77Oo0XPqKYmmTTD6iSvyaC91gLXTK5TvmQYc0ZBvTNjz/++IMPPghi4C5ePmPa6kAN8proECjLxo0b3333XQYEXSxJARiXmA7nzJkjCuEPchgz55TIjkZ9btiwYe7cuZs2bUp4juinn36aPXu2eUTfOuM+NmNy0ccee0xbN2hd/NG9e/d4r8fjAFHnDGT//v3RaFesWKH9KEOK0oqLJsyeD9BBXZsbQrK4qC4y6Yqpy0NpcPTo0UMb0RUrVrQ3iOKpxeZQroCKT5xevXrt3Lkzc+bM2vMUvFwUlChRgkAia4MuBQZRUcEjp9/tdEGbxrIkZCN79uxmvz0hF43Gr5ngXDTqK4fRM8FFE1aONuLs7VyBuiLcLHDErJwgPSJhARnNdCO6QIECMSkfA532z4MUHyxduvSJJ54YMWIEs0bEMTplfvLnos8//3zEue1pp5ZcO7oPP/ww8Zmzos7GbK1atWj0Sy65RJpblSpV7JWXgJ2uffv2kaRdfUpXr169gJk5T4AYi3BCI1EhdNTWWCH69ttvtTW6du1aY77Ipcj98ssvIqJw1AybJUMueu6A7t2pU6c8efIEGSweffRRojFPuMLp2w0aNEA077vvPiIw9KQsMwsXLtS0AS644IKrr766UKFCzMR33XUXM7e5gZAC8G6zZs2yZMkS8TX0Tw0Qwb6QEyINoTkb2Pq9Cwxn1atXj5x+yMqLeKKYymTTD0OGDNEBPOkE5ZLALKujXMCWcFiozDbIbkRAwNxatmxpOCcK37PPPstXxo0bhyqJ1jtlyhSf1yFpkThwHVGD30KKcuTI8f7773vTQRuAh/BpaOSLL76I2jR+/PjgpRCY9ipUqNC6dWuk5aGHHqpWrZq/jZb69evHzLl9dm7VqlUy/iGgZRp7gDHBgHbppZeaR+ZpNMt49DtjEJOLwtAiztYNPIc/qIp4r8fjALzLSItip8d04qIJs+eDd999N3L60TshBVxUN8qMQdcU4KOPPqI3kQhk0sybQdTiUaNG0R2M/eEgXBTqwmxIw4mN26cxAwIe660iG2puRglXeNGiRTNlyqRjtEG4aDROzQTnov5yGD0TXDRh5eggq3fXUeeroaAmxFs5QXpEwgKCbdu23X777RrWvIsOjJyukTAeSLxVq1b0XG0hqmjBuai2gocNG2anmVwu+umnnxIfRsrfdevWRSQGDhwYcSguPMdVVwG56K5du1D/ChcufPLkSeaUefPmBczMeQLti9om2b/88ktzEZTeqnO5MlO0fv16/jCDWNRRsLWhymickaaJQy56rqFp06ZBBotFixYxEhlrB8LRo0fRraXjojcTQRchUrw0AgUlM6gLejxw4ICs9l988cWLFy9OVlJ2Hv766y+YrT8X3b17d7169XyY0rmN9F7NYpKgESOWnZWYkHLpTxpjiqI/giSbGiSsPR3lAsaCiAFT/kUXXSQ7dT/99BNzubpksrgo+kHt2rXt3Z4uXbpkz57d0K1PPvmE+di1aG2jXbt2efPmhYA1tXDDDTegOdknmuClkJ+cOXOSPS8XZVoqUKCAfaHxvffeQ2lbtmxZwIJEnbrKly/fY489pkc6L1wU6uja5DT48ccfUdcqVarUpEkTO/MUv3379orDDAqxRCGeNGkSPFmGQEuXLh0vTSnQNhfVh2rVquXaec5IxOSiDz74IG2E5KA00MTIkpe3z5gxIxqHAzDG0jEplwlJJy6aMHs+UPrmhp5BCrgoBYmcfidNQEJcPmm8MB4sUGq1C4SCqw32hGrxwoULeRw0aJCJEISL0iVlZwVVj19vueUWV5YYIvxNpKId0hGyZs1qbO2YcDnakVVk1zU/CkWfoib1mJCL+tRMQC6aUA6jZ4KLJqwcMT1vww0YMIBA8ep4lROkR/gXkP5l5ghULxkldomxGK9XcrxQmxr3S8nloiKNZty20wzORXWGFonlK1WqVIk6oy61xNhCK7jOBQTkotGk7daxY8eWK1fO5agmBPM7HYQ52pwVgmoSYju7gqZqWQq9y7ZXtG3bNu2aZvwqbchFzzWkxhkxfds1NgneBeyAkC8y170gGeYuWrRo8INVdBhjDk44Iw7QzxZAMFxXYtIDzMRTp0713zln4kkP0phOyRokFHgdlIpY1j5sMMu6btbJhGZALsrEUKRIEVvX3Lp1q3cfiam9YMGCMY++Hz9+HC2Q/13hjzzyyG233eaNX7du3ZhcdPjw4YTbc5j0LdtkS0KIitvF+fjjj70r7gaofe+8844rUNtBxnZOjRo1bFd40F3R0QkTJngThMBD7EuWLOniomDBggU333zzmdJmvFz0xIkTkH+zGUJjEaFmzZr24sjgwYNVPzE5gG552RxA+qVxxqgdObsFdV/OvtYly6h33323iRPzvqh/9nxA98mfP/8111zjCpee7Toh6c9FEYmIc/TG5id79+5t2LBhwmPbnTp1gvObR3pHJMlIUkK1uHXr1jYXpa/xiIyZ+F4uisQSIpur0BWNCfZ5EPpykyZNEh4aEoVAmzcrL5T0mWeeMdZQ6aF58uSxL7DIVLKxoZqQi/rUjFd+UiaH0RRxUW2Dew/ZxoOLiwapnIceeohHmJidTr169Whcqe8+lZOwR/gXkNnE7jvM4/zqWtlZuXIlgc8++2zCspcpU8bmolo9se9R+3NRwvkbGmkfoxWZjznMxoM4baFChYwVpTp16mTKlAka6eqhwbmoTv3kzJmTITR4Ts4TwDO1sameJbtouiPKCL9u3bqvv/5ayyUMOPIjqqs3MnoEGD//sJAx2U57Lop4oTcgQ2jDq1evts3fGaAcrHFgDK9RR2g8dBsqkT7AnHTGL/OcpUgNF5UxPRcXHT16NIEpy4yWQl1clIlEerztMN0HdJsrr7zSXoiNhlw0PtB4mD+CrxynGAxSDRo0cK0fu3A2ctGAAu/DRRn0XDeZ5eAhCBdlJETvd+3zSANwdWrdWZo6dao3ESYV427egIkHTSjmsUDtNni5qKwm2uoRqmQkObcEDx06BE9wHUJDcSeQTh2TLcQcFlD6Id4iS+SBjLkiqDbMxqkBUnrHHXfwSqlSpbxcNOpY+7SP3mUkxEWhH6Ye+vTpg05v7LvItiqA2PTt2xfJhFSbnQ0UCClk9kkq8fysWbN++OGHKNnorHLXMWXKFB1F+eSTT5Qgky+cU/0XIhpxrmDBZxAzHZsvXLgwiq+IeuXKlSMeA7n+2fNHmzZtMmfO7Lp+TJYQjAsvvJD2QknQIEY2Is4dSxNNt/4+/fRTPcKZI85peYjKuHHjoB+IFmVPmAe0XtstJ1OnocdaloVmmF91K6F69ep6pGJ51IdQWpjjaAhoBqqeaklclHQUn95HPm+//XbTWNpqk6o9fPjwIUOGVKxY8e23306Y7c2bN+t+4xVXXNGlSxeozi233GKv1YqAGalGuuBX9qdpLCIQzbzy5JNPEkILJqwZr/ykTA6B/IuakQqVj/hwRbNITUcgAh3fVbR27dpRnwhqwjOExCT+iBEjglfOvn37+CLcyWQM3f2iiy6CyyWsHP8ekbCAzCb2oQC+SK261iaGDh3KK0EsNVSpUiXinBmWH1TdE7nuuuvQENSbtFVgWxqTZWPjhQUGziOkEX2ecYCGkwEqXvzggw8SZkCQK5eyZcuaUQ5SSiIvvviiK2bCTmdDSwapOZx/DkOXQj///PONGzeuWLGCv/lflEpOXOyfjAUH/eRFxuQ5jbko0qbtYNkC1h+uvvTTTz+ZQhrlTG5VVUf6wz7BHMIfR44coXtPnDiR0dPLRalwajXqLHS99dZbcmwVdTYTjNrHjMKv8nc3fvz4LxwQzhDGOCKCCpLL/WJyUS3sRZyTNoxxXyTBtDgZUwgaCV/UiMmATogZegwXRddkAmAU8zoSYI7UpXkb9Lc3HSQ07yQcO3aMGXfMmDHIs8tmvQGloNJoAnu5NOqsSDGd/Pzzz/QLqho9yd7MMTh8+PC8efP4lXRc2nm8tuMPPjdq1CiIvX0iiDosWrRoxDF/pwo0P5H55cuXU1FQDu8BDLiTFpu///574phpmLeIz6fJPx3ZXiFCffFuobtgk0aagwlswoQJtlop2KJoQCZnzJhBSzE4uHSOgMlG4zeN0v/3v/89ffp0Ks0c1Awu8PG4aMxJOjgXlVET4zBAkKl915CoGb1OnToJ0zQZi5xux9IgHheF6Eacs69mSRGVl/oxykpC0IKRWN47KlWqFEnykRAEqFAtW7bU3wi/bkDZQImPxDqrCW3WpYN4XJR+B4WIWS3pDXFRKgcS0rp1a9RW6IrrzDDaGOxUwgbdQoFTH0SD1HANGjZsaNYLGECkdEacO7S0FJ2XvymjThjyumgSqRmmxDipjWX4IbkiD7RyzZo133jjDYZc7QFKw0a9tlfK42UvIejy6OXeziLXl3ydAZ844hIR5+b/kiVL0Gu7du2aKVMmlU5nxelWxoKANNcgRDTqLPEg23yCTse8CQ3Qxi9CC8kUv6JEjIH0NV0RJ2PIGDVATjQH8d2mTZsyUMjoFMOvZhZVMqVAdPnEzTff3LZtW7vqaClopOymRpw91Tlz5gTJNqDj6P4LyJcvn32KXpg8eTI5YXCA8SIP9AKz+U930NJDkSJFRD6HDRumCxeUSIIUr2aiHvlJmRzC3sV+I87eKSMPo7eM3IqNfONARisijpkrzVnbt2+XM1WkThvj8YAM9+vXT5vP9H3oqGGAPpUj0LgPPPAA5Jmyw/ZdpzB8Kicav0cEKSCzCU1z//33M/DCOatWrerdAb7LQQAZ+X9HBmQ9BDHu378/ZdRyABlW5ciqM5SVr6BDysWUWkT8BMlHgNWzaDgE+JlnnqF01EkQMmyAYNiLLOQEaXcNdEE6nR1/2rRp9KzgeTivgL6kw7cCKrdRHalYXR8V6ESmYg35Ohe4KCrCfzvWhGVJcseOHcwWtl5FHaHhoRPbXJRq0hll/tC2qn4ND4IHAfNQuXLlGLwWLVqETlmhQgXDRWE49erVY8RhspRXZfBf//VfTCGy/mKOQyxevLh3796kE3GOAvZ2gJbfp08fTZYKSa5955hcFJpEoK5VfPrpp5paUMjMUUBmgocffrh8+fLwInigTmQxgJIBozxJD0CWrrjiijJlysj0nFxsRx27AiSYPXt2e+uMz5EfwhlGmY+ZpRhY/fNPp4UGMImiM1GxOXLkYFolP+Z0ExyeOn/hhReY6hgZSVPkBElmxpJfZqSd2Zp8MpqjRZGa/QlK1KRJE1oHFZCWYoIUt4zZdjRH1GEIhQoVYiJEI6E4xYsXN9yAurUbkXowFYLuguZBQ/MhBvcePXroeCe1QQPlzZuXOYYxS3dUZNSe/iun6vyhVXz7qmEQw8iGNKKjUBtUJjVA08v2IKOBVxQFBJi3mNf5Az2Jd8kSNS/l1T9Z/6YRqN7rr78eRWrLli0NGjSgcqKOUhtc4NUiLi66efPmmOd7g3PRW265xXiEF5Alfcvl7EH3f2juhGkKZAyFOOZP8bgoWhR6WMTZ/2EYh7dT22Z/IAhEtyAzrnCNDMYvnz8YB4hshDkmBg0aFLH2ygRmIpnNiMbnovKukXAoSA+YM7rHjx+HPsW77Bp1toLp48EnxG3bttmq3q5du+wVK5QPGKar/6KjkAepLLR7spYdk5s9ASbmdZ4RdVokBQdeYBqIqHfJyQdaW+RF9LaYK1n+UDXanZqcm1o1Z3TR8mEd8SqHMZCqo4FS4FCeJmbA8SH/+/btYwRLQcr+NRNTfmLCXw5TBnlNTEGhXEhYORSQhvNaDg8iNinrESdOnCA/NCgTLol7XydNJrLg3gEQTlv2KFEK5IGSkohufBw8eDAF9mxQG1xvpcZ6pQAfNseqQ8QEzc14iAC7Kh8BoBvSlN5bPGcQacxFtSnqulViQzzTnEvWOI6kLl261KyRi5oCH48dIYTx48ejOpuOzShWsWJFw0UPHz6so2so6xMnTmR0a968OWyECtdxXBcBiGkYQGp0yrLn5aLM1qizMAdz5QCNJOIcVLNfhIaZFVavsYRoEheFuWlDgykZfnXJJZdojYeCa0vH5qI6cGgWU5s1axbxGAawgXBC84yBDd1lYiZYu3atLlTQpeFR2rfUR3PmzAkB3rNnT9RpC63q3XHHHeYmT+bMmYsWLWo+ARey1zi7d+9O/LZt20bjtB2qNppNlixZzA0KCDxxaDiTiLcRRVpsOwFDhgyJJDmVRu3T9TBqr1evXtQno7xYfePGjRs2bGjeeuCBB1S04BBpzJMnT5s2bbQsLYOE8hhGBcYURYYCymgcWOvaDNUIbZau6Z9swqaJOgf/zIE0dItq1aqZrwcUePHDDh06THYwadIkMgynTQ0XZdpAQug1dqCaOOJxXIF+EAls3J9pieoaOnRozF/jcVFlSYsFWbNmLVGiRELnhy6ol3kvFWvP5OWXXw6SCEOE6drxcNttt1WqVMlWs5huq1SpYnZQ43HRqHOJS4sRGYyYtovOH9BYDODeoyvnBmLaLgoRIjVgajhvhwsbTNk+lupCnI1IYy66cuVK3XzdtWsXqtLWrVtt9QsBWrJkCWyEP1xndA2Yn9C9/juW99UQLlB7aFcuo3BiXOaMrg7cew2WTJkyJcO4KLPygAED0EchM3CMIkWK2NfxUXZ1od8soKJEQtiM6unDRe3byLpEZEyk6CaGzUUhWmi05jBev379iGDu03shhkY0EyIDHsaW6RtvvIF2/h8Lurkkj9jRJNsA9madDltq1R+yCteFaJnXddsEdqF1rJhtB3nLly+fbToC9oIWbh69jVi+fHmXCXjqVt5H1MtOnDjB3zly5HAdQqbh0ODNHsXChQu9txD9IdJoK/r6ln2B0CuKMrZsmCRTDuJRqFCh4Mn6N43chTdo0MBQlzFjxpikksVFa9eu3dYBrPjhhx+++OKLU8NFFy9eHPGcaF23bl3EOQroiqzdQhDv6LgNCXO8VXwfLhp11vi1Wx5xbJ+a0z5BQJePxLoapBuJAW0gXX/99f7WpNavXw9Vdnkubdq06aJFi8yjDxeVb4bU79gkF+c5F406N4fr169/Tl76CrloiLQF06I9T52HgFMsXbqUaZQJN4j1phBnEdKYi+qOqLkpqpO3ZmUaSULbljXhmFwUaiGLT8uXL88w801nL2SqbtSoUXag676oLA2glrne9Zosi6YbF61evfqIESNGjhzJRyFm3jMeyrMZXCZMmNChQwfzqw8X9RpXNPpoTPM25jgTAnbrrbdGHFMK8TI/btw4s0sptGrVihBzQqZx48YFChS414NXXnlFEfzt1OlwIPzWm4J2n+K1nSkFxadWI86NPvOrqxHlfcR7Fk7ew8TN4jmIk65M4inwyS7EbIWLLrooZ86c5tErik2aNImcfoCT5rZ9viVMNmHTSFOsUaOG1yllsrio64wuw11quOi0adMinjPthnO6hsSNGzfG5Kgx8dhjj1WuXDnerz5cFJpXpkwZhvTRo0fLYsott9wShP0K4pxevaFBgwauhZ54UPF9nMj99ddfZMnl9XTq1Kn2GBL15aIShuAn39IKTzzxBN81+//nJ37//ffnn38+of+Vsw5a4EjWtboQIeJh+PDhxor4+Qn0Rt3+jTgXgIPPQSHOCqQxF12yZMl/O55t0JKPHTu2Zs0a3Y6NOsfk+FsX0ONxUeLAJfQTOlDqrwSc25BvK5ePwb8hF3Xp1l7Io2DevHl16IK3bOMTyeKi5ghuTLrCcDZp0qQWLVrAc+SYzmdTQqbeS5Ysachz3bp1qQ3zWK5cuZtuusmnXP5cVFZqfGhevLaLOgeGabtevXrt3LnT5dfO1YjaXHW5SQAvvfRSJMnCezwuSnPcddddZkMsBfZd4pFGYB69ojhixIiI5cIE7o1s2LuFCZNN2DQQj8suuyzi2EXo2rWrffw1NVyUIcvQXRsBuaj8JTz99NN24IkTJ2ROyXUXbvny5RHHVkrCrEJiL7nkEu/mpEE8Lrp79+6CBQsOGDBAj4znMsshmvfcc8/d74vXXnsNEXUt6AiSKxeBjIkhQ4bkzJnTx/8Tn3ANDogH3XbhwoW2AYYiRYpQCfrbdQdMy1IZeRKHDMDPCxcujHZVunRp8n/ukbHzFps2bXriiSdyO6haterAgQPDw4QhQqQe/fv3Z9auVatWcu8Khfj7I425qAwxmQVmOV0FqO/y8rLdgcy1AyZg79VwCIZ+9RpLDGFDW1suN31nIxeNJm0RQEL279/vMo+WVlwUxbpatWrt27fXvqLO6PofkBs0aBBMD27wyy+/rFu3rlChQsYefdRxhFCgQAGfFRN/LiriEdPHhhCv7UaNGsWIbKyq+nNRXRa1NxUFXbCUaft4XDTqsHdjZRFC6LLvmhAp46InT56sX79+lixZ3n77bf6motDXbRsYCZNN2DRRhw+0bt1aNjkrV65sjmimhovGQ0AuSmoRjx/RaJJHDZchJagjgQ8++GDCr8uLkg/bicdFZdTUtiG5YcMG2iVHjhzU7axZs171BQI8b948UjAGhAy0FRnElvUNN9xgX4d2YcqUKV26dHEFSuZ94LL/LKO+KbBeEyJEiBAhQoRIJdKYi8pYsNk/OX78uFgl2j/Tf0x7wfv27UMp3LNnj61r6t6p7R49hBdyIvzYY4/ZgWcpF9WB1ZIlSw4ZMsT2BhZNOy4KD8yVK5c54BqEi4KnnnoKLgqDHTp0qMsKubZT7Dtpwpw5c2S5zp+LUs8R58Sj63UYy/z586Nx2k4eq42P9WgiLgrFkv7turkku7hy8xCPixoScujQobp160ZON5IUBCnjoqqEu+66C5rRoUMHaLPLjFnCZP2bhtSM5WHYtWTJGOU7g1z066+/1ha0K1zODF3nyXUsIsgNoscff9zfNk88LlqnTh3CXbs6tWrVigR27cvYfuGFF9pnyKPOscxs2bIVKVIk4cmXXbt28a2ZM2fG/JUMex2KkjHq+SsPLrvssnz58ulvV4mKFSt2wQUXhIe+QoQIESJEiIxHGnPR7777DiXY3JFAk+BRuvjBgwf3J0HhYOfOnfBVY1ZXGieaih69XhBD2KBiUdSyZ89uG7dEdyfQWKlNFhdt2LChl4vKF5lLUdu8eXMQ09633XYb70LnghRHV8jy5s17+PBhO1z7hy4zJ8nloohfxLGCay7dibT7+xZH07U9QbvwwgsvkAL1Y3PUJUuWdO/eXX/7c1FYou4/9O/f30Q4efJkkyZNZBg5ZtvJ15/honQfcXgToXnz5oTYfsnkFXrgwIF2OvXq1eMtNWs8Lmp7naa5S5QoUbZs2Xi1ERMp46JwCQiPj3uGhMn6Nw1iY5+DZRSKJFkVjsYReBf+/PNPcdGALgEDclG4Wf78+Y3ndINt27ZlzpzZZaUMvp0nTx5Dq2jEmB5odEC3V69ePt+Nx0VlRMq1GV6/fn3bjlRCIEWupRCtwthnhnfv3h2zcoYOHQqVjXnEkURatmzpYrP0LJecGzBixLwvSgo5cuSoUqVKwOKECBEiRIgQIdIQacxFURp0ZXTNmjXr168XpfReM3PdF0VbksmipUuXbtiwQd5HP//889CnS0LAKCKOj0E4GMro4sWLixcvHnEcYMgTo87I1a5d2/WinHy69lR5i8DZs2fbgTIeO2vWLLiT7qYOGzYs4vhrTpg9OS+uWbNmkLJs2rQp4lg3dYWLkl177bWIzfz586XUFi5c2HWsTnZ0jYNBpQZ90iOcTZfuBgwYgMo+cuRIxW/Tps2iRYtiGsqSVVsyD7Eh/ltvvfXOO++Yk7FRZ8+nQIEC4jxQqTfeeAPlmGTNsXPVp81mS5cuTYjZlNPmJIBIDx8+fMiQIRUrVjT0OGbbaYuMiqV/ffbZZ61atcqZM2e2bNkgDF9++WXUucVHhHbt2kFr33zzTTgkzLZgwYLwB2MF9+uvv4a2GUeRZDji+Jh2rS9UqlTJPpMMke7UqVPsxosDqpqUbSu+v//+OyEwK1PnXlGEpRDh8ccff+mll0aPHj158mSE2R5GEibr3zRw0bx58xquyyjEi++9954evQLvhRz8RDwn5GOChpC7cNciS0wgkGTGe3Oha9euUCZz/QE5J0HbV60s1k6cONH1og7o+h+urlatmrfjRx0OnCtXrsaNG5sQipAvX754fC8maDhq2xBpuN/tt9/OkGWcmzFZZMqUqWTJkl5PiTfccAPl8qaJqF988cW33XbbnRaQz+zZs8dzCRuPi65evTpy3hsQChEiRIgQIc4U0piLRh09T7dGhe3bt3sPYnltF/GWfYiXv8PLokFATT7xxBPSdCEkbdu2feaZZ/7xj3906dIFvjFu3LgyZcpEHGOb6LKrVq2KOpo3CjSaH+Hoc/379z9w4AC6HS+iBBOI0kYEQ/PQUBVepUqVI0eOEILelpCLzp07V6c6hWbNmsVT621AsUShbaCh6nYZavHYsWPhohAtJXvXXXctWbKE/FM6XfyDb8Ahp0yZgr6rOO3bt9dG/csvv6w48BOIBzpr1qxZtSMX86wgEqijni7AGw2PQrzFaQGJQ5/EcKBG/fr1U/rUG3yAqoPIKWatWrVk75fvDh48GFqocBrF7LPFbDtAYbUnTHjTpk3pOLC4iGPDRrfvyBJsQfucZpeYt9DpL7/88m7duiEbNWrUMOdvocr33HOPMtCwYUPj1jXq0Hs4AxIyY8YMmhtOkqxzjPRikzIUC/4G69Dud8TxKAsn94pi1CEnJUqUcFU7QiizqwmT3b17t0/TRJ3RhiqCuowZMwa6jhRBek22vQLvwgsvvFChQgWlnCdPHuTHNrVlAzkZP368TrqCevXq8RgzTYM9e/YgNt5eEHWs+PDdkSNHQgWRDZfhH23Ce7koBbePcLswb948eYEClSpVeu2118xCicBgXrFiRSocPj9ixAh6Is2UXKtytNF1110HHaVjUgk1a9a0t0npCzQQwuniorRjJNYpelKThHvhtRdtEI+LUhyocsIt6xAhQoQIESJEeiDtuWjU0bCPHj2K5pesjc1Tp07x1sGDB/k/yPnPEAYwH3iI9hmowDSvvX379rkcS3733XdpbuUY7hdzbyTq6PQbNmw4efJkKj8B1bG3TWAFPv7fyE+LFi2ID9X56KOPIGmTJk2C0KJV2/5Rlc66detSbCyR9oIAUMMBq1S1YWvPW7ZssSuHHkSC3tSIg5x499ziQcwT5gaZP3ToUMC3Ug8yCcmkaaCd0PhZs2bBGPv06VOkSBHXld2EiNk01IyGpv3791M0b8N5BT4jMXjw4HicimyvXLnyyy+/9C4K0HEgad5XkI1UXrynukj5448/piZTc6ly7969ixcv1kqBC7S1N+X//d//pXV8LOimHtRn6dKlfRw7hQgRIkSIECHSFenCRUOESAEGDRpk35w8s4DvwTmNCSgbS5cu9b9lGiI12L59e968eWMaNe3bt29MJnOOAe5Xp04duN+Zzsi5jz59+rhu4YYIESJEiBAhMhIhFw1xJvHbb78tWLDg+++///bbb0uUKOFjriaDMX/+/EgkMmTIEFf477//3rZt24zcJDzfIHs55nSxwZ49e7xuKs9VHD9+vH79+hs2bDjTGTmXMWfOnBYtWoRncDIAP/zww+jRowPaXj4rcPDgwVmzZg0dOnTJkiWhCKUJ9u/fP2HChDQ/b3Xy5MmFCxfGu0Z+VuCPP/74NQBkvT/q3HpwWaB0YdWqVW+//Xbqqxr9bcyYMcaKQYgQKUbIRUOcSbz88svmrtfYsWPPdHb+P3788UfdSXvggQdeeeUVBu5hw4a1adOmXr16IUNIV6A3ZM6cOWfOnE899dSoUaPeeuutIUOGNGnS5MknnzQuQM8H/P77788//7yPU9AQqcFHH330txpwzm08+uijkdMNhp/VWLp0aYMGDb7++uv77ruPcnXr1u1M5+jsBsSpRo0aUgMMoUo94Frdu3eXc+yAzrf+npD7LhlNuOSSS2R+P+I4HciTJ4+sYOhqPbj88ssjHhcJLlx22WXEWb58eSoz9uabb0Ycsx2pTCdEiJCLhjiT2LFjR7Vq1UqXLu3yKfp3wK5du9q3b1+uXLn8+fNfe+21jzzyyFk9n51FWLZsWaNGjZCKSy+9tHr16m3atDFuokKECJHxiHmNP3j8RYsW3X///Rs3bkzTTJ0ZHD16NFeuXLpj/Ouvv1KuWbNmpT7Z5NZwBiO9s3fixAnZ8EtDLirIYdVZPXd37dq1WLFihjp+/vnnIp+ynnDq1KkPP/wQyv3GG29Ek/yx+3PR4cOHP/zwwym2cGGwe/fuevXqeQ2wJ8TfXNpDZDxCLhoiRIgQIUKEiI2JEycuWbIkeHx03HP4OP3YsWMjp3uNTj2SW8MZjIxp0H/84x/pwUVbtWp1tnPRp59+2nZD4OKiwsCBA0eOHBmN4zr+74ZHH330TGchxN8LIRcNESJEiBAhQsTA2rVrs2fP7n/9zIVGjRrdeuut6ZajM4x//etfactFU1DDGYyMadCQi8ZDv379fvnlF/MYk4tu3rxZphb//lx09OjR5PBM5+IcBwLzzTffICorVqz49ttvjRtCcOjQodWrVy9ZsuSrr75yuW+Q7frPHfBHRt6KCgUiRIgQIUKEOAOAh+jk6vbt2ydOnLhw4UKvQZETJ04sXrx4zJgx/O/1fLN79260T35dunSpS4/nxQULFvDH999/P3bsWH83RaT8/vvvv/XWW6tWrdq3b58O0W3atKlo0aIojqNGjYJ92VasY3731KlTsj1WuXLlLxwYuz579uwxTpLtjy5fvpy88en9+/e7fkWdmjt3btS5O/3RRx9NmDCBRFxxyKcqZ+bMmd5ft2zZgh5GHt555x3YCJ/4woK8W1HhJsTfCpG8TMm58fjx4/WKHQHdjnDy7DXCp7JQjbSIreF5a3jDhg1KWf7GTp48abJHu5gXfRr38OHD8+bNGzduHPlxiVPMVvaBT4NCnikI5aJd7JZFpN90IH/XLpBtXnz99ddpEZtfRU/nonv37rVbKohjJxoXgZw+fTpVapM0m4vS12ig+fPnexvaJ9s0Cqp51PH1NXXqVNoxphUun9ZPW8TkogY2F6Uap02bRoiXVMBGXMbq41WgP+hELpPvdEMtrCCHM2bMIE3b/9zs2bMvuOACreYAuyZ37NhB9U6ePJnB0PUVV0dOcwNX5xhoFIZlWkH/g5UrV6qzI8MKQYr0B3Wrt37++efPPvvMfgu+mmGet0MuGiJEiBAhQmQoRowYccUVV4iEdOnS5bLLLrvkkkt4bNGihR0NjUHm01566aVChQqVKVMGnUw/oZB17Njxn//8JxrDokWL+OOOO+6Q6vD111+jgufNmxf9Hi0kV65cpBzPaW3U0QKvuuoq1Fb+GDBgAJFlKpy8lStXjsdHH320d+/eEEL/76LFtm3blvgUp7cDWARMqXr16t69GlK7+uqrR48eDZns3LkzGmqPHj3kJ5kyNmrUKHv27JdeeillIZrqKnfu3DZVWL9+fcmSJfv16wd/69OnD/HnzJkTdeyOUr1VqlThFSiZbgwCaNhTTz3FH5kyZfrwww9F7CkOGhghVLK/jks+KZFdIUCsBt7IV1544QW+e91115FPeyMODZu2mzVr1po1ax566KHixYubRvTWMNxS1fXcc88RAW62bNmym2++mRBkIGHjUttNmjR57bXXqNKsWbPWqVPH8JB4rewDb4NCzHr27Fm6dGnRibJly/JHjhw5aGg+dOedd1JAcjhlyhQqAR7rqsCqVatS5E8++QSZIQItYn61uShJderUKWfOnIMHD6aV7V2dmIB7X3/99SSLYt2gQQMExvwkLgrDufvuu0uUKCGThA8++KCJ4JNt6qpatWrEf+KJJ15++eVs2bLJUBCt+eWXX5oU/Fs/zRGQi9Kb8ufPTwfhsVSpUmJ98MO+ffsyjLj2in0qMB6QVSqNTscIoBD6lKqL2qDqkPNixYrxiISrrzFK0E91MVjiJPvG9PoOHTq0a9eO0aBhw4ZUcq9evaLxO/Lf+UD73wFr164VyYR/0jHpp4whR44cYbASBdXSFc0h8qlVOToaf2/cuFEO2BXzu+++y5g8h1w0RIgQIUKEyGigL6JXQQ/mz58fdbbOZAPTTP8HDhxAazRbB6h6/FqhQgXxH9RH2+/U+PHjeXz99df5m1fklQp+i1a3d+9e6O7w4cPj5aRx48aogOYR9mv2GKX/2SdIfb4bdc4K8miOdKLWQHh0rtXmotKnKZEJIUFCiKlHlGZUUjRdyLk20OBXRGjWrJl5pXLlyui15hHFF5LAF9HA9u/fDz0jPsoxhG3hwoXozfv27UMnRkEn3HZEgRJWsWLFeJXjgrdC+CLsUVtnyjkkipyrDlEBs2TJcu+99+rX7du3S1n3SZCWMlzUrhxxUZ/GhUvYRk27d+9ONHPV06eVfeBq0OPHj0NlYcIEPvLII6QAt9QCSseOHSOWOy5aikdjCRxaS4Z5V4/Qcn4tWLCg4f82F4UW0nDBHbEULlwYGqO/aWLeNT+Ji9JrUMejjv4tJrZ69WpF8Mk2Ojo1zGORIkUg+dQ8rakIEC2tm/i3fnogCBelMseMGaO6bd68OSFDhw6NOkcMeOvaa691cVGfCowHSjp16lTSMVwUkCYhl1566cCBAxmmyAAip3MEJg6/us7oIur9+vUzj1p5mTVrlk9HDlhX5yFoPgYTSKZ3BefYsWPa8JToRpNYq2YcesTSpUvNrv4333xj75qmN0IuGiJEiBAhQmQ0Xn31VXSsAQMGmBBxNqMjNm3a9NFHH/1PEoytUe3JQOR41CnWaJKG2qFDBz0SWRtW3mO9XqCbmp2TqONXyZz59DIl/++6qIswZcoUFxctX7482rwdB80JZkI0WIpCcufOnS1bNhPh4MGDLsUX9fSGG24wj3feeScRzDagmNgLL7zgKiwhhD/99NMmpFu3brSFfxUZeCvkjTfeKFGixH8s3H333cQZPHhw1LmdlS9fvq5du5r4mTNnrlSpkn+CLi4qUREXjcZpXBR3qnTixIkmG7AvouXKlUuLFz6t7IOYDXrTTTcRiL5rB0LbYJtwYz3CLohj5ISGa9mypR0fktyuXTvzaLgojLpOnTqwvoR5E6CXvNigQQNDa6Fh5ldx0RkzZpgQCYZuVybM9nvvvccjPdG8Tj3LJ8rkyZOjiVo/PRCEi5o1nWjSGpZtLujJJ5+0xxn/CvQBlebqkl9//TUh1IAJoeZdfd/FRRGwLFmy7Nixw1Rg//79iVC7dm1FiNeRQ8TEgQMHGEyWL19+9OjRb7/9dsOGDXv27FHLMjaKpppbFfxKiPdc+u+//87owU/Bu2EqEXLRECFChAgRIqPhIhhRhxTZWrIO5d7rAcq6Ipj7fmhy0rnRMhWCtqHtkSA56dy5M5FLly5tb1QKXqbk/92Y1MVlTwXdKBLrzDBcxVbiXVwU9SjiHBY1IX85iDo8dtasWTAxIhhSAZfjUY4ubBw+fPgiBz///LMSoeAJT6v6VEjjxo0LFCjgbaZXXnnFVV3wwJEjR6qqfRJMyEVjNu6WLVsIrFq1qjcnqKdR31b2QcwG5Sv2Br6BKSmqMK8QR85vdu7cyd/+DEdcFOGHM5t9m4DQRl+NGjW82zhe20XaZNY+oX+2wfvvvx9xzujaaUq0dJQ3YeunOYLfFxW++uorQu677z4T4q0Tnwr0ARmIyUXvueceE7Jw4UIXE3ZxUaQiU6ZM3gp8/PHHFSFeRw4REz/88IOueur8rbBu3bqoM07qUZJDLyMaj2b5T+BR79oGAtIbIRcNcRYDZWLq1KlSKc44jh8/PnfuXOa5jz/++OjRo5s2bXLd6Q/hxalTp1auXDls2LBJkyal08EbhubRo0e7rE18//33WtXOSMQrLHrwggULBg4ciMa5fv365CYbs4BnHL/99htKhn0SMiZ27do1c+bMtP306tWr/85WSQ38uSiUib+7d+/un8jSpUtRlEeMGPHBBx/YSnNMutKzZ8+rLJiDqceOHbvrrruk4N5///2GzkXjcFGf7wbhotqosbc0BaqCcKODJuSiUecUZf/+/du1a7dixQrti8rkT9RXhW3fvr3ZkaYg9erV88aJB2+FlCtX7qabbvJ/C9JO8Xv16gUry5w5c6lSpXwSTBkXhY1HTj/27IJPK/sgWVyUIY7BrUWLFmSmd+/eZvPwnXfe4W9+8vmQuCjExt6WDAjGGe1VXnDBBV27drVtHcXjouaQuU+2o3G46FtvvRVxjihHg7V+2iJlXNScEo/GqhOfCvRBmnBRXUj2+aK3Ix84cOCq0zFu3LggGT4fAIEU4dy6dSuz8P79+/XIhBJ1ruJra3Tt2rXGfJHLf/uGDRuWL18uQpth2nXIRUOclZBJDyb1mDNixoN5HdUKPQDFOmvWrJoqQida/vjjjz8aNmyImoIGgNKZK1eu4LsTwUEr0BYorHpEydAacMAto7RCvMJOnz4dvXDZsmXr1q1jTo2cfpwsCFwF/JsAQkWu7NtrLnzxxRey0WKrMqkEjasrl39nlwYG/lwU9sLf9evXj/c62hs6JaxA6oI0VH8uSv20smCfkEQdHzZs2MUXX8xbefPm1Tp6NBZT8v9uEC6qV4oUKeIqka6e9ujRQ48JuSiqUokSJUhcj8G56K5du7JkyVK4cOGTJ0+2bt163rx5sas4FrwVUqxYsQIFCvjYPRo1ahTZ3rRpkx7TiYtOmDCBQDmZjId4reyD4FwUJbhatWrwfG0z6rCrSN3EiRMjjrkanw+Ji27ZsuViB8EviwpHjx6lKWVbqHLlyuaodkIu6pPtaBwuKmrdp0+faIDWT3OkBxeNxq9AH6QJF9V1VvhPvK94O/L//M//tDodydrqP7ehfVFg7ot++eWXPOqqNkOHzuWCVatWyV6RGZoM6Av6CcqaMdkOuWiIswm2DXqmVZSJvwkXredAf8+dO/eWW25Jcy6a0P7+WQdUE3NWbdq0aXXr1j1x4kSaf2XRokWQPXnOEKRdZTAXjVlYlGAmZrP0uGfPnooVK7799tvJStlbQOHMCgwaHj1i9uzZrnA7V2qIVHJRVzFff/31c4OLojTAly666CKvUqjVCkU27jSCcNF4MArHoUOHkMyIZVzHy5T8vxuEi1IiKdOGNwoy7mq4pT8XPXDgAIylVq1aJkJwLgoefvhhfh07dmy5cuWS5dPSWyE61Uk3dMWcM2cOKUsXHzRokAlPJy5KCgQy9biy8euvv8o4lk8r+yA4F73xxhtz5cpl+qNN6pYvX87fZcuWdfVWGtF4FjH3RWfOnMkfV199dUB/Egykxi6xWdEzxrQSclGfbEfjcNERI0YQCCONJmr9IPlPLtKci/pXoA/ShItqI7pnz56uxOFCsiAVntFNFujdDAXLli0z6yNQTUJsTznQVF01R20wNHWPA3MFXfdOP/vss4xZZwm5aIizBhMnTnTZ8o53UiiDgfaTKVMmezD1jr+pBEOGfabo3ECRIkXsSSvDkCw1Pa0Qs7CVKlWqU6dOenzO21n+DnCJsVeVSQFcvezv7+rdIOF90dtuu43HmjVr2hr84MGDpQTLHKjhhBpzzAHXZAm5ThsKp06dKlGiBLRBj9q1kCtLwf+72s51nb/1NspDDz1EyMCBA+1o9erVK1mypFGG/Lno9OnTebS5KKSCEHPHyV+F3bBhA7/mzJmzc+fOiarnNMguqE0dZQypWLFiNjeg9+l8devWrW0uevz4cR4pponpreFp06ZFTreXIyefxsxVzMaF4VNjkdOPSJw8ebJJkya6EeDTyj6I2aDemVeWpciA2Y2RMGtljTbVwrE9S/7yyy8tWrQw8W07ujLihZAkzF7U2SWzLVHpbqox3uPPRf2zHY3DRWHyV155pbLq3/pRp7GSu8frDy06AK9L3miKuKh/BfogZVxUjl5MN4ftRJyzwXaf2rt3Lx1NLCjkoskCkqzbnrq2IxtmuiNKr1+3bh1tpPVNBge5EpVPl5UrV+pkr9LZvHmzbCBlTLbTnosiPYgy0k9vXL16NV3dG2fLli1rHHhN/DFo6qeYL4Y4b7F27drs2bO7ri39TbioTO3ZK99py0UZOJj5/A84nXWQEnCecNGYhf3pp58IfPjhh9P8czE7yxmHV4xTz0VHjx4dOd09wFnERfv27eva/pJ9S+NcQXZQwbXXXktkwmvXrm3UYrndq1+//rZt22bPnv3ggw/yeN1119H6TMGoF+JasqHqj0qVKi1evNg8Quo6deqkv6UItmvXDsUFkkxq/t9lTketvPDCC+GETPQSwlGjRhHnscceM59goi9YsGChQoWMKVc0pIsuuoiRU4/Q76xZs2bJksVcJJPRTt7S48cff8wjcT788MP169c/++yzOp49ZcoUlUW+OnzMmYoP+xwOjIk77riDt+wNf6q6QIECIiQIHkpzy5Ytb7rpJml4ZIyfkHwyiY4IDaBR4NgohbKH7K1hKjZTpkzU4QcffLBx48Y+ffrcd999Ecu0TLzG1cayiMfw4cOhW/Y5C59W9kHMBq1cuXIkyZ6zAMcmmggz6uzIkSNla7dNmzaLFi1CP9ah/YjjnANhZhyACcvPiqA6lJZ84sQJfYLXE27LoHPnzZvX+KL49ddfM2fOzKSsR22AT5w40cSXXdbnn38+SLbFRW3XSp9++im1YQ6F+rd+1PGd48pAKkGDqibNepCNsWPHRpLusgq6nl29enUTIsl/66239OhfgT7YtGkT6ZQoUcKEwG0ijgEtEyIb2rYzIalts2bNoq2nT59OiCwP58qVq3nz5uPGjaNHqL8ofsKOHMIFXQr9/PPPGT1WrFjB3/yvBU05cbF/Ms6NGIp1dpcQRif9bZwwpTfSmIsyamg7GIhwA5dJEiTeGHdyncFgADJvuU7vhIgHBlBNCUeOHGGCfPfddxle9RNdncmMEUdm9Gwwr6C0jRkzhgo3J0l48QsLpgmQWoUEtI+CKGtxBWEYP368fXLdgC7xpgOvOWkkRN66+CKZ/+WXX0inaNGiEccvPIFm5dvmoui1duY1EyCQJiSIThZ1Fh2pNz46YcIEe6w/fPjwvHnzGCi/+uore3Yk5Z49e5KN9u3bm29px8PLRenYU6dOnTx5sn1ewgD55+uvv/76O++8I5d6UWeekPaDDkrKATUncrhkyRLmP5QPiJDrArp/5WuWJTOffPLJpEmTjPCgKtEu1ID3dkHCorlAQWRpgznbJWyMmOQZyZw5c6bXRVvKpJ107KZ0cdG0khyabO7cuYjoggUL7HOVMQtLO0qlgKCaD6GqMjcbE44m89L/kMAZM2bQbb1H1+wCejsLlWYX0FSXHhNKFBVi3pXA8IorJGqNEvaLxnxXTDG2uSiRaT46nTmzlxAIgPRIe3SyuSjsZdq0aYR4j7ki3hIz/g/i9STNQStrf6BIkSIin+Yi31VXXaWdz6ijR2q/SLraiy++aPZIkZY8efKIk/Tv3x+pFhm79dZb6RfIld7SLWX/zCCZ5cqVIxEEDC22cePGpk7ozvny5VN/kQ9Gn++qCeQ3laahrekUlKtkyZKEUDrim+7JH6jpvNutW7cuXbpAtMwhUmSgRYsWyj/5+caB+FjEcceyf/9+eqhosHoW6pcsykDzGPegOsokdHfQoEExnT0iG1Do4E3GyPPMM8/ISAFtRLmMrFJL4jAAGvn4448bzV52VgiHVzdt2pQqgpPzSCdV3/HWMBg4cKA+RCkYKBhAcufOjabO2MKwHK9xqRNUdjn+iTi7r3PmzAnSyv6wG3Tz5s3a6dUSCaJrJveXX35Ztw0RbJgMw45MJ/C6ZkxkXiUF5MT45EQJUZ1EHM8iFJDaE18Sd6X4PtmjSkkWak13ZlK76667dNYAyYRhIqURx3qwLCcNHTpU1LFw4cIK8c+2uCh5oPaaOKDU9ijn3/rg/vvvTysuytjeqVMn5R+UKlWqR48etrFTWhYWp77JWEH7MiVdc801aj4UFbrJCy+8AJeWDL/22ms+FegPWlOeP6X8fP311zSoTABQCX379qUS5s+fX7ZsWeUHyZQYMG5LtqtUqSKXIcxozZo1o4MoNRIREWX0CNKRQ7iAxqLDt8LKlSuNPolI6PqowIBj+i+to8UmAzp7QOUn9UhjLorKK+NLyBYFQz2VTQ4TgYLRjWWjyctF6Wm8KzoactGEYIrS2uFzzz3HlFCmTBkZZSlevDgNwWjCNH/DDTcwLqDumBUB2qVjx47of1T1okWL+AMdUQ0B2dBtq4hzcswYkmF0JnFGYSPQMYGS1KdPH827UNBGjRqhFii1m2++2aSGXnjnnXcy0zB4MZwxxco2etTxol6vXj1mAuZseTaPOBYC0KqZusTuGJs++ugjxbe5KIPaU089pXEQBU6zLIVFcyLklVde8V9eRS1mpGbGkmqrATRHjhxalR87dizFJ0udO3cme3Xq1JF2izyTHxkn5P/eSSD/kdO5KHXboUOHdu3a0VIoEGSpV69edgbQiSkOJWUmpkWoFmZBwhnN7733Xql6pExOEgoG3yIF0tfGBUkZU6U+lU+/40PMB2SDSkO0EB4mLcq7YsUKssEkx4yLQkyIbSI4YdFcUKXJet5ll12mGtOCPTMQ+lO/fv3gKrR79uzZjS6VAmnnQ1SXZkd7o8zFRVMpOQI8nMkSnWnNmjVUL7nSDZx4hR05cqQW7JG0bg5QMiTPiLrSJDPoQBHnWhd6M2mKvRBBmYxZQG9nQQykKtGCZhEUDo9aRvvS7v5FY3CQXnjppZeKLTC3XX311VLRzMIEBUdJkjkcPsorNJ/Z84wpxoaLok/nz5+fqqDC0aSRt4QVTq6QEKndqlWtfxkuipZGmmJBtlvFaJLlM1oWsZHfFHNd6u8J1E1y6L1+RiXAZ0w4PZFKSMH1HokTVcSw4LUfJj91drIJv4tOE3DhkndJymwiJRfItn02cteuXUFsrggQ4CCX4oKDkQRt59ixY65wtD0GNFvboX5styXeGlZq1Iw0RSIEd3PCsEBqVIUrQf9W9kfABoV42+dRKYJXkaPJ0pZRUEwZGti/fz9F89Z/Qvhk25zRRb2hVr0LnfZbMVufFzNscyllSH0FJhdM0F7ftuhaVKBN40OkBowYVCZDh4tP0twMkgcPHjTr+DZohcMOAtpSTiukMRfVpqjPmcmdO3cSQZdiXVxUPJZJV0w15KJBoDv06FvGBrp8iKGMmt0VVK6I5SkYvhexLu7LdKE9JdeuXZsQ20Y2OgeKe5BT07SslmyvueaaBQsWMI8iDBUrViSkcePGiqMTF2YBuFmzZjzqkjodAA1SCvrEiRM3btzYvHnzTz/9NBrHtYDrjC5zLdonIbYnCeiNcV3gA7olE0bevHkjzko8kyU6fYsWLfgJcmibA9UJH9iFCfHaiPee0YVBQbHMI+Q84hxT0SMd55JLLjEzFmp9xDmNJmVCCwTBz+iOGTMG2mAUETkR0d8+lQ9QfSLO9sugQYOkA2kmRpVHudeIBhsh5LbbbgtYtHiIaRIDtgm7MI9QL6iCKUhypZ0XUbl09ciHi0ZTJzlRRwuBw5sLOdu3b4+cbhckZmF17ceOxugXOf3M6rvvvisSOHDgQOqfEum6Gt3Wp4DezqIrQ0WLFrWnpeHDh9vXhHywd+9eCmi3hSxJqoMI/HT55ZeLCdCRIeeusnjFWFw0T548bdq00cyn4ch2hecPlxmMaBIXpXHpBcqt7uMZd4KMUfaJOx1gq1ChQoYtAIf4O4AuX7p06QxQu0Oc1Yh5XzREiBBpizTmorr8iuKya9cu9NqtW7fabJPRf8mSJVu2bOEPFxdFaVjlAIUg5KLB4R0oFy9eTAh80oSIYNStW1eP6F6o+0abl022Dh06mPi6Sm4rkTCr+++/P2CWOnXqFDn9ojlcUTucOkzSq1cveJdxbiazdSY/Ug1tqiME4aLRJEMCtobdrVu3V199NWDmtX1EDZiQP//8s3jx4hDj/yRBl7ggbEZ5TchFoSKo8lBNk0j//v3tZqK2W7ZsaecErms8LiSXi8LQMmXKZM4jQAwMM/SvfPqjmKdJSrQtR44cdvow9osvvjhg0eIhJj2rVq2abSRDhjHNRkcKpD2adF/Fn4tGUyc5EMJ8+fJ17drVhGTOnLlSpUr+hfVy0XimIO6++24TMmPGDFdxvAWM2VlkCMc+0XfjjTe6HIv5QCfNjLnIP/74gyIjS8b0Mf3CGLCJJt3uC8JFr776ahNCahGPD0kfxOOituENDSmmMzZt2pS/jbjyRW2u2pffQpyrYHxYunQpAx0D7LPPPnumsxPi746Qi4YIkQFIYy6q47XmzqcsApu7akwD6CuyJuzioroTpbXqkIsGh3eg9NpM+/777yPOjRoTYm4cQSFkUe3JJ5+0kxUlM+cwmzdvHtz3tLaqjEl0QaRRluXtDNDWMolu9rU++eSTyOkmBIWAXPT/snfucTpV7f+/5ZxzCCE8IocUOql4UhHlHMqpb6kHITmlnF8OKWeGaJymqOQQIUJJRsjkzCSE5JRzEeLRPPv3/u3rNeu17H3PvvfM3DMG6/PHvGave+2111rXtda+PnutdV3wrlttiNb973//K1mypP/9SO4Cd+3aFbDP4j/rgtquE5KLRkZGQg7dJYjtLm7ryJNQrRLLRUUroIsRERHuwB4ene/mokD6U0+RoNhCQryb5oGg9Ox/Niyb6sCfixYtSh7FnJOm7W5nNkG5aDI1R/Uqk9j48eMD9gkl78b656LebgndDQw6WOTGRx55RC737t1bsWJFn60Dixcv1gfm6dOns2bNSora/s0soR+jcrclIS7q8F2ECLJly+azVglxUbcbSbXWKpty3RrLzOPzoQbXKeLi4sTTrMxy1+ScsMH1BSwZtMX/t3gDA4MkIMxcNDo6+js7sg0G2fnz5zdt2iSnYy3b1ON/cULt4KLiskid2DFc1D/8W+eVK1fWb6TDuWvcuHFiYjo++82bN0+txiAsXttu50MJISgXFc8E6vg+NsGMGTNat24N35DoUip/MrkoeP311wPx7u9ppgr76QfuAsXrjHck5ZBcVI4LJrT/XrY7qm20biSWiwLZ6gwqVKjgOH3n0fmJ4qIyeL2btmjRotJXQ63WBqVnln0yasiQIR07dqTajoCBSdN2n1zUSp7mWPaXHZ7St2/f/fv3O0IIpgUuCmS3vOjDoEGDIiIi/LcOtSlcuHCWLFlkmXrw4MF0V7p06SSoBtTUEfUhOVzUoW8e8M9FRUl4DfG/CrdgcLOBuYXpC6U1TlAMQmLChAnly5fPmTNn3rx5u3TpontJMDAwCCPCzEW///57DCB15kqCrgLsGInysteGctaEiYbpiekv/8uvsqyKEeZxTNxAkATrHNrQtm1bSJes/zgilQuQl3hj27Zt26xZs5iF/VcpKBft1KkTiRLw8LfffqtatSqGrCwlOUJLJ5+LHjhwIH369AULFrx8+XK7du0WLlzov/LuAqdNm0bK+PHjPe4KyUXlxFpCDkuh6N5UMwlc1LL9x0CHuBFepCIWend+Eriod9NiYmLaXg3leTIoPUNDihUrpoLdpzIXTY7mYLXQLcqRT9rkovKNv1GjRpa9LTyxXiL69evH7ZMmTWIOYX5g6q5VqxYtPXz48MiRIx1jJG1yUQmW+Nxzz/lutIGBgYGBgUEKIsxcVJwFqz11Fy5cEM6J4fvDDz98FwxHjhyRmKpuxMbGhrd6Nx6SYJ1LKGcVASIoF7W0KFX169d3R/7wQFAuivmLzSq270MPPZQ9e3a1pzHsXNSKDylGE8qVK+d2PukBd4FCGB577DFHTpiY2nIckovK8qMe5lsA1Uf5165dG7DdNTn20x47dkyYW2K5qAqNAKcS/gC/kr2v3p2fBC7q3TSPSrrpGe3NkSOHHrw+lbmolVTNEXHrAWbTJhelRUWLFk2XLt2cOXOEkSYKv/32G/eiQvSPLC3KroF3332XOjvcbKZNLkoPpE+fnvLd3lZnz57t86EGBgYGBgYG4UKYuaiscCp/GBI7VQ4RHT9+/Gg8VExVTG34KmbBUQ2yuAoRdQRFNHAjCdb53XffrXNRMW3dp/suXbpUuHDhDBkyVKlSJVFVcnNRisqXL5+43EQN+DVnzpxq069wYxWPOyEuKutvX331lZ6YEBfdsWNHwA5pRWUSVXl3gSinHDEaMmSISoTjNW/eXIXJGT58uDcXFXdQdKZODw4fPty0aVMo4sWLF+GKDkZ37tw5ekx6SdZmddc43ujatau+5PXiiy9y+3Eb3p2fBC7q3TSPSu7cudNBz2bNmkWKzkWhPYF4l1dWqnDRpGmOBNxTXJQ5LWD7+/VorJWSXDToYBFIqCQaKBGDEotatWpJ02TTCgMhb968lKaHVk+oLW41Tj4XlSA3+sE/by5qxftwoiH6px+GcMggnAYGBgYGBgZhR5i56Pnz5+XI6KZNm7Zt2yaEUy2TKrh9F+kw50X9Q8x33ZwVbqA8lFh2vJCA5kmFn2SXmgSflHDh999//+bNmx1R5idMmMBPEg3ZP4SLQtUUFRk4cCB2v6gBZrqEp3/33Xd37949fvx48ZPUvn37FStWwJEk5IzbC2vv3r1J79ixI+bvhx9+KD5sy5cvT2LQZVuJiJjQ3tGEIBEsHR41qWrABuZsREQEnLNChQqKv1l2nDp+HTRokEqZM2dOQAtjA2rWrBmwve/CEyZPnkxzSpUqJQGdAS2SR1StWpVy+vfvX6ZMmTVr1sivws/hVwycJUuWhBwaGOL9+vVTlxDOSpUqWT46H4IRsINKq3ux1yUCtXKXCvLnzx/QXAp5Ny0hrF69mruQoEr5+uuvScmYMeOyZcu4vVevXiVKlAjYrpUk+mgStN2KV+OXXnpJpcihwTx58gStWBI0h6oG7OidVJsqtW3bFnqWKVOmrVu3ii65G2vFR1fSVV08TuteZOXGRx99VKWI11yovkcDgw4WASmFCxdGxInaL6AgJ8nh3iqlc+fOpChdVRBBFCtWTKW41RglDNgRYlWev//+O2DvKvd5QF0+Hs2dO/fPP/9EPSxtQ4fKI350q1WrJpfiB1tqwlibOHEiIjB+Mg0MDAwMDK4JwsxFLduNpCxsCvbu3eteHjFcNCyYOXPmvffeKzRgzJgxZ8+e/fLLLx977DFS0qVL17dv319//ZWelICfAdtjB2wTWzlXrlyyNjJkyBBMUrH4//3vfzt22R09ehR7+vTp04mqlXBRDHoIGzYrdh5cRQ9HPmrUKKpHniJFiixatAh7FPohSxnYkbJsC//p0aOHWry1bLeft912myxnbdiwYdOmTZja0q4nn3zSvb+OzoFg+6/2rl27ZHVLjFQsVGUNo8DDhw+XwA+yKIRFrn6Cqws3w76HpooD2LJly8oK5MiRI8WvD6resmVL4XViGTvYGhxDGhiwA2YyiNRPEEKqJIKmi0K2BXoAGaN/qAlEFMmqlV6PzkcxGjduLBWAXfPTli1bxOkUaNas2bp16yhHnBWBhg0biheckE1zAJWDPkGPJT8FSsgZOlO+jARsR7g7d+786KOP+B8l/Oyzz5Kg7fDJsWPHIq+A7VUYbYdswwBlcQ9AGpltHNVLrOZY9u7i0qVLi962aNGCcST9BuvbvHlz0MZS+QcffFBaN2DAgJMnT65cubJOnTqSrVOnTjQHHaAzpYGwJvJA4cqUKSODF508d+6cu4GWa7A4atumTRvkm6gG6rKDKuuh2+GcjoVNy1bm6tWrS1tef/112SnjUOMffvhBCat9+/aUyaBWGti8eXO1Hu6Bzz//HOIasL9HMFMxD8hBd/rnnXfe4UWzYMEC6fwMGTL06dNHBjXslJ6RB1EZcrrdTRsYGBgYGBikAsLPRS3bpsRSxHLS11IM0g4gD9u3b1cLI5cvX4Z4uD8ZLF68WF+D8gm1R/fChQtwkqDBxLGYeaK6xIj08+kBpYKfeO/8VMDa/uCDD/xXOyTi4uJ4+oEDB3xWICjgpVu3bvXwGbNnz56gDh6xoWFWSMrPU2TLIs+KjY11rHVbSe38kAjZNJ+gB/QvF3S4+2hfiiJpmiMC0j+u7dq1y6e8UgIeg+WBBx5QTsuTAF06ArVZPSQSpcY+wdNRkiTcCNelH5K2PmxgYGBgYGAQFqQIFzW4MVC7dm33qlFIBPVdlMqAjJUsWTIoDTYw8MANrzkxMTE1atS41rUwMDAwMDAwMPj/MFzU4Cr8/vvvS5cuPXXq1GeffaafUvOPa8hFt2/fvnr16r/++qtDhw69evVK/QoYXKe44TVn5cqVW7duPXPmzEMPPWSi5BmExKFDhyZOnOg4tZFyuHjxYmRkpIoGd73jwIEDc+bMuda1CA+uXLnyzTffJMqXfmoiJiZm+vTpfjYrIRG3a/Ekgydu2LABYymZ5cTFxa1fv37s2LEzZszwv8Ek1fDrr79e23UFhbRTE4OUgOGiBlehbt26cowqY8aMiXX8I3jllVe4fcyYMWGvmzeY08XhbcD2BKu71jQw8MANrzmbNm0KxKNZs2bXujoG1wH+7//+L3C18/AUhThvuwFW7H/44Qc54+0+RH3d4dKlS127dhXvEipCdVqDOHUPuYFL/KtnzZrVp1M0D1DCoEGDChUqFAjm8D+xRTVt2nT+/Plz587NlClT9uzZT5w4kczqhQsQPzneH9Th/M1ZE4OUg+GiBlfhyy+/LFu2bKVKlZLwBfHs2bO9evUqWLAgln3JkiX79+/vHWEy7MBy4s1Uu3btoEcuDQwSwo2tOVeuXMHiKVKkyGuvvSaetAxueCTWG5Mj/4oVK+rXr59qIb5/++23hg0bfv7556nzuCTDT69KMOEbgIsKoFtpmYtGREQ0a9Ys5KmKuLi41q1b+4/RHRISLTmZXJT6KJfvM2fOrFevXprysSKanBYYYNqpiUEKwXBRAwMDAwODGwdRUVHR0dH+82PKd+jQIeXqc8NAj+ubEIJGzb1+ITGo0ywXvVZIKBB6olCoUCE9dnRag0cg7pu2JgYpBMNFDQwMDAwMbhBs3rw5c+bMidrY8vzzz//73/9OsRrdIJg4cSIGcchshoveDEg+Fz1+/DglGC56fdXkesG5c+e2b9/+/fffr1u3bufOnfrW9BMnTmzcuDE6OnrDhg1BA0PQ21u3bt20aVPIKPFhhOGiBgYGBgYG1wDYBBJg6aeffpo6dSoE0nGe7dKlS1999ZVlH3ibNGmSHr1m3759n3766ccff7x3716VSDmFCxfGbpswYcIPP/ygx2jl/88++ywyMnL16tUqkk1cXNybb75J/ooVK/5ggxT56eDBg3qEZ8GpU6eWL19OIVQVc8fxKykLFiyw7AhPZJs2bZr/Te9nz551eNW6ePHil19++dFHH1GNI0eO+NkfG7I/pcnYWNOnT585c+auXbvchcTGxvJQHn3o0CEJ2GvZkWwzZMhAR0kveXh10rkojVq8eDH94I6tZYXqTMuWPj998MEH8+fPD5ohKIIKWuBTQKdPnyZbVFQU+pYoLkqLFi5cOHnyZMxch41LW2iFJCImpKMiS5G4Y8cOUlauXOko0I9AyePoXrL9+eefNJYGKh2mKxhK7oBS3IsmTJkyZfPmzY6fpLsYStzoCC0WlIuiOT73I6BCc+fOlUjaolF6ZDU0f+3atYx3lPDo0aPu24M28OTJk8uWLbPsrqZ6M2bMUNpLq6ElyIVudBTFsPr222/Rljlz5jiUIbEMkA780Ibb05UfxfPobcNFEwWmHcY+SiJ/wfr162X+ZCKVFPRB/nHPgb/88ov8xO2pVmfDRQ0MDAwMDFIPmAUDBw4sXbo0BhYW9vPPP58pUyZxLlWlShXxX7Jly5a2bdvmyZMHCwxLInv27PxavXp1y7YsO3fu3LFjx4kTJzZt2jRdunR9+/aVkrHkypUrR87/+7//69+/P2afZdv6Xbp0gR1hKK9YsYJ/nnjiCYmFi23aoUMH8t955539bWAsYgSLA5433nhD1ZlCRo0aVblyZWxWTOR69erlzp37k08+kV/hFbQic+bMt99+OzUvW7bsXXfdRQk5c+YM6YKVSjZp0oR79bVEmDb9A0ngn3fffZeiPNy6+OlPAWbWI488Ar/C0ho9enSuXLloiDLZQe/evRs1akQT1q1bV758+fbt21t2RG7Kv/XWWylQekkP0eyA4qJQr7x585YpUwYBcS8F+uxMAQzh0UcfRaDwCuRFT5LTuyc9BO1fQLAyVOjTTz+lBG655557fHJR1KZ58+bvv/9+t27dMmbMWLduXWEUv/7666uvvpojRw7KQZq1a9euVKlSvnz5uKQT9uzZg4zuv//+ggULkjJgwACfAoX3Dho06O677ybxiy++kJ7v06dPyZIl5ZMBPS/+iuBIDBZ5ov4R4fz588i3ZcuWdCytRkx16tRRvuvogQIFCsAYN23ahH4WLVpUD8vs5qL0s2gI+b07Ki4uDhVyjDvELb8yHJAOQ5sUejJDhgw9e/YUCp1QA5HUs88+mz59ehRm1apVFStWfPDBB7NkyYIU0LolS5aUKlUK0sscQor+xWfbtm3FixcfPHjwjh076HDUY968eepX/wwQQT/55JP0EqqFGqNUb775pvzkU/G8e9tw0UQBhReSyThiPkdV1qxZc/r0aRRPKKh800Rj0RYu4a7qXgYFiWvXrjVc1MDAwMDA4EYG/Ofpp5/GwMIu/+qrr/773/9CkypUqEDKCy+8QAaMZoxILmEpUM3Dhw937949IiLCsvkS5qMqCuucbJhxconlx6W+R3fhwoWkjBgxQi4x7rn84IMP5FL8gqg9uvAZbP3XXnvNwUWHDBmSLVu2kydPyiVmDQyKPLNnz5YUuAHWPEZn69atZREPWkIGbH3vruBGLFHHvlY6AZqtLhs0aOC9xBqyP8GZM2fy58//9ttvq7uw0rDgySbrh1hv5FdG8NatW1955RWVGWPa/x5dWC48R1yFSYfDc1SekJ35008/IXeYm1yKK2wq7x28xFvQfgTELRAqFVwEW1b6MCQXhZvpbpDpZO5Sh5AvXbokjmfbtGkjrUZekCh6qX79+sjFso1g6CjdIo6IQgqUvqWrxcOqcNELFy7QY3ny5CHlxRdfRGFg8jQWUxvGCw1zcNFWrVpRH3UpQQToE8teGUYxIHjy0969e/mJkaW318FF6StIIE0IupLphmPcCaAKJMrypgBpksJ49GigZYclIxG2OWzYMFk6hmCLZ3hGsWx2gKKQ8vjjj6vCqTDiVpdFihSBECod888Au3TpQs4NGzbIJRrFpXJdGVLxQva24aL+cfHiRSZ/+KR7BwEjSxY81e4AYa2MLJWHFIgoqmW4qIGBgYGBwQ2Orl27YmBNmTJFpWATyOKP7K3Fgpd1Dz3OEBYedhsm6ZV4QGzI9swzz0gGNxfFtMXilD1yVry927lzZ1Wg2yb+5JNPdC6KaZIlSxbMXz0PVI08GK/KOXPOnDkzZcqkMsiJOD8nJ2HajpxwDMxoxRyWLl2q708OipD9KStRjv2ccKFAfBAyMd/Hjx+vfo2MjFT/J4qLli1bVqWIHO+880659NOZdIVOk6TyHTt29H60t6CtUAL666+/aOOrr76qlyk0w5uLQsOKFi0aFRWldHLNmjVCjdSWbyGN+k7UqlWrkvLjjz+qlEaNGpGi9sqGFCigtoqLCh5++GFSsMUdlZTlRKVR8+fP51LnjRs3bqxevbrU58SJE7fddluPHj3Ur7fccst9992nLoPu0YXFOTZFeyDouCtfvjw9qafAKPLnz68vtwZtILIT5qlShL8xe+jZ4LE5cuRQl4jgwQcfVJdPPvkkt6j9sf4ZYN++fXPnzs0olsvBgwdzo9JDK5Tihextw0X949ixY0z+8MmzZ8/u3Llzx44dTDjyfQHJCk1VWsqvpKgFarmXv4wLw0UNDAwMDAxucHTr1g0DyxHA/dFHHyVxyZIlVgIWGOwoXbp0z7rw8ssvSwY3F7W0YCSQ2LZt25JBUY6gNvFnn32mc9EZM2ZwOXDgQEcTSpUqpdMJh8UJrdI5mAfc/n6kc+AP+hqRN0L2Z4kSJaDxih0JZs6cqZg8Rphss4T1uU+EJoqLOhg4xWbLlk3+D9mZsGX+0Wmwf3gI2goloFmzZgXsk8Z6gX7Oi8p6Ml3tVku1/9nNRflVX0yz4qPaKomHFCiQNupcVDLoSz0C2fGrxPriiy/C/D0apXqSW8aPHy/aqH5Nvu8i97iDMwTi9+HraNOmDenDhw+Xy6ANdHNRy9Y6fdnTig/HqiLH/M+GZTPeuXPnQoP5VVHKRDFA1V2wIBrFjfqe85Azg3dvGy7qHwwxJv/o6GjZfyvYunWrZUtZLpmjLPusB9m4lM8cdDKy27JlC/8bLmqQCFy4cOGvq5HYmHLe2Lhxo7czxpiYmOnTp3vvGkoCYmNjv//++4R+ZRbzCFvKC3jhwoUrV67UXRRgfPjvJYarnjnsrQuJPXv2TJs27f3339+xY0cqP/rGBnP0p59+6j//r7/+6jCDwoKLFy9iOan3fdrBgQMH5syZk8oPPX78+Ndff7148eLTp0+H9xaPiYIZgHfz/PnzmeIczCQ1EdTUfumll0iMioqyErDAZHHPI05sUC4KMCxeeeWVcePG0XVkULtP/XBR2XKpL1wIZBclbwG5DCMXPX/+fI0aNWQRrH79+n7Gi3d/Mu7g8PyvLzJb9jZdEosXLy6XCxYsyJIlCyn58uVzEDAHF120aFHpqyEGX0JcVLGCkJ0pS3ZQ1pBNDoqEBG2FElC/fv24hJHqpfnhouKGx/urgX8uqo7FhhwgVjK4aIUKFUqUKOFRYcs2JxgCffv23b9//y233KIzvZTgonQgKfpCpeC9994jXX1sSj4XlSPEgrNnzw4ZMqRjx47r1q2TdVElo0QxQCZSNLZ169YoQ//+/R2C8zMzePS2oybHjh1zDL3Jkyf7qeTNgN9++00I5+7du5nrhFWCU6dOWfbxXVka3bx5s3JfJPwTjSIdWmEZLmqQKEycOFFOCoEcOXKUKVMmf/78/K1Xr96ECRNEpZIGJhGm6cDV54XckHlt7dq1SX6QG7wqihQpoh8VULh06dL48eMLFSrEK8r964kTJxo2bIj5Mnv2bF6fxYoVUxsPGITM5vfdd5/0lb5nyY0mTZpItrvuuuudd94JGUQ7vBgzZkyvXr0wj7CNqIO40DRIJphhH3nkEZ9msWXrv1hO4f0QC3fiVS2WLiIOY8nJBJURXzWpGYgC8wJVL1euHGYEao/l4fDdkuRbvCcK+KecOhNUqlRJdzabmghqanfq1IlE8cYZ1BZs1aoViR4fqtxcFMsPkx0TVg7mydbNRHFR2XTXvHlzx7PkYJh4SLLCykUt27odO3as+LzJkyePMD0PePfnP//8I/5v9uzZo2eQw2m8SVUKGapXry7qIYfxBA4uGhMT0/ZqyO7fkFw0ZGdCtAK2kyTv9rrhLWgrlIBk/Y0+18v0w0WnTZsWuHpvsxvh4qL6ALGSwUWLFi2aPn1695k6BYwoekY5nk0FLiryYuJy5JRzvz179pTLMHJRuhFLicEul0nmokyhVatWff311+VDv2h4oriod287aoIQHUPP/+6JGx6yLqp7nP7xxx+5lMPn9KTsywXMYNu2beMfup3MmEnr16/fa0PSSeF/t+vplIDhotc3IGDyyuRlICkQsDp16pDCzJvYtRd9wfCDDz4IyUUjIiKaNWsWXrYmhpSbizL1MxczPfGr28RkgEE27r77brVc0Lt373z58umu2NRRk2zZssmr2o2DBw/yfpJsHmuzKQQGfyB+hwxyhFfr9TdIDkT6PrmoFW8opMSmIMhPWLho8jdB6CVIe1OTi3bv3j1z5szKoTwDnKHnWJNJwi3eEwXv44cffvjrr79m1kIlxGHMtQrxF9TUbtSoEXaY+HcJagvKmkOfPn0cpWE9yDqwm4sKnVCxH5LARRcsWCCf5xwPrVmzZkA7dBdGLqoODfKOEzEF/UCpI2R/yudIx/eLdevWkYg5a9mzhDLT586dK76L1ep6MvfoKlYQsjPXrl3LP2XKlHGM8WPHjgWNDaPgLWgrlICGDh3K5UsvveQu05uLypvrsccec6TTmWozbbi4qC5QKxlcVFbdZ86c6cgmM/PSpUv5ddiwYSo9Fbjon3/+KbaH3ktA/EgrxhguLoo65ciRo3bt2urXJHPRhx56iMGi1DWxXDRkb5s9uv7BhMl4XLNmjdrTB9UkRQ/9BfOU7SGxsbFCUyV8VFAkZ1nLPwwXve4h+47UPGXZywLly5cnsXHjxv7LiYqK0kNjOWyR1IHs8fAwO0aPHh3UxJwyZYrjfcn4yZAhQ4MGDVQKY48JLmvWrORkcg9afo8ePWSiD7hcXKQCIPb6fG0QRvg3iwUp9/ITXynJ5KK8QpS3zLCUENSATjns3r07YMcd0RMfeeSR/PnzJ/QVNlG3JDRR9O7d+/jx4+qSWSJXrlwMuvCebvAJt6nN1J0vXz61FhdUCVetWkUik5vONg8fPty0aVMxPmThVN9SIXEvFEURy09t+cMQCbh2BjrmfzqqWLFipKxfv17lwaCBnulzdRi5qO7aJy4ujqfDzbwLCdmfEyZMIEOtWrX0uyIiItKnTy/rzFCa+fPnq59kfVL5ti1SpEjAtcXXT1usq1lByM7kERLgRP/icO7cORrisY5nhRK0FUpAsl05c+bMepCbzp076x+7gwISRclkGzJkiEpkVDZv3ly55A0LF3UI1EoGFx0zZoy0XbfR586dK49r166dzo4QWUDbyG0lwEURvf9tYjt37nR/A5JtWUOHDtUTGzZsyKOV4oWLi8rxYJ2LQikDml8ony9BcUSEAijllO8Xauu+FUrxQva24aL+ISucvB1E1cWRmJwRZSLdunXrli1bxD0VI1QCkJ49e5Y34FENspUXRsD//t1xJQfh56K8DjHimV9oxsaNG/UXv8KuXbs22VCji7GxyYXUWRq+3gG/cnBRy+ZUJDIN+TzuuHnzZt5AunGT+lz0119/feqpp/jrwUVltdZtYsoHb+7VE6tUqULnqImV6Y/ZsGPHjgHbXaE6vq/ADJg3b145+uIuLRWAsWW4aArhRuKivEhKlSqVhC18HiWkMhcVA9ex2NKzZ08SEzrTm6hbEpoo3CdIJdRh4lsQBoipjb2uZumBAweicmo/CyZCwN7H4TjUKgto2bNnh3ZOnjwZgo00t23bJr9yGbC97/ACpbu4VzaoP/fcc3v27Pn888/FW+n999/PtM/LmrcwzDZLlixMlbya5S0gtE1fIoPckg3TWb2Xx48fD2VStcWayZgxI7xObU4R77j58+cP2RU//fQTOWFoKoUpXUVctGwruWvXrsnsT7qiWrVq6dKlU0Qdc61kyZL9+vWTSyiNzg3gcnS+YlPCAXhBMHw8FvDlo4nuDVUmH15GylgP2ZkITl5DVatWHTRoEEOVtwM2pXcPeAvaj4CgPaSUK1cOE445EBGIP5snnnhi8eLFHo+WtTsAw4TejxgxokKFCjobEZ6sD8DHH3+cFD3cpTAxtXAdUqDqlo8++kilVKxYMXC1e16BxBdV3pjpeXEWlTt37jZt2owaNapZs2YNGjSQZ/Xq1YufZFhh2cN40QTezpjyUjLdSwZ6WJV/7tw58gRCHQJSgAaQuXz58noiyoY4sE9UPWEOGHKooncDjx07JoaNSkHcsslLN3XEJa90ID3P/6jEsmXLaCZNlpNZ9L8MvVOnTgXs7fHeDZHv/vKJH+VHk8XTb/v27VesWIHOh1S8kL3tsyYGAmGS33//fWxs7Lp16/ifv/K9VYK46D9B09wlXPfnRRnGshwszZB/1FQuOHnypFr8VfthsITcS8NutmDgRlAuKptt+OnQoUM/aJCYtohJpfB6RmSFCxcO2A70SBHypnNRJo6ZM2eSopx9K6DHjvVDNJ6JLDIycs6cOd4R4Rx3YWAxkVHhxHJR+SznNijFeOUdI5fCReVYfMCOoO3IP3HiRHgCU3/yuSiqK+YOhUyaNEmPRrBv3z5M548//lj/HIsI6HmawJQtclEHJ6Q06VL+ur/KM1KQCy/CadOmqS/ilj19L1y4EFMVq8LxSUKCR0me2bNnI1ndmYECfYXcp0yZovbL6aBY+nDBggVqu1TSQOvmz58vNUSdKFPtTCZxx44dpKxcudJ9I12xdu1auvfLL78MGtIN3Uaa9AAvcvnU6uaiQcVhpQoX5SUtAhLPAVJhx1Clb1WKyAjrGbswYG+9IzEJDq6ClqBzUR6N3Yk6Bd0aEBa5S5R2Xcmt+L2LdevWTf4tCXFRB9AK7Dzvc24pBzG1Maax2tu1a/fMM88wB4qHQ8teeBFnNqBp06b6eh2a0LJlS3WaAH6liKhlH4C87bbbRHtl0QnzLleuXEJrhwwZgm6L0QkXkm/nzPMBe60VlWAmGTt2rJxXz5EjB/nVKhmlQd3hNoMHD8Z8b9y48YkTJ+QnVEW2tATsyIfbbchpEdCpUyePoIvYvup85uuvvy7DAXMWRsTTmaAo8IUXXgi5IOndnwIYSI8ePWB9tHTAgAE1atTQd2nCRYsUKcIIZU4YOXIk5FNfXoZ+yLsDypeQ3ywGlJIatjjTy6ZNm+goSYFWqW+jHp2pukXkKOTQz5kRD0Fj1vsREJ1Mz4hq8brs0KHDm2++iSJ1795dTVNBwVw9fPhw8UIcsBe15s2bJz/98ssvQjZAvXr1qCQaBasUAkMPQO/Pnz8PkxEuh/hkLdpboBSLBOX4fenSpd9///1du3bJChuoXLkyL3Qh/zxRQr8E7GVAte5Kh1Om7CyjMjxO6Zh4xyGdrmjRogXDRHwmYSkx1pgxhFpnzZoV8YmpwL1iR4X8toVcsLXksEbAjsKqggPLo6HECO6tt96i25966in1/k2ogdHR0UrHuAU7CmFJhQEcG9ZBd4nbM9CwYUNSEJl8rQAMN167UHqROyYB76ZatWrJr5BD7/VerCzpRobPokWLqIBEc2ViYQiEVDyP3iZzompiYNmGhGy+Faxfv17Culq2lsrxUQGzUNCtFtc9Fz1z5ows7IoDUrRwzZo1ussBMbZQJgcX5fXJJSbySQ3X0MPhdYSgXFQ+FvIq5ZX5n//8h/+ZKZYtWyZTLaJhdiZl9OjR/M+0yKsuYO9/69+/vziiUFy0Z8+eefPmFdNEBXyDwwwaNEimY317DNM0OZmdMXB52WTOnFm9kLzBLRKSOwlcVILCURl3mQEt3LZwUdU55NcZGv+TwthLJhfldqbLPHny8P5mCpATR+KlHTMIetyxY0deIRiX9H/fvn3lLux+el5e5P1tqD1RmCC8mZDUe++9V6BAASopVI1Xcp8+fSRmGmNKLHVejfLpEYaG3cPrmb7irYCxLt8R0AGJ6kYPY4QVLVpUNp6hALqph2WAIYW9S9/CRakqLw+VARlxO3bAuHHjsCRy5syp64B/0MOYCOKbhLkCK0EWqQL2F4Q9e/ZUqVKF8mW7Go/T70VLy5YtS0/Cz2kjlgSKqu+koH+4HQWGx6LhYiDqXNRDHFbKc1HYr8hOQFfDyVFC3g1igEJFLJs3QgsZgIH4pdQlS5bI3jbsS/QEQSe2AkFLUFwUzsPjUCc6BIXEZFE3hkvuvBel1fpWQCv+eBuqmPxb/HBRepuhGhERkYQmhAVqCyKUmJkzsQfvGem8W4N+EZDIcvr8xqsWq07ttkL5sRf1DJi57igmQUHhFJXSu5ZktqFKzKgOkpYQ/PcnDaf5bnosY/Cff/5hOsKYc29OO3LkSMgwp4lCyM5kGvT/SdfyIWg/QLUoRM6JHT9+3L8lRk4Ujy4Ki//5ZA4Qn2BuoXD3lw5sdMwY/SstY8Rb7dEc8sASk18rHoQI5ItkigIF07/XIDv3koMfMDOjaeoSy9Nx6tUbSehtA2/Qe7wdUCHH+GVsImLGdeocBPWJMHNRWRR179RX2L9//3d2KFUHF2XU6X6fDPzDzUVl9wgWrUQNYpIVW1b3H8jkW6FCBXXpdnchXBRbPDIyUj+GNHLkSMt+VzF/yQkQ3R6tWLGifj4BngN9Cvla+vHHHzHQ5f8kcFHxMvfQQw85MmMxB7Q1E8VFeZzYtYsWLVKZly5dinlt2WQyOVwU4wlbP2Dv/IHbHD58uHv37mLv9u7dG3qscooPZP2DqNs3BiMF8qlsRPH5fs899zC5MI9gMEF65XMj9gqMSw7SQGNq1KihCpEQAoqTIy8uedbQoUMpB+nAxAJXLxQjaz3SOn1IBpitZU9k1apVUx/pT506lS1btsyZMyfKYFLA+CtUqBCF8zixqmkyjDpXrlyohLiYwgSBjvIUZYsIA9Fd540YMYKU1157TRUL0+vSpYvKIFuvdS7qLY6U5qJVq1aNiYlBiGiLCJH6SAbZJidcVCDUUW3rlVGQnD267hKEi9Lt7du3l88ZMqzq1KkjGcIod/FcGnAFJuEtELC3nib/lpBclLnxqaeeIg9Tlgoin8oI6prFIMkw/XmD4XoU6KhRo0L6AzcwMHAgzFx0/fr18Bns7wMHDmAl7N69W//OASmKjo7etWsX/zi4KDeuXr2a/OvWrcNEw/Iwi6I+IVz0ueeee++999544w0503LffffFxsaqPAMGDJDtECrlrbfeGjNmjLpMiIsq496KJ0K67xDZ96JzUSxs3QeGuGXz/swGwaDOarkjCVx07NixJGJZOjLLkRtVH8VFgcRiprYq89NPPy2btZK/RxciJEuU+qfWn3/+OX369LDHK/EYMmRIID7GusDNRVu0aEGHq1soWdZO1VkROZixatUqdcs///xTtGjRqKgoddeaNWvEXpcxJQ2sWbOmumX27NkB7WywRLfTFw02btxYvXp1eeiUKVOKFSt2RYOcXlORuBMLt08LWbnVz8PIViK1Val8+fL6cSzL/qoqJ2GEVwwbNiygxey24o/eKS4aUhwpzUX1vX+ysI/CyEYahO7goo4jpinHRcuWLatSRI1Vj4VR7lu3bg3Y27Ec6XJWPBDMPUxib/HmorxievXq1aRJE7h0wPa64VhuTR1cj6Z2WobpzxsM151AJ06cmOT3oIHBzYwwc1E5I6pOikqAGhU/A3aKWSzehHUuioms8qt7QwYTMxAIF4UWQskiIyM///xzt3+OU6dOiUc1kcX//ve/kiVL6hufEuKiuu+iDRs26OskVjAXdv+zYdncYO7cueL2wDu0zH/+858FCxaoyyRwUeGcjzzyiCPz+++/Tzp8WC51LipBwJV9v3PnTqoq+5qSz0WD0hhEky5dumdd0J0curmobMp136WIitul3q5duwL29mz3XWJwSwP1OBbiblF9ZXjxxRd1FwgOvPDCC/ny5XMXPnr06KR1l3//irIQevDgwUD8tmcdEhxPTAE6zXFox+G7KKQ4UtN3EROgHDSSxGvIRd3OP7Nlyyb/h1HuikA6NsLExsYGJZxJuMXnedEDBw6I/5IePXokthXJxyuvvMKj9W+CBsmB6c8bDNedQNPUpkcDg+sIYeai0dHR39mRbf7444/z589v2rRJTsdaNh3if3U+XueimInk2bhxoywLHD9+XH5NKAikgY6g50XdeP311wPxsUwg/A0bNtR/9c9FsT5VipuLWvYC1JAhQzp27Lhu3To9XNWiRYtKX42tW7d+9dVXcEjdYdWcOXOEacjBY0crgpqY3377bSDYmTFZ6WrZsqVc6lwUwly2bFlZT5aGqPgWKcRFxW2AY4ehAw4uKr7j3n77bY9b3FxUNqN6hH4OyUUrVKhQokSJhG6nnx9++GGPKiUWifX1L+vzjhAU4L333gvYAQygK5ATx/lhBxcNKY5U9qMra4yyQzhNcVG15T6Mcr906ZK4LXGcdZSwitDy5N/ik4ta8XEs9G0CqQAmyV69ehUsWDBnzpwlS5ZEEO4PiAb+YfrzBoMRqIHBTYUwc9Hvv/8eCqHOJUrQVRAXFydRXvbaEMfxgPkl6OFs2esbXicBNyp8clE6EwOdyf3y5cvt2rVbuHCh/mu4uCgiLlasmKqMzkVjYmLaXo39+/eLe6GE4A5wEtTElAjRNM2RWXb4jBs3Ti51LmrZ7oICtksnKgYJVBuJU4iLymlbb6+nDi4qcf+ELScENxeVdnm4Bg3JRYsWLYqqJHR4u0iRIvny5QuLawpBYrmoHBYtVKiQoxw539izZ8+jR48G7KOP+q8OLhpSHKnMRVu2bEmieKpMm1w0vHKXsAS6rwsrfq+yHiYhybf456Igb968jpiTBgYGBgYGBqmDMHNRcRas9mReuHBBOOc///yDIeWO2vKdHfEFporlp0cbxwzlp6ARBQwc8MlFQbNmzcg5adKkcuXKOTwEhoWLHjt2LEeOHHroZJ2LBgW0YcPVkFWvmjVr8r/bp0hCJqbEVXNsBq5WrRqJu3btksuLFy/qXBROLg5asbD1gGApxEWx+wNXxy4XbNu2TX3xdXBRyoETQgbcB25V+HU3F0WIpDz22GOOW/76668lS5ZYPrhojRo1uNRDHQiEC8lR2xUrVjh+nTdvXtJiIieWi8qnB7deSYA79Ba+lDVr1oAWSs5ycdGQ4khlLkqfo5ziNjBtctHwyl1iPDicfPTr14/EyMjI5N+SKC5aqFAh3YWygYGBgYGBQaohzFwUmxhTWMWhwhbkUkyo48ePH42HpAvbhK9iU35nR18VOgpnWLVqFSk+Pbnf5BC7PKEA8Tp27NgRsCOPuU00WSbS/akkgYvOmjUrYMfvUhkeeughUlRENT8QmzhR50VBVFSUw06VVVDdoRHqRB7dbpZdnZB5nXZKMwN2lBH/1dYRlMag0gE7iJlO+CHPTZs2VWtN4n1Hv0uigdeqVUv/UjN8+HAVbNDNRaFqOXPmJHHIkCEqEZLTvHlzifQbkouOGTNGaJsecnPu3LniQ0L8YBUpUkR3BB8dHe29l9gDieWiVnxUnqFDh+rlNGzYsHjx4uLDRiK46H50hcFSbbkMKQ63EOPi4tauXZvMYKpWMC6KrubNmxdaJZdy8HXKlCkqwwMPPECKCq8iS9/JOeLoLiEkFw2v3Pfs2cO4e/XVV/VE6G6uXLmUt2REoK+C+rlFwT8X5R1EGx3LrQYGBgYGBgapgzBzUWwCOTK6adOmbdu2CeF0u65xnBcV/7pcYmzFxsbKRt8ff/zRuNINCdmO6LbLE4IY8e6tib179ya9Y8eOkJYPP/yQnp80aVLADhai8siKZbVq1RylffTRR3L59ddfc5kxY0ZyIv1evXpJoG0o4rfffuuzRd5ctG/fvlJPRzoVrlKlSrly5S5duiQp/fv3z5o1608//aTyfPPNNw4O8Mcff8DMGzdurBclEXECVzunTRTEZSslOxRYzgRmz54d5j958mT6vFSpUipI/X//+1/IMxlOnTqlbhEXuAE7sPWgQYMmTpz4zDPPvPLKKyqDbFzUXc5a8SuE8uEgIiJixIgRFSpUmD59uvy6evXqgO3cSOVHQKRAw+QSHRCHLrlz54YXjRo1qlmzZg0aNBCSRuskBCi05I033oAykefhhx9OciQ0iVKrHwcSBo46qRTRNPWtAVINby9QoIBa+YRgwygg1XLJ/CP7BegK+vPMmTNyQJTE8ePHy13e4pDDunny5FF1ePPNN0mBNAqlTzIkKLnur4uRAttUh1dlszHdQitiYmLatWsn3pLfeustOW8vmoxKMHMuWbIkUWHcBO4SIGOk6N6JZSWZHpPd2mGXO0yYEaoOdKxcuVKfTAAqR0pUVJT/WxQSmijozPbt2yu1ofmMkRkzZiStCQYGBgYGBgbJRJi5qGXb90ImBXv37nUfMXLHdDl58iRmt7oLI8zt1t/AgZEjR1aqVElYR86cOTt16rR+/XrvW2bOnClRNB1ATLfddpssBG3YsGH27NnCRiBU77zzDrLAdJZnZciQoU+fPjt37hwwYECWLFlIKV26tIo8KbE3AEYqeTATA/axTz9biAUJcVFqBd/OlSuX8IFhw4ZhieoZzp8/36JFi6eeegrS1aVLF3jp2rVr5afDhw+TIg0sWLAgNr1SvM6dO6vlpoMHD8I3YDjShDvvvLNnz556UCI/wMqXRTlhd2oB07J3ybZs2TJ9+vTyK6xeMZ8vvvhC6JasWEZGRir9h9gjFPkJ4oQ4ZI10165dGNaKqUJT1QlPBDF8+HCJ/gKKFy8+b948+YmxKVuX06VLB7ll3EFFypQpI7LmLhmtJ06cgPSSRyTerVs3fTyiLcKOpJyXX345aauFv/zyi2y8BPXq1YP8Hzt2bODAgeKlBkWdO3cuYoVPUjdSYNRqczI54SolSpRAmt27d0fuKuKLgGkECSpR/vDDD9Aq+hbiITL1EMfChQtr1aol6W3bthVFEldYYNq0aUlorEJsbCzVQM3q1KmDWtavXx+KpZ/OvXLlitAwGVw//vgjRJomdO3aVWqIAshiMvowadKkJNTBUQKdo5QWqrZv3z5mYOHMoHnz5rK1IVxyVxgxYsQ999wzfvx4hjbcW49wa8UvIOtcNOQtVqiJ4rHHHpMZibmCzkex9c9VBgYGBgYGBqmM8HNRyzaFz549i5miFqn8APMIHosRjPUZRs8oBjqw2j/44IOgPyEy2GPye37Pnj36Lr4DBw54xxcNL3gWJAT7Ut/Umqbw999/b926NbFGPGQA6STqYF5cXBy30P9Jlum5c+cgPwl9FTp9+jQNcW+PTE1cvnx5+/btHktzBw8elL3WdELQGJKJEsepU6cgYMuXL09yhRWoz/79+/XN1Q4gcYaSyE5fKhfAXXfs2CHnS5OGJJcQXrnzjli/fj18261mDOGg++Q9bgkJ+nPz5s1Lly5laCTkncvAwMDAwMAg1ZAiXNQgbQLTrWTJkteWPBgYXL+AzdapU8ecHTAwMDAwMDAwCAsMF73xsX379tWrV//1118dOnTo1avXta6OgcF1iSNHjjz//PP6mr+BwTXEnDlzdM9bKYq4uLj169ePHTt2xowZyTwvHRLHjx+fO3fuyJEjo6OjzXefa4itW7fqe0BiYmKmT58e9j1rhw4dmjhx4h9//KFSLl68+MUXX7j9jCQTKVR//6ClfnxMXnOk5sRiYCAwXPQGB+9y8aoK/vWvf5lTuAYGScOlS5fS7MZvg5sNv/76K1N61qxZU2GnMY+Qo+9QxEyZMmXPnj3lXNyvXr26cePGW7ZsqVOnjvjrSqEHGXhg8uTJxYsXD2jO1YEcv1deGMIF8ZEuXt9Pnz7dunVr8UPhiHqVfKRQ/f1g1apVEnZOBRVLs0jNicXAQMFw0RsfzPLMgLVr1z548OC1rouBgYGBQXIRFxeH1Z6cGLP+wVNKliwp/8+cObNevXqJ8gThH2fPnoXoirvsv/76q379+rBf+elm+AyUQm1MWrFTpkxxcNGIiIhmzZr5P+Pj87krVqxA0LGxsSpFvCQmn4s6KpDY+ocXv/zyy3XBRVNzYjEwUDBc1MDAwMDAwCA4ChUqpIcjTjlIIDE3CYmKioqOjk6FClxDpFAbk1ysI+h0EpDke90RmJMAyO2IESOSU0J4ISGy0j4XNTC4JjBc1MDAwMDAwCAIjh8/LoGmUuFZr732mpuEbN68OXPmzDf2AbYUamNyik0mF504cSK3J+3e5HPRP//8s1SpUmlqcc9wUYPUxLlz57Zv3/7999+vW7fO4TT+xIkTGzdujI6O3rBhgyPOwi+//LLpakg4t1SA4aIGBgYGBgapCuyAH+KhYpwePHhQUpQFgKGA0RAVFfXtt99CC8+cOaNKuHLlyldffaVH5fHI7IGLFy+uXbt20qRJX3755dGjR/WfqMncuXMlXrRU7NChQ96lUcJnn302a9YsGuV29HXq1Knly5dHRkZCkLCWVDrFqiC3U6dOlWeRTiGFCxcmccKECXq3nDx5ctmyZZZ9ivubb76ZMWOGithEh2CBTZ482R059p9//qFnePqcOXP0Eyu7du36QYM0XLB///7k9CEVdoh4y5YtkvLzzz9LSkJt5B8aYtle0z799NMFCxYoBz/8o9cW7Nu3Ty5jYmK8i/UAfAm50ApM1aBclHRHhwQV9+effy4xoqVKqtr0M2ZxXFzc/Pnzv/jiC2UEIwtVbUvjohjQCxcuRJR0mv+Gk+eJJ56ghFdeeYX0HTt2eNTfsk9Izps3D61jSLoPSVI3IfOo7uzZs2ms/5DjtJSaU38688KFC4qL8r+ub2pMxcbGOnrMz9ORLOlo9erVqx1R3+hhEkXVafhHH33EpfIHJr6UEBZy1+9yTywCSpg5c+aUKVMcobyl5hSO8lNm0Nhpem1DjgipA53GDEYTkCx96H6oQUI4e/YsgkZz5C9Yv369bFlnMpEU5hb5h1GpboS4fnc1dKGkKAwXNTAwMDAwSFWsXLnytttuwzxt0qTJ3r17JREzrlmzZuXLl8c+tmxahVXdt2/fPXv2YDLmzJkTEmXZNKNjx4758uXjdmW2JpTZGzDDsmXLTpw4EZLWrVs3KETPnj3FDMVm7d+/f4cOHcSG7m+DbB6lwRweeOAByCH2TePGjSlZ/YRNOWrUqMqVK1MrbNZ69erlzp1bjoYCiqXwcuXKCf+RZ1EBeJSeSG2xrp599tn06dM/+uijq1atqlix4oMPPpglS5aMGTNiSC1ZsqRUqVIw5+zZs5Py9ddfqwps27atePHigwcPhpwMHDgwc+bMMBD5id6WJVmAFU4Kxj3/9+vXzw+F8+jD06dPd+7cmaKorWTm6f/5z3/0pWZ3G7H4q1atKmyKTsuUKVO6dOm4LFCgwI8//mjZpJE8UmGhH/ANWYokc0LFercCa7VkyZJjxoyJjo7u0aMHfai4KERo0KBBd999NylwSG9xQ5bo3ltvvZXMIkeIyrhx48R5D6Ti+eefl5oL761WrRr/v/HGG6pY4aIff/wx9QnEo2XLlpcuXfLTcHQADSHl3//+N0/nEQnV/9y5cy+//HKDBg2WLVs2Y8aMe+65hybASOVXEkUKVJiHFi1atEiRIlzSq358QMLMq1SpQrsY6chCvrMIF0U3PvjgA2nFe++9pzyB7d69m0o2b96civl5OmOqS5cu9957LyJbsWIF/zADCFnlEb1795ZbEBPTBU276667uKxbty55eAopZcqUIaV69epSYNCJBZw/f759+/aIgJELF0Ub69Spo6rBgxo1agSlZAAyd5HTo1tCjgjaToa8efOKoykSqbYMAehuyG43sOwNEUIy4Z8MGXj+mjVr6HlmVKGgBw4csOyhyhTKpURoJzP/b9y48aQG/19ekgnDRQ0MDAwMDFIbw4cPx97CKNQTGzZsOH/+fPk/MjLy9ttvV8tHElLFsj97QzjhWrrJmFBmD2CXUIIsMApGjBhBCsRMpfz8889i1vtpUcGCBSEG8j+mKsa0+mnIkCHZsmXDuJFLrCLoKCXPnj1b5RGW4thT6k7cvn07KbDNYcOGyUIWJrI4isf0l2UfrDFSHn/8cXUXrBWCpC4x06F2qrv4RxbTMLW57NWr1zvvvOOnySH7EA6sW96WvSTu2PbsaCPy7du3LymFChWCSiFi7EiYAClwErVglSdPHkXJBDRQUbKE+jMooIvcCGlRKfINQrgo5izMqnLlyg4u5yFuVFHt0cXGPXr0KISHFPJAepcuXdqkSZPDhw9Dw+QrgJuLkjMmJubChQtwS2kpnMdnw4XpqT26CdW/Ro0a0EWlA1SmWLFiWbNmlS9BgMzcQluGDh2KXpGzadOmsnTv3Z/QZog0RFGlyP4CfY/uM888I+RcpdCiO+644/jx4z6fjry4VMdiSeeStqsCn3vuOVJg+wwZEcRDDz0kKail3ttwEiuBiQW0atWqTZs26hI2S4b333/fste6+X/nzp3y09atW1955RXvzgk5Iqin+K9iSFIfueWWW24pXLiwd8kGlj0SGfII1L3If/78eVntVHOIsNZffvnFsr8C8L90eOrDcFEDAwMDA4PUBpZfzpw5saHV5sY///wTe0vZEN26dUuXLh3mnVyeOnVK+ZUFsmqkTEbvzEFRvnx5uI2ewqPz589PsZs2bZIU/1z0r7/+Imfjxo2VcQ89ln8OHjyYJUuWF198Uc9PVWWtT20R9MlF5UEwT5WCER+wA1HoN8JYcuTIoS7hNg8++KC6fPLJJ7mFDlcp+/fvh9LQ/EWLFj322GM+3cCG7ENxoKpb3lu2bPHmooA6kNKiRQuVQn0kKsnHH38sKfAWByUTdfIoNiHUrl37rrvu0lOE5+h7dF999VWdy3mI27qaiwrefvttUgYMGOB49CeffBKUi8oCtUC+NSBf2dcdsuEOLhq0/kIOo6Ki9DxjxowhkQrIpUiqZs2aKsPs2bMdtQ2KYcOGkU0Pkcpgd3BR2AIp9957r0qBoqtH+3n6smXL0NgFCxbIpXwW6dy5s8rPnKArDJBvHMOHD1cp48aNI2X06NEqxTGxzJ8/n0t95/nGjRurV68uS/QimvHjx6tfdTUICj8jQnRg3bp1KkWWcHWGbBAUx44dY8ivXbsWldu5c+eOHTuYfmWQMt0JTVVjh19JkU8VciMpyJfbmZ/16TGlYbiogYGBgYHBNcBbb72FgdWrVy+5nDZtmm5Kip0HoYqIiHBTo9KlS+vGmXdmNzBQ9O15Cm3atNGt1USti8rS01NPPaWfQQIzZswgfeDAgY78pUqVIl2MWisZXNSyV8b0ZU8rPp6kCj/zPxuWzRXhIRBIB1uw7LAfJGbOnFntmvaGnz5MGhcVaTqWmHr37k3im2++KZfh4qLYoAF7r7ie6D4v2rZtW8e6YkLitoJxUam8LDvrkO3Qbi6q+y6Ki4uTs6+SmDQu6qh/69atuXQ4GYZxkZgtWzZRFbekfLp0uvvuu/Ply6enBPVdJBuh1U7yVq1aKWLp8+lqpO/bt08aCOVWv7q5qCza6x6GP/zwQ1LefvttleKYWF588cUCBQok1FKUR/Zjd+zY0SdR9M9FdR2QFV21ZG2QEA4dOsSQR7Fl/61AvlEy9cmlfP28fPky2biUr2b79++XX/V7U438Gy5qkHbBG2j9+vWy2ezIkSPXujo3I5jCQh40EiCsNWvWIK+UrlIScO7cuZkzZ6bERz5mapTTO9zinDlzUtML6J49e6A077//vu60I2hiWgPG5TfffCPfaFMOGzduTDtOWbEJsKHz5MkjYQ+ffPJJtXdO0LNnz4CNChUq6KsElstk9M7sxrJly8ipLxUK3nvvPdJffvlluUwUF0XNhAFmyJChR48easFT1sRIceSXQ3TTp0+Xy5Tgovp5p7Nnzw4ZMgSjmc6RdVGHKyYYSMWKFR2Lch7w04dh5KIfffQRiWp5OVxcdOXKlWRr166dnuiHiyYkbivcXBTUrFmTRFnqDwsXFR7oFnTmzJlJl3PCSeOiWPzp06eHjuqJQbnovHnz1MrnxYsXUWl9X6XPp69evRo9GTdu3OLFix0645+LklOlOCYWJpMSJUp4tBf+nCVLFm6BflOaR05B8rkoBLj01dC3Ot/kQHWFRu7evRulOnr0qFyeOnWKX3fu3ClLo5s3b1bui8Q32L59+zZs2MCgxpZjcMmLUm2QSWkYLmqQRsGk3LRp0/nz5/P64TWTPXt2dcTfIBXA5F68eHE/34DB4MGDxeEBRlgq1M0/9u/fjxbJAZjwflI9cuRIy5YtsTm8Nw7x0IC9u8x9eCMlMGbMmF69evEKF9mJpRU0MU0BMt+1a9dcuXJRPT/WTNKATYZRFfCxxS41ge1IlTAlMRruv/9+d4bly5djpJLnlltu0TvHzUU9MrshO/oKFSrkSJdTZ9BauUwUF7VsvgerEV878Dr5AMT8EHCdjAVyBlJ97UpRLhodHV2sWDGYj1wG5aIYauXLlye9SJEiupvfhOCnD8PIRWW3pFpeDhcXFW9ADRo00BP9cFErAXFbKcBFRVXEaA4LFxUFcHOYwoUL0xxxzJM0LiqLq8xmemJQLorRL1sDtm3bNmvWLP18qZ+nUyaNQrXEY7ZoY9i5aNGiRXnNeb+/IDByHhi0bt3aI6cVDi5K3dpeDf3A9k0OWRcFSmQ//vgjl1BNy/7gK/tyQUxMDIrHP26X41b8ll2mTT3oS8rBcFGDNApeJCVLlpT/eVnWq1fPe/XJIOzAbvDJRQFcIg1yUcte65D9XWHhovruR0ouUKCANxfF2uDdnDqR7nhzBOK3HW7fvr1GjRryEdSdmMwH+TxKl1i0aNEiJbioXlsxUtMUFxXnH8WLF8dAhJHqP6kwBpcvX+7Xrx/ZChYsqCwDh8nondkNaIPYjg4+9u6775KoOJt/Lsr8rLswkeqJJ5UFCxbwv+NEohW/2KWOoqUcF8WuypEjR+3atdWvbi6K6ValShXMMvHq6VgnDAo/fRhGLipH+5Rrq3Bx0fXr14sG6toSkot6iNtKAS7KxEXTxOdKWLioeHPVd7Ra9pROObRFLpPGRSkka9asZBNvpYKE4otOmjQpYK9102rHlpCQT5cd/iqYTQpxUXqeS2wwR81FQKi3+twzd+7c7Nmzk9k7EIjZo5uiOHHiBEN+zZo1ajgzp5GinztgrpOvLbGxsTpNBequkydPygqqCgKUojBc1CCNolChQqkTYN0gISQq3Ll4fUiDXNQK32vs/PnzHTp00FOCrk1dKzRr1kw3yDwSkwmfKpFYiGkVXi4aFRWlHwlzG75pAY0bN6ZWefLkkW1UCl27dlWOZy374BbZlJtNh+55Zw6KJk2akGfo0KF6YsOGDaElKmADfMMnF6UmnTp1Upf79+8PxLuTvXDhQrFixbjU9/BjD8FY4EsqRdyEOrhTq1atAlcv5ieBi86aNYv/dS4qc4IesqVPnz6y5Hj27Fn5euVnL3fIPpRVsiJFiiiTbsmSJYGrfdK42xiUi9arV69UqVKKg8mSmvjAtOyTCOnSpcuQIYNHsUHBtCaeaXU/uvL5gBJUioPLeYjbst0Uc6nHPkkOF4XI5c2bt1+/fj4bPm3atIBrT7ij/tu2bUufPn2uXLn0b9zi4lUx6iSfF5XN5/o6p3y2oFscOXk6ykblq1Sp4vgp5NMlSo3iovKr2l1vhYmLypud0aSTGWinFEt/qo8jlj3fBq52ju2GnxFhuGiSwbwqpz1FgkwX8FI5I0qHb926Fb2S/QuXL1+WAKQS00W27Kop8eeff+ZSHeZPaYSfi8KqmZU2bNiABbBx48ag78Jdu3ZtsqFPVUwo27dvpzvWrVvH+y91trQZpE2gNo5Z2CD1YbioA9jNDqM8TXHRMmXKuGln0MTkQKL5hbFAhbBz0c2bN2fOnFlnFGmTi/70008B2yWpI516KvvbsvunUqVK6lJ2xau1F+/MQXHkyJH8+fMXKFBAFYKZAqNj4Ks8GCs8pXz58iFbwSiA0ig+DAm85ZZbFi1aJJcwIgxuho8KJzB+/PiCBQvq3oMkqsrnn3+uFyscpmPHjtyIbmBOia8d3Z/KP//8I7vldV4hzmyl/K+//pr/M2bMuGzZMvhGr169ZLf2J598IhFTMVfKlSunrA7xIgufDHkwxE8fCjF799139+zZQxOYUQP2qjXMXIilu43CRSEbam5ZuXJllixZ9L2Ism31ueee2717N4+jWKHQ8AQxLt3FJtQKcdqUI0cOeAXEj3oiKWEgUA7h88K6VYxHb3E/+uijUhOs3lmzZpECMQtc7cFVMGHCBNJfeukllSKfZnQvPsjrgQceUOdRQzb8m2++4bJy5cpYmPAcWbV21F/1j9qOju1KnurVq6uOEuXXV/DE62/Tpk0T6kkBxi29IUI/derUmTNnJEYOiai9vl6qekBCpOgI+XQJ2Uo/SEjhRo0acXn//fcz72GEk6Fdu3aBq6O8DBgwIKA5S1NP19eHHRMLyiPkP3fu3G3atBk1alSzZs0aNGggC2hwUf2diDiyZcsW0rtHyBEhUwFyVLeId9/kb+q5GSD7oSBTsbGx8Cn+56/sD5IgLvpP0DS5C14mC6HwVRRY9vEy2aZOncNsUqCdshwMhHADh17Kyq9ALe4zg0h+dRdKmUI7wW48nD59mlcXNiJD19FpqBd6ydzKO4ZZQ62/k8Irefr06TNnznQ7wbPsb1fYbbxFEKgKOSBAiZnQeSJTvB9NReKovmVv6uBG/RzOhg0bpk6dyltH/6JPNvG3/vDDD/9gQ98BhbWB9RAZGclfR8hpfpJvwLCOSZMm6TP+vn37Pv30U16rbgeJBw8eFGuVd8bs2bNpddDwvgxOqsrLwB393KNK3iAz3UifxMTEMEx02fEU6TTSqTld5CA8SWusZU9GH9oI6iSG9/13dghyZqgkc9E1a9bw/tPDWOmgwvPmzaMzkb4y/lDIH+Ih9gQqoVJ0ifiUFy/jGTNmkAF9c3NRD/UOCqr35ptvBuwzUVIlsVcUF6UhtJp+c39H5OWKpPSuYBhi+0ZFRaEwx48fl9M+PhFUuLSCKmFDYG1L9X6y4U7Uiwo6+hToQCaHKVOmqM2fAIsHRiFfrIHSSeYEh0dKn2DuogJ0BQoclIt6DC70ZPHixZb9HZN/ELc+NmmsWKgYW1RVftK5KCyFBpKSmp7rEwLWnrRFR+fOnbHA4BLMh3QONp+sBWEuSIAKWetjDvHI7A0mcMxKiBm3dO/e/amnnlLiRm/pOgn0BzCmvYPEoAy33XYbYw1hIcQaNWo4vkyhb5SGrTx48GCMWiiHYnqMGsaXmO+MqbFjx4oxDdBziiX9jjvukG/cwlUAFYaNwP1gMpKClYyBRcPF9AcNGzYkhREnlrq8Vngnih+gTJkyoQBUGDsbo19ZurJ8BO65556QR9E8+lAAE6Z8oSLdunVjwmEQ1apVi8El04KjjVb8umjVqlWpbXMbMCvHtlVUumzZskoNKLZ8+fJko9vlvewu1gPjxo2DRUglUR4mGS5btWpF8+lkOIz4p0E6wpq8xc1EIdKELzG0+/fvL6fBIe3Dhg1jDrds+oqg5RA7NHjIkCFSbSaTp59+mpx16tSBwdavX79Hjx764kTIhvMmFR+/2bNnZ05GH9z1FzCRMkvUrVsXXoSGvP3222rZmfdvtWrVuCVdunSDBg1ikoTWSmQRegZS7X2OjpeUrMwLpUd2dAjtYppyvLB4GaGHzIR6op+nMw9Ir5JC71Fz+cKC+DCZ6FtZ7qavZA0TGixTYv78+SMiInjXYwEKz0SUkMzly5e7JxbL3vb5zDPPyKlgVBcdVlMxViXEEhmhMCNHjmQQ+fFH4DEimNWZH8TFA8pDafSMnACSWinuZJAQME5k860iU8rqRnByfFSg22CMGnWUVE6KyjhNHYSZi2JUSRsYbAwVzCbsMxXxzIq3ONeuXevgokLWIUV0ByOEPNzoGJwGQcH8wsuPiYCJg1cOMwtvINSLV4t8Nps8ebKcGwnEezBnauYnXpz0+ejRo5nO6tWrp7PKhQsXPvDAAzBbJMKLn7lM/dS7d2+mbF7/vOB5AbRv396jbpSDKcC00qJFC14AUgfZB8VcSa14Q1BPrJOcOXPK5hk0hPeWWBLM4P1tyKdry56geetTZ946vKvuvvtusR6oT9u2bZl56QEGnhxaEFf7vOyx0jDR4OpNmzZlPu3bt6+UxluWlz05qQlWadGiReVzXbly5XSrF6uIWbJPnz50SKdOndKnT6+vPyRUpZBgdPBe5Ln8I+eLxDIjRWr1yiuv8HrgLSXvAAoXnpO0xlr2NqEnn3yySZMmlACpps9VeAABpWHOwirRE17/4mkwUVyUnuFtEYgHzE3/jsCE+PLLL9Nd9DyvZOw8VEuMJKYL/hHLSb6GYutgnefNmzcQv1fHp7xQfixdRMbLG5OI13/BggV1Luqh3gkBYuPQSTEihYtSvbvuugvRi7nDa17dhSzkM7Oibdz4xBNPIBf5mI0U5syZ46eHPYQ7bdo0qiS+9aV602y4EyV/QqNPcP78ecZ1y5YtmVIwDngQRiE9zHTN4NULxEi1bJtSEhPrc4/CkR1z14oVK6gP+uDgogkNLhQVwWXOnPlf//oXkxgzGMNE7CTVRngUhYsCU1VxkKO4aM+ePVEtsYMp5NqubPPepCbub6+i1bwQMSwUN0sIicrsAKq1fft2+QaUZDCEZVkS25oZRjwDu8FTeFbQr1QJQQLlJd+FBiNO//AERwrjZwjvPkQ627ZtE4sQQbv1zdFGtUeXzKQn9M1XflUHbt0flRLVdbx8ySyvIW70/q4aUtxHjhxxLAAmCrLDLqHvKSEbzlsAw9qnmlFVprKU8NGCNS+H8Sg8ISHymtN3qicKzL1oneLPtDeFGmLZr2902L0AwOMQB81k5tEP8Xoj5IgwSCZQBsYFA9mxIQJ5Me8dP378woUL7rtIZAbglZTKW1PDzEVlUdTjc6xEsBEHTYqLopSyNGz25SYWGF4VKlRQe1egLgF7rxdjm2laPJthvmO6LV26FBLCnIuS5c+fXw8nhSUNv6IcNY9gu2Pvyv9IhxLkf3GzoXsscBxoceDUqVMSZqBMmTJRUVFMVa1atVq5ciWDoVq1arLuJ9myZcuGZak+wwR1mIHa6HuWxJ8+9isjjUQ5cpA7d24M9MOHD3fv3l0oAeR58ODBqpAqVaoE4l3DW/ZXPS5vv/32oUOHUg4VkzNLU6dOlQyMTGGMcsnwFr5EW7yrFEJylvXCCy/oW32wuaX5zB0SkLpQoUKTJk2i8NOnT8uuJNgXFUhyY2WXlPpALmUqNwO0CINePzIk7CtRXLRYsWLwK3QG60RWVB577DGVp0aNGlRJvSmZ8sifNWtWxRIbNmwYuHpnzrPPPhvQzo2ElJe068EHH1TKDO8SoqKekpB6eyOoTgoXrVu3rmwFJA90CLnIVIYoMX/lE69SksjISOqvOkFCFvmpgLdwrWD+QoImhhx9DFLIvMpP6wLaFjJ3gcw2FStWpFf1eOghgchgsGrXDIUwBelc1GNwMePJoj3Kw1SGyYtJJPsMYc5q+dftu0W46B133IEURARypm7kyJH+ax52DBs2bMiQIdewAgZpDUHPixrckKhdu/batWuvdS0MDK4lwsxF4Ty8+DHLMA62b9++e/dufTcCZl90dDR8Rsin4qJCTRmN8g1vx44dWEWp40f4uga9hBGp+zejA2vVqgXrk0uJ6jZgwAD9LiEYjg/nclIcOmHFe4aA0CoRYLfJP/KCHD9+vLpR/ZQQxIJ8/PHH9cQpU6ZAQq5oEIeK3gHWW7RoAS9St2B9ymqMrBZyKbap/t2OcqDZ+/btU3dh85HtmWeekQziHkA/ND979uyAdqKsU6dO8A1dG7GV6WT5oO5dJW9UrlxZX5DBtlZfkRctWkQhFK4yY6nLhh/ZbJO0xkJcoUnqgJYEWlDHcngjOhxdyqGpRHFR3V0EVFNitcmytuy7Vsqp34X6yaV4UtW5qMOHQUh5xcTEBOxjYPpTJGagcFEP9faGBxfVT8XLYrK+H1gOuihBd+vWDb6kdotABb23PqqnewvX8s1FvUefxI3QWeXGjRurV6+uVDroU+hM/1/ELVsKlONwYinfShQX9R5c586dE1aplyCfV5QFnxAXVR5WrPgJKoW8MXmAkfvVV1+hJ7zyEEfQbdIGNy0MF72x8fvvv/PGZ/JnRtJPhBoY3JwIMxd1nPmU1U51Ggp2umbNGvEmrHNRiYcDTRXvTwJ9Z69BUIjLsqCnPQVBPdeVKFECo9axcCcRxpRdK2ctnnrqKUfhx44dE3OwY8eOPvdUiBcBnVZZ9pJgvnz5nnVh9OjRkiGo3S+b9Nx3CXXBWnXbptAM7H73LcrXXEhXdUWLFqW2CbXOu0reEB93EBX3eaSghohIU3bVJq2xlhbfYu3ateKdQmibuANp0qSJXmDyfRc1b95cJbZu3ToQv0tcQVzqZcuWTZihTy7qIS/x1uA4GOk4L5qQenvDg4vqY0EWcvUzLY48ItwcOXJERET4PxLvR7g+uaj36HvxxRd1rzBuBH1KYiF+TSdMmKAnOs6Leg+uoM5UZbZ54IEH5DIhLqr7LtqwYQMpderUSWaLEgvZwyKYNGlSKj/dII3j448/1j/SGdxgkM0mAduf1o4dO651dQwMrjHCzEUxNCWyDYbX+fPnxReT7Ak8deoU/8vndgcX/e233+Ry9+7d/EQeuXQ4uDdwoFOnTsxlHseL3VyU7pXDh45N/9j6AdttoFzu2bNHVuEyZMjQo0cPtQfYsl29y6E4zFn9ZFfNmjVLa1ArHkG5aLly5R5++GGPprntfpSBFH1rsQNB6ZksAuv1d8Cb25w5cyaQcOzmkFXyBgNEIneJzaH7kwzKRcXZBlTBSmpjLftE0IwZM2jR3Llz+/fvrxZaV65cGXCF1Es+F5VzsBIHRRYM3Y4NZO1UXMskn4uKvwfHyRwHF/VQbw8kiovqnkLceWTjOqhQocK6dev8PN2PcH1yUe/RR5VKlCiR2KckFhIAUxxsKuhcNOTgCspFDxw4ELC3ssulfy6K1JLZosRi3759VatWLVmypCOmqIHBhAkTypcvnzNnzrx583bp0uXrr7++1jUyCDN4xZctW7ZSpUrf+YgbZGBwwyPMXFQC1GDqyaUEXQVYwOIBb68N8R0MMO/Onj0r66JAnRcVR09y5tsgIUgEOY+5zM1F//nnHzk7p2QkQCgk6hGukAvMRIhrxYoVdR8P3CsnUXWe1rdv37YalIEVlIsWKVIEKuuxDdtt96MMAdt9eUK3BKVnchjM47ujN7eRmGkJxdYLWaWQYFyMHTs2R44cATu6oNoLEJSLyuZJ8fyUtMbC9zB/X3/9dVmOkz26wkVlYbxBgwZ6/uRz0alTpwbi935LcPnJkyc7bixcuDBqJh9Hks9FxSugY1eF24+uh3onhDByUbB8+XJ4VMB2JOgniklI4Vq+uaj36IPIpU+f3uPofli4aJs2bSgE5dcTdS4acnAF5aLy8Uj8eFlpm4saGBgYGBgYWGHnosIh1QrPhQsXhGRi+2JNfhcMR44cEcq6Zs0aZR6JD6SgESkMFOTAmO5lRIAUhGwE3aN73333BVwH6tatW0ciHNKyzyLq3onEkpYQVb/88os6ADx37lzx4Kqc3wRFUC4qu0NXrFjhyDxv3jw5dea2+0nHRL711lvdtEECKwelZ7L016dPH8ct27Ztk2p7cxu4YubMmTNmzOgITUl6TExMyCp5Q/n9R//r1asXsN3DSkpQLgq9J1HiSietsVAyRKb2hepcdP369QF7YVynKMnnoqKiq1atsuyYE4Gr45hZ9jnDTJkyoWNymXwuWqtWrcDVQeSsq7moh3p7I1xcVMn98uXLsjxYsGDBkMfjQwrX8s1FvUefrNXrp9AFSgRh4aJDhw4NXB1U0Lqai4YcXEG56Pbt20ns1KmTXBouamBgYGBgkMYRZi4KV+HFj70olwcOHOBSjJjjx48fjYekg/3798NX//vf/8pJUTHXsELgpVz6ift3MwOjFisKi00Pq41hikkn/wflohLaGJNdT4yIiKAcWXVBCsqYs+LXBsXbxxdffCFcSCAHVr15V1AuKgGXixQpoos4OjpabcmDLbjt/scff1xqrp+yGz58uAc9Q68C9lZM3R49fPhw06ZNxfoPyW2EC5FB+aznxjfffFMWlr2r5A3ZbSuA3BYrVqxMmTJyGZSLwldLlSolXD0JjWUA8mvOnDnVkpeY/tOnT7fsDcMSi0z3o7tgwQJSWrVqFbItVgJcFBNfCRHWhI7lypVLj0dPok4FZblM19gHHniAFLWRNaS8qEDAjnKun4iW7y+yz8JDvb0hK3UPPvignpgELtq1a1fdUY3sbtC9HwVFSE0G+fPnd7NEd6L36BM53nnnnfqnwLlz58o3Cys+TLljkz9FJcoVpBwKyJw5s76bWr5WqKAs3oMrKBcdPXo0XaRqLovJ+rZww0UNDAwMDAzSFMLMRbFo5cjopk2bsDKFcOoH4QSO86KWzT24/P7772NjY7E7+Z+//h173LTABA/YYQwwSbHSMLLvvfdeFUBc/FIq57QCbPRq1apxizLRsJJLliypYmZyCS1R5jIyuuWWWxYtWmTZXFTnh9CAbNmyqagMQSG+WHVvn5a9Q1KCLmLXYhfCPSAhDz/8sArOtnr1an4tX768fteaNWsCNmAagwYNmjhxIsUqwsa9AdsLjsMtk/gIzZ49O4bp5MmT4ecwOpRTf5DuyO6TTz4hRUVbgdvLgca77rqre/fudOZjjz02YsQIP1XyBgRJxU217LU7WIr8L1xUD2ixcuXKLFmyKC9HSWjshQsXMNP59d133929e/f48ePlAGf79u1XrFgBQZWQGDly5MDW//vvvyHbsoAGLYGHOMJzuyHxY6ETKmX58uW33367vmwuH0d69uwpl5CoJk2aVK9eXbVC9vTScCaQmJiYdu3aSSWhzXLUPKS8aKaE8yYF9gjvRSjicIuWbty40UO9vcGsRQcihd9++01OGVh2eJjA1V6ppcLIS6WIqisnySi8Hp+WplWqVCnk061QmowEZfu9fsw+aKL36Lt8+bLsc86dOzfpo0aNatasWYMGDRTjpfMDdiyZP//8Uw58njt3DlV0SD8kJH5PuXLlYINXrlxhLBQtWpSUJ554YvHixVaowSVcNGPGjNu3b5cUXjSIvn///uoRom8dO3akUR9++CFqNmnSpED8oWuB+NFlSvRfcwMDAwMDA4NwIcxc1LKZjJwaFezdu9e9/czNRbESYKHqrvXr10sMXANvYMN169ZNyFLA9gYpPmDoPWyyXLlykVigQIFhw4bpLo6wzHr06IEZjWE3YMCAGjVq6FvykOBtt90GNYqMjMSA41e12AUXxX6tX7/+p59+OnLkSKxStysaHVjM8ApZvOWJsAv1E4ohVrtw6ZdfflnoAS2aMGGChKYM2G5v9IgXGI533HGH/IRR/s4778gHi2+++ebpp5+WdEiIviyJjrVs2ZIKyK8Yncp8R1HF1Q0VwNilAkuWLClTpozQPGinqC68qGzZsnI7PeNYZ06oSiFB8zHEhwwZMnv2bIzjF154Qa01CRetWrUqeZrbwBxXmyST1ljLdt0pJyQRIuwLRiqhLyEk0tJx48YJqYCeQUSRMpcwH9oYMmIqaoMQUSqqDSdp0aIFPNMd3RtaC2GoW7culLhRo0Zvv/22HguE/6E9UvnSpUv/+OOPKABkGJZOQ3zKS47FSiFQ6+nTp9ONMP8RI0ZAVzzUOyToKFmcZOAwoCA58hQKiY6OprEoufQwT4RKrVq16tVXX5U8tWvXRqyWvfpXsmRJ7kWxIaL0s0dAZh0ewmVg0tuSjm7QNHQpaKLkT2j0CU6cOAHrk4bQWGYYfRX0888/Rz346ZFHHjl9+rRlz+fC/6G4PntS7qIbpTkQZgT95ptvMpS6d++udtZ4DC7hougbWkT/t2vXrmLFio7TyDRTogFTCIyXgSY0G22hKCqwYMECmWpoZp8+fUyAawMDAwMDg1RG+LmoZS93nD17FuNG34znB3Ak7uLekIavgQ5MqO3bt4td6B+ICTbiDk9PugiOnzAK1d5Uyz5rx6+Yg/v27YuNjU1URMGgoM5bt27VH+EHkI2dO3cm6ul///03D0pOEL/ff//9559/TohnJqFKYt9DjehktZQtUHt0eRzFuhmdNzwaS1EIXV3S/4cOHdIzMPR4otSHkejYiukH3Ltjxw7vrjhy5AjVSOiQJJ25Z88e+TXJzrTPnDmDioq89M2oHurtB7t27fIZzSghSJciI6rnCPPrB8nXZAXv0Xfu3Dm4blAFQHxqmVdAP9MzlStXTmwdaA5z14ULFyz7HEfQmT/o4NL36IrCBC1fYlabaNUGBgYGBgZpEynCRQ0MDJIDE+jc4LrDqFGjHB7RUhRBz4saGBgYGBgYXF8wXNTAIM3BcFGD6wsTJ050nEtPaRguamBgYGBgcAPAcFEDgzSHjz/+GDu7fv3617oiBga+IJtsUxOHDh0K2FF5b6QDHVeuXPnmm2+UN6abEDExMdOnT78h91Rv3bp1+fLl6tJnS+fMmeMRQjzJSKFi0zJuYNW68XDixAk/YbcNbhgYLmpgkLYwYcKE8uXL58yZM2/evF26dPn666+vdY0MDNIWvvrqq5o1a+a08cILL0ydOvVa1yi5uHTpUteuXcXb3M1shN155530QKLiA6V9TJ48uXjx4oGrYzX7aemvv/5KnqxZs4bXq1YKFZvGcUOq1o2Hbdu21ahRI126dJkyZbrWdTFIPRguamBgYGBgcO3RokWLm5yLRkRENGvWLLEexdI+pkyZ4uCiQVvq8I0XFxfXunVrPUxRWJBCxaZx3KiqdePhzz//NFz0ZoPhogYGBgYGBtceb7311k3ORW9ULF261MFFgyJkBgODmwE5c+Y0XPSmguGiBgYGBgYG1x6Gi96o8MNFJ06cSJ5Uq5KBQZqF4aLJxLlz57Zv3/7999+vW7du586d+m78EydObNy4MTo6esOGDQcOHNBPUPP//v37SedX8hw/fjzVKmwmPgMDAwMDg2uD06dPL1iwICoqCrMgKBe9dOnSt99+GxkZyV9HuFd++uqrryz7BOCkSZMcQV8d2LVrF0ZJXFzc/Pnzv/jiC2WCeJQvwDqZOXPmlClTNm/eLCl//PHHD/GQlH379sllTEyMn4fGxsZ+9NFHX3755aFDhxzxk7GBJO4uzVFPUY+muyRl69at6pZTp04tXLhw8uTJWFE+ndPQ6u++++6DDz6gYthtjl+p8LZt26ZPn07DaYLj1ytXrsAtz5w5w7NoL89V1dPx999/8wjkQouCclHVUvD5559nyJCBPNI6FcSYZyHiy5cvh7d67mLpBPRQqr18+fJp06YdPHjQ3aiffvoJXZ0zZ47/2MgnT57EJuYf2oXQ9d5GXlOnTuW5joDJ1Hz16tVSAR7EXVwqL2XozKeffkqPUVXHs3777bfPPvsMZSa/O8a13uECegZV5J+9e/fSLvrNoT+MCLSUCtCTR44cSSjAuAIZZDTRRe4OJEVcRqGxs2fPpqp//fWXd4GCkBJHmufPn4dyrFmzhqG6ZcsWdyEewyRpFTt79uzixYstW3n4Z8aMGfS/I09CM4B3ixQXZbx//PHHlOw9uRnoQC7oPwKVv2D9+vWiuuiwpDAk5R/V+YiG0S2J6kbyp06dDRc1MDAwMDC4BsBqLFeuHIb1ihUrnn/++XvuucfBRbEYGjRoMHr06Pfee69AgQJ33303hh3p2Jpt27bNkyfPHXfcgZ2RPXt2bqxevbr7EZin48aNe+SRR8iAGcpTAjaio6M9yhdg3bZv375ly5aY41Q1Xbp0derUwTqHA2BBSjli8WPLyrKeWJDeD+3du3ejRo1owrp168qXL88jLNsIHjRoEBUgGzYrKb///vuzzz7LZY4cObCepUqYWd27d8+WLRs9JimQvebNm7///vvdunXLmDFj3bp1//zzT+9uhy08+uijEyZM+Oabb5544gkMXxqofv3ll1+o+VtvvYUpRs/kypWrXr16QpixuTt37pw3b17xgvP000/fddddNJmega7oj0AoJUuWHDNmDE3u0aPHww8/rLiou6XY/QMHDrz11ltJ6W9j9+7d2IUdO3bMly8fiYqaJr967mKROALKnDnz7bffjlDKli3LXfxKt+gunTFVkRTdu2rVqn79+pGhePHiPAIZuRmIAObTsGFDhNKiRQsEJDpASy2bT/LQAQMGoCf3338/z5KugB6jHkWKFCEnt1NVVR8eTUcha1LKlCnjUHiq16VLl3vvvZcORzf4B8kKoXJ3OOC5UixqgEbdeeeduXPn5rJ169aqzH379pUuXRpV5593332XX0+cOOGhV5Ar+mTw4ME7duygmXTpvHnz5Kdly5ZVrVqVEmg1BRYtWlTayPAP+gFIh4fEoQodOnQQaUL1GU2IW/qZ+UFn4wkNk6RVDPVu3LgxDfzXv/5FraiSPDdDhgzTpk2zQs0AHi0SCBddtGgRI11uvOWWWyIiIrw7ykCwefNmIZnwT+ZqFGPNmjWwevi/UFAh9owOxjKXTKpcnjlzhv8REOmMJnSeu/RPfikKw0UNDAwMDAxSG1OnToV+qA/P2A0VKlTQuSjGGQa04iFYjfwKX8WkIHHJkiVcYkD37dv38OHD2NNBbTWKPXr0KFY7mTE6MSKXLl3apEkTnutRvqS0atWqTZs2qijsVzJgzsolTFhxUQHNES7q8VAsJBIV48XWkUDK2EyQz8qVK+uEgXZRYPr06cVaEkRGRmLFyv+QyRo1aqif3n77bW7HOvfodsgYnYalJZebNm3ilvz588uKDQYZ/1OOyo8lRwUQjbSUplWqVIlboDp79uyxbAaCoVy4cGF1S2xsLNWGSqkUqqS4aNCWAqigvkeXJlM+tEHnosmvXtBiYWvwVagFTEzWLYU6tmzZUj0IakGKWnB78cUXuYRmk+Jen1TF9uzZk2xQx6ioKLoFjVq5ciVdXa1aNVkslWz/j71/j9+pyv//8csphKiEhkZFOUwmTTqMDqNo6CByFhU1dJCk0om6kTQ6kEMKE03SUaQcopGJvEQhQg4hynnoM0Rpqvf+3n/7cbN+y97Xta/9ul6Xl7Aef7xur72utdde67mea+3nY6+1nk8oB083C4nNmjXjLvKIDNOo888/Xyk0R3muvfZaUjCmdYm0uXz66ad1yeDi8oUXXogQ+F133UUKbJOh5PlM/rTTTiMFpqQMrVu3btmypcnfpEmTpGvFBrVr12YImEtIXfny5c1KII+mcHq5f//+DDHSKZyUaDfg0T0O5UOTpTnwvQULFlAyVBwuRwojRbdED5MMKoZItdRfvHhxSoPb7Nu3j/mHFBSJIRYxA6TVYc/noihthw4dvv76a/I/++yzFEtRNCRCVg6ev5IPpWRchL1k79mzR6udZkOEWKsUXouiRvnzGY6LOjg4ODg45Cu+//57jL9bbrnFTrz77rttLnr99dfDXn7eD6w9LZ19+umnnr/LVLZg2nUVb7/12bt3bzsxuvwJEybwPwalyY+li3GpX8Hvfve7ABcNnPJK+tBJkyaROHToUJNiLGaAQAKEAaZqSIUAIdF3fezdU045BZJjmjBnzhwylyxZMiLq7B//+EebYHs+UezSpYv5nxICOzlFezCI7cu5c+eaDFqmM9SuUaNGVatWtUsQU7L36IZbGuCiQpUqVeySs1K9cLFeqO+2bdtGBmRlUurUqQNhMMwKVkAG2JoXCX3g+Mtf/mIn/uMf/6hcufLPFq644gqyPfXUU8pwzz33cPnKK6+YW3r16mVn8PZz44EDB5oHob3aZuz5C/782q1bN5M/LHAkRsoTTzxhUm677TY7D/T19NNPN1KCTUXvFIV0nXfeeeby8ssvpzSzSg9p55KWmgxvvvkmKVDiiDLj9Li+PtgsQlScynsxhklmFYO6k4dJwE5s164difq65KWYAeK0CG2EfNr7hKUSSDiiSg6e/wUTSpmTk7Nr164vv/xy6dKl33zzjYYtqiiaaiZtfiVFX3zmzZvH/xs3bkTJSVm1alXMDeRZgeOiRwhWr149atSo5557Dt061HVxSAmGt/2x3CECTqWzCx2yipmZV9dnn32G7ZXdOmDVjRkzBs6Tl0KOjJj1b7zxhvYH2omB86LaNHtVCFocwJ4I24Kp8PDDD5MZDmAnRpd/ww03kCGizLRcNOlDMZXEeKF/NhcSOnfuHCAMS5YsIaV27dq6ZAqF6el/LbHWrVs33ITAGVQDLGB7vSiM0047DcYVoLLakHzllVfqUnazOSsLtGr39ddfq4H836JFC7uE8HnRcEuTctEzzzzTJo15r17SYr1Q3/34449k+P3vf29STj75ZFLMwc4tW7Zw2bZtWy8SoqzXX3+9nQiDLVu2bLjXDLEMc9Gnn37aXvYEDBNS7OU1c5hz7dq1Eq/9rScscHHRv//97yYlMABVDXg7RDe6mcL/+fD8Harjxo2DAXI7xr1+FeX761//avLH8WgVp8e15MsMbzLs3btXS9979uxJO0wyqxhExdBdA3V3nTp1dJl0BojTorDvIuwBMhQrVuxwn/kPNlADbbXV/ltBW21RS10yeD1/PzzZuFy4cCGXgSOmYq3fffdd/lTbcdEjAUypDz30EO8eBdSWNwuH3xR4BdaoUSMw4zukglPpLII3is7t2JZlKvC6euyxx2R3BizIvGDTpk3t2rXDBAlYwBngyIhZrxN3MFI70TaFd+zYETC1A8gjF01bfq1atbAaI8rMjIuCiRMnYlPyE4Qk4KgpTBjARRddROKCBQs8X0QTJkxQOuY+6TF5gqDF3jFjxiT99YcfftBWwMBSMxNRwj8eqctosjdz5kz+v/XWW+0SssJFs1K9cLFCWi563XXX2Txt0aJF4Y8pYSTlojVr1rzgggsi7orPRclp34glffPNNw8ZMmTy5Mn2Ap2XEReFyDVo0CDhA6kaVhmBXbt29evXr0uXLnPnztW6qKGIGVC+mD0e5qKgcuXKWn5MO0yyyEXXr19PIiRcl+EZIGaLkvrR1ZHU//znP1DoMw/EyJEjI6p6VGHDhg1ikqtWrULImzdv1iUTvucfDhfJZPwa90XaeC9eOmfOHKYFNB+CyqU5qH+w4bjoYQ/UxXx7++KLL5g6becTmSGtsziHDPDee+8dbC6accf9pnr8YKj0UY6vvvoqJhcVXnjhhexyUc9fNChfvnzeueiREbO+U6dOiGLQoEF2om0Kr127lv+bNWuWqoQ8ctG05WNQFipUKHzoyCBjLur5qxw6S5Y40FtMUi6qNRMkpsOQ5omjRo1KHLjdNy1Gjx6d8P0DJf2V8mXv6qSlwZo1a0i88MILdRlN9lTbJk2a2CVkhYtmpXrhYoW0XBSqU716dYbw/Pnz9+3bR681btw4Yi+0kJSLVqpUqWzZshELXBlwUSqMSOvWrauVHO3RzSMX9Xx3rwzSUqVKkX788cdHu3LBmocBvv7667rMOxeN2eNJuWitWrUKFy7MYEk7TLLIRRF+wvIpFZ4BYrYoKRetWLFi6dKlPX9/TecDkasPUkc2tC4KzNT96aefcqkT8uiD9uUCBvKSJUv4Z/ny5Z4/ZPjf9Mv27duVLe0YzwocFz3sgVmW9UBMLuL2wUB4xs8usM6jnXakwrJly+x3/CHHwVDpoxxhyzIaSS3IvCNsAR+16N+/P6K46aab7ETbFMZogAoee+yxYa+wb775ppdnLpq2fK0IwawCvxqSkxkX/eqrr8wxpHHjxskD8IoVK5SSlItiVMHTSpQogZX/4IMPmnR9tLrooosCNaR8eaMJIycnJ+G70gl8fdu6dasOsJ199tlkGDt2rP3r3LlzE75jUl1Gk7158+ZphcfmWtnao5v36iUt1ovBRT3/y2D9+vXvvvvuHj162J6HI5B0Jrn00ktJNJ6QDcaPHy91yoCLauyYkEJZ4aImFg52OcQ74fsHStVSVAjKajaQe9ngol68Hk/KRWHO0FEvxjDJIhdFQ0js2rWrLpPOAHFaFOaijCZSAgePHcIQh5wzZ46Zf+SUCLZv8jCjal0a28/QVFFWs/i/d+9ecdH8WajIPheNEyx15cqVC31IHJs2bVqYDKtWrcp69Y488FrNruHuIm4fJBxsLsprknd8bu/CEj3jjDNSLRQcEmRdpR0cF/2tQXvSihYtap9s7NatG4kKigAwvLhs2LChbQ089dRT2qSa9/Oi0eXLUkdnbCMG9mgYAvNGwvKYsnv37gIFChQuXDj6oZABs8nW279QKfbrpeCioGfPnlqYsl2eMHfJX2i/fv1M4k8//dS2bdtUYfEwOSpUqMAtFGgSqXnHjh21jDBs2DDJxL5r8ODB8HZzcD2a7O3Zs0cehm3XABMnTiSlffv2JiXcUsXSCOxdDAyZvFcvabFeDC66YsWKZs2a5fa0XtKZpHfv3iTSXp1bE7AYzY7xDLioQrYYLio21aFDB5M/Ay56ww03mJ9+/fXXypUr825K1VKdALe5qMRuAt5kRvni9HiYi2oHtfaipx0mWeSiAwcOZAYwM0bSGSBOi8JcFE7BXTNnzoyokoPn80ydFNXolqsqnRFFhxcvXkx36/sjOqDTofJSzkxu9ut6/nZrLu1p5KAiy5QjTrDU//znP+ZorL6PQsr/nQw6UOuQCogaRSlbtmyRIkUUIFtL7UJ0BPNUIaEDEbdNYHEgfaX7TIrtZSsinjX9++qrr/JesW0aYfPmzVSDSZya26+l+GDOfcmHHQktL1WKg4gQ8zt27Jg+fTqCRYEDIdTtGX/16tUjR47EQDFHw5mFJVW9UZgmjJwDIygcJp4p5r777kv4Hj50S8xtFcxWl112mb4fc5ftJSg6FHXeBZW0C/Ki0gicGRaZY8obi8TLRoBvzF+EwAs1aUT7VOHaY4K7tL+I1mG3YT0YcoIOoMDU3BaC3a5UmibQg6gct2NY7N27NykXTVX5PHJRpm6KHTt2bCDwoLGAFZMdlTBOWXPVtHDMeu8gd9PBQNOmTRN+HD/qxiSMVsvZCUNSEeTl7hJgaz722GPPP//8lVdeaZZ6mJD5qUSJEnEGuzz02m5I05aP+oltlilTplOnTgMGDGjTpk2TJk3MIJLPTPjJqlWr0DEs14oVK5ICX9XLIulDIQP2JzNupAlmimvRogW3BGJ1ev7GM0xVOy6FoKiP4KqrrsKchavUqlWLWStCFOIwCd8nJ61+9NFHIRiIQr8izEsuuQRSbc6oo65VqlR55JFHTAmaM+3wEnJLa44SKLhFqVKlYN2QOmZ7rQQyAJnxNMmEW1q3bl1Jj3nMHCRW6Egzc2aleuFif/nlF6ZcJGyis2zcuDHhh7oxt9SvX5+7unbtiiYwchlraGzaUK5yIGx80giohyoAHb3rrrsYsyjYBRdcYCL33HrrrYkDnSeLvj700EMmRZTGeCfSkXi0EWljxuh067nnnstsoLkiLHB6nxT4kkmRr10Ggi7PPvts2mh+hVt27949VUs/+OAD7kWMzOe8OqmqIsQwDaoQbK2E70PI3MJPpNhhY8KI0+PionSKLhm5V1xxRb169czMED1MMquYuCjtNaYXOsMMYH/XTjoDxGnRiSeeWLBgQR1x9PxPSKjfnXfeGVEfBwMdCsV4wFacO3cu//NXHxwVxMX+SefwPf8jmnFlpL279jLpwUaWuWjaYKloIfZlTk6OzUURwX8sbNu2TRuXA1sOHALA5mbY2wGyzQf1iAjmESGhwxG3ISHYSSeccIJ5tzFrYCcpmrY+mUTEs2ZO7NatW5cuXZjcmdeYfXr16mXqz4116tShWJ7SvHnzGjVq5Kr5vAUvv/xyXjAY3Eydxx13HHzMlJxZldIiIsQ8guUlzVvhrbfegig2btwYG87eiGK4KE/U8X2AJBUhDbbGBG1ejfqadeGFFwY+3CYNEw9XkZ90bB11nIkfFY0pU6YomjymEneZl1naUNR5EVREF2Sg0lu2bOnZs6eMLRRS0QuKFy8uoyqPAb6ZmpAwNjcdisFEVa+++mqTIVW49pjAAkD42H8YAehA7dq1zzvvvGLFilFPOpeugQlgnyE6UjB0zI1pNU1iQXmw82bOnInRhtYlQqe/IiqfMRfF7GvYsCE9QgmYrbTOtjDERemmqlWr0oNyYGNHxYxuWtKY9d5B7qaDB2oI8ZM/p2OOOYYhzAzGeLn33nvNx2kUVVthE34Mhscff1wmBeJVn8pktFcaA4DMM44YwuRk4Dz55JN2jMRU5Qvbt2+HRWiyKly4MIPIHh0bNmyQP7aEvxyEyjEj0XeM0DVr1qR6KMJnrF177bWvvvrqM888g/LLJGXOoY+kEuiJiWJqwJQedkKOwmDpasZI+Dtjx48fn1byaJReahryJtClwATVo0ePChUq0DtUCQJsNiozq/Tt21ceSpkhqfnOnTvhJ0YIxrBD2eDYJGJSM7vSWC7bt2+PwKHuSVsKgyKzSqZY5gRRI5Vs9sTmsXrhYhmzHTt2VMoNN9zwhQ9GkFIYxYrrM2bMGCNnA0ZThGO5kSNHarSi5NTZ/kSIhjC5qRAUrEOHDvpIhBEyaNAgLSyjXVoaHTp0qD5zwI2ZLmgmPEofSuhHZgzUknZJ35Bzv379eIGKCiJ8bOuwwNEBzfknn3yyyKc5F0oeDShqiHpQ2ptvvolkWrduHRE/CVUUAQbcyOsJ3quh/frrr6Njer/TWCYxGssMr7cVFUaHIxacI3pcEBflV+Y3XqzM/Ewm9knviGGSccXERakVraZKt956K68w40MoetpJ26KJEyfSKF5Ybdq0oUVQ61T+xhzCgGdp862AAWY+6aLA2osrYN7beoJ5bxwaaVtvvnktzjIXTRsslVmPDAqAY7hoAKtXr/73/og3DmkRPmQSHcE8IiR0qgL1/d7+zioCIy6aKp615xMnXo3mLjGrcePG6ZKZyHyAZITkNnKUPrkZN1/6SK9zRxlXKS0iQszzxmLuNqsuSFsnTMz2M3FR3p2wYspZv379jTfeqNe5vv/pa7r9mVYbkwwXTRUm3vM3UOm9mysZevu91NjfMuOEos6LoNJ2Qa5Ueu/evWvXrpXtgrnACw/qJW8oeQ/wjdrYoQihsmSQKZM2XHsc6HQNHIBXtV4Jir54+umnQyM1YLXbyj4nk1bT9u3bBzlngJhb5ErRcNG0lc+Mi9IXmHHGqsDgkMXPAFSKuChi1NdWlBaGg4aY12F001LFrD/Y3XRQQaNQA0Tn+UEdky5ywvoY9fFHX24RXT52zJIlS5Ja4RBXbjQxSOOsOaOcdAo3MmxRjPiNoutTGUYIjWowo+bKcsLSiFADioI02uFVcwvVCj7v+SuBccLAbtq0KTqCZRarl1swBgcOHIh5OmvWrMmTJ7/xxhtMlTBVOwZpbgFV5i2WLT9k2JMMJaNRzD+IKC/GtLqM9w7vbvVjWqBU9g4vejPt0nFMRPS42aOLPG0JBJDZMEkFe48uE0jAF1EcpNVh3gtMEUkP+jmkBfrPhMzME3inIHZ0EqnqpRMAv3ILN+Yx9FpukWUuGh0slYHNLIY9zT+puCjDXuduI9z3OdgIG+7REczThoROWmCAiwZOpCSNZ42hCYHB4DA1wdBM7N+uo4msefPmZlqMiPmWFDAcrFizhQB6Q4GmXRlUKSaShpjHpilWrJh9vMTzuaI+CmqNTlzUjoVN2+vUqUOiFgb/8Y9/BLho4EBLRJj4LHLROKGo4yCpoOJ0QW5V2vM/YHOpFWYh7wG+Ff7BflMuWLCgXr16emjacO1xED5yo0OACM3OBtMuVaqU/o+jaTDbhBXXztu/n9Nw0bSVz4yLYpjCNm1D56WXXmrYsKGxxsRFbdtCHaeTbHGa5oVi1udDNzk4HOV4++23maaSchjbP5DDIUFS30UHG0nPizo4ZIYsc9HoYKmwU5HMVFyUmW7+/Plud26uEDbcoyOYe+lCQmfARZNartCkAgUKhKth3AloAq1fv37GxxFNQ3JycnQgx2zny6xKcZDUZciYMWMS+7cB29A+IpnFSX0XjRw50iSm5aIRYeKzyEXjhKKOg6SCitMFGai0jlrZOzLyHuAbUsRzU7Uubbj2OEj6Oj/Wh52iiJr6ThlH05AVdbN/DXgiSVv5zLgo5J+SIzKEPaZc5e+w0M7GOE3zQj5I8qGbHByOctSpU6dChQrmPKcBBt6AAQMOSZUcDBwXdTjckWUuGhEsdceOHfyvr9epuOi2bdvkuCl/AtocGQgY7mkjmAsRIaGzxUW1vGZWM8JYvXq1jOzChQv36NEjImcqoCfYrx07dhw3bhxsKmF53susSnGQlGJp/yetCGTWmS45CUjKReXKvGbNml4MLuqlDhOfLS4aMxR1HCQVVJwuyEClw1w07wG+a9WqBS1PdXvacO1xkCsuqtkyrab973//K1SoEHTU/jXARdNWPgMuqshydqzIMFJxUb0j4gwiL8RF86GbHByOcjz00EMMulNOOYXhOXLkyBdffPHxxx9v3Lgxfw911Rw83iD0jjlknj+A+iZ819bOXHfIO7LMRSOCpSrKyxofK1euVDoGtP2lbfHixSTanscd0iJguKeNYJ42JHS2uGj79u1JtF2zhkHv33rrrSI/tWvXztXJig0bNlx88cV33nmnVke1Rzeai8apUlokpVh6etu2bQOZdYp1+vTpXgouqhDPyNOLx0W9FGHis8VFY4aijoOkgorTBblVaS8ZF817gG8ML0hdqsMCacO1x0EGXDStpm3evJl/FBPcIMBF01Y+Ay66bt26tBoYzUXjDCIvxEXzoZscHBx4t9avX79ixYqMuEaNGvGeysz1vUMWsXz5coy343zwEuzfv3+2Dt9GY+rUqVdccYWe27p1a9vJgoNDBsgyF40IlgpvSRq4xThz37dvn1LyZywdMQgY7mkjmKcNCZ0tLqqFSjuMm7BkyRKIE91t++CRkWq7UEqL888/v2TJkmabbhwuGl2lmM9NSrEUPq5q1aqBzDqcpu0ASbmoYq/37t3bi8FFI8LEZ3GPbpxQ1HGQVFBxuiC3Ku0l46L/znOA7wYNGnAZ8O/n+UvEXoxw7XGQARdNq2nwruLFiyesgA1eiIumrXwGXPTXX38tWrRokSJFAh8TSTezTTQXjTOIvBAXzYducnBwcHBwcDhIyDIXjQiWum3bts37oXSwbt0648ppy5YtpGCaZ7dKRzxOOumkAHWMjmCeNiR0OOJ2p06dEgcGLJbHHfiJLpNarh999FHC33/7bz+Eo7Bx48aWLVtiLmOPdu3a1aRrUeW2226L2WrUKeF7oDXrIeLYZiNfBlWK+eikFAs1rly5Munz5s0zidQNWtWqVStdJuWiTz/99AknnCD/kzqTaddZUUOfeOIJXUaEidfioe0YKSa0fmhvjIwTijoOkgoqThfkVqW9ZFw07wG+9SEA/mZHQB03bpy+d6QN1x4HGXDROJqmTa22H12kodrqMm3lMzsvqk9UPN18T6RP0WGzxh7NReM0zQtx0Tx2E1VFJ/PZZ6CDg4ODg4ODkGUuGjNYatLzogrlks9b3g93YKhpR6UJCuyli2CeNiR0OOK24r5AYulWSOytt94q75fQPy1WJI1n7e1f0ChZsmT79u1Hjhz58MMPn3HGGSiG5ztMPv74400MADShYMGC7733XsyGY7bCZ8TTVq1aNXToUFXp9ttvnzFjBmLJoEoxkSrE/NSpU6nSpZdeamJ7UqsKFSoY/V+2bBk3nnPOOebG9evXY0ObsOb0SIECBYoVKzZ58mQy9+nTR0HejHuniDDxjCmezr0bNmzQHviYzRHrQFUoYcqUKd9++22cUNR5EVR0F2Sg0qB27doJy72NkMcA3/SjvOaUKVOmU6dOAwYMaNOmTZMmTcSZ04Zrj4OtW7cmfCexJgWyrYCTNjsSOTeKlFbTGKcKVIgEEON3332nY7okkhOtS1t5ZgZ+ZXKI3xbPX5wvWrSo1jbvvffep5566qKLLjLhozw/jFPiQBfNGraKtxSnaV4oZn0eu0mf1VADt4/XwcHBwcEh/5FlLurFC5aalIvqsGj8rZIOMBOZZVqLGD58uFnMjIhgHhESWusVgYjbnr/AhW2n0s4880wsfkxbSFT37t2hEBHxrOnfdu3aybYGMBxDOXjWCSeccP7551Ptl156qUGDBoFTkWmB0amDpliZkFgYqWJ8Y3GOGDEigyrFQXSI+c8++wyqCbHv27cvJm/z5s0DQckQOKSuZs2anTt37tixI0WZ+KhC//79JXz6CNY0bty44447Ds4mWpgqTLxAw7XkCEmLb1ijGPLCh54gNyWmDUWdF0FFdEEGKg3xvvXWWw1ThaaapfK8B/im+yC9UjMEe88999j7BVKFa4+JWbNmoSG6HeaGAn/++ec33XSTUiBUc+fO/eqrr0QjQdOmTc1OhLSaxlyq1dSEv2b4ySefoFeIdMyYMZp1U1WehkP/NHyKFy9O+bk6wA8NrlGjhoplgJvNFN9++22XLl2UjjrRdng4OibZUpM5c+akbRrSCMesz2M36csIWLt2bfxmOjg4ODg4OGQF2eei3qELluoQQKoI5mlDQieNuK1wxspmr1mlxY8//rh48eKAmU45Uo/Nmzdjgmd2SBhzlpqbS5hzTLfmSauULaD8iNcs7IRBY3l6OLiuoHDVIlQUZZeTNkw8xCwQ6yUOeNbSpUvDFT6o4dQz64JUKh2BvAf43r17N2w5Vaj67IZrzxXSato333wjikXbFckmgINU+S1btqxYscLeUJ1bpG1aGBl3E7WtWbOm81Pg4ODg4OCQ/zgoXNTBwcHBweGwwEcffdS9e/dDXQsHBwcHB4ejEY6LOjg4ODgcpfjwww/vuOMO51PXwcHBwcHhkMBxUQcHBweHoxTGkfshwddff23CUP1GgEC+PxDRZ22g8YH8e/bsid4PH35ErjZjG7z11lvxnbQd2fjhhx+GDx8eCAqdx5wxQd9NmzZt8eLFub0RzfnXv/71xRdfZKsmhx1i9sW33377/PPPZ3D6xsHhcIHjog4ODg4ODvkKKKh8hgWCHh1yjBgxwngdK1SoULVq1SpWrFiiRIlTTz21devWL730UoCafvnllw888MDxxx+vW8qWLVu9evXSpUuT8uc///n+++9ftmxZ4BEjR4686KKLlL9IkSI1atSoVKnS73//+0svvfTee++13SxHABov91rGV9nRDPpFXsGymDMt1q9f36VLF0UztkO+pQUq1L17d/lQpD55r8lhiph9ceONNyYODE7m4HCEwXFRBwcHBweH/MaKFSt+g1zU81e6RDB69uyplF9++eWTTz5p1apVwYIFy5UrZ8JQGfTt21fE0qwz79y5c9CgQTBYuYAOuLv7/vvv5ff4ySefVMp3333Xq1cvUo499tgZM2akreSvv/7asWPHRx99NK+tPSKwYcMGhPz2229nMWdMoBW55aLC9ddff5Rz0VR9EfD6xnC49tprw990DlPkxaedw5EKx0UdHBwcHBzyGz///PNvk4uCk08+mbo9++yzgfSpU6cqSFLgp5EjR5J43HHHBfJDTRUkGVIK27R/KlWqVJjDtG/fnsQqVapkrykOBxcPP/xwZlz0/vvvP8q5aFLs2bPnjjvuONS1OFg4slvnkDEcF3VwcHBwcMhv/Ja5qGL5hrkoGDNmDD8VLVrUjqcFFUnKRT1/Q6Yi93bs2NFOJ3OYw/zzn//U3t0tW7ZkqSkOBxeOi2YXrVq1uvTSSw91LQ4WjuzW/Xawe/fuL7744uOPP547d+6XX35pH2TYvn37ggULZs2a9dlnn5lYd/xdmAIUlQ8VdlzUwcHBwcEhv5GKi+7YsePdd98dOXIktkLACRC8bsKECUrEnnjxxRexM/QTiUuXLiVl5syZea9bBBcFderU4deGDRualAguCqZMmSKG+cknn5jEpFx00KBByhnHUwsCnDp1qu33CCFgY40ePfrDDz/ctm1bYCU2KTZs2PD6668PHz589uzZAXfKGGETJ070/GDI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CTm56667cjQ/cdGzZ88ePXqk/7uxONw14XDPv0PakHou+tdff23cuPHjjz/G4ixfvnz79u3mJ6jCioMROzPD/aTv2bMn5Rk78nDvvffal3G56NixYyXkI4+L/vzzz5UqVerbt69JcVz0qEIauGisjmUBjoseGRlIOXKai37yySfHHnvsBx98kEPvz0WkpGEegjjylNxGZhWyVatWl112WU7mKD527dpVtGjRGTNmpP/TNoYPH44y5G4esoPDPf+HKbZu3boiHr788kvdAL1auXLlggULli5dihv5559/+t4AiVu1apW5Pz1IsaJQhs8///yDKCiq/kE0+nXt2rUfHAxfN0wHs3DhQtKzE5flqEVcLmpguOj//vc/hDxy5MiPPvoo9radO3e+9dZbo0aN+vjjj7O/lRwt//TTT3kbXey+ffviclE+9MILL0ydOvWHH37w/bR8+XK1B5SKe1AMs5GDgtSuXZsX/utf/0KLNPdrc9Hdu3e/++67o0eP3rhxYzZLsX///nfeeeell15atmwZymwvO+Ers2bN8t2/d+/e9957b8SIETQBnvX9Ch1CGmg44uWFCIce2ncPn5gzZw5veO2117755hvfrynhoryWr9sp27Zte/XVVydOnIi0kWR2Xk5VqiM/cODA+++/P3bs2O+//14//fbbbx9++CGl5iuxD0LYpkyZQl2jFXE37fz666+oAdqLbth+2+bNm5dEYV6L4inlv//9r3k8ERelCl6MYvXq1SYxro4ZBOitF90pSqknTZqE3U8hF6Xl/uc//0ECiFG/0qyWWNiyZYvS16xZo5TsDD8lkraNpHKYMGHC888/H6vkXjaq24B0XwPnQxp9W79+/ZgxY3gq1o4Ft9C0wXBRyi6ri9KaX2mDds1iarxoD2tSYn0IGzQELQ4fNmwYN9NAzE8BRp4G+8YbbygR2VI19Nr6iUSaAClz5871fSvAUNtvlk3jr0/m/DRt2jQvqg/U9aZNm5SeyAzGNsyQzR+QN9wMWiVdg20AA7IXDF6F8iNkiuCLTxbG1HvhWllc8H4+ijKrT6eV2fojfPHFF9QgqkK1vvnmm3Z1B7c+KlQeAsRs8uTJPIup0U8Uk76VDtFY9TD5CVDIWJDhe++9l5vPOecco+3k0yi/qWgUQynmhfxDF+NFnfLx48dTO3FtYLDhatu27d///vfsuEBh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DrnMnTs3xbzkkkvkcujQoaktqYEdac09GRgEhOGiFxQ2bdqEqyhSpEik8X4izgIFCiguKqhdu3YQLjpnzhyy7dy5k7/XrFmDB/35559jKHxAxHAqIzmPOnPmTMGCBS9ULppG5otgRGmNiwJ6Sko7++D1/8QTT8Qklm3YsGGtWrXQarkcPXp00aJFvafgfvjhhyxZssyePVsu4XiErV9//bXvu7BCTz/99LfffptMmbt06ZI/f37FmSdOnJg9e/YNGzZ43HL48OEaNWros7iPPPJI5syZlyxZkkxhUg7lypV75ZVX5G9YdKtWrYLclbp9x2keafS6deu2a9cuVeRJadhqO1Jhbf1627Zt1atXHzt2bHyEDIiWLVsWKlRo4cKFckk3F/IpY14U7fvvv6ejBRm8Po+QRlxe8hEH95RauGDayMAJw0UvKDRt2lTchod7u/fee21c9J133gnCRQkf//Wvf8VM1qgwcODAefPmxeRR69at69y5c3KecOedd16oXDSNeLK33norDXLRqVOnprSzD/jwf/75hy4JP0nm63788UdKtGzZMj2xePHiRKWRbjly5Mg111xzxx136IktWrTIly8fUnm/7o033mjQoEFyBLbCw2EZM2a0SVimTJnHHnvM465x48ZR0sqVK6uUPn36pOXQDWqNeB9//HFSb0z1vnMBm0cnAtZ2mlUzHXRPfcGCjYsKOnbs+Omnn6aGdCmCxMTERo0apbYUsUEc3FOqIIaxn0EaROy56JkzZ7Zs2bJ8+XL0ZsWKFQkJCeonbNnKcwEfkJ9Onz69adOmpUuXzp07d/HixZs3bzZDIEkF9vTKK68kMMUS/fvf/46ULWouev3116cuFyVizpQpU0x2HB08eJBQO5mD9BdqsCXReWpL8V+kejztipR29sHrH2tJzu+++y6Zb3z77bdz5MhhS6xbty5sM9ItUglNmjTRE0ePHk0i/3u8SyZV9P3q0UF045tvvtETGzZsmC5dOo9FyziXDBkyPP300yplyJAhPOeJJ55IpjwphFGjRhkumvYRpLbTjl31xgcffHD48GF16cpFf/nll7RmlpOD2rVrlytXLrWliA0uSC4aw9jvgseuXbtWukGtGKJ3r1q1av78+UuWLIEIQL7UvQTGP/300w9h8Ec8D0OJsWWEiK5fv35OGBRV/qBq5Neff/55zrlQG3Uo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Bgb0djinfpqFwvz5820LBQ2SCaLV3LlzO0ccrPAyp3h+JsvAFwsXLnzggQdMVGHgjbFjxxKhuuqJxxp4g/MXrlsHDWKLtFbJaU0eg1SB4aIGBimC7777LnTuln3BP//806hRI7USzyAmaNGiBbXtXL2zfft2ajtVRDLwwIQJE958801DRw08UKZMmQIFCjjnBufOndu1a9dUEckgRWFoSRyQ1io5rcljkCowXNTAIEWwZ88e2eFQrVq1bt26DR48uEePHg0bNqxevbrHF0ENosPUqVPTpUuXNWvWevXq9e7de9CgQZ07d65Tp84rr7ySnG/rGaQcFi5c6L1/2OAih5zsctVVV7Vs2bJ///4DBgz48MMPq1atmioHTRnEATt27KDFc+fObXZppRzSWiWnNXkMUgWGixoYpBS2bt36+uuvlyxZMm/evLfddtvzzz8/YcKE1BbqgsWCBQtq165drFixyy+/vGzZstD+WH3H0sDAIFUwdOjQChUqFCxYEEZauXLld955JybbUA3SIKZMmfLQQw/lCOOpp54aMGBAakt0ASKtVXJak8cgtWC4qIGBgYGBgYGBgYGBgUG8YbiogYGBgYGBgYGBgYGBQbxhuKiBgYGBgYGBgYGBgYFBvGG4qIGBgYGBgYGBgYGBgUG8YbiogYGBgYGBgYGBgYGBQbxhuKiBgYGBgYGBgYGBgYFBvGG4qIGBgYGBgYGBgYGBgUG8YbioQQriwIEDp06d8s5z4sSJhISEM2fOBH/s/v37//rrr+SJFmNs2LBh4sSJHhmOHj3at2/fjRs3xk2kZOL06dN/++HIkSPOG9esWWNr9N9++y0OAv/555/Dhw/n/zi8yyAVcd51pQsG+/bt++qrr7zzJL8bpuX23bJli36J21qyZMm4cePWr1/ve++sWVs2btzvm+3UqdNr1yZ8880v69fvs7nF+BjSCwnECUOGDDl27JhHntGjR8+ZMydeEl1oOHz48IgRIw4ePJjaghic3zBc1CD2OHny5Pvvv//8888/++yzJUuWvOeee+bNm+fMBgWtXbv2c88916FDh7p1637xxRe+Tx47duzjjz/evXt3nl+1atVly5algPhJw4QJE2644YZQKPTwww97ZCOGI0/FihXjJlgysWfPnnfffTd//vyhMPij5FkUK1Yse/bsJF577bX6LbDQGjVqkA5N1dMn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
```

---
