# metrics seed43 and misc refresh

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_metrics_seed43-and-misc-refresh_20260515T121419_result.json`
- **Structured JSON:** [`dfa9a86bb1f8924384d9.json`](../../sessions/df/dfa9a86bb1f8924384d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 全部更新完成。总结：

- **bjb1-18228**：4 个实验全部存活。norm03-r2 完成 5/10，scalar-r2 完成 6/7（还剩最后 1 个 task T9），两个 seed43 实验已加载完毕正在开始 rollout。
- **bjb2-40593**：PID 227434 存活，etime 6h43m（合理，非 ghost），完成 4/10。
- 所有 JSON 输出文件尚未生成，属正常（实验完成后才写入）。
- norm03-r2 和 norm003-b2 的前 4 个 task 成绩完全一致（90%/100%/0%/30%），符合预期（同一 obs_only 模型、同 seed，只是 norm 不同但这几个 task 可能未触发差异）。scalar-r2 即将完成，预计 1h 内结束。

---
