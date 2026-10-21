# ssh gpu status both servers

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu_status_both_servers_20260521T154119_result.json`
- **Structured JSON:** [`fa03770eca0e373b8b65.json`](../../sessions/fa/fa03770eca0e373b8b65.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

### autodl-5090
| GPU | Util | 显存 | 实验 |
|-----|------|------|------|
| 0 | 83% | 30152 / 32607 MiB | `run_mvp_pilot.py` — Qwen2.5-7B-Instruct, fewnerd NER, seed=456, logprobs (VLLM) |
| 1 | 84% | 30204 / 32607 MiB | 同上 (VLLM worker) |
| 2 | 80% | 30230 / 32607 MiB | 同上 (VLLM worker) |
| 3 | 54% | 29946 / 32607 MiB | 同上 (VLLM worker) |

### autodl-5090-c
| GPU | Util | 显存 | 实验 |
|-----|------|------|------|
| 0 | 0% | 0 / 32607 MiB | 空闲 |
| 1 | 0% | 0 / 32607 MiB | 空闲 |
| 2 | 0% | 0 / 32607 MiB | 空闲 |
| 3 | 0% | 0 / 32607 MiB | 空闲 |

**空闲 GPU 列表：autodl-5090-c GPU 0/1/2/3（共 4 张）**

autodl-5090 全部 4 卡被 vLLM 占满，正在跑 `e2_pretrained_fewnerd_s456` 实验（output dir: `output/e2_pretrained_fewnerd_s456/`）。

---
