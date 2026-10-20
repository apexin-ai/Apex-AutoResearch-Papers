# ops registry cleanup

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_registry-cleanup_20260522T192134_result.json`
- **Structured JSON:** [`1a2760612292a7967dcf.json`](../../sessions/1a/1a2760612292a7967dcf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息齐全，汇总如下：

```
exp_id                              | 进程 | checkpoint?                    | eval_results? | 建议终态       | 原因
------------------------------------|------|--------------------------------|---------------|----------------|------
cross_dataset_batch                 | 无   | 无（batch脚本，产出在子实验下） | 无（同上）     | DONE(success)  | 批处理脚本，4/4子实验全部DONE（cross_he2mbpp_exception_only, cross_he2mbpp_no_trace, cross_mbpp2he_exception_only, cross_mbpp2he_no_trace），EXIT_CODE=0
cross_mbpp2he_no_trace_seed42       | 无   | 有final/ (cross_mbpp2he_no_trace) | 有eval_results.json | DONE(success)  | 实际checkpoint目录名为cross_mbpp2he_no_trace（无seed42后缀），训练完成有模型和eval结果，由cross_dataset_batch在15:16完成
cross_mbpp2he_exception_only_seed42 | 无   | 有final/ (cross_mbpp2he_exception_only) | 有eval_results.json | DONE(success)  | 实际checkpoint目录名为cross_mbpp2he_exception_only（无seed42后缀），训练完成有模型和eval结果，由cross_dataset_batch在14:57完成
exc_type_only                       | 无   | 无checkpoint目录               | 无            | killed         | 无任何日志或checkpoint，从未实际提交（注：exc_type_only_seed42是另一个实验，有自己的日志）
gradient_masking_qwen7b             | 无   | 无checkpoint目录               | 无            | killed         | 无任何日志或checkpoint，从未实际提交（注：gradient_masking_qwen7b_seed42/123/456是另外的实验，有各自日志）
attention_gradient_analysis         | 无   | 无（分析脚本非训练）           | 有results.json在artifacts | DONE(success) | 分析脚本已完成，EXIT_CODE=0，产出10个文件在artifacts/attention_gradient_analysis/
```

---
