# figure fix fig1 overlap

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_fix-fig1-overlap_20260522T061939_result.json`
- **Structured JSON:** [`c21781130d4f6b413e3b.json`](../../sessions/c2/c21781130d4f6b413e3b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有重叠问题已修复，验证通过。

### 修改清单

| 问题 | 修复方式 |
|------|---------|
| **跨面板箭头 (P1→P2, P2→P3)** 与面板边框重叠 | 添加 `patheffects.withStroke(linewidth=5, foreground='white')` 白色描边缓冲，zorder 提升至 7 |
| **"enabling" 标签** bbox 溢出子面板右边缘 | `enabling_x` 从 `gp_w-0.35` 内移至 `gp_w-0.6`，bbox pad 从 0.15 减至 0.1，字号 10→9.5 |
| **t+1 循环箭头** 弧线穿过 "Sample from G∩S" 方框 | 替换为 U 形折线路径：yt 左边 → x=11.45 垂直段 → Mfinal 左边，完全绕开所有 Panel 3 内部元素 |
| **No/Yes 标签** 与箭头线距离过近 | 偏移量从 0.12 增至 0.25/0.28，添加白色 bbox 背景隔离 |

### 产出文件
- `gen_fig1.py` — 本地已更新
- `fig1_framework.png` (454KB) + `fig1_framework.pdf` (56KB) — 本地 artifacts 目录已更新

---
