# code qwen15b tail256

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qwen15b_tail256_20260517T202656_result.json`
- **Structured JSON:** [`ee3344597dc14117c459.json`](../../sessions/ee/ee3344597dc14117c459.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Loss 值应通过 wandb 记录。训练正常进行中：444 total steps，~1.05s/step，预计 ~7 分钟完成。

## 汇报

### Qwen-1.5B tail-256 训练
- **状态**: 已提交并运行中，tmux session `qwen15b_tail256`
- **GPU**: cuda:1，~1.05s/step，444 steps total，预计约 7 分钟完成训练 + eval
- **日志**: `/root/trace-verdict-study/logs/qwen15b_tail256_seed42.log`
- **Output**: `/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_tail256_seed42/`
- **wandb**: `trace-verdict-study / qwen15b_full_trace_tail256_seed42`
- 训练完成后自动跑 eval

### DeepSeek head-2048 结果（已完成）
| Metric | Value |
|--------|-------|
| **Accuracy** | **78.7%** (95% CI: [76.5%, 81.0%]) |
| Majority baseline | 71.5% |
| Lift | +7.2pp (CI: [+4.4pp, +10.2pp]) |
| Pass P/R/F1 | 0.84 / 0.86 / 0.85 |
| Fail P/R/F1 | 0.63 / 0.60 / 0.62 |

DeepSeek-6.7B head-2048 = 78.7%，和 Qwen-7B head-2048 的结果在同一水平，cross-model 一致性良好。

---
