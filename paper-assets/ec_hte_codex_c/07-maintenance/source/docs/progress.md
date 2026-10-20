# 进度日志 — ec_hte_codex_c

> 由 Agent 自动维护，记录关键里程碑和决策。

- **[2026-05-31 16:59 UTC]** D014 fixed-k6 component formal runs completed: hierarchical_shrinkage_ec_hte_001 success, adaptive_expert_allocation_001 success, variance_propagation_ci_001 negative; all CPU-only with logs/results/hash/env registered and Reviewer audit requested.
- **[2026-05-31 17:12 UTC]** Fixed D014 script metadata bug for future reuse: phase/hierarchical/adaptive/variance scripts now default to smoke_only=false and run_mode=formal unless --smoke is passed; registered variance_propagation_ci_real_001 design-only CPU spec.
- **[2026-05-31 17:18 UTC]** D016 variance_propagation_ci_real_001 implementation and CPU smoke completed: py_compile passed, smoke outputs present, metadata smoke_only=true/run_mode=smoke valid, formal gate remains closed.
- **[2026-05-31 17:21 UTC]** D017 variance_propagation_ci_real_001 smoke rerun completed after Reviewer warning: expected outputs include ci_width/audit covariance, bootstrap per-draw and delta PSD/Jacobian diagnostics recorded, strict gate remains fail in smoke, formal gate closed.
- **[2026-05-31 17:26 UTC]** D019 variance_propagation_ci_real_001 covariance-audit smoke completed: audit_confusion_covariance.json now includes shape/block/count/rank/PSD/eigen/condition/regularization summaries consistent with delta diagnostics; strict gate remains false; formal gate closed.
- **[2026-05-31 17:29 UTC]** D020 variance_propagation_ci_real_001 smoke completed: delta diagnostics now output both j_sigma_jt_psd_check and j_sigma_j_psd_check; results/config include script/config sha256; output_file_hashes.json covers the 9 expected smoke files; strict gate remains false and formal gate closed.
- **[2026-05-31 17:36 UTC]** D022 next CI design submitted without running experiments: registered ci_covariance_shrinkage_001, ci_allocation_aware_audit_001, and ci_guarded_bootstrap_fallback_001 as PREPARING/design-only CPU specs with formal gates closed.
