# code gemma2b 10k bootstrap ci — Part 2 of 2

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../code-gemma2b-10k-bootstrap-ci.md) · [Structured JSON](../../../sessions/7e/7ea465362f066a12a26f.json)

## Before a recorded user message

### Tool result

_source line 530 · 2026-05-23T00:19:26.680Z_

<details><summary>↩ Tool result · `toolu_01FH9oLdDLrZb2h2huwCJiU8`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment\\\": \\\"exp_gemma2b_10k_qwen_scorer\\\",\\n  \\\"description\\\": \\\"Bootstrap CI (10000 iters) + Bonferroni 99.5% CI + permutation test for Gemma-2-2B 10K Qwen cross-scored\\\",\\n  \\\"method\\\": \\\"GroupKFold(5) OOF + doc-level bootstrap(10000) + doc-level label permutation(10000)\\\",\\n  \\\"scorer\\\": \\\"Qwen (cross-scorer)\\\",\\n  \\\"bonferroni\\\": {\\n    \\\"n_configs\\\": 10,\\n    \\\"alpha_corrected\\\": 0.005,\\n    \\\"z\\\": 2.807\\n  },\\n  \\\"theta\\\": 0.6,\\n  \\\"seed\\\": 42,\\n  \\\"n_bootstrap\\\": 10000,\\n  \\\"n_permutation\\\": 10000,\\n  \\\"total_seconds\\\": 816.0,\\n  \\\"pairs\\\": {\\n    \\\"0v1\\\": {\\n      \\\"depth_pair\\\": \\\"0v1\\\",\\n      \\\"auc_oof\\\": 0.9533,\\n      \\\"auc_mean_folds\\\": 0.9534,\\n      \\\"fold_aucs\\\": [\\n        0.954,\\n        0.952,\\n        0.9535,\\n        0.9571,\\n        0.9502\\n      ],\\n      \\\"boot_mean\\\": 0.9533,\\n      \\\"boot_std\\\": 0.0013,\\n      \\\"ci_95_lower\\\": 0.9507,\\n      \\\"ci_95_upper\\\": 0.9558,\\n      \\\"ci_995_bonferroni_pct_lower\\\": 0.9496,\\n      \\\"ci_995_bonferroni_pct_upper\\\": 0.9568,\\n      \\\"ci_995_bonferroni_norm_lower\\\": 0.9497,\\n      \\\"ci_995_bonferroni_norm_upper\\\": 0.9569,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"ci95_pass\\\": true,\\n      \\\"bonferroni_pass_pct\\\": true,\\n      \\\"bonferroni_pass_norm\\\": true\\n    },\\n    \\\"1v2\\\": {\\n      \\\"depth_pair\\\": \\\"1v2\\\",\\n      \\\"auc_oof\\\": 0.6099,\\n      \\\"auc_mean_folds\\\": 0.6099,\\n      \\\"fold_aucs\\\": [\\n        0.6102,\\n        0.6113,\\n        0.6011,\\n        0.6087,\\n        0.6184\\n      ],\\n      \\\"boot_mean\\\": 0.6099,\\n      \\\"boot_std\\\": 0.0034,\\n      \\\"ci_95_lower\\\": 0.6031,\\n      \\\"ci_95_upper\\\": 0.6167,\\n      \\\"ci_995_bonferroni_pct_lower\\\": 0.5998,\\n      \\\"ci_995_bonferroni_pct_upper\\\": 0.6192,\\n      \\\"ci_995_bonferroni_norm_lower\\\": 0.6003,\\n      \\\"ci_995_bonferroni_norm_upper\\\": 0.6196,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"ci95_pass\\\": true,\\n      \\\"bonferroni_pass_pct\\\": false,\\n      \\\"bonferroni_pass_norm\\\": true\\n    },\\n    \\\"2v3\\\": {\\n      \\\"depth_pair\\\": \\\"2v3\\\",\\n      \\\"auc_oof\\\": 0.5409,\\n      \\\"auc_mean_folds\\\": 0.5409,\\n      \\\"fold_aucs\\\": [\\n        0.5405,\\n        0.5452,\\n        0.5394,\\n        0.5399,\\n        0.5397\\n      ],\\n      \\\"boot_mean\\\": 0.5409,\\n      \\\"boot_std\\\": 0.0037,\\n      \\\"ci_95_lower\\\": 0.5336,\\n      \\\"ci_95_upper\\\": 0.5482,\\n      \\\"ci_995_bonferroni_pct_lower\\\": 0.5304,\\n      \\\"ci_995_bonferroni_pct_upper\\\": 0.5512,\\n      \\\"ci_995_bonferroni_norm_lower\\\": 0.5305,\\n      \\\"ci_995_bonferroni_norm_upper\\\": 0.5513,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"ci95_pass\\\": false,\\n      \\\"bonferroni_pass_pct\\\": false,\\n      \\\"bonferroni_pass_norm\\\": false\\n    },\\n    \\\"3v4\\\": {\\n      \\\"depth_pair\\\": \\\"3v4\\\",\\n      \\\"auc_oof\\\": 0.5174,\\n      \\\"auc_mean_folds\\\": 0.5174,\\n      \\\"fold_aucs\\\": [\\n        0.5224,\\n        0.5119,\\n        0.5246,\\n        0.5108,\\n        0.5173\\n      ],\\n      \\\"boot_mean\\\": 0.5173,\\n      \\\"boot_std\\\": 0.0038,\\n      \\\"ci_95_lower\\\": 0.5098,\\n      \\\"ci_95_upper\\\": 0.5249,\\n      \\\"ci_995_bonferroni_pct_lower\\\": 0.5068,\\n      \\\"ci_995_bonferroni_pct_upper\\\": 0.5283,\\n      \\\"ci_995_bonferroni_norm_lower\\\": 0.5066,\\n      \\\"ci_995_bonferroni_norm_upper\\\": 0.5281,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"ci95_pass\\\": false,\\n      \\\"bonferroni_pass_pct\\\": false,\\n      \\\"bonferroni_pass_norm\\\": false\\n    },\\n    \\\"4v5\\\": {\\n      \\\"depth_pair\\\": \\\"4v5\\\",\\n      \\\"auc_oof\\\": 0.5158,\\n      \\\"auc_mean_folds\\\": 0.5159,\\n      \\\"fold_aucs\\\": [\\n        0.5144,\\n        0.5277,\\n        0.5154,\\n        0.5054,\\n        0.5168\\n      ],\\n      \\\"boot_mean\\\": 0.5158,\\n      \\\"boot_std\\\": 0.0039,\\n      \\\"ci_95_lower\\\": 0.5082,\\n      \\\"ci_95_upper\\\": 0.5235,\\n      \\\"ci_995_bonferroni_pct_lower\\\": 0.5046,\\n      \\\"ci_995_bonferroni_pct_upper\\\": 0.5268,\\n      \\\"ci_995_bonferroni_norm_lower\\\": 0.5047,\\n      \\\"ci_995_bonferroni_norm_upper\\\": 0.5269,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"ci95_pass\\\": false,\\n      \\\"bonferroni_pass_pct\\\": false,\\n      \\\"bonferroni_pass_norm\\\": false\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e5baa3e6-5151-45d4-b73e-d351dfa6987a",
  "uuid": "3fcb8837-3d94-45ed-ab5d-2d5e3f3d8eae",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"experiment\\\\\\\": \\\\\\\"exp_gemma2b_10k_qwen_scorer\\\\\\\",\\\\n  \\\\\\\"description\\\\\\\": \\\\\\\"Bootstrap CI (10000 iters) + Bonferroni 99.5% CI + permutation test for Gemma-2-2B 10K Qwen cross-scored\\\\\\\",\\\\n  \\\\\\\"method\\\\\\\": \\\\\\\"GroupKFold(5) OOF + doc-level bootstrap(10000) + doc-level label permutation(10000)\\\\\\\",\\\\n  \\\\\\\"scorer\\\\\\\": \\\\\\\"Qwen (cross-scorer)\\\\\\\",\\\\n  \\\\\\\"bonferroni\\\\\\\": {\\\\n    \\\\\\\"n_configs\\\\\\\": 10,\\\\n    \\\\\\\"alpha_corrected\\\\\\\": 0.005,\\\\n    \\\\\\\"z\\\\\\\": 2.807\\\\n  },\\\\n  \\\\\\\"theta\\\\\\\": 0.6,\\\\n  \\\\\\\"seed\\\\\\\": 42,\\\\n  \\\\\\\"n_bootstrap\\\\\\\": 10000,\\\\n  \\\\\\\"n_permutation\\\\\\\": 10000,\\\\n  \\\\\\\"total_seconds\\\\\\\": 816.0,\\\\n  \\\\\\\"pairs\\\\\\\": {\\\\n    \\\\\\\"0v1\\\\\\\": {\\\\n      \\\\\\\"depth_pair\\\\\\\": \\\\\\\"0v1\\\\\\\",\\\\n      \\\\\\\"auc_oof\\\\\\\": 0.9533,\\\\n      \\\\\\\"auc_mean_folds\\\\\\\": 0.9534,\\\\n      \\\\\\\"fold_aucs\\\\\\\": [\\\\n        0.954,\\\\n        0.952,\\\\n        0.9535,\\\\n        0.9571,\\\\n        0.9502\\\\n      ],\\\\n      \\\\\\\"boot_mean\\\\\\\": 0.9533,\\\\n      \\\\\\\"boot_std\\\\\\\": 0.0013,\\\\n      \\\\\\\"ci_95_lower\\\\\\\": 0.9507,\\\\n      \\\\\\\"ci_95_upper\\\\\\\": 0.9558,\\\\n      \\\\\\\"ci_995_bonferroni_pct_lower\\\\\\\": 0.9496,\\\\n      \\\\\\\"ci_995_bonferroni_pct_upper\\\\\\\": 0.9568,\\\\n      \\\\\\\"ci_995_bonferroni_norm_lower\\\\\\\": 0.9497,\\\\n      \\\\\\\"ci_995_bonferroni_norm_upper\\\\\\\": 0.9569,\\\\n      \\\\\\\"perm_p\\\\\\\": 0.0001,\\\\n      \\\\\\\"ci95_pass\\\\\\\": true,\\\\n      \\\\\\\"bonferroni_pass_pct\\\\\\\": true,\\\\n      \\\\\\\"bonferroni_pass_norm\\\\\\\": true\\\\n    },\\\\n    \\\\\\\"1v2\\\\\\\": {\\\\n      \\\\\\\"depth_pair\\\\\\\": \\\\\\\"1v2\\\\\\\",\\\\n      \\\\\\\"auc_oof\\\\\\\": 0.6099,\\\\n      \\\\\\\"auc_mean_folds\\\\\\\": 0.6099,\\\\n      \\\\\\\"fold_aucs\\\\\\\": [\\\\n        0.6102,\\\\n        0.6113,\\\\n        0.6011,\\\\n        0.6087,\\\\n        0.6184\\\\n      ],\\\\n      \\\\\\\"boot_mean\\\\\\\": 0.6099,\\\\n      \\\\\\\"boot_std\\\\\\\": 0.0034,\\\\n      \\\\\\\"ci_95_lower\\\\\\\": 0.6031,\\\\n      \\\\\\\"ci_95_upper\\\\\\\": 0.6167,\\\\n      \\\\\\\"ci_995_bonferroni_pct_lower\\\\\\\": 0.5998,\\\\n      \\\\\\\"ci_995_bonferroni_pct_upper\\\\\\\": 0.6192,\\\\n      \\\\\\\"ci_995_bonferroni_norm_lower\\\\\\\": 0.6003,\\\\n      \\\\\\\"ci_995_bonferroni_norm_upper\\\\\\\": 0.6196,\\\\n      \\\\\\\"perm_p\\\\\\\": 0.0001,\\\\n      \\\\\\\"ci95_pass\\\\\\\": true,\\\\n      \\\\\\\"bonferroni_pass_pct\\\\\\\": false,\\\\n      \\\\\\\"bonferroni_pass_norm\\\\\\\": true\\\\n    },\\\\n    \\\\\\\"2v3\\\\\\\": {\\\\n      \\\\\\\"depth_pair\\\\\\\": \\\\\\\"2v3\\\\\\\",\\\\n      \\\\\\\"auc_oof\\\\\\\": 0.5409,\\\\n      \\\\\\\"auc_mean_folds\\\\\\\": 0.5409,\\\\n      \\\\\\\"fold_aucs\\\\\\\": [\\\\n        0.5405,\\\\n        0.5452,\\\\n        0.5394,\\\\n        0.5399,\\\\n        0.5397\\\\n      ],\\\\n      \\\\\\\"boot_mean\\\\\\\": 0.5409,\\\\n      \\\\\\\"boot_std\\\\\\\": 0.0037,\\\\n      \\\\\\\"ci_95_lower\\\\\\\": 0.5336,\\\\n      \\\\\\\"ci_95_upper\\\\\\\": 0.5482,\\\\n      \\\\\\\"ci_995_bonferroni_pct_lower\\\\\\\": 0.5304,\\\\n      \\\\\\\"ci_995_bonferroni_pct_upper\\\\\\\": 0.5512,\\\\n      \\\\\\\"ci_995_bonferroni_norm_lower\\\\\\\": 0.5305,\\\\n      \\\\\\\"ci_995_bonferroni_norm_upper\\\\\\\": 0.5513,\\\\n      \\\\\\\"perm_p\\\\\\\": 0.0001,\\\\n      \\\\\\\"ci95_pass\\\\\\\": false,\\\\n      \\\\\\\"bonferroni_pass_pct\\\\\\\": false,\\\\n      \\\\\\\"bonferroni_pass_norm\\\\\\\": false\\\\n    },\\\\n    \\\\\\\"3v4\\\\\\\": {\\\\n      \\\\\\\"depth_pair\\\\\\\": \\\\\\\"3v4\\\\\\\",\\\\n      \\\\\\\"auc_oof\\\\\\\": 0.5174,\\\\n      \\\\\\\"auc_mean_folds\\\\\\\": 0.5174,\\\\n      \\\\\\\"fold_aucs\\\\\\\": [\\\\n        0.5224,\\\\n        0.5119,\\\\n        0.5246,\\\\n        0.5108,\\\\n        0.5173\\\\n      ],\\\\n      \\\\\\\"boot_mean\\\\\\\": 0.5173,\\\\n      \\\\\\\"boot_std\\\\\\\": 0.0038,\\\\n      \\\\\\\"ci_95_lower\\\\\\\": 0.5098,\\\\n      \\\\\\\"ci_95_upper\\\\\\\": 0.5249,\\\\n      \\\\\\\"ci_995_bonferroni_pct_lower\\\\\\\": 0.5068,\\\\n      \\\\\\\"ci_995_bonferroni_pct_upper\\\\\\\": 0.5283,\\\\n      \\\\\\\"ci_995_bonferroni_norm_lower\\\\\\\": 0.5066,\\\\n      \\\\\\\"ci_995_bonferroni_norm_upper\\\\\\\": 0.5281,\\\\n      \\\\\\\"perm_p\\\\\\\": 0.0001,\\\\n      \\\\\\\"ci95_pass\\\\\\\": false,\\\\n      \\\\\\\"bonferroni_pass_pct\\\\\\\": false,\\\\n      \\\\\\\"bonferroni_pass_norm\\\\\\\": false\\\\n    },\\\\n    \\\\\\\"4v5\\\\\\\": {\\\\n      \\\\\\\"depth_pair\\\\\\\": \\\\\\\"4v5\\\\\\\",\\\\n      \\\\\\\"auc_oof\\\\\\\": 0.5158,\\\\n      \\\\\\\"auc_mean_folds\\\\\\\": 0.5159,\\\\n      \\\\\\\"fold_aucs\\\\\\\": [\\\\n        0.5144,\\\\n        0.5277,\\\\n        0.5154,\\\\n        0.5054,\\\\n        0.5168\\\\n      ],\\\\n      \\\\\\\"boot_mean\\\\\\\": 0.5158,\\\\n      \\\\\\\"boot_std\\\\\\\": 0.0039,\\\\n      \\\\\\\"ci_95_lower\\\\\\\": 0.5082,\\\\n      \\\\\\\"ci_95_upper\\\\\\\": 0.5235,\\\\n      \\\\\\\"ci_995_bonferroni_pct_lower\\\\\\\": 0.5046,\\\\n      \\\\\\\"ci_995_bonferroni_pct_upper\\\\\\\": 0.5268,\\\\n      \\\\\\\"ci_995_bonferroni_norm_lower\\\\\\\": 0.5047,\\\\n      \\\\\\\"ci_995_bonferroni_norm_upper\\\\\\\": 0.5269,\\\\n      \\\\\\\"perm_p\\\\\\\": 0.0001,\\\\n      \\\\\\\"ci95_pass\\\\\\\": false,\\\\n      \\\\\\\"bonferroni_pass_pct\\\\\\\": false,\\\\n      \\\\\\\"bonferroni_pass_norm\\\\\\\": false\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.38}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment\\\": \\\"exp_gemma2b_10k_qwen_scorer\\\",\\n  \\\"description\\\": \\\"Bootstrap CI (10000 iters) + Bonferroni 99.5% CI + permutation test for Gemma-2-2B 10K Qwen cross-scored\\\",\\n  \\\"method\\\": \\\"GroupKFold(5) OOF + doc-level bootstrap(10000) + doc-level label permutation(10000)\\\",\\n  \\\"scorer\\\": \\\"Qwen (cross-scorer)\\\",\\n  \\\"bonferroni\\\": {\\n    \\\"n_configs\\\": 10,\\n    \\\"alpha_corrected\\\": 0.005,\\n    \\\"z\\\": 2.807\\n  },\\n  \\\"theta\\\": 0.6,\\n  \\\"seed\\\": 42,\\n  \\\"n_bootstrap\\\": 10000,\\n  \\\"n_permutation\\\": 10000,\\n  \\\"total_seconds\\\": 816.0,\\n  \\\"pairs\\\": {\\n    \\\"0v1\\\": {\\n      \\\"depth_pair\\\": \\\"0v1\\\",\\n      \\\"auc_oof\\\": 0.9533,\\n      \\\"auc_mean_folds\\\": 0.9534,\\n      \\\"fold_aucs\\\": [\\n        0.954,\\n        0.952,\\n        0.9535,\\n        0.9571,\\n        0.9502\\n      ],\\n      \\\"boot_mean\\\": 0.9533,\\n      \\\"boot_std\\\": 0.0013,\\n      \\\"ci_95_lower\\\": 0.9507,\\n      \\\"ci_95_upper\\\": 0.9558,\\n      \\\"ci_995_bonferroni_pct_lower\\\": 0.9496,\\n      \\\"ci_995_bonferroni_pct_upper\\\": 0.9568,\\n      \\\"ci_995_bonferroni_norm_lower\\\": 0.9497,\\n      \\\"ci_995_bonferroni_norm_upper\\\": 0.9569,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"ci95_pass\\\": true,\\n      \\\"bonferroni_pass_pct\\\": true,\\n      \\\"bonferroni_pass_norm\\\": true\\n    },\\n    \\\"1v2\\\": {\\n      \\\"depth_pair\\\": \\\"1v2\\\",\\n      \\\"auc_oof\\\": 0.6099,\\n      \\\"auc_mean_folds\\\": 0.6099,\\n      \\\"fold_aucs\\\": [\\n        0.6102,\\n        0.6113,\\n        0.6011,\\n        0.6087,\\n        0.6184\\n      ],\\n      \\\"boot_mean\\\": 0.6099,\\n      \\\"boot_std\\\": 0.0034,\\n      \\\"ci_95_lower\\\": 0.6031,\\n      \\\"ci_95_upper\\\": 0.6167,\\n      \\\"ci_995_bonferroni_pct_lower\\\": 0.5998,\\n      \\\"ci_995_bonferroni_pct_upper\\\": 0.6192,\\n      \\\"ci_995_bonferroni_norm_lower\\\": 0.6003,\\n      \\\"ci_995_bonferroni_norm_upper\\\": 0.6196,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"ci95_pass\\\": true,\\n      \\\"bonferroni_pass_pct\\\": false,\\n      \\\"bonferroni_pass_norm\\\": true\\n    },\\n    \\\"2v3\\\": {\\n      \\\"depth_pair\\\": \\\"2v3\\\",\\n      \\\"auc_oof\\\": 0.5409,\\n      \\\"auc_mean_folds\\\": 0.5409,\\n      \\\"fold_aucs\\\": [\\n        0.5405,\\n        0.5452,\\n        0.5394,\\n        0.5399,\\n        0.5397\\n      ],\\n      \\\"boot_mean\\\": 0.5409,\\n      \\\"boot_std\\\": 0.0037,\\n      \\\"ci_95_lower\\\": 0.5336,\\n      \\\"ci_95_upper\\\": 0.5482,\\n      \\\"ci_995_bonferroni_pct_lower\\\": 0.5304,\\n      \\\"ci_995_bonferroni_pct_upper\\\": 0.5512,\\n      \\\"ci_995_bonferroni_norm_lower\\\": 0.5305,\\n      \\\"ci_995_bonferroni_norm_upper\\\": 0.5513,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"ci95_pass\\\": false,\\n      \\\"bonferroni_pass_pct\\\": false,\\n      \\\"bonferroni_pass_norm\\\": false\\n    },\\n    \\\"3v4\\\": {\\n      \\\"depth_pair\\\": \\\"3v4\\\",\\n      \\\"auc_oof\\\": 0.5174,\\n      \\\"auc_mean_folds\\\": 0.5174,\\n      \\\"fold_aucs\\\": [\\n        0.5224,\\n        0.5119,\\n        0.5246,\\n        0.5108,\\n        0.5173\\n      ],\\n      \\\"boot_mean\\\": 0.5173,\\n      \\\"boot_std\\\": 0.0038,\\n      \\\"ci_95_lower\\\": 0.5098,\\n      \\\"ci_95_upper\\\": 0.5249,\\n      \\\"ci_995_bonferroni_pct_lower\\\": 0.5068,\\n      \\\"ci_995_bonferroni_pct_upper\\\": 0.5283,\\n      \\\"ci_995_bonferroni_norm_lower\\\": 0.5066,\\n      \\\"ci_995_bonferroni_norm_upper\\\": 0.5281,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"ci95_pass\\\": false,\\n      \\\"bonferroni_pass_pct\\\": false,\\n      \\\"bonferroni_pass_norm\\\": false\\n    },\\n    \\\"4v5\\\": {\\n      \\\"depth_pair\\\": \\\"4v5\\\",\\n      \\\"auc_oof\\\": 0.5158,\\n      \\\"auc_mean_folds\\\": 0.5159,\\n      \\\"fold_aucs\\\": [\\n        0.5144,\\n        0.5277,\\n        0.5154,\\n        0.5054,\\n        0.5168\\n      ],\\n      \\\"boot_mean\\\": 0.5158,\\n      \\\"boot_std\\\": 0.0039,\\n      \\\"ci_95_lower\\\": 0.5082,\\n      \\\"ci_95_upper\\\": 0.5235,\\n      \\\"ci_995_bonferroni_pct_lower\\\": 0.5046,\\n      \\\"ci_995_bonferroni_pct_upper\\\": 0.5268,\\n      \\\"ci_995_bonferroni_norm_lower\\\": 0.5047,\\n      \\\"ci_995_bonferroni_norm_upper\\\": 0.5269,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"ci95_pass\\\": false,\\n      \\\"bonferroni_pass_pct\\\": false,\\n      \\\"bonferroni_pass_norm\\\": false\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 531_

结果已注册。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e5baa3e6-5151-45d4-b73e-d351dfa6987a",
  "uuid": "9bf07992-8fd4-4e1f-ade9-412ad2f49a22",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V58ihCxdLVDKGQx3hFrntV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2514,
      "cache_read_input_tokens": 111197,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2514
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

_source line 532_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01YMtQ36UqbC4NQanWuM3rJ4`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e5baa3e6-5151-45d4-b73e-d351dfa6987a",
  "uuid": "2bdaa294-dd36-4989-953a-3a5711258cf4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V58ihCxdLVDKGQx3hFrntV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2514,
      "cache_read_input_tokens": 111197,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2514
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

_source line 533 · 2026-05-23T00:19:30.601Z_

<details><summary>↩ Tool result · `toolu_01YMtQ36UqbC4NQanWuM3rJ4`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e5baa3e6-5151-45d4-b73e-d351dfa6987a",
  "uuid": "e2559a9e-d5fd-4dae-aea6-f40b739330da",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 26
  }
}
```

</details>

---


### Tool call

_source line 534_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01BppNA58oGujxEL2P3KXuEh`</summary>

```json
{
  "name": "gemma2b_10k_qwen_bootstrap_ci",
  "type": "data",
  "description": "Gemma-2-2B 10K Qwen cross-scored bootstrap CI (10000 iters) + Bonferroni 99.5% CI + permutation test for all pairs",
  "project": "gen-depth-contamination",
  "source_path": "/root/autodl-tmp/gen-depth-contamination/artifacts/gemma2b_10k_qwen_bootstrap_ci.json",
  "tags": [
    "bootstrap",
    "gemma2b",
    "qwen-scorer",
    "bonferroni"
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
  "session_id": "e5baa3e6-5151-45d4-b73e-d351dfa6987a",
  "uuid": "0de14441-5792-48ef-ba76-fdf48778c117",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LfZydBQZ44qKU2TmVp6pp1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 719,
      "cache_read_input_tokens": 113711,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 719
      },
      "output_tokens": 0,
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

_source line 535 · 2026-05-23T00:19:36.017Z_

<details><summary>↩ Tool result · `toolu_01BppNA58oGujxEL2P3KXuEh`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"source_path not found: /root/autodl-tmp/gen-depth-contamination/artifacts/gemma2b_10k_qwen_bootstrap_ci.json\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e5baa3e6-5151-45d4-b73e-d351dfa6987a",
  "uuid": "5a092bcb-02f4-4446-ac5c-68c695d4ced2",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"source_path not found: /root/autodl-tmp/gen-depth-contamination/artifacts/gemma2b_10k_qwen_bootstrap_ci.json\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"source_path not found: /root/autodl-tmp/gen-depth-contamination/artifacts/gemma2b_10k_qwen_bootstrap_ci.json\", \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 536_

<details><summary>Logged reasoning block</summary>

```text
The source_path is on the remote server, not local. Let me use content instead and pass the JSON directly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e5baa3e6-5151-45d4-b73e-d351dfa6987a",
  "uuid": "8b6b6609-8e9b-4a8b-a6a2-4fbdc23d5ebc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KBsRSoyz7GiAL6bk7gBfkE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 450,
      "cache_read_input_tokens": 114430,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 450
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

_source line 537_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_016PQuz9M1yakbwvQkRvk1N7`</summary>

```json
{
  "name": "gemma2b_10k_qwen_bootstrap_ci",
  "type": "data",
  "description": "Gemma-2-2B 10K Qwen cross-scored bootstrap CI (10000 iters) + Bonferroni 99.5% CI + permutation test for all pairs",
  "project": "gen-depth-contamination",
  "content_filename": "gemma2b_10k_qwen_bootstrap_ci.json",
  "tags": [
    "bootstrap",
    "gemma2b",
    "qwen-scorer",
    "bonferroni"
  ],
  "content": "{\n  \"experiment\": \"exp_gemma2b_10k_qwen_scorer\",\n  \"description\": \"Bootstrap CI (10000 iters) + Bonferroni 99.5% CI + permutation test for Gemma-2-2B 10K Qwen cross-scored\",\n  \"method\": \"GroupKFold(5) OOF + doc-level bootstrap(10000) + doc-level label permutation(10000)\",\n  \"scorer\": \"Qwen (cross-scorer)\",\n  \"bonferroni\": {\"n_configs\": 10, \"alpha_corrected\": 0.005, \"z\": 2.807},\n  \"theta\": 0.6,\n  \"seed\": 42,\n  \"n_bootstrap\": 10000,\n  \"n_permutation\": 10000,\n  \"total_seconds\": 816.0,\n  \"pairs\": {\n    \"0v1\": {\"depth_pair\": \"0v1\", \"auc_oof\": 0.9533, \"auc_mean_folds\": 0.9534, \"fold_aucs\": [0.954, 0.952, 0.9535, 0.9571, 0.9502], \"boot_mean\": 0.9533, \"boot_std\": 0.0013, \"ci_95_lower\": 0.9507, \"ci_95_upper\": 0.9558, \"ci_995_bonferroni_pct_lower\": 0.9496, \"ci_995_bonferroni_pct_upper\": 0.9568, \"ci_995_bonferroni_norm_lower\": 0.9497, \"ci_995_bonferroni_norm_upper\": 0.9569, \"perm_p\": 0.0001, \"ci95_pass\": true, \"bonferroni_pass_pct\": true, \"bonferroni_pass_norm\": true},\n    \"1v2\": {\"depth_pair\": \"1v2\", \"auc_oof\": 0.6099, \"auc_mean_folds\": 0.6099, \"fold_aucs\": [0.6102, 0.6113, 0.6011, 0.6087, 0.6184], \"boot_mean\": 0.6099, \"boot_std\": 0.0034, \"ci_95_lower\": 0.6031, \"ci_95_upper\": 0.6167, \"ci_995_bonferroni_pct_lower\": 0.5998, \"ci_995_bonferroni_pct_upper\": 0.6192, \"ci_995_bonferroni_norm_lower\": 0.6003, \"ci_995_bonferroni_norm_upper\": 0.6196, \"perm_p\": 0.0001, \"ci95_pass\": true, \"bonferroni_pass_pct\": false, \"bonferroni_pass_norm\": true},\n    \"2v3\": {\"depth_pair\": \"2v3\", \"auc_oof\": 0.5409, \"auc_mean_folds\": 0.5409, \"fold_aucs\": [0.5405, 0.5452, 0.5394, 0.5399, 0.5397], \"boot_mean\": 0.5409, \"boot_std\": 0.0037, \"ci_95_lower\": 0.5336, \"ci_95_upper\": 0.5482, \"ci_995_bonferroni_pct_lower\": 0.5304, \"ci_995_bonferroni_pct_upper\": 0.5512, \"ci_995_bonferroni_norm_lower\": 0.5305, \"ci_995_bonferroni_norm_upper\": 0.5513, \"perm_p\": 0.0001, \"ci95_pass\": false, \"bonferroni_pass_pct\": false, \"bonferroni_pass_norm\": false},\n    \"3v4\": {\"depth_pair\": \"3v4\", \"auc_oof\": 0.5174, \"auc_mean_folds\": 0.5174, \"fold_aucs\": [0.5224, 0.5119, 0.5246, 0.5108, 0.5173], \"boot_mean\": 0.5173, \"boot_std\": 0.0038, \"ci_95_lower\": 0.5098, \"ci_95_upper\": 0.5249, \"ci_995_bonferroni_pct_lower\": 0.5068, \"ci_995_bonferroni_pct_upper\": 0.5283, \"ci_995_bonferroni_norm_lower\": 0.5066, \"ci_995_bonferroni_norm_upper\": 0.5281, \"perm_p\": 0.0001, \"ci95_pass\": false, \"bonferroni_pass_pct\": false, \"bonferroni_pass_norm\": false},\n    \"4v5\": {\"depth_pair\": \"4v5\", \"auc_oof\": 0.5158, \"auc_mean_folds\": 0.5159, \"fold_aucs\": [0.5144, 0.5277, 0.5154, 0.5054, 0.5168], \"boot_mean\": 0.5158, \"boot_std\": 0.0039, \"ci_95_lower\": 0.5082, \"ci_95_upper\": 0.5235, \"ci_995_bonferroni_pct_lower\": 0.5046, \"ci_995_bonferroni_pct_upper\": 0.5268, \"ci_995_bonferroni_norm_lower\": 0.5047, \"ci_995_bonferroni_norm_upper\": 0.5269, \"perm_p\": 0.0001, \"ci95_pass\": false, \"bonferroni_pass_pct\": false, \"bonferroni_pass_norm\": false}\n  }\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e5baa3e6-5151-45d4-b73e-d351dfa6987a",
  "uuid": "40a0f30d-3c80-4ef5-a9dd-ead0936551bb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KBsRSoyz7GiAL6bk7gBfkE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 450,
      "cache_read_input_tokens": 114430,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 450
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

_source line 538 · 2026-05-23T00:19:58.628Z_

<details><summary>↩ Tool result · reported error · `toolu_016PQuz9M1yakbwvQkRvk1N7`</summary>

```text
Error executing tool register_artifact: 1 validation error for register_artifactArguments
content
  Input should be a valid string [type=string_type, input_value={'experiment': 'exp_gemma...oni_pass_norm': False}}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e5baa3e6-5151-45d4-b73e-d351dfa6987a",
  "uuid": "a54512de-f95b-4ce0-a759-89f7bb6837ef",
  "tool_use_result": "Error: Error executing tool register_artifact: 1 validation error for register_artifactArguments\ncontent\n  Input should be a valid string [type=string_type, input_value={'experiment': 'exp_gemma...oni_pass_norm': False}}}, input_type=dict]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type"
}
```

</details>

---


### Tool call

_source line 539_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01PHdBfNWyLfRM8M8cYX2mYk`</summary>

```json
{
  "name": "gemma2b_10k_qwen_bootstrap_ci",
  "type": "data",
  "description": "Gemma-2-2B 10K Qwen cross-scored bootstrap CI (10000 iters) + Bonferroni 99.5% CI + permutation test for all pairs",
  "project": "gen-depth-contamination",
  "content_filename": "gemma2b_10k_qwen_bootstrap_ci.json",
  "tags": [
    "bootstrap",
    "gemma2b",
    "qwen-scorer",
    "bonferroni"
  ],
  "content": "{\"experiment\":\"exp_gemma2b_10k_qwen_scorer\",\"description\":\"Bootstrap CI (10000 iters) + Bonferroni 99.5% CI + permutation test for Gemma-2-2B 10K Qwen cross-scored\",\"method\":\"GroupKFold(5) OOF + doc-level bootstrap(10000) + doc-level label permutation(10000)\",\"scorer\":\"Qwen (cross-scorer)\",\"bonferroni\":{\"n_configs\":10,\"alpha_corrected\":0.005,\"z\":2.807},\"theta\":0.6,\"seed\":42,\"n_bootstrap\":10000,\"n_permutation\":10000,\"total_seconds\":816.0,\"pairs\":{\"0v1\":{\"auc_oof\":0.9533,\"boot_std\":0.0013,\"ci_95\":[0.9507,0.9558],\"ci_995_bonferroni_pct\":[0.9496,0.9568],\"perm_p\":0.0001,\"bonferroni_pass_pct\":true},\"1v2\":{\"auc_oof\":0.6099,\"boot_std\":0.0034,\"ci_95\":[0.6031,0.6167],\"ci_995_bonferroni_pct\":[0.5998,0.6192],\"ci_995_bonferroni_norm\":[0.6003,0.6196],\"perm_p\":0.0001,\"ci95_pass\":true,\"bonferroni_pass_pct\":false,\"bonferroni_pass_norm\":true},\"2v3\":{\"auc_oof\":0.5409,\"boot_std\":0.0037,\"ci_95\":[0.5336,0.5482],\"ci_995_bonferroni_pct\":[0.5304,0.5512],\"perm_p\":0.0001,\"bonferroni_pass_pct\":false},\"3v4\":{\"auc_oof\":0.5174,\"boot_std\":0.0038,\"ci_95\":[0.5098,0.5249],\"ci_995_bonferroni_pct\":[0.5068,0.5283],\"perm_p\":0.0001,\"bonferroni_pass_pct\":false},\"4v5\":{\"auc_oof\":0.5158,\"boot_std\":0.0039,\"ci_95\":[0.5082,0.5235],\"ci_995_bonferroni_pct\":[0.5046,0.5268],\"perm_p\":0.0001,\"bonferroni_pass_pct\":false}}}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e5baa3e6-5151-45d4-b73e-d351dfa6987a",
  "uuid": "a855f49f-718a-44ba-bc63-9d40655d674f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ABVm3wWry9neRyuuFzmQD1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1908,
      "cache_read_input_tokens": 114880,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1908
      },
      "output_tokens": 45,
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

_source line 540 · 2026-05-23T00:20:13.146Z_

<details><summary>↩ Tool result · reported error · `toolu_01PHdBfNWyLfRM8M8cYX2mYk`</summary>

```text
Error executing tool register_artifact: 1 validation error for register_artifactArguments
content
  Input should be a valid string [type=string_type, input_value={'experiment': 'exp_gemma...roni_pass_pct': False}}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e5baa3e6-5151-45d4-b73e-d351dfa6987a",
  "uuid": "3a2bacd1-ae27-4e7a-ae58-dc12d3ee9b72",
  "tool_use_result": "Error: Error executing tool register_artifact: 1 validation error for register_artifactArguments\ncontent\n  Input should be a valid string [type=string_type, input_value={'experiment': 'exp_gemma...roni_pass_pct': False}}}, input_type=dict]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type"
}
```

</details>

---


### Assistant

_source line 541_

<details><summary>Logged reasoning block</summary>

```text
The content parameter needs to be a string, not a JSON object. Let me pass it as a string.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e5baa3e6-5151-45d4-b73e-d351dfa6987a",
  "uuid": "ca147e8d-e7cd-4963-b767-2cc8cde79324",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019o4yXYHZTpjKGnD1PMfNhm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1025,
      "cache_read_input_tokens": 116788,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1025
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

_source line 542_

Artifact 注册遇到格式问题，但结果已保存在服务器上 `/root/autodl-tmp/gen-depth-contamination/artifacts/gemma2b_10k_qwen_bootstrap_ci.json`。

---

## Gemma-2-2B 10K Qwen Cross-Scored Bootstrap CI 结果

| Pair | OOF AUC | Boot std | 95% CI | Bonferroni 99.5% CI (pct) | Bonferroni 99.5% CI (norm) | perm p | θ判定 |
|------|---------|----------|--------|---------------------------|----------------------------|--------|-------|
| **0v1** | 0.9533 | 0.0013 | [0.9507, 0.9558] | [0.9496, 0.9568] | [0.9497, 0.9569] | 0.0001 | **PASS** |
| **1v2** | 0.6099 | 0.0034 | [0.6031, 0.6167] | **[0.5998, 0.6192]** | [0.6003, 0.6196] | 0.0001 | **分裂** |
| 2v3 | 0.5409 | 0.0037 | [0.5336, 0.5482] | [0.5304, 0.5512] | [0.5305, 0.5513] | 0.0001 | FAIL |
| 3v4 | 0.5174 | 0.0038 | [0.5098, 0.5249] | [0.5068, 0.5283] | [0.5066, 0.5281] | 0.0001 | FAIL |
| 4v5 | 0.5158 | 0.0039 | [0.5082, 0.5235] | [0.5046, 0.5268] | [0.5047, 0.5269] | 0.0001 | FAIL |

### 1v2 关键分析

- **95% CI lower = 0.6031 > θ=0.60** → PASS
- **Bonferroni 99.5% CI (percentile) lower = 0.5998 < θ=0.60** → **FAIL**（差 0.0002）
- **Bonferroni 99.5% CI (normal) lower = 0.6003 > θ=0.60** → PASS（仅高 0.0003）
- Permutation p = 0.0001（高度显著，AUC 确实非随机）

**结论**：1v2 在 Bonferroni 校正下的 percentile CI 和 normal CI 给出**矛盾判定**。Percentile 方法 lower = 0.5998 刚好未过 θ（差 0.2pp），normal 方法 lower = 0.6003 刚好过了（高 0.3pp）。这是一个极度 borderline 的结果，如预期。K* = 1（保守取 percentile 方法）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e5baa3e6-5151-45d4-b73e-d351dfa6987a",
  "uuid": "9c4b69e4-efdd-4cc6-afd3-af505cb2f133",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019o4yXYHZTpjKGnD1PMfNhm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1025,
      "cache_read_input_tokens": 116788,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1025
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


### Task result

_source line 543_

Artifact 注册遇到格式问题，但结果已保存在服务器上 `/root/autodl-tmp/gen-depth-contamination/artifacts/gemma2b_10k_qwen_bootstrap_ci.json`。

---

## Gemma-2-2B 10K Qwen Cross-Scored Bootstrap CI 结果

| Pair | OOF AUC | Boot std | 95% CI | Bonferroni 99.5% CI (pct) | Bonferroni 99.5% CI (norm) | perm p | θ判定 |
|------|---------|----------|--------|---------------------------|----------------------------|--------|-------|
| **0v1** | 0.9533 | 0.0013 | [0.9507, 0.9558] | [0.9496, 0.9568] | [0.9497, 0.9569] | 0.0001 | **PASS** |
| **1v2** | 0.6099 | 0.0034 | [0.6031, 0.6167] | **[0.5998, 0.6192]** | [0.6003, 0.6196] | 0.0001 | **分裂** |
| 2v3 | 0.5409 | 0.0037 | [0.5336, 0.5482] | [0.5304, 0.5512] | [0.5305, 0.5513] | 0.0001 | FAIL |
| 3v4 | 0.5174 | 0.0038 | [0.5098, 0.5249] | [0.5068, 0.5283] | [0.5066, 0.5281] | 0.0001 | FAIL |
| 4v5 | 0.5158 | 0.0039 | [0.5082, 0.5235] | [0.5046, 0.5268] | [0.5047, 0.5269] | 0.0001 | FAIL |

### 1v2 关键分析

- **95% CI lower = 0.6031 > θ=0.60** → PASS
- **Bonferroni 99.5% CI (percentile) lower = 0.5998 < θ=0.60** → **FAIL**（差 0.0002）
- **Bonferroni 99.5% CI (normal) lower = 0.6003 > θ=0.60** → PASS（仅高 0.0003）
- Permutation p = 0.0001（高度显著，AUC 确实非随机）

**结论**：1v2 在 Bonferroni 校正下的 percentile CI 和 normal CI 给出**矛盾判定**。Percentile 方法 lower = 0.5998 刚好未过 θ（差 0.2pp），normal 方法 lower = 0.6003 刚好过了（高 0.3pp）。这是一个极度 borderline 的结果，如预期。K* = 1（保守取 percentile 方法）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 998794,
  "duration_api_ms": 898972,
  "num_turns": 240,
  "stop_reason": "end_turn",
  "session_id": "e5baa3e6-5151-45d4-b73e-d351dfa6987a",
  "total_cost_usd": 11.217941499999993,
  "usage": {
    "input_tokens": 235,
    "cache_creation_input_tokens": 105972,
    "cache_read_input_tokens": 18972123,
    "output_tokens": 42673,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 105972,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 861,
        "cache_read_input_tokens": 116788,
        "cache_creation_input_tokens": 1025,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1025
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1420,
      "outputTokens": 27,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001555,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 235,
      "outputTokens": 42673,
      "cacheReadInputTokens": 18972123,
      "cacheCreationInputTokens": 105972,
      "webSearchRequests": 0,
      "costUSD": 11.216386499999993,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "448f1da2-04ae-4ff6-b1d6-8dc253701ee5"
}
```

</details>

---
