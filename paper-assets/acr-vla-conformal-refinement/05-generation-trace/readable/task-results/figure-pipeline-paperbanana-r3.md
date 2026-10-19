# figure pipeline paperbanana r3

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_pipeline-paperbanana-r3_20260528T152223_result.json`
- **Structured JSON:** [`7c889a620a42e3772e7c.json`](../../sessions/7c/7c889a620a42e3772e7c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**输出文件**：
- PNG: `docs/paper/figures/fig1_pipeline.png` (1.8 MB, 2752×1536, 300 DPI)
- PDF: `docs/paper/figures/fig1_pipeline.pdf` (3.3 MB)

**修复记录**：
- PaperBanana asyncio 崩溃：在 `cli.py` 开头注入 `nest_asyncio.apply()` 解决 Python 3.14 event loop 冲突
- Critic agent `_parse_response` 加了 None 和 TypeError 防御

**迭代历程**（4 轮）：
1. Round 1: 结构正确但 VLA 盒子颜色错（蓝色应为灰色）、sans-serif 字体
2. Round 2: 结构严重偏离（丢弃）
3. Round 3: 结构+颜色+字体全部修正，质量大幅提升
4. Round 4: 菱形放大、虚线边框完整化、最终打磨

---
