# check gemma gpu zero util

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gemma-gpu-zero-util_20260520T130644_result.json`
- **Structured JSON:** [`1b6564f820d2381bc231.json`](../../sessions/1b/1b6564f820d2381bc231.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. 进程状态：**全部存活，没崩**

| GPU | 利用率 | 显存 | VLLM PID | tmux session | 状态 |
|-----|--------|------|----------|-------------|------|
| 0 | **71%** | 26383/32607 MiB | 247435 | gemma-gpu0 | **正在跑 chemistry-mix** |
| 1 | **0%** | 26383/32607 MiB | 36105 | gemma-11tasks | **跑完了，空闲等待** |

### 2. 各 task episode 数

| task | episodes | 最后修改 | 状态 |
|------|----------|---------|------|
| boil | 20 | 16:09 | done |
| melt | **2** | 16:16 | **异常少，疑似早期失败/跳过** |
| identify-life-stages-1 | 20 | 18:06 | done |
| freeze | 20 | 19:25 | done |
| lifespan-longest-lived... | 20 | 20:29 | done |
| grow-fruit | 20 | 20:47 | done |
| chemistry-mix | 10 | 21:06 | **进行中 (GPU 0)** |

总计 112 episodes，7 个 task。

### 3. GPU 1 为什么 0%

gemma-11tasks session 跑完了 grow-fruit（最后一个分配的任务），打印了汇总后停了。VLLM 服务还驻留在显存里但没有请求进来，所以利用率归零。**不是崩溃，是任务跑完了。**

### 4. 需要关注

- **melt 只有 2 条**，其余 task 都是 20 条。可能是提前出错或被跳过，需要查 melt 的具体日志确认原因。
- chemistry-mix 正在 GPU 0 上跑（10/20），预计还需一段时间。
- GPU 1 的 VLLM 进程白占 26GB 显存，如果不再需要可以 kill 释放。

---
