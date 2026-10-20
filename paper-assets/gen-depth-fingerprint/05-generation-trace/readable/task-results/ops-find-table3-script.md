# ops find table3 script

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_find-table3-script_20260516T173941_result.json`
- **Structured JSON:** [`eed4cc5d61d6dd42aed6.json`](../../sessions/ee/eed4cc5d61d6dd42aed6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== Command 1 ===
/root/gen-depth-fingerprint/results/8gen_classifier_comparison.json
/root/gen-depth-fingerprint/results/8gen_logo_baselines.json
/root/gen-depth-fingerprint/results/8gen_logo_unfiltered.json
/root/gen-depth-fingerprint/results/bootstrap_ci_results.json
/root/gen-depth-fingerprint/results/bootstrap_ci_v2_results.json
/root/gen-depth-fingerprint/results/filter_diagnostic.json
/root/gen-depth-fingerprint/results/finer_ordinal_results.json
/root/gen-depth-fingerprint/results/ordinal_baseline_results.json
/root/gen-depth-fingerprint/results/per_gen_binary_f1.json
/root/gen-depth-fingerprint/results/review_p0a_binary_logo.json
/root/gen-depth-fingerprint/results/sampling_ablation.json
/root/gen-depth-fingerprint/eval_8gen_baselines_pooled.py

=== Command 2 ===
/root/gen-depth-fingerprint/scripts/alt_classifier_eval.py
/root/gen-depth-fingerprint/scripts/binary_bootstrap_pvalue.py
/root/gen-depth-fingerprint/scripts/bootstrap_ci.py
/root/gen-depth-fingerprint/scripts/bootstrap_ci_6gen.py
/root/gen-depth-fingerprint/scripts/bootstrap_ci_v2.py
/root/gen-depth-fingerprint/scripts/gemma_rp11_held_out_logo.py
/root/gen-depth-fingerprint/scripts/instruct_length_confound.py
/root/gen-depth-fingerprint/scripts/lofo_ablation.py
/root/gen-depth-fingerprint/scripts/multi_seed_stability.py
/root/gen-depth-fingerprint/scripts/olmo_instruct_length_confound.py
/root/gen-depth-fingerprint/scripts/ordinal_baseline.py
/root/gen-depth-fingerprint/scripts/p1c_instruct_logo_f1.py
/root/gen-depth-fingerprint/scripts/plot_fig2.py
/root/gen-depth-fingerprint/scripts/plot_fig3.py
/root/gen-depth-fingerprint/scripts/review_baseline_ensemble.py
/root/gen-depth-fingerprint/scripts/review_overall_ci.py
/root/gen-depth-fingerprint/scripts/review_p0a_binary_logo.py
/root/gen-depth-fingerprint/scripts/review_p0b_volume_matched.py
/root/gen-depth-fingerprint/scripts/review_p1c_qwen06b_instruct.py
/root/gen-depth-fingerprint/scripts/review_p1d_6gen_baselines.py
/root/gen-depth-fingerprint/scripts/review_p1e_ordinal.py
/root/gen-depth-fingerprint/scripts/round3_computations.py
/root/gen-depth-fingerprint/analyze_7gen_logo.py
/root/gen-depth-fingerprint/bootstrap_ci_plan015.py
/root/gen-depth-fingerprint/classify_multi.py
/root/gen-depth-fingerprint/cross_generator_eval.py
/root/gen-depth-fingerprint/cross_ref_analysis.py
/root/gen-depth-fingerprint/detector_baseline.py
/root/gen-depth-fingerprint/eval_8gen_baselines.py
/root/gen-depth-fingerprint/eval_8gen_baselines_pooled.py
/root/gen-depth-fingerprint/eval_8gen_classifier_comparison.py
/root/gen-depth-fingerprint/eval_8gen_cross_model_chains.py
/root/gen-depth-fingerprint/eval_8gen_finer_depth.py
/root/gen-depth-fingerprint/eval_8gen_logo.py
/root/gen-depth-fingerprint/eval_8gen_logo_baselines.py
/root/gen-depth-fingerprint/eval_8gen_sampling_ablation.py
/root/gen-depth-fingerprint/extract_confusion_3class.py
/root/gen-depth-fingerprint/finer_ordinal.py
/root/gen-depth-fingerprint/fix_tail_decay_and_eval.py
/root/gen-depth-fingerprint/generate_artifacts_d038.py
/root/gen-depth-fingerprint/sampling_ablation.py

=== Command 3 ===
-rw-r--r-- 1 root root 14398 May 17 01:31 /root/gen-depth-fingerprint/eval_8gen_logo_baselines.py
-rw-r--r-- 1 root root  3567 May 17 01:13 /root/gen-depth-fingerprint/plot_fig1_8gen.py
-rw-r--r-- 1 root root  9550 May 17 01:12 /root/gen-depth-fingerprint/eval_8gen_cross_model_chains.py
-rw-r--r-- 1 root root  4166 May 17 00:09 /root/gen-depth-fingerprint/scripts/gemma_rp11_held_out_logo.py
-rw-r--r-- 1 root root  4553 May 17 00:06 /root/gen-depth-fingerprint/extract_features_jsonl.py
-rw-r--r-- 1 root root  5188 May 16 23:20 /root/gen-depth-fingerprint/eval_8gen_sampling_ablation.py
-rw-r--r-- 1 root root  6032 May 16 23:00 /root/gen-depth-fingerprint/eval_8gen_classifier_comparison.py
-rw-r--r-- 1 root root  7304 May 16 23:00 /root/gen-depth-fingerprint/eval_8gen_finer_depth.py
-rw-r--r-- 1 root root 19396 May 16 22:21 /root/gen-depth-fingerprint/eval_8gen_baselines.py
-rw-r--r-- 1 root root 13403 May 16 22:18 /root/gen-depth-fingerprint/eval_8gen_baselines_pooled.py
-rw-r--r-- 1 root root  9023 May 16 20:54 /root/gen-depth-fingerprint/fix_artifacts.py
-rw-r--r-- 1 root root  4790 May 16 20:52 /root/gen-depth-fingerprint/supplement_rp_lofo.py
-rw-r--r-- 1 root root 13512 May 16 20:51 /root/gen-depth-fingerprint/generate_artifacts_d038.py
-rw-r--r-- 1 root root 19421 May 16 20:41 /root/gen-depth-fingerprint/fix_tail_decay_and_eval.py
-rw-r--r-- 1 root root  9396 May 16 20:18 /root/gen-depth-fingerprint/eval_8gen_logo.py
-rw-r--r-- 1 root root 10542 May 16 19:47 /root/gen-depth-fingerprint/llama_filter_and_extract.py
-rw-r--r-- 1 root root 10226 May 16 19:39 /root/gen-depth-fingerprint/mistral_filter_and_extract.py
-rw-r--r-- 1 root root  9006 May 16 17:19 /root/gen-depth-fingerprint/generate_chain.py
-rw-r--r-- 1 root root  5907 May 16 16:32 /root/gen-depth-fingerprint/extract_qwen8b_crossref.py
-rw-r--r-- 1 root root  4854 May 16 13:43 /root/gen-depth-fingerprint/bootstrap_downstream_ci.py
-rw-r--r-- 1 root root  2145 May 16 13:20 /root/gen-depth-fingerprint/compute_dataset_stats.py
-rw-r--r-- 1 root root 11608 May 16 07:47 /root/gen-depth-fingerprint/end_to_end_classifier_v2.py
-rw-r--r-- 1 root root 11653 May 16 07:26 /root/gen-depth-fingerprint/end_to_end_classifier_pythia.py
-rw-r--r-- 1 root root 25268 May 16 07:25 /root/gen-depth-fingerprint/paraphrastic_chains.py
-rw-r--r-- 1 root root 11588 May 16 07:09 /root/gen-depth-fingerprint/end_to_end_classifier.py
-rw-r--r-- 1 root root  8352 May 16 07:01 /root/gen-depth-fingerprint/finer_ordinal.py
-rw-r--r-- 1 root root 26637 May 16 04:45 /root/gen-depth-fingerprint/cross_model_chains.py
-rw-r--r-- 1 root root  3220 May 16 02:58 /root/gen-depth-fingerprint/dedup_generations.py
-rw-r--r-- 1 root root 25857 May 16 02:26 /root/gen-depth-fingerprint/multi_domain_seeds.py
-rw-r--r-- 1 root root  2267 May 16 00:48 /root/gen-depth-fingerprint/run_high_only.py
-rw-r--r-- 1 root root 18260 May 16 00:02 /root/gen-depth-fingerprint/sampling_ablation.py
-rw-r--r-- 1 root root  5674 May 15 23:51 /root/gen-depth-fingerprint/scripts/p1c_instruct_logo_f1.py
-rw-r--r-- 1 root root  8734 May 15 23:26 /root/gen-depth-fingerprint/analyze_7gen_logo.py
-rw-r--r-- 1 root root  4522 May 15 21:44 /root/gen-depth-fingerprint/analyze_instruct.py
-rw-r--r-- 1 root root  9118 May 15 21:43 /root/gen-depth-fingerprint/scripts/review_p1d_6gen_baselines.py
-rw-r--r-- 1 root root  7520 May 15 21:43 /root/gen-depth-fingerprint/generate_chain_instruct.py
-rw-r--r-- 1 root root  9490 May 15 21:43 /root/gen-depth-fingerprint/scripts/review_p0a_binary_logo.py
-rw-r--r-- 1 root root 16052 May 15 20:38 /root/gen-depth-fingerprint/scripts/review_baseline_ensemble.py
-rw-r--r-- 1 root root  4201 May 15 17:40 /root/gen-depth-fingerprint/scripts/alt_classifier_eval.py
-rw-r--r-- 1 root root  3650 May 15 16:35 /root/gen-depth-fingerprint/extract_confusion_3class.py
-rw-r--r-- 1 root root  2054 May 15 16:16 /root/gen-depth-fingerprint/multi_seed_stability.py
-rw-r--r-- 1 root root 19500 May 15 13:44 /root/gen-depth-fingerprint/analyze_prompt_types.py
-rw-r--r-- 1 root root 11704 May 15 11:41 /root/gen-depth-fingerprint/classify_multi.py
-rw-r--r-- 1 root root 15297 May 15 11:41 /root/gen-depth-fingerprint/cross_generator_eval.py
-rw-r--r-- 1 root root  8943 May 15 11:41 /root/gen-depth-fingerprint/extract_features_multi.py
-rw-r--r-- 1 root root 10469 May 15 11:27 /root/gen-depth-fingerprint/generate_chain_prompt.py
-rw-r--r-- 1 root root 27276 May 15 08:55 /root/gen-depth-fingerprint/scripts/ordinal_baseline.py
-rw-r--r-- 1 root root 15161 May 15 08:46 /root/gen-depth-fingerprint/scripts/ordinal_baseline.py.bak
-rw-r--r-- 1 root root  7355 May 15 08:40 /root/gen-depth-fingerprint/bootstrap_ci_plan015.py
-rw-r--r-- 1 root root  5942 May 15 08:38 /root/gen-depth-fingerprint/finetune_downstream.py
-rw-r--r-- 1 root root 11276 May 15 08:21 /root/gen-depth-fingerprint/detector_baseline.py
-rw-r--r-- 1 root root  4000 May 15 08:16 /root/gen-depth-fingerprint/compute_binary_baseline.py
-rw-r--r-- 1 root root  8675 May 15 08:13 /root/gen-depth-fingerprint/prepare_downstream_data.py
-rw-r--r-- 1 root root  7918 May 15 08:05 /root/gen-depth-fingerprint/cross_ref_analysis.py
-rw-r--r-- 1 root root  7202 May 15 08:01 /root/gen-depth-fingerprint/extract_features_crossref.py
-rw-r--r-- 1 root root 13967 May 15 07:44 /root/gen-depth-fingerprint/text_length_analysis.py
-rw-r--r-- 1 root root  1703 May 15 02:56 /root/gen-depth-fingerprint/merge_shards.py
-rw-r--r-- 1 root root 15925 May 15 02:56 /root/gen-depth-fingerprint/ablation_analysis.py
-rw-r--r-- 1 root root  9839 May 15 01:19 /root/gen-depth-fingerprint/classify_and_eval.py
-rw-r--r-- 1 root root  7847 May 15 01:04 /root/gen-depth-fingerprint/extract_features.py
```

Note: Command 3 output exceeds 20 lines because `| head -20` pipes are blocked by the read-only tool; full output shown instead.

---
