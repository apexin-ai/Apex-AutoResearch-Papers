# figure dual track dose response

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_dual_track_dose_response_20260519T042604_result.json`
- **Structured JSON:** [`6f0ee58b8a7d642bc2fa.json`](../../sessions/6f/6f0ee58b8a7d642bc2fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**产出清单**：

| 文件 | 大小 | 路径 |
|------|------|------|
| `dual_track_data.csv` | 271B | `artifacts/dual_track_figure/` |
| `dual_track_dose_response.pdf` | 29KB | `artifacts/dual_track_figure/` |
| `dual_track_dose_response.png` | 198KB | `artifacts/dual_track_figure/` |

**图表特性**：
- 左 panel: PermG bar chart，清晰展示 α=0.50→0.75 的 step transition（0%→8.3%→83.3%），含 Wilson CI error bars
- 右 panel: MMCT line+scatter，展示从 α=0.10 开始的 gradual onset（0%→12.5%→43.8%→...→81.3%），含 CI shaded band
- α=1.00 标注了 cross-architecture variance（75% vs 83.3%）
- α=0.05 和 α=0.60 用灰色虚线 + "?" 标记 pending 实验
- Okabe-Ito 色盲友好配色，300 DPI，字号 ≥ 8pt，无 em-dash

---
