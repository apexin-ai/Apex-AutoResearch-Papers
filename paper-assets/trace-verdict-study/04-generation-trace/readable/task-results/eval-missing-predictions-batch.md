# eval missing predictions batch

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_missing_predictions_batch_20260516T013951_result.json`
- **Structured JSON:** [`a9896a159dd159ea5e7f.json`](../../sessions/a9/a9896a159dd159ea5e7f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 全部更新完毕。

## 执行总结

### 完成
- **debugbench_vota_seed42**: predictions.jsonl 生成成功 (426 行), accuracy=99.77%, 与 registry 一致
- **deepseek_full_trace_seed42_v3**: predictions.jsonl 生成成功 (1190 行)

### 需要注意的问题
**deepseek_full_trace_seed42_v3 accuracy 异常**: 
- Registry 记录 accuracy=79.16% (pass_recall=0.851, fail_recall=0.643)
- 实际重跑结果 accuracy=28.5% (模型全部预测 fail, pass_recall=0.0, fail_recall=1.0)
- 即使用 `--max_length 16384` 也是同样结果
- 该 checkpoint 目录下已有的旧 eval_results.json 也显示 28.5%

这说明 registry 中记录的 79.16% 可能来自不同的评估流程/代码版本/checkpoint 状态。predictions.jsonl 已按当前 checkpoint 正确生成，但 paired bootstrap 检验使用时需注意此差异。

### 文件路径
- `/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace_seed42_v3/final/predictions.jsonl` (1190 行)
- `/root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_vota/final/predictions.jsonl` (426 行)

---
