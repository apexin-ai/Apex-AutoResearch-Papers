# ops check math500 sft cka only v3

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_math500_sft_cka_only_v3_20260518T170320_result.json`
- **Structured JSON:** [`9f64269971bb8718ab30.json`](../../sessions/9f/9f64269971bb8718ab30.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/failed。

**结果汇总：**

| 项目 | 值 |
|------|-----|
| 状态 | 失败 (timeout) |
| EXIT_CODE | 124 (被 `timeout` 命令杀掉) |
| 进度 | 170/500 (34%) |
| 运行时间 | ~3h55m (21:01 → 00:57) |
| 中间准确率 | 150题时 36.67% |
| 结果文件 | 无（未完成，未写入） |

**失败原因**：评估脚本被外层 `timeout` 命令终止。MATH-500 推理速度非常慢（平均每题约 1.4 分钟），按此速度跑完 500 题需要 ~11.5 小时，远超设定的 timeout 阈值。

如需重跑，建议延长 timeout 或加 `--max_new_tokens` 限制生成长度。

---
