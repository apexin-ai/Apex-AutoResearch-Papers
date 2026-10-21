# infra progress check

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_progress-check_20260522T060604_result.json`
- **Structured JSON:** [`16a6460b041d6ba87004.json`](../../sessions/16/16a6460b041d6ba87004.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 1. Gemma translate
**已停止。** 日志停在 390/1274，无 `translate_to_zh` 进程存活。可能已崩溃或被中断。

### 2. Bootstrap n=2000
两个模型都在运行中，各有 4 个条件（EN→EN, ZH→ZH, EN→ZH, ZH→EN）：

| 模型 | EN→EN | ZH→ZH | EN→ZH | ZH→EN | 进度 |
|------|-------|-------|-------|-------|------|
| **Qwen3** | done (bal_acc=0.7528±0.0168, 3838s) | **运行中** | 待跑 | 待跑 | ~25-50% |
| **Llama31** | done (bal_acc=0.7709±0.0127, 4746s) | **运行中** | 待跑 | 待跑 | ~25-50% |

EN→EN 每个耗时约 1-1.3h，估计全部完成还需 **2-4h**。结果文件尚未生成。

### 3. 额外发现：COMET 验证在跑
GPU 0/2 上有 `validate_translation.py` 进程（非原始 translate 任务）：
- Qwen3: 660/798 back-translated (~83%)
- Llama31: 640/1096 back-translated (~58%)

### 4. GPU 状态

| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| 0 | 16.5 / 97.9 GB | 20% |
| 1 | 16.5 / 97.9 GB | 12% |
| 2 | 16.5 / 97.9 GB | 21% |
| 3 | 0 / 97.9 GB | 0% (空闲) |

GPU 1 可能是 COMET 模型的共享负载，GPU 3 完全空闲。

---
