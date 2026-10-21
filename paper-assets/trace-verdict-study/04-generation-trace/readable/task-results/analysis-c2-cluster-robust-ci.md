# analysis c2 cluster robust ci

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_c2-cluster-robust-ci_20260516T060303_result.json`
- **Structured JSON:** [`b260774817dbbf73e086.json`](../../sessions/b2/b260774817dbbf73e086.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

| Condition | N | Problems | Sample Acc | Problem Acc | Cluster CI | Wilson CI | Width Ratio |
|-----------|---|----------|-----------|-------------|------------|-----------|-------------|
| **ae_only** | 1190 | 119 | 0.9992 | — | [0.9975, 1.0000] | [0.9953, 0.9999] | **0.55** |
| **exception_only** | 1190 | 119 | 0.9983 | — | [0.9950, 1.0000] | [0.9939, 0.9995] | 0.89 |
| **vota** | 1190 | 119 | 0.9941 | — | [0.9832, 1.0000] | [0.9879, 0.9971] | 1.82 |
| **vota_no_ae** | 1190 | 119 | 0.9941 | — | [0.9832, 1.0000] | [0.9879, 0.9971] | 1.82 |
| **loop_only** | 1190 | 119 | 0.8563 | — | [0.8025, 0.9059] | [0.8352, 0.8751] | 2.59 |
| **full_trace** | 1190 | 119 | 0.8176 | — | [0.7571, 0.8731] | [0.7947, 0.8386] | 2.64 |
| **full_trace_label_only** | 1190 | 119 | 0.8622 | — | [0.8050, 0.9143] | [0.8414, 0.8806] | 2.79 |
| **no_trace** | 1190 | 119 | 0.7513 | — | [0.6840, 0.8160] | [0.7259, 0.7750] | 2.69 |
| **deepseek_vota** | 1190 | 119 | 0.8445 | — | [0.7866, 0.9000] | [0.8228, 0.8640] | 2.76 |
| **deepseek_exception_only** | 1190 | 119 | 0.9933 | — | [0.9815, 1.0000] | [0.9868, 0.9966] | 1.89 |
| **deepseek_no_trace** | 1190 | 119 | 0.7336 | — | [0.6630, 0.8009] | [0.7078, 0.7579] | 2.75 |
| **deepseek_full_trace** | 1190 | 119 | 0.1059 | — | [0.0655, 0.1513] | [0.0897, 0.1247] | 2.45 |

关键发现：

1. **119 unique problems**，每个 problem 10 个 solutions（1190/119）
2. **高准确率条件（>99%）**：cluster CI 反而比 Wilson CI **更窄**（ratio < 1）。这是因为几乎所有 problem 都是全对，cluster 内方差极低，有效样本量反而没有损失。
3. **中低准确率条件（75%-86%）**：cluster CI 比 Wilson CI **宽 2.5-2.8 倍**，符合预期——同一 problem 下 solutions 高度相关，有效独立样本量从 1190 降到接近 119。
4. **deepseek_full_trace 只有 10.6% accuracy**——明显异常，可能是失败的 run。

输出文件：
- JSON: `/root/autodl-tmp/trace-verdict-study-checkpoints/analysis/cluster_robust_ci.json`
- Markdown: `/root/autodl-tmp/trace-verdict-study-checkpoints/analysis/cluster_robust_ci_summary.md`
- 脚本: `/root/trace-verdict-study/analysis/cluster_robust_ci.py`

---
