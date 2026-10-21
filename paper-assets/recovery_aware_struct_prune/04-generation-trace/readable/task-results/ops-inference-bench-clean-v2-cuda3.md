# ops inference bench clean v2 cuda3

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_inference_bench_clean_v2_cuda3_20260519T014113_result.json`
- **Structured JSON:** [`f82c4ae38870a72a3570.json`](../../sessions/f8/f82c4ae38870a72a3570.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已提交。

**状态汇总：**
- **exp_id**: `inference_bench_clean_v2`
- **GPU**: westd-29022 cuda:3（干净，0 MiB / 0% util）
- **三个模型**: Dense (7B) / CKA-only 20% / Standard 20%，路径均确认存在
- **配置**: 50 prompts × 256 max_new_tokens，GSM8K 测试集
- **输出**: `/root/autodl-tmp/recovery_aware_struct_prune/results/inference_bench_clean_v2.json`
- **日志**: `~/runs/recovery_aware_struct_prune/inference_bench_clean_v2.log`
- **预计完成**: ~20 分钟（3 模型 × warmup + 50 prompts 各两次 generate）

---
