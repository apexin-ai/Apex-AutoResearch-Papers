# infra gpu status check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu-status-check_20260516T143932_result.json`
- **Structured JSON:** [`fe68003eaff97eda6a16.json`](../../sessions/fe/fe68003eaff97eda6a16.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态汇总

| GPU | 显存占用 | PID | 命令 | 状态 |
|-----|---------|-----|------|------|
| **cuda:0** | 7061/24564 MiB | 780943 | `compute_signals.py` — 3B d000_s123 mmlu s4 | **busy** |
| **cuda:1** | 3387/24564 MiB | 796913 | `compute_signals.py` — 0.5B-Instruct gsm8k s4 | **busy** |
| **cuda:2** | 0/24564 MiB | — | — | **free** |
| **cuda:3** | 0/24564 MiB | — | — | **free** |
| **cuda:4** | 8313/24564 MiB | 796493 | `evaluate.py` — Llama-3.2-3B d000_s42 aligned | **busy** |
| **cuda:5** | 3893/24564 MiB | 786898 | `evaluate.py` — Qwen2.5-1.5B-Instruct aligned | **busy** |

另外，后台有 CPU-only 的 Stan IRT 采样进程在跑（2pl_gamma 和 4pl_simple，PID 794847-794850, 797263），以及 `run_pooled_rrf_irt.py`（PID 795903）。

**空闲 GPU：cuda:2, cuda:3**

---
