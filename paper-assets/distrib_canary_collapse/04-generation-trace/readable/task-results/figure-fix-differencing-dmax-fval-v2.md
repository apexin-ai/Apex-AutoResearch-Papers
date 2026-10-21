# figure fix differencing dmax fval v2

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_fix-differencing-dmax-fval-v2_20260515T180921_result.json`
- **Structured JSON:** [`df6b4614f8948eafc672.json`](../../sessions/df/df6b4614f8948eafc672.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。修改汇总：

**数据验证（与上次审计一致）：**
| pair | differenced F | undifferenced F |
|------|--------------|-----------------|
| token_entropy→d1 | 612–2615 | 200–501 |
| token_entropy→d2 | 226–1798 | 114–550 |
| token_entropy→d3 | 95–738 | 101–232 |
| ece→d1 | 567–6124 | 84–3370 |
| ece→d2 | 171–7643 | 124–249 |
| ece→d3 | 71–921 | 74–236 |

**修正内容（`gen_fig_differencing_dmax.py` 第47行）：**
- Undifferenced: `F = 200–501` → `F = 74–3370`
- Differenced: `F = 612–2615` → `F = 71–7643`

PDF/PNG 已重新生成并注册（`art_20260515_2e7869`）。

---
