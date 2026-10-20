# monitor 14838 gpu stall check

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_14838-gpu-stall-check_20260517T185123_result.json`
- **Structured JSON:** [`9e955cd2dc91172ae63e.json`](../../sessions/9e/9e955cd2dc91172ae63e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论：两个进程**完全正常**，无需干预。

**状态摘要：**

| PID | GPU | 当前任务 | 进度 | 状态 |
|-----|-----|---------|------|------|
| 321045 | cuda:0 | 第2个task, Episode 2/20 | 已完成第1个task全部20 episodes | 正常运行 |
| 321159 | cuda:2 | 第2个task, Episode 2/20 | 已完成第1个task全部20 episodes | 正常运行 |
| 69734 | cuda:1 | — | — | 正常运行 |

**为什么 nvidia-smi 显示 0% GPU util：**
- nvidia-smi 是瞬时快照。两个进程当时恰好在 step 间隙（CPU 侧处理/环境交互），不在做 inference
- 日志文件在查询前几秒仍有写入（02:52:01 和 02:52:08）
- GPU 2 显示 100% 是因为采样时刚好在推理

**额外发现：** GPU 3 上有一个 Qwen2.5-7B vLLM API server (PID 323187, port 8002)，不属于 72B collection 任务。

---
