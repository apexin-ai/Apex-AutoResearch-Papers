# ssh b2 v3 domain invariant

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_b2-v3-domain-invariant_20260520T114740_result.json`
- **Structured JSON:** [`9bb276cb2b5b9e86b9ad.json`](../../sessions/9b/9bb276cb2b5b9e86b9ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

## B2-v3 Domain-Invariant Verifier Results

**Fold 3 (关键: train CoNLL+SciERC → test FewNERD):**

| Version | XGB AUC | LGB AUC | LGB ECE |
|---------|---------|---------|---------|
| B2 orig | 0.8282 | 0.8335 | - |
| B2-v2 (13 features) | 0.8603 | 0.8477 | 0.1357 |
| **B2-v3 (9 features)** | **0.8518** | **0.8562** | **0.1373** |
| v3 vs v2 Δ | -0.0085 | **+0.0085** | +0.0016 |

**所有 Fold:**

| Fold | Test | XGB AUC | LGB AUC | vs v2 XGB | vs v2 LGB |
|------|------|---------|---------|-----------|-----------|
| 1 | CoNLL | 0.9386 | 0.9368 | -0.0005 | -0.0010 |
| 2 | SciERC | **0.8163** | **0.8152** | **+0.0253** | **+0.0146** |
| 3 | FewNERD | 0.8518 | **0.8562** | -0.0085 | **+0.0085** |

**核心发现:**
1. **LGB 跨域提升**: 去掉 domain features 后 LGB 在 FewNERD (+0.0085) 和 SciERC (+0.0146) 上都提升了，说明 domain features 确实引入了负迁移
2. **XGB 混合结果**: XGB 在 SciERC 上大幅提升 (+0.0253)，但在 FewNERD 上略降 (-0.0085)
3. **Feature importance**: agreement_count (58.4%) + vc (30.3%) 占 XGB gain 的 88%，剩余 7 个特征贡献极小
4. **ECE 基本持平**: 去掉 domain features 对校准影响不大

产出已保存到 `artifacts/b2_v3_domain_invariant/`（script + results.json + summary.md）。

---
