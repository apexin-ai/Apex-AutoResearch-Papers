# infra check exp003 progress

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_check_exp003_progress_20260513T075043_result.json`
- **Structured JSON:** [`f442c9529aacf8b2b98c.json`](../../sessions/f4/f442c9529aacf8b2b98c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
Config 1 (greedy):       进行中 — depth 0/1/2 完成, depth 3 进行中 (21/313 batches, 7%)
Config 2 (p=0.9/T=1.0):  未开始
Config 3 (p=0.95/T=0.7): 未开始
Config 4 (p=0.95/T=1.2): 未开始

GPU: 45% utilization, 3919 MiB / 24564 MiB, 50°C
```

**Config 1 详情**：
- `data_exp003_greedy/` 已有 depth_0 (4.6MB), depth_1 (6.8MB), depth_2 (6.9MB)
- depth 3 刚开始 (~2min in)，每 depth ~31min（313 batches × ~6.1s/it）
- `results_exp003_greedy/` 为空（pipeline 结束后才写评估结果）

**时间估算**：
- Config 1 剩余：depth 3 (~29min) + depth 4 (~31min) + depth 5 (~31min) ≈ **1.5h**
- Config 2-4 各需 5 个生成 depth × ~31min ≈ **2.6h/config**
- 总剩余：1.5 + 2.6×3 ≈ **9.3h**

4 个 config 串行执行（`run_exp003_ablation.sh 1 && 2 && 3 && 4`），只用了 GPU 0。

---
