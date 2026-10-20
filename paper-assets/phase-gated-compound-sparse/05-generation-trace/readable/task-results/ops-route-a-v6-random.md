# ops route a v6 random

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_route-a-v6-random_20260514T050646_result.json`
- **Structured JSON:** [`30c318e4caefd84cf738.json`](../../sessions/30/30c318e4caefd84cf738.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 0 上的 PID 71626 是另一个 worker 的 `diagnose_nan.py`（15GB），不影响我们的实验——GPU 0 总共 98GB，两个进程加起来约 30GB，空间充裕。

**汇报：**

| 实验 | GPU | PID | 状态 |
|------|-----|-----|------|
| v6_random_s015 | cuda:0 | 72073 | RUNNING，模型已加载 |
| v6_random_s020 | cuda:1 | 71488 | RUNNING，模型已加载（15GB） |

- GPU 0/1 上的 Qwen importance 残留进程（68743/68885）已清理
- GPU 2/3 上的进程未受影响
- 两个实验 timeout 3h，output 分别在 `profiling_output_v6_random_s015` 和 `profiling_output_v6_random_s020`

---
