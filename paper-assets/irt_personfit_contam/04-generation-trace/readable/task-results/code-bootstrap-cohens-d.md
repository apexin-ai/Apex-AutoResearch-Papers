# code bootstrap cohens d

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_bootstrap-cohens-d_20260521T142506_result.json`
- **Structured JSON:** [`eb1d991e47f721d33f16.json`](../../sessions/eb/eb1d991e47f721d33f16.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果如下：

## Bootstrap Cohen's d (10,000 resamples, seed=42)

| Model | Benchmark | Condition | n_clean | contam lz* | Cohen's d | 95% CI lower | 95% CI upper |
|-------|-----------|-----------|---------|------------|-----------|-------------|-------------|
| Qwen | MMLU | contam_15 | 10 | 3.8494 | **6.575** | 4.540 | 15.188 |
| Qwen | MMLU | contam_50 | 10 | 7.2892 | **1.897** | 1.042 | 4.945 |
| Llama | MMLU | contam_15 | 7 | −2.9922 | **2.591** | 2.035 | 5.818 |
| Llama | MMLU | contam_50 | 7 | −3.3313 | **2.840** | 2.243 | 6.470 |
| Mistral | MMLU | contam_15 | 3 | −1.3849 | **1.195** | 0.668 | 4.933 |
| Mistral | MMLU | contam_50 | 3 | −3.1503 | **1.731** | 1.141 | 6.363 |

**ARC-C 跳过**：仅 2 个 clean seeds，不足以计算。

## Clean baseline 统计

| Group | n | mean | sd | range |
|-------|---|------|----|----- |
| Qwen MMLU | 10 | 8.684 | 0.735 | [7.054, 9.529] |
| Llama MMLU | 7 | 0.540 | 1.363 | [−1.084, 2.847] |
| ARC-C | 2 | −5.502 | 0.013 | [−5.511, −5.493] |
| Mistral MMLU | 3 | 2.550 | 3.293 | [−1.046, 5.418] |

所有条件的 95% CI 下界均 > 0，效应显著。Qwen contam_15 效应量最大（d=6.6），CI 非常宽是因为 contam lz* 远离 clean 分布。Mistral n=3 估计不稳定，CI 较宽。ARC-C 需等更多 clean seeds 完成后再算。

---
