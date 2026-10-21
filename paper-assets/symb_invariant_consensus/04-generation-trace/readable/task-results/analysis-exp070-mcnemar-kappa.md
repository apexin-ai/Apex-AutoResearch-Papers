# analysis exp070 mcnemar kappa

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp070-mcnemar-kappa_20260519T135944_result.json`
- **Structured JSON:** [`77bb852a3441cdc9dbe8.json`](../../sessions/77/77bb852a3441cdc9dbe8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Scipy 验证通过，数值一致。结果：

```json
{
  "contingency_table": {"a": 136, "b": 1, "c": 6, "d": 57},
  "n": 200,
  "discordant_b": "1 (SC correct, SICA wrong)",
  "discordant_c": "6 (SC wrong, SICA correct)",
  "mcnemar_chi2": 2.2857,
  "mcnemar_p": 0.130570,
  "mcnemar_p_exact": 0.125000,
  "significant_005": false,
  "cohens_kappa": 0.9171,
  "kappa_interpretation": "almost_perfect"
}
```

**关键发现：**

- **Discordant pairs 极少**：仅 7 对 (b=1, c=6)。SICA 翻转了 6 题从错到对，仅丢失 1 题。
- **McNemar's test 不显著**：p=0.131 (asymptotic), p=0.125 (exact binomial)，均 >0.05。discordant pairs 太少，统计功效不足。
- **Cohen's κ=0.917 (almost perfect)**：SC 和 SICA 在 193/200 题上决策一致，两方法高度一致。

Δ=+2.5pp 的改进方向正确（c=6 > b=1），但 n=200 下 discordant pairs 仅 7 对，无法达到统计显著性。需要更大样本量或更多 discordant pairs 才能确认显著性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "contingency_table": {
      "a": 136,
      "b": 1,
      "c": 6,
      "d": 57
    },
    "n": 200,
    "discordant_b": "1 (SC correct, SICA wrong)",
    "discordant_c": "6 (SC wrong, SICA correct)",
    "mcnemar_chi2": 2.2857,
    "mcnemar_p": 0.13057,
    "mcnemar_p_exact": 0.125,
    "significant_005": false,
    "cohens_kappa": 0.9171,
    "kappa_interpretation": "almost_perfect"
  }
}
```

</details>

---
