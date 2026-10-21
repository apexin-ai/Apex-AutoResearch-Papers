# collect exp 028 results

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_collect_exp_028_results_20260517T202458_result.json`
- **Structured JSON:** [`ad05d92dd92f1479b734.json`](../../sessions/ad/ad05d92dd92f1479b734.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp_028 结果已收集并写入 memory.md。关键发现：

**exp_028 5-epoch Few-NERD 结论：NEGATIVE**

| Metric | 3-epoch (exp-021) | 5-epoch (exp-028) | Delta |
|--------|-------------------|-------------------|-------|
| Degeneracy (CF1) | 11.1% | **31.3%** | +20.2pp |
| Greedy F1 | 0.7478 | 0.7773 | +2.95pp |
| LP sel delta | +1.37pp | **+0.62pp** | -0.75 |
| LP ρ (global) | — | 0.4495 | — |
| SJ ρ (global) | — | 0.3777 | — |

核心问题：5-epoch 训练使 degeneracy 从 11.1% 跃升至 31.3%。Few-NERD 之前的低 degeneracy 可能源于模型 under-convergence，而非任务本质特性。结构信号（SJ/FK/EM/VC）selection delta 全为负，仅 LP 仍为正（+0.62pp）。论文叙事需要修正。

---
