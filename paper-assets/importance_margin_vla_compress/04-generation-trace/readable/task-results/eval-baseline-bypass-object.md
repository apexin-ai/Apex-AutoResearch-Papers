# eval baseline bypass object

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_baseline_bypass_object_20260517T132204_result.json`
- **Structured JSON:** [`bb6f9790d3125f22ba30.json`](../../sessions/bb/bb6f9790d3125f22ba30.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Bypass Baseline Eval 完成。结果如下：

## 结果汇报

**Overall SR: 44.8% (224/500)**
**Wilson 95% CI: [40.5%, 49.2%]**

**Checkpoint**: `checkpoints/libero_imm_twostage_fullft/stage1_done/checkpoint.pt` — 与 `eval_true_removal_k05` 使用的一致 ✓

### Per-task SR

| Task | Description | SR |
|------|------------|-----|
| T0 | alphabet soup | 11/50 (22.0%) |
| T1 | cream cheese | 30/50 (60.0%) |
| T2 | salad dressing | 21/50 (42.0%) |
| T3 | bbq sauce | 19/50 (38.0%) |
| T4 | ketchup | 29/50 (58.0%) |
| T5 | tomato sauce | 13/50 (26.0%) |
| T6 | butter | 31/50 (62.0%) |
| T7 | milk | 19/50 (38.0%) |
| T8 | chocolate pudding | 25/50 (50.0%) |
| T9 | orange juice | 26/50 (52.0%) |

所有 10 个 task 的 SR 与参考 `eval_stage1only_object.json` 完全一致（逐 task 匹配）。这验证了 bypass 模式（k_ratio=1.0, zero_mask）等价于不做任何 pruning 的前向传播，可以作为 Table 1 的 baseline SR = 44.8%。

---
