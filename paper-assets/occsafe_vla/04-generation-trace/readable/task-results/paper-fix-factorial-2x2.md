# paper fix factorial 2x2

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fix_factorial_2x2_20260527T201048_result.json`
- **Structured JSON:** [`4dbf90d3c1fb2a092765.json`](../../sessions/4d/4dbf90d3c1fb2a092765.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

PDF 生成成功，数据已全部更新。

## 汇报

### 1. 源代码文件路径
`artifacts/figures/gen_factorial_2x2_v2.py`（本地）

### 2. 修改的数据值

| 数据点 | 旧值 | 新值 |
|--------|------|------|
| Cell 2 LN ON (mean) | 0.740 | **0.777** |
| Cell 2 LN ON (n) | 1 | **3** |
| Cell 2 LN ON (std) | None | **0.032** |
| Cell 4 LN OFF (mean) | 0.765 | **0.826** |
| Cell 4 LN OFF (n) | 3 | **1** |
| Cell 4 LN OFF (std) | 0.023 | **None** |
| Vanilla baseline | 0.768 | **0.745** |
| LN Δ 标注 | -2.5 pp | **-4.9 pp** |
| BN Δ 标注 | -4.2 pp | -4.2 pp（不变） |
| ylim 上界 | 0.80 | **0.86** |

### 3. PDF 生成位置
- `docs/paper/figures/factorial_2x2.pdf` — 23KB, 2026-05-27 20:13
- `docs/paper/figures/factorial_2x2.png` — 127KB, 2026-05-27 20:13

---
