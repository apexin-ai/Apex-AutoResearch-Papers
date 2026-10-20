# ops eval exc message and submit next

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval-exc-message-and-submit-next_20260522T125358_result.json`
- **Structured JSON:** [`12515beb9442a764ef43.json`](../../sessions/12/12515beb9442a764ef43.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正在正常进行中（step 15/444）。

## 汇报

### exc_message_only_seed42 评估结果

| 指标 | 值 |
|------|-----|
| **accuracy** | **99.5%** (CI: [99.1%, 99.8%]) |
| pass_precision | 1.000 |
| pass_recall | 0.993 |
| pass_f1 | 0.996 |
| fail_precision | 0.983 |
| fail_recall | 1.000 |
| fail_f1 | 0.991 |
| n_test | 1190 |

对比同系列消融实验：
- exc_stacktrace_only: 99.8%
- **exc_message_only: 99.5%**
- exc_type_only: 待评估

三个子组件均保持极高准确率，message_only 仅比 stacktrace_only 低 0.3pp。

### gradient_masking_qwen7b_seed123

**已在运行中**（之前已提交），当前进度 step 15/444，~14s/step，预计还需约 1.5 小时完成。

### GPU 利用情况

| GPU | 利用率 | 显存 |
|-----|--------|------|
| cuda:0 | 0% | 49175/97887 MiB（有残留显存） |
| cuda:1 | 100% | 56085/97887 MiB（训练中） |

注意：用户提供的训练命令包含多个不存在的参数（`--epochs`, `--lr`, `--batch_size`, `--gradient_accumulation_steps`, `--max_seq_len`, `--model_name`），已提交的任务使用了脚本实际支持的参数。Registry 已更新 exc_message_only_seed42 为 DONE。

---
