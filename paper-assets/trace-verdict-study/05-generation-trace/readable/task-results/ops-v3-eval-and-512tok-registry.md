# ops v3 eval and 512tok registry

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_v3_eval_and_512tok_registry_20260515T233607_result.json`
- **Structured JSON:** [`a6e497d60b3158725d07.json`](../../sessions/a6/a6e497d60b3158725d07.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两项更新均成功。汇总：

### Part A: deepseek_full_trace_seed42_v3 — 已完成

PID 207777 已结束。eval 结果已在 registry 中（之前的 Worker 已更新）。

| 指标 | 值 |
|------|-----|
| accuracy | **0.7916** |
| majority_baseline | 0.7151 |
| lift | +0.0765 |
| pass_f1 | 0.854 |
| fail_f1 | 0.637 |
| accuracy CI | [0.768, 0.813] |
| n | 1190 |

Registry 状态: DONE / success。修正了 `log_path` → `/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace_seed42_v3.log`。

### Part B: full_trace_512tok_seed42 — reproduce 字段已补全

| 字段 | 值 |
|------|-----|
| pid | 197608 |
| gpu | cuda:0 |
| started_at | 2026-05-15T23:16:13Z |
| wandb_run_name | full_trace_512tok_seed42 |
| code_commit | e404237 |

训练进度: step ~140/444 (~32%), epoch ~0.68, loss 0.108, token_accuracy 0.970。

### 异常
- 512tok 日志中未见 wandb 初始化输出（grep 为空），但命令行有 `--wandb_project trace-verdict-study --wandb_run_name full_trace_512tok_seed42`。可能 wandb 输出被 tqdm 覆盖，或 wandb 未登录。建议后续确认 wandb 是否在记录。

---
