# submit eval 15B d005 d025 s123

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_eval-15B-d005-d025-s123_20260515T133817_result.json`
- **Structured JSON:** [`49438289de103f4dd570.json`](../../sessions/49/49438289de103f4dd570.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 成功启动，确认正常运行：

| 实验 | exp_id | GPU | PID | 显存 | 利用率 |
|------|--------|-----|-----|------|--------|
| 1.5B d005 s123 aligned | exp_001_eval_15B_d005_s123 | cuda:0 | 566224 | 5848MiB | 80% |
| 1.5B d025 s123 aligned | exp_001_eval_15B_d025_s123 | cuda:1 | 566311 | 5848MiB | 80% |

注意事项：
- 跳过了 merge 步骤，因为 `train_sft.py --merge` 会重新训练。改用 evaluate.py 的 `--adapter-path` 直接加载 LoRA adapter
- 发现并清理了之前的孤儿进程（PID 565095/565271），它们来自 21:39 创建的同名 tmux session，写同一输出目录。已 kill 并确认无残留数据
- 输出目录：`/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d{005,025}_s123_aligned/`

---
