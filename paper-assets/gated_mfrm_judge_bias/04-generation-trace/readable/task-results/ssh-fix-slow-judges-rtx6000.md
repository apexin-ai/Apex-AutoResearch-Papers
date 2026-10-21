# ssh fix slow judges rtx6000

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix_slow_judges_rtx6000_20260522T165813_result.json`
- **Structured JSON:** [`228c9586eb9240a931dc.json`](../../sessions/22/228c9586eb9240a931dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

一切恢复正常。

## 诊断与修复总结

### 根因
1. **qwen2.5-72b (port 8002)**: vLLM 在 01:02:30 因 `EngineDeadError` 崩溃（EngineCore worker 进程死亡），导致 collector 连接错误。在崩溃前 vLLM 正常运行，collector 实际已从 1640 恢复到 2180/8534。
2. **mistral-large-2 (port 8003)**: `max-model-len=8192` 不够 — 部分 prompt 7169 tokens + 1024 output = 8193 超限。同时旧 vLLM 被 kill 后子进程（EngineCore worker PID 405731）未被回收，占住 GPU 90GB 内存。

### 修复措施
1. Kill 所有残留 vLLM 进程（包括孤儿 worker 405731）
2. 重启 **qwen vLLM** → GPU 1, PID 420981, max-model-len=8192, CUDA_VISIBLE_DEVICES=1
3. 重启 **mistral vLLM** → GPU 3, PID 421050, **max-model-len=16384**, CUDA_VISIBLE_DEVICES=3

### 当前状态
| GPU | 进程 | 显存 | GPU利用率 |
|-----|------|------|-----------|
| 0 | exp009 | 74/98 GB | 67% |
| 1 | qwen vLLM (port 8002) | 90/98 GB | 96% |
| 2 | llama vLLM (port 8001) | 91/98 GB | 100% |
| 3 | mistral vLLM (port 8003) | 90/98 GB | 97% |

两个 vLLM 都在正常服务 8 并发请求，全部 200 OK，零错误。mistral 的 token 超限问题已通过提升 max-model-len 到 16384 解决。Collector 进度更新会在 tee 缓冲刷新后显示。

---
