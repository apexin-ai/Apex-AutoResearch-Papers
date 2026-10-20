# paper verify figures

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_verify-figures_20260514T204938_result.json`
- **Structured JSON:** [`8767675452c5fc4ddb61.json`](../../sessions/87/8767675452c5fc4ddb61.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已存在且内容完整。验证结果：

**Figure fixes 全部未落地。**

| Figure | PDF 尺寸 | 期望 | LaTeX 环境 |
|--------|---------|------|-----------|
| fig1 | 11.63 in (旧) | 6.75 in | `figure` → 需 `figure*` |
| fig2 | 6.77 in (旧) | 3.25 in | `figure` 0.95x → 需 1x |
| fig3 | 9.77 in (旧) | 6.75 in | `figure` → 需 `figure*` |
| fig4 | 10.02 in (旧) | 6.75 in | `figure` → 需 `figure*` |

4 个 gen 脚本的 `figsize` 均未更新（fig1 仍是 15in 宽，fig2 仍是 7in 宽等）。编译无报错是因为 `includegraphics` 强制缩放，但字体被压缩到 ~5-6pt，打印不可读。

**数据一致性**: fig4 Prolog s44 ISR*=0.387 正确；fig3 ISR β=0.1 s42 Genuine=32.1%（gen 脚本）vs appendix Table 30.9%，有 1.2pp 不一致。

报告位于 `artifacts/_project/report/figure_verification_report.md`，已包含完整的修复清单。

---
