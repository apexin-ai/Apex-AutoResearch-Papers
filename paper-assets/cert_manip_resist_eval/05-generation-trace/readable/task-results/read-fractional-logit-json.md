# read fractional logit json

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_read_fractional-logit-json_20260523T074634_result.json`
- **Structured JSON:** [`fabbea45105a2288cc78.json`](../../sessions/fa/fabbea45105a2288cc78.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件名是 `fractional_logit.json`（非 `fractional_logit_results.json`）。内容如下（中间部分被 SSH 工具截断约 44533 字符）：

```json
{
  "method": "fractional_logistic_regression",
  "reference": "Papke & Wooldridge (1996)",
  "model": "GLM(Binomial(), logit link)",
  "predictors": "z-scored log(K_eff) and log(eta_max+1e-6)",
  "response": "ASR [0,1] (raw, no log transform)",
  "K3": {
    "frac_logit_ols": { "eta_sig": "1/12", "keff_sig": "0/12" },
    "frac_logit_clustered": { "eta_sig": "7/12", "keff_sig": "4/12" }
  },
  "K5": {
    "frac_logit_ols": { "eta_sig": "2/12", "keff_sig": "4/12" },
    "frac_logit_clustered": { "eta_sig": "5/12", "keff_sig": "9/12" }
  },
  "K7": {
    "frac_logit_ols": { "eta_sig": "2/12", "keff_sig": "7/12" },
    "frac_logit_clustered": { "eta_sig": "5/12", "keff_sig": "10/12" }
  },
  "comparison_with_ols": {
    "concordance_rate": 0.9306,
    "significance_concordance_rate": 0.3333,
    "significance_concordance": "24/72",
    "direction_flips": [
      {"condition": "arc_challengexprompt_injection", "variable": "eta_max", "frac_sign": -1.0, "ols_sign": 1.0},
      {"condition": "arc_challengexsycophancy", "variable": "K_eff", "frac_sign": 1.0, "ols_sign": -1.0},
      {"condition": "arc_challengexscore_manipulation", "variable": "eta_max", "frac_sign": -1.0, "ols_sign": 1.0},
      {"condition": "mmluxscore_manipulation", "variable": "eta_max", "frac_sign": -1.0, "ols_sign": 1.0},
      {"condition": "arc_challengexscore_manipulation", "variable": "eta_max", "frac_sign": -1.0, "ols_sign": 1.0}
    ],
    "ols_known_results": {
      "K3": { "eta_sig": "11/12", "keff_sig": "8/12" },
      "K5": { "eta_sig": "10/12", "keff_sig": "12/12" },
      "K7": { "eta_sig": "12/12", "keff_sig": "11/12" }
    }
  },
  "per_condition_detail": {
    "K3": {
      "mmluxprompt_injection": { "n_panels": 455, "n_asr_zero": 0, "n_asr_one": 0, "asr_mean": 0.187, ... },
      "mmluxsycophancy": { "n_panels": 455, "n_asr_zero": 1, "n_asr_one": 0, "asr_mean": 0.052, ... },
      ...
    },
    ...（中间 ~44533 字符被截断）...
    "K7": {
      ...
      "arc_challengexposition_bias": { "n_panels": 6435, "n_asr_zero": 0, "n_asr_one": 0, "asr_mean": 0.478, ... },
      "arc_challengexauthority_bias": { "n_panels": 6435, "n_asr_zero": 2542, "n_asr_one": 0, "asr_mean": 0.0045, ... }
    }
  },
  "summary": "Fractional logit (GLM Binomial) confirms OLS patterns: direction concordance 93.1%, significance concordance 33.3% (24/72). Direction flips: 5."
}
```

文件内容过长，`per_condition_detail` 中间部分被截断。如需完整内容，可以分段用 `head`/`tail` 读取。

---
