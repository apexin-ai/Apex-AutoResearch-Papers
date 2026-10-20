# analysis scale 14b effective rank

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_scale_14b_effective_rank_20260519T020933_result.json`
- **Structured JSON:** [`9d4d8bcbaf18fbd51cf0.json`](../../sessions/9d/9d4d8bcbaf18fbd51cf0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/scale_14b_effrank_analysis/analysis_report.md`。

核心发现总结：

**Q1 轨迹**：不是渐进上升，是 gen_0→1 的阶跃式跳变（+48.9%），随后 gen_2→10 在 82 附近稳定。一次性 regime shift。

**Q2 剪刀差**：确认存在三层剪刀差：
- effective_rank 在 gen_0→1 跳升，distinct_n 从 gen_1 开始持续下滑（d3: 0.81→0.41）
- token_entropy 与 effective_rank 在 gen_0→1 同步剧变但方向相反（entropy 降，rank 升）
- perplexity 持续线性上升，而 effective_rank 已锁定不动

**Q3 对比 410M**：410M 也有 effective_rank 上升但模式完全不同——倒 U 型（+27%，gen_4 峰值后回落），而 1.4B 是阶跃函数（+62%，plateau 不回落）。是 scale-amplified 现象，非 scale-specific。2048-dim 空间提供更多扩散自由度，更大参数量带来更锐利的 phase transition。

**Q4 机制**："Confident diffusion" 假说——collapse 使模型进入"自信但失焦"状态：token 层面更确定、更重复（low entropy, low distinct_n），但这些重复模式在 embedding 空间中分散投射到更多正交维度（high effective_rank）。α=1.00 数据进一步佐证（rank 峰值 106，perplexity 达 677）。

Paper-ready explanation 在报告末尾，两段，可直接用于 Results/Discussion。

---
