# check eval imm k07 result

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_eval_imm_k07_result_20260517T032912_result.json`
- **Structured JSON:** [`4bea1f05a85ca4fb0546.json`](../../sessions/4b/4bea1f05a85ca4fb0546.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。结果汇总：

## eval_imm_k07_object 结果

| 指标 | 值 |
|------|-----|
| **Overall SR** | **4.8%** (24/500) |
| 95% Wilson CI | [3.25%, 7.04%] |

### Per-task breakdown

| Task | Description | SR |
|------|------------|-----|
| 0 | alphabet soup → basket | 0% |
| 1 | cream cheese → basket | 0% |
| 2 | salad dressing → basket | 6% |
| 3 | bbq sauce → basket | 2% |
| **4** | **ketchup → basket** | **32%** |
| 5 | tomato sauce → basket | 6% |
| 6 | butter → basket | 2% |
| 7 | milk → basket | 0% |
| 8 | chocolate pudding → basket | 0% |
| 9 | orange juice → basket | 0% |

### 判断

**k=0.7 比 k=0.5 还差**（4.8% vs k=0.5 的 3.5-15.4%），假设被证伪。问题不在 retention ratio，而在 `acis_prune` 推理模式本身。仅 task 4 (ketchup) 有 32% 的信号，其余几乎全灭。

### GPU 状态

| GPU | 型号 | 显存占用 | 利用率 |
|-----|------|---------|--------|
| 0 | RTX PRO 6000 Blackwell (98GB) | 0 MiB | 0% |
| 1 | RTX PRO 6000 Blackwell (98GB) | 0 MiB | 0% |

**两块 GPU 完全空闲，可立即调度新实验。**

---
