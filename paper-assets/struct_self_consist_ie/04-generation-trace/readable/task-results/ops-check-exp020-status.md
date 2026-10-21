# ops check exp020 status

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_exp020_status_20260516T121557_result.json`
- **Structured JSON:** [`52d5944707a022816482.json`](../../sessions/52/52d5944707a022816482.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-020 Few-NERD Smoke Test 状态

**训练仍在进行中**，PID 288683，GPU 1 (RTX 5090, 27710MiB / 99% util)。

| 指标 | 值 |
|------|-----|
| 进度 | 2622 / 8236 steps (31.8%) |
| Epoch | ~0.32 |
| 已运行 | ~1h46m |
| 预计剩余 | ~3h03m |
| 当前 loss | 0.0603 (step 2600) |
| Eval loss (step 2000) | 0.0658 |
| 速度 | ~1.95 s/it |

**Loss 曲线**：从 0.96 (step 50) → 0.21 (step 100) → 0.07 (step 1700) → 0.06 (step 2600)，收敛正常。

**Checkpoints 已保存**：`checkpoint-1000`, `checkpoint-2000` 在 `/root/autodl-tmp/struct_self_consist_ie/checkpoints/ft_fewnerd_smoke/`

预计约 3 小时后训练完成。尚无 inference 结果。

---
