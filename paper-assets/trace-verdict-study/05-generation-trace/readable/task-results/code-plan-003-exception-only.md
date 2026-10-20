# code plan 003 exception only

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_003_exception_only_20260515T070308_result.json`
- **Structured JSON:** [`cd02f4873e5fd59d1c41.json`](../../sessions/cd/cd02f4873e5fd59d1c41.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常推进中。

**汇总**：
- `vota_exception_only_seed42` 在 westd-11235 GPU 1 上运行
- 数据: 4720 train / 1190 test（与其他条件一致）
- 444 steps, ~6s/step, 预计 ~45 分钟完成训练
- 训练后自动链接 eval（已修补 evaluate.py 的 choices 列表）
- tmux session: `vota_exception_only_seed42`
- Registry 状态: RUNNING

---
