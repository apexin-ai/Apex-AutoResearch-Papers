# diagnose vla only object seed49 analyzing

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_vla-only-object-seed49-analyzing_20260521T025811_result.json`
- **Structured JSON:** [`a9fda51eac9ed0d5f141.json`](../../sessions/a9/a9fda51eac9ed0d5f141.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已被手动解决。Registry 显示 `eval-vla-only-object-seed49` 已经是 **DONE/success** 状态：

- **status**: DONE
- **conclusion**: success
- **updated_at**: 2026-05-21T02:58:40（约 2 小时前已更新）
- **metrics**: SR=10%（10/100 rollouts 成功）
- **notes**: 记录了"stuck in ANALYZING >24h, manual resolution on 2026-05-21"

有人在今天凌晨已经完成了诊断和更新：
- 确认 JSON 输出完整（10 tasks × 10 rollouts = 100 total）
- Overall SR = 10%，per-task SR 范围 0.0-0.2
- 设置了 checkpoint_path = "N/A (eval-only)"

另外还存在一个 `eval-vla-only-object-seed49-r2`（在 bjb1-18228 上），状态仍为 PREPARING，看起来是之前尝试重跑但未实际启动的。

**结论：无需进一步操作。** 实验已被正确标记为 DONE/success，metrics 已记录。如果需要，我可以清理那个停留在 PREPARING 的 r2 条目。

---
