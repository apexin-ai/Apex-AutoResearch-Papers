# ops check grpo standard exit

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-grpo-standard-exit_20260514T213401_result.json`
- **Structured JSON:** [`7b6d328f108a26e8d595.json`](../../sessions/7b/7b6d328f108a26e8d595.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。两个实验的状态总结：

| 实验 | 步数 | 耗时 | 最终 reward | 结论 |
|------|------|------|-------------|------|
| grpo_standard_20_fast | 500/500 | 3h31m | 0.00625 | negative |
| grpo_rasp_20_fast | 500/500 | 3h32m | 0.00625 | negative |

**核心问题**：两个模型都没有产生有效学习信号。grad_norm=0、loss=0、所有生成都被截断在 max_length=1024、没有自然终止的 completion。GRPO 完全没有梯度可以学习。

**意外发现**：RASP 模型（post-prune 29% GSM8K）也未能恢复，这与假设（RASP 保留的结构能支持 GRPO 恢复）不符。可能原因：
- max_completion_length=1024 不够长，模型需要更多 token 才能生成完整推理
- 学习率或训练步数不足
- 剪枝后模型的生成能力退化严重，需要先做 SFT warmup 再上 GRPO

Registry 已更新为 ANALYZING/negative，grpo_standard_20_fast 的 cron 不存在（可能已被清除），grpo_rasp_20_fast 的 cron 已删除。下一步需要跑 formal GSM8K eval 确认最终准确率。

---
