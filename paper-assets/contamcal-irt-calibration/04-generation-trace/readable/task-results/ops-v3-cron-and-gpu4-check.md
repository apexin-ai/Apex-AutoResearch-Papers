# ops v3 cron and gpu4 check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_v3_cron_and_gpu4_check_20260514T032745_result.json`
- **Structured JSON:** [`beea964a95e0178d6e69.json`](../../sessions/be/beea964a95e0178d6e69.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### 任务 1: exp_005_noise_prop_v3

- **进程**：无 `noise_prop` 进程在运行
- **输出**：服务器上不存在 `artifacts/exp005_noise_propagation/` 目录，无任何输出文件或日志
- **判断**：该实验 spec 记录的 `server: local`（非 cqa1-21977），且 PID 339838 已不存在。实验从未在此服务器上运行，或在 local 机器上已终止且未产出结果
- **操作**：已将 registry 更新为 `conclusion: negative`, `status: DONE`
- **cron 监控**：`register_cron` 工具不可用，且实验已结束无需注册

### 任务 2: cuda:4 空闲检查

- **cuda:4 并非空闲**：PID 271921 正在 GPU 4 上运行，占用 18538 MiB 显存
- **PID 关系**：
  - PID 271916 = bash wrapper（`exp_001_sft_d005_15B` 的启动壳，设置了 `CUDA_VISIBLE_DEVICES=4`）
  - PID 271921 = 实际 python 子进程（`train_sft.py`，Qwen2.5-1.5B，d005 dosage）
- **结论**：资源面板显示 cuda:4 空闲是因为 registry 未记录 GPU 字段。实际上 `exp_001_sft_d005_15B` 正在独占 GPU 4。

---
