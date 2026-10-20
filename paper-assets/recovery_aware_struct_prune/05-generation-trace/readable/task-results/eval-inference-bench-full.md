# eval inference bench full

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_inference_bench_full_20260517T015328_result.json`
- **Structured JSON:** [`6f16110ece27b1cbf4c7.json`](../../sessions/6f/6f16110ece27b1cbf4c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务正常运行中。Dense 模型正在加载到 GPU 2，即将开始 benchmark。

状态汇总：
- **实验**: `inference_bench_full` (RUNNING)
- **服务器**: westd-11672, cuda:2 (PID 67337)
- **模型路径**:
  - Dense: `/root/autodl-tmp/models/DeepSeek-R1-Distill-Qwen-7B`
  - RASP 20%: `/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20`
  - Standard 20%: `/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd`
- **测试矩阵**: 3 models × 3 batch_sizes × 2 seq_lengths = 18 配置
- **结果路径**: `/root/autodl-tmp/recovery_aware_struct_prune/results/inference_bench_full.json`
- **日志**: `/root/autodl-tmp/recovery_aware_struct_prune/results/inference_bench_full.log`

注意：改用 cuda:2 因为 cuda:3 正在跑 alpha ablation eval。预计运行约 30-60 分钟。

---
