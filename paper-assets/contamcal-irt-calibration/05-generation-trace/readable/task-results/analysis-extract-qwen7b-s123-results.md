# analysis extract qwen7b s123 results

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_extract-qwen7b-s123-results_20260519T174054_result.json`
- **Structured JSON:** [`246117a42dc60cab31da.json`](../../sessions/24/246117a42dc60cab31da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Qwen-7B seed=123 Eval 结果

每个文件两行 accuracy，第一行 MMLU，第二行 ARC：

| Dosage | MMLU Acc | ARC Acc |
|--------|----------|---------|
| d000 | 69.74% | 89.68% |
| d005 | 69.41% | 90.10% |
| d025 | 70.25% | 90.10% |
| d050 | 70.40% | 89.85% |
| d100 | 70.66% | 89.68% |

### 与 seed=42 对比 (MMLU)

| Dosage | s42 | s123 | Δ |
|--------|-----|------|---|
| d000 | 66.11% | 69.74% | +3.63pp |
| d005 | 65.04% | 69.41% | +4.37pp |
| d025 | 63.01% | 70.25% | +7.24pp |
| d050 | 63.56% | 70.40% | +6.84pp |
| d100 | 64.33% | 70.66% | +6.33pp |

### Pattern 判断

**s123 没有复现 V-recovery pattern。**

- **MMLU s123**：d005 仅微降 0.33pp，之后 d025→d050→d100 单调递增，d100 比 baseline 还高 0.92pp。整体近似 monotonic increase。与 s42 的明显 V 形（d025 跌至 63.01% 后回升）完全不同。
- **ARC s123**：全程极稳定（89.68%–90.10%），dosage 几乎无影响。
- **s42 vs s123 基线差异大**：d000 差 3.63pp，这在同一 base model 上不应出现。需确认 s42 数据是否来自 eval_results_v2 还是 v1（eval 配置可能不同）。

---
