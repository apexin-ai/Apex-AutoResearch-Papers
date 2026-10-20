# code exp accuracy zscore baseline

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-accuracy-zscore-baseline_20260520T113128_result.json`
- **Structured JSON:** [`12c8ab08228066a1df49.json`](../../sessions/12/12c8ab08228066a1df49.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。核心结果：

| 指标 | Z-score | lz* |
|------|---------|-----|
| Flagged cells | **4/60** (6.7%) | **57/60** (95%) |
| Agreement rate | **11.7%** | — |

**Confusion matrix**: TP=4, FP=0, FN=53, TN=3

**Gemini-1.5 MMLU case study**: acc=1.000, z=1.413 (**未被 flag**), lz\*=31.815 (flagged)。N=12 时即使 perfect accuracy 也不超过 |z|>1.96 阈值。

z-score 仅能捕获 4 个极端低准确率 outlier（Gemma-2B-it 和 Vicuna-7B-v1.3 在部分 benchmark 上），完全无法检测高准确率模型的 contamination。lz\* 通过 item-level response pattern 信息检测到 53 个 z-score 遗漏的 cells。

产出：`artifacts/accuracy_zscore_baseline/` 下 4 个文件，均已注册。Registry → DONE。

---
