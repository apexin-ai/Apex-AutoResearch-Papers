# exp qwen math sft standard

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_qwen_math_sft_standard_20260520T063534_result.json`
- **Structured JSON:** [`d0125da907313bf26cac.json`](../../sessions/d0/d0125da907313bf26cac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。总结：

- **实验**: `sft_qwen_math_standard_20`，状态 RUNNING
- **服务器**: westb-23072 cuda:1，GPU 利用率 78%，显存 51GB
- **训练配置**: 7473 GSM8K 样本，2 epochs，1870 steps，~1.13s/step
- **预计完成**: ~35 分钟（约 14:50 + 35min ≈ 15:25 UTC+8）
- **输出路径**: `/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_qwen_math`
- **问题修复**: `sft_recovery.py` 的 EOS assertion 已被自动修复（支持 Qwen 的 `<|im_end|>` token）
- **Cron 自动回调**将在训练完成后触发

---
