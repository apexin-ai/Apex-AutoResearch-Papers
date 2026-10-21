# code full trace tail truncation

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_full_trace_tail_truncation_20260517T040927_result.json`
- **Structured JSON:** [`53c852a9adc01a71662d.json`](../../sessions/53/53c852a9adc01a71662d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

## 方案选择：B + C 结合

1. **数据层（方案 C）**：写了 `data/format_tail_truncation.py`，从 raw_traces.jsonl 重新格式化 full_trace 数据，对 trace 部分做 tail-truncation（`trace_tokens[-trace_budget:]`），保留 code/test_code/suffix 完整。生成 `full_trace_tail_train.jsonl` (4720) / `full_trace_tail_test.jsonl` (1190)

2. **代码层（方案 B）**：给 `train_sft.py` 和 `evaluate.py` 添加了 `--truncation_side` 参数（`left`=保留尾部），作为二次截断的保障

## 验证结果
- 数据结构正确：code, test_code, trace marker, question 全部完整
- 5610/5910 (95%) 样本被截断
- 截断标记 `[...trace truncated...]` 放在 trace 开头（表示前面被截掉了）

## 训练状态
- PID: 327379
- GPU: cuda:1
- 已进入 tokenization 阶段，模型加载成功
- 训练 + eval 链式执行，结果将输出到 `/root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_tail_seed42/final/eval_results.json`

---
