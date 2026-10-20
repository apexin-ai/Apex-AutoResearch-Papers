# d153 gpu1 ablation cwm followup

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_d153-gpu1-ablation-cwm-followup_20260519T121402_result.json`
- **Structured JSON:** [`3aef9536992d0972efa2.json`](../../sessions/3a/3aef9536992d0972efa2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**进度汇总**:

| 任务 | 状态 |
|------|------|
| ckpt-2200 eval | **完成** — accuracy=85.34%, f1_macro=79.04% |
| ckpt-3600 eval | 运行中 (10/9784, ~20min) |
| ckpt-6633 eval | 排队等 ckpt-3600 完成 |
| DeepSeek CWM eval | 排队等 CLS chain 完成 (~1h后开始, ~3h) |

tmux sessions: `cls8b-s42-ckpt-ablation`（CLS chain）, `deepseek-cwm-repo-s42-e3-seq4096-eval`（CWM 等待中）。270s 后回来检查 ckpt-3600 进度。

---
