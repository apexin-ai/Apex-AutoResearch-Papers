# code submit 05B s123 signals cuda1

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_submit-05B-s123-signals-cuda1_20260516T020608_result.json`
- **Structured JSON:** [`50fb14eb3ebaed3d85f8.json`](../../sessions/50/50fb14eb3ebaed3d85f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cuda:1 正在跑 3B 评估任务：

- **PID**: 676497
- **显存**: 8976 MiB
- **命令**: `python evaluate.py --model-path Qwen2.5-3B --adapter-path Qwen2.5-3B_d000_s42/lora_adapter --output-dir eval_results/Qwen2.5-3B_d000_s42_a32_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned`

按 C001/C002 约束，不能提交。

**其余准备已确认**：
- 4 个 checkpoints（d000/d005/d025/d100 × s123）和 base model 均存在
- `compute_signals.py` 参数名确认：`--ref-model-path` 正确

需要你决定：
1. 等 cuda:1 评估跑完后再提交
2. 换一个空闲 GPU

要我查一下其他 GPU 的占用情况吗？

---
