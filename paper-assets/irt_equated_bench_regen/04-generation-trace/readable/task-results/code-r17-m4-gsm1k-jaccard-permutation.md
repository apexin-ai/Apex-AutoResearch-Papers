# code r17 m4 gsm1k jaccard permutation

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r17_m4_gsm1k_jaccard_permutation_20260522T161908_result.json`
- **Structured JSON:** [`575b85acc0c9f8ad9648.json`](../../sessions/57/575b85acc0c9f8ad9648.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个产出已生成：

| 文件 | 说明 |
|------|------|
| `gsm1k_jaccard_permutation.py` | 脚本（median split + 6 组阈值 robustness + Spearman） |
| `gsm1k_jaccard_results.csv` | 主分析 10,000 次 permutation 的 null 分布 |
| `gsm1k_jaccard_report.md` | 完整报告 |

**关键结果：**
- **Jaccard (median split)**: 0.3913, null mean = 0.3256, **p = 0.31** — 不显著。二值化后 set-level 重合无异于随机。
- **Robustness**: 6 组阈值中仅 gap>0.02 & |dif|>0.10 一组边际显著 (p=0.029)，但该组合将 33 个模型中 20/25 个分别标记为 contaminated/dif-sensitive，集合过大，Jaccard 膨胀。
- **Spearman**: r = 0.40, **p = 0.02** — 连续变量上存在中等正相关。binarization 丢失信息导致 Jaccard 不显著，但 rank order 上 contamination gap 大的模型倾向于 DIF magnitude 也大。

结论：两个信号 **部分相关但不冗余** — DIF 捕捉的 item-level 心理测量异常不能被 contamination gap 完全预测。

---
