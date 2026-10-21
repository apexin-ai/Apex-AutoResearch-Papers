# figures paperbanana calibration

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figures_paperbanana_calibration_20260524T232431_result.json`
- **Structured JSON:** [`8bfe5612bfb6519d606f.json`](../../sessions/8b/8bfe5612bfb6519d606f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

1. **PaperBanana 安装成功**（v0.1.2），但 `plot` 子命令与 gemini-2.5-pro 存在兼容性问题（thinking mode 导致 `response.text` 返回 None），已通过直接调用 Gemini API 绕过
2. **参考图已生成**：`artifacts/figures/grid_b_paperbanana_ref.png`
3. **标定参数已写入**：`artifacts/figures/paperbanana_calibrated_rc.py`

与现有 PREMIUM_RC 的主要差异：
| 参数 | PREMIUM_RC | PB Calibrated | 
|------|-----------|--------------|
| `font.size` | 8.5 | 9 |
| `xtick/ytick.labelsize` | 7.5 | 8 |
| `legend.fontsize` | 7 | 8 |
| `axes.linewidth` | 0.6 | 0.8 |
| `grid.alpha` | 0.4 | 0.3 |
| `grid.linewidth` | 0.3 | 0.5 |
| `grid.color` | #E0E0E0 | #CCCCCC |

整体方向：PB 风格偏好稍大字号、稍淡网格透明度但稍粗网格线、更显著的 axes edge。

---
