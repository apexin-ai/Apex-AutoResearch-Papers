# ops cleanup tmux d005 15B

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cleanup_tmux_d005_15B_20260514T031659_result.json`
- **Structured JSON:** [`e769b39df009cae64a8e.json`](../../sessions/e7/e769b39df009cae64a8e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果：**

| 项目 | 状态 |
|------|------|
| tmux `exp_001_sft_d005_15B` | 已清理 |
| GPU 4 显存 | 18545 MiB / 24564 MiB (75.5%) |
| GPU 4 利用率 | 30% |
| GPU 4 残留进程 | PID 271921, python, 占用 18536 MiB |

GPU 4 上仍有一个 python 进程（PID 271921）占用约 18.5GB 显存。这个进程可能来自其他 tmux 会话（如 `exp_001_sft_d100_15B_v2` 或 eval 相关会话）。是否需要进一步排查或清理？

---
