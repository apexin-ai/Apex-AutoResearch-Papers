# ssh diagnose seed123 eval exit

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_diagnose_seed123_eval_exit_20260522T143716_result.json`
- **Structured JSON:** [`a515b1de126fe27d7ca3.json`](../../sessions/a5/a515b1de126fe27d7ca3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

1. **进程状态**: PID 46229 已退出（ps 无输出，exit code 1）
2. **结果 JSON**: 存在，eval 完整完成
3. **结果**:
   - **accuracy: 51.25%** (676/1319)
   - stderr: 0.0138
   - EOS rate: 99.2% (1309 natural / 10 truncated)
   - avg response length: 184.2 tokens
   - 模型路径: `grpo_random_20_seed123/checkpoint-100`

注意：最终 accuracy 51.25% 比上次检查时的中间值 52.0% 略低。此结果已标记作废（v1 GRPO batch_size=1 错误）。

磁盘: `/root/autodl-tmp/` 85% (551G/650G, 100G 可用)，正常。

---
