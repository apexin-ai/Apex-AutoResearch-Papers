# analysis ground truth redefine b1

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_ground_truth_redefine_b1_20260516T061705_result.json`
- **Structured JSON:** [`a821df01c5e8213de361.json`](../../sessions/a8/a821df01c5e8213de361.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结论：

**新 Ground Truth 定义**（不依赖任何统计检验）：
- 标准：α=1.0 drift ≥ N× α=0.0 drift + canary 时序先于 downstream
- **8/8 pairs 在 2×/3×/5× 阈值下完全不变**（因为 canary drift ratio 远超阈值：token_entropy 11.93×, ece 73.12×）

**新 FNR = 25%**（2/8 pairs missed）：
- FN pairs: token_entropy→perplexity 和 ece→perplexity
- 原因：TY 和 permutation Granger 在这两对上 0/4 seeds 显著（短序列 T=11 功效不足）
- 旧 FNR = 0% 是基于更小的旧参考集（仅 4 pairs），新定义扩展为 8 pairs 更严格

**对 rebuttal 的意义**：ground truth 完全由可观测物理量定义，消除了循环论证；25% FNR 反映 Granger 类方法的已知功效限制而非参考集缺陷。

---
