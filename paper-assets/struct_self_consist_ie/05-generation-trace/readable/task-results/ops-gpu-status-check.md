# ops gpu status check

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_status_check_20260515T114433_result.json`
- **Structured JSON:** [`66fc6c027e7997453e5b.json`](../../sessions/66/66fc6c027e7997453e5b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态报告

| GPU | 显存占用 | GPU 利用率 | 状态 | 进程 |
|-----|---------|-----------|------|------|
| GPU 0 | 30208 / 32607 MiB (93%) | 87-94% | **占用** | PID 180048 `VLLM::EngineCore` (30198 MiB) |
| GPU 1 | 4 / 32607 MiB | 0% | **空闲** | — |
| GPU 2 | 4 / 32607 MiB | 0% | **空闲** | — |
| GPU 3 | 4 / 32607 MiB | 0% | **空闲** | — |

硬件：4× RTX 5090 (32GB)，Driver 595.58.03，CUDA 13.2

## Tmux Sessions

| Session | 状态 |
|---------|------|
| `exp_011_ood_scierc_to_conll` | **运行中** — vLLM 推理进行中，进度 90% (24760/27624)，约 35s 后完成 |
| `exp_017_llama_conll_n16_r1024` | **已完成** — 停在 shell prompt，无活跃进程 |
| `exp_017_llama_conll_n16_s456_r1024` | **已完成** — 停在 shell prompt，无活跃进程 |

GPU 0 被 `exp_011_ood_scierc_to_conll` 的 vLLM 推理占用，预计 1 分钟内完成。GPU 1-3 空闲可用。

---
