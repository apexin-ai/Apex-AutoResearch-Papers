# ops full gpu progress check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_full-gpu-progress-check_20260519T174130_result.json`
- **Structured JSON:** [`a7089b21011bb46d7c0b.json`](../../sessions/a7/a7089b21011bb46d7c0b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 4 实验进度总览

| GPU | 实验 | PID | 状态 | Util / VRAM / Temp | 进度 | 关键指标 | ETA |
|-----|------|-----|------|-------------------|------|---------|-----|
| 0 | Qwen3-8B CWM eval | 778328 | 运行 17.5h | 92% / 27.7G / 62°C | **8768/9784 (89.6%)** | acc=64.1% | ~2h |
| 1 | CLS 8B s456 train | 840928 | 运行 3.5h | 96% / 28.1G / 70°C | **9316/9335 (99.8%)** | — | **即将完成（<1min）** |
| 2 | DeepSeek CWM eval | 833667 | 运行 5h | 84% / 28.8G / 55°C | **3884/9784 (39.7%)** | acc=61.2% | ~8h |
| 3 | DeepSeek CLS s456 train | 842751 | 运行 3.2h | 100% / 28.5G / 73°C | **996/6489 (15.3%)** | ~11s/it | ~17h |

### 重点

- **GPU 0 D146 eval**：从 ~75% 推进到 89.6%，剩余 1016 样本，预计 **~2 小时完成**，acc 稳定在 64.1%
- **GPU 1 CLS 训练**：9316/9335，差 19 步，**几秒内完成**——需要关注完成后是否自动启动 eval 或需要手动接续
- GPU 2 DeepSeek CWM eval 还需约 8 小时，GPU 3 DeepSeek CLS 训练还需约 17 小时

---
