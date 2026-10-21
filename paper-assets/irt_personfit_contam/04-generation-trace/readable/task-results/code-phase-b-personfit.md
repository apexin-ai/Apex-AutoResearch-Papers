# code phase b personfit

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phase_b_personfit_20260520T081354_result.json`
- **Structured JSON:** [`06a12cb58e7e90235da9.json`](../../sessions/06/06a12cb58e7e90235da9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。产出文件在 `artifacts/phase_b_results/`，脚本在 `src/phase_b_personfit.py`。

**关键结果：**

| Benchmark | lz* mean | lz* SD | sig(<-1.96) | 异常模型 |
|-----------|----------|--------|-------------|---------|
| MMLU | +24.19 | 16.47 | 1 | M2 |
| HellaSwag | +20.09 | 17.59 | 2 | M3, M8 |
| GSM8K | +8.22 | 8.97 | 2 | M3, M5 |
| ARC-C | +4.09 | 2.59 | 0 | — |
| HumanEval | +2.21 | 4.89 | 1 | M3 |

所有 benchmark 的 lz* SD 均远大于 0.5，说明模型间 person-fit 差异显著。大多数模型 lz* 显著为正（response pattern 比 IRT 模型预期更 "regular"），少数模型显著为负（M3 在 3 个 benchmark 上均异常）。

跨 benchmark Spearman 相关普遍较低（大多 p > 0.05），唯一显著的是 GSM8K vs HumanEval（ρ=0.62, p=0.031），表明 lz* 异常模式在不同 benchmark 间不太一致——person-fit 偏差是 benchmark-specific 的。

验证通过：HumanEval accuracy-theta Spearman ρ=0.87。

---
