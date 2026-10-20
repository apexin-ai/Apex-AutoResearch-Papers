# fix figure legends

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_figure_legends_20260523T064838_result.json`
- **Structured JSON:** [`8db2641ebc36cc8f5198.json`](../../sessions/8d/8db2641ebc36cc8f5198.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**Figure 2 (`phase_diagram.pdf`)**：已将图例从 `upper left` 改为 `lower left`，PDF/PNG 已重新生成并复制到 `paper/figures/`。

**Figure 1 (`spectral_trajectory.pdf`)**：脚本 `plot_spectral_trajectory.py` 是 5 面板图（eff_rank / log_det / ppl / distinct-4 / hellaswag），**没有任何 legend 调用**，不存在图例需要移动。你描述的"SLV 双线图 r=0 solid, r=0.5 dashed"和这个脚本不匹配——可能是另一个脚本生成的，或者 Figure 1 已经换成了这个 5 面板图。需要你确认是否还需要处理 Figure 1。

---
