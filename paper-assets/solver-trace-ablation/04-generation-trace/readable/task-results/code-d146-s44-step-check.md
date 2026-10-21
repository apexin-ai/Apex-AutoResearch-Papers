# code d146 s44 step check

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d146-s44-step-check_20260519T192953_result.json`
- **Structured JSON:** [`05475ea3395ff187342f.json`](../../sessions/05/05475ea3395ff187342f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

| # | 问题 | 答案 |
|---|------|------|
| 1 | exec-s44 的 num_steps | **500**（pipeline 六个 run 全部是 `--num_steps 500`） |
| 2 | checkpoint 保存间隔 | **save_steps=50**，`save_total_limit=1`（只保留最新一个） |
| 3 | step 500 是否自动保存 | **是**。500 能被 50 整除会触发 checkpoint 保存，训练结束后还有 `trainer.save_model()` 写最终模型到 output_dir 根目录 |
| 4 | s44 当前 checkpoint | **checkpoint-350**（当前 step 375，~15GB 完整权重） |
| 5 | s42/s43 参考 | 均已完成：**checkpoint-500** + output_dir 根目录的最终模型文件 |

**结论：无需干预。** s44 按 500 步训练，save_steps=50 + save_total_limit=1 符合 C003 约束。到 step 500 时会自动保存 checkpoint-500 和最终模型，与 s42/s43 行为一致。按当前速率（~14s/step），约 29 分钟后完成。

---
