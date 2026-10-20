# ssh kill mistral restart local judges

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill-mistral-restart-local-judges_20260524T090047_result.json`
- **Structured JSON:** [`1e5e137d35faeda7bf52.json`](../../sessions/1e/1e5e137d35faeda7bf52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

执行完成。最终状态：

```
Mistral: KILLED ✅ (cuda:3 完全释放, 0 MiB)

LLaMA: PID=564416, workers=32, records/min≈14.5, ETA≈19h
  - 当前 1245/18000 records (18 models × 500 prompts × 2 positions)

Qwen:  PID=564492, workers=32, records/min≈16.0, ETA≈18h
  - 当前 800/18000 records

GPU: cuda:0 FREE, cuda:1 LLaMA vLLM 100%, cuda:2 Qwen vLLM 100%, cuda:3 FREE
Disk: 40% (19G available)
```

**说明**：collect.py 无 `--models` 参数，但有 resume（自动跳过已完成记录）。所有 18 个模型在 n17 结果中均只 ~6% 进度，因此用完整 config + workers=32 重启，resume 跳过已完成条目的开销可忽略，实际效果等同于"仅跑新模型"。API judges（sonnet/gemini/deepseek/qwen3）未受影响，继续运行。

---
