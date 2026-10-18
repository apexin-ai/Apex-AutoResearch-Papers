# analysis eval pi05 l2norm k095 long seed42 strict

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_pi05_l2norm_k095_long_seed42_strict_20260527T094811_result.json`
- **Structured JSON:** [`ad8674e82b1db5324e91.json`](../../sessions/ad/ad8674e82b1db5324e91.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

日志中没有 W&B run ID，跳过 W&B 查询。

## 实验结果：`eval_pi05_l2norm_k095_long_seed42_strict`

**总体 Success Rate (strict): 86.2%** (431/500)

### Per-task 结果

| Task | Description | SR | Successes |
|------|------------|-----|-----------|
| T0 | put both the alphabet soup and the tomat... | 92.0% | 46/50 |
| T1 | put both the cream cheese box and the bu... | 96.0% | 48/50 |
| T2 | turn on the stove and put the moka pot o... | 96.0% | 48/50 |
| T3 | put the black bowl in the bottom drawer | **100.0%** | 50/50 |
| T4 | put the white mug on the left plate and... | 98.0% | 49/50 |
| T5 | pick up the book and place it in the bac... | 98.0% | 49/50 |
| T6 | put the white mug on the plate and put t... | **48.0%** | 24/50 |
| T7 | put both the alphabet soup and the cream... | 90.0% | 45/50 |
| T8 | put both moka pots on the stove | **46.0%** | 23/50 |
| T9 | put the yellow and white mug in the micr... | 98.0% | 49/50 |

### 分析

- **Strict vs Lenient 偏差**: 86.2% vs 87.0% = **-0.8pp**，差异极小
- **实验状态**: 正常完成，EXIT_CODE=0，无错误，总耗时 130.1 min
- **薄弱 task**: T6 (48%) 和 T8 (46%) 明显低于其他 task，均为 "put both...on..." 类双物体操作任务
- **Conclusion**: **success** — strict 值 86.2% 与 lenient 87.0% 几乎一致，确认原值可靠，L2norm k=0.95 在 Long suite 上表现稳健

---
