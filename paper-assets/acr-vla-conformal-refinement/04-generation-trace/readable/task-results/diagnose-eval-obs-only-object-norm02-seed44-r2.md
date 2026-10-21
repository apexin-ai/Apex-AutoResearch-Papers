# diagnose eval obs only object norm02 seed44 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-obs-only-object-norm02-seed44-r2_20260516T144155_result.json`
- **Structured JSON:** [`f5093acc52442542c13a.json`](../../sessions/f5/f5093acc52442542c13a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**诊断结果：实验实际已正常完成，不需要重试。**

- 所有 100 次 rollout 全部执行完毕，overall success rate = 16.0% (16/100)
- 结果文件 `logs/eval_object_obs_only_norm02_seed44.json` 完整存在（1490 bytes, 写入时间 May 16 22:38）
- EXIT_CODE=129 是脚本正常退出后 wrapper/tmux 收到的 SIGHUP，属于误报
- 该结果可直接用于 3-seed Fisher test

诊断报告已写入 `artifacts/diagnose-norm02-seed44-r2.md`。

---
