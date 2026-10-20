# ops gpu0 kill and submit para

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu0-kill-and-submit-para_20260515T000428_result.json`
- **Structured JSON:** [`3bb40e0d57d08b85de78.json`](../../sessions/3b/3bb40e0d57d08b85de78.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

| 步骤 | 结果 |
|------|------|
| Kill PID 461879 | 进程已不存在（kill 前已自行退出） |
| 清理空目录 | `Qwen2.5-3B_d100_v2_s42_aligned/` 已删除（空目录） |
| GPU 0 状态 | 空闲 → 已占用 |
| 提交 para eval | PID 470062, GPU 0, 7122 MiB, 正在跑 paraphrased MMLU |
| Registry | `exp_001_eval_3B_d100_v2_para_aligned` → RUNNING |
| 进程来源排查 | **不可追溯** — /proc 已消亡，bash_history 无记录，tmux 无对应 session，无 nohup 文件。最可能是某个已关闭的 tmux session 或自动化 hook 启动后 session 被清理 |

---
