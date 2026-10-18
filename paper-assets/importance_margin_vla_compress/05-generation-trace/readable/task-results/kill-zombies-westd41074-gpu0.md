# kill zombies westd41074 gpu0

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_kill-zombies-westd41074-gpu0_20260523T203208_result.json`
- **Structured JSON:** [`b40cd479d18bc2c4fae4.json`](../../sessions/b4/b40cd479d18bc2c4fae4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

| 项目 | 结果 |
|------|------|
| PID 834290 | KILLED |
| PID 835885 | KILLED |
| PID 843167 | SAFE（运行 54min，eval_pi05_pruning_libero.py attention keep_ratio=0.5） |
| GPU 0 显存 | 10,657 MiB / 97,887 MiB（从 ~42GB 降至 ~10.4GB） |
| GPU 0 进程 | 仅剩 843167（10,638 MiB） |

释放了约 31GB 显存，比预期更多。

---
