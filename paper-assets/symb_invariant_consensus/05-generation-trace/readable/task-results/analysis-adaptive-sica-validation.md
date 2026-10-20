# analysis adaptive sica validation

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_adaptive-sica-validation_20260519T011448_result.json`
- **Structured JSON:** [`6abc47c07ec359490ec0.json`](../../sessions/6a/6abc47c07ec359490ec0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果出来了。合并两台服务器的数据：

## 合并结果（19 个实验）

### 主表

| Server | Experiment | Model | Dataset | n | n_low | n_high | SC% | SICA% | Adaptive% | D(A-SC) |
|--------|-----------|-------|---------|---|-------|--------|-----|-------|-----------|---------|
| 25068 | exp-033 | Mistral-7B | FOLIO-204 | 204 | 131 | 73 | 54.41 | 59.31 | 57.84 | **+3.43** |
| 25068 | exp-001/026 | Qwen2.5-14B | FOLIO-204 | 204 | 183 | 21 | 75.00 | 74.51 | 75.49 | **+0.49** |
| 25068 | exp-027 | Qwen3-14B-NT | FOLIO-204 | 204 | 190 | 14 | 83.82 | 84.31 | 85.29 | **+1.47** |
| 25068 | exp-035 | Qwen2.5-7B | FOLIO-204 | 204 | 171 | 33 | 76.96 | 76.47 | 76.47 | **-0.49** |
| 25068 | exp-044b | Qwen2.5-14B | FOLIO-199-ICL | 199 | 175 | 24 | 74.37 | 74.87 | 73.87 | **-0.50** |
| 25068 | exp-046 | Mistral-7B | PW-600 | 600 | 326 | 274 | 39.33 | 36.50 | 37.50 | **-1.83** |
| 25068 | exp-034-pw | Qwen2.5-14B | PW-600 | 393 | 320 | 73 | 72.52 | 74.30 | 73.54 | **+1.02** |
| 25068 | exp-028b | Qwen3-14B-T | FOLIO-204 | 122 | 121 | 1 | 83.61 | 85.25 | 83.61 | 0.00 |
| 25068 | exp-051-k4 | Mistral-7B | FOLIO-204-k4 | 204 | 160 | 44 | 54.41 | 52.94 | 53.92 | **-0.49** |
| 25068 | exp-051-k8 | Mistral-7B | FOLIO-204-k8 | 204 | 136 | 68 | 57.35 | 56.37 | 56.86 | **-0.49** |
| 25068 | exp-051-k16 | Mistral-7B | FOLIO-204-k16 | 73 | 49 | 24 | 61.64 | 63.01 | 64.38 | **+2.74** |
| 16639 | exp-052 | Mistral-7B | FOLIO-204-s123 | 204 | 134 | 70 | 53.92 | 57.35 | 56.37 | **+2.45** |
| 16639 | exp-053 | Mistral-7B | FOLIO-204-s456 | 204 | 125 | 79 | 56.37 | 55.88 | 56.37 | 0.00 |
| 16639 | exp-038 | Qwen2.5-14B | LogiQA-200 | 200 | 184 | 16 | 78.50 | 78.00 | 78.50 | 0.00 |
| 16639 | exp-049b | Mistral-7B | LogiQA-200 | 200 | 75 | 125 | 51.00 | 51.50 | 51.00 | 0.00 |
| 16639 | exp-050b | Mistral-7B | FOLIO-199-ICL | 199 | 120 | 79 | 57.79 | 54.27 | 55.28 | **-2.51** |
| 16639 | exp-041 | Qwen2.5-14B | FOLIO-204 | 204 | 178 | 26 | 77.45 | 75.49 | 75.98 | **-1.47** |
| 16639 | exp-032 | Qwen2.5-14B | PW-600 | 412 | 335 | 77 | 74.76 | 73.30 | 74.03 | **-0.73** |
| 16639 | exp-033-pw | Qwen3-14B-NT | PW-600 | 263 | 240 | 23 | 85.55 | 85.17 | 85.55 | 0.00 |

### 汇总

| | Count |
|---|---|
| Adaptive SICA > SC | **6/19** |
| Adaptive SICA = SC | **5/19** |
| Adaptive SICA < SC | **8/19** |

### 阈值敏感性（合并）

两台服务器的阈值扫描都显示：**没有任何阈值能让 Adaptive SICA 在所有实验上 >= SC**。即使提高到 1.5 bit（几乎所有问题都用 SC），仍有实验出现退化。

### 根因

高 entropy 子集中，SICA 也不总是优于 SC：
- exp-035 (Qwen2.5-7B): 高 entropy 组 SICA 54.55% vs SC 57.58% (-3.03)
- exp-044b (ICL Oracle): 高 entropy 组 SICA 45.83% vs SC 50.00% (-4.17)
- exp-046 (Mistral-7B PW): 高 entropy 组 SICA 29.56% vs SC 33.58% (-4.02)
- exp-050b (Mistral ICL): 高 entropy 组 SICA 45.57% vs SC 51.90% (-6.33)
- exp-041 (Qwen2.5-14B): 高 entropy 组 SICA 42.31% vs SC 53.85% (-11.54)

**结论：Entropy-Gated Adaptive SICA 不 work。** 核心假设"高 entropy 时 SICA 优于 SC"在数据上不成立。8/19 实验中 Adaptive SICA 劣于 SC，无法作为 method contribution。

---
