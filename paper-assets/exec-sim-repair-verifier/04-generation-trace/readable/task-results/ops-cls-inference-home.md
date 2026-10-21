# ops cls inference home

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cls-inference-home_20260517T044847_result.json`
- **Structured JSON:** [`1b8e3c96963ada9c8a00.json`](../../sessions/1b/1b8e3c96963ada9c8a00.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

CLS verifier inference 完成。产出汇总：

**脚本**: `/home/sonny/exec-sim-repair-verifier/cls_inference_for_rerepair.py`

**输出**: `/home/sonny/exec-sim-repair-verifier/data/re_repair_v2/cls_predictions.jsonl` (59 instances)

**统计结果**:
| 指标 | 值 |
|------|------|
| 总预测数 | 11,464 |
| Unparseable | 0 |
| Pass 预测 | 8,471 (73.9%) |
| Fail 预测 | 2,993 (26.1%) |
| 全 pass 预测的 instance | 5/59 |
| **Accuracy vs oracle** | **93.29%** |
| **F1 macro vs oracle** | **91.52%** |
| 推理耗时 | 397.7s (6.6 min) |

准确率 93.29% 远高于 test set 的 82.35%，原因是 re-repair 数据分布更偏 pass（~74% pass），模型在高 pass 比例场景下表现更好。54/59 instances 有 fail 预测，能为 condition B 提供有效信号。

---
