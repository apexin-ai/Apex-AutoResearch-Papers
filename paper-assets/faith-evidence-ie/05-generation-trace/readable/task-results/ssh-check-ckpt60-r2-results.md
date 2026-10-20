# ssh check ckpt60 r2 results

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-ckpt60-r2-results_20260515T000602_result.json`
- **Structured JSON:** [`8895d4bddf2c82ef3c31.json`](../../sessions/88/8895d4bddf2c82ef3c31.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## ckpt-60 eval 结果

**进程状态**: 已正常完成，cuda:1 已释放（0 MiB, 0%）。

**结果文件**: `/root/autodl-tmp/eval_results/grpo_ced_lr5e6_ckpt60/metrics.json`

**关键指标**:

| 指标 | ckpt-20 | ckpt-40 | **ckpt-60** |
|------|---------|---------|-------------|
| rel_f1 | 0.0077 | 0.0071 | **0.0093** |
| evi_f1 | — | — | **0.8100** |
| edcr | — | — | **0.9930** |
| pred_count | — | — | **14626** (gold: 12151) |
| format_ok_rate | — | — | **99.8%** |
| precision | — | — | 0.0085 |
| recall | — | — | 0.0103 |

**结论**: rel_f1 = 0.0093，与 ckpt-20 (0.0077) 和 ckpt-40 (0.0071) 处于同一量级，无实质性提升。lr=5e-6 方案在 step 20→40→60 全程平坦（~0.007-0.009），进一步确认该学习率失败。

值得注意的是 evi_f1=0.81 和 format_ok_rate=99.8% 都很高，说明模型格式和证据引用能力正常，问题出在关系抽取本身——pred_count=14626 vs gold=12151，但 tp 只有 125，说明模型在大量产出预测但几乎全错。

---
