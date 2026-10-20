# code gemma2b 10k bootstrap ci

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gemma2b_10k_bootstrap_ci_20260523T000341_result.json`
- **Structured JSON:** [`a23afecc6722391ff6b0.json`](../../sessions/a2/a23afecc6722391ff6b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

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

---
