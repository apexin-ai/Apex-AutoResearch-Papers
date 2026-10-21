# ssh harvest cka only 15 seed123 final

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_harvest_cka_only_15_seed123_final_20260520T230609_result.json`
- **Structured JSON:** [`928ae856beab203d6a29.json`](../../sessions/92/928ae856beab203d6a29.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果汇总：**

**CKA-only 15% seed123 GSM8K eval 失败。** 进程退出码 1，未生成结果 JSON。

**失败原因链：**
1. GRPO 训练（同一 nohup 脚本）在保存最终模型时因 **磁盘满（No space left on device）** 崩溃
2. Eval 从 `checkpoint-100` 加载模型后开始评估，进度到 ~796/1319（60%）时中断
3. 日志最后一条 Progress 报告：**750/1319, acc=73.20%**（中间值，非最终结果）
4. 之后进度条显示评估速度骤降（从 ~3s/it 到 109-183s/it），最终被杀

**当前磁盘：** 数据盘 63GB 可用（已恢复），根分区 26GB 可用。磁盘满问题已解除，可以重跑。

**需要重跑此 eval。** Checkpoint-100 模型文件存在于 `/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_15_seed123/checkpoint-100`，可直接用它重新跑 GSM8K eval。

---
