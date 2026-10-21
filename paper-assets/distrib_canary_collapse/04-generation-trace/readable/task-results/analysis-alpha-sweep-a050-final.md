# analysis alpha sweep a050 final

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_alpha_sweep_a050_final_20260515T054443_result.json`
- **Structured JSON:** [`68ef1f54bed1ac4210f9.json`](../../sessions/68/68ef1f54bed1ac4210f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结果：

## Gen10 最终指标
| 指标 | Gen0 | Gen10 | Drift |
|------|------|-------|-------|
| token_entropy | 3.234 | 2.632 | **-18.6%** |
| ece | 0.011 | 0.102 | **+842.8%** |
| perplexity | 26.95 | 32.64 | +21.1% |
| distinct_1 | 0.098 | 0.062 | **-37.3%** |
| distinct_2 | 0.518 | 0.251 | **-51.5%** |
| distinct_3 | 0.813 | 0.387 | **-52.4%** |

## Granger 因果 (diff-permutation, 5000 perms)
| Pair | p_diff | sig? |
|------|--------|------|
| entropy→d1 | 0.095 | **No** |
| entropy→d2 | 0.097 | **No** |
| ece→d1 | 0.019 | **Yes** |
| ece→d2 | 0.039 | **Yes** |

**2/4 diff-sig** — ece 通道显著，entropy 通道不显著（p≈0.095，刚好在边界之上）。

## 关键发现
α=0.50 **不是统一的可检测性边界**，而是 **token_entropy 作为 canary 的特异性边界**。ECE 在 α=0.50 仍然是有效 canary（p=0.019-0.039），这修正了 D025 的判断：可检测性阈值因 canary 类型而异，不存在单一 α 截断点。

## Cross-alpha 规律
- 多样性崩塌 (d1/d2 drift) 在 α 上**非单调**，α=0.25 最严重
- 校准退化 (ece drift) **超线性增长**：+52% → +80% → +843% → +3700%
- Granger 可检测性跟随 ece_drift 而非 d1_drift

## α=0.75 预测
entropy 应跨过显著性门槛，预期 3/4 或 4/4 diff-sig。

**Conclusion: success** | checkpoint: `results/alpha_sweep/a050_s42/gen_10/checkpoint`

---
