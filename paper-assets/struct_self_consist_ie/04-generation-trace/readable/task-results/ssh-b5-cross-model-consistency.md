# ssh b5 cross model consistency

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_b5-cross-model-consistency_20260520T090138_result.json`
- **Structured JSON:** [`157f4324edb95eb88900.json`](../../sessions/15/157f4324edb95eb88900.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## B5 结果汇总

**M030 校验**: Qwen greedy F1 = 0.7478 ✓ | LLaMA greedy F1 = 0.7841 (任务预期 0.745 有误，实际三种子均值 0.7842)

| Group | Degen | Uniform F1 | VC F1 | Uni ΔF1 vs greedy | VC ΔF1 vs greedy | p (uni) | p (vc) |
|---|---|---|---|---|---|---|---|
| Pure Qwen (N=8) | 10.0% | 0.7499 | 0.7448 | +0.21pp | −0.30pp | 0.031 | 0.997 |
| Pure LLaMA (N=8) | 23.4% | 0.7873 | 0.7869 | +0.33pp | +0.28pp | 0.000 | 0.000 |
| **Mixed (4Q+4L)** | **11.6%** | **0.7916** | **0.7898** | **+4.37pp** | **+4.20pp** | **0.000** | **0.000** |

**关键对比 (mixed vs pure construction)**:
- Mixed vs Pure LLaMA uniform: **+0.42pp** (p=0.000, CI [0.27, 0.58])
- Mixed vs Pure LLaMA VC: **+0.29pp** (p=0.0001, CI [0.13, 0.45])

**解读**:
- 混合的大幅 ΔF1 (+4.37pp vs Qwen greedy) 主要来自 LLaMA 本身更强 (greedy 0.784 vs 0.748)
- 但 mixed 也显著优于 pure LLaMA construction (+0.42pp uniform)，说明跨模型多样性确实带来额外增益
- 混合后 degeneracy (11.6%) 低于 LLaMA (23.4%) 但略高于 Qwen (10.0%)，两个模型的输出空间不同导致退化减少

输出: `artifacts/b5_cross_model/cross_model_results.json` (已注册)

---
