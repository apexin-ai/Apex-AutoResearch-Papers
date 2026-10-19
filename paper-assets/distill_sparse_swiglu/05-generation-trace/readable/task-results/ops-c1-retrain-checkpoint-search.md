# ops c1 retrain checkpoint search

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_c1-retrain-checkpoint-search_20260519T031853_result.json`
- **Structured JSON:** [`d2e7311beb222f467e37.json`](../../sessions/d2/d2e7311beb222f467e37.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个都进入 winogrande + mmlu（5-shot）。MMLU 有 57 个子任务，约需 10-15 分钟。之后还有 gsm8k。总计还需 15-25 分钟。

Benchmark eval 还在运行中。以下是目前已有的结果汇总：

## 当前状态

**训练完成：**
- `c1_retrain_30pct_s123`: 1000 steps, 878s, EXIT_CODE=0
- `c1_retrain_30pct_s456`: 1000 steps, 876s, EXIT_CODE=0

**训练内部 eval（来自 train_bce_kl_targets.py）：**
- s123: KL PPL=11.79, BCE PPL=22.51
- s456: KL PPL=11.79, BCE PPL=22.51

**Benchmark eval 进度：**
- WikiText-2 PPL: s123=8.8372, s456=8.8181 ✅
- ARC-Challenge: 已完成，结果待最终日志刷出
- Winogrande + MMLU: 正在运行
- GSM8K: 待运行

Eval 任务在 westd-41718 上两张 GPU 并行执行，预计还需 15-25 分钟。日志路径：
- `~/runs/distill_sparse_swiglu/eval_c1_retrain_30pct_s123.log`
- `~/runs/distill_sparse_swiglu/eval_c1_retrain_30pct_s456.log`

需要我继续等待并汇报最终结果，还是你之后自己查看？

---
