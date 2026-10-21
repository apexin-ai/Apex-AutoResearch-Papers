# Multi-Threshold Robustness Analysis — VLA Exit Collapse

> Generated: 2026-05-23 ~16:42 UTC | Source: Bootstrap v3 (MCCV) 20/20 conditions

## Threshold Sweep

| Threshold | VLM→VLA trained (N/6) | OpenVLA trained (N/4) | Untrained (N/10) | Clean separation? |
|-----------|------------------------|------------------------|-------------------|-------------------|
| 0.05      | 6/6                    | 1/4                    | 6/10             | NO               |
| 0.08      | 6/6                    | 1/4                    | 3/10             | NO               |
| **0.10**  | **6/6**                | **0/4**                | **0/10**         | **YES**          |
| **0.15**  | **6/6**                | **0/4**                | **0/10**         | **YES**          |
| 0.20      | 5/6                    | 0/4                    | 0/10             | NO               |

## Individual Canonical Δ Values

### VLM→VLA trained (6 conditions)

| Condition | Δ | 95% CI |
|---|---|---|
| tracvla_goal/trained | 0.3334 | [0.2069, 0.4508] |
| tracvla_spatial/trained | 0.1557 | [0.0906, 0.2244] |
| tracvla_object/trained | 0.3623 | [0.2834, 0.5038] |
| tracvla_long/trained | 0.3579 | [0.1714, 0.5333] |
| nora_goal/trained | 0.4551 | [0.9099, 1.6077]† |
| nora_spatial/trained | 0.3080 | [0.3011, 0.5119] |

### OpenVLA trained (4 conditions)

| Condition | Δ | 95% CI |
|---|---|---|
| openvla_goal/trained | 0.0864 | [-0.056, 0.1064] |
| openvla_spatial/trained | 0.0371 | [0.0087, 0.102] |
| openvla_object/trained | 0.0370 | [-0.0038, 0.0854] |
| openvla_long/trained | 0.0325 | [0.0037, 0.103] |

### Untrained (10 conditions)

| Condition | Δ | 95% CI |
|---|---|---|
| tracvla_goal/untrained | 0.0645 | [-0.1084, 0.051] |
| tracvla_spatial/untrained | 0.0477 | [-0.6067, -0.4606]‡ |
| tracvla_object/untrained | 0.0090 | [-0.0669, 0.0169] |
| tracvla_long/untrained | 0.0971 | [-0.0208, 0.1078] |
| nora_goal/untrained | 0.0806 | [-0.0147, 0.1102] |
| nora_spatial/untrained | 0.0885 | [-0.0128, 0.0931] |
| openvla_goal/untrained | 0.0558 | [0.0113, 0.0773] |
| openvla_spatial/untrained | 0.0437 | [0.0295, 0.1113] |
| openvla_object/untrained | 0.0513 | [-0.0044, 0.0905] |
| openvla_long/untrained | 0.0349 | [0.0261, 0.1047] |

## Separation Analysis

- VLM→VLA trained **minimum** Δ: **0.1557** (tracvla_spatial/trained)
- OpenVLA trained **maximum** Δ: **0.0864** (openvla_goal/trained)
- Untrained **maximum** Δ: **0.0971** (tracvla_long/untrained)
- **Gap: 0.1557 − 0.0971 = 0.0586**
- Clean separation exists for any threshold in **(0.0971, 0.1557)** — both 0.10 and 0.15 fall within this range

## Notes

- †NORA goal/trained CI unreliable due to near-zero exit R² (see bootstrap_v3_summary_table.md)
- ‡TracVLA spatial/untrained CI reflects L4 instability in flat R² profile, not real exit collapse
