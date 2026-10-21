# analysis false positive rate

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_false-positive-rate_20260524T082828_result.json`
- **Structured JSON:** [`232c3d311a6cf8b7e479.json`](../../sessions/23/232c3d311a6cf8b7e479.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

**数据**：26 个 clean seeds（Qwen 10, Llama 10, Mistral 6）

**lz* 分布**：
- Qwen: mean=8.68, 全部强正值
- Llama: mean=0.26, 范围 [-2.25, 2.85]
- Mistral: mean=3.40, 范围 [-1.05, 5.80]

**False Positive Rate**：
| 阈值 | FPR |
|------|-----|
| α=0.05 (lz*<-1.96) | 1/26 = 3.8% |
| α=0.01 (lz*<-2.58) | 0/26 = 0% |
| α=0.001 (lz*<-3.0) | 0/26 = 0% |

唯一的 borderline case 是 Llama s10（lz*=-2.25），介于 0.05 和 0.01 阈值之间，符合预期 Type I error rate。

文件已写入 `artifacts/rebuttal/false_positive_analysis.tex`，包含 FPR 汇总表、逐 seed 审计表、以及可直接嵌入论文的分析段落。

---
