# code death aware postprocess

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_death-aware-postprocess_20260513T191005_result.json`
- **Structured JSON:** [`fb68fed22fa1681e8091.json`](../../sessions/fb/fb68fed22fa1681e8091.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。`src/death_aware_labeling.py` 已写入服务器并验证通过。

**find-non-living-thing dry-run 结果：**
- 5 episodes → det_score=2, int_score=1, tie=2, 无 death 案例
- 90 SFT steps (det=60, int=30)
- Internal label ratio: 33.3%

该任务没有 death 案例（find-non-living-thing 不涉及致死操作），所以全部走 `both_alive` 分支按 score 比较。可以用 `--input_dirs` 逗号分隔传入多个 task 目录（如含 melt、chemistry-mix 等有 death 的任务）来看 death-aware labeling 的效果。

---
