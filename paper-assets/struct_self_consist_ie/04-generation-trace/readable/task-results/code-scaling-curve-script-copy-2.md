# code scaling curve script

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_scaling-curve-script_20260519T170619_result.json`
- **Structured JSON:** [`ad825da2dd4009872acb.json`](../../sessions/ad/ad825da2dd4009872acb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本和草图已就绪。

**产出：**
- 脚本：`artifacts/plot_scaling_curve.py`
- 草图：`artifacts/scaling_curve_draft.pdf` / `.png`（+ 单独的 `scaling_signal_rho`、`scaling_degeneracy`、`scaling_construction_delta`）

**布局：**
- Row 1：3 个 subplot，每个 dataset 一幅 signal ρ vs model size（LP/SJ/VC 三条线，FT solid / ZS dashed）
- Row 2 左：degeneracy rate，右：greedy F1（bonus 参考）
- Row 3：construction ΔF1，绿色/红色背景区分正负

**填入新数据的方式：** 修改脚本顶部 `DATA` dict 中对应 `(size, regime, dataset)` 的 `None` 值即可，重新 `python3 plot_scaling_curve.py` 生成。

---
