# code fix fig overview auroc

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_fig_overview_auroc_20260519T011046_result.json`
- **Structured JSON:** [`be71eab7ab7d6184a8d8.json`](../../sessions/be/be71eab7ab7d6184a8d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

AUROC 已修正为 0.82，图已更新到两个位置：
- `figures/paper/fig_overview.pdf`
- `docs/paper/figures/fig_overview.pdf`（编译版本）

### 产出总结

| 项目 | 内容 |
|------|------|
| 原始脚本 | `/tmp/gen_fig_overview.py`（已被服务器清理），从 worker log 恢复 |
| 修正脚本 | `/tmp/gen_fig_overview_fixed.py` |
| 修改内容 | `AUROC ≈ 0.70` → `AUROC ≈ 0.82` |
| ρ 值 | 保持 0.39（与 caption 中 "0.38 on the primary test bed" 一致） |
| 输出路径 | `docs/paper/figures/fig_overview.pdf`, `figures/paper/fig_overview.pdf` |

注意：右面板的 y₁/y₂/y₃ 样本排列顺序与原图反转了（y₃ 在上），视觉上差异不大，语义无影响。如需严格还原顺序可再调。

---
