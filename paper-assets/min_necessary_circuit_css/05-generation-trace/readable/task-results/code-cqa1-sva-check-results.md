# code cqa1 sva check results

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cqa1-sva-check-results_20260513T080048_result.json`
- **Structured JSON:** [`413ef438a65edadcb579.json`](../../sessions/41/413ef438a65edadcb579.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都用了 top-100 binarization，构成跨服务器复现而非 binarization 对照。

### cqa1 vs westd 对比表 (SVA GPT-2 K=3, top-100)

| 指标 | cqa1-21977 | westd-pro6000 |
|------|-----------|---------------|
| **CSS 分布** | 52/55/46 | 60/54/44 |
| **J(acdc×eapig)** | 0.370 | 0.316 |
| **J(acdc×ep)** | 0.429 | 0.418 |
| **J(eapig×ep)** | 0.653 | 0.653 |
| **3-way Jaccard** | 0.301 | 0.279 |
| **Off-diagonal** | 91.8% | 92.1% |
| **CSS=1.0 mean CPR** | 1.174 | 1.180 |
| **eapig mean CPR** | 1.168 | 1.168 |
| **ep mean CPR** | 1.168 | 1.168 |
| **acdc mean CPR** | 1.162 | 1.172 |
| **CSS=1.0 zero CPR** | -0.740 | -0.703 |
| **Gate** | PASS_MAIN | PASS_MAIN |
| **D025 ④** | PASS (mean only) | FAIL (zero ablation) |
| **Conclusion** | success | negative |

### 关键发现

1. **两次复现高度一致**：CSS 分布、Jaccard、off-diagonal 几乎相同，跨服务器可复现性强。

2. **结论不一致是评估标准差异**：cqa1 版本只用 mean ablation 判定条件④（1.174 > 1.168/1.168/1.162 → PASS）；westd 版本额外检查了 zero ablation（CSS=1.0 CPR -0.703 < eapig -0.348 → FAIL）。**实际上 cqa1 的 zero ablation 也不满足条件④**（-0.740 < -0.348）。

3. **建议**：统一条件④判定标准。若 D025 要求 zero+mean 双通过，cqa1 结论应从 `success` 改为 `negative`（与 westd 一致）。

是否需要将 cqa1 结论改为 `negative` 以保持一致？

---
