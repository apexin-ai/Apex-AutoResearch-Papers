# submit crossover batch

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_crossover-batch_20260514T002221_result.json`
- **Structured JSON:** [`fd122328c732b34b2bbc.json`](../../sessions/fd/fd122328c732b34b2bbc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个实验全部提交成功，registry 已更新为 RUNNING。

| exp_id | sparsity | GPU | PID | 状态 |
|--------|----------|-----|-----|------|
| mvp_v4_legacy_s025 | 0.25 | cuda:0 | 38120 | RUNNING, [3/50] |
| mvp_v4_legacy_s035 | 0.35 | cuda:1 | 38996 | RUNNING, [1/50] |
| mvp_ii_profiling_v4d | 0.40 | cuda:2 | 39843 | RUNNING, [1/50] |

日志路径：`/root/autodl-tmp/pacs/profiling_output_v4_s0{25,35,40}.log`。预计每个约 30 分钟完成。

---
