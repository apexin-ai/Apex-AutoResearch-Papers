# code d023 reeval check and rasp

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d023-reeval-check-and-rasp_20260515T110130_result.json`
- **Structured JSON:** [`24865770bd0c105fd71f.json`](../../sessions/24/24865770bd0c105fd71f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

排队脚本正常运行，在等 PID 509954 完成。以下是完整汇报：

---

## 任务 A: pruned_standard_20 re-eval 状态

- **状态**: 运行中，PID 509954，cuda:1
- **进度**: **63/100** (63%)
- **中间准确率**: 50-sample checkpoint 为 **28%**，eos_rate=68%，avg_len=1594
- **输出文件**: `results/reeval_pruned_standard_20.json`（尚未生成，运行完才写）
- **预计剩余**: ~12-15 分钟（37 samples，平均 ~20s/it）

## 任务 B: sft_standard_20 eval 状态

- **状态**: ✅ 已完成
- **准确率**: **64%** (64/100)
- **EOS rate**: 99%（99/100 natural EOS，仅 1 truncated）
- **平均 response 长度**: 182.48 tokens
- **结果文件**: `/root/autodl-tmp/recovery_aware_struct_prune/eval_sft_standard_20_n100.json`

## 任务 C: pruned_rasp_20 re-eval

- **cuda:1 状态**: 被 pruned_standard_20 eval 占用（13003 MiB）
- **已排队**: 创建了自动等待脚本（PID 512434），监听 PID 509954 退出后立即启动：
  ```
  CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py \
    --model_path /root/autodl-tmp/pruned_rasp_20 \
    --max_samples 100 --max_new_tokens 4096 \
    --output_path results/reeval_pruned_rasp_20_n100.json
  ```
- **日志**: `/tmp/reeval_rasp_20_n100.log`
- **注意**: 之前的 `reeval_rasp_20_gpu0.json` 只有 n=20 且 max_new_tokens=512（40% acc, eos_rate=65%），不可靠。这次用 n=100 + max_new_tokens=4096 重新验证 29% 数字。

## 任务 D: GRPO v5 进度

- **进度**: **42/250** (17%)
- **速度**: ~111s/it
- **GPU**: cuda:0，PID 498479，65187 MiB / 97887 MiB
- **ETA**: 剩余 208 steps × 111s ≈ **~6.4 小时**
- **观察**: 日志显示模型在做退化的逐步计数推理（"Step 1: magnets = 8, Step 2: magnets = 9..."），reward 信号可能有问题

---
