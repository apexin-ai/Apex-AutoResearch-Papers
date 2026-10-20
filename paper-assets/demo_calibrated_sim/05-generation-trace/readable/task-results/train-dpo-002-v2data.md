# train dpo 002 v2data

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_dpo-002-v2data_20260512T170432_result.json`
- **Structured JSON:** [`f8796ffdb4da67e25118.json`](../../sessions/f8/f8796ffdb4da67e25118.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**dpo-002 训练已启动**

| 项目 | 值 |
|---|---|
| v2 数据 | 1563 对 DPO pairs（messages 格式），`data/dpo_pairs_v2.jsonl` |
| 数据来源 | 37 条 calibrated + 137 条 uncalibrated traces，20 个 task 重叠 |
| device_map 修复 | `{"": 0}` → `{"": gpu_id}`，参数化 |
| GPU | cuda:3（23.1GB/24.5GB） |
| batch_size | 1（bs=4 和 bs=2 均 OOM，降到 1） |
| 总步数 | 1173 步，~3.95s/step |
| PID | 276053（tmux session: dpo002） |
| 预计时长 | ~1.3 小时 |
| 日志 | `/root/democalib/results/dpo_train_v2.log` |
| 输出 | `/root/democalib/dpo_output_v2/` |

**注意**：TRL 的 tokenizer mismatch 警告 100% 出现（v1 为 48%），这是 TRL 处理 conversational format 的固有行为，不影响训练。v2 的实际改进在于使用了正确的 chat template 格式化，让 TRL 能正确 apply template 而非依赖手动拼接的文本。

---
