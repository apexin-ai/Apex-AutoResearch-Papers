# exp tost equivalence 118

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_tost-equivalence-118_20260523T073611_result.json`
- **Structured JSON:** [`6e529f7651597a01352a.json`](../../sessions/6e/6e529f7651597a01352a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇报结果：

## TOST 等价性检验结果

**方案**：A（从 CI 反推 SE）
**等价边界**：±2pp

| Model | Δ_conflict | Δ_xnli | Diff (C−X) | SE_diff | p_TOST | 等价? |
|-------|-----------|--------|------------|---------|--------|------|
| Llama-3.1-8B | 7.27pp | 6.00pp | +1.27pp | 4.37pp | 0.434 | NO |
| Qwen-3-8B | 7.23pp | 6.72pp | +0.51pp | 4.36pp | 0.366 | NO |
| Gemma-2-9B | 6.62pp | 7.81pp | −1.19pp | 2.58pp | 0.377 | NO |

**结论**：三个模型均未通过 TOST（p > 0.05），无法在 ±2pp 边界内证明统计等价。

**但需注意**：这是 **power 不足**，不是差异大。点估计差值都在 ±1.3pp 以内（远小于 2pp 边界），但 bootstrap SE 太大（2.6–4.4pp），导致无法拒绝 H0。Gemma 的 SE 最小（2.58pp），最接近能证明等价——如果 SE 能降到 ~1.5pp（大约需要 n≈6000 bootstrap 或更多样本），Gemma 可能通过。

结果已保存至 `data/tost_equivalence_results.json`。

---
