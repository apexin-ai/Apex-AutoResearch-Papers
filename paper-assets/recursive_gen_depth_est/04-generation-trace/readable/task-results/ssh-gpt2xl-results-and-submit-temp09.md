# ssh gpt2xl results and submit temp09

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpt2xl_results_and_submit_temp09_20260514T182600_result.json`
- **Structured JSON:** [`c3234df437079bc646e7.json`](../../sessions/c3/c3234df437079bc646e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPT-2 XL temp09 已在 cuda:1 上成功启动，正在训练 Step 1 (depth-0 finetune)，~1.33 it/s。

## 汇总

### Part 1: GPT-2 XL nucleus (cross_model_gpt2xl_001)
- **Status**: DONE / success
- **数据**: 4 depth × 5000 samples = 20000 条，全部生成完成
- **Checkpoints**: lora_depth_0/1/2 均存在 (~27MB each)
- **Finetune loss**: depth_0=2.550, depth_1=1.715, depth_2=1.342 (递减趋势正常，与 Pythia baseline 一致)
- **分类/AUC**: **未运行** — pipeline 脚本仅含 finetune+generate，需单独执行 extract_features → train_classifier → filter_code
- **Cron**: 不存在（已无需删除）

### Part 2: GPT-2 XL temp09 (gpt2xl_temp09_001)
- **Status**: RUNNING on cuda:1 (PID 168793)
- **GPU**: cuda:1 占用 34979 MiB / 100% 利用率
- **进度**: Step 1 depth-0 finetune 进行中，37/939 steps (~1.33 it/s)
- **预估总时长**: ~3.5-4h (参考 nucleus pipeline 3.76 GPU-hours)

---
