# ssh fix tmux bjb1 18228

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix-tmux-bjb1-18228_20260520T013939_result.json`
- **Structured JSON:** [`eae53e7ccee6c6aaaddf.json`](../../sessions/ea/eae53e7ccee6c6aaaddf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。结果汇总：

**tmux 清理**：`eval-vla-only-spatial-seed50` 已 kill。剩余 3 个 session 正常运行：
- `eval-vla-only-object-seed49-r2`
- `eval-crm-spatial-seed47`
- `eval-adaptive-k-p50-seed43`

**GPU 状态**：

| GPU | 利用率 | 显存占用 | 对应实验 |
|-----|--------|----------|----------|
| 0 | 20% | 5166 MiB | seed49 (vla-only-object) |
| 1 | 19% | 5148 MiB | seed50 残留进程（刚 kill session，GPU 可能还未释放） |
| 2 | 14% | 5133 MiB | crm-spatial-seed47 |
| 3 | 22% | 3824 MiB | p50-seed43 |

注意：cuda:1 仍有 ~5GB 显存占用，tmux session 已杀但 GPU 进程可能还在。需要确认是否要 kill 残留 GPU 进程？

---
