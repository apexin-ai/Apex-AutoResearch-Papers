# code redraw appendix figs

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_redraw_appendix_figs_20260524T144214_result.json`
- **Structured JSON:** [`5338c643773e9c24e995.json`](../../sessions/53/5338c643773e9c24e995.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 10 个脚本已更新并成功生成 12 个图（含 kl_ar_gar 的两个子图）。

变更摘要：
- 每个脚本移除了独立的 `matplotlib.use('Agg')` + `rcParams.update({...})` + 硬编码颜色 + 手动 `savefig`
- 统一替换为 `from palette import *` + `apply_style()` + palette 颜色变量 + `save_fig()`
- 颜色映射：TG→`C_TG`(steel blue), UG→`C_UG`(sage green), LoRA→`C_LO`(muted gold), PCGrad→`C_PC`(dusty rose), SS→`C_SS`(terracotta), Base→`C_BASE`(cool gray), TF/AR semantic→`C_TF`/`C_AR`
- heatmap 的 colormap 保持不变，仅更新 rcParams 和注解颜色

---
