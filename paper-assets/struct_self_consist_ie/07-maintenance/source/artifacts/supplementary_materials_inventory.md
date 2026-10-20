# Supplementary Materials Inventory

> EMNLP 2026 ARR May — struct_self_consist_ie
> Generated: 2026-05-20

## Code

### Core Pipeline

| File | Description | Source Location | Status |
|------|-------------|-----------------|--------|
| `sampling.py` | vLLM batch inference with XGrammar constrained decoding | `artifacts/sampling.py` | ✅ have |
| `compute_signals.py` | 5-signal computation (LP/SJ/FK/VC/EM) + entity construction pipeline | `artifacts/compute_signals.py` | ✅ have |
| `consistency.py` | Soft Jaccard, Fleiss Kappa, Exact Match metric implementations | `artifacts/consistency.py` | ✅ have |
| `evaluation.py` | Unified NER/RE evaluation (P/R/F1) | `artifacts/evaluation.py` | ✅ have |
| `data_utils.py` | Data loading and preprocessing utilities | `artifacts/data_utils.py` | ✅ have |

### Entity Construction & Selection

| File | Description | Source Location | Status |
|------|-------------|-----------------|--------|
| `entity_construction.py` | Entity-level majority vote construction (Contribution C) | `artifacts/entity_construction.py` | ✅ have |
| `entity_construction_fair.py` | Fair entity construction variant | `artifacts/entity_construction_fair.py` | ✅ have |
| `construction_variants.py` | Construction method variants (θ=2/N, LP-weighted, oracle) | `artifacts/construction_variants.py` | ✅ have |
| `bootstrap_construction.py` | Paired bootstrap test: greedy vs construction (B=10000) | `artifacts/bootstrap_construction.py` | ✅ have |
| `bootstrap_selection_test.py` | Bootstrap significance test for selection methods | `artifacts/bootstrap_selection_test.py` | ✅ have |
| `selective_prediction.py` | QE-driven selective prediction (@80% coverage) | `artifacts/selective_prediction.py` | ✅ have |
| `lp_alignment_gated_selection.py` | LP-F1 alignment gating for automatic method routing | `artifacts/lp_alignment_gated_selection.py` | ✅ have |
| `ccs_selection.py` | Cascaded consistency selection (3-stage) | `artifacts/ccs_selection.py` | ✅ have |

### Aggregation & Analysis

| File | Description | Source Location | Status |
|------|-------------|-----------------|--------|
| `aggregate_seeds.py` | Multi-seed (42/123/456) result aggregation | `artifacts/aggregate_seeds.py` | ✅ have |
| `aggregate_scaling_results.py` | Scale dimension (4B/7B/8B/14B/32B/72B) aggregation | `code/aggregate_scaling_results.py` | ✅ have |
| `generate_scale_table.py` | LaTeX table generation for scaling results | `code/generate_scale_table.py` | ✅ have |
| `token_lp_aggregator.py` | Entity-token logprob aggregation (ablation) | `artifacts/token_lp_aggregator.py` | ✅ have |
| `recompute_table_metrics.py` | Paper table metric recomputation from raw data | `artifacts/recompute_table_metrics.py` | ✅ have |
| `compute_error_correlation.py` | Few-shot vs zero-shot error correlation | `artifacts/compute_error_correlation.py` | ✅ have |

### Figure Generation

| File | Description | Source Location | Status |
|------|-------------|-----------------|--------|
| `fig_signal_heatmap.py` | Signal correlation heatmap (Fig 2) | `figures/paper/fig_signal_heatmap.py` | ✅ have |
| `fig_reliability.py` | Reliability/calibration diagram (Fig 3) | `figures/paper/fig_reliability.py` | ✅ have |
| `plot_scaling_curve.py` | Scaling curve across model sizes | `code/plot_scaling_curve.py` | ✅ have |

### Verifier Baselines

| File | Description | Source Location | Status |
|------|-------------|-----------------|--------|
| `train_supervised_verifier.py` | Logistic regression supervised verifier (5 signals) | `artifacts/train_supervised_verifier.py` | ✅ have |
| `evaluate_verifier.py` | Verifier evaluation script | `artifacts/evaluate_verifier.py` | ✅ have |
| `deberta_verifier.py` | DeBERTa verifier baseline | `artifacts/deberta_verifier.py` | ✅ have |
| `deberta_verifier_5fold.py` | 5-fold CV DeBERTa verifier | `artifacts/deberta_verifier_5fold.py` | ✅ have |

### Ablation-Specific

| File | Description | Source Location | Status |
|------|-------------|-----------------|--------|
| `zeroshot_prompts.py` | Zero-shot/few-shot prompt templates for 72B | `code/zeroshot_prompts.py` | ✅ have |
| `analysis_mbr_selection.py` | MBR selection analysis | `code/analysis_mbr_selection.py` | ✅ have |
| `run_mvp_pilot.py` | MVP pilot experiment runner | `artifacts/run_mvp_pilot.py` | ✅ have |

## Configs

### Training Configs (LLamaFactory)

| File | Description | Source Location | Status |
|------|-------------|-----------------|--------|
| `train_config.yaml` | Qwen3-8B SciERC LoRA (rank=16, α=32, 3ep) | `server:/root/autodl-tmp/struct_self_consist_ie/train_config.yaml` | ❌ need to retrieve from server |
| `train_config_v2.yaml` | LLaMA-3.1-8B SciERC LoRA (rank=32, α=64, 5ep) | `server:/root/autodl-tmp/struct_self_consist_ie/train_config_v2.yaml` | ❌ need to retrieve from server |
| Qwen3-8B CoNLL config | CoNLL-2003 fine-tuning config | `server: path TBD` | ❌ need to retrieve from server |
| Qwen3-8B FewNERD config | Few-NERD INTRA fine-tuning config | `server: path TBD` | ❌ need to retrieve from server |
| LLaMA-3.1-8B CoNLL config | CoNLL cross-model fine-tuning | `server: path TBD` | ❌ need to retrieve from server |
| LLaMA-3.1-8B FewNERD config | FewNERD cross-model fine-tuning | `server: path TBD` | ❌ need to retrieve from server |
| Qwen3-4B SciERC config | 4B scale ablation training | `server: path TBD` | ❌ need to retrieve from server |
| Qwen3-4B CoNLL config | 4B scale ablation training | `server: path TBD` | ❌ need to retrieve from server |
| Qwen2.5-7B FewNERD config | QLoRA 7B fine-tuning | `server: path TBD` | ❌ need to retrieve from server |
| Qwen2.5-14B FewNERD config | QLoRA 14B fine-tuning | `server: path TBD` | ⏳ pending (14B training in progress) |
| Qwen2.5-32B FewNERD config | QLoRA 32B fine-tuning | `server: path TBD` | ⏳ pending (32B training in progress) |
| LoRA rank=8 config | SciERC rank=8 ablation (exp-023) | `server: path TBD` | ❌ need to retrieve from server |

### Inference Parameters

| File | Description | Source Location | Status |
|------|-------------|-----------------|--------|
| Inference params | vLLM sampling params: N=8/16/32, T={0.5,0.8,1.0,1.2}, max_tokens=1024 | Embedded in `sampling.py` | ✅ have (in code) |
| XGrammar JSON schema | UIE output schema for constrained decoding | Embedded in `sampling.py` | ✅ have (in code) |
| 72B zero-shot prompts | Zero-shot prompt templates (SciERC/CoNLL/FewNERD) | `code/zeroshot_prompts.py` | ✅ have |
| 72B few-shot prompts | Few-shot prompt templates with exemplars | `code/zeroshot_prompts.py` | ✅ have |

## Raw Results

### Multi-Seed Aggregated Results

| File | Description | Source Location | Status |
|------|-------------|-----------------|--------|
| `3seed_5signal_data.json` | SciERC 3-seed (42/123/456) × 5 signals | `artifacts/_project/data/3seed_5signal_data.json` | ✅ have |
| `w1_table3_multiseed.json` | Table 3 multi-seed QE results | `artifacts/w1_table3_multiseed.json` | ✅ have |
| `analysis_unified_rho_full.json` | Unified ρ across all model×dataset configs | `artifacts/analysis_unified_rho_full.json` | ✅ have |
| `fewnerd_multiseed_unified.json` | FewNERD multi-seed unified results | `artifacts/fewnerd_multiseed_unified.json` | ✅ have |
| `freeform_3seed_summary.json` | Free-form ablation 3-seed summary | `artifacts/freeform_3seed_summary.json` | ✅ have |

### Bootstrap & Statistical Tests

| File | Description | Source Location | Status |
|------|-------------|-----------------|--------|
| `bootstrap_ci_summary.json` | Bootstrap CI for all selection methods | `artifacts/bootstrap_ci_summary.json` | ✅ have |
| `analysis_fk_bootstrap_ci_full.json` | FK bootstrap CI (full set) | `artifacts/analysis_fk_bootstrap_ci_full.json` | ✅ have |
| `bootstrap_ci_nscaling_results.json` | N-scaling bootstrap results | `artifacts/_project/data/bootstrap_ci_nscaling_results.json` | ✅ have |

### Selection F1 Results

| File | Description | Source Location | Status |
|------|-------------|-----------------|--------|
| `analysis_scierc_n16_3seed_selection_f1.json` | SciERC NER N=16 3-seed selection F1 | `artifacts/analysis_scierc_n16_3seed_selection_f1.json` | ✅ have |
| `analysis_scierc_re_n16_3seed_selection_f1.json` | SciERC RE N=16 3-seed selection F1 | `artifacts/analysis_scierc_re_n16_3seed_selection_f1.json` | ✅ have |

### Signal Diagnostic Results

| File | Description | Source Location | Status |
|------|-------------|-----------------|--------|
| `analysis_lp_range_cdf.json` | LP range CDF (score compression evidence) | `artifacts/analysis_lp_range_cdf.json` | ✅ have |
| `analysis_lp_range_cdf_n16_3seed.json` | LP range CDF N=16 3-seed | `artifacts/analysis_lp_range_cdf_n16_3seed.json` | ✅ have |
| `diagnostic_calibration_results.json` | Calibration diagnostic (ECE etc.) | `artifacts/_project/data/diagnostic_calibration_results.json` | ✅ have |
| `loo_sj_v2_results.json` | Leave-one-out SJ robustness check | `artifacts/_project/data/loo_sj_v2_results.json` | ✅ have |

### Construction & Voting Results

| File | Description | Source Location | Status |
|------|-------------|-----------------|--------|
| `construction_voting_variants.json` | Entity construction voting variant results | `artifacts/construction_voting_variants.json` | ✅ have |
| `fs_vs_zs_error_correlation.json` | Few-shot vs zero-shot error correlation | `artifacts/fs_vs_zs_error_correlation.json` | ✅ have |

### 72B Zero-Shot / Few-Shot Results

| File | Description | Source Location | Status |
|------|-------------|-----------------|--------|
| `72b_zeroshot_signal_summary.json` | 72B zero-shot signal summary (SciERC/CoNLL/FewNERD) | `artifacts/72b_zeroshot_signal_summary.json` | ✅ have |
| `72b_fewshot_signal_summary.json` | 72B few-shot signal summary | `artifacts/72b_fewshot_signal_summary.json` | ✅ have |

### Scaling Results

| File | Description | Source Location | Status |
|------|-------------|-----------------|--------|
| `scaling_results.json` | Aggregated scaling results across model sizes | `code/scaling_results.json` | ✅ have |
| `scaling_results.csv` | CSV format scaling results | `code/scaling_results.csv` | ✅ have |

### Verifier Results

| File | Description | Source Location | Status |
|------|-------------|-----------------|--------|
| `deberta_verifier_results.json` | DeBERTa verifier baseline results | `artifacts/deberta_verifier_results.json` | ✅ have |
| `deberta_verifier_5fold_results.json` | DeBERTa 5-fold CV results | `artifacts/deberta_verifier_5fold_results.json` | ✅ have |
| `claim_audit_v2.json` | Numerical claim audit (all tables/figures) | `artifacts/claim_audit_v2.json` | ✅ have |

### Per-Experiment Raw Outputs (on server)

| File | Description | Source Location | Status |
|------|-------------|-----------------|--------|
| SciERC Qwen3-8B samples | N=8 T=1.0 seed{42,123,456} samples.jsonl | `server:output/exp_001_*/samples.jsonl` | ❌ need to retrieve |
| CoNLL Qwen3-8B samples | N=8/16 seed{42,123,456} samples.jsonl | `server:output/exp_002_*/samples.jsonl` | ❌ need to retrieve |
| FewNERD Qwen3-8B samples | N=8 seed{42,123,789} samples.jsonl | `server:output/exp_021_*/samples.jsonl` | ❌ need to retrieve |
| LLaMA-3.1-8B samples | SciERC/CoNLL/FewNERD samples | `server:output/exp_007_*/samples.jsonl` | ❌ need to retrieve |
| Qwen3-4B samples | SciERC/CoNLL scale ablation | `server:output/exp_qwen3_4b_*/samples.jsonl` | ❌ need to retrieve |
| 72B zero-shot samples | SciERC/CoNLL/FewNERD zero-shot | `server:output/72b_zeroshot/*/samples.jsonl` | ❌ need to retrieve |
| 72B few-shot samples | SciERC/CoNLL/FewNERD few-shot | `server:output/72b_fewshot/*/samples.jsonl` | ❌ need to retrieve |
| Temperature ablation samples | T={0.5,0.8,1.2} × 3 seeds | `server:output/exp_026_*/samples.jsonl` | ❌ need to retrieve |
| Free-form ablation samples | No JSON grammar constraint | `server:output/exp_freeform_*/samples.jsonl` | ❌ need to retrieve |
| LoRA rank=8 samples | SciERC rank=8 ablation | `server:output/exp_023_*/samples.jsonl` | ❌ need to retrieve |
| Qwen2.5-7B samples | FewNERD 3-seed | `server:output/exp_qwen25_7b_*/samples.jsonl` | ✅ have (DONE) |
| Qwen2.5-14B samples | FewNERD inference | `server:output/exp_qwen25_14b_*/samples.jsonl` | ⏳ pending (training 77.7%) |
| Qwen2.5-32B samples | FewNERD inference | `server:output/exp_qwen25_32b_*/samples.jsonl` | ⏳ pending (training 56.9%) |

## Missing / TODO

### Critical (must have before submission)
- [ ] **Training configs from server**: All LLamaFactory YAML configs need to be retrieved from `autodl-5090:/root/autodl-tmp/struct_self_consist_ie/`. At least 12 config files across model×dataset combinations.
- [ ] **14B/32B results**: Training still in progress. Need inference + signal computation + bootstrap after training completes.
- [ ] **Per-experiment signal reports**: Individual `full_signal_report.json` files from server (currently only aggregated results stored locally).

### Important (strongly recommended)
- [ ] **Raw samples.jsonl retrieval**: Raw model outputs per experiment. Large files (~50-200MB each) — consider providing representative subset or hosting on anonymous repo.
- [ ] **Data preprocessing scripts**: Scripts for SciERC/CoNLL/FewNERD data preparation (format conversion to LLamaFactory format).
- [ ] **README for supplementary**: Instructions for reproducing experiments (environment, execution order, expected outputs).

### Nice to have
- [ ] **Checkpoint/adapter weights**: LoRA adapter weights for key models (Qwen3-8B SciERC, LLaMA-3.1-8B SciERC). Large files — anonymous hosting needed.
- [ ] **WandB run logs**: Training loss curves and hyperparameter tracking.

## Summary Statistics

| Category | Have | Pending (14B/32B) | Missing/Need Retrieval |
|----------|------|--------------------|-----------------------|
| Core pipeline scripts | 5 | 0 | 0 |
| Construction & selection scripts | 8 | 0 | 0 |
| Analysis & aggregation scripts | 6 | 0 | 0 |
| Figure generation scripts | 3 | 0 | 0 |
| Verifier scripts | 4 | 0 | 0 |
| Training configs | 0 | 2 | 10 |
| Aggregated result JSONs | 19 | 0 | 0 |
| Per-experiment raw outputs | 1 | 2 | ~10 |
| **Total** | **46** | **4** | **~20** |
