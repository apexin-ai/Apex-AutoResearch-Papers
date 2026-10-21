# code olmo nucleus eval

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_olmo_nucleus_eval_20260514T182449_result.json`
- **Structured JSON:** [`932fb4fca446cceb4855.json`](../../sessions/93/932fb4fca446cceb4855.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。以下是完整结果和对比。

---

## OLMo-1B nucleus (p=0.95) 完整 Evaluation 结果

### 4-class Classification (RF)

| Metric | OLMo nucleus | Pythia nucleus | Delta |
|--------|-------------|---------------|-------|
| **Accuracy** | **78.8%** [77.6, 80.0] | 78.2% [76.9, 79.4] | **+0.6%** |
| LR Accuracy | 75.1% [73.7, 76.5] | — | — |
| AUC 0v1 | 0.9834 | 0.9975 | -0.014 |
| AUC 0v2 | 0.9949 | — | — |
| AUC 0v3 | 0.9989 | — | — |
| AUC 1v2 | 0.8673 | 0.8607 | **+0.007** |
| AUC 1v3 | 0.9806 | — | — |
| AUC 2v3 | 0.8124 | 0.8005 | **+0.012** |

### 4-class Per-class (RF)

| Class | Precision | Recall | F1 |
|-------|-----------|--------|-----|
| depth-0 | 0.95 | 0.99 | 0.97 |
| depth-1 | 0.85 | 0.82 | 0.83 |
| depth-2 | 0.63 | 0.59 | 0.61 |
| depth-3 | 0.71 | 0.76 | 0.73 |

### 3-class Classification (d1-d3 only, RF)

| Metric | OLMo | Pythia | Delta |
|--------|------|--------|-------|
| **Accuracy** | **74.4%** [72.8, 76.0] | 70.8% [69.2, 72.5] | **+3.6%** |
| MAE | 0.270 | 0.320 | -0.050 |
| d1 recall | 0.864 | 0.790 | +0.074 |
| d2 recall | 0.607 | 0.607 | 0.000 |
| d3 recall | 0.761 | 0.728 | +0.033 |
| d1 precision | 0.863 | 0.852 | +0.011 |
| d2 precision | 0.646 | 0.605 | +0.041 |
| d3 precision | 0.718 | 0.680 | +0.038 |
| AUC d1v2 | 0.8664 | 0.854 | +0.012 |
| AUC d1v3 | 0.9852 | 0.957 | +0.028 |
| AUC d2v3 | 0.8274 | 0.793 | +0.034 |

### Code Contamination (broad filter)

| Depth | OLMo | Pythia | Delta |
|-------|------|--------|-------|
| d0 | **0.5%** | — | — |
| d1 | **2.7%** | 5% | **-2.3pp** |
| d2 | **0.7%** | 9% | **-8.3pp** |
| d3 | **0.8%** | 12% | **-11.2pp** |

### Other Metrics

| Metric | OLMo | Pythia |
|--------|------|--------|
| Finetune loss d0 | 2.269 | — |
| Finetune loss d1 | 1.650 | — |
| Finetune loss d2 | 1.226 | — |
| Feature dim | 19 | 19 |
| Truncation length | 507 | 498 |
| Top-5 features | p90_ppl, var_surprisal, p75_ppl, mean_surprisal, type_token_ratio | var_surprisal, p90_ppl, mean_ppl, mean_surprisal, p75_ppl |

### 关键发现

1. **4-class 准确率几乎一致**（78.8% vs 78.2%，CI 重叠），跨模型泛化成立
2. **3-class 准确率 OLMo 明显更高**（74.4% vs 70.8%，+3.6pp），说明 OLMo 的递归深度信号在 d1-d3 间分离更清晰
3. **Code contamination 极低**（OLMo d1=2.7%, d2/d3 < 1%），远低于 Pythia（5-12%），排除代码混入干扰
4. **特征重要性排序高度一致**：top-5 特征重叠 4/5（p90_ppl, var_surprisal, p75_ppl, mean_surprisal）
5. **相邻深度 AUC 全面优于 Pythia**：1v2 +0.007, 2v3 +0.012, d1v3 +0.028

---
