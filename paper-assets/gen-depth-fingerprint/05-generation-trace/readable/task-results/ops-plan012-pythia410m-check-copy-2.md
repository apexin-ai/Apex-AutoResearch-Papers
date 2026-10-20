# ops plan012 pythia410m check

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_plan012-pythia410m-check_20260516T011151_result.json`
- **Structured JSON:** [`7bc179cc4b5a85640df5.json`](../../sessions/7b/7bc179cc4b5a85640df5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验成功完成，正常退出（return code 0）。** cron 报 "no sentinel" 只是因为进程已在 cron 检查前正常结束。

### 关键结果

| 指标 | QLoRA (Pythia-410M) | XGBoost baseline | Delta |
|------|-------------------|-----------------|-------|
| **5-class macro F1** | 0.5564 ± 0.0158 | 0.5028 | **+0.0536** |
| **3-class macro F1** | 0.8703 ± 0.0220 | 0.7815 | **+0.0888** |

### Per-class F1 (5-class)

| Class | F1 |
|-------|-----|
| depth_0 | 0.991 |
| depth_1 | 0.733 |
| depth_2 | 0.347 |
| depth_3 | 0.291 |
| depth_4 | 0.420 |

### Per-class F1 (3-class)

| Class | F1 |
|-------|-----|
| gen0 | 0.991 |
| gen1 | 0.733 |
| gen2+ | 0.887 |

配置：QLoRA 4-bit, r=16, alpha=32, 3 epochs, 5-fold stratified CV, 18423 samples, 运行时间 61.8 min。结果已保存至 `results/plan012_pythia410m_results.json`。

---
