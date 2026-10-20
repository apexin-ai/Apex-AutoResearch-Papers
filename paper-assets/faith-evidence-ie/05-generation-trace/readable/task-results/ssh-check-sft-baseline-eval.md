# ssh check sft baseline eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-sft-baseline-eval_20260514T233704_result.json`
- **Structured JSON:** [`102273f533d10e8a08c0.json`](../../sessions/10/102273f533d10e8a08c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## SFT Baseline Eval 结果

**进程状态**: 正常完成（PID 104979 已退出，metrics.json 和 predictions.json 均已写入）

**关键指标**:

| 指标 | 值 |
|------|-----|
| rel_f1 | **0.4057** |
| evi_f1 | **0.7979** |
| edcr | **0.7118** |
| pred_count | 12,234 (gold: 12,151) |
| format_ok_rate | **99.80%** (983/985) |
| format_compliance_rate | 99.80% |
| field_compliance_rate | 62.64% |
| n_truncated | 367 |
| inference_time | 6138.5s (~102min) |

**结果与之前 SFT eval r2/r3 完全一致**（rel_f1=0.4057, evi_f1=0.7979），确认 apple-to-apple 对比协议复现成功。

**结果文件**: `/root/autodl-tmp/sft_baseline_eval_results/metrics.json`

**cuda:3**: 已释放（0 MiB, 0% utilization）

---
