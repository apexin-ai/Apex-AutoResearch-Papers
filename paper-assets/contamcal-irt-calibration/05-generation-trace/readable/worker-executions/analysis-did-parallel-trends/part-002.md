# analysis did parallel trends — Part 2 of 2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../analysis-did-parallel-trends.md) · [Structured JSON](../../../sessions/86/86281b2e6943d71dcc0b.json)

## Round 2

### Assistant

_source line 327_

<details><summary>Logged reasoning block</summary>

```text
The DiD analysis results from `treated_untreated_analysis.md` were run on the westd server. The cross-family eval results are likely on westd, not cqa1. But I have the IRT response matrix on cqa1 with 4 d000 Qwen-family models, which gives a good balance check.

For the purpose of the balance check:
- With 4 d000 models (Llama-3B, Qwen-0.5B, Qwen-1.5B, Qwen-3B), the results already show strong balance
- The balance check result doesn't depend on which specific d000 models we use — the question is whether the random 25% selection of MMLU items for treatment is representative of the full item pool


- Since the item selection was random, I'd expect good balance, which the results confirm

The existing run is comprehensive and valid. Across all metrics—accuracy showing negligible differences, quintile and domain distributions with minimal effect sizes, and subject-level analysis all pointing to no meaningful imbalance—the data demonstrates that the treatment assignment was properly randomized.

The discrete nature of item accuracy (0, 0.25, 0.5, 0.75, 1.0) with only 4 binary observations per item does collapse the quintile distribution, but the overall balance remains solid. At this point, the 3,540 treated items clearly represent a random sample from the full 14,042 items, so I'm confident in moving forward with the analysis rather than running additional validation checks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1be6f27b-2a04-4c12-9597-e7b6b8334c96",
  "uuid": "5e7be24d-7e21-4d88-bf04-4cdd671092ef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H68JyTXLWbJ3tRSZdsDtLB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 984,
      "cache_read_input_tokens": 81949,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 984
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

_source line 328_

Balance check 结果已经很清晰了。让我检查是否有更完整的 v3 response matrix（25 respondents）可用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1be6f27b-2a04-4c12-9597-e7b6b8334c96",
  "uuid": "9ba071a4-dfef-4f2a-bd49-053f69113d04",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H68JyTXLWbJ3tRSZdsDtLB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 984,
      "cache_read_input_tokens": 81949,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 984
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

_source line 329_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Nb2oPXpsmyWmQzTwvGsF2u`</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/contamcal-irt-calibration -name \"response_matrix*mmlu*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1be6f27b-2a04-4c12-9597-e7b6b8334c96",
  "uuid": "12b5368a-d01d-4e88-a4ef-309a063acaca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H68JyTXLWbJ3tRSZdsDtLB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 984,
      "cache_read_input_tokens": 81949,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 984
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

_source line 330 · 2026-05-22T23:23:38.506Z_

<details><summary>↩ Tool result · `toolu_01Nb2oPXpsmyWmQzTwvGsF2u`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1be6f27b-2a04-4c12-9597-e7b6b8334c96",
  "uuid": "1a363c1f-0ed5-4364-a647-0143cc597a9e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.39}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 331_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_0124mUz279nwY5VmSYuvDCR2`</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/contamcal-irt-calibration -path \"*/irt_data*\" -name \"*.csv\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1be6f27b-2a04-4c12-9597-e7b6b8334c96",
  "uuid": "160ffa34-b437-49ea-a4dc-f3d606d91c77",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H68JyTXLWbJ3tRSZdsDtLB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 984,
      "cache_read_input_tokens": 81949,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 984
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

_source line 332 · 2026-05-22T23:23:39.152Z_

<details><summary>↩ Tool result · `toolu_0124mUz279nwY5VmSYuvDCR2`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/contamcal-irt-calibration/analysis/irt_data/mmlu/response_matrix.csv\\n/root/contamcal-irt-calibration/analysis/irt_data/mmlu/exposure_scores.csv\\n/root/contamcal-irt-calibration/analysis/irt_data/mmlu/item_metadata.csv\\n/root/contamcal-irt-calibration/analysis/irt_data/gsm8k/response_matrix.csv\\n/root/contamcal-irt-calibration/analysis/irt_data/gsm8k/exposure_scores.csv\\n/root/contamcal-irt-calibration/analysis/irt_data/gsm8k/item_metadata.csv\\n/root/contamcal-irt-calibration/analysis/irt_data/arc_challenge/response_matrix.csv\\n/root/contamcal-irt-calibration/analysis/irt_data/arc_challenge/exposure_scores.csv\\n/root/contamcal-irt-calibration/analysis/irt_data/arc_challenge/item_metadata.csv\\n/root/contamcal-irt-calibration/analysis/irt_data/humaneval/response_matrix.csv\\n/root/contamcal-irt-calibration/analysis/irt_data/humaneval/exposure_scores.csv\\n/root/contamcal-irt-calibration/analysis/irt_data/humaneval/item_metadata.csv\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1be6f27b-2a04-4c12-9597-e7b6b8334c96",
  "uuid": "786749ad-39a2-494e-af5b-385912701fb2",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/contamcal-irt-calibration/analysis/irt_data/mmlu/response_matrix.csv\\\\n/root/contamcal-irt-calibration/analysis/irt_data/mmlu/exposure_scores.csv\\\\n/root/contamcal-irt-calibration/analysis/irt_data/mmlu/item_metadata.csv\\\\n/root/contamcal-irt-calibration/analysis/irt_data/gsm8k/response_matrix.csv\\\\n/root/contamcal-irt-calibration/analysis/irt_data/gsm8k/exposure_scores.csv\\\\n/root/contamcal-irt-calibration/analysis/irt_data/gsm8k/item_metadata.csv\\\\n/root/contamcal-irt-calibration/analysis/irt_data/arc_challenge/response_matrix.csv\\\\n/root/contamcal-irt-calibration/analysis/irt_data/arc_challenge/exposure_scores.csv\\\\n/root/contamcal-irt-calibration/analysis/irt_data/arc_challenge/item_metadata.csv\\\\n/root/contamcal-irt-calibration/analysis/irt_data/humaneval/response_matrix.csv\\\\n/root/contamcal-irt-calibration/analysis/irt_data/humaneval/exposure_scores.csv\\\\n/root/contamcal-irt-calibration/analysis/irt_data/humaneval/item_metadata.csv\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.39}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/contamcal-irt-calibration/analysis/irt_data/mmlu/response_matrix.csv\\n/root/contamcal-irt-calibration/analysis/irt_data/mmlu/exposure_scores.csv\\n/root/contamcal-irt-calibration/analysis/irt_data/mmlu/item_metadata.csv\\n/root/contamcal-irt-calibration/analysis/irt_data/gsm8k/response_matrix.csv\\n/root/contamcal-irt-calibration/analysis/irt_data/gsm8k/exposure_scores.csv\\n/root/contamcal-irt-calibration/analysis/irt_data/gsm8k/item_metadata.csv\\n/root/contamcal-irt-calibration/analysis/irt_data/arc_challenge/response_matrix.csv\\n/root/contamcal-irt-calibration/analysis/irt_data/arc_challenge/exposure_scores.csv\\n/root/contamcal-irt-calibration/analysis/irt_data/arc_challenge/item_metadata.csv\\n/root/contamcal-irt-calibration/analysis/irt_data/humaneval/response_matrix.csv\\n/root/contamcal-irt-calibration/analysis/irt_data/humaneval/exposure_scores.csv\\n/root/contamcal-irt-calibration/analysis/irt_data/humaneval/item_metadata.csv\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 333_

<details><summary>Logged reasoning block</summary>

```text
OK, the response matrix on cqa1 has 20 respondents (the older Qwen within-family data), not the v3 25-respondent matrix. The v3 data was created on westd. But for the balance check, the 4-model d000 data is sufficient and actually very clean.

Let me also note: the balance check is about whether treated and untreated items are similar at baseline. Since items were randomly selected for treatment, we'd expect good balance. With 4 independent d000 models confirming balance, the result is robust.

Now let me write the output balance table markdown to the artifacts directory.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1be6f27b-2a04-4c12-9597-e7b6b8334c96",
  "uuid": "05b65cb8-8a5e-42fe-bfaf-6f8219fe4f0c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QEDxgtmzU6PzAaG8aofCxg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1457,
      "cache_read_input_tokens": 82933,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1457
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

_source line 334_

现有 4 个 d000 模型的结果已经足够充分。现在生成 balance table 到 artifacts。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1be6f27b-2a04-4c12-9597-e7b6b8334c96",
  "uuid": "67bf1c99-7449-41f6-bf91-7c2c1bf9c8ef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QEDxgtmzU6PzAaG8aofCxg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1457,
      "cache_read_input_tokens": 82933,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1457
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

_source line 335_

<details open><summary>🔧 Tool call — Write · `toolu_01Eh3buDYZSBaZsBKsKBHnkh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/did_parallel_trends_balance.md",
  "content": "# DiD Parallel Trends Balance Check (B1)\n\n## Overview\n\nValidates the parallel trends assumption for the Difference-in-Differences design by checking pre-treatment (d000) balance between treated items (n=3,540; included in d025 SFT data) and untreated items (n=10,502).\n\nBaseline accuracy computed from 4 d000 models: Llama-3.2-3B, Qwen2.5-0.5B, Qwen2.5-1.5B, Qwen2.5-3B (all seed=42, 0% contamination).\n\n## 1. Baseline Accuracy\n\n| Group | n | Mean | Std | Median |\n|-------|---|------|-----|--------|\n| Treated | 3,540 | 0.5214 | 0.3429 | 0.50 |\n| Untreated | 10,502 | 0.5156 | 0.3458 | 0.50 |\n| **Difference** | — | **+0.0058** | — | — |\n\n| Test | Statistic | p-value |\n|------|-----------|---------|\n| Two-sample t-test | t = 0.858 | 0.391 |\n| Mann-Whitney U | U = 18,765,476 | 0.386 |\n| Cohen's d | 0.017 | — |\n| Kolmogorov-Smirnov | D = 0.014 | 0.639 |\n\n**Interpretation**: Negligible difference (d = 0.017, ~0.6 pp). Not statistically significant.\n\n## 2. Per-Model d000 Accuracy\n\n| Model | Treated Acc | Untreated Acc | Diff | t | p |\n|-------|-------------|---------------|------|---|---|\n| Llama-3.2-3B | 0.4596 | 0.4528 | +0.0068 | 0.706 | 0.480 |\n| Qwen2.5-0.5B | 0.3989 | 0.3975 | +0.0013 | 0.139 | 0.889 |\n| Qwen2.5-1.5B | 0.5862 | 0.5850 | +0.0011 | 0.118 | 0.906 |\n| Qwen2.5-3B | 0.6410 | 0.6272 | +0.0137 | 1.466 | 0.143 |\n\n**Interpretation**: No model shows a significant treated-untreated gap at baseline. All p > 0.14, all |diff| < 1.4 pp.\n\n## 3. Difficulty Quintile Distribution\n\nItems binned by d000 accuracy (4 discrete levels with 4 models: 0.00, 0.25, 0.50, 0.75, 1.00).\n\n| Quintile | Accuracy | Treated (%) | Untreated (%) | Diff (pp) |\n|----------|----------|-------------|---------------|-----------|\n| Q1 (hardest) | [0.00–0.25] | 34.7% | 36.2% | −1.4 |\n| Q2 | [0.50] | 23.2% | 22.8% | +0.4 |\n| Q3 | [0.75] | 22.8% | 21.3% | +1.5 |\n| Q4 (easiest) | [1.00] | 19.3% | 19.8% | −0.5 |\n\n- Chi-square: χ² = 4.72, df = 3, p = 0.194\n- Cramér's V = 0.018\n\n**Interpretation**: Treated and untreated items have near-identical difficulty profiles. Maximum discrepancy is 1.5 pp.\n\n## 4. Domain Distribution\n\n| Domain | Treated (%) | Untreated (%) | Diff (pp) |\n|--------|-------------|---------------|-----------|\n| Humanities | 32.7% | 33.8% | −1.1 |\n| Other | 23.2% | 21.8% | +1.4 |\n| STEM | 22.7% | 22.4% | +0.3 |\n| Social Sciences | 21.5% | 22.1% | −0.6 |\n\n- Chi-square: χ² = 3.99, df = 3, p = 0.263\n- Cramér's V = 0.017\n\n**Interpretation**: Domain composition is well-balanced. All discrepancies < 1.5 pp.\n\n## 5. Subject Distribution\n\n57 MMLU subjects tested. Top 5 by |diff|:\n\n| Subject | N | Treated (%) | Untreated (%) | Diff (pp) |\n|---------|---|-------------|---------------|-----------|\n| philosophy | 311 | 2.60% | 2.09% | +0.51 |\n| professional_law | 1,534 | 10.56% | 11.05% | −0.48 |\n| high_school_macroeconomics | 390 | 2.43% | 2.89% | −0.47 |\n| medical_genetics | 100 | 1.05% | 0.60% | +0.45 |\n| high_school_computer_science | 100 | 1.02% | 0.61% | +0.41 |\n\n- Chi-square: χ² = 61.37, df = 56, p = 0.290\n- Cramér's V = 0.066\n\n**Interpretation**: Subject-level proportions are well-matched. Maximum discrepancy is 0.5 pp and chi-square is non-significant.\n\n## Summary\n\n| Dimension | Test | Statistic | p-value | Effect Size | Verdict |\n|-----------|------|-----------|---------|-------------|---------|\n| Accuracy | t-test | t = 0.86 | 0.391 | d = 0.017 | ✓ Balanced |\n| Accuracy | Mann-Whitney U | U = 18.8M | 0.386 | — | ✓ Balanced |\n| Accuracy | KS test | D = 0.014 | 0.639 | — | ✓ Balanced |\n| Difficulty quintile | Chi-square | χ² = 4.72 | 0.194 | V = 0.018 | ✓ Balanced |\n| Domain | Chi-square | χ² = 3.99 | 0.263 | V = 0.017 | ✓ Balanced |\n| Subject (57 subj.) | Chi-square | χ² = 61.4 | 0.290 | V = 0.066 | ✓ Balanced |\n\n## Conclusion\n\nPre-treatment balance holds across all dimensions. Treated and untreated items are well-matched on:\n- **Baseline accuracy**: diff = +0.006, Cohen's d = 0.017 (negligible)\n- **Difficulty distribution**: χ² p = 0.194, Cramér's V = 0.018\n- **Domain composition**: χ² p = 0.263, Cramér's V = 0.017\n- **Subject composition**: χ² p = 0.290, Cramér's V = 0.066\n\nAll effect sizes are negligible (d < 0.02, V < 0.07). This is consistent with the random 25% selection mechanism used to construct the treated set. The parallel trends assumption for the DiD design is well-supported.\n\n## Data Source\n\n- Contamination labels: `contamination_labels_mmlu_d025.json` (d025 = 25% of 14,042 MMLU items = 3,540 treated)\n- Baseline responses: IRT response matrix (4 d000 respondents × 14,042 items)\n- Item metadata: `item_metadata.csv` (subject, domain, difficulty_baseline)\n- Script: `analysis/did_balance_check.py` on cqa1-21977\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1be6f27b-2a04-4c12-9597-e7b6b8334c96",
  "uuid": "cbcd4670-a39a-45d2-805f-bb101c883952",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QEDxgtmzU6PzAaG8aofCxg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1457,
      "cache_read_input_tokens": 82933,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1457
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

_source line 336 · 2026-05-22T23:24:22.275Z_

<details><summary>↩ Tool result · `toolu_01Eh3buDYZSBaZsBKsKBHnkh`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/did_parallel_trends_balance.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1be6f27b-2a04-4c12-9597-e7b6b8334c96",
  "uuid": "ef287302-ecd3-4097-bbc6-665e28f5165d",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/did_parallel_trends_balance.md",
    "content": "# DiD Parallel Trends Balance Check (B1)\n\n## Overview\n\nValidates the parallel trends assumption for the Difference-in-Differences design by checking pre-treatment (d000) balance between treated items (n=3,540; included in d025 SFT data) and untreated items (n=10,502).\n\nBaseline accuracy computed from 4 d000 models: Llama-3.2-3B, Qwen2.5-0.5B, Qwen2.5-1.5B, Qwen2.5-3B (all seed=42, 0% contamination).\n\n## 1. Baseline Accuracy\n\n| Group | n | Mean | Std | Median |\n|-------|---|------|-----|--------|\n| Treated | 3,540 | 0.5214 | 0.3429 | 0.50 |\n| Untreated | 10,502 | 0.5156 | 0.3458 | 0.50 |\n| **Difference** | — | **+0.0058** | — | — |\n\n| Test | Statistic | p-value |\n|------|-----------|---------|\n| Two-sample t-test | t = 0.858 | 0.391 |\n| Mann-Whitney U | U = 18,765,476 | 0.386 |\n| Cohen's d | 0.017 | — |\n| Kolmogorov-Smirnov | D = 0.014 | 0.639 |\n\n**Interpretation**: Negligible difference (d = 0.017, ~0.6 pp). Not statistically significant.\n\n## 2. Per-Model d000 Accuracy\n\n| Model | Treated Acc | Untreated Acc | Diff | t | p |\n|-------|-------------|---------------|------|---|---|\n| Llama-3.2-3B | 0.4596 | 0.4528 | +0.0068 | 0.706 | 0.480 |\n| Qwen2.5-0.5B | 0.3989 | 0.3975 | +0.0013 | 0.139 | 0.889 |\n| Qwen2.5-1.5B | 0.5862 | 0.5850 | +0.0011 | 0.118 | 0.906 |\n| Qwen2.5-3B | 0.6410 | 0.6272 | +0.0137 | 1.466 | 0.143 |\n\n**Interpretation**: No model shows a significant treated-untreated gap at baseline. All p > 0.14, all |diff| < 1.4 pp.\n\n## 3. Difficulty Quintile Distribution\n\nItems binned by d000 accuracy (4 discrete levels with 4 models: 0.00, 0.25, 0.50, 0.75, 1.00).\n\n| Quintile | Accuracy | Treated (%) | Untreated (%) | Diff (pp) |\n|----------|----------|-------------|---------------|-----------|\n| Q1 (hardest) | [0.00–0.25] | 34.7% | 36.2% | −1.4 |\n| Q2 | [0.50] | 23.2% | 22.8% | +0.4 |\n| Q3 | [0.75] | 22.8% | 21.3% | +1.5 |\n| Q4 (easiest) | [1.00] | 19.3% | 19.8% | −0.5 |\n\n- Chi-square: χ² = 4.72, df = 3, p = 0.194\n- Cramér's V = 0.018\n\n**Interpretation**: Treated and untreated items have near-identical difficulty profiles. Maximum discrepancy is 1.5 pp.\n\n## 4. Domain Distribution\n\n| Domain | Treated (%) | Untreated (%) | Diff (pp) |\n|--------|-------------|---------------|-----------|\n| Humanities | 32.7% | 33.8% | −1.1 |\n| Other | 23.2% | 21.8% | +1.4 |\n| STEM | 22.7% | 22.4% | +0.3 |\n| Social Sciences | 21.5% | 22.1% | −0.6 |\n\n- Chi-square: χ² = 3.99, df = 3, p = 0.263\n- Cramér's V = 0.017\n\n**Interpretation**: Domain composition is well-balanced. All discrepancies < 1.5 pp.\n\n## 5. Subject Distribution\n\n57 MMLU subjects tested. Top 5 by |diff|:\n\n| Subject | N | Treated (%) | Untreated (%) | Diff (pp) |\n|---------|---|-------------|---------------|-----------|\n| philosophy | 311 | 2.60% | 2.09% | +0.51 |\n| professional_law | 1,534 | 10.56% | 11.05% | −0.48 |\n| high_school_macroeconomics | 390 | 2.43% | 2.89% | −0.47 |\n| medical_genetics | 100 | 1.05% | 0.60% | +0.45 |\n| high_school_computer_science | 100 | 1.02% | 0.61% | +0.41 |\n\n- Chi-square: χ² = 61.37, df = 56, p = 0.290\n- Cramér's V = 0.066\n\n**Interpretation**: Subject-level proportions are well-matched. Maximum discrepancy is 0.5 pp and chi-square is non-significant.\n\n## Summary\n\n| Dimension | Test | Statistic | p-value | Effect Size | Verdict |\n|-----------|------|-----------|---------|-------------|---------|\n| Accuracy | t-test | t = 0.86 | 0.391 | d = 0.017 | ✓ Balanced |\n| Accuracy | Mann-Whitney U | U = 18.8M | 0.386 | — | ✓ Balanced |\n| Accuracy | KS test | D = 0.014 | 0.639 | — | ✓ Balanced |\n| Difficulty quintile | Chi-square | χ² = 4.72 | 0.194 | V = 0.018 | ✓ Balanced |\n| Domain | Chi-square | χ² = 3.99 | 0.263 | V = 0.017 | ✓ Balanced |\n| Subject (57 subj.) | Chi-square | χ² = 61.4 | 0.290 | V = 0.066 | ✓ Balanced |\n\n## Conclusion\n\nPre-treatment balance holds across all dimensions. Treated and untreated items are well-matched on:\n- **Baseline accuracy**: diff = +0.006, Cohen's d = 0.017 (negligible)\n- **Difficulty distribution**: χ² p = 0.194, Cramér's V = 0.018\n- **Domain composition**: χ² p = 0.263, Cramér's V = 0.017\n- **Subject composition**: χ² p = 0.290, Cramér's V = 0.066\n\nAll effect sizes are negligible (d < 0.02, V < 0.07). This is consistent with the random 25% selection mechanism used to construct the treated set. The parallel trends assumption for the DiD design is well-supported.\n\n## Data Source\n\n- Contamination labels: `contamination_labels_mmlu_d025.json` (d025 = 25% of 14,042 MMLU items = 3,540 treated)\n- Baseline responses: IRT response matrix (4 d000 respondents × 14,042 items)\n- Item metadata: `item_metadata.csv` (subject, domain, difficulty_baseline)\n- Script: `analysis/did_balance_check.py` on cqa1-21977\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---


### Assistant

_source line 337_

Balance check 完成。

**结果**：pre-treatment balance 在所有维度上都成立，parallel trends 假设有良好支撑：

| 维度 | p-value | 效应量 |
|------|---------|--------|
| Accuracy | 0.391 | d = 0.017 |
| Difficulty quintile | 0.194 | V = 0.018 |
| Domain | 0.263 | V = 0.017 |
| Subject (57个) | 0.290 | V = 0.066 |
| KS 分布检验 | 0.639 | D = 0.014 |

Treated 和 untreated 组在 baseline accuracy（差异仅 +0.6pp）、难度分布、领域组成和科目组成上均无显著差异，所有效应量均可忽略。这与 25% 随机抽样机制一致。

输出已写入 `artifacts/did_parallel_trends_balance.md`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1be6f27b-2a04-4c12-9597-e7b6b8334c96",
  "uuid": "1641c46b-00d5-4aa7-a788-b5a28fe46c3c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FKfVjov3serLuKat4LCwKW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2380,
      "cache_read_input_tokens": 84390,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2380
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

_source line 338_

Balance check 完成。

**结果**：pre-treatment balance 在所有维度上都成立，parallel trends 假设有良好支撑：

| 维度 | p-value | 效应量 |
|------|---------|--------|
| Accuracy | 0.391 | d = 0.017 |
| Difficulty quintile | 0.194 | V = 0.018 |
| Domain | 0.263 | V = 0.017 |
| Subject (57个) | 0.290 | V = 0.066 |
| KS 分布检验 | 0.639 | D = 0.014 |

Treated 和 untreated 组在 baseline accuracy（差异仅 +0.6pp）、难度分布、领域组成和科目组成上均无显著差异，所有效应量均可忽略。这与 25% 随机抽样机制一致。

输出已写入 `artifacts/did_parallel_trends_balance.md`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 433425,
  "duration_api_ms": 471651,
  "num_turns": 48,
  "stop_reason": "end_turn",
  "session_id": "1be6f27b-2a04-4c12-9597-e7b6b8334c96",
  "total_cost_usd": 2.196122549999999,
  "usage": {
    "input_tokens": 1602,
    "cache_creation_input_tokens": 74929,
    "cache_read_input_tokens": 1618031,
    "output_tokens": 20266,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 74929,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 270,
        "cache_read_input_tokens": 84390,
        "cache_creation_input_tokens": 2380,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2380
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 5621,
      "outputTokens": 11413,
      "cacheReadInputTokens": 1629498,
      "cacheCreationInputTokens": 142804,
      "webSearchRequests": 0,
      "costUSD": 0.40414079999999997,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 1602,
      "outputTokens": 20266,
      "cacheReadInputTokens": 1618031,
      "cacheCreationInputTokens": 74929,
      "webSearchRequests": 0,
      "costUSD": 1.7919817499999997,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "34950a35-1f5b-4f6d-9180-f6a40a209f71"
}
```

</details>

---
