# code bootstrap 10k resamples

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_bootstrap_10k_resamples_20260517T175254_result.json`
- **Structured JSON:** [`0343f49dc49beee39095.json`](../../sessions/03/0343f49dc49beee39095.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。全部 12/12 通过 Holm-Bonferroni 校正。

## 结果总结

| Rank | Model | Metric | Delta | p (10k) | HB Threshold | Pass |
|------|-------|--------|-------|---------|--------------|------|
| 1 | r1_8b | bal_acc | +0.1796 | 0.0000 | 0.00417 | YES |
| 2 | r1_8b | precision | +0.2786 | 0.0000 | 0.00455 | YES |
| 3 | r1_8b | pre_cp_fpr | -0.1255 | 0.0000 | 0.00500 | YES |
| 4 | ot_7b | precision | +0.2189 | 0.0000 | 0.00556 | YES |
| 5 | ot_7b | pre_cp_fpr | -0.1705 | 0.0000 | 0.00625 | YES |
| 6 | r1_32b | bal_acc | +0.1871 | 0.0000 | 0.00714 | YES |
| 7 | r1_32b | precision | +0.1544 | 0.0000 | 0.00833 | YES |
| 8 | qwq_32b | bal_acc | +0.1478 | 0.0000 | 0.01000 | YES |
| 9 | qwq_32b | precision | +0.2349 | 0.0000 | 0.01250 | YES |
| 10 | ot_7b | bal_acc | +0.1067 | 0.0003 | 0.01667 | YES |
| 11 | qwq_32b | pre_cp_fpr | -0.0952 | 0.0061 | 0.02500 | YES |
| 12 | r1_32b | pre_cp_fpr | -0.1457 | 0.0096 | 0.05000 | YES |

**Holm-Bonferroni: 12/12 pass**

## 关于 R1-8B FPR 的关键发现

用 W=3 配置，R1-8B FPR 的 p 值从预期的 0.044（那是旧的 W=15 配置）变为 **p<0.0001**（rank 3），远不是 marginal case。原因：W=3 下 HS-Text FPR 差距更大（delta=-0.1255 vs W=15 时的 -0.0736）。

实际 marginal tests 是：
- R1-32B FPR: p=0.0096 (rank 12, threshold=0.05) → 通过
- QwQ-32B FPR: p=0.0061 (rank 11, threshold=0.025) → 通过

结果已保存至 `/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r3_bootstrap_10k/results.json`

---
