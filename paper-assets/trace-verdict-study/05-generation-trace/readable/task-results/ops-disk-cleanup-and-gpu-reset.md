# ops disk cleanup and gpu reset

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk_cleanup_and_gpu_reset_20260521T010737_result.json`
- **Structured JSON:** [`558153ad09d9b42da8bf.json`](../../sessions/55/558153ad09d9b42da8bf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

| 指标 | 清理前 | 清理后 |
|------|--------|--------|
| 根分区使用 | 30G / 30G (100%) | 21G / 30G (69%) |
| 可用空间 | 300K | **9.5GB** |
| outputs/ | ~6.1GB | 499MB (仅保留 final/) |
| 释放总量 | — | **~9.5GB** |

**清理明细：**
- checkpoint-* 目录：~5.7GB（18个中间 checkpoint）
- `/root/.cache/huggingface/`：~3.9GB（无关模型 gpt2/contriever/Qwen3-1.7B + wikitext 数据集）
- conda 包缓存：~107MB
- pip 缓存 + lock/incomplete 文件：少量

**GPU 状态：** 2× RTX PRO 6000 (98GB)，无残留进程，GPU 0 有 49GB 显存被 VRAM 预留占用但无计算进程。

---
