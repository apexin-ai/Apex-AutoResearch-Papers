# analysis exp 005 gla jaccard

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-005-gla-jaccard_20260522T164331_result.json`
- **Structured JSON:** [`552e5e9e3d2a5f73872d.json`](../../sessions/55/552e5e9e3d2a5f73872d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 4 架构 Pairwise Jaccard 分析完成

### ARC-Easy (n=2376, 340M)

| Pair | J_helped | J_hurt | z (helped) | z (hurt) |
|------|---------|--------|-----------|---------|
| GDN-RetNet | 0.0885 | 0.1135 | 4.04 | 6.03 |
| GDN-HGRN2 | 0.1216 | 0.1049 | 7.07 | 5.44 |
| GDN-GLA | 0.1141 | 0.1059 | 6.35 | 5.02 |
| RetNet-HGRN2 | 0.0866 | 0.1146 | 4.26 | 6.55 |
| RetNet-GLA | 0.1124 | 0.1095 | 6.70 | 5.70 |
| HGRN2-GLA | 0.0976 | 0.0874 | 5.24 | 3.78 |
| **Mean** | **0.1034** | **0.1059** | | |

### LAMBADA (n=5153, 340M)

| Pair | J_helped | J_hurt | z (helped) | z (hurt) |
|------|---------|--------|-----------|---------|
| GDN-RetNet | 0.1276 | 0.1212 | 12.04 | 11.02 |
| GDN-HGRN2 | 0.1225 | 0.0826 | 9.95 | 6.48 |
| GDN-GLA | 0.1240 | 0.1003 | 10.38 | 9.46 |
| RetNet-HGRN2 | 0.1080 | 0.0828 | 9.02 | 6.36 |
| RetNet-GLA | 0.1227 | 0.1067 | 11.23 | 10.10 |
| HGRN2-GLA | 0.1267 | 0.0856 | 10.15 | 7.67 |
| **Mean** | **0.1219** | **0.0965** | | |

### 关键发现

1. **GLA 完美融入**：GLA vs 其他 3 架构的 Jaccard（J_helped≈0.11-0.12）与原 3 架构内部（≈0.10-0.12）完全一致
2. **全部 24 个 permutation tests p < 0.001**，z-scores 3.78–12.04
3. 340M 4-arch 结果与 1.3B 3-arch 参考值（J_helped≈0.10, J_hurt≈0.09）高度一致
4. 结论：architecture-driven divergence 跨 4 种架构和 2 个 benchmark 稳健成立

结果已保存到 `westb-48145:/root/entrainment_gated_ft/results/exp005_zoo_expansion/jaccard_4arch.json`，artifact 已注册。

---
