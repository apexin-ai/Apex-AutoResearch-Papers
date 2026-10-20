# fix reml 500iter

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_reml_500iter_20260521T060958_result.json`
- **Structured JSON:** [`a7816dcca49afeb8bd34.json`](../../sessions/a7/a7816dcca49afeb8bd34.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇报

### 1. 收敛状态
**converged = false**，500 迭代仍未达到 tol=1e-8。最终 Δ=2.12e-03（从 100 迭代时的 ~1.1e-02 降至 ~2.1e-03）。EM 算法的线性收敛特性导致需要远超 500 次迭代才能达到 1e-8 精度。

### 2. 实际迭代次数
500 次，耗时 1304.9 秒（~21.7 分钟）。

### 3. 新旧差异
**没有任何分量差异超过 0.1pp。** 最大差异仅 0.003pp（model 分量：0.488% → 0.490%）。所有主要分量在小数点后第三位完全一致。

### 4. 完整方差分量表

| Component | Estimate | % |
|---|---|---|
| item_id | 0.081097 | 38.424% |
| model:item_id | 0.055636 | 26.361% |
| residual | 0.051517 | 24.409% |
| prompt_template:item_id | 0.005960 | 2.824% |
| seed:item_id | 0.005283 | 2.503% |
| precision:item_id | 0.004184 | 1.982% |
| model:precision | 0.002767 | 1.311% |
| temperature:item_id | 0.002155 | 1.021% |
| ordering:item_id | 0.001332 | 0.631% |
| model | 0.001035 | 0.490% |
| 其余 18 个分量 | — | < 0.02% each |

**结论：100 迭代的结果虽然 converged=false，但估计值已经实质收敛。500 迭代结果与 100 迭代差异微乎其微（<0.003pp），可以放心使用。** 500 迭代结果保存在 `results/analysis/cross_model_reml_500iter.json`。

---
