# check 4b conll completion and next

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_4b_conll_completion_and_next_20260515T190804_result.json`
- **Structured JSON:** [`798b3d4957fc1d4f3bec.json`](../../sessions/79/798b3d4957fc1d4f3bec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

一切就绪：

**诊断结果：**
- 训练停在 step 3920/4390 (epoch 4.46/5)，无 error log，原因不明
- checkpoint-3800 有效（adapter 264MB，eval_loss=0.023）

**已完成：**
- Registry 更新：metrics + notes 写入，cron 已删除
- Merge 完成：`checkpoints/qwen3-4b-conll2003-merged/` (2 shards, ~8GB)
- 推理已在运行：`exp_qwen3_4b_conll_scs_inference` tmux session 活跃，cuda:0 占用 29.5GB / 73% 利用率，进度 15% (4064/27624 prompts)

注意有一个额外的 `qwen3_4b_conll` tmux session (03:12:26 创建)，可能是重复或残留进程，建议后续确认。

---
