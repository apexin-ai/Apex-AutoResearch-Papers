# monitor vllm config check 14838

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_vllm-config-check-14838_20260517T154714_result.json`
- **Structured JSON:** [`7f48ca230750f2d23887.json`](../../sessions/7f/7f48ca230750f2d23887.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

检查完成。结果如下：

## 配置一致性报告

| 端口 | GPU | 模型 | 量化 | max_model_len | gpu_mem_util | 状态 |
|------|-----|------|------|---------------|-------------|------|
| 8000 | cuda:2 | Qwen2.5-7B-Instruct | 无 | **32768** | 0.9 | 运行中 |
| 8001 | cuda:3 | Qwen2.5-7B-Instruct | 无 | **32768** | 0.9 | 运行中 |
| 8002 | cuda:0 | Qwen2.5-7B-Instruct | 无 | 4096 | 0.9 | 运行中 |
| 8003 | cuda:1 | — | — | — | — | **未运行** |

## 关键发现

**Reviewer 担心的问题不存在**：port 8002 加载的是 `Qwen2.5-7B-Instruct`，与 8000/8001 完全相同，不是 72B。

但有两个新问题：

1. **max_model_len 不一致**：8000/8001 启动时未指定 `--max-model-len`，vLLM 使用模型默认值 32768；8002 显式设置了 `--max-model-len 4096`。预期三个 7B 实例都应是 4096。

2. **Port 8003 (72B AWQ) 未运行**：进程不存在，curl 连接被拒。GPU 1 仍占用 ~87GB 显存（可能是残留未释放，或有其他进程）。

3. **启动参数差异**：8000/8001 带 `--trust-remote-code`，8002 带 `--tensor-parallel-size 1`（但无 `--trust-remote-code`）。

---
