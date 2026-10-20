# analysis ht zscore cohens d n10

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_ht-zscore-cohens-d-n10_20260521T170728_result.json`
- **Structured JSON:** [`746982ceeb467214583d.json`](../../sessions/74/746982ceeb467214583d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总结果：

**Table A: HT Cohen's d + 95% CI**

| Model | n | d_HT(15%) | 95% CI | d_HT(50%) | 95% CI |
|---------|---|-----------|--------|-----------|--------|
| Qwen | 10 | -7.26 | [-13.98, -4.30] | -1.66 | [-3.83, -0.63] |
| Llama | 10 | -2.45 | [-4.29, -1.46] | -3.07 | [-5.34, -1.90] |
| Mistral | 6 | -4.36 | [-6.97, -1.22] | -5.89 | [-9.42, -1.85] |

**Table B: Accuracy z-score Cohen's d + 95% CI**

| Model | n | d_z(15%) | 95% CI | d_z(50%) | 95% CI |
|---------|---|----------|--------|----------|--------|
| Qwen | 10 | -42.28 | [-85.10, -26.82] | -68.69 | [-138.91, -43.31] |
| Llama | 10 | -22.50 | [-46.98, -13.55] | -32.82 | [-68.56, -19.81] |
| Mistral | 6 | -7.81 | [-14.37, -4.38] | -16.60 | [-34.57, -9.71] |

注意事项：
- HT 的 Cohen's d 为**负值**，意味着 contam 的 HT 比 clean **更高**（misfit 更大）
- z-score 的 Cohen's d 极大（绝对值），因为 contam accuracy 远超 clean 分布导致 z-score 本身就是几十个标准差
- Qwen 50% contam 的 HT d 反而比 15% 小（-1.66 vs -7.26），因为 50% contam 的 HT=0.936 实际落在 clean 范围内（高 accuracy 使 response pattern 重新与 4PL 曲线对齐）

结果 JSON 已保存在 `westd-35694:/root/autodl-tmp/ht_zscore_results_n10.json`，脚本在同目录 `compute_ht_zscore.py`。

---
