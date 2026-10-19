# analyze eval vla only goal seed47

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-vla-only-goal-seed47_20260520T121700_result.json`
- **Structured JSON:** [`bfc4502bc8c2a8b353b8.json`](../../sessions/bf/bfc4502bc8c2a8b353b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。总结：

**eval-vla-only-goal-seed47: FAILED（不完整）**

- 仅完成 2/10 tasks，无 JSON 输出
- 部分结果：`open_the_middle_drawer_of_the_cabinet` 80%, `put_the_bowl_on_the_stove` 90%
- 进程在 `CUDA_VISIBLE_DEVICES=4` 上运行，`EXIT_CODE=0` 但日志仅 18 行，推测被 OOM 或其他原因提前终止
- 这是该实验的第 2 次失败（registry 显示 `retry_count: 1`，上次 conclusion 也是 `killed`）
- Registry 状态：`conclusion=failed`，metrics 标记 `incomplete=true`

**需要重新提交该实验。** 建议排查 GPU 4 的显存占用情况后再重试，或换一张空闲 GPU。Goal VLA-only 目前仍为 n=6（seed42/43/44/45/46/49，均值 0.687）。

---
