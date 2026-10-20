# ops qwen14b gsm8k eval 3gpu

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_qwen14b-gsm8k-eval-3gpu_20260521T035128_result.json`
- **Structured JSON:** [`0e61dbdf4e728fb847ac.json`](../../sessions/0e/0e61dbdf4e728fb847ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个 eval 全部成功启动并在加载模型。

**启动确认：**

| 实验 | GPU | 显存占用 | 状态 |
|------|-----|---------|------|
| eval_qwen14b_gsm8k_d000_s0 | cuda:0 | 28731 MiB / 97887 MiB | 模型加载中 |
| eval_qwen14b_gsm8k_d005_s0 | cuda:2 | 28731 MiB / 97887 MiB | 模型加载中 |
| eval_qwen14b_gsm8k_d025_s0 | cuda:3 | 28731 MiB / 97887 MiB | 模型加载中 |
| (existing job) | cuda:1 | 42911 MiB | 不受影响 |

C009 md5 ✓，C006 lora_alpha=32 ✓，C004 显式 CUDA_VISIBLE_DEVICES ✓，C001/C002 GPU 空闲已确认 ✓。

**预估完成时间：** GSM8K 1319 道题，14B 模型 batch_size=2，约 40-60 分钟，预计 ~12:40-13:00 CST。

日志路径：`/tmp/eval_q14b_d{000,005,025}_gsm8k.log`

---
