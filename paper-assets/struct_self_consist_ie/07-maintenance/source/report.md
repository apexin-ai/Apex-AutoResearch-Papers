# Handover — 2026-05-24

> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。

## 运行中
（无）

## 待处理
- exp_fewnerd_mf4v2_s42_v4: Superseded: v3 (exp_fewnerd_mf4v2_s42_v3) already succeeded. This v4 retry is no longer needed.（准备中）
- exp_fewnerd_mf4v2_s123_v2: FewNERD MF4v2 s123 re-run: original died without output on autodl-5090. Generating instance-level samples.jsonl for MV unified recompute with seed=123, N=8, T=1.0.（准备中）
- exp_fewnerd_mf4v2_s42_v2: FewNERD MF4v2 s42 re-run: original died without output on autodl-5090. Generating instance-level samples.jsonl for MV unified recompute with seed=42, N=8, T=1.0.（准备中）
- eval_scd_fewnerd_fallback（准备中）
- exp_a1_spider_sql_sc: Cross-task universality: SC diagnostic cascade (degeneracy, LP-quality gap, agreement-correctness correlation) applies to SQL structured generation on Spider. Qwen2.5-7B-Instruct base model, 200 dev examples, N=8 T=1.0, execution accuracy evaluation. If F1-F4 failure modes exist in SQL, the framework generalizes beyond NER.（准备中）
- exp_b2_v4_inverse_frequency: Inverse-frequency weighting of entity features (agreement_count, vc, sj normalized by log(1+type_freq)) improves cross-domain generalization by reducing dominance of high-frequency entity types. Two variants: A) replace original features, B) augment as additional features.（准备中）
- exp_b2_v3_domain_invariant: Removing domain-specific features (dataset_enc, entity_type distributions) forces the verifier to rely on domain-invariant signals, improving cross-domain generalization at the cost of some discriminative power. If LGB AUC improves on held-out domains, domain features were causing negative transfer.（准备中）
- exp_b2_v2_multi_domain_joint: Joint multi-domain training (CoNLL+SciERC+FewNERD LODO) improves entity verifier AUC and cross-domain construction F1 by exposing the model to diverse entity patterns. Tests whether training data diversity overcomes the calibration gap that caused B2 original to fail on FewNERD.（准备中）
- exp_b2_entity_verifier: An XGBoost/LightGBM entity-level verifier trained on agreement_count, VC, LP features can predict whether entity candidates are in gold annotations, enabling post-hoc filtering or score-weighted construction that improves over greedy baseline, with cross-dataset generalization from CoNLL+SciERC to FewNERD+WNUT.（准备中）
- exp_a2_degen_regression: Degeneracy rate is primarily driven by task difficulty (dataset entropy ceiling) rather than model capability, with a positive correlation between base F1 and degeneracy — easy tasks with high F1 produce degenerate outputs because the model has already converged.（准备中）
- …另有 7 项

## 近期结论
- **exp_fewnerd_mf4v2_s123_v4** (killed): FewNERD MF4v2 s123 v4: regenerate finetuned FewNERD seed=123 instance-level samples.jsonl on autodl-5090-c for v4 MV unified recompute. N=8, T=1.0, seed=123. Model: qwen3-8b-fewnerd-exp021-merged. Parent retries v2 (failed on 5090) and v3 (killed). Using confirmed-working 5090-c environment from s456_v3. ← 基于 exp_fewnerd_mf4v2_s123_v2
- **exp_fewnerd_pretrained_n32_s42_v2** (success): Pretrained N-scaling rerun: FewNERD N=32 with Qwen2.5-7B-Instruct. v1 killed at 70% to prevent UnicodeEncodeError crash at save stage (no incremental checkpoint). Fix (errors='replace') deployed. Same hypothesis: tests pretrained MV advantage at 4× budget (N=32). ← 基于 exp_fewnerd_pretrained_n32_s42
- **exp_fewnerd_pretrained_n16_s42_v2** (success): Pretrained N-scaling: FewNERD N=16 T=1.0 seed=42 with unfinetuned Qwen2.5-7B-Instruct. Fills the N=16 point on the pretrained N-scaling curve (N=8/16/32). Tests whether doubling sample budget from N=8 increases MV delta and oracle headroom for pretrained models. ← 基于 exp_fewnerd_pretrained_n16_s42

## 趋势
成功 206 / 负向 55 / 失败 15 / 共 312
degeneracy_rate: 5.42 ↑（近 3 次 success）
greedy_f1: 0.539 ↓（近 3 次 success）

## 下一步
（无活跃 idea，请通过 ideas.md 添加）

## 资源状态
autodl-5090: 空闲 cuda:0, cuda:1, cuda:2, cuda:3

## 告警
- ft_002: 已被终止 — unknown
- mvp_pilot_002: 训练失败 — unknown
- exp_007_ner_llama: 已被终止 — unknown
- exp001_seed123: 已被终止 — unknown
- exp001_seed456: 已被终止 — unknown
- exp008_re_n16: 已被终止 — unknown
- exp_002_merge_conll2003: 已被终止 — unknown
- exp_001_n16_seed123_full: 已被终止 — unknown
- exp_001_n16_seed456_full: 已被终止 — unknown
- exp_008_re_n16_full: 已被终止 — unknown
- exp_001_seed42_v2_r1024: 已被终止 — unknown
- exp_001_seed123_v2_r1024: 已被终止 — unknown
- exp_001_seed456_v2_ner_r1024: 已被终止 — unknown
- exp_002_conll_n16_r1024: 已被终止 — unknown
- exp_007_llama_n16_r1024: 已被终止 — unknown
- exp_018_llama_scierc_seed456: 已被终止 — unknown
- exp_019_supervised_verifier: 已被终止 — unknown
- exp_lp_t07_scierc: 已被终止 — unknown
- exp_qwen3_4b_scierc_finetune: 已被终止 — unknown
- exp_freeform_seed789_v2: 训练失败 — unknown
- exp_qwen3_4b_scierc_finetune_v2: 训练失败 — unknown
- exp_qwen3_4b_scierc_finetune_v3: 训练失败 — unknown
- exp_qwen3_4b_conll_merge_inference_v2: 已被终止 — unknown
- exp_qwen3_4b_scierc_merge_inference: 已被终止 — unknown
- exp_tacred_re_benchmark: 已被终止 — unknown
- exp_vc_lp_cascade_selection: 已被终止 — unknown
- hidden_state_probe_conll_v2: 已被终止 — unknown
- hidden_state_probe_conll_full: 已被终止 — unknown
- dgs_pilot: 已被终止 — unknown
- mbr_pilot: 已被终止 — unknown
- exp_031_fewnerd_t12: 已被终止 — unknown
- exp_030_conll_t12: 已被终止 — unknown
- exp_b1_scd: 已被终止 — unknown
- exp_b3_prompted_diversity: 已被终止 — unknown
- exp_b1_scd_threshold_ablation: 训练失败 — unknown
- exp_14b_inference_scierc: 已被终止 — unknown
- exp_14b_inference_conll: 已被终止 — unknown
- exp_a2_humaneval_sc: 训练失败 — unknown
- exp_b_frontier_sc_fewnerd: 训练失败 — unknown
- exp_fewnerd_7b_n16_s42: 训练失败 — unknown
- exp_fewnerd_n16_s456: 训练失败 — unknown
- exp_fewnerd_mf4_s123: 训练失败 — unknown
- exp_conll_mf4_s123: 已被终止 — unknown
- exp_conll_mf4_s456: 已被终止 — unknown
- exp_fewnerd_mf4_v2_s456: 已被终止 — unknown
- exp_fewnerd_mf4v2_s123: 训练失败 — unknown
- exp_fewnerd_mf4v2_s42: 训练失败 — unknown
- exp_14b_inference_conll_v2: 训练失败 — unknown
- exp_fewnerd_mf4v2_s123_v4: 已被终止 — unknown
- exp_fewnerd_pretrained_n32_s42: 训练失败 — unknown
- exp_fewnerd_pretrained_n16_s42: 训练失败 — unknown
