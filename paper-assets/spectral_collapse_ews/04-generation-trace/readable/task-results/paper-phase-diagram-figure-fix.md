# paper phase diagram figure fix

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_phase-diagram-figure-fix_20260519T185510_result.json`
- **Structured JSON:** [`1ad59cb26e7a112b7e1d.json`](../../sessions/1a/1ad59cb26e7a112b7e1d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图表已修正完成。

**修改内容**：r=0 线现在使用 exp_001 (seed42) 完整 Gen 0-10 数据，显示经典 Type I 崩溃轨迹——Gen 0→2 短暂 decompression（2367→2470 峰值），随后单调下降至 Gen 10 的 2179，跨越完整 10 代。

**验证**：
- r=0 红线完整覆盖 Gen 0-10（之前错误地只到 Gen 4）
- 5 条线全部从相同 G₀=2366.68 起点出发
- r_crit 灰色带正确标注在 r=0.25 与 r=0.3 之间
- r=0.2 在 Gen 5 截断并有 "5-gen" 标注
- PDF + PNG 已保存到 `paper/figures/`

---
