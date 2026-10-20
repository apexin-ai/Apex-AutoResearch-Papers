# ops verify 15B eval start

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-15B-eval-start_20260514T092606_result.json`
- **Structured JSON:** [`63772b38e1b7fc3f483e.json`](../../sessions/63/63772b38e1b7fc3f483e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**进程正常运行。**

| 项目 | 状态 |
|------|------|
| PID 336750 | 存活，已运行 7m57s，状态 Ss+ |
| 当前配置 | d000 original (Qwen2.5-1.5B + LoRA d000_s42) |
| MMLU | **已完成**，accuracy = 0.5853 (8219/14042) |
| GSM8K | **进行中**，33/1319 (~2.5%)，~6.4s/it，预计还需 ~2.3h |
| GPU 1 显存 | 5857 MiB，utilization 48% |

bitsandbytes 报了 `libnvJitLink.so.13` 加载失败的 warning，不影响推理，已正常跑过 MMLU 全量。无其他报错。

---
