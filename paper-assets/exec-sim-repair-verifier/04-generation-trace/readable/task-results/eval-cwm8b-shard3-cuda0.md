# eval cwm8b shard3 cuda0

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cwm8b-shard3-cuda0_20260516T023620_result.json`
- **Structured JSON:** [`6e5da198c442a32139dc.json`](../../sessions/6e/6e5da198c442a32139dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Shard3 已成功启动，一切正常。

**状态汇总：**
- **GPU 0** → shard3 (PID 453335)：`test[6200:7680]`，1480 条，tmux session `shard3`
- **GPU 1** → shard2 (PID 448100)：`test[7680:]`，已完成 616 条
- **GPU 3** → v3 主跑 (PID 443221)：`test[0:]`，已完成 6224 条
- **GPU 2** → 空闲

shard3 正在快速跳过 idx 0-6199，之后开始推理 6200-7679 区间。预计 ~1480 条 / 每分钟约 57 条 ≈ 26 分钟完成。三个 shard 之间有轻微重叠（v3 和 shard3 在 6200-6224 区间），后续合并时去重即可。

---
