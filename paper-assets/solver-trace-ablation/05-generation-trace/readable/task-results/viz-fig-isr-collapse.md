# viz fig isr collapse

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_fig-isr-collapse_20260515T202603_result.json`
- **Structured JSON:** [`7d1ea0728951d18a82a7.json`](../../sessions/7d/7d1ea0728951d18a82a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图表已生成，验证通过。

**输出文件：**
- PDF: `/root/solver-trace-ablation/paper/figures/isr_collapse.pdf` (22KB)
- PNG: `/root/solver-trace-ablation/paper/figures/isr_collapse.png` (104KB, 1352×974px)

**数据汇总：**

| 条件 | Steps | ISR (proved-only) |
|------|-------|-------------------|
| Exec-only (s42) | 100 | 0.642 |
| Exec-only (s42) | 500 | 0.132 |
| Exec-only (s42) | 1000 | 0.003 |
| ISR β=0.1 (3-seed mean±std) | 500 | 0.716 ± 0.263 |
| Random β=0.1 (3-seed mean±std) | 500 | 0.117 ± 0.042 |

ISR/Random 缺少 100-step 数据，因此 exec-only 画完整 trajectory 折线，ISR 和 Random 作为 500-step 对比点（带 error bar）。

---
