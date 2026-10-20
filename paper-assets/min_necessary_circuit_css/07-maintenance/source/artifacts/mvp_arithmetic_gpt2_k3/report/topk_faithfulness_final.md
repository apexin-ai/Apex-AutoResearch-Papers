Top-K CSS Faithfulness — Final Gate Data

== Arithmetic ==
| Circuit | k | Edges | Zero CPR | Mean CPR |
|---------|---|-------|----------|----------|
| CSS=1.0 | 50 | 44 | -0.2411 | 0.9186 |
| CSS>=2/3 | 50 | 83 | -0.1756 | 0.9577 |
| ACDC | 50 | 50 | -0.2335 | 0.9073 |
| EAP-IG | 50 | 50 | -0.0900 | 0.9853 |
| EP | 50 | 50 | -0.0934 | 0.9619 |
| CSS=1.0 | 75 | 54 | -0.2411 | 0.9186 |
| EAP-IG | 75 | 75 | -0.0433 | 0.9959 |

Condition④: CSS=1.0 < EAP-IG → FAIL

== IOI ==
| Circuit | k | Edges | Zero CPR | Mean CPR |
|---------|---|-------|----------|----------|
| CSS=1.0 | 50 | 14 | 0.1087 | 0.1803 |
| ACDC | 50 | 50 | 0.0088 | 0.1987 |
| EAP-IG | 50 | 50 | 0.0905 | 0.1794 |
| EP | 50 | 50 | -0.0182 | 0.1902 |
| CSS=1.0 | 100 | 24 | 0.1099 | 0.1760 |
| EAP-IG | 100 | 100 | -0.1092 | 0.1003 |

Condition④ IOI: CSS=1.0 (14e) CPR≥EAP-IG (50e) → PASS (edge-efficient)

IOI CPR inconsistency: RESOLVED — different tasks compared, not a data reliability issue.