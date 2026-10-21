# fix d067 paper text

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_d067-paper-text_20260527T042938_result.json`
- **Structured JSON:** [`1717f3e18ac5fbba30f7.json`](../../sessions/17/1717f3e18ac5fbba30f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修改完成，编译无错误。汇总：

| 项目 | 修改内容 |
|------|---------|
| **Table 1 Detach+LN 行** | 已有 `$^\star$` 和 `---`，无需改 |
| **Table 1 caption** | `$^\star$v1 code` → `$^\star$Trained with v1 code; v2 multi-seed results pending` |
| **正文 ΔCAR 描述** | 删除 Detach+LN 的 `$\Delta{=}+2.0$\,pp`，改为 `Detach+LN$^\star$ (0.765) shows a comparable level under v1 code` |
| **Table 2** | `Detach+LN (0.765)` → `Detach+LN$^\star$ (0.765)` |
| **Table 2 caption** | `$n{=}1$ for LN cells` → `Full OCC+LN: $n{=}1$, v2; Detach+LN: $n{=}3$, v1$^\star$` |
| **Figure 2 caption** | `LN cells have $n{=}1$` → `Full OCC+LN has $n{=}1$ (v2); Detach+LN has $n{=}3$ (v1, marked $^\star$)` |
| **appendix.tex Statistical tests** | 删除 v1 统计数据（`d ≈ -0.04, p = 0.91` 及相关句子） |
| **编译** | pdflatex 无报错 |

---
