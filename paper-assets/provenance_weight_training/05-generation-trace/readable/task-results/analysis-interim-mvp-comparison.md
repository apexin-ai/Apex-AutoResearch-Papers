# analysis interim mvp comparison

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_interim-mvp-comparison_20260514T110155_result.json`
- **Structured JSON:** [`e0368732eeb82e0d747b.json`](../../sessions/e0/e0368732eeb82e0d747b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已生成并注册：`artifacts/interim_mvp_analysis.md` (art_20260514_d8c3e0)

核心发现：

- **Adaptive b* 均值 PPL 17.653 vs Uniform 17.693**，改善 0.040 (−0.23%)
- **Grid b=0.5 均值 PPL 17.645** (2 seeds)，改善 0.048 (−0.27%)
- **MVP capture ratio: 83.3%**，低于 90% 阈值 → 暂定 marginal FAIL
- 主要问题：seed42 的 adaptive 完全无效 (17.69 = uniform)，seed123/456 则表现良好 (17.63/17.64)
- 效果量很小 (全部方法 PPL 范围仅 0.07)，seed 方差占信号比例大
- 最终判断需等 grid-b 完成，特别是 seed456 的 b=0.5 结果

---
