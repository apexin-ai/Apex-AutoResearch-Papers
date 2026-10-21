# ssh kill 5090c duplicate seed123

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill-5090c-duplicate-seed123_20260520T044411_result.json`
- **Structured JSON:** [`b2d559c1d5e06592bc52.json`](../../sessions/b2/b2d559c1d5e06592bc52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果：**

- **PID 155276 已成功 kill**（SIGTERM，无需 SIGKILL）
- **无其他 seed123 相关进程**
- **GPU 3 已释放**：0% 利用率，0 MiB 显存占用

**5090-c 当前 GPU 状态：**

| GPU | 利用率 | 显存占用 | 用途 |
|-----|--------|----------|------|
| 0 | 97% | 25885/32607 MiB | 14B fewnerd s42 训练 (llamafactory) |
| 1 | 97% | 25827/32607 MiB | 14B fewnerd s42 训练 (llamafactory) |
| 2 | 83% | 29869/32607 MiB | vLLM EngineCore（可能是 pipeline 其他推理任务） |
| 3 | **0%** | **0/32607 MiB** | **已释放** ✓ |

GPU 0-1 在跑 `train_config_qwen25_14b_fewnerd_s42.yaml` 训练，GPU 2 有个 vLLM 进程（PID 155544），不是 seed123 相关，未动。

---
