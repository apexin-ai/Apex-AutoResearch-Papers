# eval cqa1 seed44 sweep

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cqa1_seed44_sweep_20260519T215208_result.json`
- **Structured JSON:** [`089a24dda4238db5ef82.json`](../../sessions/08/089a24dda4238db5ef82.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**两个 eval 都已经完成了**，结果文件完整（500 episodes，10 tasks × 50 eps）：

| 模型 | Success Rate | 95% CI |
|------|-------------|--------|
| **m64_seed44** | **64.4%** | [60.1%, 68.5%] |
| **m96_seed44** | **52.8%** | [48.4%, 57.1%] |

GPU 3 上的残留进程 685415 就是跑完这些 eval 后没退出的。现在已清理，无需重新提交。

---
