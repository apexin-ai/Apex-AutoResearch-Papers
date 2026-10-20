# ssh verify 5090c gpu state

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify-5090c-gpu-state_20260520T070020_result.json`
- **Structured JSON:** [`28196f9c6665a6e49fbf.json`](../../sessions/28/28196f9c6665a6e49fbf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结果

### Hostname
`autodl-container-jb1uyxxe0t-1a1cc6c5` — 已确认连接到 autodl-5090-c。

### GPU 状态

| GPU | 显存占用 | GPU-Util | 进程 |
|-----|---------|----------|------|
| 0 | 25885/32607 MiB | **96%** | PID 56978 — 14B 训练 |
| 1 | 25827/32607 MiB | **96%** | PID 56979 — 14B 训练 |
| 2 | **29869/32607 MiB** | **0%** | PID 155544 — **VLLM::EngineCore** |
| 3 | 0/32607 MiB | 0% | 空闲 |

### 关键发现

1. **GPU 0,1** — 正在跑 14B 训练，config 为 `train_config_qwen25_14b_fewnerd_s42.yaml`，`nproc_per_node=2`，符合预期。
2. **GPU 2 — vLLM PID 155544 并未退出！** 仍然占用 ~29.8GB 显存（GPU-Util 0% 说明没有在处理请求，但进程未释放）。之前报告说该 PID 已退出是错误的。
3. **GPU 3** — 空闲。
4. **没有 32B 训练进程在此服务器上** — 之前 Worker 报告"全部 4 GPU 被 32B 训练占用"完全不符合实际。

### 结论

需要手动 kill PID 155544 释放 GPU 2 的 ~30GB 显存。之后 GPU 2,3 均可用于新任务。

---
