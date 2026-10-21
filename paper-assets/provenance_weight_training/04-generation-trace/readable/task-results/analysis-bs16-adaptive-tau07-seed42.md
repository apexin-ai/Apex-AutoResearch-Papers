# analysis bs16 adaptive tau07 seed42

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bs16_adaptive_tau07_seed42_20260521T175441_result.json`
- **Structured JSON:** [`6c0a4e3cb6f715d3fa9a.json`](../../sessions/6c/6c0a4e3cb6f715d3fa9a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。总结：

## bs16_adaptive_tau07_seed42 实验结果

| 指标 | bs16 adaptive | bs4 adaptive (主实验) | bs4 uniform |
|------|--------------|----------------------|-------------|
| holdout_ppl | **17.631** | 17.674 | 17.694 |
| Δ vs bs4 adaptive | **−0.043** | — | — |
| train_loss | 2.537 | — | — |
| 总步数 | 6,103 | — | — |
| 训练时长 | 4h11m | — | — |

**结论：success**

bs16 adaptive (n_min=8) 的 holdout PPL 为 17.631，比 bs4 adaptive (n_min=2) 的 17.674 还低 0.043。这说明：

1. **Dual-constraint 对 batch size 鲁棒**——从 bs=4 扩大到 bs=16（n_min 从 2 涨到 8），PPL 没有变差反而微幅改善
2. **n_min=8 没有过度正则化**——担心的 "n_min 过大导致权重分布过于保守" 没有发生，ESS 约束在更大 batch 下仍能自适应调节
3. 支持论文中 "dual-constraint robustness to batch size" 的 claim

附注：bs16_uniform_seed42 仍在训练中（~93%），完成后可做配对对比确认 Δ(adaptive−uniform) 在 bs=16 下是否也存在。

---
