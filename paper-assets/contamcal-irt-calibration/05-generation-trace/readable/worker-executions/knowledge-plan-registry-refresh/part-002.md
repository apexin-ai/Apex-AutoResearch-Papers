# knowledge plan registry refresh — Part 2 of 2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../knowledge-plan-registry-refresh.md) · [Structured JSON](../../../sessions/40/40ede6e08d6f4b48ab07.json)

## Round 1

### Tool call

_source line 115_

<details open><summary>🔧 Tool call — Edit · `toolu_01H23jr4qZStVrbwXswPPxo9`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/experiment_plan.yaml",
  "old_string": "    registry_id: exp_001_sft_d100_15B_v2\n    # Multi-run experiment; related registry entries:\n    # exp_001_sft_injection, exp_001_sft_0pct_05B (DONE), exp_001_sft_0pct_15B (DONE),\n    # exp_001_sft_0pct_3B, exp_001_sft_0pct_05B_s123, exp_001_sft_0pct_15B_s123,\n    # exp_001_sft_0pct_3B_s123, exp_001_sft_d100_05B (DONE), exp_001_sft_d005_05B (DONE),\n    # exp_001_eval_* (various)",
  "new_string": "    registry_id: exp_001_sft_injection\n    # Multi-run experiment; related successful registry entries:\n    # SFT training: exp_001_sft_0pct_05B, exp_001_sft_0pct_15B, exp_001_sft_0pct_3B,\n    #   exp_001_sft_0pct_05B_s123, exp_001_sft_0pct_15B_s123, exp_001_sft_0pct_3B_s123,\n    #   exp_001_sft_d005_05B_v3, exp_001_sft_d005_15B, exp_001_sft_d005_3B,\n    #   exp_001_sft_05B_d005_s123, exp_001_sft_15B_d005_s123_v2, exp_001_sft_3B_d005_s123,\n    #   exp_001_sft_d025_05B_v3, exp_001_sft_d025_15B, exp_001_sft_d025_3B_v2,\n    #   exp_001_sft_05B_d025_s123_v2, exp_001_sft_15B_d025_s123_v2, exp_001_sft_3B_d025_s123,\n    #   exp_001_sft_d100_05B, exp_001_sft_d100_15B_v2, exp_001_sft_d100_3B_v2,\n    #   exp_001_sft_05B_d100_s123, exp_001_sft_15B_d100_s123, exp_001_sft_3B_d100_s123,\n    #   exp_001_sft_3B_d000_v2, exp_001_sft_3B_d000_s123\n    # Eval (aligned): exp_001_eval_05B_d000_s123_aligned, exp_001_eval_05B_d005_aligned,\n    #   exp_001_eval_05B_d025_aligned, exp_001_eval_05B_d100_aligned_v4,\n    #   exp_001_eval_05B_d005_s123_aligned, exp_001_eval_05B_d025_s123_aligned,\n    #   exp_001_eval_05B_d100_s123_aligned, exp_001_eval_15B_aligned_batch,\n    #   exp_001_eval_15B_d005_aligned_v2, exp_001_eval_15B_d025_aligned,\n    #   exp_001_eval_15B_d100_aligned, exp_001_eval_15B_d000_s123_aligned,\n    #   exp_001_eval_15B_d100_s123_aligned, exp_001_eval_3B_d000_aligned,\n    #   exp_001_eval_3B_d005_aligned, exp_001_eval_3B_d100_aligned,\n    #   exp_001_eval_3B_d000_v2_aligned, exp_001_eval_3B_d025_v2_aligned,\n    #   exp_001_eval_3B_d100_v2_aligned_v2, exp_001_eval_3B_d000_s123_aligned,\n    #   exp_001_eval_3B_d005_s123_aligned, exp_001_eval_3B_d025_s123_aligned,\n    #   exp_001_eval_3B_d100_v2_s123_aligned, exp_001_eval_3B_d000_v2_s123_aligned\n    # Eval (para_aligned): exp_001_eval_05B_d005_para_aligned, exp_001_eval_05B_d025_aligned_v2,\n    #   exp_001_eval_05B_d005_s123_para_aligned, exp_001_eval_15B_d025_para_aligned,\n    #   exp_001_eval_3B_d000_s42_para_aligned, exp_001_eval_3B_d100_s42_para_aligned,\n    #   exp_001_eval_3B_d000_v2_para_aligned, exp_001_eval_3B_d000_v2_para_aligned_v2,\n    #   exp_001_eval_3B_d025_v2_para_aligned, exp_001_eval_3B_d100_v2_para_aligned,\n    #   exp_001_eval_3B_d005_s123_para_aligned, exp_001_eval_3B_d025_s123_para_aligned,\n    #   exp_001_eval_3B_d100_s123_para_aligned_v2, exp_001_eval_3B_d000_v2_s123_para_aligned\n    # Excluded from IRT pool: d000_s42 and d005_s42 experiments (lr=2e-4 confound, D076)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d61fa97d-0b3f-42cc-a383-d75fd89e4948",
  "uuid": "638161c9-5568-4e80-9dac-8b2b8764337b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cc8qvdwDtjDxFG2ksWT2XZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11983,
      "cache_read_input_tokens": 52916,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11983
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

_source line 116 · 2026-05-15T20:14:30.336Z_

<details><summary>↩ Tool result · `toolu_01H23jr4qZStVrbwXswPPxo9`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/experiment_plan.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d61fa97d-0b3f-42cc-a383-d75fd89e4948",
  "uuid": "85543d86-ae02-4826-85d5-62219dda8eff",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/experiment_plan.yaml",
    "oldString": "    registry_id: exp_001_sft_d100_15B_v2\n    # Multi-run experiment; related registry entries:\n    # exp_001_sft_injection, exp_001_sft_0pct_05B (DONE), exp_001_sft_0pct_15B (DONE),\n    # exp_001_sft_0pct_3B, exp_001_sft_0pct_05B_s123, exp_001_sft_0pct_15B_s123,\n    # exp_001_sft_0pct_3B_s123, exp_001_sft_d100_05B (DONE), exp_001_sft_d005_05B (DONE),\n    # exp_001_eval_* (various)",
    "newString": "    registry_id: exp_001_sft_injection\n    # Multi-run experiment; related successful registry entries:\n    # SFT training: exp_001_sft_0pct_05B, exp_001_sft_0pct_15B, exp_001_sft_0pct_3B,\n    #   exp_001_sft_0pct_05B_s123, exp_001_sft_0pct_15B_s123, exp_001_sft_0pct_3B_s123,\n    #   exp_001_sft_d005_05B_v3, exp_001_sft_d005_15B, exp_001_sft_d005_3B,\n    #   exp_001_sft_05B_d005_s123, exp_001_sft_15B_d005_s123_v2, exp_001_sft_3B_d005_s123,\n    #   exp_001_sft_d025_05B_v3, exp_001_sft_d025_15B, exp_001_sft_d025_3B_v2,\n    #   exp_001_sft_05B_d025_s123_v2, exp_001_sft_15B_d025_s123_v2, exp_001_sft_3B_d025_s123,\n    #   exp_001_sft_d100_05B, exp_001_sft_d100_15B_v2, exp_001_sft_d100_3B_v2,\n    #   exp_001_sft_05B_d100_s123, exp_001_sft_15B_d100_s123, exp_001_sft_3B_d100_s123,\n    #   exp_001_sft_3B_d000_v2, exp_001_sft_3B_d000_s123\n    # Eval (aligned): exp_001_eval_05B_d000_s123_aligned, exp_001_eval_05B_d005_aligned,\n    #   exp_001_eval_05B_d025_aligned, exp_001_eval_05B_d100_aligned_v4,\n    #   exp_001_eval_05B_d005_s123_aligned, exp_001_eval_05B_d025_s123_aligned,\n    #   exp_001_eval_05B_d100_s123_aligned, exp_001_eval_15B_aligned_batch,\n    #   exp_001_eval_15B_d005_aligned_v2, exp_001_eval_15B_d025_aligned,\n    #   exp_001_eval_15B_d100_aligned, exp_001_eval_15B_d000_s123_aligned,\n    #   exp_001_eval_15B_d100_s123_aligned, exp_001_eval_3B_d000_aligned,\n    #   exp_001_eval_3B_d005_aligned, exp_001_eval_3B_d100_aligned,\n    #   exp_001_eval_3B_d000_v2_aligned, exp_001_eval_3B_d025_v2_aligned,\n    #   exp_001_eval_3B_d100_v2_aligned_v2, exp_001_eval_3B_d000_s123_aligned,\n    #   exp_001_eval_3B_d005_s123_aligned, exp_001_eval_3B_d025_s123_aligned,\n    #   exp_001_eval_3B_d100_v2_s123_aligned, exp_001_eval_3B_d000_v2_s123_aligned\n    # Eval (para_aligned): exp_001_eval_05B_d005_para_aligned, exp_001_eval_05B_d025_aligned_v2,\n    #   exp_001_eval_05B_d005_s123_para_aligned, exp_001_eval_15B_d025_para_aligned,\n    #   exp_001_eval_3B_d000_s42_para_aligned, exp_001_eval_3B_d100_s42_para_aligned,\n    #   exp_001_eval_3B_d000_v2_para_aligned, exp_001_eval_3B_d000_v2_para_aligned_v2,\n    #   exp_001_eval_3B_d025_v2_para_aligned, exp_001_eval_3B_d100_v2_para_aligned,\n    #   exp_001_eval_3B_d005_s123_para_aligned, exp_001_eval_3B_d025_s123_para_aligned,\n    #   exp_001_eval_3B_d100_s123_para_aligned_v2, exp_001_eval_3B_d000_v2_s123_para_aligned\n    # Excluded from IRT pool: d000_s42 and d005_s42 experiments (lr=2e-4 confound, D076)",
    "originalFile": "# ContamCal Experiment Plan\n# Each experiment maps to Core Claims in paper_framing.md\n# Priority: P0 = must-run, P1 = important, P2 = bonus\n\nexperiments:\n  # ============================================================\n  # P0: Core experiments — must complete for submission\n  # ============================================================\n\n  - id: exp-001\n    name: controlled_sft_injection\n    claim: 1\n    description: >\n      SFT contamination injection on Qwen2.5-0.5B/1.5B/3B at 5 dosage levels\n      (0%, 5%, 25%, 50%, 100% benchmark items as paraphrases in SFT data).\n      Produces ground-truth contaminated/clean model pairs. 15 SFT runs total\n      (3 models × 5 dosages), parallelized across GPUs. 3 seeds per condition\n      for key metrics (mean ± std).\n      Paraphrase generation: use strong open LLM (Qwen2.5-72B-Instruct or\n      equivalent) with controlled semantic similarity — following methodology\n      of \"Rethinking Benchmark and Contamination\" (arXiv 2023). Target:\n      high semantic similarity (cosine >0.85) but low lexical overlap\n      (BLEU <0.3) to evade n-gram decontamination while preserving\n      contamination effect. Quality validation: automated similarity metrics\n      + human spot-check on 50 random pairs per benchmark.\n    priority: P0\n    gpu_budget_hours: 50\n    deps: []\n    benchmarks: [MMLU, GSM8K, ARC-Challenge, HumanEval]\n    models: [Qwen2.5-0.5B, Qwen2.5-1.5B, Qwen2.5-3B]\n    seeds: 3\n    registry_id: exp_001_sft_d100_15B_v2\n    # Multi-run experiment; related registry entries:\n    # exp_001_sft_injection, exp_001_sft_0pct_05B (DONE), exp_001_sft_0pct_15B (DONE),\n    # exp_001_sft_0pct_3B, exp_001_sft_0pct_05B_s123, exp_001_sft_0pct_15B_s123,\n    # exp_001_sft_0pct_3B_s123, exp_001_sft_d100_05B (DONE), exp_001_sft_d005_05B (DONE),\n    # exp_001_eval_* (various)\n\n  - id: exp-002\n    name: stage1_signal_pipeline\n    claim: 2\n    description: >\n      Compute 4 detection signals on all contaminated + clean models from exp-001:\n      (a) embedding-based semantic retrieval (FAISS + sentence-transformers),\n      (b) Min-K%++ membership inference,\n      (c) ConStat performance gap (original vs paraphrased items),\n      (d) Self-Critique entropy collapse.\n      Output: per-model-item exposure scores for each signal.\n    priority: P0\n    gpu_budget_hours: 20\n    deps: [exp-001]\n\n  - id: exp-003\n    name: rrf_aggregation_ablation\n    claim: 2\n    description: >\n      RRF fusion of 4 signals into composite per-item exposure score.\n      Ablations: (a) RRF vs equal-weight rank averaging, (b) single-signal only\n      (×4), (c) calibration-based weighted RRF variant, (d) false positive\n      injection robustness check (inject FP at rates matching Duan et al. 2024).\n      Also test degraded 2-signal mode (ConStat + Self-Critique) for closed-weight.\n    priority: P0\n    gpu_budget_hours: 2\n    deps: [exp-002]\n\n  - id: exp-004\n    name: simulation_identifiability_sweep\n    claim: 1\n    also_supports: [3]\n    description: >\n      Systematic synthetic-data sweep (NEW, not MVP — MVP only covered 4-5 conditions):\n      exposure signal AUC (0.55, 0.60, 0.65, 0.70, 0.80, 0.90) ×\n      model count (20, 50, 100, 200) ×\n      prior strength (N(0,0.5), N(0,1), N(0,2)) ×\n      exposure type (binary, continuous).\n      144 conditions, 10 seeds each. Reports: θ-γ recovery RMSE, posterior\n      correlation, coverage (50%/80%/95%), prior sensitivity. Establishes\n      minimum AUC threshold; if 95% CI width > 15pp at AUC=0.65, label as\n      \"cannot distinguish no contamination from moderate contamination.\"\n      N_items=300 fixed (per MVP finding).\n      Subsumes exp-010 (prior sensitivity) and exp-011 (few-examinee regime)\n      — prior × N_models dimensions already in sweep grid. Growing Pains\n      pre-estimation sub-experiment: at N_models=20/50, compare flat prior\n      vs informative prior from pre-estimated item parameters.\n      Also includes Fisher Information matrix analysis: derive approximate\n      analytical relationship between signal AUC, N_models, and γ\n      recoverability. Distinguish structural identifiability (parameters\n      uniquely determined) from practical identifiability (estimation\n      quality sufficient for decisions). Provides theoretical grounding\n      for the empirical AUC ≥ 0.70 threshold.\n    priority: P0\n    gpu_budget_hours: 0\n    deps: []\n    note: CPU only. MVP (mvp_sim_4pl_gamma) was preliminary; this is the full sweep.\n    registry_id: exp_004_sim_sweep\n    # Related: mvp_sim_4pl_gamma (DONE/success), mvp_sim_confounding (DONE/success)\n\n  - id: exp-005\n    name: noise_propagation_analysis\n    claim: 3\n    description: >\n      Two parts:\n      (A) Measurement error model (PRIMARY): extend Stan model to treat exposure\n      as noisy observation: exposure_ij ~ N(τ_ij, σ_e²), where τ is latent true\n      contamination. σ_e estimated from exp-001 ground truth FP/FN rates.\n      This propagates Stage 1 uncertainty into posteriors automatically.\n      Compare coverage (50%/80%/95%) vs point-estimate exposure baseline.\n      (B) Post-hoc noise injection: inject Gaussian noise at 1×/1.5×/2× matched\n      levels, re-fit standard model, measure CI widening for γ and θ.\n      Both parts inform whether measurement error model closes the coverage gap.\n    priority: P0\n    gpu_budget_hours: 0\n    deps: [exp-002, exp-004]\n    note: CPU only\n    registry_id: exp_005_noise_prop_v2\n    # Related: exp_005_noise_prop (v1, DONE/failed — sigma_e=0 bug)\n\n  - id: exp-006\n    name: irt_calibration_and_baselines\n    claim: 1\n    also_supports: [3]\n    description: >\n      Fit 4PL+γ IRT (Stan NUTS) on controlled models from exp-001/003.\n      PRIMARY: per-benchmark fitting with benchmark-specific γ_k — this is\n      the natural parameterization when IRT is fitted per-benchmark (each\n      benchmark's model has its own γ_k). ABLATION: joint fitting across\n      benchmarks with shared global γ (stronger assumption, tests whether\n      contamination effect is homogeneous across benchmarks). Report both.\n      Per-benchmark fitting (not joint) is the default to reduce local\n      independence violation scope. Posterior predictive checks on item-level residual\n      correlations to assess local independence empirically.\n      Compute calibrated scores via exposure=0 counterfactual with CIs.\n      Compare against 7 baselines:\n      (0) Raw — no adjustment (anchor),\n      (1) remove-and-rescore (drop flagged items),\n      (2) single-signal 2PL+γ (best signal only, simpler IRT),\n      (3) vanilla 4PL without γ (standard IRT, no contamination modeling),\n      (4) linear exposure regression + bootstrap CI (simplest post-hoc),\n      (5) Emperor's mitigation: rephrasing + option shuffling,\n      (6) DCR fuzzy inference (EMNLP 2025) — the only existing method\n          producing adjusted accuracy; must include or reviewers will reject.\n      Evaluate all 5 metrics: MAE, coverage (50%/80%/95%), sharpness,\n      Kendall τ, dose-response monotonicity.\n      Report mean ± std across 3 seeds (matched to exp-001 seeds).\n    priority: P0\n    gpu_budget_hours: 8\n    deps: [exp-003]\n    benchmarks: [MMLU, GSM8K, ARC-Challenge, HumanEval]\n    seeds: 3\n\n  # ============================================================\n  # P1: Important — run if time/GPU permit\n  # ============================================================\n\n  - id: exp-015\n    name: sft_d100_qc_only\n    claim: 1\n    description: >\n      100% dosage SFT using only QC-pass paraphrases (7547/16697 items).\n      Isolates noisy vs clean contamination confound identified by reviewer.\n      D012 decision. Compare calibration metrics against exp-001 d100 (all\n      paraphrases) to quantify effect of noisy contamination on IRT estimates.\n    priority: P1\n    gpu_budget_hours: 5\n    deps: [exp-001]\n    benchmarks: [MMLU, GSM8K, ARC-Challenge, HumanEval]\n    models: [Qwen2.5-0.5B]\n    seeds: 1\n    status: planned\n    registry_id: exp_001_sft_d100_qc_only\n    data_script: exp001/prepare_qc_only_data.py\n\n  - id: exp-007\n    name: scale_bridging_7b\n    claim: 1\n    description: >\n      Qwen2.5-7B controlled SFT injection at 5 dosage levels.\n      Validates calibration accuracy scales to larger models.\n      Requires multi-GPU node (7B LoRA SFT ~4-8h per run on 1×H100).\n    priority: P1\n    gpu_budget_hours: 30\n    deps: [exp-001]\n\n  - id: exp-008\n    name: signal_survival_analysis\n    claim: 2\n    description: >\n      Systematic evaluation of detection signal reliability across training regimes.\n      Signal × regime AUC heatmap: 4 signals × {base, SFT-clean, SFT-contaminated,\n      RL-post-trained}. Confirms Self-Critique compensates where Min-K%++/ConStat\n      degrade post-RL (per fragility paper arXiv 2510.02386).\n      ELEVATED to Core Contribution 2 per Dream review (all 3 tiers identified\n      this as the most genuinely novel finding).\n    priority: P0\n    gpu_budget_hours: 10\n    deps: [exp-002]\n\n  - id: exp-014\n    name: multi_family_validation\n    claim: 1\n    description: >\n      Controlled SFT injection on at least one non-Qwen model family\n      (Llama-3.2-1B or Pythia-1.4B) at 3 dosage levels (0%, 25%, 100%).\n      Validates that identifiability boundaries and calibration accuracy\n      generalize beyond Qwen2.5. Addresses Dream reviewer concern about\n      single model family limiting generalizability (flagged [M][W]).\n    priority: P1\n    gpu_budget_hours: 15\n    deps: [exp-001]\n\n  - id: exp-009\n    name: rl_observational_case_study\n    claim: 2\n    also_supports: [3]\n    description: >\n      Apply Self-Critique + available signals to existing RL-trained models:\n      Qwen2.5-Instruct (0.5B/1.5B/3B/7B), DeepSeek-R1-Distill-1.5B/7B.\n      Fit IRT with appropriately wider CIs. Expected regret quantification:\n      compare uncalibrated vs calibrated vs remove-rescore for top-5 model\n      selection. Framed as observational — directional external validity,\n      not full quantitative validation. Near-zero γ check on known-clean\n      benchmark (specificity test).\n    priority: P1\n    gpu_budget_hours: 15\n    deps: [exp-006, exp-008]\n\n  # exp-010 (prior_sensitivity) and exp-011 (few_examinee_regime) merged into exp-004.\n  # Prior × N_models dimensions already covered in the sweep grid.\n\n  # ============================================================\n  # P2: Bonus — adds breadth if resources allow\n  # ============================================================\n\n  - id: exp-012\n    name: observational_72b\n    claim: 1\n    description: >\n      Qwen2.5-72B observational analysis (inference only, no SFT).\n      Extends ecological validity to frontier model scale.\n    priority: P2\n    gpu_budget_hours: 15\n    deps: [exp-006]\n\n  - id: exp-013\n    name: closed_weight_2signal_mode\n    claim: 2\n    description: >\n      Degraded 2-signal mode (ConStat + Self-Critique, no logits/embeddings)\n      for closed-weight models. Ablation quantifying 2-signal vs 4-signal\n      calibration accuracy gap.\n    priority: P2\n    gpu_budget_hours: 5\n    deps: [exp-003]\n\n# ============================================================\n# GPU Budget Summary\n# ============================================================\ngpu_budget:\n  P0_hours: 90\n  P1_hours: 60\n  P2_hours: 20\n  buffer_hours: 30\n  total_hours: 200\n  note: >\n    CPU-only experiments (exp-004, exp-005, exp-011) excluded.\n    Buffer covers reruns, debugging, multi-seed overhead, and unexpected issues.\n    Requires 2-4× H100/A100-80G for parallel SFT runs.\n    EMNLP 2026 ARR May 25 sprint (12 days from May 13):\n    - With 4× H100: P0 in ~4 days, P1 in ~3 days, total ~8 days (fits deadline)\n    - With 2× H100: P0 in ~7 days, P1 in ~4 days, tight but feasible if parallelized\n    - Day-8 contingency: reduce benchmarks to MMLU + GSM8K if behind schedule\n\n# Multi-seed protocol:\n# - exp-001, exp-006: 3 seeds, report mean ± std for key metrics\n# - exp-004, exp-005, exp-011: 10 seeds (simulation, CPU)\n# - exp-007, exp-008, exp-009: 1 seed (resource-constrained, note as limitation if needed)\n",
    "structuredPatch": [
      {
        "oldStart": 29,
        "oldLines": 12,
        "newStart": 29,
        "newLines": 37,
        "lines": [
          "     benchmarks: [MMLU, GSM8K, ARC-Challenge, HumanEval]",
          "     models: [Qwen2.5-0.5B, Qwen2.5-1.5B, Qwen2.5-3B]",
          "     seeds: 3",
          "-    registry_id: exp_001_sft_d100_15B_v2",
          "-    # Multi-run experiment; related registry entries:",
          "-    # exp_001_sft_injection, exp_001_sft_0pct_05B (DONE), exp_001_sft_0pct_15B (DONE),",
          "-    # exp_001_sft_0pct_3B, exp_001_sft_0pct_05B_s123, exp_001_sft_0pct_15B_s123,",
          "-    # exp_001_sft_0pct_3B_s123, exp_001_sft_d100_05B (DONE), exp_001_sft_d005_05B (DONE),",
          "-    # exp_001_eval_* (various)",
          "+    registry_id: exp_001_sft_injection",
          "+    # Multi-run experiment; related successful registry entries:",
          "+    # SFT training: exp_001_sft_0pct_05B, exp_001_sft_0pct_15B, exp_001_sft_0pct_3B,",
          "+    #   exp_001_sft_0pct_05B_s123, exp_001_sft_0pct_15B_s123, exp_001_sft_0pct_3B_s123,",
          "+    #   exp_001_sft_d005_05B_v3, exp_001_sft_d005_15B, exp_001_sft_d005_3B,",
          "+    #   exp_001_sft_05B_d005_s123, exp_001_sft_15B_d005_s123_v2, exp_001_sft_3B_d005_s123,",
          "+    #   exp_001_sft_d025_05B_v3, exp_001_sft_d025_15B, exp_001_sft_d025_3B_v2,",
          "+    #   exp_001_sft_05B_d025_s123_v2, exp_001_sft_15B_d025_s123_v2, exp_001_sft_3B_d025_s123,",
          "+    #   exp_001_sft_d100_05B, exp_001_sft_d100_15B_v2, exp_001_sft_d100_3B_v2,",
          "+    #   exp_001_sft_05B_d100_s123, exp_001_sft_15B_d100_s123, exp_001_sft_3B_d100_s123,",
          "+    #   exp_001_sft_3B_d000_v2, exp_001_sft_3B_d000_s123",
          "+    # Eval (aligned): exp_001_eval_05B_d000_s123_aligned, exp_001_eval_05B_d005_aligned,",
          "+    #   exp_001_eval_05B_d025_aligned, exp_001_eval_05B_d100_aligned_v4,",
          "+    #   exp_001_eval_05B_d005_s123_aligned, exp_001_eval_05B_d025_s123_aligned,",
          "+    #   exp_001_eval_05B_d100_s123_aligned, exp_001_eval_15B_aligned_batch,",
          "+    #   exp_001_eval_15B_d005_aligned_v2, exp_001_eval_15B_d025_aligned,",
          "+    #   exp_001_eval_15B_d100_aligned, exp_001_eval_15B_d000_s123_aligned,",
          "+    #   exp_001_eval_15B_d100_s123_aligned, exp_001_eval_3B_d000_aligned,",
          "+    #   exp_001_eval_3B_d005_aligned, exp_001_eval_3B_d100_aligned,",
          "+    #   exp_001_eval_3B_d000_v2_aligned, exp_001_eval_3B_d025_v2_aligned,",
          "+    #   exp_001_eval_3B_d100_v2_aligned_v2, exp_001_eval_3B_d000_s123_aligned,",
          "+    #   exp_001_eval_3B_d005_s123_aligned, exp_001_eval_3B_d025_s123_aligned,",
          "+    #   exp_001_eval_3B_d100_v2_s123_aligned, exp_001_eval_3B_d000_v2_s123_aligned",
          "+    # Eval (para_aligned): exp_001_eval_05B_d005_para_aligned, exp_001_eval_05B_d025_aligned_v2,",
          "+    #   exp_001_eval_05B_d005_s123_para_aligned, exp_001_eval_15B_d025_para_aligned,",
          "+    #   exp_001_eval_3B_d000_s42_para_aligned, exp_001_eval_3B_d100_s42_para_aligned,",
          "+    #   exp_001_eval_3B_d000_v2_para_aligned, exp_001_eval_3B_d000_v2_para_aligned_v2,",
          "+    #   exp_001_eval_3B_d025_v2_para_aligned, exp_001_eval_3B_d100_v2_para_aligned,",
          "+    #   exp_001_eval_3B_d005_s123_para_aligned, exp_001_eval_3B_d025_s123_para_aligned,",
          "+    #   exp_001_eval_3B_d100_s123_para_aligned_v2, exp_001_eval_3B_d000_v2_s123_para_aligned",
          "+    # Excluded from IRT pool: d000_s42 and d005_s42 experiments (lr=2e-4 confound, D076)",
          " ",
          "   - id: exp-002",
          "     name: stage1_signal_pipeline"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Tool call

_source line 117_

<details open><summary>🔧 Tool call — Edit · `toolu_018vDrKazzr2wFEcW2QMeR9S`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/experiment_plan.yaml",
  "old_string": "    deps: [exp-001]\n\n  - id: exp-003",
  "new_string": "    deps: [exp-001]\n    registry_id: exp_002_signals_05B\n    # Related: exp002-signals-1p5B (DONE/success), exp002-signal-d025-05B (DONE/success)\n    # Note: 3B signal runs (exp_002_signals_3B v1-v4) all failed/killed\n\n  - id: exp-003"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d61fa97d-0b3f-42cc-a383-d75fd89e4948",
  "uuid": "325b8ec4-afdc-47e1-9062-8522b2a6d3f1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cc8qvdwDtjDxFG2ksWT2XZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11983,
      "cache_read_input_tokens": 52916,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11983
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

_source line 118 · 2026-05-15T20:14:31.930Z_

<details><summary>↩ Tool result · `toolu_018vDrKazzr2wFEcW2QMeR9S`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/experiment_plan.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d61fa97d-0b3f-42cc-a383-d75fd89e4948",
  "uuid": "d58ebe44-3344-4e46-844d-f9cec0c5be06",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/experiment_plan.yaml",
    "oldString": "    deps: [exp-001]\n\n  - id: exp-003",
    "newString": "    deps: [exp-001]\n    registry_id: exp_002_signals_05B\n    # Related: exp002-signals-1p5B (DONE/success), exp002-signal-d025-05B (DONE/success)\n    # Note: 3B signal runs (exp_002_signals_3B v1-v4) all failed/killed\n\n  - id: exp-003",
    "originalFile": "# ContamCal Experiment Plan\n# Each experiment maps to Core Claims in paper_framing.md\n# Priority: P0 = must-run, P1 = important, P2 = bonus\n\nexperiments:\n  # ============================================================\n  # P0: Core experiments — must complete for submission\n  # ============================================================\n\n  - id: exp-001\n    name: controlled_sft_injection\n    claim: 1\n    description: >\n      SFT contamination injection on Qwen2.5-0.5B/1.5B/3B at 5 dosage levels\n      (0%, 5%, 25%, 50%, 100% benchmark items as paraphrases in SFT data).\n      Produces ground-truth contaminated/clean model pairs. 15 SFT runs total\n      (3 models × 5 dosages), parallelized across GPUs. 3 seeds per condition\n      for key metrics (mean ± std).\n      Paraphrase generation: use strong open LLM (Qwen2.5-72B-Instruct or\n      equivalent) with controlled semantic similarity — following methodology\n      of \"Rethinking Benchmark and Contamination\" (arXiv 2023). Target:\n      high semantic similarity (cosine >0.85) but low lexical overlap\n      (BLEU <0.3) to evade n-gram decontamination while preserving\n      contamination effect. Quality validation: automated similarity metrics\n      + human spot-check on 50 random pairs per benchmark.\n    priority: P0\n    gpu_budget_hours: 50\n    deps: []\n    benchmarks: [MMLU, GSM8K, ARC-Challenge, HumanEval]\n    models: [Qwen2.5-0.5B, Qwen2.5-1.5B, Qwen2.5-3B]\n    seeds: 3\n    registry_id: exp_001_sft_injection\n    # Multi-run experiment; related successful registry entries:\n    # SFT training: exp_001_sft_0pct_05B, exp_001_sft_0pct_15B, exp_001_sft_0pct_3B,\n    #   exp_001_sft_0pct_05B_s123, exp_001_sft_0pct_15B_s123, exp_001_sft_0pct_3B_s123,\n    #   exp_001_sft_d005_05B_v3, exp_001_sft_d005_15B, exp_001_sft_d005_3B,\n    #   exp_001_sft_05B_d005_s123, exp_001_sft_15B_d005_s123_v2, exp_001_sft_3B_d005_s123,\n    #   exp_001_sft_d025_05B_v3, exp_001_sft_d025_15B, exp_001_sft_d025_3B_v2,\n    #   exp_001_sft_05B_d025_s123_v2, exp_001_sft_15B_d025_s123_v2, exp_001_sft_3B_d025_s123,\n    #   exp_001_sft_d100_05B, exp_001_sft_d100_15B_v2, exp_001_sft_d100_3B_v2,\n    #   exp_001_sft_05B_d100_s123, exp_001_sft_15B_d100_s123, exp_001_sft_3B_d100_s123,\n    #   exp_001_sft_3B_d000_v2, exp_001_sft_3B_d000_s123\n    # Eval (aligned): exp_001_eval_05B_d000_s123_aligned, exp_001_eval_05B_d005_aligned,\n    #   exp_001_eval_05B_d025_aligned, exp_001_eval_05B_d100_aligned_v4,\n    #   exp_001_eval_05B_d005_s123_aligned, exp_001_eval_05B_d025_s123_aligned,\n    #   exp_001_eval_05B_d100_s123_aligned, exp_001_eval_15B_aligned_batch,\n    #   exp_001_eval_15B_d005_aligned_v2, exp_001_eval_15B_d025_aligned,\n    #   exp_001_eval_15B_d100_aligned, exp_001_eval_15B_d000_s123_aligned,\n    #   exp_001_eval_15B_d100_s123_aligned, exp_001_eval_3B_d000_aligned,\n    #   exp_001_eval_3B_d005_aligned, exp_001_eval_3B_d100_aligned,\n    #   exp_001_eval_3B_d000_v2_aligned, exp_001_eval_3B_d025_v2_aligned,\n    #   exp_001_eval_3B_d100_v2_aligned_v2, exp_001_eval_3B_d000_s123_aligned,\n    #   exp_001_eval_3B_d005_s123_aligned, exp_001_eval_3B_d025_s123_aligned,\n    #   exp_001_eval_3B_d100_v2_s123_aligned, exp_001_eval_3B_d000_v2_s123_aligned\n    # Eval (para_aligned): exp_001_eval_05B_d005_para_aligned, exp_001_eval_05B_d025_aligned_v2,\n    #   exp_001_eval_05B_d005_s123_para_aligned, exp_001_eval_15B_d025_para_aligned,\n    #   exp_001_eval_3B_d000_s42_para_aligned, exp_001_eval_3B_d100_s42_para_aligned,\n    #   exp_001_eval_3B_d000_v2_para_aligned, exp_001_eval_3B_d000_v2_para_aligned_v2,\n    #   exp_001_eval_3B_d025_v2_para_aligned, exp_001_eval_3B_d100_v2_para_aligned,\n    #   exp_001_eval_3B_d005_s123_para_aligned, exp_001_eval_3B_d025_s123_para_aligned,\n    #   exp_001_eval_3B_d100_s123_para_aligned_v2, exp_001_eval_3B_d000_v2_s123_para_aligned\n    # Excluded from IRT pool: d000_s42 and d005_s42 experiments (lr=2e-4 confound, D076)\n\n  - id: exp-002\n    name: stage1_signal_pipeline\n    claim: 2\n    description: >\n      Compute 4 detection signals on all contaminated + clean models from exp-001:\n      (a) embedding-based semantic retrieval (FAISS + sentence-transformers),\n      (b) Min-K%++ membership inference,\n      (c) ConStat performance gap (original vs paraphrased items),\n      (d) Self-Critique entropy collapse.\n      Output: per-model-item exposure scores for each signal.\n    priority: P0\n    gpu_budget_hours: 20\n    deps: [exp-001]\n\n  - id: exp-003\n    name: rrf_aggregation_ablation\n    claim: 2\n    description: >\n      RRF fusion of 4 signals into composite per-item exposure score.\n      Ablations: (a) RRF vs equal-weight rank averaging, (b) single-signal only\n      (×4), (c) calibration-based weighted RRF variant, (d) false positive\n      injection robustness check (inject FP at rates matching Duan et al. 2024).\n      Also test degraded 2-signal mode (ConStat + Self-Critique) for closed-weight.\n    priority: P0\n    gpu_budget_hours: 2\n    deps: [exp-002]\n\n  - id: exp-004\n    name: simulation_identifiability_sweep\n    claim: 1\n    also_supports: [3]\n    description: >\n      Systematic synthetic-data sweep (NEW, not MVP — MVP only covered 4-5 conditions):\n      exposure signal AUC (0.55, 0.60, 0.65, 0.70, 0.80, 0.90) ×\n      model count (20, 50, 100, 200) ×\n      prior strength (N(0,0.5), N(0,1), N(0,2)) ×\n      exposure type (binary, continuous).\n      144 conditions, 10 seeds each. Reports: θ-γ recovery RMSE, posterior\n      correlation, coverage (50%/80%/95%), prior sensitivity. Establishes\n      minimum AUC threshold; if 95% CI width > 15pp at AUC=0.65, label as\n      \"cannot distinguish no contamination from moderate contamination.\"\n      N_items=300 fixed (per MVP finding).\n      Subsumes exp-010 (prior sensitivity) and exp-011 (few-examinee regime)\n      — prior × N_models dimensions already in sweep grid. Growing Pains\n      pre-estimation sub-experiment: at N_models=20/50, compare flat prior\n      vs informative prior from pre-estimated item parameters.\n      Also includes Fisher Information matrix analysis: derive approximate\n      analytical relationship between signal AUC, N_models, and γ\n      recoverability. Distinguish structural identifiability (parameters\n      uniquely determined) from practical identifiability (estimation\n      quality sufficient for decisions). Provides theoretical grounding\n      for the empirical AUC ≥ 0.70 threshold.\n    priority: P0\n    gpu_budget_hours: 0\n    deps: []\n    note: CPU only. MVP (mvp_sim_4pl_gamma) was preliminary; this is the full sweep.\n    registry_id: exp_004_sim_sweep\n    # Related: mvp_sim_4pl_gamma (DONE/success), mvp_sim_confounding (DONE/success)\n\n  - id: exp-005\n    name: noise_propagation_analysis\n    claim: 3\n    description: >\n      Two parts:\n      (A) Measurement error model (PRIMARY): extend Stan model to treat exposure\n      as noisy observation: exposure_ij ~ N(τ_ij, σ_e²), where τ is latent true\n      contamination. σ_e estimated from exp-001 ground truth FP/FN rates.\n      This propagates Stage 1 uncertainty into posteriors automatically.\n      Compare coverage (50%/80%/95%) vs point-estimate exposure baseline.\n      (B) Post-hoc noise injection: inject Gaussian noise at 1×/1.5×/2× matched\n      levels, re-fit standard model, measure CI widening for γ and θ.\n      Both parts inform whether measurement error model closes the coverage gap.\n    priority: P0\n    gpu_budget_hours: 0\n    deps: [exp-002, exp-004]\n    note: CPU only\n    registry_id: exp_005_noise_prop_v2\n    # Related: exp_005_noise_prop (v1, DONE/failed — sigma_e=0 bug)\n\n  - id: exp-006\n    name: irt_calibration_and_baselines\n    claim: 1\n    also_supports: [3]\n    description: >\n      Fit 4PL+γ IRT (Stan NUTS) on controlled models from exp-001/003.\n      PRIMARY: per-benchmark fitting with benchmark-specific γ_k — this is\n      the natural parameterization when IRT is fitted per-benchmark (each\n      benchmark's model has its own γ_k). ABLATION: joint fitting across\n      benchmarks with shared global γ (stronger assumption, tests whether\n      contamination effect is homogeneous across benchmarks). Report both.\n      Per-benchmark fitting (not joint) is the default to reduce local\n      independence violation scope. Posterior predictive checks on item-level residual\n      correlations to assess local independence empirically.\n      Compute calibrated scores via exposure=0 counterfactual with CIs.\n      Compare against 7 baselines:\n      (0) Raw — no adjustment (anchor),\n      (1) remove-and-rescore (drop flagged items),\n      (2) single-signal 2PL+γ (best signal only, simpler IRT),\n      (3) vanilla 4PL without γ (standard IRT, no contamination modeling),\n      (4) linear exposure regression + bootstrap CI (simplest post-hoc),\n      (5) Emperor's mitigation: rephrasing + option shuffling,\n      (6) DCR fuzzy inference (EMNLP 2025) — the only existing method\n          producing adjusted accuracy; must include or reviewers will reject.\n      Evaluate all 5 metrics: MAE, coverage (50%/80%/95%), sharpness,\n      Kendall τ, dose-response monotonicity.\n      Report mean ± std across 3 seeds (matched to exp-001 seeds).\n    priority: P0\n    gpu_budget_hours: 8\n    deps: [exp-003]\n    benchmarks: [MMLU, GSM8K, ARC-Challenge, HumanEval]\n    seeds: 3\n\n  # ============================================================\n  # P1: Important — run if time/GPU permit\n  # ============================================================\n\n  - id: exp-015\n    name: sft_d100_qc_only\n    claim: 1\n    description: >\n      100% dosage SFT using only QC-pass paraphrases (7547/16697 items).\n      Isolates noisy vs clean contamination confound identified by reviewer.\n      D012 decision. Compare calibration metrics against exp-001 d100 (all\n      paraphrases) to quantify effect of noisy contamination on IRT estimates.\n    priority: P1\n    gpu_budget_hours: 5\n    deps: [exp-001]\n    benchmarks: [MMLU, GSM8K, ARC-Challenge, HumanEval]\n    models: [Qwen2.5-0.5B]\n    seeds: 1\n    status: planned\n    registry_id: exp_001_sft_d100_qc_only\n    data_script: exp001/prepare_qc_only_data.py\n\n  - id: exp-007\n    name: scale_bridging_7b\n    claim: 1\n    description: >\n      Qwen2.5-7B controlled SFT injection at 5 dosage levels.\n      Validates calibration accuracy scales to larger models.\n      Requires multi-GPU node (7B LoRA SFT ~4-8h per run on 1×H100).\n    priority: P1\n    gpu_budget_hours: 30\n    deps: [exp-001]\n\n  - id: exp-008\n    name: signal_survival_analysis\n    claim: 2\n    description: >\n      Systematic evaluation of detection signal reliability across training regimes.\n      Signal × regime AUC heatmap: 4 signals × {base, SFT-clean, SFT-contaminated,\n      RL-post-trained}. Confirms Self-Critique compensates where Min-K%++/ConStat\n      degrade post-RL (per fragility paper arXiv 2510.02386).\n      ELEVATED to Core Contribution 2 per Dream review (all 3 tiers identified\n      this as the most genuinely novel finding).\n    priority: P0\n    gpu_budget_hours: 10\n    deps: [exp-002]\n\n  - id: exp-014\n    name: multi_family_validation\n    claim: 1\n    description: >\n      Controlled SFT injection on at least one non-Qwen model family\n      (Llama-3.2-1B or Pythia-1.4B) at 3 dosage levels (0%, 25%, 100%).\n      Validates that identifiability boundaries and calibration accuracy\n      generalize beyond Qwen2.5. Addresses Dream reviewer concern about\n      single model family limiting generalizability (flagged [M][W]).\n    priority: P1\n    gpu_budget_hours: 15\n    deps: [exp-001]\n\n  - id: exp-009\n    name: rl_observational_case_study\n    claim: 2\n    also_supports: [3]\n    description: >\n      Apply Self-Critique + available signals to existing RL-trained models:\n      Qwen2.5-Instruct (0.5B/1.5B/3B/7B), DeepSeek-R1-Distill-1.5B/7B.\n      Fit IRT with appropriately wider CIs. Expected regret quantification:\n      compare uncalibrated vs calibrated vs remove-rescore for top-5 model\n      selection. Framed as observational — directional external validity,\n      not full quantitative validation. Near-zero γ check on known-clean\n      benchmark (specificity test).\n    priority: P1\n    gpu_budget_hours: 15\n    deps: [exp-006, exp-008]\n\n  # exp-010 (prior_sensitivity) and exp-011 (few_examinee_regime) merged into exp-004.\n  # Prior × N_models dimensions already covered in the sweep grid.\n\n  # ============================================================\n  # P2: Bonus — adds breadth if resources allow\n  # ============================================================\n\n  - id: exp-012\n    name: observational_72b\n    claim: 1\n    description: >\n      Qwen2.5-72B observational analysis (inference only, no SFT).\n      Extends ecological validity to frontier model scale.\n    priority: P2\n    gpu_budget_hours: 15\n    deps: [exp-006]\n\n  - id: exp-013\n    name: closed_weight_2signal_mode\n    claim: 2\n    description: >\n      Degraded 2-signal mode (ConStat + Self-Critique, no logits/embeddings)\n      for closed-weight models. Ablation quantifying 2-signal vs 4-signal\n      calibration accuracy gap.\n    priority: P2\n    gpu_budget_hours: 5\n    deps: [exp-003]\n\n# ============================================================\n# GPU Budget Summary\n# ============================================================\ngpu_budget:\n  P0_hours: 90\n  P1_hours: 60\n  P2_hours: 20\n  buffer_hours: 30\n  total_hours: 200\n  note: >\n    CPU-only experiments (exp-004, exp-005, exp-011) excluded.\n    Buffer covers reruns, debugging, multi-seed overhead, and unexpected issues.\n    Requires 2-4× H100/A100-80G for parallel SFT runs.\n    EMNLP 2026 ARR May 25 sprint (12 days from May 13):\n    - With 4× H100: P0 in ~4 days, P1 in ~3 days, total ~8 days (fits deadline)\n    - With 2× H100: P0 in ~7 days, P1 in ~4 days, tight but feasible if parallelized\n    - Day-8 contingency: reduce benchmarks to MMLU + GSM8K if behind schedule\n\n# Multi-seed protocol:\n# - exp-001, exp-006: 3 seeds, report mean ± std for key metrics\n# - exp-004, exp-005, exp-011: 10 seeds (simulation, CPU)\n# - exp-007, exp-008, exp-009: 1 seed (resource-constrained, note as limitation if needed)\n",
    "structuredPatch": [
      {
        "oldStart": 74,
        "oldLines": 6,
        "newStart": 74,
        "newLines": 9,
        "lines": [
          "     priority: P0",
          "     gpu_budget_hours: 20",
          "     deps: [exp-001]",
          "+    registry_id: exp_002_signals_05B",
          "+    # Related: exp002-signals-1p5B (DONE/success), exp002-signal-d025-05B (DONE/success)",
          "+    # Note: 3B signal runs (exp_002_signals_3B v1-v4) all failed/killed",
          " ",
          "   - id: exp-003",
          "     name: rrf_aggregation_ablation"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Tool call

_source line 119_

<details open><summary>🔧 Tool call — Edit · `toolu_01LRm2AmfP5hprgscXG3vpGp`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/experiment_plan.yaml",
  "old_string": "    deps: [exp-002]\n\n  - id: exp-004",
  "new_string": "    deps: [exp-002]\n    registry_id: exp_003_rrf_05B\n    # Related: exp_003_mmlu_item_aligned_gap (DONE/success)\n\n  - id: exp-004"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d61fa97d-0b3f-42cc-a383-d75fd89e4948",
  "uuid": "44252e5e-6e2a-40bb-87fd-582dff80a4fc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cc8qvdwDtjDxFG2ksWT2XZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11983,
      "cache_read_input_tokens": 52916,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11983
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

_source line 120 · 2026-05-15T20:14:33.370Z_

<details><summary>↩ Tool result · `toolu_01LRm2AmfP5hprgscXG3vpGp`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/experiment_plan.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d61fa97d-0b3f-42cc-a383-d75fd89e4948",
  "uuid": "21bd2c21-6f9f-4559-b96a-0ee03452a348",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/experiment_plan.yaml",
    "oldString": "    deps: [exp-002]\n\n  - id: exp-004",
    "newString": "    deps: [exp-002]\n    registry_id: exp_003_rrf_05B\n    # Related: exp_003_mmlu_item_aligned_gap (DONE/success)\n\n  - id: exp-004",
    "originalFile": "# ContamCal Experiment Plan\n# Each experiment maps to Core Claims in paper_framing.md\n# Priority: P0 = must-run, P1 = important, P2 = bonus\n\nexperiments:\n  # ============================================================\n  # P0: Core experiments — must complete for submission\n  # ============================================================\n\n  - id: exp-001\n    name: controlled_sft_injection\n    claim: 1\n    description: >\n      SFT contamination injection on Qwen2.5-0.5B/1.5B/3B at 5 dosage levels\n      (0%, 5%, 25%, 50%, 100% benchmark items as paraphrases in SFT data).\n      Produces ground-truth contaminated/clean model pairs. 15 SFT runs total\n      (3 models × 5 dosages), parallelized across GPUs. 3 seeds per condition\n      for key metrics (mean ± std).\n      Paraphrase generation: use strong open LLM (Qwen2.5-72B-Instruct or\n      equivalent) with controlled semantic similarity — following methodology\n      of \"Rethinking Benchmark and Contamination\" (arXiv 2023). Target:\n      high semantic similarity (cosine >0.85) but low lexical overlap\n      (BLEU <0.3) to evade n-gram decontamination while preserving\n      contamination effect. Quality validation: automated similarity metrics\n      + human spot-check on 50 random pairs per benchmark.\n    priority: P0\n    gpu_budget_hours: 50\n    deps: []\n    benchmarks: [MMLU, GSM8K, ARC-Challenge, HumanEval]\n    models: [Qwen2.5-0.5B, Qwen2.5-1.5B, Qwen2.5-3B]\n    seeds: 3\n    registry_id: exp_001_sft_injection\n    # Multi-run experiment; related successful registry entries:\n    # SFT training: exp_001_sft_0pct_05B, exp_001_sft_0pct_15B, exp_001_sft_0pct_3B,\n    #   exp_001_sft_0pct_05B_s123, exp_001_sft_0pct_15B_s123, exp_001_sft_0pct_3B_s123,\n    #   exp_001_sft_d005_05B_v3, exp_001_sft_d005_15B, exp_001_sft_d005_3B,\n    #   exp_001_sft_05B_d005_s123, exp_001_sft_15B_d005_s123_v2, exp_001_sft_3B_d005_s123,\n    #   exp_001_sft_d025_05B_v3, exp_001_sft_d025_15B, exp_001_sft_d025_3B_v2,\n    #   exp_001_sft_05B_d025_s123_v2, exp_001_sft_15B_d025_s123_v2, exp_001_sft_3B_d025_s123,\n    #   exp_001_sft_d100_05B, exp_001_sft_d100_15B_v2, exp_001_sft_d100_3B_v2,\n    #   exp_001_sft_05B_d100_s123, exp_001_sft_15B_d100_s123, exp_001_sft_3B_d100_s123,\n    #   exp_001_sft_3B_d000_v2, exp_001_sft_3B_d000_s123\n    # Eval (aligned): exp_001_eval_05B_d000_s123_aligned, exp_001_eval_05B_d005_aligned,\n    #   exp_001_eval_05B_d025_aligned, exp_001_eval_05B_d100_aligned_v4,\n    #   exp_001_eval_05B_d005_s123_aligned, exp_001_eval_05B_d025_s123_aligned,\n    #   exp_001_eval_05B_d100_s123_aligned, exp_001_eval_15B_aligned_batch,\n    #   exp_001_eval_15B_d005_aligned_v2, exp_001_eval_15B_d025_aligned,\n    #   exp_001_eval_15B_d100_aligned, exp_001_eval_15B_d000_s123_aligned,\n    #   exp_001_eval_15B_d100_s123_aligned, exp_001_eval_3B_d000_aligned,\n    #   exp_001_eval_3B_d005_aligned, exp_001_eval_3B_d100_aligned,\n    #   exp_001_eval_3B_d000_v2_aligned, exp_001_eval_3B_d025_v2_aligned,\n    #   exp_001_eval_3B_d100_v2_aligned_v2, exp_001_eval_3B_d000_s123_aligned,\n    #   exp_001_eval_3B_d005_s123_aligned, exp_001_eval_3B_d025_s123_aligned,\n    #   exp_001_eval_3B_d100_v2_s123_aligned, exp_001_eval_3B_d000_v2_s123_aligned\n    # Eval (para_aligned): exp_001_eval_05B_d005_para_aligned, exp_001_eval_05B_d025_aligned_v2,\n    #   exp_001_eval_05B_d005_s123_para_aligned, exp_001_eval_15B_d025_para_aligned,\n    #   exp_001_eval_3B_d000_s42_para_aligned, exp_001_eval_3B_d100_s42_para_aligned,\n    #   exp_001_eval_3B_d000_v2_para_aligned, exp_001_eval_3B_d000_v2_para_aligned_v2,\n    #   exp_001_eval_3B_d025_v2_para_aligned, exp_001_eval_3B_d100_v2_para_aligned,\n    #   exp_001_eval_3B_d005_s123_para_aligned, exp_001_eval_3B_d025_s123_para_aligned,\n    #   exp_001_eval_3B_d100_s123_para_aligned_v2, exp_001_eval_3B_d000_v2_s123_para_aligned\n    # Excluded from IRT pool: d000_s42 and d005_s42 experiments (lr=2e-4 confound, D076)\n\n  - id: exp-002\n    name: stage1_signal_pipeline\n    claim: 2\n    description: >\n      Compute 4 detection signals on all contaminated + clean models from exp-001:\n      (a) embedding-based semantic retrieval (FAISS + sentence-transformers),\n      (b) Min-K%++ membership inference,\n      (c) ConStat performance gap (original vs paraphrased items),\n      (d) Self-Critique entropy collapse.\n      Output: per-model-item exposure scores for each signal.\n    priority: P0\n    gpu_budget_hours: 20\n    deps: [exp-001]\n    registry_id: exp_002_signals_05B\n    # Related: exp002-signals-1p5B (DONE/success), exp002-signal-d025-05B (DONE/success)\n    # Note: 3B signal runs (exp_002_signals_3B v1-v4) all failed/killed\n\n  - id: exp-003\n    name: rrf_aggregation_ablation\n    claim: 2\n    description: >\n      RRF fusion of 4 signals into composite per-item exposure score.\n      Ablations: (a) RRF vs equal-weight rank averaging, (b) single-signal only\n      (×4), (c) calibration-based weighted RRF variant, (d) false positive\n      injection robustness check (inject FP at rates matching Duan et al. 2024).\n      Also test degraded 2-signal mode (ConStat + Self-Critique) for closed-weight.\n    priority: P0\n    gpu_budget_hours: 2\n    deps: [exp-002]\n\n  - id: exp-004\n    name: simulation_identifiability_sweep\n    claim: 1\n    also_supports: [3]\n    description: >\n      Systematic synthetic-data sweep (NEW, not MVP — MVP only covered 4-5 conditions):\n      exposure signal AUC (0.55, 0.60, 0.65, 0.70, 0.80, 0.90) ×\n      model count (20, 50, 100, 200) ×\n      prior strength (N(0,0.5), N(0,1), N(0,2)) ×\n      exposure type (binary, continuous).\n      144 conditions, 10 seeds each. Reports: θ-γ recovery RMSE, posterior\n      correlation, coverage (50%/80%/95%), prior sensitivity. Establishes\n      minimum AUC threshold; if 95% CI width > 15pp at AUC=0.65, label as\n      \"cannot distinguish no contamination from moderate contamination.\"\n      N_items=300 fixed (per MVP finding).\n      Subsumes exp-010 (prior sensitivity) and exp-011 (few-examinee regime)\n      — prior × N_models dimensions already in sweep grid. Growing Pains\n      pre-estimation sub-experiment: at N_models=20/50, compare flat prior\n      vs informative prior from pre-estimated item parameters.\n      Also includes Fisher Information matrix analysis: derive approximate\n      analytical relationship between signal AUC, N_models, and γ\n      recoverability. Distinguish structural identifiability (parameters\n      uniquely determined) from practical identifiability (estimation\n      quality sufficient for decisions). Provides theoretical grounding\n      for the empirical AUC ≥ 0.70 threshold.\n    priority: P0\n    gpu_budget_hours: 0\n    deps: []\n    note: CPU only. MVP (mvp_sim_4pl_gamma) was preliminary; this is the full sweep.\n    registry_id: exp_004_sim_sweep\n    # Related: mvp_sim_4pl_gamma (DONE/success), mvp_sim_confounding (DONE/success)\n\n  - id: exp-005\n    name: noise_propagation_analysis\n    claim: 3\n    description: >\n      Two parts:\n      (A) Measurement error model (PRIMARY): extend Stan model to treat exposure\n      as noisy observation: exposure_ij ~ N(τ_ij, σ_e²), where τ is latent true\n      contamination. σ_e estimated from exp-001 ground truth FP/FN rates.\n      This propagates Stage 1 uncertainty into posteriors automatically.\n      Compare coverage (50%/80%/95%) vs point-estimate exposure baseline.\n      (B) Post-hoc noise injection: inject Gaussian noise at 1×/1.5×/2× matched\n      levels, re-fit standard model, measure CI widening for γ and θ.\n      Both parts inform whether measurement error model closes the coverage gap.\n    priority: P0\n    gpu_budget_hours: 0\n    deps: [exp-002, exp-004]\n    note: CPU only\n    registry_id: exp_005_noise_prop_v2\n    # Related: exp_005_noise_prop (v1, DONE/failed — sigma_e=0 bug)\n\n  - id: exp-006\n    name: irt_calibration_and_baselines\n    claim: 1\n    also_supports: [3]\n    description: >\n      Fit 4PL+γ IRT (Stan NUTS) on controlled models from exp-001/003.\n      PRIMARY: per-benchmark fitting with benchmark-specific γ_k — this is\n      the natural parameterization when IRT is fitted per-benchmark (each\n      benchmark's model has its own γ_k). ABLATION: joint fitting across\n      benchmarks with shared global γ (stronger assumption, tests whether\n      contamination effect is homogeneous across benchmarks). Report both.\n      Per-benchmark fitting (not joint) is the default to reduce local\n      independence violation scope. Posterior predictive checks on item-level residual\n      correlations to assess local independence empirically.\n      Compute calibrated scores via exposure=0 counterfactual with CIs.\n      Compare against 7 baselines:\n      (0) Raw — no adjustment (anchor),\n      (1) remove-and-rescore (drop flagged items),\n      (2) single-signal 2PL+γ (best signal only, simpler IRT),\n      (3) vanilla 4PL without γ (standard IRT, no contamination modeling),\n      (4) linear exposure regression + bootstrap CI (simplest post-hoc),\n      (5) Emperor's mitigation: rephrasing + option shuffling,\n      (6) DCR fuzzy inference (EMNLP 2025) — the only existing method\n          producing adjusted accuracy; must include or reviewers will reject.\n      Evaluate all 5 metrics: MAE, coverage (50%/80%/95%), sharpness,\n      Kendall τ, dose-response monotonicity.\n      Report mean ± std across 3 seeds (matched to exp-001 seeds).\n    priority: P0\n    gpu_budget_hours: 8\n    deps: [exp-003]\n    benchmarks: [MMLU, GSM8K, ARC-Challenge, HumanEval]\n    seeds: 3\n\n  # ============================================================\n  # P1: Important — run if time/GPU permit\n  # ============================================================\n\n  - id: exp-015\n    name: sft_d100_qc_only\n    claim: 1\n    description: >\n      100% dosage SFT using only QC-pass paraphrases (7547/16697 items).\n      Isolates noisy vs clean contamination confound identified by reviewer.\n      D012 decision. Compare calibration metrics against exp-001 d100 (all\n      paraphrases) to quantify effect of noisy contamination on IRT estimates.\n    priority: P1\n    gpu_budget_hours: 5\n    deps: [exp-001]\n    benchmarks: [MMLU, GSM8K, ARC-Challenge, HumanEval]\n    models: [Qwen2.5-0.5B]\n    seeds: 1\n    status: planned\n    registry_id: exp_001_sft_d100_qc_only\n    data_script: exp001/prepare_qc_only_data.py\n\n  - id: exp-007\n    name: scale_bridging_7b\n    claim: 1\n    description: >\n      Qwen2.5-7B controlled SFT injection at 5 dosage levels.\n      Validates calibration accuracy scales to larger models.\n      Requires multi-GPU node (7B LoRA SFT ~4-8h per run on 1×H100).\n    priority: P1\n    gpu_budget_hours: 30\n    deps: [exp-001]\n\n  - id: exp-008\n    name: signal_survival_analysis\n    claim: 2\n    description: >\n      Systematic evaluation of detection signal reliability across training regimes.\n      Signal × regime AUC heatmap: 4 signals × {base, SFT-clean, SFT-contaminated,\n      RL-post-trained}. Confirms Self-Critique compensates where Min-K%++/ConStat\n      degrade post-RL (per fragility paper arXiv 2510.02386).\n      ELEVATED to Core Contribution 2 per Dream review (all 3 tiers identified\n      this as the most genuinely novel finding).\n    priority: P0\n    gpu_budget_hours: 10\n    deps: [exp-002]\n\n  - id: exp-014\n    name: multi_family_validation\n    claim: 1\n    description: >\n      Controlled SFT injection on at least one non-Qwen model family\n      (Llama-3.2-1B or Pythia-1.4B) at 3 dosage levels (0%, 25%, 100%).\n      Validates that identifiability boundaries and calibration accuracy\n      generalize beyond Qwen2.5. Addresses Dream reviewer concern about\n      single model family limiting generalizability (flagged [M][W]).\n    priority: P1\n    gpu_budget_hours: 15\n    deps: [exp-001]\n\n  - id: exp-009\n    name: rl_observational_case_study\n    claim: 2\n    also_supports: [3]\n    description: >\n      Apply Self-Critique + available signals to existing RL-trained models:\n      Qwen2.5-Instruct (0.5B/1.5B/3B/7B), DeepSeek-R1-Distill-1.5B/7B.\n      Fit IRT with appropriately wider CIs. Expected regret quantification:\n      compare uncalibrated vs calibrated vs remove-rescore for top-5 model\n      selection. Framed as observational — directional external validity,\n      not full quantitative validation. Near-zero γ check on known-clean\n      benchmark (specificity test).\n    priority: P1\n    gpu_budget_hours: 15\n    deps: [exp-006, exp-008]\n\n  # exp-010 (prior_sensitivity) and exp-011 (few_examinee_regime) merged into exp-004.\n  # Prior × N_models dimensions already covered in the sweep grid.\n\n  # ============================================================\n  # P2: Bonus — adds breadth if resources allow\n  # ============================================================\n\n  - id: exp-012\n    name: observational_72b\n    claim: 1\n    description: >\n      Qwen2.5-72B observational analysis (inference only, no SFT).\n      Extends ecological validity to frontier model scale.\n    priority: P2\n    gpu_budget_hours: 15\n    deps: [exp-006]\n\n  - id: exp-013\n    name: closed_weight_2signal_mode\n    claim: 2\n    description: >\n      Degraded 2-signal mode (ConStat + Self-Critique, no logits/embeddings)\n      for closed-weight models. Ablation quantifying 2-signal vs 4-signal\n      calibration accuracy gap.\n    priority: P2\n    gpu_budget_hours: 5\n    deps: [exp-003]\n\n# ============================================================\n# GPU Budget Summary\n# ============================================================\ngpu_budget:\n  P0_hours: 90\n  P1_hours: 60\n  P2_hours: 20\n  buffer_hours: 30\n  total_hours: 200\n  note: >\n    CPU-only experiments (exp-004, exp-005, exp-011) excluded.\n    Buffer covers reruns, debugging, multi-seed overhead, and unexpected issues.\n    Requires 2-4× H100/A100-80G for parallel SFT runs.\n    EMNLP 2026 ARR May 25 sprint (12 days from May 13):\n    - With 4× H100: P0 in ~4 days, P1 in ~3 days, total ~8 days (fits deadline)\n    - With 2× H100: P0 in ~7 days, P1 in ~4 days, tight but feasible if parallelized\n    - Day-8 contingency: reduce benchmarks to MMLU + GSM8K if behind schedule\n\n# Multi-seed protocol:\n# - exp-001, exp-006: 3 seeds, report mean ± std for key metrics\n# - exp-004, exp-005, exp-011: 10 seeds (simulation, CPU)\n# - exp-007, exp-008, exp-009: 1 seed (resource-constrained, note as limitation if needed)\n",
    "structuredPatch": [
      {
        "oldStart": 90,
        "oldLines": 6,
        "newStart": 90,
        "newLines": 8,
        "lines": [
          "     priority: P0",
          "     gpu_budget_hours: 2",
          "     deps: [exp-002]",
          "+    registry_id: exp_003_rrf_05B",
          "+    # Related: exp_003_mmlu_item_aligned_gap (DONE/success)",
          " ",
          "   - id: exp-004",
          "     name: simulation_identifiability_sweep"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Assistant

_source line 121_

<details><summary>Logged reasoning block</summary>

```text
Good, 3 edits done. Now let me do the remaining ones:

4. exp-004: Add extreme_gamma to related (keep registry_id)
5. exp-005: Add v3, v4 to related (keep registry_id)
6. exp-006: Add registry_id
7. exp-008: Add registry_id
8. exp-015: Clear orphaned registry_id
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d61fa97d-0b3f-42cc-a383-d75fd89e4948",
  "uuid": "52fa85c3-b4cf-4b51-b1a7-0069a8694834",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UKH6PEcKW2jXD5D9ZNbohA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12013,
      "cache_read_input_tokens": 64899,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12013
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

_source line 122_

<details open><summary>🔧 Tool call — Edit · `toolu_01BcWVjCkoMiRkU92B7fQQUb`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/experiment_plan.yaml",
  "old_string": "    registry_id: exp_004_sim_sweep\n    # Related: mvp_sim_4pl_gamma (DONE/success), mvp_sim_confounding (DONE/success)",
  "new_string": "    registry_id: exp_004_sim_sweep\n    # Related: mvp_sim_4pl_gamma (DONE/success), mvp_sim_confounding (DONE/success),\n    #   exp_004_sim_sweep_extreme_gamma (DONE/success)\n    # Note: full sweep v1-v6 all failed (tmpfs/timeout issues); MVP + extreme_gamma succeeded"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d61fa97d-0b3f-42cc-a383-d75fd89e4948",
  "uuid": "5f13c07d-2e8a-4d2d-b47a-5683c1e75c5b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UKH6PEcKW2jXD5D9ZNbohA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12013,
      "cache_read_input_tokens": 64899,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12013
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

_source line 123 · 2026-05-15T20:14:40.143Z_

<details><summary>↩ Tool result · `toolu_01BcWVjCkoMiRkU92B7fQQUb`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/experiment_plan.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d61fa97d-0b3f-42cc-a383-d75fd89e4948",
  "uuid": "e0ae572f-2d2f-4932-9592-64315288b75b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/experiment_plan.yaml",
    "oldString": "    registry_id: exp_004_sim_sweep\n    # Related: mvp_sim_4pl_gamma (DONE/success), mvp_sim_confounding (DONE/success)",
    "newString": "    registry_id: exp_004_sim_sweep\n    # Related: mvp_sim_4pl_gamma (DONE/success), mvp_sim_confounding (DONE/success),\n    #   exp_004_sim_sweep_extreme_gamma (DONE/success)\n    # Note: full sweep v1-v6 all failed (tmpfs/timeout issues); MVP + extreme_gamma succeeded",
    "originalFile": "# ContamCal Experiment Plan\n# Each experiment maps to Core Claims in paper_framing.md\n# Priority: P0 = must-run, P1 = important, P2 = bonus\n\nexperiments:\n  # ============================================================\n  # P0: Core experiments — must complete for submission\n  # ============================================================\n\n  - id: exp-001\n    name: controlled_sft_injection\n    claim: 1\n    description: >\n      SFT contamination injection on Qwen2.5-0.5B/1.5B/3B at 5 dosage levels\n      (0%, 5%, 25%, 50%, 100% benchmark items as paraphrases in SFT data).\n      Produces ground-truth contaminated/clean model pairs. 15 SFT runs total\n      (3 models × 5 dosages), parallelized across GPUs. 3 seeds per condition\n      for key metrics (mean ± std).\n      Paraphrase generation: use strong open LLM (Qwen2.5-72B-Instruct or\n      equivalent) with controlled semantic similarity — following methodology\n      of \"Rethinking Benchmark and Contamination\" (arXiv 2023). Target:\n      high semantic similarity (cosine >0.85) but low lexical overlap\n      (BLEU <0.3) to evade n-gram decontamination while preserving\n      contamination effect. Quality validation: automated similarity metrics\n      + human spot-check on 50 random pairs per benchmark.\n    priority: P0\n    gpu_budget_hours: 50\n    deps: []\n    benchmarks: [MMLU, GSM8K, ARC-Challenge, HumanEval]\n    models: [Qwen2.5-0.5B, Qwen2.5-1.5B, Qwen2.5-3B]\n    seeds: 3\n    registry_id: exp_001_sft_injection\n    # Multi-run experiment; related successful registry entries:\n    # SFT training: exp_001_sft_0pct_05B, exp_001_sft_0pct_15B, exp_001_sft_0pct_3B,\n    #   exp_001_sft_0pct_05B_s123, exp_001_sft_0pct_15B_s123, exp_001_sft_0pct_3B_s123,\n    #   exp_001_sft_d005_05B_v3, exp_001_sft_d005_15B, exp_001_sft_d005_3B,\n    #   exp_001_sft_05B_d005_s123, exp_001_sft_15B_d005_s123_v2, exp_001_sft_3B_d005_s123,\n    #   exp_001_sft_d025_05B_v3, exp_001_sft_d025_15B, exp_001_sft_d025_3B_v2,\n    #   exp_001_sft_05B_d025_s123_v2, exp_001_sft_15B_d025_s123_v2, exp_001_sft_3B_d025_s123,\n    #   exp_001_sft_d100_05B, exp_001_sft_d100_15B_v2, exp_001_sft_d100_3B_v2,\n    #   exp_001_sft_05B_d100_s123, exp_001_sft_15B_d100_s123, exp_001_sft_3B_d100_s123,\n    #   exp_001_sft_3B_d000_v2, exp_001_sft_3B_d000_s123\n    # Eval (aligned): exp_001_eval_05B_d000_s123_aligned, exp_001_eval_05B_d005_aligned,\n    #   exp_001_eval_05B_d025_aligned, exp_001_eval_05B_d100_aligned_v4,\n    #   exp_001_eval_05B_d005_s123_aligned, exp_001_eval_05B_d025_s123_aligned,\n    #   exp_001_eval_05B_d100_s123_aligned, exp_001_eval_15B_aligned_batch,\n    #   exp_001_eval_15B_d005_aligned_v2, exp_001_eval_15B_d025_aligned,\n    #   exp_001_eval_15B_d100_aligned, exp_001_eval_15B_d000_s123_aligned,\n    #   exp_001_eval_15B_d100_s123_aligned, exp_001_eval_3B_d000_aligned,\n    #   exp_001_eval_3B_d005_aligned, exp_001_eval_3B_d100_aligned,\n    #   exp_001_eval_3B_d000_v2_aligned, exp_001_eval_3B_d025_v2_aligned,\n    #   exp_001_eval_3B_d100_v2_aligned_v2, exp_001_eval_3B_d000_s123_aligned,\n    #   exp_001_eval_3B_d005_s123_aligned, exp_001_eval_3B_d025_s123_aligned,\n    #   exp_001_eval_3B_d100_v2_s123_aligned, exp_001_eval_3B_d000_v2_s123_aligned\n    # Eval (para_aligned): exp_001_eval_05B_d005_para_aligned, exp_001_eval_05B_d025_aligned_v2,\n    #   exp_001_eval_05B_d005_s123_para_aligned, exp_001_eval_15B_d025_para_aligned,\n    #   exp_001_eval_3B_d000_s42_para_aligned, exp_001_eval_3B_d100_s42_para_aligned,\n    #   exp_001_eval_3B_d000_v2_para_aligned, exp_001_eval_3B_d000_v2_para_aligned_v2,\n    #   exp_001_eval_3B_d025_v2_para_aligned, exp_001_eval_3B_d100_v2_para_aligned,\n    #   exp_001_eval_3B_d005_s123_para_aligned, exp_001_eval_3B_d025_s123_para_aligned,\n    #   exp_001_eval_3B_d100_s123_para_aligned_v2, exp_001_eval_3B_d000_v2_s123_para_aligned\n    # Excluded from IRT pool: d000_s42 and d005_s42 experiments (lr=2e-4 confound, D076)\n\n  - id: exp-002\n    name: stage1_signal_pipeline\n    claim: 2\n    description: >\n      Compute 4 detection signals on all contaminated + clean models from exp-001:\n      (a) embedding-based semantic retrieval (FAISS + sentence-transformers),\n      (b) Min-K%++ membership inference,\n      (c) ConStat performance gap (original vs paraphrased items),\n      (d) Self-Critique entropy collapse.\n      Output: per-model-item exposure scores for each signal.\n    priority: P0\n    gpu_budget_hours: 20\n    deps: [exp-001]\n    registry_id: exp_002_signals_05B\n    # Related: exp002-signals-1p5B (DONE/success), exp002-signal-d025-05B (DONE/success)\n    # Note: 3B signal runs (exp_002_signals_3B v1-v4) all failed/killed\n\n  - id: exp-003\n    name: rrf_aggregation_ablation\n    claim: 2\n    description: >\n      RRF fusion of 4 signals into composite per-item exposure score.\n      Ablations: (a) RRF vs equal-weight rank averaging, (b) single-signal only\n      (×4), (c) calibration-based weighted RRF variant, (d) false positive\n      injection robustness check (inject FP at rates matching Duan et al. 2024).\n      Also test degraded 2-signal mode (ConStat + Self-Critique) for closed-weight.\n    priority: P0\n    gpu_budget_hours: 2\n    deps: [exp-002]\n    registry_id: exp_003_rrf_05B\n    # Related: exp_003_mmlu_item_aligned_gap (DONE/success)\n\n  - id: exp-004\n    name: simulation_identifiability_sweep\n    claim: 1\n    also_supports: [3]\n    description: >\n      Systematic synthetic-data sweep (NEW, not MVP — MVP only covered 4-5 conditions):\n      exposure signal AUC (0.55, 0.60, 0.65, 0.70, 0.80, 0.90) ×\n      model count (20, 50, 100, 200) ×\n      prior strength (N(0,0.5), N(0,1), N(0,2)) ×\n      exposure type (binary, continuous).\n      144 conditions, 10 seeds each. Reports: θ-γ recovery RMSE, posterior\n      correlation, coverage (50%/80%/95%), prior sensitivity. Establishes\n      minimum AUC threshold; if 95% CI width > 15pp at AUC=0.65, label as\n      \"cannot distinguish no contamination from moderate contamination.\"\n      N_items=300 fixed (per MVP finding).\n      Subsumes exp-010 (prior sensitivity) and exp-011 (few-examinee regime)\n      — prior × N_models dimensions already in sweep grid. Growing Pains\n      pre-estimation sub-experiment: at N_models=20/50, compare flat prior\n      vs informative prior from pre-estimated item parameters.\n      Also includes Fisher Information matrix analysis: derive approximate\n      analytical relationship between signal AUC, N_models, and γ\n      recoverability. Distinguish structural identifiability (parameters\n      uniquely determined) from practical identifiability (estimation\n      quality sufficient for decisions). Provides theoretical grounding\n      for the empirical AUC ≥ 0.70 threshold.\n    priority: P0\n    gpu_budget_hours: 0\n    deps: []\n    note: CPU only. MVP (mvp_sim_4pl_gamma) was preliminary; this is the full sweep.\n    registry_id: exp_004_sim_sweep\n    # Related: mvp_sim_4pl_gamma (DONE/success), mvp_sim_confounding (DONE/success)\n\n  - id: exp-005\n    name: noise_propagation_analysis\n    claim: 3\n    description: >\n      Two parts:\n      (A) Measurement error model (PRIMARY): extend Stan model to treat exposure\n      as noisy observation: exposure_ij ~ N(τ_ij, σ_e²), where τ is latent true\n      contamination. σ_e estimated from exp-001 ground truth FP/FN rates.\n      This propagates Stage 1 uncertainty into posteriors automatically.\n      Compare coverage (50%/80%/95%) vs point-estimate exposure baseline.\n      (B) Post-hoc noise injection: inject Gaussian noise at 1×/1.5×/2× matched\n      levels, re-fit standard model, measure CI widening for γ and θ.\n      Both parts inform whether measurement error model closes the coverage gap.\n    priority: P0\n    gpu_budget_hours: 0\n    deps: [exp-002, exp-004]\n    note: CPU only\n    registry_id: exp_005_noise_prop_v2\n    # Related: exp_005_noise_prop (v1, DONE/failed — sigma_e=0 bug)\n\n  - id: exp-006\n    name: irt_calibration_and_baselines\n    claim: 1\n    also_supports: [3]\n    description: >\n      Fit 4PL+γ IRT (Stan NUTS) on controlled models from exp-001/003.\n      PRIMARY: per-benchmark fitting with benchmark-specific γ_k — this is\n      the natural parameterization when IRT is fitted per-benchmark (each\n      benchmark's model has its own γ_k). ABLATION: joint fitting across\n      benchmarks with shared global γ (stronger assumption, tests whether\n      contamination effect is homogeneous across benchmarks). Report both.\n      Per-benchmark fitting (not joint) is the default to reduce local\n      independence violation scope. Posterior predictive checks on item-level residual\n      correlations to assess local independence empirically.\n      Compute calibrated scores via exposure=0 counterfactual with CIs.\n      Compare against 7 baselines:\n      (0) Raw — no adjustment (anchor),\n      (1) remove-and-rescore (drop flagged items),\n      (2) single-signal 2PL+γ (best signal only, simpler IRT),\n      (3) vanilla 4PL without γ (standard IRT, no contamination modeling),\n      (4) linear exposure regression + bootstrap CI (simplest post-hoc),\n      (5) Emperor's mitigation: rephrasing + option shuffling,\n      (6) DCR fuzzy inference (EMNLP 2025) — the only existing method\n          producing adjusted accuracy; must include or reviewers will reject.\n      Evaluate all 5 metrics: MAE, coverage (50%/80%/95%), sharpness,\n      Kendall τ, dose-response monotonicity.\n      Report mean ± std across 3 seeds (matched to exp-001 seeds).\n    priority: P0\n    gpu_budget_hours: 8\n    deps: [exp-003]\n    benchmarks: [MMLU, GSM8K, ARC-Challenge, HumanEval]\n    seeds: 3\n\n  # ============================================================\n  # P1: Important — run if time/GPU permit\n  # ============================================================\n\n  - id: exp-015\n    name: sft_d100_qc_only\n    claim: 1\n    description: >\n      100% dosage SFT using only QC-pass paraphrases (7547/16697 items).\n      Isolates noisy vs clean contamination confound identified by reviewer.\n      D012 decision. Compare calibration metrics against exp-001 d100 (all\n      paraphrases) to quantify effect of noisy contamination on IRT estimates.\n    priority: P1\n    gpu_budget_hours: 5\n    deps: [exp-001]\n    benchmarks: [MMLU, GSM8K, ARC-Challenge, HumanEval]\n    models: [Qwen2.5-0.5B]\n    seeds: 1\n    status: planned\n    registry_id: exp_001_sft_d100_qc_only\n    data_script: exp001/prepare_qc_only_data.py\n\n  - id: exp-007\n    name: scale_bridging_7b\n    claim: 1\n    description: >\n      Qwen2.5-7B controlled SFT injection at 5 dosage levels.\n      Validates calibration accuracy scales to larger models.\n      Requires multi-GPU node (7B LoRA SFT ~4-8h per run on 1×H100).\n    priority: P1\n    gpu_budget_hours: 30\n    deps: [exp-001]\n\n  - id: exp-008\n    name: signal_survival_analysis\n    claim: 2\n    description: >\n      Systematic evaluation of detection signal reliability across training regimes.\n      Signal × regime AUC heatmap: 4 signals × {base, SFT-clean, SFT-contaminated,\n      RL-post-trained}. Confirms Self-Critique compensates where Min-K%++/ConStat\n      degrade post-RL (per fragility paper arXiv 2510.02386).\n      ELEVATED to Core Contribution 2 per Dream review (all 3 tiers identified\n      this as the most genuinely novel finding).\n    priority: P0\n    gpu_budget_hours: 10\n    deps: [exp-002]\n\n  - id: exp-014\n    name: multi_family_validation\n    claim: 1\n    description: >\n      Controlled SFT injection on at least one non-Qwen model family\n      (Llama-3.2-1B or Pythia-1.4B) at 3 dosage levels (0%, 25%, 100%).\n      Validates that identifiability boundaries and calibration accuracy\n      generalize beyond Qwen2.5. Addresses Dream reviewer concern about\n      single model family limiting generalizability (flagged [M][W]).\n    priority: P1\n    gpu_budget_hours: 15\n    deps: [exp-001]\n\n  - id: exp-009\n    name: rl_observational_case_study\n    claim: 2\n    also_supports: [3]\n    description: >\n      Apply Self-Critique + available signals to existing RL-trained models:\n      Qwen2.5-Instruct (0.5B/1.5B/3B/7B), DeepSeek-R1-Distill-1.5B/7B.\n      Fit IRT with appropriately wider CIs. Expected regret quantification:\n      compare uncalibrated vs calibrated vs remove-rescore for top-5 model\n      selection. Framed as observational — directional external validity,\n      not full quantitative validation. Near-zero γ check on known-clean\n      benchmark (specificity test).\n    priority: P1\n    gpu_budget_hours: 15\n    deps: [exp-006, exp-008]\n\n  # exp-010 (prior_sensitivity) and exp-011 (few_examinee_regime) merged into exp-004.\n  # Prior × N_models dimensions already covered in the sweep grid.\n\n  # ============================================================\n  # P2: Bonus — adds breadth if resources allow\n  # ============================================================\n\n  - id: exp-012\n    name: observational_72b\n    claim: 1\n    description: >\n      Qwen2.5-72B observational analysis (inference only, no SFT).\n      Extends ecological validity to frontier model scale.\n    priority: P2\n    gpu_budget_hours: 15\n    deps: [exp-006]\n\n  - id: exp-013\n    name: closed_weight_2signal_mode\n    claim: 2\n    description: >\n      Degraded 2-signal mode (ConStat + Self-Critique, no logits/embeddings)\n      for closed-weight models. Ablation quantifying 2-signal vs 4-signal\n      calibration accuracy gap.\n    priority: P2\n    gpu_budget_hours: 5\n    deps: [exp-003]\n\n# ============================================================\n# GPU Budget Summary\n# ============================================================\ngpu_budget:\n  P0_hours: 90\n  P1_hours: 60\n  P2_hours: 20\n  buffer_hours: 30\n  total_hours: 200\n  note: >\n    CPU-only experiments (exp-004, exp-005, exp-011) excluded.\n    Buffer covers reruns, debugging, multi-seed overhead, and unexpected issues.\n    Requires 2-4× H100/A100-80G for parallel SFT runs.\n    EMNLP 2026 ARR May 25 sprint (12 days from May 13):\n    - With 4× H100: P0 in ~4 days, P1 in ~3 days, total ~8 days (fits deadline)\n    - With 2× H100: P0 in ~7 days, P1 in ~4 days, tight but feasible if parallelized\n    - Day-8 contingency: reduce benchmarks to MMLU + GSM8K if behind schedule\n\n# Multi-seed protocol:\n# - exp-001, exp-006: 3 seeds, report mean ± std for key metrics\n# - exp-004, exp-005, exp-011: 10 seeds (simulation, CPU)\n# - exp-007, exp-008, exp-009: 1 seed (resource-constrained, note as limitation if needed)\n",
    "structuredPatch": [
      {
        "oldStart": 123,
        "oldLines": 7,
        "newStart": 123,
        "newLines": 9,
        "lines": [
          "     deps: []",
          "     note: CPU only. MVP (mvp_sim_4pl_gamma) was preliminary; this is the full sweep.",
          "     registry_id: exp_004_sim_sweep",
          "-    # Related: mvp_sim_4pl_gamma (DONE/success), mvp_sim_confounding (DONE/success)",
          "+    # Related: mvp_sim_4pl_gamma (DONE/success), mvp_sim_confounding (DONE/success),",
          "+    #   exp_004_sim_sweep_extreme_gamma (DONE/success)",
          "+    # Note: full sweep v1-v6 all failed (tmpfs/timeout issues); MVP + extreme_gamma succeeded",
          " ",
          "   - id: exp-005",
          "     name: noise_propagation_analysis"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Tool call

_source line 124_

<details open><summary>🔧 Tool call — Edit · `toolu_01SmQkh8schxMyGrWi2GR72F`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/experiment_plan.yaml",
  "old_string": "    registry_id: exp_005_noise_prop_v2\n    # Related: exp_005_noise_prop (v1, DONE/failed — sigma_e=0 bug)",
  "new_string": "    registry_id: exp_005_noise_prop_v2\n    # Related: exp_005_noise_prop (v1, DONE/failed — sigma_e=0 bug),\n    #   exp_005_noise_prop_v3 (DONE/failed), exp_005_noise_prop_v4 (DONE/negative)\n    # Note: all versions failed or negative; v4 completed but results negative"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d61fa97d-0b3f-42cc-a383-d75fd89e4948",
  "uuid": "f6f7f2fc-b5ff-494e-b071-fc0f6dfca7a9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UKH6PEcKW2jXD5D9ZNbohA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12013,
      "cache_read_input_tokens": 64899,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12013
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

_source line 125 · 2026-05-15T20:14:42.900Z_

<details><summary>↩ Tool result · `toolu_01SmQkh8schxMyGrWi2GR72F`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/experiment_plan.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d61fa97d-0b3f-42cc-a383-d75fd89e4948",
  "uuid": "4f695ed6-9836-4adf-bb7f-fef3cc9a5364",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/experiment_plan.yaml",
    "oldString": "    registry_id: exp_005_noise_prop_v2\n    # Related: exp_005_noise_prop (v1, DONE/failed — sigma_e=0 bug)",
    "newString": "    registry_id: exp_005_noise_prop_v2\n    # Related: exp_005_noise_prop (v1, DONE/failed — sigma_e=0 bug),\n    #   exp_005_noise_prop_v3 (DONE/failed), exp_005_noise_prop_v4 (DONE/negative)\n    # Note: all versions failed or negative; v4 completed but results negative",
    "originalFile": "# ContamCal Experiment Plan\n# Each experiment maps to Core Claims in paper_framing.md\n# Priority: P0 = must-run, P1 = important, P2 = bonus\n\nexperiments:\n  # ============================================================\n  # P0: Core experiments — must complete for submission\n  # ============================================================\n\n  - id: exp-001\n    name: controlled_sft_injection\n    claim: 1\n    description: >\n      SFT contamination injection on Qwen2.5-0.5B/1.5B/3B at 5 dosage levels\n      (0%, 5%, 25%, 50%, 100% benchmark items as paraphrases in SFT data).\n      Produces ground-truth contaminated/clean model pairs. 15 SFT runs total\n      (3 models × 5 dosages), parallelized across GPUs. 3 seeds per condition\n      for key metrics (mean ± std).\n      Paraphrase generation: use strong open LLM (Qwen2.5-72B-Instruct or\n      equivalent) with controlled semantic similarity — following methodology\n      of \"Rethinking Benchmark and Contamination\" (arXiv 2023). Target:\n      high semantic similarity (cosine >0.85) but low lexical overlap\n      (BLEU <0.3) to evade n-gram decontamination while preserving\n      contamination effect. Quality validation: automated similarity metrics\n      + human spot-check on 50 random pairs per benchmark.\n    priority: P0\n    gpu_budget_hours: 50\n    deps: []\n    benchmarks: [MMLU, GSM8K, ARC-Challenge, HumanEval]\n    models: [Qwen2.5-0.5B, Qwen2.5-1.5B, Qwen2.5-3B]\n    seeds: 3\n    registry_id: exp_001_sft_injection\n    # Multi-run experiment; related successful registry entries:\n    # SFT training: exp_001_sft_0pct_05B, exp_001_sft_0pct_15B, exp_001_sft_0pct_3B,\n    #   exp_001_sft_0pct_05B_s123, exp_001_sft_0pct_15B_s123, exp_001_sft_0pct_3B_s123,\n    #   exp_001_sft_d005_05B_v3, exp_001_sft_d005_15B, exp_001_sft_d005_3B,\n    #   exp_001_sft_05B_d005_s123, exp_001_sft_15B_d005_s123_v2, exp_001_sft_3B_d005_s123,\n    #   exp_001_sft_d025_05B_v3, exp_001_sft_d025_15B, exp_001_sft_d025_3B_v2,\n    #   exp_001_sft_05B_d025_s123_v2, exp_001_sft_15B_d025_s123_v2, exp_001_sft_3B_d025_s123,\n    #   exp_001_sft_d100_05B, exp_001_sft_d100_15B_v2, exp_001_sft_d100_3B_v2,\n    #   exp_001_sft_05B_d100_s123, exp_001_sft_15B_d100_s123, exp_001_sft_3B_d100_s123,\n    #   exp_001_sft_3B_d000_v2, exp_001_sft_3B_d000_s123\n    # Eval (aligned): exp_001_eval_05B_d000_s123_aligned, exp_001_eval_05B_d005_aligned,\n    #   exp_001_eval_05B_d025_aligned, exp_001_eval_05B_d100_aligned_v4,\n    #   exp_001_eval_05B_d005_s123_aligned, exp_001_eval_05B_d025_s123_aligned,\n    #   exp_001_eval_05B_d100_s123_aligned, exp_001_eval_15B_aligned_batch,\n    #   exp_001_eval_15B_d005_aligned_v2, exp_001_eval_15B_d025_aligned,\n    #   exp_001_eval_15B_d100_aligned, exp_001_eval_15B_d000_s123_aligned,\n    #   exp_001_eval_15B_d100_s123_aligned, exp_001_eval_3B_d000_aligned,\n    #   exp_001_eval_3B_d005_aligned, exp_001_eval_3B_d100_aligned,\n    #   exp_001_eval_3B_d000_v2_aligned, exp_001_eval_3B_d025_v2_aligned,\n    #   exp_001_eval_3B_d100_v2_aligned_v2, exp_001_eval_3B_d000_s123_aligned,\n    #   exp_001_eval_3B_d005_s123_aligned, exp_001_eval_3B_d025_s123_aligned,\n    #   exp_001_eval_3B_d100_v2_s123_aligned, exp_001_eval_3B_d000_v2_s123_aligned\n    # Eval (para_aligned): exp_001_eval_05B_d005_para_aligned, exp_001_eval_05B_d025_aligned_v2,\n    #   exp_001_eval_05B_d005_s123_para_aligned, exp_001_eval_15B_d025_para_aligned,\n    #   exp_001_eval_3B_d000_s42_para_aligned, exp_001_eval_3B_d100_s42_para_aligned,\n    #   exp_001_eval_3B_d000_v2_para_aligned, exp_001_eval_3B_d000_v2_para_aligned_v2,\n    #   exp_001_eval_3B_d025_v2_para_aligned, exp_001_eval_3B_d100_v2_para_aligned,\n    #   exp_001_eval_3B_d005_s123_para_aligned, exp_001_eval_3B_d025_s123_para_aligned,\n    #   exp_001_eval_3B_d100_s123_para_aligned_v2, exp_001_eval_3B_d000_v2_s123_para_aligned\n    # Excluded from IRT pool: d000_s42 and d005_s42 experiments (lr=2e-4 confound, D076)\n\n  - id: exp-002\n    name: stage1_signal_pipeline\n    claim: 2\n    description: >\n      Compute 4 detection signals on all contaminated + clean models from exp-001:\n      (a) embedding-based semantic retrieval (FAISS + sentence-transformers),\n      (b) Min-K%++ membership inference,\n      (c) ConStat performance gap (original vs paraphrased items),\n      (d) Self-Critique entropy collapse.\n      Output: per-model-item exposure scores for each signal.\n    priority: P0\n    gpu_budget_hours: 20\n    deps: [exp-001]\n    registry_id: exp_002_signals_05B\n    # Related: exp002-signals-1p5B (DONE/success), exp002-signal-d025-05B (DONE/success)\n    # Note: 3B signal runs (exp_002_signals_3B v1-v4) all failed/killed\n\n  - id: exp-003\n    name: rrf_aggregation_ablation\n    claim: 2\n    description: >\n      RRF fusion of 4 signals into composite per-item exposure score.\n      Ablations: (a) RRF vs equal-weight rank averaging, (b) single-signal only\n      (×4), (c) calibration-based weighted RRF variant, (d) false positive\n      injection robustness check (inject FP at rates matching Duan et al. 2024).\n      Also test degraded 2-signal mode (ConStat + Self-Critique) for closed-weight.\n    priority: P0\n    gpu_budget_hours: 2\n    deps: [exp-002]\n    registry_id: exp_003_rrf_05B\n    # Related: exp_003_mmlu_item_aligned_gap (DONE/success)\n\n  - id: exp-004\n    name: simulation_identifiability_sweep\n    claim: 1\n    also_supports: [3]\n    description: >\n      Systematic synthetic-data sweep (NEW, not MVP — MVP only covered 4-5 conditions):\n      exposure signal AUC (0.55, 0.60, 0.65, 0.70, 0.80, 0.90) ×\n      model count (20, 50, 100, 200) ×\n      prior strength (N(0,0.5), N(0,1), N(0,2)) ×\n      exposure type (binary, continuous).\n      144 conditions, 10 seeds each. Reports: θ-γ recovery RMSE, posterior\n      correlation, coverage (50%/80%/95%), prior sensitivity. Establishes\n      minimum AUC threshold; if 95% CI width > 15pp at AUC=0.65, label as\n      \"cannot distinguish no contamination from moderate contamination.\"\n      N_items=300 fixed (per MVP finding).\n      Subsumes exp-010 (prior sensitivity) and exp-011 (few-examinee regime)\n      — prior × N_models dimensions already in sweep grid. Growing Pains\n      pre-estimation sub-experiment: at N_models=20/50, compare flat prior\n      vs informative prior from pre-estimated item parameters.\n      Also includes Fisher Information matrix analysis: derive approximate\n      analytical relationship between signal AUC, N_models, and γ\n      recoverability. Distinguish structural identifiability (parameters\n      uniquely determined) from practical identifiability (estimation\n      quality sufficient for decisions). Provides theoretical grounding\n      for the empirical AUC ≥ 0.70 threshold.\n    priority: P0\n    gpu_budget_hours: 0\n    deps: []\n    note: CPU only. MVP (mvp_sim_4pl_gamma) was preliminary; this is the full sweep.\n    registry_id: exp_004_sim_sweep\n    # Related: mvp_sim_4pl_gamma (DONE/success), mvp_sim_confounding (DONE/success),\n    #   exp_004_sim_sweep_extreme_gamma (DONE/success)\n    # Note: full sweep v1-v6 all failed (tmpfs/timeout issues); MVP + extreme_gamma succeeded\n\n  - id: exp-005\n    name: noise_propagation_analysis\n    claim: 3\n    description: >\n      Two parts:\n      (A) Measurement error model (PRIMARY): extend Stan model to treat exposure\n      as noisy observation: exposure_ij ~ N(τ_ij, σ_e²), where τ is latent true\n      contamination. σ_e estimated from exp-001 ground truth FP/FN rates.\n      This propagates Stage 1 uncertainty into posteriors automatically.\n      Compare coverage (50%/80%/95%) vs point-estimate exposure baseline.\n      (B) Post-hoc noise injection: inject Gaussian noise at 1×/1.5×/2× matched\n      levels, re-fit standard model, measure CI widening for γ and θ.\n      Both parts inform whether measurement error model closes the coverage gap.\n    priority: P0\n    gpu_budget_hours: 0\n    deps: [exp-002, exp-004]\n    note: CPU only\n    registry_id: exp_005_noise_prop_v2\n    # Related: exp_005_noise_prop (v1, DONE/failed — sigma_e=0 bug)\n\n  - id: exp-006\n    name: irt_calibration_and_baselines\n    claim: 1\n    also_supports: [3]\n    description: >\n      Fit 4PL+γ IRT (Stan NUTS) on controlled models from exp-001/003.\n      PRIMARY: per-benchmark fitting with benchmark-specific γ_k — this is\n      the natural parameterization when IRT is fitted per-benchmark (each\n      benchmark's model has its own γ_k). ABLATION: joint fitting across\n      benchmarks with shared global γ (stronger assumption, tests whether\n      contamination effect is homogeneous across benchmarks). Report both.\n      Per-benchmark fitting (not joint) is the default to reduce local\n      independence violation scope. Posterior predictive checks on item-level residual\n      correlations to assess local independence empirically.\n      Compute calibrated scores via exposure=0 counterfactual with CIs.\n      Compare against 7 baselines:\n      (0) Raw — no adjustment (anchor),\n      (1) remove-and-rescore (drop flagged items),\n      (2) single-signal 2PL+γ (best signal only, simpler IRT),\n      (3) vanilla 4PL without γ (standard IRT, no contamination modeling),\n      (4) linear exposure regression + bootstrap CI (simplest post-hoc),\n      (5) Emperor's mitigation: rephrasing + option shuffling,\n      (6) DCR fuzzy inference (EMNLP 2025) — the only existing method\n          producing adjusted accuracy; must include or reviewers will reject.\n      Evaluate all 5 metrics: MAE, coverage (50%/80%/95%), sharpness,\n      Kendall τ, dose-response monotonicity.\n      Report mean ± std across 3 seeds (matched to exp-001 seeds).\n    priority: P0\n    gpu_budget_hours: 8\n    deps: [exp-003]\n    benchmarks: [MMLU, GSM8K, ARC-Challenge, HumanEval]\n    seeds: 3\n\n  # ============================================================\n  # P1: Important — run if time/GPU permit\n  # ============================================================\n\n  - id: exp-015\n    name: sft_d100_qc_only\n    claim: 1\n    description: >\n      100% dosage SFT using only QC-pass paraphrases (7547/16697 items).\n      Isolates noisy vs clean contamination confound identified by reviewer.\n      D012 decision. Compare calibration metrics against exp-001 d100 (all\n      paraphrases) to quantify effect of noisy contamination on IRT estimates.\n    priority: P1\n    gpu_budget_hours: 5\n    deps: [exp-001]\n    benchmarks: [MMLU, GSM8K, ARC-Challenge, HumanEval]\n    models: [Qwen2.5-0.5B]\n    seeds: 1\n    status: planned\n    registry_id: exp_001_sft_d100_qc_only\n    data_script: exp001/prepare_qc_only_data.py\n\n  - id: exp-007\n    name: scale_bridging_7b\n    claim: 1\n    description: >\n      Qwen2.5-7B controlled SFT injection at 5 dosage levels.\n      Validates calibration accuracy scales to larger models.\n      Requires multi-GPU node (7B LoRA SFT ~4-8h per run on 1×H100).\n    priority: P1\n    gpu_budget_hours: 30\n    deps: [exp-001]\n\n  - id: exp-008\n    name: signal_survival_analysis\n    claim: 2\n    description: >\n      Systematic evaluation of detection signal reliability across training regimes.\n      Signal × regime AUC heatmap: 4 signals × {base, SFT-clean, SFT-contaminated,\n      RL-post-trained}. Confirms Self-Critique compensates where Min-K%++/ConStat\n      degrade post-RL (per fragility paper arXiv 2510.02386).\n      ELEVATED to Core Contribution 2 per Dream review (all 3 tiers identified\n      this as the most genuinely novel finding).\n    priority: P0\n    gpu_budget_hours: 10\n    deps: [exp-002]\n\n  - id: exp-014\n    name: multi_family_validation\n    claim: 1\n    description: >\n      Controlled SFT injection on at least one non-Qwen model family\n      (Llama-3.2-1B or Pythia-1.4B) at 3 dosage levels (0%, 25%, 100%).\n      Validates that identifiability boundaries and calibration accuracy\n      generalize beyond Qwen2.5. Addresses Dream reviewer concern about\n      single model family limiting generalizability (flagged [M][W]).\n    priority: P1\n    gpu_budget_hours: 15\n    deps: [exp-001]\n\n  - id: exp-009\n    name: rl_observational_case_study\n    claim: 2\n    also_supports: [3]\n    description: >\n      Apply Self-Critique + available signals to existing RL-trained models:\n      Qwen2.5-Instruct (0.5B/1.5B/3B/7B), DeepSeek-R1-Distill-1.5B/7B.\n      Fit IRT with appropriately wider CIs. Expected regret quantification:\n      compare uncalibrated vs calibrated vs remove-rescore for top-5 model\n      selection. Framed as observational — directional external validity,\n      not full quantitative validation. Near-zero γ check on known-clean\n      benchmark (specificity test).\n    priority: P1\n    gpu_budget_hours: 15\n    deps: [exp-006, exp-008]\n\n  # exp-010 (prior_sensitivity) and exp-011 (few_examinee_regime) merged into exp-004.\n  # Prior × N_models dimensions already covered in the sweep grid.\n\n  # ============================================================\n  # P2: Bonus — adds breadth if resources allow\n  # ============================================================\n\n  - id: exp-012\n    name: observational_72b\n    claim: 1\n    description: >\n      Qwen2.5-72B observational analysis (inference only, no SFT).\n      Extends ecological validity to frontier model scale.\n    priority: P2\n    gpu_budget_hours: 15\n    deps: [exp-006]\n\n  - id: exp-013\n    name: closed_weight_2signal_mode\n    claim: 2\n    description: >\n      Degraded 2-signal mode (ConStat + Self-Critique, no logits/embeddings)\n      for closed-weight models. Ablation quantifying 2-signal vs 4-signal\n      calibration accuracy gap.\n    priority: P2\n    gpu_budget_hours: 5\n    deps: [exp-003]\n\n# ============================================================\n# GPU Budget Summary\n# ============================================================\ngpu_budget:\n  P0_hours: 90\n  P1_hours: 60\n  P2_hours: 20\n  buffer_hours: 30\n  total_hours: 200\n  note: >\n    CPU-only experiments (exp-004, exp-005, exp-011) excluded.\n    Buffer covers reruns, debugging, multi-seed overhead, and unexpected issues.\n    Requires 2-4× H100/A100-80G for parallel SFT runs.\n    EMNLP 2026 ARR May 25 sprint (12 days from May 13):\n    - With 4× H100: P0 in ~4 days, P1 in ~3 days, total ~8 days (fits deadline)\n    - With 2× H100: P0 in ~7 days, P1 in ~4 days, tight but feasible if parallelized\n    - Day-8 contingency: reduce benchmarks to MMLU + GSM8K if behind schedule\n\n# Multi-seed protocol:\n# - exp-001, exp-006: 3 seeds, report mean ± std for key metrics\n# - exp-004, exp-005, exp-011: 10 seeds (simulation, CPU)\n# - exp-007, exp-008, exp-009: 1 seed (resource-constrained, note as limitation if needed)\n",
    "structuredPatch": [
      {
        "oldStart": 145,
        "oldLines": 7,
        "newStart": 145,
        "newLines": 9,
        "lines": [
          "     deps: [exp-002, exp-004]",
          "     note: CPU only",
          "     registry_id: exp_005_noise_prop_v2",
          "-    # Related: exp_005_noise_prop (v1, DONE/failed — sigma_e=0 bug)",
          "+    # Related: exp_005_noise_prop (v1, DONE/failed — sigma_e=0 bug),",
          "+    #   exp_005_noise_prop_v3 (DONE/failed), exp_005_noise_prop_v4 (DONE/negative)",
          "+    # Note: all versions failed or negative; v4 completed but results negative",
          " ",
          "   - id: exp-006",
          "     name: irt_calibration_and_baselines"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Tool call

_source line 126_

<details open><summary>🔧 Tool call — Edit · `toolu_01CD3EJJ1HQ5hya74nZeDZMx`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/experiment_plan.yaml",
  "old_string": "    seeds: 3\n\n  # ============================================================\n  # P1: Important — run if time/GPU permit\n  # ============================================================\n\n  - id: exp-015",
  "new_string": "    seeds: 3\n    registry_id: exp_006_irt_05B_gsm8k\n    # Related: exp_006_irt_05B_arc (DONE/success), exp006-s1only-gsm8k-2pl (DONE/success),\n    #   exp006-oracle-arc-2pl (DONE/success), exp006-oracle-gsm8k-extended-v2 (DONE/success),\n    #   exp006-pooled-s1only-gsm8k-v2 (DONE/success), exp006-pooled-s1only-arc (DONE/success),\n    #   exp006-pooled-05B-15B-arc-v2 (DONE/success)\n\n  # ============================================================\n  # P1: Important — run if time/GPU permit\n  # ============================================================\n\n  - id: exp-015"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d61fa97d-0b3f-42cc-a383-d75fd89e4948",
  "uuid": "102e4160-82a2-46e2-9651-f281b6dc690b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UKH6PEcKW2jXD5D9ZNbohA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12013,
      "cache_read_input_tokens": 64899,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12013
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

_source line 127 · 2026-05-15T20:14:50.910Z_

<details><summary>↩ Tool result · `toolu_01CD3EJJ1HQ5hya74nZeDZMx`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/experiment_plan.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d61fa97d-0b3f-42cc-a383-d75fd89e4948",
  "uuid": "c29b15e9-96dc-4dad-9f69-8d8af5420860",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/experiment_plan.yaml",
    "oldString": "    seeds: 3\n\n  # ============================================================\n  # P1: Important — run if time/GPU permit\n  # ============================================================\n\n  - id: exp-015",
    "newString": "    seeds: 3\n    registry_id: exp_006_irt_05B_gsm8k\n    # Related: exp_006_irt_05B_arc (DONE/success), exp006-s1only-gsm8k-2pl (DONE/success),\n    #   exp006-oracle-arc-2pl (DONE/success), exp006-oracle-gsm8k-extended-v2 (DONE/success),\n    #   exp006-pooled-s1only-gsm8k-v2 (DONE/success), exp006-pooled-s1only-arc (DONE/success),\n    #   exp006-pooled-05B-15B-arc-v2 (DONE/success)\n\n  # ============================================================\n  # P1: Important — run if time/GPU permit\n  # ============================================================\n\n  - id: exp-015",
    "originalFile": "# ContamCal Experiment Plan\n# Each experiment maps to Core Claims in paper_framing.md\n# Priority: P0 = must-run, P1 = important, P2 = bonus\n\nexperiments:\n  # ============================================================\n  # P0: Core experiments — must complete for submission\n  # ============================================================\n\n  - id: exp-001\n    name: controlled_sft_injection\n    claim: 1\n    description: >\n      SFT contamination injection on Qwen2.5-0.5B/1.5B/3B at 5 dosage levels\n      (0%, 5%, 25%, 50%, 100% benchmark items as paraphrases in SFT data).\n      Produces ground-truth contaminated/clean model pairs. 15 SFT runs total\n      (3 models × 5 dosages), parallelized across GPUs. 3 seeds per condition\n      for key metrics (mean ± std).\n      Paraphrase generation: use strong open LLM (Qwen2.5-72B-Instruct or\n      equivalent) with controlled semantic similarity — following methodology\n      of \"Rethinking Benchmark and Contamination\" (arXiv 2023). Target:\n      high semantic similarity (cosine >0.85) but low lexical overlap\n      (BLEU <0.3) to evade n-gram decontamination while preserving\n      contamination effect. Quality validation: automated similarity metrics\n      + human spot-check on 50 random pairs per benchmark.\n    priority: P0\n    gpu_budget_hours: 50\n    deps: []\n    benchmarks: [MMLU, GSM8K, ARC-Challenge, HumanEval]\n    models: [Qwen2.5-0.5B, Qwen2.5-1.5B, Qwen2.5-3B]\n    seeds: 3\n    registry_id: exp_001_sft_injection\n    # Multi-run experiment; related successful registry entries:\n    # SFT training: exp_001_sft_0pct_05B, exp_001_sft_0pct_15B, exp_001_sft_0pct_3B,\n    #   exp_001_sft_0pct_05B_s123, exp_001_sft_0pct_15B_s123, exp_001_sft_0pct_3B_s123,\n    #   exp_001_sft_d005_05B_v3, exp_001_sft_d005_15B, exp_001_sft_d005_3B,\n    #   exp_001_sft_05B_d005_s123, exp_001_sft_15B_d005_s123_v2, exp_001_sft_3B_d005_s123,\n    #   exp_001_sft_d025_05B_v3, exp_001_sft_d025_15B, exp_001_sft_d025_3B_v2,\n    #   exp_001_sft_05B_d025_s123_v2, exp_001_sft_15B_d025_s123_v2, exp_001_sft_3B_d025_s123,\n    #   exp_001_sft_d100_05B, exp_001_sft_d100_15B_v2, exp_001_sft_d100_3B_v2,\n    #   exp_001_sft_05B_d100_s123, exp_001_sft_15B_d100_s123, exp_001_sft_3B_d100_s123,\n    #   exp_001_sft_3B_d000_v2, exp_001_sft_3B_d000_s123\n    # Eval (aligned): exp_001_eval_05B_d000_s123_aligned, exp_001_eval_05B_d005_aligned,\n    #   exp_001_eval_05B_d025_aligned, exp_001_eval_05B_d100_aligned_v4,\n    #   exp_001_eval_05B_d005_s123_aligned, exp_001_eval_05B_d025_s123_aligned,\n    #   exp_001_eval_05B_d100_s123_aligned, exp_001_eval_15B_aligned_batch,\n    #   exp_001_eval_15B_d005_aligned_v2, exp_001_eval_15B_d025_aligned,\n    #   exp_001_eval_15B_d100_aligned, exp_001_eval_15B_d000_s123_aligned,\n    #   exp_001_eval_15B_d100_s123_aligned, exp_001_eval_3B_d000_aligned,\n    #   exp_001_eval_3B_d005_aligned, exp_001_eval_3B_d100_aligned,\n    #   exp_001_eval_3B_d000_v2_aligned, exp_001_eval_3B_d025_v2_aligned,\n    #   exp_001_eval_3B_d100_v2_aligned_v2, exp_001_eval_3B_d000_s123_aligned,\n    #   exp_001_eval_3B_d005_s123_aligned, exp_001_eval_3B_d025_s123_aligned,\n    #   exp_001_eval_3B_d100_v2_s123_aligned, exp_001_eval_3B_d000_v2_s123_aligned\n    # Eval (para_aligned): exp_001_eval_05B_d005_para_aligned, exp_001_eval_05B_d025_aligned_v2,\n    #   exp_001_eval_05B_d005_s123_para_aligned, exp_001_eval_15B_d025_para_aligned,\n    #   exp_001_eval_3B_d000_s42_para_aligned, exp_001_eval_3B_d100_s42_para_aligned,\n    #   exp_001_eval_3B_d000_v2_para_aligned, exp_001_eval_3B_d000_v2_para_aligned_v2,\n    #   exp_001_eval_3B_d025_v2_para_aligned, exp_001_eval_3B_d100_v2_para_aligned,\n    #   exp_001_eval_3B_d005_s123_para_aligned, exp_001_eval_3B_d025_s123_para_aligned,\n    #   exp_001_eval_3B_d100_s123_para_aligned_v2, exp_001_eval_3B_d000_v2_s123_para_aligned\n    # Excluded from IRT pool: d000_s42 and d005_s42 experiments (lr=2e-4 confound, D076)\n\n  - id: exp-002\n    name: stage1_signal_pipeline\n    claim: 2\n    description: >\n      Compute 4 detection signals on all contaminated + clean models from exp-001:\n      (a) embedding-based semantic retrieval (FAISS + sentence-transformers),\n      (b) Min-K%++ membership inference,\n      (c) ConStat performance gap (original vs paraphrased items),\n      (d) Self-Critique entropy collapse.\n      Output: per-model-item exposure scores for each signal.\n    priority: P0\n    gpu_budget_hours: 20\n    deps: [exp-001]\n    registry_id: exp_002_signals_05B\n    # Related: exp002-signals-1p5B (DONE/success), exp002-signal-d025-05B (DONE/success)\n    # Note: 3B signal runs (exp_002_signals_3B v1-v4) all failed/killed\n\n  - id: exp-003\n    name: rrf_aggregation_ablation\n    claim: 2\n    description: >\n      RRF fusion of 4 signals into composite per-item exposure score.\n      Ablations: (a) RRF vs equal-weight rank averaging, (b) single-signal only\n      (×4), (c) calibration-based weighted RRF variant, (d) false positive\n      injection robustness check (inject FP at rates matching Duan et al. 2024).\n      Also test degraded 2-signal mode (ConStat + Self-Critique) for closed-weight.\n    priority: P0\n    gpu_budget_hours: 2\n    deps: [exp-002]\n    registry_id: exp_003_rrf_05B\n    # Related: exp_003_mmlu_item_aligned_gap (DONE/success)\n\n  - id: exp-004\n    name: simulation_identifiability_sweep\n    claim: 1\n    also_supports: [3]\n    description: >\n      Systematic synthetic-data sweep (NEW, not MVP — MVP only covered 4-5 conditions):\n      exposure signal AUC (0.55, 0.60, 0.65, 0.70, 0.80, 0.90) ×\n      model count (20, 50, 100, 200) ×\n      prior strength (N(0,0.5), N(0,1), N(0,2)) ×\n      exposure type (binary, continuous).\n      144 conditions, 10 seeds each. Reports: θ-γ recovery RMSE, posterior\n      correlation, coverage (50%/80%/95%), prior sensitivity. Establishes\n      minimum AUC threshold; if 95% CI width > 15pp at AUC=0.65, label as\n      \"cannot distinguish no contamination from moderate contamination.\"\n      N_items=300 fixed (per MVP finding).\n      Subsumes exp-010 (prior sensitivity) and exp-011 (few-examinee regime)\n      — prior × N_models dimensions already in sweep grid. Growing Pains\n      pre-estimation sub-experiment: at N_models=20/50, compare flat prior\n      vs informative prior from pre-estimated item parameters.\n      Also includes Fisher Information matrix analysis: derive approximate\n      analytical relationship between signal AUC, N_models, and γ\n      recoverability. Distinguish structural identifiability (parameters\n      uniquely determined) from practical identifiability (estimation\n      quality sufficient for decisions). Provides theoretical grounding\n      for the empirical AUC ≥ 0.70 threshold.\n    priority: P0\n    gpu_budget_hours: 0\n    deps: []\n    note: CPU only. MVP (mvp_sim_4pl_gamma) was preliminary; this is the full sweep.\n    registry_id: exp_004_sim_sweep\n    # Related: mvp_sim_4pl_gamma (DONE/success), mvp_sim_confounding (DONE/success),\n    #   exp_004_sim_sweep_extreme_gamma (DONE/success)\n    # Note: full sweep v1-v6 all failed (tmpfs/timeout issues); MVP + extreme_gamma succeeded\n\n  - id: exp-005\n    name: noise_propagation_analysis\n    claim: 3\n    description: >\n      Two parts:\n      (A) Measurement error model (PRIMARY): extend Stan model to treat exposure\n      as noisy observation: exposure_ij ~ N(τ_ij, σ_e²), where τ is latent true\n      contamination. σ_e estimated from exp-001 ground truth FP/FN rates.\n      This propagates Stage 1 uncertainty into posteriors automatically.\n      Compare coverage (50%/80%/95%) vs point-estimate exposure baseline.\n      (B) Post-hoc noise injection: inject Gaussian noise at 1×/1.5×/2× matched\n      levels, re-fit standard model, measure CI widening for γ and θ.\n      Both parts inform whether measurement error model closes the coverage gap.\n    priority: P0\n    gpu_budget_hours: 0\n    deps: [exp-002, exp-004]\n    note: CPU only\n    registry_id: exp_005_noise_prop_v2\n    # Related: exp_005_noise_prop (v1, DONE/failed — sigma_e=0 bug),\n    #   exp_005_noise_prop_v3 (DONE/failed), exp_005_noise_prop_v4 (DONE/negative)\n    # Note: all versions failed or negative; v4 completed but results negative\n\n  - id: exp-006\n    name: irt_calibration_and_baselines\n    claim: 1\n    also_supports: [3]\n    description: >\n      Fit 4PL+γ IRT (Stan NUTS) on controlled models from exp-001/003.\n      PRIMARY: per-benchmark fitting with benchmark-specific γ_k — this is\n      the natural parameterization when IRT is fitted per-benchmark (each\n      benchmark's model has its own γ_k). ABLATION: joint fitting across\n      benchmarks with shared global γ (stronger assumption, tests whether\n      contamination effect is homogeneous across benchmarks). Report both.\n      Per-benchmark fitting (not joint) is the default to reduce local\n      independence violation scope. Posterior predictive checks on item-level residual\n      correlations to assess local independence empirically.\n      Compute calibrated scores via exposure=0 counterfactual with CIs.\n      Compare against 7 baselines:\n      (0) Raw — no adjustment (anchor),\n      (1) remove-and-rescore (drop flagged items),\n      (2) single-signal 2PL+γ (best signal only, simpler IRT),\n      (3) vanilla 4PL without γ (standard IRT, no contamination modeling),\n      (4) linear exposure regression + bootstrap CI (simplest post-hoc),\n      (5) Emperor's mitigation: rephrasing + option shuffling,\n      (6) DCR fuzzy inference (EMNLP 2025) — the only existing method\n          producing adjusted accuracy; must include or reviewers will reject.\n      Evaluate all 5 metrics: MAE, coverage (50%/80%/95%), sharpness,\n      Kendall τ, dose-response monotonicity.\n      Report mean ± std across 3 seeds (matched to exp-001 seeds).\n    priority: P0\n    gpu_budget_hours: 8\n    deps: [exp-003]\n    benchmarks: [MMLU, GSM8K, ARC-Challenge, HumanEval]\n    seeds: 3\n\n  # ============================================================\n  # P1: Important — run if time/GPU permit\n  # ============================================================\n\n  - id: exp-015\n    name: sft_d100_qc_only\n    claim: 1\n    description: >\n      100% dosage SFT using only QC-pass paraphrases (7547/16697 items).\n      Isolates noisy vs clean contamination confound identified by reviewer.\n      D012 decision. Compare calibration metrics against exp-001 d100 (all\n      paraphrases) to quantify effect of noisy contamination on IRT estimates.\n    priority: P1\n    gpu_budget_hours: 5\n    deps: [exp-001]\n    benchmarks: [MMLU, GSM8K, ARC-Challenge, HumanEval]\n    models: [Qwen2.5-0.5B]\n    seeds: 1\n    status: planned\n    registry_id: exp_001_sft_d100_qc_only\n    data_script: exp001/prepare_qc_only_data.py\n\n  - id: exp-007\n    name: scale_bridging_7b\n    claim: 1\n    description: >\n      Qwen2.5-7B controlled SFT injection at 5 dosage levels.\n      Validates calibration accuracy scales to larger models.\n      Requires multi-GPU node (7B LoRA SFT ~4-8h per run on 1×H100).\n    priority: P1\n    gpu_budget_hours: 30\n    deps: [exp-001]\n\n  - id: exp-008\n    name: signal_survival_analysis\n    claim: 2\n    description: >\n      Systematic evaluation of detection signal reliability across training regimes.\n      Signal × regime AUC heatmap: 4 signals × {base, SFT-clean, SFT-contaminated,\n      RL-post-trained}. Confirms Self-Critique compensates where Min-K%++/ConStat\n      degrade post-RL (per fragility paper arXiv 2510.02386).\n      ELEVATED to Core Contribution 2 per Dream review (all 3 tiers identified\n      this as the most genuinely novel finding).\n    priority: P0\n    gpu_budget_hours: 10\n    deps: [exp-002]\n\n  - id: exp-014\n    name: multi_family_validation\n    claim: 1\n    description: >\n      Controlled SFT injection on at least one non-Qwen model family\n      (Llama-3.2-1B or Pythia-1.4B) at 3 dosage levels (0%, 25%, 100%).\n      Validates that identifiability boundaries and calibration accuracy\n      generalize beyond Qwen2.5. Addresses Dream reviewer concern about\n      single model family limiting generalizability (flagged [M][W]).\n    priority: P1\n    gpu_budget_hours: 15\n    deps: [exp-001]\n\n  - id: exp-009\n    name: rl_observational_case_study\n    claim: 2\n    also_supports: [3]\n    description: >\n      Apply Self-Critique + available signals to existing RL-trained models:\n      Qwen2.5-Instruct (0.5B/1.5B/3B/7B), DeepSeek-R1-Distill-1.5B/7B.\n      Fit IRT with appropriately wider CIs. Expected regret quantification:\n      compare uncalibrated vs calibrated vs remove-rescore for top-5 model\n      selection. Framed as observational — directional external validity,\n      not full quantitative validation. Near-zero γ check on known-clean\n      benchmark (specificity test).\n    priority: P1\n    gpu_budget_hours: 15\n    deps: [exp-006, exp-008]\n\n  # exp-010 (prior_sensitivity) and exp-011 (few_examinee_regime) merged into exp-004.\n  # Prior × N_models dimensions already covered in the sweep grid.\n\n  # ============================================================\n  # P2: Bonus — adds breadth if resources allow\n  # ============================================================\n\n  - id: exp-012\n    name: observational_72b\n    claim: 1\n    description: >\n      Qwen2.5-72B observational analysis (inference only, no SFT).\n      Extends ecological validity to frontier model scale.\n    priority: P2\n    gpu_budget_hours: 15\n    deps: [exp-006]\n\n  - id: exp-013\n    name: closed_weight_2signal_mode\n    claim: 2\n    description: >\n      Degraded 2-signal mode (ConStat + Self-Critique, no logits/embeddings)\n      for closed-weight models. Ablation quantifying 2-signal vs 4-signal\n      calibration accuracy gap.\n    priority: P2\n    gpu_budget_hours: 5\n    deps: [exp-003]\n\n# ============================================================\n# GPU Budget Summary\n# ============================================================\ngpu_budget:\n  P0_hours: 90\n  P1_hours: 60\n  P2_hours: 20\n  buffer_hours: 30\n  total_hours: 200\n  note: >\n    CPU-only experiments (exp-004, exp-005, exp-011) excluded.\n    Buffer covers reruns, debugging, multi-seed overhead, and unexpected issues.\n    Requires 2-4× H100/A100-80G for parallel SFT runs.\n    EMNLP 2026 ARR May 25 sprint (12 days from May 13):\n    - With 4× H100: P0 in ~4 days, P1 in ~3 days, total ~8 days (fits deadline)\n    - With 2× H100: P0 in ~7 days, P1 in ~4 days, tight but feasible if parallelized\n    - Day-8 contingency: reduce benchmarks to MMLU + GSM8K if behind schedule\n\n# Multi-seed protocol:\n# - exp-001, exp-006: 3 seeds, report mean ± std for key metrics\n# - exp-004, exp-005, exp-011: 10 seeds (simulation, CPU)\n# - exp-007, exp-008, exp-009: 1 seed (resource-constrained, note as limitation if needed)\n",
    "structuredPatch": [
      {
        "oldStart": 181,
        "oldLines": 6,
        "newStart": 181,
        "newLines": 11,
        "lines": [
          "     deps: [exp-003]",
          "     benchmarks: [MMLU, GSM8K, ARC-Challenge, HumanEval]",
          "     seeds: 3",
          "+    registry_id: exp_006_irt_05B_gsm8k",
          "+    # Related: exp_006_irt_05B_arc (DONE/success), exp006-s1only-gsm8k-2pl (DONE/success),",
          "+    #   exp006-oracle-arc-2pl (DONE/success), exp006-oracle-gsm8k-extended-v2 (DONE/success),",
          "+    #   exp006-pooled-s1only-gsm8k-v2 (DONE/success), exp006-pooled-s1only-arc (DONE/success),",
          "+    #   exp006-pooled-05B-15B-arc-v2 (DONE/success)",
          " ",
          "   # ============================================================",
          "   # P1: Important — run if time/GPU permit"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Tool call

_source line 128_

<details open><summary>🔧 Tool call — Edit · `toolu_01K71KAxYjH8URRpcy7Jx3we`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/experiment_plan.yaml",
  "old_string": "    registry_id: exp_001_sft_d100_qc_only\n    data_script: exp001/prepare_qc_only_data.py",
  "new_string": "    registry_id: null\n    data_script: exp001/prepare_qc_only_data.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d61fa97d-0b3f-42cc-a383-d75fd89e4948",
  "uuid": "f13258aa-277a-4c56-b1f0-f095f11a3e89",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UKH6PEcKW2jXD5D9ZNbohA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12013,
      "cache_read_input_tokens": 64899,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12013
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

_source line 129 · 2026-05-15T20:14:51.512Z_

<details><summary>↩ Tool result · `toolu_01K71KAxYjH8URRpcy7Jx3we`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/experiment_plan.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d61fa97d-0b3f-42cc-a383-d75fd89e4948",
  "uuid": "0a55171b-722a-402d-9690-5f19d6f94687",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/experiment_plan.yaml",
    "oldString": "    registry_id: exp_001_sft_d100_qc_only\n    data_script: exp001/prepare_qc_only_data.py",
    "newString": "    registry_id: null\n    data_script: exp001/prepare_qc_only_data.py",
    "originalFile": "# ContamCal Experiment Plan\n# Each experiment maps to Core Claims in paper_framing.md\n# Priority: P0 = must-run, P1 = important, P2 = bonus\n\nexperiments:\n  # ============================================================\n  # P0: Core experiments — must complete for submission\n  # ============================================================\n\n  - id: exp-001\n    name: controlled_sft_injection\n    claim: 1\n    description: >\n      SFT contamination injection on Qwen2.5-0.5B/1.5B/3B at 5 dosage levels\n      (0%, 5%, 25%, 50%, 100% benchmark items as paraphrases in SFT data).\n      Produces ground-truth contaminated/clean model pairs. 15 SFT runs total\n      (3 models × 5 dosages), parallelized across GPUs. 3 seeds per condition\n      for key metrics (mean ± std).\n      Paraphrase generation: use strong open LLM (Qwen2.5-72B-Instruct or\n      equivalent) with controlled semantic similarity — following methodology\n      of \"Rethinking Benchmark and Contamination\" (arXiv 2023). Target:\n      high semantic similarity (cosine >0.85) but low lexical overlap\n      (BLEU <0.3) to evade n-gram decontamination while preserving\n      contamination effect. Quality validation: automated similarity metrics\n      + human spot-check on 50 random pairs per benchmark.\n    priority: P0\n    gpu_budget_hours: 50\n    deps: []\n    benchmarks: [MMLU, GSM8K, ARC-Challenge, HumanEval]\n    models: [Qwen2.5-0.5B, Qwen2.5-1.5B, Qwen2.5-3B]\n    seeds: 3\n    registry_id: exp_001_sft_injection\n    # Multi-run experiment; related successful registry entries:\n    # SFT training: exp_001_sft_0pct_05B, exp_001_sft_0pct_15B, exp_001_sft_0pct_3B,\n    #   exp_001_sft_0pct_05B_s123, exp_001_sft_0pct_15B_s123, exp_001_sft_0pct_3B_s123,\n    #   exp_001_sft_d005_05B_v3, exp_001_sft_d005_15B, exp_001_sft_d005_3B,\n    #   exp_001_sft_05B_d005_s123, exp_001_sft_15B_d005_s123_v2, exp_001_sft_3B_d005_s123,\n    #   exp_001_sft_d025_05B_v3, exp_001_sft_d025_15B, exp_001_sft_d025_3B_v2,\n    #   exp_001_sft_05B_d025_s123_v2, exp_001_sft_15B_d025_s123_v2, exp_001_sft_3B_d025_s123,\n    #   exp_001_sft_d100_05B, exp_001_sft_d100_15B_v2, exp_001_sft_d100_3B_v2,\n    #   exp_001_sft_05B_d100_s123, exp_001_sft_15B_d100_s123, exp_001_sft_3B_d100_s123,\n    #   exp_001_sft_3B_d000_v2, exp_001_sft_3B_d000_s123\n    # Eval (aligned): exp_001_eval_05B_d000_s123_aligned, exp_001_eval_05B_d005_aligned,\n    #   exp_001_eval_05B_d025_aligned, exp_001_eval_05B_d100_aligned_v4,\n    #   exp_001_eval_05B_d005_s123_aligned, exp_001_eval_05B_d025_s123_aligned,\n    #   exp_001_eval_05B_d100_s123_aligned, exp_001_eval_15B_aligned_batch,\n    #   exp_001_eval_15B_d005_aligned_v2, exp_001_eval_15B_d025_aligned,\n    #   exp_001_eval_15B_d100_aligned, exp_001_eval_15B_d000_s123_aligned,\n    #   exp_001_eval_15B_d100_s123_aligned, exp_001_eval_3B_d000_aligned,\n    #   exp_001_eval_3B_d005_aligned, exp_001_eval_3B_d100_aligned,\n    #   exp_001_eval_3B_d000_v2_aligned, exp_001_eval_3B_d025_v2_aligned,\n    #   exp_001_eval_3B_d100_v2_aligned_v2, exp_001_eval_3B_d000_s123_aligned,\n    #   exp_001_eval_3B_d005_s123_aligned, exp_001_eval_3B_d025_s123_aligned,\n    #   exp_001_eval_3B_d100_v2_s123_aligned, exp_001_eval_3B_d000_v2_s123_aligned\n    # Eval (para_aligned): exp_001_eval_05B_d005_para_aligned, exp_001_eval_05B_d025_aligned_v2,\n    #   exp_001_eval_05B_d005_s123_para_aligned, exp_001_eval_15B_d025_para_aligned,\n    #   exp_001_eval_3B_d000_s42_para_aligned, exp_001_eval_3B_d100_s42_para_aligned,\n    #   exp_001_eval_3B_d000_v2_para_aligned, exp_001_eval_3B_d000_v2_para_aligned_v2,\n    #   exp_001_eval_3B_d025_v2_para_aligned, exp_001_eval_3B_d100_v2_para_aligned,\n    #   exp_001_eval_3B_d005_s123_para_aligned, exp_001_eval_3B_d025_s123_para_aligned,\n    #   exp_001_eval_3B_d100_s123_para_aligned_v2, exp_001_eval_3B_d000_v2_s123_para_aligned\n    # Excluded from IRT pool: d000_s42 and d005_s42 experiments (lr=2e-4 confound, D076)\n\n  - id: exp-002\n    name: stage1_signal_pipeline\n    claim: 2\n    description: >\n      Compute 4 detection signals on all contaminated + clean models from exp-001:\n      (a) embedding-based semantic retrieval (FAISS + sentence-transformers),\n      (b) Min-K%++ membership inference,\n      (c) ConStat performance gap (original vs paraphrased items),\n      (d) Self-Critique entropy collapse.\n      Output: per-model-item exposure scores for each signal.\n    priority: P0\n    gpu_budget_hours: 20\n    deps: [exp-001]\n    registry_id: exp_002_signals_05B\n    # Related: exp002-signals-1p5B (DONE/success), exp002-signal-d025-05B (DONE/success)\n    # Note: 3B signal runs (exp_002_signals_3B v1-v4) all failed/killed\n\n  - id: exp-003\n    name: rrf_aggregation_ablation\n    claim: 2\n    description: >\n      RRF fusion of 4 signals into composite per-item exposure score.\n      Ablations: (a) RRF vs equal-weight rank averaging, (b) single-signal only\n      (×4), (c) calibration-based weighted RRF variant, (d) false positive\n      injection robustness check (inject FP at rates matching Duan et al. 2024).\n      Also test degraded 2-signal mode (ConStat + Self-Critique) for closed-weight.\n    priority: P0\n    gpu_budget_hours: 2\n    deps: [exp-002]\n    registry_id: exp_003_rrf_05B\n    # Related: exp_003_mmlu_item_aligned_gap (DONE/success)\n\n  - id: exp-004\n    name: simulation_identifiability_sweep\n    claim: 1\n    also_supports: [3]\n    description: >\n      Systematic synthetic-data sweep (NEW, not MVP — MVP only covered 4-5 conditions):\n      exposure signal AUC (0.55, 0.60, 0.65, 0.70, 0.80, 0.90) ×\n      model count (20, 50, 100, 200) ×\n      prior strength (N(0,0.5), N(0,1), N(0,2)) ×\n      exposure type (binary, continuous).\n      144 conditions, 10 seeds each. Reports: θ-γ recovery RMSE, posterior\n      correlation, coverage (50%/80%/95%), prior sensitivity. Establishes\n      minimum AUC threshold; if 95% CI width > 15pp at AUC=0.65, label as\n      \"cannot distinguish no contamination from moderate contamination.\"\n      N_items=300 fixed (per MVP finding).\n      Subsumes exp-010 (prior sensitivity) and exp-011 (few-examinee regime)\n      — prior × N_models dimensions already in sweep grid. Growing Pains\n      pre-estimation sub-experiment: at N_models=20/50, compare flat prior\n      vs informative prior from pre-estimated item parameters.\n      Also includes Fisher Information matrix analysis: derive approximate\n      analytical relationship between signal AUC, N_models, and γ\n      recoverability. Distinguish structural identifiability (parameters\n      uniquely determined) from practical identifiability (estimation\n      quality sufficient for decisions). Provides theoretical grounding\n      for the empirical AUC ≥ 0.70 threshold.\n    priority: P0\n    gpu_budget_hours: 0\n    deps: []\n    note: CPU only. MVP (mvp_sim_4pl_gamma) was preliminary; this is the full sweep.\n    registry_id: exp_004_sim_sweep\n    # Related: mvp_sim_4pl_gamma (DONE/success), mvp_sim_confounding (DONE/success),\n    #   exp_004_sim_sweep_extreme_gamma (DONE/success)\n    # Note: full sweep v1-v6 all failed (tmpfs/timeout issues); MVP + extreme_gamma succeeded\n\n  - id: exp-005\n    name: noise_propagation_analysis\n    claim: 3\n    description: >\n      Two parts:\n      (A) Measurement error model (PRIMARY): extend Stan model to treat exposure\n      as noisy observation: exposure_ij ~ N(τ_ij, σ_e²), where τ is latent true\n      contamination. σ_e estimated from exp-001 ground truth FP/FN rates.\n      This propagates Stage 1 uncertainty into posteriors automatically.\n      Compare coverage (50%/80%/95%) vs point-estimate exposure baseline.\n      (B) Post-hoc noise injection: inject Gaussian noise at 1×/1.5×/2× matched\n      levels, re-fit standard model, measure CI widening for γ and θ.\n      Both parts inform whether measurement error model closes the coverage gap.\n    priority: P0\n    gpu_budget_hours: 0\n    deps: [exp-002, exp-004]\n    note: CPU only\n    registry_id: exp_005_noise_prop_v2\n    # Related: exp_005_noise_prop (v1, DONE/failed — sigma_e=0 bug),\n    #   exp_005_noise_prop_v3 (DONE/failed), exp_005_noise_prop_v4 (DONE/negative)\n    # Note: all versions failed or negative; v4 completed but results negative\n\n  - id: exp-006\n    name: irt_calibration_and_baselines\n    claim: 1\n    also_supports: [3]\n    description: >\n      Fit 4PL+γ IRT (Stan NUTS) on controlled models from exp-001/003.\n      PRIMARY: per-benchmark fitting with benchmark-specific γ_k — this is\n      the natural parameterization when IRT is fitted per-benchmark (each\n      benchmark's model has its own γ_k). ABLATION: joint fitting across\n      benchmarks with shared global γ (stronger assumption, tests whether\n      contamination effect is homogeneous across benchmarks). Report both.\n      Per-benchmark fitting (not joint) is the default to reduce local\n      independence violation scope. Posterior predictive checks on item-level residual\n      correlations to assess local independence empirically.\n      Compute calibrated scores via exposure=0 counterfactual with CIs.\n      Compare against 7 baselines:\n      (0) Raw — no adjustment (anchor),\n      (1) remove-and-rescore (drop flagged items),\n      (2) single-signal 2PL+γ (best signal only, simpler IRT),\n      (3) vanilla 4PL without γ (standard IRT, no contamination modeling),\n      (4) linear exposure regression + bootstrap CI (simplest post-hoc),\n      (5) Emperor's mitigation: rephrasing + option shuffling,\n      (6) DCR fuzzy inference (EMNLP 2025) — the only existing method\n          producing adjusted accuracy; must include or reviewers will reject.\n      Evaluate all 5 metrics: MAE, coverage (50%/80%/95%), sharpness,\n      Kendall τ, dose-response monotonicity.\n      Report mean ± std across 3 seeds (matched to exp-001 seeds).\n    priority: P0\n    gpu_budget_hours: 8\n    deps: [exp-003]\n    benchmarks: [MMLU, GSM8K, ARC-Challenge, HumanEval]\n    seeds: 3\n    registry_id: exp_006_irt_05B_gsm8k\n    # Related: exp_006_irt_05B_arc (DONE/success), exp006-s1only-gsm8k-2pl (DONE/success),\n    #   exp006-oracle-arc-2pl (DONE/success), exp006-oracle-gsm8k-extended-v2 (DONE/success),\n    #   exp006-pooled-s1only-gsm8k-v2 (DONE/success), exp006-pooled-s1only-arc (DONE/success),\n    #   exp006-pooled-05B-15B-arc-v2 (DONE/success)\n\n  # ============================================================\n  # P1: Important — run if time/GPU permit\n  # ============================================================\n\n  - id: exp-015\n    name: sft_d100_qc_only\n    claim: 1\n    description: >\n      100% dosage SFT using only QC-pass paraphrases (7547/16697 items).\n      Isolates noisy vs clean contamination confound identified by reviewer.\n      D012 decision. Compare calibration metrics against exp-001 d100 (all\n      paraphrases) to quantify effect of noisy contamination on IRT estimates.\n    priority: P1\n    gpu_budget_hours: 5\n    deps: [exp-001]\n    benchmarks: [MMLU, GSM8K, ARC-Challenge, HumanEval]\n    models: [Qwen2.5-0.5B]\n    seeds: 1\n    status: planned\n    registry_id: exp_001_sft_d100_qc_only\n    data_script: exp001/prepare_qc_only_data.py\n\n  - id: exp-007\n    name: scale_bridging_7b\n    claim: 1\n    description: >\n      Qwen2.5-7B controlled SFT injection at 5 dosage levels.\n      Validates calibration accuracy scales to larger models.\n      Requires multi-GPU node (7B LoRA SFT ~4-8h per run on 1×H100).\n    priority: P1\n    gpu_budget_hours: 30\n    deps: [exp-001]\n\n  - id: exp-008\n    name: signal_survival_analysis\n    claim: 2\n    description: >\n      Systematic evaluation of detection signal reliability across training regimes.\n      Signal × regime AUC heatmap: 4 signals × {base, SFT-clean, SFT-contaminated,\n      RL-post-trained}. Confirms Self-Critique compensates where Min-K%++/ConStat\n      degrade post-RL (per fragility paper arXiv 2510.02386).\n      ELEVATED to Core Contribution 2 per Dream review (all 3 tiers identified\n      this as the most genuinely novel finding).\n    priority: P0\n    gpu_budget_hours: 10\n    deps: [exp-002]\n\n  - id: exp-014\n    name: multi_family_validation\n    claim: 1\n    description: >\n      Controlled SFT injection on at least one non-Qwen model family\n      (Llama-3.2-1B or Pythia-1.4B) at 3 dosage levels (0%, 25%, 100%).\n      Validates that identifiability boundaries and calibration accuracy\n      generalize beyond Qwen2.5. Addresses Dream reviewer concern about\n      single model family limiting generalizability (flagged [M][W]).\n    priority: P1\n    gpu_budget_hours: 15\n    deps: [exp-001]\n\n  - id: exp-009\n    name: rl_observational_case_study\n    claim: 2\n    also_supports: [3]\n    description: >\n      Apply Self-Critique + available signals to existing RL-trained models:\n      Qwen2.5-Instruct (0.5B/1.5B/3B/7B), DeepSeek-R1-Distill-1.5B/7B.\n      Fit IRT with appropriately wider CIs. Expected regret quantification:\n      compare uncalibrated vs calibrated vs remove-rescore for top-5 model\n      selection. Framed as observational — directional external validity,\n      not full quantitative validation. Near-zero γ check on known-clean\n      benchmark (specificity test).\n    priority: P1\n    gpu_budget_hours: 15\n    deps: [exp-006, exp-008]\n\n  # exp-010 (prior_sensitivity) and exp-011 (few_examinee_regime) merged into exp-004.\n  # Prior × N_models dimensions already covered in the sweep grid.\n\n  # ============================================================\n  # P2: Bonus — adds breadth if resources allow\n  # ============================================================\n\n  - id: exp-012\n    name: observational_72b\n    claim: 1\n    description: >\n      Qwen2.5-72B observational analysis (inference only, no SFT).\n      Extends ecological validity to frontier model scale.\n    priority: P2\n    gpu_budget_hours: 15\n    deps: [exp-006]\n\n  - id: exp-013\n    name: closed_weight_2signal_mode\n    claim: 2\n    description: >\n      Degraded 2-signal mode (ConStat + Self-Critique, no logits/embeddings)\n      for closed-weight models. Ablation quantifying 2-signal vs 4-signal\n      calibration accuracy gap.\n    priority: P2\n    gpu_budget_hours: 5\n    deps: [exp-003]\n\n# ============================================================\n# GPU Budget Summary\n# ============================================================\ngpu_budget:\n  P0_hours: 90\n  P1_hours: 60\n  P2_hours: 20\n  buffer_hours: 30\n  total_hours: 200\n  note: >\n    CPU-only experiments (exp-004, exp-005, exp-011) excluded.\n    Buffer covers reruns, debugging, multi-seed overhead, and unexpected issues.\n    Requires 2-4× H100/A100-80G for parallel SFT runs.\n    EMNLP 2026 ARR May 25 sprint (12 days from May 13):\n    - With 4× H100: P0 in ~4 days, P1 in ~3 days, total ~8 days (fits deadline)\n    - With 2× H100: P0 in ~7 days, P1 in ~4 days, tight but feasible if parallelized\n    - Day-8 contingency: reduce benchmarks to MMLU + GSM8K if behind schedule\n\n# Multi-seed protocol:\n# - exp-001, exp-006: 3 seeds, report mean ± std for key metrics\n# - exp-004, exp-005, exp-011: 10 seeds (simulation, CPU)\n# - exp-007, exp-008, exp-009: 1 seed (resource-constrained, note as limitation if needed)\n",
    "structuredPatch": [
      {
        "oldStart": 206,
        "oldLines": 7,
        "newStart": 206,
        "newLines": 7,
        "lines": [
          "     models: [Qwen2.5-0.5B]",
          "     seeds: 1",
          "     status: planned",
          "-    registry_id: exp_001_sft_d100_qc_only",
          "+    registry_id: null",
          "     data_script: exp001/prepare_qc_only_data.py",
          " ",
          "   - id: exp-007"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Tool call

_source line 130_

<details open><summary>🔧 Tool call — Edit · `toolu_01WiB34qkQGWEvA3Sncxh59u`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/experiment_plan.yaml",
  "old_string": "    deps: [exp-002]\n\n  - id: exp-014",
  "new_string": "    deps: [exp-002]\n    registry_id: exp_008_signal_survival_v4\n    # Related: exp_008_signal_survival (DONE/success), exp_008_base_pretrained_eval_v2 (DONE/success),\n    #   exp_008_base_pretrained_15B_eval_v2 (DONE/success), exp_008_instruct_05B_eval (DONE/success)\n\n  - id: exp-014"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d61fa97d-0b3f-42cc-a383-d75fd89e4948",
  "uuid": "4c1c9f34-55f5-47fd-a171-ba375ca64506",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UKH6PEcKW2jXD5D9ZNbohA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12013,
      "cache_read_input_tokens": 64899,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12013
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

_source line 131 · 2026-05-15T20:14:52.281Z_

<details><summary>↩ Tool result · `toolu_01WiB34qkQGWEvA3Sncxh59u`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/experiment_plan.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d61fa97d-0b3f-42cc-a383-d75fd89e4948",
  "uuid": "b3f96849-345a-4d81-8ce9-146c6e580046",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/experiment_plan.yaml",
    "oldString": "    deps: [exp-002]\n\n  - id: exp-014",
    "newString": "    deps: [exp-002]\n    registry_id: exp_008_signal_survival_v4\n    # Related: exp_008_signal_survival (DONE/success), exp_008_base_pretrained_eval_v2 (DONE/success),\n    #   exp_008_base_pretrained_15B_eval_v2 (DONE/success), exp_008_instruct_05B_eval (DONE/success)\n\n  - id: exp-014",
    "originalFile": "# ContamCal Experiment Plan\n# Each experiment maps to Core Claims in paper_framing.md\n# Priority: P0 = must-run, P1 = important, P2 = bonus\n\nexperiments:\n  # ============================================================\n  # P0: Core experiments — must complete for submission\n  # ============================================================\n\n  - id: exp-001\n    name: controlled_sft_injection\n    claim: 1\n    description: >\n      SFT contamination injection on Qwen2.5-0.5B/1.5B/3B at 5 dosage levels\n      (0%, 5%, 25%, 50%, 100% benchmark items as paraphrases in SFT data).\n      Produces ground-truth contaminated/clean model pairs. 15 SFT runs total\n      (3 models × 5 dosages), parallelized across GPUs. 3 seeds per condition\n      for key metrics (mean ± std).\n      Paraphrase generation: use strong open LLM (Qwen2.5-72B-Instruct or\n      equivalent) with controlled semantic similarity — following methodology\n      of \"Rethinking Benchmark and Contamination\" (arXiv 2023). Target:\n      high semantic similarity (cosine >0.85) but low lexical overlap\n      (BLEU <0.3) to evade n-gram decontamination while preserving\n      contamination effect. Quality validation: automated similarity metrics\n      + human spot-check on 50 random pairs per benchmark.\n    priority: P0\n    gpu_budget_hours: 50\n    deps: []\n    benchmarks: [MMLU, GSM8K, ARC-Challenge, HumanEval]\n    models: [Qwen2.5-0.5B, Qwen2.5-1.5B, Qwen2.5-3B]\n    seeds: 3\n    registry_id: exp_001_sft_injection\n    # Multi-run experiment; related successful registry entries:\n    # SFT training: exp_001_sft_0pct_05B, exp_001_sft_0pct_15B, exp_001_sft_0pct_3B,\n    #   exp_001_sft_0pct_05B_s123, exp_001_sft_0pct_15B_s123, exp_001_sft_0pct_3B_s123,\n    #   exp_001_sft_d005_05B_v3, exp_001_sft_d005_15B, exp_001_sft_d005_3B,\n    #   exp_001_sft_05B_d005_s123, exp_001_sft_15B_d005_s123_v2, exp_001_sft_3B_d005_s123,\n    #   exp_001_sft_d025_05B_v3, exp_001_sft_d025_15B, exp_001_sft_d025_3B_v2,\n    #   exp_001_sft_05B_d025_s123_v2, exp_001_sft_15B_d025_s123_v2, exp_001_sft_3B_d025_s123,\n    #   exp_001_sft_d100_05B, exp_001_sft_d100_15B_v2, exp_001_sft_d100_3B_v2,\n    #   exp_001_sft_05B_d100_s123, exp_001_sft_15B_d100_s123, exp_001_sft_3B_d100_s123,\n    #   exp_001_sft_3B_d000_v2, exp_001_sft_3B_d000_s123\n    # Eval (aligned): exp_001_eval_05B_d000_s123_aligned, exp_001_eval_05B_d005_aligned,\n    #   exp_001_eval_05B_d025_aligned, exp_001_eval_05B_d100_aligned_v4,\n    #   exp_001_eval_05B_d005_s123_aligned, exp_001_eval_05B_d025_s123_aligned,\n    #   exp_001_eval_05B_d100_s123_aligned, exp_001_eval_15B_aligned_batch,\n    #   exp_001_eval_15B_d005_aligned_v2, exp_001_eval_15B_d025_aligned,\n    #   exp_001_eval_15B_d100_aligned, exp_001_eval_15B_d000_s123_aligned,\n    #   exp_001_eval_15B_d100_s123_aligned, exp_001_eval_3B_d000_aligned,\n    #   exp_001_eval_3B_d005_aligned, exp_001_eval_3B_d100_aligned,\n    #   exp_001_eval_3B_d000_v2_aligned, exp_001_eval_3B_d025_v2_aligned,\n    #   exp_001_eval_3B_d100_v2_aligned_v2, exp_001_eval_3B_d000_s123_aligned,\n    #   exp_001_eval_3B_d005_s123_aligned, exp_001_eval_3B_d025_s123_aligned,\n    #   exp_001_eval_3B_d100_v2_s123_aligned, exp_001_eval_3B_d000_v2_s123_aligned\n    # Eval (para_aligned): exp_001_eval_05B_d005_para_aligned, exp_001_eval_05B_d025_aligned_v2,\n    #   exp_001_eval_05B_d005_s123_para_aligned, exp_001_eval_15B_d025_para_aligned,\n    #   exp_001_eval_3B_d000_s42_para_aligned, exp_001_eval_3B_d100_s42_para_aligned,\n    #   exp_001_eval_3B_d000_v2_para_aligned, exp_001_eval_3B_d000_v2_para_aligned_v2,\n    #   exp_001_eval_3B_d025_v2_para_aligned, exp_001_eval_3B_d100_v2_para_aligned,\n    #   exp_001_eval_3B_d005_s123_para_aligned, exp_001_eval_3B_d025_s123_para_aligned,\n    #   exp_001_eval_3B_d100_s123_para_aligned_v2, exp_001_eval_3B_d000_v2_s123_para_aligned\n    # Excluded from IRT pool: d000_s42 and d005_s42 experiments (lr=2e-4 confound, D076)\n\n  - id: exp-002\n    name: stage1_signal_pipeline\n    claim: 2\n    description: >\n      Compute 4 detection signals on all contaminated + clean models from exp-001:\n      (a) embedding-based semantic retrieval (FAISS + sentence-transformers),\n      (b) Min-K%++ membership inference,\n      (c) ConStat performance gap (original vs paraphrased items),\n      (d) Self-Critique entropy collapse.\n      Output: per-model-item exposure scores for each signal.\n    priority: P0\n    gpu_budget_hours: 20\n    deps: [exp-001]\n    registry_id: exp_002_signals_05B\n    # Related: exp002-signals-1p5B (DONE/success), exp002-signal-d025-05B (DONE/success)\n    # Note: 3B signal runs (exp_002_signals_3B v1-v4) all failed/killed\n\n  - id: exp-003\n    name: rrf_aggregation_ablation\n    claim: 2\n    description: >\n      RRF fusion of 4 signals into composite per-item exposure score.\n      Ablations: (a) RRF vs equal-weight rank averaging, (b) single-signal only\n      (×4), (c) calibration-based weighted RRF variant, (d) false positive\n      injection robustness check (inject FP at rates matching Duan et al. 2024).\n      Also test degraded 2-signal mode (ConStat + Self-Critique) for closed-weight.\n    priority: P0\n    gpu_budget_hours: 2\n    deps: [exp-002]\n    registry_id: exp_003_rrf_05B\n    # Related: exp_003_mmlu_item_aligned_gap (DONE/success)\n\n  - id: exp-004\n    name: simulation_identifiability_sweep\n    claim: 1\n    also_supports: [3]\n    description: >\n      Systematic synthetic-data sweep (NEW, not MVP — MVP only covered 4-5 conditions):\n      exposure signal AUC (0.55, 0.60, 0.65, 0.70, 0.80, 0.90) ×\n      model count (20, 50, 100, 200) ×\n      prior strength (N(0,0.5), N(0,1), N(0,2)) ×\n      exposure type (binary, continuous).\n      144 conditions, 10 seeds each. Reports: θ-γ recovery RMSE, posterior\n      correlation, coverage (50%/80%/95%), prior sensitivity. Establishes\n      minimum AUC threshold; if 95% CI width > 15pp at AUC=0.65, label as\n      \"cannot distinguish no contamination from moderate contamination.\"\n      N_items=300 fixed (per MVP finding).\n      Subsumes exp-010 (prior sensitivity) and exp-011 (few-examinee regime)\n      — prior × N_models dimensions already in sweep grid. Growing Pains\n      pre-estimation sub-experiment: at N_models=20/50, compare flat prior\n      vs informative prior from pre-estimated item parameters.\n      Also includes Fisher Information matrix analysis: derive approximate\n      analytical relationship between signal AUC, N_models, and γ\n      recoverability. Distinguish structural identifiability (parameters\n      uniquely determined) from practical identifiability (estimation\n      quality sufficient for decisions). Provides theoretical grounding\n      for the empirical AUC ≥ 0.70 threshold.\n    priority: P0\n    gpu_budget_hours: 0\n    deps: []\n    note: CPU only. MVP (mvp_sim_4pl_gamma) was preliminary; this is the full sweep.\n    registry_id: exp_004_sim_sweep\n    # Related: mvp_sim_4pl_gamma (DONE/success), mvp_sim_confounding (DONE/success),\n    #   exp_004_sim_sweep_extreme_gamma (DONE/success)\n    # Note: full sweep v1-v6 all failed (tmpfs/timeout issues); MVP + extreme_gamma succeeded\n\n  - id: exp-005\n    name: noise_propagation_analysis\n    claim: 3\n    description: >\n      Two parts:\n      (A) Measurement error model (PRIMARY): extend Stan model to treat exposure\n      as noisy observation: exposure_ij ~ N(τ_ij, σ_e²), where τ is latent true\n      contamination. σ_e estimated from exp-001 ground truth FP/FN rates.\n      This propagates Stage 1 uncertainty into posteriors automatically.\n      Compare coverage (50%/80%/95%) vs point-estimate exposure baseline.\n      (B) Post-hoc noise injection: inject Gaussian noise at 1×/1.5×/2× matched\n      levels, re-fit standard model, measure CI widening for γ and θ.\n      Both parts inform whether measurement error model closes the coverage gap.\n    priority: P0\n    gpu_budget_hours: 0\n    deps: [exp-002, exp-004]\n    note: CPU only\n    registry_id: exp_005_noise_prop_v2\n    # Related: exp_005_noise_prop (v1, DONE/failed — sigma_e=0 bug),\n    #   exp_005_noise_prop_v3 (DONE/failed), exp_005_noise_prop_v4 (DONE/negative)\n    # Note: all versions failed or negative; v4 completed but results negative\n\n  - id: exp-006\n    name: irt_calibration_and_baselines\n    claim: 1\n    also_supports: [3]\n    description: >\n      Fit 4PL+γ IRT (Stan NUTS) on controlled models from exp-001/003.\n      PRIMARY: per-benchmark fitting with benchmark-specific γ_k — this is\n      the natural parameterization when IRT is fitted per-benchmark (each\n      benchmark's model has its own γ_k). ABLATION: joint fitting across\n      benchmarks with shared global γ (stronger assumption, tests whether\n      contamination effect is homogeneous across benchmarks). Report both.\n      Per-benchmark fitting (not joint) is the default to reduce local\n      independence violation scope. Posterior predictive checks on item-level residual\n      correlations to assess local independence empirically.\n      Compute calibrated scores via exposure=0 counterfactual with CIs.\n      Compare against 7 baselines:\n      (0) Raw — no adjustment (anchor),\n      (1) remove-and-rescore (drop flagged items),\n      (2) single-signal 2PL+γ (best signal only, simpler IRT),\n      (3) vanilla 4PL without γ (standard IRT, no contamination modeling),\n      (4) linear exposure regression + bootstrap CI (simplest post-hoc),\n      (5) Emperor's mitigation: rephrasing + option shuffling,\n      (6) DCR fuzzy inference (EMNLP 2025) — the only existing method\n          producing adjusted accuracy; must include or reviewers will reject.\n      Evaluate all 5 metrics: MAE, coverage (50%/80%/95%), sharpness,\n      Kendall τ, dose-response monotonicity.\n      Report mean ± std across 3 seeds (matched to exp-001 seeds).\n    priority: P0\n    gpu_budget_hours: 8\n    deps: [exp-003]\n    benchmarks: [MMLU, GSM8K, ARC-Challenge, HumanEval]\n    seeds: 3\n    registry_id: exp_006_irt_05B_gsm8k\n    # Related: exp_006_irt_05B_arc (DONE/success), exp006-s1only-gsm8k-2pl (DONE/success),\n    #   exp006-oracle-arc-2pl (DONE/success), exp006-oracle-gsm8k-extended-v2 (DONE/success),\n    #   exp006-pooled-s1only-gsm8k-v2 (DONE/success), exp006-pooled-s1only-arc (DONE/success),\n    #   exp006-pooled-05B-15B-arc-v2 (DONE/success)\n\n  # ============================================================\n  # P1: Important — run if time/GPU permit\n  # ============================================================\n\n  - id: exp-015\n    name: sft_d100_qc_only\n    claim: 1\n    description: >\n      100% dosage SFT using only QC-pass paraphrases (7547/16697 items).\n      Isolates noisy vs clean contamination confound identified by reviewer.\n      D012 decision. Compare calibration metrics against exp-001 d100 (all\n      paraphrases) to quantify effect of noisy contamination on IRT estimates.\n    priority: P1\n    gpu_budget_hours: 5\n    deps: [exp-001]\n    benchmarks: [MMLU, GSM8K, ARC-Challenge, HumanEval]\n    models: [Qwen2.5-0.5B]\n    seeds: 1\n    status: planned\n    registry_id: null\n    data_script: exp001/prepare_qc_only_data.py\n\n  - id: exp-007\n    name: scale_bridging_7b\n    claim: 1\n    description: >\n      Qwen2.5-7B controlled SFT injection at 5 dosage levels.\n      Validates calibration accuracy scales to larger models.\n      Requires multi-GPU node (7B LoRA SFT ~4-8h per run on 1×H100).\n    priority: P1\n    gpu_budget_hours: 30\n    deps: [exp-001]\n\n  - id: exp-008\n    name: signal_survival_analysis\n    claim: 2\n    description: >\n      Systematic evaluation of detection signal reliability across training regimes.\n      Signal × regime AUC heatmap: 4 signals × {base, SFT-clean, SFT-contaminated,\n      RL-post-trained}. Confirms Self-Critique compensates where Min-K%++/ConStat\n      degrade post-RL (per fragility paper arXiv 2510.02386).\n      ELEVATED to Core Contribution 2 per Dream review (all 3 tiers identified\n      this as the most genuinely novel finding).\n    priority: P0\n    gpu_budget_hours: 10\n    deps: [exp-002]\n\n  - id: exp-014\n    name: multi_family_validation\n    claim: 1\n    description: >\n      Controlled SFT injection on at least one non-Qwen model family\n      (Llama-3.2-1B or Pythia-1.4B) at 3 dosage levels (0%, 25%, 100%).\n      Validates that identifiability boundaries and calibration accuracy\n      generalize beyond Qwen2.5. Addresses Dream reviewer concern about\n      single model family limiting generalizability (flagged [M][W]).\n    priority: P1\n    gpu_budget_hours: 15\n    deps: [exp-001]\n\n  - id: exp-009\n    name: rl_observational_case_study\n    claim: 2\n    also_supports: [3]\n    description: >\n      Apply Self-Critique + available signals to existing RL-trained models:\n      Qwen2.5-Instruct (0.5B/1.5B/3B/7B), DeepSeek-R1-Distill-1.5B/7B.\n      Fit IRT with appropriately wider CIs. Expected regret quantification:\n      compare uncalibrated vs calibrated vs remove-rescore for top-5 model\n      selection. Framed as observational — directional external validity,\n      not full quantitative validation. Near-zero γ check on known-clean\n      benchmark (specificity test).\n    priority: P1\n    gpu_budget_hours: 15\n    deps: [exp-006, exp-008]\n\n  # exp-010 (prior_sensitivity) and exp-011 (few_examinee_regime) merged into exp-004.\n  # Prior × N_models dimensions already covered in the sweep grid.\n\n  # ============================================================\n  # P2: Bonus — adds breadth if resources allow\n  # ============================================================\n\n  - id: exp-012\n    name: observational_72b\n    claim: 1\n    description: >\n      Qwen2.5-72B observational analysis (inference only, no SFT).\n      Extends ecological validity to frontier model scale.\n    priority: P2\n    gpu_budget_hours: 15\n    deps: [exp-006]\n\n  - id: exp-013\n    name: closed_weight_2signal_mode\n    claim: 2\n    description: >\n      Degraded 2-signal mode (ConStat + Self-Critique, no logits/embeddings)\n      for closed-weight models. Ablation quantifying 2-signal vs 4-signal\n      calibration accuracy gap.\n    priority: P2\n    gpu_budget_hours: 5\n    deps: [exp-003]\n\n# ============================================================\n# GPU Budget Summary\n# ============================================================\ngpu_budget:\n  P0_hours: 90\n  P1_hours: 60\n  P2_hours: 20\n  buffer_hours: 30\n  total_hours: 200\n  note: >\n    CPU-only experiments (exp-004, exp-005, exp-011) excluded.\n    Buffer covers reruns, debugging, multi-seed overhead, and unexpected issues.\n    Requires 2-4× H100/A100-80G for parallel SFT runs.\n    EMNLP 2026 ARR May 25 sprint (12 days from May 13):\n    - With 4× H100: P0 in ~4 days, P1 in ~3 days, total ~8 days (fits deadline)\n    - With 2× H100: P0 in ~7 days, P1 in ~4 days, tight but feasible if parallelized\n    - Day-8 contingency: reduce benchmarks to MMLU + GSM8K if behind schedule\n\n# Multi-seed protocol:\n# - exp-001, exp-006: 3 seeds, report mean ± std for key metrics\n# - exp-004, exp-005, exp-011: 10 seeds (simulation, CPU)\n# - exp-007, exp-008, exp-009: 1 seed (resource-constrained, note as limitation if needed)\n",
    "structuredPatch": [
      {
        "oldStart": 233,
        "oldLines": 6,
        "newStart": 233,
        "newLines": 9,
        "lines": [
          "     priority: P0",
          "     gpu_budget_hours: 10",
          "     deps: [exp-002]",
          "+    registry_id: exp_008_signal_survival_v4",
          "+    # Related: exp_008_signal_survival (DONE/success), exp_008_base_pretrained_eval_v2 (DONE/success),",
          "+    #   exp_008_base_pretrained_15B_eval_v2 (DONE/success), exp_008_instruct_05B_eval (DONE/success)",
          " ",
          "   - id: exp-014",
          "     name: multi_family_validation"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Assistant

_source line 132_

All edits applied. Let me verify the file and recompute coverage.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d61fa97d-0b3f-42cc-a383-d75fd89e4948",
  "uuid": "ecc1ac79-529e-4686-97f9-3a10ca729e16",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GRkDTbwWmggkfToS5ejR1f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1829,
      "cache_read_input_tokens": 76912,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1829
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

_source line 133_

<details open><summary>🔧 Tool call — Read · `toolu_01Ctvuoe9W4CVVcfZDQBYU54`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d61fa97d-0b3f-42cc-a383-d75fd89e4948",
  "uuid": "dd0280ef-cfa6-465d-9061-98a248393673",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GRkDTbwWmggkfToS5ejR1f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1829,
      "cache_read_input_tokens": 76912,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1829
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

_source line 134 · 2026-05-15T20:14:56.102Z_

<details><summary>↩ Tool result · `toolu_01Ctvuoe9W4CVVcfZDQBYU54`</summary>

```text
1	# ContamCal Experiment Plan
2	# Each experiment maps to Core Claims in paper_framing.md
3	# Priority: P0 = must-run, P1 = important, P2 = bonus
4	
5	experiments:
6	  # ============================================================
7	  # P0: Core experiments — must complete for submission
8	  # ============================================================
9	
10	  - id: exp-001
11	    name: controlled_sft_injection
12	    claim: 1
13	    description: >
14	      SFT contamination injection on Qwen2.5-0.5B/1.5B/3B at 5 dosage levels
15	      (0%, 5%, 25%, 50%, 100% benchmark items as paraphrases in SFT data).
16	      Produces ground-truth contaminated/clean model pairs. 15 SFT runs total
17	      (3 models × 5 dosages), parallelized across GPUs. 3 seeds per condition
18	      for key metrics (mean ± std).
19	      Paraphrase generation: use strong open LLM (Qwen2.5-72B-Instruct or
20	      equivalent) with controlled semantic similarity — following methodology
21	      of "Rethinking Benchmark and Contamination" (arXiv 2023). Target:
22	      high semantic similarity (cosine >0.85) but low lexical overlap
23	      (BLEU <0.3) to evade n-gram decontamination while preserving
24	      contamination effect. Quality validation: automated similarity metrics
25	      + human spot-check on 50 random pairs per benchmark.
26	    priority: P0
27	    gpu_budget_hours: 50
28	    deps: []
29	    benchmarks: [MMLU, GSM8K, ARC-Challenge, HumanEval]
30	    models: [Qwen2.5-0.5B, Qwen2.5-1.5B, Qwen2.5-3B]
31	    seeds: 3
32	    registry_id: exp_001_sft_injection
33	    # Multi-run experiment; related successful registry entries:
34	    # SFT training: exp_001_sft_0pct_05B, exp_001_sft_0pct_15B, exp_001_sft_0pct_3B,
35	    #   exp_001_sft_0pct_05B_s123, exp_001_sft_0pct_15B_s123, exp_001_sft_0pct_3B_s123,
36	    #   exp_001_sft_d005_05B_v3, exp_001_sft_d005_15B, exp_001_sft_d005_3B,
37	    #   exp_001_sft_05B_d005_s123, exp_001_sft_15B_d005_s123_v2, exp_001_sft_3B_d005_s123,
38	    #   exp_001_sft_d025_05B_v3, exp_001_sft_d025_15B, exp_001_sft_d025_3B_v2,
39	    #   exp_001_sft_05B_d025_s123_v2, exp_001_sft_15B_d025_s123_v2, exp_001_sft_3B_d025_s123,
40	    #   exp_001_sft_d100_05B, exp_001_sft_d100_15B_v2, exp_001_sft_d100_3B_v2,
41	    #   exp_001_sft_05B_d100_s123, exp_001_sft_15B_d100_s123, exp_001_sft_3B_d100_s123,
42	    #   exp_001_sft_3B_d000_v2, exp_001_sft_3B_d000_s123
43	    # Eval (aligned): exp_001_eval_05B_d000_s123_aligned, exp_001_eval_05B_d005_aligned,
44	    #   exp_001_eval_05B_d025_aligned, exp_001_eval_05B_d100_aligned_v4,
45	    #   exp_001_eval_05B_d005_s123_aligned, exp_001_eval_05B_d025_s123_aligned,
46	    #   exp_001_eval_05B_d100_s123_aligned, exp_001_eval_15B_aligned_batch,
47	    #   exp_001_eval_15B_d005_aligned_v2, exp_001_eval_15B_d025_aligned,
48	    #   exp_001_eval_15B_d100_aligned, exp_001_eval_15B_d000_s123_aligned,
49	    #   exp_001_eval_15B_d100_s123_aligned, exp_001_eval_3B_d000_aligned,
50	    #   exp_001_eval_3B_d005_aligned, exp_001_eval_3B_d100_aligned,
51	    #   exp_001_eval_3B_d000_v2_aligned, exp_001_eval_3B_d025_v2_aligned,
52	    #   exp_001_eval_3B_d100_v2_aligned_v2, exp_001_eval_3B_d000_s123_aligned,
53	    #   exp_001_eval_3B_d005_s123_aligned, exp_001_eval_3B_d025_s123_aligned,
54	    #   exp_001_eval_3B_d100_v2_s123_aligned, exp_001_eval_3B_d000_v2_s123_aligned
55	    # Eval (para_aligned): exp_001_eval_05B_d005_para_aligned, exp_001_eval_05B_d025_aligned_v2,
56	    #   exp_001_eval_05B_d005_s123_para_aligned, exp_001_eval_15B_d025_para_aligned,
57	    #   exp_001_eval_3B_d000_s42_para_aligned, exp_001_eval_3B_d100_s42_para_aligned,
58	    #   exp_001_eval_3B_d000_v2_para_aligned, exp_001_eval_3B_d000_v2_para_aligned_v2,
59	    #   exp_001_eval_3B_d025_v2_para_aligned, exp_001_eval_3B_d100_v2_para_aligned,
60	    #   exp_001_eval_3B_d005_s123_para_aligned, exp_001_eval_3B_d025_s123_para_aligned,
61	    #   exp_001_eval_3B_d100_s123_para_aligned_v2, exp_001_eval_3B_d000_v2_s123_para_aligned
62	    # Excluded from IRT pool: d000_s42 and d005_s42 experiments (lr=2e-4 confound, D076)
63	
64	  - id: exp-002
65	    name: stage1_signal_pipeline
66	    claim: 2
67	    description: >
68	      Compute 4 detection signals on all contaminated + clean models from exp-001:
69	      (a) embedding-based semantic retrieval (FAISS + sentence-transformers),
70	      (b) Min-K%++ membership inference,
71	      (c) ConStat performance gap (original vs paraphrased items),
72	      (d) Self-Critique entropy collapse.
73	      Output: per-model-item exposure scores for each signal.
74	    priority: P0
75	    gpu_budget_hours: 20
76	    deps: [exp-001]
77	    registry_id: exp_002_signals_05B
78	    # Related: exp002-signals-1p5B (DONE/success), exp002-signal-d025-05B (DONE/success)
79	    # Note: 3B signal runs (exp_002_signals_3B v1-v4) all failed/killed
80	
81	  - id: exp-003
82	    name: rrf_aggregation_ablation
83	    claim: 2
84	    description: >
85	      RRF fusion of 4 signals into composite per-item exposure score.
86	      Ablations: (a) RRF vs equal-weight rank averaging, (b) single-signal only
87	      (×4), (c) calibration-based weighted RRF variant, (d) false positive
88	      injection robustness check (inject FP at rates matching Duan et al. 2024).
89	      Also test degraded 2-signal mode (ConStat + Self-Critique) for closed-weight.
90	    priority: P0
91	    gpu_budget_hours: 2
92	    deps: [exp-002]
93	    registry_id: exp_003_rrf_05B
94	    # Related: exp_003_mmlu_item_aligned_gap (DONE/success)
95	
96	  - id: exp-004
97	    name: simulation_identifiability_sweep
98	    claim: 1
99	    also_supports: [3]
100	    description: >
101	      Systematic synthetic-data sweep (NEW, not MVP — MVP only covered 4-5 conditions):
102	      exposure signal AUC (0.55, 0.60, 0.65, 0.70, 0.80, 0.90) ×
103	      model count (20, 50, 100, 200) ×
104	      prior strength (N(0,0.5), N(0,1), N(0,2)) ×
105	      exposure type (binary, continuous).
106	      144 conditions, 10 seeds each. Reports: θ-γ recovery RMSE, posterior
107	      correlation, coverage (50%/80%/95%), prior sensitivity. Establishes
108	      minimum AUC threshold; if 95% CI width > 15pp at AUC=0.65, label as
109	      "cannot distinguish no contamination from moderate contamination."
110	      N_items=300 fixed (per MVP finding).
111	      Subsumes exp-010 (prior sensitivity) and exp-011 (few-examinee regime)
112	      — prior × N_models dimensions already in sweep grid. Growing Pains
113	      pre-estimation sub-experiment: at N_models=20/50, compare flat prior
114	      vs informative prior from pre-estimated item parameters.
115	      Also includes Fisher Information matrix analysis: derive approximate
116	      analytical relationship between signal AUC, N_models, and γ
117	      recoverability. Distinguish structural identifiability (parameters
118	      uniquely determined) from practical identifiability (estimation
119	      quality sufficient for decisions). Provides theoretical grounding
120	      for the empirical AUC ≥ 0.70 threshold.
121	    priority: P0
122	    gpu_budget_hours: 0
123	    deps: []
124	    note: CPU only. MVP (mvp_sim_4pl_gamma) was preliminary; this is the full sweep.
125	    registry_id: exp_004_sim_sweep
126	    # Related: mvp_sim_4pl_gamma (DONE/success), mvp_sim_confounding (DONE/success),
127	    #   exp_004_sim_sweep_extreme_gamma (DONE/success)
128	    # Note: full sweep v1-v6 all failed (tmpfs/timeout issues); MVP + extreme_gamma succeeded
129	
130	  - id: exp-005
131	    name: noise_propagation_analysis
132	    claim: 3
133	    description: >
134	      Two parts:
135	      (A) Measurement error model (PRIMARY): extend Stan model to treat exposure
136	      as noisy observation: exposure_ij ~ N(τ_ij, σ_e²), where τ is latent true
137	      contamination. σ_e estimated from exp-001 ground truth FP/FN rates.
138	      This propagates Stage 1 uncertainty into posteriors automatically.
139	      Compare coverage (50%/80%/95%) vs point-estimate exposure baseline.
140	      (B) Post-hoc noise injection: inject Gaussian noise at 1×/1.5×/2× matched
141	      levels, re-fit standard model, measure CI widening for γ and θ.
142	      Both parts inform whether measurement error model closes the coverage gap.
143	    priority: P0
144	    gpu_budget_hours: 0
145	    deps: [exp-002, exp-004]
146	    note: CPU only
147	    registry_id: exp_005_noise_prop_v2
148	    # Related: exp_005_noise_prop (v1, DONE/failed — sigma_e=0 bug),
149	    #   exp_005_noise_prop_v3 (DONE/failed), exp_005_noise_prop_v4 (DONE/negative)
150	    # Note: all versions failed or negative; v4 completed but results negative
151	
152	  - id: exp-006
153	    name: irt_calibration_and_baselines
154	    claim: 1
155	    also_supports: [3]
156	    description: >
157	      Fit 4PL+γ IRT (Stan NUTS) on controlled models from exp-001/003.
158	      PRIMARY: per-benchmark fitting with benchmark-specific γ_k — this is
159	      the natural parameterization when IRT is fitted per-benchmark (each
160	      benchmark's model has its own γ_k). ABLATION: joint fitting across
161	      benchmarks with shared global γ (stronger assumption, tests whether
162	      contamination effect is homogeneous across benchmarks). Report both.
163	      Per-benchmark fitting (not joint) is the default to reduce local
164	      independence violation scope. Posterior predictive checks on item-level residual
165	      correlations to assess local independence empirically.
166	      Compute calibrated scores via exposure=0 counterfactual with CIs.
167	      Compare against 7 baselines:
168	      (0) Raw — no adjustment (anchor),
169	      (1) remove-and-rescore (drop flagged items),
170	      (2) single-signal 2PL+γ (best signal only, simpler IRT),
171	      (3) vanilla 4PL without γ (standard IRT, no contamination modeling),
172	      (4) linear exposure regression + bootstrap CI (simplest post-hoc),
173	      (5) Emperor's mitigation: rephrasing + option shuffling,
174	      (6) DCR fuzzy inference (EMNLP 2025) — the only existing method
175	          producing adjusted accuracy; must include or reviewers will reject.
176	      Evaluate all 5 metrics: MAE, coverage (50%/80%/95%), sharpness,
177	      Kendall τ, dose-response monotonicity.
178	      Report mean ± std across 3 seeds (matched to exp-001 seeds).
179	    priority: P0
180	    gpu_budget_hours: 8
181	    deps: [exp-003]
182	    benchmarks: [MMLU, GSM8K, ARC-Challenge, HumanEval]
183	    seeds: 3
184	    registry_id: exp_006_irt_05B_gsm8k
185	    # Related: exp_006_irt_05B_arc (DONE/success), exp006-s1only-gsm8k-2pl (DONE/success),
186	    #   exp006-oracle-arc-2pl (DONE/success), exp006-oracle-gsm8k-extended-v2 (DONE/success),
187	    #   exp006-pooled-s1only-gsm8k-v2 (DONE/success), exp006-pooled-s1only-arc (DONE/success),
188	    #   exp006-pooled-05B-15B-arc-v2 (DONE/success)
189	
190	  # ============================================================
191	  # P1: Important — run if time/GPU permit
192	  # ============================================================
193	
194	  - id: exp-015
195	    name: sft_d100_qc_only
196	    claim: 1
197	    description: >
198	      100% dosage SFT using only QC-pass paraphrases (7547/16697 items).
199	      Isolates noisy vs clean contamination confound identified by reviewer.
200	      D012 decision. Compare calibration metrics against exp-001 d100 (all
201	      paraphrases) to quantify effect of noisy contamination on IRT estimates.
202	    priority: P1
203	    gpu_budget_hours: 5
204	    deps: [exp-001]
205	    benchmarks: [MMLU, GSM8K, ARC-Challenge, HumanEval]
206	    models: [Qwen2.5-0.5B]
207	    seeds: 1
208	    status: planned
209	    registry_id: null
210	    data_script: exp001/prepare_qc_only_data.py
211	
212	  - id: exp-007
213	    name: scale_bridging_7b
214	    claim: 1
215	    description: >
216	      Qwen2.5-7B controlled SFT injection at 5 dosage levels.
217	      Validates calibration accuracy scales to larger models.
218	      Requires multi-GPU node (7B LoRA SFT ~4-8h per run on 1×H100).
219	    priority: P1
220	    gpu_budget_hours: 30
221	    deps: [exp-001]
222	
223	  - id: exp-008
224	    name: signal_survival_analysis
225	    claim: 2
226	    description: >
227	      Systematic evaluation of detection signal reliability across training regimes.
228	      Signal × regime AUC heatmap: 4 signals × {base, SFT-clean, SFT-contaminated,
229	      RL-post-trained}. Confirms Self-Critique compensates where Min-K%++/ConStat
230	      degrade post-RL (per fragility paper arXiv 2510.02386).
231	      ELEVATED to Core Contribution 2 per Dream review (all 3 tiers identified
232	      this as the most genuinely novel finding).
233	    priority: P0
234	    gpu_budget_hours: 10
235	    deps: [exp-002]
236	    registry_id: exp_008_signal_survival_v4
237	    # Related: exp_008_signal_survival (DONE/success), exp_008_base_pretrained_eval_v2 (DONE/success),
238	    #   exp_008_base_pretrained_15B_eval_v2 (DONE/success), exp_008_instruct_05B_eval (DONE/success)
239	
240	  - id: exp-014
241	    name: multi_family_validation
242	    claim: 1
243	    description: >
244	      Controlled SFT injection on at least one non-Qwen model family
245	      (Llama-3.2-1B or Pythia-1.4B) at 3 dosage levels (0%, 25%, 100%).
246	      Validates that identifiability boundaries and calibration accuracy
247	      generalize beyond Qwen2.5. Addresses Dream reviewer concern about
248	      single model family limiting generalizability (flagged [M][W]).
249	    priority: P1
250	    gpu_budget_hours: 15
251	    deps: [exp-001]
252	
253	  - id: exp-009
254	    name: rl_observational_case_study
255	    claim: 2
256	    also_supports: [3]
257	    description: >
258	      Apply Self-Critique + available signals to existing RL-trained models:
259	      Qwen2.5-Instruct (0.5B/1.5B/3B/7B), DeepSeek-R1-Distill-1.5B/7B.
260	      Fit IRT with appropriately wider CIs. Expected regret quantification:
261	      compare uncalibrated vs calibrated vs remove-rescore for top-5 model
262	      selection. Framed as observational — directional external validity,
263	      not full quantitative validation. Near-zero γ check on known-clean
264	      benchmark (specificity test).
265	    priority: P1
266	    gpu_budget_hours: 15
267	    deps: [exp-006, exp-008]
268	
269	  # exp-010 (prior_sensitivity) and exp-011 (few_examinee_regime) merged into exp-004.
270	  # Prior × N_models dimensions already covered in the sweep grid.
271	
272	  # ============================================================
273	  # P2: Bonus — adds breadth if resources allow
274	  # ============================================================
275	
276	  - id: exp-012
277	    name: observational_72b
278	    claim: 1
279	    description: >
280	      Qwen2.5-72B observational analysis (inference only, no SFT).
281	      Extends ecological validity to frontier model scale.
282	    priority: P2
283	    gpu_budget_hours: 15
284	    deps: [exp-006]
285	
286	  - id: exp-013
287	    name: closed_weight_2signal_mode
288	    claim: 2
289	    description: >
290	      Degraded 2-signal mode (ConStat + Self-Critique, no logits/embeddings)
291	      for closed-weight models. Ablation quantifying 2-signal vs 4-signal
292	      calibration accuracy gap.
293	    priority: P2
294	    gpu_budget_hours: 5
295	    deps: [exp-003]
296	
297	# ============================================================
298	# GPU Budget Summary
299	# ============================================================
300	gpu_budget:
301	  P0_hours: 90
302	  P1_hours: 60
303	  P2_hours: 20
304	  buffer_hours: 30
305	  total_hours: 200
306	  note: >
307	    CPU-only experiments (exp-004, exp-005, exp-011) excluded.
308	    Buffer covers reruns, debugging, multi-seed overhead, and unexpected issues.
309	    Requires 2-4× H100/A100-80G for parallel SFT runs.
310	    EMNLP 2026 ARR May 25 sprint (12 days from May 13):
311	    - With 4× H100: P0 in ~4 days, P1 in ~3 days, total ~8 days (fits deadline)
312	    - With 2× H100: P0 in ~7 days, P1 in ~4 days, tight but feasible if parallelized
313	    - Day-8 contingency: reduce benchmarks to MMLU + GSM8K if behind schedule
314	
315	# Multi-seed protocol:
316	# - exp-001, exp-006: 3 seeds, report mean ± std for key metrics
317	# - exp-004, exp-005, exp-011: 10 seeds (simulation, CPU)
318	# - exp-007, exp-008, exp-009: 1 seed (resource-constrained, note as limitation if needed)
319	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d61fa97d-0b3f-42cc-a383-d75fd89e4948",
  "uuid": "2f824e24-9692-4c7a-b877-d0129cbe685c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/experiment_plan.yaml",
      "content": "# ContamCal Experiment Plan\n# Each experiment maps to Core Claims in paper_framing.md\n# Priority: P0 = must-run, P1 = important, P2 = bonus\n\nexperiments:\n  # ============================================================\n  # P0: Core experiments — must complete for submission\n  # ============================================================\n\n  - id: exp-001\n    name: controlled_sft_injection\n    claim: 1\n    description: >\n      SFT contamination injection on Qwen2.5-0.5B/1.5B/3B at 5 dosage levels\n      (0%, 5%, 25%, 50%, 100% benchmark items as paraphrases in SFT data).\n      Produces ground-truth contaminated/clean model pairs. 15 SFT runs total\n      (3 models × 5 dosages), parallelized across GPUs. 3 seeds per condition\n      for key metrics (mean ± std).\n      Paraphrase generation: use strong open LLM (Qwen2.5-72B-Instruct or\n      equivalent) with controlled semantic similarity — following methodology\n      of \"Rethinking Benchmark and Contamination\" (arXiv 2023). Target:\n      high semantic similarity (cosine >0.85) but low lexical overlap\n      (BLEU <0.3) to evade n-gram decontamination while preserving\n      contamination effect. Quality validation: automated similarity metrics\n      + human spot-check on 50 random pairs per benchmark.\n    priority: P0\n    gpu_budget_hours: 50\n    deps: []\n    benchmarks: [MMLU, GSM8K, ARC-Challenge, HumanEval]\n    models: [Qwen2.5-0.5B, Qwen2.5-1.5B, Qwen2.5-3B]\n    seeds: 3\n    registry_id: exp_001_sft_injection\n    # Multi-run experiment; related successful registry entries:\n    # SFT training: exp_001_sft_0pct_05B, exp_001_sft_0pct_15B, exp_001_sft_0pct_3B,\n    #   exp_001_sft_0pct_05B_s123, exp_001_sft_0pct_15B_s123, exp_001_sft_0pct_3B_s123,\n    #   exp_001_sft_d005_05B_v3, exp_001_sft_d005_15B, exp_001_sft_d005_3B,\n    #   exp_001_sft_05B_d005_s123, exp_001_sft_15B_d005_s123_v2, exp_001_sft_3B_d005_s123,\n    #   exp_001_sft_d025_05B_v3, exp_001_sft_d025_15B, exp_001_sft_d025_3B_v2,\n    #   exp_001_sft_05B_d025_s123_v2, exp_001_sft_15B_d025_s123_v2, exp_001_sft_3B_d025_s123,\n    #   exp_001_sft_d100_05B, exp_001_sft_d100_15B_v2, exp_001_sft_d100_3B_v2,\n    #   exp_001_sft_05B_d100_s123, exp_001_sft_15B_d100_s123, exp_001_sft_3B_d100_s123,\n    #   exp_001_sft_3B_d000_v2, exp_001_sft_3B_d000_s123\n    # Eval (aligned): exp_001_eval_05B_d000_s123_aligned, exp_001_eval_05B_d005_aligned,\n    #   exp_001_eval_05B_d025_aligned, exp_001_eval_05B_d100_aligned_v4,\n    #   exp_001_eval_05B_d005_s123_aligned, exp_001_eval_05B_d025_s123_aligned,\n    #   exp_001_eval_05B_d100_s123_aligned, exp_001_eval_15B_aligned_batch,\n    #   exp_001_eval_15B_d005_aligned_v2, exp_001_eval_15B_d025_aligned,\n    #   exp_001_eval_15B_d100_aligned, exp_001_eval_15B_d000_s123_aligned,\n    #   exp_001_eval_15B_d100_s123_aligned, exp_001_eval_3B_d000_aligned,\n    #   exp_001_eval_3B_d005_aligned, exp_001_eval_3B_d100_aligned,\n    #   exp_001_eval_3B_d000_v2_aligned, exp_001_eval_3B_d025_v2_aligned,\n    #   exp_001_eval_3B_d100_v2_aligned_v2, exp_001_eval_3B_d000_s123_aligned,\n    #   exp_001_eval_3B_d005_s123_aligned, exp_001_eval_3B_d025_s123_aligned,\n    #   exp_001_eval_3B_d100_v2_s123_aligned, exp_001_eval_3B_d000_v2_s123_aligned\n    # Eval (para_aligned): exp_001_eval_05B_d005_para_aligned, exp_001_eval_05B_d025_aligned_v2,\n    #   exp_001_eval_05B_d005_s123_para_aligned, exp_001_eval_15B_d025_para_aligned,\n    #   exp_001_eval_3B_d000_s42_para_aligned, exp_001_eval_3B_d100_s42_para_aligned,\n    #   exp_001_eval_3B_d000_v2_para_aligned, exp_001_eval_3B_d000_v2_para_aligned_v2,\n    #   exp_001_eval_3B_d025_v2_para_aligned, exp_001_eval_3B_d100_v2_para_aligned,\n    #   exp_001_eval_3B_d005_s123_para_aligned, exp_001_eval_3B_d025_s123_para_aligned,\n    #   exp_001_eval_3B_d100_s123_para_aligned_v2, exp_001_eval_3B_d000_v2_s123_para_aligned\n    # Excluded from IRT pool: d000_s42 and d005_s42 experiments (lr=2e-4 confound, D076)\n\n  - id: exp-002\n    name: stage1_signal_pipeline\n    claim: 2\n    description: >\n      Compute 4 detection signals on all contaminated + clean models from exp-001:\n      (a) embedding-based semantic retrieval (FAISS + sentence-transformers),\n      (b) Min-K%++ membership inference,\n      (c) ConStat performance gap (original vs paraphrased items),\n      (d) Self-Critique entropy collapse.\n      Output: per-model-item exposure scores for each signal.\n    priority: P0\n    gpu_budget_hours: 20\n    deps: [exp-001]\n    registry_id: exp_002_signals_05B\n    # Related: exp002-signals-1p5B (DONE/success), exp002-signal-d025-05B (DONE/success)\n    # Note: 3B signal runs (exp_002_signals_3B v1-v4) all failed/killed\n\n  - id: exp-003\n    name: rrf_aggregation_ablation\n    claim: 2\n    description: >\n      RRF fusion of 4 signals into composite per-item exposure score.\n      Ablations: (a) RRF vs equal-weight rank averaging, (b) single-signal only\n      (×4), (c) calibration-based weighted RRF variant, (d) false positive\n      injection robustness check (inject FP at rates matching Duan et al. 2024).\n      Also test degraded 2-signal mode (ConStat + Self-Critique) for closed-weight.\n    priority: P0\n    gpu_budget_hours: 2\n    deps: [exp-002]\n    registry_id: exp_003_rrf_05B\n    # Related: exp_003_mmlu_item_aligned_gap (DONE/success)\n\n  - id: exp-004\n    name: simulation_identifiability_sweep\n    claim: 1\n    also_supports: [3]\n    description: >\n      Systematic synthetic-data sweep (NEW, not MVP — MVP only covered 4-5 conditions):\n      exposure signal AUC (0.55, 0.60, 0.65, 0.70, 0.80, 0.90) ×\n      model count (20, 50, 100, 200) ×\n      prior strength (N(0,0.5), N(0,1), N(0,2)) ×\n      exposure type (binary, continuous).\n      144 conditions, 10 seeds each. Reports: θ-γ recovery RMSE, posterior\n      correlation, coverage (50%/80%/95%), prior sensitivity. Establishes\n      minimum AUC threshold; if 95% CI width > 15pp at AUC=0.65, label as\n      \"cannot distinguish no contamination from moderate contamination.\"\n      N_items=300 fixed (per MVP finding).\n      Subsumes exp-010 (prior sensitivity) and exp-011 (few-examinee regime)\n      — prior × N_models dimensions already in sweep grid. Growing Pains\n      pre-estimation sub-experiment: at N_models=20/50, compare flat prior\n      vs informative prior from pre-estimated item parameters.\n      Also includes Fisher Information matrix analysis: derive approximate\n      analytical relationship between signal AUC, N_models, and γ\n      recoverability. Distinguish structural identifiability (parameters\n      uniquely determined) from practical identifiability (estimation\n      quality sufficient for decisions). Provides theoretical grounding\n      for the empirical AUC ≥ 0.70 threshold.\n    priority: P0\n    gpu_budget_hours: 0\n    deps: []\n    note: CPU only. MVP (mvp_sim_4pl_gamma) was preliminary; this is the full sweep.\n    registry_id: exp_004_sim_sweep\n    # Related: mvp_sim_4pl_gamma (DONE/success), mvp_sim_confounding (DONE/success),\n    #   exp_004_sim_sweep_extreme_gamma (DONE/success)\n    # Note: full sweep v1-v6 all failed (tmpfs/timeout issues); MVP + extreme_gamma succeeded\n\n  - id: exp-005\n    name: noise_propagation_analysis\n    claim: 3\n    description: >\n      Two parts:\n      (A) Measurement error model (PRIMARY): extend Stan model to treat exposure\n      as noisy observation: exposure_ij ~ N(τ_ij, σ_e²), where τ is latent true\n      contamination. σ_e estimated from exp-001 ground truth FP/FN rates.\n      This propagates Stage 1 uncertainty into posteriors automatically.\n      Compare coverage (50%/80%/95%) vs point-estimate exposure baseline.\n      (B) Post-hoc noise injection: inject Gaussian noise at 1×/1.5×/2× matched\n      levels, re-fit standard model, measure CI widening for γ and θ.\n      Both parts inform whether measurement error model closes the coverage gap.\n    priority: P0\n    gpu_budget_hours: 0\n    deps: [exp-002, exp-004]\n    note: CPU only\n    registry_id: exp_005_noise_prop_v2\n    # Related: exp_005_noise_prop (v1, DONE/failed — sigma_e=0 bug),\n    #   exp_005_noise_prop_v3 (DONE/failed), exp_005_noise_prop_v4 (DONE/negative)\n    # Note: all versions failed or negative; v4 completed but results negative\n\n  - id: exp-006\n    name: irt_calibration_and_baselines\n    claim: 1\n    also_supports: [3]\n    description: >\n      Fit 4PL+γ IRT (Stan NUTS) on controlled models from exp-001/003.\n      PRIMARY: per-benchmark fitting with benchmark-specific γ_k — this is\n      the natural parameterization when IRT is fitted per-benchmark (each\n      benchmark's model has its own γ_k). ABLATION: joint fitting across\n      benchmarks with shared global γ (stronger assumption, tests whether\n      contamination effect is homogeneous across benchmarks). Report both.\n      Per-benchmark fitting (not joint) is the default to reduce local\n      independence violation scope. Posterior predictive checks on item-level residual\n      correlations to assess local independence empirically.\n      Compute calibrated scores via exposure=0 counterfactual with CIs.\n      Compare against 7 baselines:\n      (0) Raw — no adjustment (anchor),\n      (1) remove-and-rescore (drop flagged items),\n      (2) single-signal 2PL+γ (best signal only, simpler IRT),\n      (3) vanilla 4PL without γ (standard IRT, no contamination modeling),\n      (4) linear exposure regression + bootstrap CI (simplest post-hoc),\n      (5) Emperor's mitigation: rephrasing + option shuffling,\n      (6) DCR fuzzy inference (EMNLP 2025) — the only existing method\n          producing adjusted accuracy; must include or reviewers will reject.\n      Evaluate all 5 metrics: MAE, coverage (50%/80%/95%), sharpness,\n      Kendall τ, dose-response monotonicity.\n      Report mean ± std across 3 seeds (matched to exp-001 seeds).\n    priority: P0\n    gpu_budget_hours: 8\n    deps: [exp-003]\n    benchmarks: [MMLU, GSM8K, ARC-Challenge, HumanEval]\n    seeds: 3\n    registry_id: exp_006_irt_05B_gsm8k\n    # Related: exp_006_irt_05B_arc (DONE/success), exp006-s1only-gsm8k-2pl (DONE/success),\n    #   exp006-oracle-arc-2pl (DONE/success), exp006-oracle-gsm8k-extended-v2 (DONE/success),\n    #   exp006-pooled-s1only-gsm8k-v2 (DONE/success), exp006-pooled-s1only-arc (DONE/success),\n    #   exp006-pooled-05B-15B-arc-v2 (DONE/success)\n\n  # ============================================================\n  # P1: Important — run if time/GPU permit\n  # ============================================================\n\n  - id: exp-015\n    name: sft_d100_qc_only\n    claim: 1\n    description: >\n      100% dosage SFT using only QC-pass paraphrases (7547/16697 items).\n      Isolates noisy vs clean contamination confound identified by reviewer.\n      D012 decision. Compare calibration metrics against exp-001 d100 (all\n      paraphrases) to quantify effect of noisy contamination on IRT estimates.\n    priority: P1\n    gpu_budget_hours: 5\n    deps: [exp-001]\n    benchmarks: [MMLU, GSM8K, ARC-Challenge, HumanEval]\n    models: [Qwen2.5-0.5B]\n    seeds: 1\n    status: planned\n    registry_id: null\n    data_script: exp001/prepare_qc_only_data.py\n\n  - id: exp-007\n    name: scale_bridging_7b\n    claim: 1\n    description: >\n      Qwen2.5-7B controlled SFT injection at 5 dosage levels.\n      Validates calibration accuracy scales to larger models.\n      Requires multi-GPU node (7B LoRA SFT ~4-8h per run on 1×H100).\n    priority: P1\n    gpu_budget_hours: 30\n    deps: [exp-001]\n\n  - id: exp-008\n    name: signal_survival_analysis\n    claim: 2\n    description: >\n      Systematic evaluation of detection signal reliability across training regimes.\n      Signal × regime AUC heatmap: 4 signals × {base, SFT-clean, SFT-contaminated,\n      RL-post-trained}. Confirms Self-Critique compensates where Min-K%++/ConStat\n      degrade post-RL (per fragility paper arXiv 2510.02386).\n      ELEVATED to Core Contribution 2 per Dream review (all 3 tiers identified\n      this as the most genuinely novel finding).\n    priority: P0\n    gpu_budget_hours: 10\n    deps: [exp-002]\n    registry_id: exp_008_signal_survival_v4\n    # Related: exp_008_signal_survival (DONE/success), exp_008_base_pretrained_eval_v2 (DONE/success),\n    #   exp_008_base_pretrained_15B_eval_v2 (DONE/success), exp_008_instruct_05B_eval (DONE/success)\n\n  - id: exp-014\n    name: multi_family_validation\n    claim: 1\n    description: >\n      Controlled SFT injection on at least one non-Qwen model family\n      (Llama-3.2-1B or Pythia-1.4B) at 3 dosage levels (0%, 25%, 100%).\n      Validates that identifiability boundaries and calibration accuracy\n      generalize beyond Qwen2.5. Addresses Dream reviewer concern about\n      single model family limiting generalizability (flagged [M][W]).\n    priority: P1\n    gpu_budget_hours: 15\n    deps: [exp-001]\n\n  - id: exp-009\n    name: rl_observational_case_study\n    claim: 2\n    also_supports: [3]\n    description: >\n      Apply Self-Critique + available signals to existing RL-trained models:\n      Qwen2.5-Instruct (0.5B/1.5B/3B/7B), DeepSeek-R1-Distill-1.5B/7B.\n      Fit IRT with appropriately wider CIs. Expected regret quantification:\n      compare uncalibrated vs calibrated vs remove-rescore for top-5 model\n      selection. Framed as observational — directional external validity,\n      not full quantitative validation. Near-zero γ check on known-clean\n      benchmark (specificity test).\n    priority: P1\n    gpu_budget_hours: 15\n    deps: [exp-006, exp-008]\n\n  # exp-010 (prior_sensitivity) and exp-011 (few_examinee_regime) merged into exp-004.\n  # Prior × N_models dimensions already covered in the sweep grid.\n\n  # ============================================================\n  # P2: Bonus — adds breadth if resources allow\n  # ============================================================\n\n  - id: exp-012\n    name: observational_72b\n    claim: 1\n    description: >\n      Qwen2.5-72B observational analysis (inference only, no SFT).\n      Extends ecological validity to frontier model scale.\n    priority: P2\n    gpu_budget_hours: 15\n    deps: [exp-006]\n\n  - id: exp-013\n    name: closed_weight_2signal_mode\n    claim: 2\n    description: >\n      Degraded 2-signal mode (ConStat + Self-Critique, no logits/embeddings)\n      for closed-weight models. Ablation quantifying 2-signal vs 4-signal\n      calibration accuracy gap.\n    priority: P2\n    gpu_budget_hours: 5\n    deps: [exp-003]\n\n# ============================================================\n# GPU Budget Summary\n# ============================================================\ngpu_budget:\n  P0_hours: 90\n  P1_hours: 60\n  P2_hours: 20\n  buffer_hours: 30\n  total_hours: 200\n  note: >\n    CPU-only experiments (exp-004, exp-005, exp-011) excluded.\n    Buffer covers reruns, debugging, multi-seed overhead, and unexpected issues.\n    Requires 2-4× H100/A100-80G for parallel SFT runs.\n    EMNLP 2026 ARR May 25 sprint (12 days from May 13):\n    - With 4× H100: P0 in ~4 days, P1 in ~3 days, total ~8 days (fits deadline)\n    - With 2× H100: P0 in ~7 days, P1 in ~4 days, tight but feasible if parallelized\n    - Day-8 contingency: reduce benchmarks to MMLU + GSM8K if behind schedule\n\n# Multi-seed protocol:\n# - exp-001, exp-006: 3 seeds, report mean ± std for key metrics\n# - exp-004, exp-005, exp-011: 10 seeds (simulation, CPU)\n# - exp-007, exp-008, exp-009: 1 seed (resource-constrained, note as limitation if needed)\n",
      "numLines": 319,
      "startLine": 1,
      "totalLines": 319
    }
  }
}
```

</details>

---


### Tool call

_source line 135_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__compute_coverage_matrix · `toolu_01LybxxnRoUsZnQxSDNNxfth`</summary>

```json
{
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d61fa97d-0b3f-42cc-a383-d75fd89e4948",
  "uuid": "08fee079-e1fb-4981-a2e5-5d2784c0ba71",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GRkDTbwWmggkfToS5ejR1f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1829,
      "cache_read_input_tokens": 76912,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1829
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

_source line 136 · 2026-05-15T20:14:58.692Z_

<details><summary>↩ Tool result · `toolu_01LybxxnRoUsZnQxSDNNxfth`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"claims\": [1, 2, 3], \"matrix\": {\"1\": {\"experiments\": [{\"id\": \"exp-001\", \"name\": \"controlled_sft_injection\", \"claim\": 1, \"description\": \"SFT contamination injection on Qwen2.5-0.5B/1.5B/3B at 5 dosage levels (0%, 5%, 25%, 50%, 100% benchmark items as paraphrases in SFT data). Produces ground-truth contaminated/clean model pairs. 15 SFT runs total (3 models × 5 dosages), parallelized across GPUs. 3 seeds per condition for key metrics (mean ± std). Paraphrase generation: use strong open LLM (Qwen2.5-72B-Instruct or equivalent) with controlled semantic similarity — following methodology of \\\"Rethinking Benchmark and Contamination\\\" (arXiv 2023). Target: high semantic similarity (cosine >0.85) but low lexical overlap (BLEU <0.3) to evade n-gram decontamination while preserving contamination effect. Quality validation: automated similarity metrics + human spot-check on 50 random pairs per benchmark.\\n\", \"priority\": \"P0\", \"gpu_budget_hours\": 50, \"deps\": [], \"benchmarks\": [\"MMLU\", \"GSM8K\", \"ARC-Challenge\", \"HumanEval\"], \"models\": [\"Qwen2.5-0.5B\", \"Qwen2.5-1.5B\", \"Qwen2.5-3B\"], \"seeds\": 3, \"registry_id\": \"exp_001_sft_injection\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"arc_qc_pass\": 697, \"arc_qc_rate\": 0.595, \"arc_total\": 1172, \"gsm8k_qc_pass\": 228, \"gsm8k_qc_rate\": 0.173, \"gsm8k_total\": 1319, \"humaneval_total\": 164, \"mmlu_qc_pass\": 6596, \"mmlu_qc_rate\": 0.47, \"mmlu_total\": 14042}}, {\"id\": \"exp-004\", \"name\": \"simulation_identifiability_sweep\", \"claim\": 1, \"also_supports\": [3], \"description\": \"Systematic synthetic-data sweep (NEW, not MVP — MVP only covered 4-5 conditions): exposure signal AUC (0.55, 0.60, 0.65, 0.70, 0.80, 0.90) × model count (20, 50, 100, 200) × prior strength (N(0,0.5), N(0,1), N(0,2)) × exposure type (binary, continuous). 144 conditions, 10 seeds each. Reports: θ-γ recovery RMSE, posterior correlation, coverage (50%/80%/95%), prior sensitivity. Establishes minimum AUC threshold; if 95% CI width > 15pp at AUC=0.65, label as \\\"cannot distinguish no contamination from moderate contamination.\\\" N_items=300 fixed (per MVP finding). Subsumes exp-010 (prior sensitivity) and exp-011 (few-examinee regime) — prior × N_models dimensions already in sweep grid. Growing Pains pre-estimation sub-experiment: at N_models=20/50, compare flat prior vs informative prior from pre-estimated item parameters. Also includes Fisher Information matrix analysis: derive approximate analytical relationship between signal AUC, N_models, and γ recoverability. Distinguish structural identifiability (parameters uniquely determined) from practical identifiability (estimation quality sufficient for decisions). Provides theoretical grounding for the empirical AUC ≥ 0.70 threshold.\\n\", \"priority\": \"P0\", \"gpu_budget_hours\": 0, \"deps\": [], \"note\": \"CPU only. MVP (mvp_sim_4pl_gamma) was preliminary; this is the full sweep.\", \"registry_id\": \"exp_004_sim_sweep\", \"status\": \"DONE\", \"conclusion\": \"failed\"}, {\"id\": \"exp-006\", \"name\": \"irt_calibration_and_baselines\", \"claim\": 1, \"also_supports\": [3], \"description\": \"Fit 4PL+γ IRT (Stan NUTS) on controlled models from exp-001/003. PRIMARY: per-benchmark fitting with benchmark-specific γ_k — this is the natural parameterization when IRT is fitted per-benchmark (each benchmark's model has its own γ_k). ABLATION: joint fitting across benchmarks with shared global γ (stronger assumption, tests whether contamination effect is homogeneous across benchmarks). Report both. Per-benchmark fitting (not joint) is the default to reduce local independence violation scope. Posterior predictive checks on item-level residual correlations to assess local independence empirically. Compute calibrated scores via exposure=0 counterfactual with CIs. Compare against 7 baselines: (0) Raw — no adjustment (anchor), (1) remove-and-rescore (drop flagged items), (2) single-signal 2PL+γ (best signal only, simpler IRT), (3) vanilla 4PL without γ (standard IRT, no contamination modeling), (4) linear exposure regression + bootstrap CI (simplest post-hoc), (5) Emperor's mitigation: rephrasing + option shuffling, (6) DCR fuzzy inference (EMNLP 2025) — the only existing method\\n    producing adjusted accuracy; must include or reviewers will reject.\\nEvaluate all 5 metrics: MAE, coverage (50%/80%/95%), sharpness, Kendall τ, dose-response monotonicity. Report mean ± std across 3 seeds (matched to exp-001 seeds).\\n\", \"priority\": \"P0\", \"gpu_budget_hours\": 8, \"deps\": [\"exp-003\"], \"benchmarks\": [\"MMLU\", \"GSM8K\", \"ARC-Challenge\", \"HumanEval\"], \"seeds\": 3, \"registry_id\": \"exp_006_irt_05B_gsm8k\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"joint_gamma\": 0.3463, \"joint_gamma_ci\": [-0.65, 1.4], \"joint_rhat\": 1.0081, \"joint_ess\": 956.4, \"joint_divergences\": 0, \"perbench_gamma\": 0.508, \"perbench_gamma_ci\": [-0.64, 1.84], \"perbench_rhat\": 1.0096, \"perbench_ess\": 522.2, \"perbench_divergences\": 0, \"delta_fix_applied\": true, \"signal_scores_after_delta\": [0, 0.016, 0.065, 0.197], \"baselines_mae\": {\"B0_raw\": 0.0034, \"B4_linear_regression\": 0.003, \"B3_vanilla_4pl\": 0.0123, \"IRT_4pl_gamma\": 0.0195, \"B6_dcr_fuzzy\": 0.2634, \"B2_2pl_gamma\": 0.3202}}}, {\"id\": \"exp-015\", \"name\": \"sft_d100_qc_only\", \"claim\": 1, \"description\": \"100% dosage SFT using only QC-pass paraphrases (7547/16697 items). Isolates noisy vs clean contamination confound identified by reviewer. D012 decision. Compare calibration metrics against exp-001 d100 (all paraphrases) to quantify effect of noisy contamination on IRT estimates.\\n\", \"priority\": \"P1\", \"gpu_budget_hours\": 5, \"deps\": [\"exp-001\"], \"benchmarks\": [\"MMLU\", \"GSM8K\", \"ARC-Challenge\", \"HumanEval\"], \"models\": [\"Qwen2.5-0.5B\"], \"seeds\": 1, \"status\": \"planned\", \"registry_id\": null, \"data_script\": \"exp001/prepare_qc_only_data.py\"}, {\"id\": \"exp-007\", \"name\": \"scale_bridging_7b\", \"claim\": 1, \"description\": \"Qwen2.5-7B controlled SFT injection at 5 dosage levels. Validates calibration accuracy scales to larger models. Requires multi-GPU node (7B LoRA SFT ~4-8h per run on 1×H100).\\n\", \"priority\": \"P1\", \"gpu_budget_hours\": 30, \"deps\": [\"exp-001\"], \"status\": \"planned\"}, {\"id\": \"exp-014\", \"name\": \"multi_family_validation\", \"claim\": 1, \"description\": \"Controlled SFT injection on at least one non-Qwen model family (Llama-3.2-1B or Pythia-1.4B) at 3 dosage levels (0%, 25%, 100%). Validates that identifiability boundaries and calibration accuracy generalize beyond Qwen2.5. Addresses Dream reviewer concern about single model family limiting generalizability (flagged [M][W]).\\n\", \"priority\": \"P1\", \"gpu_budget_hours\": 15, \"deps\": [\"exp-001\"], \"status\": \"planned\"}, {\"id\": \"exp-012\", \"name\": \"observational_72b\", \"claim\": 1, \"description\": \"Qwen2.5-72B observational analysis (inference only, no SFT). Extends ecological validity to frontier model scale.\\n\", \"priority\": \"P2\", \"gpu_budget_hours\": 15, \"deps\": [\"exp-006\"], \"status\": \"planned\"}], \"counts\": {\"planned\": 4, \"running\": 0, \"done\": 2, \"failed\": 1, \"orphaned\": 0}, \"total\": 7, \"coverage\": \"2/7\", \"coverage_pct\": 28.6}, \"2\": {\"experiments\": [{\"id\": \"exp-002\", \"name\": \"stage1_signal_pipeline\", \"claim\": 2, \"description\": \"Compute 4 detection signals on all contaminated + clean models from exp-001: (a) embedding-based semantic retrieval (FAISS + sentence-transformers), (b) Min-K%++ membership inference, (c) ConStat performance gap (original vs paraphrased items), (d) Self-Critique entropy collapse. Output: per-model-item exposure scores for each signal.\\n\", \"priority\": \"P0\", \"gpu_budget_hours\": 20, \"deps\": [\"exp-001\"], \"registry_id\": \"exp_002_signals_05B\", \"status\": \"DONE\", \"conclusion\": \"success\"}, {\"id\": \"exp-003\", \"name\": \"rrf_aggregation_ablation\", \"claim\": 2, \"description\": \"RRF fusion of 4 signals into composite per-item exposure score. Ablations: (a) RRF vs equal-weight rank averaging, (b) single-signal only (×4), (c) calibration-based weighted RRF variant, (d) false positive injection robustness check (inject FP at rates matching Duan et al. 2024). Also test degraded 2-signal mode (ConStat + Self-Critique) for closed-weight.\\n\", \"priority\": \"P0\", \"gpu_budget_hours\": 2, \"deps\": [\"exp-002\"], \"registry_id\": \"exp_003_rrf_05B\", \"status\": \"DONE\", \"conclusion\": \"success\"}, {\"id\": \"exp-008\", \"name\": \"signal_survival_analysis\", \"claim\": 2, \"description\": \"Systematic evaluation of detection signal reliability across training regimes. Signal × regime AUC heatmap: 4 signals × {base, SFT-clean, SFT-contaminated, RL-post-trained}. Confirms Self-Critique compensates where Min-K%++/ConStat degrade post-RL (per fragility paper arXiv 2510.02386). ELEVATED to Core Contribution 2 per Dream review (all 3 tiers identified this as the most genuinely novel finding).\\n\", \"priority\": \"P0\", \"gpu_budget_hours\": 10, \"deps\": [\"exp-002\"], \"registry_id\": \"exp_008_signal_survival_v4\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"S1_d005_auc_mean\": 0.979, \"S2_d005_auc_mean\": 0.465, \"S4_d005_auc_mean\": 0.481, \"S1_d100_cross_cohens_d_mean\": 3.6, \"S2_d100_cross_cohens_d_mean\": -1.98, \"S4_d100_cross_cohens_d_mean\": 0.45, \"effective_signals_at_05B\": 1, \"d021_fix\": \"within-model AUC only for d005; d100 uses cross-model Cohen's d\"}}, {\"id\": \"exp-009\", \"name\": \"rl_observational_case_study\", \"claim\": 2, \"also_supports\": [3], \"description\": \"Apply Self-Critique + available signals to existing RL-trained models: Qwen2.5-Instruct (0.5B/1.5B/3B/7B), DeepSeek-R1-Distill-1.5B/7B. Fit IRT with appropriately wider CIs. Expected regret quantification: compare uncalibrated vs calibrated vs remove-rescore for top-5 model selection. Framed as observational — directional external validity, not full quantitative validation. Near-zero γ check on known-clean benchmark (specificity test).\\n\", \"priority\": \"P1\", \"gpu_budget_hours\": 15, \"deps\": [\"exp-006\", \"exp-008\"], \"status\": \"planned\"}, {\"id\": \"exp-013\", \"name\": \"closed_weight_2signal_mode\", \"claim\": 2, \"description\": \"Degraded 2-signal mode (ConStat + Self-Critique, no logits/embeddings) for closed-weight models. Ablation quantifying 2-signal vs 4-signal calibration accuracy gap.\\n\", \"priority\": \"P2\", \"gpu_budget_hours\": 5, \"deps\": [\"exp-003\"], \"status\": \"planned\"}], \"counts\": {\"planned\": 2, \"running\": 0, \"done\": 3, \"failed\": 0, \"orphaned\": 0}, \"total\": 5, \"coverage\": \"3/5\", \"coverage_pct\": 60.0}, \"3\": {\"experiments\": [{\"id\": \"exp-005\", \"name\": \"noise_propagation_analysis\", \"claim\": 3, \"description\": \"Two parts: (A) Measurement error model (PRIMARY): extend Stan model to treat exposure as noisy observation: exposure_ij ~ N(τ_ij, σ_e²), where τ is latent true contamination. σ_e estimated from exp-001 ground truth FP/FN rates. This propagates Stage 1 uncertainty into posteriors automatically. Compare coverage (50%/80%/95%) vs point-estimate exposure baseline. (B) Post-hoc noise injection: inject Gaussian noise at 1×/1.5×/2× matched levels, re-fit standard model, measure CI widening for γ and θ. Both parts inform whether measurement error model closes the coverage gap.\\n\", \"priority\": \"P0\", \"gpu_budget_hours\": 0, \"deps\": [\"exp-002\", \"exp-004\"], \"note\": \"CPU only\", \"registry_id\": \"exp_005_noise_prop_v2\", \"status\": \"DONE\", \"conclusion\": \"failed\"}], \"counts\": {\"planned\": 0, \"running\": 0, \"done\": 0, \"failed\": 1, \"orphaned\": 0}, \"total\": 1, \"coverage\": \"0/1\", \"coverage_pct\": 0.0}}, \"unassigned\": [], \"summary\": {\"total_experiments\": 13, \"total_claims\": 3, \"counts\": {\"planned\": 6, \"running\": 0, \"done\": 5, \"failed\": 2, \"orphaned\": 0}, \"coverage\": \"5/13\", \"coverage_pct\": 38.5, \"unassigned\": 0}}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d61fa97d-0b3f-42cc-a383-d75fd89e4948",
  "uuid": "8e82dc69-7210-4854-85e3-b3deaaf55108",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"claims\\\": [1, 2, 3], \\\"matrix\\\": {\\\"1\\\": {\\\"experiments\\\": [{\\\"id\\\": \\\"exp-001\\\", \\\"name\\\": \\\"controlled_sft_injection\\\", \\\"claim\\\": 1, \\\"description\\\": \\\"SFT contamination injection on Qwen2.5-0.5B/1.5B/3B at 5 dosage levels (0%, 5%, 25%, 50%, 100% benchmark items as paraphrases in SFT data). Produces ground-truth contaminated/clean model pairs. 15 SFT runs total (3 models × 5 dosages), parallelized across GPUs. 3 seeds per condition for key metrics (mean ± std). Paraphrase generation: use strong open LLM (Qwen2.5-72B-Instruct or equivalent) with controlled semantic similarity — following methodology of \\\\\\\"Rethinking Benchmark and Contamination\\\\\\\" (arXiv 2023). Target: high semantic similarity (cosine >0.85) but low lexical overlap (BLEU <0.3) to evade n-gram decontamination while preserving contamination effect. Quality validation: automated similarity metrics + human spot-check on 50 random pairs per benchmark.\\\\n\\\", \\\"priority\\\": \\\"P0\\\", \\\"gpu_budget_hours\\\": 50, \\\"deps\\\": [], \\\"benchmarks\\\": [\\\"MMLU\\\", \\\"GSM8K\\\", \\\"ARC-Challenge\\\", \\\"HumanEval\\\"], \\\"models\\\": [\\\"Qwen2.5-0.5B\\\", \\\"Qwen2.5-1.5B\\\", \\\"Qwen2.5-3B\\\"], \\\"seeds\\\": 3, \\\"registry_id\\\": \\\"exp_001_sft_injection\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"arc_qc_pass\\\": 697, \\\"arc_qc_rate\\\": 0.595, \\\"arc_total\\\": 1172, \\\"gsm8k_qc_pass\\\": 228, \\\"gsm8k_qc_rate\\\": 0.173, \\\"gsm8k_total\\\": 1319, \\\"humaneval_total\\\": 164, \\\"mmlu_qc_pass\\\": 6596, \\\"mmlu_qc_rate\\\": 0.47, \\\"mmlu_total\\\": 14042}}, {\\\"id\\\": \\\"exp-004\\\", \\\"name\\\": \\\"simulation_identifiability_sweep\\\", \\\"claim\\\": 1, \\\"also_supports\\\": [3], \\\"description\\\": \\\"Systematic synthetic-data sweep (NEW, not MVP — MVP only covered 4-5 conditions): exposure signal AUC (0.55, 0.60, 0.65, 0.70, 0.80, 0.90) × model count (20, 50, 100, 200) × prior strength (N(0,0.5), N(0,1), N(0,2)) × exposure type (binary, continuous). 144 conditions, 10 seeds each. Reports: θ-γ recovery RMSE, posterior correlation, coverage (50%/80%/95%), prior sensitivity. Establishes minimum AUC threshold; if 95% CI width > 15pp at AUC=0.65, label as \\\\\\\"cannot distinguish no contamination from moderate contamination.\\\\\\\" N_items=300 fixed (per MVP finding). Subsumes exp-010 (prior sensitivity) and exp-011 (few-examinee regime) — prior × N_models dimensions already in sweep grid. Growing Pains pre-estimation sub-experiment: at N_models=20/50, compare flat prior vs informative prior from pre-estimated item parameters. Also includes Fisher Information matrix analysis: derive approximate analytical relationship between signal AUC, N_models, and γ recoverability. Distinguish structural identifiability (parameters uniquely determined) from practical identifiability (estimation quality sufficient for decisions). Provides theoretical grounding for the empirical AUC ≥ 0.70 threshold.\\\\n\\\", \\\"priority\\\": \\\"P0\\\", \\\"gpu_budget_hours\\\": 0, \\\"deps\\\": [], \\\"note\\\": \\\"CPU only. MVP (mvp_sim_4pl_gamma) was preliminary; this is the full sweep.\\\", \\\"registry_id\\\": \\\"exp_004_sim_sweep\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, {\\\"id\\\": \\\"exp-006\\\", \\\"name\\\": \\\"irt_calibration_and_baselines\\\", \\\"claim\\\": 1, \\\"also_supports\\\": [3], \\\"description\\\": \\\"Fit 4PL+γ IRT (Stan NUTS) on controlled models from exp-001/003. PRIMARY: per-benchmark fitting with benchmark-specific γ_k — this is the natural parameterization when IRT is fitted per-benchmark (each benchmark's model has its own γ_k). ABLATION: joint fitting across benchmarks with shared global γ (stronger assumption, tests whether contamination effect is homogeneous across benchmarks). Report both. Per-benchmark fitting (not joint) is the default to reduce local independence violation scope. Posterior predictive checks on item-level residual correlations to assess local independence empirically. Compute calibrated scores via exposure=0 counterfactual with CIs. Compare against 7 baselines: (0) Raw — no adjustment (anchor), (1) remove-and-rescore (drop flagged items), (2) single-signal 2PL+γ (best signal only, simpler IRT), (3) vanilla 4PL without γ (standard IRT, no contamination modeling), (4) linear exposure regression + bootstrap CI (simplest post-hoc), (5) Emperor's mitigation: rephrasing + option shuffling, (6) DCR fuzzy inference (EMNLP 2025) — the only existing method\\\\n    producing adjusted accuracy; must include or reviewers will reject.\\\\nEvaluate all 5 metrics: MAE, coverage (50%/80%/95%), sharpness, Kendall τ, dose-response monotonicity. Report mean ± std across 3 seeds (matched to exp-001 seeds).\\\\n\\\", \\\"priority\\\": \\\"P0\\\", \\\"gpu_budget_hours\\\": 8, \\\"deps\\\": [\\\"exp-003\\\"], \\\"benchmarks\\\": [\\\"MMLU\\\", \\\"GSM8K\\\", \\\"ARC-Challenge\\\", \\\"HumanEval\\\"], \\\"seeds\\\": 3, \\\"registry_id\\\": \\\"exp_006_irt_05B_gsm8k\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"joint_gamma\\\": 0.3463, \\\"joint_gamma_ci\\\": [-0.65, 1.4], \\\"joint_rhat\\\": 1.0081, \\\"joint_ess\\\": 956.4, \\\"joint_divergences\\\": 0, \\\"perbench_gamma\\\": 0.508, \\\"perbench_gamma_ci\\\": [-0.64, 1.84], \\\"perbench_rhat\\\": 1.0096, \\\"perbench_ess\\\": 522.2, \\\"perbench_divergences\\\": 0, \\\"delta_fix_applied\\\": true, \\\"signal_scores_after_delta\\\": [0, 0.016, 0.065, 0.197], \\\"baselines_mae\\\": {\\\"B0_raw\\\": 0.0034, \\\"B4_linear_regression\\\": 0.003, \\\"B3_vanilla_4pl\\\": 0.0123, \\\"IRT_4pl_gamma\\\": 0.0195, \\\"B6_dcr_fuzzy\\\": 0.2634, \\\"B2_2pl_gamma\\\": 0.3202}}}, {\\\"id\\\": \\\"exp-015\\\", \\\"name\\\": \\\"sft_d100_qc_only\\\", \\\"claim\\\": 1, \\\"description\\\": \\\"100% dosage SFT using only QC-pass paraphrases (7547/16697 items). Isolates noisy vs clean contamination confound identified by reviewer. D012 decision. Compare calibration metrics against exp-001 d100 (all paraphrases) to quantify effect of noisy contamination on IRT estimates.\\\\n\\\", \\\"priority\\\": \\\"P1\\\", \\\"gpu_budget_hours\\\": 5, \\\"deps\\\": [\\\"exp-001\\\"], \\\"benchmarks\\\": [\\\"MMLU\\\", \\\"GSM8K\\\", \\\"ARC-Challenge\\\", \\\"HumanEval\\\"], \\\"models\\\": [\\\"Qwen2.5-0.5B\\\"], \\\"seeds\\\": 1, \\\"status\\\": \\\"planned\\\", \\\"registry_id\\\": null, \\\"data_script\\\": \\\"exp001/prepare_qc_only_data.py\\\"}, {\\\"id\\\": \\\"exp-007\\\", \\\"name\\\": \\\"scale_bridging_7b\\\", \\\"claim\\\": 1, \\\"description\\\": \\\"Qwen2.5-7B controlled SFT injection at 5 dosage levels. Validates calibration accuracy scales to larger models. Requires multi-GPU node (7B LoRA SFT ~4-8h per run on 1×H100).\\\\n\\\", \\\"priority\\\": \\\"P1\\\", \\\"gpu_budget_hours\\\": 30, \\\"deps\\\": [\\\"exp-001\\\"], \\\"status\\\": \\\"planned\\\"}, {\\\"id\\\": \\\"exp-014\\\", \\\"name\\\": \\\"multi_family_validation\\\", \\\"claim\\\": 1, \\\"description\\\": \\\"Controlled SFT injection on at least one non-Qwen model family (Llama-3.2-1B or Pythia-1.4B) at 3 dosage levels (0%, 25%, 100%). Validates that identifiability boundaries and calibration accuracy generalize beyond Qwen2.5. Addresses Dream reviewer concern about single model family limiting generalizability (flagged [M][W]).\\\\n\\\", \\\"priority\\\": \\\"P1\\\", \\\"gpu_budget_hours\\\": 15, \\\"deps\\\": [\\\"exp-001\\\"], \\\"status\\\": \\\"planned\\\"}, {\\\"id\\\": \\\"exp-012\\\", \\\"name\\\": \\\"observational_72b\\\", \\\"claim\\\": 1, \\\"description\\\": \\\"Qwen2.5-72B observational analysis (inference only, no SFT). Extends ecological validity to frontier model scale.\\\\n\\\", \\\"priority\\\": \\\"P2\\\", \\\"gpu_budget_hours\\\": 15, \\\"deps\\\": [\\\"exp-006\\\"], \\\"status\\\": \\\"planned\\\"}], \\\"counts\\\": {\\\"planned\\\": 4, \\\"running\\\": 0, \\\"done\\\": 2, \\\"failed\\\": 1, \\\"orphaned\\\": 0}, \\\"total\\\": 7, \\\"coverage\\\": \\\"2/7\\\", \\\"coverage_pct\\\": 28.6}, \\\"2\\\": {\\\"experiments\\\": [{\\\"id\\\": \\\"exp-002\\\", \\\"name\\\": \\\"stage1_signal_pipeline\\\", \\\"claim\\\": 2, \\\"description\\\": \\\"Compute 4 detection signals on all contaminated + clean models from exp-001: (a) embedding-based semantic retrieval (FAISS + sentence-transformers), (b) Min-K%++ membership inference, (c) ConStat performance gap (original vs paraphrased items), (d) Self-Critique entropy collapse. Output: per-model-item exposure scores for each signal.\\\\n\\\", \\\"priority\\\": \\\"P0\\\", \\\"gpu_budget_hours\\\": 20, \\\"deps\\\": [\\\"exp-001\\\"], \\\"registry_id\\\": \\\"exp_002_signals_05B\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, {\\\"id\\\": \\\"exp-003\\\", \\\"name\\\": \\\"rrf_aggregation_ablation\\\", \\\"claim\\\": 2, \\\"description\\\": \\\"RRF fusion of 4 signals into composite per-item exposure score. Ablations: (a) RRF vs equal-weight rank averaging, (b) single-signal only (×4), (c) calibration-based weighted RRF variant, (d) false positive injection robustness check (inject FP at rates matching Duan et al. 2024). Also test degraded 2-signal mode (ConStat + Self-Critique) for closed-weight.\\\\n\\\", \\\"priority\\\": \\\"P0\\\", \\\"gpu_budget_hours\\\": 2, \\\"deps\\\": [\\\"exp-002\\\"], \\\"registry_id\\\": \\\"exp_003_rrf_05B\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, {\\\"id\\\": \\\"exp-008\\\", \\\"name\\\": \\\"signal_survival_analysis\\\", \\\"claim\\\": 2, \\\"description\\\": \\\"Systematic evaluation of detection signal reliability across training regimes. Signal × regime AUC heatmap: 4 signals × {base, SFT-clean, SFT-contaminated, RL-post-trained}. Confirms Self-Critique compensates where Min-K%++/ConStat degrade post-RL (per fragility paper arXiv 2510.02386). ELEVATED to Core Contribution 2 per Dream review (all 3 tiers identified this as the most genuinely novel finding).\\\\n\\\", \\\"priority\\\": \\\"P0\\\", \\\"gpu_budget_hours\\\": 10, \\\"deps\\\": [\\\"exp-002\\\"], \\\"registry_id\\\": \\\"exp_008_signal_survival_v4\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"S1_d005_auc_mean\\\": 0.979, \\\"S2_d005_auc_mean\\\": 0.465, \\\"S4_d005_auc_mean\\\": 0.481, \\\"S1_d100_cross_cohens_d_mean\\\": 3.6, \\\"S2_d100_cross_cohens_d_mean\\\": -1.98, \\\"S4_d100_cross_cohens_d_mean\\\": 0.45, \\\"effective_signals_at_05B\\\": 1, \\\"d021_fix\\\": \\\"within-model AUC only for d005; d100 uses cross-model Cohen's d\\\"}}, {\\\"id\\\": \\\"exp-009\\\", \\\"name\\\": \\\"rl_observational_case_study\\\", \\\"claim\\\": 2, \\\"also_supports\\\": [3], \\\"description\\\": \\\"Apply Self-Critique + available signals to existing RL-trained models: Qwen2.5-Instruct (0.5B/1.5B/3B/7B), DeepSeek-R1-Distill-1.5B/7B. Fit IRT with appropriately wider CIs. Expected regret quantification: compare uncalibrated vs calibrated vs remove-rescore for top-5 model selection. Framed as observational — directional external validity, not full quantitative validation. Near-zero γ check on known-clean benchmark (specificity test).\\\\n\\\", \\\"priority\\\": \\\"P1\\\", \\\"gpu_budget_hours\\\": 15, \\\"deps\\\": [\\\"exp-006\\\", \\\"exp-008\\\"], \\\"status\\\": \\\"planned\\\"}, {\\\"id\\\": \\\"exp-013\\\", \\\"name\\\": \\\"closed_weight_2signal_mode\\\", \\\"claim\\\": 2, \\\"description\\\": \\\"Degraded 2-signal mode (ConStat + Self-Critique, no logits/embeddings) for closed-weight models. Ablation quantifying 2-signal vs 4-signal calibration accuracy gap.\\\\n\\\", \\\"priority\\\": \\\"P2\\\", \\\"gpu_budget_hours\\\": 5, \\\"deps\\\": [\\\"exp-003\\\"], \\\"status\\\": \\\"planned\\\"}], \\\"counts\\\": {\\\"planned\\\": 2, \\\"running\\\": 0, \\\"done\\\": 3, \\\"failed\\\": 0, \\\"orphaned\\\": 0}, \\\"total\\\": 5, \\\"coverage\\\": \\\"3/5\\\", \\\"coverage_pct\\\": 60.0}, \\\"3\\\": {\\\"experiments\\\": [{\\\"id\\\": \\\"exp-005\\\", \\\"name\\\": \\\"noise_propagation_analysis\\\", \\\"claim\\\": 3, \\\"description\\\": \\\"Two parts: (A) Measurement error model (PRIMARY): extend Stan model to treat exposure as noisy observation: exposure_ij ~ N(τ_ij, σ_e²), where τ is latent true contamination. σ_e estimated from exp-001 ground truth FP/FN rates. This propagates Stage 1 uncertainty into posteriors automatically. Compare coverage (50%/80%/95%) vs point-estimate exposure baseline. (B) Post-hoc noise injection: inject Gaussian noise at 1×/1.5×/2× matched levels, re-fit standard model, measure CI widening for γ and θ. Both parts inform whether measurement error model closes the coverage gap.\\\\n\\\", \\\"priority\\\": \\\"P0\\\", \\\"gpu_budget_hours\\\": 0, \\\"deps\\\": [\\\"exp-002\\\", \\\"exp-004\\\"], \\\"note\\\": \\\"CPU only\\\", \\\"registry_id\\\": \\\"exp_005_noise_prop_v2\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}], \\\"counts\\\": {\\\"planned\\\": 0, \\\"running\\\": 0, \\\"done\\\": 0, \\\"failed\\\": 1, \\\"orphaned\\\": 0}, \\\"total\\\": 1, \\\"coverage\\\": \\\"0/1\\\", \\\"coverage_pct\\\": 0.0}}, \\\"unassigned\\\": [], \\\"summary\\\": {\\\"total_experiments\\\": 13, \\\"total_claims\\\": 3, \\\"counts\\\": {\\\"planned\\\": 6, \\\"running\\\": 0, \\\"done\\\": 5, \\\"failed\\\": 2, \\\"orphaned\\\": 0}, \\\"coverage\\\": \\\"5/13\\\", \\\"coverage_pct\\\": 38.5, \\\"unassigned\\\": 0}}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"claims\": [1, 2, 3], \"matrix\": {\"1\": {\"experiments\": [{\"id\": \"exp-001\", \"name\": \"controlled_sft_injection\", \"claim\": 1, \"description\": \"SFT contamination injection on Qwen2.5-0.5B/1.5B/3B at 5 dosage levels (0%, 5%, 25%, 50%, 100% benchmark items as paraphrases in SFT data). Produces ground-truth contaminated/clean model pairs. 15 SFT runs total (3 models × 5 dosages), parallelized across GPUs. 3 seeds per condition for key metrics (mean ± std). Paraphrase generation: use strong open LLM (Qwen2.5-72B-Instruct or equivalent) with controlled semantic similarity — following methodology of \\\"Rethinking Benchmark and Contamination\\\" (arXiv 2023). Target: high semantic similarity (cosine >0.85) but low lexical overlap (BLEU <0.3) to evade n-gram decontamination while preserving contamination effect. Quality validation: automated similarity metrics + human spot-check on 50 random pairs per benchmark.\\n\", \"priority\": \"P0\", \"gpu_budget_hours\": 50, \"deps\": [], \"benchmarks\": [\"MMLU\", \"GSM8K\", \"ARC-Challenge\", \"HumanEval\"], \"models\": [\"Qwen2.5-0.5B\", \"Qwen2.5-1.5B\", \"Qwen2.5-3B\"], \"seeds\": 3, \"registry_id\": \"exp_001_sft_injection\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"arc_qc_pass\": 697, \"arc_qc_rate\": 0.595, \"arc_total\": 1172, \"gsm8k_qc_pass\": 228, \"gsm8k_qc_rate\": 0.173, \"gsm8k_total\": 1319, \"humaneval_total\": 164, \"mmlu_qc_pass\": 6596, \"mmlu_qc_rate\": 0.47, \"mmlu_total\": 14042}}, {\"id\": \"exp-004\", \"name\": \"simulation_identifiability_sweep\", \"claim\": 1, \"also_supports\": [3], \"description\": \"Systematic synthetic-data sweep (NEW, not MVP — MVP only covered 4-5 conditions): exposure signal AUC (0.55, 0.60, 0.65, 0.70, 0.80, 0.90) × model count (20, 50, 100, 200) × prior strength (N(0,0.5), N(0,1), N(0,2)) × exposure type (binary, continuous). 144 conditions, 10 seeds each. Reports: θ-γ recovery RMSE, posterior correlation, coverage (50%/80%/95%), prior sensitivity. Establishes minimum AUC threshold; if 95% CI width > 15pp at AUC=0.65, label as \\\"cannot distinguish no contamination from moderate contamination.\\\" N_items=300 fixed (per MVP finding). Subsumes exp-010 (prior sensitivity) and exp-011 (few-examinee regime) — prior × N_models dimensions already in sweep grid. Growing Pains pre-estimation sub-experiment: at N_models=20/50, compare flat prior vs informative prior from pre-estimated item parameters. Also includes Fisher Information matrix analysis: derive approximate analytical relationship between signal AUC, N_models, and γ recoverability. Distinguish structural identifiability (parameters uniquely determined) from practical identifiability (estimation quality sufficient for decisions). Provides theoretical grounding for the empirical AUC ≥ 0.70 threshold.\\n\", \"priority\": \"P0\", \"gpu_budget_hours\": 0, \"deps\": [], \"note\": \"CPU only. MVP (mvp_sim_4pl_gamma) was preliminary; this is the full sweep.\", \"registry_id\": \"exp_004_sim_sweep\", \"status\": \"DONE\", \"conclusion\": \"failed\"}, {\"id\": \"exp-006\", \"name\": \"irt_calibration_and_baselines\", \"claim\": 1, \"also_supports\": [3], \"description\": \"Fit 4PL+γ IRT (Stan NUTS) on controlled models from exp-001/003. PRIMARY: per-benchmark fitting with benchmark-specific γ_k — this is the natural parameterization when IRT is fitted per-benchmark (each benchmark's model has its own γ_k). ABLATION: joint fitting across benchmarks with shared global γ (stronger assumption, tests whether contamination effect is homogeneous across benchmarks). Report both. Per-benchmark fitting (not joint) is the default to reduce local independence violation scope. Posterior predictive checks on item-level residual correlations to assess local independence empirically. Compute calibrated scores via exposure=0 counterfactual with CIs. Compare against 7 baselines: (0) Raw — no adjustment (anchor), (1) remove-and-rescore (drop flagged items), (2) single-signal 2PL+γ (best signal only, simpler IRT), (3) vanilla 4PL without γ (standard IRT, no contamination modeling), (4) linear exposure regression + bootstrap CI (simplest post-hoc), (5) Emperor's mitigation: rephrasing + option shuffling, (6) DCR fuzzy inference (EMNLP 2025) — the only existing method\\n    producing adjusted accuracy; must include or reviewers will reject.\\nEvaluate all 5 metrics: MAE, coverage (50%/80%/95%), sharpness, Kendall τ, dose-response monotonicity. Report mean ± std across 3 seeds (matched to exp-001 seeds).\\n\", \"priority\": \"P0\", \"gpu_budget_hours\": 8, \"deps\": [\"exp-003\"], \"benchmarks\": [\"MMLU\", \"GSM8K\", \"ARC-Challenge\", \"HumanEval\"], \"seeds\": 3, \"registry_id\": \"exp_006_irt_05B_gsm8k\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"joint_gamma\": 0.3463, \"joint_gamma_ci\": [-0.65, 1.4], \"joint_rhat\": 1.0081, \"joint_ess\": 956.4, \"joint_divergences\": 0, \"perbench_gamma\": 0.508, \"perbench_gamma_ci\": [-0.64, 1.84], \"perbench_rhat\": 1.0096, \"perbench_ess\": 522.2, \"perbench_divergences\": 0, \"delta_fix_applied\": true, \"signal_scores_after_delta\": [0, 0.016, 0.065, 0.197], \"baselines_mae\": {\"B0_raw\": 0.0034, \"B4_linear_regression\": 0.003, \"B3_vanilla_4pl\": 0.0123, \"IRT_4pl_gamma\": 0.0195, \"B6_dcr_fuzzy\": 0.2634, \"B2_2pl_gamma\": 0.3202}}}, {\"id\": \"exp-015\", \"name\": \"sft_d100_qc_only\", \"claim\": 1, \"description\": \"100% dosage SFT using only QC-pass paraphrases (7547/16697 items). Isolates noisy vs clean contamination confound identified by reviewer. D012 decision. Compare calibration metrics against exp-001 d100 (all paraphrases) to quantify effect of noisy contamination on IRT estimates.\\n\", \"priority\": \"P1\", \"gpu_budget_hours\": 5, \"deps\": [\"exp-001\"], \"benchmarks\": [\"MMLU\", \"GSM8K\", \"ARC-Challenge\", \"HumanEval\"], \"models\": [\"Qwen2.5-0.5B\"], \"seeds\": 1, \"status\": \"planned\", \"registry_id\": null, \"data_script\": \"exp001/prepare_qc_only_data.py\"}, {\"id\": \"exp-007\", \"name\": \"scale_bridging_7b\", \"claim\": 1, \"description\": \"Qwen2.5-7B controlled SFT injection at 5 dosage levels. Validates calibration accuracy scales to larger models. Requires multi-GPU node (7B LoRA SFT ~4-8h per run on 1×H100).\\n\", \"priority\": \"P1\", \"gpu_budget_hours\": 30, \"deps\": [\"exp-001\"], \"status\": \"planned\"}, {\"id\": \"exp-014\", \"name\": \"multi_family_validation\", \"claim\": 1, \"description\": \"Controlled SFT injection on at least one non-Qwen model family (Llama-3.2-1B or Pythia-1.4B) at 3 dosage levels (0%, 25%, 100%). Validates that identifiability boundaries and calibration accuracy generalize beyond Qwen2.5. Addresses Dream reviewer concern about single model family limiting generalizability (flagged [M][W]).\\n\", \"priority\": \"P1\", \"gpu_budget_hours\": 15, \"deps\": [\"exp-001\"], \"status\": \"planned\"}, {\"id\": \"exp-012\", \"name\": \"observational_72b\", \"claim\": 1, \"description\": \"Qwen2.5-72B observational analysis (inference only, no SFT). Extends ecological validity to frontier model scale.\\n\", \"priority\": \"P2\", \"gpu_budget_hours\": 15, \"deps\": [\"exp-006\"], \"status\": \"planned\"}], \"counts\": {\"planned\": 4, \"running\": 0, \"done\": 2, \"failed\": 1, \"orphaned\": 0}, \"total\": 7, \"coverage\": \"2/7\", \"coverage_pct\": 28.6}, \"2\": {\"experiments\": [{\"id\": \"exp-002\", \"name\": \"stage1_signal_pipeline\", \"claim\": 2, \"description\": \"Compute 4 detection signals on all contaminated + clean models from exp-001: (a) embedding-based semantic retrieval (FAISS + sentence-transformers), (b) Min-K%++ membership inference, (c) ConStat performance gap (original vs paraphrased items), (d) Self-Critique entropy collapse. Output: per-model-item exposure scores for each signal.\\n\", \"priority\": \"P0\", \"gpu_budget_hours\": 20, \"deps\": [\"exp-001\"], \"registry_id\": \"exp_002_signals_05B\", \"status\": \"DONE\", \"conclusion\": \"success\"}, {\"id\": \"exp-003\", \"name\": \"rrf_aggregation_ablation\", \"claim\": 2, \"description\": \"RRF fusion of 4 signals into composite per-item exposure score. Ablations: (a) RRF vs equal-weight rank averaging, (b) single-signal only (×4), (c) calibration-based weighted RRF variant, (d) false positive injection robustness check (inject FP at rates matching Duan et al. 2024). Also test degraded 2-signal mode (ConStat + Self-Critique) for closed-weight.\\n\", \"priority\": \"P0\", \"gpu_budget_hours\": 2, \"deps\": [\"exp-002\"], \"registry_id\": \"exp_003_rrf_05B\", \"status\": \"DONE\", \"conclusion\": \"success\"}, {\"id\": \"exp-008\", \"name\": \"signal_survival_analysis\", \"claim\": 2, \"description\": \"Systematic evaluation of detection signal reliability across training regimes. Signal × regime AUC heatmap: 4 signals × {base, SFT-clean, SFT-contaminated, RL-post-trained}. Confirms Self-Critique compensates where Min-K%++/ConStat degrade post-RL (per fragility paper arXiv 2510.02386). ELEVATED to Core Contribution 2 per Dream review (all 3 tiers identified this as the most genuinely novel finding).\\n\", \"priority\": \"P0\", \"gpu_budget_hours\": 10, \"deps\": [\"exp-002\"], \"registry_id\": \"exp_008_signal_survival_v4\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"S1_d005_auc_mean\": 0.979, \"S2_d005_auc_mean\": 0.465, \"S4_d005_auc_mean\": 0.481, \"S1_d100_cross_cohens_d_mean\": 3.6, \"S2_d100_cross_cohens_d_mean\": -1.98, \"S4_d100_cross_cohens_d_mean\": 0.45, \"effective_signals_at_05B\": 1, \"d021_fix\": \"within-model AUC only for d005; d100 uses cross-model Cohen's d\"}}, {\"id\": \"exp-009\", \"name\": \"rl_observational_case_study\", \"claim\": 2, \"also_supports\": [3], \"description\": \"Apply Self-Critique + available signals to existing RL-trained models: Qwen2.5-Instruct (0.5B/1.5B/3B/7B), DeepSeek-R1-Distill-1.5B/7B. Fit IRT with appropriately wider CIs. Expected regret quantification: compare uncalibrated vs calibrated vs remove-rescore for top-5 model selection. Framed as observational — directional external validity, not full quantitative validation. Near-zero γ check on known-clean benchmark (specificity test).\\n\", \"priority\": \"P1\", \"gpu_budget_hours\": 15, \"deps\": [\"exp-006\", \"exp-008\"], \"status\": \"planned\"}, {\"id\": \"exp-013\", \"name\": \"closed_weight_2signal_mode\", \"claim\": 2, \"description\": \"Degraded 2-signal mode (ConStat + Self-Critique, no logits/embeddings) for closed-weight models. Ablation quantifying 2-signal vs 4-signal calibration accuracy gap.\\n\", \"priority\": \"P2\", \"gpu_budget_hours\": 5, \"deps\": [\"exp-003\"], \"status\": \"planned\"}], \"counts\": {\"planned\": 2, \"running\": 0, \"done\": 3, \"failed\": 0, \"orphaned\": 0}, \"total\": 5, \"coverage\": \"3/5\", \"coverage_pct\": 60.0}, \"3\": {\"experiments\": [{\"id\": \"exp-005\", \"name\": \"noise_propagation_analysis\", \"claim\": 3, \"description\": \"Two parts: (A) Measurement error model (PRIMARY): extend Stan model to treat exposure as noisy observation: exposure_ij ~ N(τ_ij, σ_e²), where τ is latent true contamination. σ_e estimated from exp-001 ground truth FP/FN rates. This propagates Stage 1 uncertainty into posteriors automatically. Compare coverage (50%/80%/95%) vs point-estimate exposure baseline. (B) Post-hoc noise injection: inject Gaussian noise at 1×/1.5×/2× matched levels, re-fit standard model, measure CI widening for γ and θ. Both parts inform whether measurement error model closes the coverage gap.\\n\", \"priority\": \"P0\", \"gpu_budget_hours\": 0, \"deps\": [\"exp-002\", \"exp-004\"], \"note\": \"CPU only\", \"registry_id\": \"exp_005_noise_prop_v2\", \"status\": \"DONE\", \"conclusion\": \"failed\"}], \"counts\": {\"planned\": 0, \"running\": 0, \"done\": 0, \"failed\": 1, \"orphaned\": 0}, \"total\": 1, \"coverage\": \"0/1\", \"coverage_pct\": 0.0}}, \"unassigned\": [], \"summary\": {\"total_experiments\": 13, \"total_claims\": 3, \"counts\": {\"planned\": 6, \"running\": 0, \"done\": 5, \"failed\": 2, \"orphaned\": 0}, \"coverage\": \"5/13\", \"coverage_pct\": 38.5, \"unassigned\": 0}}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 137_

更新完成。

**汇总：**

| 指标 | 更新前 | 更新后 |
|------|--------|--------|
| **Claim 1** | 14.3% (1/7) | **28.6% (2/7)** |
| **Claim 2** | 0% (0/5) | **60.0% (3/5)** |
| **Claim 3** | 0% (0/1) | 0% (0/1) |
| **Overall** | 7.7% (1/13) | **38.5% (5/13)** |
| Orphaned | 1 | **0** |

**更新了 6 个 plan entry 的 registry_id：**
- exp-001: `exp_001_sft_d100_15B_v2` → `exp_001_sft_injection`（更准确的 umbrella 实验）
- exp-002: 空 → `exp_002_signals_05B` ✓ (Claim 2 +1)
- exp-003: 空 → `exp_003_rrf_05B` ✓ (Claim 2 +1)
- exp-006: 空 → `exp_006_irt_05B_gsm8k` ✓ (Claim 1 +1)
- exp-008: 空 → `exp_008_signal_survival_v4` ✓ (Claim 2 +1)
- exp-015: `exp_001_sft_d100_qc_only`(orphaned) → `null`

**未能提升的：**
- exp-004 (sim sweep): 全 6 版均 failed，保留原 ID
- exp-005 (noise prop): 全版本 failed/negative，保留原 ID
- Claim 3 仍 0%——唯一实验 exp-005 无成功版本

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d61fa97d-0b3f-42cc-a383-d75fd89e4948",
  "uuid": "7dd6b764-03be-4c5d-8eaf-dbc45e1b7fe9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YCvuoGKa4Q1bwqgbmVht7t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10662,
      "cache_read_input_tokens": 78741,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10662
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

_source line 138_

更新完成。

**汇总：**

| 指标 | 更新前 | 更新后 |
|------|--------|--------|
| **Claim 1** | 14.3% (1/7) | **28.6% (2/7)** |
| **Claim 2** | 0% (0/5) | **60.0% (3/5)** |
| **Claim 3** | 0% (0/1) | 0% (0/1) |
| **Overall** | 7.7% (1/13) | **38.5% (5/13)** |
| Orphaned | 1 | **0** |

**更新了 6 个 plan entry 的 registry_id：**
- exp-001: `exp_001_sft_d100_15B_v2` → `exp_001_sft_injection`（更准确的 umbrella 实验）
- exp-002: 空 → `exp_002_signals_05B` ✓ (Claim 2 +1)
- exp-003: 空 → `exp_003_rrf_05B` ✓ (Claim 2 +1)
- exp-006: 空 → `exp_006_irt_05B_gsm8k` ✓ (Claim 1 +1)
- exp-008: 空 → `exp_008_signal_survival_v4` ✓ (Claim 2 +1)
- exp-015: `exp_001_sft_d100_qc_only`(orphaned) → `null`

**未能提升的：**
- exp-004 (sim sweep): 全 6 版均 failed，保留原 ID
- exp-005 (noise prop): 全版本 failed/negative，保留原 ID
- Claim 3 仍 0%——唯一实验 exp-005 无成功版本

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 391479,
  "duration_api_ms": 365413,
  "num_turns": 21,
  "stop_reason": "end_turn",
  "session_id": "d61fa97d-0b3f-42cc-a383-d75fd89e4948",
  "total_cost_usd": 1.3472937,
  "usage": {
    "input_tokens": 15,
    "cache_creation_input_tokens": 77562,
    "cache_read_input_tokens": 500665,
    "output_tokens": 18000,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 77562,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 497,
        "cache_read_input_tokens": 78741,
        "cache_creation_input_tokens": 10662,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 10662
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 11071,
      "outputTokens": 4592,
      "cacheReadInputTokens": 417377,
      "cacheCreationInputTokens": 69084,
      "webSearchRequests": 0,
      "costUSD": 0.1621237,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 15,
      "outputTokens": 18000,
      "cacheReadInputTokens": 500665,
      "cacheCreationInputTokens": 77562,
      "webSearchRequests": 0,
      "costUSD": 1.18517,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "5d6fea9e-9623-4d95-ae40-9ece9d6bb860"
}
```

</details>

---
