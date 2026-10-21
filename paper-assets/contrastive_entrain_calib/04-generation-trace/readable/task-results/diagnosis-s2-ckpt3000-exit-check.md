# diagnosis s2 ckpt3000 exit check

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_s2-ckpt3000-exit-check_20260521T092653_result.json`
- **Structured JSON:** [`721f0eac93bfb3721174.json`](../../sessions/72/721f0eac93bfb3721174.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：**Success**

362/362 samples 全部完成评估，结果如下：

| 指标 | 值 |
|------|-----|
| **ToF** | 0.0497 |
| **NoF** | 0.9503 |
| **SYCONScore** | 0.0945 |
| n_valid | 181 |
| n_invalid | 181 |
| n_total | 362 |
| 耗时 | 4488s (~75min) |

模型：Qwen3-8B + exp003_s2/checkpoint-3000 LoRA，评估数据集 calibration_v2_1_expanded.jsonl。

SYCONScore = 0.0945，ToF 极低（0.0497），NoF 极高（0.9503）——该 checkpoint 几乎不产生 sycophantic 输出，校准效果非常强，但需要结合其他 checkpoint 的分数判断是否过度校准（ToF 过低可能意味着模型变得过于"固执"）。

---
