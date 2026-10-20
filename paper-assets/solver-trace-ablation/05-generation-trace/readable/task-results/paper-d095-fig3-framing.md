# paper d095 fig3 framing

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_d095-fig3-framing_20260515T195733_result.json`
- **Structured JSON:** [`4118864ef73bc9ff72e5.json`](../../sessions/41/4118864ef73bc9ff72e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All changes verified. Summary:

**子任务 1 — fig3 更新完成**：
- `paper/figures/gen_fig3.py` 和 `figures/paper/gen_fig3.py` 均已更新为 D095 数据
- 数据：Random β=0.1 H7 从 0→13.7%, ISR β=0.1 H7 从 69.7→70.6%, genuine 和 other 相应调整
- 注释从 `69.7% H7 (0% in Random)` → `ISR H7: 70.6% vs Random: 13.7%`
- PDF/PNG 已重新生成（4 个文件）

**子任务 2 — paper_framing.md 更新完成**（8 处修改）：
- L117: s43 行填入 PR=92%, ISR*=0.180, H7=7.6%, H1=89.1%, genuine=3.3%
- L119: 2-seed mean → 3-seed mean±std (PR=54.3±35.1%, ISR*=0.091±0.090, pooled H7=6.7%, H1=91.4%, genuine=1.8%)
- L113: 表头 `s43 训练中` → `全部完成`
- L125: 去掉 `（待 s43 确认）`
- L131: β dose-response 表 Random PR/ISR 列填入 3-seed 数据
- L234: Goodhart landscape 表 random β=0.3 s43 行填入完整数据
- L121: D060 叙事 `2-seed mean PR=35.5%` → `3-seed mean PR=54.3±35.1%`

---
