# eval bs8 seed456 full

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_bs8_seed456_full_20260523T223622_result.json`
- **Structured JSON:** [`c4813bb9bb5857b75f26.json`](../../sessions/c4/c4813bb9bb5857b75f26.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

## B=8 实验状态
- Adaptive seed456: **完成** `/root/autodl-tmp/provenance_weight_training/output/models/bs8_nmin4_adaptive_seed456/final`
- Uniform seed456: **完成** `/root/autodl-tmp/provenance_weight_training/output/models/bs8_nmin4_uniform_seed456/final`

## Eval 结果
- Adaptive seed456: holdout_ppl = **17.646**, loss = 2.8705
- Uniform seed456: holdout_ppl = **17.702**, loss = 2.8737
- seed456 Δ = **-0.056**

## 3-seed 统计量

| Seed | Adaptive | Uniform | Δ |
|------|----------|---------|--------|
| 42 | 17.650 | 17.694 | -0.044 |
| 123 | 17.631 | 17.687 | -0.056 |
| 456 | 17.646 | 17.702 | -0.056 |
| **Mean±SD** | **17.642±0.010** | **17.694±0.008** | **-0.052±0.007** |

**t = -13.00, df = 2, p = 0.0059**
Cohen's d = 7.51
Amplification vs B=4: **2.6×**

## results.tex 更新建议
当前: `$-$0.050 (2-seed mean)`
建议改为: `$-$0.052$\pm$0.007 (3 seeds, $p{=}0.006$)`

三个 seed 结果高度一致（SD 极小），paired t-test 在 df=2 下仍 p<0.01，效果量巨大（Cohen's d=7.51）。B=8 的 Δ 是 B=4 的 2.6 倍，dose-response 关系明确。

---
