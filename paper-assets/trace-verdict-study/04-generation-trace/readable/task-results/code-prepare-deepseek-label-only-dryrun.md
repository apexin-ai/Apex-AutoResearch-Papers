# code prepare deepseek label only dryrun

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare_deepseek_label_only_dryrun_20260519T175329_result.json`
- **Structured JSON:** [`d419e599e9f9be3713fc.json`](../../sessions/d4/d419e599e9f9be3713fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`eval_results_maxlen2048.json` 确认了 79.16% 的 baseline。所有验证完成。

## 验证结果汇总

| 检查项 | 状态 | 详情 |
|--------|------|------|
| `--label_only_loss` 参数支持 | **通过** | train_sft.py 第124行定义，第138/152/168/219行使用 |
| full_trace 数据文件 | **通过** | train 30.7MB / test 7.7MB，train 共 **4720 行** |
| DeepSeek 模型 | **通过** | config.json 存在于预期路径 |
| 输出目录冲突 | **无冲突** | `deepseek_label_only_seed42/` 目录不存在 |
| Baseline 结果 (deepseek_full_trace_seed42_v3) | **确认** | `eval_results_maxlen2048.json` accuracy = **79.16%**，pass_F1=85.4%，fail_F1=63.7% |

**注意**：默认的 `eval_results.json` 结果异常（28.5% accuracy，全部预测为 fail），79.16% 来自 `eval_results_maxlen2048.json`。提交 label_only 实验后评估时可能需要同样指定 max_len=2048。

**无阻塞问题，预期提交命令可直接使用。**

---
