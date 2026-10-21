# code figure integration

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_figure_integration_20260525T084523_result.json`
- **Structured JSON:** [`b598795cd0901a5ce602.json`](../../sessions/b5/b598795cd0901a5ce602.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 复制完成

| 图表 | 源文件 | 目标 | 大小 |
|------|--------|------|------|
| dose-response | `westd-10894:/root/autodl-tmp/analysis/dose_response_car.pdf`（May 25 16:30） | `docs/paper/figures/dose_response.pdf` | 35KB |
| factorial 2x2 | `artifacts/fig_factorial_2x2.pdf`（May 25 06:58） | `docs/paper/figures/factorial_2x2.pdf` | 25KB |

### LaTeX 引用路径

- `results.tex:70` → `figures/factorial_2x2.pdf` — **路径匹配** ✓
- `appendix.tex:97` → `figures/dose_response.pdf` — **路径匹配** ✓

### Caption 匹配检查

**`results.tex:71` (factorial 2x2)** — **匹配** ✓  
Caption 描述 BN/LN × gradient flow ON/OFF, +5.1pp/-2.2pp, 7.3pp interaction (p=0.025), error bars: cross-seed SD (n=3)。新图是 BN(蓝)/LN(橙) 分组柱状图 + p=0.025 bracket 标注，内容一致。

**`appendix.tex:98` (dose-response)** — **不匹配，需要更新** ✗

| 项目 | 旧 caption | 新图实际 |
|------|-----------|---------|
| 早期 cutoff 标记 | "Blue circles" | 实心圆（3-seed 完成）/ 空心圆（待补 seed） |
| Reverse cutoff 标记 | "Red square" | 菱形（◇） |
| Vanilla baseline | "Gray band: Vanilla ± 1 SD" | 水平虚线 |
| 新增元素 | 无 | SE error band, `n=2`/`n=1` 标注, "+0.2%" gap 标注 |

需要修改 `appendix.tex:98` 的 caption 以匹配新图。是否现在更新？

---
