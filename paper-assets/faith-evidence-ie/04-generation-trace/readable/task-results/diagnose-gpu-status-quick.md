# diagnose gpu status quick

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gpu-status-quick_20260520T145513_result.json`
- **Structured JSON:** [`3cd98dc9125c0adc4c7d.json`](../../sessions/3c/3cd98dc9125c0adc4c7d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 卡全在跑，所有进程存活：

| GPU | 显存占用 | 利用率 | 任务 | PID | 运行时间 |
|-----|---------|--------|------|-----|---------|
| 0 | 32503/97887 MiB | 91% | plan017_14b_rsft_generate_r3 | 17644 | 3h20m |
| 1 | 18879/97887 MiB | 92% | eval_llama_sft_s43_no_evidence | 27322 | 47m |
| 2 | 18879/97887 MiB | 90% | eval_llama_sft_s44_no_evidence | 29983 | 5m |
| 3 | 18879/97887 MiB | 91% | eval_llama_rsft_s44_no_evidence | 30188 | 5m |

GPU 0 的 14B RSFT generate 显存占用最大（32.5GB），3 个 eval 任务各占约 18.9GB。所有任务均正确设置了 `CUDA_VISIBLE_DEVICES` 且带 `--no_evidence` 参数。

---
