# analysis random b01 cross seed interim

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_random-b01-cross-seed-interim_20260514T150143_result.json`
- **Structured JSON:** [`08beab3b76b5b8f49659.json`](../../sessions/08/08beab3b76b5b8f49659.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。已写入并注册 (art_20260514_76792b)。

**核心数字**:
- Random β=0.1 (n=2): PR=0.84±0.07, mean ISR=0.083±0.030, proved-only ISR=0.100±0.044
- ISR β=0.1 (n=3): PR=0.77±0.14, mean ISR=0.549±0.236, proved-only ISR=0.716±0.263
- 聚合 ISR 比率 6.62×，但 2/3 ISR seeds 是 conclusion duplication hacking (s43 H7=96.7%, s44 H7=86.5%)
- 同 seed 配对: s42 仅 3.24× (可能 genuine)，s44 12.97× (hacking-driven, PR 完全相同 0.89=0.89)

**D043 框架**: β=0.1 不是 sweet spot 而是 "lowest hacking rate"；Random 低 ISR 是冗余编码非推理差 (C006)。

**待办**: Random s43-r2 (ALLOCATED) 完成后补齐 3-seed；ISR s42 H7 逐样本审查决定是否 genuine。

---
