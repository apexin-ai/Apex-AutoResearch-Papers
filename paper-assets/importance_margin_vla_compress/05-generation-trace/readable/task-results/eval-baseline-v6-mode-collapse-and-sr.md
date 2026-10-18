# eval baseline v6 mode collapse and sr

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_baseline_v6_mode_collapse_and_sr_20260516T105955_result.json`
- **Structured JSON:** [`a9dcd244e1d7435c5181.json`](../../sessions/a9/a9dcd244e1d7435c5181.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE / negative。

## 总结

**Task B (Mode Collapse 验证): FAIL**
- Noise diversity std = **0.007352** (阈值 < 0.01 = FAIL)
- alpha=64 时 std=0.006，alpha=16 时 std=0.007 — 几乎无改善
- Cross-obs std = 0.096（不同 obs 可以产生不同 action），但 same-obs 不同 noise seed 仍收敛到同一 action

**Task C (Success Rate): 未执行** — mode collapse 未修复，success rate 必定 0%

**结论**: LoRA scale 不是 mode collapse 的根因。alpha 从 64 降到 16（scale 从 2.0 降到 0.5）对 ODE noise diversity 无实质改善。问题可能在 flow matching ODE + LoRA fine-tuning 的根本兼容性上 — LoRA 修改的参数子空间导致 velocity field 在推理时（从纯 noise 出发）无法正确积分，无论 scale 大小。

---
