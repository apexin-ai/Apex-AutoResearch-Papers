# ssh kill vllm 5090c

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill-vllm-5090c_20260520T120859_result.json`
- **Structured JSON:** [`a2feeb951d7368b994f8.json`](../../sessions/a2/a2feeb951d7368b994f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果：**

- PID 189534 (VLLM::EngineCore) 已成功 kill，`kill` 信号即生效，无需 `kill -9`
- **GPU 3 已完全释放**：0 MiB / 32607 MiB，利用率 0%

**当前 GPU 状态：**

| GPU | 显存占用 | 利用率 | 用途 |
|-----|---------|--------|------|
| 0 | 25885/32607 MiB | 97% | train_14b_s42 (llamafactory) |
| 1 | 25887/32607 MiB | 97% | train_14b_s42 (llamafactory) |
| 2 | 29275/32607 MiB | 84% | exp_b3_prompted_diversity.py + 新 VLLM (PID 192539) |
| 3 | **0/32607 MiB** | **0%** | **已释放** |

GPU 2 上有一个新的 VLLM 进程 (PID 192539)，属于刚启动的 `exp_b3_prompted_diversity.py`（20:04 启动），是活跃任务，非空转。

---
