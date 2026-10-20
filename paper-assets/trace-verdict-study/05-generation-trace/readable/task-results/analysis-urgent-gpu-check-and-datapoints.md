# analysis urgent gpu check and datapoints

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_urgent_gpu_check_and_datapoints_20260518T234723_result.json`
- **Structured JSON:** [`26afd34bdc20dca7c21b.json`](../../sessions/26/26afd34bdc20dca7c21b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

收割完成。汇总如下：

---

```
Q1 nvidia-smi:
  cuda:0 — 空闲 (49175MiB占用, 0% util, 28°C, P8) — 无计算进程
  cuda:1 — 满载 (40126MiB, 100% util, 72°C, P0) — PID 473809 codellama13b训练中

Q2 seed123_v2:
  已完成 ✓  accuracy = 99.83% (CI: [99.58%, 100.0%])
  pass: P=1.00 R=1.00 F1=1.00 | fail: P=0.99 R=1.00 F1=1.00
  → 已收割到 registry (status=DONE, conclusion=success)

Q3 cuda:1:
  codellama13b_full_trace_tail512_seed456 训练中, step 157/444 (~35%)
  tmux session 存活, 预计还需 ~1.5h

Q4 收割:
  qwen15b_exception_only_seed123_v2 — 已收割, accuracy=99.83%
  codellama13b_full_trace_tail512_seed456 — 仍在训练, 无eval结果
```

---

**数据点核实：**

```
CodeLlama-13B tail-512 seed42: ❌ Registry 中不存在
  - 存在 codellama13b_vota_seed42 (RUNNING, 无metrics)
  - 存在 codellama13b_exception_only_seed42 (RUNNING, 无metrics)
  - 无任何 codellama + tail_512 + seed42 的实验

DeepSeek tail-512 seed42: ⚠️ Registry 中无 metrics 字段
  - deepseek_full_trace_seed42_v3 (PREPARING, 无metrics)
  - notes 中提到 "79.16% confirmed with max_length=2048"
  - 但 accuracy 未正式录入 registry metrics
```

两个数据点都不在 registry metrics 中。DeepSeek 那个 79.16% 只记在 notes 里。CodeLlama tail-512 seed42 完全没有对应实验。

---
