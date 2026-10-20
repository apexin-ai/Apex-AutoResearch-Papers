# ops gpu5 cleanup

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu5-cleanup_20260513T235504_result.json`
- **Structured JSON:** [`a8a576d52b4b9b48d7ac.json`](../../sessions/a8/a8a576d52b4b9b48d7ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 清理报告

| 项目 | 状态 |
|------|------|
| PID 234755 (zombie eval) | 已不存在，无需 kill |
| PID 235248 | 在 GPU 0 上运行（非 GPU 5），未动它 |
| GPU 5 进程 | **无任何进程占用**，0MiB / 24564MiB，0% util |
| 旧 checkpoint 目录 | 已删除 `Qwen2.5-0.5B_d005_s42/`（仅含空的 lora_adapter） |

GPU 5 完全空闲，可以重跑 d005 SFT。

---
