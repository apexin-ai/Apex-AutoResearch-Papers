# paper fig6 data fix critical

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fig6_data_fix_critical_20260525T165049_result.json`
- **Structured JSON:** [`2ff5359fe436633b48a9.json`](../../sessions/2f/2ff5359fe436633b48a9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。修改总结：

**脚本 `fig6_multiple_pathways.py`：**
- 右列数据从 008e_v3 s2（eval 崩溃到 136.96，NVE 3.78）替换为 exp_080 s1（eval 876.7，NVE ≤ 0.6×）
- 右列颜色从红色（C_MAIN）改为绿色（C_HEALTHY = #27AE60），视觉上与左列 CIVO 崩溃形成对比
- 移除右列所有红色崩溃区域（axvspan）和崩溃标注（"eval crash -81%"、"policy destabilizing"）
- 新标注：eval 终点 "876.7 (94% baseline)"、"NVE ≤ 0.6× (calibrated)"、"entropy ↓ (normal convergence)"
- 底部注释更新为 "CIVO onset requires dt > 1 imagination (F6)"

**`results.tex` L117 caption：**
- `008e_v3 s2` → `008e_v3 s1`
- `NVE 0.5×` → `NVE ≤ 0.6×`
- `eval 64% baseline` → `eval 94% baseline`

图和 caption 现在一致：右列显示平稳上升的 eval 曲线 + 校准的 value + 正常收敛的 entropy，与 caption "no CIVO onset" 完全匹配。

---
