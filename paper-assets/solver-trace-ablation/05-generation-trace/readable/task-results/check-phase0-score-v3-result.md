# check phase0 score v3 result

**solver trace ablation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_phase0_score_v3_result_20260513T100902_result.json`
- **Structured JSON:** [`3d16a0992ec09ca27637.json`](../../sessions/3d/3d16a0992ec09ca27637.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 不存在（可能已在之前删除），不影响结果。

---

## 结果报告

**Phase 0 Score V3：PASS**

### correlation_matrix.json 完整内容

```json
{
  "pearson": {
    "lexical_conformity_vs_semantic_novelty":  { "r": -0.1170, "p_value": 0.0 },
    "lexical_conformity_vs_quality":           { "r": -0.0475, "p_value": 0.00079 },
    "lexical_conformity_vs_confidence":        { "r":  0.3028, "p_value": 0.0 },
    "semantic_novelty_vs_quality":             { "r": -0.0289, "p_value": 0.041293 },
    "semantic_novelty_vs_confidence":          { "r":  0.1080, "p_value": 0.0 },
    "quality_vs_confidence":                   { "r": -0.2871, "p_value": 0.0 }
  },
  "spearman": {
    "lexical_conformity_vs_semantic_novelty":  { "rho": -0.1144, "p_value": 0.0 },
    "lexical_conformity_vs_quality":           { "rho": -0.3312, "p_value": 0.0 },
    "lexical_conformity_vs_confidence":        { "rho":  0.3354, "p_value": 0.0 },
    "semantic_novelty_vs_quality":             { "rho": -0.1212, "p_value": 0.0 },
    "semantic_novelty_vs_confidence":          { "rho":  0.1123, "p_value": 0.0 },
    "quality_vs_confidence":                   { "rho": -0.9979, "p_value": 0.0 }
  },
  "judgment": {
    "pass_no_pair_above_0.7": true,
    "pass_lc_confidence_below_0.5": true,
    "overall": "PASS"
  }
}
```

### 关键发现

| 指标对 | Pearson r | Spearman ρ |
|--------|-----------|------------|
| LC vs SN | -0.117 | -0.114 |
| LC vs Quality | -0.048 | -0.331 |
| **LC vs Confidence** | **0.303** | **0.335** |
| SN vs Quality | -0.029 | -0.121 |
| SN vs Confidence | 0.108 | 0.112 |
| **Quality vs Confidence** | **-0.287** | **-0.998** |

- 所有 Pearson |r| < 0.7 ✓
- LC vs Confidence |r| = 0.303 < 0.5 ✓
- Quality vs Confidence 的 Spearman ρ = -0.998（近乎完美负相关），但 Pearson r = -0.287，说明两者存在强单调但非线性关系

### Registry 状态

- `status`: ANALYZING
- `conclusion`: success
- Cron: 已不存在（无需删除）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "pearson": {
      "lexical_conformity_vs_semantic_novelty": {
        "r": -0.117,
        "p_value": 0.0
      },
      "lexical_conformity_vs_quality": {
        "r": -0.0475,
        "p_value": 0.00079
      },
      "lexical_conformity_vs_confidence": {
        "r": 0.3028,
        "p_value": 0.0
      },
      "semantic_novelty_vs_quality": {
        "r": -0.0289,
        "p_value": 0.041293
      },
      "semantic_novelty_vs_confidence": {
        "r": 0.108,
        "p_value": 0.0
      },
      "quality_vs_confidence": {
        "r": -0.2871,
        "p_value": 0.0
      }
    },
    "spearman": {
      "lexical_conformity_vs_semantic_novelty": {
        "rho": -0.1144,
        "p_value": 0.0
      },
      "lexical_conformity_vs_quality": {
        "rho": -0.3312,
        "p_value": 0.0
      },
      "lexical_conformity_vs_confidence": {
        "rho": 0.3354,
        "p_value": 0.0
      },
      "semantic_novelty_vs_quality": {
        "rho": -0.1212,
        "p_value": 0.0
      },
      "semantic_novelty_vs_confidence": {
        "rho": 0.1123,
        "p_value": 0.0
      },
      "quality_vs_confidence": {
        "rho": -0.9979,
        "p_value": 0.0
      }
    },
    "judgment": {
      "pass_no_pair_above_0.7": true,
      "pass_lc_confidence_below_0.5": true,
      "overall": "PASS"
    }
  }
}
```

</details>

---
