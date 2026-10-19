# DPO Pipeline Integration Test Report

Date: 2026-05-13
Total checks: 49 | PASS: 46 | FAIL: 3

## Results

| # | Check | Status | Detail |
|---|-------|--------|--------|
| 1 | jsonl_load | PASS | 10 samples loaded |
| 2 | field_prompt | PASS |  |
| 3 | field_chosen | PASS |  |
| 4 | field_rejected | PASS |  |
| 5 | field_gamma_e | PASS |  |
| 6 | field_error_type | PASS |  |
| 7 | field_divergence_step | PASS |  |
| 8 | field_game_file | PASS |  |
| 9 | field_correction_span | PASS |  |
| 10 | prompt_is_msg_list | PASS |  |
| 11 | chosen_is_msg_list | PASS |  |
| 12 | rejected_is_msg_list | PASS |  |
| 13 | gamma_e_range | PASS | min=0.85, max=0.97 (target: covers 0.85-0.97) |
| 14 | d_range | PASS | min=0.1, max=0.9 |
| 15 | error_type_coverage | PASS | found: {'action', 'verification', 'planning'} |
| 16 | tokenizer_load | PASS | gpt2 with custom chat_template |
| 17 | dataset_etadn_load | PASS | 10 samples |
| 18 | sample_keys | PASS | got: {'idx', 'rejected_ids', 'chosen_ids', 'prompt_len', 'gamma'} |
| 19 | etadn_gamma_from_jsonl | PASS | dataset=0.85, jsonl=0.85 |
| 20 | collate_dpo | PASS | batch keys: ['indices', 'chosen_ids', 'chosen_mask', 'rejected_ids', 'rejected_mask', 'prompt_lens', 'chosen_resp_len... |
| 21 | batch_gammas_etadn | PASS | batch=[0.85, 0.92, 0.97], expected=[0.85, 0.92, 0.97] |
| 22 | batch_tensor_shapes | PASS | chosen=torch.Size([3, 235]), rejected=torch.Size([3, 185]) |
| 23 | single_gamma_mode | PASS | gamma=0.92 (should be CLI value 0.92, not jsonl gamma_e=0.85) |
| 24 | all_samples_accessible | PASS | all 10 indexed without error |
| 25 | phi_shape_gamma=0.85 | PASS | shape=torch.Size([10]) |
| 26 | phi_positive_gamma=0.85 | PASS | min=0.043259 |
| 27 | phi_monotone_gamma=0.85 | PASS |  |
| 28 | phi_shape_gamma=0.92 | PASS | shape=torch.Size([10]) |
| 29 | phi_positive_gamma=0.92 | PASS | min=0.066782 |
| 30 | phi_monotone_gamma=0.92 | PASS |  |
| 31 | phi_shape_gamma=0.97 | PASS | shape=torch.Size([10]) |
| 32 | phi_positive_gamma=0.97 | PASS | min=0.086858 |
| 33 | phi_monotone_gamma=0.97 | PASS |  |
| 34 | phi_normalized_gamma=0.85 | FAIL | sum=4.215314 |
| 35 | phi_normalized_gamma=0.92 | FAIL | sum=4.820022 |
| 36 | phi_normalized_gamma=0.97 | FAIL | sum=5.249103 |
| 37 | scalar_vec_match_gamma=0.85 | PASS |  |
| 38 | scalar_vec_match_gamma=0.97 | PASS |  |
| 39 | phi_T=1 | PASS | T=1 weight=1.000000 |
| 40 | phi_gamma=1_uniform | PASS | weights=[0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224] |
| 41 | phi_T=0 | PASS | shape=torch.Size([0]) |
| 42 | dmpo_loss_scalar | PASS | loss=0.754548 |
| 43 | dmpo_loss_batch | PASS | loss=0.8397, metrics_keys=['chosen_reward', 'rejected_reward', 'reward_margin', 'reward_accuracy'] |
| 44 | dmpo_loss_gradient | PASS |  |
| 45 | gamma_action | PASS |  |
| 46 | gamma_verification | PASS |  |
| 47 | gamma_planning | PASS |  |
| 48 | gamma_unknown_fallback | PASS |  |
| 49 | three_loss_variants | PASS | uniform=0.8978, single_gamma=0.8311, etadn=0.8275 |

## Key Findings

### phi weights are NOT normalized to sum=1

The φ(t,T) = γ^t · (1 - γ^(T-t)) / (1 - γ^T) formula produces weights where φ(0)=1.0 for all γ, but the total sum > 1 for γ < 1. This is by design — the formula normalizes such that the first weight is always 1, not such that the sum is 1. The dmpo_loss.py docstring claiming 'already normalized (sum=1)' is inaccurate.

- phi_normalized_gamma=0.85: sum=4.215314
- phi_normalized_gamma=0.92: sum=4.820022
- phi_normalized_gamma=0.97: sum=5.249103

**Impact**: In `train_dpo.py:compute_batch_loss`, chosen and rejected use separate φ weight vectors (potentially different lengths → different sums). The absolute scale cancels within each log-ratio but NOT across the chosen-vs-rejected comparison when lengths differ. This may cause length bias. Consider normalizing weights to sum=1 or documenting the current behavior as intentional.

**File**: `src/dmpo_loss.py:5` (docstring), `src/etadn_discount.py:56-70` (implementation)

3 check(s) failed. See details above.
