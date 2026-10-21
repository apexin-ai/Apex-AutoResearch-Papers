# ops r5 csv k3 bugfix

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_r5_csv_k3_bugfix_20260520T204937_result.json`
- **Structured JSON:** [`088061768454e8306e2c.json`](../../sessions/08/088061768454e8306e2c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done. Here's the final output:

```json
{
  "csv_fix": {
    "bug_found": true,
    "bug_description": "compile_dose_response.py did not apply D111 direction filter (peak_lag < 0) for naive_xcorr and diff_xcorr. Both methods were counted as forward-significant regardless of peak_lag direction, inflating K values.",
    "fix_applied": true,
    "fix_detail": "Added peak_lag < 0 check for naive_xcorr (.significant) and diff_xcorr (.significant_fdr) in both forward and reverse directions",
    "t20_a045_k3_before": 7,
    "t20_a045_k3_after": 3,
    "t20_a045_k4_before": 3,
    "t20_a045_k4_after": 1,
    "total_rows_with_k3_change": 33,
    "total_rows_with_k4_change": 18,
    "total_rows_with_k5_change": 4,
    "total_field_changes": 138,
    "total_rows": 71
  },
  "registry_cleanup": {
    "experiments_cleaned": 6,
    "fields_removed": ["OLD_robust_pairs", "OLD_perm_granger_fdr", "OLD_diff_xcorr_fdr"],
    "experiments": [
      "generalize_pythia1b_c4_a100_s42",
      "generalize_pythia1b_c4_a100_s43",
      "generalize_pythia14b_wiki_a100_s42",
      "generalize_pythia14b_wiki_a100_s43",
      "generalize_opt1b_wiki_a100_s42",
      "generalize_pythia410m_wiki_a100_s42"
    ],
    "note": "The specific old field names from the task (TY_granger, consensus_k3_3sigma, granger_fdr_sig_count, K_ge3, K_ge4, PermG_fwd, PermG_rev) were not found in the registry. The actual old fields were OLD_* prefixed fields in the 6 generalize experiments. alpha_sweep_a060_s43_fp32 uses intermediate naming (K_gte3_3sigma etc.) which is distinct but not the old format — left as-is.",
    "sample_verification": [
      "generalize_pythia410m_wiki_a100_s42: only new fields (robust_pairs_K3=1/8, ty_forward_sig=1/8)",
      "generalize_opt1b_wiki_a100_s42: only new fields (robust_pairs_K3=2/8, threshold_forward_sig=2/8)",
      "generalize_pythia14b_wiki_a100_s43: only new fields (robust_pairs_K3=7/8, robust_pairs_K4=5/8)",
      "generalize_pythia1b_c4_a100_s42: only new fields (robust_pairs_K3=8/8, robust_pairs_K4=8/8)",
      "generalize_pythia1b_c4_a100_s43: only new fields (robust_pairs_K3=8/8, robust_pairs_K4=7/8)"
    ]
  }
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "csv_fix": {
      "bug_found": true,
      "bug_description": "compile_dose_response.py did not apply D111 direction filter (peak_lag < 0) for naive_xcorr and diff_xcorr. Both methods were counted as forward-significant regardless of peak_lag direction, inflating K values.",
      "fix_applied": true,
      "fix_detail": "Added peak_lag < 0 check for naive_xcorr (.significant) and diff_xcorr (.significant_fdr) in both forward and reverse directions",
      "t20_a045_k3_before": 7,
      "t20_a045_k3_after": 3,
      "t20_a045_k4_before": 3,
      "t20_a045_k4_after": 1,
      "total_rows_with_k3_change": 33,
      "total_rows_with_k4_change": 18,
      "total_rows_with_k5_change": 4,
      "total_field_changes": 138,
      "total_rows": 71
    },
    "registry_cleanup": {
      "experiments_cleaned": 6,
      "fields_removed": [
        "OLD_robust_pairs",
        "OLD_perm_granger_fdr",
        "OLD_diff_xcorr_fdr"
      ],
      "experiments": [
        "generalize_pythia1b_c4_a100_s42",
        "generalize_pythia1b_c4_a100_s43",
        "generalize_pythia14b_wiki_a100_s42",
        "generalize_pythia14b_wiki_a100_s43",
        "generalize_opt1b_wiki_a100_s42",
        "generalize_pythia410m_wiki_a100_s42"
      ],
      "note": "The specific old field names from the task (TY_granger, consensus_k3_3sigma, granger_fdr_sig_count, K_ge3, K_ge4, PermG_fwd, PermG_rev) were not found in the registry. The actual old fields were OLD_* prefixed fields in the 6 generalize experiments. alpha_sweep_a060_s43_fp32 uses intermediate naming (K_gte3_3sigma etc.) which is distinct but not the old format — left as-is.",
      "sample_verification": [
        "generalize_pythia410m_wiki_a100_s42: only new fields (robust_pairs_K3=1/8, ty_forward_sig=1/8)",
        "generalize_opt1b_wiki_a100_s42: only new fields (robust_pairs_K3=2/8, threshold_forward_sig=2/8)",
        "generalize_pythia14b_wiki_a100_s43: only new fields (robust_pairs_K3=7/8, robust_pairs_K4=5/8)",
        "generalize_pythia1b_c4_a100_s42: only new fields (robust_pairs_K3=8/8, robust_pairs_K4=8/8)",
        "generalize_pythia1b_c4_a100_s43: only new fields (robust_pairs_K3=8/8, robust_pairs_K4=7/8)"
      ]
    }
  }
}
```

</details>

---
