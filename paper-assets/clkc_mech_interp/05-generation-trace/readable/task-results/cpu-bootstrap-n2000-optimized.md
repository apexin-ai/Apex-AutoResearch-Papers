# cpu bootstrap n2000 optimized

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cpu_bootstrap-n2000-optimized_20260522T081516_result.json`
- **Structured JSON:** [`65df14c1f6eec0fa92b6.json`](../../sessions/65/65df14c1f6eec0fa92b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务都在运行：

| 任务 | PID | 状态 | 进度 |
|------|-----|------|------|
| **Qwen** (36层) | 465546 | en_en 方向, 98/2000 seeds done @ 1.1min | 4方向 × ~6min ≈ **~25min 总计** |
| **Llama** (32层) | 465846 | en_en 方向, 刚开始 | **~30min 总计** |

- 旧慢速进程 331575/335148 已 kill
- 优化脚本 `src/train_probe_fast.py`: joblib 32 workers + `OMP_NUM_THREADS=2`，含 StandardScaler（匹配原脚本）、paired asymmetry CI 计算
- 预估 Qwen ~16:40 完成，Llama ~16:50 完成

---
