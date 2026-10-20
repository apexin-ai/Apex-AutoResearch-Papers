# analysis claim audit — Part 2 of 2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../analysis-claim-audit.md) · [Structured JSON](../../../sessions/1b/1b9b5d4c25dd42d866f7.json)

## Before a recorded user message

### Assistant

_source line 114_

I now have comprehensive data for the audit. Let me write the report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e21c3add-633d-4663-b1eb-e2854d1b8be8",
  "uuid": "21c69f8d-03ff-4060-9ee8-5dba79491824",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JBpPZ1qkhfRoSAM3ug3t1x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4045,
      "cache_read_input_tokens": 116905,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4045
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

_source line 115_

<details open><summary>🔧 Tool call — Write · `toolu_01NzsCcGUJhzAYrvoNpTybrt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/claim_audit_report.md",
  "content": "# Claim Audit Report — struct_self_consist_ie\n\n**Date**: 2026-05-19  \n**Scope**: All quantitative claims in `docs/paper/sections/` cross-verified against experiment registry and paper_framing.md  \n**Method**: Extracted every numerical claim (ρ, AUROC, F1, pp-delta, percentages), traced to source experiment, compared.\n\n---\n\n## ❌ Inconsistencies Requiring Fix\n\n### 1. WNUT VC ρ inconsistency within paper (0.724 vs 0.730)\n\n| Location | Value |\n|----------|-------|\n| experiments.tex:48 | VC ρ=0.724 |\n| experiments.tex:104 | VC ρ=0.730 |\n| appendix.tex:217 (tab:wnut) | VC .724 |\n| appendix.tex:226 | VC ρ=0.724 |\n\n**Verdict**: 0.724 is the tabulated value, used 3× consistently. The 0.730 on line 104 is a **typo**.  \n**Fix**: Change experiments.tex:104 from `VC $\\rho{=}0.730$` to `VC $\\rho{=}0.724$`.\n\n### 2. SciERC AUROC in Table 1 vs registry (systematic offset)\n\nPaper Table 1 SciERC AUROC vs registry `exp_012_rerun_1024` (same ρ values, so same data):\n\n| Signal | Paper AUC | Registry AUROC | Δ |\n|--------|-----------|---------------|-----|\n| VC | .663 | .684 | -2.1pp |\n| SJ | .650 | .692 | -4.2pp |\n| FK | .602 | .629 | -2.7pp |\n| EM | .614 | .749 | **-13.5pp** |\n| LP | .578 | .578 | 0pp |\n\nρ values match to 3 decimal places (confirming same source data), but AUROC diverges except for LP. The EM gap (0.614 vs 0.749) is extreme. CoNLL AUROC values match the registry within 1pp.\n\n**Hypothesis**: Different AUROC binarization threshold or pipeline for SciERC. The SciERC median F1 may have tied instances handled differently.  \n**Action required**: Verify which AUROC pipeline produced Table 1. If the registry values are correct, Table 1 SciERC AUROC column needs updating. This also affects:\n- Abstract/Introduction \"AUROC up to 0.82\" → still valid (CoNLL EM 0.816 matches registry)\n- But SciERC EM AUROC should be ~0.749, not 0.614\n\n### 3. CoNLL LP selection Δ: Table 3 vs Appendix cross-selection table\n\n| Source | Greedy | LP F1 | LP Δ |\n|--------|--------|-------|------|\n| Table 3 (experiments.tex:122) | .908 | — | **-0.85pp** |\n| Appendix tab:cross_selection (appendix.tex:248) | .908 | .897 | **-1.1pp** |\n\nBoth claim 3-seed means, Qwen/CoNLL N=8. The Δ values (-0.85pp vs -1.1pp) are inconsistent.  \n**Fix**: Reconcile these two tables. Check whether different seed combinations or averaging methods were used.\n\n### 4. WNUT-17 zero-F1 rate inconsistency within paper\n\n| Location | Value |\n|----------|-------|\n| experiments.tex:12 (dataset description) | \"52% zero F1\" |\n| experiments.tex:103 | \"51% of instances yield F1=0\" |\n| limitations.tex:3 | \"51% F1=0\" |\n\n**Fix**: Unify to one value. If it's N=8 data, verify the exact percentage and use consistently.\n\n---\n\n## ⚠️ Ambiguous/Unverifiable Claims\n\n### 5. \"13–87% degeneracy\" in Introduction (line 15)\n\nThe introduction says \"instance degeneracy (13–87% across our benchmarks).\"\n\n- 13% ≈ FewNERD (10.1–13.1% depending on seed) ✓\n- 87% = LLaMA CoNLL N=16 (registry: 86.5–86.7%) — this is a specific **model×dataset×N** configuration, not a benchmark\n\nThe appendix (line 232) confirms: \"On CoNLL, 48–87% of instances produce identical outputs\" — spanning Qwen N=8 (48%) to LLaMA N=16 (87%).\n\n**Issue**: \"across our benchmarks\" suggests cross-dataset variation, but 87% comes from a specific model+N configuration within CoNLL. The dataset-only range is ~10–68% (FewNERD to WNUT).  \n**Recommendation**: Change to \"across our experimental configurations\" or specify: \"(13% on Few-NERD to 87% on CoNLL under LLaMA at N=16)\".\n\n### 6. CoNLL degeneracy 48.4% labeled as N=8 in Table 3\n\nTable 3 caption: \"Qwen3-8B, N=8, T=1.0\". CoNLL Degen.% = 48.4%.\n\nBut `tab:degeneracy` (appendix.tex:362) shows: \"CoNLL 8B (N=16)\" = 48.4%.\n\nRegistry `exp_002_conll_n16` (N=16, seed 42): degen_rate = 0.4844 (48.4%).\n\nNo N=8 CoNLL degeneracy rate found in registry. With fewer samples (N=8), ALL having identical F1 is easier, so N=8 degeneracy should be **higher** than N=16's 48.4%.\n\n**Risk**: Table 3 may be using the N=16 degeneracy value in an N=8 context.  \n**Action**: Verify the N=8 CoNLL degeneracy from the actual N=8 experiment data.\n\n### 7. FewNERD degeneracy 13.8% vs registry data\n\nPaper Table 3: FewNERD degen = 13.8%.\n\nRegistry individual seeds (all N=8):\n- Seed 42 (exp_021_fewnerd_full): 10.1%\n- Seed 123: 13.1%\n- Seed 456: 12.1%\n- Seed 789: 11.8%\n\n3-seed mean (42/123/456): (10.1 + 13.1 + 12.1) / 3 = **11.8%** ≠ 13.8%  \n4-seed mean: (10.1 + 13.1 + 12.1 + 11.8) / 4 = **11.8%** ≠ 13.8%\n\n**Source of 13.8% unclear.** No seed combination produces this value. Could be from a different computation or epoch checkpoint.\n\n### 8. FewNERD LP global ρ = .220 in Table 3 vs seed 42 = 0.422\n\nTable 3 says LP ρ = .220 (3-seed mean). Registry seed 42: lp_global_rho = 0.4215. Seed 789: lp_rho_global = 0.1788.\n\nThis implies seeds 123/456 have very low LP ρ (~0.12 each) for the 3-seed mean to be 0.22. The seed variance (0.18–0.42) is extremely high for Spearman ρ, which is unusual.\n\n**Cannot verify** from available registry data (seeds 123/456 lack LP ρ).  \n**Recommendation**: Verify the 3-seed LP ρ values and consider reporting seed-specific values to acknowledge this variance.\n\n### 9. WNUT LP ρ: paper -0.446 vs registry -0.410\n\nPaper Table 3: LP ρ = -.446 (claimed N=8).  \nRegistry exp_003_ner_wnut17 (N=16): rho_logprob_full = -0.414.  \nRegistry exp_003_wnut17_eval (N=16): rho_logprob_full = -0.409.\n\nDifferent N values (paper N=8, registry N=16), so some difference is expected. But no N=8 WNUT data found in registry to verify.\n\n### 10. Entity construction Δ: paper vs registry (protocol mismatch)\n\nPaper (multi-seed mean) vs registry (5-fold CV):\n\n| Dataset | Paper LP Δ | Registry LP Δ | Paper Unif Δ | Registry Unif Δ |\n|---------|-----------|--------------|-------------|----------------|\n| SciERC | +1.02pp | +1.67pp | +0.74pp | +1.12pp |\n| FewNERD | +1.40pp | +0.88pp | +0.74pp | +0.32pp |\n| CoNLL | -0.39pp | -0.39pp | — | — |\n\nLarge differences on SciERC and FewNERD. The paper uses \"multi-seed mean±σ\" (averaging results from different training seeds), while the registry uses \"5-fold CV, bootstrap B=10000\" (within one model). These are legitimately different evaluation protocols, so direct comparison is invalid.\n\n**However**: The direction of difference is inconsistent — registry is higher than paper on SciERC but lower on FewNERD. This means multi-seed averaging isn't simply scaling all values down.  \n**Recommendation**: Source the individual seed construction results to verify the multi-seed means match.\n\n---\n\n## ⚠️ Known Contradiction (from task description)\n\n**\"Discussion '+0.1pp over single-sample' vs Limitations '+0.4pp over greedy'\"**\n\n**Status**: Not found in current paper text.\n\nThe closest matches are:\n- Experiments §5.5 (scaling): \"LP selection fails (SciERC −0.1pp, CoNLL −0.4pp)\" — these are 72B zero-shot LP selection results, different datasets, both negative. Not contradictory.\n- TOST appendix table: SJ NER Δ = +0.1pp (vs single-sample) — this is in the appendix, not Discussion.\n- Limitations: \"LP×VC combinations yield at most +0.2pp over greedy\" — 0.2pp, not 0.4pp.\n\n**Conclusion**: The contradiction may have been resolved in the current paper version, or the task description references numbers from an earlier draft. The current paper does not contain this specific conflict.\n\n---\n\n## ✅ Verified Claims\n\n### Abstract & Introduction\n| Claim | Source | Registry/Verified Value | Status |\n|-------|--------|------------------------|--------|\n| ρ up to 0.45 | CoNLL EM | exp_002: EM rho=0.4507 → 0.45 | ✅ |\n| AUROC up to 0.82 | CoNLL EM | exp_002: EM AUROC=0.8156 → 0.82 | ✅ |\n| +5–8pp F1 at 80% coverage | Selective pred. | exp_selective_prediction: SciERC +5.0, CoNLL +8.4, FewNERD +6.2 | ✅ |\n| LP +1.39pp on FewNERD (p<0.001) | LP selection | 4-seed mean = 1.38pp (CI [1.32, 1.44]) | ✅ (rounds) |\n| SciERC LP +0.2pp, p=0.29 | Table 2 (2-seed) | 0.647 - 0.645 = 0.2pp | ✅ |\n| ρ=0.052 (23 configs, p=0.81) | Degen vs LP | paper_framing confirms | ✅ |\n| MBR SJ median ρ=0.524 | Discussion | tab:degeneracy: 0.524 | ✅ |\n\n### Table 1 (QE) — Spearman ρ\n| Signal | Paper | Registry (exp_012_rerun_1024) | Status |\n|--------|-------|-------------------------------|--------|\n| SciERC VC ρ | .379 | 0.3792 | ✅ |\n| SciERC SJ ρ | .360 | 0.3599 | ✅ |\n| SciERC FK ρ | .267 | 0.2665 | ✅ |\n| SciERC EM ρ | .295 | 0.2945 | ✅ |\n| SciERC LP ρ | .205 | 0.2052 | ✅ |\n| CoNLL SJ ρ | .436 | exp_002: 0.4357 | ✅ |\n| CoNLL EM ρ | .451 | exp_002: 0.4507 | ✅ |\n| CoNLL LP ρ | .316 | exp_002: 0.3157 | ✅ |\n\n### Table 2 (SciERC Selection)\n| Method | Paper | Notes | Status |\n|--------|-------|-------|--------|\n| Oracle | .775±.001 | exp_012_rerun_1024: oracle F1=0.7758 (framing) | ✅ |\n| Greedy | .645±.001 | Consistent with framing 0.6439/0.6442 | ✅ |\n| LP | .647±.005 | 2-seed mean | ✅ |\n| Random | .610±.003 | exp_016_rerun_1024 framing: 0.6077 | ✅ |\n\n### Table 3 (Cross-dataset)\n| Dataset | Greedy | Degen | LP ρ | LP Δ | Status |\n|---------|--------|-------|------|------|--------|\n| SciERC | .644 | 17.8% | .205 | +0.61pp | ✅ all match single-seed exp_012 |\n| FewNERD | .748 | 13.8% | .220 | +1.39pp | ⚠️ degen 13.8% unverifiable; LP ρ unverifiable |\n| CoNLL | .908 | 48.4% | .302 | -0.85pp | ⚠️ degen might be N=16; LP Δ conflicts with appendix |\n| WNUT | .452 | 67.9% | -.446 | -0.45pp | ⚠️ LP ρ unverifiable at N=8 |\n\n### Scale Ablation (Table in experiments.tex)\n| Metric | Paper | Registry | Status |\n|--------|-------|----------|--------|\n| CoNLL 8B SJ ρ | .436 | exp_002: 0.4357 | ✅ |\n| CoNLL 4B SJ ρ | .422 | exp_qwen3_4b_conll: 0.4217 | ✅ |\n| SciERC 8B SJ ρ | .360 | exp_012_rerun_1024: 0.3599 | ✅ |\n| SciERC 4B SJ ρ | .422 | exp_qwen3_4b_scierc: 0.4221 | ✅ |\n| SciERC 8B degen | 17.8% | 0.1777 | ✅ |\n| SciERC 4B degen | 10.4% | 0.104 | ✅ |\n\n### 72B Zero-shot (Table in experiments.tex)\n| Metric | Paper | Source | Status |\n|--------|-------|--------|--------|\n| SciERC 72B LP ρ | .081 | paper_framing: 0.081 | ✅ |\n| CoNLL 72B LP ρ | -.002 | paper_framing: -0.002 | ✅ |\n| SciERC 72B constr. +1.5pp | +1.5pp | paper_framing: +1.53pp | ✅ (rounded) |\n| CoNLL 72B constr. -0.37pp | -0.37pp | paper_framing: -0.37pp | ✅ |\n\nNote: 72B experiment is still RUNNING in registry — no final metrics to cross-verify. Paper values sourced from framing doc only.\n\n### LoRA Rank Ablation\n| Metric | Paper | Registry (exp_023_lora_rank8) | Status |\n|--------|-------|-------------------------------|--------|\n| Rank=8 degen | 7.2% | 0.072 | ✅ |\n| VC ρ | .394 (text) | 0.394 | ✅ |\n| SJ ρ | .365 (text) | 0.3649 | ✅ |\n\n### Other Verified Claims\n| Claim | Source | Status |\n|-------|--------|--------|\n| T=1.2 degen 14.9% | exp_026_t12: 0.1493 | ✅ |\n| Non-tied LP +2.9pp | Discussion | ✅ (p-value differs: paper 0.004 vs framing 0.01 — check which is post-correction) |\n| Bootstrap CI [-3.0, +4.2]pp | exp_016_rerun_1024_bootstrap: [-0.030, 0.042] | ✅ |\n| Cohen's d = 0.038 | exp_016_rerun_1024_bootstrap: 0.038 | ✅ |\n| Freeform std ratio 0.97 | exp_freeform_ablation: 0.97 | ✅ |\n| Parse rate 99.95% | exp_freeform_ablation: 0.9995 | ✅ |\n| FewNERD LP CI [1.02, 1.34] paper vs [1.18, 1.53] registry | Abstract says [1.02, 1.34]; registry says [1.18, 1.53] | ⚠️ see below |\n\n### Abstract LP CI discrepancy\nAbstract line 7: \"p<0.005\" (Table 5 shows p=.004 for SciERC and p<.001 for FewNERD — both < 0.005). The \"(multi-seed mean, p<0.005)\" applies to the joint claim. ✅\n\nBut the **bootstrap CI** for FewNERD LP selection:\n- Abstract: implied from \"p<0.005\"\n- Registry exp_021_fewnerd_full: lp_bootstrap_ci_95_pp = [1.18, 1.53]\n- Paper Table 3: not shown explicitly\n- Paper framing: LP selection CI [+1.02, +1.34] (for the 4-seed mean)\n\nThe CI [1.02, 1.34] (framing) vs [1.18, 1.53] (registry) represent different computations: framing uses 4-seed bootstrap of means, registry uses single-seed bootstrap. Not an error, but worth documenting.\n\n---\n\n## Summary of Required Actions\n\n| Priority | Issue | Action |\n|----------|-------|--------|\n| **P0** | ❌ WNUT VC ρ typo (0.730 → 0.724) | Fix experiments.tex:104 |\n| **P0** | ❌ SciERC AUROC pipeline discrepancy | Verify Table 1 AUROC computation; if registry is correct, update table |\n| **P0** | ❌ CoNLL LP Δ mismatch (-0.85 vs -1.1pp) | Reconcile Table 3 and Appendix cross-selection table |\n| **P0** | ❌ WNUT zero-F1 rate (51% vs 52%) | Unify within paper |\n| **P1** | ⚠️ \"13–87%\" in intro | Change to \"across configurations\" or give dataset-specific range |\n| **P1** | ⚠️ CoNLL degen 48.4% N=8 vs N=16 | Verify the N=8 value |\n| **P1** | ⚠️ FewNERD degen 13.8% source | Document or correct |\n| **P2** | ⚠️ FewNERD LP ρ seed variance | Consider reporting seed-level values |\n| **P2** | ⚠️ Non-tied LP p-value (0.004 vs 0.01) | Verify: one is pre-correction, one post? |\n| **INFO** | Known contradiction from task | Not found in current version; appears resolved |\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e21c3add-633d-4663-b1eb-e2854d1b8be8",
  "uuid": "4f668703-09dd-4f6b-835c-c332885f3b5d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JBpPZ1qkhfRoSAM3ug3t1x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4045,
      "cache_read_input_tokens": 116905,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4045
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

_source line 116 · 2026-05-19T13:46:11.394Z_

<details><summary>↩ Tool result · `toolu_01NzsCcGUJhzAYrvoNpTybrt`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/claim_audit_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e21c3add-633d-4663-b1eb-e2854d1b8be8",
  "uuid": "d4012bfa-415b-4af0-9d55-d52206d3d23c",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/claim_audit_report.md",
    "content": "# Claim Audit Report — struct_self_consist_ie\n\n**Date**: 2026-05-19  \n**Scope**: All quantitative claims in `docs/paper/sections/` cross-verified against experiment registry and paper_framing.md  \n**Method**: Extracted every numerical claim (ρ, AUROC, F1, pp-delta, percentages), traced to source experiment, compared.\n\n---\n\n## ❌ Inconsistencies Requiring Fix\n\n### 1. WNUT VC ρ inconsistency within paper (0.724 vs 0.730)\n\n| Location | Value |\n|----------|-------|\n| experiments.tex:48 | VC ρ=0.724 |\n| experiments.tex:104 | VC ρ=0.730 |\n| appendix.tex:217 (tab:wnut) | VC .724 |\n| appendix.tex:226 | VC ρ=0.724 |\n\n**Verdict**: 0.724 is the tabulated value, used 3× consistently. The 0.730 on line 104 is a **typo**.  \n**Fix**: Change experiments.tex:104 from `VC $\\rho{=}0.730$` to `VC $\\rho{=}0.724$`.\n\n### 2. SciERC AUROC in Table 1 vs registry (systematic offset)\n\nPaper Table 1 SciERC AUROC vs registry `exp_012_rerun_1024` (same ρ values, so same data):\n\n| Signal | Paper AUC | Registry AUROC | Δ |\n|--------|-----------|---------------|-----|\n| VC | .663 | .684 | -2.1pp |\n| SJ | .650 | .692 | -4.2pp |\n| FK | .602 | .629 | -2.7pp |\n| EM | .614 | .749 | **-13.5pp** |\n| LP | .578 | .578 | 0pp |\n\nρ values match to 3 decimal places (confirming same source data), but AUROC diverges except for LP. The EM gap (0.614 vs 0.749) is extreme. CoNLL AUROC values match the registry within 1pp.\n\n**Hypothesis**: Different AUROC binarization threshold or pipeline for SciERC. The SciERC median F1 may have tied instances handled differently.  \n**Action required**: Verify which AUROC pipeline produced Table 1. If the registry values are correct, Table 1 SciERC AUROC column needs updating. This also affects:\n- Abstract/Introduction \"AUROC up to 0.82\" → still valid (CoNLL EM 0.816 matches registry)\n- But SciERC EM AUROC should be ~0.749, not 0.614\n\n### 3. CoNLL LP selection Δ: Table 3 vs Appendix cross-selection table\n\n| Source | Greedy | LP F1 | LP Δ |\n|--------|--------|-------|------|\n| Table 3 (experiments.tex:122) | .908 | — | **-0.85pp** |\n| Appendix tab:cross_selection (appendix.tex:248) | .908 | .897 | **-1.1pp** |\n\nBoth claim 3-seed means, Qwen/CoNLL N=8. The Δ values (-0.85pp vs -1.1pp) are inconsistent.  \n**Fix**: Reconcile these two tables. Check whether different seed combinations or averaging methods were used.\n\n### 4. WNUT-17 zero-F1 rate inconsistency within paper\n\n| Location | Value |\n|----------|-------|\n| experiments.tex:12 (dataset description) | \"52% zero F1\" |\n| experiments.tex:103 | \"51% of instances yield F1=0\" |\n| limitations.tex:3 | \"51% F1=0\" |\n\n**Fix**: Unify to one value. If it's N=8 data, verify the exact percentage and use consistently.\n\n---\n\n## ⚠️ Ambiguous/Unverifiable Claims\n\n### 5. \"13–87% degeneracy\" in Introduction (line 15)\n\nThe introduction says \"instance degeneracy (13–87% across our benchmarks).\"\n\n- 13% ≈ FewNERD (10.1–13.1% depending on seed) ✓\n- 87% = LLaMA CoNLL N=16 (registry: 86.5–86.7%) — this is a specific **model×dataset×N** configuration, not a benchmark\n\nThe appendix (line 232) confirms: \"On CoNLL, 48–87% of instances produce identical outputs\" — spanning Qwen N=8 (48%) to LLaMA N=16 (87%).\n\n**Issue**: \"across our benchmarks\" suggests cross-dataset variation, but 87% comes from a specific model+N configuration within CoNLL. The dataset-only range is ~10–68% (FewNERD to WNUT).  \n**Recommendation**: Change to \"across our experimental configurations\" or specify: \"(13% on Few-NERD to 87% on CoNLL under LLaMA at N=16)\".\n\n### 6. CoNLL degeneracy 48.4% labeled as N=8 in Table 3\n\nTable 3 caption: \"Qwen3-8B, N=8, T=1.0\". CoNLL Degen.% = 48.4%.\n\nBut `tab:degeneracy` (appendix.tex:362) shows: \"CoNLL 8B (N=16)\" = 48.4%.\n\nRegistry `exp_002_conll_n16` (N=16, seed 42): degen_rate = 0.4844 (48.4%).\n\nNo N=8 CoNLL degeneracy rate found in registry. With fewer samples (N=8), ALL having identical F1 is easier, so N=8 degeneracy should be **higher** than N=16's 48.4%.\n\n**Risk**: Table 3 may be using the N=16 degeneracy value in an N=8 context.  \n**Action**: Verify the N=8 CoNLL degeneracy from the actual N=8 experiment data.\n\n### 7. FewNERD degeneracy 13.8% vs registry data\n\nPaper Table 3: FewNERD degen = 13.8%.\n\nRegistry individual seeds (all N=8):\n- Seed 42 (exp_021_fewnerd_full): 10.1%\n- Seed 123: 13.1%\n- Seed 456: 12.1%\n- Seed 789: 11.8%\n\n3-seed mean (42/123/456): (10.1 + 13.1 + 12.1) / 3 = **11.8%** ≠ 13.8%  \n4-seed mean: (10.1 + 13.1 + 12.1 + 11.8) / 4 = **11.8%** ≠ 13.8%\n\n**Source of 13.8% unclear.** No seed combination produces this value. Could be from a different computation or epoch checkpoint.\n\n### 8. FewNERD LP global ρ = .220 in Table 3 vs seed 42 = 0.422\n\nTable 3 says LP ρ = .220 (3-seed mean). Registry seed 42: lp_global_rho = 0.4215. Seed 789: lp_rho_global = 0.1788.\n\nThis implies seeds 123/456 have very low LP ρ (~0.12 each) for the 3-seed mean to be 0.22. The seed variance (0.18–0.42) is extremely high for Spearman ρ, which is unusual.\n\n**Cannot verify** from available registry data (seeds 123/456 lack LP ρ).  \n**Recommendation**: Verify the 3-seed LP ρ values and consider reporting seed-specific values to acknowledge this variance.\n\n### 9. WNUT LP ρ: paper -0.446 vs registry -0.410\n\nPaper Table 3: LP ρ = -.446 (claimed N=8).  \nRegistry exp_003_ner_wnut17 (N=16): rho_logprob_full = -0.414.  \nRegistry exp_003_wnut17_eval (N=16): rho_logprob_full = -0.409.\n\nDifferent N values (paper N=8, registry N=16), so some difference is expected. But no N=8 WNUT data found in registry to verify.\n\n### 10. Entity construction Δ: paper vs registry (protocol mismatch)\n\nPaper (multi-seed mean) vs registry (5-fold CV):\n\n| Dataset | Paper LP Δ | Registry LP Δ | Paper Unif Δ | Registry Unif Δ |\n|---------|-----------|--------------|-------------|----------------|\n| SciERC | +1.02pp | +1.67pp | +0.74pp | +1.12pp |\n| FewNERD | +1.40pp | +0.88pp | +0.74pp | +0.32pp |\n| CoNLL | -0.39pp | -0.39pp | — | — |\n\nLarge differences on SciERC and FewNERD. The paper uses \"multi-seed mean±σ\" (averaging results from different training seeds), while the registry uses \"5-fold CV, bootstrap B=10000\" (within one model). These are legitimately different evaluation protocols, so direct comparison is invalid.\n\n**However**: The direction of difference is inconsistent — registry is higher than paper on SciERC but lower on FewNERD. This means multi-seed averaging isn't simply scaling all values down.  \n**Recommendation**: Source the individual seed construction results to verify the multi-seed means match.\n\n---\n\n## ⚠️ Known Contradiction (from task description)\n\n**\"Discussion '+0.1pp over single-sample' vs Limitations '+0.4pp over greedy'\"**\n\n**Status**: Not found in current paper text.\n\nThe closest matches are:\n- Experiments §5.5 (scaling): \"LP selection fails (SciERC −0.1pp, CoNLL −0.4pp)\" — these are 72B zero-shot LP selection results, different datasets, both negative. Not contradictory.\n- TOST appendix table: SJ NER Δ = +0.1pp (vs single-sample) — this is in the appendix, not Discussion.\n- Limitations: \"LP×VC combinations yield at most +0.2pp over greedy\" — 0.2pp, not 0.4pp.\n\n**Conclusion**: The contradiction may have been resolved in the current paper version, or the task description references numbers from an earlier draft. The current paper does not contain this specific conflict.\n\n---\n\n## ✅ Verified Claims\n\n### Abstract & Introduction\n| Claim | Source | Registry/Verified Value | Status |\n|-------|--------|------------------------|--------|\n| ρ up to 0.45 | CoNLL EM | exp_002: EM rho=0.4507 → 0.45 | ✅ |\n| AUROC up to 0.82 | CoNLL EM | exp_002: EM AUROC=0.8156 → 0.82 | ✅ |\n| +5–8pp F1 at 80% coverage | Selective pred. | exp_selective_prediction: SciERC +5.0, CoNLL +8.4, FewNERD +6.2 | ✅ |\n| LP +1.39pp on FewNERD (p<0.001) | LP selection | 4-seed mean = 1.38pp (CI [1.32, 1.44]) | ✅ (rounds) |\n| SciERC LP +0.2pp, p=0.29 | Table 2 (2-seed) | 0.647 - 0.645 = 0.2pp | ✅ |\n| ρ=0.052 (23 configs, p=0.81) | Degen vs LP | paper_framing confirms | ✅ |\n| MBR SJ median ρ=0.524 | Discussion | tab:degeneracy: 0.524 | ✅ |\n\n### Table 1 (QE) — Spearman ρ\n| Signal | Paper | Registry (exp_012_rerun_1024) | Status |\n|--------|-------|-------------------------------|--------|\n| SciERC VC ρ | .379 | 0.3792 | ✅ |\n| SciERC SJ ρ | .360 | 0.3599 | ✅ |\n| SciERC FK ρ | .267 | 0.2665 | ✅ |\n| SciERC EM ρ | .295 | 0.2945 | ✅ |\n| SciERC LP ρ | .205 | 0.2052 | ✅ |\n| CoNLL SJ ρ | .436 | exp_002: 0.4357 | ✅ |\n| CoNLL EM ρ | .451 | exp_002: 0.4507 | ✅ |\n| CoNLL LP ρ | .316 | exp_002: 0.3157 | ✅ |\n\n### Table 2 (SciERC Selection)\n| Method | Paper | Notes | Status |\n|--------|-------|-------|--------|\n| Oracle | .775±.001 | exp_012_rerun_1024: oracle F1=0.7758 (framing) | ✅ |\n| Greedy | .645±.001 | Consistent with framing 0.6439/0.6442 | ✅ |\n| LP | .647±.005 | 2-seed mean | ✅ |\n| Random | .610±.003 | exp_016_rerun_1024 framing: 0.6077 | ✅ |\n\n### Table 3 (Cross-dataset)\n| Dataset | Greedy | Degen | LP ρ | LP Δ | Status |\n|---------|--------|-------|------|------|--------|\n| SciERC | .644 | 17.8% | .205 | +0.61pp | ✅ all match single-seed exp_012 |\n| FewNERD | .748 | 13.8% | .220 | +1.39pp | ⚠️ degen 13.8% unverifiable; LP ρ unverifiable |\n| CoNLL | .908 | 48.4% | .302 | -0.85pp | ⚠️ degen might be N=16; LP Δ conflicts with appendix |\n| WNUT | .452 | 67.9% | -.446 | -0.45pp | ⚠️ LP ρ unverifiable at N=8 |\n\n### Scale Ablation (Table in experiments.tex)\n| Metric | Paper | Registry | Status |\n|--------|-------|----------|--------|\n| CoNLL 8B SJ ρ | .436 | exp_002: 0.4357 | ✅ |\n| CoNLL 4B SJ ρ | .422 | exp_qwen3_4b_conll: 0.4217 | ✅ |\n| SciERC 8B SJ ρ | .360 | exp_012_rerun_1024: 0.3599 | ✅ |\n| SciERC 4B SJ ρ | .422 | exp_qwen3_4b_scierc: 0.4221 | ✅ |\n| SciERC 8B degen | 17.8% | 0.1777 | ✅ |\n| SciERC 4B degen | 10.4% | 0.104 | ✅ |\n\n### 72B Zero-shot (Table in experiments.tex)\n| Metric | Paper | Source | Status |\n|--------|-------|--------|--------|\n| SciERC 72B LP ρ | .081 | paper_framing: 0.081 | ✅ |\n| CoNLL 72B LP ρ | -.002 | paper_framing: -0.002 | ✅ |\n| SciERC 72B constr. +1.5pp | +1.5pp | paper_framing: +1.53pp | ✅ (rounded) |\n| CoNLL 72B constr. -0.37pp | -0.37pp | paper_framing: -0.37pp | ✅ |\n\nNote: 72B experiment is still RUNNING in registry — no final metrics to cross-verify. Paper values sourced from framing doc only.\n\n### LoRA Rank Ablation\n| Metric | Paper | Registry (exp_023_lora_rank8) | Status |\n|--------|-------|-------------------------------|--------|\n| Rank=8 degen | 7.2% | 0.072 | ✅ |\n| VC ρ | .394 (text) | 0.394 | ✅ |\n| SJ ρ | .365 (text) | 0.3649 | ✅ |\n\n### Other Verified Claims\n| Claim | Source | Status |\n|-------|--------|--------|\n| T=1.2 degen 14.9% | exp_026_t12: 0.1493 | ✅ |\n| Non-tied LP +2.9pp | Discussion | ✅ (p-value differs: paper 0.004 vs framing 0.01 — check which is post-correction) |\n| Bootstrap CI [-3.0, +4.2]pp | exp_016_rerun_1024_bootstrap: [-0.030, 0.042] | ✅ |\n| Cohen's d = 0.038 | exp_016_rerun_1024_bootstrap: 0.038 | ✅ |\n| Freeform std ratio 0.97 | exp_freeform_ablation: 0.97 | ✅ |\n| Parse rate 99.95% | exp_freeform_ablation: 0.9995 | ✅ |\n| FewNERD LP CI [1.02, 1.34] paper vs [1.18, 1.53] registry | Abstract says [1.02, 1.34]; registry says [1.18, 1.53] | ⚠️ see below |\n\n### Abstract LP CI discrepancy\nAbstract line 7: \"p<0.005\" (Table 5 shows p=.004 for SciERC and p<.001 for FewNERD — both < 0.005). The \"(multi-seed mean, p<0.005)\" applies to the joint claim. ✅\n\nBut the **bootstrap CI** for FewNERD LP selection:\n- Abstract: implied from \"p<0.005\"\n- Registry exp_021_fewnerd_full: lp_bootstrap_ci_95_pp = [1.18, 1.53]\n- Paper Table 3: not shown explicitly\n- Paper framing: LP selection CI [+1.02, +1.34] (for the 4-seed mean)\n\nThe CI [1.02, 1.34] (framing) vs [1.18, 1.53] (registry) represent different computations: framing uses 4-seed bootstrap of means, registry uses single-seed bootstrap. Not an error, but worth documenting.\n\n---\n\n## Summary of Required Actions\n\n| Priority | Issue | Action |\n|----------|-------|--------|\n| **P0** | ❌ WNUT VC ρ typo (0.730 → 0.724) | Fix experiments.tex:104 |\n| **P0** | ❌ SciERC AUROC pipeline discrepancy | Verify Table 1 AUROC computation; if registry is correct, update table |\n| **P0** | ❌ CoNLL LP Δ mismatch (-0.85 vs -1.1pp) | Reconcile Table 3 and Appendix cross-selection table |\n| **P0** | ❌ WNUT zero-F1 rate (51% vs 52%) | Unify within paper |\n| **P1** | ⚠️ \"13–87%\" in intro | Change to \"across configurations\" or give dataset-specific range |\n| **P1** | ⚠️ CoNLL degen 48.4% N=8 vs N=16 | Verify the N=8 value |\n| **P1** | ⚠️ FewNERD degen 13.8% source | Document or correct |\n| **P2** | ⚠️ FewNERD LP ρ seed variance | Consider reporting seed-level values |\n| **P2** | ⚠️ Non-tied LP p-value (0.004 vs 0.01) | Verify: one is pre-correction, one post? |\n| **INFO** | Known contradiction from task | Not found in current version; appears resolved |\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---


### Tool call

_source line 117_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01LP7P8zMGPdca168yWfg2J2`</summary>

```json
{
  "name": "claim_audit_report",
  "type": "report",
  "description": "Full quantitative claim audit of the paper: cross-verified all numerical claims against experiment registry. Found 4 inconsistencies requiring fix, 6 ambiguous/unverifiable claims, and confirmed ~30 claims as correct.",
  "project": "struct_self_consist_ie",
  "exp_id": "exp_024_claim_audit",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/claim_audit_report.md",
  "tags": [
    "audit",
    "paper",
    "claim-verification"
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
  "session_id": "e21c3add-633d-4663-b1eb-e2854d1b8be8",
  "uuid": "c213d1e5-4be9-4115-808e-23a7f3f32e74",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BuN2LRgjR1b2Fpov4TqCRx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7872,
      "cache_read_input_tokens": 120950,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7872
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    },
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 118 · 2026-05-19T13:46:18.571Z_

<details><summary>↩ Tool result · `toolu_01LP7P8zMGPdca168yWfg2J2`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260519_146f83\", \"name\": \"claim_audit_report\", \"type\": \"report\", \"description\": \"Full quantitative claim audit of the paper: cross-verified all numerical claims against experiment registry. Found 4 inconsistencies requiring fix, 6 ambiguous/unverifiable claims, and confirmed ~30 claims as correct.\", \"path\": \"projects/struct_self_consist_ie/artifacts/exp_024_claim_audit/report/claim_audit_report.md\", \"url\": null, \"project\": \"struct_self_consist_ie\", \"exp_id\": \"exp_024_claim_audit\", \"skill\": \"\", \"created_at\": \"2026-05-19T13:46:18.176541+00:00\", \"tags\": [\"audit\", \"paper\", \"claim-verification\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e21c3add-633d-4663-b1eb-e2854d1b8be8",
  "uuid": "e4d8543f-1044-4f4a-bd85-78c6928304da",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260519_146f83\\\", \\\"name\\\": \\\"claim_audit_report\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Full quantitative claim audit of the paper: cross-verified all numerical claims against experiment registry. Found 4 inconsistencies requiring fix, 6 ambiguous/unverifiable claims, and confirmed ~30 claims as correct.\\\", \\\"path\\\": \\\"projects/struct_self_consist_ie/artifacts/exp_024_claim_audit/report/claim_audit_report.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"struct_self_consist_ie\\\", \\\"exp_id\\\": \\\"exp_024_claim_audit\\\", \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-19T13:46:18.176541+00:00\\\", \\\"tags\\\": [\\\"audit\\\", \\\"paper\\\", \\\"claim-verification\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260519_146f83\", \"name\": \"claim_audit_report\", \"type\": \"report\", \"description\": \"Full quantitative claim audit of the paper: cross-verified all numerical claims against experiment registry. Found 4 inconsistencies requiring fix, 6 ambiguous/unverifiable claims, and confirmed ~30 claims as correct.\", \"path\": \"projects/struct_self_consist_ie/artifacts/exp_024_claim_audit/report/claim_audit_report.md\", \"url\": null, \"project\": \"struct_self_consist_ie\", \"exp_id\": \"exp_024_claim_audit\", \"skill\": \"\", \"created_at\": \"2026-05-19T13:46:18.176541+00:00\", \"tags\": [\"audit\", \"paper\", \"claim-verification\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 119_

审计报告已写入 `artifacts/claim_audit_report.md` 并注册。

核心发现：

**4 个需修复的不一致 (❌)**：
1. WNUT VC ρ 打字错误：experiments.tex:104 写了 0.730，应为 0.724
2. Table 1 SciERC AUROC 列与 registry 系统性偏离（EM: 0.614 vs 0.749），疑似 AUROC 计算管线不同
3. CoNLL LP 选择 Δ：Table 3 写 -0.85pp，附录 cross-selection 表算出 -1.1pp
4. WNUT zero-F1 率在论文内不统一（51% vs 52%）

**6 个存疑/无法验证的声明 (⚠️)**：
- "13–87% degeneracy" 跨 benchmarks → 87% 来自特定 model×N 配置，非跨数据集
- CoNLL 退化率 48.4% 可能是 N=16 值误用于 N=8 表格
- FewNERD 退化率 13.8% 无法从 registry seed 数据复现（3-seed 均值约 11.8%）
- FewNERD LP ρ=.220 种子间方差极大，无法从现有数据验证
- Entity construction 数值因评估协议不同（multi-seed vs 5-fold CV）无法直接对比

**已知矛盾状态**：当前论文版本中未找到 "Discussion +0.1pp" vs "Limitations +0.4pp" 冲突，可能已在编辑中修复。72B 节中 SciERC -0.1pp 和 CoNLL -0.4pp 是不同数据集的结果，非矛盾。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e21c3add-633d-4663-b1eb-e2854d1b8be8",
  "uuid": "0bd64ac1-08b8-4e69-9a86-11643cff4161",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BdAa2b99RFZP6L5dWoT8wE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8455,
      "cache_read_input_tokens": 120950,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8455
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    },
    "context_management": null
  }
}
```

</details>

---


### Task result

_source line 120_

审计报告已写入 `artifacts/claim_audit_report.md` 并注册。

核心发现：

**4 个需修复的不一致 (❌)**：
1. WNUT VC ρ 打字错误：experiments.tex:104 写了 0.730，应为 0.724
2. Table 1 SciERC AUROC 列与 registry 系统性偏离（EM: 0.614 vs 0.749），疑似 AUROC 计算管线不同
3. CoNLL LP 选择 Δ：Table 3 写 -0.85pp，附录 cross-selection 表算出 -1.1pp
4. WNUT zero-F1 率在论文内不统一（51% vs 52%）

**6 个存疑/无法验证的声明 (⚠️)**：
- "13–87% degeneracy" 跨 benchmarks → 87% 来自特定 model×N 配置，非跨数据集
- CoNLL 退化率 48.4% 可能是 N=16 值误用于 N=8 表格
- FewNERD 退化率 13.8% 无法从 registry seed 数据复现（3-seed 均值约 11.8%）
- FewNERD LP ρ=.220 种子间方差极大，无法从现有数据验证
- Entity construction 数值因评估协议不同（multi-seed vs 5-fold CV）无法直接对比

**已知矛盾状态**：当前论文版本中未找到 "Discussion +0.1pp" vs "Limitations +0.4pp" 冲突，可能已在编辑中修复。72B 节中 SciERC -0.1pp 和 CoNLL -0.4pp 是不同数据集的结果，非矛盾。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 788905,
  "duration_api_ms": 788299,
  "num_turns": 43,
  "stop_reason": "end_turn",
  "session_id": "e21c3add-633d-4663-b1eb-e2854d1b8be8",
  "total_cost_usd": 2.5893235000000003,
  "usage": {
    "input_tokens": 25,
    "cache_creation_input_tokens": 125576,
    "cache_read_input_tokens": 1604747,
    "output_tokens": 40013,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 125576,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 515,
        "cache_read_input_tokens": 120950,
        "cache_creation_input_tokens": 8455,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 8455
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1570,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.00165,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 25,
      "outputTokens": 40013,
      "cacheReadInputTokens": 1604747,
      "cacheCreationInputTokens": 125576,
      "webSearchRequests": 0,
      "costUSD": 2.5876735,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "4d980ee5-2707-4ab7-bbb6-e67dd4dc9db7"
}
```

</details>

---
