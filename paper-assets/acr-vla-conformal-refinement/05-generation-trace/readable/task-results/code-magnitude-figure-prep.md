# code magnitude figure prep

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_magnitude-figure-prep_20260516T201843_result.json`
- **Structured JSON:** [`8e04055bb763a8570f38.json`](../../sessions/8e/8e04055bb763a8570f38.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。产出文件：

| 文件 | 路径 |
|------|------|
| 脚本 | `artifacts/figures/magnitude_curve.py` |
| PDF | `artifacts/figures/magnitude_curve.pdf` |
| PNG | `artifacts/figures/magnitude_curve.png` |

图表要点：
- **obs_only**（蓝实线）在 ε=0.2 达峰值 22%，星号标记最优点
- **perdof**（红虚线）随 ε 增大急剧下降至 0%
- 合并的 argmin/VLA-only baseline 灰色点线在 12%
- 标注 ε=0.2 处 +11pp gap 和 ε=0.3 处 +15pp gap
- 单栏 3.5" 宽，serif 字体，可直接嵌入 LaTeX

脚本独立可运行，只依赖 matplotlib + numpy。seed45/46 数据到位后可加 error bar。

---
