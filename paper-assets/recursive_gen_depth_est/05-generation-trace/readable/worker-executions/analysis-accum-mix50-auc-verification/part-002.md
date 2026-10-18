# analysis accum mix50 auc verification — Part 2 of 2

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../analysis-accum-mix50-auc-verification.md) · [Structured JSON](../../../sessions/a8/a845730c981fd63ddf20.json)

## Before a recorded user message

### Tool result

_source line 214 · 2026-05-22T08:15:06.353Z_

<details><summary>↩ Tool result · `toolu_01VbhAnYhD8Pjo5rhGqaUUX7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"method\\\": \\\"binary RF, 500 trees, 5-fold stratified CV, seed=42\\\",\\n  \\\"timestamp\\\": \\\"2026-05-22T16:14:01.403187\\\",\\n  \\\"results\\\": {\\n    \\\"gpt2xl_nuc_mix50\\\": {\\n      \\\"pairwise_auc_500tree\\\": {\\n        \\\"d0v1\\\": 0.9996,\\n        \\\"d1v2\\\": 0.8305,\\n        \\\"d2v3\\\": 0.6945\\n      },\\n      \\\"pairwise_auc_200tree\\\": {\\n        \\\"d0v1\\\": 0.9995,\\n        \\\"d1v2\\\": 0.8314,\\n        \\\"d2v3\\\": 0.6903\\n      },\\n      \\\"edd_T070\\\": 2,\\n      \\\"edd_T070_200tree\\\": 2\\n    },\\n    \\\"pythia_nuc_mix50\\\": {\\n      \\\"pairwise_auc_500tree\\\": {\\n        \\\"d0v1\\\": 0.9999,\\n        \\\"d1v2\\\": 0.7925,\\n        \\\"d2v3\\\": 0.7159\\n      },\\n      \\\"pairwise_auc_200tree\\\": {\\n        \\\"d0v1\\\": 0.9998,\\n        \\\"d1v2\\\": 0.7915,\\n        \\\"d2v3\\\": 0.7133\\n      },\\n      \\\"edd_T070\\\": 3,\\n      \\\"edd_T070_200tree\\\": 3\\n    },\\n    \\\"olmo_temp_mix50\\\": {\\n      \\\"pairwise_auc_500tree\\\": {\\n        \\\"d0v1\\\": 0.9999,\\n        \\\"d1v2\\\": 0.8166,\\n        \\\"d2v3\\\": 0.7262\\n      },\\n      \\\"pairwise_auc_200tree\\\": {\\n        \\\"d0v1\\\": 0.9999,\\n        \\\"d1v2\\\": 0.8162,\\n        \\\"d2v3\\\": 0.7223\\n      },\\n      \\\"edd_T070\\\": 3,\\n      \\\"edd_T070_200tree\\\": 3\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.12}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d4232873-36cc-4637-aa32-766dcf85d815",
  "uuid": "3e333d10-0a99-425c-a308-32e3a687b95d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"method\\\\\\\": \\\\\\\"binary RF, 500 trees, 5-fold stratified CV, seed=42\\\\\\\",\\\\n  \\\\\\\"timestamp\\\\\\\": \\\\\\\"2026-05-22T16:14:01.403187\\\\\\\",\\\\n  \\\\\\\"results\\\\\\\": {\\\\n    \\\\\\\"gpt2xl_nuc_mix50\\\\\\\": {\\\\n      \\\\\\\"pairwise_auc_500tree\\\\\\\": {\\\\n        \\\\\\\"d0v1\\\\\\\": 0.9996,\\\\n        \\\\\\\"d1v2\\\\\\\": 0.8305,\\\\n        \\\\\\\"d2v3\\\\\\\": 0.6945\\\\n      },\\\\n      \\\\\\\"pairwise_auc_200tree\\\\\\\": {\\\\n        \\\\\\\"d0v1\\\\\\\": 0.9995,\\\\n        \\\\\\\"d1v2\\\\\\\": 0.8314,\\\\n        \\\\\\\"d2v3\\\\\\\": 0.6903\\\\n      },\\\\n      \\\\\\\"edd_T070\\\\\\\": 2,\\\\n      \\\\\\\"edd_T070_200tree\\\\\\\": 2\\\\n    },\\\\n    \\\\\\\"pythia_nuc_mix50\\\\\\\": {\\\\n      \\\\\\\"pairwise_auc_500tree\\\\\\\": {\\\\n        \\\\\\\"d0v1\\\\\\\": 0.9999,\\\\n        \\\\\\\"d1v2\\\\\\\": 0.7925,\\\\n        \\\\\\\"d2v3\\\\\\\": 0.7159\\\\n      },\\\\n      \\\\\\\"pairwise_auc_200tree\\\\\\\": {\\\\n        \\\\\\\"d0v1\\\\\\\": 0.9998,\\\\n        \\\\\\\"d1v2\\\\\\\": 0.7915,\\\\n        \\\\\\\"d2v3\\\\\\\": 0.7133\\\\n      },\\\\n      \\\\\\\"edd_T070\\\\\\\": 3,\\\\n      \\\\\\\"edd_T070_200tree\\\\\\\": 3\\\\n    },\\\\n    \\\\\\\"olmo_temp_mix50\\\\\\\": {\\\\n      \\\\\\\"pairwise_auc_500tree\\\\\\\": {\\\\n        \\\\\\\"d0v1\\\\\\\": 0.9999,\\\\n        \\\\\\\"d1v2\\\\\\\": 0.8166,\\\\n        \\\\\\\"d2v3\\\\\\\": 0.7262\\\\n      },\\\\n      \\\\\\\"pairwise_auc_200tree\\\\\\\": {\\\\n        \\\\\\\"d0v1\\\\\\\": 0.9999,\\\\n        \\\\\\\"d1v2\\\\\\\": 0.8162,\\\\n        \\\\\\\"d2v3\\\\\\\": 0.7223\\\\n      },\\\\n      \\\\\\\"edd_T070\\\\\\\": 3,\\\\n      \\\\\\\"edd_T070_200tree\\\\\\\": 3\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.12}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"method\\\": \\\"binary RF, 500 trees, 5-fold stratified CV, seed=42\\\",\\n  \\\"timestamp\\\": \\\"2026-05-22T16:14:01.403187\\\",\\n  \\\"results\\\": {\\n    \\\"gpt2xl_nuc_mix50\\\": {\\n      \\\"pairwise_auc_500tree\\\": {\\n        \\\"d0v1\\\": 0.9996,\\n        \\\"d1v2\\\": 0.8305,\\n        \\\"d2v3\\\": 0.6945\\n      },\\n      \\\"pairwise_auc_200tree\\\": {\\n        \\\"d0v1\\\": 0.9995,\\n        \\\"d1v2\\\": 0.8314,\\n        \\\"d2v3\\\": 0.6903\\n      },\\n      \\\"edd_T070\\\": 2,\\n      \\\"edd_T070_200tree\\\": 2\\n    },\\n    \\\"pythia_nuc_mix50\\\": {\\n      \\\"pairwise_auc_500tree\\\": {\\n        \\\"d0v1\\\": 0.9999,\\n        \\\"d1v2\\\": 0.7925,\\n        \\\"d2v3\\\": 0.7159\\n      },\\n      \\\"pairwise_auc_200tree\\\": {\\n        \\\"d0v1\\\": 0.9998,\\n        \\\"d1v2\\\": 0.7915,\\n        \\\"d2v3\\\": 0.7133\\n      },\\n      \\\"edd_T070\\\": 3,\\n      \\\"edd_T070_200tree\\\": 3\\n    },\\n    \\\"olmo_temp_mix50\\\": {\\n      \\\"pairwise_auc_500tree\\\": {\\n        \\\"d0v1\\\": 0.9999,\\n        \\\"d1v2\\\": 0.8166,\\n        \\\"d2v3\\\": 0.7262\\n      },\\n      \\\"pairwise_auc_200tree\\\": {\\n        \\\"d0v1\\\": 0.9999,\\n        \\\"d1v2\\\": 0.8162,\\n        \\\"d2v3\\\": 0.7223\\n      },\\n      \\\"edd_T070\\\": 3,\\n      \\\"edd_T070_200tree\\\": 3\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.12}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 215_

现在并行更新 3 个 mix50 实验的 registry metrics，并查找实验 ID。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d4232873-36cc-4637-aa32-766dcf85d815",
  "uuid": "b1498cae-8a8e-4de7-9561-aae305a183c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DcV4QQxHgsTEyQ88jiNehf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2059,
      "cache_read_input_tokens": 94840,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2059
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 216_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01JbJxGwkxfYLPAwPfbMUWUB`</summary>

```json
{
  "filters": {
    "status": "DONE"
  },
  "project": "recursive_gen_depth_est",
  "limit": 0,
  "fields": [
    "exp_id",
    "status",
    "hypothesis"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d4232873-36cc-4637-aa32-766dcf85d815",
  "uuid": "59325e5e-94a0-4f39-8e46-c192223ef7a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DcV4QQxHgsTEyQ88jiNehf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2059,
      "cache_read_input_tokens": 94840,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2059
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 217 · 2026-05-22T08:15:11.979Z_

<details><summary>↩ Tool result · `toolu_01JbJxGwkxfYLPAwPfbMUWUB`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"wild_data_calibration_015\": {\"status\": \"DONE\", \"hypothesis\": \"RF depth estimator's wild-data FPR is consistent across diverse web corpora (C4, FineWeb, RedPajama) and can be reduced below 5% via P(d0) threshold adjustment with minimal recall loss, confirming the distribution shift is a calibration issue not a fundamental limitation.\"}, \"accum_olmo_temp_mix50\": {\"status\": \"DONE\", \"hypothesis\": \"OLMo-1B temp0.9 accumulation at 50% human mix ratio shows further depth signal degradation vs mix25 (73.47%), paralleling GPT-2 XL pattern (mix25 70.08% → mix50 69.05%) and Pythia pattern, confirming cross-model consistency of accumulation mixing effects\"}, \"accum_pythia_nuc_mix50\": {\"status\": \"DONE\", \"hypothesis\": \"Pythia-1.4B nucleus accumulation at 50% human mix ratio shows further signal degradation vs mix25 (70.77%), paralleling GPT-2 XL pattern (mix25 70.08% → mix50 69.05%)\"}, \"conditional_pi_001\": {\"status\": \"DONE\", \"hypothesis\": \"Perplexity tail features (p90_ppl, kurtosis_ppl, var_ppl, etc.) remain the top-ranked feature family under permutation importance (not Gini), with stable bootstrap rank CIs across all 9 model-strategy cells, refuting R17's concern that VIF>10 collinearity invalidates importance rankings.\"}, \"conditional_pi_002\": {\"status\": \"DONE\", \"hypothesis\": \"Perplexity tail features (p90_ppl, var_surprisal, kurt_ppl) remain the top family under conditional permutation importance with Random Forest, even after controlling for inter-feature correlation across all 9 model×strategy cells.\"}, \"accum_pythia_nuc_002\": {\"status\": \"DONE\", \"hypothesis\": \"Accumulation scenario with Pythia-1.4B nucleus sampling shows comparable depth signal degradation pattern to GPT-2 XL nucleus (accum_v3): mix25 ~70% and mix50 ~69%, confirming cross-model consistency of accumulation effects on depth estimation. Retry of accum_pythia_nuc_001 (failed due to cuda:1 not existing).\"}, \"accum_olmo_temp_001\": {\"status\": \"DONE\", \"hypothesis\": \"Accumulation scenario with OLMo-1B temp0.9 shows comparable depth signal degradation pattern to GPT-2 XL nucleus (accum_v3), confirming cross-strategy consistency of accumulation effects on depth estimation\"}, \"accum_pythia_nuc_001\": {\"status\": \"DONE\", \"hypothesis\": \"Accumulation scenario with Pythia-1.4B nucleus sampling shows comparable depth signal degradation pattern to GPT-2 XL nucleus (accum_v3): mix25 ~70% and mix50 ~69%, confirming cross-model consistency of accumulation effects on depth estimation\"}, \"14b_cross_ref_001\": {\"status\": \"DONE\", \"hypothesis\": \"Cross-reference control: using Pythia-1.4B (same as Table 1 pipeline) instead of self-reference (Qwen2.5-14B) for feature extraction on 14B generated text yields comparable classification accuracy, confirming that the reference model choice does not fundamentally change the depth signal detection at 14B scale. Addresses R17 concern about self-reference vs cross-reference consistency.\"}, \"fpr_coverage_001\": {\"status\": \"DONE\", \"hypothesis\": \"Confidence thresholding on RF max_prob can reduce C4 FPR substantially while maintaining reasonable coverage, providing a practical operating point for deployment where users can trade coverage for lower false positive rates.\"}, \"binoculars_14b_topk50\": {\"status\": \"DONE\", \"hypothesis\": \"Binoculars cross-perplexity features provide complementary signal at 14B scale under top-k sampling when merged with 19 statistical features. Tests whether the merged feature gain (~+3.7pp at temp09) holds under the weakest decoding strategy.\"}, \"qwen25_14b_topk50\": {\"status\": \"DONE\", \"hypothesis\": \"Recursive generation depth signal persists at 14B scale under top-k sampling (k=50), achieving RF 4-class accuracy above 25% baseline. Top-k typically yields lowest accuracy across strategies; if signal persists even here, 14B scale-generality claim is robust. Directly addresses Dream worst review M3.\"}, \"binoculars_14b_temp09\": {\"status\": \"DONE\", \"hypothesis\": \"Binoculars cross-perplexity features provide complementary signal at 14B scale when merged with 19 statistical features, yielding accuracy above stat-only baseline. Tests whether cross-model divergence channel persists at larger scale.\"}, \"qwen25_14b_temp09\": {\"status\": \"DONE\", \"hypothesis\": \"Recursive generation depth signal persists at 14B scale under temperature sampling (τ=0.9), achieving RF 4-class accuracy above 25% baseline and comparable to scale_002 nucleus (54.05%). Validates Claim 2: Atlas spans 3 strategies at 14B. Directly addresses Dream worst review M3 \\\"14B too narrow\\\".\"}, \"feature_ablation_merged_001\": {\"status\": \"DONE\", \"hypothesis\": \"Merging our 19 statistical features with 11 Binoculars cross-perplexity features (30 total) should reveal whether the two feature sets provide complementary depth signal. If merged RF >80%, the cross-model transfer signal from Binoculars adds value beyond our features (answers reviewer \\\"why not merge?\\\"). If merged RF ≈ 78%, signal is saturated and both feature sets are redundant — depth information ceiling is ~78% on these features.\"}, \"feature_ablation_overlap_001\": {\"status\": \"DONE\", \"hypothesis\": \"The 6 overlapping features between Binoculars and our 19-feature set (ppl_mean, ppl_var, ppl_median, p10_ppl, p90_ppl, skewness_ppl) capture the core depth signal. If 6-feature RF ≈ 78%, the overlap features alone are sufficient and shape features add negligible value. If 6-feature RF significantly < 78%, the remaining shape features (var_surprisal, kurtosis, etc.) have independent discriminative contribution beyond mean-level displacement.\"}, \"binoculars_ordinal_baseline_001\": {\"status\": \"DONE\", \"hypothesis\": \"Binoculars (Hans et al., ICML 2024) cross-perplexity scores (observer=pythia-1.4b, performer=pythia-410m), when calibrated to 4-class ordinal depth, achieve near-chance accuracy on 9-cell atlas. Binoculars is binary detection SOTA; testing it is critical for completeness. Reviewer will ask \\\"did you test Binoculars?\\\"\"}, \"detectgpt_ordinal_baseline_004\": {\"status\": \"DONE\", \"hypothesis\": \"DetectGPT perturbation discrepancy scores on pythia_nucleus cell achieve near-chance 4-class ordinal accuracy, completing the 9/9 cell coverage. Extends detectgpt_ordinal_baseline_002 (8/9 cells, 29.1%) with the missing pythia_nucleus cell. Script fixed with cell→directory mapping for pythia_nucleus (\\\".\\\").\"}, \"detectgpt_ordinal_baseline_003\": {\"status\": \"DONE\", \"hypothesis\": \"Fast-DetectGPT (Mitchell et al. 2023) perturbation discrepancy scores, when calibrated to 4-class ordinal depth via equal-width/CORAL/threshold methods, achieve near-chance accuracy on full 9-cell atlas. Extends detectgpt_ordinal_baseline_002 (8/9 cells, 29.1%) to include pythia_nucleus. Confirms perturbation-based binary detection lacks ordinal resolution.\"}, \"deberta_pilot_pythia_temp09\": {\"status\": \"DONE\", \"hypothesis\": \"DeBERTa-v3-base (LoRA) end-to-end 4-class depth classification on pythia_temp09 cell achieves lower accuracy than RF+19-feature baseline, confirming cross-model generality of \\\"simple features beat neural\\\" finding. Paired with gpt2xl_temp09 pilot to cover both strong and weak atlas cells.\"}, \"deberta_pilot_gpt2xl_temp09\": {\"status\": \"DONE\", \"hypothesis\": \"DeBERTa-v3-base (LoRA) end-to-end 4-class depth classification on gpt2xl_temp09 cell achieves lower accuracy than RF+19-feature baseline (78.2%), demonstrating that hand-crafted perplexity-distribution features capture depth signal more effectively than neural text representations. Addresses reviewer concern \\\"RF has no algorithmic contribution\\\" — if RF ≥ DeBERTa, \\\"simple features beat neural\\\" is a paper insight.\"}, \"mink_ordinal_baseline_002\": {\"status\": \"DONE\", \"hypothesis\": \"Min-K% Prob (Shi et al. 2024) continuous membership-inference scores, when calibrated to 4-class ordinal depth via equal-width/CORAL/threshold methods, achieve near-chance accuracy (30-35%) on 9-cell atlas. Establishes that binary detection scores lack ordinal depth resolution. Rebuttal ammunition against \\\"did you test Min-K% for ordinal?\\\"\"}, \"detectgpt_ordinal_baseline_001\": {\"status\": \"DONE\", \"hypothesis\": \"DetectGPT (Mitchell et al. 2023) perturbation discrepancy scores, when calibrated to 4-class ordinal depth via equal-width/CORAL/threshold methods, achieve near-chance accuracy (30-35%) on 9-cell atlas. Establishes that perturbation-based binary detection lacks ordinal resolution. Rebuttal ammunition against \\\"binary detectors might also detect depth.\\\"\"}, \"mink_ordinal_baseline_001\": {\"status\": \"DONE\", \"hypothesis\": \"Min-K% Prob (Shi et al. 2024) continuous membership-inference scores, when calibrated to 4-class ordinal depth via equal-width/CORAL/threshold methods, achieve near-chance accuracy (30-35%) on 9-cell atlas. Establishes that binary detection scores lack ordinal depth resolution. Rebuttal ammunition against \\\"did you test Min-K% for ordinal?\\\"\"}, \"detectgpt_ordinal_baseline_002\": {\"status\": \"DONE\", \"hypothesis\": \"DetectGPT (Mitchell et al., 2023) perturbation discrepancy scores, when calibrated to 4-class ordinal depth via equal-width/CORAL/threshold methods, achieve near-chance accuracy (~29%) on 8/9 atlas cells. Fast-DetectGPT (Bao et al., 2024) is a strictly stronger baseline; if even original DetectGPT fails at ordinal depth, Fast-DetectGPT would perform no better. Establishes that perturbation-based binary detection lacks ordinal resolution.\"}, \"cross_strategy_dann_001\": {\"status\": \"DONE\", \"hypothesis\": \"DANN (Domain-Adversarial Neural Network) learns strategy-invariant feature representations via gradient reversal, improving cross-strategy LOSO depth classification from naive RF 59.1% and two-stage 70.5% to 73-75%+. The shared encoder + adversarial strategy discriminator forces the model to extract depth-discriminative features that are invariant to decoding strategy differences. If delta vs two-stage >= 3pp, becomes main method contribution in §3.\"}, \"accum_v3_mix25\": {\"status\": \"DONE\", \"hypothesis\": \"Under 25/75 accumulation (mixing 25% human + 75% previous-depth synthetic text at each depth, then LoRA fine-tune + generate), depth signal attenuates to ~70% compared to full-replacement (84.2%). Comparable to mix50 (~69%, 1pp difference within seed noise of 2.04pp). Together with mix50, establishes accumulation degradation magnitude for Discussion §6.\"}, \"accum_v3_mix50\": {\"status\": \"DONE\", \"hypothesis\": \"Under 50/50 accumulation (mixing 50% human + 50% previous-depth synthetic text at each depth, then LoRA fine-tune + generate), depth signal attenuates to ~69% compared to full-replacement (84.2%), establishing that full-replacement results are a ceiling. Comparable to mix25 (~70%, within seed noise). Quantifies accumulation degradation for Discussion §6. Parent: invalidated accum_mix50 (feature-space mixing error).\"}, \"accum_mix50\": {\"status\": \"DONE\", \"hypothesis\": \"Accumulation scenario (50% human + 50% synthetic per depth) will degrade RF 4-class accuracy below full-replacement (84.2%), confirming that full-replacement results are an upper bound on feature separability. The degradation magnitude quantifies how much human-text mixing attenuates the depth signal.\"}, \"accum_mix25\": {\"status\": \"DONE\", \"hypothesis\": \"Accumulation scenario (25% human + 75% synthetic per depth) will show intermediate degradation between full-replacement (84.2%) and 50/50 mix, establishing a degradation curve that characterizes how human-text proportion affects depth separability.\"}, \"coral_ordinal_9cell_001\": {\"status\": \"DONE\", \"hypothesis\": \"CORAL ordinal regression with DNN backbone (19→64→32→CORAL) achieves comparable or superior 4-class accuracy to RF on all 9 atlas cells, while providing better ordinal consistency (monotonic predictions) and lower MAE due to ordinal-aware loss. Prior baseline_battery_9cell_001 showed RF≈CORAL with simple CORAL; DNN backbone may widen the gap. Algorithmic contribution: ordinal-specific classifier for depth estimation.\"}, \"lr_zscore_cross_strategy_001\": {\"status\": \"DONE\", \"hypothesis\": \"LR cross-strategy LOO + z-score: 验证 paper_framing 声称的 z-score 恢复 LR d1v2 AUC（GPT-2 XL 0.13→0.68, OLMo 0.25→0.83）。论文 claim 硬依赖。\"}, \"rf_21feature_augmented_001\": {\"status\": \"DONE\", \"hypothesis\": \"Adding Min-K% Prob and DetectGPT scores to the 19 statistical features will either show redundancy (detection scores add no info beyond statistical features) or complementarity (detection scores capture unique signal), both outcomes strengthen the paper narrative\"}, \"qwen25_14b_scale_003\": {\"status\": \"DONE\", \"hypothesis\": \"14B scale validation reproducibility: Qwen2.5-14B FP16 recursive chain on westd-48862 (RTX PRO 6000 Blackwell) produces consistent depth signal with gpu-6000pro-2 run, confirming results are not hardware-dependent.\"}, \"d4_extension_olmo_001\": {\"status\": \"DONE\", \"hypothesis\": \"OLMo-1B nucleus d4 depth extension: recursive generation depth signal persists at d4, completing 3/3 model coverage for EDD >= 4 verification.\"}, \"d4_extension_pythia_001\": {\"status\": \"DONE\", \"hypothesis\": \"Pythia-1.4B nucleus d4 depth extension: recursive generation depth signal persists at d4, providing second model evidence for EDD >= 4. d3v4 pairwise AUC > 0.70, 5-class RF accuracy well above 20% chance.\"}, \"d4_extension_gpt2xl_001\": {\"status\": \"DONE\", \"hypothesis\": \"GPT-2 XL nucleus d4 depth extension: recursive generation depth signal persists at d4 (5th recursive iteration). 5-class RF (d0-d4) accuracy remains significantly above 20% chance level, d3-vs-d4 pairwise AUC > 0.6, and key features (p90_ppl, var_surprisal, mean_ppl) continue monotonic trends observed in d0-d3.\"}, \"qwen25_14b_scale_002\": {\"status\": \"DONE\", \"hypothesis\": \"Recursive generation depth signal (statistical features distinguishing d0-d3) persists at 14B parameter scale (Qwen2.5-14B FP16), achieving RF 4-class accuracy significantly above 25% baseline, validating that model collapse signatures are not artifacts of small model capacity.\"}, \"olmo_seed43_001\": {\"status\": \"DONE\", \"hypothesis\": \"OLMo-1B with seed=43 and nucleus sampling (p=0.95) will reproduce the recursive generation depth signal (d0-d3 classification accuracy) observed in prior seeds, validating cross-seed reproducibility for the OLMo model family.\"}, \"pythia_seed43_001\": {\"status\": \"DONE\", \"hypothesis\": \"Pythia-1.4B recursive generation chain with seed=43 will produce depth-discriminative statistical features comparable to seed=42 (83.3% 4-class RF accuracy), confirming depth signal is inherent to recursive process not seed-specific.\"}, \"gpt2xl_seed43_001\": {\"status\": \"DONE\", \"hypothesis\": \"GPT-2 XL recursive generation depth signal is reproducible across random seeds: seed=43 should yield 4-class RF accuracy within 5pp of seed=42 baseline (83.3%), confirming depth degradation is inherent to the recursive fine-tuning process rather than LoRA weight initialization.\"}, \"prompted_gen_gpt2xl_001\": {\"status\": \"DONE\", \"hypothesis\": \"Prompted generation preserves depth signal: GPT-2 XL topic-prompted 4-class acc >= 70%, delta <= 15pp vs BOS-seeded baseline (83.3%)\"}, \"qwen25-1p5b-instruct-001\": {\"status\": \"DONE\", \"hypothesis\": \"Depth signal persists in instruction-tuned models: Qwen2.5-1.5B-Instruct recursive chain (nucleus p=0.95, d0-d3) achieves RF 4-class accuracy significantly above 25% baseline, demonstrating that instruction tuning does not eliminate model collapse signatures.\"}, \"learned_estimator_001\": {\"status\": \"DONE\", \"hypothesis\": \"Statistical features (19-dimensional: perplexity stats, surprisal, n-gram entropy, repetition ratios) can predict generation depth (0-3) with over 70% accuracy using learned classifiers (ordinal MLP, prototypical networks, XGBoost), and this generalizes across models in leave-one-out evaluation, because recursive generation progressively degrades text quality in statistically measurable ways.\"}, \"downstream_benchmark_001\": {\"status\": \"DONE\", \"hypothesis\": \"Depth-filtered training data (strict subset: depth 0-1 only) will produce better fine-tuned models than unfiltered or random data, because lower-depth text contains more original content with cleaner training signal, leading to lower perplexity on held-out evaluation after LoRA fine-tuning of Pythia-410M.\"}, \"qwen25-1p5b-instruct-002\": {\"status\": \"DONE\"}, \"qwen25-1p5b-instruct-001-ph45v3\": {\"status\": \"DONE\"}, \"qwen25-1p5b-instruct-001-ph45v2\": {\"status\": \"DONE\"}, \"qwen25-1p5b-instruct-001-ph45\": {\"status\": \"DONE\"}, \"qwen25-1p5b-instruct-001-phase45\": {\"status\": \"DONE\"}, \"learned_estimator_002\": {\"status\": \"DONE\", \"hypothesis\": \"Fixing NaN issues in Prototypical Network (torch.clamp + nan_to_num in distances, safe softmax conversion) and running full data sweep (no max_samples limit) will enable learned estimators (XGBoost, CORAL MLP, Prototypical) to exceed the RF baseline of 66.4% accuracy in cross-model depth estimation.\"}, \"wild_data_features_001\": {\"status\": \"DONE\", \"hypothesis\": \"Wild web corpora (C4, FineWeb) contain measurable proportions of text classified as recursive-generation depth d1+ by our RF estimator, providing evidence that model-generated text is present in training data.\"}, \"downstream_benchmark_002\": {\"status\": \"DONE\", \"hypothesis\": \"Fine-tuning on depth-0 (original) text produces lower held-out perplexity than fine-tuning on higher-depth (recursive) text, because d0 data has higher quality signal without recursive degradation artifacts.\"}, \"learned_estimator_proto_fix_001\": {\"status\": \"DONE\", \"hypothesis\": \"Prototypical Network with NaN fix (torch.clamp + nan_to_num on distance computation) achieves ~67.1% leave-one-model-out accuracy on 19 statistical features, comparable to RF baseline (66.4%), completing the learned estimator comparison matrix.\"}, \"detector_ord_baseline_001\": {\"status\": \"DONE\", \"hypothesis\": \"Existing AI-text detectors (Binoculars, Fast-DetectGPT) calibrated for ordinal depth estimation perform worse than our RF-on-19-features approach, confirming that depth-specific statistical features capture information beyond generic detection scores.\"}, \"plan_018_binoculars_baseline\": {\"status\": \"DONE\"}, \"bootstrap_ci_table1_001\": {\"status\": \"DONE\", \"hypothesis\": \"Bootstrap 95% CIs for all 9 cells of the 3×3 core matrix (3 models × 3 strategies) confirm that RF accuracy point estimates are stable (CI width ~1pp), and RF significantly outperforms LR in 8/9 cells.\"}, \"text_length_sensitivity_001\": {\"status\": \"DONE\", \"hypothesis\": \"Depth estimation accuracy degrades gracefully with shorter text truncation because the key statistical features (surprisal moments, entropy) converge within the first 100-200 tokens, making the method practical for short-text scenarios.\"}, \"qwen25_14b_scale_001\": {\"status\": \"DONE\", \"hypothesis\": \"Recursive generation depth signal (statistical features distinguishing d0-d3) persists at 14B parameter scale (Qwen2.5-14B FP16), achieving RF 4-class accuracy significantly above 25% baseline, validating that model collapse signatures are not artifacts of small model capacity.\"}, \"mlp_19feat_001\": {\"status\": \"DONE\", \"hypothesis\": \"2-layer MLP on 19 features achieves similar accuracy to RF (delta <= 3pp), confirming features rather than classifier as the performance bottleneck\"}, \"cross_strategy_pipeline_001\": {\"status\": \"DONE\", \"hypothesis\": \"Strategy classifier achieves >90% accuracy on 19 statistical features; two-stage pipeline (predict strategy then route to per-strategy depth RF) recovers cross-strategy depth accuracy to >=70% vs naive LOO 59.1%\"}, \"gen_length_ablation_001\": {\"status\": \"DONE\", \"hypothesis\": \"Depth signal scales with passage length: 128-token passages are detectable but weaker; 512-token passages match 256-token baseline; cross-length accuracy spread ≤ 5pp\"}, \"cross_seed_transfer_001\": {\"status\": \"DONE\", \"hypothesis\": \"If depth signal is an inherent property of recursive generation, an RF trained on seed=42 features should generalize to seed=43 features with cross-seed acc ≥ 75% (Δ ≤ 3pp vs within-seed)\"}, \"mixed_depth_corpus_001\": {\"status\": \"DONE\", \"hypothesis\": \"RF per-sample classifier does not rely on corpus-level depth distribution prior; accuracy on mixed-depth corpus (50/30/15/5%) should match balanced baseline within Δ ≤ 2pp\"}, \"ensemble_reference_001\": {\"status\": \"DONE\", \"hypothesis\": \"Ensemble reference (mean surprisal across multiple ref models) improves robustness vs worst single-model reference; ensemble acc should exceed GPT-2 XL-only (67.3%) by ≥5pp\"}, \"second_seed_replication_001\": {\"status\": \"DONE\", \"hypothesis\": \"递归生成 depth signal 是 recursive process 的固有属性而非特定 LoRA 权重的 idiosyncrasy；用不同 seed(=43) 训练的 LoRA 应产生与 seed=42 一致的 depth fingerprint（accuracy Δ ≤ 3pp vs 78.2%）\"}, \"reference_free_baseline_001\": {\"status\": \"DONE\", \"hypothesis\": \"Depth signal is partially accessible without reference model: reference-free token statistics (TTR, repetition, entropy, sentence length) achieve >60% 4-class accuracy (>2.5x chance)\"}, \"feat_ablation_v1\": {\"status\": \"DONE\", \"hypothesis\": \"A small subset of surprisal features (top-5 by RF importance) captures most depth signal: top-5 acc ≥95% of full 19-feature accuracy, identifying the minimal sufficient feature set for depth estimation\"}, \"feature_ablation_9cell\": {\"status\": \"DONE\", \"hypothesis\": \"Top-5 surprisal features achieve ≥90% of full 19-feature accuracy across all 9 atlas cells, confirming a minimal sufficient feature set independent of model/strategy combination\"}, \"depth_extension_olmo_d4d5_002\": {\"status\": \"DONE\", \"hypothesis\": \"OLMo-1B EDD 与 Pythia-1.4B 一致（EDD=4），验证 EDD 跨模型稳定性\"}, \"wild_data_calibration_005\": {\"status\": \"DONE\", \"hypothesis\": \"RedPajama web-crawl text is classified as d0 with FPR≤25%, consistent with C4/FineWeb calibration patterns, confirming cross-corpus robustness of depth classifier on diverse web data\"}, \"wild_data_calibration_004\": {\"status\": \"DONE\", \"hypothesis\": \"OpenWebText curated web text is classified as d0 with near-zero FPR (≤5%), confirming editorial curation quality correlates with lower false positive rates vs raw web-crawl\"}, \"gpt2xl_ref_ablation_001\": {\"status\": \"DONE\"}, \"ref_model_ablation_001\": {\"status\": \"DONE\", \"hypothesis\": \"OLMo-1B as alternative reference model yields depth classification within ±5pp of Pythia-1.4B reference, confirming surprisal-based features are not specific to a matched Pythia architecture\"}, \"baseline_battery_001\": {\"status\": \"DONE\", \"hypothesis\": \"Multiple classifier families (RF/LR/CORAL/CE-MLP/DivEye/PPL-Reg) achieve >40% 4-class accuracy on surprisal features, confirming depth signal is classifier-agnostic and not specific to RF decision boundaries\"}, \"batch_feature_extraction_5cells\": {\"status\": \"DONE\", \"hypothesis\": \"Feature extraction pipeline produces consistent 19-dim feature vectors across 5 new cells (GPT-2 XL + OLMo × 3 strategies), enabling downstream cross-model/cross-strategy generalization analysis\"}, \"cross_model_loo_v1\": {\"status\": \"DONE\", \"hypothesis\": \"RF trained on depth features from 2 generator models generalizes to held-out 3rd model with acc>50% (chance=25%), confirming depth features encode model-agnostic recursive degradation patterns\"}, \"cross_scale_llama3_8b_003\": {\"status\": \"DONE\", \"hypothesis\": \"Llama-3.1-8B-Instruct preserves monotonic AUC decay with EDD≥4 at 8B scale, confirming depth signal generalizes beyond 1-1.5B models to production-scale LLMs\"}, \"lora_rank_ablation_001\": {\"status\": \"DONE\", \"hypothesis\": \"LoRA rank (r∈{4,16,64}) minimally affects depth signal: accuracy spread ≤5pp across ranks would confirm depth signal is not an artifact of a specific LoRA fine-tuning configuration\"}, \"cross_scale_llama3_base_001\": {\"status\": \"DONE\"}, \"cross_model_reverse_chain_001\": {\"status\": \"DONE\"}, \"cross_scale_qwen7b_001\": {\"status\": \"DONE\", \"hypothesis\": \"Plan_014 7B cross-scale probe: Qwen2.5-7B nucleus p=0.95, d0-d5, 500 samples/depth。验证 depth signal 和 EDD 在 7B scale 上是否与 1-1.5B 模型一致。成功标准：4-class acc ≥ 60%, EDD 测定, pairwise AUC 衰减趋势方向一致。\"}, \"domain_extension_001\": {\"status\": \"DONE\", \"hypothesis\": \"Domain extension: 用 arXiv abstracts 替代 WikiText 作为 seed，验证 depth signal 是否 domain-independent。成功标准：4-class acc ≥ 65%, top features 与 WikiText pipeline 一致。\"}, \"cross_scale_llama3_8b_002\": {\"status\": \"DONE\"}, \"cross_model_recursive_chain_002\": {\"status\": \"DONE\"}, \"cross_model_recursive_chain_001\": {\"status\": \"DONE\", \"hypothesis\": \"Cross-model recursive chain: Human→Pythia d1→OLMo finetune→GPT-2 XL finetune。验证 depth signal 是否能跨越模型边界累积——即使每一步用不同模型递归，distributional artifacts 仍然可检测。成功标准：chain-d2/d3 的 pairwise AUC > chance, 4-class acc ≥ 50%。\"}, \"cross_scale_llama3_8b_001\": {\"status\": \"DONE\", \"hypothesis\": \"7B cross-scale probe (Llama-3-8B): 验证 depth signal 在 Llama-3 架构上的可检测性。Nucleus p=0.95, d0-d5, 500 samples/depth。成功标准：4-class acc ≥ 60%, EDD 测定, pairwise AUC 衰减趋势与 1-1.5B 模型方向一致。\"}, \"two_stage_strategy_pipeline_001\": {\"status\": \"DONE\", \"hypothesis\": \"Two-stage pipeline: 先分类 decoding strategy，再用 strategy-conditioned depth classifier。验证 Discussion 中提出的 two-stage 方案的可行性和瓶颈。\"}, \"multi_tau_ablation_001\": {\"status\": \"DONE\", \"hypothesis\": \"R2-W3 multi-τ ablation: 4 τ values (0.5, 0.7, 0.9, 1.1) × Pythia-1.4B。验证 depth classification signal 跨温度的鲁棒性，特别是 d1v2 AUC 是否随 τ 单调变化或在特定 τ 出现 inversion。Cross-τ LOO 验证跨温度泛化能力。\"}, \"zeroshot_qwen7b_500_001\": {\"status\": \"DONE\", \"hypothesis\": \"R1-W4 第二个 LLM baseline：Qwen2.5-7B-Instruct 4-bit zero-shot depth classification。与 DeepSeek-v3.2 (36.2%) 对比，验证 LLM zero-shot 在 depth task 上的一般性劣势（vs RF 78.2%）。\"}, \"wild_data_calibration_003\": {\"status\": \"DONE\", \"hypothesis\": \"Wild data calibration v3: 离线方案。先下载 RedPajama/Dolma 到本地磁盘，再用 wild_data_calibration_001 的 RF 模型评估 FPR。验证论文 wild-text calibration 在更多数据源上的泛化。\"}, \"wild_data_calibration_002\": {\"status\": \"DONE\"}, \"wild_data_redpajama_dolma_001\": {\"status\": \"DONE\"}, \"wild_data_calibration_001\": {\"status\": \"DONE\", \"hypothesis\": \"Classifiers trained on recursive generation data should correctly classify wild (human) text as d0 with low FPR, confirming calibration on out-of-distribution natural text\"}, \"random_soft_control_001\": {\"status\": \"DONE\"}, \"downstream_curation_poc_001\": {\"status\": \"DONE\"}, \"wild_data_olmo_calibration_001\": {\"status\": \"DONE\"}, \"pythia7b_cross_scale_001\": {\"status\": \"DONE\"}, \"wild_data_gpt2xl_calibration_001\": {\"status\": \"DONE\"}, \"wild_data_c4_supplement_001\": {\"status\": \"DONE\"}, \"w2_domain_bias_001\": {\"status\": \"DONE\"}, \"xgboost_lgbm_3cell_001\": {\"status\": \"DONE\"}, \"xgboost_lgbm_baseline_001\": {\"status\": \"DONE\"}, \"shap_supplement_001\": {\"status\": \"DONE\"}, \"zeroshot_llm_500_001\": {\"status\": \"DONE\", \"hypothesis\": \"R1-W4 zero-shot 样本量扩展: 从 200→500 samples 缩窄 CI。当前 200 samples 的 CI 过宽，500 samples 可将 CI 宽度缩小 ~37%，更可靠地与 RF 78.2% 对比。\"}, \"temp07_pilot_pythia_001\": {\"status\": \"DONE\", \"hypothesis\": \"R2-W3 multi-τ: τ=0.7 temperature pilot with Pythia-1.4B. 验证 d1v2 inversion 是否在 τ=0.7 也出现（对比 τ=0.9 的 GPT-2 XL 0.129 / OLMo 0.253）。若出现则 temperature inversion 是 τ<1 的通用现象；若不出现则 τ=0.9 是边界条件。\"}, \"n2_roberta_finetune_001\": {\"status\": \"DONE\", \"hypothesis\": \"N2 reviewer concern: end-to-end RoBERTa-base finetune baseline vs RF on hand-crafted features (78.2%). 与 DeBERTa 形成双 backbone 对比，排除模型选择偏差。\"}, \"n2_deberta_finetune_001\": {\"status\": \"DONE\", \"hypothesis\": \"N2 reviewer concern: end-to-end DeBERTa-v3-base finetune baseline vs RF on hand-crafted features (78.2%). 若 DeBERTa acc < RF，证明手工特征确有独立贡献；若 ≥ RF，需重新定位 narrative。\"}, \"cross_strategy_loo_001\": {\"status\": \"DONE\", \"hypothesis\": \"Cross-strategy LOO (plan_007): 深度信号跨策略可迁移——同模型内，用 2 种解码策略训练的 RF 可泛化到第 3 种，4-class acc 均值 59.1% 远超 chance 25%。temp09 holdout 的 d1v2 AUC 反转 (GPT-2 XL: 0.13, OLMo: 0.25) 证明解码策略塑造不同的退化轨迹 (D014)\"}, \"depth_extension_gpt2xl_d4d5_001\": {\"status\": \"DONE\", \"hypothesis\": \"GPT-2 XL depth extension: 从 d3 checkpoint 继续递归生成 d4/d5 各 5000 samples，binary pairwise RF 验证 EDD。GPT-2 XL 是 3×3 矩阵中信号最强的模型 (85.4%)，若 EDD≥4 则与 Pythia 结果 (EDD=4) 形成跨模型 EDD 一致性证据。\"}, \"depth_extension_olmo_d4d5_001\": {\"status\": \"DONE\", \"hypothesis\": \"OLMo-1B depth extension: 从 d3 checkpoint 继续递归生成 d4/d5 各 5000 samples，binary pairwise RF 验证 EDD。OLMo 是 3×3 矩阵中间模型 (78.8%)，若 EDD≥4 则与 Pythia (EDD=4) 形成跨模型 EDD 一致性证据，3 模型 EDD 完整对比。\"}, \"granularity_ablation_rf_001\": {\"status\": \"DONE\", \"hypothesis\": \"Granularity ablation: 对比 binary/3-class/4-class/6-class RF 性能，量化分类粒度对决策边界稀释的影响。预期 accuracy 随粒度增加单调下降，adjacent-pair AUC 在 binary 设置下最高。支持 Claim 1 (feasibility) + Claim 2 (EDD boundary dilution)。\"}, \"zero_shot_llm_baseline_001\": {\"status\": \"DONE\", \"hypothesis\": \"Zero-shot LLM baseline: DeepSeek V3.2 直接判断文本递归生成深度 (4-class)，无需统计特征提取。作为 upper-bound baseline 对比 feature-based 方法。\"}, \"olmo_temp09_002\": {\"status\": \"DONE\", \"hypothesis\": \"解码策略鲁棒性: OLMo-1B 在 temperature-only τ=0.9 下递归生成的深度信号与 nucleus p=0.95 一致（olmo_temp09_001 重跑，从 Step 3 断点恢复）\"}, \"depth_extension_pythia_d4d5_001\": {\"status\": \"DONE\", \"hypothesis\": \"Depth extension to d4/d5: EDD 从 d3 (当前 EDD=3 未饱和) 继续延伸——如果 d3v4 和 d4v5 AUC 仍 >0.75，则 EDD≥5，证明递归深度信号至少在 5 代内不饱和\"}, \"depth_extension_binary_pairwise_002\": {\"status\": \"DONE\", \"hypothesis\": \"Retry of binary_pairwise_001 (failed due to missing script on server). Dedicated binary RF for d3v4 and d4v5 pairwise AUC. Judgment: d3v4>0.75 + d4v5>0.75 → EDD≥5; d3v4>0.75 only → EDD=4.\"}, \"depth_extension_binary_pairwise_001\": {\"status\": \"DONE\", \"hypothesis\": \"Dedicated binary pairwise RF 评估 d3v4 和 d4v5 可区分性。6-class RF 的 pairwise AUC 因决策边界稀释不可靠（d2v3 从 4-class 0.80 降到 0.69 是 artifact）。Binary classifier 消除此 artifact，与原 4-class pipeline 的 d0v1/d1v2/d2v3 AUC 可比。判定标准：binary d3v4 AUC > 0.75 且 d4v5 AUC > 0.75 → EDD≥5；d3v4 > 0.75 但 d4v5 < 0.75 → EDD=4。\"}, \"dcol_roberta_v6_001\": {\"status\": \"DONE\", \"hypothesis\": \"DCOL v6: RoBERTa-large 替代 DeBERTa 解决数值不稳定。lr=5e-5 + grad clip 1.0 + NaN guard + collapse guard (step 500 acc&lt;30% kill)。若 4-class acc > RF baseline (78.2%) 则 DCOL 成功，否则降级为 negative result。\"}, \"cross_strategy_loo_zscore_001\": {\"status\": \"DONE\", \"hypothesis\": \"Z-score standardization recovers temp09 d1v2 AUC from covariate shift inversion in cross-strategy LOO (RF classifier)\"}, \"baseline_battery_9cell_001\": {\"status\": \"DONE\", \"hypothesis\": \"9-cell baseline battery: 4 种分类方法 (RF/LR/CORAL/DivEye) 在 3×3 矩阵全部 cells 上的 4-class accuracy 对比，生成 paper Table 1\"}, \"olmo_topk50_001\": {\"status\": \"DONE\", \"hypothesis\": \"解码策略鲁棒性: OLMo-1B 在 top-k k=50 下递归生成的深度信号与 nucleus p=0.95 一致，支持跨策略泛化\"}, \"atlas_v2_analysis\": {\"status\": \"DONE\", \"hypothesis\": \"Atlas v2 (9-cell): p90_ppl 和 var_surprisal 在所有 9 cells 中稳定为 top-2 features，EDD≥3 在多数 cells 成立，证明深度退化信号具有跨模型跨策略一致性\"}, \"cross_model_loo_001\": {\"status\": \"DONE\", \"hypothesis\": \"Cross-model LOO: 深度信号跨模型泛化，train on 2 families test on 3rd 的 4-class acc ≥ 45%（plan_005 gate）\"}, \"gpt2xl_topk50_001\": {\"status\": \"DONE\", \"hypothesis\": \"解码策略鲁棒性: GPT-2 XL 在 top-k k=50 下递归生成的深度信号与 nucleus p=0.95 一致，支持跨策略泛化\"}, \"dcol_deberta_005\": {\"status\": \"DONE\", \"hypothesis\": \"DCOL v5 (LoRA r=16 alpha=16, margin_lr=1e-4): DeBERTa-v3-large + LoRA + Contrastive Ordinal Loss，修正 margin_lr 从 1e-3 到 1e-4 避免 embedding collapse\"}, \"dcol_deberta_004\": {\"status\": \"DONE\", \"hypothesis\": \"DCOL v4 (LoRA r=16 alpha=16): DeBERTa-v3-large + LoRA + Contrastive Ordinal Loss，冻结 backbone 只训 LoRA adapter + head + margins\"}, \"dcol_deberta_003\": {\"status\": \"DONE\"}, \"olmo_temp09_001\": {\"status\": \"DONE\", \"hypothesis\": \"解码策略鲁棒性: OLMo-1B 在 temperature-only τ=0.9 下递归生成的深度信号与 nucleus p=0.95 一致，支持跨策略泛化\"}, \"atlas_v1_analysis\": {\"status\": \"DONE\", \"hypothesis\": \"Depth Degradation Atlas v1: 跨模型/策略的深度退化特征具有单调性(monotonicity)，EDD 可量化退化饱和点\"}, \"dcol_deberta_002\": {\"status\": \"DONE\", \"hypothesis\": \"DCOL v2 (修复 embedding collapse): margin_lr=1e-4, L2 norm, cl_weight=1.0\"}, \"gpt2xl_temp09_001\": {\"status\": \"DONE\", \"hypothesis\": \"解码策略鲁棒性: GPT-2 XL 在 temperature-only τ=0.9 下递归生成的深度信号与 nucleus p=0.95 一致，支持跨策略泛化\"}, \"dcol_deberta_001\": {\"status\": \"DONE\", \"hypothesis\": \"DCOL (DeBERTa-v3-large + Contrastive Ordinal Loss with learnable margins) 从原始文本直接预测递归生成深度，优于统计特征+RF方法\"}, \"cross_model_olmo_temp09_001\": {\"status\": \"DONE\", \"hypothesis\": \"OLMo-1B cross-model validation with temp_only decoding (t=0.9)\"}, \"pythia_topk50_001\": {\"status\": \"DONE\", \"hypothesis\": \"解码策略鲁棒性: Pythia-1.4B 在 top-k k=50 下递归生成的深度信号与 nucleus p=0.95 一致，支持跨策略泛化\"}, \"cross_model_gpt2xl_001\": {\"status\": \"DONE\"}, \"cross_model_olmo_002\": {\"status\": \"DONE\", \"hypothesis\": \"跨模型泛化: OLMo-1B 递归生成的统计特征与 Pythia-1.4B 一致，支持深度估计跨模型迁移 (重跑 olmo_001, 修复脚本 bug)\"}, \"pythia_temp09_001\": {\"status\": \"DONE\", \"hypothesis\": \"解码策略鲁棒性: Pythia-1.4B 在 temperature-only τ=0.9 下递归生成的深度信号与 nucleus p=0.95 一致，支持跨策略泛化\"}, \"mvp_pipeline_pythia_002\": {\"status\": \"DONE\"}, \"cross_model_olmo_001\": {\"status\": \"DONE\"}, \"mvp_pipeline_qwen_base_004\": {\"status\": \"DONE\"}, \"mvp_pipeline_pythia_001\": {\"status\": \"DONE\"}, \"mvp_pipeline_base_002\": {\"status\": \"DONE\"}, \"mvp_pipeline_003\": {\"status\": \"DONE\"}, \"mvp_pipeline_002\": {\"status\": \"DONE\"}, \"mvp_pipeline_001\": {\"status\": \"DONE\"}, \"mvp_pipeline_base_003\": {\"status\": \"DONE\"}, \"mvp_pipeline_004\": {\"status\": \"DONE\"}}, \"count\": 147, \"total\": 147, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5427}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d4232873-36cc-4637-aa32-766dcf85d815",
  "uuid": "9578f213-f0c8-4dc0-a29b-b0fbddb9ac67",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"wild_data_calibration_015\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"RF depth estimator's wild-data FPR is consistent across diverse web corpora (C4, FineWeb, RedPajama) and can be reduced below 5% via P(d0) threshold adjustment with minimal recall loss, confirming the distribution shift is a calibration issue not a fundamental limitation.\\\"}, \\\"accum_olmo_temp_mix50\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"OLMo-1B temp0.9 accumulation at 50% human mix ratio shows further depth signal degradation vs mix25 (73.47%), paralleling GPT-2 XL pattern (mix25 70.08% → mix50 69.05%) and Pythia pattern, confirming cross-model consistency of accumulation mixing effects\\\"}, \\\"accum_pythia_nuc_mix50\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Pythia-1.4B nucleus accumulation at 50% human mix ratio shows further signal degradation vs mix25 (70.77%), paralleling GPT-2 XL pattern (mix25 70.08% → mix50 69.05%)\\\"}, \\\"conditional_pi_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Perplexity tail features (p90_ppl, kurtosis_ppl, var_ppl, etc.) remain the top-ranked feature family under permutation importance (not Gini), with stable bootstrap rank CIs across all 9 model-strategy cells, refuting R17's concern that VIF>10 collinearity invalidates importance rankings.\\\"}, \\\"conditional_pi_002\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Perplexity tail features (p90_ppl, var_surprisal, kurt_ppl) remain the top family under conditional permutation importance with Random Forest, even after controlling for inter-feature correlation across all 9 model×strategy cells.\\\"}, \\\"accum_pythia_nuc_002\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Accumulation scenario with Pythia-1.4B nucleus sampling shows comparable depth signal degradation pattern to GPT-2 XL nucleus (accum_v3): mix25 ~70% and mix50 ~69%, confirming cross-model consistency of accumulation effects on depth estimation. Retry of accum_pythia_nuc_001 (failed due to cuda:1 not existing).\\\"}, \\\"accum_olmo_temp_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Accumulation scenario with OLMo-1B temp0.9 shows comparable depth signal degradation pattern to GPT-2 XL nucleus (accum_v3), confirming cross-strategy consistency of accumulation effects on depth estimation\\\"}, \\\"accum_pythia_nuc_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Accumulation scenario with Pythia-1.4B nucleus sampling shows comparable depth signal degradation pattern to GPT-2 XL nucleus (accum_v3): mix25 ~70% and mix50 ~69%, confirming cross-model consistency of accumulation effects on depth estimation\\\"}, \\\"14b_cross_ref_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Cross-reference control: using Pythia-1.4B (same as Table 1 pipeline) instead of self-reference (Qwen2.5-14B) for feature extraction on 14B generated text yields comparable classification accuracy, confirming that the reference model choice does not fundamentally change the depth signal detection at 14B scale. Addresses R17 concern about self-reference vs cross-reference consistency.\\\"}, \\\"fpr_coverage_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Confidence thresholding on RF max_prob can reduce C4 FPR substantially while maintaining reasonable coverage, providing a practical operating point for deployment where users can trade coverage for lower false positive rates.\\\"}, \\\"binoculars_14b_topk50\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Binoculars cross-perplexity features provide complementary signal at 14B scale under top-k sampling when merged with 19 statistical features. Tests whether the merged feature gain (~+3.7pp at temp09) holds under the weakest decoding strategy.\\\"}, \\\"qwen25_14b_topk50\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Recursive generation depth signal persists at 14B scale under top-k sampling (k=50), achieving RF 4-class accuracy above 25% baseline. Top-k typically yields lowest accuracy across strategies; if signal persists even here, 14B scale-generality claim is robust. Directly addresses Dream worst review M3.\\\"}, \\\"binoculars_14b_temp09\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Binoculars cross-perplexity features provide complementary signal at 14B scale when merged with 19 statistical features, yielding accuracy above stat-only baseline. Tests whether cross-model divergence channel persists at larger scale.\\\"}, \\\"qwen25_14b_temp09\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Recursive generation depth signal persists at 14B scale under temperature sampling (τ=0.9), achieving RF 4-class accuracy above 25% baseline and comparable to scale_002 nucleus (54.05%). Validates Claim 2: Atlas spans 3 strategies at 14B. Directly addresses Dream worst review M3 \\\\\\\"14B too narrow\\\\\\\".\\\"}, \\\"feature_ablation_merged_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Merging our 19 statistical features with 11 Binoculars cross-perplexity features (30 total) should reveal whether the two feature sets provide complementary depth signal. If merged RF >80%, the cross-model transfer signal from Binoculars adds value beyond our features (answers reviewer \\\\\\\"why not merge?\\\\\\\"). If merged RF ≈ 78%, signal is saturated and both feature sets are redundant — depth information ceiling is ~78% on these features.\\\"}, \\\"feature_ablation_overlap_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"The 6 overlapping features between Binoculars and our 19-feature set (ppl_mean, ppl_var, ppl_median, p10_ppl, p90_ppl, skewness_ppl) capture the core depth signal. If 6-feature RF ≈ 78%, the overlap features alone are sufficient and shape features add negligible value. If 6-feature RF significantly < 78%, the remaining shape features (var_surprisal, kurtosis, etc.) have independent discriminative contribution beyond mean-level displacement.\\\"}, \\\"binoculars_ordinal_baseline_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Binoculars (Hans et al., ICML 2024) cross-perplexity scores (observer=pythia-1.4b, performer=pythia-410m), when calibrated to 4-class ordinal depth, achieve near-chance accuracy on 9-cell atlas. Binoculars is binary detection SOTA; testing it is critical for completeness. Reviewer will ask \\\\\\\"did you test Binoculars?\\\\\\\"\\\"}, \\\"detectgpt_ordinal_baseline_004\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"DetectGPT perturbation discrepancy scores on pythia_nucleus cell achieve near-chance 4-class ordinal accuracy, completing the 9/9 cell coverage. Extends detectgpt_ordinal_baseline_002 (8/9 cells, 29.1%) with the missing pythia_nucleus cell. Script fixed with cell→directory mapping for pythia_nucleus (\\\\\\\".\\\\\\\").\\\"}, \\\"detectgpt_ordinal_baseline_003\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Fast-DetectGPT (Mitchell et al. 2023) perturbation discrepancy scores, when calibrated to 4-class ordinal depth via equal-width/CORAL/threshold methods, achieve near-chance accuracy on full 9-cell atlas. Extends detectgpt_ordinal_baseline_002 (8/9 cells, 29.1%) to include pythia_nucleus. Confirms perturbation-based binary detection lacks ordinal resolution.\\\"}, \\\"deberta_pilot_pythia_temp09\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"DeBERTa-v3-base (LoRA) end-to-end 4-class depth classification on pythia_temp09 cell achieves lower accuracy than RF+19-feature baseline, confirming cross-model generality of \\\\\\\"simple features beat neural\\\\\\\" finding. Paired with gpt2xl_temp09 pilot to cover both strong and weak atlas cells.\\\"}, \\\"deberta_pilot_gpt2xl_temp09\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"DeBERTa-v3-base (LoRA) end-to-end 4-class depth classification on gpt2xl_temp09 cell achieves lower accuracy than RF+19-feature baseline (78.2%), demonstrating that hand-crafted perplexity-distribution features capture depth signal more effectively than neural text representations. Addresses reviewer concern \\\\\\\"RF has no algorithmic contribution\\\\\\\" — if RF ≥ DeBERTa, \\\\\\\"simple features beat neural\\\\\\\" is a paper insight.\\\"}, \\\"mink_ordinal_baseline_002\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Min-K% Prob (Shi et al. 2024) continuous membership-inference scores, when calibrated to 4-class ordinal depth via equal-width/CORAL/threshold methods, achieve near-chance accuracy (30-35%) on 9-cell atlas. Establishes that binary detection scores lack ordinal depth resolution. Rebuttal ammunition against \\\\\\\"did you test Min-K% for ordinal?\\\\\\\"\\\"}, \\\"detectgpt_ordinal_baseline_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"DetectGPT (Mitchell et al. 2023) perturbation discrepancy scores, when calibrated to 4-class ordinal depth via equal-width/CORAL/threshold methods, achieve near-chance accuracy (30-35%) on 9-cell atlas. Establishes that perturbation-based binary detection lacks ordinal resolution. Rebuttal ammunition against \\\\\\\"binary detectors might also detect depth.\\\\\\\"\\\"}, \\\"mink_ordinal_baseline_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Min-K% Prob (Shi et al. 2024) continuous membership-inference scores, when calibrated to 4-class ordinal depth via equal-width/CORAL/threshold methods, achieve near-chance accuracy (30-35%) on 9-cell atlas. Establishes that binary detection scores lack ordinal depth resolution. Rebuttal ammunition against \\\\\\\"did you test Min-K% for ordinal?\\\\\\\"\\\"}, \\\"detectgpt_ordinal_baseline_002\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"DetectGPT (Mitchell et al., 2023) perturbation discrepancy scores, when calibrated to 4-class ordinal depth via equal-width/CORAL/threshold methods, achieve near-chance accuracy (~29%) on 8/9 atlas cells. Fast-DetectGPT (Bao et al., 2024) is a strictly stronger baseline; if even original DetectGPT fails at ordinal depth, Fast-DetectGPT would perform no better. Establishes that perturbation-based binary detection lacks ordinal resolution.\\\"}, \\\"cross_strategy_dann_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"DANN (Domain-Adversarial Neural Network) learns strategy-invariant feature representations via gradient reversal, improving cross-strategy LOSO depth classification from naive RF 59.1% and two-stage 70.5% to 73-75%+. The shared encoder + adversarial strategy discriminator forces the model to extract depth-discriminative features that are invariant to decoding strategy differences. If delta vs two-stage >= 3pp, becomes main method contribution in §3.\\\"}, \\\"accum_v3_mix25\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Under 25/75 accumulation (mixing 25% human + 75% previous-depth synthetic text at each depth, then LoRA fine-tune + generate), depth signal attenuates to ~70% compared to full-replacement (84.2%). Comparable to mix50 (~69%, 1pp difference within seed noise of 2.04pp). Together with mix50, establishes accumulation degradation magnitude for Discussion §6.\\\"}, \\\"accum_v3_mix50\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Under 50/50 accumulation (mixing 50% human + 50% previous-depth synthetic text at each depth, then LoRA fine-tune + generate), depth signal attenuates to ~69% compared to full-replacement (84.2%), establishing that full-replacement results are a ceiling. Comparable to mix25 (~70%, within seed noise). Quantifies accumulation degradation for Discussion §6. Parent: invalidated accum_mix50 (feature-space mixing error).\\\"}, \\\"accum_mix50\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Accumulation scenario (50% human + 50% synthetic per depth) will degrade RF 4-class accuracy below full-replacement (84.2%), confirming that full-replacement results are an upper bound on feature separability. The degradation magnitude quantifies how much human-text mixing attenuates the depth signal.\\\"}, \\\"accum_mix25\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Accumulation scenario (25% human + 75% synthetic per depth) will show intermediate degradation between full-replacement (84.2%) and 50/50 mix, establishing a degradation curve that characterizes how human-text proportion affects depth separability.\\\"}, \\\"coral_ordinal_9cell_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"CORAL ordinal regression with DNN backbone (19→64→32→CORAL) achieves comparable or superior 4-class accuracy to RF on all 9 atlas cells, while providing better ordinal consistency (monotonic predictions) and lower MAE due to ordinal-aware loss. Prior baseline_battery_9cell_001 showed RF≈CORAL with simple CORAL; DNN backbone may widen the gap. Algorithmic contribution: ordinal-specific classifier for depth estimation.\\\"}, \\\"lr_zscore_cross_strategy_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"LR cross-strategy LOO + z-score: 验证 paper_framing 声称的 z-score 恢复 LR d1v2 AUC（GPT-2 XL 0.13→0.68, OLMo 0.25→0.83）。论文 claim 硬依赖。\\\"}, \\\"rf_21feature_augmented_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Adding Min-K% Prob and DetectGPT scores to the 19 statistical features will either show redundancy (detection scores add no info beyond statistical features) or complementarity (detection scores capture unique signal), both outcomes strengthen the paper narrative\\\"}, \\\"qwen25_14b_scale_003\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"14B scale validation reproducibility: Qwen2.5-14B FP16 recursive chain on westd-48862 (RTX PRO 6000 Blackwell) produces consistent depth signal with gpu-6000pro-2 run, confirming results are not hardware-dependent.\\\"}, \\\"d4_extension_olmo_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"OLMo-1B nucleus d4 depth extension: recursive generation depth signal persists at d4, completing 3/3 model coverage for EDD >= 4 verification.\\\"}, \\\"d4_extension_pythia_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Pythia-1.4B nucleus d4 depth extension: recursive generation depth signal persists at d4, providing second model evidence for EDD >= 4. d3v4 pairwise AUC > 0.70, 5-class RF accuracy well above 20% chance.\\\"}, \\\"d4_extension_gpt2xl_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"GPT-2 XL nucleus d4 depth extension: recursive generation depth signal persists at d4 (5th recursive iteration). 5-class RF (d0-d4) accuracy remains significantly above 20% chance level, d3-vs-d4 pairwise AUC > 0.6, and key features (p90_ppl, var_surprisal, mean_ppl) continue monotonic trends observed in d0-d3.\\\"}, \\\"qwen25_14b_scale_002\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Recursive generation depth signal (statistical features distinguishing d0-d3) persists at 14B parameter scale (Qwen2.5-14B FP16), achieving RF 4-class accuracy significantly above 25% baseline, validating that model collapse signatures are not artifacts of small model capacity.\\\"}, \\\"olmo_seed43_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"OLMo-1B with seed=43 and nucleus sampling (p=0.95) will reproduce the recursive generation depth signal (d0-d3 classification accuracy) observed in prior seeds, validating cross-seed reproducibility for the OLMo model family.\\\"}, \\\"pythia_seed43_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Pythia-1.4B recursive generation chain with seed=43 will produce depth-discriminative statistical features comparable to seed=42 (83.3% 4-class RF accuracy), confirming depth signal is inherent to recursive process not seed-specific.\\\"}, \\\"gpt2xl_seed43_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"GPT-2 XL recursive generation depth signal is reproducible across random seeds: seed=43 should yield 4-class RF accuracy within 5pp of seed=42 baseline (83.3%), confirming depth degradation is inherent to the recursive fine-tuning process rather than LoRA weight initialization.\\\"}, \\\"prompted_gen_gpt2xl_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Prompted generation preserves depth signal: GPT-2 XL topic-prompted 4-class acc >= 70%, delta <= 15pp vs BOS-seeded baseline (83.3%)\\\"}, \\\"qwen25-1p5b-instruct-001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Depth signal persists in instruction-tuned models: Qwen2.5-1.5B-Instruct recursive chain (nucleus p=0.95, d0-d3) achieves RF 4-class accuracy significantly above 25% baseline, demonstrating that instruction tuning does not eliminate model collapse signatures.\\\"}, \\\"learned_estimator_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Statistical features (19-dimensional: perplexity stats, surprisal, n-gram entropy, repetition ratios) can predict generation depth (0-3) with over 70% accuracy using learned classifiers (ordinal MLP, prototypical networks, XGBoost), and this generalizes across models in leave-one-out evaluation, because recursive generation progressively degrades text quality in statistically measurable ways.\\\"}, \\\"downstream_benchmark_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Depth-filtered training data (strict subset: depth 0-1 only) will produce better fine-tuned models than unfiltered or random data, because lower-depth text contains more original content with cleaner training signal, leading to lower perplexity on held-out evaluation after LoRA fine-tuning of Pythia-410M.\\\"}, \\\"qwen25-1p5b-instruct-002\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"qwen25-1p5b-instruct-001-ph45v3\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"qwen25-1p5b-instruct-001-ph45v2\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"qwen25-1p5b-instruct-001-ph45\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"qwen25-1p5b-instruct-001-phase45\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"learned_estimator_002\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Fixing NaN issues in Prototypical Network (torch.clamp + nan_to_num in distances, safe softmax conversion) and running full data sweep (no max_samples limit) will enable learned estimators (XGBoost, CORAL MLP, Prototypical) to exceed the RF baseline of 66.4% accuracy in cross-model depth estimation.\\\"}, \\\"wild_data_features_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Wild web corpora (C4, FineWeb) contain measurable proportions of text classified as recursive-generation depth d1+ by our RF estimator, providing evidence that model-generated text is present in training data.\\\"}, \\\"downstream_benchmark_002\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Fine-tuning on depth-0 (original) text produces lower held-out perplexity than fine-tuning on higher-depth (recursive) text, because d0 data has higher quality signal without recursive degradation artifacts.\\\"}, \\\"learned_estimator_proto_fix_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Prototypical Network with NaN fix (torch.clamp + nan_to_num on distance computation) achieves ~67.1% leave-one-model-out accuracy on 19 statistical features, comparable to RF baseline (66.4%), completing the learned estimator comparison matrix.\\\"}, \\\"detector_ord_baseline_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Existing AI-text detectors (Binoculars, Fast-DetectGPT) calibrated for ordinal depth estimation perform worse than our RF-on-19-features approach, confirming that depth-specific statistical features capture information beyond generic detection scores.\\\"}, \\\"plan_018_binoculars_baseline\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"bootstrap_ci_table1_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Bootstrap 95% CIs for all 9 cells of the 3×3 core matrix (3 models × 3 strategies) confirm that RF accuracy point estimates are stable (CI width ~1pp), and RF significantly outperforms LR in 8/9 cells.\\\"}, \\\"text_length_sensitivity_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Depth estimation accuracy degrades gracefully with shorter text truncation because the key statistical features (surprisal moments, entropy) converge within the first 100-200 tokens, making the method practical for short-text scenarios.\\\"}, \\\"qwen25_14b_scale_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Recursive generation depth signal (statistical features distinguishing d0-d3) persists at 14B parameter scale (Qwen2.5-14B FP16), achieving RF 4-class accuracy significantly above 25% baseline, validating that model collapse signatures are not artifacts of small model capacity.\\\"}, \\\"mlp_19feat_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"2-layer MLP on 19 features achieves similar accuracy to RF (delta <= 3pp), confirming features rather than classifier as the performance bottleneck\\\"}, \\\"cross_strategy_pipeline_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Strategy classifier achieves >90% accuracy on 19 statistical features; two-stage pipeline (predict strategy then route to per-strategy depth RF) recovers cross-strategy depth accuracy to >=70% vs naive LOO 59.1%\\\"}, \\\"gen_length_ablation_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Depth signal scales with passage length: 128-token passages are detectable but weaker; 512-token passages match 256-token baseline; cross-length accuracy spread ≤ 5pp\\\"}, \\\"cross_seed_transfer_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"If depth signal is an inherent property of recursive generation, an RF trained on seed=42 features should generalize to seed=43 features with cross-seed acc ≥ 75% (Δ ≤ 3pp vs within-seed)\\\"}, \\\"mixed_depth_corpus_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"RF per-sample classifier does not rely on corpus-level depth distribution prior; accuracy on mixed-depth corpus (50/30/15/5%) should match balanced baseline within Δ ≤ 2pp\\\"}, \\\"ensemble_reference_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Ensemble reference (mean surprisal across multiple ref models) improves robustness vs worst single-model reference; ensemble acc should exceed GPT-2 XL-only (67.3%) by ≥5pp\\\"}, \\\"second_seed_replication_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"递归生成 depth signal 是 recursive process 的固有属性而非特定 LoRA 权重的 idiosyncrasy；用不同 seed(=43) 训练的 LoRA 应产生与 seed=42 一致的 depth fingerprint（accuracy Δ ≤ 3pp vs 78.2%）\\\"}, \\\"reference_free_baseline_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Depth signal is partially accessible without reference model: reference-free token statistics (TTR, repetition, entropy, sentence length) achieve >60% 4-class accuracy (>2.5x chance)\\\"}, \\\"feat_ablation_v1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"A small subset of surprisal features (top-5 by RF importance) captures most depth signal: top-5 acc ≥95% of full 19-feature accuracy, identifying the minimal sufficient feature set for depth estimation\\\"}, \\\"feature_ablation_9cell\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Top-5 surprisal features achieve ≥90% of full 19-feature accuracy across all 9 atlas cells, confirming a minimal sufficient feature set independent of model/strategy combination\\\"}, \\\"depth_extension_olmo_d4d5_002\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"OLMo-1B EDD 与 Pythia-1.4B 一致（EDD=4），验证 EDD 跨模型稳定性\\\"}, \\\"wild_data_calibration_005\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"RedPajama web-crawl text is classified as d0 with FPR≤25%, consistent with C4/FineWeb calibration patterns, confirming cross-corpus robustness of depth classifier on diverse web data\\\"}, \\\"wild_data_calibration_004\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"OpenWebText curated web text is classified as d0 with near-zero FPR (≤5%), confirming editorial curation quality correlates with lower false positive rates vs raw web-crawl\\\"}, \\\"gpt2xl_ref_ablation_001\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"ref_model_ablation_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"OLMo-1B as alternative reference model yields depth classification within ±5pp of Pythia-1.4B reference, confirming surprisal-based features are not specific to a matched Pythia architecture\\\"}, \\\"baseline_battery_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Multiple classifier families (RF/LR/CORAL/CE-MLP/DivEye/PPL-Reg) achieve >40% 4-class accuracy on surprisal features, confirming depth signal is classifier-agnostic and not specific to RF decision boundaries\\\"}, \\\"batch_feature_extraction_5cells\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Feature extraction pipeline produces consistent 19-dim feature vectors across 5 new cells (GPT-2 XL + OLMo × 3 strategies), enabling downstream cross-model/cross-strategy generalization analysis\\\"}, \\\"cross_model_loo_v1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"RF trained on depth features from 2 generator models generalizes to held-out 3rd model with acc>50% (chance=25%), confirming depth features encode model-agnostic recursive degradation patterns\\\"}, \\\"cross_scale_llama3_8b_003\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Llama-3.1-8B-Instruct preserves monotonic AUC decay with EDD≥4 at 8B scale, confirming depth signal generalizes beyond 1-1.5B models to production-scale LLMs\\\"}, \\\"lora_rank_ablation_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"LoRA rank (r∈{4,16,64}) minimally affects depth signal: accuracy spread ≤5pp across ranks would confirm depth signal is not an artifact of a specific LoRA fine-tuning configuration\\\"}, \\\"cross_scale_llama3_base_001\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"cross_model_reverse_chain_001\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"cross_scale_qwen7b_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Plan_014 7B cross-scale probe: Qwen2.5-7B nucleus p=0.95, d0-d5, 500 samples/depth。验证 depth signal 和 EDD 在 7B scale 上是否与 1-1.5B 模型一致。成功标准：4-class acc ≥ 60%, EDD 测定, pairwise AUC 衰减趋势方向一致。\\\"}, \\\"domain_extension_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Domain extension: 用 arXiv abstracts 替代 WikiText 作为 seed，验证 depth signal 是否 domain-independent。成功标准：4-class acc ≥ 65%, top features 与 WikiText pipeline 一致。\\\"}, \\\"cross_scale_llama3_8b_002\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"cross_model_recursive_chain_002\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"cross_model_recursive_chain_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Cross-model recursive chain: Human→Pythia d1→OLMo finetune→GPT-2 XL finetune。验证 depth signal 是否能跨越模型边界累积——即使每一步用不同模型递归，distributional artifacts 仍然可检测。成功标准：chain-d2/d3 的 pairwise AUC > chance, 4-class acc ≥ 50%。\\\"}, \\\"cross_scale_llama3_8b_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"7B cross-scale probe (Llama-3-8B): 验证 depth signal 在 Llama-3 架构上的可检测性。Nucleus p=0.95, d0-d5, 500 samples/depth。成功标准：4-class acc ≥ 60%, EDD 测定, pairwise AUC 衰减趋势与 1-1.5B 模型方向一致。\\\"}, \\\"two_stage_strategy_pipeline_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Two-stage pipeline: 先分类 decoding strategy，再用 strategy-conditioned depth classifier。验证 Discussion 中提出的 two-stage 方案的可行性和瓶颈。\\\"}, \\\"multi_tau_ablation_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"R2-W3 multi-τ ablation: 4 τ values (0.5, 0.7, 0.9, 1.1) × Pythia-1.4B。验证 depth classification signal 跨温度的鲁棒性，特别是 d1v2 AUC 是否随 τ 单调变化或在特定 τ 出现 inversion。Cross-τ LOO 验证跨温度泛化能力。\\\"}, \\\"zeroshot_qwen7b_500_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"R1-W4 第二个 LLM baseline：Qwen2.5-7B-Instruct 4-bit zero-shot depth classification。与 DeepSeek-v3.2 (36.2%) 对比，验证 LLM zero-shot 在 depth task 上的一般性劣势（vs RF 78.2%）。\\\"}, \\\"wild_data_calibration_003\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Wild data calibration v3: 离线方案。先下载 RedPajama/Dolma 到本地磁盘，再用 wild_data_calibration_001 的 RF 模型评估 FPR。验证论文 wild-text calibration 在更多数据源上的泛化。\\\"}, \\\"wild_data_calibration_002\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"wild_data_redpajama_dolma_001\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"wild_data_calibration_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Classifiers trained on recursive generation data should correctly classify wild (human) text as d0 with low FPR, confirming calibration on out-of-distribution natural text\\\"}, \\\"random_soft_control_001\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"downstream_curation_poc_001\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"wild_data_olmo_calibration_001\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"pythia7b_cross_scale_001\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"wild_data_gpt2xl_calibration_001\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"wild_data_c4_supplement_001\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"w2_domain_bias_001\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"xgboost_lgbm_3cell_001\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"xgboost_lgbm_baseline_001\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"shap_supplement_001\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"zeroshot_llm_500_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"R1-W4 zero-shot 样本量扩展: 从 200→500 samples 缩窄 CI。当前 200 samples 的 CI 过宽，500 samples 可将 CI 宽度缩小 ~37%，更可靠地与 RF 78.2% 对比。\\\"}, \\\"temp07_pilot_pythia_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"R2-W3 multi-τ: τ=0.7 temperature pilot with Pythia-1.4B. 验证 d1v2 inversion 是否在 τ=0.7 也出现（对比 τ=0.9 的 GPT-2 XL 0.129 / OLMo 0.253）。若出现则 temperature inversion 是 τ<1 的通用现象；若不出现则 τ=0.9 是边界条件。\\\"}, \\\"n2_roberta_finetune_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"N2 reviewer concern: end-to-end RoBERTa-base finetune baseline vs RF on hand-crafted features (78.2%). 与 DeBERTa 形成双 backbone 对比，排除模型选择偏差。\\\"}, \\\"n2_deberta_finetune_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"N2 reviewer concern: end-to-end DeBERTa-v3-base finetune baseline vs RF on hand-crafted features (78.2%). 若 DeBERTa acc < RF，证明手工特征确有独立贡献；若 ≥ RF，需重新定位 narrative。\\\"}, \\\"cross_strategy_loo_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Cross-strategy LOO (plan_007): 深度信号跨策略可迁移——同模型内，用 2 种解码策略训练的 RF 可泛化到第 3 种，4-class acc 均值 59.1% 远超 chance 25%。temp09 holdout 的 d1v2 AUC 反转 (GPT-2 XL: 0.13, OLMo: 0.25) 证明解码策略塑造不同的退化轨迹 (D014)\\\"}, \\\"depth_extension_gpt2xl_d4d5_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"GPT-2 XL depth extension: 从 d3 checkpoint 继续递归生成 d4/d5 各 5000 samples，binary pairwise RF 验证 EDD。GPT-2 XL 是 3×3 矩阵中信号最强的模型 (85.4%)，若 EDD≥4 则与 Pythia 结果 (EDD=4) 形成跨模型 EDD 一致性证据。\\\"}, \\\"depth_extension_olmo_d4d5_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"OLMo-1B depth extension: 从 d3 checkpoint 继续递归生成 d4/d5 各 5000 samples，binary pairwise RF 验证 EDD。OLMo 是 3×3 矩阵中间模型 (78.8%)，若 EDD≥4 则与 Pythia (EDD=4) 形成跨模型 EDD 一致性证据，3 模型 EDD 完整对比。\\\"}, \\\"granularity_ablation_rf_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Granularity ablation: 对比 binary/3-class/4-class/6-class RF 性能，量化分类粒度对决策边界稀释的影响。预期 accuracy 随粒度增加单调下降，adjacent-pair AUC 在 binary 设置下最高。支持 Claim 1 (feasibility) + Claim 2 (EDD boundary dilution)。\\\"}, \\\"zero_shot_llm_baseline_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Zero-shot LLM baseline: DeepSeek V3.2 直接判断文本递归生成深度 (4-class)，无需统计特征提取。作为 upper-bound baseline 对比 feature-based 方法。\\\"}, \\\"olmo_temp09_002\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"解码策略鲁棒性: OLMo-1B 在 temperature-only τ=0.9 下递归生成的深度信号与 nucleus p=0.95 一致（olmo_temp09_001 重跑，从 Step 3 断点恢复）\\\"}, \\\"depth_extension_pythia_d4d5_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Depth extension to d4/d5: EDD 从 d3 (当前 EDD=3 未饱和) 继续延伸——如果 d3v4 和 d4v5 AUC 仍 >0.75，则 EDD≥5，证明递归深度信号至少在 5 代内不饱和\\\"}, \\\"depth_extension_binary_pairwise_002\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Retry of binary_pairwise_001 (failed due to missing script on server). Dedicated binary RF for d3v4 and d4v5 pairwise AUC. Judgment: d3v4>0.75 + d4v5>0.75 → EDD≥5; d3v4>0.75 only → EDD=4.\\\"}, \\\"depth_extension_binary_pairwise_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Dedicated binary pairwise RF 评估 d3v4 和 d4v5 可区分性。6-class RF 的 pairwise AUC 因决策边界稀释不可靠（d2v3 从 4-class 0.80 降到 0.69 是 artifact）。Binary classifier 消除此 artifact，与原 4-class pipeline 的 d0v1/d1v2/d2v3 AUC 可比。判定标准：binary d3v4 AUC > 0.75 且 d4v5 AUC > 0.75 → EDD≥5；d3v4 > 0.75 但 d4v5 < 0.75 → EDD=4。\\\"}, \\\"dcol_roberta_v6_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"DCOL v6: RoBERTa-large 替代 DeBERTa 解决数值不稳定。lr=5e-5 + grad clip 1.0 + NaN guard + collapse guard (step 500 acc&lt;30% kill)。若 4-class acc > RF baseline (78.2%) 则 DCOL 成功，否则降级为 negative result。\\\"}, \\\"cross_strategy_loo_zscore_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Z-score standardization recovers temp09 d1v2 AUC from covariate shift inversion in cross-strategy LOO (RF classifier)\\\"}, \\\"baseline_battery_9cell_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"9-cell baseline battery: 4 种分类方法 (RF/LR/CORAL/DivEye) 在 3×3 矩阵全部 cells 上的 4-class accuracy 对比，生成 paper Table 1\\\"}, \\\"olmo_topk50_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"解码策略鲁棒性: OLMo-1B 在 top-k k=50 下递归生成的深度信号与 nucleus p=0.95 一致，支持跨策略泛化\\\"}, \\\"atlas_v2_analysis\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Atlas v2 (9-cell): p90_ppl 和 var_surprisal 在所有 9 cells 中稳定为 top-2 features，EDD≥3 在多数 cells 成立，证明深度退化信号具有跨模型跨策略一致性\\\"}, \\\"cross_model_loo_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Cross-model LOO: 深度信号跨模型泛化，train on 2 families test on 3rd 的 4-class acc ≥ 45%（plan_005 gate）\\\"}, \\\"gpt2xl_topk50_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"解码策略鲁棒性: GPT-2 XL 在 top-k k=50 下递归生成的深度信号与 nucleus p=0.95 一致，支持跨策略泛化\\\"}, \\\"dcol_deberta_005\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"DCOL v5 (LoRA r=16 alpha=16, margin_lr=1e-4): DeBERTa-v3-large + LoRA + Contrastive Ordinal Loss，修正 margin_lr 从 1e-3 到 1e-4 避免 embedding collapse\\\"}, \\\"dcol_deberta_004\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"DCOL v4 (LoRA r=16 alpha=16): DeBERTa-v3-large + LoRA + Contrastive Ordinal Loss，冻结 backbone 只训 LoRA adapter + head + margins\\\"}, \\\"dcol_deberta_003\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"olmo_temp09_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"解码策略鲁棒性: OLMo-1B 在 temperature-only τ=0.9 下递归生成的深度信号与 nucleus p=0.95 一致，支持跨策略泛化\\\"}, \\\"atlas_v1_analysis\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Depth Degradation Atlas v1: 跨模型/策略的深度退化特征具有单调性(monotonicity)，EDD 可量化退化饱和点\\\"}, \\\"dcol_deberta_002\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"DCOL v2 (修复 embedding collapse): margin_lr=1e-4, L2 norm, cl_weight=1.0\\\"}, \\\"gpt2xl_temp09_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"解码策略鲁棒性: GPT-2 XL 在 temperature-only τ=0.9 下递归生成的深度信号与 nucleus p=0.95 一致，支持跨策略泛化\\\"}, \\\"dcol_deberta_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"DCOL (DeBERTa-v3-large + Contrastive Ordinal Loss with learnable margins) 从原始文本直接预测递归生成深度，优于统计特征+RF方法\\\"}, \\\"cross_model_olmo_temp09_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"OLMo-1B cross-model validation with temp_only decoding (t=0.9)\\\"}, \\\"pythia_topk50_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"解码策略鲁棒性: Pythia-1.4B 在 top-k k=50 下递归生成的深度信号与 nucleus p=0.95 一致，支持跨策略泛化\\\"}, \\\"cross_model_gpt2xl_001\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"cross_model_olmo_002\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"跨模型泛化: OLMo-1B 递归生成的统计特征与 Pythia-1.4B 一致，支持深度估计跨模型迁移 (重跑 olmo_001, 修复脚本 bug)\\\"}, \\\"pythia_temp09_001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"解码策略鲁棒性: Pythia-1.4B 在 temperature-only τ=0.9 下递归生成的深度信号与 nucleus p=0.95 一致，支持跨策略泛化\\\"}, \\\"mvp_pipeline_pythia_002\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"cross_model_olmo_001\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"mvp_pipeline_qwen_base_004\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"mvp_pipeline_pythia_001\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"mvp_pipeline_base_002\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"mvp_pipeline_003\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"mvp_pipeline_002\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"mvp_pipeline_001\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"mvp_pipeline_base_003\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"mvp_pipeline_004\\\": {\\\"status\\\": \\\"DONE\\\"}}, \\\"count\\\": 147, \\\"total\\\": 147, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.5427}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"wild_data_calibration_015\": {\"status\": \"DONE\", \"hypothesis\": \"RF depth estimator's wild-data FPR is consistent across diverse web corpora (C4, FineWeb, RedPajama) and can be reduced below 5% via P(d0) threshold adjustment with minimal recall loss, confirming the distribution shift is a calibration issue not a fundamental limitation.\"}, \"accum_olmo_temp_mix50\": {\"status\": \"DONE\", \"hypothesis\": \"OLMo-1B temp0.9 accumulation at 50% human mix ratio shows further depth signal degradation vs mix25 (73.47%), paralleling GPT-2 XL pattern (mix25 70.08% → mix50 69.05%) and Pythia pattern, confirming cross-model consistency of accumulation mixing effects\"}, \"accum_pythia_nuc_mix50\": {\"status\": \"DONE\", \"hypothesis\": \"Pythia-1.4B nucleus accumulation at 50% human mix ratio shows further signal degradation vs mix25 (70.77%), paralleling GPT-2 XL pattern (mix25 70.08% → mix50 69.05%)\"}, \"conditional_pi_001\": {\"status\": \"DONE\", \"hypothesis\": \"Perplexity tail features (p90_ppl, kurtosis_ppl, var_ppl, etc.) remain the top-ranked feature family under permutation importance (not Gini), with stable bootstrap rank CIs across all 9 model-strategy cells, refuting R17's concern that VIF>10 collinearity invalidates importance rankings.\"}, \"conditional_pi_002\": {\"status\": \"DONE\", \"hypothesis\": \"Perplexity tail features (p90_ppl, var_surprisal, kurt_ppl) remain the top family under conditional permutation importance with Random Forest, even after controlling for inter-feature correlation across all 9 model×strategy cells.\"}, \"accum_pythia_nuc_002\": {\"status\": \"DONE\", \"hypothesis\": \"Accumulation scenario with Pythia-1.4B nucleus sampling shows comparable depth signal degradation pattern to GPT-2 XL nucleus (accum_v3): mix25 ~70% and mix50 ~69%, confirming cross-model consistency of accumulation effects on depth estimation. Retry of accum_pythia_nuc_001 (failed due to cuda:1 not existing).\"}, \"accum_olmo_temp_001\": {\"status\": \"DONE\", \"hypothesis\": \"Accumulation scenario with OLMo-1B temp0.9 shows comparable depth signal degradation pattern to GPT-2 XL nucleus (accum_v3), confirming cross-strategy consistency of accumulation effects on depth estimation\"}, \"accum_pythia_nuc_001\": {\"status\": \"DONE\", \"hypothesis\": \"Accumulation scenario with Pythia-1.4B nucleus sampling shows comparable depth signal degradation pattern to GPT-2 XL nucleus (accum_v3): mix25 ~70% and mix50 ~69%, confirming cross-model consistency of accumulation effects on depth estimation\"}, \"14b_cross_ref_001\": {\"status\": \"DONE\", \"hypothesis\": \"Cross-reference control: using Pythia-1.4B (same as Table 1 pipeline) instead of self-reference (Qwen2.5-14B) for feature extraction on 14B generated text yields comparable classification accuracy, confirming that the reference model choice does not fundamentally change the depth signal detection at 14B scale. Addresses R17 concern about self-reference vs cross-reference consistency.\"}, \"fpr_coverage_001\": {\"status\": \"DONE\", \"hypothesis\": \"Confidence thresholding on RF max_prob can reduce C4 FPR substantially while maintaining reasonable coverage, providing a practical operating point for deployment where users can trade coverage for lower false positive rates.\"}, \"binoculars_14b_topk50\": {\"status\": \"DONE\", \"hypothesis\": \"Binoculars cross-perplexity features provide complementary signal at 14B scale under top-k sampling when merged with 19 statistical features. Tests whether the merged feature gain (~+3.7pp at temp09) holds under the weakest decoding strategy.\"}, \"qwen25_14b_topk50\": {\"status\": \"DONE\", \"hypothesis\": \"Recursive generation depth signal persists at 14B scale under top-k sampling (k=50), achieving RF 4-class accuracy above 25% baseline. Top-k typically yields lowest accuracy across strategies; if signal persists even here, 14B scale-generality claim is robust. Directly addresses Dream worst review M3.\"}, \"binoculars_14b_temp09\": {\"status\": \"DONE\", \"hypothesis\": \"Binoculars cross-perplexity features provide complementary signal at 14B scale when merged with 19 statistical features, yielding accuracy above stat-only baseline. Tests whether cross-model divergence channel persists at larger scale.\"}, \"qwen25_14b_temp09\": {\"status\": \"DONE\", \"hypothesis\": \"Recursive generation depth signal persists at 14B scale under temperature sampling (τ=0.9), achieving RF 4-class accuracy above 25% baseline and comparable to scale_002 nucleus (54.05%). Validates Claim 2: Atlas spans 3 strategies at 14B. Directly addresses Dream worst review M3 \\\"14B too narrow\\\".\"}, \"feature_ablation_merged_001\": {\"status\": \"DONE\", \"hypothesis\": \"Merging our 19 statistical features with 11 Binoculars cross-perplexity features (30 total) should reveal whether the two feature sets provide complementary depth signal. If merged RF >80%, the cross-model transfer signal from Binoculars adds value beyond our features (answers reviewer \\\"why not merge?\\\"). If merged RF ≈ 78%, signal is saturated and both feature sets are redundant — depth information ceiling is ~78% on these features.\"}, \"feature_ablation_overlap_001\": {\"status\": \"DONE\", \"hypothesis\": \"The 6 overlapping features between Binoculars and our 19-feature set (ppl_mean, ppl_var, ppl_median, p10_ppl, p90_ppl, skewness_ppl) capture the core depth signal. If 6-feature RF ≈ 78%, the overlap features alone are sufficient and shape features add negligible value. If 6-feature RF significantly < 78%, the remaining shape features (var_surprisal, kurtosis, etc.) have independent discriminative contribution beyond mean-level displacement.\"}, \"binoculars_ordinal_baseline_001\": {\"status\": \"DONE\", \"hypothesis\": \"Binoculars (Hans et al., ICML 2024) cross-perplexity scores (observer=pythia-1.4b, performer=pythia-410m), when calibrated to 4-class ordinal depth, achieve near-chance accuracy on 9-cell atlas. Binoculars is binary detection SOTA; testing it is critical for completeness. Reviewer will ask \\\"did you test Binoculars?\\\"\"}, \"detectgpt_ordinal_baseline_004\": {\"status\": \"DONE\", \"hypothesis\": \"DetectGPT perturbation discrepancy scores on pythia_nucleus cell achieve near-chance 4-class ordinal accuracy, completing the 9/9 cell coverage. Extends detectgpt_ordinal_baseline_002 (8/9 cells, 29.1%) with the missing pythia_nucleus cell. Script fixed with cell→directory mapping for pythia_nucleus (\\\".\\\").\"}, \"detectgpt_ordinal_baseline_003\": {\"status\": \"DONE\", \"hypothesis\": \"Fast-DetectGPT (Mitchell et al. 2023) perturbation discrepancy scores, when calibrated to 4-class ordinal depth via equal-width/CORAL/threshold methods, achieve near-chance accuracy on full 9-cell atlas. Extends detectgpt_ordinal_baseline_002 (8/9 cells, 29.1%) to include pythia_nucleus. Confirms perturbation-based binary detection lacks ordinal resolution.\"}, \"deberta_pilot_pythia_temp09\": {\"status\": \"DONE\", \"hypothesis\": \"DeBERTa-v3-base (LoRA) end-to-end 4-class depth classification on pythia_temp09 cell achieves lower accuracy than RF+19-feature baseline, confirming cross-model generality of \\\"simple features beat neural\\\" finding. Paired with gpt2xl_temp09 pilot to cover both strong and weak atlas cells.\"}, \"deberta_pilot_gpt2xl_temp09\": {\"status\": \"DONE\", \"hypothesis\": \"DeBERTa-v3-base (LoRA) end-to-end 4-class depth classification on gpt2xl_temp09 cell achieves lower accuracy than RF+19-feature baseline (78.2%), demonstrating that hand-crafted perplexity-distribution features capture depth signal more effectively than neural text representations. Addresses reviewer concern \\\"RF has no algorithmic contribution\\\" — if RF ≥ DeBERTa, \\\"simple features beat neural\\\" is a paper insight.\"}, \"mink_ordinal_baseline_002\": {\"status\": \"DONE\", \"hypothesis\": \"Min-K% Prob (Shi et al. 2024) continuous membership-inference scores, when calibrated to 4-class ordinal depth via equal-width/CORAL/threshold methods, achieve near-chance accuracy (30-35%) on 9-cell atlas. Establishes that binary detection scores lack ordinal depth resolution. Rebuttal ammunition against \\\"did you test Min-K% for ordinal?\\\"\"}, \"detectgpt_ordinal_baseline_001\": {\"status\": \"DONE\", \"hypothesis\": \"DetectGPT (Mitchell et al. 2023) perturbation discrepancy scores, when calibrated to 4-class ordinal depth via equal-width/CORAL/threshold methods, achieve near-chance accuracy (30-35%) on 9-cell atlas. Establishes that perturbation-based binary detection lacks ordinal resolution. Rebuttal ammunition against \\\"binary detectors might also detect depth.\\\"\"}, \"mink_ordinal_baseline_001\": {\"status\": \"DONE\", \"hypothesis\": \"Min-K% Prob (Shi et al. 2024) continuous membership-inference scores, when calibrated to 4-class ordinal depth via equal-width/CORAL/threshold methods, achieve near-chance accuracy (30-35%) on 9-cell atlas. Establishes that binary detection scores lack ordinal depth resolution. Rebuttal ammunition against \\\"did you test Min-K% for ordinal?\\\"\"}, \"detectgpt_ordinal_baseline_002\": {\"status\": \"DONE\", \"hypothesis\": \"DetectGPT (Mitchell et al., 2023) perturbation discrepancy scores, when calibrated to 4-class ordinal depth via equal-width/CORAL/threshold methods, achieve near-chance accuracy (~29%) on 8/9 atlas cells. Fast-DetectGPT (Bao et al., 2024) is a strictly stronger baseline; if even original DetectGPT fails at ordinal depth, Fast-DetectGPT would perform no better. Establishes that perturbation-based binary detection lacks ordinal resolution.\"}, \"cross_strategy_dann_001\": {\"status\": \"DONE\", \"hypothesis\": \"DANN (Domain-Adversarial Neural Network) learns strategy-invariant feature representations via gradient reversal, improving cross-strategy LOSO depth classification from naive RF 59.1% and two-stage 70.5% to 73-75%+. The shared encoder + adversarial strategy discriminator forces the model to extract depth-discriminative features that are invariant to decoding strategy differences. If delta vs two-stage >= 3pp, becomes main method contribution in §3.\"}, \"accum_v3_mix25\": {\"status\": \"DONE\", \"hypothesis\": \"Under 25/75 accumulation (mixing 25% human + 75% previous-depth synthetic text at each depth, then LoRA fine-tune + generate), depth signal attenuates to ~70% compared to full-replacement (84.2%). Comparable to mix50 (~69%, 1pp difference within seed noise of 2.04pp). Together with mix50, establishes accumulation degradation magnitude for Discussion §6.\"}, \"accum_v3_mix50\": {\"status\": \"DONE\", \"hypothesis\": \"Under 50/50 accumulation (mixing 50% human + 50% previous-depth synthetic text at each depth, then LoRA fine-tune + generate), depth signal attenuates to ~69% compared to full-replacement (84.2%), establishing that full-replacement results are a ceiling. Comparable to mix25 (~70%, within seed noise). Quantifies accumulation degradation for Discussion §6. Parent: invalidated accum_mix50 (feature-space mixing error).\"}, \"accum_mix50\": {\"status\": \"DONE\", \"hypothesis\": \"Accumulation scenario (50% human + 50% synthetic per depth) will degrade RF 4-class accuracy below full-replacement (84.2%), confirming that full-replacement results are an upper bound on feature separability. The degradation magnitude quantifies how much human-text mixing attenuates the depth signal.\"}, \"accum_mix25\": {\"status\": \"DONE\", \"hypothesis\": \"Accumulation scenario (25% human + 75% synthetic per depth) will show intermediate degradation between full-replacement (84.2%) and 50/50 mix, establishing a degradation curve that characterizes how human-text proportion affects depth separability.\"}, \"coral_ordinal_9cell_001\": {\"status\": \"DONE\", \"hypothesis\": \"CORAL ordinal regression with DNN backbone (19→64→32→CORAL) achieves comparable or superior 4-class accuracy to RF on all 9 atlas cells, while providing better ordinal consistency (monotonic predictions) and lower MAE due to ordinal-aware loss. Prior baseline_battery_9cell_001 showed RF≈CORAL with simple CORAL; DNN backbone may widen the gap. Algorithmic contribution: ordinal-specific classifier for depth estimation.\"}, \"lr_zscore_cross_strategy_001\": {\"status\": \"DONE\", \"hypothesis\": \"LR cross-strategy LOO + z-score: 验证 paper_framing 声称的 z-score 恢复 LR d1v2 AUC（GPT-2 XL 0.13→0.68, OLMo 0.25→0.83）。论文 claim 硬依赖。\"}, \"rf_21feature_augmented_001\": {\"status\": \"DONE\", \"hypothesis\": \"Adding Min-K% Prob and DetectGPT scores to the 19 statistical features will either show redundancy (detection scores add no info beyond statistical features) or complementarity (detection scores capture unique signal), both outcomes strengthen the paper narrative\"}, \"qwen25_14b_scale_003\": {\"status\": \"DONE\", \"hypothesis\": \"14B scale validation reproducibility: Qwen2.5-14B FP16 recursive chain on westd-48862 (RTX PRO 6000 Blackwell) produces consistent depth signal with gpu-6000pro-2 run, confirming results are not hardware-dependent.\"}, \"d4_extension_olmo_001\": {\"status\": \"DONE\", \"hypothesis\": \"OLMo-1B nucleus d4 depth extension: recursive generation depth signal persists at d4, completing 3/3 model coverage for EDD >= 4 verification.\"}, \"d4_extension_pythia_001\": {\"status\": \"DONE\", \"hypothesis\": \"Pythia-1.4B nucleus d4 depth extension: recursive generation depth signal persists at d4, providing second model evidence for EDD >= 4. d3v4 pairwise AUC > 0.70, 5-class RF accuracy well above 20% chance.\"}, \"d4_extension_gpt2xl_001\": {\"status\": \"DONE\", \"hypothesis\": \"GPT-2 XL nucleus d4 depth extension: recursive generation depth signal persists at d4 (5th recursive iteration). 5-class RF (d0-d4) accuracy remains significantly above 20% chance level, d3-vs-d4 pairwise AUC > 0.6, and key features (p90_ppl, var_surprisal, mean_ppl) continue monotonic trends observed in d0-d3.\"}, \"qwen25_14b_scale_002\": {\"status\": \"DONE\", \"hypothesis\": \"Recursive generation depth signal (statistical features distinguishing d0-d3) persists at 14B parameter scale (Qwen2.5-14B FP16), achieving RF 4-class accuracy significantly above 25% baseline, validating that model collapse signatures are not artifacts of small model capacity.\"}, \"olmo_seed43_001\": {\"status\": \"DONE\", \"hypothesis\": \"OLMo-1B with seed=43 and nucleus sampling (p=0.95) will reproduce the recursive generation depth signal (d0-d3 classification accuracy) observed in prior seeds, validating cross-seed reproducibility for the OLMo model family.\"}, \"pythia_seed43_001\": {\"status\": \"DONE\", \"hypothesis\": \"Pythia-1.4B recursive generation chain with seed=43 will produce depth-discriminative statistical features comparable to seed=42 (83.3% 4-class RF accuracy), confirming depth signal is inherent to recursive process not seed-specific.\"}, \"gpt2xl_seed43_001\": {\"status\": \"DONE\", \"hypothesis\": \"GPT-2 XL recursive generation depth signal is reproducible across random seeds: seed=43 should yield 4-class RF accuracy within 5pp of seed=42 baseline (83.3%), confirming depth degradation is inherent to the recursive fine-tuning process rather than LoRA weight initialization.\"}, \"prompted_gen_gpt2xl_001\": {\"status\": \"DONE\", \"hypothesis\": \"Prompted generation preserves depth signal: GPT-2 XL topic-prompted 4-class acc >= 70%, delta <= 15pp vs BOS-seeded baseline (83.3%)\"}, \"qwen25-1p5b-instruct-001\": {\"status\": \"DONE\", \"hypothesis\": \"Depth signal persists in instruction-tuned models: Qwen2.5-1.5B-Instruct recursive chain (nucleus p=0.95, d0-d3) achieves RF 4-class accuracy significantly above 25% baseline, demonstrating that instruction tuning does not eliminate model collapse signatures.\"}, \"learned_estimator_001\": {\"status\": \"DONE\", \"hypothesis\": \"Statistical features (19-dimensional: perplexity stats, surprisal, n-gram entropy, repetition ratios) can predict generation depth (0-3) with over 70% accuracy using learned classifiers (ordinal MLP, prototypical networks, XGBoost), and this generalizes across models in leave-one-out evaluation, because recursive generation progressively degrades text quality in statistically measurable ways.\"}, \"downstream_benchmark_001\": {\"status\": \"DONE\", \"hypothesis\": \"Depth-filtered training data (strict subset: depth 0-1 only) will produce better fine-tuned models than unfiltered or random data, because lower-depth text contains more original content with cleaner training signal, leading to lower perplexity on held-out evaluation after LoRA fine-tuning of Pythia-410M.\"}, \"qwen25-1p5b-instruct-002\": {\"status\": \"DONE\"}, \"qwen25-1p5b-instruct-001-ph45v3\": {\"status\": \"DONE\"}, \"qwen25-1p5b-instruct-001-ph45v2\": {\"status\": \"DONE\"}, \"qwen25-1p5b-instruct-001-ph45\": {\"status\": \"DONE\"}, \"qwen25-1p5b-instruct-001-phase45\": {\"status\": \"DONE\"}, \"learned_estimator_002\": {\"status\": \"DONE\", \"hypothesis\": \"Fixing NaN issues in Prototypical Network (torch.clamp + nan_to_num in distances, safe softmax conversion) and running full data sweep (no max_samples limit) will enable learned estimators (XGBoost, CORAL MLP, Prototypical) to exceed the RF baseline of 66.4% accuracy in cross-model depth estimation.\"}, \"wild_data_features_001\": {\"status\": \"DONE\", \"hypothesis\": \"Wild web corpora (C4, FineWeb) contain measurable proportions of text classified as recursive-generation depth d1+ by our RF estimator, providing evidence that model-generated text is present in training data.\"}, \"downstream_benchmark_002\": {\"status\": \"DONE\", \"hypothesis\": \"Fine-tuning on depth-0 (original) text produces lower held-out perplexity than fine-tuning on higher-depth (recursive) text, because d0 data has higher quality signal without recursive degradation artifacts.\"}, \"learned_estimator_proto_fix_001\": {\"status\": \"DONE\", \"hypothesis\": \"Prototypical Network with NaN fix (torch.clamp + nan_to_num on distance computation) achieves ~67.1% leave-one-model-out accuracy on 19 statistical features, comparable to RF baseline (66.4%), completing the learned estimator comparison matrix.\"}, \"detector_ord_baseline_001\": {\"status\": \"DONE\", \"hypothesis\": \"Existing AI-text detectors (Binoculars, Fast-DetectGPT) calibrated for ordinal depth estimation perform worse than our RF-on-19-features approach, confirming that depth-specific statistical features capture information beyond generic detection scores.\"}, \"plan_018_binoculars_baseline\": {\"status\": \"DONE\"}, \"bootstrap_ci_table1_001\": {\"status\": \"DONE\", \"hypothesis\": \"Bootstrap 95% CIs for all 9 cells of the 3×3 core matrix (3 models × 3 strategies) confirm that RF accuracy point estimates are stable (CI width ~1pp), and RF significantly outperforms LR in 8/9 cells.\"}, \"text_length_sensitivity_001\": {\"status\": \"DONE\", \"hypothesis\": \"Depth estimation accuracy degrades gracefully with shorter text truncation because the key statistical features (surprisal moments, entropy) converge within the first 100-200 tokens, making the method practical for short-text scenarios.\"}, \"qwen25_14b_scale_001\": {\"status\": \"DONE\", \"hypothesis\": \"Recursive generation depth signal (statistical features distinguishing d0-d3) persists at 14B parameter scale (Qwen2.5-14B FP16), achieving RF 4-class accuracy significantly above 25% baseline, validating that model collapse signatures are not artifacts of small model capacity.\"}, \"mlp_19feat_001\": {\"status\": \"DONE\", \"hypothesis\": \"2-layer MLP on 19 features achieves similar accuracy to RF (delta <= 3pp), confirming features rather than classifier as the performance bottleneck\"}, \"cross_strategy_pipeline_001\": {\"status\": \"DONE\", \"hypothesis\": \"Strategy classifier achieves >90% accuracy on 19 statistical features; two-stage pipeline (predict strategy then route to per-strategy depth RF) recovers cross-strategy depth accuracy to >=70% vs naive LOO 59.1%\"}, \"gen_length_ablation_001\": {\"status\": \"DONE\", \"hypothesis\": \"Depth signal scales with passage length: 128-token passages are detectable but weaker; 512-token passages match 256-token baseline; cross-length accuracy spread ≤ 5pp\"}, \"cross_seed_transfer_001\": {\"status\": \"DONE\", \"hypothesis\": \"If depth signal is an inherent property of recursive generation, an RF trained on seed=42 features should generalize to seed=43 features with cross-seed acc ≥ 75% (Δ ≤ 3pp vs within-seed)\"}, \"mixed_depth_corpus_001\": {\"status\": \"DONE\", \"hypothesis\": \"RF per-sample classifier does not rely on corpus-level depth distribution prior; accuracy on mixed-depth corpus (50/30/15/5%) should match balanced baseline within Δ ≤ 2pp\"}, \"ensemble_reference_001\": {\"status\": \"DONE\", \"hypothesis\": \"Ensemble reference (mean surprisal across multiple ref models) improves robustness vs worst single-model reference; ensemble acc should exceed GPT-2 XL-only (67.3%) by ≥5pp\"}, \"second_seed_replication_001\": {\"status\": \"DONE\", \"hypothesis\": \"递归生成 depth signal 是 recursive process 的固有属性而非特定 LoRA 权重的 idiosyncrasy；用不同 seed(=43) 训练的 LoRA 应产生与 seed=42 一致的 depth fingerprint（accuracy Δ ≤ 3pp vs 78.2%）\"}, \"reference_free_baseline_001\": {\"status\": \"DONE\", \"hypothesis\": \"Depth signal is partially accessible without reference model: reference-free token statistics (TTR, repetition, entropy, sentence length) achieve >60% 4-class accuracy (>2.5x chance)\"}, \"feat_ablation_v1\": {\"status\": \"DONE\", \"hypothesis\": \"A small subset of surprisal features (top-5 by RF importance) captures most depth signal: top-5 acc ≥95% of full 19-feature accuracy, identifying the minimal sufficient feature set for depth estimation\"}, \"feature_ablation_9cell\": {\"status\": \"DONE\", \"hypothesis\": \"Top-5 surprisal features achieve ≥90% of full 19-feature accuracy across all 9 atlas cells, confirming a minimal sufficient feature set independent of model/strategy combination\"}, \"depth_extension_olmo_d4d5_002\": {\"status\": \"DONE\", \"hypothesis\": \"OLMo-1B EDD 与 Pythia-1.4B 一致（EDD=4），验证 EDD 跨模型稳定性\"}, \"wild_data_calibration_005\": {\"status\": \"DONE\", \"hypothesis\": \"RedPajama web-crawl text is classified as d0 with FPR≤25%, consistent with C4/FineWeb calibration patterns, confirming cross-corpus robustness of depth classifier on diverse web data\"}, \"wild_data_calibration_004\": {\"status\": \"DONE\", \"hypothesis\": \"OpenWebText curated web text is classified as d0 with near-zero FPR (≤5%), confirming editorial curation quality correlates with lower false positive rates vs raw web-crawl\"}, \"gpt2xl_ref_ablation_001\": {\"status\": \"DONE\"}, \"ref_model_ablation_001\": {\"status\": \"DONE\", \"hypothesis\": \"OLMo-1B as alternative reference model yields depth classification within ±5pp of Pythia-1.4B reference, confirming surprisal-based features are not specific to a matched Pythia architecture\"}, \"baseline_battery_001\": {\"status\": \"DONE\", \"hypothesis\": \"Multiple classifier families (RF/LR/CORAL/CE-MLP/DivEye/PPL-Reg) achieve >40% 4-class accuracy on surprisal features, confirming depth signal is classifier-agnostic and not specific to RF decision boundaries\"}, \"batch_feature_extraction_5cells\": {\"status\": \"DONE\", \"hypothesis\": \"Feature extraction pipeline produces consistent 19-dim feature vectors across 5 new cells (GPT-2 XL + OLMo × 3 strategies), enabling downstream cross-model/cross-strategy generalization analysis\"}, \"cross_model_loo_v1\": {\"status\": \"DONE\", \"hypothesis\": \"RF trained on depth features from 2 generator models generalizes to held-out 3rd model with acc>50% (chance=25%), confirming depth features encode model-agnostic recursive degradation patterns\"}, \"cross_scale_llama3_8b_003\": {\"status\": \"DONE\", \"hypothesis\": \"Llama-3.1-8B-Instruct preserves monotonic AUC decay with EDD≥4 at 8B scale, confirming depth signal generalizes beyond 1-1.5B models to production-scale LLMs\"}, \"lora_rank_ablation_001\": {\"status\": \"DONE\", \"hypothesis\": \"LoRA rank (r∈{4,16,64}) minimally affects depth signal: accuracy spread ≤5pp across ranks would confirm depth signal is not an artifact of a specific LoRA fine-tuning configuration\"}, \"cross_scale_llama3_base_001\": {\"status\": \"DONE\"}, \"cross_model_reverse_chain_001\": {\"status\": \"DONE\"}, \"cross_scale_qwen7b_001\": {\"status\": \"DONE\", \"hypothesis\": \"Plan_014 7B cross-scale probe: Qwen2.5-7B nucleus p=0.95, d0-d5, 500 samples/depth。验证 depth signal 和 EDD 在 7B scale 上是否与 1-1.5B 模型一致。成功标准：4-class acc ≥ 60%, EDD 测定, pairwise AUC 衰减趋势方向一致。\"}, \"domain_extension_001\": {\"status\": \"DONE\", \"hypothesis\": \"Domain extension: 用 arXiv abstracts 替代 WikiText 作为 seed，验证 depth signal 是否 domain-independent。成功标准：4-class acc ≥ 65%, top features 与 WikiText pipeline 一致。\"}, \"cross_scale_llama3_8b_002\": {\"status\": \"DONE\"}, \"cross_model_recursive_chain_002\": {\"status\": \"DONE\"}, \"cross_model_recursive_chain_001\": {\"status\": \"DONE\", \"hypothesis\": \"Cross-model recursive chain: Human→Pythia d1→OLMo finetune→GPT-2 XL finetune。验证 depth signal 是否能跨越模型边界累积——即使每一步用不同模型递归，distributional artifacts 仍然可检测。成功标准：chain-d2/d3 的 pairwise AUC > chance, 4-class acc ≥ 50%。\"}, \"cross_scale_llama3_8b_001\": {\"status\": \"DONE\", \"hypothesis\": \"7B cross-scale probe (Llama-3-8B): 验证 depth signal 在 Llama-3 架构上的可检测性。Nucleus p=0.95, d0-d5, 500 samples/depth。成功标准：4-class acc ≥ 60%, EDD 测定, pairwise AUC 衰减趋势与 1-1.5B 模型方向一致。\"}, \"two_stage_strategy_pipeline_001\": {\"status\": \"DONE\", \"hypothesis\": \"Two-stage pipeline: 先分类 decoding strategy，再用 strategy-conditioned depth classifier。验证 Discussion 中提出的 two-stage 方案的可行性和瓶颈。\"}, \"multi_tau_ablation_001\": {\"status\": \"DONE\", \"hypothesis\": \"R2-W3 multi-τ ablation: 4 τ values (0.5, 0.7, 0.9, 1.1) × Pythia-1.4B。验证 depth classification signal 跨温度的鲁棒性，特别是 d1v2 AUC 是否随 τ 单调变化或在特定 τ 出现 inversion。Cross-τ LOO 验证跨温度泛化能力。\"}, \"zeroshot_qwen7b_500_001\": {\"status\": \"DONE\", \"hypothesis\": \"R1-W4 第二个 LLM baseline：Qwen2.5-7B-Instruct 4-bit zero-shot depth classification。与 DeepSeek-v3.2 (36.2%) 对比，验证 LLM zero-shot 在 depth task 上的一般性劣势（vs RF 78.2%）。\"}, \"wild_data_calibration_003\": {\"status\": \"DONE\", \"hypothesis\": \"Wild data calibration v3: 离线方案。先下载 RedPajama/Dolma 到本地磁盘，再用 wild_data_calibration_001 的 RF 模型评估 FPR。验证论文 wild-text calibration 在更多数据源上的泛化。\"}, \"wild_data_calibration_002\": {\"status\": \"DONE\"}, \"wild_data_redpajama_dolma_001\": {\"status\": \"DONE\"}, \"wild_data_calibration_001\": {\"status\": \"DONE\", \"hypothesis\": \"Classifiers trained on recursive generation data should correctly classify wild (human) text as d0 with low FPR, confirming calibration on out-of-distribution natural text\"}, \"random_soft_control_001\": {\"status\": \"DONE\"}, \"downstream_curation_poc_001\": {\"status\": \"DONE\"}, \"wild_data_olmo_calibration_001\": {\"status\": \"DONE\"}, \"pythia7b_cross_scale_001\": {\"status\": \"DONE\"}, \"wild_data_gpt2xl_calibration_001\": {\"status\": \"DONE\"}, \"wild_data_c4_supplement_001\": {\"status\": \"DONE\"}, \"w2_domain_bias_001\": {\"status\": \"DONE\"}, \"xgboost_lgbm_3cell_001\": {\"status\": \"DONE\"}, \"xgboost_lgbm_baseline_001\": {\"status\": \"DONE\"}, \"shap_supplement_001\": {\"status\": \"DONE\"}, \"zeroshot_llm_500_001\": {\"status\": \"DONE\", \"hypothesis\": \"R1-W4 zero-shot 样本量扩展: 从 200→500 samples 缩窄 CI。当前 200 samples 的 CI 过宽，500 samples 可将 CI 宽度缩小 ~37%，更可靠地与 RF 78.2% 对比。\"}, \"temp07_pilot_pythia_001\": {\"status\": \"DONE\", \"hypothesis\": \"R2-W3 multi-τ: τ=0.7 temperature pilot with Pythia-1.4B. 验证 d1v2 inversion 是否在 τ=0.7 也出现（对比 τ=0.9 的 GPT-2 XL 0.129 / OLMo 0.253）。若出现则 temperature inversion 是 τ<1 的通用现象；若不出现则 τ=0.9 是边界条件。\"}, \"n2_roberta_finetune_001\": {\"status\": \"DONE\", \"hypothesis\": \"N2 reviewer concern: end-to-end RoBERTa-base finetune baseline vs RF on hand-crafted features (78.2%). 与 DeBERTa 形成双 backbone 对比，排除模型选择偏差。\"}, \"n2_deberta_finetune_001\": {\"status\": \"DONE\", \"hypothesis\": \"N2 reviewer concern: end-to-end DeBERTa-v3-base finetune baseline vs RF on hand-crafted features (78.2%). 若 DeBERTa acc < RF，证明手工特征确有独立贡献；若 ≥ RF，需重新定位 narrative。\"}, \"cross_strategy_loo_001\": {\"status\": \"DONE\", \"hypothesis\": \"Cross-strategy LOO (plan_007): 深度信号跨策略可迁移——同模型内，用 2 种解码策略训练的 RF 可泛化到第 3 种，4-class acc 均值 59.1% 远超 chance 25%。temp09 holdout 的 d1v2 AUC 反转 (GPT-2 XL: 0.13, OLMo: 0.25) 证明解码策略塑造不同的退化轨迹 (D014)\"}, \"depth_extension_gpt2xl_d4d5_001\": {\"status\": \"DONE\", \"hypothesis\": \"GPT-2 XL depth extension: 从 d3 checkpoint 继续递归生成 d4/d5 各 5000 samples，binary pairwise RF 验证 EDD。GPT-2 XL 是 3×3 矩阵中信号最强的模型 (85.4%)，若 EDD≥4 则与 Pythia 结果 (EDD=4) 形成跨模型 EDD 一致性证据。\"}, \"depth_extension_olmo_d4d5_001\": {\"status\": \"DONE\", \"hypothesis\": \"OLMo-1B depth extension: 从 d3 checkpoint 继续递归生成 d4/d5 各 5000 samples，binary pairwise RF 验证 EDD。OLMo 是 3×3 矩阵中间模型 (78.8%)，若 EDD≥4 则与 Pythia (EDD=4) 形成跨模型 EDD 一致性证据，3 模型 EDD 完整对比。\"}, \"granularity_ablation_rf_001\": {\"status\": \"DONE\", \"hypothesis\": \"Granularity ablation: 对比 binary/3-class/4-class/6-class RF 性能，量化分类粒度对决策边界稀释的影响。预期 accuracy 随粒度增加单调下降，adjacent-pair AUC 在 binary 设置下最高。支持 Claim 1 (feasibility) + Claim 2 (EDD boundary dilution)。\"}, \"zero_shot_llm_baseline_001\": {\"status\": \"DONE\", \"hypothesis\": \"Zero-shot LLM baseline: DeepSeek V3.2 直接判断文本递归生成深度 (4-class)，无需统计特征提取。作为 upper-bound baseline 对比 feature-based 方法。\"}, \"olmo_temp09_002\": {\"status\": \"DONE\", \"hypothesis\": \"解码策略鲁棒性: OLMo-1B 在 temperature-only τ=0.9 下递归生成的深度信号与 nucleus p=0.95 一致（olmo_temp09_001 重跑，从 Step 3 断点恢复）\"}, \"depth_extension_pythia_d4d5_001\": {\"status\": \"DONE\", \"hypothesis\": \"Depth extension to d4/d5: EDD 从 d3 (当前 EDD=3 未饱和) 继续延伸——如果 d3v4 和 d4v5 AUC 仍 >0.75，则 EDD≥5，证明递归深度信号至少在 5 代内不饱和\"}, \"depth_extension_binary_pairwise_002\": {\"status\": \"DONE\", \"hypothesis\": \"Retry of binary_pairwise_001 (failed due to missing script on server). Dedicated binary RF for d3v4 and d4v5 pairwise AUC. Judgment: d3v4>0.75 + d4v5>0.75 → EDD≥5; d3v4>0.75 only → EDD=4.\"}, \"depth_extension_binary_pairwise_001\": {\"status\": \"DONE\", \"hypothesis\": \"Dedicated binary pairwise RF 评估 d3v4 和 d4v5 可区分性。6-class RF 的 pairwise AUC 因决策边界稀释不可靠（d2v3 从 4-class 0.80 降到 0.69 是 artifact）。Binary classifier 消除此 artifact，与原 4-class pipeline 的 d0v1/d1v2/d2v3 AUC 可比。判定标准：binary d3v4 AUC > 0.75 且 d4v5 AUC > 0.75 → EDD≥5；d3v4 > 0.75 但 d4v5 < 0.75 → EDD=4。\"}, \"dcol_roberta_v6_001\": {\"status\": \"DONE\", \"hypothesis\": \"DCOL v6: RoBERTa-large 替代 DeBERTa 解决数值不稳定。lr=5e-5 + grad clip 1.0 + NaN guard + collapse guard (step 500 acc&lt;30% kill)。若 4-class acc > RF baseline (78.2%) 则 DCOL 成功，否则降级为 negative result。\"}, \"cross_strategy_loo_zscore_001\": {\"status\": \"DONE\", \"hypothesis\": \"Z-score standardization recovers temp09 d1v2 AUC from covariate shift inversion in cross-strategy LOO (RF classifier)\"}, \"baseline_battery_9cell_001\": {\"status\": \"DONE\", \"hypothesis\": \"9-cell baseline battery: 4 种分类方法 (RF/LR/CORAL/DivEye) 在 3×3 矩阵全部 cells 上的 4-class accuracy 对比，生成 paper Table 1\"}, \"olmo_topk50_001\": {\"status\": \"DONE\", \"hypothesis\": \"解码策略鲁棒性: OLMo-1B 在 top-k k=50 下递归生成的深度信号与 nucleus p=0.95 一致，支持跨策略泛化\"}, \"atlas_v2_analysis\": {\"status\": \"DONE\", \"hypothesis\": \"Atlas v2 (9-cell): p90_ppl 和 var_surprisal 在所有 9 cells 中稳定为 top-2 features，EDD≥3 在多数 cells 成立，证明深度退化信号具有跨模型跨策略一致性\"}, \"cross_model_loo_001\": {\"status\": \"DONE\", \"hypothesis\": \"Cross-model LOO: 深度信号跨模型泛化，train on 2 families test on 3rd 的 4-class acc ≥ 45%（plan_005 gate）\"}, \"gpt2xl_topk50_001\": {\"status\": \"DONE\", \"hypothesis\": \"解码策略鲁棒性: GPT-2 XL 在 top-k k=50 下递归生成的深度信号与 nucleus p=0.95 一致，支持跨策略泛化\"}, \"dcol_deberta_005\": {\"status\": \"DONE\", \"hypothesis\": \"DCOL v5 (LoRA r=16 alpha=16, margin_lr=1e-4): DeBERTa-v3-large + LoRA + Contrastive Ordinal Loss，修正 margin_lr 从 1e-3 到 1e-4 避免 embedding collapse\"}, \"dcol_deberta_004\": {\"status\": \"DONE\", \"hypothesis\": \"DCOL v4 (LoRA r=16 alpha=16): DeBERTa-v3-large + LoRA + Contrastive Ordinal Loss，冻结 backbone 只训 LoRA adapter + head + margins\"}, \"dcol_deberta_003\": {\"status\": \"DONE\"}, \"olmo_temp09_001\": {\"status\": \"DONE\", \"hypothesis\": \"解码策略鲁棒性: OLMo-1B 在 temperature-only τ=0.9 下递归生成的深度信号与 nucleus p=0.95 一致，支持跨策略泛化\"}, \"atlas_v1_analysis\": {\"status\": \"DONE\", \"hypothesis\": \"Depth Degradation Atlas v1: 跨模型/策略的深度退化特征具有单调性(monotonicity)，EDD 可量化退化饱和点\"}, \"dcol_deberta_002\": {\"status\": \"DONE\", \"hypothesis\": \"DCOL v2 (修复 embedding collapse): margin_lr=1e-4, L2 norm, cl_weight=1.0\"}, \"gpt2xl_temp09_001\": {\"status\": \"DONE\", \"hypothesis\": \"解码策略鲁棒性: GPT-2 XL 在 temperature-only τ=0.9 下递归生成的深度信号与 nucleus p=0.95 一致，支持跨策略泛化\"}, \"dcol_deberta_001\": {\"status\": \"DONE\", \"hypothesis\": \"DCOL (DeBERTa-v3-large + Contrastive Ordinal Loss with learnable margins) 从原始文本直接预测递归生成深度，优于统计特征+RF方法\"}, \"cross_model_olmo_temp09_001\": {\"status\": \"DONE\", \"hypothesis\": \"OLMo-1B cross-model validation with temp_only decoding (t=0.9)\"}, \"pythia_topk50_001\": {\"status\": \"DONE\", \"hypothesis\": \"解码策略鲁棒性: Pythia-1.4B 在 top-k k=50 下递归生成的深度信号与 nucleus p=0.95 一致，支持跨策略泛化\"}, \"cross_model_gpt2xl_001\": {\"status\": \"DONE\"}, \"cross_model_olmo_002\": {\"status\": \"DONE\", \"hypothesis\": \"跨模型泛化: OLMo-1B 递归生成的统计特征与 Pythia-1.4B 一致，支持深度估计跨模型迁移 (重跑 olmo_001, 修复脚本 bug)\"}, \"pythia_temp09_001\": {\"status\": \"DONE\", \"hypothesis\": \"解码策略鲁棒性: Pythia-1.4B 在 temperature-only τ=0.9 下递归生成的深度信号与 nucleus p=0.95 一致，支持跨策略泛化\"}, \"mvp_pipeline_pythia_002\": {\"status\": \"DONE\"}, \"cross_model_olmo_001\": {\"status\": \"DONE\"}, \"mvp_pipeline_qwen_base_004\": {\"status\": \"DONE\"}, \"mvp_pipeline_pythia_001\": {\"status\": \"DONE\"}, \"mvp_pipeline_base_002\": {\"status\": \"DONE\"}, \"mvp_pipeline_003\": {\"status\": \"DONE\"}, \"mvp_pipeline_002\": {\"status\": \"DONE\"}, \"mvp_pipeline_001\": {\"status\": \"DONE\"}, \"mvp_pipeline_base_003\": {\"status\": \"DONE\"}, \"mvp_pipeline_004\": {\"status\": \"DONE\"}}, \"count\": 147, \"total\": 147, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5427}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 218_

<details><summary>Logged reasoning block</summary>

```text
Good. I found the experiment IDs:
- `accum_v3_mix50` — GPT-2 XL mix50 (the v2 accumulation for GPT-2 XL)
- `accum_pythia_nuc_mix50` — Pythia nucleus mix50
- `accum_olmo_temp_mix50` — OLMo temp09 mix50

Now let me update the registry metrics for all 3, then write the report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d4232873-36cc-4637-aa32-766dcf85d815",
  "uuid": "3ee3fe40-c4f3-403e-98d3-186cb8333d28",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0165qcksEmvoW6MxaEgEz76E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12529,
      "cache_read_input_tokens": 96899,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12529
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 219_

验证完成。现在并行更新 3 个实验的 registry metrics。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d4232873-36cc-4637-aa32-766dcf85d815",
  "uuid": "218d5cf3-3730-4992-8fb7-d51919914f1c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0165qcksEmvoW6MxaEgEz76E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12529,
      "cache_read_input_tokens": 96899,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12529
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 220_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01VX7zmRrxDbsiy8nV3Uu2Np`</summary>

```json
{
  "exp_id": "accum_v3_mix50",
  "field": "metrics",
  "value": {
    "rf_4class_acc": 0.6905,
    "verified_pairwise_auc_500tree": {
      "d0v1": 0.9996,
      "d1v2": 0.8305,
      "d2v3": 0.6945
    },
    "verified_pairwise_auc_200tree": {
      "d0v1": 0.9995,
      "d1v2": 0.8314,
      "d2v3": 0.6903
    },
    "edd_T070_500tree": 2,
    "edd_T070_200tree": 2,
    "verification_method": "binary RF, 500 trees, 5-fold stratified CV, seed=42",
    "verification_date": "2026-05-22"
  },
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d4232873-36cc-4637-aa32-766dcf85d815",
  "uuid": "4c51c3c0-f71f-40c2-8104-a5201c717e4f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0165qcksEmvoW6MxaEgEz76E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12529,
      "cache_read_input_tokens": 96899,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12529
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 221 · 2026-05-22T08:15:23.808Z_

<details><summary>↩ Tool result · `toolu_01VX7zmRrxDbsiy8nV3Uu2Np`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"accum_v3_mix50\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T08:08:06.546Z\", \"updated_at\": \"2026-05-22T08:15:23.442Z\", \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/recursive_gen_depth_est && bash scripts/run_accumulation_gpt2xl_nucleus.sh --mix_ratio 0.5 --cuda 0 --seed 42\\\"\", \"server\": \"westd-48862\", \"gpu\": [\"cuda:0\"], \"pid\": \"114337\", \"log_path\": \"~/runs/recursive_gen_depth_est/accum_v3_mix50.log\", \"submitted_at\": \"2026-05-19T08:17:14.577Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/recursive_gen_depth_est/data/gpt2xl/depth_0.jsonl + depth_1.jsonl\", \"data_count\": 5000, \"model_name\": \"gpt2-xl (LoRA) + EleutherAI/pythia-1.4b (feature ref)\", \"seed\": 42, \"mix_ratio\": 0.5, \"lora_config\": \"r=16 alpha=32 target=[c_attn,c_proj] dropout=0.05 lr=2e-4 epochs=3 bs=8\", \"feature_ref_model\": \"EleutherAI/pythia-1.4b\", \"checkpoint_path\": \"/root/autodl-tmp/recursive_gen_depth_est/checkpoints/accumulation_v2/mix50/\", \"wall_clock_seconds\": 17480.5, \"gpu_hours\": 4.86}, \"hypothesis\": \"Under 50/50 accumulation (mixing 50% human + 50% previous-depth synthetic text at each depth, then LoRA fine-tune + generate), depth signal attenuates to ~69% compared to full-replacement (84.2%), establishing that full-replacement results are a ceiling. Comparable to mix25 (~70%, within seed noise). Quantifies accumulation degradation for Discussion §6. Parent: invalidated accum_mix50 (feature-space mixing error).\", \"reproduce\": {\"finished_at\": \"2026-05-19T12:44:58.087Z\"}, \"metrics\": {\"rf_4class_acc\": 0.6905, \"verified_pairwise_auc_500tree\": {\"d0v1\": 0.9996, \"d1v2\": 0.8305, \"d2v3\": 0.6945}, \"verified_pairwise_auc_200tree\": {\"d0v1\": 0.9995, \"d1v2\": 0.8314, \"d2v3\": 0.6903}, \"edd_T070_500tree\": 2, \"edd_T070_200tree\": 2, \"verification_method\": \"binary RF, 500 trees, 5-fold stratified CV, seed=42\", \"verification_date\": \"2026-05-22\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T13:08:35.103Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8652}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d4232873-36cc-4637-aa32-766dcf85d815",
  "uuid": "0bb517b9-a36b-4972-a93b-96387267b73f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"accum_v3_mix50\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T08:08:06.546Z\\\", \\\"updated_at\\\": \\\"2026-05-22T08:15:23.442Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"cd /root/autodl-tmp/recursive_gen_depth_est && bash scripts/run_accumulation_gpt2xl_nucleus.sh --mix_ratio 0.5 --cuda 0 --seed 42\\\\\\\"\\\", \\\"server\\\": \\\"westd-48862\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"114337\\\", \\\"log_path\\\": \\\"~/runs/recursive_gen_depth_est/accum_v3_mix50.log\\\", \\\"submitted_at\\\": \\\"2026-05-19T08:17:14.577Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/recursive_gen_depth_est/data/gpt2xl/depth_0.jsonl + depth_1.jsonl\\\", \\\"data_count\\\": 5000, \\\"model_name\\\": \\\"gpt2-xl (LoRA) + EleutherAI/pythia-1.4b (feature ref)\\\", \\\"seed\\\": 42, \\\"mix_ratio\\\": 0.5, \\\"lora_config\\\": \\\"r=16 alpha=32 target=[c_attn,c_proj] dropout=0.05 lr=2e-4 epochs=3 bs=8\\\", \\\"feature_ref_model\\\": \\\"EleutherAI/pythia-1.4b\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/recursive_gen_depth_est/checkpoints/accumulation_v2/mix50/\\\", \\\"wall_clock_seconds\\\": 17480.5, \\\"gpu_hours\\\": 4.86}, \\\"hypothesis\\\": \\\"Under 50/50 accumulation (mixing 50% human + 50% previous-depth synthetic text at each depth, then LoRA fine-tune + generate), depth signal attenuates to ~69% compared to full-replacement (84.2%), establishing that full-replacement results are a ceiling. Comparable to mix25 (~70%, within seed noise). Quantifies accumulation degradation for Discussion §6. Parent: invalidated accum_mix50 (feature-space mixing error).\\\", \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-19T12:44:58.087Z\\\"}, \\\"metrics\\\": {\\\"rf_4class_acc\\\": 0.6905, \\\"verified_pairwise_auc_500tree\\\": {\\\"d0v1\\\": 0.9996, \\\"d1v2\\\": 0.8305, \\\"d2v3\\\": 0.6945}, \\\"verified_pairwise_auc_200tree\\\": {\\\"d0v1\\\": 0.9995, \\\"d1v2\\\": 0.8314, \\\"d2v3\\\": 0.6903}, \\\"edd_T070_500tree\\\": 2, \\\"edd_T070_200tree\\\": 2, \\\"verification_method\\\": \\\"binary RF, 500 trees, 5-fold stratified CV, seed=42\\\", \\\"verification_date\\\": \\\"2026-05-22\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-19T13:08:35.103Z\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.8652}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"accum_v3_mix50\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T08:08:06.546Z\", \"updated_at\": \"2026-05-22T08:15:23.442Z\", \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/recursive_gen_depth_est && bash scripts/run_accumulation_gpt2xl_nucleus.sh --mix_ratio 0.5 --cuda 0 --seed 42\\\"\", \"server\": \"westd-48862\", \"gpu\": [\"cuda:0\"], \"pid\": \"114337\", \"log_path\": \"~/runs/recursive_gen_depth_est/accum_v3_mix50.log\", \"submitted_at\": \"2026-05-19T08:17:14.577Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/recursive_gen_depth_est/data/gpt2xl/depth_0.jsonl + depth_1.jsonl\", \"data_count\": 5000, \"model_name\": \"gpt2-xl (LoRA) + EleutherAI/pythia-1.4b (feature ref)\", \"seed\": 42, \"mix_ratio\": 0.5, \"lora_config\": \"r=16 alpha=32 target=[c_attn,c_proj] dropout=0.05 lr=2e-4 epochs=3 bs=8\", \"feature_ref_model\": \"EleutherAI/pythia-1.4b\", \"checkpoint_path\": \"/root/autodl-tmp/recursive_gen_depth_est/checkpoints/accumulation_v2/mix50/\", \"wall_clock_seconds\": 17480.5, \"gpu_hours\": 4.86}, \"hypothesis\": \"Under 50/50 accumulation (mixing 50% human + 50% previous-depth synthetic text at each depth, then LoRA fine-tune + generate), depth signal attenuates to ~69% compared to full-replacement (84.2%), establishing that full-replacement results are a ceiling. Comparable to mix25 (~70%, within seed noise). Quantifies accumulation degradation for Discussion §6. Parent: invalidated accum_mix50 (feature-space mixing error).\", \"reproduce\": {\"finished_at\": \"2026-05-19T12:44:58.087Z\"}, \"metrics\": {\"rf_4class_acc\": 0.6905, \"verified_pairwise_auc_500tree\": {\"d0v1\": 0.9996, \"d1v2\": 0.8305, \"d2v3\": 0.6945}, \"verified_pairwise_auc_200tree\": {\"d0v1\": 0.9995, \"d1v2\": 0.8314, \"d2v3\": 0.6903}, \"edd_T070_500tree\": 2, \"edd_T070_200tree\": 2, \"verification_method\": \"binary RF, 500 trees, 5-fold stratified CV, seed=42\", \"verification_date\": \"2026-05-22\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T13:08:35.103Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8652}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 222_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01BnYxhKuns2P1K845Gn2A2T`</summary>

```json
{
  "exp_id": "accum_pythia_nuc_mix50",
  "field": "metrics",
  "value": {
    "rf_4class_acc": 0.6865,
    "verified_pairwise_auc_500tree": {
      "d0v1": 0.9999,
      "d1v2": 0.7925,
      "d2v3": 0.7159
    },
    "verified_pairwise_auc_200tree": {
      "d0v1": 0.9998,
      "d1v2": 0.7915,
      "d2v3": 0.7133
    },
    "edd_T070_500tree": 3,
    "edd_T070_200tree": 3,
    "verification_method": "binary RF, 500 trees, 5-fold stratified CV, seed=42",
    "verification_date": "2026-05-22"
  },
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d4232873-36cc-4637-aa32-766dcf85d815",
  "uuid": "2c33b280-f841-420b-b80e-ea4cd2b752ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0165qcksEmvoW6MxaEgEz76E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12529,
      "cache_read_input_tokens": 96899,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12529
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 223 · 2026-05-22T08:15:26.186Z_

<details><summary>↩ Tool result · `toolu_01BnYxhKuns2P1K845Gn2A2T`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"accum_pythia_nuc_mix50\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T02:11:04.592Z\", \"updated_at\": \"2026-05-22T08:15:25.841Z\", \"hypothesis\": \"Pythia-1.4B nucleus accumulation at 50% human mix ratio shows further signal degradation vs mix25 (70.77%), paralleling GPT-2 XL pattern (mix25 70.08% → mix50 69.05%)\", \"spec\": {\"command\": \"python3 scripts/accumulation_pipeline_pythia_nucleus.py --mix_ratio 0.5 --seed 42\", \"server\": \"gpu-6000pro-2\", \"gpu\": \"cuda:0\", \"pid\": \"907272\", \"log_path\": \"~/runs/recursive_gen_depth_est/accum_pythia_nuc_mix50.log\", \"submitted_at\": \"2026-05-22T02:12:11.209Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/pythia_nucleus/depth_0.jsonl + depth_1.jsonl\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-1.4b (LoRA) + EleutherAI/pythia-1.4b (feature ref)\", \"seed\": 42, \"mix_ratio\": 0.5, \"lora_config\": \"r=16 alpha=32 target=[query_key_value] dropout=0.05 lr=2e-4 epochs=3 bs=4 grad_accum=4\", \"feature_ref_model\": \"EleutherAI/pythia-1.4b\", \"wall_clock_seconds\": 9713.0, \"gpu_hours\": 2.7}, \"parent\": \"accum_pythia_nuc_002\", \"conclusion\": \"success\", \"metrics\": {\"rf_4class_acc\": 0.6865, \"verified_pairwise_auc_500tree\": {\"d0v1\": 0.9999, \"d1v2\": 0.7925, \"d2v3\": 0.7159}, \"verified_pairwise_auc_200tree\": {\"d0v1\": 0.9998, \"d1v2\": 0.7915, \"d2v3\": 0.7133}, \"edd_T070_500tree\": 3, \"edd_T070_200tree\": 3, \"verification_method\": \"binary RF, 500 trees, 5-fold stratified CV, seed=42\", \"verification_date\": \"2026-05-22\"}, \"checkpoint_path\": \"results/accumulation_v3/pythia_nucleus/mix50/summary.json\", \"completed_at\": \"2026-05-22T04:54:04.173Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8648}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d4232873-36cc-4637-aa32-766dcf85d815",
  "uuid": "aa370c46-0be4-4204-a6c8-a921afa1d0db",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"accum_pythia_nuc_mix50\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T02:11:04.592Z\\\", \\\"updated_at\\\": \\\"2026-05-22T08:15:25.841Z\\\", \\\"hypothesis\\\": \\\"Pythia-1.4B nucleus accumulation at 50% human mix ratio shows further signal degradation vs mix25 (70.77%), paralleling GPT-2 XL pattern (mix25 70.08% → mix50 69.05%)\\\", \\\"spec\\\": {\\\"command\\\": \\\"python3 scripts/accumulation_pipeline_pythia_nucleus.py --mix_ratio 0.5 --seed 42\\\", \\\"server\\\": \\\"gpu-6000pro-2\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": \\\"907272\\\", \\\"log_path\\\": \\\"~/runs/recursive_gen_depth_est/accum_pythia_nuc_mix50.log\\\", \\\"submitted_at\\\": \\\"2026-05-22T02:12:11.209Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"data/pythia_nucleus/depth_0.jsonl + depth_1.jsonl\\\", \\\"data_count\\\": 5000, \\\"model_name\\\": \\\"EleutherAI/pythia-1.4b (LoRA) + EleutherAI/pythia-1.4b (feature ref)\\\", \\\"seed\\\": 42, \\\"mix_ratio\\\": 0.5, \\\"lora_config\\\": \\\"r=16 alpha=32 target=[query_key_value] dropout=0.05 lr=2e-4 epochs=3 bs=4 grad_accum=4\\\", \\\"feature_ref_model\\\": \\\"EleutherAI/pythia-1.4b\\\", \\\"wall_clock_seconds\\\": 9713.0, \\\"gpu_hours\\\": 2.7}, \\\"parent\\\": \\\"accum_pythia_nuc_002\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"rf_4class_acc\\\": 0.6865, \\\"verified_pairwise_auc_500tree\\\": {\\\"d0v1\\\": 0.9999, \\\"d1v2\\\": 0.7925, \\\"d2v3\\\": 0.7159}, \\\"verified_pairwise_auc_200tree\\\": {\\\"d0v1\\\": 0.9998, \\\"d1v2\\\": 0.7915, \\\"d2v3\\\": 0.7133}, \\\"edd_T070_500tree\\\": 3, \\\"edd_T070_200tree\\\": 3, \\\"verification_method\\\": \\\"binary RF, 500 trees, 5-fold stratified CV, seed=42\\\", \\\"verification_date\\\": \\\"2026-05-22\\\"}, \\\"checkpoint_path\\\": \\\"results/accumulation_v3/pythia_nucleus/mix50/summary.json\\\", \\\"completed_at\\\": \\\"2026-05-22T04:54:04.173Z\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.8648}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"accum_pythia_nuc_mix50\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T02:11:04.592Z\", \"updated_at\": \"2026-05-22T08:15:25.841Z\", \"hypothesis\": \"Pythia-1.4B nucleus accumulation at 50% human mix ratio shows further signal degradation vs mix25 (70.77%), paralleling GPT-2 XL pattern (mix25 70.08% → mix50 69.05%)\", \"spec\": {\"command\": \"python3 scripts/accumulation_pipeline_pythia_nucleus.py --mix_ratio 0.5 --seed 42\", \"server\": \"gpu-6000pro-2\", \"gpu\": \"cuda:0\", \"pid\": \"907272\", \"log_path\": \"~/runs/recursive_gen_depth_est/accum_pythia_nuc_mix50.log\", \"submitted_at\": \"2026-05-22T02:12:11.209Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/pythia_nucleus/depth_0.jsonl + depth_1.jsonl\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-1.4b (LoRA) + EleutherAI/pythia-1.4b (feature ref)\", \"seed\": 42, \"mix_ratio\": 0.5, \"lora_config\": \"r=16 alpha=32 target=[query_key_value] dropout=0.05 lr=2e-4 epochs=3 bs=4 grad_accum=4\", \"feature_ref_model\": \"EleutherAI/pythia-1.4b\", \"wall_clock_seconds\": 9713.0, \"gpu_hours\": 2.7}, \"parent\": \"accum_pythia_nuc_002\", \"conclusion\": \"success\", \"metrics\": {\"rf_4class_acc\": 0.6865, \"verified_pairwise_auc_500tree\": {\"d0v1\": 0.9999, \"d1v2\": 0.7925, \"d2v3\": 0.7159}, \"verified_pairwise_auc_200tree\": {\"d0v1\": 0.9998, \"d1v2\": 0.7915, \"d2v3\": 0.7133}, \"edd_T070_500tree\": 3, \"edd_T070_200tree\": 3, \"verification_method\": \"binary RF, 500 trees, 5-fold stratified CV, seed=42\", \"verification_date\": \"2026-05-22\"}, \"checkpoint_path\": \"results/accumulation_v3/pythia_nucleus/mix50/summary.json\", \"completed_at\": \"2026-05-22T04:54:04.173Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8648}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 224_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01PkohND9XV9PsCiCPrExqMi`</summary>

```json
{
  "exp_id": "accum_olmo_temp_mix50",
  "field": "metrics",
  "value": {
    "rf_4class_acc": 0.7023,
    "verified_pairwise_auc_500tree": {
      "d0v1": 0.9999,
      "d1v2": 0.8166,
      "d2v3": 0.7262
    },
    "verified_pairwise_auc_200tree": {
      "d0v1": 0.9999,
      "d1v2": 0.8162,
      "d2v3": 0.7223
    },
    "edd_T070_500tree": 3,
    "edd_T070_200tree": 3,
    "verification_method": "binary RF, 500 trees, 5-fold stratified CV, seed=42",
    "verification_date": "2026-05-22"
  },
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d4232873-36cc-4637-aa32-766dcf85d815",
  "uuid": "a6bfcc6c-d19f-4740-bb5b-2ce4bb3cd932",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0165qcksEmvoW6MxaEgEz76E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12529,
      "cache_read_input_tokens": 96899,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12529
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 225 · 2026-05-22T08:15:29.421Z_

<details><summary>↩ Tool result · `toolu_01PkohND9XV9PsCiCPrExqMi`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"accum_olmo_temp_mix50\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T04:54:56.379Z\", \"updated_at\": \"2026-05-22T08:15:28.975Z\", \"hypothesis\": \"OLMo-1B temp0.9 accumulation at 50% human mix ratio shows further depth signal degradation vs mix25 (73.47%), paralleling GPT-2 XL pattern (mix25 70.08% → mix50 69.05%) and Pythia pattern, confirming cross-model consistency of accumulation mixing effects\", \"parent\": \"\", \"spec\": {\"command\": \"python3 scripts/accumulation_pipeline_olmo_temp09.py --mix_ratio 0.5 --seed 42\", \"server\": \"gpu-6000pro-2\", \"gpu\": \"cuda:0\", \"pid\": \"722400\", \"log_path\": \"~/runs/recursive_gen_depth_est/accum_olmo_temp_mix50.log\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/olmo_temp09/depth_0.jsonl + depth_1.jsonl\", \"data_count\": 5000, \"model_name\": \"OLMo-1B (LoRA) + OLMo-1B (feature ref)\", \"seed\": 42, \"mix_ratio\": 0.5, \"lora_config\": \"r=16 alpha=32 target=[q_proj,k_proj,v_proj] dropout=0.05 lr=2e-4 epochs=3 bs=4 grad_accum=4\", \"feature_ref_model\": \"OLMo-1B\", \"generation_params\": \"temperature=0.9, do_sample=True (no top_p/top_k)\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"results/accumulation_v3/olmo_temp09/mix50/\", \"log_path\": \"~/runs/recursive_gen_depth_est/accum_olmo_temp_mix50.log\", \"metrics\": {\"rf_4class_acc\": 0.7023, \"verified_pairwise_auc_500tree\": {\"d0v1\": 0.9999, \"d1v2\": 0.8166, \"d2v3\": 0.7262}, \"verified_pairwise_auc_200tree\": {\"d0v1\": 0.9999, \"d1v2\": 0.8162, \"d2v3\": 0.7223}, \"edd_T070_500tree\": 3, \"edd_T070_200tree\": 3, \"verification_method\": \"binary RF, 500 trees, 5-fold stratified CV, seed=42\", \"verification_date\": \"2026-05-22\"}, \"completed_at\": \"2026-05-22T07:56:28.621Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.2699}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d4232873-36cc-4637-aa32-766dcf85d815",
  "uuid": "ca5ffe0e-e438-4b5d-ad7e-727905f705a1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"accum_olmo_temp_mix50\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T04:54:56.379Z\\\", \\\"updated_at\\\": \\\"2026-05-22T08:15:28.975Z\\\", \\\"hypothesis\\\": \\\"OLMo-1B temp0.9 accumulation at 50% human mix ratio shows further depth signal degradation vs mix25 (73.47%), paralleling GPT-2 XL pattern (mix25 70.08% → mix50 69.05%) and Pythia pattern, confirming cross-model consistency of accumulation mixing effects\\\", \\\"parent\\\": \\\"\\\", \\\"spec\\\": {\\\"command\\\": \\\"python3 scripts/accumulation_pipeline_olmo_temp09.py --mix_ratio 0.5 --seed 42\\\", \\\"server\\\": \\\"gpu-6000pro-2\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": \\\"722400\\\", \\\"log_path\\\": \\\"~/runs/recursive_gen_depth_est/accum_olmo_temp_mix50.log\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"data/olmo_temp09/depth_0.jsonl + depth_1.jsonl\\\", \\\"data_count\\\": 5000, \\\"model_name\\\": \\\"OLMo-1B (LoRA) + OLMo-1B (feature ref)\\\", \\\"seed\\\": 42, \\\"mix_ratio\\\": 0.5, \\\"lora_config\\\": \\\"r=16 alpha=32 target=[q_proj,k_proj,v_proj] dropout=0.05 lr=2e-4 epochs=3 bs=4 grad_accum=4\\\", \\\"feature_ref_model\\\": \\\"OLMo-1B\\\", \\\"generation_params\\\": \\\"temperature=0.9, do_sample=True (no top_p/top_k)\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"checkpoint_path\\\": \\\"results/accumulation_v3/olmo_temp09/mix50/\\\", \\\"log_path\\\": \\\"~/runs/recursive_gen_depth_est/accum_olmo_temp_mix50.log\\\", \\\"metrics\\\": {\\\"rf_4class_acc\\\": 0.7023, \\\"verified_pairwise_auc_500tree\\\": {\\\"d0v1\\\": 0.9999, \\\"d1v2\\\": 0.8166, \\\"d2v3\\\": 0.7262}, \\\"verified_pairwise_auc_200tree\\\": {\\\"d0v1\\\": 0.9999, \\\"d1v2\\\": 0.8162, \\\"d2v3\\\": 0.7223}, \\\"edd_T070_500tree\\\": 3, \\\"edd_T070_200tree\\\": 3, \\\"verification_method\\\": \\\"binary RF, 500 trees, 5-fold stratified CV, seed=42\\\", \\\"verification_date\\\": \\\"2026-05-22\\\"}, \\\"completed_at\\\": \\\"2026-05-22T07:56:28.621Z\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.2699}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"accum_olmo_temp_mix50\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T04:54:56.379Z\", \"updated_at\": \"2026-05-22T08:15:28.975Z\", \"hypothesis\": \"OLMo-1B temp0.9 accumulation at 50% human mix ratio shows further depth signal degradation vs mix25 (73.47%), paralleling GPT-2 XL pattern (mix25 70.08% → mix50 69.05%) and Pythia pattern, confirming cross-model consistency of accumulation mixing effects\", \"parent\": \"\", \"spec\": {\"command\": \"python3 scripts/accumulation_pipeline_olmo_temp09.py --mix_ratio 0.5 --seed 42\", \"server\": \"gpu-6000pro-2\", \"gpu\": \"cuda:0\", \"pid\": \"722400\", \"log_path\": \"~/runs/recursive_gen_depth_est/accum_olmo_temp_mix50.log\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/olmo_temp09/depth_0.jsonl + depth_1.jsonl\", \"data_count\": 5000, \"model_name\": \"OLMo-1B (LoRA) + OLMo-1B (feature ref)\", \"seed\": 42, \"mix_ratio\": 0.5, \"lora_config\": \"r=16 alpha=32 target=[q_proj,k_proj,v_proj] dropout=0.05 lr=2e-4 epochs=3 bs=4 grad_accum=4\", \"feature_ref_model\": \"OLMo-1B\", \"generation_params\": \"temperature=0.9, do_sample=True (no top_p/top_k)\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"results/accumulation_v3/olmo_temp09/mix50/\", \"log_path\": \"~/runs/recursive_gen_depth_est/accum_olmo_temp_mix50.log\", \"metrics\": {\"rf_4class_acc\": 0.7023, \"verified_pairwise_auc_500tree\": {\"d0v1\": 0.9999, \"d1v2\": 0.8166, \"d2v3\": 0.7262}, \"verified_pairwise_auc_200tree\": {\"d0v1\": 0.9999, \"d1v2\": 0.8162, \"d2v3\": 0.7223}, \"edd_T070_500tree\": 3, \"edd_T070_200tree\": 3, \"verification_method\": \"binary RF, 500 trees, 5-fold stratified CV, seed=42\", \"verification_date\": \"2026-05-22\"}, \"completed_at\": \"2026-05-22T07:56:28.621Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.2699}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 226_

Registry 更新完毕。现在注册验证数据 artifact 并写报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d4232873-36cc-4637-aa32-766dcf85d815",
  "uuid": "09acba13-1f2b-47bc-83a6-8677742f0166",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DPBBTnTx48TN8JXeGr3yKJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3767,
      "cache_read_input_tokens": 109428,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3767
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 227_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01W7MEsxTiRCvQxpdze2zBqR`</summary>

```json
{
  "name": "accum_mix50_pairwise_auc_verified",
  "type": "data",
  "description": "Verified pairwise AUC for 3 mix50 accumulation cells (500-tree binary RF, 5-fold stratified CV, seed=42). Confirms EDD claim: 2/3 mix50 cells EDD=3, GPT-2 XL EDD=2.",
  "project": "recursive_gen_depth_est",
  "content": "{\n  \"method\": \"binary RF, 500 trees, 5-fold stratified CV, seed=42\",\n  \"timestamp\": \"2026-05-22T16:14:01.403187\",\n  \"results\": {\n    \"gpt2xl_nuc_mix50\": {\n      \"pairwise_auc_500tree\": {\"d0v1\": 0.9996, \"d1v2\": 0.8305, \"d2v3\": 0.6945},\n      \"pairwise_auc_200tree\": {\"d0v1\": 0.9995, \"d1v2\": 0.8314, \"d2v3\": 0.6903},\n      \"edd_T070\": 2, \"edd_T070_200tree\": 2\n    },\n    \"pythia_nuc_mix50\": {\n      \"pairwise_auc_500tree\": {\"d0v1\": 0.9999, \"d1v2\": 0.7925, \"d2v3\": 0.7159},\n      \"pairwise_auc_200tree\": {\"d0v1\": 0.9998, \"d1v2\": 0.7915, \"d2v3\": 0.7133},\n      \"edd_T070\": 3, \"edd_T070_200tree\": 3\n    },\n    \"olmo_temp_mix50\": {\n      \"pairwise_auc_500tree\": {\"d0v1\": 0.9999, \"d1v2\": 0.8166, \"d2v3\": 0.7262},\n      \"pairwise_auc_200tree\": {\"d0v1\": 0.9999, \"d1v2\": 0.8162, \"d2v3\": 0.7223},\n      \"edd_T070\": 3, \"edd_T070_200tree\": 3\n    }\n  }\n}",
  "content_filename": "accum_mix50_pairwise_auc_verified.json",
  "tags": [
    "accumulation",
    "pairwise_auc",
    "verification",
    "edd"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d4232873-36cc-4637-aa32-766dcf85d815",
  "uuid": "26aa5bcf-31ab-4ad1-8091-1ddb32f7267b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DPBBTnTx48TN8JXeGr3yKJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3767,
      "cache_read_input_tokens": 109428,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3767
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 228 · 2026-05-22T08:15:40.899Z_

<details><summary>↩ Tool result · reported error · `toolu_01W7MEsxTiRCvQxpdze2zBqR`</summary>

```text
Error executing tool register_artifact: 1 validation error for register_artifactArguments
content
  Input should be a valid string [type=string_type, input_value={'method': 'binary RF, 50...'edd_T070_200tree': 3}}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d4232873-36cc-4637-aa32-766dcf85d815",
  "uuid": "d4d71e0e-94d5-4b6c-bf21-1284623f21ba",
  "tool_use_result": "Error: Error executing tool register_artifact: 1 validation error for register_artifactArguments\ncontent\n  Input should be a valid string [type=string_type, input_value={'method': 'binary RF, 50...'edd_T070_200tree': 3}}}, input_type=dict]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type"
}
```

</details>

---


### Tool call

_source line 229_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01TyJtdvw7QSPma9KefEmte7`</summary>

```json
{
  "name": "accum_mix50_pairwise_auc_verified",
  "type": "data",
  "description": "Verified pairwise AUC for 3 mix50 accumulation cells (500-tree binary RF, 5-fold stratified CV, seed=42). Confirms EDD claim: 2/3 mix50 cells EDD=3, GPT-2 XL EDD=2.",
  "project": "recursive_gen_depth_est",
  "source_path": "/root/autodl-tmp/recursive_gen_depth_est/results/accum_mix50_pairwise_auc_verified.json",
  "tags": [
    "accumulation",
    "pairwise_auc",
    "verification",
    "edd"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d4232873-36cc-4637-aa32-766dcf85d815",
  "uuid": "942d8d47-0ed8-4f86-b4e9-6a1d46850425",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ST5zg2jjEqberfYBekF9oD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1001,
      "cache_read_input_tokens": 113195,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1001
      },
      "output_tokens": 70,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 230 · 2026-05-22T08:15:45.474Z_

<details><summary>↩ Tool result · `toolu_01TyJtdvw7QSPma9KefEmte7`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"source_path not found: /root/autodl-tmp/recursive_gen_depth_est/results/accum_mix50_pairwise_auc_verified.json\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d4232873-36cc-4637-aa32-766dcf85d815",
  "uuid": "d15674b7-3066-4819-8b29-abb93ff4327f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"source_path not found: /root/autodl-tmp/recursive_gen_depth_est/results/accum_mix50_pairwise_auc_verified.json\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"source_path not found: /root/autodl-tmp/recursive_gen_depth_est/results/accum_mix50_pairwise_auc_verified.json\", \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 231_

<details><summary>Logged reasoning block</summary>

```text
The artifact registration with source_path expects a local file, but it's on the remote server. Let me use content instead as a string.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d4232873-36cc-4637-aa32-766dcf85d815",
  "uuid": "786687f1-ccf1-442a-b72b-70ce78cd2595",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LFnwCHbvDSqhg7jHDvJrre",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 367,
      "cache_read_input_tokens": 114196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 367
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 232_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01LMtUMURA6DEvXxcdZML1cv`</summary>

```json
{
  "name": "accum_mix50_pairwise_auc_verified",
  "type": "data",
  "description": "Verified pairwise AUC for 3 mix50 accumulation cells (500-tree binary RF, 5-fold stratified CV, seed=42). Confirms EDD claim: 2/3 mix50 cells EDD=3, GPT-2 XL EDD=2.",
  "project": "recursive_gen_depth_est",
  "content": "{\"method\": \"binary RF, 500 trees, 5-fold stratified CV, seed=42\", \"timestamp\": \"2026-05-22T16:14:01\", \"results\": {\"gpt2xl_nuc_mix50\": {\"pairwise_auc_500tree\": {\"d0v1\": 0.9996, \"d1v2\": 0.8305, \"d2v3\": 0.6945}, \"pairwise_auc_200tree\": {\"d0v1\": 0.9995, \"d1v2\": 0.8314, \"d2v3\": 0.6903}, \"edd_T070\": 2}, \"pythia_nuc_mix50\": {\"pairwise_auc_500tree\": {\"d0v1\": 0.9999, \"d1v2\": 0.7925, \"d2v3\": 0.7159}, \"pairwise_auc_200tree\": {\"d0v1\": 0.9998, \"d1v2\": 0.7915, \"d2v3\": 0.7133}, \"edd_T070\": 3}, \"olmo_temp_mix50\": {\"pairwise_auc_500tree\": {\"d0v1\": 0.9999, \"d1v2\": 0.8166, \"d2v3\": 0.7262}, \"pairwise_auc_200tree\": {\"d0v1\": 0.9999, \"d1v2\": 0.8162, \"d2v3\": 0.7223}, \"edd_T070\": 3}}}",
  "content_filename": "accum_mix50_pairwise_auc_verified.json",
  "tags": [
    "accumulation",
    "pairwise_auc",
    "verification",
    "edd"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d4232873-36cc-4637-aa32-766dcf85d815",
  "uuid": "ba484ed5-879d-4b47-b64b-bfbbf73ada8f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LFnwCHbvDSqhg7jHDvJrre",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 367,
      "cache_read_input_tokens": 114196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 367
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 233 · 2026-05-22T08:15:53.480Z_

<details><summary>↩ Tool result · reported error · `toolu_01LMtUMURA6DEvXxcdZML1cv`</summary>

```text
Error executing tool register_artifact: 1 validation error for register_artifactArguments
content
  Input should be a valid string [type=string_type, input_value={'method': 'binary RF, 50....7223}, 'edd_T070': 3}}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d4232873-36cc-4637-aa32-766dcf85d815",
  "uuid": "144b6329-8212-4baa-9490-f28ec4854a60",
  "tool_use_result": "Error: Error executing tool register_artifact: 1 validation error for register_artifactArguments\ncontent\n  Input should be a valid string [type=string_type, input_value={'method': 'binary RF, 50....7223}, 'edd_T070': 3}}}, input_type=dict]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type"
}
```

</details>

---


### Tool call

_source line 234_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_013CohFh5eeS1LzWwhvCUGjz`</summary>

```json
{
  "name": "accum_mix50_pairwise_auc_verified",
  "type": "data",
  "description": "Verified pairwise AUC for 3 mix50 accumulation cells (500-tree binary RF, 5-fold stratified CV, seed=42). Confirms EDD claim: 2/3 mix50 cells EDD=3, GPT-2 XL EDD=2.",
  "project": "recursive_gen_depth_est",
  "content": "{\n  \"method\": \"binary RF, 500 trees, 5-fold stratified CV, seed=42\",\n  \"timestamp\": \"2026-05-22T16:14:01\",\n  \"results\": {\n    \"gpt2xl_nuc_mix50\": {\n      \"pairwise_auc_500tree\": {\"d0v1\": 0.9996, \"d1v2\": 0.8305, \"d2v3\": 0.6945},\n      \"pairwise_auc_200tree\": {\"d0v1\": 0.9995, \"d1v2\": 0.8314, \"d2v3\": 0.6903},\n      \"edd_T070\": 2\n    },\n    \"pythia_nuc_mix50\": {\n      \"pairwise_auc_500tree\": {\"d0v1\": 0.9999, \"d1v2\": 0.7925, \"d2v3\": 0.7159},\n      \"pairwise_auc_200tree\": {\"d0v1\": 0.9998, \"d1v2\": 0.7915, \"d2v3\": 0.7133},\n      \"edd_T070\": 3\n    },\n    \"olmo_temp_mix50\": {\n      \"pairwise_auc_500tree\": {\"d0v1\": 0.9999, \"d1v2\": 0.8166, \"d2v3\": 0.7262},\n      \"pairwise_auc_200tree\": {\"d0v1\": 0.9999, \"d1v2\": 0.8162, \"d2v3\": 0.7223},\n      \"edd_T070\": 3\n    }\n  }\n}\n",
  "content_filename": "accum_mix50_pairwise_auc_verified.json",
  "tags": [
    "accumulation",
    "pairwise_auc",
    "verification",
    "edd"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d4232873-36cc-4637-aa32-766dcf85d815",
  "uuid": "c94a67a1-ffea-4097-bc4f-f3fb5afa3c58",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014qVSx4Tm2JhQfYoBXuVGPE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 831,
      "cache_read_input_tokens": 114563,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 831
      },
      "output_tokens": 70,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 235 · 2026-05-22T08:16:02.896Z_

<details><summary>↩ Tool result · reported error · `toolu_013CohFh5eeS1LzWwhvCUGjz`</summary>

```text
Error executing tool register_artifact: 1 validation error for register_artifactArguments
content
  Input should be a valid string [type=string_type, input_value={'method': 'binary RF, 50....7223}, 'edd_T070': 3}}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d4232873-36cc-4637-aa32-766dcf85d815",
  "uuid": "535a0051-e243-4b5b-a503-2691530efa3c",
  "tool_use_result": "Error: Error executing tool register_artifact: 1 validation error for register_artifactArguments\ncontent\n  Input should be a valid string [type=string_type, input_value={'method': 'binary RF, 50....7223}, 'edd_T070': 3}}}, input_type=dict]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type"
}
```

</details>

---


### Assistant

_source line 236_

<details><summary>Logged reasoning block</summary>

```text
The content parameter is being parsed as a dict instead of a string. Let me try escaping it differently - maybe I need to use double-encoding or a different format. Let me try wrapping it as a plain text string.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d4232873-36cc-4637-aa32-766dcf85d815",
  "uuid": "dd8e3a99-5eec-4af6-a2a4-b3d66b5122f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HjsTredPyDL2vzKcQZBcif",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 834,
      "cache_read_input_tokens": 115394,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 834
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 237_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01RctgKgeCXxhxfJpKGcM8Co`</summary>

```json
{
  "name": "accum_mix50_pairwise_auc_verified",
  "type": "report",
  "description": "Verified pairwise AUC for 3 mix50 accumulation cells (500-tree binary RF, 5-fold stratified CV, seed=42). Confirms EDD claim: 2/3 mix50 cells EDD=3, GPT-2 XL EDD=2.",
  "project": "recursive_gen_depth_est",
  "content": "Pairwise AUC Verification Report — 3 mix50 Accumulation Cells\nMethod: Binary RF, 500 trees, 5-fold stratified CV, seed=42\nDate: 2026-05-22\n\nGPT-2 XL nucleus mix50:\n  d0v1: 500-tree=0.9996  200-tree=0.9995\n  d1v2: 500-tree=0.8305  200-tree=0.8314\n  d2v3: 500-tree=0.6945  200-tree=0.6903\n  EDD_0.70 = 2 (both 500 and 200 tree)\n\nPythia nucleus mix50:\n  d0v1: 500-tree=0.9999  200-tree=0.9998\n  d1v2: 500-tree=0.7925  200-tree=0.7915\n  d2v3: 500-tree=0.7159  200-tree=0.7133\n  EDD_0.70 = 3 (both 500 and 200 tree)\n\nOLMo temp09 mix50:\n  d0v1: 500-tree=0.9999  200-tree=0.9999\n  d1v2: 500-tree=0.8166  200-tree=0.8162\n  d2v3: 500-tree=0.7262  200-tree=0.7223\n  EDD_0.70 = 3 (both 500 and 200 tree)\n\nCLAIM CHECK: 2/3 mix50 cells have EDD>=3 (GPT-2 XL is the exception).\nCombined with 3/3 mix25 cells having EDD=3, paper claim \"5/6 cells preserve EDD_0.70=3\" is CONFIRMED.\n\nBASELINE ANALYSIS:\n- accumulation_pairwise_auc.json was computed with 200-tree binary RF (matching compute_accum_edd.py method)\n- 500-tree results differ by at most +0.0042 from 200-tree, EDD conclusions unchanged\n- GPT-2 XL d2v3 remains below 0.70 threshold (0.6945 at 500-tree vs 0.6903 at 200-tree)\n\nBASELINE SOURCE ISSUE:\n- GPT-2 XL pipeline hardcodes full_replacement_baseline=0.8428 (line 633/646)\n- Pythia pipeline ALSO hardcodes 0.8428 (same lines)\n- 0.8428 = GPT-2 XL seed-43 rerun accuracy (results/gpt2xl/rf_eval_seed42_rerun/summary.json)\n- Atlas v2 data shows: GPT-2 XL=83.3%, Pythia=78.2%, OLMo=82.0% (100-tree, 1000 samples/depth)\n- GPT-2 XL v2 mix25/mix50 summaries correctly used 0.859 as baseline (from an earlier pipeline run)\n- The current script was later modified to 0.8428, which is incorrect for GPT-2 XL (should be ~0.859)\n- Pythia baseline 0.8428 is completely wrong (should be ~0.78, it's GPT-2 XL's value)\n- OLMo pipeline has no baseline field at all\n\nFiles on server: /root/autodl-tmp/recursive_gen_depth_est/results/accum_mix50_pairwise_auc_verified.json",
  "content_filename": "accum_mix50_verification_report.txt",
  "tags": [
    "accumulation",
    "pairwise_auc",
    "verification",
    "edd",
    "baseline"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d4232873-36cc-4637-aa32-766dcf85d815",
  "uuid": "f3198d93-ec99-4afc-bd6d-1a53f2e47652",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HjsTredPyDL2vzKcQZBcif",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 834,
      "cache_read_input_tokens": 115394,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 834
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 238 · 2026-05-22T08:16:24.666Z_

<details><summary>↩ Tool result · `toolu_01RctgKgeCXxhxfJpKGcM8Co`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260522_46d805\", \"name\": \"accum_mix50_pairwise_auc_verified\", \"type\": \"report\", \"description\": \"Verified pairwise AUC for 3 mix50 accumulation cells (500-tree binary RF, 5-fold stratified CV, seed=42). Confirms EDD claim: 2/3 mix50 cells EDD=3, GPT-2 XL EDD=2.\", \"path\": \"projects/recursive_gen_depth_est/artifacts/_project/report/accum_mix50_verification_report.txt\", \"url\": null, \"project\": \"recursive_gen_depth_est\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-22T08:16:24.363129+00:00\", \"tags\": [\"accumulation\", \"pairwise_auc\", \"verification\", \"edd\", \"baseline\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d4232873-36cc-4637-aa32-766dcf85d815",
  "uuid": "b2eac914-025e-4b8d-865e-8d16a9d0d4c4",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260522_46d805\\\", \\\"name\\\": \\\"accum_mix50_pairwise_auc_verified\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Verified pairwise AUC for 3 mix50 accumulation cells (500-tree binary RF, 5-fold stratified CV, seed=42). Confirms EDD claim: 2/3 mix50 cells EDD=3, GPT-2 XL EDD=2.\\\", \\\"path\\\": \\\"projects/recursive_gen_depth_est/artifacts/_project/report/accum_mix50_verification_report.txt\\\", \\\"url\\\": null, \\\"project\\\": \\\"recursive_gen_depth_est\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-22T08:16:24.363129+00:00\\\", \\\"tags\\\": [\\\"accumulation\\\", \\\"pairwise_auc\\\", \\\"verification\\\", \\\"edd\\\", \\\"baseline\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260522_46d805\", \"name\": \"accum_mix50_pairwise_auc_verified\", \"type\": \"report\", \"description\": \"Verified pairwise AUC for 3 mix50 accumulation cells (500-tree binary RF, 5-fold stratified CV, seed=42). Confirms EDD claim: 2/3 mix50 cells EDD=3, GPT-2 XL EDD=2.\", \"path\": \"projects/recursive_gen_depth_est/artifacts/_project/report/accum_mix50_verification_report.txt\", \"url\": null, \"project\": \"recursive_gen_depth_est\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-22T08:16:24.363129+00:00\", \"tags\": [\"accumulation\", \"pairwise_auc\", \"verification\", \"edd\", \"baseline\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 239_

全部完成。总结：

---

## 任务 1: Pairwise AUC 验证结果

用 **500-tree binary RF, 5-fold stratified CV, seed=42** 重新计算了 3 个 mix50 cell 的 pairwise AUC：

| Cell | d0v1 | d1v2 | d2v3 | EDD₀.₇₀ |
|------|------|------|------|---------|
| GPT-2 XL mix50 | 0.9996 | 0.8305 | **0.6945** | **2** |
| Pythia mix50 | 0.9999 | 0.7925 | **0.7159** | **3** |
| OLMo mix50 | 0.9999 | 0.8166 | **0.7262** | **3** |

- 旧值（`accumulation_pairwise_auc.json`）是用 **200 trees** 计算的（完美复现），200→500 trees 差异 ≤ 0.0042
- **EDD 结论不受 tree 数量影响**：GPT-2 XL 始终 EDD=2，Pythia/OLMo 始终 EDD=3
- **论文 claim "5/6 cells preserve EDD₀.₇₀=3" 已确认**（mix25 3/3 + mix50 2/3 = 5/6）

## 任务 2: Baseline 来源分析

**发现严重 bug：**

1. **`accumulation_pipeline_gpt2xl.py` 和 `accumulation_pipeline_pythia_nucleus.py` 都硬编码了 `full_replacement_baseline = 0.8428`**
2. **0.8428 = GPT-2 XL seed-43 rerun 的 4-class RF accuracy**（`results/gpt2xl/rf_eval_seed42_rerun/summary.json`）
3. **Pythia 的 baseline 完全错误** — 0.8428 是 GPT-2 XL 的值，Pythia atlas 值是 78.2%
4. GPT-2 XL v2 results 里 baseline=0.859（旧脚本），当前脚本被改成了 0.8428
5. OLMo pipeline 没有 baseline 字段
6. Atlas v2 实际值：GPT-2 XL=83.3%, Pythia=78.2%, OLMo=82.0%（100 trees, 1000 samples/depth — 与 pipeline 的 200 trees / 5000 samples 不同）

**注意：这个 baseline 值只影响 summary.json 中的 `delta_vs_baseline` 显示，不影响 pairwise AUC 或 EDD 计算。** 但论文引用时需要用正确的 baseline。

## 产出

1. `results/accum_mix50_pairwise_auc_verified.json` — 服务器上已保存
2. Registry 已更新：`accum_v3_mix50`, `accum_pythia_nuc_mix50`, `accum_olmo_temp_mix50` 的 metrics 含 verified pairwise_auc
3. Artifact `art_20260522_46d805` 已注册（完整报告）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d4232873-36cc-4637-aa32-766dcf85d815",
  "uuid": "1693543c-3e3b-4338-ae10-ca72e28e9caf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011GDE6d7RH2uVmYrwHGjA1y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1560,
      "cache_read_input_tokens": 116228,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1560
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Task result

_source line 240_

全部完成。总结：

---

## 任务 1: Pairwise AUC 验证结果

用 **500-tree binary RF, 5-fold stratified CV, seed=42** 重新计算了 3 个 mix50 cell 的 pairwise AUC：

| Cell | d0v1 | d1v2 | d2v3 | EDD₀.₇₀ |
|------|------|------|------|---------|
| GPT-2 XL mix50 | 0.9996 | 0.8305 | **0.6945** | **2** |
| Pythia mix50 | 0.9999 | 0.7925 | **0.7159** | **3** |
| OLMo mix50 | 0.9999 | 0.8166 | **0.7262** | **3** |

- 旧值（`accumulation_pairwise_auc.json`）是用 **200 trees** 计算的（完美复现），200→500 trees 差异 ≤ 0.0042
- **EDD 结论不受 tree 数量影响**：GPT-2 XL 始终 EDD=2，Pythia/OLMo 始终 EDD=3
- **论文 claim "5/6 cells preserve EDD₀.₇₀=3" 已确认**（mix25 3/3 + mix50 2/3 = 5/6）

## 任务 2: Baseline 来源分析

**发现严重 bug：**

1. **`accumulation_pipeline_gpt2xl.py` 和 `accumulation_pipeline_pythia_nucleus.py` 都硬编码了 `full_replacement_baseline = 0.8428`**
2. **0.8428 = GPT-2 XL seed-43 rerun 的 4-class RF accuracy**（`results/gpt2xl/rf_eval_seed42_rerun/summary.json`）
3. **Pythia 的 baseline 完全错误** — 0.8428 是 GPT-2 XL 的值，Pythia atlas 值是 78.2%
4. GPT-2 XL v2 results 里 baseline=0.859（旧脚本），当前脚本被改成了 0.8428
5. OLMo pipeline 没有 baseline 字段
6. Atlas v2 实际值：GPT-2 XL=83.3%, Pythia=78.2%, OLMo=82.0%（100 trees, 1000 samples/depth — 与 pipeline 的 200 trees / 5000 samples 不同）

**注意：这个 baseline 值只影响 summary.json 中的 `delta_vs_baseline` 显示，不影响 pairwise AUC 或 EDD 计算。** 但论文引用时需要用正确的 baseline。

## 产出

1. `results/accum_mix50_pairwise_auc_verified.json` — 服务器上已保存
2. Registry 已更新：`accum_v3_mix50`, `accum_pythia_nuc_mix50`, `accum_olmo_temp_mix50` 的 metrics 含 verified pairwise_auc
3. Artifact `art_20260522_46d805` 已注册（完整报告）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 588197,
  "duration_api_ms": 457350,
  "num_turns": 98,
  "stop_reason": "end_turn",
  "session_id": "d4232873-36cc-4637-aa32-766dcf85d815",
  "total_cost_usd": 2.69287975,
  "usage": {
    "input_tokens": 39,
    "cache_creation_input_tokens": 105947,
    "cache_read_input_tokens": 2653660,
    "output_tokens": 28029,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 105947,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 900,
        "cache_read_input_tokens": 116228,
        "cache_creation_input_tokens": 1560,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1560
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2846,
      "outputTokens": 23,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002961,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 39,
      "outputTokens": 28029,
      "cacheReadInputTokens": 2653660,
      "cacheCreationInputTokens": 105947,
      "webSearchRequests": 0,
      "costUSD": 2.6899187499999995,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "eb2ec09c-4eb6-4847-a30e-75253772dc5d"
}
```

</details>

---
