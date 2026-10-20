# fix eval postprune cka only 30

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_eval_postprune_cka_only_30_20260517T215905_result.json`
- **Structured JSON:** [`fd24c05e3c7c5398a598.json`](../../sessions/fd/fd24c05e3c7c5398a598.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已正常启动，模型加载成功，正在加载 GSM8K 测试集。

**总结：**
- Tokenizer 检查结果：`pruned_cka_only_30` 目录中的 `tokenizer_config.json` 已包含 `chat_template`，tokenizer 可正常加载。之前的报错可能是临时环境问题或文件已被其他进程修复。
- 评估任务已通过 `submit_training_job` 提交到 westd-11672 cuda:2，exp_id=`eval_postprune_cka_only_30`，日志: `~/runs/recovery_aware_struct_prune/eval_postprune_cka_only_30.log`。

---
