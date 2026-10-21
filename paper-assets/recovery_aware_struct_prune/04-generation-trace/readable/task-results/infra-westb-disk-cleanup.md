# infra westb disk cleanup

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_westb-disk-cleanup_20260517T094801_result.json`
- **Structured JSON:** [`d3e150a8b2d6541623b0.json`](../../sessions/d3/d3e150a8b2d6541623b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**磁盘**：数据盘已扩至 14T（50% 使用，7.2T 可用），原 250GB 满盘问题已不存在。清理释放 ~34G（189G → 155G），删除了 grpo_stage2_standard_20_v8、pruned_rasp_alpha_0.0/1.0 等废弃模型。待训练结束后可再删 checkpoint-935 回收 35G。

**实验**：
- **gradient_sft_v3**: step 1141/1870 (61%), loss 0.63, 预计 ~13 分钟完成
- **random postprune eval**: 89/200 (44%), acc=30.0%, 预计 ~86 分钟完成
- 两张 GPU 均在正常工作

报告已写入服务器和本地 artifacts 目录。

---
