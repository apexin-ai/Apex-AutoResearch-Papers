# ops kill invalid eval

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_invalid_eval_20260518T011509_result.json`
- **Structured JSON:** [`623060783c1f0f70b606.json`](../../sessions/62/623060783c1f0f70b606.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

### Kill 结果
旧的错误 eval 进程 (363261, 364260) **已自行退出**。新的正确 eval 已被启动并在运行中。

### GPU 状态
| GPU | 显存占用 | 任务 |
|-----|---------|------|
| 0 | 3352 MiB | M=32 正确 eval（ep 144/500） |
| 1 | 3494 MiB | M=64 正确 eval（ep 127/500） |
| 2 | 2787 MiB | M=96 训练 |
| 3 | 2815 MiB | M=16 训练 |

### 训练进度
- **M=96**: step 65850/100000 (65.9%), loss=0.13, sps=4.1
- **M=16**: step 62550/100000 (62.6%), loss=0.03, sps=4.2

### Eval 进度
- **M=32**: ep 144/500 (28.8%)，最近 5 个 episode 4 SUCCESS 1 FAIL
- **M=64**: ep 127/500 (25.4%)，最近 5 个 episode 3 SUCCESS 2 FAIL

四个 GPU 都在正常工作，无需额外操作。

---
