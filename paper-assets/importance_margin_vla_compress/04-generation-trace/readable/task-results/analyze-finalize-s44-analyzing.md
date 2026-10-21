# analyze finalize s44 analyzing

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_finalize_s44_analyzing_20260528T062200_result.json`
- **Structured JSON:** [`e43dad59f797247b1242.json`](../../sessions/e4/e43dad59f797247b1242.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个 ANALYZING 实验全部处理完毕（实际发现 3 个而非 2 个），已更新至 DONE：

| Experiment | SR | Conclusion |
|---|---|---|
| `eval_pi05_attn_k09_long_seed44_strict_w38` | **64.0%** | success |
| `eval_pi05_random_k085_long_seed44_strict_w41` | **44.2%** | success |
| `eval_pi05_l2norm_k095_long_seed45_strict_w38` | **87.8%** | success |

交叉验证：Attn k=0.9 seed44 = 64.0%，与 seed42 的 64.0% 完全一致，plateau 稳定性确认。Random k=0.85 seed44 = 44.2%，与 seed42 (44.0%) / seed43 (47.2%) 一致，U-shape valley 误差棒收窄。L2norm k=0.95 seed45 = 87.8%，高位表现稳定。

---
